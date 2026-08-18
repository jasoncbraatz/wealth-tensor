#!/usr/bin/env python3
"""wt150 · Paper IV §10 — "Regenerate §6" names a command that regenerates nothing, and the
committed record that IS §6's evidence is named nowhere in the section.

THE FINDING (wealthTensor-82, `IV-1`, found by `scripts/wt148_promise_sweep.py`)
-------------------------------------------------------------------------------
§10 carried the bare bullet `- **Regenerate §6:** python3 scripts/reg013_citation_whitespace.py`.
Run on darwin on 2026-08-18, that command exits **1**: it queries `api.openalex.org` live and
died on `HTTP 429 Too Many Requests` partway through the split-half ceiling control, after
resolving all 25 seeds and retrieving four audiences. And a clean run would not regenerate §6
either, for a reason the instrument's own docstring implies: a cluster's audience is the set of
works CITING its seeds, which grows every day, so §6's audience sizes (7 801 and 43 048) and its
overlap coefficients are the record of ONE pull, on 2026-08-16.

That record is committed -- `docs/preregistration/RESULT-REG-013-run.json` and `-run.log`, both
entered at `5efe626`, plus `RESULT-REG-013.md` which reads the verdict off them. **§10 named none
of the three.** The manuscript names `RESULT-REG-013` exactly once, in §6, for two audience sizes.

WHY THIS ONE IS WORTH THE SPACE. Paper III §11 already carries the repair, in the same register,
for the same failure mode, applied at `-80`: *"That command reproduces the instrument and not the
sample, and the distinction is the whole of this bullet... those logs, not a command, are the
record of §5.3. Nothing in this repository re-derives §5.3's figures from committed data, and this
bullet implied otherwise until wealthTensor-80."* The sibling learned it and the lesson did not
cross the corridor -- through two subsequent whole-manuscript reader-passes over Paper IV, one of
which (`-81`) ran six of §10's named commands. `-81`(ii) says a predecessor's lesson is a map of
where to look hardest; this is that map pointing one manuscript sideways instead of one paragraph
down.

THE REPAIR is charter §2 REPLACE: the record gets a bullet of its own, the command keeps a bullet
but stops claiming to regenerate anything, and §1's promise that "§10 names the command for each"
stays true -- which is a post-condition below, not a hope.

    python3 scripts/wt150_paperIV_reg013_record.py           # idempotent; .bak first
"""
from __future__ import annotations

import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-IV-composition/paper-IV.md"
BAK = PAPER.with_suffix(".md.bak-wt150")

OLD = "- **Regenerate §6:** `python3 scripts/reg013_citation_whitespace.py`\n"

NEW = """- **The record of §6:** `docs/preregistration/RESULT-REG-013-run.log` and
  `docs/preregistration/RESULT-REG-013-run.json`, the committed output of the 2026-08-16 run, with
  `docs/preregistration/RESULT-REG-013.md` reading the verdict off them. **Those files, not a
  command, are the record of §6.**
- **Re-run the instrument:** `python3 scripts/reg013_citation_whitespace.py`. It reproduces the
  instrument and not the pull. Each cluster's audience is the set of works citing its seeds,
  retrieved live from OpenAlex, and that set grows every day; the run is also subject to the API's
  rate limit, and on 2026-08-18 it exited non-zero on `HTTP 429` inside the ceiling control.
  Nothing in this repository re-derives §6's figures from committed data, and this bullet said
  "regenerate" until wealthTensor-82.
"""


def main() -> int:
    text = PAPER.read_text(encoding="utf-8")
    if NEW in text:
        print("wt150: already applied (idempotent)")
    elif OLD not in text:
        sys.exit("wt150: the §10 bullet is not in the form this patch was written against; "
                 "re-read §10 before editing it")
    else:
        shutil.copy2(PAPER, BAK)
        PAPER.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
        print(f"wt150: applied; backup at {BAK.name}")

    t = PAPER.read_text(encoding="utf-8")
    flat = " ".join(t.split())
    checks = [
        ("the regeneration promise is gone",
         "**Regenerate §6:** `python3 scripts/reg013_citation_whitespace.py`" not in flat),
        ("the committed run record is now named",
         "`docs/preregistration/RESULT-REG-013-run.log`" in flat
         and "`docs/preregistration/RESULT-REG-013-run.json`" in flat),
        ("the record, not the command, is called the record",
         "Those files, not a command, are the record of §6." in flat),
        ("the instrument/pull distinction is stated",
         "It reproduces the instrument and not the pull." in flat),
        ("the observed failure is dated and named",
         "on 2026-08-18 it exited non-zero on `HTTP 429`" in flat),
        ("the negative fact Paper III already states is stated here too",
         "Nothing in this repository re-derives §6's figures from committed data" in flat),
        # NEGATIVE, load-bearing: §1 promises §10 names a command for §6. It still must.
        ("NEGATIVE · §10 still names a command for §6",
         "`python3 scripts/reg013_citation_whitespace.py`" in flat
         and "§10 names the command for each" in flat),
        # NEGATIVE, load-bearing: no new SHA entered the manuscript.
        ("NEGATIVE · no new commit SHA was introduced",
         flat.count("5efe626") == 1 and flat.count("fff7063") == 1),
        # NEGATIVE: the §10 pin sentence is untouched.
        ("NEGATIVE · the §10 pin sentence is untouched",
         "the last commit touching\n  `scripts/reg013_citation_whitespace.py`" in t),
        ("§6's own RESULT-REG-013 reference still stands",
         "true-audience sizes are `RESULT-REG-013` §2's" in flat),
    ]
    bad = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n}")
    if bad:
        sys.exit(f"wt150: {len(bad)} post-condition(s) failed")
    print("wt150: 10/10 post-conditions hold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
