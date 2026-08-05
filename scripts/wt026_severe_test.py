#!/usr/bin/env python3
"""Run the WT-026 severe test exactly as registered in PRE-001.

    python3 scripts/wt026_severe_test.py --universe pilot
    python3 scripts/wt026_severe_test.py --universe replication

Nothing here decides anything. Every threshold, tag, rule and statistic comes from
`docs/preregistration/PRE-001-wt026-observability-lag.md` by way of `wealth_tensor.edgar`,
which is the point: the script that produces the number must not be the place the number's
definition lives, or the definition drifts toward the number.

Survivorship
------------
The universe is built from SEC Financial Statement Data Set `sub.txt` files spanning
2013-2024, one quarter per year, rather than from a current list of registrants. A retailer
that went bankrupt in 2017 stopped filing and is absent from any present-day list -- and a
bankrupt retailer is precisely a firm whose deferred information arrived all at once. Building
the universe from today's filers would drop the observations most likely to carry the effect,
in whichever direction it runs.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import pathlib
import sys
import zipfile
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))   # L14

from wealth_tensor import edgar as E     # noqa: E402

CACHE = os.environ.get("WT_EDGAR_CACHE", str(pathlib.Path.home() / ".cache" / "wealth-tensor-edgar"))
SUB_QUARTERS = [f"{y}q2" for y in range(2013, 2025)]


def build_universe(sic_lo: int, sic_hi: int) -> dict[int, str]:
    """CIK -> name for every registrant that filed in range, alive or dead."""
    path = os.path.join(CACHE, f"universe_{sic_lo}_{sic_hi}.json")
    if os.path.exists(path):
        with open(path) as fh:
            return {int(k): v for k, v in json.load(fh).items()}

    os.makedirs(CACHE, exist_ok=True)
    found: dict[int, str] = {}
    for q in SUB_QUARTERS:
        zpath = os.path.join(CACHE, f"{q}.zip")
        try:
            if not os.path.exists(zpath):
                raw = E._get(f"https://www.sec.gov/files/dera/data/financial-statement-data-sets/{q}.zip")
                with open(zpath, "wb") as fh:
                    fh.write(raw)
            with zipfile.ZipFile(zpath) as z, z.open("sub.txt") as fh:
                for row in csv.DictReader(io.TextIOWrapper(fh, "utf-8", errors="replace"),
                                          delimiter="\t"):
                    sic = row.get("sic") or ""
                    if sic.isdigit() and sic_lo <= int(sic) <= sic_hi:
                        found[int(row["cik"])] = row.get("name", "")
            print(f"  {q}: universe now {len(found)}", flush=True)
        except Exception as exc:                              # noqa: BLE001
            print(f"  {q}: SKIPPED ({exc})", flush=True)
        finally:
            if os.path.exists(zpath):
                os.remove(zpath)          # 120MB each; the map is what we keep

    with open(path, "w") as fh:
        json.dump({str(k): v for k, v in found.items()}, fh)
    return found


def collect(universe: dict[int, str], include_annual: bool,
            onset_rule: str = "streak", signal: str = "revenue"):
    events, drops, seen = [], defaultdict(int), 0
    for i, (cik, name) in enumerate(sorted(universe.items()), 1):
        try:
            facts = E.company_facts(cik, CACHE)
        except Exception:                                     # noqa: BLE001
            drops["no_revenue_tag"] += 1
            continue
        seen += 1
        events.extend(E.extract_events(facts, str(cik), name, drops,
                                       include_annual_attributed=include_annual,
                                       onset_rule=onset_rule, signal=signal))
        if i % 50 == 0:
            print(f"  {i}/{len(universe)} firms, {len(events)} events", flush=True)
    return events, drops, seen


def analyse(events: list[dict], label: str, alpha: float = 0.05) -> dict:
    groups = [[e["lag"] for e in events if e["tier"] == t] for t in (0, 1, 2, 3)]
    jt = E.jonckheere_terpstra(groups)
    mw = E.mann_whitney_one_sided(groups[0], groups[3])
    by_firm = defaultdict(list)
    for e in events:
        by_firm[e["cik"]].append(e)
    lo, hi = E.bootstrap_median_diff(by_firm, 3, 0)
    out = {
        "label": label,
        "n_events": len(events),
        "n_firms": len(by_firm),
        "by_tier": {
            E.TIER_NAMES[t]: {
                "n": len(groups[t]),
                "median_lag": E.median(groups[t]),
                "iqr": list(E.iqr(groups[t])),
                "mean_lag": (sum(groups[t]) / len(groups[t])) if groups[t] else float("nan"),
            } for t in (0, 1, 2, 3)},
        "jonckheere_terpstra": jt,
        "mann_whitney_t3_vs_t0": mw,
        "median_diff_t3_minus_t0": E.median(groups[3]) - E.median(groups[0]),
        "bootstrap_ci_95": [lo, hi],
        "censored_share": (sum(1 for e in events if e["censored"]) / len(events)) if events else 0.0,
        "annual_attributed_share": (sum(1 for e in events if e["annual_attributed"]) / len(events))
        if events else 0.0,
    }
    # PRE-001 s7: an underpowered test is INCONCLUSIVE, never a pass.
    underpowered = len(groups[0]) < 10 or len(groups[3]) < 10
    passes = (not underpowered
              and jt["p_one_sided"] < alpha
              and E.median(groups[3]) > E.median(groups[0]))
    out["alpha"] = alpha
    out["verdict"] = "INCONCLUSIVE (underpowered)" if underpowered else (
        "PREDICTION SURVIVES" if passes else "PREDICTION FAILS")
    return out


def show(r: dict) -> None:
    print(f"\n===== {r['label']} =====")
    print(f"  {r['n_events']} events across {r['n_firms']} firms")
    print(f"  {'tier':<32}{'n':>6}{'median':>9}{'IQR':>14}{'mean':>8}")
    for name, d in r["by_tier"].items():
        q = d["iqr"]
        print(f"  {name:<32}{d['n']:>6}{d['median_lag']:>9.1f}"
              f"{f'{q[0]:.1f}-{q[1]:.1f}':>14}{d['mean_lag']:>8.2f}")
    jt = r["jonckheere_terpstra"]
    print(f"  Jonckheere-Terpstra  J={jt['J']:.0f}  z={jt['z']:.3f}  p(1-sided)={jt['p_one_sided']:.5f}")
    mw = r["mann_whitney_t3_vs_t0"]
    print(f"  Mann-Whitney t3>t0   z={mw['z']:.3f}  p={mw['p_one_sided']:.5f}")
    ci = r["bootstrap_ci_95"]
    print(f"  median(t3)-median(t0) = {r['median_diff_t3_minus_t0']:+.1f} quarters"
          f"  [95% CI {ci[0]:+.1f}, {ci[1]:+.1f}]")
    print(f"  censored {r['censored_share']:.1%} · annual-attributed {r['annual_attributed_share']:.1%}")
    print(f"  VERDICT: {r['verdict']}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--universe", choices=("pilot", "replication"), default="pilot")
    ap.add_argument("--onset", choices=("streak", "peak"), default="streak",
                    help="streak = PRE-001 as registered; peak = PRE-002 s2")
    ap.add_argument("--signal", choices=("revenue", "opinc_addback"), default="revenue")
    ap.add_argument("--alpha", type=float, default=None,
                    help="PRE-001 registers 0.05; PRE-002 s4 registers 0.025 for two looks")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    alpha = args.alpha if args.alpha is not None else (0.025 if args.onset == "peak" else 0.05)

    lo, hi = E.PILOT_SIC if args.universe == "pilot" else E.REPLICATION_SIC
    print(f"Universe: SIC {lo}-{hi} ({args.universe})")
    universe = build_universe(lo, hi)
    print(f"  {len(universe)} registrants ever filing in range 2013-2024")

    reg = "PRE-002 peak-to-charge" if args.onset == "peak" else "PRE-001 as registered"
    print(f"Instrument: {reg} · signal={args.signal} · alpha={alpha}")
    events, drops, seen = collect(universe, include_annual=True,
                                  onset_rule=args.onset, signal=args.signal)
    primary = analyse(events, f"{args.universe} SIC {lo}-{hi} · PRIMARY ({reg})", alpha)

    strict = [e for e in events if not e["annual_attributed"]]
    sens_a = analyse(strict, "SENSITIVITY · annual-attributed charges excluded", alpha)
    uncens = [e for e in events if not e["censored"]]
    sens_b = analyse(uncens, "SENSITIVITY · right-censored events excluded", alpha)

    one_per: dict[str, dict] = {}
    for e in events:
        if e["cik"] not in one_per or e["severity"] > one_per[e["cik"]]["severity"]:
            one_per[e["cik"]] = e
    sens_c = analyse(list(one_per.values()),
                     "SENSITIVITY · one event per firm (largest charge)", alpha)

    for r in (primary, sens_a, sens_b, sens_c):
        show(r)

    # PRE-002 s3: controls. Reported for both instruments -- a null needs its own detectability
    # attached, and a positive needs proof the pipeline cannot manufacture one.
    perm = E.permutation_null(events, n_perm=1000)
    print("\n  NEGATIVE CONTROL (tier labels permuted, lag distribution held fixed):")
    print(f"    null z: mean {perm['z_mean']:+.3f}, sd {perm['z_sd']:.3f} over {perm['n_perm']} draws"
          "   (must be ~0 +/- ~1 or nothing here is reportable)")
    print(f"    observed z {perm['observed_z']:+.3f} -> empirical p = {perm['p_empirical']:.4f}"
          "   (does not rely on the normal approximation)")
    sizes = [primary["by_tier"][E.TIER_NAMES[t]]["n"] for t in (0, 1, 2, 3)]
    pool = [e["lag"] for e in events]
    print("  POWER (what this design could have detected, at these sizes and this spread):")
    for eff in (0.5, 1.0, 2.0, 3.0):
        pw = E.synthetic_power(sizes, pool, effect_per_tier=eff, n_trials=400, alpha=alpha)
        print(f"    {eff:>4.1f} quarters per tier -> power {pw['power']:.2f}")

    print("\n  drop accounting (PRE-001 s9).  NOTE: duplicate_restated_fact counts SUPERSEDED")
    print("  FACTS replaced by a later filing, not events dropped -- restatement is routine.")
    for k in E.DROP_BUCKETS:
        print(f"    {k:<28}{drops.get(k, 0):>8}")
    print(f"    {'firms with facts fetched':<28}{seen:>8}")

    payload = {"universe": args.universe, "instrument": reg, "onset": args.onset,
               "signal": args.signal, "alpha": alpha,
               "permutation_control": perm,
               "sic": [lo, hi], "n_registrants": len(universe),
               "n_firms_fetched": seen, "drops": dict(drops),
               "primary": primary, "sensitivities": [sens_a, sens_b, sens_c],
               "events": events}
    out = args.out or os.path.join(CACHE, f"wt026_{args.universe}_{args.onset}.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=1)
    print(f"\n  written: {out}")


if __name__ == "__main__":
    main()
