"""wealthTensor-81 · Paper IV §8's twelve-point tie convention, held by derivation.

WHY THIS EXISTS. Paper IV §10 says `python3 -m pytest tests/test_excess_demand.py -q`
regenerates "the twelve-point tie convention §8 records" — §8's claim that a 12-point grid
spanning the full range returns **four** distinct excess-demand schedules rather than one.
No test in this module measured it. `test_but_the_curves_themselves_are_not_invariant`
builds the same 12-point grid and counts DEMAND schedules (25), which is a different
number about a different object. So §10's promise was false for the life of the paper,
and the repair is to make the promise TRUE rather than to withdraw it.

The four is not an economic effect. Both grid endpoints coincide with data points; the
strict inequalities in `demand_at`/`supply_at` then disagree about a single agent whose
holding status varies by allocation; two endpoints x two holding states = four. §8 records
it as a near-miss — reporting it as a partial invariance would have published the central
claim one full step weaker than it is true.
"""
import numpy as np

from wealth_tensor.excess_demand import Market

RNG = np.random.default_rng(7)
M = RNG.lognormal(3.0, 0.6, 400)
S = 150


def _allocations(k=25):
    return [Market(M, S, rng=np.random.default_rng(i)) for i in range(k)]


def test_the_twelve_point_grid_returns_four_distinct_excess_demand_schedules():
    """§8's number, asserted where §10 promises a reader can regenerate it."""
    grid = np.linspace(M.min(), M.max(), 12)
    excess = {tuple(mk.excess_demand(float(p)) for p in grid) for mk in _allocations()}
    assert len(excess) == 4


def test_the_four_is_a_tie_convention_and_not_an_economic_effect():
    """The witness for §8's explanation: exclude the two endpoints and the four collapses to
    one. If this ever returns anything but 1, §8's account of WHY it was four is wrong and
    the sentence has to change, not the number."""
    grid = np.linspace(M.min(), M.max(), 12)[1:-1]
    excess = {tuple(mk.excess_demand(float(p)) for p in grid) for mk in _allocations()}
    assert len(excess) == 1


def test_the_twelve_point_grid_still_gives_twenty_five_demand_schedules():
    """Guards against the lazy repair of repointing the neighbouring test at excess demand:
    the 25 and the 4 are both real and are about different objects."""
    grid = np.linspace(M.min(), M.max(), 12)
    demand = {tuple(mk.demand_at(float(p)) for p in grid) for mk in _allocations()}
    assert len(demand) == 25
