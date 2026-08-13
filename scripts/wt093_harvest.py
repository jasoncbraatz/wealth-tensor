#!/usr/bin/env python3
"""REG-007 harvest: locate each window firm-year's 10-K, extract the registered
passages, and COMPUTE NOTHING.

Registered in REG-007 §3.2 before this file existed. This script's only job is to turn
(cik, fiscal_year) into a list of 1,500-character passages around the registered phrase
set. It does not classify, does not count by arm, and does not know what JOINT means.

Runs in the CLOUD -- darwin's disk is at 95% and this streams ~1,900 filings. Documents
are fetched, scanned, and DISCARDED; only passages are retained, so peak disk is the
output file and nothing else.

The frame is data/reg-006-wt092-panel.json, re-read and UNMODIFIED. REG-007 §3.1 forbids
rebuilding it from edgar.py: -18 lost three runs to reconstructing registered machinery
from its signature instead of copying its call site, and a JSON file is the same trap
with a friendlier face.
"""
from __future__ import annotations

import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "wealth-tensor academic research jasoncbraatz@gmail.com"
HERE = pathlib.Path(__file__).resolve().parent

# ---- REG-007 §3.2, frozen. Extending this set after the run is a new registration. ----
PHRASES = (
    "triggering event",
    "triggering events",
    "impairment indicator",
    "impairment indicators",
    "indicators of impairment",
    "indicator of impairment",
    "interim impairment test",
    "interim goodwill impairment",
    "events or circumstances",
)
HALF = 750                      # REG-007 §3.2: 1,500-character window, 750 either side
SENS = (375, 750, 1500)         # F3 half-widths; the harvest keeps the widest and slices


def get(url: str, tries: int = 5) -> bytes:
    last = None
    for a in range(tries):
        try:
            r = urllib.request.Request(url, headers={"User-Agent": UA,
                                                     "Accept-Encoding": "gzip, deflate"})
            with urllib.request.urlopen(r, timeout=60) as fh:
                enc = fh.headers.get("Content-Encoding", "")
                raw = fh.read()
            if enc == "gzip":
                import gzip
                raw = gzip.decompress(raw)
            elif enc == "deflate":
                import zlib
                raw = zlib.decompress(raw, -zlib.MAX_WBITS)
            time.sleep(0.11)
            return raw
        except Exception as e:                                   # noqa: BLE001
            last = e
            time.sleep(0.4 * (a + 1))
    raise RuntimeError(f"{url}: {last}")


_TAG = re.compile(rb"(?is)<(script|style)[^>]*>.*?</\1>")
_ANY = re.compile(rb"(?s)<[^>]+>")
_WS = re.compile(r"\s+")


def to_text(raw: bytes) -> str:
    """Strip tags THEN normalise whitespace, in that order.

    Order matters: a filing that writes 'triggering <b>event</b>' would defeat a
    phrase search run against the raw bytes, and normalising first would glue words
    across tag boundaries that were never adjacent. Tags become spaces, then runs of
    whitespace collapse.
    """
    raw = _TAG.sub(b" ", raw)
    raw = _ANY.sub(b" ", raw)
    txt = raw.decode("utf-8", "replace")
    txt = html.unescape(txt)
    txt = txt.replace("\xa0", " ")
    return _WS.sub(" ", txt)


def submissions(cik: int) -> list[dict]:
    """Every filing on record, following filings.files -- filings.recent alone stops
    at ~1,000 entries and a busy filer's 2013 10-K is behind that horizon."""
    d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    out = []

    def absorb(blk):
        n = len(blk.get("accessionNumber", []))
        for i in range(n):
            out.append({k: blk[k][i] for k in
                        ("accessionNumber", "form", "primaryDocument", "reportDate", "filingDate")
                        if k in blk})

    absorb(d.get("filings", {}).get("recent", {}))
    for f in d.get("filings", {}).get("files", []):
        try:
            absorb(json.loads(get(f"https://data.sec.gov/submissions/{f['name']}")))
        except Exception:                                        # noqa: BLE001
            pass
    return out


