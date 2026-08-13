#!/usr/bin/env python3
"""REG-007's §7 ledger row, and the positional reference it would otherwise break.

TWO EDITS, AND THE SECOND EXISTS ONLY BECAUSE OF THE FIRST. §7's closing prose says
"The last row is the one this programme would defend hardest." Appending a row silently
re-points that sentence at the new row, and no guard in this repository would ever flag
it -- patchkit compares structure, not reference. It is exactly the §4.4 failure of
wealthTensor-18, where inserting a column pointed "the column beside it" at the wrong
column. So the ordinal is replaced by the row's own name, in the same pass.

A THIRD POSITIONAL REFERENCE IS LEFT ALONE, DELIBERATELY, AND TEED UP INSTEAD. The same
paragraph opens "The fifth is the reason this section is not decoration", and which row
"the fifth" names cannot be recovered from the table as it now stands -- the description
that follows (400 draws, an identification result that explained a registered null)
does not match the fifth row of the current table. Guessing would replace a knowable
ambiguity with an unknowable error. It is carried in the handoff for whoever knows.
"""
from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from patchkit import apply_edits                                  # noqa: E402

PAPER = HERE.parent / "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md"

ROW = ("| **The disclosed trigger does not separate the two channels** | rate at which filers "
       "name the standard's own internal trigger, joint-charge against goodwill-only, inside the "
       "window where ASC 350-20-50-2(a) compels the description — against a placebo arm on whom "
       "it does not | a window-versus-placebo gap wide enough to show the measure reads events "
       "rather than accounting policy | **0.436 against 0.403** on 1,833 classified firm-years; "
       "the difference is **+0.041** (*p* 0.38) or **−0.032** (*p* 0.24) according to a coding "
       "choice fixed in advance so that the sign could not be chosen afterwards |\n")

OLD_TAIL = """
Two rows deserve a comment.
"""
NEW_TAIL = ROW + """
Two rows deserve a comment.
"""

OLD_LAST = """The last row is the one this programme would defend hardest."""
NEW_LAST = """The row on the guards' own audit is the one this programme would defend hardest."""


def main() -> int:
    apply_edits([
        (PAPER, OLD_TAIL, NEW_TAIL, "§7 · the REG-007 ledger row"),
        (PAPER, OLD_LAST, NEW_LAST, "§7 · ordinal re-anchored by name, so the row it "
                                    "points at does not move when the table grows"),
    ], expect_structure={})
    return 0


if __name__ == "__main__":
    sys.exit(main())
