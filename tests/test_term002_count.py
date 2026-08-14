"""The TERM-002 guard — the number the paper states is the length of the list it states it over.

WHY THIS EXISTS
---------------
`RESULT-TERM-002.md` records a defect that survived five sessions of grepping and one
review that named it correctly: §8 said the free-parameter move had been refused **five**
times and then enumerated **four**, and §8.1 and §A.2.4 repeated the five. Nothing noticed,
because the number was a NUMERAL IN PROSE — three occurrences, no arithmetic behind any of
them anywhere in `scripts/`, `tests/` or `src/`. `REVIEW-004` caught it on 2026-08-13 and
nothing was built from the catch, which is how a docs/ finding becomes a manuscript defect
with a paper trail.

So this file does not check wording. **It counts the list and asserts the prose agrees**,
in BOTH directions: a fifth instance added without renumbering goes red, and a renumbering
without a fifth instance goes red. That symmetry is the point. The prior art in this
repository — `test_pin001_code_state.py` — pins a sentence to the repository's git state;
this pins a sentence to a list four lines below it, which is the same move against a
smaller universe.

TWO NUMERALS, NOT ONE, AND WHY
------------------------------
The class has four members; three were refused and the fourth, §8.1's unmeasured φ, was
not. §8.1's sentence says "refused ... times in other costumes (§8) and should have refused
here", and §8.1's costume IS the fourth — so "other costumes" is the other three. §A.2.4
says the same of Λ, which is not in the list at all, so its other costumes are the four, of
which three were refused. The manuscript therefore states the CLASS count once, in §8 where
the list is, and the REFUSAL count at the two sites carrying the word *refused*. Both are
derived here from one parse, so they cannot drift apart.

THE WITNESS PROBLEM, AND HOW IT IS SIDESTEPPED
----------------------------------------------
Nothing here is retyped. The three repaired constructions are produced by the BUILDERS in
`scripts/wt100_edits_term002.py` — the script that performed the edit and the only place in
the repository where their wording is written down — and this file calls those builders
with counts it parses out of the manuscript. A guard carrying its own copy of "four" would
pass forever while the list grew: the defect this card is about, in miniature.

WHAT IT CANNOT DO
-----------------
It cannot tell whether an enumerated item is a genuine instance of the class; a fifth item
that is really the third one restated would satisfy every assertion here. It cannot see the
count asserted in a table row or a figure caption, since it looks only at the two remote
constructions and §8's paragraph. And it does not adjudicate II's ρ, which `REVIEW-004`
excluded on grounds this guard has no way to check.
"""

import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from wt100_edits_term002 import (  # noqa: E402
    CLASS_COUNT,
    CLASS_PARAGRAPH_OPENER,
    CONCEDED_COUNT,
    CONCESSION_MARK,
    ENUMERATION_OPENER,
    NUMERAL,
    REFUSED_COUNT,
    ROTTED,
    class_clause,
    reconciling_clause,
    remote_construction,
)

PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
RESULT_DOC = ROOT / "docs/preregistration/RESULT-TERM-002.md"


@pytest.fixture(scope="module")
def paper() -> str:
    return PAPER.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def class_paragraph(paper: str) -> str:
    """§8's class paragraph, unwrapped to one line so hard wrapping cannot hide a split."""
    i = paper.find(CLASS_PARAGRAPH_OPENER)
    assert i != -1, (
        f"{CLASS_PARAGRAPH_OPENER!r} is not in paper III. TERM-002's whole repair hangs "
        f"off this paragraph; if it was renamed, rename it in "
        f"scripts/wt100_edits_term002.py in the same commit."
    )
    j = paper.index("\n\n", i)
    return " ".join(paper[i:j].split("\n"))


@pytest.fixture(scope="module")
def enumerated_items(class_paragraph: str) -> list[str]:
    """The semicolon-separated instances §8 lists — the ONLY evidence for the number.

    Boundaries, both structural rather than lexical: the enumeration runs from the clause
    that opens it to the end of that sentence, and the reconciling clause is split off at
    its em dash. `§8.1` inside the list is safe because its period is not followed by a
    space.
    """
    _, _, region = class_paragraph.partition(ENUMERATION_OPENER)
    assert region, f"{ENUMERATION_OPENER!r} no longer opens §8's enumeration"
    sentence = region.split(". ", 1)[0]
    enumeration, dash, _ = sentence.rpartition(" — ")
    assert dash, (
        "§8's enumeration sentence no longer ends in the reconciling clause TERM-002 "
        "added. The class count and the refusal count are reconciled there and nowhere "
        "else in the manuscript."
    )
    return [item.strip() for item in enumeration.split("; ")]


# --------------------------------------------------------------------------------------
# The load-bearing half: the prose numerals ARE the arithmetic of the list, both ways.
# --------------------------------------------------------------------------------------

