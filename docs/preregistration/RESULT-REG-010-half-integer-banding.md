# RESULT · REG-010 — the half-integer-edged banding, run beside P3's failure
*wealthTensor-36 · 2026-08-14 · the robustness row `RESULT-REG-009` §4 teed up and priced. Registered alone in `REG-010-p3-half-integer-banding.md` (`f61f75a`); construction registered alone in `CONSTRUCTION-REG-010-edge-convention.md` (`8d1245b`); the instrument existed at neither commit. Instrument: `scripts/reg010_half_integer_banding.py`. Full output: `RESULT-REG-010-half-integer-banding-run.log`. Table: `data/reg-010-half-integer-banding.json`. 25 severe checks, 0 definitional, 0 vacuous.*

---

## 0 · What ran, and against what

`RESULT-REG-009` §4 scored **P3 as FAILING** — Ψ_band = 0.7236 against Ψ = 0.6586, a difference of 0.0650 against a tolerance of five points registered before the number existed — and then observed, post-hoc and labelled as such, that D3's bins are half-open on the left and that 55.7 % of the lives entering Ψ_band are integers sitting exactly on a left edge. A midpoint collapse therefore *translates* a heaped disclosure by half a year rather than *rounding* it. §4 attached the repair rather than filing the objection: a second banding whose edges fall on half-integers, registered in its own document, run beside the failure and never instead of it.

This is that run. **P3 failed as registered and REG-010 does not re-score it.** REG-009 is closed; no registered number moves; §4's verdict is not amended below.

**The committed row was reproduced before it was extended** (G5): 683 pairs, Ψ = 0.6586466165, Ψ_band = 0.7236255572, 665 and 673 admissible rows, 428 and 178 distinct pairs, and an integer share of 0.5571010249 — the same 55.7 % §4 published, which is how the run knows it is reading Ψ's population and not another one. The run stops if any of them disagrees.

**The population is Ψ's 683 disclosed pairs, not the band count's filled 133.** The registration §1 says why at length: a handoff item cited §4's tee-up and directed the run at the band count's population, which is a different instrument on a different unit answering a different question — and re-edging *that* would additionally spend `CONSTRUCTION-REG-009-coverage-fill` R5's refusal to re-choose a band edge in response to a number. State Machine `1217494028527267`.

## 1 · The shift, and what it does to the heap

Both conventions are one-line reflections of D3's **lifted** midpoint. Nothing about a bin is typed in REG-010, and a source-text guard (G2a) refuses the instrument if a bin index is retyped in it:

```
shifted(v, w) = mid(v + w/2, w) - w/2        the registered convention
mirror(v, w)  = -shifted(-v, w)              priced, never chosen
```

| | D3's banding | REG-010's banding |
|---|---|---|
| bin edges at | the integers | the half-integers |
| lives sitting on a left edge | **2283 of 4098 — 55.71 %** | **715 of 4098 — 17.45 %** |
| what happens to an integer life | carried up by w/2 | **fixed point** — displacement zero |
| what happens to a half-integer life | fixed point | carried up by w/2 |
| mean displacement over the lives it collapses | **0.3162 y** | **0.1838 y** |
| maximum displacement | 0.5000 y | 0.5000 y |

**The shift does what §4 asked of it, and the honest verb for the rest is *relocate*.** The collapse becomes a rounding for the 55.71 % integer heap and a translation for a 17.45 % half-integer heap that D3 left alone: disclosed useful lives cluster on half-years as well as on years. **Neither banding is the operator-free one**, and this document does not describe either as one. `CONSTRUCTION-REG-010` §C3 registered that sentence, and registered the *direction* of the expected difference, before the run — so a smaller movement under the shift is the predicted consequence of a smaller surviving heap and is not reported here as a discovery.

## 2 · The row

**`R_MID`, primary, pooled and by cycle.** Ψ under the raw lives, under D3's banding, and under both edge conventions of REG-010's:

