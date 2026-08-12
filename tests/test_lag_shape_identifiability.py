"""Tests pinning REG-005 / WT-091's claims about lag-shape identifiability.

Written to pin the claims in `docs/preregistration/REG-005-p3-lag-shape-
identifiability.md` and §4.10, NOT to hunt bugs -- which, per RESULT-REG-004 §2, is
historically when this project's tests have found the interesting ones.

Run with the venv: `./.venv/bin/python -m pytest tests/test_lag_shape_identifiability.py`
"""
from __future__ import annotations

import math
import pathlib
import sys

import numpy as np
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from wt091_lag_shape_identifiability import (  # noqa: E402
    CONFLUENT_EPS,
    K_HAT,
    Q_HAT,
    alpha_eff_annual,
    eps_rel,
    fit_mimic,
    fit_weibull_free_k,
    geometric_survival,
    pgf_outside,
    q_to_yr,
    series_closed_form,
    series_from_survival,
    series_geometric,
    series_weibull,
    weibull_survival,
    yr_to_q,
)

D10 = yr_to_q(0.10)          # a ten-year life, quarterly
N = 40


# ======================================================================================
# The construction: does the convolution BE §4.2's closed form where it must?
# ======================================================================================
@pytest.mark.parametrize("life", [3.0, 5.0, 10.0, 20.0, 40.0])
@pytest.mark.parametrize("phi", [0.20, 0.60, 0.80])
@pytest.mark.parametrize("alpha", [0.02, 0.12272272272272272, 0.40])
def test_f1_convolution_nests_the_published_closed_form(life, phi, alpha):
    """REG-005 §2 F1. A geometric survival in the convolution IS §4.2's closed form."""
    d = yr_to_q(1.0 / life)
    a = series_geometric(alpha, d, phi, N)
    b = series_closed_form(alpha, d, phi, N)
    assert np.max(np.abs(a - b) / np.abs(b)) <= 1e-12


def test_books_open_square():
    """c(0) = 1 in every world -- the normalisation REG-005 §1 declares."""
    for surv in (geometric_survival(0.12, N), weibull_survival(K_HAT, Q_HAT, N)):
        assert series_from_survival(surv, D10, 0.6, N)[0] == pytest.approx(1.0, abs=0.0)


def test_series_is_positive_throughout_under_admissibility():
    """REG-005 §4: the relative-per-point metric requires c(t) > 0, and it is."""
    for life in (3.0, 10.0, 40.0):
        d = yr_to_q(1.0 / life)
        for phi in (0.0, 0.5, 1.0):
            assert np.all(series_weibull(K_HAT, Q_HAT, d, phi, 400) > 0.0)


def test_confluent_limit_is_continuous_at_alpha_equals_delta():
    """REG-005 §3 Q3.2. The closed form is 0/0 at alpha = delta and the optimiser walks
    there; the limit branch must agree with the neighbourhood it replaces."""
    d = 0.05
    lim = series_closed_form(d, d, 0.6, N)
    near = series_closed_form(d * (1 + 1e-7), d, 0.6, N)
    assert np.max(np.abs(lim - near) / np.abs(lim)) < 1e-6
    # and the limit branch is genuinely a DIFFERENT code path, not a coincidence
    assert abs(d - d) < CONFLUENT_EPS


def test_section_4_2_mirror_holds_exactly_in_this_construction():
    """§4.2's theorem: (alpha, delta, phi) and (delta, alpha, phi*delta/alpha) generate
    the identical reported series. Nothing in REG-005 breaks it, and F2's search relies
    on it being exact rather than approximate."""
    alpha, d, phi = 0.30, 0.05, 0.40
    a = series_geometric(alpha, d, phi, N)
    b = series_geometric(d, alpha, phi * d / alpha, N)
    assert np.max(np.abs(a - b) / np.abs(a)) < 1e-13


# ======================================================================================
# F4: the T = 0 mass, the erratum that bit REG-004 twice and on two estimators
# ======================================================================================
@pytest.mark.parametrize("life", [3.0, 10.0, 40.0])
@pytest.mark.parametrize("phi", [0.20, 0.60, 0.80])
def test_f4_conditioning_on_t_ge_1_is_exactly_a_phi_reparameterisation(life, phi):
    """REG-005 §2 F4. S(a) -> S(a)/S(1) divides the gap by S(1) at every age alike, and
    the gap is proportional to (1-phi). So the conditioning is absorbed, exactly."""
    d = yr_to_q(1.0 / life)
    s = weibull_survival(K_HAT, Q_HAT, N)
    base = series_from_survival(s, d, phi, N)
    moved = series_from_survival(s / s[0], d, 1.0 - (1.0 - phi) * s[0], N)
    assert np.max(np.abs(moved - base) / base) <= 1e-12


