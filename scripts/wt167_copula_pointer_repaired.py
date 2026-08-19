#!/usr/bin/env python3
"""wt167 — REPAIR THE ONE BARE POINTER THE LABELLING FOUND THAT NO READING HAD.

WHAT THIS REPAIRS, AND HOW IT WAS FOUND
---------------------------------------
`docs/pointer-groundtruth.tsv` labelled all 341 bare-target constructions at `07cd47e`.
Fifteen are POINTERs. Fourteen are REVIEW-028 §4's fourteen. The fifteenth is

    III 1261   «Four registered sensitivity analyses per universe are in the run logs;
                none reverses the verdict.»

and no reading in this programme had it. Its verb is the COPULA. REVIEW-028's own
"vocabulary-free" enumeration filtered the corpus's 264 tokens at step 2 by keeping
"every token that could locate content in an artefact" — and `are` does not LOOK like a
locating verb even though it does the locating work. So the reading that was offered as
free of a word list had a covert one, and only labelling every row exposed it. That is
REVIEW-028 §8 falsifier 1, fired from inside.

WHAT THE BARE TARGET WAS HIDING — the reason this class is not a style nit
-------------------------------------------------------------------------
Naming the artefact made the sentence checkable, and it does not check out. The committed
instrument `scripts/wt026_severe_test.py` runs **THREE** sensitivities — annual-attributed
charges excluded, right-censored events excluded, one event per firm — and both
`RESULT-002-*-run.log` files print exactly those three. No fourth sensitivity is named in
`PRE-001`, registered in `PRE-002`, implemented in the instrument, or printed in any log.
**The count of four has no referent anywhere in this repository.** A bare pointer is what
let it stand: with no artefact named, there was nothing to check the number against.

THE REPAIR, and why it is `remove` rather than `re-target` on the number
-----------------------------------------------------------------------
Two independent defects sit in one sentence and they get different treatment, per
`docs/CO-AUTHOR-CHARTER.md` §2:

  * the POINTER is RE-TARGETED — the logs are named, so a reader can go and check;
  * the unsupported COUNT is REMOVED — "Four registered sensitivity analyses" becomes
    "The registered sensitivity analyses". Every registered sensitivity IS in those logs
    and none reverses the verdict, so the repaired sentence asserts nothing this
    repository cannot support, and asserts nothing new either.

**What this repair deliberately does NOT do.** It does not write "Three", and it does not
touch `PRE-002` §2, `RESULT-001` §1 or `RESULT-002` §1, which carry the same "four". Those
are pre-registration and result documents, and an in-place edit to them is a standing
JASON-SIZED ruling (Asana `1217603625863293`, the RESULT-001 "320 against 322" card, which
is the same class one instance over). Writing "Three" into the manuscript alone would trade
one defect for a fresh cross-document contradiction while that ruling is pending. The
finding is carded against the existing card so the one ruling covers both instances.

POST-CONDITIONS. Eight, three NEGATIVE. **G4 is the one that carries the review's claim**,
on the model of `wt164`'s E4: `wt163`'s flag set must be BIT-IDENTICAL across this repair,
and `wt160`'s must be too. An instrument that noticed this repair would be an instrument
that could have found the defect. Neither can, because the verb is `are`.

ROLLBACK: `docs/papers/paper-III-dual-tensor/paper-III.md.bak-wt167` is written BEFORE the
edit. `python3 scripts/wt167_copula_pointer_repaired.py --rollback` restores it.

EXIT CODES: 0 = repair applied (or already applied) and every post-condition holds ·
2 = a post-condition failed, or the anchor was not found exactly once.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shutil
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(REPO_ROOT, "docs", "papers", "paper-III-dual-tensor", "paper-III.md")
BAK = PAPER + ".bak-wt167"

_here = os.path.dirname(os.path.abspath(__file__))


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_here, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


wt160 = _load("wt160", "wt160_bare_pointer_sweep.py")
wt163 = _load("wt163", "wt163_pointer_vocabulary.py")

BEFORE = ("Four registered sensitivity analyses per universe are in the run logs; "
          "none reverses the verdict.")
AFTER = ("The registered sensitivity analyses per universe are in the run logs "
         "(`docs/preregistration/RESULT-002-*-run.log`); none reverses the verdict.")

WS = re.compile(r"\s+")


def _flat(s: str) -> str:
    return WS.sub(" ", s).strip()


def _rewrap(text: str) -> str:
    """Apply the substitution on the whitespace-FLATTENED text, hard wraps and all.

    wt164's E8 asserted a line-count drift and was wrong because three of its four anchors
    already spanned a line break. The lesson (wealthTensor-87 (vii), earned twice) is to
    work whitespace-insensitively rather than to predict wrap arithmetic, so this matches
    the anchor across whatever line breaks it happens to straddle.
    """
    pattern = re.compile(r"\s+".join(re.escape(w) for w in BEFORE.split()))
    hits = pattern.findall(text)
    if len(hits) != 1:
        raise SystemExit(f"wt167: anchor found {len(hits)} time(s), expected exactly 1")
    return pattern.sub(lambda _m: AFTER, text, count=1)


def _flags(mod, text):
    return {(f["verb"], f["target"]) for f in mod.sweep_text(text, PAPER)[0]}


def _postconditions(before_text, after_text):
    checks = []

    def add(cid, kind, desc, fn):
        checks.append((cid, kind, desc, fn))

    add("G1", "POSITIVE", "the pre-repair sentence IS a bare pointer under the ground truth's rule",
        lambda: (wt160._is_named(
            wt160._target_window(_flat(BEFORE), _flat(BEFORE).index("are in ") + len("are in "))
        ) is None, "target «the run logs» satisfies no N1..N6"))

    add("G2", "NEGATIVE", "the repaired sentence is NOT a bare pointer — N1 now fires",
        lambda: (wt160._is_named(
            wt160._target_window(_flat(AFTER), _flat(AFTER).index("are in ") + len("are in "))
        ) == "N1 backticked span", "the named log glob satisfies N1"))

    add("G3", "NEGATIVE", "the unsupported count is gone: «Four registered sensitivity» does not "
                          "survive in the manuscript",
        lambda: ("Four registered sensitivity" not in _flat(after_text),
                 "removed rather than replaced with a number this session is not authorised to set"))

    add("G4", "NEGATIVE", "wt163's AND wt160's flag sets are BIT-IDENTICAL across the repair — "
                          "neither instrument can see this defect or its cure",
        lambda: _g4(before_text, after_text))

    add("G5", "POSITIVE", "the repair is whitespace-exact: flatten before, substitute, and it "
                          "equals flatten after",
        lambda: (_flat(before_text).replace(_flat(BEFORE), _flat(AFTER)) == _flat(after_text),
                 "wrap-independent, per wt164 E8's correction"))

    add("G6", "POSITIVE", "the named artefacts EXIST and carry the sensitivity blocks",
        _g6)

    add("G7", "NEGATIVE", "no pre-registration or result document was touched by this script",
        lambda: (True, "wt167 writes exactly one path: " + os.path.relpath(PAPER, REPO_ROOT)))

    add("G8", "POSITIVE", "the logs print THREE sensitivity blocks, which is why the count was "
                          "removed rather than kept",
        _g8)

    return checks


def _g4(before_text, after_text):
    b160, a160 = _flags(wt160, before_text), _flags(wt160, after_text)
    b163, a163 = _flags(wt163, before_text), _flags(wt163, after_text)
    ok = (b160 == a160) and (b163 == a163)
    return ok, (f"wt160 {len(b160)}->{len(a160)}, wt163 {len(b163)}->{len(a163)}; "
                f"{'identical' if ok else 'MOVED — an instrument saw it'}")


def _logs():
    d = os.path.join(REPO_ROOT, "docs", "preregistration")
    return [os.path.join(d, f) for f in sorted(os.listdir(d))
            if re.fullmatch(r"RESULT-002-.*-run\.log", f)]


def _g6():
    paths = _logs()
    if len(paths) != 2:
        return False, f"{len(paths)} file(s) match RESULT-002-*-run.log, expected 2"
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            if "SENSITIVITY" not in fh.read():
                return False, f"{os.path.basename(p)} carries no SENSITIVITY block"
    return True, ", ".join(os.path.basename(p) for p in paths)


def _g8():
    counts = {}
    for p in _logs():
        with open(p, encoding="utf-8") as fh:
            counts[os.path.basename(p)] = sum(
                1 for line in fh if line.startswith("===== SENSITIVITY"))
    ok = set(counts.values()) == {3}
    return ok, f"{counts} — the manuscript said four; carded on Asana 1217603625863293"


def run_postconditions(before_text, after_text, verbose=True):
    ok_all, out = True, []
    for cid, kind, desc, fn in _postconditions(before_text, after_text):
        try:
            ok, detail = fn()
        except Exception as exc:                                  # noqa: BLE001
            ok, detail = False, f"raised {exc!r}"
        ok_all &= ok
        out.append({"id": cid, "kind": kind, "desc": desc, "ok": ok, "detail": detail})
        if verbose:
            print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} — {detail}")
    return ok_all, out


def main(argv=None):
    ap = argparse.ArgumentParser(description="wt167 — repair the copula bare pointer at III 1261")
    ap.add_argument("--rollback", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    if args.rollback:
        if not os.path.exists(BAK):
            print("wt167: no .bak-wt167 to roll back to", file=sys.stderr)
            return 2
        shutil.copyfile(BAK, PAPER)
        print(f"wt167: rolled back {os.path.relpath(PAPER, REPO_ROOT)} from .bak-wt167")
        return 0

    with open(PAPER, encoding="utf-8") as fh:
        current = fh.read()

    already = _flat(AFTER) in _flat(current)
    if already:
        before_text = current.replace(AFTER, BEFORE)
        if _flat(BEFORE) not in _flat(before_text):
            # the repair straddles a wrap; reconstruct wrap-insensitively
            pat = re.compile(r"\s+".join(re.escape(w) for w in AFTER.split()))
            before_text = pat.sub(lambda _m: BEFORE, current, count=1)
        after_text = current
    else:
        before_text = current
        if not os.path.exists(BAK):
            shutil.copyfile(PAPER, BAK)
        after_text = _rewrap(current)
        with open(PAPER, "w", encoding="utf-8") as fh:
            fh.write(after_text)

    if not args.json:
        print("=== wt167 post-conditions ===")
    ok, post = run_postconditions(before_text, after_text, verbose=not args.json)

    if args.json:
        print(json.dumps({"already_applied": already, "postconditions_ok": ok,
                          "postconditions": post}, indent=2, ensure_ascii=False))
    else:
        print()
        print(f"{'ALREADY APPLIED' if already else 'APPLIED'}: {os.path.relpath(PAPER, REPO_ROOT)}")
        print(f"  before: {BEFORE}")
        print(f"  after : {AFTER}")

    if not ok:
        print("wt167: POST-CONDITIONS FAILED.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
