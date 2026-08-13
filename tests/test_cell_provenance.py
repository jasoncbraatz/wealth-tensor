"""The guard for the defect wealthTensor-20 and -21 each found by READING: a §5.4 cell
whose number came from a run other than the one the sentence is reporting.

WHY THIS EXISTS
---------------
§5.4 is the one section of paper III that prints numbers from TWO runs side by side --
the published crawl (`RESULT-REG-003`) and REG-006's re-crawl, in a repaired and an
unrepaired arm (`RESULT-REG-006`). Every sentence there is a comparison, and a comparison
is only as good as the claim that both halves came from the same place.

    A NUMBER FROM THE WRONG RUN IS INDISTINGUISHABLE, ON THE PAGE, FROM A NUMBER FROM
    THE RIGHT ONE. Both are plausible, both are the right order of magnitude, and both
    round the way a reader expects.

Twice now the section has shipped one anyway, and both times the conclusion happened to
survive while the attribution did not:

  * `-20` -- the PP&E × goodwill cell juxtaposed PUBLISHED-crawl numbers (4.35×, 4.03×)
    against REPAIRED ones (3.99×, 2.17×) and attributed the whole movement to the repair.
    The same-crawl original is 3.63× / 4.14×, and on one crawl the repair *raises* retail.
  * `-21` -- the intangible-with-goodwill pair shipped as "5.83× and 2.41×"... printed as
    **5.83× and 2.34×**: retail's half from the published run, computer services' half
    from REG-006's new crawl, in a sentence whose whole job was to report the published
    result. `RESULT-REG-003` says 2.41× (p 0.0020).

Both were caught by a human re-reading two result docs against one paragraph. That does
not scale and it does not survive a handoff. This test does.

WHAT IT CHECKS, AND WHAT IT CANNOT
----------------------------------
It checks two things, and the second is the load-bearing one:

  1. The set of ×-multipliers §5.4 prints is EXACTLY the set declared in `CELLS` below.
     A number cannot enter or leave the section without someone declaring where it came
     from -- which is the step `-21` found missing (REG-006 §4's constants list
     enumerated what the run READ, never what it WROTE into the manuscript).
  2. Every value declared `PUBLISHED` resolves in `RESULT-REG-003.md`, and every value
     declared `RECRAWL` resolves in `RESULT-REG-006.md`. This is the assertion that
     fails on the `-21` defect: 2.34× declared PUBLISHED is not in REG-003 and the suite
     says so.

It CANNOT tell you a correctly-sourced number is sitting in the wrong SLOT in a sentence
-- that is a claim about prose, and prose is not parseable here. What it removes is the
silent case: the section's numbers and their provenance can no longer drift from what a
human verified once without the suite going red.

Offline, like every test here. It reads the manuscript and the two result docs.
"""

from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPER = ROOT / "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md"
PREREG = ROOT / "docs" / "preregistration"

PUBLISHED = "RESULT-REG-003.md"   # the crawl the manuscript's §5.4 table was built on
RECRAWL = "RESULT-REG-006.md"     # REG-006's re-crawl, original and corrected arms

# Every ×-multiplier §5.4 prints, and the run that owns it.
# `-21`: 2.41× is the published indefinite × goodwill cell for computer services.
# 2.34× is the SAME cell on the re-crawl, where it is the value on BOTH arms -- which is
# exactly why substituting it was invisible.
CELLS = {
    # --- the headline, published table -------------------------------------------
    "4.12×": (PUBLISHED, "headline lift, retail"),
    "2.02×": (PUBLISHED, "headline lift, computer services"),
    # --- pairwise cells, published ------------------------------------------------
    "5.83×": (PUBLISHED, "indefinite-lived intangible × goodwill, retail"),
    "2.41×": (PUBLISHED, "indefinite-lived intangible × goodwill, computer services"),
    "3.33×": (PUBLISHED, "finite-lived intangible × goodwill, retail"),
    "2.22×": (PUBLISHED, "finite-lived intangible × goodwill, computer services"),
    "4.35×": (PUBLISHED, "PP&E × goodwill, retail"),
    "4.03×": (PUBLISHED, "PP&E × goodwill, computer services"),
    # --- the re-crawl: repaired arm ------------------------------------------------
    "3.99×": (RECRAWL, "PP&E × goodwill, retail, repaired"),
    "2.17×": (RECRAWL, "PP&E × goodwill, computer services, repaired"),
    "2.10×": (RECRAWL, "headline lift, computer services, repaired"),
    "5.86×": (RECRAWL, "indefinite × goodwill, retail, repaired"),
    "3.35×": (RECRAWL, "finite × goodwill, retail, repaired"),
    # --- the re-crawl: same-crawl unrepaired control (REG-007 F8) -------------------
    "3.63×": (RECRAWL, "PP&E × goodwill, retail, unrepaired"),
    "4.14×": (RECRAWL, "PP&E × goodwill, computer services, unrepaired"),
    "2.01×": (RECRAWL, "headline lift, computer services, unrepaired"),
    "3.34×": (RECRAWL, "finite × goodwill, retail, unrepaired"),
    "2.21×": (RECRAWL, "finite × goodwill, computer services, unrepaired"),
    # --- identical on both arms of the re-crawl ------------------------------------
    "4.01×": (RECRAWL, "headline lift, retail, both arms"),
    "2.34×": (RECRAWL, "indefinite × goodwill, computer services, both arms"),
}