| subset | reading | n | admissible | A | Ψ | 95 % clustered | distinct pairs | modal share |
|---|---|---|---|---|---|---|---|---|
| pooled | raw | 683 | 665 | 0.9736 | **0.6586** | [0.6211, 0.6964] | 428 | 0.0256 |
| pooled | D3's banding (Ψ_band) | 683 | 673 | 0.9854 | **0.7236** | [0.6886, 0.7574] | 178 | 0.0431 |
| pooled | **half-integer edges — registered** | 683 | 664 | 0.9722 | **0.6536** | [0.6145, 0.6914] | 176 | 0.0557 |
| pooled | half-integer edges — mirror | 683 | 657 | 0.9619 | **0.6225** | [0.5827, 0.6606] | 176 | 0.0457 |
| 2014-15 | raw | 321 | 313 | 0.9751 | 0.6326 | [0.5793, 0.6859] | 249 | 0.0256 |
| 2014-15 | D3's banding | 321 | 316 | 0.9844 | 0.7120 | [0.6593, 0.7610] | 140 | 0.0411 |
| 2014-15 | half-integer — registered | 321 | 312 | 0.9720 | 0.6314 | [0.5784, 0.6845] | 133 | 0.0481 |
| 2014-15 | half-integer — mirror | 321 | 309 | 0.9626 | 0.6052 | [0.5513, 0.6613] | 133 | 0.0421 |
| 2022-23 | raw | 362 | 352 | 0.9724 | 0.6818 | [0.6335, 0.7314] | 251 | 0.0284 |
| 2022-23 | D3's banding | 362 | 357 | 0.9862 | 0.7339 | [0.6880, 0.7809] | 111 | 0.0532 |
| 2022-23 | half-integer — registered | 362 | 352 | 0.9724 | 0.6733 | [0.6243, 0.7239] | 114 | 0.0625 |
| 2022-23 | half-integer — mirror | 362 | 348 | 0.9613 | 0.6379 | [0.5879, 0.6884] | 109 | 0.0603 |
*Every row is a band of the DISCLOSED δ, not the economic δ — paper III §4.7's weak joint, unmeasured, and the slack in every row here as in §4's. The intervals are a fresh draw at wt088's lifted `SEED`; the point estimates are deterministic and are the quantities compared below.*

## 3 · The reading — Branch B, and it was written down first

| reading | \|Ψ_x − Ψ\| | inside P3's five points |
|---|---|---|
| D3's banding — **P3's registered subject** | **0.0650** | **no — P3 FAILS** |
| half-integer edges, registered convention | **0.0050** | yes |
| half-integer edges, mirror convention | **0.0361** | yes |

**This is the registration's Branch B, and the registration said in advance what it is allowed to mean.** Quoted from `f61f75a`, written before the instrument existed:

> *"P3 STILL FAILS, and this outcome is WORSE for Ψ than Branch A, not better. … What Branch B would establish is that the registered statistic's verdict turns on the edge placement of a nuisance parameter nobody registered. … Under Branch B no sentence anywhere is softened, no verdict is amended, and REG-010's row does not enter any table that reports P3."*

So: **P3 fails. §4 is not edited. Nothing is softened.** A control that failed on the banding it was registered against cannot be un-failed by a banding built after the failure was seen, and the thirteenfold drop from 0.0650 to 0.0050 is not a rescue — **it is the size of the problem.** Ψ_band and Ψ_band′ are the same statistic on the same 683 pairs at the same 1.00-year width, differing by w/2 of offset and by nothing else, and they land on opposite sides of P3's threshold. The tolerance is crossed by the offset alone.

**Had this branch not been registered in advance, the flattering reading was available and would have gone green.** Ψ_band′ = 0.6536 sits 0.0050 from Ψ; a session holding the tee-up and not the branch could have written *"the failure was an artefact of the translation; under the banding §4 itself asked for, Ψ moves half a point"* — and the registration, the ordering proof, the guards and the suite would all have passed over it. That sentence is exactly the seventh free parameter arriving in the costume of a fix, which is the thing §4 named when it teed the row up and refused to run it itself.

