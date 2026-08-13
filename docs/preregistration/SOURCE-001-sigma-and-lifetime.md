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

Equity return volatility fails this on three independent counts, any one of which is
fatal — **and only the second of the three is what the dominant-asset restriction
addresses; §4c measures the other two**:
it is levered (so it moves with capital structure, which is not in the model); it aggregates
every asset the firm holds (so for a multi-asset firm it is a weighted mixture in which the
asset under test may be a small term); and it prices growth options that correspond to no
recognised asset at all. The model's σ is the innovation volatility of a *single* asset's
economic value. Equity volatility shares its name and not its meaning. **That is WT-038, and
"we controlled for leverage" does not repair a type error.**

The same test applies to lifetime. The model's T is how long the asset goes on existing —
the horizon over which observations are generated. A **disclosed useful life** is a
different object: an accounting schedule, anchored by industry convention and by tax and
regulatory practice. §4.7 — **not §4.8, which is where this document sent readers until
`REG-009` §1.5 corrected it** — argues the two coincide closely enough for δ to be read off a
disclosure. That argument is on the record and is not reopened here, **but it does not travel
alone and this sentence used to let it.** §4.7 names its own weak joint in the same breath —
*a disclosed useful life is chosen by the same management whose timeliness is being
measured* — and bounds it with three claims (lives are anchored by industry convention, are
sticky within a firm, and can be run as industry medians) **each of which occurs exactly once
in this repository, in the sentence that declares it.** `REG-009` §1.3 carries that finding and
§2's P0 measures two of the three. It does mean that if the useful life is used, the paper is
using an *accounting* rate and must say so.

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

> **THE MIDDLE CAVEAT IS NOW RUN — §3b, `wealthTensor-25`.** It half-holds, and the half
> that fails is not the half it warned about. There is no December advantage in the 2023
> cycle (+0.003, z = 0.09), so 0.82 is not a December artifact *in the panel's recent
> years*. But the same probe on the 2014–15 cycle finds coverage of **0.727**, and the
> gap between the two cycles is carried almost entirely by non-December firm-years
> (+0.140, z = 4.07). §3a's own sentence — *"coverage is flat across a decade, so the
> join's usable window is the panel's whole span"* — is **true of the slice it measured
> and false of the panel**, which is this document's recurring mistake in its third
> costume.

## 3b · The caveat, run: no December bias now, a large one a decade ago

`wealthTensor-25`, 2026-08-13. §3a's outstanding caveat, and the precondition the handoff
put on designing the δ half. Probe: `scripts/source001_lifetime_by_fyend.py`, offline
against six FSN notes zips per cycle, unit of analysis the **firm-year**, denominator the
panel's own rows.

**Why the caveat could not be waved off.** A 10-K is filed 60–90 days after the year ends,
so a Q1 notes zip can only contain filers whose year ended in roughly the preceding
October–January. **40.8 per cent of this panel's 9,782 firm-years end in a month other than
December**, and about 31 per cent end in a month a Q1 zip cannot reach at all. §3a's 0.82
was not a biased estimate of those firm-years; it was silent about them.

**Design.** Six quarters per cycle, not four, so the twelve fiscal-year-end month ends in
the window each have their whole filing season inside the instrument. Coverage is
decomposed — *no 10-K found in the window* is reported separately from *10-K found, no life
tagged* — because only the second is a statement about tagging.

| | 2014-10-31 … 2015-09-30 | 2022-10-31 … 2023-09-30 |
|---|---|---|
| panel firm-years in window | 847 | 837 |
| 10-K located | 0.949 | 0.981 |
| **canonical life, December fy_end** | **0.758** (n=505) | **0.824** (n=540) |
| **canonical life, every other month** | **0.681** (n=342) | **0.822** (n=297) |
| December − other | **+0.077, z = +2.47** | **+0.003, z = +0.09** |
| all firm-years | 0.727 | 0.823 |

**The answer, in two parts, because it is two answers.**

1. **For the panel's recent years the caveat is closed.** December and non-December
   firm-years are covered at the same rate to within a tenth of a point. A join on the
   2023 cycle can use 0.82 for every month, and the fiscal-calendar worry that gated this
   step is not a live risk there.
