---
project: wealth-tensor
gh_sha: 09169b22fe7d4a07cd71c12cba5ca11d4f15de57
updated: 2026-08-14
session: wealthTensor-42
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

*`gh_sha` points at the commit this file describes; the only thing added after it is this file, so
`--check` prints `ADVISORY: docs-only drift` and exits 0. **Read the exit code.***

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff, any
   result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the other
   thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. **`docs/preregistration/CONSTRAINT-INVENTORY-001.md` — NEW, and it is the map for this thread.**
   **Fifty reporting constraints across sixteen registration and construction documents**, each with
   its governed quantity, **the RESOLUTION it is written at**, its scope, **whether it is LIVE**, the
   compliance verdict, and whether a machine exists. §3 names the five a machine could recognise and
   does not have one — **that is `-43`'s at-bat.** §2 is what the sweep found. Read §0 first: it says
   how the list was built and why a keyword grep alone produces a plausible, shorter, wrong one.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md` §§3.2, 3.3, 7.** §3.2 is
   the four-regime ladder, **§3.3 is the registered bias asymmetry AND the second reporting
   constraint**, §7 the rest. **BOTH §3.3 and §7 now have machines** —
   `tests/test_reg003_sec33_asymmetry.py` and `tests/test_reg003_sec7_rounding.py`. They are the only
   two guards in the estate written FOR a constraint rather than inheriting it from a prediction.
5. **`docs/scouting/SCOUT-001-paper-III-opposing-team.md`** — **WORKED, NOT PENDING.** `-41` landed
   five of six tickets and both free steelmen; only T2 remains and T2 is carded and barred on this
   data. **It does not run again on this paper.** Read it for measurements, not for a to-do list, and
   know that two of its own statements are wrong (§3's censoring prose, corrected in place; T1's row
   grading §5.4 compliant, which grades a paragraph against a sentence rule).
6. `REG-012` §§1–2 and §6 · `RESULT-REG-012` **§0 first**, then §3, §4 · **`RESULT-TERM-001`** the
   five-site ruling, §2 before touching any *rectangle* · `REG-010` **§1 is the population ruling** ·
   `CONSTRUCTION-REG-010` **§C2 owns 55.71 % and its population in one sentence**, C3 and C5 are the
   two a later session walks past.
7. `RESULT-REG-010` §3 → §4 · **`RESULT-TERM-002`** §2 before §8, §8.1, §A.2.4 · `RESULT-PIN-001` ·
   `RESULT-SCOPE-001` · `RESULT-REG-009-band-count-filled` §4 → §3 → §6 ·
   `CONSTRUCTION-REG-009` (**R5 is load-bearing and unspent**) · `RESULT-REG-009` (**§3's S = 0.1391
   is load-bearing in a test**) · `REG-009` (**READ THE HEADER NOTE FIRST**; numbering 6–12 by ruling).

> **`-42` in one line: THE CONSTRAINT CLASS HAS A SECOND MEMBER, IT IS CONDITIONAL, AND THE ONE SITE
> THAT ALREADY COMPLIED COMPLIED BY ACCIDENT.** `REG-003` §3.3 says a high α̂ must be reported with the
> two registered upward biases attached **in the same paragraph, not in a limitations section** — but
> only if the run lands in R1 or R2. It landed in **R1 in every cut**. The manuscript reported the
> finding at five places and attached the direction at exactly one: the abstract, because `-41`'s §7
> repair happened to carry the phrase. Nobody was aiming at §3.3. **`SCOUT-001`'s own diagnosis of §7
> — *a qualification that exists in the right paragraph and does not travel* — was reproduced by the
> repair for the other constraint, in the session that named it.**

---

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-42`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.

**`--replaces` verified again in `-42`**: `roster join --replaces cloud-<fp>` printed `absorbed 1
row(s)` and the board showed one name. `roster leave` ONCE at wrap.

> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
>
> `-40` closed card `1217496462088036` after eight sessions: dx spawns a **fresh remote shell per
> call and carries no environment**. **`-42` used the inline form on `roster join`, `roster claim`,
> the commit, `gate-selfcheck.sh` and `lessons.py` — all five first time**, and the commit hook
> logged `big-wealthTensor-42`.
>
> ```
> /tmp/dx 'cd ~/repos/wealth-tensor && GATE_ROSTER_WHO=big-wealthTensor-NN ROSTER_BRAKE_ACK=<n> git commit -F <file>'
> ```
>
> **Three consumers, all needing it:** the commit hook · `gate-selfcheck.sh` (without it the gate
> says *"I cannot tell whether that is you"* about a dirty sibling; with it, a definite answer) ·
> **`lessons.py`, which AUTO-COMMITS AND PUSHES** — prefix the `lessons.py` call itself or its commit
> files a `cloud-<fp>` claim on `claude-blackbook` that survives your `roster leave`.

