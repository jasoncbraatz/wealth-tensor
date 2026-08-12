"""WT-090's deferral transform, protected independently of a data run.

`wt090` proves its own claims at run time through `severity.check`, whose witnesses
have to make each guard go red -- but only when somebody runs the instrument against
the sample. These pin the same algebra in CI, where they cost nothing, and they pin
the two properties a future refactor is most likely to break silently: that the
general form NESTS the published one, and that the existence condition is a statement
about the lag's tail rather than about its mean.
"""

import math
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

from wt090_age_dependent_alpha import (  # noqa: E402
    R_naive, R_registered, a2q, alpha_eff, dweibull, empirical, geometric,
    kendall_tau, q2a, simulate_R, solve_delta_star)

K_HAT, Q_HAT = 1.21, 0.9213424092985028
DW = dweibull(Q_HAT, K_HAT)
DW1 = DW.conditioned()


# --------------------------------------------------------------------------- nesting
@pytest.mark.parametrize("alpha", [0.05, 0.1227, 0.30])
@pytest.mark.parametrize("delta", [0.001, 0.01, 0.04])
@pytest.mark.parametrize("phi", [0.0, 0.4, 0.9])
def test_registered_form_nests_the_published_one(alpha, delta, phi):
    """R = (1-phi)(Pi(1/(1-d)) - 1) IS (1-phi)d/(a-d) at a geometric lag."""
    assert delta < alpha
    got = R_registered(geometric(alpha), delta, phi)
    want = R_naive(alpha, delta, phi)
    assert got == pytest.approx(want, rel=1e-12)


def test_the_generating_function_identity_itself():
    """SUM_{a>=1} z^a P(T>=a) = z(Pi(z)-1)/(z-1), which is what the derivation turns on."""
    lag, delta = DW1, 0.03
    z = 1.0 / (1.0 - delta)
    direct = sum(z ** a * lag.sur(a) for a in range(1, 4000))
    viaform = z * (lag.pi(z) - 1.0) / (z - 1.0)
    assert direct == pytest.approx(viaform, rel=1e-10)


# ------------------------------------------------------------------------ simulation
@pytest.mark.parametrize("delta", [0.002, 0.01, 0.03])
def test_age_structured_simulation_matches_the_closed_form(delta):
    """The filter carried as ageing cohorts, with no closed form in the loop."""
    assert simulate_R(DW1, delta, 0.5) == pytest.approx(
        R_registered(DW1, delta, 0.5), rel=1e-8)


def test_the_simulation_would_have_rejected_the_naive_substitution():
    """Otherwise the previous test proves nothing about the shape."""
    delta = 0.03
    sim = simulate_R(DW1, delta, 0.5)
    naive = R_naive(1.0 / DW1.mean(), delta, 0.5)
    assert abs(sim - naive) / sim > 1e-3


@pytest.mark.parametrize("phi", [0.0, 0.1, 0.5, 0.9, 1.0])
def test_phi_is_a_pure_scale_under_age_dependence(phi):
    r0 = R_registered(DW1, 0.03, 0.0)
    assert R_registered(DW1, 0.03, phi) / r0 == pytest.approx(1.0 - phi, abs=1e-14)


# ------------------------------------------------------------- the existence condition
def test_the_geometric_transform_diverges_exactly_at_its_own_rate():
    """alpha > delta is the geometric's radius of convergence and nothing more."""
    alpha = 0.1227
    assert math.isfinite(R_registered(geometric(alpha), 0.99 * alpha, 0.5))
    with pytest.raises((RuntimeError, OverflowError)):
        R_registered(geometric(alpha), 1.05 * alpha, 0.5)


def test_an_increasing_hazard_has_no_such_condition():
    """k > 1 makes the generating function entire; the domain restriction evaporates."""
    for delta in (0.05, 0.15, 0.30, 0.45):
        assert math.isfinite(R_registered(DW1, delta, 0.5))


def test_a_decreasing_hazard_would_have_had_no_domain_at_all():
    """The claim in §4.9 that k < 1 would leave no steady state, checked rather than said."""
    dfr = dweibull(Q_HAT, 0.75).conditioned()
    with pytest.raises((RuntimeError, OverflowError)):
        R_registered(dfr, 0.02, 0.5)


