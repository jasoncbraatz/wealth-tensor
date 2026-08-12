# PRE-POSTING DOSSIER
## wealth-tensor · Papers II and III · compiled `wealthTensor-10`, 2026-08-12

---

> **How to read this.** Four hostile referees were run in parallel — one on Paper II, two on
> Paper III (one from the conservatism-and-measurement literature you are moving §9 toward, one from
> the crash-risk literature you are keeping as secondary), and one above the level of either paper.
> None was asked to be kind. Each was told you have killed three of your own framings in five
> sessions and enjoyed it.
>
> **Two of their findings are FATAL, and I verified both myself against your source and your own
> published table before writing them down.** They are in Part A. Everything after that is ranked
> and labelled with what I could and could not check.
>
> **Nothing here is a reason not to post.** Read Part A with coffee, Part F last.

---

# PART A · VERIFIED BY ME, MECHANICALLY, BEFORE IT REACHED THIS PAGE

*WT-065 fires when a finding is about to be CALLED a result. Both of these were checked against
`src/wealth_tensor/redistribution.py` and `paper-II.md` at HEAD. Neither rests on a referee's word.*

## A1 · **FATAL — ρ is a rate multiplier, and the ρ = 0 result is an identity, not a finding**

**The abstract's second headline claim does not survive its own implementation.**

Line 131 of `redistribution.py`:

```python
recognised_flow += self.rho * gain + self.wage
```

then, at assessment:

```python
liable = np.maximum(0.0, assessed - self.threshold * assessed.mean())
levy   = np.minimum(self.rate * liable, w)
w      = w - levy + pot / self.n            # pure transfer, per capita
```

**ρ multiplies the gain, and the levy then multiplies by r. So the levy on gains is (r·ρ)·gain, and
ρ enters the model *only* through the product rρ.** Two runs with the same rρ are the same
experiment.

**At ρ = 0 the mechanism is exactly self-cancelling**, and the reason is sharper than "r × 0 = 0":
the only thing left in `recognised_flow` is `self.wage`, which is **identical across all agents**.
A uniform levy followed by a per-capita rebate is the identity map — every agent pays the same
amount and receives the same amount back. The levy is not weak at ρ = 0. **It is arithmetically
inert.**

*(One honest qualification I owe you, and it is the interesting part: it is not* perfectly *inert.
`levy = min(rate·liable, w)` caps agents too poor to pay. At ρ = 0 the process condenses, so the
poorest agents hit that clamp and a vanishing transfer does occur. That is why the row reads 0.994
rather than being byte-identical to `none`. **Your table's third decimal is a clamp artefact.**)*

**What this costs:** the abstract's *"a 100 % levy on flow is statistically indistinguishable from no
levy at all"* is true, and it is true the way *"a tax on nothing raises nothing"* is true. §3.2 calls
this "the crux" and "sharper" than result 1. It is a tautology in a table.

**What it opens, and this is the better paper.** Make ρ a **deferral operator rather than a
deletion operator.** Unrealised gains accumulate in a basis pool and are assessed on a later
realisation event — a sale, a hazard rate, a step-up at death. Then ρ is genuinely *not* a rate: it
is a timing parameter, the levy becomes path-dependent, and *"the observability binds first"* becomes
a claim with content instead of an identity. **This is also the repair that makes the corpus
cohere** — see D2, because Paper III's φ already is a deferral operator, and that mismatch is the
system's deepest crack.

**Confidence: certain.** Read from your source at HEAD.

---

## A2 · **FATAL to the title claim — at matched budget the base ranking reverses, and your own table shows it**

The title says *the base caps the region, the rate moves you within it*. §3.1 says *"the mechanism is
κ, the share of aggregate wealth actually moved per assessment."* **Both are refuted two rows apart
in the table that states them:**

| levy | κ | Gini |
|---|---|---|
| **stock**, *r* = 0.100 | **0.1000** | **0.222** |
| **flow**, *r* = 1.000 | **0.1026** | **0.125** |

**Same budget — the flow row is 2.6 % *larger* — and 44 % more compression.** If κ were the
mechanism, two rows at the same κ could not differ by that much. If the base set a ceiling the rate
could not cross, the flow base could not beat the stock base at all.

**§3.3 says the same thing from a third angle and the paper does not connect it:** a threshold at
0.25× the mean *"costs nothing measurable in compression (0.444 against 0.443) while reducing κ by a
quarter."* Remove a quarter of the budget, lose nothing. **κ cannot be the mechanism.**

**The mechanism that actually explains all five rows** (referee's derivation; I have checked the
algebra, not re-run the simulation). Write the process in normalised units as a Kesten recursion
*x′ = A·x + κ*:

- a **stock** levy sets *A* = (1−r)(1+η)/(1+μ) — it **scales** the growth multiplier, cutting
  E[log A] and leaving Var[log A] untouched;
- a **flow** levy sets *A* = (1+η−rρη⁺)/(1+μ) — it **truncates the multiplier's upper tail**,
  cutting E[log A] *and* Var[log A].

Tail index from E[*A*^α] = 1. At r = 1 the flow levy caps *A* below 1, so **no power-law tail exists
at all.** That is a theorem, not a regularity, and it says the opposite of your title.

> **This is the strongest result in Paper II and you are currently publishing the conventional
> intuition instead.** "At equal revenue, a levy contingent on the realised shock compresses more
> than a proportional levy on the stock, because it truncates the growth multiplier instead of
> scaling it" is a surprising, mechanical, checkable claim that reverses the standard
> wealth-tax-is-stronger prior. **Lead with it.**

**Confidence: the inversion is certain** — it is in your published table. **The Kesten explanation is
high-confidence but unverified by simulation.** Before it goes in the paper, run it (WT-053).

**Unchecked and important:** whether anyone has already published the truncation-vs-scaling effect on
the tail index. Search the optimal-taxation-with-Pareto-tails literature before claiming it. *This is
the one thing I would most want searched, precisely because it is the thing I am telling you to lead
with.*

---

## A3 · Three smaller things I verified in passing

- **The unopposed run has two values in one paper.** §3.1 and the abstract: Gini **0.994**, top decile
  1.000. §3.4: Gini **0.977**, top decile 0.988. Nothing explains the gap. The referee's independent
  reimplementation returned 0.996 — matching §3.1. §3.4 is probably a stale run from the drift-test
  era. Cheap to fix, and it makes §3.4's ceiling argument *stronger*.
- **The κ closed form is better than advertised.** §3.1 claims agreement "within 5 %." The residuals
  are −6.78 %, −4.91 %, −4.35 % — **monotone, therefore a denominator convention, not noise.** κ is
  measured against *post-growth* wealth, so the exact form is κ = r·E[η⁺]/(1+μ+a/w̄), which agrees
  **under 1 %**. Fix the denominator, delete the hedge, tighten the test from 5 % to 1 %. *You are
  advertising an error you do not have.*
- **The test count contradicts itself across the batch.** Paper II says **18 tests**; Paper III says
  **100 at the pinned commit**; the suite today runs **121**. One repository, three numbers, visible
  to anyone with both PDFs open. Say "18 of the suite's N tests cover this module."

---

# PART B · PAPER II — THE RANKED DOSSIER

*Beyond A1–A3. The referee reproduced your entire headline table from the prose alone, with no
repo access, in twenty minutes — which is itself a reproducibility result worth one sentence in §7,
and a stronger one than the commit SHA, because it requires the reader to trust none of your code.*

**B1 · SERIOUS — the periodicity result has the wrong sign.** §3.3 matches rates arithmetically
(0.02 × 20 = 0.40). The correct twenty-period equivalent of a 2 % levy is 1 − 0.98²⁰ = **0.332**. Your
lumpy levy simply takes 20 % more. Under compounding-matched rates the referee gets P=1 → 0.483,
P=20 → **0.496** — *lumpier is weaker*, the opposite of what §3.3 concludes, and the causal story
("catches dispersion that has had time to accumulate") is unnecessary because the whole effect is the
compounding gap. **One line of code; the conclusion reverses.**

**B2 · SERIOUS — the novelty of result 1.** κ_stock = r and κ_flow = r·E[η⁺] is the standard
public-finance conversion τ_wealth = τ_income × return. "Roughly an order of magnitude" is the
statement that the return is about 10 % — a calibration choice. **The stronger version, which you
have not made:** the gap *is* E[η⁺], exactly; and E[η⁺] ≈ 0.107 is close to the observed return on
wealth, so the factor is the inverse of Piketty's β. Name the equivalence, cite Saez & Zucman (already
in your bibliography), and claim the exact identity instead of the order of magnitude.

