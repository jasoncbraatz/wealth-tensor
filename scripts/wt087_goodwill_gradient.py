"""WT-087: Section 4.8's goodwill limit is a property of the noiseless model.

WHY THIS SCRIPT EXISTS
----------------------
Section 4.8 argues the goodwill limit from a limit POINT: at delta = 0 the physical layer
does not move, the term phi*dE vanishes identically, the gap is zero at every phi, and phi
is not ill-conditioned but ABSENT from the dynamics. `wt086` then found that the approach
to that limit is a smooth gradient, and the section was to be rewritten around the
gradient -- a limit point at delta = 0 invites the reply "no real asset has delta exactly
zero," and a gradient forecloses it.

The rewrite needed the gradient's shape. Measuring it refuted the premise instead.

WHAT IS ESTABLISHED HERE
------------------------
E1  THE LIMIT POINT IS EXACT, AND MUCH NARROWER THAN THE SECTION CLAIMS. At delta = 0 with
    a motionless asset, the gap is exactly 0.0 -- not small, zero -- at every phi in [0,1].
    The existing claim is re-verified, not replaced.

E2  IT DOES NOT SURVIVE NEWS, AND THAT IS THE SECTION'S REAL PROBLEM. Set delta = 0 and let
    the asset's value MOVE: phi is recovered exactly from the reported series and returns.
    The limit is a property of a motionless asset, not of a slowly-decaying one. An asset
    whose value never changes is not goodwill; impairment testing exists precisely because
    goodwill's value does change.

E3  THE DRIVER IS THE ROOT GAP, NOT THE DECAY RATE. Every sweep so far, `wt086`'s included,
    moved the two together. Held apart: at a fixed gap, sweeping the decay rate 15x barely
    moves the standard error -- and what movement there is favours SLOW decay, because a
    slow asset stays alive to be observed. Sweeping the gap at a fixed decay rate moves it
    a great deal.

E4  WHICH MAKES A SENTENCE COMMITTED EARLIER TODAY WRONG, AND §4.4's LADDER SHAKY. §4.7
    says the worst corner is "small sigma and small delta." The sigma half holds; the delta
    half is refuted here. Worse, §4.4 assigns goodwill delta = 0.002 and §4.8 assigns it
    delta = 0, both inferred from the standards declining to amortise it -- reading a
    PHYSICAL decay rate off a REPORTING rule, which is the move §4.2 proves unavailable.

E5  THE REPLACEMENT CLAIM, WHICH IS CHECKABLE BY A READER. The unreadable case is the firm
    whose book amortisation rate sits close to its asset's true rate of decline, whatever
    the asset class -- two numbers being told apart that are nearly the same number.

    ./.venv/bin/python scripts/wt087_goodwill_gradient.py
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


# ------------------------------------------------------------------ model (as wt085/86)
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
    return -beta[2] / (beta[1] / a_hat)


def se_phi(alpha, delta, phi, sigma, periods, sigma_eps, g0=0.0, reps=40, seed=5):
    out = []
    for k in range(reps):
        E = economic_path(delta, periods, sigma=sigma, seed=seed + 1000 * k)
        z = np.random.default_rng(70000 + seed + k).standard_normal(periods + 1)
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


ALPHA, PHI, T, SIGMA = 0.080, 0.60, 400, 0.150
SIG_EPS = 0.010          # accrual noise at 1% of the asset's carrying value per period


hr("E1 - the limit point is exact, and Section 4.8's existing claim survives intact")

# NOTE: the first pass initialised the running maximum's phi to None and crashed
# formatting it, because `g > worst_gap` never fired -- every gap was EXACTLY 0.0, not
# merely small. The crash was the result.
gaps_by_phi = []
for phi in np.linspace(0.0, 1.0, 11):
    E = economic_path(0.0, T, sigma=0.0)            # delta = 0, and the asset does not move
    C = reported_series(ALPHA, phi, E, g0=0.0)
    gaps_by_phi.append((float(np.max(np.abs(C - E))), float(phi)))
worst_gap, worst_phi = max(gaps_by_phi)
exact_zeros = sum(1 for g, _ in gaps_by_phi if g == 0.0)

print(f"  delta = 0, sigma = 0, phi swept over 11 values in [0,1], {T} periods")
print(f"  worst |C(t) - E(t)| over every phi and every t = {worst_gap:.3e}")
print(f"  values of phi giving a gap of EXACTLY 0.0, not merely small: {exact_zeros} of 11")
print("  phi is not ill-conditioned here; it is absent from the dynamics. That is the")
print("  section's current argument and it is correct. Note what the run required, though:")
print("  BOTH delta = 0 and sigma = 0. E2 asks which of the two was doing the work.")
check("with a motionless asset the gap vanishes identically for every phi in [0,1]",
      worst_gap == 0.0 and exact_zeros == 11,
      witness=lambda: float(np.max(np.abs(
          reported_series(ALPHA, 0.6, economic_path(0.002, T, sigma=0.0))
          - economic_path(0.002, T, sigma=0.0)))) == 0.0)
print("  Witness runs the same test at goodwill's delta = 0.002 rather than at zero. If a")
print("  gap that small also counted as vanishing, the check could not tell the limit from")
print("  its neighbourhood, which is the whole subject of this script.")


hr("E2 - THE LIMIT DOES NOT SURVIVE NEWS, AND THIS IS THE SECTION'S REAL PROBLEM")

# This section was written to measure how fast identification fails as delta -> 0. It does
# not fail. The first sweep returned a standard error that IMPROVED as decay slowed --
# the opposite of the premise -- and chasing that inversion found the error below.
E_dn = economic_path(0.0, T, sigma=SIGMA, seed=17)       # delta = 0, but the asset MOVES
C_dn = reported_series(ALPHA, PHI, E_dn, g0=0.0)
gap_dn = float(np.max(np.abs(C_dn - E_dn)))
phi_dn = estimate_phi(C_dn, E_dn / E_dn[0])

print(f"  delta = 0 exactly, and now the asset's value moves: sigma = {SIGMA}")
print(f"  worst |C(t) - E(t)|              = {gap_dn:.4f}      (E1's was exactly 0.0)")
print(f"  phi recovered from (C, returns)  = {phi_dn:.10f}")
print(f"  recovery error against phi = {PHI}  = {abs(phi_dn - PHI):.2e}")
print()
print("  At zero decay WITH news, phi is recovered exactly. The limit belongs to the")
print("  motionless asset, not to the slow one. Section 4.8's reasoning -- 'the physical")
print("  layer does not move, so phi has nothing to act on' -- holds only if the physical")
print("  layer never moves for ANY reason, scheduled or not. An asset whose value never")
print("  changes is not goodwill. It is not any asset anyone impairs.")
check("at zero decay with news, phi is exactly identified and the gap is not zero",
      abs(phi_dn - PHI) < 1e-8 and gap_dn > 0.01,
      witness=lambda: gap_dn < 1e-12)
print("  Witness asserts the gap still vanishes once news is switched on -- i.e. that E1's")
print("  result is about delta rather than about the absence of variation. It is not.")


hr("E3 - so what DOES drive it? Hold the decay rate and the root gap apart.")

# Every sweep so far, wt086's included, moved the two together: changing delta at a fixed
# alpha changes the root gap by the same amount. Hold each fixed in turn.
GAP_FIXED, DELTA_FIXED = 0.030, 0.010
same_gap = [(round(d + GAP_FIXED, 4), d) for d in (0.002, 0.005, 0.010, 0.020, 0.030)]
same_delta = [(round(DELTA_FIXED + g, 4), DELTA_FIXED) for g in (0.005, 0.010, 0.020, 0.040, 0.080)]

print(f"  (a) root gap HELD at alpha - delta = {GAP_FIXED}; decay rate swept 15x:")
print(f"  {'alpha':>8}{'delta':>8}{'se(phi-hat)':>14}")
ses_a = []
for a, d in same_gap:
    s = se_phi(a, d, PHI, SIGMA, T, SIG_EPS)
    ses_a.append(s)
    print(f"  {a:>8.3f}{d:>8.3f}{s:>14.4f}")
p_d = loglog_slope([d for _, d in same_gap], ses_a)
spread_a = max(ses_a) / min(ses_a)
print(f"      fitted: se ~ delta^{p_d:+.3f}     spread {spread_a:.2f}x")

print()
print(f"  (b) decay rate HELD at delta = {DELTA_FIXED}; root gap swept 16x:")
print(f"  {'alpha':>8}{'delta':>8}{'gap':>8}{'se(phi-hat)':>14}")
ses_b = []
for a, d in same_delta:
    s = se_phi(a, d, PHI, SIGMA, T, SIG_EPS)
    ses_b.append(s)
    print(f"  {a:>8.3f}{d:>8.3f}{a-d:>8.3f}{s:>14.4f}")
p_g = loglog_slope([a - d for a, d in same_delta], ses_b)
spread_b = max(ses_b) / min(ses_b)
print(f"      fitted: se ~ (alpha-delta)^{p_g:+.3f}     spread {spread_b:.2f}x")

print()
print("  The ROOT GAP drives it; the decay rate at a fixed gap barely does, and what little")
print("  it does favours SLOW decay -- a slow asset stays alive to be observed. This is the")
print("  ordinary shape of a near-degenerate identification problem, not anything peculiar")
print("  to long-lived assets.")
check("the root gap governs the standard error and the decay rate at a fixed gap does not",
      spread_b > 1.8 * spread_a,
      witness=lambda: spread_a > spread_b)
print("  Witness asserts the decay rate dominates -- the reading under which §4.7's 'small")
print("  sigma and small delta' would have been right.")


hr("E4 - which makes a sentence committed earlier today wrong, and §4.4's ladder shaky")

gw_a, gw_d = 0.050, 0.002
se_gw = se_phi(gw_a, gw_d, PHI, SIGMA, T, SIG_EPS)
se_ppe = se_phi(0.080, 0.030, PHI, SIGMA, T, SIG_EPS)

print("  §4.7 as committed this morning says goodwill, brands and long-lived plant sit in")
print("  'the corner in which every term above is worst -- small sigma and small delta.'")
print(f"  The sigma half is right. The delta half is refuted: at a fixed root gap, slow")
print(f"  decay is mildly HELPFUL (se ~ delta^{p_d:+.2f}). The correct statement names small")
print("  sigma and a small ROOT GAP.")
print()
print(f"  goodwill rate (alpha={gw_a}, delta={gw_d}, gap {gw_a-gw_d:.3f}) : se = {se_gw:.4f}")
print(f"  PP&E rate     (alpha=0.080, delta=0.030, gap 0.050) : se = {se_ppe:.4f}")
print("  On the model's own arithmetic the goodwill rate is not the unreadable one. It is")
print("  not even the worse of these two.")
print()
print("  The deeper problem is upstream and this script cannot repair it. §4.4 assigns")
print("  goodwill delta = 0.002 and §4.8 assigns it delta = 0, both on the ground that the")
print("  standards decline to put it on an amortisation schedule. But delta is the PHYSICAL")
print("  decay rate and a schedule is a REPORTING rule. Inferring the first from the second")
print("  is the move §4.2 proves unavailable -- and impairment testing exists precisely")
print("  because goodwill's economic value does decline. The paper reads its ladder off the")
print("  reporting layer in the middle of proving that the reporting layer does not")
print("  determine it.")
check("at a realistic root gap the goodwill rate is no harder to read than the PP&E rate",
      se_gw < 1.5 * se_ppe,
      witness=lambda: se_gw > 3.0 * se_ppe)
print("  Witness asserts goodwill is several times harder, which is what §4.8 currently")
print("  implies and what this script was written expecting to confirm.")


hr("E5 - the corner that IS worst, stated so a reader can locate their own case")

print(f"  se(phi-hat) at accrual noise {SIG_EPS:.0%}, sigma = {SIGMA}, T = {T}, delta = 0.010:")
print(f"  {'alpha':>8}{'gap':>8}{'se(phi-hat)':>14}{'phi readable to':>18}")
worst_se = 0.0
for a, d in [(0.012, 0.010), (0.015, 0.010), (0.020, 0.010),
             (0.030, 0.010), (0.050, 0.010), (0.090, 0.010)]:
    s = se_phi(a, d, PHI, SIGMA, T, SIG_EPS)
    worst_se = max(worst_se, s)
    print(f"  {a:>8.3f}{a-d:>8.3f}{s:>14.4f}{'+/- ' + format(2*s, '.3f'):>18}")
print()
print("  A firm whose book amortisation rate sits within a fifth of a percentage point of")
print("  its asset's true rate of decline is the hard case, and it is hard for the plainest")
print("  reason in econometrics: the two numbers being told apart are nearly the same")
print("  number. That is the claim §4.8 should be making. It has two virtues the goodwill")
print("  version lacks -- it is checkable by a reader against a disclosed useful life,")
print("  which §4.7 already argues the standards publish, and it does not require inferring")
print("  a physical rate from a reporting rule.")
check("the standard error blows up as the two rates approach each other",
      worst_se > 3.0 * se_ppe,
      witness=lambda: worst_se < 1.2 * se_ppe)
print("  Witness asserts the near-degenerate corner is no worse than the ordinary case. If")
print("  that held there would be no hard corner at all and §4.8 could simply be deleted.")


hr("E6 - reconciling this with wt086, which appeared to say the opposite")

# wt086 found the sigma-exponent tracking delta*(alpha-delta); E3 here finds the LEVEL
# barely moving with delta at a fixed gap. Left side by side those read as a
# contradiction and a referee would say so. They are statements about different things,
# and this check separates them: fit the sigma-exponent at a FIXED gap, across delta.
SIGS = [0.150, 0.100, 0.050, 0.025]
print(f"  root gap held at {GAP_FIXED}; for each delta, the sigma-exponent re-fitted:")
print(f"  {'alpha':>8}{'delta':>8}{'p_sigma':>10}{'se @ sigma=0.15':>18}{'se @ sigma=0.025':>19}")
p_sigmas, lvl_hi, lvl_lo = [], [], []
for a, d in same_gap:
    row = [se_phi(a, d, PHI, s, T, SIG_EPS) for s in SIGS]
    ps = loglog_slope(SIGS, row)
    p_sigmas.append(ps)
    lvl_hi.append(row[0])
    lvl_lo.append(row[-1])
    print(f"  {a:>8.3f}{d:>8.3f}{ps:>10.3f}{row[0]:>18.4f}{row[-1]:>19.4f}")

exp_spread = max(p_sigmas) - min(p_sigmas)
lvl_spread_hi = max(lvl_hi) / min(lvl_hi)
lvl_spread_lo = max(lvl_lo) / min(lvl_lo)
print()
print(f"  sigma-exponent spread across delta, at a FIXED gap : {exp_spread:.3f}")
print(f"  level spread at sigma = 0.150                      : {lvl_spread_hi:.2f}x")
print(f"  level spread at sigma = 0.025                      : {lvl_spread_lo:.2f}x")
print()
print("  Both readings are right, and they are about different quantities. The DECAY RATE")
print("  governs how strongly the standard error RESPONDS to volatility -- that is wt086's")
print("  finding, and it holds at a fixed gap. The RATE GAP governs the standard error's")
print("  LEVEL -- that is E3's. The curves nearly coincide at the volatility E3 happened to")
print("  sweep at and separate away from it, which is why E3 alone reads as 'delta barely")
print("  matters' and wt086 alone reads as 'delta is decisive.' Neither sentence is safe")
print("  without the other, and the paper must carry both.")
check("delta governs the response to volatility while the gap governs the level",
      exp_spread > 0.20 and lvl_spread_lo > 1.5 * lvl_spread_hi,
      witness=lambda: exp_spread < 0.05)
print("  Witness asserts the sigma-exponent is flat across delta at a fixed gap, which")
print("  would mean wt086's result was purely the gap in disguise and one sentence would")
print("  do. It is not flat, so both sentences are load-bearing.")


hr("SUMMARY")
summary()
print()
print("  FOR SECTION 4.8 -- a rewrite, and a demotion")
print("  - KEEP E1, narrowed: with a MOTIONLESS asset, phi is absent from the dynamics.")
print("    True and exact, and far narrower than the section currently claims.")
print("  - E2 is the correction: that limit belongs to the noiseless model. Give the asset")
print("    news and phi is recovered exactly at delta = 0.")
print(f"  - E3/E4: the driver is the root gap (spread {spread_b:.1f}x) not the decay rate")
print(f"    (spread {spread_a:.1f}x). §4.7's 'small delta is the worst corner' must be corrected,")
print("    and §4.4's ladder infers a physical rate from a reporting rule.")
print("  - E5 is the replacement claim, and it is checkable by a reader.")
