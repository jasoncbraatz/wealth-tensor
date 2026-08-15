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
#: `TRIPWIRE` is a legal `machine` grade and is **NOT** coverage — it names a machine on a
#: constraint's ANTECEDENT, not on the constraint (`-45`, `CONSTRAINT-INVENTORY-001` §3.4).
#: It is kept out of `BINDING` deliberately: `test_the_partition_adds_up` counts FOR + BINDS
#: as bound, and a grade that slipped into that tuple would re-create the false-green class
#: `-44` spent a session removing. `tests/test_tripwire_class_is_registered.py` owns the
#: rest of the class's invariants.
GRADES = BINDING + ("TRIPWIRE",)

ROW = re.compile(r"^\| (C\d\d) \|")
HEADER = re.compile(r"^\| # \| source \|")
COUNTS_ROW = re.compile(r"^\| ([a-z]+(?::[A-Za-z/]+)?) \| (\d+) \|$")
GRADE_PREFIX = re.compile(r"^\*\*(" + "|".join(GRADES) + r")\*\* · ")

PRE = ROOT / "docs/preregistration"
#: The `source` cell's document, e.g. `` `REG-002` `` or `` `CONSTRUCTION-REG-009` ``.
SOURCE_DOC = re.compile(r"`([A-Z][A-Z0-9-]*-\d{3})`")
#: Its locator: a section (`§3.1`, `§4 Q1`) or a labelled item (`E2`, `R5`, `C4`, `P4`).
SOURCE_LOC = re.compile(r"§\s*([0-9]+(?:\.[0-9]+)*[a-z]?)|(?<![A-Za-z0-9])([ERCPQ])(\d+)(?![0-9])")
#: The short verbatim quotation the `constraint` cell carries, `*"…"*`.
QUOTED = re.compile(r'\*"(.+?)"\*')
#: Rows that describe their constraint rather than quoting it. **PINNED, so the set cannot
#: grow silently** — a row that stops quoting stops being checkable, which is how C33 sat
#: three sessions pointing at the wrong section of the right file.
UNQUOTED_ROWS = frozenset({"C02", "C03", "C04", "C06"})
#: Markdown that carries no meaning for a containment check. Quote glyphs go too: the
#: inventory nests a quotation inside `*"…"*`, so the registration's own `"the"` is
#: re-rendered as `'the'` (C19) and a literal match would fail on the punctuation alone.
_NOISE = str.maketrans({c: None for c in "\\*`\"'\u2018\u2019\u201c\u201d"})
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


def _flat(text: str) -> str:
    """Blockquote markers, emphasis, quote glyphs and line breaks removed; casefolded.

    Every one of these was a false MISMATCH in `-45`'s audit before it was normalised, and
    a normaliser built only from the failures it happened to see would have been the
    `-41` one-door defect: C12's clause lives inside a `>` blockquote, C19's inside nested
    quotes, C01's is sentence-initial in the source and mid-sentence in the row. What must
    NOT be normalised away is a word — `test_the_provenance_check_still_sees_a_wrong_word`
    holds that line.
    """
    stripped = "\n".join(re.sub(r"^\s*>+\s?", "", ln) for ln in text.split("\n"))
    return " ".join(stripped.translate(_NOISE).replace("\u00a0", " ").split()).casefold()


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


# --------------------------------------------------------------- provenance (`-45`)
#
# `-44`: a column that names a guard is a COVERAGE claim and nobody ever verifies it.
# **One column to the left, a `source` cell is a PROVENANCE claim, and nobody had verified
# one of those either.** C09 said `REG-002` E1 for three sessions; the clause it quotes is
# E2's. The citation survived every check a reader would think to run, because BOTH
# falsifiers constrain §4.4's headline — so *does the cited item exist* returns yes to a
# wrong pointer, and E1 is the one RESULT-REG-002 §2 records as MIS-SPECIFIED. The question
# that catches it is not whether the section exists. It is whether the section contains the
# words in the quotation column. Asked of all fifty: C09 wrong falsifier, C33 wrong section
# (§4; the clause is in §3.1), C05 a paraphrase that had dropped the antecedent.


