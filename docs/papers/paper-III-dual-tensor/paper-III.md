# A crisis is deferred information arriving at once: the dual tensor of wealth, and a pre-registered prediction it lost

**Jason C. Braatz**
*Independent researcher*
jasoncbraatz@gmail.com

**Draft — not yet submitted.** Version 0.4, 2026-08-11.

*Revision history — recorded because the version string had not moved since v0.1 while three rounds of
revision had: **v0.1** first draft; **v0.2** the responses to `REVIEW-001`, the internal adversarial
referee report that ships beside this paper; **v0.3** §8 Limitation 4 (φ's conditioning on the effective
decay δ), the notation audit, and references verified against live sources; **v0.4** §9 rewritten twice
in one day — once from `POSITIONING-001`, then again after that rewrite's own adversarial pass found
Jin & Myers' saintly-manager case and Bleck & Liu (2007), which between them retire this paper's claim
to a non-agency accumulate-and-release mechanism and to §4.4's volatility result. §4.4 now attributes
its qualitative finding, Basu is reclassified from threat to ingredient, and the reference list gains a
version pass and the **✓⧗** mark. **§9 is provisional: `POSITIONING-002-second-pass.md` §6 lists four
works that must be read at source before it is final.***

---

## Abstract

Three propositions about wealth, followed to a measurable consequence.
**P1**: every unit of wealth is a compound of a physical component and a claim component obeying
different laws. **P2**: the physical component degrades absent maintenance. **P3**: measured
aggregates are folds over units. Under P2 the claim component is a low-pass filter on the physical
one, with one parameter — the share φ of degradation that is observable. Recognition lag rises
**0 → 26 periods** as φ falls to zero; the integral of undelivered information is **exactly
proportional to (1 − φ)**, in closed form; and volatility is not suppressed but *relocated*, with
inter-event smoothing falling to 0.35 while the share of reported movement inside recognition events
rises to **0.99**. On this reading a crisis is the filter delivering its accumulated error at once.
P1 obliges a coupling between the components; its dimensionless form is a sawtooth touching unity
only at recognition events (mean 1.137), and every dimensionless result here is invariant — spread
**exactly 0.0** — across twelve orders of magnitude of the dimensional coupling. **The framework's
sharpest empirical prediction — that recognition lag scales with the unobservability of
degradation, with GAAP asset class supplying the observability ranking — was pre-registered, tested
on 688 EDGAR-derived events across two sectors declared in advance, and it failed.**
Jonckheere–Terpstra z = −0.290 and −0.095 (permutation p = 0.590, 0.520) against power 0.95–1.00.
The registered stopping rule fired. **The framework therefore has no confirmed
empirical claim**, and §6 states which of its results were never at risk.

**Keywords:** dual tensor · deferred information · reporting lag · financial abstraction ·
thermodynamics of capital · pre-registration · impairment · econophysics

**JEL classification:** E01, M41, D80, Q57, C63, G14

---

## 1 · Introduction

A balance sheet is not a window. It is an instrument, and instruments have transfer functions.

That sentence is the whole paper, and the rest of it is an attempt to make the sentence cost
something — to state it precisely enough that it forbids outcomes, to derive consequences that can
be checked, and then to check the sharpest one against public data and report what happened.

The starting observation is old and belongs to Soddy: a physical asset and a financial claim on
that asset are different kinds of object, and confusing them is how societies come to believe they
are wealthier than they are. What this paper adds is that the confusion has a *dynamics*. If the
physical component degrades whether or not anyone records the degradation, and the claim component
changes only when someone records something, then the gap between them is an accumulating
quantity, and it is an accumulating quantity of a specific kind: **information the reporting layer
owes and has not delivered.**

Read that way, several things stop being metaphors. Technical debt becomes off-balance-sheet
entropy. Deferred maintenance becomes an unrecognised liability with a measurable integral. And a
crisis stops being *necessarily* exogenous. Within this model a deferral has one available ending —
arrival — so the crisis is not a bolt from outside the system but the system's own accumulated
error, delivered at once because it can no longer be carried. In the world a deferral can also be
amortised, refinanced, forgiven or recognised gradually; the claim is about the ending this
structure forces, not about the only ending there is.

The claim that this reading is *useful* rather than merely evocative rests on it making
predictions, and the paper's structure follows from taking that obligation seriously:

- **§2** states the three propositions as propositions — truth-apt, deniable, with stated domains
  — rather than as a formalism asserted to be self-evident.
- **§3** treats the coupling Λ once, at full strength, and then stops. Λ has been this
  programme's most-attacked quantity; the defence is three legs long, it is deployed here, and it
  does not recur. An argument that keeps returning to one quantity tells a reader where the soft
  ground is.
- **§4** builds the filter and reports what it does.
- **§5** reports the severe test, which **failed**.
- **§6** states, plainly, what the framework may and may not now claim.

**Contributions.** Numbered, so that a reader is not obliged to construct a smaller list than the
one intended.

1. **An axiom set stated as propositions with domains** (§2), replacing an appeal to
   "first principles" that the earlier drafts of this programme made four times and never defined.
   Includes the test that separates a first principle from a result, and a demonstration —
   in committed code — that all three propositions are *deniable*.
2. **Λ relocated from posit to entailment** (§3). If P1 holds, a relation between the two
   components must exist; naming it invents nothing. This dissolves the standing objection at the
   root rather than at the perimeter.
3. **A measured invariance rather than an asserted one** (§3.3): every dimensionless diagnostic is
   bit-identical across twelve orders of magnitude of the coupling, and every dimensional one
   scales exactly linearly. The coupling is used in the code, and no conclusion depends on it.
4. **The filter model and its results** (§4): recognition lag scales with unobservability;
   deferred information is **exactly proportional to (1 − φ)**, derived in closed form and
   confirmed by simulation to a relative error of 10⁻¹⁵; and volatility is *relocated rather than
   suppressed* — the last of which corrects a prediction this programme previously made in the
   opposite direction.
5. **A pre-registered severe test of the framework's sharpest prediction, and its failure**
   (§5) — registered before the data were touched, replicated in a second sector declared in
   advance, controlled against a label-permutation null, powered at 0.95–1.00 against the effect
   size of interest, and lost. With the stopping rule honoured.
6. **A stated bridge discipline** (§6.2) arising from that loss: any identification of a model
   parameter with a measurable must itself be written as a numbered proposition a competent critic
   could deny. The failed registration did not have one, and that is the leading suspect.

**A word about §5, since its placement is deliberate.** The failed prediction is in the body and
in the abstract. It is not in *Abandoned Approaches*. A pre-registered prediction that was tested
and lost is a **result**; filing it under abandonments would be the softest available way to hide
it, and this paper has no claim on a reader's seriousness if it takes that route.

---

## 2 · Three propositions

### 2.1 · What a first principle is, and what it is not

The earlier drafts of this work appealed to "first principles" repeatedly and defined the term
zero times. The gap was not a wording problem, and several attempts to fix it by rewording failed
for a reason worth stating, because it is a type error and type errors do not respond to prose:

**An axiom is a proposition** — truth-apt, deniable, the kind of thing that can be false. **A
model is a structure** — it has interpretations, not a truth value. A structure cannot be promoted
to a proposition by describing it more emphatically. The tensor is not the axiom. **The axiom is
the proposition that wealth has the structure the tensor formalises.**

The second correction is that **"undeniable" must go.** An axiom nobody can deny is a definition,
and definitions generate no empirical content. The useful notion is the one from computing: a
**invariant** — never proved undeniable, proved *preserved*, within a **stated domain**. "Sound
within a stated domain" is a defensible claim. "Undeniable" is a self-defeating one.

The test that separates a first principle from a result: **denying a first principle produces a
different science; denying a result produces a wrong number.** Deny *r > g* and you have a
different empirical claim within the same science.

The example on the other side needs stating carefully, because the obvious version of it is a
strawman and an economist referee would stop on it. **Neoclassical economics does not deny physical
depreciation** — δK appears in every growth model from Solow forward, and claiming otherwise would
be an error of exactly the kind §6.2 is about. What P3 puts at issue is different and narrower:
whether an aggregate can be treated as a primitive carrying its own laws. Deny P3 — assert that an
aggregate production function is a fundamental object rather than a fold over units whose validity
requires conditions on the units — and the disagreement is not about a coefficient. It is about
what kind of thing the object of study is, and it changes which questions are well-formed. That is
what "a different science" is meant to pick out, and P3 rather than P2 is where this framework's
commitment actually bites. The three propositions below are offered as principles on that test.

### 2.2 · The propositions

> **P1 · Composition.** Every unit of wealth is a compound of a physical component and a claim
> component, obeying different laws — thermodynamic and arithmetic respectively.
>
> *Domain:* units of wealth having any physical referent. Silent on purely contractual objects
> whose referent is another claim.

> **P2 · Decay.** The physical component degrades absent maintenance. No store is inert.
>
> *Domain:* physical referents over horizons long relative to their maintenance cycle. Silent on
> the short run, where degradation is negligible against measurement noise.

> **P3 · Atomism.** Measured aggregates are folds over units. No aggregate is more fundamental
> than its constituents.
>
> *Domain:* any measurement presented as a property of an economy rather than of a population.
> This is the proposition an aggregate-production-function economist denies, and denies knowingly.

Three, not ten. Each is stated so that a competent economist can say *no* to it and mean something
specific by the refusal.

### 2.3 · The propositions are deniable, and this repository proves it

