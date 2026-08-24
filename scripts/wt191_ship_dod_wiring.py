import pathlib, subprocess, sys
REPO = pathlib.Path.home() / "repos/wealth-tensor"
FAILED, NEG = [], 0
def chk(label, cond, negative=False):
    global NEG
    if negative: NEG += 1
    print("  %s %s%s" % ("PASS" if cond else "FAIL", "(NEGATIVE) " if negative else "", label))
    if not cond: FAILED.append(label)

# ---------- 1 · done-criteria.tsv : the P7 row ----------
T = REPO / "docs/done-criteria.tsv"
orig = T.read_text()
OLD_TEXT = "Convergence per paper: fresh-eyes review passes repeat until TWO CONSECUTIVE passes yield ZERO substantive findings"
NEW_TEXT = "Ship the corpus per docs/DEFINITION-OF-DONE-SHIP.md: zero OPEN S1 and zero OPEN S2 on the FROZEN ship list"
OLD_NOTE_HEAD = "manual:perfection==done operationalized; a zero-finding pass is a RESULT and gets its REVIEW doc."
NEW_NOTE_HEAD = ("manual:SUPERSEDED AT -102 BY JASON'S RULING -- the convergence clause (two consecutive "
  "zero-finding passes per paper) is RETIRED and docs/DEFINITION-OF-DONE-SHIP.md is the SSOT for what done means. "
  "Sixteen passes, zero zeros, and paper-II's last eight sit flat in a 2-5 band: a stopping rule that terminates "
  "only when a backlog empties, on a process whose backlog is stationary, has no termination proof -- and it "
  "REWARDED NOT LOOKING, which every honest session had to fight. Replaced by a FROZEN, FINITE ship list gated on "
  "severity (S1 false / S2 unsupported BLOCK; S3 precision ships disclosed), three named passes, and a hard stop "
  "at -106. The bar on the WORK is unchanged; only the stopping rule moved.")
lines = orig.split("\n")
hit = 0
for i, l in enumerate(lines):
    if l.startswith("P7\t"):
        hit += 1
        c = l.split("\t")
        assert len(c) == 4, len(c)
        c[2] = c[2].replace(OLD_TEXT, NEW_TEXT)
        c[3] = c[3].replace(OLD_NOTE_HEAD, NEW_NOTE_HEAD)
        lines[i] = "\t".join(c)
newtsv = "\n".join(lines)
if newtsv != orig:
    T.write_text(newtsv)
t = T.read_text()
chk("C1 exactly one P7 row was rewritten", hit == 1)
chk("C2 the P7 row now points at the ship DoD", NEW_TEXT in t)
chk("C3 NEGATIVE: the retired convergence wording is GONE from the criteria", OLD_TEXT not in t, True)
chk("C4 the P7 row still has four columns", all(l.count("\t") == 3 for l in t.split("\n") if l.startswith("P7\t")))
# C5 ASSUMED THIS WAS THE FIRST APPLICATION. On the second run orig == t, so ZERO lines differ
# and a `== 1` check fails on its own success -- the same defect wt188's E4 and wt189's Q11 both
# had this session, now three-for-three. The durable statement is about WHICH rows may differ,
# not HOW MANY: every non-P7 row is untouched, which is true on both paths.
chk("C5 NEGATIVE: every criterion row OTHER than P7 is byte-identical",
    all(a == b for a, b in zip(orig.split("\n"), t.split("\n")) if not a.startswith("P7\t")), True)
chk("C5b NEGATIVE: and the file still has the same number of rows",
    len(orig.split("\n")) == len(t.split("\n")), True)
chk("C6 P7 is still manual: (PENDING-HUMAN, not auto-closable)",
    [l for l in t.split("\n") if l.startswith("P7\t")][0].split("\t")[3].startswith("manual:"))

# ---------- 2 · HANDOFF definition_of_done ----------
H = REPO / "docs/HANDOFF.md"
ho = H.read_text()
OLD_DOD = ('definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, '
 'every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review '
 'passes per paper), Jason\'s own-hand pass complete — then the batch declared, once."')
NEW_DOD = ('definition_of_done: "SEE docs/DEFINITION-OF-DONE-SHIP.md — IT IS THE SSOT AND IT WINS OVER THIS LINE. '
 'Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from '
 'committed scripts, ZERO OPEN S1 AND ZERO OPEN S2 on the FROZEN docs/SHIP-LIST.md (the convergence clause — two '
 'consecutive zero-finding passes per paper — was RETIRED by Jason at -102 after sixteen passes produced zero '
 'zeros; it had no termination proof and it rewarded not looking), docs/SHIP-STATEMENT.md written, Jason\'s '
 'own-hand pass complete — then the batch declared, once. HARD STOP: if the ship list is not clear by the end of '
 '-106, the work stops and Jason rules on shipping with the remainder disclosed."')
