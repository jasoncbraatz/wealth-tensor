#!/usr/bin/env python3
"""wt148 · the PROMISE sweep — every sentence that names an artefact, and what it promises.

WHY THIS FILE EXISTS
--------------------
Eleven reader-passes on this corpus (`-71`..`-81`) each found 2-9 findings, and every
mechanism offered for that rate is dead: new instruments (`-71`/`-77`), residue (`-78`),
depth (`-79`), coverage (`-81`) — each proposed by the pass whose own number it explained,
each killed by the next pass. A twelfth reader-pass buys a twelfth row and no information.

But `-80` and `-81` measured something a pass cannot argue with: **5 of 9 and 5 of 9
findings, two manuscripts, two reviewers, the same shape** — a sentence whose subject is a
named file, command, test or commit, asserting what it does FOR A READER, where it does
not. `-79` named the class ("a promise about an artefact is a claim, and checking the
artefact does not check it"); `-80` generalised it across manuscripts; nobody enumerated
it. `wt133` checks one narrow slice of it (`§N.M` resolution) and only entry→body.

This file enumerates the class MECHANICALLY, so the question stops being "did the reviewer
notice?" and becomes "is every row ticked?".

    python3 scripts/wt148_promise_sweep.py                  # every manuscript
    python3 scripts/wt148_promise_sweep.py paper-IV         # one
    python3 scripts/wt148_promise_sweep.py --checklist      # unadjudicated, as a worklist
    python3 scripts/wt148_promise_sweep.py --md             # markdown, for a REVIEW doc
    python3 scripts/wt148_promise_sweep.py --json           # every promise, machine-readable

EXIT CODE IS LOAD-BEARING: 0 iff every promise emitted for an IN-SCOPE manuscript carries a
row in `docs/promises-adjudicated.tsv` AND no row in scope has gone stale. Scope is declared
in the TSV's own `#scope` line, not here, so widening it is a data edit that goes red
immediately — the way `-81` learned a green row can be satisfied by a sibling's artefact.

WHAT THIS INSTRUMENT CANNOT SEE (say it, so a green run is not read as more than it is):
  * It finds sentences that NAME an artefact. A promise that names none — "the appendix
    proves it", "the Austrian account of the cycle" (`IV-6`) — is invisible here, by
    construction. That class needs a different instrument.
  * It cannot tell a promise from a mention. Deciding that is the adjudication, and the
    adjudication is a human running the artefact — which is the point, not a shortfall.
  * It reads prose only: fenced code blocks are skipped (a listing is not a promise;
    the prose around it is). The References section IS swept — an entry that names a
    repository path makes exactly this kind of claim.
  * A row asserts that SOMEONE RAN SOMETHING. Delete a row and the sweep goes red; that is
    how you audit this file instead of trusting it.
"""
from __future__ import annotations

import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPERS = sorted((ROOT / "docs" / "papers").glob("*/paper-*.md"))
ADJUDICATED = ROOT / "docs" / "promises-adjudicated.tsv"

# ---------------------------------------------------------------------------
# 1 · what counts as a named artefact
# ---------------------------------------------------------------------------
# Ordered: the first pattern to match at a position wins, so END-TO-END-001 is not shredded
# into "RESULT-END" by a lazier id rule (that exact mis-parse showed up in this file's own
# first probe run, which is the argument for probing before committing a regex).
ARTEFACT_PATTERNS = [
    ("cmd", re.compile(r"python3\s+(?:-m\s+)?[^\s`,;)]+(?:\s+[-\w./=]+)*")),
    ("path", re.compile(r"(?:[\w.\-*?]+/)+[\w.\-*?]+\.(?:py|md|json|tsv|log|txt|csv|sh|toml)\b")),
    ("id", re.compile(r"\b(?:RESULT-)?(?:END-TO-END|REG|ADR|METHOD|DECISION|ROADS|REVIEW|WT|PRE)-\d+(?:-[A-Z0-9]+)*")),
    ("test", re.compile(r"\btest_[a-z0-9_]+\b")),
    ("file", re.compile(r"\b[\w\-]+\.(?:py|md|json|tsv|log|csv|toml)\b")),
    # Bare tool tags: `wt091`, `wt026`. Named without an extension, so the file/path rules miss
    # them -- and paper III names one exactly that way ("before `wt091` existed").
    ("tag", re.compile(r"\bwt\d{2,3}\b")),
    ("sha", re.compile(r"(?<![\w.])(?=[0-9a-f]{7,40}(?![0-9a-f]))(?=[0-9a-f]*\d)[0-9a-f]{7,40}")),
]


