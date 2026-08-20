---
new_instrument: none
instrument_name: "— (none. All five axes A1–A5 inherited; docs/p7-passes.tsv records Paper II at 5 of 5 and the axis matrix closed at -80, so no cell could be filled. A6, the docstring axis, remains parked. The FOURTH consecutive frozen pass. scripts/wt181_paperII_p7pass12.py is a PATCH script — the same object wt141 was at -79 — not an axis.)"
new_instrument_alt: none
findings_from_new_axis: 0 of 3
findings_from_new_instrument: 0 of 3
residue_of_previous_pass: 2 of 3
manuscript_edits: 2 of 3
consecutive_zero_passes_after_this_pass: 0
# FALSIFY THIS ROW, FIVE WAYS.
#   1. `none`:     git log --diff-filter=A --format='%h %ad' --date=short -- scripts/wt181_paperII_p7pass12.py
#                  An add-commit in THIS session is expected and does not falsify the row: wt181
#                  is the patch of record, not an instrument. What WOULD falsify it is a new way
#                  of LOOKING. §1 cites every axis to the session that built it. The sharpest test
#                  is II-42: open REVIEW-014 §4 item 2 (wealthTensor-74, five passes ago) and find
#                  the check described there — "§3.4's 'The top-share statistic is also
#                  horizon-stable where the Gini is not.' Not measured … tests stability in *N*,
#                  not in *T*." If that item is absent, this pass invented the axis and the row is
#                  wrong. It is present, named, and was left unrun for five passes.
#   2. `residue`:  git blame the three sites at the parent commit (5b8a198).
#                  II-40 → 76355d6 (wealthTensor-92, 2026-08-19). II-41 → 76355d6, same clause.
#                  II-42 → 2b3e24b5 (2026-08-17, Paper II's FIRST independent read).
#                  If II-42 blames to 76355d6, or either of II-40/II-41 does not, the row is wrong.
#   3. `2 of 3`:   the residue count is 2, not 3, and the third is what keeps it honest — II-42
#                  has been in the tree through NINE P7 reads. If a successor reports 3 of 3, it
#                  has stopped reading at the first two.
#   4. the count:  scripts/wt181_paperII_p7pass12.py carries 24 post-conditions, 8 NEGATIVE. Run it.
#                  It exposes section_of(), measure_horizons() and separation_by_horizon() as
#                  imports, so every number below can be red-proofed without re-running the verdict.
#   5. II-42:      python3 -c "import sys; sys.path.insert(0,'scripts'); ..." — or simply run wt181
#                  and read the E5 seam. 14 of 18 config-seed pairs, worst spread 0.1706 against
#                  0.0496. If the top decile is the MORE stable statistic, the cut was wrong and
#                  the sentence must come back.
# Ledger of all twelve Paper II passes: docs/p7-passes.tsv
---

# REVIEW-034 · Paper II's TWELFTH independent `P7` read — the sentence eleven passes carried

**Session:** `wealthTensor-99` · **Date:** 2026-08-20 · **Manuscript:**
`docs/papers/paper-II-redistribution/paper-II.md`, **569 lines read end to end**
**Patch of record:** `scripts/wt181_paperII_p7pass12.py` — **2 manuscript edits, net −1 line**,
**24 post-conditions, 8 NEGATIVE**, RC 0
**Result:** **three findings, three repairs, zero carded.** Paper II's counter goes
9 → 2 → 4 → 3 → 4 → 5 → 3 → 2 → 2 → **3**.

**THIS IS NOT A ZERO, AND THE DEFINITION OF DONE IS UNMOVED.** `definition_of_done` asks for
**two consecutive zero-finding passes per paper**. Paper II's consecutive-zero count was 0 before
this pass and is **0 after it**. Convergence is at minimum two further reads away for this
manuscript, and this document does not score it — `P7` is `PENDING-HUMAN` and the verdict is
Jason's.

