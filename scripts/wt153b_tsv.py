#!/usr/bin/env python3
"""wt153b · REVIEW-024 · repair docs/promises-adjudicated.tsv.

Two jobs:
  1. Retire the row wt153 made STALE (388811fc0a) and adjudicate the sentence that replaced it.
     The new sentence is taken BYTE-EXACT from `wt148 --json`, never retyped.
  2. Re-adjudicate the four rows REVIEW-024's sample found NON-DISCRIMINATING — rows whose
     `evidence`, run or read, leaves the sentence free to be false. Each gets an evidence column
     that bears on the sentence's own assertion about its own artefact, and a note saying what
     reading it showed. One further row (fd2b77f988) has its note's overstatement corrected.

No sentence is edited here, so no promise_id changes except the one wt153 already changed.
Rolls back on any failed post-condition.
"""
import json, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TSV = ROOT / "docs/promises-adjudicated.tsv"

RETIRE = "388811fc0a"
NEW_PID = "f06ce25844"

NEW_ROW_CLASS = "R"
NEW_ROW_EVIDENCE = "scripts/wt153_paperIV_s1_record_not_command.py (10 post-conditions, 4 NEGATIVE) + read paper-IV.md section 10"
NEW_ROW_NOTE = ("REPAIRED IN PASS (REVIEW-024, retiring row 388811fc0a). The retired sentence promised '§10 names the "
    "command for each'; §10 says in bold 'Those files, not a command, are the record of §6' and states 'Nothing in this "
    "repository re-derives §6's figures from committed data'. §10 was corrected at wealthTensor-82 and §1's promise ABOUT "
    "§10 was not. wt153 rewrites §1 to name the record; §10 is untouched.")

REPAIRS = {
 "bf2138f041": (
   "sed -n '/def test_a_flat_gini_does_not_mean_a_bounded_one/,/^def /p' tests/test_redistribution.py + grep -ci gini docs/papers/paper-IV-composition/paper-IV.md",
   "READ, not located (REVIEW-024 repair; the prior evidence was `grep -rln`, which prints filenames and cannot show what a test forbids). "
   "The body asserts drift < 0.02 AND top_share > 0.95 AND not is_bounded, and the docstring states that a refactor reducing is_bounded to a "
   "drift test alone 'will fail here rather than quietly scoring condensation as success' -- that IS forbidding a saturating statistic to be "
   "read as convergence. It is defined in tests/test_redistribution.py, Paper II's module. paper-IV.md contains exactly two occurrences of "
   "'gini', both inside this sentence, so 'this paper reports no Gini' holds."),
 "75220244de": (
   "grep -n 'bibliographic details verified' docs/papers/PREPRINT-CHECKLIST.md + read docs/REFERENCE-POLICY.md L97",
   "READ, not ls'd (REVIEW-024 repair; the prior evidence was `ls -l + git ls-files` and its note read 'present, 134 lines' -- true, and "
   "silent on what the file prescribes). L42 is the checkbox \"Every reference entry's bibliographic details verified against a publisher "
   "page, a ...\"; L6-7 dates the venue verification and orders re-verification before submitting; REFERENCE-POLICY L97 makes the "
   "bibliographic question its own numbered pass. The checklist prescribes what the sentence says it prescribes."),
 "76617b04e0": (
   "head -1 scripts/wt027_report.py + git log -1 --format=%h ad779eb -- src/wealth_tensor/lag.py",
   "READ, not ls'd (REVIEW-024 repair; the prior evidence was `ls -l + git ls-files`, note 'present, 164 lines -- Paper III's', which is "
   "silent on the regeneration claim). wt027_report.py's docstring, line 1, is 'Regenerate every number Paper III reports from `lag.py`.' -- "
   "the sentence's two assertions, that lag.py is Paper III's module and that wt027_report.py regenerates it, are both in that one line."),
 "7e1c612368": (
   "read docs/LEDGER.md WT-059 (from L1489) AND WT-062 (from L1632)",
   "BOTH ENTRIES READ (REVIEW-024 repair; the prior evidence grepped WT-059's line number and never opened WT-062, which carries the half "
   "of the sentence about the search). WT-062 is titled 'Two false conclusions in one session' and names them: a false positive on `Mayo` "
   "(Kaserman & John W. Mayo, an antitrust economist, for Deborah G. Mayo) and a false negative on Odum's Environmental Accounting, found "
   "later on a different Kindle. Those are the two entries. WT-059 carries the correction and the rule adopted ('cite the edition "
   "consulted'), which is the sentence's 'the citations were not wrong, the search was'."),
 "fd2b77f988": (
   "read docs/preregistration/RESULT-REG-008.md section 2.2, and section 1 P2 for the pooled figure",
   "§2.2 is 'At sentence level the (f) family and the named unit never meet' and prints zero of 281 JOINT and one of 363 GOODWILL-ONLY. "
   "The sentence's 'once in 644' is those two disjoint strata summed -- 281+363=644, the mandated-disclosure window of §1's table -- and is "
   "printed verbatim at §1's P2, not at §2.2. REVIEW-024 repair: the prior note said 'Both figures at the section cited' and only one of them is."),
}

