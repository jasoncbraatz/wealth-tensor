"""C36 · `REG-009` §4 — a refusal is *"stated in the same sentence as the number that
caused it."*

**THIS FILE IS A TRIPWIRE, NOT A GUARD**, and it is the one whose consequent belongs to
**Jason**, not to a Claude. `CONSTRAINT-INVENTORY-001` §3.4 defines the class; §3.3 is where
C36's gap is stated, and it is worth quoting whole because it is the reason this file exists
rather than a test of the constraint:

> the registration says nothing about the row sharing a table with thirty rows that risked
> nothing. **A machine can check the sentence; only a reader can see the table.**

THE TWO HALVES, AND WHY ONLY ONE OF THEM IS HERE
-------------------------------------------------
The **registration's** requirement is sentence-local: `RESULT-REG-009` §4 states the refusal
of the δ design in the same sentence as the number that caused it, and complies. That half
is checkable and is not what is at issue.

The **reader's** worry is presentational and is not in the registration at all: §7's
survivals ledger is long, and most of its rows are algebra that could not have come out any
other way. The rows that risked something — the one that refused in every one of 400 draws
and cost the paper its neatest sentence, the one that failed as registered — sit in the same
undifferentiated table as `held to 10⁻¹⁵`. Whether that dilutes them is a judgement about
what a referee's eye does with a long table. Per `docs/CO-AUTHOR-CHARTER.md` that is one of
the few things reserved to Jason: it is not a fact about the repo, and no Claude with darwin
and the repos can settle it.

So this file watches the **shape** of the ledger and nothing else. It does not grade the
presentation, it does not card anything, and it must not be "improved" into doing either.

WHY SHAPE, AND WHY IT IS NOT ASKED TODAY
-----------------------------------------
The judgement was made once, on a ledger of a particular size and a particular set of
columns, and it was made by leaving the ledger as it is. Two mechanical events put it back in
play: **a column appears** — most obviously one separating algebra rows from rows that risked
something, which is the repair the worry implies — or **the row count moves**, because the
dilution argument is entirely about how many rows the load-bearing ones are buried among.
Neither is a violation of `REG-009` §4. Both mean *ask Jason, once*.

**Once.** A tripwire that re-asks on every subsequent commit is a tripwire that trains its
owner to ignore it — the same death as one whose red message cries violation. The re-pin path
in the message below is how the answer gets recorded, and the commit message is where the
answer lives.

WHAT THIS CANNOT DO
-------------------
It cannot see a row being *reworded* into or out of load-bearing status, cannot see rows
reordered, and cannot see the ledger's length in a reader's sense (a row here is one to
fifteen lines of prose). `CONSTRAINT-INVENTORY-001` C36 stays `recog: READER`,
`machine: TRIPWIRE`, and **TRIPWIRE IS NOT COVERAGE** — a reader-only constraint has no
machine that binds it, which is the entire point of §3.4.
"""
from __future__ import annotations

import pathlib
import re

import pytest

pytestmark = pytest.mark.tripwire

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_009 = ROOT / "docs/preregistration/REG-009-p3-lifetime-sourced-delta.md"

#: `REG-009` §4's clause. The warrant — and note it is the SENTENCE-local half, which this
#: file does not check and does not claim to.
CONSTRAINT = "with the refusal stated in the same sentence as the number that caused it"

#: §7's ledger as the presentation judgement was left standing on it, at `a1fef70`.
LEDGER_COLUMNS = ("claim", "test", "what would have killed it", "outcome")
LEDGER_ROWS = 47

_HEADING_7 = re.compile(r"^## 7 · .*$", re.M)
_HEADING_8 = re.compile(r"^## 8 · ", re.M)


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def section_7(text: str) -> str:
    start = _HEADING_7.search(text)
    assert start, "§7's heading is gone from the manuscript"
    rest = text[start.start():]
    end = _HEADING_8.search(rest)
    assert end, "§8's heading is gone from the manuscript"
    return rest[: end.start()]


def ledger(text: str) -> tuple[list[str], list[list[str]]]:
    """§7's survivals table: its header cells and its body rows.

    The separator row (`|---|`) is dropped, not counted — a count that included it would
    be off by one forever and nobody would notice, which is this estate's most reliably
    repeated defect.
    """
    lines = [ln for ln in section_7(text).splitlines() if ln.startswith("|")]
    assert len(lines) >= 3, "§7 no longer contains a table"
    header, sep, *body = lines
    assert set(sep.replace("|", "").replace(" ", "")) <= set("-:"), (
        f"§7's second table line is not a separator: {sep!r}"
    )
    return _cells(header), [_cells(ln) for ln in body]


