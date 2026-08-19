#!/usr/bin/env python3
"""wt172 - adjudicate the FIVE promises wt171's repair minted, and retire the THREE it killed.

WHY A SECOND SCRIPT AND WHY IN THE SAME SESSION
-----------------------------------------------
`wt171` repaired six sentences in Paper II. Three of the fifteen adjudicated promises were keyed
on sentences it touched, so `promise_id` re-keyed and `wt148` went red the moment `wt171` landed:
three rows STALE, five unadjudicated. `wealthTensor-87` lesson (iii), now confirmed a fifth time:
the repair and the adjudication of the promises it emits belong in the SAME session, because a
manuscript left with re-keyed promises is a manuscript nobody can gate.

The two scripts are separate and committed separately so the ORDER is a git fact: the repaired
manuscript is an object at `76355d6` before any evidence about it exists.

    retired  dfd41f5263  the abstract bullet's exception clause was narrowed (R4)
             c9a565b3fe  section 7's exception clause was narrowed (R5) - THE CLASS C ROW
             1cbe31f16c  same sentence as c9a565b3fe, keyed on the other command
    minted   6914c59765  the abstract bullet, re-keyed
             7b6a20118e  R2's new target: test_the_levy_is_a_pure_transfer
             bc1f66a253  R2's other artefact: the file that test lives in
             b9dea67210  section 7, re-keyed - and the C is DISCHARGED here
             5f6d5c4fb9  section 7, keyed on wt077_tail_index.py

THE SUPERSESSION LEDGER, AND WHY A DELETED ADJUDICATION NEEDED ONE
------------------------------------------------------------------
`wt170 --verify` re-runs the fifteen evidence cells it wrote, and it REFUSES if one of its fifteen
is not in the TSV. That refusal is correct - an adjudication must not be able to vanish - but as
written it also makes the file un-repairable: any repair of an adjudicated sentence deletes a row
and turns a green guard red, which is a standing incentive not to repair. So this pass adds three
`#superseded` lines to the TSV (comments, invisible to every sweep) and teaches `wt170 --verify`
one rule: a missing pid is forgiven ONLY if a `#superseded` line names a successor AND that
successor is itself an adjudicated row. F9 below fabricates a supersession pointing at a pid that
does not exist and proves `wt170 --verify` still fails on it, so the ledger is a redirection and
not a bypass.

WHAT `--verify` DOES HERE, AND WHY IT IS WIDER THAN wt170's
------------------------------------------------------------
`wt170 --verify` is pinned to a fixed fifteen written into its source. `wt172 --verify` reads
EVERY `paper-II` row out of the committed TSV, re-runs its evidence cell and holds the stdout to
its note line for line. It is therefore not a list that has to be maintained: the next repair that
adds a Paper II row is covered by it the day it lands.

EXIT: 0 = five rows written, three retired, every post-condition holds - 2 = refused, or a
post-condition failed and the TSV was restored to its pre-run bytes.

USAGE
    python3 scripts/wt172_tsv.py            # one-shot: retire three, mint five
    python3 scripts/wt172_tsv.py --verify   # re-run EVERY committed paper-II evidence cell
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TSV = "docs/promises-adjudicated.tsv"
TAG = "wt172"
PII = "docs/papers/paper-II-redistribution/paper-II.md"

# The commit carrying wt171's repair. Paper II's prose must be byte-identical to it: this
# script adjudicates a fixed emitted set and refuses to chase a moving manuscript.
REPAIR_COMMIT = "76355d6"

RETIRED = ["dfd41f5263", "c9a565b3fe", "1cbe31f16c"]
PIDS = ["6914c59765", "7b6a20118e", "bc1f66a253", "b9dea67210", "5f6d5c4fb9"]

SUPERSEDES = {
    "dfd41f5263": ("6914c59765",
                   "wt171 R4 narrowed the abstract bullet's exception clause; same artefact, "
                   "same evidence, new promise_id"),
    "c9a565b3fe": ("b9dea67210",
                   "wt171 R5 narrowed section 7's exception clause; the class C defect this row "
                   "carried is discharged at the successor"),
    "1cbe31f16c": ("5f6d5c4fb9",
                   "same sentence as c9a565b3fe, keyed on wt077_tail_index.py; the claim about "
                   "THIS artefact never changed"),
}

CLS = {p: "H" for p in PIDS}

# The row whose SENTENCE never moved and whose EVIDENCE did. See wt170's verify()
# docstring and F15 below.
REEVIDENCED = {
    "5a47d4caef": (
        'python3 -c "import subprocess;f=lambda p: len([l for l in subprocess.run([\'python3\',\'-m\',\'pytest\',p,\'-q\',\'--collect-only\'],capture_output=True,text=True).stdout.split(chr(10)) if \'::\' in l]);print(\'whole repository:\', f(\'tests/\'));print(\'tests/test_redistribution.py:\', f(\'tests/test_redistribution.py\'));L=open(\'docs/papers/paper-II-redistribution/paper-II.md\').read().split(chr(10));sec=lambda i: [l for l in L[:i] if l.startswith(\'## \')][-1][3:];print(\'18 quoted in sections:\', sorted({sec(i) for i,l in enumerate(L,1) if \'18 tests\' in l or \'**18** tests\' in l}))"',
        'prints \'whole repository: 1095\', \'tests/test_redistribution.py: 18\' and "18 quoted in sections: [\'1 · Introduction\', \'7 · Data and code availability\', \'Abstract\']". pytest\'s OWN collector is what counts here, not a grep for \'def test_\', so \'python3 -m pytest tests/ -q runs the whole repository\' is measured at 1095 collected tests and the paper-scoped count at 18. The third line settles the sentence\'s last clause -- \'that count is the one quoted in the abstract and in section 1\' -- and it now settles it by NAMING the sections rather than by printing line numbers and arguing about ranges in prose. RE-EVIDENCED BY wt172, AND WHY: the retired form of this cell printed \'18 quoted at lines: [38, 90, 459]\', and wt171\'s repair added four lines above 459 and turned it into 463. The sentence was never edited, so promise_id held and this row did not re-key -- but the evidence broke anyway. A positional evidence command is invalidated by any edit above it, including one that changes nothing the row asserts, and it fails LOUDLY (wt170 --verify caught it, which is the whole argument for --verify) rather than silently. The replacement reads the section headings and is stable under reflow.',
        "wt171 added four lines above L459, so the retired cell's positional third line ('18 quoted at lines: [38, 90, 459]') became [38, 90, 463]; the sentence was never edited, so the row did not re-key. Replaced with a section-name check, stable under reflow."),
}

EV = {

"6914c59765":
 "python3 -c \"import re;src=open('tests/test_redistribution.py').read();"
 "ns=re.findall(r'^def (test_\\w+)',src,re.M);print('tests:',len(ns));"
 "print('overclaim guard present:','test_a_flat_gini_does_not_mean_a_bounded_one' in ns)\"",

"7b6a20118e":
 "python3 -c \"import re;src=open('tests/test_redistribution.py').read();"
 "m=re.search(r'^def test_the_levy_is_a_pure_transfer\\(.*?(?=^def |\\Z)',src,re.M|re.S).group(0);"
 "print('asserts:',[l.strip() for l in m.split(chr(10)) if l.strip().startswith('assert')]);"
 "print('settings swept:',re.findall(r'\\(\\\"\\w+\\\", [0-9.]+, [0-9.]+\\)',m));"
 "print('implementation reports transfer_error:',"
 "'transfer_error' in open('src/wealth_tensor/redistribution.py').read())\"",

"bc1f66a253":
 "python3 -c \"import re,subprocess;src=open('tests/test_redistribution.py').read();"
 "print('defined in this file:',bool(re.search(r'^def test_the_levy_is_a_pure_transfer\\(',src,re.M)));"
 "r=subprocess.run(['python3','-m','pytest',"
 "'tests/test_redistribution.py::test_the_levy_is_a_pure_transfer','-q'],"
 "capture_output=True,text=True);"
 "print('pytest:',[l.split(' in ')[0] for l in r.stdout.split(chr(10)) "
 "if 'passed' in l or 'failed' in l])\"",

"b9dea67210":
 "python3 -c \"import re,subprocess;"
 "L=open('docs/papers/paper-II-redistribution/paper-II.md').read().split(chr(10));"
 "a=next(i for i,l in enumerate(L) if l.startswith('## 3 '));"
 "b=next(i for i,l in enumerate(L) if i>a and l.startswith('## '));"
 "o=''.join(subprocess.check_output(['python3','scripts/'+c],text=True) "
 "for c in ('wt030_report.py','wt077_tail_index.py'));"
 "n=set();[n.add(m.group(1)) for i in range(a,b) if not L[i].startswith('#') "
 "for m in re.finditer(r'(\\d+[.]\\d+)',L[i]) if L[i][max(0,m.start()-1)] != chr(167)];"
 "res=sorted(x for x in n if x not in o);"
 "c7=next(i for i,l in enumerate(L) if l.startswith('## 7 '));"
 "cl=' '.join(L[c7:]).split('The two commands are named')[0];"
 "rnd=lambda x: sorted({p for p in re.findall(r'\\d+[.]\\d+',o) "
 "if round(float(p),len(x.split(chr(46))[1]))==float(x)});"
 "print('printed by neither command:',res);"
 "inbullet=lambda x: bool(re.search(r'(?<![0-9.])'+re.escape(x)+r'(?![0-9])',cl));"
 "print('named as an exception in the section 7 bullet:',[x for x in res if inbullet(x)]);"
 "print('not named, and what it rounds from:',{x:rnd(x) for x in res if not inbullet(x)});"
 "print('unaccounted:',[x for x in res if not inbullet(x) and not rnd(x)])\"",

"5f6d5c4fb9":
 "python3 -c \"import subprocess;"
 "o=subprocess.check_output(['python3','scripts/wt077_tail_index.py'],text=True).split(chr(10));"
 "print([l.strip() for l in o if 'closed form' in l]);"
 "print([l.strip() for l in o if 'Var[log a] =' in l])\"",
}


# --------------------------------------------------------------------------------------
# The notes. Every non-empty line of every command's stdout appears here VERBATIM (F5).
# wealthTensor-91 lesson (iii): five of that pass's own fifteen notes quoted the first
# line and paraphrased the rest, every one of them was TRUE, and none was diffable. The
# author cannot catch this by re-reading, so it is asserted instead of intended.
# --------------------------------------------------------------------------------------
NOTE = {

"6914c59765": """prints 'tests: 18' and 'overclaim guard present: True'. The file defines exactly eighteen test functions and one of them is test_a_flat_gini_does_not_mean_a_bounded_one, whose three asserts (read at row c138f0078e) fail if section 3.4's criterion is ever simplified back to a drift test -- which is what 'the claims are held in place by the 18 tests in tests/test_redistribution.py, one of which exists specifically to make overclaiming fail loudly' asserts about THIS artefact. SUPERSEDES dfd41f5263: wt171 R4 narrowed the same sentence's OTHER clause, which re-keyed the row; the evidence is byte-identical to the retired row's because nothing about this artefact's clause changed, and that identity is the argument that this is a re-key and not a re-adjudication. WHAT THIS ROW DOES NOT CLEAR: the same sentence's first clause, about regeneration by the two commands section 7 names, is carried at b9dea67210 -- where it is now H rather than the C it was at c9a565b3fe.""",

