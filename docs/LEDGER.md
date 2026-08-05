# Findings Ledger

Every serendipitous connection, open problem, dead end and piece of supporting
evidence — whether or not it survives into the manuscript.

**Dead ends are recorded with equal weight.** In a synthesis assembled over eleven
years the expensive failure is not losing a good idea; it is re-deriving a bad one
because nobody wrote down why it was abandoned.

Entry types: `CONNECTION` · `OPEN` · `EVIDENCE` · `RESULT` · `RISK` · `HYGIENE` ·
`METHOD` · `DEAD-END`

---

## WT-001 · CONNECTION · 2026-08-04
**Cournot corner solutions are the marginal pair from the reservation-price section.**

The Cournot test suite failed on its first run: costs `[8,9,10,11,30]` produce a
*negative* analytic output for firm 5. That firm is not loss-making — it is excluded,
because its marginal cost (30) exceeds the price the survivors set (27.6).

That exclusion boundary is exactly the manuscript's "marginal pair": the last agent
holding a unit and the first agent excluded. The Cournot chapter and the axiomatic
price-formation chapter describe the same object from two directions and currently do
not reference each other.

*Why it matters:* first genuine cross-chapter link found. Candidate spine for the
telescope layer. Implemented in `solve_cournot()`; hand-verified.

---

## WT-002 · OPEN · 2026-08-04 · **ADDRESSED IN TEXT** (items 1–3 written; item 4 unbuilt)
**Lambda's second component is dimensionally a price, and that is the paper's weakest wall.**

`eta_work_to_financial` has units `[currency]/[J]`. A free scalar converting a physical
substrate into observed money is the failure mode that sank Odum's emergy programme and
is structurally identical to the transformation problem. Unaddressed, it reads as
"tuned to fit."

Four-part defence, in priority order:
1. Ground it — it is the reciprocal of a published statistic (see WT-003).
2. **Demote it from parameter to dependent variable.** Do not derive price from energy.
   Measure the coupling and argue its *drift and variance* are the phenomenon: C rising
   against flat E is Lambda diverging, i.e. a bubble with a thermodynamic signature.
3. Express headline results as dimensionless (Buckingham pi) groups so the numeraire
   cancels.
4. Publish a sensitivity sweep showing conclusions invariant across orders of magnitude.

Item 4 is the empirical rebuttal and is the reason this repo exists. Not yet built.

---

## WT-003 · EVIDENCE · 2026-08-04
**Lambda^-1 is UN SDG indicator 7.3.1.**

Energy intensity of output is World Bank series `EG.EGY.PRIM.PP.KD` — "Energy intensity
level of primary energy (MJ/$2021 PPP GDP)" — and is formally SDG indicator 7.3.1,
co-tracked by the IEA. Global coverage, long time series.

*Why it matters:* converts "you invented a conversion constant" into "I inverted an
indicator the United Nations reports against." Single most efficient sentence available
for defending WT-002.

---

## WT-004 · RISK · 2026-08-04 · **RESOLVED IN TEXT**
**Georgescu-Roegen is a hostile witness inside our own bibliography.**

The manuscript quotes him: *"the real source of economic value is the subjective
enjoyment of life by individuals."* He is the most-cited authority in the biophysical
section and he explicitly refused the physical-to-monetary reduction that a naive
reading of Lambda proposes. A reviewer finds this immediately and it reads as not
understanding one's own source.

*Resolution:* WT-002 item 2 dissolves it. Measuring the wedge between physical
throughput and financial claims does not claim energy determines value — it measures the
gap Georgescu-Roegen said would exist. **This must be made explicit in the text**, not
left for the reader to reconstruct.

---

## WT-005 · RESULT · 2026-08-04
**Cournot tatonnement is unstable exactly where its own assumption is weakest.**

The linearised undamped best-response map has gain `(n-1)/2`: stable at n=2, marginal at
n=3, non-convergent beyond. Verified numerically across n and damping; output floored at
zero, so it oscillates rather than diverging.

