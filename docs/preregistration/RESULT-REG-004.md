# RESULT-REG-004 · the closed form survives, and the ordering was never about the shape

- **Registration:** `REG-004-p3-age-dependent-recognition.md`, commit **5160f51**, 2026-08-12 —
  committed and pushed before a line of `wt090` was written.
- **Instrument:** `scripts/wt090_age_dependent_alpha.py`. **14 severe · 0 definitional · 0 vacuous.**
  Inputs: `data/pre-002-events.json` and RESULT-REG-003's fitted `k̂ = 1.21`, `q̂ = 0.921342`.
  Nothing new was collected.
- **Verdict, the derivation:** **F1, F2, F3, F4 all pass.** `R = (1 − φ)(Π(1/(1 − δ)) − 1)`.
- **Verdict, the ladders:** **N1 · M1 on the tabulated ladder and M3 on the disclosed rectangle ·
  C2 · D1 · E2 · S2.**

---

## 1 · The closed form survives, and it survives as a transform

Let a gap cohort created at time *s* be recognised after a lag `T ≥ 1` periods, so it sits in the
gap over `s+1 … s+T`. The gap is then an age-convolution of the flow with the lag's survival
function, and with `E(t) = E₀(1 − δ)ᵗ` and `z = 1/(1 − δ)`,

> **R = (1 − φ) · δ · Σ_{a ≥ 1} zᵃ P(T ≥ a) = (1 − φ) · ( Π(z) − 1 )**,  **Π(z) = E[z^T]**

because `Σ_{a≥1} zᵃP(T ≥ a) = z(Π(z) − 1)/(z − 1)` and `z − 1 = δ/(1 − δ)`. The generating function
is evaluated **outside the unit disc**, so it is a discrete moment generating function and not a
Laplace transform — which is the whole reason it can fail to exist.

**The published form is the geometric case and nothing else.** With `T` geometric at rate α on
{1, 2, …}, `Π(z) = αz/(1 − (1 − α)z)`, which at `z = 1/(1 − δ)` is `α/(α − δ)`, giving
`R = (1 − φ)δ/(α − δ)` exactly. **F1** reproduces this to **2.1 × 10⁻¹³** over the tabulated ladder
crossed with three recognition rates.

**And the filter agrees.** **F2** runs an age-structured simulation — the gap carried as cohorts,
each aged one period and multiplied by its own `P(T ≥ a+1)/P(T ≥ a)`, no closed form anywhere in
the loop — for 400 periods at the fitted lag distribution. Worst departure from the registered form
**1.9 × 10⁻¹³**, against §4.3's published transient bound of 2 × 10⁻⁴. **F3** makes that
non-vacuous: the same simulation rejects the naive substitution `α ← 1/E[T]` at up to
**2.0 × 10⁻³**, ten times the bound.

**φ is untouched.** **F4**: `R(φ)/R(0) = (1 − φ)` to **0.0 exactly**, at every φ on a tenth-grid.
Every statement in the paper that depends only on the `(1 − φ)` channel is unaffected by anything
in this file.

**The equivalent statement, and the one that is easier to misuse.** Define
`α_eff(δ) = δ·Π(z)/(Π(z) − 1)` and the published form returns verbatim, `R = (1 − φ)δ/(α_eff − δ)`.
**α_eff is not a parameter. It is a function of δ**, and §5 measures how much of a function.

## 2 · The existence condition is a statement about the tail, not about the mean · **D1**

`R` is finite exactly when `Π(1/(1 − δ)) < ∞`, i.e. when the lag's generating function has radius
of convergence above `1/(1 − δ)`. For a geometric lag that radius is `1/(1 − α)`, which reproduces
**α > δ**. For the fitted discrete Weibull the survival `q^(aᵏ)` with `k̂ = 1.21 > 1` decays faster
than any `z⁻ᵃ`, the generating function is entire, and **the condition has no analogue**: `Π` is
finite at every δ swept, including δ = 0.80 per year, where it is 7.5 × 10²⁵ and still a number.

The instrument checks that this is a real difference and not a tautology: the geometric form is
**infinite** at δ = 0.60 per year, where the registered form returns a finite value — the two checks
that close §5 of the run log.

**This does not validate the disclosed rectangle, and REG-004 §3 struck the statistic that would
have looked as if it did.** §4.4 reports "the share of the disclosed rectangle inside the model's
domain". Under an entire generating function the domain is everything and the complement is empty,
so that share is 100% by construction and carries no information. It is not reported here at any
value. What replaces it is §3's **level**, which is defined everywhere and moves in both directions.

