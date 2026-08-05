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

## WT-002 · OPEN · 2026-08-04 · **CLOSED 2026-08-05** — items 1–3 written, item 4 built (WT-036)
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

**Reframed by WT-038 (2026-08-05): Λ is an ENTAILMENT of the composition axiom, not a posit.**
If wealth is a compound of two components in different units, a coupling between them must
exist; it was obliged, not introduced. That answers this entry at the root rather than the
perimeter, and supersedes the defensive ordering of the four-part defence below.

Item 4 is the empirical rebuttal and is the reason this repo exists. **Built 2026-08-05** —
`lambda_sensitivity.py`, spread exactly zero across twelve orders of magnitude. See WT-036.

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

## WT-022 · CONNECTION · 2026-08-05 · **WRITTEN INTO MANUSCRIPT**
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

## WT-023 · CONNECTION · 2026-08-05 · **BUILT** (`lag.py`, 10 tests)
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

## WT-024 · CONNECTION · 2026-08-05 · **unifies WT-002** · **WRITTEN INTO MANUSCRIPT**
**Λ's drift is the accumulated deferred information.**

WT-002 demoted the work-to-financial coefficient to a dependent variable and asserted that
its *drift and variance* are the phenomenon. WT-023 supplies the mechanism: Λ diverges
precisely when the abstraction layer is deferring information about atomic-layer decay.

**Λ's divergence is the integral of undelivered entropy.** The wedge Georgescu-Roegen
identified (WT-004) and the lag the author observed in 10-K filings are the same quantity
measured two ways. Two chapters and three prior ledger entries collapse into one mechanism.

---

## WT-025 · RISK · 2026-08-05 · **ALL THREE ADDRESSED IN TEXT**
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

## WT-026 · METHOD · 2026-08-05 · **BUILT + WRITTEN**
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


---

## WT-027 · RESULT · 2026-08-05
**Lag and crisis severity scale with unobservability. Verified.**

`lag.py`. Real layer decays at an entropy rate net of maintenance. A share phi of each
change is observable and passes to the reported layer immediately; the remainder accrues
unrecognised and is released when the gap exceeds a threshold.

Filter isolated (crisis mechanism disabled), phi from 1.0 down to 0.0:

| phi | recognition lag | smoothing | deferred information |
|----|----|----|----|
| 1.0 | 0 | 1.000 | 0.0 |
| 0.8 | 2 | 0.919 | 398.5 |
| 0.5 | 12 | 0.824 | 996.2 |
| 0.2 | 20 | 0.771 | 1593.9 |
| 0.0 | 25 | 0.762 | 1992.4 |

phi = 1 is a perfect window: zero lag, zero deferred information, coupling identically 1.
That is what answers the forward-looking-markets objection — disclosed change passes
through untouched, so the objection holds exactly where the model predicts no lag and has
nothing to act on where degradation is undisclosed.

Crisis frequency over 400 periods by entropy rate: retail (d=0.01) **0**, industrial
(d=0.05) **16**, SaaS (d=0.20) **100**. The Costco-versus-zero-day contrast is a position
in parameter space, not a rhetorical flourish.

---

## WT-028 · RESULT · 2026-08-05 · **corrects a stated prediction**
**Volatility is not suppressed. It is relocated.**

The "over-smoothing" prediction was wrong as stated, and the probe caught it: measured
across the whole path, reported changes are *more* volatile than real ones, because the
corrections dominate.

The true behaviour is better than the prediction. Between corrections the reported layer
is far smoother than the underlying (0.93 → 0.80 → 0.52 → 0.35 as phi falls), while the
share of total reported movement occurring inside corrections rises 0.00 → 0.69 → 0.96 →
**0.99**. At zero observability essentially every reported movement is a correction.

The signature is therefore not a quiet system but one that is quiet for long intervals and
then abruptly is not — which is a far more recognisable description of the historical
record than uniform smoothing, and a sharper empirical target.

*Method note:* the original metric measured the wrong object. Two metrics now exist —
`variance_suppression` on inter-crisis periods, `variance_concentration` on the corrections
— because one number could not carry both claims.

---

## WT-029 · RISK · 2026-08-05 · **RESOLVED IN TEXT**
**The redistribution section read as prescription. It is now positive, not normative.**

The zakat/waqf/sadaqah passage entered the manuscript circa 2014 as an *observation* about
what those systems appeared structurally designed to do. As written it read as advocacy for
government intervention — which is the fastest available route to having a technical paper
dismissed as ideology, and the first thing an Austrian-school reader would fire at.

