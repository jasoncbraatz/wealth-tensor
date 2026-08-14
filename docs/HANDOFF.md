---
project: wealth-tensor
gh_sha: 7088f6b6d41aff6f9ec76fedf61f36c37e794c01
updated: 2026-08-14
session: wealthTensor-41
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
2. **`docs/scouting/SCOUT-001-paper-III-opposing-team.md`** — the scheduled scouting report under
   §4. **`-41` WORKED FIVE OF ITS SIX TICKETS (T1, T3, T4, T5, T6) AND BOTH FREE STEELMEN; only T2
   remains, and T2 is carded and barred on this data.** Read it for the measurements and the drills,
   not for a to-do list. **It does not run again on this paper**, it is not the manuscript, and two
   of its own statements are now known to be wrong — §3's censoring prose (corrected in place at
   `7088f6b`) and T1's row grading §5.4 compliant (it grades a paragraph against a sentence rule;
   see §0). Four read-only probes in `docs/scouting/probes/` re-run in seconds and all four still pass.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md` §§3.2, 3.3, 7** —
   §3.2 is the four-regime ladder, §3.3 the registered bias directions, §7 the reporting constraints.
   **A registration carries reporting constraints as well as predictions, and they are greppable.**
   §7 is now *enforced* rather than merely written: `tests/test_reg003_sec7_rounding.py` fails the
   suite if any sentence rounds α̂ again, and it declares its own warrant — if §7's sentence is ever
   deleted or restated the test says the guard has lost its licence instead of quietly enforcing a
   rule the repository no longer holds. **It is the only registration constraint in the estate that
   has a machine behind it. There are others, and nobody has enumerated them** (see §3).
5. **`docs/preregistration/REG-012-band-count-edge-phase.md`** — §§1–2 are two findings about how the
   question was ASKED; §6 is the two-branch ruling. Read both before touching anything edge- or
   band-shaped.
6. `docs/preregistration/RESULT-REG-012-band-edge-phase.md` — **§0 first** (the two defects), then §3, then §4.
7. **`docs/preregistration/RESULT-TERM-001.md`** — the **five-site ruling**. §2 before touching any *rectangle*.
8. `docs/preregistration/REG-010-p3-half-integer-banding.md` — **§1 is the population ruling**, §3 the two-branch ruling.
9. `docs/preregistration/CONSTRUCTION-REG-010-edge-convention.md` — **§C2 owns the 55.71 % and owns its
   population in the same sentence.** C3 and C5 are the two a later session walks past.
10. `RESULT-REG-010-half-integer-banding.md` §3 then §4 · **`RESULT-TERM-002.md`** the two-numeral
    ruling, §2 before §8, §8.1, §A.2.4 · `RESULT-PIN-001.md` · `RESULT-SCOPE-001.md`.
11. `RESULT-REG-009-band-count-filled.md` §4 → §3 → §6 · `CONSTRUCTION-REG-009-coverage-fill.md`
    (**R5 is load-bearing and unspent**) · `RESULT-REG-009.md` (**§3's S = 0.1391 is load-bearing in a
    test**) · `REG-009-p3-lifetime-sourced-delta.md` (**READ THE HEADER NOTE FIRST**; numbering 6–12 by ruling).

> **`-40` in one line: THE SCOUTING REPORT SHIPPED, AND ITS TWO REAL FINDINGS ARE BOTH THE PAPER
> FAILING TO KEEP A PROMISE IT WROTE DOWN ITSELF.** `REG-003` §7 says *"no sentence anywhere may
> round"* α̂ to *"the recognition rate"*; the abstract rounds it, and so do four other sites, while
> §5.4 — the section that produced the number — complies in full. And `REVIEW-004` C12 named the
> elected annual test date in the dossier era, proposed a diagnostic, and the diagnostic was
> never run: run now, charges concentrate on a firm's own calendar quarter at p < 0.0003 in both
> universes. Neither finding needed a new idea. Both needed somebody to grep a document against a
> promise and run a script somebody else had already specified.

---

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-40`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.

**`--replaces` WORKS and is verified again in `-40`** — `roster join --replaces cloud-<fp>` printed
`absorbed 1 row(s)` and the board showed one name, one session row. `roster leave` ONCE at wrap.