## 3 · The sign, and the size · **N1**, **M1** on the ladder, **M3** on the rectangle

Against a geometric with the **same mean** — the comparison the naive substitution actually makes —
the measured lag distribution defers **less**, at every δ swept, on both the as-fitted and the
`T ≥ 1` versions. That is **N1**, the direction registered in advance on the reliability argument
that an increasing failure rate is NBUE and an NBUE distribution's moment generating function is
dominated by the equal-mean exponential's (Marshall and Proschan, 1972).

**The size depends entirely on where you stand, and the two answers are the finding.**

| where | worst departure of the naive form | ladder |
|---|---|---|
| §4.4's tabulated four-tier ladder (δ = 0.030 … 0.002/yr) | **0.67%** | **M1** |
| the decay rates disclosure spans (δ = 0.025 … 0.333/yr) | **43.9%**, at a three-year life | **M3** |

At a forty-year life the correction is half a per cent. At a ten-year life it is 2.9%. At a
five-year life 9.3%. At the three-year life ASC 350-30-50 routinely carries, the constant-hazard
closed form **overstates the deferral measure by 43.9%**. The correction is negligible where the
paper's own ladder sits and material where the filings sit, and the reason is visible in the
transform: `zᵃ` with `z > 1` weights the tail, and the tail is exactly what a constant hazard gets
wrong.

**The rectangle's maximum is a bounded number and not an artefact.** The naive form's pole sits at
δ = 0.435 per year, a 2.3-year life, **outside** the rectangle whose fastest rate is 0.333 — which
is REG-003's R1 verdict arriving from the other direction. The instrument checks this, because a
maximum taken next to a pole cannot fail to reach M4 and would have been a phantom tag.

**Both registered estimator failures behaved as registered.** Conditioning on `T ≥ 1` — the mass
the fitted Weibull puts at a lag `peak_onset` cannot produce, 7.87% of it — moves `R` **up** at
every tier, as REG-004 §3 said it would. And the Kaplan–Meier transform built from the observed
twenty-quarter window sits **below** the fitted one at every tier, confirming it as the lower bound
the registration insisted it be called.

## 4 · **C2** — and the rung that moved was moved by the LEVEL, not by the shape

This is the half that could refute a sentence already in print, and something in §4.4 does need
correcting — though not the sentence the registration was watching.

**The top-rung crossing barely moves.** §4.4's `δ₃* = Kα/(1 + K)` generalises exactly to
`Π(1/(1 − δ₃*)) = 1 + K`, and the two channels REG-004 §4 named as opposing very nearly cancel:

| | K | δ₃\* per year | goodwill's tabulated 0.002 sits |
|---|---|---|---|
| §4.4 as published, α = 0.05 | 0.1875 | **0.00789** | 3.9× below the crossing |
| constant hazard at the measured α̂ | 0.01566 | **0.00755** | 3.77× below |
| the measured shape, `k̂ = 1.21` | 0.01439 | **0.00754** | 3.77× below |

**The shape moves the crossing by 0.13%.** The knife edge §4.4 describes is not a knife edge in the
hazard's shape at all, and goodwill's tabulated decay rate stays a factor of 3.8 inside it.

**But the tabulated Kendall τ is −0.67 at the measured rate, not −1 — and that is true before any
shape correction is applied.** §4.4's own first-rung boundary,

> δ₁ < αδ₀/(2α − δ₀),  which tends to δ₀/2 as α grows

sits at **0.0214** when α = 0.05 and the table assigns δ₁ = 0.020, inside by a fourteenth. At the
**measured** α̂ = 0.408 the same boundary sits at **0.0156**, and 0.020 is outside it. The first
rung rises, τ moves from −1 to −0.67, and **the cause is the level of α that §5.4 measured, not the
shape this registration went looking for.** The section's closing sentence already says the
measured rate is the one that applies; its table is still evaluated at the calibration. Those two
cannot both stand, and the repair is in the manuscript rather than in this file.

**The direction is the right one for the paper.** §4.4's argument is that a φ-ordered design does
not read what it ordered; τ = −0.67 is still a design reading the reverse of its own ordering at
five of six pairs. What it costs is the word *exactly*, and the tabulated ladder can no longer be
described as the reversal case — it is the reversal case **at the calibration**, and the near-miss
case at the measured rate. §4.4's own dispersion result already supplies the general statement:
across 4,000 draws under the standards' falling ladder, recovery 1.9% and mean τ −0.41.

