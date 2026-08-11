"""Recognition as a fold over units, and the label set that is supposed to cancel.

This module is the second layer of the P3 port registered in
``docs/preregistration/REG-001-p3-second-layer.md``. It exists to answer one question and
it is written so that the answer can be *no*.

The question
------------
``excess_demand.py`` shows that in a unit-demand market the allocation cancels from the
difference of the two schedules: ``z(p) = #{m_i > p} - S`` at every non-reservation price.
That is Wicksteed (1910), Bk II Ch. IV, and this project claims no priority in it.

What is at issue here is whether the same cancellation survives a change of layer into a
setting with two structures a market does not have:

* the label set is **endogenous** -- what is on the books is produced by the model's own
  history, not handed to it as data;
* recognition is **aggregate-coupled** -- items are booked at a rate applied to the total
  pending pool, so no item's fate is a function of that item alone.

Neither has an analogue in a market where the allocation is exogenous. If the invariance
survives both, the identity is portable. If it does not, it is not, and REG-001 §4 H3
says to report that rather than repair it.

Setup
-----
N items, each with a recognition threshold ``tau_i`` -- the scrutiny at which it must be
booked -- and a magnitude ``v_i``, the value it carries onto the books when it is. A
booked set ``B`` records what is currently recognised.

At scrutiny ``s``:

    an unbooked item is *pending* if       tau_i < s     (overdue, not yet recognised)
    a booked item is *reversible* if       tau_i > s      (booked ahead of its threshold)

so the two halves are properties of the pair (threshold, current booking) evaluated at s,
exactly as demand and supply are properties of (reservation price, current holding)
evaluated at p.

The fold
--------
``net_pressure(s) = #{tau_i < s} - R``, where R is the current booked count. The booked
set partitions at s into those above it and those below it, so it enters the two counts
with opposite signs and cancels -- at every s, not merely where the pressure is zero.

What this module does NOT demonstrate
-------------------------------------
REG-001 §4 registers in advance that the static identity is a **near-trivial** pass and is
**not sufficient** to claim a second instantiation of P3. The partition argument is the
price layer's argument with the nouns swapped. Only the endogenous, aggregate-coupled
dynamics discriminate, and only the *magnitude* results say anything the count does not.

The count is a fold over units. The magnitude is not. That asymmetry is the object here,
and it is the derivation of the one thing Wicksteed asserted without proving -- that the
partition "does affect the amount of business done" while leaving the price alone.
"""

from __future__ import annotations

import numpy as np