"7b6a20118e": """prints asserts: ['assert res["assessments"] == 200', 'assert res["transfer_error"] < 1e-12'], then settings swept: ['("stock", 0.25, 0.0)', '("flow", 1.0, 2.0)', '("stock", 0.025, 5.0)'], then implementation reports transfer_error: True. The repaired sentence says this test 'holds the implementation's reported transfer_error below 1e-12'; the second assert IS that bound, character for character, and it runs over three (base, rate, threshold) settings rather than one. The third line carries the other half: transfer_error is a quantity src/wealth_tensor/redistribution.py itself reports, so the test checks the implementation's own number instead of recomputing the invariant beside it. THIS ROW IS NEW, not a re-key: it exists because wt171 R2 replaced the bare target 'the implementation' with a named one, and a repair that names an artefact emits a promise -- wealthTensor-87's lesson, which is the promise sweep working rather than failing. REVIEW-030 section 5.1 row 4, card 1217629169253037.""",

"bc1f66a253": """prints defined in this file: True and pytest: ['1 passed']. The repaired sentence names two artefacts and this row carries the file: test_the_levy_is_a_pure_transfer is defined in tests/test_redistribution.py rather than merely somewhere under tests/, and pytest invoked on that exact node id collects and passes exactly one test. The duration is stripped from the quoted line deliberately -- an evidence command whose stdout carries a timing cannot be held to a verbatim quotation on any later run, which is exactly the property wt170's N28b and F5 below exist to enforce, and the first probe of this command returned '1 passed in 0.18s'. The test's CONTENT is read at 7b6a20118e; this row asserts only where it lives and that it is green.""",

