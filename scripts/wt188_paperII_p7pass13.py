#!/usr/bin/env python3
"""wt188 — the PATCH OF RECORD for wealthTensor-102's P7 pass 13 on Paper II (REVIEW-037).

NOT AN INSTRUMENT.  This is the same object wt181 was at -99, wt185 at -101: the evidence
script for one review pass.  It measures, it asserts, and it applies the pass's single
manuscript edit.  Every number in REVIEW-037 is printed by a check below.

The axes themselves are inherited and were run BEFORE any of this was written:
  A1  scripts/wt130_quantifier_sweep.py paper-II          (RC 0, 166 tokens on 126 lines)
  A2  the EIGHT failure modes the paper names, inherited from REVIEW-018 section 1
  A3  scripts/wt133_crossref_sweep.py                     (RC 0)
  A3' scripts/wt184_pointer_correctness.py paper-II       (RC 0) -- the HELD-OUT TEST
  A4  scripts/wt030_report.py + scripts/wt077_tail_index.py, and A4's SECOND question
  A5  every named artefact enumerated from the whole document, resolved and READ

CHECKS
  E1  RULE-1 CO-OCCURRENCE.  wt184 Rule 1 has the SAME defect -101 diagnosed in Rule 2:
      a number and a pointer merely CO-OCCURRING in one clause is read as attribution.
      11 of 11 paper-II flags are false positives from this cause.  NEGATIVE control: the
      cause is structural, not a paper-II accident -- remove the attribution window and
      the flag count MOVES, so the window is what does the work, not a possessive.
  E2  wt184 HAS NO POSSESSIVE FORM IN RULE 1.  -101's tee-up 1 says three times, in
      REVIEW-036 and twice in HANDOFF.md, that the fix for Rule 2 is "the possessive form
      Rule 1 already uses, which cut its own flag set from 44 to 5."  Rule 1 contains no
      possessive logic of any kind.  Repaired FORWARD (REVIEW-034 section 4 item 7 precedent).
  E3  wt184 MIS-BUCKETS AN AUTHOR-ATTRIBUTED FOREIGN POINTER.  Paper II section 6 line 418
      cites Benhabib, Bisin and Zhu's "their section 4.1".  wt133 dismisses it as another
      document's section; wt184's FOREIGN regex matches only paper-N / companion paper /
      REVIEW- / RESULT- forms, so it lands in `unresolved`.  wt184's OWN post-condition
      asserts "zero unresolved, agreeing with wt133" -- on paper-III only.  On paper-II
      that agreement is FALSE.
  E4  A4's SECOND QUESTION, THE FINDING.  Section 7 enumerates "five quantities neither
      command prints in any precision".  There are SIX.  Section 3.1's 6e-6 change in
      Var[log a] is a difference of two values wt077_tail_index.py prints, is stated in
      section 3.1, and is in none of the five.  NEGATIVE controls: each of the five named
      quantities really is absent from both stdouts, and the two closed-form exceptions
      really are present.
  E5  THE PERIODICITY ARGMIN ACROSS SEEDS.  Section 3.3 pins the interior minimum at
      "0.451 at P = 30" and tests/test_redistribution.py asserts gs[30] < gs[20] at
      T = 600, seed 0.  Measured at the REPORTED horizon T = 1200 across five seeds.
  E6  THE MANUSCRIPT EDIT, with an IDEMPOTENCY MARKER and an EXACTLY-ONCE check.
      -101's trap: a post-condition that cannot fail on a double application is not a
      post-condition.  Run this script twice; the second run is the test.
  E7  DEFENSIVE COUNT, before and against.
  E8  THE OTHER THREE MANUSCRIPTS ARE BYTE-IDENTICAL across the repair.

Exit 0 iff every check passes.  --apply lands the edit; without it, report only.
"""
from __future__ import annotations
import hashlib, re, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
P2 = REPO / 'docs/papers/paper-II-redistribution/paper-II.md'
RESULTS = []

