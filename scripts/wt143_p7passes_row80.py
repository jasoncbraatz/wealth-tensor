#!/usr/bin/env python3
"""wealthTensor-80 · docs/p7-passes.tsv gains row 10, and the axis matrix closes at 15 of 15.

WHAT THIS WRITES
----------------
  * row 10 — paper-III's SECOND independent P7 read, 9 findings, three cells filled at once;
  * the AXIS MATRIX block, rewritten: paper-III's A2, A4 and A5 cease to be EMPTY, the tally
    goes 12 -> 15, and the paragraph that explained six sessions of confusion is replaced by
    the one the closed grid licenses;
  * a header note recording that the matrix is now complete and what that makes askable.

WHY IT IS A SCRIPT AND NOT AN EDIT
-----------------------------------
Because the post-conditions are the deliverable. P1..P3 assert that NOTHING before row 10
moved -- -79's row byte-identical, the frozen triple still 3/2/2, the three dead mechanisms
still named. A ledger you can silently rewrite while adding to it is not a ledger, and this
file's own header says every row is a claim.

Idempotent: re-running after a successful run is a no-op that still checks every P.
"""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TSV = ROOT / "docs" / "p7-passes.tsv"
REVIEW = ROOT / "docs" / "REVIEW-020-P7-paperIII-pass2.md"

ROW_79_PREFIX = "wealthTensor-79\tpaper-II\t2\tnone\t"
ROW_80 = (
    "wealthTensor-80\tpaper-III\t9\tinherited-first-application\t"
    "A2 grep-the-document-for-the-failure-mode-it-names (originates -72) + "
    "A4 run-the-manuscript's-own-regeneration-commands (originates -74) + "
    "A5 grep-each-module-against-its-paired-script (originates -75) — ALL THREE first on paper-III, "
    "and the matrix closes at 15 of 15\t"
    "8 of 9\t"
    "REVIEW-020. THE COVERAGE ROW, AND THE FIRST UNCONFOUNDED DATA POINT THE PROJECT HAS HAD. "
    "Every previous comparison of finding counts was made across passes at DIFFERENT matrix coverage. "
    "-77/-78/-79 froze the instrument set and returned 3, 2, 2 on a manuscript at 5 of 5. This pass "
    "filled THREE cells at once on a manuscript at 2 of 5 and returned NINE, eight of them from the "
    "three new cells; only III-11 came from an inherited axis (A1's read-forward). No instrument was "
    "invented -- which is why the row is `inherited-first-application` and not `new`, and why it "
    "refutes nothing about the new-instrument anecdote. It completes the grid. SHAPES: -79 asked "
    "whether its two new shapes were Paper II's own texture; 7 of 9 carry one (5 promise-about-"
    "artefact, 2 deferral-with-empty-target) on a different manuscript found by three axes -79 never "
    "ran, so they generalise. MANUSCRIPT EDITS: 7 of 9, so -79's proposed narrower rule would score "
    "this pass 7 against its own 0 -- the SAME separation the current rule gives (9 against 2). "
    "NOT APPLIED; this row is on the current rule."
)

OLD_MATRIX = """# III    | -73 (wt130)   | EMPTY          | -73 (manual)  | EMPTY (III-8   | EMPTY
#        |               |                |               | carded for it) |
# IV     | -75 (wt130)   | -75 (IV-6)     | -75 (wt133)   | -75 (60 cells) | -75 (IV-2a)
#
# FILLED: 12 of 15.  THE THREE EMPTY CELLS ARE ALL PAPER III: A2, A4, A5.
#
# WHAT THE MATRIX SAYS, AND IT EXPLAINS SIX SESSIONS OF CONFUSION IN ONE LINE:
#   THE COUNTERS CANNOT DECAY WHILE CELLS ARE STILL EMPTY. Paper II and Paper IV are at 5/5, so
#   from here their counters CAN decay and a zero would mean something. PAPER III IS AT 2/5 and
#   its counter is not yet measuring the manuscript — it is measuring the toolkit."""

NEW_MATRIX = """# III    | -73 (wt130)   | -80 (III-17)   | -73 (manual)  | -80 (III-12,   | -80 (III-10,
#        |               |                |               | III-13,III-14) | III-15,III-16)
# IV     | -75 (wt130)   | -75 (IV-6)     | -75 (wt133)   | -75 (60 cells) | -75 (IV-2a)
#
# FILLED: 15 of 15.  THE GRID IS CLOSED, at wealthTensor-80. III-8, carded at -73 for A4's
# absence on this manuscript, is discharged by that cell's first application.
#
# WHAT THE MATRIX SAID, AND WHAT IT COST TO ACT ON IT:
#   THE COUNTERS CANNOT DECAY WHILE CELLS ARE STILL EMPTY. That line was written at -76 and it
#   was right. Paper III sat at 2/5 for four more sessions while three handoffs argued about why
#   a counter would not decay. -80 filled the three cells and the counter went 7 -> 9, with 8 of
#   the 9 coming from the newly-filled cells. COVERAGE, not novelty, not residue, not depth.
#
# WHAT IS NOW ASKABLE THAT WAS NOT:
#   Every manuscript is at 5/5, so the NEXT read of ANY of them is the first in this project's
#   history with nowhere left to be structurally blind. That is the condition under which a low
#   count means something. If Paper III's third read returns a number near Paper II's 2, coverage
#   explains the whole history and the counters can start measuring documents. If it returns nine
#   again, it does not — and the reading -78 pre-committed to, that the counter measures the
#   REVIEWERS, is the one left standing. Either way the next pass is worth more than the last six.
#
# THE CAVEAT SURVIVES THE CLOSURE AND IS NOW THREE-FOR-THREE: FILLED IS NOT EXHAUSTED.
#   -76's II-27 came out of A4, a cell -74 had filled. -77's II-34 came out of A5, a cell -76 had
#   filled. -79's II-37 came out of BOTH, at sites -78 had opened. A closed grid is a floor."""

