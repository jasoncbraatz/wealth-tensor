#!/usr/bin/env python3
"""wt192 — Jason's SECOND amendment to the ship DoD: the coherence class and the ratchet.

WHAT CHANGED AND WHY (Jason, 2026-08-24, after reading -102's first cut):

  1. THE RUBRIC HAD A HOLE. Sections 2.1-2.4 grade TRUTH. The defect class Jason actually cares
     about -- antithesis residue, scaffolding voice, orphans, fold problems -- is ENTIRELY TRUE
     STATEMENTS, so every one scored S3 and SHIPPED. Exactly backwards. New section 2.5 adds the
     C-class, blocking, found and repaired in a new Pass D.
  2. THE HARD STOP INVITED THE FAILURE IT MEANT TO PREVENT. "-106 or stop" teaches a session to
     stop on a NUMBER. Replaced by a RATCHET: every pass owns its SUCCESSOR'S preconditions, and
     Jason rules only when the ratchet stalls TWICE ON THE SAME ONE.
  3. THE END PRODUCT WAS UNDER-SPECIFIED. "Correct" is necessary, not sufficient. The bar is a
     manuscript JASON CAN REWRITE FROM without a false start -- plus FIGURE-PLAN.md, because the
     corpus carries ZERO figure captions and ~230 table rows and his layout work needs a running
     start rather than a blank page.

Idempotent. The section bodies live in /tmp/sec*.md rather than inline, which is this repo's own
rule after five sessions of bash eating parens in heredocs.

EXIT 0 = amended or verified. EXIT 1 = a post-condition failed.
"""
import pathlib, sys, subprocess

REPO = pathlib.Path.home() / "repos/wealth-tensor"
D = REPO / "docs/DEFINITION-OF-DONE-SHIP.md"
FAILED, NEG = [], 0
def chk(l, c, n=False):
    global NEG
    if n: NEG += 1
    print("  %s %s%s" % ("PASS" if c else "FAIL", "(NEGATIVE) " if n else "", l))
    if not c: FAILED.append(l)

orig = D.read_text()
t = orig

S25 = pathlib.Path("/tmp/sec25.md").read_text().rstrip("\n")
S3  = pathlib.Path("/tmp/sec3.md").read_text().rstrip("\n")
S4  = pathlib.Path("/tmp/sec4.md").read_text().rstrip("\n")

# ---- 1 · splice: 2.5 goes after 2.4's close; 3 and 4 are replaced wholesale ----
A = "\n---\n\n## 3 · THE BOUNDED PLAN"
B = "\n---\n\n## 4 · WHAT SHIPPING PRODUCES"
C = "\n---\n\n## 5 · THE LOOPHOLES THIS CLOSES"
if "## 2.5 · THE COHERENCE CLASS" not in t:
    i, j, k = t.index(A), t.index(B), t.index(C)
    t = t[:i] + "\n" + S25 + "\n\n" + S3 + "\n\n" + S4 + "\n" + t[k:]
    # loophole table gains two rows
    LAST = ("| L8 | **Silent imperfection.** Shipping while quietly knowing about S3s. | "
            "§ 4.3 publishes them **in the papers**. |")
    assert LAST in t or "| L8 |" in t
    L910 = LAST + """
| L9 | **Truth-only grading.** A paper free of S1 and S2 that still reads as a lab notebook — every seam is a TRUE statement, so every seam scored S3 and shipped. | § 2.5's **C-class**, blocking, with seven named defect types and a Pass that owns them. |
| L10 | **Stopping on a number.** *"I am `-105`, therefore I stop."* The countdown taught the exact behaviour it was meant to prevent. | § 3.0's **ratchet** — every pass owns its SUCCESSOR'S preconditions; Jason rules only on a **twice-stalled** gate, never on a session number. |
| L11 | **A session re-voicing the papers.** "Harmonising" spends Jason's hours for him and usually loses something. | **C-f is flagged, never fixed.** The structural/voice line is drawn in § 2.5 and restated in § 4.1. |"""
    t = t.replace(LAST, L910, 1)
    # the stamp section learns about the amendment
    t = t.replace("* **Ruled by:** Jason, 2026-08-24, in session `wealthTensor-102`.",
                  "* **Ruled by:** Jason, 2026-08-24, in session `wealthTensor-102`.\n"
                  "* **AMENDED the same day, same session, by Jason:** § 2.5 (the coherence class), "
                  "§ 3.0 (the ratchet, replacing the `-106` hard stop), § 3's fourth pass, § 4's "
                  "restated end product and `FIGURE-PLAN.md`, and loopholes L9–L11. **The amendment "
                  "RAISED the bar** — correct is no longer sufficient; structurally final is the bar.", 1)
    D.write_text(t)
