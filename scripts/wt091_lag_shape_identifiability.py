#!/usr/bin/env python3
"""WT-091 · REG-005 · is the recognition lag's SHAPE identified from a reported series?

Run exactly as registered in `docs/preregistration/REG-005-p3-lag-shape-
identifiability.md`, committed and pushed (6f0e7be) before this file existed.

    ./.venv/bin/python scripts/wt091_lag_shape_identifiability.py

Nothing here decides anything. Every ladder boundary, tolerance, sweep grid, metric and
predicted direction comes from REG-005. Ladders I, P, W, S and N are exhaustive.

THE QUESTION (REG-005 §0). Section 4.2 proves an impossibility by counting: a reported
series is a sum of two geometrics, so it holds four numbers -- two roots, two amplitudes
-- against five parameters, and the shortfall lands on phi. That count assumed a constant
recognition hazard. REG-004 replaced it with an arbitrary lag distribution T >= 1, which
is not one more parameter but an INFINITE-DIMENSIONAL object. Is the extra structure
visible?

    c(t) = D^t + (1-phi) * delta * SUM_{a=1..t} D^(t-a) * S(a),   D = 1-delta

normalised so c(0) = 1, which is section 4.2's FAVOURABLE case (the physical scale is
granted). Every negative result below is therefore a fortiori; a positive one would hold
only for an asset followed from acquisition. REG-005 section 1.

THE METRIC IS REGISTERED AND THE OBVIOUS ONE IS REGISTERED AS WRONG (REG-005 section 4).
Relative-per-point RMS, not norm-relative. Under the norm-relative metric a geometrically
decaying series' late points contribute nothing, so ladder S -- does a longer series help?
-- would land on S3 by construction, having measured the decay of C rather than the
information in it.

THE GUARD IS AN OPTIMISER, AND -16's QUESTION APPLIES TO IT (REG-005 section 3).
A converged flag cannot tell a true minimum from a canyon floor flat to machine
precision, exactly as a term ratio could not tell an exhausted tail from an underflowed
one. Repairs, all registered: >= 64 deterministic starts; report the canyon's DIAMETER,
not its argmin; survival by multiplicative recursion, never as a quotient of two survival
values; and REFUSE a run whose best objective equals its worst start to machine precision.

NOTE ON ORDER (the trap -14 paid two round trips for): severity.check() EXECUTES its
witness immediately, so every helper is defined ABOVE the first check that uses it.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import pathlib
import sys

import numpy as np
from scipy.optimize import minimize
from scipy.signal import lfilter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from severity import check, DEFINITIONAL, summary  # noqa: E402

# ---- everything below is fixed by REG-005; nothing is chosen at run time -------------
K_HAT = 1.21                     # RESULT-REG-003 §3, discrete Weibull profile MLE
Q_HAT = 0.9213424092985028       # RESULT-REG-003 §3
ALPHA_Q_HAT = 0.12272272272272272    # RESULT-REG-003 §2, censored geometric MLE, pooled
K_CI_WIDTH = 0.150               # RESULT-REG-003 §3, [1.135, 1.285]
K_WITNESS = 0.5                  # REG-005 §2 F3, the world the geometric must NOT fit

NEST_TOL = 1e-12                 # REG-005 §2 F1, F4
F2_TOL = 1e-6                    # REG-005 §2 F2
CONFLUENT_EPS = 1e-9             # REG-005 §3 Q3.2, the removable singularity at a = d
CANYON_SLACK = 1e-6              # REG-005 §3 Q4.2, the (1+eps) level set

N_DEFAULT = 40                   # quarters, REG-005 §5 ladder I
N_LADDER_S = (20, 40, 80, 400)   # REG-005 §5 ladder S
SIGMA_GRID = (1e-6, 1e-4, 1e-3, 1e-2)          # REG-005 §5 ladder W
SIGMA_LADDER_W = 1e-3                          # ladder W is read here
SIGMA_GRID_N = (1e-4, 1e-3, 1e-2)              # REG-005 §5 ladder N
N_DRAWS = 200                                  # REG-005 §5 ladder N
DRAW_SEED = 20260812                           # recorded, per REG-005 §5
K_SWEEP = (0.6, 2.0)                           # REG-005 §3 Q1, the reported k range
K_GRID_N = 141                                 # 0.6 .. 2.0 by 0.01

# The disclosed rectangle, annual (ASC 360 / ASC 350-30-50 lives), REG-005 §5 ladder I.
LIVES_YEARS = (3.0, 5.0, 10.0, 20.0, 40.0)
PHI_GRID = (0.20, 0.40, 0.60, 0.80)            # §4.4's four tabulated tiers

ALPHA_A_HAT = 1.0 - (1.0 - ALPHA_Q_HAT) ** 4   # 0.408/yr, the event-date MLE


# ======================================================================================
# §0 · lag distributions.  Each exposes S(a) = P(T >= a) for a >= 1, by MULTIPLICATIVE
#      RECURSION and never as a quotient of two survival values (REG-005 §3 Q4.3).
# ======================================================================================
def weibull_survival(k: float, q: float, n: int) -> np.ndarray:
    """S(a) = q^(a^k) for a = 1..n, carried in log space.

    The exponent is accumulated as a**k directly rather than as a ratio of two
    survival values, which is the REG-004 repair: for a decreasing hazard the survival
    underflows to 0.0 while the term is still large, and a quotient reads that as an
    exhausted tail.
    """
    a = np.arange(1, n + 1, dtype=float)
    return np.exp(np.power(a, k) * math.log(q))


def geometric_survival(alpha: float, n: int) -> np.ndarray:
    """S(a) = (1-alpha)^(a-1), the constant hazard.  Constant ratio, in closed form."""
    a = np.arange(1, n + 1, dtype=float)
    return np.exp((a - 1.0) * math.log1p(-alpha))


# ======================================================================================
# §1 · the reported series, normalised to c(0) = 1
# ======================================================================================
def series_from_survival(surv: np.ndarray, delta: float, phi: float, n: int) -> np.ndarray:
    """c(t) = D^t + (1-phi) delta SUM_{a=1..t} D^(t-a) S(a),  t = 0..n.

    The inner sum is the one-pole recursion g(i) = D g(i-1) + S(i), run as a linear
    filter rather than as D^(-a) times a running sum -- D^(-a) overflows well before
    n = 400 and the overflow would arrive as a silent inf, which is the same failure
    mode as -16's underflowed tail wearing the other sign.
    """
    D = 1.0 - delta
    t = np.arange(0, n + 1, dtype=float)
    base = np.power(D, t)
    gap = np.zeros(n + 1)
    gap[1:] = lfilter([1.0], [1.0, -D], surv[:n])
    return base + (1.0 - phi) * delta * gap


def series_weibull(k, q, delta, phi, n):
    return series_from_survival(weibull_survival(k, q, n), delta, phi, n)


def series_geometric(alpha, delta, phi, n):
    return series_from_survival(geometric_survival(alpha, n), delta, phi, n)


def series_closed_form(alpha, delta, phi, n):
    """§4.2's published closed form, with the confluent limit at alpha = delta."""
    A, D = 1.0 - alpha, 1.0 - delta
    t = np.arange(0, n + 1, dtype=float)
    if abs(delta - alpha) < CONFLUENT_EPS:
        # lim_{a->d}: c(t) = D^t [1 + (1-phi) delta t / (1-delta)]
        return np.power(D, t) * (1.0 + (1.0 - phi) * delta * t / D)
    return (delta * (1.0 - phi) * np.power(A, t)
            - (alpha - phi * delta) * np.power(D, t)) / (delta - alpha)


