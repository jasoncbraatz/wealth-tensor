---
new_instrument: none
instrument_name: "— (none. All five axes A1–A5 inherited and run before a word of prose; the axis matrix has been closed at 15 of 15 since `-80` and Paper II sits at 5 of 5, so no cell could be filled. `A3′` — pointer CORRECTNESS — is inherited too: the axis originates `wealthTensor-99` on this manuscript (`II-40`) and `-101` mechanised it as `scripts/wt184_pointer_correctness.py`; this pass is its FIRST APPLICATION TO PAPER II, the held-out test `-101`'s handoff set up, and the instrument is `-101`'s, not this pass's. `A6`, the docstring axis, remains parked — sixth pass. `scripts/wt188_paperII_p7pass13.py` and `scripts/wt189_paperII_promises.py` are the PATCHES of record, not instruments — the same object `wt181` was at `-99` and `wt185`/`wt186` were at `-101`. The FIFTH consecutive frozen-instrument pass on Paper II.)"
new_instrument_alt: none
findings_from_new_axis: 0 of 2
findings_from_new_instrument: 0 of 2
residue_of_previous_pass: 0 of 2
shape_promise_about_artefact: 2 of 2
shape_deferral_with_empty_target: 0 of 2
shape_neither: 0 of 2
manuscript_edits: 2 of 2
consecutive_zero_passes_after_this_pass: 0
prediction_under_test: "none — `-101`'s row proposes no mechanism and makes no prediction, and this pass does not invent one to settle. See §5."
prediction_verdict: N/A
# FALSIFY THIS ROW, SEVEN WAYS.
#   1. `none`: two scripts were ADDED this session and neither is an instrument.
#      `git log --diff-filter=A -- scripts/wt188_paperII_p7pass13.py scripts/wt189_paperII_promises.py`
#      returns 4478f25, this session — expected, and it does not falsify the row. What WOULD
#      falsify it is a new way of LOOKING. §1 cites every axis to the session that built it.
#      The sharpest test is A3′: if `scripts/wt184_pointer_correctness.py` blames to THIS
#      session the row is wrong. It blames to `d162969`, `wealthTensor-101`.
#   2. `0 of 2` from the new axis — AND THIS IS THE ROW'S HEADLINE, NOT ITS FOOTNOTE.
#      wt184 was pointed at paper-II for the first time and returned ELEVEN Rule-1 flags and
#      ZERO findings: all eleven are false positives, and §3 names the cause and proves it.
#      `python3 scripts/wt188_paperII_p7pass13.py` re-derives every one. If a successor
#      credits II-43 or II-44 to wt184, it has not read §2 — wt184 flagged neither and §3
#      says why it structurally could not.
#   3. `0 of 2` residue: `git blame` the two sites at the parent commit 73e1966.
#      II-43's defective word ("five") → 76355d62, `wealthTensor-92`, 2026-08-19, a REPAIR
#      pass and not a P7 read. II-44's three sites → bf073634, 2026-08-17 14:31, the commit
#      that placed the two mandatory citations. NEITHER blames to `-99`'s 8df6d40. But read
#      §5 before you enjoy that number: `-99`'s own repair commit edits a line two below
#      II-43's, inside the same clause, and left the count uncorrected. NO MECHANISM IS
#      PROPOSED FROM EITHER FACT; see -77/-78 for why residue is not one.
#   4. `2 of 2` manuscript edits: `scripts/wt188_paperII_p7pass13.py` touches paper-II.md at
#      FIVE sites for two findings (II-44 has three, II-43 has two). It carries 62
#      post-conditions, 19 NEGATIVE, and is idempotent — run it twice and diff the stdout;
#      they are byte-identical. If any finding is repaired outside the manuscript, the count
#      is wrong. `-79`'s narrower rule (count only findings requiring a manuscript edit)
#      scores this pass 2 as well, so the two rules agree.
#   5. the shapes: 2 promise / 0 deferral / 0 neither, on REVIEW-019 §6's two definitions
#      unchanged, against the 1/2/1 `-83` found and the 1/1/1 `-101` found on paper-III.
#      n = 2 AND THE ROW CLAIMS NOTHING FROM IT. Both findings are `-79(i)` — a promise about
#      an artefact, unchecked by checking the artefact — and for II-44 the artefact is a
#      CITED PAPER, which is the reading A5 exists for and which five passes deferred.
#   6. `consecutive_zero_passes_after_this_pass: 0`. It is not zero because the pass found
#      two things. §6 says what a reader should and should not conclude from 2 being the
#      lowest number in this manuscript's thirteen-pass history.
#   7. THE ONE THAT MATTERS MOST: is this a HARD-LOOKED-FOR two, or a tired one? Six checks
#      that could have produced a finding and did not are named in §3 with the evidence that
#      killed them, and the periodicity measurement in §4 is a check that came back CLEAN on
#      five seeds at the reported horizon and is reported as a strength rather than buried.
# Ledger of all thirteen Paper II passes: docs/p7-passes.tsv
---

