# REG-006 · Theory + data registration · does the ordering rule MANUFACTURE the off-diagonality, or FIGHT it?

- **Status:** REGISTERED — committed and pushed before any line of
  `scripts/wt092_sequencing_vs_coupling.py` was written and before any statistic below was
  computed. WT-052.
- **Registered:** 2026-08-13, session `wealthTensor-18`.
- **Series:** `REG-*`. Unlike REG-004 and REG-005 this is **not** a claim about our own
  arithmetic. It collects new data and it re-derives a published sample under a corrected
  instrument. It is closest in kind to REG-003.
- **Instrument to be written after this file is pushed:**
  `scripts/wt092_sequencing_vs_coupling.py`.
- **Sample:** the REG-003 universes — US-listed SIC 5200–5999 (retail trade) and SIC 7370–7379
  (computer and data processing services), 2013–2024, `companyfacts`. **Re-harvested**, for the
  reason in §1. All EDGAR access runs in a cloud container; darwin's disk is at 95%.

---

## 0 · The question, and why §5.4's concession is the thing under test

§5.4 measures the departure from diagonality and then concedes it away:

> "ASC 360 requires the recoverability screen on long-lived assets *before* the goodwill test, so
> one triggering event can produce two charges in one quarter by the ordering of the standards
> rather than by the coupling of the assets. **This design cannot separate those.**"

Limitation 9 repeats the concession. The concession is stated as though the sequencing rule were a
single channel pushing in a single direction — toward more co-occurrence. **It is not.** The rule
does two things at once and they carry opposite signs on the statistic §5.4 reports.

**The rule is also not where the paper says it is.** It is **ASC 350-20-35-31**, in the goodwill
subtopic, not in ASC 360; ASC 360-10-35-27 carries the reciprocal cross-reference. And
**ASC 350-20-35-32** extends it to *all* assets tested for impairment, "not just those included in
the scope of the Impairment or Disposal of Long-Lived Assets Subsections of Subtopic 360-10" —
which means the rule governs §5.4's **strongest** pairwise cells, indefinite-lived intangible ×
goodwill (5.83×) and finite-lived intangible × goodwill (2.22×), and not merely the PP&E one. The
manuscript's version of the concession is narrower than the rule that generates it. Both defects
are repaired in §7.

### The two channels

**(S+) CO-TESTING — sequencing creates joint testing.**
ASC 350-20-35-3C(f) lists, among the events requiring an interim goodwill test, "a change in the
composition or carrying amount of its net assets" and — explicitly — "**the testing for
recoverability of a significant asset group within a reporting unit**." ASC 350-20-35-31 itself
parenthesises the same thing: "if a significant asset group is to be tested for impairment under
the Impairment or Disposal of Long-Lived Assets Subsections of Subtopic 360-10 **(thus potentially
requiring a goodwill impairment test)**." The act of testing one class is a listed indicator for
testing the other. This channel raises co-occurrence and it is the one §5.4 names.

**(S−) ABSORPTION — sequencing suppresses joint *recognition*.**
The other asset's charge is recognised **first**, and it reduces the reporting unit's carrying
amount before the goodwill comparison is made (ASC 360-10-35-27). Under the single-step measurement
the goodwill charge is the excess of the reporting unit's carrying amount over its fair value,
"limited to the total amount of goodwill allocated to that reporting unit" (ASC 350-20-35-2,
35-8). The reporting unit's **fair value is an economic quantity and is not moved by the accounting
entry** — this is our analytical premise and we mark it as ours; no source states it. Therefore a
prior charge of size *x* reduces the recognised goodwill charge by *x*, until zero or the cap
binds.

This is not our arithmetic. KPMG's *Handbook: Impairment of nonfinancial assets* (2024), Question
4.4.10, states the direction — "the practical effect of this sequencing is that if the reporting
unit's carrying amount is reduced through these other impairment tests, it is less likely that the
adjusted carrying amount will exceed the reporting unit's fair value" — and Example 4.4.10 works a
case in which $850 of prior charges converts a goodwill impairment into **zero**, closing with
"however, if goodwill had been tested for impairment before the indefinite-lived intangible assets
and long-lived assets were tested, a different conclusion would have been reached." Grant Thornton
(2023) and EY's FRD state the mechanism in prose. **"Dollar for dollar" is our phrasing and appears
in none of them**; what they state is the sign.

