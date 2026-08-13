# Timeliness and durability are not separately identified from a reported series

**Jason C. Braatz**
*Independent researcher*
jason@braatzresearch.com

**Draft — not yet submitted.** Version 0.5, 2026-08-12.

**Declaration of interest.** The author is employed by a company building accounting software for very small businesses. This work was conducted independently, on personal time, and without company funding, data or direction.

**Use of AI assistance.** Anthropic Claude Opus 5, at high reasoning effort, was used throughout as a research and drafting assistant: literature retrieval, adversarial review, code review and prose drafting. All claims, results and final text are the author's, and every computational result is produced by committed code in the repository named in the data-availability statement.

---

## Abstract

A balance sheet is an instrument, and instruments have transfer functions. Model the reporting
layer as a low-pass filter on a physical layer that degrades whether or not anyone records the
degradation: a share **φ** of each true change is observable and passes through at once, the
remainder accrues in an unrecognised gap and is released at rate **α**, and the integral of what the
statements owe is exactly **(1 − φ)** times its value at φ = 0, in closed form.

The parameter of interest is not recoverable from what the instrument emits. **The triples (α, δ, φ)
and (δ, α, φδ/α) generate the identical reported series**, where δ is the physical decay rate: the
filter's two roots are exchangeable and the exchange preserves φδ exactly. The proof is four lines —
the exchange imposes two coefficient conditions and both reduce to φ′α = φδ — and the reported gap is
a Bateman function, whose exchange symmetry pharmacokinetics has called *flip-flop* since the 1970s.
Timeliness and durability are therefore not separately identified from a reported series, and a
series cannot distinguish a prompt reporter of a durable asset from a slow reporter of a perishable
one. **Where the asset's physical scale is not observed — every firm-level series, which aggregates
vintages — the identified set is not two points but a continuum, and a factor of 1.67 in that
unobserved scale spans the whole unit interval of timeliness.** A second series drawn from the
asset repairs this — the returns the field's instruments already condition on suffice — but the
repair is a rate and not a proof. Its strength belongs to the asset rather than to the design: the
level is set by how far the book's amortisation rate sits from the asset's true decline, the
response to news is set by the decay rate and reverses sign as that rate approaches zero, and no
horizon attains the root-T rate, because every term in the estimating equation decays with the asset
itself.

Indexing asset classes and writing the recursion with a Hadamard product, the corollary is
cross-sectional: **classes are ordered by (1 − φ) ⊙ δ ⊘ (α − δ), not by φ** — decay reaching the
ranking through two channels, neither of them the parameter of interest. A φ-ordered
cross-section is therefore valid only inside a region of δ-space, and the region has a closed-form
boundary in quantities the design already declares: the probability that it recovers its own
ordering crosses one half when per-rung δ leverage reaches **0.61** of the design budget. Across the
four GAAP classes with the decay rates the standards imply, that ratio is 2.58 and the composite
does not blur the intended ranking but **inverts** it, Kendall τ = −1. Draw δ independently instead
and the ordering survives in **11.5%** of 4,000 ladders — dispersion destroys the ranking, and the
standards' ladder is what turns the wreck into a reversal. This constrains any cross-sectional use
of the conditional-conservatism measures, which read a recognition property off a reported series.

The framework's own sharpest prediction — recognition lag ordered by GAAP asset class — was
pre-registered, tested on 688 EDGAR-derived events across two sectors declared in advance, and
**failed** (Jonckheere–Terpstra z = −0.290 and −0.095 against power 0.95–1.00; the stopping rule
fired). The identification result does not explain that failure, and this paper reports the check
that refused to: **the lag statistic is the one observable the composite does not invert**, holding
its ordering in 100% of the same admissible ladders and in 66.2% when δ is drawn independently,
against 11.5% for the magnitude measure. What it cannot do is exist in public data — the
model's lag is a cross-correlation against a physical series no filing reports — so the registered
instrument necessarily measured a substitute, and the bridge to it was never written down. The
repair follows from the theorem: **disclosed useful lives supply δ from outside the series**,
restoring φ for every class that has one, and none for goodwill, where at δ = 0 the parameter is not
ill-conditioned but absent. The disclosed lives also fix the model's domain, and they fix it
tightly: the deferral measure exists only where the recognition rate exceeds the decay rate, and at
the calibration used here **no disclosed useful life short enough to appear in a filing satisfies
that** — which makes the recognition rate, rather than the ordering, the quantity a cross-sectional
design has to establish first. The same registered events establish it: **the recognition rate is
0.41 per year against a calibration of 0.05**, so the disclosed lives lie inside the model's domain,
and the hazard rises with the age of the gap rather than staying constant as the model assumes.
**The closed form survives that: the deferral measure is the recognition lag's moment generating
function evaluated at the decay rate, and what the constant hazard supplied was not the result but
its domain** — under a rising hazard there is no domain restriction, and the correction to the
measure is under one per cent across the classes ranked here and 44% at a disclosed three-year life.
The events also reject the reporting layer's diagonality, clustering across asset classes within a
firm-quarter at two to four times the independence rate in both sectors.

**Keywords:** identification · conditional conservatism · reporting lag · impairment ·
pre-registration · asset life · deferred information

**JEL classification:** M41, D80, C18, G14, E01

---

## 1 · Introduction

A balance sheet is not a window. It is an instrument, and instruments have transfer functions.

That sentence is the whole paper, and the rest of it is an attempt to make the sentence cost
something — to state the transfer function precisely enough that it forbids outcomes, to derive a
consequence that can be checked, and then to check the sharpest one against public data and report
what happened.

The starting observation is old and belongs to Soddy: a physical asset and a financial claim on that
asset are different kinds of object, and confusing them is how societies come to believe they are
wealthier than they are. What this paper adds is that the confusion has a *dynamics*. If the
physical component degrades whether or not anyone records the degradation, and the claim component
changes only when someone records something, then the gap between them is an accumulating quantity
of a specific kind: **information the reporting layer owes and has not delivered.**

Read that way, several things stop being metaphors. Technical debt becomes off-balance-sheet
entropy, and deferred maintenance becomes an unrecognised liability with a measurable integral —
exactly proportional to (1 − φ), where φ is the share of degradation the reporting layer can see.

The paper's substance, however, is not that model. It is what the model implies about the *readers*
of reported numbers, including this paper's own attempt to be one.

The filter has two roots: the rate at which the reporting layer releases what it has withheld, and
the rate at which the physical layer decays. **Those two roots are exchangeable, and the exchange
preserves the product of timeliness and decay.** A reported series therefore contains φδ and nothing
further about φ — a prompt reporter of a durable asset and a slow reporter of a perishable one emit
the *same series*, to fourteen decimal places. Timeliness and durability are not separately
identified from reported numbers.

That constraint is not a property of this framework. It is a property of the object every
conditional-conservatism measure takes as input, and its cross-sectional form is sharp enough to
be uncomfortable: indexing asset classes, the ranking a reader can compute is the ranking of
**(1 − φ) ⊙ δ ⊘ (α − δ)**, so a comparison across classes with different asset lives is not a
comparison of timeliness. Across the four GAAP classes, with the decay rates the standards themselves imply, the
composite does not blur the intended ranking — it **inverts** it — and the ordering the design
imposed survives in **11.5%** of ladders even when no durability ordering is imposed at all.

This programme learned that the hard way, which is the second reason the paper exists. The
framework's sharpest empirical prediction was pre-registered, tested twice on EDGAR-derived
impairment data with a stopping rule declared in advance, and it failed. §5 reports the failure at
full length. §4 reports what the identification result says about that failure, and the answer is
that it **does not explain it**. The one observable the composite spares is precisely the one the
registration ordered — and it is not computable from public filings, so the instrument measured a
substitute whose relation to the model was never written down. A theorem about identification, a
registered null, and the discovery that the two are less connected than they look, are three
different results, and this paper reports them as three.

**Contributions.** Numbered, so that a reader is not obliged to construct a smaller list than the
one intended.

1. **An exact observational equivalence, with its proof and its reach** (§4.2). The filter's two
   roots exchange, preserving φδ, so timeliness is not recoverable from a reported series by any
   estimator. The structure is the Bateman function's, and the accounting instance is placed against
   its known analogues in pharmacokinetics and compartmental identifiability. Where the physical
   scale is unobserved the degeneracy widens from two points to a continuum spanning all of φ.
2. **The cross-class corollary, in Hadamard form** (§4.3–4.4). With classes indexed the reporting
   layer is diagonal, the observable ranking is the ranking of (1 − φ) ⊙ δ ⊘ (α − δ), and on the
   ladder GAAP supplies that ranking is the reverse of the ranking of φ. The validity condition for a
   timeliness-ordered design is itself a statement about decay rates.
3. **A constraint on the conditional-conservatism measures** (§4.6), stated with its three
   qualifications, together with the specific circumstance under which those measures remain sound.
   The returns those measures condition on do break the equivalence (§4.7) — and the strength with
   which they break it is a property of the asset rather than of the design: its level is set by the
   gap between the book's amortisation rate and the asset's true decline, its response to news is set
   by the decay rate and reverses sign as that rate nears zero, and no horizon attains the root-T
   rate. The corner where the repair is weakest is the one the standards decline to schedule.
4. **A repair that needs no new data** (§4.7). Disclosed useful lives supply δ from outside the
   series, which is what the theorem requires; comparing timeliness within a life band reads φ.
5. **A pre-registered severe test and its failure** (§5) — registered before the data were touched,
   replicated in a second sector declared in advance, controlled against a label-permutation null,
   powered at 0.95–1.00, and lost, with the stopping rule honoured.
6. **A bridge discipline** (§6.2) arising from that loss, and now with an argument behind it: any
   identification of a model parameter with a measurable must be written as a proposition a
   competent critic could deny.
7. **A survivals ledger** (§7), including the row that overturned this paper's own preferred reading
   of its null.

**A word about §5, since its placement is deliberate.** The failed prediction is in the body and in
the abstract. It is not in *Abandoned Approaches*. A pre-registered prediction that was tested and
lost is a **result**; filing it under abandonments would be the softest available way to hide it, and
this paper has no claim on a reader's seriousness if it takes that route.

The framework the filter was built inside — three propositions about the composition of wealth, and
the coupling they oblige — is set out in **Appendix A**. Nothing in §§2–7 depends on it, which is
the point of putting it there.

---

## 2 · The filter

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
objection that would otherwise kill it outright — see §8.1.

---

## 3 · What the filter does

### 3.1 · Lag and deferred information scale with unobservability

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

### 3.2 · Volatility is not suppressed, it is relocated

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
§10; it is noted here because the table's headline result is nineteen years old.

**It is not, however, a usable empirical target.** Against filed accounting data the concentration
statistic is unfalsifiable by construction: the asset class with no amortisation schedule has
essentially all of its recognised change arrive discretely *as a matter of accounting definition*,
not of firm behaviour. A test of that is a test that cannot fail, and a test that cannot fail is
not a test. Neither pre-registration included it, on exactly those grounds, before either was
run. The relocation result is therefore a property of the model and a candidate
description of the world, and it is **not** offered as the replacement severe test. The framework
does not currently have one.

*Method note, because the fix mattered more than the result.* The original metric measured the
wrong object: one number was being asked to carry two claims. Two now exist — smoothing measured
on the periods between recognition events, concentration measured on the recognition events — because a statistic that
answers two questions answers neither.

---

## 4 · Timeliness and durability are not separately identified

§3 established what the filter does to one asset. This section establishes what a reader of the
filter's output can learn from it. The answer is a constraint on the instrument rather than a
caution about estimation: it holds for every estimator, it has a four-line proof, and it applies to
measures built without reference to this model or any like it.

The weak form is a conditioning statement — φ is recoverable, but the estimator's variance grows
like 1/δ². That form is true and too kind. In the filter regime the degeneracy is exact.

### 4.1 · The class index, and why the product is elementwise

A firm holds several classes of asset, and the accounting standards treat them differently on
purpose. Index the classes *i*. Each carries its own physical decay rate δᵢ, its own observable
share φᵢ, its own recognition rate αᵢ and its own threshold θᵢ, and §2's two recursions become one
line in vectors:

> **C**(t+1) = **C**(t) + **φ** ⊙ Δ**E** + **α** ⊙ **gap**(t),  **gap**(t) = **E**(t) − **C**(t)

with ⊙ the Hadamard product. The elementwise form is a substantive claim rather than a notational
economy: **the reporting layer is diagonal in class space.** A dollar of unrecognised deterioration
in a distribution centre does not force recognition against a trademark. Each class's filter reads
its own gap and nothing else.

That claim is an assumption and it is false in detail; §9 says so and proposes the test. What
matters here is that writing it down makes the next result expressible. Without the class index the
identification result below is a remark about a single parameter. With it, the remark acquires a
corollary about *rankings*, and rankings are what the empirical literature on this subject
estimates.

### 4.2 · The theorem

Take one class and disable the recognition mechanism, so the filter is examined in isolation. Write
δ for the effective decay rate d(1 − m) of §2. Substituting ΔE = −δE(t) collapses the pair of
recursions to a single line:

> C(t+1) = C(t)(1 − α) + E(t)(α − φδ),  E(t) = E₀(1 − δ)ᵗ

φ appears once, in the product φδ, and nowhere else. With the books opening square — C(0) = E(0) =
E₀, an asset carried at cost on the day it is acquired — this solves in closed form. Writing
A = 1 − α and D = 1 − δ for the two roots,

> **C(t) = E₀ · [ δ(1 − φ) Aᵗ − (α − φδ) Dᵗ ] / (δ − α)**

and the reported series is a linear combination of two geometrics whose exponents are the
reporting rate and the physical decay rate.

Now exchange them. Send (α, δ, φ) → (δ, α, φ′), which swaps A and D, and ask what φ′ must be for
the series to come back unchanged. The Aᵗ coefficient requires δ(1 − φ) = δ − φ′α. The Dᵗ
coefficient requires α − φδ = α(1 − φ′). Both reduce to

> **φ′α = φδ**

Two equations, one unknown, and they agree. That coincidence is the theorem: the system is
overdetermined and consistent, so the exchange is not approximate, not local, and not a matter of
conditioning.

> **Observational equivalence.** The parameter triples **(α, δ, φ)** and **(δ, α, φδ/α)** generate
> the *identical* reported series. The filter's two roots — the reporting rate and the physical
> decay rate — are exchangeable, and the quantity preserved by the exchange is exactly **φδ**.

The numerical confirmation runs alongside the proof rather than in place of it: the largest
deviation between a series and its mirror is 8 × 10⁻¹⁶, the arithmetic and not the model, against
3 × 10⁻¹ when the mirror's φ′ is replaced by the value that would preserve the *unrecognised gap*
instead of the reported series — a discrepancy of fourteen orders of magnitude between the right
conserved quantity and a plausible wrong one. Admissibility requires φδ ≤ α, which holds at every
parameter setting used anywhere in this paper.

So a reported series does not merely make φ hard to recover. **It does not contain φ.** It contains
φδ, and it cannot distinguish a timely reporter of a durable asset from a laggard reporter of a
perishable one.

**What the two worlds disagree about is the firm, not the filing.** The mirror is not a
mathematical curiosity with no economic content. It is a slow reporter of a fast-decaying asset:
at t = 400 its physical stock stands at 4 × 10⁻⁶ of the original world's, a book value sitting
above an asset that has all but evaporated. That is a recognisable kind of company. It files the
same statements, to fourteen decimal places, as the prompt reporter of the durable asset.

