"""The supply/demand argument, checked rather than asserted."""

import numpy as np
import pytest

from wealth_tensor.excess_demand import Market

RNG = np.random.default_rng(7)
M = RNG.lognormal(3.0, 0.6, 400)
S = 150


def allocations(k=25):
    return [Market(M, S, rng=np.random.default_rng(i)) for i in range(k)]


def test_marginal_pair_is_the_sth_and_s_plus_first_reservation_prices():
    mk = Market(M, S, rng=np.random.default_rng(0))
    desc = np.sort(M)[::-1]
    lo, hi = mk.marginal_pair()
    assert hi == desc[S - 1]      # last agent who can hold a unit
    assert lo == desc[S]          # first agent excluded
    assert lo < hi


def test_clearing_interval_is_invariant_to_allocation():
    """THE central claim: who happens to hold the stock does not move the price."""
    pairs = {tuple(np.round(mk.marginal_pair(), 12)) for mk in allocations()}
    assert len(pairs) == 1


def test_but_the_curves_themselves_are_not_invariant():
    """The complement, and the whole point: the curves are not primitive objects.

    Same c(m), same S, same clearing price -- and yet every allocation yields a different
    demand curve. Supply and demand cannot be independent equations if a change that
    leaves the equilibrium untouched moves both of them.
    """
    grid = np.linspace(M.min(), M.max(), 12)
    curves = {tuple(mk.demand_at(p) for p in grid) for mk in allocations()}
    assert len(curves) == 25


def test_the_twelve_point_grid_returns_the_four_schedules_section_8_reports():
    """Paper IV §8's abandoned approach, asserted rather than remembered.

    §8 reports that §5's identity was first measured on a 12-point grid spanning the full range
    of reservation prices and returned FOUR distinct excess-demand schedules rather than one --
    two grid endpoints x two holding states. Until wealthTensor-86 the manuscript said that four
    was ASSERTED by this module, and it was not: the twelve-point test above counts DEMAND curves
    (25) and never builds the excess-demand set at all. The number is asserted here, so §8's
    figure is checked by the suite rather than carried in a paragraph.
    """
    grid = np.linspace(M.min(), M.max(), 12)
    excess = {tuple(mk.excess_demand(float(p)) for p in grid) for mk in allocations()}
    assert len(excess) == 4


def test_excess_demand_is_identically_invariant_to_the_allocation():
    """The sharper form of the claim, and the one the paper leads with.

    `test_but_the_curves_themselves_are_not_invariant` shows the schedules move and
    `test_clearing_interval_is_invariant_to_allocation` shows the crossing does not. Those
    two together license an *inference* that the schedules are not independent equations.
    The identity is stronger and needs no inference: for any price that is not itself a
    reservation price,

        z(p) = D(p) - S(p) = #{i : m_i > p} - S

    because the holders with m_i > p and the holders with m_i < p partition the S holders.
    The allocation cancels from the difference at EVERY price, not only at the zero. So D
    and S are two decompositions of one function of c(m) and S, and the decomposition
    carries no economic content -- which is exactly why they cannot be perturbed
    independently.

    Grid endpoints are excluded because M.min() and M.max() are themselves data points,
    and the strict inequalities in demand_at/supply_at then disagree about a single agent.
    That is a tie convention, not an economic effect, and a coarse grid that includes the
    endpoints reports it as extra distinct schedules.
    """
    grid = np.linspace(M.min(), M.max(), 401)[1:-1]
    grid = np.array([p for p in grid if np.min(np.abs(M - p)) > 1e-9])
    # Paper IV §5 says "399 interior grid points" and §10 says this command regenerates it.
    # `> 300` let the manuscript's own number go unheld for the life of the paper; the tie
    # filter drops none of the 399, so the exact count is the assertion the sentence needs.
    assert grid.size == 399

    demand = {tuple(mk.demand_at(float(p)) for p in grid) for mk in allocations()}
    supply = {tuple(mk.supply_at(float(p)) for p in grid) for mk in allocations()}
    excess = {tuple(mk.excess_demand(float(p)) for p in grid) for mk in allocations()}

    assert len(demand) == 25          # every allocation gives a different demand curve
    assert len(supply) == 25          # and a different supply curve
    assert len(excess) == 1           # and they all give the SAME difference

    identity = tuple(int(np.sum(M > p)) - S for p in grid)
    assert excess.pop() == identity


def test_excess_demand_crosses_zero_exactly_on_the_marginal_pair():
    for mk in allocations(10):
        lo, hi = mk.marginal_pair()
        assert mk.excess_demand(lo - 1e-9) == 1
        assert mk.excess_demand((lo + hi) / 2) == 0
        assert mk.excess_demand(hi + 1e-9) == -1


def test_marshallian_cross_is_recovered_exactly():
    """Reduction result: the textbook construction is a correct snapshot.

    For any fixed allocation the intersection of D and S lands inside the structural
    clearing interval. The cross is not wrong -- it is incomplete, because it cannot be
    perturbed without moving both curves at once.
    """
    for mk in allocations(10):
        lo, hi = mk.marginal_pair()
        assert lo <= mk.marshallian_cross() <= hi + 1e-9


