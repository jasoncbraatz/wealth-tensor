#!/usr/bin/env python3
"""END-TO-END-001 · leg E1b — the iso-kappa locus inside the flow base.

WHAT THIS ANSWERS, and it is not a question about redistribution
----------------------------------------------------------------
`END-TO-END-001` (docs/END-TO-END-001.md) tests whether the corpus's Paper II <-> Paper III
join is load-bearing or vocabulary. Paper III's reported series identifies the PRODUCT
phi*delta and nothing about the factor (Paper III §4.2). Paper II asserts the two layers are
"the same structure ... seen from two sides" (§3.2). If Paper II's (r, rho) stand in the same
relation to Paper II's observable, Paper II carries an unstated non-identification result of
exactly Paper III's shape and the chain predicted it. If they do not, the sovereign link is a
resemblance.

THE REASON THIS IS A TEST AND NOT ALGEBRA
-----------------------------------------
The committed implementation does not make kappa a clean product of r and rho:

    recognised_flow += rho * gain + wage        # the wage enters UNSCALED by rho
    assessed = max(recognised_flow, 0.0)        # and the clip is non-linear

So r scales the liability while rho scales the base's DISPERSION toward a wage floor. Whether
the observable can tell those apart at matched kappa is not stated anywhere in the corpus.
The locus is therefore located NUMERICALLY, off `src/wealth_tensor/redistribution.py`, never
off the paper's closed form.

REGISTERED THRESHOLDS -- fixed by END-TO-END-001 §2/E1b and §5, not re-chosen here
---------------------------------------------------------------------------------
  * kappa matched to 1 % relative
  * within-point spread measured over >= 20 seeds at the same (r, rho)
  * separation >= 3x the within-point spread on ANY of the three registered observables = FAIL
  * <= 1x on ALL three across the whole admissible locus                              = REFUTED
  * between                                                                           = UNDECIDED
  * no non-trivial locus                                                              = VOID

THE THREE REGISTERED OBSERVABLES
--------------------------------
  1. stationary Gini      -- simulation, tail-quarter mean (redistribution.stationary_gini)
  2. top-decile share     -- simulation, final cross-section (redistribution.top_share)
  3. Var[log a]           -- Paper II §3.1's own instrument for this exact comparison, i.e. the
                             variance of the log of the normalised per-period multiplier.
                             Computed with the COMMITTED quadrature in scripts/wt077_tail_index.py
                             (`A_flow`, `E`, `MU`), which is where §3.1's 0.076542 / 0.076536 /
                             0.051189 come from.

  DISCLOSURE, stated here rather than discovered later: wt077's A_flow is the LARGE-w limit
  A(eta) = 1 + eta - r*rho*max(eta, 0), which depends on r and rho only through the PRODUCT
  r*rho. On a locus that is nearly an iso-(r*rho) locus this instrument therefore has very
  little room to move, and that is a property of the instrument, not a result. It is reported
  because the design names it and because Paper II uses it; the discriminating weight sits on
  the two simulation observables. A fourth statistic, Var[log w] of the final cross-section, is
  reported as SUPPLEMENTARY and is NOT part of the verdict -- the design fixes three observables
  and a run may not add a fourth to its own failure criterion.

Var[log a] is measured analytically rather than from the simulated path for one reason: the
committed `run()` does not return the wealth path, and `src/` may not be edited -- Paper II §7
pins d655501 as "the last commit touching src/", and moving that pin to take a measurement
would break a published provenance claim to make a number more convenient.

USAGE
-----
    python3 scripts/e2e001_e1_iso_kappa.py            # full run, ~10-20 min
    python3 scripts/e2e001_e1_iso_kappa.py --quick    # 4 seeds, 2 targets, smoke test only
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "src"))
sys.path.insert(0, str(HERE))

from wealth_tensor.redistribution import (  # noqa: E402
    RedistributiveEconomy,
    stationary_gini,
    top_share,
)
from wt077_tail_index import MU, A_flow, E as quad_E  # noqa: E402

# ---- the paper's standard parameters (paper-II §2.1), not free here ----------------------
N_AGENTS, GROWTH_MEAN, GROWTH_SD, WAGE, PERIODS = 800, 0.05, 0.20, 0.05, 1200

# ---- registered by END-TO-END-001 §2/E1b -------------------------------------------------
KAPPA_TOL = 0.01          # 1 % relative match
FAIL_AT = 3.0             # >= 3x the within-point spread on any observable
REFUTE_AT = 1.0           # <= 1x on all three

# The ladder is fixed BEFORE any statistic is computed and spans the attainable range: the
# flow base's maximum kappa is ~0.1026 (r = rho = 1), and 0.10 is the matched budget Paper II
# §3.1 itself uses. Every attainable target is reported; none is dropped for its answer.
KAPPA_TARGETS = (0.005, 0.010, 0.020, 0.050, 0.100)
RHO_GRID = (1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05)
SEEDS = tuple(range(20))


def _econ(rate, rho, seed):
    return RedistributiveEconomy(
        n_agents=N_AGENTS, growth_mean=GROWTH_MEAN, growth_sd=GROWTH_SD, wage=WAGE,
        base="flow", rate=rate, periodicity=1, threshold=0.0, realization=rho, seed=seed,
    )


def point(rate, rho, seeds):
    """Every registered observable at one (r, rho), across `seeds`."""
    gini, top, vlw, kap = [], [], [], []
    for s in seeds:
        res = _econ(rate, rho, s).run(PERIODS)
        gini.append(stationary_gini(res))
        top.append(top_share(res))
        kap.append(res["kappa"])
        w = np.asarray(res["wealth"], dtype=float)
        w = w[w > 0]
        vlw.append(float(np.var(np.log(w))) if w.size > 1 else float("nan"))
    return {"gini": np.array(gini), "top_decile": np.array(top),
            "var_log_w": np.array(vlw), "kappa": np.array(kap)}


def var_log_a(rate, rho):
    """Paper II §3.1's instrument, on the committed wt077 quadrature."""
    afn = A_flow(rate, rho)
    lg = lambda e: np.log(np.maximum(afn(e), 1e-300) / (1.0 + MU))  # noqa: E731
    return quad_E(lambda e: lg(e) ** 2) - quad_E(lg) ** 2


