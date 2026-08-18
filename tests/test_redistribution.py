"""Which regions of the redistribution parameter space bound the Gini. Checked, not argued.

The claim under test (WT-030) was that **the base is decisive** -- a levy on stock opposes
the multiplicative term, a levy on flow does not, regardless of rate. It reproduces, but not
in the form it was stated. `test_a_flow_levy_is_powerless_when_gains_are_unrealised` and
`test_the_base_sets_a_ceiling_that_the_rate_cannot_cross` are the two that carry the
refined result; the rest fence it in.
"""

import numpy as np
import pytest

from wealth_tensor.redistribution import (BASES, RedistributiveEconomy, gini, is_bounded,
                                          reachable_frontier, stationary_gini, sweep,
                                          top_share)

T = 600


def econ(**kw):
    return RedistributiveEconomy(**kw).run(T)


# --------------------------------------------------------------------------- the measure

def test_gini_matches_hand_computed_values():
    """Closed-form anchors, per L10: no model result is trusted without one."""
    assert gini(np.ones(50)) == pytest.approx(0.0, abs=1e-12)
    # A single holder among n: (n-1)/n, the finite-population maximum.
    for n in (4, 10, 800):
        w = np.zeros(n)
        w[0] = 1.0
        assert gini(w) == pytest.approx((n - 1) / n, abs=1e-12)
    # Uniform ramp 1..n: (n-1)/(3n).
    for n in (4, 9, 100):
        assert gini(np.arange(1, n + 1)) == pytest.approx((n - 1) / (3 * n), abs=1e-12)
    assert np.isnan(gini(np.zeros(10)))


def test_top_share_matches_hand_computed_values():
    w = np.array([4.0, 3.0, 2.0, 1.0])
    assert top_share({"wealth": w}, 0.25) == pytest.approx(0.4)
    assert top_share({"wealth": w}, 0.50) == pytest.approx(0.7)
    assert top_share({"wealth": w}, 1.00) == pytest.approx(1.0)


# ------------------------------------------------------------------------- the baseline

def test_unopposed_multiplicative_growth_condenses():
    """No levy: the top decile ends up holding essentially everything.

    This is the phenomenon the whole module exists to oppose. Note it is asserted on the
    top share and not on the Gini -- see the next test for why.
    """
    res = econ()
    assert top_share(res) > 0.95
    assert stationary_gini(res) > 0.95
    assert not is_bounded(res)


def test_a_flat_gini_does_not_mean_a_bounded_one():
    """The trap in WT-034, kept as a standing guard rather than a comment.

    The unopposed process's Gini stops rising -- not because it reached a stationary
    distribution but because it hit the (N-1)/N ceiling. Any future refactor that reduces
    `is_bounded` to a drift test alone will fail here rather than quietly scoring
    condensation as success.
    """
    res = econ()
    g = res["gini"]
    k = g.size // 4
    drift = float(np.mean(g[-k:]) - np.mean(g[-2 * k:-k]))
    assert drift < 0.02                     # flat by a drift test...
    assert top_share(res) > 0.95            # ...and completely condensed
    assert not is_bounded(res)


def test_zero_rate_is_bit_identical_to_no_levy():
    """A levy that takes nothing must perturb nothing, including the random stream."""
    a = RedistributiveEconomy(base="stock", rate=0.0, seed=3).run(200)
    b = RedistributiveEconomy(base=None, seed=3).run(200)
    assert np.array_equal(a["gini"], b["gini"])
    assert np.array_equal(a["wealth"], b["wealth"])


def test_the_levy_is_a_pure_transfer():
    """Structural invariant: no assessment ever creates or destroys aggregate wealth.

    Every comparison in this file is between economies that differ only in dispersion, so
    if this ever failed, a "levy lowers the Gini" result could be a growth artefact instead.
    Checked inside the loop rather than across runs, because two seeded paths diverge the
    moment the first levy lands and their totals are no longer comparable.
    """
    for base, rate, thr in (("stock", 0.25, 0.0), ("flow", 1.0, 2.0), ("stock", 0.025, 5.0)):
        res = RedistributiveEconomy(base=base, rate=rate, threshold=thr, seed=7).run(200)
        assert res["assessments"] == 200
        assert res["transfer_error"] < 1e-12


# ------------------------------------------------------------------------- the base result

def test_a_stock_levy_bounds_the_gini_at_every_positive_rate():
    """WT-029's positive claim: continuous redistribution prevents terminal condensation."""
    rates = [0.005, 0.01, 0.025, 0.05, 0.10, 0.25]
    gs = [stationary_gini(econ(base="stock", rate=r)) for r in rates]
    assert all(is_bounded(econ(base="stock", rate=r)) for r in rates)
    assert all(a >= b for a, b in zip(gs, gs[1:]))      # monotone in rate
    assert gs[0] < 0.90                                  # even the weakest levy bites


