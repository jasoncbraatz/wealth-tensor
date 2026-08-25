"""C17 · `REG-003` §7 — §4.4 *"may change one number and the sentences that carry it, and
may not reopen the argument."*

**THIS FILE IS A TRIPWIRE, NOT A GUARD.** It fires on the antecedent of a re-read and says
*go and read §4.4*; it never says a violation occurred. `CONSTRAINT-INVENTORY-001` §3.4
defines the class. `conftest.py` registers the marker.

WHY THIS ONE CANNOT BE A FREEZE
--------------------------------
C48 freezes §4.7 byte-for-byte (`test_reg012_sec6_sec47_frozen.py`) because `REG-012` §6
forbids *any* change to it. C17 is the harder shape: `REG-003` §7 **licenses** an edit —
one number, and the sentences that carry it — and forbids only the *argument* being
reopened. A byte freeze on §4.4 would go red every time the registration did exactly what
it registered, and a tripwire that fires when nothing happened is a tripwire that gets
deleted as a false alarm.

So the pin is over §4.4 **with every numeric literal masked**. A registered number moving —
0.0079, 11.5 %, 2.58, the ladder's cells — leaves the masked text identical and this file
silent. Prose changing shape does not.

WHAT THE MASK CANNOT SEE, STATED PLAINLY
-----------------------------------------
* **Section cross-references are numerals too.** `§4.2` masks to `§#.#`, so §4.4 re-pointing
  an argument from §4.2 to §4.6 is invisible here. Known, accepted, and the reason this is a
  tripwire on an antecedent rather than a guard on the constraint.
* **An argument can be reopened by numbers alone.** Flip the sign of the decomposition terms
  and the prose stands while the reasoning inverts. No masked digest can see that.
* **A rewritten carrying-sentence fires.** `REG-003` §7 permits it, so a red here is often a
  *licensed* edit. That is correct behaviour: the licensed edit is precisely the moment a
  reader has to ask whether the argument moved with the sentence, and this file exists to
  make somebody ask it out loud.

`CONSTRAINT-INVENTORY-001` C17 stays `recog: PROXY`, `machine: TRIPWIRE`, and **TRIPWIRE IS
NOT COVERAGE**: C17 is in cell (b) before this file and in cell (b) after it. Only FOR and
BINDS mean a constraint is guarded.
"""
from __future__ import annotations

import hashlib
import pathlib
import re

import pytest

pytestmark = pytest.mark.tripwire

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_003 = ROOT / "docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md"

#: `REG-003` §7's clause. The warrant.
CONSTRAINT = (
    "this registration may change one number and the sentences that carry it, "
    "and may not reopen the argument"
)

#: SHA-256 of §4.4 with every numeric literal masked.
#:
#: RE-PINNED at wealthTensor-105 (Pass C), and the reading is CARRYING SENTENCE, not
#: ARGUMENT REOPENED. Two sentences gained provenance and nothing else moved:
#:   * the sentence introducing α̂ now names the estimator (a censored geometric maximum
#:     likelihood on the registered sample's onset-to-charge intervals, right-censored at
#:     twenty quarters) at the point a reader first meets the value, instead of leaving it
#:     to §5.4 eight hundred lines on. PRE-002 keeps the attribution it had.
#:   * "the unregistered adverse cut" is glossed in place as a refit of the same sample with
#:     the 175 one-quarter events dropped; it had no referent in this manuscript until §5.4.
#: §4.4's argument is unchanged: the calibrated α still puts the whole asserted rectangle
#: outside the domain, the measured rate still puts it inside across the 95% interval, and
#: the admissible shares are the same numbers from the same runs. Nothing was added to the
#: argument, removed from it, or re-ordered within it. A C-d repair under
#: DEFINITION-OF-DONE-SHIP §2.5 — the fold was that the value arrived unevaluable, and the
#: repair moved the DEFINITION forward, not the section.
#: An earlier draft of this repair also restated n = 695 here; it was dropped rather than
#: declared, because a restated value is a second copy that can drift.
#: RE-PINNED AGAIN at wealthTensor-105, by that session's own adversarial verification, and
#: the reading is still CARRYING SENTENCE. The first cut put the estimator gloss a hundred
#: lines BELOW the table whose two measured columns are where a reader first meets the
#: value -- so it had not repaired the fold at all. The gloss moved to immediately above
#: the table and restates NO number (the table prints them); the sentence introducing
#: alpha-hat reverted, byte for byte, to the text REG-003 section 7's own guard requires,
#: with PRE-002's qualifier intact; and the unregistered label came back to the site that
#: reports 0.327, which REG-004 section 6 requires. The ARGUMENT is untouched throughout:
#: same rectangle, same domain, same admissible shares, same runs.
#: RE-PINNED AT wealthTensor-106 (Pass D). READING: CARRYING SENTENCE, and NO NUMBER MOVED
#: -- which is why this entry is longer than its predecessors. Pass D removed one clause from
#: the table preamble, "and both are worth having in hand before the table is read": document
#: navigation, not a claim about the world, and the C-b shape REVIEW-039 section 6.2 hands to
#: Pass D by name as Pass C's own residue. The rectangle, the domain, the admissible shares,
#: the two measured columns, the crossing rate and every figure in the table are byte-identical
#: across this edit; the masked digest moves because the mask covers numerals, not prose.
SEC_44_MASKED_SHA256 = "faad3cb054cc5f73b61ae9f19c7fc4d6ab39420c80dff5b7a5b64f282087ec47"

