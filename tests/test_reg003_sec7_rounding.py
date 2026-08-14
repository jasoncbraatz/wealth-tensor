"""`REG-003` §7 is a REPORTING constraint, and reporting constraints are greppable.

    **α̂ is the recognition rate of the quantity PRE-002's instrument identifies**, under
    PRE-002's onset bridge. It is not "the" recognition rate of US GAAP, and **no sentence
    anywhere may round it to that.**

A registration carries reporting constraints as well as predictions. Predictions get an
instrument, a `RESULT-*` and a test; **constraints have historically got nothing**, and
this one was violated at six sites for two days — including in the abstract — of a paper
whose one unusual credibility asset is that its registrations are public and honoured.
`SCOUT-001` T1 found five of the six by hand. This file is the machine that finds the
seventh, whenever somebody writes it.

WHAT IT DOES NOT DO, STATED SO NOBODY READS IT AS MORE THAN IT IS
-----------------------------------------------------------------
It does not ban the phrase *"the recognition rate."* That phrase is the correct English
for **the model's α**, an unmeasured structural parameter, and the manuscript uses it that
way at seven sites which round nothing because they attach the phrase to no estimate. A
guard that banned the phrase outright would fail every legal site and push the paper
toward vagueness — the failure mode `defensive_count.py`'s own lexicon comment warns
about, arriving in a second costume.

So the rule is predication, not vocabulary: **a unit of text violates §7 when it names a
recognition rate, carries a MEASUREMENT of α̂, and carries no qualifier.** That is exactly
the move §7 forbids and exactly nothing else.

THE CONTROL, AND WHY THIS FILE WOULD BE WORTHLESS WITHOUT IT
-------------------------------------------------------------
`-37`: *a mutation that does not mutate reports your guard as weak.* `-40`: *a green case
that is green because the state was already there is the same defect as a red case that is
red for the wrong reason.* A linter asserting zero violations against a document somebody
just cleaned is green for free. So `test_the_linter_sees_the_defect_it_was_written_for`
feeds it the six real pre-edit sentences, verbatim from `paper-III.md` at `0b26a8a`, and
requires all six to be flagged; `test_the_legal_uses_are_not_flagged` feeds it the real
legal sentences and requires none of them to be. Red at six, green at zero, on text this
file does not get to choose.

AND THE WARRANT
---------------
`test_the_registration_still_says_this` asserts §7's sentence is still in `REG-003`. If
the constraint is ever deleted or restated, this guard loses its warrant, and it says so
rather than quietly enforcing a rule the repository no longer holds — the `TERM-001`
pattern, where an adjective's justification had to stay measurable for the adjective to
keep its licence.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_003 = ROOT / "docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md"

#: The governed noun phrase.
NOUN = re.compile(r"recognition rate", re.I)

#: The governed SYMBOL: a bare α, meaning the model's structural parameter. `α̂`, `α_eff`
#: and `α_ser` are other quantities with their own names and are not it. §9's limitation 4
#: violated §7 through this door and not through the noun's — *"α is no longer in that
#: list: §5.4 estimates it at 0.408 per year"* names no recognition rate at all, and a
#: linter watching only the noun phrase reports the manuscript clean. **Six sites, two
#: doors, and the hand-audit that found five of them found all five through one door.**
BARE_ALPHA = re.compile(r"(?<![\w_̂])α(?![̂_])")

#: α̂ written out. A unit that names the estimate as the estimate has not rounded it, which
#: is why the symbol rule below stands down when this appears — the paper contrasting α
#: with α̂ in one breath (§4.4's table header, §5.4's memorylessness sentence, the §7
#: ledger's domain row) is §7 being *honoured*, at the three sites that look most like
#: violations to a cruder rule.
ALPHA_HAT = re.compile(r"α̂")

#: A unit "carries a measurement" when it puts α̂'s value, α̂ itself, or §5.4's act of
#: measuring next to the noun. Deliberately narrow: 0.437 and 0.476 are α_eff and 0.435 is
#: a reciprocal mean lag, and §4.10 discusses all three as *distinct* quantities, which is
#: the paper doing the right thing and must not be flagged.
MEASUREMENT = re.compile(
    r"α̂"
    r"|0\.40[0-9]"
    r"|0\.41 per year"
    r"|order of magnitude above the calibration"
    r"|§5\.4 (?:measures|estimates)",
)

#: The qualifiers that satisfy §7. `peak-to-charge` is PRE-002's own registered name for
#: the interval; the other two are §7's own wording.
QUALIFIER = re.compile(
    r"peak-to-charge"
    r"|PRE-002's instrument identifies"
    r"|PRE-002's instrument dates",
)

#: §7's sentence, as the registration spells it. The warrant.
CONSTRAINT = "no sentence anywhere may round it to that"


def units(text: str):
    """Sentences, plus table rows as their own units.

    A table row is not prose — `defensive_count.py` skips them for that reason — but §7
    governs *sentences anywhere*, and one of the six real sites was a row label in the §7
    survivals ledger. A splitter that inherited the prose-only convention would have
    missed it, which is how a convention borrowed from one guard defeats another.
    """
    for block in re.split(r"\n\s*\n", text):
        if block.lstrip().startswith("|"):
            for row in block.splitlines():
                if row.strip():
                    yield row.strip()
            continue
        flat = " ".join(block.split())
        for sentence in re.split(r"(?<=[.!?]) +(?=[A-Z*_\"'(§])", flat):
            if sentence.strip():
                yield sentence.strip()


#: α̂'s value, as the manuscript prints it. The symbol rule keys on the VALUE rather than
#: on the act of measuring, because "α is estimated" is a true sentence and "α is 0.408" is
#: the rounding.
ALPHA_HAT_VALUE = re.compile(r"0\.40[0-9]|0\.41 per year")


def rounds(unit: str) -> bool:
    """§7's forbidden move, and exactly it.

    Two doors, because the manuscript used both:

    * **the noun phrase** — "the recognition rate" predicated of a measurement of α̂, with
      no qualifier saying *whose* recognition rate. Five of the six real sites.
    * **the symbol** — α̂'s value attached to a bare α, the model's parameter, in a unit
      that never writes α̂. The sixth.
    """
    if QUALIFIER.search(unit):
        return False
    if NOUN.search(unit) and MEASUREMENT.search(unit):
        return True
    return bool(BARE_ALPHA.search(unit)
                and ALPHA_HAT_VALUE.search(unit)
                and not ALPHA_HAT.search(unit))


def violations(text: str) -> list[str]:
    return [u for u in units(text) if rounds(u)]


# ---------------------------------------------------------------------------------------
# The six real sites, verbatim from paper-III.md at 0b26a8a — the commit before wt102 ran.
# Hard-wraps flattened, because `units()` flattens; nothing else touched.
# ---------------------------------------------------------------------------------------
PRE_EDIT_SITES = [
    # abstract
    "The same registered events establish it: **the recognition rate is 0.41 per year "
    "against a calibration of 0.05**, so the disclosed lives lie inside the model's domain, "
    "and the hazard rises with the age of the gap rather than staying constant as the model "
    "assumes.",
    # §4.4
    "On the registered sample the recognition rate is **α̂ = 0.408 per year**, 95% interval "
    "[0.383, 0.432].",
    # §4.9
    "§5.4 measures the recognition rate and, in the same fit, rejects the shape the model "
    "assumes: discrete Weibull k̂ = 1.210.",
    # §5.4's bolded lead — the site SCOUT-001 graded compliant, because it graded the
    # paragraph and §7 governs the sentence.
    "**The recognition rate is 0.41 per year, and the calibration was low by an order of "
    "magnitude.**",
    # §7 survivals ledger — a table row.
    "| **The recognition rate is an order of magnitude above the calibration** | censored "
    "geometric MLE on 695 registered events | any cut returning a rate near the swept 0.05 "
    "| **α̂ = 0.408/yr** [0.383, 0.432] |",
    # §9 limitation 4
    "α is no longer in that list: §5.4 estimates it at 0.408 per year on the registered "
    "sample, against the 0.05 swept through the body.",
]

#: Real sentences that name a recognition rate and round NOTHING. A linter that flags
#: these is the ban-the-phrase guard this file exists not to be.
LEGAL_SITES = [
    "The disclosed lives also fix the model's domain, and they fix it tightly: the deferral "
    "measure exists only where the recognition rate exceeds the decay rate.",
    "The two **R** columns are the world the standards describe, at the recognition rate "
    "calibrated here and at the one §5.4 goes on to measure.",
    "Any comparative static that holds α_eff fixed while moving δ is using the wrong "
    "derivative, and a single recognition rate quoted for a cross-section of asset lives "
    "misstates one end of it.",
    "**Three recognition rates now live in this paper and they are three different "
    "quantities.**",
    "That made the recognition rate, not the ordering, the quantity to establish first — "
    "and §5.4 establishes it.",
    # The three sites a noun-phrase-blind symbol rule flags and must not: each writes α and
    # α̂ in one breath, which is the paper drawing §7's distinction rather than collapsing
    # it. They are here because the first cut of this linter flagged all three, and a guard
    # tuned until it is quiet is worth nothing unless the sites it went quiet ON are named.
    "| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** at α = 0.05, the calibration | **R** at "
    "α̂ = 0.408, measured (§5.4) | R at a common δ |",
    "**The longer a gap has been open, the likelier it is to close** — which is the "
    "opposite of the memorylessness a single α encodes, and it means α̂ is an average over "
    "a window and not a constant of the technology.",
    "| **The *asserted* rectangle lies outside the model's domain *at the calibrated "
    "rate*** | useful lives spanning disclosure practice against α = 0.05 | **0%** "
    "admissible at α = 0.05; **0.974** of the disclosed pairs at the measured α̂ = 0.408 |",
]


def test_the_registration_still_says_this():
    flat = " ".join(REG_003.read_text(encoding="utf-8").split())
    assert CONSTRAINT in flat, (
        "REG-003 §7's constraint is gone or restated. This guard has lost its warrant; "
        "read the registration before trusting anything else in this file."
    )


@pytest.mark.parametrize("site", PRE_EDIT_SITES, ids=range(len(PRE_EDIT_SITES)))
def test_the_linter_sees_the_defect_it_was_written_for(site):
    """RED at six. Without this the zero below is green for free."""
    assert violations(site) == [site]


@pytest.mark.parametrize("site", LEGAL_SITES, ids=range(len(LEGAL_SITES)))
def test_the_legal_uses_are_not_flagged(site):
    """The model's α keeps its English."""
    assert violations(site) == []


def test_the_manuscript_rounds_nowhere():
    found = violations(PAPER.read_text(encoding="utf-8"))
    assert found == [], (
        f"REG-003 §7 violated at {len(found)} site(s) — a sentence attaches a measurement "
        f"of α̂ to an unqualified 'recognition rate':\n  " + "\n  ".join(found)
    )