The claim that these are empirical rather than definitional is cheap to make and is usually made
by assertion. Here it is demonstrated, because the regimes in which each proposition fails are
committed, tested code rather than thought experiments:

- **P2 fails at complete maintenance.** Effective decay is the entropy rate *net of maintenance*,
  so a fully maintained asset has no dynamics at all and the model collapses to an identity. This
  is the regime in which "no store is inert" is simply not true, and it is reachable by setting one
  parameter.
- **The framework's own central mechanism switches off at φ = 1**, which is a separate and equally
  important point. Perfect observability annihilates the entire phenomenon: recognition lag 0,
  deferred information 0.0, coupling identically 1, zero recognition events. Note carefully what this does
  *not* say — P2 still holds at φ = 1, and the physical layer still decays (from E₀ = 100 to 0.031
  over 400 periods). What vanishes is the *gap*, and therefore everything this paper is about.
  A framework whose subject matter can be dialled to zero by an observability parameter is a
  framework making a claim about the world rather than a definition of it.
These regimes are not embarrassments to be hidden behind a stronger word. **They are the evidence
that the model has degenerate limits reachable by setting a parameter** — which is weaker than
proving a proposition about the world false, and is stated at that strength deliberately. What a
switch-off regime demonstrates is that the framework's subject matter is contingent on a quantity
that could take another value, which is the minimum a claim must satisfy to be empirical rather
than definitional. It is not itself a refutation, and no refutation is offered here.

*A companion result on the same theme, in a sibling paper of this programme, is cited rather than
reproduced: a levy whose base cannot observe an accrual is inert regardless of its rate. The
mechanism is the same — observability binds before intensity — and the evidence for it belongs to
that paper.*

### 2.4 · Independence

P1 concerns composition and is silent about time. P2 concerns time and presupposes only that a
physical component exists — it is not derivable from P1, since a compound whose physical component
were inert would satisfy P1 and violate P2. P3 concerns the relation between measurements at
different scales and is independent of both: an economy of inert single-component units would
satisfy P3 while violating P1 and P2. No proposition is derivable from the others, and each is
denied by an identifiable school.

---

## 3 · The coupling

*This section is where Λ is defended. It is defended here, at full strength, on three independent
legs, and then it is used for the rest of the paper without further apology. That is a deliberate
posture and it is worth naming: a defence that recurs is a tell. Five defences of one quantity
inform a referee that there are five soft places, and recruit attention to precisely the ground an
author would rather they walked over.*

### 3.1 · Λ is obliged by P1, not introduced

**Notation, stated before the argument because two different objects have been sharing one symbol
in this programme's working notes.** Write **C** for the claim component and **E** for the physical
component. Then:

- **λ = C/E** is **dimensionless** — a ratio of the claim measure to the physical measure once both
  are expressed in the same numeraire. This is the object §3.4 reports as a sawtooth, and it is the
  one with dynamics.
- **Λ = η·C/E** is **dimensional**, carrying units of currency per joule, where η is the numeraire
  conversion. This is the object the standing dimensional objection is aimed at, and the object
  §3.3 sweeps.

Conflating them is easy and this paper has done it before. Everything below is explicit about which
is meant.

**The entailment argument, and its actual reach.** If P1 holds, wealth is a compound of two
components measured in different units, so *some* relation between them exists in any unit of
wealth. That much is entailed and it does useful work: it establishes that the framework is not
smuggling in an extra object, and that asking "why did you introduce a coupling?" mistakes a
consequence for a choice.

**It does not, however, entail that the relation is a scalar**, and the standing objection is aimed
at the scalar. The relation could be state-dependent, non-stationary, set-valued, or not a function
at all — and P1's own wording, *obeying different laws*, is if anything a reason to expect that no
single constant suffices. So the honest version of this leg is narrower than the version this
programme has previously stated: **the existence of a coupling is entailed; its representability as
a scalar is an additional modelling assumption, and it is one this paper makes and does not
prove.** What follows in §3.3 is a demonstration that no conclusion here depends on the scalar's
*value*, which is a different and weaker guarantee than showing the scalar is the right object —
and the difference is exactly the kind of thing §6.2 will show this programme has previously
glossed over at its cost.

λ is not stable, and §3.4 shows what shape its instability takes.

### 3.2 · Λ⁻¹ is an indicator the United Nations already publishes

Energy intensity of output — the World Bank series *Energy intensity level of primary energy*
(`EG.EGY.PRIM.PP.KD`, MJ per unit of PPP GDP) — is formally **SDG indicator 7.3.1**, co-tracked by
the International Energy Agency, with global coverage and a long time series.

That series has **the dimensions of Λ⁻¹**, and the claim made here is exactly that and nothing
more. It is emphatically **not** that SDG 7.3.1 measures Λ⁻¹. The two differ in a way this paper is
obliged to name, since naming it is the discipline §6.2 arrives at the hard way: **Λ is a ratio of
two stocks** (a claim stock in currency over a physical stock in joules), while **SDG 7.3.1 is a
ratio of two flows** (annual primary energy over annual PPP output). Two quantities can share
dimensions and remain different quantities, and a paper that lost a pre-registered test to precisely
that error is in no position to commit it a second time in its own defence.

What survives the qualification is narrow and is still worth stating: **currency-per-energy is not
an exotic dimension and not this author's coinage.** An institution with no stake in this framework
tracks a quantity of that dimension against a global target, which places the construction outside
the position that proved fatal to Odum's emergy programme — transformity coefficients derived from
the accounting system that consumed them, and therefore unmeasurable from outside it. That is a
claim about *availability in principle*, not about measurement in fact.

**And it is a weaker leg than §3.3, which should be said plainly rather than left to a referee.**
If, as §3.3 demonstrates, no conclusion in this paper depends on the coupling's value, then
anchoring that value to a published statistic cannot be load-bearing for any result here. The two
legs answer different objections — §3.3 answers *"your findings are an artefact of a number you
made up"*, and this section answers *"the dimension you are working in is invented"* — and only the
first is doing work for the results. A reader who finds this section unconvincing loses nothing
downstream.

### 3.3 · The numeraire cancels — measured, not argued

The dimensional objection can be answered by algebra, and algebra is exactly what a sceptical
reviewer declines to take on trust. So the two-layer system of §4 is **dressed in units** — the
physical layer in joules at scale E₀, the claim layer in currency, the coupling η between them —
and the invariance is measured on the dressed system.

Sweeping η across twelve orders of magnitude, from 10⁻⁶ to 10⁺⁶ currency units per joule, at
**φ = 0.3, recognition mechanism live, 400 periods** (the diagnostics below are the same statistics
§4.4 reports, under **this paper's names**; the module and `scripts/wt002_lambda_report.py` call them
`variance_suppression`, `variance_concentration` and `n_crises`):

| diagnostic | value at every η | spread across the sweep |
|---|---|---|
| recognition lag | 22 | **0.0** |
| inter-event smoothing | 0.6097 | **0.0** |
| share of reported movement inside recognition events | 0.9199 | **0.0** |
| recognition events | 16 | **0.0** |
| relative event magnitude | 0.20138 | **0.0** |
| mean / min / terminal coupling ratio | — | **0.0** |

Not "within tolerance." **Bit-identical**, because the coupling never enters the recursion; it is
dressing applied afterwards.

That result alone would be worthless, and it is important to say why: it is trivially easy to
build a module in which nothing depends on a parameter *because the parameter is never used*. So
the positive half is what makes this a test rather than a tautology. The dimensional quantities
**do** move, and they move exactly as a unit conversion must:

| quantity | at η = 10⁻⁶ | at η = 10⁺⁶ | log-log slope |
|---|---|---|---|
| deferred information (currency) | 6.323144 × 10⁶ | 6.323144 × 10¹⁸ | **1.000000000000** |
| terminal Λ | 1.0 × 10⁻⁶ | 1.0 × 10⁺⁶ | **1.000000000000** |

η is used, the currency figures track it linearly to twelve decimal places, and no conclusion moves
at all. Both directions are mutation-tested: leaking η into the dynamics fails four tests, and
removing the scaling fails two.

**Scaling collapse.** Two systems differing in energy scale (1 J against 6.02 × 10²³ J) *and* in
coupling (10⁻⁶ against 42) lie on a single dimensionless curve — every diagnostic identical, pairwise
difference **exactly 0**, at φ = 0.3 over 300 periods. (The shorter horizon is inherited from the
verifier this figure comes from and is stated because it changes the values: at 300 periods the
system has had 12 recognition events rather than 16, and inter-event smoothing reads 0.6100 rather than
0.6097. The *collapse* is horizon-independent; the numbers collapsed onto are not.)

The sentence this licenses, and the paper will not need to say it twice: *the conversion
coefficient is a numeraire; every result reported here is invariant to it across twelve orders of
magnitude, while every currency-denominated quantity scales with it exactly linearly.*

### 3.4 · Λ is not a constant that wobbles; it is a sawtooth

A freely-varying Λ that is never pinned would forbid nothing, and a quantity that forbids nothing
is the free parameter this programme has refused five times in other costumes. So the claim is not
that Λ *varies*. It is that Λ varies **in a specific parameterised shape**, and the shape is a
prediction.

At φ = 0.3 over 400 periods, with the recognition mechanism live:

| | value |
|---|---|
| mean Λ | 1.136838 |
| minimum Λ | 1.000000 |
| maximum Λ | 1.245384 |
| recognition events | 16 |
| Λ = 1 exactly at every recognition event | **yes, all 16** |