> ### ⚠ THE `export GATE_ROSTER_WHO=...` LINE EVERY HANDOFF SINCE `-30` CARRIED IS RETIRED. IT NEVER DID ANYTHING.
>
> **`-40` closed card `1217496462088036` after eight consecutive sessions.** dx spawns a **fresh
> remote shell per call and carries no environment**, so an `export` run in the cloud container
> reaches darwin as the empty string — measured in ninety seconds with
> `dx 'echo [$GATE_ROSTER_WHO]'`, which returns `[]`. The card's own narrowing (*"this is NOT a
> variable lost crossing the dx boundary; the hook is not reading it"*) was **backwards**: `-37`
> measured the inline shape against a hook that had no read of the variable at all, so both shapes
> failed for the same reason and the boundary hypothesis was eliminated by a test that could not
> distinguish them. `-38` then fixed the reader, correctly, and nothing re-tested the shape the card
> had ruled out. **A stale negative closes a question harder than an open one.**
>
> **SET IT INLINE, in the same dx invocation as the commit:**
>
> ```
> /tmp/dx 'cd ~/repos/wealth-tensor && GATE_ROSTER_WHO=big-wealthTensor-NN ROSTER_BRAKE_ACK=<n> git commit -F <file>'
> ```
>
> `-40`'s own two commits are the proof, one token apart: `3f315af` **without** the prefix logged
> `cloud-h+04cOcn` and warned the session about its own claim; `f45ee62` **with** it logged
> `big-wealthTensor-40` and named only the two real siblings. Drill:
> `~/Scripts/roster-identity-drill.sh` — three cases against a scratch `ROSTER_DB`, live board never
> written, mutation-proved red at exactly 1. **`-39`'s "commits logged `big-wealthTensor-39`" was
> the `--replaces` half being true and the commit-name half not.**
>
> **THE COMMIT HOOK IS NOT THE ONLY CONSUMER — `gate-selfcheck.sh` NEEDS IT TOO.** Without the
> prefix the gate says of a dirty sibling repo *"THIS session did not export GATE_ROSTER_WHO so I
> cannot tell whether that is you"*; with it, the same run says *"ANOTHER session's work in flight.
> Do NOT commit it"* — a definite answer instead of a shrug. **Prefix it at wrap:**
> `dx 'GATE_ROSTER_WHO=big-wealthTensor-NN ~/Scripts/gate-selfcheck.sh'`. Assume any darwin-side
> tool that asks who you are needs the prefix; it is one token and it is never wrong to add.
> **A THIRD consumer, found by the ghost it left: `lessons.py` AUTO-COMMITS, so prefix the
> `lessons.py` call itself** — `dx 'cd ~/repos/claude-blackbook && GATE_ROSTER_WHO=... LESSONS_CONTRIBUTOR=opus python3 lessons.py add ...'` — or its commit files a `cloud-<fp>`
> claim on `claude-blackbook` that survives your `roster leave`. `-40` left one and had to
> `roster release --who cloud-<fp>` after leaving.

**THE MINUTE-TWO STANZA IS TWO LINES.** `dx --get`/`--put` are **binary-clean and self-verifying**
(`darwin-scripts 9fd8b1f`). **No base64. No manual `shasum`.**

```
/tmp/dx 'cd ~/repos/wealth-tensor && tar czf /tmp/wt-lite.tgz docs scripts tests src && tar czf /tmp/wt-data.tgz data'
/tmp/dx --get /tmp/wt-lite.tgz /tmp/wt-lite.tgz && /tmp/dx --get /tmp/wt-data.tgz /tmp/wt-data.tgz
```

`-40` measured 1,983,750 + 4,682,857 bytes, both `verified against darwin` **in words**, seconds.
**Trust the sentence, not a number. Exit 5 = bytes crossed but did not match, nothing written,
replay-safe, re-run.** `UNVERIFIED` means dx could not check and deliberately does not share that
exit code. Drill: `~/Scripts/dx-transfer-drill.sh`, run **from the cloud**, also at
`https://system.europeanflorist.com/dsh/dx-transfer-drill.sh`.

