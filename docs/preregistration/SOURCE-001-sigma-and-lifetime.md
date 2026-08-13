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

## 3 · The lifetime half: MEASURED, and the machine-readable route is closed

The intuition was that useful lives, being mandated disclosures (ASC 360-10-50,
ASC 350-30-50), would be available as tagged XBRL facts and could be joined to the existing
panel cheaply. **That is false on this project's own universes, and the failure is not
marginal.**

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
`companyconcept` for Target, Microsoft and Exxon individually — it is not a sparsely-used
tag, it is one these filers do not use at all. **The class with zero coverage is PP&E, which
is this project's tier 0, in the universe (retail) where tier 0 carries the most weight.**

Three consequences, and the third is the useful one:

1. **A tagged-XBRL join is not a route.** Not "expensive" — absent.
2. **Where a life IS tagged it is a range**, which matches §4.4's "disclosed rectangle"
   framing and means a design must take an interval, not a number, as its primitive.
3. **The route that remains is the one this project is already good at.** Useful lives are
   disclosed *in the accounting-policy footnote, as prose* ("three to seven years"), and
   REG-007 and REG-008 built exactly this machinery: locate a sentence in a filing, require
   named structure inside it, hand-audit the precision. The δ half is a sentence-extraction
   problem of a shape already registered, run and audited twice — **not new infrastructure.**

**What this measurement does NOT establish, stated so it is not read as more than it is.**
The sample is every-k-th by CIK and is therefore not size-weighted; the panel includes small
and shell filers, who tag least, so 0.037 is a floor on large-filer coverage rather than an
estimate of it. And `companyconcept` may not expose every detail-tagged footnote fact: the
SEC's **Financial Statement and Notes Data Sets** are the fuller surface and were not
checked. Neither caveat touches the 0-of-80 on PP&E, which is a statement about a concept no
one used, but both must be closed before the XBRL route is called closed *in general*.

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
  rather than assumed.

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

1. **Close the XBRL question properly.** Check the Financial Statement and **Notes** Data
   Sets for the same concepts. If footnote detail tags are materially better covered there,
   §3's conclusion narrows to "not via `companyconcept`" and the join may be back.
2. **Measure the single-dominant-asset restriction on the existing panel.** For each firm,
   the largest asset class as a share of total assets, from data already crawled. This is
   an offline count and it prices option three in §4 without any new source: if the
   restriction leaves twenty firms, that option is dead and the registration is simpler.
3. **Only then, σ.** Whichever of §4's families survives step 2 gets one probe, and the
   probe reports coverage the way §3 does — a number against a denominator, on this
   project's own panel.

**Do not skip to step 3.** Steps 1 and 2 are offline or nearly so, and either can close a
branch that would otherwise cost a session to open.

---

*Written against `RESULT-REG-003` §4, `REG-008` §6, and paper III §§4.7–4.8. The probes in
§3 were throwaway scripts, read-only against `data.sec.gov`; their result is reproduced by
the table above and the sample rule is stated so a re-run lands on the same 80 firms.*