## 4 · The finding: the sensitivity is to DIRECTION, not to distance

The registered convention and its mirror **move every life by exactly the same distance** — G7a checks it pointwise over all 4098 lives, not on probe points — and they disagree on **exactly the 715 half-integer lives** and nowhere else (G7b). Their displacement profiles are identical: mean 0.1838 y, maximum 0.5000 y, 740 fixed points, 626 lives moved. The only difference is which way the half-integer heap goes: **495 up / 131 down** against **116 up / 510 down**.

**They give Ψ = 0.6536 and Ψ = 0.6225.**

That is **0.0311 of Ψ from the direction of a half-open interval**, with distance held exactly fixed — six times the whole difference between Ψ and the registered shifted reading, and it is bought by a convention that no registration in this programme ever had to name, because before REG-010 no banding in it had an edge a disclosed life could sit on other than the integers.

**This is the row §4 asked for, and it says more than §4 expected.** The quantity Ψ is sensitive to is not *how far* a collapse moves the disclosed lives — that is held fixed here — but *which way it moves the heap*. §4's post-hoc observation about translation-versus-rounding was pointing at a real mechanism and pointing at only half of it: the operator's magnitude is the half that was visible, and its direction is the half that moves the answer.

**The mirror is not promoted, under this outcome or any other.** `CONSTRUCTION-REG-010` C4 fixed that before the run, and the reason it matters is now concrete rather than theoretical: the mirror is the reading under which Ψ_band′ sits furthest from Ψ, which makes it the reading a session wanting P3's failure to look robust would reach for. It is reported beside the registered convention and it does not replace it.

## 5 · The band the shift creates, discharged

δ enters the model as `1/L`. D3's leftmost band is `[0, w)` with midpoint 0.5 — a legal life — while REG-010's is `[−w/2, +w/2)` with midpoint **0**, which is not: `1/0` is infinite and `adm = (δ < α̂)` is then silently **false**. C5 registered the hazard, the handling and the refusal before the run.

| convention | lives collapsed to zero | of those, admissible on their own raw value |
|---|---|---|
| D3's banding | **0** | 0 |
| half-integer, registered | **7** | **0** |
| half-integer, mirror | **9** | **0** |

Admissibility needs `1/L < α̂ = 0.408`, i.e. `L > 2.45` years; every zero-collapsing life is below 0.50 years. **The guard passed with real subjects rather than vacuously** — there were sixteen lives to examine across the two conventions — and no pair left the admissible set unannounced. The admissible counts still move between readings (665 / 673 / 664 / 657) because re-banding moves short lives across the 2.45-year line, which is ordinary and was already true of the committed Ψ-versus-Ψ_band comparison; **none of that movement is the zero band**, and C5 exists so that sentence is a measurement rather than an assumption.

Had any zero-collapsed life been admissible, the registered handling was **refuse the run** — not exclude the life, not widen a band, either of which is a rule re-chosen in response to the sample.

## 6 · What this does not measure

It does not re-score P3, which failed and stays failed. It does not measure the economic δ: Ψ, Ψ_band, Ψ_band′ and the mirror are all computed from the life a filing **discloses**, and the disclosed-versus-economic qualifier stands on every number above. It does not identify a *correct* banding, because there is no registered ground truth about the granularity of a disclosed useful life and this design does not invent one — the pair of rows brackets the operator's contribution and that bracket is the deliverable. It does not touch the band count, §7.5's floor of 30, or REG-011's universe. It does not sweep the offset: w/2 is fixed by §4's own words and no second value was tried. And it does not move Ψ, A, S, α̂, the 683 pairs, the verdicts on P1, P2 or P4, or any artifact REG-009 committed — G9 digests all fourteen `reg-009-*.json` files before and after the run and refuses if one of them changed.