Still true: `--put` does **not** create parent directories (fails loudly, exit 1) — **`-40` hit this:
`mkdir -p` the remote directory first, in its own `dx` call.** Remote paths interpolate **raw**, so
`~` and globs expand remotely. **Never inline a multi-line string in `dx '...'`** — write locally,
`--put`, run it. **`ROSTER_BRAKE_ACK=<n>` MUST EQUAL THE STAGED COUNT** (`-40`'s were 5 and 2).

**SUITE COUNTS — COLLECTED + SKIPS, NOT TWO PASS COUNTS.**

| | at `3f315af` (verified in `-40`, both machines, same day) |
|---|---|
| collected | **828** |
| cloud (`PYTHONPATH=<root>/src`) | **820 passed / 8 skipped**, ~138 s, **every skip `not a git work tree`** |
| darwin (`.venv/bin/python -m pytest`) | **828 passed**, ~57 s |

*The cloud figure came off a tree pulled entirely by `--get`, which beats a sha: a sha proves the
tarball, a green suite proves the extracted tree.*

---

## 0 · THE TELL, NOW IN TWENTY-FIVE SHAPES

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL GONE QUIET (`-32`). `-33`: instruments that agree with themselves.
`-34`: defects nobody introduced. `-35`: defects you are about to introduce. `-36`: pre-commit the
FAVOURABLE outcome's meaning; an item naming both a document and a population is two claims. `-37`:
a pre-written repair's site count is the one part no anchor can contradict; a mutation that does not
mutate reports your guard as weak. `-38`: a proposed statistic can be a tautology in measurement's
clothing — do the algebra first; a citation carries its population or nothing; grep the estate for
the ANSWER, not the symptom; in a shared tools directory the file-creation verb is the safety check.
`-39`: an inherited claim about HOW something fails is a claim about whether it gets fixed; N
observations with N workarounds and zero causes means the corpus is accumulating; a handoff
instruction silently outranks a standing doctrine leaf; **assert the EXACT exit code, never merely
"nonzero"**; build the fix where it can be proven without shipping it. **`-40` adds three:**

- **A HYPOTHESIS ELIMINATED BY A MEASUREMENT TAKEN AGAINST A SINCE-CHANGED SYSTEM IS A STALE
  NEGATIVE, AND A STALE NEGATIVE CLOSES A QUESTION HARDER THAN AN OPEN ONE.** `-37` ruled out the dx
  environment boundary on a test run against a hook that could not read the variable; `-38` fixed the
  hook; nobody re-tested the ruled-out shape, and the card ran eight sessions on a one-token fix.
  This is `-39`'s severity finding one layer down — there the wrong attribute was *how* it failed,
  here it is *what it is not*. **When you eliminate a hypothesis, record WHAT ELSE WAS TRUE AT THE
  TIME**, because a fix landing anywhere in the chain revives it and nothing will notice.
  Banked: `2026-08-14-hypothesis-eliminated-against-since-changed-system`.
- **A REGISTRATION CARRIES REPORTING CONSTRAINTS AS WELL AS PREDICTIONS, AND THE CONSTRAINTS ARE
  GREPPABLE.** `REG-003` §7 forbade rounding α̂; §5.4 obeyed and the abstract did not, along with three
  other downstream sites. That is the characteristic shape and it is *worse* than a uniform lapse:
  the qualification exists, in the right paragraph, and does not travel. **The audit is a grep** —
  pull every MUST / MAY NOT / NO SENTENCE MAY out of the registrations and grep the manuscript for
  each governed quantity. The repair is always **replace the noun phrase**, never add a caveat: a
  narrower noun phrase is shorter than a hedge and cannot raise the defensive-sentence count.
- **WHEN A ROBUSTNESS CUT IS REPORTED, CHECK IT AGAINST THE BOUNDARY THE *CLAIM* NEEDS, NOT THE
  BENCHMARK THAT FLATTERS IT.** §5.4 reports the adverse cut as *"still an order of magnitude above
  the calibration"* — 0.327 against 0.05, true — while the claim it supports needs 0.327 above
  **0.3333**, which it misses by 0.006. **And note which uncertainty bites:** the 95% interval was
  harmless (0.959 at its lower bound) and the *bridge* uncertainty was fatal, which is the general
  case whenever an instrument is repurposed.

**AND (BUG SPRAY, live again):** `-40`'s first identity drill printed three cases and could not tell
any of them apart, because it copied a live board that already carried both names. **A green case
that is green because the state was already there is the same defect as a red case that is red for
the wrong reason.** Wipe the state each case sets out to create, and add a control that writes a
name belonging to nobody.

**`-41` adds four, and the first two are the same finding seen from two sides:**

- **WHEN A HAND-AUDIT FINDS N VIOLATION SITES, IT FOUND THEM THROUGH ONE DOOR.** `SCOUT-001` T1
  tabulated **five** sites for `REG-003` §7 by grepping the noun phrase *"the recognition rate."*
  There were **six**. The sixth, §9 limitation 4, violated §7 through the **symbol**: *"α is no
  longer in that list: §5.4 estimates it at 0.408 per year"* names no recognition rate at all, so a
  grep of the noun phrase reports the manuscript clean. **Before trusting a site count, ask what
  the audit matched ON, and enumerate the other ways the document could say the same thing.**
  Banked: `2026-08-14-registration-carries-reporting-constraints-well-predictions`.
- **A COMPLIANCE GRADE APPLIED AT PARAGRAPH RESOLUTION AGAINST A RULE WRITTEN AT SENTENCE RESOLUTION
  IS A FALSE GREEN — AND THE DOCUMENT THAT MAKES THAT MISTAKE IS OFTEN THE ONE THAT JUST NAMED THE
  FAILURE MODE.** `SCOUT-001` identified the defect's characteristic shape as *"a qualification that
  exists in the right paragraph and does not travel"* and, one row later in the same table, graded
  §5.4 as complying **in full** — because §5.4's *paragraph* names the instrument and both biases.
  §5.4's bolded **lead sentence** rounded exactly as §7 forbids, and it is the one line a skimming
  referee reads. **Read the resolution of the rule before checking compliance.**
  Banked: `2026-08-14-compliance-grade-applied-paragraph-resolution-against`.
- **A PUBLISHED NUMBER NOBODY EVER RECOMPUTED IN EXACT ARITHMETIC CAN BE ONE ULP WRONG AND LOOK
  PERFECT.** §4.4 printed **0.2999** for a cell that is exactly **3/10**; `0.05 − 0.030` is
  `0.020000000000000004` in binary and something in the original chain truncated. The repository
  **already knew this hazard** — `scripts/reg012_band_edge_phase.py` carries a comment about
  `4.3 − 4` and `RESULT-REG-012` §4 says it in prose — and had never pointed it at a published
  table. *A hazard known in one instrument is not knowledge the estate has.* The practice that
  caught it: when an edit script must reproduce a published column as its gate, compute in
  `fractions.Fraction`, and the gate **finds** the artefact instead of being tuned around it.
  Banked: `2026-08-14-published-number-nobody-ever-recomputed-exact`.
- **AN INHERITED CLAIM IS A CLAIM, NOT A MEASUREMENT, EVEN WHEN THE DOCUMENT CARRYING IT DID THE
  MEASURING — AND THE CHEAPEST CHECK IS ITS OWN TABLE.** `SCOUT-001` §3 says *"goodwill is the
  least-censored tier in retail"*; its own printed table, one line above, shows tier 0 at **4.8%**
  against goodwill's **5.1%**. It was three lines from entering the manuscript as prose nobody had
  re-derived. Banked: `2026-08-14-inherited-claim-claim-measurement-even-document`.

**AND (BUG SPRAY, `-41`): A GUARD GOING RED ON A LEGITIMATE ADDITION IS INFORMATION ABOUT THE NUMBER
YOU CHOSE, NOT ONLY ABOUT THE GUARD.** T4's new identified-set width was written as `0.32`;
`test_restatement_reach.py` went red because `0.32` is already REG-002's ladder draw pinned to two
sections. Declaring the new section in the guard's counts would have silenced it and left a future
red pointing at the wrong quantity. **The repair was to change the representation** — `31.7%` of the
unit interval, which is what the probe actually reports and is strictly more precise than the
rounding it replaced. Banked: `2026-08-14-document-has-restatement-count-guard-new`.

**Everything `-33` through `-40` banked is unchanged and still sharp.** A guard must scan assertions,
not quotations. Commit-shaped mutations go in a throwaway worktree. `severity.check`'s witness must
return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory, and
APPEND to an existing drill rather than replacing it — **`-40` obeyed this: `roster-identity-drill.sh`
is a new name checked free, and `roster-oncommit-drill.sh` is untouched.**

---

## 1 · WHAT HAPPENED

**`7088f6b` — `SCOUT-001`'s five manuscript tickets, worked. This was the at-bat.** T1, T3, T4, T5,
T6 plus both free steelmen, in six `wtNNN` edit scripts and three new guards. **`G-COACH-3` was
engaged for the first time and held at 3 → 3 (+0)** against
`docs/papers/paper-III-dual-tensor/paper-III.md.bak-pre-wt102-tickets`, the pre-edit copy taken
before a byte moved. Every ticket was a REPLACE, a STEELMAN or a CUT. **ABSORB was not used and not
one hedging sentence was added.**

- **T1 · `REG-003` §7 — SIX sites, not the five the report named.** Repaired by noun-phrase
  replacement at the abstract, §4.4, §4.9, **§5.4's own bolded lead**, the §7 ledger and §9
  limitation 4. Two replacement phrases, both assembled in one place: *"the peak-to-charge
  recognition rate"* (PRE-002's own registered name for the interval) where the number is the point,
  and §7's own *"the recognition rate PRE-002's instrument identifies"* at first use in a section
  that reasons about it. **§9 limitation 4 is not a rename:** *"α is no longer in that list"* was
  false, and now says what is true — α is measured *for the quantity PRE-002's instrument dates*,
  and the bridge to the model's α is the one §6.2 requires of every registration and this paper has
  not written. That is §6.2's discipline applied to §5.4's own number, in the section that lists
  what the paper does not know. `scripts/wt102_edits_reg003_sec7.py`.
- **T3 · the domain rescue, at the boundary the claim needs.** §4.4 gains an **R at α̂ = 0.327**
  column (τ unchanged at −0.67, so the ordering does not move) and the flat *"lies inside the domain
  after all"* becomes the range: 0.974 admissible at the measured rate, **0.959** at the interval's
  lower bound, **0.814** at the registered adverse cut where the rectangle's own fastest disclosed
  rate of 0.3333 is no longer cleared — and the closing sentence now names **which uncertainty
  bites** (the bridge, not the sample). **The abstract mirrors it**, because a qualification that
  does not travel is precisely T1's defect and repeating it in the same session would be comic.
  `scripts/wt103_edits_t3_adverse_cut.py`.
- **T4 · the continuum priced in the currency accountants have intuitions about.** The φ = 0 end
  demands books opening **51% above** the physical asset; bounding that gap at ten per cent still
  leaves an identified set covering **31.7% of the unit interval** — fatal to a cross-sectional
  ranking, and no longer dismissible as an unbounded-freedom artefact. Plus the CUT: the family is
  computed on a **g₀ = +0.15** world, not §4.2's square books.
  **Free steelman, same script:** §4.3's rate-times-duration paragraph **moved** to sit directly
  under §4.2's observational-equivalence box, where it converts *this filter* into *any filter of
  this kind* at the moment the identification bench first doubts it. §4.3 now ends on *"That is why
  the standards distinguish them"* — a better last line than the one it had.
  `scripts/wt104_edits_t4_and_form_independence.py`.
- **T6 · the paper's one overclaim about its own failure, replaced by the shorter true thing.**
  *"No reading of the tier ordering as a noisy version of the predicted one survives that pattern"*
  is gone; **the predicted ordering appears in 5.7% of firm-clustered resamples in the pilot and
  5.8% in the replication**, resampling firms because §5.4's own co-occurrence finding says events
  are not the unit. The tier-2 observation stays as an observation.
  **Free steelman, same script:** the per-tier censoring row in §5.3's PRE-001-vs-PRE-002 table.
  `scripts/wt105_edits_t6_and_censoring.py`.
- **T5 · the scope sentence, and the pull that was never pinned.** §6.1 now reads *"in US-listed
  retail trade (SIC 5200–5999) or computer and data processing services (SIC 7370–7379), among
  registrants filing in 2013–2024, on charges recognised 2012 Q2 – 2026 Q2"*. §11 gains a **Data
  retrieval, pinned** bullet: retrieval date **2026-08-12**, commit **0569ab6**, and a SHA-256 for
  **both** `data/pre-002-events.json` and `data/pre-002-riskset.json`. That is §11's own per-file
  `src/` discipline applied to the input that actually moves.
  `scripts/wt106_edits_t5_scope_and_pull.py`.
- **`wt107` re-wraps only the paragraphs this session touched**, guarded by an identity on the
  whitespace-flattened file, so its diff is reviewable as whitespace and nothing else. It exists
  because `patchkit`'s no-internal-newline rule and a tidy 100-column manuscript pull in opposite
  directions, and the next session should not have to find an anchor inside a ragged paragraph.

**TWO DEFECTS FOUND BY GUARDS RATHER THAN BY READING, both repaired in the same commit:**

- **§4.4's tier-0 calibration cell printed `0.2999` for an exactly rational `3/10`** — a float
  truncation carried unread since it was typed as a literal into `scripts/wt092_edits_44.py`.
  `wt103`'s gate, which reproduces the manuscript's own two published columns in
  `fractions.Fraction` before writing a third, **refused on it**. Corrected to `0.3000`.
  **`wt092_edits_44.py` is deliberately NOT edited: it is the record of an edit that happened, and a
  record rewritten to match the present is not a record.**
- **`SCOUT-001` §3's censoring prose contradicts `SCOUT-001` §3's censoring table.** Corrected in
  place, and the manuscript got the true version — goodwill is the least-censored tier in the
  replication and the **second**-least in the pilot (4.8% for tier 0 against its 5.1%). The attack
  it closes is closed either way, because the attack needs goodwill's tail to be the hidden one.

**Three new guards, and each one is a wire between a claim and the thing that licenses it:**

| guard | what goes red |
|---|---|
| `tests/test_reg003_sec7_rounding.py` | any sentence that names a recognition rate, carries a measurement of α̂ and carries no qualifier — **two doors**, noun phrase and bare symbol. Also goes red if `REG-003` §7's sentence is deleted or restated, because the guard would have lost its warrant. **RED on the six real pre-edit sentences; GREEN on eight real legal ones, including the three a cruder first cut flagged.** |
| `tests/test_t6_predicted_ordering.py` | §5.3's 5.7% / 5.8% drifting from what `probes/tier2_tallest.py` measures. Runs the committed probe (~6 s) rather than duplicating its arithmetic. |
| `tests/test_pre002_data_is_pinned.py` | either data file's SHA-256 no longer appearing in §11 — i.e. a re-pull landing without the manuscript being told. |

`tests/test_restatement_reach.py`'s `REACH` gains three declared counts (0.327 in §4.4 twice, 688 and
695 in §11 once each) — the bargain that file's own docstring struck, paid.

