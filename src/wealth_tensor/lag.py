"""Virtual wealth as a transfer function on real wealth.

The claim: the financial reporting layer is not a neutral window onto physical assets. It
is a *filter*. Some changes pass through immediately; others are deferred, accumulate
unrecognised, and are eventually released at once. Under this reading a crisis is not an
external shock -- it is the filter's accumulated error being delivered in a single period.

Layers
------
Real     E(t)  physical capacity, decaying at an entropy rate, offset by maintenance
Reported C(t)  the balance-sheet abstraction
Gap      E - C the information the reporting layer owes the world but has not delivered
Coupling L(t)  = C/E, the work-to-financial coefficient of the dual tensor

Mechanism
---------
Effective decay is the entropy rate net of maintenance::

    E(t+1) = E(t) * (1 - d * (1 - maintenance_ratio))

Of each true change, a share phi is *observable* -- announced capex, disclosed impairment,
a write-down someone had to sign. It reaches the reported layer at once. The remaining
(1 - phi) is deferred maintenance and technical debt: real, accruing, and absent from the
statements. It accumulates in the gap and is recognised only at rate alpha per period::

    C(t+1) = C(t) + phi * dE + alpha * gap(t)

When the unrecognised gap exceeds a threshold share of real wealth the deferral becomes
unsustainable and the reported layer snaps to the real one. That discontinuity is the
crisis, and its magnitude is exactly the information that had been withheld.

The asymmetry is the point
--------------------------
phi is not a fudge factor. It is the *observability* of the degradation, and it makes the
model's sharpest prediction: **lag and crisis severity scale with (1 - phi)**. A pure-delay
model would be falsified by markets pricing an announced transition ahead of the physical
change; this one is not, because announced change has phi near 1 and passes straight
through. The reporting layer leads on what is disclosed and lags on what is deferred.
"""

from __future__ import annotations

import numpy as np


class LayeredFirm:
    """A firm with a real layer, a reported layer, and a filter between them."""

    def __init__(self, initial_wealth=100.0, entropy_rate=0.05, maintenance_ratio=0.6,
                 observable_share=0.3, recognition_rate=0.05, crisis_threshold=0.25):
        if not 0.0 <= observable_share <= 1.0:
            raise ValueError("observable_share must lie in [0, 1]")
        if not 0.0 < recognition_rate <= 1.0:
            raise ValueError("recognition_rate must lie in (0, 1]")
        self.e0 = float(initial_wealth)
        self.d = float(entropy_rate)
        self.maint = float(maintenance_ratio)
        self.phi = float(observable_share)
        self.alpha = float(recognition_rate)
        self.theta = float(crisis_threshold)

    def effective_decay(self) -> float:
        """Entropy net of maintenance. Zero when maintenance is complete."""
        return self.d * (1.0 - self.maint)

    def run(self, periods=400) -> dict:
        E = np.empty(periods + 1)
        C = np.empty(periods + 1)
        gap = np.empty(periods + 1)
        E[0] = C[0] = self.e0
        gap[0] = 0.0
        crises = []
        decay = self.effective_decay()

        for t in range(periods):
            E[t + 1] = E[t] * (1.0 - decay)
            dE = E[t + 1] - E[t]
            C[t + 1] = C[t] + self.phi * dE + self.alpha * gap[t]
            gap[t + 1] = E[t + 1] - C[t + 1]

            if E[t + 1] > 0 and abs(gap[t + 1]) / E[t + 1] > self.theta:
                crises.append({"period": t + 1, "magnitude": float(abs(gap[t + 1])),
                               "reported_before": float(C[t + 1]),
                               "reported_after": float(E[t + 1])})
                C[t + 1] = E[t + 1]
                gap[t + 1] = 0.0

        with np.errstate(divide="ignore", invalid="ignore"):
            lam = np.where(E > 0, C / E, np.nan)

        return {"real": E, "reported": C, "gap": gap, "coupling": lam,
                "crises": crises, "n_crises": len(crises)}


def variance_suppression(res: dict) -> float:
    """std of reported changes over std of real changes, measured BETWEEN crises.

    The smoothing claim is a statement about ordinary periods, not about the whole series.
    Measured across the full path the number exceeds 1, because the snap discontinuities
    dominate -- see `variance_concentration`, which is the more interesting quantity.
    """
    dE, dC = np.diff(res["real"]), np.diff(res["reported"])
    mask = np.ones(dE.size, dtype=bool)
    for c in res["crises"]:
        i = c["period"] - 1
        if 0 <= i < mask.size:
            mask[i] = False
    if mask.sum() < 3 or dE[mask].std() == 0:
        return np.nan
    return float(dC[mask].std() / dE[mask].std())


def variance_concentration(res: dict) -> float:
    """Share of total squared reported change occurring in crisis periods.

    The model's real claim about volatility is not that the reporting layer reduces it.
    It is that the layer *relocates* it: long quiet stretches during which deferred
    information accrues invisibly, punctuated by periods in which all of it arrives at
    once. Zero means volatility is evenly spread; near one means essentially all of the
    reported movement happens in the snaps.
    """
    dC = np.diff(res["reported"])
    total = float((dC ** 2).sum())
    if total == 0:
        return 0.0
    crisis = 0.0
    for c in res["crises"]:
        i = c["period"] - 1
        if 0 <= i < dC.size:
            crisis += float(dC[i] ** 2)
    return crisis / total


def recognition_lag(res: dict, max_lag=200) -> int:
    """Lag maximising cross-correlation of real and reported changes.

    To isolate the filter this should be measured on a path with the crisis mechanism
    disabled (`crisis_threshold=np.inf`); otherwise the snap timing truncates the usable
    window and the number reports the crisis schedule rather than the filter.
    """
    end = res["crises"][0]["period"] if res["crises"] else len(res["real"]) - 1
    dE, dC = np.diff(res["real"][: end + 1]), np.diff(res["reported"][: end + 1])
    if dE.size < 5:
        return 0
    dE, dC = dE - dE.mean(), dC - dC.mean()
    best, best_lag = -np.inf, 0
    for k in range(min(max_lag, dE.size - 2)):
        a, b = dE[: dE.size - k], dC[k:]
        denom = np.linalg.norm(a) * np.linalg.norm(b)
        if denom == 0:
            continue
        c = float(np.dot(a, b) / denom)
        if c > best:
            best, best_lag = c, k
    return best_lag


def deferred_information(res: dict) -> float:
    """Integral of the unrecognised gap over the path.

    This is the quantity WT-024 identifies with the drift of the dual tensor's coupling
    coefficient: the information the reporting layer owes and has not delivered.
    """
    return float(np.abs(res["gap"]).sum())
