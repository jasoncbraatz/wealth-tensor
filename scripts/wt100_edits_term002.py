"""TERM-002 · "refused five times" at three sites, over a list of four.

Registered first in `docs/preregistration/RESULT-TERM-002.md`, committed alone at
`75111ea` before this script existed on disk. The find, recorded by `REVIEW-004` on
2026-08-13 and never built: §8's class paragraph says the programme refused the
free-parameter move **five** times and then enumerates **four**, and §8.1 and §A.2.4
repeat the five. The number is the length of a list four lines below it, and nothing in
`scripts/`, `tests/` or `src/` has ever known that.

THE RULING, AND THE ONE AMENDMENT TO IT
---------------------------------------
The class has FOUR members and the fourth — §8.1's unmeasured φ — is kept, because it is
the instance that got through and the only one that cost this programme anything.

The amendment, registered in §2 of the result doc: the repair binds TWO numerals rather
than one. §8.1's own sentence reads "refused ... times in other costumes (§8) and should
have refused here", and §8.1's φ move IS one of §8's four — so "other costumes" is the
other three, all genuinely refused. §A.2.4 says the same of Λ, which is not in the list at
all, so its other costumes are the four, of which three were refused. Writing "four"
beside the word *refused* at either site would assert a refusal the paper concedes two
lines later that it did not make: the repair introducing a fresh instance of the defect it
repairs. So the manuscript states the CLASS count once, in §8, where the list is, and the
REFUSAL count at the two sites that use the word "refused".

Four anchors, every one a span with NO internal newline (patchkit's rule of thumb). No
heading and no horizontal rule moves, so the structure delta is declared empty.

THE NUMERALS ARE WRITTEN DOWN HERE AND NOWHERE ELSE, AND NOT EVEN HERE AS FINISHED TEXT.
The three repaired constructions are emitted by the BUILDERS below, from a count.
`tests/test_term002_count.py` imports the builders and calls them with the count it parses
out of the manuscript's own enumeration — so the guard cannot drift from its own witness,
and the number and the list cannot disagree in either direction. A guard that retyped
"four" would pass forever while the list grew, which is this defect exactly, in miniature.
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

PAPER = (
    pathlib.Path(__file__).resolve().parents[1]
    / "docs/papers/paper-III-dual-tensor/paper-III.md"
)

#: Members of the class §8 enumerates, as this edit found them. NOT a constant the
#: manuscript is generated from: the guard counts the enumeration and compares to this.
CLASS_COUNT = 4

#: Members the manuscript marks as conceded rather than refused — §8.1's unmeasured φ,
#: which the enumeration flags with `CONCESSION_MARK` and §8.1 spends a subsection
#: retracting. It is the one that got through, and the ruling keeps it in the list.
CONCEDED_COUNT = 1

#: What the two remote sites are entitled to say. Derived, never typed twice.
REFUSED_COUNT = CLASS_COUNT - CONCEDED_COUNT

#: Numerals and ordinals as the manuscript spells them. Only three entries are exercised;
#: the rest exist so a future renumbering has a word to reach for instead of retyping one.
NUMERAL = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven"}
ORDINAL = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth"}

#: The word the enumeration's conceded item carries; the guard counts items containing it.
CONCESSION_MARK = "concedes"

#: The guard's two handles on the manuscript: the paragraph, and the clause that opens the
#: enumeration inside it. Everything between the second and the sentence's end is the list.
CLASS_PARAGRAPH_OPENER = "**Adding a free parameter to absorb an objection.**"
ENUMERATION_OPENER = "looked locally reasonable: "

#: The construction the repair removes, in the form it must never reappear in.
ROTTED = f"refused {NUMERAL[5]} times"


# --------------------------------------------------------------------------------------
# THE BUILDERS. Every repaired string in the manuscript comes from one of these three, and
# the guard calls the same three with counts parsed from the manuscript. This is the whole
# mechanism: there is no place to type a numeral that the arithmetic does not reach.
# --------------------------------------------------------------------------------------

def class_clause(members: int) -> str:
    """§8's opening: how many times the programme met the move. Not how many it refused."""
    return f"Faced {NUMERAL[members]} times across this programme"


def reconciling_clause(refused: int, conceded_position: int) -> str:
    """§8's close: where the class count and the refusal count are reconciled, in eight
    words, inside the existing sentence, with no hedge and no new sentence."""
    return f" — {NUMERAL[refused]} refused, the {ORDINAL[conceded_position]} not."


def remote_construction(refused: int) -> str:
    """What §8.1 and §A.2.4 say. Both use the word *refused*, so both take the refusal
    count; §8.1's own costume is excluded by its own "in other costumes"."""
    return f"refused {NUMERAL[refused]} times in other costumes"


# --------------------------------------------------------------------------------------
# EDIT 1 · §8's opening — the class count stops being one more than the list
# --------------------------------------------------------------------------------------

A1_OLD = (
    "**Adding a free parameter to absorb an objection.** "
    f"Refused {NUMERAL[5]} times across this programme and"
)
A1_NEW = (
    "**Adding a free parameter to absorb an objection.** "
    f"{class_clause(CLASS_COUNT)} and"
)

# --------------------------------------------------------------------------------------
# EDIT 2 · §8's close — the two counts reconciled where the list is
# --------------------------------------------------------------------------------------

A2_OLD = (
    "leaning on an unmeasured φ. A quantity that can accommodate any observation "
    "forbids nothing."
)
A2_NEW = (
    f"leaning on an unmeasured φ{reconciling_clause(REFUSED_COUNT, CLASS_COUNT)} "
    "A quantity that can accommodate any\nobservation forbids nothing."
)

# --------------------------------------------------------------------------------------
# EDIT 3 · §8.1 — "other costumes" excludes the costume it is standing in
# --------------------------------------------------------------------------------------

B1_OLD = (
    f"the move this programme has refused {NUMERAL[5]} times in other costumes (§8) "
    "and should have refused here."
)
B1_NEW = (
    f"the move this programme has {remote_construction(REFUSED_COUNT)} (§8) "
    "and should have refused here."
)

# --------------------------------------------------------------------------------------
# EDIT 4 · §A.2.4 — Λ is not in the list, so its other costumes are the four, of which
# three were refused
# --------------------------------------------------------------------------------------

B2_OLD = (
    f"is the free parameter this programme has refused {NUMERAL[5]} times in other "
    "costumes. So the claim is not"
)
B2_NEW = (
    f"is the free parameter this programme has {remote_construction(REFUSED_COUNT)}. "
    "So the claim is not"
)


def main() -> int:
    apply_edits(
        [
            (PAPER, A1_OLD, A1_NEW, "§8 · the class count becomes the length of the list"),
            (PAPER, A2_OLD, A2_NEW, "§8 · the refusal count reconciled where the list is"),
            (PAPER, B1_OLD, B1_NEW, "§8.1 · other costumes excludes the one it stands in"),
            (PAPER, B2_OLD, B2_NEW, "§A.2.4 · Λ's other costumes, three of them refused"),
        ],
        expect_structure={},
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
