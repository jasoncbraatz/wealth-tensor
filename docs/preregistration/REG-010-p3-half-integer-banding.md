# REGISTRATION · REG-010 — the half-integer-edged banding, and what it is allowed to decide
*wealthTensor-36 · 2026-08-14 · registered in its own commit, ahead of the commit that carries
the construction detail and ahead of the commit that carries the instrument and the number.
`git log --follow` on this file is the ordering, on `CONSTRUCTION-REG-009-coverage-fill.md`'s
precedent. No instrument for this measurement exists on disk at this commit.*

---

## 0 · What this registers, and the one thing it is forbidden to do

`RESULT-REG-009` §4 reported that **P3 FAILS**: every δ collapsed to its D3 band midpoint moved Ψ
by 0.0650 against a registered tolerance of five points. That section then attached its own repair,
per charter §2, and priced it before it could become a rescue:

> *"A second banding whose bin edges fall on half-integers, so the heap sits at a bin's centre and
> the collapse is a rounding rather than a translation, is the robustness row this failure asks
> for. It costs one function and one run on committed data. It must be **registered in its own
> document before it is run**, beside this failure rather than instead of it, and both rows
> reported — otherwise it is the seventh free parameter arriving in the costume of a fix."*

This is that document. It is written before the function exists.

**P3 failed as registered and REG-010 does not re-score it.** REG-009 is **closed**; its
predictions are scored; §4's verdict stands whatever this run returns. Nothing here moves a
registered number, renumbers a section, or reopens a prediction. REG-010 asks a strictly narrower
question than P3 did, and §3 below pre-commits what each answer is permitted to mean — including,
and especially, the answer that would look like good news.

## 1 · The population, stated explicitly because a handoff got it wrong

**REG-010 runs on Ψ's population: the 683 disclosed pairs** carried by the two SHA-pinned cycle
files `data/reg-009-p0-lives-2015.json` and `data/reg-009-p0-lives-2023.json`, loaded by
`reg009_ladder_inputs.load_population`, contributing 4098 lives across three interval rules and two
tags. Unit: the firm-year **pair** (`PropertyPlantAndEquipmentUsefulLife`,
`FiniteLivedIntangibleAssetUsefulLife`). This is the population P3 was scored on and the only
population on which a Ψ_band row means anything.

**It is NOT the band-count population.** `RESULT-REG-009-band-count-filled`'s **133 of 151** are
tier-0 property *events* joined across nine cycles by a different instrument
(`reg009_band_count_filled`), on one tag rather than two, answering a different question (how many
bands hold at least 30). `chronological()` builds that join and has no path to Ψ. The two objects
share the word *band* and nothing else.

This paragraph exists because `HANDOFF.md` §3 item 1 cited §4's tee-up **and** directed the run at
the filled 133 — two populations in one instruction, the citation right and the population drifted.
It is recorded on State Machine `1217494028527267`. **A future session that finds this registration
and that handoff in the same sitting should believe this file**: the population is resolved from the
cited document's own instrument, never from the sentence that cites it.

**And re-edging the band count is not merely the wrong object — it is a registered refusal.**
`CONSTRUCTION-REG-009-coverage-fill.md` R5: *"No band edge, band width, floor, tag or interval rule
is re-chosen in response to the number."* The band count's entire content is a threshold reading, so
shifting its edges and re-reading the floor of 30 spends that refusal. Ψ_band is exempt from the
objection for one reason and it is the reason this registration is admissible at all: **it is a
robustness row reported beside a failure, never a threshold re-read.** The separate, legitimate
half-integer question for the band count is carded at `1217494219393416` and is not run here.

## 2 · The measurement

One statistic, computed twice on the same 683 pairs under the primary interval rule `R_MID`:

| row | banding | status |
|---|---|---|
| **Ψ_band** | D3's own bins, `[b·w, (b+1)·w)`, lifted at run time | **committed, unchanged** — `RESULT-REG-009` §4 |
| **Ψ_band′** | the same rule with its edges shifted by **w/2** | this registration's row |

`w` is D3's committed 1.00-year width and is not re-chosen. **No second band width is tried**, F10's
refusal being the reason §4 gave for not trying one after P3 failed. The shift is the single new
parameter, it is fixed at w/2 by the tee-up's own words (*"bin edges fall on half-integers"*), and
it is not swept.

**The shifted rule is DERIVED FROM the lifted rule, not retyped.** `lift_band_rule()` already
refuses `reg009_ladder_inputs` if D3's bin index or bin edges change shape; REG-010's instrument
must obtain its binner and edges from that same lift and apply the shift to them, so that a change
to D3 propagates rather than diverging silently. Retyping `int((v + 0.5) // 1)` anywhere would make
Ψ_band′ a statistic about REG-010's idea of a band, which is the exact defect
`lift_band_rule()` exists to prevent — banked as
`2026-08-13-robustness-row-collapses-values-band-midpoint`. A source-text guard refuses the
instrument if the shifted rule appears in it as a literal.

