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
    """Undamped simultaneous adjustment: stable at n=2, non-convergent at n>=3."""
    c2 = np.full(2, 10.0)
    assert cn.tatonnement(A, B, c2, damping=1.0)["iterations"] > 0

    for n in [3, 4, 6]:
        with pytest.raises(RuntimeError, match="did not converge"):
            cn.tatonnement(A, B, np.full(n, 10.0), damping=1.0, max_iter=5000)
        # damping rescues it, and it lands on the analytic point
        damped = cn.tatonnement(A, B, np.full(n, 10.0), damping=0.4)
        assert np.allclose(damped["q"], cn.closed_form(A, B, np.full(n, 10.0))["q"], atol=1e-6)


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
