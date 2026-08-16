"""A whitespace-identity guard certifies that no CHARACTER moved, not that no MEANING moved.

WHAT HAPPENED
-------------
`-41` shipped `scripts/wt107_rewrap_edited_paragraphs.py` — a re-wrap whose unit is "the
block between blank lines" and whose guard is an identity on `" ".join(text.split())` before
and after. Its docstring makes the correct argument for that design: if a single character of
content moved the identity differs, which makes the edit's correctness independent of
anybody reading its output.

It is right about characters, and §9's limitations are a **markdown numbered list**, which is
one block. Re-filling that block to 100 columns moved `2.`, `3.` and `4.` off their line
starts and into the middle of lines. Markdown then renders the four limitations as ONE list
item containing the literal text "2. … 3. … 4. …" — charter §3.2's *one honest room* becoming
one honest paragraph. **Flattening is precisely the operation that cannot see this**, so the
one guard chosen was the one guard structurally blind to the one thing that moved.

The general form, which is why this file is not a patch to `wt107`: **in any line-oriented
format — markdown lists and tables, YAML, diffs — the line break is content, and a guard that
normalises whitespace away has agreed in advance not to look at it.** The repair is not to
fix the tool that did it (that script is the record of an edit that happened, per the `wt092`
precedent) but to put the assertion where it catches the NEXT tool too.

WHAT THIS CHECKS
----------------
One property, at the resolution the defect lives at: **a numbered or bulleted list-item
marker may not appear mid-line.** That is a pure structural fact about the source, cheap to
state, and it is exactly what a re-wrap breaks and a content edit does not.

WHAT THIS FILE DOES **NOT** ASSERT — READ THIS BEFORE PARAPHRASING IT
--------------------------------------------------------------------
**It asserts no COUNT, of §9's limitations or of anything else.** It asserts one structural
property, everywhere in the manuscript: a list-item marker may not sit mid-line.

Recorded because a paraphrase of this file went wrong and was inherited ten times.
`-42`'s handoff introduced a DO-NOT reading **"§9's LIMITATIONS ARE FOUR LIST ITEMS AND STAY
FOUR"**, citing this file as its machine. §9 had **nine** numbered items on the day that
sentence was written — `git show e947fb6:…/paper-III.md` counts nine — and has nine today. The
"four" was lifted from the WHAT HAPPENED narrative above, where four *markers* (`1.`–`4.`) were
the ones a single re-wrapped block flattened. An incident's arithmetic became a standing rule
about a section's contents, and rode the DO-NOT list from `-42` through `-51` unmeasured,
because a DO-NOT is the one part of a handoff nobody re-runs.

The live risk was to the manuscript, not to the suite: a session obeying that rule and finding
nine items would either delete five real limitations — from the section whose whole purpose is
that a reader can calibrate what is admitted — or refuse to add a tenth the paper needed. A
rule that is false in the direction of removing honesty is worse than no rule.

Measured and corrected `wealthTensor-52` (2026-08-16). If you need a count of §9, run:
    awk '/^## 9 · Limitations/{f=1;next} /^## 10 /{f=0} f' <paper> | grep -cE '^[0-9]+\. \*\*'
The count is a MEASUREMENT. Nothing in this repository mandates it.

THE CONTROL
-----------
`-37`: a mutation that does not mutate reports your guard as weak. So the red proof is the
real §9 block as `wt107` left it at `1e474b4`, verbatim, and the green proof is the same
block as `wt109` repaired it plus real prose that legitimately carries a numeral and a full
stop mid-line (`"§4.4. 0.408 per year"`-shaped text, and an ordinary decimal), because a
guard that flagged those would fire on half the manuscript.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"

#: A list-item marker sitting mid-line. Narrow on purpose:
#:
#: * the marker must be preceded by non-space text on the SAME line, which is what makes it
#:   mid-line rather than leading;
#: * a numbered marker must be followed by whitespace and then `**`, the shape every list in
#:   this manuscript uses for its item lead-in. `"...in 1. 2 per cent"` is not a list.
#:
#: Both narrowings exist because the first cut of this file flagged §4.10's decimal table and
#: §11's version strings, and a guard tuned until it is quiet is worth nothing unless the
#: sites it went quiet on are named.
MIDLINE_NUMBERED = re.compile(r"\S[ \t]+\d+\.[ \t]+\*\*")
MIDLINE_BULLET = re.compile(r"\S[ \t]{2,}[-*+][ \t]+\*\*")


def malformed(text: str) -> list[str]:
    """Every source line carrying a mid-line list-item marker."""
    out = []
    for block in re.split(r"\n\s*\n", text):
        stripped = block.lstrip()
        if stripped.startswith("|") or stripped.startswith("```"):
            continue
        for line in block.splitlines():
            if MIDLINE_NUMBERED.search(line) or MIDLINE_BULLET.search(line):
                out.append(line.strip())
    return out


# ---------------------------------------------------------------------------------------
# The control
# ---------------------------------------------------------------------------------------
#: §9 as `wt107` left it — verbatim from paper-III.md at 1e474b4.
BROKEN = (
    "1. **The severe test failed and this paper does not know why.** Three post-hoc "
    "explanations exist —\n"
    "   the theory is wrong; the bridge was wrong; the unit of observation was wrong — and "
    "**the data do\n"
    "   not distinguish them.** The first is listed first on purpose, being the one the "
    "author has the\n"
    "   strongest incentive to list last. 2. **The unit mismatch is real, unfixed, and was "
    "unfixed by\n"
    "   both registrations.** The impairment charge is asset-level.\n"
)

#: The same content, as `wt109` repaired it.
REPAIRED = (
    "1. **The severe test failed and this paper does not know why.** Three post-hoc "
    "explanations exist —\n"
    "   the theory is wrong; the bridge was wrong; the unit of observation was wrong — and "
    "**the data do\n"
    "   not distinguish them.** The first is listed first on purpose, being the one the "
    "author has the\n"
    "   strongest incentive to list last.\n"
    "2. **The unit mismatch is real, unfixed, and was unfixed by both registrations.** The "
    "impairment\n"
    "   charge is asset-level.\n"
)

#: Real manuscript shapes a cruder rule flags. Named, because a linter that went quiet on
#: something unnamed is a linter nobody can audit.
LEGAL = [
    "the censored geometric maximum likelihood estimate is 0.1227 per quarter, 0.408 per year.",
    "Half of the rectangle is admissible only at α ≈ 0.19, and all of it above α = 0.33.",
    "See §4.4. **The binding constraint** is the model's domain, not the ordering.",
    "retrieval date 2026-08-12, commit 0569ab6, and a SHA-256 for both inputs.",
]


def test_the_guard_sees_the_defect_it_was_written_for():
    found = malformed(BROKEN)
    assert len(found) == 1, f"expected 1 mid-line marker in the real broken block, got {found}"


def test_the_repaired_block_is_clean():
    assert malformed(REPAIRED) == []


@pytest.mark.parametrize("line", LEGAL, ids=range(len(LEGAL)))
def test_ordinary_prose_is_not_flagged(line):
    assert malformed(line) == [], (
        "A legal manuscript line is flagged. This guard watches for LIST STRUCTURE, not for "
        "numerals followed by full stops."
    )


def test_the_two_proofs_are_disjoint():
    assert BROKEN != REPAIRED
    assert " ".join(BROKEN.split()) == " ".join(REPAIRED.split()), (
        "The red and green fixtures must differ ONLY in line breaks — otherwise this file "
        "proves nothing about the guard flattening cannot make."
    )


# ---------------------------------------------------------------------------------------
# The manuscript
# ---------------------------------------------------------------------------------------
def test_the_manuscript_has_no_midline_list_markers():
    found = malformed(PAPER.read_text(encoding="utf-8"))
    assert not found, (
        "A list-item marker sits mid-line, so markdown will render the items after it as "
        "body text of the item before it. This is what a block-level re-wrap does to a list, "
        "and a whitespace-identity guard cannot see it: flattening is exactly the operation "
        "that erases the difference. Re-wrap the ITEMS, not the block.\n\n"
        + "\n".join(f"  * {line[:160]}" for line in found)
    )