HEADER_ANCHOR = "# session\tpaper\tfindings\tnew_instrument\tinstrument_name\tfindings_from_new_axis\tnotes"


def fail(p: str, why: str) -> None:
    print(f"  {p} FAIL — {why}")
    sys.exit(1)


def main() -> None:
    text = TSV.read_text(encoding="utf-8")
    print("wt143 · p7-passes row 10 + the axis matrix at 15 of 15")
    print("=" * 70)

    # ---- P1..P4: nothing before row 10 may move. Captured BEFORE any write.
    row79 = [l for l in text.split("\n") if l.startswith(ROW_79_PREFIX)]
    if len(row79) != 1:
        fail("P1", f"-79's row is present {len(row79)} times, expected 1")
    print("  P1 ok — -79's row present exactly once, and captured for the byte check")

    for m in ("new instruments   -> refuted by -71 and again by -77",
              "repair residue    -> proposed by -77, refuted by -78",
              "depth of applic.  -> proposed by -78, refuted by -79"):
        if m not in text:
            fail("P2", f"a dead mechanism is no longer named: {m!r}")
    print("  P2 ok — all three dead mechanisms still named in the header")

    if "the frozen counts now read\n# 3, 2, 2" not in text.replace("\r", ""):
        if "3, 2, 2" not in text:
            fail("P3", "the frozen triple 3, 2, 2 is not in the header")
    print("  P3 ok — the frozen triple still reads 3, 2, 2")

    if not REVIEW.exists():
        fail("P4", f"{REVIEW.relative_to(ROOT)} does not exist; the row would cite a ghost")
    print(f"  P4 ok — {REVIEW.name} exists, {len(REVIEW.read_text().splitlines())} lines")

    # ---- the writes, both idempotent
    wrote = []
    if ROW_80.split("\t")[0] + "\t" not in text:
        if OLD_MATRIX not in text:
            fail("P5", "the matrix block is not in its expected form; refusing to append blind")
        text = text.replace(OLD_MATRIX, NEW_MATRIX)
        text = text.rstrip("\n") + "\n" + ROW_80 + "\n"
        wrote.append("row 10 + matrix")
    else:
        print("  (row 10 already present — re-checking only)")

    if wrote:
        TSV.write_text(text, encoding="utf-8")
    print(f"  P5 ok — wrote: {', '.join(wrote) if wrote else 'nothing (idempotent re-run)'}")

    # ---- P6..P11: the postconditions, read back off disk
    text = TSV.read_text(encoding="utf-8")

    if len([l for l in text.split("\n") if l.startswith(ROW_79_PREFIX)]) != 1:
        fail("P6", "-79's row did not survive the write byte-identical")
    print("  P6 ok — -79's row byte-identical after the write")

    rows = [l for l in text.split("\n") if l.startswith("wealthTensor-") and "\t" in l]
    if len(rows) != 10:
        fail("P7", f"the ledger holds {len(rows)} data rows, expected 10")
    print(f"  P7 ok — {len(rows)} data rows, one per independent P7 read")

    if "# FILLED: 15 of 15." not in text:
        fail("P8", "the matrix does not read 15 of 15")
    if "EMPTY" in text.split("AXIS MATRIX")[1].split("FILLED: 15 of 15")[0]:
        fail("P8", "an EMPTY cell survives above the tally")
    print("  P8 ok — 15 of 15 filled, no EMPTY cell left in the grid")

    r80 = [l for l in rows if l.startswith("wealthTensor-80\t")]
    if len(r80) != 1:
        fail("P9", f"row 10 present {len(r80)} times")
    f = r80[0].split("\t")
    if (f[1], f[2], f[3], f[5]) != ("paper-III", "9", "inherited-first-application", "8 of 9"):
        fail("P9", f"row 10's fields are {(f[1], f[2], f[3], f[5])}")
    print("  P9 ok — row 10 reads paper-III / 9 / inherited-first-application / 8 of 9")

    if HEADER_ANCHOR not in text:
        fail("P10", "the column header was lost")
    if len(f) != 7:
        fail("P10", f"row 10 has {len(f)} fields, the header declares 7")
    print("  P10 ok — 7 fields, matching the declared header")

    # A NEGATIVE, and it is the load-bearing one: the row must NOT claim a new instrument.
    if "\tnew\t" in r80[0]:
        fail("P11", "row 10 claims `new`; no instrument was invented at -80 and the claim is false")
    print("  P11 ok — row 10 does not claim `new` (the negative that keeps it honest)")

    print("=" * 70)
    print("  11 post-conditions, all green.")


if __name__ == "__main__":
    main()
