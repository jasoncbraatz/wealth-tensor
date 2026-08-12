# REG-005 · Theory registration · is the recognition lag's SHAPE identified from a reported series?

- **Status:** REGISTERED — committed and pushed before any line of
  `scripts/wt091_lag_shape_identifiability.py` was written and before any number below was
  computed. WT-052.
- **Registered:** 2026-08-12, session `wealthTensor-17`.
- **Series:** `REG-*`. **A claim about our own arithmetic**, in the manner of REG-001, REG-002 and
  REG-004 — with one exception: ladder `P` routes through REG-003's measured lag distribution and
  can therefore put a third quantity next to two the manuscript already prints.
- **Instrument to be written after this file is pushed:** `scripts/wt091_lag_shape_identifiability.py`.
- **Sample:** none collected. The only empirical inputs are REG-003's fitted `k̂ = 1.210`,
  `q̂ = 0.921342` and its profile interval `[1.135, 1.285]`, all already committed and already
  reported. No EDGAR access, no new data, no re-fit.

---

## 0 · The question, and why it is now the largest one open

§4.9 closes on a sentence: *"Whether the shape parameter itself is recoverable from a reported
series is a different question and is open."* REG-004 §5's stopping rule put it here on purpose,
so that a promising result could not pull that session into an unregistered search. This file
opens it.

§4.2 proves an impossibility by counting: the reported series is a sum of two geometrics, so it
contains **four numbers** — two roots and two amplitudes — and the model has **five** parameters.
Five into four does not go and the shortfall lands on φ. That count was taken under a constant
recognition hazard. REG-004 replaced the constant hazard with an arbitrary lag distribution `T ≥ 1`,
which is not one more parameter but an **infinite-dimensional** object, and under it the reported
series is no longer a finite-order recursion at all. The question this registration asks is not
whether `k` is another parameter to lose. It is whether the extra structure is **visible**:

> Does a constant-hazard world exist whose reported series reproduces an age-dependent world's, and
> if so, how closely?

The two outcomes are both worth having and they point in opposite directions.

- **If the shape is not identified**, §4.2's impossibility result gets materially stronger — the
  shortfall is not five-into-four but infinite-into-four — and §4.9's correction becomes something
  a reader **cannot apply from filings**, because the quantity it corrects for is not in them. That
  is a limitation of the correction, it is worth stating precisely, and stating it is a repair of
  §4.9's scope rather than a hedge added to it.
- **If the shape is identified**, there is a **second observable in the reported series that nobody
  in this literature has used**, and §5.4's event-date estimate acquires an independent check that
  needs no hand-collected deal data.

## 1 · The instrument's observational setting, chosen to be the FAVOURABLE one

Under REG-004's transform the reported series is

> **C(t) = E(t) + G(t)**,  E(t) = E₀(1 − δ)ᵗ,
> **G(t) = (1 − φ) δ E₀ Σ_{a=1}^{t} (1 − δ)^{t−a} S(a)**,  S(a) = P(T ≥ a)

which is the §4.2 closed form's construction with the geometric survival `(1 − α)^{a−1}` replaced by
an arbitrary `S`. The books open square, `C(0) = E(0) = E₀`, and the series is normalised by `C(0)`.

**That normalisation is a choice and it is the generous one.** §4.2's sharpest result is that when
the physical scale `E₀` is *not* observed, φ is not two-valued but **free** — a factor of 1.67 in the
unobserved scale spans the whole unit interval. Normalising by `C(0)` grants the analyst exactly the
thing §4.2 says a firm-level series does not have. **Every negative result in this file is therefore
a fortiori**: if the shape is invisible even to an analyst who has been given the physical scale, it
is invisible to one who has not. A positive result carries the opposite asymmetry and is registered
with that caveat attached in advance: it would hold only for an asset followed from acquisition.

