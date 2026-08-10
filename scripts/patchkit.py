"""patchkit — validate-every-anchor-THEN-write, so a multi-anchor documentation edit
cannot leave a half-patched tree.

Why this exists (WT-058, session wealthTensor-05). A patch script that asserted each
anchor and wrote immediately missed anchor twelve of sixteen — a hard-wrapped sentence
broke after "negative" rather than after "conventional" — and exited with eleven edits
on disk and five not. The tree was then in a state no commit and no `git checkout`
described, and `git status` could not tell you which half you had.

"Create the undo path first" is satisfied by git for a CLEAN tree. It is NOT satisfied
for a tree the script itself dirtied halfway through. Validate-then-write is what makes
the undo path exist at the moment it is needed.

Usage
-----
    from patchkit import apply_edits

    apply_edits([
        (path, old, new, "label shown on success or failure"),
        ...
    ])

Raises AnchorError -- having written NOTHING -- if any `old` does not occur exactly
once in its file. Multiple edits to the same file compose in order against in-memory
text, so an earlier edit may legitimately create the anchor a later one matches.

Rule of thumb that costs nothing and saves a round trip: anchor on a span with NO
internal newline. In a file hard-wrapped at 100 columns, every anchor that has ever
missed in this project missed on a line break, never on a word.
"""
from __future__ import annotations

import pathlib
from typing import Iterable, Sequence


class AnchorError(RuntimeError):
    """Raised when an anchor is absent or ambiguous. Nothing has been written."""


def plan_edits(edits: Iterable[Sequence]) -> dict:
    """Validate every edit against in-memory text. Return {path: new_text}.

    Writes nothing. Raises AnchorError on the first anchor that does not occur
    exactly once, naming the label and the actual count.
    """
    texts: dict = {}
    for edit in edits:
        if len(edit) == 4:
            path, old, new, label = edit
        elif len(edit) == 3:
            path, old, new = edit
            label = f"{pathlib.Path(path).name}: {old[:40]!r}"
        else:
            raise AnchorError(f"edit must be (path, old, new[, label]); got {len(edit)} items")

        path = pathlib.Path(path)
        if path not in texts:
            texts[path] = path.read_text()
        n = texts[path].count(old)
        if n != 1:
            raise AnchorError(
                f"ANCHOR FAIL ({n} occurrences, expected exactly 1), NOTHING WRITTEN: {label}"
            )
        texts[path] = texts[path].replace(old, new)
    return texts


def apply_edits(edits: Iterable[Sequence], verbose: bool = True) -> dict:
    """Validate ALL anchors, then write. All-or-nothing."""
    edits = list(edits)
    texts = plan_edits(edits)
    for path, text in texts.items():
        path.write_text(text)
    if verbose:
        for edit in edits:
            label = edit[3] if len(edit) == 4 else f"{pathlib.Path(edit[0]).name}"
            print("  -", label)
        print("OK — %d edit(s) across %d file(s)" % (len(edits), len(texts)))
    return texts