The defect was never the content. It was the missing positive/normative boundary. The
finding is a property of a model class: within kinetic exchange models, continuous
redistribution *of any kind* prevents terminal condensation. The historical systems are
**instances demonstrating the property is implementable**, not recommendations.

Text now states the boundary explicitly and maintains it.

---

## WT-030 · CONNECTION · 2026-08-05 · **BUILT — REFINED BY WT-033**
**Classify redistribution by structural parameters, not institutional origin — and the base is decisive.**

What determines whether a mechanism bounds inequality in a *multiplicative* wealth process
is not where it came from but its parameters: base, rate, periodicity, threshold.

**The base does the work.** A levy on *flow* (income received in a period) does not directly
oppose the multiplicative term, because that term operates on the *stock*. A levy on stock
does. Zakat is analytically interesting on exactly this ground — assessed on qualifying
wealth held above a threshold across a full year, not on income received — which places it
in a different region of the parameter space from an income tax **regardless of rate**.

*Why it matters:* converts "which system do you favour" into "which regions of the parameter
space bound the Gini below unity", which is a question the models answer and nobody can call
advocacy. Also dissolves the data problem — no causal field evidence on any historical
institution is required, because the claim is a property of a model class.

*Superseded by WT-033:* built. The base is decisive, but through
**realisation**, not rate — see WT-033 for the corrected claim and the numbers.

*Original next-artifact note:* `redistribution.py` — sweep (base ∈ {stock, flow}) × rate × periodicity ×
threshold over the multiplicative-additive process, and map which regions bound the Gini.

---

## WT-031 · CONNECTION · 2026-08-05 · **the counter-factual produced an ally**
**Austrian business cycle theory has the same architecture as the two-layer lag model.**

The author's adversarial exercise — "what would the Austrian school shoot at?" — surfaced
convergence rather than conflict, in two places:

1. **Hayek's knowledge problem.** "The Use of Knowledge in Society" holds that prices
   transmit dispersed information and that the characteristic failure is *informational*,
   not moral. WT-023's reporting layer as an information-deferring filter is a formalisation
   of precisely that concern.
2. **Malinvestment (Mises 1940).** Misallocated capital accumulates *unrecognised* through
   the boom and is revealed and liquidated in the bust. Structurally identical to WT-027:
   unrecognised accumulation followed by discontinuous correction.

**Different causes, same architecture.** Austrians assign credit expansion; this framework
assigns undisclosed physical degradation. Stated as a structural analogy, not an identity —
overclaiming here would be easy and fatal.

*Why it matters most:* a single mechanism that reproduces a phenomenon which mutually
hostile traditions each describe in their own vocabulary is worth far more than alignment
with any one of them. It makes the framework non-tribal, which is rare and defensible.

---

## WT-032 · METHOD · 2026-08-05
**Never infer document indices by arithmetic. Measure them.**

While placing the WT-029 edit, indices were computed by adding a known insertion length to a
cached structure snapshot. The arithmetic was wrong by 6,944 characters — the cached snapshot
had already been taken *after* that insertion, so the offset double-counted. Applying it
would have written four paragraphs into the middle of the bibliography.

Caught only by re-measuring before editing rather than trusting the derived number.

*Rule:* re-run `inspect_doc_structure` after every mutation and read indices from it. A
cached snapshot is valid only for style-only operations, which do not change length. The
cost of measuring is one call; the cost of being wrong is a corrupted manuscript.

---

## WT-033 · RESULT · 2026-08-05 · **refines WT-030** · `redistribution.py`, 18 tests
**The base is decisive — but the mechanism is realisation, not rate, and the sharp claim needed rewriting.**

WT-030 asserted that a levy on stock opposes the multiplicative term and a levy on flow does
not, *regardless of rate*. Built and swept, that is **half right, and the surviving half is
better than the original**.

Multiplicative-additive process, N=800, mu=0.05, sigma=0.20, wage=0.05, T=1200. The levy is a
pure transfer — everything collected is redistributed per capita in the same period, verified
to machine precision, so nothing below can be a growth artefact.

| levy | Gini | kappa | top 10% | bounded |
|---|---|---|---|---|
| none | 0.994 | — | 1.000 | **no** |
| stock, rate 0.025 | 0.443 | 0.0250 | 0.336 | yes |
| stock, rate 0.100 | 0.222 | 0.1000 | 0.193 | yes |
| flow, rate 0.025 | 0.812 | 0.0025 | 0.734 | yes |
| flow, rate 0.100 | 0.596 | 0.0102 | 0.481 | yes |
| flow, rate **1.000** | 0.125 | 0.1026 | 0.138 | yes |
| flow, rate 1.000, **nothing realised** | 0.994 | 0.0006 | 1.000 | **no** |

