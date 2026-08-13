#!/usr/bin/env python3
"""REG-009 §2 · P0 — the pre-condition probe: the disclosed life VALUES.

NOT A REGISTRATION AND NOT A RESULT. A pre-condition probe, declared and priced in
REG-009 §2 before it was written, and the thing standing between REG-009 §1 and its
§§2-8. It reports numbers. It does NOT choose D2, D3 or D4 -- those are fixed in
REG-009 §2 in a later commit, citing this probe's table. A probe that both measures the
choice and makes it is the shape SOURCE-001 §4c spent a session unwinding.

WHY A RE-READ AND NOT A GROUPBY. `data/source-001-lifetime-by-fyend*.json` carries, per
firm-year, four booleans and a COUNT of tag occurrences. `source001_lifetime_by_fyend.
scan_zip()` filters `txt.tsv` on the tag NAME and never opens a value column. It answers
"was a life tagged", not "what was the life". The two are indistinguishable from the
filename and from every prose reference in the repository, which is why REG-009 §5 keeps
the error: this probe's price was checked rather than assumed.

WHAT IT REPORTS
  P0-a  STICKINESS   -- within-firm dispersion of the disclosed life across years.
                        Paper III §4.7's bound 2, measured for the first time. Reported
                        at TWO horizons, because the bound is stated "across the horizon
                        over which timeliness is measured" and the panel's horizon is
                        2013-2025:
                          a1 · adjacent years  (consecutive fiscal year ends)
                          a2 · the decade      (the 2014-15 cycle against the 2022-23 one)
                        The never-changed share is stated separately from the moved-once
                        share, as §2 requires.
  P0-b  ANCHORING    -- within-SIC dispersion against the cross-SIC total. §4.7's bounds
                        1 and 3 together: "anchored by industry convention" and "can be
                        run on industry-median lives" are one claim measured from two
                        sides.
  P0-c  DISPERSION   -- within-band dispersion of the IMPLIED delta = 1/L, swept over
                        band width, per interval->point rule, fed into §4.4's COMMITTED
                        simulation (extracted from `wt088_disclosed_ladder.py` at run
                        time, never re-implemented) to yield a recovery probability per
                        band width. This is D3's ruler and the input REG-009 §1.4 says
                        has never been computed.

GUARDS CARRIED AS CODE, not as memory (REG-009 §2):
  * THIN refuses any band or SIC cell under --thin firm-years (§3b's guard, §4b's mistake).
  * Every quoted gap carries a two-proportion z or its continuous analogue (a paired
    bootstrap over FIRMS, so a firm contributing many rows cannot vote many times).
  * No comparison is printed between two cells whose own rates this file has just
    refused -- SOURCE-001 §4c's incoherent-guard find, promoted to an assertion.
  * Every median is printed with its IQR beside it, and a median whose IQR spans an
    order of magnitude is reported as TWO POPULATIONS rather than one -- REG-009 §5's
    "what I would do differently", promoted from a lesson to a mechanism.
  * NO SILENT CAPS: every row this probe declines to use is counted and named.

Usage:
    reg009_p0_lifetime_values.py extract ZIP [ZIP ...] --cycle NAME --out FILE
                                [--window-start YYYYMMDD] [--window-end YYYYMMDD]
    reg009_p0_lifetime_values.py report  RECORDS.json [RECORDS.json ...]
                                [--thin N] [--out FILE]

Runs in the CLOUD, not on darwin -- settled four times; see the handoff. The zips are
inputs to `extract`, so `report` is offline and rerunnable, and the committed records are
auditable without re-reading 7.5 GB.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import math
import pathlib
import re
import statistics
import sys
import zipfile
from collections import Counter, defaultdict

import numpy as np

csv.field_size_limit(10_000_000)
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
PANEL = ROOT / "data" / "reg-006-wt092-panel.json"
LADDER_SRC = HERE / "wt088_disclosed_ladder.py"

sys.path.insert(0, str(HERE))
# Registered machinery, imported rather than copied: the firm-year join is §3b's and any
# drift between the two would be a silent redefinition of "covered".
from source001_lifetime_by_fyend import (  # noqa: E402
    CANON, FUZZ_DAYS, MONTHS, candidate_periods, ztest,
)

# --------------------------------------------------------------------------------------
# P0's OWN construction decisions. These are NOT D2/D3/D4 -- they are the choices a
# reader needs in order to know what was measured, and each is declared here rather than
# discovered in the code.
# --------------------------------------------------------------------------------------
# C1 · tag set: §3b's two canonical tags only. Every other `*UsefulLife*` tag is counted
#      and named in the extract's `excluded_tags`, because a tag set is a coverage claim.
# C2 · period: a row counts for a firm-year only when its `ddate` equals the submission's
#      own `period`. Other ddates are prior-period comparatives -- the same firm at an
#      EARLIER year end -- and are kept SEPARATELY as `comparatives`, where P0-a1 uses
#      them rather than throwing them away.
# C3 · duplicates: keep the lowest `iprx` per (adsh, tag, ddate, dimh); count the rest.
# C4 · Range=WeightedAverage is a POINT, not an interval endpoint. Counted.
# C5 · component = the first non-Range dimension member; a row with no dimension is the
#      entity-level disclosure and gets the component `__ENTITY__`.
# C6 · an interval is a (Minimum, Maximum) pair on the SAME (adsh, tag, component). A
#      component carrying only one endpoint is a HALF-INTERVAL and each D2 rule below
#      states what it does with one.
RANGE_MIN, RANGE_MAX, RANGE_WAVG = "Minimum", "Maximum", "WeightedAverage"
ENTITY = "__ENTITY__"

# The four decay rates §4.4 attributes to the standards bracket the model's domain, and
# the domain is the binding constraint: R is defined only for delta < alpha. §5.4's
# MEASURED recognition rate is what puts the disclosed rectangle inside it at all.
ALPHA_MEASURED = 0.408          # §5.4, 95% interval [0.383, 0.432]
ALPHA_CALIBRATED = 0.05         # §4.4's calibration, kept for the domain report only

ISO_DUR = re.compile(r"^P(?:(\d+(?:\.\d+)?)Y)?(?:(\d+(?:\.\d+)?)M)?(?:(\d+(?:\.\d+)?)W)?"
                     r"(?:(\d+(?:\.\d+)?)D)?$")


def parse_years(v: str) -> float | None:
    """ISO-8601 duration -> years. Returns None on anything this does not understand,
    and the caller COUNTS those rather than dropping them quietly."""
    v = (v or "").strip()
    m = ISO_DUR.match(v)
    if not m or v == "P":
        return None
    y, mo, w, d = (float(g) if g else 0.0 for g in m.groups())
    yrs = y + mo / 12.0 + w * 7.0 / 365.25 + d / 365.25
    return yrs if yrs > 0 else None


def iqr(xs: list[float]) -> tuple[float, float]:
    if not xs:
        return (float("nan"), float("nan"))
    a = sorted(xs)
    return (float(np.percentile(a, 25)), float(np.percentile(a, 75)))


def med_iqr(xs: list[float], label: str = "") -> str:
    """A median is never printed without its IQR, and an IQR spanning an order of
    magnitude is reported as two populations rather than one (REG-009 §2)."""
    if not xs:
        return f"{label}n=0"
    m = float(statistics.median(xs))
    lo, hi = iqr(xs)
    s = f"{m:.3f} [IQR {lo:.3f}-{hi:.3f}]  n={len(xs)}"
    if lo > 0 and hi / lo >= 10.0:
        s += "  ** IQR SPANS AN ORDER OF MAGNITUDE -- read as two populations, not one **"
    return label + s


# ======================================================================================
# EXTRACT
# ======================================================================================
def load_panel() -> list[dict]:
    return json.loads(PANEL.read_text())


def scan_zip_values(path: str, panel_ciks: set[int], tally: Counter) -> tuple[dict, list]:
    """Return (subs, rows) where rows carry the life VALUE, its component and its Range.

    The sibling `scan_zip()` answers *was a life tagged*. This answers *what was the
    life*, which is a different file (`dim.tsv`) and a different column (`value`).
    """
    z = zipfile.ZipFile(path)
    subs: dict[str, dict] = {}
    with z.open("sub.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        ix = {n: i for i, n in enumerate(next(rd))}
        for row in rd:
            if len(row) <= ix["period"] or row[ix["form"]] != "10-K":
                continue
            try:
                cik = int(row[ix["cik"]])
            except (ValueError, TypeError):
                continue
            if cik not in panel_ciks:
                continue
            subs[row[ix["adsh"]]] = {"cik": cik, "period": row[ix["period"]],
                                     "filed": row[ix["filed"]], "sic_sub": row[ix["sic"]]}

    raw: list[tuple] = []
    need: set[str] = set()
    with z.open("txt.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        ix = {n: i for i, n in enumerate(next(rd))}
        for row in rd:
            if len(row) <= ix["value"]:
                continue
            tag = row[ix["tag"]]
            if "UsefulLife" not in tag:
                continue
            if row[ix["adsh"]] not in subs:
                continue
            if tag not in CANON:                                   # C1
                tally[f"excluded_tag:{tag}"] += 1
                continue
            raw.append((row[ix["adsh"]], tag, row[ix["ddate"]], row[ix["dimh"]],
                        int(row[ix["iprx"]] or 0), row[ix["value"]]))
            need.add(row[ix["dimh"]])

    dim: dict[str, str] = {}
    with z.open("dim.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        next(rd)
        for row in rd:
            if row and row[0] in need:
                dim[row[0]] = row[1] if len(row) > 1 else ""

    # C3 · dedupe on the lowest iprx
    best: dict[tuple, tuple] = {}
    for adsh, tag, ddate, dimh, iprx, value in raw:
        k = (adsh, tag, ddate, dimh)
        if k not in best or iprx < best[k][0]:
            if k in best:
                tally["dupe_iprx_dropped"] += 1
            best[k] = (iprx, value)
        else:
            tally["dupe_iprx_dropped"] += 1

    rows = []
    for (adsh, tag, ddate, dimh), (_iprx, value) in best.items():
        yrs = parse_years(value)
        if yrs is None:
            tally["unparseable_duration"] += 1
            tally[f"unparseable:{value[:24]}"] += 1
            continue
        seg = dim.get(dimh, "")
        parts = [p for p in seg.split(";") if p and "=" in p]
        rng, comp = "", ""
        for p in parts:
            ax, _, mem = p.partition("=")
            if ax == "Range":
                rng = mem
            elif not comp:
                comp = mem                                          # C5
        rows.append({"adsh": adsh, "tag": tag, "ddate": ddate,
                     "component": comp or ENTITY, "range": rng, "years": yrs})
        tally["rows_kept"] += 1
        tally[f"range:{rng or 'NONE'}"] += 1
    print(f"  {pathlib.Path(path).name}: {len(subs)} panel 10-Ks, "
          f"{len(rows)} canonical life values", flush=True)
    return subs, rows


# ---- D2's three candidate interval->point rules, run SIDE BY SIDE in one pass so a rule
#      cannot be discovered and then re-chosen (REG-009 §2). --------------------------
def _component_points(rows: list[dict]) -> dict[str, dict]:
    """component -> {mid, lo, hi, kind} for one (firm-year, tag)."""
    by: dict[str, dict] = defaultdict(lambda: {"min": [], "max": [], "point": []})
    for r in rows:
        b = by[r["component"]]
        if r["range"] == RANGE_MIN:
            b["min"].append(r["years"])
        elif r["range"] == RANGE_MAX:
            b["max"].append(r["years"])
        else:                                                       # C4: WAVG is a point
            b["point"].append(r["years"])
    out = {}
    for comp, b in by.items():
        lo = min(b["min"]) if b["min"] else None
        hi = max(b["max"]) if b["max"] else None
        pts = b["point"]
        if lo is not None and hi is not None:
            kind = "interval"
        elif lo is not None or hi is not None:
            kind = "half_interval"                                  # C6
        elif pts:
            kind = "point"
        else:
            continue
        if kind == "point":
            lo = hi = float(statistics.median(pts))
        elif kind == "half_interval":
            v = lo if lo is not None else hi
            lo = hi = float(v)
        out[comp] = {"lo": float(lo), "hi": float(hi), "kind": kind,
                     "mid": float((lo + hi) / 2.0)}
    return out


def firm_year_lives(rows: list[dict], weights: dict | None = None) -> dict:
    """The three D2 candidates for one firm-year, per canonical tag.

    R_MID    · per component, the midpoint of [min,max]; median across components.
    R_MIN    · per component, the SHORTEST endpoint (the fastest delta); median across.
    R_WEIGHT · components weighted by gross carrying amount where the filing supplies one;
               falls back to R_MID for the components it cannot weight, and the fallback
               SHARE IS REPORTED rather than absorbed.
    """
    out: dict[str, dict] = {}
    for tag in CANON:
        tr = [r for r in rows if r["tag"] == tag]
        if not tr:
            continue
        comps = _component_points(tr)
        if not comps:
            continue
        mids = [c["mid"] for c in comps.values()]
        los = [c["lo"] for c in comps.values()]
        w = (weights or {}).get(tag, {})
        num = den = 0.0
        weighted_comps = 0
        for comp, c in comps.items():
            wt = w.get(comp)
            if wt and wt > 0:
                num += wt * c["mid"]
                den += wt
                weighted_comps += 1
        out[tag] = {
            "R_MID": float(statistics.median(mids)),
            "R_MIN": float(statistics.median(los)),
            "R_WEIGHT": float(num / den) if den > 0 else float(statistics.median(mids)),
            "R_WEIGHT_backed": den > 0,
            "weighted_components": weighted_comps,
            "n_components": len(comps),
            "kinds": Counter(c["kind"] for c in comps.values()),
            "components": {k: round(v["mid"], 4) for k, v in comps.items()},
        }
    return out


def scan_zip_weights(path: str, adshs: set[str], comps_needed: set[str]) -> dict:
    """Gross carrying amounts per component, for D2's component-weighted candidate.

    Read from `num.tsv` -- the numeric file the FIRST FSN scan reached for and the reason
    §3a's coverage came back worse when the surface got bigger. It is the right file for
    an AMOUNT and the wrong one for a DURATION, and both halves of that are load-bearing.
    """
    WTAGS = {"PropertyPlantAndEquipmentGross": CANON[0],
             "PropertyPlantAndEquipmentNet": CANON[0],
             "FiniteLivedIntangibleAssetsGross": CANON[1],
             "FiniteLivedIntangibleAssetsNet": CANON[1]}
    z = zipfile.ZipFile(path)
    need: set[str] = set()
    hits: list[tuple] = []
    with z.open("num.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        ix = {n: i for i, n in enumerate(next(rd))}
        for row in rd:
            if len(row) <= ix["value"]:
                continue
            tag = row[ix["tag"]]
            if tag not in WTAGS or row[ix["adsh"]] not in adshs:
                continue
            if not row[ix["dimh"]]:
                continue
            try:
                val = float(row[ix["value"]])
            except (ValueError, TypeError):
                continue
            if val <= 0:
                continue
            hits.append((row[ix["adsh"]], WTAGS[tag], row[ix["dimh"]], val, tag))
            need.add(row[ix["dimh"]])
    dim: dict[str, str] = {}
    with z.open("dim.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        next(rd)
        for row in rd:
            if row and row[0] in need:
                dim[row[0]] = row[1] if len(row) > 1 else ""
    out: dict = defaultdict(lambda: defaultdict(dict))
    for adsh, tag, dimh, val, _src in hits:
        seg = dim.get(dimh, "")
        parts = [p for p in seg.split(";") if p and "=" in p]
        if any(p.startswith("Range=") for p in parts):
            continue
        comp = parts[0].partition("=")[2] if parts else ""
        if not comp or comp not in comps_needed:
            continue
        prev = out[adsh][tag].get(comp, 0.0)
        out[adsh][tag][comp] = max(prev, val)
    return {a: {t: dict(c) for t, c in v.items()} for a, v in out.items()}


def cmd_extract(args: argparse.Namespace) -> int:
    panel = load_panel()
    panel_ciks = {int(f["cik"]) for f in panel}
    sic_of = {int(f["cik"]): f.get("sic") for f in panel}
    name_of = {int(f["cik"]): f.get("name") for f in panel}

    tally: Counter = Counter()
    subs: dict[str, dict] = {}
    rows_by_adsh: dict[str, list] = defaultdict(list)
    for p in args.zips:
        s, rows = scan_zip_values(p, panel_ciks, tally)
        subs.update(s)
        for r in rows:
            rows_by_adsh[r["adsh"]].append(r)

    # component-weighted candidate needs amounts from the same zips
    comps_needed = {r["component"] for rs in rows_by_adsh.values() for r in rs}
    weights: dict[str, dict] = {}
    if not args.no_weights:
        for p in args.zips:
            w = scan_zip_weights(p, set(rows_by_adsh), comps_needed)
            for a, v in w.items():
                weights.setdefault(a, {})
                for t, c in v.items():
                    weights[a].setdefault(t, {}).update(c)
            print(f"  {pathlib.Path(p).name}: component amounts for {len(w)} filings",
                  flush=True)

    w0 = dt.datetime.strptime(args.window_start, "%Y%m%d").date()
    w1 = dt.datetime.strptime(args.window_end, "%Y%m%d").date()
    by_key: dict[tuple, list[str]] = defaultdict(list)
    for adsh, s in subs.items():
        by_key[(s["cik"], s["period"])].append(adsh)

    records: list[dict] = []
    comparatives: list[dict] = []
    for f in panel:
        cik = int(f["cik"])
        for r in f["rows"]:
            try:
                fe = dt.datetime.strptime(r["fy_end"], "%Y-%m-%d").date()
            except (ValueError, TypeError, KeyError):
                continue
            if not (w0 <= fe <= w1):
                continue
            tally["panel_firm_years_in_window"] += 1
            hit = None
            for i, per in enumerate(candidate_periods(fe)):
                if (cik, per) in by_key:
                    hit = by_key[(cik, per)][0]
                    if i:
                        tally["fuzz_used"] += 1
                    break
            if hit is None:
                tally["no_submission"] += 1
                continue
            tally["submission_found"] += 1
            allrows = rows_by_adsh.get(hit, [])
            period = subs[hit]["period"]
            own = [x for x in allrows if x["ddate"] == period]        # C2
            prior = [x for x in allrows if x["ddate"] != period]
            tally["rows_own_period"] += len(own)
            tally["rows_prior_period_comparative"] += len(prior)
            if not own:
                tally["submission_no_life_value"] += 1
                continue
            lives = firm_year_lives(own, weights.get(hit))
            if not lives:
                tally["submission_no_life_value"] += 1
                continue
            tally["firm_years_with_a_life"] += 1
            records.append({
                "cik": cik, "name": name_of.get(cik), "sic": sic_of.get(cik),
                "fy_end": r["fy_end"], "adsh": hit, "period": period,
                "cycle": args.cycle,
                "lives": {t: {k: v for k, v in d.items() if k != "kinds"}
                          for t, d in lives.items()},
                "kinds": {t: dict(d["kinds"]) for t, d in lives.items()},
            })
            for pd_ in sorted({x["ddate"] for x in prior}):
                sub_rows = [x for x in prior if x["ddate"] == pd_]
                pl = firm_year_lives(sub_rows, None)
                if pl:
                    comparatives.append({
                        "cik": cik, "sic": sic_of.get(cik), "adsh": hit,
                        "ddate": pd_, "cycle": args.cycle,
                        "lives": {t: {k: v for k, v in d.items() if k != "kinds"}
                                  for t, d in pl.items()}})

    print(f"\ncycle {args.cycle}: {tally['panel_firm_years_in_window']} panel firm-years "
          f"in [{w0} .. {w1}]")
    for k in ("submission_found", "no_submission", "submission_no_life_value",
              "firm_years_with_a_life", "rows_own_period",
              "rows_prior_period_comparative", "dupe_iprx_dropped",
              "unparseable_duration", "fuzz_used"):
        print(f"  {k:<34} {tally[k]}")
    print("  NO SILENT CAPS -- every declined row is counted above and named in the "
          "artifact's `tally`.")

    pathlib.Path(args.out).write_text(json.dumps({
        "cycle": args.cycle,
        "zips": [pathlib.Path(p).name for p in args.zips],
        "window": [args.window_start, args.window_end],
        "fuzz_days": FUZZ_DAYS,
        "canon": list(CANON),
        "alpha_measured": ALPHA_MEASURED,
        "tally": dict(tally),
        "records": records,
        "comparatives": comparatives,
    }, indent=1))
    print(f"\nwrote {args.out}  ({len(records)} firm-year records, "
          f"{len(comparatives)} prior-period comparatives -- both counts auditable "
          f"without re-reading the zips)")
    return 0


# ======================================================================================
# §4.4's COMMITTED SIMULATION, EXTRACTED AT RUN TIME
# ======================================================================================
# A drill that carries its own COPY of the logic under test passes forever while the
# original rots (claude-blackbook, 2026-08-08). So P0-c does not re-implement §4.4's
# recovery machinery -- it lifts the definitions out of `wt088_disclosed_ladder.py` by
# name and FAILS LOUDLY if the extraction stops matching or if the lifted code stops
# reproducing the three numbers §4.4 committed to print.
_LADDER_NAMES = ("closed_form", "kendall_tau", "strictly_increasing",
                 "strictly_decreasing", "draw_magnitude", "_common_delta_recovery")
_LADDER_CONSTS = ("ALPHA", "PHI_LO", "PHI_HI", "DELTA_LO", "DELTA_HI", "N", "SEED")

# §4.4's committed poles, quoted from paper III. If the extraction reproduces these, the
# lifted code IS the code the paper ran; if it does not, P0-c has no ruler and says so.
LADDER_POLES = {"independent": 0.115, "common": 1.000, "standards_ladder": 0.019}


def load_ladder() -> dict:
    src = LADDER_SRC.read_text()
    ns: dict = {"np": np}
    missing = []
    for c in _LADDER_CONSTS:
        # `wt088` declares some of these singly (`ALPHA = 0.05`) and some as tuple
        # assignments (`DELTA_LO, DELTA_HI = 0.001, 0.040`). Lift BOTH shapes, and if a
        # name matches neither, say so rather than silently substituting a default --
        # this guard already fired once on the tuple form, which is the whole point.
        m = re.search(rf"^{c}\s*=\s*(.+?)\s*(?:#.*)?$", src, re.M)
        if m:
            exec(f"{c} = {m.group(1)}", ns)                                # noqa: S102
            continue
        for mm in re.finditer(r"^([A-Za-z_][\w ]*(?:,\s*[A-Za-z_]\w*)+)\s*=\s*"
                              r"(.+?)\s*(?:#.*)?$", src, re.M):
            names = [x.strip() for x in mm.group(1).split(",")]
            if c in names:
                exec(f"{mm.group(1).strip()} = {mm.group(2)}", ns)         # noqa: S102
                break
        else:
            missing.append(c)
    for fn in _LADDER_NAMES:
        m = re.search(rf"^def {fn}\(.*?(?=\n(?:def |[A-Za-z_#@]|\Z))", src,
                      re.M | re.S)
        if not m:
            missing.append(f"def {fn}")
            continue
        exec(m.group(0), ns)                                               # noqa: S102
    if missing:
        raise SystemExit(
            "P0-c ABORTS: could not lift §4.4's simulation out of "
            f"{LADDER_SRC.name} -- missing {missing}. The ruler moved; re-derive the "
            "extraction rather than re-implementing the simulation here.")
    got = {
        "independent": round(ns["draw_magnitude"](ns["N"], ns["SEED"], False)[0], 3),
        "common": round(ns["_common_delta_recovery"](ns["SEED"]), 3),
        "standards_ladder": round(ns["draw_magnitude"](ns["N"], ns["SEED"], True)[0], 3),
    }
    bad = {k: (got[k], v) for k, v in LADDER_POLES.items() if abs(got[k] - v) > 0.002}
    if bad:
        raise SystemExit(
            "P0-c ABORTS: the lifted simulation no longer reproduces §4.4's committed "
            f"poles (got, expected): {bad}. Either the manuscript's numbers or the "
            "script drifted, and P0-c must not price a band width against a ruler that "
            "disagrees with the paper it is answering.")
    print("  §4.4's simulation lifted from wt088_disclosed_ladder.py and VERIFIED "
          "against its committed poles:")
    print(f"    delta independent {got['independent']:.3f} · delta common "
          f"{got['common']:.3f} · standards' falling ladder "
          f"{got['standards_ladder']:.3f}   (paper III §4.4: 0.115 / 1.000 / 0.019)")
    return ns


def recovery_from_deltas(deltas: np.ndarray, alpha: float, ns: dict,
                         n: int | None = None, seed: int | None = None) -> float:
    """§4.4's recovery probability with the delta support replaced by a MEASURED one.

    Everything else is §4.4's: the same phi draw, the same R, the same strict-monotone
    test, the same N and seed. The one substitution is the quantity REG-009 §1.4 says has
    never been computed -- the delta dispersion a life band actually leaves behind.
    """
    n = n or ns["N"]
    seed = ns["SEED"] if seed is None else seed
    rng = np.random.default_rng(seed)
    d_ok = deltas[deltas < alpha]
    if len(d_ok) < 2:
        return float("nan")
    hits = 0
    inc = ns["strictly_increasing"]
    for _ in range(n):
        phi = np.sort(rng.uniform(ns["PHI_LO"], ns["PHI_HI"], 4))[::-1]
        d = rng.choice(d_ok, 4)
        R = (1 - phi) * d / (alpha - d)
        if inc(R):
            hits += 1
    return hits / n


# ======================================================================================
# REPORT
# ======================================================================================
def boot_ci(vals: list[float], stat, groups: list, reps: int = 2000,
            seed: int = 20260813) -> tuple[float, float]:
    """A CLUSTERED bootstrap CI -- resampling FIRMS, not rows, so a firm contributing
    many firm-years cannot vote many times. This is the continuous analogue REG-009 §2
    demands wherever a gap is quoted and a two-proportion z does not apply."""
    rng = np.random.default_rng(seed)
    idx: dict = defaultdict(list)
    for i, g in enumerate(groups):
        idx[g].append(i)
    keys = list(idx)
    out = []
    for _ in range(reps):
        pick = rng.choice(len(keys), len(keys))
        sel = [i for k in pick for i in idx[keys[k]]]
        if len(sel) < 3:
            continue
        try:
            out.append(stat([vals[i] for i in sel]))
        except Exception:                                              # noqa: BLE001
            continue
    if not out:
        return (float("nan"), float("nan"))
    return (float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5)))


def _rule_life(rec: dict, tag: str, rule: str) -> float | None:
    d = rec.get("lives", {}).get(tag)
    return float(d[rule]) if d and d.get(rule) else None


def p0a(records: list[dict], comps: list[dict], tag: str, rule: str, thin: int) -> dict:
    """P0-a · STICKINESS, at two horizons."""
    obs: dict[int, dict[str, float]] = defaultdict(dict)
    for r in records:
        v = _rule_life(r, tag, rule)
        if v:
            obs[r["cik"]][r["fy_end"][:4] + "|" + r["cycle"]] = v
    for c in comps:
        d = c.get("lives", {}).get(tag)
        if d and d.get(rule):
            obs[c["cik"]].setdefault(c["ddate"][:4] + "|" + c["cycle"] + "|cmp",
                                     float(d[rule]))

    # a1 · adjacent years, from the comparatives inside a single filing plus any
    #      consecutive year ends the twelve zips happen to contain.
    adj: list[float] = []
    adj_firms: list[int] = []
    for cik, m in obs.items():
        yrs: dict[int, float] = {}
        for k, v in m.items():
            y = int(k.split("|")[0])
            yrs.setdefault(y, v)
        ys = sorted(yrs)
        for a, b in zip(ys, ys[1:]):
            if b - a == 1:
                adj.append(abs(math.log(yrs[b] / yrs[a])))
                adj_firms.append(cik)

    # a2 · the decade: the same firm in BOTH cycles. This is the horizon §4.7's bound
    #      actually names -- the panel's own 2013-2025 span -- and it is the reason P0
    #      reads two cycles rather than one.
    cyc: dict[int, dict[str, float]] = defaultdict(dict)
    for r in records:
        v = _rule_life(r, tag, rule)
        if v:
            cyc[r["cik"]].setdefault(r["cycle"], v)
    dec: list[float] = []
    dec_firms: list[int] = []
    dec_pairs: list[tuple] = []
    for cik, m in cyc.items():
        if len(m) >= 2:
            ks = sorted(m)
            dec.append(abs(math.log(m[ks[-1]] / m[ks[0]])))
            dec_firms.append(cik)
            dec_pairs.append((cik, m[ks[0]], m[ks[-1]]))

    # never-changed vs moved-once, stated separately (REG-009 §2)
    runs = Counter()
    for cik, m in obs.items():
        yrs: dict[int, float] = {}
        for k, v in m.items():
            yrs.setdefault(int(k.split("|")[0]), v)
        if len(yrs) < 3:
            continue
        seq = [yrs[y] for y in sorted(yrs)]
        moves = sum(1 for a, b in zip(seq, seq[1:]) if abs(math.log(b / a)) > 1e-9)
        runs["firms_with_3plus_observations"] += 1
        runs["never_changed" if moves == 0
             else "moved_once" if moves == 1 else "moved_more_than_once"] += 1

    def pack(vals, firms, label):
        if len(vals) < thin:
            return {"n": len(vals), "THIN": True, "label": label}
        return {"n": len(vals), "THIN": False, "label": label,
                "unchanged_share": float(np.mean([v <= 1e-9 for v in vals])),
                "within_10pct_share": float(np.mean([v <= math.log(1.10) for v in vals])),
                "median_abs_dlog": float(statistics.median(vals)),
                "iqr": iqr(vals),
                "ci_median": boot_ci(vals, lambda x: float(statistics.median(x)), firms),
                "vals": vals}
    # PER-COMPONENT, the confound removed. The firm-year figures above move when the
    # component MIX changes -- a firm that stops disclosing "Buildings" separately shifts
    # its own median without any life having been revised. Matching on the component
    # MEMBER STRING isolates the question §4.7's bound 2 actually asks: did THIS
    # disclosed life move? The cost is that only components present in both years count,
    # and that count is reported rather than absorbed.
    comp_obs: dict[tuple, dict[str, float]] = defaultdict(dict)
    for r in records:
        d = r.get("lives", {}).get(tag) or {}
        for comp, v in (d.get("components") or {}).items():
            if v:
                comp_obs[(r["cik"], comp)][r["cycle"]] = float(v)
    comp_dec, comp_firms = [], []
    for (cik, _comp), m in comp_obs.items():
        if len(m) >= 2:
            ks = sorted(m)
            comp_dec.append(abs(math.log(m[ks[-1]] / m[ks[0]])))
            comp_firms.append(cik)
    return {"adjacent": pack(adj, adj_firms, "adjacent years"),
            "decade": pack(dec, dec_firms, "2014-15 cycle vs 2022-23 cycle"),
            "decade_by_component": pack(comp_dec, comp_firms,
                                        "same firm, same component, decade apart"),
            "runs": dict(runs), "decade_pairs": dec_pairs[:40]}


def p0b(records: list[dict], tag: str, rule: str, thin: int) -> dict:
    """P0-b · INDUSTRY ANCHORING: within-SIC dispersion against the cross-SIC total.

    ratio = within-SIC sd of log L / total sd of log L. 1.00 says industry convention
    explains nothing; 0.00 says it explains everything. §4.7's bound 1 ("anchored by
    industry convention") and bound 3 ("can be run on industry-median lives, at the cost
    of resolution") are the same claim from two sides, and this ratio IS that cost.

    THE POINT ESTIMATE AND THE BOOTSTRAP RUN THE SAME ESTIMATOR. The first draft had two
    -- the point estimate applied the THIN rule and the bootstrap did not -- and the CI
    came back not bracketing its own point estimate, which is how the defect announced
    itself. A confidence interval computed on a different statistic than the one it is
    printed beside is worse than no interval at all.
    """
    rows = [(int(r["sic"]) // 100, float(_rule_life(r, tag, rule) or 0), r["cik"])
            for r in records if r.get("sic") and _rule_life(r, tag, rule)]
    rows = [(s_, v, c) for s_, v, c in rows if v > 0]
    if len(rows) < thin:
        return {"n": len(rows), "THIN": True}

    def estimate(sample: list[tuple]) -> dict:
        """sample: [(sic, life_years, cik)] -> the ratio and everything behind it."""
        by: dict[int, list[float]] = defaultdict(list)
        for s_, v, _c in sample:
            by[s_].append(math.log(v))
        kept = {s_: xs for s_, xs in by.items() if len(xs) >= thin}
        refused = {s_: len(xs) for s_, xs in by.items() if len(xs) < thin}
        if len(kept) < 2:
            return {}
        pooled = [x for xs in kept.values() for x in xs]
        total_sd = float(np.std(pooled, ddof=1))
        ss = n = 0.0
        for xs in kept.values():
            ss += float(np.var(xs, ddof=1)) * (len(xs) - 1)
            n += len(xs) - 1
        within_sd = math.sqrt(ss / n) if n else float("nan")
        return {"ratio": within_sd / total_sd if total_sd else float("nan"),
                "within_sd_log": within_sd, "total_sd_log": total_sd,
                "kept": kept, "refused": refused,
                "n_in_kept": sum(len(x) for x in kept.values())}

    pt = estimate(rows)
    if not pt:
        return {"n": len(rows), "THIN": True,
                "why": f"fewer than two SIC major groups clear the {thin} floor"}

    # clustered bootstrap over FIRMS, running the SAME estimator
    rng = np.random.default_rng(20260813)
    byfirm: dict[int, list[tuple]] = defaultdict(list)
    for r in rows:
        byfirm[r[2]].append(r)
    firms = list(byfirm)
    reps = []
    for _ in range(800):
        pick = rng.choice(len(firms), len(firms))
        samp = [r for k in pick for r in byfirm[firms[k]]]
        e = estimate(samp)
        if e and e["ratio"] == e["ratio"]:
            reps.append(e["ratio"])
    ci = ((float(np.percentile(reps, 2.5)), float(np.percentile(reps, 97.5)))
          if len(reps) >= 100 else (float("nan"), float("nan")))

    cells = {}
    for s_, xs in sorted(pt["kept"].items()):
        yrs = [math.exp(x) for x in xs]
        cells[s_] = {"n": len(xs), "sd_log": float(np.std(xs, ddof=1)),
                     "median_years": float(statistics.median(yrs)),
                     "iqr_years": iqr(yrs)}
    allyrs = [v for _s, v, _c in rows]
    return {"n": len(rows), "THIN": False,
            "total_sd_log": pt["total_sd_log"], "within_sd_log": pt["within_sd_log"],
            "ratio": pt["ratio"], "ratio_ci95": ci, "boot_reps": len(reps),
            "n_cells": len(cells), "cells": cells, "refused_cells": pt["refused"],
            "firm_years_in_kept_cells": pt["n_in_kept"],
            "kept_coverage": pt["n_in_kept"] / len(rows),
            "median_years_all": float(statistics.median(allyrs)),
            "iqr_years_all": iqr(allyrs)}


def p0c(records: list[dict], tag: str, rule: str, thin: int, ns: dict,
        widths: list[float], alpha: float) -> dict:
    """P0-c · WITHIN-BAND delta DISPERSION, SWEPT OVER BAND WIDTH. D3's ruler."""
    lives = [(float(_rule_life(r, tag, rule) or 0), r["cik"]) for r in records]
    lives = [(v, c) for v, c in lives if v > 0]
    if len(lives) < thin:
        return {"n": len(lives), "THIN": True}
    d_all = np.array([1.0 / v for v, _c in lives])
    out_of_domain = int((d_all >= alpha).sum())
    # HEAPING. A disclosed life is a round number far more often than an economic life
    # could be, so a narrow band can contain one distinct VALUE repeated many times.
    # Within-band delta dispersion then goes to zero by ARITHMETIC rather than by
    # economics, and §4.4's condition is met by the coarseness of the disclosure rather
    # than by the homogeneity of the assets. Measured here so the recovery numbers below
    # are read for what they are: an UPPER BOUND on the recovery the design would reach
    # if the disclosed life were the economic one -- which is exactly §4.7's weak joint,
    # unresolved, and therefore never to be quietly assumed by a table.
    vals = [v for v, _c in lives]
    ROUND = {3, 5, 7, 10, 15, 20, 25, 30, 39, 40, 50}
    heaping = {
        "distinct_values": len(set(round(v, 4) for v in vals)),
        "integer_share": float(np.mean([abs(v - round(v)) < 1e-6 for v in vals])),
        "round_number_share": float(np.mean([abs(v - round(v)) < 1e-6
                                             and round(v) in ROUND for v in vals])),
        "modal_share": float(max(Counter(round(v, 4) for v in vals).values()) / len(vals)),
        "top_values": Counter(round(v, 4) for v in vals).most_common(8),
    }
    poles = {
        "common_delta": float(ns["_common_delta_recovery"](ns["SEED"])),
        "whole_disclosed_range": recovery_from_deltas(d_all, alpha, ns),
    }
    sweep = []
    for w in widths:
        bands: dict[int, list] = defaultdict(list)
        for v, c in lives:
            bands[int(v // w)].append(v)
        rows, wsum, wn, worst = [], 0.0, 0, 1.0
        for b, vs in sorted(bands.items()):
            if len(vs) < thin:
                continue                                   # THIN: refused, not compared
            d = np.array([1.0 / x for x in vs])
            rec = recovery_from_deltas(d, alpha, ns)
            rows.append({"band": [b * w, (b + 1) * w], "n": len(vs),
                         "distinct_values": len(set(round(x, 4) for x in vs)),
                         "modal_share": float(max(Counter(round(x, 4)
                                                          for x in vs).values()) / len(vs)),
                         "median_years": float(statistics.median(vs)),
                         "iqr_years": iqr(vs),
                         "delta_median": float(np.median(d)),
                         "delta_iqr": iqr(list(d)),
                         "delta_cv": float(np.std(d, ddof=1) / np.mean(d)),
                         "out_of_domain": int((d >= alpha).sum()),
                         "recovery": rec})
            if rec == rec:
                wsum += rec * len(vs)
                wn += len(vs)
                worst = min(worst, rec)
        nd = [r["distinct_values"] for r in rows]
        ms = [r["modal_share"] for r in rows]
        sweep.append({"width_years": w, "n_qualifying_bands": len(rows),
                      "median_distinct_values_per_band":
                          float(statistics.median(nd)) if nd else float("nan"),
                      "median_modal_share":
                          float(statistics.median(ms)) if ms else float("nan"),
                      "firm_years_in_qualifying_bands": wn,
                      "coverage": wn / len(lives) if lives else 0.0,
                      "recovery_weighted": (wsum / wn) if wn else float("nan"),
                      "recovery_min_band": worst if rows else float("nan"),
                      "bands": rows})
    return {"n": len(lives), "THIN": False, "alpha": alpha, "heaping": heaping,
            "out_of_domain": out_of_domain,
            "out_of_domain_share": out_of_domain / len(lives),
            "poles": poles, "sweep": sweep}


# --------------------------------------------------------------------------------------
# The refusal-coherence guard, promoted from a find to an assertion (SOURCE-001 §4c).
# --------------------------------------------------------------------------------------
def compare_or_refuse(label: str, a: dict, b: dict, fmt) -> None:
    """Print a comparison ONLY if neither side was refused by THIS file's own THIN rule.

    §4c found a probe printing a contrast between two cells whose individual rates the
    same function had just declined to report. A guard that refuses a cell and then
    compares it is not a guard."""
    if a.get("THIN") or b.get("THIN"):
        who = [x.get("label", "?") for x in (a, b) if x.get("THIN")]
        print(f"  {label}: NOT COMPARED -- {', '.join(who)} was refused as THIN, and a "
              f"comparison between two cells whose own rates were refused is not a "
              f"comparison.")
        return
    print(fmt(a, b))


RULES = ("R_MID", "R_MIN", "R_WEIGHT")


def cmd_report(args: argparse.Namespace) -> int:
    blobs = [json.loads(pathlib.Path(p).read_text()) for p in args.records]
    records = [r for b in blobs for r in b["records"]]
    comps = [c for b in blobs for c in b.get("comparatives", [])]
    alpha = args.alpha
    thin = args.thin

    print("=" * 86)
    print("REG-009 §2 · P0 -- THE PRE-CONDITION PROBE.  Numbers only; P0 does not fix "
          "D2/D3/D4.")
    print("=" * 86)
    print(f"cycles: {', '.join(b['cycle'] for b in blobs)}")
    print(f"firm-year records with at least one canonical life VALUE: {len(records)}")
    print(f"prior-period comparatives (the same firm at an earlier year end): {len(comps)}")
    print(f"THIN threshold: {thin} firm-years (§3b's line, not a new number)")
    print(f"recognition rate alpha = {alpha} -- §5.4's MEASURED rate, 95% [0.383, 0.432]. "
          f"§4.4's calibrated {ALPHA_CALIBRATED} puts the ENTIRE disclosed rectangle "
          f"outside the model's domain, so the measured rate is not a refinement here, "
          f"it is the precondition.")
    for b in blobs:
        t = b["tally"]
        print(f"\n  cycle {b['cycle']}: {t.get('panel_firm_years_in_window',0)} panel "
              f"firm-years, {t.get('submission_found',0)} with a 10-K, "
              f"{t.get('firm_years_with_a_life',0)} with a life VALUE "
              f"({t.get('firm_years_with_a_life',0)/max(1,t.get('panel_firm_years_in_window',1)):.3f})")
        print(f"    declined and counted: {t.get('submission_no_life_value',0)} filings "
              f"with no canonical life value · {t.get('dupe_iprx_dropped',0)} duplicate "
              f"iprx rows · {t.get('unparseable_duration',0)} unparseable durations · "
              f"{sum(v for k,v in t.items() if k.startswith('excluded_tag:'))} rows on "
              f"non-canonical UsefulLife tags")

    ncan = Counter()
    for b in blobs:
        for k, v in b["tally"].items():
            if k.startswith("excluded_tag:"):
                ncan[k[13:]] += v
    print("\n  NON-CANONICAL UsefulLife TAGS, NAMED RATHER THAN CAPPED SILENTLY "
          "(top 6 of %d):" % len(ncan))
    for k, v in ncan.most_common(6):
        print(f"    {v:7d}  {k}")

    interval_share = Counter()
    for r in records:
        for _t, k in r.get("kinds", {}).items():
            interval_share.update(k)
    tot = sum(interval_share.values()) or 1
    print(f"\n  D2's SHAPE PROBLEM, MEASURED ON COMPONENTS: "
          + " · ".join(f"{k} {v} ({v/tot:.3f})" for k, v in interval_share.most_common()))
    print("    §1.6 said the disclosure is an interval for the majority of firm-years. "
          "That is the axis D2 has to collapse and nothing in this repository said how.")

    ns = None
    out: dict = {"alpha": alpha, "thin": thin, "n_records": len(records),
                 "cycles": [b["cycle"] for b in blobs], "by_tag": {}}

    for tag in CANON:
        print("\n" + "=" * 86)
        print(f"TAG: {tag}")
        print("=" * 86)
        n_tag = sum(1 for r in records if r.get("lives", {}).get(tag))
        backed = sum(1 for r in records
                     if (r.get("lives", {}).get(tag) or {}).get("R_WEIGHT_backed"))
        print(f"firm-years carrying this tag: {n_tag}")
        print(f"  R_WEIGHT actually backed by component amounts: {backed} "
              f"({backed/max(1,n_tag):.3f}) -- the rest FALL BACK TO R_MID, so where "
              f"this share is low the two columns are not two rules.")
        if n_tag < thin:
            print(f"  THIN (<{thin}) -- refused as evidence, and NOT compared with "
                  f"anything below.")
            out["by_tag"][tag] = {"THIN": True, "n": n_tag}
            continue
        tagout: dict = {"n": n_tag, "THIN": False}

        # ---------------- P0-a ----------------
        print("\n-- P0-a · STICKINESS (paper III §4.7 bound 2, measured for the first "
              "time) --")
        print("   |Dlog L| between two observations of the SAME firm. 0 = the disclosed "
              "life did not move.")
        for rule in RULES:
            a = p0a(records, comps, tag, rule, thin)
            tagout.setdefault("p0a", {})[rule] = a
            for key in ("adjacent", "decade", "decade_by_component"):
                d = a[key]
                if d.get("THIN"):
                    print(f"   {rule:<9} {key:<20} n={d['n']:<5} THIN (<{thin}) -- "
                          f"refused as evidence")
                    continue
                lo, hi = d["iqr"]
                cl, ch = d["ci_median"]
                print(f"   {rule:<9} {key:<20} n={d['n']:<5} unchanged "
                      f"{d['unchanged_share']:.3f} · within 10% "
                      f"{d['within_10pct_share']:.3f} · median |Dlog L| "
                      f"{d['median_abs_dlog']:.4f} [IQR {lo:.4f}-{hi:.4f}] "
                      f"CI95 [{cl:.4f}, {ch:.4f}]")
            compare_or_refuse(f"   {rule:<9} adjacent vs decade", a["adjacent"],
                              a["decade"],
                              lambda x, y: f"   {rule:<9} adjacent vs decade: unchanged "
                                           f"{x['unchanged_share']:.3f} -> "
                                           f"{y['unchanged_share']:.3f}  "
                                           f"({y['unchanged_share']-x['unchanged_share']:+.3f})")
            r = a["runs"]
            if r.get("firms_with_3plus_observations", 0) >= thin:
                n3 = r["firms_with_3plus_observations"]
                print(f"   {rule:<9} firms with >=3 observations: {n3} · never changed "
                      f"{r.get('never_changed',0)} ({r.get('never_changed',0)/n3:.3f}) · "
                      f"moved once {r.get('moved_once',0)} "
                      f"({r.get('moved_once',0)/n3:.3f}) · moved more "
                      f"{r.get('moved_more_than_once',0)}")
            else:
                print(f"   {rule:<9} firms with >=3 observations: "
                      f"{r.get('firms_with_3plus_observations',0)} -- THIN, the "
                      f"never-changed and moved-once shares are refused")

        # ---------------- P0-b ----------------
        print("\n-- P0-b · INDUSTRY ANCHORING (§4.7 bounds 1 and 3, one claim from two "
              "sides) --")
        print("   ratio = within-SIC sd of log L / total sd of log L. 1.00 = industry "
              "explains nothing; 0.00 = industry explains everything.")
        for rule in RULES:
            b = p0b(records, tag, rule, thin)
            tagout.setdefault("p0b", {})[rule] = b
            if b.get("THIN"):
                print(f"   {rule:<9} n={b['n']} THIN -- refused")
                continue
            lo, hi = b["iqr_years_all"]
            cl, ch = b["ratio_ci95"]
            print(f"   {rule:<9} n={b['n']:<5} SIC major groups kept "
                  f"{b['n_cells']:<3} refused(THIN) {len(b['refused_cells']):<3} "
                  f"ratio {b['ratio']:.3f} CI95 [{cl:.3f}, {ch:.3f}]")
            print(f"   {'':<9} kept cells hold {b['firm_years_in_kept_cells']} of "
                  f"{b['n']} firm-years ({b['kept_coverage']:.3f}); "
                  f"life-years, all firms: "
                  f"median {b['median_years_all']:.2f} [IQR {lo:.2f}-{hi:.2f}]"
                  + ("  ** IQR SPANS AN ORDER OF MAGNITUDE -- two populations, not one **"
                     if lo > 0 and hi / lo >= 10 else ""))

        # ---------------- P0-c ----------------
        print("\n-- P0-c · WITHIN-BAND delta DISPERSION, SWEPT OVER BAND WIDTH (D3's "
              "ruler, §1.4's uncomputed input) --")
        if ns is None:
            ns = load_ladder()
        for rule in RULES:
            c = p0c(records, tag, rule, thin, ns, args.widths, alpha)
            tagout.setdefault("p0c", {})[rule] = c
            if c.get("THIN"):
                print(f"   {rule:<9} n={c['n']} THIN -- refused")
                continue
            print(f"\n   {rule}  n={c['n']}  outside the model's domain (delta >= alpha, "
                  f"i.e. a life under {1/alpha:.2f} years): {c['out_of_domain']} "
                  f"({c['out_of_domain_share']:.3f})")
            h = c["heaping"]
            print(f"   HEAPING: {h['distinct_values']} distinct life values in "
                  f"{c['n']} firm-years · integer {h['integer_share']:.3f} · "
                  f"round number {h['round_number_share']:.3f} · modal value "
                  f"{h['modal_share']:.3f}")
            print(f"   -> every recovery below is an UPPER BOUND: it is computed from "
                  f"the DISCLOSED delta, and a heaped disclosure makes within-band")
            print(f"      dispersion small by arithmetic. The gap between disclosed and "
                  f"economic delta is §4.7's weak joint and is NOT measured here.")
            print(f"   {'width':>7} {'bands':>6} {'firm-yrs':>9} {'coverage':>9} "
                  f"{'recovery':>9} {'worst band':>11} {'distinct/band':>14} "
                  f"{'modal':>7}")
            for s in c["sweep"]:
                flag = "" if s["recovery_weighted"] != s["recovery_weighted"] else (
                    "   <-- clears §4 (>0.80)" if s["recovery_weighted"] > 0.80 else "")
                print(f"   {s['width_years']:>7.2f} {s['n_qualifying_bands']:>6} "
                      f"{s['firm_years_in_qualifying_bands']:>9} {s['coverage']:>9.3f} "
                      f"{s['recovery_weighted']:>9.3f} {s['recovery_min_band']:>11.3f} "
                      f"{s['median_distinct_values_per_band']:>14.1f} "
                      f"{s['median_modal_share']:>7.3f}{flag}")
            print(f"   reference poles at alpha={alpha}: the whole disclosed range as "
                  f"one band -> {c['poles']['whole_disclosed_range']:.3f}")
        out["by_tag"][tag] = tagout

    # ---------------- §4 · the pre-committed stopping rule ----------------
    print("\n" + "=" * 86)
    print("REG-009 §4 · THE PRE-COMMITTED STOPPING RULE, APPLIED")
    print("=" * 86)
    print("Declared BEFORE this probe was written: if no band width achieves a §4.4")
    print("recovery probability above 0.80 while leaving at least 30 firm-years per band,")
    print("the delta design is REFUSED and P0's table is the result.")
    print("Evaluated on the firm-year-weighted recovery across bands that clear the 30")
    print("floor; the worst single band is printed beside it so a mean cannot hide one.")
    print("")
    print("ERRATUM, RECORDED AND NOT REPAIRED. The rule as written prices RECOVERY and")
    print("the THIN floor and says nothing about COVERAGE -- the share of firm-years")
    print("living in bands that clear the floor. It is therefore satisfied by a width")
    print("that recovers well on a quarter of the sample. Coverage is printed in every")
    print("row below and in the sweep above; the verdict is computed on the rule AS")
    print("WRITTEN, because rewriting a pre-commitment after seeing the table is the one")
    print("move a pre-commitment exists to prevent (REG-002 E1's precedent: the defect")
    print("is recorded, the number is left unambiguous).")
    verdict: dict = {}
    for tag in CANON:
        t = out["by_tag"].get(tag, {})
        if t.get("THIN"):
            continue
        for rule, c in (t.get("p0c") or {}).items():
            if c.get("THIN"):
                continue
            best = max((s for s in c["sweep"]
                        if s["recovery_weighted"] == s["recovery_weighted"]),
                       key=lambda s: s["recovery_weighted"], default=None)
            if best is None:
                continue
            verdict[f"{tag}|{rule}"] = {
                "best_width": best["width_years"],
                "median_distinct_values_per_band":
                    best["median_distinct_values_per_band"],
                "median_modal_share": best["median_modal_share"],
                "recovery": best["recovery_weighted"],
                "worst_band": best["recovery_min_band"],
                "coverage": best["coverage"],
                "clears": bool(best["recovery_weighted"] > 0.80)}
            print(f"  {tag[:34]:<34} {rule:<9} width "
                  f"{best['width_years']:>5.2f}y  recovery "
                  f"{best['recovery_weighted']:.3f}  worst band "
                  f"{best['recovery_min_band']:.3f}  coverage {best['coverage']:.3f}  "
                  f"distinct/band {best['median_distinct_values_per_band']:.1f}  "
                  f"-> {'CLEARS' if best['recovery_weighted'] > 0.80 else 'REFUSED'}")
            # The same verdict at the widest band that still holds 80% of the sample --
            # printed because the rule's silence on coverage is an omission, not a licence.
            wide = [x for x in c["sweep"]
                    if x["coverage"] >= 0.80
                    and x["recovery_weighted"] == x["recovery_weighted"]]
            if wide:
                bw = max(wide, key=lambda x: x["recovery_weighted"])
                print(f"  {'':<34} {'':<9} at coverage >= 0.80: width "
                      f"{bw['width_years']:>5.2f}y  recovery "
                      f"{bw['recovery_weighted']:.3f}  worst band "
                      f"{bw['recovery_min_band']:.3f}  coverage {bw['coverage']:.3f}  "
                      f"distinct/band {bw['median_distinct_values_per_band']:.1f}  "
                      f"-> {'clears' if bw['recovery_weighted'] > 0.80 else 'refused'}")
                verdict[f"{tag}|{rule}"]["at_coverage_80"] = {
                    "width": bw["width_years"], "recovery": bw["recovery_weighted"],
                    "worst_band": bw["recovery_min_band"], "coverage": bw["coverage"]}
    out["stopping_rule"] = verdict
    any_clear = any(v["clears"] for v in verdict.values())
    print(f"\n  VERDICT: {'the delta design CLEARS §4 on at least one (tag, rule)' if any_clear else 'REFUSED -- no band width clears 0.80 at >=30 firm-years per band'}")

    if args.out:
        pathlib.Path(args.out).write_text(json.dumps(out, indent=1, default=str))
        print(f"\nwrote {args.out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract")
    e.add_argument("zips", nargs="+")
    e.add_argument("--cycle", required=True)
    e.add_argument("--window-start", default="20221031")
    e.add_argument("--window-end", default="20230930")
    e.add_argument("--no-weights", action="store_true")
    e.add_argument("--out", required=True)
    e.set_defaults(fn=cmd_extract)
    r = sub.add_parser("report")
    r.add_argument("records", nargs="+")
    r.add_argument("--thin", type=int, default=30)
    r.add_argument("--alpha", type=float, default=ALPHA_MEASURED)
    r.add_argument("--widths", type=float, nargs="+",
                   default=[0.25, 0.5, 1, 2, 3, 5, 7.5, 10, 15, 20])
    r.add_argument("--out", default="")
    r.set_defaults(fn=cmd_report)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
