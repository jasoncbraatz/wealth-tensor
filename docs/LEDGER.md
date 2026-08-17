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

## WT-026 · METHOD · 2026-08-05 · **THEORY BUILT + WRITTEN (`lag.py` φ) · EMPIRICAL TEST RUN S3 AND FAILED — see WT-048**
**The lag is selective, not uniform — and that asymmetry is the actual mechanism.**

> **Header corrected S3.** This entry read `BUILT + WRITTEN`, which was true of the *theoretical*
> asymmetry — φ in `lag.py`, written into the manuscript — and false of the *empirical* severe
> test, which was the START HERE of two consecutive handoffs. Anyone reading the ledger without
> the handoff would have concluded WT-026 was finished. Two claims were living under one number;
> they now have two. The empirical half is WT-048.

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

## WT-027 · RESULT · 2026-08-05 · **TABLE SUPERSEDED 2026-08-10 — see WT-053**
**Lag and crisis severity scale with unobservability. Verified.**

> **The table below does NOT regenerate from the committed code.** It was hand-transcribed
> from an exploratory run whose configuration no longer exists. The qualitative finding
> stands and is if anything stronger; the numbers are superseded by
> `scripts/wt027_report.py`, which is now the source of truth and is what Paper III quotes.
> Left in place rather than edited, because a ledger that silently corrects itself teaches
> nothing. See WT-053.

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

---

## WT-046 · METHOD · 2026-08-05 · **DECIDED — see `docs/adr/ADR-001-paper-decomposition.md`**
**The manuscript is four papers. Not too long — too broad for its length.**

7,711 words of body across **eight topics** (~950 words each), which is why the atomic unit — the
central object — receives **280 words**. The defect is breadth, not length, and it produces every
symptom already logged: WT-040's 76%, WT-037's absent results, WT-038's undefined first principle.

Every strategic move of S2 narrowed the attack surface. This applies the same discipline at the
level nobody had applied it: the document.

**I** price formation without independent curves (`excess_demand` + `cournot`, 20 tests) ·
**II** redistribution as a parameter space (`redistribution`, 18 tests) ·
**III** the dual tensor and the reporting layer — *the flagship*, carries the axioms
(`lag` + `lambda_sensitivity`, 20 tests, needs WT-026) ·
**IV** the atomic theory: composition across scales (cites I–III).

Publication order **II → III → I → IV**: II is the *rehearsal*, because Jason's stated gap is
preprint machinery rather than science, and WT-026 proceeds in parallel so the flagship is not
deferred. Full reasoning, evidence allocation and alternatives in the ADR. Do not re-litigate
without reading it.

**Audience, stated by Jason and load-bearing:** his three children, 8, 11 and 17. The paper is a
stewardship artifact. Two hard consequences follow, both now decided: `docs/` **stays public** —
a ledger in which WT-030 half-failed and was sharpened rather than defended teaches more about
method than any conclusion the papers reach — and **`Abandoned Approaches` is promoted from a
distinctive section to a load-bearing one**, appearing in every paper, populated from the
DEAD-END entries. When the audience is someone learning how to think, the method IS the message.

---

## WT-047 · HYGIENE · 2026-08-05
**Measured: the standard apparatus of a 2026 preprint is entirely absent, and one TODO is live in the deliverable.**

Zero occurrences of: **abstract** (the document opens with a rhetorical question), **keywords**,
**JEL codes** (an economics convention with no CS analogue — Jason last published in 1993, in CS),
**contributions statement**, **limitations section**, **data/code availability**, **affiliation**.

The code-availability gap is the expensive one. Economics has a known-poor replication record;
this project has five modules, 58 tests and every figure regenerable from two scripts, in a
**public** repo — and the manuscript does not mention any of it exists. That is the largest
unexploited asset in the project and it costs one paragraph.

Live placeholder in the text: *"Further entries to be migrated from the project findings ledger
as they accumulate."* The handoff gate refuses placeholders in handoffs; the manuscript has no
such guard. Consider one.

*Deltas since 1993 worth stating once, since they are the author's self-identified blind spot:*
preprints went from irregular to primary; reproducibility became a review criterion; an explicit
contributions list is now expected; related work is positioning rather than survey; and
**arXiv q-fin and econ.GN require endorsement for unaffiliated first-time submitters** — SSRN
does not, which matters for sequencing.

---

## WT-048 · RESULT · 2026-08-05 · **the severe test ran and the prediction LOST** · PRE-001, PRE-002, RESULT-001, RESULT-002
**Recognition lag does not scale with GAAP-assigned unobservability. Registered in advance, tested twice, replicated in a second sector, and refuted with power.**

WT-043 settled that what escapes the Odum trap is a risky prediction, not prose. The prediction was
registered at commit `9722342` **before any lag was computed**, and the git ordering of that commit
against the result commit is the only reason the word "prediction" applies to it.

**The claim.** Lag between the onset of deterioration and its accounting recognition increases
monotonically along an observability ladder that **US GAAP supplies and we did not**: PP&E
(scheduled depreciation, ASC 360) → finite-lived intangibles (scheduled amortisation, ASC 350-30)
→ indefinite-lived intangibles (annual test only) → goodwill (annual test only, ASC 350-20).
Neoclassical finance predicts no gradient. The institutional prior ran *against* us and was
registered as doing so: goodwill is the only tier standard-setters forced onto a mandatory annual
calendar, and PP&E has no scheduled impairment test at all.

**The result — four registered runs, four failures.**

| registration | universe | n events | JT z | empirical p | median t3 − t0 |
|---|---|---|---|---|---|
| PRE-001 streak | retail 5200–5999 | 120 | −0.177 | — | **−1.0 q** |
| PRE-001 streak | computer svcs 7370–7379 | 202 | +0.634 | — | 0.0 q |
| PRE-002 peak | retail | 244 | −0.290 | 0.590 | 0.0 q |
| PRE-002 peak | computer svcs | 444 | −0.095 | 0.520 | 0.0 q |

**And the null has teeth, which is the part that took the work.** PRE-002's design detects a
one-quarter-per-tier gradient with power **0.95** (retail) and **1.00** (computer services) at
α = 0.025. The label-permutation control returns null *z* of mean +0.007 / sd 1.025 and
−0.002 / 1.000 — the pipeline cannot manufacture a gradient, and the empirical p-values agree with
the parametric ones despite tier sizes of 21/34/34/155. This is not an absence of evidence. Over
the effect sizes the framework needs, it is evidence of absence.

**The stopping rule fired.** PRE-002 §5 was written before its result: if it fails, the line stops.
It failed and it stopped. There is no third instrument, because a hypothesis needing one on the
same data is a hypothesis being fitted.

**What this does NOT establish.** That the two-layer model is refuted. A failed test refutes a
*conjunction* — theory, instrument, bridge — and which link broke is not settled by a p-value.
Quine–Duhem is the paper's own stated caution (WT-025) and does not get to apply only when the
result is inconvenient. Candidates, all post-hoc and none admissible as evidence, in
RESULT-002 §4.

**The Odum verdict is unchanged by the direction of the answer, and this is the entry's point.**
Emergy's fatal defect was never that its predictions failed — it was that it *made none*. This
framework registered one in public and lost it. **The trap is escaped by betting, not by winning.**
A theory that has lost a stated bet is falsifiable, and that is the entire difference.

---

## WT-049 · METHOD · 2026-08-05 · **the most useful thing the failure produced** · post-hoc, not evidence
**A model parameter and a measurable that share a name may not share a meaning — and the bridge between them is a proposition nobody wrote down.**

`lag.py`'s φ is the observability **of degradation**. PRE-001 measured the observability **of the
accounting treatment** — whether an asset class carries an amortisation schedule. The registration
treated these as the same quantity and never said so out loud, because the identification felt
like a definition rather than a claim.

They may not merely differ; they may run *opposite*. Goodwill has no schedule, but its impairment
is triggered by conspicuously public signals — a share-price fall, a missed segment, a lost
contract. The physical condition of a distribution centre is on a schedule and is visible to
essentially nobody outside the firm. On that reading the ladder is not a φ gradient at all.

**This is WT-038's type error in a second costume.** There, a *structure* was being asked to do a
*proposition's* work and no amount of rewording could promote it. Here, a model parameter was
matched to a world quantity by name. The general rule, and it is worth more than the failed test:
**the bridge from a model's parameter to its measurable is itself a proposition with a stated
domain, and it must be written down and defended before it is measured — not assumed because the
two things are called the same word.**

Registered rule for this project, from here: **any pre-registration must state its bridge
assumption explicitly, as a numbered proposition a competent critic could deny**, alongside the
prediction. PRE-001 had a tier table and no bridge proposition. That is now a defect a
pre-registration can be rejected for.

*Status: conjecture. If it is ever tested it is registered fresh, from scratch, and it may not be
cited as though the failure of PRE-001/002 supported it.*

---

## WT-050 · METHOD · 2026-08-05 · **the instrument, not the hypothesis, was the binding constraint the first time**
**An unbroken-streak onset rule measures the volatility of the signal, not the phenomenon — and the tell was zero censoring.**

PRE-001 dated onset as the start of an unbroken run of YoY revenue declines. Symptoms, all visible
in the drop accounting before any theory was invoked:

- **zero censoring in 322 events across two universes.** Not one reached the 20-quarter cap;
- **69 % of lags ≤ 6 quarters**, piled at 2–4, observed maximum 15;
- **1,047 material charges discarded** for having no qualifying run — three to five times the
  number retained.

A streak is terminated by the *noise* of the signal, not by the phenomenon. And the discards were
not random: an event survived only if the firm happened to be in an unbroken decline, which
preferentially retains firms whose deterioration was **already visible** — the exact opposite of
the regime the hypothesis concerns.

Replacing it with the pre-charge peak in trailing-twelve-month revenue doubled retention
(322 → 688), took censoring to 8–14 %, and widened the IQRs to the registered range.

**The generalisable tell, and it is cheap: if a duration measure never hits its own cap, the cap
is not what is binding — something in the instrument is.** Same family as WT-034 (a saturating
statistic cannot detect convergence) and WT-028 (the first-draft metric measured the wrong object).
That is now three times in this project that the first-draft measurement was the defect. **Budget
for it: the first metric is a draft, and the way to find out is to ask what would have to be true
for the measure to reach its extremes, and then check whether anything ever does.**

---

## WT-051 · HYGIENE · 2026-08-05 · **verified against current documentation, not recalled**
**arXiv needs an endorsement; SSRN does not — but SSRN's rejections are final, unexplained and unappealable, which inverts the naive sequencing argument.**

WT-047 recorded that arXiv q-fin and econ.GN require endorsement for unaffiliated first-time
submitters and that SSRN does not. Both confirmed 2026-08-05 against the live documentation.
**One fact was missing and it changes the reasoning:** SSRN states that *"rejection decisions are
final. We do not provide individualized reasons for each rejection"* and that it *"does not
reconsider decisions to reject submissions."*

So the two venues are not "hard gate" versus "easy gate". They are:

- **arXiv** — a gate on the way in (find one endorser, who is asked only whether the paper belongs
  in the category, not whether it is correct), and a visible process on the way out.
- **SSRN** — no gate on the way in, and on the way out a **silent, permanent, uninstructive**
  rejection.

