#!/usr/bin/env python3
"""REG-006 harvest: the annual firm-year panel of L, G, W.

Registered in REG-006 §2 before this file existed. Computes NO statistic --
it writes a panel and stops. Every ladder lives in wt092_sequencing_vs_coupling.py.

Panel rule, registered: annual duration facts (350-380 day span) from 10-K forms,
deduplicated by preferring facts the SEC itself framed; instants (Assets, Goodwill)
taken at the START of the fiscal year, i.e. the prior year end.

Runs in the cloud. darwin's disk is at 95%.
"""
from __future__ import annotations

import csv, io, json, os, pathlib, sys, time, urllib.request, zipfile
import datetime as dt
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
UA = {"User-Agent": "jason c braatz jasoncbraatz@gmail.com"}

# --- REG-006 §1: the CORRECTED tier-0 list. The registered list named an element
# --- that does not exist. This is the amendment, registered before it ran.
TIER_TAGS = {
    0: ("ImpairmentOfLongLivedAssetsHeldForUse",      # <- the element that EXISTS
        "TangibleAssetImpairmentCharges",
        "ImpairmentOfLeasehold"),
    1: ("ImpairmentOfIntangibleAssetsFinitelived",),
    2: ("ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill",),
    3: ("GoodwillImpairmentLoss",),
}
DEAD_TAG = "ImpairmentOfLongLivedAssetsHeldAndUsed"   # kept ONLY as F1's witness
COMBINED_TAG = "GoodwillAndIntangibleAssetImpairment"
AGG_TAG = "AssetImpairmentCharges"
ASSETS_TAG = "Assets"
GOODWILL_TAG = "Goodwill"
SEGMENT_TAG = "NumberOfReportableSegments"

L_TAGS = TIER_TAGS[0] + TIER_TAGS[1] + TIER_TAGS[2]
G_TAG = "GoodwillImpairmentLoss"
ALL_DURATION = tuple(set(L_TAGS + (G_TAG, COMBINED_TAG, AGG_TAG, DEAD_TAG)))

PILOT_SIC = (5200, 5999)
REPLICATION_SIC = (7370, 7379)
SUB_QUARTERS = [f"{y}q2" for y in range(2013, 2025)]


def _get(url: str, retries: int = 4) -> bytes:
    last = None
    for i in range(retries):
        try:
            r = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(r, timeout=90).read()
        except Exception as e:  # noqa: BLE001
            last = e
            if "404" in str(e):
                raise
            time.sleep(1.0 + 1.5 * i)
    raise last