def _resolve(doc: str) -> pathlib.Path | None:
    hits = sorted(PRE.glob(f"{doc}-*.md")) + sorted(PRE.glob(f"{doc}.md"))
    return hits[0] if hits else None


def _locator_block(text: str, token: str) -> str | None:
    """The cited section or labelled item, from its own line to the next peer.

    Two shapes, because the estate uses two: a heading (`## 5 · …`, `### 3.3 Two biases`,
    `## R3 · …`) and a bold inline label (`**P4 · The magnitude is not predicted.**`). A
    resolver that knew only headings would fall back to whole-file on `REG-007` P4 and
    quietly weaken to the check that cannot see C09.
    """
    esc = re.escape(token)
    m = re.search(rf"^(#{{2,4}}) \*{{0,2}}{esc}\*{{0,2}}(?=[ ·—:])", text, re.M)
    if m:
        depth = len(m.group(1))
        rest = text[m.end():]
        nxt = re.search(rf"^#{{1,{depth}}} ", rest, re.M)
        return text[m.start(): m.end() + (nxt.start() if nxt else len(rest))]
    m = re.search(rf"^\*\*{esc}(?=[ ·—:])", text, re.M)
    if m:
        rest = text[m.end():]
        nxt = re.search(r"^(\*\*[A-Z]\d|#{1,4} )", rest, re.M)
        return text[m.start(): m.end() + (nxt.start() if nxt else len(rest))]
    return None


def _cited_blocks(source_cell: str) -> tuple[list[str], list[str]]:
    """Every (document, locator) the `source` cell names, resolved to text. And the misses.

    A cell may cite more than one registration — `` `REG-004` §6 / `REG-005` §7 `` — so it
    is split on `/` and each side resolved against its own document.
    """
    blocks: list[str] = []
    misses: list[str] = []
    for part in source_cell.split("/"):
        docs = SOURCE_DOC.findall(part) or SOURCE_DOC.findall(source_cell)
        for doc in docs:
            path = _resolve(doc)
            if path is None:
                misses.append(f"{doc}: no such document in docs/preregistration/")
                continue
            text = path.read_text(encoding="utf-8")
            tokens = [g[0] or f"{g[1]}{g[2]}" for g in SOURCE_LOC.findall(part)]
            if not tokens:
                misses.append(f"{doc}: the source cell names no section or item")
                continue
            # Locators NEST, left to right: `§4 Q1` means Q1 *inside* §4, and each token is
            # resolved within the block the one before it produced. A union would have been
            # forgiving in exactly the way that hides a defect — `Q1` is unique in REG-006,
            # so a union resolves `§4 Q1` correctly even though Q1 lives in §3, which is
            # where C26, C27 and C28 had been pointing since the file was built.
            scope, ok = text, True
            for token in tokens:
                found = _locator_block(scope, token)
                if found is None:
                    where = path.name if scope is text else f"the block above in {path.name}"
                    misses.append(f"{doc}: no section or item `{token}` in {where}")
                    ok = False
                    break
                scope = found
            if ok:
                blocks.append(scope)
    return blocks, misses