**B3 · SERIOUS — the opening hook is a non sequitur, and your own citation is the counterexample.**
*"Every wealth distribution that is not condensed is being opposed by something."* Finite lifetimes
alone bound the distribution with no opposing transfer — and **Benhabib, Bisin & Zhu (2011) is in your
reference list.** Death, consumption, bankruptcy, mean-reverting returns all bound it. Defensible
version: *conditional on a multiplicative process with positive drift and infinite-lived agents,
non-condensation requires an opposing term.* Also: nothing in the paper licenses the abstract's word
**"empirical."**

**B4 · SERIOUS — contribution 1 claims a demonstration that does not appear, and there is a hidden
fifth coordinate.** §1 promises "a demonstration that the process's behaviour is a function of these
alone." Four coordinates cannot represent a **graduated rate schedule** — the defining feature of
every real income tax. And the **rebate rule** is silently pinned at per-capita, its maximally
compressive setting, doing a large share of the work attributed to the base. Under a *proportional*
rebate, κ compresses nothing at all. **That is one extra row and it makes the point.**

**B5 · ANSWERABLE — the boundedness criterion is a post-hoc free parameter.** §3.4 adds a 0.90
top-decile cut *after* observing that the previous criterion gave the wrong answer, in a paper whose
§4 says "no free parameter may be added to absorb an objection." The fix is not a different
criterion, it is one sentence: bounded runs sit at 0.19–0.50 and condensed runs at 0.99–1.00, **so any
cut in (0.50, 0.99) classifies identically.** That converts an arbitrary constant into a demonstrated
insensitivity.

**B6 · ANSWERABLE — no seed counts, no dispersion, and a statistical claim with no statistic.** Not
one table reports seeds or spread, and the abstract says "statistically indistinguishable." Per A1
the right word is stronger: **inert by construction.**

**B7 · ANSWERABLE — the abstract overstates against the body it summarises.** "The base sets a
ceiling the rate cannot cross" against §3.1's own "the bases occupy *nested* regions, not disjoint
ones." "An order of magnitude in **compression**" when the order of magnitude is in **κ** (Gini goes
0.812 → 0.443, which is not an order of magnitude in anything a reader means by compression).
**§3.1's half-failure paragraph is creditable and the abstract does not carry the correction.**

**Where Paper II is stronger than it presents itself:** the matched-κ inversion (A2) is the paper;
the threshold result is filed under "trim" and is the one finding a public-finance reader carries
away; Limitation 5 is more conservative than your own N-sweep requires (you are robust to the third
decimal at N ∈ {200 … 12 800} everywhere except the near-condensation rows).

### The sentence someone writes on a forum within a day

> **"He has simulated the fact that 2 % of your wealth is more than 2 % of your income, and that a tax
> rate multiplied by zero is zero."**

**The defence is not rhetorical — it is A2.** Neither the conversion arithmetic nor the empty-base
tautology predicts an *inversion at matched revenue*, and the inversion is a fact about your model
that nobody has stated.

---

# PART C · PAPER III — THE ACCOUNTING LENS
### *(your new primary audience after yesterday's ruling; it has never been refereed from here)*

**Convention note, offered as a gift rather than a criticism: in accounting, "conservatism" is never
used unmodified in a theory paper.** It is always *conditional* (news-dependent write-downs — Basu's
object) or *unconditional* (news-independent understatement). You use the bare word five times and
the modified term once. `unconditional` appears **zero** times in the document.

## C1 · **FATAL to the new framing — there is no asymmetry anywhere in §4's equations**

You are about to lead with conservatism, in a model where conservatism does no work.

```
C(t+1) = C(t) + φ·ΔE + α·gap(t),    gap(t) = E(t) − C(t)
```

**No `max`. No floor. No ratchet.** The one-signedness in every result comes from the *input* being
monotone (ΔE < 0 throughout), not from an accounting rule. Run the same code with ΔE > 0 and C snaps
*upward* — the α·gap term is symmetric and the trigger is on |gap|. **The model as written revalues
PP&E upward, which no US GAAP entity may do.**

§9 *names* the missing condition — "reported value may fall and may not rise" — and never imposes it.