### What follows, and it is the point of this registration

Under a **sequencing-only** null, the two charges are **substitutes at the margin**: the standards
convert what would have been a goodwill charge into a long-lived-asset charge, one for one, in the
region where both would otherwise bind. Under **economic coupling**, a common shock makes both
charges **larger together**: they are complements.

**§5.4 observes them as complements, at 4.12× and 2.02×.** The mechanical reading the paper
conceded does not merely fail to explain that sign on its recognition channel — on that channel it
predicts the opposite. The concession is not wrong, because S+ is real and may dominate; but it is
**incompletely stated in a way that understates the paper's own result**, and it makes a point
prediction the paper never extracted.

**This registration does not claim the identification is closed.** It claims the null has an
internal structure that can be measured, and it registers the measurement.

---

## 1 · A DEFECT IN OUR OWN INSTRUMENT, FOUND WHILE READING FOR THIS ONE, AND WHY IT IS REGISTERED HERE RATHER THAN PATCHED

`src/wealth_tensor/edgar.py` declares tier 0 as

```python
0: ("ImpairmentOfLongLivedAssetsHeldAndUsed",
    "TangibleAssetImpairmentCharges",
    "ImpairmentOfLeasehold"),
```

**`ImpairmentOfLongLivedAssetsHeldAndUsed` is not a us-gaap element.** It returns HTTP 404 from the
XBRL frames API for every year tested (CY2010, CY2015, CY2016, CY2020–CY2023) and it matches
**zero facts across all 307 firms of the registered sample**. The element that exists is
**`ImpairmentOfLongLivedAssetsHeldForUse`** — 811 filers in CY2016 and 1,080 in CY2021, and 2,202
facts across 126 firms of our own sample.

Audited against the committed sample (`data/pre-002-events.json`, all 307 firms, FY 2013–2024,
fact counts only — no event extraction, no statistic):

| tag | facts | firms > 0 | |
|---|---|---|---|
| `ImpairmentOfLongLivedAssetsHeldAndUsed` | **0** | **0** | registered, matches nothing |
| `TangibleAssetImpairmentCharges` | 930 | 61 | registered |
| `ImpairmentOfLeasehold` | 213 | 27 | registered |
| `ImpairmentOfLongLivedAssetsHeldForUse` | **2,202** | **126** | **omitted** |

| universe | firms seen by registered tier 0 | firms seen by the omitted tag | firms it ADDS | union | **coverage** |
|---|---|---|---|---|---|
| retail (pilot) | 41 | 59 | 37 | 78 | **52.6%** |
| computer services (replication) | 40 | 67 | 50 | 90 | **44.4%** |

**Tier 0 has been seeing under half of the firms that separately tag a long-lived-asset
impairment, and the cause is a misspelled element name.** Tier 0 is the smallest tier in the
sample — 21 retail and 34 computer-services events out of 695 — and it is the tier that feeds
§5.4's PP&E × goodwill cell, at 4.35× and 4.03×, the one cell whose magnitude replicates across
both sectors.

**This is registered rather than patched because patching it changes a published sample.** The
corrected tier-0 list is an input to this registration, declared before the re-derivation runs.
Ladder `C` below re-derives REG-003's lifts under it. **The corrected lift may be lower than
4.12× and 2.02×. This file registers, in advance, that whatever it is, it is reported, and that
§5.4 and Limitation 9 are amended to it.**

**The general defect, which is the one worth carrying.** A tag name matching nothing is, in every
downstream statistic, indistinguishable from a tag name matching nothing *in this sample*: both
contribute zero events and neither raises an error. That is the `-16` underflowed tail and the
`-17` truncated tail arriving a third time, in a new domain — **the misspelled tail**. The guard
is in §6, F1, and it is a test, not a comment.

