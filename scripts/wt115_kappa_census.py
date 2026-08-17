#!/usr/bin/env python3
"""wealthTensor-65 · every place the corpus calls kappa a MECHANISM.

`DECISION-001` prices option A as *"demote kappa from mechanism to budget in 5 places"* and
lists them: the abstract, §1 contribution 2, §2.4, §3.1's heading and gloss, §6. All five are
in `paper-II.md`.

`WT-092`, asked of that census: what is the widest object its own words claim, and what is the
narrowest thing it touches? It says *the paper asserts kappa-as-mechanism in five places*. It
looked in one file. `tests/test_redistribution.py:158` opens

    \"\"\"kappa -- the share of aggregate wealth moved per assessment -- is the mechanism.

and nothing asserts that sentence, which is the `PIN-001` shape exactly: load-bearing prose in
an instrument, checked by nothing, in the file a replicator reads to find out what the estate
believes.

So: sweep the WHOLE corpus before editing any of it, and print every hit with its context, so
the patch is built from a census rather than from a list somebody wrote from memory.
"""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

#: Where kappa-as-mechanism could hide. Manuscripts, instruments, and the source.
SEARCH = [
    *sorted((ROOT / "docs/papers").glob("*/paper-*.md")),
    *sorted((ROOT / "tests").rglob("*.py")),
    *sorted((ROOT / "scripts").rglob("*.py")),
    *sorted((ROOT / "src").rglob("*.py")),
]

#: kappa named as a mechanism, in either word order, in prose or with the glyph.
PATTERNS = [
    re.compile(r"mechanism is (κ|kappa)", re.I),
    re.compile(r"(κ|kappa)[^.\n]{0,80}?is the mechanism", re.I),
    re.compile(r"mechanism identified as (κ|kappa)", re.I),
    re.compile(r"closed-form mechanism \((κ|kappa)\)", re.I),
    re.compile(r"quantity through which the base", re.I),
    re.compile(r"is the mechanism", re.I),
    re.compile(r"the mechanism is visible", re.I),
]

def is_record(path: pathlib.Path) -> bool:
    """A patch script QUOTES the text it replaced, as its anchor.

    Those quotes are a RECORD of an edit that already happened, not a live assertion, and
    rewriting them would falsify the history of what a past session did. `wt112` carries
    `-64`'s anchors and `wt116` carries this session's; both are hits and neither is a site.
    Reported separately rather than silently dropped -- a census that hides a category is
    the defect this census exists to find (WT-092).
    """
    n = path.name
    return n.startswith("wt115_") or ("_edits_" in n and n.startswith("wt"))


hits = 0
records = 0
for path in SEARCH:
    if is_record(path):
        records += sum(
            1 for line in path.read_text(encoding="utf-8", errors="ignore").split("\n")
            if any(pat.search(line) for pat in PATTERNS)
        )
        continue
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").split("\n")
    except OSError:
        continue
    for i, line in enumerate(lines, 1):
        for pat in PATTERNS:
            if pat.search(line):
                rel = path.relative_to(ROOT)
                print(f"{rel}:{i}\n    {line.strip()[:110]}")
                hits += 1
                break

print()
print(f"{hits} LIVE site(s), plus {records} anchor(s) inside patch scripts, which are records.")
print("DECISION-001's census said FIVE, all in paper-II.md. The sixth was a test docstring.")
