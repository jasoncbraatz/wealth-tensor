"""The numeraire cancels: WT-002 item 4, the last leg of the Lambda defence.

Two halves, and both are needed. The negative half asserts that no conclusion moves when the
coupling moves across twelve orders of magnitude. The positive half asserts that the
*dimensional* outputs move exactly linearly with it -- without which the invariance would be
the empty kind you get from never using the constant at all.
"""

import numpy as np
import pytest

from wealth_tensor.lambda_sensitivity import (COUPLINGS, DIMENSIONLESS, DimensionedSystem,
                                              collapses_onto, diagnostics, invariance_report,
                                              scaling_exponent, sweep_coupling)

PHI = 0.3          # partial observability: the regime where the model has something to say


def test_the_sweep_spans_twelve_orders_of_magnitude():
    """A sensitivity claim is only as good as its range. State the range as a test."""
    assert min(COUPLINGS) == pytest.approx(1e-6)
    assert max(COUPLINGS) == pytest.approx(1e6)
    assert len(COUPLINGS) == 13


def test_no_dimensionless_conclusion_moves_with_the_coupling():
    """THE RESULT. Every claim the manuscript makes is bit-identical across the sweep.

    Spread is asserted at exactly zero rather than within a tolerance, because the algebra
    says exactly zero: the coupling never enters the recursion, only the dressing applied
    afterwards. A tolerance here would hide a real regression behind a generous epsilon.
    """
    rows = sweep_coupling(observable_share=PHI)
    spread = invariance_report(rows)
    for key in DIMENSIONLESS:
        assert spread[key] == 0.0, f"{key} moved with the numeraire: spread {spread[key]}"


def test_the_model_is_in_a_regime_where_there_is_something_to_be_invariant_about():
    """Guard against a vacuous pass: the diagnostics must be non-trivial at all.

    If a future parameter change flattened the model into doing nothing, the invariance test
    above would still pass -- triumphantly, and meaninglessly. This is the companion that
    makes it mean something.
    """
    d = diagnostics(DimensionedSystem(observable_share=PHI).run(400))
    assert d["n_crises"] > 5
    assert d["recognition_lag"] >= 0
    assert 0.0 < d["variance_concentration"] < 1.0
    assert d["relative_crisis_magnitude"] > 0.0


def test_dimensional_quantities_scale_exactly_linearly():
    """The positive half: currency-denominated outputs are proportional to the coupling.

    Slope of exactly 1 in log-log. Anything else would mean the coupling is doing physical
    work rather than converting units, which is precisely the accusation.
    """
    rows = sweep_coupling(observable_share=PHI)
    assert scaling_exponent(rows, "deferred_currency") == pytest.approx(1.0, abs=1e-9)
    assert scaling_exponent(rows, "terminal_lambda") == pytest.approx(1.0, abs=1e-9)

    # Lambda/eta is one number, not thirteen -- but it is computed as (eta * c/e) / eta, so it
    # round-trips through the numeraire and lands within a unit in the last place. That is a
    # property of IEEE 754, not of the model, and the distinction is worth keeping sharp: the
    # *conclusions* above are invariant to the bit (spread exactly 0.0), while a quantity that
    # is multiplied and then divided by 1e6 is invariant to floating point. Asserting exact
    # equality here would be asserting something untrue about arithmetic.
    ratios = [r["lambda_over_eta"] for r in rows]
    assert max(ratios) - min(ratios) < 1e-15


def test_the_coupling_is_actually_used():
    """Belt and suspenders against the emptiest possible failure mode.

    An invariance result is worthless if the constant is simply ignored. Two couplings must
    produce genuinely different currency figures -- differing here by twelve orders of
    magnitude -- while producing identical conclusions.
    """
    lo = DimensionedSystem(coupling=1e-6, observable_share=PHI).run(300)
    hi = DimensionedSystem(coupling=1e6, observable_share=PHI).run(300)
    assert hi["deferred_currency"] / lo["deferred_currency"] == pytest.approx(1e12, rel=1e-9)
    assert not np.allclose(hi["reported_currency"], lo["reported_currency"])
    assert diagnostics(hi) == diagnostics(lo)


def test_energy_scale_is_also_a_numeraire():
    """The same argument for the other unit. E0 sets the size of the system, not its physics."""
    small = DimensionedSystem(energy_scale=1.0, observable_share=PHI).run(300)
    large = DimensionedSystem(energy_scale=1e18, observable_share=PHI).run(300)
    assert diagnostics(small) == diagnostics(large)
    assert large["deferred_currency"] / small["deferred_currency"] == pytest.approx(1e18,
                                                                                    rel=1e-9)


def test_two_differently_dimensioned_systems_collapse_onto_one_curve():
    """The scaling collapse, stated as Buckingham pi requires it.

    Different energy scale, different coupling, same dimensionless parameters: one curve.
    This is the form in which the result should appear in the manuscript, because a collapse
    is a picture a reviewer can check in one glance.
    """
    a = DimensionedSystem(energy_scale=1.0, coupling=1e-6, observable_share=PHI).run(300)
    b = DimensionedSystem(energy_scale=6.02e23, coupling=42.0, observable_share=PHI).run(300)
    assert collapses_onto(a, b)


def test_the_collapse_test_can_fail():
    """A verifier that cannot fail is not a verifier. Perturb a pi-group; the collapse breaks."""
    a = DimensionedSystem(observable_share=PHI).run(300)
    b = DimensionedSystem(observable_share=PHI + 0.05).run(300)
    assert not collapses_onto(a, b)


def test_invariance_holds_across_the_observability_range_not_just_one_point():
    """One lucky parameter point is not a sensitivity analysis."""
    for phi in (1.0, 0.8, 0.5, 0.2, 0.0):
        spread = invariance_report(sweep_coupling(couplings=(1e-6, 1.0, 1e6),
                                                  observable_share=phi, periods=300))
        assert all(v == 0.0 for v in spread.values() if np.isfinite(v))


def test_parameter_validation():
    with pytest.raises(ValueError, match="energy_scale"):
        DimensionedSystem(energy_scale=0.0)
    with pytest.raises(ValueError, match="coupling"):
        DimensionedSystem(coupling=-1.0)
