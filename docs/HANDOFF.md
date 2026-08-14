---
project: wealth-tensor
gh_sha: ebbb4f141ed2c7596d22037f1bef26f19fc67c52
updated: 2026-08-14
session: wealthTensor-30
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. **`docs/preregistration/RESULT-REG-009.md`** — the run `-30` committed. Read §0 first: it states
   the one reading §11 required, and §4 is a **registered control that FAILED** and is reported
   rather than repaired.
4. `docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.**
   Two parts; §§0–5 are Part I, §§6–12 Part II. **The numbering is 6–12 and not 2–8 by ruling.**
5. `docs/preregistration/RESULT-P0.md` — the evidence §6 cites.

> **`-30` in one line: §3's definition of done is CLOSED — the instrument ran, and the manuscript's
> 99.7 % did not survive contact with the disclosure's own joint distribution.** Ψ = **0.6586**
> [0.6211, 0.6964] on 665 admissible pairs across 577 firms, against Ψ_rect(α̂) = **0.9980** on the
> asserted rectangle at the *same* rate. **P1 HOLDS · P2 HOLDS · P3 FAILS · P4 HOLDS.** §12's three
> manuscript repairs landed in the same session, as registered. And the charter's G-COACH-3 — the
> defensive-sentence invariant declared 2026-08-12 and evaluated zero times since — is **mechanised**.

## 0 · TRANSPORT — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -30 without exception**. Roster join/claim as
`big-wealthTensor-31` — **`roster claim` takes `--resource`, not `--repo`**.
`export LESSONS_CONTRIBUTOR=opus` and **`export GATE_ROSTER_WHO=<you>` at the TOP**, not at the gate.

**THE ROSTER BRAKE IS LIVE.** It fired on both of `-30`'s commits and both were honest
`git add <path>` stagings, so the exit is routine: `ROSTER_BRAKE_ACK=<n> git commit -F <file>` where
*n* must EQUAL the staged count (6 and 7 here). It is a **heads-up after the fact**, not a block;
the block is pre-commit and only refuses the `git add -A` shape.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy.
**732 tests, ~56 s on darwin** (was 690; `-30` added 42).

**NEVER inline a multi-line string in a `dx '...'` argument — a heredoc is not an escape.** Write
locally → `dx --put` → run it / `git commit -F`, and `shasum` every file across. `-30` moved eleven
files that way, all eleven byte-for-byte. **macOS `base64` rejects a bare file argument:**
`cat f.b64 | base64 -d > out`. **Patch scripts beat `sed`; `patchkit` validates every anchor before
writing anything.** `patchkit` reads a shell `# ` comment as a markdown heading — declare
`expect_structure={"#": +N}`, and it applies PER FILE inside one call.

**NEW · NESTED SAME-QUOTE f-STRINGS NEED PYTHON 3.12+.** `f"{', '.join(f'{d[k]}' for k in ks)}"`
parses on the cloud container and **fails on darwin's venv**. Precompute the inner string with
`%`-formatting or a named variable. Cost `-30` one round trip.

**Bulk SEC work: CLOUD, NOT DARWIN.** Settled five times.

## THE FIFTEEN THINGS THAT HAVE EACH COST A SESSION A RUN

1–8 unchanged (registered machinery: `onset_rule="peak"`; `peak_onset` returns a tuple; control arm
in the same pass; the panel is registered machinery; `git log -S` recovers a dangling ordinal; a
feasibility probe that reads the arm label is the experiment; "the latest X" and "the latest Y"
taken independently is comparing two periods).

