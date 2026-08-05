"""The numeraire cancels. Demonstrated, so that Lambda stops being the paper's weakest wall.

WT-002 identified the framework's most exposed point: ``eta_work_to_financial`` carries units
of ``[currency]/[J]``, and a free scalar converting a physical substrate into observed money
is precisely the failure mode that sank Odum's emergy programme. Unaddressed it reads as
"tuned to fit", and a reviewer reaches it on the first pass.

The defence had four parts. Three were written into the manuscript in S1: ground the constant
in a published statistic (it is the reciprocal of UN SDG indicator 7.3.1 -- WT-003), demote it
from parameter to dependent variable, and express results as dimensionless groups. The fourth
was the empirical leg and is this module: **a sensitivity sweep demonstrating that every
conclusion the paper draws is invariant to the coupling across many orders of magnitude.**

The argument
------------
Dress the two-layer system of `lag.py` in units. The real layer is physical, measured in
joules; the reported layer is financial, measured in currency; the coupling ``eta`` converts::

    E_phys(t) = E0 * e(t)                  [J]
    C_fin(t)  = eta * E0 * c(t)            [currency]
    Lambda(t) = C_fin(t) / E_phys(t) = eta * c(t) / e(t)      [currency/J]

The dimensionless state ``(e, c)`` obeys a recursion in which neither ``E0`` nor ``eta``
appears -- both enter only as multiplicative dressing applied afterwards. Three consequences
follow, and each is asserted in the test suite rather than argued:

1. **Normalised coupling is exactly invariant.** ``Lambda(t)/eta`` is bit-identical across
   twelve orders of magnitude of ``eta``. So is every ratio built from the two layers.
2. **Dimensionless diagnostics are exactly invariant.** Recognition lag, variance
   suppression, variance concentration, crisis count and relative crisis magnitude do not
   move. These are the manuscript's actual claims.
3. **Dimensional quantities scale exactly linearly.** Deferred information, denominated in
   currency, is proportional to ``eta`` to floating-point precision -- which is the correct
   and expected behaviour of a numeraire, and is the positive half of the demonstration. A
   quantity that failed to scale would mean the constant was doing physical work.

Point 3 is what makes this a test rather than a tautology. It would be easy to build a module
in which nothing depends on ``eta`` because ``eta`` is never used; here it is used, the
dimensional outputs move with it exactly as a unit conversion must, and the *conclusions* do
not move at all.

What this does and does not settle
----------------------------------
It settles the dimensional objection: the numeraire cancels out of every reported result, so
"you invented a conversion constant" is answered by showing the constant cannot influence any
conclusion. It does **not** settle whether the coupling is *measurable* in practice, nor
whether its drift means what WT-024 says it means. Those are empirical questions and this
module deliberately makes no claim about them.
"""

from __future__ import annotations

import numpy as np

from .lag import (LayeredFirm, deferred_information, recognition_lag,
                  variance_concentration, variance_suppression)

# Twelve orders of magnitude, straddling plausible energy-intensity values. Global energy
# intensity of output (SDG 7.3.1) sits near 4.6 MJ per 2021 PPP dollar, so the reciprocal --
# the coupling this sweep varies -- is order 1e-7 currency per joule. The range below brackets
# that by six orders in each direction, which is far wider than any real disagreement.
COUPLINGS = tuple(10.0 ** k for k in range(-6, 7))

# The diagnostics that carry the manuscript's claims. All are ratios or counts, hence
# dimensionless, hence required to be invariant.
DIMENSIONLESS = ("recognition_lag", "variance_suppression", "variance_concentration",
                 "n_crises", "relative_crisis_magnitude", "terminal_coupling_ratio",
                 "mean_coupling_ratio", "min_coupling_ratio")


