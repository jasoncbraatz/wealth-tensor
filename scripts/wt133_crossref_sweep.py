#!/usr/bin/env python3
"""wt133 · the two CROSS-REFERENCE sweeps, as a committed instrument.

WHY THIS FILE EXISTS
--------------------
`WT-120` (`-73`): *a cross-reference is a quantifier over a section, and it is the one a careful
read cannot catch.* Reading forward from "every" means holding one set in your head; reading
"§4.4's volatility result" means holding a DIFFERENT section in your head, and you cannot -- so
this class survives every careful read by construction, not by oversight. Four of `-73`'s seven
findings were this class, and `-74`'s `II-22` and `II-24` are downstream of the same idea.

`-73` ran both loops ad hoc and wrote them into `REVIEW-013` §3 instead of committing them.
`WT-116` was banked to prevent exactly that (*"a procedure that lives in a ledger entry is a
procedure the next session re-derives"*), and `-74` re-derived them, which is the second data
point. This file is the fix. Queue item 4, closed.

    python3 scripts/wt133_crossref_sweep.py                 # every manuscript
    python3 scripts/wt133_crossref_sweep.py paper-II        # one
    python3 scripts/wt133_crossref_sweep.py paper-II --md   # markdown, for a REVIEW doc

EXIT CODE IS LOAD-BEARING: 0 iff every sweep is clean, 1 if anything is flagged. A flag is NOT
automatically a finding -- `-73` measured 1 real in 7 flagged and `-74` measured 0 in 18, and
BOTH ratios were worth the five minutes, because the alternative is that nobody checks at all.
The two standing false-positive classes, named so they cost seconds:

  (A) the reference names the SOURCE'S OWN section  ("their §4.1", "Sims's §5")
  (B) the entry makes a claim ABOUT a section rather than asserting a citation IN it
  (C) sweep 2 matches SURNAMES, so an entry counts as cited when any of its authors' surnames
      appears -- including via a shared co-author, or because the surname is also the name of a
      statistic. Paper II's Gini (1912) entry and its Chakraborti entry are both class C: "Gini"
      occurs 21 times as the coefficient and never as the citation. Read the flagged list, do
      not total it.

REPORT WHAT YOU COUNT, NOT JUST THE NUMBER (`-73`(iii)): every line below says what it counted.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPERS = sorted((ROOT / "docs" / "papers").glob("*/paper-*.md"))
DISMISSED = ROOT / "docs" / "crossref-dismissed.tsv"


def _dismissed():
    """(paper stem, ref) pairs already adjudicated as another document's section.

    Without this the exit code is decoration: class-A false positives are PERMANENT, so an
    un-filtered sweep exits 1 forever and stops meaning anything. With it, RC 1 means a NEW
    unresolved reference has appeared -- which is the only thing worth a tripwire.
    """
    out = {}
    if not DISMISSED.exists():
        return out
    for line in DISMISSED.read_text(encoding="utf-8").split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        f = line.split("\t")
        if len(f) >= 4:
            out[(f[0].strip(), f[1].strip())] = f[3].strip()
    return out

HEADING = re.compile(r"^#{1,6}\s+([A-Z]?\.?\d+(?:\.\d+)*)\s*·", re.M)
SECREF = re.compile(r"§\s*([A-Z]?\.?\d+(?:\.\d+)*)")
CITEDIN = re.compile(r"cited in\s+§\s*([A-Z]?\.?\d+(?:\.\d+)*)", re.I)
# An entry opens a paragraph with a surname, a comma and an initial: "Bouchaud, J.-P., & ..."
ENTRY = re.compile(r"^([^\s,][^,]{1,40}),\s+[A-Z]\.", re.M)


def _refs_start(lines):
    for i, ln in enumerate(lines):
        if ln.strip().lower().startswith("## references"):
            return i
    return len(lines)


def _sections(lines):
    """[(first_line_index, section_id)] for level-N numbered headings."""
    out = []
    for i, ln in enumerate(lines):
        m = HEADING.match(ln)
        if m:
            out.append((i, m.group(1)))
    return out


def _section_of(idx, secs):
    cur = "front"
    for i, s in secs:
        if i <= idx:
            cur = s
        else:
            break
    return cur


def _section_text(sec_id, lines, secs):
    for n, (i, s) in enumerate(secs):
        if s == sec_id:
            end = secs[n + 1][0] if n + 1 < len(secs) else len(lines)
            return "\n".join(lines[i:end])
    return ""


def sweep(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    while lines and not lines[-1].strip():
        lines.pop()
    r0 = _refs_start(lines)
    body, refs_block = lines[:r0], lines[r0:]
    secs = _sections(lines)
    heads = {s for _i, s in secs}

    # ---- SWEEP 1 · every §N.M in the body resolves to a heading of THIS document ----
    hits = {}
    for i, ln in enumerate(body):
        for m in SECREF.finditer(ln):
            hits.setdefault(m.group(1), []).append(i + 1)
    total = sum(len(v) for v in hits.values())
    dis = _dismissed()
    stem = path.stem
    unresolved, dismissed = {}, {}
    for k, v in hits.items():
        if k in heads:
            continue
        (dismissed if (stem, k) in dis else unresolved)[k] = v

    # ---- SWEEP 2 · reference entries against the body ------------------------------
    entries, buf = [], []
    for ln in refs_block[1:]:
        if ln.strip():
            buf.append(ln)
        elif buf:
            entries.append("\n".join(buf))
            buf = []
    if buf:
        entries.append("\n".join(buf))
    entries = [e for e in entries if ENTRY.match(e)]

    body_text = "\n".join(body)
    uncited, claims = [], []
    for e in entries:
        surnames = [m.group(1).strip() for m in ENTRY.finditer(e)]
        surnames += re.findall(r"&\s+([A-Z][^\s,]{1,30}),\s+[A-Z]\.", e)
        surnames = [s for s in dict.fromkeys(surnames) if len(s) > 2]
        key = surnames[0] if surnames else e[:30]
        if not any(s in body_text for s in surnames):
            uncited.append(key)
        for sec_id in CITEDIN.findall(e):
            txt = _section_text(sec_id, lines, secs)
            ok = any(s in txt for s in surnames)
            claims.append((key, sec_id, ok))

    return dict(path=path, lines=len(lines), total=total, distinct=len(hits),
                unresolved=unresolved, dismissed=dismissed, entries=len(entries),
                uncited=uncited, claims=claims, cited=len(entries) - len(uncited))


def report(r, md=False):
    name = r["path"].name
    bad = bool(r["unresolved"]) or any(not ok for _k, _s, ok in r["claims"])
    if md:
        print(f"\n**{name}** — {r['total']} `§N.M` references on {r['lines']} lines, "
              f"{r['distinct']} distinct; {r['entries']} reference entries.\n")
        print("| sweep | counted | result |")
        print("|---|---|---|")
        print(f"| §N.M vs heading list | {r['total']} refs, {r['distinct']} distinct | "
              f"{'**' + str(len(r['unresolved'])) + ' UNRESOLVED**' if r['unresolved'] else 'zero unresolved'}"
              f" ({len(r['dismissed'])} dismissed) |")
        print(f"| entries vs body, by surname | {r['entries']} entries | "
              f"{r['cited']} do work in the body, {len(r['uncited'])} do not |")
        if r["claims"]:
            n_bad = sum(1 for _k, _s, ok in r["claims"] if not ok)
            print(f"| \"cited in §N.M\" claims | {len(r['claims'])} claims | "
                  f"{n_bad} flagged |")
    else:
        print(f"\n=== {name} — {r['lines']} lines ===")
        print(f"  sweep 1: {r['total']} §N.M references, {r['distinct']} distinct, "
              f"{len(r['unresolved'])} unresolved, "
              f"{len(r['dismissed'])} dismissed as another document's section")
        for k, v in sorted(r["unresolved"].items()):
            print(f"           *** §{k} does not resolve to a heading — lines {v[:8]} "
                  f"(check false-positive class A: is it the SOURCE'S own §?)")
        print(f"  sweep 2: {r['entries']} reference entries, {r['cited']} cited in the body, "
              f"{len(r['uncited'])} not")
        if r["uncited"]:
            print(f"           not cited: {', '.join(r['uncited'])}")
        print(f"           {len(r['claims'])} explicit \"cited in §N.M\" claims, "
              f"{sum(1 for _k, _s, ok in r['claims'] if not ok)} flagged")
        for k, s, ok in r["claims"]:
            if not ok:
                print(f"           *** {k} claims §{s}; that section's text does not name it "
                      f"(check class B: a claim ABOUT the section?)")
    return bad


def main(argv):
    md = "--md" in argv
    sel = [a for a in argv if not a.startswith("-")]
    # NB: match the FILE STEM, not the path -- "paper-II" is a prefix of "paper-III" and a
    # substring match silently swept two manuscripts when one was asked for (found by -74's
    # own first run of this file, which is the argument for running what you write).
    paths = [p for p in PAPERS if not sel or any(s == p.stem for s in sel)]
    if not paths:
        sys.exit(f"no manuscript matched {sel}; have {[p.name for p in PAPERS]}")
    bad = False
    for p in paths:
        bad |= report(sweep(p), md=md)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
