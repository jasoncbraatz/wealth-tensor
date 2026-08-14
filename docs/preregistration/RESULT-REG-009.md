# RESULT-REG-009 · The ladder's first rung, measured on the disclosure rather than on a rectangle
*wealthTensor-30 · 2026-08-14 · REG-009 §§6–12's registered run. Instrument: `scripts/reg009_ladder_inputs.py`, written after Part II was committed and pushed alone. Full output: `RESULT-REG-009-run.log`. Table: `data/reg-009-result.json`. Resolution audit: `data/reg-009-resolution-audit.json`. Pass id `e5acfd79512df290`.*

---

## 0 · What ran, and the one reading §11 required

§11 says each falsifier runs **before Ψ is computed, in the order listed**. Six of them can, and did: F1, F2, F7, F8, F9's absence half and F10 are properties of the ruler, the population and the instrument, and all six ran before any statistic existed. **F3, F4, F5 and F6 are properties of the report** — a qualifier travelling inside a table, three rates printed in one table, a heaping column beside every Ψ — and their subject does not exist until the document is rendered. They ran against the rendered document **before it was written to disk**, so a report violating any of them would never have been published. Nothing about the run's validity was decided after Ψ was seen; what was decided after Ψ existed is whether this file could be written. The reading is recorded rather than taken silently.

**The ruler was lifted, not rebuilt, and checked twice.** F1 extracts `ALPHA`, `A_EXT`, `PHI`, `DELTA`, `LIFE_PPE`, `LIFE_FIN`, `G`, `N`, `SEED` and the `d1_boundary` line out of `wt088_disclosed_ladder.py` by name, recomputes that script's committed poles from them, **and runs `wt088` as a subprocess in the same pass to compare against its own stdout**: 0.0 % admissible at α = 0.05, the first rung rising in 99.7 % of the admissible rectangle at α = 0.35, both figures matching wt088's own printed line. The closed-form boundary and the R comparison it summarises were checked for agreement on every cell of `wt088`'s own grid. The bootstrap's replicate count and seed are `wt088`'s `N` = 4000 and `SEED` = 20260812: **this instrument chooses no number of its own**, which is what makes F10 checkable rather than rhetorical.

## 1 · The population, unmoved

| | 2014-15 | 2022-23 | pooled |
|---|---|---|---|
| firm-years with any canonical life | 612 | 684 | 1296 |
| **… with BOTH — the registered unit** | **321** | **362** | **683** |
| distinct firms carrying a pair | 321 | 362 | **577** |
| … appearing in both cycles | — | — | **106** |
| `R_WEIGHT` amount-backed on both tags | 122 | 151 | **273 (0.400)** |

**F2 passed against §7.1's table exactly.** F9's row: **613 firm-years carry one tag and not the other** — 523 property-only, 90 intangible-only. They are counted here and enter no denominator anywhere below. No industry-median variant was computed (§6, D4); F9 asserts the absence rather than leaving a reader to notice it.

## 2 · Ψ, A and the heaping columns — the registered table

α̂ = 0.408 (paper III §5.4; interval [0.383, 0.432]), φ = (0.80, 0.60) lifted from `wt088`. **A is a gate on the run, not evidence about the world** — Q3 spends its direction, so it is reported and not interpreted. Pairs outside the admissible region are counted and named, never clipped and never folded into Ψ's denominator.

**pooled**

| rule | pairs | admissible | A | Ψ | 95 % clustered CI | distinct pairs | modal share |
|---|---|---|---|---|---|---|---|
| **`R_MID`** (primary) | 683 | 665 | 0.974 | 0.6586 | [0.6211, 0.6964] | 428 | 0.026 |
| `R_MIN` | 683 | 533 | 0.780 | 0.5366 | [0.4893, 0.5794] | 199 | 0.109 |
| `R_WEIGHT` | 683 | 664 | 0.972 | 0.6431 | [0.6057, 0.6798] | 629 | 0.009 |
| `R_MID` **banded** (D3, 1.00 y) | 683 | 673 | 0.985 | 0.7236 | [0.6886, 0.7574] | 178 | 0.043 |
*Every number in this table is DISCLOSED δ, not the economic δ — paper III §4.7's weak joint, unmeasured, and the slack in every row. `R_WEIGHT` is amount-backed on both tags in 273 of 683 pairs (0.400); on the other 410 it is `R_MID` under another name.*

**2014-15**

| rule | pairs | admissible | A | Ψ | 95 % clustered CI | distinct pairs | modal share |
|---|---|---|---|---|---|---|---|
| **`R_MID`** (primary) | 321 | 313 | 0.975 | 0.6326 | [0.5796, 0.6871] | 249 | 0.026 |
| `R_MIN` | 321 | 245 | 0.763 | 0.4939 | [0.4318, 0.5551] | 128 | 0.086 |
| `R_WEIGHT` | 321 | 312 | 0.972 | 0.6474 | [0.5935, 0.6994] | 299 | 0.013 |
| `R_MID` **banded** (D3, 1.00 y) | 321 | 316 | 0.984 | 0.7120 | [0.6602, 0.7612] | 140 | 0.041 |
*Every number in this table is DISCLOSED δ, not the economic δ — paper III §4.7's weak joint, unmeasured, and the slack in every row. `R_WEIGHT` is amount-backed on both tags in 273 of 683 pairs (0.400); on the other 410 it is `R_MID` under another name.*

