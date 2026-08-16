#!/usr/bin/env python3
"""REG-013 · the citation-graph whitespace, measured against a ceiling and a floor.

Registered at docs/preregistration/REG-013-citation-graph-whitespace.md, commit fff7063,
BEFORE this file existed. Everything fixed by that document is transcribed here as a
constant and nothing here may be re-chosen in response to a number it prints.

WHAT THIS DOES
--------------
Four clusters of seed works (three targets + one unrelated-field floor). For each cluster,
retrieve the set of works CITING at least one resolved seed -- the cluster's audience --
capped at N_MAX by descending citation count. Then read overlap coefficients:

    O(A,B) = |cite(A) & cite(B)| / min(|cite(A)|, |cite(B)|)

for the three target pairs, for the three floor pairs (.,X), and for each cluster split
against itself by seed-index parity (the ceiling control that cannot be tuned).

WHY THE CONTROLS ARE THE POINT
------------------------------
A low co-citation rate between two specialties is the normal condition of any two
specialties, so the three target numbers alone would say nothing. The split-half ceiling
establishes what this instrument reads for a literature joined to itself; the CRISPR floor
establishes what it reads for a pair unrelated by construction. The verdict is a position
on that scale, not a raw rate. REG-013 s4 fixes the thresholds and the VOID rule.

The statistic is computed over the CITING works, never over the seeds' own reference
lists, because OpenAlex reference coverage collapses before the mid-1990s and four of
these seeds predate that (REG-013 s5.1).
"""

from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request

MAILTO = "jasoncbraatz@gmail.com"
API = "https://api.openalex.org/works"
N_MAX = 4000  # REG-013 s3.3
PER_PAGE = 200
Z_WHITESPACE = 0.10  # REG-013 s4
Z_JOINED = 0.25  # REG-013 s4
P_VOID = 0.20  # REG-013 s4 -- ceiling below this voids the run

# REG-013 s3.1 / s3.2. Order is load-bearing: the split-half control is by index parity
# in exactly this order. Do not reorder.
CLUSTERS: dict[str, list[tuple[str, int]]] = {
    "T": [
        ("The Entropy Law and the Economic Process", 1971),
        ("The Economic Growth Engine", 2009),
        ("Accounting for growth: the role of physical work", 2005),
        ("Energy and the Wealth of Nations", 2012),
        ("Environmental Accounting: Emergy and Environmental Decision Making", 1996),
        ("Steady-State Economics", 1977),
        ("The Second Law of Economics", 2011),
    ],
    "S": [
        ("Monetary Economics: An Integrated Approach to Credit, Money, Income, Production and Wealth", 2007),
        ("Post-Keynesian stock-flow-consistent modelling: a survey", 2015),
        ("Stock-flow consistent macroeconomic models: a survey", 2017),
        ("Seven unsustainable processes", 1999),
        ("Post-Keynesian Economics: New Foundations", 2014),
        ("Keynesian theorising during hard times", 2005),
    ],
    "K": [
        ("Statistical mechanics of money", 2000),
        ("Statistical mechanics of money: how saving propensity affects its distribution", 2000),
        ("Wealth condensation in a simple model of economy", 2000),
        ("Kinetic exchange models for income and wealth distributions", 2007),
        ("Colloquium: Statistical mechanics of money, wealth, and income", 2009),
        ("Statistical model with a standard Gamma distribution", 2004),
    ],
    "X": [
        ("A Programmable Dual-RNA-Guided DNA Endonuclease in Adaptive Bacterial Immunity", 2012),
        ("Multiplex Genome Engineering Using CRISPR/Cas Systems", 2013),
        ("RNA-Guided Human Genome Engineering via Cas9", 2013),
        ("The new frontier of genome engineering with CRISPR-Cas9", 2014),
        ("Genome engineering using the CRISPR-Cas9 system", 2013),
        ("Programmable editing of a target base in genomic DNA without double-stranded DNA cleavage", 2016),
    ],
}


def _get(url: str, tries: int = 5) -> dict:
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": f"wealth-tensor REG-013 (mailto:{MAILTO})"})
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except Exception as exc:  # noqa: BLE001 -- transport, not logic
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"GET failed after {tries}: {url}\n{last}")


def _filter_safe(title: str) -> str:
    """OpenAlex filter VALUES are parsed positionally: a ':' or ',' inside one is a
    syntax error (HTTP 400), not a literal. Strip everything that is not a letter,
    digit, space or hyphen. This is a transport concern only -- it narrows nothing,
    because title.search tokenises anyway."""
    return "".join(c if (c.isalnum() or c in " -") else " " for c in title)


def resolve_seed(title: str, year: int) -> tuple[str, str, int] | None:
    """Best match by title search, preferring the nearest publication year."""
    q = urllib.parse.urlencode(
        {
            "filter": f"title.search:{_filter_safe(title)}",
            "per-page": "25",
            "select": "id,display_name,publication_year,cited_by_count",
            "mailto": MAILTO,
        }
    )
    res = _get(f"{API}?{q}").get("results", [])
    if not res:
        return None
    # Prefer within 3 years of the stated year; among those take the most-cited.
    near = [w for w in res if w.get("publication_year") and abs(w["publication_year"] - year) <= 3]
    pool = near or res
    best = max(pool, key=lambda w: w.get("cited_by_count") or 0)
    return best["id"].rsplit("/", 1)[-1], best["display_name"], best.get("cited_by_count") or 0