2. **For the panel's early years it is closed the other way.** Coverage of the 2014–15
   cycle is 0.727, and the shortfall is concentrated in exactly the firm-years §3a could
   not see: non-December coverage rose **+0.140 (z = 4.07)** across the decade against
   December's +0.066. A design that inherits 0.82 across the panel's full 2013–2025 span
   **overstates early non-December coverage by about fourteen points.**

**So §3a's "flat across a decade" needs its scope written back on.** It is flat *on Q1
filers*, which is to say on December and January year-ends — and that is exactly the
population a Q1-only instrument can see. The series that moved is the one it could not.
This is §3's error and §4a's error in the same shape for the third time: **a property of
the measured slice, stated as a property of the panel.** The instrument was not wrong and
the number was not wrong; the quantifier was.

**An error this probe made in flight, kept because the tell is cheap and general.** The
first run used four quarters (2023q1–q4) rather than six, and reported that only **0.718**
of September year-ends had a locatable 10-K — a number that looks like delinquency and
would have gone into this table as one. A September 30 year end is due about December 29;
the late half of that filing season lands in **2024q1**, outside the window. Adding the
two edge quarters moved September to 0.923, August to 1.000, and October to 1.000, and
moved nothing in the interior. **A coverage rate that is low only at the ends of the
window is measuring the window.** The sibling of §3a's tell, and it cost ten minutes
because the same question — *could this instrument have seen a higher number?* — was asked
before the table was written rather than after.

**Two guards this probe carries as code**, following §3a's and §4a's precedent that the
mistake and its refusal ship together. `THIN` marks and refuses any month bucket under 30
firm-years (seven of twelve are refused in both cycles) — the direct descendant of §4b's
zero cell read as a finding. And every gap between two buckets is printed with a
two-proportion **z**, so a difference has to earn the word: it is what demotes the
December gap from "0.824 versus 0.822" to nothing, and what promotes the cross-cycle move
to a result.

**What this does NOT establish.** Two cycles are two points, and nothing here says the
non-December series rose smoothly rather than in a step — the intervening years were not
run, and a firm-year join that needs a per-year weight should run them (six zips and a
minute each). The window is one fiscal cycle per corner, so a firm that skips a year is
counted as uncovered in that year, correctly for a join and misleadingly as a statement
about the firm. And coverage is still not accuracy: §2's warning that a disclosed useful
life is an accounting rate is untouched by any of this.

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
  **AND IT BITES ON ONE COUNT OF THREE — §4c.** The restriction is aimed at aggregation;
  leverage and growth options survive every threshold. §4c measures the first (the
  PP&E arm is the most levered of the three classes, medians 0.113 against 0.641 and
  0.605), leaves the third unmeasured for want of a market-data source, and finds a
  fourth objection §2 never listed: 35 of the 99 survivors have total assets under
  \$1M.

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
   ~~which is exactly the trade §2 cares about.~~ **INVERTED BY §4c: it is not that
   trade.** Tightening the threshold buys concentration by trading real firms for
   shells — median total assets fall \$33.5M → \$12.0M → \$4.76M → \$1.28M across the
   four thresholds, and the sub-\$1M share rises 0.216 → 0.291 → 0.354 → **0.475**. At
   0.80 nearly half the survivors have a balance sheet smaller than a house.

**Refusals, since they are the guard reporting for duty.** Seven firms produced an
impossible class share and were excluded by name, the largest an intangibles share of
**704** — one balance sheet divided by another, loudly. That is the defect §4a's probe
shipped and this file's `IMPOSSIBLE` constant now refuses; at panel scale it fires seven
times, and at sample scale it fired once.

## 4c · The restriction against §2's OTHER two counts — and the size nobody read

`wealthTensor-26`, 2026-08-13. §6's step 5, and it does not get as far as σ, because the
step before it had not been taken. Probe: `scripts/source001_sigma_admissibility.py`,
run from the cloud against `data/source-001-concentration-full.json` and
`data.sec.gov`, per-firm records in `data/source-001-sigma-admissibility.json`. The
report regenerates offline from that artifact with `--from-json`.

**The gap, stated plainly.** §2 rejects equity return volatility on **three independent
counts, "any one of which is fatal"**: it is levered, it aggregates every asset the firm
holds, and it prices growth options corresponding to no recognised asset. §4's third
candidate family — the dominant-asset restriction — is aimed at the **second** count, and
§4a and §4b priced how hard it bites there. §6 step 3 then promotes the result to
*"equity-return volatility for PP&E-dominant firms only, where the restriction is what
makes it admissible under §2 rather than a proxy in violation of it."*

