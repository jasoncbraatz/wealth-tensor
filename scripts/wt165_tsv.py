#!/usr/bin/env python3
"""wt165 — adjudicate the three promises `wt164`'s repair EMITTED, and run every evidence
command inside this script rather than asserting that someone once ran it.

Naming an artefact emits a promise. `wt164` replaced three off-list bare pointers with named
artefacts — `PRE-001` §4.2, the `RESULT-002-*-run.log` pair, `docs/REFERENCE-POLICY.md` — and
`wt148` immediately and correctly reported three unadjudicated promises on in-scope manuscripts.
That is not a regression; it is the instrument doing its job on prose that now says something
checkable. `wealthTensor-87` lesson (iii), budgeted into the same session this time.

ONE OF THESE THREE NEARLY WENT IN WRONG, AND THE NEAR-MISS IS WORTH THE PARAGRAPH.
The first evidence command drafted for `PRE-001` ran `git log --diff-filter=A` over the
registration AND the pilot log **in one invocation**, which prints two dates in reverse
chronological order and attributes neither to a file. Read that way it appeared to show the
pilot log entering the repository 35 minutes BEFORE the registration — i.e. to REFUTE the
sentence. Split per file, it shows the opposite and the truth: `9722342` at 17:11:01 added
`PRE-001` alone, `d655501` at 17:46:52 added the pilot's run log along with PRE-002 and the
RESULT-001 documents. **A `git log` over several paths yields dates you cannot attribute**, and
an evidence column that cannot attribute its own output is worse than no evidence column,
because it looks like diligence. Both commands below are per file.

RED-PROOF: this script REFUSES unless `wt148` reports EXACTLY the three promise ids it is
written to adjudicate, and it keys each row's sentence column off `wt148 --json` so the text is
byte-exact rather than retyped.

EXIT CODES: 0 = three rows added and every post-condition holds · 2 = refused or failed.
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
TAG = "wt165"

PRE1 = "docs/preregistration/PRE-001-wt026-observability-lag.md"
PILOT = "docs/preregistration/RESULT-001-pilot-run.log"
POLICY = "docs/REFERENCE-POLICY.md"

# --- the three evidence commands. Each is ONE line: a TSV cell cannot hold a newline. -----
EV_PRE001 = (
    "python3 -c \"import re,subprocess;"
    "t=re.sub(r'\\s+',' ',open('" + PRE1 + "').read());"
    "g=lambda p: subprocess.check_output(['git','log','--diff-filter=A','--format=%cI %h',"
    "'--',p]).decode().strip();"
    "print('sec42:', '4.2 \\u00b7 Replication universe \\u2014 declared now, run unchanged' in t);"
    "print('deliberate:', 'Declaring the replication *now* is deliberate.' in t);"
    "print('PRE-001 added:', g('" + PRE1 + "'));"
    "print('pilot log added:', g('" + PILOT + "'))\""
)
NOTE_PRE001 = (
    "prints 'sec42: True', 'deliberate: True', 'PRE-001 added: 2026-08-05T17:11:01-05:00 9722342' "
    "and 'pilot log added: 2026-08-05T17:46:52-05:00 d655501'. PRE-001 §4.2 is headed 'Replication "
    "universe -- declared now, run unchanged' and its body says 'Declaring the replication *now* "
    "is deliberate', so the registration DOES declare the replication universe; and the two "
    "add-dates, taken PER FILE, put the registration in the repository 35 minutes before the "
    "pilot's run log, which is what 'before the pilot was run' asserts. Read as a single git log "
    "over both paths the same two dates appear to run the other way and attribute to neither "
    "file -- that draft was discarded, and the reason is in this script's docstring"
)

EV_LOGS = (
    "python3 -c \"import glob;fs=sorted(glob.glob('docs/preregistration/RESULT-002-*-run.log'));"
    "print([(f.split('/')[-1], [l.strip() for l in open(f) if 'permut' in l.lower()]) "
    "for f in fs])\""
)
NOTE_LOGS = (
    "prints both log basenames each carrying exactly one line, 'NEGATIVE CONTROL (tier labels "
    "permuted, lag distribution held fixed):' -- so the label-permutation control IS printed in "
    "those same run logs, in both the pilot and the replication log, and the log's own wording "
    "carries the sentence's 'permutes the tier labels while holding the lag distribution fixed'"
)

EV_POLICY = (
    "python3 -c \"import re;t=re.sub(r'\\s+',' ',open('" + POLICY + "').read());"
    "print('mark-table:', 'Checked against a publisher page, library catalogue, Crossref record "
    "or the issuing body' in t)\""
)
NOTE_POLICY = (
    "prints 'mark-table: True'. REFERENCE-POLICY.md's mark table defines the tick as 'Checked "
    "against a publisher page, library catalogue, Crossref record or the issuing body's own "
    "documentation. Not recalled.' -- which is exactly 'the sources the mark table requires', so "
    "the repaired sentence points at a table that states what the mark means rather than at the "
    "sessions in which it was applied, which a reader cannot open"
)

NEW_ROWS = {
    # pid: (paper, artefact, verdict, evidence, note)
    "608c3d4572": ("paper-III", "PRE-001", "H", EV_PRE001, NOTE_PRE001),
    "fed63cfe77": ("paper-III", "docs/preregistration/RESULT-002-*-run.log", "H",
                   EV_LOGS, NOTE_LOGS),
    "d108d720bb": ("paper-IV", POLICY, "H", EV_POLICY, NOTE_POLICY),
}

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
    except Exception as exc:                                   # noqa: BLE001
        return die(f"wt148 --json unusable: {exc!r}")

    if set(pending) != set(NEW_ROWS):
        return die(f"wt148's unadjudicated set is {sorted(pending)}, not {sorted(NEW_ROWS)} — "
                   f"the repair and this adjudication have come apart.")
    for pid in NEW_ROWS:
        if any(line.split("\t")[1:2] == [pid] for line in before_lines if not line.startswith("#")):
            return die(f"{pid} already has a row; refusing to write a twin.")
    print(f"{TAG}: guard passed — wt148 reports exactly {sorted(pending)} unadjudicated.")

    shutil.copyfile(full_tsv, f"{full_tsv}.bak-{TAG}")
    added = []
    for pid, (paper, artefact, verdict, ev, note) in NEW_ROWS.items():
        row = "\t".join([paper, pid, artefact, verdict, ev, note, pending[pid]["sentence"]])
        if "\n" in row:
            return die(f"row for {pid} contains a newline")
        added.append(row)

    with open(full_tsv, "a", encoding="utf-8") as fh:
        for row in added:
            fh.write(row + "\n")
    print(f"{TAG}: appended {len(added)} row(s).")

    after_lines = open(full_tsv, encoding="utf-8").read().splitlines()
    unchanged_hash = hashlib.sha256("\n".join(after_lines[:len(before_lines)]).encode()).hexdigest()

    def rc(script, *args):
        return sh([sys.executable, f"scripts/{script}", *args]).returncode

    out_pre = sh(EV_PRE001, shell=True)
    out_log = sh(EV_LOGS, shell=True)
    out_pol = sh(EV_POLICY, shell=True)

    new_evidence = [r.split("\t")[4] for r in added]
    new_sentences = [r.split("\t")[6] for r in added]
    rc148 = rc("wt148_promise_sweep.py")
    pending_after = pending_now(after_lines)

    checks = [
        ("F1", "POSITIVE", "wt148 RC 0 after the three rows land", rc148 == 0, f"RC {rc148}"),
        ("F2", "POSITIVE", "no in-scope promise is left unadjudicated",
         not pending_after, f"{len(pending_after)} pending"),
        ("F3", "POSITIVE", "the PRE-001 evidence RUNS and its dates ATTRIBUTE per file",
         ("sec42: True" in out_pre.stdout and "deliberate: True" in out_pre.stdout
          and "PRE-001 added: 2026-08-05T17:11:01-05:00 9722342" in out_pre.stdout
          and "pilot log added: 2026-08-05T17:46:52-05:00 d655501" in out_pre.stdout),
         out_pre.stdout.strip().replace("\n", " | ")[:110]),
        ("F4", "POSITIVE", "the registration PRECEDES the pilot log — the ordering, not just "
                           "two dates",
         "17:11:01" in out_pre.stdout.split("PRE-001 added:")[-1].split("\n")[0]
         and "17:46:52" in out_pre.stdout.split("pilot log added:")[-1],
         "9722342 17:11:01 < d655501 17:46:52"),
        ("F5", "POSITIVE", "the run-log evidence RUNS and both logs carry the control",
         out_log.stdout.count("NEGATIVE CONTROL (tier labels permuted, "
                              "lag distribution held fixed):") == 2,
         out_log.stdout.strip()[:100]),
        ("F6", "POSITIVE", "the policy evidence RUNS and prints True",
         "mark-table: True" in out_pol.stdout, out_pol.stdout.strip()),
        ("F7", "POSITIVE", "wt154 RC 0 — every evidence column READS rather than locates",
         rc("wt154_evidence_discrimination_sweep.py") == 0, "discrimination"),
        ("F8", "POSITIVE", "wt156 RC 0 — every evidence column is runnable today",
         rc("wt156_reproducibility_sweep.py") == 0, "reproducibility"),
        ("F9", "POSITIVE", "wt160 RC 0 and wt163 RC 0 — the repaired prose stays clean",
         rc("wt160_bare_pointer_sweep.py") == 0
         and rc("wt163_pointer_vocabulary.py") == 0, "both pointer sweeps"),
        ("F10", "NEGATIVE", "no pre-existing TSV row changed",
         unchanged_hash == before_hash, "prefix hash identical"),
        ("F11", "NEGATIVE", "the file grew by exactly three lines",
         len(after_lines) - len(before_lines) == 3,
         f"+{len(after_lines) - len(before_lines)}"),
        ("F12", "NEGATIVE", "no new evidence column is a bare path or empty",
         all(e.strip() and "python3" in e for e in new_evidence), "all three are commands"),
        ("F13", "NEGATIVE", "no new sentence still carries its PRE-repair bare pointer",
         all("in the registration before the pilot" not in s
             and "in the same logs" not in s
             and "in the sessions that introduced" not in s for s in new_sentences),
         "post-repair text"),
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
