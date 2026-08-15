"""`REG-001` §5 · **"This registration may not be amended after the first result commit."**

C07, and it is the first position in `CONSTRAINT-INVENTORY-001` §3.2 that has been MEASURED
rather than ranked.

WHY THIS FILE EXISTS, AND WHY ITS EVIDENCE IS A MUTATION AND NOT AN ARGUMENT
----------------------------------------------------------------------------
C07's `machine` cell named `test_registrations_precede_their_instruments.py`, marked
ADJACENT. That file's own docstring says why the pointer is not coverage, in its own words:

    "It cannot see a registration edited after its result existed."

`-46` ruled that a grade is earned by a mutation going red, never by a cell naming a file.
So `-47` made the move C07 forbids — appended an amendment section to `REG-001` and
**committed it**, on a scratch copy, with the whole suite behind it — and the suite stayed
green. Probe `R1` in `scripts/mutation_control.py`. That green is the warrant for this file.

THE GREEN WAS ALMOST A LIE, AND THAT IS THE SESSION'S FIRST LESSON
------------------------------------------------------------------
`mutation_control.py` as `-46` shipped it excluded `.git` from every scratch copy, because a
scratch copy does not need history to run the suite. But nine tests in this estate — the
whole git axis, including the only machine anywhere near C07 — **skip** with *"not a git work
tree"*. Under that harness R1 would have come back green while proving nothing: the harness
would have deleted the only candidate guard and then reported its absence as a measurement.

    A MUTATION THE HARNESS CANNOT SEE REPORTS EVERY GUARD IN THE UNSEEN PART OF THE
    ESTATE AS ABSENT.

So `.git` is now copied on request (`{"git": True}`) and R1 was re-run under a real work
tree before a line of this file was written. `-37` found that a mutation which does not
mutate reports a guard as weak; this is the same tell one level up, in the instrument built
to catch it.

WHAT THIS GUARD BINDS, EXACTLY
-------------------------------
One registration. `REG-001` §5 is the only document in `docs/preregistration/` that makes
this promise, and `test_reg001_is_still_the_only_registration_that_promises_this` holds that
scope honest: if a second registration adopts the sentence, this file goes red saying
**EXTEND ME**, which is a scope failure and not a violation. `-45`'s provenance lesson is
the reason for the narrowness — binding a constraint to documents that never made its
promise is the same error as citing an address that does not say what you claim.

The mechanical form is *ancestry*, not date. A commit touching `REG-001` is an amendment iff
the result's introducing commit is an **ancestor** of it. Dates lie under rebase and cherry-
pick; ancestry is what "after the first result commit" means in a repository.

WHAT IT IS NOT, AND THE TWO CLEAN ADDENDA THAT PROVE THE DISTINCTION MATTERS
----------------------------------------------------------------------------
`9b3b013` amended `PRE-002` and `REG-008` after both of their results existed — dated
addenda, marked as written after the fact, disclosing violations that had lived only in
`tests/`. Those are **not** C07 violations and this guard does not flag them, because
neither registration ever promised not to be amended. A guard that flagged them would be
enforcing a rule nobody wrote, and would be deleted the first time it fired.

WHAT IT CANNOT DO
------------------
It cannot see an amendment made in the working tree and never committed — that is a dirty
tree, not a violation of a rule about history. It cannot see content: a commit touching
`REG-001` to fix a typo is red, which is correct, because §5 admits no exception and the
disciplined move is `PRE-002`'s dated `## AMENDMENTS` section in a document that permits
one. And it skips outside a git work tree, because a source tarball is a legitimate way to
read this repository — see the module docstring of
`test_registrations_precede_their_instruments.py`, whose convention this follows.
"""
from __future__ import annotations

import pathlib
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREREG = ROOT / "docs" / "preregistration"

# EXPLICIT, never inferred. `-47`'s scratch audit built this mapping by stem-matching and
# silently paired REG-009 with `RESULT-REG-009-band-count-filled.md` — alphabetically first,
# and the wrong document. An inferred map is a provenance claim (`-45`).
REGISTRATION = "REG-001-p3-second-layer.md"
RESULT = "RESULT-REG-001.md"

# §5's sentence, which is the antecedent of everything below (`-42`).
RULE = "This registration may not be amended after the first\nresult commit"

PREFIXES = ("REG-", "PRE-", "CONSTRUCTION-")


# --------------------------------------------------------------------------- the detector
def _git(root: pathlib.Path, *args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=str(root), capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {proc.stderr.strip()}")
    return proc.stdout.strip()


def _is_work_tree(root: pathlib.Path) -> bool:
    proc = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                          cwd=str(root), capture_output=True, text=True)
    return proc.returncode == 0 and proc.stdout.strip() == "true"


def _first_commit(root: pathlib.Path, rel: str) -> str | None:
    out = _git(root, "rev-list", "--reverse", "HEAD", "--", rel)
    return out.split("\n")[0] if out else None