That is one count doing three counts' work. A restaurant chain that is 87 per cent PP&E
is still levered and still holds growth options; concentration of **assets** is silent
about capital structure and silent about what the equity prices beyond the balance sheet.
By §2's own arithmetic — any one is fatal — a restriction that clears one leaves two
standing. **`levered` and `growth options` appear exactly once each in this repository:
in the sentence that declares them fatal.** Nothing between there and §6 step 3 returns
to them. Running the volatility probe on the strength of that sentence would have
committed WT-038 with the restriction serving as the alibi.

### The count that was not in §2 at all: the denominator's size

A class share is a **ratio**, and a ratio is silent about how big its denominator is. The
cheapest way for one asset class to be four-fifths of a balance sheet is for there to be
almost no balance sheet.

| | firms | composition | median total assets | current registrant |
|---|---|---|---|---|
| **≥ 0.70, no floor** | **99** | ppe 47, gw 18, int 34 | **$4.76M** | 24 / 99 = 0.242 |
| ≥ 0.70, assets ≥ $1M | 64 | ppe 28, gw 17, int 19 | $21.0M | 18 / 64 = 0.281 |
| ≥ 0.70, assets ≥ $10M | 40 | ppe 19, gw 12, int 9 | $95.5M | 13 / 40 = 0.325 |
| ≥ 0.70, assets ≥ $100M | 18 *(THIN)* | ppe 10, gw 7, int 1 | $895M | 4 / 18 = 0.222 |

**35 of the 99 have total assets under one million dollars.** The smallest is a
PP&E-dominant filer with **$388** of total assets, of which about $283 is property. It
passes every guard §4a and §4b carry — the period match, the `IMPOSSIBLE` refusal — and
it is counted, correctly, as one of the 99 firms whose equity series is supposed to
approximate a single decaying asset.

**And the restriction is concentrating these filers, not inheriting them.** The panel's
matchable firms are 0.128 sub-$1M in the complement of the restriction and **0.354**
inside it — **z = +6.18** (sub-$10M: 0.236 against 0.596, **z = +7.86**). The mechanism
is not subtle and it is monotone in the threshold:

| threshold | firms | median total assets | under $1M |
|---|---|---|---|
| 0.50 | 255 | $33.5M | 0.216 |
| 0.60 | 148 | $12.0M | 0.291 |
| 0.70 | 99 | $4.76M | 0.354 |
| **0.80** | **59** | **$1.28M** | **0.475** |

So **§4b's third consequence inverts.** It reads: *"The 0.70 threshold no longer chooses
itself. On the panel, 0.80 keeps 59 firms and buys a much tighter restriction, which is
exactly the trade §2 cares about."* The tighter restriction is bought by trading real
firms for shells — at 0.80 nearly half the survivors have balance sheets under a million
dollars, and the median is $1.28M. Tightening the threshold makes the sample **less**
able to carry the design, not more. The trade §2 cares about is not the trade the
threshold makes.

`MATERIALITY_FLOORS` is now swept in the probe rather than assumed, because *which* floor
to use is REG-009's choice to defend; this document's job is only to price it. What the
price looks like: **§4b's 99 — the number a power calculation was to lean on — is 40 at
$10M and 18 at $100M.**

### Count 1, measured: the restriction and leverage pull in opposite directions

Book equity over assets, period-matched to the same balance sheet the class share came
off. Under the accounting identity E/A **is** the deleveraging factor E/(D+E), so
σ_asset ≈ σ_equity × E/A, and 1/(E/A) is the factor by which an equity vol overstates the
asset vol it is standing in for.

At the $10M floor, on the 40 firms that survive it:

| class | n | median E/A | IQR | E/A < 0.50 |
|---|---|---|---|---|
| **ppe** | 19 *(THIN)* | **0.113** | [−0.381, 0.545] | 14 / 19 |
| goodwill | 12 *(THIN)* | 0.641 | [0.344, 0.838] | 5 / 12 |
| intangibles | 9 *(THIN)* | 0.605 | [0.226, 0.822] | 3 / 9 |
| **ALL** | **40** | **0.384** | | |

