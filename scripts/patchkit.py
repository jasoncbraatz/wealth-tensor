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

THE SECOND FAILURE MODE, AND IT IS SILENT (WT-090, session wealthTensor-16, paid for
by wealthTensor-15). An anchor whose `old` spans a STRUCTURAL DELIMITER — a heading, a
horizontal rule — must re-emit that delimiter in `new`. Inserting a section before
`## 6`, the anchor ran through `---` and the heading in order to be unique, and the
replacement did not put them back. **Every anchor resolved exactly once, the patch
reported success, and §6 was silently absorbed into §5.** Validate-then-write does not
catch this: nothing about it is ambiguous. The only symptom was a downstream metric
moving by one, inside its budget, and therefore nearly explained away.

So `apply_edits` now compares the document's STRUCTURE before and after and refuses a
write that changes it. An edit that legitimately adds or removes a heading declares the
delta:

    apply_edits(edits, expect_structure={"###": +1})    # one subsection added

Anything undeclared is an AnchorError with the exact headings gained and lost, and
nothing is written. A guard in the deterministic layer, because the doc version of this
rule was written down once and forgotten within a session.
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterable, Sequence

_HEADING = re.compile(r"^(#{1,6}) .*$", re.M)
_RULE = re.compile(r"^-{3,}\s*$", re.M)


class AnchorError(RuntimeError):
    """Raised when an anchor is absent or ambiguous. Nothing has been written."""


class StructureError(AnchorError):
    """Raised when a write would add or drop a heading or rule undeclared."""


def structure(text: str) -> dict:
    """The document's skeleton: headings by level, plus horizontal rules.

    Deliberately NOT a hash. When this guard fires, the caller needs to see WHICH
    heading vanished, and a checksum cannot tell them.
    """
    out: dict = {"---": len(_RULE.findall(text))}
    for m in _HEADING.finditer(text):
        out.setdefault(m.group(1), []).append(m.group(0))
    return out


def _levels(sig: dict) -> dict:
    return {k: (v if isinstance(v, int) else len(v)) for k, v in sig.items()}


def check_structure(before: str, after: str, expect: dict | None = None,
                    label: str = "") -> None:
    """Refuse a structural change that was not declared. Raises StructureError."""
    expect = expect or {}
    b, a = structure(before), structure(after)
    lb, la = _levels(b), _levels(a)
    problems = []
    for key in sorted(set(lb) | set(la)):
        got = la.get(key, 0) - lb.get(key, 0)
        want = expect.get(key, 0)
        if got == want:
            continue
        detail = f"{key}: {lb.get(key, 0)} -> {la.get(key, 0)} (delta {got:+d}, declared {want:+d})"
        if key != "---":
            lost = [h for h in b.get(key, []) if h not in a.get(key, [])]
            gained = [h for h in a.get(key, []) if h not in b.get(key, [])]
            if lost:
                detail += "\n      LOST:   " + "\n              ".join(lost)
            if gained:
                detail += "\n      GAINED: " + "\n              ".join(gained)
        problems.append(detail)
    if problems:
        raise StructureError(
            "STRUCTURE CHANGED, NOTHING WRITTEN"
            + (f" [{label}]" if label else "") + ":\n    "
            + "\n    ".join(problems)
            + "\n  An anchor spanning a heading or a rule must RE-EMIT it in `new`."
              "\n  If the change is intended, declare it: "
              "apply_edits(..., expect_structure={'###': +1})")


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


def apply_edits(edits: Iterable[Sequence], verbose: bool = True,
                expect_structure: dict | None = None) -> dict:
    """Validate ALL anchors AND the document skeleton, then write. All-or-nothing.

    expect_structure: declared deltas keyed by heading marker ("#", "##", ...) or
    "---" for horizontal rules. Anything undeclared and non-zero raises
    StructureError with the headings gained and lost, having written nothing.
    """
    edits = list(edits)
    texts = plan_edits(edits)
    for path, text in texts.items():
        check_structure(pathlib.Path(path).read_text(), text,
                        expect_structure, label=pathlib.Path(path).name)
    for path, text in texts.items():
        path.write_text(text)
    if verbose:
        for edit in edits:
            label = edit[3] if len(edit) == 4 else f"{pathlib.Path(edit[0]).name}"
            print("  -", label)
        print("OK — %d edit(s) across %d file(s)" % (len(edits), len(texts)))
    return texts
