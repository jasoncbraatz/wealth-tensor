# PRE-001 · Pre-registration · WT-026, the severe test

- **Status:** REGISTERED — committed before any lag statistic was computed. The git commit
  containing this file is the timestamp. If a later commit reports the result, the ordering of
  those two commits is the evidence that the prediction preceded the outcome.
- **Registered:** 2026-08-05 (S3)
- **Target paper:** III — the dual tensor and the reporting layer (ADR-001)
- **Model under test:** `src/wealth_tensor/lag.py`, the two-layer filter. Ledger WT-023, WT-026,
  WT-027, WT-028, WT-043.
- **Amendment rule:** this file is append-only after the first result commit. Corrections go in a
  dated `## AMENDMENT` section below, never by editing the text above it. A pre-registration you
  are free to rewrite is a diary.

---

## 0 · Why this exists at all

WT-043 established what actually killed Odum's emergy programme, and it was two things: (a)
coefficients that could not be measured independently of the accounting system that used them, and
(b) **no risky prediction** — so it became closed bookkeeping rather than a theory that could lose.

This framework passes (a) decisively: Λ⁻¹ is UN SDG indicator 7.3.1, published by somebody else,
for other reasons (WT-003). (b) is unbuilt, and (b) is the entire difference between a theory and
an accounting scheme.

This document is (b). It states, in advance and in public, a prediction the framework can lose.

---

## 1 · The prediction, in one sentence

**Recognition lag scales with the unobservability of the degradation** — and accounting standards
themselves supply the observability ranking, because the categories hardest to observe are exactly
the ones GAAP declines to depreciate on a schedule.

In the model's own notation (`lag.py`): φ is the observable share of each true change; the model's
sharpest claim is that lag and correction magnitude scale with **(1 − φ)**. This test asks whether
a φ ordering that we did not choose — one written into US GAAP decades before this framework
existed — produces the lag ordering the model requires.

---

## 2 · The observability ladder

The ladder is **assigned by accounting standard, not by us.** That is the point: an ordering we
constructed would be a free parameter (WT-016), and a free parameter forbids nothing.

| tier | asset class | standard | how value change reaches the statements | φ |
|---|---|---|---|---|
| **0** | Property, plant and equipment | ASC 360 | **scheduled depreciation**, every period, plus impairment on a triggering event | highest |
| **1** | Finite-lived intangibles | ASC 350-30 | **scheduled amortisation**, every period, plus impairment | high |
| **2** | Indefinite-lived intangibles ex goodwill (trade names, licences) | ASC 350-30 | **no schedule**; annual impairment test only | low |
| **3** | Goodwill | ASC 350-20 | **no schedule**; annual impairment test at reporting-unit level | lowest |

Tiers 0 and 1 carry a mandatory *continuous* channel through which deterioration reaches the
reported layer. Tiers 2 and 3 carry none: the only channel is a discrete test whose outcome is a
judgement. That is a φ gradient in the plain sense of `lag.py`, and it was not built by us.

**Tier 4 exists and this design cannot see it.** R&D (ASC 730), advertising and brand (ASC 720-35),
and human capital are *never capitalised at all* — φ ≈ 0, the model's most extreme regime. There is
no asset to impair, so there is no event to date. GAAP's most unobservable category is invisible to
any test built on GAAP. This is a known blind spot of the design, stated in advance, not discovered
afterwards. See §8.

---

## 3 · What makes this risky, stated before the result

Three legs, and the second is the one that matters.

1. **Neoclassical finance predicts no gradient.** Accounting classification is a veil over the same
   underlying cash flows. Under efficient markets, deterioration is incorporated when it becomes
   knowable, and how the bookkeeper files it is immaterial. A flat lag profile across tiers is
   exactly what the mainstream expects and is a live, plausible outcome here.

2. **The institutional prior runs *against* our prediction, and hard.** Goodwill and indefinite-lived
   intangibles are subject to a **mandatory annual impairment test**. PP&E is subject to **no
   scheduled test whatsoever** — ASC 360-10-35 requires a test only when a triggering event occurs.
   So the tier we predict will lag *most* is the only tier the standard-setters forced onto a
   calendar, and the tier we predict will lag *least* is the one nobody is required to look at until
   something goes visibly wrong. If our prediction survives, it survived a regime designed to defeat
   it. If we had chosen the ordering to flatter the theory, we would have chosen the opposite one.

3. **We can lose, and the loss is recorded with equal weight.** §7 states the falsification
   condition. A failure is written into `docs/LEDGER.md` as a DEAD-END entry with the same
   prominence as a success, per the ledger's opening rule, and it appears in the *Abandoned
   Approaches* section that ADR-001 promoted to load-bearing in every paper.