**What reproduced.** At a matched rate the two bases are roughly an order of magnitude apart,
in the predicted direction, at every rate tested. The mechanism is `kappa`, the share of
aggregate wealth actually moved per assessment: for a stock base `kappa = rate` exactly; for a
flow base `kappa = rate * E[eta+]`, the *gross positive* growth rate, because a levy cannot
rebate a loss. Closed form `E[eta+] = mu*Phi(mu/sigma) + sigma*phi(mu/sigma) = 0.1073` —
asserted in the suite, matched to 5%. So a **confiscatory** flow levy has the compressive
budget of a **10% stock levy**, and the base sets a ceiling the rate cannot cross.

**What did not.** "Regardless of rate" is false as stated. At full mark-to-market realisation
a flow levy *does* bound the Gini; it is merely weak. Rate at 1.00 reaches Gini 0.125, which a
stock levy reaches at rate 0.25. The reachable frontiers are `stock 0.000 < flow 0.125`, so
the bases occupy nested regions rather than disjoint ones.

**The surviving claim, which is sharper.** The decisive quantity is **realisation** — the share
of a period's gain the base can see. The multiplicative term operates on the *stock*; a flow
base reaches it only through whatever share is recognised as income. At `rho = 0` — the pure
rentier whose gains accrue but are never realised — a **100% flow levy is statistically
indistinguishable from no levy at all** (Gini 0.994 vs 0.994, top decile 1.000 in both).
*That* is the true "regardless of rate" result, and it is a statement about what a base can
observe rather than about how hard it squeezes. Frontier by realisation:
`rho=1.00 → 0.125 · rho=0.25 → 0.395 · rho=0.00 → 0.994`.

**Manuscript action:** replace "regardless of rate" with the realisation statement. The
weaker claim is the more defensible one and it names a real, documented feature of every tax
system rather than a modelling convenience. It also connects: unrealised appreciation is
precisely wealth whose growth the reporting layer has not been asked to recognise, which is
WT-023's deferred information wearing a different hat.

**Compatibility with WT-029.** No contradiction. WT-029's claim — redistribution *of any kind*
prevents terminal condensation — survives: every levy with a visible base is `bounded`, down
to a 1% flow levy (Gini 0.891, but not condensing). WT-033 is about *where* it lands, not
whether it lands. Both belong in the text; conflating them would overclaim WT-029.

---

## WT-034 · METHOD · 2026-08-05
**The Gini saturates, so "the Gini stopped rising" cannot detect condensation. Measure the top share.**

`is_bounded` was first written as a drift test: the Gini has settled if its mean over the last
quarter of the path exceeds the previous quarter's by less than a tolerance. It scored the
**unopposed** process — the one the entire module exists to contrast against — as *bounded*.

The Gini of N agents is capped at `(N-1)/N`. A fully condensed economy therefore also stops
rising: not because it reached a stationary distribution but because it ran out of headroom.
At N=800 the unopposed process reads Gini 0.977 and *flat*, while its top decile holds 0.988
of everything. The drift test was measuring the ceiling, not the phenomenon.

Fix: `is_bounded` requires both a settled Gini **and** a top decile below 0.90. The separation
is then unambiguous — bounded runs sit at 0.19–0.50, condensed runs at 0.99–1.00, and the
top-share statistic is horizon-stable where the Gini is not.

*Rule, and it generalises past this module:* **a summary statistic with a hard ceiling cannot
distinguish "converged" from "saturated."** Before using one as a convergence criterion, ask
what its maximum is and whether the failure mode you are trying to detect drives it there.
Same family as WT-028, where the volatility metric measured the wrong object and the probe
caught it; twice now the first-draft metric has been the defect.

Kept as a standing guard, not a comment: `test_a_flat_gini_does_not_mean_a_bounded_one`
asserts the trap explicitly, so any future simplification of `is_bounded` fails loudly
instead of quietly re-scoring condensation as success.

---

## WT-035 · RESULT · 2026-08-05
**Periodicity and threshold are trim, not structure — and a low threshold is nearly free.**

Both remaining parameters of WT-030 turn out to modulate the *effective rate* rather than
open or close a region, which is what leaves base and rate as the two structural coordinates.