**THE HEADLINE IS `II-42`.** §3.4 has said, since Paper II's **first** independent read on
2026-08-17, that *"The top-share statistic is also horizon-stable where the Gini is not."*
`wealthTensor-74` flagged it **NOT MEASURED** five passes ago, named the exact check, and called
it *"a natural `wt133`"*. Nobody ran it. It was run here. **It is false**: across
*T* = 600 / 1200 / 2400 on six configurations and three seeds, the **top decile's spread exceeds
the Gini's in 14 of 18 config-seed pairs**, and its worst spread — 0.1706, flow *r* = 0.025 — is
**3.4× the Gini's worst of 0.0496**. The sentence is cut.

**AND `II-40`/`II-41` ARE BOTH IN SIX LINES `-92` WROTE.** §7's exception clause, rewritten at
`76355d6` to enumerate the five quantities no command prints, points the 0.035 periodicity span at
**§3.2**, which is *Realisation is the crux* and contains neither the number nor the sweep — and
calls 0.039 a *"difference of numbers both commands do print"* eleven words after declaring one of
its two inputs unprinted. **`wt133_crossref_sweep` is green on both**, because §3.2 resolves. A
cross-reference that resolves is not a cross-reference that is correct.

---

## 0 · What is NOT claimed here, stated before the findings

* **Nothing was invented.** Five axes, all inherited, all run before a word of prose was written
  about them. `A6` stays parked. `wt181` is the patch of record, the same object `wt141` was at
  `-79` and `wt171` was at `-92`.
* **No mechanism is proposed for the finding counter.** Five have been proposed and four died one
  pass after being proposed (new instruments `-71`/`-77`, residue `-77`/`-78`, depth `-78`/`-79`,
  coverage `-80`/`-81`); only enumeration `-82`/`-83` survives. §5 reports this pass's numbers and
  **declines the sixth**, including the one its own residue column would make easy.
* **No finding was manufactured.** Four live candidates died on contact and are named in §3 with
  the evidence that killed them, not merely listed.
* **One defect in this document's own instrument is recorded and NOT counted.** `wt181`'s first
  `section_of()` ended the last `### N.M` subsection at end-of-file, swallowing §4–§7 into "3.4",
  so it reported 0.035 in **two** subsections — counting the §7 pointer as an occurrence of the
  thing it points at. It **failed closed**, the repair rolled back untouched, and the fix is in the
  committed docstring rather than silently applied. A locator whose ranges are wrong reports the
  pointer as its own referent, which is the one answer that cannot falsify anything.

---

## 1 · The five axes, run before a word of prose

| axis | what was run | measured output | findings |
|---|---|---|---|
| `A1` | `scripts/wt130_quantifier_sweep.py paper-II` (**RC 0**) — built at `-72` | **166 quantifier tokens on 126 of 569 lines** (`-79` read 162 on 124; the manuscript moved at `-92`), read forward from every flagged line during the end-to-end read | 0 |
| `A2` | grep Paper II for the failure modes it names in its own prose — originates `-72`; the eight are **inherited** from REVIEW-018 §1, not re-derived | 8 named failure modes turned back on the paper | **`II-40` and `II-41` — BOTH.** §7's own *"a single command named for numbers it does not produce is a provenance claim that reads as checked and is not"*, applied one level up: a **section** named for a number it does not contain, and a **description** true of two of three items |
| `A3` | `scripts/wt133_crossref_sweep.py` (**RC 0**) — built at `-74` | Paper II: **49 §N.M references, 12 distinct, 0 unresolved, 1 dismissed**; sweep 2: 16 entries, 7 cited, **9 not** (carded `1217568192511533`, untouched) | 0 — **and that is the finding about `A3`**, not about the paper: it is green on `II-40` |
| `A4` | `wt030_report.py` (**RC 0**) **and** `wt077_tail_index.py` (**RC 0**) — originates `-74`. Both of `-77`'s questions asked | **all 39 tabulated §3 values reproduce**; and the five quantities §7 declares unprinted are **each grep-absent from both commands' stdout in every precision** | 0 |
| `A5` | every named artefact greped against its pairing, **enumerated from the whole document**, every named command run, and the artefacts **read** — originates `-75`, first on Paper II at `-76` | **22 distinct backticked artefacts** (unchanged from `-79`), all resolve; 5 named files exist and were read; **4 named test functions exist at their named sites and their bodies were read against the sentences that cite them**; the `3b11f23` pin is still the last commit touching the module | 0 — `II-42`'s **site** was opened by `A5` (the suite), but the finding is `-74`'s named-and-unrun check |

