---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-14
session: wealthTensor-29
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. **`docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — READ THE HEADER NOTE FIRST.**
   The file is now in two parts. §§0–5 are Part I (the arm, the four decisions, P0's declaration,
   the definition of done, P0's stopping rule). **§§6–12 are Part II, committed by `-29` alone** —
   D2/D3/D4 fixed, the registered quantities, the seven questions, the predictions, ten falsifiers,
   the stopping rule. **The numbering is 6–12 and not 2–8, on purpose; the header note says why.**
4. `docs/preregistration/RESULT-P0.md` — the evidence §6 cites.
5. §7's SEEN/UNSEEN table before you compute anything, then §12's stopping rule.

> **`-29` in one line: REG-009 is now a registration rather than a design note — and the seventh
> unmeasured quantifier turned up in paper III's own REPAIR, in the clause "it runs on the sample
> §5 already collected."** Counted: **55 property events across 38 firms** as §5 collected them,
> **151 across 98** on the `REG-006`-repaired tag list. **The mirror tell caught this session's own
> first draft**, which had shipped the 55 alone and read as a refusal — the repaired count is 2.7×
> larger and changes the verdict to MARGINAL. **The tell now has three shapes: a number that
> disappoints, a number that pleases, and a number that SETTLES AN ARGUMENT.** A count is a claim
> about the tag list that produced it.

## 0 · TRANSPORT — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -29 without exception**. Roster join/claim as
`big-wealthTensor-30` — **`roster claim` takes `--resource`, not `--repo`**.
`export LESSONS_CONTRIBUTOR=opus`. **`export GATE_ROSTER_WHO=<you>` at the TOP**, not at the gate.

**NEW · THE ROSTER BRAKE IS LIVE AND IT WILL STOP YOU (`-29` built it, AAR A1).** `pre-commit` now
refuses a commit when another **fresh** (<4h) session claims the repo AND more than one path is
staged AND **nothing dirty is left unstaged** — the `git add -A` fingerprint. **It blocked its own
author's first commit**: four files staged by path, nothing else dirty, one live sibling. Exits, in
order: stage by path · `ROSTER_BRAKE_ACK=<n> git commit ...` where *n* must equal the staged count ·
`git commit --no-verify`. Not a bug, a known false-positive shape — see State Machine
`1217468064910605`.

**NEW · `patchkit` READS A SHELL `# ` COMMENT AS A MARKDOWN HEADING.** Patching a hook or any
`.sh`/`.py` file with a block comment raises `StructureError` until you declare
`expect_structure={"#": +N}`. And `expect_structure` applies **per file inside one call**, so a
multi-file patch with different deltas needs **one `apply_edits` call per file**. Cost `-29` two
round trips.

**macOS `base64` REJECTS A BARE FILE ARGUMENT.** `cat f.b64 | base64 -d > out`, never `base64 -d f`.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy.
**690 tests, ~42 s on darwin.**

**NEVER inline a multi-line string in a `dx '...'` argument — AND A HEREDOC IS NOT AN ESCAPE.**
Write locally → `dx --put` → run it / `git commit -F`, and `shasum` every file across. `-29` moved
eight files that way, all eight byte-for-byte. **Patch scripts beat `sed`; verify EVERY anchor
before writing ANY file** — patchkit does both and it refused a bad write twice this session.

**Stage by PATH. Never `git add -A` on darwin** — and now the brake enforces it.

**Bulk SEC work: CLOUD, NOT DARWIN.** Settled five times. `data.sec.gov`/`www.sec.gov` are fast
(630 MB zip < 1 min, full `txt.tsv` scan ~16 s). **No free equity price series is reachable.**

## THE FOURTEEN THINGS THAT HAVE EACH COST A SESSION A RUN

1–8 unchanged (registered machinery: `onset_rule="peak"`; `peak_onset` returns a tuple; control arm
in the same pass; the panel is registered machinery; `git log -S` recovers a dangling ordinal; a
feasibility probe that reads the arm label is the experiment; "the latest X" and "the latest Y"
taken independently is comparing two periods).

9. **A MEASUREMENT THAT CANNOT REPRESENT THE ANSWER IS NOT EVIDENCE OF ABSENCE.**
10. **AND ASK IT OF EVERY NON-ZERO TOO — a rate is a claim about whatever the instrument could reach.**
11. **AN ADJECTIVE IN A DESIGN SENTENCE IS AN UNMEASURED QUANTITY UNTIL YOU NAME THE MEASUREMENT.**
    The cheap tell is a grep: an objection keyword occurring exactly ONCE is an objection nobody answered.
12. **AND THE WORST CASE IS THE OBJECTION THE DOCUMENT RAISED AGAINST ITSELF.**
13. **ASK THE INSTRUMENT-ARTEFACT QUESTION OF NUMBERS THAT LOOK GOOD** (`-28`, on a 99.8 % recovery
    from a band holding one distinct value).