**Periodicity.** Holding the average rate constant at 0.02 per period, assessing every P
periods at rate `0.02*P` moves the stationary Gini from 0.486 (P=1) to 0.456 (P=20) — a
lumpier assessment is very slightly *stronger*, because it catches dispersion that has had
time to accumulate. An annual assessment is therefore not a watered-down continuous one, which
is the relevant observation for any historical system assessed on a yearly cycle.

**Threshold.** Monotone and smooth, no cliff: Gini 0.443 at zero exemption rising to 0.770 at
20x the mean of the base. The useful part is the near end. A threshold at 0.25x the mean costs
**nothing measurable** in compression (0.444 vs 0.443) while reducing `kappa` by a quarter —
exempting small holders removes a quarter of the assessed volume and none of the effect,
because the compression is done by the transfers at the top of the distribution.

*Why it matters:* a threshold that exempts the poor is not a concession that weakens the
mechanism, it is close to free. Any historical levy with a low exemption floor sits in the
barely-weakened region, and that is a measured coordinate rather than an interpretation.

---

## WT-036 · RESULT · 2026-08-05 · **CLOSES WT-002 item 4** · `lambda_sensitivity.py`, 10 tests
**The numeraire cancels. Twelve orders of magnitude, spread exactly zero.**

WT-002 named the work-to-financial coefficient the paper's weakest wall: a free scalar with
units `[currency]/[J]` is the failure mode that sank Odum's emergy programme. Three legs of
the four-part defence were written in S1. This is the fourth and it is now built.

The two-layer system of `lag.py` is dressed in units — real layer in joules at scale `E0`,
reported layer in currency, coupling `eta` between them — so that invariance is *measured*
rather than asserted from the algebra, which is exactly what a sceptical reviewer declines to
take on trust.

**Negative half.** Across `eta` from 1e-6 to 1e+6, the spread of every dimensionless
diagnostic is **exactly 0.0**: recognition lag (22), variance suppression (0.6097), variance
concentration (0.9199), crisis count (16), relative crisis magnitude (0.20138), and the mean,
minimum and terminal coupling ratios. Not "within tolerance" — bit-identical, because the
coupling never enters the recursion, only the dressing applied afterwards.

**Positive half, and the half that makes it a test rather than a tautology.** Dimensional
outputs scale with a log-log slope of **1.000000000000**. Deferred information runs
6.32e6 → 6.32e18 currency units across the sweep. It would be trivially easy to build a module
where nothing depends on `eta` because `eta` is never used; here it is used, the currency
figures move with it exactly as a unit conversion must, and no conclusion moves at all.
Mutation-tested both ways: leaking `eta` into the dynamics fails four tests, and removing the
scaling fails two.

**Scaling collapse.** Two systems differing in energy scale (1 J against 6.02e23 J) and in
coupling (1e-6 against 42) lie on a single dimensionless curve to within 1e-12. This is the
form the result should take in the manuscript — a collapse is a figure a reviewer checks in
one glance, where a paragraph about Buckingham pi is a paragraph they skim.

*Sentence available for the text:* "the conversion coefficient is a numeraire, and every
result reported here is invariant to it across twelve orders of magnitude, while every
currency-denominated quantity scales with it exactly linearly." That answers "you invented a
constant" without conceding anything.

*Incidental result worth its own line.* Λ equals its physical value **only at the instants
the reported layer snaps to the real one**, and overstates it by roughly 14% on average in
between (at phi = 0.3). The coupling is not a constant that occasionally wobbles; it is a
sawtooth that touches truth only at corrections. That is WT-024's "Λ drift is the integral of
undelivered entropy" rendered as a picture.

**What this does not settle:** whether the coupling is *measurable* in practice, and whether
its drift means what WT-024 says it means. Both are empirical and the module claims neither.

---

## WT-037 · RISK · 2026-08-05 · **the largest remaining pre-print gap**
**The manuscript asserts computational results it does not contain, from a repository it does not name.**

Audited after the WT-033 edit landed. The document has, in 62,834 characters: **zero figures,
zero results tables, zero appendices, and zero references to the code.** The strings "github",
"repository", "appendix", "figure" and "source code" do not occur.

Meanwhile the repository holds five verified modules and 58 passing tests whose results the
text now leans on:

