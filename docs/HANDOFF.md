---
project: wealth-tensor
gh_sha: 0140d2e9549fd4b30021f0179996a58737cc0302
updated: 2026-08-14
session: wealthTensor-38
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

*`gh_sha` points at the commit this file describes; the only thing added after it is this file, so
`--check` prints `ADVISORY: docs-only drift` and exits 0. `-37` used two commits for that; one is
enough and the meaning is the same.*

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale. `ADVISORY: docs-only
   drift` exits 0 and is NOT a defect. **Read the exit code.**
3. **`docs/preregistration/REG-012-band-count-edge-phase.md`** — `-38`'s registration. **§§1–2 are
   two findings about how the question was ASKED, and they are the session's main result**; §6 is the
   two-branch ruling. Read both before touching anything edge- or band-shaped.
4. `docs/preregistration/RESULT-REG-012-band-edge-phase.md` — **§0 first** (the two defects), then
   **§3** (why one quarter of the phase circle is not one quarter of an argument), then §4.
5. **`docs/preregistration/RESULT-TERM-001.md`** — `-37`'s registration and the one place the
   **five-site ruling** is recorded. §2 before touching any *rectangle*.
6. `docs/preregistration/REG-010-p3-half-integer-banding.md` — **§1 is the population ruling** and §3
   is the two-branch ruling. **§1 is now doubly load-bearing: `-38` found it was violated two
   documents later, by a card, in the other direction.**
7. `docs/preregistration/CONSTRUCTION-REG-010-edge-convention.md` — **§C2 owns the 55.71 %, and owns
   its population in the same sentence.** C3 and C5 are the two a later session walks past.
8. `docs/preregistration/RESULT-REG-010-half-integer-banding.md` — §3 first, then §4.
9. **`docs/preregistration/RESULT-TERM-002.md`** — the **two-numeral ruling**; §2 before §8, §8.1, §A.2.4.
10. `RESULT-PIN-001.md` · `RESULT-SCOPE-001.md` — `-34`'s and `-33`'s repairs.
11. `docs/preregistration/RESULT-REG-009-band-count-filled.md` — `-32`'s run. §4, then §3, then §6.
12. `docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md` — **R5 is load-bearing and `-38`
    did not spend it.**
13. `RESULT-REG-009.md` — **§3's S = 0.1391 is load-bearing in a test.**
14. `REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.** Numbering is 6–12 by ruling.

> **`-38` in one line: THE CARD WAS RIGHT THAT THERE WAS A QUESTION AND WRONG ABOUT BOTH THE NUMBER
> AND THE INSTRUMENT, AND BOTH WERE SETTLED BY READING BEFORE ANYTHING WAS COMPUTED.** Its premise
> — *55.7 % of lives are integers on a left edge* — is **Ψ_band's** statistic over 4098 lives
> (683 pairs × 2 tags × 3 rules); the band count's unit is an **event**, one tag, one rule, one life
> each, and its own edge mass is **63.16 %**. Four boundaries, one number carried across all four —
> **two documents after `REG-010` §1 was written to forbid exactly that.** And the instrument the
> card proposed, *"mass within w/2 of an edge"*, is **1.000 for every band of every sample**: every
> point of a half-open band of width `w` is within `w/2` of its nearer edge. It would have been
> computed, tabled as a description of the heap, and believed.

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-38`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.

**Join with `--replaces`, which no STEP 0 has ever used:**

```
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-39 --replaces "$DARLISH_SESSION" --task "..."'
```

The enrollment auto-joins a `cloud-*` **session** row before you pick a name; `--replaces` absorbs it
instead of leaving a twin. **The CLAIM half of that twinning is fixed as of `-38`** (see §1), so with
`--replaces` you should now be **one name, one session row, one claim row** — the first session that
can be. If `roster who` still shows you twice, that is a finding, not a nuisance.

**`dx --get` IS TEXT-ONLY.** Base64 binaries and `shasum` both ends — dx prints the on-wire byte
count, not the file size, so its own success line certifies nothing (card `1217488245131362`).
**The minute-two shape, run again in `-38` and again worth it:** `tar czf` `docs scripts tests src`
**and** `data` separately on darwin, base64, ONE `--get` each, `shasum` both ends, extract. Every
instrument run, every mutation and both full suites happened in the cloud copy first, so the first
command that touched the real tree had already worked. **And cross the BUILDER, not the artifact:**
`-38` shipped the instrument, ran it on darwin, and the artifact came out byte-identical on both
machines (`e4de7842`) — two interpreters, free reproduction proof.