**What is NOT claimed here.** The permutation null of REG-003 §4 redraws within each firm's own
eligible quarters and takes each firm's per-class frequency as given, so a thin tier 0 costs
**power** and does not by itself bias the lift. The concern is composition, not arithmetic:
`ImpairmentOfLeasehold` is a store-closure tag, so the retail tier 0 may be selected toward
lease-driven closures rather than toward long-lived assets generally. Whether the lift moves is
the empirical question ladder `C` asks, and it is asked before it is answered.

---

## 2 · The registered quantities

For firm *f* and fiscal period *t*, from `companyfacts`, all scaled by total assets at the start
of the period:

- **L** — recognised impairment of assets other than goodwill: tiers 0, 1, 2 under the
  **corrected** tag list of §1.
- **G** — recognised goodwill impairment: `GoodwillImpairmentLoss`.
- **W** — goodwill carrying amount (`Goodwill`) at the start of the period.
- **U** — the unresolved bin of §5, Q4.

**Regime.** `PRE` = fiscal periods beginning on or before 15 December 2019; `POST` = after. ASU
2017-04 is effective for annual and interim tests in periods beginning after 15 December 2019 for
SEC-filer public business entities (ASC 350-20-65-3(a)(1)), with early adoption permitted from a
measurement date after 1 January 2017 (65-3(b)) and prospective application (65-3(c)). **Early
adopters are not identifiable from XBRL**; they sit in `PRE` and attenuate the contrast toward
zero. Registered as such, in advance, in the conservative direction.

---

## 3 · THE FIVE REGISTRATION QUESTIONS, EACH ANSWERED IN ONE SENTENCE, BEFORE ANY DATA

**Q1 · WHICH OUTCOMES DOES THIS THRESHOLD FAIL TO SEPARATE?** (the falsifier · `-14`)
The threshold "charge > 0" cannot separate a reporting unit that was tested and passed from one
that was never tested, cannot separate a \$1 charge from a \$1bn one, and cannot separate a charge
folded into an aggregate tag from no charge at all — so **every statistic in this file is about
separately-tagged recognised charges**, the word "impairment" never appears in it unqualified, and
the count of firm-periods behind each ratio is printed next to the ratio.

**Q2 · IS THE SET I AM TAKING A SHARE OF GUARANTEED NON-EMPTY?** (the falsifier · `-14`)
Three sets, adjudicated now: `{L > 0 and G > 0}` is not guaranteed non-empty in any sector ×
regime cell, so **a cell with fewer than 20 firm-periods is reported as its count and no ratio is
formed from it**; `{the impaired asset group lies inside the reporting unit carrying the goodwill}`
is **guaranteed empty as an observable** — reporting-unit allocation is not in XBRL — so every
statistic conditioned on it is **WITHHELD IN ADVANCE and named here so that its absence is
legible**; and `{the goodwill cap binds}` needs goodwill allocated to the reporting unit, which is
likewise unobservable, so the cap region is handled by reporting the slope **as a function of
L/W**, never as a point.

**Q3 · WHICH VALUES CAN THIS INSTRUMENT NOT PRODUCE, AND DOES MY ESTIMATOR ASSIGN THEM MASS?**
(the ESTIMATOR · `-15`)
The instrument cannot produce `G < 0` (US GAAP forbids reversal — ASC 350-20-35-13), cannot
produce `G > W`, and — the one that matters — **cannot produce the fully-absorbed observation
`(L large, G = 0)` inside a sample conditioned on `G > 0`**, which is precisely where the
registered prediction lives; therefore the estimator is **censored at zero on `{L > 0, W > 0}`**,
and the `G > 0` least-squares slope is computed and printed **beside it as the deliberately wrong
variant**, in the `-17` pattern, so that the selection is visible rather than argued.