**`claude-blackbook` — five global leaves banked, five corroborated.** `use` at the moment each was
read, `record-outcome wealthTensor-41 pass` at wrap.

| | |
|---|---|
| **G-COACH-3** | **ENGAGED and HELD — 3 → 3 (+0)** against the pre-edit copy; `DEFENSIVE-BASELINE.json` unchanged and still accurate |
| **G-COACH-1** | held — every weakness named shipped a REPLACE, STEELMAN or CUT |
| **G-COACH-5** | held — the strength named is `SCOUT-001` S3, the §4.5 row that refused in 400 of 400 draws and took the claim out of the paper. **It is still buried in a 40-row ledger where it looks like the other 39.** |
| suite | **849 collected** · darwin **849 passed** (~60 s) · cloud **841 passed / 8 skipped** (~171 s, every skip `not a git work tree`) |
| new guards | 3 test files, 21 new tests |
| lessons | **five** banked global · **five** corroborated via `use` + `record-outcome` |
| cards | `1217501627934797` **worked and commented** · `1217501628088122` (T2) untouched and still barred |
| stopping rules | **honoured — no lag gradient was computed on any subsample, and the research ledger on paper III is still empty** |

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-39`'s rulings stand **verbatim**: no third disclosure instrument; phrase set
  frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS THE *DISCLOSED* δ**; **REG-009 IS
  CLOSED, numbering 6–12**; **§4's COVERAGE SILENCE AND §7.5's TWO ERRATA STAY RECORDED, NOT
  REPAIRED**; **DO NOT SPEND THE TIE-BREAK**; **DO NOT PROMOTE `R_MIN`**; **`data/reg-009-band-count.json`
  IS `-31`'s**; **`test_the_cycle_choice_now_decides_the_answer` IS A RESULT**; **§10 IS NOT TOUCHED BY
  SCOPE-001**; **SCOPE-001, PIN-001, TERM-001, TERM-002 ARE CLOSED**; **§11 PINS PER FILE**; **P3 FAILED
  AND REG-010 DID NOT RE-SCORE IT**; **REG-010's POPULATION IS Ψ's 683 PAIRS**; **NEITHER BANDING IS
  PROMOTED**; **REG-008 §2's PROVISIONAL FILENAMES STAY and the CONTAMINATED probe's DOCSTRING IS LEFT
  STANDING**; **THE BAND COUNT MAY NOT BE RE-EDGED AND ITS FLOOR RE-READ (R5)**; **REG-012 IS CLOSED ON
  BRANCH F AND ANSWERS NOTHING ABOUT §7.5** — the shifted band count is *refused rather than merely
  unperformed*; **THE TWO SENSITIVITIES ARE SEPARATE AND MUST NOT BE MERGED**; **REG-012's NUMBERS ARE
  THE BAND COUNT'S AND 55.71 % IS Ψ's** — `tests/test_reg012_band_edge_phase.py` goes red if they
  converge; **`selected_lives` IS THE ONE SELECTION PATH.**
- **THE SCOUTING REPORT'S TIMING IS CLAUDE'S CALL, NOT JASON'S** (his ruling, 2026-08-14). Charter §4
  says so at the scene. **`-40` ran it. It is done and it does not run again on this paper** unless the
  manuscript changes materially.
- **`dx --get`/`--put` DO NOT NEED BASE64.** A base64 leg around dx means you are reading a superseded
  leaf. Run `~/Scripts/dx-transfer-drill.sh` and believe it.
- **NEW · `SCOUT-001` IS NOT THE MANUSCRIPT AND MAY NOT FLOW INTO IT RAW.** Charter §4: it feeds
  practice, as §2-style repair tickets. **ABSORB stays illegal** — every ticket in it names a narrower
  claim, and not one asks for a hedging sentence. If a session finds itself pasting a scouting finding
  into the paper as a caveat, it has the direction exactly backwards.
- **NEW · T2 MAY NOT BE RUN ON THIS DATA.** Any design using the annual-test-date confound — an onset
  bridge carrying the offset, or a restriction to interim-triggered charges — is a **third instrument
  for the lag gradient**. PRE-002 §5's stopping rule bars it; `REG-003` §7 bars reading any such
  finding as evidence the gradient was there all along. **Fresh registration, fresh pull, registered
  before the instrument is coded, and it may not cite the present failure as support for anything.**
  Carded at `1217501628088122`. `SCOUT-001` measured only a property of the *instrument* and says so
  in a scope guard in its own docstring.
- **NEW · §4.4's TIER-0 CALIBRATION CELL IS `0.3000` AND STAYS `0.3000`.** It is `3/10` exactly,
  in rationals. The old `0.2999` was a binary-float truncation, and `scripts/wt092_edits_44.py`
  still carries the original literal **on purpose** — it is the record of an edit that happened.
  Do not "restore" the cell and do not edit the historical script to match.
- **NEW · T4's IDENTIFIED-SET WIDTH IS PRINTED AS `31.7%` OF THE UNIT INTERVAL, NOT AS `0.32`.**
  `0.32` is already REG-002's ladder draw, pinned to §4.4 and §7 by `test_restatement_reach.py`;
  printing a second, unrelated quantity with that token makes the guard pin the collision and its
  next red would name the wrong quantity. `31.7%` is also what the probe actually reports.
- **NEW · `SCOUT-001` IS WORKED, NOT PENDING.** Five of its six tickets and both free steelmen
  landed at `7088f6b`. Only **T2** remains, and T2 is barred on this data by the ruling above. A
  session that opens `SCOUT-001` looking for work should read §3 of this file first.

---

## 3 · THE AT-BAT for `-42` — **the constraint sweep. `REG-003` §7 was not the only one.**

**`-41` enforced one reporting constraint and proved the class exists.** `REG-003` §7 said *no
sentence anywhere may round it* and the manuscript rounded at six sites for two days, in the abstract
of a paper whose one unusual credibility asset is that its registrations are public and honoured.
There is now a machine behind that one sentence — `tests/test_reg003_sec7_rounding.py`. **There are
a dozen registrations in `docs/preregistration/` and nobody has ever enumerated what the others
forbid.**

**The at-bat, and it is a grep before it is anything else:**

1. **Pull every MUST / MAY NOT / NO SENTENCE MAY / MAY NOT BE CITED / IS REPORTED AS out of every
   file in `docs/preregistration/`,** and write the inventory down — the point is the LIST, and it
   does not exist. Ten minutes with `grep -n` gets a first cut; the reading is what costs.
2. **For each governed quantity, grep the manuscript** and check compliance **at the resolution the
   constraint is written at** (`-41`'s second tell: a paragraph-level grade against a sentence-level
   rule is a false green). Check both doors — the noun phrase *and* the symbol.
3. **Mechanise the ones a machine can recognise on sight**, in the same session, in the shape
   `test_reg003_sec7_rounding.py` established: *predication, not vocabulary* — flag a unit that
   names the governed quantity, carries the governed measurement and carries no qualifier. **Prove
   each RED on real violating text and GREEN on real legal text**, including any site a cruder first
   cut flags. A linter tuned until it is quiet is worth nothing unless the sites it went quiet on
   are named in the test.
4. **Every guard declares its warrant**: assert the registration's own sentence is still there, so a
   deleted constraint reports a lost licence instead of silently enforcing a rule the repo dropped.

**Cheap known starting points, already visible from `-41`:** `PRE-002` §5's stopping rule (*"there is
no third instrument"*), `REG-003` §7's *"rejecting independence in §4 does not rescue PRE-001"*,
`REG-003` §5's *"nothing in §5 may be cited as support for anything in §4.7"*, `REG-009` §12's
terminology ruling and `REG-012` §7's *refused rather than merely unperformed*. Two of those are
already enforced by other tests; **the point of the sweep is finding the ones that are not.**

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The remaining board:

1. **`SCOUT-001` §1.1's presentation observation, and it is Jason's call, not a ticket:** §7's
   forty-row ledger dilutes its two load-bearing rows — including **S3, the §4.5 row that refused in
   400 of 400 draws**, which `SCOUT-001` §3 calls the single strongest fact about this paper's
   process — in thirty rows showing a closed form matching the simulation that shares its code. The
   fix is a column separating algebra-versus-code rows from rows that risked something. `-41` did not
   take it because re-sorting the ledger is a judgement about a reader, not a defect.
2. **Infra siblings, carded, Claude-hands:** `@concierge_ingest` / `@concierge_router` carry the same
   Caddy ordering defect `@darlish` had (`1217488447555628`) · the live capability path is committed
   in cleartext to `n8n-stack` and the repo copy has drifted (`1217488117177482`).
3. **AAR A2's residual** (`1217496462088036` is **CLOSED**; what remains is the other four `post-*`
   hooks) · card-lint (`1217483699706758`) · the gate card (`1217465036940491`).
4. **Still open from the dossier era and still good**, re-served by nobody: `REVIEW-004` **C6** (name
   one asset class where §2's domain restriction holds *and* a recognition event is observable in
   filings — ASC 410 asset retirement obligations is the referee's own offered rescue) and **C10**
   (IAS 36's impairment-reversal asymmetry is a free cross-regime falsification test).
5. The phrase set has a passenger: 30.4 % of trigger sentences match only `events or circumstances`;
   7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
6. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
7. **Not mine, not touched:** handoff-lint warns `HANDOFF-acmeLedger-07.md:22` and `-09.md:36,42`
   make verification claims with no vantage point. Siblings were live on those; don't clobber.

---

## 4 · WHAT WOULD HAVE SAVED `-41` TIME

- **THE FIRST TEN MINUTES DECIDED THE SESSION FOR THE SEVENTH TIME RUNNING** (`-35` truth, `-36`
  population, `-37` count, `-38` premise-and-instrument, `-39` severity, `-40` the promise the
  document made about itself, `-41` **the resolution the promise was written at**). `-41`'s sixth
  T1 site came from reading `REG-003` §7 and then running the grep **myself** instead of trusting
  the inherited site count. **Spend the ten minutes, and spend them on the registration.**
- **RE-RUN THE INHERITED MEASUREMENTS BEFORE BUILDING ON THEM.** All four `SCOUT-001` probes
  reproduce exactly — which is why the *two* places its prose diverges from its own output stand out
  instead of hiding. Four probe runs cost under a minute and turned two inherited claims into
  measurements, one of which was wrong.
- **WRITE THE EDIT SCRIPT'S GATE AGAINST THE MANUSCRIPT'S OWN PUBLISHED CELLS.** `wt103` had to
  reproduce §4.4's two existing R columns before it could add a third, and that gate found a defect
  nobody was looking for. **A gate that only protects the new work is half a gate.**
- **`patchkit` ANCHORS MUST HAVE NO INTERNAL NEWLINE, AND THE REPLACEMENT CARRIES THE RE-WRAP.**
  Every anchor in `wt102`–`wt106` is newline-free and every one resolved first time. The cost is a
  ragged paragraph, and `wt107` is the answer: re-wrap at the end, in its own commitable step,
  guarded by an identity on the flattened text so the diff is provably whitespace.
- **A GUARD GOING RED ON A LEGITIMATE ADDITION IS INFORMATION ABOUT YOUR NUMBER.** See §0.
- **`--put` DOES NOT CREATE PARENT DIRECTORIES.** `mkdir -p` the remote directory in its own `dx`
  call first. (`-41` needed none; every target directory already existed.)
- **SET `GATE_ROSTER_WHO` INLINE IN THE SAME `dx` INVOCATION.** Worked first time on the commit,
  `roster join` and `roster claim`. The retired `export` line stays retired.
- **`roster leave` ONCE**, at wrap.
- **CORROBORATE THE LEAVES YOU USED.** `use` at the moment each is read, `record-outcome` at wrap.

---

## 5 · DEFINITION OF DONE (carry this forward)

**The manuscript pass is done.** `SCOUT-001`'s five workable tickets and both free steelmen landed,
`G-COACH-3` was engaged with a pre-edit copy taken before a byte moved and held flat, three guards
now wire three of the new claims to the data that licenses them, and two defects the tickets did not
name were found by gates and repaired in the same commit. **The scouting report is worked, not
pending.**

**The research ledger on paper III is still empty, and it stays empty.** T2 is the only live
registration idea and it is barred on this data by ruling; it needs a fresh registration, a fresh
pull, and registration before its instrument is coded.

**The next unit of done is the CONSTRAINT SWEEP** (§3): an inventory of every reporting constraint in
`docs/preregistration/`, each checked against the manuscript at its own resolution and through both
doors, and each one a machine can recognise mechanised with a red-and-green proof and a declared
warrant. **`-41` proved the class is real by finding six live violations of the one constraint anyone
had read. The honest question is how many of the others have never been checked at all** — and unlike
most items on this board, that question has a bounded, greppable answer.
