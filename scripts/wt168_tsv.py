#!/usr/bin/env python3
"""wt168 — adjudicate the ONE promise `wt167`'s repair emitted, evidence run inside this script.

`wt167` re-targeted the fifteenth bare pointer — the one the labelling of all 341 rows found and
no reading in this programme had, because its verb is the copula `are`. Naming an artefact emits
a promise, `wt148` went red with exactly one, and this adjudicates it. `wealthTensor-87` lesson
(iii), now confirmed a third time and budgeted into the same session for the third time.

THE SENTENCE IS NOT THE SENTENCE THAT WAS THERE, AND THAT MATTERS TO THE VERDICT.
The pre-repair sentence read "**Four** registered sensitivity analyses per universe are in the
run logs". `wt167` removed the count as well as repairing the pointer, because the count has no
referent: `scripts/wt026_severe_test.py` runs THREE sensitivities, both `RESULT-002-*-run.log`
files print exactly three, and no fourth is named in `PRE-001`, registered in `PRE-002`, or
implemented anywhere. **Had the count survived the repair, this promise would have adjudicated R,
not H** — which is the point worth keeping: the bare target was what let an unsupported number
stand, because with no artefact named there was nothing to check it against. The identical
"four" in `PRE-002` §2, `RESULT-001` §1 and `RESULT-002` §1 is NOT touched here; an in-place edit
to a registration or a result document is a standing Jason-sized ruling (Asana
`1217603625863293`, the RESULT-001 "320 against 322" card, the same class one instance over) and
this session carded the second instance against it rather than ruling on his behalf.

EVIDENCE DISCIPLINE. The command below queries EACH log file separately and prints a per-file
result. `wealthTensor-88`'s lesson (v) — a command run over several paths at once yields output
you cannot attribute, and an evidence column that cannot attribute its own output is worse than
none because it reads as diligence.

RED-PROOF: this script REFUSES unless `wt148` reports EXACTLY the one promise id it is written to
adjudicate, and it keys the row's sentence column off `wt148 --json` so the text is byte-exact
rather than retyped.

EXIT CODES: 0 = one row added and every post-condition holds · 2 = refused or failed.
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
TAG = "wt168"

PID = "37d8d59fa8"
ARTEFACT = "docs/preregistration/RESULT-002-*-run.log"

# ONE line — a TSV cell cannot hold a newline. Per FILE, never one command over both paths.
EV = (
    "python3 -c \"import glob;"
    "fs=sorted(glob.glob('docs/preregistration/RESULT-002-*-run.log'));"
    "print([(f.split('/')[-1],"
    "sum(1 for l in open(f) if l.startswith('===== SENSITIVITY')),"
    "sorted({l.split('VERDICT:')[1].strip() for l in open(f) if 'VERDICT:' in l}))"
    " for f in fs])\""
)
QUOTED_OUTPUT = (
    "[('RESULT-002-pilot-run.log', 3, ['INCONCLUSIVE (underpowered)', 'PREDICTION FAILS']), "
    "('RESULT-002-replication-run.log', 3, ['PREDICTION FAILS'])]"
)
NOTE = (
    "prints " + QUOTED_OUTPUT + " "
    "-- queried PER FILE, so each count and each verdict set attributes to a named log. Both "
    "named logs exist and each carries the registered sensitivity analyses, which is what 'are in "
    "the run logs (docs/preregistration/RESULT-002-*-run.log)' asserts; and the only verdicts any "
    "sensitivity block reports are PREDICTION FAILS and INCONCLUSIVE (underpowered), never a pass, "
    "which is what 'none reverses the verdict' asserts. NOTE FOR A SUCCESSOR: the count is THREE "
    "per universe. The pre-repair sentence said four and wt167 removed the number rather than "
    "rewriting it, because the same unsupported four still stands in PRE-002 s2, RESULT-001 s1 and "
    "RESULT-002 s1 and editing a registration in place is Jason's ruling, carded 1217603625863293"
)

IN_SCOPE = ("paper-III", "paper-IV")


def sh(cmd, shell=False):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, shell=shell)


def die(msg):
    print(f"{TAG}: REFUSED — {msg}", file=sys.stderr)
    return 2


def emitted():
    r = sh([sys.executable, "scripts/wt148_promise_sweep.py", "--json"])
    if r.returncode == 2:
        raise RuntimeError(r.stderr)
    return json.loads(r.stdout)


def adjudicated_ids(lines):
    return {ln.split("\t")[1] for ln in lines if ln and not ln.startswith("#") and "\t" in ln}


def pending_now(lines):
    have = adjudicated_ids(lines)
    return {p["pid"]: p for p in emitted()
            if p["paper"] in IN_SCOPE and p["pid"] not in have}


def main():
    full_tsv = os.path.join(REPO, TSV)
    before_lines = open(full_tsv, encoding="utf-8").read().splitlines()
    before_hash = hashlib.sha256("\n".join(before_lines).encode()).hexdigest()

    try:
        pending = pending_now(before_lines)
    except Exception as exc:                                    # noqa: BLE001
        return die(f"wt148 --json unusable: {exc!r}")

    if set(pending) != {PID}:
        return die(f"wt148's unadjudicated set is {sorted(pending)}, not ['{PID}'] — "
                   f"the repair and this adjudication have come apart.")
    if any(line.split("\t")[1:2] == [PID] for line in before_lines if not line.startswith("#")):
        return die(f"{PID} already has a row; refusing to write a twin.")
    print(f"{TAG}: guard passed — wt148 reports exactly ['{PID}'] unadjudicated.")

    sentence = pending[PID]["sentence"]
    row = "\t".join(["paper-III", PID, ARTEFACT, "H", EV, NOTE, sentence])
    if "\n" in row:
        return die("the row contains a newline")

    shutil.copyfile(full_tsv, f"{full_tsv}.bak-{TAG}")
    with open(full_tsv, "a", encoding="utf-8") as fh:
        fh.write(row + "\n")
    print(f"{TAG}: appended 1 row.")

    after_lines = open(full_tsv, encoding="utf-8").read().splitlines()
    unchanged_hash = hashlib.sha256("\n".join(after_lines[:len(before_lines)]).encode()).hexdigest()

    def rc(script, *a):
        return sh([sys.executable, f"scripts/{script}", *a]).returncode

    out = sh(EV, shell=True)
    rc148 = rc("wt148_promise_sweep.py")
    pending_after = pending_now(after_lines)

    checks = [
        ("H1", "POSITIVE", "wt148 RC 0 after the row lands", rc148 == 0, f"RC {rc148}"),
        ("H2", "POSITIVE", "no in-scope promise is left unadjudicated",
         not pending_after, f"{len(pending_after)} pending"),
        ("H3", "POSITIVE", "the evidence RUNS and attributes PER FILE — both logs named, each "
                           "with its own count",
         out.stdout.count("RESULT-002-") == 2 and "pilot-run.log" in out.stdout
         and "replication-run.log" in out.stdout, out.stdout.strip()[:150]),
        ("H4", "POSITIVE", "each named log carries THREE sensitivity blocks",
         out.stdout.count(", 3, ") == 2, "3 and 3"),
        ("H5", "NEGATIVE", "no sensitivity block reverses the verdict — no verdict other than "
                           "PREDICTION FAILS or INCONCLUSIVE appears",
         ("PREDICTION FAILS" in out.stdout and "INCONCLUSIVE (underpowered)" in out.stdout
          and "PREDICTION HOLDS" not in out.stdout and "PASSES" not in out.stdout),
         "FAILS / INCONCLUSIVE only"),
        ("H6", "NEGATIVE", "the adjudicated sentence no longer carries the unsupported count",
         "Four registered sensitivity" not in sentence, "the count was removed by wt167"),
        ("H7", "NEGATIVE", "the adjudicated sentence is the REPAIRED one, not the bare pointer",
         "run logs (`docs/preregistration/RESULT-002-*-run.log`)" in sentence,
         "keyed off wt148 --json, byte-exact"),
        ("H8", "POSITIVE", "wt154 RC 0 — the evidence column READS rather than locates",
         rc("wt154_evidence_discrimination_sweep.py") == 0, "discrimination"),
        ("H9", "POSITIVE", "wt156 RC 0 — the evidence column is runnable today",
         rc("wt156_reproducibility_sweep.py") == 0, "reproducibility"),
        ("H10", "POSITIVE", "wt160 RC 0, wt163 RC 0 and wt166 RC 0 — the repaired prose stays "
                            "clean and the ground truth still matches the corpus",
         rc("wt160_bare_pointer_sweep.py") == 0 and rc("wt163_pointer_vocabulary.py") == 0
         and rc("wt166_pointer_groundtruth.py") == 0, "three sweeps"),
        ("H11", "NEGATIVE", "no pre-existing TSV row changed",
         unchanged_hash == before_hash, "prefix hash identical"),
        ("H12", "NEGATIVE", "the file grew by exactly one line",
         len(after_lines) - len(before_lines) == 1,
         f"+{len(after_lines) - len(before_lines)}"),
        ("H13", "NEGATIVE", "the evidence command queries each path separately — it is not one "
                            "invocation over a glob whose output cannot be attributed",
         "for f in fs" in EV and "f.split('/')[-1]" in EV,
         "per-file, wealthTensor-88 lesson (v)"),
        ("H14", "POSITIVE", "the note QUOTES its command's ACTUAL output, character for "
                            "character — a note that paraphrases its own evidence is a note "
                            "nobody has checked",
         out.stdout.strip() == QUOTED_OUTPUT,
         "first draft of this note claimed INCONCLUSIVE in BOTH logs; only the pilot has one, "
         "and H3's printed output is what caught it"),
    ]

    ok_all = True
    print(f"\n=== {TAG} post-conditions ===")
    for cid, kind, desc, ok, detail in checks:
        ok_all &= bool(ok)
        print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} — {detail}")
    print(f"\n{len(checks)} post-conditions, "
          f"{sum(1 for c in checks if c[1] == 'NEGATIVE')} NEGATIVE.")

    if not ok_all:
        print(f"{TAG}: POST-CONDITIONS FAILED — rolling back.", file=sys.stderr)
        shutil.copyfile(f"{full_tsv}.bak-{TAG}", full_tsv)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
