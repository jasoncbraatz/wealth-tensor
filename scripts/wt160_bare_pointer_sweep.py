#!/usr/bin/env python3
"""wt160 — THE BARE-POINTER SWEEP.

WHAT THIS ASKS, AND WHY NEITHER EXISTING SWEEP ASKS IT
------------------------------------------------------
`wt133` resolves `§N.M` references and reference entries. `wt156` reads the evidence
column of `docs/promises-adjudicated.tsv`. `wt148` emits promises about NAMED artefacts.
All three are blind, BY CONSTRUCTION, to a sentence that says

    "Three post-hoc conjectures ... are recorded in the repository's working notes."

because the pointer's target is a BARE NOUN PHRASE. There is no path to resolve, no
section number to check, no artefact name to look up. The reader supplies the referent
silently and does not notice having done it — which is exactly how `wealthTensor-83`'s
III-2 stood in Paper III until a human read it. (`wealthTensor-86` found the same defect
one level out, in the TSV's own evidence column: `the script` and `the module` are
pronouns.)

THE CRITERION (fixed before the count was predicted; see docs/REVIEW-027)
------------------------------------------------------------------------
Over `paper-III.md` and `paper-IV.md`, with all whitespace flattened so a pointer that
straddles a line break is still one pointer, FLAG every

    <VERB> in <TARGET>

where VERB is one of the eight commissioned pointer verbs — recorded, named, given,
listed, documented, stated, set out, reported — or its third-person-singular present
form, and TARGET names NO checkable handle. TARGET is read from just after `in ` to the
FIRST of: a sentence/clause boundary (`. ; : ! ? , | ) ]`), or twelve words. The window
is deliberately TIGHT: a `§` or a backtick appearing LATER in the sentence must not
rescue a pointer whose own target is bare. That is `wealthTensor-86`'s lesson (i) —
letting a neighbour rescue the row collapses the count and makes the file unfalsifiable
by construction — and it is guarded by post-condition C7.

TARGET counts as NAMED, and is therefore NOT flagged, when it carries any of:
  N1  a backticked span                        `docs/preregistration/RESULT-002-wt026.md`
  N2  a section reference                      §10, §5.3, §A.1.1
  N3  a programme identifier                   PRE-002, REG-013, WT-059, RESULT-*, REVIEW-023,
                                               METHOD-001, ADR-*, DECISION-*, ROADS-*, SCOUT-*,
                                               POSITIONING-*, NOTE-*, END-TO-END-001
  N4  an appendix label                        Appendix A
  N5  a bare file path with an extension       docs/notes/NOTE-001.md
  N6  an INDEFINITE head ("a ", "an ")         "an instrument named in a paper before it is
                                               registered" — this construction QUANTIFIES, it
                                               does not point; there is no target the reader
                                               is being asked to supply.

N4 and N6 are the two judgement calls, and both are disclosed here rather than patched in
after the measurement. Each carries its own NEGATIVE post-condition (C4, C5).

WHAT THIS DOES NOT DO
---------------------
It cannot reach a pointer whose target IS named but names the WRONG thing. -83's III-3 —
"after the reading queue in §10 is discharged", where §10 held no queue — is OUT OF THIS
CLASS by construction: its target is a section reference, so N2 excludes it, and the
defect is resolves-to-the-wrong-thing, not resolves-to-nothing. The handoff commissioned a
two-legged severe test on III-2 and III-3; only the III-2 leg is satisfiable by the rule
it commissioned. C11 records that limit as a post-condition rather than widening the rule
to swallow it, because widening a criterion so that a post-condition passes is the
opposite of a severe test.

INVITED ATTACK. The count is sensitive to the twelve-word window and to N6. Someone who
thinks the window is too tight should widen it and show the count collapse; someone who
thinks N6 is a bend should drop it and show the flag it adds is a real pointer. Both are
one edit and a re-run.

EXIT CODES:  0 = no flags · 1 = flags present · 2 = the instrument itself is broken.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAPERS = [
    "docs/papers/paper-III-dual-tensor/paper-III.md",
    "docs/papers/paper-IV-composition/paper-IV.md",
]

# The eight commissioned pointer verbs, plus their 3sg present forms. Ordered longest
# first so "set out" wins over a bare word boundary.
VERBS = [
    "set out", "sets out",
    "recorded", "records",
    "documented", "documents",
    "reported", "reports",
    "listed", "lists",
    "stated", "states",
    "named", "names",
    "given", "gives",
]
# `\b` alone fires INSIDE a hyphenated compound — `mis-specified in` matches as `specified
# in`, and the compound means the NEGATION of the verb matched. Found at wealthTensor-88 BY
# the widened vocabulary of `wt163`, which is the only reason it surfaced: no verb on the
# eight occurs as the tail of a hyphenated compound in this corpus, so the defect was latent
# here and live there. wt163's post-condition D13 proves this guard leaves the ten flags
# published in REVIEW-027 untouched, and C12 below pins the case directly.
VERB_RE = re.compile(r"(?<![\w-])(" + "|".join(VERBS) + r")\s+in\s+", re.IGNORECASE)

# --- the NAMED-target tests (N1..N6) ------------------------------------------------
RE_BACKTICK = re.compile(r"`[^`]+`")
RE_SECTION = re.compile(r"§\s*[0-9A-Z]")
RE_PROG_ID = re.compile(
    r"\b(?:END-TO-END|PRE|REG|WT|RESULT|REVIEW|METHOD|ADR|DECISION|ROADS|SCOUT|"
    r"POSITIONING|NOTE)-[0-9A-Za-z][0-9A-Za-z.\-]*"
)
RE_APPENDIX = re.compile(r"\bAppendix\s+[A-Z]\b")
RE_PATHISH = re.compile(r"[A-Za-z0-9_./-]+\.(?:md|py|json|tsv|csv|log|txt|toml|yaml|yml)\b")
RE_INDEF = re.compile(r"^(?:an?)\s+", re.IGNORECASE)

MARKUP = re.compile(r"[*_]{1,3}")
BOUNDARY_CHARS = set(";:!?,|)]")
WORD_CAP = 12


def _flatten(text: str):
    """Collapse all whitespace runs to one space; return (flat, index -> line number)."""
    out = []
    lines = []
    line = 1
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        if ch.isspace():
            j = i
            while j < n and text[j].isspace():
                if text[j] == "\n":
                    line += 1
                j += 1
            out.append(" ")
            lines.append(line)
            i = j
        else:
            out.append(ch)
            lines.append(line)
            i += 1
    return "".join(out), lines


def _target_window(flat: str, start: int) -> str:
    """Read the pointer's TARGET: from `start` to the first clause boundary or 12 words.

    Boundary scanning never fires inside a backticked span, and a period flanked by
    digits (§5.3, 24.1) or sitting inside a path is not a boundary.
    """
    i = start
    n = len(flat)
    in_tick = False
    words = 0
    while i < n:
        ch = flat[i]
        if ch == "`":
            in_tick = not in_tick
            i += 1
            continue
        if not in_tick:
            if ch == " ":
                words += 1
                if words >= WORD_CAP:
                    break
            elif ch in BOUNDARY_CHARS:
                break
            elif ch == ".":
                prev = flat[i - 1] if i else ""
                nxt = flat[i + 1] if i + 1 < n else " "
                # a period only ends the window when it ends a word: not 5.3, not foo.md
                if not (prev.isdigit() and nxt.isdigit()) and not nxt.isalnum():
                    break
            elif ch == "—":
                break
        i += 1
    return flat[start:i].strip()


def _is_named(target: str):
    """Return the name of the first NAMED-target test the window satisfies, or None."""
    if RE_BACKTICK.search(target):
        return "N1 backticked span"
    if RE_SECTION.search(target):
        return "N2 section reference"
    if RE_PROG_ID.search(target):
        return "N3 programme identifier"
    if RE_APPENDIX.search(target):
        return "N4 appendix label"
    if RE_PATHISH.search(target):
        return "N5 file path"
    if RE_INDEF.match(MARKUP.sub("", target).strip()):
        return "N6 indefinite head (quantifies, does not point)"
    return None


def sweep_text(text: str, path: str = "<text>"):
    """Return (flags, considered) over one document's raw text."""
    flat, lines = _flatten(text)
    flags = []
    considered = 0
    for m in VERB_RE.finditer(flat):
        considered += 1
        target = _target_window(flat, m.end())
        named = _is_named(target)
        excerpt = flat[max(0, m.start() - 70): min(len(flat), m.end() + 90)].strip()
        rec = {
            "file": path,
            "line": lines[m.start()] if m.start() < len(lines) else 0,
            "verb": m.group(1).lower(),
            "target": target,
            "excerpt": excerpt,
            "named_by": named,
        }
        if named is None:
            flags.append(rec)
    return flags, considered


