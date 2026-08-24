import pathlib, sys
REPO = pathlib.Path.home() / "repos/wealth-tensor"
T = REPO / "docs/done-criteria.tsv"
FAILED, NEG = [], 0
def chk(l, c, n=False):
    global NEG
    if n: NEG += 1
    print("  %s %s%s" % ("PASS" if c else "FAIL", "(NEGATIVE) " if n else "", l))
    if not c: FAILED.append(l)

orig = T.read_text()
OLD = "Ship the corpus per docs/DEFINITION-OF-DONE-SHIP.md: zero OPEN S1 and zero OPEN S2 on the FROZEN ship list"
NEW = ("Ship the corpus per docs/DEFINITION-OF-DONE-SHIP.md: STRUCTURALLY FINAL manuscripts Jason can rewrite from "
       "-- zero OPEN S1, zero OPEN S2, zero open C-class")
ADD = (" AMENDED THE SAME DAY, SAME SESSION: the truth rubric (S1/S2/S3) could not see the defect class that "
       "actually matters, because antithesis residue, scaffolding voice, orphans and fold problems are ALL TRUE "
       "STATEMENTS and every one scored S3 and shipped. Section 2.5 adds the blocking C-class with seven named "
       "types (register drift is FLAGGED not fixed -- re-voicing is JASON'S pass). The -106 hard stop is GONE: a "
       "countdown teaches a session to stop on a NUMBER, the exact failure it was meant to prevent. Section 3.0 is "
       "a RATCHET -- every pass owns its SUCCESSOR'S preconditions -- and Jason rules only on a TWICE-stalled gate. "
       "THE END PRODUCT IS NOT A CORRECT MANUSCRIPT, IT IS ONE JASON CAN REWRITE FROM WITHOUT A FALSE START.")
lines = orig.split("\n")
hit = 0
for i, l in enumerate(lines):
    if l.startswith("P7\t"):
        hit += 1
        c = l.split("\t")
        if OLD in c[2]:
            c[2] = c[2].replace(OLD, NEW)
        # THE FIRST AMENDMENT'S OWN SENTENCE HAD TO GO, NOT JUST BE APPENDED TO.
        # wt191 wrote "three named passes, and a hard stop at -106" into this note. Appending
        # "the -106 hard stop is GONE" after it leaves the cell CONTRADICTING ITSELF, and B5
        # caught exactly that -- a guard refusing because the file was wrong, which is the
        # correct direction. The stale clause is REPLACED; only then is the amendment appended.
        c[3] = c[3].replace(
            "three named passes, and a hard stop at -106.",
            "and four named passes.")
        if ADD.strip() not in c[3]:
            c[3] = c[3] + ADD
        lines[i] = "\t".join(c)
new = "\n".join(lines)
if new != orig: T.write_text(new)
t = T.read_text()
row = [l for l in t.split("\n") if l.startswith("P7\t")][0]
chk("B1 exactly one P7 row", hit == 1)
chk("B2 the criterion names structural finality, not just truth", NEW in row)
chk("B3 the C-class is named on the board", "zero open C-class" in row)
chk("B4 NEGATIVE: the retired convergence wording is still gone",
    "TWO CONSECUTIVE passes yield ZERO" not in t, True)
chk("B5 NEGATIVE: the -106 countdown is no longer promised on the board",
    "hard stop at -106" not in t, True)
chk("B5b NEGATIVE: and the note does not contradict itself about the stop",
    not ("hard stop at -106" in row and "-106 hard stop is GONE" in row), True)
chk("B6 the ratchet is on the board", "RATCHET" in row)
chk("B7 the row still has four columns", row.count("\t") == 3)
chk("B8 NEGATIVE: every non-P7 row is byte-identical",
    all(a == b for a, b in zip(orig.split("\n"), t.split("\n")) if not a.startswith("P7\t")), True)
chk("B9 NEGATIVE: the file still has the same number of rows",
    len(orig.split("\n")) == len(t.split("\n")), True)
chk("B10 P7 is still manual/PENDING-HUMAN", row.split("\t")[3].startswith("manual:"))
chk("B11 NEGATIVE: the note records that the amendment RAISED the bar",
    "NOT A CORRECT MANUSCRIPT" in row, True)
print("\n post-conditions: %d checks, %d NEGATIVE" % (12, NEG))
if FAILED:
    print(" FAILURE"); [print("   FAILED:", f) for f in FAILED]; sys.exit(1)
print(" ALL PASS")
