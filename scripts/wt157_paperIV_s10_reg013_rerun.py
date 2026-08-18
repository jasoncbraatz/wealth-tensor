#!/usr/bin/env python3
"""wt157 · Paper IV §10 — the reg013 bullet, corrected by a re-run.

wealthTensor-86 re-ran every command the sixteen unreproducible rows of
docs/promises-adjudicated.tsv stood on.  One of them disagreed with its note.

Row d4dd6baf17's note said, of `scripts/reg013_citation_whitespace.py`:

    "a clean run would not regenerate §6 either -- the audience is a live citing set that
     grows daily"

A clean run on 2026-08-18 returned RC 0 and **every figure §6 reports, unchanged**: the three
intersections (23 / 15 / 6), the three overlaps (0.0202 / 0.0108 / 0.0053), the three split-half
intersections (134 / 155 / 380), the pooled ceiling (0.4773) and the zero floor, with H1 SURVIVES.
Only the seed `cited_by` counts — which §6 does not report — had moved.

So §10's bullet was carrying two claims that the re-run contradicts: that the audience "grows every
day" (S and K were byte-identical two days on), and, by implication, that a clean run tells you
nothing about §6.  The load-bearing claim — *nothing in this repository re-derives §6's figures
from committed data* — is TRUE and is kept verbatim.  What is added is the replication and its
committed record, which is the thing this at-bat is about: a run whose output nobody can find is a
run nobody can check.

This script:
  1. writes the re-run's JSON to docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json
  2. replaces the §10 bullet
  3. verifies 12 post-conditions, 5 of them NEGATIVE, and ROLLS BACK from .bak-wt157 on any failure

RC 0 repaired · RC 2 refused or rolled back.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PAPER = REPO / "docs/papers/paper-IV-composition/paper-IV.md"
PAPER_III = REPO / "docs/papers/paper-III-dual-tensor/paper-III.md"
RERUN_SRC = Path("/tmp/wt86/runs/reg013.out")
RERUN_JSON = REPO / "docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json"
COMMITTED_JSON = REPO / "docs/preregistration/RESULT-REG-013-run.json"
BAK = PAPER.with_suffix(".md.bak-wt157")

OLD = """- **Re-run the instrument:** `python3 scripts/reg013_citation_whitespace.py`. It reproduces the
  instrument and not the pull. Each cluster's audience is the set of works citing its seeds,
  retrieved live from OpenAlex, and that set grows every day; the run is also subject to the API's
  rate limit, and on 2026-08-18 it exited non-zero on `HTTP 429` inside the ceiling control.
  Nothing in this repository re-derives §6's figures from committed data, and this bullet said
  "regenerate" until wealthTensor-82."""

NEW = """- **Re-run the instrument:** `python3 scripts/reg013_citation_whitespace.py`. It reproduces the
  instrument and not the pull. Each cluster's audience is the set of works citing its seeds,
  retrieved live from OpenAlex, so a run depends on that graph on the day it is made and on the
  API's rate limit: one attempt on 2026-08-18 exited non-zero on `HTTP 429` inside the ceiling
  control, and a second attempt the same day exited zero and returned every figure §6 reports
  unchanged — the three intersections, the three overlaps, the three split-half intersections, the
  pooled ceiling and the zero floor — while the seed citation counts the run prints had already
  moved. That second run is committed at
  `docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json`, and it replicates §6 on the live
  graph rather than regenerating it from anything held here. Nothing in this repository re-derives
  §6's figures from committed data, and this bullet said "regenerate" until wealthTensor-82."""

CHECKED = ("pairs", "ceiling", "P_ceiling", "F_floor", "void", "H1")


def extract_json(text):
    """The instrument prints a log then one top-level JSON object."""
    start = None
    for i, ch in enumerate(text):
        if ch == "{" and (i == 0 or text[i - 1] == "\n"):
            start = i
    if start is None:
        raise SystemExit("wt157: no top-level JSON object in the re-run output")
    return json.loads(text[start:])