# REVIEW-037 · Paper II's THIRTEENTH independent `P7` read — the pass that finally opened the source

**Session:** `wealthTensor-102` · **Date:** 2026-08-24 · **Manuscript:**
`docs/papers/paper-II-redistribution/paper-II.md`, **569 lines read end to end**
**Patches of record:** `scripts/wt188_paperII_p7pass13.py` — **5 manuscript sites, net +5 lines**,
**62 post-conditions, 19 NEGATIVE**, idempotent, RC 0 — and
`scripts/wt189_paperII_promises.py` — 4 promise rows, 3 superseded, **19 post-conditions,
11 NEGATIVE**, idempotent, RC 0
**Repair commit** `4478f25` (layout guard RED on purpose) · **recapture** `ee4f70e`
**Result:** **two findings, two repairs, zero carded.** Paper II's counter goes
9 → 2 → 4 → 3 → 4 → 5 → 3 → 2 → 2 → 3 → **2**.

**THIS IS NOT A ZERO, AND THE DEFINITION OF DONE IS UNMOVED.** `definition_of_done` asks for
**two consecutive zero-finding passes per paper**. Paper II's consecutive-zero count was 0 before
this pass and is **0 after it**. Convergence is at minimum two further reads away for this
manuscript, and this document does not score it — `P7` is `PENDING-HUMAN` and the verdict is
Jason's.

**THE HEADLINE IS `II-44`, AND IT CAME OUT OF A TEE-UP FIVE PASSES OLD.** Tee-up 5 — *"Bouchaud
& Mézard's two verbatim quotations in Paper II §3.1, unread against source"* — was named at `-74`
and deferred at `-77`, `-99`, `-100` and `-101`. It was run here, against arXiv
`cond-mat/0002374`, the text the reference entry itself names. **Both quotations verify word for
word**, which is a clean result and is reported as one in §4. But opening the source to check the
quotations put the rest of the paragraph in view, and the sentence beside them says Bouchaud and
Mézard *"give the stationary Pareto exponent in closed form in **all four coordinates**."* In this
manuscript's own vocabulary — fixed in the Abstract, §1 and §2.2 — **the four coordinates are
base, rate, periodicity and threshold.** Their solution is continuous-time and has neither a
periodicity nor a threshold: its four are φ_I, φ_C, f_I and f_C, a rate and a redistributed
fraction for each base. The sentence over-credits the source **and, by the same stroke, hands it
§3.3** — the section whose whole result is that periodicity and threshold are trim.

**AND `II-43` IS `A4`'S SECOND QUESTION, ANSWERED ON PAPER II FOR THE FIRST TIME.** §7 enumerates
*"five quantities neither command prints in any precision."* **There are six.** §3.1's
6 × 10⁻⁶ change in Var[log *a*] is the difference of two values `wt077_tail_index.py` prints, sits
in §3, and is in none of the five. That is §7's own named failure mode — *"a single command named
for numbers it does not produce is a provenance claim that reads as checked and is not"* — one
level up, **inside the clause written to enumerate exactly this**.

---

## 0 · What is NOT claimed here, stated before the findings

* **Nothing was invented.** Five axes, all inherited, all run before a word of prose was written
  about them. `A6` stays parked. `wt188` and `wt189` are patches of record, the same object
  `wt181` was at `-79`/`-99` and `wt185`/`wt186` were at `-101`.
