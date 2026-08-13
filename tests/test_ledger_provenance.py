"""The provenance guard for §7's falsifier ledger -- the sibling of `test_cell_provenance`.

WHY THIS EXISTS
---------------
`test_cell_provenance.py` guards §5.4, where wealthTensor-20 and -21 each found a number
sourced from a run other than the one the sentence was reporting. §7 has the identical
exposure and more of it. Every row in that table is a RESTATEMENT: the run happened
somewhere else, was written up in a `RESULT-REG-00N.md`, and §7 prints a shortened,
rounded echo of it. Nine registered runs feed one table.

    A RESTATEMENT HAS NO SOURCE OF TRUTH ON ITS OWN PAGE. When a run is re-done -- and
    REG-006 re-crawled REG-003, and REG-008 re-instrumented REG-007 -- the result doc
    moves and the echo does not. Nothing in the repository noticed, because a stale echo
    is a well-formed sentence containing a plausible number.

That is the same defect §5.4 shipped twice, in a section with three times the surface.
The `-22` handoff teed this up as at-bat item 2; this file is it.

WHAT IT CHECKS
--------------
Four things, and the third is the one that would have caught a real defect:

  1. **Every row is classified.** Each claim row of §7 is either in `LEDGER` (it restates
     a registered run) or in `SIMULATION_ROWS` (its figures are produced by a script in
     this repository and no result doc reports them). A row cannot enter §7 without
     someone saying which. This is the generalisation of §5.4's undeclared-multiplier
     check, lifted from the number to the row -- necessary here because §7's numbers are
     not one clean token class the way `\\d+\\.\\d+×` was.
  2. **Every declared figure is still printed** in the row that declares it. Edit §7 and
     the ledger goes red rather than quietly describing a paragraph that no longer exists.
  3. **Every declared figure resolves in the run that owns it** -- and resolves on the
     surface where that run REPORTS, not merely somewhere in its file (see the surface
     note below).
  4. **The rounding is faithful.** §7 prints `0.103` where REG-008 reports `0.1025`, and
     `+0.014` where it reports `+0.0139`. Both are legitimate; `0.113` would not be. Each
     entry carries the source value and the check is that the printed figure is within
     half a unit of its own last decimal place. This is what makes a shortened echo
     verifiable instead of merely plausible, and it is the check with no analogue in
     `test_cell_provenance` -- §5.4 prints its multipliers at full precision.

THE REPORTING SURFACE, AND WHY IT IS NOT "BOLD"
----------------------------------------------
`test_cell_provenance` learned in `-21` that a whole-file search is not a provenance
check: REG-006 §4 *quotes* the published 2.41× while explaining why substituting it was
wrong, and grep cannot tell a quotation from a report. Its answer was to read table rows
only.

§7 cannot inherit that rule unchanged, because four of its figures -- REG-003's
`0.327-0.499` range and its `[1.135, 1.285]` shape interval -- are reported in REG-003's
prose and appear in no table. The obvious widening is "tables plus **bolded** spans,"
since these result docs bold what they report. That widening was measured before being
adopted, and it FAILS: REG-006's disallowed quotation of 2.41× is itself bolded, so
"bold" re-admits precisely the false positive `-21` paid to find.

So the surface is declared per figure instead. An entry is either `TABLE` -- the value
must appear in a table row of its owner -- or it carries an ANCHOR, a literal phrase that
must sit on the same line as the value. An anchor is a human's statement of where a
number reports, and it is exactly as narrow as the sentence that reports it.

WHAT IT CANNOT DO
-----------------
It cannot check a correctly-sourced figure sitting in the wrong slot of a sentence; that
is a claim about prose. And it deliberately does not chase REG-004's and REG-005's
simulation residuals (`2 × 10⁻¹³`, `5.4 × 10⁻³`). Those are reported to one significant
figure, where the half-a-last-place tolerance in check 4 is so wide it admits nearly
anything -- a green assertion that proves nothing is worse than an absent one, because it
reads as coverage. They are classified, named, and left unresolved on purpose.

AND IT COVERS §7 ONLY, WHICH IS NOT THE ONLY PLACE THESE FIGURES ARE RESTATED.
The mutation drill written alongside this file found that by accident: its first anchor
for REG-008's headline, `**0.103 against 0.030**`, matched at line 1432 -- inside §5.4,
where the existing guard reads multipliers and 0.103 is not one -- before it ever reached
§7's row, so the drill mutated an unwatched passage and reported a false miss. REG-003's
α̂ turned out to be printed **eleven times across five sections**.

`tests/test_restatement_reach.py` closes that, and is the reason the figures below are
worth keeping in one place: it pins, per section, how many times the manuscript prints
each figure THIS file declares, so a copy that drifts anywhere in paper III is caught.
The two files are coupled -- add an entry here without a reach declaration there and that
suite goes red.

Offline, like every test here. It reads the manuscript and the result docs.
"""