#: Sanity floor on the extractor, so a heading-regex change cannot silently pin "".
SEC_44_MIN_LINES = 100

_HEADING_44 = re.compile(r"^### 4\.4 · .*$", re.M)
_HEADING_45 = re.compile(r"^### 4\.5 · ", re.M)
#: Signed decimals with thousands separators — `2.58`, `−0.41`, `4,000`, `0.0079`.
NUMERAL = re.compile(r"[-−+]?\d[\d,]*(?:\.\d+)?")


def section_44(text: str) -> str:
    start = _HEADING_44.search(text)
    assert start, "§4.4's heading is gone from the manuscript"
    rest = text[start.start():]
    end = _HEADING_45.search(rest)
    assert end, "§4.5's heading is gone from the manuscript"
    return rest[: end.start()]


def masked(section: str) -> str:
    return NUMERAL.sub("#", section)


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def test_the_registration_still_says_this():
    flat = " ".join(REG_003.read_text(encoding="utf-8").split())
    assert CONSTRAINT in flat, (
        "REG-003 §7's clause about §4.4 is gone or restated. THIS TRIPWIRE HAS LOST ITS "
        "WARRANT — read the registration before trusting anything else in this file."
    )


def test_section_44_is_extractable_and_is_the_validity_region():
    section = section_44(PAPER.read_text(encoding="utf-8"))
    assert section.startswith("### 4.4 · The design has a validity region")
    assert len(section.splitlines()) >= SEC_44_MIN_LINES, "§4.4 extracted suspiciously short"
    assert "### 4.5" not in section


def test_sec_44_argument_prose_has_not_moved():
    found = digest(masked(section_44(PAPER.read_text(encoding="utf-8"))))
    assert found == SEC_44_MASKED_SHA256, (
        "TRIPWIRE · §4.4's PROSE MOVED IN A WAY A NUMBER CHANGE ALONE DOES NOT EXPLAIN. "
        "**THIS IS NOT A FAILURE.**\n"
        f"  pinned  {SEC_44_MASKED_SHA256}\n  current {found}\n\n"
        "GO AND READ §4.4 against REG-003 §7:\n"
        "  '§4.4 has been rewritten whole twice and is closed as an argument; this\n"
        "   registration may change one number and the sentences that carry it, and may\n"
        "   not reopen the argument.'\n"
        "Ask, as a reader: is this edit a sentence carrying a changed number, or is the\n"
        "ARGUMENT different?\n"
        "  CARRYING SENTENCE → licensed. Re-pin SEC_44_MASKED_SHA256 in the SAME commit\n"
        "        and name the number that moved in the commit message. A pin moved in a\n"
        "        later commit is a pin nobody reviewed.\n"
        "  ARGUMENT REOPENED → that is what REG-003 §7 forbids; the repair is §4.4, not\n"
        "        this file. It is Jason's call whether a re-registration is the right move."
    )


# ----------------------------------------------------------------------- non-vacuity


def test_a_number_change_alone_does_not_fire():
    """The whole design. If this fails the tripwire is a freeze wearing a mask."""
    section = section_44(PAPER.read_text(encoding="utf-8"))
    moved = section.replace("**0.0079**", "**0.0081**").replace("**2.58**", "**2.61**")
    assert moved != section, "the mutation did not mutate — `-37`: check the control moved"
    assert digest(masked(moved)) == SEC_44_MASKED_SHA256, (
        "VACUOUS AS A TRIPWIRE — a bare number change fires it, so every registered edit "
        "reads as a reopened argument and the next session learns to re-pin without "
        "reading. That is the failure mode CONSTRAINT-INVENTORY-001 §3.4 names."
    )


def test_a_prose_change_does_fire():
    section = section_44(PAPER.read_text(encoding="utf-8"))
    reopened = section.replace(
        "The natural expectation is that a confound of this kind adds noise to a ranking.",
        "The natural expectation is right: a confound of this kind adds noise to a ranking.",
    )
    assert reopened != section, "the mutation did not mutate"
    assert digest(masked(reopened)) != SEC_44_MASKED_SHA256, (
        "VACUOUS — rewriting §4.4's opening claim leaves the masked digest unchanged."
    )


def test_the_mask_masks_the_numbers_the_section_actually_carries():
    """`-43`: assert the conjunction. A mask that missed one family would be a false green
    on every edit that touched it."""
    for form in ("0.0079", "11.5%", "4,000", "−0.41", "+1.58", "2.58", "0.00600"):
        assert NUMERAL.sub("#", form).strip("%") == "#", f"NUMERAL misses {form!r}"
    assert NUMERAL.sub("#", "the ranking inverts") == "the ranking inverts", (
        "NUMERAL is eating prose, which would make the digest blind to argument changes"
    )
