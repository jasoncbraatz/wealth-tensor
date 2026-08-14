"""The PIN-001 guard — §11's pins name the code state, and the code state answers back.

WHY THIS EXISTS
---------------
`RESULT-PIN-001.md` records a defect with a signature no reflow guard can see: **nobody
edited the sentence.** §11 said `d655501` was "the last commit touching `src/`" and that
it "is verifiable now". It was true on 2026-08-05 and false by 2026-08-10, falsified not
by an error but by four subsequent commits — one of them, `93a159b`, the repair of the
REG-006 tag defect. The manuscript went on asserting it for nine days because the
sentence's truth value depends on something that changes without the sentence changing,
and nothing in this repository could notice: `d655501` occurs six times here and every
one of them is prose.

So this file is not a source-text guard with a git check bolted on. **It is a git check**,
and the source-text assertions are the small half. The load-bearing test is
`test_each_pinned_path_was_last_touched_by_the_sha_the_paper_discloses`, which goes red
on the NEXT commit that touches a pinned module — which is the moment, and the only
moment, at which §11 needs re-reading. The pin and the paper then move in the same commit
or the suite says so, which is the committed-baseline pattern `defensive_count.py`
already uses for G-COACH-3.

THE WITNESS PROBLEM, AND HOW IT IS SIDESTEPPED
----------------------------------------------
Nothing here is retyped. Every SHA, the `TIER_TAGS` block hash and the two rotted phrases
are IMPORTED from `scripts/wt099_edits_pin001.py`, the script that performed the edit and
the only place in the repository where they are written down. A guard carrying its own
copy of its subject passes forever while the original rots — the failure this very card
is about, in miniature.

WHAT IT CANNOT DO
-----------------
It cannot tell whether `93a159b`'s addition left every downstream NUMBER unchanged; it
checks the narrower and checkable thing the manuscript actually claims, that the
registered `TIER_TAGS` block is byte-identical at both SHAs. It cannot see a pinned file
edited and re-pinned wrongly. And outside a git work tree it skips rather than fails,
because a source tarball is a legitimate way to read this repository and a red suite
there would be a lie about the paper.
"""

import hashlib
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from wt099_edits_pin001 import (  # noqa: E402
    LATEST_TOUCH,
    PINS,
    ROTTED,
    TIER_TAGS_BLOCK_SHA256,
)

PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
RESULT_DOC = ROOT / "docs/preregistration/RESULT-PIN-001.md"


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


@pytest.fixture(scope="module")
def git_repo() -> None:
    try:
        inside = _git("rev-parse", "--is-inside-work-tree")
    except (OSError, subprocess.CalledProcessError):
        pytest.skip("not a git work tree — the per-file pins are unverifiable here")
    if inside != "true":
        pytest.skip("not a git work tree — the per-file pins are unverifiable here")


@pytest.fixture(scope="module")
def paper() -> str:
    return PAPER.read_text(encoding="utf-8")


def _tier_tags_block(text: str) -> str:
    """The registered `TIER_TAGS` mapping, first line through its closing brace."""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("TIER_TAGS: "):
            for j in range(i, len(lines)):
                if lines[j] == "}":
                    return "\n".join(lines[i:j + 1]) + "\n"
            break
    raise AssertionError("no TIER_TAGS block in edgar.py — the disclosure has no subject")


# --------------------------------------------------------------------------------------
# The load-bearing half: the repository answers the question the manuscript asks of it.
# --------------------------------------------------------------------------------------

def test_each_pinned_path_was_last_touched_by_the_sha_the_paper_discloses(git_repo):
    for path, sha in LATEST_TOUCH.items():
        actual = _git("log", "-1", "--format=%H", "--", path)
        assert actual.startswith(sha), (
            f"{path} was last touched by {actual[:7]}, but §11 discloses {sha}. This is "
            f"the PIN-001 defect recurring: a pinned module moved and the manuscript did "
            f"not. Update LATEST_TOUCH and the §11 sentence in the SAME commit, and say "
            f"in the paper what the new commit changed — or, if it changed a published "
            f"result, register that before saying anything."
        )


def test_every_pin_names_a_commit_that_actually_touched_that_file(git_repo):
    for path, sha in PINS.items():
        touching = _git("log", "--format=%H", "--", path).split()
        assert any(c.startswith(sha) for c in touching), (
            f"§11 pins {path} at {sha}, but no commit in that file's history starts with "
            f"it. A pin that names the wrong commit is worse than no pin."
        )


def test_the_registered_tier_tags_block_is_byte_identical_at_both_shas(git_repo):
    at_pin = _git("show", f"{PINS['src/wealth_tensor/edgar.py']}:src/wealth_tensor/edgar.py")
    at_head = (ROOT / "src/wealth_tensor/edgar.py").read_text(encoding="utf-8")
    digests = {
        name: hashlib.sha256(_tier_tags_block(text).encode()).hexdigest()
        for name, text in (("pinned", at_pin), ("head", at_head))
    }
    assert digests["pinned"] == digests["head"] == TIER_TAGS_BLOCK_SHA256, (
        f"§11 claims the TIER_TAGS block that selected §5's published sample is "
        f"byte-identical at the pin and at head. It is not: {digests}. Either the "
        f"registered tag list was edited — which PRE-001 forbids without an amendment — "
        f"or the disclosure about 93a159b needs rewriting."
    )


# --------------------------------------------------------------------------------------
# The small half: the rotted sentences are gone and the repair is present.
# --------------------------------------------------------------------------------------

def test_the_rotted_claims_are_gone_from_the_manuscript(paper):
    for phrase in ROTTED:
        assert phrase not in paper, (
            f"{phrase!r} is back in paper III. Both forms assert a fact about the "
            f"repository's PRESENT state in prose that nothing updates; PIN-001 replaced "
            f"them with per-file pins precisely so the claim could go red instead of stale."
        )


def test_section_11_carries_every_pin_and_the_edit_stayed_inside_it(paper):
    i = paper.index("\n## 11 · ")
    j = paper.index("\n# Appendix A", i)
    eleven = paper[i:j]
    for path, sha in PINS.items():
        assert path in eleven, f"§11 no longer names {path}"
        assert sha in eleven, f"§11 no longer pins {path} at {sha}"
    assert "93a159b" in eleven, "§11 must disclose the commit that moved edgar.py after the pin"
    before = paper[:i]
    for sha in ("ad779eb", "b9089c7", "93a159b"):
        assert sha not in before, (
            f"{sha} appears outside §11 — PIN-001 registers both edits as staying inside "
            f"§11, and a SHA leaking into the body is a second place for it to rot."
        )


def test_the_result_doc_still_documents_the_pair(paper):
    doc = RESULT_DOC.read_text(encoding="utf-8")
    assert "last commit touching" in doc, "the result doc must quote the claim it repaired"
    assert TIER_TAGS_BLOCK_SHA256 in doc
    assert "93a159b" in doc