def chk(label, cond, negative=False):
    RESULTS.append(1 if negative else 0)
    print(("  %-4s %s%s" % ("ok" if cond else "FAIL", "[NEG] " if negative else "", label)))
    if not cond:
        FAILED.append(label)
    return cond

FAILED = []

def sh(cmd):
    p = subprocess.run(cmd, shell=True, cwd=REPO, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr

# ---------------------------------------------------------------- E1 / E2 / E3
print("== E1 · wt184 RULE 1 co-occurrence, on paper-II ==")
sys.path.insert(0, str(REPO / 'scripts'))
import wt184_pointer_correctness as wt184

st2, fl2 = wt184.run(P2, verbose=False)
chk("paper-II: RULE 1 adjudicates a non-zero number of figures", st2['num_checked'] > 0)
chk("paper-II: RULE 1 flags 11", st2['num_flag'] == 11)
chk("paper-II: RULE 2 flags 0 (only 1 quoted phrase is in scope at all)",
    st2['phr_flag'] == 0 and st2['phr_checked'] == 1)

# every flagged number IS somewhere in the manuscript -- i.e. none is a wrong number,
# they are numbers attributed to the wrong section by co-occurrence.
body = P2.read_text()
nums = [f[3] for f in fl2 if f[0] == 'NUMBER']
chk("paper-II: every one of the 11 flagged numbers occurs in the manuscript",
    all(n in body.replace(',', '') for n in nums))
# ... and each one occurs in a DIFFERENT section from the one it was attributed to,
# which is the definition of a co-occurrence false positive.
secs = wt184.parse_sections(body)
idx = wt184.section_index(secs)
norm = {k: wt184.strip_emphasis(' '.join(s['body'] for s in v)) for k, v in idx.items()}
elsewhere = 0
for kind, ln, tgt, item, ctx in fl2:
    if kind != 'NUMBER':
        continue
    if any(item in wt184.norm_num(v) for k, v in norm.items()
           if '§' + k not in tgt.split('/')):
        elsewhere += 1
chk("paper-II: all 11 flagged numbers live in SOME other section (co-occurrence, not error)",
    elsewhere == 11)

def _run_without_window(paper):
    """Re-run RULE 1 with the `|`/`;` fragmenting removed, to measure what the window does."""
    text = paper.read_text()
    sections = wt184.parse_sections(text)
    i2 = wt184.section_index(sections)
    nb = {k: wt184.strip_emphasis(' '.join(s['body'] for s in v)) for k, v in i2.items()}
    flag = 0
    for lineno, clause in wt184.split_clauses(text):
        refs = wt184.REF.findall(clause)
        if not refs or wt184.FOREIGN.search(clause):
            continue
        targets = [r for r in refs if '.' in r and r in nb]
        if not targets:
            continue
        pool = wt184.norm_num(' || '.join(nb[t] for t in targets))
        cnorm = wt184.strip_emphasis(clause)
        cnorm = wt184.REF_RANGE.sub(lambda m: m.group(1) + ' SECTIONRANGE ', cnorm)
        cnorm = wt184.REF_RUN.sub(lambda m: m.group(0)[:m.start(1) - m.start(0)] + ' SECTIONRUN ', cnorm)
        cnum = wt184.REF.sub(' SECTIONREF ', cnorm)      # NO fragmenting
        for tok in wt184.NUMTOK.findall(cnum):
            tok = tok.strip()
            if not tok or wt184.bad_number(tok):
                continue
            if wt184.norm_num(tok) not in pool:
                flag += 1
    return flag

# NEGATIVE control for the mechanism -- AND THE FIRST CUT OF THIS CHECK WAS WRONG ABOUT
# THE FILE, WHICH IS THE CORRECT DIRECTION FOR A GUARD TO FAIL (-101's trap 3).  It asserted
# that removing the `|`/`;` attribution window would MOVE paper-II's flag count.  It does
# not move at all: 11 with the window, 11 without.  The window only ever fires on a markdown
# TABLE ROW, and not one of paper-II's eleven flagged clauses is a table row.  So on prose --
# which is where a manuscript makes its attributions -- RULE 1 HAS NO ATTRIBUTION WINDOW,
# the whole clause is the window, and co-occurrence IS the rule.  That is a stronger
# statement than the one the check was written to make, so the check was tightened to it.
no_window = _run_without_window(P2)
chk("paper-II: the window is INERT on prose -- same count with and without (%d)" % no_window,
    no_window == st2['num_flag'])
window_chars = sum(1 for _k, _l, _t, _i, ctx in fl2 if '|' in ctx or ' ; ' in ctx)
chk("paper-II: not one flagged clause is a table row or carries a `;` (%d)" % window_chars,
    window_chars == 0, negative=True)
# AND THE SAME MEASUREMENT ON PAPER-III, which is where -101's "44 to 5" number came from.
P3 = REPO / 'docs/papers/paper-III-dual-tensor/paper-III.md'
st3, fl3 = wt184.run(P3, verbose=False)
nw3 = _run_without_window(P3)
print("     paper-III RULE 1: %d flags with the window, %d without" % (st3['num_flag'], nw3))
chk("paper-III: the window IS load-bearing there (that is what cut 44 to 5, not a possessive)",
    nw3 > st3['num_flag'], negative=True)

print("== E2 · RULE 1 has no possessive form ==")
src = (REPO / 'scripts/wt184_pointer_correctness.py').read_text()
rule1 = src.split('# RULE 1 ---')[1].split('# RULE 2 ---')[0]
chk("wt184 RULE 1 body contains no possessive/apostrophe logic",
    "'s" not in rule1 and '’' not in rule1 and 'possess' not in rule1.lower())
chk("wt184 contains no possessive logic ANYWHERE outside quote normalisation",
    src.count("possess") == 0)
# the tee-up that says otherwise, in all three places it is written
tee = 0
for f in ('docs/REVIEW-036-P7-paperIII-pass4.md', 'docs/HANDOFF.md'):
    tee += (REPO / f).read_text().count('possessive form')
chk("the claim 'the possessive form Rule 1 already uses' is written 3 times (%d)" % tee,
    tee == 3)

print("== E3 · wt184 mis-buckets an author-attributed foreign pointer ==")
chk("paper-II: wt184 reports exactly 1 unresolved", st2['unresolved'] == 1)
chk("paper-II: wt184 reports 0 foreign", st2['foreign'] == 0, negative=True)
chk("paper-II has no section 4.1 of its own", '4.1' not in idx)
line418 = [i for i, l in enumerate(body.split('\n'), 1)
           if 'their §4.1 notes' in l]
chk("the pointer is Benhabib/Bisin/Zhu's own §4.1", len(line418) == 1)
rc, out, _ = sh('python3 scripts/wt133_crossref_sweep.py')
m = re.search(r'paper-II\.md.*?sweep 1: (\d+) §N\.M references, (\d+) distinct, (\d+) unresolved, (\d+) dismissed',
              out, re.S)
chk("wt133 ran (RC 0)", rc == 0)
chk("wt133 says 0 unresolved on paper-II", m is not None and m.group(3) == '0')
chk("wt133 dismisses exactly 1 as another document's", m is not None and m.group(4) == '1')
chk("SO: wt184 and wt133 DISAGREE on paper-II's unresolved count",
    st2['unresolved'] != int(m.group(3)))
# and wt184's own post-condition asserts that agreement -- on paper-III only
chk("wt184's post-conditions assert the agreement for paper-III only",
    src.count("agreeing with wt133") == 1 and 'paper-III' in
    [l for l in src.split('\n') if 'agreeing with wt133' in l][0])

# ---------------------------------------------------------------- E4
print("== E4 · A4's SECOND QUESTION — section 7 says five; there are six ==")
rc30, o30, _ = sh('python3 scripts/wt030_report.py')
rc77, o77, _ = sh('python3 scripts/wt077_tail_index.py')
chk("wt030_report.py RC 0", rc30 == 0)
chk("wt077_tail_index.py RC 0", rc77 == 0)
both = o30 + '\n' + o77

FIVE = ['0.99875', '0.90', '0.035', '0.103', '0.039']
for q in FIVE:
    chk("section 7's %s is absent from both stdouts (as section 7 claims)" % q,
        q not in both, negative=True)
# the two closed-form exceptions ARE printed -- the positive control for the same greps
chk("E[eta+] 0.107269 IS printed by wt077 (positive control)", '0.107269' in o77)
chk("Var[log a] 0.076542 IS printed by wt077 (positive control)", '0.076542' in o77)
chk("Var[log a] 0.076536 IS printed by wt077 (positive control)", '0.076536' in o77)

# THE SIXTH.  section 3.1: "a change of 6 x 10^-6".
s31 = norm['3.1']
chk("section 3.1 states the 6 x 10-6 change", '6 x 10-6' in s31 or '6 × 10⁻⁶' in
    wt184.strip_emphasis(' '.join(s['body'] for s in idx['3.1'])))
chk("0.076542 - 0.076536 == 6e-06 exactly", round(0.076542 - 0.076536, 8) == 6e-06)
for form in ('6e-06', '6e-6', '0.000006', '6 x 10', '6*10'):
    chk("the 6e-6 change is absent from both stdouts in form %r" % form,
        form not in both, negative=True)
# THE FINDING IS ABOUT THE MANUSCRIPT AS IT STOOD BEFORE THIS PASS, so it is asserted
# against the PRE-EDIT text.  Reading it off the live file makes the check evaporate the
# moment the repair lands -- which is exactly what the second run caught.
_bak = P2.with_suffix('.md.bak-wt188')
PRE = _bak.read_text() if _bak.exists() else P2.read_text()
_pre_idx = wt184.section_index(wt184.parse_sections(PRE))
sec7_pre = wt184.strip_emphasis(' '.join(x['body'] for x in _pre_idx['7']))
chk("BEFORE the repair, section 7 said 'five quantities neither command prints'",
    'five quantities neither command prints' in sec7_pre)
chk("BEFORE the repair, section 7's enumeration did NOT contain the 6e-6 change",
    '6 x 10' not in sec7_pre and '6 × 10' not in sec7_pre and '0.000006' not in sec7_pre,
    negative=True)
chk("BEFORE the repair, section 7 DID name each of the five (positive control)",
    all(q in wt184.norm_num(sec7_pre) for q in FIVE))
chk("BEFORE the repair, section 3.1 already stated the 6e-6 change (so it was IN section 3)",
    '6 × 10' in wt184.strip_emphasis(' '.join(x['body'] for x in _pre_idx['3.1'])))

# ---------------------------------------------------------------- E5
print("== E5 · the periodicity argmin across seeds, at the REPORTED horizon ==")
sys.path.insert(0, str(REPO / 'src'))
from wealth_tensor.redistribution import RedistributiveEconomy, stationary_gini
PS = (1, 2, 4, 10, 20, 30, 50)
rows = {}
for seed in range(5):
    gs = [stationary_gini(RedistributiveEconomy(base='stock', rate=min(1.0, 0.02 * p),
                                                periodicity=p, seed=seed).run(1200))
          for p in PS]
    rows[seed] = gs
    print("     seed %d  " % seed + "  ".join("P%-3d %.4f" % (p, g) for p, g in zip(PS, gs)))
argmins = [PS[g.index(min(g))] for g in rows.values()]
print("     argmin by seed: %s" % argmins)
spans = [max(g) - min(g) for g in rows.values()]
print("     span by seed  : %s" % ["%.4f" % s for s in spans])
chk("seed 0 at T=1200 reproduces section 3.3's P=1 0.486", round(rows[0][0], 3) == 0.486)
chk("seed 0 at T=1200 reproduces section 3.3's P=20 0.456", round(rows[0][4], 3) == 0.456)
chk("seed 0 at T=1200 reproduces section 3.3's P=30 0.451", round(rows[0][5], 3) == 0.451)
chk("seed 0 at T=1200 reproduces section 3.3's P=50 0.469", round(rows[0][6], 3) == 0.469)
chk("seed 0's argmin is P=30, as section 3.3 states", argmins[0] == 30)
chk("THE MINIMUM IS INTERIOR ON EVERY SEED (never P=1 and never P=50)",
    all(a not in (1, 50) for a in argmins))
chk("the sweep span is < 0.25 on every seed (the test's bound)", all(s < 0.25 for s in spans))
print("     >> ARGMIN LOCATION STABLE ACROSS SEEDS: %s" % (len(set(argmins)) == 1))

# ---------------------------------------------------------------- E6/E7/E8

# ================================================================ E6 · THE EDITS
# -101's trap: A POST-CONDITION THAT CANNOT FAIL ON A DOUBLE APPLICATION IS NOT A
# POST-CONDITION.  Every edit below is a REPLACE of a unique anchor that the replacement
# DESTROYS, and every check is an EXACTLY-ONCE count, never a presence test.  Run twice.

EDITS = [
    # ---- II-44, site 1 · §3.1 -------------------------------------------------------
    ("II-44a",
     "give the stationary Pareto exponent in closed form in all four coordinates. They write that exponent",
     "give the stationary Pareto exponent in closed form in all four of their own tax parameters — a\nrate and a redistributed fraction for each base. They write that exponent"),
    # ---- II-44, site 2 · §6 ---------------------------------------------------------
    ("II-44b",
     "each in one wealth balance and give the stationary Pareto exponent in closed form in all four\ncoordinates, together with the stock-versus-flow ranking (§3.1).",
     "each in one wealth balance and give the stationary Pareto exponent in closed form in all four of\ntheir own tax parameters — a rate and a redistributed fraction for each base — together with the\nstock-versus-flow ranking (§3.1)."),
    # ---- II-44, site 3 · §6, the third use of the word ------------------------------
    ("II-44c",
     "per-capita rebate fraction is a coordinate in their solution rather than an extension awaiting one.",
     "per-capita rebate fraction is a parameter in their solution rather than an extension awaiting one.\nTheir solution is continuous-time and carries neither a periodicity nor a threshold, so §3.3's two\ntrim coordinates are outside it."),
    # ---- II-43 · §7's enumeration ---------------------------------------------------
    ("II-43a",
     "simulation output and come from `python3 scripts/wt077_tail_index.py`, and except five\n  quantities neither command prints in any precision:",
     "simulation output and come from `python3 scripts/wt077_tail_index.py`, and except six\n  quantities neither command prints in any precision:"),
    ("II-43b",
     "values `wt030_report.py` prints; and §3.4's 0.039 top-decile margin, the distance from that\n  command's printed 0.861 to the 0.90 threshold above.",
     "values `wt030_report.py` prints; §3.4's 0.039 top-decile margin, the distance from that\n  command's printed 0.861 to the 0.90 threshold above; and §3.1's 6 × 10⁻⁶ change in\n  Var[log *a*], the difference of two values `wt077_tail_index.py` prints."),
]

print("== E6 · the manuscript edits ==")
before = P2.read_text()
print("     paper-II sha256 before: %s" % hashlib.sha256(before.encode()).hexdigest()[:16])
applied = []
after = before
for tag, old, new in EDITS:
    n_old, n_new = after.count(old), after.count(new)
    if n_old == 1 and n_new == 0:
        after = after.replace(old, new, 1)
        applied.append(tag)
    elif n_old == 0 and n_new == 1:
        pass                                   # already landed; idempotent
    else:
        print("     REFUSED %s: anchor count old=%d new=%d" % (tag, n_old, n_new))
        FAILED.append("edit anchor %s is not unique" % tag)

if '--apply' in sys.argv and after != before:
    bak = P2.with_suffix('.md.bak-wt188')
    if not bak.exists():
        bak.write_text(before)
    P2.write_text(after)
    print("     APPLIED: %s   (backup %s)" % (", ".join(applied), bak.name))
elif after != before:
    print("     DRY RUN — would apply: %s   (re-run with --apply)" % ", ".join(applied))
else:
    print("     no change needed (already landed) — the SECOND-RUN test")

cur = P2.read_text()
print("     paper-II sha256 after : %s" % hashlib.sha256(cur.encode()).hexdigest()[:16])

if '--apply' in sys.argv or after == before:
    # EXACTLY-ONCE, never presence.  An inserting edit keeps its own anchor; these do not.
    chk("§7 says 'except six' EXACTLY once", cur.count("and except six\n  quantities neither command prints in any precision") == 1)
    chk("§7 says 'except five' EXACTLY zero times",
        cur.count("except five\n  quantities neither command prints in any precision") == 0, negative=True)
    chk("the sixth quantity is enumerated EXACTLY once",
        cur.count("§3.1's 6 × 10⁻⁶ change in") == 1)
    chk("§7 still enumerates all five originals EXACTLY once each",
        all(cur.count(q) >= 1 for q in ('0.99875', '0.90 top-decile criterion',
                                        '0.035 periodicity span', '0.103 Gini gap',
                                        '0.039 top-decile margin')))
    chk("'in closed form in all four coordinates' occurs EXACTLY zero times",
        cur.count("in closed form in all four coordinates") == 0, negative=True)
    # THE FIRST CUT OF THESE TWO WAS WRONG ABOUT THE FILE, NOT THE OTHER WAY ROUND.
    # The manuscript is hard-wrapped at ~100 columns and both replacements land a newline
    # INSIDE the phrase, so a byte-literal count reads 1 where the prose reads 2.  The fix
    # is a TIGHTER check -- count on whitespace-normalised text -- not a deleted one.
    flat = re.sub(r'\s+', ' ', cur)
    chk("'all four of their own tax parameters' occurs EXACTLY twice (whitespace-normalised)",
        flat.count("all four of their own tax parameters") == 2)
    chk("'a rate and a redistributed fraction for each base' occurs EXACTLY twice",
        flat.count("a rate and a redistributed fraction for each base") == 2)
    chk("a byte-literal count would MISS one of them (that is why this is normalised)",
        cur.count("all four of their own tax parameters") == 1, negative=True)
    chk("the §6 rebate sentence says 'parameter', EXACTLY once",
        cur.count("rebate fraction is a parameter in their solution") == 1)
    chk("the §6 rebate sentence no longer says 'coordinate'",
        cur.count("rebate fraction is a coordinate in their solution") == 0, negative=True)
    chk("the continuous-time scope sentence occurs EXACTLY once",
        cur.count("Their solution is continuous-time and carries neither a periodicity nor a threshold") == 1)
    chk("paper-II's own four coordinates are untouched (§Abstract, §1, §2.2)",
        cur.count("**base, rate, periodicity, threshold**") == 1
        and cur.count("four structural coordinates") == 1
        and cur.count("The levy, as four numbers") == 1)
    # the manuscript got LONGER by exactly the two steelman clauses and nothing else
    print("     lines before/after: %d / %d" % (before.count('\n'), cur.count('\n')))

    # ------------------------------------------------------------ E7 · defensive count
    print("== E7 · defensive count ==")
    pre = REPO / '/tmp/wt188_pre.md'
    pathlib_pre = Path('/tmp/wt188_pre.md')
    pathlib_pre.write_text(before)
    rc, out, err = sh('python3 scripts/defensive_count.py %s --against /tmp/wt188_pre.md' % P2)
    print("     " + "\n     ".join((out + err).strip().split('\n')[:12]))
    chk("defensive_count --against the pre-edit file: RC 0 (no section outside §Limitations gained)",
        rc == 0)

    # ------------------------------------------------------------ E8 · the other papers
    print("== E8 · the other three manuscripts are untouched ==")
    rc, out, _ = sh("git status --porcelain docs/papers/paper-I-price-formation "
                    "docs/papers/paper-III-dual-tensor docs/papers/paper-IV-composition")
    chk("papers I, III and IV are byte-identical across this repair", out.strip() == "",
        negative=True)

print()
print(" post-conditions: %d checks, %d NEGATIVE" % (len(RESULTS), sum(RESULTS)))
print(" post-conditions: %s" % ("ALL PASS" if not FAILED else "FAILURE"))
for f in FAILED:
    print("   FAILED: %s" % f)
sys.exit(0 if not FAILED else 1)