* **No mechanism is proposed for the finding counter.** Five have been proposed and four died one
  pass after being proposed (new instruments `-71`/`-77`, residue `-77`/`-78`, depth `-78`/`-79`,
  coverage `-80`/`-81`); only enumeration `-82`/`-83` survives. `-99` declined a 2-of-3 residue
  row, `-100` a 2-of-4 and `-101` a 0-of-3. **This pass has a 0-of-2 and declines the sixth on
  the same grounds `-101` did: a clean number on n = 2 is the same error with a friendlier face.**
* **No finding was manufactured.** Six live candidates died on contact and are named in §3 with
  the evidence that killed them, not merely listed.
* **THE NEW AXIS FOUND NOTHING ON THIS MANUSCRIPT, AND THAT IS REPORTED AS THE RESULT IT IS.**
  `-101`'s handoff set up wt184's first application to paper-II as a held-out test and said either
  outcome would be a result. The outcome is **eleven flags, eleven false positives, zero
  findings** — and three defects in the instrument, recorded in §3 and **not counted**, following
  `-99`'s precedent for a defect in a pass's own instrument.

---

## 1 · The five axes, run before a word of prose

| axis | what was run | measured output | findings |
|---|---|---|---|
| `A1` | `scripts/wt130_quantifier_sweep.py paper-II` (**RC 0**) — built at `-72` | **166 quantifier tokens on 126 of 569 lines** — unchanged from `-99`, because the manuscript has not moved since `8df6d40`; read forward from every flagged line during the end-to-end read | 0 |
| `A2` | grep Paper II for the failure modes it names in its own prose — originates `-72`; the eight are **inherited** from REVIEW-018 §1, not re-derived | 8 named failure modes turned back on the paper | **the LENS for both.** §7's *"a single command named for numbers it does not produce"* is what makes `II-43` legible; §3.1's own two letter-collision disclosures are what make `II-44`'s third, undisclosed collision legible. Neither finding is credited to `A2` — §2 credits the axis that PRODUCED it |
| `A3` | `scripts/wt133_crossref_sweep.py` (**RC 0**) — built at `-74` | Paper II: **50 §N.M references, 12 distinct, 0 unresolved, 1 dismissed as another document's**; sweep 2: 16 entries, 7 cited, **9 not** (carded `1217568192511533`, untouched — sixth pass) | 0 |
| `A3′` | `scripts/wt184_pointer_correctness.py docs/papers/paper-II-redistribution/paper-II.md` (**RC 0**) — axis originates `-99` (`II-40`), instrument built at `-101`, **first application to paper-II** | 18 sections parsed, 30 clauses carrying a §, **50 references · 12 bare top-level · 1 "unresolved" · RULE 1 28 checked, 11 FLAGGED · RULE 2 1 checked, 0 flagged** | **0 — and §3 is where that number is spent.** All eleven are false positives from one cause, and the run produced three defects in the instrument |
| `A4` | `wt030_report.py` (**RC 0**) **and** `wt077_tail_index.py` (**RC 0**) — originates `-74`. Both of `-77`'s questions asked, **and `-80`'s second question asked on this manuscript for the first time** | every tabulated §3 value reproduces; the five quantities §7 declares unprinted are each grep-absent from both stdouts in every precision — **and so is a sixth the enumeration does not name** | **`II-43`** |
| `A5` | every named artefact enumerated from the whole document, resolved, **and READ** — originates `-75`, first on Paper II at `-76` | **16 distinct backticked artefact tokens in the body** — one repo URL, five files, four named tests, three commands, three bare directories — enumerated from the pre-edit manuscript and **all resolve**; the five named files were READ; the 18-test count is **18**; `3b11f23` is still the last commit touching the module; and **the two Bouchaud & Mézard quotations were read against arXiv `cond-mat/0002374` for the first time in six passes**. *`-99` counted 22 on a broader rule that admits non-path tokens; this pass did not re-derive that rule and does not claim its number.* | **`II-44`** |