**2022-23**

| rule | pairs | admissible | A | Ψ | 95 % clustered CI | distinct pairs | modal share |
|---|---|---|---|---|---|---|---|
| **`R_MID`** (primary) | 362 | 352 | 0.972 | 0.6818 | [0.6348, 0.7322] | 251 | 0.028 |
| `R_MIN` | 362 | 288 | 0.796 | 0.5729 | [0.5158, 0.6285] | 116 | 0.128 |
| `R_WEIGHT` | 362 | 352 | 0.972 | 0.6392 | [0.5887, 0.6882] | 345 | 0.006 |
| `R_MID` **banded** (D3, 1.00 y) | 362 | 357 | 0.986 | 0.7339 | [0.6899, 0.7793] | 111 | 0.053 |
*Every number in this table is DISCLOSED δ, not the economic δ — paper III §4.7's weak joint, unmeasured, and the slack in every row. `R_WEIGHT` is amount-backed on both tags in 273 of 683 pairs (0.400); on the other 410 it is `R_MID` under another name.*

**What A excludes, by coordinate.** Of the 683 pooled pairs, 3 are inadmissible on the property life alone, 15 on the intangible life alone and 0 on both — a life at or under 2.45 years under `R_MID`. R is undefined there; they are excluded and counted, not clipped.

## 3 · The bridge — Ψ against the manuscript's own rectangle, three rates, one pass

