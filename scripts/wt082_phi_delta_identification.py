"""WT-082: what a reported series can and cannot say about phi.

THE QUESTION
------------
Limitation 4 of paper III observed that phi reaches the observable only through the
product phi*delta, and measured the consequence: recovering phi means dividing by an
estimated decay rate, and the estimator's variance grows like 1/delta^2. That was
reported as a conditioning result -- awkward, but survivable.

This script asks whether it is worse than that, and finds that it is. In the filter
regime the degeneracy is not a matter of conditioning at all. It is EXACT.

WHAT IS ESTABLISHED HERE
------------------------
C1  Closed form for the steady-state gap ratio: |gap|/E -> (1-phi)*delta/(alpha-delta).
    phi never appears alone; it appears as (1-phi)*delta.

C2  EXACT OBSERVATIONAL EQUIVALENCE. With the recognition mechanism disabled, the
    parameter triples

        (alpha, delta, phi)   and   (delta, alpha, phi*delta/alpha)

    generate the IDENTICAL reported series, to machine precision. The two roots of the
    filter -- the reporting rate and the physical decay rate -- are exchangeable, and the
    quantity preserved by the exchange is exactly phi*delta. A reported series therefore
    determines phi*delta and nothing further about phi. Admissibility condition:
    phi*delta <= alpha, which holds at every parameter setting the paper uses.

C3  The equivalence is broken ONLY by the recognition events, whose trigger references
    the gap -- that is, references E, which is not reported. Whether the break is usable
    is measured here rather than asserted.

C4  ISO-OBSERVABLE PAIRS. Two asset classes with different phi produce identical
    observable behaviour when their delta differ appropriately. Holding delta fixed
    across classes, the observables DO respond to phi -- which is the witness that the
    pairing is not vacuous, and the statement of the condition a cross-class design
    would have to satisfy.

C5  THE CROSS-CLASS COROLLARY. Index asset classes i. The recursion becomes

        C(t+1) = C(t) + phi (*) dE + alpha (*) gap(t)

    with (*) the Hadamard product -- elementwise, because each class's filter acts only
    on its own class. On the diagonal the observable ordering of classes is the ordering
    of (1-phi) (*) delta, NOT of phi. A design that ranks classes by expected phi while
    their delta also vary is reading the composite. PRE-001 was such a design.

C6  THE GOODWILL LIMIT. At delta = 0 the gap is identically zero, there are no
    recognition events at any phi, and phi drops out of the model entirely. The class
    that supplied the majority of PRE-001's events is the class at which the model's
    parameter of interest is not merely ill-conditioned but absent.

C7  The model's own lag statistic is a cross-correlation between dE and dC. dE is not
    reported. The statistic is therefore not computable from public data, which is a
    separate identification problem from C2 and was not previously stated.

Every check ships a WITNESS (see scripts/severity.py). Claims C2 and C6 are
DISCONTINUITIES, so each side of the boundary witnesses the other -- WT-076.

    ./.venv/bin/python scripts/wt082_phi_delta_identification.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from wealth_tensor.lag import (LayeredFirm, recognition_lag,  # noqa: E402
                               variance_concentration)
from severity import check, summary  # noqa: E402

PERIODS = 400
E0 = 100.0


def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


def firm(phi, delta, alpha=0.05, theta=0.25):
    """A firm whose EFFECTIVE decay is delta exactly (maintenance switched off)."""
    return LayeredFirm(initial_wealth=E0, entropy_rate=delta, maintenance_ratio=0.0,
                       observable_share=phi, recognition_rate=alpha,
                       crisis_threshold=theta)


def reported(phi, delta, alpha=0.05, theta=np.inf, periods=PERIODS):
    return firm(phi, delta, alpha, theta).run(periods)["reported"]


def gap_ratio_terminal(phi, delta, alpha=0.05):
    r = firm(phi, delta, alpha, np.inf).run(PERIODS)
    return float(abs(r["gap"][-1]) / r["real"][-1])


def closed_form_gap_ratio(phi, delta, alpha=0.05):
    """|gap|/E at the fixed point of g(t+1) = [(1-alpha)g(t) - (1-phi)delta] / (1-delta)."""
    return (1.0 - phi) * delta / (alpha - delta)


# ---------------------------------------------------------------- C1
hr("C1 - the steady-state gap ratio is (1-phi)*delta/(alpha-delta)")

GRID = [(0.2, 0.010), (0.3, 0.020), (0.5, 0.020), (0.8, 0.030), (0.0, 0.015)]
errs = []
for phi, delta in GRID:
    sim, cf = gap_ratio_terminal(phi, delta), closed_form_gap_ratio(phi, delta)
    errs.append(abs(sim - cf) / cf)
    print(f"  phi={phi:.2f} delta={delta:.3f}   sim {sim:.10f}   closed {cf:.10f}"
          f"   rel err {errs[-1]:.2e}")
worst = max(errs)

# WITNESS: feed the closed form a phi that is wrong by 0.1. If the assertion still
# passes, it was never touching phi.
wrong = [abs(gap_ratio_terminal(p, d) - closed_form_gap_ratio(min(p + 0.1, 1.0), d))
         / closed_form_gap_ratio(min(p + 0.1, 1.0), d) for p, d in GRID]
# The transient decays like [(1-alpha)/(1-delta)]^t, which at alpha=0.05, delta=0.030
# leaves ~2e-4 after 400 periods. The tolerance is set from that rate, not from taste.
transient = max(((1 - 0.05) / (1 - d)) ** PERIODS for _, d in GRID)
check("terminal gap ratio matches the closed form to the transient bound",
      worst < 1e-3,
      witness=lambda: max(wrong) < 1e-3)
print(f"  worst relative error {worst:.3e}   predicted transient {transient:.3e}"
      f"   (witness, phi off by 0.1: {max(wrong):.3e})")

# ---------------------------------------------------------------- C2
hr("C2 - EXACT observational equivalence: (alpha,delta,phi) ~ (delta,alpha,phi*delta/alpha)")

MIRROR = [(0.05, 0.020, 0.30), (0.05, 0.020, 0.00), (0.05, 0.020, 0.80),
          (0.08, 0.010, 0.50), (0.10, 0.040, 0.25)]
devs = []
for alpha, delta, phi in MIRROR:
    phi_m = phi * delta / alpha
    a = reported(phi, delta, alpha)
    b = reported(phi_m, alpha, delta)          # roots swapped
    dev = float(np.max(np.abs(a - b)))
    devs.append(dev / E0)
    print(f"  (a={alpha:.3f}, d={delta:.3f}, phi={phi:.2f})  ~  "
          f"(a={delta:.3f}, d={alpha:.3f}, phi'={phi_m:.4f})   "
          f"max|C - C'| = {dev:.3e}   phi*d = {phi*delta:.6f}, phi'*d' = {phi_m*alpha:.6f}")
worst_dev = max(devs)

# WITNESS: a mirror that does NOT preserve phi*delta. If the paths still coincide, the
# check is not touching the invariant.
bad = []
for alpha, delta, phi in MIRROR:
    phi_bad = min(phi * delta / alpha + 0.05, 1.0)
    bad.append(float(np.max(np.abs(reported(phi, delta, alpha)
                                   - reported(phi_bad, alpha, delta)))) / E0)
check("the root swap with phi' = phi*delta/alpha reproduces the reported path exactly",
      worst_dev < 1e-12,
      witness=lambda: max(bad) < 1e-12)
print(f"  worst normalised deviation {worst_dev:.3e}   "
      f"(witness, phi' perturbed by 0.05: {max(bad):.3e})")

products = [abs(phi * delta - (phi * delta / alpha) * alpha) for alpha, delta, phi in MIRROR]
check("the exchange preserves phi*delta exactly",
      max(products) < 1e-15,
      witness=lambda: max(abs(phi * delta - (phi * delta / alpha + 0.05) * alpha)
                          for alpha, delta, phi in MIRROR) < 1e-15)

# ---------------------------------------------------------------- C3
hr("C3 - what breaks the equivalence: the recognition events, and by how much")

print("  Same mirror pairs, recognition mechanism LIVE (theta = 0.25).")
print("  The trigger reads gap/E, and E is not reported -- so any information that")
print("  breaks the degeneracy arrives through a channel the reported series lacks.\n")
breaks = []
for alpha, delta, phi in MIRROR:
    phi_m = phi * delta / alpha
    r1 = firm(phi, delta, alpha, 0.25).run(PERIODS)
    r2 = firm(phi_m, alpha, delta, 0.25).run(PERIODS)
    n1, n2 = r1["n_crises"], r2["n_crises"]
    breaks.append((n1, n2))
    print(f"  (a={alpha:.3f}, d={delta:.3f}, phi={phi:.2f}): events {n1:3d}   "
          f"mirror: {n2:3d}   {'DISTINGUISHABLE' if n1 != n2 else 'still identical'}")
distinguishable = sum(1 for n1, n2 in breaks if n1 != n2)
print(f"\n  distinguishable by event count in {distinguishable}/{len(breaks)} pairs")

# ---------------------------------------------------------------- C4
hr("C4 - iso-observable pairs: different phi, identical observables")

# Choose (phi1, d1) and solve for d2 giving the same (1-phi)*delta/(alpha-delta) at phi2.
ALPHA = 0.05


def delta_matching(phi_target, ratio, alpha=ALPHA):
    """Solve (1-phi)d/(alpha-d) = ratio for d."""
    return ratio * alpha / (1.0 - phi_target + ratio)


pairs = []
for (phi1, d1), phi2 in [((0.20, 0.020), 0.60), ((0.30, 0.015), 0.75), ((0.10, 0.025), 0.50)]:
    ratio = closed_form_gap_ratio(phi1, d1, ALPHA)
    d2 = delta_matching(phi2, ratio, ALPHA)
    g1, g2 = gap_ratio_terminal(phi1, d1, ALPHA), gap_ratio_terminal(phi2, d2, ALPHA)
    pairs.append(abs(g1 - g2))
    print(f"  phi={phi1:.2f}, delta={d1:.4f}   vs   phi={phi2:.2f}, delta={d2:.4f}"
          f"   ->   gap ratio {g1:.8f} vs {g2:.8f}")
worst_pair = max(pairs)

# WITNESS: hold delta fixed and change phi -- the observable MUST move, or the whole
# construction is vacuous.
held = [abs(gap_ratio_terminal(0.20, 0.020) - gap_ratio_terminal(0.60, 0.020)),
        abs(gap_ratio_terminal(0.30, 0.015) - gap_ratio_terminal(0.75, 0.015))]
check("phi differing by 0.4-0.45 is invisible once delta is chosen to match",
      worst_pair < 1e-3,
      witness=lambda: max(held) < 1e-3)
print(f"  worst mismatch {worst_pair:.2e} (transient, not structure)   "
      f"witness, delta held fixed instead: {max(held):.4f} -- three orders larger")

# ---------------------------------------------------------------- C5
hr("C5 - the cross-class corollary: the observable ranks (1-phi) (*) delta")

TIERS = ["0 PP&E", "1 finite-lived intangible", "2 indefinite-lived intangible", "3 goodwill"]
PHI = np.array([0.80, 0.60, 0.40, 0.20])        # the registered ordering: phi falls
DELTA = np.array([0.030, 0.020, 0.010, 0.002])  # durability rises up the same ladder

print("  Registered design: phi is MONOTONE DECREASING across the four tiers.")
print("  Physical fact: delta is monotone decreasing across the same four tiers.\n")
print(f"  {'tier':<32}{'phi':>7}{'delta':>9}{'(1-phi)d':>12}{'gap ratio':>13}{'events':>9}")
composite, observed = [], []
for name, p, d in zip(TIERS, PHI, DELTA):
    comp = (1.0 - p) * d
    g = gap_ratio_terminal(p, d, ALPHA)
    n = firm(p, d, ALPHA, 0.25).run(PERIODS)["n_crises"]
    composite.append(comp)
    observed.append(g)
    print(f"  {name:<32}{p:>7.2f}{d:>9.3f}{comp:>12.5f}{g:>13.6f}{n:>9d}")

phi_monotone = all(PHI[i] > PHI[i + 1] for i in range(3))
obs_monotone = (all(observed[i] < observed[i + 1] for i in range(3))
                or all(observed[i] > observed[i + 1] for i in range(3)))
print(f"\n  phi monotone across tiers: {phi_monotone}")
print(f"  observable monotone across tiers: {obs_monotone}")

# WITNESS: give the four tiers a COMMON delta. Then the observable must order by phi,
# which is the condition the registered design silently assumed.
common = [gap_ratio_terminal(p, 0.020, ALPHA) for p in PHI]
common_monotone = all(common[i] < common[i + 1] for i in range(3))
check("with delta varying across classes, the observable does NOT order by phi",
      phi_monotone and not obs_monotone,
      witness=lambda: not common_monotone)
print(f"  witness -- same phi ladder at a COMMON delta = 0.020: "
      f"{[round(c, 5) for c in common]}  monotone: {common_monotone}")

order_comp = np.argsort(composite)
order_obs = np.argsort(observed)
check("the observable ordering is the ordering of (1-phi)*delta",
      list(order_comp) == list(order_obs),
      witness=lambda: list(np.argsort(-PHI)) == list(order_obs))
print(f"  ordering by (1-phi)*delta: {list(order_comp)}   "
      f"ordering by observable: {list(order_obs)}   "
      f"ordering by phi alone: {list(np.argsort(-PHI))}")

# ---------------------------------------------------------------- C6
hr("C6 - the goodwill limit: at delta = 0 the parameter is not ill-conditioned, it is absent")

zero_events, zero_gaps = [], []
for p in [0.0, 0.2, 0.5, 0.8, 1.0]:
    r = firm(p, 0.0, ALPHA, 0.25).run(PERIODS)
    zero_events.append(r["n_crises"])
    zero_gaps.append(float(np.abs(r["gap"]).max()))
print(f"  delta = 0, phi in [0, 1]:  events {zero_events}   max|gap| {max(zero_gaps):.2e}")

live_events = [firm(p, 0.020, ALPHA, 0.25).run(PERIODS)["n_crises"]
               for p in [0.0, 0.2, 0.5, 0.8, 1.0]]
print(f"  delta = 0.020, same phi grid: events {live_events}")

check("at delta = 0 there are no recognition events at any phi",
      all(n == 0 for n in zero_events),
      witness=lambda: all(n == 0 for n in live_events))
check("at delta = 0 the gap is identically zero at any phi",
      max(zero_gaps) < 1e-12,
      witness=lambda: max(float(np.abs(firm(p, 0.020, ALPHA, np.inf).run(PERIODS)["gap"]).max())
                          for p in [0.0, 0.5]) < 1e-12)
print("  phi does not appear in the delta = 0 dynamics at all: dE = 0, so phi*dE = 0.")

# ---------------------------------------------------------------- C7
hr("C7 - the model's own lag statistic is not computable from reported data")

r = firm(0.30, 0.020, ALPHA, np.inf).run(PERIODS)
print(f"  recognition_lag(res) at phi=0.30, delta=0.020: {recognition_lag(r)} periods")
print("  It is the cross-correlation lag between dE and dC. dE is the change in PHYSICAL")
print("  value. No filing reports it. The empirical instrument of PRE-001/002 measured a")
print("  different quantity -- onset-of-decline to charge -- and the bridge between the two")
print("  was never written down. That is a SECOND identification gap, upstream of C2.")

conc = variance_concentration(firm(0.0, 0.020, ALPHA, 0.25).run(PERIODS))
print(f"\n  (for the record, unchanged: concentration at phi=0 is {conc:.2f})")

hr("SUMMARY")
summary()