9. **A MEASUREMENT THAT CANNOT REPRESENT THE ANSWER IS NOT EVIDENCE OF ABSENCE.**
10. **AND ASK IT OF EVERY NON-ZERO TOO — a rate is a claim about whatever the instrument could reach.**
11. **AN ADJECTIVE IN A DESIGN SENTENCE IS AN UNMEASURED QUANTITY UNTIL YOU NAME THE MEASUREMENT.**
12. **AND THE WORST CASE IS THE OBJECTION THE DOCUMENT RAISED AGAINST ITSELF.**
13. **ASK THE INSTRUMENT-ARTEFACT QUESTION OF NUMBERS THAT LOOK GOOD.**
14. **AND OF NUMBERS THAT SETTLE AN ARGUMENT. A COUNT IS A CLAIM ABOUT THE TAG LIST THAT PRODUCED IT.**
15. **NEW · AND OF A REGISTERED CONTROL THAT FAILS — ASK WHETHER THE OPERATOR IS THE ONE THE
    PREDICTION NAMED.** `-30`'s P3 failed on Ψ_band. Before writing that down, the band's bin edges
    were checked against the instrument that PRICED the band and found identical — so the banding was
    inherited, not invented, and the failure is real. But the bins are half-open on the left and
    **55.7 % of the lives are integers**, which sit on a bin's LEFT EDGE, so a midpoint collapse
    **translates** by +0.5 y where §9 said "a one-year *rounding*". **That does not rescue the
    control** — it is reported FAILED, the mechanism is labelled post-hoc, and the alternative
    banding is teed up for its OWN registration so it cannot arrive later as a fix. The general
    rule now lives in `claude-blackbook`.

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace.
**NEW · A SOURCE-TEXT GUARD FIRES ON ITS OWN WITNESS.** F9a greps the instrument's source for
`industry_median` and matched the literal inside its own `witness=lambda: ... "def
industry_median(): pass"`. Fixes, both one line: write the pattern with single-char classes
(`industry[_]median`) so the literal cannot match itself, and **compose the witness world from
fragments** (`"def industry" + "_median"`). Any check whose subject is text it is part of has this.
**The gh_sha dance is NOT a defect.** `--stamp`, then a commit whose whole content is the stamp;
`--check` calls that `ADVISORY: docs-only drift` and **exits 0**. Read the exit code.

## 1 · WHAT HAPPENED

**`f069ab2` — the instrument.** `scripts/reg009_ladder_inputs.py` (+ 12 pinning tests,
`RESULT-REG-009.md`, its run log, `reg-009-result.json`, `reg-009-resolution-audit.json`).
**24 severe checks, 0 definitional, 0 vacuous.**

| | value |
|---|---|
| **Ψ** (`R_MID`, pooled) | **0.6586** [0.6211, 0.6964] · 665 admissible of 683 · 428 distinct pairs · modal 0.026 |
| Ψ by cycle | 0.6326 (2014-15) · 0.6818 (2022-23) — **P1 holds in both separately** |
| **Ψ_rect(α̂ = 0.408)** | **0.9980** · at α = 0.35, 0.9973 · at α = 0.05, **vacuous** (admissible set empty) |
| **S** (`R_MID`) | **0.1391** — 95 of 683 pairs inside the asserted rectangle |
| **Ψ_band** | 0.7236 — **|Δ| = 0.0650, above P3's five points** |
| A (`R_MID`) | 0.974 · 3 pairs inadmissible on property alone, 15 on intangible, 0 on both |

**§12's attribution is PERFORMED, not pointed at.** Moving α from 0.35 to α̂ on the *same* rectangle
moves its answer by **0.0007 — 0.2 % of the 0.339 gap.** The recognition rate is ruled out
quantitatively; support (S = 0.139) and measure (428 distinct pairs, modal 0.026) jointly carry the
rest, and **this design does not decompose those two and says so**.

**`d4c6487` — §12's manuscript repairs, plus G-COACH-3.** §4.4's 99.7 % → the measured share with
its denominator; §4.4's now-redundant sequel sentence CUT and replaced by 0.974 of the 683 pairs;
§4.7's "runs on the sample §5 already collected" → carries 151/98, 55/38, 110 joinable, and 21 per
band against a floor of 30; §7's rectangle row relabelled **asserted** and REG-009 added to the
ledger with six figures, six reach declarations and a new docs-fixture owner.

**`scripts/defensive_count.py` + `tests/test_defensive_count.py` + `DEFENSIVE-BASELINE.json`.** The
charter's §2 invariant was declared 2026-08-12 and evaluated **zero times**, because nothing could
count one. It reports a **delta between two versions of one document**, never a verdict about a
document — which is what survives this estate's own "a crude detector reads as coverage" objection.
The baseline is committed, so a legitimate increase must be raised in the same commit. First live
fire on `-30`'s own pass: **3 → 3. G-COACH-3 holds.**

## 2 · RULINGS — DO NOT REOPEN

- Prior rulings stand: no third disclosure instrument; the two dead (f) keywords stay in `INTERNAL`;
  phrase set frozen at 38; retail PP&E × intangible cells out of §5.4; §4.4 settled; References
  block; §4.5's 400-vs-4,000 not a defect. **`SOURCE-001` IS FINISHED.**