---

## 4 · Data

- **Source:** SEC EDGAR XBRL `companyfacts` (`https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`).
  Public, no key, no licence. Firm universe from `https://www.sec.gov/files/company_tickers.json`
  and SIC codes from EDGAR submissions metadata.
- **Access is logged.** The raw pull is cached to disk with the retrieval date so the analysis is
  reproducible without re-hitting the API, and so a later disagreement about a number can be settled
  against what we actually downloaded rather than against what EDGAR serves next year. EDGAR
  restates: `companyfacts` reflects the latest filing, so a figure can change under us.

### 4.1 · Universe — pilot

**Retail trade, SIC 5200–5999.** Chosen a priori, before any lag was computed, on four grounds:

1. all four tiers are materially populated (owned stores and distribution centres → Tier 0;
   customer relationships and franchise agreements → Tier 1; trade names → Tier 2; an acquisitive
   sector → Tier 3);
2. the 2013–2024 window contains a genuine, sustained, sector-wide operational deterioration — the
   e-commerce transition — so impairment events are plentiful and are not all one macro shock;
3. deterioration in retail is unusually *physically* legible (store traffic, square footage,
   inventory turns), which is the regime the framework is about;
4. large N.

Inclusion: SIC in [5200, 5999]; at least 12 quarters of revenue history; at least one impairment
event meeting §5.2.

### 4.2 · Replication universe — declared now, run unchanged

The identical code, with only the SIC filter changed, is run on **SIC 7370–7379 (computer and data
processing services)** as a held-out replication. Structurally different: asset-light, goodwill-heavy,
R&D-intensive (so its Tier 4 is enormous and invisible), and deteriorating for different reasons.

Declaring the replication *now* is deliberate. A pilot that succeeds and a replication chosen
afterwards is one experiment reported twice.

---

## 5 · Operational definitions

### 5.1 · Deterioration signal

**Primary:** year-over-year decline in quarterly revenue (`Revenues`, `RevenueFromContractWithCustomerExcludingAssessedTax`,
or `SalesRevenueNet`, in that fallback order; the tag actually used is recorded per firm).

Year-over-year, not sequential, because retail is violently seasonal and a sequential definition
would detect Christmas.

Revenue, not operating income, for one reason stated in advance: **operating income is contaminated
by the impairment charge itself.** An impairment lands in operating income, so an onset rule keyed to
operating income would partly detect the event it is trying to date. Revenue is not touched by the
charge. The cost of this choice is that an asset can degrade without revenue falling, which will
cause events to be dropped rather than mis-dated — a loss of power, not a bias toward the hypothesis.

### 5.2 · Impairment event

An event is (firm *i*, tier *T*, fiscal quarter *q\**) where a charge is reported under one of:

| tier | XBRL tags (any) |
|---|---|
| 0 | `ImpairmentOfLongLivedAssetsHeldAndUsed`, `TangibleAssetImpairmentCharges`, `ImpairmentOfLeasehold` |
| 1 | `ImpairmentOfIntangibleAssetsFinitelived` |
| 2 | `ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill` |
| 3 | `GoodwillImpairmentLoss`, `GoodwillAndIntangibleAssetImpairment` (assigned to tier 3 only when no separate tier-1/2 charge is reported in the same quarter) |

**Materiality floor:** charge ≥ **1.0 % of total assets** (`Assets`) at the most recent prior
period end. Charges below the floor are dropped and counted.

### 5.3 · Onset and lag

For event (*i*, *T*, *q\**), let *q₀* be the **earliest** quarter such that every quarter from *q₀*
through *q\* − 1* inclusive shows a YoY revenue decline, requiring a run of **at least 2** quarters.

**lag = q\* − q₀, in quarters.**

- No qualifying run → the event is **dropped** and counted as *no-deterioration-run*. It is not
  scored as lag 0.
- Lookback capped at **20 quarters**. An event whose run reaches the cap is **right-censored**,
  recorded at 20, and reported separately; the primary test is re-run excluding censored events as a
  robustness check.
- Quarters with missing revenue break a run.

### 5.4 · Multiple tiers in one quarter

A firm impairing two tiers in the same quarter contributes one event per tier. These share an onset
by construction and are therefore *not* independent; §6 handles it.

---

## 6 · Test statistic, fixed in advance

**Primary — Jonckheere–Terpstra trend test**, one-sided, alternative *L₀ ≤ L₁ ≤ L₂ ≤ L₃* with at
least one strict. This is the test built for an ordered alternative across k groups and it is being
named here precisely so that a different test cannot be selected later because it read better.

- **α = 0.05, one-sided.** The direction is predicted, so a one-sided test is legitimate — and the
  direction is written above, before the data.
