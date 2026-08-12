"""WT-088: section 4.4 rebuilt on the observable pair. Registered as REG-002.

WHY THIS SCRIPT EXISTS
----------------------
WT-083 established that the model's deferral measure R = (1-phi)*delta/(alpha-delta) runs
BACKWARDS across the four GAAP classes -- Kendall tau = -1 against the ordering PRE-001
registered -- and that over 4,000 random ladders the registered ordering is recovered in
1.9% of worlds, reversed in 23.8%, non-monotone in 74.2%.

Both figures are computed under TWO constraints imposed jointly:

    (1) observability falls up the ladder     <- the design. Not in question.
    (2) durability RISES up the ladder        <- inferred from the standards' SCHEDULING
                                                 behaviour.

WT-087 and section 4.4's own closing paragraph established that (2) is an inference from a
reporting rule, and that scheduling tracks how PREDICTABLE a decline is rather than how
FAST it is. Goodwill is unscheduled because it is LUMPY, not because it is SLOW. The paper
forbids inferring delta from a reported series and then infers a delta ladder from a
reporting rule. Naming that as an assumption -- which section 4.4 now does -- is an honest
disclosure and is NOT a repair.

Every falsifier below was written into docs/preregistration/REG-002-*.md and pushed BEFORE
this file existed (WT-052). No check's pass condition encodes its own expected answer
(WT-080, and the rule -13 paid for five times: FIT THE EXPONENT, DO NOT ASSERT IT).

WHAT IS ESTABLISHED HERE
------------------------
E1  Drop constraint (2). Redraw with delta i.i.d. and unordered.
E2  Solve for the goodwill decay rate at which the strict reversal breaks.
E3  Lumpy, not slow: drive a class with a compound-Poisson decline at the SAME mean rate.
E4  The disclosed-numbers ladder: sweep the (delta_0, delta_1) rectangle disclosure spans.
E5  What governs the direction -- a FITTED logistic, with a crossover ratio.
E6  The alpha-delta boundary, which the disclosed numbers walk into.
E7  Does the LAG survival (section 4.5) survive dropping (2) as well?

Each check ships a witness (scripts/severity.py).

    ./.venv/bin/python scripts/wt088_disclosed_ladder.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from wealth_tensor.lag import LayeredFirm, recognition_lag  # noqa: E402
from severity import check, summary  # noqa: E402

PERIODS = 400
E0 = 100.0
ALPHA = 0.05
THETA = 0.25
SEED = 20260812

TIERS = ["0 PP&E", "1 finite-lived intangible",
         "2 indefinite-lived intangible", "3 goodwill"]

# WT-083's ladder, unchanged, so every number here is comparable to the paper's table.
PHI = np.array([0.80, 0.60, 0.40, 0.20])
DELTA = np.array([0.030, 0.020, 0.010, 0.002])

DELTA_LO, DELTA_HI = 0.001, 0.040          # WT-083's support, reused verbatim
PHI_LO, PHI_HI = 0.05, 0.95

N = 4000       # WT-083's sample size for the magnitude draw
M = 400        # WT-083's sample size for the lag draw (lag needs a simulation each)


def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


def firm(phi, delta, alpha=ALPHA, theta=THETA):
    return LayeredFirm(initial_wealth=E0, entropy_rate=delta, maintenance_ratio=0.0,
                       observable_share=phi, recognition_rate=alpha,
                       crisis_threshold=theta)


def closed_form(phi, delta, alpha=ALPHA):
    return (1.0 - phi) * delta / (alpha - delta)


def kendall_tau(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    n = len(a)
    num = 0
    for i in range(n):
        for j in range(i + 1, n):
            num += np.sign(a[j] - a[i]) * np.sign(b[j] - b[i])
    return float(num / (n * (n - 1) / 2))


def strictly_increasing(x):
    return all(x[i] < x[i + 1] for i in range(len(x) - 1))


def strictly_decreasing(x):
    return all(x[i] > x[i + 1] for i in range(len(x) - 1))


def half_life(delta):
    """Periods for the asset to lose half its value at a constant rate."""
    return float(np.log(0.5) / np.log(1.0 - delta))


# ================================================================== E1
hr("E1 - drop the durability ordering entirely (REG-002 E1)")

print("  WT-083 drew delta SORTED DESCENDING: durability rises up the ladder, the")
print("  inference from the standards' scheduling behaviour. Here delta is drawn i.i.d.")
print("  and UNORDERED over the same support. phi still falls up the ladder -- that is")
print("  the design and it is not in question.\n")


def draw_magnitude(n, seed, order_delta):
    rng = np.random.default_rng(seed)
    agree = reverse = neither = 0
    taus = np.empty(n)
    for k in range(n):
        phi = np.sort(rng.uniform(PHI_LO, PHI_HI, 4))[::-1]
        d = rng.uniform(DELTA_LO, DELTA_HI, 4)
        if order_delta:
            d = np.sort(d)[::-1]
        R = (1 - phi) * d / (ALPHA - d)
        taus[k] = kendall_tau(-phi, R)
        if strictly_increasing(R):
            agree += 1
        elif strictly_decreasing(R):
            reverse += 1
        else:
            neither += 1
    return agree / n, reverse / n, neither / n, taus


def _common_delta_recovery(seed):
    """delta held COMMON across tiers: the design MUST recover its ordering always."""
    rng = np.random.default_rng(seed)
    hits = 0
    for _ in range(N):
        phi = np.sort(rng.uniform(PHI_LO, PHI_HI, 4))[::-1]
        d = rng.uniform(DELTA_LO, DELTA_HI)
        R = (1 - phi) * d / (ALPHA - d)
        if strictly_increasing(R):
            hits += 1
    return hits / n if (n := N) else 0.0


a_ord, r_ord, n_ord, tau_ord = draw_magnitude(N, SEED, order_delta=True)
a_un, r_un, n_un, tau_un = draw_magnitude(N, SEED, order_delta=False)

print(f"  {'':<34}{'ORDERED (WT-083)':>20}{'UNORDERED':>16}")
print(f"  {'recovers the registered ordering':<34}{100*a_ord:>19.1f}%{100*a_un:>15.1f}%")
print(f"  {'exactly reverses it':<34}{100*r_ord:>19.1f}%{100*r_un:>15.1f}%")
print(f"  {'non-monotone':<34}{100*n_ord:>19.1f}%{100*n_un:>15.1f}%")
print(f"  {'mean Kendall tau':<34}{tau_ord.mean():>+20.3f}{tau_un.mean():>+16.3f}")
print(f"  {'   sd':<34}{tau_ord.std():>20.3f}{tau_un.std():>16.3f}")
se_un = tau_un.std() / np.sqrt(N)
print(f"  {'   se of the mean':<34}{tau_ord.std()/np.sqrt(N):>20.4f}{se_un:>16.4f}")

frac_neg_ord = float((tau_ord <= 0).mean())
frac_neg_un = float((tau_un <= 0).mean())
print(f"  {'share of ladders with tau <= 0':<34}{100*frac_neg_ord:>19.1f}%"
      f"{100*frac_neg_un:>15.1f}%")

# REGISTERED FALSIFIER (REG-002 E1) -- AND ITS OWN DEFECT, REPORTED RATHER THAN REPAIRED.
#
# REG-002 E1 was written as: "if mean tau in (-0.10, +0.10), the headline downgrades from
# INVERTS to DESTROYS." That threshold is stated on |mean tau|, and an absolute value
# CANNOT DISTINGUISH AN EFFECT THAT VANISHED FROM ONE THAT CHANGED SIGN. The measured
# unordered mean is +0.318 -- far outside the band, so the registered test as literally
# written returns "the inversion survives", which is the exact opposite of what the number
# says. The registration is defective, the number is unambiguous, and the defect is
# recorded in REG-002 as an erratum rather than quietly rewritten.
#
# The correct reading, on the signed quantity the falsifier should have named:
signed = tau_un.mean()
print(f"\n  REG-002 E1 falsifier was stated on |mean tau| and is DEFECTIVE -- see the")
print(f"  erratum in REG-002. An absolute value cannot tell a vanished effect from a")
print(f"  reversed one, and this is the case that separates them.")
print(f"  signed mean tau, unordered: {signed:+.3f}  (se {se_un:.4f}) -- POSITIVE.")
print(f"  -> the inversion is not weakened by dropping the durability ordering. It is")
print(f"     ABSENT. Without that ordering the design's own term is the only systematic")
print(f"     force left and the ranking runs, on average, the way it was designed to.")

check("dropping the durability ordering moves mean tau materially toward zero",
      abs(tau_un.mean()) < abs(tau_ord.mean()) - 10 * se_un,
      witness=lambda: abs(tau_ord.mean()) < abs(tau_ord.mean()) - 10 * se_un)
print("  Witness is the ordered draw asked the same question of itself, which cannot")
print("  be materially closer to zero than it is.")

check("the reversal RATE is a property of the assumed ordering, not of the confound alone",
      r_un < 0.5 * r_ord,
      witness=lambda: r_ord < 0.5 * r_ord)

# The half that does NOT depend on the ordering, and it is the load-bearing half.
# Stated against the common-delta world rather than against a chosen number, because a
# threshold picked after seeing 11.5% would be the finding grading its own homework.
common_rec = _common_delta_recovery(SEED)
print(f"\n  WITNESS WORLD -- delta held COMMON across the four tiers: recovery "
      f"{100*common_rec:.1f}%")
check("delta DISPERSION alone -- with no ordering imposed at all -- destroys the design's "
      "recovery of its own ordering",
      a_un < 0.25 * common_rec,
      witness=lambda: common_rec < 0.25 * common_rec)
print("  Witness is the common-delta world asked to clear its own bar, which it cannot.")
print("  So the confound and the ordering do DIFFERENT damage: dispersion destroys the")
print("  ranking (98.1% -> 88.5% of worlds non-recovering), and the ordering is what")
print("  turns the wreckage into a REVERSAL (23.8% against 1.1%).")

# ================================================================== E2
hr("E2 - the goodwill decay rate at which the strict reversal breaks (REG-002 E2)")

R_paper = closed_form(PHI, DELTA)
print(f"  the paper's ladder, R = {[round(float(x), 5) for x in R_paper]}")
print(f"  strictly decreasing (the tau = -1 claim): {strictly_decreasing(R_paper)}")

# R_3 = R_2  <=>  (1-phi_3) d/(alpha-d) = R_2  <=>  d = K*alpha/(1+K), K = R_2/(1-phi_3)
K = R_paper[2] / (1.0 - PHI[3])
d3_star = K * ALPHA / (1.0 + K)
print(f"\n  closed form: delta_3* = K*alpha/(1+K) with K = R_2/(1-phi_3) = {K:.6f}")
print(f"  delta_3*                      = {d3_star:.6f}")
print(f"  implied half-life             = {half_life(d3_star):.1f} periods")
print(f"  the paper assumes delta_3     = {DELTA[3]:.6f}  (half-life "
      f"{half_life(DELTA[3]):.1f})")
print(f"  margin                        = {d3_star - DELTA[3]:.6f}")

# verify the closed form numerically rather than trusting it
lo, hi = DELTA_LO, ALPHA - 1e-9
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if closed_form(PHI[3], mid) < R_paper[2]:
        lo = mid
    else:
        hi = mid
d3_bisect = 0.5 * (lo + hi)
print(f"  bisection check               = {d3_bisect:.6f}   "
      f"(|closed - bisect| = {abs(d3_star - d3_bisect):.2e})")

check("the closed form for the crossing rate agrees with bisection to 1e-9",
      abs(d3_star - d3_bisect) < 1e-9,
      witness=lambda: abs(d3_star * 1.001 - d3_bisect) < 1e-9)

D_broken = DELTA.copy()
D_broken[3] = d3_star * 1.05
R_broken = closed_form(PHI, D_broken)
print(f"\n  at delta_3 = {D_broken[3]:.5f} (5% above the crossing):")
print(f"    R = {[round(float(x), 5) for x in R_broken]}")
print(f"    strictly decreasing: {strictly_decreasing(R_broken)}   "
      f"Kendall tau = {kendall_tau(-PHI, R_broken):+.2f}")

check("a goodwill decay rate barely above the crossing destroys the tau = -1 reversal",
      not strictly_decreasing(R_broken),
      witness=lambda: not strictly_decreasing(R_paper))
print("  Witness is the paper's own calibration, where the ladder IS strictly")
print("  decreasing -- so the check is reading the goodwill rate and nothing else.")

# REGISTERED FALSIFIER (REG-002 E2): delta_3* < 0.010 makes tau = -1 a knife edge.
print(f"\n  REG-002 E2 threshold: delta_3* < 0.010 -> knife edge.  delta_3* = "
      f"{d3_star:.6f}  -> {'FIRES' if d3_star < 0.010 else 'does not fire'}")

# ================================================================== E3
hr("E3 - lumpy, not slow (REG-002 E3)")

print("  REG-002 section 3.1 declared this extension BEFORE it was written: LayeredFirm")
print("  takes a scalar entropy_rate; E3 needs a per-period sequence. The extension is a")
print("  strict generalisation and its reproduction of LayeredFirm is itself a check.\n")


def run_varying(decay_seq, phi, alpha=ALPHA, e0=E0):
    """LayeredFirm with a per-period decay sequence. maintenance_ratio = 0, theta = inf."""
    T = len(decay_seq)
    E = np.empty(T + 1)
    C = np.empty(T + 1)
    gap = np.empty(T + 1)
    E[0] = C[0] = e0
    gap[0] = 0.0
    for t in range(T):
        E[t + 1] = E[t] * (1.0 - decay_seq[t])
        dE = E[t + 1] - E[t]
        C[t + 1] = C[t] + phi * dE + alpha * gap[t]
        gap[t + 1] = E[t + 1] - C[t + 1]
    return E, C, gap


_e, _c, _g = run_varying(np.full(PERIODS, 0.013), 0.37)
_ref = firm(0.37, 0.013, ALPHA, np.inf).run(PERIODS)
repro = float(np.max(np.abs(_g - _ref["gap"])))
print(f"  constant-sequence reproduction of LayeredFirm: max |gap diff| = {repro:.3e}")
check("the varying-decay extension reproduces LayeredFirm on a constant sequence",
      repro < 1e-12,
      witness=lambda: float(np.max(np.abs(
          run_varying(np.full(PERIODS, 0.014), 0.37)[2] - _ref["gap"]))) < 1e-12)
print("  Witness is the same comparison at a DIFFERENT constant rate, which must differ.")

MEAN_D = 0.010          # tier 2's rate: a class that IS scheduled
PHI_L = 0.20            # goodwill's observability
JUMP_P = 0.05           # rare
JUMP_D = MEAN_D / JUMP_P
BURN = 100
PATHS = 2000

print(f"\n  smooth class : delta = {MEAN_D} every period")
print(f"  lumpy class  : delta = {JUMP_D:.3f} with probability {JUMP_P}, else 0")
print(f"                 -> identical MEAN decay rate {JUMP_P*JUMP_D:.4f}, phi = {PHI_L}")

rng = np.random.default_rng(SEED + 7)
ratios = np.empty(PATHS)
for k in range(PATHS):
    seq = np.where(rng.random(PERIODS) < JUMP_P, JUMP_D, 0.0)
    E, C, g = run_varying(seq, PHI_L)
    good = E[BURN:] > 0
    ratios[k] = float(np.mean(np.abs(g[BURN:][good]) / E[BURN:][good]))

R_smooth = closed_form(PHI_L, MEAN_D)
lumpy_mean = float(ratios.mean())
lumpy_se = float(ratios.std() / np.sqrt(PATHS))
ratio = lumpy_mean / R_smooth

print(f"\n  R at the mean rate (closed form)      : {R_smooth:.6f}")
print(f"  realised deferral ratio, lumpy path   : {lumpy_mean:.6f}  (se {lumpy_se:.6f}, "
      f"{PATHS} paths)")
print(f"  lumpy / smooth                        : {ratio:.4f}")
print(f"  in delta-equivalent terms, the lumpy class defers like a smooth class at "
      f"delta = {ALPHA*lumpy_mean/((1-PHI_L)+lumpy_mean):.5f}")

# REGISTERED (REG-002 E3): MEASURE the ratio; either sign is informative.
check("a lumpy decline defers MORE than a smooth one at the same mean rate",
      ratio > 1.0 + 10 * lumpy_se / R_smooth,
      witness=lambda: closed_form(PHI_L, MEAN_D) / R_smooth
      > 1.0 + 10 * lumpy_se / R_smooth)
print("  Witness is the smooth class measured against itself, which is 1.0 by")
print("  construction and cannot exceed the tolerance.")

d_equiv = ALPHA * lumpy_mean / ((1 - PHI_L) + lumpy_mean)
print(f"\n  So 'unscheduled' proxied as 'slow' is wrong TWICE over: the mean rate need not")
print(f"  be small, and at any given mean rate lumpiness RAISES the deferral measure.")
print(f"  Goodwill's delta-equivalent under this lumpy path is {d_equiv:.5f}, against the")
print(f"  paper's assumed {DELTA[3]:.5f} and the crossing rate {d3_star:.5f}.")
print(f"  Above the crossing: {d_equiv > d3_star}")

# ================================================================== E4
hr("E4 - the disclosed-numbers ladder (REG-002 E4)")

print("  Two rungs need no inference. ASC 360 and ASC 350-30-50 make firms DISCLOSE")
print("  useful lives for property and for finite-lived intangibles. Under REG-002")
print("  section 3.2's stated bridge, a disclosed life L gives a write-down rate 1/L.")
print("  That bridge is an ASSUMPTION -- but a falsifiable one about a published number,")
print("  which is strictly better located than an inference from an ABSENCE.\n")

# Ranges spanned by disclosure practice, declared as ranges rather than as a sample this
# session does not have. A reader with their own filings locates themselves on the curve.
LIFE_PPE = (10.0, 40.0)          # ASC 360 practice: machinery through buildings
LIFE_FIN = (3.0, 20.0)           # ASC 350-30 practice: technology through trademarks

print(f"  property, plant and equipment : lives {LIFE_PPE[0]:.0f}-{LIFE_PPE[1]:.0f}y "
      f"-> delta_0 in [{1/LIFE_PPE[1]:.4f}, {1/LIFE_PPE[0]:.4f}]")
print(f"  finite-lived intangibles      : lives {LIFE_FIN[0]:.0f}-{LIFE_FIN[1]:.0f}y "
      f"-> delta_1 in [{1/LIFE_FIN[1]:.4f}, {1/LIFE_FIN[0]:.4f}]")
print(f"  the paper's table asserts       delta_0 = {DELTA[0]:.3f} > delta_1 = "
      f"{DELTA[1]:.3f}  (lives {1/DELTA[0]:.0f}y and {1/DELTA[1]:.0f}y)")

G = 400
d0_grid = np.linspace(1 / LIFE_PPE[1], 1 / LIFE_PPE[0], G)
d1_grid = np.linspace(1 / LIFE_FIN[1], 1 / LIFE_FIN[0], G)
D0, D1 = np.meshgrid(d0_grid, d1_grid, indexing="ij")

admissible = (D0 < ALPHA) & (D1 < ALPHA)
frac_admissible = float(admissible.mean())

with np.errstate(divide="ignore", invalid="ignore"):
    R0 = (1 - PHI[0]) * D0 / (ALPHA - D0)
    R1 = (1 - PHI[1]) * D1 / (ALPHA - D1)
rung_rises = (R1 > R0) & admissible

frac_rises_of_admissible = float(rung_rises.sum() / max(admissible.sum(), 1))
frac_rises_of_all = float(rung_rises.mean())

print(f"\n  fraction of the disclosed rectangle INSIDE the model's domain (delta < alpha):"
      f" {100*frac_admissible:.1f}%")
print(f"  of that admissible part, the first rung RISES in : "
      f"{100*frac_rises_of_admissible:.1f}%")
print(f"  as a share of the whole rectangle               : "
      f"{100*frac_rises_of_all:.1f}%")

# the exact boundary, so a reader can locate their own firm
print("\n  the boundary is exact: rung 0->1 falls iff  (1-phi_1)*g(delta_1) <"
      " (1-phi_0)*g(delta_0),")
print("  g(d) = d/(alpha-d).  With phi = (0.80, 0.60) that is g(delta_1) < 0.5*g(delta_0),")
print("  i.e. delta_1 < alpha*delta_0 / (2*alpha - delta_0).")
d1_boundary = ALPHA * DELTA[0] / (2 * ALPHA - DELTA[0])
print(f"  At the paper's delta_0 = {DELTA[0]:.3f} the boundary sits at delta_1 = "
      f"{d1_boundary:.5f}")
print(f"  and the paper picks delta_1 = {DELTA[1]:.3f} -- inside by "
      f"{d1_boundary - DELTA[1]:.5f}, i.e. a life of {1/d1_boundary:.1f}y against the "
      f"{1/DELTA[1]:.0f}y assumed.")

check("the paper's first rung sits within a hair of its own boundary",
      abs(d1_boundary - DELTA[1]) < 0.25 * DELTA[1],
      witness=lambda: abs(d1_boundary - DELTA[2]) < 0.25 * DELTA[2])
print("  Witness is the same margin computed for tier 2's rate, which is not near it.")

# REGISTERED FALSIFIER (REG-002 E4) -- AND THE ANSWER IS BIGGER THAN THE QUESTION.
#
# The registered test asks what fraction of the ADMISSIBLE rectangle sees the first rung
# rise. At the paper's alpha the admissible rectangle is EMPTY: every disclosed useful
# life short enough to appear in a filing implies a decay rate at or above alpha = 0.05,
# and R is not defined there. E6 was registered as a boundary check on a corner of the
# parameter space. It is not a corner. It is where the disclosed numbers all live.
#
# The registered falsifier is therefore VACUOUS AT THE PAPER'S CALIBRATION -- a share of
# an empty set -- and saying "does not fire" would be a phantom tag on the section scale.
# It is evaluated instead at an alpha for which the question has a domain, and that
# substitution is marked as an extension of the registered test rather than the test.
print(f"\n  REG-002 E4's registered falsifier is a share of the ADMISSIBLE rectangle,")
print(f"  and at alpha = {ALPHA} that rectangle is EMPTY. The registered test is vacuous")
print(f"  here -- not passed, not failed. Reported as such, and evaluated below at an")
print(f"  alpha where it has a domain. That substitution is an EXTENSION of REG-002 E4,")
print(f"  not the registered test, and is labelled so in the manuscript.")

check("at the paper's calibration the disclosed rectangle lies entirely outside the "
      "model's domain",
      frac_admissible == 0.0,
      witness=lambda: float((((D0 < 0.35) & (D1 < 0.35)).mean())) == 0.0)
print("  Witness is the same rectangle against a recognition rate of 0.35, which contains")
print("  it -- so the check is reading alpha and not the rectangle.")

# What alpha does the disclosed rectangle require?
alpha_full = float(max(d0_grid.max(), d1_grid.max()))
alpha_half = None
for a in np.linspace(0.02, 0.40, 761):
    if float(((D0 < a) & (D1 < a)).mean()) >= 0.5:
        alpha_half = float(a)
        break
print(f"\n  recognition rate needed for HALF the disclosed rectangle to be admissible : "
      f"{alpha_half:.4f}  (a catch-up half-life of {np.log(0.5)/np.log(1-alpha_half):.1f}"
      f" periods)")
print(f"  recognition rate needed for ALL of it                                     : "
      f"> {alpha_full:.4f}")
print(f"  the paper's alpha                                                         : "
      f"{ALPHA:.4f}")

# The rung question, asked where it has a domain.
A_EXT = 0.35
R0e = (1 - PHI[0]) * D0 / (A_EXT - D0)
R1e = (1 - PHI[1]) * D1 / (A_EXT - D1)
adm_e = (D0 < A_EXT) & (D1 < A_EXT)
rises_e = float(((R1e > R0e) & adm_e).sum() / max(adm_e.sum(), 1))
print(f"\n  EXTENSION, alpha = {A_EXT}: admissible share {100*float(adm_e.mean()):.1f}%,"
      f" first rung RISES in {100*rises_e:.1f}% of it")
print(f"  boundary in general form: the rung falls iff delta_1 < alpha*delta_0 /"
      f" (2*alpha - delta_0),")
print(f"  which tends to delta_0/2 as alpha grows. Disclosure amortises finite-lived")
print(f"  intangibles over SHORTER lives than property, i.e. delta_1 > delta_0 -- so the")
print(f"  rung cannot fall anywhere a filing actually puts a firm.")

check("wherever the question has a domain at all, the first rung of the paper's table "
      "runs the other way on disclosed useful lives",
      rises_e > 0.5,
      witness=lambda: float((((1 - PHI[1]) * np.minimum(D1, d1_boundary)
                              / (A_EXT - np.minimum(D1, d1_boundary))
                              > (1 - PHI[0]) * D0 / (A_EXT - D0)) & adm_e).sum()
                            / max(adm_e.sum(), 1)) > 0.5)
print("  Witness caps delta_1 at the boundary curve, where the rung cannot rise -- so a")
print("  check that passed for both would not be reading the curve.")

# ================================================================== E5
hr("E5 - what governs the direction, FITTED (REG-002 E5)")

print("  Section 4.4's decomposition: a rung rises iff")
print("      dlog(1-phi) + dlog(delta) - dlog(alpha-delta) > 0")
print("  Define, per ladder, the DESIGN BUDGET as the mean design term per rung and the")
print("  DELTA LEVERAGE as the mean absolute combined delta contribution per rung.\n")

rng5 = np.random.default_rng(SEED + 11)
xs, ys = [], []
for _ in range(N):
    phi = np.sort(rng5.uniform(PHI_LO, PHI_HI, 4))[::-1]
    d = rng5.uniform(DELTA_LO, DELTA_HI, 4)
    R = (1 - phi) * d / (ALPHA - d)
    budget = np.mean([np.log((1 - phi[i + 1]) / (1 - phi[i])) for i in range(3)])
    lever = np.mean([abs(np.log(d[i + 1] / d[i])
                         - np.log((ALPHA - d[i + 1]) / (ALPHA - d[i]))) for i in range(3)])
    if budget <= 0 or lever <= 0:
        continue
    xs.append(np.log(lever / budget))
    ys.append(0.0 if strictly_increasing(R) else 1.0)

x = np.asarray(xs)
y = np.asarray(ys)
X = np.column_stack([np.ones_like(x), x])

def _irls(design, outcome):
    bb = np.zeros(design.shape[1])
    for _ in range(60):
        pp = 1.0 / (1.0 + np.exp(-(design @ bb)))
        WW = np.clip(pp * (1 - pp), 1e-9, None)
        bb = bb + np.linalg.solve(design.T @ (design * WW[:, None]),
                                  design.T @ (outcome - pp))
    pp = 1.0 / (1.0 + np.exp(-(design @ bb)))
    ss = np.sqrt(np.diag(np.linalg.inv(
        design.T @ (design * np.clip(pp * (1 - pp), 1e-9, None)[:, None]))))
    return bb, ss


def _shuffled_slope_z():
    """The identical fit on a PERMUTED outcome: the slope must lose significance."""
    rs = np.random.default_rng(SEED + 13)
    bb, ss = _irls(X, rs.permutation(y))
    return float(abs(bb[1] / ss[1]))


b = np.zeros(2)
for _ in range(60):                       # IRLS
    eta = X @ b
    p = 1.0 / (1.0 + np.exp(-eta))
    W = np.clip(p * (1 - p), 1e-9, None)
    H = X.T @ (X * W[:, None])
    g = X.T @ (y - p)
    b = b + np.linalg.solve(H, g)
cov = np.linalg.inv(X.T @ (X * (1.0 / (1.0 + np.exp(-(X @ b)))
                                * (1 - 1.0 / (1.0 + np.exp(-(X @ b)))))[:, None]))
se = np.sqrt(np.diag(cov))
crossover = float(np.exp(-b[0] / b[1]))

print(f"  fitted logit P(design fails) = {b[0]:+.4f} + {b[1]:+.4f} * log(leverage/budget)")
print(f"     se                        =  {se[0]:.4f}          {se[1]:.4f}")
print(f"     z on the slope            =  {b[1]/se[1]:+.1f}")
print(f"  crossover (P = 0.5) at leverage/budget = {crossover:.4f}")
print(f"\n  THE DESIGN RULE, and it is a fitted number, not an asserted one: a phi-ordered")
print(f"  cross-section is more likely than not to recover its own ordering only while the")
print(f"  ladder's per-rung delta leverage stays below {crossover:.2f} times its design")
print(f"  budget. The paper's own ladder sits at "
      f"{np.mean([abs(np.log(DELTA[i+1]/DELTA[i]) - np.log((ALPHA-DELTA[i+1])/(ALPHA-DELTA[i]))) for i in range(3)]) / np.mean([np.log((1-PHI[i+1])/(1-PHI[i])) for i in range(3)]):.2f}.")

check("the fitted slope is positive and many standard errors from zero",
      b[1] > 0 and b[1] / se[1] > 10,
      witness=lambda: _shuffled_slope_z() > 10)
print(f"  Witness is the identical fit on a PERMUTED outcome: z = "
      f"{_shuffled_slope_z():.2f}, so the check is reading the ladder and not the design"
      f" matrix.")

# ================================================================== E6
hr("E6 - the alpha-delta boundary, which the disclosed numbers walk into (REG-002 E6)")

print(f"  R = (1-phi)*delta/(alpha-delta) has a pole at delta = alpha and is NEGATIVE")
print(f"  beyond it. The paper's calibration keeps delta <= {DELTA[0]:.3f} under alpha =")
print(f"  {ALPHA}. Disclosed intangible lives of {1/ALPHA:.0f} years or shorter cross it.\n")

print(f"  {'delta':>8}{'d/alpha':>10}{'log10 ratio t=400':>20}{'t=800':>12}"
      f"{'closed form':>14}{'settles':>10}")
for d in [0.010, 0.030, 0.045, 0.049, 0.051, 0.060, 0.100, 0.200]:
    r400 = firm(0.20, d, ALPHA, np.inf).run(400)
    r800 = firm(0.20, d, ALPHA, np.inf).run(800)
    v400 = float(abs(r400["gap"][-1]) / r400["real"][-1])
    v800 = float(abs(r800["gap"][-1]) / r800["real"][-1])
    cf = closed_form(0.20, d)
    settles = abs(v800 - v400) < 1e-3 * max(v400, 1.0)
    print(f"  {d:>8.3f}{d/ALPHA:>10.2f}{np.log10(max(v400, 1e-300)):>20.3f}"
          f"{np.log10(max(v800, 1e-300)):>12.3f}{cf:>14.4f}{str(settles):>10}")
print("  (log10 of the gap ratio, because past the pole it leaves the page: at delta =")
print("   0.200 it reaches 10^69 by t = 400 and 10^140 by t = 800.)")

r_sub = firm(0.20, 0.030, ALPHA, np.inf)
sub400 = float(abs(r_sub.run(400)["gap"][-1]) / r_sub.run(400)["real"][-1])
sub800 = float(abs(r_sub.run(800)["gap"][-1]) / r_sub.run(800)["real"][-1])
r_sup = firm(0.20, 0.100, ALPHA, np.inf)
sup400 = float(abs(r_sup.run(400)["gap"][-1]) / r_sup.run(400)["real"][-1])
sup800 = float(abs(r_sup.run(800)["gap"][-1]) / r_sup.run(800)["real"][-1])

print(f"\n  delta < alpha : ratio settles     ({sub400:.4f} -> {sub800:.4f}, "
      f"change {abs(sub800-sub400):.2e})")
print(f"  delta > alpha : ratio does NOT    ({sup400:.4f} -> {sup800:.4f}, "
      f"change {abs(sup800-sup400):.2e})")

check("no steady-state deferral ratio exists once the decay rate exceeds the "
      "recognition rate",
      abs(sup800 - sup400) > 1e3 * abs(sub800 - sub400),
      witness=lambda: abs(sub800 - sub400) > 1e3 * abs(sub800 - sub400))
print("  Witness is the sub-critical case asked the same question, which settles.")

print("\n  So section 4.4's measure is defined only where the recognition rate exceeds the")
print("  economic decay rate. That is not a calibration detail: it is a statement about")
print("  WHICH FIRMS the section speaks to, and it belongs in the section.")

# ================================================================== E7
hr("E7 - does the LAG survival survive it too? (REG-002 E7, registered before coding)")

print("  Section 4.5 reports the lag ordering holding in 100% of 400 random admissible")
print("  ladders -- drawn under the SAME two constraints E1 drops. If the statistic that")
print("  survived the confound survived it only because of the durability assumption,")
print("  section 4.5's concession needs narrowing in the same breath it reports the 100%.\n")


def lag_draw(m, seed, order_delta):
    rng = np.random.default_rng(seed)
    hits = 0
    for _ in range(m):
        phi = np.sort(rng.uniform(PHI_LO, PHI_HI, 4))[::-1]
        d = rng.uniform(DELTA_LO, DELTA_HI, 4)
        if order_delta:
            d = np.sort(d)[::-1]
        lag = [recognition_lag(firm(p, dd, ALPHA, np.inf).run(PERIODS))
               for p, dd in zip(phi, d)]
        if all(lag[i] <= lag[i + 1] for i in range(3)):
            hits += 1
    return hits / m


lag_ord = lag_draw(M, SEED + 1, order_delta=True)
lag_un = lag_draw(M, SEED + 1, order_delta=False)

print(f"  lag non-decreasing up the ladder, ORDERED delta   : {100*lag_ord:.1f}%"
      f"   (WT-083 reports 100.0%)")
print(f"  lag non-decreasing up the ladder, UNORDERED delta : {100*lag_un:.1f}%")
print(f"  compare the MAGNITUDE measure, unordered          : {100*a_un:.1f}%")

se400 = float(np.sqrt(lag_un * (1 - lag_un) / M))
print(f"  binomial se at M = {M} (WT-083's sample size, the registered one) : "
      f"{se400:.3f}")

# The registered figure lands within one standard error of the registered threshold, so
# the threshold is not cleanly separated at WT-083's sample size. Precision on a
# REGISTERED QUANTITY is raised; the registered figure is reported alongside, and the
# larger sample was run before either side of the threshold was preferred.
M_BIG = 2000
lag_un_big = lag_draw(M_BIG, SEED + 1, order_delta=False)
se_big = float(np.sqrt(lag_un_big * (1 - lag_un_big) / M_BIG))
print(f"\n  PRECISION CHECK, same estimator at M = {M_BIG}                       : "
      f"{100*lag_un_big:.1f}%  (se {se_big:.3f})")
print(f"  the registered figure sits {abs(lag_un - 0.70)/se400:.2f} se from the registered")
print(f"  threshold; the precision check sits {abs(lag_un_big - 0.70)/se_big:.2f} se from it.")

verdict = ('NARROW' if lag_un_big + 2 * se_big < 0.70 else
           ('STRENGTHENS' if lag_un_big - 2 * se_big >= 0.90 else
            'DEGRADES, threshold not cleanly separated'))
print(f"\n  REG-002 E7: below 0.70 -> narrow the concession; at or above 0.90 ->")
print(f"  a strengthening obtained by trying to break it.")
print(f"  registered M = {M}: {lag_un:.3f}   ·   precision M = {M_BIG}: {lag_un_big:.3f}")
print(f"  -> {verdict}")

check("the lag ordering DEGRADES materially once the durability ordering is dropped",
      lag_un_big + 3 * se_big < lag_ord,
      witness=lambda: lag_ord + 3 * se_big < lag_ord)
print("  Witness is the ordered draw asked to fall materially below itself.")

check("the timing statistic survives an assumption the magnitude statistic needed",
      lag_un > 5 * max(a_un, 1e-9),
      witness=lambda: a_un > 5 * max(a_un, 1e-9))
print("  Witness is the magnitude measure asked to clear its own bar, which it cannot.")

hr("SUMMARY")
print(f"  E1  mean tau, ordered {tau_ord.mean():+.3f} -> unordered {tau_un.mean():+.3f}")
print(f"  E2  the reversal breaks at delta_3 = {d3_star:.5f} (half-life "
      f"{half_life(d3_star):.0f}y); the paper assumes {DELTA[3]:.5f}")
print(f"  E3  lumpy/smooth deferral ratio {ratio:.3f} at an identical mean rate")
print(f"  E4  first rung rises over {100*frac_rises_of_admissible:.1f}% of the admissible "
      f"disclosed rectangle")
print(f"  E5  P(failure) = 0.5 at leverage/budget = {crossover:.3f} (fitted, z = "
      f"{b[1]/se[1]:+.0f})")
print(f"  E6  no steady state for delta > alpha; {100*(1-frac_admissible):.1f}% of the "
      f"disclosed rectangle is outside the model's domain")
print(f"  E7  lag ordering {100*lag_ord:.1f}% ordered -> {100*lag_un_big:.1f}% unordered "
      f"(M = {M_BIG}, se {se_big:.3f})")
summary()
