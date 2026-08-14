"""Re-wrap only the paragraphs this session edited, and prove nothing but whitespace moved.

WHY THIS EXISTS
---------------
`patchkit`'s standing rule is that an anchor must have no internal newline, because every
anchor that has ever missed in this project missed on a line break. Honouring it means a
replacement longer than the line it lands in leaves the paragraph ragged — five of this
session's edits did. Ragged wraps are harmless to the rendered document and expensive to the
NEXT session, which has to find an anchor inside them.

So the tickets are applied first, wrapping is repaired last, and the repair is separated from
the content edits precisely so that its diff is reviewable as *whitespace only*.

THE GUARD IS AN IDENTITY, NOT A REVIEW
---------------------------------------
`" ".join(text.split())` is computed for the whole file before and after. If a single
character of content moved, it differs, and nothing is written. That makes this the one
edit in the session whose correctness does not depend on anybody reading its output — which
is the only kind of bulk reflow worth running on a manuscript.
"""
from __future__ import annotations

import pathlib
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"

WIDTH = 100

#: One unique substring per paragraph this session left ragged. The block containing it —
#: bounded by blank lines — is the unit re-wrapped.
TARGETS = [
    "The same registered events establish it",                     # abstract, T1 + T3
    "It is free.** Fix a reported series generated at",            # §4.2, T4
    "On the registered sample the recognition rate PRE-002",       # §4.4, T1 + T3
    "§5.4 measures the recognition rate PRE-002's instrument",     # §4.9, T1
    "Those are point estimates, and the ordering is the claim",    # §5.3, T6
    "unobservability is identified with GAAP asset class",         # §6.1, T5
    "α is measured, but",                                          # §9 limitation 4, T1
]


def rewrap(block: str) -> str:
    lines = block.split("\n")
    first_indent = lines[0][: len(lines[0]) - len(lines[0].lstrip())]
    cont_indent = first_indent
    if len(lines) > 1:
        cont_indent = lines[1][: len(lines[1]) - len(lines[1].lstrip())]
    body = " ".join(" ".join(lines).split())
    return textwrap.fill(body, width=WIDTH, initial_indent=first_indent,
                         subsequent_indent=cont_indent, break_long_words=False,
                         break_on_hyphens=False)


def main() -> int:
    text = PAPER.read_text(encoding="utf-8")
    before = " ".join(text.split())

    blocks = text.split("\n\n")
    touched = 0
    for i, block in enumerate(blocks):
        if not any(t in block for t in TARGETS):
            continue
        if block.lstrip().startswith(("|", ">", "#", "```")) or "\n|" in block:
            raise SystemExit(f"wt107: block {i} is a table, quote or heading — refusing")
        new = rewrap(block)
        if new != block:
            blocks[i] = new
            touched += 1

    out = "\n\n".join(blocks)
    if " ".join(out.split()) != before:
        raise SystemExit("wt107: content changed, not just whitespace. NOTHING WRITTEN.")
    if out == text:
        print("wt107 · nothing to re-wrap")
        return 0
    PAPER.write_text(out, encoding="utf-8")
    print(f"wt107 ok · {touched} paragraph(s) re-wrapped at {WIDTH} cols · "
          f"flattened text byte-identical")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