t = D.read_text()

# ---- post-conditions ----
chk("D1 the coherence class exists", "## 2.5 · THE COHERENCE CLASS" in t)
chk("D2 all seven C-types are named", all(("**C-%s ·" % c) in t for c in "abcdefg"))
chk("D3 the ratchet replaces the countdown", "## 3.0 · THE RATCHET" in t)
chk("D4 NEGATIVE: no session may stop on its own number",
    "NO SESSION MAY STOP BECAUSE ITS NUMBER CAME UP" in t, True)
chk("D5 NEGATIVE: the old automatic hard stop is GONE",
    "### 3.4 · THE HARD STOP" not in t and "the work stops and Jason rules**\non shipping" not in t, True)
chk("D6 Jason rules only on a TWICE-stalled precondition",
    "TWICE ON THE\nSAME PRECONDITION" in t or "TWICE ON THE SAME PRECONDITION" in t)
chk("D7 there are four named passes", all(("### PASS %s —" % p) in t for p in "ABCD"))
chk("D8 every pass declares its successor's precondition", t.count("SUCCESSOR PRECONDITION") >= 4)
chk("D9 Pass A inventories the C-class without repairing it",
    "INVENTORY THE C-CLASS — count, do not repair" in t)
chk("D10 NEGATIVE: Pass A still may not repair", "may not repair anything" in t, True)
chk("D11 structure settles in Pass C, before the 30,000-foot read",
    "SETTLE THE STRUCTURE" in t and "still moving" in t)
chk("D12 the end product is defined as Jason's rewrite input",
    "IT IS A MANUSCRIPT JASON CAN REWRITE FROM" in t)
chk("D13 that bar is stated as a FAILABLE test",
    "STATED SO IT CAN BE FAILED" in t and "never discovers that a paragraph" in t)
chk("D14 FIGURE-PLAN.md is specified with its columns",
    "FIGURE-PLAN.md` — THE ARTEFACT" in t and "**chart candidate**" in t)
chk("D15 the measured zero-figures fact is recorded, not asserted vaguely",
    "ZERO figure captions" in t and "230 markdown" in t)
chk("D16 NEGATIVE: a session may propose chart forms but not build them",
    "must NOT build them" in t, True)
chk("D17 NEGATIVE: register drift is flagged, never fixed by a session",
    "FLAG C-f (register drift); do not fix it" in t and "Flagging is the repair" in t, True)
chk("D18 loopholes L9, L10 and L11 are named", all(("| L%d |" % i) in t for i in (9, 10, 11)))
chk("D19 NEGATIVE: the original eight loopholes survive the edit",
    all(("| L%d |" % i) in t for i in range(1, 9)), True)
chk("D20 NEGATIVE: the charter still wins over this document",
    "CO-AUTHOR-CHARTER.md` still wins over this file" in t, True)
chk("D21 NEGATIVE: the freeze section was not disturbed",
    "## 1 · THE FREEZE" in t and "THE INSTRUMENT SET IS FROZEN" in t, True)
chk("D22 NEGATIVE: the S1/S2/S3 truth rubric was not disturbed",
    all(s in t for s in ("### S1 ·", "### S2 ·", "### S3 ·", "Ambiguity resolves UPWARD, once")), True)
chk("D23 the amendment is disclosed in the stamp", "AMENDED the same day" in t)
chk("D24 NEGATIVE: the document still opens by naming itself the SSOT",
    "It is the SSOT for what \"done\" means on this corpus" in t, True)
chk("D25 NEGATIVE: the file grew (the amendment raised the bar, it did not trade one rule for another)",
    len(t) > len(orig) or "## 2.5 · THE COHERENCE CLASS" in orig, True)

print("\n post-conditions: %d checks, %d NEGATIVE" % (25, NEG))
if FAILED:
    print(" FAILURE"); [print("   FAILED:", f) for f in FAILED]; sys.exit(1)
print(" ALL PASS")