| module | result the text uses | ledger |
|---|---|---|
| `cournot.py` | tatonnement instability boundary at n>=3; the corner solution *is* the marginal pair | WT-001, WT-005 |
| `excess_demand.py` | 25 allocations, 25 demand schedules, **1** clearing interval; exact reduction to the Marshallian cross | WT-018, WT-019, WT-021 |
| `lag.py` | lag and crisis severity scale with unobservability; volatility relocated not suppressed | WT-027, WT-028 |
| `redistribution.py` | the base caps the reachable region; realisation is the crux | WT-033, WT-035 |
| `lambda_sensitivity.py` | the numeraire cancels across twelve orders of magnitude | WT-036 |

The text currently says things like "swept numerically over that process" with nothing for the
reader to inspect. For a pre-print that is the difference between a synthesis essay and a
paper: **a reviewer cannot check any of it.** It is also the cheapest remaining improvement per
unit of effort, because every number already exists, is regenerable from
`scripts/wt030_report.py` and `scripts/wt002_lambda_report.py`, and is defended by tests.

*Diagnosis superseded by WT-040:* the gap is real but it is a symptom. The paper does not
merely lack a results section — its contribution begins at 76% of the body. Fixing the
symptom without the restructure puts five results at the end of a paper nobody reached.

*Recommended shape, not yet built:* a Results section carrying four or five collapsed tables
plus the Λ scaling collapse as the one figure, and a Reproducibility note naming the repository
and the exact test command. This does not require new science. It requires transcription.

*Correction made the same day, before it could mislead anyone:* this entry first framed the open
question as "does the repository go public". **It already is** —
`github.com/jasoncbraatz/wealth-tensor`, visibility PUBLIC, created S1 and confirmed via
`gh repo view`. So citing it in the paper costs nothing and is available immediately. The
residual question is narrower and genuinely worth asking: `docs/LEDGER.md`, `docs/HANDOFF.md`
and `docs/sessions/` are *already world-readable* and contain candid internal assessments —
"the paper's weakest wall", "reads as ideology", "a reviewer finds this immediately". The
recommendation is to **leave them exactly where they are** and add one README line framing
`docs/` as a working lab notebook. A paper whose method section insists dead ends be recorded
with equal weight is strengthened, not embarrassed, by a public ledger that does it. But it is
Jason's call, not a Claude's.

---

## WT-038 · METHOD · 2026-08-05 · **reframes WT-002** · from Jason's note #3
**A first principle is an invariant with a stated domain, not an undeniable truth — and on that footing Λ is an entailment rather than a posit.**

The manuscript uses "first principles" four times and never defines one. Zero occurrences of
Aristotle, ontology, epistemology or primitive. The connection Jason was struggling to word was
not weak; it was **absent from the page**, carried in his head. Absent is far cheaper than broken.

**The type error.** An axiom is a *proposition* — truth-apt, deniable. A model is a *structure* —
it has interpretations, not a truth value. Promoting a structure to a proposition cannot be done
by rewording, which is why every wording attempt failed. The tensor is not the axiom. **The axiom
is the proposition that wealth has the structure the tensor formalises.**

**"Undeniable" is self-defeating and must go.** An axiom nobody can deny is a definition, and
definitions generate no empirical content. This repo *proves* the axioms are deniable: φ = 1 in
`lag.py` annihilates the phenomenon, realisation = 0 in `redistribution.py` makes a confiscatory
levy inert. Those regimes are committed, tested code. They are the evidence the claims are
empirical, not an embarrassment to be hidden behind a stronger word.

**Replacement, in the author's own idiom (CS, not philosophy).** A first principle in computing
is an **invariant**: never proved undeniable, proved *preserved*, within a *stated domain*.
P1 is a type declaration (`wealth : (Physical, Claim)`); P2 is a loop invariant; P3 is
compositionality. "Sound within a stated domain" is defensible; "undeniable" is not.

**Candidate axiom set**, stated as propositions a competent economist can deny:
- **P1 Composition** — every unit of wealth is a compound of a physical and a claim component,
  obeying different laws (thermodynamics vs arithmetic). Soddy, made axiomatic.
- **P2 Decay** — the physical component degrades absent maintenance; no store is inert.
- **P3 Atomism** — measured aggregates are folds over units; no aggregate is more fundamental
  than its constituents. This is what an aggregate-production-function economist denies.

Check independence before publishing. Three, not ten.

**The test that separates a principle from a result:** *denying a first principle produces a
different science; denying a result produces a wrong number.* Deny r > g → a different empirical
claim, same science. Deny "wealth has a physical component subject to entropy" → neoclassical
economics. Different science. The commitment passes.

