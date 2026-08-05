"""Redistribution classified by structural parameters, not by institutional origin.

The manuscript's redistribution passage was reframed in S1 from advocacy into a positive
statement about a model class (WT-029). This module supplies the result that reframe
promised: within a multiplicative-additive wealth process, *which regions of the parameter
space bound the Gini below unity* -- a question the models answer and nobody can call
policy preference.

The process
-----------
N agents. Each period every agent's wealth is multiplied by an idiosyncratic growth factor
and receives a common additive wage::

    w_i(t+1) = w_i(t) * (1 + eta_i(t)) + a,      eta_i ~ N(mu, sigma)

The multiplicative term is the engine of condensation: the variance of log-wealth grows
without bound, so with mu > 0 the additive wage becomes negligible and the Gini approaches
unity. That is not a pathology of the model, it is the model's whole content -- unopposed
multiplicative growth condenses, and every empirical wealth distribution that does not
condense is being opposed by something.

The four structural parameters
------------------------------
A levy is fully described, for these purposes, by four numbers -- and *not* by its name,
its era, or the tradition that produced it:

``base``          what is assessed: the ``stock`` held, or the ``flow`` received
``rate``          the fraction of the liable amount taken
``periodicity``   how many periods elapse between assessments
``threshold``     the exempt amount, in multiples of the mean of the base

Everything collected in a period is redistributed per capita in the same period, so the
levy is a pure transfer: aggregate wealth is untouched and only its dispersion changes.

Realisation, and why it is the crux
-----------------------------------
``realization`` (rho) is the share of a period's capital gain that is *recognised* as flow
and therefore enters a flow levy's base. It is not a fudge factor and not a free parameter
absorbing an objection (WT-002, WT-016 forbid those): it is a stated structural property of
every real tax system, which taxes gains when they are realised rather than when they
accrue. rho = 1 is a mark-to-market levy on accruals; rho = 0 is the pure rentier who
never sells.

This parameter is where the base's decisiveness actually lives, and the result is sharper
than the claim it replaces -- see WT-033.

What is measured
----------------
``gini``          dispersion of the wealth vector each period
``reallocation``  kappa, the share of aggregate wealth moved per assessment. This is the
                  levy's compressive budget, and it is what the base caps.

A note on what this does and does not license
---------------------------------------------
This is a statement about a model class, not about any historical institution. No causal
field evidence is claimed, required, or available. Zakat is analytically interesting here
for exactly one reason -- it is assessed on stock above a threshold rather than on income
received -- and that places it in a region of the parameter space, which is a coordinate,
not an endorsement.
"""

from __future__ import annotations

import numpy as np

BASES = ("stock", "flow")


def gini(w) -> float:
    """Gini coefficient of a non-negative wealth vector.

    Uses the sorted-rank form ``2*sum(i*w_i)/(n*sum(w)) - (n+1)/n``, which is exact rather
    than a Lorenz-curve approximation. Returns nan for a non-positive total.
    """
    w = np.sort(np.asarray(w, dtype=float))
    n = w.size
    total = w.sum()
    if n == 0 or total <= 0:
        return float("nan")
    idx = np.arange(1, n + 1)
    return float(2.0 * (idx * w).sum() / (n * total) - (n + 1.0) / n)


class RedistributiveEconomy:
    """A multiplicative-additive wealth process with one parameterised levy."""

    def __init__(self, n_agents=800, initial_wealth=1.0, growth_mean=0.05,
                 growth_sd=0.20, wage=0.05, base=None, rate=0.0, periodicity=1,
                 threshold=0.0, realization=1.0, seed=0):
        if base is not None and base not in BASES:
            raise ValueError(f"base must be one of {BASES} or None")
        if not 0.0 <= rate <= 1.0:
            raise ValueError("rate must lie in [0, 1]")
        if int(periodicity) < 1:
            raise ValueError("periodicity must be a positive whole number of periods")
        if threshold < 0.0:
            raise ValueError("threshold must be non-negative")
        if not 0.0 <= realization <= 1.0:
            raise ValueError("realization must lie in [0, 1]")
        self.n = int(n_agents)
        self.w0 = float(initial_wealth)
        self.mu = float(growth_mean)
        self.sigma = float(growth_sd)
        self.wage = float(wage)
        self.base = base
        self.rate = float(rate)
        self.periodicity = int(periodicity)
        self.threshold = float(threshold)
        self.rho = float(realization)
        self.seed = seed

    @property
    def levies(self) -> bool:
        """True when this economy actually moves anything."""
        return self.base is not None and self.rate > 0.0

    def run(self, periods=600) -> dict:
        rng = np.random.default_rng(self.seed)
        w = np.full(self.n, self.w0, dtype=float)
        recognised_flow = np.zeros(self.n)          # accrued since the last assessment
        g = np.empty(periods)
        kappas: list[float] = []
        transfer_error = 0.0        # the levy must never create or destroy wealth

        for t in range(1, periods + 1):
            eta = rng.normal(self.mu, self.sigma, self.n)
            gain = w * eta
            # Wealth cannot go negative. With sigma << 1 this clamp is essentially never
            # active; it exists so an extreme parameter choice degrades rather than lies.
            w = np.maximum(w + gain + self.wage, 0.0)
            recognised_flow += self.rho * gain + self.wage

            if self.levies and t % self.periodicity == 0:
                assessed = w if self.base == "stock" else np.maximum(recognised_flow, 0.0)
                liable = np.maximum(0.0, assessed - self.threshold * assessed.mean())
                levy = np.minimum(self.rate * liable, w)   # nobody pays more than they hold
                pot = float(levy.sum())
                total = float(w.sum())
                kappas.append(pot / total if total > 0 else 0.0)
                w = w - levy + pot / self.n                # pure transfer, per capita
                recognised_flow[:] = 0.0
                if total > 0:
                    transfer_error = max(transfer_error,
                                         abs(float(w.sum()) - total) / total)

            g[t - 1] = gini(w)

        return {"gini": g, "wealth": w, "reallocation": np.array(kappas),
                "kappa": float(np.mean(kappas)) if kappas else 0.0,
                "assessments": len(kappas), "transfer_error": transfer_error}


