# The tensor composes, the behaviour does not: one atomic unit from the household to the sovereign

**Jason C. Braatz**
*Independent researcher*
jason@braatzresearch.com

**Draft — not yet submitted.** Version 0.1, 2026-08-16.

**Declaration of interest.** The author is employed by a company building accounting software for very small businesses. This work was conducted independently, on personal time, and without company funding, data or direction.

**Use of AI assistance.** Anthropic Claude Opus 5, at high reasoning effort, was used throughout as a research and drafting assistant: literature retrieval, adversarial review, code review and prose drafting. All claims, results and final text are the author's, and every computational result is produced by committed code in the repository named in the data-availability statement.

---

## Abstract

Three literatures describe wealth and do not read each other: biophysical economics, stock-flow
consistent macroeconomics, and kinetic-exchange econophysics. This paper joins them on one claim —
the same atomic unit composes from the household to the sovereign — and states exactly where
composition stops.

The unit is an **extensive state**, and extensive states add. **Behavioural maps do not**, and the
theorem saying so is Sonnenschein–Mantel–Debreu. SMD is therefore not an objection to composition
across scales; it is its boundary. **Aggregation preserves the extensive state and destroys the
behavioural map** — so a discipline that aggregates in order to recover behaviour is estimating the
half that does not survive, while the half that does, the physical stock and the claim recorded
against it, is largely unmeasured.

A worked instance at the smallest scale: for a single indivisible good, 25 allocations of one
population yield 25 demand schedules, 25 supply schedules and **one** excess-demand schedule, and
the crossing height is not a behavioural aggregate but the allocation mismatch.

The motivating whitespace is measured, not asserted. A pre-registered co-citation instrument
returns a split-half ceiling of **0.477**, a floor of exactly **0.000** against a literature
unrelated by construction, and target overlaps of **0.020, 0.011 and 0.005** — one pair undecided
under a stricter ceiling, and **six works in the world cite both a stock-flow-consistent and a
kinetic-exchange seed.**

**Keywords:** aggregation · Sonnenschein–Mantel–Debreu · biophysical economics · stock-flow consistency · econophysics · composition · citation graph · pre-registration

**JEL classification:** B41, D50, E01, Q57, C63

---

## 1 · Introduction

Three literatures describe wealth and do not cite each other. **Biophysical economics** treats
production as a transformation of energy and materials subject to thermodynamic constraint.
**Stock-flow-consistent macroeconomics** insists that every flow leaves a stock somewhere and that
the accounting must close. **Kinetic-exchange econophysics** treats a wealth distribution as the
stationary state of a stochastic exchange process. Each is a serious research programme with its
own journals, and each is describing a different layer of the same object.

This paper is the claim that they are layers of one stack, and that the object at the bottom of it
composes: **the same atomic unit, a household's, aggregates to a firm's and to a sovereign's
without changing type.** That claim is worth stating carefully, because a nearby and stronger
version of it is false, and the difference between the two is this paper's central technical
content.

### 1.1 · Why now, and it is not because the idea is new

The models this framework declines to use were not errors. They were **force-fits, not form-fits**
— rational responses to constraints that have since expired.

The distinction is worth stating exactly, because the soft version of the concession gives away
more than it needs to. A *benign* simplification drops detail and preserves structure: refine it
and the numbers move. A *structural* one collapses a distinction the theory needs: refine it and
the conclusions move. Capital as a malleable scalar is the second kind, and the Cambridge
controversy was fought over precisely that — Samuelson (1966) conceded that with reswitching
available the marginal-productivity account cannot be recovered from an aggregate capital measure.
The scalar survived anyway, and it survived for a reason that had nothing to do with the argument
being settled.

**The reason was that the scalar was the only object anyone could populate.** There was no
firm-level panel in machine-readable form, no national input-output energy table at usable
granularity, and no standing international series for energy intensity. A theory that requires a
per-entity state vector was, in 1956, not a theory anyone could take data to. Those three
constraints are datable and all three have lapsed: machine-readable structured filings became
mandatory in the United States over a phase-in ending in 2011; energy intensity of GDP is now
published annually as a United Nations Sustainable Development Goal indicator (7.3.1); and
firm-level panels of both are public and free.

Note what is deliberately *not* argued here. The parallel claim about computation — that models of
that era had to be analytically solvable because numerical solution was unavailable — is true and
is left out, because a claim about hardware dates a paper and a claim about what a model can be
populated with does not. The data constraint is the stronger half of the argument and it is the
half with an expiry date one can cite.

This is also the paper's posture toward everything it disagrees with, and §6 states it as a
method rather than leaving it as a habit: the disagreement is never that a predecessor was wrong.
It is that a predecessor was solving a differently-constrained problem, and the constraints moved.

**Contributions.**

