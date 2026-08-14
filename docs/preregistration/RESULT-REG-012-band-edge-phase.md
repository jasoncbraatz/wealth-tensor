# RESULT · REG-012 — the band count's edge-phase question, answered as a description of the heap
*wealthTensor-38 · 2026-08-14 · registered alone in `REG-012-band-count-edge-phase.md` (`ba59370`);
this instrument did not exist at that commit. Instrument: `scripts/reg012_band_edge_phase.py`. Full
output: `RESULT-REG-012-band-edge-phase-run.log`. Table: `data/reg-012-band-edge-phase.json`. Guard:
`tests/test_reg012_band_edge_phase.py`. 13 severe checks, 0 definitional, 0 vacuous.*

---

## 0 · What was asked, and the two things wrong with how it was asked

State Machine card `1217494219393416` asked whether the band count of
`RESULT-REG-009-band-count-filled` has the edge-placement sensitivity Ψ_band has — whether a shift of
D3's bin edges would move events across a boundary. **The question is real and it is answered below.
The premise the card gave for it and the instrument the card proposed for it were both defective, and
both were established by reading, before anything was computed.** REG-012 §§1–2 record them; they are
restated here because a result document that omits why its measurement differs from the one it was
asked for has hidden the finding in the registration.

**Defect one — the premise counted another population.** The card's *"55.7 % of disclosed lives are
integers sitting exactly on a left edge"* is Ψ_band's statistic.
`CONSTRUCTION-REG-010-edge-convention.md` §C2 states the population in the same sentence that reports
the number: *"Of the 4098 lives entering Ψ_band across two tags and three interval rules"* — and
683 pairs × 2 tags × 3 rules = 4098 exactly. The band count's unit is an **event**, not a life; its
tag is the property tag alone; its rule is `R_MID` alone; each event contributes one life, picked
from up to nine cycles. **Four boundaries, and one number was carried across all four.**

That is the failure mode `REG-010-p3-half-integer-banding.md` §1 was written to stop — *"the
population is resolved from the cited document's own instrument, never from the sentence that cites
it"* — recorded there after `HANDOFF.md` cited §4's tee-up and pointed the run at the filled 133
(State Machine `1217494028527267`). The card was written the same day, cites the same tee-up, and
crosses the same boundary in the other direction. **A rule stated inside a registration protects that
registration and nothing else.**

**Defect two — the proposed statistic could not discriminate.** The card proposed *"how much of the
modal band's mass sits within w/2 of an edge."* For a half-open band `[b·w, (b+1)·w)` and any `v` in
it, `min(v − b·w, (b+1)·w − v) ≤ w/2`. **The answer is 1.000 for every band of every sample.** It
would have been computed, reported as a description of the heap, and discriminated nothing — the
green number that reads as coverage.

Both defects are repaired rather than filed (charter §2, REPLACE): the population is taken from the
cited document's own instrument, and the statistic is replaced by one that is not satisfiable by
construction.

## 1 · The population, and how it is known to be the right one

The cited document's instrument is `scripts/reg009_band_count_filled.py`; its committed table is
`data/reg-009-band-count-filled.json`. This run reproduces that table's registered row before
describing anything behind it: **133 events joinable, in 17 occupied bins, and the whole `R_MID|near`
row vector band for band** (P4, P4b). The run stops if any of it disagrees.

**The lives are taken from the count's own selection path, not from one retyped beside it.**
`reg009_band_count.py` gains one helper, `selected_lives`, returning the (cycle, value) pair
`bands_for` already computed inside its loop; `bands_for` now consumes it, so the repository holds
exactly one selection path and a divergence between the count and its description is impossible
rather than merely unlikely. **The refactor is behaviour-preserving and the published tables are the
proof:** both committed instruments were re-run in a scratch copy of the tree and their artifacts
compared **byte-identical** — `reg-009-band-count.json` at `6aa58d63`, `reg-009-band-count-filled.json`
at `6c86b96c`, on a different interpreter and a different machine from the ones that wrote them.
P2b then re-bins the lifted values and rebuilds the cited row exactly, which is the second, independent
way of knowing these are the values the published table was built from.

**The fractional parts are re-read, not rounded** (H3). Each value is taken through its own shortest
round-tripping decimal, and every one of the 133 round-trips exactly. Binary subtraction is avoided
deliberately: `4.3 − 4` is `0.2999999999999998` in floating point, and a histogram built on that
would report hundreds of distinct fractional values where the disclosure has a handful — an artefact
of the arithmetic, presented as a property of the sample.