"b9dea67210": """prints printed by neither command: ['0.035', '0.039', '0.103', '0.1073', '0.90', '0.99875', '4.6'], then named as an exception in the section 7 bullet: ['0.035', '0.039', '0.103', '0.1073', '0.90', '0.99875'], then not named, and what it rounds from: {'4.6': ['4.568']}, then unaccounted: []. The first line is IDENTICAL to what the same scan printed for the retired row c9a565b3fe, and that is the point: wt171 narrowed the CLAIM and did not touch a single number in section 3, so the residue could not move. The inherited done-when asked this line to read ['0.1073', '0.99875', '4.6'] and it cannot -- that outcome would require deleting numbers from section 3, and the defect was never in the numbers. The repaired clause excepts six of the seven by name; the seventh, 4.6, is section 3.1's -4.6 % rounded from the -4.568 % the commands print, and 'unaccounted: []' is the sweep of the residue that says so. Two membership tests, differing on purpose: against the section 7 bullet it is boundary-guarded (no digit or dot on either side) so 0.103 cannot be credited by matching inside 0.1073, and against the commands' stdout it is left as the bare substring test c9a565b3fe used, so the two measurements stay commensurable. SUPERSEDES c9a565b3fe, class C. Card 1217630566080722.""",

"5f6d5c4fb9": """prints ['E[eta+] closed form = 0.107269   quadrature = 0.107269'] and ['unlevied Var[log a] = 0.076542', 'stock r=0.10: Var[log a] = 0.076536   (kappa=0.10000)', 'flow  r=0.10: Var[log a] = 0.073276   (kappa=0.01022)', 'flow  r=1.00: Var[log a] = 0.051189   (kappa=0.10216)']. The clause this row carries is that section 3.1's closed-form quantities 'come from python3 scripts/wt077_tail_index.py', and they do: the command prints E[eta+] = 0.107269, which is section 3.1's 0.1073 at the paper's precision, and it prints the three values section 3.1 quotes -- unlevied 0.076542, stock 0.076536 and flow 0.051189. It prints a FOURTH, flow r=0.10 Var[log a] = 0.073276, which the paper does not quote; 'the three Var[log a] values' is a claim about what section 3.1 uses, not about what the script prints, and both are shown here so a later reader can tell the two apart rather than reading 'three' against an output that has four. SUPERSEDES 1cbe31f16c: wt171 R5 edited the OTHER half of the same sentence, which re-keyed this row without changing anything it asserts, and the evidence is byte-identical to the retired row's for that reason. The other half -- regeneration of every number in section 3 -- is adjudicated H at b9dea67210, where it was C.""",
}


