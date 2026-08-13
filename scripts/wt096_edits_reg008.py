#!/usr/bin/env python3
"""REG-008 §7's manuscript repairs, committed in the registration before the run.

Three edits, all REPLACEMENTS (charter §2: the defensive-sentence count is non-increasing;
nothing here is a hedge, and no slot is added that was not already there except one ledger
row, which is a result). patchkit validates every anchor and the document skeleton before
writing anything.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits                                       # noqa: E402

P = str(pathlib.Path(__file__).resolve().parent.parent /
        "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md")

EDITS = [
    (P,
     "Three points across 1,833 classified firm-years measures the vocabulary of the disclosure, not the\n"
     "mechanism behind it.",
     "Three points across 1,833 classified firm-years measures the vocabulary of the disclosure, not the\n"
     "mechanism behind it. `REG-008` sharpens the instrument to the sentence and to the *named* reporting\n"
     "unit, and the separation from the placebo more than doubles — **0.103 against 0.030** — while the\n"
     "joint-versus-goodwill-only difference stays at **+0.014** (*p* 0.60) in a design that could have\n"
     "detected 0.068. The reason is countable: **no firm-year in the window writes a sentence naming a\n"
     "reporting unit, a trigger, and any of the standard's own (f)-family language**, and the two phrases\n"
     "the Codification uses for that family appear in none of the 1,925 filings. The disclosure does not\n"
     "carry the quantity the decomposition needs.",
     "§5.4 · the disclosure route, closed on a count rather than on a selection argument alone"),

    (P,
     "The disclosure\n"
     "   route that would separate them is closed by a selection argument rather than by sample size,\n"
     "   and §5.4 says that where the number is too.",
     "The disclosure\n"
     "   route that would separate them is closed twice over — by a selection argument, and by a count:\n"
     "   sharpened to the sentence and to the named reporting unit, the disclosure does not once, in 644\n"
     "   firm-years, tie the standard's own internal trigger to the unit it fired in, and §5.4 says that\n"
     "   where the numbers are.",
     "Limitation 9 · the same repair, in the limitation that owns it"),

    (P,
     "\n\nTwo rows deserve a comment.\n",
     "\n| **A sharper disclosure instrument finds the quantity absent, not merely unresolved** | "
     "sentence-level co-occurrence of a registered trigger phrase with a *named* reporting unit, "
     "joint-charge against goodwill-only, inside the same mandated window and against the same placebo | "
     "a window-versus-placebo gap no wider than the keyword families', which would leave the null "
     "attributable to the instrument rather than to the filings | the separation more than doubles — "
     "**0.103 against 0.030**, where the families gave 0.436 against 0.403 — and the difference stays at "
     "**+0.014** (*p* 0.60) in a design that could have detected **0.068**; **0 of 281** joint firm-years "
     "name a unit and an (f)-family trigger in one sentence |"
     "\n\nTwo rows deserve a comment.\n",
     "§7 ledger · REG-008's row, beside REG-007's"),
]

if __name__ == "__main__":
    apply_edits(EDITS)