**THE PRIZE — Λ stops being the weakest wall.** If P1 holds, wealth is a compound of two
components in different units, so **a relation between them must exist**. Λ is its name. The
coefficient was not introduced; it is *obliged*. The standing objection — "you invented a scalar
converting joules to dollars" — is answered not at the perimeter but at the root: nothing was
invented, and the only open question is whether the coupling is stable. It is not, and its drift
is the phenomenon (WT-024, WT-036). Three sessions of defending WT-002 are superseded by
reordering the argument.

**Open, and Jason should decide it:** P1 may not be indemonstrable. It may be an instance of a
general map/territory claim about representation and deferred information, of which wealth is one
domain. That is a more ambitious and more attackable paper — and given the author's signature
move recurs in 1993 (checksums) and 2026 (10-Ks), it may be closer to what he actually believes.

---

## WT-039 · METHOD · 2026-08-05 · **name it and do it on purpose** · from notes #3–#5
**The author's rhetorical method is relocation: never "you are wrong", always "you are a special case."**

Four instances, arrived at independently and none of them recognised as a pattern until now:

| target | the relocation | entry |
|---|---|---|
| Piketty | not wrong — measuring a different **layer** | WT-022 |
| SMD | not opposition — the mainstream **already proved it** | WT-013 |
| Austrian school | different cause, **same architecture** | WT-031 |
| Solow / scalar capital | not wrong — different **constraints** | WT-042 |

Every time, the disagreement is moved somewhere other than correctness, and a probable enemy
becomes a possible ally. For an outsider with no institutional armour this is not a stylistic
tic — it is the single strongest reason the paper could survive review.

*Action:* state it in the methods section as a deliberate strategy, and apply it consciously from
here. A method used four times by accident is worth more used deliberately the fifth.

---

## WT-040 · RESULT · 2026-08-05 · **supersedes the diagnosis in WT-037** · from note #4
**Measured: the contribution begins at 76% of the body and is one third the size of the history it follows.**

Jason asked whether the Cournot/Bertrand history should be condensed. Measurement says the
instinct was right and the diagnosis inverted.

- Cournot + Bertrand: **5,603 chars = 8.9%** of the document. Three sections are individually
  larger (Price Indifference 12.0%, Kinetic Exchange Summary 10.7%, Layer-Not-Error 10.5%).
  Halving it buys 4.5% and costs a join.
- Everything before "The Research Whitespace" is **40,411 of a 53,363-char body — 76%.** The paper
  is three-quarters over before it defines its own central object.
- "Define the Atomic Unit: The Thermodynamic-Financial Dual Tensor" is **1,893 chars** — *one third*
  of what Cournot and Bertrand receive.

