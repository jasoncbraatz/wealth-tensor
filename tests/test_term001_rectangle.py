"""TERM-001 · the adjective on §4.4's product, bound to the measurement that warrants it.

WHY THIS EXISTS
---------------
Paper III called the ASSUMED product [10, 40] x [3, 20] "the disclosed rectangle" at five
sites, while `RESULT-REG-009` measured S = 0.1391 against it -- 95 of 683 disclosed pairs
inside, 86.1 % of the disclosure outside. `wealthTensor-30` repaired the two sites
`REG-009` §12 named and the other five survived for seven sessions inside a pre-written
stanza that says there are four of them.

THE FAILURE THIS GUARD IS SHAPED AGAINST, WHICH IS A COUNT AND NOT A STRING
---------------------------------------------------------------------------
`patchkit` proves every anchor resolves EXACTLY once and writes nothing otherwise. It
cannot know the list is short. A four-anchor patch against a five-site defect reports
total success, leaves the fifth site untouched two hundred lines away, and every guard in
this repository stays green -- so a guard that asserted five presences would be satisfied
by the same short list that caused the defect. **This one asserts an ABSENCE and a
COUNT**: zero occurrences of the wrong phrase anywhere in the manuscript, and the
registration's stated site count equal to the length of the edit list. Absence is the only
assertion a short list cannot satisfy.

WHY IT SCANS THE MANUSCRIPT AND NOT THE REGISTRATION
-----------------------------------------------------
`RESULT-TERM-001.md` QUOTES the wrong phrase repeatedly -- naming the sentence it exists
to refuse is the strongest thing in the document. A forbidden-phrase scan pointed at it
would go red on its own witness, and both naive fixes are wrong: deleting the quotation
guts the document, deleting the phrase guts the guard. `-36` banked that shape. Here the
scan is scoped to the manuscript, where the phrase is asserted in the paper's own voice
and has no legitimate use, and the registration is read only for the two numerals it
declares -- with a carrier sentence specific enough that the document's other, correct
uses of "four sites", "two sites" and "three sites" are not mistaken for its subject.

WHY THE ADJECTIVE IS BOUND TO A MEASUREMENT AND NOT TO A WORD LIST
------------------------------------------------------------------
"asserted" is only the right word while 86.1 % of the disclosure really does fall outside
the rectangle. So the last check does not compare the manuscript to a constant: it reads S
out of `RESULT-REG-009` and recomputes the complement at test time. If that measurement is
ever removed, restated or drifts, the rename loses its warrant and this goes red -- rather
than the paper carrying a word whose justification has quietly left the repository. A
terminology guard that only checks spelling would pass forever over a term that had
stopped being true.

WHAT IT CANNOT SEE
------------------
It cannot see the phrase re-entering a sibling paper, a registration or a run log; those
are records by the ruling in §2 of the registration and are deliberately out of scope. It
cannot tell whether a SIXTH site exists that neither the stanza nor this session found --
only that the count the registration asserts and the list the edit performs are the same
number. And it cannot judge whether "asserted" is the best word, only that the paper is
not calling the product disclosed while its own §4.4 measures it otherwise.
"""
from __future__ import annotations

import pathlib
import re
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from wt101_edits_term001 import (  # noqa: E402
    EDITS,
    NUMERAL,
    PAPER,
    REGISTRATION,
    RESULT_REG_009,
    RIGHT_ADJ,
    WRONG_ADJ,
    counts_sentence,
    outside_share_sentence,
    phrase,
    sections_touched,
)


@pytest.fixture(scope="module")
def paper() -> str:
    return PAPER.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def registration() -> str:
    return REGISTRATION.read_text(encoding="utf-8")