def amendments_after(root: pathlib.Path, registration: str, result: str) -> list[str]:
    """Commits touching `registration` that have `result`'s introducing commit as ancestor.

    This is the whole detector, and it is a pure function of the repository so that
    `test_the_detector_fires_on_a_synthetic_amendment` can run it against a history built
    for the purpose. A guard whose logic only exists inline in an assertion cannot be shown
    to fire (`-43`: a non-vacuity test must exercise the real path).
    """
    pivot = _first_commit(root, result)
    if pivot is None:
        return []
    out = []
    for sha in _git(root, "rev-list", "HEAD", "--", registration).split("\n"):
        if not sha or sha == pivot:
            continue
        anc = subprocess.run(["git", "merge-base", "--is-ancestor", pivot, sha],
                             cwd=str(root), capture_output=True)
        if anc.returncode == 0:
            out.append(sha)
    return out


@pytest.fixture(scope="module")
def repo() -> pathlib.Path:
    if not _is_work_tree(ROOT):
        pytest.skip("not a git work tree")
    return ROOT


# ------------------------------------------------------------------- the antecedent (-42)
def test_the_rule_is_still_in_force():
    """`-42`: a conditional constraint's guard must assert its antecedent.

    If §5 loses this sentence the correct report is LOST WARRANT — *this rule no longer
    applies, retire me* — and not a violation. Different failures, different messages.
    """
    text = (PREREG / REGISTRATION).read_text()
    flat = " ".join(text.split())
    assert " ".join(RULE.split()) in flat, (
        f"LOST WARRANT: {REGISTRATION} §5 no longer carries the no-amendment sentence. "
        "This guard enforces a rule that has been withdrawn — read §5 and retire or "
        "re-anchor this file. Do NOT delete the guard to make the suite green."
    )


def test_both_documents_are_in_history(repo):
    """A rename that empties the check must be loud, not silent.

    Either path resolving to no commit would make `amendments_after` return `[]` and the
    guard below would pass over nothing while reading as coverage — `-44`'s false-green
    class, in the one shape a path-based test is prone to.
    """
    assert _first_commit(repo, f"docs/preregistration/{REGISTRATION}"), REGISTRATION
    assert _first_commit(repo, f"docs/preregistration/{RESULT}"), RESULT


def test_reg001_is_still_the_only_registration_that_promises_this():
    """Scope honesty. A red here means EXTEND ME, not: somebody violated something.

    `CONSTRAINT-INVENTORY-001` is excluded because it QUOTES the rule rather than making
    the promise — `-33`'s tell, that a guard must scan assertions and not quotations.
    """
    needle = "may not be amended"
    promising = sorted(
        p.name for p in PREREG.glob("*.md")
        if p.name.startswith(PREFIXES) and not p.name.startswith("RESULT")
        and needle in p.read_text()
    )
    assert promising == [REGISTRATION], (
        f"registrations carrying {needle!r} are {promising}, not just [{REGISTRATION}]. "
        "EXTEND THIS GUARD to cover the new one — its scope is a fact about the estate, "
        "and a guard that silently under-covers is the defect this file was built from."
    )


# -------------------------------------------------------------------------- the guard
def test_the_registration_was_not_amended_after_its_result_commit(repo):
    found = amendments_after(repo, f"docs/preregistration/{REGISTRATION}",
                             f"docs/preregistration/{RESULT}")
    assert found == [], (
        f"REG-001 §5 VIOLATED: {len(found)} commit(s) touched {REGISTRATION} after "
        f"{RESULT} was introduced: {[s[:8] for s in found]}. §5 admits no exception. "
        "The disciplined move is a dated addendum in a registration that permits one "
        "(PRE-002's ## AMENDMENTS section); REG-001 does not."
    )


# ------------------------------------------------------------- non-vacuity, on real git
def test_the_detector_fires_on_a_synthetic_amendment(tmp_path):
    """`-43`: feed the guard its own forbidden move, and assert the CONJUNCTION.

    Both legs run against the SAME synthetic repository, so a detector that returned `[]`
    unconditionally — or non-empty unconditionally — fails one of them. Asserting only the
    red leg would pass for a function that flags everything; asserting only the green leg
    would pass for a function that flags nothing. The pair is the test.
    """
    root = tmp_path / "synthetic"
    root.mkdir()
    reg, res = "reg.md", "result.md"
    ident = ["-c", "user.name=t", "-c", "user.email=t@invalid"]

    def commit(msg: str):
        _git(root, "add", "-A")
        _git(root, *ident, "commit", "-q", "-m", msg)

    _git(root, "init", "-q", "-b", "main")
    (root / reg).write_text("the registration\n")
    commit("register")
    (root / res).write_text("the result\n")
    commit("result")

    # LEG 1 — a compliant history: the registration was never touched after the result.
    assert amendments_after(root, reg, res) == [], (
        "the detector reports an amendment in a history that has none — it would flag "
        "REG-001 forever and be deleted as a false alarm"
    )

    # LEG 2 — the forbidden move, and nothing else changed.
    (root / reg).write_text("the registration\n\n## AMENDMENT\n\nadded after the result\n")
    commit("amend the registration after its result")
    found = amendments_after(root, reg, res)
    assert len(found) == 1, (
        f"the detector missed an amendment committed after the result: {found}. This is "
        "the exact move probe R1 makes on REG-001, and the reason this file exists."
    )
