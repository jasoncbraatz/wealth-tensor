"""The reporting layer as a filter, checked rather than asserted."""

import numpy as np
import pytest

from wealth_tensor.lag import (LayeredFirm, variance_suppression, variance_concentration,
                               recognition_lag, deferred_information)

PHIS = [1.0, 0.8, 0.5, 0.2, 0.0]


def no_crisis(phi):
    return LayeredFirm(observable_share=phi, crisis_threshold=np.inf).run(300)


def test_gap_is_exactly_real_minus_reported():
    """Structural invariant: the tracked gap and the layer difference never diverge."""
    for phi in PHIS:
        r = LayeredFirm(observable_share=phi).run(200)
        assert np.abs(r["gap"] - (r["real"] - r["reported"])).max() == 0.0


def test_full_observability_is_a_perfect_window():
    """phi = 1: no lag, no deferred information, no crisis, coupling identically one."""
    r = LayeredFirm(observable_share=1.0).run(400)
    assert recognition_lag(r) == 0
    assert deferred_information(r) == 0.0
    assert r["n_crises"] == 0
    assert np.abs(r["coupling"] - 1.0).max() < 1e-12


def test_full_maintenance_removes_the_phenomenon_entirely():
    """No net entropy means nothing to defer, whatever the observability."""
    firm = LayeredFirm(maintenance_ratio=1.0, observable_share=0.0)
    assert firm.effective_decay() == 0.0
    r = firm.run(400)
    assert r["n_crises"] == 0
    assert np.abs(r["coupling"] - 1.0).max() < 1e-12


def test_lag_grows_monotonically_as_observability_falls():
    """WT-026's sharp prediction: lag scales with UNobservability, not with delay per se.

    This is what saves the thesis from the forward-looking-markets objection. Announced
    change (phi near 1) passes straight through; only deferred degradation accumulates.
    """
    lags = [recognition_lag(no_crisis(phi)) for phi in PHIS]
    assert lags[0] == 0
    assert all(a <= b for a, b in zip(lags, lags[1:]))
    assert lags[-1] > lags[0]


def test_smoothing_grows_monotonically_as_observability_falls():
    vs = [variance_suppression(no_crisis(phi)) for phi in PHIS]
    assert np.isclose(vs[0], 1.0)
    assert all(a >= b for a, b in zip(vs, vs[1:]))
    assert vs[-1] < 0.8


def test_deferred_information_grows_monotonically_as_observability_falls():
    """The integral of the unrecognised gap -- WT-024's identification with coupling drift."""
    di = [deferred_information(no_crisis(phi)) for phi in PHIS]
    assert di[0] == 0.0
    assert all(a <= b for a, b in zip(di, di[1:]))


def test_volatility_is_relocated_not_removed():
    """The corrected claim, and a better one than over-smoothing.

    With crises active the reporting layer is markedly SMOOTHER than reality between
    crises, while an increasing share of all its movement occurs inside the snaps. Total
    volatility is not suppressed; it is concentrated. Long quiet stretches during which
    deferred information accrues invisibly, then all of it at once.
    """
    conc, between = [], []
    for phi in [0.8, 0.5, 0.2, 0.0]:
        r = LayeredFirm(observable_share=phi).run(400)
        conc.append(variance_concentration(r))
        between.append(variance_suppression(r))
    assert all(a <= b for a, b in zip(conc, conc[1:]))     # concentration rises
    assert all(a >= b for a, b in zip(between, between[1:]))  # quiet periods get quieter
    assert conc[-1] > 0.95


def test_crisis_frequency_scales_with_entropy_rate():
    """The Costco-versus-SaaS point: a decade of re-provisioning against continuous zero-days."""
    counts = [LayeredFirm(entropy_rate=d, observable_share=0.3).run(400)["n_crises"]
              for d in [0.01, 0.05, 0.20]]
    assert counts[0] == 0
    assert counts[0] < counts[1] < counts[2]


def test_crisis_magnitude_equals_the_withheld_information():
    """The snap delivers exactly what had been deferred -- no more, no less."""
    r = LayeredFirm(observable_share=0.2).run(400)
    assert r["n_crises"] > 0
    for c in r["crises"]:
        assert np.isclose(c["magnitude"], abs(c["reported_before"] - c["reported_after"]))


def test_parameter_validation():
    with pytest.raises(ValueError, match="observable_share"):
        LayeredFirm(observable_share=1.5)
    with pytest.raises(ValueError, match="recognition_rate"):
        LayeredFirm(recognition_rate=0.0)