**The mathematics is old, and saying so costs nothing.** Subtract E(t) from the closed form and the
unrecognised gap is

> G(t) = E₀ · (1 − φ) δ · S(t),  S(t) = (Aᵗ − Dᵗ)/(δ − α)

a scalar amplitude carrying every trace of φ, multiplied by a shape function that is invariant
under exchanging the roots. S is the Bateman function, written down in 1910 for the daughter
activity of a radioactive decay chain (Bateman, 1910), and its exchange symmetry is the reason
pharmacokinetics has a name for this: **flip-flop**, the interchange of an absorption rate constant
with an elimination rate constant in a one-compartment model, which leaves the concentration–time
profile unmoved (Garrett, 1994). Kuan, Wright and Duffull (2023) place it as an issue of
*local* identifiability, "in that there exists a finite set of parameter values (rather than a single
set) that solves the problem" — which is precisely the two-point structure above. Their own caution
should be carried across with the result: they hold that the competing solutions are "not simply a
function of swapping the rate constants" but a partial permutation of the parameter set, with n + 1
of them for an n-compartment model. The accounting case here, where the exchange **is** a clean swap
of two roots, is therefore the simplest member of that family rather than the general one. The general framework is Bellman
and Åström's (1970), which defines structural identifiability by what the input–output map
determines and tests it through the transfer function — and a transfer function fixes its poles as
a set, which is the exchange above stated once and for all.

Economics has its own instance, and it sits closer to this paper than either. Nerlove's
supply-response model (1958) stacks adaptive expectations at rate β on partial adjustment at rate γ;
eliminating the two unobservables leaves a reduced form in which **every systematic coefficient is a
symmetric function of β and γ** — [(1 − β) + (1 − γ)] on the lagged dependent variable, −(1 − β)(1 − γ)
on its second lag, βγa₁ on the price. The conditional mean is exactly invariant under exchanging the
two behavioural rates. What distinguishes them is the disturbance, γ[u(t) − (1 − β)u(t−1)], which is
not symmetric. That the tie is broken by the error process rather than by the systematic part is a
property of the Nerlovian model which the filter here does not inherit, and §4.7 says what breaks it
instead.

The ambiguity bites here for the same reason it bites in pharmacokinetics and not in
radiochemistry: it needs a **free scale parameter** to hide in. A decay chain's parent activity is
measured independently, so the exchange changes the observed curve by a detectable factor and
nothing is lost. A plasma profile has an unknown volume of distribution, and a balance sheet has an
unknown (1 − φ). Accounting is on the pharmacokinetic side of that line, and the next result is
what it costs.

**The result is stronger than a two-point ambiguity.** The closed form has two roots and two
amplitudes: four numbers, and that is everything a reported series contains. The model has five
parameters — α, δ, φ, the physical scale E₀, and any gap g₀ already open when the observation
starts. Five into four does not go, and the shortfall lands on φ.

Two consequences, both exact. First, opening the books with a gap already in place does not rescue
identification: the mirror survives with the same g₀ under the shifted map φ′ = [φδ + g₀(α − δ)]/α,
and the conserved quantity generalises to (φ − g₀)δ = (φ′ − g₀)α. The obvious escape — *real firms
are not observed from acquisition* — makes matters worse rather than better.

Second, and this is the sharp form: **when the physical scale is not observed, φ is not two-valued.
It is free.** Fix a reported series generated at φ = 0.60 and ask what other parameter vectors
reproduce it exactly. Assuming a physical scale of 0.76 implies φ = 0; assuming 1.27 implies φ = 1;
every assumption in between implies an intermediate φ, and every one of them regenerates the
observed series to 2 × 10⁻¹⁶. **A factor of 1.67 in the unobserved physical scale spans the entire
unit interval of timeliness.** The reported series is consistent with a firm that recognises
everything at once and with a firm that recognises nothing.

The condition under which this bites is worth naming precisely, because it is the empirical norm
rather than an edge case. E₀ is observed when an asset is followed from acquisition, where cost
fixes the physical scale and the gap opens at zero. It is not observed for a firm-level series,
which aggregates assets of many vintages, so the scale that would pin φ is exactly what a
cross-sectional study does not have.

The earlier conditioning result stands underneath all of this and is worth keeping for its size:
fitting the model to a synthetic series recovers φ with a median absolute error of 0.211 when δ is
estimated jointly and 0.00073 when δ is pinned at its true value, a **291-fold** difference, with a
noise-free series giving 0.211 as well. That is what an exact degeneracy looks like from inside a
numerical optimiser: not a cliff, a canyon.

One channel does break the equivalence, and it is closed. The recognition events' trigger reads
gap/E, and across five mirror pairs the event counts differ sharply enough to separate them (16
against 66, 25 against 80, 36 against 133, and two pairs where one side is silent entirely). **The
trigger reads E, which no filing reports.** The information that breaks the degeneracy arrives
through a channel the reported series does not have.

### 4.3 · What a cross-class ranking reads

The class index now earns its keep. What a series identifies is φᵢδᵢ, so a cross-class ranking
computed from reported numbers is a ranking of the product — and a ranking of φ ⊙ δ is not a
ranking of φ unless δ is constant across the classes being ranked.

The model's own measure of how much a class defers sharpens this. The steady-state ratio of
unrecognised gap to physical value has a closed form:

> **R**ᵢ = (1 − φᵢ) δᵢ / (αᵢ − δᵢ)

which simulation reproduces to the transient bound, 2 × 10⁻⁴ after 400 periods, against a witness
of 1.0 when φ is misstated by 0.1. Across classes with a common α this is a Hadamard product again,
**(1 − φ) ⊙ δ**, divided elementwise by (α − δ). Decay reaches the ranking through two channels,
neither of them the parameter of interest.

R is the model's deferral measure and not an observable — it is a ratio to E, and E is the series
nobody reports. Under the mirror it does not shrink or stretch: it **changes sign**, from +0.267 to
−1.267, because the mirror world is one in which the books outrun the asset. A quantity that
reverses sign under an exchange the data cannot detect is not a quantity a reader recovers. What
§4.4 uses R for is what it is good for: computing, inside the model, which way a ranking runs.

**Timeliness sets the ranking only when durability is constant across the classes being ranked** —
and the classes accounting standards distinguish are, almost by construction, the classes whose
durability differs. That is why the standards distinguish them.

This is not a defect of the present model. Any model in which reporting lag attenuates a physical
signal will multiply a timeliness parameter by an asset-life parameter somewhere, because the
observable is a rate times a duration. The model's contribution is to make the product explicit
enough to be checked.

### 4.4 · The design has a validity region, and the disclosed numbers fall outside it

The natural expectation is that a confound of this kind adds noise to a ranking. It does something
more specific. There is an exact region of δ-space inside which a φ-ordered cross-section recovers
the ordering it imposed; the region has a closed-form boundary in quantities the design already
declares; and it is small. The case this paper's own registration used sits outside it, and so does
every firm whose asset lives are read off its filings.

Order the four GAAP classes as the registration did — property, plant and equipment; finite-lived
intangibles; indefinite-lived intangibles; goodwill — and assign the observability shares the
registration assumed, falling up the ladder as the standards' willingness to put a class on an
amortisation schedule falls. Then assign the decay rates the same standards imply, which fall up the
same ladder, because a class is placed on a schedule precisely when its decline is predictable
enough to schedule. Goodwill sits at the end of both: least observable, and with no degradation
schedule at all.

| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** | R at a common δ |
|---|---|---|---|---|---|---|
| 0 · property, plant and equipment | 0.80 | 0.20 | 0.030 | 0.00600 | **0.2999** | 0.1333 |
| 1 · finite-lived intangibles | 0.60 | 0.40 | 0.020 | 0.00800 | **0.2667** | 0.2667 |
| 2 · indefinite-lived intangibles | 0.40 | 0.60 | 0.010 | 0.00600 | **0.1500** | 0.4000 |
| 3 · goodwill | 0.20 | 0.80 | 0.002 | 0.00160 | **0.0333** | 0.5333 |

The right-hand column is the world the design assumed: classes differing in observability and in
nothing else. There the deferral measure rises monotonically up the ladder exactly as predicted,
Kendall τ = +1. The column beside it is the world the standards describe. There the deferral measure
is monotone too — **running the other way.** Kendall τ = **−1** at the calibrated rate, and **−0.67**
at the measured one; the rung that separates them is identified below.

**The design and its own observable are anti-aligned across the ladder.** A confounded design
returns noise; this one returns the reverse of what it ordered. On the model's own arithmetic, the
class predicted to defer most defers least, because it barely deteriorates, and there is little to
defer.

The condition deciding the direction is worth writing out, because of what it contains. Taking logs
of R,

> log R = log(1 − φ) + log δ − log(α − δ)

so the deferral measure rises from one tier to the next exactly when

> Δlog(1 − φ) + Δlog δ − Δlog(α − δ) > 0

The first term is the design. **The other two are facts about δ**, and on a falling ladder they
carry the same sign, so they add. At every rung of the ladder above, the combined δ contribution
(−0.81, −0.98, −1.79) outweighs the design term (+0.69, +0.41, +0.29), and the decomposition
predicts the direction of every step. Checking only the log δ term would have got the first rung
right for the wrong reason: there the design term is the larger of the two, and the step still falls,
because δ enters twice.

**So the validity condition for a φ-ordered cross-sectional design is a statement about δ** — the
quantity §4.2 says the reported series does not contain. A researcher cannot establish that the
design is sound without already possessing what the design was built to avoid needing.

**Dispersion and ordering do different damage, and the two are worth separating.** Draw 4,000
four-class ladders under the design's own constraint alone — observability falls up the ladder —
with δ drawn independently across classes. The deferral measure recovers the registered ordering in
**11.5%** of them and exactly reverses it in **1.1%**, mean Kendall τ **+0.32**. Hold δ common
across the four classes instead and redraw: recovery is **100.0%**. Now impose the standards'
falling ladder on the same draw and recovery falls to **1.9%** while exact reversal rises to
**23.8%**, mean τ **−0.41**. So δ *dispersion* is what destroys the ranking, and the *ordering* is
what turns the wreckage into a reversal. The table above is what the confound does at one corner of
the region; losing the ranking is what it does across the region.

**The boundary is exact, and it is drawn in quantities the design already declares.** Write the
design's *budget* as the mean per-rung Δlog(1 − φ) and the ladder's *δ leverage* as the mean
per-rung |Δlog δ − Δlog(α − δ)|. Over the same 4,000 draws the probability that the design fails to
recover its ordering, fitted as a logistic in log(leverage / budget), has slope **+1.58** (se 0.081,
z = +19.5; the same fit on a permuted outcome returns z = 0.23) and crosses one half at a
leverage-to-budget ratio of **0.61**. A φ-ordered cross-section is more likely than not to read what
it ordered only while per-rung δ leverage stays under about three fifths of the design budget. The
ladder tabulated above sits at **2.58**.

**The tabulated ladder is a knife edge in its own top rung.** Holding the first three tiers fixed,
the deferral measures of goodwill and indefinite-lived intangibles cross at

> δ₃\* = Kα/(1 + K),  K = R₂/(1 − φ₃)

which is **0.0079**, a half-life of eighty-seven periods. Five per cent above it the ladder is no
longer monotone and Kendall τ moves from −1 to −0.67. The table assigns goodwill 0.002. The exact
reversal therefore needs goodwill to lose half its value no faster than in eighty-seven years, and
the standards do not say that: a class is left off an amortisation schedule when its decline cannot
be *scheduled*, which is a statement about predictability and not about speed.

**Unpredictable is not slow, and the difference is measurable in the same direction.** Drive a class
at δ = 0.20 with probability 0.05 and at zero otherwise — an identical mean decay rate of 0.010,
delivered in rare jumps — and its realised deferral is **1.30 times** the closed form evaluated at
that mean rate (se 0.002 over 2,000 paths). An unscheduled class defers *more* than a scheduled one
of the same average durability, and the lumpy path defers as a smooth class at δ = **0.0123**, above
the crossing rate. Both halves of the inference from an absent schedule therefore push the same way.