**Units.** REG-003's lag is in **quarters**; §4.4's ladder and §4.9's table are in **years**. The
instrument works in quarters throughout and converts by `δ_q = 1 − (1 − δ_y)^{1/4}`, reporting every
δ in years. Any figure in this file in years has been through that conversion.

## 2 · Falsifiers on the construction — each one can kill the instrument

Deterministic, run before any of §4–§6.

- **F1 · Nesting.** At `k = 1` the convolution above must equal §4.2's published closed form
  `C(t) = E₀[δ(1 − φ)Aᵗ − (α − φδ)Dᵗ]/(δ − α)` to **≤ 1 × 10⁻¹² relative at every t**, at every
  swept `(δ, φ)`. A larger departure is an algebra error and the registration fails outright.
- **F2 · Non-vacuity of the search.** Given a series generated *in a constant-hazard world*, the
  mimic search must recover the generating `(α, δ, φ)` **or its exact §4.2 mirror** `(δ, α, φδ/α)`
  to ≤ 1 × 10⁻⁶, from the registered multi-start grid alone. **If the search cannot find the answer
  when there is one, no residual it reports about any other world means anything.**
- **F3 · Witness.** The mimic search must **fail** on a world it should not be able to fit. The
  registered wrong world is a lag with `k = 0.5` — a *decreasing* hazard, which by §4.9 admits no
  steady-state deferral measure at any positive decay rate. Its best geometric mimic must leave a
  residual above ladder `I`'s I2 threshold. If the geometric mimics that too, the metric is blind
  and **no verdict may be read from any ladder in this file.**
- **F4 · The `T = 0` mass is a pure φ reparameterisation, and this is why REG-003's erratum cannot
  bite here.** The fitted Weibull places `1 − q̂ = 7.87%` of its mass at `T = 0`, which `peak_onset`
  cannot produce — the erratum that bit REG-004 twice and on a second estimator. Conditioning on
  `T ≥ 1` replaces `S(a)` by `S(a)/S(1)`, which divides `G(t)` by `q̂` at **every age and every t
  alike**, and `G` is proportional to `(1 − φ)`. The conditioning is therefore **exactly absorbed**
  by `(1 − φ) → (1 − φ)/q̂`, and the reported series after that substitution must be unchanged to
  ≤ 1 × 10⁻¹². If it moves, the absorption argument is wrong and every φ statement in this file
  inherits a caveat. **This is registered as a falsifier rather than assumed**, precisely because
  the same erratum has now been paid for twice.

## 3 · The four questions, answered before any number exists

**WHICH OUTCOMES DOES THIS THRESHOLD FAIL TO SEPARATE?** *(the falsifier · -14)*

A verdict of the form *"the best constant-hazard mimic leaves a residual below tolerance, therefore
the shape is invisible"* fails to separate **the series cannot see shape** from **this particular
k̂ = 1.21 is close enough to 1 that there is barely any shape to see.** The Weibull at `k = 1` *is*
the geometric, so the residual is **zero by construction** there and rises continuously away from
it: a small residual at k̂ is ambiguous between a statement about the instrument and a statement
about the sample. **Registered repair:** the residual is reported as a **function of `k` over
[0.6, 2.0]** and never as a point value at k̂, and the headline statistic of ladder `W` is the
**width of the k-interval a series of given precision cannot resolve** — which is defined at every
k, is non-empty at every k, and cannot be confused with "k̂ is near 1."

**IS THE SET I AM TAKING A SHARE OF GUARANTEED NON-EMPTY?** *(the falsifier · -14)*

The tempting statistic is *"the share of the disclosed δ-rectangle over which the shape is visible."*
**If the residual is below tolerance everywhere, that set is empty and its share is 0% by
construction** — the exact mirror image of the statistic REG-004 §3 struck, arriving from the other
side. **Registered guard: no share over the δ-rectangle is reported unless the instrument exhibits
both a δ at which the shape is visible and a δ at which it is not.** If the set is empty, or is
everything, the finding is reported as the **level** — the residual curve over δ — and the share is
withheld at any value. Ladder `W`'s statistic is deliberately built to be immune to this: the
k-interval always contains k̂, so it is non-empty by construction and its *width* is the content.