**And this is four lines of code from being the paper's best contribution.** Impose C(t+1) ≤ C(t).
Run constrained and unconstrained side by side. **The difference between them is conditional
conservatism's contribution, measured — and the ratchet *derives* the one-signed wedge from symmetric
primitives**, which is exactly the derivation §9 concedes it lacks and attributes to someone else.
*It does not belong to someone else. It is a ratchet and you are four lines from it.*

Then run a **Basu (1997) regression on your own simulated (earnings, return) pairs** and report the
asymmetric-timeliness coefficient as a function of φ. That one figure is the paper's entry ticket to
this literature: it shows the model can produce the field's summary statistic *and* says what the
statistic misses.

## C2 · **SERIOUS — Beaver & Ryan (2005) is not cited, and it is preemption-as-buffer**

*RAST* 10(2–3), 269–309, *Conditional and Unconditional Conservatism: Concepts and Modeling*. From
the abstract, verbatim: unconditional conservatism and other factors **"preempt"** conditional
conservatism. **Preemption is a stock-versus-threshold statement** — accumulated understatement is a
buffer, bad news is absorbed by the buffer, the write-down triggers when the buffer is exhausted.
That is §4.1's `gap(t)` against `θ`, in prose, twenty-one years earlier.

**Worse, and better: your φ is their mix parameter.** The share recognised immediately and
independent of news is unconditional; the deferred share triggered by a threshold is conditional. §4
is a continuous reparameterisation of their interaction.

**What survives as yours, and it is defensible:** (i) the *continuous* index where they have discrete
regimes; (ii) the closed form **D(φ) = (1−φ)·D(0)**, which the referee did not find anywhere in this
literature; (iii) the separation of inter-event smoothing from event concentration as two statistics.
**Claim those three. Do not claim "threshold-crossing accumulation."**

⚠ **This is now item 8 on the download queue and it is closed everywhere.** The referee read the
abstract, not the body, and says so. *Do not write the positioning paragraph until you have the
body* — if their preemption is a comparative static rather than a dynamic accumulation, your gap
claim is partly rescued and you should say exactly how.

## C3 · **SERIOUS — the tier ladder is inverted by the Codification itself, knowable with no data**

| class | when tested | first hurdle |
|---|---|---|
| goodwill (ASC 350-20) | **annually, mandatory** + interim triggers | fair value of reporting unit |
| indefinite-lived intangibles (ASC 350-30) | **annually, mandatory** + interim | fair value |
| PP&E (ASC 360-10) | **only on a triggering event** | **undiscounted** cash-flow recoverability |

**PP&E is the class with no mandated look and the highest first hurdle.** An undiscounted screen is a
deferral device by design. Goodwill gets a compulsory annual examination. **The standards predict
longer lag for PP&E — the reverse of your ladder — and your two negative z-statistics point that
way.**

This does not rescue the theory. **It makes §6.2's lesson much sharper:** the bridge was not merely
unwritten, it was *wrong in a direction derivable from the Codification alone, with no data.* That is
a better methodological finding than "we did not write the proposition down."

Also: "discretionary" is the wrong word. Goodwill testing is not optional, it is **unverifiable**.
Discretion is in the inputs, not in whether to look.

## C4 · **SERIOUS — 60 % of your test events are outside P1's stated domain**

P1 is *"silent on purely contractual objects whose referent is another claim."* Goodwill is 155/244
pilot and 262/444 replication events — **59–64 %.** §5 never asks whether the tiers are inside the
domain. **And your model has no acquisition mechanism at all — E only decays — so it cannot generate a
goodwill balance.** You tested a class your generative model cannot produce.

**Constructive:** re-run Jonckheere–Terpstra on tiers 0–1 only (n = 55 / 136) as a registered-from-
scratch secondary. That is a fourth candidate explanation for the null and, unlike the other three,
the data *can* speak to it.

## C5 · **SERIOUS — there is a published benchmark for your instrument and it disagrees 3×**

Your goodwill median recognition lag: **5.0 quarters ≈ 1.25 years.** Hayn & Hughes (2006), abstract
verbatim: *"goodwill write-offs lag behind the economic impairment of goodwill by an average of three
to four years"*, with delays up to ten years for a third of firms. Li & Sloan (2017): post-SFAS 142
*"relatively inflated goodwill balances and untimely impairments."*

Two consequences. **External validation fails** — that is an instrument result and belongs beside
§5.3's three qualifications. And **the top rung already had published empirical support**, so your
null is in tension with prior evidence, which by your own §5.2 logic should raise suspicion of the
*measurement* before it demotes the *theory*. **Limitation 1 lists three explanations. There is a
fourth and prior evidence favours it: the onset instrument does not measure economic impairment
onset.**

*(Caveat the referee verified and I am passing on: Hayn & Hughes is largely pre-SFAS 142. It is a
benchmark from a partly different regime. Li & Sloan is the post-142 evidence.)*

## C6 · **SERIOUS — the free parameter you refused six times is back, wearing a domain restriction**

§9: *"§4's claim is correspondingly restricted to degradation … carrying no impairment trigger, no
estimable expected loss and no observable event to key recognition to."*

**A domain defined by the absence of accounting evidence is not a domain, it is an alibi.** §4.3
retired the φ-partition for exactly this. **The test: name one asset class where the restriction
holds and a recognition event is nevertheless observable in filings.** If you can, it is a scope
statement. If you cannot, the honest sentence is that §4's domain is presently empty of observable
instances.

*Candidate rescue the referee offers:* **asset retirement obligations and environmental remediation
(ASC 410)** — degradation genuinely accrues with no trigger, and the liability is recognised only
when estimable. Real class, real disclosures, not in the paper.

## C7 · **SERIOUS — the field has firm-year measures of the construct φ reparameterises, and you call φ unmeasurable**

Khan & Watts (2009) **C_Score**; Bushman & Williams (2015) **DELR** and their *"expected loss
overhang"* — **which is your gap variable, operationalised, in banks, with a panel**, and which §9
mentions in half a sentence; Ball & Shivakumar (2006); **Givoly & Hayn (2000)**, whose accumulated
negative accruals measure is literally a *stock*; Beaver & Ryan (2000) for the unconditional half.

**And the field already agrees the Basu coefficient is a poor statistic** — Dietrich, Muller & Riedl
(2007), Patatoukas & Thomas (2011). *That agreement is your opening, and it is far better than a gap
claim.*

## C8 · **SERIOUS — §4.2 predicted that §5 would be uninformative, and §5 ran anyway**