**Consequence for ADR-001's ordering, which survives but for a second and better reason.** Paper II
being the "rehearsal" cannot mean treating its submission as a cheap draw — SSRN gives no feedback
and no second attempt. Its rehearsal value is in **assembling the apparatus**, not in experimenting
with the submission. And the endorsement ask for Paper III gets materially easier once a paper
already exists in public with a clean apparatus and a public test suite, because the endorser is
being asked a *category* question, not a quality one. II then III is right; the reason is now
firmer than "SSRN is easier."

Captured in `docs/papers/PREPRINT-CHECKLIST.md` with sources, so the next session re-verifies
rather than re-researches.


---

## WT-052 · METHOD · 2026-08-10 · **the registration discipline had a hole and the reported result is in it**
**A pre-registration must precede the INSTRUMENT's code, not merely the result.**

L21 and the project's own practice held that what makes a prediction a prediction is the commit
ordering: register alone, push, then write the analysis code, then compute. **PRE-001 honoured that
exactly** — `9722342` is a single-file commit containing the registration and nothing else.

**PRE-002 did not, and PRE-002 is where the reported result comes from.** Commit `d655501`
registers `PRE-002-wt026-peak-to-charge.md` *and ships the peak-onset implementation in
`edgar.py`* — verifiable with `git log -S"peak" -- src/wealth_tensor/edgar.py`. RESULT-002 landed
later at `c43c484`, so the registration still precedes the outcome. What is **not** demonstrable is
that the instrument's details — onset window, tie-break direction, materiality floor — were fixed
before anyone saw what they produced. On a second look that is precisely where the surviving
researcher degrees of freedom live.

*Found by:* an adversarial referee agent run against Paper III v0.1 (`REVIEW-001`, finding F3). Not
found by three sessions of humans and Claudes reading the same commits, including one earlier the
same session that noticed `d655501` was both the PRE-002 commit and the last `src/` commit and did
not follow the thought through.

**The amended rule, effective now:** a registration commit contains the registration and nothing
else, *and* no code implementing the registered instrument may exist in the repository before it.
Where an instrument must be prototyped first, the prototype is committed and the registration then
declares which committed SHA it is registering — the ordering has to be visible either way.

**Not repairable retroactively. Disclosed instead**, in Paper III §5.1 and §10, at full strength.
A methodological gap that is disclosed costs a reader a discount; one that is discovered costs the
paper.

---

## WT-053 · METHOD · 2026-08-10 · **a number without a script is a number nobody has checked since the day it was typed**
**WT-027's results table did not regenerate from the committed code, and it was four hours from being published.**

Paper III's headline table came from WT-027. Regenerating it from `lag.py` at the committed
defaults gives **different numbers**: deferred information uniformly ~0.33 % low, recognition lags
1–2 periods short (φ=0.8 → 3 not 2; φ=0.5 → 14 not 12; φ=0.0 → 26 not 25). `lag.py` has exactly one
commit in its history, so the module never changed — the table was hand-transcribed from an
exploratory run whose configuration no longer exists anywhere.

**The control that distinguishes the two cases already existed and had simply not been applied
here.** WT-028's numbers, from the *same module*, reproduce bit-for-bit — because Paper II had
`wt030_report.py` and Paper III had no equivalent.

*Fixes, all shipped:* `scripts/wt027_report.py` written (tables A–D, incl. the §3.4 sawtooth);
`scripts/wt002_lambda_report.py` extended with the Buckingham-pi scaling collapse, which had been
living only inside `tests/test_lambda_sensitivity.py` and was therefore quoted by the paper with no
regeneration path; and **PREPRINT-CHECKLIST §A amended** — the regeneration command must be a
committed script that reproduces *every* number and has been run against current code.

**Bonus finding from the same exercise, and it upgrades a result rather than correcting one.**
Deferred information is not "approximately linear" in (1 − φ). It is **exactly** proportional:
substituting E(t+1) − C(t) = gap(t) + ΔE gives gap(t+1) = (1−α)·gap(t) + (1−φ)·ΔE, so with
gap(0) = 0 every gap carries the factor and — since ΔE < 0 throughout — the absolute integral
inherits it exactly. **D(φ) = (1 − φ)·D(0)**, confirmed to relative error 10⁻¹⁵. Two guard tests
added. The prose had *underclaimed* a closed form because nobody had run the sweep.

---

## WT-054 · METHOD · 2026-08-10 · **two adversarial agents, two disjoint classes of defect** · `REVIEW-001`
**Run the numbers agent and the reject-it agent. Neither finds the other's bugs.**

Paper III v0.1 was reviewed by two agents before any commit: one instructed to check every numeric
claim against the code that produced it, one instructed to find reasons to **reject** the paper,
given the ADR, the checklist, the registrations, the ledger and the sibling paper.

- **The numbers agent found 4 errors**, the worst being a conflation of PRE-001's two universes
  (z = −0.177 was the *pilot*, 120 events; the replication was z = **+0.634**, opposite sign) —
  **inside the section about honesty.**
- **The reject agent found 16**, including two rated FATAL that no amount of re-reading would have
  surfaced, because they were about what the paper *did to the reader* rather than what it said:
  (1) §6.1 certified that losing the bet cost the framework nothing, which puts it back in the
  Odum trap §6.3 claimed to escape; (2) §6.3 converted the loss into a virtue claim and then denied
  doing so in the same sentence.

**The sharpest single observation it made** was to turn the paper's own §3 rule against it: *a
defence that recurs is a tell.* The draft announced its own integrity in the abstract, §1, §5.2,
§7, §9 and §10. Five instances cut.

**It also caught the ADR alarm firing unheard.** The ADR-001 addendum written *earlier the same
session* said: "the alarm to listen for while drafting III is the urge to reach into I's or II's
evidence." §2.3 then used Paper II's headline empirical result as evidence inside Paper III's
argument. Writing a guard does not install it.

*Standing recommendation:* every preprint in this project gets both passes before it is committed,
and the report is kept in the repo beside the paper. `docs/` is a lab notebook; a paper that
publishes its own hostile review is the strongest single artifact this project can produce for its
stated audience.

---

## WT-055 · HYGIENE · 2026-08-10 · **one symbol, two objects, in the most-attacked section**
**Λ (dimensional) and λ (dimensionless) had been sharing a name since S1.**

`lambda_sensitivity.py` has always distinguished `Lambda_T = eta·C/E` (currency per joule) from the
coupling ratio `C/E` (dimensionless, mean 1.136838 at φ=0.3). The prose did not. So the three-legged
defence — entailment, numeraire cancellation, SDG 7.3.1 — attaches to the **dimensional** object,
while the sawtooth result and "its instability is the phenomenon" are about the **dimensionless**
one. Defending one quantity for a full section and reporting results about another under the same
symbol is a rejection-grade presentation defect, and it survived three sessions because both were
called "Lambda" in every document.

*Fixed in Paper III §3.1:* **Λ** dimensional, **λ** dimensionless, stated before the argument. The
manuscript and any future paper touching the coupling inherit the convention.

**Two related retreats, both accepted rather than argued down.** (a) The entailment argument
proves that *some relation* between the components must exist; it does not prove the relation is a
**scalar**, and the standing objection is to the scalar. WT-038's "prize" is therefore narrower
than recorded: the coupling is entailed, its representability as a scalar is an additional
modelling assumption. (b) SDG 7.3.1 is a **flow/flow** ratio and Λ is **stock/stock** — the same
type error WT-049 diagnosed, committed one more time in the defence against it. The dimensional
availability claim survives; the identity claim does not.

---

## WT-056 · METHOD · 2026-08-10 · **the compute question was a data question wearing a hardware costume** · `docs/notes/NOTE-001`
**φ is confounded with the EFFECTIVE DECAY δ = d(1 − m). Pin δ externally and φ recovers to ~10⁻³; leave it free and φ is badly conditioned across most of the swept δ range — a CONDITIONING result, not non-identifiability.**

> **Corrected 2026-08-10 (wealthTensor-05).** This entry was written before the adversarial audit recorded in `NOTE-001` §5 and kept the pre-audit algebra for a day after the paper and the note had been fixed — `d` where δ belongs (understating the divisor by (1 − m) = 0.4 in the flattering direction), 280× for the like-for-like 291×, “unrecoverable” for “ill-conditioned”, and the cherry-picked δ = 0.01 best case. See WT-057.

Jason asked whether a 3090 would carry a PyTorch port of the dual tensor, or whether HF/DeepInfra
GPU time would be needed. Characterising the workload answered the question and then produced
something better.

**The hardware answer, measured on a deliberately weak 2-core 2.8 GHz Xeon** (upper bounds, not
best case): forward+backward over the 400-step recursion costs 30 ms at *both* 1 firm and 100 firms
— the recursion is **latency-bound**, so the batch dimension is free until it is wide and a GPU
helps least. And **float64 is free on CPU** (6.7 ms fp64 vs 7.5 ms fp32) where a consumer Ampere
card runs fp64 at ~1/64 of fp32. Since this programme checks closed forms to 10⁻¹⁵, fp64 is the
working default and the 3090 is *disqualified by precision, not by size*. A full 10,000-firm,
300-step, float64 fit ran in **76 seconds**.

**The finding.** That fit recovered φ badly — median abs error **0.20** on a true range of 0.1–0.9.
Three checks, all like-for-like at B = 2000 and 400 Adam steps: the noise-free series fits *equally badly*
(0.21138, so not noise); **pinning δ at truth drops the median error to 0.00073** (p90 0.01727 — a **291×**
improvement in the median, so the confound is the whole story); and recovery degrades **continuously** as δ
falls, with no cliff: median 0.017 at δ ∈ [0.025, 0.035] against 0.468 at δ ∈ [0.005, 0.010].

**The algebra, which makes it structural rather than numerical.** The recursion is driven by the *effective*
decay δ = d(1 − m) — entropy rate d = 0.05 net of maintenance ratio m = 0.6, so δ = 0.02. Substituting
ΔE = −δ·E(t):

> **C(t+1) = C(t)(1 − α) + E(t)(α − φδ)**,  E(t) = E₀(1 − δ)ᵗ

**φ enters the observable only through the product φδ.** The data identify α, δ and k = (α − φδ);
φ = (α − k)/δ, a division by δ, so the estimator's variance grows like 1/δ². Pinning δ helps most where it
is needed least: at the §4.2 sector sketches converted to effective decay, δ pinned gives median 0.00026 for
software (δ = 0.080) and 0.00054 for industrial (δ = 0.020), but **0.00433 with a p90 of 0.191 for warehouse
retail (δ = 0.004)** — the slow-decay tail stays bad even in the best case.

**Consequence for REVIEW-001 F11, which this narrows sharply: to measure φ, acquire an independent
estimate of δ.** Depreciation schedules, useful-life assumptions in the filings, asset-life tables,
capex replacement cycles. No GPU is on the critical path and never was.

*Worth saying in Paper III eventually:* **to measure the observability of degradation you must
observe the degradation from somewhere the reporting layer is not.** φ is not recoverable from the
reported series alone without the physical series it is defined against.

**Disciplines observed, and they are the reason this entry is safe to keep.** Synthetic data only.
Different estimator from PRE-001/002 (parametric fit vs non-parametric rank test), so it **explains
nothing about their null and may not be cited as an account of it** — RESULT-002 §4 applies. The
tempting conjecture that the pilot universe (retail, lowest δ) was the worst-conditioned sector for
this parameter is **written down and left undeveloped**; any test of it registers from scratch. And
per **WT-052** the prototypes are committed as *declared scratch* with a written declaration
(`scripts/prototypes/README.md`) so a future PRE-003 can name the SHA it registers against — the
escape hatch WT-052 specified, used one day after it was written.

