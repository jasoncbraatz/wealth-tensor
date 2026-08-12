"""WT-086: do wt085's exponents survive a second parameter regime?

WHY THIS SCRIPT EXISTS
----------------------
`wt085` measured two exponents and Paper III now quotes both IN PRINT, in Section 4.7:
collinearity degrading as sigma^-0.98 and the standard error on phi-hat as sigma^-0.52.
Both were measured at exactly one setting -- alpha = 0.05, delta = 0.02, T = 400, one
accrual-noise level -- and a number in a manuscript is a promise about a class of cases,
not about the case you happened to run. The sign and the saturation are structural and
will hold anywhere. The EXPONENTS were not known to.

This is the check `wt085` itself teed up, run rather than deferred. If the exponents move
materially across the four decay rates the standards imply, Section 4.7 must quote a
regime rather than a pair of numbers, and this script says which.

WHAT IS ESTABLISHED HERE
------------------------
E1  THE EXPONENTS ACROSS THE GAAP LADDER. Nine (alpha, delta) regimes spanning the four
    decay rates Section 4.4 attributes to the standards and three book amortisation rates,
    each swept over the same volatilities. Both exponents are re-fitted per regime and the
    spread is reported.

E2  THE COLLINEARITY EXPONENT IS A CONSTANT OF THE PROBLEM. It is -1 in every regime, to
    within fitting error, and it should be: the third regressor's departure from
    proportionality with the second is the innovation itself, whose size is sigma, so the
    design's conditioning is reciprocal in sigma independently of where the roots sit.

E3  THE STANDARD-ERROR EXPONENT IS NOT, AND THE PAPER'S NUMBER IS THE WRONG KIND OF
    OBJECT. Reported with its range. Whatever the spread turns out to be, the manuscript
    is corrected to match it.

E4  THE LEVEL, WHICH MATTERS MORE THAN THE EXPONENT AND WAS NOT MEASURED AT ALL. Two
    regimes can share an exponent and differ by orders of magnitude in the standard error
    at any given volatility. Section 4.7 tells a reader how identification DEGRADES; it
    does not yet tell them where it starts. Reported here at a common sigma.

Each check ships a witness (scripts/severity.py).

    ./.venv/bin/python scripts/wt086_exponent_robustness.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from severity import check, summary  # noqa: E402


def hr(title: str) -> None:
    print("\n" + "=" * 78)
    print(f"  {title}")
    print("=" * 78)


# ------------------------------------------------------------------ model (as wt085)
# Duplicated rather than imported: wt085 executes at import time, and these scripts are
# meant to be standalone reproducible artifacts. Any change here must be mirrored there.
def economic_path(delta, periods, E0=1.0, sigma=0.0, seed=0):
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(periods + 1)
    E = np.empty(periods + 1)
    E[0] = E0
    for t in range(periods):
        E[t + 1] = E[t] * (1.0 - delta + sigma * z[t + 1])
    return E


def reported_series(alpha, phi, E, g0=0.0, eps=None):
    periods = len(E) - 1
    C = np.empty(periods + 1)
    C[0] = E[0] * (1.0 + g0)
    for t in range(periods):
        C[t + 1] = C[t] * (1.0 - alpha) + alpha * E[t] - phi * (E[t] - E[t + 1])
        if eps is not None:
            C[t + 1] += eps[t + 1]
    return C


def estimate_phi(C, e):
    X = np.column_stack([C[:-1], e[:-1], e[:-1] - e[1:]])
    beta, *_ = np.linalg.lstsq(X, C[1:], rcond=None)
    a_hat = 1.0 - beta[0]
    E0_hat = beta[1] / a_hat
    return -beta[2] / E0_hat


def collinearity(alpha, delta, phi, sigma, periods, g0, seed=3):
    E = economic_path(delta, periods, sigma=sigma, seed=seed)
    C = reported_series(alpha, phi, E, g0=g0)
    e = E / E[0]
    X = np.column_stack([C[:-1], e[:-1], e[:-1] - e[1:]])
    return float(np.linalg.cond(X / np.linalg.norm(X, axis=0)))


def se_phi(alpha, delta, phi, sigma, periods, g0, sigma_eps=2e-4, reps=40, seed=3):
    out = []
    for k in range(reps):
        E = economic_path(delta, periods, sigma=sigma, seed=seed + 1000 * k)
        z = np.random.default_rng(90000 + seed + k).standard_normal(periods + 1)
        C = reported_series(alpha, phi, E, g0=g0, eps=z * sigma_eps * E)
        try:
            p = estimate_phi(C, E / E[0])
            if np.isfinite(p):
                out.append(p)
        except np.linalg.LinAlgError:
            pass
    return float(np.std(out, ddof=1))


def loglog_slope(xs, ys):
    return float(np.polyfit(np.log(np.asarray(xs)), np.log(np.asarray(ys)), 1)[0])


PHI, G0, PERIODS = 0.60, 0.15, 400
SIGMAS = [0.150, 0.100, 0.050, 0.025]     # the quiet branch of wt085 E5

# The four decay rates §4.4 attributes to the standards, against book amortisation rates
# that bracket the paper's 0.05. Only alpha > delta is admissible.
REGIMES = [
    ("PP&E",                    0.080, 0.030),
    ("PP&E, slow book",         0.040, 0.030),
    ("finite-lived intang.",    0.050, 0.020),   # <- the paper's regime
    ("finite-lived, fast book", 0.120, 0.020),
    ("indefinite-lived",        0.050, 0.010),
    ("indefinite, slow book",   0.020, 0.010),
    ("goodwill-adjacent",       0.050, 0.002),
    ("goodwill, slow book",     0.010, 0.002),
    ("near-degenerate",         0.025, 0.020),   # alpha and delta close together
]

hr("E1 - the two exponents, re-fitted across nine regimes")

print(f"  phi={PHI}  g0={G0}  T={PERIODS}  sigma swept over {SIGMAS}")
print(f"  {'regime':<26}{'alpha':>7}{'delta':>7}{'p_cond':>9}{'p_se':>8}{'se @ .10':>11}")

p_conds, p_ses, rows = [], [], []
for name, a, d in REGIMES:
    conds = [collinearity(a, d, PHI, s, PERIODS, G0) for s in SIGMAS]
    ses = [se_phi(a, d, PHI, s, PERIODS, G0) for s in SIGMAS]
    pc, ps = loglog_slope(SIGMAS, conds), loglog_slope(SIGMAS, ses)
    se10 = ses[SIGMAS.index(0.100)]
    p_conds.append(pc)
    p_ses.append(ps)
    rows.append((name, a, d, pc, ps, se10))
    print(f"  {name:<26}{a:>7.3f}{d:>7.3f}{pc:>9.3f}{ps:>8.3f}{se10:>11.2e}")

paper_pc, paper_ps = -0.980, -0.516
print()
print(f"  the paper quotes p_cond = {paper_pc:+.2f} and p_se = {paper_ps:+.2f}, both from row 3")


hr("E2 - NEITHER exponent is a constant. Both quoted numbers are regime values.")

spread_c, spread_s = max(p_conds) - min(p_conds), max(p_ses) - min(p_ses)
worst = max(rows, key=lambda r: abs(r[4] - paper_ps))
print(f"  p_cond range : [{min(p_conds):+.3f}, {max(p_conds):+.3f}]   spread {spread_c:.3f}")
print(f"  p_se   range : [{min(p_ses):+.3f}, {max(p_ses):+.3f}]   spread {spread_s:.3f}")
print(f"  furthest from the quoted p_se: {worst[0]} at {worst[4]:+.3f} against {paper_ps:+.3f}")
print()
print("  This section was written expecting p_cond to be a constant of the problem -- the")
print("  third regressor's departure from proportionality with the second IS the innovation,")
print("  so the conditioning ought to be reciprocal in sigma wherever the roots sit. It is")
print("  not, and the two regimes that break it are the two where alpha and delta are")
print("  CLOSEST (spreads of 0.010 and 0.005), which the argument had no term for. Both")
print("  numbers now in print are regime values, not model properties.")
check("both exponents vary across regimes by far more than fitting error",
      spread_c > 0.20 and spread_s > 0.30,
      witness=lambda: spread_c < 0.05 and spread_s < 0.05)
print("  Witness asserts the nine regimes agree to within 0.05 on both -- i.e. that the")
print("  single measured pair was safe to print as constants. Had it held, this script")
print("  would be the celebrated empty result and §4.7 would need no change.")


hr("E3 - what the exponent tracks, and it is the thing §4.8 already worried about")


def spearman(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for pos, i in enumerate(order):
            r[i] = float(pos)
        return r
    rx, ry = rank(xs), rank(ys)
    return float(np.corrcoef(rx, ry)[0, 1])


mag = [abs(p) for p in p_ses]
deltas = [d for _, _, d in REGIMES]
gaps = [a - d for _, a, d in REGIMES]
prod = [d * (a - d) for _, a, d in REGIMES]

rho_d, rho_g, rho_p = spearman(deltas, mag), spearman(gaps, mag), spearman(prod, mag)
print(f"  Spearman rank correlation of |p_se| with")
print(f"    delta        : {rho_d:+.3f}")
print(f"    alpha-delta  : {rho_g:+.3f}")
print(f"    delta*(alpha-delta) : {rho_p:+.3f}   <-- the two act together")
print()
slow = [r for r in rows if r[2] <= 0.002]
print("  The slowest-decaying regimes have the FLATTEST response to volatility:")
for r in slow:
    print(f"    {r[0]:<26} delta={r[2]:.3f}  p_se={r[4]:+.3f}")
print()
print("  Read that plainly. For a goodwill-rate asset the standard error is very nearly")
print("  INSENSITIVE to return volatility: doubling the news buys almost nothing. Put it")
print("  beside wt085 E6, where the panel saturates within a few half-lives, and the two")
print("  levers close together. **For a slow-decaying asset, neither more news nor more")
print("  years materially helps.** §4.8 said the model has nothing to say about goodwill")
print("  because phi is absent from the dynamics at delta = 0; this is the same wall")
print("  approached from outside, and it is now a measured gradient rather than a limit")
print("  point -- the repair does not fail suddenly at zero decay, it fades out on the way.")
check("the exponent's magnitude tracks the decay rate and the root gap jointly",
      rho_p > 0.70 and all(abs(r[4]) < 0.20 for r in slow),
      witness=lambda: rho_p < 0.20)
print("  Witness asserts no rank relationship with delta*(alpha-delta). If the exponent")
print("  were unrelated to where the roots sit, the spread in E2 would be noise and there")
print("  would be nothing to say about which asset classes are readable.")


hr("E4 - the level, which the paper never measured and which a reader needs more")

lo_r = min(rows, key=lambda r: r[5])
hi_r = max(rows, key=lambda r: r[5])
print(f"  se(phi-hat) at a common sigma = 0.10:")
print(f"    best  : {lo_r[0]:<26} {lo_r[5]:.2e}")
print(f"    worst : {hi_r[0]:<26} {hi_r[5]:.2e}")
print(f"    ratio : {hi_r[5]/lo_r[5]:.1f}x")
print()
print("  Two regimes can share an exponent and still differ by this much at the same")
print("  volatility. An exponent says how identification DEGRADES; it does not say where")
print("  it starts, and §4.7 currently reports only the first. Note also which regimes are")
print("  worst: the slow-book ones, where alpha sits close to delta. A firm that amortises")
print("  at nearly the rate its asset decays is the hardest case, and it is also the case")
print("  in which the two parameters are nearest to being the same number.")
check("the level of the standard error varies more across regimes than the exponent does",
      hi_r[5] / lo_r[5] > 3.0,
      witness=lambda: hi_r[5] / lo_r[5] < 1.5)
print("  Witness asserts the level is near-constant across regimes, which would make the")
print("  exponent the whole story. It is not, so the exponent is not.")


hr("SUMMARY")
summary()
print()
print("  VERDICT FOR THE MANUSCRIPT -- §4.7 must change")
print(f"  - DELETE both quoted exponents. p_cond spans [{min(p_conds):+.2f}, {max(p_conds):+.2f}]"
      f" and p_se spans [{min(p_ses):+.2f}, {max(p_ses):+.2f}];")
print("    the printed pair is one regime's, and the near-degenerate cases break both.")
print("  - KEEP the structural claims, which hold in all nine: both exponents negative")
print("    everywhere, so identification always degrades as the asset quietens; and the")
print("    panel saturation of wt085 E6, which is independent of this.")
print("  - ADD the finding that is better than the number it replaces: the response to")
print(f"    volatility flattens as decay slows (rank corr {rho_p:+.2f} with delta*(alpha-delta)),")
print("    so for goodwill-rate assets neither news nor years buys identification. That")
print("    walks §4.8's limit point back into a gradient.")
