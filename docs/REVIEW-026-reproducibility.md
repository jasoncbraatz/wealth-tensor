---
review: REVIEW-026
title: "The rows nobody could falsify — a rule, a census of it, and the one false sentence it turned up"
session: wealthTensor-86
opened: 2026-08-18
closed: 2026-08-18
instrument: scripts/wt156_reproducibility_sweep.py
repairs: [scripts/wt157_paperIV_s10_reg013_rerun.py, scripts/wt158_twelve_point_four.py, scripts/wt159_tsv.py, scripts/wt159b_tsv.py]
before_rev: b50bccd
# ---------------------------------------------------------------------------------
# THE PREDICTION WAS COMMITTED BEFORE THE SWEEP WAS RUN — commit 127cec9, with every
# `measured_` field reading PENDING. wealthTensor-84 established the rule: a count
# written down after the fact is an argument, not a measurement. The predicted numbers
# were reasoned out from the 90 distinct `evidence` strings across the 129 rows and from
# the detector definitions. They were WRONG BY THREE, all in the same direction, and §2
# names the three rows the prediction missed.
# ---------------------------------------------------------------------------------
predicted_D1_record_in_a_vanished_session: 35
predicted_D2_no_operand: 8
predicted_total_flagged: 43
predicted_beyond_the_sixteen: 27
measured_D1_record_in_a_vanished_session: 36
measured_D2_no_operand: 10
measured_total_flagged: 46
measured_beyond_the_sixteen: 30
sixteen_agreed_with_their_old_note: 12
sixteen_whose_recorded_value_had_legitimately_moved: 2
sixteen_disagreed_with_their_old_note: 2
false_sentences_found: 1
notes_corrected: 4
flagged_at_HEAD_after_repair: 0
suite: "1095 passed, 0 failed, 69.66 s"
falsifiers:
  - "Run `python3 scripts/wt156_reproducibility_sweep.py --rev b50bccd --json` and read `n_d1`
     and `n_d2`. If they are not 36 and 10, this review is wrong."
  - "Run `python3 scripts/wt156_reproducibility_sweep.py` at HEAD. If it does not return 0 with
     11/11 post-conditions, the repair claimed here did not land."
  - "Take any of the 46 promise_ids, run the command its `evidence` column now names, and compare
     against the value its `note` now records. If they differ, the row is FALSE and §3's
     agreement count is wrong."
  - "Check out `b50bccd`, run `python3 -m pytest tests/test_excess_demand.py -q` and grep the
     module for an assertion of 4. If you find one, §4's claim that §10's twelve-point four was
     unasserted is wrong and wt158 was unnecessary."
  - "The detectors read the `evidence` column ONLY. Re-run with the `artefact` column allowed to
     rescue a row and the flag count collapses to near zero. §2 argues the header forbids that;
     that argument is the thing to attack."
---

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

# REVIEW-026 — the rows nobody could falsify

## 1 · What was asked and what came back

`docs/promises-adjudicated.tsv` states its own falsification procedure in its header:

> 1. Take the row's `evidence` column. It names a command to run or a file to read.
> 2. Run it or read it. If it does not show what `note` says it shows, the row is FALSE.

wealthTensor-85's census (REVIEW-025) asked whether an adjudication had READ its artefact or merely
LOCATED it. This pass asked the prior question: **can step 1 be carried out at all, today, by a
reader who was not in the session that wrote the row?** A row that cannot reach step 2 can never be
falsified, and wealthTensor-83 already priced an unfalsified row: nothing.

`scripts/wt156_reproducibility_sweep.py` flagged **46 of 129** rows — **36** under D1 (the evidence
locates the record in a session, a log or a machine, and nothing re-executable survives once those
locators are stripped) and **10** under D2 (the evidence is a verb or a back-reference with no
operand). All 46 are repaired in this pass with a command that runs today and the value it returned
today. The sweep returns **0** at HEAD, with 11/11 post-conditions, 4 of them NEGATIVE.

**The headline is not the 46.** It is that one of the sixteen rows the handoff named turned out to
sit on a **false sentence**, and it was false in the direction nobody checks: the manuscript
claimed a test module ASSERTED a number, and the module asserted no such thing. §4.

## 2 · The rule, the prediction, and the three rows the prediction missed

