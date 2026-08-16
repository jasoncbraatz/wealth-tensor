#!/usr/bin/env python3
"""wealthTensor-57 · P11 gets sub-rows, one per leg, so the board can show a run.

WHY. -56 named this and deliberately did not take it: "P11 HAS NO WAY TO SHOW THAT ONE OF
SIX LEGS IS RUN". It is now acute -- two legs are run, both FAILED, the pass verdict is
SYSTEM FAILS, and the board reads 45/59 exactly as it did two sessions ago. A fresh session
would conclude P11 was untouched.

THE TEMPLATE. All seven rows are one expression instantiated seven times. The check does not
assert that a leg passed; it asserts that the leg has a RESULT document which states a
verdict for that leg in its header, in the shape both existing result documents already use:

    - **Verdict: E<N> ...

That is a derivation, not a constant: the row goes green when the artefact says so and goes
red the moment the verdict line is removed, which is what scripts/redproof_p11.py proves.

SEEN RED. Five of the seven (P11b, P11d, P11e, P11f, P11g) are red at the moment of creation
because their legs have not run -- that is the check demonstrating it can fail, live, on
five instances. The two green ones (P11a, P11c) are red-proofed mechanically by
scripts/redproof_p11.py, which removes the verdict line from a copy, runs the row's OWN
check verbatim, requires a non-zero exit, and restores byte-for-byte.

Row ids are never renumbered. File order is dependency order: these sit immediately after
P11 and before P13, which is where they belong -- P13 is last, and P13 renders what this
verdict decides.
"""
import pathlib
import shutil
import sys

REPO = pathlib.Path.home() / "repos" / "wealth-tensor"
TSV = REPO / "docs" / "done-criteria.tsv"

CHECK = (
    "cmd:cd $HOME/repos/wealth-tensor && "
    "grep -qE '^- \\*\\*Verdict: %s ' docs/RESULT-END-TO-END-001-%s.md"
)

PASS_CHECK = (
    "cmd:cd $HOME/repos/wealth-tensor && "
    "grep -qE '^- \\*\\*Verdict: THE SYSTEM (HOLDS|IS WOUNDED|FAILS|PASS IS VOID)' "
    "docs/RESULT-END-TO-END-001.md"
)

LEGS = [
    ("P11a", "E1", "TEST",
     "the shared degeneracy — is the II<->III join load-bearing or vocabulary?",
     "RUN 2026-08-16 (wealthTensor-56). FAILED at E1a. Green."),
    ("P11b", "E2", "TEST",
     "the unowned claim — does the conjunction assert something no paper defends?",
     "NOT RUN. Wants a genuinely BLIND pass: the extraction is written down BEFORE "
     "END-TO-END-001 §2's candidate is read, and a run that reads the candidate first has "
     "destroyed the leg and must say so. Red, correctly."),
    ("P11c", "E3", "TEST",
     "the containment matrix — is ADR-001's promise about failure true?",
     "RUN 2026-08-16 (wealthTensor-57). FAILED on failure shape 2. Green."),
    ("P11d", "E4", "AUDIT",
     "the corpus's empirical content, stated whole",
     "NOT RUN. AUDIT: the designer expects the count to be zero, so the value is the "
     "pre-registered one-sentence remedy in Paper IV, not the discovery. Red, correctly."),
    ("P11e", "E5", "TEST",
     "the over-subscribed guard — does one test hold two claims that could come apart?",
     "NOT RUN. Cheap; P3n already established the repair shape (derive the count, do not "
     "assert it). RESULT-END-TO-END-001-E3.md §5 carries the quotations collected in "
     "passing and counted nowhere. Red, correctly."),
    ("P11f", "E6", "AUDIT",
     "the cross-paper contradiction — does the corpus assert and deny the same fact in two volumes?",
     "NOT RUN. AUDIT, and its worked example was found at design time and is EXCLUDED from "
     "its own run. Red, correctly."),
]

PASS_ROW = (
    "P11g", "corpus",
    "The pass verdict, read off END-TO-END-001 §3's rule rather than off anyone's judgement, "
    "and recorded in the pass-level RESULT document",
    PASS_CHECK,
    "cmd:, same template family. NOT WRITTEN. T = 2 as of wealthTensor-57 so §3's rule already reads THE SYSTEM "
    "FAILS and T can only rise, but the pass-level document is the artefact and it does not "
    "exist. This row is red until it does. Reporting the verdict in a leg document is not "
    "reporting the pass.",
)

NOTE = (
    "cmd:, generated from ONE template in scripts/add_p11_rows.py and red-proofed by "
    "scripts/redproof_p11.py. Checks that leg %s of END-TO-END-001 has a RESULT document "
    "stating a verdict for it -- not that the verdict was favourable; a leg that FAILS is a "
    "leg that RAN. Classified %s by the registration (§2.0). %s"
)


def main():
    lines = TSV.read_text(encoding="utf-8").split("\n")
    if any(l.startswith("P11a\t") for l in lines):
        sys.exit("ABORT: P11a already present")
    idx = [i for i, l in enumerate(lines) if l.startswith("P11\t")]
    if len(idx) != 1:
        sys.exit("ABORT: expected exactly one P11 row, found %d" % len(idx))

    new = []
    for rid, leg, kind, title, state in LEGS:
        crit = ("END-TO-END-001 leg %s is RUN and its verdict is recorded — %s" % (leg, title))
        new.append("\t".join([rid, "corpus", crit, CHECK % (leg, leg) + " # " + (NOTE % (leg, kind, state))]))
    new.append("\t".join([PASS_ROW[0], PASS_ROW[1], PASS_ROW[2], PASS_ROW[3] + " # " + PASS_ROW[4]]))

    shutil.copy2(TSV, str(TSV) + ".bak-wt57-p11")
    out = lines[: idx[0] + 1] + new + lines[idx[0] + 1:]
    TSV.write_text("\n".join(out), encoding="utf-8")
    print("inserted %d rows after P11" % len(new))


if __name__ == "__main__":
    main()