## 5 · **E2** — α_eff is a function, and over the disclosed rectangle it is not a flat one

| life | δ per year | α_eff per year |
|---|---|---|
| 40 y | 0.025 | 0.4368 |
| 20 y | 0.050 | 0.4388 |
| 10 y | 0.100 | 0.4431 |
| 5 y | 0.200 | 0.4538 |
| 3 y | 0.333 | 0.4758 |

Top-to-bottom ratio **1.115**, which is **E2**: a single recalibrated α misstates one end of the
disclosed rectangle by about a ninth, and the direction is that faster-decaying classes behave as
if recognition were faster. Across §4.4's own four-tier ladder the ratio is 1.006 and a constant
would have done — which is why §4's magnitudes barely move and §3's rectangle magnitudes do.

Note that α_eff → 1/E[T] = 0.435 per year as δ → 0, which is **not** α̂ = 0.408: the geometric MLE
and the fitted distribution's mean are different summaries of the same sample, and they differ by
exactly the shape this file is about.

## 6 · **S2** — the exchange survives, and the check's own limit is worth stating

REG-004 §5 registered one check and a stopping rule. The result: an age-dependent world sits
**5.09 × 10⁻⁴** from its own constant-hazard match at α_eff, and **5.09 × 10⁻⁴** from that match's
§4.2 mirror. The ratio is 1.000.

**That equality is forced, not discovered, and saying so is the point.** The two constant-hazard
worlds are an exact §4.2 mirror pair — the instrument verifies they agree to 10⁻⁹ — so their
distances to any third series are identical by construction. What the check actually establishes is
the number in front: an age-dependent world departs from the constant-hazard family by 5 × 10⁻⁴ in
the reported series, which is four orders of magnitude below the 3 × 10⁻¹ that separated the right
conserved quantity from a plausible wrong one in §4.2. **The degeneracy is not repaired by
age-dependence.** S2, and the stopping rule holds: the general search — whether `k` is identified
from a reported series at all, and whether the *best-fitting* constant-hazard world rather than the
α_eff one is closer still — is teed up in the handoff and was not attempted.

## 7 · What may be claimed

**May be claimed.** That `R = (1 − φ)(Π(1/(1 − δ)) − 1)` for any recognition-lag distribution, with
the published form as its geometric special case; that the existence condition is a tail condition
and is vacuous at the measured shape; that the shape correction is under 1% on the paper's ladder
and up to 44% at disclosed lives; that the top-rung crossing is insensitive to the shape; and that
§4.4's tabulated τ = −1 is a property of the α = 0.05 calibration.

**May not be claimed.** That α_eff is "the" recognition rate. That the fitted lag distribution
transfers to classes the PRE-002 sample does not cover. That the vanishing domain restriction
validates the disclosed rectangle — a share of an empty set is not evidence. That any of this
touches PRE-001; REG-003 §7 ruled that out in writing before the numbers existed and nothing here
reopens it.

**Two process notes, which belong here and not in the paper.** The instrument's first draft placed
the naive form's pole *inside* the disclosed rectangle and declared the rectangle-wide maximum an
unbounded phantom-tag statistic. The pole is at 0.435 and the rectangle stops at 0.333; the error
was a mis-taken fourth root. The correction turned an excuse into the strongest number in the file.
A guard that lets you *skip* a statistic deserves the same arithmetic scrutiny as one that lets you
report it.


**And the unit tests caught something no run of the instrument could have.** `Π` was summed with the
term ratio evaluated as `S(a+1)/S(a)`. For a geometric lag past its own radius of convergence, and
for any decreasing-hazard lag, the survival function **underflows to 0.0 while the term is still
large** — and the loop read that as the tail being exhausted and returned a finite number for a
divergent sum. Every ladder in this file was unaffected, because the fitted shape converges in a few
dozen terms and never approaches the underflow; the defect would only ever have fired on the two
cases the paper uses to say what the condition *excludes*. It was found by
`tests/test_deferral_transform.py` asserting that the geometric transform diverges at 1.05 α and
that a `k < 1` fit would have had no steady state at all — two tests written to pin claims in §4.9
rather than to hunt a bug. **A guard that certifies convergence has to be able to tell an exhausted
tail from an underflowed one**, and the repair is to carry the ratio in a form that cannot underflow
(`q^((a+1)^k − a^k)` for the Weibull, the constant `1 − α` for the geometric) rather than as a
quotient of two survival values.