def artefacts(sentence: str) -> list[str]:
    """Distinct artefact tokens in one sentence, longest-match-first, no overlaps."""
    spans: list[tuple[int, int, str]] = []
    for _kind, pat in ARTEFACT_PATTERNS:
        for m in pat.finditer(sentence):
            if any(not (m.end() <= a or m.start() >= b) for a, b, _ in spans):
                continue
            spans.append((m.start(), m.end(), m.group(0)))
    out, seen = [], set()
    for _s, _e, tok in sorted(spans):
        tok = tok.rstrip(".,;:)")
        if tok and tok not in seen:
            seen.add(tok)
            out.append(tok)
    return out


# ---------------------------------------------------------------------------
# 2 · prose blocks — fenced code and References are not prose
# ---------------------------------------------------------------------------
BOUNDARY = re.compile(r"(?:#{1,6}\s|[-*+]\s|\d+[.)]\s)")
ABBREV = ("e.g", "i.e", "cf", "vs", "Fig", "Eq", "No", "al", "resp", "approx", "Dr", "St")
SENT_END = re.compile(r"(?<=[.!?])[\"'’)\]]*\s+(?=[\"'`(\[A-Z§*])")


def blocks(path: pathlib.Path) -> list[tuple[int, str]]:
    """[(1-based line, text)] — one block per prose unit.

    A list item, a table row, a heading and a paragraph are each their own unit; a wrapped
    continuation line joins the unit above it. Getting this wrong is not cosmetic: this
    file's first run glued eight bullets of Paper I's §8 into one 900-character "sentence"
    carrying seven artefacts, which is a checklist nobody can tick.
    """
    lines = path.read_text(encoding="utf-8").split("\n")
    out: list[tuple[int, str]] = []
    fenced = False
    para: list[str] = []
    start = 0

    def flush():
        nonlocal para
        if para:
            out.append((start, " ".join(para)))
            para = []

    for i, raw in enumerate(lines, 1):
        s = raw.strip()
        if s.startswith("```"):
            fenced = not fenced
            flush()
            continue
        if fenced:
            continue
        s = re.sub(r"^>\s?", "", s).strip()   # blockquote marker is not content
        if not s:
            flush()
            continue
        if s.startswith("|"):
            flush()
            if not set(s) <= set("|-: "):      # a table RULE row carries nothing
                out.append((i, s))
            continue
        if BOUNDARY.match(s):                  # heading / bullet / numbered item
            flush()
            start = i
            para = [s]
            continue
        if not para:
            start = i
        para.append(s)
    flush()
    return out


def sentences(block: str) -> list[str]:
    parts, buf = [], ""
    for chunk in SENT_END.split(block):
        buf = (buf + " " + chunk).strip() if buf else chunk
        if any(buf.rstrip(".").endswith(a) for a in ABBREV):
            continue
        parts.append(buf)
        buf = ""
    if buf:
        parts.append(buf)
    return [p for p in parts if p.strip()]


