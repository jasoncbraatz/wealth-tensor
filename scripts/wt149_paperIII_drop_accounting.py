#!/usr/bin/env python3
"""wt149 · Paper III §11 — the drop-accounting bullet promised a per-tier breakdown the run
logs do not carry, and told the reader to run a check the artefact makes impossible.

THE FINDING (wealthTensor-82, `III-1`, found by `scripts/wt148_promise_sweep.py`)
--------------------------------------------------------------------------------
§11 said the attrition "by universe and by tier, is in the run logs", and then instructed:
*"A reader should check that attrition does not differ systematically by tier, since
differential attrition is the one selection channel capable of manufacturing the reported
null."* Both run logs were read end to end. They carry a flat drop table of ten buckets per
universe and no per-tier breakdown of any of them; the only tier-keyed numbers in either log
are the SURVIVING events' lag distributions and one bucket, `ambiguous_tier`, which counts
charges whose tier could not be resolved -- the opposite of attrition from a tier.

The instrument agrees: `src/wealth_tensor/edgar.py` declares `DROP_BUCKETS` and every
increment in the file is `drops["<bucket>"] += n`. The counter has no tier key, so the
breakdown the sentence promised was never recorded by anything.

This is `-79`'s class exactly -- a promise ABOUT an artefact, which checking the artefact's
existence does not check -- and it is the sharpest instance in the corpus, because the
sentence does not merely describe the artefact, it hands the reader a task the artefact
cannot support, on the paper's own account of the one channel that could manufacture its null.

THE REPAIR is charter §2 REPLACE, not ABSORB: the claim is narrowed to what the logs bear
(per bucket, per universe), the absence is stated positively as a fact about the counter, and
the check that DOES exist -- the registered label-permutation control, whose null is printed
in the same logs -- takes the place of the one that does not. No hedge is added; a sentence is
deleted and a narrower one replaces it.

    python3 scripts/wt149_paperIII_drop_accounting.py        # idempotent; .bak first
"""
from __future__ import annotations

import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
BAK = PAPER.with_suffix(".md.bak-wt149")

OLD = """- **Drop accounting for §5**, as required by the registrations: the per-bucket attrition from
  candidate charges to the 688 analysed events, by universe and by tier, is in the run logs at
  `docs/preregistration/RESULT-002-*-run.log`. **A reader should check that attrition does not
  differ systematically by tier, since differential attrition is the one selection channel capable
  of manufacturing the reported null.** It is reported there whether or not it flatters the result."""

NEW = """- **Drop accounting for §5**, as required by the registrations: the attrition from candidate
  charges to the 688 analysed events is in the run logs at
  `docs/preregistration/RESULT-002-*-run.log`, one log per universe, counted per drop bucket. It
  is reported there whether or not it flatters the result. **The count is per bucket and not per
  tier.** `edgar.py`'s `drops` counter is keyed by bucket alone, so *does attrition differ
  systematically by tier?* — the one selection channel capable of manufacturing the reported null
  — is not answerable from these logs. What the registrations put in its place is the
  label-permutation control printed in the same logs, which permutes the tier labels while
  holding the lag distribution fixed; in the pilot its null runs at mean **+0.007**, standard
  deviation **1.025** over 1 000 draws, against an observed *z* of **−0.290**. This bullet
  promised a per-tier breakdown until wealthTensor-82."""


def main() -> int:
    text = PAPER.read_text(encoding="utf-8")
    if NEW in text:
        print("wt149: already applied (idempotent)")
    elif OLD not in text:
        sys.exit("wt149: the §11 bullet is not in the form this patch was written against; "
                 "re-read §11 before editing it")
    else:
        shutil.copy2(PAPER, BAK)
        PAPER.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
        print(f"wt149: applied; backup at {BAK.name}")

    t = PAPER.read_text(encoding="utf-8")
    flat = " ".join(t.split())
    checks = [
        ("the promise is gone",
         "by universe and by tier, is in the run logs" not in flat),
        ("the reader-instruction sentence is gone",
         "A reader should check that attrition does not" not in flat),
        ("the narrower claim is present",
         "The count is per bucket and not per tier." in flat),
        ("the absence is attributed to the counter, not to the log's author",
         "`edgar.py`'s `drops` counter is keyed by bucket alone" in flat),
        ("the surviving check is named",
         "label-permutation control printed in the same logs" in flat),
        ("the permutation null is quoted from the log",
         "mean **+0.007**" in flat and "**1.025**" in flat),
        ("the log glob still points where it pointed",
         "`docs/preregistration/RESULT-002-*-run.log`" in flat),
        ("688 is untouched", "688 analysed events" in flat),
        # NEGATIVE, and load-bearing: the repair must not invent a new artefact to lean on.
        ("NEGATIVE · no new file or command is named in this bullet",
         "RESULT-002-*-run.log" in flat and "attrition-by-tier" not in flat),
        # NEGATIVE: the edit stays inside §11.
        ("NEGATIVE · §5 and §A.2 are untouched",
         t.count("Drop accounting for §5") == 1),
    ]
    bad = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n}")
    if bad:
        sys.exit(f"wt149: {len(bad)} post-condition(s) failed")
    print("wt149: 10/10 post-conditions hold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
