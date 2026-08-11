#!/usr/bin/env python3
"""wealthTensor-10 · the §6.3 sentence Jason flagged and then ruled on.

WAS:
    That argument is withdrawn, and the reason it is withdrawn is worth more than the
    argument was.

The defect by the letter of the house-style ruling: the paper appraising its own
reasoning. Jason's instruction, 2026-08-11: "drastically re-write it - not just flatter
but FLATTERING :-)"

The pun is the fix. The sentence stops grading ITSELF the moment it hands the grading
OUTWARD -- and the passage already ends by saying exactly that ("A paper does not get to
grade its own integrity; a reader grades it, or does not"). So the opening sentence now
credits the reader with having got there first, which is flattering, is not self-grading,
and -- the part that is a real improvement rather than a compliance move -- ANNOUNCES THE
LIST THAT FOLLOWS. Three counts follow it in the existing text and they were previously
unannounced:

    1. it selects its own reference class
    2. it is an assessment of the author's conduct rather than of the world
    3. it arrives last in the section, so it is what a reader carries away

Reversible: one line, git-tracked, `git revert` or a one-anchor re-patch.
"""
import sys
sys.path.insert(0, "/Users/jasoncbraatz/repos/wealth-tensor/scripts")
from patchkit import apply_edits  # noqa: E402

P = "/Users/jasoncbraatz/repos/wealth-tensor/docs/papers/paper-III-dual-tensor/paper-III.md"

apply_edits([
    (
        P,
        "That argument is withdrawn, and the reason it is withdrawn is worth more than the argument was.",
        "That argument is withdrawn, on three counts a sceptical reader would have reached first.",
        "§6.3 opening sentence: stop grading the reasoning, credit the reader, announce the list",
    ),
])
print("patched: §6.3 — the appraisal now points outward, and the three counts are announced")