def test_deferred_information_is_exactly_linear_in_unobservability():
    """D(phi) = (1 - phi) * D(0), exactly -- a closed form, not a simulation regularity.

    With the correction mechanism disabled, substituting E(t+1) - C(t) = gap(t) + dE into the
    two recursions gives gap(t+1) = (1 - alpha)*gap(t) + (1 - phi)*dE, so with gap(0) = 0 every
    gap is (1 - phi) times its value on the phi = 0 path. dE < 0 throughout, so all terms share
    a sign and the absolute integral inherits the factor exactly.

    Paper III (S4) reports this as a closed form. If a future change to `lag.py` makes the gap
    recursion non-linear in phi, this test is the thing that screams -- the paper's claim is
    exactness, and "approximately linear" would be a different and much weaker sentence.
    """
    base = deferred_information(
        LayeredFirm(observable_share=0.0, crisis_threshold=np.inf).run(400))
    assert base > 0
    for phi in [0.0, 0.1, 0.2, 0.3, 0.5, 0.8, 0.9, 1.0]:
        got = deferred_information(
            LayeredFirm(observable_share=phi, crisis_threshold=np.inf).run(400))
        assert np.isclose(got, (1.0 - phi) * base, rtol=1e-12, atol=1e-9), phi


def test_recognition_lag_is_not_linear_in_unobservability():
    """The delay and the quantity deferred do NOT move together, and the paper says so.

    Deferred information is exactly linear in (1 - phi); the lag is sigmoidal. Guarding the
    negative claim matters as much as the positive one -- if both were linear the paper would
    be entitled to a much simpler story than the one it tells.
    """
    lags = {phi: recognition_lag(
        LayeredFirm(observable_share=phi, crisis_threshold=np.inf).run(400))
        for phi in [1.0, 0.9, 0.5, 0.1, 0.0]}
    assert lags[1.0] == 0
    assert all(a <= b for a, b in zip(
        [lags[p] for p in [1.0, 0.9, 0.5, 0.1, 0.0]],
        [lags[p] for p in [0.9, 0.5, 0.1, 0.0]]))          # monotone in unobservability
    # Slow at the disclosed end, steep through the middle, saturating at the undisclosed end.
    assert (lags[0.9] - lags[1.0]) < (lags[0.5] - lags[0.9])   # convex early
    assert (lags[0.0] - lags[0.1]) < (lags[0.5] - lags[0.9])   # saturating late


def test_the_two_layer_recursion_collapses_to_the_form_limitation_4_publishes():
    """C(t+1) = C(t)*(1-alpha) + E(t)*(alpha - phi*delta), with delta = d*(1-m).

    Paper III's Limitation 4 publishes this collapse and derives phi = (alpha - k)/delta from
    it, where k = alpha - phi*delta. That algebra is the entire basis of the identifiability
    argument, and until 2026-08-10 it had no test -- an audit caught the published form using
    `d` (the ENTROPY RATE) where it meant `d*(1-m)` (the EFFECTIVE decay), a factor-0.4 error
    in the flattering direction. This test exists so that cannot recur silently.

    Correction mechanism disabled: the snap is a separate, non-differentiable branch and
    Limitation 4's claim is explicitly about the filter in isolation.
    """
    for phi, d, m, alpha in [(0.3, 0.05, 0.6, 0.05),
                             (0.77, 0.11, 0.25, 0.09),
                             (0.0, 0.20, 0.0, 0.5),
                             (1.0, 0.01, 0.9, 0.01)]:
        firm = LayeredFirm(observable_share=phi, entropy_rate=d, maintenance_ratio=m,
                           recognition_rate=alpha, crisis_threshold=np.inf)
        res = firm.run(60)
        delta = d * (1.0 - m)
        assert np.isclose(delta, firm.effective_decay(), rtol=0, atol=1e-15)

        E, C = res["real"], res["reported"]
        predicted = C[:-1] * (1.0 - alpha) + E[:-1] * (alpha - phi * delta)
        assert np.allclose(C[1:], predicted, rtol=1e-12, atol=1e-10), (phi, d, m, alpha)

        # E(t) = E0 * (1 - delta)^t, the geometric driving term the composite is read against.
        t = np.arange(E.size)
        assert np.allclose(E, 100.0 * (1.0 - delta) ** t, rtol=1e-12, atol=1e-10)

        # phi = (alpha - k)/delta inverts exactly, which is what makes the 1/delta
        # conditioning claim a statement about this model rather than about an optimiser.
        if delta > 0:
            k = alpha - phi * delta
            assert np.isclose((alpha - k) / delta, phi, rtol=1e-12, atol=1e-12)


# --------------------------------------------------------------------------------------
# §4.4 publishes two closed-form boundaries and a domain restriction (wt088 / REG-002).
# Each is load-bearing in print and none of them had a test. Pinned here.
# --------------------------------------------------------------------------------------

def _R(phi, delta, alpha):
    """The steady-state deferral measure §4.3 derives."""
    return (1.0 - phi) * delta / (alpha - delta)


