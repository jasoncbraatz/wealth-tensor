# REG-002 · Structural registration · §4.4 on the observable pair

- **Status:** REGISTERED — committed and pushed before any line of `wt088` was written and before
  any statistic in it was computed. WT-052.
- **Registered:** 2026-08-12, session `wealthTensor-14`.
- **Series:** `REG-*`, per REG-001 §1. This is a claim about **our own model's arithmetic**, not
  about the world. It can only fail against our own code. Nothing here may be cited as empirical
  support for P1, P2 or P3.
- **Instrument to be written after this file is pushed:** `scripts/wt088_disclosed_ladder.py`.

---

## 1 · What is being registered, and why it is not a polish pass

§4.4 of Paper III reports that the model's deferral measure **R = (1 − φ)δ/(α − δ)** runs backwards
across the four GAAP classes — Kendall τ = −1 against the ordering PRE-001 registered — and that
over 4,000 randomly drawn ladders the registered ordering is recovered in 1.9% of worlds, reversed
in 23.8%, and non-monotone in 74.2%, mean τ = −0.41.

Both numbers are computed under **two** qualitative constraints, imposed jointly:

1. **observability falls up the ladder** — the design, PRE-001, and not in question here;
2. **durability rises up the ladder** — so δ falls up the ladder, monotonically, with goodwill at
   δ = 0.002.

`wt087` and §4.4's own closing paragraph established that constraint (2) is **inferred from the
standards' scheduling behaviour**, and that scheduling tracks how *predictable* a decline is rather
than how *fast* it is. Goodwill is unscheduled because its decline is lumpy. A lumpy decline is a δ
with large variance, not a δ near zero. §4.4 currently names this as an assumption and reports the
inversion as conditional on it. **That is an honest disclosure and it is not a repair.** The paper
forbids inferring δ from a reported series and then infers a δ ladder from a reporting rule.

This registration fixes, in advance, what would have to be true for §4.4's headline to survive, and
what the section must be rebuilt on if it does not.

## 2 · The falsifiers, stated before the instrument exists

Each is a **fitted or measured quantity with a stated threshold**, per WT-080 and the rule
`-13` paid for five times: *fit the exponent, do not assert it.* No check below encodes its own
expected answer as its pass condition.

### E1 · Drop constraint (2) entirely

Redraw the 4,000 ladders with φ falling up the ladder and **δ drawn i.i.d. across the four classes,
unordered**, over the same support the existing draw uses.

- **Reported:** % recovering the registered ordering, % exactly reversing, % non-monotone, and mean
  Kendall τ with its standard deviation.
- **REGISTERED FALSIFIER.** §4.4's headline is *"the ranking does not merely blur, it inverts."*
  If the inversion is a property of the confound, mean τ stays materially negative without the
  durability ordering. **If mean τ ∈ (−0.10, +0.10), the inversion is a property of the assumed
  ordering rather than of the confound, and §4.4's headline claim is downgraded from *inverts* to
  *destroys*** — the ranking becomes uninformative rather than reversed, which is a weaker and
  different result and must be stated as such.
- Both outcomes are reportable. Neither is a failure of the section; only one of them lets the
  present headline stand.

### E2 · The threshold on goodwill's δ

Hold rungs 0–2 at the paper's calibration. Solve, in closed form and then verify numerically, for
the **δ₃\*** at which R₃ = R₂ — the exact decay rate above which goodwill stops being the
least-deferring class.

- **Reported:** δ₃\* to four figures, the implied half-life, and whether the paper's assumed
  δ₃ = 0.002 sits inside or outside a defensible interval for an asset whose decline is lumpy.
- **REGISTERED FALSIFIER.** **If δ₃\* < 0.010** — i.e. if a goodwill half-life shorter than about
  seventy years is enough to break the strict reversal — then τ = −1 is a knife-edge on an
  unsourced number and §4.4 may not report it as the section's headline.

### E3 · Lumpy, not slow

Constraint (2)'s replacement hypothesis, made concrete. Extend the model to a **time-varying decay
sequence** (declared below in §3 as an extension, not a re-specification) and drive one class with a
compound-Poisson decline: rare large drops with the **same mean rate** as a scheduled class.

- **Reported:** the realised deferral ratio under the lumpy path against R evaluated at the mean
  rate, as a measured ratio with its Monte-Carlo standard error.
- **REGISTERED FALSIFIER.** The convexity of δ ↦ δ/(α − δ) on δ < α suggests lumpiness should raise
  the deferral measure above its mean-rate value. **That is a hypothesis, not a finding, and the
  check measures the ratio rather than asserting its sign.** If the measured ratio is ≤ 1.00 the
  conjecture is refuted and goes to Abandoned Approaches; the run is still informative, because
  either sign settles whether "unscheduled" may be proxied by "slow."

### E4 · The disclosed-numbers ladder