The handoff commissioned a rule — *a run with no committed output file, no printed value in the
note, and no named test* — and a post-condition: all sixteen must flag at `b50bccd`. **They
contradict each other.** Five of the sixteen carry real values in their notes (`D(0)=1998.9895`;
`4.12x`; `9 severe, 0 definitional, 0 failed`), so the literal rule cannot flag them. This is
wealthTensor-85(ii) arriving a second time: when a commissioned post-condition contradicts the
commissioned rule, the handoff has bundled two failure modes under one name.

The rule actually implemented is the header's own step 1, applied to the column the header names:

> **A row is re-runnable iff its `evidence` column carries a HANDLE** — a path with a known
> extension, a git object id, a `§` or `L` pointer, a quoted search pattern, a named test function,
> or a programme identifier (`PRE-002`, `REG-013`, `WT-059`) — **once session and machine locators
> are stripped out.**

Reading the `evidence` column *alone* is not a narrowing chosen to make the count come out. It is
the header's contract about which column carries the handle. Several flagged rows do name a runnable
command in their `artefact` column, and that is a weaker claim than the header makes: the artefact
says *what the sentence is about*, the evidence says *what the adjudicator did*. Allowing the
artefact to rescue a row collapses the count to near zero and makes the file unfalsifiable by
construction — which is exactly the failure this sweep exists to detect. The falsifier block invites
the attack.

**The prediction, committed at `127cec9` with every measured field reading PENDING, was 35 / 8 / 43.
The measurement was 36 / 10 / 46 — three too low, all three in the same direction.** The three
missed rows:

| row | evidence at `b50bccd` | detector |
|---|---|---|
| `6c9aacc322` | `ls -l + git ls-files on darwin, wealthTensor-82` | D1 |
| `01ed28c1a8` | `grep for each of the three names in the script and the module` | D2 |
| `1d538d6e60` | `grep -n E7 on the script` | D2 |

The first was simply overlooked in a hand-read of the evidence vocabulary. The other two are the
more interesting miss: both *name a real operation* and read as runnable, and neither is — "the
script" and "the module" are pronouns. A human skimming the vocabulary supplies the referent from
the artefact column without noticing they have done it. **The machine could not, which is the whole
argument for running the sweep rather than reading the list.**

## 3 · The sixteen, re-run

Every one of the sixteen was executed on darwin on 2026-08-18. Eight of them are expensive — one
re-pulls EDGAR `companyfacts`, one calls a live OpenAlex endpoint, two are the full suite — and all
eight returned.

| outcome | count | rows |
|---|---|---|
| agreed with its old note | **12** | `ac16838bdb` `d6c6430592` `314390a26e` `f7674cbd06` `070d5c7a60` `a01f12e7be` `f8f41df587` `e91d103026` `4c35bb44b7` `12dc448265` `41744fe2ae` `a00820b165` |
| recorded value had legitimately moved | **2** | `6d9934a0bc` `c14cdd1f1b` |
| **disagreed with its old note** | **2** | `d4dd6baf17` `10d2d456ea` |

**The two that moved** are the two pytest rows. Their notes read *"1090 passed, 0 failed, 68.73 s at
HEAD 73b77f9"*. Today the suite is 1095 at a different HEAD. The note was **correctly pinned** — it
named the HEAD it measured — and both sentences are about the suite at the *registered* commit
`d655501`, which `tests/test_paper_test_counts_are_derived.py` asserts. Nothing failed here; a
HEAD-indexed value simply cannot be re-checked at a HEAD that has moved, which is worth knowing
before the next session writes one down.

**The first disagreement — `d4dd6baf17`, and it is a good one.** The note said, of
`scripts/reg013_citation_whitespace.py`: *"a clean run would not regenerate §6 either — the audience
is a live citing set that grows daily."* A clean run on 2026-08-18 returned **RC 0** and **every
figure §6 reports, unchanged**: intersections 23 / 15 / 6, overlaps 0.0202 / 0.0108 / 0.0053,
split-half intersections 134 / 155 / 380, pooled ceiling 0.4773, floor 0.0, `H1 SURVIVES`. Only the
seed `cited_by` counts — which §6 does not report — had moved, and two of the four audience sizes
were byte-identical two days on. The row's class (R) and wealthTensor-82's repair both stand: §10 was
right that nothing here re-derives §6 *from committed data*. What was wrong was the stronger claim
smuggled in beside it. `scripts/wt157_paperIV_s10_reg013_rerun.py` rewrites the bullet to say
**replication, not regeneration**, keeps the load-bearing sentence verbatim, and — the point of this
whole at-bat — **commits the re-run's own JSON** as
`docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json`, so the claim about the re-run is itself
a row anyone can check. That new artefact reference emitted a new promise, `df3cdc8d2a`, adjudicated
in the same pass.