*Why it matters:* the manuscript argues tatonnement rests on an expectation falsified
every period. The instability boundary makes that argument quantitative instead of
rhetorical — and damping, which rescues convergence, is an inertia assumption the
original model does not contain.

---

## WT-006 · METHOD · 2026-08-04
**The whitespace claim should be a citation-graph result, not a search anecdote.**

"I looked and found nothing" is the first thing a reviewer attacks. Instead: compute
co-citation between seed clusters (biophysical/Georgescu-Roegen-Soddy · stock-flow
consistent/Godley-Lavoie · kinetic exchange/Chakraborti). Near-zero inter-cluster
citation is *quantified evidence* of the gap.

Tooling: OpenAlex (CC0 full snapshot on public S3, no key required for bulk),
Semantic Scholar Academic Graph, Unpaywall for locked DOIs. Verify OpenAlex API key
policy at build time — official docs and a third-party report disagree as of 2026-07.

Hardware: `shellac` (Ryzen 9950X / 96GB / RTX 3090) is idle and sized for a local
snapshot with no rate limits.

---

## WT-007 · EVIDENCE · 2026-08-04
**The existing bibliography is already ~97% open access.**

Audit of the ~57 references: arXiv x4, PMC x4, IDEAS/RePEc x3, financialresearch.gov x3,
plus EconStor, NBER, PLOS, Frontiers, PDXScholar, Digital CSIC, Bank of Greece, JASSS and
numerous university-hosted PDFs. One or two paywalled entries total.

*Why it matters:* no institutional subscription is required for this project. Econophysics
and heterodox macro are preprint cultures. The access anxiety was unfounded.

---

## WT-008 · HYGIENE · 2026-08-04 · **FRAGMENTS FIXED** · checkboxes still deferred
**Six duplicated/orphaned sentence fragments in the manuscript.**

Each sits immediately after an italicised formula — the tell of a paste that split text
following a formula run. Includes two fully duplicated paragraphs (Transformation
Efficiency Vector; the closing paragraph of Project 3) and a stray solitary period.

Restore point taken and verified before any edit:
`RESTORE POINT 2026-08-04 — Axiomatic Reconstruction of Wealth (pre-Claude-edit)`
(40,052 chars · 253 paragraphs · 4 tables). All six defects removed 2026-08-04 (716 chars, arithmetic reconciled) and verified absent by independent read-back. Checkbox-list question remains unanswered.

Also deferred: all bulleted lists in the manuscript are *checkbox* lists, including all
57 references. Intent unconfirmed.

---

## WT-009 · HYGIENE · 2026-08-04 · DEFERRED
**A twin document exists and its title lies.**

`2The Axiomatic Reconstruction of` (19KB, 2026-08-03) sits alongside the canonical 29KB
version. Title truncated mid-sentence. Not yet diffed; unknown whether it is an earlier
draft, a partial export, or holds unique content the canonical copy lost.


---

## WT-010 · METHOD · 2026-08-04
**Google Docs API: two formatting traps, both found the hard way.**

1. **Insertion inherits the style of the paragraph you insert into.** Inserting at an
   index that is the *first character of a heading* silently gives every inserted
   paragraph that heading's style. Eight body paragraphs came out as H2. Symptomless in
   the API response — it reports success. Only a read-back reveals it.
2. **Applying `NORMAL_TEXT` wipes character formatting that spans the whole paragraph.**
   A partial bold run survived; a full-width italic run did not. Apply paragraph styles
   *before* character styles, never after.

*Standing rule for this project:* every batch of doc edits is followed by an independent
read-back that checks rendering, not just the API's success reply. The API reporting
"6 operations succeeded" says nothing about whether the result is correct.

---

## WT-011 · HYGIENE · 2026-08-04 · FIXED
**Body paragraph absorbed into a checkbox list.**

"To capture financial capitalism, this exchange framework is extended to the loan
interest model..." was glued to the final item of the Policy Interventions list, so it
rendered as a list item rather than as body prose. Bullet removed, paragraph normalised.