# ======================================================================================
# §2 · the metric (REG-005 §4), and the mimic search (REG-005 §3 Q4)
# ======================================================================================
def eps_rel(fit: np.ndarray, target: np.ndarray) -> float:
    """Relative-per-point RMS over t = 1..N.  t = 0 is 1.0 in both by construction."""
    r = (fit[1:] - target[1:]) / target[1:]
    return float(np.sqrt(np.mean(r * r)))


def _clip01(x, lo=1e-9, hi=1.0 - 1e-9):
    return min(max(x, lo), hi)


def fit_mimic(target, n, admissible: bool, starts=None):
    """Best constant-hazard (geometric-lag) world for `target`.

    Returns dict with the argmin, the objective, and the DIAMETER of the set of starts
    landing within (1+CANYON_SLACK) of the best objective -- REG-005 §3 Q4.2, which is
    the reported quantity rather than the argmin.
    """
    if starts is None:
        starts = MIMIC_STARTS
    phi_lo, phi_hi = (0.0, 1.0) if admissible else (-5.0, 5.0)
    bnds = [(1e-6, 1.0 - 1e-6), (1e-6, 1.0 - 1e-6), (phi_lo, phi_hi)]

    def obj(p):
        a, d, ph = p
        if admissible and ph * d > a:
            return 1e6 + (ph * d - a)          # §4.2 admissibility, REG-005 §3 Q3.1
        try:
            return eps_rel(series_geometric(a, d, ph, n), target)
        except (FloatingPointError, ValueError):
            return 1e9

    best, results = None, []
    worst_start = -1.0
    for s in starts:
        worst_start = max(worst_start, obj(s))
        r = minimize(obj, s, method="L-BFGS-B", bounds=bnds,
                     options={"maxiter": 4000, "ftol": 1e-18, "gtol": 1e-14})
        results.append((float(r.fun), np.asarray(r.x, dtype=float)))
        if best is None or r.fun < best[0]:
            best = (float(r.fun), np.asarray(r.x, dtype=float))
    level = best[0] * (1.0 + CANYON_SLACK) + 1e-18
    near = [x for f, x in results if f <= level]
    diam = 0.0
    for u, v in itertools.combinations(near, 2):
        diam = max(diam, float(np.max(np.abs(u - v))))
    arr = np.array(near)
    span = (arr.max(axis=0) - arr.min(axis=0)).tolist() if len(near) else [0.0, 0.0, 0.0]
    # is the canyon exactly §4.2's mirror pair?  (alpha,delta,phi) -> (delta,alpha,phi d/a)
    a0, d0, p0 = best[1]
    mir = np.array([d0, a0, p0 * d0 / a0])
    mirror_found = min((float(np.max(np.abs(x - mir))) for x in near), default=9.9)
    return {"eps": best[0], "alpha": best[1][0], "delta": best[1][1], "phi": best[1][2],
            "canyon_diameter": diam, "canyon_span": span, "n_at_optimum": len(near),
            "mirror_distance": mirror_found,
            "worst_start_obj": float(worst_start), "n_starts": len(starts)}