**Λ equals its physical value only at the instants the claim layer snaps to the physical one, and
overstates it by ~14% on average in between.** Floor pinned at unity by construction of the
recognition event; ceiling set by observability; mean determined by φ. That is a shaped variable, not a
free one — and it is the picture of the assertion that Λ's drift *is* the accumulated deferred
information.

---

## 4 · The reporting layer as a filter

### 4.1 · The model

Two layers and one parameter that matters.

The physical layer decays at an entropy rate net of maintenance:

> **E(t+1) = E(t) · (1 − d·(1 − m))**

Of each true change, a share **φ** is *observable* — announced capital expenditure, a disclosed
impairment, a write-down someone had to sign — and reaches the claim layer immediately. The
remaining (1 − φ) is deferred maintenance and technical debt: real, accruing, and absent from the
statements. It accumulates in the gap and is recognised only at rate α per period:

> **C(t+1) = C(t) + φ·ΔE + α·gap(t)**,  **gap(t) = E(t) − C(t)**

When the unrecognised gap exceeds a threshold share θ of physical wealth, the deferral becomes
unsustainable and the claim layer snaps to the physical one. **That discontinuity is the crisis,
and its magnitude is exactly the information that had been withheld.**

*Terminology, fixed here and used consistently from this point.* The discrete event is called a
**recognition event** throughout, and where the referent is literally ASC 350 it is called an
**impairment loss**. It is deliberately **not** called a *correction*: in finance a correction is a
price decline of a specified magnitude from a peak, and in accounting ASC 250 — *Accounting Changes
and Error Corrections* — reserves the word for the repair of an **error**, which a change in
estimate driven by later information is not. An earlier draft of this paper used *correction* for
the event thirty times and would have asserted, in the technical register of the standard §5 is
built on, that the prior statements required retrospective restatement. The word **crisis** is kept
in the title and for the phenomenon the paper is *about*; the systemic, country-level sense used in
the banking-crisis literature is not intended anywhere here.

Throughout: E₀ = 100, d = 0.05, m = 0.6 (effective decay 0.02 per period), α = 0.05, θ = 0.25, 400
periods. Where the filter is examined in isolation the recognition mechanism is disabled (θ = ∞),
because otherwise the snap timing truncates the measurement window and the lag statistic reports
the recognition schedule rather than the filter.

**φ is not a fudge factor**, and the distinction is load-bearing enough to state before any
result. φ is the *observability of the degradation*, and it is what makes this model survive the
objection that would otherwise kill it outright — see §4.3.

### 4.2 · Result: lag and deferred information scale with unobservability

Filter isolated, θ = ∞:

| φ | recognition lag (periods) | inter-period smoothing | deferred information |
|---|---|---|---|
| 1.0 | 0 | 1.000 | 0.0 |
| 0.8 | 3 | 0.928 | 399.8 |
| 0.5 | 14 | 0.845 | 999.5 |
| 0.2 | 22 | 0.798 | 1599.2 |
| 0.0 | 26 | 0.791 | 1999.0 |

**Deferred information is exactly proportional to (1 − φ), and this is a closed form rather than a
simulation regularity.** With the recognition mechanism disabled, substituting
E(t+1) − C(t) = gap(t) + ΔE into the two recursions gives

> **gap(t+1) = (1 − α)·gap(t) + (1 − φ)·ΔE(t)**

so with gap(0) = 0 the gap at every t is (1 − φ) times its value on the φ = 0 path. Since ΔE < 0
throughout, every term shares a sign and the absolute integral inherits the factor exactly:

> **D(φ) = (1 − φ) · D(0)**,  D(0) = 1998.99 for the parameters above.

The simulation reproduces this to a relative error of 10⁻¹⁵ across φ, and the test suite asserts
it. **A doubling of unobservability doubles the integral of what the statements owe, exactly.**

The lag does not share that simplicity: it is sigmoidal in (1 − φ), rising slowly at first
(φ = 0.9 → lag 1), then steeply through the middle of the range (φ = 0.8 → 3, φ = 0.5 → 14), then
saturating (φ = 0.1 → 24, φ = 0.0 → 26). So the *quantity* of undelivered information is linear in
unobservability while the *delay* in delivering it is not, and the two should not be expected to
move together.

With the recognition mechanism live, recognition-event frequency at fixed observability (φ = 0.3)
sorts by
entropy rate:

| entropy rate d | sketch | recognition events in 400 periods |
|---|---|---|
| 0.01 | warehouse retail: re-provisions on a decade | **0** |
| 0.05 | industrial | **16** |
| 0.20 | software: faces zero-days continuously | **100** |

The contrast between a warehouse retailer and a firm exposed to continuous obsolescence is
therefore a **position in a parameter space**, not a rhetorical flourish. Two firms with identical
observability and different entropy rates live in different worlds, and the model says by how much.

### 4.3 · The forward-looking-markets objection, and why the φ = 1 reply does not survive

The strongest standing objection to any lag thesis is efficient-markets in its plainest form:
prices already discount deferred maintenance, so a systematic lag should not survive. Note that a
**pure-delay** model has no answer to this and is straightforwardly falsified by cases where
financial signals *lead* physical change — markets price an announced technology transition before
a single unit of capital is built, and such cases obviously exist.

This model is not a pure-delay model, and the asymmetry is the whole mechanism. **The claim layer
leads on what is disclosed and lags on what is deferred.** At φ = 1 the filter is a perfect window:
zero lag, zero deferred information, coupling identically 1, no recognition events. So the objection holds
*exactly* where the model predicts no lag, and has nothing to act on where degradation is
undisclosed. The two are not in competition; they partition the space by φ.

**That reply is not available to this paper, and the rest of this section retracts it.**

The partition is drawn along φ, and φ is not measured anywhere in this work — Limitation 4 concedes
it is swept, not estimated. So "the objection holds where φ is high and the model holds where φ is
low" concedes every case an efficient-markets reader could check and claims every case nobody can,
along a coordinate no one has observed. That is a free parameter absorbing an objection, which is
the move this programme has refused five times in other costumes (§7) and should have refused here.

The requirement was recognised before the severe test was run and was written down: a framework
conceding everything the efficient-markets reading claims and retaining only the unobserved residue
**must be able to identify that residue in the world**, with evidence rather than assertion. §5 is
the attempt to supply that evidence. It failed.

**So §4.3 is an open problem, not a reply.** The asymmetry remains a coherent structure and a
genuine improvement on pure delay — a pure-delay model is refuted outright by observed leads, and
this one is not. But until φ is independently measurable the asymmetry cannot be used to answer
the efficient-markets objection, and this paper does not use it that way. §4.1's assertion that φ
is not a fudge factor rests on the argument in this section; with that argument withdrawn, the
assertion is a statement of intent about how φ is to be treated, and it should be read as one.

### 4.4 · Result: volatility is not suppressed, it is relocated

This programme previously predicted that the claim layer would be *smoother* than the physical one.
Measured across a whole path, **that prediction is false wherever the mechanism is actually
active**: at φ = 0.5, 0.2 and 0.0 the full-path ratio of reported to physical volatility is 1.56,
2.71 and 3.27 — the claim layer is *more* volatile, because the recognition events dominate the variance.
The prediction survives only at φ ≥ 0.8, where the gap never reaches the recognition threshold and
there are no recognition events to dominate anything; there the ratio is 1.00 and 0.93. **So the original
claim was not merely wrong, it was right only in the regime where the model has nothing to say.**

The true behaviour is more interesting than the prediction it replaced. Measured with the
recognition mechanism live, the claim layer is far smoother than the underlying **between**
recognition events, while the share of all reported movement occurring **inside** recognition events rises
toward one:

| φ | inter-event smoothing | share of reported movement inside recognition events | events |
|---|---|---|---|
| 1.0 | 1.00 | 0.00 | 0 |
| 0.8 | 0.93 | 0.00 | 0 |
| 0.5 | 0.80 | 0.69 | 8 |
| 0.2 | 0.52 | 0.96 | 19 |
| 0.0 | 0.35 | **0.99** | 25 |

At zero observability, **essentially every reported movement is a recognition event.** The signature is
therefore not a quiet system but one that is quiet for long intervals and then abruptly is not —
which is a more recognisable description of the historical record than uniform smoothing.

**The qualitative result is not new and is not claimed here.** Bleck and Liu stated it in 2007:
historic cost accounting "stabilizes asset prices in the short term. Under the veil of this apparent
stability, volatility actually accumulates only to hit the market at a later date," transferring
volatility across time and raising it overall. **What the table above adds is the parameterisation** —
the same claim indexed by a continuous observability parameter, with the smoothing and concentration
measured separately rather than argued. The provenance and the difference in mechanism are set out in
§9; it is noted here because the table's headline result is nineteen years old.

**It is not, however, a usable empirical target.** Against the accounting data available to this programme the concentration
statistic is unfalsifiable by construction: the asset class with no amortisation schedule has
essentially all of its recognised change arrive discretely *as a matter of accounting definition*,
not of firm behaviour. A test of that is a test that cannot fail, and a test that cannot fail is
not a test. It was excluded from this programme's pre-registrations on exactly those grounds
before either was run. The relocation result is therefore a property of the model and a candidate
description of the world, and it is **not** offered as the replacement severe test. The framework
does not currently have one.

*Method note, because the fix mattered more than the result.* The original metric measured the
wrong object: one number was being asked to carry two claims. Two now exist — smoothing measured
on the periods between recognition events, concentration measured on the recognition events — because a statistic that
answers two questions answers neither.

---

## 5 · The severe test: registered, run twice, and lost

### 5.1 · What was predicted, and when

