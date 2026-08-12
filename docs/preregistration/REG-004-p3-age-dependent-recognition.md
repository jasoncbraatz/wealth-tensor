# REG-004 · Theory registration · the deferral measure under an age-dependent recognition rate

- **Status:** REGISTERED — committed and pushed before any line of `scripts/wt090_age_dependent_alpha.py`
  was written and before any number below was computed. WT-052.
- **Registered:** 2026-08-12, session `wealthTensor-16`.
- **Series:** `REG-*`. **This one is a claim about our own arithmetic**, in the manner of REG-001
  and REG-002, not about the world — with one exception, §4's `C`-ladder, which routes through the
  measured lag distribution of REG-003 and can therefore refute a sentence already in print.
- **Instrument to be written after this file is pushed:** `scripts/wt090_age_dependent_alpha.py`.
- **Sample:** none collected. The only empirical input is `data/pre-002-events.json`, already
  committed, already reported in RESULT-REG-003, and not re-derived here.

---

## 0 · The disclosure this registration owes, stated first

The algebra in §1 was carried out **before** this file was written. It is four lines of
generating-function manipulation on a recursion already in print, it is checkable by any reader in
the time it takes to read it, and pretending otherwise would be theatre. What a registration can
still bind — and what this one binds — is everything the algebra does not settle: the **sign** of
the correction, its **magnitude**, whether §4.4's tabulated crossing **survives** it, whether the
existence condition has an analogue, and whether §4.2's impossibility result was leaning on the
constant hazard without saying so. None of those numbers exists yet. The falsifiers in §2 can kill
the derivation itself; the ladders in §3–§5 are exhaustive and were written before any run.

## 1 · What is being registered

`wt089`/REG-003 measured the recognition lag and **rejected the constant hazard the model assumes**:
discrete Weibull k̂ = 1.210, 95% profile interval [1.135, 1.285], stable under truncation at 8, 12
and 16 quarters. The rejected assumption is not decorative. Paper III's deferral measure

> **R = (1 − φ) δ / (α − δ)**

is derived by summing a geometric, and §4.3, §4.4 and §7 all use it. §4.4 in particular reads its
**domain** (`R` exists only where α > δ), its **crossing** (δ₃\* = Kα/(1 + K), K = R₂/(1 − φ₃),
numerically 0.00789), and its **first-rung boundary** off that closed form. If the closed form is an
artefact of the memorylessness the data reject, so is everything read off it.

**The claim being registered.** Let a gap cohort be recognised after a lag `T` measured in periods,
with `T ≥ 1`, and write `Π(z) = E[z^T]` for its probability generating function. Then the
steady-state ratio of unrecognised gap to physical value is

> **R = (1 − φ) · ( Π(1/(1 − δ)) − 1 )**

with `Π` evaluated at `z = 1/(1 − δ) > 1` — a generating function outside the unit disc, so a
**discrete moment generating function**, not a Laplace transform. Equivalently the closed form
survives verbatim with a **δ-dependent effective rate**

> **α_eff(δ) = δ · Π(1/(1 − δ)) / ( Π(1/(1 − δ)) − 1 )**,  **R = (1 − φ) δ / (α_eff − δ)**

and the existence condition **α > δ** becomes **Π(1/(1 − δ)) < ∞**, a condition on the radius of
convergence of the lag's generating function and therefore on its **tail**, not on its mean.

**φ is untouched.** It multiplies the whole expression, exactly as before, so §4.2's `(1 − φ)`
proportionality and every ranking statement that depends only on the `(1 − φ)` channel is
unaffected by anything in this file. That is registered as a prediction too, and §2's F4 can
falsify it.

## 2 · Falsifiers on the derivation — each one can kill it

Every check below is deterministic and is run before any of §3–§5.

- **F1 · Nesting.** With `T` geometric on {1, 2, …} at rate α, the registered form must reduce to
  `(1 − φ)δ/(α − δ)` to **machine precision (≤ 1 × 10⁻¹²** relative) at every δ on the swept grid.
  Any larger departure is an algebra error and the registration fails outright.