- **Secondary:** Mann–Whitney U, tier 3 versus tier 0, one-sided.
- **Effect size:** difference in median lag, tier 3 − tier 0, in quarters, with a bootstrap
  interval (10,000 resamples, resampled **by firm**).
- **Non-independence:** the bootstrap resamples firms, not events. Additionally, a
  **one-event-per-firm** sensitivity (the largest charge by share of assets) is reported alongside
  the primary.
- **Reported regardless of outcome:** n by tier, median and IQR lag by tier, the JT statistic and
  p-value, the censored share, and the full drop accounting from §8.

---

## 7 · Falsification condition

The prediction **fails** if any of the following holds on the pilot universe:

1. the Jonckheere–Terpstra test is not significant at one-sided α = 0.05 in the predicted direction; **or**
2. median lag for tier 3 is **≤** median lag for tier 0; **or**
3. fewer than 10 events survive in any of tiers 0 and 3 — in which case the test is **inconclusive
   rather than passed**, and is reported as underpowered, not quietly widened until it populates.

A pass on the pilot that **does not replicate** on §4.2 is reported as a pass that did not
replicate. It is not reported as a pass.

---

## 8 · Confounds and rivals, named before the result

**These are not hedges. Each is a way this result could be true and mean something other than what
we claim, and each is stated now so that stating it later cannot look like a retreat.**

1. **Managerial discretion / the big bath.** Managers are documented to delay goodwill impairments
   for self-interested reasons. This design **cannot separate** that from an observability effect,
   and we will not pretend otherwise. Note, though, that the two are not really rivals: discretion
   requires something to be discretionary, and you cannot exercise judgement about the depreciation
   of a delivery van. Unobservability is plausibly the *enabling condition* for the agency story
   rather than its competitor — the relocation move of WT-039 applied a fifth time. **What would
   separate them:** lag regressed on managerial-incentive proxies (CEO tenure, turnover year,
   compensation structure) alongside tier. Out of scope for the pilot; named as the next test.

2. **Mechanical availability.** Only capitalised assets can be impaired. Conditioning on an
   impairment having occurred controls the extensive margin but induces selection on the intensive
   one: firms that never impair tier 3 are absent. Named; not solved here.

3. **Tier composition is not random across firms.** Goodwill-heavy firms are serial acquirers and
   may differ in ways unrelated to observability. The one-event-per-firm sensitivity and the
   two-sector design bound this; they do not eliminate it.

4. **Revenue is an imperfect proxy for physical deterioration.** §5.1. Costs power, should not bias
   toward the hypothesis.

5. **The annual-test calendar.** Tier 2 and 3 tests cluster in Q4 for most registrants. This
   *shortens* measured tier-2/3 lag by up to three quarters relative to a continuous-testing
   counterfactual, so it works against the prediction. Recorded as a known distortion in our
   disfavour rather than corrected, because correcting it would require a modelled counterfactual
   and a modelled correction in the favourable direction is exactly the move this project refuses.

6. **EDGAR restatement.** §4.

### What we deliberately do NOT test, and why

The model also predicts that **variance concentration** rises with unobservability (WT-028: 0.00 →
0.69 → 0.96 → 0.99 as φ falls). It would be easy to "confirm" that here and it would be worthless:
tier 3 has *no amortisation schedule by rule*, so 100 % of its recognised change is discrete
**as a matter of accounting definition, not of firm behaviour**. That test cannot fail, therefore it
is not a test. It is excluded on purpose, and the exclusion is recorded here so no future session
re-discovers it as a finding.

---

## 9 · Drop accounting — to be reported in full

Every event that leaves the sample is counted in one of these buckets, and the counts are published
with the result whether or not they are flattering:

`no_sic` · `sic_out_of_range` · `no_revenue_tag` · `insufficient_history` · `below_materiality` ·
`no_assets_denominator` · `no_deterioration_run` · `right_censored` · `ambiguous_tier` ·
`duplicate_restated_fact`

Saying what we sampled **and what we dropped** is a condition of the result being reportable at all.

---

## 10 · Reproducibility

- Code: `src/wealth_tensor/edgar.py` and `scripts/wt026_severe_test.py`, in
  `github.com/jasoncbraatz/wealth-tensor`.
- The tier map, the tag lists, the materiality floor, the onset rule and the test statistic are all
  fixed by **this document** and are read by the code, not re-typed into it.
- Unit tests run on synthetic fixtures and require no network, so the logic is checkable by anyone
  without an EDGAR round trip.
- The result commit names the commit SHA of this file.

---

## AMENDMENTS

*(none — append below, dated, never by editing above)*