**The pass that produced `II-42` is not an axis.** `-74` wrote the check, its target and its
negative control (*"tests stability in N, not in T"*). Running a check a previous pass specified
and left unrun is not a new way of looking; it is the old instrument taken back out of the bag.
That is the same shape as `-79`'s `II-38`, which came off item 7 of `-78`'s own not-checked list
and was recorded `none`.

---

## 2 · The three findings, each with its repair

### 2.1 · `II-40` — §7 points the periodicity span at the wrong section · **REPLACE**

§7 line 459 read *"three differences of numbers both commands do print — **§3.2's** 0.035
periodicity span"*. The span is in **§3.3**, *Periodicity and threshold are trim, not structure*
(line 295: *"The whole sweep spans 0.035"*). §3.2 is *Realisation is the crux*; it has no
periodicity content, no sweep and no 0.035.

* **Introduced at `76355d6`** (`wealthTensor-92`, 2026-08-19) — the commit that repaired §7's
  exception clause by enumerating it. The enumeration is right; one of its five addresses is not.
* **`A3` cannot see it.** `wt133_crossref_sweep` asks whether a `§N.M` reference **resolves**.
  §3.2 exists, so the sweep is green. `wt181`'s `E4` is the check that separates *resolving* from
  *correct* for this number, and it is deliberately exposed as an import (`section_of`).
* **Repair (landed):** `§3.2` → `§3.3`, inside the R1 rewrite below. `E4` asserts positively that
  0.035 lives in `['3.3']` **and** negatively that 3.2 is not in that list.

### 2.2 · `II-41` — the same sentence mis-describes one of its own three items · **REPLACE**

The clause called all three *"differences of numbers both commands do print"*. Two are: 0.035 is
0.486 − 0.451 and 0.103 is 0.994 − 0.891, and `wt030_report.py` prints all four (`E9`). **0.039 is
not.** It is 0.90 − 0.861, and the **same sentence**, eleven words earlier, lists *"§3.4's 0.90
top-decile criterion, which is a chosen threshold and not an output"* among the quantities neither
command prints. `E9`'s negative control confirms it: `wt030_report.py` prints no 0.90.

This is REVIEW-021's measurement at the smallest scale it has been seen at — **naming a defect
class does not exhaust it in the site where it was named** — now inside a single sentence, in the
clause written to fix the class.

* **Repair (landed), one edit with `II-40`:**

  > *…§3.3's 0.035 periodicity span and §3.4's 0.103 Gini gap, each a difference of two values
  > `wt030_report.py` prints; and §3.4's 0.039 top-decile margin, the distance from that command's
  > printed 0.861 to the 0.90 threshold above.*

  Still five quantities (`E3`), no number is new to the paper, and 0.861 is printed by the command
  the sentence now names (`E9`).

### 2.3 · `II-42` — §3.4's horizon claim is false · **CUT**

> *"The top-share statistic is also horizon-stable where the Gini is not."* — §3.4, since
> `2b3e24b5`, 2026-08-17

**Measured** (`wt181` `E5`, `measure_horizons()`, seed 0/1/2 × six configurations ×
*T* = 600/1200/2400, max−min spread of each statistic):

| | Gini worst spread | top-decile worst spread | pairs where top decile moves MORE |
|---|---|---|---|
| six configs × three seeds | **0.0496** (flow *r* = 0.025, seed 0) | **0.1706** (flow *r* = 0.025, seed 0) | **14 of 18** |

The top decile is the **less** horizon-stable of the two, by 3.4× at the worst and in a clear
majority of pairs. The claim is false under its natural reading.

**Why CUT and not REPLACE.** The sentence has two readings and they disagree — the shape
REVIEW-008 already ruled a defect at `II-14`. Under the natural reading (the statistic's *value*
moves less with *T*) it is false. Under the charitable one (the *criterion's verdict* does not
change with *T*) it is true, and `E6` measures that too:

