"""`CONSTRAINT-INVENTORY-001` · **the inventory counts itself.**

WHY THIS FILE EXISTS
--------------------
The inventory is the estate's map of what its own registrations forbid, and for two
sessions it misreported its own column. §2 said *"nine of the fifty already had a
machine"*; the table has **twenty-four** rows naming one, eighteen of them incidental.
`-43` read that sentence, concluded the cell *"a machine could recognise this and nobody
wrote one"* was EMPTY, and wrote that conclusion into the handoff as the finding to
protect. It was a count of a column in a markdown file, stated in prose, and nobody had
recomputed it — the `-38` tell in its cheapest possible form.

`-44` also introduced the defect this file's first test catches: `wt111` announced the new
`recog` column in the header one position to the LEFT of where it inserted the cells, and
every one of the fifty rows was silently misaligned. The table still rendered. It was
caught by recomputing counts, not by reading it.

So: the inventory is a data structure, and a data structure with prose summaries needs the
summaries derived or asserted. These are asserted, because deriving them would let a wrong
table print a self-consistent wrong summary.

WHAT IT CANNOT DO
-----------------
It cannot tell you whether a `recog` grade is *right* — whether a constraint really is
machine-recognisable is a judgement, recorded in §3 and defended there. It cannot tell you
whether a named machine BINDS; that audit is per-row reading and its result is the grade
this file merely checks for legality. It checks that the table is internally coherent, that
every pointer resolves, and that the prose counts match the rows. That is the class of
defect that put a wrong sentence in two handoffs.
"""
from __future__ import annotations

import collections
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/preregistration/CONSTRAINT-INVENTORY-001.md"
TESTS = ROOT / "tests"

RECOG = ("MECH", "PROXY", "READER", "n/a")
BINDING = ("FOR", "BINDS", "PARTIAL", "ADJACENT")

ROW = re.compile(r"^\| (C\d\d) \|")
HEADER = re.compile(r"^\| # \| source \|")
COUNTS_ROW = re.compile(r"^\| ([a-z]+(?::[A-Za-z/]+)?) \| (\d+) \|$")
GRADE_PREFIX = re.compile(r"^\*\*(" + "|".join(BINDING) + r")\*\* · ")
#: A machine pointer is a python test module. `(adjacent)` prose and file names inside a
#: verdict do not count — only the `machine` column is scanned.
#: `[A-Za-z0-9_]`, not `[a-z0-9_]`: the first cut of this regex was lowercase-only, and a
#: pointer renamed to `..._OLD.py` failed to match at all — so the DANGLING POINTER check
#: never ran and the grade-agreement check fired instead, blaming the wrong thing. A
#: pointer regex narrower than the filenames it must catch is a guard that reports the
#: wrong defect, which is worse than one that reports none.
TEST_FILE = re.compile(r"test_[A-Za-z0-9_]+\.py")


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


@pytest.fixture(scope="module")
def table() -> tuple[list[str], list[list[str]]]:
    lines = DOC.read_text(encoding="utf-8").split("\n")
    header = next((_cells(ln) for ln in lines if HEADER.match(ln)), None)
    assert header is not None, f"{DOC.name}: §1's header row is gone"
    rows = [_cells(ln) for ln in lines if ROW.match(ln)]
    return header, rows


@pytest.fixture(scope="module")
def stated_counts() -> dict[str, int]:
    """§2a's counts block — the prose half of the invariant."""
    out: dict[str, int] = {}
    for ln in DOC.read_text(encoding="utf-8").split("\n"):
        m = COUNTS_ROW.match(ln)
        if m:
            out[m.group(1)] = int(m.group(2))
    return out


@pytest.fixture(scope="module")
def actual_counts(table: tuple[list[str], list[list[str]]]) -> dict[str, int]:
    header, rows = table
    ri, mi = header.index("recog"), header.index("machine")
    c: collections.Counter[str] = collections.Counter()
    c["rows"] = len(rows)
    for row in rows:
        c[f"recog:{row[ri]}"] += 1
        g = GRADE_PREFIX.match(row[mi])
        c[f"machine:{g.group(1) if g else 'none'}"] += 1
    return dict(c)


# ------------------------------------------------------------------ shape and pointers


def test_the_header_names_the_column_the_cells_are_in(
    table: tuple[list[str], list[list[str]]],
) -> None:
    """The `wt111` defect. A header can name a column one position from the data."""
    header, rows = table
    assert "recog" in header, "§1's header no longer declares a `recog` column"
    ri = header.index("recog")
    misaligned = [r[0] for r in rows if r[ri] not in RECOG]
    assert not misaligned, (
        f"COLUMN MISALIGNED — the header puts `recog` at position {ri}, and "
        f"{len(misaligned)} row(s) carry something else there, first {misaligned[:3]}. "
        "Either the header moved or the cells did. The table still renders; that is the "
        "point of this assertion."
    )


def test_every_row_has_the_header_s_width(
    table: tuple[list[str], list[list[str]]],
) -> None:
    header, rows = table
    bad = {r[0]: len(r) for r in rows if len(r) != len(header)}
    assert not bad, f"width mismatch against a {len(header)}-column header: {bad}"


def test_the_fifty_are_fifty_and_contiguous(
    table: tuple[list[str], list[list[str]]],
) -> None:
    ids = [r[0] for r in table[1]]
    assert ids == [f"C{i:02d}" for i in range(1, 51)], (
        "§1 is no longer C01…C50 in order, with no gaps and no duplicates"
    )


