"""`REG-012` §7 · **the shifted band count is REFUSED, not merely unperformed** — and the
guard that was filed under it could not tell those two states apart.

WHY THIS FILE EXISTS
--------------------
`CONSTRAINT-INVENTORY-001` C49 named `tests/test_reg012_band_edge_phase.py` as this
constraint's machine. That file's relevant assertion is `assert not _threshold_reads(doc)`
— an **absence**: the result may not name any of the ways a band count is read in this
repository. It is a good assertion and it binds the wrong limb. Both of the states
`REG-012` §7 distinguishes have zero band counts in them:

    merely unperformed :  no count present, no refusal declared
    refused            :  no count present, refusal declared, warrant named

An absence guard has the same truth value in both. `-44` deleted every refusal sentence
from `RESULT-REG-012-band-edge-phase.md` and the suite stayed green — the document went
silent about the measurement it declined, which is the exact state the registration wrote
the word *merely* to exclude, and nothing noticed.

THE PAIRED-GUARD SHAPE (`-42`'s whitespace lesson, one domain over)
--------------------------------------------------------------------
`-42` found a re-wrap guard that certified no character had moved and was blind by
construction to line breaks, and the repair was a **pair**: identity for the characters,
a structural assertion for the breaks. Same shape here. The absence limb stays where it
is, in `test_reg012_band_edge_phase.py`; this file owns the **presence** limb, and
`test_the_absence_limb_still_exists` binds the two together so the pair cannot be
silently halved by a later session tidying one file.

WHAT A REFUSAL IS, MECHANICALLY
--------------------------------
Three things, and they fail separately because they fail for different reasons:

  1. the document declines the measurement **in its own voice** — not inside a blockquote.
     A document that quotes the registration's prohibition has reported the rule; it has
     not made the refusal. (`-33`'s tell: a guard must scan assertions, not quotations.)
  2. the refusal **names its warrant** — R5, or the construction document that carries it.
     A refusal with no warrant is a preference.
  3. the registration **still carries the rule**. If `REG-012` §7 loses the sentence, this
     file reports a LOST WARRANT — *this rule no longer applies, retire me* — and not a
     violation. (`-42`'s conditional-constraint lesson: different failures, different
     messages.)

WHAT IT CANNOT DO
-----------------
It cannot judge whether the refusal is *sincere*, and it cannot see a refusal made in a
document other than this one. It also cannot check the thing C49's row is really about at
manuscript scope — the manuscript is silent on the shifted count, and silence is what the
absence limb already covers. This guard watches the `RESULT-*` document, which is where
the estate chose to put the speech act.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
REG_012 = ROOT / "docs/preregistration/REG-012-band-count-edge-phase.md"
RESULT = ROOT / "docs/preregistration/RESULT-REG-012-band-edge-phase.md"
ABSENCE_LIMB = ROOT / "tests/test_reg012_band_edge_phase.py"

#: The registration sentence that warrants this file. Its loss is a LOST WARRANT, not a pass.
RULE = "refused, not merely unperformed"

#: The absence limb's assertion, in the file that owns it. Quoted, not imported, because
#: what must not vanish is the assertion — importing a helper would survive its deletion.
ABSENCE_ASSERTION = "assert not _threshold_reads(doc)"

#: A refusal verb applied to the measurement. `refus*` alone is too loose: the document
#: uses it about other things, and `-43`'s prefix lesson (`unregistered` contains
#: `registered`) says to bound the token rather than substring-match it.
REFUSAL = re.compile(
    r"\b(?:is\s+)?refus(?:ed|es|al)\b(?:(?!\.).){0,120}?"
    r"(?:merely\s+unperformed|unperformed|recount|re-edged band count|band count)",
    re.IGNORECASE,
)
#: The same move stated as a licence denial rather than a refusal verb.
DENIAL = re.compile(
    r"does not license the measurement|not a permit to recount", re.IGNORECASE
)

#: R5 is the warrant the refusal rests on.
WARRANT = re.compile(
    r"\bR5\b|CONSTRUCTION-REG-009", re.IGNORECASE
)


def _own_voice(text: str) -> list[str]:
    """Lines the document asserts, with blockquotes dropped.

    A blockquote is how this estate reproduces someone else's sentence. Reporting a
    prohibition is not performing a refusal, and the difference is one `>`.
    """
    return [ln for ln in text.split("\n") if not ln.lstrip().startswith(">")]


def _refuses(lines: list[str]) -> list[str]:
    return [ln for ln in lines if REFUSAL.search(ln) or DENIAL.search(ln)]


def _names_warrant(lines: list[str]) -> list[str]:
    return [ln for ln in lines if WARRANT.search(ln)]


@pytest.fixture(scope="module")
def result_text() -> str:
    return RESULT.read_text(encoding="utf-8")


@pytest.fixture()
def compliant_text(result_text: str) -> str:
    """The document, when it is compliant.

    The three fixtures below mutate the real document to prove the detectors are not
    vacuous, which presupposes something to mutate. On a document that is ALREADY
    violating they would each fail with `fixture is broken`, turning one defect into
    four red lines and burying the one that names it. `-39`'s tell says to assert the
    exact failure; the same discipline says a detector self-test skips rather than
    piles on.
    """
    if not _refuses(_own_voice(result_text)):
        pytest.skip(
            "the document carries no refusal — see "
            "test_the_refusal_is_declared_and_not_merely_absent, which is the failure"
        )
    return result_text


# --------------------------------------------------------------------------- warrant


def test_the_registration_still_carries_the_rule() -> None:
    """LOST WARRANT check. If `REG-012` §7 drops the sentence, retire this file."""
    text = REG_012.read_text(encoding="utf-8")
    assert RULE in text, (
        f"LOST WARRANT — {REG_012.name} no longer contains {RULE!r}. This is not a "
        "violation: the rule this file guards may have been retired. Read §7, then "
        "either restore the sentence or delete this file and C49's row."
    )


def test_the_absence_limb_still_exists() -> None:
    """The pair. This file is the presence half and is incomplete on its own."""
    src = ABSENCE_LIMB.read_text(encoding="utf-8")
    assert ABSENCE_ASSERTION in src, (
        f"HALF A PAIR — {ABSENCE_LIMB.name} no longer contains {ABSENCE_ASSERTION!r}. "
        "`REG-012` §7 needs both limbs: no count performed (there) AND the refusal "
        "declared (here). One without the other grades a silence as a refusal, or a "
        "refusal as a count."
    )


# --------------------------------------------------------------------------- presence


def test_the_refusal_is_declared_and_not_merely_absent(result_text: str) -> None:
    hits = _refuses(_own_voice(result_text))
    assert hits, (
        f"MERELY UNPERFORMED — {RESULT.name} reports no band count and says nothing "
        "about declining to compute one. `REG-012` §7 distinguishes a refusal from a "
        "silence, and the absence guard in test_reg012_band_edge_phase.py is green in "
        "both worlds. Restore the sentence that declines the re-edged count."
    )


def test_the_refusal_is_the_documents_own_words(result_text: str) -> None:
    everywhere = _refuses(result_text.split("\n"))
    own = _refuses(_own_voice(result_text))
    assert not (everywhere and not own), (
        "QUOTED, NOT ASSERTED — every refusal sentence in "
        f"{RESULT.name} sits inside a blockquote. Reproducing the registration's "
        "prohibition reports the rule; it does not perform the refusal."
    )


def test_the_refusal_names_its_warrant(result_text: str) -> None:
    lines = _own_voice(result_text)
    assert _refuses(lines), "precondition: no refusal to check (see the test above)"
    assert _names_warrant(lines), (
        f"UNWARRANTED REFUSAL — {RESULT.name} declines the measurement without naming "
        "R5 or `CONSTRUCTION-REG-009`. A refusal that cites nothing is a preference, "
        "and a later session cannot tell whether it was registered in advance."
    )


# ----------------------------------------------------------------------- non-vacuity
#
# The predicate is a CONJUNCTION — no count performed AND a refusal declared — so the
# fixtures have to move each conjunct separately (`-43`'s fourth tell: asserting that one
# half fires nowhere is a false-alarm generator). Every fixture below is the real
# document with one thing changed.


def test_stripping_the_refusal_leaves_the_merely_unperformed_state(compliant_text: str) -> None:
    """The state the registration wrote `merely` to exclude. Must be detectable."""
    stripped = "\n".join(
        ln for ln in compliant_text.split("\n")
        if not (REFUSAL.search(ln) or DENIAL.search(ln))
    )
    assert not _refuses(_own_voice(stripped)), (
        "VACUOUS — the refusal detector still fires on a document with every refusal "
        "sentence removed. It is matching something else."
    )


def test_blockquoting_the_refusal_is_not_a_refusal(compliant_text: str) -> None:
    quoted = "\n".join(
        ("> " + ln if (REFUSAL.search(ln) or DENIAL.search(ln)) else ln)
        for ln in compliant_text.split("\n")
    )
    assert _refuses(quoted.split("\n")), "fixture is broken: the sentences vanished"
    assert not _refuses(_own_voice(quoted)), (
        "VACUOUS — the own-voice filter does not distinguish a quotation from an "
        "assertion, so the guard would accept a document that only reports the rule."
    )


def test_dropping_the_warrant_is_detectable(compliant_text: str) -> None:
    unwarranted = "\n".join(
        ln for ln in compliant_text.split("\n") if not WARRANT.search(ln)
    )
    lines = _own_voice(unwarranted)
    assert _refuses(lines), (
        "fixture is broken: removing warrant lines also removed every refusal, so this "
        "fixture cannot isolate the warrant limb"
    )
    assert not _names_warrant(lines), (
        "VACUOUS — the warrant detector still fires with every R5 line removed."
    )


def test_the_registration_rule_check_is_not_vacuous() -> None:
    text = REG_012.read_text(encoding="utf-8").replace(RULE, "PERFORMED AND REPORTED")
    assert RULE not in text, (
        "VACUOUS — the LOST WARRANT check cannot see the sentence leaving the file."
    )
