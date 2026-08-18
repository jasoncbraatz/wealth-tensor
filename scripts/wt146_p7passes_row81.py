#!/usr/bin/env python3
"""wt146 · wealthTensor-81 · docs/p7-passes.tsv gains row 11, and the matrix commentary
records the answer to the question -80 wrote into it. The matrix itself does NOT move: it
closed at 15 of 15 and this pass filled no cell, which is the whole point of the row.

Idempotent. Eleven post-conditions, two of them NEGATIVE and load-bearing:
the row must NOT claim a new instrument, and the matrix must NOT change.
"""
import pathlib, re, shutil

REPO = pathlib.Path(__file__).resolve().parent.parent
TSV = REPO / "docs/p7-passes.tsv"
TAG = "wt146"

ROW = (
    "wealthTensor-81\tpaper-IV\t9\tnone\t"
    "— (all five axes inherited; the grid closed at -80, so NO cell could be filled. "
    "THE FIRST PASS IN THIS PROJECT'S HISTORY RUN ON A CLOSED MATRIX, which is the condition "
    "-80's coverage reading had to be tested in and the reason this at-bat existed.)\t"
    "0 of 9\t"
    "REVIEW-021. THE FALSIFIER ROW, AND COVERAGE IS DEAD. -80 proposed COVERAGE OF THE AXIS "
    "MATRIX and made the prediction explicit: a pass with nowhere left to be structurally blind "
    "should return MATERIALLY FEWER THAN NINE. This pass had a closed grid, filled no cell, and "
    "returned NINE -- 9 of 9 from cells that were already filled, on a manuscript that was at "
    "5 of 5 before and after. That is the FOURTH mechanism refuted by the pass immediately after "
    "the pass that proposed it (new instruments -71/-77, residue -77/-78, depth -78/-79, "
    "coverage -80/-81), and REVIEW-021 section 5 argues the four-for-four is the finding rather "
    "than any of the four: every mechanism was proposed by the pass whose own number it "
    "explained, and every one died next pass. -78's reading -- the counter measures the "
    "REVIEWERS -- is what is left, and REVIEW-021 says out loud that it survives partly because "
    "it predicts nothing. RESIDUE 2 of 9: IV-1 and IV-3 blame to 7ca35c7 (-75) and were ADDED by "
    "the edit that repaired the defect -75's own global lesson describes; the other seven blame "
    "to 5efe626, present since 2026-08-16 through three prior reads. MEASUREMENT, not mechanism: "
    "naming a defect class does not exhaust it in the site where it was named, even for the pass "
    "that named it -- four of nine are in the section -75 wrote its lesson FROM. SHAPES REPLICATE "
    "EXACTLY: 5 promise-about-artefact / 2 deferral-with-empty-target / 2 neither, the SAME split "
    "-80 found on Paper III, now on a third manuscript by a different reviewer -- two data points "
    "became a property of the corpus. MANUSCRIPT EDITS: 9 of 9, so -79's proposed narrower rule "
    "scores this pass 9 as well; the two rules agree here and separated -79 and -80 by the same "
    "margin. NOT APPLIED; this row is on the current rule."
)

OLD_ASKABLE = """# WHAT IS NOW ASKABLE THAT WAS NOT:
#   Every manuscript is at 5/5, so the NEXT read of ANY of them is the first in this project's
#   history with nowhere left to be structurally blind. That is the condition under which a low
#   count means something. If Paper III's third read returns a number near Paper II's 2, coverage
#   explains the whole history and the counters can start measuring documents. If it returns nine
#   again, it does not — and the reading -78 pre-committed to, that the counter measures the
#   REVIEWERS, is the one left standing. Either way the next pass is worth more than the last six."""