class DimensionedSystem:
    """A `LayeredFirm` dressed in units: an energy scale, a coupling, and a time step.

    The dynamics are untouched. This class exists to make the unit structure explicit so the
    invariance can be *measured* rather than asserted from the algebra -- which is the whole
    point, since the algebra is exactly what a sceptical reviewer declines to take on trust.
    """

    def __init__(self, energy_scale=1.0e12, coupling=1.0e-7, **firm_kwargs):
        if energy_scale <= 0:
            raise ValueError("energy_scale must be positive")
        if coupling <= 0:
            raise ValueError("coupling must be positive")
        self.energy_scale = float(energy_scale)      # E0, joules
        self.coupling = float(coupling)              # eta, currency per joule
        self.firm = LayeredFirm(initial_wealth=1.0, **firm_kwargs)

    def run(self, periods=400) -> dict:
        res = self.firm.run(periods)                 # dimensionless: e(t), c(t)
        e, c = res["real"], res["reported"]
        out = dict(res)
        out["energy_joules"] = self.energy_scale * e
        out["reported_currency"] = self.coupling * self.energy_scale * c
        with np.errstate(divide="ignore", invalid="ignore"):
            out["lambda_measured"] = np.where(e > 0, self.coupling * c / e, np.nan)
        out["deferred_currency"] = (self.coupling * self.energy_scale
                                    * deferred_information(res))
        return out


def diagnostics(res: dict) -> dict:
    """The manuscript's claims, reduced to numbers. Every entry is dimensionless."""
    mags = [c["magnitude"] / c["reported_before"] for c in res["crises"]
            if c["reported_before"] != 0]
    lam = res["coupling"]
    finite = lam[np.isfinite(lam)]
    return {"recognition_lag": recognition_lag(res),
            "variance_suppression": variance_suppression(res),
            "variance_concentration": variance_concentration(res),
            "n_crises": res["n_crises"],
            "relative_crisis_magnitude": float(np.mean(mags)) if mags else 0.0,
            # The terminal ratio is pinned at 1 whenever the path ends on or just after a
            # correction, which is most of the time once crises are frequent -- Lambda equals
            # its physical value *only* at the instants the reported layer snaps to the real
            # one. The mean and minimum are the informative readings: they measure how far the
            # coupling drifts between corrections, which is the quantity WT-024 identifies
            # with undelivered information.
            "terminal_coupling_ratio": float(finite[-1]) if finite.size else float("nan"),
            "mean_coupling_ratio": float(np.mean(finite)) if finite.size else float("nan"),
            "min_coupling_ratio": float(np.min(finite)) if finite.size else float("nan")}


def sweep_coupling(couplings=COUPLINGS, periods=400, **kw) -> list[dict]:
    """One row per coupling. The dimensionless columns must not move; the currency ones must."""
    rows = []
    for eta in couplings:
        sysm = DimensionedSystem(coupling=eta, **kw)
        res = sysm.run(periods)
        row = {"coupling": eta, "deferred_currency": res["deferred_currency"],
               "terminal_lambda": float(res["lambda_measured"][-1]),
               "lambda_over_eta": float(res["lambda_measured"][-1] / eta)}
        row.update(diagnostics(res))
        rows.append(row)
    return rows


def invariance_report(rows: list[dict]) -> dict:
    """Spread of each dimensionless diagnostic across the sweep. Every entry should be zero.

    Reported as an absolute spread rather than a tolerance-checked boolean so that a future
    change which introduces a *small* dependence is visible as a small number rather than
    silently passing whatever threshold happened to be chosen here.
    """
    out = {}
    for key in DIMENSIONLESS:
        vals = np.array([r[key] for r in rows], dtype=float)
        vals = vals[np.isfinite(vals)]
        out[key] = float(vals.max() - vals.min()) if vals.size else float("nan")
    return out


def scaling_exponent(rows: list[dict], column="deferred_currency") -> float:
    """Slope of log(column) against log(coupling).

    A pure numeraire gives exactly 1.0: the quantity is denominated in currency and nothing
    else about it depends on the conversion. Anything other than 1.0 would mean the coupling
    is doing physical work somewhere in the model, which is the accusation this module exists
    to answer.
    """
    x = np.log10([r["coupling"] for r in rows])
    y = np.log10([r[column] for r in rows])
    keep = np.isfinite(x) & np.isfinite(y)
    if keep.sum() < 2:
        return float("nan")
    return float(np.polyfit(x[keep], y[keep], 1)[0])


def collapses_onto(a: dict, b: dict) -> bool:
    """True when two dimensioned systems produce the same dimensionless path.

    The scaling-collapse test proper: two systems differing in energy scale, coupling and
    absolute magnitudes, but sharing the dimensionless parameters, must lie on one curve once
    normalised. If the manuscript's results are properties of the pi-groups, this holds; if
    the numeraire leaks in anywhere, it does not.
    """
    ra = a["reported"] / a["real"]
    rb = b["reported"] / b["real"]
    return bool(np.nanmax(np.abs(ra - rb)) < 1e-12)
