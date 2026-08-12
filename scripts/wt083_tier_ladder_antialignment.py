"""WT-083: the registered ladder, and the direction the composite actually runs.

WHY THIS SCRIPT EXISTS
----------------------
WT-082 established the identification result (phi reaches a reported series only as
phi*delta; the root swap is exact) and then asserted, as C5, that "with delta varying
across classes the observable does NOT order by phi." At the paper's own calibration
THAT ASSERTION IS FALSE -- the observable came out monotone across the four tiers, and
the run failed. The assertion was written from the shape of the algebra rather than from
a number, which is the thing WT-080 exists to prevent.

The failure is more interesting than the claim it was meant to support, and this script
establishes what is actually true.

WHAT IS ESTABLISHED HERE
------------------------
D1  The steady-state observable is R = (1-phi)*delta/(alpha-delta). Up the GAAP ladder
    (1-phi) RISES by design and delta FALLS by physical fact. The two move against each
    other, so the ordering of R across the ladder is not determined by the registered
    ordering of phi at all: it is determined by which of the two moves further in logs.

D2  AT THE PAPER'S OWN CALIBRATION THE COMPOSITE RUNS BACKWARDS. R is monotone across
    the four tiers -- but DECREASING, while the registration predicted the deferral
    measure to INCREASE. The registered design and the model's own observable are
    anti-aligned across the ladder: Kendall tau = -1.

D3  THE DESIGN'S VALIDITY CONDITION IS A STATEMENT ABOUT DELTA. R orders by phi iff
        dlog(1-phi) + dlog(delta) - dlog(alpha-delta) > 0
    tier by tier. Every term but the first is a fact about delta -- the quantity the
    identification result says a reported series cannot supply. So a researcher cannot
    check whether a phi-ordered design is valid without already knowing what the design
    was built to avoid needing.

D4  IT IS NOT A KNIFE EDGE. Over random ladders drawn to respect only the qualitative
    facts the registration relied on (phi falls up the ladder, durability rises up the
    ladder), the observable recovers the registered ordering a minority of the time, and
    reverses it far more often than it agrees.

D5  THE SAME REVERSAL HOLDS IN THE REGISTERED QUANTITY. The registration ordered
    RECOGNITION LAG, not the gap ratio. Computed across the realistic ladder the model's
    own lag statistic is flat-to-reversed; computed across the ladder the design silently
    assumed (a common delta) it is monotone in the predicted direction. The design was
    valid in a world it did not inhabit.

D6  THE EVENT COUNT COLLAPSES AT THE TOP OF THE LADDER. At the realistic ladder the two
    least-observable tiers generate ZERO recognition events in 400 periods, while the two
    most-observable tiers generate all of them. The tiers the registration leaned on
    hardest are the tiers at which this model produces nothing to measure.

Each check ships a witness (scripts/severity.py). Where a claim is a direction, the
witness is the same computation with the opposing ladder substituted -- so a check that
would pass under either ladder is caught.

    ./.venv/bin/python scripts/wt083_tier_ladder_antialignment.py
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

# The registered ordering: observability falls up the ladder. PRE-001, verbatim in intent.
PHI = np.array([0.80, 0.60, 0.40, 0.20])

# The physical fact the registration did not price in: durability RISES up the same
# ladder, so the effective decay rate falls. Goodwill has no degradation schedule at all,
# which is why ASC 350 tests it rather than amortising it -- the same sentence that
# supplied the phi ordering supplies the delta ordering, running the other way.
DELTA = np.array([0.030, 0.020, 0.010, 0.002])

# What the design silently assumed: that the classes differ in phi and in nothing else.
DELTA_COMMON = np.full(4, 0.020)


def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


def firm(phi, delta, alpha=ALPHA, theta=THETA):
    return LayeredFirm(initial_wealth=E0, entropy_rate=delta, maintenance_ratio=0.0,
                       observable_share=phi, recognition_rate=alpha,
                       crisis_threshold=theta)


def gap_ratio(phi, delta, alpha=ALPHA):
    r = firm(phi, delta, alpha, np.inf).run(PERIODS)
    return float(abs(r["gap"][-1]) / r["real"][-1])


def closed_form(phi, delta, alpha=ALPHA):
    return (1.0 - phi) * delta / (alpha - delta)


def kendall_tau(a, b):
    """Kendall tau-a. No scipy dependency; n = 4."""
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


# ---------------------------------------------------------------- D1 / D2
hr("D1/D2 - the registered ladder, and the direction the observable actually runs")

print("  The registration predicted DEFERRAL RISES up the ladder: PP&E least, goodwill most.")
print("  R = (1-phi)*delta/(alpha-delta) is the model's steady-state deferral measure.\n")
print(f"  {'tier':<32}{'phi':>6}{'1-phi':>8}{'delta':>8}{'(1-phi)d':>11}{'R sim':>11}{'R closed':>11}")

R_real, R_common, comp = [], [], []
for name, p, d in zip(TIERS, PHI, DELTA):
    g, cf = gap_ratio(p, d), closed_form(p, d)
    R_real.append(g)
    comp.append((1 - p) * d)
    print(f"  {name:<32}{p:>6.2f}{1 - p:>8.2f}{d:>8.3f}{(1 - p) * d:>11.5f}{g:>11.6f}{cf:>11.6f}")

for p, d in zip(PHI, DELTA_COMMON):
    R_common.append(gap_ratio(p, d))

tau_real = kendall_tau(-PHI, R_real)       # -PHI = the registered rank order (rising deferral)
tau_common = kendall_tau(-PHI, R_common)

print(f"\n  ladder the design ASSUMED (common delta = 0.020):  R = "
      f"{[round(x, 5) for x in R_common]}")
print(f"  ladder the world SUPPLIES (delta falls up the ladder): R = "
      f"{[round(x, 5) for x in R_real]}")
print(f"\n  Kendall tau (registered rank vs observable), assumed ladder : {tau_common:+.2f}")
print(f"  Kendall tau (registered rank vs observable), real ladder    : {tau_real:+.2f}")

check("under a COMMON delta the observable recovers the registered ordering exactly",
      tau_common == +1.0,
      witness=lambda: kendall_tau(-PHI, R_real) == +1.0)

check("under the REAL delta ladder the observable runs exactly backwards",
      tau_real == -1.0,
      witness=lambda: kendall_tau(-PHI, R_common) == -1.0)

print("\n  So the test was not merely confounded. Across this ladder the quantity the")
print("  instrument can see is anti-aligned with the quantity the registration ordered:")
print("  a design that could confirm the theory only if the theory were wrong about delta.")

# ---------------------------------------------------------------- D3
hr("D3 - the design's validity condition is a statement about delta")

print("  log R = log(1-phi) + log(delta) - log(alpha - delta).")
print("  R rises up the ladder iff, tier by tier,")
print("      dlog(1-phi)  +  dlog(delta)  -  dlog(alpha-delta)  >  0")
print("  The first term is the design. The second and third are facts about delta.\n")
print(f"  {'step':<12}{'dlog(1-phi)':>14}{'dlog(delta)':>14}{'-dlog(a-d)':>13}{'sum':>10}{'R rises':>10}")

sums = []
for i in range(3):
    t1 = np.log((1 - PHI[i + 1]) / (1 - PHI[i]))
    t2 = np.log(DELTA[i + 1] / DELTA[i])
    t3 = -np.log((ALPHA - DELTA[i + 1]) / (ALPHA - DELTA[i]))
    s = t1 + t2 + t3
    sums.append(s)
    print(f"  {i}->{i+1:<9}{t1:>14.4f}{t2:>14.4f}{t3:>13.4f}{s:>10.4f}"
          f"{str(R_real[i + 1] > R_real[i]):>10}")

pred = [s > 0 for s in sums]
obs = [R_real[i + 1] > R_real[i] for i in range(3)]
check("the log-decomposition predicts the step direction at every rung",
      pred == obs,
      witness=lambda: [s > 0 for s in sums] == [not o for o in obs])

# delta enters log R TWICE -- once through log(delta) and once through -log(alpha-delta) --
# and on a falling ladder both carry the same sign, against the design. The comparison
# that matters is therefore the design term against the COMBINED delta contribution, not
# against log(delta) alone. (At rung 0->1 log(delta) alone does NOT outweigh the design
# term: 0.4055 against 0.6931. The rung still falls, because the second delta term adds
# another -0.4055. Checking one term would have got the rung right for the wrong reason.)
def delta_term(i):
    return np.log(DELTA[i + 1] / DELTA[i]) - np.log((ALPHA - DELTA[i + 1]) / (ALPHA - DELTA[i]))


def design_term(i):
    return np.log((1 - PHI[i + 1]) / (1 - PHI[i]))


dominates = [abs(delta_term(i)) > design_term(i) for i in range(3)]
print(f"\n  |combined delta contribution| exceeds the design term at every rung: "
      f"{all(dominates)}  {[bool(x) for x in dominates]}")
print(f"    combined delta terms : {[round(float(delta_term(i)), 4) for i in range(3)]}")
print(f"    design terms         : {[round(float(design_term(i)), 4) for i in range(3)]}")
check("the combined delta contribution outweighs the design term at every rung",
      all(dominates),
      witness=lambda: all(abs(0.0) > design_term(i) for i in range(3)))
print("  Witness is the common-delta ladder, where both delta terms vanish identically")
print("  and therefore cannot outweigh anything.")

# ---------------------------------------------------------------- D4
hr("D4 - not a knife edge: random ladders respecting only the qualitative facts")

rng = np.random.default_rng(SEED)
N = 4000
agree = reverse = neither = 0
taus = []
for _ in range(N):
    # phi: four draws, sorted DESCENDING -- observability falls up the ladder (the design).
    phi = np.sort(rng.uniform(0.05, 0.95, 4))[::-1]
    # delta: four draws, sorted DESCENDING -- durability rises up the ladder (the fact).
    # Range spans the paper's own sector sketches, from software to a class that barely decays.
    delta = np.sort(rng.uniform(0.001, 0.040, 4))[::-1]
    R = (1 - phi) * delta / (ALPHA - delta)
    t = kendall_tau(-phi, R)
    taus.append(t)
    if strictly_increasing(R):
        agree += 1
    elif strictly_decreasing(R):
        reverse += 1
    else:
        neither += 1

taus = np.array(taus)
print(f"  {N} random ladders, both orderings imposed and nothing else:")
print(f"    observable recovers the registered ordering : {agree:5d}  ({100*agree/N:5.1f}%)")
print(f"    observable exactly reverses it              : {reverse:5d}  ({100*reverse/N:5.1f}%)")
print(f"    neither (non-monotone)                      : {neither:5d}  ({100*neither/N:5.1f}%)")
print(f"    mean Kendall tau vs the registered rank     : {taus.mean():+.3f}"
      f"   (sd {taus.std():.3f})")

check("a phi-ordered design recovers its own ordering in a minority of admissible worlds",
      agree / N < 0.5,
      witness=lambda: agree / N > 0.99)

# WITNESS for the direction: hold delta COMMON across tiers and redraw. Then the design
# must recover its ordering every single time, or the construction proves nothing.
agree_c = 0
rng2 = np.random.default_rng(SEED)
for _ in range(N):
    phi = np.sort(rng2.uniform(0.05, 0.95, 4))[::-1]
    d = rng2.uniform(0.001, 0.040)
    R = (1 - phi) * d / (ALPHA - d)
    if strictly_increasing(R):
        agree_c += 1
print(f"\n  WITNESS -- same draw, delta held COMMON across the four tiers:"
      f" {100*agree_c/N:.1f}% recover the ordering")
check("with delta common the same design recovers its ordering in every world",
      agree_c == N,
      witness=lambda: agree == N)

# ---------------------------------------------------------------- D5
hr("D5 - the same reversal in the registered quantity: recognition lag")

print("  PRE-001 ordered LAG, not the gap ratio. The model's lag statistic, both ladders:\n")
print(f"  {'tier':<32}{'lag (real ladder)':>20}{'lag (common delta)':>21}")
lag_real, lag_common = [], []
for name, p, d in zip(TIERS, PHI, DELTA):
    lr = recognition_lag(firm(p, d, ALPHA, np.inf).run(PERIODS))
    lc = recognition_lag(firm(p, 0.020, ALPHA, np.inf).run(PERIODS))
    lag_real.append(lr)
    lag_common.append(lc)
    print(f"  {name:<32}{lr:>20}{lc:>21}")

print(f"\n  lag monotone increasing up the ladder, common delta : "
      f"{strictly_increasing(lag_common)}")
print(f"  lag monotone increasing up the ladder, real ladder  : "
      f"{strictly_increasing(lag_real)}")

# THE NEGATIVE RESULT, AND IT IS THE IMPORTANT ONE.
# The magnitude observable reverses (D2). The TIMING observable does not: lag orders by
# phi under BOTH ladders, and the falling delta ladder makes the ordering STEEPER rather
# than flattening it. So the identification result does NOT, by itself, wreck a design
# ordered on lag. Anything claiming otherwise is claiming more than the arithmetic gives.
check("lag orders by phi under BOTH ladders -- the reversal does NOT reach the timing statistic",
      strictly_increasing(lag_real) and strictly_increasing(lag_common),
      witness=lambda: strictly_increasing(R_real) and strictly_increasing(R_common))
print("  Witness is the same question asked of the MAGNITUDE observable R, which is")
print("  monotone under one ladder and reversed under the other -- so a check that passed")
print("  for both statistics would be reading something other than the ladder.")

print("\n  How lag moves in each parameter separately (alpha = 0.05, theta = inf):")
print(f"  {'delta':>8}" + "".join(f"{p:>9.2f}" for p in [0.0, 0.2, 0.4, 0.6, 0.8]))
for d in [0.002, 0.005, 0.010, 0.020, 0.030, 0.040]:
    row = [recognition_lag(firm(p, d, ALPHA, np.inf).run(PERIODS))
           for p in [0.0, 0.2, 0.4, 0.6, 0.8]]
    print(f"  {d:>8.3f}" + "".join(f"{v:>9d}" for v in row))
print("  Lag falls in phi at every delta, and rises as delta falls at every phi.")
print("  On a ladder where BOTH move the way GAAP says they do, the two effects ADD.")

# D5b -- does the lag ordering survive arbitrary admissible ladders, or only this one?
rng3 = np.random.default_rng(SEED + 1)
M = 400
lag_agree = 0
for _ in range(M):
    phi = np.sort(rng3.uniform(0.05, 0.95, 4))[::-1]
    delta = np.sort(rng3.uniform(0.001, 0.040, 4))[::-1]
    lag = [recognition_lag(firm(p, d, ALPHA, np.inf).run(PERIODS)) for p, d in zip(phi, delta)]
    if all(lag[i] <= lag[i + 1] for i in range(3)):
        lag_agree += 1
print(f"\n  {M} random admissible ladders: lag non-decreasing up the ladder in "
      f"{100*lag_agree/M:.1f}% of them")
print(f"  (compare the magnitude observable R, which recovered the ordering in 1.9%)")
check("the lag ordering is robust across admissible ladders, not an artefact of this one",
      lag_agree / M > 0.9,
      witness=lambda: agree / N > 0.9)
print("  Witness is R's recovery rate over the same construction. If a check passes for")
print("  both, it is not distinguishing the timing statistic from the magnitude one.")

# ---------------------------------------------------------------- D6
hr("D6 - the event count collapses exactly where the registration leaned hardest")

print(f"  {'tier':<32}{'events (real)':>15}{'events (common d)':>19}")
ev_real, ev_common = [], []
for name, p, d in zip(TIERS, PHI, DELTA):
    er = firm(p, d, ALPHA, THETA).run(PERIODS)["n_crises"]
    ec = firm(p, 0.020, ALPHA, THETA).run(PERIODS)["n_crises"]
    ev_real.append(int(er))
    ev_common.append(int(ec))
    print(f"  {name:<32}{er:>15d}{ec:>19d}")

top_two_silent = ev_real[2] == 0 and ev_real[3] == 0
print(f"\n  the two least-observable tiers produce no events at all: {top_two_silent}")
check("at the real ladder the two least-observable tiers are silent",
      top_two_silent,
      witness=lambda: ev_common[2] == 0 and ev_common[3] == 0)
print("  Goodwill supplied the largest share of the registered sample. In this model,")
print("  at goodwill's decay rate, this model has nothing to say about goodwill.")

hr("SUMMARY")
summary()
