---
project: wealth-tensor
gh_sha: 66fd4f7011bec911ec1b49019a0f0c47b2e69a4a
updated: 2026-08-14
session: wealthTensor-32
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale. `ADVISORY: docs-only
   drift` exits 0 and is NOT a defect. **Read the exit code.**
3. **`docs/preregistration/RESULT-REG-009-band-count-filled.md`** — `-32`'s run. §4 first (the
   verdict and the parameter the fill created), then §3 (the fill's price), then §6 (the manuscript
   repair, registered and performed).
4. `docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md` — the rules `-32` fixed **in their
   own commit, before any count existed**. `git log --follow` on that file is the ordering proof.
5. `docs/preregistration/RESULT-REG-009-band-count.md` — `-31`'s two-cycle run, **unaltered except
   for the amendment at the end of §4**. Its two errata stay errata.
6. `docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.**
   §§0–5 are Part I, §§6–12 Part II. **The numbering is 6–12 and not 2–8 by ruling.**

> **`-32` in one line: the coverage fill is RUN, the second band did NOT clear — and the fill
> CREATED a free parameter that decides the answer.** 110 of 151 joinable becomes **133 of 151**;
> `[4, 5)` reached **27** against the floor of 30 where `-31`'s proportional bracket predicted 30.2,
> so the unjoined events did not fall like the joined ones. **One band still clears and §7.5's
> verdict stands.** But with two cycles the nearest-cycle rule's **tie-break was structurally
> unreachable** (0 of 110 events equidistant); with nine it decides **50 of 133**, and the count is
> **1 tie-to-earlier, 2 tie-to-later**. Both other cycle picks give 2. `R_MIN` gives 2 under all
> three. **The registered reading is now the only reading that gives one.**

## 0 · TRANSPORT — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -32 without exception**. Roster join/claim as
`big-wealthTensor-33` — **`roster claim` takes `--resource`, not `--repo`**, and **both print
NOTHING on success**; check `$?`, not stdout (`-32` briefly thought a silent join had failed).
`export LESSONS_CONTRIBUTOR=opus` and **`export GATE_ROSTER_WHO=<you>` at the TOP**.

> **`GATE_ROSTER_WHO` STILL DOES NOT REACH THE COMMIT HOOK — third session running.** `-32`'s
> commits printed `[roster] wealth-tensor: 1 live claim(s) by big-wealthTensor-32` and then warned
> **`ROSTER CONTENTION — wealth-tensor is ALSO claimed by: big-wealthTensor-32`**, i.e. the hook
> resolved the committer as the session's `cloud-*` row and read the session's own claim as a
> stranger's. Both rows are you. Live evidence for A1's residual (State Machine
> `1217468064910605`): **`roster join` should write an alias file so a session's identity set
> survives a fresh `dx` shell.** `roster leave` BOTH at wrap.

**ROSTER BRAKE:** stage by path, then `ROSTER_BRAKE_ACK=<n> git commit -F <file>` where *n* EQUALS
the staged count (1, 12 and 3 this session). Heads-up after the fact; the block only refuses `add -A`.

**Never inline a multi-line string in `dx '...'`.** Write locally → `dx --put` → run it, and
`shasum` every file across. `-32` moved eleven files that way, all byte-for-byte. **Patch scripts
beat `sed`; anchor patchkit on a span with NO internal newline** — `-32`'s three edits are three
single-line anchors, each replaced by multi-line text, which is the shape that works.

**Run pytest with `.venv/bin/python`, not `python3`. 772 tests, ~57 s on darwin** (was 753; `-32`
added 19). **In the cloud container pytest is not installed** — `pip install pytest
--break-system-packages`.

**Bulk SEC work: CLOUD, NOT DARWIN.** Settled six times.

## THE SEVENTEEN THINGS THAT HAVE EACH COST A SESSION A RUN

1–15 unchanged (registered machinery; `onset_rule="peak"`; the control arm in the same pass; a
measurement that cannot represent the answer is not evidence of absence; an adjective in a design
sentence is an unmeasured quantity; ask the instrument-artefact question of numbers that look GOOD,
of numbers that SETTLE AN ARGUMENT, and of a REGISTERED CONTROL THAT FAILS).

16. **AND OF THE DENOMINATOR.** `-31`'s. A per-unit average is a claim about the *rule* that
    produced its denominator. For any "X per Y", find the run that produced Y and name its arm.
17. **NEW · AND OF A CHOICE RULE'S TIE-BREAK AT A NEW CARDINALITY. EXTENDING A REFERENCE SET CAN
    CREATE A FREE PARAMETER THAT DID NOT EXIST BEFORE IT, AND THE PARAMETER CAN DECIDE THE ANSWER.**
    At two cycles no event was equidistant, so no registration ever had to name the nearest-cycle
    tie-break. At nine it decides 50 of 133 events and moves the band count across the floor.
    **Before extending any reference set a choice rule matches against, enumerate the rules whose
    TIES become reachable at the new cardinality, register the tie-break in its own commit BEFORE
    the run, and report the mirror convention beside the registered answer.** The standing refusal
    has a harder second form here: the parameter was not *added*, it was **created by the
    measurement**, so the refusal that matters is the refusal to **spend** it.

**Witness contract:** `severity.check`'s witness must return **FALSY**, and a witness that could be
true in a legitimate world dies as VACUOUS rather than reporting. Write witnesses that are
*structurally* false (`{ids} | {sentinel} <= {ids}`), not merely-usually false. **A source-text
guard fires on its own witness** — `-32` sidestepped it entirely by IMPORTING `BIN_RULE_PAT` from
`reg009_band_count` instead of retyping it, so the subject is never written down twice. Do that.

## 1 · WHAT HAPPENED

**`958956a` — the construction, registered before the count.** `CONSTRUCTION-REG-009-coverage-fill.md`
carries R1–R6 and **no number**, so the ordering is provable rather than asserted.

**`35eeaf1` — the fill, run.** Seven cycles `2015-16 … 2021-22` extracted with
`reg009_p0_lifetime_values.py extract`, six zips each, through the committed 2014-15 window
translated by whole years. `scripts/reg009_band_count_filled.py` + 19 tests + result doc + run log.
**21 severe checks, 0 definitional, 0 vacuous. Byte-identical result json on darwin (3.14) and in
the cloud (3.11).**

| | value |
|---|---|
| tier-0 property events | **151** (unmoved; H6 refuses the run if it moves) |
| … joinable, two cycles → nine | **110 → 133** |
| **bands clearing 30 EVENTS, `R_MID` / near — REGISTERED PRIMARY** | **1** — [5, 6): 47 events, 22 firms |
| the second band `[4, 5)` | **27** against a floor of 30 (`-31`'s bracket predicted **30.2**) |
| `R_MID` by cycle pick | near **1** · early **2** · late **2** |
| `R_MID` / near, **tie broken to the LATER disclosure** | **2** |
| by interval rule | `R_MID` **1** · `R_MIN` **2** · `R_WEIGHT` **1** |
| bands clearing 30 **firms**; and in both universes | **0**; **0** |
| decomposition | 23 newly joinable · **14 MOVED band** · 96 unchanged · 18 still unjoined |
| near-pick ties | **0 of 110** two-cycle → **50 of 133** filled |
| residual ceilings on 18 unjoined | adversarial **2** · proportional **2** |

**`66fd4f7` — the manuscript repair, registered in the result doc §6 first.** §4.7's conditional
("*would* bring a second band to the floor *if* the unjoined events fall like the joined ones") is
**REPLACED** by the measurement. Its other clause — "no allocation brings more than a third" — HELD
and is deliberately **not re-asserted**: a bound the measurement has superseded is a hedge kept past
its usefulness. **G-COACH-3 across the edit: 3 → 3 (+0).** `RESULT-REG-009-band-count` §4 gets the
one-line amendment its own tee-up asked for, **appended beside the verdict, repairing nothing**.

**Also measured rather than assumed.** The **1–30 October gap** the abutting windows leave in every
year (8 gaps × 30 days; 26 panel firm-years across 8 firms; **one** of those firms owns a tier-0
event and is joined anyway, so it cost this count nothing) — reported, **not closed by widening the
window**, which would be a parameter chosen after the fact. The **35** duplicate (cik, cycle) rows
`-31`'s last-in-file rule decides. And **P0's nine-point coverage series, 0.723 → 0.817, rising
smoothly rather than in a step** — at P0's level (a parsed life VALUE), **NOT** §3b's tagging rate,
and the two are never plotted as one series.

**The §1.3 grep is RUN** (at-bat item 2, skipped by `-30` and `-31`). Its original form now returns
NOTHING — every needle recurs 2–6 times in POSITIONING / REVIEW-004 / LEDGER. **That is the first
finding**: a grep tell decays as the corpus grows, and the decay looks like a clean bill of health.
The live form — count **instrument** occurrences separately from **prose** — fires immediately, and
found the fifth costume of the §1.3 shape. **State Machine `1217484751716249`, with the repair
pre-written.** See §3 item 1.

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s rulings stand verbatim: no third disclosure instrument; the two dead (f) keywords
  stay in `INTERNAL`; phrase set frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM
  IS δ** (reopening needs a *quoted price*); **D1 is the whole span with a per-year, per-fiscal-
  calendar weight**; **§4.8 IS NOT THE COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009
  NUMBER IS AN UPPER BOUND — the *disclosed* δ**; **REG-009's NUMBERING IS 6–12 BY RULING** and
  **REG-009 IS CLOSED**; **§4's COVERAGE SILENCE STAYS RECORDED, NOT REPAIRED**; **§7.5's TWO ERRATA
  ARE RECORDED, NOT REPAIRED**; **P3's FAILURE IS NOT REOPENED BY RE-BANDING**.
- **DO NOT PROMOTE `R_MIN` TO PRIMARY.** It now clears two bands under **every** cycle choice on the
  filled join, so the temptation is larger than it was for `-31` and the ruling is correspondingly
  firmer.
- **NEW · DO NOT SPEND THE TIE-BREAK.** The chronological convention (tie → earlier disclosure) was
  fixed in `958956a` before any count existed. **Do not flip it, do not switch the cycle pick to
  `early` or `late`, and do not report the mirror as the answer.** The straddle is the result.
- **NEW · `data/reg-009-band-count.json` IS `-31`'s AND IS NOT OVERWRITTEN.** The filled run writes
  `data/reg-009-band-count-filled.json`. `test_thirty_ones_artifact_is_untouched` goes red if a
  future session replaces the two-cycle table with a filled one. *(The old handoff's definition of
  done named the two-cycle filename; its own next sentence said "beside, never instead". **Beside
  wins** — a status report cannot amend a ruling.)*
- **NEW · `test_the_cycle_choice_now_decides_the_answer` IS A RESULT, NOT A DEFECT.** It is the
  deliberate counterpart of `-31`'s `test_the_cycle_choice_does_not_decide_the_answer`, which
  passed on two cycles and does not hold on nine. **A session that "repairs" it has repaired away
  the finding.**

## 3 · THE AT-BAT, RANKED

1. **§10's SCOPE RESTRICTION vs §5's SAMPLE SELECTION — the §1.3 grep's fifth costume, located to
   the line, repair pre-written.** State Machine **`1217484751716249`**. paper-III.md **1919–1921**
   restricts §2's claim to degradation "carrying no impairment trigger, no estimable expected loss
   and no observable event to key recognition to … Where a loss is estimable, recognition is faster
   than the market and §2 predicts nothing" — while `src/wealth_tensor/edgar.py`'s
   `TIER_TAGS_REG006[0]` selects **the entire sample on three recognised-impairment tags**. The two
   sentences are each right in their own section and have never been read in the same sitting;
   neither appears in any instrument. **The repair is a STEELMAN, not a caveat** — a recognised
   impairment marks the *transition into* estimability, so §5's sample is the **boundary** of §10's
   restricted region rather than a violation of it, and that is why timeliness is measurable on it
   at all. **The registration stanza is written out in full on the card.** Paste it into a
   two-paragraph `RESULT-SCOPE-001.md`, perform the edit **on §5 and not on §10**, then
   `defensive_count.py --against` and pytest. *`-32` teed this up rather than performing it because
   its own registration was the coverage fill and a wrong steelman on the paper's central scope
   claim is worse than a correct tee-up.*
2. **AND THE GREP IS NOT EXHAUSTED.** 31 self-critical paragraphs enumerated; 8 read in full.
   Paragraphs **90, 134–139, 185–188, 252, 265, 277–283, 294, 305, 316–317, 322, 347** were NOT
   read. Re-run with the **instrument-vs-prose split** as the discriminator, not the raw count.
3. **REG-010: the half-integer-edged banding, REGISTERED BEFORE IT IS RUN.** §4's tee-up in
   `RESULT-REG-009`. Bins centred on the heap rather than starting on it. In its own document,
   beside P3's failure, never instead of it. **The filled join is now the population it should run
   on** — 133 events, not 110 — and `reg009_band_count_filled.chronological()` hands it that index
   in one call.
4. **"disclosed rectangle" at paper III lines 964, 996, 1123, 1573.** 86.1 % of the disclosure falls
   outside it, so the adjective is wrong at all four. **The registration stanza is pre-written in
   `-31`'s handoff §3 item 4** (recover it with `git show 958956a~1:docs/HANDOFF.md`) — paste into a
   two-paragraph `RESULT-TERM-001.md`, perform, then re-run `test_ledger_provenance` +
   `test_restatement_reach`. **Three sessions old.**
5. **AAR A2** — the four other `post-*` hooks in `darwin-mac-ops/hooks`; plus **A1's residual**
   (State Machine `1217468064910605`), for which `-32` is the third consecutive session's live
   evidence (§0 above).
6. **card-lint's structural false positive** — State Machine `1217483699706758`, fix shape included.
7. **The gate defect card** — State Machine `1217465036940491`.
8. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
9. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**
   REG-010 may want it.

## 4 · WHAT WOULD HAVE SAVED `-32` TIME

- **The zips are ~6 SECONDS each, not the ~1 minute the last handoff priced.** 30 zips (the whole
  2015q4–2023q1 series) is **13 GB and ~3 minutes** at ~54 MB/s, inside a 30 GB container allowance
  if you delete them after. The scan, not the download, is the cost: **~2 min per six-zip cycle**.
  A whole nine-point series is one coffee, not one afternoon.
- **`mkdir -p` the `--out` directory first.** `-32` lost a two-minute extract to
  `FileNotFoundError` *after* the scan finished, because `pathlib.write_text` does not create
  parents and the failure lands at the very end.
- **RE-EXTRACT A COMMITTED CYCLE BEFORE RUNNING NEW ONES.** Re-running the 2014-15 extract
  reproduced `data/reg-009-p0-lives-2015.json` **object-identical** on a different interpreter. That
  is the cheapest possible proof that the invocation, window and zip set match the published one —
  ninety seconds that make every later number attributable to the fill rather than to the harness.
  It is `-31`'s "reproduce the published table" rule applied to an *input* rather than an output.
- **`scripts/defensive_count.py` takes a PATH argument** and is meaningless without `--against`.
  Its own docstring says the level is not evidence; only the delta is.
- **Ask what a larger reference set does to the MATCHING RULE, not just to coverage.** `-32` nearly
  reported "the fill confirms one band" — which is true, and which would have hidden that the
  registered reading had become the only one producing it. The decomposition (item R4 of the
  construction doc) was registered before the number existed *because* that question was asked
  first, and it is the reason the session has a finding rather than a confirmation.

## 5 · DEFINITION OF DONE (carry this forward)

The coverage fill is **done**: the count is recomputed on the filled population, committed, pinned
by 19 tests, reported beside `-31`'s row, and the published sentence it prices has been repaired to
carry it. **It commissioned REG-011 rather than retiring it** — on the registered rule, one band
clears and the expensive half arrives — **and it also demoted the confidence in that verdict**,
because the registered reading is now the only one of four that produces it.

The next unit of done is **item 1 above**, and it has one: *`RESULT-SCOPE-001.md` written from the
stanza on the card, the one-sentence steelman performed on §5 (not §10), G-COACH-3 evaluated across
the edit with `--against`, and the full suite green.* That is a paste-and-perform, not a search.