**Neither finding is credited to `A3′`.** wt184 flagged neither, and §3.1 says why it structurally
could not: `II-43` is a claim about what a *command* prints, which wt184 does not model at all, and
`II-44` is a claim about what *another document* contains — explicitly out of wt184's stated scope.

---

## 2 · The two findings, each with its repair

### 2.1 · `II-43` — §7 enumerates five exceptions and there are six · **REPLACE**

§7's regeneration bullet read *"…and except **five** quantities neither command prints in any
precision"*, then named them: §3.4's 0.99875 ceiling, §3.4's 0.90 criterion, §3.3's 0.035
periodicity span, §3.4's 0.103 Gini gap, §3.4's 0.039 top-decile margin.

**The sixth is §3.1's 6 × 10⁻⁶.** *"Unlevied, Var[log a] = 0.076542. Under the stock levy at that
budget it is 0.076536 — a change of 6 × 10⁻⁶, which is to say none at all."* `wt077_tail_index.py`
prints both inputs and does not print the difference; `wt030_report.py` prints neither. Measured
(`wt188` `E4`), with the five as its own positive-and-negative control:

| quantity | in either stdout? |
|---|---|
| 0.99875 · 0.90 · 0.035 · 0.103 · 0.039 (the five §7 names) | **absent, all five** |
| 0.107269 · 0.076542 · 0.076536 (the closed forms §7 says wt077 prints) | **present, all three** |
| **6 × 10⁻⁶** — `6e-06` / `6e-6` / `0.000006` / `6 x 10` | **absent, every form** |

The paper's own standard admits differences into that list: two of the five already are (*"each a
difference of two values `wt030_report.py` prints"*), and a third is a margin. So the enumeration
is not mis-scoped; it is one item short.

* **The word "five" blames to `76355d62`** (`wealthTensor-92`, 2026-08-19) — the repair pass that
  enumerated the clause in the first place. **`-99`'s own repair edits a line two below it**,
  inside the same clause, and re-counted nothing. Stated because it is true; §5 declines to build
  anything on it.
* **`A3′` cannot see it and neither can `A3`.** Both ask about `§N.M` pointers. This is a pointer
  at a *command*, and no axis in the matrix models command output as a referent. `A4`'s second
  question — *"is there a number the paper reports that no named command produces?"* — is the only
  one that reaches it, and this is its first run on Paper II.
* **Repair (landed):** *five* → *six*, and the sixth added in the list's own form —
  *"and §3.1's 6 × 10⁻⁶ change in Var[log *a*], the difference of two values
  `wt077_tail_index.py` prints."* No number is new to the paper; the sentence now says what is
  true of it. `E4`'s checks are **exactly-once counts, not presence tests**.

### 2.2 · `II-44` — the paper credits Bouchaud & Mézard with two coordinates they do not model · **STEELMAN**

> *"…and give the stationary Pareto exponent in closed form in all four coordinates."* — §3.1,
> and again in §6, both since `bf073634`, 2026-08-17

**"The four coordinates" is a defined term in this manuscript**, and the paper defines it three
times before §3.1: the Abstract (*"four coordinates — **base, rate, periodicity, threshold**"*),
§1 contribution 1 (*"four structural coordinates — base, rate, periodicity, threshold"*), and
§2.2, whose title is *"The levy, as four numbers."* A reader who follows the definition is told
that Bouchaud & Mézard solved in closed form for a periodicity and a threshold.

**They did not.** Read against arXiv `cond-mat/0002374` — the text the reference entry names, and
the same read that verified the quotations:

| | Bouchaud & Mézard (2000) | Paper II |
|---|---|---|
| the four in the closed form | φ_I, φ_C, f_I, f_C — a rate and a redistributed fraction **for each base** | base, rate, periodicity, threshold |
| time | **continuous** (`dW_i/dt`, Fokker–Planck) | discrete, period-assessed |
| periodicity | **absent** | §3.3, swept to *P* = 50 |
| threshold / exemption | **absent** | §3.3, swept to 20× the mean |

