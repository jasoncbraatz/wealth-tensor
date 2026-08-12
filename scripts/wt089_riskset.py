#!/usr/bin/env python3
"""REG-003 §2, second pass: the eligible-quarter risk set, for firms with events.

A quarter is ELIGIBLE for firm f when an event could have been recorded there:
an assets denominator exists in one of the five preceding quarters AND
`peak_onset` resolves from the same revenue series `extract_events` uses.
That is exactly the set of quarters `extract_events` would have admitted, so the
§4 null permutes within the opportunity set and not within an invented one.

Computes no statistic. Registered before it ran.
"""
from __future__ import annotations

import json
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
from wealth_tensor import edgar as E  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent / "data"
OUT = HERE / "pre-002-riskset.json"


def facts_streaming(cik: int) -> dict:
    c = f"{int(cik):010d}"
    raw = E._get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json")
    time.sleep(0.11)
    return json.loads(raw)


def eligible_quarters(facts: dict) -> list[int]:
    revenue, rev_tag, _ = E.duration_series(facts, E.REVENUE_TAGS)
    if rev_tag is None or len(revenue) < E.MIN_HISTORY_QUARTERS:
        return []
    assets = E.instant_series(facts, E.ASSETS_TAG)
    if not assets:
        return []
    out = []
    for q in sorted(revenue):
        denom = next((assets[k] for k in range(q - 1, q - 6, -1) if k in assets), None)
        if not denom or denom <= 0:
            continue
        onset, _c = E.peak_onset(revenue, q)
        if onset is None:
            continue
        out.append(q)
    return out


def main() -> None:
    payload = json.loads((HERE / "pre-002-events.json").read_text())
    ciks = sorted({e["cik"] for u in payload["universes"].values()
                   for e in u["events"]}, key=int)
    print(f"{len(ciks)} firms with events", flush=True)
    risk: dict[str, list[int]] = {}
    t0 = time.time()
    for i, cik in enumerate(ciks, 1):
        try:
            risk[cik] = eligible_quarters(facts_streaming(int(cik)))
        except Exception as exc:  # noqa: BLE001
            print(f"  !! {cik}: {exc}", flush=True)
            risk[cik] = []
        if i % 40 == 0:
            el = time.time() - t0
            print(f"  {i}/{len(ciks)} · {el/60:.1f} min · "
                  f"eta {(el/i)*(len(ciks)-i)/60:.1f} min", flush=True)
    OUT.write_text(json.dumps(risk))
    sizes = [len(v) for v in risk.values()]
    print(f"\nDONE. median risk-set size {sorted(sizes)[len(sizes)//2]} quarters; "
          f"{sum(1 for s in sizes if s == 0)} firms with an empty risk set", flush=True)


if __name__ == "__main__":
    main()