def test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result():
    """Deliberate limit on the claim.

    Unit demand and no income effects: excess demand is a well-behaved monotone step
    function. Note the reason carefully -- it is NOT that "SMD needs at least two goods
    and this has one", which an earlier version of this docstring said. One traded good
    priced against money is already a two-commodity partial equilibrium. What does the
    work is unit demand plus the absence of income effects, which makes aggregate demand
    a non-increasing step function by construction. This module shows invariance of the
    curves' difference to the allocation; it does NOT show arbitrary shape, and the two
    must not be conflated in the manuscript.
    """
    mk = Market(M, S, rng=np.random.default_rng(3))
    zs = [mk.excess_demand(float(p)) for p in np.linspace(M.min(), M.max(), 500)]
    assert all(a >= b for a, b in zip(zs, zs[1:]))


def test_endowment_effect_reduces_trade_volume():
    """Behaviour enters as a shape transform of c(m), and makes a falsifiable prediction.

    Raising holders' reservation prices (loss aversion) monotonically reduces the number
    of units that change hands -- which is the documented experimental finding, not a
    free parameter tuned to produce it.
    """
    mk = Market(M, S, rng=np.random.default_rng(1))
    vols = [mk.with_endowment_effect(l).volume() for l in [1.0, 1.05, 1.15, 1.3, 1.6, 2.0]]
    assert all(a >= b for a, b in zip(vols, vols[1:]))
    assert vols[0] > vols[-1]


def test_loss_aversion_below_one_is_rejected():
    mk = Market(M, S, rng=np.random.default_rng(1))
    with pytest.raises(ValueError, match="loss aversion"):
        mk.with_endowment_effect(0.9)


def test_allocation_must_match_stock():
    with pytest.raises(ValueError, match="allocation does not match"):
        Market(M, S, holders=np.zeros(M.size, dtype=bool))


def test_the_monotone_sweep_endpoints_and_single_crossing_are_what_section_5_reports():
    """Paper IV §5's three unheld numbers, asserted here (wealthTensor-100, IV-10).

    §5 reports the 500-point sweep as "zero monotonicity violations ... running from +249 to
    -150 with one sign change".  `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`
    asserts only the monotonicity; the endpoints and the single crossing were printed by
    `scripts/wt018_report.py` -- which Paper IV named nowhere until wealthTensor-100 -- and
    asserted by nothing.  Naming the script in §10 makes them reproducible; this test holds them.

    AND THE CONTROL IS THE INTERESTING HALF, because the first version of it was WRONG and the
    module said so.  That version asserted the endpoints are (N - 1) - S and -S by derivation,
    and predicted (299, -100) at S = 100.  The module returned (300, -100).  The 500-point grid
    is CLOSED -- both endpoints are data points, `M.min()` and `M.max()` -- and those are exactly
    the points `test_excess_demand_is_identically_invariant_to_the_allocation` excludes, because
    the strict inequalities in demand_at/supply_at disagree there about a single agent whose
    holding status varies by allocation.  That is §8's tie convention, met in §5.

    So the endpoint reading is NOT guaranteed to equal §5's identity #{i : m_i > p} - S.  At the
    paper's configuration (S = 150) it does, at both ends, and that agreement is a MEASURED fact
    -- which is what the negative control below establishes by finding a stock where it fails.
    """
    mk = Market(M, S, rng=np.random.default_rng(3))
    grid = np.linspace(M.min(), M.max(), 500)
    zs = [mk.excess_demand(float(p)) for p in grid]

    assert len(zs) == 500
    assert sum(1 for a, b in zip(zs, zs[1:]) if a < b) == 0                 # zero violations
    assert (zs[0], zs[-1]) == (249, -150)                                   # the endpoints §5 prints
    assert sum(1 for a, b in zip(zs, zs[1:]) if (a > 0) != (b > 0)) == 1    # one sign change

    # At THIS configuration the closed-grid endpoints agree with §5's identity at both ends.
    identity = (int(np.sum(M > grid[0])) - S, int(np.sum(M > grid[-1])) - S)
    assert (zs[0], zs[-1]) == identity

    # NEGATIVE CONTROL: the agreement above is a measurement, not an algebraic necessity. At
    # S = 180, the same population and the same closed grid, the lower endpoint reads one above
    # the identity -- the tie §8 describes, resolving the other way.
    other = Market(M, 180, rng=np.random.default_rng(3))
    z2 = [other.excess_demand(float(p)) for p in grid]
    id2 = (int(np.sum(M > grid[0])) - 180, int(np.sum(M > grid[-1])) - 180)
    assert (z2[0], z2[-1]) == (220, -179)
    assert (z2[0], z2[-1]) != id2

    # And the interior grid, where §5's identity IS asserted, is untouched by the tie.
    interior = grid[1:-1]
    zi = [mk.excess_demand(float(p)) for p in interior]
    assert all(z == int(np.sum(M > p)) - S for z, p in zip(zi, interior))
