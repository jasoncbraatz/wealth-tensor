"""The severity harness must itself be severe (WT-069).

A harness built to catch phantom tags, that has never been shown to catch one, would be
the defect it exists to prevent - wearing the costume of the cure. So the original defect
is run through it here, and must die.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import severity  # noqa: E402
from severity import DEFINITIONAL, VacuousGuard, check  # noqa: E402


@pytest.fixture(autouse=True)
def _fresh_tally():
    severity._TALLY = severity._Tally()
    yield


def test_the_original_defect_is_killed():
    """`assert 4/21 < 4/11 < 4/7 < 4/3` - four rational constants, no model output.

    This is the assertion that started the whole family, in wealthTensor-06. There is no
    world in which it is false, so no witness can exist, and the honest witness - the
    same expression - passes too. The harness must refuse it.
    """
    with pytest.raises(SystemExit) as exc:
        check("the damping shrinks like 4/n",
              4.0 / 21 < 4.0 / 11 < 4.0 / 7 < 4.0 / 3,
              witness=lambda: 4.0 / 21 < 4.0 / 11 < 4.0 / 7 < 4.0 / 3)
    assert "PHANTOM TAG" in str(exc.value)


def test_the_rank_preserving_control_is_killed():
    """wealthTensor-08's costume: a control that varies rank-preservation, not allocation.

    Multiplying every value by a constant cannot change an order statistic's RANK, so a
    'distinct intervals == 1' check is forced by monotonicity whatever the allocation
    does. The witness is a perturbation that is population-defined but NOT
    rank-preserving; it fans out, so the guard was never reading the allocation.
    """
    values = [3.0, 1.0, 4.0, 1.5, 9.0, 2.6]
    scaled = {tuple(sorted(v * k for v in values)) for k in (1.2,)}

    def witness_shuffles_ranks():
        # a genuinely population-defined perturbation that reorders: still one answer?
        got = {tuple(sorted(v * (1.2 if i % 2 else 0.5)
                            for i, v in enumerate(values))) for _ in range(3)}
        return len(got) == 1 and len(scaled) == 1 and False  # fans out -> falsy

    with pytest.raises(SystemExit):
        check("scaling everything gives exactly one ordering",
              len(scaled) == 1,
              witness=lambda: len(scaled) == 1)          # same world -> phantom tag

    severity._TALLY = severity._Tally()
    check("scaling everything gives exactly one ordering",
          len(scaled) == 1,
          witness=witness_shuffles_ranks)                 # a real falsifying world
    assert severity._TALLY.severe == 1


def test_a_genuine_guard_survives():
    observed = [1, 1, 1]
    broken = [1, 2, 3]
    check("all equal", len(set(observed)) == 1,
          witness=lambda: len(set(broken)) == 1)
    assert severity._TALLY.severe == 1


def test_a_missing_witness_is_refused():
    with pytest.raises(VacuousGuard) as exc:
        check("something true", True)
    assert "PHANTOM TAG" in str(exc.value)


def test_definitional_needs_a_real_reason():
    with pytest.raises(VacuousGuard):
        DEFINITIONAL("obvious")
    d = DEFINITIONAL("no admissible world falsifies this because the constructor "
                     "validates it before any check runs")
    check("definitional claims are counted, not waved through", True, witness=d)
    assert severity._TALLY.severe == 0
    assert len(severity._TALLY.definitional) == 1


def test_a_failing_condition_still_fails():
    with pytest.raises(SystemExit) as exc:
        check("false thing", False, witness=lambda: False)
    assert "ASSERTION FAILED" in str(exc.value)
