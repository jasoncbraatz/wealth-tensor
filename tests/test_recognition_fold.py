"""The recognition port failed. These tests pin WHY, so nobody quietly un-fails it.

`RESULT-REG-001.md` records that `recognition_fold.py` is not a second layer: under the
order-reversing bijection m = -tau, p = -s, H = B it *is* `excess_demand.py`. The port was
force-fit, not form-fit (WT-042), and REG-001 returned no verdict.

The module stays in the tree because `docs/` is a public lab notebook and a buried
instrument teaches more than a deleted one. What must not happen is a future session
finding it, assuming it is a working second layer, and building on it. So the defect is
pinned by a test that fails if anyone makes the two modules diverge.
"""

import numpy as np
import pytest

from wealth_tensor.excess_demand import Market
from wealth_tensor.recognition_fold import RecognitionLedger


def _population(seed=20260811, n=200, r=80):
    rng = np.random.default_rng(seed)
    tau = rng.lognormal(3.0, 0.45, n)
    v = rng.lognormal(1.0, 0.8, n)
    booked = np.zeros(n, dtype=bool)
    booked[rng.choice(n, size=r, replace=False)] = True
    return tau, v, booked, r


def test_the_recognition_layer_IS_the_price_layer_under_a_sign_flip():
    """D1 of RESULT-REG-001. This test exists to keep a refuted claim refuted.

    If this ever fails, someone has given the two modules genuinely different content --
    which would be good news, and would mean REG-001 deserves a second look. Read
    RESULT-REG-001 §4 before celebrating: the port also needs to conserve the label count
    and drive its mechanism off the fold rather than off one half.
    """
    tau, _, booked, r = _population()
    market = Market(-tau, stock=r, holders=booked)

    grid = np.linspace(float(tau.min()), float(tau.max()), 201)[1:-1]
    for s in grid:
        assert RecognitionLedger.pending_at(tau, booked, s) == market.demand_at(-s)
        assert RecognitionLedger.reversible_at(tau, booked, s) == market.supply_at(-s)
        assert RecognitionLedger.net_pressure(tau, booked, s) == market.excess_demand(-s)


def test_the_static_identity_holds_and_both_halves_genuinely_move():
    """H1. Registered in REG-001 §4 as a near-trivial pass and INSUFFICIENT on its own.

    The second half of this test is the load-bearing half: an identity whose two terms
    never moved would be pinning nothing.
    """
    tau, _, _, r = _population()
    rng = np.random.default_rng(7)
    grid = np.linspace(float(tau.min()), float(tau.max()), 201)[1:-1]

    halves, folds = set(), set()
    for _ in range(12):
        b = np.zeros(tau.size, dtype=bool)
        b[rng.choice(tau.size, size=r, replace=False)] = True
        halves.add(tuple(RecognitionLedger.pending_at(tau, b, s) for s in grid))
        folds.add(tuple(RecognitionLedger.net_pressure(tau, b, s) for s in grid))
        for s in grid:
            assert (RecognitionLedger.net_pressure(tau, b, s)
                    == RecognitionLedger.structural_pressure(tau, r, s))

    assert len(folds) == 1, "the fold must not move with the labelling"
    assert len(halves) > 1, "if the halves do not move, the identity pins nothing"


def test_the_negative_control_reads_array_POSITION_and_is_therefore_not_a_control():
    """D2 of RESULT-REG-001, pinned by the only mutation that actually discriminates.

    ``tie_break='index'`` was documented as smuggling the labelling into the booking
    order. It does not -- it reads the item's position in the array, which is neither a
    unit property nor a label. The discriminating experiment is a **permutation of array
    order carrying (tau, v, booked) together**: a pure renaming of items that changes
    nothing physical. A rule reading unit properties must be invariant to it; a rule
    reading array position must not be.

    This test has now been wrong TWICE. v1 asserted that two identical runs agree, which
    is determinism. v2 compared ``pressure_trace``, which IS the fold and is invariant by
    construction -- so it compared two invariants with ``!=`` and asserted nothing. Both
    survived a mutant that makes the control identical to the treatment. v3 reads event
    magnitudes, which depend on the *values* of the booked items and therefore see
    composition. **Mutation-verified: the mutant that collapses the control into the
    treatment kills this test.** Anyone editing it must re-run that mutation.
    """
    tau, v, booked, _ = _population()
    scrutiny = np.linspace(float(tau.min()) * 0.6, float(tau.max()) * 1.05, 40)
    perm = np.random.default_rng(3).permutation(tau.size)

    def trace(rule, order):
        """Read the COMPOSITION of the outcome, not the fold.

        ``pressure_trace`` is the fold, invariant by construction -- comparing two of
        them with ``!=`` compares two invariants and asserts nothing. The first version
        of this test did exactly that and survived a mutant that made the control
        identical to the treatment. Event magnitudes read the *values* of the booked
        items, so they see composition; sorting undoes the permutation's relabelling.
        """
        led = RecognitionLedger(tau[order], v[order], booked=booked[order],
                                recognition_rate=0.10)
        out = led.run(scrutiny, tie_break=rule)
        return (out["event_periods"], out["event_magnitudes"])

    identity = np.arange(tau.size)
    assert trace("threshold", identity) == trace("threshold", perm), (
        "the real rule reads unit properties and must survive a renaming of items")
    assert trace("index", identity) != trace("index", perm), (
        "the control reads array position -- if it survived a renaming it would be "
        "reading unit properties too, and would control for nothing")
    assert trace("threshold", identity) != trace("index", identity), (
        "a control indistinguishable from the treatment is not a control")


def test_a_regime_with_no_events_must_not_be_reported_as_invariant():
    """The 4/21 < 4/11 lesson, pinned at the place it recurred.

    The first run of WT-066 reported ``H2a PASS`` from a regime with zero events: timing
    was invariant because there was no timing. This asserts that such a regime is
    identifiable as vacuous from the run output alone, so the script can refuse to score
    it. An assertion that cannot fail has not been passed.
    """
    tau, v, booked, _ = _population()
    scrutiny = np.linspace(float(tau.min()) * 0.6, float(tau.max()) * 1.05, 200)
    led = RecognitionLedger(tau, v, booked=booked, recognition_rate=0.40,
                            crisis_threshold=0.25)
    out = led.run(scrutiny)
    assert out["events"] == [], "expected the switch-off regime for these parameters"
    assert out["peak_pending_share"] < 0.25, "vacuity must be visible in the output"


def test_rejects_a_booked_set_that_contradicts_its_own_count():
    tau, v, booked, r = _population()
    with pytest.raises(ValueError):
        RecognitionLedger(tau, v, booked=booked, recognised_count=r + 1)


def test_rejects_an_out_of_range_recognition_rate():
    tau, v, _, r = _population()
    with pytest.raises(ValueError):
        RecognitionLedger(tau, v, recognised_count=r, recognition_rate=0.0)