**SUITE COUNTS — STATE THE COLLECTED COUNT, NOT THE PASS COUNT.** `-37` left *"cloud 806 passed / 8
skipped"* and *"darwin 816 passed"* in this file, and those two numbers **disagreed with each other**:
806 + 8 = 814 ≠ 816. The cloud figure was stale by two tests `-37` itself added after stamping, and
nothing could tell, because a pass count on a machine that skips is not comparable to a pass count on
a machine that does not. **Collected is:** cloud `pytest --collect-only` and darwin's pass count are
the same number when the suite is green, so it cross-checks itself.

| | at `0140d2e` |
|---|---|
| collected | **828** |
| cloud (`PYTHONPATH=<root>/src`) | **820 passed / 8 skipped**, ~229 s, **every skip `not a git work tree`** |
| darwin (`.venv/bin/python -m pytest`) | **828 passed**, ~60 s |

## 0 · THE TELL, NOW IN FIFTEEN SHAPES

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL THAT HAS GONE QUIET (`-32`). `-33`: instruments that agree with
themselves. `-34`: defects nobody introduced. `-35`: defects you are about to introduce. `-36`:
pre-commit the FAVOURABLE outcome's meaning, and an item naming both a document and a population is
two claims. `-37`: a pre-written repair's site count is the one part no anchor can contradict; bind a
repair to the measurement that warrants it, not to a spelling; and a mutation that does not mutate
reports your guard as weak. `-38` adds three:

- **A PROPOSED STATISTIC CAN BE A TAUTOLOGY IN MEASUREMENT'S CLOTHING — EVALUATE IT ON AN ARBITRARY
  INPUT BEFORE YOU BUILD IT.** If it returns the same value for every possible sample it is a
  definition, and it will ship as a green number that reads as coverage. The check is purely
  symbolic, costs one minute, needs no data — and the same minute usually hands you the statistic
  that *does* discriminate, because working out **why** the proposal is constant tells you what the
  constant was hiding. Live fire: *"how much of the modal band's mass sits within w/2 of an edge"* →
  always 1.000 → the quantity it was hiding is the **fractional parts**, which is what edge phase is
  a function of. Banked: `2026-08-14-before-building-instrument-tee-up-proposes`.
- **A CITATION CARRIES ITS POPULATION OR IT CARRIES NOTHING — AND COUNT THE BOUNDARIES.** `-36`
  banked the two-claims version of this; `-38` is the recurrence, and the recurrence is the finding.
  A number reached this session's card across **four** boundaries at once (unit, tag, interval rule,
  selection) and was 7.45 points wrong for the population it was quoted about, **while the rule
  forbidding it sat in a registration two documents earlier, written by the session that had just
  been burned.** *A rule stated inside a document protects that document and nothing else.* To bind,
  it has to leave: a guard, a checklist item, or the habit of treating *names a document AND a
  number* as two verifications. Banked: `2026-08-14-citation-carries-its-population-carries-nothing`.
- **WHEN A QUESTION HAS SURVIVED THREE OR MORE HANDOFFS, GREP THE ESTATE FOR THE ANSWER — NOT THE
  SYMPTOM.** Grep the **identifier by name**, docstrings included, and ask **which consumer actually
  reads it**. Nine handoffs carried `GATE_ROSTER_WHO`; one grep settled it (§1). The tell that you
  are in this failure mode: **a handoff item whose text has grown by observations and not by
  hypotheses eliminated.** Banked: `2026-08-14-question-has-survived-three-handoffs-grep`.

