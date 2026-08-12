#!/usr/bin/env python3
"""Rebuild the PRE-002 688-event sample and dump it as a committable table.

The sample was collected in session S3 inside a cloud container whose
`$WT_EDGAR_CACHE` died with the container. Nothing about the sample changed --
`edgar.py` is the pre-registration and is untouched here -- but the events
themselves existed only as a cache. This script rebuilds them and writes them to
ONE small JSON so that no future session pays the crawl again.

Streams companyfacts rather than caching them: the facts are 5-30 MB each and
several thousand firms would be tens of GB for a table that is a few hundred KB.
"""
from __future__ import annotations

import json
import csv
import io
import os
import pathlib
import sys
import time
import zipfile
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
from wealth_tensor import edgar as E  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "pre-002-events.json"
UCACHE = ROOT / "data" / ".universes"
UCACHE.mkdir(exist_ok=True)
SUB_QUARTERS = [f"{y}q2" for y in range(2013, 2025)]


def build_universe(sic_lo: int, sic_hi: int) -> dict[int, str]:
    path = UCACHE / f"universe_{sic_lo}_{sic_hi}.json"
    if path.exists():
        return {int(k): v for k, v in json.loads(path.read_text()).items()}
    found: dict[int, str] = {}
    for q in SUB_QUARTERS:
        zpath = UCACHE / f"{q}.zip"
        try:
            if not zpath.exists():
                raw = E._get(
                    "https://www.sec.gov/files/dera/data/"
                    f"financial-statement-data-sets/{q}.zip")
                zpath.write_bytes(raw)
            with zipfile.ZipFile(zpath) as z, z.open("sub.txt") as fh:
                for row in csv.DictReader(
                        io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t"):
                    sic = row.get("sic") or ""
                    if sic.isdigit() and sic_lo <= int(sic) <= sic_hi:
                        found[int(row["cik"])] = row.get("name", "")
            print(f"  {q}: universe now {len(found)}", flush=True)
        except Exception as exc:  # noqa: BLE001
            print(f"  {q}: SKIPPED ({exc})", flush=True)
        finally:
            if zpath.exists():
                zpath.unlink()
    path.write_text(json.dumps({str(k): v for k, v in found.items()}))
    return found


def facts_streaming(cik: int) -> dict:
    """companyfacts with NO disk cache -- fetch, parse, discard."""
    c = f"{int(cik):010d}"
    raw = E._get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json")
    time.sleep(0.11)
    return json.loads(raw)


def collect(universe: dict[int, str], label: str):
    events, drops, seen = [], defaultdict(int), 0
    t0 = time.time()
    for i, (cik, name) in enumerate(sorted(universe.items()), 1):
        try:
            facts = facts_streaming(cik)
        except Exception:  # noqa: BLE001
            drops["no_revenue_tag"] += 1
            continue
        seen += 1
        try:
            events.extend(E.extract_events(facts, str(cik), name, drops,
                                           include_annual_attributed=True,
                                           onset_rule="peak", signal="revenue"))
        except Exception as exc:  # noqa: BLE001
            print(f"  !! {cik} extract failed: {exc}", flush=True)
        del facts
        if i % 50 == 0:
            el = time.time() - t0
            print(f"  [{label}] {i}/{len(universe)} firms · {len(events)} events "
                  f"· {el/60:.1f} min · eta {(el/i)*(len(universe)-i)/60:.1f} min",
                  flush=True)
    return events, dict(drops), seen


def main() -> None:
    payload = {"note": "PRE-002 peak-to-charge sample, rebuilt; edgar.py untouched",
               "onset_rule": "peak", "signal": "revenue",
               "materiality_floor": E.MATERIALITY_FLOOR,
               "max_lookback": E.MAX_LOOKBACK, "universes": {}}
    for label, (lo, hi) in (("pilot", E.PILOT_SIC), ("replication", E.REPLICATION_SIC)):
        print(f"\n=== {label}: SIC {lo}-{hi} ===", flush=True)
        uni = build_universe(lo, hi)
        print(f"  {len(uni)} registrants ever filing in range 2013-2024", flush=True)
        ev, drops, seen = collect(uni, label)
        payload["universes"][label] = {
            "sic": [lo, hi], "n_registrants": len(uni), "n_firms_fetched": seen,
            "drops": drops, "n_events": len(ev), "events": ev}
        print(f"  {label}: {len(ev)} events across "
              f"{len({e['cik'] for e in ev})} firms", flush=True)
        OUT.write_text(json.dumps(payload, indent=1))
        print(f"  checkpointed -> {OUT}", flush=True)
    print(f"\nDONE. total events "
          f"{sum(u['n_events'] for u in payload['universes'].values())}", flush=True)


if __name__ == "__main__":
    main()