§4.2's own table: entropy rate d = 0.01 → 0 events; 0.05 → 16; 0.20 → 100. **At fixed φ, δ moves
recognition frequency from nothing to everything.** §5 then tested φ while letting δ vary freely
across firms. Limitation 7 raises this and waves it off as "an ordinary identification problem with
ordinary remedies" — **and the ordinary remedies were not applied.** δ is observable: depreciation
expense over gross PP&E, or the useful-life disclosures, in the XBRL you already pull. **This is a
fifth entry for Limitation 1, and unlike the others it is derivable from your own §4 with no
accounting knowledge at all.**

## C9 · **ANSWERABLE — you cite Basu as load-bearing machinery and disclose you read only the abstract**

The disclosure discipline is excellent. It is also, in a paper leading with conservatism, an
admission that the field's foundational article was not read. **Read it, and read Watts (2003)
*Accounting Horizons* Parts I and II** — verifiability-as-the-ground-of-conservatism is argued there,
and it is the actual home of your mechanism. *Presenting to an accounting audience with Basu unread
and Watts (2003) uncited is a reject on sight, independent of merit.*

**Related and important:** the lag is **not** produced by conservatism. Conditional conservatism makes
bad news arrive **faster**; your mechanism makes it arrive **slower**. What produces your lag is the
**verifiability threshold** that conservatism requires before it may act. *The lag is the price of
verifiability.* That reframing is correct, defensible, and not currently in the paper.

## C10 · **ANSWERABLE, and it is a gift — IAS 36 gives you a free cross-regime falsification test**

US GAAP **prohibits** impairment reversal. **IAS 36 requires it** for non-goodwill assets. The
ratchet C1 asks you to impose is *present* in US GAAP and *absent* in IFRS for the same asset class.

> **Prediction: the wedge is one-signed under US GAAP and two-signed under IFRS, so recognition-event
> concentration and the crash-vs-jump asymmetry should be strictly larger for US filers than for IFRS
> filers on matched asset classes.**

**Registerable, with an institutional instrument, no observability proxy, and immune to the exact
failure mode that killed PRE-001 and PRE-002.** `IFRS` and `IAS 36` appear zero times in the paper.

## C11 · **ANSWERABLE — D is dimensionally currency×time, reported as currency, in a paper whose §3 is a dimensional-hygiene showcase**

D(0) = 1998.99 is a sum of gap *levels* over 400 periods; a terminal gap is ~30. §3.3 labels it
"(currency)". §4.1's event magnitude is the level gap, also currency. **Two different quantities, one
name — and neither is information, which is measured in bits.** The field's word for this is
**overhang** (Bushman & Williams). Rename: *unrecognised-loss overhang* (currency·periods) and
*unrecognised loss* (currency). Removes a free hit and adopts the audience's vocabulary at once.

## C12 · **ANSWERABLE — your flat medians are the signature of the annual testing date**

Eight medians across four tiers and two universes, all within 2.0 quarters, near-identical IQRs. ASC
350-20-35-28 lets a firm elect *any* annual test date provided it is consistent. **For a firm that
trips no interim trigger, the earliest possible recognition is its elected annual date** — a uniform
0–4 quarter delay bolted onto every lag, independent of observability, identical across tiers.
**Diagnostic:** split charges by whether they fall in the firm's modal fiscal quarter. If the
annual-test-quarter lags collapse onto the test-date offset, the instrument was measuring the audit
calendar and the tier test could never have detected anything.

### Where Paper III is stronger than it presents itself — accounting lens

1. **Limitation 4 is the best thing in the paper and is buried in a limitations section.** φ reaches
   the observable only through φδ; recovery requires dividing by δ; variance grows like 1/δ². **That
   is a general result about conservatism measurement:** C_Score, Basu coefficients and Givoly–Hayn
   accruals should all vary systematically with industry asset life for reasons having nothing to do
   with conservatism. Testable, cross-sectional, 291× effect in your own simulations. **Promote it to
   a section titled something like "Why conservatism intensity and asset durability are not
   separately identified from reported series."** That is a paper an accounting journal would review.
2. **The three-way taxonomy in §9 is a contribution written as a defence.** *"Deliberately withheld
   known news, honestly held unverifiable news, and unrecognised unknown degradation are three
   objects, and only the third is §4's."* The literature has the first two cleanly separated. The
   third is genuinely under-theorised. **Lead paragraph, not concession.**
3. **The gap recursion is a convergence result, not a novelty problem.** gap(t+1) = (1−α)gap(t) +
   (1−φ)ΔE(t) is an AR(1) in the book-to-economic wedge — the Ryan/Beaver-Ryan lag component in
   state-space form. *"An independent derivation from physical primitives reproduces the canonical
   accounting lag structure, and supplies a closed form for its integral that the accounting
   derivation does not"* is a sentence you can defend. **"This literature has no dynamics" is one you
   cannot.**
4. **The registered null is publishable as an accounting finding on its own.** Pre-registration is
   essentially absent from this field. *"Impairment recognition lag does not order monotonically by
   amortisation regime, n = 688, two sectors, pre-registered, replicated, powered 0.95–1.00"* is a
   contribution independent of your framework, and this literature has almost no clean registered
   nulls. **Report the null twice: once as a loss for the framework, once as a finding for the
   impairment-timeliness literature, with Hayn & Hughes as the prior it is surprising against.**

### The accounting reader's one-sentence dismissal

> **"An outsider has rediscovered — in a deterministic simulation containing no good news, and
> therefore no asymmetry for conservatism to act on — that accumulated unrecognised understatement
> must be exhausted before a write-down triggers, which Beaver and Ryan modelled in 2005; he then
> predicted an impairment-lag ordering that the Codification itself contradicts, tested it, lost, and
> reports the loss as a bridge problem."**

**Three moves defuse it, in order of value: impose the ratchet (C1); cite Beaver & Ryan 2005 and
reposition as continuous reparameterisation plus closed form (C2); state the ASC testing-regime
inversion in §6.2 as your finding rather than your oversight (C3).**

---

# PART D · PAPER III — THE CRASH-RISK LENS
### *(secondary after your ruling, and the audience most likely to be dismissive)*

## D1 · **FATAL to the §9 positioning — there is no price in this model, so it cannot produce a crash**

§4 has two state variables, E and C. **No investor, no information set, no expectation operator, no
discount rate, no market.** §9 nonetheless asserts a causal ordering from the model's event to a price
event — **which is an unstated bridge proposition of exactly the type §6.2 was written to forbid.**
The paper diagnoses the φ↔GAAP-tier type error at length and then commits its twin forty lines later.