* **This is an over-credit that costs the paper its own result.** On the sentence as written, §3.3
  is already inside a twenty-six-year-old closed form. It is not. §6 exists to say precisely what
  is prior and what is not — *"the credit belongs precisely"* is §3.1's own phrase — and this is
  the one sentence in the paper where that goes the wrong way.
* **AND IT IS THE PAPER'S THIRD LETTER-OR-WORD COLLISION, THE ONLY ONE UNDISCLOSED.** §3.1 stops
  twice in eight lines to disclose one — *"a different object from §2.1's wage *a*, with which it
  unhappily shares a letter"*, then *"a different object from §2.1's growth drift μ … and the
  second such collision this paper has had to disclose."* **The third is in the sentence
  immediately after the second disclosure, and §6 uses the same word a third time** (*"the
  per-capita rebate fraction is a **coordinate** in their solution"*). This is REVIEW-021's
  measurement at the smallest scale it has been seen at — *naming a defect class does not exhaust
  it in the site where it was named* — now **one sentence away from the disclosure that names it**.
* **Why STEELMAN and not REPLACE or CUT.** The claim underneath is right and under-armed: Bouchaud
  & Mézard genuinely do carry both bases and both redistribution fractions in one closed form,
  which is more than "a stock-versus-flow ranking" and is worth saying in their own units. Naming
  their four as *theirs* is the stronger sentence and the accurate one at the same time.
* **Repair (landed), three sites, one edit:**

  > §3.1 · *"…give the stationary Pareto exponent in closed form in all four of **their own tax
  > parameters** — a rate and a redistributed fraction for each base."*
  >
  > §6 · the same clause, plus *"the per-capita rebate fraction is a **parameter** in their
  > solution rather than an extension awaiting one. **Their solution is continuous-time and
  > carries neither a periodicity nor a threshold, so §3.3's two trim coordinates are outside
  > it.**"*

  The added sentence is a **scope statement, not a hedge** — `defensive_count.py`'s lexicon
  deliberately excludes scope words, and `E7` proves the delta: **0 → 0 (+0)** outside
  §Limitations, against Paper II's committed baseline of 0. The manuscript is five lines longer
  and no claim in it got smaller; one claim about somebody ELSE's paper got smaller, which is the
  direction that returns §3.3 to this paper.

---

## 3 · What the held-out test measured, and six candidates that died on contact

### 3.1 · `wt184` on Paper II: eleven flags, eleven false positives, and three defects in the instrument

`-101` built `wt184` and pointed it at paper-III's 244 references. `-101`'s handoff set up its
first paper-II run as a **held-out test** and said either outcome would be a result. Here is the
outcome, and the instrument is the thing that moved.

**Eleven Rule-1 flags, all false, one cause.** Every flagged number occurs in the manuscript —
not one is a wrong number — and every one of the eleven occurs in a section *other* than the one
it was attributed to (`wt188` `E1`, checked mechanically, 11 of 11). The cause is that
**Rule 1 reads CO-OCCURRENCE as attribution**: any figure in the same clause as a `§N.M` pointer
is asserted to live in that section. The clearest case is L322, where §3.4 writes *"Across §3.1's
full rate sweep… the bounded runs' Gini spans 0.000–0.891"* — the **sweep** is §3.1's and the
**numbers** are §3.4's, and Rule 1 charges six of §3.4's own figures to §3.1.

**THIS IS THE SAME DEFECT `-101` DIAGNOSED IN RULE 2 AND BELIEVED RULE 1 DID NOT HAVE.** Tee-up 1
says, in REVIEW-036 §7 and twice in `docs/HANDOFF.md`, that Rule 2's fix is *"a verb list … or the
possessive form Rule 1 already uses, which cut its own flag set from 44 to 5."* Both halves are
wrong, and `wt188` proves each:

1. **Rule 1 contains no possessive logic of any kind** (`E2`, on the source text between the
   `# RULE 1` and `# RULE 2` markers, and on the whole file). What Rule 1 has that Rule 2 lacks is
   `bad_number()`, the `SECTIONREF` substitution, and an attribution window that fragments on
   table-cell `|` and ` ; ` boundaries.
2. **Rule 1's flag set was never cut to 5.** Measured at `-101`'s own parent commit `74934b9`:
   **43 flags**, and **44** at HEAD. REVIEW-036 adjudicates Rule 2's three flags explicitly and is
   silent on Rule 1's forty-three, so a successor reading it concludes Rule 1 came back clean.
3. **On prose, Rule 1 has no attribution window at all.** `E1`'s negative control was written to
   show the window doing work on paper-II and **failed on its first run** — 11 flags with it, 11
   without. The window only ever fires on a markdown table row, and **not one of paper-II's eleven
   flagged clauses is one**. The check was wrong about the file, so it was **tightened into the
   true statement**, not loosened. On paper-III, where §7's ledger rows are tables, the window
   *is* load-bearing: 44 with, 53 without. **That is what cut the flag set, and it is a window,
   not a possessive.**

**And a fourth defect, in the bucketing rather than the rules.** wt184 reports paper-II as having
**1 unresolved** reference; `wt133` reports **0 unresolved, 1 dismissed as another document's**.
Both are looking at the same pointer — §6's *"their §4.1"*, which is **Benhabib, Bisin & Zhu's**
§4.1, and Paper II has no §4.1. wt184's `FOREIGN` regex matches `paper-N`, `companion paper`,
`REVIEW-`, `RESULT-` and friends, and **does not match an author-attributed citation**, which is
how a literature section names another document. So the pointer lands in `unresolved` — the bucket
that reads as a defect in the *paper*. **wt184's own post-conditions assert *"zero unresolved,
agreeing with wt133"* — for paper-III only.** On paper-II that assertion is false, and nothing
would have caught it.

**None of these four is counted as a finding.** `-99` set the precedent — *"one defect in this
document's own instrument is recorded and NOT counted"* — and `-101` carded rather than counted an
apparatus item. They are §7's tee-up 1, rewritten from a guess into a measurement.

### 3.2 · Six candidates that died on contact

1. **§7's *"five quantities"* clause, checked for a SEVENTH.** Every numeric literal in §3 was
   greped against both stdouts. Exactly six are absent. A successor should not go looking for a
   seventh in §3; `E4` is the census.
2. **§1's *"to within 7 % at every rate tabulated"* against the sweep's −6.831 % at *r* = 0.010.**
   §3.1 tabulates three flow rates and their residuals are −4.344, −4.568 and −5.749 %.
   **§1 is true as written**, and `-99` already killed this exact candidate. *Settled twice; do not
   re-derive.*
3. **The Bouchaud & Mézard quotations themselves.** Both verify verbatim. See §4.
4. **§3.3's *"the minimum is interior, 0.451 at P = 30"* as a single-seed artefact.** Measured at
   the **reported** horizon *T* = 1200 across five seeds (`E5`). The argmin is **P = 30 on every
   one of the five**, seed 0 reproduces all four of §3.3's printed Ginis to three decimals, and
   the sweep span is 0.0319–0.0426 against the paper's 0.035. **Not a finding — a strength**, and
   §4 reports it as one.
5. **§2.2's `transfer_error` < 1e-12 and §3.1's *"asserts agreement within 10 %"* as unwatched
   claims** — §7's own *"nothing in the repository was watching"* turned back on the paper.
   Both are watched: `test_the_levy_is_a_pure_transfer` asserts the first literally, and
   `test_the_base_sets_a_ceiling_that_the_rate_cannot_cross` carries
   `assert flow_max == pytest.approx(ceiling, rel=0.10)`. The `3b11f23` pin is watched by
   `test_manuscript_shas_are_instrumented` + `test_pin001_code_state`'s `LATEST_TOUCH`, and the
   18-test count by `test_paper_test_counts_are_derived`. **All four claims have a guard.**
6. **The References note's *"The two marked ✓⧗"* against the file.** `✓⧗` occurs three times:
   the note itself and exactly two entries. True as written.

---

## 4 · Two checkable strengths, and one retired tee-up (charter §5)

1. **THE QUOTATIONS ARE EXACT, AFTER FIVE DEFERRALS.** Read against arXiv `cond-mat/0002374`, the
   text §7's reference entry names. The source reads: *"It shows that income taxes **tend to
   reduce the inequalities of wealth (i.e., lead to an increase of μ), even more so if part of
   this tax is redistributed**."* and *"On the other hand, **quite surprisingly, capital tax, if
   used simultaneously to income tax and not redistributed, leads to a decrease of μ**, i.e. to a
   wider distribution of wealth."* Paper II's two quotations are those two spans, word for word
   and punctuation for punctuation, including the *"quite surprisingly"* the paper keeps inside
   the quotation marks and the *"income taxes"* it correctly leaves outside them. The truncation
   at *μ* elides only *"i.e. to a wider distribution of wealth"*, which **strengthens** the
   sentence Paper II builds on it — *"Their stock levy can reverse the sign of the effect"* is
   exactly what a decrease of μ means. **Tee-up 5 is RETIRED, clean, and it is the oldest unrun
   named check on this manuscript.**
2. **§3.3'S INTERIOR MINIMUM SURVIVES A SEED SWEEP AT THE REPORTED HORIZON.** §5 item 5 says every
   simulated number is one seed at `seed = 0`, and the guard that pins this shape
   (`test_periodicity_is_second_order_at_a_matched_average_rate`) runs at *T* = 600 while the
   figure is reported at *T* = 1200 — the general form of `II-34`, tee-up 7. Measured here at
   *T* = 1200 on five seeds:

   | seed | *P*=1 | *P*=20 | *P*=30 | *P*=50 | argmin | span |
   |---|---|---|---|---|---|---|
   | 0 | 0.4860 | 0.4565 | **0.4507** | 0.4691 | **30** | 0.0353 |
   | 1 | 0.4838 | 0.4576 | **0.4466** | 0.4646 | **30** | 0.0371 |
   | 2 | 0.4927 | 0.4615 | **0.4501** | 0.4655 | **30** | 0.0426 |
   | 3 | 0.4725 | 0.4464 | **0.4406** | 0.4635 | **30** | 0.0319 |
   | 4 | 0.4798 | 0.4556 | **0.4423** | 0.4667 | **30** | 0.0375 |

   The minimum is interior on **five of five**, at the **same** *P* on five of five, and the paper's
   *"whole sweep spans 0.035"* sits inside the seed range. **The claim §5 declines to defend at the
   third decimal turns out to hold at the third decimal.** This is the `II-34` question asked on
   one specific figure and answered; it does not settle the other seventeen tests.
3. **The paper's provenance discipline is what caught its own error.** `II-43` exists only because
   §7 enumerates rather than gestures. A section that had written *"a few derived quantities are
   not printed"* would have been unfalsifiable and would have passed thirteen reads. The clause is
   wrong by one item **because it is the kind of clause that can be wrong by one item**, and that
   is the trade this project keeps making on purpose.

---

## 5 · What this pass measures about the counter — and the sixth mechanism it declines to propose

**The numbers, first, with no story attached.**

* Paper II's counter, thirteen passes: **9, 2, 4, 3, 4, 5, 3, 2, 2, 3, 2** (passes 3–13).
  **2 ties the lowest this manuscript has recorded** (`-78`, `-79`) and it has never gone below.
* **Five** consecutive frozen-instrument passes on a manuscript at 5 of 5 with a grid closed since
  `-80`: `-77` **3**, `-78` **2**, `-79` **2**, `-99` **3**, `-102` **2**.
* **Residue 0 of 2.** Neither site blames to `-99`'s `8df6d40`. The counter-evidence inside the
  same row: `-99`'s repair edits a line **two below** `II-43`'s defective word, in the same clause,
  and did not re-count it — which is not residue by the column's definition and is worth one
  sentence, not a mechanism.
* **Manuscript edits 2 of 2**, over five sites. `-79`'s narrower rule scores this pass **2** as
  well; the two rules agree.
* **The new axis contributed 0 of 2**, on its first application to this manuscript.

**The easy story, and why it is not told here.** Both findings came from checks a previous pass
NAMED and did not run — `A4`'s second question (`-80`'s move, never run on paper-II) and tee-up 5
(named at `-74`, deferred five times). That looks like a mechanism: *the counter is fed by the
not-checked list, so it will fall as the list drains.* **It is not proposed, for three reasons.**
It is a mechanism about *where findings come from*, and `-77`/`-78`, `-78`/`-79` and `-80`/`-81`
all died as exactly that. It cannot be tested by the next pass without draining the list first,
which makes it unfalsifiable on the schedule this project runs. And n = 2. **`-101` declined a
0-of-3 because a clean number on three is the same error with a friendlier face; this is a clean
number on two.**