# ======================================================================================
# helpers
# ======================================================================================
def sh(cmd, shell=False):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, shell=shell)


def die(msg):
    print(f"{TAG}: REFUSED - {msg}", file=sys.stderr)
    return 2


def emitted():
    r = sh([sys.executable, "scripts/wt148_promise_sweep.py", "--json"])
    if r.returncode == 2:
        raise RuntimeError(r.stderr)
    return json.loads(r.stdout)


def read_tsv():
    return open(os.path.join(REPO, TSV), encoding="utf-8").read().splitlines()


def data_rows(lines):
    return {ln.split("\t")[1]: ln.split("\t")
            for ln in lines if ln and not ln.startswith("#") and "\t" in ln}


def quoted_ok(note, out):
    """Every non-empty line of stdout appears verbatim in the note. wt170 N28b."""
    return all(l in note for l in out.split("\n") if l.strip())


def verify():
    """Re-run EVERY committed paper-II evidence cell and hold it to its note, line by line."""
    rows = [f for f in data_rows(read_tsv()).values() if f[0] == "paper-II"]
    if not rows:
        return die(f"no paper-II rows in {TSV}")
    print(f"=== {TAG} --verify: every paper-II row in {TSV}, evidence re-run ===")
    ok_all = True
    for f in sorted(rows, key=lambda r: r[1]):
        pid, cls, ev, note = f[1], f[3], f[4], f[5]
        r = sh(ev, shell=True)
        ok = r.returncode == 0 and quoted_ok(note, r.stdout)
        ok_all &= ok
        detail = ("stdout is quoted verbatim in the note" if ok else
                  f"rc={r.returncode} first unquoted line: "
                  + repr(next((l for l in r.stdout.split("\n")
                               if l.strip() and l not in note), "<none>")))
        print(f"  [{'ok  ' if ok else 'FAIL'}] {pid} {cls}  {detail}")
    print(f"\n{len(rows)} paper-II rows verified against their committed evidence.")
    if not ok_all:
        print(f"{TAG}: a committed row no longer shows what its note says it shows.",
              file=sys.stderr)
        return 2
    return 0