| quantity | α | admissible share | first rung rises | distinct pairs | modal share |
|---|---|---|---|---|---|
| Ψ_rect · asserted rectangle, uniform 400×400 (the manuscript's calibration) | 0.050 | 0.0000 | — (vacuous: the admissible set is empty) | grid | grid |
| Ψ_rect · asserted rectangle (wt088's labelled EXTENSION, where 99.7 % is computed) | 0.350 | 1.0000 | 0.9973 | grid | grid |
| Ψ_rect · asserted rectangle, at the MEASURED rate | 0.408 | 1.0000 | 0.9980 | grid | grid |
| **Ψ (disclosed pairs)**, `R_MID` | 0.408 | 0.9736 | **0.6586** | 428 | 0.026 |
*Every number in this table is DISCLOSED δ, not the economic δ — paper III §4.7's weak joint, unmeasured, and the slack in every row. `R_WEIGHT` is amount-backed on both tags in 273 of 683 pairs (0.400); on the other 410 it is `R_MID` under another name.*

**Without the third row this table would not be readable.** A gap between Ψ and 99.7 % could be the disclosure or it could be the recognition rate; Ψ_rect(α̂) holds the rectangle fixed and moves only the rate, so the two channels separate.

**S — the support share.** The share of disclosed pairs falling inside the manuscript's asserted rectangle, L₀ ∈ [10, 40] and L₁ ∈ [3, 20]. This measures the assumption directly rather than arguing about it.

| rule | S | pairs inside | pairs |
|---|---|---|---|
| `R_MID` | 0.1391 | 95 | 683 |
| `R_MIN` | 0.0571 | 39 | 683 |
| `R_WEIGHT` | 0.2123 | 145 | 683 |
*Every number in this table is DISCLOSED δ, not the economic δ — paper III §4.7's weak joint, unmeasured, and the slack in every row. `R_WEIGHT` is amount-backed on both tags in 273 of 683 pairs (0.400); on the other 410 it is `R_MID` under another name.*

## 4 · Ψ_band — the heaping robustness row, and the control that failed

Every δ collapsed to its D3 band midpoint (1.00 year) and Ψ recomputed: **Ψ_band = 0.7236** against **Ψ = 0.6586**, a difference of **0.0650**, on 178 distinct banded pairs against 428 raw ones. P3 registered five points as the line beyond which Ψ would be a statistic about the granularity of the disclosure rather than about the ladder.

**P3 FAILS, and §9 says what that means: Ψ is sensitive to the granularity of the disclosure, and §10 records it rather than the registration arguing its way out.** A one-year regranulation moves the registered statistic by 0.065, above the five points registered before the number existed. The banding was not changed after the failure and no second band width was tried: F10 refuses a free parameter introduced to reconcile a number, and a control rescued after it fails is not a control.

**What the failure does NOT do is close the gap in §3.** Ψ_band = 0.7236 is still 0.274 below Ψ_rect(α̂) = 0.9980. The granularity channel moves Ψ by 0.065; the distance to the manuscript's rectangle is 0.339. At its worst the channel is about 19% of what would have to be explained, so P2 survives P3's failure — which is the only reason both are reported in the same section rather than one of them in a footnote.

**Post-hoc, and labelled as such because it was not registered: the mechanism is visible in the bin edges.** D3's bins are lifted from `reg009_p0_lifetime_values.py` at run time — index `int(v // w)`, edges `[b * w, (b + 1) * w)` — so this file did not choose them. Those bins are half-open on the left, and **55.7% of the lives entering Ψ_band are integers**, which sit exactly on a bin's left edge. A midpoint collapse therefore *translates* a heaped disclosure by half a year rather than *rounding* it, which is not the operation the phrase 'a one-year rounding' in §9 brings to mind. That is an observation about the operator, checkable from two lines of committed source, and it is **not** offered as a reason to discount the verdict: P3 failed as registered.

**Repair, attached, per charter §2 — TEE UP, priced now so it cannot become a rescue later.** A second banding whose bin edges fall on half-integers, so the heap sits at a bin's *centre* and the collapse is a rounding rather than a translation, is the robustness row this failure asks for. It costs one function and one run on committed data. It must be **registered in its own document before it is run**, beside this failure rather than instead of it, and both rows reported — otherwise it is the seventh free parameter arriving in the costume of a fix. REG-010's, not this one's.

## 5 · The registered predictions, scored

| prediction | registered claim | verdict |
|---|---|---|
| **P1** | Ψ > 0.50 under `R_MID`, in **both cycles separately** | **HOLDS** |
| **P2** | Ψ < 0.997 under `R_MID`, with 0.997 **outside** the clustered interval | **HOLDS** |
| **P3** | Ψ_band within five points of Ψ under `R_MID` | **FAILS** |
| **P4** | `R_MIN` and `R_WEIGHT` land on the same side of 0.50 as `R_MID` | **HOLDS** |
*Every number in this table is DISCLOSED δ, not the economic δ — paper III §4.7's weak joint, unmeasured, and the slack in every row. `R_WEIGHT` is amount-backed on both tags in 273 of 683 pairs (0.400); on the other 410 it is `R_MID` under another name.*

**P4 holds pooled, and the pooled verdict hides a cell — so here it is.** Under `R_MIN` in 2014-15, Ψ = 0.4939 with a clustered interval [0.4318, 0.5551] — which straddles 0.50. That is not a direction flip, which is what P4 was written to catch and what §9 says would be the larger finding; it is a cell the data does not resolve. `R_MIN` is the rule §6 refused as primary because it heaps hardest, and it carries the smallest admissible sample (533 of 683 pooled, against 665 under `R_MID`) on the fewest distinct points (199 against 428). Reported here rather than left for a reader to compute from §2.

## 6 · §12's stopping rule, applied

**Ψ = 0.6586 and Ψ_rect(α̂) = 0.9980 disagree**: Ψ_rect(α̂) falls outside Ψ's clustered interval [0.6211, 0.6964], by 0.339. §12 says the difference is attributed by S, by the distinct-pair columns and by Ψ_rect(α̂), never by narration. Attributed:

- **The recognition rate is not doing the work, and this is the row that says so.** Holding the manuscript's rectangle fixed and moving α from 0.35 to α̂ = 0.408 moves the rectangle's answer by 0.0007. That is 0.2% of the gap. Without Ψ_rect(α̂) this sentence could not be written, and the gap would have been attributable to whichever channel a reader preferred.
- **The support is wrong, and S measures it rather than arguing it.** S = 0.1391 under `R_MID`: 95 of 683 disclosed pairs fall inside L₀ ∈ [10, 40] × L₁ ∈ [3, 20]. **86.1% of the disclosure lives outside the rectangle the manuscript integrates over.**
- **The measure is not uniform and not a product.** 428 distinct pairs carry 665 admissible rows, with a modal pair share of 0.026; the two coordinates are chosen by one management on one page, and §4.4 sweeps them independently.

**What this attribution does NOT do is split the last two.** The rate channel is ruled out quantitatively; support and measure jointly carry the remaining 0.339, and this design does not decompose them — Q1 registered that all three channels would be computed and printed together, not that the last two would be separated. Saying which of support or measure carries more would need a fourth quantity nobody registered, and F10 is why it is not being invented here.

**Stated positively, which is what the paper needs:** at the measured recognition rate, the first rung of §4.4's ladder rises in **65.9% of the firm-years that disclose both lives** (665 admissible pairs across 577 firms), in both cycles separately (63.3% and 68.2%). The 99.7 % is a property of an asserted rectangle under a uniform product measure, not of the disclosure — and the direction the manuscript claims survives; only the magnitude does not.

No free parameter was introduced to reconcile Ψ with 99.7 %. F10 asserts the seventh refusal, and it passed.

## 7 · What this does not measure

**Every quantity above is DISCLOSED δ, not the economic δ.** Ψ, A, S, Ψ_band, and every recovery number `RESULT-P0` printed, are computed from the life a filing DISCLOSES. Paper III §4.7's weak joint is the gap between that and the rate at which the asset actually declines; REG-009 §10 says this registration does not measure it, and it does not. Every number here is an upper bound in that sense.

This run did not re-test §5.1's lag gradient, did not read φ per firm, did not run the industry-median variant, did not quote a price for §7.5's property-impairing universe, and did not touch σ. No zip was opened, no network module was imported, and both record files were checked by digest before they were read.
