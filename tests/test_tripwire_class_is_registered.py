"""**THE TRIPWIRE CLASS EXISTS, AND IT CANNOT DISSOLVE ONE LAYER AT A TIME.**

`CONSTRAINT-INVENTORY-001` §3.4 (`-44`) named the class and `wealthTensor-45` built the
first three members. §3.4's own warning is the reason this file exists:

> a suite that cannot tell a tripwire from a guard will eventually have one deleted as a
> false alarm.

A tripwire fires on the machine-checkable **antecedent of a re-read** and says *a human must
read this*. A guard fires on a **violation** and says *this is wrong*. They are the same
mechanism and opposite speech acts, and the difference is invisible in a `1 failed` line.

THE CLASS IS MARKED IN THREE PLACES, AND THAT IS DELIBERATE
------------------------------------------------------------
1. **The file name** — `tests/test_tripwire_*.py`. Survives a grep, sorts together, and is
   the only marker visible in a bare pytest failure line.
2. **The pytest marker** — `pytestmark = pytest.mark.tripwire`, registered in `conftest.py`.
   `pytest -m tripwire` lists the class; `-m "not tripwire"` excludes it. A marker that is
   not registered raises `PytestUnknownMarkWarning` and decays into a typo, so registration
   is asserted here rather than assumed.
3. **The inventory** — a `TRIPWIRE` grade in `CONSTRAINT-INVENTORY-001` §1's `machine`
   column, counted in §2a.

Any one of the three alone rots quietly: a file renamed, a marker dropped in a tidy-up, a
row re-graded. This file requires all three to agree, in both directions.

**TRIPWIRE IS NOT COVERAGE, AND THAT IS ASSERTED HERE.** `HANDOFF` §2's ruling — *only FOR
and BINDS mean the constraint is guarded* — is exactly what a new grade could quietly
break: a row moving `none → TRIPWIRE` looks like progress in a diff and is not. A tripwire
leaves its constraint in cell (b), or reader-only, where it was. What it changes is that
somebody is now guaranteed to be asked.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"
DOC = ROOT / "docs/preregistration/CONSTRAINT-INVENTORY-001.md"
CONFTEST = ROOT / "conftest.py"

ROW = re.compile(r"^\| (C\d\d) \|")
HEADER = re.compile(r"^\| # \| source \|")
TEST_FILE = re.compile(r"test_[A-Za-z0-9_]+\.py")
GRADE = re.compile(r"^\*\*([A-Z]+)\*\* · ")
#: The grades that mean the constraint is guarded. `HANDOFF` §2, `-44`.
COVERAGE = ("FOR", "BINDS")


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _rows() -> tuple[list[str], list[list[str]]]:
    lines = DOC.read_text(encoding="utf-8").split("\n")
    header = next(_cells(ln) for ln in lines if HEADER.match(ln))
    return header, [_cells(ln) for ln in lines if ROW.match(ln)]


def _tripwire_files() -> list[pathlib.Path]:
    return sorted(TESTS.glob("test_tripwire_*.py"))


def _members() -> list[pathlib.Path]:
    """Tripwire files excluding this one, which is the class's registrar, not a member."""
    return [p for p in _tripwire_files() if p.name != pathlib.Path(__file__).name]


def test_the_class_is_not_empty():
    assert _members(), (
        "no `tests/test_tripwire_*.py` members remain. If the class was genuinely retired, "
        "retire this file and CONSTRAINT-INVENTORY-001 §3.4's TRIPWIRE grade in the same "
        "commit — do not leave a registrar guarding nothing."
    )


def test_the_marker_is_registered_in_conftest():
    """An unregistered mark warns and then rots into a typo, silently ungrouping the class."""
    src = CONFTEST.read_text(encoding="utf-8")
    assert "addinivalue_line" in src and '"markers"' in src and "tripwire:" in src, (
        "conftest.py no longer registers the `tripwire` marker. `pytest -m tripwire` stops "
        "selecting the class and every member raises PytestUnknownMarkWarning."
    )