def pick(filings: list[dict], fy_end: str) -> dict | None:
    """The 10-K whose period is this fiscal year end. Exact reportDate first; a +/-10 day
    tolerance second, because a 52/53-week filer's period end drifts off the panel's date.
    A plain 10-K outranks a 10-K/A; the amendment is used only if it is all there is, and
    the choice is recorded so F4 can see it."""
    import datetime as dt
    want = dt.date.fromisoformat(fy_end)
    cand = []
    for f in filings:
        form = (f.get("form") or "").upper()
        if not form.startswith("10-K"):
            continue
        rd = f.get("reportDate") or ""
        if not rd:
            continue
        try:
            got = dt.date.fromisoformat(rd)
        except ValueError:
            continue
        delta = abs((got - want).days)
        if delta <= 10:
            cand.append((0 if form == "10-K" else 1, delta, f))
    if not cand:
        return None
    cand.sort(key=lambda x: (x[0], x[1]))
    best = dict(cand[0][2])
    best["_amended_only"] = cand[0][0] == 1
    best["_day_delta"] = cand[0][1]
    return best


def passages(txt: str, half: int) -> list[dict]:
    low = txt.lower()
    out = []
    for p in PHRASES:
        start = 0
        while True:
            i = low.find(p, start)
            if i < 0:
                break
            a, b = max(0, i - half), min(len(txt), i + len(p) + half)
            out.append({"phrase": p, "at": i, "text": txt[a:b]})
            start = i + len(p)
    return out


def main() -> None:
    panel = json.loads((HERE / "panel.json").read_text())
    jobs: dict[int, list[dict]] = {}
    for f in panel:
        cik = int(f["cik"])
        for r in f["rows"]:
            t = (r.get("t0") or 0) + (r.get("t1") or 0) + (r.get("t2") or 0)
            g = r.get("G") or 0
            if g > 0:
                arm = "JOINT" if t > 0 else "GWONLY"
            elif t > 0:
                arm = "PLACEBO"
            else:
                continue
            jobs.setdefault(cik, []).append(
                {"cik": cik, "universe": f["universe"], "sic": f.get("sic"),
                 "fy_end": r["fy_end"], "arm": arm,
                 "G": g, "t_sum": t, "A": r.get("A")})

    print(f"REG-007 harvest · {sum(len(v) for v in jobs.values())} firm-years "
          f"across {len(jobs)} filers", flush=True)

    results, misses = [], []

    def one(cik: int):
        rows = jobs[cik]
        try:
            fl = submissions(cik)
        except Exception as e:                                   # noqa: BLE001
            return [{"_miss": "submissions", "cik": cik, "err": str(e)[:120],
                     "fy_end": r["fy_end"]} for r in rows]
        out = []
        for r in rows:
            hit = pick(fl, r["fy_end"])
            if not hit or not hit.get("primaryDocument"):
                out.append({"_miss": "no_10k", "cik": cik, "fy_end": r["fy_end"]})
                continue
            acc = hit["accessionNumber"].replace("-", "")
            url = (f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/"
                   f"{hit['primaryDocument']}")
            try:
                txt = to_text(get(url))
            except Exception as e:                               # noqa: BLE001
                out.append({"_miss": "fetch", "cik": cik, "fy_end": r["fy_end"],
                            "url": url, "err": str(e)[:120]})
                continue
            rec = dict(r)
            rec.update({"accession": hit["accessionNumber"], "doc": hit["primaryDocument"],
                        "amended_only": hit["_amended_only"], "day_delta": hit["_day_delta"],
                        "doc_chars": len(txt),
                        "gwi_mention": "goodwill impairment" in txt.lower(),
                        "passages": passages(txt, max(SENS))})
            out.append(rec)
        return out

    ciks = sorted(jobs)
    done = 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        for batch in ex.map(one, ciks):
            for rec in batch:
                (misses if rec.get("_miss") else results).append(rec)
            done += 1
            if done % 50 == 0:
                print(f"  {done}/{len(ciks)} filers · {len(results)} firm-years "
                      f"· {len(misses)} misses", flush=True)

    n_pass = sum(len(r["passages"]) for r in results)
    print(f"\nharvest complete: {len(results)} firm-years, {len(misses)} misses, "
          f"{n_pass} passages", flush=True)
    out = {"schema": "reg-007-passages/1", "half_widths": SENS, "phrases": PHRASES,
           "firm_years": results, "misses": misses}
    p = HERE / "reg-007-passages.json"
    p.write_text(json.dumps(out, separators=(",", ":")))
    print(f"wrote {p} ({p.stat().st_size/1e6:.1f} MB)")


if __name__ == "__main__":
    sys.exit(main())