§4 establishes a property of a model. Whether the property holds of the world is a separate
question, and this programme's assessment was — and remains — that no amount of prose does the
work of one empirical result. The framework's sharpest available prediction is the one that
follows directly from §4.2:

> **Recognition lag scales with the unobservability of degradation.**

To test it, unobservability must be identified with something measurable. The identification
chosen was **GAAP asset class**, on the reasoning that the categories accounting standards decline
to place on an amortisation schedule are precisely the categories whose degradation is hardest to
observe. The classes and their schedules are those of the FASB *Accounting Standards Codification*:
Topic 360 for property, plant and equipment, Topic 350 for intangibles and goodwill — where the
indefinite-lived classes are tested for impairment rather than amortised, which is what makes the
recognition moment discretionary — and Topic 280 for the segment disclosures §8 identifies as the
unit of observation this test did not have. That yields a four-tier ordering, predicted in advance to be monotone in lag:

| tier | asset class | predicted |
|---|---|---|
| 0 | property, plant and equipment | shortest lag |
| 1 | finite-lived intangibles | ↓ |
| 2 | indefinite-lived intangibles | ↓ |
| 3 | goodwill | longest lag |

**The registration preceded the data.** PRE-001 was committed **alone**, at commit 9722342, and
pushed, before any lag was computed; the analysis code did not yet exist. The git history is the
timestamp, and it is the entire evidence that the prediction preceded the outcome — which is why
the registration and the code were deliberately not batched into one commit.

**A disclosure, because the discipline just described does not fully cover the test this paper
reports.** PRE-001 timestamps the *prediction*. The result reported in §5.3 comes from PRE-002,
which specifies a different *instrument* — and PRE-002's registration shipped in the same commit
(d655501) as the implementation of that instrument. The result itself came later, at a subsequent
commit, so the git history still establishes that PRE-002 was registered before its outcome
existed. What it does **not** establish is that the instrument's details — the onset rule's window,
the tie-break direction, the materiality floor — were fixed before anyone had seen what they
produced. On a second look, that is precisely where the remaining researcher degrees of freedom
live.

No claim is made here that they were exploited, and the author's account is that they were not.
The point is that this is an *account* rather than a demonstration, whereas for PRE-001 it is a
demonstration. A reader is entitled to weight the two differently, and this programme now requires
that a registration precede the **instrument's code**, not merely the result — a rule it did not
have when PRE-002 was written.

### 5.2 · The first instrument failed, and so did its diagnosis

The first test (PRE-001) returned a null in both universes, and the two nulls did not even agree
with each other. The Jonckheere–Terpstra statistic sums the pairwise Mann–Whitney counts across the ordered tiers, so a
tier ordering carrying no information returns z near zero from either direction — which is what happened,
twice, in opposite directions. The pilot retained 120 events across 72 firms and gave Jonckheere–Terpstra
**z = −0.177** (one-sided p = 0.570), with goodwill's median lag sitting *below* PP&E's — 4.0
quarters against 5.0, the reverse of the predicted ordering. The replication universe, declared in
the registration before the pilot was run, retained 202 events across 106 firms and gave
**z = +0.634** (p = 0.263), with goodwill and PP&E tied at 3.0. A weak negative and a weak positive,
neither significant: the signature of a measurement carrying no information about the ordering
rather than of an effect in either direction.

The instrument was then examined, and it had a defect. Across the 322 events retained by both
universes combined there was **zero right-censoring**, 69% of pilot lags fell at six quarters or
fewer, and **1,047 charges were discarded for having no measurable onset**. An onset rule requiring
an unbroken decline in a firm-level signal measures the volatility of that signal, not the
phenomenon: the rule can only find an onset when the signal happens to fall monotonically, which is
common over short windows and vanishingly rare over long ones. The lag distribution was therefore
pinned against a ceiling the instrument itself imposed.

**This diagnosis was not permitted to rescue the result.** A second, **separately numbered**
registration (PRE-002) was written with a different onset instrument (peak-to-charge), a
label-permutation negative control, a power curve to be reported whatever happened, α tightened to
0.025 for the second look, and — decisively — an explicit **stopping rule** stating in advance that
there would be no third instrument.

### 5.3 · The second instrument worked, and the prediction failed anyway

**Pilot — retail trade (SIC 5200–5999).** 244 events across 121 firms.

| tier | n | median lag (quarters) | IQR | mean |
|---|---|---|---|---|
| 0 · PP&E | 21 | 5.0 | 3.0–9.0 | 7.05 |
| 1 · finite-lived intangible | 34 | 4.0 | 1.0–8.0 | 5.71 |
| 2 · indefinite-lived intangible | 34 | 5.5 | 1.2–9.0 | 6.12 |
| 3 · goodwill | 155 | 5.0 | 1.0–9.0 | 5.93 |

Jonckheere–Terpstra **z = −0.290**, permutation p = **0.590**. median(t₃) − median(t₀) = **0.0
quarters**, CI [−4.0, +2.0].

**Replication — computer and data processing services (SIC 7370–7379).** 444 events across 190
firms.

| tier | n | median lag | IQR | mean |
|---|---|---|---|---|
| 0 · PP&E | 34 | 5.0 | 1.2–9.8 | 6.62 |
| 1 · finite-lived intangible | 102 | 4.5 | 1.2–10.0 | 6.12 |
| 2 · indefinite-lived intangible | 46 | 6.0 | 2.2–11.0 | 6.85 |
| 3 · goodwill | 262 | 5.0 | 1.0–10.0 | 6.46 |

Jonckheere–Terpstra **z = −0.095**, permutation p = **0.520**. median(t₃) − median(t₀) = **0.0
quarters**, CI [−4.0, +2.5]. Four registered sensitivity analyses per universe are in the run logs;
none reverses the verdict.

**The instrument was demonstrably better this time, and that is what makes the null bite:**

| | PRE-001 (streak onset) | PRE-002 (peak onset) |
|---|---|---|
| events retained, both universes | 322 | **688** |
| charges discarded for no onset | **1,047** | **0** |
| right-censored | 0% | 7.8% pilot, 14.2% replication |
| pilot IQR width, tier 3 | 3.0–7.0 | 1.0–9.0 |

The lag distribution now spans the registered range instead of piling against a ceiling imposed by
signal volatility, and censoring is non-zero — which is what an instrument capable of observing
long lags looks like.

**Negative control.** Tier labels permuted 1,000 times with the lag distribution held fixed:

| universe | null z mean | null z sd | observed z | empirical p |
|---|---|---|---|---|
| pilot | +0.007 | 1.025 | −0.290 | 0.590 |
| replication | −0.002 | 1.000 | −0.095 | 0.520 |

The permutation distribution is centred on zero with unit spread in both universes. The pipeline
does not manufacture a gradient, and the empirical p-values do not lean on a normal approximation,
so they are untroubled by tier sizes of 21/34/34/155.

**Power, reported because a null without its detectability attached is not a result:**

| true effect | power, pilot | power, replication |
|---|---|---|
| 0.5 quarters per tier | 0.65 | 0.87 |
| **1.0 quarter per tier** | **0.95** | **1.00** |
| 2.0 quarters per tier | 1.00 | 1.00 |

**This design would have detected a one-quarter-per-tier gradient with 95% probability in retail
and with certainty in computer services, and it found nothing.**

Three qualifications belong immediately next to that sentence rather than in a limitations section,
because without them it would be overstated:

1. **The power simulation assumes the onset instrument measures lag without error.** It resamples
   the observed lag distribution and adds a noiseless per-tier shift. The peak rule always finds an
   onset — which is why zero charges were discarded, and which is a property of the rule rather
   than proof of its quality. Any measurement error in the onset attenuates a true gradient, and
   the reported power does not model that attenuation. The true power is therefore lower than
   0.95–1.00, by an unquantified amount.
2. **The 688 events come from 311 firms**, and the test statistic, the permutation control and the
   power simulation all treat events as independent. The effective sample is smaller than 688 and
   the reported power is an upper bound.
3. **One quarter per tier was never derived from the model.** It is a plausible round number, not a
   minimum interesting effect computed from the framework — and it could not have been, because
   deriving one requires the very φ-to-tier bridge that §6.2 concludes was unsound. A design cannot
   be well-powered against an effect size the theory never specified.

**What the result supports, stated at the strength the evidence carries:** a well-powered,
pre-registered, replicated test found no gradient, and if a gradient of the size tested exists it
is unlikely to have been missed twice. **What it does not support** is the stronger reading that
the framework's own predicted effect has been ruled out, because the framework never named that
effect in the units the test measured. Calling this *evidence of absence* — as an earlier draft of
this section did — would contradict §6.2 in the same paper: the bridge cannot be too broken to
license a prediction and sound enough to license its refutation.

**The shape of the failure, stated as sharply as the data allow.** Both z-statistics are negative,
meaning the point estimates ran *opposite* to the predicted ordering in both universes, as they had
in the PRE-001 pilot. And the ladder does not merely fail to be monotone — it is wrong in a
specific and instructive place: **tier 2, indefinite-lived intangibles, carries the longest median
lag in both universes, with goodwill sitting below it** (5.5 against 5.0 in the pilot, 6.0 against
5.0 in the replication). A four-rung ladder whose *third* rung is the tallest cannot be rescued by
appeal to the top rung's behaviour, and no reading of the tier ordering as a noisy version of the
predicted one survives that pattern.

**The stopping rule fired.** There is no third instrument. A hypothesis that requires one on the
same data is a hypothesis being fitted.

---

## 6 · What may now be claimed, and what may not

### 6.1 · The demotion, stated exactly

