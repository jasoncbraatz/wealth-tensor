"""A registration must not ship in the same commit as an instrument.

WHY THIS EXISTS
---------------
The rule is old, banked and stated in prose at least four times in this repository:

    "WHAT MAKES A PREDICTION A PREDICTION IS THE COMMIT ORDER, SO COMMIT THE REGISTRATION
     ALONE AND PUSH IT BEFORE THE ANALYSIS CODE EXISTS. A single commit containing both
     the registration and the result proves nothing, and neither does a registration that
     ships its own implementation."
        -- lessons.py 2026-08-05 (PRE-001/PRE-002) and 2026-08-10 (REVIEW-001 F3)

It had been enforced nowhere, and `-35`'s finding says what that costs: **a doctrine
sentence written in docs/ twice and enforced nowhere is still an unguarded invariant; the
second writing feels like progress and buys nothing.** So it is mechanised here, in the
one form a machine can check without a map from registrations to instruments: the commit
that INTRODUCES a registration document must introduce nothing under `scripts/` or `src/`.

WHAT IT FOUND WHEN IT WAS FIRST RUN — TWO VIOLATIONS, ONE OF THEM NEW
---------------------------------------------------------------------
`PRE-002` (`d655501`) was already known: it is the live-fire instance the 2026-08-10 lesson
was banked from, and it shipped `scripts/wt026_severe_test.py` alongside the registration.

`REG-008` (`b02d02e`) was **not** known, and it is the sharper one. Its commit subject reads
*"REG-008: the entity-anchored trigger sentence, registered alone"* and it was not alone: it
carried three prototype probes under `scripts/prototypes/`, one of them named
`reg008_probe_00_CONTAMINATED.py`, and `REG-008-p3-entity-anchored-disclosure.md` names none
of the three. A commit asserting a property it does not have, written eight days after the
lesson forbidding it was banked. **A lesson in the corpus is not a guard.**

WHY THE LEDGER IS A LEDGER AND NOT A SUPPRESSION
-------------------------------------------------
History is not rewritten to make a test green. `KNOWN_VIOLATIONS` records the two, by SHA,
with the files they carried — the `DEFENSIVE-BASELINE.json` shape from G-COACH-3, where the
invariant is not "never X" but "never X SILENTLY", which is the only version a session can
be held to. The set is asserted in BOTH directions: a new violation goes red because it is
absent from the ledger, and a ledger entry that stops being a violation ALSO goes red,
because that means someone rewrote history or moved a file and nobody would otherwise
notice.

WHAT IT CANNOT SEE
------------------
It cannot tell whether an instrument committed *later* was actually written later; only that
the repository cannot prove otherwise. It cannot see a registration edited after its result
existed — `handoff_gate.py` and the result documents' own reproduce-before-extending guards
are what cover that. And it skips outside a git work tree, because a source tarball is a
legitimate way to read this repository and a red suite there would be a lie about the work.
"""

from __future__ import annotations

import pathlib
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREREG = ROOT / "docs" / "preregistration"
PREFIXES = ("REG-", "CONSTRUCTION-", "PRE-")
CODE_DIRS = ("scripts/", "src/")

# The two commits in this repository's history that introduced a registration alongside
# code. Recorded, not suppressed: see the module docstring. Keyed by the registration's
# filename; the value is the introducing commit and the code files it carried.
KNOWN_VIOLATIONS = {
    "PRE-002-wt026-peak-to-charge.md": (
        "d655501c177ad835c4d552dd8bd05c43c0321c41",
        ("scripts/wt026_severe_test.py", "src/wealth_tensor/edgar.py"),
    ),
    "REG-008-p3-entity-anchored-disclosure.md": (
        "b02d02ede286e0c1f8c2b00bfa51a205cda086e5",
        ("scripts/prototypes/reg008_probe_00_CONTAMINATED.py",
         "scripts/prototypes/reg008_probe_01_armblind.py",
         "scripts/prototypes/reg008_probe_02_segmentation.py"),
    ),
}


def _git(*args):
    return subprocess.run(("git", "-C", str(ROOT)) + args, capture_output=True,
                          text=True, check=True).stdout


@pytest.fixture(scope="module")
def introductions():
    if not (ROOT / ".git").exists():
        pytest.skip("not a git work tree")
    out = {}
    for p in sorted(PREREG.glob("*.md")):
        if not p.name.startswith(PREFIXES):
            continue
        shas = _git("log", "--follow", "--format=%H", "--diff-filter=A",
                    "--", f"docs/preregistration/{p.name}").split()
        if not shas:
            continue
        sha = shas[-1]
        files = _git("show", "--name-only", "--format=", sha).split()
        out[p.name] = (sha, tuple(f for f in files if f.startswith(CODE_DIRS)))
    return out


def test_the_scan_found_registrations_to_scan(introductions):
    assert len(introductions) >= 10, (
        "the registration scan found almost nothing, so every assertion below would pass "
        "vacuously — check PREFIXES against docs/preregistration/")


def test_no_registration_ships_with_its_own_instrument(introductions):
    offenders = {name: v for name, v in introductions.items() if v[1]}
    unknown = {n: v for n, v in offenders.items() if n not in KNOWN_VIOLATIONS}
    assert not unknown, (
        "a registration was committed together with code:\n"
        + "\n".join(f"  {n}  {sha[:7]}  {', '.join(files)}"
                    for n, (sha, files) in unknown.items())
        + "\n\nWhat makes a prediction a prediction is the commit order. Commit the "
          "registration ALONE, push it, and let the instrument follow in its own commit. "
          "If this is a historical commit you did not make, add it to KNOWN_VIOLATIONS "
          "with its files — the ledger records violations, it does not excuse them.")


def test_every_ledger_entry_is_still_a_violation(introductions):
    """The other branch. A ledger nobody re-checks becomes a list of excuses."""
    for name, (sha, files) in KNOWN_VIOLATIONS.items():
        assert name in introductions, (
            f"{name} is in KNOWN_VIOLATIONS but no longer exists under "
            f"docs/preregistration/ — the ledger has outlived its subject")
        got_sha, got_files = introductions[name]
        assert got_sha == sha, (
            f"{name}'s introducing commit is now {got_sha[:7]}, not {sha[:7]}: history "
            f"was rewritten, and a ledger of violations that silently follows the history "
            f"it records is not a ledger")
        assert got_files, (
            f"{name} is recorded as a violation and no longer carries code. That is good "
            f"news that should not arrive silently — remove the entry deliberately.")
        assert set(got_files) == set(files), (
            f"{name}'s introducing commit carried {sorted(got_files)}, and the ledger "
            f"records {sorted(files)}")


def test_reg010_was_registered_alone(introductions):
    """The instance this guard was written alongside, asserted by name."""
    for name in ("REG-010-p3-half-integer-banding.md",
                 "CONSTRUCTION-REG-010-edge-convention.md"):
        assert name in introductions, f"{name} has no introducing commit"
        sha, files = introductions[name]
        assert not files, (
            f"{name} shipped with {files}, which is the defect this file exists to catch, "
            f"committed by the session that wrote the catcher")
