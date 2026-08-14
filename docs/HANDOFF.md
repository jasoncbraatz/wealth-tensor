---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-14
session: wealthTensor-31
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. **`docs/preregistration/RESULT-REG-009-band-count.md`** — `-31`'s run. §0 first (what §7.5
   registered before the count existed), then §4 (the verdict) and §3 (what the count could not
   reach, which is where the next at-bat comes from).
4. `docs/preregistration/RESULT-REG-009.md` — `-30`'s run. §0 states the reading §11 required; §4
   is a registered control that FAILED and is reported rather than repaired.
5. `docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.**
   Two parts; §§0–5 are Part I, §§6–12 Part II. **The numbering is 6–12 and not 2–8 by ruling.**
   §7.5 is the section `-31` executed, and it now carries two recorded errata (below).

> **`-31` in one line: §7.5's tee-up is RUN, and the answer is ONE band.** 110 of the 151 property
> events can be binned at all; under the primary rule they occupy **16 bands and exactly one clears
> 30** — [5, 6) with 36 events from 20 firms. §7.5's rule was *fewer than two → the expensive half
> arrives*, so **REG-011 needs a new universe — unless the coverage fill says otherwise, and a
> proportional fill puts a second band at 30.2 against a floor of 30.** That one number is the whole
> of the next at-bat.

## 0 · TRANSPORT — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -31 without exception**. Roster join/claim as
`big-wealthTensor-32` — **`roster claim` takes `--resource`, not `--repo`**.
`export LESSONS_CONTRIBUTOR=opus` and **`export GATE_ROSTER_WHO=<you>` at the TOP**, not at the gate.

**THE ROSTER BRAKE IS LIVE and it is a heads-up after the fact**, not a block; the block is
pre-commit and only refuses the `git add -A` shape. Exit is routine: stage by path, then
`ROSTER_BRAKE_ACK=<n> git commit -F <file>` where *n* EQUALS the staged count (5, 2 and 3 here).

> **NEW · `GATE_ROSTER_WHO` DOES NOT REACH THE COMMIT HOOK.** All three of `-31`'s commits printed
> `[roster] wealth-tensor claimed for cloud-EF+kxZZ7` while the session had joined and claimed as
> `big-wealthTensor-31` **and** exported `GATE_ROSTER_WHO`. Both rows are the same session — the
> hook resolves identity from the `dx` shell's own fingerprint, not from the environment. This is
> live evidence for A1's residual (State Machine `1217468064910605`): **`roster join` should write
> an alias file so a session's identity set survives a fresh `dx` shell.** Until it does, expect a
> second `cloud-*` row on the board per session and do not chase it as a sibling.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy.
**753 tests, ~55 s on darwin** (was 732; `-31` added 14 and parametrised 7 into 12).

**NEVER inline a multi-line string in a `dx '...'` argument — a heredoc is not an escape.** Write
locally → `dx --put` → run it / `git commit -F`, and `shasum` every file across. `-31` moved seven
files and one bash script that way, all byte-for-byte. **macOS `base64` rejects a bare file
argument:** `cat f.b64 | base64 -d > out`. **Patch scripts beat `sed`; `patchkit` validates every
anchor before writing anything**, and it reads a shell `# ` comment as a markdown heading — declare
`expect_structure={"#": +N}`, PER FILE inside one call. **Anchor on a span with NO internal
newline**: `-31`'s first draft of the §4.7 patch spanned the hard wrap and was rewritten as two
single-line anchors before it ran.

**Nested same-quote f-strings need Python 3.12+.** Darwin's venv is 3.14.2 now, so the `-30` failure
would not reproduce — but the cloud container and darwin are still two interpreters and only one of
them runs the suite. Precompute with `%`-formatting and the question never arises.

**Bulk SEC work: CLOUD, NOT DARWIN.** Settled five times. `-31`'s exploration ran in the cloud on
`dx --get` copies with `sha256` verified both ways, and only the finished instrument went to darwin.

## THE SIXTEEN THINGS THAT HAVE EACH COST A SESSION A RUN

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
15. **AND OF A REGISTERED CONTROL THAT FAILS — ASK WHETHER THE OPERATOR IS THE ONE THE PREDICTION
    NAMED.** `-30`'s P3 failed on Ψ_band; the bin edges were checked against the instrument that
    PRICED the band and found identical, so the failure is real, and the heaping mechanism is
    labelled post-hoc. **That does not rescue the control.**