def test_a_flow_levy_is_weaker_than_a_stock_levy_at_the_same_rate():
    """Matched on rate, the two bases are not close -- roughly an order of magnitude apart."""
    for r in (0.01, 0.025, 0.05, 0.10, 0.25):
        assert (stationary_gini(econ(base="flow", rate=r))
                > stationary_gini(econ(base="stock", rate=r)) + 0.15)


def test_a_flow_levy_is_powerless_when_gains_are_unrealised():
    """THE HEADLINE. A 100% flow levy changes nothing at all when nothing is realised.

    This is the surviving form of "regardless of rate". The multiplicative term operates on
    the stock; if the base cannot see accruals, the maximum possible rate applied to the
    remainder is indistinguishable from no levy whatsoever -- here the wage, which is
    identical for every agent and therefore carries no dispersion to redistribute.
    """
    unrealised = econ(base="flow", rate=1.0, realization=0.0)
    nothing = econ()
    # wealthTensor-76. §3.2 claims the two paths agree AGENT BY AGENT and calls the identity
    # structural -- "stronger than calling it a near-match". Until now the only committed
    # check WAS a near-match: abs=0.01 on one summary statistic. The manuscript's strongest
    # sentence in §3.2 was pinned by nothing able to see what it claims. GUARD HONESTY --
    # this line passes at rho = 0.00 and fails at rho = 0.10, 0.25 and 1.00, both verified.
    assert np.array_equal(unrealised["wealth"], nothing["wealth"])
    assert stationary_gini(unrealised) == pytest.approx(stationary_gini(nothing), abs=0.01)
    assert top_share(unrealised) > 0.95
    assert not is_bounded(unrealised)


def test_flow_compression_scales_with_the_realised_share():
    """rho interpolates continuously between "a weak stock levy" and "nothing"."""
    gs = [stationary_gini(econ(base="flow", rate=1.0, realization=rho))
          for rho in (1.0, 0.75, 0.5, 0.25, 0.1, 0.0)]
    assert all(a <= b for a, b in zip(gs, gs[1:]))
    assert gs[0] < 0.20 and gs[-1] > 0.95


def test_the_base_sets_a_ceiling_that_the_rate_cannot_cross():
    """The refined WT-030: the rate moves you *within* a base's region, never *between*.

    Minimising over the whole admissible rate range, a stock levy reaches equality and a
    fully-realised flow levy cannot get below roughly the Gini a stock levy reaches at a
    quarter rate. With nothing realised, the flow frontier is the unopposed process itself.
    """
    stock = reachable_frontier("stock")
    flow_full = reachable_frontier("flow")
    flow_none = reachable_frontier("flow", realization=0.0)
    assert stock < 0.02
    assert 0.05 < flow_full < 0.25
    assert flow_none > 0.95
    assert stock < flow_full < flow_none


def test_reallocation_intensity_is_what_the_base_caps():
    """kappa -- the share of aggregate wealth moved per assessment -- is the levy's BUDGET.

    NOT its mechanism, and this docstring said otherwise until `-65`. DECISION-001 prices
    option A as "demote kappa from mechanism to budget in FIVE places" and all five are in
    paper-II.md; this file was the sixth. Nothing asserts a docstring, so the retraction in
    the manuscript would have left the test suite still making the claim -- the
    abstract-versus-body defect one file out. What refutes it is the paper's own table: two
    levies matched at kappa ~ 0.10 compress to Gini 0.222 and 0.125, and a threshold at 0.25x
    the mean removes a quarter of kappa at no measurable cost. kappa is necessary, not
    sufficient. The assertions below were always budget facts; only the prose overreached.

    For a stock base kappa is the rate itself -- exactly, by construction. For a flow base
    it is the rate times the *gross positive* growth rate, because a levy cannot rebate a
    loss: an agent whose wealth fell contributes zero rather than a negative. So the closed
    form is not mu but the mean of the positive part of the growth shock,

        E[eta+] = mu * Phi(mu/sigma) + sigma * phi(mu/sigma)

    which for mu = 0.05, sigma = 0.20 is 0.1073 -- twice mu, and still an order of magnitude
    below what a stock levy reaches. Non-deductibility of losses works *in favour* of the
    flow base here, and it is still not close. That gap, not the rate, is what the base caps.
    """
    from math import erf, exp, pi, sqrt

    for r in (0.05, 0.25, 1.0):
        assert econ(base="stock", rate=r)["kappa"] == pytest.approx(r, rel=1e-9)

    mu, sigma = 0.05, 0.20
    z = mu / sigma
    Phi = 0.5 * (1.0 + erf(z / sqrt(2.0)))
    phi = exp(-0.5 * z * z) / sqrt(2.0 * pi)
    ceiling = mu * Phi + sigma * phi                    # 0.10734...
    assert ceiling == pytest.approx(0.10734, abs=1e-4)

    flow_max = econ(base="flow", rate=1.0)["kappa"]
    assert flow_max == pytest.approx(ceiling, rel=0.10)
    assert econ(base="flow", rate=1.0, realization=0.0)["kappa"] < 0.01