**WHICH VALUES CAN THIS INSTRUMENT NOT PRODUCE, AND DOES MY ESTIMATOR ASSIGN THEM MASS?**
*(the ESTIMATOR · -15)*

Three, and the first is the one that could manufacture a false positive.

1. **The mimic's parameter box.** §4.2's world requires `α ∈ (0, 1]`, `δ' ∈ (0, 1)`, `φ' ∈ [0, 1]`
   and admissibility `φ'δ' ≤ α'`. An unconstrained least-squares optimiser assigns mass to
   `φ' > 1` — a firm recognising more than the whole decline — and to `φ' < 0`. **If the best mimic
   lives outside the box, then clipping to it inflates the residual, and the instrument would report
   the shape as identified when what separated the two worlds was the constraint and not the data.**
   Registered: **both optima are computed and both are reported, always** — the unconstrained one,
   which answers *is this series a two-exponential sum at all*, and the admissible one, which
   answers *is it the series of an economically possible firm*. If they differ, **the difference is
   itself the finding**, and it is a finding about the admissible set rather than about the series.
2. **The removable singularity at `α' = δ'`.** §4.2's closed form is `0/0` there and the optimiser
   walks into it. The instrument uses the confluent limit `C(t) = E₀Dᵗ[1 + (1 − φ)δt/(1 − δ)]` in a
   registered neighbourhood rather than letting a division by `δ − α` decide anything.
3. **`T = 0`,** which `peak_onset` cannot produce. Handled by F4 above, which proves rather than
   assumes that it is absorbed.

**CAN THIS GUARD TELL AN EXHAUSTED TAIL FROM AN UNDERFLOWED ONE?** *(the guard · -16, generalised)*

`-16` summed `Π` with the term ratio `S(a+1)/S(a)`, the survival underflowed to `0.0` while the term
was still large, and the loop read that as an exhausted tail and returned a **finite number for a
divergent sum**. The analogue here is an optimiser rather than a sum, and it is the same defect:
**a converged flag cannot distinguish a true minimum from a canyon floor where the objective is flat
to machine precision.** §4.2 already reports that canyon at 291-fold. A single-start optimiser
returning a small residual and a tight parameter vector looks identical to one that stopped because
the gradient underflowed. Registered repairs, all four:

1. **Multi-start** from a registered deterministic grid, **≥ 64 starts**, no random seeds.
2. The reported quantity is **not the argmin** but the **diameter, in parameter space, of the set of
   optima within `(1 + 10⁻⁶)` of the best objective** — the canyon's width rather than its floor.
3. Survival is carried by the **multiplicative recursion REG-004 installed** (`q^((a+1)^k − a^k)`,
   the constant `1 − α` for the geometric) and never as a quotient of two survival values.
4. **A run whose best objective equals its worst starting objective to machine precision is
   REFUSED, not reported.** That is what an underflowed optimiser looks like from outside, and
   refusing is the only answer that cannot be mistaken for a result.

## 4 · The metric, and the reason the obvious one is registered as WRONG

The residual between a candidate series `ĉ` and the target `c` is the **relative-per-point** RMS

> **ε = sqrt( (1/N) Σ_{t=1}^{N} ( (ĉ(t) − c(t)) / c(t) )² )**

and **not** `‖ĉ − c‖ / ‖c‖`. The reason is registered because it is the difference between a live
ladder and a vacuous one: the series decays geometrically, so under the norm-relative metric the
late observations contribute essentially nothing and **ladder `S` — does a longer series help? —
would land on S3 by construction**, having measured the decay of `C` rather than the information in
it. The relative-per-point metric also happens to be the economically right one, since a financial
statement's precision is relative to its own magnitude and not to its magnitude twenty years ago.
`C(t) > 0` throughout under admissibility, and the instrument checks it rather than assuming it.