16. **NEW · AND OF THE DENOMINATOR. A PER-UNIT AVERAGE IS A CLAIM ABOUT THE *RULE* THAT PRODUCED
    ITS DENOMINATOR, not only about the tag list that produced its numerator.** §7.5 wrote "151
    events average 21 per band" and paper III published it. The 151 was audited to death. The 7 was
    the qualifying-band count under **`R_MIN`** — the interval rule §6 refuses to promote *because
    it scores best* — and under the primary rule it is 9, so the average is 16.8. The denominator
    had drifted to the friendlier arm with nobody choosing it. **For any "X per Y" in a document,
    find the run that produced Y and name which arm it came from.** One grep.

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace.
**A SOURCE-TEXT GUARD FIRES ON ITS OWN WITNESS.** Write the pattern with single-char classes
(`int\(v [/][/] w\)`) so the literal cannot match itself, and **compose the witness world from
fragments** (`"int(v " + "// w)"`). `-31`'s G3a is the second instance and it was written correct
the first time because `-30` wrote the rule down. **The gh_sha dance is NOT a defect.** `--stamp`,
then a commit whose whole content is the stamp; `--check` calls that `ADVISORY: docs-only drift`
and **exits 0**. Read the exit code.

## 1 · WHAT HAPPENED

**`12e3fd1` — the band count.** `scripts/reg009_band_count.py` (+ 14 pinning tests,
`RESULT-REG-009-band-count.md`, its run log, `data/reg-009-band-count.json`).
**14 severe checks, 0 definitional, 0 vacuous.**

| | value |
|---|---|
| tier-0 property events (REG-006-repaired crawl) | **151** across **98** firms |
| … that can be binned at all | **110** across **72** firms — 41 have no life in either cycle |
| **bands clearing 30 EVENTS, `R_MID`, all three cycle choices** | **1** — [5, 6): 36 events, 20 firms |
| occupied bands | 16 — ten of them hold five events or fewer |
| bands clearing 30 **firms** (§3b's own unit is firm-years) | **0** |
| bands clearing 30 in pilot **and** replication separately | **0** |
| by interval rule | `R_MID` **1** · `R_MIN` **2** · `R_WEIGHT` **0** |
| coverage-fill ceiling | adversarial **3** · proportional **2**, second band at **30.2** |

**The verdict, at the strength the count supports.** §7.5's rule was *fewer than two → the expensive
half arrives*, and one band clears, so **§4.7's within-band design is not supported by the sample
§4.7 says it runs on**. But the honest form is *"the expensive half arrives unless the cheap fill
says otherwise, and the cheap fill has not been run"* — because 41 events could not be binned and a
proportional fill lands the second band on 30.2 against a floor of 30.

**And the interval rule moves the answer ACROSS the threshold.** `R_MIN` gives two. `R_MIN` is the
reading under which the design lives and it is the rule §6 refuses to promote *because it scores
best*; adopting it here would be that refusal spent on the same afternoon the threshold was tested.
The primary rule stands and the count is 1. `test_the_interval_rule_moves_the_answer_across_the_
threshold` goes red if a future session quietly changes `PRIMARY`.

**TWO ERRATA IN §7.5, recorded and NOT repaired retroactively** — both found by reproducing the
table before extending it, which is the only reason they were found at all:

- the `all` row prints **307** distinct firms in *both* columns; the repaired crawl carries **338**.
  307 is the pre-repair count, carried across.
- **"7 qualifying bands at a 1.00-year width" is P0-c's count under `R_MIN`.** The primary rule
  gives **9**. This is finding 16 above.

**`7ae8841` — §4.7 carries the measured count**, registered in the result doc §5 before the edit,
performed by `scripts/wt097_edits_47.py` through patchkit. G-COACH-3 across the edit: **3 → 3**.

**`8d5c908` — G-COACH-3 now means the estate.** `-30` shipped it against paper III alone while the
charter says "the manuscript"; papers I and II were covered by a rule with no instrument. Both now
carry a committed baseline and run through parametrised tests, and a census test globs the papers
tree so a fourth paper cannot arrive uncounted. paper-I 0 outside §Limitations (1 inside, exempt);
paper-II 0 and 0 — a zero that is a *measurement*, because the vacuity test proves the counter fires.

## 2 · RULINGS — DO NOT REOPEN

- Prior rulings stand: no third disclosure instrument; the two dead (f) keywords stay in `INTERNAL`;
  phrase set frozen at 38; retail PP&E × intangible cells out of §5.4; §4.4 settled; References
  block; §4.5's 400-vs-4,000 not a defect. **`SOURCE-001` IS FINISHED.**
- **THE ARM IS δ.** Reopening it requires a *quoted price* for a delisted-inclusive series.
- **D1 IS RULED: the whole span, with a per-year, per-fiscal-calendar weight.**
- **§4.8 IS NOT THE COINCIDENCE ARGUMENT; §4.7 IS, AND IT COMES WITH A WEAK JOINT.**
- **EVERY P0 AND REG-009 NUMBER IS AN UPPER BOUND** — the *disclosed* δ. F4 asserts it travels.
  **Every band in `-31`'s table is a band of the DISCLOSED life**, and the doc says so under the table.
- **REG-009's NUMBERING IS 6–12 BY RULING.** §§0–5 keep their addresses. **REG-009 IS CLOSED**;
  `-31` executed a tee-up §7.5 had already registered and moved no registered number.
- **§4's COVERAGE SILENCE STAYS RECORDED, NOT REPAIRED.** Honoured three times now.
- **§7.5's TWO ERRATA ARE RECORDED, NOT REPAIRED.** `test_the_two_errata_are_still_errata` goes red
  if anyone repairs them, so the repair gets noticed rather than absorbed.
- **P3's FAILURE IS NOT REOPENED BY RE-BANDING.** The half-integer-edged banding is REG-010's, in
  its own document, reported BESIDE the failure and never instead of it.
- **DO NOT PROMOTE `R_MIN` TO PRIMARY.** §6 refuses it because it scores best, it carries the
  smallest admissible sample (533/683) on the fewest distinct points (199) — and it is now also the
  rule under which §4.7's design would survive. That makes the temptation concrete rather than
  theoretical, which is exactly why the ruling stays.

## 3 · THE AT-BAT, RANKED

1. **FILL THE COVERAGE SERIES BETWEEN §3b's TWO CYCLES — and it is no longer tidy-up, it is the
   measurement that decides REG-011.** ~1 min download + ~16 s scan per zip, **CLOUD**. It raises
   the joinable column (110 of 151) and **does NOT move the 151**. `-31`'s proportional bracket puts
   the second band at **30.2 against a floor of 30**, so a representative fill flips §7.5's verdict
   and an unrepresentative one does not — and nobody can say which without running it. The
   deliverable is `data/reg-009-band-count.json` recomputed on the filled join, reported beside
   `-31`'s row, never instead of it. **Definition of done: a second band count on the filled
   population, and a one-line amendment to `RESULT-REG-009-band-count` §4 saying which way it went.**
2. **REG-010: the half-integer-edged banding, REGISTERED BEFORE IT IS RUN.** §4's tee-up in
   `RESULT-REG-009`. Bins centred on the heap rather than starting on it, so the collapse is a
   rounding and not a translation. One function and one run on committed data.
3. **The §1.3 grep on paper III's other self-critical passages.** Five sessions, four finds — `-30`
   and `-31` both skipped it. Still the cheapest lead in the repository.
4. **"disclosed rectangle" at paper III lines 964, 996, 1123 and 1573**, denoting the [10,40]×[3,20]
   product. 86.1 % of the disclosure falls outside it, so the adjective is wrong at all four; `-30`
   renamed it to *asserted* only at the two sites §12 registered. **`-31` did not do it because the
   charter requires a manuscript repair to be registered first and this session's registration was
   about the band count. So here is the registration, pre-written — paste it into the repair's own
   result doc or a two-paragraph `RESULT-TERM-001.md`, then perform it:**
   > *Registered before the edit: the noun phrase "disclosed rectangle" at paper III lines 964, 996,
   > 1123 and 1573 denotes the [10,40]×[3,20] product asserted in `wt088_disclosed_ladder.py`, not
   > any measured feature of the disclosure. RESULT-REG-009 §3 measures S = 0.1391, so 86.1 % of the
   > disclosure lies outside it and the adjective states the opposite of the measurement. All four
   > sites are replaced by "asserted rectangle", the term §12 already registered at two other sites.
   > No claim is weakened, no hedge is added, and G-COACH-3 is evaluated across the edit.*
   Re-run `test_ledger_provenance` and `test_restatement_reach` after.
5. **AAR A2** — the four other `post-*` hooks in `darwin-mac-ops/hooks`; plus A1's residual (State
   Machine `1217468064910605`), for which `-31` has live evidence (§0 above).
