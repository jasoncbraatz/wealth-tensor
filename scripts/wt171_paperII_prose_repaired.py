#!/usr/bin/env python3
"""wt171 - repair Paper II's four standing prose defects in ONE pass, and prove what did not move.

WHY ALL FOUR IN ONE SCRIPT
--------------------------
Every defect standing in Paper II at `wealthTensor-91`'s wrap was a prose defect in one
manuscript: the section 7 exception clause (card 1217630566080722, `docs/promises-adjudicated.tsv`
row `c9a565b3fe`, class C) and three bare pointers (card 1217629169253037, rows 3, 4 and 7 of
REVIEW-030 section 5.1's seven). Repairing them separately costs two re-adjudication cycles for
one paper, because ANY edit to a sentence re-keys `promise_id` and the old row must be deleted in
the same commit or `wt148` reports it STALE. One edit, one re-adjudication: `wt172_tsv`.

THE SIX EDITS, AND WHICH CHARTER MODE EACH IS (`docs/CO-AUTHOR-CHARTER.md` section 2)
--------------------------------------------------------------------------------------
  R1  RE-TARGET  L11   "named in the data-availability statement" -> "named in section 7".
                       This is the construction `wt164` already repaired in Paper III; Papers III
                       and IV carry "named in section 11" and "named in section 10" respectively,
                       so the identical defect was shipping in one manuscript of three. The repair
                       is not invented here, it is copied.
  R2  RE-TARGET  L132  "verified to machine precision in the implementation" -> names the test.
                       "The implementation" is a bare target: the reader is sent to check
                       something and given nothing to open. `test_the_levy_is_a_pure_transfer`
                       in `tests/test_redistribution.py` is what actually holds the invariant.
  R3  RE-TARGET  L177  "visible in the third column" -> "the table's kappa column". REVIEW-030
                       classes this SOFT because the table is adjacent, and the card asks for an
                       explicit ruling. THE RULING IS: repair it. Naming the column by its header
                       costs one word, and a positional handle breaks silently the moment a
                       column is inserted - which is a defect that arrives with no diff.
  R4  REPLACE    L88   the abstract's exception clause, narrowed to the whole class.
  R5  REPLACE    L452  section 7's exception clause, narrowed to the whole class and ENUMERATED.
  R6  REPLACE    L447  drops the numeral in "save five closed-form quantities". R5 introduces a
                       DIFFERENT five two bullets below it, and two adjacent fives naming
                       different sets is `wealthTensor-91` lesson (i) written into a manuscript.
                       No claim changes; only the numeral goes.

None is an ABSORB. No hedge is added anywhere and `defensive_count.py` is run over the result
(E10) against Paper II's committed baseline of 0.

THE POINT OF E5, E6 AND E7 - WHAT THE INSTRUMENTS CANNOT SEE
-------------------------------------------------------------
`wealthTensor-92`'s brief asks for `wt167`'s G4 pattern: `wt160`'s and `wt163`'s flag sets
BIT-IDENTICAL across the repair, proved in the script rather than asserted in the review. They
are - and the reason is worth more than the check. **`wt160.PAPERS` and `wt163.PAPERS` are
Papers III and IV. Neither instrument has ever read Paper II.** E5 and E6 therefore prove the
bit-identity AND assert the reason for it, so a successor reads a real fact instead of a green
line that sounds like coverage. That gap is why the seven bare pointers of REVIEW-030 section 5.1
were found by a labelling pass and not by the sweep that is named for them.

`wt169`'s revision pin is the same story one level deeper. REVIEW-030 section 8 falsifier 4 says
the pin "has never been exercised by a real repair" and asks the first repairing session to
exercise it. E7 exercises it: `wt169`'s entire JSON payload is captured before and after the
edit and must be byte-identical. **It is, and it could not have been otherwise** - `wt169` reads
both manuscripts through `git show 83db4d5:` and never touches the working tree, so a manuscript
repair cannot move it by construction. The pin is a guard against the ground-truth TSV and the
word lists drifting; it is NOT a guard against manuscript repair, and falsifier 4 mis-describes
what it does. E7 is the run that settles that, which is why it captures the payload rather than
just the exit code.

ROLLBACK: `paper-II.md` is copied to `paper-II.md.bak-wt171` before the first byte moves and
restored if any post-condition fails. A rollback is not a verdict on the repair
(`wealthTensor-87` lesson (iv)).

EXIT: 0 = repaired and every post-condition holds - 1 = rolled back - 2 = refused before writing.
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PII = "docs/papers/paper-II-redistribution/paper-II.md"
PIII = "docs/papers/paper-III-dual-tensor/paper-III.md"
PIV = "docs/papers/paper-IV-composition/paper-IV.md"
BAK = ".bak-wt171"


def _load(name):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(REPO, "scripts", name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


wt148 = _load("wt148_promise_sweep")
wt160 = _load("wt160_bare_pointer_sweep")
wt163 = _load("wt163_pointer_vocabulary")

# --------------------------------------------------------------------------------------
# The six repairs. Anchors are matched with EVERY space widened to \s+, because an anchor
# string spans hard-wrapped line breaks in the file and a substring test true of the
# rendered text is false of the bytes -- wealthTensor-87 lesson (vii).
# --------------------------------------------------------------------------------------
REPAIRS = [
    ("R1 re-target",
     "in the repository named in the data-availability statement.",
     "in the repository named in §7."),

    ("R2 re-target",
     "This is verified to machine precision in the implementation rather than assumed, "
     "so that no result below can be an artefact of the levy quietly changing the growth rate.",
     "This is\n"
     "verified to machine precision rather than assumed: `test_the_levy_is_a_pure_transfer` in\n"
     "`tests/test_redistribution.py` holds the implementation's reported `transfer_error` "
     "below 1e-12,\n"
     "so that no result below can be an artefact of the levy quietly changing the growth rate."),

    ("R3 re-target",
     "The budget is visible in the third column and is not a fitted relationship:",
     "The budget is the table's κ column and is not a fitted relationship:"),

    ("R4 replace",
     "save §3.4's Gini ceiling, which is arithmetic in *N* and is printed by neither —",
     "save the five quantities §7 enumerates, which no command\n"
     "   prints —"),

    ("R5 replace",
     "and except §3.4's Gini ceiling, which is arithmetic in *N* and is printed by neither.",
     "and except five\n"
     "  quantities neither command prints in any precision: §3.4's Gini ceiling "
     "(*N*−1)/*N* = 0.99875,\n"
     "  which is arithmetic in *N*; §3.4's 0.90 top-decile criterion, which is a chosen "
     "threshold and\n"
     "  not an output; and three differences of numbers both commands do print — "
     "§3.2's 0.035\n"
     "  periodicity span, and §3.4's 0.103 Gini gap and 0.039 top-decile margin."),

    ("R6 replace",
     "save five closed-form quantities: the four the next bullet names, and §3.4's Gini "
     "ceiling (*N*−1)/*N* = 0.99875, which is arithmetic in *N* and is printed by no "
     "command here.",
     "save the four closed-form quantities the next bullet names and §3.4's Gini ceiling\n"
     "(*N*−1)/*N* = 0.99875, which is arithmetic in *N* and is printed by no command here."),
]

# The three bare targets that must be GONE afterwards, as they read before the repair.
GONE = [
    "named in the data-availability statement",
    "verified to machine precision in the implementation",
    "visible in the third column",
]

# The promise ids this repair must retire and mint. Written BEFORE the run, from a dry run
# on a scratch copy, so a surprise here is a real surprise and not a rationalisation.
RETIRED = ["dfd41f5263", "c9a565b3fe", "1cbe31f16c"]
MINTED = ["6914c59765", "7b6a20118e", "bc1f66a253", "b9dea67210", "5f6d5c4fb9"]


def _rx(anchor: str) -> re.Pattern:
    return re.compile(r"\s+".join(re.escape(w) for w in anchor.split()))


def _read(path):
    with open(os.path.join(REPO, path), encoding="utf-8") as fh:
        return fh.read()


def _write(path, text):
    with open(os.path.join(REPO, path), "w", encoding="utf-8") as fh:
        fh.write(text)


def _flat(t):
    return re.sub(r"\s+", " ", t)


def _flags(mod):
    """(verb, target) pairs the sweep flags, over the papers IT reads -- not over ours."""
    out = []
    for p in mod.PAPERS:
        out += [(f["verb"], f["target"]) for f in mod.sweep_text(_read(p), p)[0]]
    return sorted(out)


def _wt169_payload():
    """wt169's whole measurement as JSON, so E7 compares the numbers and not the exit code."""
    r = subprocess.run(
        [sys.executable, "scripts/wt169_pointer_groundtruth_heldout.py", "--json"],
        cwd=REPO, capture_output=True, text=True)
    return r.returncode, r.stdout


