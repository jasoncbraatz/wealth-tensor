"""Severity for assertions: a guard is not a guard until a world has made it fire.

WHY THIS EXISTS
---------------
This project has now shipped the same defect four times across three sessions, in four
costumes that look nothing like each other:

  1. `assert 4.0/21 < 4.0/11 < 4.0/7 < 4.0/3`  - four rational constants, no model output
  2. H2b "magnitude varies"                     - probability-1 under ANY mechanism
  3. `tie_break="index"` as a negative control  - index is a per-item attribute, so the
                                                  control was indistinguishable from the
                                                  treatment it was controlling for
  4. `pressure_trace != pressure_trace`         - compares two invariants
  5. "raise EVERYONE 20%" as a control          - rank-preserving by construction, so the
                                                  single answer was forced by monotonicity
                                                  and not by the allocation being irrelevant
  6. 25 uniform allocations as 25 experiments   - 25 draws from a distribution the
                                                  population already fixes

In EVERY case the code was correct and the WORLD could not produce a falsifying
observation. WT-069 mutates the code; all six survive every code mutant, because the
defect is upstream of the code.

The lesson has been written down four times and mechanised zero times. Writing it a fifth
time would itself be an instance of it. So it is mechanised here.

THE NAME
--------
It was called "the 4/21 < 4/11 defect" - named after its FIRST COSTUME, which is exactly
why it is not recognised in its fourth. Renamed here after its behaviour:

    THE PHANTOM TAG. In baseball, the phantom tag is the fielder credited with an out he
    never actually made - he never touched the bag. A phantom-tag assertion is a guard
    credited with catching something it never touched. The question "did the fielder touch
    the bag?" translates exactly: DID THE ASSERTION TOUCH A VALUE THAT COULD HAVE BEEN
    OTHERWISE?

THE RULE
--------
Every check ships a WITNESS: a callable returning a state under which the condition is
FALSE. The witness is executed. If it does not make the condition fail, the check is
VACUOUS and the run dies. If you cannot construct a witness, you have learned in thirty
seconds that your guard is worthless.

This is Mayo's severity requirement applied one level below where this project has been
applying it. A test passes severely only if it would very probably have FAILED had the
claim been false. This programme has used severity language for pre-registrations and
never once for an assertion. All six instances above have severity zero.

AND THE PAYOFF THAT IS NOT OBVIOUS
----------------------------------
For instances 5 and 6, constructing the witness does not merely DETECT the defect - it
hands you the CORRECT EXPERIMENT. "Show me a population-defined perturbation giving more
than one interval" IS the random-subset control. "Show me an allocation with volume
outside 85-103" IS the comonotone coupling. Both took an adversarial agent and two hours
to find in wealthTensor-08. The witness requirement would have produced them in ten
minutes, for free.

USAGE
-----
    from severity import check, DEFINITIONAL, summary

    check("z is invariant across allocations",
          len(observed) == 1,
          witness=lambda: len(observed_under_a_wedge))     # must be != 1

    check("|H| equals the stock", h.sum() == stock, witness=DEFINITIONAL(
          "true by the constructor's own validation; there is no admissible world in "
          "which it is false, and the check exists to catch a refactor, not a claim"))

    summary()   # prints counts and exits non-zero if anything was vacuous
"""

from __future__ import annotations

from dataclasses import dataclass, field


class VacuousGuard(Exception):
    """Raised when a check's witness fails to make the condition false."""


@dataclass
class _Definitional:
    reason: str


def DEFINITIONAL(reason: str) -> _Definitional:
    """Declare a check definitional rather than empirical.

    An escape hatch that leaves a mark. Definitional checks are COUNTED and PRINTED by
    summary(), so a script that quietly reclassifies its way out of severity is visible
    in its own output. The reason string is mandatory and is printed.
    """
    if not reason or len(reason) < 30:
        raise VacuousGuard(
            "DEFINITIONAL needs a real reason (>=30 chars) saying why NO admissible "
            "world falsifies this. 'obvious' is not a reason.")
    return _Definitional(reason)


@dataclass
class _Tally:
    severe: int = 0
    definitional: list = field(default_factory=list)
    failures: list = field(default_factory=list)


_TALLY = _Tally()


def check(label: str, condition: bool, witness=None) -> None:
    """Assert `condition`, and PROVE the assertion could have failed.

    witness: a zero-argument callable returning a value that is FALSY, or that differs
             from the passing value - i.e. the same computation performed on a world
             where the claim is false. It is executed. If it does not come back false,
             the guard is a phantom tag and the run dies.
             Or DEFINITIONAL("<why no world falsifies this>").
    """
    if witness is None:
        raise VacuousGuard(
            f"PHANTOM TAG: '{label}' has no witness. Every guard ships a world in which "
            f"it goes red, or declares itself DEFINITIONAL with a reason.")

    if not condition:
        _TALLY.failures.append(label)
        print(f"  FAIL       {label}")
        raise SystemExit(f"ASSERTION FAILED: {label}")

    if isinstance(witness, _Definitional):
        _TALLY.definitional.append((label, witness.reason))
        print(f"  DEFN       {label}")
        return

    got = witness()
    if got:
        _TALLY.failures.append(label)
        print(f"  VACUOUS    {label}")
        raise SystemExit(
            f"PHANTOM TAG: '{label}' passed, but so did its witness (returned {got!r}). "
            f"The guard did not touch a value that could have been otherwise. Either the "
            f"witness is not really a falsifying world, or the check cannot fail. Both "
            f"are findings; neither is a pass.")

    _TALLY.severe += 1
    print(f"  SEVERE     {label}")


def summary(title: str = "SEVERITY") -> None:
    """Print the tally. Non-zero exit if anything was vacuous."""
    print("\n" + "-" * 78)
    print(f"{title}: {_TALLY.severe} severe · {len(_TALLY.definitional)} definitional · "
          f"{len(_TALLY.failures)} failed/vacuous")
    for label, reason in _TALLY.definitional:
        print(f"  definitional — {label}\n      because: {reason}")
    print("-" * 78)
    if _TALLY.failures:
        raise SystemExit(1)