def solve_rate(target, rho, seeds, max_iter=12):
    """r such that the seed-mean kappa hits `target` to within KAPPA_TOL, or None."""
    def kap(r):
        return float(np.mean([_econ(r, rho, s).run(PERIODS)["kappa"] for s in seeds]))

    k_hi = kap(1.0)
    if k_hi < target * (1.0 - KAPPA_TOL):
        return None, k_hi          # unattainable at this rho even at r = 1
    lo, hi = 1e-6, 1.0
    r = min(1.0, max(1e-6, target / max(k_hi, 1e-12)))   # kappa is near-linear in r
    for _ in range(max_iter):
        k = kap(r)
        if abs(k / target - 1.0) <= KAPPA_TOL:
            return r, k
        if k < target:
            lo = r
        else:
            hi = r
        r_lin = r * target / max(k, 1e-12)
        r = r_lin if lo < r_lin < hi else 0.5 * (lo + hi)
    return None, kap(r)


def spread_units(values, spread):
    """Range of point-means, in units of the pooled within-point seed spread."""
    if spread <= 0 or len(values) < 2:
        return float("nan")
    return (max(values) - min(values)) / spread


def resolution_study(seeds):
    """THREAT TO VALIDITY, measured rather than asserted.

    The registered criterion is RELATIVE to the seed spread at the paper's own N = 800. A
    separation that is small against seed noise at N = 800 need not be small at larger N: the
    seed spread falls with N while a systematic drift along the locus does not. Paper III's
    degeneracy is EXACT (held to 7e-14); if Paper II's is merely below the resolution of an
    N = 800 design, the two are the same in SHAPE and not in STRENGTH, and the result document
    has to say so. This block measures which it is. It is a disclosure, not part of the
    verdict -- END-TO-END-001 §5 fixes the thresholds at the paper's standard parameters.
    """
    target = 0.020
    ends = (1.0, 0.2)          # the locus endpoints at kappa* = 0.02: maximum separation
    print("=" * 70)
    print("DISCLOSED SENSITIVITY — is the non-identification exact, or resolution-limited?")
    print(f"  kappa* = {target}, locus endpoints rho = {ends[0]} and {ends[1]}, "
          f"{len(seeds)} seeds")
    print(f"{'N':>7} {'Gini(rho=1.0)':>16} {'Gini(rho=0.2)':>16} {'drift':>10} "
          f"{'seed SD':>9} {'sep':>7}")
    global N_AGENTS
    keep = N_AGENTS
    rows = []
    for n in (800, 1600, 3200, 6400):
        N_AGENTS = n
        means, sds = [], []
        for rho in ends:
            r, _ = solve_rate(target, rho, seeds)
            if r is None:
                means, sds = [], []
                break
            p = point(r, rho, seeds)
            means.append(float(np.mean(p["gini"])))
            sds.append(float(np.std(p["gini"], ddof=1)))
        if not means:
            print(f"{n:7d}   unattainable")
            continue
        drift = abs(means[1] - means[0])
        sd = float(np.sqrt(np.mean(np.square(sds))))
        sep = drift / sd if sd > 0 else float("nan")
        rows.append({"n": n, "gini_hi_rho": means[0], "gini_lo_rho": means[1],
                     "drift": drift, "seed_sd": sd, "sep": sep})
        print(f"{n:7d} {means[0]:16.6f} {means[1]:16.6f} {drift:10.6f} "
              f"{sd:9.6f} {sep:6.2f}x")
    N_AGENTS = keep
    if len(rows) >= 2:
        print("  Read this column, not the verdict: if `sep` climbs with N the degeneracy is")
        print("  RESOLUTION-LIMITED (same shape as Paper III's, weaker in kind); if it is flat")
        print("  the drift is itself seed noise and the degeneracy is structural.")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--resolution", action="store_true",
                    help="run the disclosed N-sensitivity block as well")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    seeds = SEEDS[:4] if args.quick else SEEDS
    targets = KAPPA_TARGETS[1:3] if args.quick else KAPPA_TARGETS
    t0 = time.time()

    print("END-TO-END-001 · E1b — the iso-kappa locus inside the flow base")
    print(f"N={N_AGENTS} mu={GROWTH_MEAN} sigma={GROWTH_SD} a={WAGE} T={PERIODS} "
          f"seeds={len(seeds)} kappa_tol={KAPPA_TOL:.0%}")
    print("registered: FAIL >= 3x seed spread on any of {Gini, top-decile, Var[log a]}; "
          "REFUTED <= 1x on all three; VOID if no non-trivial locus\n")

    out = {"params": {"n": N_AGENTS, "mu": GROWTH_MEAN, "sigma": GROWTH_SD, "wage": WAGE,
                      "T": PERIODS, "seeds": list(seeds), "kappa_tol": KAPPA_TOL},
           "loci": []}

    for target in targets:
        print(f"=== kappa* = {target:.4f} " + "=" * 52)
        print(f"{'rho':>5} {'r':>8} {'kappa':>9} {'Gini':>18} {'top10%':>18} "
              f"{'Var[log a]':>11} {'Var[log w]':>16}")
        rows = []
        for rho in RHO_GRID:
            r, k = solve_rate(target, rho, seeds)
            if r is None:
                print(f"{rho:5.2f} {'--':>8} {'--':>9}   unattainable (max kappa "
                      f"at r=1 is {k:.5f})")
                continue
            p = point(r, rho, seeds)
            vla = var_log_a(r, rho)
            rows.append({"rho": rho, "rate": r, "kappa": float(np.mean(p["kappa"])),
                         "gini_mean": float(np.mean(p["gini"])),
                         "gini_sd": float(np.std(p["gini"], ddof=1)),
                         "top_mean": float(np.mean(p["top_decile"])),
                         "top_sd": float(np.std(p["top_decile"], ddof=1)),
                         "var_log_a": float(vla),
                         "vlw_mean": float(np.mean(p["var_log_w"])),
                         "vlw_sd": float(np.std(p["var_log_w"], ddof=1))})
            rr = rows[-1]
            print(f"{rho:5.2f} {r:8.5f} {rr['kappa']:9.5f} "
                  f"{rr['gini_mean']:11.5f}+-{rr['gini_sd']:.5f} "
                  f"{rr['top_mean']:11.5f}+-{rr['top_sd']:.5f} "
                  f"{vla:11.6f} {rr['vlw_mean']:9.4f}+-{rr['vlw_sd']:.4f}")

        if len(rows) < 2:
            print("  -> VOID for this target: no non-trivial locus (fewer than two "
                  "matched (r, rho) pairs)\n")
            out["loci"].append({"target": target, "rows": rows, "verdict": "VOID"})
            continue

        # pooled within-point spread = RMS of the per-point seed SDs
        sd_g = float(np.sqrt(np.mean([x["gini_sd"] ** 2 for x in rows])))
        sd_t = float(np.sqrt(np.mean([x["top_sd"] ** 2 for x in rows])))
        sd_v = float(np.sqrt(np.mean([x["vlw_sd"] ** 2 for x in rows])))
        sep_g = spread_units([x["gini_mean"] for x in rows], sd_g)
        sep_t = spread_units([x["top_mean"] for x in rows], sd_t)
        # Var[log a] is analytic: it has no seed spread of its own. Its separation is scored
        # against the Gini's seed spread ONLY as a scale of last resort, and is reported
        # alongside its own raw range so a reader can see it is not doing the work.
        rng_a = max(x["var_log_a"] for x in rows) - min(x["var_log_a"] for x in rows)
        sep_v = rng_a / sd_g if sd_g > 0 else float("nan")
        sep_w = spread_units([x["vlw_mean"] for x in rows], sd_v)

        worst = max(sep_g, sep_t, sep_v)
        verdict = ("FAIL" if worst >= FAIL_AT
                   else "REFUTED" if max(sep_g, sep_t, sep_v) <= REFUTE_AT
                   else "UNDECIDED")
        print(f"  locus points: {len(rows)}  rho span {min(x['rho'] for x in rows):.2f}"
              f"-{max(x['rho'] for x in rows):.2f}")
        print(f"  within-point seed spread (pooled SD): Gini {sd_g:.5f}  "
              f"top10% {sd_t:.5f}  Var[log w] {sd_v:.4f}")
        print(f"  separation across the locus, in seed-spread units: "
              f"Gini {sep_g:.2f}x  top10% {sep_t:.2f}x  Var[log a] {sep_v:.2f}x  "
              f"(supplementary Var[log w] {sep_w:.2f}x)")
        print(f"  -> {verdict} at kappa* = {target:.4f}\n")
        out["loci"].append({"target": target, "rows": rows, "verdict": verdict,
                            "sep": {"gini": sep_g, "top_decile": sep_t,
                                    "var_log_a": sep_v, "var_log_w_supp": sep_w},
                            "sd": {"gini": sd_g, "top_decile": sd_t, "var_log_w": sd_v}})

    scored = [l for l in out["loci"] if l["verdict"] != "VOID"]
    print("=" * 70)
    if not scored:
        leg = "VOID"
    elif any(l["verdict"] == "FAIL" for l in scored):
        leg = "FAIL"
    elif all(l["verdict"] == "REFUTED" for l in scored):
        leg = "REFUTED"
    else:
        leg = "UNDECIDED"
    out["leg_verdict"] = leg
    print(f"E1b LEG VERDICT: {leg}")
    print("  (FAIL on any attainable target is FAIL: the design's failure criterion is "
          "'on ANY of the three observables', and a locus that separates anywhere is a "
          "locus on which the observable identifies the factors.)")
    if args.resolution:
        out["resolution_study"] = resolution_study(seeds)
    print(f"  elapsed {time.time() - t0:.0f}s")

    dest = args.json or str(HERE.parent / "docs" / "notes" / "e2e001-e1b-iso-kappa.json")
    pathlib.Path(dest).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(dest).write_text(json.dumps(out, indent=2))
    print(f"  json -> {dest}")


if __name__ == "__main__":
    main()
