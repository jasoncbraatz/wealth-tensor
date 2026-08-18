#!/usr/bin/env python3
"""wt154 · EVIDENCE-DISCRIMINATION SWEEP over docs/promises-adjudicated.tsv

WHAT THIS IS FOR
----------------
REVIEW-024 drew twelve adjudicated rows at random, committed the twelve ids BEFORE
reading any of them, and found k = 5 false. Four of the five failed the same way, and
it is not the way `-83` found:

    THE ADJUDICATOR LOCATED THE ARTEFACT INSTEAD OF READING IT.

An evidence column reading `ls -l + git ls-files on darwin` with a note reading
"present, 134 lines" is a TRUE note. It is also true of a checklist that prescribes
nothing, a test that asserts the opposite of what the sentence says it forbids, and a
module no script regenerates. The row records that the artefact EXISTS; the sentence
claims what the artefact DOES.

That gap is mechanically detectable. This is the sweep REVIEW-024 §1 assigned, run over
all 129 rows instead of twelve.

THE QUESTION EACH ROW IS ASKED
------------------------------
Not "is the sentence true?" but REVIEW-024's criterion:

    Could the sentence be FALSE with this evidence unchanged?

TWO DETECTORS, REPORTED SEPARATELY
----------------------------------
D1 · LOCATE-ONLY
    No read-operation in `evidence` targets the row's own artefact. Either the evidence
    names no content-printing operation at all (`ls -l`, `git ls-files`, `grep -l`, a
    bare `same test` back-reference), or every read it does name is explicitly scoped to
    a DIFFERENT file. The second half is `-83`'s rule ("checked a different artefact"),
    mechanised; the first half is the shape REVIEW-024 found.

    `grep -l` is a locator even though grep normally reads: `-l` suppresses the matched
    lines and prints filenames, which is exactly why `bf2138f041` was false. The flag
    cluster is parsed, so `-rln` is a locator (the `l` dominates) while `-n` and `-c`
    are reads. A grep with no flags prints matching lines and is a read.

D2 · UNDER-COVERAGE
    The row's artefact carries a recognised programme ID (WT-nnn, REG-nnn, PRE-nnn,
    ADR-nnn, RESULT-*, REVIEW-nnn, POSITIONING-nnn, METHOD-nnn). The SENTENCE names at
    least one OTHER id of the same family, and that sibling appears in neither
    `evidence` nor `note`. The row's own share of a conjunctive sentence was checked and
    the other side was not.

    D2 exists because the fourth row REVIEW-024 filed as LOCATED is not one.
    `7e1c612368`'s evidence at 8855aba was `grep -n WT-059 docs/LEDGER.md` — a genuine
    read, of the artefact the row names, quoted in the note. No locate-detector can flag
    it, and REVIEW-024's own candidate-pattern list says so in a parenthetical ("the -l
    is the tell; `grep -n` is a read"). What was actually wrong is that the sentence
    claims a record spanning WT-059 AND WT-062 and the evidence never opened WT-062.
    Bending D1 until it caught a `grep -n` would have been tuning the instrument to a
    known answer; naming the second failure mode is the honest repair. See
    docs/REVIEW-025-adjudication-census.md §2.

THE RESCUE RULE
---------------
A row that trips D1 is rescued when its `note` carries a checkable value — a commit sha,
a hex digest, or a section reference — that also appears VERBATIM IN THE SENTENCE. Such a
note records the discriminating value whatever the evidence string says: `6efe91d805`'s
evidence is the bare back-reference `same test`, but its note reads "pinned at b9089c7"
and the sentence claims lambda_sensitivity.py is at b9089c7, so the sentence cannot be
false with that note unchanged. REVIEW-024 scored that row TRUE by hand for this reason.

The rescue is deliberately narrow — it requires a token SHARED with the sentence, so
"present, 134 lines" does not rescue anything: 134 is not a number the sentence makes a
claim about.

WHAT THIS SWEEP DOES NOT FLAG, AND WHY (stated, not silently dropped)
--------------------------------------------------------------------
16 rows carry `run on darwin, wealthTensor-82; output in the session log`. That evidence
RAN something — it is a read of behaviour, not a location — but its record is a session
log that no longer exists, so the row cannot be re-checked by a later reader. That is a
real defect and a DIFFERENT one: unreproducible, not undiscriminating. It is counted and
reported under `unreproducible` in --json and named in REVIEW-025 §4, but it does not
flag, because widening this sweep's criterion to cover it would make the census
incomparable with REVIEW-024's sample, which scored on discrimination alone.

18 rows carry `git log/cat-file on darwin, wealthTensor-82`. `git log`, `git show` and
`git cat-file` print content — commit messages, dates, paths touched, blob bodies — so they are reads.
The rows are terse, but terse is not the defect this sweep measures.

EXIT CODES (load-bearing)
-------------------------
    0  no row flags
    1  at least one row flags
    2  a POST-CONDITION failed — the sweep itself is broken and its output means nothing.
       (This is a widening of the two codes REVIEW-024 §4 specified. It is here because a
       sweep whose self-test failed must not be readable as "0 = clean"; see -84(vi).)

POST-CONDITIONS
---------------
Run on every invocation, before any result is printed. The severe test is already sitting
in git: `8855aba` is the TSV BEFORE `-84`'s repairs. At 8855aba the sweep must flag all
four rows REVIEW-024 found; at HEAD it must flag none of them, because -84 rewrote all
four evidence columns to name a read. A sweep validated only against the rows it was
written from is a rescued control. Four of the ten post-conditions are NEGATIVE.

USAGE
    python3 scripts/wt154_evidence_discrimination_sweep.py            # working tree
    python3 scripts/wt154_evidence_discrimination_sweep.py --json
    python3 scripts/wt154_evidence_discrimination_sweep.py --rev 8855aba
    python3 scripts/wt154_evidence_discrimination_sweep.py --skip-postconditions
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

TSV = "docs/promises-adjudicated.tsv"
BEFORE_REV = "8855aba"

# The four rows REVIEW-024 §2 scored FALSE for evidence that did not discriminate.
REVIEW_024_FALSE_EVIDENCE = ["bf2138f041", "75220244de", "76617b04e0", "7e1c612368"]
# The seven REVIEW-024 §2 scored TRUE by hand. A sweep that flags these disagrees with a
# read-by-hand verdict and must say so out loud rather than quietly outvoting it.
REVIEW_024_TRUE = ["3bdab165bf", "ec8622f081", "6efe91d805", "aebdfa4d76",
                   "fd2b77f988", "c487d43b12", "9add6ff45d"]

# --------------------------------------------------------------------------- parsing

FIELDS = ("paper", "promise_id", "artefact", "class", "evidence", "note", "sentence")


def parse(text: str) -> list[dict]:
    rows = []
    for line in text.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        f = line.split("\t")
        if len(f) < len(FIELDS):
            continue
        rows.append(dict(zip(FIELDS, f)))
    return rows


def load(rev: str | None, root: str) -> list[dict]:
    if rev is None:
        with open(os.path.join(root, TSV), encoding="utf-8") as fh:
            return parse(fh.read())
    out = subprocess.run(["git", "show", f"{rev}:{TSV}"], cwd=root,
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"wt154: git show {rev}:{TSV} failed: {out.stderr.strip()}")
    return parse(out.stdout)


# ------------------------------------------------------------------- D1 · locate-only

GREP = re.compile(r"\bgrep\b(?:\s+-(?P<flags>[A-Za-z]+))?", re.I)

# Operations that print some of a thing's CONTENT. `ls`, `git ls-files` and `grep -l`
# print only names, sizes and dates, so they are absent by construction.
READ_OPS = (
    r"\bread\b", r"\bsed\s+-n", r"\bhead\s+-", r"\btail\s+-", r"\bcat\b",
    r"\bcat-file\b", r"\bgit\s+log\b", r"\bgit\s+show\b", r"\bwc\s+-",
    r"\bshasum\b",
    r"\bpython3?\s", r"\bwt\d{2,3}\b", r"tests?/test_", r"\brun on darwin\b", r"§",
)
FILEISH = re.compile(r"[\w./-]+\.(?:py|md|json|tsv|log|txt)\b")


def clauses(evidence: str) -> list[str]:
    """Split an evidence cell into its separate operations.

    Adjudicators join operations with ` + ` (and occasionally `;` or `, and `). Scoping
    matters: `cat both logs end to end + grep every drop increment in edgar.py` is TWO
    operations, and reading the whole cell as one would let the second clause's filename
    decide what the first clause looked at.
    """
    parts = re.split(r"\s\+\s|;\s|,\sand\s", evidence)
    return [p.strip() for p in parts if p.strip()]


def read_ops(evidence: str) -> list[str]:
    """Return the clauses of `evidence` that name a content-printing operation."""
    ops: list[str] = []
    for c in clauses(evidence):
        greps = list(GREP.finditer(c))
        if greps and all("l" in (m.group("flags") or "").lower() for m in greps):
            # -l prints filenames only, whatever else is in the cluster
            if not any(re.search(p, GREP.sub("", c), re.I) for p in READ_OPS):
                continue
        if greps and any("l" not in (m.group("flags") or "").lower() for m in greps):
            ops.append(c)
            continue
        if any(re.search(p, c, re.I) for p in READ_OPS):
            ops.append(c)
    return ops


IS_PATHLIKE = re.compile(r"[\w./-]+\.(?:py|md|json|tsv|log|txt)$|^(?:test|def\s+test)[\w]*$")
IS_TESTREF = re.compile(r"tests?/test_|::test_|\btest_[a-z0-9_]+")


def artefact_is_a_file(artefact: str) -> bool:
    """Arm B only applies when the artefact IS a file (or a function inside one).

    For a programme ID — `PRE-001`, `REG-006`, a commit sha — the artefact is not a
    file, and the read that settles a claim about it very often lives somewhere else:
    a claim about what PRE-001 RETURNED is checked by reading RESULT-001, never by
    reading the registration. Arm B would call every such row a wrong-file read, which
    is why it is scoped to artefacts that are files.
    """
    return bool(IS_PATHLIKE.search(artefact) or artefact.startswith("test_"))


def _targets(op: str, artefact: str) -> bool:
    """Does this read-operation bear on THIS row's artefact?

    Three ways to be credited. The operation names the artefact. The operation names no
    file at all, so it is unscoped ('read §5.1') and gets the benefit of the doubt. Or
    the operation is a TEST reference: asserting things about other modules is a test's
    entire job, so "it names a different file" carries no information about a test.
    """
    if artefact and artefact in op:
        return True
    base = artefact.rsplit("/", 1)[-1]
    if base and base in op:
        return True
    if IS_TESTREF.search(op):
        return True
    named = FILEISH.findall(op)
    if not named:
        return True
    return any(base and (base in n or n.rsplit("/", 1)[-1] == base) for n in named)


SHA = re.compile(r"\b[0-9a-f]{7,64}\b")
SEC = re.compile(r"§[\d.]+[A-Za-z]?")
NUM = re.compile(r"\b\d+\.\d+\b")


def rescue_tokens(row: dict) -> list[str]:
    """Checkable values in the NOTE that the SENTENCE also carries.

    A sha, a digest, a section reference or a decimal figure. Shared with the sentence
    is the whole point: "present, 134 lines" carries a number, but 134 is not a number
    the sentence makes any claim about, so it rescues nothing.
    """
    toks = (set(SHA.findall(row["note"])) | set(SEC.findall(row["note"]))
            | set(NUM.findall(row["note"])))
    return sorted(t for t in toks if t in row["sentence"])


def d1(row: dict) -> tuple[bool, str]:
    ops = read_ops(row["evidence"])
    if not ops:
        why = "evidence names no content-printing operation"
    elif (artefact_is_a_file(row["artefact"])
          and not any(_targets(op, row["artefact"]) for op in ops)):
        why = "every read in the evidence is scoped to a different file"
    else:
        return False, ""
    resc = rescue_tokens(row)
    if resc:
        return False, ""
    return True, why


# --------------------------------------------------------------- D2 · under-coverage

FAMILIES = (
    r"WT-\d+", r"REG-\d+", r"PRE-\d+", r"ADR-\d+", r"REVIEW-\d+",
    r"POSITIONING-\d+", r"METHOD-\d+", r"RESULT-[A-Z0-9-]+\d",
)


def d2(row: dict) -> tuple[bool, str]:
    # Class N rows assert nothing that could fail independently of a row adjudicated
    # elsewhere (the TSV header's own definition), so there is no conjunction for the
    # evidence to under-cover. A §5.3 table header naming both PRE-001 and PRE-002 is
    # the canonical case.
    if row["class"].strip() == "N":
        return False, ""
    art = row["artefact"]
    for fam in FAMILIES:
        m = re.fullmatch(fam, art)
        if not m:
            continue
        sibs = {s for s in re.findall(fam, row["sentence"]) if s != art}
        missing = sorted(s for s in sibs
                         if s not in row["evidence"] and s not in row["note"])
        if missing:
            return True, ("sentence also names " + ", ".join(missing) +
                          "; neither evidence nor note mentions " +
                          ("it" if len(missing) == 1 else "them"))
        return False, ""
    return False, ""


# ------------------------------------------------------------------------- the sweep

UNREPRODUCIBLE = re.compile(r"output in the session log", re.I)


def sweep(rows: list[dict]) -> dict:
    flagged = []
    for r in rows:
        hit1, why1 = d1(r)
        hit2, why2 = d2(r)
        if hit1 or hit2:
            flagged.append({
                "promise_id": r["promise_id"], "paper": r["paper"],
                "artefact": r["artefact"], "class": r["class"],
                "evidence": r["evidence"],
                "detectors": ([("D1", why1)] if hit1 else []) + ([("D2", why2)] if hit2 else []),
            })
    return {
        "population": len(rows),
        "flagged": flagged,
        "n_flagged": len(flagged),
        "n_d1": sum(1 for f in flagged if any(d[0] == "D1" for d in f["detectors"])),
        "n_d2": sum(1 for f in flagged if any(d[0] == "D2" for d in f["detectors"])),
        "rescued": [r["promise_id"] for r in rows
                    if read_ops(r["evidence"]) == [] and rescue_tokens(r)],
        "unreproducible": [r["promise_id"] for r in rows
                           if UNREPRODUCIBLE.search(r["evidence"])],
    }


# --------------------------------------------------------------------- post-conditions

SYNTH_LOCATE = dict(paper="x", promise_id="synthetic-locate", artefact="docs/X.md",
                    **{"class": "H"}, evidence="ls -l + git ls-files on darwin",
                    note="present, 134 lines", sentence="`docs/X.md` prescribes the check.")
SYNTH_READ = dict(paper="x", promise_id="synthetic-read", artefact="docs/X.md",
                  **{"class": "H"}, evidence="read docs/X.md §2",
                  note="§2 prescribes the check, verbatim",
                  sentence="`docs/X.md` prescribes the check.")
SYNTH_GREPN = dict(paper="x", promise_id="synthetic-grep-n", artefact="docs/X.md",
                   **{"class": "H"}, evidence="grep -n 'prescribes' docs/X.md",
                   note="L42", sentence="`docs/X.md` prescribes the check.")
SYNTH_GREPL = dict(paper="x", promise_id="synthetic-grep-l", artefact="docs/X.md",
                   **{"class": "H"}, evidence="grep -rln 'prescribes' docs/",
                   note="docs/X.md", sentence="`docs/X.md` prescribes the check.")


def post_conditions(root: str) -> list[tuple[bool, str, str]]:
    """Returns (ok, POSITIVE|NEGATIVE, description). Ten checks, four NEGATIVE."""
    res: list[tuple[bool, str, str]] = []
    before = {f["promise_id"] for f in sweep(load(BEFORE_REV, root))["flagged"]}
    head_rows = load(None, root)
    head = {f["promise_id"] for f in sweep(head_rows)["flagged"]}
    head_ids = {r["promise_id"] for r in head_rows}

    for pid in REVIEW_024_FALSE_EVIDENCE:
        res.append((pid in before, "POSITIVE",
                    f"at {BEFORE_REV}, {pid} flags (REVIEW-024 §2 scored it FALSE)"))
    res.append((not (set(REVIEW_024_FALSE_EVIDENCE) & head), "NEGATIVE",
                "at HEAD, none of REVIEW-024's four flag (-84 rewrote all four "
                "evidence columns to name a read)"))
    still = sorted(p for p in REVIEW_024_TRUE if p in head and p in head_ids)
    res.append((not still, "NEGATIVE",
                "at HEAD, no row REVIEW-024 §2 scored TRUE by hand flags"
                + (f" — but {', '.join(still)} does" if still else "")))
    res.append((len(before) > len(head), "POSITIVE",
                f"the repairs moved the count down: {len(before)} at {BEFORE_REV} "
                f"> {len(head)} at HEAD"))
    res.append((d1(SYNTH_LOCATE)[0] and d1(SYNTH_GREPL)[0], "POSITIVE",
                "a synthetic `ls -l` row and a synthetic `grep -rln` row both flag"))
    res.append((not d1(SYNTH_READ)[0], "NEGATIVE",
                "a synthetic `read docs/X.md §2` row does NOT flag"))
    res.append((not d1(SYNTH_GREPN)[0], "NEGATIVE",
                "a synthetic `grep -n` row does NOT flag (REVIEW-024: the -l is the "
                "tell; grep -n is a read)"))
    return res


# -------------------------------------------------------------------------- reporting

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rev", default=None,
                    help="sweep the TSV at a git revision instead of the working tree")
    ap.add_argument("--skip-postconditions", action="store_true")
    ap.add_argument("--root", default=None)
    args = ap.parse_args()

    root = args.root or subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True
    ).stdout.strip() or "."

    pcs: list[tuple[bool, str, str]] = []
    if not args.skip_postconditions:
        pcs = post_conditions(root)

    result = sweep(load(args.rev, root))
    result["post_conditions"] = [
        {"ok": ok, "polarity": pol, "check": desc} for ok, pol, desc in pcs
    ]
    result["rev"] = args.rev or "working tree"

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"=== wt154 · evidence-discrimination sweep — {result['rev']} ===")
        print(f"{result['population']} adjudicated rows · "
              f"{result['n_flagged']} flagged "
              f"(D1 locate-only {result['n_d1']}, D2 under-coverage {result['n_d2']})")
        print(f"rescued by a note carrying a value the sentence also carries: "
              f"{len(result['rescued'])}")
        print(f"not flagged, reported: {len(result['unreproducible'])} rows whose "
              f"evidence is a run whose output lived in a session log")
        if result["flagged"]:
            print()
            for f in result["flagged"]:
                tags = "+".join(d[0] for d in f["detectors"])
                print(f"  [{tags}] {f['promise_id']}  {f['paper']}  {f['artefact']}")
                print(f"          evidence: {f['evidence']}")
                for d, why in f["detectors"]:
                    print(f"          {d}: {why}")
        if pcs:
            print()
            print(f"POST-CONDITIONS ({sum(1 for ok, _, _ in pcs if ok)}/{len(pcs)} ok, "
                  f"{sum(1 for _, p, _ in pcs if p == 'NEGATIVE')} negative)")
            for ok, pol, desc in pcs:
                print(f"  {'ok  ' if ok else 'FAIL'} [{pol}] {desc}")

    if any(not ok for ok, _, _ in pcs):
        print("\nwt154: A POST-CONDITION FAILED. The sweep is broken; its count above "
              "means nothing.", file=sys.stderr)
        return 2
    return 1 if result["n_flagged"] else 0


if __name__ == "__main__":
    sys.exit(main())