**Q4 · CAN THIS GUARD TELL AN EXHAUSTED TAIL FROM AN UNDERFLOWED ONE?** (the GUARD · `-16`)
Here the question is whether the guard can tell `G = 0` — tested, absorbed, nothing recognised —
from `G` **absent**, which may mean no goodwill, or goodwill impaired inside an aggregate tag, or
a filer who simply did not use the element: **missing is not zero**, so an absent goodwill charge
is admitted as a zero only when `W > 0` at the start of the period **and** no positive
`GoodwillAndIntangibleAssetImpairment` or `AssetImpairmentCharges` fact exists in the same period
that could contain an untagged goodwill component; otherwise the firm-period goes to the
**unresolved bin `U`**, which is printed, and **a run in which `U` exceeds 15% of eligible
firm-periods fails the guard and reports no slope at all**.

**Q5 · IS THIS CONSTANT READ FROM THE TABLE THAT PUBLISHED IT, OR RECOMPUTED FROM ITS INPUTS?**
(the LEVEL · `-17`)
Every §5.4 quantity this file cites — 4.12×, 2.02×, 4.35×, 4.03×, 5.83×, 2.22×, 695 events, 307
firms, 0.408/yr — is **read from `RESULT-REG-003.md`**, checked line by line against it before
this file was written and not recomputed from `k̂` or `q̂`; and the instrument carries a severe
check that reproduces REG-003's two universe lifts from the committed event file to `1e-4`
**with the from-scratch recomputation as its witness**, on the rule that if the two disagree,
**the published table wins and the disagreement is the finding.**

---

## 4 · The registered predictions

**A · ABSORPTION HAS A SIGN, AND IT IS NEGATIVE.**
Conditional on `L > 0` and `W > 0`, the censored slope `∂G/∂L` is **negative** in `POST`.
Pure economic coupling predicts a **positive** slope: a common shock raises both charges together.
The two hypotheses are separated by a sign, not by a magnitude, which is why this is worth running.

**A2 · THE MAGNITUDE IS BOUNDED BELOW BY ENTITY AGGREGATION.**
XBRL reports entity totals. A firm with several reporting units may recognise `L` in one and `G`
in another, between which no absorption occurs. **Entity-level aggregation therefore attenuates
the slope toward zero, monotonically in the number of reporting units, which is unobserved.**
Registered consequence: **the estimated slope is a lower bound in magnitude and is never to be
read as the standard's arithmetic coefficient.** No free parameter is introduced to absorb this.

**A3 · THE ATTENUATION IS ITSELF TESTABLE.** Firms with a single reported operating segment
should show a **steeper** negative slope than multi-segment firms. This is a consistency check on
A2 and it is registered as such: **if it fails, A2's attenuation story is wrong and A's magnitude
must be reported without it.**

**R · THE REGIME CONTRAST IS THE IDENTIFICATION.**
ASU 2017-04 changed the goodwill **measurement** — Step 2's implied-goodwill comparison gave way
to the direct excess of carrying amount over fair value — while leaving **ASC 350-20-35-31 and
-32 unamended**; their text is byte-identical from FAS 142 ¶29 (2001) through the 2025 EY FRD, and
neither paragraph appears in the amendment instructions of ASU 2011-08, ASU 2017-04 or ASU 2021-03.
So the reform **sharpens S− and leaves S+ alone.** Registered prediction: **the negative slope is
steeper in `POST` than in `PRE`, and the co-occurrence lift computed on positive charges is
lower in `POST` than in `PRE`.** This is a difference across a rule change within the same firms,
and it is the closest thing to an instrument this design has.

**C · THE PUBLISHED LIFTS, RE-DERIVED UNDER THE CORRECTED TAG LIST.**
REG-003 §4's permutation, unchanged in every other respect — same eligible-quarter risk set, same
10,000 draws, same two-sided reporting — with tier 0 corrected. **Reported whatever it is.**

---

## 5 · What this registration explicitly does NOT do

- **It does not collect triggering-event text**, which is the discriminator §5.4 actually named.
  8-K Item 2.06 is dead as a population: roughly 100 filings a year against some 1,400 firms
  recording an impairment, because the Item's own instruction exempts a conclusion reached "in
  connection with" the preparation of the next periodic report, and a 2013 SEC C&DI extended the
  exemption to conclusions that merely *coincide* with it. The live route is "triggering event"
  text in 10-K/10-Q — 1,235 such 10-Ks in 2023, 764 of them also containing "goodwill impairment" —
  and it is a hand-and-NLP collection that deserves its own registration. **Teed up as REG-007.**
