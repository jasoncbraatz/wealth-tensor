"""WT-089's estimators, protected independently of a data run.

`wt089` proves its own helpers at run time through `severity.check`, which is
stronger than a unit test in one way -- the witness has to make the guard go red --
and weaker in another: it only runs when somebody runs the instrument against the
sample. These pin the same properties in CI, where they cost nothing.
"""

import math
import pathlib
import random
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

from wt089_recognition_and_offdiagonal import (  # noqa: E402
    annualise, co_stats, fit_dweibull, fit_q_given_k, fq_tiers, geom_mle,
    inject_cooccurrence, marginals, null_draw, regime, two_sided_p)


def _synth(alpha, n=4000, cap=20, seed=11):
    rng = random.Random(seed)
    lags, cens = [], []
    for _ in range(n):
        t = 0
        while rng.random() > alpha and t < cap:
            t += 1
        lags.append(t)
        cens.append(t >= cap)
    return lags, cens


@pytest.mark.parametrize("alpha", [0.05, 0.12, 0.20, 0.40])
def test_geometric_mle_recovers_the_rate_it_was_not_told(alpha):
    lags, cens = _synth(alpha)
    assert abs(geom_mle(lags, cens)[0] - alpha) < 0.02


def test_censored_observations_contribute_exposure():
    """Dropping a censored event's exposure raises the estimate. The whole point of
    the censored form is that a long-running gap is evidence of a SLOW rate."""
    with_cens = geom_mle([1, 2, 3, 20], [False, False, False, True])[0]
    without = geom_mle([1, 2, 3], [False, False, False])[0]
    assert with_cens < without


def test_a_fully_censored_cell_is_undefined_and_not_a_number():
    """REG-003 §3.3: d = 0 returns UNDEFINED. Reporting 0.0 here would be a rate of
    zero, which is the opposite of what no observed recognitions means."""
    assert math.isnan(geom_mle([20, 20], [True, True])[0])


def test_annualisation_is_strictly_increasing_and_fixed_at_the_ends():
    assert annualise(0.0) == 0.0
    assert annualise(0.1227) == pytest.approx(0.4077, abs=5e-4)
    prev = -1.0
    for q in [i / 100 for i in range(0, 100)]:
        cur = annualise(q)
        assert cur > prev
        prev = cur


def test_the_alpha_regimes_are_exhaustive_and_ordered():
    """Every real number lands in exactly one cell -- the property REG-003 §3.2 bought
    by refusing to state a threshold. -14 lost a section to a band that could not
    separate a dead effect from a reversed one."""
    boundaries = [(0.9, "R1"), (0.33, "R1"), (0.32999, "R2"), (0.25, "R2"),
                  (0.19, "R2"), (0.18999, "R3"), (0.0500001, "R3"),
                  (0.05, "R4"), (0.0, "R4")]
    for value, expected in boundaries:
        assert regime(value)[0] == expected


def test_discrete_weibull_nests_the_geometric_at_k_equals_one():
    lags, cens = _synth(0.20)
    q, _ = fit_q_given_k(1.0, lags, cens)
    assert abs((1.0 - q) - geom_mle(lags, cens)[0]) < 0.01


def test_discrete_weibull_recovers_a_shape_it_was_not_told():
    """WT-080: the exponent is fitted. A fit that cannot recover a known k has no
    standing to reject k = 1 on the real sample."""
    rng = random.Random(5)
    q_true, k_true, lags, cens = 0.90, 1.6, [], []
    for _ in range(3000):
        u = rng.random()
        t = 0
        while q_true ** ((t + 1) ** k_true) > u and t < 40:
            t += 1
        lags.append(min(t, 20))
        cens.append(t >= 20)
    fit = fit_dweibull(lags, cens)
    assert abs(fit["k"] - k_true) < 0.15
    assert fit["k_ci_excludes_1"]


def test_the_null_preserves_every_per_firm_per_tier_marginal():
    ev = [{"cik": "A", "q_star": 10, "tier": 0}, {"cik": "A", "q_star": 10, "tier": 3},
          {"cik": "A", "q_star": 14, "tier": 3}, {"cik": "B", "q_star": 8, "tier": 1},
          {"cik": "B", "q_star": 8, "tier": 3}]
    marg = marginals(ev)
    risk = {"A": list(range(5, 30)), "B": list(range(5, 30))}
    for seed in range(25):
        drawn = {}
        for (f, _q), tiers in null_draw(marg, risk, random.Random(seed)).items():
            for t in tiers:
                drawn[(f, t)] = drawn.get((f, t), 0) + 1
        assert drawn == {(f, t): n for f, d in marg.items() for t, n in d.items()}


def test_co_occurrence_counts_stacked_quarters_and_not_spread_ones():
    stacked = [{"cik": "A", "q_star": 10, "tier": 0}, {"cik": "A", "q_star": 10, "tier": 3}]
    spread = [{"cik": "A", "q_star": 10, "tier": 0}, {"cik": "A", "q_star": 12, "tier": 3}]
    assert co_stats(fq_tiers(stacked))[0] == 1
    assert co_stats(fq_tiers(spread))[0] == 0
    assert co_stats(fq_tiers(stacked))[1][(0, 3)] == 1


def test_the_power_injection_moves_rather_than_adds():
    """The null is reused across power trials only because marginals are invariant
    under the injection. If that ever stops holding, every power figure is measuring
    a null the observed data does not come from."""
    ev = [{"cik": "A", "q_star": 10, "tier": 0}, {"cik": "A", "q_star": 12, "tier": 3},
          {"cik": "A", "q_star": 15, "tier": 1}, {"cik": "B", "q_star": 8, "tier": 1},
          {"cik": "B", "q_star": 9, "tier": 3}]
    for seed in range(25):
        inj = inject_cooccurrence(ev, 1.0, random.Random(seed))
        assert marginals(inj) == marginals(ev)
        assert len(inj) == len(ev)


def test_two_sided_p_sees_both_tails():
    """A one-sided test cannot separate independence from ANTI-co-occurrence, which is
    a finding and not a null. REG-003 §4.3 is two-sided for that reason."""
    draws = list(range(100))
    assert two_sided_p(99, draws) < 0.10
    assert two_sided_p(0, draws) < 0.10
    assert two_sided_p(50, draws) > 0.50