def _read(path: str, rev: str | None):
    if rev:
        return subprocess.check_output(
            ["git", "show", f"{rev}:{path}"], cwd=REPO_ROOT
        ).decode("utf-8")
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as fh:
        return fh.read()


# --- post-conditions -----------------------------------------------------------------
# Each is (id, kind, description, callable -> (ok, detail)).  KIND is POSITIVE (the
# instrument must fire) or NEGATIVE (the instrument must stay silent).

III2_BEFORE = ("Three post-hoc conjectures about where the conjunction broke are recorded "
               "in the repository's working notes.")
III3_BEFORE = ("The crash paper is a later paper in this corpus, written with a price line "
               "and after the reading queue in §10 is discharged.")
REPAIR_COMMIT = "908d5b1"   # wealthTensor-83, the commit that repaired III-2 and III-3


def _flags_of(text):
    return sweep_text(text)[0]


def _postconditions():
    checks = []

    def add(cid, kind, desc, fn):
        checks.append((cid, kind, desc, fn))

    add("C1", "POSITIVE", "III-2's pre-repair sentence flags",
        lambda: (len(_flags_of(III2_BEFORE)) == 1, f"{len(_flags_of(III2_BEFORE))} flag(s)"))

    add("C2", "NEGATIVE", "a target named as a backticked path does not flag",
        lambda: (len(_flags_of(
            "Three post-hoc conjectures are recorded in "
            "`docs/preregistration/RESULT-002-pilot-run.log`.")) == 0, "N1"))

    add("C3", "NEGATIVE", "a target named as a section reference does not flag",
        lambda: (len(_flags_of("The result reported in §5.3 comes from PRE-002.")) == 0, "N2"))

    add("C4", "NEGATIVE", "an appendix label is a named target and does not flag",
        lambda: (len(_flags_of("The framework is set out in **Appendix A**.")) == 0, "N4"))

    add("C5", "NEGATIVE", "an indefinite head quantifies and does not flag",
        lambda: (len(_flags_of(
            "An instrument named in a paper before it is registered is an instrument "
            "that has escaped its registration.")) == 0, "N6"))

    add("C6", "NEGATIVE", "a bare programme identifier is a named target",
        lambda: (len(_flags_of("Six guards were found and retired, recorded in METHOD-001.")) == 0,
                 "N3"))

    add("C7", "POSITIVE", "a § LATER in the sentence does not rescue a bare target",
        lambda: (len(_flags_of(
            "Cited for the decomposition named in its own title. §10 identifies this as "
            "the closest prior art.")) == 1, "anti-rescue; guards -86 lesson (i)"))

    add("C8", "POSITIVE", "a pointer straddling a line break is still one pointer",
        lambda: (len(_flags_of(
            "Three post-hoc conjectures about where the conjunction broke are recorded in\n"
            "the repository's working notes.")) == 1, "whitespace-insensitive"))

    add("C9", "POSITIVE", f"at {REPAIR_COMMIT}^ Paper III flags III-2's sentence",
        _c9)
    add("C10", "NEGATIVE", f"at {REPAIR_COMMIT} Paper III no longer flags it",
        _c10)
    add("C12", "NEGATIVE", "a hyphenated compound whose meaning negates the verb does not flag",
        lambda: (len(_flags_of(
            "The instrument was mis-specified in four ways and produced no answer.")) == 0,
            "the tokenisation guard; found at wealthTensor-88 by wt163's widened vocabulary"))

    add("C11", "NEGATIVE", "III-3 is OUT OF CLASS: its target is a section reference",
        lambda: (len(_flags_of(III3_BEFORE)) == 0,
                 "the commissioned two-legged severe test has one satisfiable leg"))
    return checks


