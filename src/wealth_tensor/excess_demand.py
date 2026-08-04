"""Supply and demand as two readings of a single distribution of indifference points.

The manuscript's claim is that agents are not intrinsically buyers or sellers: each holds
a reservation price and buys below it or sells above it. This module makes that claim
executable, and separates it carefully from two neighbouring claims it is often confused
with.

Setup (matching the manuscript's c(m) formulation)
--------------------------------------------------
N agents, each with a reservation price m_i drawn from a distribution c(m).
S indivisible units of a commodity, at most one per agent.
An allocation records which agents currently hold a unit.

At price p:
    an agent holding a unit sells if   m_i < p
    an agent holding nothing buys if   m_i > p

so demand and supply are not properties of *people*, they are properties of the pair
(reservation price, current holding) evaluated at p.

What this module demonstrates
-----------------------------
1. The market-clearing price interval is exactly the manuscript's **marginal pair** --
   the S-th and (S+1)-th highest reservation prices -- and it is a property of c(m) and
   S alone.

2. That interval is **invariant to the allocation**, while the supply and demand curves
   themselves are **not**. Two economies with identical c(m) and identical S but different
   allocations produce visibly different curves that cross in exactly the same place.
   This is the precise sense in which the curves are not independent equations: they are
   two readings of one distribution, and only their difference is structural.

3. **Reduction to the Marshallian cross.** For any *fixed* allocation the textbook
   construction is recovered exactly -- the intersection of D(p) and S(p) is the correct
   clearing interval. The cross is therefore a valid *snapshot*. What it cannot do is
   comparative statics that move the allocation, because both curves shift together and
   cannot be perturbed independently. Descriptive, not predictive -- stated as a theorem
   rather than a complaint.

What this module does NOT demonstrate
-------------------------------------
It does **not** produce Sonnenschein-Mantel-Debreu pathology. With one good and unit
demand, aggregate excess demand here is a monotone decreasing step function: well behaved,
single crossing. SMD's arbitrary-shape result requires at least two goods and income
effects. Conflating the two claims would be a real error, so the monotonicity is asserted
in the tests deliberately, as a limit on what this construction shows.
"""

from __future__ import annotations

import numpy as np


class Market:
    """A population of reservation prices, S units, and an allocation."""

    def __init__(self, reservation_prices, stock: int, holders=None, rng=None):
        self.m = np.asarray(reservation_prices, dtype=float)
        self.n = self.m.size
        if not 0 < stock < self.n:
            raise ValueError("stock must be strictly between 0 and the number of agents")
        self.stock = int(stock)
        if holders is None:
            rng = np.random.default_rng() if rng is None else rng
            holders = np.zeros(self.n, dtype=bool)
            holders[rng.choice(self.n, size=self.stock, replace=False)] = True
        holders = np.asarray(holders, dtype=bool)
        if holders.sum() != self.stock:
            raise ValueError("allocation does not match the stock")
        self.holders = holders

    # --- the two "curves", each a reading of the same m, differing only by allocation ---

    def demand_at(self, p: float) -> int:
        """Non-holders whose reservation price exceeds p: they would buy."""
        return int(np.sum(~self.holders & (self.m > p)))

    def supply_at(self, p: float) -> int:
        """Holders whose reservation price falls below p: they would sell."""
        return int(np.sum(self.holders & (self.m < p)))

    def excess_demand(self, p: float) -> int:
        return self.demand_at(p) - self.supply_at(p)

    # --- structural quantities: functions of c(m) and S only ---

    def marginal_pair(self):
        """(first excluded, last included) -- the manuscript's marginal pair.

        Sorting reservation prices descending, the S-th highest is the last agent who can
        hold a unit and the (S+1)-th is the first excluded. Any price strictly between
        them clears the market, for every allocation.
        """
        desc = np.sort(self.m)[::-1]
        return float(desc[self.stock]), float(desc[self.stock - 1])

    def clearing_price(self) -> float:
        lo, hi = self.marginal_pair()
        return (lo + hi) / 2.0

    def marshallian_cross(self, grid=None) -> float:
        """Lowest price on a grid at which excess demand is non-positive.

        This is the textbook construction: read D(p), read S(p), find where they cross.
        It is included so the tests can show it recovers the structural answer, rather
        than being told that it does.
        """
        if grid is None:
            lo, hi = float(self.m.min()), float(self.m.max())
            grid = np.linspace(lo, hi, 4001)
        for p in grid:
            if self.excess_demand(float(p)) <= 0:
                return float(p)
        return float(grid[-1])

    def volume(self) -> int:
        """Units changing hands on the way to the efficient allocation."""
        p = self.clearing_price()
        return self.demand_at(p)

    # --- behavioural agents as shape transforms of c(m), never as free coefficients ---

    def with_endowment_effect(self, loss_aversion: float) -> "Market":
        """Holders value what they hold more highly (Kahneman-Knetsch-Thaler).

        This is the correct way to admit behavioural agents: not a coefficient bolted onto
        the model to absorb objections, but a *stated transform of the reservation-price
        distribution*, which remains measurable and therefore falsifiable. Prospect theory
        is a claim about how reservation prices move with a reference point; that is a
        property of c(m).
        """
        if loss_aversion < 1.0:
            raise ValueError("loss aversion coefficient must be >= 1")
        m2 = self.m.copy()
        m2[self.holders] *= loss_aversion
        return Market(m2, self.stock, holders=self.holders)

    def with_dispersion(self, sigma: float, rng=None) -> "Market":
        """Noisy indifference points -- imperfect introspection about one's own price."""
        rng = np.random.default_rng() if rng is None else rng
        return Market(self.m + rng.normal(0.0, sigma, self.n), self.stock,
                      holders=self.holders)
