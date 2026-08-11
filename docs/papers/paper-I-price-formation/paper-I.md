# Supply and demand are not independent equations: price formation from a single distribution of reservation prices

**Jason C. Braatz**
*Independent researcher*
jasoncbraatz@gmail.com

**Draft — not yet submitted.** Version 0.1, 2026-08-10.

---

> ## ⚠ SUPERSEDED — read `REVIEW-002-internal-referee.md` before this file
>
> **This draft was rejected by its own internal referee on the day it was written, and the
> rejection was substantially correct.** It is retained as written, rather than revised or deleted,
> because `docs/` is a working lab notebook (ADR-001 §Consequences) and a paper that was wrong in
> instructive ways teaches more than its own corrected successor.
>
> **What is wrong with it, in short:**
>
> 1. **Contribution 2 is Böhm-Bawerk (1889).** The term *marginal pairs* is his, for this exact
>    object; his horse-market numbers reproduce this paper's formula to the shilling. The modern
>    formalisation is Shapley & Shubik (1971), whose §4 is titled *"The Horse Market of
>    Böhm-Bawerk"*. Neither is cited below.
> 2. **Contribution 5 is Theocharis (1960) and Fisher (1961)**, and the bound *d* < 4/(*n*+1) is
>    eq. (2.26) of a 2010 Springer monograph, presented there as routine. Not new.
> 3. **The central negative claim is false in this paper's own model.** *"The schedules cannot be
>    perturbed independently"* does not follow from the invariance, and the referee shifted one
>    schedule while holding the other pointwise fixed, using this repository's unmodified code.
> 4. **§3.4 breaks §3.1**, because its behavioural transform makes *c*(*m*) a function of the
>    allocation. At λ = 1.3 the invariance gives 25 distinct excess-demand schedules, not 1.
> 5. **§3.3 is circular**: `marshallian_cross` is computed *from* excess demand, so the reduction
>    result substitutes §3.1 into itself. And "exactly recovered" is a coincidence of two
>    resolutions — at *N* = 4000 it is 0/25.
> 6. **§4.2's gain expression was wrong** (the Jacobian has a second eigenvalue, 1 − *d*/2). The
>    stability condition happens to survive it. Fixed in the code and the tests; **left standing
>    below** so the review has something to point at.
>
> **What may survive**, and it is stated at the strength the audit supports and no further: no
> source checked states the *invariance* of *z*(*p*) to which agents hold the units — but the
> auditor's own warning stands, that this is one short step from Coase, Gorman, Böhm-Bawerk and
> Shapley–Shubik, and is plausibly folklore in a literature not yet searched. **Searching
> Gul–Stacchetti, Demange–Gale–Sotomayor and the law-and-economics treatment of Coase in
> indivisible-goods markets is a precondition of any successor draft, not an optional extra.**

---

## Abstract