def _paperIII_flag_targets(rev):
    text = _read(PAPERS[0], rev)
    return [f["target"] for f in sweep_text(text, PAPERS[0])[0]]


def _c9():
    try:
        targets = _paperIII_flag_targets(f"{REPAIR_COMMIT}^")
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    hit = [t for t in targets if "working notes" in t]
    return bool(hit), f"{len(targets)} flag(s) at parent; working-notes hit: {hit}"


def _c10():
    try:
        targets = _paperIII_flag_targets(REPAIR_COMMIT)
    except subprocess.CalledProcessError as exc:
        return False, f"git show failed: {exc}"
    hit = [t for t in targets if "working notes" in t]
    return not hit, f"{len(targets)} flag(s) at the repair commit; working-notes hit: {hit}"


def run_postconditions(verbose=True):
    ok_all = True
    results = []
    for cid, kind, desc, fn in _postconditions():
        try:
            ok, detail = fn()
        except Exception as exc:                     # noqa: BLE001
            ok, detail = False, f"raised {exc!r}"
        ok_all &= ok
        results.append({"id": cid, "kind": kind, "desc": desc, "ok": ok, "detail": detail})
        if verbose:
            mark = "ok  " if ok else "FAIL"
            print(f"  [{mark}] {cid} {kind:8s} {desc} — {detail}")
    return ok_all, results