**No free parameter was added.** δ was always in the model — it *is* `entropy_rate` net of
`maintenance_ratio`. This proposes *measuring* it.

---

## WT-057 · HYGIENE · 2026-08-10 · **the fix reached the paper, the note and the handoff — and stopped one file short** · session wealthTensor-05

**A correction is not applied until it has been applied to every file that repeats the thing being
corrected. Grep for the corrected symbol, do not re-read the file you just fixed.**

wealthTensor-04 caught its own near-miss — the handoff was emitted before the last four fixes and
carried expired algebra for half an hour — and fixed it, and wrote the lesson down. The **LEDGER**
was not in the sweep. WT-056 sat at head for a day carrying **all four** of the errors the audit had
removed from `NOTE-001` and Paper III §8: `d` where δ belongs, 280× where the like-for-like pair
gives 291×, “unrecoverable below d ≈ 0.02” where the result is conditioning, and the cherry-picked
δ = 0.01 best case that `NOTE-001` §5 lists **by name** as error #2.

**Why this one is worse than the handoff near-miss it rhymes with.** A handoff is read once by one
session. `LEDGER.md` is named in the orientation block of every handoff as *the project's brain*, and
the standing instruction is to read it before touching anything. An error there is not stale — it is
**authoritative and stale**, which is the combination that gets copied forward. A future session
would have read the corrected paper and the corrected note *and then* read the uncorrected ledger,
and had no way to tell which was current.

**The mechanical rule, which costs one command.** After correcting a symbol or a figure anywhere,
`grep -rn` the **wrong** form across `docs/` and `src/` and confirm zero hits before committing. Do
not verify by re-reading the file you just fixed; that file is the one place the fix is guaranteed
to be. This is the fourth instance of the notation family (WT-049, WT-055, WT-056's draft, now the
ledger copy of WT-056) and the first where the correct text and the incorrect text were **both at
head, in the same repository, at the same time**.

*Found by:* reading `docs/LEDGER.md` at orientation exactly as the handoff instructs, and noticing
that its algebra disagreed with the paper's.

---

## WT-058 · HYGIENE · 2026-08-10 · **a patch script that applies as it goes leaves a half-patched tree** · session wealthTensor-05

**A multi-anchor edit script must validate every anchor BEFORE it writes the first byte.**

wealthTensor-05's first patch script did sixteen exact-match replacements in a loop, each one
asserting its anchor and writing immediately. Anchor twelve missed — a hard-wrapped sentence broke
after *negative* rather than after *conventional*, so the literal did not match — and the script
exited with eleven edits already on disk and five not. The tree was in a state no commit and no
`git checkout` described: not the old version, not the new one, and not obviously either from
`git status`.

The fix is four lines and it is the difference between a failed run and a *recoverable* failed run:
build the replacements into a dict of in-memory texts, assert every anchor against those texts, and
only then write. A miss now prints `ANCHOR FAIL, NOTHING WRITTEN` and the tree is exactly as it was.

**Two companions, both cheap.**
- **Anchor on a span with no internal line break** where the file is hard-wrapped at 100 columns.
  Wrapping is invisible in a rendered view and load-bearing in a literal match. Every anchor that
  missed in this session missed on a newline, never on a word.
- **This generalises the `.bak`-first rule to scripted edits.** "Create the undo path first" is
  satisfied by git for a *clean* tree; it is not satisfied for a tree the script itself dirtied
  halfway. Validate-then-write is what makes the undo path exist at the moment it is needed.

*Cost this session:* one round trip and a hand-written continuation patch. *Cost if the miss had
been at anchor two instead of anchor twelve:* the same. That is the point — the failure is silent
about its own size.

---

## WT-059 · METHOD · 2026-08-10 · **verifying a reference is not the same act as verifying a citation** · session wealthTensor-05

**A bibliographic check asks “does this work exist with these details?”. A provenance check asks
“is this the object the claim is about, and is it the one I read?”. They are different questions
and the first one passes while the second fails.**

Paper III's seventeen references were verified against publishers, library catalogues, Crossref and
issuing-body documentation and every one came back correct. Then the same list was checked against
**Jason's own digitised library** — copy-matched scans of the prints he owned — and three of the
five books present there were being cited as the wrong object:

| entry | what the catalogue said | what his copy says |
|---|---|---|
| Popper | *The Logic of Scientific Discovery*, Hutchinson & Co., 1959 | Routledge Classics **2002**; colophon gives *Logik der Forschung* 1935, preface dated 1934 |
| Soddy | George Allen & Unwin, 1926 | **third edition, Omni Publications, 1961**, LCCN 60-53331, reprinting the 1933 second edition |
| Piketty | Belknap Press, 2014 | 2014 Belknap **and** a 2017 HUP printing, both Goldhammer; French original Seuil **2013** |

Both were right. They were answering different questions.

**The rule adopted, and it is two rules that had been welded into one.**
1. **Cite the edition consulted.** This is the near-universal modern norm (APA 7, Chicago) and it is
   an *honesty* rule, not a scholarship one: pagination, wording and — for translations — the actual
   sentences are edition-specific, so pointing at an edition never opened is a small false statement
   about one's own evidence.
2. **Cite the first appearance only when making a claim about firstness.** Jason remembered this as a
   general obligation from 1993. It is not, and never quite was — it fires on priority claims and
   nowhere else. Dual dating (`1926/1961`) discharges both at once.

**The corollary that matters more than either.** *Reading order is irrelevant to citation.* No style
guide has ever asked what sequence a bibliography was consumed in. It asks what is on the shelf, and
separately what came first. A researcher who picks the next book by its title is running a
high-variance sample of a literature, which is how a Nobel chemist's monetary theory ends up in an
econophysics paper at all.

**Where it did NOT fire, which is the discipline half.** Georgescu-Roegen's copy is the Harvard
Paperback *second printing* of 1974. A printing does not change the edition and is **not** dual-dated;
the entry stays 1971. Adding provenance noise where provenance did not change is the failure mode on
the other side of this rule.

**Open, and it needs Jason.** Four cited books — Mises, Godley & Lavoie, Mayo, Odum — are in neither
store, so their editions cannot be named on the same evidence as the other five. Filed against
`REVIEW-001`, not the Batter's Box: a Claude with darwin can check a library, but only he knows which
copy he read.

*Found by:* Jason asking whether the first-appearance rule he learned in 1993 was still practice. It
half is, and asking the question found three wrong citations in a list that had passed verification
forty minutes earlier.

**Postscript, same session, ten minutes later — WT-057 fired inside the file that documents it.** The
References section's closing summary still read “Popper is Hutchinson & Co.” after the Popper *entry*
directly above it had been changed to Routledge Classics 2002. The entry was corrected; the sentence
*about* the entry was not. It was caught by reading the rendered section end to end rather than by
grepping, which is worth noting because **the WT-057 grep would not have caught it either** — the
stale text contained no wrong symbol and no wrong number, only a right fact about a superseded
decision. Grep finds stale *tokens*; only reading finds stale *claims*. Both passes are needed and
they catch disjoint things — which is the same shape as WT-054's two adversarial agents, and by now
the third time this project has learned that two cheap different checks beat one thorough identical
one.

---

## WT-060 · METHOD · 2026-08-10 · **an inconsistent word is worth checking, because it may not be an inconsistency** · session wealthTensor-05

**Before standardising on one of two words, check whether either is already a term of art in the
field you are writing for. Ours was — both of them, and the one we were leaning toward was wrong in
the exact standard the paper is built on.**

Paper III used *correction* 29 times and *crisis* 12 times for the same event. Jason read it as a
vernacular tic from eleven years of notes taken at different times, and asked which word current
academia prefers — a reasonable question with a reasonable premise. The premise was wrong twice:

1. **Finance.** A *correction* is a defined magnitude: a decline of at least 10% from a recent peak
   (FINRA; Schwab). A finance referee reads that on first encounter, 29 times.
2. **Accounting, and this is the one that would have cost something.** **ASC 250 is titled
   *Accounting Changes and Error Corrections*.** An impairment is a change in **estimate**, driven
   by information that arrives later; an error is a mistake about facts that existed at the time.
   Calling the event a *correction* asserts, in the technical register of the codification §5 is
   built on, that the prior financial statements were wrong and require **retrospective
   restatement**. That is a substantive misstatement of the accounting, not a style problem.