def test_the_class_numeral_is_the_length_of_the_list(class_paragraph, enumerated_items):
    expected = class_clause(len(enumerated_items))
    assert expected in class_paragraph, (
        f"§8 enumerates {len(enumerated_items)} instances and must therefore say "
        f"{expected!r}. It does not. This is TERM-002 recurring, and it fires in both "
        f"directions on purpose: if you ADDED an instance, renumber the prose in this "
        f"same commit; if you renumbered the prose, the list has not moved with it. "
        f"Items parsed: {enumerated_items}"
    )


def test_exactly_one_enumerated_instance_is_the_one_that_got_through(enumerated_items):
    conceded = [i for i in enumerated_items if CONCESSION_MARK in i]
    assert len(conceded) == CONCEDED_COUNT, (
        f"§8's list marks {len(conceded)} instance(s) with {CONCESSION_MARK!r}; TERM-002 "
        f"registered {CONCEDED_COUNT}. The ruling is that the instance which got through "
        f"stays in the list and the manuscript says which one it was — so if a second "
        f"concession is now enumerated, the refusal count below has changed too and both "
        f"numerals need re-deriving, not one."
    )
    assert conceded[0] == enumerated_items[-1], (
        "the conceded instance is no longer last in §8's list, but the reconciling "
        "clause names it by ordinal position. Move it back, or re-derive the ordinal."
    )


def test_the_refusal_numeral_is_the_members_minus_the_one_that_got_through(
    class_paragraph, enumerated_items
):
    members = len(enumerated_items)
    conceded = len([i for i in enumerated_items if CONCESSION_MARK in i])
    expected = reconciling_clause(members - conceded, members)
    assert expected in class_paragraph, (
        f"§8 lists {members} instances of which {conceded} was conceded, so the "
        f"reconciling clause must read {expected!r}. The class count and the refusal "
        f"count are stated in the same sentence precisely so they cannot drift apart."
    )


def test_the_refusal_numeral_appears_at_exactly_the_two_remote_sites(
    paper, enumerated_items
):
    members = len(enumerated_items)
    conceded = len([i for i in enumerated_items if CONCESSION_MARK in i])
    construction = remote_construction(members - conceded)
    assert paper.count(construction) == 2, (
        f"{construction!r} occurs {paper.count(construction)} times in paper III; "
        f"TERM-002 repaired exactly two sites, §8.1 and §A.2.4. A future edit that "
        f"repairs one and not the other must leave this red rather than leave the "
        f"manuscript quietly disagreeing with itself, which is how the original defect "
        f"lived for as long as it did."
    )
    assert paper.count("times in other costumes") == 2, (
        "a third 'times in other costumes' site has appeared and is not carrying the "
        "derived refusal count. Add it to the repair or remove it."
    )


def test_the_five_times_construction_is_gone_from_paper_III(paper):
    # Case-folded deliberately: the original defect occurred once sentence-initially
    # ("Refused five times across this programme") and twice mid-sentence, and a guard
    # that only saw the lower-case form would have missed a third of its own subject.
    lowered = paper.lower()
    assert ROTTED not in lowered, (
        f"{ROTTED!r} is back in paper III. It was the count the list never supported; "
        f"nothing in the manuscript is entitled to state a number for this class that "
        f"is not derived from §8's enumeration."
    )
    assert f"{NUMERAL[5]} times in other costumes" not in lowered


# --------------------------------------------------------------------------------------
# The small half: the edit script's declared counts and the registration still agree.
# --------------------------------------------------------------------------------------

def test_the_edit_scripts_declared_counts_are_internally_consistent(enumerated_items):
    assert REFUSED_COUNT == CLASS_COUNT - CONCEDED_COUNT
    assert CLASS_COUNT == len(enumerated_items), (
        f"scripts/wt100_edits_term002.py declares CLASS_COUNT = {CLASS_COUNT} and §8 now "
        f"enumerates {len(enumerated_items)}. The manuscript tests above are derived from "
        f"the parse and may well be green; this one exists so the script's own record of "
        f"what it found cannot rot silently behind them."
    )


def test_the_result_doc_registers_the_repair_it_performed():
    doc = RESULT_DOC.read_text(encoding="utf-8")
    assert ROTTED in doc, "the result doc must quote the claim it repaired"
    assert "REVIEW-004" in doc, (
        "the result doc must record that this was found a day before it was built — the "
        "distinguishing feature of this costume is the paper trail, not the error."
    )
    for numeral in (NUMERAL[CLASS_COUNT], NUMERAL[REFUSED_COUNT]):
        assert numeral in doc, (
            f"the result doc must state {numeral!r}: the two-numeral ruling is the one "
            f"amendment this session made to the card's pre-written stanza, and an "
            f"unregistered amendment is an unregistered decision."
        )
