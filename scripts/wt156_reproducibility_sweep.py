#!/usr/bin/env python3
"""wt156 · REPRODUCIBILITY SWEEP over docs/promises-adjudicated.tsv.

WHAT THIS MEASURES, IN THE FILE'S OWN WORDS
-------------------------------------------
The TSV header states the falsification procedure for a row:

    1. Take the row's `evidence` column. It names a command to run or a file to read.
    2. Run it or read it. If it does not show what `note` says it shows, the row is FALSE.

wt154 asked whether the evidence READ the artefact or merely LOCATED it.  This sweep asks the
prior question: **can step 1 be carried out at all today, by a reader who was not in the session
that wrote the row?**  A row that fails step 1 cannot reach step 2, so it can never be falsified,
and an unfalsifiable row is worth what wealthTensor-83 said it was worth: nothing.

The detectors operate on the `evidence` column ALONE.  That is not a narrowing chosen to make the
count come out — it is the header's own contract about which column carries the handle.  Several
flagged rows do name a runnable command in their `artefact` column; REVIEW-026 §2 says so, and says
why that is a different (weaker) claim than the header makes.

TWO DETECTORS, REPORTED SEPARATELY
----------------------------------
D1 · RECORD IN A VANISHED SESSION
    The evidence's account of where the result lives is a session, a session log, or a machine
    ("output in the session log", "on darwin", "wealthTensor-NN") and, once those locators are
    removed, nothing re-executable remains.  `run on darwin, wealthTensor-82; output in the
    session log` is the canonical instance; `git log/cat-file on darwin, wealthTensor-82` is the
    same defect with a command family in place of the word "run".

D2 · NO OPERAND
    No session locator is involved — the evidence is simply a verb or a back-reference with
    nothing to act on: `same test`, `read the document`, `read the module`.

A HANDLE is anything a later reader can execute or open:
    · a path with a known extension            src/wealth_tensor/lag.py, docs/LEDGER.md
    · a git object id (>=7 hex, >=1 digit)     9722342, d655501
    · a section or line pointer                §5.4, L1206
    · a quoted search pattern                  'def test_', "244 events"
    · a named test function                    test_pre001_constants_are_what_was_registered
    · a programme identifier                   PRE-002, REG-013, WT-059, REVIEW-001

EXIT CODES  (load-bearing; do not collapse 2 into 1)
    0  no row flags
    1  at least one row flags
    2  a POST-CONDITION failed — the sweep itself is broken and its count means nothing

USAGE
    python3 scripts/wt156_reproducibility_sweep.py [--json] [--rev REV] [--skip-postconditions]
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TSV = "docs/promises-adjudicated.tsv"

# --------------------------------------------------------------------------------------------
# the vocabulary
# --------------------------------------------------------------------------------------------

LOCATORS = [
    re.compile(r"output in the session log", re.I),
    re.compile(r"in the session log", re.I),
    re.compile(r"\bon darwin\b", re.I),
    re.compile(r"\bwealthTensor-\d+\b", re.I),
]

HANDLES = [
    ("path", re.compile(r"[\w./\-]+\.(?:py|md|json|jsonl|log|tsv|txt)\b")),
    ("gitobj", re.compile(r"\b(?=[0-9a-f]{7,40}\b)(?=[0-9a-f]*\d)[0-9a-f]{7,40}\b")),
    ("section", re.compile(r"§\s*\d|\bL\d{1,5}\b")),
    ("quoted", re.compile(r"'[^']+'|\"[^\"]+\"|`[^`]+`")),
    ("testname", re.compile(r"\btest_\w+")),
    ("programme_id", re.compile(r"\b[A-Z]{2,}-\d{3}\b")),
]

VALUE_IN_NOTE = re.compile(r"\d")  # a number the re-run could disagree with


def strip_locators(evidence: str) -> str:
    out = evidence
    for pat in LOCATORS:
        out = pat.sub(" ", out)
    return out


def has_locator(evidence: str) -> bool:
    return any(p.search(evidence) for p in LOCATORS)


def handles(evidence: str):
    stripped = strip_locators(evidence)
    return [name for name, pat in HANDLES if pat.search(stripped)]


# --------------------------------------------------------------------------------------------
# the file
# --------------------------------------------------------------------------------------------

COLUMNS = ("paper", "promise_id", "artefact", "class", "evidence", "note", "sentence")


def read_tsv(rev=None):
    if rev:
        raw = subprocess.run(
            ["git", "show", f"{rev}:{TSV}"], cwd=REPO, capture_output=True, text=True, check=True
        ).stdout
    else:
        raw = (REPO / TSV).read_text()
    rows = []
    for line in raw.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != len(COLUMNS):
            raise SystemExit(f"wt156: malformed row ({len(parts)} cols): {line[:80]!r}")
        rows.append(dict(zip(COLUMNS, parts)))
    return rows


def sweep(rev=None):
    rows = read_tsv(rev)
    d1, d2, clean = [], [], []
    for r in rows:
        ev = r["evidence"]
        h = handles(ev)
        rec = {
            "promise_id": r["promise_id"],
            "paper": r["paper"],
            "artefact": r["artefact"],
            "class": r["class"],
            "evidence": ev,
            "handles": h,
            "value_in_note": bool(VALUE_IN_NOTE.search(r["note"])),
        }
        if h:
            clean.append(rec)
        elif has_locator(ev):
            d1.append(rec)
        else:
            d2.append(rec)
    return {"rev": rev or "WORKTREE", "n_rows": len(rows), "d1": d1, "d2": d2, "clean": clean}


# --------------------------------------------------------------------------------------------
# post-conditions — the severe test is the b50bccd-vs-HEAD pair
# --------------------------------------------------------------------------------------------

BEFORE = "b50bccd"  # -85's census commit: the file BEFORE any wt156 repair

SIXTEEN = [
    "ac16838bdb", "d6c6430592", "314390a26e", "f7674cbd06", "070d5c7a60", "6d9934a0bc",
    "a01f12e7be", "d4dd6baf17", "c14cdd1f1b", "f8f41df587", "e91d103026", "4c35bb44b7",
    "12dc448265", "41744fe2ae", "10d2d456ea", "a00820b165",
]
GITLOG_SEVENTEEN = [
    "988f2c17eb", "c8ce16780e", "d9f85198a4", "6d3081f7d0", "ff83025f93", "e982f4354d",
    "b027807bb2", "f0e2d9c802", "a1e418ec3d", "08661953ec", "3de6bdab52", "9add6ff45d",
    "e1e02600e0", "d0729375b9", "55a9b6a983", "e087b31b91", "ffc2d520de",
]
SHASUM_TWO = ["37b5a0dc57", "aebdfa4d76"]
BARE_EIGHT = [
    "e949f42f3b", "6399cc6879", "1ae72956c3", "6efe91d805",
    "150f86a167", "79d2484c84", "b64ff1c700", "30191fec1a",
]


def post_conditions():
    """Returns (results, ok). Each result: (name, polarity, passed, detail)."""
    before = sweep(BEFORE)
    now = sweep(None)
    b_d1 = {r["promise_id"] for r in before["d1"]}
    b_d2 = {r["promise_id"] for r in before["d2"]}
    b_all = b_d1 | b_d2
    n_d1 = {r["promise_id"] for r in now["d1"]}
    n_d2 = {r["promise_id"] for r in now["d2"]}
    n_all = n_d1 | n_d2

    res = []

    def check(name, polarity, cond, detail):
        res.append((name, polarity, bool(cond), detail))

    # --- POSITIVE: the sweep must catch, at BEFORE, every row this at-bat was written from
    missing = [p for p in SIXTEEN if p not in b_d1]
    check("P1 the sixteen unrunnable rows flag under D1 at " + BEFORE, "POSITIVE",
          not missing, f"missing={missing}")

    missing = [p for p in GITLOG_SEVENTEEN if p not in b_d1]
    check("P2 the seventeen `git log/cat-file` rows flag under D1 at " + BEFORE, "POSITIVE",
          not missing, f"missing={missing}")

    missing = [p for p in SHASUM_TWO if p not in b_d1]
    check("P3 the two `shasum -a 256 on darwin` rows flag under D1 at " + BEFORE, "POSITIVE",
          not missing, f"missing={missing}")

    missing = [p for p in BARE_EIGHT if p not in b_d2]
    check("P4 the eight bare back-reference rows flag under D2 at " + BEFORE, "POSITIVE",
          not missing, f"missing={missing}")

    # --- NEGATIVE: a locator is not the tell; a HANDLE is. These rows carry BOTH.
    check("P5 NEGATIVE 9696c13d6a (`python3 on darwin, wealthTensor-83: ... data/pre-002-events.json`) "
          "does NOT flag at " + BEFORE, "NEGATIVE",
          "9696c13d6a" not in b_all, "a locator with a path is still runnable")

    check("P6 NEGATIVE 5f35388d48 and 7090dac01e (`read <path> §N, wealthTensor-83`) do NOT flag at "
          + BEFORE, "NEGATIVE",
          "5f35388d48" not in b_all and "7090dac01e" not in b_all, "")

    check("P7 NEGATIVE bb9fba4abf (`python3 scripts/wt089_...py (RC 0) §3 A1`) does NOT flag at "
          + BEFORE, "NEGATIVE", "bb9fba4abf" not in b_all, "")

    check("P8 NEGATIVE 3bdab165bf (`read docs/preregistration/REG-005-...md §2 and §5`) does NOT "
          "flag at " + BEFORE, "NEGATIVE", "3bdab165bf" not in b_all, "")

    # --- shape
    check(f"P9 the file at {BEFORE} parses to 129 rows", "POSITIVE",
          before["n_rows"] == 129, f"n_rows={before['n_rows']}")

    # --- the repair, at the working tree
    still = [p for p in SIXTEEN if p in n_all]
    check("P10 none of the sixteen flag at the WORKTREE (the repair moved the file)", "POSITIVE",
          not still, f"still flagging={still}")

    check("P11 nothing flags at the WORKTREE (the file is clean at its own criterion)", "POSITIVE",
          not n_all, f"flagging={sorted(n_all)}")

    ok = all(r[2] for r in res)
    return res, ok, before, now


# --------------------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rev", default=None, help="sweep the TSV as of a git revision")
    ap.add_argument("--skip-postconditions", action="store_true")
    args = ap.parse_args()

    result = sweep(args.rev)

    pc, pc_ok = None, True
    if not args.skip_postconditions and args.rev is None:
        pc, pc_ok, _, _ = post_conditions()

    flagged = result["d1"] + result["d2"]

    if args.json:
        out = dict(result)
        out["n_flagged"] = len(flagged)
        out["n_d1"] = len(result["d1"])
        out["n_d2"] = len(result["d2"])
        out["no_value_in_note"] = [r["promise_id"] for r in flagged if not r["value_in_note"]]
        if pc is not None:
            out["post_conditions"] = [
                {"name": n, "polarity": p, "passed": ok, "detail": d} for n, p, ok, d in pc
            ]
            out["post_conditions_ok"] = pc_ok
        print(json.dumps(out, indent=2))
    else:
        print(f"=== wt156 · reproducibility sweep — {result['rev']} — {result['n_rows']} adjudicated rows ===")
        print()
        print(f"D1 · RECORD IN A VANISHED SESSION  {len(result['d1'])} row(s)")
        for r in result["d1"]:
            print(f"    {r['promise_id']}  {r['paper']:<9} [{r['class']}]  evidence: {r['evidence']}")
        print()
        print(f"D2 · NO OPERAND                    {len(result['d2'])} row(s)")
        for r in result["d2"]:
            print(f"    {r['promise_id']}  {r['paper']:<9} [{r['class']}]  evidence: {r['evidence']}")
        print()
        novalue = [r["promise_id"] for r in flagged if not r["value_in_note"]]
        print(f"    of the {len(flagged)} flagged, {len(novalue)} carry no number in `note` at all,")
        print(f"    so even a successful re-run would have nothing to disagree with: {novalue}")
        print()
        if pc is not None:
            npos = sum(1 for n, p, o, d in pc if p == "POSITIVE")
            nneg = sum(1 for n, p, o, d in pc if p == "NEGATIVE")
            print(f"POST-CONDITIONS ({len(pc)} total, {nneg} NEGATIVE, {npos} POSITIVE)")
            for n, p, ok, d in pc:
                mark = "ok  " if ok else "FAIL"
                print(f"    [{mark}] {n}" + (f"   {d}" if (d and not ok) else ""))
            print()
            if not pc_ok:
                print("wt156: A POST-CONDITION FAILED. The sweep is broken; its counts mean nothing.")
                return 2
        print(f"TOTAL FLAGGED: {len(flagged)} of {result['n_rows']}")

    if pc is not None and not pc_ok:
        return 2
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