| *T* | condensed top decile | worst bounded top decile | 0.90 separates? |
|---|---|---|---|
| 600 | 0.9882 | 0.6589 | yes |
| 1200 | 1.0000 | 0.7339 | yes |
| 2400 | 1.0000 | 0.8295 | yes |

Stating the true reading in the manuscript costs three numbers §7 would then have to account
for — and the sentence immediately in front of it already carries the separation **and** its
0.039 margin. So the slot is unnecessary and the paper is stronger shorter. The true content is
not lost: it is measured, here, in `docs/`, which is where charter §1 puts the coach's notes.

**This is a CUT, not an ABSORB.** No hedge replaces it. `defensive_count.py` reads **0 outside
§Limitations, 0 inside** before and after (`E7`), against Paper II's committed baseline of 0, and
the manuscript is one line shorter.

---

## 3 · Four candidates that died on contact

1. **§1's *"within 7 % at every rate tabulated"* versus §3.1's *"4–7 %"* and its −6.8 % at
   *r* = 0.010.** §3.1's table lists three flow rates (1.000, 0.100, 0.025) whose residuals are
   −4.344 %, −4.568 %, −5.749 %; −6.831 % occurs at *r* = 0.010, which §3.1 explicitly calls *"the
   sweep's lowest rate"* and not a tabulated one. **§1 is true as written.** Tightening it to the
   full sweep (max 6.831 %) is taste, not truth, and a finding manufactured out of an under-claim
   is still a manufactured finding.
2. **§3.1's *"a denominator convention rather than noise"* against a residual that is flat at
   −4.34 % and widens to −6.83 %.** A pure 1/(1+μ) convention predicts a constant −4.76 %, so the
   widening is unexplained by the convention as named. **Already adjudicated:** REVIEW-004 line
   128–129 gives the exact form as κ = *r*·E[η⁺]/(1 + μ + *a*/w̄) — the wage term is what widens it
   at low rate — and REVIEW-011 re-opened and closed the same sentence. Settled; do not re-derive.
3. **§3.4's top-decile criterion is itself a ceiling-capped statistic, in a section whose thesis
   is that ceiling-capped statistics fail.** It is used as a **level** test, not a drift test, and
   §3.4's failure was specifically the drift test. `E6` shows the level test separating at all
   three horizons with the condensed run pinned at the ceiling — which is where the failure mode
   lives, so the criterion is pointed the right way. Not a defect.
4. **§3.1's *"Rate 1.00 on flow reaches Gini 0.125, which a stock levy reaches at rate 0.25."***
   `wt030_report.py` gives stock *r* = 0.250 → 0.123, i.e. at or below 0.125, and *r* = 0.100 →
   0.222. 0.25 is the tabulated rate at which the stock levy first reaches that depth. True as
   written.

---

## 4 · What was NOT checked, named so the next pass starts here

1. **Bouchaud & Mézard's two verbatim quotations in §3.1, still not read against the source.**
   Flagged at `-74` (REVIEW-014 §4 item 4) and again at `-77` (REVIEW-017 §4 item 4). **Third pass
   running.** `REFERENCE-POLICY` §4 governs it and the entry names arXiv `cond-mat/0002374` as the
   text consulted. This is now the **oldest unrun named check on Paper II** — and `II-42` is what
   the last one of those turned out to be worth.
2. **The general form of `II-34`, still deliberately scoped out.** 16 of the 18 tests reach the
   model through `econ()` at *T* = 600 while every reported figure is at *T* = 1200, and §7 calls
   those 18 *"the ones that hold this paper's claims in place."* `II-42` **strengthens the lead**:
   the top decile moves up to 0.17 between horizons, so a band checked only at *T* = 600 is not
   automatically a band at *T* = 1200. It was checked here that **no current assertion breaks** —
   the three `top_share(res) > 0.95` lines are one-sided on the condensed side, which only
   strengthens with *T* — so it stays a **question, not a finding**.
