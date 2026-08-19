#!/usr/bin/env python3
"""wt162 — adjudicate the two promises wt161's repair EMITTED, and run every sweep behind them.

Naming an artefact emits a promise. `wt161` replaced Paper IV §6's two bare `the registration`
pointers with `REG-013`, which is the whole point of the repair — and `wt148` immediately and
correctly reported two unadjudicated promises on an in-scope manuscript. That is not a
regression; it is the instrument doing its job on prose that now says something checkable.

RED-PROOF: this script REFUSES unless `wt148` reports EXACTLY the two promise ids it is written
to adjudicate, and it keys each new row's sentence column off `wt148 --json` so the text is
byte-exact rather than retyped. It then RUNS both evidence commands and requires their output to
carry the values the notes claim — an evidence column nobody executed is a promise about a
promise.

EXIT CODES: 0 = both rows added and every post-condition holds · 2 = refused or failed.
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
TAG = "wt162"
REG = "docs/preregistration/REG-013-citation-graph-whitespace.md"
RUN = "docs/preregistration/RESULT-REG-013-run.json"

EV_SEEDS = (
    "python3 -c \"import json,re;t=re.sub(r'\\s+',' ',open('" + REG + "').read());"
    "d=json.load(open('" + RUN + "'));"
    "a=[(k,s['asked']) for k,c in d['seeds'].items() for s in c];"
    "print({k:'%d/%d'%(sum(1 for kk,x in a if kk==k and x in t),"
    "sum(1 for kk,_ in a if kk==k)) for k in d['seeds']})\""
)
NOTE_SEEDS = (
    "prints {'T': '7/7', 'S': '5/6', 'K': '5/6', 'X': '0/6'} on 2026-08-18 -- every seed title the "
    "run ASKED for, matched verbatim against REG-013 with whitespace flattened. The two S/K misses "
    "are the same works under REG-013 §3.1's shorter forms (*Monetary Economics* for the full "
    "subtitle; 'standard Γ distribution' for the run's 'standard Gamma distribution'). X is 0/6 "
    "because §3.2 names the FLOOR cluster by author-year (Jinek et al. 2012; Cong et al. 2013; Mali "
    "et al. 2013; Doudna & Charpentier 2014; Ran et al. 2013; Komor et al. 2016) rather than by "
    "title, and X is a control, not one of the three literatures the sentence is about"
)

EV_FERTILE = (
    "python3 -c \"import re,subprocess;t=re.sub(r'\\s+',' ',open('" + REG + "').read());"
    "print('disclaimer:', 'It is not evidence that the intersection is *fertile*.' in t);"
    "print(subprocess.check_output(['git','log','--diff-filter=A','--format=%cI %h','--',"
    "'" + REG + "','" + RUN + "']).decode().strip())\""
)
NOTE_FERTILE = (
    "prints 'disclaimer: True' and the two add-dates 2026-08-16T09:40:55-05:00 fff7063 (REG-013) "
    "and 2026-08-16T09:56:54-05:00 5efe626 (the run's JSON) -- the registration entered the "
    "repository 16 minutes BEFORE the numbers did, which is what 'before the numbers existed' "
    "asserts. REG-013 §4 carries the disclaimer verbatim: 'a measured absence of co-citation is "
    "evidence that the intersection is *unoccupied*. It is not evidence that the intersection is "
    "*fertile*. Paper IV may cite this result for the first claim only.'"
)

NEW_ROWS = {
    "80809cfe15": ("paper-IV", "REG-013", "H", EV_SEEDS, NOTE_SEEDS),
    "a6735d5cbc": ("paper-IV", "REG-013", "H", EV_FERTILE, NOTE_FERTILE),
}


def sh(cmd, shell=False):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, shell=shell)


def die(msg):
    print(f"{TAG}: REFUSED — {msg}", file=sys.stderr)
    return 2


IN_SCOPE = ("paper-III", "paper-IV")


def emitted():
    """wt148 --json is a FLAT list of every promise it emits, adjudicated or not."""
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

    # ---- guard: exactly the two ids, and neither already has a row --------------------
    try:
        pending = pending_now(before_lines)
    except Exception as exc:                                   # noqa: BLE001
        return die(f"wt148 --json unusable: {exc!r}")

    if set(pending) != set(NEW_ROWS):
        return die(f"wt148's unadjudicated set is {sorted(pending)}, "
                   f"not {sorted(NEW_ROWS)} — the repair and this adjudication have come apart.")
    for pid in NEW_ROWS:
        if any(line.split("\t")[1:2] == [pid] for line in before_lines if not line.startswith("#")):
            return die(f"{pid} already has a row; refusing to write a twin.")
    print(f"{TAG}: guard passed — wt148 reports exactly {sorted(pending)} unadjudicated.")

    # ---- build the rows, sentence keyed off wt148 so it is byte-exact -----------------
    shutil.copyfile(full_tsv, f"{full_tsv}.bak-{TAG}")
    added = []
    for pid, (paper, artefact, verdict, ev, note) in NEW_ROWS.items():
        sentence = pending[pid]["sentence"]
        row = "\t".join([paper, pid, artefact, verdict, ev, note, sentence])
        if "\n" in row:
            return die(f"row for {pid} contains a newline")
        added.append(row)

    with open(full_tsv, "a", encoding="utf-8") as fh:
        for row in added:
            fh.write(row + "\n")
    print(f"{TAG}: appended {len(added)} row(s).")

    # ---- post-conditions --------------------------------------------------------------
    after_lines = open(full_tsv, encoding="utf-8").read().splitlines()
    unchanged_hash = hashlib.sha256("\n".join(after_lines[:len(before_lines)]).encode()).hexdigest()

    def rc(script, *args):
        return sh([sys.executable, f"scripts/{script}", *args]).returncode

    ev_seed_out = sh(EV_SEEDS, shell=True)
    ev_fert_out = sh(EV_FERTILE, shell=True)

    new_sentences = [r.split("\t")[6] for r in added]
    new_evidence = [r.split("\t")[4] for r in added]

    rc148 = rc("wt148_promise_sweep.py")
    pending_after = pending_now(after_lines)

    checks = [
        ("E1", "POSITIVE", "wt148 RC 0 after the two rows land", rc148 == 0, f"RC {rc148}"),
        ("E2", "POSITIVE", "no in-scope promise is left unadjudicated",
         not pending_after, f"{len(pending_after)} pending"),
        ("E3", "POSITIVE", "wt154 RC 0 — both evidence columns READ rather than locate",
         rc("wt154_evidence_discrimination_sweep.py") == 0, "discrimination"),
        ("E4", "POSITIVE", "wt156 RC 0 — both evidence columns are runnable today",
         rc("wt156_reproducibility_sweep.py") == 0, "reproducibility"),
        ("E5", "POSITIVE", "wt160 RC 0 — the repaired prose still has no bare pointer",
         rc("wt160_bare_pointer_sweep.py") == 0, "bare pointers"),
        ("E6", "POSITIVE", "wt133 RC 0", rc("wt133_crossref_sweep.py") == 0, "cross-refs"),
        ("E7", "POSITIVE", "the seed-title evidence RUNS and prints the note's dictionary",
         "{'T': '7/7', 'S': '5/6', 'K': '5/6', 'X': '0/6'}" in ev_seed_out.stdout,
         ev_seed_out.stdout.strip()[:70]),
        ("E8", "POSITIVE", "the registration evidence RUNS and prints the disclaimer and both dates",
         "disclaimer: True" in ev_fert_out.stdout
         and "2026-08-16T09:40:55-05:00 fff7063" in ev_fert_out.stdout
         and "2026-08-16T09:56:54-05:00 5efe626" in ev_fert_out.stdout,
         ev_fert_out.stdout.strip().replace("\n", " | ")[:90]),
        ("E9", "NEGATIVE", "no pre-existing TSV row changed",
         unchanged_hash == before_hash, "prefix hash identical"),
        ("E10", "NEGATIVE", "the file grew by exactly two lines",
         len(after_lines) - len(before_lines) == 2, f"+{len(after_lines) - len(before_lines)}"),
        ("E11", "NEGATIVE", "neither new evidence column is empty or a bare path",
         all(e.strip() and ("python3" in e or "`" in e) for e in new_evidence), "both are commands"),
        ("E12", "NEGATIVE", "both new sentences carry the REPAIRED text (`REG-013`, not "
                            "'the registration')",
         all("`REG-013`" in s and "in the registration" not in s for s in new_sentences),
         "post-repair text"),
    ]

    ok_all = True
    print(f"\n=== {TAG} post-conditions ===")
    for cid, kind, desc, ok, detail in checks:
        ok_all &= bool(ok)
        print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} — {detail}")
    print(f"\n{len(checks)} post-conditions, {sum(1 for c in checks if c[1]=='NEGATIVE')} NEGATIVE.")

    if not ok_all:
        print(f"{TAG}: POST-CONDITIONS FAILED — rolling back.", file=sys.stderr)
        shutil.copyfile(f"{full_tsv}.bak-{TAG}", full_tsv)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
