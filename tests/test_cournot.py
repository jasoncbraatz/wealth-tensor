"""Every claim checked against a closed form or a textbook result."""

import numpy as np
import pytest

from wealth_tensor import cournot as cn

A, B = 100.0, 1.0


def test_symmetric_matches_textbook():
    """Symmetric n-firm Cournot: q = (a-c)/(b(n+1)), p = (a + n*c)/(n+1)."""
    for n in [1, 2, 3, 5, 10]:
        c = np.full(n, 10.0)
        r = cn.closed_form(A, B, c)
        assert np.allclose(r["q"], (A - 10.0) / (B * (n + 1)))
        assert np.isclose(r["p"], (A + n * 10.0) / (n + 1))


def test_monopoly_is_the_n_equals_one_case():
    r = cn.closed_form(A, B, [10.0])
    assert np.isclose(r["q"][0], (A - 10.0) / (2 * B))
    assert np.isclose(r["p"], (A + 10.0) / 2)


def test_three_routes_agree():
    """Closed form, FOC solve and damped tatonnement must land on the same point."""
    for c in ([10.0, 10.0], [5.0, 12.0, 20.0], [8.0, 9.0, 10.0, 11.0]):
        analytic = cn.closed_form(A, B, c)
        numeric = cn.solve_foc(A, B, c)
        dynamic = cn.tatonnement(A, B, c, damping=0.4)
        assert np.allclose(analytic["q"], numeric["q"], atol=1e-9)
        assert np.allclose(analytic["q"], dynamic["q"], atol=1e-6)


def test_lerner_identity_holds():
    """(p - MC_i)/p == s_i/|eps| -- the manuscript's markup equation, verified."""
    for c in ([10.0, 10.0], [5.0, 12.0, 20.0], [1.0, 2.0, 3.0, 4.0]):
        r = cn.closed_form(A, B, c)
        assert np.allclose(cn.lerner_residual(r), 0.0, atol=1e-12)


def test_hhi_tracks_concentration():
    """HHI must fall as symmetric firms are added, and equal 1/n exactly."""
    prev = 2.0
    for n in [1, 2, 4, 8]:
        r = cn.closed_form(A, B, np.full(n, 10.0))
        assert np.isclose(r["hhi"], 1.0 / n)
        assert r["hhi"] < prev
        prev = r["hhi"]


def test_price_approaches_marginal_cost_as_n_grows():
    """The Cournot limit theorem: p -> MC as n -> infinity."""
    c0 = 10.0
    gaps = [cn.closed_form(A, B, np.full(n, c0))["p"] - c0 for n in [2, 10, 100, 1000]]
    assert all(x > y > 0 for x, y in zip(gaps, gaps[1:]))
    assert gaps[-1] < 0.1


def test_tatonnement_stability_boundary():
    """Undamped simultaneous adjustment: stable at n=2, non-convergent at n>=3.

    NOTE the damping used below is 0.4 and the n tested are 3, 4 and 6. That is not an
    arbitrary trio: 0.4 rescues convergence only while 0.4 < 4/(n+1), i.e. n < 9. Adding
    n = 10 to this list fails, and it fails for a real reason rather than a numerical one
    -- see test_the_damping_that_rescues_tatonnement_shrinks_like_4_over_n.
    """
    c2 = np.full(2, 10.0)
    assert cn.tatonnement(A, B, c2, damping=1.0)["iterations"] > 0

    for n in [3, 4, 6]:
        assert 0.4 < 4.0 / (n + 1)           # the reason 0.4 works here, stated
        with pytest.raises(RuntimeError, match="did not converge"):
            cn.tatonnement(A, B, np.full(n, 10.0), damping=1.0, max_iter=5000)
        # damping rescues it, and it lands on the analytic point
        damped = cn.tatonnement(A, B, np.full(n, 10.0), damping=0.4)
        assert np.allclose(damped["q"], cn.closed_form(A, B, np.full(n, 10.0))["q"], atol=1e-6)