def citing_set(seed_ids: list[str], label: str) -> tuple[set[str], bool]:
    """Works citing ANY of seed_ids, descending citation count, capped at N_MAX."""
    if not seed_ids:
        return set(), False
    out: set[str] = set()
    cursor = "*"
    while cursor and len(out) < N_MAX:
        q = urllib.parse.urlencode(
            {
                "filter": f"cites:{'|'.join(seed_ids)}",
                "sort": "cited_by_count:desc",
                "per-page": str(PER_PAGE),
                "cursor": cursor,
                "select": "id",
                "mailto": MAILTO,
            }
        )
        page = _get(f"{API}?{q}")
        rows = page.get("results", [])
        if not rows:
            break
        for w in rows:
            out.add(w["id"].rsplit("/", 1)[-1])
        cursor = page.get("meta", {}).get("next_cursor")
        print(f"    {label}: {len(out)}", file=sys.stderr)
    bound = len(out) >= N_MAX
    return out, bound


def overlap(a: set[str], b: set[str]) -> tuple[float, int, int]:
    if not a or not b:
        return float("nan"), 0, 0
    inter = len(a & b)
    denom = min(len(a), len(b))
    return inter / denom, inter, denom


def main() -> int:
    report: dict = {"n_max": N_MAX, "clusters": {}, "seeds": {}, "pairs": {}, "ceiling": {}}

    # --- resolve seeds -------------------------------------------------------
    resolved: dict[str, list[str]] = {}
    for name, seeds in CLUSTERS.items():
        ids: list[str] = []
        rows = []
        for title, year in seeds:
            hit = resolve_seed(title, year)
            if hit is None:
                rows.append({"asked": title, "year": year, "resolved": None})
                print(f"[seed] {name}: UNRESOLVED — {title}", file=sys.stderr)
                continue
            wid, disp, cites = hit
            ids.append(wid)
            rows.append({"asked": title, "year": year, "resolved": wid, "as": disp, "cited_by": cites})
            print(f"[seed] {name}: {wid}  {cites:>7}  {disp[:70]}", file=sys.stderr)
        resolved[name] = ids
        report["seeds"][name] = rows

    # --- audiences -----------------------------------------------------------
    audience: dict[str, set[str]] = {}
    for name in CLUSTERS:
        print(f"[cite] {name}: fetching audience", file=sys.stderr)
        s, bound = citing_set(resolved[name], name)
        audience[name] = s
        report["clusters"][name] = {
            "seeds_asked": len(CLUSTERS[name]),
            "seeds_resolved": len(resolved[name]),
            "audience": len(s),
            "cap_bound": bound,
            "under_powered": len(resolved[name]) < 4,  # REG-013 s5.4
        }

    # --- ceiling: split-half by seed-index parity ---------------------------
    ceilings = []
    for name in ("T", "S", "K"):
        ids = resolved[name]
        even, odd = ids[0::2], ids[1::2]
        if not even or not odd:
            report["ceiling"][name] = {"overlap": None, "note": "cluster too small to split"}
            continue
        print(f"[ceil] {name}: split {len(even)}/{len(odd)}", file=sys.stderr)
        a, _ = citing_set(even, f"{name}-even")
        b, _ = citing_set(odd, f"{name}-odd")
        o, inter, denom = overlap(a, b)
        report["ceiling"][name] = {
            "overlap": o,
            "intersection": inter,
            "min_size": denom,
            "even_seeds": len(even),
            "odd_seeds": len(odd),
        }
        if o == o:  # not nan
            ceilings.append(o)

    P = sum(ceilings) / len(ceilings) if ceilings else float("nan")

    # --- floor: (.,X) --------------------------------------------------------
    floors = []
    for name in ("T", "S", "K"):
        o, inter, denom = overlap(audience[name], audience["X"])
        report["pairs"][f"{name},X"] = {"overlap": o, "intersection": inter, "min_size": denom, "role": "floor"}
        if o == o:
            floors.append(o)
    F = sum(floors) / len(floors) if floors else float("nan")

    # --- targets -------------------------------------------------------------
    verdicts = {}
    for a, b in (("T", "S"), ("T", "K"), ("S", "K")):
        o, inter, denom = overlap(audience[a], audience[b])
        z = (o - F) / (P - F) if (P == P and F == F and P != F) else float("nan")
        if z != z:
            v = "UNCOMPUTABLE"
        elif z <= Z_WHITESPACE:
            v = "WHITESPACE"
        elif z >= Z_JOINED:
            v = "JOINED"
        else:
            v = "UNDECIDED"
        verdicts[f"{a},{b}"] = v
        report["pairs"][f"{a},{b}"] = {
            "overlap": o,
            "intersection": inter,
            "min_size": denom,
            "z": z,
            "verdict": v,
            "role": "target",
        }

    report["P_ceiling"] = P
    report["F_floor"] = F
    report["void"] = bool(P != P or P < P_VOID)
    report["H1"] = (
        "VOID — ceiling control failed"
        if report["void"]
        else ("SURVIVES" if all(v == "WHITESPACE" for v in verdicts.values()) else "PARTIAL/FAILS")
    )

    print(json.dumps(report, indent=2))

    # human-readable tail on stderr so the log carries it too
    print("\n=== REG-013 ===", file=sys.stderr)
    print(f"ceiling P = {P:.4f}   floor F = {F:.4f}   VOID={report['void']}", file=sys.stderr)
    for k, v in report["pairs"].items():
        print(f"  {k:6} O={v['overlap']:.4f}  z={v.get('z', float('nan')):.3f}  {v.get('verdict', v['role'])}", file=sys.stderr)
    print(f"H1: {report['H1']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
