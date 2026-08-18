#!/usr/bin/env python3
"""wealthTensor-78 — docs/p7-passes.tsv gains its EIGHTH row: the SECOND frozen pass,
and the first with a RESIDUE column.

-77's row was the control for the "each pass brought a new instrument" anecdote.
-78's row is the control for -77's OWN replacement mechanism ("a repair pass creates
surface"). It returned 0 of 2 residue, so neither standing explanation survives, and
REVIEW-018 §5 argues the third: depth of application.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TSV = ROOT / "docs/p7-passes.tsv"

ROW = "\t".join([
    "wealthTensor-78",
    "paper-II",
    "2",
    "none",
    "— (all five axes inherited; Paper II was 5 of 5 before this pass, A6 left parked as ordered)",
    "0 of 2",
    "REVIEW-018. THE SECOND FROZEN ROW, AND THE CONTROL FOR -77's OWN MECHANISM. "
    "-77 proposed that a repair pass creates the next pass's findings and made -78 the experiment "
    "by handing it four manuscript edits and one test edit. RESIDUE: 0 of 2. II-35 blames to "
    "2b3e24b5 (2026-08-17), II-36 to 3b11f236 (2026-08-05) — the very commit §7 pins, present for "
    "ALL EIGHT reads. Neither new instruments nor repair residue explains the counter; "
    "REVIEW-018 §5 argues DEPTH OF APPLICATION, which unlike residue leaves a zero REACHABLE. "
    "First DECAYING count in the project's history (3 -> 2).",
]) + "\n"

CAVEAT = """#
# THE RESIDUE COLUMN (born wealthTensor-78, and it is not a TSV column — it lives in the review
# documents' front matter as `residue_of_previous_pass`, because only two rows can carry it).
# -77 asked whether a pass's findings are residue of its predecessor's repairs. -77: 2 of 3 YES.
# -78: 0 of 2. The mechanism does not generalise on two data points, and -78's second finding
# had been in the tree since 2026-08-05 — through every P7 read this paper has had.
#
# READ THE new_instrument COLUMN AND THE findings COLUMN TOGETHER, AND DO NOT STOP AT ROW 7.
# Three rows now carry `none` or its equivalent: -71 (4 findings), -77 (3), -78 (2). The anecdote
# that a new instrument is what produces findings is refuted three times. But -78 is the first
# row where the count actually FELL under a frozen set, which is the only evidence so far that
# the axes can be exhausted at all.
"""


def main() -> int:
    t = TSV.read_text(encoding="utf-8")
    assert "wealthTensor-78" not in t, "row already present"
    assert t.endswith("\n"), "ledger does not end in a newline"
    before_rows = [l for l in t.splitlines() if l and not l.startswith("#")]
    assert len(before_rows) == 7, "expected 7 data rows, found %d" % len(before_rows)

    # the caveat block goes with the header comments, the row at the end
    head, sep, body = t.partition("\n# session\t")
    assert sep, "header line not found"
    TSV.write_text(head + "\n" + CAVEAT + "# session\t" + body + ROW, encoding="utf-8")

    t2 = TSV.read_text(encoding="utf-8")
    rows = [l for l in t2.splitlines() if l and not l.startswith("#")]

    # ---- POST-CONDITIONS ----
    assert len(rows) == 8, "P1 expected 8 data rows, got %d" % len(rows)
    assert rows[-1].startswith("wealthTensor-78\t"), "P2 new row is not last"
    ncols = {len(r.split("\t")) for r in rows}
    assert ncols == {7}, "P3 ragged ledger: column counts %s" % ncols
    # new_instrument stays FOUR-VALUED across all eight rows (-77's post-condition, extended)
    vals = {r.split("\t")[3] for r in rows}
    assert vals == {"none", "new", "new+inherited-first-application",
                    "inherited-first-application"}, "P4 new_instrument vocabulary drifted: %s" % vals
    # exactly three rows now claim `none`
    assert sum(1 for r in rows if r.split("\t")[3] == "none") == 3, "P5 expected 3 `none` rows"
    # the two frozen rows are consecutive and the count DECAYED
    assert [r.split("\t")[2] for r in rows[-2:]] == ["3", "2"], "P6 frozen pair counts moved"
    # every row still names a REVIEW document in notes
    assert all("REVIEW-0" in r.split("\t")[6] for r in rows), "P7 a row lost its falsifier"
    assert "residue_of_previous_pass" in t2, "P8 caveat block missing"

    print("wt140: p7-passes.tsv row 8 written, 8 post-conditions PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