def test_the_binding_grade_and_the_machine_pointer_agree(
    table: tuple[list[str], list[list[str]]],
) -> None:
    """A grade with no test named, or a test named with no grade, is a false green."""
    header, rows = table
    mi = header.index("machine")
    for row in rows:
        cell, graded = row[mi], bool(GRADE_PREFIX.match(row[mi]))
        named = bool(TEST_FILE.search(cell))
        assert graded == named, (
            f"{row[0]}: machine cell is {'graded' if graded else 'ungraded'} but "
            f"{'names' if named else 'names no'} test file — {cell!r}. Every named "
            "machine carries a FOR/BINDS/PARTIAL/ADJACENT grade, and nothing else does."
        )


def test_every_named_machine_exists(
    table: tuple[list[str], list[list[str]]],
) -> None:
    header, rows = table
    mi = header.index("machine")
    missing = {
        row[0]: name
        for row in rows
        for name in TEST_FILE.findall(row[mi])
        if not (TESTS / name).exists()
    }
    assert not missing, (
        f"DANGLING POINTER — the inventory names test files that do not exist: "
        f"{missing}. A row pointing at a deleted or renamed guard reads as coverage."
    )


def test_not_live_and_n_a_are_the_same_rows(
    table: tuple[list[str], list[list[str]]],
) -> None:
    """`n/a` means *there is nothing to recognise*, which is exactly *not live*."""
    header, rows = table
    li, ri = header.index("live?"), header.index("recog")
    for row in rows:
        not_live = row[li].replace("*", "").strip().startswith("NO")
        assert not_live == (row[ri] == "n/a"), (
            f"{row[0]}: live? is {row[li]!r} and recog is {row[ri]!r}. A constraint "
            "whose antecedent never fired has nothing to recognise, and a live one does."
        )


# ------------------------------------------------------------------ prose vs the table


def test_the_counts_block_matches_the_table(
    stated_counts: dict[str, int], actual_counts: dict[str, int]
) -> None:
    assert stated_counts, "§2a's counts block is missing or unparseable"
    wrong = {
        k: (stated_counts[k], actual_counts.get(k, 0))
        for k in stated_counts
        if stated_counts[k] != actual_counts.get(k, 0)
    }
    assert not wrong, (
        f"§2a DISAGREES WITH §1 — stated vs actual: {wrong}. This is the exact defect "
        "that put *'nine of the fifty already had a machine'* into two handoffs."
    )


def test_the_counts_block_is_complete(actual_counts: dict[str, int]) -> None:
    """Every grade that occurs must be stated, or a whole class can go unreported."""
    unstated = sorted(set(actual_counts) - set(_stated()))
    assert not unstated, (
        f"§2a does not state {unstated}. A count block that omits a class lets the "
        "class grow silently, which is how eighteen became nine."
    )


def _stated() -> dict[str, int]:
    out: dict[str, int] = {}
    for ln in DOC.read_text(encoding="utf-8").split("\n"):
        m = COUNTS_ROW.match(ln)
        if m:
            out[m.group(1)] = int(m.group(2))
    return out


def test_the_partition_adds_up(actual_counts: dict[str, int]) -> None:
    """§3's four cells. 43 recognisable + 3 reader-only + 4 not-live = 50."""
    rec = sum(actual_counts.get(f"recog:{g}", 0) for g in RECOG)
    binds = actual_counts.get("machine:FOR", 0) + actual_counts.get("machine:BINDS", 0)
    recognisable = actual_counts.get("recog:MECH", 0) + actual_counts.get("recog:PROXY", 0)
    assert rec == actual_counts["rows"], "every row carries exactly one recog grade"
    assert binds <= recognisable, (
        f"{binds} rows are bound by a machine but only {recognisable} are graded "
        "machine-recognisable — a machine cannot bind a constraint no machine can see. "
        "One of the two grades is wrong."
    )


# ----------------------------------------------------------------------- non-vacuity
#
# Each fixture below breaks the table in the one way its assertion is supposed to see,
# and asserts the DETECTOR fires — not that the whole predicate fails, which any typo
# would achieve (`-43`: assert the conjunction, not a conjunct).


def test_misalignment_would_be_detected(
    table: tuple[list[str], list[list[str]]],
) -> None:
    header, rows = table
    shifted = header.index("recog") - 1
    assert not all(r[shifted] in RECOG for r in rows), (
        "VACUOUS — the column one to the left also parses as recog grades, so the "
        "alignment check cannot distinguish the two positions."
    )


def test_a_dangling_pointer_would_be_detected() -> None:
    assert not (TESTS / "test_this_guard_does_not_exist.py").exists()
    assert TEST_FILE.search("**FOR** · `test_this_guard_does_not_exist.py`"), (
        "VACUOUS — the pointer regex does not extract a test name from a machine cell."
    )


def test_a_count_drift_would_be_detected(actual_counts: dict[str, int]) -> None:
    drifted = dict(actual_counts, rows=actual_counts["rows"] + 1)
    assert drifted != actual_counts, "VACUOUS — the counts comparison is not a comparison"
    assert any(
        _stated().get(k) != v for k, v in drifted.items() if k in _stated()
    ), "VACUOUS — a moved count would still match the stated block."
