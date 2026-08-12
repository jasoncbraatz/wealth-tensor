#!/usr/bin/env python3
"""WT-077 · tail index of the levied Kesten process — the computation Road One rests on.

Run BEFORE any claim is written down. If it comes back negative, the truncation-vs-scaling
story goes in Abandoned Approaches and nothing is lost but an afternoon.

SETUP, stated so the assumptions are checkable rather than buried.
-----------------------------------------------------------------
The levy is a pure transfer (verified to machine precision in RedistributionEconomy.run,
`transfer_error`), so aggregate wealth grows at the same rate with or without it. Write the
per-agent map for LARGE w, where the flat wage and the per-capita rebate are negligible
relative to w -- which is exactly the regime that sets the tail:

    stock levy, rate r :   A(eta) = (1 - r) * (1 + eta)
    flow  levy, rate r :   A(eta) = 1 + eta - r * rho * max(eta, 0)

Normalise by aggregate growth, a(eta) = A(eta) / (1 + mu). The Kesten tail index is the
alpha > 1 solving E[a^alpha] = 1. Note E[a] = 1 - kappa < 1, so alpha = 1 is not a root and
the process is stationary (E[log a] < 0 by Jensen).

THE CLAIM UNDER TEST: a stock levy SCALES the multiplier and a flow levy TRUNCATES its upper
tail, so at equal kappa the flow levy yields a LARGER alpha (thinner tail, more compression).
And at r = 1 the flow multiplier satisfies A = 1 + min(eta, 0) <= 1, hence a <= 1/(1+mu) < 1
almost surely, hence E[a^alpha] is strictly decreasing and BELOW 1 for every alpha > 1 --
NO ROOT, so no power-law tail exists at all.

That last one is analytic. This script's job is to confirm it numerically and to produce the
alphas for the cases where a root does exist.

FALSIFIERS -- any of these kills the claim:
  * at matched kappa the stock levy yields a LARGER alpha than the flow levy
  * the r=1 flow case admits a finite root
  * alpha does not order monotonically with r within a base
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

MU, SIGMA = 0.05, 0.20          # model defaults, redistribution.py
# Deterministic grid rather than Gauss-Hermite: hermegauss(400) overflows its own weights.
# +/- 12 sigma at 400k points; the truncation error is far below the 1e-10 root tolerance.
ETA = np.linspace(MU - 12 * SIGMA, MU + 12 * SIGMA, 400_001)
_PDF = norm.pdf(ETA, MU, SIGMA)
PROB = _PDF / _PDF.sum()


def E(f):
    return float(np.sum(PROB * f(ETA)))


# Wealth is clamped at zero in the simulation (`np.maximum(w + gain + wage, 0.0)`), so the
# multiplier is clamped here too. It matters only for eta < -1, i.e. beyond -5.25 sigma.
def A_stock(r):
    return lambda e: np.maximum((1.0 - r) * (1.0 + e), 0.0)


def A_flow(r, rho=1.0):
    return lambda e: np.maximum(1.0 + e - r * rho * np.maximum(e, 0.0), 0.0)


def kappa(Afn):
    """Share of aggregate wealth moved per assessment: 1 - E[A]/(1+mu)."""
    return 1.0 - E(Afn) / (1.0 + MU)


def tail_index(Afn, hi=60.0):
    """alpha > 1 with E[a^alpha] = 1.

    Returns (alpha, ess-sup a).  alpha is None when a <= 1 almost surely -- no power law
    exists at all -- and "unstable" when there is no levy, because then E[a] = 1, the
    process has no stationary distribution, and it condenses.  That is the `none` row of
    the paper's own table (Gini 0.994, unbounded), so it is a check on the setup rather
    than a missing result.
    """
    a = lambda e: Afn(e) / (1.0 + MU)                      # noqa: E731
    sup = float(np.max(a(ETA)))
    if sup <= 1.0:
        return None, sup
    if kappa(Afn) <= 1e-12:
        return "unstable", sup
    g = lambda al: np.log(E(lambda e: np.maximum(a(e), 1e-300) ** al))  # noqa: E731
    if g(hi) < 0:
        return float("inf"), sup                            # decays but never returns to 1
    return brentq(g, 1.0 + 1e-9, hi, xtol=1e-10), sup


def eta_plus_closed_form():
    z = MU / SIGMA
    return MU * norm.cdf(z) + SIGMA * norm.pdf(z)


if __name__ == "__main__":
    print(f"mu={MU}  sigma={SIGMA}")
    ep = eta_plus_closed_form()
    print(f"E[eta+] closed form = {ep:.6f}   quadrature = {E(lambda e: np.maximum(e,0)):.6f}")
    print(f"kappa_flow(r=1) predicted = r*E[eta+]/(1+mu) = {ep/(1+MU):.6f}\n")

    rows = []
    for label, Afn in (
        [("none",            lambda e: 1.0 + e)]
        + [(f"stock r={r:<5}", A_stock(r)) for r in (0.025, 0.05, 0.10, 0.20)]
        + [(f"flow  r={r:<5}", A_flow(r)) for r in (0.025, 0.10, 0.25, 0.50, 1.00)]
    ):
        k = kappa(Afn)
        al, sup = tail_index(Afn)
        rows.append((label, k, al, sup))
        a_txt = ("NO POWER LAW (ess-sup a < 1)" if al is None
                 else al if isinstance(al, str)
                 else "inf" if al == float("inf") else f"{al:.4f}")
        print(f"{label:16s} kappa={k:8.5f}   ess-sup a={sup:7.4f}   alpha={a_txt}")

    print("\n--- THE TEST: matched budget, both bases ---")
    for target in (0.0250, 0.0500, 0.1000):
        # stock: kappa = r exactly.  flow: solve r numerically.
        r_s = target
        r_f = brentq(lambda r: kappa(A_flow(r)) - target, 1e-9, 1.0) \
            if kappa(A_flow(1.0)) >= target else None
        a_s, _ = tail_index(A_stock(r_s))
        as_txt = a_s if isinstance(a_s, str) else f"{a_s:.4f}"
        if r_f is None:
            print(f"kappa={target:.4f}  stock r={r_s:.4f} alpha={as_txt}   "
                  f"flow: UNREACHABLE (max kappa_flow={kappa(A_flow(1.0)):.5f})")
            continue
        a_f, sup_f = tail_index(A_flow(r_f))
        af_txt = "NO POWER LAW" if a_f is None else f"{a_f:.4f}"
        verdict = ("FLOW THINNER (claim holds)" if a_f is None or a_f > a_s
                   else "STOCK THINNER -- CLAIM REFUTED")
        print(f"kappa={target:.4f}  stock r={r_s:.4f} alpha={as_txt}   "
              f"flow r={r_f:.4f} alpha={af_txt}   -> {verdict}")

    print("\n--- variance of log a: does the flow levy cut it and the stock levy not? ---")
    base_v = E(lambda e: (np.log((1+e)/(1+MU)))**2) - E(lambda e: np.log((1+e)/(1+MU)))**2
    print(f"unlevied Var[log a] = {base_v:.6f}")
    for label, Afn in (("stock r=0.10", A_stock(0.10)), ("flow  r=0.10", A_flow(0.10)),
                       ("flow  r=1.00", A_flow(1.00))):
        lg = lambda e: np.log(np.maximum(Afn(e), 1e-300) / (1 + MU))   # noqa: E731
        v = E(lambda e: lg(e)**2) - E(lg)**2
        print(f"{label}: Var[log a] = {v:.6f}   (kappa={kappa(Afn):.5f})")