def test_every_quoted_constraint_appears_in_its_cited_source(
    table: tuple[list[str], list[list[str]]],
) -> None:
    """**THE SOURCE COLUMN IS A PROVENANCE CLAIM. THIS IS THE ROW-BY-ROW AUDIT OF IT.**

    For each row: resolve the `source` cell to the exact section or labelled item it cites,
    and require the row's own quotation to be in it. Nothing here judges the constraint,
    the grade, or the verdict — only that the row is quoting the thing it says it is
    quoting. A wrong citation is not cosmetic: it is the address every future session,
    every guard docstring and every red message is sent to.
    """
    header, rows = table
    si, ci = header.index("source"), header.index("the constraint")
    unsourced: dict[str, str] = {}
    for row in rows:
        cid, source, constraint = row[0], row[si], row[ci]
        quotes = QUOTED.findall(constraint)
        if not quotes:
            continue
        blocks, misses = _cited_blocks(source)
        if not blocks:
            unsourced[cid] = f"{source} → unresolvable ({'; '.join(misses)})"
            continue
        hay = _flat(" ".join(blocks))
        # EVERY quoted fragment, not any. `any` was the first cut and it is a false green:
        # a row that quotes two clauses passes on the easier one, so C05's paraphrase
        # survived because the annotation beside it quoted the antecedent correctly. A
        # containment check over a disjunction certifies the weakest conjunct — `-43`.
        absent = [q for q in quotes if _flat(q) not in hay]
        if absent:
            unsourced[cid] = (
                f"{source} does not contain {absent[0][:70]!r}"
                + (f" (+{len(absent) - 1} more)" if len(absent) > 1 else "")
                + (f" [{'; '.join(misses)}]" if misses else "")
            )
    assert not unsourced, (
        "WRONG PROVENANCE — a row quotes a constraint the section it cites does not "
        f"contain:\n  " + "\n  ".join(f"{k}: {v}" for k, v in sorted(unsourced.items()))
        + "\n\nThree readings, and only one of them is a typo:\n"
        "  (a) the row cites the wrong section or falsifier — repair the `source` cell,\n"
        "      and CHECK WHAT ELSE INHERITED IT: C09's E1 reached two handoffs, §2, §3.3\n"
        "      and §3.4 before anyone recomputed it;\n"
        "  (b) the quotation is a paraphrase — make it verbatim. C05's short form had\n"
        "      silently dropped `in that case`, which is the constraint's ANTECEDENT;\n"
        "  (c) the registration was edited — then the row's verdict was reached against\n"
        "      text that no longer exists, and the row needs re-grading, not re-quoting."
    )


def test_the_unquoted_rows_are_the_pinned_four(
    table: tuple[list[str], list[list[str]]],
) -> None:
    """A row that stops quoting stops being audited, and nothing else would notice.

    The provenance check above can only see rows that quote. Four rows describe their
    constraint instead — C02, C03, C04, C06, all of `PRE-002` §3 and `PRE-002` §2 — and
    that set is pinned rather than tolerated, so the cheapest way to silence a provenance
    failure (delete the quotation marks) is itself a red.
    """
    header, rows = table
    ci = header.index("the constraint")
    unquoted = {r[0] for r in rows if not QUOTED.search(r[ci])}
    assert unquoted == UNQUOTED_ROWS, (
        f"the set of rows carrying no verbatim quotation moved from "
        f"{sorted(UNQUOTED_ROWS)} to {sorted(unquoted)}. Added rows are unauditable by "
        "`test_every_quoted_constraint_appears_in_its_cited_source`; quote them, or pin "
        "them here in the same commit and say in the message why the constraint cannot "
        "be quoted."
    )


def test_the_provenance_check_still_sees_a_wrong_word() -> None:
    """NON-VACUITY. `_flat` normalises punctuation, and a normaliser that went one step
    further — stripping stopwords, stemming, comparing loosely — would pass everything.

    So: feed it the real failure. C09's quotation against E1's actual text must NOT match,
    and against E2's must. `-43`: feed the registration its own forbidden claim before you
    trust the green.
    """
    reg_002 = _resolve("REG-002")
    assert reg_002 is not None, "REG-002 is gone from docs/preregistration/"
    text = reg_002.read_text(encoding="utf-8")
    quote = _flat("§4.4 may not report it as the section's headline")

    e1, e2 = _locator_block(text, "E1"), _locator_block(text, "E2")
    assert e1 and e2, "REG-002's E1/E2 blocks no longer resolve — the resolver is broken"
    assert quote in _flat(e2), (
        "C09's quotation is not in REG-002 E2. Either E2 was reworded, in which case C09 "
        "and tests/test_tripwire_c09_sec44_headline.py both need re-reading, or the "
        "resolver has stopped finding E2."
    )
    assert quote not in _flat(e1), (
        "VACUOUS — the provenance check cannot tell E1 from E2, which is the exact defect "
        "it was written to catch. It would have passed the wrong citation it now forbids."
    )
    assert _flat("the next move is not a third instrument") not in _flat(
        "The next move in that case is not a third instrument"
    ), "VACUOUS — the check tolerates a paraphrase that drops words from the middle."


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