def normalise(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def promise_id(stem: str, artefact: str, sentence: str) -> str:
    key = f"{stem}\x1f{artefact}\x1f{normalise(sentence)}".encode("utf-8")
    return hashlib.sha1(key).hexdigest()[:10]


# ---------------------------------------------------------------------------
# 3 · emit
# ---------------------------------------------------------------------------
def emit(path: pathlib.Path) -> list[dict]:
    rows = []
    for line_no, block in blocks(path):
        for sent in sentences(block):
            toks = artefacts(sent)
            for tok in toks:
                rows.append(dict(paper=path.stem, line=line_no, artefact=tok,
                                 sentence=normalise(sent),
                                 pid=promise_id(path.stem, tok, sent)))
    return rows


def load_adjudications():
    """(scope stems, {promise_id: row dict}) from the TSV — data, not code."""
    scope: list[str] = []
    rows: dict[str, dict] = {}
    if not ADJUDICATED.exists():
        return scope, rows
    for raw in ADJUDICATED.read_text(encoding="utf-8").split("\n"):
        if raw.lstrip().startswith("#scope"):
            scope = [f.strip() for f in raw.split("\t")[1:] if f.strip()]
            continue
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        f = raw.split("\t")
        if len(f) < 6:
            continue
        rows[f[1].strip()] = dict(paper=f[0].strip(), pid=f[1].strip(),
                                  artefact=f[2].strip(), cls=f[3].strip(),
                                  evidence=f[4].strip(), note=f[5].strip(),
                                  sentence=(f[6].strip() if len(f) > 6 else ""))
    return scope, rows


CLASSES = {
    "H": "HELD — the artefact bears the sentence out",
    "N": "NOT A PROMISE — names the artefact, asserts nothing about it that could fail",
    "R": "REPAIRED — it failed; the manuscript was changed in the same pass",
    "C": "CARDED — it failed and could not be repaired in-pass; note carries the falsifier",
}


def main(argv: list[str]) -> int:
    md = "--md" in argv
    as_json = "--json" in argv
    checklist = "--checklist" in argv
    sel = [a for a in argv if not a.startswith("-")]
    paths = [p for p in PAPERS if not sel or any(s == p.stem for s in sel)]
    if not paths:
        sys.exit(f"no manuscript matched {sel}; have {[p.name for p in PAPERS]}")

    if as_json:
        import json
        out = []
        for path in paths:
            out.extend(emit(path))
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return 0

    scope, adj = load_adjudications()
    if not scope:
        print("!! docs/promises-adjudicated.tsv declares no #scope line — nothing is gated.")
    bad = False
    seen_ids: set[str] = set()
    grand = dict(emitted=0, adjudicated=0, failed=0, pending=0)

    for path in paths:
        rows = emit(path)
        in_scope = path.stem in scope
        done = [r for r in rows if r["pid"] in adj]
        todo = [r for r in rows if r["pid"] not in adj]
        seen_ids |= {r["pid"] for r in rows}
        by_class: dict[str, int] = {}
        for r in done:
            by_class[adj[r["pid"]]["cls"]] = by_class.get(adj[r["pid"]]["cls"], 0) + 1
        failed = by_class.get("R", 0) + by_class.get("C", 0)
        grand["emitted"] += len(rows)
        grand["adjudicated"] += len(done)
        grand["failed"] += failed
        grand["pending"] += 0 if in_scope else len(todo)

        tag = "IN SCOPE" if in_scope else "not yet in scope — NOT GATED"
        if md:
            print(f"\n**{path.name}** — {len(rows)} promises emitted, {len(done)} adjudicated "
                  f"({tag}).\n")
            print("| class | meaning | count |")
            print("|---|---|---|")
            for k, v in CLASSES.items():
                print(f"| {k} | {v} | {by_class.get(k, 0)} |")
            print(f"| — | unadjudicated | {len(todo)} |")
        else:
            print(f"\n=== {path.name} — {len(rows)} promises over "
                  f"{len({r['sentence'] for r in rows})} sentences  [{tag}] ===")
            print("  " + ", ".join(f"{k}={by_class.get(k, 0)}" for k in CLASSES)
                  + f", unadjudicated={len(todo)}")
        if todo and (checklist or in_scope):
            for r in todo[:200]:
                print(f"  [ ] {r['pid']}  L{r['line']}  {r['artefact']}")
                print(f"        {r['sentence'][:220]}")
        if in_scope and todo:
            print(f"  *** {len(todo)} UNADJUDICATED promise(s) on an in-scope manuscript.")
            bad = True
        if not in_scope and todo:
            # No silent caps: an ungated manuscript still says what it is hiding.
            print(f"  ({len(todo)} promise(s) here are unchecked by anyone; widen #scope "
                  f"in docs/promises-adjudicated.tsv to gate them.)")

    stale = [pid for pid, r in adj.items()
             if pid not in seen_ids and r["paper"] in scope
             and (not sel or r["paper"] in sel)]
    if stale:
        print(f"\n*** {len(stale)} STALE row(s) in docs/promises-adjudicated.tsv — the "
              f"sentence they adjudicated no longer exists verbatim, so the check they "
              f"record no longer applies: {', '.join(sorted(stale))}")
        bad = True

    print(f"\nTOTAL over {len(paths)} manuscript(s): {grand['emitted']} promises emitted, "
          f"{grand['adjudicated']} adjudicated, {grand['failed']} failed adjudication "
          f"(R or C), {grand['pending']} left unchecked outside scope.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