from __future__ import annotations

import pathlib
import re
from decimal import Decimal

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPER = ROOT / "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md"
PREREG = ROOT / "docs" / "preregistration"

SECTION_START = "## 7 · What was tested and survived"
SECTION_END = "## 8 · Abandoned approaches"

R2 = "RESULT-REG-002.md"   # the ladder draws
R3 = "RESULT-REG-003.md"   # the published crawl, recognition rate, off-diagonal
R6 = "RESULT-REG-006.md"   # the re-crawl, sequencing vs coupling
R7 = "RESULT-REG-007.md"   # the keyword-family disclosure instrument
R8 = "RESULT-REG-008.md"   # the entity-anchored instrument

TABLE = "TABLE"            # the value must appear in a table row of its owner

# --------------------------------------------------------------------------------------
# THE LEDGER.  (row-key, printed-in-§7, reported-by-the-run, owner, surface)
#
# `row` is a substring that must identify EXACTLY ONE claim row (asserted below, so a
# copy-pasted key cannot silently guard the wrong row).  `printed` is the figure as §7
# prints it, without units.  `source` is the figure as the owning run reports it.  Where
# the two differ, §7 is rounding, and check 4 proves the rounding is faithful.
# --------------------------------------------------------------------------------------
LEDGER = [
    # --- REG-002 · the ladder draws --------------------------------------------------
    ("inversion belongs to the ordering", "0.32", "0.318", R2, TABLE),
    ("inversion belongs to the ordering", "0.41", "0.414", R2, TABLE),
    ("inversion belongs to the ordering", "11.5", "11.5", R2, TABLE),
    ("inversion belongs to the ordering", "1.1", "1.1", R2, TABLE),
    ("inversion belongs to the ordering", "23.8", "23.8", R2, TABLE),
    ("knife edge in its top rung", "0.0079", "0.00789", R2, TABLE),
    ("Lumpy defers more", "1.30", "1.303", R2, TABLE),
    ("Lumpy defers more", "0.0123", "0.0123", R2, TABLE),
    ("validity region has a fitted boundary", "1.58", "1.58", R2, TABLE),
    ("validity region has a fitted boundary", "19.5", "19.5", R2, TABLE),
    ("Lag's 100% is partly the ladder", "66.2", "66.2", R2, TABLE),
    ("Lag's 100% is partly the ladder", "0.011", "0.011", R2, TABLE),

    # --- REG-003 · the published crawl -------------------------------------------------
    # The calibrated rate this row leans on is REG-003's, not REG-002's own.
    ("disclosed rectangle lies outside", "0.408", "0.4077", R3, TABLE),
    ("recognition rate is an order of magnitude", "0.408", "0.4077", R3, TABLE),
    ("recognition rate is an order of magnitude", "0.383", "0.383", R3, TABLE),
    ("recognition rate is an order of magnitude", "0.432", "0.432", R3, TABLE),
    # The range over every cut is REG-003's summary sentence; no table carries it.
    ("recognition rate is an order of magnitude", "0.327", "0.327",
     R3, "The range across all of them"),
    ("recognition rate is an order of magnitude", "0.499", "0.499",
     R3, "The range across all of them"),
    # Likewise the fitted shape and its profile interval.
    ("constant hazard the model assumes is rejected", "1.210", "1.210",
     R3, "interval [1.135, 1.285]"),
    ("constant hazard the model assumes is rejected", "1.135", "1.135",
     R3, "interval [1.135, 1.285]"),
    ("constant hazard the model assumes is rejected", "1.285", "1.285",
     R3, "interval [1.135, 1.285]"),
    ("reporting layer is not diagonal", "4.12", "4.12", R3, TABLE),
    ("reporting layer is not diagonal", "2.02", "2.02", R3, TABLE),
    ("reporting layer is not diagonal", "0.0002", "0.0002", R3, TABLE),
    ("sample rebuilds from a live endpoint", "695", "695", R3, TABLE),
    ("sample rebuilds from a live endpoint", "688", "688", R3, TABLE),

    # --- REG-006 · the re-crawl --------------------------------------------------------
    # Both arms of one crawl.  4.01× is unmoved by the repair, 2.01× → 2.10× is not.
    ("artefact of tier 0's tag list", "4.01", "4.01", R6, TABLE),
    ("artefact of tier 0's tag list", "2.01", "2.01", R6, TABLE),
    ("artefact of tier 0's tag list", "2.10", "2.10", R6, TABLE),
    ("Testing another asset first", "700", "700", R6, "Test goodwill first"),
    ("Testing another asset first", "850", "850", R6, "Test goodwill first"),

    # --- REG-007 · the keyword-family instrument ---------------------------------------
    ("disclosed trigger does not separate", "0.436", "0.436", R7, TABLE),
    ("disclosed trigger does not separate", "0.403", "0.403", R7, TABLE),
    ("disclosed trigger does not separate", "0.041", "0.0414", R7, TABLE),
    ("disclosed trigger does not separate", "0.38", "0.3805", R7, TABLE),
    ("disclosed trigger does not separate", "0.032", "0.0319", R7, TABLE),
    ("disclosed trigger does not separate", "0.24", "0.2435", R7, TABLE),

    # --- REG-008 · the entity-anchored instrument --------------------------------------
    # This row restates BOTH runs -- its whole point is the contrast -- which is the
    # configuration the witness below proves is still separable.
    ("sharper disclosure instrument", "0.103", "0.1025", R8, TABLE),
    ("sharper disclosure instrument", "0.030", "0.0295", R8, TABLE),
    ("sharper disclosure instrument", "0.014", "0.0139", R8, TABLE),
    ("sharper disclosure instrument", "0.60", "0.6013", R8, TABLE),
    ("sharper disclosure instrument", "0.068", "0.0675", R8, TABLE),
    ("sharper disclosure instrument", "281", "281", R8, TABLE),
    ("sharper disclosure instrument", "0.436", "0.436", R7, TABLE),
    ("sharper disclosure instrument", "0.403", "0.403", R7, TABLE),
]

