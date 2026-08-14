# REGISTRATION · the coverage fill, declared before the count exists
*wealthTensor-32 · 2026-08-14 · registered in its own commit, ahead of the commit that
carries the instrument and the number. `git log --follow` on this file is the ordering.*

This is not a new registration of REG-009, which is **closed**. §7.5 registered the band
count's procedure and its decision rule; `RESULT-REG-009-band-count` §3 named the coverage
fill, priced it, and stated why it is decision-relevant rather than tidy. What follows is
the construction detail that fill requires and that neither document could state before the
fill was attempted — written down here **before the filled count was computed**, because a
probe that both measures a quantity and chooses the rule that produces it is the shape
SOURCE-001 §4c spent a session unwinding.

---

## R1 · The cycle set: §3b's window, translated by whole years, and nothing else

SOURCE-001 §3b measures two cycles, `2014-10-31 … 2015-09-30` and `2022-10-31 …
2023-09-30`, each read from six consecutive FSN notes zips so that all twelve fiscal-year-
end months have their whole filing season inside the instrument. **The fill invents no
window.** It runs the seven intervening cycles, each of which is the committed 2014-15
window translated forward by a whole number of years:

| cycle | window | zips |
|---|---|---|
| 2015-16 … 2021-22 | `YYYY-10-31 … YYYY+1-09-30`, YYYY = 2015 … 2021 | `YYYYq4 … YYYY+2q1` |

A guard in the instrument (H2) refuses the run if any filled window is not the committed
one translated by whole years, and its witness is a window displaced by a single day. The
nine cycles are then `2014-15 … 2022-23`, contiguous in the sense §3b's shape allows.

**And that shape leaves a hole, which is registered here rather than closed.** Consecutive
windows abut at 09-30 / 10-31, so fiscal-year ends falling on **1–30 October** lie in no
window of the series, in any year. Widening the window to close it would be a new
parameter chosen after the fact. The hole is therefore **measured and reported** — the
count of panel firm-years inside it, and how many of them belong to a firm owning a tier-0
property event — and left open. *A measurement that cannot represent the answer is not
evidence of absence*, and this is the fill's own version of that rule, declared before its
size was known.

## R2 · What the fill may move, and what it may not

The fill raises **the joinable column only**. It does not touch the 151 tier-0 property
events, the 98 firms, REG-006's crawl, the 683 pairs, Ψ, or any registered REG-009 number.
H6 refuses the run if `events_total` moves.

## R3 · The count is reported BESIDE `-31`'s, never instead of it

The committed `data/reg-009-band-count.json` and every assertion in
`tests/test_reg009_band_count.py` stand untouched. The filled run writes its own artifact,
`data/reg-009-band-count-filled.json`, whose first block **reproduces `-31`'s two-cycle
count from the same committed inputs** — 151 events, 110 joinable, one band clearing — and
whose second block carries the filled population. H3 refuses the run if the reproduction
disagrees, which is `-31`'s own rule (*reproduce the published table before extending it*)
turned on `-31`.

*(The handoff's definition of done names `data/reg-009-band-count.json` as the artifact to
recompute. Its own next sentence says the new row goes beside `-31`'s and never instead of
it, and STEP 3 of the session brief repeats that. Overwriting the committed file would
replace `-31`'s row and silently flip four assertions in a committed test. **Beside wins**;
the handoff is a status report and cannot amend a ruling.)*

## R4 · The decomposition, declared before it is read

A ninefold cycle set does not only add events to the join. `pick_cycle`'s primary mode is
*the cycle nearest the event's own fiscal year*, so a firm that already had a disclosed
life may now have a **nearer** one, and an event already binned may move band without ever
having been unjoinable. A filled count reported as a single number would hide that. The
run therefore decomposes the change into three disjoint parts and prints all three:

1. **newly joinable** — events with no property life in either original cycle that have one now;
2. **moved** — events joinable before, placed in a different band now because a nearer cycle supplies the life;
3. **unchanged** — events joinable before and in the same band.

**Part 2 is not a bug to be suppressed and not a result to be celebrated. It is the price
of the fill**, and it is reported whether it is large or small, because a count whose
inputs were re-chosen is a claim about the choosing rule as much as about the sample —
`-31`'s finding 16, applied to `-31`'s successor.

## R5 · The decision rule is still §7.5's, and it is not moved here

> *"Only if fewer than two bands clear does the expensive half arrive."*

Under the primary interval rule `R_MID` and the primary cycle pick. **`R_MIN` is not
promoted to primary under any outcome of this run** — §6 refuses it because it scores best,
and it is now also the rule under which §4.7's design survives, which makes the temptation
concrete rather than theoretical. If the filled count under `R_MID` reaches two, the design
is supported on the registered rule; if it does not, it is not; and if the two rules
disagree the disagreement is reported exactly as `-31` reported it. **No band edge, band
width, floor, tag or interval rule is re-chosen in response to the number.**

## R6 · What this fill cannot do

It cannot make a disclosed life an economic one: every band remains a band of the
**disclosed** life, and the δ qualifier stands on every number below it. It cannot reach a
firm that discloses no canonical property life in any of the nine cycles. It cannot reach
the 1–30 October hole of R1. And it does not price REG-011's universe, which §7.5 put out
of scope and which stays there.
