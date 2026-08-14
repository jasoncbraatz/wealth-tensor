"""§9's four limitations are one list item wearing four numbers. Put the line breaks back.

THE DEFECT, AND WHO INTRODUCED IT
----------------------------------
`-41`'s `wt107_rewrap_edited_paragraphs.py` re-wrapped every block that contained one of its
seven target strings. One of those targets is `"α is measured, but"` — §9 limitation 4 — and
in markdown §9's four limitations are **one block**: a numbered list, bounded by blank lines,
whose items begin at line starts. `wt107` re-filled the block to 100 columns, so `2.`, `3.`
and `4.` now sit **mid-line**:

    strongest incentive to list last. 2. **The unit mismatch is real, unfixed, ...

Any renderer reads that as list item 1 containing the literal text "2. … 3. … 4. …". The
paper's limitations section — charter §3.2's *one honest room* — renders as a single
limitation. At `1e474b4` this is three sites and nothing else in the manuscript; the
pre-`wt102` backup has zero.

WHY THE GUARD DID NOT CATCH IT, WHICH IS THE PART WORTH KEEPING
----------------------------------------------------------------
`wt107`'s guard is an identity on `" ".join(text.split())` before and after, and its
docstring is right that this makes the edit's correctness independent of anybody reading the
output. It is right about characters. **Flattening is precisely the operation that erases the
distinction between `2.` at a line start and `2.` mid-line**, so the one guard chosen was the
one guard structurally blind to the one thing that moved. A whitespace-identity guard
certifies that no character moved, not that no *meaning* moved — and in any line-oriented
format (markdown lists and tables, YAML, diffs) the line break **is** content.

`wt107` is left exactly as it is: it is the record of an edit that happened, per the
`wt092` precedent. The durable repair is not a patch to one script but
`tests/test_manuscript_lists_are_well_formed.py`, which goes red on a mid-line item marker
whatever tool put it there.

THIS SCRIPT'S OWN GUARD, WHICH IS THE PAIRED VERSION
------------------------------------------------------
Same flattened identity — nothing but line breaks may move — **plus** the structural
assertion the flattening cannot make: after the write, every numbered item marker in the
target block begins a line, and the block carries exactly four of them. Identity for the
characters, structure for the breaks. Either alone is half a guard.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
BAK = PAPER.with_suffix(".md.bak-pre-wt109-list")

WIDTH = 100
#: The block, identified by a string unique to §9 limitation 1.
MARKER = "**The severe test failed and this paper does not know why.**"
EXPECT_ITEMS = 4

#: A numbered item marker that is NOT at the start of a line — the defect itself.
INLINE_ITEM = re.compile(r"\S[ \t]+(\d+)\.[ \t]+\*\*")
#: A numbered item marker at a line start — what a well-formed list looks like.
LEADING_ITEM = re.compile(r"^(\d+)\.[ \t]+", re.M)


def rewrap_list(block: str) -> str:
    """Re-fill each numbered item separately, so every marker starts its own line."""
    flat = " ".join(block.split())
    parts = re.split(r"(?:^|(?<= ))(\d+\.) ", flat)
    # parts == ['', '1.', 'text', '2.', 'text', ...]
    out = []
    for marker, body in zip(parts[1::2], parts[2::2]):
        out.append(
            textwrap.fill(
                f"{marker} {body.strip()}",
                width=WIDTH,
                initial_indent="",
                subsequent_indent="   ",
                break_long_words=False,
                break_on_hyphens=False,
            )
        )
    return "\n".join(out)


def main() -> int:
    text = PAPER.read_text(encoding="utf-8")
    before_flat = " ".join(text.split())

    blocks = text.split("\n\n")
    hits = [i for i, b in enumerate(blocks) if MARKER in b]
    if len(hits) != 1:
        raise SystemExit(f"GATE: expected exactly 1 block carrying §9's marker, found {len(hits)}")
    i = hits[0]
    original = blocks[i]

    inline_before = INLINE_ITEM.findall(original)
    if not inline_before:
        print("  nothing to repair — §9's list already has every marker at a line start")
        return 0
    print(f"  found {len(inline_before)} mid-line item marker(s): {inline_before}")

    blocks[i] = rewrap_list(original)
    new_text = "\n\n".join(blocks)

    # --- guard 1 · the identity: characters may not move -------------------------------
    if " ".join(new_text.split()) != before_flat:
        raise SystemExit("GATE: flattened text changed. Nothing written.")

    # --- guard 2 · the structure: the breaks must carry what flattening cannot see ------
    repaired = blocks[i]
    if INLINE_ITEM.search(repaired):
        raise SystemExit(f"GATE: markers still mid-line: {INLINE_ITEM.findall(repaired)}")
    leading = LEADING_ITEM.findall(repaired)
    if leading != [str(n) for n in range(1, EXPECT_ITEMS + 1)]:
        raise SystemExit(f"GATE: expected items 1..{EXPECT_ITEMS} at line starts, got {leading}")

    if not BAK.exists():
        shutil.copy2(PAPER, BAK)
        print(f"  backup: {BAK.name}")
    PAPER.write_text(new_text, encoding="utf-8")
    print(f"  §9's limitations are {len(leading)} list items again; "
          f"flattened text identical (guard 1), every marker line-leading (guard 2)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