def fit_weibull_free_k(target, n, k, starts=None):
    """Best (q, delta, phi) for a FIXED shape k -- ladder W's inner minimisation."""
    if starts is None:
        starts = WEIBULL_STARTS
    bnds = [(0.05, 1.0 - 1e-9), (1e-6, 1.0 - 1e-6), (0.0, 1.0)]

    def obj(p):
        q, d, ph = p
        try:
            return eps_rel(series_weibull(k, q, d, ph, n), target)
        except (FloatingPointError, ValueError):
            return 1e9

    best = None
    for s in starts:
        r = minimize(obj, s, method="L-BFGS-B", bounds=bnds,
                     options={"maxiter": 4000, "ftol": 1e-18, "gtol": 1e-14})
        if best is None or r.fun < best[0]:
            best = (float(r.fun), np.asarray(r.x, dtype=float))
    return best[0], best[1]


def fit_weibull_full(target, n, starts):
    """Best (k, q, delta, phi) jointly -- ladder N's estimator on a noisy series."""
    bnds = [K_SWEEP, (0.05, 1.0 - 1e-9), (1e-6, 1.0 - 1e-6), (0.0, 1.0)]

    def obj(p):
        k, q, d, ph = p
        try:
            return eps_rel(series_weibull(k, q, d, ph, n), target)
        except (FloatingPointError, ValueError):
            return 1e9

    best = None
    for s in starts:
        r = minimize(obj, s, method="L-BFGS-B", bounds=bnds,
                     options={"maxiter": 4000, "ftol": 1e-18, "gtol": 1e-14})
        if best is None or r.fun < best[0]:
            best = (float(r.fun), np.asarray(r.x, dtype=float))
    return best[0], best[1]


# ---- the deterministic multi-start grids, REG-005 §3 Q4.1 (>= 64 starts, no seeds) ---
MIMIC_STARTS = [np.array([a, d, p]) for a in (0.03, 0.08, 0.15, 0.30)
                for d in (0.002, 0.01, 0.05, 0.15)
                for p in (0.05, 0.30, 0.60, 0.90)]                      # 64
WEIBULL_STARTS = [np.array([q, d, p]) for q in (0.75, 0.88, 0.95)
                  for d in (0.002, 0.01, 0.05, 0.15)
                  for p in (0.10, 0.40, 0.70, 0.95)]                    # 48
FULL_STARTS = [np.array([k, q, d, p]) for k in (0.8, 1.2, 1.7)
               for q in (0.80, 0.93) for d in (0.005, 0.03, 0.12)
               for p in (0.25, 0.75)]                                   # 36


def yr_to_q(delta_a: float) -> float:
    return 1.0 - (1.0 - delta_a) ** 0.25


def q_to_yr(alpha_q: float) -> float:
    return 1.0 - (1.0 - alpha_q) ** 4


def pgf_outside(surv: np.ndarray, z: float) -> float:
    """Pi(z) = 1 + (z-1) SUM_{a>=1} z^(a-1) S(a).  Used only for alpha_eff, ladder P.

    REG-004's repair was to refuse rather than return once a still-rising term passes
    1e290. A test written to pin §4.9's claim that a decreasing-hazard lag diverges found
    that repair INCOMPLETE: with a truncation shorter than it takes `term` alone to reach
    1e290, the loop runs off the end of the array and returns an astronomically large but
    FINITE number for a divergent sum -- the same defect as -16's underflowed tail, now
    wearing "I ran out of array" instead of "the survival hit zero".

    A guard that certifies convergence has to be able to tell an exhausted tail from a
    TRUNCATED one. So the contribution `z^(a-1) S(a)` is tracked, and reaching the end of
    the array while it is still at its maximum is refused: the tail was never exhausted,
    it was merely stopped.
    """
    tot, term, peak, last = 0.0, 1.0, 0.0, 0.0
    for a in range(1, len(surv) + 1):
        last = term * surv[a - 1]
        peak = max(peak, last)
        tot += last
        term *= z
        if term > 1e290:
            raise OverflowError("REG-004's refusal: still-rising term past 1e290")
    if peak > 0.0 and last >= peak:
        raise OverflowError(
            "tail not exhausted at truncation: the last contribution is still the "
            "largest, so this sum was stopped rather than converged")
    return 1.0 + (z - 1.0) * tot


# RESULT-REG-004 §5's published curve, annual, typed from the manuscript's §4.9 table.
ALPHA_EFF_PUBLISHED = {40.0: 0.4368, 20.0: 0.4388, 10.0: 0.4431, 5.0: 0.4538,
                       3.0: 0.4758}


def alpha_eff_annual(delta_a: float, k=K_HAT, q=Q_HAT, n=6000,
                     conditioned: bool = True) -> float:
    """REG-004's deferral-matching effective rate, alpha_eff(delta) = d Pi(z)/(Pi(z)-1).

    `conditioned` selects the T >= 1 version, which is the one RESULT-REG-004 §5 and
    §4.9's table PRINT -- and getting this wrong is REG-003's T = 0 erratum arriving a
    THIRD time on a THIRD estimator. The fitted Weibull puts 1-q = 7.87% of its mass at
    a lag `peak_onset` cannot produce; dropping it raises E[T] from 6.93 to 7.52 quarters
    and lowers alpha_eff by about 6% at every life. The series cannot see the difference
    at all -- F4 proves the conditioning is a pure phi reparameterisation -- and the
    LEVEL sees it at 6%, which is exactly why a downstream instrument that recomputes
    alpha_eff from the same two fitted constants silently gets the other curve.
    """
    dq = yr_to_q(delta_a)
    z = 1.0 / (1.0 - dq)
    surv = weibull_survival(k, q, n)
    if conditioned:
        surv = surv / surv[0]
    Pi = pgf_outside(surv, z)
    return q_to_yr(dq * Pi / (Pi - 1.0))


