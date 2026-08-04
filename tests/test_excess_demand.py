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

    One good, unit demand, no income effects: excess demand is a well-behaved monotone
    step function. Sonnenschein-Mantel-Debreu pathology needs at least two goods. This
    module shows non-independence of the curves; it does NOT show arbitrary shape, and
    the two must not be conflated in the manuscript.
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