14. **NEW · AND OF NUMBERS THAT SETTLE AN ARGUMENT. A COUNT IS A CLAIM ABOUT THE TAG LIST THAT
    PRODUCED IT.** `-29` was one paragraph from publishing a feasibility refusal built on 55 events
    from a tier tag list **this repository had already repaired**; the repaired count is 151.
    Cheapest check in the family: when two artifacts of one population exist and one is labelled
    *corrected*, **diff their counts before quoting either**.

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace.
**Manuscript:** `patchkit.apply_edits`, never `sed`. Back the file up first.
**The gh_sha dance is NOT a defect — do not "fix" it.** `--stamp`, then a commit whose whole content
is the stamp. `--check` calls that `ADVISORY: docs-only drift` and **exits 0**. Read the exit code.

## 1 · WHAT HAPPENED

**`0dbbdef` in `wealth-tensor` — one file, no instrument code.** REG-009 Part II (§§6–12), plus
three dated pointers appended to Part I in §1.3a's manner (the header numbering note, §1.6a, and a
disposition line on §3's item 3). **Nothing in Part I was rewritten.** 690 tests green.

**§3's definition of done: items 1, 2, 3, 5 and 6 are now DONE. Item 4 is the only one left.**

**THE NUMBERING, because it will look wrong at first glance.** Part I said "§§2–8 are deliberately
absent" while §§2–5 already existed: 2–8 named the *template's* slots (REG-007/008 run
3 quantities · 4 questions · 5 predictions · 6 not-doing · 7 repairs · 8 falsifiers · 9 stopping)
and §§2–5 were this file's own scaffolding. **Resolved by ADDITION.** §§0–5 keep their addresses
because `RESULT-P0` §4 cites "REG-009 §4" and `tests/test_reg009_design.py` cites §1.3 — and
re-addressing a pre-commitment after seeing its result is the move a pre-commitment exists to
prevent. **Do not renumber it later "for tidiness."**

**THE EXPERIMENT REG-009 NOW REGISTERS.** §4.4 evaluates its first rung over a **400 × 400 uniform
grid** on a rectangle **asserted** in `wt088_disclosed_ladder.py` as `LIFE_PPE = (10, 40)` and
`LIFE_FIN = (3, 20)`, with δ₀ and δ₁ swept **independently** — and the **99.7 %** the manuscript
quotes is computed at **α = 0.35**, a rate that appears nowhere in the paper (verified by running
`wt088`; at the paper's own α = 0.05 the number is 0.0 %). A filing does not supply a rectangle. It
supplies **one point, both coordinates chosen by one management on one page**. Ψ replaces the
product measure on an assumed support with the **empirical joint distribution**: **683 paired
firm-years across 577 firms** (321 and 362 by cycle, 106 firms in both), all three D2 rules
resolvable on every one. **P2 predicts against this project's own published number.**

**D2/D3/D4, FIXED — AND D2 REFUSES THE RULE THAT SCORES BEST, ON PURPOSE.** `R_MIN` leads P0-c's
recovery column partly because it **heaps hardest** (87.5 % integers, 46 distinct values over 1,206
property firm-years), which is an argument about the disclosure wearing a rule's costume — and it
collapses both tags toward each other **along the exact axis of §7's comparison**. `R_MID` is
primary (the only rule using both disclosed endpoints); `R_WEIGHT` is amount-backed on both tags in
**273 of 683 pairs (0.400)** and cannot be primary on a count. D3 → 1.00 y / property / `R_MIN`, the
one rung clearing §4 at coverage ≥ 0.80, used here as the heaping-robustness row Ψ_band. D4 →
firm-specific; the industry-median variant is **not run at all** and F9 asserts the absence.

**AAR A1, DEFERRED SIX SESSIONS, IS BUILT** — `darwin-scripts 27bea21`, `darwin-mac-ops a4bde04`.
See §3.

## 2 · RULINGS — DO NOT REOPEN

- Prior rulings stand: no third disclosure instrument; the two dead (f) keywords stay in `INTERNAL`;
  phrase set frozen at 38; retail PP&E × intangible cells out of §5.4; §4.4 settled; References
  block; §4.5's 400-vs-4,000 not a defect. **`SOURCE-001` IS FINISHED.**
- **THE ARM IS δ.** Reopening it requires a *quoted price* for a delisted-inclusive series.
- **D1 IS RULED: the whole span, with a per-year, per-fiscal-calendar weight.**
- **§4.8 IS NOT THE COINCIDENCE ARGUMENT; §4.7 IS, AND IT COMES WITH A WEAK JOINT.**
- **P0 DID NOT CHOOSE D2/D3/D4. §6 DID, and that is now closed too.**
- **EVERY P0 AND REG-009 NUMBER IS AN UPPER BOUND** — computed from the *disclosed* δ. F4 asserts
  the qualifier travels in the same table.
- **NEW · REG-009's NUMBERING IS 6–12 BY RULING, NOT BY ACCIDENT.** §§0–5 keep their addresses.
- **NEW · §4's COVERAGE SILENCE STAYS RECORDED, NOT REPAIRED**, and §6's D3 applies the coverage
  hold-out *in §6*, not retroactively into §4. REG-002 E1's precedent, honoured twice now.

## 3 · NEW MACHINERY (outside wealth-tensor)

`~/Scripts/roster-brake.py` (pre-commit brake) · `~/Scripts/roster_live.py` (**the one reader** of
the board's claim rows) · `~/Scripts/roster-brake-drill.py` (**15 hermetic cases**, scratch repos +
`ROSTER_DB` override, calling the real brake) · `hooks/pre-commit` wiring, **after** the secret scan,
at both exit paths. **Two bugs found and fixed while building it:** `roster-oncommit.py` filtered on
a column named `expires_at` while the table's is `expires`, so the expiry predicate was **silently
dropped**; and **a session can be its own sibling** — a container joins under `GATE_ROSTER_WHO` and
auto-claims under `DARLISH_SESSION`, one session and two rows, so `me` is now a **set**. Drills:
brake 15/15, estate `hooks-drill.sh` 26/26.

## 4 · THE AT-BAT, RANKED

1. **BUILD THE INSTRUMENT AND COMMIT `RESULT-REG-009`** — §3's item 4, the last one open.
   `scripts/reg009_ladder_inputs.py`, written **after** Part II (it is), running F1–F10 in order,
   then §7.3's Ψ / A / S / Ψ_rect(0.05, 0.35, α̂) / Ψ_band. **F1 lifts the ruler from `wt088` by
   name at run time** and aborts unless it still reproduces 0.0 % and 99.7 % — P0-c's mechanism,
   which caught its own miss on its first run. **Read §7.4's UNSEEN list before you compute
   anything; this session deliberately did not look at any of it.**
2. **§12's manuscript repairs land whatever Ψ returns**, and that is registered so the result cannot
   decide whether the paper gets fixed. Two sentences: §4.4's 99.7 % (name the α, label the
   rectangle as asserted, or replace it with the measured share) and §4.7's "it runs on the sample
   §5 already collected" (carry the 151/55, or cut the clause). §7's survived-tests row on the
   disclosed rectangle's admissibility goes in the same pass.