def test_the_registration_still_says_this():
    flat = " ".join(REG_009.read_text(encoding="utf-8").split())
    assert CONSTRAINT in flat, (
        "REG-009 §4's refusal clause is gone or restated. THIS TRIPWIRE HAS LOST ITS "
        "WARRANT — read the registration before trusting anything else in this file."
    )


def test_the_ledger_columns_have_not_changed():
    header, _ = ledger(PAPER.read_text(encoding="utf-8"))
    assert tuple(header) == LEDGER_COLUMNS, (
        "TRIPWIRE · §7's LEDGER GREW OR LOST A COLUMN. **THIS IS NOT A FAILURE AND NOTHING "
        "IS WRONG.**\n"
        f"  pinned  {LEDGER_COLUMNS}\n  current {tuple(header)}\n\n"
        "ASK JASON, ONCE. CONSTRAINT-INVENTORY-001 §3.3: the reader's worry behind C36 is "
        "that §7's ledger dilutes the two rows that risked something by tabling them with "
        "rows that could not have come out otherwise. A new column — especially one "
        "separating algebra from risk — is that judgement being re-made, and the charter "
        "reserves it to him: it is a judgement about a referee's eye, not a fact about the "
        "repo.\n"
        "Then re-pin LEDGER_COLUMNS in the SAME commit and put HIS ANSWER in the commit "
        "message. Ask once; a tripwire that re-asks every commit gets ignored."
    )


def test_the_ledger_row_count_has_not_moved():
    _, body = ledger(PAPER.read_text(encoding="utf-8"))
    assert len(body) == LEDGER_ROWS, (
        f"TRIPWIRE · §7's LEDGER MOVED FROM {LEDGER_ROWS} ROWS TO {len(body)}. **THIS IS "
        "NOT A FAILURE.**\n\n"
        "ASK JASON, ONCE. The dilution worry behind C36 is entirely about how many rows "
        "the load-bearing ones are buried among — the row that refused in 400 of 400 draws "
        "and the row that failed as registered. Adding rows makes the worry sharper; "
        "removing them may have removed one of the two.\n"
        "Then re-pin LEDGER_ROWS in the SAME commit, with his answer in the message.\n"
        "REG-009 §4 itself is NOT violated by any of this: its requirement is that the "
        "refusal share a sentence with its number, and RESULT-REG-009 §4 does that."
    )


# ----------------------------------------------------------------------- non-vacuity


def test_the_extractor_finds_the_survivals_ledger_and_not_some_other_table():
    header, body = ledger(PAPER.read_text(encoding="utf-8"))
    assert header[0] == "claim" and header[-1] == "outcome"
    joined = " ".join(" ".join(r) for r in body)
    assert "refused" not in header, "the separating column already exists — ask Jason"
    assert "failed as registered" in joined, (
        "the ledger no longer contains the row that FAILED as registered — one of the two "
        "rows the C36 worry is about. ASK JASON."
    )
    assert "lag ordering held in **100%**" in joined, (
        "the ledger no longer contains the 400-of-400 row — the other row the C36 worry is "
        "about. ASK JASON."
    )


def test_a_new_column_would_be_detected():
    text = PAPER.read_text(encoding="utf-8")
    header, _ = ledger(text)
    assert tuple(header + ["risked something?"]) != LEDGER_COLUMNS, (
        "VACUOUS — an added column compares equal to the pinned column tuple."
    )


def test_a_row_count_move_would_be_detected():
    _, body = ledger(PAPER.read_text(encoding="utf-8"))
    assert len(body) + 1 != LEDGER_ROWS and len(body) - 1 != LEDGER_ROWS, (
        "VACUOUS — the pinned row count is not the count this extractor produces."
    )


def test_the_separator_row_is_not_counted_as_a_claim():
    _, body = ledger(PAPER.read_text(encoding="utf-8"))
    assert not any(set("".join(r).replace(" ", "")) <= set("-:") for r in body), (
        "the separator row is being counted as a ledger row, so LEDGER_ROWS is off by one"
    )