# --------------------------------------------------------------------------------------
# 0 · the guard's own vacuity. An empty or inert edit list must FAIL, not pass over
#     nothing: a scan that finds nothing reads as coverage and is the one result this
#     repository will not accept silently.
# --------------------------------------------------------------------------------------
def test_the_edit_list_is_not_empty_and_every_entry_performs_the_rename():
    assert EDITS, "TERM-001's edit list is empty: nothing is guarded and this must be red"
    olds = [old for old, _, _ in EDITS]
    assert len(set(olds)) == len(olds), "two entries share an anchor"
    for old, new, label in EDITS:
        assert phrase(WRONG_ADJ) in old, f"{label}: anchor does not contain the wrong term"
        assert phrase(RIGHT_ADJ) in new, f"{label}: replacement does not contain the right term"
        assert old != new, f"{label}: the edit is inert"
        assert "\n" not in old, f"{label}: anchor spans a line break"


# --------------------------------------------------------------------------------------
# 1 · the absence. The assertion a short list cannot satisfy.
# --------------------------------------------------------------------------------------
def test_the_manuscript_never_calls_the_asserted_product_disclosed(paper):
    hits = [line for line in paper.split("\n") if phrase(WRONG_ADJ) in line]
    assert not hits, (
        f"paper III still says {phrase(WRONG_ADJ)!r} at {len(hits)} site(s):\n  "
        + "\n  ".join(h.strip()[:110] for h in hits)
    )


# --------------------------------------------------------------------------------------
# 2 · the count, with exactly one parse. The registration declares it; the list is it.
# --------------------------------------------------------------------------------------
def test_the_registration_states_the_number_of_sites_the_edit_performs(registration):
    expected = counts_sentence(len(EDITS), len(sections_touched()))
    assert expected in registration, (
        f"the registration does not carry {expected!r}. The edit list has "
        f"{len(EDITS)} site(s) across {len(sections_touched())} section(s) "
        f"({', '.join(sorted(sections_touched()))}); the document must say so, or one of "
        "the two was changed without the other."
    )
    # And it says it ONCE, so there is no second numeral to drift.
    pattern = re.compile(r"at (\w+) sites across (\w+) sections")
    found = pattern.findall(registration)
    assert len(found) == 1, f"the counts sentence occurs {len(found)} times, expected 1"
    assert found[0] == (NUMERAL[len(EDITS)], NUMERAL[len(sections_touched())])


# --------------------------------------------------------------------------------------
# 3 · every repaired span is present and unambiguous, so a later reflow that dissolves
#     an anchor is visible rather than silent.
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize("old,new,label", EDITS, ids=[e[2] for e in EDITS])
def test_each_repaired_span_occurs_exactly_once(paper, old, new, label):
    assert paper.count(new) == 1, (
        f"{label}: the repaired span occurs {paper.count(new)} times, expected 1"
    )


# --------------------------------------------------------------------------------------
# 4 · THE WARRANT. The rename is true only while the measurement is. Recomputed here from
#     RESULT-REG-009 rather than compared to a constant.
# --------------------------------------------------------------------------------------
def test_the_share_outside_the_rectangle_is_the_complement_of_the_measured_support(paper):
    reg009 = RESULT_REG_009.read_text(encoding="utf-8")
    s_hits = set(re.findall(r"\bS = (\d\.\d+)\b", reg009))
    assert len(s_hits) == 1, (
        f"RESULT-REG-009 states the support share {len(s_hits)} different ways: {s_hits}"
    )
    s = float(s_hits.pop())

    # The manuscript is hard-wrapped at 100 columns and this sentence straddles the wrap,
    # so every run of whitespace in the template matches a newline too. An anchor that
    # could not cross a line break is the one failure mode `patchkit`'s docstring says has
    # caused every missed anchor in this project.
    printed = re.search(
        r"\s+".join(
            re.escape(tok)
            for tok in outside_share_sentence("\x00PCT\x00").split(" ")
        ).replace(re.escape("\x00PCT\x00"), r"(\d+\.\d)"),
        paper,
    )
    assert printed, (
        "paper III no longer prints the share of the disclosure falling outside the "
        f"{RIGHT_ADJ} rectangle. The adjective's warrant is that share; without it the "
        "manuscript asserts a term nothing in the repository supports."
    )
    assert round((1.0 - s) * 100.0, 1) == float(printed.group(1)), (
        f"the manuscript prints {printed.group(1)}% outside the rectangle; "
        f"RESULT-REG-009's S = {s} makes it {round((1.0 - s) * 100.0, 1)}%"
    )
