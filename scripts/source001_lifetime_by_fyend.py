#!/usr/bin/env python3
"""SOURCE-001 section 3b: does section 3a's 0.82 lifetime coverage survive outside December?

NOT A REGISTRATION AND NOT A RESULT. A source probe, and specifically the probe that
section 3a named as its own outstanding caveat:

    "It is also measured on Q1 filings, which favours December fiscal-year ends; a
     firm-year join must confirm per-year coverage on the panel's own fy_end
     distribution rather than inherit 0.82 from this table."

WHY THE CAVEAT IS NOT COSMETIC. A 10-K is filed 60-90 days after the fiscal year ends,
so a single Q1 notes zip can only contain filers whose year ended in roughly the
preceding October-January. 40.8 per cent of this panel's firm-years end in a month
other than December, and about 31 per cent end in a month a Q1 zip CANNOT REACH. That
is the ninth entry in the handoff's list wearing a new hat: a measurement restricted to
one quarter cannot represent the other three, so a number read off it is not evidence
about them either way.

WHAT IS DIFFERENT HERE, in three parts:

 1. FOUR quarters, so every fiscal-year-end month is inside the instrument's reach at
    least once. Safe window: fiscal year ends 2022-10-31 .. 2023-09-30 -- twelve
    consecutive month ends, one per calendar month, whose 10-Ks are all due inside
    calendar 2023.
 2. The unit is the FIRM-YEAR, not the firm, because a firm-year is what the join
    actually needs. Section 3a counted distinct CIKs inside one quarter.
 3. Coverage is decomposed, because "not covered" hides two different things:
    NO SUBMISSION FOUND (the firm did not file inside the window, or filed late enough
    to fall out of it) is a different failure from SUBMISSION FOUND BUT NO LIFE TAGGED.
    Only the second is a statement about tagging behaviour. Reporting them as one
    number is how a coverage figure becomes uninterpretable.

The guard this file carries as code, in the spirit of its two siblings: a bucket whose
denominator is too small to distinguish a rate from noise is printed with a THIN marker
and is refused as evidence, because a small denominator producing an extreme rate is
exactly the shape that put "the branch is alive for property only" into section 4a.

Usage:
    source001_lifetime_by_fyend.py NOTES_ZIP [NOTES_ZIP ...] [--out FILE]
                                   [--window-start YYYYMMDD] [--window-end YYYYMMDD]
                                   [--thin N]

NOTES_ZIPs are quarterly files from
https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/
Nothing is fetched here; the zips are inputs, so the probe is offline and rerunnable.
Runs in the cloud, not on darwin -- see the handoff's note on data.sec.gov throttling.
"""
from __future__ import annotations

import argparse
import calendar
import csv
import datetime as dt
import io
import json
import math
import pathlib
import sys
import zipfile
from collections import Counter, defaultdict

csv.field_size_limit(10_000_000)
HERE = pathlib.Path(__file__).resolve().parent
PANEL = HERE.parent / "data" / "reg-006-wt092-panel.json"

CANON = ("PropertyPlantAndEquipmentUsefulLife",
         "FiniteLivedIntangibleAssetUsefulLife")

# FSN rounds `period` to the nearest month end. A 52/53-week filer whose year ends
# 2023-01-28 appears as 20230131. Match on month end, and allow the year end to sit a
# few days either side of a month boundary -- but COUNT how often that slack is used,
# so it is an auditable number rather than a silent fudge.
FUZZ_DAYS = 5

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def month_end(d: dt.date) -> dt.date:
    return d.replace(day=calendar.monthrange(d.year, d.month)[1])


def candidate_periods(d: dt.date) -> list[str]:
    """The FSN `period` strings a fiscal year end of `d` could plausibly appear as."""
    out = []
    for off in (0, FUZZ_DAYS, -FUZZ_DAYS):
        me = month_end(d + dt.timedelta(days=off))
        s = me.strftime("%Y%m%d")
        if s not in out:
            out.append(s)
    return out


