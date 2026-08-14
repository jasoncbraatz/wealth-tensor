"""SCOPE-001 · the one-sentence steelman, performed on §5 and not on §10.

Registered first in `docs/preregistration/RESULT-SCOPE-001.md` §2, which was written and
committed before this script ran. The find: paper III §10 restricts §2's claim to
degradation carrying "no impairment trigger, no estimable expected loss and no observable
event to key recognition to", while §5 selects its whole sample on recognised-impairment
tags (`edgar.TIER_TAGS_REG006`). The repair is a STEELMAN — a recognised impairment marks
the TRANSITION into estimability, so the sample is the BOUNDARY of §10's restricted region
rather than a violation of it — and it goes in §5, because §10's restriction is correct as
written and is not being weakened.

One anchor, no internal newline (patchkit's rule of thumb), inside §5.1, immediately after
the four-tier table and before the registration paragraph — the first place a reader has
both the sample's nature and the restriction in mind. No heading is added or removed, so
the structure delta is declared empty.
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

ANCHOR = (
    "**The registration preceded the data.** PRE-001 was committed **alone**, at commit 9722342, and"
)

NEW = (
    "**Every event in this test is a recognised impairment, which places the sample on the boundary\n"
    "of §10's restriction rather than inside its complement:** a charge is the moment degradation\n"
    "became estimable, so §2 governs the accumulation that precedes it and the event marks where that\n"
    "accumulation ends — which is why an interval is measurable on these events and on no others.\n"
    "\n"
    + ANCHOR
)


def main() -> int:
    apply_edits(
        [(PAPER, ANCHOR, NEW, "§5.1 · the sample is the boundary of §10's restriction")],
        expect_structure={},
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