**Resolution.** The body uses **recognition event** — the verb ASC 350 itself uses ("shall recognize
an impairment loss"), so it names the mechanism rather than a consequence, and it collides with
nothing. *Impairment loss* where the referent is literally ASC 350. **Crisis** is kept in the title
and for the phenomenon, with a definitional sentence in §4.1 disclaiming the systemic country-level
sense. Rejected on evidence: *shock* (inverts the endogenous/exogenous distinction the whole
mechanism rests on), *impairment event* (ASC 350's "triggering event" already means the thing that
prompts a test), *adjustment* (the crash-risk literature uses it for the gradual counterfactual),
*critical transition* (invites a demand for critical slowing down the model cannot supply).

**And the question found something bigger than itself.** Searching for the field's preferred word
surfaced the **stock price crash risk** literature — Jin & Myers (2006), Hutton, Marcus & Tehranian
(2009), and an unbroken stream through 2026 — which models firms hoarding bad news until it releases
all at once and the price moves discontinuously. **That is Paper III's thesis, published twenty years
earlier, and the paper cited none of it.** Now positioned in §9, including the sentence that this
paper is the weaker of the two on evidence. It was the single most likely reject-reason in the draft
and it was invisible from inside the project's own vocabulary.

*The transferable rule:* **a word you use inconsistently is a word you have not checked.** The
inconsistency is not the defect — it is the *symptom*, and the useful move is to look up what the
word already means to your readers rather than to pick the more frequent one and move on. Jason's
instinct to fix the tic was right; the fix was not the one either of us expected.

---

## WT-061 · HYGIENE · 2026-08-10 · **a hand-maintained summary sitting next to the thing it summarises will go stale on every edit** · session wealthTensor-05

**Three strikes in one session, all in the same paragraph. That is not bad luck, it is structure.**

Paper III's References section ended with a prose note summarising what the verification pass had
changed — how many entries were uncited, which publishers were wrong, which entries carried which
mark. Every subsequent correction to an *entry* silently invalidated the *note*:

| pass | what changed in the list | what the note still said |
|---|---|---|
| provenance | Popper → Routledge Classics 2002 | "Popper is Hutchinson & Co." |
| library match | Mayo removed entirely | "Six now do work in the text" (five) |
| library match | Odum → Columbia UP 2007 | "Odum is John Wiley & Sons" |

Each time it was caught by **reading the rendered section**, and each time the WT-057 grep would
have missed it — the stale text contained no wrong symbol and no wrong figure, only a right fact
about a superseded decision.

**The structural diagnosis, which is the transferable part.** A summary adjacent to its subject has
no mechanism forcing the two to agree. It is a *derived value cached by hand*, and a hand-cached
derived value goes stale on every write to its source — the same failure as a hard-transcribed table
(WT-053), one level up in abstraction, and with no test that can fail. WT-053's answer was *make the
number come from a script that has been run*. The same answer applies here and this project is not
yet paying it: the note should either be **generated** from the list, or be written so it says
nothing that a later edit can falsify — history and reasoning, which do not change, rather than
counts and publishers, which do.

**The rule adopted.** *Prose that counts or names items in an adjacent list is a cache. Either
generate it, or write only the parts an edit cannot invalidate.* The rewritten note keeps the
narrative — which citation was added and withdrawn and why — and drops the running tallies, except
where the number IS the finding.

*Worth saying plainly, because it is the third distinct class of staleness this project has found in
two days:* WT-057 was a fix that did not reach every file; WT-059 was a check that answered the wrong
question; this one is a claim that was true when written and was never re-derived. Grep catches the
first, a different pass catches the second, and **only regeneration catches the third.**

---

## WT-062 · HYGIENE · 2026-08-10 · **search a personal library by TITLE, not by author — and a null result from a sprawl is not evidence of absence** · session wealthTensor-05

**Two false conclusions in one session, both from searching an eleven-year reading library the wrong
way, and both in the flattering direction of "the citation is unsupported, remove it."**

The provenance sweep (WT-059) searched `~/Desktop/downloads` and the `BOOK MASTERS` archive **by
author surname**. It returned:

- **A false positive.** `Mayo` matched *Government and Business: The Economics of Antitrust*, by
  Kaserman and **John W. Mayo**, an antitrust economist. The paper cites **Deborah G. Mayo**, a
  philosopher of statistics. The sweep reported a match and the match was a different person.
- **A false negative.** `odum|emergy|environmental account` returned two Odum books but not
  *Environmental Accounting*, so the entry was re-pointed to a book he owns but which was not the one
  the argument came from. It was on a different Kindle. **He has seven.**

**The mechanical cause, in his words:** Kindle exports usually do **not** put the author in the
filename — it lives in the AZW metadata, and older devices do not index those fields. **Title is the
searchable field, and it is also the more distinctive one.** Search `"environmental accounting"`, not
`odum`. Search `"error and the growth"`, not `mayo`.

**The judgement error underneath it, which is the part worth keeping.** A sweep over a *sprawl*
returns absence-of-evidence, and it was reported as evidence-of-absence — as "four cited books are
not in the author's library." The honest form was available and was not used: *a search of the
indexed subset, by a field that subset does not reliably carry, did not find them.* Note the
direction: **both errors pushed toward deleting a citation**, which felt like the rigorous move and
was the careless one. Rigour that only ever subtracts is not rigour, it is a bias with good manners.

**And the outcome inverted.** Searching properly did not merely restore what had been removed:

| | before | after |
|---|---|---|
| Mayo | (2018) *Statistical Inference as Severe Testing*, unread | **(1996) *Error and the Growth of Experimental Knowledge*** — 374 uses of *severity*, where the requirement is **introduced**, and read. Plus *Error and Inference* (Mayo & Spanos, CUP 2010), the volume of exchanges with her critics. |
| Odum | (1996) Wiley, unverified | (1996) Wiley, **✓✎ against the copy** |

The Mayo citation is now correct on **both** rules at once — it is the edition consulted *and* the
first appearance — where before it was neither. **An hour spent believing a citation was unsupported
produced a better citation than the one that was there.** File that next to WT-054: the value was in
the attack, not in its verdict.

*Standing amendment to the library-search procedure (HANDOFF L24):* search by **title**, treat a null
as "not found in the indexed subset", and **ask Jason before removing a citation on the strength of
one.**

---

## WT-063 · RESULT · 2026-08-10 · **the allocation cancels from the DIFFERENCE, identically — not just at the crossing** · session wealthTensor-06

**Paper I's central claim was being made one step weaker than the code supports, and writing its
regeneration script is what exposed the gap.**

WT-018 reported the experiment as *the schedules move, the crossing does not*: 25 allocations of the
same c(m) and the same S give **25 distinct demand schedules** and **1 distinct clearing interval**.
From that pair a reader is invited to *infer* that the schedules cannot be independent equations —
two things that both move under a perturbation which leaves the equilibrium fixed are not free to
vary separately.

The inference is unnecessary. Measured on 399 interior grid points with the ties excluded:

| object | distinct values over 25 allocations |
|---|---|
| demand schedule D(p) | **25** |
| supply schedule S(p) | **25** |
| **excess demand z(p) = D(p) − S(p)** | **1** |

and that one function equals `#{i : m_i > p} − S` **exactly, at every grid point**. The reason is a
one-line partition argument and it is not asymptotic, statistical or seed-dependent:

> The S holders split at any price p into those with m_i > p and those with m_i < p. So
> S(p) = #{holders, m_i < p} = S − #{holders, m_i > p}, and
> D(p) − S(p) = #{non-holders, m_i > p} − S + #{holders, m_i > p} = **#{m_i > p} − S.**

*Why it matters, and it is the difference between a good paper and a sharp one.* "The curves are not
independent" is an inference from two measurements. **"The allocation cancels from their difference
identically" is an algebraic fact about the construction**, and it says something strictly stronger:
the decomposition of z into a supply half and a demand half carries **no economic content whatever**.
Only z is structural. D and S are a bookkeeping choice about which side of the ledger to write each
agent on, and the textbook draws them as if the choice were data.

This also gives the reduction result (WT-019) its proper shape. The Marshallian cross is a valid
snapshot **because** it reads the zero of z correctly; it fails as a comparative static **because**
it treats a bookkeeping split as two perturbable objects. Same theorem, both directions, one line.

Pinned by `test_excess_demand_is_identically_invariant_to_the_allocation`, which asserts all three
counts (25 / 25 / 1) *and* the closed form, so a future simplification cannot quietly weaken it back
to the crossing-only claim.

**A tie convention worth stating, because it cost twenty minutes and looked like a result.** The
first run used a coarse 12-point grid spanning `[M.min(), M.max()]` and reported **4** distinct
excess-demand schedules, which read as a partial invariance and nearly went into the paper as one.
Both endpoints are themselves data points, and `demand_at`/`supply_at` use strict inequalities, so at
p = min(m) the minimum agent is counted by neither — and whether that agent happens to hold a unit
varies by allocation. Two endpoints × two holding states = the 4. **It was a boundary convention, not
an economic effect.** The grid now excludes any point within 1e-9 of an m_i, in the script and in the
test, with the reason written next to it.

---

## WT-064 · RESULT · 2026-08-10 · **the damping that rescues Cournot tâtonnement vanishes like 4/n, so the repair needs exactly what the model denies** · session wealthTensor-06

**WT-005 established the instability. This is the sharper form of it, and it was found by a test
failing for a real reason.**

WT-005: the undamped best-response map has linearised gain (n−1)/2 — stable at n = 2, marginal at
n = 3, non-convergent beyond — and the standing gloss was *"damping rescues convergence, but damping
is an inertia assumption the original model does not contain."* True, and it undersells the point.

Writing Paper I's regeneration script extended the existing test's n ∈ {3, 4, 6} to n = 10 at the
same damping 0.4 the test uses, and it **failed**. Not a numerical artefact. Damped, q ← q + d(BR(q) − q)
has linearised gain |1 − d(n+1)/2|, so the process is stable **iff d < 4/(n+1)**. Measured on a 0.02
grid, the boundary is bracketed at every n tested:

| n | 4/(n+1) | largest d converging | smallest d failing |
|---|---|---|---|
| 2 | 1.3333 | 1.32 | 1.34 |
| 3 | 1.0000 | 0.98 | 1.00 |
| 4 | 0.8000 | 0.78 | 0.80 |
| 6 | 0.5714 | 0.56 | 0.58 |
| 10 | 0.3636 | 0.36 | 0.38 |
| 20 | 0.1905 | 0.18 | 0.20 |

**The threshold is not a constant to be chosen once. It vanishes like 4/n.**

*Why it matters.* The damping repair is usually treated as a technical patch — firms adjust
sluggishly, convergence returns, move on. But the sluggishness required is **a function of n**, so
each firm must know how many rivals it has and condition its own adjustment speed on that number.
Cournot's dynamic is built on the expectation that rivals hold output constant; the repair for its
instability demands that every firm track the size of the field and slow itself in proportion.
**The fix requires precisely the information the assumption denies.** That is a structural claim
about the model (WT-056) with no expiry date, and it is stronger than "damping is an extra
assumption" because it says *which* assumption and *how much* of it — a quantity that grows without
bound as the market gets more competitive, which is the direction the model is usually defended in.

Pinned by `test_the_damping_that_rescues_tatonnement_shrinks_like_4_over_n`. The pre-existing
`test_tatonnement_stability_boundary` now states, as an assertion rather than a comment, *why* its
damping of 0.4 works for the three n it tests: 0.4 < 4/(n+1) holds only while n < 9. That trio was
never arbitrary; nothing recorded that it was not.

**Cleared on the way past (BUG SPRAY).** `tatonnement` overflowed to `inf` on the genuinely divergent
branch, one line before its own `isfinite` guard caught it and raised — putting a numpy
`RuntimeWarning` into a fully passing test suite. Divergence is a documented outcome of that function,
not a surprise, so the loop is now wrapped in `np.errstate(over="ignore", invalid="ignore")` with the
`isfinite` check left in place as the real guard, and the reason written above it. Suite is clean.

---

## WT-063 · **CORRECTION** appended 2026-08-10, same session · two errors in the entry above

**1 · The tie-convention story misdescribes its own fix, in the entry that exists to record it.**
The paragraph above says the grid "now excludes any point within 1e-9 of an m_i". Measured: that
filter removes **zero** points from the actual grid — 399 interior points before it, 399 after. The
entire 4 → 1 correction came from dropping the two **endpoints**, which are `M.min()` and `M.max()`
and are therefore data points. The filter is a correct guard against a case that does not arise
here; it is not what fixed this. *An entry whose subject is a near-miss in self-reporting, getting
its own self-report wrong.* Both the script and the test are correct — only the description was
wrong.

**2 · The identity's caveat is dropped in the entry's own headline.** "at every price, not merely at
the crossing" is false at ties. At *p* = *m_j* the tied agent falls in neither part of the partition
and *z* **is** allocation-dependent: at the clearing interval's own endpoints, *z* = −1 for 16 of the
25 allocations and 0 for the other 9. The correct statement is the one the derivation actually
supports — **at every price that is not itself a reservation price** — and both endpoints of the
marginal pair are tie prices, so the caveat is not a technicality.

**3 · And the claim the entry drew from it does not follow.** WT-063 concluded that the identity
licenses *"the decomposition carries no economic content"* and, in the paper, that the schedules
"cannot be perturbed independently". **The second does not follow from the first.** The invariance is
to *reallocating units with reservation prices held fixed*, which is not an operation comparative
statics performs. Change only non-holders' valuations and the supply schedule is unchanged at every
grid point while demand moves and the price moves with it. See REVIEW-002 §F1. **The surviving claim
is narrower: the schedules are not independent *as functions of the allocation*.** Whether even that
is new is open — see the priority audit.

---

## WT-064 · **CORRECTION** appended 2026-08-10, same session · this is not a new result, and its gloss was wrong

**The entry above should not have been filed as a RESULT. It is a recapitulation.** Filed here as a
correction rather than deleted, because how it happened is the useful part.

**Prior art, complete.** The undamped gain (*n*−1)/2 and the loss of asymptotic stability at *n* ≥ 3
are **Theocharis (1960)**, *Rev. Econ. Stud.* 27(2), 133–134 — argued twenty years earlier still by
**Palander (1939)**. That the required adjustment speed *falls* as *n* rises is **Fisher (1961)**,
*Rev. Econ. Stud.* 28(2), 125–135, on his own p. 125: *"the tendency to instability does rise with
the number of sellers for most of the processes considered."* And the bound itself, *d* < 4/(*N*+1),
is **eq. (2.26)** of Bischi, Chiarella, Kopel & Szidarovszky, *Nonlinear Oligopolies* (Springer,
2010), where it appears as a routine worked example.

**A second correction, independent of priority: the gain expression above is wrong.** The damped
Jacobian is (1−*d*)*I* + *dF* with *F* = −½(**11**ᵀ − *I*), so the eigenvalues are 1 − *d*(*n*+1)/2
with multiplicity 1 **and 1 − *d*/2 with multiplicity *n*−1**. The gain is the spectral radius of
those, not the first term alone — which vanishes at *d* = 2/(*n*+1) where the true gain is still
1 − *d*/2. The **stability condition survives** only because 4/(*n*+1) ≤ 4/3 < 4, so the symmetric
mode always binds first. *The condition was right for a reason the wrong expression happened not to
disturb*, which is the least reassuring way for a claim to be correct.

**Third, the epistemic gloss is withdrawn entirely, and it was the part that felt like the
discovery.** The entry claimed that the repair "requires each firm to know *n*, which the model
denies". It does not:

- Cournot's *static equilibrium* q_i = (a + Σc − (*n*+1)c_i)/(b(*n*+1)) **is not definable without
  *n***, so *n* is not denied by the model — it is presupposed by it.
- **Sequential (Gauss–Seidel) best response converges undamped** at *n* = 2, 3, 4, 6, 10, 20 and 50.
  The instability is an artefact of *simultaneous* updating, a modelling choice, not of Cournot's
  expectation.
- **One fixed damping chosen once** (*d* = 0.10, or 0.05) converges at every *n* in the table. At
  most a modeller needs an upper bound on *n*; no firm needs to know it.
- A **diminishing gain** d_t = t^−0.6, with no knowledge of *n* at all, converges at *n* = 3, 10, 20.

Three counterexamples, produced by an adversarial referee in minutes, against a claim that had by
then been written into a paper, an ADR addendum, and a message to Jason. **An *n*-dependent
parameter was dressed as an epistemic scandal.** The measured 4/(*n*+1) table is fine and stays; the
story told about it does not.

---

## WT-065 · METHOD · 2026-08-10 · **WT-054 fires too late: adversarial review belongs at the moment a finding is CALLED a result, not at the preprint** · session wealthTensor-06

**The rule as written was *two adversarial agents before any preprint commits*. This session
demonstrated that the damage is done well before that.**

The sequence, which is the evidence:

1. Wrote `wt018_report.py` to guard against WT-027's failure mode. The guarded-against thing did not
   happen — every hand-transcribed figure regenerated bit for bit.
2. The script surfaced two things the modules supported and nobody had stated. Both were checked
   against the code, found to reproduce, and **that check was mistaken for verification.**
3. Both were banked as ledger entries (WT-063 RESULT, WT-064 RESULT), pinned with new tests, written
   into a paper, recorded in an ADR addendum, committed, pushed, and **reported to Jason as
   discoveries.**
4. Later the same session, the adversarial pass found that one was in a 2010 textbook as a routine
   exercise with a 1960 and a 1961 ancestor, and that the other's headline gloss was refuted by
   three counterexamples the referee wrote in minutes.

**Nothing in step 2 was wrong.** The numbers were right, the algebra was right, the tests pin real
behaviour. What was missing is that *reproducing from the code* answers "is this true of the model?"
and says **nothing** about "is this new?" or "does the interpretation follow?" — and those are
different questions, in exactly the way WT-059 established that verifying a reference and verifying a
citation are different acts. **This is the same lesson arriving in a new place: the pass that comes
back clean is the one whose cleanliness is most misleading.**

**The rule adopted, amending WT-054.** *The trigger for adversarial review is the moment a finding is
about to be called a **result** — banked in the ledger, written into a paper, or told to Jason —
whichever comes first. Not the preprint.* Concretely, before a finding earns the word:

- **a priority check**, run by an agent told that an over-eager priority claim is as damaging as a
  missed one, so it does not simply agree;
- **an attempt to refute the interpretation**, separately from checking the arithmetic — the
  arithmetic was never in doubt here;
- and for anything with a *rhetorical* payload — "the repair needs what the model denies" — the
  **specific** question *what would have to be true for this to be false, and is it?*

**Cheap, and it would have worked.** The priority audit cost one agent and a few minutes, and it
would have prevented four artifacts from carrying a false claim. Running it before the ledger entry
rather than after the push is a scheduling change, not extra work.

*The companion observation, which is Jason's standing doctrine arriving on schedule.* The failure was
worth more than the result would have been. **A false "we found something new" that survives to a
referee costs the paper; the same claim caught in-session costs one commit and produces a better
paper, a corrected ledger, five citations the paper needed anyway, and this rule.** Failures are
gold — but only if the machinery that catches them runs before the belief hardens, and the whole
content of this entry is *when* that machinery should fire.

---

## WT-066 · Paper I's last surviving claim is Wicksteed (1910). DISPLACED.

*wealthTensor-07, 2026-08-11. Full audit: `docs/papers/paper-I-price-formation/REVIEW-003-priority-audit.md`.*

`REVIEW-002` rejected Paper I on four FATAL findings and left exactly one claim standing — that the
allocation cancels from excess demand identically, *z*(*p*) = #{*mᵢ* > *p*} − *S*, at every
non-reservation price — and made a literature search a **precondition** of any redraft. The search
was run. **The claim is Philip H. Wicksteed, *The Common Sense of Political Economy* (Macmillan,
1910), Book II Ch. IV**, on the same Böhm-Bawerk/Hobson horse market, with the same reallocation
exercise. Every quote verified first-hand against the 1910 first edition, not accepted from an agent.

> "**The irrelevant facts are that the eight horses are at present in the possession of A-H**, and
> that I-R are all without horses."

> "**The method of intersection is, in fact, a mere disguise of the method of addition** … if adopted
> to shew the ultimate considerations that determine the market price, it is, to say the least of it,
> **seriously misleading and mischievous**."

The second quote is Paper I §5's thesis, 1910, better argued.

**Three consequences, each of which costs us something.**

1. **Within the market, our version is the SPECIAL case.** Wicksteed's damson stall-keeper and
   Marshall corn market are divisible goods with multi-unit holdings; our identity requires each
   holder to hold exactly one unit. He does not need our restriction. This must be conceded in print.
2. **Our corollary was overclaimed.** We wrote that the supply/demand split *"carries no economic
   content."* Wicksteed: it has content for exactly one thing — *"the initial distribution of the
   stock affects the amount of business done"* — and none for price and final allocation. **Volume is
   allocation-dependent; excess demand is not.** He is right and we were sloppy.
3. **Böhm-Bawerk runs the other way, and Jason called it before the audit did.** *Positive Theory of
   Capital* p. 203 — ten buyers, eight sellers — and p. 209's **"Marginal Pairs"** needs *four*
   parties in two pairs. Pool the eighteen at *S* = 8 and the bracket is two order statistics. That
   is not us being his special case; it is the distinction his statement requires being dissolved.
   Arithmetic re-verified against Jason's own copy.

**Lineage: Böhm-Bawerk (1889) states the two-sided form → Wicksteed (1910) shows the two-sidedness is
irrelevant → Paper I restated Wicksteed.** Disposition (Jason, same day): **re-scope Paper I around
P3 · Atomism**, one level up, where Wicksteed's subjective-value apparatus cannot follow. Not
scooped — **written one level too low.** It went out as a market result and met the man who owns
markets.

**Pages, and the L24 lesson landing the right way up.** The audit's first draft inferred from two
PDFs — both Vol. I — that Jason had never read the displacing chapter. He said his memory was of
reading Vol. II, went and charged a Kindle that had been flat for years, and **produced it the same
day.** Bk II Ch. IV is **pp. 493–526** in the 1933 Robbins edition; every quote survives **verbatim**;
the six load-bearing passages are at **498, 505, 506, 507, 509, 516**. The citation is now a page
citation and the WT-059 exposure is closed. *A null was not an absence, exactly as L24 says, and the
person who invoked L24 about his NAS broke it about his Kindles four messages later.*

**And a footnote that was nearly lost, chased down, and is Wicksteed's.** The 1933 text carries a
note at p. 512, hanging off Fig. 29, absent from the entire Econlib 1910 file: *"I have preserved
the convention by which the 'demand' curve is made to run down and the 'supply' curve to run up …
**Of course it has no significance and might just as well be neglected or reversed.**"* The
corollary at its most naked — the visual signature of the whole construction, disowned in a
footnote while drawing it.

It was quarantined on the reasoning that *a quote that would help us this much is the one to check
hardest*, and the check ran: the 1910 Macmillan printing (Cornell scan, archive.org
`cu31924030395606`) carries it at **leaf 538**, confirmed by two independent phrase searches each
returning exactly one match at the same leaf. **1910, and Wicksteed's, not Robbins'.** Cite as
**Bk II Ch. IV p. 512 n. 1**; the 1933 set preserves the 1910 pagination (Vol. II opens at p. 401).

**The transferable lesson is L24 in a costume nobody had seen.** The Econlib absence was worth
nothing, because Econlib renders figures as images and drops the apparatus around them — at that
exact point its text has a bare figure placeholder and runs on. *A null is not an absence* has now
bitten this project three ways in one session: a NAS that was not indexed, a Kindle that was not
charged, and **a transcription that was read too trustingly.** See L33.

**The method note worth keeping.** Three agents: one hunting priority, one told an over-eager
priority claim is as damaging as a missed one (L28), one told to **REFUTE the displacement** — to
defend this paper. *The defence attorney returned the displacement stronger than the prosecution
had*, and caught that the prosecution's own quotation had ellipsis-ed out the single most damaging
sentence in the book. **An adversary told to attack finds what it expects; an adversary told to
defend has to actually read.**

---

## WT-067 · The instrument built to rescue the re-scope returned NO VERDICT, and its guards could not fire

*wealthTensor-07. Registration `REG-001`; result `docs/preregistration/RESULT-REG-001.md`.*

The P3 re-scope is only worth anything if the identity does work somewhere Wicksteed cannot follow.
`REG-001` registered a port to an accounting-recognition layer to test exactly that — **committed and
pushed alone before a line of the instrument existed** (WT-052), with the falsifier stated in advance
and H1 declared insufficient in advance. `WT-066`/`wt066_p3_port.py` was then built and run.

**It returned no verdict, and the reason is four defects in the instrument, not a fact about layers.**

- **D1 · The port is layer-free.** Under *m* = −*τ*, *p* = −*s*, *H* = *B* it **is**
  `excess_demand.py` — verified pointwise on 399 grid points. Not one operation in it is
  recognition-specific. **Force-fit, not form-fit** (WT-042); ADR-001 §4 names the exact alarm, and
  it did not fire because the person who should have heard it wrote the thing.
- **D2 · The negative control is not a control.** `tie_break="index"` reads array position — a fixed
  per-item attribute identical across every labelling — not the labelling. Measured, it is
  indistinguishable from the treatment and in one regime *more* invariant than it.
- **D3 · H3 and H2b have empty failure sets.** H1 is an algebraic identity from a two-set partition;
  it has no failure mode, so its falsifier cannot falsify. "Magnitude varies" is probability 1 for
  continuous i.i.d. values under any mechanism.
- **D4 · Refuted by construction — and our own data already said so.** Conserve the label count (a
  market reallocation is a *permutation*; the port created and destroyed membership at unequal
  rates) and drive the trigger off the fold rather than off one half, and the registered expectation
  is met exactly. Our isolation run took H2a from 0/5 to 3/5 live regimes in exactly the predicted
  direction and **was written down as "REFUTED."**

**Priority, audited separately, is worse than the defects.** The general proposition is standard
equipment in four literatures: **Markov-chain lumpability (Kemeny & Snell 1960)** — state aggregation
exact for the measurement needs an extra rate condition for the dynamics, i.e. the claim as a theorem
sixty-six years ago; **Mori–Zwanzig** coarse-graining; **Granovetter (1978)** on threshold
populations, read in full; **Pesaran & Chudik (2014)**. Estimated ~0.85 an economic theorist and
~0.90 a physicist recognise it instantly. *"Expect a one-line referee report: 'this is
coarse-graining; see Zwanzig.'"* **Forni & Lippi (1997) remains unread and is named as the largest
live risk.**

**Disposition.** `REG-001`'s stopping rule stays fired; no second port. The repair is *known* to
succeed, which makes rebuilding worse, not better. **Paper I's P3 re-scope is neither supported nor
refuted, and its limitations section must say the generality is unexercised, in those words.**

### The two rules this produced

**WT-068 — a registration must state how to tell REPAIRING a mis-specified instrument from FITTING a
hypothesis.** `REG-001` §5 said "one instrument, no second port" to prevent fitting, and now locks in
a no-verdict from an instrument whose guards demonstrably cannot fire. Those are different acts and
the registration provides no test to separate them. Until a future registration carries one, the
conservative reading holds.

**WT-069 — a guard is not verified until a mutation that SHOULD kill it has been run and did.** The
`4/21 < 4/11` defect recurred **three times in this session**, twice inside artifacts written
specifically to prevent it: the first `wt066` run scored `H2a PASS` from a regime with zero events;
the negative control was built to catch label-smuggling and was label-blind; and the test written to
pin that defect was itself wrong twice — v1 asserted determinism, v2 compared `pressure_trace`, which
*is* the fold and therefore invariant by construction, so it compared two invariants with `!=`. Both
survived mutation. v3 reads event magnitudes and **is mutation-verified**: the mutant collapsing the
control into the treatment kills it. *An incomplete mutant is worse than none — the first mutation
attempt touched the booking branch and not the reversal branch, and the false green nearly shipped.*

**The one thing worth being pleased about.** WT-065 moved adversarial review to the moment a finding
is about to be **called** a result — ledger, paper, or Jason, whichever is first. Here the gap between
finding and disbelieving was **one tool call**. Nothing false reached the ledger, the papers, or
Jason. Under the old WT-054 rule this would have been caught at preprint time, four artifacts and one
conversation too late — which is precisely what happened in wealthTensor-06. **The rule that session
paid for has now earned its keep in the very next one.**

---

## WT-070 · Paper I's P3 re-scope died to its own referees, and so did its replacement · wealthTensor-08

**The at-bat was "write Paper I at the P3 level." No paper was written, and that is the result.**

**What was going to be claimed.** Excess demand is a fold over units; the two schedules are folds over
units *and the allocation H*, which is not a property of the population; so the Marshallian
decomposition manufactures two objects carrying information no fold contains. **P3 caught in the act
on the most canonical diagram in economics.**

**Three instruments, all committed and run, every guard mutation-tested (WT-069):**
`scripts/wt070_p3_fold.py` · `scripts/wt071_refuter.py` · `scripts/wt072_coupling.py`.
Full report: `docs/papers/paper-I-price-formation/RESULT-WT070-p3-is-dead.md`.

### The framing died three ways, each settled by running it

**1 · The crossing height IS the volume.** At a clearing price interior to the interval,
{*i* : *mᵢ* > *p*\*} is exactly *T*, so *D*(*p*\*) = |*T* \ *H*| and *S*(*p*\*) = |*H* \ *T*| = *V*,
and they are equal. Verified across 25 allocations. **The quantity coordinate of the Marshallian
cross is the allocation mismatch** — the one thing *z* cannot deliver. The diagram is not displaying
irrelevant information; it reads the population on one axis and the coupling on the other. *The
conclusion was upside down.*

**2 · The headline number was noise and the control was misspecified.** "26× the interval width" is
26.1× / 8.3× / 113.5× / 47.2× at *N* = 400 / 1,000 / 4,000 / 10,000 — a 13.6-fold non-monotone swing,
because the denominator is a single random order-statistic gap. And the honest control — raise a
RANDOM 250 agents by 20%, never naming *H* — gives spread 0.8934 / 21 intervals against the
*H*-indexed 0.9576 / 23. **The contrast was rank-scrambling versus rank-preserving. The allocation
contributed nothing.**

**3 · The load-bearing sentence is false in the formalism we were about to cite.** With the unit
(*mᵢ*, *hᵢ*), *D* and *S* are additive folds over units in exactly the sense *z* is. This is
Arrow–Debreu, Aumann (1964), Hildenbrand (1974) — and **Hildenbrand (1994) p. 36**, established the
same morning: the household characteristic is (income, demand function). *We would have cited the
source that refutes us.* Four rescue routes fail; the fifth — the Fréchet-class rearrangement group —
is natural rather than gerrymandered and **ratifies the prosecution**, its invariants being exactly
the marginals.

### And the exhibit was measuring a hypergeometric

The reported crossing-height range 85–103 across 25 uniform allocations sits inside the ±2 sd band
[84.4, 103.1] of a hypergeometric with mean *S*(*N*−*S*)/*N* = **93.75** and sd 4.69. **The quantity
the paper was about had never been varied.** *v0.1's "93 → 49" volume table inherits this: its
baseline 93 is S(N−S)/N to two significant figures and nobody noticed for two sessions.* Vary the
COUPLING instead — comonotone, antitone, block, alternating — and volume traverses **0 to 150** while
the clearing interval is bit-identical in every row.

### The replacement was checked and it died too

With a per-unit wedge *t*, the allocation stops cancelling and the residual is a sliding-window count
*W*(*p*) of locked-in holders. Across 25 couplings with identical population marginal: **1 distinct
*W* at *t* = 0, 25 at *t* = 0.01**, including two holder sets differing in one agent. *Identification
discontinuous at zero.* Verified. **And displaced twice over:**

- **the *t* = 0 invariance is stated in print, three times, in the indivisible setting, as an aside** —
  Azevedo, Weyl & White (2013, *TE*): *"We do not specify which agents initially own the endowment
  because, with quasilinear preferences and financially unconstrained agents, the initial allocation
  is moot"*; Gul, Pesendorfer & Zhang (2019); Baldwin, Jagadeesan, Klemperer & Teytelboym (*JPE*).
  Each uses it as a reason to omit endowments from the model primitives.
- **the identification lemma is the Titchmarsh convolution theorem (1926)**, and the finite-support
  restriction is unnecessary; the *shape* of the claim is **Bertanha, McCallum & Seegert (2023,
  *J. Econometrics*)** — *"a notch identifies the elasticity but a kink does not."* And it requires
  the entire excess-demand schedule over a continuum, which nobody observes: **it trades an
  observable for an unobservable.**

### Disposition

**Paper I is not written and is not re-scoped.** What survives is a subsection-sized expository
observation (the crossing height is the volume) and a large Abandoned Approaches entry. Folding into
**Paper IV** is recommended and is Jason's call under ADR-001; Paper III would be force-fit and the
WT-042 alarm was audible.

**Paper III is CLEAN, checked rather than assumed (WT-057).** Its P3 — *"measured aggregates are
folds over units; no aggregate is more fundamental than its constituents"*, domain *"any measurement
presented as a property of an economy rather than of a population"* — is a weaker claim aimed at the
aggregate production function and survives untouched. **Papers II and III cite Paper I zero times.**
ADR-001's containment firewall, designed 2026-08-05, held completely. **Third time "failure is
contained" has been cashed, and the first time the fire was in the room the policy named.**

### The rules this produced

**WT-070 — the defence attorney has now done the most damage twice, and it is doctrine, not a tip.**
Three agents ran. The prosecution found the framing false. **The defender found it false, supplied
the replacement, found that the prosecution's own best hit had the wrong mechanism, and found the
same hypergeometric defect in the one exhibit the prosecution left standing.** L28's second half is
promoted: *an adversary told to attack finds what it expects; an adversary told to defend has to
actually read.*

**WT-071 — a ratio whose denominator is a single order statistic is not a statistic.** The 26× was
reported because the number was large, and the number was large because a random gap happened to be
small. **Before quoting a ratio, vary N and check the denominator is not the thing doing the moving.**
Same family as L32, one level up: L32 says check the quantity you are reading is supposed to vary;
WT-071 says check the quantity you are *dividing by* is not.

**WT-072 — resampling is not varying.** Twenty-five uniform allocations look like twenty-five
experiments and are twenty-five draws from one distribution the population already fixes. **If the
object of study is a coupling, vary the coupling — comonotone, antitone, block — and never infer
range from a sample whose spread is its own sampling error.** *This is the `4/21 < 4/11` defect in
its fourth costume across three sessions. It recurs because it wears whatever the session is wearing.
The only thing that has ever caught it is running the control nobody asked for.*

**The pleasing part.** Briefed to write a paper, the session wrote three scripts, killed its own
thesis, killed the replacement, and wrote no paper — in one morning, for a few minutes of agent time,
with nothing false reaching the ledger, the papers or Jason. Wicksteed's chapter needed 116 years to
catch up with Paper I v0.1. **P3 · Atomism did not survive the morning it was born, and its
successor turned out to have been proved in 1926.** 🪃

---

## WT-073 · The phantom tag: the defect is renamed, mechanised and tested · wealthTensor-08

**Six instances across three sessions, and the lesson had been written down after every one.**
See `docs/METHOD-001-the-phantom-tag.md` for the full record; the six are tabulated there.

**Why writing it down kept failing.** It was named `the 4/21 < 4/11 defect` — **after its first
costume** — which is exactly why it was not recognised in its sixth. Renamed after its behaviour:
**THE PHANTOM TAG**, the fielder credited with an out he never made because his foot never touched
the bag. The umpire question translates without loss: *did the assertion touch a value that could
have been otherwise?*

**Why WT-069 was not enough.** WT-069 mutates the CODE. **All six instances survive every code
mutant**, because in every case the code was correct and the WORLD could not produce a falsifying
observation. The defect is upstream of the code.

**WT-073 — EVERY CHECK SHIPS A WITNESS.** `scripts/severity.py`. A witness is a callable returning
the condition evaluated in a world where the claim is FALSE, executed at check time. If the witness
also passes, the guard is a phantom tag and the run dies. One escape hatch, `DEFINITIONAL(reason)`,
which rejects reasons under 30 characters and reprints every use in the summary.

**This is Mayo severity applied one level below where this project had been applying it.** The
programme has used severity language for pre-registrations and never once for an assertion. All six
instances have severity zero. *(Jason invoked error-statistical philosophy for the corpus-level test
the same day — see ADR-001 addendum 6. The vocabulary was already in the building.)*

**THE PAYOFF THAT WAS NOT OBVIOUS.** For instances 5 and 6, constructing the witness does not merely
DETECT the defect — **it hands you the correct experiment.** *Show me a population-defined
perturbation giving more than one interval* IS the random-subset control. *Show me an allocation with
volume outside 85-103* IS the comonotone coupling. Both cost an adversarial agent and two hours in
-08; the witness rule produces them in ten minutes as a side effect of being unable to write the check.

**The harness is tested with the original defect.** `tests/test_severity.py` runs
`4/21 < 4/11 < 4/7 < 4/3` through it and requires it to die. **A harness against unverified guards
that had never been shown to catch one would be the defect wearing the costume of the cure.** Six
tests; suite now **121 passing**.

**And the unification worth keeping.** The phantom tag and the house style Jason ruled on the same
day are **the same pathology in two media** — prose that announces its rigour instead of
demonstrating it, and assertions that announce their severity instead of having it. Instance 3 shipped
with a docstring explaining why it was a good control, and it was not one. **A guard that needs a
paragraph explaining why it is a good guard probably is not one.**

**Status, honestly.** `wt070_p3_fold.py` fully retrofitted — 18 severe, 1 definitional, 0 vacuous,
with instance 5 preserved in place as `HISTORICAL PHANTOM TAG` and the witness that kills it attached,
so the repo holds the defect and its refutation in one executable file. **`wt071` and `wt072` are NOT
yet retrofitted** and that is recorded rather than quietly finished later. ⚾

---

## WT-074 · Paper III §9 was rewritten from the reading and died anyway, one page from the sentence it quotes · wealthTensor-09

**The at-bat was "rewrite §9 from `POSITIONING-001`." It was rewritten, and then it lost, inside the
hour, to its own adversarial pass.** Both drafts are in `git log -p`; the record of the second death
is `docs/papers/paper-III-dual-tensor/POSITIONING-002-second-pass.md`.

**The fact.** Jin & Myers, NBER WP 10453, pp. 4–5 — *before the model starts* — consider "an opaque
firm run by a **saintly manager** who always acts in shareholders' interest," and give three
possibilities for how the hidden news comes out. The third: *"think of good or bad news accumulating
within the firm until the difference between intrinsic value and share price reaches a critical value.
The news would then be released all at once, like a pressure vessel letting off steam."*

**Non-agency accumulate-to-threshold-then-release-at-once was published in 2004.** §9 had just
positioned this paper as *the non-agency generator of the same asymmetry*. Verified by the author
character-by-character with `pdftotext` and `grep` — **no model in the loop** — which is also how the
programme learned that the sentence it *does* quote sits one page later in the same PDF.
`POSITIONING-001` reached that paper by string search and asked it the wrong question.

**What survives, read forensically instead of defensively.** *Saintly ≠ ignorant*: "saintly"
qualifies capture, not information, and the next sentence says it is **investors** who "cannot see the
news as it happens." An informed party still holds the wedge; §4 has none. Their case is **two-sided**
("good or bad news," a threshold on a signed difference) and they assign it **kurtosis, not skew** —
then enter kurtosis as a **control variable** against which their agency crash results are identified.
**Jin & Myers' non-agency channel is the nuisance term they partial out.** And the working paper
contains zero occurrences of `goodwill`, `intangible`, `impair`, `GAAP`, `asset class`, `book value`,
`historical cost` or `historic cost` — all eight counted by the author.

**The larger casualty was not Jin & Myers.** **Bleck & Liu (2007, *JAR* 45(2))**, verified in full
text: historic cost *"stabilizes asset prices in the short term. Under the veil of this apparent
stability, volatility actually accumulates only to hit the market at a later date"* — transferring
volatility across time and raising it overall. **That is §4.4, nineteen years earlier, in prose.**
§4.4 now says so in place rather than at §9, because a reader meeting the table first should not have
to travel to learn that its headline is old. Their manager is strategic and fully informed; that is
the whole separation, and it is the same axis that survives Jin & Myers.

**The correction worth keeping, and it came from the defence attorney.** *§4's asymmetry is ASSUMED,
not DERIVED.* Jin & Myers obtain one-sidedness from symmetric primitives — absorption is bounded below
because capture is unbounded above. §4 assumes a one-signed physical layer, which is **not sufficient**:
degradation at a stochastic rate around a booked rate gives a two-signed reporting error, which is Jin
& Myers' case again. The wedge is one-signed only under a second condition — reported value may fall
and may not rise — and **that condition is conditional conservatism, i.e. Basu's object.**
`POSITIONING-001` had listed Basu as **Threat 1, to be scoped around.** He is not the threat. He is
the machinery the programme had not noticed it was standing on.

**One adversarial over-reach, struck on evidence the author ran himself.** The prosecution held that
Jin & Myers "predicted the failure of the registered prediction in 2004." PRE-001 registered an
ordering of **recognition lags across GAAP asset classes**; see the eight-way zero-hit count above.
Category error. *Agreeing with an adversary is as much a failure as agreeing with oneself, and this
programme was wrong in both directions inside one session.*

**Two quotation defects found in `POSITIONING-001` by the same mechanical method, corrected in place.**
The Andreou et al. quote read "nonsignificant" where the abstract reads **"non-significant"** — the
abstract uses both spellings in consecutive sentences, so the pipeline blended them. And the **27% is
the CRSP–Compustat–Execucomp universe; CRSP-wide is 23%** — a distinction the abstract does not make
and the body does. §9 was about to lead with the bare 27%.

**WT-070 held for the third consecutive session, and the defence attorney did the most damage again.**
It supplied the assumed-not-derived correction, identified Bleck & Liu where the prosecution had
buried it in a list, and caught the prosecution's over-reach. *The prosecution's prompt ended with a
paste marker and no pasted section — it never received §9's text, said so, and landed the fatal hit
from the two-line summary anyway. The lesson is not "check your prompts": it is that a hit available
from a summary was available to any referee who had opened the source at all.*

**Undischarged and recorded as such.** Four works reached this entry through agents and **not one is
in the paper**: Ryan (1995, *JAR*) — possibly closer prior art than Beaver & Ryan (2000); Kim & Zhang
(2016, *CAR*) — conditional conservatism *lowers* crash risk, which may already be §4.2's comparative
static, empirically supported; Kim, Wang & Zhang (2016, *CAR*); Zhu (2016, *RAST*).
`POSITIONING-002` §6 is the read-status table. **An adversarial agent is a retrieval pipeline in a
better suit.**

---

## WT-075 · A working copy cited as the article of record is the phantom tag in a third medium · wealthTensor-09

**Jason, unprompted, on being shown that the Jin & Myers quotations came from the NBER working paper:**
*"the Journal of Financial Economics were items I had read working copies on and I (wrongly) assumed
them to be the useful versions; 1993-era mistake, I didn't distinguish them."*

**The reference apparatus already had three passes and none of them catches this.** Bibliographic asks
*does this work exist with these details?* — and the article does. Provenance asks *is this the copy
that was read?* — and a working copy on the author's own disk **is** his own copy. Neither asks the
question that matters: **is the text I quoted the text of record?**

**Added: a fourth pass, `Version`, and a third mark, `✓⧗`.** Bibliographically verified, but the
*text* consulted is a pre-publication version; any quotation is attributed to the version read and may
not appear in the article of record. The entry is dual-dated in the opposite direction to the existing
rule — `consulted/published` rather than `original/consulted` — and the reference section states that
this is an extension rather than an instance. **Jin & Myers is now `(2004/2006)` with ✓⧗**, and §9
carries exactly one verbatim quotation from them because every verification obligation is paid per
quote.

**And the unification, which is the reason this is a ledger entry and not a style note.** The phantom
tag is a fielder credited with an out he never made, because his foot never touched the bag. A working
copy cited as the article of record is **a journal credited with words it never printed.** The house
style is prose credited with a rigour it never performed. *Three media, one animal: a claim collecting
credit for a contact it never made.* The 1993 habit and `4/21 < 4/11` are the same error in different
clothes, which is precisely why neither was recognised in the other's costume — see `METHOD-001` on
naming a defect after its behaviour rather than its first appearance.

---

## WT-076 · wt071 and wt072 retrofitted to the witness discipline, and building the witnesses corrected the script · wealthTensor-09

**`wt071_refuter.py` — 9 severe · 0 definitional · 0 vacuous. `wt072_coupling.py` — 10 severe ·
0 definitional · 0 vacuous.** Both mutation-tested per WT-069: one vacuous witness substituted into
each, both runs died with `PHANTOM TAG` as required, both reverted. Commit `fcb27a0`.

**`wt072` is the script that DIAGNOSED the phantom tag in D1**, and it was doing so while asserting
with a bare `check(label, condition)`. The fielder wrote the rulebook on touching the bag from several
feet off it.

**Building the witnesses corrected `wt071`'s own prose, which is the payoff WT-073 predicted.** The
C2(a) comment claimed the 26× ratio was *"dominated by the noise in its own denominator."* Measured
across N = 400/1,000/4,000/10,000: the **order-statistic gap swings 12.9×** and the **spread swings
4.6×**. The denominator moves more; it does not move alone. That was two claims wearing one assertion,
so it is now two checks — and the second one's witness is the **population standard deviation, which
swings 1.24×**, which is what makes the gap the culprit rather than the sweep. The conclusion — not an
effect size — survives both.

**A generalisation worth keeping, because the witnesses here were nearly free.** Both scripts' hardest
claims are **discontinuities**: unidentified at *t* = 0, exactly identified at every *t* > 0. **When a
claim has a sharp boundary, each side is the other's falsifying world and the witness writes itself.**
A claim that tells you where its edge is has already told you where to stand to watch it fail. The
corollary is the useful half: *a claim for which no witness suggests itself may be a claim with no
edge.*


---

## WT-088 · §4.4's inversion belongs to an assumption, and the registration that found it was wrong twice · wealthTensor-14

**`scripts/wt088_disclosed_ladder.py` — 14 severe · 0 definitional · 0 vacuous. Registered as
`REG-002` and pushed before a line of the instrument existed.** Three registered falsifiers fired,
one was **defective**, and one was **vacuous at the paper's own calibration**. All four are recorded
as found rather than repaired, which is the only version of this discipline worth its cost.

**The result.** §4.4 said *the ranking does not merely blur, it inverts.* Both figures behind that —
Kendall τ = −1 at the tabulated ladder, and 1.9% recovery over 4,000 random ladders — were computed
under **two** constraints imposed jointly: observability falls up the ladder (the design), and
durability rises up it (an inference from the standards' *scheduling* behaviour). Drop the second
and draw δ independently: **mean τ goes −0.414 → +0.318.** Not weakened. **Reversed.**

**So dispersion and ordering do different damage, and the paper had them fused.** δ dispersion is
what *destroys* the ranking — recovery falls from 100.0% at a common δ to 11.5% with no ordering at
all. The ordering is what turns the wreckage into a *reversal* — 23.8% exact reversal against 1.1%.
The inversion is what the confound does at one corner. Losing the ranking is what it does across the
region. §4.4 now claims the region and reports the corner.

**And the corner is a knife edge in its own top rung.** The deferral measures of goodwill and
indefinite-lived intangibles cross in closed form at **δ₃\* = Kα/(1 + K) = 0.00789**, an
eighty-seven-period half-life, verified against bisection to 1 × 10⁻⁹. The table assigns 0.002. Five
per cent above the crossing, τ moves from −1 to −0.67.

**Two ways of reading an absent schedule, both pushing the same way.** A class is left off an
amortisation schedule when its decline cannot be *scheduled* — a statement about predictability, not
speed. Driving a class at δ = 0.20 with probability 0.05 and zero otherwise — **identical mean rate**
— the realised deferral is **1.303×** the closed form at that mean (se 0.002, 2,000 paths), a
δ-equivalent of 0.0123, **above the crossing rate.** Measured, not argued from the convexity of
δ/(α − δ), because WT-080 exists.

**THE ERRATUM THAT IS THE REUSABLE PART. E1's falsifier was stated on |mean τ|.** An absolute value
**cannot distinguish an effect that vanished from one that changed sign.** The measured +0.318 sits
far outside the ±0.10 band, so the registered test *as literally written* returns "the inversion
survives" — the exact opposite of what the number says. The symmetric band **feels** conservative,
because it looks like it guards both directions; it is in fact the one shape that is blind to the
most interesting outcome a directional hypothesis has. **A falsifier on |x| cannot tell a dead
effect from a reversed one. State the signed quantity, or state two thresholds.** Banked globally.

**THE SECOND ERRATUM, AND IT IS THE BIGGER FINDING. E4's falsifier is a share of an empty set.** It
asks what fraction of the *admissible* disclosed-useful-life rectangle sees the first rung rise, and
at α = 0.05 **the admissible rectangle is empty**: R exists only for δ < α, and every useful life
short enough to appear in a filing implies a decay rate at or above the recognition rate. Not passed
and not failed — reporting "does not fire" would have been a phantom tag at section scale. **E6 was
registered as a boundary check on a corner of the parameter space. It is not a corner. It is where
the disclosed numbers all live.** Half the rectangle is admissible only at α ≈ 0.19, all of it above
α = 0.33. Re-asked at an α where the question has a domain, the first rung rises in **99.7%** of the
rectangle — labelled an EXTENSION of E4 everywhere it appears, never as E4.

**The generalisation, because this is the second registration in this project to break in this
family:** WT-052 was written about a check appended *after* the numbers arrive. This is the mirror
image — **a check specified so that no number can address it.** A registered falsifier can fail two
ways before it ever runs: it can be blind to an outcome (E1), or it can name a quantity that has no
domain (E4). Both are visible *at registration time* to anyone who asks the two questions: *which
outcomes does this threshold fail to separate?* and *is the set I am taking a share of guaranteed
non-empty?* Neither was asked. Both take a sentence.

**The statistic that survived does not survive this either.** §4.5's lag ordering holds in 100% of
400 ladders — drawn under the same two constraints. Unordered it is **66.2%** (M = 2,000, se 0.011),
3.55 se below the 0.70 threshold registered blind as E7. §4.5's concession is **narrowed, not
withdrawn**: lag is still the more robust statistic by a factor of six against the magnitude
measure's 11.5%. The registered figure at WT-083's own M = 400 came out at 69.0%, **0.43 se from the
threshold** — so the precision check was run on a *registered quantity* before either side was
preferred, and both figures are reported. A threshold landing within one standard error is not a
verdict; it is an instruction to buy more sample.

**A fitted design rule, which is the part somebody else can use.** Writing the design's *budget* as
the mean per-rung Δlog(1 − φ) and the ladder's *δ leverage* as the mean per-rung
|Δlog δ − Δlog(α − δ)|, the probability the design fails to recover its ordering is logistic in
log(leverage / budget) with slope **+1.58** (se 0.081, z = +19.5; the same fit on a permuted outcome
gives z = **0.23**), crossing one half at **0.61**. A φ-ordered cross-section reads what it ordered,
more likely than not, only while per-rung δ leverage stays under three fifths of the design budget.
The tabulated ladder sits at **2.58**. That is a number a reader can compute for their own design.

**Three tests that should have existed, and what the third one found.** §4.4 publishes two closed
forms and a domain restriction and none of them had a test. Writing the domain test surfaced
something the run had not: **convergence to the closed form slows without bound as δ → α.** At
δ = 0.045 the 400-period gap ratio is still 11% short of its own limit — which is why §4.3's
transient bound is quoted for the tabulated ladder and not near the pole. Past the pole the growth
rate is exactly log((1 − α)/(1 − δ)) per period, pinned at δ = 0.051 and 0.060 only: by δ = 0.100 the
ratio reaches 10⁹⁴ by period 4,000, and a longer check would be measuring float64's exponent range
rather than the model. **The test that is hard to write is the one that knows something.**

**And one reference narrowed before a referee could narrow it.** §4.2 attributed to Bellman and
Åström (1970) the statement that a compartmental system's rate constants are recovered only as an
unordered pair. Nothing readable in that paper supports putting it in their mouths — the source is
paywalled, its abstract and every secondary description cover the *definition* of structural
identifiability and the transfer-function criterion, and no citing source describes them treating
root exchange. The transfer-function definition **is** theirs; the pole-set consequence is now drawn
in this paper's own voice, where it can be checked. Same animal as the Kuan adjective (WT-084), one
costume over: **a source credited with a consequence of its method rather than with its method.**

---

## WT-089 · RESULT · 2026-08-16
**The corpus's II↔III join is vocabulary, and the fact that says so had been sitting in
`docs/REVIEW-004` for four days.**

`END-TO-END-001` leg `E1` — the first leg of the corpus's one and only end-to-end pass — asked
whether Paper II's realisation share ρ and Paper III's observability share φ are the same object
seen from two sides, as Paper II §3.2 asserted and Paper IV §3 built a chain on. **They are not.**
What Paper III's filter does not recognise is *deferred* — held in an unrecognised gap and released
at rate α, which is the whole of that paper's crisis result. What Paper II's base does not recognise
is *destroyed*: `recognised_flow[:] = 0.0` at every assessment, and Paper II has no parameter that
plays α's part. A lag and a loss share the adjective *"a measurement layer with a systematically
incomplete view"* and share nothing else. The leg FAILS at `E1a`, and by the design's own text a
simulation may not be run to rescue an equation between objects of different type.

**The remedy was pre-registered and is applied**: Paper II §3.2's "same structure" sentence is
withdrawn in the paper, and Paper IV §3's *"a chain rather than three analogies"* is demoted in
terms to *"three instances of one question, asked at three scales"*.

**The part worth re-reading in five years is where the fact came from.** `REVIEW-004` §E2, written
2026-08-12, states it: *"They are not the same structure … Non-arrival and deferred arrival are
different dynamical objects."* `REVIEW-004` §E3, same document, is titled *"What it would mean to
fail as a SYSTEM — the answer to your open question"* and ranks *"the conjunction is a coincidence
of vocabulary"* first, **already partly true**, with the diagnostic *"write the bridge proposition
between ρ and φ"* — which is E1, named four days before E1 was designed by a session that recorded
the question as having *"no written answer anywhere in this repository."* The answer was in a
document that session had read for other purposes and that nothing indexed as the answer.

**The transferable half.** `E1a` run against the three *manuscripts* returned "same kind" and would
have sent the leg to a simulation that reports REFUTED. `E1a` run against the two *implementations*
returned "different in kind" and ends the leg. The deciding fact — the fate of the unrecognised
remainder — is in neither paper's prose, because neither paper has a reason to state what its own
complement does. **A cross-paper type check is a check on code and not on text**, and this
repository now has one instance where the two answer differently and the difference is the result.

*(Same class as `WT-049` — a model parameter and a measurable that share a name may not share a
meaning — one level up: two model parameters in two papers that share a *sentence* may not share a
type. And the same class as `RESULT-TERM-002`'s costume: a finding correctly named in `docs/` and
never turned into an edit.)*

---

## WT-090 · METHOD · 2026-08-17 · wealthTensor-62
**A result document's defence of an un-preregisterable judgement is itself a checkable claim, and this one was false in both directions.**

`REG-013` measures the citation-graph whitespace with everything that *can* be pre-committed
pre-committed: seeds, controls, statistic, cap, thresholds, VOID rule. Exactly one thing cannot be,
and `RESULT-REG-013.md` §4.3 names it — *"Seed choice is a judgement."* The bullet then answers the
threat it has just named, by grounding the judgement outside the analyst: *"The seeds … **are the
works this corpus actually cites** — which makes them the right seeds for *this* claim (does the
work I am building on get read together?)."*

**One grep over four reference lists, and the grounding fails both ways.**

- **Five of nineteen target seeds are cited nowhere in Papers I–IV**: Ayres & Warr *The Economic
  Growth Engine* (2009), Kümmel *The Second Law of Economics* (2011), Godley "Seven unsustainable
  processes" (1999), Lavoie *Post-Keynesian Economics: New Foundations* (2014), Dos Santos
  "Keynesian theorising during hard times" (2005). By cluster: **K 6/6 · T 5/7 · S 3/6.**
- **And the corpus cites inside a seeded literature without seeding it**: Paper II carries
  Chakrabarti, Chakraborti, Chakravarty & Chatterjee (2013), *Econophysics of Income and Wealth
  Distributions* — kinetic exchange by its title and by three of cluster `K`'s own seed authors,
  and not a seed. (Paper III's Soddy 1926/1961 is a second, arguable, case.)

**It moves no number and may not.** `REG-013` §6 forbids re-choosing a seed list in response to
anything, this finding included; the verdict, the ceiling, the floor and the three *z* values stand
exactly as run. A dated correction note is appended to `RESULT-REG-013.md` rather than an edit made
to it — a result document is a record (`RESULT-…-E6.md` §7's precedent). No manuscript is touched:
the claim occurs at exactly one line in `docs/`, and Paper IV §6 does not repeat it.

***Why it is worth a ledger row anyway, and this is the transferable half.*** The corpus's audit
machinery is pointed at **claims about the world** — registrations, results, propositions, the
end-to-end pass. This is a claim about **the repository itself**, made in passing, inside a
threats-to-validity section, in the sentence whose whole job is to retire the one threat that
pre-registration cannot. **A defence is the least-audited sentence in a document, because it reads
as the place where the auditing already happened.** `wealthTensor-61` found the same shape one level
out: *a candidate produced by asking "what did I miss?" arrives with a gap's authority rather than a
claim's.* This is that again — a sentence arrives with a **defence's** authority rather than a
claim's, and gets less scrutiny for it, in the one section a referee reads most carefully.

*Cost to find: one grep, after two false starts that are themselves the lesson's fine print.* A
line-oriented grep for a multi-word title returns zero when the title wraps (`-61`'s `A rate is not
extensive`, in the opposite direction — here it would have manufactured absences rather than
fabrications), so the check ran with newlines normalised to spaces. And the first draft of the
correction asserted that the seed lists were at least a **superset** of the corpus's bibliography;
that sentence was written before it was checked, and checking it produced direction two. **The
finding got sharper because the write-up was verified against the bytes rather than shipped.**

*(Same class as `WT-089` — a fact correctly stated in `docs/` and indexed under nothing — inverted:
here the fact was correctly stated in `docs/` and indexed under *reassurance*, which is worse,
because a reader who finds it stops looking.)*