def build_universe() -> dict[int, tuple[str, int]]:
    """CIK -> (name, sic) for both registered SIC ranges. Same route as wt089_harvest."""
    cache = HERE / "universe.json"
    if cache.exists():
        return {int(k): tuple(v) for k, v in json.loads(cache.read_text()).items()}
    found: dict[int, tuple[str, int]] = {}
    for q in SUB_QUARTERS:
        try:
            raw = _get("https://www.sec.gov/files/dera/data/"
                       f"financial-statement-data-sets/{q}.zip")
            with zipfile.ZipFile(io.BytesIO(raw)) as z, z.open("sub.txt") as fh:
                for row in csv.DictReader(
                        io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t"):
                    sic = row.get("sic") or ""
                    if not sic.isdigit():
                        continue
                    s = int(sic)
                    if (PILOT_SIC[0] <= s <= PILOT_SIC[1]
                            or REPLICATION_SIC[0] <= s <= REPLICATION_SIC[1]):
                        found[int(row["cik"])] = (row.get("name", ""), s)
            print(f"  {q}: universe now {len(found)}", flush=True)
        except Exception as exc:  # noqa: BLE001
            print(f"  {q}: SKIPPED ({exc})", flush=True)
    cache.write_text(json.dumps({str(k): list(v) for k, v in found.items()}))
    return found


def _annual(node: dict) -> dict[str, float]:
    """{fiscal-year-end ISO date: value} from annual duration facts."""
    out: dict[str, float] = {}
    framed: set[str] = set()
    for unit, rows in node.get("units", {}).items():
        if unit != "USD":
            continue
        for r in rows:
            s, e = r.get("start"), r.get("end")
            if not s or not e:
                continue
            try:
                span = (dt.date.fromisoformat(e) - dt.date.fromisoformat(s)).days
            except ValueError:
                continue
            if not (350 <= span <= 380):
                continue
            if not str(r.get("form", "")).startswith("10-K"):
                continue
            has_frame = "frame" in r
            if e in out and not has_frame and e in framed:
                continue          # a framed value already won this year
            out[e] = float(r["val"])
            if has_frame:
                framed.add(e)
    return out


def _instant(node: dict, fy_only: bool = False) -> dict[str, float]:
    """Instant facts. With fy_only, restrict to fiscal-YEAR-END balance dates:
    10-K filings with fp == 'FY'. Without that filter the series carries every
    quarterly comparative and a 'firm-year' row would be a firm-QUARTER row."""
    out: dict[str, float] = {}
    framed: set[str] = set()
    for unit, rows in node.get("units", {}).items():
        if unit != "USD":
            continue
        for r in rows:
            e = r.get("end")
            if not e or r.get("start"):
                continue
            if fy_only and not (str(r.get("form", "")).startswith("10-K")
                                and r.get("fp") == "FY"):
                continue
            has_frame = "frame" in r
            if e in out and not has_frame and e in framed:
                continue
            out[e] = float(r["val"])
            if has_frame:
                framed.add(e)
    return out


def _prior_year(iso: str) -> str | None:
    try:
        d = dt.date.fromisoformat(iso)
    except ValueError:
        return None
    try:
        return (d.replace(year=d.year - 1)).isoformat()
    except ValueError:
        return (d.replace(year=d.year - 1, day=28)).isoformat()


def _nearest(series: dict[str, float], target: str, tol_days: int = 20):
    if target in series:
        return series[target]
    try:
        t = dt.date.fromisoformat(target)
    except ValueError:
        return None
    best, bd = None, tol_days + 1
    for k, v in series.items():
        try:
            d = abs((dt.date.fromisoformat(k) - t).days)
        except ValueError:
            continue
        if d < bd:
            best, bd = v, d
    return best


def firm_panel(item):
    cik, (name, sic) = item
    try:
        raw = _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json")
    except Exception:
        return None
    try:
        gaap = json.loads(raw).get("facts", {}).get("us-gaap", {})
    except Exception:
        return None

    dur = {t: _annual(gaap[t]) for t in ALL_DURATION if t in gaap}
    assets = _instant(gaap[ASSETS_TAG], fy_only=True) if ASSETS_TAG in gaap else {}
    goodwill = _instant(gaap[GOODWILL_TAG], fy_only=True) if GOODWILL_TAG in gaap else {}
    segs = _instant(gaap[SEGMENT_TAG]) if SEGMENT_TAG in gaap else {}
    if not segs and SEGMENT_TAG in gaap:
        segs = {}
    nseg = None
    for _n in gaap.get(SEGMENT_TAG, {}).get("units", {}).values():
        vals = [r["val"] for r in _n if r.get("val") is not None]
        if vals:
            nseg = float(sorted(vals)[len(vals) // 2])
        break

    # fiscal-year ends: the ANNUAL duration facts, plus every FY-end balance date.
    years = set()
    for t in dur:
        years |= set(dur[t])
    years |= set(assets)
    rows = []
    for ye in sorted(years):
        if not ("2013-01-01" <= ye <= "2025-06-30"):
            continue
        py = _prior_year(ye)
        A = _nearest(assets, py) if py else None
        W = _nearest(goodwill, py) if py else None
        if A is None or A <= 0:
            continue
        tier = {k: sum(dur.get(t, {}).get(ye, 0.0) for t in tags)
                for k, tags in TIER_TAGS.items()}
        rows.append({
            "fy_end": ye,
            "L": tier[0] + tier[1] + tier[2],
            "t0": tier[0], "t1": tier[1], "t2": tier[2],
            "G": tier[3],
            "G_present": G_TAG in dur and ye in dur[G_TAG],
            "combined": dur.get(COMBINED_TAG, {}).get(ye, 0.0),
            "agg": dur.get(AGG_TAG, {}).get(ye, 0.0),
            "dead": dur.get(DEAD_TAG, {}).get(ye, 0.0),
            "W": W, "A": A,
        })
    if not rows:
        return None
    return {"cik": int(cik), "name": name, "sic": sic, "n_segments": nseg,
            "universe": "pilot" if PILOT_SIC[0] <= sic <= PILOT_SIC[1] else "replication",
            "rows": rows}


if __name__ == "__main__":
    print("[1/2] building universe from SEC financial statement data sets", flush=True)
    uni = build_universe()
    print(f"  universe: {len(uni)} registrants", flush=True)

    print("[2/2] harvesting annual panel from companyfacts", flush=True)
    out, n = [], 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        for res in ex.map(firm_panel, list(uni.items())):
            n += 1
            if res:
                out.append(res)
            if n % 100 == 0:
                print(f"  {n}/{len(uni)}  firms with panel: {len(out)}", flush=True)
    json.dump(out, open(HERE / "wt092-panel.json", "w"))
    nrows = sum(len(f["rows"]) for f in out)
    print(f"\nDONE  firms={len(out)}  firm-years={nrows}", flush=True)