def main():
    if not PAPER.exists():
        print("wt157: paper-IV.md missing"); return 2
    text = PAPER.read_text()
    if text.count(OLD) != 1:
        print(f"wt157: REFUSING — the §10 bullet does not appear exactly once "
              f"(found {text.count(OLD)}). The anchor moved; re-read §10 before editing.")
        return 2
    if not RERUN_SRC.exists():
        print(f"wt157: REFUSING — {RERUN_SRC} not found. Re-run the instrument first.")
        return 2

    rerun = extract_json(RERUN_SRC.read_text())
    committed = json.loads(COMMITTED_JSON.read_text())
    for k in CHECKED:
        if rerun[k] != committed[k]:
            print(f"wt157: REFUSING — the re-run does NOT reproduce {k}; this script's whole "
                  f"claim is that it does. Investigate rather than edit.")
            return 2

    shutil.copy2(PAPER, BAK)
    iii_before = PAPER_III.read_bytes()
    try:
        RERUN_JSON.write_text(json.dumps(rerun, indent=2) + "\n")
        PAPER.write_text(text.replace(OLD, NEW))
        new_text = PAPER.read_text()

        checks = []

        def c(name, polarity, cond, detail=""):
            checks.append((name, polarity, bool(cond), detail))

        c("C1 the new bullet is present exactly once", "POSITIVE", new_text.count(NEW) == 1)
        c("C2 the old bullet is gone", "POSITIVE", OLD not in new_text)
        c("C3 'and that set grows every day' no longer appears anywhere in paper-IV",
          "POSITIVE", "and that set grows every day" not in new_text)
        c("C4 the re-run record is referenced exactly once", "POSITIVE",
          new_text.count("RESULT-REG-013-rerun-2026-08-18.json") == 1)
        c("C5 the re-run record exists on disk and re-parses", "POSITIVE",
          RERUN_JSON.exists() and json.loads(RERUN_JSON.read_text())["H1"] == "SURVIVES")
        c("C6 the record reproduces every checked block of the committed run", "POSITIVE",
          all(json.loads(RERUN_JSON.read_text())[k] == committed[k] for k in CHECKED))
        c("C7 the load-bearing sentence is kept VERBATIM (modulo line wrapping)", "POSITIVE",
          "Nothing in this repository re-derives \u00a76's figures from committed data"
          in " ".join(new_text.split()))

        # ---- NEGATIVE: the edit must not reach past the bullet it names
        c("C8 NEGATIVE §6's three intersections are byte-unchanged", "NEGATIVE",
          all(s in new_text for s in ("| **23** | 1 139 | 0.0202 | 0.042 |",
                                      "| **15** | 1 383 | 0.0108 | 0.023 |",
                                      "| **6** | 1 139 | 0.0053 | 0.011 |")))
        c("C9 NEGATIVE §6's pooled ceiling of 0.477 is byte-unchanged", "NEGATIVE",
          "It came back at\n**0.477** pooled." in new_text or "**0.477** pooled" in new_text)
        c("C10 NEGATIVE paper-III.md is untouched", "NEGATIVE",
          PAPER_III.read_bytes() == iii_before)
        c("C11 NEGATIVE the word 'regenerate' has not gained an occurrence in paper-IV",
          "NEGATIVE", new_text.count("regenerate") == text.count("regenerate"))
        c("C12 NEGATIVE no OTHER manuscript is dirty in the working tree", "NEGATIVE",
          _only_paper_iv_dirty())

        ok = all(x[2] for x in checks)
        npos = sum(1 for x in checks if x[1] == "POSITIVE")
        nneg = sum(1 for x in checks if x[1] == "NEGATIVE")
        print(f"wt157 · POST-CONDITIONS ({len(checks)} total, {nneg} NEGATIVE, {npos} POSITIVE)")
        for name, pol, passed, detail in checks:
            print(f"    [{'ok  ' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail and not passed else ""))
        if not ok:
            shutil.copy2(BAK, PAPER)
            RERUN_JSON.unlink(missing_ok=True)
            print("\nwt157: ROLLED BACK from .bak-wt157. Nothing was changed.")
            return 2
        print("\nwt157: §10's reg013 bullet repaired; the re-run is committed as the record.")
        return 0
    except Exception as exc:  # noqa: BLE001
        shutil.copy2(BAK, PAPER)
        RERUN_JSON.unlink(missing_ok=True)
        print(f"wt157: EXCEPTION {exc!r} — ROLLED BACK from .bak-wt157.")
        return 2


def _only_paper_iv_dirty():
    out = subprocess.run(["git", "status", "--porcelain"], cwd=REPO,
                         capture_output=True, text=True).stdout
    dirty_manuscripts = [
        line[3:] for line in out.splitlines()
        if "docs/papers/" in line and line.rstrip().endswith(".md")
    ]
    return dirty_manuscripts == ["docs/papers/paper-IV-composition/paper-IV.md"]


if __name__ == "__main__":
    sys.exit(main())