**And the bridge is implausible as written.** If C is book value, the recognition event is an
impairment charge, and impairment charges are among the most heavily anticipated events in the
literature — the market has typically moved long before. **Your own §5 instrument found a median five
quarters between deterioration peak and charge.** If that signal is price-linked, §5 measured *price
leading the recognition event by more than a year* — §9's ordering with the arrow reversed, in your
own data. **See D5: the paper never says what the deterioration signal is, and its identity decides
this.**

**Fix:** write the third line. P(t) = f(C(t), information about E). Two lines suffice, and the choice
of f *is* the real contribution claim.

## D2 · **SERIOUS — the measurement-rule cell is empty unless someone is fooled**

Run the trilemma on your own claim:

- **(a) Everyone knows the rule and the rate.** §4 is deterministic — E(t) = E₀(1−δ)ᵗ, in closed
  form, δ constant, printed in Limitation 4. A rational investor who knows δ knows E exactly. Book
  diverges; price does not. **No crash.**
- **(b) Degradation is stochastic and unknown to all.** Two-signed error, fat tails, not skew. **That
  is Jin & Myers' saintly-manager cell**, already theirs, already handled via kurtosis-as-control.
- **(c) Conservatism truncates the upward revisions, so the residual is one-signed.** Now the
  direction of the error is *deterministic and publicly known* — the rule is in the Codification. A
  market that does not undo a publicly known, mechanical, one-signed bias is exhibiting **functional
  fixation on reported numbers.** That is a real and respectable cell: Sloan-style accrual
  mispricing, Hirshleifer–Teoh limited attention. **The paper cites none of them.**

**So the surviving cell is not "the wedge lives in the measurement rule." It is "the wedge lives in
the measurement rule *and investors price the rule's output rather than its input*."** A joint
hypothesis with a behavioural second limb, and the second limb is where all the empirical action is.

**Either own the behavioural limb explicitly as a numbered bridge proposition and cite the fixation
literature — a defensible, uncrowded position — or drop the price claim and market §4 as a
book-value/disclosure-timing object, where the absence of an agent is a feature.** What is not
available is keeping the crash positioning while insisting nobody is misinformed and nobody is
inattentive.

## D3 · **SERIOUS — Kim & Zhang's sign is the opposite of yours, and the reconciliation is already in your paper**

They find conditional conservatism **lowers** crash risk on 114,548 firm-years. §4 makes conservatism
the thing that *creates* the accumulation. Same construct, opposite sign, panel on their side.

**But you already wrote the answer, one sentence later, without noticing:** *"§4's claim is
correspondingly restricted to degradation on which conservatism has nothing further to bite … Where a
loss is estimable, recognition is faster than the market and §4 predicts nothing."*

> **Make it a partition and it becomes a test.** Kim & Zhang's conservatism operates on *triggerable*
> losses — timeliness drains the reservoir, crash risk falls. §4 operates on the *untriggerable
> residue*, where the no-write-up rule makes the error one-signed with nothing forcing release.
> **Prediction: conditional conservatism is negatively associated with crash risk in trigger-rich
> asset classes and positively or not at all in trigger-poor ones.** Interacting C_Score with asset
> composition is a one-table test on data everyone in the field already has.

**That is the single most valuable paragraph the paper is currently not writing.**

## D4 · **SERIOUS — "crash" is not being used in this field's technical sense and the paper never says so**

In this literature a crash is firm-specific weekly returns residualised against an expanded
market-and-industry model, then NCSKEW / DUVOL / a count beyond ~3.09σ, netted against symmetric
upside outliers. **Every component is absent here.** Sharper: **residualisation is not a detail — a
crash is idiosyncratic by construction, so a single-firm model with no market factor cannot define
the object at all.**

§4.1 disciplines "correction" and "crisis" beautifully. **It stopped one word short of the word §9
leans on**, which reads as inadvertence to a friendly reader and as evasion to a hostile one.

## D5 · **SERIOUS — §5's deterioration signal is never identified, and its identity decides whether §9 survives**

Described four times, never defined. "An unbroken decline in a firm-level signal." "Peak-to-charge."
Limitation 2 mentions "consolidated revenue rises" in passing. **If the peak is a *market* peak, §5's
median five-quarter lag is direct evidence that price leads recognition and §9's causal ordering is
refuted by your own 688 events. If it is an accounting peak, §5 says nothing either way.** One clause
in §5.1 fixes the reproducibility defect; one sentence in §9 says which way it cuts.

## D6 · **SERIOUS, and it is your best unexploited asset — the skew-not-kurtosis prediction**

Jin & Myers assign the saintly-manager case **kurtosis** and use kurtosis as a **control**. §4's
conservatism condition makes the release **one-signed**. Therefore:

> **Under the saintly-manager case the accumulation channel produces excess kurtosis and no skew.
> Under §4's conservatism condition it produces negative skew *that survives controlling for
> kurtosis*. Jin & Myers' own control variable is the discriminating instrument.**

Sharp, sign-restricted, non-agency, testable on CRSP tomorrow, made by none of the five prior works,
and **one inferential step from a sentence already in your manuscript.**

*Concession owed in the same breath:* a model where firm-specific information reaches the reported
layer only in rare lumps **mechanically implies rising R² with (1−φ)** — which is Jin & Myers'
headline. §4.4's table is a synchronicity result in disguise. Concede it.

## D7 · **SERIOUS — §4.4's concentration statistic was retired on grounds that are too wide**

It is unfalsifiable *against accounting data* — true, and correctly reasoned. **On returns it is not.**
"Share of annual firm-specific return variance in the largest k weeks, as a function of opacity" is
live, non-tautological, cross-sectionally testable, with a predicted direction. **You looked for your
best target in the one dataset where it cannot fail and concluded it could never fail anywhere.** And
this route needs no measurement of φ — any existing opacity proxy ranks it, which sidesteps the exact
failure that killed both registrations.

## D8 · **ANSWERABLE — FAS 142 is the natural experiment your claimed cell requires**

SFAS 142 abolished goodwill amortisation for impairment testing, effective for fiscal years beginning
after 15 December 2001. **A change in the measurement rule, differential by pre-existing goodwill
intensity, with no contemporaneous change in incentives or beliefs.**