**AND (BUG SPRAY, and an AAR): IN A SHARED TOOLS DIRECTORY THE FILE-CREATION VERB IS THE SAFETY
CHECK.** `git status` showing ` M` where you expected `??` means you did not create a file, you
overwrote one. `-38` destroyed a five-case drill in `~/Scripts` with a whole-file write to a name it
had guessed correctly and never checked, and **every downstream signal was consistent with success**
— the new drill passed, and it correctly went red against the bug. Restored from git, cases merged.
The distinguishing feature is whether a filename is **derived or conventional**: a derived name
forces you to look at what exists (`REG-NNN` numbering did, the same session); a conventional one
lets you guess it right and never look. AAR `drill-name-collision-clobbered-sibling-drill`; banked
`2026-08-14-shared-tools-directory-file-creation-verb`.

**Everything `-33` through `-37` banked is unchanged and still sharp.** A guard must scan assertions,
not quotations. Expose builders, not finished strings or finished rules. Commit-shaped mutations go
in a throwaway worktree. **`severity.check`'s witness must return FALSY** — `-38` tripped the phantom
tag twice by writing witnesses that returned True.

---

## 1 · WHAT HAPPENED

**`ba59370` — REG-012 registered, ALONE, pushed before the instrument existed.** Both defects in the
card established by reading (§§1–2), the population fixed to the cited document's own instrument
(§3), the descriptor specified (§4), the refusals stated as an **absence** to be asserted (§5), and
both branches pre-committed **with the flattering one written at greater length** (§6) — including
the complete list of what a rigid heap would *not* be allowed to mean.

**`0140d2e` — REG-012 performed.** `scripts/reg012_band_edge_phase.py`, 13 severe checks, 0 vacuous.

- **The heap.** 84 of 133 lives sit exactly on a left edge — **63.16 %**, not the card's 55.71 %.
  **Four** distinct fractional values in the entire sample: 0, 1/4, 1/2, 3/4. A 1.00-year band drawn
  on a variable that moves in steps of 0.25.
- **Phase rigidity.** The grouping survives on **1/4** of the phase circle, and **all** of it is the
  interval `(3/4, 1]` above the largest fractional value, where the whole heap moves down together
  and *any* sample's grouping survives — asserted separately as `E4-blind`, so the trivial quarter
  cannot be read as concentration. **Measure strictly below it: 0.0000.** There is no non-trivial
  edge placement under which these 133 events group as they do now. **Branch F.**
- **R5 is not spent.** No edge moved, no floor re-read, **no count of bands computed** — asserted as
  an ABSENCE over the instrument, the result document and the artifact's keys, and mutation-proved
  live in both directions (injected threshold read → exit 1, A1 red; clean → exit 0).
- **One selection path.** `reg009_band_count.selected_lives` extracted from `bands_for` so a
  description of the count's lives cannot read a different sample than the count does.
  **Behaviour-preserving, proved by re-running both committed instruments byte-identical**
  (`6aa58d63`, `6c86b96c`) in a scratch tree, on a different interpreter and machine.

**`darwin-scripts fd4f278` — the nine-session `GATE_ROSTER_WHO` item, CLOSED.** Cause: **nothing had
ever wired it.** The variable appears **nowhere** in the hook chain — it is the *gate's* variable
(`gate-selfcheck.sh`, drilled by `gate-roster-drill.sh`) and `~/Scripts/roster-oncommit.py` read only
`DARLISH_SESSION`. Not lost in transit, not read early: there was nothing to lose and nothing to be
early for. **And the consequence was already written down** — `roster_live.me_names()`'s docstring
says *"ONE session, TWO rows"* in as many words, added the same day the mystery was being re-narrowed
one directory away. `me_names()` taught the **readers** both names; `-38` fixed the **write**.
Drilled three directions, **appended** to the five existing cases; red against the pre-fix hook
(exactly the two new cases, 15/2) and green against the fixed one (17/0). Live proof on the board:
`big-wealthTensor-38 claims Scripts — "roster-oncommit: claim under the name the session gave itself"`.

**`claude-blackbook 82fc9e11` — AAR for the drill clobber**, cause class `unverified-preserved-
behaviour`, lesson adopted so the sweep stops matching it by date. `aar.py sweep` PASSES.

