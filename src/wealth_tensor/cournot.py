"""Cournot-Nash equilibrium under linear inverse demand.

Three independent routes to the same equilibrium, so that each one checks the others:

  closed_form   - analytic solution
  solve_foc     - simultaneous first-order conditions via scipy.optimize.root
  tatonnement   - iterated best response, i.e. Cournot's own dynamic adjustment

The third is not redundant. The manuscript argues that tatonnement rests on an
expectation that is falsified every period out of equilibrium: each firm assumes its
rivals hold output constant, and each period every firm moves. Having it as running
code lets that critique be inspected rather than asserted -- the convergence path is
observable, and so is its dependence on the damping factor.

Model
-----
Inverse demand:   p = a - b * Q,  Q = sum_i q_i
Firm i profit:    pi_i = q_i * p - c_i * q_i
FOC:              a - b*Q - b*q_i - c_i = 0
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import root


def closed_form(a: float, b: float, c) -> dict:
    """Analytic interior Cournot-Nash equilibrium.

    q_i = (a + sum(c) - (n+1) * c_i) / (b * (n + 1))

    Valid while every q_i > 0. Corner solutions (a firm priced out of the market)
    are not handled here on purpose -- see solve_foc for the clipped version.
    """
    c = np.asarray(c, dtype=float)
    n = c.size
    q = (a + c.sum() - (n + 1) * c) / (b * (n + 1))
    if np.any(q <= 0):
        raise ValueError(
            "interior assumption violated: firms "
            f"{np.flatnonzero(q <= 0).tolist()} take non-positive output. "
            "Their marginal cost exceeds the price the rest of the market sets, so "
            "they are excluded rather than loss-making. Use solve_cournot()."
        )
    return _summarise(a, b, c, q)


def solve_foc(a: float, b: float, c, x0=None) -> dict:
    """Solve the simultaneous FOC system numerically."""
    c = np.asarray(c, dtype=float)
    n = c.size

    def residual(q):
        Q = q.sum()
        return a - b * Q - b * q - c

    if x0 is None:
        x0 = np.full(n, (a - c.mean()) / (b * (n + 1)))
    sol = root(residual, x0, method="hybr")
    if not sol.success:
        raise RuntimeError(f"FOC solve failed: {sol.message}")
    return _summarise(a, b, c, sol.x)


def tatonnement(a: float, b: float, c, damping: float = 1.0,
                tol: float = 1e-12, max_iter: int = 100_000) -> dict:
    """Iterated best response.

    Best response of firm i to rivals' aggregate output Q_minus_i:
        q_i = max(0, (a - c_i - b * Q_minus_i) / (2b))

    The linearised undamped map has gain (n-1)/2, so simultaneous adjustment is
    stable only for n = 2, marginal at n = 3, and unstable beyond. Because output is
    floored at zero it does not run off to infinity; it settles into a bounded
    oscillation and never converges. Verified numerically in tests, not assumed.

    This is the manuscript's point made executable: Cournot's own adjustment process
    fails precisely where his static expectation is least defensible -- every firm
    assumes its rivals stand still, and every period they all move. Damping < 1
    restores convergence, but damping is an assumption about inertia that the
    original model does not contain.
    """
    c = np.asarray(c, dtype=float)
    n = c.size
    q = np.zeros(n)
    # Overflow here is not an error condition to be warned about -- it IS divergence, and
    # divergence is a documented outcome of this function that the isfinite check below
    # detects and reports. Left unsuppressed, numpy warns about an intermediate the very
    # next line already handles, which puts a RuntimeWarning in a passing test suite.
    with np.errstate(over="ignore", invalid="ignore"):
        for i in range(max_iter):
            Q_minus = q.sum() - q
            target = np.maximum(0.0, (a - c - b * Q_minus) / (2 * b))
            q_new = q + damping * (target - q)
            if not np.all(np.isfinite(q_new)):
                raise RuntimeError(f"tatonnement diverged at iteration {i}")
            if np.max(np.abs(q_new - q)) < tol:
                out = _summarise(a, b, c, q_new)
                out["iterations"] = i + 1
                return out
            q = q_new
    raise RuntimeError(f"tatonnement did not converge in {max_iter} iterations")


def _summarise(a: float, b: float, c: np.ndarray, q: np.ndarray) -> dict:
    Q = q.sum()
    p = a - b * Q
    share = q / Q if Q > 0 else np.zeros_like(q)
    elasticity = p / (b * Q) if Q > 0 else np.inf   # |dQ/dp * p/Q| for p = a - bQ
    return {
        "q": q,
        "Q": Q,
        "p": p,
        "profit": q * p - c * q,
        "share": share,
        "abs_elasticity": elasticity,
        "lerner": (p - c) / p,
        "hhi": float((share ** 2).sum()),
    }


def lerner_residual(res: dict) -> np.ndarray:
    """Check the markup identity asserted in the manuscript.

        (p - MC_i) / p  ==  s_i / |epsilon|

    Returns the elementwise residual. Should be zero to machine precision at
    equilibrium; this is a verification of the paper's equation, not an assumption
    baked into it.
    """
    return res["lerner"] - res["share"] / res["abs_elasticity"]


def solve_cournot(a: float, b: float, c) -> dict:
    """Cournot-Nash allowing corner solutions.

    The closed form assumes every firm produces. When a firm's marginal cost exceeds
    the price the remaining firms would set, its analytic output goes negative -- which
    means excluded, not loss-making. Standard remedy: iteratively drop the worst
    offender and re-solve on the surviving set.

    This is not a numerical nicety. It is the marginal pair from the manuscript's
    section on reservation prices: the last agent holding a unit and the first agent
    excluded. The exclusion boundary is an equilibrium object, and it belongs in the
    model rather than in a footnote.
    """
    c = np.asarray(c, dtype=float)
    active = np.ones(c.size, dtype=bool)

    while True:
        sub = c[active]
        m = sub.size
        if m == 0:
            raise ValueError("no firm can profitably produce at these costs")
        q_sub = (a + sub.sum() - (m + 1) * sub) / (b * (m + 1))
        if np.all(q_sub > 0):
            q = np.zeros(c.size)
            q[active] = q_sub
            out = _summarise(a, b, c, q)
            out["excluded"] = np.flatnonzero(~active).tolist()
            return out
        # drop the single worst offender, then re-solve
        idx = np.flatnonzero(active)
        active[idx[np.argmin(q_sub)]] = False
