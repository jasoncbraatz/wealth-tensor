"""wealthTensor-58 · the papers' quoted test counts are DERIVED, not asserted.

WHY THIS EXISTS. `REVIEW-004` A3 (2026-08-12): *"The test count contradicts itself across the
batch. Paper II says 18 tests; Paper III says 100 at the pinned commit; the suite today runs
121. One repository, three numbers, visible to anyone with both PDFs open."* Four days later
the head suite ran 1068 and nothing had been fixed, because the repair was prose and prose
rots. `END-TO-END-001` leg E5 asked the sharper version — *is any paper's quoted count
invariant to a sibling paper adding tests to the same suite?* — and could not decide it
(`docs/RESULT-END-TO-END-001-E5.md` §3.3, the registration's clauses are not complements).
This module is the repair that outlives both: every count either paper quotes is recomputed
here from the repository and asserted against the manuscript.

THE TWO KINDS OF COUNT, AND WHY ONLY ONE OF THEM CAN DRIFT.

  * Paper III's counts are PINNED to commit d655501 and are read back out of git at that
    commit. They cannot drift with head; they can still be mistyped, and they were never
    once verified between 2026-08-05 and 2026-08-16.
  * Paper II's 18 is scoped to `tests/test_redistribution.py` at HEAD, in the present tense,
    with no pin. **That is the number a sibling can move** -- including by E5's own
    pre-registered repair, which would split a guard in that very module and take it to 19.
    It is asserted against the live tree, which is the point.

A NOTE ON THE COUNTING RULE. `def test_` at module scope, which is the same rule the papers'
own sentences use ("the 18 tests in tests/test_redistribution.py") and NOT pytest's collected
count -- the suite parametrises, so collection at head is 1068 against 566 definitions. If a
future session wants the collected number in a paper, it needs a different derivation and a
different sentence; do not quietly repoint these asserts at `--collect-only`.
"""
import pathlib
import re
import subprocess

REPO = pathlib.Path(__file__).resolve().parent.parent
PIN = "d655501"

PAPER_II = REPO / "docs/papers/paper-II-redistribution/paper-II.md"
PAPER_III = REPO / "docs/papers/paper-III-dual-tensor/paper-III.md"

PAPER_III_MODULES = [
    "tests/test_edgar.py",
    "tests/test_lag.py",
    "tests/test_lambda_sensitivity.py",
]
PAPER_II_MODULE = "tests/test_redistribution.py"

DEF_TEST = re.compile(r"^def test_", re.MULTILINE)


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True, text=True, check=True,
    ).stdout


def _defs_at_pin(path: str) -> int:
    return len(DEF_TEST.findall(_git("show", f"{PIN}:{path}")))


def _defs_at_head(path: str) -> int:
    return len(DEF_TEST.findall((REPO / path).read_text()))


def _flat(path: pathlib.Path) -> str:
    """The manuscript with newlines collapsed, so a markdown wrap cannot defeat a phrase grep."""
    return " ".join(path.read_text().split())


def test_the_pin_still_names_a_commit_this_repository_has():
    """If this fails, every number below is unanchored and the papers are citing a ghost."""
    assert _git("cat-file", "-t", PIN).strip() == "commit"


def test_paper_iii_suite_total_at_the_pin_is_what_paper_iii_says():
    """100 -- verified for the first time in wealthTensor-58, eleven days after it was written."""
    files = [f for f in _git("ls-tree", "--name-only", PIN, "tests/").split() if f.endswith(".py")]
    total = sum(_defs_at_pin(f) for f in files)
    assert total == 100, f"suite at {PIN} holds {total} tests, Paper III says 100"
    assert f"held **{total}** tests" in _flat(PAPER_III)


def test_paper_iii_paper_scoped_count_at_the_pin_is_what_paper_iii_says():
    """62 of the 100. The other 38 hold a sibling's claims -- 20 of them a WITHDRAWN sibling's."""
    scoped = sum(_defs_at_pin(m) for m in PAPER_III_MODULES)
    assert scoped == 62, f"Paper III's modules hold {scoped} tests at {PIN}, the paper says 62"
    assert f"the **{scoped}** in" in _flat(PAPER_III)


def test_paper_iii_names_every_module_it_counts():
    """A subtotal whose modules are not named is a number a reader cannot check."""
    flat = _flat(PAPER_III)
    for module in PAPER_III_MODULES:
        assert f"`{module}`" in flat, f"Paper III counts {module} but never names it"


def test_paper_ii_module_count_is_live_and_is_what_paper_ii_says():
    """THE ONE THAT CAN MOVE. Present tense, no pin, and a sibling's repair would break it."""
    live = _defs_at_head(PAPER_II_MODULE)
    assert live == 18, f"{PAPER_II_MODULE} holds {live} tests at head, Paper II says 18"
    flat = _flat(PAPER_II)
    assert f"the **{live}** tests in `{PAPER_II_MODULE}`" in flat


def test_paper_ii_does_not_claim_both_named_guards_are_in_the_counted_module():
    """Bug spray, wealthTensor-58. Paper II §1 said the claims are held by '18 tests INCLUDING
    two that exist specifically to make overclaiming fail loudly'. Only one of the two is in
    the counted module: the other lives in tests/test_excess_demand.py. §7 never claimed
    otherwise; §1 compressed §7 and lost the distinction."""
    assert "18 tests including two" not in _flat(PAPER_II)
    assert len(DEF_TEST.findall((REPO / "tests/test_excess_demand.py").read_text())) > 0
    assert "test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result" not in (
        REPO / PAPER_II_MODULE
    ).read_text(), "the guard moved into the counted module; Paper II §1's old wording is now true"