# --------------------------------------------------------------------------------------
# The rows whose figures no result doc reports.  Each is a closed-form identity, a
# simulation residual, or an audit of the framework -- produced by a script here, not by
# a registered run against filings.  Listed so that check 1 is a real partition: an
# unclassified row fails, and moving a row between the two lists is a visible edit.
# --------------------------------------------------------------------------------------
SIMULATION_ROWS = [
    "D(φ) = (1 − φ)·D(0)",
    "(α, δ, φ) ~ (δ, α, φδ/α)",
    "φδ is the conserved quantity",
    "An open initial gap does not restore identification",
    "Unobserved physical scale",
    "Returns kill the two-point exchange",
    "Returns cannot touch the scale continuum",
    "News, not returns, restores identification",
    "The repair's strength is the asset's",
    "Neither degradation exponent is a model constant",
    "The response to news flattens as decay slows",
    "The goodwill limit needs a motionless asset",
    "The rate gap governs readability",
    "The two rates do different jobs",
    "R = (1 − φ)δ/(α − δ)",
    "The ranking inverts, not just blurs",
    "The inversion spares the lag statistic",
    # REG-004 and REG-005: simulation residuals reported to one significant figure.
    # Classified, deliberately unresolved -- see WHAT IT CANNOT DO in the module docstring.
    "The closed form survives an age-dependent hazard",
    "φ is a pure scale under age-dependence too",
    "The domain restriction is the constant hazard's",
    "The shape correction is small on the ranked ladder",
    "The lag's shape leaves a trace in the reported series",
    "The T = 0 mass is invisible in the reported series",
    "A decreasing-hazard lag is NOT mimicked",
    "Three recognition rates are three quantities",
    # framework-level checks, reported in METHOD-001 and the scripts themselves
    "Results are dimensionless",
    "and not because η is unused",
    "Recognition frequency is driven by δ",
    "The tier instrument has no baked-in ordering",
    "The registered design had power",
    "The framework's guards can fail",
    # registered, but the outcome is a verdict rather than a figure
    "The suppressing channel is not visible in entity-level filings",
]