6. **The gate defect card** — State Machine `1217465036940491`.
7. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
8. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**
   REG-010 may want it.

## 4 · WHAT WOULD HAVE SAVED `-31` TIME

- **Reproduce the published table before extending it, always — it is where the errata live.** Both
  of `-31`'s findings came out of the reproduction pass, not out of the new measurement. A fresh
  count alone would have printed correct numbers, agreed with itself, and left two wrong published
  ones standing, because a new correct number does not announce that the old one was wrong.
- **Grep the instrument that produced the number you are about to divide by.** The "7 qualifying
  bands" took ninety seconds to trace to `data/reg-009-p0-result.json` and turned a sentence in a
  published paper from wrong-and-unnoticed into wrong-and-recorded.
- **`load_events(root, fn)` takes the REPO ROOT, not the data dir.** Two of `-31`'s helpers take
  root and one takes a path; if you extend the instrument, read the signature.
- **The exploration belongs in the cloud on `dx --get` copies.** Four data files, `sha256` verified
  both directions, and every probe iterated in a second instead of a round trip. Only the finished
  instrument went to darwin.

## 5 · DEFINITION OF DONE (carry this forward)

§7.5's tee-up is **done**: the count is printed, committed, pinned by tests, and the published
sentence it prices has been repaired to carry it. The next unit of done is item 1 above, and it has
one: *the band count recomputed on the coverage-filled join, reported beside `-31`'s row rather
than instead of it, with a one-line amendment to `RESULT-REG-009-band-count` §4 stating whether the
second band cleared.* That amendment is what commissions REG-011 or retires it.