## 5 · The ladders — exhaustive, every real number in exactly one cell, all written before any run

**Ladder I · is the shape visible in a NOISELESS series?** `ε` = the best **admissible**
constant-hazard mimic's residual against the k̂ = 1.21 world, `N = 40` quarters, maximised over the
disclosed δ-rectangle (three- to forty-year lives).

- **I1 ·** ε < 10⁻⁶ → invisible to arithmetic. The constant hazard mimics the measured shape to
  machine precision and `k` is not identified from a reported series **at any noise level**.
- **I2 ·** 10⁻⁶ ≤ ε < 10⁻³ → invisible in practice. No reported series carries the relevant
  structure to four significant figures, and §4.9's correction is not applicable from filings.
- **I3 ·** 10⁻³ ≤ ε < 10⁻² → borderline; length and noise decide, and ladders `S` and `N` do.
- **I4 ·** ε ≥ 10⁻² → **the shape is visible**, and there is a second observable in the reported
  series that this literature has not used.

**Predicted before running: I2.** The reasoning is Jorgenson (1966) — rational distributed lags,
of which the geometric is the lowest-order member, are dense in lag space, so a mimic of arbitrary
accuracy exists in principle — read together with the classical ill-conditioning of exponential
sums, where a three-exponential signal is reproduced by two to a few parts in 10⁴ with rates bearing
no relation to the truth (Lanczos 1956, as quantified by Varah 1982). **I4 would refute that reading
on our own construction** and is the outcome that yields a new instrument rather than a new
limitation. **I1 is live and would be the strongest form of the negative result.**

**Ladder P · where does the best-fitting constant hazard SIT?** The manuscript already prints two
recognition rates: **α̂ = 0.408/yr**, the geometric MLE on event dates, and **α_eff(δ) ∈ [0.437,
0.476]/yr**, REG-004's deferral-matching function. The series-matching constant `α_ser` is a third
functional of the same lag distribution. The mimic's two roots are recovered as a **set** — §4.2's
exchange is not broken by anything here — and `α_ser` is read as the root that is not δ, with both
reported whenever the assignment is ambiguous.

- **P1 ·** `α_ser` within 1% of α̂ at every swept δ → the series-matching constant is the event-data
  MLE and no new quantity exists.
- **P2 ·** `α_ser` within 1% of `α_eff(δ)` at the same δ → the series match and the deferral match
  are one recalibration.
- **P3 ·** differs from both by more than 1% somewhere on the rectangle → **three distinct
  "recognition rates" live in this paper and the manuscript must say which is which.**

**Predicted before running: P3.** Registered reason: least squares on the series weights the
**transient**, `α_eff` matches the **steady state**, and α̂ matches the **event dates** — three
different functionals of one distribution, with no reason to coincide. P1 or P2 would be a genuine
surprise and would mean the series match is a quantity already in print.

**Ladder W · how wide is the k-interval a series cannot resolve?** Define

> **I(σ) = { k : min over (q, δ', φ') of ε( series(k, q, δ', φ'), series(k̂, q̂, δ, φ) ) ≤ σ }**

— the shapes that reproduce the truth to within σ once every other parameter is best-fitted. `I(σ)`
contains k̂ by construction, so it is **non-empty at every σ** and its **width** is the content.
Reported at σ ∈ {10⁻⁶, 10⁻⁴, 10⁻³, 10⁻²}, against REG-003's event-based interval width
**0.150** (`[1.135, 1.285]`). Ladder read at **σ = 10⁻³**, with `W = |I(10⁻³)| / 0.150`.

- **W1 ·** W < 1 → the reported series is **more** informative about the shape than the event dates.
- **W2 ·** 1 ≤ W < 10 → comparable; the series is a usable second instrument.
- **W3 ·** 10 ≤ W < 100 → an order of magnitude less shape information; a weak check at best.
- **W4 ·** W ≥ 100, or `I(10⁻³)` covers the whole swept range [0.6, 2.0] → **`k` is not identified
  from a reported series.** §4.2's shortfall deepens from five-into-four to infinite-into-four.

