<!-- wealthTensor-108 · extracted verbatim from docs/papers/paper-III-dual-tensor/paper-III.md
     lines 2127-2378, at commit c75343c. Do not edit here and there. -->

# Appendix A, in full · the framework the filter was built inside

*Paper III's Appendix A (`paper-III-v1.md`) is the short form and says so: it carries the three
propositions, their domains, their independence and the boundary SMD draws on P3, and it points
here for the rest. **This file is that rest** — the three-leg defence of the coupling Λ and the
invariance evidence — extracted verbatim from the v0.x draft of Paper III, which remains on `main`
and under tag `v1.0-preprint` with all guards passing.*

*Section numbering below is the v0.x draft's own (A.1.1–A.2.4) and does not match `paper-III-v1.md`'s
A.1–A.4. That is deliberate: this is a quotation, not a rewrite, and a quotation that renumbers
itself is no longer verifiable against its source.*

---

# Appendix A · The framework the filter was built inside

*Three propositions about the composition of wealth, and the coupling they oblige. This material
motivated the filter: it states the domain within which §2's two layers are
the right two layers, and it carries the invariance evidence the ledger in §7 cites. It is an
appendix rather than a section because **nothing in §§2–7 depends on it.** The identification
result holds for any two-layer filter of the stated form, whatever one believes about the
composition of wealth — and a result that needs a metaphysics is weaker than one that does not.*

## A.1 · Three propositions

### A.1.1 · What a first principle is, and what it is not

An appeal to "first principles" is worthless without a definition of the term, and the gap is not
a wording problem — it is a type error, and type errors do not respond to prose:

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
by assertion. Here it is demonstrated for **one** of the three, because the regime in which P2
fails is committed, tested code rather than a thought experiment. P1 and P3 are argued deniable
in §A.1.1 and §A.1.4 and are not demonstrated in code, and the second item below is the
mechanism's own switch-off rather than a proposition:

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

*A companion result on the same theme is cited rather than reproduced: **Paper II** of this
programme reports that a levy whose base cannot observe an accrual is inert regardless of its
rate, and the evidence for it belongs to that paper. The identification of the two mechanisms that the
shared theme invites is withdrawn. Put to a cross-scale check it does not hold: what this paper's filter fails to recognise is deferred, held in the gap and
released at rate α, while what a levy's base fails to recognise is never assessed at all, and a
levy has no parameter that plays α's part. The two results share the question and not the
operator. The check, and the fact that the withdrawal was written down before it was run, are
recorded in `docs/RESULT-END-TO-END-001-E1.md`.*

### A.1.4 · Independence

P1 concerns composition and is silent about time. P2 concerns time and presupposes only that a
physical component exists — it is not derivable from P1, since a compound whose physical component
were inert would satisfy P1 and violate P2. P3 concerns the relation between measurements at
different scales and is independent of both: an economy of inert single-component units would
satisfy P3 while violating P1 and P2. No proposition is derivable from the others, and each is
denied by an identifiable school.

---

## A.2 · The coupling

*This section defends Λ, at full strength and on three independent legs; the rest of the paper
then uses it without re-arguing it.*

### A.2.1 · Λ is obliged by P1, not introduced

**Notation, stated before the argument because two different objects are easily conflated under
one symbol.** Write **C** for the claim component and **E** for the physical
component. Then:

- **λ = C/E** is **dimensionless** — a ratio of the claim measure to the physical measure once both
  are expressed in the same numeraire. This is the object §A.2.4 reports as a sawtooth, and it is the
  one with dynamics.
- **Λ = η·C/E** is **dimensional**, carrying units of currency per joule, where η is the numeraire
  conversion. This is the object the standing dimensional objection is aimed at, and the object
  §A.2.3 sweeps.

Conflating them is easy. Everything below is explicit about which
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
and the difference is exactly the kind §6.2 is about.

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

**This leg is weaker than §A.2.3's.**
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
difference **exactly 0**, at φ = 0.3 over 300 periods. (The shorter horizon is stated because it changes the values: at 300 periods the
system has had 12 recognition events rather than 16, and inter-event smoothing reads 0.6100 rather than
0.6097. The *collapse* is horizon-independent; the numbers collapsed onto are not.)

The sentence this licenses, and the paper will not need to say it twice: *the conversion
coefficient is a numeraire; every result reported here is invariant to it across twelve orders of
magnitude, while every currency-denominated quantity scales with it exactly linearly.*

### A.2.4 · λ is not a constant that wobbles; it is a sawtooth

*Throughout this section the object is **λ = C/E**, the dimensionless ratio of §A.2.1 — not the
dimensional **Λ = η·C/E** swept in §A.2.3. The numeraire enters nothing below.*

A freely-varying λ that is never pinned would forbid nothing, and a quantity that forbids nothing
is the free parameter this programme has refused three times in other costumes. So the claim is not
that λ *varies*. It is that λ varies **in a specific parameterised shape**, and the shape is a
prediction.

At φ = 0.3 over 400 periods, with the recognition mechanism live:

| | value |
|---|---|
| mean λ | 1.136838 |
| minimum λ | 1.000000 |
| maximum λ | 1.245384 |
| recognition events | 16 |
| λ = 1 exactly at every recognition event | **yes, all 16** |

**λ equals its physical value only at the instants the claim layer snaps to the physical one, and
overstates it by ~14% across the run.** Floor pinned at unity by construction of the
recognition event; ceiling set by observability; mean determined by φ. That is a shaped variable, not a
free one — and it is the picture of the assertion that λ's drift *is* the accumulated deferred
information.

---