assert ho.count(OLD_DOD) == 1 or ho.count(NEW_DOD) == 1, "DoD field not matched"
if OLD_DOD in ho:
    ho = ho.replace(OLD_DOD, NEW_DOD, 1)
    H.write_text(ho)
h = H.read_text()
chk("C7 HANDOFF's definition_of_done points at the ship DoD", "DEFINITION-OF-DONE-SHIP.md — IT IS THE SSOT" in h)
chk("C8 NEGATIVE: the retired convergence clause is no longer asserted as the DoD",
    "convergence reached (two consecutive zero-finding review" not in h, True)
chk("C9 definition_of_done is still exactly one line",
    len([l for l in h.split("\n") if l.startswith("definition_of_done:")]) == 1)

# ---------- 3 · POST-SHIP.md, carrying the freeze sha ----------
rc = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"], capture_output=True, text=True)
sha = rc.stdout.strip()
chk("C10 the freeze sha resolves", len(sha) == 40)
P = REPO / "docs/POST-SHIP.md"
if not P.exists():
    tmpl = pathlib.Path("/tmp/POST-SHIP.tmpl").read_text()
    assert "@@SHA@@" in tmpl, "template lost its placeholder"
    P.write_text(tmpl.replace("@@SHA@@", sha))
p = P.read_text()
# C11 ASSERTED THAT *CURRENT HEAD* IS ON POST-SHIP'S LINE 3. That is false the moment anything
# else is committed, which is every session -- and it collided with wt191b, whose whole job is to
# pin the freeze to the commit that DECLARED it rather than to whatever HEAD happens to be. Fifth
# first-run/moving-state assumption this session. The durable statement: line 3 carries a sha that
# git resolves AND that commit is the one that added the DoD document. wt191b OWNS that value;
# this check only confirms it is present and real, and does not re-derive it.
_l3 = p.split("\n")[2]
_cand = [w.strip("`*") for w in _l3.replace("`", " ").split() if len(w.strip("`*")) == 40]
chk("C11 POST-SHIP.md line 3 carries a resolvable 40-char sha", len(_cand) == 1
    and subprocess.run(["git", "-C", str(REPO), "cat-file", "-e", _cand[0]]).returncode == 0)
chk("C11b that commit is the one that ADDED the ship DoD, not whatever HEAD is today",
    _cand and "docs/DEFINITION-OF-DONE-SHIP.md" in subprocess.run(
        ["git", "-C", str(REPO), "show", "--name-only", "--format=", _cand[0]],
        capture_output=True, text=True).stdout)
chk("C11c NEGATIVE: the freeze is NOT pinned to current HEAD, which moves every session",
    _cand and _cand[0] != sha, True)
chk("C12 NEGATIVE: POST-SHIP does not claim to block anything",
    "Nothing in this file blocks shipping" in p, True)
chk("C13 the DoD points at POST-SHIP for the freeze rather than restating a sha",
    "that file's first line is the\n  authority" in (REPO / "docs/DEFINITION-OF-DONE-SHIP.md").read_text()
    or "first line is the" in (REPO / "docs/DEFINITION-OF-DONE-SHIP.md").read_text())

# ---------- 4 · the DoD document's own integrity ----------
d = (REPO / "docs/DEFINITION-OF-DONE-SHIP.md").read_text()
chk("C14 all eight loopholes L1-L8 are named", all(("| L%d |" % i) in d for i in range(1, 9)))
chk("C15 the three severity classes are defined", all(s in d for s in ("### S1 ·", "### S2 ·", "### S3 ·")))
chk("C16 the hard stop names a session", "-106" in d)
chk("C17 NEGATIVE: the rubric is committed BEFORE any retrospective scoring",
    "committed at the freeze, **ahead of Pass A's retrospective audit**" in d, True)
chk("C18 NEGATIVE: the charter still wins over this document",
    "CO-AUTHOR-CHARTER.md` still wins over this file" in d, True)
chk("C19 NEGATIVE: carding is explicitly NOT a way to close a blocker",
    "Carding is not a third option" in d, True)
chk("C20 Pass A is forbidden from repairing", "PASS A MAY NOT REPAIR ANYTHING" in d)

print("\n post-conditions: %d checks, %d NEGATIVE" % (23, NEG))
if FAILED:
    print(" FAILURE"); [print("   FAILED:", f) for f in FAILED]; sys.exit(1)
print(" ALL PASS")