def test_every_member_file_declares_the_marker(request: pytest.FixtureRequest):
    """Source-level, so a member that fails to COLLECT is still caught."""
    undeclared = [
        p.name
        for p in _members()
        if "pytestmark = pytest.mark.tripwire" not in p.read_text(encoding="utf-8")
    ]
    assert not undeclared, (
        f"named `test_tripwire_*` but not marked: {undeclared}. The file name and the "
        "marker must agree — otherwise `-m \"not tripwire\"` silently runs a tripwire and "
        "its red reads as a violation."
    )


def test_every_member_says_out_loud_that_it_is_not_a_guard():
    """The docstring is the only part of a tripwire the next session reads before acting."""
    missing = [
        p.name
        for p in _members()
        if "TRIPWIRE, NOT A GUARD" not in p.read_text(encoding="utf-8")
    ]
    assert not missing, (
        f"{missing} do not declare themselves tripwires in their docstring. §3.4: a "
        "tripwire whose red message names a violation teaches the next session to "
        "suppress it — and the docstring is where the reader finds out which it is."
    )


def test_every_member_red_message_names_a_re_read_not_a_failure():
    """Assert the SHAPE of the speech act, at the scene, in every member."""
    for p in _members():
        src = p.read_text(encoding="utf-8")
        assert "TRIPWIRE ·" in src, f"{p.name}: no red message is tagged `TRIPWIRE ·`"
        assert "NOT A FAILURE" in src or "NOTHING IS WRONG" in src, (
            f"{p.name}: no red message tells the reader this is not a failure."
        )
        assert "GO AND READ" in src or "ASK JASON" in src, (
            f"{p.name}: no red message names the re-read or the person to ask. A tripwire "
            "that fires without saying what to read is noise, and noise gets suppressed."
        )


# ------------------------------------------------------- the inventory, in both directions


def test_the_inventory_and_the_files_name_each_other():
    header, rows = _rows()
    mi = header.index("machine")
    named: dict[str, str] = {}
    for row in rows:
        if (g := GRADE.match(row[mi])) and g.group(1) == "TRIPWIRE":
            for name in TEST_FILE.findall(row[mi]):
                named[name] = row[0]

    on_disk = {p.name for p in _members()}
    assert set(named) == on_disk, (
        f"the inventory's TRIPWIRE rows name {sorted(named)} and the tests directory holds "
        f"{sorted(on_disk)}. Every tripwire is registered against the constraint it "
        "watches, and every TRIPWIRE row points at a file — a tripwire nobody can trace to "
        "a constraint is the false-alarm deletion §3.4 warns about, arriving on schedule."
    )


def test_a_tripwire_is_never_filed_as_coverage():
    """`HANDOFF` §2: only FOR and BINDS mean guarded. A new grade must not smuggle a third."""
    header, rows = _rows()
    mi = header.index("machine")
    smuggled = [
        row[0]
        for row in rows
        if (g := GRADE.match(row[mi]))
        and g.group(1) in COVERAGE
        and any(n.startswith("test_tripwire_") for n in TEST_FILE.findall(row[mi]))
    ]
    assert not smuggled, (
        f"{smuggled} are graded FOR/BINDS against a tripwire. A tripwire watches an "
        "ANTECEDENT; it cannot bind the constraint, which is why the constraint has one. "
        "Re-grade the row, or the estate has just re-created the false-green class `-44` "
        "spent a session removing."
    )


def test_the_marker_actually_selects_the_class(pytestconfig: pytest.Config):
    """The registration is real at runtime, not just present in conftest's source."""
    markers = pytestconfig.getini("markers")
    assert any(m.startswith("tripwire:") for m in markers), (
        f"`tripwire` is not among the registered markers at runtime: {list(markers)[:5]}…"
    )
