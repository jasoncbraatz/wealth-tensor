#!/usr/bin/env python3
"""wt192c — close the dangling references Jason's amendment left behind.

FOUND BY DOING THE THING THE LESSON SAYS: when you delete a feature, GREP FOR EVERY DOC THAT
MENTIONS IT before you celebrate a green run. Three survivors, and the first is the good one:

  1. DEFINITION-OF-DONE-SHIP.md's own loophole table, row L6, closed "infinite polish" by pointing
     at "section 3.4's hard stop at -106" -- A SECTION THE AMENDMENT DELETED. The table whose job
     is to close loopholes had a dangling pointer to the mechanism it named. Nothing went red;
     nothing could have. This is exactly wt191's C16 failure wearing prose instead of code.
  2. HANDOFF.md's ESTATE said the wt184 card "is the at-bat". It is now STEP 2 of Pass A.
  3. HANDOFF.md's TEE-UPS entry 1 said the same.

NOTE ON THE LABELS: these checks are R-prefixed, and that is DELIBERATE and load-bearing.
`tests/test_reg002_sec5_e4_extension_label.py::test_the_third_surface_scope_is_warranted` pins an
identity across every file in scripts/: substring hits on a certain two-character REG-002 exhibit
label, minus its known flake8-suppression homograph, must equal WORD-BOUNDARY hits on the same
label. A bookkeeping label that merely CONTAINS that token as a substring breaks the identity by
one, and the guard says exactly that: "a THIRD homograph has appeared, find it before trusting
either number." IT WAS RIGHT AND IT WAS MINE, twice -- first a check label, then this very
docstring while explaining the first. The token is deliberately NOT spelled here; see the test.
RENAMED, NEVER SILENCED -- the guard is one of the better ones in this repo.

EXIT 0 = repaired or verified. EXIT 1 = a post-condition failed.
"""
import pathlib, sys
REPO = pathlib.Path.home() / "repos/wealth-tensor"
FAILED, NEG = [], 0
def chk(l, c, n=False):
    global NEG
    if n: NEG += 1
    print("  %s %s%s" % ("PASS" if c else "FAIL", "(NEGATIVE) " if n else "", l))
    if not c: FAILED.append(l)

D = REPO / "docs/DEFINITION-OF-DONE-SHIP.md"
d = D.read_text()
L6_OLD = ('| L6 | **The infinite polish.** "A few more passes" with no enforcement. | § 3.4\'s hard '
          'stop at `-106`, with an explicit ship-with-remainder-disclosed path. |')
L6_NEW = ('| L6 | **The infinite polish.** "A few more passes" with no enforcement. | § 3.0\'s '
          '**ratchet** — a pass closes only when its successor can start AND finish — plus § 3.5, '
          'where a **twice-stalled** precondition becomes a Jason ruling with an explicit '
          'ship-with-remainder-disclosed path. *(This row named § 3.4\'s hard stop until `-102` '
          'noticed the amendment had DELETED § 3.4: the loophole table had a dangling pointer to '
          'the mechanism it was citing, and nothing went red. See L10.)* |')
if L6_OLD in d:
    d = d.replace(L6_OLD, L6_NEW, 1)
    D.write_text(d)
d = D.read_text()
# R1/R4 (WAS E1/E4) TRIPPED ON THE DISCLOSURE THEY WERE WRITTEN TO PROTECT -- a MENTION-vs-USE bug, and the
# THIRD time this repo has hit one (handoff_gate --emit refused a handoff for NAMING the markers
# TODO/TBD in a sentence about those markers; -94 fixed it there). A negative grep cannot tell a
# CITATION from a HISTORY NOTE. The honest checks: the row's mechanism column must LEAD with the
# live section, and any surviving 3.4 must sit inside the parenthetical that explains its death.
_l6 = [l for l in d.split("\n") if l.startswith("| L6 |")][0]
_mech = _l6.split("|")[3]
chk("R1 L6's mechanism column LEADS with the live section, not the deleted one",
    _mech.strip().startswith("§ 3.0's **ratchet**"))
chk("R1b NEGATIVE: and 3.4 survives ONLY inside the parenthetical that records its deletion",
    all(seg.count("3.4") == 0 for seg in _l6.split("*(")[:1]), True)
chk("R2 L6 cites the ratchet and the twice-stall ruling instead",
    "L6 |" in d and "§ 3.0's **ratchet**" in d and "§ 3.5" in d)