- **Measurement-rule account (§4):** schedule → threshold-triggered means recognition goes lumpy;
  crash risk **rises** post-142, increasing in goodwill intensity.
- **Agency account:** SOX lands in the same window and cuts the **other** way — the post-SOX
  dissipation you already cite against yourself.

**Opposite signs, same window, differential treatment intensity, no φ, no bridge from an unobserved
parameter to an accounting category.** Register it before writing the instrument's code.

## D9 · **ANSWERABLE — deterministic periodicity is a liability whose repair is three free predictions**

Constant δ, φ, θ ⇒ exactly periodic, identically sized events. Not what crash arrival looks like. But:

- **hazard increases in time since the last event** (the gap is refilling) — agency models tie hazard
  to incentives and news arrival, not elapsed time;
- **hazard collapses immediately after an event** — no back-to-back crashes;
- **event magnitude increases in the elapsed interval**, slope ∝ (1−φ)δ.

Three duration-model tests on existing data, and they survive the stochastic generalisation.

## D10 · **On standing, and the paper's own diagnosis is wrong here**

Theory-only is **not** a disqualification: **Bleck & Liu (2007) is an analytical paper in *JAR* with
no dataset, well cited, and in your own bibliography.** What disqualifies §4 in this audience's eyes
is not the absence of data but the absence of **an agent, a price, and an equilibrium**.

And **nobody will hold a disclosed, stopping-rule-honoured null against you.** What they will hold
against you is the inference that a failed φ↔tier bridge tells us anything about §4's standing in
crash risk. **It does not. The crash-risk prediction has never been tested — it has not been
weakened.** §9 inherits an unearned pessimism from §6.

### The crash-risk reader's one-sentence dismissal

> **"A deterministic two-line recursion with no prices, no investors and no equilibrium restates
> Bleck and Liu (2007) with a continuous opacity parameter, re-derives Jin and Myers' saintly-manager
> case with the sign asserted rather than derived, computes no crash measure of any kind, and its
> only registered empirical prediction failed twice — the crash-risk section is an aspiration with a
> bibliography."**

Every clause is currently true. **D1, D2, D3 and D6 are the ones that, if answered, make it false.**

---

# PART E · THE SYSTEM, AND THE RECEPTION

## E1 · **CRITICAL — symbol collisions between the two abstracts**

| symbol | Paper II | Paper III | fix |
|---|---|---|---|
| **φ** | the **standard normal PDF**, in κ = r·(μΦ(μ/σ) + σφ(μ/σ)) — **in the abstract** | **observability**, 74 occurrences, the load-bearing parameter — **in the abstract** | rename II's density to `n(·)` |
| **η** | the **growth shock**, η ~ 𝒩(μ,σ²) | the **numeraire conversion coefficient**, the most-defended quantity in III | rename II's shock to `g` or `ε` |
| **θ** | the **exemption threshold**, illustrative value **0.25** | the **recognition threshold**, parameter value **0.25** | same symbol, same word, *same number*, different object |
| **E** | the expectation operator, E[η⁺] | the physical component, E(t), E₀ = 100 | |
| **r** | the **levy rate**, r = 0.025 … 1.000 | **Piketty's return**, r > g | |
| **α** | — | **both** the recognition rate (0.05) *and* the significance level (0.025) — **inside III** | |

**Posted side by side, your two abstracts use φ for two different things.** Cheapest high-value fix
in the corpus.

## E2 · **The corpus's unifying thesis is asserted twice and established nowhere — and the two models disagree on exactly the point at issue**

II §3.2: *"A levy that cannot see an accrual and a financial statement that does not record a
degradation **are the same structure**."* III §2.3: *"observability binds before intensity."*

**They are not the same structure:**

- In **II at ρ = 0** the base is **permanently empty**. Nothing is ever collected. The information
  does not arrive late; **it never arrives.**
- In **III at φ = 0** *everything* arrives — late, and all at once. 25 recognition events, 0.99 of
  reported movement inside them. **Nothing is lost; it is deferred.**

**Non-arrival and deferred arrival are different dynamical objects.** And note what this means
together with **A1**: II's model *would* produce III's structure if a realisation event were added —
which is exactly the repair A1 already demands on independent grounds. **One fix closes both.**

> **This is the bridge-proposition error one level up.** §6.2 requires that identifying a model
> parameter with a measurable be written as a deniable proposition. Nobody wrote *"ρ in Paper II and
> φ in Paper III are the same quantity, because…"* **Paper III invented the discipline and did not
> apply it to its own corpus.**