Found by the verification subagent as an incidental observation while checking something
else — an argument for having the verifier look at the whole document rather than only
at the diff.

---

## WT-012 · RISK · 2026-08-04 · **RESOLVED IN TEXT**
**The supply/demand critique as currently written attacks the textbook diagram, not the theory.**

The manuscript argues that partitioning agents into fixed buyers and sellers is
mathematically invalid because any agent buys below and sells above their reservation
price. That observation is correct — but it is not a critique of general equilibrium. It
*is* general equilibrium. Walras's excess demand `z_i(p) = x_i(p) - e_i` has exactly this
property: positive means net buyer, negative means net seller, same agent, resolved by
price. Arrow-Debreu never used the Marshallian cross; the cross is a pedagogical device.

As written, a reviewer replies: "the author is attacking the introductory diagram rather
than the theory," and the section does not recover.

---

## WT-013 · CONNECTION · 2026-08-04 · **WRITTEN INTO MANUSCRIPT + CITED**
**Sonnenschein-Mantel-Debreu already proves the paper's claim, canonically.**

SMD (Sonnenschein 1972-73, Mantel 1974, Debreu 1974): aggregate excess demand inherits
from individually rational agents ONLY continuity, homogeneity of degree zero, and
Walras's Law. It does **not** inherit downward slope, uniqueness of equilibrium, or
stability under tatonnement. Aggregate excess demand can take essentially arbitrary shape.

That is the manuscript's thesis — the intersection is descriptive, not predictive —
established inside the mainstream, by a Nobel laureate among others, fifty years ago.

*Why it matters:* converts the author from a lone critic of Econ 101 into someone
building on a canonical impossibility result. Strongest available rhetorical position.

*Second-order connection:* SMD denies tatonnement stability in general. WT-005 found
Cournot tatonnement unstable for n >= 3 in the specific. The specific instance is a
micro-instance of the general result — the Cournot chapter and the price-formation
chapter link again, through a different door than WT-001.

---

## WT-014 · CONNECTION · 2026-08-04 · **WRITTEN INTO MANUSCRIPT**
**c(m) is a limit order book. Not a metaphor — an identity.**

The distribution of indifference points across a population, with each agent buying below
and selling above their own reservation price, is exactly the structure of a limit order
book: one population, bids below and asks above, and the "intersection" is merely where
the book crosses.

*Why it matters:* gives the c(m) formulation an empirical object with abundant data, and
lands it inside an existing econophysics literature (order-book microstructure: Bouchaud,
Farmer, Lillo) rather than outside all literatures. Candidate empirical test bed.

---

## WT-015 · DEAD-END · 2026-08-04
**Schrodinger / superposition framing for agent role. Rejected.**

Proposed as a way to soften the supply-demand critique for traditionalists. Rejected on
technical grounds: superposition denotes genuine indeterminacy prior to measurement, but
agents here hold a definite reservation price at all times and their role is a
deterministic threshold function of that price against the market price. It is a sign
function, not a superposition.

Cost of using it anyway: a reviewer observes that quantum mechanics was invoked to
describe a piecewise function, in a paper whose entire defensive strategy rests on
dimensional rigour. Econophysics already carries reputational damage from loose physics
metaphor; do not add to it.

The metaphor also *undersells* the claim. "Both curves are expressions of one
distribution, therefore they are not independent equations, therefore solving them
simultaneously is invalid" is a precise mathematical statement. Fog makes it weaker.

---

## WT-016 · DEAD-END · 2026-08-04
**A free coefficient to accommodate behavioural deviation. Rejected — same trap as WT-002.**

Adding a tunable coefficient so the model can absorb behavioural objections makes it less
falsifiable, not more durable. This is precisely the failure mode already rejected for
the work-to-financial coefficient: a quantity that can accommodate any observation
forbids nothing.

