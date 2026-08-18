#!/usr/bin/env python3
"""wt138 -- add wealthTensor-77's row to docs/p7-passes.tsv and refresh the axis matrix.

THE ROW THIS FILE WAS BUILT TO HOLD. -76 created the ledger to measure the claim that every
non-decaying counter was explained by a new instrument. -77 is the CONTROL: `none`, and three
findings anyway. That makes TWO rows out of seven that cut against the anecdote (-71 and -77),
and -77's is the stronger of the two because -71 predates the matrix and -77 was assigned a
frozen set on purpose.

The matrix gains nothing -- Paper II was already 5 of 5 and no axis was invented -- but its
CAVEAT gains a second data point, and that is the edit that matters. `Filled is not exhausted`
was a one-example warning at -76 (II-27 from a cell -74 filled). II-34 is the second (from a
cell -76 filled), and two examples make it a pattern rather than an anecdote about an anecdote.

GUARD HONESTY (WT-118): every OLD string asserted present before any backup or write.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TSV = ROOT / "docs/p7-passes.tsv"
TAG = ".bak-wt138"

ROW_ANCHOR = ("wealthTensor-76\tpaper-II\t5\tinherited-first-application\tA5 "
              "grep-each-module-against-its-paired-script + run every command §7 names "
              "(-75's axis, first on paper-II)\t2 of 5\tREVIEW-016 §1.2. II-27 from diffing "
              "the named command's output against §3; II-30 from grepping the file §7 names. "
              "II-28, II-29 and II-31 came from reading.")

NEW_ROW = ("wealthTensor-77\tpaper-II\t3\tnone\t— (all five axes inherited; Paper II was 5 of 5 "
           "before this pass and the handoff forbade a sixth while Paper III has three empty "
           "cells)\t0 of 3\tREVIEW-017. THE CONTROL ROW. First pass in the project run with the "
           "instrument set held still, and it returned THREE, not zero. Two of the three (II-32, "
           "II-33) are residue of -76's own repairs; one (II-34) is A5 pointed at §5 instead of "
           "§7 — a cell -76 had already filled. See REVIEW-017 §5: a repair pass creates surface, "
           "which is a reason for a non-zero count that has nothing to do with new instruments.")

CAVEAT_OLD = """# THE CAVEAT THAT KEEPS THIS HONEST: FILLED IS NOT EXHAUSTED. -76's II-27 came out of A4, a cell
# -74 had ALREADY filled on Paper II — because -74 ran the commands and did not diff their output
# against §3 cell by cell. A filled cell is a floor, not a certificate. Read this matrix as "which
# axes have never been pointed at this manuscript", never as "which axes are done with it"."""

CAVEAT_NEW = """# THE CAVEAT THAT KEEPS THIS HONEST: FILLED IS NOT EXHAUSTED, AND IT IS NOW TWO-FOR-TWO.
# -76's II-27 came out of A4, a cell -74 had ALREADY filled on Paper II — because -74 ran the
# commands and did not diff their output against §3 cell by cell. -77's II-34 came out of A5, a
# cell -76 had already filled — because -76 ran A5 against the artefacts §7 names and the
# manuscript names one in §5 too. EVERY TIME A "FILLED" CELL HAS BEEN RE-ENTERED IT HAS PAID.
# A filled cell is a floor, not a certificate. Read this matrix as "which axes have never been
# pointed at this manuscript", never as "which axes are done with it".
#
# WHAT -77 ADDS THAT NO OTHER ROW COULD: it is the CONTROL. `none` in new_instrument, three
# findings out. Two of seven rows now cut against the new-instrument anecdote (-71, -77), and
# -77's is the stronger because it was assigned a frozen set deliberately. REVIEW-017 §5 offers
# the alternative mechanism — a repair pass creates surface for the next pass to read — and it
# is testable at -78, which inherits four edits and nothing else new."""


def main():
    text = TSV.read_text()
    assert text.count(ROW_ANCHOR) == 1, "GUARD FAILED: -76's row not found verbatim"
    assert "wealthTensor-77" not in text, "GUARD FAILED: a -77 row already exists"
    assert text.count(CAVEAT_OLD) == 1, "GUARD FAILED: the caveat block not found verbatim"
    assert CAVEAT_NEW not in text, "GUARD FAILED: new caveat already present"

    out = text.replace(ROW_ANCHOR, ROW_ANCHOR + "\n" + NEW_ROW, 1)
    out = out.replace(CAVEAT_OLD, CAVEAT_NEW, 1)

    TSV.with_suffix(TSV.suffix + TAG).write_text(text)
    TSV.write_text(out)

    # ---- POST-CONDITIONS ----
    now = TSV.read_text()
    rows = [l for l in now.splitlines() if l and not l.startswith("#")]
    assert len(rows) == 7, f"POST-CONDITION FAILED: {len(rows)} data rows, want 7"
    for i, r in enumerate(rows):
        f = r.split("\t")
        assert len(f) == 7, f"POST-CONDITION FAILED: row {i} has {len(f)} fields, want 7"
    assert rows[-1].startswith("wealthTensor-77\tpaper-II\t3\tnone\t"), \
        "POST-CONDITION FAILED: -77's row is not last or not `none`"
    # the field that makes the ledger worth having must still be three-valued
    vals = {r.split("\t")[3] for r in rows}
    assert vals == {"none", "new", "new+inherited-first-application",
                    "inherited-first-application"}, f"POST-CONDITION FAILED: values drifted: {vals}"
    print(f"wt138 OK -- 7 rows, all 7 fields wide, -77 recorded as `none` with 3 findings")


if __name__ == "__main__":
    main()
