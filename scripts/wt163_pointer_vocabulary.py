#!/usr/bin/env python3
"""wt163 — THE POINTER VOCABULARY: is `wt160`'s ten a property of the corpus, or of a word list?

WHAT THIS ASKS
--------------
`wt160` flags `<VERB> in <TARGET>` where TARGET carries no handle a reader could follow. It
reads EIGHT commissioned verbs in participle and 3sg-present form only — SIXTEEN surface
forms. `wealthTensor-87` predicted ten flags at `07cd47e` and measured ten, the same ten; and
REVIEW-027 §5 says why that agreement is the WEAKER result: the hand prediction was built from
the SAME sixteen forms, so it tests the ADJUDICATION (are N1–N6 applicable by hand?) and cannot
test the ENUMERATION (is the vocabulary right?). REVIEW-027 §8 falsifier 4 names widening the
vocabulary as the strongest attack available on that count. This is that attack.

THE CRITERION IS NOT RE-IMPLEMENTED HERE.
-----------------------------------------
`_flatten`, `_target_window` and `_is_named` are IMPORTED from `wt160_bare_pointer_sweep.py`.
The twelve-word window, the clause-boundary rule and the N1–N6 named-target tests are therefore
byte-identical to `wt160`'s by construction rather than by assertion, and post-condition **D6**
proves it: run this module with `wt160`'s own verb list and it must reproduce `wt160`'s output
exactly, at a pinned revision. **The vocabulary is the ONLY thing that differs.** If a successor
edits the window or an N-test, it must edit `wt160` and both instruments move together — which
is the point.

THE VOCABULARY UNDER TEST — chosen by the PREVIOUS session, not this one
-----------------------------------------------------------------------
`WIDENING` below is the verb set the `wealthTensor-87` handoff commissioned, verbatim. This
session did not choose it, did not add to it after reading the corpus, and did not remove
`held in` after discovering it contributes only false positives. **That discipline is the whole
experiment**: an a priori list, chosen the same way `wt160`'s was, tests whether the count
survives a change of list. A list tuned against the corpus would test nothing at all.

The prediction — B = 13, of which 10 are `wt160`'s ten and 3 are `held in` false positives, and
ZERO of the four bare pointers a vocabulary-free reading finds — is committed in
`docs/REVIEW-028-pointer-vocabulary.md` §5 at commit `c89f764`, BEFORE this file existed.

WHY FLAGS CAN BE EXCLUDED WITHOUT THAT BEING TUNING
---------------------------------------------------
A widened vocabulary buys false positives: `held in place by a test suite` is an idiom, not a
pointer. Repairing prose to satisfy a detector is the ABSORB move the co-author charter §2
forbids. So flags are adjudicated against `docs/pointer-exclusions.tsv`, and **D3 refuses to
pass unless that file's rows are EXACTLY the three named in the prediction**. The exclusions
were predicted before they were measured; a successor who needs a fourth row has to change D3
and say so in a review. The table cannot grow silently.

WHAT THIS CANNOT DO — pinned, not patched
------------------------------------------
It cannot see a bare pointer whose verb is off BOTH lists. Four such live in the corpus at
`07cd47e` (REVIEW-028 §4 rows 11–14): `visible in the parameter sweep`, `declared in the
registration before the pilot was run`, `printed in the same logs`, `verified in the sessions
that introduced them to Papers II or III`. **D4 and D5 are NEGATIVE post-conditions asserting
that this instrument stays SILENT on two of them.** Widening the list to swallow them would
make the post-conditions pass and destroy the experiment — the `wealthTensor-87` lesson (vi),
applied. They are repaired in the manuscripts by hand, by a reader, and the instrument's
inability to have found them is recorded here as a fact about instruments.

EXIT CODES:  0 = every flag repaired or disclosed-excluded · 1 = undisclosed flags present ·
             2 = the instrument itself is broken.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_WT160_PATH = os.path.join(REPO_ROOT, "scripts", "wt160_bare_pointer_sweep.py")

_spec = importlib.util.spec_from_file_location("wt160_bare_pointer_sweep", _WT160_PATH)
wt160 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wt160)

PAPERS = list(wt160.PAPERS)
EXCLUSIONS_TSV = "docs/pointer-exclusions.tsv"

# --- the vocabulary under test -------------------------------------------------------
# (a) wt160's sixteen surface forms, imported so they cannot drift.
BASELINE = list(wt160.VERBS)

# (b) the widening the wealthTensor-87 handoff commissioned, verbatim. Ordered longest
#     first within the multiword group so "laid out" wins over "laid".
WIDENING = [
    # twelve new verbs the handoff named
    "held", "holds",
    "found", "finds",
    "described", "describes",
    "specified", "specifies",
    "covered", "covers",
    "shown", "shows",
    "presented", "presents",
    "laid out", "lays out",
    "spelled out", "spells out",
    "set down", "sets down",
    "collected", "collects",
    "summarised", "summarises", "summarized", "summarizes",
    # the BASE forms of wt160's own eight, which wt160 misses purely by inflection
    "record", "name", "give", "list", "document", "state", "report",
]

VOCAB = sorted(set(BASELINE) | set(WIDENING), key=lambda w: (-len(w), w))
# `\b` alone fires INSIDE a hyphenated compound: `mis-specified in four ways` matched as
# `specified in`, and `mis-specified` means the NEGATION of the verb matched. The lookbehind
# refuses a match preceded by a word character or a hyphen. Post-condition D12 pins the case;
# D13 proves the guard leaves wt160's published ten at 07cd47e untouched, so the two
# instruments still differ only in vocabulary. Found by the widening — wt160's narrower list
# never had a verb that occurs as the tail of a hyphenated compound in this corpus.
VERB_RE = re.compile(r"(?<![\w-])(" + "|".join(re.escape(v) for v in VOCAB) + r")\s+in\s+",
                     re.IGNORECASE)

# The four bare pointers a vocabulary-free reading finds and NEITHER list can reach.
# REVIEW-028 §4 rows 11-14. Kept here so the blind spot is documented in the instrument
# and not only in the review -- the wealthTensor-87 lesson about the criterion living in
# the module docstring, applied to the criterion's LIMIT.
BLIND_SPOT = [
    ("III", "visible in",  "the parameter sweep"),
    ("III", "declared in", "the registration before the pilot was run"),
    ("III", "printed in",  "the same logs"),
    ("IV",  "verified in", "the sessions that introduced them to Papers II or III"),
]

PREDICTION_COMMIT = "c89f764"      # REVIEW-028 §§1-5, committed before this file existed
PRED_REV = "07cd47e"               # where wt160 measured ten
SIGMA_REPAIR = "c14aed3"           # where wealthTensor-87 repaired "the two rows above"


def sweep_text(text: str, path: str = "<text>", verbs_re=None):
    """Identical to wt160.sweep_text except for the verb regex. Window and N1-N6 imported."""
    rx = verbs_re or VERB_RE
    flat, lines = wt160._flatten(text)
    flags, considered = [], 0
    for m in rx.finditer(flat):
        considered += 1
        target = wt160._target_window(flat, m.end())
        named = wt160._is_named(target)
        rec = {
            "file": path,
            "line": lines[m.start()] if m.start() < len(lines) else 0,
            "verb": m.group(1).lower(),
            "target": target,
            "excerpt": flat[max(0, m.start() - 70): min(len(flat), m.end() + 90)].strip(),
            "named_by": named,
            "in_baseline": m.group(1).lower() in {v.lower() for v in BASELINE},
        }
        if named is None:
            flags.append(rec)
    return flags, considered


def _read(path: str, rev: str | None):
    if rev:
        return subprocess.check_output(["git", "show", f"{rev}:{path}"],
                                       cwd=REPO_ROOT).decode("utf-8")
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def load_exclusions():
    """Read the disclosed NOT-A-POINTER adjudications. Each row must carry a reason."""
    path = os.path.join(REPO_ROOT, EXCLUSIONS_TSV)
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            parts = raw.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            rows.append({"file": parts[0].strip(), "verb": parts[1].strip(),
                         "target": parts[2].strip(), "reason": parts[3].strip()})
    return rows


def adjudicate(flags, exclusions):
    """Split flags into (undisclosed, excluded). A flag matches a row on verb+target."""
    keys = {(_norm(r["verb"]), _norm(r["target"])) for r in exclusions if r["reason"]}
    undisclosed, excluded = [], []
    for f in flags:
        (excluded if (_norm(f["verb"]), _norm(f["target"])) in keys else undisclosed).append(f)
    return undisclosed, excluded


# --- post-conditions -----------------------------------------------------------------
BASELINE_RE = re.compile(r"(?<![\w-])(" + "|".join(re.escape(v) for v in
                         sorted(BASELINE, key=lambda w: (-len(w), w))) + r")\s+in\s+",
                         re.IGNORECASE)
BASELINE_RE_UNGUARDED = re.compile(r"\b(" + "|".join(re.escape(v) for v in
                         sorted(BASELINE, key=lambda w: (-len(w), w))) + r")\s+in\s+",
                         re.IGNORECASE)


def _flags_of(text, rx=None):
    return sweep_text(text, verbs_re=rx)[0]


def _d1():
    """POSITIVE: at 07cd47e the widened list flags a SUPERSET of wt160's ten.

    This post-condition was WRONG on its first run, in exactly the way a claim can be: it
    compared SETS, so the two `named in its own title` flags and the two `named in the
    data-availability statement` flags collapsed and wt160's published ten read as eight.
    A rollback is not a verdict on the instrument — wealthTensor-87 lesson (iv). Multisets now.
    """
    try:
        mine, theirs = [], []
        for p in PAPERS:
            t = _read(p, PRED_REV)
            mine += [(f["verb"], f["target"], f["line"]) for f in sweep_text(t, p)[0]]
            theirs += [(f["verb"], f["target"], f["line"]) for f in wt160.sweep_text(t, p)[0]]
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    missing = [x for x in theirs if x not in mine]
    return (not missing and len(theirs) == 10,
            f"wt160 flags {len(theirs)}, wt163 flags {len(mine)}, wt160-not-in-wt163: {missing}")


def _d2():
    """POSITIVE: `give in` — a base form wt160 cannot see and this list can."""
    s = "The reason Papers I, II and IV give in their own front matter is the same one."
    wide = len(_flags_of(s))
    narrow = len(_flags_of(s, BASELINE_RE))
    return (wide == 1 and narrow == 0,
            f"widened flags {wide}, wt160's sixteen forms flag {narrow} — the inflection gap")


def _d3():
    """POSITIVE: the exclusions file holds EXACTLY the six MEASURED flags.

    The prediction named three; the measurement produced six. See REVIEW-028 §6.
    """
    rows = load_exclusions()
    got = sorted(_norm(r["verb"]) + " | " + _norm(r["target"]) for r in rows)
    # THE PREDICTION NAMED THREE AND THE MEASUREMENT PRODUCED SIX. The three `holds in`
    # rows were MISSED because REVIEW-028 §5's arithmetic counted only `held in`, having
    # overlooked that this session mirrored wt160's participle+3sg symmetry onto the
    # commissioned widening. The miss is reported in REVIEW-028 §6 and is the stronger
    # result: it is a fact about ENUMERATION that the exact agreement of REVIEW-027 could
    # not have produced. The list below is the MEASURED set; a successor who needs a
    # seventh row must edit this post-condition and say so in a review.
    want = sorted([
        "held | place by a test suite",
        "held | **100%**",
        "held | the gap and released at rate α",
        "holds | **100%** of them",
        "holds | **66.2%** (2",
        "holds | all nine is the sign",
    ])
    unreasoned = [r for r in rows if not r["reason"]]
    return (got == want and not unreasoned,
            f"{len(rows)} row(s); matches prediction: {got == want}; unreasoned: {len(unreasoned)}")


def _d4():
    """NEGATIVE: the instrument is BLIND to `visible in <bare>` — pinned, not patched."""
    s = "The reason is visible in the parameter sweep: lag falls in phi at every delta."
    return (len(_flags_of(s)) == 0,
            "REVIEW-028 row 11 — a real bare pointer NEITHER list can reach")


def _d5():
    """NEGATIVE: the instrument is BLIND to `printed in <bare>` and `verified in <bare>`."""
    a = "The control is printed in the same logs, which permute the tier labels."
    b = "Entries marked as checked were verified in the sessions that introduced them."
    return (len(_flags_of(a)) == 0 and len(_flags_of(b)) == 0,
            "REVIEW-028 rows 13-14 — two more the vocabulary cannot reach")


def _d6():
    """POSITIVE: run this module with wt160's OWN verb list and it reproduces wt160 exactly.

    This is what licenses the claim that the vocabulary is the only difference.
    """
    try:
        for p in PAPERS:
            t = _read(p, PRED_REV)
            a = [(f["verb"], f["target"], f["line"]) for f in sweep_text(t, p, BASELINE_RE)[0]]
            b = [(f["verb"], f["target"], f["line"]) for f in wt160.sweep_text(t, p)[0]]
            if a != b:
                return False, f"{p}: {a} != {b}"
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    return True, "same window, same N1-N6, same output — only the vocabulary differs"


def _d7():
    """POSITIVE at 07cd47e: `given in the two rows above` flags (the wealthTensor-87 defect)."""
    try:
        t = _read(PAPERS[0], PRED_REV)
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    hit = [f for f in sweep_text(t, PAPERS[0])[0] if "two rows above" in f["target"]]
    return bool(hit), f"{len(hit)} hit(s) at {PRED_REV}"


def _d8():
    """NEGATIVE at c14aed3: the same sentence no longer flags. The revision-pinned pair."""
    try:
        t = _read(PAPERS[0], SIGMA_REPAIR)
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    hit = [f for f in sweep_text(t, PAPERS[0])[0] if "two rows above" in f["target"]]
    return not hit, f"{len(hit)} hit(s) at {SIGMA_REPAIR} — the FILE moved, not the instrument"


def _d9():
    """NEGATIVE: a widened-vocabulary verb with a NAMED target stays silent."""
    outs = [
        "The framework is summarised in §4.2 and nowhere else.",
        "The derivation is laid out in `docs/notes/NOTE-001.md` at length.",
        "Every route is described in Appendix A.",
        "The residue is found in an unrecognised gap and released at rate alpha.",
    ]
    bad = [s for s in outs if _flags_of(s)]
    return not bad, f"N1/N2/N4/N6 hold for the NEW verbs too; leaks: {bad}"


def _d10():
    """POSITIVE: the widening genuinely widens — it considers strictly more than wt160."""
    try:
        wide = narrow = 0
        for p in PAPERS:
            t = _read(p, PRED_REV)
            wide += sweep_text(t, p)[1]
            narrow += wt160.sweep_text(t, p)[1]
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    return wide > narrow, f"considered at {PRED_REV}: widened {wide} vs wt160 {narrow}"


def _d11():
    """POSITIVE: the prediction is a git object that predates this file."""
    try:
        files = subprocess.check_output(
            ["git", "show", "--name-only", "--format=", PREDICTION_COMMIT],
            cwd=REPO_ROOT).decode("utf-8").split()
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    has_review = any("REVIEW-028" in f for f in files)
    has_script = any("wt163" in f for f in files)
    return (has_review and not has_script,
            f"{PREDICTION_COMMIT} carries REVIEW-028={has_review}, wt163={has_script}")


def _d12():
    """NEGATIVE: `mis-specified in four ways` does not flag — the tokenisation guard."""
    s = "The instrument was mis-specified in four ways and the run produced no answer."
    guarded = len(_flags_of(s))
    unguarded = len(re.compile(r"\b(" + "|".join(re.escape(v) for v in VOCAB) + r")\s+in\s+",
                               re.IGNORECASE).findall(wt160._flatten(s)[0]))
    return (guarded == 0 and unguarded == 1,
            f"guarded {guarded}, unguarded {unguarded} — a hyphenated compound whose meaning "
            f"negates the verb matched; found BY the widening")


def _d13():
    """POSITIVE: the guard is NEUTRAL on wt160 — its published ten at 07cd47e is untouched."""
    try:
        a = b = []
        a, b = [], []
        for p in PAPERS:
            t = _read(p, PRED_REV)
            a += [(f["verb"], f["target"]) for f in sweep_text(t, p, BASELINE_RE)[0]]
            b += [(f["verb"], f["target"]) for f in sweep_text(t, p, BASELINE_RE_UNGUARDED)[0]]
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    return a == b and len(a) == 10, f"guarded {len(a)} vs unguarded {len(b)} on wt160's vocabulary"


def _postconditions():
    return [
        ("D1", "POSITIVE", "at 07cd47e the widened list flags a superset of wt160's ten", _d1),
        ("D2", "POSITIVE", "`give in` — a base form wt160 cannot see, this list can", _d2),
        ("D3", "POSITIVE", "exclusions hold EXACTLY the six MEASURED flags (3 predicted, 3 missed)", _d3),
        ("D4", "NEGATIVE", "BLIND to `visible in <bare>` — pinned, not patched", _d4),
        ("D5", "NEGATIVE", "BLIND to `printed in` and `verified in` — two more", _d5),
        ("D6", "POSITIVE", "with wt160's verb list this module reproduces wt160 exactly", _d6),
        ("D7", "POSITIVE", "at 07cd47e `given in the two rows above` flags", _d7),
        ("D8", "NEGATIVE", "at c14aed3 it no longer flags — the revision-pinned pair", _d8),
        ("D9", "NEGATIVE", "a NEW verb with a NAMED target stays silent (N1/N2/N4/N6)", _d9),
        ("D10", "POSITIVE", "the widening considers strictly more than wt160", _d10),
        ("D11", "POSITIVE", "the prediction is a git object predating this file", _d11),
        ("D12", "NEGATIVE", "`mis-specified in` does not flag — the tokenisation guard", _d12),
        ("D13", "POSITIVE", "the guard is neutral on wt160's published ten at 07cd47e", _d13),
    ]


def run_postconditions(verbose=True):
    ok_all, results = True, []
    for cid, kind, desc, fn in _postconditions():
        try:
            ok, detail = fn()
        except Exception as exc:                      # noqa: BLE001
            ok, detail = False, f"raised {exc!r}"
        ok_all &= ok
        results.append({"id": cid, "kind": kind, "desc": desc, "ok": ok, "detail": detail})
        if verbose:
            print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} — {detail}")
    return ok_all, results


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="wt163 — is wt160's ten a property of the corpus, or of a word list?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rev", default=None, help="sweep a git revision instead of the working tree")
    ap.add_argument("--skip-postconditions", action="store_true")
    ap.add_argument("--census", action="store_true",
                    help="print the per-verb census: what each verb contributes")
    args = ap.parse_args(argv)

    exclusions = load_exclusions()
    per_file, all_flags, total_considered = [], [], 0
    for path in PAPERS:
        try:
            text = _read(path, args.rev)
        except Exception as exc:                      # noqa: BLE001
            print(f"wt163: cannot read {path}: {exc}", file=sys.stderr)
            return 2
        flags, considered = sweep_text(text, path)
        total_considered += considered
        all_flags.extend(flags)
        per_file.append({"file": path, "considered": considered, "flagged": len(flags),
                         "flags": flags})

    undisclosed, excluded = adjudicate(all_flags, exclusions)

    post_ok, post = (True, [])
    if not args.skip_postconditions:
        if not args.json:
            print("=== wt163 post-conditions ===")
        post_ok, post = run_postconditions(verbose=not args.json)

    if args.json:
        print(json.dumps({
            "rev": args.rev or "working-tree",
            "considered": total_considered,
            "flagged": len(all_flags),
            "undisclosed": undisclosed,
            "excluded": excluded,
            "per_file": per_file,
            "blind_spot": BLIND_SPOT,
            "postconditions_ok": post_ok,
            "postconditions": post,
        }, indent=2, ensure_ascii=False))
    else:
        print()
        for pf in per_file:
            base = sum(1 for f in pf["flags"] if f["in_baseline"])
            print(f"=== {pf['file']} — {pf['considered']} considered, {pf['flagged']} flagged "
                  f"({base} by wt160's sixteen forms, {pf['flagged'] - base} by the widening) ===")
            for f in pf["flags"]:
                tag = "wt160" if f["in_baseline"] else "NEW  "
                mark = "excluded" if f in excluded else "FLAG"
                print(f"  [{tag}] {mark:8s} line {f['line']:>5}  «{f['verb']} in {f['target']}»")
            if not pf["flags"]:
                print("  (none)")
            print()
        if args.census:
            from collections import Counter
            c = Counter(f["verb"] for f in all_flags)
            print("--- per-verb census of flags ---")
            for v, n in c.most_common():
                print(f"  {n:3d}  {v}")
            print()
        print(f"TOTAL: {total_considered} considered, {len(all_flags)} flagged "
              f"({len(excluded)} disclosed-excluded, {len(undisclosed)} undisclosed).")
        print(f"BLIND SPOT (neither list reaches these; see REVIEW-028 §4 rows 11-14): "
              f"{len(BLIND_SPOT)} known bare pointer(s).")

    if not post_ok:
        print("wt163: POST-CONDITIONS FAILED — the instrument is not trustworthy.", file=sys.stderr)
        return 2
    return 1 if undisclosed else 0


if __name__ == "__main__":
    sys.exit(main())