With indivisible units and no income effects, the supply and demand schedules are not two equations.
They are two readings of one distribution of reservation prices, and the reading is a bookkeeping
choice rather than an economic fact. This paper demonstrates that as an identity rather than an
inference. Across 25 allocations of the same 400 reservation prices and the same stock of 150 units
there are **25 distinct demand schedules, 25 distinct supply schedules, and exactly one
excess-demand schedule**, equal to *#{i : mᵢ > p} − S* at every price that is not itself a
reservation price: the allocation cancels from the difference algebraically, because the holders
partition at any price into those above it and those below it. Three consequences follow. The
market-clearing interval is the **marginal pair**, the *S*-th and (*S*+1)-th highest reservation
prices. The Marshallian cross is **exactly recovered** for any fixed allocation, making it a valid
snapshot and an invalid comparative static — the schedules cannot be perturbed independently because
their difference does not move. And behaviour enters as a stated transform of the distribution rather
than a free coefficient, reproducing the endowment effect's documented volume decline (93 → 49 units)
as a consequence. The same exclusion boundary appears in Cournot competition, where the damping that
stabilises tâtonnement is shown to vanish like 4/*n*, so the repair for Cournot's instability needs
more information than his own assumption grants. Every number regenerates from one command against a
public repository.

**Keywords:** reservation prices · excess demand · Marshallian cross · comparative statics ·
Cournot competition · tâtonnement stability · Sonnenschein–Mantel–Debreu · endowment effect

**JEL classification:** D40, D41, D51, L13, C62

---

## 1 · Introduction

The supply-and-demand cross is the first diagram in economics and the last one most readers ever
see. Two schedules, drawn as independent objects, crossing at a price. The construction is old
enough that its status is rarely examined: it is treated as a *model*, in which the two curves are
primitives that can be shifted one at a time, and comparative statics is the exercise of doing so.

This paper's claim is that in the simplest exchange setting the two schedules are not primitives at
all, and that the demonstration is an identity rather than an argument. Given a population of
reservation prices and a stock of indivisible units, an *allocation* records who currently holds
one. Demand at price *p* counts the non-holders who value a unit above *p*; supply counts the
holders who value theirs below it. Change the allocation and both schedules change. Their
difference does not change at all.

That is not a near-invariance or a statistical regularity. The *S* holders partition at any price
into those above it and those below it, so the allocation enters the two counts with opposite signs
and cancels. The excess-demand function is *#{i : mᵢ > p} − S*: a function of the reservation-price
distribution and the stock, and of nothing else. **The split of that single function into a supply
half and a demand half carries no economic content.** The textbook draws a bookkeeping convention
as though it were data, and then perturbs it.

**This is an instance of a proposition stated elsewhere in this programme, and it is cited rather
than restated.** P3 — *measured aggregates are folds over units; no aggregate is more fundamental
than its constituents* — is stated with its domain in the companion paper on the dual tensor
[III, §2.2]. Supply and demand are exactly such folds: two different ways of summing over the same
units, presented as two objects. The general proposition and this instance were developed together
and it would be circular for each to support the other, so no support is claimed in either
direction. What is claimed is that the price system is where P3 is cheapest to check, because here
the fold can be written down and the cancellation performed in one line.

**Contributions.** This paper is short and its claims are specific.

1. An **identity**: with indivisible units and no income effects, aggregate excess demand is
   invariant to the allocation *at every price*, not merely at its zero, and equals
   *#{i : mᵢ > p} − S* (§3.1). This is stronger than the usual observation that the schedules
   co-move, and it is what licenses the rest.
2. The identification of the market-clearing interval with the **marginal pair**, the *S*-th and
   (*S*+1)-th highest reservation prices, together with the demonstration that excess demand steps
   +1 → 0 → −1 across it for every allocation (§3.2).
3. A **reduction result**: for any fixed allocation the Marshallian construction recovers the
   structural clearing interval exactly (§3.3). The cross is therefore a correct *snapshot* and an
   incorrect *comparative static*, and the failure is located precisely — not in the diagram's
   accuracy but in the independence its perturbation assumes.
4. A demonstration that **behaviour enters as a shape transform of the distribution**, not as a
   fitted coefficient: raising holders' reservation prices reproduces the endowment effect's
   documented volume decline monotonically, 93 → 49 units (§3.4).
5. The **same exclusion boundary in Cournot competition** (§4): a firm whose marginal cost exceeds
   the price the survivors set is excluded rather than loss-making, which is the marginal pair
   arriving from the quantity side. And a sharpening of the classical instability result — the
   damping that rescues tâtonnement is not a constant but **vanishes like 4/*n***, so the repair
   requires each firm to know how many rivals it has (§4.2).
6. A **stated limit on the claim**: this construction produces a monotone, single-crossing excess
   demand and therefore does *not* exhibit Sonnenschein–Mantel–Debreu pathology (§3.5). The limit
   is enforced by a test rather than by a promise.

**A boundary, stated once.** Everything here concerns a model class. The setting is one good, unit
demand, indivisible units and no income effects; §5 records what that costs and §6 records which
of the results survive its relaxation and which do not. No claim is made about any market.

---

## 2 · The construction

### 2.1 · Reservation prices, and the two readings

*N* agents. Agent *i* holds a reservation price *mᵢ*, drawn from a distribution *c*(*m*). There are
*S* indivisible units of a single good, at most one per agent, and an **allocation** is the subset
of agents currently holding one. At price *p*:

> a holder **sells** if *mᵢ* < *p* — a non-holder **buys** if *mᵢ* > *p*

Nothing here partitions the population into buyers and sellers. An agent's side of the market is
not a property of the agent; it is a property of the pair (reservation price, current holding)
evaluated at *p*. This is the standard content of excess demand as Walras (1874) formulated it,
where *zᵢ*(*p*) = *xᵢ*(*p*) − *eᵢ* is positive for a net buyer and negative for a net seller — the
same agent, resolved by price — and it is worth saying plainly that the observation is *not* a
critique of general equilibrium. It **is** general equilibrium. The object under examination is the
cross of Marshall (1890), a pedagogical device that the general-equilibrium tradition does not
itself use: Arrow and Debreu (1954) prove existence without it. §5 records what happened when that
distinction was not maintained.

### 2.2 · What is measured

**Demand** *D*(*p*) = #{non-holders with *mᵢ* > *p*}. **Supply** *S*(*p*) = #{holders with
*mᵢ* < *p*}. **Excess demand** *z*(*p*) = *D*(*p*) − *S*(*p*). The **marginal pair** is the *S*-th
and (*S*+1)-th highest reservation prices. **Volume** is the number of units changing hands on the
way to the efficient allocation at the clearing price.

Throughout: *N* = 400, reservation prices lognormal(μ = 3.0, σ = 0.6) under NumPy's `default_rng(7)`,
*S* = 150, and 25 allocations drawn under `default_rng(0…24)`. Every figure in §3 is produced by one
command against the committed modules; §7 gives it.

---

## 3 · Results

### 3.1 · The allocation cancels from the difference, identically

Take the same *c*(*m*), the same *S*, and 25 different allocations. Measured at 399 interior grid
points, ties excluded:

| object | distinct values across 25 allocations |
|---|---|
| demand schedule *D*(*p*) | **25** |
| supply schedule *S*(*p*) | **25** |
| **excess demand *z*(*p*) = *D*(*p*) − *S*(*p*)** | **1** |

Every allocation gives a different demand curve. Every allocation gives a different supply curve.
All 25 give the same difference, and that difference equals *#{i : mᵢ > p} − S* at every grid point.

The reason is a partition and it takes one line. At any price *p* that is not itself a reservation
price, the *S* holders divide into those with *mᵢ* > *p* and those with *mᵢ* < *p*. So

> *S*(*p*) = #{holders, *mᵢ* < *p*} = *S* − #{holders, *mᵢ* > *p*}

and therefore

> *z*(*p*) = #{non-holders, *mᵢ* > *p*} − *S* + #{holders, *mᵢ* > *p*} = **#{*mᵢ* > *p*} − *S*.**

The allocation appears in both counts with opposite signs and leaves.

**Why the identity is worth more than the co-movement.** The usual way to state this result is that
the schedules move while the crossing does not, from which a reader infers that two things which
both shift under a perturbation leaving the equilibrium fixed cannot be independent equations. The
inference is sound and unnecessary. The identity says something strictly stronger and says it
without inference: **the decomposition of *z* into a supply half and a demand half is a bookkeeping
choice.** It records which side of the ledger each agent is written on, and the economy is invariant
to that choice at every price, not only where the two halves happen to be equal.

An economist may reasonably respond that this is obvious once written down. It is — that is the
point of writing it down. What is not obvious is that a construction with this property is
routinely perturbed one curve at a time.

### 3.2 · The clearing interval is the marginal pair

The invariant object has a zero, and the zero is structural. For the population above:

| quantity | value |
|---|---|
| (*S*+1)-th highest reservation price (first excluded) | 21.461883 |
| *S*-th highest reservation price (last included) | 21.498548 |
| interval width | 0.036665 |
| distinct clearing intervals across 25 allocations | **1** |

Any price strictly inside the interval clears the market, for every allocation. Excess demand steps
**+1 → 0 → −1** across it, and the triple (*z* just below, *z* at the midpoint, *z* just above) takes
exactly one value — (1, 0, −1) — across all 25 allocations.

The interval is the manuscript's **marginal pair**: the last agent who can hold a unit and the first
who cannot. It is a property of *c*(*m*) and *S*. It has no dependence on who currently holds what,
which is the same statement as §3.1 evaluated at one price.

### 3.3 · The textbook construction is recovered exactly

The reduction result. For each of the 25 allocations, read *D*(*p*) and *S*(*p*) off the schedules
and find where they cross, exactly as the diagram instructs:

| quantity | value |
|---|---|
| allocations tested | 25 |
| crosses landing inside the structural interval | **25 / 25** |
| distinct cross values across allocations | 1 |
| cross value | 21.469835 |
| structural interval | [21.461883, 21.498548] |

**The Marshallian cross is not wrong.** It is a correct instantaneous description, and this paper
contains it rather than contradicting it — which is the only form of concession that survives
review, because it is a theorem rather than a courtesy.

What the cross cannot do is comparative statics that move the allocation. The diagram's method is to
shift one schedule and read off the new intersection, and that method presumes the schedules can be
shifted separately. They cannot: §3.1 says their difference is fixed, so any perturbation of the
allocation moves both in lockstep and moves the crossing not at all. **The failure is not in the
picture. It is in the operation performed on the picture** — and locating it there is what makes
this a result rather than a complaint.

### 3.4 · Behaviour is a shape transform, not a coefficient

The endowment effect — named by Thaler (1980) — is the finding that holders value what they hold
more highly than non-holders value acquiring it. In this construction that is not an additional
mechanism. It is a statement about where reservation prices sit, and reservation prices are the
model's only primitive. Multiply holders' *mᵢ* by a factor λ ≥ 1 and re-read the same two schedules:

| λ | volume | change |
|---|---|---|
| 1.00 | 93 | — |
| 1.05 | 88 | −5 |
| 1.15 | 82 | −6 |
| 1.30 | 74 | −8 |
| 1.60 | 62 | −12 |
| 2.00 | 49 | −13 |

Volume falls monotonically, by 47.3 % of baseline across the range. **Reduced trading volume is the
documented experimental finding**, and it is the right one to match: Kahneman, Knetsch and Thaler
(1990) report that observed volume in mug-exchange experiments is persistently below the Coase
prediction, and that markets in induced-value tokens run by the same subjects hit the predicted
volume — which is what rules out transaction costs as the explanation. The undertrading, not the
willingness-to-accept/willingness-to-pay gap alone, is the result reproduced here, and here it is a
**consequence of a stated transform** rather than a coefficient chosen to produce it. The
distinction is the whole of the
methodological claim: a transform of *c*(*m*) is measurable and therefore falsifiable, and it makes
a prediction the modeller does not control. A free parameter fitted to the same data forbids
nothing.

Note also what the transform does *not* do. It does not move the clearing interval away from the
marginal pair; it moves the marginal pair, because it moves the distribution. The identity of §3.1
is untouched — this is a different *c*(*m*), not a different reading of the same one.

### 3.5 · What this is not: the Sonnenschein–Mantel–Debreu boundary

Sonnenschein (1972, 1973), Mantel (1974) and Debreu (1974) established that aggregate excess demand
inherits from individually rational agents only continuity, homogeneity of degree zero and Walras's
Law — not downward slope, not uniqueness, not stability under tâtonnement. Aggregate excess demand
can take essentially arbitrary shape. Two conditions of the construction are worth stating rather
than eliding, because they are where the result's scope actually lies: the agents' preferences are
*not* weakened — they remain continuous, convex and monotone, which is the entire force of the
theorem — and the number of households is taken to be at least the number of commodities, Debreu's
construction using *n* households for *n* goods. Within those conditions it is the strongest
available statement that the aggregate schedules are not well-behaved primitives, it is fifty years
old, and it was established inside the mainstream.

**It is not what this paper demonstrates, and the two must not be conflated.** Excess demand here is
monotone and single-crossing: 0 monotonicity violations across 500 grid points, running from +249 to
−150 with one sign change. It is perfectly well behaved.

The reason is worth stating precisely, because the loose version of it is wrong. It is tempting to
say that SMD "requires at least two goods" and that this model has one. That is not the operative
distinction — a single traded good priced against money is already a two-commodity partial
equilibrium, so the count of goods is not what does the work. **What does the work is unit demand
together with the absence of income effects.** With each agent demanding at most one unit and no
wealth channel from the endowment back into demand, aggregate demand is a non-increasing step
function of price by construction, and there is nothing for the SMD construction to get purchase on.
This is the same restriction that §6 identifies as load-bearing for §3.1's identity, and it is the
restriction known to tame the aggregate more generally. Mas-Colell, Whinston and Green (1995, §10.C)
note that the quasi-linear partial-equilibrium price is uniquely defined and warn in the same breath
that uniqueness "need not hold in more general settings in which wealth effects are present". The
chain is theirs: absent wealth effects the aggregate excess demand is that of a single representative
consumer, which satisfies the weak axiom (*ibid.*, §17.F) — and the weak axiom delivers both
uniqueness of the normalised equilibrium and convergence of tâtonnement (*ibid.*, Propositions
17.F.2 and 17.H.1). **The two results are therefore not rivals but opposite ends of one axis**, and
§7 states the relation. Note that this is *not* the gross-substitutes route to the same conclusion,
which is a logically independent condition: the same source records that gross substitutes can fail
in quasi-linear one-consumer economies and that neither property implies the other.

Selling this construction as a demonstration of SMD would be a genuine error and an easy one, since
the two arguments are adjacent and point the same way. The monotonicity is therefore asserted in the
test suite deliberately — `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` — as a
standing limit on the claim rather than as a property being celebrated. **The relationship between
the two results is complementarity, not support**, and §6 states it precisely.

---

## 4 · The same boundary from the quantity side

ADR-001 allocates the Cournot material to this paper for a reason that is a result rather than a
convenience: **the Cournot corner solution is the marginal pair, arrived at from the other
direction.** The two chapters of the original manuscript described one object and did not cite each
other.

### 4.1 · The exclusion boundary is an equilibrium object

Linear inverse demand *p* = 100 − *Q*, five firms with marginal costs [8, 9, 10, 11, 30]. The
closed-form interior solution returns a **negative** output for the fifth firm, and the correct
reading of that is not that the firm loses money:

| firm | MC | *q* | profit | share |
|---|---|---|---|---|
| 1 | 8 | 19.6 | 384.16 | 0.2707 |
| 2 | 9 | 18.6 | 345.96 | 0.2569 |
| 3 | 10 | 17.6 | 309.76 | 0.2431 |
| 4 | 11 | 16.6 | 275.56 | 0.2293 |
| 5 | 30 | **0** | 0 | 0 |

with *Q* = 72.4 and *p* = **27.6**. The fifth firm is **excluded**, because its marginal cost exceeds
the price the survivors set, and 27.6 < 30 confirms the exclusion is self-consistent. The
implementation refuses the interior closed form on this input rather than returning the negative
quantity, and says why.

That boundary — the last participant inside and the first outside, determined by the price the
market reaches rather than by any participant's own circumstances — is the marginal pair of §3.2.
In the exchange setting it is the *S*-th and (*S*+1)-th reservation prices; here it is the highest
marginal cost below *p* and the lowest above it. **Same object, two directions**, and this is the
join that makes these two modules one paper.

### 4.2 · Tâtonnement fails where its own expectation is weakest — and the repair needs what the model denies

Cournot's adjustment process has each firm best-respond to its rivals' current output. Its
linearised map has gain (*n* − 1)/2, so undamped simultaneous adjustment is stable at *n* = 2,
marginal at *n* = 3, and non-convergent beyond. Measured:

| *n* | gain (*n*−1)/2 | undamped, 5000 iterations |
|---|---|---|
| 2 | 0.5 | converged in 47 |
| 3 | 1.0 | did not converge |
| 4 | 1.5 | did not converge |
| 6 | 2.5 | did not converge |
| 10 | 4.5 | did not converge |
| 20 | 9.5 | did not converge |

Output is floored at zero, so the failure is bounded oscillation rather than divergence. The process
rests on an expectation falsified every period out of equilibrium: each firm assumes its rivals hold
output constant, and each period they all move. Bertrand (1883), reviewing Cournot four decades
later, objected to the choice of strategic variable rather than to the adjustment — firms set prices,
not quantities, and under price competition the equilibrium collapses to marginal cost. That
objection is orthogonal to the one here and is not answered by it: the point below is that even
granting Cournot his quantity-setting firms, his own adjustment process does not reach his own
equilibrium without an assumption he did not make.

The standard repair is damping — firms adjust part of the way, *q* ← *q* + *d*(BR(*q*) − *q*) — and
the standard gloss is that damping restores convergence at the cost of an inertia assumption the
original model does not contain. That is true and it undersells the point. The damped map has
linearised gain |1 − *d*(*n*+1)/2|, so it is stable **iff *d* < 4/(*n*+1)**:

| *n* | 4/(*n*+1) | largest *d* converging | smallest *d* failing |
|---|---|---|---|
| 2 | 1.3333 | 1.32 | 1.34 |
| 3 | 1.0000 | 0.98 | 1.00 |
| 4 | 0.8000 | 0.78 | 0.80 |
| 6 | 0.5714 | 0.56 | 0.58 |
| 10 | 0.3636 | 0.36 | 0.38 |
| 20 | 0.1905 | 0.18 | 0.20 |

measured on a 0.02 grid, bracketing the prediction at every *n* tested.

**The threshold is not a constant. It vanishes like 4/*n*.** So the damping that rescues Cournot's
own adjustment process is not a single inertia parameter chosen once — it is a quantity each firm
must condition on the number of rivals it has, slowing itself in proportion as the market gets more
competitive. **Rescuing the dynamic requires every firm to know *n* and act on it, which is more
information than the static expectation the dynamic is built on grants them.** The repair needs
precisely what the model denies.

This is a claim about the structure of the adjustment process and it does not expire. It is also
sharper than the usual objection: not *damping is an extra assumption*, but *which* assumption and
*how much* of it, in a direction that worsens without bound as *n* grows.

### 4.3 · Identities checked rather than assumed

The markup condition of Lerner (1934), (*p* − MCᵢ)/*p* = *sᵢ*/|ε|, holds to machine precision at
equilibrium (maximum absolute residual 1.1 × 10⁻¹⁶ across the cost vectors tested) — a verification
of the markup equation rather than an assumption baked into the solver. The Cournot limit theorem is exhibited
rather than asserted: with symmetric MC = 10, *p* − MC falls 30.0 → 8.18 → 0.891 → 0.0899 for
*n* = 2, 10, 100, 1000. HHI equals 1/*n* exactly for symmetric firms. Three independent solution
routes — closed form, simultaneous first-order conditions, and damped tâtonnement — agree to
10⁻⁶, so each checks the others.

---

## 5 · Abandoned approaches

*This section is not a formality and it is not an appendix. A result reported without the routes
that failed is a result the reader cannot calibrate — they are shown the one path that worked and
left to assume it was the only one considered. The test applied to every entry below is: had this
route worked, which sentence in this paper would be different?*

**Attacking the diagram rather than the theory.** The original framing argued that partitioning
agents into fixed buyers and sellers is mathematically invalid, and presented that as a critique of
general equilibrium. It is not. Walrasian excess demand already has exactly this property, and
Arrow–Debreu never used the Marshallian cross. The framing was abandoned because a referee's reply
was available and fatal — *the author is attacking the introductory diagram rather than the theory*
— and the section could not have recovered from it. **The cost was the paper's most rhetorically
satisfying claim.** What replaced it is the reduction result of §3.3, which concedes that the cross
is correct as a snapshot and locates the failure in the *operation* instead. That is a smaller claim
and a true one, and §3.3 exists only because the larger one was given up.

**A superposition framing for agent role.** Proposed as a way to soften the critique for
traditionalists: the agent is "in superposition" between buyer and seller until the price is
observed. Rejected on technical grounds. Superposition denotes genuine indeterminacy prior to
measurement, and these agents hold a definite reservation price at all times; their role is a
deterministic threshold function of that price against *p*. It is a sign function, not a
superposition. The cost of using it anyway would have been a reviewer observing that quantum
mechanics was invoked to describe a piecewise-constant function, in a paper whose defensive strategy
rests on dimensional rigour — and econophysics carries enough reputational damage from loose physics
metaphor already. **The metaphor also undersells the claim**, which is the part worth keeping: "both
schedules are readings of one distribution, therefore they are not independent equations, therefore
perturbing them separately is invalid" is a precise mathematical statement, and fog makes it weaker.
Had this route been taken, §1 and §2.1 would be written in a vocabulary the result does not need.

**Reporting the invariance as partial.** §3.1's first measurement used a 12-point grid spanning the
full range of reservation prices and returned **4** distinct excess-demand schedules rather than 1.
That reads as a partial invariance, it is the kind of finding that gets written up as one, and it
was very nearly written up as one. Both grid endpoints coincide with data points — the minimum and
maximum reservation prices — and the strict inequalities in the demand and supply counts then
disagree about a single agent, whose holding status varies by allocation. Two endpoints × two
holding states = 4. **It was a tie convention, not an economic effect.** Had it gone in, the paper's
central claim would have been stated one full step weaker than it is true, and the identity in §3.1
would never have been looked for. The grid now excludes any point within 10⁻⁹ of a reservation
price, in the regeneration script and in the test, with the reason recorded beside it.

---

## 6 · Limitations

1. **The identity is a property of the no-income-effect case, and that is the load-bearing
   restriction.** In general, *z*(*p*) = Σᵢ *dᵢ*(*p*) − *E*, and the allocation enters only through
   the aggregate endowment *E* precisely when each agent's demand *dᵢ* does not depend on their own
   endowment. Income effects break that, and income effects are exactly what SMD requires to
   generate pathology. So the two results sit at opposite ends of one axis: **at zero income effects
   the allocation cancels exactly and the schedules are one object; with income effects the
   aggregate inherits almost nothing and the schedules are not well-behaved objects at all.** The
   conclusion that they are not independent primitives survives at both ends, but *for different
   reasons*, and **only the first end is proved here.** The middle of that axis is not
   characterised by this paper and the general statement above is algebra, not one of this paper's
   demonstrated results. That the no-income-effect end is the tame one is not this paper's
   discovery — the absence of wealth effects is the standard route to a unique and
   tâtonnement-stable normalised equilibrium (§3.5) — which makes the identity in §3.1 a sharp
   instance of a known regularity rather than an isolated curiosity, and correspondingly less
   impressive than it would be if the general case behaved this way. It does not. One further
   caveat belongs here rather than in a footnote: the no-wealth-effect property itself holds only
   while numéraire consumption is interior, so even the tame end has an edge.
2. **Indivisible units, one per agent.** Multi-unit and divisible demand are not modelled. The
   partition argument in §3.1 is written for the unit-demand case and its generalisation is stated
   in Limitation 1 rather than demonstrated.
3. **One good.** There are no relative prices, no substitution and no budget constraint binding
   across markets. The construction is an exchange economy in the narrowest available sense.
4. **No production, no entry, no dynamics in §3.** The exchange results are static; the only
   dynamics in the paper are Cournot's adjustment process in §4.2, which belongs to a different
   model.
5. **The endowment-effect transform is exogenous and uncalibrated.** λ is swept, not estimated. The
   monotone volume decline is a qualitative match to a documented experimental finding; no claim is
   made that any particular λ describes any particular population, and the magnitudes are not
   compared to experimental magnitudes.
6. **Finite *N*, one distributional family, one seed.** *N* = 400 and *c*(*m*) is lognormal. The
   identity of §3.1 is exact and distribution-free by the partition argument, so it does not depend
   on these; the reported figures do.
7. **§4.2's threshold is a linearised result verified on a grid.** The bracket is 0.02 wide and the
   test asserts a bracket rather than an equality. The scaling is the claim; the third decimal is
   not defended.

---

## 7 · Relation to existing work

**The non-independence of the schedules is not itself new**, and the paper is stronger for saying
so. Walras's excess-demand formulation already resolves an agent's side of the market by price
rather than by type, and the Sonnenschein–Mantel–Debreu theorems already deny that the aggregate
inherits the properties the cross depends on. The contribution here is narrower and more elementary:
the *identity* in §3.1 — the algebraic cancellation of the allocation from the difference in the
unit-demand case — makes the point without invoking either, and it locates the failure of the
textbook construction in one specific operation rather than in the construction as a whole.

**The capital controversies are the nearest precedent for the shape of the argument**, and the
relation is a debt rather than an application. Sraffa (1926) on returns under competitive
conditions, and then Sraffa (1960), where prices and distribution are derived from the technical
conditions of production without an aggregate capital measure entering as a primitive; Robinson
(1953), objecting that a scalar "capital" presupposes the price system it is used to derive; and
Samuelson (1966, p. 568), conceding that reswitching and capital-reversing cannot be excluded once
capital goods are heterogeneous, so that the neoclassical parables relating a falling interest rate
to greater roundaboutness "cannot be universally valid" — the formal withdrawal of the non-switching
theorem being Levhari and Samuelson (1966). **That concession is narrower than it is often reported
to be and is stated here at its actual width:** it concerns aggregate-capital parables, not
general-equilibrium or marginal-productivity theory, and it is a claim about what cannot be excluded
rather than about what is empirically common. All the same, the move is one move: an aggregate
treated as a primitive turns out to be a fold over units whose validity requires conditions on the
units. This paper's object is smaller — a schedule rather than a capital stock — and its conditions
are cheaper to state, but the structure of the objection is theirs.

**The reservation-price distribution is a limit order book**, and this is the empirical opening the
construction offers rather than a metaphor: one population, bids below and asks above, and the
"intersection" is where the book crosses. That places the formulation inside an existing
microstructure literature with abundant data — Bouchaud, Farmer, Lillo and the surrounding work on
order-book dynamics and market impact — rather than outside all literatures. **No empirical claim is
made here.** The connection is stated because it names where a test would come from, and because a
construction with an empirical object available is a different proposition from one without.

**On accounting consistency**, the cancellation in §3.1 is a stock–flow statement: the allocation is
a stock, trade is a flow, and the identity holds because every unit held is a unit not demanded. The
stock–flow consistent tradition, in the form developed by Godley and Lavoie, makes the general
discipline explicit — that every flow originates somewhere and terminates somewhere, and that models
which do not enforce this can produce results that are artefacts of the omission.

**On the Cournot side**, the instability of simultaneous best-response adjustment is classical and
the (*n*−1)/2 gain is standard. The extension in §4.2 — that the stabilising damping shrinks like
4/*n*, so the informational requirement of the repair grows with the size of the field — is stated
here as a small result rather than a survey of the stability literature, which is large and which
this paper does not attempt to cover.

---

## 8 · Data and code availability

All results in this paper are produced by open code, and no proprietary or restricted data is used,
because no empirical data is used at all — every number is generated by computation over a specified
distribution.

- **Repository:** `https://github.com/jasoncbraatz/wealth-tensor` (public)
- **Modules:** `src/wealth_tensor/excess_demand.py`, `src/wealth_tensor/cournot.py`
- **Regenerate every number in §3 and §4:** `python3 scripts/wt018_report.py`
- **Test suite:** `python3 -m pytest tests/ -q` — 109 tests across the repository, of which 22 hold
  this paper's two modules in place (`tests/test_excess_demand.py`, `tests/test_cournot.py`)
- **Commit for the results reported here:** **6492157** — the last commit touching `src/`, and
  therefore the state of the code that produced every number. *A head-of-repository SHA will
  additionally be pinned when this paper is posted.*

Pinning the last commit that touched `src/` rather than a bare placeholder is deliberate: it is
non-circular (a paper cannot cite the commit that adds the paper), it is verifiable today, and it
names the object a replicator actually needs — the state of the code, not the state of the prose.

Two of the tests exist specifically to make overclaiming fail loudly rather than quietly.
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` pins the limit stated in §3.5, so
that a future draft cannot promote this construction into an SMD result.
`test_excess_demand_is_identically_invariant_to_the_allocation` asserts all three counts of §3.1
(25 / 25 / 1) *and* the closed form, so that the central claim cannot be quietly weakened back to
the crossing-only version it was stated as before. A test suite that constrains the author is a
different object from one that flatters him.

The repository's `docs/` directory is deliberately public and contains the project's working
notebook, including the ledger entries in which this paper's central claim was found to be one step
weaker than the code supported, and in which §5's tie-convention near-miss is recorded in full.

---

## References

***The citation rule this list follows.*** *The edition cited is the edition **consulted** — the copy
in the author's possession — not the earliest printing a catalogue happens to list. Where the
original's date does argumentative work, because the entry is a translation or because a claim about
priority rests on it, the entry is **dual-dated** `original/consulted`. A reprint that changes no
pagination is a printing, not an edition, and is not dual-dated.*

*Verified 2026-08-10 (session wealthTensor-06).* **✓** — checked against a publisher page, a
library-catalogue record, a Crossref record or the issuing body's own documentation, not recalled.
**✓✎** — additionally checked against **the author's own copy**, by reading that copy's title page
and colophon.

**Price formation and general equilibrium**

Arrow, K. J., & Debreu, G. (1954). Existence of an equilibrium for a competitive economy.
*Econometrica*, 22(3), 265–290. ✓

Debreu, G. (1974). Excess demand functions. *Journal of Mathematical Economics*, 1(1), 15–21. ✓

Mantel, R. R. (1974). On the characterization of aggregate excess demand. *Journal of Economic
Theory*, 7(3), 348–353. ✓

Marshall, A. (1890). *Principles of Economics* (Vol. I). Macmillan. ✓ *(The 1890 imprint is Volume I;
no second volume was published. This paper cites the construction, not a page, so no edition among
the eight is selected — a citation to specific text would have to choose between the first edition
of 1890 and the eighth of 1920.)*

Mas-Colell, A., Whinston, M. D., & Green, J. R. (1995). *Microeconomic Theory*. Oxford University
Press. ✓ *(Cited in §3.5 for three linked results: the quasi-linear uniqueness statement and its
wealth-effects warning at §10.C; the weak axiom for excess demand and Proposition 17.F.2; and
Proposition 17.H.1 on tâtonnement convergence. Also the source of the caution recorded in §3.5 that
gross substitutes and quasi-linearity are logically independent conditions.)*

Sonnenschein, H. (1972). Market excess demand functions. *Econometrica*, 40(3), 549–563. ✓

Sonnenschein, H. (1973). Do Walras' identity and continuity characterize the class of community
excess demand functions? *Journal of Economic Theory*, 6(4), 345–354. ✓

Walras, L. (1874–1877). *Éléments d'économie politique pure*. L. Corbaz & Cie. ✓ *(The 1874 imprint
is the first instalment only; the work was completed in 1877. Full imprint: Lausanne, L. Corbaz &
Cie; Paris, Guillaumin; Bâle, H. Georg.)*

**Oligopoly and adjustment**

Bertrand, J. (1883). Review of *Théorie mathématique de la richesse sociale* and *Recherches sur les
principes mathématiques de la théorie des richesses*. *Journal des Savants*, 67 (septembre), 499–508.
✓ *(An earlier draft of this list gave volume 68. No source consulted supports 68; the New Palgrave
entry on Bertrand competition gives 67, and the Walras bibliography that reproduces the review gives
the month without a volume.)*

Cournot, A. A. (1838/1960). *Researches into the Mathematical Principles of the Theory of Wealth*
(N. T. Bacon, Trans.). Augustus M. Kelley. ✓✎ *(The copy consulted is the Augustus M. Kelley*
Reprints of Economic Classics *printing, New York, 1960, LCCN 64-7663, whose title page carries the
Bacon translation together with Irving Fisher's essay* Cournot and Mathematical Economics *and his
bibliography of mathematical economics. Fisher's foreword, dated Yale University, August 1927,
describes the volume as "an exact reprint of the edition of 1897 except for the addition of the
Mathematical 'Notes'" reprinted from his 1898* Quarterly Journal of Economics *article. The French
original is* Recherches sur les principes mathématiques de la théorie des richesses*, L. Hachette,
Paris, 1838. The entry is dual-dated because §4 attributes the oligopoly model and its adjustment
process to Cournot's priority, so the 1838 date does argumentative work.)*

Lerner, A. P. (1934). The concept of monopoly and the measurement of monopoly power. *The Review of
Economic Studies*, 1(3), 157–175. ✓

**The aggregation objection**

Levhari, D., & Samuelson, P. A. (1966). The nonswitching theorem is false. *The Quarterly Journal of
Economics*, 80(4), 518–519. ✓

Robinson, J. (1953). The production function and the theory of capital. *The Review of Economic
Studies*, 21(2), 81–106. ✓

Samuelson, P. A. (1966). A summing up. *The Quarterly Journal of Economics*, 80(4), 568–583. ✓

Sraffa, P. (1926). The laws of returns under competitive conditions. *The Economic Journal*, 36(144),
535–550. ✓

Sraffa, P. (1960). *Production of Commodities by Means of Commodities: Prelude to a Critique of
Economic Theory*. Cambridge University Press. ✓

**Behaviour, and the order book**

Bouchaud, J.-P., Farmer, J. D., & Lillo, F. (2009). How markets slowly digest changes in supply and
demand. In T. Hens & K. R. Schenk-Hoppé (Eds.), *Handbook of Financial Markets: Dynamics and
Evolution* (pp. 57–160). North-Holland. ✓ *(The publisher's own table of contents lists a variant
chapter title; the Crossref record matches the title given here.)*

Kahneman, D., Knetsch, J. L., & Thaler, R. H. (1990). Experimental tests of the endowment effect and
the Coase theorem. *Journal of Political Economy*, 98(6), 1325–1348. ✓ *(This is the correct primary
citation for the* volume *result specifically — undertrading against the Coase prediction, with the
induced-value control that rules out transaction costs — as distinct from the willingness-to-accept /
willingness-to-pay gap, which is older. §3.4 reproduces the volume result and cites accordingly.)*

Thaler, R. (1980). Toward a positive theory of consumer choice. *Journal of Economic Behavior &
Organization*, 1(1), 39–60. ✓

**Accounting consistency**

Godley, W., & Lavoie, M. (2007). *Monetary Economics: An Integrated Approach to Credit, Money,
Income, Production and Wealth*. Palgrave Macmillan. ✓

**This programme**

[II] Braatz, J. C. (2026). *The base caps the region, the rate moves you within it: redistribution as
a parameter space*. Manuscript, `docs/papers/paper-II-redistribution/paper-II.md` in the repository
named in §8. *Not yet posted; this citation will carry a public identifier at submission.*

[III] Braatz, J. C. (2026). *A crisis is deferred information arriving at once: the dual tensor of
wealth, and a pre-registered prediction it lost*. Manuscript,
`docs/papers/paper-III-dual-tensor/paper-III.md` in the repository named in §8. *Not yet posted; this
citation will carry a public identifier at submission.* §1 cites P3 from its §2.2.

---

*How this list was checked, recorded because a reference section that silently improves teaches a
reader nothing.*

**Two passes ran, in this order, and the second found what the first structurally could not.**

1. **Bibliographic** — *does this work exist with these details?* Every entry checked against a
   publisher page, a library catalogue, a Crossref record or the issuing body's documentation. It
   found **one error**, Bertrand's volume number, and two entries stated more narrowly than the
   record supports (Marshall's 1890 imprint is Volume I; Walras's is the first instalment of a work
   completed in 1877). Otherwise clean.
2. **Cited-in-text** — *does this entry do any work in the body?* It found **two failure modes, and
   most of the list had one of them.** Several entries were listed and never mentioned in any form:
   Bertrand, Sraffa (1960), Thaler (1980), and a Kahneman–Knetsch–Thaler survey from 1991. More
   were invoked *eponymously* — "Walrasian excess demand", "the Marshallian cross", "the Lerner
   condition", "the documented experimental finding" — prose that names a person or a construction
   and cites nothing, so the body reads as attributed while the list reads as used, and neither
   document reveals the gap on its own. **That is the failure a bibliographic pass structurally
   cannot see**, because every entry it checks is real.

   Disposition: Bertrand, Sraffa (1960) and Thaler were given the work they had been listed for, and
   the eponymous invocations now carry years. The 1991 survey was **removed** — the 1990 paper does
   the same job better, and an entry retained for completeness is an entry doing no work.

*A third pass — provenance, against the author's own library — was run and is partially complete.
It located Cournot and corrected that entry from the 1838 French original to the Kelley reprint of
the Bacon translation actually consulted. It did **not** locate Marshall, Sraffa, Robinson,
Samuelson, Mas-Colell et al., or the Kahneman–Knetsch–Thaler and Thaler papers. **That is a null
result from an indexed subset, not an absence** — journal articles are not expected in a book
archive, and the book collection is mid-reorganisation across several devices. No citation has been
altered or removed on the strength of it. The outstanding question, which needs the author and not
a session, is which edition of Marshall, Sraffa (1960) and Mas-Colell et al. he consulted.*