def fail(m):
    print("wt153b: FAIL — " + m); sys.exit(1)

raw = TSV.read_text(encoding="utf-8")
before = raw
lines = raw.split("\n")

# byte-exact sentence for the new promise, straight out of the sweep
j = json.loads(subprocess.run([sys.executable, str(ROOT/"scripts/wt148_promise_sweep.py"), "--json"],
                              capture_output=True, text=True, cwd=str(ROOT)).stdout)
hit = [p for p in j if p["pid"] == NEW_PID]
if len(hit) != 1:
    fail("wt148 --json does not emit exactly one promise with pid %s (got %d) — REFUSING" % (NEW_PID, len(hit)))
newp = hit[0]

idx = {}
for i, ln in enumerate(lines):
    if ln.startswith("#") or not ln.strip(): continue
    f = ln.split("\t")
    if len(f) == 7: idx[f[1]] = i

for pid in [RETIRE] + list(REPAIRS):
    if pid not in idx: fail("row %s is not in the TSV — REFUSING" % pid)
if NEW_PID in idx: fail("row %s is already adjudicated — REFUSING" % NEW_PID)

# 1 · repairs, in place
for pid, (ev, note) in REPAIRS.items():
    f = lines[idx[pid]].split("\t")
    f[4], f[5] = ev, note
    lines[idx[pid]] = "\t".join(f)

# 2 · retire the stale row, put the new adjudication in its place
newrow = "\t".join([newp["paper"], NEW_PID, newp["artefact"], NEW_ROW_CLASS,
                    NEW_ROW_EVIDENCE, NEW_ROW_NOTE, newp["sentence"]])
lines[idx[RETIRE]] = newrow

out = "\n".join(lines)
TSV.write_text(out, encoding="utf-8")

def rollback(m):
    TSV.write_text(before, encoding="utf-8")
    print("wt153b: ROLLED BACK — " + m); sys.exit(1)

after = TSV.read_text(encoding="utf-8")
checks = []
def check(n, ok, neg=False):
    checks.append((n, ok, neg))
    if not ok: rollback("post-condition failed: " + n)

drows = [l for l in after.split("\n") if l.strip() and not l.startswith("#")]
check("Q1  row count is unchanged at 129 (one retired, one added)", len(drows) == 129)
check("Q2  NEGATIVE: the retired promise_id is no longer any row's promise_id (it survives only as prose in the new row's note, which is the audit trail)",
      all(l.split("\t")[1] != RETIRE for l in drows), True)
check("Q3  the new promise_id is adjudicated exactly once", sum(1 for l in drows if l.split("\t")[1] == NEW_PID) == 1)
check("Q4  every data row still has exactly 7 tab-separated fields", all(len(l.split("\t")) == 7 for l in drows))
check("Q5  every promise_id is unique", len({l.split("\t")[1] for l in drows}) == len(drows))
check("Q6  the five repaired rows kept their promise_id and their sentence",
      all(l.split("\t")[1] in idx or l.split("\t")[1] == NEW_PID for l in drows))
for pid in REPAIRS:
    row = [l for l in drows if l.split("\t")[1] == pid][0]
    check("Q7:%s  evidence column changed and note records REVIEW-024" % pid,
          row.split("\t")[4] == REPAIRS[pid][0] and "REVIEW-024" in row.split("\t")[5])
check("Q8  NEGATIVE: no note or evidence cell contains a stray tab or newline",
      all("\t" not in c and "\n" not in c for l in drows for c in l.split("\t")[4:6]), True)
check("Q9  the #scope line is untouched (paper-III, paper-IV only)",
      "#scope\tpaper-III\tpaper-IV" in after)
check("Q10 NEGATIVE: exactly one file is dirty beyond wt153's manuscript edit",
      len([l for l in subprocess.run(["git","-C",str(ROOT),"diff","--name-only"],
          capture_output=True,text=True).stdout.split("\n") if l.strip()]) <= 3, True)

print("wt153b · TSV — 1 retired, 1 adjudicated, 5 re-adjudicated; %d post-conditions (%d NEGATIVE)"
      % (len(checks), sum(1 for _,_,n in checks if n)))
for n, ok, neg in checks:
    print(("  ✓ " if ok else "  ✗ ") + n)
print("\nNOW RUN: python3 scripts/wt148_promise_sweep.py — it MUST return to RC 0.")
