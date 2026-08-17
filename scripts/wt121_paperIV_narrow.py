#!/usr/bin/env python3
"""wt121_paperIV_narrow.py -- narrow Paper IV's title and abstract leading clause.

JASON'S RULING, 2026-08-17 (wealthTensor-66b): replace the ladder framing "from the
household to the sovereign" with type identity at three NAMED scales.

WHY THIS IS NOT A NEW IDEA -- IT IS A REMEDY OPEN SINCE E1 AND FALSELY CERTIFIED BY E3
---------------------------------------------------------------------------------------
END-TO-END-001 leg E1 rejected the CHAIN relation between the sovereign and firm scales
(Paper II's rho and Paper III's phi are not one object seen twice; a lag and a loss are
different operators; Paper II has no parameter playing alpha's part) and issued a remedy
requiring the abstract's "from the household to the sovereign" to be NARROWED to the
scales actually joined.

E3 reported that remedy APPLIED and quoted, in quotation marks, an abstract reading
"the same atomic state composes by addition wherever it is summed". RESULT-...-E6.md
sec 6 establishes THAT STRING OCCURS NOWHERE IN THE CORPUS. Diffed against
paper-IV.md.bak-wt57-e3, E3's actual edit was `unit` -> `**state**` plus the APPENDED
"sooner than an earlier draft claimed..." clause. The substance was appended; the phrase
the remedy names was never touched.

So this script closes a remedy that has been open across five sessions, was certified
closed by the session that half-applied it, and was caught by a later leg. Jason's
ruling supplies the wording; E1 supplied the requirement.

E3's phantom wording is NOT adopted. "Wherever it is summed" drops the scales entirely,
and it was never ratified by anyone -- adopting a sentence that only ever existed inside
a false certification would be a strange way to repair a false certification. The
addition mechanism it names is already carried by the very next abstract paragraph
("The unit is an extensive state, and extensive states add") and by the title's first
clause.

WHAT CHANGES, AND WHAT DELIBERATELY DOES NOT
---------------------------------------------
1. TITLE: "one atomic unit from the household to the sovereign"
       -> "one atomic unit at the household, firm and sovereign scales"
   105 chars. Titles are NOT bound by the body's 100-column hard wrap -- measured, not
   assumed: paper-I.md's title is 115 chars.

2. ABSTRACT paragraph 1, replaced whole (the -65 rule: in re-wrapped prose the only safe
   anchor is THE WHOLE PARAGRAPH; a sentence anchor collides with whatever survived on
   the same source line).
   - "composes from the household to the sovereign" -> "has one type at the household,
     firm and sovereign scales". Type identity is what E1 left standing; the ladder is
     what it removed.
   - "and states exactly where composition stops -- sooner than an earlier draft
     claimed, because..." -> "and on one limit its own end-to-end test imposed: ...".
     THE DEMOTION IS ACHIEVED BY DELETING THE ASSERTION, NOT BY ARGUING WITH IT
     (WT-098). Once the leading clause no longer promises a ladder, the clause that
     walked the ladder back has nothing to do, and it goes -- taking one G-COACH-3
     conduct-narration hit with it.

3. NOT TOUCHED: the sixteen occurrences of the phrase in END-TO-END-001.md and the
   RESULT-...-E1/E2/E3/E6 documents. Those are RECORDS OF WHAT THE PAPER SAID AT THE
   TIME, and rewriting them would falsify the history of what past sessions did -- the
   WT-099 corollary, and the same reason a patch script's own quoted anchors are left
   alone. The census (scripts/wt120_scale_census.py) reports them as a separate
   category rather than dropping them silently.

VERIFIED BEFORE WRITING: scripts/wt120_scale_census.py found ZERO content SHAs pinned
against paper-IV.md, so the PIN-001 guard should not go red on this edit. "Should" is
not "does" -- WT-095 stands, run the suite.

USAGE
    python3 scripts/wt121_paperIV_narrow.py --dry     # writes *.wt66b-dryrun
    python3 scripts/wt121_paperIV_narrow.py
"""

import argparse
import shutil
import sys

PATH = "docs/papers/paper-IV-composition/paper-IV.md"

OLD_TITLE = ("# The tensor composes, the behaviour does not: "
             "one atomic unit from the household to the sovereign")
NEW_TITLE = ("# The tensor composes, the behaviour does not: "
             "one atomic unit at the household, firm and sovereign scales")

OLD_ABS = (
    "Three literatures describe wealth and do not read each other: biophysical economics, stock-flow\n"
    "consistent macroeconomics, and kinetic-exchange econophysics. This paper joins them on one claim —\n"
    "the same atomic **state** composes from the household to the sovereign — and states exactly\n"
    "where composition stops — sooner than an earlier draft claimed, because the corpus's end-to-end\n"
    "test found the sovereign and firm scales share **one question, not one structure**."
)

NEW_ABS = (
    "Three literatures describe wealth and do not read each other: biophysical economics, stock-flow\n"
    "consistent macroeconomics, and kinetic-exchange econophysics. This paper joins them on one claim —\n"
    "the same atomic **state** has one type at the household, firm and sovereign scales — and on one\n"
    "limit its own end-to-end test imposed: those scales share **one question, not one structure**."
)

EDITS = [("title", OLD_TITLE, NEW_TITLE), ("abstract-para-1", OLD_ABS, NEW_ABS)]

WRAP_LIMIT = 100


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()

    src = open(PATH).read()

    # ---- assert count == 1 for EVERY anchor BEFORE any write.
    ok = True
    for name, old, _new in EDITS:
        n = src.count(old)
        print("anchor %-16s occurrences=%d (require exactly 1)" % (name, n))
        if n != 1:
            ok = False
    if not ok:
        print("REFUSING: at least one anchor is not unique.")
        return 2
    if "at the household, firm and sovereign scales" in src:
        print("REFUSING: narrowing already present (idempotence guard).")
        return 3

    out = src
    for _name, old, new in EDITS:
        out = out.replace(old, new)

    # ---- line width, measured in CHARACTERS not bytes: —, ⊙, φ, δ are multi-byte and
    # `awk 'length>100'` would report a 94-character line as 100+. Body prose only;
    # the title is a heading and is exempt (measured: paper-I.md's title is 115).
    over = [(i + 1, len(l), l[:70]) for i, l in enumerate(NEW_ABS.split("\n"))
            if len(l) > WRAP_LIMIT]
    if over:
        print("REFUSING: replacement prose exceeds %d characters:" % WRAP_LIMIT)
        for ln, w, t in over:
            print("   line %d width %d :: %s" % (ln, w, t))
        return 4
    print("replacement prose widths (chars): %s -- all <= %d"
          % ([len(l) for l in NEW_ABS.split("\n")], WRAP_LIMIT))
    print("new title width (chars): %d  [heading, exempt from the body wrap]"
          % len(NEW_TITLE))

    dest = PATH + ".wt66b-dryrun" if a.dry else PATH
    if not a.dry:
        shutil.copyfile(PATH, PATH + ".bak-wt66b-narrow")
        print("backed up -> %s.bak-wt66b-narrow" % PATH)
    open(dest, "w").write(out)
    print("wrote %s  (%d -> %d chars)" % (dest, len(src), len(out)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