**Not supported:** that recognition lag scales with the unobservability of degradation, where
unobservability is identified with GAAP asset class, in US-listed retail trade or computer and
data processing services over 2013–2024, at the firm level, at effect sizes of one quarter per
tier or larger.

**Unaffected:** every result in §3 and §4. Those are properties of a stated model, established by
simulation and held in place by a test suite. A model result is not made false by the failure of
an empirical identification, and it is not made true by one either.

**And that sentence is a problem, not a reassurance.** If nothing in §3 or §4 was at risk, then
nothing in §3 or §4 was on test — and a framework that retains every claim after losing its only
public bet is in exactly the position §6.3 accuses Odum's of occupying. The accounting is therefore:

- **What was at risk and lost:** the conjunction of the model, the bridge, and the firm-level unit
  of observation. That conjunction was the framework's *entire empirical content* as of this
  writing. It is gone.
- **What was never at risk:** everything in §3 and §4, because those are theorems about a
  simulation. They were never capable of losing and no result of the severe test could have
  retracted one of them. Calling them "unaffected" states a fact about their logical type, not a
  survival.
- **What follows:** **the framework currently has no confirmed empirical claim.** It has a model
  with derived consequences, one registered prediction that failed, and a stated method for
  building the next one. A reader who wants to know what this paper has established about the
  world should read that list literally.

The framework would have been *confirmed* had the gradient appeared; it was not, and the correct
posture is not that the theory survived but that the theory has not yet been given a test it can
pass. Designing one is §6.2's business and it is unfinished work, not a conclusion.

**Demoted:** the lag-scaling claim moves from *a prediction the framework makes* to *a prediction
the framework made, at one level of aggregation, with one bridge, and lost.* Any surviving version
must state its measurable and its bridge before it is tested again.

Three post-hoc conjectures about where the conjunction broke are recorded in the repository's
working notes. They are excluded from this paper's argument deliberately: **each arrived after the
number, none is evidence for anything, and any of them that is ever tested must be registered from
scratch.** One is worth naming here only because it generalises into a discipline rather than a
defence, and that is §6.2.

### 6.2 · The bridge discipline

The registration contained a tier table and no **bridge proposition**. It never wrote down, as a
deniable claim, the sentence connecting the model to the world:

> *φ, the observability of degradation, is identified with the presence or absence of a GAAP
> amortisation schedule, because…*

Had that sentence been written, its weakness would have been visible before the data were touched.
The observability of *degradation* and the observability of the *accounting treatment* are
different quantities, and they may even be anti-correlated: goodwill carries no schedule, but its
impairment is triggered by conspicuously public signals — a share-price fall, a missed segment, a
lost contract. The physical condition of a distribution centre carries a schedule and is visible to
essentially nobody outside the firm.

**The general form of the error is a type error in a second costume.** §2.1 recorded one: a
structure cannot be promoted to a proposition by rewording. This is its empirical twin — **a
quantity in the model was matched to a quantity in the world that shares its name and not its
meaning.** The lesson is not about accounting. It is that a bridge from a parameter to a measurable
must itself be stated as a proposition and checked, and this programme now requires it of every
registration.

### 6.3 · The comparison this paper is not entitled to make

An earlier draft of this section argued that the framework had escaped the trap that closed on
Odum's emergy programme — that emergy's fatal defect was making no risky predictions, and that
losing a registered bet therefore counted as a kind of methodological success.

That argument is withdrawn, and the reason it is withdrawn is worth more than the argument was.
It selects its own reference class: introduce a comparator that made no predictions and any loss
becomes a comparative victory. It is an assessment of the author's conduct rather than of the
world, and it arrives at the end of the section reporting the failure, so it would be the last
thing a reader carried away from it. A paper does not get to grade its own integrity; a reader
grades it, or does not.

What remains after the withdrawal is a fact and not an evaluation. **A prediction was registered
before the data were seen, it was tested, and it failed.** Whether that is worth anything is a
judgement this paper leaves to whoever is reading it.

---

## 7 · Abandoned approaches

*Every route below was actually taken and then abandoned. The section is placed in the body, not an
appendix, for the reason given in the companion papers of this programme.*

**"First principles" as undeniable truths.** The original formulation asserted the framework's
foundations were undeniable. Abandoned on the argument of §2.1: an undeniable axiom is a
definition, and definitions forbid nothing. Several attempts to repair it by rewording failed
before the type error was identified, and that failure is instructive — a wording problem responds
to wording, and this one did not.

**The pure-delay reading of the reporting layer.** The claim layer as a simple lag on the physical
one. Abandoned because it is falsified by any case where financial signals *lead* physical change,
and those cases plainly exist. Replaced by the asymmetry of §4.3, which is strictly sharper: it
predicts *where* the lead-versus-lag boundary falls rather than denying that leads occur.

**The over-smoothing prediction.** §4.4. The framework predicted the claim layer would be less
volatile than the physical layer. Measured over a whole path this is **false**, and the probe
caught it. Retained here in full rather than quietly replaced, because the shape of the failure is
informative: the direction was wrong, the mechanism was right, and the corrected claim
(relocation, with 99% of reported movement occurring inside recognition events at φ = 0) is stronger than
the one it replaced.

**The streak-onset instrument (PRE-001).** §5.2. A genuine methodological dead end and the one part
of the severe-test story that belongs in this section: an onset rule requiring an unbroken decline
in a firm-level signal measures that signal's volatility rather than the phenomenon, which is why
1,047 charges were discarded and zero events were censored. *The failed prediction itself is not
here — it is in §5, in the body, and in the abstract, because it is a result.*

**Re-specifying the onset rule until it worked.** After PRE-002 also failed, a third instrument was
available and was not built, because PRE-002's stopping rule had been registered in advance.

**Answering the efficient-markets objection with φ.** §4.3. This was the paper's reply to its most
serious standing objection until the severe test removed its support, and it is abandoned in §4.3
rather than defended. It is listed here as well because the failure mode is the general one this
programme keeps meeting: an unmeasured parameter partitioning a space so that the objection lands
only where nothing can be checked.

**Estimating φ from the reported series alone.** The obvious route to closing §4.3's gap — fit the
model's parameters to an observed reporting layer and read φ off the fit. Abandoned because the
recovery is ill-conditioned by construction rather than by bad luck: φ reaches the observable only
through the product φδ, so estimating it means dividing by an effective decay rate that is itself
being estimated, and the variance grows like 1/δ². Limitation 4 gives the algebra and the measured
degradation. The route is recorded because its failure identifies its own successor, and the
successor has two handles rather than one: **φ becomes tractable as δ grows, and — at any δ — as δ
is known more precisely from outside the reported series.** Fast-decaying assets are therefore
partly self-rescuing, since at the top of the range tested φ recovers usably even with δ estimated
jointly; slow-decaying assets are not, and for those an independent δ is the only handle available.
What that independent determination should be is deliberately *not* specified here — an instrument
named in a paper before it is registered is an instrument that has escaped its registration.

**Adding a free parameter to absorb an objection.** Refused five times across this programme and
worth recording as a class, since each instance looked locally reasonable: introducing a scaling
constant to rescue the dimensional argument; defining a levy's base so a companion paper's claim
came out right; letting λ vary freely rather than in a shaped way; and, as §4.3 now concedes,
leaning on an unmeasured φ. A quantity that can accommodate any observation forbids nothing.

---

## 8 · Limitations

1. **The severe test failed and this paper does not know why.** Three post-hoc explanations exist —
   the theory is wrong; the bridge was wrong; the unit of observation was wrong — and **the data do
   not distinguish them.** The first is listed first on purpose, being the one the author has the
   strongest incentive to list last.
2. **The unit mismatch is real, unfixed, and was unfixed by both registrations.** The impairment
   charge is asset-level; the deterioration signal used was firm-level. A firm can impair a failing
   reporting unit while consolidated revenue rises. Fixing this requires segment-level disclosures
   and is a different project with a different registration — which **may not cite the present
   failure as support for anything.**
3. **The filter model is deterministic and single-firm.** No stochastic degradation, no
   heterogeneity, no interaction between firms, no market. Every empirical signature it suggests is
   therefore a qualitative target, not a fitted one.
