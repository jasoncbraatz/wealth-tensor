#!/usr/bin/env python3
"""SOURCE-001 section 6 step 1, run: are disclosed useful lives machine-readable?

NOT A REGISTRATION AND NOT A RESULT. A source probe: coverage as a count against a
denominator, on this project's own 1,602-firm panel, plus the shape of what a join
would actually get.

WHAT THIS OVERTURNED, stated first because the earlier number is in a document.
SOURCE-001 section 3 reported 0 of 80 panel firms tagging
`PropertyPlantAndEquipmentUsefulLife`, on `data.sec.gov`'s companyconcept API, and
concluded a tagged-XBRL join was 'not expensive -- absent'. That zero is an
instrument artifact. Useful lives are xbrli:durationItemType facts ('P39Y'), which
are NOT numeric; companyconcept serves numeric `units` only and 404s on the concept
even for filers that tag it six times. The SEC's Financial Statement and Notes data
sets keep non-numeric facts in **txt.tsv**, and there the concept is everywhere.

THE TELL, which is the transferable part: the FULLER surface first returned a WORSE
number. Scanning num.tsv (numeric) gave 11 filers of 4,711 -- below the companyconcept
figure it was supposed to beat -- and the three Minimum/Maximum reporters section 3
did find were absent from it entirely. A coverage number that gets worse when the
surface gets bigger is a statement about the surface, not about the filers.

Usage:
    source001_lifetime_coverage.py NOTES_ZIP [--audit CIK] [--out FILE]

NOTES_ZIP is a quarterly/monthly file from
https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/
(e.g. 2023q1_notes.zip). Nothing is fetched here; the zip is an input, so the probe
is offline and rerunnable.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import pathlib
import sys
import zipfile
from collections import Counter, defaultdict

csv.field_size_limit(10_000_000)
HERE = pathlib.Path(__file__).resolve().parent
PANEL = HERE.parent / "data" / "reg-006-wt092-panel.json"

CANON = ("PropertyPlantAndEquipmentUsefulLife",
         "FiniteLivedIntangibleAssetUsefulLife")


def load_panel_ciks() -> set[int]:
    return {int(f["cik"]) for f in json.loads(PANEL.read_text())}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zip")
    ap.add_argument("--audit", type=int, default=0,
                    help="print one firm's resolved life rectangle (hand-audit hook)")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    panel = load_panel_ciks()
    z = zipfile.ZipFile(args.zip)

    subs: dict[str, tuple[int, str]] = {}
    with z.open("sub.tsv") as fh:
        for r in csv.DictReader(io.TextIOWrapper(fh, "utf-8", errors="replace"),
                                delimiter="\t"):
            try:
                subs[r["adsh"]] = (int(r["cik"]), r.get("form", ""))
            except (ValueError, TypeError, KeyError):
                continue
    tenk = {a for a, (_c, f) in subs.items() if f == "10-K"}
    tenk_ciks = {subs[a][0] for a in tenk}
    panel_tenk = tenk_ciks & panel
    print(f"{args.zip}: 10-K filers {len(tenk_ciks)}, of them in panel {len(panel_tenk)}",
          flush=True)

    tag_ciks: dict[str, set[int]] = defaultdict(set)
    tag_rows: Counter = Counter()
    per_firm: Counter = Counter()          # canon facts per panel firm
    dimh_wanted: set[str] = set()
    audit_rows: list[dict] = []
    ext = Counter()

    with z.open("txt.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        head = next(rd)
        ix = {n: i for i, n in enumerate(head)}
        for row in rd:
            if len(row) <= ix["tag"]:
                continue
            tag = row[ix["tag"]]
            if "UsefulLife" not in tag:
                continue
            adsh = row[ix["adsh"]]
            if adsh not in tenk:
                continue
            cik = subs[adsh][0]
            tag_rows[tag] += 1
            tag_ciks[tag].add(cik)
            ext[row[ix["version"]] if ix.get("version") is not None else "?"] += 1
            if tag in CANON and cik in panel:
                per_firm[cik] += 1
            if tag in CANON:
                dimh_wanted.add(row[ix["dimh"]])
            if args.audit and cik == args.audit and tag in CANON:
                audit_rows.append({"tag": tag, "ddate": row[ix["ddate"]],
                                   "value": row[ix["value"]], "dimh": row[ix["dimh"]]})

    any_cik = set().union(*tag_ciks.values()) if tag_ciks else set()
    p_any = any_cik & panel
    print(f"\nANY useful-life tag: {len(any_cik)}/{len(tenk_ciks)} of all 10-K filers"
          f" = {len(any_cik)/max(1,len(tenk_ciks)):.3f}")
    print(f"  on OUR panel:      {len(p_any)}/{len(panel_tenk)}"
          f" = {len(p_any)/max(1,len(panel_tenk)):.3f}")
    for c in CANON:
        pc = tag_ciks.get(c, set()) & panel
        print(f"  {c}: panel {len(pc)}/{len(panel_tenk)}"
              f" = {len(pc)/max(1,len(panel_tenk)):.3f}"
              f"   (all filers {len(tag_ciks.get(c, ()))})")
    std = sum(v for k, v in ext.items() if k.startswith("us-gaap"))
    print(f"\nstandard us-gaap tags: {std} of {sum(ext.values())} rows"
          f" = {std/max(1,sum(ext.values())):.3f} -- the rest are company extensions")

    if per_firm:
        vals = sorted(per_firm.values())
        print(f"\nfacts per reporting panel firm: median {vals[len(vals)//2]}, "
              f"max {vals[-1]} -- a SCHEDULE, not a point")

    # --- dimensions: what a join actually gets
    dims: dict[str, str] = {}
    with z.open("dim.tsv") as fh:
        rd = csv.reader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t")
        h = next(rd)
        for row in rd:
            if row[0] in dimh_wanted:
                dims[row[0]] = row[h.index("segments")]
    ranged = sum(1 for s in dims.values() if "Range=" in s)
    print(f"\ndistinct dimension sets on the two canonical tags: {len(dims)};"
          f" carrying a Range axis: {ranged} = {ranged/max(1,len(dims)):.3f}")
    axes = Counter()
    for s in dims.values():
        for part in s.split(";"):
            if "=" in part:
                axes[part.split("=")[0]] += 1
    print("top axes: " + ", ".join(f"{k} {v}" for k, v in axes.most_common(6)))

    if args.audit:
        print(f"\n--- hand-audit, CIK {args.audit} ---")
        for r in sorted(audit_rows, key=lambda r: dims.get(r["dimh"], "")):
            print(f"  {r['ddate']}  {r['value']:>8}  {dims.get(r['dimh'], '(no dim)')}")

    if args.out:
        pathlib.Path(args.out).write_text(json.dumps({
            "zip": args.zip, "tenk_ciks": len(tenk_ciks),
            "panel_tenk": len(panel_tenk), "panel_any": len(p_any),
            "canon": {c: len(tag_ciks.get(c, set()) & panel) for c in CANON},
            "dims_with_range": ranged, "dims_total": len(dims),
        }, indent=1))
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
