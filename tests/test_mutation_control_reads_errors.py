"""The mutation harness can see a red that arrives as an ERROR, and never calls one green.

WHY THIS EXISTS
---------------
`mutation_control.py` is the instrument that earns every `FOR` and `BINDS` in
`CONSTRAINT-INVENTORY-001` §1. Its output vocabulary has exactly two words, and one of
them is load-bearing: **a probe with no catchers is the evidence a guard is needed.** So a
green is not "nothing happened" — it is a documented claim that the estate is unguarded at
that position, and it is the claim sessions act on.

`-51` ran the first mutation ever aimed at a MODULE rather than a document. Renaming the
registered `TIER_TAGS` block in `edgar.py` broke the import in three files, pytest stopped
at collection having run no test at all, and the harness reported:

    [GREEN]  G8  edit the registered TIER_TAGS block [git]

because it parsed only lines beginning `FAILED ` and pytest had emitted `ERROR ` lines and
then given up. **The loudest possible red — a suite that will not collect — was the one
shape the instrument could not see, and it printed as the strongest possible claim about
the estate's blindness.** The instrument was anti-monotonic in severity: the more damage a
probe did, the cleaner its green.

This is `-37`'s tell at the third level. `-37`: a mutation that does not mutate reports a
guard as weak. `-47`: a mutation the harness cannot SEE reports every guard in the unseen
part of the estate as absent. Here: **a red the harness cannot PARSE reports the guard as
absent** — and the parse, not the mutation, is what failed.

WHAT IS PINNED, AND WHY EACH HALF IS SEPARATELY NECESSARY
----------------------------------------------------------
Two independent things had to be true for that green, so two independent things are pinned:

1. **The recogniser sees `ERROR`.** Predicated on CONTRIBUTION, never on absence
   (`-49`/`-50`): the test does not assert "an ERROR line is matched", which a recogniser
   matching *everything* would also satisfy. It asserts that adding the ERROR line to a
   fixed transcript raises the count by exactly that line — and, in the other direction,
   that a non-`tests/` path and a bare mention are not counted.
2. **A run that did not complete is never green.** Even with the recogniser fixed, a
   collection failure can leave zero attributable catchers; `is_unparsed_red` is what
   stops that becoming a claim about the estate. Fixing only the recogniser leaves the
   defect reachable, which is why this is not one test.

The invocation flag is pinned too, in its own test, because both halves above are correct
and useless if the summary lines are never requested: `-rf` prints failures only.
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from mutation_control import CATCHER_RE, is_unparsed_red  # noqa: E402

MC = ROOT / "scripts" / "mutation_control.py"

#: A pytest short-summary transcript with one ordinary failure in it.
_FAILED_ONLY = """\
FAILED tests/test_alpha.py::test_one - AssertionError
1 failed, 3 passed
"""

#: The same transcript as it looks when a probe breaks an import instead: pytest reports
#: the affected files with `ERROR`, and past a handful it stops before running anything.
_ERROR_LINE = "ERROR tests/test_beta.py - NameError: name 'TIER_TAGS' is not defined\n"


# --------------------------------------------------------------- 1 · the recogniser
def test_an_error_line_contributes_a_catcher():
    """CONTRIBUTION, not presence. A recogniser that matched every line would pass an
    `assert "tests/test_beta.py" in matched`; it cannot pass this, because the assertion
    is about the DIFFERENCE the one added line makes to a fixed transcript."""
    before = set(CATCHER_RE.findall(_FAILED_ONLY))
    after = set(CATCHER_RE.findall(_FAILED_ONLY + _ERROR_LINE))
    assert after - before == {"tests/test_beta.py"}, (
        "adding an ERROR line to the transcript did not add exactly one catcher. This is "
        "the -51 defect: a probe that breaks an import produces ERROR lines, not FAILED "
        "ones, and a harness blind to them reports the loudest red as GREEN — which this "
        "file's own vocabulary defines as 'no guard exists'."
    )


def test_the_ordinary_failure_is_still_recognised():
    """The other direction of the same pair. A recogniser narrowed to ERROR would pass
    the test above and break every grade in the inventory."""
    assert set(CATCHER_RE.findall(_FAILED_ONLY)) == {"tests/test_alpha.py::test_one"}


def test_the_recogniser_is_not_indiscriminate():
    """Non-vacuity for the two tests above. Neither a summary line about a non-test path
    nor prose naming a test file may count as a catcher; if they did, the CONTRIBUTION
    assertions could be satisfied by a regex that matches anything."""
    noise = (
        "ERROR scripts/wt026_severe_test.py - NameError\n"
        "see tests/test_gamma.py for the worked example\n"
        "  FAILED tests/test_delta.py::test_indented\n"
    )
    assert set(CATCHER_RE.findall(noise)) == set(), (
        "the catcher recogniser matched something that is not a red test: it must be "
        "anchored at line start and scoped to tests/."
    )


# ------------------------------------------------- 2 · a run that did not complete
def test_a_collection_error_with_no_catchers_is_not_green():
    """pytest exits 2 when it is interrupted or collection fails. `-51`'s G8 landed here
    exactly: rc=2, nothing attributable, and the harness called it UNGUARDED."""
    assert is_unparsed_red(2, []) is True


def test_a_completed_run_with_no_catchers_is_still_a_real_green():
    """The other branch, and the one that matters for the ranking: rc=0 with no catchers
    is the genuine measurement this whole instrument exists to produce. `-51` re-ran the
    five recorded greens (R5a-R5e) under the fixed harness and all five returned rc=0 —
    so the fix moved no grade, and this test is what keeps it that way."""
    assert is_unparsed_red(0, []) is False
    assert is_unparsed_red(1, []) is False


def test_a_run_that_failed_hard_but_attributed_its_reds_is_not_unparsed():
    """`unparsed` is a CONJUNCTION — did not complete AND nothing attributable. Asserting
    only the rc leg would flag every hard-stopped run whose reds we can in fact read."""
    assert is_unparsed_red(2, ["tests/test_beta.py"]) is False


# ------------------------------------------------------------- 3 · the invocation
def test_the_harness_asks_pytest_for_error_lines():
    """Both halves above are correct and useless if the ERROR summary is never printed.
    `-rf` requests failures only; the flag must ask for E as well."""
    src = MC.read_text(encoding="utf-8")
    assert '"-rf"' not in src, (
        "mutation_control.py invokes pytest with -rf, which prints FAILED lines and not "
        "ERROR lines. That is the -51 defect at its source. Use -rfE."
    )
    assert '"-rfE"' in src, (
        "mutation_control.py must invoke pytest with -rfE so that import errors reach the "
        "short summary the catcher recogniser reads."
    )