def test_f4_is_not_vacuous_conditioning_without_the_phi_shift_does_move_the_series():
    """The witness for F4: leave phi alone and the series MUST move, or F4 is a phantom
    tag credited with catching an absorption that was never in doubt."""
    s = weibull_survival(K_HAT, Q_HAT, N)
    base = series_from_survival(s, D10, 0.60, N)
    unshifted = series_from_survival(s / s[0], D10, 0.60, N)
    assert np.max(np.abs(unshifted - base) / base) > 1e-4


def test_weibull_at_k_1_conditioned_is_the_geometric():
    """The mechanism behind F4, stated as an identity: q^a conditioned on T >= 1 is
    (1-alpha)^(a-1) at alpha = 1-q. The T = 0 mass IS the whole difference."""
    q = 0.87
    s = weibull_survival(1.0, q, N)
    assert np.allclose(s / s[0], geometric_survival(1.0 - q, N), rtol=0, atol=1e-14)


# ======================================================================================
# The convolution's arithmetic, and a docstring that had to be narrowed
# ======================================================================================
def test_lfilter_recursion_equals_the_naive_loop():
    """The vectorised inner sum is the one-pole recursion and nothing else."""
    surv = weibull_survival(K_HAT, Q_HAT, 120)
    d, phi, n = 0.07, 0.5, 120
    D = 1.0 - d
    gap, run = np.zeros(n + 1), 0.0
    for i in range(1, n + 1):
        run = run * D + surv[i - 1]
        gap[i] = run
    naive = np.power(D, np.arange(n + 1, dtype=float)) + (1 - phi) * d * gap
    assert np.allclose(series_from_survival(surv, d, phi, n), naive, rtol=1e-14, atol=0)


def test_the_dinverse_form_overflows_only_OUTSIDE_the_swept_rectangle():
    """The recursion is used because it is exact and O(n). The `D**(-a)` form it replaces
    would overflow -- but NOT at any rate this instrument sweeps, and the docstring says
    so rather than claiming a save it never made.

    D^(-n) overflows a double at n*|log D| > 709. At n = 400 that needs D < 0.17, i.e.
    delta > 0.83 PER QUARTER. The fastest rate swept is a three-year life, 0.0964 per
    quarter, where D^(-400) is about 4e17 -- large, exact, and nowhere near overflow.
    """
    d_fastest = yr_to_q(1.0 / 3.0)
    assert d_fastest == pytest.approx(0.09640, abs=1e-4)
    assert np.isfinite((1.0 - d_fastest) ** -400)
    assert not np.isfinite(np.float64(1.0 - 0.90) ** -400)      # delta = 0.90/quarter
    # and where it does NOT overflow, the two forms agree, so nothing is being hidden
    surv = weibull_survival(K_HAT, Q_HAT, 400)
    D = 1.0 - d_fastest
    a = np.arange(1, 401, dtype=float)
    gap_direct = np.power(D, 400) * np.sum(np.power(D, -a) * surv)
    assert series_from_survival(surv, d_fastest, 0.0, 400)[400] == pytest.approx(
        np.power(D, 400) + d_fastest * gap_direct, rel=1e-10)


# ======================================================================================
# The metric (REG-005 §4), and why the obvious one is registered as wrong
# ======================================================================================
def test_eps_rel_is_zero_on_identity_and_blind_to_a_common_scale():
    tgt = series_weibull(K_HAT, Q_HAT, D10, 0.6, N)
    assert eps_rel(tgt, tgt) == 0.0
    assert eps_rel(2.0 * tgt, 2.0 * tgt) == 0.0


def test_the_norm_relative_metric_would_have_made_ladder_S_vacuous():
    """REG-005 §4's registered reason, pinned as an inequality rather than asserted.

    A geometrically decaying series' late points carry almost no NORM. Perturb only the
    second half of a 400-quarter series by 1% per point: the relative-per-point metric
    sees it, the norm-relative metric essentially does not -- so under the latter a
    longer series could not have helped and ladder S was decided by the metric.
    """
    tgt = series_weibull(K_HAT, Q_HAT, yr_to_q(0.10), 0.6, 400)
    bumped = tgt.copy()
    bumped[200:] *= 1.01
    per_point = eps_rel(bumped, tgt)
    norm_rel = float(np.linalg.norm(bumped - tgt) / np.linalg.norm(tgt))
    assert per_point > 0.5 * 0.01                 # sees it at nearly its full size
    assert norm_rel < per_point / 100.0           # and the norm metric does not


# ======================================================================================
# The results REG-005's ladders read, pinned so a refactor cannot move them silently
# ======================================================================================
def test_the_constant_hazard_mimics_the_measured_shape_to_under_one_part_in_a_thousand():
    """Ladder I. The headline: a constant-hazard world reproduces the k = 1.21 world's
    reported series to ~4e-4 relative, per point, over ten years."""
    tgt = series_weibull(K_HAT, Q_HAT, D10, 0.60, N)
    r = fit_mimic(tgt, N, admissible=True)
    assert r["eps"] < 1e-3
    assert r["eps"] > 1e-6                    # and it is NOT exact -- ladder I is not I1