## 4 · The false sentence

**`10d2d456ea` and `30191fec1a` both stood on `read the module`, and the module did not say it.**

Paper IV §10 said, and had said since the section existed:

> §5's **399** interior grid points and §8's twelve-point **four** are *asserted* by
> `tests/test_excess_demand.py` rather than printed by it, so that command's output is a verdict
> and not a table.

The 399 is asserted, at `assert grid.size == 399`. **The four was asserted nowhere.** The module's
only twelve-point test counts DEMAND CURVES and asserts 25; no line in it ever built the twelve-point
EXCESS-DEMAND set, which is the object §8's four counts. The two rows adjudicating those sentences
carried the evidence `read the module` and `read the module` — and nobody could tell, from either
row, which lines had been read.

§8's number is nonetheless **right**: measured on darwin, the 12-point grid returns exactly **4**
distinct excess-demand schedules across the 25 allocations. So the honest repair is not to weaken
the manuscript but to give the artefact the property the sentence claimed for it.
`scripts/wt158_twelve_point_four.py` adds
`test_the_twelve_point_grid_returns_the_four_schedules_section_8_reports`, with 10 post-conditions,
5 NEGATIVE. §8's four is now machine-checked, and both sentences are true rather than softened. The
suite is 1094 → **1095**.

**Four notes were corrected** without any sentence failing: `d9f85198a4` and `ff83025f93` shared a
note claiming *"RESULT-001-* logs entered at d655501 and the analysed result later"* — `RESULT-001-wt026.md`
is IN `d655501`; PRE-002's own outcome, `RESULT-002-wt026.md`, is the one that came later, at
`c43c484`, twelve minutes on. `150f86a167` put *"written before the leg ran"* in E1 §2.2; §2.2 is the
type check and §6 is where that sentence lives. `d4dd6baf17` is §3's.

## 5 · What this does to REVIEW-024's [3, 47], and one blind spot found in wt154

**One sentence in 46 rows was false. Wilson 95% on 1/46 is [0.4 %, 11.3 %]; the interval does not
narrow REVIEW-024's [3, 47] of 129 and is not entitled to, because the 46 are a targeted stratum
rather than a draw and their defining property — unrunnable evidence — is not the property [3, 47]
estimates; the only thing this pass moves is the FLOOR, which is now one known-and-repaired false
sentence higher than it was.** That is the one sentence the at-bat asked for, and the temptation it
resists is the same one REVIEW-025 §3 named: a stratified count is not the population rate.

**The blind spot.** wt159's first repair gave `d0729375b9` the evidence
`git merge-base --is-ancestor fff7063 5efe626; echo $?` — the exactly right instrument for a claim
about ORDER. **wt154 flagged it**, D1, *"evidence names no content-printing operation"*, because
`merge-base --is-ancestor` writes nothing to stdout and answers with an exit code. wt154 is wrong
here and the row is not: an exit code is a read of behaviour, the same class wt154 already declines
to flag when a named test's pass/fail is the verdict. Rather than widen a committed instrument's
criterion inside a pass that is not about that instrument, `wt159b` widened the **evidence** — the
predicate stays and two timestamps are added beside it — and the defect is carded. A future session
that repairs a row with a predicate will hit this again.

## 6 · State inherited and handed on

| gate | before | after |
|---|---|---|
| `pytest tests/ -q` | 1094 passed, 0 failed | **1095 passed, 0 failed, 69.66 s** |
| `wt148_promise_sweep.py` | RC 0, 129 adjudicated | **RC 0, 130 adjudicated** (III 88, IV 42) |
| `wt133_crossref_sweep.py` | RC 0 | **RC 0** |
| `wt154_evidence_discrimination_sweep.py` | RC 0, 0 flagged | **RC 0, 0 flagged** |
| `wt156_reproducibility_sweep.py` | — | **RC 0, 0 flagged, 11/11 post-conditions** |
| coach | III 5 / 0, IV 1 / 0 | **III 5 / 0, IV 1 / 0** |

Papers I and II remain out of `#scope`; 28 promises there are checked by nobody, the sweep prints it
on every run, and **five** passes have now parked it deliberately.