def test_the_damping_that_rescues_tatonnement_shrinks_like_4_over_n():
    """The rescue is n-dependent, and that is the paper's point rather than a footnote.

    The best-response map has linearised gain (n-1)/2. Damped, q <- q + d(BR(q) - q), the
    gain becomes |1 - d(n+1)/2|, so the process is stable iff

        d < 4/(n+1)

    The threshold is therefore not a constant to be chosen once: it vanishes like 4/n.
    Each firm must slow its own adjustment in proportion to the number of rivals it has,
    which means rescuing Cournot's adjustment process requires every firm to know n and
    condition on it -- more information than the static expectation the process is built
    on grants them. The repair needs precisely what the model denies.

    This is asserted as a bracket rather than an equality because convergence is measured
    on a grid; the point is that the measured boundary tracks 4/(n+1) as n grows, not that
    it is located to arbitrary precision.
    """
    step = 0.02
    for n in [2, 3, 4, 6, 10, 20]:
        c = np.full(n, 10.0)
        converged, failed = [], []
        for d in np.round(np.arange(step, 1.41, step), 3):
            try:
                cn.tatonnement(A, B, c, damping=float(d), max_iter=20000)
                converged.append(float(d))
            except RuntimeError:
                failed.append(float(d))
        threshold = 4.0 / (n + 1)
        assert converged, f"nothing converged at n={n}"
        assert max(converged) <= threshold, f"n={n}: converged above the predicted bound"
        if failed:
            assert min(failed) >= threshold - step, f"n={n}: failed below the bound"
        # and the damped solution is the analytic one, not merely a fixed point
        damped = cn.tatonnement(A, B, c, damping=float(max(converged)))
        assert np.allclose(damped["q"], cn.closed_form(A, B, c)["q"], atol=1e-6)

    # the standing overclaim guard: the threshold really does fall, it is not flat
    assert 4.0 / 21 < 4.0 / 11 < 4.0 / 7 < 4.0 / 3


def test_lower_cost_firm_takes_larger_share():
    r = cn.closed_form(A, B, [5.0, 10.0, 15.0])
    assert r["q"][0] > r["q"][1] > r["q"][2]
    assert r["profit"][0] > r["profit"][1] > r["profit"][2]


def test_closed_form_refuses_corner_cases():
    """A negative analytic output is an excluded firm, not a valid equilibrium."""
    with pytest.raises(ValueError, match="interior assumption violated"):
        cn.closed_form(A, B, [8.0, 9.0, 10.0, 11.0, 30.0])


def test_corner_solution_excludes_the_high_cost_firm():
    """Firm with MC=30 cannot produce when the rest set p=27.6; it is excluded at q=0.

    Hand-checked: dropping it leaves c=[8,9,10,11], q_i=(138-5c_i)/5, Q=72.4, p=27.6,
    and 27.6 < 30 confirms the exclusion is self-consistent.
    """
    c = [8.0, 9.0, 10.0, 11.0, 30.0]
    r = cn.solve_cournot(A, B, c)
    assert r["excluded"] == [4]
    assert np.isclose(r["q"][4], 0.0)
    assert np.allclose(r["q"][:4], [19.6, 18.6, 17.6, 16.6])
    assert np.isclose(r["p"], 27.6)
    assert r["p"] < c[4]  # the exclusion is self-consistent

    # and the dynamic route, which floors output at zero, finds the same point
    dyn = cn.tatonnement(A, B, c, damping=0.4)
    assert np.allclose(dyn["q"], r["q"], atol=1e-6)


def test_solve_cournot_matches_closed_form_when_interior():
    for c in ([10.0, 10.0], [5.0, 12.0, 20.0], [8.0, 9.0, 10.0, 11.0]):
        assert np.allclose(cn.solve_cournot(A, B, c)["q"], cn.closed_form(A, B, c)["q"])
