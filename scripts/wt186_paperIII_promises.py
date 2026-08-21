#!/usr/bin/env python3
"""wt186 — adjudicate the FOUR promises wt185's §11 repair EMITTED (wealthTensor-101).

wt185 added one bullet to Paper III §11 — "Regenerate §4.10" — and wt148 immediately went
RED with four unadjudicated promises, which is the guard doing its job: a new sentence that
names an artefact is a new claim, and a claim nobody ran is not adjudicated by the fact that
the person who wrote it believed it.

NOTHING WAS RETIRED.  wt148 went 169 emitted -> 173, 156 adjudicated -> 156, 0 STALE -> 0.
wt185's other three edits touched prose that names no artefact, so no promise_id moved and
this script writes NO `#superseded` line.  If a successor sees one here, this comment is wrong.

RE-CHECK, DO NOT RE-KEY.  Every evidence cell below was RUN in wealthTensor-101, every note
quotes what it printed, and the seventh column is DERIVED from `wt148.emit()` rather than
transcribed — the wt183 pattern, after wt156 caught a six-column hand-written row.

EXIT 0 = four rows written, every post-condition holds.
EXIT 2 = refused or a post-condition failed; the TSV is rolled back to its pre-run bytes.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TSV = ROOT / "docs/promises-adjudicated.tsv"
sys.path.insert(0, str(ROOT / "scripts"))
import wt148_promise_sweep as wt148

PAPER_III = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"


def sentence_for(pid: str) -> str:
    """The SEVENTH column is derived from wt148's own emitter, never transcribed."""
    for e in wt148.emit(PAPER_III):
        if e["pid"] == pid:
            return e["sentence"]
    sys.exit("PRECONDITION FAILED: wt148 emits no promise %s for paper-III" % pid)


ROWS = [
 ("paper-III", "fe878a6dc4", "python3 scripts/wt091_lag_shape_identifiability.py", "H",
  "python3 scripts/wt091_lag_shape_identifiability.py | sed -n '/LADDER W/,/the search.s own floor/p'   (~6 min)",
  "prints §4.10's table, row for row: sigma 1e-06/1e-04/1e-03/1e-02 -> k in [1.21,1.21]/[1.16,1.26]/[0.6,1.87]/[0.6,2.0], widths 0.0000/0.1000/1.2700/1.4000, and 0.00/0.67/8.47/9.33 x -- the paper's 0.00/0.67/8.5/9.3. It also prints 'the search's own floor, at k = 1.21 (the truth): 2.691e-08 -- 37x below the finest sigma reported', which is §4.10's '2.7 x 10^-8, thirty-seven times below the finest tolerance reported'. THIS IS FINDING III-6: §11 named a Regenerate command for §3, §A.2.3, §5, §5.4 and §A.2.4 and NONE for §4.10 until wealthTensor-101, while this script -- registered, committed, and quoting the manuscript in its own docstring -- produced every number in it. The same output is finding III-5's evidence: it labels the reference 'REG-003's 0.150' on all four rows, never §5.4's",
  ),
 ("paper-III", "4198aa70dc", "docs/preregistration/REG-005-p3-lag-shape-identifiability.md", "H",
  "grep -n '^## ' docs/preregistration/REG-005-p3-lag-shape-identifiability.md",
  "prints §2 'Falsifiers on the construction -- each one can kill the instrument' and §5 'The ladders -- exhaustive, every real number in exactly one cell, all written before any run', so the file registers the falsifiers and the ladders the bullet attributes to it. wt091's own docstring names the same five, 'Ladders I, P, W, S and N are exhaustive', and its run prints ladders I, P, W, S and N under those letters -- so 'exactly as registered in REG-005' is borne out by the registration AND by the run",
  ),
 ("paper-III", "214e67a32a", "6f0e7be", "H",
  "git log -1 --format='%h %ad %s' --date=iso 6f0e7be; git log --diff-filter=A --format='%h %ad' --date=iso -- scripts/wt091_lag_shape_identifiability.py | tail -1",
  "prints '6f0e7be 2026-08-12 15:10:24 -0500 REG-005 registered: is the recognition lag's shape identified from a reported series?' and '42ca377 2026-08-12 16:24:12 -0500'. The registration commit precedes the script's first appearance in the repository by one hour and fourteen minutes, which is what the bullet's 'committed at 6f0e7be before that script existed' asserts and what §4.10's 'four falsifiers and five ladders before wt091 existed' asserts. Both hold on the same two lines of git log",
  ),
 ("paper-III", "64e11e7bc4", "wt091", "N",
  "grep -c '`wt091`' docs/papers/paper-III-dual-tensor/paper-III.md",
  "prints 2 -- §4.10's chronology sentence and the closing clause of the §11 bullet wt185 added. The clause asserts a fact about the MANUSCRIPT's own history (that this section named no command for §4.10 before wealthTensor-101), not a property of the artefact `wt091` that could fail independently: the artefact itself is adjudicated by row fe878a6dc4 under its runnable path. N, and the row exists so that the sweep stays green rather than because the bare token needs its own evidence",
  ),
]


def main():
    original = TSV.read_text()
    lines = original.split("\n")

    present = {l.split("\t")[1] for l in lines if l.startswith("paper-") and l.count("\t") >= 2}
    for r in ROWS:
        if r[1] in present:
            print("wt186: row %s already present — nothing to do." % r[1])
            return 0

    new_rows = ["\t".join(list(r) + [sentence_for(r[1])]) for r in ROWS]
    while lines and lines[-1] == "":
        lines.pop()
    text = "\n".join(lines + new_rows) + "\n"
    TSV.write_text(text)

    checks = []
    for i, r in enumerate(ROWS):
        checks.append(("Q%d row %s present exactly once" % (i + 1, r[1]),
                       text.count("\t" + r[1] + "\t") == 1, True))
    checks.append(("Q5 every new row has SEVEN columns",
                   all(len(l.split("\t")) == 7 for l in new_rows), False))
    checks.append(("Q6 the seventh column is wt148's, not a transcription",
                   all(l.split("\t")[6] == sentence_for(l.split("\t")[1]) for l in new_rows), False))
    checks.append(("Q7 no #superseded line was written (nothing was retired)",
                   text.count("#superseded\t") == original.count("#superseded\t"), True))
    checks.append(("Q8 promise_ids are unique across the whole file",
                   len({l.split("\t")[1] for l in text.split("\n") if l.startswith("paper-")}) ==
                   len([l for l in text.split("\n") if l.startswith("paper-")]), True))
    checks.append(("Q9 exactly four rows were added",
                   len([l for l in text.split("\n") if l.startswith("paper-")]) ==
                   len([l for l in original.split("\n") if l.startswith("paper-")]) + 4, True))
    checks.append(("Q10 no row carries a literal TAB inside a cell",
                   all("\t\t" not in l for l in new_rows), True))
    checks.append(("Q11 the scope line is untouched",
                   "#scope\tpaper-II\tpaper-III\tpaper-IV" in text, False))

    for label, cond, isneg in checks:
        print("  [%s] %s%s" % ("PASS" if cond else "FAIL", "(NEGATIVE) " if isneg else "", label))
    neg = sum(1 for _, _, n in checks if n)
    print("wt186: %d rows written, 0 superseded, %d post-conditions, %d NEGATIVE"
          % (len(ROWS), len(checks), neg))

    if any(not c for _, c, _ in checks):
        TSV.write_text(original)
        print("ROLLED BACK — the TSV is at its pre-run bytes.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
