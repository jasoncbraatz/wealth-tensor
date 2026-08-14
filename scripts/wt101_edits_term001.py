"""TERM-001 · "the disclosed rectangle" at five sites, over a product nothing disclosed.

Registered first in `docs/preregistration/RESULT-TERM-001.md`, committed alone at
`c0c0814` and pushed before this script existed on disk. The find: paper III names the
ASSUMED product [10, 40] x [3, 20] after the disclosure at five sites, while
`RESULT-REG-009` measures S = 0.1391 against it -- 95 of 683 disclosed pairs inside, so
86.1 % of the disclosure outside. The adjective states the opposite of the manuscript's
own measurement, printed six lines above the first offending site.

WHY FIVE AND NOT THE STANZA'S FOUR
----------------------------------
The repair has been pre-written since `wealthTensor-31` and carried unchanged through
five handoffs. It names four sites by line number -- 964, 996, 1123, 1573 -- and all four
are live, drifted to 976, 1008, 1135 and 1591. The fifth is in §4.4, the section
`REG-009` §12's repair was aimed at: "the entire disclosed rectangle lies outside the
domain" sits five lines above "the asserted rectangle lies inside the domain after all",
one object under two names in one paragraph, either side of the paper's sharpest
reversal.

**The count was the only part of the stanza that no anchor could have contradicted.** A
patch that resolves four anchors exactly once reports total success while a fifth site
sits two hundred lines away; `patchkit` proves each anchor is unambiguous and cannot know
the list is short. That is why the guard below asserts a COUNT and an ABSENCE rather than
five presences: presences are what a short list already satisfies.

THE ADJECTIVE IS BUILT, NOT TYPED, AND ITS WARRANT IS A MEASUREMENT
-------------------------------------------------------------------
Both phrases come out of one builder over one pair of adjectives, so there is no place to
type either noun phrase that the rename does not reach -- the `-35`/`-36` rule, applied to
a term rather than to a string or a rule. And the rename is only TRUE while the
measurement holds: `tests/test_term001_rectangle.py` recomputes the manuscript's printed
share from `RESULT-REG-009`'s S at test time, so if that measurement is ever removed or
restated the adjective loses its warrant and the guard says so, instead of the paper
carrying a word whose justification has quietly left the repository.
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REGISTRATION = ROOT / "docs/preregistration/RESULT-TERM-001.md"
RESULT_REG_009 = ROOT / "docs/preregistration/RESULT-REG-009.md"

#: The noun. Unclaimed on its own -- eleven bare occurrences keep their wording, because
#: the defect is the adjective's claim about the disclosure and not the shape.
NOUN = "rectangle"

#: The adjective that asserts the product came out of filings. It did not.
WRONG_ADJ = "disclosed"

#: The term `REG-009` §12 registered for this object and `wealthTensor-30` applied at the
#: two sites it reached. Adopted unchanged here and carried to the other five.
RIGHT_ADJ = "asserted"


def phrase(adj: str) -> str:
    """The only place either noun phrase is assembled. The guard calls this too, so a
    guard that drifts from the edit is not expressible."""
    return f"{adj} {NOUN}"


#: Numerals as the registration spells them, so the guard compares words to words.
NUMERAL = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven"}

#: The registration's one carrier of both counts, as a pattern rather than as a sentence.
#: The guard fills it from `EDITS` and requires the filled sentence to be present -- so
#: the numerals in the document and the length of the list cannot drift apart, in either
#: direction. Deliberately NOT a bare `(\w+) sites` sweep: the document legitimately says
#: "four sites" of the stanza it corrects, "two sites" of what `-30` reached and "three
#: sites" of the remainder, and a guard that could not tell those apart from its own
#: subject would be the voice bug `-36` banked, one level down.
COUNTS_SENTENCE = "at {sites} sites across {sections} sections"


def counts_sentence(sites: int, sections: int) -> str:
    return COUNTS_SENTENCE.format(sites=NUMERAL[sites], sections=NUMERAL[sections])


def sections_touched() -> set[str]:
    """The distinct manuscript sections `EDITS` reaches, read off the labels."""
    return {label.split(" · ")[0] for _, _, label in EDITS}


#: How the manuscript spells the share of the disclosure falling OUTSIDE the rectangle.
#: Not the value -- the value is recomputed from `RESULT-REG-009`'s S by the guard. This
#: is only how to find it on the page.
OUTSIDE_SHARE_TEMPLATE = "{pct}% of the disclosed pairs fall outside that {noun}"


def outside_share_sentence(pct: str) -> str:
    return OUTSIDE_SHARE_TEMPLATE.format(pct=pct, noun=NOUN)


# --------------------------------------------------------------------------------------
# THE FIVE ANCHORS. Every `old` is a span with NO internal newline; no heading and no
# horizontal rule falls inside any of them, so the structure delta is empty. Each is
# quoted with enough of its own sentence to be unique, and each was read in its own
# context before this file existed -- the referent test is recorded in the registration's
# §2 and it is the same at all five: the object is the ASSUMED product.
# --------------------------------------------------------------------------------------

#: §4.4 -- the straggler inside the repaired section. Five lines below this span the same
#: paragraph already says `asserted rectangle` of the same object at the measured rate.
S1_OLD = f"**the entire {phrase(WRONG_ADJ)} lies outside the domain**"
S1_NEW = f"**the entire {phrase(RIGHT_ADJ)} lies outside the domain**"

#: §4.9 -- what the fitted shape does not rescue. The object is §4.4's product, whose
#: admissible share is the statistic the next sentence withdraws.
S2_OLD = f"**This does not rescue the {phrase(WRONG_ADJ)}, and the statistic"
S2_NEW = f"**This does not rescue the {phrase(RIGHT_ADJ)}, and the statistic"

#: §4.9 -- alpha_eff's span, forty years to three: the product's own extent, whose fast
#: edge delta = 0.333 the preceding paragraph names.
S3_OLD = f"a ninth of itself across the {phrase(WRONG_ADJ)},"
S3_NEW = f"a ninth of itself across the {phrase(RIGHT_ADJ)},"

#: §4.10 -- the back-reference to §4.9's span. Renamed with its referent or it points at
#: a name the paper no longer uses.
S4_OLD = f"effective rate misstates one end of the {phrase(WRONG_ADJ)};"
S4_NEW = f"effective rate misstates one end of the {phrase(RIGHT_ADJ)};"

#: §7 -- the TEST column of the three-rates row, a different cell of the same table whose
#: CLAIM column `wealthTensor-30` repaired. `test_ledger_provenance`'s key for that row is
#: anchored on `rectangle lies outside` with the adjective deliberately omitted and is
#: untouched by this edit; this row's key lives in `SIMULATION_ROWS` and is untouched too.
S5_OLD = f"event-date MLE across the {phrase(WRONG_ADJ)}"
S5_NEW = f"event-date MLE across the {phrase(RIGHT_ADJ)}"

#: The edit list IS the site count. The registration states a numeral; the guard parses
#: that numeral and asserts it equals `len(EDITS)`, so the number has exactly one parse
#: and this list is it.
EDITS = [
    (S1_OLD, S1_NEW, "§4.4 · the straggler inside the section §12's repair was aimed at"),
    (S2_OLD, S2_NEW, "§4.9 · what the fitted shape does not rescue"),
    (S3_OLD, S3_NEW, "§4.9 · alpha_eff across the product's own extent"),
    (S4_OLD, S4_NEW, "§4.10 · the back-reference, renamed with its referent"),
    (S5_OLD, S5_NEW, "§7 · the test column of the three-rates row"),
]


def main() -> int:
    apply_edits(
        [(PAPER, old, new, label) for old, new, label in EDITS],
        expect_structure={},
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