# ----------------------------------------------------------- the second-order parameters

def test_threshold_monotonically_weakens_compression():
    """Exempting more of the base moves less of it. Smooth, with no cliff."""
    gs = [stationary_gini(econ(base="stock", rate=0.025, threshold=t))
          for t in (0.0, 0.5, 1.0, 2.0, 5.0, 20.0)]
    assert all(a <= b for a, b in zip(gs, gs[1:]))
    assert gs[-1] - gs[0] > 0.2
    assert gs[-1] < 0.95        # even a levy on the top sliver alone still opposes


def test_periodicity_is_second_order_at_a_matched_average_rate():
    """Levying rate*P every P periods is close to levying rate every period. Lumpier is
    slightly stronger up to an INTERIOR MINIMUM near P = 30, and weaker after it -- so what
    this test pins is the SHAPE of the sweep and its small total spread, not monotonicity.

    wealthTensor-74. The previous version swept p in (1, 2, 4, 10, 20) and asserted
    monotonicity outright. The sweep the manuscript's own regeneration command prints
    (`scripts/wt030_report.py`) runs to P = 50, where the Gini returns ABOVE its P = 20
    value; the assertion could not see that because its subject stopped where its claim
    stopped. WT-092: what is the widest object this check's words claim, and what is the
    narrowest thing it actually touches? Verified horizon-stable at T = 600 and T = 1200.

    Worth stating precisely: an annual 2.5% assessment is not a watered-down version of a
    continuous one. Periodicity cannot rescue or ruin a base -- it is a modifier on the
    effective rate, which is what makes base and rate the two structural coordinates and
    these two the trim.
    """
    ps = (1, 2, 4, 10, 20, 30, 50)
    gs = [stationary_gini(econ(base="stock", rate=min(1.0, 0.02 * p), periodicity=p))
          for p in ps]
    assert all(a >= b - 1e-9 for a, b in zip(gs[:5], gs[1:5]))  # monotone THROUGH P = 20
    assert gs[ps.index(30)] < gs[ps.index(20)]                  # the minimum is interior
    assert gs[ps.index(50)] > gs[ps.index(20)]                  # and the effect turns back
    assert max(gs) - min(gs) < 0.25                             # the whole sweep is trim


def test_the_result_is_not_a_finite_size_artifact():
    """Stationary Gini is stable in N; the condensed one is pinned to the ceiling and rises."""
    bounded = [stationary_gini(RedistributiveEconomy(base="stock", rate=0.025,
                                                     n_agents=n).run(400))
               for n in (250, 500, 1000, 2000)]
    assert max(bounded) - min(bounded) < 0.08
    condensed = [top_share(RedistributiveEconomy(n_agents=n).run(400))
                 for n in (250, 500, 1000, 2000)]
    assert min(condensed) > 0.9


def test_the_result_is_not_a_lucky_seed():
    """wealthTensor-77, II-34. Paper II S5.5 offers THIS test as the mitigation for "one seed
    per reported figure" -- and every reported figure is at T = 1200 while econ() runs at
    T = 600. S3.4 says in the paper's own words that the top share "is also horizon-stable
    where the Gini is not", and the band below is on the Gini, so a band checked only at half
    the reported horizon did not reach the numbers it was offered for. Both horizons now.
    Measured before asserted: at T = 1200 the two configurations read 0.4318-0.4451 and
    0.3867-0.3957, inside the bands the T = 600 version already used.
    """
    for base, rate, lo, hi in (("stock", 0.025, 0.35, 0.55), ("flow", 0.25, 0.30, 0.50)):
        for horizon in (T, 1200):
            gs = [stationary_gini(RedistributiveEconomy(base=base, rate=rate, seed=s).run(horizon))
                  for s in range(5)]
            assert all(lo < g < hi for g in gs), f"{base} r={rate} T={horizon}: {gs}"


# ------------------------------------------------------------------------------ plumbing

def test_sweep_maps_the_space_and_agrees_with_the_point_results():
    rows = sweep(rates=(0.025, 0.25), realizations=(1.0, 0.0), periods=400)
    assert len(rows) == len(BASES) * 2 * 2
    assert {r["base"] for r in rows} == set(BASES)
    for r in rows:
        assert 0.0 <= r["kappa"] <= 1.0
        if r["base"] == "flow" and r["realization"] == 0.0:
            assert not r["bounded"]
        if r["base"] == "stock":
            assert r["bounded"]


def test_parameter_validation():
    with pytest.raises(ValueError, match="base"):
        RedistributiveEconomy(base="income")
    with pytest.raises(ValueError, match="rate"):
        RedistributiveEconomy(base="stock", rate=1.5)
    with pytest.raises(ValueError, match="periodicity"):
        RedistributiveEconomy(periodicity=0)
    with pytest.raises(ValueError, match="threshold"):
        RedistributiveEconomy(threshold=-1.0)
    with pytest.raises(ValueError, match="realization"):
        RedistributiveEconomy(realization=1.5)