**What IS reported, because it is a count and not a story:** of the ten tee-ups `-101` carried,
this pass ran two (5 and 2) and both returned something — one a clean verification, one a finding.
That is a fact about two items. It is offered as a reason for `-103` to spend another one, not as
a law.

**What remains askable, unchanged from `-83` and still Jason's to authorise:** two independent
readers on the **same** manuscript at the **same** coverage in the same window — the only design
that separates *"the paper has n defects left"* from *"a reviewer finds n"*. It costs two sessions
to buy one data point.

---

## 6 · What was NOT checked, named so the next pass starts here

1. **`wt184` Rule 1's forty-four flags on paper-III have never been adjudicated.** §3.1 measured
   them; nobody has read them. Eleven of eleven were false on paper-II from a cause that applies
   to paper-III identically, so the prior is that most of the forty-four are too — but *most* is
   not *all*, and `III-5` came out of that set. **This is `-103`'s at-bat.**
2. **The nine uncited reference entries on Paper II.** `wt133` sweep 2, card
   `1217568192511533`. Untouched. **Sixth pass carrying it.** paper-IV 28/28, paper-III 49/49,
   paper-II 7 of 16.
3. **`A6`, the docstring axis — PARKED, NOT SPENT.** Nineteen unasserted prose claims in
   `tests/test_redistribution.py`. Sixth pass. `-99` named
   `test_periodicity_is_second_order_at_a_matched_average_rate`'s *"Verified horizon-stable at
   T = 600 and T = 1200"* as the highest-value one; **§4's seed table is evidence for it and it
   still is not asserted anywhere in the docstring's own terms.**