# ======================================================================================
# main
# ======================================================================================
def main():
    if "--verify" in sys.argv[1:]:
        return verify()

    full = os.path.join(REPO, TSV)
    before_lines = read_tsv()
    before_rows = data_rows(before_lines)

    # ---- guards, before a byte moves ---------------------------------------------------
    prose = sh(["git", "diff", "--name-only", REPAIR_COMMIT, "--", PII])
    if prose.returncode != 0:
        return die(f"git diff against {REPAIR_COMMIT} failed: {prose.stderr.strip()}")
    if prose.stdout.strip():
        return die(f"{PII} has changed since {REPAIR_COMMIT}; this pass adjudicates a fixed "
                   f"emitted set and a manuscript edit moves it underneath the measurement")
    missing_retired = [p for p in RETIRED if p not in before_rows]
    if missing_retired:
        return die(f"refusing to write a twin: {missing_retired} already retired "
                   f"(this script is one-shot; use --verify)")
    already = [p for p in PIDS if p in before_rows]
    if already:
        return die(f"refusing to write a twin: {already} already have rows")
    try:
        pending = {p["pid"]: p for p in emitted()
                   if p["paper"] == "paper-II" and p["pid"] not in before_rows}
    except Exception as exc:                                        # noqa: BLE001
        return die(f"wt148 --json unusable: {exc!r}")
    if set(pending) != set(PIDS):
        return die(f"wt148's unadjudicated paper-II set has come apart from this script's: "
                   f"missing {sorted(set(PIDS) - set(pending))}, "
                   f"unexpected {sorted(set(pending) - set(PIDS))}")
    print(f"{TAG}: guards passed - {PII} is byte-identical to {REPAIR_COMMIT}, the three "
          f"retired rows are present, and wt148 reports exactly the five expected new ids.")

    # ---- run every evidence command BEFORE writing anything -----------------------------
    ran = {pid: sh(EV[pid], shell=True) for pid in PIDS}
    ran.update({pid: sh(cell, shell=True) for pid, (cell, _n, _r) in REEVIDENCED.items()})

    # ---- write --------------------------------------------------------------------------
    new_rows = []
    for pid in PIDS:
        p = pending[pid]
        row = "\t".join([p["paper"], pid, p["artefact"], CLS[pid], EV[pid], NOTE[pid],
                         p["sentence"]])
        if "\n" in row or row.count("\t") != 6:
            return die(f"row for {pid} is malformed ({row.count(chr(9))} tabs)")
        new_rows.append(row)

    ledger = ["\t".join(["#superseded", old, new, "wt171", why])
              for old, (new, why) in SUPERSEDES.items()]
    ledger += ["\t".join(["#reevidenced", pid, TAG, why])
               for pid, (_c, _n, why) in REEVIDENCED.items()]

    shutil.copyfile(full, f"{full}.bak-{TAG}")
    kept = []
    for ln in before_lines:
        f = ln.split("\t")
        if ln and not ln.startswith("#") and "\t" in ln and f[1] in RETIRED:
            continue                                    # retired: its sentence was repaired
        if ln and not ln.startswith("#") and "\t" in ln and f[1] in REEVIDENCED:
            cell, note, _why = REEVIDENCED[f[1]]
            f[4], f[5] = cell, note                     # same promise, new evidence
            ln = "\t".join(f)
        kept.append(ln)
    out = kept + ledger + new_rows
    with open(full, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"{TAG}: retired {len(RETIRED)} rows, re-evidenced {len(REEVIDENCED)}, appended "
          f"{len(new_rows)} rows and {len(ledger)} ledger lines.")

    after_lines = read_tsv()
    after_rows = data_rows(after_lines)
    checks = []

    def rc(script, *a):
        return sh([sys.executable, f"scripts/{script}", *a]).returncode

    try:
        # --- F1 POSITIVE: the sweep this whole pass exists to keep green ----------------
        r148 = sh([sys.executable, "scripts/wt148_promise_sweep.py"])
        pii_line = next((l for l in r148.stdout.split("\n") if "paper-II.md" in l), "")
        checks.append(("F1", "POSITIVE", "wt148 RC 0 and Paper II emits 17 promises",
                       r148.returncode == 0 and "17 promises" in pii_line,
                       f"rc={r148.returncode} line={pii_line.strip()!r}"))

        # --- F2 NEGATIVE: the row-set delta is EXACTLY the predicted one ----------------
        gone = sorted(set(before_rows) - set(after_rows))
        added = sorted(set(after_rows) - set(before_rows))
        checks.append(("F2", "NEGATIVE",
                       "exactly the three predicted rows removed and five added",
                       gone == sorted(RETIRED) and added == sorted(PIDS),
                       f"gone={gone} added={added}"))

        # --- F3 NEGATIVE: no surviving pre-existing row was touched --------------------
        untouched = all(before_rows[p] == after_rows[p] for p in before_rows
                        if p not in RETIRED and p not in REEVIDENCED)
        moved = [p for p in before_rows if p not in RETIRED and p not in REEVIDENCED
                 and before_rows[p] != after_rows.get(p)]
        checks.append(("F3", "NEGATIVE",
                       "every pre-existing row except the retired three and the one "
                       "re-evidenced row is byte-identical",
                       untouched, f"also moved: {moved}"))

        # --- F3b NEGATIVE: the re-evidenced row kept its pid, artefact, class and sentence
        b, a = before_rows["5a47d4caef"], after_rows["5a47d4caef"]
        checks.append(("F3b", "NEGATIVE",
                       "5a47d4caef kept its pid, artefact, class and sentence; only columns "
                       "4 and 5 moved",
                       [b[0], b[1], b[2], b[3], b[6]] == [a[0], a[1], a[2], a[3], a[6]]
                       and b[4] != a[4] and b[5] != a[5],
                       "the re-evidenced row changed more than its evidence and note"))

        # --- F4 POSITIVE: every evidence command ran clean ------------------------------
        allpids = PIDS + list(REEVIDENCED)
        bad_rc = [p for p in allpids if ran[p].returncode != 0]
        checks.append(("F4", "POSITIVE", "all six evidence commands (five new, one "
                       "re-evidenced) exit 0", not bad_rc, f"non-zero: {bad_rc}"))

        # --- F5 NEGATIVE: THE GUARD. Every stdout line is verbatim in its note ----------
        notes = dict(NOTE, **{p: n for p, (_c, n, _r) in REEVIDENCED.items()})
        para = [p for p in allpids if not quoted_ok(notes[p], ran[p].stdout)]
        checks.append(("F5", "NEGATIVE",
                       "every non-empty stdout line appears VERBATIM in its note "
                       "(no paraphrase) - wt170 N28b",
                       not para, f"paraphrased: {para}"))

        # --- F6 NEGATIVE: shape ---------------------------------------------------------
        shape = all(len(after_rows[p]) == 7 for p in PIDS)
        checks.append(("F6", "NEGATIVE", "each new row has exactly seven columns",
                       shape, "a row is malformed"))

        # --- F7 POSITIVE: the supersession ledger names living successors ---------------
        sup = {f[1]: f[2] for f in (l.split("\t") for l in after_lines)
               if f[0] == "#superseded" and len(f) >= 3}
        ree = {f[1] for f in (l.split("\t") for l in after_lines)
               if f[0] == "#reevidenced" and len(f) >= 2}
        ledger_ok = (set(sup) == set(RETIRED) and all(sup[o] in after_rows for o in RETIRED)
                     and ree == set(REEVIDENCED) and all(r in after_rows for r in ree))
        checks.append(("F7", "POSITIVE",
                       "three #superseded lines each naming an ADJUDICATED successor, and "
                       "one #reevidenced line naming a row that is still there",
                       ledger_ok, f"superseded={sup} reevidenced={sorted(ree)}"))

        # --- F8 POSITIVE: wt170 --verify survives the repair, via the ledger ------------
        r170 = sh([sys.executable, "scripts/wt170_paperII_promises.py", "--verify"])
        checks.append(("F8", "POSITIVE",
                       "wt170 --verify RC 0: three rows RETIRED, one REVISED, eleven re-run",
                       r170.returncode == 0 and r170.stdout.count("RETIRED") == 3
                       and r170.stdout.count("REVISED") == 1,
                       f"rc={r170.returncode} RETIRED={r170.stdout.count('RETIRED')} "
                       f"REVISED={r170.stdout.count('REVISED')}"))

        # --- F9 NEGATIVE: THE LEDGER IS A REDIRECTION, NOT A BYPASS ---------------------
        # Fabricate a supersession pointing at a pid that does not exist and prove
        # wt170 --verify still refuses. Done on a copy; the real TSV is restored after.
        probe = f"{full}.probe-{TAG}"
        shutil.copyfile(full, probe)
        try:
            faked = [("\t".join(["#superseded", RETIRED[0], "0000000000", "wt171", "fake"])
                      if l.startswith("#superseded\t" + RETIRED[0]) else l)
                     for l in after_lines]
            with open(full, "w", encoding="utf-8") as fh:
                fh.write("\n".join(faked) + "\n")
            r_fake = sh([sys.executable, "scripts/wt170_paperII_promises.py", "--verify"])
        finally:
            shutil.copyfile(probe, full)
            os.unlink(probe)
        checks.append(("F9", "NEGATIVE",
                       "a #superseded line naming a NON-EXISTENT successor still fails "
                       "wt170 --verify (the ledger redirects, it does not excuse)",
                       r_fake.returncode == 2, f"rc={r_fake.returncode}"))

        # --- F10 POSITIVE: the standing sweeps -----------------------------------------
        sweeps = {s: rc(s) for s in (
            "wt133_crossref_sweep.py", "wt154_evidence_discrimination_sweep.py",
            "wt156_reproducibility_sweep.py", "wt160_bare_pointer_sweep.py",
            "wt163_pointer_vocabulary.py", "wt166_pointer_groundtruth.py",
            "wt169_pointer_groundtruth_heldout.py")}
        checks.append(("F10", "POSITIVE", "wt133/154/156/160/163/166/169 all RC 0",
                       set(sweeps.values()) == {0},
                       str({k.split('_')[0]: v for k, v in sweeps.items()})))

        # --- F11 NEGATIVE: the class distribution says the C is GONE and the N stands ---
        pii = [f for f in after_rows.values() if f[0] == "paper-II"]
        dist = {c: sum(1 for f in pii if f[3] == c) for c in ("H", "N", "R", "C")}
        checks.append(("F11", "NEGATIVE",
                       "Paper II is now 16 H, 1 N, 0 R, 0 C - the C repaired, the N still "
                       "standing and still carded (54c1c5fb27, the arXiv mis-parse)",
                       dist == {"H": 16, "N": 1, "R": 0, "C": 0}
                       and any(f[1] == "54c1c5fb27" for f in pii), str(dist)))

        # --- F12 NEGATIVE: no retired pid survives anywhere as an adjudication ----------
        checks.append(("F12", "NEGATIVE", "no retired pid still has a data row",
                       not [p for p in RETIRED if p in after_rows], "a retired row survived"))

        # --- F13 POSITIVE: this script's own --verify is green over all 17 --------------
        r_self = sh([sys.executable, f"scripts/{TAG}_tsv.py", "--verify"])
        checks.append(("F13", "POSITIVE",
                       f"{TAG} --verify RC 0 over every paper-II row, not just the five",
                       r_self.returncode == 0 and "17 paper-II rows" in r_self.stdout,
                       f"rc={r_self.returncode}"))

        # --- F14 NEGATIVE: the file grew by exactly what was written --------------------
        delta = len(after_lines) - len(before_lines)
        checks.append(("F14", "NEGATIVE",
                       "the file's line count moved by exactly (5 rows + 4 ledger - 3 retired)",
                       delta == 6, f"delta={delta}"))

        # --- F15 NEGATIVE: A `#reevidenced` LINE IS NOT A PARDON ------------------------
        # Break a row's NOTE while leaving its evidence cell byte-identical to wt170's
        # frozen one, and add a #reevidenced line for it. wt170 --verify must STILL fail:
        # the forgiveness is conditional on the cell having actually been replaced.
        probe2 = f"{full}.probe2-{TAG}"
        shutil.copyfile(full, probe2)
        try:
            victim = "4eae009313"
            faked = []
            for l in open(full, encoding="utf-8").read().splitlines():
                g = l.split("\t")
                if not l.startswith("#") and len(g) >= 6 and g[1] == victim:
                    g[5] = "this note quotes nothing at all"
                    l = "\t".join(g)
                faked.append(l)
            faked.append("\t".join(["#reevidenced", victim, TAG, "fabricated by F15"]))
            with open(full, "w", encoding="utf-8") as fh:
                fh.write("\n".join(faked) + "\n")
            r_pardon = sh([sys.executable, "scripts/wt170_paperII_promises.py", "--verify"])
        finally:
            shutil.copyfile(probe2, full)
            os.unlink(probe2)
        checks.append(("F15", "NEGATIVE",
                       "a #reevidenced line for a row whose cell is UNCHANGED does not "
                       "pardon it - wt170 --verify still fails",
                       r_pardon.returncode == 2, f"rc={r_pardon.returncode}"))

        print()
        bad = 0
        for tag, kind, what, ok, detail in checks:
            print(f"  [{'ok  ' if ok else 'FAIL'}] {tag} {kind} {what}"
                  + ("" if ok else f" - {detail}"))
            bad += not ok
        if bad:
            raise RuntimeError(f"{bad} post-condition(s) failed")

    except Exception as exc:                                        # noqa: BLE001
        shutil.copyfile(f"{full}.bak-{TAG}", full)
        print(f"\n{TAG}: ROLLED BACK - {exc}", file=sys.stderr)
        return 2

    h = hashlib.sha256(open(full, "rb").read()).hexdigest()[:12]
    print(f"\n{TAG}: {TSV} now sha256:{h}  -  Paper II 17 of 17 adjudicated, 16 H / 1 N.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
