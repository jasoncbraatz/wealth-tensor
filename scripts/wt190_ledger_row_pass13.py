#!/usr/bin/env python3
"""wt190 — append wealthTensor-102's row to docs/p7-passes.tsv (Paper II, P7 pass 13).

A LEDGER ROW IS A CLAIM AND A CLAIM NEEDS A SCRIPT.  The row's own falsifier block lives in
REVIEW-037's front matter and points at scripts/wt188_paperII_p7pass13.py for the numbers;
this file exists so the APPEND itself is re-checkable rather than a hand edit -- seven
columns, no empty cell, the header untouched, and the row present exactly once.

IDEMPOTENT AND STILL AUDIBLE (-101's rule): the already-appended path re-runs every
post-condition against the file on disk and prints the same summary line, so a count_re can
hold this script to a number on the second run as well as the first.

EXIT 0 = row appended or verified.  EXIT 2 = a post-condition failed; the TSV is rolled back.
"""
import pathlib
T = pathlib.Path("docs/p7-passes.tsv")
orig = T.read_text()
ROW = "\t".join([
 "wealthTensor-102", "paper-II", "2", "none",
 "— (none. All five axes A1-A5 inherited and run before a word of prose; the grid closed at 15 of 15 at -80 and paper-II sits at 5 of 5, so no cell could be filled. A3' -- pointer CORRECTNESS -- is inherited TWICE OVER: the axis originates wealthTensor-99 on this manuscript (II-40) and the INSTRUMENT, scripts/wt184_pointer_correctness.py, was built at -101 and blames to d162969. This pass is its FIRST APPLICATION TO PAPER II, the held-out test -101's handoff set up. A6 stays parked, sixth pass. scripts/wt188_paperII_p7pass13.py (62 post-conditions, 19 NEGATIVE, idempotent) and scripts/wt189_paperII_promises.py (19, 11 NEGATIVE, idempotent) are the PATCHES of record, not instruments. The FIFTH consecutive frozen-instrument pass on paper-II.)",
 "0 of 2",
 "REVIEW-037. TWO FINDINGS, TWO REPAIRS, ALL LANDED IN-PASS, ZERO CARDED -- and 2 TIES THE LOWEST NUMBER THIS MANUSCRIPT HAS EVER RECORDED (-78, -79). II-44 IS THE HEADLINE and it came out of tee-up 5, named at -74 and deferred at -77, -99, -100 and -101: the two Bouchaud & Mezard quotations were finally read against arXiv cond-mat/0002374, BOTH VERIFY WORD FOR WORD, and the sentence beside them does not -- SS3.1 and SS6 credited them with the stationary Pareto exponent 'in closed form in all four coordinates', which in THIS manuscript's own defined vocabulary (Abstract, SS1, SS2.2) means base, rate, periodicity and threshold. Their solution is continuous-time and carries neither; their four are phi_I, phi_C, f_I, f_C. The over-credit handed SS3.3 to a 26-year-old closed form. STEELMAN, three sites, and the third site retires the paper's THIRD word-collision -- the only one of three it never disclosed, one sentence after the disclosure of the second. II-43 is A4's SECOND QUESTION run on paper-II for the first time: SS7 enumerates 'five quantities neither command prints' and there are SIX -- SS3.1's 6e-6 change in Var[log a], a difference of two values wt077_tail_index.py prints. THE NEW AXIS FOUND NOTHING AND THAT IS THE OTHER RESULT: wt184's first paper-II run returned 11 Rule-1 flags, 11 of 11 FALSE POSITIVES from co-occurrence-as-attribution -- the SAME defect -101 diagnosed in Rule 2 and believed Rule 1 did not have. Measured: Rule 1 has NO possessive form anywhere, and its flag set was never cut from 44 to 5 -- it stood at 43 at -101's own parent commit 74934b9 and 44 at HEAD, all forty-three unadjudicated. Plus a fourth instrument defect: wt184 buckets SS6's 'their SS4.1' (Benhabib/Bisin/Zhu's) as UNRESOLVED where wt133 dismisses it as another document's, and wt184's own post-condition asserting agreement with wt133 is written for paper-III only. FOUR INSTRUMENT DEFECTS RECORDED, NOT COUNTED (the -99 precedent). RESIDUE 0 of 2 -- II-43's defective word blames to 76355d62 (-92, a repair pass) and II-44's three sites to bf073634, 2026-08-17, eight P7-read commits ago -- AND NO MECHANISM IS PROPOSED FROM IT; the pass declines the sixth on n=2 exactly as -101 declined on n=3. SHAPES 2 promise / 0 deferral / 0 neither on REVIEW-019 SS6's definitions, against -83's 1/2/1 and -101's 1/1/1; n=2 and this row claims nothing from it. MANUSCRIPT EDITS 2 of 2 findings over 5 sites, and -79's narrower rule scores this pass 2 as well. defensive_count --against the pre-edit file: 0 -> 0 (+0) outside SSLimitations on a manuscript whose baseline is ZERO. G-COACH-3 holds. STRENGTH BANKED, NOT A FINDING: SS3.3's interior minimum was measured at the REPORTED horizon T=1200 across five seeds and the argmin is P=30 on five of five, so the claim SS5 declines to defend at the third decimal holds at the third decimal -- the II-34 question answered for one figure and one only. CONSECUTIVE-ZERO COUNT AFTER THIS PASS: 0. The pass does not score P7; that is PENDING-HUMAN.",
])
assert ROW.count("\t") == 6, ROW.count("\t")
if "wealthTensor-102\tpaper-II" in orig:
    print("row already present - verifying, not rewriting.")
    text = orig
else:
    text = orig.rstrip("\n") + "\n" + ROW + "\n"
    T.write_text(text)
rows = [l for l in text.split("\n") if l.startswith("wealthTensor-")]
checks = [
  ("L1 the row is present exactly once", len([l for l in rows if l.startswith("wealthTensor-102\t")]) == 1, True),
  ("L2 the row has SEVEN columns", all(l.count("\t") == 6 for l in rows if l.startswith("wealthTensor-102\t")), False),
  ("L3 every row in the file still has seven columns", all(l.count("\t") == 6 for l in rows), True),
  ("L4 the ledger now holds SIXTEEN passes", len(rows) == 16, False),
  ("L5 paper-II now holds NINE ledger rows", len([l for l in rows if l.split("\t")[1] == "paper-II"]) == 9, False),
  ("L6 findings column is 2", [l for l in rows if l.startswith("wealthTensor-102\t")][0].split("\t")[2] == "2", False),
  ("L7 new_instrument is none (A3' instrument blames to -101, not here)",
   [l for l in rows if l.startswith("wealthTensor-102\t")][0].split("\t")[3] == "none", False),
  ("L8 findings_from_new_axis is 0 of 2", [l for l in rows if l.startswith("wealthTensor-102\t")][0].split("\t")[5] == "0 of 2", False),
  ("L9 the header comment block is untouched",
   text.count("# session\tpaper\tfindings\tnew_instrument\tinstrument_name\tfindings_from_new_axis\tnotes") == 1, True),
  ("L10 no cell is empty", "\t\t" not in ROW, True),
]
for lab, c, n in checks:
    print("  [%s] %s%s" % ("PASS" if c else "FAIL", "(NEGATIVE) " if n else "", lab))
print("ledger: 1 row %s, %d post-conditions, %d NEGATIVE"
      % ("verified" if "wealthTensor-102\tpaper-II" in orig else "appended",
         len(checks), sum(1 for _, _, n in checks if n)))
if any(not c for _, c, _ in checks):
    T.write_text(orig); print("ROLLED BACK"); raise SystemExit(2)