**THE MINUTE-TWO STANZA IS TWO LINES.** `dx --get`/`--put` are **binary-clean and self-verifying**.
**No base64. No manual `shasum`.**

```
/tmp/dx 'cd ~/repos/wealth-tensor && tar czf /tmp/wt-lite.tgz docs scripts tests src && tar czf /tmp/wt-data.tgz data'
/tmp/dx --get /tmp/wt-lite.tgz /tmp/wt-lite.tgz && /tmp/dx --get /tmp/wt-data.tgz /tmp/wt-data.tgz
```

`-42` measured 2,117,197 + 4,682,859 bytes, both `verified against darwin` **in words**, seconds.
**Trust the sentence, not a number. Exit 5 = bytes crossed but did not match, nothing written,
replay-safe, re-run.** **PULL BOTH TARBALLS BEFORE RUNNING THE SUITE** — `-42` ran it with only
`wt-lite` and got *12 failed / 59 errors*, which is what an absent `data/` looks like and is not a
defect. `--put` does **not** create parent directories. **Never inline a multi-line string in
`dx '...'`** — write locally, `--put`, run it. **`ROSTER_BRAKE_ACK=<n>` MUST EQUAL THE STAGED COUNT**
(`-42`'s was 6).

**SUITE COUNTS — COLLECTED + SKIPS, NOT TWO PASS COUNTS.**

| | at `09169b2` (verified in `-42`, both machines, same day) |
|---|---|
| collected | **872** |
| cloud (`PYTHONPATH=<root>/src`) | **864 passed / 8 skipped**, ~166 s, **every skip `not a git work tree`** |
| darwin (`.venv/bin/python -m pytest`) | **872 passed**, ~61 s |

---

## 0 · THE TELL, NOW IN TWENTY-NINE SHAPES

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL GONE QUIET (`-32`). `-33`: instruments that agree with themselves.
`-34`: defects nobody introduced. `-35`: defects you are about to introduce. `-36`: pre-commit the
FAVOURABLE outcome's meaning. `-37`: a mutation that does not mutate reports your guard as weak.
`-38`: a statistic can be a tautology in measurement's clothing; grep the estate for the ANSWER, not
the symptom. `-39`: a handoff silently outranks a doctrine leaf; **assert the EXACT exit code**.
`-40`: a STALE NEGATIVE closes a question harder than an open one; a registration carries REPORTING
CONSTRAINTS and they are greppable; check a robustness cut against the boundary the CLAIM needs.
`-41`: a hand-audit that found N sites found them through ONE DOOR; a compliance grade at paragraph
resolution against a sentence rule is a FALSE GREEN; a published number nobody recomputed in exact
arithmetic can be one ULP wrong; an inherited claim is a claim, and the cheapest check is its own
table. **`-42` adds four:**

- **A CONSTRAINT CAN BE CONDITIONAL, AND A CONDITIONAL CONSTRAINT'S GUARD MUST ASSERT ITS
  ANTECEDENT, NOT ONLY ITS TEXT.** `REG-003` §3.3 fires only in R1/R2, so *reading the registration
  cannot tell you whether the rule is live* — you have to go and read which branch the `RESULT-*`
  recorded. That is exactly why it sat unchecked while §7, four sections later **in the same file**,
  got a machine: §7 reads as a rule and §3.3 reads as a contingency. Two consequences. Any inventory
  of what a corpus forbids needs a **LIVE?** column filled from the result, not the registration
  (three of fifty in this sweep were conditional and did not fire, and recording that is the point —
  a constraint graded *not live* with its antecedent named is a question that stays closed). And the
  guard asserts the antecedent so a flipped branch reports a **LOST TRIGGER** — *this rule no longer
  applies, retire me* — rather than a violation. Different failures, different messages.
  Banked: `2026-08-14-constraint-can-conditional-conditional-constraint-s`.
- **A WHITESPACE-IDENTITY GUARD CERTIFIES THAT NO CHARACTER MOVED, NOT THAT NO MEANING MOVED — AND
  IN A LINE-ORIENTED FORMAT THE LINE BREAK IS CONTENT.** `wt107`'s re-wrap guard is an identity on
  `" ".join(text.split())`, which is a genuinely strong design for prose and **blind by construction
  to the only thing it can break**. Its target list named a string inside §9's markdown numbered
  list, a list is one block, and re-filling it moved `2.` `3.` `4.` off their line starts —
  rendering four limitations as one. Flattening is *precisely* the operation that erases that
  difference. The repair is the **paired** guard: identity for the characters, a structural
  assertion for the breaks. And put the durable check in the SUITE, not in the script that did it —
  the script is the record of an edit that happened (`wt092` precedent) and the next re-wrap will be
  a different tool. Banked: `2026-08-14-whitespace-identity-guard-certifies-character-moved`.
- **WHEN A CORPUS HAS A HOUSE STYLE, THE SECOND DOOR INTO IT IS THE SECTION HEADING, NOT A BIGGER
  KEYWORD LIST.** The keyword grep returned 102 lines; **twenty-seven constraint-shaped headings**
  (*Stopping rule* · *What may be claimed, and what may not* · *What a pass does NOT license* ·
  *What this may not move* · *What this cannot do* · the `R*`/`C*` sections) carry **at least six
  rules with none of those tokens in them** — *"is a condition of the result being reportable at
  all"*, *"no result from this pipeline is reportable"*, *"it does not license any claim that"*,
  *"the design is refused and P0's table is the result"*, *"refused, not merely unperformed"*,
  *"reported BESIDE, never instead of"*. `-41`'s one-door tell, applied to the inventory rather than
  to the sites. Banked: `2026-08-14-corpus-has-house-style-second-door`.
- **(BUG SPRAY) EVIDENCE FOR AN INVARIANT THAT LIVES IN A GITIGNORED FILE IS NOT IN THE SSOT — AND
  THE IGNORE RULE CAN BE MACHINE-GLOBAL.** Every handoff since G-COACH-3 was mechanised cites
  *"3 → 3 (+0) against `paper-III.md.bak-pre-<script>`"*. `git check-ignore -v` says those `.bak`
  files match `*.bak*` in **`~/.gitignore_global`** — one laptop, no clone, gone with the machine,
  and nothing in the repo mentions the rule. **The control is fine**: `DEFENSIVE-BASELINE.json` plus
  `tests/test_defensive_count.py` binds the same invariant from the SSOT and that is the durable
  half. **The quoted evidence was the un-reproducible half.** Run `git check-ignore -v` on anything
  you are about to cite as proof, and when a control has a durable form and a convenient one, cite
  the durable one — the handoff sentence is what the next session will try to reproduce.
  Banked: `2026-08-14-evidence-invariant-lives-gitignored-file-ssot`.

**Everything `-33` through `-41` banked is unchanged and still sharp.** A guard must scan assertions,
not quotations. `severity.check`'s witness must return FALSY. Check `git ls-files <name>` before a
whole-file write into a shared directory (`-42` checked; all four new names were free). `patchkit`
anchors have **no internal newline** — `-42` lost one anchor to a hard wrap inside
`**α̂ = 0.408 per year**, 95% interval` and fixed it by shortening to the newline-free tail, which is
the standing repair and costs thirty seconds.

---

## 1 · WHAT HAPPENED

**`09169b2` — the constraint sweep. Fifty constraints inventoried; one live violation, at four sites.**

- **`docs/preregistration/CONSTRAINT-INVENTORY-001.md`** — the list that did not exist. Fifty
  constraints, both doors, with resolution / scope / live? / verdict / machine per row, plus §2's
  findings and §3's ranked list of the ones a machine could recognise and does not have one.
  **Nine of the fifty already had a machine, all of them incidental** — the test was written for a
  prediction or an artifact and happens to bind the constraint too. **`REG-003` §7 and §3.3 are the
  only two with a guard written FOR the constraint**, and `-41` wrote one of them.
- **T-`REG-003`-§3.3 · the live one.** R1 in every cut (pooled 0.4077; 0.3940–0.4986 across both
  universes and all three registered sensitivities), so the asymmetry fires. Repaired at **§4.4**,
  **§5.4's bolded lead** (the one line a skimming referee reads — and `-41` said so about the same
  sentence), **§7's survivals ledger row**, and **§9 limitation 4** (the section §3.3 names
  explicitly as where the qualification may *not* live). Every one a **REPLACE**: the registered
  direction goes inside the sentence that already carries the number. **+154 characters, 0
  sentences, 0 new numeric tokens**, so neither `G-COACH-3` nor `test_restatement_reach.py`'s
  declared counts could move. `scripts/wt108_edits_reg003_sec33.py`.
  **Its gate** re-derives §3.2's annualisation `α̂_yr = 1 − (1 − α̂_q)⁴` from §5.4's own published
  per-quarter cell in `fractions.Fraction` and refuses unless it reproduces the published `0.408`
  **and clears §3.2's R1 floor of 0.33** — the constraint's antecedent, recomputed rather than
  inherited. `-41`'s exact-arithmetic practice pointed at a *conditional* instead of at a cell.