1. **A composition result and its exact boundary** (§3, §4). The atomic unit is an extensive
   state, and extensive states compose by addition across scales. **Behaviour does not compose,
   and the theorem that says so is Sonnenschein–Mantel–Debreu.** SMD is therefore not an
   objection to this framework; it is the framework's own statement of where composition stops.
   A paper claiming clean composition across scales while citing SMD as a shield would be
   contradicting itself, and §4 exists to make sure this one does not.
2. **The consequence, which is the corpus's thesis in one sentence** (§4.3): aggregation destroys
   the behavioural information macroeconomics believes it is measuring, and preserves the
   thermodynamic structure nobody is looking at.
3. **A worked instance at the smallest possible scale** (§5): in a market for a single indivisible
   good, the quantity coordinate of the supply-and-demand diagram is not a behavioural aggregate
   at all. It is a state variable — the allocation mismatch — and the two curves' difference is
   invariant to the allocation identically, at every price.
4. **The whitespace, measured rather than asserted** (§6). The claim that these three literatures
   do not meet is normally made by an author reporting that he looked. Here it is a pre-registered
   citation-graph measurement (`REG-013`) with both ends of its scale established in the same run:
   a split-half control that cannot be tuned, and an unrelated-field floor.
5. **A stated method** (§7). The relocation move — *not wrong, differently constrained* — is used
   deliberately and named, rather than deployed four times by accident.

**What this paper does not contain.**

No new code and no new simulation. Papers II and III carry the computational results and their
test suites; this paper cites them as established and adds one measurement of its own, on the
literature rather than on the model. Where a number appears below without a citation to II or III
it is from `REG-013` and is reproducible by the command in §10.

---

## 2 · The atomic unit

### 2.1 · The three propositions, cited not restated

Paper III states the framework's propositions with their domains and defends the coupling once.
They are named here because §3 composes them and §4 bounds them, and re-arguing them would be the
duplication ADR-001's decomposition exists to avoid.

- **P1 · Composition.** A holding's value is a composite of a physical component and a claim
  component, and the two obey different laws.
- **P2 · Decay.** The physical component degrades whether or not the degradation is recorded.
- **P3 · Atomism.** Measured aggregates are folds over units, and no aggregate is more fundamental
  than its constituents.

P3 is the one this paper is about, and it is worth being precise about which P3. It is the weak
form: aggregates are folds. It is **not** the strong form — that some aggregates carry information
no fold contains — which was tried, in this project, and did not survive (§8).

### 2.2 · What kind of object composes

An **extensive** quantity is one whose value for a composite system is the sum of its values for
the parts: mass, energy, a stock of steel, a balance of claims. An **intensive** one is not:
temperature, a price, a rate of return. A **behavioural map** is neither — it is a function from
states to actions, and the question of whether it composes is the question of whether the map of
the whole is the map built from the maps of the parts.

The atomic unit of this framework is an extensive state. It composes by addition, and the
statement that it does so is a definition rather than a discovery. The content of this paper is
not that extensive states add; it is **what stops adding at the same moment**, and what that
implies about which measurements survive aggregation.

---

## 3 · Composition, at three scales

The claim to be checked is not "the framework applies at every scale" — a framework can be applied
anywhere, which is why applicability is not evidence. The claim is that **the same object appears
at each scale and the operator that moves between them is addition**.

**Household.** The unit is a holding: a dwelling, a vehicle, a claim on a pension. It has a
physical component that degrades at some rate and a claim component recorded at some other rate.
Nothing here is metaphorical; a roof has a service life and a mortgage has an amortisation
schedule, and they are different numbers.

**Firm.** A balance sheet is the household's holding, summed and reported. Paper III's result is
that this reporting is a filter: a share φ of each true change passes through at once and the
remainder is released at rate α from an unrecognised gap. The filter is a *per-class* object —
Paper III indexes classes *i* and writes the recursion with a Hadamard product,

> **C**(*t*+1) = **C**(*t*) + **φ** ⊙ Δ**E** + **α** ⊙ **gap**(*t*),

and the elementwise product is not notation. It is the claim that the reporting layer is
**diagonal in class space**, which is exactly the statement that the firm's reporting composes
from its classes' reporting without cross-terms.

**Sovereign.** National accounts are firms summed, and Paper II's parameter space is what happens
when a levy is assessed on that sum. Its central result is a composition result wearing different
clothes: the base of a levy — stock or flow — is the question of *which component of the composed
state the assessing layer can see*, and at zero realisation a confiscatory levy on flow is
statistically indistinguishable from no levy at all.