- **It does not touch PRE-001.** REG-003 §7 ruled it out in writing before any number existed and
  nothing here reaches it.
- **It does not re-fit `α̂`, `k̂` or `q̂`.** Those are read where needed and not recomputed (Q5).
- **It adds no free parameter anywhere**, to absorb A2's attenuation or anything else.

---

## 6 · Falsifiers — each one can kill the instrument, all run before any ladder

- **F1 · TAG RESOLUTION.** Every element named in `TIER_TAGS`, and every element named in this
  file, must resolve to **strictly more than zero facts** in the registered sample. A zero is a
  misspelling until proven otherwise. **This is the guard that would have caught §1 the day it was
  written and it ships as a test, not as a note.** If any tag returns zero, the run aborts and
  names it.
- **F2 · THE MODEL OF THE STANDARD NESTS ITS OWN WORKED EXAMPLE.** Implemented as
  `G = min(max(CA − x − FV, 0), GW)` under the single-step measurement, the instrument must
  reproduce KPMG Example 4.4.10 exactly: carrying amount \$4,200 before other charges, fair value
  \$3,500, goodwill \$1,500, prior charges \$850 → recognised goodwill impairment **\$0**, against
  **\$700** had goodwill been tested first. If it does not reproduce both branches, our model of
  the standard is wrong and nothing downstream means anything.
- **F3 · NON-VACUITY.** On synthetic firm-periods generated **with** absorption, the censored
  estimator must recover a slope of −1 to within 0.05 from the registered specification alone.
  **If it cannot find the answer when there is one, no null result it reports means anything.**
- **F4 · WITNESS.** On synthetic firm-periods generated with **pure economic coupling and no
  absorption** — both charges drawn increasing in a common shock — the estimator must return a
  **positive** slope. If it returns a negative slope on a world with no absorption, the estimator
  manufactures the finding and **no verdict may be read from ladder A.**
- **F5 · PLACEBO REGIME.** Ladder R re-run with a placebo adoption date of 15 December 2016 must
  produce a smaller slope shift than the real date. If the placebo moves as much, the contrast is
  a time trend and ladder R is void.
- **F6 · THE PUBLISHED TABLE WINS.** The severe check of Q5 must reproduce RESULT-REG-003's 4.12×
  and 2.02× from the committed event file to `1e-4` under the **original** tag list. A failure
  here means the committed sample and the published table have drifted apart, which is a bigger
  finding than anything in §4 and is reported first.

---

## 7 · The manuscript repairs this registration commits to, whatever the ladders return

Two are factual and are owed regardless of any result:

1. **§5.4 and Limitation 9 attribute the ordering rule to ASC 360. It is ASC 350-20-35-31**, with
   the reciprocal cross-reference at ASC 360-10-35-27. Corrected in place.
2. **ASC 350-20-35-32 makes the rule general**, so the concession covers the indefinite-lived and
   finite-lived intangible cells — §5.4's strongest — and not only PP&E. The concession is
   **widened**, which makes it a stronger objection, and stating it accurately is owed before any
   answer to it is offered.

Neither is polish and neither reopens a section under a standing no-polish order: one is a wrong
citation and one is a scope error, both in sentences that carry the paper's own limitation. The
substantive rewrite of the concession — the two-channel statement — lands only if the ladders
return, and it **replaces** hedging rather than adding to it: `-18`'s pass must leave the
defensive-sentence count non-increasing, per charter §2.

---

## 8 · Stopping rule

The instrument runs once. If ladder A returns and R does not, A is reported alone with R's failure
named. **No third specification is fitted to rescue a ladder.** If the corrected lift of ladder C
lands below REG-003's published figure, §5.4's number is amended down and the amendment is stated
in the text where the number is — not in a footnote, and not in Limitation 9.

**REG-007 is teed up here and is not begun in this session:** the triggering-disclosure
instrument, the discriminator §5.4 named, on 10-K/10-Q "triggering event" text.