# ======================================================================================
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--quick", action="store_true",
                    help="ladder N at 20 draws; robustness only, cannot change a verdict")
    args = ap.parse_args()
    out = {"registration": "REG-005", "k_hat": K_HAT, "q_hat": Q_HAT,
           "alpha_a_hat": ALPHA_A_HAT}

    print("=" * 86)
    print("WT-091 · REG-005 · is the recognition lag's SHAPE identified from a reported "
          "series?")
    print("=" * 86)
    print(f"  k_hat = {K_HAT}  q_hat = {Q_HAT:.9f}  alpha_hat = {ALPHA_A_HAT:.4f}/yr "
          f"(event dates)")
    print(f"  metric: relative-per-point RMS (REG-005 §4).  N = {N_DEFAULT} quarters.")
    print(f"  {len(MIMIC_STARTS)} deterministic starts per mimic fit (REG-005 §3 Q4.1).")
    print()

    # ==================================================================================
    print("§2 · FALSIFIERS ON THE CONSTRUCTION")
    print("-" * 86)

    # ---- F1 · nesting -------------------------------------------------------------
    worst_f1, worst_at = 0.0, None
    for life in LIVES_YEARS:
        d_a = 1.0 / life
        d = yr_to_q(d_a)
        for phi in PHI_GRID:
            for alpha in (0.02, ALPHA_Q_HAT, 0.40):
                a = series_geometric(alpha, d, phi, N_DEFAULT)
                b = series_closed_form(alpha, d, phi, N_DEFAULT)
                dev = float(np.max(np.abs(a - b) / np.abs(b)))
                if dev > worst_f1:
                    worst_f1, worst_at = dev, (life, phi, alpha)
    print(f"  F1 · convolution vs §4.2's closed form at k = 1: worst relative deviation "
          f"{worst_f1:.3e}")
    print(f"       (at {worst_at})")
    out["F1_worst"] = worst_f1
    check("F1 · the general convolution nests §4.2's published closed form at k = 1",
          worst_f1 <= NEST_TOL,
          witness=lambda: float(np.max(np.abs(
              series_weibull(1.6, Q_HAT, 0.05, 0.5, N_DEFAULT)
              - series_closed_form(ALPHA_Q_HAT, 0.05, 0.5, N_DEFAULT))
              / np.abs(series_closed_form(ALPHA_Q_HAT, 0.05, 0.5, N_DEFAULT)))) <= NEST_TOL)

    # ---- F4 · the T = 0 mass is a pure phi reparameterisation ----------------------
    worst_f4 = 0.0
    for life in LIVES_YEARS:
        d = yr_to_q(1.0 / life)
        for phi in PHI_GRID:
            s_raw = weibull_survival(K_HAT, Q_HAT, N_DEFAULT)
            s_cond = s_raw / s_raw[0]                       # conditioned on T >= 1
            base = series_from_survival(s_raw, d, phi, N_DEFAULT)
            # (1-phi) -> (1-phi)/q  i.e.  phi' = 1 - (1-phi)*s_raw[0]
            phi_star = 1.0 - (1.0 - phi) * s_raw[0]
            moved = series_from_survival(s_cond, d, phi_star, N_DEFAULT)
            worst_f4 = max(worst_f4, float(np.max(np.abs(moved - base) / np.abs(base))))
    print(f"  F4 · the T >= 1 conditioning absorbed into phi: worst deviation "
          f"{worst_f4:.3e}")
    print(f"       -> REG-003's T = 0 erratum, which bit REG-004 twice, CANNOT bite here")
    out["F4_worst"] = worst_f4
    check("F4 · conditioning on T >= 1 is exactly a phi reparameterisation",
          worst_f4 <= NEST_TOL,
          witness=lambda: float(np.max(np.abs(
              series_from_survival(weibull_survival(K_HAT, Q_HAT, N_DEFAULT)
                                   / weibull_survival(K_HAT, Q_HAT, N_DEFAULT)[0],
                                   yr_to_q(0.10), 0.60, N_DEFAULT)
              - series_from_survival(weibull_survival(K_HAT, Q_HAT, N_DEFAULT),
                                     yr_to_q(0.10), 0.60, N_DEFAULT))
              / series_from_survival(weibull_survival(K_HAT, Q_HAT, N_DEFAULT),
                                     yr_to_q(0.10), 0.60, N_DEFAULT))) <= NEST_TOL)

    # ---- F2 · non-vacuity of the mimic search -------------------------------------
    f2_worst, f2_detail = 0.0, []
    for (alpha_t, d_a, phi_t) in ((0.12, 0.10, 0.60), (0.30, 0.05, 0.30),
                                  (0.06, 0.20, 0.80)):
        d_t = yr_to_q(d_a)
        tgt = series_geometric(alpha_t, d_t, phi_t, N_DEFAULT)
        r = fit_mimic(tgt, N_DEFAULT, admissible=True)
        truth = np.array([alpha_t, d_t, phi_t])
        mirror = np.array([d_t, alpha_t, phi_t * d_t / alpha_t])
        got = np.array([r["alpha"], r["delta"], r["phi"]])
        dist = min(float(np.max(np.abs(got - truth))), float(np.max(np.abs(got - mirror))))
        f2_worst = max(f2_worst, min(dist, r["eps"]))
        f2_detail.append({"truth": truth.tolist(), "got": got.tolist(),
                          "eps": r["eps"], "param_dist": dist})
        print(f"  F2 · generated (a={alpha_t:.3f}, d={d_t:.4f}, p={phi_t:.2f}) -> "
              f"eps {r['eps']:.2e}, nearest-of-mirror-pair param distance {dist:.2e}")
    out["F2"] = f2_detail
    check("F2 · the mimic search finds the answer when a constant-hazard answer exists",
          f2_worst <= F2_TOL,
          witness=lambda: min(
              fit_mimic(series_weibull(K_WITNESS, Q_HAT, yr_to_q(0.10), 0.60, N_DEFAULT),
                        N_DEFAULT, admissible=True, starts=MIMIC_STARTS[:4])["eps"],
              1.0) <= F2_TOL)

    print()

    # ==================================================================================
    print("§5 · LADDER I · is the shape visible in a NOISELESS series?")
    print("-" * 86)
    print(f"  {'life':>6} {'delta/yr':>9} {'phi':>5} | {'eps admissible':>15} "
          f"{'eps free-phi':>13} | {'alpha_ser/yr':>12} {'phi_mimic':>10} "
          f"{'canyon':>9}")
    I_rows, eps_max, eps_max_at = [], 0.0, None
    eps_free_max = 0.0
    for life in LIVES_YEARS:
        d_a = 1.0 / life
        d = yr_to_q(d_a)
        for phi in PHI_GRID:
            tgt = series_weibull(K_HAT, Q_HAT, d, phi, N_DEFAULT)
            ra = fit_mimic(tgt, N_DEFAULT, admissible=True)
            rf = fit_mimic(tgt, N_DEFAULT, admissible=False)
            # §4.2's exchange: the roots come back as a SET.  alpha_ser is the one that
            # is not delta.  REG-005 §5 ladder P.
            roots = sorted([ra["alpha"], ra["delta"]])
            a_ser_q = roots[1] if abs(roots[0] - d) < abs(roots[1] - d) else roots[0]
            row = {"life": life, "delta_a": d_a, "phi": phi,
                   "eps_admissible": ra["eps"], "eps_free": rf["eps"],
                   "alpha_ser_a": q_to_yr(a_ser_q), "phi_mimic": ra["phi"],
                   "delta_mimic_a": q_to_yr(ra["delta"]),
                   "phi_mimic_free": rf["phi"],
                   "canyon_diameter": ra["canyon_diameter"],
                   "canyon_span": ra["canyon_span"],
                   "mirror_distance": ra["mirror_distance"],
                   "n_at_optimum": ra["n_at_optimum"],
                   "worst_start_obj": ra["worst_start_obj"]}
            I_rows.append(row)
            if ra["eps"] > eps_max:
                eps_max, eps_max_at = ra["eps"], (life, phi)
            eps_free_max = max(eps_free_max, rf["eps"])
            print(f"  {life:>5.0f}y {d_a:>9.4f} {phi:>5.2f} | {ra['eps']:>15.3e} "
                  f"{rf['eps']:>13.3e} | {q_to_yr(a_ser_q):>12.4f} "
                  f"{ra['phi']:>10.4f} {ra['canyon_diameter']:>9.2e}")

    ladder_I = ("I1" if eps_max < 1e-6 else "I2" if eps_max < 1e-3
                else "I3" if eps_max < 1e-2 else "I4")
    out["I_rows"], out["I_eps_max"], out["ladder_I"] = I_rows, eps_max, ladder_I
    print(f"\n  worst eps over the disclosed rectangle: {eps_max:.3e} at "
          f"{eps_max_at[0]:.0f}-year life, phi = {eps_max_at[1]}")
    print(f"  -> LADDER I = {ladder_I}   (predicted I2)")

    # REG-005 §3 Q4.4 -- refuse a run whose best equals its worst start.
    flat = [r for r in I_rows if r["worst_start_obj"] <= r["eps_admissible"] * (1 + 1e-12)]
    check("Q4.4 · no mimic fit is an underflowed optimiser (best == worst start)",
          len(flat) == 0,
          witness=lambda: len([r for r in I_rows
                               if r["worst_start_obj"] <= r["eps_admissible"] * 1e12]) == 0)

    # REG-005 §3 Q3.1 -- did the admissible box, rather than the data, separate them?
    box_bound = [r for r in I_rows
                 if r["eps_admissible"] > r["eps_free"] * 1.01]
    out["box_bound_rows"] = len(box_bound)
    print(f"  the admissible box binds at {len(box_bound)} of {len(I_rows)} settings "
          f"(worst free-phi eps {eps_free_max:.3e})")
    check("Q3.1 · the admissible and free-phi optima are both reported and compared",
          eps_free_max <= eps_max + 1e-15,
          witness=lambda: eps_free_max <= 0.0)

    # REG-005 §3 Q2 -- the share guard.
    visible = [r for r in I_rows if r["eps_admissible"] >= 1e-2]
    invisible = [r for r in I_rows if r["eps_admissible"] < 1e-2]
    share_reportable = bool(visible) and bool(invisible)
    out["share_reportable"] = share_reportable
    print(f"  REG-005 §3 Q2 · visible cells {len(visible)}, invisible {len(invisible)} "
          f"-> share {'REPORTED' if share_reportable else 'WITHHELD (one side empty)'}")
    check("Q2 · a share over the rectangle is reported only if BOTH sides are non-empty",
          share_reportable == (bool(visible) and bool(invisible)),
          witness=DEFINITIONAL(
              "this check pins the guard's own wiring rather than a quantity: it asserts "
              "that the reporting decision equals the non-emptiness test, and there is "
              "no admissible world in which the guard may report on an empty side"))
    print()

    # ==================================================================================
    print("§5 · LADDER P · where does the best-fitting constant hazard SIT?")
    print("-" * 86)
    repro = max(abs(alpha_eff_annual(1.0 / L) - v)
                for L, v in ALPHA_EFF_PUBLISHED.items())
    print(f"  alpha_eff reproduces RESULT-REG-004 §5's published curve to {repro:.1e} "
          f"at all five lives")
    print(f"  (the AS-FITTED curve, which drops the T >= 1 conditioning, would sit "
          f"{max(abs(alpha_eff_annual(1.0/L, conditioned=False) - v) / v for L, v in ALPHA_EFF_PUBLISHED.items()):.1%} "
          f"high -- the erratum's third visit)")
    out["P_alpha_eff_repro"] = repro
    check("P · alpha_eff is the T >= 1 curve the manuscript prints, not the as-fitted one",
          repro < 1e-4,
          witness=lambda: max(abs(alpha_eff_annual(1.0 / L, conditioned=False) - v)
                              for L, v in ALPHA_EFF_PUBLISHED.items()) < 1e-4)
    print(f"  {'life':>6} {'alpha_ser/yr':>12} {'alpha_eff/yr':>12} {'as-fitted':>10} "
          f"{'alpha_hat/yr':>12} | {'ser vs hat':>11} {'ser vs eff':>11}")
    P_rows, p_dev_hat_min, p_dev_eff_min = [], 1e9, 1e9
    for life in LIVES_YEARS:
        d_a = 1.0 / life
        rows = [r for r in I_rows if r["life"] == life]
        a_ser = float(np.mean([r["alpha_ser_a"] for r in rows]))
        a_ser_sd = float(np.std([r["alpha_ser_a"] for r in rows]))
        a_eff = alpha_eff_annual(d_a)
        dh = abs(a_ser - ALPHA_A_HAT) / ALPHA_A_HAT
        de = abs(a_ser - a_eff) / a_eff
        p_dev_hat_min = min(p_dev_hat_min, dh)
        p_dev_eff_min = min(p_dev_eff_min, de)
        P_rows.append({"life": life, "delta_a": d_a, "alpha_ser_a": a_ser,
                       "alpha_ser_sd": a_ser_sd, "alpha_eff_a": a_eff,
                       "dev_vs_hat": dh, "dev_vs_eff": de})
        print(f"  {life:>5.0f}y {a_ser:>12.4f} {a_eff:>12.4f} "
              f"{alpha_eff_annual(d_a, conditioned=False):>10.4f} {ALPHA_A_HAT:>12.4f} "
              f"| {dh:>10.2%} {de:>10.2%}")
    p_dev_hat_max = max(r["dev_vs_hat"] for r in P_rows)
    p_dev_eff_max = max(r["dev_vs_eff"] for r in P_rows)
    ladder_P = ("P1" if p_dev_hat_max <= 0.01 else "P2" if p_dev_eff_max <= 0.01 else "P3")
    out["P_rows"], out["ladder_P"] = P_rows, ladder_P
    out["P_dev_hat_max"], out["P_dev_eff_max"] = p_dev_hat_max, p_dev_eff_max
    print(f"\n  worst departure from alpha_hat {p_dev_hat_max:.2%}, from alpha_eff "
          f"{p_dev_eff_max:.2%}")
    print(f"  -> LADDER P = {ladder_P}   (predicted P3)")
    check("P · alpha_eff is a curve and not a constant, so 'ser vs eff' is per-delta",
          len({round(r["alpha_eff_a"], 6) for r in P_rows}) == len(P_rows),
          witness=lambda: len({round(ALPHA_A_HAT, 6) for _ in P_rows}) == len(P_rows))
    print()

    # ==================================================================================
    print("§5 · LADDER W · how wide is the k-interval a series cannot resolve?")
    print("-" * 86)
    d_ref, phi_ref = yr_to_q(0.10), 0.60          # a ten-year life, the middle tier
    ks = np.linspace(K_SWEEP[0], K_SWEEP[1], K_GRID_N)
    tgt = series_weibull(K_HAT, Q_HAT, d_ref, phi_ref, N_DEFAULT)
    prof = np.array([fit_weibull_free_k(tgt, N_DEFAULT, float(k))[0] for k in ks])
    out["W_profile_k"] = ks.tolist()
    out["W_profile_eps"] = prof.tolist()

    def interval_width(profile, grid, sigma):
        inside = grid[profile <= sigma]
        if inside.size == 0:
            return 0.0, None, None
        return float(inside.max() - inside.min()), float(inside.min()), float(inside.max())

    W_rows = []
    for s in SIGMA_GRID:
        w, lo, hi = interval_width(prof, ks, s)
        W_rows.append({"sigma": s, "width": w, "lo": lo, "hi": hi,
                       "ratio_to_reg003": w / K_CI_WIDTH})
        print(f"  sigma = {s:>7.0e} -> k in [{lo}, {hi}]  width {w:.4f}  "
              f"= {w / K_CI_WIDTH:>8.2f} x REG-003's 0.150")
    w_read = [r for r in W_rows if r["sigma"] == SIGMA_LADDER_W][0]
    W = w_read["ratio_to_reg003"]
    covers_all = (w_read["width"] >= (K_SWEEP[1] - K_SWEEP[0]) - 1e-9)
    ladder_W = ("W4" if (W >= 100 or covers_all) else "W3" if W >= 10
                else "W2" if W >= 1 else "W1")
    out["W_rows"], out["ladder_W"], out["W_ratio"] = W_rows, ladder_W, W
    print(f"\n  -> LADDER W = {ladder_W}   W = {W:.2f}   (predicted W4)")
    i_hat = int(np.argmin(np.abs(ks - K_HAT)))
    i_one = int(np.argmin(np.abs(ks - 1.0)))
    floor_ = float(prof[i_hat])
    out["W_search_floor"] = floor_
    out["W_sigma_star"] = float(prof[i_one])
    print(f"  the search's own floor, at k = {ks[i_hat]:.2f} (the truth): {floor_:.3e} "
          f"-- {min(SIGMA_GRID)/floor_:.0f}x below the finest sigma reported")
    print(f"  the profile at k = 1.00 (the constant hazard): {prof[i_one]:.3e} "
          f"= the precision a series must carry to reject a constant hazard at all")
    check("W · the search floor at k_hat is far below every sigma reported, so I(sigma) "
          "is non-empty at each and its WIDTH is the content, not its emptiness",
          floor_ <= min(SIGMA_GRID) / 10.0,
          witness=lambda: float(prof[i_one]) <= min(SIGMA_GRID) / 10.0)

    # Is the interval censored by the registered sweep?  REG-005 §3 Q1 fixed [0.6, 2.0].
    censored = [r["sigma"] for r in W_rows
                if r["lo"] is not None and (r["lo"] <= K_SWEEP[0] + 1e-9
                                            or r["hi"] >= K_SWEEP[1] - 1e-9)]
    out["W_censored_sigmas"] = censored
    if censored:
        print(f"  CENSORED at the registered sweep boundary for sigma in {censored}: "
              f"the reported width is a LOWER bound there.")
        # robustness only, REG-005 §7: reported, labelled, and may not change a verdict.
        ks_wide = np.arange(0.20, 3.001, 0.02)
        pw = np.array([fit_weibull_free_k(tgt, N_DEFAULT, float(k))[0] for k in ks_wide])
        ww, wlo, whi = interval_width(pw, ks_wide, SIGMA_LADDER_W)
        out["W_robustness_wide"] = {"lo": wlo, "hi": whi, "width": ww,
                                    "ratio_to_reg003": ww / K_CI_WIDTH}
        print(f"  ROBUSTNESS (unregistered, cannot change a verdict): on k in "
              f"[0.20, 3.00] the sigma = 1e-3 interval is [{wlo:.2f}, {whi:.2f}], "
              f"width {ww:.3f} = {ww/K_CI_WIDTH:.2f} x -- ladder W is unchanged.")

    # What is IN the interval matters more than how wide it is.  §4.9: a lag with k < 1
    # has a DECREASING hazard and no steady-state deferral measure at any positive delta.
    w1e3 = [r for r in W_rows if r["sigma"] == SIGMA_LADDER_W][0]
    sub_one = w1e3["lo"] is not None and w1e3["lo"] < 1.0
    out["W_contains_k_below_1"] = bool(sub_one)
    if sub_one:
        print(f"  I(1e-3) reaches k = {w1e3['lo']:.2f} < 1 — a DECREASING hazard, which "
              f"by §4.9 admits\n     no steady-state deferral measure at any positive "
              f"decay rate. A series good to one part\n     in a thousand cannot "
              f"separate the well-posed model from one with no steady state.")
    check("W · the sub-unit shapes inside I(1e-3) are genuinely fitted, not grid edge",
          (not sub_one) or float(fit_weibull_free_k(tgt, N_DEFAULT, 0.8)[0])
          <= SIGMA_LADDER_W,
          witness=lambda: float(fit_weibull_free_k(tgt, N_DEFAULT, 0.2)[0])
          <= SIGMA_LADDER_W)
    print()

    # ==================================================================================
    print("§5 · LADDER S · a sample-size problem, or an identification problem?")
    print("-" * 86)
    S_rows = []
    for n in N_LADDER_S:
        t_n = series_weibull(K_HAT, Q_HAT, d_ref, phi_ref, n)
        ks_s = ks[::2]   # 0.02, ample for a width read to two decimals
        pr = np.array([fit_weibull_free_k(t_n, n, float(k))[0] for k in ks_s])
        w, lo, hi = interval_width(pr, ks_s, SIGMA_LADDER_W)
        S_rows.append({"N": n, "width": w, "lo": lo, "hi": hi})
        print(f"  N = {n:>4} quarters -> k in [{lo}, {hi}]  width {w:.4f}")
    w20 = [r for r in S_rows if r["N"] == 20][0]["width"]
    w400 = [r for r in S_rows if r["N"] == 400][0]["width"]
    shrink = (w20 / w400) if w400 > 0 else float("inf")
    sqrt_rate = math.sqrt(400 / 20)                    # 4.47
    ladder_S = ("S3" if shrink < 2.0 else "S1" if shrink >= sqrt_rate else "S2")
    out["S_rows"], out["ladder_S"], out["S_shrink"] = S_rows, ladder_S, shrink
    best_n = min(S_rows, key=lambda r: r["width"])
    monotone = all(S_rows[i]["width"] >= S_rows[i + 1]["width"]
                   for i in range(len(S_rows) - 1))
    out["S_monotone"], out["S_best_N"] = monotone, best_n["N"]
    print(f"\n  width at N=20 / width at N=400 = {shrink:.3f}, against "
          f"sqrt(20) = {sqrt_rate:.3f} for the N^-1/2 rate")
    if not monotone:
        print(f"  NOT monotone in N. The narrowest interval is at N = {best_n['N']} "
              f"quarters ({best_n['width']:.3f}); a longer\n     window is WORSE. The "
              f"shape lives in the transient, and once the gap reaches its steady\n"
              f"     state every further quarter repeats one number, which an average "
              f"over t dilutes.")
    print(f"  -> LADDER S = {ladder_S}   (predicted S3)")
    check("S · the metric admits improvement with N (the norm-relative one would not)",
          w400 <= w20 + 1e-12,
          witness=lambda: w400 <= 0.0)
    print()

    # ==================================================================================
    print("§5 · LADDER N · what noise buries it?")
    print("-" * 86)
    rng = np.random.default_rng(DRAW_SEED)
    ndraws = 20 if args.quick else N_DRAWS
    N_rows = []
    for s in SIGMA_GRID_N:
        fits = []
        pile = 0
        for _ in range(ndraws):
            noisy = tgt * (1.0 + rng.normal(0.0, s, size=tgt.shape))
            noisy[0] = tgt[0]                      # books square is observed, not noisy
            kbest = float(fit_weibull_full(noisy, N_DEFAULT, FULL_STARTS)[1][0])
            if kbest <= K_SWEEP[0] + 1e-9 or kbest >= K_SWEEP[1] - 1e-9:
                pile += 1
            fits.append(kbest)
        fits = np.array(fits)
        iqr = float(np.percentile(fits, 75) - np.percentile(fits, 25))
        N_rows.append({"sigma": s, "iqr": iqr, "median": float(np.median(fits)),
                       "pile_up_fraction": pile / ndraws, "draws": ndraws})
        print(f"  sigma = {s:>7.0e} -> median k_hat {np.median(fits):.3f}  "
              f"IQR {iqr:.4f}  boundary pile-up {pile/ndraws:.1%}")
    n_read = [r for r in N_rows if r["sigma"] == SIGMA_LADDER_W][0]
    ladder_N = ("N3" if (n_read["iqr"] >= 1.5 or n_read["pile_up_fraction"] >= 0.5)
                else "N1" if n_read["iqr"] < K_CI_WIDTH else "N2")
    out["N_rows"], out["ladder_N"] = N_rows, ladder_N
    print(f"\n  -> LADDER N = {ladder_N}   (read at sigma = 1e-3)")
    print()

    # ==================================================================================
    print("§2 · F3 · THE WITNESS — a world the geometric must NOT be able to fit")
    print("-" * 86)
    wit = series_weibull(K_WITNESS, Q_HAT, d_ref, phi_ref, N_DEFAULT)
    rw = fit_mimic(wit, N_DEFAULT, admissible=True)
    # The comparison is AT MATCHED (delta, phi).  Against ladder I's worst cell -- a
    # different life and a different phi -- the ratio is 1.3x and means nothing; the
    # witness has to be judged against the same world it is standing in for.
    matched = [r for r in I_rows
               if r["life"] == 10.0 and abs(r["phi"] - phi_ref) < 1e-9][0]["eps_admissible"]
    print(f"  k = {K_WITNESS} (decreasing hazard, no steady state at any positive delta "
          f"per §4.9)")
    print(f"  best admissible constant-hazard mimic: eps = {rw['eps']:.3e}")
    print(f"  at the SAME life and phi, the measured shape gives {matched:.3e} "
          f"-- a separation of {rw['eps'] / matched:.1f} x")
    print(f"  (against ladder I's worst cell, {eps_max:.3e}, the ratio is "
          f"{rw['eps'] / eps_max:.1f}x -- a different life and a different phi, so that "
          f"comparison is reported and not read)")
    out["F3_eps"] = rw["eps"]
    out["F3_ratio_matched"] = rw["eps"] / matched
    out["F3_ratio_vs_worst_cell"] = rw["eps"] / eps_max
    check("F3 · the metric is not blind: a k = 0.5 world is NOT mimicked below I2",
          rw["eps"] >= 1e-3,
          witness=lambda: fit_mimic(
              series_geometric(ALPHA_Q_HAT, d_ref, phi_ref, N_DEFAULT),
              N_DEFAULT, admissible=True)["eps"] >= 1e-3)
    print()

    print("=" * 86)
    print(f"  LADDERS · I = {ladder_I} · P = {ladder_P} · W = {ladder_W} · "
          f"S = {ladder_S} · N = {ladder_N}")
    print("=" * 86)
    print()

    if args.json_out:
        pathlib.Path(args.json_out).write_text(json.dumps(out, indent=2))
    summary()
    return 0


if __name__ == "__main__":
    sys.exit(main())