**Note what this is: three instances of one question, asked at three scales.** At each step the
same two components appear, the same question is asked of them — what does the measuring layer
observe? — and the answer at each scale is a *quantitative* one that the paper for that scale
reports. Paper II's κ,
the share of aggregate wealth actually moved per assessment, is a composition quantity: it is
defined at the sovereign scale and it is a fold over household-scale liabilities. Paper III's φ ⊙ δ
is a composition quantity: it is defined at the firm scale and is *written* as diagonal over asset
classes — a form the next paragraph reports as tested and rejected, which changes what the link
carries and not whether there is one.

**An earlier draft of this section claimed more than three instances of one question, and the
corpus's first end-to-end test took the surplus away.** It said the three scales made *a chain
rather than three analogies*. `END-TO-END-001` leg `E1` asked whether the sovereign and firm scales
stand in the relation the word *chain* asserts — whether Paper II's realisation share ρ and Paper
III's observability share φ are the same object seen twice — and they are not. What Paper III's
filter does not recognise is **deferred**, held in an unrecognised gap and released at rate α;
what Paper II's base does not recognise is **never assessed**. A lag and a loss are different
operators, and Paper II has no parameter that plays α's part. So what joins the scales is the
question and the fact that each scale answers it quantitatively, which is what this section now
claims and no more. The demotion was written into that document's §2 **before** the leg was run,
precisely so that it could not be renegotiated afterwards; `docs/RESULT-END-TO-END-001-E1.md`
records the run and the reasoning.