4. **φ, α and θ are not measured. They are swept — and for φ there is a specific reason why, worse
   than the bare concession it replaces.** The paper reports how outcomes vary across the sweep and
   does not claim any firm's φ is known. An attempt to close that gap directly — estimating the
   parameters by fitting the model to a reported series — establishes that **φ is severely
   ill-conditioned when estimated jointly with the effective decay rate.**

   Write **δ = d(1 − m)** for the effective decay of §4.1 (entropy rate net of maintenance;
   δ = 0.02 at the parameters used throughout). Substituting ΔE = −δ·E(t) collapses the two
   recursions to a single line:

   > C(t+1) = C(t)·(1 − α) + E(t)·(α − φδ),  E(t) = E₀(1 − δ)ᵗ

   **φ reaches the observable only through the product φδ.** The series identifies α, δ and the
   composite k = (α − φδ), so recovering the parameter of interest requires **φ = (α − k)/δ** — a
   division by δ, giving an estimator whose variance grows like 1/δ² as δ → 0.

   On synthetic data (φ ∈ [0.1, 0.9], δ ∈ [0.005, 0.035], identical batch and iteration budget for
   both arms) the effect is large: with δ estimated jointly, φ recovers with a **median absolute
   error of 0.211** (p90 0.644); with δ **pinned at its true value**, **0.00073** (p90 0.017) — a
   291-fold improvement in the median. A noise-free series gives 0.211 as well, so noise is not the
   explanation.

   **Two qualifications, both of which cut against the strong reading.** First, this is a
   *conditioning* result and not a non-identifiability one: φ remains identifiable in principle at
   every δ > 0, and recovery degrades continuously rather than at a cliff. Bucketing the δ-free
   fits by true δ across [0.005, 0.010), [0.010, 0.017), [0.017, 0.025) and [0.025, 0.035) gives
   medians of 0.468, 0.468, 0.164 and **0.017** — but p90s of 0.773, 0.727, 0.462 and **0.212**.
   So at the top of the range the *typical* firm's φ is recovered to about 2% of its span while one
   firm in ten is still off by more than a quarter of it, and the median alone would overstate the
   case. Second, the quoted range of δ sits mostly in the poorly conditioned region, so the headline
   0.211 should be read as characteristic of slow-decaying assets and not of the model generally.

   **Pinning δ helps most where it is needed least.** At the sector sketches of §4.2, converted to
   effective decays and with δ pinned: software (δ = 0.080) recovers φ to a median 0.00026 and p90
   0.00078; industrial (δ = 0.020) to 0.00054 and 0.00367; **warehouse retail (δ = 0.004) to a
   median 0.00433 but a p90 of 0.191** — so even in the best case the slowest-decaying assets
   retain a bad tail.

   The consequence for this paper's construction is stated rather than softened: **a usable
   estimate of φ requires an independent determination of the physical decay rate, obtained outside
   the reported series — and for the slowest-decaying assets, φ may not be usefully recoverable
   even then.** Until such an estimate exists, φ is a swept parameter and every result depending on
   its value is a conditional statement. (Method, scripts and full figures:
   `docs/notes/NOTE-001-phi-identifiability.md`. Synthetic data only. It is **not** evidence about
   §5's null, which used an entirely different, non-parametric estimator.)
5. **Λ⁻¹ and SDG 7.3.1 are the same quantity dimensionally, not empirically.** The SDG series is a
   national aggregate over primary energy and PPP output; the model's coupling is a firm-level
   ratio between a physical capacity measure and a claim measure. The correspondence licenses "this
   dimension is one institutions already report," not "this series measures the model."
6. **P1's domain excludes purely contractual objects** whose referent is another claim, and a large
   share of modern financial wealth is precisely that. The framework applies to the base of that
   stack, and the composition of layers above it is a question this paper does not address.
7. **A Duhem–Quine problem is present and is narrower than the usual invocation.** A failed test
   here cannot distinguish a false theory from a bad observability proxy — that is genuine, and §5
   is an instance of it. It should not be confused with heterogeneity in entropy rates across
   industries, which is an ordinary identification problem with ordinary remedies and not a
   philosophical one.
8. **The framework claims necessary conditions, not uniqueness.** Any adequate account must
   distinguish physical from claim components, must let the second lag the first asymmetrically,
   and must make the residue accumulate. This construction satisfies those conditions; it is not
   argued to be the only one that does.

---

## 9 · Relation to existing work

**Soddy** is the origin of the composition claim and P1 is his observation made axiomatic. The
present contribution is not the distinction between physical wealth and claims on it but its
*dynamics*: that the gap between them is an accumulating quantity with a measurable integral and a
characteristic release.

**Georgescu-Roegen is a hostile witness inside this framework's own bibliography, and the paper
states so.** He is the most-cited authority in the biophysical
tradition this work draws on, and he explicitly refused the physical-to-monetary reduction that a
naive reading of Λ proposes: for him the source of economic value is the subjective enjoyment of
life. That refusal is not answered here — it is *adopted*. Measuring the wedge between physical
throughput and financial claims does not assert that energy determines value. It measures the gap
Georgescu-Roegen said would exist, and treats its drift as the object of study. On this reading he
is not an obstacle to the construction but the reason the construction measures a wedge rather than
proposing a conversion.

**Piketty is not contradicted; he is relocated.** The datasets and the rigour are not in question.
The disagreement is about *layer*: those measurements are taken on the claim component — the
financial abstraction — and are, on this framework's reading, silent about the physical component
beneath. *r > g* may hold exactly as described at the abstraction layer while saying nothing about
the atomic one. This converts the relationship from refutation into a **scope statement**, which
makes the two accounts complementary rather than rival.

**Austrian business cycle theory shares this framework's architecture while disagreeing about its
cause, and that is worth more than agreement would be.** Hayek's knowledge problem holds that
prices transmit dispersed information and that the characteristic failure is *informational* rather
than moral; §4 is a formalisation of exactly that concern. Mises's malinvestment — misallocated
capital accumulating unrecognised through a boom, revealed and liquidated in the bust — is
structurally identical to §4.4: unrecognised accumulation followed by discontinuous recognition event.
The causes assigned differ (credit expansion there, undisclosed physical degradation here) and the
claim made here is a structural analogy, not an identity. What it offers is a single mechanism
reproducing a phenomenon that mutually hostile traditions each describe in their own vocabulary.

**Stock-flow consistent macroeconomics** (Godley and Lavoie) shares the insistence that accounting
identities constrain dynamics. The difference is what the accounts are taken to *be*: consistent
and complete there, consistent and **systematically incomplete** here, with the incompleteness
being the object of study.

**The efficient-markets literature**, in Fama's canonical statement of it, supplies the objection §4.3
answers — and, as §4.3 now concedes, does not yet receive an answer. What the model offers is a
partition rather than a refutation: the model concedes disclosed information entirely and retains
only the undisclosed residue.

**The stock price crash risk literature is this paper's nearest neighbour, it arrived twenty years
earlier, and the concession owed to it is larger than the contribution claimed against it.** Jin and
Myers model a firm whose insiders absorb firm-specific bad news up to a limit and then, when a long
enough run of it arrives, give up and release the accumulated stock at once; the frequency of large
negative firm-specific return outliers rises with how opaque the firm is to outsiders. Hutton, Marcus
and Tehranian supplied the firm-level opacity measure and the panel, and an active literature has
extended both continuously since. **That is §4.4 in a different vocabulary, and on evidence this
paper is much the weaker of the two accounts**: crash risk is measured on prices, tested on large
panels and supported, while §4 is a property of a simulation whose one registered prediction failed.
The asymmetry is theirs before it is this paper's, too — their COUNT measure nets downside outlier
frequencies against upside ones and their COLLAR trade shorts a call against a put, so the
crash-not-jump direction is already inside the quantity they measure.

**And the concession runs one step further than the paragraph above, into a case Jin and Myers
themselves set out and this paper claims no priority over.** Before their model begins, they consider
an opaque firm run by "a saintly manager who always acts in shareholders' interest, never taking a
dollar more or less than deserved," and ask what such a firm's returns look like. Their third
possibility is this paper's mechanism:

> "If a stable lag is implausible, think of good or bad news accumulating within the firm until the
> difference between intrinsic value and share price reaches a critical value. The news would then be
> released all at once, like a pressure vessel letting off steam."

**Accumulation to a threshold and release all at once, with the agency conflict switched off, was
written down in 2004.** No claim of priority over it is made here, and an earlier draft of this
section made one.

**What that case retains, and §4 removes, is an informed party.** "Saintly" qualifies capture and not
information: the manager still observes the hidden component, and it is *investors* who "cannot see
the news as it happens." Their friction is verifiability toward outsiders; §4's manager knows no more
than the market does. **Deliberately withheld known news, honestly held unverifiable news, and
unrecognised unknown degradation are three objects, and only the third is §4's.** Two further
differences follow from the same page rather than from a defence of it. Their case is **two-sided** —
"good or bad news accumulating," against a threshold on a signed difference — and they assign it long
tails rather than crashes, entering kurtosis as a control variable against which their agency-driven
crash results are then identified. And it has no accounting layer of any kind; the working paper
contains no occurrence of *goodwill*, *intangible*, *impair*, *GAAP*, *book value* or *historic
cost*. The operating asset neither depreciates nor is reinvested in by declared assumption, and the
footnote attached to that assumption concedes only depreciation "according to a pre-defined
schedule" — which, being common knowledge, enters value and price identically and opens no wedge at
all.

That epistemic difference is observationally fragile. From the price's point of view a wedge that
widens because someone will not speak and a wedge that widens because nobody yet knows resolve
identically, and the obvious discriminating tests cut against §4 rather than for it: deliberate
withholding predicts correlation with insider incentives, insider selling, litigation exposure and
regulatory regime, and the post-SOX dissipation Hutton, Marcus and Tehranian report is exactly that
pattern.

**The trend the agency account is losing its grip on is nonetheless real, and it is where a mechanism
without a lying manager would matter if one were established.** Andreou, Lambertides and Magidou
document that idiosyncratic crash occurrences among US-listed firms rose from 5.5% of firm-years in
1950 to 27% in 2019 — 23% across the CRSP universe and 27% once the sample is narrowed to
CRSP–Compustat–Execucomp — while the opacity– and overinvestment–crash relations they test come back
non-significant, particularly in the period after Sarbanes–Oxley. Hutton, Marcus and Tehranian report
the same dissipation in their own abstract. Those authors read their own nulls as the *conduct*
declining rather than the explanation failing, and this paper does not recruit them against that
reading. **What the trend establishes is that the space is open, not that §4 occupies it.**

**Two things must be conceded here, or §4's claim is not narrow but wrong.**

**The first is that §4's asymmetry is assumed and not derived, and that the thing which would derive
it belongs to someone else.** Jin and Myers obtain one-sidedness from symmetric primitives: the
quantity of good news insiders can absorb is unbounded because they can capture it, and the quantity
of bad news is not, so the bound is one-sided for a reason internal to the model. §4 assumes a
physical layer that only degrades. That assumption is not by itself sufficient — degradation at a
stochastic rate around a booked rate produces a two-signed reporting error, which is Jin and Myers'
case again, long tails and no skew. What makes the wedge one-signed is a second condition, that
reported value may fall and may not rise: no upward revaluation of property, plant and equipment, no
impairment reversal for goodwill or indefinite-lived intangibles. **That condition is conditional
conservatism, it is Basu's object, and §4 uses it as machinery rather than contributing it.** An
earlier draft of this section cited Basu as an obstacle to be scoped around. He is not the obstacle;
he is the part of the mechanism this programme had not noticed it was standing on. §4's claim is
correspondingly restricted to degradation on which conservatism has nothing further to bite —
carrying no impairment trigger, no estimable expected loss and no observable event to key recognition
to. Where a loss is estimable, recognition is faster than the market and §4 predicts nothing.

**The second is that the reported layer accumulating hidden deterioration and releasing it as a price
crash is a published result, and §4.4 quantifies it rather than discovering it.** Bleck and Liu model
the accounting regime itself: historical cost gives management a "veil," poor performance
"accumulate[s] and only eventually materialize[s]," and greater opacity produces more frequent and
more severe crashes. Their statement of the volatility result is §4.4's, nineteen years earlier and
in prose — historic cost "stabilizes asset prices in the short term. Under the veil of this apparent
stability, volatility actually accumulates only to hit the market at a later date," transferring
volatility across time and raising it overall. **§4.4's contribution is the parameterisation, not the
finding.** Their manager, however, is strategic and fully informed, keeping a project alive for a
private benefit while knowing it will not recover, and their regimes are two discrete alternatives
rather than a continuum. The separation from §4 is the same one that survives Jin and Myers, which is
either reassuring or the last plank.

**What is left is a claim about form.** Beaver and Ryan decomposed the divergence between book value
and economic value into a **bias** component and a **lag** component twenty-six years ago, and
Bushman and Williams connect delayed expected-loss recognition to the risk profile of banks. That
literature models conditional conservatism as a contemporaneous asymmetric response; §4 models it as
threshold-crossing accumulation under a continuous observability parameter, which is a form that can
carry a recognition lag, a jump magnitude and a location for the variance where a response
coefficient cannot. **The ordering remains the whole of the claim — the recognition event is the
cause and the price crash is the effect — and it remains a research programme and not a finding.**

**On pre-registration and severe testing**, this paper is a straightforward application of the
standard argument — that a prediction's evidential weight depends on the test having had a real
chance to fail — to a domain where the practice remains uncommon. The lineage is Popper's
demarcation — that a claim earns its standing from the risk it ran — Mayo's severity requirement,
which makes that standing quantitative by asking how probable it was that the test would have
detected the error had it been present, and the preregistration case made by Nosek and colleagues.
Mayo's account is cited here at its origin rather than at its restatement, and the volume in which
she and her critics argue it out directly is listed beside it, for the same reason this paper ships
with `REVIEW-001`: an argument is easier to judge when its objections are in the room. The
registration, the negative control, the power analysis and the stopping rule are all conventional,
and are claimed as nothing more than that.

---

## 10 · Data and code availability

Every simulation result in §3 and §4 is produced by open code. The severe test in §5 uses only
public data.

- **Repository:** `https://github.com/jasoncbraatz/wealth-tensor` (public)
- **Modules:** `src/wealth_tensor/lag.py` · `src/wealth_tensor/lambda_sensitivity.py` ·
  `src/wealth_tensor/edgar.py`
- **Regenerate §4 (and §3.4):** `python3 scripts/wt027_report.py`
- **Regenerate §3.3:** `python3 scripts/wt002_lambda_report.py`
- **Regenerate §5:**
  `python3 scripts/wt026_severe_test.py --universe pilot --onset peak` and
  `--universe replication --onset peak`
- **Test suite:** `python3 -m pytest tests/ -q` — **100 tests at the pinned commit d655501**, which
  is the state that produced every result in §3 and §4. The head of the repository carries 103.
  The three later additions guard claims this paper makes and change no model code: two for §4.2's
  closed form D(φ) = (1 − φ)·D(0) and its accompanying negative claim that the lag is *not* linear,
  and one asserting the algebraic collapse Limitation 4 publishes — which had no test until an
  audit found the published form using the entropy rate where it meant the effective decay.
- **Hardware:** none required. Every figure in §3 and §4 regenerates on a commodity CPU in seconds.
  The fits reported in Limitation 4 use two thousand synthetic firms at four hundred gradient steps
  in double precision; a larger reference fit of ten thousand firms at three hundred steps
  completed in **76 seconds on two 2.8 GHz cores**, a machine chosen deliberately so the figure is
  an upper bound. No accelerator is used and none is needed.
- **Empirical data source:** SEC EDGAR `companyfacts` (XBRL), and the SEC Financial Statement Data
  Sets for the CIK→SIC mapping including dead registrants. No proprietary or restricted data is
  used.
- **Pre-registrations:** `docs/preregistration/PRE-001-wt026-observability-lag.md`, registered at
  commit **9722342** — a single-file commit containing the registration and nothing else ·
  `docs/preregistration/PRE-002-wt026-peak-to-charge.md`, registered at commit **d655501**, which
  **also contains the implementation of PRE-002's instrument**; see the disclosure in §5.1. Results
  and full run logs are in the same directory.
- **Code state for the results reported here:** commit **d655501** (last commit touching `src/`).
  A submission-time head-of-repository SHA will be pinned when this paper is posted; **d655501** is
  the SHA a replicator needs and is verifiable now.
- **Drop accounting for §5**, as required by the registrations: the per-bucket attrition from
  candidate charges to the 688 analysed events, by universe and by tier, is in the run logs at
  `docs/preregistration/RESULT-002-*-run.log`. **A reader should check that attrition does not
  differ systematically by tier, since differential attrition is the one selection channel capable
  of manufacturing the reported null.** It is reported there whether or not it flatters the result.

Two tests are worth naming because of what they forbid rather than what they check.
`test_pre001_constants_are_what_was_registered` fails if any registered constant is edited, so a
registration cannot be amended by stealth. Companion modules in this programme carry
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` and
`test_a_flat_gini_does_not_mean_a_bounded_one`, both of which exist solely to make overclaiming
fail loudly.

The repository's `docs/` directory is public and holds the registrations, the run logs, the failed
result, the reasoning that led to the stopping rule, and an internal adversarial referee report on
this draft with the author's responses.

---

## References

***The citation rule this list follows, stated because the author was inconsistent about it before this
pass and the correction is method rather than tidiness.* The edition cited is the edition *consulted* —
the copy in the author's possession — not the earliest printing a catalogue happens to list. Where the
original's date does argumentative work, because the entry is a translation or because a claim about
priority rests on it, the entry is **dual-dated** `original/consulted`. A reprint that changes no
pagination is a *printing*, not an edition, and is not dual-dated.**

***Extended on 2026-08-11 to cover the case the rule above does not reach: a text consulted in a
pre-publication version.** Where the copy read was a working paper or accepted manuscript rather than
the typeset article of record, the entry is dual-dated in the other direction —
`consulted/published` — and carries **✓⧗**. The extension exists because the author had for years
treated a downloaded working copy and the published article as the same object, which is a habit that
survives a bibliographic check intact: the article exists, with those details, and none of that is
evidence that the sentence quoted from it was ever printed there.*

*Verified on 2026-08-10 (session wealthTensor-05); crash-risk entries added 2026-08-11.* **✓** —
checked against a publisher page, a library-catalogue record, a Crossref record or the issuing body's
own documentation, not recalled. **✓✎** — additionally checked against **the author's own copy**, by
reading that copy's title page and colophon. The ✓✎ entries are the ones where doing so changed the
citation. **✓⧗** — bibliographically verified, but the **text** consulted is a pre-publication
version; any quotation is attributed to the version read and may not appear in the article of record.

Andreou, P. C., Lambertides, N., & Magidou, M. (2023). A critique of the agency theory viewpoint of
stock price crash risk: the opacity and overinvestment channels. *British Journal of Management*,
34(4), 2158–2185. ✓ *(Open access. The copy consulted is the publisher's own typesetting, deposited
by the authors' institution, whose EarlyView pagination runs 1–28 and therefore does not match the
issue pagination given here; quotations from it are cited without page numbers for that reason. §9
takes both the 5.5%→27% figure and the universe split from it directly: the 27% is the
CRSP–Compustat–Execucomp sample and the CRSP-wide figure is 23%, a distinction the abstract does not
make and the body does.)*

Basu, S. (1997). The conservatism principle and the asymmetric timeliness of earnings. *Journal of
Accounting and Economics*, 24(1), 3–37. ✓ *(Cited for the asymmetric-timeliness result named in its
own title, and characterised from the author's own posted abstract rather than from the article,
which was not available to the author. Nothing is quoted from it.)*

Beaver, W. H., & Ryan, S. G. (2000). Biases and lags in book value and their effects on the ability
of the book-to-market ratio to predict book return on equity. *Journal of Accounting Research*,
38(1), 127–148. ✓ *(Cited for the bias/lag decomposition named in its own title. §9 identifies this
as the closest prior art to §4's filter, so the entry is load-bearing against this paper rather than
for it.)*

Bleck, A., & Liu, X. (2007). Market transparency and the accounting regime. *Journal of Accounting
Research*, 45(2), 229–256. ✓ *(Read in full text; the copy consulted carries the journal's own title
page — vol. 45 no. 2, May 2007, DOI 10.1111/j.1475-679X.2007.00231.x — so it is the typeset article
and not a pre-publication version. §4.4 and §9 both cite it against this paper: it states §4.4's
volatility result nineteen years earlier.)*

Bushman, R. M., & Williams, C. D. (2015). Delayed expected loss recognition and the risk profile of
banks. *Journal of Accounting Research*, 53(3), 511–553. ✓

Fama, E. F. (1970). Efficient capital markets: a review of theory and empirical work. *Journal of
Finance*, 25(2), 383–417. ✓

Financial Accounting Standards Board. *Accounting Standards Codification*, Topic 350 — *Intangibles —
Goodwill and Other*; Topic 360 — *Property, Plant, and Equipment*; Topic 280 — *Segment Reporting*. ✓

Georgescu-Roegen, N. (1971). *The Entropy Law and the Economic Process*. Harvard University Press. ✓✎
*(The copy consulted is the Harvard Paperback second printing, 1974, ISBN 0-674-25781-2; a printing is
not an edition, so no dual date.)*

Godley, W., & Lavoie, M. (2007). *Monetary Economics: An Integrated Approach to Credit, Money, Income,
Production and Wealth*. Palgrave Macmillan. ✓✎ *(Copy consulted confirms first published 2007, ISBN
978-0-230-50055-6.)*

Hayek, F. A. (1945). The use of knowledge in society. *American Economic Review*, 35(4), 519–530. ✓

Hutton, A. P., Marcus, A. J., & Tehranian, H. (2009). Opaque financial reports, R², and crash risk.
*Journal of Financial Economics*, 94(1), 67–86. ✓ *(Nothing is quoted from the body, which was read
as full text rather than as the typeset article. The post-SOX dissipation §9 attributes to them is
from the published abstract, checked at source.)*

International Energy Agency & United Nations Statistics Division. *SDG Indicator 7.3.1 — Energy
intensity measured in terms of primary energy and GDP.* Reported as World Bank series
`EG.EGY.PRIM.PP.KD`, *Energy intensity level of primary energy*, compiled for *Tracking SDG 7: The
Energy Progress Report* by the IEA, IRENA, UNSD, the World Bank and the WHO. ✓

Jin, L., & Myers, S. C. (2004/2006). R² around the world: New theory and new tests. *Journal of
Financial Economics*, 79(2), 257–292. ✓⧗ *(The published article is verified bibliographically and is
what §9 cites for the model and its results. The **text** consulted is the earlier NBER Working Paper
10453, April 2004, whose proposition numbering differs from the published version; §9's one
quotation — "For simplicity, we ignore depreciation and reinvestment" — is from that working paper,
was checked character-by-character against its PDF, and has **not** been checked against the typeset
article. Two years and a referee process separate the two texts, so the sentence may not appear in
the article of record in this form. §9 quotes it because it is the sentence that establishes the
model has no physical layer, and a reader entitled to doubt that on a paraphrase should be able to
see the words; every other characterisation of this paper in §9 is a paraphrase for the same reason
in reverse.)*

Jonckheere, A. R. (1954). A distribution-free k-sample test against ordered alternatives. *Biometrika*,
41(1–2), 133–145. ✓

Mann, H. B., & Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically
larger than the other. *Annals of Mathematical Statistics*, 18(1), 50–60. ✓

Mayo, D. G. (1996). *Error and the Growth of Experimental Knowledge*. University of Chicago Press. ✓✎
*(The copy consulted is the University of Chicago Press edition of 1996, which uses* severity *374 times
and* severe test *232 times and is where the severity requirement is introduced. An earlier draft of
this list cited Mayo (2018),* Statistical Inference as Severe Testing *— a later restatement the author
has not read. Both the edition-consulted rule and the first-appearance rule select 1996, and they agree
here because the book he read is also the origin.)*

Mayo, D. G., & Spanos, A. (Eds.). (2010). *Error and Inference: Recent Exchanges on Experimental
Reasoning, Reliability, and the Objectivity and Rationality of Science*. Cambridge University Press. ✓✎
*(Copy consulted gives © Cambridge University Press 2010, first published in print 2009.)*

Mises, L. von (1949/1998). *Human Action: A Treatise on Economics* (Scholar's ed.). Ludwig von Mises
Institute. ✓✎ *(The copy consulted is the Scholar's Edition, ISBN 0-945466-24-2, whose own front matter
states that it reissues* the first edition *— load-bearing, because the 1963 and 1966 editions differ
from 1949. Original work published by Yale University Press, 1949.)*

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution.
*Proceedings of the National Academy of Sciences*, 115(11), 2600–2606. ✓

Odum, H. T. (1996). *Environmental Accounting: Emergy and Environmental Decision Making*. John Wiley &
Sons. ✓✎ *(Copy consulted gives © 1996 John Wiley & Sons, Inc., New York, ISBN 0-471-11442-1. This entry
was re-pointed away to* Environment, Power, and Society *(Columbia, 2007) when the first library sweep
did not find the 1996 book, then restored when it did. The sweep, not the citation, was wrong — see
WT-062.)*

Piketty, T. (2013/2014). *Capital in the Twenty-First Century* (A. Goldhammer, Trans.). Belknap Press of
Harvard University Press. ✓ *(Original work published as* Le Capital au XXIe siècle*, Éditions du Seuil,
2013. §9's relocation argument is about work that existed a year before the English text cited here.)*

Popper, K. R. (1935/2002). *The Logic of Scientific Discovery*. Routledge Classics. ✓✎ *(The copy
consulted is the Routledge Classics edition of 2002. Its own colophon gives the chain:* Logik der
Forschung *first published 1935, Vienna — its preface dated 1934 — first English edition Hutchinson &
Co., 1959, Routledge from 1992. §9 cites Popper for the demarcation criterion, which is 1935's, not
1959's, so the original date is load-bearing and the entry is dual-dated.)*

Quine, W. V. O. (1951). Two dogmas of empiricism. *Philosophical Review*, 60(1), 20–43. ✓

Soddy, F. (1926/1961). *Wealth, Virtual Wealth and Debt: The Solution of the Economic Paradox* (3rd ed.).
Omni Publications. ✓✎ *(The copy consulted is the third edition, LCCN 60-53331, printed in the United
States under a Britons Publishing Company, London, title page, and described on that page as a reprint
of the second edition of 1933 “containing new material and Foreword to the American Nation”. The first
edition is George Allen & Unwin, London, 1926; the copy's own* Preface to the First Edition *is dated
January 1926 and its Addition to the Second Edition refers to “the book, which first appeared in 1926”.
The term* virtual wealth *is in the 1926 title, so 1926 is the earliest appearance this paper can
support; Soddy's own footnote points back to* Cartesian Economics *(Hendersons, 1922) as prior work on
the subject, and whether the term itself originates there has NOT been checked — the 1922 pamphlet is
not in the author's library. No claim of priority is made in the text, so none is made here.)*

Terpstra, T. J. (1952). The asymptotic normality and consistency of Kendall's test against trend, when
ties are present in one ranking. *Indagationes Mathematicae*, 14, 327–333. ✓

*How this list was checked, recorded because a reference section that silently improves teaches a
reader nothing. The per-entry findings live in the ✓ and ✓✎ notes above, attached to the entries they
describe, so that correcting an entry cannot leave a summary of it behind.*

**Three passes ran, in this order, and each one found what the previous one structurally could not.**

1. **Bibliographic.** Every entry checked against a publisher page, a library catalogue, a Crossref
   record or the issuing body's own documentation. It asks *does this work exist with these details?*
   and it came back clean.
2. **Cited-in-text.** Every entry checked against the body. It asks *does this reference do any work?*
   — and found several that did not. Some were given the work they had been listed for; the rest were
   removed rather than retro-fitted, because a reference kept for the look of the list is exactly the
   padding the list is supposed to be evidence against.
3. **Provenance.** Every entry checked against the author's own copy. It asks *is this the object the
   claim is about, and is it the one that was read?* Several entries survived passes 1 and 2 and
   failed this one: right work, wrong edition; right argument, wrong book; and in one case an author's
   surname matched a different scholar entirely. Two entries were corrected, reverted, and corrected
   again as the library search improved — the citations were not wrong, the *search* was, and the
   record of that is in `LEDGER.md` WT-059 and WT-062.
4. **Version**, added 2026-08-11 with the crash-risk entries. It asks *is the text I quoted the text
   of record?* — which passes 1 and 3 both leave open, the first because the article exists either
   way and the second because a working copy on the author's own disk **is** his own copy. It found
   that the crash-risk papers had been read in pre-publication and untypeset versions and cited as
   though they were the published articles. Hence **✓⧗**, and hence the single surviving quotation in
   §9 being attributed to the working paper it was actually read in rather than to the journal.

**The order is the lesson.** A clean bibliographic pass is not evidence of a correct citation; it is
evidence of a correct *bibliography*. The two are different documents that happen to share a page.
The fourth pass is the same observation one step further in: a correct citation of a work is not
evidence that the work said the words attributed to it.

*A third note, on the order these were found in, because it is the reusable part.* The bibliographic
pass came back clean — every work exists, with those details, from a publisher or a catalogue. The
provenance pass an hour later found that **three of the five books present in the author's library
were being cited as the wrong object**. Both passes were correct; they answer different questions, and
only the second one asks whether the citation points at the thing that was read. See `LEDGER.md`
WT-059.