3. **Fill the coverage series between §3b's two cycles.** Unconditional since D1's ruling.
   ~1 min download + ~16 s scan per zip from the **cloud**; `reg009_p0_lifetime_values.py extract`
   gives values for the same zips in the same pass and `--compare` does the coverage arithmetic.
   **It raises §7.5's joinable column and does NOT move the 151.**
4. **The cheap half of §7.5's tee-up.** Join `reg-006-ladderC-events-corrected.json`'s 151 property
   events to the disclosed lives, bin at D3's 1.00 y, **count how many bands clear 30.** One
   afternoon on committed data, no new harvest — and it decides whether REG-011 needs an expensive
   new universe or not.
5. **Run the §1.3 grep on paper III's OTHER self-critical passages.** `-27` ran it on one and found
   three unanswered bounds; `-28` measured all three and two came back against the paper; `-29`
   found the seventh in §4.7's repair clause. **Still the cheapest lead in the repository.**
6. **AAR action A2** — audit the four other `post-*` hooks in `darwin-mac-ops/hooks`. A1 is done;
   A2 is not, and A1 turned up two silent bugs in the one file it touched.
7. **The gate defect card** — State Machine `1217465036940491`.
8. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
9. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded** to
   keep its population identical to §3a's and §3b's. REG-010 may want it.

## 5 · WHAT WOULD HAVE SAVED `-29` TIME

- **Read the sibling REG docs' section headings FIRST** (`grep -n "^#\{1,3\} " REG-00{6,7,8}*.md`).
  The template is §3 quantities · §4 questions · §5 predictions · §6 not-doing · §7 repairs ·
  §8 falsifiers · §9 stopping. Thirty seconds, and it is what exposed the numbering collision.
- **Measure the join before designing the statistic.** The `-28` handoff ranked the §4.7 within-band
  design first; twenty minutes of counting showed the class it selects carries 55 events. **The
  feasibility probe is the design step, not a preliminary to it.**
- **Print counts and NOTHING else in a feasibility probe.** `-29`'s probes deliberately emitted no
  life value, no percentile, no correlation — looking at them spends them (REG-008 §2.6). Write that
  refusal into the probe's docstring so the next reader knows the omission was a decision.