## 2 · The heap

| | |
|---|---|
| population | **133 events**, one disclosed property life each |
| lives sitting exactly on a left edge | **84 — 63.16 %** |
| distinct fractional values present | **4** |
| modal fractional value | **0**, at 63.16 % |

| fractional part | events | share |
|---|---|---|
| 0 *(the modal value — on a left edge)* | 84 | 0.6316 |
| 1/4 | 9 | 0.0677 |
| 1/2 | 35 | 0.2632 |
| 3/4 | 5 | 0.0376 |

**The card's premise was directionally right and numerically another population's.** This sample's
edge mass is **63.16 %**, not the 55.71 % the card imported — 7.45 points apart, and the two numbers
are not estimates of one quantity that happened to differ. They count different things. Had the
measurement been skipped and the 55.7 % quoted for this population, the sentence would have been
wrong about a number that was available.

**And the disclosure is coarser than the band count's width suggests.** Every one of the 133 lives
lands on a quarter-year: the sample takes **four** fractional values out of a continuum. A band of
1.00 year is being drawn on a variable that moves in steps of 0.25.

## 3 · Phase rigidity — and why 0.25 of the circle is not 0.25 of an argument

Under an edge phase `s ∈ [0, 1)` the bin index is `floor(v) − [frac(v) < s]`, so the grouping the
bins induce — which events share a bin, ignoring which bin — is piecewise constant in `s`, with
breakpoints at the four fractional values. The phase axis therefore has **4 constant pieces**, and
the measure of phases whose grouping is identical to the registered one is one quarter of the circle:
**0.2500**.

**That quarter is entirely the trivial one.** The single grouping-preserving interval is **(3/4, 1]**
— every phase larger than the largest fractional value present, where the whole heap moves down one
bin together and the grouping is preserved by relabelling. E4-blind asserts that this holds for *any*
sample whatsoever, so that interval carries no information about this one. Reported apart, as the
registration required: the measure of grouping-preserving phases strictly below the largest
fractional value present is **0.0000 — exactly zero**.

**There is no non-trivial edge placement under which these 133 events group as they do now.** Move
the edges by any amount from just above 0 to 3/4 of a year and the partition changes.

## 4 · The verdict, in the branch's own registered words

**Branch F — FRAGILE**, as registered in REG-012 §6.

The card's worry is a live one for this population. The band count's placement of events into bands
depends on an edge convention that D3 fixed for reasons having nothing to do with this sample, and
the sample gives that convention no support: 63.16 % of its lives sit exactly on a left edge, where
an edge is a decision rather than an observation, and no non-trivial phase reproduces the grouping.

**And Branch F does not license the measurement it makes tempting.**
`CONSTRUCTION-REG-009-coverage-fill.md` R5 — *"No band edge, band width, floor, tag or interval rule
is re-chosen in response to the number"* — forbids re-edging the band count and re-reading its floor,
and it forbids it whether the heap turns out rigid or fragile. A fragile answer is a **disclosure
written beside the count**, not a permit to recount. Registered before the number existed; honoured
now that it is known; and the honouring is worth exactly as much as the fact that the number came out
on the side that makes the refusal cost something.

**What this result does not do**, each registered in §6 before the run:

- It reports **no count of bands** and reaches **no verdict on §7.5's decision rule**. That refusal is
  asserted as an *absence* — `A1` refuses the instrument if it names any of the ways a band count is
  read in this repository, and the test suite asserts the same of this document. An absence is the
  only assertion a short list cannot satisfy.
- It does **not** touch the straddle `RESULT-REG-009-band-count-filled` §4 reports — registered
  reading gives one clearing band, every other reading of the same 133 gives two. That straddle is
  made by the **nearest-cycle tie-break, which decides 50 of these 133 events**: a different
  parameter, of a different kind, and edge phase cannot reach it. **The two sensitivities are
  separate and this document establishes only the second.**
- It does **not** support §4.7's within-band design, promote `R_MIN` or any pick mode, or weaken the
  δ qualifier. Every life above is a **disclosed** life.
- No sentence of the manuscript changes on this result, as §6 registered in advance.

## 5 · What this cannot do

It cannot say which events would move between which bands under a particular shift — that is a
re-edged band count, and it is refused rather than merely unperformed. It cannot reach the 18 events
the coverage fill leaves unjoined, which have no life and therefore no fractional part. It says
nothing about Ψ_band, whose population is the one §0 is about. And it does not price REG-011's
universe, which §7.5 put out of scope and which stays there.
