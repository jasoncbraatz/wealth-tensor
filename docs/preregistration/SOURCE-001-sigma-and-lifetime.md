# SOURCE-001 · The σ-and-lifetime claim: what data would test it, and what selects the sample

*wealthTensor-23 · 2026-08-13 · the first move on `-22`'s at-bat item 1.*

**THIS IS NOT A REGISTRATION AND DOES NOT LICENSE A RUN.** No hypothesis is pre-committed
here and no falsifier is declared. A registration commits to a design *against a pinned
source*; the source was not pinned, and the reason item 1 has sat is that nobody had
established what the data actually contains. This document establishes half of that, by
measurement, and names precisely what is still unknown. `REG-009` gets written against
this, or against whatever this turns out to be wrong about.

---

## 1 · The claim that is untested

§4.7 establishes, **by simulation only**, that the strength with which φ is identified is a
property of the asset rather than of the analyst:

> Over a twelvefold range of return volatility both the design's collinearity and the
> standard error on φ̂ degrade as power laws in σ … Neither exponent is a constant of the
> model … What holds in all nine is the sign: identification always degrades as the asset
> quietens.

and, separately, that the panel cannot compensate — the standard error never attains the
root-T rate, because every term in the estimating equation is proportional to the asset's
remaining value, so **a decayed asset's later periods are absent observations rather than
noisy ones**.

Both statements are about the world and neither has met data. `RESULT-REG-003` §4 says so
in one sentence: *"§4.7's σ-and-lifetime claim remains untested: realised return volatility
and disclosed useful lives are not in this sample."* §7's ledger classifies both rows as
simulation, and `tests/test_restatement_reach.py` now holds them there.

## 2 · The admissibility test a candidate source must pass (the WT-038 guard)

WT-038 is a **type error**: a quantity that shares a name with a model primitive is
substituted for it. This project has paid for that error four times, and REG-003, REG-007
and REG-008 — the three registrations that touch filings — each carry an explicit
prohibition against proxying σ or asset lifetime. (REG-004, REG-005 and REG-006 do not, and
do not need to: a simulation has no proxy available to reach for. The prohibition is a rule
about *data*, which is exactly why it binds hardest here.) It is easy to state and hard to
apply, so state it as a test:

> **A candidate for σ is admissible only if it measures the volatility of news about the
> value of THE ASSET WHOSE RECOGNITION IS BEING TIMED.** Not the firm. Not the equity.

Equity return volatility fails this on three independent counts, any one of which is fatal:
it is levered (so it moves with capital structure, which is not in the model); it aggregates
every asset the firm holds (so for a multi-asset firm it is a weighted mixture in which the
asset under test may be a small term); and it prices growth options that correspond to no
recognised asset at all. The model's σ is the innovation volatility of a *single* asset's
economic value. Equity volatility shares its name and not its meaning. **That is WT-038, and
"we controlled for leverage" does not repair a type error.**

The same test applies to lifetime. The model's T is how long the asset goes on existing —
the horizon over which observations are generated. A **disclosed useful life** is a
different object: an accounting schedule, anchored by industry convention and by tax and
regulatory practice. §4.8 already argues the two coincide closely enough for δ to be read
off a disclosure; that argument is on the record and is not reopened here. It does mean
that if the useful life is used, the paper is using an *accounting* rate and must say so.

## 3 · The lifetime half: what `companyconcept` says — and why that answer is an artifact

> **SUPERSEDED IN ITS CONCLUSIONS BY §3a, `wealthTensor-24`, 2026-08-13.** The measurement
> below is reproducible and was not wrong; the inference drawn from it was. `companyconcept`
> does not serve duration-typed facts at all, so a zero from it is a statement about the
> **instrument**, not about the filers. §3a measures the same question on the surface §3's
> own final paragraph named as unchecked, and the answer reverses: **0.82 of this panel's
> 10-K filers tag `PropertyPlantAndEquipmentUsefulLife`.** Anything downstream that cites
> "the XBRL route is closed" — `-23`'s handoff, its commit messages, the banked lesson — is
> citing this section's error. §3 is kept rather than deleted because the shape of the
> mistake is the useful part.

The intuition was that useful lives, being mandated disclosures (ASC 360-10-50,
ASC 350-30-50), would be available as tagged XBRL facts and could be joined to the existing
panel cheaply. **That intuition was right. This section concluded it was false**, on the
evidence below.

