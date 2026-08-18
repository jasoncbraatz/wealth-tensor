"""wealthTensor-81 · Paper IV may not claim an exhaustive suite-wide guard count.

WHY THIS EXISTS. Paper IV §10 said *"Two tests in the suite exist specifically to make
overclaiming fail loudly"* and named two. That is a count over the whole suite, and it was
wrong by a wide margin: `test_the_forbidden_claim_is_red` alone lives in two registration
modules, Paper III names `test_pre001_constants_are_what_was_registered` for the same
office, and there is a registered tripwire class besides.

This is the same shape `test_paper_test_counts_are_derived.py` was written for and the same
shape III-17 found in Paper III §11 — a count over a set the repository can enumerate,
written once in prose and never checked again. `tests/test_paper_test_counts_are_derived.py`
covers Papers II and III. Paper IV had no equivalent; this is it.

WHAT IT ASSERTS, AND WHAT IT DELIBERATELY DOES NOT. It does not assert HOW MANY
overclaim-forbidding tests the suite holds — that set has no mechanical definition and a
number pulled from a regex would be exactly the false precision this file exists to stop.
It asserts (a) that the manuscript does not make the exhaustive claim, (b) that both tests
it names still exist, which is what apparatus row P5j requires, and (c) that the two
sibling guards the repaired sentence cites are real, so the repair cannot rot into its own
phantom.
"""
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
PAPER_IV = REPO / "docs/papers/paper-IV-composition/paper-IV.md"
TESTS = REPO / "tests"

NAMED_BY_PAPER_IV = (
    "test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result",
    "test_a_flat_gini_does_not_mean_a_bounded_one",
)
NAMED_AS_EVIDENCE_OF_MORE = (
    "test_the_forbidden_claim_is_red",
    "test_pre001_constants_are_what_was_registered",
)


def _flat(path):
    """The manuscript with newlines collapsed, so a markdown wrap cannot defeat a phrase grep."""
    return " ".join(path.read_text(encoding="utf-8").split())


def _defined(name):
    pattern = re.compile(r"^def %s\b" % re.escape(name), re.MULTILINE)
    return [p.name for p in sorted(TESTS.glob("test_*.py"))
            if pattern.search(p.read_text(encoding="utf-8"))]


def test_paper_iv_does_not_claim_the_suite_holds_exactly_two_such_tests():
    """The defect itself. The old sentence, and the near-miss forms of it."""
    flat = _flat(PAPER_IV)
    for forbidden in (
        "Two tests in the suite exist specifically to make overclaiming fail loudly",
        "The two tests in the suite that exist",
        "the only two tests in the suite",
    ):
        assert forbidden not in flat, (
            "Paper IV §10 is again asserting an exhaustive count of the suite's "
            "overclaim-forbidding tests. There are more than two. Name the ones you mean "
            "and say the suite holds more; do not count a set nobody enumerated."
        )


def test_paper_iv_still_names_both_guards_apparatus_row_P5j_requires():
    flat = _flat(PAPER_IV)
    for name in NAMED_BY_PAPER_IV:
        assert name in flat, "P5j: Paper IV must name %s" % name


def test_every_guard_paper_iv_names_actually_exists():
    for name in NAMED_BY_PAPER_IV:
        assert _defined(name), "Paper IV names %s and no module defines it" % name


def test_the_sentence_s_evidence_that_there_are_more_than_two_is_real():
    """The repaired sentence cites two further guards as its warrant. If either disappears,
    the repair becomes an assertion about a set the reader cannot check -- which is the
    defect it replaced."""
    modules = _defined("test_the_forbidden_claim_is_red")
    assert len(modules) >= 2, (
        "Paper IV §10 says test_the_forbidden_claim_is_red appears in two registration "
        "modules; it now appears in %s" % modules
    )
    assert _defined("test_pre001_constants_are_what_was_registered"), (
        "Paper IV §10 credits Paper III with naming "
        "test_pre001_constants_are_what_was_registered; it no longer exists"
    )


def test_this_file_is_not_vacuous():
    """A negative-only guard passes on an empty file. This proves the reader works."""
    assert "overclaim" in _flat(PAPER_IV).lower()
    assert not _defined("test_a_name_no_module_defines_xyzzy")
