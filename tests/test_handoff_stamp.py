"""wealthTensor-28 · `handoff_gate --stamp` must not report success on a no-op.

THE DEFECT, LIVE. `re.sub(count=1)` returns its input unchanged when nothing matches, so
a handoff whose frontmatter was missing the `gh_sha` key was written back byte-identical
and the function printed `stamped gh_sha: <head>` anyway. `--stamp` said it stamped, the
follow-up commit said "nothing to commit, working tree clean", and `--check` went on
refusing the file — three lines apart, one of them cheerful.

It could only fire on a handoff that was ALREADY malformed, which is exactly when a false
success costs the most: the author has been told the file is stamped and the gate keeps
blocking. Same family as `grep -c PATTERN f || echo 0` yielding "0\\n0" (wealthTensor-27) —
a success report on a path where nothing happened.

Three branches, and the MIDDLE ONE IS WHY THIS FILE EXISTS. The naive fix (`re.subn` with
`count=1`, assert `n == 1`) catches a MISSING key and is blind to a DUPLICATED one, because
`count=1` stops after the first hit and reports 1 either way.
"""
from __future__ import annotations

import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import handoff_gate as G  # noqa: E402

GOOD = """---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-13
session: test
gate_passed: true
gate_version: "2.51"
---

# body
"""


def _run(tmp_path, text) -> tuple[int, str]:
    p = tmp_path / "HANDOFF.md"
    p.write_text(text)
    before = p.read_text()
    old = G.HANDOFF
    G.HANDOFF = p
    try:
        rc = G.stamp()
    finally:
        G.HANDOFF = old
    return rc, before


def test_one_gh_sha_line_stamps_and_writes(tmp_path):
    rc, before = _run(tmp_path, GOOD)
    after = (tmp_path / "HANDOFF.md").read_text()
    assert rc == 0
    assert after != before
    assert "gh_sha: PENDING" not in after


def test_zero_gh_sha_lines_refuses_and_writes_NOTHING(tmp_path):
    """The live-fire case. A refusal that still writes is not a refusal."""
    rc, before = _run(tmp_path, GOOD.replace("gh_sha: PENDING\n", ""))
    assert rc == 1
    assert (tmp_path / "HANDOFF.md").read_text() == before


def test_two_gh_sha_lines_refuses_too(tmp_path):
    """THE MIDDLE BRANCH. `re.subn(count=1)` reports n == 1 here, so the obvious fix
    passes this input silently and rewrites one of two keys."""
    rc, before = _run(tmp_path, GOOD.replace("gh_sha: PENDING\n",
                                             "gh_sha: PENDING\ngh_sha: PENDING\n"))
    assert rc == 1
    assert (tmp_path / "HANDOFF.md").read_text() == before


def test_the_message_names_the_required_keys_rather_than_just_complaining(tmp_path, capsys):
    _run(tmp_path, GOOD.replace("gh_sha: PENDING\n", ""))
    err = capsys.readouterr().err
    assert "NOTHING WAS WRITTEN" in err
    for k in G.REQUIRED:
        assert k in err


def test_the_repos_own_handoff_carries_every_required_key():
    """The frontmatter omission that exposed the defect, held so it cannot recur."""
    fm, _ = G.frontmatter()
    missing = [k for k in G.REQUIRED if k not in fm]
    assert not missing, f"docs/HANDOFF.md frontmatter is missing {missing}"