The pooled median implies **σ_equity ≈ 2.6 × σ_asset**, and the multiplier is not a
constant to be divided out — the IQR spans firms where it is near 1 and firms where book
equity is negative and the ratio has no sign to speak of.

**The class-level reading, which is the part that bears on §6 step 3, and the reason it
is stated carefully.** All three class buckets are under `THIN`, so their *rates* are
refused. What survives refusal is the comparison itself: on the share below E/A 0.50,
ppe against intangibles gives **z = +2.04**, and the PP&E median of 0.113 against 0.605
and 0.641 is a gap no reasonable n makes disappear. **The class §6 step 3 named as the
right first probe is the most levered of the three, and mechanically so: property is
collateral, collateral supports debt, so PP&E-dominance and leverage are one phenomenon
observed twice.** The restriction buys count 2 by selecting exactly the firms that fail
count 1 hardest. That is not a coincidence to be controlled for; it is the same balance
sheet read from either side.

At **no floor** the same table reads ppe −0.476, intangibles −0.009, all-firms 0.052 —
true numbers about a population half of which is book-insolvent, and a demonstration of
why the floor has to be stated before the median is quoted.

### Count 3: not measured, and the reason recorded rather than elided

Growth options need **market** equity, and no market-data source was reachable from the
container this ran in. **That is a fact about the instrument and not about the firms** —
§3's error, and the one this document keeps meeting. It is recorded in the artifact as
`count3_measured: false` with its reason, so nothing downstream can read the silence as a
zero. What would close it: market capitalisation at each matched period end, hence
market-to-book, from a **delisted-inclusive** price source.

### Reach: whether the price series can be got at all

Two instruments, because one instrument agreeing with itself is one instrument.

| class | n | last fy_end ≤ 2019 | current registrant |
|---|---|---|---|
| **ppe** | 47 | **38 / 47 = 0.809** | **4 / 47 = 0.085** |
| goodwill | 18 *(THIN)* | 7 / 18 = 0.389 | 6 / 18 = 0.333 |
| intangibles | 34 | 16 / 34 = 0.471 | 14 / 34 = 0.412 |

The two agree without touching each other: current-registrant presence is **0 / 61** for
firms whose last panel balance sheet is 2019 or earlier and **23 / 32** for 2023 or
later. ppe against intangibles on the registrant rate is **z = −3.49**.

**What this does and does not say, because the difference is this document's whole
recurring subject.** `company_tickers.json` lists **current** registrants; a firm
delisted in 2016 is absent from it *by construction*. So 4 / 47 is **not** evidence that
no price series exists for those firms — that would be §3's 404 read as a fact about the
filer, in a new coat. What is established, by two independent instruments, is the
antecedent: **the PP&E-dominant arm is overwhelmingly composed of firms that stopped
filing years ago**, median last balance sheet **2016**. Their price histories, if wanted,
must come from a delisted-inclusive source, which is a cost this design has never been
quoted.

### Structural or terminal

A firm in wind-down writes off goodwill and sells inventory, and what is left is
property — so distress **mechanically** concentrates a balance sheet, and the dominance
that licenses the restriction may be an artifact of dying rather than a description of
the business. The class share is recomputed at every period end the filer reports and
compared with the share three years earlier.

Of the 47 PP&E-dominant firms, only **31** have a matched balance sheet three years
before their last; of those, **17 / 31 = 0.548** were already dominant then, with a
median rise of **+0.142**. So about half the arm's dominance is structural and about half
arrives late. **And the sample answering the question is itself selected**: the lag is
unobservable for the other 16 precisely *because* they are short-lived filers, which is
the same fact the reach table reports. This is a direction, not a rate, and it is
reported as one.

### What this changes

1. **§6 step 3's sentence does not survive.** The restriction makes equity volatility
   admissible on count 2 alone. Counts 1 and 3 are untouched by any threshold, count 1 is
   measured here and is **worse** for the PP&E arm than for either other class, and count
   3 has not been measured at all. A σ probe run on the 47 would produce a number, and
   §2's own test would reject it.
2. **§4b's "large enough to run something" needs its floor written on**, exactly as
   §3a's "flat across a decade" needed its slice. 99 is right. 99 *firms of the size a
   power calculation assumes* is 40 at $10M and 18 at $100M, and 4 of the 18 are
   currently listed.