class RecognitionLedger:
    """Items with thresholds and magnitudes, a booked set, and a filter between them."""

    def __init__(self, thresholds, magnitudes, booked=None, recognised_count=None,
                 recognition_rate=0.25, crisis_threshold=0.25, rng=None):
        self.tau = np.asarray(thresholds, dtype=float)
        self.v = np.asarray(magnitudes, dtype=float)
        if self.tau.shape != self.v.shape:
            raise ValueError("thresholds and magnitudes must have the same shape")
        self.n = self.tau.size
        if not 0.0 < recognition_rate <= 1.0:
            raise ValueError("recognition_rate must lie in (0, 1]")
        self.alpha = float(recognition_rate)
        self.theta = float(crisis_threshold)

        if booked is None:
            if recognised_count is None:
                raise ValueError("supply either booked or recognised_count")
            r = int(recognised_count)
            if not 0 <= r <= self.n:
                raise ValueError("recognised_count out of range")
            rng = np.random.default_rng() if rng is None else rng
            booked = np.zeros(self.n, dtype=bool)
            if r:
                booked[rng.choice(self.n, size=r, replace=False)] = True
        booked = np.asarray(booked, dtype=bool)
        if recognised_count is not None and booked.sum() != int(recognised_count):
            raise ValueError("booked set does not match recognised_count")
        self.booked0 = booked.copy()

    # --- the two "halves", each a reading of the same tau, differing only by the labels ---

    @staticmethod
    def pending_at(tau, booked, s: float) -> int:
        """Unbooked items whose threshold has been passed: they are overdue."""
        return int(np.sum(~booked & (tau < s)))

    @staticmethod
    def reversible_at(tau, booked, s: float) -> int:
        """Booked items whose threshold has not been passed: they are premature."""
        return int(np.sum(booked & (tau > s)))

    @classmethod
    def net_pressure(cls, tau, booked, s: float) -> int:
        return cls.pending_at(tau, booked, s) - cls.reversible_at(tau, booked, s)

    @staticmethod
    def structural_pressure(tau, recognised_count: int, s: float) -> int:
        """The fold: a function of the threshold population and the booked COUNT alone."""
        return int(np.sum(tau < s)) - int(recognised_count)

    # --- the discriminating part: endogenous, aggregate-coupled labelling ---

    def run(self, scrutiny_path, magnitude_trigger=True, tie_break="threshold") -> dict:
        """Evolve the booked set under the model's own dynamics.

        Each period the pending pool is booked at rate ``alpha`` applied to the pool as a
        whole -- an item's fate is therefore not a function of that item alone. Ties are
        broken by threshold (most overdue first), which is a property of units and not of
        labels; breaking them by index would smuggle the labelling back in through the
        ordering and is exactly the move this test exists to detect.

        ``tie_break="index"`` does exactly that, deliberately. It is the **negative
        control**: a rule that reads the labels rather than the units, under which the
        invariance MUST break. A test suite that cannot distinguish it from the real rule
        cannot detect failure at all, and would be a guard incapable of firing -- the
        defect this project shipped once already and does not intend to ship twice.

        A recognition event fires when the unrecognised share exceeds ``theta``, at which
        point the whole pending pool is booked at once. ``magnitude_trigger`` selects
        whether that share is measured in value (as ``lag.py`` measures its gap) or in
        count -- the two are reported separately because REG-001 predicts they differ.
        """
        booked = self.booked0.copy()
        total_v = float(self.v.sum())
        events = []
        pressure_trace = []
        share_trace = []

        for t, s in enumerate(scrutiny_path):
            pending = ~booked & (self.tau < s)
            pressure_trace.append(int(pending.sum())
                                  - int(np.sum(booked & (self.tau > s))))

            n_pending = int(pending.sum())
            if n_pending:
                if magnitude_trigger:
                    share = float(self.v[pending].sum()) / total_v
                else:
                    share = n_pending / self.n
                share_trace.append(share)

                if share > self.theta:
                    events.append({"period": t, "scrutiny": float(s),
                                   "count": n_pending,
                                   "magnitude": float(self.v[pending].sum())})
                    booked |= pending
                    continue

                # aggregate-coupled partial recognition: rate applied to the whole pool
                k = int(np.ceil(self.alpha * n_pending))
                idx = np.flatnonzero(pending)
                if tie_break == "threshold":
                    order = idx[np.argsort(self.tau[idx], kind="stable")]
                elif tie_break == "index":
                    order = idx
                else:
                    raise ValueError("tie_break must be 'threshold' or 'index'")
                booked[order[:k]] = True

            # reversal of prematurely booked items, at the same aggregate rate
            reversible = booked & (self.tau > s)
            n_rev = int(reversible.sum())
            if n_rev:
                j = int(np.ceil(self.alpha * n_rev))
                ridx = np.flatnonzero(reversible)
                if tie_break == "threshold":
                    rorder = ridx[np.argsort(-self.tau[ridx], kind="stable")]
                else:
                    rorder = ridx
                booked[rorder[:j]] = False

        return {"events": events,
                "peak_pending_share": max(share_trace) if share_trace else 0.0,
                "event_periods": tuple(e["period"] for e in events),
                "event_magnitudes": tuple(round(e["magnitude"], 9) for e in events),
                "event_counts": tuple(e["count"] for e in events),
                "pressure_trace": tuple(pressure_trace),
                "final_recognised": int(booked.sum())}