chk("R3 NEGATIVE: the correction is disclosed in the row rather than applied silently",
    "dangling pointer to" in d, True)
chk("R4 NEGATIVE: no section 3.4 reference survives OUTSIDE that one historical note",
    len([l for l in d.split("\n") if "3.4" in l and not l.startswith("| L6 |")]) == 0, True)
chk("R4b NEGATIVE: and the document really has no section 3.4 heading any more",
    "### 3.4" not in d and "## 3.4" not in d, True)
chk("R5 NEGATIVE: every loophole row L1-L11 is still present",
    all(("| L%d |" % i) in d for i in range(1, 12)), True)

H = REPO / "docs/HANDOFF.md"
h = H.read_text()
EST_OLD = "- **Carded this session:** `wt184` Rule 1 — State Machine `1217774684736450`. That is the at-bat."
EST_NEW = ("- **Carded this session:** `wt184` Rule 1 — State Machine `1217774684736450`. **It is STEP 2\n"
           "  of Pass A, not the whole at-bat** — Jason's amendment made the at-bat larger than this card.")
if EST_OLD in h:
    h = h.replace(EST_OLD, EST_NEW, 1)
TEE_OLD = ("1. **THE AT-BAT ABOVE** — `wt184` Rule 1's 44 unadjudicated paper-III flags, then the rule.\n"
           "   State Machine `1217774684736450`, with all four measured defects written out.")
TEE_NEW = ("1. **FOLDED INTO YOUR AT-BAT AS STEP 2** — `wt184` Rule 1's 44 unadjudicated paper-III flags,\n"
           "   then the rule. State Machine `1217774684736450`, with all four measured defects written\n"
           "   out. **It is no longer the whole at-bat**; Pass A is larger. Read it there, not here.")
if TEE_OLD in h:
    h = h.replace(TEE_OLD, TEE_NEW, 1)
if h != H.read_text():
    H.write_text(h)
h = H.read_text()
chk("R6 the ESTATE card no longer claims to BE the at-bat",
    "That is the at-bat." not in h)
# wealthTensor-103: R7, R8 and R10 assert the CONTENT OF docs/HANDOFF.md, which every successor
# session is REQUIRED to rewrite -- so this migration's post-conditions were green for exactly one
# session and red forever after. They are records of a COMPLETED migration, not live guards, so they
# now read the commit the migration landed in. R6, R9 and R11 stay pointed at the LIVE file, because
# those three are durable negatives that a future handoff really could violate.
import subprocess as _sp
_p = _sp.run(["git", "-C", str(REPO), "show", "7b5e114:docs/HANDOFF.md"],
             capture_output=True, text=True)
H102 = _p.stdout if _p.returncode == 0 else ""
chk("R7 the ESTATE card said what it actually was, at 7b5e114", "It is STEP 2\n  of Pass A" in H102)
chk("R8 tee-up 1 pointed at the at-bat instead of impersonating it, at 7b5e114",
    "FOLDED INTO YOUR AT-BAT AS STEP 2" in H102)
# R9 was `h.count(gid) >= 2` until wealthTensor-104 -- two MENTIONS in one file that every
# successor rewrites, which is the wt188 shape in a third costume. It now reads TWO FILES,
# one of them durable, so it fires on an orphaned card and not on an ordinary handoff rewrite.
POSTSHIP = (REPO / "docs/POST-SHIP.md").read_text(encoding="utf-8")
chk("R9 NEGATIVE: the wt184 card gid still resolves in the handoff AND in POST-SHIP",
    "1217774684736450" in h and "1217774684736450" in POSTSHIP, True)
chk("R10 NEGATIVE: at 7b5e114 the handoff named Pass A as the at-bat",
    "PASS A of the ship plan" in H102 or "PASS A OF THE SHIP PLAN" in H102, True)
chk("R11 NEGATIVE: no doc still promises an automatic stop at a session number",
    "hard stop at `-106`" not in d and "hard stop at -106" not in h.replace(
        "wt191 had written \"a hard stop at -106\"", ""), True)

print("\n post-conditions: %d checks, %d NEGATIVE" % (13, NEG))
if FAILED:
    print(" FAILURE"); [print("   FAILED:", f) for f in FAILED]; sys.exit(1)
print(" ALL PASS")