| | |
|---|---|
| **G-COACH-3** | **unmoved — the manuscript was not touched at all** (`git diff --stat` on `docs/papers/` across the session is empty), as REG-012 §6 registered in advance |
| suite | **816 → 828 collected**; cloud 820 passed / 8 skipped, darwin 828 passed |
| new guards | `tests/test_reg012_band_edge_phase.py` (12) + `A1`/`A2` inside the instrument |
| mutations | live absence mutation (instrument, both directions) · numeral guard both directions · premise-convergence guard · drill red-against-old-hook — **each asserted to have actually changed its subject first** |
| lessons | **four** banked global; one adopted by an AAR |
| cards | `1217494219393416` answered · `1217468064910605` closed |

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-37`'s rulings stand verbatim: no third disclosure instrument; phrase set
  frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS THE *DISCLOSED* δ**; **REG-009
  IS CLOSED, numbering 6–12**; **§4's COVERAGE SILENCE AND §7.5's TWO ERRATA STAY RECORDED, NOT
  REPAIRED**; **DO NOT SPEND THE TIE-BREAK**; **DO NOT PROMOTE `R_MIN`**; **`data/reg-009-band-count.json`
  IS `-31`'s**; **`test_the_cycle_choice_now_decides_the_answer` IS A RESULT**; **§10 IS NOT TOUCHED
  BY SCOPE-001**; **SCOPE-001, PIN-001, TERM-001, TERM-002 ARE CLOSED**; **§11 PINS PER FILE**;
  **P3 FAILED AND REG-010 DID NOT RE-SCORE IT**; **REG-010's POPULATION IS Ψ's 683 PAIRS**;
  **NEITHER BANDING IS PROMOTED**; **REG-008 §2's PROVISIONAL FILENAMES STAY and the CONTAMINATED
  probe's DOCSTRING IS LEFT STANDING**; **THE BAND COUNT MAY NOT BE RE-EDGED AND ITS FLOOR RE-READ (R5).**
- **NEW · REG-012 IS CLOSED, ON BRANCH F, AND IT ANSWERS NOTHING ABOUT §7.5.** The band count's
  placement is edge-phase dependent and that is **a disclosure written beside the count, not a permit
  to recount**. R5 forbids re-edging whether the heap is rigid or fragile. **Do not "follow up" by
  running the shifted band count** — that is the measurement REG-012 §7 says is *refused rather than
  merely unperformed*.
- **NEW · THE TWO SENSITIVITIES ARE SEPARATE AND MUST NOT BE MERGED.** `RESULT-REG-009-band-count-
  filled` §4's straddle (registered reading 1, every other 2) is made by the **nearest-cycle
  tie-break deciding 50 of the 133**. Edge phase cannot reach it and REG-012 does not touch it.
  Any sentence that treats "the band count is fragile" as one fact is wrong about which parameter.
- **NEW · REG-012's NUMBERS ARE THE BAND COUNT'S, AND 55.71 % IS Ψ's.** Do not restate either for
  the other population. `tests/test_reg012_band_edge_phase.py` reads both out of the files that own
  them and goes red if they converge.
- **NEW · `selected_lives` IS THE ONE SELECTION PATH.** Anything that needs the lives behind the band
  count calls it. Retyping the selection beside it is the defect the extraction exists to prevent.

---

## 3 · THE AT-BAT, RANKED — **the research ledger is empty; what is left is infra and process**

**`-38` closed the last open research item on paper III.** Nothing below is a paste, and nothing
below is a measurement. That is the cleanest this ledger has been and it is worth saying out loud
before you go looking for something to measure: **if you find yourself designing a new registration,
check first that you are not re-opening a closed one.**

1. **Infra, all carded, all Claude-hands** — the top of the list for the first time:
   `@concierge_ingest` / `@concierge_router` carry the same Caddy ordering defect `@darlish` had
   (`1217488447555628`) · the live capability path is committed in cleartext to `n8n-stack` and the
   repo copy has drifted from live (`1217488117177482`) · **`dx --get`'s byte count and its total
   failure on binary** (`1217488245131362`) — the last one is felt every single session at minute two.
2. **AAR A2's residual** (`1217496462088036`) — A1 is **closed** (§1). What remains is the other four
   `post-*` hooks, and the cheap follow-up `-38` did not take: the enrollment auto-join still creates
   a `cloud-*` **session** row. `roster join --replaces "$DARLISH_SESSION"` is the designed remedy and
   belongs in the STEP 0 text (already in this file's Transport section — **verify it works and then
   say so**, because an untested instruction in a handoff is exactly what item 2 above was for nine sessions).
3. **card-lint's structural false positive** (`1217483699706758`) · **the gate defect card** (`1217465036940491`).
4. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
5. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**
6. **Not mine, not touched:** handoff-lint warns `HANDOFF-acmeLedger-07.md:22` makes a verification
   claim with no vantage point. A sibling was live on it; don't clobber, but it is still open.
7. **A genuine option, and say so if you take it:** with the research ledger empty, the highest-value
   *paper* work is no longer a new row but the **scouting report** the charter §4 schedules before
   posting. It is not carded and it is not started. It needs Jason's ruling on timing, not a session's.

---

## 4 · WHAT WOULD HAVE SAVED `-38` TIME

- **THE FIRST TEN MINUTES DECIDED THE SESSION FOR THE FOURTH TIME RUNNING** (`-35` truth, `-36`
  population, `-37` count, `-38` **premise and instrument**). Both of `-38`'s findings came from
  reading three documents before writing a line, and **neither could have been found afterwards**:
  a tautological statistic returns a clean number and a wrong-population premise is invisible to
  every check on the instrument that uses it. Spend the ten minutes.
- **RESOLVE A NUMBER TO THE FILE THAT OWNS IT, THEN READ THAT FILE'S SENTENCE.** `CONSTRUCTION-REG-010`
  §C2 names its population *in the same sentence as the number*. One `grep 55.7` and one read.
- **DO THE ALGEBRA ON THE PROPOSED STATISTIC BEFORE BUILDING IT.** Thirty seconds of
  `min(v − b·w, (b+1)·w − v) ≤ w/2` saved an instrument that could only ever print 1.000.
- **`severity.check`'s WITNESS MUST RETURN FALSY.** Two phantom-tag failures cost a round trip each.
  The witness evaluates the SAME predicate in a mutated world; a witness returning True means the
  guard cannot fail.
- **CHECK THE NAME BEFORE A WHOLE-FILE WRITE INTO A SHARED DIRECTORY** (`git ls-files <name>`), and
  **append to an existing drill rather than replacing it.** The recovery cost twenty minutes; the
  check costs one command.
- **A PRE-EDIT COPY BEFORE THE TREE IS DIRTIED** if the manuscript will be touched — `--against` has
  no second chance. `-38` did not touch it, which is its own kind of clean.
- **`git commit -F <file>` VIA `dx --put`, `shasum`'d BOTH ENDS.** Never inline a multi-line string
  in `dx '...'`. **`ROSTER_BRAKE_ACK=<n>` MUST EQUAL THE STAGED COUNT** — `-38`'s were 1, 6, 2, 2.
- **`roster leave` BOTH rows at wrap** until item 2 is done: the claim half is fixed, the session
  half is not.
- **STATE SUITE COUNTS AS COLLECTED + SKIPS**, not as two pass counts that cannot be compared (see
  Transport). `-37`'s two figures disagreed with each other in this very file and nothing noticed.
- **CORROBORATE THE LEAVES YOU USED.** `-38` ran `lessons.py doctrine` at student-in and never ran
  `lessons.py use`, so `record-outcome` resolved **zero** leaves at wrap. The quarantine cannot clear
  itself. Run `use` when you read a leaf, not when you remember to.

---

## 5 · DEFINITION OF DONE (carry this forward)

REG-012 is **done**: two defects in the question found by reading before anything ran, the population
resolved from the cited document's own instrument through a single selection path, a descriptor that
reads no threshold, both branches registered alone and pushed before the instrument existed, the
refusal asserted as an **absence** and mutation-proved in both directions, the artifact reproduced
byte-identically on two machines, the suite green, and the card carrying the find **and** the
performance. The `GATE_ROSTER_WHO` fix is **done**: caused, fixed, drilled red-and-green, live-proved.

**The research ledger on paper III is empty.** Every row `RESULT-REG-009` §4 teed up is run, every
repair the `§1.3` grep produced is built, and the last open research question is answered.

The next unit of done is therefore **not a measurement**. It is either item 1 (infra, and `dx --get`
on binary is the one every session pays for) or item 7 (the scouting report, which needs a ruling
before it needs a session). **A session that goes looking for a new registration to write should
first satisfy itself that the estate is asking for one** — the ledger says it is not.