- **THE SECOND DEFECT, found by the new guard's splitter rather than by reading.** §9's four
  limitations had become **one list item**: `wt107` re-wrapped the block containing
  `"α is measured, but"`, a markdown numbered list is one block, and `2.` `3.` `4.` ended up
  mid-line. Three sites, nothing else in the manuscript, zero in the pre-`wt102` backup.
  `scripts/wt109_repair_section9_list.py` puts them back under the **paired** guard — the same
  flattened identity *plus* every marker line-leading and exactly items 1–4. **`wt107` is left
  untouched**: the record of an edit that happened.

**Two new guards, and each is a wire between a rule and the thing that licenses it:**

| guard | what goes red |
|---|---|
| `tests/test_reg003_sec33_asymmetry.py` | a **paragraph** (or table row, or list item) reporting α̂ *as the result* — its interval, or against the calibration it overturns — with no word about the two registered upward biases. **RED on the four real pre-edit units, GREEN on six real legal ones** including §4.4's column header and §4.10's rate table, two of which `REG-003` §7's own guard had to be taught to leave alone. **Warrant in two halves:** §3.3's sentence still in `REG-003`, *and* `RESULT-REG-003` still recording R1/R2. |
| `tests/test_manuscript_lists_are_well_formed.py` | any list-item marker sitting mid-line, whatever tool put it there. Red and green fixtures **differ only in line breaks**, so the file proves it makes the assertion flattening cannot. |

| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** against `paper-III.md.bak-pre-wt108-sec33`, taken before a byte moved |
| **G-COACH-1** | held — every weakness named shipped a REPLACE |
| **G-COACH-5** | held — the strength named is **`REG-003` §3.2 itself**: an exhaustive four-regime ladder stated on the signed, unbounded quantity, where *three of the four outcomes require §4.4 to be edited and no cell is the one anyone was hoping for*. That design is what made §3.3's antecedent checkable weeks later by reading one column. |
| suite | **872 collected** · darwin **872 passed** (~61 s) · cloud **864 passed / 8 skipped** (~166 s) |
| new tests | 2 files, 23 tests |
| lessons | **four** banked global · **five** used and corroborated `record-outcome wealthTensor-42 pass` |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-41`'s rulings stand **verbatim**: no third disclosure instrument; phrase
  set frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS THE *DISCLOSED* δ**; **REG-009 IS
  CLOSED, numbering 6–12**; **§4's COVERAGE SILENCE AND §7.5's TWO ERRATA STAY RECORDED, NOT
  REPAIRED**; **DO NOT SPEND THE TIE-BREAK**; **DO NOT PROMOTE `R_MIN`**; **`data/reg-009-band-count.json`
  IS `-31`'s**; **`test_the_cycle_choice_now_decides_the_answer` IS A RESULT**; **SCOPE-001, PIN-001,
  TERM-001, TERM-002 ARE CLOSED**; **§11 PINS PER FILE**; **P3 FAILED AND REG-010 DID NOT RE-SCORE
  IT**; **REG-010's POPULATION IS Ψ's 683 PAIRS**; **NEITHER BANDING IS PROMOTED**; **THE BAND COUNT
  MAY NOT BE RE-EDGED AND ITS FLOOR RE-READ (R5)**; **REG-012 IS CLOSED ON BRANCH F**; **THE TWO
  SENSITIVITIES ARE SEPARATE**; **55.71 % IS Ψ's AND 63.16 % IS THE BAND COUNT'S** —
  `test_reg012_band_edge_phase.py` goes red if they converge; **`selected_lives` IS THE ONE SELECTION
  PATH**; **§4.4's TIER-0 CALIBRATION CELL IS `0.3000`** and `wt092_edits_44.py` keeps the original
  literal **on purpose**; **T4's IDENTIFIED-SET WIDTH IS `31.7%`, NOT `0.32`**; **`SCOUT-001` IS
  WORKED, NOT PENDING, AND MAY NOT FLOW INTO THE MANUSCRIPT RAW**; **T2 MAY NOT BE RUN ON THIS DATA**
  (carded `1217501628088122`); **THE SCOUTING REPORT'S TIMING IS CLAUDE'S CALL**; **`dx --get`/`--put`
  DO NOT NEED BASE64**.
- **NEW · `CONSTRAINT-INVENTORY-001` IS AN INVENTORY, NOT A LICENCE TO REOPEN.** Where a row says
  *closed by ruling*, the ruling governs and the row is a pointer to it. Its verdicts were reached by
  reading the sections, not the greps, and every quotation in it is short enough to have lost context.
- **NEW · §9's LIMITATIONS ARE FOUR LIST ITEMS AND STAY FOUR.** `test_manuscript_lists_are_well_formed.py`
  goes red if any re-wrap collapses them again. **Re-wrap the ITEMS, never the block.**
- **NEW · `wt107` IS NOT EDITED.** It is the record of an edit that happened. The defect it caused is
  repaired in the manuscript by `wt109` and guarded in the suite, which is where a guard belongs —
  it catches the next tool too.
- **NEW · THE `.bak` PRE-EDIT COPIES ARE GITIGNORED AND ALWAYS WERE** (`~/.gitignore_global:31`).
  Keep taking them — they are the reversibility path and `--against` is the cleanest read of a single
  pass — but **cite `tests/test_defensive_count.py` and `DEFENSIVE-BASELINE.json` as the evidence**,
  because those are in the SSOT and the `.bak` is not.

---

## 3 · THE AT-BAT for `-43` — **finish the mechanisation. `CONSTRAINT-INVENTORY-001` §3 is the list.**

`-42` inventoried fifty constraints and found one live violation. **§3 of the inventory names five
that a machine could recognise on sight and that have no machine.** None is a defect today; each is
an unguarded invariant, which this estate's own doctrine says is the state that rots quietly. Work
them in this order, in the shape `test_reg003_sec33_asymmetry.py` established — *predication, not
vocabulary; RED on real violating text and GREEN on real legal text including anything a cruder cut
flags; a declared warrant, plus the antecedent if the rule is conditional*:

1. **C19 · `REG-004` §6 — α_eff may not be called "the" recognition rate.** The exact sibling of the
   one `-41` mechanised, **one symbol over**, and the manuscript is clean at all six α_eff sites
   today. This is `-41`'s two-doors tell aimed at the *guard* rather than at the audit: a guard
   written for α̂ says nothing about α_eff, and the estate has three recognition rates. Cheapest and
   highest-value. `test_reg003_sec7_rounding.py` is the file to read first, not to edit.
2. **C21 · unregistered robustness must be labelled as robustness and may not change a verdict**
   (`REG-004` §6 and `REG-005` §7, identical wording). Recognisable: a unit reporting a cut that
   appears in no `REG-*` file and carrying no *unregistered* label. `RESULT-REG-003` §1 already
   tabulates the registered cuts, so the allow-list is a read, not a judgement.
3. **C48 · `REG-012` §6 — "no sentence of the manuscript's §4.7 is changed by any outcome of it."**
   A frozen-section assertion: hash §4.7 and pin it the way `test_pin001_code_state.py` pins code.
   Note the warrant subtlety — the freeze is relative to `REG-012`, so the pin must record *which*
   version it froze, or a legitimate future edit reports as a `REG-012` violation.
4. **C24 · `REG-005` §7 — the fitted lag distribution may not be claimed to transfer beyond the
   sample's classes.** Recognisable through the scope noun phrase §6.1 now owns after `-41`'s T5.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The remaining board, unchanged in order:

1. **`SCOUT-001` §1.1's presentation observation — Jason's call, not a ticket.** §7's forty-row
   ledger dilutes its two load-bearing rows, including **S3, the §4.5 row that refused in 400 of 400
   draws**, which `SCOUT-001` §3 calls the single strongest fact about this paper's process, sitting
   among thirty rows showing a closed form matching the simulation that shares its code. The fix is a
   column separating algebra-versus-code rows from rows that risked something. **`-42` found the
   registration underneath it**: `REG-009` §4 requires a refusal to be *"stated in the same sentence
   as the number that caused it"* — which it is (inventory C36). The registration says nothing about
   the row sharing a table with thirty that risked nothing. **So this is genuinely a judgement about
   a reader and not a compliance defect**, which is the cleanest reason yet to leave it to Jason.
2. **Infra siblings, carded, Claude-hands:** `@concierge_ingest` / `@concierge_router` carry the same
   Caddy ordering defect `@darlish` had (`1217488447555628`) · the live capability path is committed
   in cleartext to `n8n-stack` and the repo copy has drifted (`1217488117177482`).
3. **AAR A2's residual** — the other four `post-*` hooks · card-lint (`1217483699706758`) · the gate
   card (`1217465036940491`).
4. **Still open from the dossier era, re-served by nobody:** `REVIEW-004` **C6** (name one asset class
   where §2's domain restriction holds *and* a recognition event is observable in filings — ASC 410
   asset retirement obligations is the referee's own offered rescue) and **C10** (IAS 36's
   impairment-reversal asymmetry is a free cross-regime falsification test).
5. The phrase set has a passenger: 30.4 % of trigger sentences match only `events or circumstances`;
   7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
6. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
7. **Not mine, not touched:** handoff-lint warns `HANDOFF-acmeLedger-07.md:22`, `-09.md:36,42`, and
   `-12.md` / `-13.md` carry items with **zero `verify:` liveness lines**. Siblings were live on all
   four; don't clobber.

---

## 4 · WHAT WOULD HAVE SAVED `-42` TIME

- **THE FIRST TEN MINUTES DECIDED THE SESSION FOR THE EIGHTH TIME RUNNING** (`-35` truth, `-36`
  population, `-37` count, `-38` premise-and-instrument, `-39` severity, `-40` the promise the
  document made about itself, `-41` the resolution the promise was written at, **`-42` whether the
  promise was even in force**). The whole finding came from reading `REG-003` §3.2's ladder, noticing
  §3.3's rule was *conditional*, and then going to `RESULT-REG-003` to see which regime the run
  landed in. **Two files, four minutes.** Spend the ten minutes, and spend them on the registration.
- **BUILD THE INVENTORY THROUGH BOTH DOORS BEFORE GRADING ANYTHING.** The keyword grep took ninety
  seconds and would have produced a list missing six rules. The heading grep took another ninety.
- **PULL BOTH TARBALLS.** `-42` ran the cloud suite against a tree with no `data/` and read *12
  failed, 59 errors* for thirty seconds before recognising it. Nothing was wrong.
- **WRITE THE EDIT SCRIPT'S GATE AGAINST THE MANUSCRIPT'S OWN PUBLISHED CELLS, IN EXACT ARITHMETIC.**
  `wt108`'s gate re-derives the annualisation *and* the regime, so it refuses to attach a
  registration's sentence in a world where that registration has released the manuscript.
- **`patchkit` ANCHORS MUST HAVE NO INTERNAL NEWLINE.** One of `-42`'s four anchors spanned a hard
  wrap; shortening to the newline-free tail fixed it immediately. Do not fight the wrap, move the
  anchor.
- **SET `GATE_ROSTER_WHO` INLINE**, on every darwin-side tool that asks who you are. Five for five.
- **`roster leave` ONCE**, at wrap. **CORROBORATE THE LEAVES YOU USED** — `use` when you read one,
  `record-outcome` at wrap.

---

## 5 · DEFINITION OF DONE (carry this forward)

**The manuscript pass is done and the constraint sweep is done.** Fifty constraints are enumerated
with their resolutions and their live status; the one live violation is repaired at all four sites
with a machine behind it; a structural regression `-41` introduced is repaired with a machine behind
it too. **The estate now knows what its registrations forbid**, which is a thing it could not say
yesterday, and the answer was bounded and greppable exactly as `-41` predicted.

**The research ledger on paper III is still empty, and it stays empty.** T2 is the only live
registration idea and it is barred on this data by ruling.

**The next unit of done is `CONSTRAINT-INVENTORY-001` §3, worked to zero** — four constraints a
machine can recognise, each with a red-and-green proof and a declared warrant. That is a finite list
with a finite end, and when it is empty the honest question becomes the one the inventory cannot
answer: **which of these fifty are constraints a machine could never recognise, and what does the
estate do about those?** Answer that in the handoff, not in a new document.