**Two rungs need no inference at all, and they are the two that break the table.** ASC 360 and
ASC 350-30-50 require disclosure of useful lives for property and for finite-lived intangibles, and
a disclosed life *L* fixes a write-down rate 1/*L*. The first rung falls only when

> δ₁ < αδ₀/(2α − δ₀)

which tends to δ₀/2 as α grows. At the tabulated δ₀ = 0.030 that boundary sits at δ₁ = **0.0214**, a
life of 46.7 years, and the table assigns 0.020 — inside by a fourteenth **at α = 0.05, and outside
it at the measured rate**, where the same boundary is 0.0156. That is the rung the table's τ turns
on, and it turns on the recognition rate's *level* rather than its shape: the top three rungs are
unchanged at either rate, and §4.9 puts the shape's contribution to the crossing below it at 0.13%. Disclosure, however,
amortises finite-lived intangibles over materially *shorter* lives than property, so δ₁ > δ₀ is what
a filing presents; across the rectangle of lives disclosure spans — ten to forty years for property,
three to twenty for finite-lived intangibles — **the first rung rises in 99.7% of it.**

**And the binding constraint is the model's domain, not the ordering.** R is defined only for
δ < α. Past that the deferred gap grows without bound relative to the asset — the ratio reaches
10⁶⁹ by period 400 at δ = 0.20 — and there is no steady-state deferral measure to rank. At the
α = 0.05 calibrated here **the entire disclosed rectangle lies outside the domain**: every useful
life short enough to appear in a filing implies a decay rate at or above the recognition rate. Half
of the rectangle is admissible only at α ≈ 0.19, and all of it above α = 0.33. **That made the
recognition rate, not the ordering, the quantity to establish first — and §5.4 establishes it.**
On the registered sample the recognition rate is **α̂ = 0.408 per year**, 95% interval
[0.383, 0.432]: the calibration used here is low by an order of magnitude, the disclosed rectangle
lies inside the domain after all, and the first-rung result above therefore holds at a measured rate
rather than at a hypothetical one. The domain restriction is a property of the calibration and not
of the disclosure.

**The shape of this argument is not new, and its best-known instance is one field over.** Fisher and
McGowan (1983) argued that an accounting rate of return cannot be used to infer economic
profitability, because the reported ratio depends on the depreciation schedule and the firm's growth
rate as well as on the economic return it is supposed to measure — a reporting-rule parameter and an
asset-life parameter confounded inside a published number, forty years before this paper, and it
detonated an industrial-organisation literature. Two things about its reception instruct the present
one. Their demonstration was numerical rather than a theorem, and the analytical core of it belongs
to earlier work (Kay, 1976). And the sweeping inference they drew — that accounting returns carry
almost no information about economic ones — did not survive: it was rebutted on the arithmetic and
on the representativeness of the chosen examples (Long and Ravenscraft, 1984), and superseded by a
literature that recovers conditional usefulness once growth and capitalisation policy are corrected
for. **The claim here is deliberately the narrower kind** — an exact equivalence with a stated
domain and a repair in §4.7, rather than a verdict of futility. The ancestor is cited for the shape
of its confound, and its fate is cited as the reason not to overreach with one.

### 4.5 · One statistic survives, and it is the one nobody can compute

Everything above concerns a *magnitude* — how much a class defers. The registration did not order
magnitudes. It ordered **lag**: how long a class takes. And the lag statistic does not invert.

| tier | lag, standards' ladder | lag, common δ |
|---|---|---|
| 0 · property, plant and equipment | 2 | 3 |
| 1 · finite-lived intangibles | 10 | 10 |
| 2 · indefinite-lived intangibles | 18 | 17 |
| 3 · goodwill | **36** | 22 |

Monotone under both, and the falling-δ ladder makes the ordering *steeper* rather than flattening
it. The reason is visible in the parameter sweep: lag falls in φ at every δ, and rises as δ falls at
every φ, so on a ladder where both move the way the standards say they do, **the two effects add.**
Across 400 randomly drawn admissible ladders the lag ordering holds in **100%** of them, against
1.9% for the magnitude measure. **Part of that margin belongs to the ladder rather than to the
statistic.** Drop the durability ordering and draw δ independently across classes, as §4.4 does, and
the lag ordering holds in **66.2%** (2,000 ladders, se 0.011) against **11.5%** for the magnitude
measure. Lag is the more robust of the two by a factor of six, and it is robust in that ratio rather
than in the way a figure of 100% suggests.

**The identification result does not, by itself, wreck a design ordered on lag.** Any claim that the
registered prediction was doomed by the φδ confound is claiming more than the arithmetic gives.

What wrecks it is the next line. **The model's lag statistic is a cross-correlation between ΔE and
ΔC, and ΔE is the change in physical value, which no filing reports.** The one statistic the
confound spares is the one that cannot be computed from public data. Any empirical instrument must
substitute something else — §5's substituted the interval from the onset of a decline in a
firm-level signal to the recognition of a charge — and the relation between that substitute and the
model's lag has never been written down.

That is a second identification gap, upstream of the first, and it is the one that bit. The
framework's response to it is §6.2's bridge discipline, which was written from the failure and now
has a theorem behind it rather than a bruise.

### 4.6 · The field's instruments read the same product

The constraint is not local to this model.

Conditional-conservatism measurement estimates how promptly accounting recognises economic losses.
The standard instruments — Basu's asymmetric-timeliness coefficient (1997), Khan and Watts's C_Score
(2009), Ball and Shivakumar's accrual–cash-flow piecewise measure (2006), Givoly and Hayn's
accumulated negative accruals (2000), Bushman and Williams's DELR (2015) — differ in construction
and share an input: a reported series, and the requirement to infer a recognition property from it.

If a timeliness parameter reaches a reported series only in product with an asset-life parameter,
then a cross-sectional comparison of any of these measures is a comparison of the product. **Two
industries with identical recognition practice and different asset lives will score differently, and
two industries with identical scores may differ arbitrarily in practice.** The sign of the induced
difference is not fixed by the measure; §4.4 shows it can invert a ranking rather than attenuate it.

**The literature has already met the confound and read it the other way up.** Khan and Watts (2009)
report that firms with longer investment cycles score as more conservative, and treat the
association as an economic determinant — a demand for verification that rises with the horizon.
Ball, Kothari and Nikolaev (2013) state plainly that firms with shorter asset maturity are expected
to exhibit lower timely loss recognition, and read that dependence as the measure behaving
correctly. Under §4.4 those are the readings a δ channel would produce whether or not any
recognition practice differed at all. The data cannot separate the two accounts, which is the whole
of the present claim; it may well be both.

**One paper has the mechanism itself, in signed form, and it is the nearest accounting-native
ancestor this result has.** Beaver and Ryan (2005) model unconditional conservatism *preempting*
conditional conservatism, and name the channel exactly: "the unconditionally conservative nature of
accelerated depreciation creates unrecorded goodwill for tangible assets that preempts conditional
conservatism as long as shocks to the market value of those assets are not negative enough to use up
that goodwill." A depreciation schedule suppressing measured timeliness — in accounting, in print,
in 2005. What it is not is an identification claim. Preemption is a signed comparative static with a
stated mechanism, and it leaves the two parameters separately meaningful; the claim here is that the
reported series does not contain the difference between them. The lineage is closer than the
pharmacokinetics of §4.2 and is owed the same acknowledgement.

The distinction from the standing critiques is what makes this worth stating. The econometric
objections to the asymmetric-timeliness coefficient — truncation from conditioning on the sign of
returns, scale effects, return-variance dependence — are **estimator** problems, and their remedies
are the estimator's: controls, fixed effects, interactive corrections, a debiased functional form.
A degeneracy is not a bias. When two parameter vectors generate the identical series, no control
recovers the difference between them, because there is nothing in the series to recover it from.
The existing repairs are aimed one level up from where the problem is.

**The sharpest of those critiques deserves separating from this one precisely, because it shares
a title-word with it and almost nothing else.** Dutta and Patatoukas (2017) decompose the
asymmetric-timeliness coefficient into a component that survives when recognition is symmetric and a
component attributable to conservatism, and show that the first is positive whenever the return
distribution is skewed, while the second moves with three properties of the news process — expected
returns, cash-flow persistence, and the skewness itself — at a fixed degree of conservatism. Two
things make that a different claim from this one. Their confounders are properties of the **news
process**; the confounder here is a property of the **asset**, its decay rate, set against a
reporting rule — and their firm is a cash-flow stream with no capitalised asset in it to carry one.
And their recognition parameter stays recoverable in their own setting, from the spread between
bad-news and good-news accrual variances, which is the repair they propose. **A claim that a better
statistic can repair is a claim about a statistic.** The claim here is that the reported series is
itself invariant, so no statistic computed from it separates the two worlds. Ryan (2006), whose
title is nearly the same as theirs, uses *identifying* in the empirical sense of detecting
conservatism in practice and makes no claim of the econometric kind.

*The notation overlap is unlucky and worth naming once:* in Dutta and Patatoukas, δ is the fraction
of bad news recognised — this paper's φ. Here δ is the physical decay rate, and has no counterpart
in their model.

Three qualifications. First, the mapping from this filter to each of those estimators is not
established here: they are not fitting this model, and the composite they read need not be φδ
exactly. Second, the magnitude-versus-timing distinction of §4.5 matters, and these measures sit on
both sides of it — Basu's coefficient is a slope on returns rather than a delay, and is closer to
this paper's magnitude case than its timing one. Third, **the theorem is proved for the reported series
alone**, and the returns-based measures condition on a second series. That second series does break
the equivalence. §4.7 gives the result and its price, and the effect on this section is to narrow
its claim rather than to qualify it: what is said here is said about a comparison of reported
series, and a design holding returns is repairing the problem rather than inheriting it.

What the paper claims is that the burden has moved. **A cross-sectional conservatism ranking now
requires an argument that asset life is constant across the compared groups, a correction for it, or
an auxiliary series that identifies it** — and the ranking most often compared, across GAAP asset
classes, is the one where the first of those is least defensible.

### 4.7 · The repair

The way out is visible in the theorem's own statement: the series determines φδ, so **anything that
supplies δ from outside the series restores φ.** Two things do, and they are priced very
differently.

**The first is the one the field already holds: returns.** A market series drawn from the same asset
breaks the two-point equivalence immediately and by a wide margin. Under the exchange the mirror
firm's asset decays at α rather than δ, so two worlds whose books agree to fourteen decimal places
differ in return by α − δ in every period — three percentage points a year, indefinitely. The
ambiguity of §4.2's first half does not survive contact with a second series drawn from the asset.

It survives the continuum, and the reason is one line. **A return is a ratio, and the residual
degeneracy is a degeneracy in the unobserved physical scale.** Grant an analyst both roots exactly —
strictly more than returns supply — and the one-parameter family is untouched: φ still sweeps [0, 1]
with the reported series reproduced to 2 × 10⁻¹⁶, and every member of that family emits the
*identical* return series, bit for bit. A scale divides out of a ratio, so no quantity of returns
data bears on the parameter the scale is concealing.

What breaks the continuum is not the returns but the **news** they carry. The degeneracy is a
property of a noiseless economic path: when the asset's value decays geometrically and does nothing
else, the reported series has a single geometric driving term and a scale factor absorbs any
rescaling of φ. Let the value receive innovations and the realised rate of decline varies from
period to period; matching the driving term then requires cα = α and cφ′ = φ *simultaneously*, which
forces c = 1. Regressing the reported series on its own lag, the return-implied path and that path's
first difference recovers α, E₀ and φ to 10⁻¹⁶ at a return volatility of 0.15, against a design
matrix that is exactly singular at zero volatility.

**So §4.6's question answers yes, and the price is a rate rather than a proof.** Identification does
not switch on at the first innovation; it fades in. Over a twelvefold range of return volatility both
the design's collinearity and the standard error on φ̂ degrade as power laws in σ, with
weak-identification bias visible in the mean by σ = 0.025. **Neither exponent is a constant of the
model, and neither should be read as one.** Across nine (α, δ) settings spanning the four decay
rates §4.4 attributes to the standards, the collinearity exponent runs from −1.07 to −0.38 and the
standard error's from −0.78 to −0.09. What holds in all nine is the sign: identification always
degrades as the asset quietens.

**What the exponents track is more useful than their values, and the two rates do different jobs.**
The decay rate governs how strongly identification *responds* to volatility; the gap between the two
rates governs its *level*. Holding the gap fixed and sweeping δ, the volatility exponent runs from
−0.39 at a property-like δ of 0.030 to **+0.16** at a goodwill-like δ of 0.002 — a change of sign
rather than a flattening, so below roughly δ = 0.01 further news stops helping and begins to hurt.
Holding δ fixed and sweeping the gap moves the *level* instead, by a factor of 6.8, as
(α − δ)^−0.70. The two must be kept apart or they read as a contradiction: a sweep at one volatility
says the decay rate hardly matters, a sweep across volatilities says it decides everything, and they
are statements about different quantities. §4.8 gives the arithmetic.

The sample cannot compensate either. The standard error **never attains the root-T rate at any
horizon**: quadrupling the panel from 50 to 200 periods buys a factor of 1.22 where root-T would buy
2.00, and from 400 to 1,600 periods it buys nothing measurable at all. Every term in the estimating
equation — signal, regressors and accrual noise alike — is proportional to the asset's remaining
value, so once the asset has decayed the later periods are not noisy observations but absent ones.
**The information about recognition speed is a property of the asset: how much its value moves, and
how long it goes on existing. The analyst chooses neither.**

Two things follow, pointing opposite ways. The first is a defence of the field's specification
arrived at from outside it. The variation that identifies φ in this filter is return variation,
which is the same variation Basu's regression requires in order to run at all; an instrument
conditioning on returns is drawing on exactly the right information, and the return-variance
corrections the literature reached for empirically are operating on the identification-strength
parameter rather than on a nuisance. The second is where that leaves the assets anyone argues about.
The corner in which every term above is worst is a quiet asset whose book amortisation rate sits
close to its true rate of decline — small σ **together with a small gap between the two rates**.
Slow decay on its own is not the hazard it looks like: at a fixed rate gap it is mildly *helpful*,
because a slow asset stays alive to be observed. §4.8 separates the two and gives the arithmetic.
What holds of both terms is that a design cannot buy its way out of either — the panel saturates
within a few half-lives whatever the volatility, and the response to news flattens and then reverses
as decay slows, so more years and more news fail together rather than in sequence.

**And the design this licenses already exists.** Beaver and Ryan (2000) decompose the
book-to-market ratio into a persistent **bias** component and a **lag** component by regressing it
"on the current and six lagged security returns with fixed firm and time effects," taking the firm
effect as bias and the returns-associated portion as lag. The regression is Ryan's (1995) — the
book-to-market ratio on current and lagged market-value changes with firm and time effects — and the
bias reading is not. Ryan's model assumes conservatism away by construction: his assumption (A8)
"eliminates the possibility of conservative accounting," and his firm effects enter as a control for
what that assumption leaves unmodelled. Beaver and Ryan supply the reading that turns a lag
regression into a two-component decomposition. That is this section's repair, run empirically
twenty-six years ago: a second series used to
separate a persistent understatement from a delay, which is exactly the separation §4.2 shows a
reported series alone cannot make. The theorem supplies a warrant the design did not have. The
measurements above supply its boundary — the strength of the separation belongs to the asset, and is
weakest where the amortisation rate sits near the asset's true rate of decline, a condition a firm
effect cannot report.

**The second repair does not require the asset to be noisy, and for most classes it is already
published.** This is the accounting form of a move the pharmacokinetic literature has long
made: the tie is broken by information the profile itself does not contain. Kuan, Wright and Duffull
(2023) observe that it is precisely "in the absence of intravenous data" that covariates describing
elimination can load onto absorption parameters, and their own proposals — a mechanistic model of
the two processes, or an estimated cutoff at which the rate constants exchange — share that shape.
An outside determination of one root releases the other, and the scale with it.

For three of the four classes, the standards already supply that outside determination. Finite-lived
intangibles and depreciable property carry **disclosed useful lives and amortisation schedules** —
an estimate of the physical decay rate, made by the firm, audited, published, and *not* derived from
the series whose timeliness is in question. Pinning δ rather than estimating it jointly is precisely
the 291-fold improvement quoted in §4.2. A design that uses disclosed useful lives as an independent
δ, and compares timeliness only within a life band, is reading φ rather than φδ, and it runs on
the sample §5 already collected.

Three properties recommend that design over the one this paper registered. It is diagonal-safe: no
comparison crosses a class boundary, so the diagonality assumption of §4.1 is not load-bearing. It
holds δ approximately constant by construction, which is the condition §4.4 identifies. And it has a
built-in negative control — the same comparison across life bands, where the theorem says the
ranking should degrade — which is the kind of prediction that can embarrass the framework rather
than decorate it.

The analogy also marks its own weak joint, and the joint is real. An intravenous dose is exogenous
in the strong sense: a different physical administration of the same compound, whose elimination
rate is set by physiology and not by the analyst's question. **A disclosed useful life is chosen by
the same management whose timeliness is being measured.** Audited and published is not the same as
exogenous, and a firm that reports slowly may also amortise slowly. Three things bound the
consequence — useful lives are anchored by industry convention and by tax and regulatory schedules,
they are sticky within a firm across the horizon over which timeliness is measured, and the design
can be run on industry-median lives rather than firm-specific ones, at the cost of resolution. The
sign of any residual endogeneity is toward finding *less* timeliness variation than exists, not
more.

**The class the repair cannot rescue is goodwill**, and the reason is not a difficulty of
measurement.

### 4.8 · The goodwill limit, and what it is a limit on

At δ = 0 the physical layer does not move; ΔE = 0; the term φ ⊙ ΔE vanishes identically; the gap is
**exactly** zero at every φ — not small, zero, at all eleven values swept — and no recognition event
occurs at any φ in 400 periods. **At zero decay, φ is not ill-conditioned. It is absent from the
dynamics.**

**That limit is narrower than it looks, and saying what it rests on is worth more than the limit
is.** The run requires two conditions, not one: δ = 0 *and* an asset whose value does not otherwise
move. Set δ = 0 and let the value receive news, and the gap reopens and φ is recovered exactly — to
3 × 10⁻¹⁵ — from the reported series and returns together. **The limit belongs to a motionless asset,
not to a slowly-decaying one.** An asset whose value never changes for any reason is not goodwill.
Impairment testing exists because goodwill's value does change; the standards decline to *schedule*
that change, which is not the same as denying it.

**What decides whether a class is readable is the gap between the two rates, not either rate alone.**
Hold α − δ fixed and sweep δ over a fifteenfold range: the standard error on φ̂ moves by a factor of
1.24, and in the direction that favours *slow* decay, since a slow asset stays alive to be observed.
Hold δ fixed and sweep α − δ over a sixteenfold range: it moves by 6.8, as (α − δ)^−0.70. At a
realistic amortisation rate the goodwill decay rate is no harder to read than property's — 0.021
against 0.023. **The unreadable case is the firm whose book amortisation rate sits close to its
asset's true rate of decline**, which is hard for the plainest reason in econometrics: the two
numbers being told apart are nearly the same number. At a gap of 0.002 the standard error is 0.13,
so φ is readable to ±0.26 — the whole interval.

The two rates do different jobs and both are needed. The gap sets the level; the decay rate sets how
strongly that level responds to volatility, and the response **changes sign**. At the fixed gap
above, the volatility exponent runs from −0.39 at a property-like δ of 0.030 to +0.16 at a
goodwill-like δ of 0.002. Below roughly δ = 0.01, a noisier asset is read *less* accurately, not
more — which is the one place in this paper where the repair of §4.7 runs backwards, and it is the
corner the standards decline to schedule.

That claim has two properties the goodwill version lacks. It is checkable by a reader against a
disclosed useful life, which §4.7 argues the standards already publish. And it does not require
inferring a physical decay rate from a reporting rule.

**What survives about goodwill specifically is a fact about this model rather than about goodwill.**
Within the deterministic filter, the class the standards decline to amortise produces no recognition
events, so the model has nothing to say about it — and the registered test drew its largest single
share from that class. That much stands and §5 pays for it. But the cause is the model's determinism
(Limitation 3), not goodwill's nature: a filter admitting stochastic degradation would speak about
goodwill as readily as about anything else, and would find it neither the hardest class nor the
easiest. **Which classes this model can speak about is decided by the δ ladder before any hypothesis
about φ is entertained** — and §4.4 now states what that ladder rests on.

**None of this was known when the registration was written, and all of it was derivable.** §5 reports
what was registered and what happened; §6 states what may now be claimed.

### 4.9 · The closed form does not need the constant hazard, and what it does need is a tail

§5.4 measures the recognition rate and, in the same fit, rejects the shape the model assumes:
discrete Weibull k̂ = 1.210, 95% interval [1.135, 1.285], stable under truncation at eight, twelve
and sixteen quarters. **R = (1 − φ)δ/(α − δ) is derived by summing a geometric**, and a geometric is
the one lag distribution whose hazard does not depend on how long the gap has been open. Everything
§4.3 and §4.4 read off that expression — the cross-class ranking, the top-rung crossing, the
domain — inherits whatever the assumption was doing. REG-004 asks what it was doing.

**It survives, and it survives as a transform.** Let a gap cohort created at time *s* be recognised
after a lag *T* ≥ 1 periods, so it sits in the gap over *s*+1 … *s*+*T*. The gap is then the flow
convolved with the lag's survival function, and with E(t) = E₀(1 − δ)ᵗ and z = 1/(1 − δ),

> **R = (1 − φ) δ Σ_{a ≥ 1} zᵃ P(T ≥ a) = (1 − φ) · ( Π(z) − 1 )**,  Π(z) = **E**[z^T]

because Σ_{a≥1} zᵃP(T ≥ a) = z(Π(z) − 1)/(z − 1) and z − 1 = δ/(1 − δ). The generating function is
evaluated **outside the unit disc**, so it is a moment generating function and not a Laplace
transform, and that is precisely why it can fail to exist. With *T* geometric at rate α,
Π(z) = αz/(1 − (1 − α)z), which at z = 1/(1 − δ) is α/(α − δ) — and the published form returns
exactly. **The constant hazard was never doing structural work. It was supplying a closed form for
one transform.**

Three checks, each of which could have ended the section. The general form reproduces the published
one at a geometric lag to **2 × 10⁻¹³**. An age-structured simulation — the gap carried as cohorts,
each aged one period and multiplied by its own P(T ≥ a+1)/P(T ≥ a), no closed form anywhere in the
loop — reproduces it at the fitted lag distribution to **2 × 10⁻¹³** against the 2 × 10⁻⁴ transient
bound §4.3 already publishes, while **rejecting** the substitution α ← 1/**E**[T] at ten times that
bound. And R(φ)/R(0) = (1 − φ) to **zero**, at every φ on a tenth-grid: φ is a pure scale under
age-dependence exactly as it is under memorylessness, so §4.2's proportionality result and every
ranking statement resting on the (1 − φ) channel alone are untouched.

**What the assumption *was* doing is holding up the domain.** R is finite exactly when
Π(1/(1 − δ)) is, which is a condition on the **radius of convergence** of the lag's generating
function and therefore on its **tail** — not on its mean, and not on any single rate. For a
geometric lag that radius is 1/(1 − α) and the condition reads α > δ, which is §4.4's domain
verbatim. For a lag whose hazard *rises*, the survival function outruns every geometric and the
generating function is entire: at k̂ = 1.21 the transform is finite at every decay rate swept, up
to δ = 0.80 per year where it is 7.5 × 10²⁵ and still a number. **The existence condition has no
analogue at the measured shape.** The general statement is the classical one for distributions with
monotone hazard: the transform converges below the limit inferior of the hazard rate and diverges
above its limit superior (Barlow, Marshall and Proschan, 1963, Theorem 6.3). A constant hazard puts
both limits at α. An increasing one puts the first at infinity — and a *decreasing* one puts it at
zero, so a lag distribution with a fattening tail would admit no steady-state deferral measure at
any positive decay rate at all. **The interval [1.135, 1.285] is therefore doing more than
rejecting a null.** It is what makes the model well-posed across the disclosed range, and had the
same fit returned k̂ < 1 the closed form would have had no domain to be restricted to.

**This does not rescue the disclosed rectangle, and the statistic that would look as though it did
is withdrawn rather than reported.** §4.4 reports the share of the rectangle inside the domain. If
the domain is everything, that share is one by construction and its complement is empty; a share of
an empty set is arithmetic, not evidence. What replaces it is the level of R, which is defined
everywhere and moves in both directions — and does.

**The correction is negligible where this paper's ladder sits and material where the filings sit.**
Against a geometric with the *same mean* — which is the comparison the constant-hazard form
implicitly makes — the measured distribution defers **less**, at every decay rate, on the direction
registered in advance from the standard reliability bound for a distribution that is new-better-
than-used in expectation (Marshall and Proschan, 1972). The size is a different question from the
sign:

| disclosed life | δ per year | R at the measured shape | R under a constant hazard | overstatement |
|---|---|---|---|---|
| 40 years | 0.025 | 0.0248 | 0.0249 | **0.6%** |
| 20 years | 0.050 | 0.0523 | 0.0530 | **1.2%** |
| 10 years | 0.100 | 0.1180 | 0.1215 | **2.9%** |
| 5 years | 0.200 | 0.3152 | 0.3445 | **9.3%** |
| 3 years | 0.333 | 0.9145 | 1.3156 | **43.9%** |

*(φ held at 0.5 throughout, since it is a common scale.)* Across §4.4's tabulated four-tier ladder,
whose fastest rate is 0.030, the worst overstatement is **0.67%**. Across the rates ASC 360 and
ASC 350-30-50 disclosure actually spans it reaches **43.9%**, at the three-year life the second of
those routinely carries. The mechanism is visible in the transform: zᵃ with z > 1 weights the tail,
and the tail is what a constant hazard gets wrong. This is not an artefact of approaching a
singularity — the constant-hazard form's pole sits at 0.435 per year, a 2.3-year life, outside the
rectangle whose fastest rate is 0.333, which is §5.4's measured rate arriving from the other
direction.

**An effective rate exists and it is not a constant.** Writing α_eff(δ) = δ Π(z)/(Π(z) − 1) returns
the published form verbatim, R = (1 − φ)δ/(α_eff − δ). But α_eff runs from **0.437** per year at a
forty-year life to **0.476** at a three-year one — a ninth of itself across the disclosed rectangle,
in the direction that a faster-decaying class behaves as though recognition were faster. Across the
four-tier ladder it moves by six parts in a thousand, which is why the magnitudes there barely move.
**A recalibration is therefore available and is not a repair:** any comparative static that holds
α_eff fixed while moving δ is using the wrong derivative, and a single recognition rate quoted for a
cross-section of asset lives misstates one end of it.

**The crossing is insensitive to the shape and sensitive to the level, and §4.4 says which.**
§4.4's δ₃\* = Kα/(1 + K) generalises exactly, to Π(1/(1 − δ₃\*)) = 1 + K. REG-004 named the two
channels in advance and they oppose: a lower R₂ lowers K and pushes the crossing down, a flatter
transform pushes it up. They very nearly cancel — the shape moves δ₃\* by **0.13%**, from 0.00755
to 0.00754, and goodwill's tabulated rate stays a factor of 3.8 inside it. The *level* moves it by
4.3%, from §4.4's 0.00789 at the calibration to 0.00755 at the measured rate, and moves something
else besides, which §4.4 now states in the table where it belongs.

**One thing the shape does not do is break the exchange.** An age-dependent world sits 5 × 10⁻⁴
from its own constant-hazard match in the reported series — four orders of magnitude below the
3 × 10⁻¹ that separated the right conserved quantity from a plausible wrong one in §4.2 — and
exactly as far from that match's mirror, which is forced rather than discovered, since the two
constant-hazard worlds are an exact mirror pair to begin with. **§4.2's degeneracy is not repaired
by age-dependence.** Whether the shape parameter itself is recoverable from a reported series is a
different question, and §4.10 measures it.

**The mathematics is old here too, and the accounting instance is what is new.** That a stationary
stock equals arrival rate times *mean* delay, whatever the delay's shape, is Little's law
(Little, 1961), and its insensitivity to shape is a property of a *constant* flow. This model never
has one: the flow is (1 − φ)δE(t) against a base decaying at δ, and the moment a base grows or
shrinks geometrically the stock-to-flow ratio becomes a transform of the delay evaluated at the
growth rate rather than its mean — the same substitution that turns a stationary population's mean
age into the Laplace transform that stable population theory carries. **The accounting literature
has the delay and not the shape.** Goodwill write-offs are known to lag economic impairment by
three to four years on average, with the delay extending to ten for a third of firms (Hayn and
Hughes, 2006); impairment timing has been modelled as a first-event hazard with covariates
(Potepa and Thomas, 2023); and conditional conservatism is measured throughout as a timeliness
coefficient. In none of it is the recognition lag's **shape** estimated rather than assumed. §5.4
estimates it, and this section is what the estimate costs the model that motivated it: less than
one per cent where the paper's own ladder sits, forty-four per cent at a disclosed three-year life,
and one domain restriction that was never a fact about disclosure.

### 4.10 · The shape is identified, and the price of admission is four significant figures

§4.2 proves an impossibility by counting. A reported series is a sum of two geometrics, so it holds
four numbers — two roots and two amplitudes — against five parameters, and the shortfall lands on φ.
That count was taken under a constant recognition hazard. §4.9 replaced the constant hazard with an
arbitrary lag distribution, which is not one more parameter but an **infinite-dimensional** object,
so the count has to be taken again: does the extra structure leave a trace in the series, or does a
constant-hazard world reproduce an age-dependent one exactly?

**It leaves a trace, and the trace has a size.** REG-005 registered the question, four falsifiers and
five ladders before `wt091` existed. The measurement is made in §4.2's *favourable* setting — the
books open square and the physical scale is granted, which is precisely what §4.2 says a firm-level
series does not supply — so a null result would have held a fortiori and a positive one carries the
condition that the asset is followed from acquisition.

**The best constant-hazard world reproduces the measured world's reported series to 3.9 × 10⁻⁴ per
quarter** over ten years at a ten-year life, rising to **4.1 × 10⁻³** at a three-year one, with the
best mimic an admissible firm at every rate and every φ swept rather than a fit escaping into
inadmissible parameters. That number is the whole answer in one figure: **it is the precision a
reported series must carry to reject the constant hazard at all.** Coarser than that and the two
worlds are the same series.

The same statement made from the other side is the set of shapes a series of given precision cannot
separate from the measured one, fitting the remaining three parameters freely at each shape:

| precision of the reported series | shapes it cannot separate from k̂ = 1.21 | width | against §5.4's 0.150 |
|---|---|---|---|
| 10⁻⁶ per quarter | 1.21 alone | 0.00 | — |
| **10⁻⁴** | **[1.16, 1.26]** | **0.100** | **0.67 ×** |
| 10⁻³ | [0.60, 1.87] | 1.27 | 8.5 × |
| 10⁻² | the whole range swept | ≥ 1.40 | ≥ 9.3 × |

*(The lower two rows run into the boundary of the pre-registered sweep, so their widths are lower
bounds; on a sweep extended to [0.2, 3.0] the 10⁻³ interval is [0.50, 1.86] and the reading is
unchanged. The search's own floor at the true shape is 2.7 × 10⁻⁸, thirty-seven times below the
finest tolerance reported, so the top row measures the model and not the optimiser.)*

**At one part in ten thousand the reported series is a better instrument for the shape than the event
dates are** — an interval of 0.100 against §5.4's 0.150 from hand-collected impairment lags. At one
part in a thousand it is an order of magnitude worse. The identification is real and it is
expensive.

**And what lies inside the interval matters more than how wide it is.** At one part in a thousand the
set reaches **k = 0.50**, below one, a *decreasing* hazard — and §4.9's tail condition says a
decreasing-hazard lag admits no steady-state deferral measure at any positive decay rate, because its
generating function diverges inside the disc the transform is evaluated on. A series matched to a
tenth of a per cent per quarter **cannot separate the world in which this model is well-posed from
one in which it has no steady state at all.** That is a sharper limit than any width, and it is the
sense in which [1.135, 1.285] was doing structural work rather than rejecting a null.

**The identified set and the estimator answer different questions, and both were registered.** The
widths above are deterministic and worst-case: every shape that *could* have produced the series.
Fitting the shape to a series carrying independent noise at the same level — 200 draws, seed
recorded — recovers k̂ with a median of **1.211** and an interquartile range of **0.125**, narrower
than the event-date interval. The two are not in tension. Forty observations average independent
noise down by a factor of six, and the estimator sees the identified set at the resulting effective
tolerance rather than at the raw one. At one part in a hundred it breaks: the interquartile range is
1.19 and a third of the draws pile on the boundary of the swept range, which is reported as a
fraction rather than as the quantiles of a censored distribution.

**A longer series does not help, and the reason is where the information sits.** The interval is not
monotone in the observation window: 1.40 over five years, 1.26 over ten, **0.98 over twenty**, and
1.32 over a hundred. The narrowest window is twenty years and a longer one is *worse*. Once the gap
reaches its steady state each further quarter repeats a single number — the deferral measure itself —
so extending the window adds redundancy to a mean and dilutes the transient that carries the shape.
This is an identification property rather than a sample-size one, which is the general result for any
finite-dimensional approximation to a lag space: the approximating families are meagre in it and
their approximation error "cannot, in other words, be made asymptotically negligible" (Sims, 1971,
§5), a statement he makes of exactly the rational lag distributions of which a constant hazard is the
lowest-order member (Jorgenson, 1966).

**Three recognition rates now live in this paper and they are three different quantities.**

| disclosed life | δ per year | α̂, the event dates | α_ser, the series | α_eff, the deferral measure |
|---|---|---|---|---|
| 40 years | 0.025 | 0.408 | 0.4383 | 0.4368 |
| 20 years | 0.050 | 0.408 | 0.4385 | 0.4388 |
| 10 years | 0.100 | 0.408 | 0.4388 | 0.4431 |
| 5 years | 0.200 | 0.408 | 0.4370 | 0.4538 |
| 3 years | 0.333 | 0.408 | 0.4037 | 0.4758 |

The series-matching constant is nearly flat across the rectangle at 0.438 per year, which is the
**reciprocal mean lag** 1/**E**[T] = 0.435 to within a per cent; α_eff rises with the decay rate
because the transform weights the tail; and α̂ is the geometric maximum-likelihood summary of the
same sample. They agree to **five parts in ten thousand** at a twenty-year life and part company at
a three-year one, where they differ by **15%** and move in opposite directions from α̂. Least squares
on the series matches the mean, the transform matches the tail, and the likelihood matches the event
dates: three functionals of one distribution, with no obligation to coincide. §4.9 says a single
effective rate misstates one end of the disclosed rectangle; the series adds that a single
*recognition rate* does not name one quantity.

**§4.2's exchange survives into all of this, and it is forced rather than discovered.** The mimic
search returns the mirror pair (α, δ, φ) and (δ, α, φδ/α) at an identical objective, which it must,
since the theorem makes the two worlds one series and any third series is equidistant from both by
construction. What the mirror costs is the mimic's own parameters: at a forty-year life the set of
worlds fitting within one part in a million of the best spans **0.128 in each root and 0.577 in φ**.
**The best-fitting constant hazard is not a world. It is a pair, and φ inside it is as free as §4.2
says it is.**

**So §4.9's open question closes with a number rather than a verdict.** The shape correction of §4.9
is recoverable from a reported series, at a precision of one part in ten thousand per quarter that
audited financial statements do not carry for the relevant quantity — which is why §5.4 dated
impairments rather than fitting a series, and why the correction travels with the lag distribution
rather than with the filings. §4.2's count is not made worse by age-dependence. The
infinite-dimensional lag does not disappear into the four numbers; it leaves a residue, and the
residue is measurable by anyone who can read a balance sheet to four significant figures.

**Two predictions registered in advance were wrong, in the same direction.** REG-005 predicted the
shape would be invisible below one part in a thousand and that the shape interval would be a hundred
times the event-date interval, reasoning from the density of rational lag distributions in lag space
and from the classical ill-conditioning of exponential sums, where a three-term signal is reproduced
by two terms to a few parts in ten thousand with rates bearing no relation to the truth (Lanczos,
1956, as quantified by Varah, 1982). The measured residue is four times larger than that reading
allows and the interval is nine times, not a hundred. Approximation theory describes what a family
can do in the limit; this is one distribution over one horizon, and it leaves more behind than the
general argument suggests. The literature's positive identification results do not close the gap
either, since recovering hazard shape there is bought with a covariate that varies, a proportionality
restriction and a moment condition (Elbers and Ridder, 1982) — and a single reported series supplies
none of the three, which is why the answer here had to be measured rather than cited.

---

## 5 · The severe test: registered, run twice, and lost

**What §4 does and does not say about what follows.** The test reported here ordered asset classes
by expected timeliness. §4.4 shows that a *magnitude* reading of such a ladder is inverted by the
composite; §4.5 shows that the *timing* reading — the one this registration used — is not. So the
identification result is not an excuse for the null, and it is not offered as one. It bears on this
section at one point only, and that point is §4.5's second half: the model's lag is defined against a
physical series that no filing reports, so the instrument below measures a substitute. Read §5 as the
record of what was predicted and what happened; §6 states what may be concluded from it.

### 5.1 · What was predicted, and when

§3 establishes a property of a model. Whether the property holds of the world is a separate
question, and no amount of prose does the work of one empirical result. The framework's sharpest available prediction is the one that
follows directly from §3.1:

> **Recognition lag scales with the unobservability of degradation.**

To test it, unobservability must be identified with something measurable. The identification
chosen was **GAAP asset class**, on the reasoning that the categories accounting standards decline
to place on an amortisation schedule are precisely the categories whose degradation is hardest to
observe. The classes and their schedules are those of the FASB *Accounting Standards Codification*:
Topic 360 for property, plant and equipment, Topic 350 for intangibles and goodwill — where the
indefinite-lived classes are tested for impairment rather than amortised, which is what makes the
recognition moment discretionary — and Topic 280 for the segment disclosures §9 identifies as the
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

### 5.4 · The same sample answers two questions it was not collected for

The stopping rule bars a third instrument for the *lag gradient*. It does not bar asking the sample
questions it was never asked. Two were registered in `REG-003`, committed and pushed before the
instrument existed, and both returned. Neither is a re-test of §5.1's prediction and neither may be
read as one.

**The sample rebuilt to within one per cent, which is itself worth one line.** `companyfacts` serves
each firm's latest view of its own history, so a re-pull is not the original pull. Rebuilt: **695
events across 307 firms** against 688 across 311, with three of four tier counts identical and
censoring at 7.7% against 7.8%. The registered reconciliation rule, fixed before the count was
known, admits this as the registered sample.

**The recognition rate is 0.41 per year, and the calibration was low by an order of magnitude.**
Each event carries the interval from the onset of deterioration to the charge, right-censored at
twenty quarters — which is α's definition, measured once per event, by an instrument built to look
at something else. The censored geometric maximum likelihood estimate is **α̂ = 0.1227 per quarter
(se 0.0046), 0.408 per year, 95% interval [0.383, 0.432]**; the median observed gap is five
quarters. Retail gives 0.433 and computer services 0.394. The three sensitivities registered with PRE-002 give
0.397, 0.499 and 0.413, and administratively censoring the sample at eight, twelve and sixteen
quarters instead of twenty gives 0.396, 0.398 and 0.404. **Every cut lands in the same regime,** and
the calibrated 0.05 is outside the interval of all of them.

**The shape was fitted rather than assumed, and it is not the model's shape.** A discrete Weibull
in Nakagawa and Osaki's (1975) parameterisation, whose hazard is increasing exactly when its shape
parameter exceeds one, so that the nesting is a boundary case and not a coincidence of fit,
gives **k̂ = 1.210, 95% profile interval [1.135, 1.285]**, excluding the constant hazard the model
assumes. The non-parametric hazard shows why: a quarter of the sample (175 of 695) is recognised one
quarter after the peak, and the rest faces a hazard rising from 0.09 to about 0.25 over the
following five years. **The longer a gap has been open, the likelier it is to close** — which is the
opposite of the memorylessness a single α encodes, and it means α̂ is an average over a window and
not a constant of the technology.

**Two biases push this estimate up, and one pushes it down; the direction of each was registered
before the number.** A gap that opened and was never recognised leaves no filing, so conditioning on
a charge over-represents short intervals. If revenue peaks after economic value has turned — the
ordinary case for a business whose customers have not yet left — the measured interval is short of
the true one. Against those, the sample contains no lag of zero, so fitting on a support that
includes it understates α̂; the unregistered shifted estimate is 0.460. **The one cut that removes
the mass where the onset bridge is least credible — the 175 events charged one quarter after the
peak — gives 0.327, still an order of magnitude above the calibration.** The result does not rest on
its most suspect quarter.

**And the reporting layer is not diagonal.** §9's ninth limitation states the assumption and names
its test: a diagonal layer predicts that recognition in one class does not force recognition in
another, so events should be independent across classes within a firm-quarter. Taking each firm's
per-class impairment frequency as given and redrawing which quarters they land in — 10,000 draws
within each firm's own eligible-quarter set — firm-quarters carrying two or more classes are

| universe | observed | null mean | central 95% | observed/expected | two-sided *p* |
|---|---|---|---|---|---|
| retail | **30** | 7.3 | [3, 12] | **4.12×** | 0.0002 |
| computer services | **44** | 21.8 | [15, 29] | **2.02×** | 0.0002 |

Both universes, the same direction, at the resolution 10,000 draws can report; the design detects an
injected excess of five per cent of events with probability 1.00. The pairwise cells put the
strongest coupling on goodwill with indefinite-lived intangibles in retail (5.83×) and on goodwill
with finite-lived intangibles in computer services (2.22×), and it is these two
intangible-with-goodwill cells that replicate across both sectors — 5.83× and 2.34×, 3.33× and
2.22×, all four surviving Holm correction. Property with goodwill runs at 4.35× and 4.03× on a
tier whose tag list omitted the element most filers use for it; `REG-006` repairs the omission and
re-derives that cell at **3.99×** and **2.17×**, the second no longer significant, so its
cross-sector agreement does not survive the repair. The headline does: **4.01× and 2.10×**
repaired, against 4.01× and 2.01× from the same crawl unrepaired.

**The mechanical reading has to be excluded before the economic one is available, §9 already
named it, and it is two readings rather than one.** The ordering is imposed by ASC 350-20-35-31,
which requires that any other asset or asset group of a reporting unit be tested before goodwill,
and by ASC 350-20-35-32, which extends that requirement to every asset tested rather than only to
those within ASC 360-10 — so it governs the intangible cells above as well as the property one. On
one channel the rule creates joint *testing*: ASC 350-20-35-3C(f) names the testing for
recoverability of a significant asset group as an event requiring an interim goodwill test, so a
single trigger fires two tests. On the other it suppresses joint *recognition*: the other charge is
recognised first and reduces the reporting unit's carrying amount, and under ASC 350-20-35-2 and
35-8 the goodwill charge is the excess of that carrying amount over fair value, so the prior charge
is subtracted from it one for one until zero or the goodwill cap binds. **Under the ordering alone
the two charges are substitutes at the margin, and this sample shows them as complements.** Signing
the net requires the two charges at the reporting-unit level, which US filings do not disclose;
`REG-006` registered an entity-level test of the suppressing channel and it returned no consistent
sign in either sector. What this design establishes is the magnitude of the departure from
diagonality, which was previously unmeasured, and that §5's treatment of the events as independent
draws overstates the information they carry.

---

## 6 · What may now be claimed, and what may not

### 6.1 · The demotion, stated exactly

**Not supported:** that recognition lag scales with the unobservability of degradation, where
unobservability is identified with GAAP asset class, in US-listed retail trade or computer and
data processing services over 2013–2024, at the firm level, at effect sizes of one quarter per
tier or larger.

**Unaffected:** every result in §A.2 and §§2–3. Those are properties of a stated model, established by
simulation and held in place by a test suite. A model result is not made false by the failure of
an empirical identification, and it is not made true by one either.

**And that sentence is a problem, not a reassurance.** If nothing in §A.2 or §§2–3 was at risk, then
nothing in §A.2 or §§2–3 was on test — and a framework that retains every claim after losing its only
public bet is in exactly the position §6.3 accuses Odum's of occupying. The accounting is therefore:

- **What was at risk and lost:** the conjunction of the model, the bridge, and the firm-level unit
  of observation. That conjunction was the framework's *entire empirical content* as of this
  writing. It is gone.
- **What was never at risk:** everything in §A.2 and §§2–3, because those are theorems about a
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

**The general form of the error is a type error in a second costume.** §A.1.1 recorded one: a
structure cannot be promoted to a proposition by rewording. This is its empirical twin — **a
quantity in the model was matched to a quantity in the world that shares its name and not its
meaning.** The lesson is not about accounting. It is that a bridge from a parameter to a measurable
must itself be stated as a proposition and checked, and this programme now requires it of every
registration.

### 6.3 · The comparison this paper is not entitled to make

An earlier draft of this section argued that the framework had escaped the trap that closed on
Odum's emergy programme — that emergy's fatal defect was making no risky predictions, and that
losing a registered bet therefore counted as a kind of methodological success.

That argument is withdrawn, on three counts a sceptical reader would have reached first.
It selects its own reference class: introduce a comparator that made no predictions and any loss
becomes a comparative victory. It is an assessment of the author's conduct rather than of the
world, and it arrives at the end of the section reporting the failure, so it would be the last
thing a reader carried away from it. A paper does not get to grade its own integrity; a reader
grades it, or does not.

What remains after the withdrawal is a fact and not an evaluation. **A prediction was registered
before the data were seen, it was tested, and it failed.** Whether that is worth anything is a
judgement this paper leaves to whoever is reading it.

---

## 7 · What was tested and survived

A paper that reports only its failures gives a reader no way to weigh them. This programme's public
record has been unbalanced in that direction: every test run is reported, and until this section
existed, none of the ones that held were collected anywhere a reader could find them. Here they are,
with what would have killed each.

| claim | test | what would have killed it | outcome |
|---|---|---|---|
| **D(φ) = (1 − φ)·D(0)** | closed form against simulation, φ swept | any φ at which the ratio departs from (1 − φ) | held to **10⁻¹⁵** |
| **(α, δ, φ) ~ (δ, α, φδ/α)** | mirrored simulation, five parameter settings | any visible separation between a series and its mirror | **7 × 10⁻¹⁴**, against 4 × 10⁻² when the mirror's φ is perturbed by 0.05 |
| **φδ is the conserved quantity, not (1 − φ)δ** | both candidate maps run against the reported series | the two maps agreeing, which would make the check vacuous | mirror **8 × 10⁻¹⁶**, rival map **3 × 10⁻¹** — the gap is preserved by one, the filing by the other |
| **An open initial gap does not restore identification** | mirror rebuilt at g₀ = 0.15 with the shifted map | the shifted map failing, or the g₀ = 0 map still working | shifted map **7 × 10⁻¹⁶**, naive map **5 × 10⁻²**; invariant (φ − g₀)δ held exactly |
| **Unobserved physical scale ⇒ φ free over [0, 1]** | one-parameter family constructed and regenerated | any member of the family failing to reproduce the series, or the family collapsing to one φ | nine members spanning φ ∈ [0, 1], **all exact to 2 × 10⁻¹⁶** |
| **Returns kill the two-point exchange** | mirror rebuilt with its own asset, return series compared | the two worlds' returns agreeing, which would leave §4.6's question open the other way | books agree to **7 × 10⁻¹⁶**, returns differ by **α − δ = 0.0300 every period** |
| **Returns cannot touch the scale continuum** | the nine-member family regenerated, return series compared across it | any member emitting a different return series | **2 × 10⁻¹⁶ — bit for bit identical** across a family spanning φ ∈ [0, 1] |
| **News, not returns, restores identification** | regression on lag, return-implied path and its first difference, σ = 0.15 | recovery failing, or the σ = 0 design being well conditioned | α, E₀, φ recovered to **10⁻¹⁶**; cond(X) **11.8** at σ = 0.15 against **4 × 10¹⁶** at σ = 0 |
| **The repair's strength is the asset's, not the analyst's** | σ swept 12×, T swept 32×, at nine (α, δ) settings | the panel buying the root-T rate, or the σ and T channels agreeing | T: 50→200 buys **1.22×** where root-T buys 2.00×, 400→1600 buys **1.00×** — regime-independent; the σ exponents are not, and are given in the two rows above |
| **Neither degradation exponent is a model constant** | both re-fitted over nine (α, δ) settings on the GAAP ladder | the nine agreeing to within fitting error, which would license quoting a number | collinearity spans **−1.07 to −0.38**, se(φ̂) **−0.78 to −0.09** — *the check that removed two numbers from §4.7* |
| **The response to news flattens as decay slows** | |exponent| ranked against δ(α − δ) | no rank relationship, which would make the spread noise | Spearman **+0.92**; at δ = 0.002 the exponent is **−0.09**, and the level is **4.7×** worse than the best regime at matched σ |
| **The goodwill limit needs a motionless asset, not a slow one** | δ = 0 rerun with the asset's value allowed to move | the gap staying zero once news is on, which would make the limit about δ | gap **0.204** against an exact 0.0, and φ recovered to **3 × 10⁻¹⁵** — *the check that rewrote §4.8* |
| **The rate gap governs readability; the decay rate does not** | each held fixed while the other is swept, 15× and 16× | the decay rate dominating, which is what §4.7 had asserted that morning | δ at fixed gap: **1.24×**, favouring slow decay. Gap at fixed δ: **6.8×**, as (α − δ)^−0.70 |
| **The two rates do different jobs** | volatility exponent re-fitted across δ at a fixed rate gap | the exponent being flat across δ, which would collapse the two findings into one | exponent spans **−0.39 to +0.16** — *a change of sign*; level spread 1.24× at σ = 0.15 against 2.16× at σ = 0.025 |
| **R = (1 − φ)δ/(α − δ)** | closed form against simulation | departure beyond the transient bound | held to **2 × 10⁻⁴**, the bound the geometric transient predicts; **1.0** when φ is misstated by 0.1 |
| **The ranking inverts, not just blurs** | 4,000 ladders drawn on the two qualitative facts alone | the intended ordering surviving often enough to be a design | recovered in **1.9%**; **100.0%** when δ is held common — the witness that the construction is not vacuous |
| **The inversion spares the lag statistic** | 400 admissible ladders, lag ordering checked | lag inverting like the magnitude measure, which would have made the story tidier | lag ordering held in **100%** |
| **The inversion belongs to the ordering; the destruction belongs to the dispersion** | 4,000 ladders with δ drawn independently, no durability ordering imposed | mean τ staying negative, which would have made the inversion the general case | mean τ **+0.32**, recovery **11.5%**, exact reversal **1.1%** — against −0.41 / 1.9% / 23.8% ordered |
| **τ = −1 is a knife edge in its top rung** | closed form for the crossing rate, verified by bisection to 1 × 10⁻⁹ | a crossing rate far above any defensible goodwill decay | **δ₃\* = 0.0079**, an eighty-seven-year half-life; the table assigns 0.002 |
| **Lumpy defers more than slow at an identical mean rate** | compound-Poisson decline, 2,000 paths, mean rate matched exactly | the ratio at or below 1, which would license reading "unscheduled" as "slow" | **1.30×** (se 0.002), a δ-equivalent of 0.0123 — above the crossing rate |
| **The design's validity region has a fitted boundary** | logistic of failure on log(leverage / budget), 4,000 ladders | a slope indistinguishable from zero | slope **+1.58**, z = **+19.5**; the same fit on a permuted outcome gives z = 0.23 |
| **The disclosed rectangle lies outside the model's domain *at the calibrated rate*** | useful lives spanning disclosure practice against α = 0.05 | any part of it admitting a steady-state deferral measure | **0%** admissible at α = 0.05; **all** of it admissible at the measured α̂ = 0.408 |
| **The recognition rate is an order of magnitude above the calibration** | censored geometric MLE on 695 registered events, two universes, three sensitivities, four truncations | any cut returning a rate near the swept 0.05 | **α̂ = 0.408/yr** [0.383, 0.432]; range **0.327–0.499** across every cut, none containing 0.05 |
| **The constant hazard the model assumes is rejected** | discrete Weibull fitted, not assumed, with a profile interval | k̂ = 1, which would have left α a constant | **k̂ = 1.210** [1.135, 1.285]; the hazard rises with the age of the gap |
| **The closed form survives an age-dependent hazard** | general form against an age-structured simulation carrying the gap as cohorts, no closed form in the loop | departure beyond §4.3's published transient bound | held to **2 × 10⁻¹³** against a 2 × 10⁻⁴ bound; the same simulation **rejects** α ← 1/E[T] at 2 × 10⁻³ |
| **φ is a pure scale under age-dependence too** | R(φ)/R(0) against (1 − φ), φ swept on a tenth-grid | any φ at which the ratio departs | held to **exactly 0.0** |
| **The domain restriction is the constant hazard's, not the disclosure's** | the transform evaluated to a proven remainder bound across the disclosed rates | divergence anywhere the bound admits | finite at every rate to δ = 0.80/yr, where it is 7.5 × 10²⁵; the geometric form is **infinite** at δ = 0.60 |
| **The shape correction is small on the ranked ladder and large at disclosed lives** | measured lag distribution against a geometric of the same mean | the two agreeing, which would make the fitted shape decorative | **0.67%** across the tabulated ladder, **43.9%** at a disclosed three-year life — and the constant-hazard pole sits outside the rectangle, so this is not a pole artefact |
| **The reporting layer is not diagonal** | 10,000 within-firm permutations of which quarters each class's impairments land in | co-occurrence at the independence rate, which the Hadamard form requires | **4.12×** and **2.02×**, both *p* = 0.0002, power 1.00 at a 5% injected excess |
| **The sample rebuilds from a live endpoint** | full re-pull of both universes a week after the original | drift large enough to make the original unrecoverable | **695 events against 688**; three of four tier counts identical |
| **Lag's 100% is partly the ladder** | 2,000 ladders, durability ordering dropped | lag holding at 100% regardless, which would have made §4.5 unconditional | **66.2%** (se 0.011) against 11.5% for the magnitude measure |
| **Results are dimensionless** | η swept over **twelve orders of magnitude** | any dimensionless output moving with η | spread **exactly 0.0** |
| …and not because η is unused | mutation testing | a mutant that leaves results unchanged | **every substituted vacuous witness killed its run** |
| **Recognition frequency is driven by δ** | sweep at fixed φ | δ having no effect on event counts | 0 → 16 → 100 events |
| **The tier instrument has no baked-in ordering** | label permutation | a non-null under randomised labels | z-mean **+0.007**, sd 1.025 |
| **The registered design had power** | power analysis, to be reported whatever the outcome | power too low to interpret a null | **0.95–1.00**, with three stated qualifications making it an upper bound |
| **The lag's shape leaves a trace in the reported series** | best admissible constant-hazard mimic, five disclosed lives x four φ | a mimic reproducing the measured shape to machine precision — the shape would not be identified at any precision | residue **3.9 × 10⁻⁴** per quarter at a ten-year life, **4.1 × 10⁻³** at a three-year one |
| **The T = 0 mass is invisible in the reported series** | conditioning on T ≥ 1 against a compensating φ, five lives x three φ | any series moving after the substitution | held to **5 × 10⁻¹⁶** — and the same conditioning moves α_eff by **6%** |
| **A decreasing-hazard lag is NOT mimicked by a constant one** | k = 0.5 witness at matched δ and φ | the metric fitting a world with no steady state as easily as the measured one | **5.4 × 10⁻³**, a **14×** separation |
| **Three recognition rates are three quantities** | series match vs. deferral match vs. event-date MLE across the disclosed rectangle | the three agreeing everywhere, making the distinction empty | agree to **7 × 10⁻⁴** at twenty years, **15%** apart at three |
| **The framework's guards can fail** | audit of the guards themselves | a guard that could not fail passing silently | **six found and retired**, before publication, recorded in `METHOD-001` |
| **The departure from diagonality is not an artefact of tier 0's tag list** | §5.4's permutation re-derived with the omitted element restored, both arms on one crawl | the lift moving with the tag list, which would make it a property of the instrument | **4.01× → 4.01×** and **2.01× → 2.10×**; every cell not involving tier 0 identical to two decimals |
| **Testing another asset first REDUCES the goodwill charge** | the single-step measurement run against a published worked example | the sequenced and goodwill-first branches agreeing, which would make the ordering inert | a \$850 prior charge converts a \$700 goodwill impairment to **\$0**; the offset is one-for-one inside the region |
| **The suppressing channel is not visible in entity-level filings** | censored slope of the goodwill charge on the other charge, by sector and by ASU 2017-04 regime, with a placebo date | a consistent negative slope, or a regime contrast the placebo could not reproduce | **failed as registered** — no consistent sign, and the placebo moved further than the true date |

Two rows deserve a comment.

The fifth is the reason this section is not decoration. The draft that preceded this one asserted
that the identification result explained the registered null. The check in that row was written to
confirm it and refused, in every one of 400 draws, and the claim came out of the paper. A survivals
ledger that contains only survivals is an advertisement; this one contains the row that cost the
paper its neatest sentence.

The last row is the one this programme would defend hardest. The claim is not that the work was
careful. It is that the guards were audited against the possibility of being unfalsifiable, that the
audit found six that could not have failed, and that they are named.

---

## 8 · Abandoned approaches

*Every route below was actually taken and then abandoned. The section is placed in the body, not an
appendix, for the reason given in the companion papers of this programme.*

**"First principles" as undeniable truths.** The original formulation asserted the framework's
foundations were undeniable. Abandoned on the argument of §A.1.1: an undeniable axiom is a
definition, and definitions forbid nothing. Several attempts to repair it by rewording failed
before the type error was identified, and that failure is instructive — a wording problem responds
to wording, and this one did not.

**The pure-delay reading of the reporting layer.** The claim layer as a simple lag on the physical
one. Abandoned because it is falsified by any case where financial signals *lead* physical change,
and those cases plainly exist. Replaced by the asymmetry of §8.1, which is strictly sharper: it
predicts *where* the lead-versus-lag boundary falls rather than denying that leads occur.

**The over-smoothing prediction.** §3.2. The framework predicted the claim layer would be less
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

**Answering the efficient-markets objection with φ.** §8.1. This was the paper's reply to its most
serious standing objection until the severe test removed its support, and it is abandoned in §8.1
rather than defended. It is listed here as well because the failure mode is the general one this
programme keeps meeting: an unmeasured parameter partitioning a space so that the objection lands
only where nothing can be checked.

**Estimating φ from the reported series alone.** The obvious route to closing §8.1's gap — fit the
model's parameters to an observed reporting layer and read φ off the fit. Abandoned because the
recovery is ill-conditioned by construction rather than by bad luck: φ reaches the observable only
through the product φδ, so estimating it means dividing by an effective decay rate that is itself
being estimated, and the variance grows like 1/δ². §4 gives the algebra and the measured
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
came out right; letting λ vary freely rather than in a shaped way; and, as §8.1 now concedes,
leaning on an unmeasured φ. A quantity that can accommodate any observation forbids nothing.

---

### 8.1 · The efficient-markets reply, withdrawn — in full

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

The partition is drawn along φ, and φ is not measured anywhere in this work — §4 concedes
it is swept, not estimated. So "the objection holds where φ is high and the model holds where φ is
low" concedes every case an efficient-markets reader could check and claims every case nobody can,
along a coordinate no one has observed. That is a free parameter absorbing an objection, which is
the move this programme has refused five times in other costumes (§8) and should have refused here.

The requirement was recognised before the severe test was run and was written down: a framework
conceding everything the efficient-markets reading claims and retaining only the unobserved residue
**must be able to identify that residue in the world**, with evidence rather than assertion. §5 is
the attempt to supply that evidence. It failed.

**So §8.1 is an open problem, not a reply.** The asymmetry remains a coherent structure and a
genuine improvement on pure delay — a pure-delay model is refuted outright by observed leads, and
this one is not. But until φ is independently measurable the asymmetry cannot be used to answer
the efficient-markets objection, and this paper does not use it that way. §2's assertion that φ
is not a fudge factor rests on the argument in this section; with that argument withdrawn, the
assertion is a statement of intent about how φ is to be treated, and it should be read as one.

### 8.2 · The crisis framing, and the paper it belongs to

The model in §2 was built to say something about crises: a deferral has one available ending —
arrival — so within the model a crisis is the reporting layer delivering its accumulated error at
once, and the magnitude of the discontinuity is exactly the information that had been withheld. That
reading survives everything in this paper. What it does not yet have is a price, an agent, an
equilibrium, or an asymmetry that a crash-risk reader would recognise as one, and the adversarial
review shipped beside this paper is unanimous and correct on the point.

So the framing is not defended here and not deleted either. The material that supported it — the
volatility-relocation result and its 2007 antecedent, the three-cell taxonomy locating the wedge in
an incentive, a belief or the measurement rule, and the priority concessions to Jin and Myers and to
Bleck and Liu — is retained in §§3.2 and 10, where it does honest work as description and
attribution rather than as a claim this paper can support.

The crash paper is a later paper in this corpus, written with a price line and after the reading
queue in §10 is discharged. **A framing that has to be argued for in the paper that introduces a
theorem is a framing that will be argued about instead of the theorem.**

---

## 9 · Limitations

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
   therefore a qualitative target, not a fitted one. **The determinism is not innocuous, and §4.8 is
   where it bites**: the goodwill limit reported there is a consequence of the physical layer being
   noiseless, and it dissolves once that layer is allowed to move for reasons other than a schedule.
   Admitting stochastic degradation is the single change to this model most likely to alter what it
   says, which is why it is named here rather than in a list of extensions.
4. **φ and θ are not measured; they are swept — and for φ the reason is §4.** α is no longer
   in that list: §5.4 estimates it at 0.408 per year on the registered sample, against the 0.05
   swept through the body, and finds the constant hazard the model assumes to be rejected. §4.9
   settles what that rejection costs: the closed form is the recognition lag's moment generating
   function evaluated at the decay rate, so it survives with an effective rate that is a function
   of δ rather than a constant, and what the constant hazard was supplying was the domain. The
   paper reports how outcomes vary across the sweep and does not claim any firm's φ is known. That is
   no longer a concession about this construction: §4.2 establishes that **no** estimator
   recovers φ from a reported series, because the series does not contain it. The consequence
   is stated there rather than softened here, together with the one repair available — an
   independent determination of δ, for which disclosed useful lives are a candidate this
   programme has not yet used. (Method, scripts and full figures for the conditioning result
   that preceded the theorem: `docs/notes/NOTE-001-phi-identifiability.md`. Synthetic data only.
   It is **not** evidence about §5's null, which used an entirely different, non-parametric
   estimator.)

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

9. **The diagonality of the reporting layer is an assumption, it was testable, and it is
   false.** §4.1 writes the reporting layer as a Hadamard product, which asserts that recognition
   in one asset class does not force recognition in another. Real practice couples them: a
   goodwill test under ASC 350-20 runs at the reporting-unit level, and the triggering event that
   forces an ASC 360 recoverability screen on property is frequently the same event. §5.4 puts
   the resulting prediction — independence across classes within a firm-quarter — to the
   registered sample and rejects it in both universes in the same direction, at **4.12×** and
   **2.02×** the independence expectation. The consequence is bounded rather than open: the
   Hadamard form is an approximation whose error is now measured, and §5's treatment of the
   events as independent draws overstates their information content by a factor this paper can
   state. What the design cannot do is separate an economic coupling from the sequencing the
   standards impose — though that sequencing, imposed by ASC 350-20-35-31 and extended to every
   asset class by 35-32, is itself two channels of opposite sign, one creating joint testing and
   one suppressing joint recognition, and §5.4 says so where the number is. It is registered
   before its instrument is coded, or it is not run.

---

## 10 · Relation to existing work

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
than moral; §2 is a formalisation of exactly that concern. Mises's malinvestment — misallocated
capital accumulating unrecognised through a boom, revealed and liquidated in the bust — is
structurally identical to §3.2: unrecognised accumulation followed by discontinuous recognition event.
The causes assigned differ (credit expansion there, undisclosed physical degradation here) and the
claim made here is a structural analogy, not an identity. What it offers is a single mechanism
reproducing a phenomenon that mutually hostile traditions each describe in their own vocabulary.

**Stock-flow consistent macroeconomics** (Godley and Lavoie) shares the insistence that accounting
identities constrain dynamics. The difference is what the accounts are taken to *be*: consistent
and complete there, consistent and **systematically incomplete** here, with the incompleteness
being the object of study.

**The efficient-markets literature**, in Fama's canonical statement of it, supplies the objection §8.1
answers — and, as §8.1 now concedes, does not yet receive an answer. What the model offers is a
partition rather than a refutation: the model concedes disclosed information entirely and retains
only the undisclosed residue.

**The stock price crash risk literature is this paper's nearest neighbour, it arrived twenty years
earlier, and the concession owed to it is larger than the contribution claimed against it.** Jin and
Myers model a firm whose insiders absorb firm-specific bad news up to a limit and then, when a long
enough run of it arrives, give up and release the accumulated stock at once; the frequency of large
negative firm-specific return outliers rises with how opaque the firm is to outsiders. Hutton, Marcus
and Tehranian supplied the firm-level opacity measure and the panel, and an active literature has
extended both continuously since. **That is §3.2 in a different vocabulary, and on evidence this
paper is much the weaker of the two accounts**: crash risk is measured on prices, tested on large
panels and supported, while §2 is a property of a simulation whose one registered prediction failed.
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

**What that case retains, and §2 removes, is an informed party.** "Saintly" qualifies capture and not
information: the manager still observes the hidden component, and it is *investors* who "cannot see
the news as it happens." Their friction is verifiability toward outsiders; §2's manager knows no more
than the market does. **Deliberately withheld known news, honestly held unverifiable news, and
unrecognised unknown degradation are three objects, and only the third is §2's.** Two further
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
identically, and the obvious discriminating tests cut against §2 rather than for it: deliberate
withholding predicts correlation with insider incentives, insider selling, litigation exposure and
regulatory regime, and the post-SOX dissipation Hutton, Marcus and Tehranian report is exactly that
pattern. Zhu (2016) runs those discriminating tests on the accruals of long-lived operating assets —
the classes §5 measures — and the agency account survives them: the crash relation concentrates in
the least reliable accrual components, strengthens where CFO option incentives are higher and where
monitoring is weaker, and is absent in non-current operating *liability* accruals. That is the
accounting layer §10 notes Jin and Myers lack, supplied for the competing explanation and not for
this one.

**The trend the agency account is losing its grip on is nonetheless real, and it is where a mechanism
without a lying manager would matter if one were established.** Andreou, Lambertides and Magidou
document that idiosyncratic crash occurrences among US-listed firms rose from 5.5% of firm-years in
1950 to 27% in 2019 — 23% across the CRSP universe and 27% once the sample is narrowed to
CRSP–Compustat–Execucomp — while the opacity– and overinvestment–crash relations they test come back
non-significant, particularly in the period after Sarbanes–Oxley. Hutton, Marcus and Tehranian report
the same dissipation in their own abstract. Those authors read their own nulls as the *conduct*
declining rather than the explanation failing, and this paper does not recruit them against that
reading. **What the trend establishes is that the space is open, not that §2 occupies it.**

**Two things must be conceded here, or §2's claim is not narrow but wrong.**

**The first is that §2's asymmetry is assumed and not derived, and that the thing which would derive
it belongs to someone else.** Jin and Myers obtain one-sidedness from symmetric primitives: the
quantity of good news insiders can absorb is unbounded because they can capture it, and the quantity
of bad news is not, so the bound is one-sided for a reason internal to the model. §2 assumes a
physical layer that only degrades. That assumption is not by itself sufficient — degradation at a
stochastic rate around a booked rate produces a two-signed reporting error, which is Jin and Myers'
case again, long tails and no skew. What makes the wedge one-signed is a second condition, that
reported value may fall and may not rise: no upward revaluation of property, plant and equipment, no
impairment reversal for goodwill or indefinite-lived intangibles. **That condition is conditional
conservatism, it is Basu's object, and §2 uses it as machinery rather than contributing it.** An
earlier draft of this section cited Basu as an obstacle to be scoped around. He is not the obstacle;
he is the part of the mechanism this programme had not noticed it was standing on. §2's claim is
correspondingly restricted to degradation on which conservatism has nothing further to bite —
carrying no impairment trigger, no estimable expected loss and no observable event to key recognition
to. Where a loss is estimable, recognition is faster than the market and §2 predicts nothing.

**The second is that the reported layer accumulating hidden deterioration and releasing it as a price
crash is a published result, and §3.2 quantifies it rather than discovering it.** Bleck and Liu model
the accounting regime itself: historical cost gives management a "veil," poor performance
"accumulate[s] and only eventually materialize[s]," and greater opacity produces more frequent and
more severe crashes. Their statement of the volatility result is §3.2's, nineteen years earlier and
in prose — historic cost "stabilizes asset prices in the short term. Under the veil of this apparent
stability, volatility actually accumulates only to hit the market at a later date," transferring
volatility across time and raising it overall. **§3.2's contribution is the parameterisation, not the
finding.** Their manager, however, is strategic and fully informed, keeping a project alive for a
private benefit while knowing it will not recover, and their regimes are two discrete alternatives
rather than a continuum. The separation from §2 is the same one that survives Jin and Myers, which is
either reassuring or the last plank.

**What is left is a claim about form.** Beaver and Ryan decomposed the divergence between book value
and economic value into a **bias** component and a **lag** component twenty-six years ago, and
Bushman and Williams connect delayed expected-loss recognition to the risk profile of banks. That
literature models conditional conservatism as a contemporaneous asymmetric response; §2 models it as
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

## 11 · Data and code availability

Every simulation result in §A.2 and §2 is produced by open code. The severe test in §5 uses only
public data.

- **Repository:** `https://github.com/jasoncbraatz/wealth-tensor` (public)
- **Modules:** `src/wealth_tensor/lag.py` · `src/wealth_tensor/lambda_sensitivity.py` ·
  `src/wealth_tensor/edgar.py`
- **Regenerate §2 (and §A.2.4):** `python3 scripts/wt027_report.py`
- **Regenerate §A.2.3:** `python3 scripts/wt002_lambda_report.py`
- **Regenerate §5:**
  `python3 scripts/wt026_severe_test.py --universe pilot --onset peak` and
  `--universe replication --onset peak`
- **Test suite:** `python3 -m pytest tests/ -q` — **100 tests at the pinned commit d655501**, which
  is the state that produced every result in §A.2 and §2. The head of the repository carries 103.
  The three later additions guard claims this paper makes and change no model code: two for §3.1's
  closed form D(φ) = (1 − φ)·D(0) and its accompanying negative claim that the lag is *not* linear,
  and one asserting the algebraic collapse §4 publishes — which had no test until an
  audit found the published form using the entropy rate where it meant the effective decay.
- **Hardware:** none required. Every figure in §A.2 and §2 regenerates on a commodity CPU in seconds.
  The fits reported in §4 use two thousand synthetic firms at four hundred gradient steps
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

# Appendix A · The framework the filter was built inside

*Three propositions about the composition of wealth, and the coupling they oblige. This material
motivated the filter and is retained in full: it states the domain within which §2's two layers are
the right two layers, and it carries the invariance evidence the ledger in §7 cites. It is an
appendix rather than a section because **nothing in §§2–7 depends on it.** The identification
result holds for any two-layer filter of the stated form, whatever one believes about the
composition of wealth — and a result that needs a metaphysics is weaker than one that does not.*

## A.1 · Three propositions

### A.1.1 · What a first principle is, and what it is not

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

### A.1.2 · The propositions

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

### A.1.3 · The propositions are deniable, and this repository proves it

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

### A.1.4 · Independence

P1 concerns composition and is silent about time. P2 concerns time and presupposes only that a
physical component exists — it is not derivable from P1, since a compound whose physical component
were inert would satisfy P1 and violate P2. P3 concerns the relation between measurements at
different scales and is independent of both: an economy of inert single-component units would
satisfy P3 while violating P1 and P2. No proposition is derivable from the others, and each is
denied by an identifiable school.

---

## A.2 · The coupling

*This section is where Λ is defended. It is defended here, at full strength, on three independent
legs, and then it is used for the rest of the paper without further apology. That is a deliberate
posture and it is worth naming: a defence that recurs is a tell. Five defences of one quantity
inform a referee that there are five soft places, and recruit attention to precisely the ground an
author would rather they walked over.*

### A.2.1 · Λ is obliged by P1, not introduced

**Notation, stated before the argument because two different objects have been sharing one symbol
in this programme's working notes.** Write **C** for the claim component and **E** for the physical
component. Then:

- **λ = C/E** is **dimensionless** — a ratio of the claim measure to the physical measure once both
  are expressed in the same numeraire. This is the object §A.2.4 reports as a sawtooth, and it is the
  one with dynamics.
- **Λ = η·C/E** is **dimensional**, carrying units of currency per joule, where η is the numeraire
  conversion. This is the object the standing dimensional objection is aimed at, and the object
  §A.2.3 sweeps.

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
prove.** What follows in §A.2.3 is a demonstration that no conclusion here depends on the scalar's
*value*, which is a different and weaker guarantee than showing the scalar is the right object —
and the difference is exactly the kind of thing §6.2 will show this programme has previously
glossed over at its cost.

λ is not stable, and §A.2.4 shows what shape its instability takes.

### A.2.2 · Λ⁻¹ is an indicator the United Nations already publishes

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

**And it is a weaker leg than §A.2.3, which should be said plainly rather than left to a referee.**
If, as §A.2.3 demonstrates, no conclusion in this paper depends on the coupling's value, then
anchoring that value to a published statistic cannot be load-bearing for any result here. The two
legs answer different objections — §A.2.3 answers *"your findings are an artefact of a number you
made up"*, and this section answers *"the dimension you are working in is invented"* — and only the
first is doing work for the results. A reader who finds this section unconvincing loses nothing
downstream.

### A.2.3 · The numeraire cancels — measured, not argued

The dimensional objection can be answered by algebra, and algebra is exactly what a sceptical
reviewer declines to take on trust. So the two-layer system of §2 is **dressed in units** — the
physical layer in joules at scale E₀, the claim layer in currency, the coupling η between them —
and the invariance is measured on the dressed system.

Sweeping η across twelve orders of magnitude, from 10⁻⁶ to 10⁺⁶ currency units per joule, at
**φ = 0.3, recognition mechanism live, 400 periods** (the diagnostics below are the same statistics
§3.2 reports, under **this paper's names**; the module and `scripts/wt002_lambda_report.py` call them
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

### A.2.4 · Λ is not a constant that wobbles; it is a sawtooth

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
issue pagination given here; quotations from it are cited without page numbers for that reason. §10
takes both the 5.5%→27% figure and the universe split from it directly: the 27% is the
CRSP–Compustat–Execucomp sample and the CRSP-wide figure is 23%, a distinction the abstract does not
make and the body does.)*

Basu, S. (1997). The conservatism principle and the asymmetric timeliness of earnings. *Journal of
Accounting and Economics*, 24(1), 3–37. ✓ *(Cited for the asymmetric-timeliness result named in its
own title. **Read at source**; the volume, year and page range are confirmed against the typeset
article, which earlier revisions of this entry could not obtain. Nothing is quoted from it.)*

Ball, R., Kothari, S. P., & Nikolaev, V. V. (2013). Econometrics of the Basu asymmetric timeliness
coefficient and accounting conservatism. *Journal of Accounting Research*, 51(5), 1071–1097. ✓
*(§4.6 cites it for its stated expectation that firms with shorter asset maturity exhibit lower
timely loss recognition, and for reading that dependence as the measure behaving correctly. **Read at
source** in this revision and the characterisation held: the passage sits in their §4.4, headed
"Other Determinants of Conditional Conservatism," and the expectation is stated of "companies with
short operating cycles, short investment cycles, or short asset maturity." The determinant reading is
theirs and is explicit — they conclude that the measure "is unbiased under the null hypothesis of
zero asymmetry, and that under the alternative hypothesis it captures conditional conservatism," in
direct rebuttal of the invalidity critiques. Asset maturity is one of several examples they give of a
comparative static, not their headline; §4.6 is worded accordingly. **No page is cited**: the text
consulted was a full-text copy reporting itself as the published article, not the typeset original,
and the MIT deposit (handle 1721.1/87767 — *not* 87766, which is the different 2013 paper in *The
Accounting Review*) refused every retrieval route attempted, so nothing is quoted beyond the two
phrases above and no absence is claimed of the typeset article.)*

Bateman, H. (1910). The solution of a system of differential equations occurring in the theory of
radioactive transformations. *Proceedings of the Cambridge Philosophical Society*, 15(V), 423–427. ✓
*(Cited for the function that bears its name and for nothing else; §4.2 characterises only the
functional form, which is standard. The bibliographic record is from catalogue listings rather than
the author's own copy, and no text is quoted.)*

Beaver, W. H., & Ryan, S. G. (2000). Biases and lags in book value and their effects on the ability
of the book-to-market ratio to predict book return on equity. *Journal of Accounting Research*,
38(1), 127–148. ✓ *(Cited for the bias/lag decomposition named in its own title. §10 identifies this
as the closest prior art to §4's filter, so the entry is load-bearing against this paper rather than
for it. **Read at source**; §4.7 quotes their method — regressing the ratio "on the current and six
lagged security returns with fixed firm and time effects" — from **p. 128**. The sentence recurs at
p. 135 as "six lagged *annual* security returns", which is not the wording quoted. That design is
this paper's returns repair carried out twenty-six years earlier, and the decomposition is theirs:
Ryan (1995) supplies the regression and assumes conservatism away.)*

Beaver, W. H., & Ryan, S. G. (2005). Conditional and unconditional conservatism: concepts and
modeling. *Review of Accounting Studies*, 10(2–3), 269–309. ✓ *(**Read at source.** Cited in §4.6 as
the nearest accounting-native ancestor of the present confound: their preemption mechanism runs a
depreciation schedule against measured conditional conservatism explicitly. One sentence is quoted,
from their development of the tangible-asset case. Theirs is a signed comparative static and not an
identification claim, and §4.6 says so rather than recruiting it.)*

Bellman, R., & Åström, K. J. (1970). On structural identifiability. *Mathematical Biosciences*,
7(3–4), 329–339. ✓ *(Cited in §4.2 for the definition of structural identifiability and the
transfer-function criterion, which is what the source is characterised on. Characterised at
abstract level; the pole-set consequence drawn in §4.2 is this paper's statement of the mechanism,
not theirs.)*

Barlow, R. E., Marshall, A. W., & Proschan, F. (1963). Properties of probability distributions with
monotone hazard rate. *The Annals of Mathematical Statistics*, 34(2), 375–389. ✓ *(§4.9 cites
Theorem 6.3, which is quoted in the paper in the form used here: the moment generating function is
finite below the limit inferior of the hazard rate and infinite above its limit superior. That
theorem is what turns this model's α > δ into a statement about the recognition lag's tail. The
paper's equation (6.2) — a hazard bounded between two constants bounds the survival function
between the corresponding exponentials — is the same result in the form a reader may find more
familiar.)*

Bleck, A., & Liu, X. (2007). Market transparency and the accounting regime. *Journal of Accounting
Research*, 45(2), 229–256. ✓ *(Read in full text; the copy consulted carries the journal's own title
page — vol. 45 no. 2, May 2007, DOI 10.1111/j.1475-679X.2007.00231.x — so it is the typeset article
and not a pre-publication version. §4.4 and §10 both cite it against this paper: it states §4.4's
volatility result nineteen years earlier.)*

Bushman, R. M., & Williams, C. D. (2015). Delayed expected loss recognition and the risk profile of
banks. *Journal of Accounting Research*, 53(3), 511–553. ✓

Elbers, C., & Ridder, G. (1982). True and spurious duration dependence: the identifiability of the
proportional hazard model. *The Review of Economic Studies*, 49(3), 403–409. ✓ *(§4.10 cites it
for what identification of a hazard's shape costs elsewhere in the literature: a regressor with
variation, a proportionality restriction and a moment condition on the mixing distribution. **The
text was not consulted.** The bibliographic record is verified; the characterisation is taken from
two independent secondary sources that state it identically, and the entry claims nothing beyond
it. The point §4.10 draws is that a single reported series supplies none of the three, which is
why that section measures rather than cites.)*

Fama, E. F. (1970). Efficient capital markets: a review of theory and empirical work. *Journal of
Finance*, 25(2), 383–417. ✓

Financial Accounting Standards Board. *Accounting Standards Codification*, Topic 350 — *Intangibles —
Goodwill and Other*; Topic 360 — *Property, Plant, and Equipment*; Topic 280 — *Segment Reporting*. ✓

Garrett, E. R. (1994). The Bateman function revisited: a critical reevaluation of the quantitative
expressions to characterize concentrations in the one compartment body model as a function of time
with first-order invasion and first-order elimination. *Journal of Pharmacokinetics and
Biopharmaceutics*, 22(2), 103–128. ✓ *(Cited in §4.2 as the bridge between the Bateman function and
the flip-flop phenomenon, which its own title and abstract establish. Characterised at abstract
level; nothing is quoted.)*

Georgescu-Roegen, N. (1971). *The Entropy Law and the Economic Process*. Harvard University Press. ✓✎
*(The copy consulted is the Harvard Paperback second printing, 1974, ISBN 0-674-25781-2; a printing is
not an edition, so no dual date.)*

Godley, W., & Lavoie, M. (2007). *Monetary Economics: An Integrated Approach to Credit, Money, Income,
Production and Wealth*. Palgrave Macmillan. ✓✎ *(Copy consulted confirms first published 2007, ISBN
978-0-230-50055-6.)*

Hayek, F. A. (1945). The use of knowledge in society. *American Economic Review*, 35(4), 519–530. ✓

Khan, M., & Watts, R. L. (2009). Estimation and empirical properties of a firm-year measure of
accounting conservatism. *Journal of Accounting and Economics*, 48(2–3), 132–150. ✓ *(§4.6 cites it
both for C_Score and for its reported association between longer investment cycles and higher
measured conservatism. Characterised at abstract level.)*

Kuan, I. H. S., Wright, D. F. B., & Duffull, S. B. (2023). The influence of flip-flop in population
pharmacokinetic analyses. *CPT: Pharmacometrics & Systems Pharmacology*, 12(3), 285–287. ✓ *(Cited
in §4.2 for the classification of flip-flop as a failure of global rather than local
identifiability. **Read at source** (PubMed Central PMC10014047). They write of *local*
identifiability rather than of a failure of global identifiability, and §4.2 uses their adjective.
Their concluding sentence qualifies the "finite set" formulation as "not just a finite set of
parameter values but a partial permutation of the set"; §4.2 carries that qualification too. Two
short phrases are quoted; no page is cited, the article running to three pages without internal
pagination in the deposit consulted.)*

Dutta, S., & Patatoukas, P. N. (2017). Identifying conditional conservatism in financial accounting
data: Theory and evidence. *The Accounting Review*, 92(4), 191–216. ✓⧗ *(Cited in §4.6 as the
nearest existing claim and the one most needing separation. The **text** consulted is the open UCLA
Anderson working-paper version, read in full for the decomposition, the three named confounders and
the accrual-variance-spread repair; the displayed algebra rendered unreliably in that copy, so
nothing interior to their coefficient B is asserted here and no page is cited. Pagination of the
published article is verified bibliographically and has **not** been checked against the working
paper's.)*

Fisher, F. M., & McGowan, J. J. (1983). On the misuse of accounting rates of return to infer
monopoly profits. *American Economic Review*, 73(1), 82–97. ⧗ *(Cited in §4.4 for the shape of its
confound — a reporting-rule parameter against an asset-life parameter inside a published ratio — and
for the fate of the inference drawn from it. **Not read**; the record is verified and the
characterisation rests on the Long and Ravenscraft comment below, whose working-paper version was
read in full, and on secondary accounts. No quotation is taken from it.)*

Hayn, C., & Hughes, P. J. (2006). Leading indicators of goodwill impairment. *Journal of
Accounting, Auditing & Finance*, 21(3), 223–265. ✓ *(§4.9 cites it for the two figures its abstract
states: goodwill write-offs lag the economic impairment of goodwill by an average of three to four
years, and for a third of the companies examined the delay extends up to ten. Cited for the
existence and length of the delay, which it establishes, and not for its shape, which it does not
model. The page range is the publisher's landing-page range and was not checked against the typeset
issue.)*

Jorgenson, D. W. (1966). Rational distributed lag functions. *Econometrica*, 34(1), 135–149. ✓
*(§4.10 cites it for the density result — that an arbitrary distributed lag may be approximated to
any desired accuracy by a rational lag function, of which a constant hazard is the lowest-order
member — which is the reason REG-005 predicted the shape would be invisible. Verified at abstract
level against the Econometric Society's own record, from which the approximation claim is taken
verbatim; the body was not read and nothing else is attributed to it.)*

Lanczos, C. (1956). *Applied Analysis*. Englewood Cliffs, NJ: Prentice-Hall. *(§4.10 cites the
exponential-decomposition example at pp. 272–280 for the classical ill-conditioning of
exponential-sum fitting. **Not read**, and the entry carries no verification mark for that reason:
every copy located was lending-restricted and no full text was obtained. The page range is from the
NIST Statistical Reference Datasets documentation of the same example, and everything §4.10 draws
from it is drawn through Varah (1982), which quotes it with page citations. Nothing here rests on
it alone.)*

Little, J. D. C. (1961). A proof for the queuing formula: L = λW. *Operations Research*, 9(3),
383–387. ✓ *(§4.9 cites it for the distribution-free stationary identity — average number in system
equals arrival rate times average time in system — and, more to the point, for what that identity
requires: a constant arrival rate. This model never has one, which is why its deferral measure is a
transform of the lag rather than its mean. Characterised from the result named in the title;
nothing is quoted.)*

Marshall, A. W., & Proschan, F. (1972). Classes of distributions applicable in replacement with
renewal theory implications. In *Proceedings of the Sixth Berkeley Symposium on Mathematical
Statistics and Probability*, Volume I. Berkeley: University of California Press. *(§4.9 cites it for
the new-better-than-used-in-expectation bound that signs the correction: an NBUE distribution's
moment generating function is dominated by that of the exponential with the same mean.
**Deliberately unmarked.** The Berkeley Symposium volume was not consulted and the page range is
omitted rather than guessed; the attribution is taken from the reliability literature that rests on
it. §4.9 does not depend on the citation, since the direction it predicts is also measured
directly — but the reasoning that produced the prediction is this lemma's and is credited as such.)*

Nakagawa, T., & Osaki, S. (1975). The discrete Weibull distribution. *IEEE Transactions on
Reliability*, R-24(5), 300–301. ✓ *(§5.4's fitted lag distribution is this one, in the survival
parameterisation P(T ≥ t) = q^(t^k) the source defines, whose discrete hazard is increasing exactly
when k ≥ 1 and which nests the geometric at k = 1. Named here because a distribution fitted and
reported ought to say whose it is.)*

Potepa, J., & Thomas, J. (2023). Goodwill impairment after M&A: acquisition-level evidence.
*Journal of Financial Reporting*, 8(2), from p. 131. ✓⧗ *(§4.9 cites it as the closest existing
treatment of impairment *timing*: their design tracks each acquisition to its first impairment
within a ten-year window and stops, which their own text describes as effectively a hazard model.
It is cited for what it is and for what it is not — a covariate model with no baseline shape
estimated — which is the gap §5.4's fit occupies. The text consulted is the authors' working paper
rather than the typeset article, hence ✓⧗; the end page could not be confirmed from an open source
and is omitted rather than guessed.)*

Kay, J. A. (1976). Accountants, too, could be happy in a golden age: The accountant's rate of profit
and the internal rate of return. *Oxford Economic Papers*, 28(3), 447–460. ⧗ *(Cited in §4.4 for the
analytical result that precedes Fisher and McGowan's numerical demonstration. **Not read**; record
verified, characterisation from secondary sources.)*

Long, W. F., & Ravenscraft, D. J. (1984). The misuse of accounting rates of return: Comment.
*American Economic Review*, 74(3), 494–500. ✓⧗ *(Cited in §4.4 for the rebuttal. The **text**
consulted is the open FTC Bureau of Economics Working Paper No. 94, June 1983, read in full; the
published comment is verified bibliographically and has not been read. Nothing is quoted.)*

Ryan, S. G. (1995). A model of accrual measurement with implications for the evolution of the
book-to-market ratio. *Journal of Accounting Research*, 33(1), 95–112. ✓ *(Cited in §4.7 for the
regression Beaver and Ryan (2000) adopt. **Read at source**, with the Autumn 1995 erratum at 33(2),
417, which corrects two typesetting errors in equation (5) — a "+" printed for the "=", and
ΔMV_{i,t−10} printed for BV_{i,t−10} — and changes no coefficient, hypothesis or result. The
erratum's γ term is absent from the equation §4.7 relies on, which is Beaver and Ryan's (4). Ryan's
assumption (A8) "eliminates the possibility of conservative accounting," and his firm effects are a
control for what that leaves unmodelled; the bias/lag reading is Beaver and Ryan's. In 1995 the
journal carried the name given here.)*

Ryan, S. G. (2006). Identifying conditional conservatism. *European Accounting Review*, 15(4),
511–525. ✓ *(Cited in §4.6 solely to distinguish a near-identical title. **Read at source.** The
characterisation holds and is now supported by the body rather than the abstract: the word
"econometric" does not occur in the article, and "identify" and its cognates are used throughout in
the empirical sense of detecting conservatism in data. Nothing is quoted.)*

Sims, C. A. (1971). Distributed lag estimation when the parameter space is explicitly
infinite-dimensional. *The Annals of Mathematical Statistics*, 42(5), 1622–1636. ✓ *(§4.10 cites it
for the conclusion that finite-dimensional approximations to a lag space are meagre in it and that
their approximation error "cannot, in other words, be made asymptotically negligible" — quoted
from §5, p. 1634 — and for his naming of "the finite-dimensional parameter spaces of rational lag
distributions (see Jorgenson (1966))" as exactly the approximating class the result covers, p. 1628.
The text consulted is an optically-recognised scan rather than the typeset original; the volume,
issue and page range are confirmed against the journal's own table of contents. **The journal is the
*Annals of Mathematical Statistics*, not *Econometrica*, and the title word is "explicitly", not
"essentially" — this entry is commonly miscited on both counts.**)*

Varah, J. M. (1982). *On fitting exponentials by nonlinear least squares.* Technical Report TR-82-02,
Department of Computer Science, University of British Columbia. ✓ *(§4.10 cites it for the
quantified form of Lanczos's example, and it is the route by which Lanczos is cited at all. **Read
in full.** It attributes the observation to "Lanczos (1956, pg. 279)" and locates the data at p. 273,
and reports the Hessian's smallest eigenvalue falling by roughly three orders of magnitude per
additional exponential term. A later journal version is believed to exist and was **not** verified,
so the technical report is what is cited and what was read.)*

Nerlove, M. (1958). *The Dynamics of Supply: Estimation of Farmers' Response to Price.* Baltimore:
Johns Hopkins Press. ⧗ *(Cited in §4.2 for the combined adaptive-expectations/partial-adjustment
model, whose reduced form is the closest economics-native analogue of this paper's exchange
symmetry. **Not read.** The bibliographic record is verified; the reduced-form algebra attributed
here — symmetry of every systematic coefficient in β ↔ γ, asymmetry of the disturbance — was
derived and checked in this repository (`scripts/wt085_returns_conditioning.py`, E7) rather than
taken from Nerlove's text, and the entry claims nothing beyond the model's structure. A session with
library access should read the monograph, and Askari and Cummings's 1977 survey of the Nerlove
literature, before this is upgraded.)*

Hutton, A. P., Marcus, A. J., & Tehranian, H. (2009). Opaque financial reports, R², and crash risk.
*Journal of Financial Economics*, 94(1), 67–86. ✓ *(Nothing is quoted from the body, which was read
as full text rather than as the typeset article. The post-SOX dissipation §10 attributes to them is
from the published abstract, checked at source.)*

International Energy Agency & United Nations Statistics Division. *SDG Indicator 7.3.1 — Energy
intensity measured in terms of primary energy and GDP.* Reported as World Bank series
`EG.EGY.PRIM.PP.KD`, *Energy intensity level of primary energy*, compiled for *Tracking SDG 7: The
Energy Progress Report* by the IEA, IRENA, UNSD, the World Bank and the WHO. ✓

Jin, L., & Myers, S. C. (2006). R² around the world: New theory and new tests. *Journal of
Financial Economics*, 79(2), 257–292. ✓ *(**Read at source**, typeset article. §10's one quotation —
"For simplicity, we ignore depreciation and reinvestment" — is verified in the published text at
**p. 262**, character for character; an earlier revision of this entry recorded it as checked only
against NBER Working Paper 10453 and flagged the risk that the referee process had altered it. It
had not. §10 quotes the sentence because it is what establishes that the model has no physical layer,
and a reader entitled to doubt that on a paraphrase should be able to see the words. Its footnote 3
is worth reading beside §4: the authors set aside depreciation "according to a pre-defined schedule"
as an easy extension, and it is the interaction of exactly that schedule with recognition timeliness
that §4.2 shows a reported series cannot resolve.)*

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
2013. §10's relocation argument is about work that existed a year before the English text cited here.)*

Popper, K. R. (1935/2002). *The Logic of Scientific Discovery*. Routledge Classics. ✓✎ *(The copy
consulted is the Routledge Classics edition of 2002. Its own colophon gives the chain:* Logik der
Forschung *first published 1935, Vienna — its preface dated 1934 — first English edition Hutchinson &
Co., 1959, Routledge from 1992. §10 cites Popper for the demarcation criterion, which is 1935's, not
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

Zhu, W. (2016). Accruals and price crashes. *Review of Accounting Studies*, 21(2), 349–399. ✓
*(Cited in §10 against §2. **Read at source**, typeset article. High accruals predict firm-level
weekly price crashes; the relation concentrates in the components Richardson, Sloan, Soliman and
Tuna rank least reliable, including non-current operating asset accruals, and strengthens with CFO
option incentives and weaker monitoring. The negative loading on current operating liability
accruals is reported by Zhu as unexplained by his own mechanism, and is noted here for the same
reason. Nothing is quoted.)*

*How this list was checked, recorded because a reference section that silently improves teaches a
reader nothing. The per-entry findings live in the ✓, ✓✎ and ✓⧗ notes above, attached to the entries they
describe, so that correcting an entry cannot leave a summary of it behind.*

**Four passes ran, in this order, and each one found what the previous ones structurally could not.**

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
   §10 being attributed to the working paper it was actually read in rather than to the journal.

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