And **the place where the firm-scale link could break was named, was tested, and the test rejected
it.**
Diagonality is an assumption, not a theorem: if recognition events cluster within firm-quarters
rather than occurring independently across classes, the Hadamard form is wrong and the firm's
reporting does *not* compose from its classes' without cross-terms. Paper III registered that test
(`REG-003`) and ran it, and **independence is rejected in both universes in the same direction —
4.12× and 2.02× the independence expectation, both *p* = 0.0002, in a design that detects an
injected excess of five per cent of events with probability 1.00** (Paper III §5.4; the headline
survives that section's tag-list repair at 4.01× and 2.10×).

**Three things follow, and the middle one is why this paper reports the rejection in the section
that makes the claim rather than only in its limitations.** First, the consequence is *bounded
rather than open*: the Hadamard form is now an approximation whose error is measured, not an
assumption whose status is unknown, and a measured approximation is a stronger object to build on
than an untested premise. Second, **what the rejection costs is the reporting layer's clean
composition, not the state's.** Diagonality is a property of the *filter* — of how recognition in
one class relates to recognition in another — and never of the extensive state, which adds by
§2.2 whatever the recording practice does. The firm-scale link is therefore degraded and
not severed: the firm's *state* still composes from its classes' states, and it is the firm's
*reporting* of that state that carries cross-terms the diagonal form omits. Third, and this is the
part that runs against the paper's convenience, **Paper III's design cannot separate an economic
coupling from the sequencing the standards impose** (ASC 350-20-35-31 and 35-32 order the tests),
so this paper may not read the rejection as evidence that the underlying degradations are coupled.
It inherits a measured departure with an unidentified cause, and §9 says so.

---

## 4 · The tension, resolved explicitly

### 4.1 · The objection, stated at full strength

Here is the objection this paper would deserve if §3 were the whole of it.

*You claim a unit that composes from household to sovereign. But the best-established result about
aggregation in economics says the opposite. Sonnenschein (1972, 1973), Mantel (1974) and Debreu
(1974) proved that aggregate excess demand inherits from individually rational agents only
continuity, homogeneity of degree zero and Walras's Law — not downward slope, not uniqueness, not
stability. Aggregate demand can take essentially arbitrary shape. Worse: your own Paper I cites
SMD approvingly, as evidence that doubting inherited aggregation is inside the mainstream. You
cannot cite the theorem that aggregation destroys structure and then claim structure survives
aggregation.*

That is correct as far as it goes and it is the strongest thing anyone will say about this paper.
It is also answerable in one distinction, and the answer is not a hedge.

### 4.2 · The distinction

**SMD is a theorem about maps, and the atomic unit is a state.**

What SMD constrains is the aggregate *excess demand function* — an object that takes prices and
returns quantities, assembled from individual demand functions. The theorem says that essentially
nothing about the individual functions survives the assembly. It is a statement about the
**behavioural map**.

What P1–P3 assert composes is the **state**: how much physical stock is held, how much claim is
recorded against it, and at what rates each moves. Summing steel is not summing preferences.

The two claims are therefore not in tension; they are complementary halves of one statement, and
the statement is sharper than either half:

> **Aggregation preserves the extensive state and destroys the behavioural map.**

SMD is the second clause, proved, fifty years ago, inside the mainstream. This framework is the
first clause, and the reason it is worth having is entirely the *conjunction*: if aggregation
destroys the map, then a discipline that measures aggregates in order to recover behaviour is
measuring the thing that does not survive, and one that measures aggregates in order to recover
stocks is measuring the thing that does.

### 4.3 · The consequence

**Macroeconomics aggregates in order to do behavioural inference.** Estimate an aggregate
production function, recover a technology; estimate an aggregate consumption function, recover a
propensity; estimate an aggregate demand curve, recover an elasticity. SMD says the object being
estimated need not have inherited any of the structure the inference requires. The response to
SMD in practice has been to restrict preference heterogeneity until the aggregate is
well-behaved — Hildenbrand and Grandmont, and the representative agent as the limiting case — which
is a legitimate research strategy and is also an admission that the structure is imposed rather
than inherited.

Meanwhile the extensive state — energy embodied, stock degraded, claim recorded against it,
and the rate of each — **does** survive the sum, and it is very largely not being measured,
because it is not what an aggregate is usually built for.

That is the thesis of this corpus in one sentence, and it is a *positive* claim about which
measurements are informative, not a complaint about anyone's research programme.

### 4.4 · The limits of the resolution, stated here rather than in §9

Three, and none of them is rhetorical.

1. **A state that composes is not thereby a state anyone can observe.** Composition is a property
   of the object; observability is a property of the measuring layer, and Papers II and III are
   both, in the end, about the measuring layer failing to see something. The framework's own
   results are the reason to be sceptical that the composed state is available.
2. **"Extensive" is doing real work and it excludes things one might want.** A rate is not
   extensive. δ, φ, α and ρ do not compose by addition; they compose, where they compose at all,
   as *weighted* combinations whose weights are themselves state, and Paper III's ladder results
   are what happens when one forgets this and ranks classes by a parameter rather than by a
   product.
3. **Diagonality is assumed at the firm scale, and the assumption is measurably wrong.** §3 names
   this; Paper III registered the test, ran it, and rejected independence across classes within a
   firm-quarter in both universes. The composition claim therefore has a *degraded* link at exactly
   the scale where the accounting is done — degraded rather than severed, because what was rejected
   is a property of the reporting filter and not of the extensive state, and because the departure
   is now a measured quantity rather than an open exposure. What is not available is its cause: the
   design cannot say whether the coupling is economic or an artefact of the order the standards
   impose on the tests.

---

## 5 · The smallest instance: the crossing height is the volume

*This section carries the surviving result of a paper that was written and then not published; §8
records why, at length, because the route matters more than the destination here.*

Take a market for a single indivisible good. *N* agents each hold a reservation price *mᵢ*; *S*
units exist; *H* is the set of current holders and *T* the set of the top-*S* valuers. The
textbook reads two schedules off this population — a demand curve and a supply curve — and finds
the price where they cross.

**The two schedules are not independent equations.** Measured over 25 allocations of the same
population at 399 interior grid points: 25 distinct demand schedules, 25 distinct supply
schedules, and **one** distinct excess-demand schedule, equal to #{*i* : *mᵢ* > *p*} − *S* at
every point. The reason is a partition. At any price that is not itself a reservation price the
*S* holders divide into those valuing above it and those valuing below, so the allocation enters
the two counts with opposite signs and cancels — at every price, not merely at the zero.

So the *price* coordinate of the cross reads the population and nothing else. The **quantity**
coordinate reads something quite different, and this is the part worth carrying into a paper about
composition. At a clearing price strictly inside the interval,

> *D*(*p*\*) = |*T* \ *H*|,  *S*(*p*\*) = |*H* \ *T*|,  and the two are equal.

**The crossing height is the allocation mismatch** — the number of units in the wrong hands — which
is precisely the quantity excess demand cannot deliver. Verified for all 25 allocations.

Read as a composition statement, the diagram is doing two jobs in one picture: the price coordinate
is a fold over the population, and the height is a *coupling* between the population and the
current state. It is not a behavioural aggregate that has smuggled in state information; it is a
state measurement that has been read as behaviour for a century and a half of teaching.

**What this instance is not.** It is not an SMD result and must not be sold as one. Excess demand
here is monotone and single-crossing — zero monotonicity violations across 500 grid points, running
from +249 to −150 with one sign change — because each agent demands at most one unit and there is
no wealth channel from the endowment back into demand. Remove that restriction and income effects
return, and income effects are exactly what SMD requires. **The two results sit at opposite ends of
one axis, which is why they belong in the same paper**: at zero income effects the allocation
cancels identically and the state is all there is; with income effects the behavioural map stops
composing and SMD is what one gets. The test suite asserts the monotonicity deliberately, under the
name `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`, as a standing limit on the
claim rather than a property being celebrated.

---

## 6 · The whitespace, measured

A paper that joins three literatures usually motivates itself by reporting that they do not meet,
and the evidence offered is that the author looked. That is the first thing a referee attacks, and
correctly: an absence found by searching is a property of the search.

So it was measured instead, and pre-registered first (`REG-013`, committed before the instrument
existed). The design's whole content is that a low co-citation rate between two specialties is
**uninformative on its own** — sociology and semiconductor lithography do not cite each other
either. What makes a number here mean something is a scale with both ends fixed in the same run.

**The instrument.** Each literature is defined by seed works named in the registration, and its
*audience* is the set of works citing at least one seed, taken from OpenAlex. For two literatures
the statistic is the overlap coefficient — the share of the smaller audience that also reads the
other. Twenty-five of twenty-five seeds resolved.

**The ceiling** is each literature split in half by seed index and measured against itself. It
cannot be tuned: if the instrument cannot see that half of econophysics is joined to the other
half, it cannot see anything, and the registration voids the run below 0.20. It came back at
**0.477** pooled.

**The floor** is each literature against six highly-cited CRISPR papers — unrelated to economics by
construction. It came back at **exactly zero**: not one work in any of the three economics
audiences also cites a CRISPR seed.

**The three pairs**, positioned on that floor-to-ceiling scale:

| pair | works citing both | audience (smaller) | overlap | position *z* |
|---|---|---|---|---|
| biophysical × stock-flow | **23** | 1 139 | 0.0202 | 0.042 |
| biophysical × kinetic exchange | **15** | 1 383 | 0.0108 | 0.023 |
| stock-flow × kinetic exchange | **6** | 1 139 | 0.0053 | 0.011 |

Against split-half intersections of 134, 155 and 380 *within* the same three literatures. **Six
works in the world cite both a stock-flow-consistent seed and a kinetic-exchange seed.** All three
pairs fall below the registered 0.10 bar; the whitespace is where it was claimed to be.

**One qualification, and it is the first thing a referee will find, so it is here rather than in
§9.** Biophysical economics is on this instrument a *loose federation*: its own split-half overlap
is 0.168, well below stock-flow's 0.520 and kinetic exchange's 0.744, because its seeds are
monographs spanning four decades and three sub-traditions that do not much cite each other.
Scoring the biophysical pairs against the pooled ceiling is therefore generous to them. Under a
stricter per-literature ceiling, biophysical × kinetic exchange and stock-flow × kinetic exchange
remain whitespace, and **biophysical × stock-flow becomes undecided** (*z* = 0.120 against a 0.10
bar). The registered rule is the one that governs — re-choosing a ceiling after seeing which
verdict it yields is not available — but the result is stated as it is: *two pairs are whitespace
under every reading tried, and one is whitespace under the registered rule and undecided under a
stricter one.*

A second qualification runs the same way. The biophysical audience was capped at 4 000 of 7 801 by
descending citation count, so a bridging work in its tail is invisible here, which suppresses both
biophysical overlaps. The floor's cap does the opposite and costs nothing, since a floor of exactly
zero is the strictest value available.

**And what the measurement does not establish, stated in the registration before the numbers
existed:** an unoccupied intersection is not thereby a fertile one. This section establishes that
the three literatures do not read each other. That there is something worth finding where they
meet is what §§3–5 have to earn on their own.

---

## 7 · Relation to existing work, and the method used to state it

Everything in this section is one move, applied deliberately, and naming it is more useful to a
reader than performing it silently four times.

**The move: relocation.** The disagreement is never *you are wrong*. It is *you are a differently
constrained case*. Piketty is not measuring the wrong thing; he is measuring a different layer.
Solow's scalar was not an error; it was the only object anyone could populate. The Austrian account
of the cycle names a different cause and describes the same architecture. SMD is not an opposing
result; it is this framework's own boundary, proved by the mainstream fifty years before the
framework existed.

Relocation is not politeness and it is not a rhetorical trick to be embarrassed about. For a claim
that spans three literatures it is a **structural** requirement: a paper that must be read by
biophysical economists, stock-flow theorists and econophysicists cannot afford to make an enemy in
any of the three, and more to the point, in each case the relocation is *true*. A predecessor
working under a binding constraint that has since lapsed has not made an error. Recording which
constraint, and when it lapsed, is a stronger and more checkable statement than "the received view
is mistaken," and it is falsifiable in a way that the received-view complaint is not.

**Biophysical economics** — Georgescu-Roegen, Daly, Odum, Ayres and Warr, Hall and Klitgaard —
establishes that production is constrained by energy and materials and that the constraint is not
a detail. What it has generally not had is an accounting-shaped object: a per-entity state that a
balance sheet could carry. Paper III's decomposition is that object, and the coupling Λ it defines
has an inverse that is already published as a United Nations indicator, which is the strongest
available evidence that the quantity is not an invention of the framework.

**Stock-flow-consistent macroeconomics** — Godley and Lavoie, and the surveys of Caverzasi and
Godin and of Nikiforos and Zezza — insists that the accounting close, and builds models in which it
does. Its stocks are financial. The claim here is that the closure is incomplete in a specific and
correctable way: a physical stock degrades on a schedule the financial accounting does not record,
so a model whose accounting closes in claims can still be open in the thing the claims are
against. That is a friendly amendment with a testable edge, and Paper III is where the edge is
tested.

**Kinetic-exchange econophysics** — Drăgulescu and Yakovenko, Chakraborti and Chakrabarti,
Bouchaud and Mézard, Chatterjee and Chakrabarti — has the stochastic machinery and the stationary
distributions. What it has mostly not had is a *base*: its exchanges are of an undifferentiated
scalar. Paper II's result is that the base is the decisive coordinate and the rate is not, which is
a statement kinetic exchange can absorb directly, and its mechanism κ is the sort of closed-form
quantity that literature likes.

**And on the aggregation literature specifically.** SMD is treated in §4 at length and is not
re-argued here. The relation is complementarity: SMD is the theorem for the map, this framework is
the claim for the state, and neither implies the other.

---

## 8 · Abandoned approaches

*This section is not a formality and it is not an appendix. The test applied to every entry is:
had this route worked, which sentence in this paper would be different? An abandonment that could
not have cost anything is an advertisement, not a disclosure.*

**"A chain rather than three analogies."** The sentence this paper's §3 carried until the corpus's
first end-to-end test was run against it. Had it survived, §3 would assert a structural
correspondence between the sovereign scale's realisation share and the firm scale's observability
share, and that correspondence — not the three separate results — would have been this paper's
central contribution. `END-TO-END-001` leg `E1` shows the two shares are not the same kind of
object: the unrecognised remainder is deferred in one and discarded in the other, and the firm
scale carries a release rate α for which the sovereign scale has no counterpart. What is left is
weaker, is what §3 now says, and is still worth publishing: one question, asked at three scales,
answered quantitatively at each. The surviving resemblance is not nothing and is not a structure —
and the test that separated those two readings was designed, with its response to every outcome
fixed in advance, before anybody knew which one it would return.

**A fourth paper, on price formation, that was written and is not being published.** The largest
entry, and it cost the most. A complete draft existed — roughly 7,400 words, references verified —
arguing that supply and demand are not independent equations. It is not in this corpus. Had the
route worked, this paper would be the fifth in a series rather than the third, and §5 above would
be a citation rather than a section.

**Its first framing: attacking the diagram.** The original claim was that partitioning agents into
fixed buyers and sellers is mathematically invalid, presented as a critique of general equilibrium.
It is not one. Walrasian excess demand already has that property and Arrow–Debreu never used the
Marshallian cross, so the available referee reply — *the author is attacking the introductory
diagram rather than the theory* — was fatal and unanswerable. **The cost was the most rhetorically
satisfying claim the project had.**

**Its second framing: the strong form of P3.** The replacement was to claim the diagram catches
atomism in the act: excess demand is a fold over units, the two schedules are folds over units
*and* the allocation, so the decomposition manufactures two objects presenting as aggregates while
carrying information no fold contains. Three supporting results were built and all three
arithmetics were correct. The framing died anyway, for three separate reasons, each established by
running it rather than by argument:

1. **The conclusion was inverted.** *D*(*p*\*) = *S*(*p*\*) = |*H* \ *T*| — the crossing height *is*
   the allocation mismatch. The diagram is not concealing the coupling; it is displaying it. What
   survived is §5, which explains what the two curves are *for* rather than indicting them.
2. **The headline number was noise.** The reported effect — an allocation-indexed perturbation
   producing clearing-interval spread 26× the baseline width — has as its denominator the gap
   between two consecutive order statistics, a single random draw with enormous relative variance.
   Repeating at *N* = 400, 1 000, 4 000 and 10 000 gave 26.1×, 8.3×, 113.5× and 47.2×: a 13.6-fold
   non-monotone swing. It is not a statistic.
3. **The load-bearing sentence was false in the formalism the paper cited.** *"H is not a property
   of the population"* fails under the standard unit (*mᵢ*, *hᵢ*), which makes the two schedules
   additive folds in exactly the sense excess demand is. This is Arrow–Debreu, Aumann and
   Hildenbrand, and the same session had already established Hildenbrand (1994) as a source it
   intended to cite.

**And a control that controlled for the wrong thing.** The 26× contrast was measured against a
rank-preserving perturbation. Against a *rank-scrambling* perturbation that never names the
allocation at all, the effect was 0.89 against 0.96 — essentially identical. The comparison had
been between scrambling and preserving, not between allocation-indexed and population-defined,
and the allocation contributed almost nothing.

**A registered test of the generality, which returned no verdict.** With the P3 framing under
pressure, a pre-registration (`REG-001`) was written to test whether the identity did work in a
second setting where the incumbent apparatus could not follow. The instrument was mis-specified in
four ways and the run produced no usable answer in either direction. It is recorded here as an
instrument dead end — which is what it is — and not as a result, because it never became one.

**A superposition framing for agent role.** Proposed to soften the critique: the agent is "in
superposition" between buyer and seller until the price is observed. Rejected on technical grounds
before it reached a draft. Superposition denotes genuine indeterminacy prior to measurement, and
these agents hold a definite reservation price at all times; the role is a sign function. The cost
of using it would have been a reviewer noting that quantum mechanics had been invoked to describe a
piecewise-constant function, in a research area already carrying reputational damage from loose
physics metaphor — and the metaphor undersells a claim that is exactly stateable without it.

**Reporting a partial invariance that was a tie convention.** §5's identity was first measured on a
12-point grid spanning the full range of reservation prices and returned **four** distinct
excess-demand schedules rather than one. That reads as a partial invariance and was very nearly
written up as one. Both grid endpoints coincide with data points, the strict inequalities in the
two counts then disagree about a single agent whose holding status varies by allocation, and two
endpoints × two holding states = four. Had it gone in, the central claim would have been published
one full step weaker than it is true, and the identity would never have been looked for.

**Centring SMD as the defence.** Considered and refused. Making SMD the centrepiece hands a referee
a ten-minute rejection — a multi-good general-equilibrium theorem applied to a single-good partial
model — and worse, makes the paper's centrepiece a fifty-year-old theorem the author did not prove.
§4 uses SMD as a *boundary*, once, which is the only load it can carry here.

---

## 9 · Limitations

1. **The composition claim is about a state, and the state is largely unobserved.** This runs
   directly against the paper's own comfort: §4.2's resolution buys its consistency by narrowing
   the claim to the extensive state, and Papers II and III are both, in substance, demonstrations
   that measuring layers do not see the thing that matters. A composed state nobody can read is a
   weaker asset than the argument's confidence might suggest.
2. **Diagonality at the firm scale is assumed, its test is closed, and it went against the
   assumption.** Recognition events do cluster within firm-quarters — 4.12× and 2.02× the
   independence expectation, both universes, both *p* = 0.0002 (Paper III §5.4) — so the Hadamard
   form in §3 is an approximation and not an identity, and the composition claim's link at the scale
   where accounting happens is degraded. It is degraded rather than broken for a reason this paper's own
   §4.2 supplies and should not be allowed to sound like a rescue: diagonality is a claim about the
   *reporting filter*, and this paper's composition claim is about the *extensive state*, which
   adds regardless of how it is recorded. The honest cost is that **the firm's reported object no
   longer composes from its classes' reported objects without cross-terms**, which is the scale at
   which anyone would actually read it. And the cause is unidentified: the standards sequence the
   tests, so an accounting artefact and an economic coupling are not separated by the design that
   found the departure.
3. **This paper contributes no new computation.** Its claims are joins over results established
   elsewhere, plus one measurement on the literature. A reader who rejects Paper II or Paper III
   should reject the corresponding link here.
4. **§5's instance is the zero-income-effect case, which is the load-bearing restriction.** The
   allocation cancels identically because each agent's demand does not depend on their own
   endowment. That is the special case; the general one is where SMD lives.
5. **The three-literature framing is a choice, not a partition.** Ecological economics, industrial
   ecology, national accounting theory and the aggregation literature proper all have claims on
   this territory. The three named here are the ones whose results the corpus actually uses.
6. **Nothing here is normative.** The corpus characterises what is measurable and what composes.
   It does not say what should be measured, taxed, recorded or done.
7. **The whitespace measurement is about occupancy, not fertility.** `REG-013` can establish that
   an intersection is unoccupied. That it is worth occupying is what the argument has to earn, and
   the measurement cannot help with it.

---

## 10 · Data and code availability

This paper's own contribution is one measurement, on the citation graph rather than on a model.
Everything else it reports is cited from Paper II or Paper III and is regenerated by those papers'
scripts.

- **Repository:** `https://github.com/jasoncbraatz/wealth-tensor` (public)
- **Pre-registration:** `docs/preregistration/REG-013-citation-graph-whitespace.md`, committed in
  `fff7063`, before the instrument existed
- **Instrument:** `scripts/reg013_citation_whitespace.py`
- **Regenerate §6:** `python3 scripts/reg013_citation_whitespace.py`
- **Test suite:** `python3 -m pytest tests/ -q`
- **Papers cited as established results:** Paper II (`src/wealth_tensor/redistribution.py`,
  regenerated by `scripts/wt030_report.py`); Paper III (`src/wealth_tensor/lag.py` and
  `src/wealth_tensor/lambda_sensitivity.py`, regenerated by `scripts/wt027_report.py`)
- **Commit for the results reported here:** **5efe626** — the last commit touching
  `scripts/reg013_citation_whitespace.py`, and therefore the state of the instrument that produced
  every number in §6. The same non-circularity that governs Papers II and III applies: a paper
  cannot cite the commit that adds the paper, so what is pinned is the code, which is what a
  replicator needs and is verifiable today.

Two tests in the suite exist specifically to make overclaiming fail loudly —
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`, which forbids §5's instance
being sold as an SMD result, and `test_a_flat_gini_does_not_mean_a_bounded_one`, which forbids a
saturating statistic being read as convergence. A test suite that constrains the author is a
different object from one that flatters him.

The repository's `docs/` directory is deliberately public and is the project's working notebook,
including the pre-registration whose prediction failed and the result document recording that a
fourth paper died to its own referees. It is part of the record rather than an appendix to it.

---

## References

*Bibliographic details are to be verified against live sources before submission, per
`docs/papers/PREPRINT-CHECKLIST.md` and `docs/REFERENCE-POLICY.md`. Entries marked ✓ were verified
in the sessions that introduced them to Papers II or III.*

**Aggregation**

Debreu, G. (1974). Excess demand functions. *Journal of Mathematical Economics*, 1(1), 15–21.

Grandmont, J.-M. (1992). Transformations of the commodity space, behavioral heterogeneity, and the
aggregation problem. *Journal of Economic Theory*, 57(1), 1–35.

Hildenbrand, W. (1994). *Market Demand: Theory and Empirical Evidence*. Princeton University Press.

Mantel, R. R. (1974). On the characterization of aggregate excess demand. *Journal of Economic
Theory*, 7(3), 348–353.

Mas-Colell, A., Whinston, M. D., & Green, J. R. (1995). *Microeconomic Theory*. Oxford University
Press.

Sonnenschein, H. (1972). Market excess demand functions. *Econometrica*, 40(3), 549–563.

Sonnenschein, H. (1973). Do Walras' identity and continuity characterize the class of community
excess demand functions? *Journal of Economic Theory*, 6(4), 345–354.

**Capital, and the constraints that expired**

Robinson, J. (1953). The production function and the theory of capital. *The Review of Economic
Studies*, 21(2), 81–106.

Samuelson, P. A. (1966). A summing up. *The Quarterly Journal of Economics*, 80(4), 568–583.

Solow, R. M. (1956). A contribution to the theory of economic growth. *The Quarterly Journal of
Economics*, 70(1), 65–94.

Sraffa, P. (1960). *Production of Commodities by Means of Commodities*. Cambridge University Press.

**Biophysical economics**

Ayres, R. U., & Warr, B. (2005). Accounting for growth: the role of physical work. *Structural
Change and Economic Dynamics*, 16(2), 181–209.

Daly, H. E. (1977). *Steady-State Economics*. W. H. Freeman.

Georgescu-Roegen, N. (1971). *The Entropy Law and the Economic Process*. Harvard University Press.

Hall, C. A. S., & Klitgaard, K. A. (2012). *Energy and the Wealth of Nations*. Springer.

Odum, H. T. (1996). *Environmental Accounting: Emergy and Environmental Decision Making*. Wiley.

**Stock-flow consistent macroeconomics**

Caverzasi, E., & Godin, A. (2015). Post-Keynesian stock-flow-consistent modelling: a survey.
*Cambridge Journal of Economics*, 39(1), 157–187.

Godley, W., & Lavoie, M. (2007). *Monetary Economics: An Integrated Approach to Credit, Money,
Income, Production and Wealth*. Palgrave Macmillan.

Nikiforos, M., & Zezza, G. (2017). Stock-flow consistent macroeconomic models: a survey. *Journal
of Economic Surveys*, 31(5), 1204–1239.

**Kinetic exchange**

Bouchaud, J.-P., & Mézard, M. (2000). Wealth condensation in a simple model of economy. *Physica
A*, 282(3), 536–545. ✓

Chakraborti, A., & Chakrabarti, B. K. (2000). Statistical mechanics of money: how saving propensity
affects its distribution. *The European Physical Journal B*, 17(1), 167–170. ✓

Drăgulescu, A., & Yakovenko, V. M. (2000). Statistical mechanics of money. *The European Physical
Journal B*, 17(4), 723–729. ✓

Yakovenko, V. M., & Rosser, J. B. (2009). Colloquium: Statistical mechanics of money, wealth, and
income. *Reviews of Modern Physics*, 81(4), 1703–1725. ✓

**This corpus**

Braatz, J. C. (2026a). The base caps the region, the rate moves you within it: redistribution as a
parameter space. *Working paper, wealth-tensor.* (Paper II.)

Braatz, J. C. (2026b). Timeliness and durability are not separately identified from a reported
series. *Working paper, wealth-tensor.* (Paper III.)