# ------------------------------------------------------------------ sign and magnitude
@pytest.mark.parametrize("delta", [0.002, 0.01, 0.03, 0.10])
def test_an_ifr_lag_defers_less_than_the_equal_mean_geometric(delta):
    """The NBUE direction, registered before it was computed."""
    same_mean = geometric(1.0 / DW1.mean())
    assert R_registered(DW1, delta, 0.5) < R_registered(same_mean, delta, 0.5)


def test_conditioning_away_the_unreachable_zero_lag_raises_R():
    """P(T=0) is mass the instrument cannot produce; removing it moves R up."""
    for delta in (0.002, 0.03):
        assert R_registered(DW1, delta, 0.5) > R_registered(DW, delta, 0.5)


def test_a_truncated_empirical_transform_is_a_lower_bound():
    """z^a with z>1 weights the tail the observation window cuts off."""
    lags = [1] * 175 + [t for t in range(2, 21) for _ in range(20)]
    cens = [False] * len(lags)
    emp = empirical(lags, cens)
    assert emp.pi(1.0 / (1.0 - 0.03)) < DW1.pi(1.0 / (1.0 - 0.03)) * 1.5
    assert emp.sur(21) == 0.0


# ------------------------------------------------------------------------- alpha_eff
def test_alpha_eff_is_constant_for_a_geometric_lag_and_only_then():
    alpha = 0.1227
    flat = [alpha_eff(geometric(alpha), d) for d in (0.002, 0.01, 0.03, 0.10)]
    assert max(flat) == pytest.approx(min(flat), rel=1e-12)
    assert max(flat) == pytest.approx(alpha, rel=1e-12)
    curved = [alpha_eff(DW1, d) for d in (0.002, 0.01, 0.03, 0.10)]
    assert max(curved) > min(curved) * 1.005


def test_alpha_eff_tends_to_the_reciprocal_mean_as_decay_vanishes():
    assert alpha_eff(DW1, 1e-7) == pytest.approx(1.0 / DW1.mean(), rel=1e-4)


# --------------------------------------------------------------------------- crossing
def test_the_crossing_solver_reproduces_section_4_4s_published_value():
    """delta3* = K alpha/(1+K) is the geometric case of Pi(1/(1-d)) = 1+K."""
    alpha_q = q2a(0.05)
    lag = geometric(alpha_q)
    r2 = R_registered(lag, q2a(0.010), 0.40)
    d3 = a2q(solve_delta_star(lag, 1.0 + r2 / (1.0 - 0.20)))
    assert d3 == pytest.approx(0.00789, abs=5e-4)


def test_the_shape_barely_moves_the_crossing_but_the_level_does():
    def crossing(lag):
        r2 = R_registered(lag, q2a(0.010), 0.40)
        return a2q(solve_delta_star(lag, 1.0 + r2 / (1.0 - 0.20)))

    at_calibration = crossing(geometric(q2a(0.05)))
    at_measured = crossing(geometric(0.12272272272272272))
    at_shape = crossing(DW1)
    assert abs(at_shape - at_measured) / at_measured < 0.01      # shape: under 1%
    assert abs(at_measured - at_calibration) / at_calibration > 0.02   # level: over 2%


# ------------------------------------------------------- the tau §4.4 now reports twice
@pytest.mark.parametrize("alpha_a,want", [(0.05, -1.0), (0.408, -2.0 / 3.0)])
def test_the_tabulated_ladders_tau_depends_on_the_recognition_rate(alpha_a, want):
    tiers = [(0.80, 0.030), (0.60, 0.020), (0.40, 0.010), (0.20, 0.002)]
    rs = [(1 - phi) * d / (alpha_a - d) for phi, d in tiers]
    assert kendall_tau(rs) == pytest.approx(want, abs=1e-9)


def test_unit_conversion_round_trips():
    for d in (0.002, 0.03, 0.3333, 0.8):
        assert a2q(q2a(d)) == pytest.approx(d, rel=1e-12)
