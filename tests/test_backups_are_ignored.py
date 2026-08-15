"""The pre-edit `.bak` copies are ignored by git — asserted, not asserted-about.

WHY THIS EXISTS
---------------
`docs/HANDOFF.md` has carried *"THE `.bak` COPIES ARE GITIGNORED — CITE THE TEST, NOT THE
BACKUP"* in its standing DO-NOT list for several sessions. `-47` read `.gitignore` and it
had no `.bak` pattern at all: the twelve backups in this repository were **untracked**,
which is a different fact with a different failure mode. An ignored file cannot be committed
by accident; an untracked one is a single `git add -A` away from the SSOT, and the estate's
defence against that was *another* prose rule — *"do not `git add -A` on darwin"* — in the
same list. Two rules propping each other up, one of them false.

This is the fourth session in a row in which a claim this estate makes **about itself** did
not survive being checked: `-44` the `machine` column, `-45` the `source` column, `-46` the
inventory's ranking prose, `-47` the DO-NOT list. The pattern is not about columns. It is
that **prose about the repository is the least-audited surface the repository has**, because
every cheaper check — does the sentence exist? is it in the right file? does it sound right?
— passes.

`-35`'s ruling is the one that applies: *a doctrine sentence written in docs/ twice and
enforced nowhere is still an unguarded invariant.* So the sentence gets a machine.

WHAT IT CANNOT DO
------------------
It cannot stop a backup being committed with `git add -f`, and it should not try — an
explicit force is a decision, and this guard is against an accident. It skips outside a git
work tree, following the convention of the other git-aware tests in this suite.
"""
from __future__ import annotations

import pathlib
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATTERNS = ("*.bak", "*.bak[0-9]", "*.bak-*")


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True)


@pytest.fixture(scope="module")
def repo():
    proc = _git("rev-parse", "--is-inside-work-tree")
    if proc.returncode != 0 or proc.stdout.strip() != "true":
        pytest.skip("not a git work tree")
    return ROOT


def _backups() -> list[pathlib.Path]:
    found: set[pathlib.Path] = set()
    for pat in PATTERNS:
        found.update(p for p in ROOT.rglob(pat) if p.is_file() and ".git/" not in str(p))
    return sorted(found)


def test_there_are_backups_to_ignore(repo):
    """Non-vacuity. With no `.bak` on disk the assertion below passes over nothing and
    reads as coverage — `-44`'s false-green class, which is what this file was built from.
    If the backups are ever all deleted, this goes red saying so rather than going quiet."""
    assert _backups(), (
        "no *.bak* files found — this guard is passing over an empty set. Either the "
        "backups were removed (retire this file and the DO-NOT line it holds) or the "
        "search patterns have drifted from the ones in .gitignore."
    )


def test_every_backup_is_ignored_by_git(repo):
    """`git check-ignore` is the authority, not a re-implementation of the match rules."""
    rels = [str(p.relative_to(ROOT)) for p in _backups()]
    proc = _git("check-ignore", "--no-index", *rels)
    ignored = set(proc.stdout.split("\n")) - {""}
    missed = [r for r in rels if r not in ignored]
    assert not missed, (
        f"{len(missed)} backup(s) are NOT ignored by git and can be swept in by "
        f"`git add -A`: {missed[:5]}. docs/HANDOFF.md states as a standing rule that the "
        ".bak copies are gitignored; add the pattern to .gitignore rather than editing the "
        "rule, because the rule is the one that is right."
    )


def test_no_backup_is_tracked(repo):
    """The other direction. A pattern in `.gitignore` does nothing to a file already in the
    index, so ignoring and not-tracking are two facts and this file asserts both."""
    tracked = [f for f in _git("ls-files").stdout.split("\n")
               if f and any(pathlib.PurePath(f).match(pat) for pat in PATTERNS)]
    assert not tracked, (
        f"backups are tracked in the index despite .gitignore: {tracked[:5]}. "
        "`git rm --cached` them — evidence in a backup is not in the SSOT, and a tracked "
        "backup makes that sentence false again."
    )