*Correct treatment:* behavioural agents are not outside the framework. They are agents
whose indifference point is noisy, reference-dependent, or time-inconsistent — all of
which are **shape properties of c(m)**, and all measurable. Prospect theory, already
cited in the manuscript, is a statement about how reservation prices shift with a
reference point. Absorb behaviour into the distribution, never into a multiplier.

---

## WT-017 · METHOD · 2026-08-04 · **BUILT** (`excess_demand.py`, 9 tests)
**Do not soften the blow. Nest it.**

The persuasive device in economics is a reduction result: show the new framework collapses
*exactly* to the standard one under explicitly stated conditions. "Under conditions A and
B, the c(m) formulation reduces to the Marshallian cross" respects the tradition by
containing it rather than contradicting it, and demonstrates the author understands what
is being replaced.

This is buildable as executable code and is the natural next artifact for this repo.


---

## WT-018 · RESULT · 2026-08-04
**The curves are not independent: demonstrated, not argued.**

`excess_demand.py`. Population of reservation prices drawn from c(m), S indivisible units,
an allocation recording who currently holds one.

Across 25 randomly drawn allocations of the *same* c(m) and the *same* stock:

- distinct market-clearing intervals: **1**
- distinct demand schedules: **25**

The clearing interval is exactly the manuscript's marginal pair — the S-th and (S+1)-th
highest reservation prices — and excess demand steps +1 → 0 → −1 across it. The schedules
move; the crossing does not. Two schedules that both shift under a perturbation which
leaves the equilibrium unchanged cannot be independent equations. That is the argument,
and it is now a passing test rather than a paragraph.

---

## WT-019 · RESULT · 2026-08-04
**Reduction to the Marshallian cross holds exactly.**

For any *fixed* allocation, the intersection of the supply and demand schedules lands
inside the structural clearing interval. The textbook construction is therefore a correct
instantaneous description; its failure is confined to comparative statics, because the two
schedules cannot be perturbed independently.

This is the nesting result of WT-017. The tradition is contained rather than contradicted
— which is the only form of "softening the blow" that survives review, because it is a
theorem rather than a courtesy.

---

## WT-020 · RISK · 2026-08-04 · **GUARDED BY TEST**
**Non-independence and SMD arbitrary-shape are different claims. Do not conflate them.**

The single-good unit-demand c(m) construction produces a *monotone* excess demand function
with a single crossing. It is well behaved. SMD pathology requires at least two goods and
income effects, and this model does not exhibit it.