def stationary_gini(res: dict, tail=0.25) -> float:
    """Gini averaged over the final `tail` share of the path.

    A point reading is a poor estimator here: the stationary wealth distribution has a
    heavy tail, so the Gini of a single period fluctuates visibly even at N in the
    thousands. Averaging over a window is the honest summary and is what every comparison
    in the test suite uses.
    """
    g = res["gini"]
    k = max(1, int(round(g.size * tail)))
    return float(np.mean(g[-k:]))


def top_share(res: dict, fraction=0.10) -> float:
    """Share of aggregate wealth held by the richest `fraction` of agents."""
    w = np.sort(np.asarray(res["wealth"], dtype=float))[::-1]
    total = w.sum()
    if total <= 0:
        return float("nan")
    k = max(1, int(round(fraction * w.size)))
    return float(w[:k].sum() / total)


def is_bounded(res: dict, tol=0.02, top_limit=0.90) -> bool:
    """True when the process is neither still condensing nor already condensed.

    Two conditions, and the second one is load-bearing:

    1. The Gini has stopped climbing -- the mean over the last quarter of the path exceeds
       the mean over the previous quarter by less than `tol`.
    2. The top decile does not hold essentially all the wealth.

    Condition 1 alone is **not sufficient**, and assuming it was is a trap this module fell
    into on its first draft. The Gini is capped at (N-1)/N, so a fully condensed economy
    also stops climbing -- it has simply run out of headroom. At N = 800 and 600 periods the
    unopposed process reads Gini 0.977 and *flat*, which a drift test scores as bounded and
    a top-share test scores correctly: its top decile holds 0.988 of everything. Boundedness
    has to be tested on the thing being claimed, which is the absence of condensation, not
    on a summary statistic that saturates. See WT-034.
    """
    g = res["gini"]
    k = max(1, g.size // 4)
    late, earlier = float(np.mean(g[-k:])), float(np.mean(g[-2 * k:-k]))
    return bool(late - earlier < tol and top_share(res) < top_limit)


def reachable_frontier(base, rates=(0.01, 0.02, 0.05, 0.1, 0.25, 0.5, 1.0),
                       periods=600, **kw) -> float:
    """Lowest stationary Gini this base can reach, minimising over rate.

    This is the quantity that makes "the base is decisive" a testable statement rather than
    a slogan. The rate moves an economy *within* a base's reachable region; it cannot move
    it *between* regions. Compare frontiers, not point estimates.
    """
    return min(stationary_gini(RedistributiveEconomy(base=base, rate=r, **kw).run(periods))
               for r in rates)


def sweep(bases=BASES, rates=(0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0),
          periodicities=(1,), thresholds=(0.0,), realizations=(1.0,),
          periods=600, **kw) -> list[dict]:
    """The WT-030 map: one row per point in base x rate x periodicity x threshold x rho.

    Returns plain dicts rather than a dataframe so the module keeps a single dependency.
    """
    rows = []
    for base in bases:
        for rate in rates:
            for p in periodicities:
                for thr in thresholds:
                    for rho in realizations:
                        econ = RedistributiveEconomy(base=base, rate=rate, periodicity=p,
                                                     threshold=thr, realization=rho, **kw)
                        res = econ.run(periods)
                        rows.append({"base": base, "rate": rate, "periodicity": p,
                                     "threshold": thr, "realization": rho,
                                     "gini": stationary_gini(res),
                                     "kappa": res["kappa"],
                                     "top_decile": top_share(res),
                                     "bounded": is_bounded(res)})
    return rows