3. **`A6`, the docstring axis — PARKED, NOT SPENT.** Nineteen unasserted prose claims remain in
   `tests/test_redistribution.py`, and `test_periodicity_is_second_order_at_a_matched_average_rate`'s
   *"Verified horizon-stable at T = 600 and T = 1200"* is one of them — **the same words as `II-42`,
   in the apparatus rather than the manuscript.** It is now the highest-value docstring in the
   nineteen and it was not touched.
4. **The nine uncited reference entries.** `wt133` sweep 2, card `1217568192511533`. Untouched.
5. **The zakat citation gap.** Flagged by the paper's own closing note. Fourth pass running.
6. **The other three manuscripts.** Untouched and proved so — `E8` asserts Papers I, III and IV
   byte-identical across the repair.
7. **A naming drift in this apparatus, repaired forward rather than retro-fitted.** REVIEW-019's
   front matter spells the field `findings_from_new_instrument`; `docs/p7-passes.tsv`'s column is
   `findings_from_new_axis`. This document carries **both**, with the same value, so a successor
   grepping either name finds it and the ledger's spelling wins going forward. Old reviews are not
   churned.

---

## 5 · What this pass measures about the counter — and the sixth mechanism it declines to propose

**The numbers, first, with no story attached.**

* Paper II's counter, twelve passes: **9, 2, 4, 3, 4, 5, 3, 2, 2, 3** (passes 3–12).
* Four **frozen-instrument** passes on a manuscript at 5 of 5 and, since `-80`, a closed grid:
  `-77` **3**, `-78` **2**, `-79` **2**, `-99` **3**.
* **Residue 2 of 3** — the highest fraction any row has carried, tying `-77`'s 2 of 3.
* **Manuscript edits 2 of 3**, so `-79`'s proposed narrower rule (count only findings requiring a
  manuscript edit) would score this pass **3**, not 2 — every repair here changed manuscript bytes,
  unlike `-79`, whose two repairs made existing sentences true. NOT APPLIED; the ledger row is on
  the current rule.
* **The gap this pass sits in:** twenty sessions since `-79`, exactly **one** of which touched the
  manuscript (`-92`, `76355d6`, six lines) and it was **not a `P7` read**.

**The easy story, and why it is not told here.** Two of three findings are in the six lines the one
intervening repair pass wrote. That is *repair residue*, and it was **proposed at `-77` and refuted
at `-78`** (0 of 2). One row does not revive a refuted mechanism, and this row contains its own
counter-evidence: **`II-42` has been in the tree through nine `P7` reads**, blames to Paper II's
first independent read, and was named-but-unrun for five passes. A mechanism that explains two of
this pass's findings and cannot touch the third — the largest of the three — is not a mechanism.

**Every mechanism in this project's history was proposed by the pass whose own number it
explained, and four of five died to the very next pass.** This pass produced a number and is
declining to explain it. That is the whole of §5, and it is deliberate.

**What remains askable, unchanged from `-83` and still Jason's to authorise:** two independent
readers on the **same** manuscript at the **same** coverage in the same window — the only design
that separates *"the paper has n defects left"* from *"a reviewer finds n"*. It costs two sessions
to buy one data point.

---

## 6 · The anti-cheerleader clause — two checkable strengths (charter §5)

1. **The paper's provenance claims about *printing* are exactly right, and were checked in every
   precision.** §7 declares five quantities that neither named command prints. All five —
   0.99875, 0.90, 0.035, 0.103, 0.039 — are **grep-absent from both commands' stdout**. All 39
   tabulated §3 values reproduce at RC 0. Both of this pass's §7 findings are about **location and
   description**; not one number in the paper is wrong.
2. **§3.2's strongest sentence is held by the strongest available check.** *"The two paths agree
   agent by agent rather than merely on the summary statistics"* is pinned by
   `np.array_equal(unrealised["wealth"], nothing["wealth"])` — exact equality on the whole vector,
   with a committed note that the line passes at ρ = 0.00 and fails at ρ = 0.10, 0.25 and 1.00,
   both verified. A paper's headline claim pinned by an identity rather than a tolerance is rare,
   and it is the reason `II-42` could be cut with confidence: §3.4's separation does not lean on
   the sentence that failed.