# --------------------------------------------------------------------------------------
# surfaces
# --------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def section_7() -> str:
    text = PAPER.read_text(encoding="utf-8")
    start = text.index(SECTION_START)
    return text[start:text.index(SECTION_END, start)]


@pytest.fixture(scope="module")
def rows(section_7) -> list[str]:
    """The claim rows of §7's ledger table, whole, one string each."""
    out = []
    for line in section_7.split("\n"):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0] == "claim" or set(cells[0]) <= set("-: "):
            continue
        out.append(line)
    return out


@pytest.fixture(scope="module")
def docs() -> dict[str, str]:
    return {name: (PREREG / name).read_text(encoding="utf-8")
            for name in (R2, R3, R6, R7, R8)}


def _table_lines(text: str) -> str:
    return "\n".join(l for l in text.split("\n") if l.lstrip().startswith("|"))


def _anchored_lines(text: str, anchor: str) -> str:
    return "\n".join(l for l in text.split("\n") if anchor in l)


def _mentions(surface: str, value: str) -> bool:
    """`value` appears as a number in its own right, not as a fragment of a longer one.

    Digit-boundaries on both sides: `0.30` must not be satisfied by `0.3055`, and `281`
    must not be satisfied by `1281`.  Thousands separators in the source are tolerated.
    """
    pattern = re.escape(value).replace(",", "[,]?")
    return re.search(rf"(?<![\d.]){pattern}(?![\d])", surface) is not None


def _faithful(printed: str, source: str) -> bool:
    """`printed` is `source` rounded to `printed`'s own last decimal place.

    Half a unit in the last place, inclusive -- 0.068 is a faithful echo of 0.0675 and
    0.103 of 0.1025, while 0.113 is not.  Decimal, not float: the tolerance for 0.0675 is
    exactly 0.0005 and binary rounding would decide that boundary by accident.
    """
    p, s = Decimal(printed.replace(",", "")), Decimal(source.replace(",", ""))
    places = -p.as_tuple().exponent
    return abs(p - s) <= Decimal(1).scaleb(-places) / 2


# --------------------------------------------------------------------------------------
# 1 · every row is classified
# --------------------------------------------------------------------------------------
def test_every_ledger_row_is_classified(rows):
    """A row cannot enter §7 without someone saying where its numbers come from.

    This is `test_cell_provenance`'s undeclared-multiplier check lifted from the number
    to the row, because §7's figures are not one parseable token class.
    """
    declared = {k for k, *_ in LEDGER} | set(SIMULATION_ROWS)
    unclassified = [r for r in rows if not any(k in r for k in declared)]
    assert not unclassified, (
        "§7 has claim rows classified neither as restating a registered run (LEDGER) nor "
        "as script-produced (SIMULATION_ROWS):\n  "
        + "\n  ".join(r[:110] for r in unclassified)
        + "\nAdd each with the run that owns its figures, or say it has no such run."
    )


@pytest.mark.parametrize("key", sorted({k for k, *_ in LEDGER} | set(SIMULATION_ROWS)))
def test_each_key_identifies_exactly_one_row(key, rows):
    """A key matching zero rows is stale; a key matching two guards the wrong one."""
    hits = [r for r in rows if key in r]
    assert len(hits) == 1, (
        f"key {key!r} matches {len(hits)} rows of §7, not 1. A stale key silently stops "
        f"guarding; an ambiguous one guards a row nobody chose."
    )


def test_the_two_lists_are_disjoint():
    overlap = {k for k, *_ in LEDGER} & set(SIMULATION_ROWS)
    assert not overlap, f"rows claimed by both lists: {sorted(overlap)}"


