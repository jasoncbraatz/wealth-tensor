"""wealthTensor-80 · III-17 · §11's count of the post-pin guards, derived rather than typed.

WHY THIS EXISTS
---------------
Paper III §11 quotes a suite total (100) and a paper-scoped subtotal (62), both pinned to
commit d655501, and `tests/test_paper_test_counts_are_derived.py` has held those two
against the repository since wealthTensor-58. The sentence immediately after them was not
held by anything:

    "...three of its additions guard claims this paper makes and change no model code:
     two for §3.1's closed form ... and one asserting the algebraic collapse §4 publishes"

`tests/test_lag.py` carries **six** post-pin additions, not three, and all six guard Paper
III claims. The three the sentence omitted were added at **cc1d198** (2026-08-12), whose own
commit subject is "REG-002 results, errata, ledger WT-088, and three tests S4.4 needed" —
**two days before the sentence was first written** (a74a4ca, 2026-08-14) and four before its
last edit (bde6d65, 2026-08-16). The sentence was never true; it was simply never derived.

WHAT THIS ASSERTS, AND WHY IT IS NOT A COMMENT WITH A SHA IN IT
---------------------------------------------------------------
`tests/test_manuscript_shas_are_instrumented.py` refuses a pin that lives only in prose, and
refuses the lazy repair of pasting the SHA into a comment. So this module states what the
§11 sentence is *for* and checks it:

  1 · the delta on `tests/test_lag.py` between the pin and HEAD is exactly six, and the
      manuscript says "six";
  2 · the six are the six named here, by name, so a seventh addition goes red rather than
      silently making the sentence wrong again;
  3 · the three §11 attributes to cc1d198 were introduced AT cc1d198 — absent at its parent,
      present at it — which is the only thing that SHA is doing in the manuscript;
  4 · none of the six touches model code: `src/` is byte-identical across cc1d198.

WHAT IT CANNOT SEE
------------------
It cannot judge whether a seventh test elsewhere in the suite guards a Paper III claim; §11
scopes its sentence to additions in this module and so does this guard. And it cannot tell
whether the three names are the *right* three for §4.4 — only that the manuscript and the
repository agree on which they are.
"""
from __future__ import annotations

import pathlib
import re
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER_III = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
MODULE = "tests/test_lag.py"
PIN = "d655501"
S44_COMMIT = "cc1d198"

DEF_TEST = re.compile(r"^def (test_\w+)", re.MULTILINE)

#: The two the closed form needs, the one §4 publishes, and the three §4.4 needed.
EXPECTED_ADDITIONS = {
    "test_deferred_information_is_exactly_linear_in_unobservability",
    "test_recognition_lag_is_not_linear_in_unobservability",
    "test_the_two_layer_recursion_collapses_to_the_form_limitation_4_publishes",
    "test_no_steady_state_deferral_ratio_once_decay_outruns_recognition",
    "test_the_crossing_rate_closed_form_44_publishes_is_exact",
    "test_the_first_rung_boundary_44_publishes_is_exact",
}
#: The three §11 attributes to S44_COMMIT by name.
FROM_S44_COMMIT = {
    "test_no_steady_state_deferral_ratio_once_decay_outruns_recognition",
    "test_the_crossing_rate_closed_form_44_publishes_is_exact",
    "test_the_first_rung_boundary_44_publishes_is_exact",
}


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(ROOT), *args],
                          capture_output=True, text=True)


def _names_at(rev: str, path: str = MODULE) -> set[str]:
    r = _git("show", f"{rev}:{path}")
    if r.returncode != 0:
        pytest.skip(f"{rev}:{path} is not in this checkout")
    return set(DEF_TEST.findall(r.stdout))


@pytest.fixture(scope="module")
def flat_paper() -> str:
    return " ".join(PAPER_III.read_text(encoding="utf-8").split())


def test_the_additions_are_exactly_the_six_named_here():
    """A seventh addition must break this, not the sentence in §11."""
    added = _names_at("HEAD") - _names_at(PIN)
    assert added == EXPECTED_ADDITIONS, (
        f"tests/test_lag.py's post-pin additions are {sorted(added)}, not the six §11 names. "
        "Update §11 and this set together, or §11 is wrong again."
    )


def test_paper_iii_says_six_and_not_three(flat_paper):
    """The count in the prose, derived from the repository rather than typed into it."""
    added = _names_at("HEAD") - _names_at(PIN)
    assert len(added) == 6, f"the module carries {len(added)} post-pin additions"
    assert "**six** of its additions" in flat_paper, "§11 does not say 'six of its additions'"
    assert "three of its additions" not in flat_paper, (
        "§11 has gone back to claiming three additions"
    )


def test_the_three_section_44_guards_were_introduced_at_the_commit_paper_iii_names(flat_paper):
    """The only work that SHA does in the manuscript, asserted instead of asserted-about."""
    assert f"**{S44_COMMIT}**" in flat_paper, f"§11 no longer names {S44_COMMIT}"
    at = _names_at(S44_COMMIT)
    before = _names_at(f"{S44_COMMIT}^")
    introduced = at - before
    assert FROM_S44_COMMIT <= introduced, (
        f"{S44_COMMIT} introduced {sorted(introduced)}; §11 attributes {sorted(FROM_S44_COMMIT)} to it"
    )


def test_none_of_the_additions_changed_model_code():
    """§11's 'and change no model code' — the clause that makes the sentence worth making."""
    r = _git("diff", "--name-only", f"{S44_COMMIT}^", S44_COMMIT, "--", "src/")
    if r.returncode != 0:
        pytest.skip("git unavailable")
    assert r.stdout.strip() == "", (
        f"{S44_COMMIT} touched model code: {r.stdout.strip()}"
    )
