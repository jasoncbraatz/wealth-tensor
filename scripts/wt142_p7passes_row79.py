#!/usr/bin/env python3
"""wt142 · wealthTensor-79 · docs/p7-passes.tsv gains row 9, plus the header note that the
DEPTH mechanism is now refuted too.

GUARD HONESTY (WT-118): every OLD string is asserted present EXACTLY ONCE before any
substitution runs, and the guards run BEFORE the backup, so a failed guard writes nothing.

WHY THE HEADER MOVES AND NOT ONLY THE TABLE. The file's own commentary told the next reader
that -78 was "the only evidence so far that the axes can be exhausted at all". -79 is the
test of exactly that sentence and it came back 2 of 2 from sites -78 had opened. Leaving the
commentary would have left a refuted claim sitting above the row that refutes it.
"""
from __future__ import annotations

import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TSV = ROOT / "docs" / "p7-passes.tsv"
TAG = ".bak-wt142"

OLD_NOTE = """# READ THE new_instrument COLUMN AND THE findings COLUMN TOGETHER, AND DO NOT STOP AT ROW 7.
# Three rows now carry `none` or its equivalent: -71 (4 findings), -77 (3), -78 (2). The anecdote
# that a new instrument is what produces findings is refuted three times. But -78 is the first
# row where the count actually FELL under a frozen set, which is the only evidence so far that
# the axes can be exhausted at all."""

NEW_NOTE = """# READ THE new_instrument COLUMN AND THE findings COLUMN TOGETHER, AND DO NOT STOP AT ROW 7.
# FOUR rows now carry `none` or its equivalent: -71 (4 findings), -77 (3), -78 (2), -79 (2). The
# anecdote that a new instrument is what produces findings is refuted four times.
#
# THREE MECHANISMS HAVE BEEN PROPOSED FOR THE NON-DECAYING COUNTER AND ALL THREE ARE DEAD.
#   new instruments   -> refuted by -71 and again by -77 (frozen set, three findings).
#   repair residue    -> proposed by -77, refuted by -78 (0 of 2 blame to -77).
#   depth of applic.  -> proposed by -78, refuted by -79 (2 of 2 from sites -78 had OPENED;
#                        one of them is item 7 on -78's OWN not-checked list). REVIEW-019 §5.
# -78 was briefly the only evidence that the axes can be exhausted; the frozen counts now read
# 3, 2, 2 and the decay stopped. The reading -78 pre-committed to -- that the counter measures
# the REVIEWERS rather than the paper -- is the one left standing, and it is Jason's to rule on.
# -79 proposes a narrower fix than changing the bar: count only findings that require a
# MANUSCRIPT edit. Under that rule -79 scores 0 and -78 scores 1. NOT APPLIED -- the counts
# below are unchanged and remain on the current rule."""

ROW = ("wealthTensor-79\tpaper-II\t2\tnone\t"
       "— (all five axes inherited; Paper II was 5 of 5 before this pass, A6 left parked as ordered)"
       "\t0 of 2\t"
       "REVIEW-019. THE THIRD FROZEN ROW, AND THE FALSIFIER -78 HANDED IT. -78 argued the counter "
       "measures how much of each axis has been SPENT and predicted that a ninth read at the same "
       "depth would find materially fewer than two. IT FOUND TWO, AND BOTH FROM SITES -78 HAD "
       "ALREADY OPENED: II-37 at the two commands A5 enumerated and A4 ran, II-38 at item 7 of "
       "REVIEW-018 §4's own not-checked list. RESIDUE: 0 of 2 (II-37 -> 58f7f5bb/-74 and "
       "6b0655b2/-77; II-38 -> f1ceac74, 2026-08-10). Depth of application is refuted. FIRST PASS "
       "IN THE PROJECT WITH ZERO MANUSCRIPT EDITS: both repairs made an existing sentence true "
       "instead of changing it. A third defect (II-39, a prefix collision in wt130's selector) was "
       "found and repaired but is DELIBERATELY NOT COUNTED -- it is in the reviewing apparatus, "
       "which Paper II names nowhere.\n")


def main() -> int:
    s = TSV.read_text(encoding="utf-8")
    assert s.count(OLD_NOTE) == 1, "header note anchor: %d occurrences" % s.count(OLD_NOTE)
    assert s.count("wealthTensor-79\t") == 0, "row 9 already present"
    assert s.endswith("\n"), "file does not end in a newline"

    before_rows = [l for l in s.splitlines() if l.startswith("wealthTensor-")]
    assert len(before_rows) == 8, "expected 8 rows, found %d" % len(before_rows)

    shutil.copy2(TSV, TSV.with_name(TSV.name + TAG))
    TSV.write_text(s.replace(OLD_NOTE, NEW_NOTE) + ROW, encoding="utf-8")

    s2 = TSV.read_text(encoding="utf-8")
    rows = [l for l in s2.splitlines() if l.startswith("wealthTensor-")]

    # ---- POST-CONDITIONS ---------------------------------------------------
    # 1. nine rows, each with the same seven fields
    assert len(rows) == 9, "P1 row count %d" % len(rows)
    for r in rows:
        assert len(r.split("\t")) == 7, "P2 field count in %s" % r.split("\t")[0]
    # 2. new_instrument is still FOUR-VALUED across all nine (the -78 post-condition, extended)
    vals = {r.split("\t")[3] for r in rows}
    assert vals == {"none", "new", "new+inherited-first-application",
                    "inherited-first-application"}, "P3 new_instrument values drifted: %s" % vals
    # 3. the FROZEN TRIPLE reads 3, 2, 2 in order -- the decay-then-stall this pass measured
    frozen = [int(r.split("\t")[2]) for r in rows
              if r.split("\t")[0] in ("wealthTensor-77", "wealthTensor-78", "wealthTensor-79")]
    assert frozen == [3, 2, 2], "P4 frozen counts are %s, not [3, 2, 2]" % frozen
    # 4. all four `none` rows are present and none of them is a zero -- the fact the
    #    header commentary now turns on
    none_rows = [(r.split("\t")[0], int(r.split("\t")[2])) for r in rows if r.split("\t")[3] == "none"]
    assert len(none_rows) == 4, "P5 expected four `none` rows, got %s" % none_rows
    assert all(n > 0 for _, n in none_rows), "P6 a `none` row went to zero -- rewrite §5"
    # 5. the refuted-mechanism note landed and names all three
    for m in ("new instruments", "repair residue", "depth of applic."):
        assert m in s2, "P7 mechanism %r missing from the header" % m
    # 6. -78's row is byte-identical: this pass reports on it, it does not rewrite it
    assert [r for r in rows if r.startswith("wealthTensor-78")] == \
           [r for r in before_rows if r.startswith("wealthTensor-78")], "P8 -78's row was edited"

    print("wt142: p7-passes.tsv row 9 added, header note updated, 8 post-conditions PASS")
    print("       9 rows; frozen triple 3, 2, 2; four `none` rows, none of them zero.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