def load_panel() -> list[dict]:
    return json.loads(PANEL.read_text())


def ztest(n1: int, d1: int, n2: int, d2: int) -> tuple[float, float]:
    """Two-proportion z on (n1/d1) - (n2/d2). Returns (difference, z).

    Here so that a gap between two buckets is REPORTED WITH ITS PRECISION rather than
    eyeballed off a table. The failure this guards is the mirror of the THIN one: a
    difference that looks like a finding because two decimals were printed next to each
    other. A z below about 2 is the table saying 'not from this measurement'.
    """
    if not d1 or not d2:
        return (0.0, 0.0)
    p1, p2 = n1 / d1, n2 / d2
    p = (n1 + n2) / (d1 + d2)
    se = math.sqrt(p * (1 - p) * (1 / d1 + 1 / d2))
    return (p1 - p2, (p1 - p2) / se if se else 0.0)


def scan_zip(path: str, panel_ciks: set[int]) -> tuple[dict, dict]:
    """Return (submissions, tagged) for panel 10-K filings in one notes zip.

    submissions: adsh -> {cik, period, filed}
    tagged:      adsh -> {canonical tag -> row count}
    """
    z = zipfile.ZipFile(path)
    subs: dict[str, dict] = {}
    with z.open("sub.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        head = next(rd)
        ix = {n: i for i, n in enumerate(head)}
        for row in rd:
            if len(row) <= ix["period"]:
                continue
            if row[ix["form"]] != "10-K":
                continue
            try:
                cik = int(row[ix["cik"]])
            except (ValueError, TypeError):
                continue
            if cik not in panel_ciks:
                continue
            subs[row[ix["adsh"]]] = {"cik": cik,
                                     "period": row[ix["period"]],
                                     "filed": row[ix["filed"]]}
    print(f"  {pathlib.Path(path).name}: {len(subs)} panel 10-K submissions", flush=True)

    tagged: dict[str, Counter] = defaultdict(Counter)
    with z.open("txt.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        head = next(rd)
        ix = {n: i for i, n in enumerate(head)}
        ti, ai = ix["tag"], ix["adsh"]
        for row in rd:
            if len(row) <= ti:
                continue
            tag = row[ti]
            if "UsefulLife" not in tag:
                continue
            adsh = row[ai]
            if adsh not in subs:
                continue
            tagged[adsh][tag] += 1
    n_any = len(tagged)
    n_canon = sum(1 for t in tagged.values() if any(c in t for c in CANON))
    print(f"    tagging any useful life: {n_any};  a canonical one: {n_canon}", flush=True)
    return subs, dict(tagged)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zips", nargs="+")
    ap.add_argument("--window-start", default="20221031")
    ap.add_argument("--window-end", default="20230930")
    ap.add_argument("--thin", type=int, default=30,
                    help="a bucket with fewer than this many firm-years is refused as "
                         "evidence and printed THIN")
    ap.add_argument("--out", default="")
    ap.add_argument("--compare", default="",
                    help="a JSON written by an earlier --out run, from a DIFFERENT "
                         "fiscal cycle: prints the cross-cycle contrasts with z, which "
                         "is the only way to tell a level shift from a table's mood")
    args = ap.parse_args()

    panel = load_panel()
    panel_ciks = {int(f["cik"]) for f in panel}

    subs: dict[str, dict] = {}
    tagged: dict[str, dict] = {}
    for p in args.zips:
        s, t = scan_zip(p, panel_ciks)
        subs.update(s)
        tagged.update(t)

    # index submissions by (cik, period)
    by_key: dict[tuple[int, str], list[str]] = defaultdict(list)
    for adsh, s in subs.items():
        by_key[(s["cik"], s["period"])].append(adsh)

    w0 = dt.datetime.strptime(args.window_start, "%Y%m%d").date()
    w1 = dt.datetime.strptime(args.window_end, "%Y%m%d").date()

    # ---- walk the panel's own firm-year rows -------------------------------------
    buckets: dict[int, Counter] = defaultdict(Counter)   # month -> counters
    rows_in_window = 0
    fuzz_used = 0
    lag_days: list[int] = []
    per_row: list[dict] = []

    for f in panel:
        cik = int(f["cik"])
        for r in f["rows"]:
            try:
                fe = dt.datetime.strptime(r["fy_end"], "%Y-%m-%d").date()
            except (ValueError, TypeError, KeyError):
                continue
            if not (w0 <= fe <= w1):
                continue
            rows_in_window += 1
            m = fe.month
            b = buckets[m]
            b["rows"] += 1

            hit, used_fuzz = None, False
            for i, per in enumerate(candidate_periods(fe)):
                if (cik, per) in by_key:
                    hit = by_key[(cik, per)][0]
                    used_fuzz = i > 0
                    break
            if hit is None:
                b["no_submission"] += 1
                per_row.append({"cik": cik, "fy_end": r["fy_end"],
                                "status": "no_submission"})
                continue
            if used_fuzz:
                fuzz_used += 1
            b["submission"] += 1
            try:
                filed = dt.datetime.strptime(subs[hit]["filed"], "%Y%m%d").date()
                lag_days.append((filed - fe).days)
            except (ValueError, TypeError):
                pass
            tg = tagged.get(hit, {})
            has_any = bool(tg)
            has_canon = any(c in tg for c in CANON)
            has_ppe = CANON[0] in tg
            has_int = CANON[1] in tg
            b["any"] += has_any
            b["canon"] += has_canon
            b["ppe"] += has_ppe
            b["intang"] += has_int
            per_row.append({"cik": cik, "fy_end": r["fy_end"], "status": "submission",
                            "adsh": hit, "any": has_any, "canon": has_canon,
                            "ppe": has_ppe, "intangible": has_int,
                            "facts": sum(v for k, v in tg.items() if k in CANON)})

    # ---- report -------------------------------------------------------------------
    print(f"\npanel firm-years with fy_end in [{w0} .. {w1}]: {rows_in_window}")
    print(f"period matched via the +/-{FUZZ_DAYS}d month-end slack: {fuzz_used}"
          f"  ({fuzz_used/max(1,rows_in_window):.3f} of rows -- 52/53-week filers)")
    if lag_days:
        lag_days.sort()
        q = lambda p: lag_days[min(len(lag_days) - 1, int(p * len(lag_days)))]
        print(f"filing lag after fiscal year end, days: median {q(0.5)}, "
              f"p90 {q(0.9)}, p99 {q(0.99)}, max {lag_days[-1]}")

    hdr = (f"\n{'fy_end':>6} | {'firm-yrs':>8} | {'10-K found':>16} | "
           f"{'any life':>16} | {'canonical':>16} | {'PP&E':>16}")
    print(hdr)
    print("-" * len(hdr))

    def cell(n: int, d: int) -> str:
        return f"{n:5d} {n/d:.3f}" if d else f"{n:5d}   -  "

    order = sorted(buckets, key=lambda m: (m != 12, m))   # December first, then Jan..
    thin_months: list[str] = []
    tot = Counter()
    for m in order:
        b = buckets[m]
        tot.update(b)
        d, s = b["rows"], b["submission"]
        mark = ""
        if d < args.thin:
            mark = "  THIN"
            thin_months.append(MONTHS[m - 1])
        print(f"{MONTHS[m-1]:>6} | {d:8d} | {cell(b['submission'], d):>16} | "
              f"{cell(b['any'], s):>16} | {cell(b['canon'], s):>16} | "
              f"{cell(b['ppe'], s):>16}{mark}")

    d, s = tot["rows"], tot["submission"]
    print("-" * len(hdr))
    print(f"{'ALL':>6} | {d:8d} | {cell(tot['submission'], d):>16} | "
          f"{cell(tot['any'], s):>16} | {cell(tot['canon'], s):>16} | "
          f"{cell(tot['ppe'], s):>16}")

    # December vs the rest -- the comparison the caveat actually asked for
    dec = buckets.get(12, Counter())
    rest = Counter()
    for m, b in buckets.items():
        if m != 12:
            rest.update(b)
    print("\nthe comparison section 3a's caveat asked for, conditional on a 10-K "
          "being found:")
    for label, b in (("December fy_end", dec), ("every other month", rest)):
        s2 = b["submission"]
        if not s2:
            print(f"  {label:<20} no submissions -- nothing to report")
            continue
        print(f"  {label:<20} n={s2:5d}   any {b['any']/s2:.3f}   "
              f"canonical {b['canon']/s2:.3f}   PP&E {b['ppe']/s2:.3f}")
    print("\nand unconditionally, which is what a join gets per firm-year:")
    for label, b in (("December fy_end", dec), ("every other month", rest)):
        d2 = b["rows"]
        if not d2:
            continue
        print(f"  {label:<20} n={d2:5d}   10-K found {b['submission']/d2:.3f}   "
              f"canonical life {b['canon']/d2:.3f}")
    if dec["rows"] and rest["rows"]:
        diff, z = ztest(dec["canon"], dec["rows"], rest["canon"], rest["rows"])
        verdict = ("a December advantage this measurement can see"
                   if abs(z) >= 2 else
                   "NO December advantage this measurement can distinguish from zero")
        print(f"\n  Dec - other, canonical life per firm-year: {diff:+.3f}  "
              f"z = {z:+.2f}  -->  {verdict}")

    if thin_months:
        print(f"\nTHIN buckets refused as evidence (<{args.thin} firm-years): "
              f"{', '.join(thin_months)} -- a rate from a denominator this small is "
              f"not distinguishable from noise, and the whole reason this probe exists "
              f"is a zero cell that was read as a finding.")

    if args.compare:
        prev = json.loads(pathlib.Path(args.compare).read_text())
        pdec = Counter(prev["by_month"].get("Dec", {}))
        prest = Counter()
        for k, v in prev["by_month"].items():
            if k != "Dec":
                prest.update(v)
        print(f"\n--- cross-cycle, against {pathlib.Path(args.compare).name} "
              f"(window {prev['window'][0]}..{prev['window'][1]}) ---")
        rowsets = (("December fy_end", dec, pdec),
                   ("every other month", rest, prest),
                   ("all firm-years", tot, Counter(prev["total"])))
        for label, now, then in rowsets:
            if not now["rows"] or not then["rows"]:
                continue
            diff, z = ztest(now["canon"], now["rows"], then["canon"], then["rows"])
            print(f"  {label:<20} {then['canon']/then['rows']:.3f} -> "
                  f"{now['canon']/now['rows']:.3f}   {diff:+.3f}  z = {z:+.2f}")
        for label, b in (("this cycle", (dec, rest)),
                         ("that cycle", (pdec, prest))):
            a, c = b
            if not a["rows"] or not c["rows"]:
                continue
            diff, z = ztest(a["canon"], a["rows"], c["canon"], c["rows"])
            print(f"  Dec - other, {label:<9} {diff:+.3f}  z = {z:+.2f}")

    if args.out:
        pathlib.Path(args.out).write_text(json.dumps({
            "zips": [pathlib.Path(p).name for p in args.zips],
            "window": [args.window_start, args.window_end],
            "fuzz_days": FUZZ_DAYS, "fuzz_used": fuzz_used,
            "thin_threshold": args.thin, "thin_months": thin_months,
            "by_month": {MONTHS[m - 1]: dict(buckets[m]) for m in order},
            "total": dict(tot),
            "rows": per_row,
        }, indent=1))
        print(f"\nwrote {args.out}  ({len(per_row)} firm-year records -- the count is "
              f"auditable without re-reading 2.2 GB of zips)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
