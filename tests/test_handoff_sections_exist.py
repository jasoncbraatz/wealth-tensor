"""G-SEC, enforced: a §N a handoff NAMES must EXIST in the paper it names.

SM 1217564707330383 / WT-112. `-69`'s HANDOFF.md assigned `-70` to read "Paper IV §4–§11".
Paper IV's last numbered section is §10; §11 is PAPER III's number for Limitations. The
number was inherited from a sibling manuscript, repeated across the prose at-bat, the
`next_at_bat` front-matter field and the forcing line, and survived a full gate pass
(v2.60, PASS, CANNOT VERIFY: 0). `scripts/wt_handoff_sections.py` detects it; this file is
what makes the detector BINDING.

THE RED-PROOF IS THE REAL FILE, NOT A FIXTURE. `test_the_wt112_defect_is_caught` reads the
handoff as it was actually committed at e65feb6 and asserts the check fires on it. A
control demonstrated only against text the same session wrote is a control demonstrated
against its own assumptions -- the same reason `test_defensive_count.py` reads the
committed baseline rather than recomputing one.

The section registry used for that historical proof is the RECORDED one (III is 11, IV is
10, II is 7 -- docs/done-criteria.tsv P5h), not today's papers on disk, so the control keeps
testing the DETECTOR even if a paper later grows a §11. Today's papers are asserted
separately, against today's handoff.
"""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wt_handoff_sections as wts  # noqa: E402

# The commit that shipped the defect, and the phrase to look for in it. Both are facts
# about git history, so neither can rot under us.
WT112_SHA = "e65feb696996a473d4476c0035572c26c29dc812"


def _handoff_at(sha):
    out = subprocess.run(["git", "show", f"{sha}:docs/HANDOFF.md"], cwd=ROOT,
                         capture_output=True, text=True)
    if out.returncode != 0:
        pytest.skip(f"{sha} not in this clone: {out.stderr.strip()}")
    return out.stdout


def test_the_wt112_defect_is_caught():
    """The real committed handoff, the real wrong number, the check must fire."""
    problems, stats = wts.scan(_handoff_at(WT112_SHA), wts.FIXTURE)
    assert problems, ("the check went green on the very handoff it exists to catch; "
                      f"scope actually parsed was {stats}")
    assert all("paper-IV has no §11" in p for p in problems), problems
    # Filed as "repeated three times"; the committed file carries it FOUR times. The
    # count is asserted low-bound rather than exactly, because the point is that a
    # repeated wrong number is repeated, not that it is repeated n times.
    assert len(problems) >= 3, problems


def test_the_neighbouring_handoffs_are_clean():
    """A detector that fires on everything has not detected anything."""
    for sha in ("HEAD",):
        problems, _ = wts.scan(_handoff_at(sha), wts.FIXTURE)
        assert not problems, (sha, problems)


@pytest.mark.parametrize("name,text,want_problem", wts.CONTROLS)
def test_controls(name, text, want_problem):
    """Every case the module ships, positive and negative, run as real tests."""
    problems, _ = wts.scan(text, wts.FIXTURE)
    assert bool(problems) == bool(want_problem), (name, problems)


def test_selftest_command_is_green():
    """The drill a session actually runs by hand must agree with this suite."""
    out = subprocess.run([sys.executable, "scripts/wt_handoff_sections.py", "--selftest"],
                         cwd=ROOT, capture_output=True, text=True)
    assert out.returncode == 0, out.stdout + out.stderr


def test_scope_is_reported_not_rounded_up():
    """wealthTensor-95: a check whose scope is DISCOVERED reports what it PARSED.

    So an unscoped reference must be counted as unscoped, never silently as checked --
    otherwise the leg's own summary line is the thing that lies.
    """
    text = "Paper IV §4-§10 is the at-bat.\nbecause §911 opens with a floor.\n"
    problems, stats = wts.scan(text, wts.FIXTURE)
    assert not problems
    assert stats["checked"] == 2 and stats["unscoped"] == 1, stats


def test_todays_handoff_names_only_sections_todays_papers_have():
    """The live state assertion, against the papers actually on disk."""
    papers = wts.discover_papers()
    assert papers, "no docs/papers/*/paper-*.md found -- G-SEC would be a silent pass"
    sections = {r: wts.paper_sections(p) for r, p in papers.items()}
    assert all(sections.values()), sections
    problems, _ = wts.scan((ROOT / "docs" / "HANDOFF.md").read_text(), sections)
    assert not problems, problems