3. **The intangibles arm's open question is answered without needing the argument.**
   §4b left it live and `-24` offered an untested read — that recognised intangibles sit
   nearer the goodwill objection than the vessel case. That argument may well be right
   and it is not needed: the arm is 34 firms with a **median size of $1.28M**, nine of
   which clear $10M and one of which clears $100M. Whether they pass §2 is downstream of
   whether there are enough of them to matter. *(A class claim from the n=1 cell at
   $100M would be §4b's own error a second time, and is not made here.)*
4. **The two families §4 named as passing §2 — assets with their own price series, and
   the dominant-asset restriction — are now one family.** The restriction does not
   deliver an admissible σ; it delivers a σ with one of three objections answered, on a
   sample that is small, levered, short-lived and, at the margin, trivial. §5's
   observable-region argument was about a *disjointness*; this is the same disjointness
   arriving as arithmetic on our own panel.

**What this does NOT establish.** Count 3 is unmeasured, so no claim is made about growth
options either way. Book leverage is not market leverage, and E/A at book understates
the deleveraging factor for a firm trading above book — the direction of that error
favours the design and is stated so it can be checked rather than assumed. Every
class-level bucket at the $10M floor is under `THIN` and its rates are refused; only the
pooled row and the between-class comparisons are reported. The materiality floors are
round numbers chosen to show the shape of the curve, not a recommendation: **the probe
prices the choice, it does not make it.** And nothing here touches δ, whose coverage
surface is measured and whose design §3b has already priced.

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
   0.70, not 5.** — **AND THE PROBE THIS STEP DESCRIBES IS NOT YET RUNNABLE: §4c.** The
   clause *"where the restriction is what makes it admissible under §2"* is one count
   doing three counts' work. §2 declared each of the three fatal on its own; the
   restriction addresses aggregation and nothing else.

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

**Step 4's own precondition — DONE, §3b.** The fiscal-calendar caveat is discharged and the
δ design may proceed on 0.82 **for the panel's recent years only**. What replaces it is a
narrower and more actionable constraint: coverage is 0.727 on the 2014–15 cycle against
0.823 on 2022–23, and the movement is almost entirely in non-December firm-years. So the
lifetime design has a **year-window decision** to make in its first section, alongside the
δ/σ split — restrict to the recent span where coverage is uniform, or carry the whole span
with a per-year, per-fiscal-calendar weight and say why. That is a design choice with a
measured price on it, which is the condition this document exists to produce.

~~**Step 5, and it is now the only cheap one left.**~~ **RUN — §4c, and it did not
reach σ, because the step before it had not been taken.** The 47 are the most levered
of the three classes, 38 of them stopped filing by 2019, and 35 of the 99 have total
assets under \$1M. The 34 intangibles-dominant firms are assessed — not by the §2
argument `-24` proposed, which §4c does not need, but by size: median total assets
\$1.28M, nine above \$10M, one above \$100M.

**Step 6, which is what replaces it, and it is a DESIGN step rather than a measurement.**
REG-009 §1 can now be written, and §4c hands it a priced δ/σ split rather than an open
one: δ has 0.82 coverage over thousands of firm-years with a known year-window cost
(§3b); σ has 40 firms at a \$10M floor, of which 13 are currently listed, before count 3
is even measured. The one measurement still worth buying is count 3 — market-to-book at
each matched period end, from a delisted-inclusive price source — and it is worth buying
only if REG-009 chooses σ anyway.

---

*Written against `RESULT-REG-003` §4, `REG-008` §6, and paper III §§4.7–4.8. §3's probes
were throwaway scripts, which is part of why their conclusion outlived its evidence;
§3a's, §4a's, §3b's and §4c's are committed — `scripts/source001_lifetime_coverage.py`,
`scripts/source001_concentration.py`, `scripts/source001_lifetime_by_fyend.py` and
`scripts/source001_sigma_admissibility.py` — and
each carries, as code, the guard that the corresponding mistake would have tripped.
Per-firm-year records for §3b's two cycles are in
`data/source-001-lifetime-by-fyend{,-2015}.json`, so both counts are auditable without
re-reading five gigabytes of zips.*