# --------------------------------------------------------------------------------------
# 2 · every declared figure is still printed where it was declared
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize("entry", LEDGER, ids=lambda e: f"{e[0][:28]}~{e[1]}")
def test_declared_figure_is_still_printed(entry, rows):
    key, printed, _source, _owner, _surface = entry
    row = next(r for r in rows if key in r)
    assert _mentions(row, printed), (
        f"the ledger declares {printed} in the §7 row {key!r}, which no longer prints it. "
        f"If the row was legitimately restated, update the entry -- including its source."
    )


# --------------------------------------------------------------------------------------
# 3 · every declared figure resolves in the run that owns it  ← the load-bearing check
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize("entry", LEDGER, ids=lambda e: f"{e[0][:28]}~{e[1]}")
def test_declared_figure_resolves_in_its_owner(entry, docs):
    key, _printed, source, owner, surface = entry
    text = docs[owner]
    where = _table_lines(text) if surface is TABLE else _anchored_lines(text, surface)
    assert where.strip(), (
        f"the declared surface for {source} is empty in {owner}: "
        + ("no table rows at all" if surface is TABLE
           else f"no line contains the anchor {surface!r}, so the anchor has gone stale "
                f"and this assertion had stopped checking anything")
    )
    assert _mentions(where, source), (
        f"§7's row {key!r} restates {source} from {owner}, but "
        + ("no table there reports it" if surface is TABLE
           else f"the line anchored on {surface!r} does not")
        + ". Either the run was re-done and §7 still prints the old figure -- the defect "
          "this file exists for -- or the declaration names the wrong run."
    )


# --------------------------------------------------------------------------------------
# 4 · the rounding is faithful
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize("entry", LEDGER, ids=lambda e: f"{e[0][:28]}~{e[1]}")
def test_printed_figure_is_a_faithful_rounding(entry):
    key, printed, source, owner, _surface = entry
    assert _faithful(printed, source), (
        f"§7's row {key!r} prints {printed} for {owner}'s {source}. That is not a rounding "
        f"of it to {printed}'s own precision, so the echo has drifted from the run."
    )


# --------------------------------------------------------------------------------------
# the witnesses -- that none of the above is vacuous
# --------------------------------------------------------------------------------------
def test_the_two_disclosure_runs_are_still_separable(docs):
    """The §5.4 witness's analogue, on the pair most at risk of being confused.

    REG-007 and REG-008 answer the same question with different instruments, and §7 prints
    both in ONE row -- 0.436/0.403 against 0.103/0.030 -- because the contrast is the
    finding. Substituting one run's headline for the other's is therefore a live way to be
    wrong, and it is detectable only while each rate is absent from the other's tables.
    """
    seven, eight = _table_lines(docs[R7]), _table_lines(docs[R8])
    assert _mentions(seven, "0.436") and _mentions(seven, "0.403")
    assert _mentions(eight, "0.1025") and _mentions(eight, "0.0295")
    assert not _mentions(eight, "0.436"), (
        "a table in REG-008 now reports REG-007's window rate, so the guard can no longer "
        "tell the keyword-family instrument's headline from the entity-anchored one's."
    )
    assert not _mentions(seven, "0.1025"), (
        "a table in REG-007 now reports REG-008's window rate; same loss, other direction."
    )


def test_the_rounding_check_rejects_a_drifted_echo():
    """Check 4 has to be able to fail, or it is decoration.

    The live values are the interesting case: 0.068 for 0.0675 sits EXACTLY on the
    tolerance and must pass, while one place further out must not.
    """
    assert _faithful("0.068", "0.0675")      # exactly half a last place -- admitted
    assert _faithful("0.103", "0.1025")
    assert not _faithful("0.069", "0.0675")  # one place out -- refused
    assert not _faithful("0.113", "0.1025")
    assert not _faithful("0.30", "0.318")    # §5.4-style substitution of a neighbour


def test_the_digit_boundary_is_real():
    """`_mentions` must not resolve a figure inside a longer number.

    Without this, `0.030` would be satisfied by REG-008's `0.0295`-adjacent `0.0300`-ish
    neighbours and half the ledger would pass on coincidence.
    """
    assert _mentions("| 0.030 |", "0.030")
    assert not _mentions("| 0.0305 |", "0.030")
    assert not _mentions("| 1281 |", "281")
    assert _mentions("| 1,833 |", "1,833")