Selling the c(m) construction as a demonstration of SMD would be a genuine error and an
easy one to make, since the two arguments appear adjacent in the manuscript.
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` asserts the monotonicity
deliberately, as a standing limit on the claim rather than as a property being celebrated.

---

## WT-021 · RESULT · 2026-08-04
**Behaviour as a shape transform yields a falsifiable prediction that matches the record.**

`with_endowment_effect(λ)` raises the reservation prices of current holders. Trade volume
falls monotonically: 93 → 88 → 82 → 74 → 62 → 49 units for λ = 1.0 … 2.0.

Reduced trading volume under the endowment effect is the documented experimental finding
(Kahneman, Knetsch and Thaler 1990). The model reproduces it as a *consequence* of a stated
transform rather than through a coefficient tuned to produce it — which is the whole
argument of WT-016 made concrete.

---

## WT-022 · CONNECTION · 2026-08-05 · **MAJOR — reframes the whole Piketty chapter**
**Piketty is not wrong. He is measuring the abstraction layer.**

Author's counterfactual exercise: adopt "Piketty is 100% correct, no exceptions", re-read the
data, methods and conclusions, cross-check against EDGAR filings and St Louis Fed series.

Result: the disagreement is not about correctness. It is about **layer**. Piketty's datasets
and rigour are not in question; his measurements are taken on virtual wealth — the financial
abstraction — not on the atomic units beneath it.

*Why this is the single most valuable move available to the paper:* it converts the entire
Piketty section from a refutation into a **scope statement**. r > g may hold exactly as
described at the abstraction layer while being silent about the atomic layer. The paper stops
being a hit-piece and becomes complementary — which is both more honest and far more likely
to survive review. A reviewer who is a Piketty admirer becomes a potential ally rather than a
guaranteed rejection.

---

## WT-023 · CONNECTION · 2026-08-05
**Virtual wealth is a transfer function, not merely an abstraction.**

The author's mechanism: virtual wealth is an abstraction of real wealth, and abstraction
*delays information*. Technical debt is off-balance-sheet entropy — the asset degrades, the
financials show steady dividends, and the information arrives only when the deferral can no
longer be sustained.

Stated properly this is a **signal-processing claim**: virtual wealth is a low-pass filter on
real wealth. That is enormously more useful than a metaphor, because filters have measurable
properties:

- **phase lag** between physical/operational condition and financial indicators
- **variance suppression** — the financial series is smoother than the underlying
- **industry-dependent time constants** — a warehouse retailer re-provisions on a decade;
  a SaaS firm faces zero-days continuously
- **accumulated unmodelled error released as a step discontinuity** — which is what a crisis
  *is* under this reading

Each of these is falsifiable, which is exactly what the paper needs.

*Third instance of the author's signature move.* 1993: predict the next byte with a learned
model so the checksum is unnecessary. 2015: economics has thermodynamic structure. 2026:
the checksum (real wealth) arrives too late and the predictor (virtual wealth) drifts. Same
structural isomorphism, three times, thirty years apart.

---

## WT-024 · CONNECTION · 2026-08-05 · **unifies WT-002**
**Λ's drift is the accumulated deferred information.**

WT-002 demoted the work-to-financial coefficient to a dependent variable and asserted that
its *drift and variance* are the phenomenon. WT-023 supplies the mechanism: Λ diverges
precisely when the abstraction layer is deferring information about atomic-layer decay.

**Λ's divergence is the integral of undelivered entropy.** The wedge Georgescu-Roegen
identified (WT-004) and the lag the author observed in 10-K filings are the same quantity
measured two ways. Two chapters and three prior ledger entries collapse into one mechanism.

---

## WT-025 · RISK · 2026-08-05
**Three attack surfaces on the lag thesis, in order of severity.**

1. **Forward-looking markets.** Efficient-markets reply: prices should already discount
   deferred maintenance. The thesis requires that this information is *systematically* not
   incorporated. This must be argued with evidence, not asserted. (Armour exists — see
   WT-026 — but it must be cited explicitly.)
2. **"The dual tensor is the *only* solution."** Overclaim. Reviewers hunt the word "only".
   Replace with necessary-conditions language: state what any adequate solution must do, then
   show the construction satisfies it.
3. **Quine-Duhem is being used for the wrong problem.** Heterogeneous entropy rates across
   industries is an *identification/heterogeneity* problem with standard remedies (fixed
   effects, hierarchical priors), not a Quine-Duhem problem. A genuine Q-D issue does exist —
   a failed test cannot distinguish a false theory from a bad entropy proxy — but it must be
   stated precisely or it reads as borrowed vocabulary.

Also: Japan 1990s is N=1. Motivating illustration, not evidence. Needs companion cases, and
more importantly a deliberate search for *disconfirming* ones.

---

## WT-026 · METHOD · 2026-08-05
**The lag is selective, not uniform — and that asymmetry is the actual mechanism.**

A pure-delay model is falsified by any case where financial signals *lead* physical change,
and such cases plainly exist (markets price an announced technology transition before the
capital is built).

The defensible and more interesting claim: the abstraction layer **leads on announced or
observable change and lags on deferred or unobservable degradation.** The asymmetry is the
mechanism, and it makes a sharper prediction than uniform delay: lag magnitude should scale
with the *unobservability* of the underlying degradation.

This is testable and it is where the accounting literature becomes armour rather than
obstacle, since the categories that are hardest to observe are precisely those the accounting
standards decline to capitalise.
