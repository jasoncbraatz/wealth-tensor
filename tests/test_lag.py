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