Probed against `data/reg-006-wt092-panel.json` (1,602 firms), a deterministic every-k-th
sample of 40 firms per universe, one `data.sec.gov` `companyconcept` call per firm per
concept, 2026-08-13:

| what was asked | answer |
|---|---|
| firms reporting **any** useful-life concept | **3 of 80 — 0.037** (pilot 1/40, replication 2/40) |
| firms reporting `PropertyPlantAndEquipmentUsefulLife` | **0 of 80** |
| firms reporting `FiniteLivedIntangibleAssetUsefulLife` | **0 of 80** |
| what the three reporters use instead | `…UsefulLifeMinimum` / `…Maximum` — a **range**, not a point |
| units the same quantity arrives in | `Y`, `years`, `pure` — three strings for one dimension |

The canonical point-valued concepts resolve for nobody. `PropertyPlantAndEquipmentUsefulLife`
returned HTTP 404 on the frames API for every unit and period tried, and on
`companyconcept` for Target, Microsoft and Exxon individually — ~~it is not a sparsely-used
tag, it is one these filers do not use at all~~. **That last clause is the error, and it is
worth seeing exactly where it happened: a 404 was read as a fact about the filer. Target's
own 10-K for the very period tested tags the concept six times.** §3a shows the tags.

The three consequences drawn here, struck through, with what replaced each:

1. ~~**A tagged-XBRL join is not a route.** Not "expensive" — absent.~~ → **It is a route,
   and it is the cheap one.** §3a.
2. **Where a life IS tagged it is a range** — this one SURVIVES, and arrives stronger: §3a
   finds the range as an explicit `Range=Minimum` / `Range=Maximum` axis on 0.57 of the
   dimension sets, crossed with an asset-component axis. §4.4's "disclosed rectangle" is
   not a framing here; it is the literal shape of the data.
3. ~~**The route that remains is prose sentence-extraction**, the REG-007/REG-008
   machinery.~~ → **Available as a fallback, not needed as the route.** The structured facts
   are better typed than anything sentence-extraction could recover, and they do not need
   hand-auditing for *precision* — only for meaning.

**What this measurement does NOT establish, stated so it is not read as more than it is.**
The sample is every-k-th by CIK and is therefore not size-weighted; the panel includes small
and shell filers, who tag least, so 0.037 is a floor on large-filer coverage rather than an
estimate of it. And `companyconcept` may not expose every detail-tagged footnote fact: the
SEC's **Financial Statement and Notes Data Sets** are the fuller surface and were not
checked. Neither caveat touches the 0-of-80 on PP&E, which is a statement about a concept no
one used, but both must be closed before the XBRL route is called closed *in general*.

> **That final paragraph was right, and it was written by the same session that then ignored
> it.** The caveat named the exact surface that reverses the finding, in bold, and the
> section still declared the route closed in its own title. A caveat that does not gate the
> conclusion is decoration. §3a is that caveat, run.

## 3a · The correction: the route is OPEN, and it was open the whole time

`wealthTensor-24`, 2026-08-13. §6's step 1, run. Probe:
`scripts/source001_lifetime_coverage.py`, offline against the SEC's **Financial Statement
and Notes** data sets (`{2015,2019,2023}q1_notes.zip`), 10-K submissions only, joined to
`data/reg-006-wt092-panel.json` on CIK.

**Why §3's zero happened.** Useful lives are `xbrli:durationItemType` facts — the value is
`P39Y`, an ISO-8601 duration, not a number. `companyconcept` and `frames` serve **numeric**
facts, keyed by `units`; a duration-typed concept has no numeric unit and the endpoint
returns 404 for every filer, including filers that tag it. In the FSN data sets the same
split appears as two files, and it is the file nobody reaches for first: numeric facts go
to `num.tsv`, everything else to **`txt.tsv`**.

**The tell, which is the part that transfers.** The first FSN scan read `num.tsv` and
returned **11 filers of 4,711** — *worse* than the companyconcept figure it was meant to
beat — and the three `…UsefulLifeMinimum` reporters §3 did find were absent from it
entirely. **A coverage number that gets worse when the surface gets bigger is a statement
about the surface.** That contradiction is what sent the scan to `txt.tsv`.

| 10-K filers tagging … | 2015q1 | 2019q1 | 2023q1 |
|---|---|---|---|
| **any** useful-life concept, **our panel** | **419 / 500 = 0.838** | **342 / 399 = 0.857** | **493 / 562 = 0.877** |
| any useful-life concept, all filers | 3,647 / 4,683 = 0.779 | 3,248 / 3,886 = 0.836 | 3,658 / 4,711 = 0.776 |
| `PropertyPlantAndEquipmentUsefulLife`, our panel | — | — | **459 / 562 = 0.817** |
| `FiniteLivedIntangibleAssetUsefulLife`, our panel | — | — | **308 / 562 = 0.548** |