NEW_ASKABLE = """# WHAT WAS ASKED HERE AT -80, AND THE ANSWER -81 BROUGHT BACK:
#   -80 wrote: "Every manuscript is at 5/5, so the NEXT read of ANY of them is the first in this
#   project's history with nowhere left to be structurally blind... If it returns nine again,
#   [coverage] does not [explain the history] — and the reading -78 pre-committed to, that the
#   counter measures the REVIEWERS, is the one left standing."
#   IT RETURNED NINE. -81 read Paper IV on a closed grid, filled no cell, and found nine, all
#   nine from filled cells. COVERAGE IS DEAD by the test -80 itself specified, in the words -80
#   itself wrote. Do not re-litigate this: the prediction was pre-committed and the run answered it.
#
# FOUR MECHANISMS, FOUR REFUTATIONS, ALWAYS BY THE VERY NEXT PASS:
#   new instruments   -> -71, -77.      repair residue -> -78.
#   depth of applic.  -> -79.           coverage       -> -81.
#   EVERY ONE was proposed by the pass whose own number it explained. That regularity is now the
#   most robust thing in this file, and it is a fact about the REVIEWERS, not the manuscripts.
#   -78's reading is what is left standing, and REVIEW-021 section 5 states its weakness in the
#   same breath: it survives because it predicts nothing, which is not the same as being right.
#
# SO WHAT IS ASKABLE NOW: STOP PROPOSING MECHANISMS FROM THE PASS THAT PRODUCED THE NUMBER.
#   Four attempts, four deaths, one shape. The next pass that finds a number and explains it in
#   the same document is the fifth. What has NOT been tried: two independent readers on the SAME
#   manuscript at the SAME coverage in the same window, which is the only design that separates
#   "the paper has n defects left" from "a reviewer finds n". That is Jason's to authorise -- it
#   costs two sessions to buy one data point -- and it is the first proposal in eleven rows that
#   is not a story a single pass told about itself."""


def main():
    t = TSV.read_text(encoding="utf-8")
    changed = 0
    if "wealthTensor-81\tpaper-IV" in t:
        print("  ALREADY  row 11")
    else:
        assert t.endswith("\n"), "ledger does not end with a newline"
        t = t + ROW + "\n"
        changed += 1
        print("  APPENDED row 11")
    if OLD_ASKABLE in t:
        t = t.replace(OLD_ASKABLE, NEW_ASKABLE, 1)
        changed += 1
        print("  REWROTE  the askable block")
    elif NEW_ASKABLE.split("\n")[0] in t:
        print("  ALREADY  the askable block")
    else:
        raise SystemExit("askable block anchor not found")

    if changed:
        shutil.copy2(TSV, str(TSV) + ".bak-" + TAG)
        TSV.write_text(t, encoding="utf-8")

    t = TSV.read_text(encoding="utf-8")
    rows = [l for l in t.splitlines() if l.startswith("wealthTensor-")]
    r81 = [l for l in rows if l.startswith("wealthTensor-81\t")]
    f = r81[0].split("\t") if r81 else []
    checks = [
        ("R1  eleven data rows", len(rows) == 11),
        ("R2  exactly one -81 row", len(r81) == 1),
        ("R3  the row has seven fields", len(f) == 7),
        ("R4  paper is paper-IV", f[1] == "paper-IV"),
        ("R5  findings is 9", f[2] == "9"),
        ("R6  NEGATIVE - new_instrument is 'none', the row claims NO new axis", f[3] == "none"),
        ("R7  findings_from_new_axis is '0 of 9'", f[5] == "0 of 9"),
        ("R8  the row names its review document", "REVIEW-021" in f[6]),
        ("R9  NEGATIVE - the matrix still reads 15 of 15 and was not touched",
         "# FILLED: 15 of 15.  THE GRID IS CLOSED, at wealthTensor-80." in t),
        ("R10 NEGATIVE - no paper-IV cell in the matrix moved",
         "# IV     | -75 (wt130)   | -75 (IV-6)     | -75 (wt133)   | -75 (60 cells) | -75 (IV-2a)" in t),
        ("R11 the askable block records the answer, not the question",
         "IT RETURNED NINE." in t and "If Paper III's third read returns a number near" not in t),
        ("R12 no tab inside any field of the new row",
         all("\t" not in x for x in f[6:]) and r81[0].count("\t") == 6),
    ]
    for n, ok in checks:
        print("  %s  %s" % ("PASS" if ok else "FAIL", n))
    bad = [n for n, ok in checks if not ok]
    if bad:
        raise SystemExit("POST-CONDITIONS FAILED: %s" % bad)
    print("\nwt146: %d change(s), %d/%d post-conditions green." % (changed, len(checks), len(checks)))


main()