**Predicted before running: W4**, on Sims (1971), whose Theorem 2 and §5 conclusion are that
finite-dimensional approximations to an infinite-dimensional lag space are meagre in it and that
their approximation error is **never asymptotically negligible** — and who names rational lag
distributions, Jorgenson's class, as exactly the approximating family his negative result covers.

**Ladder S · is it a sample-size problem or an identification problem?** `|I(10⁻³)|` at
`N ∈ {20, 40, 80, 400}` quarters.

- **S1 ·** shrinks like `N^{−1/2}` or faster → a sample-size problem; a long enough series
  identifies the shape and the limitation is about data length, not about information.
- **S2 ·** shrinks, but slower than `N^{−1/2}` → weakly identified; the rate is reported.
- **S3 ·** does not shrink materially — under 2× from `N = 20` to `N = 400` → **an identification
  problem and not a sample-size problem**, which is the sharp form of the result.

**Predicted: S3**, and the metric of §4 was chosen specifically so that this ladder could have
landed elsewhere.

**Ladder N · what noise buries it?** At σ ∈ {10⁻⁴, 10⁻³, 10⁻²}, **200 deterministic draws** (fixed
seed, recorded), fit `k` to the noisy series over the swept range, report the **interquartile range**
of the fitted `k`.

- **N1 ·** IQR < 0.150 at σ = 10⁻³ → the series recovers the shape at a realistic precision.
- **N2 ·** 0.150 ≤ IQR < 1.5 → degraded but informative.
- **N3 ·** IQR ≥ 1.5, or the fits pile on the swept boundary → buried, and the pile-up fraction is
  reported rather than the quantiles of a censored distribution.

## 6 · What the manuscript does in each case — registered so the writing is not a post-hoc choice

- **If the shape is NOT identified (I1/I2 with W3/W4).** §4.9's closing sentence is **answered
  rather than deleted**: the open question becomes a stated scope, namely that §4.9's correction
  requires the lag distribution and the lag distribution requires **event dates**, which is why
  §5.4 collected them. §4.2's paragraph beginning *"The result is stronger than a two-point
  ambiguity"* gains the generalised count. **Under charter §2 this is REPLACE, not ABSORB** — an
  open question is retired into a scope statement, and the defensive-sentence count does not rise.
- **If the shape IS identified (I3/I4 with W1/W2).** A new subsection reports the second observable
  and what precision a series must carry to use it, and §5.4 acquires an independent check that
  needs no hand-collected deal data.
- **In either case**, ladder `P`'s answer decides whether the manuscript must name three recognition
  rates where it currently names two.

## 7 · What may be claimed, and what may not

**May be claimed.** Whether a constant-hazard world reproduces an age-dependent world's reported
series, and to what precision; the width of the k-interval a series of stated precision cannot
resolve; whether that width is a function of series length; where the series-matching constant sits
relative to α̂ and α_eff; and whether the best mimic is an economically admissible firm.

**May not be claimed.** That any result here bears on the **empirical** identifiability of φ beyond
what §4.2 already proves — this file adds the shape, it does not revisit φ. That a negative result
licenses removing §4.9's correction: a correction that cannot be applied from filings is still the
right correction for anyone holding the lag distribution, and §5.4 holds it. That a negative result
says anything about PRE-001; REG-003 §7 ruled that out in writing before any of these numbers
existed and nothing here reopens it. That the fitted lag distribution transfers to classes the
PRE-002 sample does not cover. That the normalisation of §1 is innocuous — it is generous, and every
negative result inherits *a fortiori* while every positive one inherits the caveat.

**Stopping rule.** The instrument runs once. Unregistered robustness may be reported, labelled as
robustness, and may not change a verdict. **No parameter is added to the model at any point.** If a
ladder lands badly, the manuscript says so.