**Do not condense Cournot — re-genre it.** It is not history in this paper; it is evidence
(WT-001 the corner solution *is* the marginal pair; WT-005 tatonnement unstable for n>=3;
WT-013's micro-instance). What is wrong is the *verb*: it narrates where it should assert.
History narrates, results assert — and asserting is shorter.

**The restructure all six notes converge on. Flip the paper: contribution first, literature second.**

1. **The constraint expired** — force-fit not form-fit, with dates and numbers (WT-042). Answers
   *why now*, which the paper currently never answers.
2. **What wealth is** — P1/P2/P3 as propositions with stated domains (WT-038). Currently the
   smallest substantive section; should be the largest.
3. **What follows** — the five verified results, currently in the repo and nowhere in the paper.
4. **Relation to existing frameworks** — the relocation method run as a section (WT-039). Absorbs
   most of the current historical material at roughly half the length, re-genred.
5. **What this does not settle** — Quine-Duhem stated honestly, architecture left open, WT-026
   named as the unrun severe test.

Note what §4 buys: every adversary the paper currently spends three-quarters of its length
fighting becomes, in one section, a special case of the thing just proposed.

*Cost is lower than it looks:* moving sections, changing verbs, transcribing results that already
exist, and writing one genuinely new page (§1).

---

## WT-041 · RISK · 2026-08-05 · **the ledger's own guard fired** · from note #5
**SMD is the shield, not the sword. The Marshallian cross is a conceded target; scalar capital is the live one.**

Jason proposed making SMD the absolute centerpiece of the defence against neoclassical defenders
of the Marshallian cross. Two prior entries had already forbidden exactly this, and
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` exists to enforce one of them.
**The fence worked.** Best single argument for the ledger discipline the project has produced.

**Technical objection (WT-020).** SMD needs at least two goods with income effects. The c(m)
construction is one good with unit demand and yields a *monotone* excess demand with a single
crossing. The two arguments attack different targets: c(m) attacks the *independence of the two
curves*; SMD attacks *uniqueness and stability under aggregation*. Centring SMD hands a referee a
ten-minute rejection: a multi-good general-equilibrium theorem misapplied to a single-good
partial model.

**Strategic objection.** SMD is fifty-one years old and fully digested — Hildenbrand and Grandmont
restrict preference heterogeneity and recover well-behaved aggregate demand; the standard reply
is that it is a possibility result, not an empirical claim. If SMD is the centerpiece, the
centerpiece is a half-century-old theorem the author did not prove, and the rejection is for
*unoriginality*, which is worse than being wrong because the actual contribution is not unoriginal.

**Target objection (WT-012).** Nobody defends the Marshallian cross; it is a pedagogical device
and Arrow-Debreu never used it. Arming heavily against an abandoned position reads as timid.

**The swap.** The live adversary is **capital as a malleable scalar** — the aggregate production
function, named in the manuscript's own opening paragraph. It is defended by working
macroeconomists today, it is where the Cambridge fight was actually fought, it is exactly what P3
denies, and it is where the zero-count names live (Sraffa, Robinson, Samuelson). SMD gets one
early paragraph whose only job is to establish that doubting inherited aggregation is *inside*
the mainstream. Then it stops being mentioned.

---

## WT-042 · CONNECTION · 2026-08-05 · **Jason's phrase, and it is better than the alternatives** · from note #5
**"Force-fit, not form-fit" — the scalar was a rational response to constraints that have since expired.**

The concession Jason intended — "the malleable scalar was necessary for simplification" — gives
away too much. It grants that the simplification was *innocent*, and the entire Cambridge
controversy was about it not being: Samuelson conceded in 1966 that with reswitching on the table
the marginal-productivity account cannot be recovered from an aggregate capital measure. A referee
reading the soft version replies: *the author grants the aggregation was harmless, then argues it
wasn't.*

**The version that costs nothing:** the scalar was necessary **given the computational and data
constraints of the mid-1950s**, its cost was known and explicitly accepted at the time, and **both
conditions have since expired.** Solow was explicit that the one-good economy was a device;
Samuelson conceded the cost; and the constraints are datable.

- **Compute** — a model of that era had to be analytically solvable because numerical solution was
  not available. Order 10^4 operations per second then; order 10^11 on a laptop now. Roughly seven
  orders of magnitude between "must have a closed form" and "hold a tensor per agent and iterate."
  *Source the figures from a citable spec sheet; do not take them from a Claude.*
- **Data** — the stronger half and usually forgotten. No firm-level panel, no machine-readable
  EDGAR, no national input-output energy tables at usable granularity, no SDG 7.3.1 series. The
  scalar was not merely cheaper to compute; it was the only object anyone could **populate**.

**Jason's criterion, in his words, and it beats the alternatives:** the old models were
**force-fit, not form-fit**. Distinguish a *benign* simplification (drops detail, preserves
structure, refining it changes numbers) from a *structural* one (collapses a distinction the
theory needs, refining it changes conclusions). Tested four times in this repo, structural every
time: collapse real and reported in `lag.py` and the phenomenon vanishes; collapse the levy base
in `redistribution.py` and a 100% levy reads identical to none.

*Why this matters beyond the concession:* it converts an apology into the paper's **motivation
section**, which the manuscript currently lacks — it motivates by *gap* (whitespace), never by
*use*. And it accuses no one of error, which is WT-039 applied to Solow.

*Related, from the same note and not yet in the text:* the representation is n-dimensional with
n >= 3; central banks run 2D regressions; COVID-19 documented the playbook gap. That is the
concrete "why care" and it belongs in §1 of the restructure.

---

## WT-043 · METHOD · 2026-08-05 · from note #6
**Defend Λ once, decisively, then stop. And what actually escapes the Odum trap is a result, not a paragraph.**

Jason asked whether the Λ dimensional defence should stay prominent by *constantly* emphasising
dynamic variance over a fixed value. Prominent yes; constant no. **A defence that recurs is a
tell** — five defences of one quantity tells a referee there are five soft places, and recruits
attention to precisely the spot one would rather they walked past.

**Three independent legs, deployed once, in one section, then never again:** Λ is an *entailment*
of P1 (WT-038); the numeraire *cancels*, spread exactly 0.0 across twelve orders of magnitude and
publicly checkable (WT-036); Λ^-1 *is* UN SDG indicator 7.3.1 (WT-003). Nothing signals a settled
question like an author who has stopped arguing about it.

**Posture correction.** "Emphasise variance over fixed value" still fights from the back foot. The
forward version: *a fixed value would be uninteresting; the trajectory is the finding.* Λ is the
paper's primary observable, not a nuisance parameter under guard. The Λ section becomes a results
section — same content, opposite posture.

**What the Odum trap actually was**, and how this framework scores:
- **(a) coefficients not independently measurable** — emergy transformities were derived from the
  accounting system that used them. Circular. **This framework passes decisively** (WT-003).
- **(b) no risky prediction** — it became closed accounting rather than a theory that could lose.
- **(c) therefore bookkeeping, not science** — follows entirely from (b).

So (c) hinges on (b), and (b) is **WT-026**: lag magnitude scaling with the unobservability of
degradation, where accounting standards themselves identify the unobservable categories and
neoclassical finance predicts no such gradient. **No amount of prose does the work that one
empirical result does.** Third independent time in one session that WT-026 surfaced as the
highest-value unbuilt item.

**Trap inside the proposal.** A Λ that varies freely and is never pinned forbids nothing — WT-016
in a new coat. Emphasise not that Λ *varies* but that it varies in a **specific parameterised
shape**: floor at unity at every correction, ceiling set by observability, mean 1.137 at φ = 0.3
(WT-036). A free variable is a liability; a shaped one is a prediction.

---

## WT-044 · HYGIENE · 2026-08-05
**Proper-noun audit: zero errors. The defect is missing attribution, not misspelling.**

Jason flagged that he types by phoneme rather than by memorised spelling (he wrote "Carnot" for
Cournot and "Odom" for Odum in conversation), so every name in the manuscript was audited.

**Clean.** `Carnot` appears once and is correct — Sadi Carnot, in "bounded above by the Carnot
limit," in the Λ dimensional-status section. Every near-miss resolved to something right:
`Chakrabarti` / `Chakraborti` / `Chakravarty` are three distinct real econophysicists and
co-authors of the manuscript's own reference #31; the R-model is correctly attributed to
Chatterjee-Chakrabarti-Manna; `Lorenzo` is Lorenzo Peccati; `Fairer` is a Niskanen Center title.
Zero common phonemic misspellings in the prose. The risk was real and the text is already clear of it.

**The actual finding — the ledger is ahead of the manuscript on attribution.** Names the arguments
depend on, appearing **zero** times in the body:

| absent | what depends on it |
|---|---|
| Mises, "malinvestment" | WT-031's Austrian convergence, the paper's strongest non-tribal move |
| Godley, Lavoie | an entire project titled *Thermodynamic Stock-Flow Consistent Systems* |
| Farmer, Lillo | WT-014's order-book microstructure landing ground (only Bouchaud, once) |
| Sraffa, Robinson, Samuelson | the Cambridge capital controversy — now the paper's live target (WT-041) |

Citations, not rewrites. Cheapest fix-to-value ratio in the document: each one moves an argument
from *floating free* to *standing in a literature*, which is how a referee decides whether the
author has read the room.

---

## WT-045 · HYGIENE · 2026-08-05 · **DONE**
**GNN demoted from asserted method to open empirical question; KAN added with a principled reason.**

Project 3's Mathematical Formulation asserted that "by training Graph Neural Networks (GNNs) and
Graph Attention Networks (GATs)... the econometrician can simulate contagion dynamics." A specific
ML architecture was load-bearing in a paper whose contribution is axiomatic — dating the work,
widening the attack surface to training data and generalisation, and repeating WT-015's failure
mode (borrowed glamour) in a new field. None of the five verified modules uses a neural anything.

Replaced with an architecture-agnostic paragraph: the estimation problem is posed but not settled,
**nothing in the axioms depends on how it is solved**, GNN/GAT are the obvious first candidates,
and spline-based approximators such as Kolmogorov-Arnold networks may suit a domain where the
learned couplings are expected smooth and low-dimensional **and where interpretability of the
fitted function is a requirement rather than a courtesy**.

That last clause is Jason's KAN instinct, and it is stronger than he pitched it: a GNN returns a
prediction, a KAN returns the learned univariate functions themselves. For a paper whose entire
defence is dimensional rigour and measurability, an approximator whose output can be *read* is a
principled preference rather than a fashionable swap. Verified structurally: 33 headings and 14
list lines byte-identical. Restore point `12jJh93VhgfOe8EQ3J23G9heQekSCdzxHTm75ut8RL6g`.