**Ψ, A, S, the four predictions and the pooled/per-cycle tables are recomputed by nothing here.**
Ψ_band′ is compared against the **committed** Ψ = 0.6586, which the instrument reproduces from the
same pinned files before it computes anything new, and refuses the run if it disagrees — `-31`'s
*reproduce the published table before extending it*, turned on `-30`.

## 3 · The decision rule, and both branches pre-committed

The comparison is `|Ψ_band′ − Ψ|` against P3's registered five points. **Both readings are written
down here, before the number, because only one of them is dangerous and it is the flattering one.**

**Branch A — `|Ψ_band′ − Ψ| ≥ 0.05`.** The failure is not an artefact of the collapse operator. P3's
verdict is unchanged and *better supported*: Ψ is sensitive to the granularity of the disclosure
under both edge placements, and §4's post-hoc observation about integers sitting on left edges is
demoted to *true but not load-bearing*. This is the outcome that costs nothing to report.

**Branch B — `|Ψ_band′ − Ψ| < 0.05`. P3 STILL FAILS, and this outcome is WORSE for Ψ than Branch A,
not better.** Registered now, in the branch's own words, so that it cannot be spent later:

- P3 was scored on the registered banding and it failed. A second banding that a session went and
  built *after* seeing the failure cannot un-score it. A control rescued after it fails is not a
  control — §4's sentence, and it applies to this document first.
- What Branch B would establish is that the registered statistic's verdict turns on **the edge
  placement of a nuisance parameter nobody registered**. Ψ_band and Ψ_band′ differ by w/2 of
  arbitrary offset and by nothing else. A statistic that answers a five-point question one way at
  offset 0 and the other way at offset w/2 is *more* granularity-dependent than one that fails at
  both, not less, and the honest report of Branch B is **"Ψ's sensitivity to the disclosure's
  granularity is larger than P3 measured, because it includes a dependence on where the bins are
  put."**
- **Under Branch B no sentence anywhere is softened, no verdict is amended, and REG-010's row does
  not enter any table that reports P3.** It is reported in this registration's result document,
  beside §4's failure, and §4 is not edited.

**Neither banding is promoted.** D3's remains primary because it is the one D3 priced and the one P3
was registered against. Ψ_band′ is a robustness row and never replaces Ψ_band in any table, under
any outcome. **The pair of rows is the deliverable** — the tee-up said *both rows reported*, and the
reason is that neither offset is privileged: together they bracket the operator's contribution,
which is a quantity the estate does not currently have and which a single row cannot supply.

**No band edge, width, floor, tag, interval rule, cycle or tolerance is re-chosen in response to the
number.** R5's sentence, restated here so REG-010 is bound by it too.

## 4 · What this may not move

The 683 pairs, the 428 distinct pairs, the 665 admissible rows, Ψ = 0.6586 and its clustered
interval, A, S, Ψ_rect and Ψ_rect(α̂), α̂, the verdicts on P1, P2, P3 and P4, REG-009's numbering,
the 151 tier-0 events, the 98 firms, the 110 and the 133 of the band counts, and every artifact
under `data/` that a committed test asserts against. The instrument refuses its own run if the
reproduced Ψ, pair count or distinct-pair count moves. REG-010 writes **one new artifact of its
own** and overwrites nothing — `-32`'s **beside, never instead of**, which is now this
programme's standing rule for a second reading of a committed measurement.

## 5 · The manuscript consequence, declared in advance: NONE

**Paper III does not carry Ψ_band, P3, 0.7236, or any granularity claim** — checked before this
registration was written, and stated here so the check cannot be re-run later against a number.
There is therefore **no manuscript edit under Branch A and none under Branch B**, and a session that
finishes REG-010 and finds itself drafting a sentence for paper III has found the seventh free
parameter putting its costume on. G-COACH-3 is evaluated across the session regardless, and its
delta is expected to be **exactly zero** because no manuscript file is opened for writing.

If a future registration wants Ψ_band in the manuscript, it registers *that* — with both rows and
the δ qualifier — and it does not inherit permission from this one.

## 6 · What this cannot do

It cannot make a disclosed life an economic one: Ψ, Ψ_band and Ψ_band′ are all computed from the
life a filing **discloses**, and the disclosed-versus-economic δ qualifier stands on every number
REG-010 produces, exactly as it stands on §4's. It cannot remove the heaping — §2 of the
construction document registers what the shift does to the heap, and *relocate* is the honest verb.
It cannot speak to the band count, to §7.5's floor, or to REG-011's universe. And it cannot tell
whether either banding is the *right* one, because there is no registered ground truth about the
granularity of a disclosed useful life and this design does not invent one.