def test_the_crossing_rate_closed_form_44_publishes_is_exact():
    """§4.4: R_3 = R_2 at delta_3* = K*alpha/(1+K), K = R_2/(1-phi_3).

    The manuscript quotes 0.0079 and calls the tau = -1 reversal a knife edge on it.
    Verified against bisection, which knows nothing about the algebra.
    """
    alpha = 0.05
    phi = [0.80, 0.60, 0.40, 0.20]
    delta = [0.030, 0.020, 0.010, 0.002]

    r2 = _R(phi[2], delta[2], alpha)
    k = r2 / (1.0 - phi[3])
    d3_star = k * alpha / (1.0 + k)

    lo, hi = 1e-6, alpha - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if _R(phi[3], mid, alpha) < r2:
            lo = mid
        else:
            hi = mid
    assert np.isclose(d3_star, 0.5 * (lo + hi), rtol=0, atol=1e-12)
    assert np.isclose(round(d3_star, 4), 0.0079, rtol=0, atol=1e-12)

    # The published consequence: the tabulated ladder is strictly decreasing, and a rate
    # five per cent above the crossing is not.
    tabulated = [_R(p, d, alpha) for p, d in zip(phi, delta)]
    assert all(tabulated[i] > tabulated[i + 1] for i in range(3))

    broken = [_R(p, d, alpha) for p, d in
              zip(phi, delta[:3] + [d3_star * 1.05])]
    assert not all(broken[i] > broken[i + 1] for i in range(3))


def test_the_first_rung_boundary_44_publishes_is_exact():
    """§4.4: rung 0->1 falls iff delta_1 < alpha*delta_0/(2*alpha - delta_0).

    The factor of two is (1-phi_1)/(1-phi_0) at the tabulated shares; the test asserts the
    published special case AND that the general inequality tracks the measure itself.
    """
    alpha, phi0, phi1 = 0.05, 0.80, 0.60
    d0 = 0.030
    boundary = alpha * d0 / (2.0 * alpha - d0)
    assert np.isclose(boundary, 0.0214, rtol=0, atol=5e-5)
    assert np.isclose(1.0 / boundary, 46.7, rtol=0, atol=0.05)

    for d1 in [0.005, 0.015, 0.0200, 0.0214, 0.0250, 0.040]:
        falls = _R(phi1, d1, alpha) < _R(phi0, d0, alpha)
        assert falls == (d1 < boundary), (d1, boundary)

    # And the published claim that the tabulated 0.020 sits inside by a hair.
    assert 0.020 < boundary
    assert (boundary - 0.020) / 0.020 < 0.08


def test_no_steady_state_deferral_ratio_once_decay_outruns_recognition():
    """§4.4's domain restriction: R exists only for delta < alpha.

    Below the pole the gap ratio settles to the closed form; above it the ratio grows
    without bound, so there is nothing to rank. The manuscript's domain sentence rests on
    this and nothing else.
    """
    alpha, phi = 0.05, 0.20

    def ratio(d, periods):
        r = LayeredFirm(entropy_rate=d, maintenance_ratio=0.0, observable_share=phi,
                        recognition_rate=alpha, crisis_threshold=np.inf).run(periods)
        return abs(r["gap"][-1]) / r["real"][-1]

    # Below the pole the ratio converges to the closed form -- but the transient decays
    # like ((1-alpha)/(1-delta))^t, so the approach SLOWS without bound as delta -> alpha.
    # The horizon each rate needs is pinned here rather than hidden in a loose tolerance:
    # at delta = 0.045 the 400-period ratio is still 11% short of its own limit, which is
    # why §4.3's transient bound is quoted for the tabulated ladder and not for the pole.
    for d, periods in [(0.010, 400), (0.030, 400), (0.045, 3000)]:
        near, far = ratio(d, periods), ratio(d, 2 * periods)
        closed = _R(phi, d, alpha)
        assert abs(far - closed) < abs(near - closed) or np.isclose(far, closed, rtol=1e-9)
        assert np.isclose(far, closed, rtol=2e-2), (d, far, closed)

    assert abs(ratio(0.045, 400) - _R(phi, 0.045, alpha)) / _R(phi, 0.045, alpha) > 0.10

    # Past the pole the ratio does not settle at ANY horizon: it grows geometrically, at
    # a rate set by (1-alpha)/(1-delta). Just past the pole that rate is barely above one
    # -- delta = 0.051 only multiplies by ~2.5 per 400 periods -- so divergence is asserted
    # as unbounded growth rather than as a fixed factor, which would only be testing how
    # far past the pole the sample sits.
    for d in [0.051, 0.060, 0.100]:
        r1, r2, r3 = ratio(d, 400), ratio(d, 800), ratio(d, 4000)
        assert r2 > 1.5 * r1 and r3 > 1.5 * r2, (d, r1, r2, r3)
        # and the closed form is not merely wrong out here, it is the wrong SIGN
        assert _R(phi, d, alpha) < 0.0

    # The growth is geometric at exactly log((1-alpha)/(1-delta)) per period, which is why
    # no horizon rescues it. Pinned only just past the pole: by delta = 0.100 the ratio
    # reaches 10^94 by period 4000, and a check at 8000 would be measuring float64's
    # exponent range rather than the model.
    for d in [0.051, 0.060]:
        measured = (np.log(ratio(d, 8000)) - np.log(ratio(d, 4000))) / 4000.0
        predicted = np.log((1.0 - alpha) / (1.0 - d))
        assert measured > 0
        assert abs(measured - predicted) / predicted < 0.01, (d, measured, predicted)

    # The contrast that makes the domain restriction a restriction: at the same long
    # horizon the sub-critical rates are AT their closed form, to a part in ten thousand.
    for d in [0.010, 0.030]:
        assert np.isclose(ratio(d, 4000), _R(phi, d, alpha), rtol=1e-4)
