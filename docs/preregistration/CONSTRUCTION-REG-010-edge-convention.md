# REGISTRATION · REG-010's edge convention, and the band the shift creates
*wealthTensor-36 · 2026-08-14 · registered in its own commit, after `REG-010-p3-half-integer-banding.md`
and before the commit that carries the instrument and the number. `git log --follow` on both files
is the ordering. No instrument for this measurement exists on disk at this commit either.*

This is the construction detail REG-010 requires and that neither `RESULT-REG-009` §4 nor the
registration could state before the shift was examined. It is written down here **before Ψ_band′
was computed**, because a probe that both measures a quantity and chooses the convention that
produces it is the shape `SOURCE-001` §4c spent a session unwinding, and `-32` set the precedent
for writing the construction down separately.

**What was measured before this file existed, and why that is not spending the answer.** Three
properties of the *committed lives* were read off the two SHA-pinned files with no Ψ computed and
no instrument written: how many lives are integers, how many are half-integers, and how many fall
below w/2. Those are properties of the **population and the operator**, not of the statistic — they
say which conventions are *reachable*, exactly as `-32` established that the nearest-cycle tie was
reachable at nine cycles before it ran the count. **None of them is a step toward the verdict**, and
the verdict's two branches were fixed in the previous commit before any of them was read.
`|Ψ_band′ − Ψ|` does not exist anywhere at this commit.

---

## C1 · The shift is DERIVED from the lifted rule, in both directions, and typed nowhere

`reg009_ladder_inputs.lift_band_rule()` extracts three pieces from
`reg009_p0_lifetime_values.py` by shape and aborts if they change: the bin index `int(v // w)` and
the two edges `b * w` and `(b + 1) * w`. Call them `binner`, `lo`, `hi`. D3's collapse is
`mid(v, w) = (lo(b, w) + hi(b, w)) / 2` at `b = binner(v, w)`.

REG-010's collapse is the **same three pieces with the argument advanced by w/2 and the edges
retarded by w/2**:

```
b       = binner(v + w/2, w)
edges   = [ lo(b, w) - w/2 ,  hi(b, w) - w/2 )
mid′(v) = ( (lo(b,w) - w/2) + (hi(b,w) - w/2) ) / 2
```

Nothing is retyped: the floor, the half-openness and the edge arithmetic are all D3's, and a change
to D3's shape propagates into REG-010 or aborts both. **A source-text guard refuses REG-010's
instrument if `int((v + 0.5) // 1)`, `+ 0.5`-style bin arithmetic, or any literal bin edge appears
in it** — the same discipline `lift_band_rule()` was built for, banked as
`2026-08-13-robustness-row-collapses-values-band-midpoint`, and the reason it applies here is that
the failure mode is identical: a robustness row about a collapse can quietly become a statistic
about the row's own idea of a band.

## C2 · The half-openness is INHERITED, not chosen — and it decides 715 lives

D3's bins are half-open on the left, `[b·w, (b+1)·w)`. The shifted bins inherit that direction
because they inherit `binner`. **REG-010 therefore does not choose a tie-break; it declines to
introduce one.** The convention is a consequence of the lift, and the alternative would have had to
be typed in by hand — which the guard in C1 forbids.

What the inheritance decides is not small, and it is named here so it cannot be discovered later:

| where a life sits | under D3's edges | under REG-010's edges |
|---|---|---|
| exactly **integer** | on a left edge — **2283 lives, 55.71 %** | at the bin **centre**, displacement **zero** |
| exactly **half-integer** | at the bin centre | on a left edge — **715 lives, 17.45 %** |
| neither | interior | interior |

*Of the 4098 lives entering Ψ_band across two tags and three interval rules. The 55.71 % reproduces
`RESULT-REG-009` §4's published 55.7 %, which is how this file knows it is reading Ψ's population
and not another one.*

A life on a left edge is carried **up** by w/2 — the maximum displacement the operator can inflict,
and always in the same direction. So the shift does exactly what §4 asked of it for the integer
heap, and the honest description of the rest is C3's.

## C3 · The heap is RELOCATED, not removed, and *relocated* is the verb the result document uses

§4's tee-up says the shift makes the collapse *"a rounding rather than a translation."* **That is
true of 55.71 % of the lives and false of 17.45 % of them**, and the second heap is not a rounding
error in the tee-up — it is a real feature of disclosed useful lives, which cluster on half-years as
well as on years. Registered consequences:

