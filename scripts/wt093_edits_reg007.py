#!/usr/bin/env python3
"""REG-007 sec 7's manuscript repairs, committed before Lambda had a value.

Two edits, both registered in advance:

  1. Sec 5.4 gains the SELECTION statement -- ASC 350-20-50-2(a) compels the
     facts-and-circumstances description only for a recognised goodwill loss, so any
     triggering-event population assembled outside that window is conditioned on the
     outcome under study -- and the measured 0.436 / 0.403 window-versus-placebo pair
     that shows the disclosure route does not identify. It REPLACES the trailing
     sentence, which duplicated Limitation 9's own summary of the same point. Charter
     sec 2: a CUT, not an ABSORB.

  2. Limitation 9 gains one clause naming the disclosure route as closed by a selection
     argument rather than by sample size, and pointing at sec 5.4 where the number is --
     the deferral pattern the paragraph already uses.

No headings change. Anchors carry their line breaks, copied out of a dx --get of the
file, because this document hard-wraps and every anchor that has ever missed in this
project missed on a line break.
"""
from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from patchkit import apply_edits                                  # noqa: E402

PAPER = HERE.parent / "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md"

OLD_54 = """sign in either sector. What this design establishes is the magnitude of the departure from
diagonality, which was previously unmeasured, and that §5's treatment of the events as independent
draws overstates the information they carry."""

NEW_54 = """sign in either sector. The natural fallback is the triggering *disclosure* rather than the
charge, and `REG-007` measures why that route does not identify either. ASC 350-20-50-2(a) compels
a description of the facts and circumstances leading to the impairment only *for each goodwill
impairment loss recognized*; where a test is run and nothing is charged the Codification compels
nothing, and disclosure falls to MD&A. A triggering-event population assembled without that
restriction is therefore selected on the outcome under study. Inside the window where the mandate
does fall — and falls on both arms alike, which is what makes the comparison available — filers
naming the standard's own internal trigger run at **0.436**, against **0.403** among firm-years
that took a non-goodwill charge and no goodwill charge, on whom the mandate does not fall at all.
Three points across 1,833 classified firm-years measures the vocabulary of the disclosure, not the
mechanism behind it."""

OLD_L9 = """one suppressing joint recognition, and §5.4 says so where the number is. It is registered
   before its instrument is coded, or it is not run."""

NEW_L9 = """one suppressing joint recognition, and §5.4 says so where the number is. The disclosure
   route that would separate them is closed by a selection argument rather than by sample size,
   and §5.4 says that where the number is too. It is registered before its instrument is coded,
   or it is not run."""


def main() -> int:
    apply_edits([
        (PAPER, OLD_54, NEW_54, "§5.4 · the selection statement and the placebo pair"),
        (PAPER, OLD_L9, NEW_L9, "Limitation 9 · the disclosure route named as closed"),
    ], expect_structure={})
    return 0


if __name__ == "__main__":
    sys.exit(main())