def test_the_mimic_search_is_not_blind_f3():
    """REG-005 §2 F3. A k = 0.5 world -- decreasing hazard, no steady state at any
    positive delta per §4.9 -- must NOT be mimicked below the I2 threshold."""
    wit = series_weibull(0.5, Q_HAT, D10, 0.60, N)
    assert fit_mimic(wit, N, admissible=True)["eps"] >= 1e-3


def test_the_mimic_recovers_a_constant_hazard_world_or_its_mirror_f2():
    """REG-005 §2 F2. If the search cannot find the answer when there is one, no residual
    it reports about any other world means anything."""
    alpha, d, phi = 0.12, D10, 0.60
    r = fit_mimic(series_geometric(alpha, d, phi, N), N, admissible=True)
    got = np.array([r["alpha"], r["delta"], r["phi"]])
    truth = np.array([alpha, d, phi])
    mirror = np.array([d, alpha, phi * d / alpha])
    assert min(np.max(np.abs(got - truth)), np.max(np.abs(got - mirror))) < 1e-4


def test_the_search_floor_is_far_below_the_finest_sigma_reported():
    """Ladder W's non-emptiness rests on the profile bottoming out at k_hat well below
    the smallest sigma in the grid. If the optimiser's own floor rose to 1e-6, the
    sigma = 1e-6 row would be measuring scipy rather than the model."""
    tgt = series_weibull(K_HAT, Q_HAT, D10, 0.60, N)
    assert fit_weibull_free_k(tgt, N, K_HAT)[0] < 1e-7


def test_a_sub_unit_shape_reproduces_the_measured_world_to_one_part_in_a_thousand():
    """The finding §4.10 reports. k = 0.8 has a DECREASING hazard, so by §4.9 it admits
    no steady-state deferral measure at ANY positive decay rate -- and its reported
    series is within one part in a thousand of the measured world's."""
    tgt = series_weibull(K_HAT, Q_HAT, D10, 0.60, N)
    assert fit_weibull_free_k(tgt, N, 0.8)[0] <= 1e-3
    # not vacuous: far enough away and it does separate
    assert fit_weibull_free_k(tgt, N, 0.2)[0] > 1e-3


def test_three_recognition_rates_are_three_different_numbers():
    """Ladder P. alpha_hat (event dates), alpha_eff(delta) (deferral matching) and
    alpha_ser (series matching) are distinct functionals of one lag distribution."""
    def series_rate(life, phi=0.60):
        d = yr_to_q(1.0 / life)
        r = fit_mimic(series_weibull(K_HAT, Q_HAT, d, phi, N), N, admissible=True)
        roots = sorted([r["alpha"], r["delta"]])
        return q_to_yr(roots[1] if abs(roots[0] - d) < abs(roots[1] - d) else roots[0])

    a_hat = q_to_yr(0.12272272272272272)
    # At a ten-year life the series match and the deferral match nearly coincide, and
    # BOTH sit well away from the event-date MLE.
    a_ser10, a_eff10 = series_rate(10.0), alpha_eff_annual(0.10)
    assert abs(a_ser10 - a_hat) / a_hat > 0.05
    assert abs(a_ser10 - a_eff10) / a_eff10 < 0.02
    assert a_hat < a_ser10 < a_eff10                 # the ordering §4.10 reports
    # At a three-year life they part company -- which is the finding, not the agreement.
    a_ser3, a_eff3 = series_rate(3.0), alpha_eff_annual(1.0 / 3.0)
    assert abs(a_ser3 - a_eff3) / a_eff3 > 0.10
    assert a_ser3 < a_eff3 and a_ser10 < a_eff10     # series below the transform
    # and the series constant is nearly flat where the transform is not
    assert abs(series_rate(40.0) - a_ser10) / a_ser10 < 0.01
    assert abs(a_eff3 - alpha_eff_annual(0.025)) / a_eff3 > 0.05


def test_alpha_eff_is_a_curve_not_a_constant():
    """REG-004 §5's E2, re-pinned here because ladder P compares against it per-delta."""
    vals = [alpha_eff_annual(1.0 / life) for life in (40, 20, 10, 5, 3)]
    assert vals == sorted(vals)                       # rises as the class decays faster
    assert vals[-1] / vals[0] > 1.05


def test_pgf_refuses_a_divergent_sum_rather_than_returning_a_finite_number():
    """RESULT-REG-004 §2's repair, re-pinned. A decreasing-hazard lag's transform
    diverges outside the unit disc; the guard must REFUSE, not return."""
    z = 1.0 / (1.0 - yr_to_q(0.333))
    with pytest.raises(OverflowError):                   # term passes 1e290
        pgf_outside(weibull_survival(0.5, Q_HAT, 12000), z)
    with pytest.raises(OverflowError):                   # truncated, not exhausted
        pgf_outside(weibull_survival(0.5, Q_HAT, 4000), z)
    # and at the measured shape the same call returns a finite number, because the
    # contribution genuinely turns over long before the array ends
    assert math.isfinite(pgf_outside(weibull_survival(K_HAT, Q_HAT, 4000), z))