def _pids(path):
    import pathlib
    return {row["pid"] for row in wt148.emit(pathlib.Path(os.path.join(REPO, path)))}


def _defensive(path):
    """(rc, json text). `defensive_count.py --json` takes a PATH, not a dash."""
    import tempfile
    with tempfile.NamedTemporaryFile("r", suffix=".json", delete=False) as fh:
        tmp = fh.name
    r = subprocess.run([sys.executable, "scripts/defensive_count.py", path, "--json", tmp],
                       cwd=REPO, capture_output=True, text=True)
    try:
        with open(tmp, encoding="utf-8") as fh:
            body = fh.read()
    except OSError:
        body = ""
    os.unlink(tmp)
    return r.returncode, body


def main():
    full = os.path.join(REPO, PII)

    # ---- E1 PRE-CONDITION: every anchor matches exactly once, before anything moves ----
    pre = []
    for tag, old, _new in REPAIRS:
        n = len(_rx(old).findall(_read(PII)))
        pre.append((tag.split()[0], n))
        if n != 1:
            print(f"wt171: PRE-CONDITION FAILED - {tag} anchor matches {n} time(s), expected 1",
                  file=sys.stderr)
            return 2
    print("  [ok  ] E1 PRE      each of the six anchors matches exactly once - "
          + ", ".join(f"{t}:{n}" for t, n in pre))

    before160 = _flags(wt160)
    before163 = _flags(wt163)
    before169 = _wt169_payload()
    before_pids = _pids(PII)
    other_before = {p: _read(p) for p in (PIII, PIV)}

    shutil.copyfile(full, full + BAK)

    try:
        for tag, old, new in REPAIRS:
            text, n = _rx(old).subn(lambda _m, _n=new: _n, _read(PII), count=1)
            if n != 1:
                raise RuntimeError(f"{tag}: substitution applied {n} times")
            _write(PII, text)

        t = _flat(_read(PII))
        checks = []

        # --- E2 POSITIVE: the three bare targets are gone, whitespace-flattened ---------
        left = [g for g in GONE if g in t]
        checks.append(("E2", "POSITIVE", "all three bare pointer targets are gone",
                       not left, f"still present: {left}"))

        # --- E3 POSITIVE: each now names a handle a reader can open --------------------
        r1 = "in the repository named in §7." in t
        r2 = ("`test_the_levy_is_a_pure_transfer` in `tests/test_redistribution.py` holds "
              "the implementation's reported `transfer_error` below 1e-12") in t
        r3 = "The budget is the table's κ column" in t
        checks.append(("E3", "POSITIVE", "R1/R2/R3 each name a followable handle",
                       r1 and r2 and r3, f"R1={r1} R2={r2} R3={r3}"))

        # --- E4 POSITIVE: R1 is now the SAME construction its two sibling papers use ----
        sib = [(n, "in the repository named in §" in _flat(_read(p)))
               for n, p in (("III", PIII), ("IV", PIV))]
        checks.append(("E4", "POSITIVE",
                       "R1 matches Papers III and IV verbatim in construction",
                       r1 and all(v for _n, v in sib), f"{sib} + II={r1}"))

        # --- E5 NEGATIVE: wt160's flag set is bit-identical -- and MUST be, because it
        #     has never read Paper II. Both halves asserted, so the green line is honest.
        after160 = _flags(wt160)
        blind160 = PII not in wt160.PAPERS
        checks.append(("E5", "NEGATIVE",
                       "wt160's flag set UNCHANGED, and wt160 does not read Paper II at all",
                       after160 == before160 and blind160,
                       f"identical={after160 == before160} papers={ [p.split('/')[-1] for p in wt160.PAPERS] }"))

        # --- E6 NEGATIVE: same for wt163's widened vocabulary --------------------------
        after163 = _flags(wt163)
        blind163 = PII not in wt163.PAPERS
        checks.append(("E6", "NEGATIVE",
                       "wt163's flag set UNCHANGED, and wt163 does not read Paper II either",
                       after163 == before163 and blind163,
                       f"identical={after163 == before163} papers={ [p.split('/')[-1] for p in wt163.PAPERS] }"))

        # --- E7 NEGATIVE: wt169's revision pin, exercised by a real repair for the first
        #     time. Byte-identical payload, and the reason: it reads only at 83db4d5.
        after169 = _wt169_payload()
        pinned = _load("wt169_pointer_groundtruth_heldout").REV == "83db4d5"
        checks.append(("E7", "NEGATIVE",
                       "wt169's ENTIRE payload is byte-identical across the repair "
                       "(the pin cannot fire: it reads only at 83db4d5)",
                       after169 == before169 and after169[0] == 0 and pinned,
                       f"rc {before169[0]}->{after169[0]} identical={after169 == before169}"))

        # --- E8 POSITIVE: section 7's clause now names every excepted quantity ----------
        named = [x for x in ("0.99875", "0.90", "0.035", "0.103", "0.039")
                 if x in t.split("The two commands are named separately")[0].split(
                     "**Regenerate every number in §3:**")[-1]]
        checks.append(("E8", "POSITIVE",
                       "section 7's bullet names all five unregenerated quantities",
                       len(named) == 5, f"named: {named}"))

        # --- E9 NEGATIVE: the numeral collision R6 removes is really gone ---------------
        checks.append(("E9", "NEGATIVE",
                       "'save five closed-form quantities' is gone (two adjacent, different fives)",
                       "save five closed-form quantities" not in t, "still present"))

        # --- E10 NEGATIVE: no hedge added. Paper II's committed baseline is 0. ----------
        drc, dout = _defensive(PII)
        try:
            dcount = json.loads(dout)["totals"]["invariant"]
        except Exception:
            dcount = -1
        checks.append(("E10", "NEGATIVE",
                       "defensive-sentence count outside Limitations is still 0 (charter G-COACH-3)",
                       drc == 0 and dcount == 0, f"rc={drc} invariant={dcount}"))

        # --- E11 NEGATIVE: no other manuscript moved -----------------------------------
        unchanged = all(_read(p) == other_before[p] for p in (PIII, PIV))
        checks.append(("E11", "NEGATIVE", "Papers III and IV are byte-identical",
                       unchanged, "a sibling manuscript changed"))

        # --- E12 POSITIVE: the promise delta is EXACTLY what was predicted pre-run ------
        after_pids = _pids(PII)
        gone = sorted(before_pids - after_pids)
        new = sorted(after_pids - before_pids)
        checks.append(("E12", "POSITIVE",
                       "exactly the predicted 3 promises retired and 5 minted (15 -> 17)",
                       gone == sorted(RETIRED) and new == sorted(MINTED)
                       and len(after_pids) == 17,
                       f"retired={gone} minted={new} total={len(after_pids)}"))

        # --- E13 NEGATIVE: the Gini ceiling is still stated, in both places -------------
        checks.append(("E13", "NEGATIVE",
                       "the ceiling (*N*-1)/*N* = 0.99875 still appears twice - narrowed, not cut",
                       t.count("0.99875") >= 2, f"count={t.count('0.99875')}"))

        # --- E14 NEGATIVE: the repair does not leave a line longer than the file's own
        #     widest pre-existing line. A ragged reflow is a diff nobody can read.
        was = max(len(l) for l in _read(PII + BAK).split("\n"))
        now = max(len(l) for l in _read(PII).split("\n"))
        checks.append(("E14", "NEGATIVE",
                       "no line is longer than the widest line the file already had",
                       now <= was, f"widest was {was}, now {now}"))

        print()
        bad = 0
        for tag, kind, what, ok, detail in checks:
            print(f"  [{'ok  ' if ok else 'FAIL'}] {tag} {kind} {what}"
                  + ("" if ok else f" - {detail}"))
            bad += not ok
        if bad:
            raise RuntimeError(f"{bad} post-condition(s) failed")

    except Exception as exc:                                    # noqa: BLE001
        shutil.copyfile(full + BAK, full)
        print(f"\nwt171: ROLLED BACK - {exc}", file=sys.stderr)
        return 1

    print(f"\nwt171: six repairs applied to {PII}; backup at {PII}{BAK}")
    print("       3 promises retired, 5 minted -- wt148 is RED until wt172_tsv runs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