SECTION_START = "### 5.4 · "
SECTION_END = "## 6 · "


@pytest.fixture(scope="module")
def section_54() -> str:
    text = PAPER.read_text(encoding="utf-8")
    start = text.index(SECTION_START)
    end = text.index(SECTION_END, start)
    return text[start:end]


@pytest.fixture(scope="module")
def results() -> dict[str, str]:
    return {name: (PREREG / name).read_text(encoding="utf-8")
            for name in (PUBLISHED, RECRAWL)}


def _multipliers(text: str) -> set[str]:
    return set(re.findall(r"\d+\.\d+×", text))


def _reported(text: str) -> set[str]:
    """The multipliers a result doc REPORTS -- table rows only, not prose.

    Scoping this to tables is not tidiness, it is the difference between a guard that
    works and one that decays. The first run of this file failed its own witness: `-21`'s
    correction note in RESULT-REG-006 §4 *quotes* the published 2.41× while explaining why
    substituting it was wrong, and a whole-file search read that quotation as REG-006
    reporting the value. Prose about a number is not a run reporting it. Every figure
    either result doc reports lives in a table row.
    """
    return set(re.findall(r"\d+\.\d+×",
                          "\n".join(l for l in text.split("\n")
                                    if l.lstrip().startswith("|"))))


def test_section_54_prints_no_undeclared_multiplier(section_54):
    """A number cannot enter §5.4 without someone declaring which run it came from.

    This is the step REG-006 §4's constants list skipped: it enumerated what the run
    READ out of RESULT-REG-003, not what it WROTE into the manuscript.
    """
    printed = _multipliers(section_54)
    undeclared = printed - set(CELLS)
    assert not undeclared, (
        f"§5.4 prints multipliers with no declared provenance: {sorted(undeclared)}. "
        f"Add each to CELLS with the run that owns it -- RESULT-REG-003 for the published "
        f"crawl, RESULT-REG-006 for the re-crawl."
    )


def test_every_declared_cell_is_still_printed(section_54):
    """The mirror direction: a declared cell that vanished means CELLS has gone stale."""
    printed = _multipliers(section_54)
    vanished = set(CELLS) - printed
    assert not vanished, (
        f"CELLS declares multipliers §5.4 no longer prints: {sorted(vanished)}. "
        f"If the section legitimately dropped them, drop them here too."
    )


@pytest.mark.parametrize("value,owner", [(v, CELLS[v][0]) for v in sorted(CELLS)])
def test_cell_resolves_in_the_run_that_owns_it(value, owner, results):
    """THE ASSERTION THAT FAILS ON THE -21 DEFECT.

    2.34× declared PUBLISHED is not in RESULT-REG-003; the published cell is 2.41×.
    """
    what = CELLS[value][1]
    assert value in _reported(results[owner]), (
        f"§5.4 prints {value} ({what}) and declares it owned by {owner}, "
        f"but no table in {owner} reports that value. Either the number is sourced from "
        f"the wrong run -- the defect this file exists for -- or the declaration is wrong."
    )


def test_the_two_runs_really_do_disagree_about_this_cell(results):
    """The witness that the guard above is not vacuous.

    If REG-003 and REG-006 agreed everywhere, every assertion would pass under any
    declaration and this file would prove nothing. They disagree on precisely the cell
    that was substituted: 2.41× published, 2.34× on the re-crawl.
    """
    published, recrawl = _reported(results[PUBLISHED]), _reported(results[RECRAWL])
    assert "2.41×" in published
    assert "2.41×" not in recrawl, (
        "A table in the re-crawl file now reports the published indefinite × goodwill "
        "value, so the guard can no longer separate the two runs on this cell."
    )
    assert "2.34×" in recrawl
    assert "2.34×" not in published, (
        "A table in the published file now reports the re-crawl value, so substituting "
        "one for the other would no longer be detectable here."
    )