4. **The general form of `II-34`.** §4 answered it for §3.3's periodicity figure and for that
   figure only. **Seventeen of the eighteen tests are still checked at *T* = 600 while every
   reported figure is at *T* = 1200.** Still a question, not a finding.
5. **The zakat citation gap.** Flagged by the paper's own closing note. **Fifth pass running.**
6. **The other three manuscripts.** Untouched and proved so — `E8` asserts Papers I, III and IV
   byte-identical across the repair, by `git status`.
7. **§3.1's *"4–7 %"* band.** −6.831 % is inside 7 % and the band is an under-claim, not an
   error. Tightening it to the sweep's max is taste. **Named so it is not re-noticed a third time.**

---

## 7 · Tooling this pass leaves behind

| artefact | what it is | state |
|---|---|---|
| `scripts/wt188_paperII_p7pass13.py` | the patch of record: A3′'s held-out test, A4's census, the seed sweep, the five manuscript edits | **RC 0, 62 post-conditions, 19 NEGATIVE, idempotent — byte-identical stdout on two consecutive runs** |
| `scripts/wt189_paperII_promises.py` | re-adjudicates the four promises §7's repair moved; 3 `#superseded` re-keys with evidence RE-RUN, 1 genuinely new | **RC 0, 19 post-conditions, 11 NEGATIVE, idempotent** |
| `docs/papers/paper-II-redistribution/paper-II.md.bak-wt188` | the pre-repair bytes, written before the first edit | present, gitignored |

**Both patch scripts were run twice before they were believed** — `-101`'s trap, and it paid
twice: the second run of `wt188` caught an E4 assertion written against the live file that
evaporated the moment the repair landed, and the second run of `wt189` confirmed the
already-applied path stays audible. **Three checks in this session failed on their first run and
all three were wrong about the file rather than the file being wrong** — `E1`'s window control,
`E6`'s byte-literal phrase counts (the manuscript is hard-wrapped and both replacements land a
newline mid-phrase), and `wt189`'s uniqueness check (a `#superseded` line legitimately names the
new id). **All three were tightened, none was deleted.**