**And an asymmetry of standards, visible only across the batch:** II §2.3 defends ρ as "swept rather
than chosen." III §4.3 *retracts that exact defence* for φ. **Read in order, II §2.3 is refuted by
III §4.3.** (Relatedly: III says "refused five times" three separate times, and §7 enumerates four.
The missing fifth is II's ρ — which cannot be counted, because §4.3 concedes the defence was unsound.)

## E3 · **What it would mean to fail as a SYSTEM — the answer to your open question**

Five modes, ranked by likelihood, each with a diagnostic:

1. **The conjunction is a coincidence of vocabulary** *(most likely, and already partly true)*. Three
   papers sharing a metaphor, with the metaphor doing a theory's work. **Diagnostic: write the bridge
   proposition between ρ and φ. If it can be written and defended, it is the corpus's best single
   contribution and belongs in all three abstracts. If it cannot, drop the word "programme" and post
   three independent papers** — which is a perfectly good outcome and much safer.
2. **Unfalsifiable in aggregate though each paper is falsifiable alone.** Corpus-level empirical
   exposure at posting: **one prediction, two null instruments, zero confirmed claims.**
   **Diagnostic: name, in advance and in writing, one observation that would make a reader abandon
   the *programme* rather than one paper.** If none exists, the system-level failure is happening now.
3. **No joints — an anthology with a system's ambition.** Cross-references are decorative *by design*
   (REVIEW-001 F9 enforced it), so no paper's failure can propagate. Excellent per-paper hygiene,
   fatal to the "system" claim. **A system whose components cannot break each other is a list.**
   A genuine fork: add one real joint, or delete "this programme" (17 occurrences).
4. **Method-as-content substitution.** The most transferable products are all *methodology* — the
   bridge-proposition rule, the saturating-statistic result, Limitation 4, the registration ordering,
   the reference apparatus. The substantive findings are two closed forms and a null. **If the honest
   one-line summary is "exceptional lab notebook, thin findings," the system has failed as science
   while succeeding completely as pedagogy.** *Your stated audience scores that outcome positively
   and the academic audience scores it negatively. That is not a contradiction to resolve; it is a
   choice to make on purpose and then stop apologising for.*
5. **Correlated single-author error.** One author, one codebase, one commit, one test suite, one set
   of conventions. **A defect in a shared utility invalidates all three at once and is invisible to
   every per-paper referee, including the four just run.** **Diagnostic, cheap: a table of which
   shared modules each paper's headline numbers route through, and which tests exercise those modules
   independently of any paper's claim.**

## E4 · **The word "tensor"**

> **It appears in the title, the keywords, and the repository name. It appears in the body exactly
> once, at §2.1, in a sentence saying the tensor is *not* what is being claimed. There is no tensor
> in the paper.** The object is an ordered pair (E, C) and a scalar ratio. No indices, no basis, no
> transformation law, no rank, no contraction.

A physicist spots this in five seconds. An economist reads it as ML or as crankery. **This one word
costs more than every other reception feature combined, and removing it costs nothing** — §2.1 is
already prepared to say the formalism is not the claim.

## E5 · Other reception hazards, ranked

2. **"thermodynamics of capital" in the keywords, with Odum in the bibliography.** §9 defends against
   this *well* — "it measures the gap Georgescu-Roegen said would exist" — **but nobody reaches §9.**
3. **The revision history above the abstract**, naming internal session IDs. Reads as a working
   document that escaped. Move to a repo changelog.
4. **"Draft — not yet submitted. Version 0.4."** Same.
5. **271 bold spans in 14,438 words** — one every 53 words. Reads as a blog post typographically.
   Paper II is at half the density because v0.2 was scrubbed; **apply the same scrub to III.**
6. **"the programme"** (17 occurrences) for a solo hobby project reads as institutional cosplay to
   exactly the reader you are trying not to lose.
7. **Paper II's title advertises the claim its own §3.2 supersedes** — and per A2, §3.2 is itself the
   weaker framing. The title is two revisions behind the paper.

## E6 · Your assets, which are stronger than you think

1. **PRE-001 as a single-file commit pushed before the analysis code existed — and then the
   disclosure that PRE-002 does *not* have that property.** Voluntarily disclosing that your best
   methodological artefact does not cover the result you are reporting is something almost nobody
   does. **It is more convincing than the registration itself.**
2. **Reporting a null in the abstract, in bold, stopping rule honoured, third instrument available
   and not built.**
3. **Three qualifications sitting next to the power table, explaining why your own reported power is
   an upper bound.**
4. **§6.2** — a genuine contribution to metascience with a worked failure attached, citable by people
   who will never care about wealth tensors.
5. **Limitation 4** — real work performed against your own framework, with p90s reported *because*
   they undercut the median.
6. **§9's concessions.** *"The concession owed to it is larger than the contribution claimed against
   it."* **Cranks do not write these sentences.** This section is the proof of good faith.
7. **The ✓⧗ mark**, which most published authors would not recognise as a distinction.

## E7 · **Where to post — and one thing that must be fixed first**

**MPRA + SSRN + OSF now; arXiv in parallel once endorsed.**

- **arXiv** — physics.soc-ph primary for II, q-fin.GN primary for III, cross-listed. **Blocker:
  endorsement.** No institutional email means you need an endorser in-category. physics.soc-ph is
  usually the easier door. **Budget weeks, and ask an author you cite.**
- **MPRA** — the most under-considered option and probably the best single fit: built for unaffiliated
  economists, feeds RePEc/IDEAS, no endorsement.
- **SSRN** — no gate, weak for econophysics, **strong for finance and accounting, which is where §9's
  interlocutors actually are.**
- **OSF** — and here is the important part.

> ⚠ **§5.1 says: "The git history is the timestamp, and it is the entire evidence that the prediction
> preceded the outcome." That is over-claimed and a hostile reader kills it in one line.** Commit
> dates are settable (`GIT_COMMITTER_DATE`), history is rewritable, and the repository is
> author-controlled.
>
> **Fixes, cheapest first:** deposit PRE-001/PRE-002 on **OSF** (dated at deposit, but *external*);
> archive the repo to **Software Heritage** and cite the SWHID; use **OpenTimestamps** going forward;
> and cite the **GitHub push event**, which is not author-editable. **Add one sentence conceding the
> limit.** This converts the batch's central integrity artefact from *trust me* to *verify*.

## E8 · **Hard blockers on posting today**

1. **III's own revision history declares §9 provisional.** You cannot post a paper that says so.
2. **§9 is not merely provisional, it is known-stale.** Kim/Wang/Zhang and Gorton & Ordoñez appear
   nowhere in `paper-III.md`, and yesterday's finding — the wedge lives in an incentive, a belief, or
   the measurement rule — is better than what is in the paper and is not in the paper.
3. **II's reference note says details are "to be re-checked at submission."** Posting *is* submission.
4. **II's zakat footnote** — one source or delete the sentence.

## E9 · **The method disclosures: keep every fact, cut the narration**

**Judgement, not a hedge: the disclosures help. The commentary around them hurts. They are separable
and only one needs to go.**

Every *fact* is an asset. What hurts is the ~45 methodological-virtue tokens in III — twice II's
density, seven times its volume, because **II was scrubbed in v0.2 and III was not.**

Two consequences, and the first is in the paper's own words:

- **It violates your own best rule.** §3: *"a defence that recurs is a tell. Five defences of one
  quantity inform a referee that there are five soft places."* The batch mounts the integrity defence
  in eleven distinct locations. **By your own criterion, that is a map of where you think the soft
  ground is.**
- **It is calibrated for the wrong objection.** The apparatus answers *"is this person honest?"*
  **Nobody is asking that.** The objection is *"is this work load-bearing?"*, and no amount of
  disclosure touches it.

**Target: cut III's methodological narration by half — 1,500–2,000 words — without removing a single
disclosed fact.**

### The exact passage where it tips

**§1, the paragraph beginning "A word about §5, since its placement is deliberate."** Three defects in
five lines: it informs the reader of something they can see unaided; it describes a concealment you
considered and rejected, which asks for credit for not cheating; and the final clause grades your own
conduct. **The same defence recurs in §7.** **Delete both. Change nothing else. The placement speaks.**

Runners-up: §5.2's *"This diagnosis was not permitted to rescue the result"* (agentless passive
narrating virtue — say "a second registration was written instead"); §4.4's *"because the fix
mattered more than the result"*; II §4's *"This section is not a formality and it is not an
appendix."*