def main(argv=None):
    ap = argparse.ArgumentParser(description="wt160 — flag pointers whose target is a bare noun phrase")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--rev", default=None, help="sweep a git revision instead of the working tree")
    ap.add_argument("--skip-postconditions", action="store_true")
    args = ap.parse_args(argv)

    per_file = []
    all_flags = []
    total_considered = 0
    for path in PAPERS:
        try:
            text = _read(path, args.rev)
        except Exception as exc:                      # noqa: BLE001
            print(f"wt160: cannot read {path}: {exc}", file=sys.stderr)
            return 2
        flags, considered = sweep_text(text, path)
        total_considered += considered
        all_flags.extend(flags)
        per_file.append({"file": path, "considered": considered, "flagged": len(flags),
                         "flags": flags})

    post_ok, post = (True, [])
    if not args.skip_postconditions:
        if not args.json:
            print("=== wt160 post-conditions ===")
        post_ok, post = run_postconditions(verbose=not args.json)

    if args.json:
        print(json.dumps({
            "rev": args.rev or "working-tree",
            "considered": total_considered,
            "flagged": len(all_flags),
            "per_file": per_file,
            "postconditions_ok": post_ok,
            "postconditions": post,
        }, indent=2, ensure_ascii=False))
    else:
        print()
        for pf in per_file:
            print(f"=== {pf['file']} — {pf['considered']} pointer construction(s) considered, "
                  f"{pf['flagged']} flagged ===")
            for f in pf["flags"]:
                print(f"  line {f['line']:>5}  «{f['verb']} in {f['target']}»")
                print(f"           …{f['excerpt']}…")
            if not pf["flags"]:
                print("  (none)")
            print()
        print(f"TOTAL over {len(PAPERS)} manuscript(s): {total_considered} considered, "
              f"{len(all_flags)} flagged.")

    if not post_ok:
        print("wt160: POST-CONDITIONS FAILED — the instrument is not trustworthy.", file=sys.stderr)
        return 2
    return 1 if all_flags else 0


if __name__ == "__main__":
    sys.exit(main())