- **F2 · Simulation.** A direct age-structured simulation of the filter — gap carried as cohorts,
  each cohort aged and recognised at its own age-specific hazard `h(a)`, no closed form anywhere in
  the loop — must reproduce `R` to the **transient bound the geometric case already carries,
  2 × 10⁻⁴ after 400 periods** (§4.3's published tolerance). Failure means the derivation does not
  describe the filter it claims to describe.
- **F3 · Witness.** The same simulation run against a **deliberately wrong** `R` — the naive
  substitution `α ← 1/E[T]` — must **fail** the F2 tolerance somewhere in the swept rectangle.
  If the wrong answer also passes, F2 is vacuous and no verdict may be read from it.
- **F4 · φ separability.** Sweeping φ over {0.0, 0.1, …, 1.0} at fixed `T` and δ, the ratio
  `R(φ)/R(0)` must equal `(1 − φ)` to ≤ 1 × 10⁻¹². If it does not, φ is not a pure scale under
  age-dependence and §4.2's proportionality result inherits a domain restriction.

## 3 · The three questions, answered before any data are touched

**WHICH OUTCOMES DOES THIS THRESHOLD FAIL TO SEPARATE?**
The verdict "the closed form survives" fails to separate *survives with the same functional form
and a redefined constant* from *survives only as a δ-dependent function*. **The claim registered is
the second**, and it is the weaker and more inconvenient of the two: `α_eff` is **not a parameter**,
it is a function of δ, so no single recalibrated α can repair the model across the ladder. The
registration therefore reports `α_eff` **as a curve over the disclosed rectangle and never as a
number**, and §5's `E`-ladder decides whether the curve is flat enough that a single value would
have done.

**IS THE SET I AM TAKING A SHARE OF GUARANTEED NON-EMPTY?**
No — and this one bites immediately. §4.4 reports "**the share of the disclosed rectangle inside the
model's domain**", 0% at α = 0.05 and 100% at α̂ = 0.408. Under a lag distribution whose generating
function is entire, the domain is **everything**, the complement is **empty**, and that share is a
share of an empty set: it is 100% by construction and carries no information. **It is therefore not
reported as a finding of this registration**, at any value. What replaces it is the **level** of
`R`, which is defined at every δ and can move in either direction.

**WHICH VALUES CAN THIS INSTRUMENT NOT PRODUCE, AND DOES MY ESTIMATOR ASSIGN THEM MASS?**
Two failures, both registered with their direction before the numbers exist.

1. **`T = 0` is unreachable by construction** — `peak_onset` dates the peak strictly before the
   charge quarter, which is REG-003 §5's erratum, and it applies here **again and to a second
   estimator**: the fitted Nakagawa–Osaki discrete Weibull places mass `1 − q̂` at `T = 0`. Both
   versions are reported: **as registered in REG-003**, and **conditioned on `T ≥ 1`**. Registered
   direction: moving mass from `0` to `≥ 1` raises `E[z^T]` for `z > 1`, so it **raises R and lowers
   α_eff**. If the computed shift goes the other way, this reasoning is wrong and the registration
   says so.
2. **`T > 20` quarters is unobservable** — the sample is right-censored at the twenty-quarter
   lookback. The **non-parametric** `Π` built from observed frequencies truncates the tail, and
   `z^a` with `z > 1` weights precisely that tail **upward**. Registered direction: the
   non-parametric `Π` is a **strict lower bound** on the true one, and the bias **grows with δ**.
   It is therefore reported **as a lower bound and never as the point estimate**; the fitted
   discrete Weibull, which extrapolates the tail, supplies the estimate.

## 4 · The ladders — exhaustive, and every real number lands in exactly one cell

**Ladder N · the sign of the correction.** Compare `R` under the measured lag distribution against
`R` under a geometric with the **same mean**, over the disclosed rectangle.

- **N1 ·** measured `R` **below** the equal-mean geometric at every swept δ, strictly.
- **N2 ·** measured `R` below at some δ and above at others.
- **N3 ·** measured `R` **at or above** the equal-mean geometric at every swept δ.

**Predicted before running: N1**, on the reliability argument that an increasing failure rate is
NBUE and an NBUE distribution's moment generating function is dominated by that of the exponential
with the same mean (Marshall and Proschan, 1972). **N3 would refute that argument on our own data.**
N2 is live and is the specifically interesting outcome, because the sample is **bimodal** — a spike
at lag one on top of a rising hazard — and a mixture with a point mass need not be NBUE at all. The
prediction is made at the level of the *fitted* Weibull, where IFR holds; it is **not** made for the
raw empirical mixture, and the two are reported separately for exactly that reason.

**Ladder M · the magnitude.** Maximum relative departure of the naive substitution `α ← 1/E[T]`
from the registered form, over the disclosed rectangle of §4.4 (property ten to forty years,
finite-lived intangibles three to twenty, plus the tabulated four-tier ladder).

- **M1 ·** < 1% — the constant-hazard form is a safe approximation and the correction is a footnote.
- **M2 ·** 1% – 10% — real, second-order, reported as a bound on published magnitudes.
- **M3 ·** 10% – 50% — the correction changes reported magnitudes and §4.3's `R` column needs it.
- **M4 ·** > 50% — the constant-hazard closed form is not usable at disclosed rates.

**Ladder C · does §4.4's tabulated reversal survive?** This is the half that can refute a sentence
already in print. Under the registered form the top-rung crossing solves `Π(1/(1 − δ₃*)) = 1 + K`
with `K = R₂/(1 − φ₃)` recomputed under the same form. **The direction is not predicted, and the
reason is stated in advance: two channels oppose.** A lower `R₂` lowers `K` and pushes δ₃\* down; a
flatter `Π` pushes δ₃\* up. Whichever wins is the finding.

- **C1 ·** δ₃\* > 0.002 **and** the four-tier Kendall τ is still −1 → §4.4's tabulated reversal
  survives the shape correction, and the knife edge is wider or narrower by a reported factor.
- **C2 ·** δ₃\* > 0.002 **but** τ ≠ −1 → the top-rung crossing survives and a different rung moved;
  §4.4's decomposition is reported at the measured shape.
- **C3 ·** δ₃\* ≤ 0.002 → **the tabulated reversal does not survive.** §4.4's τ = −1 is an artefact
  of the constant hazard, the manuscript must say so in the section that claims it, and this
  registration will have refuted its own paper.

**Ladder D · the existence condition.** Whether `Π(1/(1 − δ))` is finite across the rectangle,
evaluated by summation to a proven remainder bound rather than by truncation.

- **D1 ·** finite everywhere on the rectangle → `α > δ` has **no analogue** under the measured
  shape; the domain restriction was a property of the assumed hazard as well as of the calibration.
- **D2 ·** finite on part of it → the restriction survives in weakened form and the boundary is
  reported.
- **D3 ·** infinite or numerically divergent anywhere the remainder bound admits → the registered
  claim about the radius of convergence is wrong.

**Ladder E · is `α_eff` flat enough to be a constant?** Ratio of `α_eff` at the top of the
rectangle to `α_eff` at the bottom.

- **E1 ·** < 1.05 → a single recalibrated α would have done, and §3's first answer is too cautious.
- **E2 ·** 1.05 – 1.50 → `α_eff` must be carried as a function; a single number misstates one end.
- **E3 ·** > 1.50 → no single recalibrated α is defensible anywhere on the ladder.

## 5 · One bounded secondary question, with its stopping rule written first

§4.2's observational-equivalence theorem swaps **two roots**. Under an age-dependent hazard the
reported series is no longer a sum of two geometrics, so the swap is not even defined, and it is
fair to ask whether the impossibility result was resting on the constant hazard without saying so.

**This registration runs exactly one check and then stops.** Construct the mirror from the
effective rate — send `(α_eff, δ, φ) → (δ, α_eff, φδ/α_eff)` — and ask whether the mirror world's
reported series still reproduces the original's.

- **S1 ·** reproduces to ≤ 1 × 10⁻¹² relative → the degeneracy is not a property of the constant
  hazard, and §4.2 needs no domain sentence.
- **S2 ·** departs by less than the dispersion a real reported series carries → the degeneracy
  survives in practice and the departure is reported as a bound, not as a repair.
- **S3 ·** departs materially → the constant hazard was load-bearing in §4.2, the theorem acquires
  a stated domain, and **the general search for an exact mirror under age-dependence is teed up in
  the handoff and is not attempted in this session.** Registered as a stopping rule so that a
  promising result cannot pull the session into an unregistered search.

## 6 · What may be claimed if the ladders land well, and what may not

**May be claimed.** The functional form of `R` under an arbitrary recognition-lag distribution; the
generalised existence condition; the sign, magnitude and δ-dependence of the correction at the
measured lag distribution; whether §4.4's crossing and first-rung boundary survive.

**May not be claimed.** That α_eff is "the" recognition rate — it is a function of δ. That the
measured lag distribution is the right one for classes other than those the sample covers; the
sample is retail and computer services, and `R`'s inputs here are the §4.4 tabulated ladder's, not
the sample's. That the correction rescues PRE-001; REG-003 §7 already ruled that out in writing and
nothing here touches it. That the disappearance of the domain restriction validates the disclosed
rectangle — a share of an empty set is not evidence, per §3's second question.

**Stopping rule.** The instrument runs once. Unregistered robustness may be reported, labelled as
robustness, and may not change a verdict. No parameter is added to the model at any point; if a
ladder lands badly, the manuscript says so.