The repair. Two rungs need no inference: property, plant and equipment and finite-lived intangibles
carry **disclosed useful lives** (ASC 360, ASC 350-30-50). Under the bridge stated in §3 below,
a disclosed life *L* gives a book write-down rate 1/*L*.

Rather than hard-code a disclosure sample this session does not have, sweep the **rectangle** of
(δ₀, δ₁) implied by the ranges disclosure practice spans and report the fraction of that rectangle
in which the first rung falls, rises, or ties.

- **Reported:** that fraction, plus the exact boundary curve in (δ₀, δ₁), plus the sign of the rung
  at the centroid of the rectangle.
- **REGISTERED FALSIFIER.** §4.4's table asserts δ₀ = 0.030 > δ₁ = 0.020 — property decaying
  *faster* than finite-lived intangibles. Disclosure practice amortises finite-lived intangibles
  over materially shorter lives than property. **If the first rung RISES over more than half the
  rectangle, §4.4's table is wrong on published numbers at its first step**, the τ = −1 line cannot
  survive in its present form, and the section is rebuilt on the sweep rather than on the table.

### E5 · What governs the direction — fitted, not asserted

From §4.4's own decomposition, a rung rises iff Δlog(1 − φ) + Δlog δ − Δlog(α − δ) > 0. Define the
ladder's **δ leverage** as the mean absolute combined δ contribution per rung and the **design
budget** as the mean design term per rung.

- **Reported:** a fitted logistic of P(reversal) on log(leverage / budget) over the random ladders,
  with the fitted slope, its standard error, and the **crossover ratio at which P = 0.5**.
- This yields a usable design rule — how much δ dispersion a φ-ordered cross-section can tolerate —
  and it is a *fitted* number. No pass condition encodes an expected slope.

### E6 · The α − δ boundary, which the disclosed numbers walk into

R = (1 − φ)δ/(α − δ) has a pole at δ = α and is negative beyond it. The paper's calibration keeps
δ ≤ 0.040 under α = 0.05 and never approaches it. **Disclosed amortisation lives for intangibles
imply rates that routinely exceed 0.05.**

- **Reported:** the model's behaviour on δ > α — whether the gap ratio diverges, converges to a
  different steady state, or has none — established by simulation, not by reading the closed form.
- **REGISTERED FALSIFIER for the section's scope.** **If no steady state exists for δ > α**, then
  §4.4's measure is defined only where the book write-down rate exceeds the economic decay rate,
  that domain restriction is a substantive claim about which firms the section speaks to, and it
  must be stated in §4.4 rather than left implicit in a calibration choice.

### E7 · The statistic that survived — does it survive this too? *(added before coding, same session)*

**Amendment, 2026-08-12, `wealthTensor-14`, registered before `wt088` existed and before any
statistic in §2 or here was computed.** Recorded as an amendment rather than folded into §2 so the
sequence is legible: E1–E6 were written first, and E7 was noticed while reading `wt083` and added
before the instrument was opened. WT-052's hole is exactly the check appended after the numbers
arrive; this one is appended before them.

§4.5 reports that the **lag** statistic does not invert — monotone under both ladders, and holding
in **100%** of 400 randomly drawn admissible ladders against 1.9% for the magnitude measure. That
draw imposes the same two constraints E1 drops, including durability rising up the ladder.

- **To be reported:** the fraction of ladders in which lag is non-decreasing up the ladder when δ
  is drawn **i.i.d. and unordered**, at the same sample size, alongside the ordered figure.
- **REGISTERED FALSIFIER.** §4.5's sentence *"the identification result does not, by itself, wreck
  a design ordered on lag"* is the paper's one concession that the confound has a limit, and §4.5
  is the section that withdrew an overreaching claim. **If the unordered fraction falls below
  0.70**, the survival of the lag ordering is itself partly an artefact of the durability
  assumption, §4.5 must say so in the same breath as it reports the 100%, and the concession is
  narrowed rather than withdrawn.
- If the fraction holds at or above 0.90, that is a **strengthening** of §4.5 obtained by trying to
  break it, and it is reported as one: the timing statistic survives an assumption the magnitude
  statistic needed.

## 3 · Declared extensions and bridges, stated before use

Two things below are **not** in the model as `src/wealth_tensor/lag.py` specifies it, and are
declared here so that no result can later be read as though it fell out of the existing model.

1. **Time-varying decay (E3).** `LayeredFirm` takes a scalar `entropy_rate`. E3 requires a
   per-period sequence. The extension is local to `wt088`, is a strict generalisation (a constant
   sequence must reproduce `LayeredFirm` to floating-point), and **that reproduction is itself a
   registered check.** If it does not reproduce, E3 is void.

2. **The disclosed-life bridge (E4).** A disclosed useful life gives the rate at which the
   **reported** asset is written down. The model's δ is the rate at which the **physical** asset
   declines. Reading one off the other assumes the disclosed schedule is unbiased for the economic
   decline. **This is an assumption, not an observation**, and §6.2's bridge discipline governs it.

   It is registered here as strictly better-located than the assumption it replaces, and the reason
   is stated in advance so it cannot be constructed after seeing the result: the disclosed-life
   bridge is a **stated and falsifiable** claim about a published number, testable against
   subsequent impairments; the δ ladder it replaces is an **inference from an absence** — from a
   class *not* being scheduled — which no observation can contradict. Both are assumptions. Only
   one of them can be wrong in a way anyone could detect.

## 4 · What this registration does not do

- It does not license removing §4.4's concessions. §4.2's Bateman/Nerlove concession and §4.5's
  withdrawal of the "PRE-001 was doomed by the φδ confound" claim are untouched by every outcome
  above.
- It does not re-open §4.8, §4.6 or §4.7.
- It registers **no prediction about the world.** Every quantity above is a property of the model.
- A result that says §4.4's headline stands is as reportable as one that says it does not, and this
  file is pushed before either is known.
