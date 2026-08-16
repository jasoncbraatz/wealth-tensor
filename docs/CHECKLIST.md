# wealth-tensor — SESSION CHECKLIST (GENERATED — the measured board)

> **GENERATED FILE — do not hand-edit; do not hand-tick.** Criteria live in the
> project's `done-criteria.tsv` (hand-maintained, quoted from ratified docs); status
> below is **measured at generation time** by `handoff-kit/board.py`. Regenerate +
> commit after work that could flip a line — `--check` fails the gate when stale.
> Scoring: this file's git history is the criteria-flip time series.

## The destination (ADR-001, restated once)
Three preprints — II, III, IV — each at "ready to submit", then ONE batch. Nothing ships
early. THE CHARTER STILL WINS; ADR-001 still governs sequencing; this board adds no law, it
makes the existing law COUNTABLE — and now MEASURED (Tier 2: criteria in
`docs/done-criteria.tsv`, status generated; upgraded from hand-ticked 2026-08-16).

## The guard contour (the drift that ate ten sessions, named)
The guard track is PAUSED (Jason, 2026-08-15) and STAYS paused as a default. A new guard is
in-contour only when it names the paper claim it protects and that claim sits on an open
P-line — "which paper sentence does this guard keep true?" is the question ten sessions
never asked. The 61 probes already built are an asset; they are not a destination.

## The board

| lane | layer | status | met |
|---|---|---|---|
| **P1** | corpus | ✅ CLOSED | 1/1 |
| **P2** | corpus | 🧍 PENDING-HUMAN | 0/1 |
| **P3** | corpus | 🧍 PENDING-HUMAN | 0/1 |
| **P4** | corpus | 🔨 OPEN | 0/1 |
| **P5** | corpus | 🧍 PENDING-HUMAN | 0/1 |
| **P6** | corpus | 🧍 PENDING-HUMAN | 0/1 |
| **P7** | corpus | 🧍 PENDING-HUMAN | 0/1 |
| **P8** | corpus | 🧍 PENDING-HUMAN | 0/1 |
| **P9** | corpus | 🧍 PENDING-HUMAN | 0/1 |
| **P10** | corpus | ✅ CLOSED | 1/1 |
| **P1a** | paper-III | ✅ CLOSED | 1/1 |
| **P1b** | paper-III | ✅ CLOSED | 1/1 |
| **P1c** | paper-III | ✅ CLOSED | 1/1 |
| **P1d** | paper-III | ✅ CLOSED | 1/1 |
| **P1e** | paper-III | ✅ CLOSED | 1/1 |
| **P1f** | paper-III | ✅ CLOSED | 1/1 |
| **P1g** | paper-III | ✅ CLOSED | 1/1 |
| **P1h** | paper-III | ✅ CLOSED | 1/1 |
| **P1i** | paper-III | ✅ CLOSED | 1/1 |
| **P1j** | paper-III | ✅ CLOSED | 1/1 |
| **P1k** | paper-III | ✅ CLOSED | 1/1 |
| **P1l** | paper-III | ✅ CLOSED | 1/1 |
| **P1m** | paper-III | 🧍 PENDING-HUMAN | 0/1 |

**The next piece is `P4`.** Work it, or say in your handoff why you worked something else.

## Every criterion, and how it was measured

- [x] P1 · Paper III measured against its ADR-001 DoD clause + PREPRINT-CHECKLIST A, gap by gap, results recorded as P1x sub-rows in this file — **MET** _(file states it)_
- [ ] P2 · Paper III gaps closed in the prose, in the file (WT-079: the deliverable is the paper) — **PENDING-HUMAN** _(P1x is COMPLETE and every sub-row is green as of wealthTensor-52. The one gap P1 found (P1a: an 872-word / 5480-char abstract, 2.85x arXiv's hard ceiling) was closed the same session. Stays manual because the measurer should not also score it -- P7's fresh eyes and P8 are the judges.)_
- [ ] P3 · Paper II re-measured against the same two lists, gaps closed, ready to submit — **PENDING-HUMAN** _(same bar as III; II built the template and must still satisfy it.)_
- [ ] P4 · Paper IV exists as a full draft (own charter + Paper I's surviving subsection + Abandoned Approaches) — **UNMET** _(rc=1)_
- [ ] P5 · Paper IV ready to submit (same two lists, same bar) — **PENDING-HUMAN** _(follows P4; the long pole.)_
- [ ] P6 · Every number in every paper regenerates from a COMMITTED script at the pinned SHA, re-run at close — **PENDING-HUMAN** _(upgrade to cmd: rows per paper as the regen scripts are enumerated (WT-027 lesson: a number without a script is a number nobody has checked).)_
- [ ] P7 · Convergence per paper: fresh-eyes review passes repeat until TWO CONSECUTIVE passes yield ZERO substantive findings — **PENDING-HUMAN** _(perfection==done operationalized; a zero-finding pass is a RESULT and gets its REVIEW doc.)_
- [ ] P8 · Jason's own-hand pass over each converged paper — his voice, his name, the last human step — **PENDING-HUMAN** _(a human gate a script can satisfy is not a human gate. Never auto-closes.)_
- [ ] P9 · The batch declared ONCE when all three are terminal (never ask Jason to trigger a submission) — **PENDING-HUMAN** _(ADR-001 -08; declaring readiness is the session's job, submitting is his.)_
- [x] P10 · Registered in the shared ledger with a calibrated estimate (brake + closer armed) — **MET** _(check passed)_
- [x] P1a · Abstract is 150-250 words AND <=1920 characters -- arXiv's hard metadata ceiling (info.arxiv.org/help/prep.html, re-verified 2026-08-16). Counted on the DECODED string: wc -w and awk NF disagree across platforms on this text — **MET** _(check passed)_
- [x] P1b · Author block carries the name, *Independent researcher* and an email — **MET** _(check passed)_
- [x] P1c · Keywords line carries 6-8 keywords — **MET** _(check passed)_
- [x] P1d · JEL classification codes present — **MET** _(check passed)_
- [x] P1e · Explicit numbered contributions list in the introduction — **MET** _(check passed)_
- [x] P1f · Abandoned approaches is a BODY section, not an appendix (ADR-001: load-bearing in every paper) — **MET** _(check passed)_
- [x] P1g · Limitations is a numbered list and the first item runs against the paper's own comfort — **MET** _(check passed)_
- [x] P1h · Data and code availability names the repo URL, module paths, a regeneration command and the test command — **MET** _(check passed)_
- [x] P1i · No live placeholders. The existence leg is FIRST on purpose: an absence predicate passes vacuously on a missing file (-49's rule), proved red in-session — **MET** _(check passed)_
- [x] P1j · The reproducibility paragraph names BOTH overclaim-forbidding tests (PREPRINT-CHECKLIST B) — **MET** _(check passed)_
- [x] P1k · Pre-registrations cited WITH their registering commit SHAs (PREPRINT-CHECKLIST D) — **MET** _(check passed)_
- [x] P1l · The failed prediction appears in the ABSTRACT as well as the body (PREPRINT-CHECKLIST D; charter 3.4 -- reported once, and not given the last word) — **MET** _(check passed)_
- [ ] P1m · Submission-time head-of-repository SHA pinned in the data-availability statement — **PENDING-HUMAN** _(DEFERRED BY DESIGN, not a gap -- 11 says so in the paper and the per-file pins are what a replicator needs today. Closes at posting, which is P9's moment, not P2's.)_