- **THE ARM IS δ.** Reopening it requires a *quoted price* for a delisted-inclusive series.
- **D1 IS RULED: the whole span, with a per-year, per-fiscal-calendar weight.**
- **§4.8 IS NOT THE COINCIDENCE ARGUMENT; §4.7 IS, AND IT COMES WITH A WEAK JOINT.**
- **EVERY P0 AND REG-009 NUMBER IS AN UPPER BOUND** — the *disclosed* δ. F4 asserts it travels.
- **REG-009's NUMBERING IS 6–12 BY RULING.** §§0–5 keep their addresses.
- **§4's COVERAGE SILENCE STAYS RECORDED, NOT REPAIRED.** Honoured twice; do not fix retroactively.
- **NEW · P3's FAILURE IS NOT REOPENED BY RE-BANDING.** A control rescued after it fails is not a
  control. The half-integer-edged banding is REG-010's, in its own document, reported BESIDE this
  failure and never instead of it. F10 refused the seventh free parameter and it passed.
- **NEW · REG-009 IS CLOSED.** §3's six items are done. Anything further is REG-010/REG-011.

## 3 · THE AT-BAT, RANKED

1. **The cheap half of §7.5's tee-up.** Join `reg-006-ladderC-events-corrected.json`'s **151**
   property events to the disclosed lives, bin at D3's 1.00 y, **count how many bands clear 30.**
   One afternoon on committed data, no harvest — and it decides whether REG-011 needs an expensive
   new universe. **The paper now prints "21 per band against a floor of 30" (§4.7), so this count is
   load-bearing for a sentence that is already published.**
2. **REG-010: the half-integer-edged banding, registered before it is run.** §4's tee-up in
   `RESULT-REG-009`. Bins centred on the heap rather than starting on it, so the collapse is a
   rounding and not a translation. **Registered in its own document, reported beside P3's failure.**
   One function and one run on committed data.
3. **Fill the coverage series between §3b's two cycles.** ~1 min download + ~16 s scan per zip,
   **CLOUD**. Raises §7.5's joinable column (110 of 151); **does NOT move the 151.**
4. **The §1.3 grep on paper III's other self-critical passages.** Four sessions, four finds. Still
   the cheapest lead in the repository. `-30` did not run it.
5. **`defensive_count.py` covers paper III only.** Papers I and II have no baseline and no test. Two
   lines each in `tests/test_defensive_count.py` if anyone wants the invariant to mean the estate.
6. **AAR action A2** — the four other `post-*` hooks in `darwin-mac-ops/hooks`. A1 turned up two
   silent bugs in the ONE file it touched; A2 is untouched. Plus A1's residual (State Machine
   `1217468064910605`): make `roster join` write an alias file so a session's identity set survives a
   fresh `dx` shell.
7. **"disclosed rectangle" still appears at lines 964, 996, 1123 and 1573 of paper III**, where it
   denotes the [10,40]×[3,20] product. `-30` renamed it to *asserted* only at the two sites §12
   registered. **86.1 % of the disclosure falls outside it, so the adjective is wrong at all four** —
   a terminology pass, with `test_ledger_provenance` and `test_restatement_reach` re-run after.
8. **The gate defect card** — State Machine `1217465036940491`.
9. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
10. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**
    REG-010 may want it.

## 4 · WHAT WOULD HAVE SAVED `-30` TIME

- **Read `severity.check`'s contract before writing ten witnesses.** A witness returns the SAME
  predicate evaluated in a falsifying world, so it must come back FALSY. Two of `-30`'s witnesses
  shipped without the leading `not` and died on the run — cheaply, loudly, correctly, but twice.
- **Grep the pricing instrument for the rule you are about to re-implement.** `Ψ_band`'s bin edges
  took ninety seconds to find in `reg009_p0_lifetime_values.py` and turned an assertion in a result
  doc into a lifted, checked mechanism. The same ninety seconds is what separates "the control
  failed" from "the control failed and here is why, from two lines of committed source."
- **When a test WRITES tracked files, snapshot and restore them.** `-30`'s rerun test regenerates
  four outputs; without the `finally` restore it would one day be blamed for a dirty tree at the gate.
- **Adding an owner to `test_ledger_provenance` is THREE edits**, not one: the `R<n>` constant, the
  `LEDGER` entries, and the `docs` fixture's enumeration. The `KeyError` from the third is the guard
  refusing to check a figure against a document it was never given.

## 5 · DEFINITION OF DONE (carry this forward)

REG-009 is **done**. The next unit of done is item 1 above, and it has one: *a printed count of
1.00-year property bands clearing 30, committed as `RESULT-REG-010` or as an amendment to §7.5,
after which §4.7's published "21 per band" sentence is either confirmed or narrowed.*