- **Neither banding is the clean one.** D3 translates a 55.71 % heap; REG-010 translates a 17.45 %
  heap. The pair of rows brackets the operator's contribution; **neither row is the operator-free
  answer, and the result document may not describe either as one.**
- The run **reports the mean and maximum absolute displacement under each banding**, so that the
  bracket is quantified rather than asserted. Those quantities are declared here and computed there.
- If Ψ_band′ moves less than Ψ_band did, the registration's Branch B governs the reading of it, and
  **the smaller surviving heap is the reason to expect it rather than a discovery to report as
  one.** Predicting the direction here is what stops it being spent as evidence later.

## C4 · The mirror convention: computed, reported beside, never used to choose

The mirror of C2's inheritance sends a half-integer **down** rather than up. It is derived from the
same lifted `binner` by reflection, so it too types nothing:

```
b_mirror = -binner( -(v - w/2), w )
```

It exists for one purpose — **to measure what the inherited convention is worth**, on `-32`'s H10
precedent, which built the reversed nine-cycle world for exactly this reason and never chose an
answer with it. **The registered reading is C2's inherited one under every outcome.** If the mirror
disagrees with it across P3's five points, that disagreement is *reported as the finding* — a
statistic whose verdict turns on the direction of a half-open interval is a statistic with a
sensitivity nobody registered — and the registered reading still stands. **The mirror is never
promoted, and a session that finds itself preferring it has found the seventh free parameter.**

## C5 · The band the shift creates, and which the estimator cannot consume

δ enters the model as **`d = 1.0 / L`**. D3's leftmost band is `[0, w)` with midpoint `w/2 = 0.5`,
which is a legal life. **REG-010's leftmost band is `[−w/2, +w/2)` and its midpoint is `0`, which is
not** — `d` becomes infinite. This is a value the *operator* can produce that the *estimator* cannot
take, which is the lesson `2026-08-12-ask-every-estimator-registration-values-can` read from the
other side, and it is created by the shift rather than inherited from D3.

**Seven of the 4098 lives fall below w/2** and collapse to zero under the registered convention;
under the mirror, **two more** — the lives at exactly 0.5 — join them. Declared before the run:

- **The instrument does not silently drop them.** `adm = (d < α)` is false for an infinite `d`, so a
  zero-collapsed life would leave the admissible set with no line of output saying so, and Ψ_band′
  would then be computed on a denominator Ψ_band was not — `-31`'s tell, aimed at the denominator,
  arriving before the number for once.
- **The run counts every zero-collapsed life and asks the one question that matters: would any of
  them have been admissible otherwise?** Admissibility needs `1/L < α̂ = 0.408`, i.e. `L > 2.45`
  years, and every zero-collapsing life is below 0.5 — so the expected answer is **no**, and the
  guard is expected to pass with real subjects rather than vacuously.
- **If the answer is ever yes, the run REFUSES.** It does not exclude the life, and it does not
  widen a band to keep it: either would be a rule re-chosen in response to the sample. A refusal is
  reported to a future session as an unrun measurement, which is a thing this programme knows how to
  carry; a silent exclusion is not.

## C6 · What the instrument must refuse

Registered as a checklist so the instrument is written to it rather than around it:

1. **Reproduce before extending.** Ψ, the 683 pairs, the 428 distinct pairs and the committed
   Ψ_band = 0.7236 are recomputed from the two pinned files and compared to the committed record;
   any disagreement aborts. `-31`'s rule, turned on `-30`.
2. **The lift, or nothing.** If `lift_band_rule()` cannot find D3's index or edges, REG-010 aborts
   rather than falling back to a typed rule.
3. **No literal bin arithmetic in REG-010's own source** (C1), witnessed by the guard firing on a
   planted literal.
4. **No new source, no network, no zip, no second band width, no swept offset.**
5. **The zero band is examined, not assumed** (C5), and a would-have-been-admissible zero-collapsed
   life aborts the run.
6. **Both rows and both conventions are printed in every table that reports either**, each carrying
   the disclosed-versus-economic δ qualifier, which stands on all of REG-010 exactly as it stands on
   §4.
7. **Nothing is written except REG-010's own artifact.** No committed file under `data/` is
   overwritten — beside, never instead of.