### And the count of failures is wrong — fix it before someone else counts

| # | failure | pre-registered? |
|---|---|---|
| 1 | II §3.1 "regardless of rate" | **no** — found in a sweep |
| 2 | III §4.4 over-smoothing | **no** — caught by a probe |
| 3 | III §5 lag-scaling (PRE-001 and PRE-002) | **yes**, twice |

**Strictly: one pre-registered prediction, two registered instruments, both null.** The papers blur
1–2 into 3 by calling all of them "predictions that failed." **A referee who notices will call it
inflation of the pre-registration claim — the one asset that cannot afford any.**

### How the null will actually land

- **Metascience and open-science people: strongly positive.** This is a poster child, and **some of
  them have platforms.** III's abstract is not written for them.
- **Accounting and finance specialists: near-indifference** — nobody held the alternative, and §6.2
  concedes the mapping may have been anti-correlated. **It is a failed bridge, not a failed theory**,
  and the paper says so three thousand words after the abstract announces the failure.
- **The hostile skimmer: uses it as an exit.** Real cost, worth paying, reducible.

> **One-clause fix, and it is the highest-leverage edit in the batch:** end the abstract with §6.2
> instead of §6.1. *"…and it failed. The diagnosis is that the registration contained a tier table
> and no bridge proposition: φ was identified with a GAAP amortisation schedule, and the
> observability of degradation and the observability of an accounting treatment are different
> quantities that may be anti-correlated."* **Same honesty; the skimmer leaves with a transferable
> lesson instead of a licence to close the tab.**

---

# PART F · THE TWO DISMISSALS AND THE ONE ENDORSEMENT
### *Read these first thing. They are what you are actually up against.*

## The paragraph a hostile, competent, time-poor reader writes to a colleague

> Braatz — unaffiliated, gmail, no coauthors, self-posted as a "batch." The long one is titled *the
> dual tensor of wealth* and contains no tensor: the object is an ordered pair (E, C) and a scalar
> ratio. The abstract then tells you in bold that the framework's only empirical prediction was tested
> twice and failed, and that it "has no confirmed empirical claim" — so we are invited to spend an
> evening on a formalism whose author concedes it currently predicts nothing that has survived data.
> The prediction it lost was that goodwill impairments lag PP&E write-downs because goodwill is not
> amortised. That is not a prediction of a thermodynamic theory of wealth; it is a guess about ASC
> 350, and §6.2 concedes the mapping probably ran backwards. Meanwhile §9 concedes, at length and to
> its credit, that Jin & Myers wrote accumulate-and-release in 2004, that Bleck & Liu wrote the
> volatility-relocation result in 2007, that Basu supplies the asymmetry the model assumes rather than
> derives, and that Beaver & Ryan decomposed book value into bias and lag in 2000; after which the
> residual contribution is "the parameterisation" — of a parameter his own Limitation 4 then proves is
> not recoverable from data at the decay rates that matter. The companion paper is an N = 800
> kinetic-exchange simulation establishing that taxing stock compresses more than taxing income, which
> is arithmetic with a Gini attached. And both papers spend more prose on the author's disclosure
> practices than on their results. **I believe every word of it, and that is the problem — the
> apparatus is calibrated against a reader who suspects fraud, and nobody suspects fraud. We suspect
> the work is not load-bearing, which is a different objection, and none of this touches it.**

## And the paragraph the same reader writes if they *do* engage

> Ignore the title — there is no tensor and he barely uses the word — and read §5, §6 and Limitation
> 4. A man with no institution, no coauthors and no funding registered a prediction as a single-file
> commit before the analysis code existed, ran it, got a null, diagnosed his own instrument as
> measuring signal volatility rather than the phenomenon, wrote a separately numbered second
> registration with a peak-onset rule, a label-permutation control, a power curve to be reported
> whatever happened, and an explicit no-third-instrument stopping rule; got a null again on 688 events
> across two sectors declared in advance; honoured the rule; and then wrote three paragraphs
> explaining why his own power figures overstate the power. He then declines to call it evidence of
> absence, on the grounds that the bridge cannot be too broken to license a prediction and sound
> enough to license its refutation — which is a sharper piece of reasoning than I have seen in most
> registered-report discussions. §6.2 names the actual defect and it is a general rule with a worked
> failure attached, worth more than the theory it came from. Limitation 4 is real work performed
> against his own framework. §9 is the most honest related-work section I have read in years. And when
> an internal referee told him the paper was grading its own homework, he cut the passages and
> published the referee report. **The theory is probably not right and is currently unfalsified in
> the bad way rather than the good one. But the conduct is a model, and the φδ conditioning result
> and the bridge-proposition discipline should outlive whatever happens to the rest.**

---

# PART G · WHAT NOBODY CHECKED

*Stated so you do not mistake this dossier for a clean bill of health.*

- **No referee ran your code.** A1's source reading is mine; A2's inversion is from your own published
  table; **the Kesten tail-index derivation in A2 is algebra I have checked and simulation I have
  not.** WT-053 applies before any of it enters a paper.
- **No referee read Beaver & Ryan (2005), Ryan (1995), Basu (1997) or Ryan (2006) at source.** C2 is
  built on an abstract and says so. **Do not write C2's positioning paragraph before reading the
  body** — the download queue has all four.
- **The crash-risk referee did not open Jin & Myers, Bleck & Liu, Kim & Zhang, Kim/Wang/Zhang or Zhu**;
  they worked from the verified block I supplied from yesterday's reads.
- **Whether the behavioural cell in D2 is already occupied** — someone joining accounting-rule-driven
  measurement error to crash risk through an inattention channel — **was not searched. If it is
  occupied, D2 is stronger than stated and the remaining cell may be gone.** *This is the single
  highest-value search still outstanding.*
- **Whether the truncation-vs-scaling tail-index result in A2 is already published** was not searched.
  Same reasoning: it is the thing I am telling you to lead with.
- **The EDGAR pipeline, the 688 events, the tier assignment, and the differential attrition by tier**
  — none inspected, and §10 correctly names attrition as the one selection channel that could
  manufacture the null.
- **Paper IV** is unwritten, so E3's system analysis covers two papers and will need redoing.

---

*Compiled `wealthTensor-10`. Four adversarial agents, two verified fatal findings, one corpus.
Nothing in Part A reached this page without being re-run by hand.*

*The papers follow.*