0.972 of the rows carry a standard `us-gaap/20NN` version — these are the mandated tags, not
company extensions. Coverage is flat across a decade, so the join's usable window is the
panel's whole span rather than its recent tail.

**PP&E — §3's "class with zero coverage" — is the best-covered class in the panel.** That
sentence is the whole correction.

**What a join actually gets: a rectangle, not a number.** Median **8** canonical life facts
per reporting panel firm (max 38), dimensioned. The axes, by frequency:
`Range` (3,617), `PropertyPlantAndEquipmentByType` (3,146),
`FiniteLivedIntangibleAssetsByMajorClass` (2,517), `BusinessAcquisition` (1,302).

Hand-audit, Target Corp (CIK 27419, `0000027419-23-000015`, FY ending 2023-01-31) — chosen
because it is one of the three firms §3 named as proof the concept was unused:

| component | minimum | maximum |
|---|---|---|
| Building and building improvements | P8Y | P39Y |
| Fixtures and equipment | P2Y | P15Y |
| Computer equipment | P2Y | P7Y |

Verified three ways, because a dataset agreeing with itself is one way: the FSN row says it;
**Target's own inline-XBRL 10-K carries `name="us-gaap:PropertyPlantAndEquipmentUsefulLife"
format="ixt-sec:duryear"` six times** (fetched from `Archives/edgar/`, independent of FSN);
and `companyconcept` for that same CIK and concept still returns 404 today. Tagged, present,
and invisible to the API §3 asked.

**What this does NOT establish.** Coverage is not accuracy: that a life is tagged says
nothing about whether the disclosed schedule is the *economic* life, and §2's warning stands
in full — a disclosed useful life remains an accounting rate, and using it means the paper
says so. It is also measured on Q1 filings, which favours December fiscal-year ends; a
firm-year join must confirm per-year coverage on the panel's own `fy_end` distribution
rather than inherit 0.82 from this table. And nothing here touches σ, which remains §4's
problem and the harder one.

## 4 · The σ half: not probed, and the harder one by a wide margin

Nothing here has been measured. What is known is the shape of the problem, and it is the
selection problem below rather than the acquisition of a price series.

Candidate families, with what each supplies and what each costs:

- **Firm equity returns** (free, universal, joins to the panel on CIK): supplies a σ that
  **fails §2's admissibility test.** Available and inadmissible is the worst combination
  available, because it is the one that gets used.
- **Asset classes with their own observable price series** — vessels, aircraft, oil and gas
  reserves against a published price deck, real estate against a property index: supplies a
  σ that *can* pass §2, because the series prices the asset rather than the firm.
- **A single-dominant-asset restriction on the existing panel** — firms where one class is
  overwhelmingly the balance sheet, so the equity series approximates one asset: supplies a
  σ that passes §2 only to the extent the restriction bites, and the extent is measurable
  rather than assumed. **Measured in §4a. It bites, and it bites asymmetrically.**

## 4a · The dominant-asset restriction, priced

§6's step 2, run on the same deterministic 80-firm sample as §3 so the numbers compare.
Each class share is `class / Assets` **on one balance sheet** — see the note below on why
that qualifier is the whole measurement. 74 of 80 firms have a class and total assets
reported at a common period end; 6 are unmatchable and dropped.

| one class ≥ this share of total assets | firms | of 74 | which class |
|---|---|---|---|
| 0.50 | 11 | 0.149 | PP&E 9, goodwill 2 |
| 0.60 | 9 | 0.122 | PP&E 7, goodwill 2 |
| **0.70** | **6** | **0.081** | **PP&E 5, goodwill 1** |
| 0.80 | 3 | 0.041 | **PP&E 3, goodwill 0** |

**The branch is alive, and it is alive for property only.** A restriction at 0.70 leaves
roughly eight per cent of the panel — on the full 1,602 firms that extrapolates to order
130, enough to run something — but the survivors are PP&E-dominant operators (restaurant
and retail chains: Kona Grill, Frisch's, Buffalo Wild Wings, Crumbs) and the
goodwill-dominant firms **disappear entirely by 0.80**.

> **THE COUNT SURVIVED THE FULL PANEL; THE COMPOSITION DID NOT. See §4b.** The
> extrapolation below is nearly right — 99 firms at 0.70, against "order 130" — and the
> sentence beside it, *"the branch is alive for property only"*, is wrong. A third class
> that is **identically zero in all 74 sampled firms** holds 34 of the 99, and goodwill,
> declared dead by 0.80, is not.

That is §5's argument arriving as a measurement rather than as a prediction. The
restriction that buys an admissible σ buys it exactly where the asset is tangible, priced
and long-lived, and it cannot be made to buy one for goodwill at any threshold, because a
firm that is mostly goodwill is not a firm whose equity series prices a single decaying
asset — it is a firm whose balance sheet is mostly the residual.

**So REG-009 can state its scope at registration instead of discovering it afterwards: a
dominant-asset design tests the σ claim on PROPERTY, and says so in its title.** The
extrapolation to ~130 is a proportion measured on 74 and should be confirmed by running the
count over the full panel before any power calculation leans on it.

**Why the one-balance-sheet qualifier is the measurement.** The first version of this probe
divided each concept's most recent 10-K value by the most recent `Assets`, taking each
independently. For firms that stop reporting different concepts in different years that
divides one balance sheet by another, and it returned shares of 93.4, 25.8 and 8.26. Those
announced themselves, being impossible; a share of 0.62 built the same way would not have.
It is §5.4's defect class — a figure from the wrong period is indistinguishable on the page
from one from the right period — committed by a throwaway script written the same session
as the guard against it. Period-matching changed the ≥0.70 count from 13 to 6.

## 4b · The same count on all 1,602 firms: the magnitude held, the composition inverted

`wealthTensor-24`. §6's step 2 finished — the arithmetic §4a said should be done "before
any power calculation leans on it". Same rule, same period-matching, same refusal, run by
`scripts/source001_concentration.py --full`; the 80-firm mode of that script reproduces
§4a's table exactly (74 matchable, 11 / 9 / 6 / 3), which is what licenses comparing them.
**1,444 of 1,602 firms matchable** (151 unmatchable, 7 refused as impossible).

| one class ≥ | firms | of 1,444 | PP&E | goodwill | intangibles | §4a's 74-firm reading |
|---|---|---|---|---|---|---|
| 0.50 | 255 | 0.177 | 92 | 107 | 56 | 11 — ppe 9, gw 2, **int 0** |
| 0.60 | 148 | 0.102 | 60 | 47 | 41 | 9 — ppe 7, gw 2, **int 0** |
| **0.70** | **99** | **0.069** | **47** | **18** | **34** | 6 — ppe 5, gw 1, **int 0** |
| 0.80 | 59 | 0.041 | 32 | 4 | 23 | 3 — ppe 3, gw 0, **int 0** |

**What survived.** The sample got the *size* of the surviving sample right, and that is the
number a power calculation needs: 0.069 against 0.081, 99 firms against an extrapolated
~130. REG-009 has a real denominator now, and it is large enough to run something.

**What did not.** §4a's headline — *"the branch is alive, and it is alive for property
only"* — is an artifact of 74 draws. Intangibles-dominant firms are **zero at every
threshold in the sample and 34 of the 99 survivors in the panel**, second only to PP&E,
and by 0.80 they are within striking distance of it (23 against 32). Goodwill, declared to
"disappear entirely by 0.80", has four survivors there and eighteen at 0.70.

**The failure mode has a name and it is not sampling error in the usual sense.** The count
is a proportion and proportions estimate well from 74 draws; the composition is a
multinomial over three classes whose rarest cell the sample never saw once. A zero cell in
a small sample is not a small number — **it is the absence of information**, and it reads
on the page as a finding. §4a wrote a scope ruling on that zero.

**Consequences for REG-009, replacing §4a's.**

1. **A dominant-asset design is not automatically a property design.** The scope sentence
   §4a offered for REG-009's title is not supported. If the design restricts to PP&E it
   must do so as a *choice*, argued from §2's admissibility test, not as a description of
   what the panel contains.
2. **Intangibles-dominant firms are a live third arm and nobody has looked at them.**
   Whether they *pass* §2 is a separate question and probably a harder one than PP&E —
   a firm that is mostly recognised intangibles is closer to the goodwill objection than
   to the vessel-and-aircraft case — but that argument now has to be made rather than
   assumed by absence.
3. **The 0.70 threshold no longer chooses itself.** It was picked where the sample still
   had survivors. On the panel, 0.80 keeps 59 firms and buys a much tighter restriction,
   which is exactly the trade §2 cares about.

**Refusals, since they are the guard reporting for duty.** Seven firms produced an
impossible class share and were excluded by name, the largest an intangibles share of
**704** — one balance sheet divided by another, loudly. That is the defect §4a's probe
shipped and this file's `IMPOSSIBLE` constant now refuses; at panel scale it fires seven
times, and at sample scale it fired once.

## 5 · The selection problem, which is the whole difficulty

**Observability of σ is correlated with σ and with T, and the correlation runs the wrong
way.** Assets that have their own price series are traded, standardised, long-lived and
capital-intensive — vessels, aircraft, reserves, buildings. That is a selection rule written
directly on the two regressors whose effect is being estimated.

And it selects *away from the finding*. §4.7's dangerous corner is a **quiet asset whose
book amortisation rate sits close to its true rate of decline** — small σ together with a
small rate gap. The asset that best fits that description in this programme is goodwill, and
goodwill has no observable price by construction: it is the residual that exists precisely
because it is not separately tradeable. So:

> **The region where σ is observable is close to disjoint from the region where the σ result
> bites.** A study run on the observable region can report an exponent, and that exponent
> will be estimated where identification was never in danger.

This is not a limitation to be disclosed in a paragraph at the end. It determines whether
the study is worth running, and a registration that does not confront it before stating a
hypothesis is registering the wrong hypothesis. Two shapes survive it, and both should be
priced before either is registered:

- **Estimate the exponent on the observable region and state its scope honestly** — a real
  result about vessels and reserves, explicitly not about goodwill, with the truncation
  named as the design rather than as a caveat. Cheap, small, and does not answer the
  question anyone is arguing about.
- **Make the truncation the instrument.** The claim has a *sign* prediction that holds in
  all nine simulated settings, and a sign survives truncation more robustly than an
  exponent does. A design that tests the sign across the observable range, and then asks
  what the truncation can and cannot do to it, is testing something the truncation does not
  automatically grant.

Nothing here chooses between them. That choice is REG-009's first section, and it is a
choice about design rather than about data.

## 6 · The next probe, named

In order, each cheap and each decisive:

1. ~~**Close the XBRL question properly.**~~ **DONE — §3a, and it did not narrow §3's
   conclusion, it reversed it.** Coverage on our own panel is 0.82 for PP&E lives, flat
   from 2015 to 2023, dimensioned by component × `Range`. The δ half of the σ-and-lifetime
   claim now has a source. This was the step the previous session called optional.
2. ~~**Measure the single-dominant-asset restriction on the existing panel.**~~ **DONE —
   §4a, and FINISHED in §4b.** The branch survives: 99 firms of 1,444 at a 0.70
   threshold. ~~The branch survives for property and is dead for goodwill at every
   threshold.~~ — that reading was the 74-firm sample's, and the panel contradicts it.
   The arithmetic this step called "what remains" changed the answer's shape.
3. **Only then, σ.** Whichever of §4's families survives ~~§4a~~ **§4b** gets one probe, and the probe
   reports coverage the way §3 does — a number against a denominator, on this project's own
   panel. §4a said which family to probe first — equity-return volatility for
   **PP&E-dominant firms only**, where the restriction is what makes it admissible under §2
   rather than a proxy in violation of it — and that remains the right *first* probe, but
   §4b removes the claim that it is the *only* one available. **47 PP&E-dominant firms at
   0.70, not 5.**

~~**Do not skip to step 3.**~~ **Both cheap steps are now run, and the instruction earned
its keep twice.** Step 2 turned "restrict to dominant-asset firms" from an option into a
scope statement REG-009 can put in its title. Step 1 — the one this document called
merely able to "narrow" §3 — reversed it outright. **Two for two on the steps that looked
like tidying.**

**The new step 4, which did not exist before §3a.** With a δ source in hand, the two halves
of §4.7's claim are no longer symmetric: **δ is now sourced and σ is not.** A design that
tests only the lifetime half is suddenly available, cheap, and does not depend on resolving
§5's selection problem at all — §5 is an argument about σ's observability, and it says
nothing about lives. REG-009's first section should price that split before assuming the
paired design.

---

*Written against `RESULT-REG-003` §4, `REG-008` §6, and paper III §§4.7–4.8. §3's probes
were throwaway scripts, which is part of why their conclusion outlived its evidence;
§3a's and §4a's are committed — `scripts/source001_lifetime_coverage.py` and
`scripts/source001_concentration.py` — and each carries, as code, the guard that the
corresponding mistake would have tripped.*
