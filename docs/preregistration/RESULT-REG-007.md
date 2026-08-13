# RESULT-REG-007 · the disclosed trigger does not discriminate, and the placebo says why

- **Registration:** `REG-007-p3-triggering-disclosure.md`, commit **656b914**, 2026-08-13 —
  committed and pushed **alone**, before `wt093` existed and before any statistic below had a
  value.
- **Instruments:** `scripts/wt093_harvest.py` (locates filings, extracts passages, computes
  nothing), `scripts/wt093_triggering_disclosure.py` (F1–F11, then Λ). **8 severe · 1
  definitional · 0 vacuous.**
- **Data:** 1,925 firm-years across 711 filers, 9,852 passages, crawled in a cloud container.
  Committed as `data/reg-007-*`; the passage corpus is `reg-007-passages.json.gz` (3.7 MB).
- **Verdict:** **every falsifier passes. Λ is not significant in either registered fold, and
  the two folds disagree in sign. The registered discriminator does not discriminate, and F8's
  placebo — registered in advance — establishes why.**

---

## 1 · What was registered, and what came back

REG-007 asked whether the **disclosed** trigger separates the two explanations REG-006 left
standing for §5.4's off-diagonality: the standard's own co-testing rule (`ASC 350-20-35-3C(f)`
makes "the testing for recoverability of a significant asset group within a reporting unit" a
goodwill triggering event) against economic co-movement. The registered statistic is

> **Λ = P(names an (f)-family trigger | JOINT) − P(names an (f)-family trigger | GOODWILL-ONLY)**

inside the mandated-disclosure window. Both registered fold variants:

| variant | JOINT | GOODWILL-ONLY | **Λ** | Fisher two-sided *p* |
|---|---|---|---|---|
| `BOTH` folded into names-(f) | 136 / 244 = 0.5574 | 145 / 281 = 0.5160 | **+0.0414** | 0.3805 |
| `BOTH` folded the other way | 20 / 244 = 0.0820 | 32 / 281 = 0.1139 | **−0.0319** | 0.2435 |

**The sign of Λ is a coding choice.** REG-007 §3.4 required both variants to be reported
precisely so that this could not be discovered after the fact and then resolved in the
convenient direction. It was, and it is reported. Neither is close to significant on 525
classified firm-years.

Under REG-007 §5 P3, registered before the run: **Λ ≈ 0 is not evidence for co-movement.** The
omission of an internal trigger runs one way, so a null was registered as uninformative in
advance. It is uninformative now.

## 2 · THE PLACEBO IS THE RESULT

F8 required the control arm and the placebo window to run **in the same pass**, which is ladder
C's lesson promoted to a falsifier. The placebo is firm-years with a non-goodwill charge and
**no** goodwill charge, where `ASC 350-20-50-2(a)` does not apply and nothing compels a
facts-and-circumstances description at all:

| | firm-years classified | (f)-family rate |
|---|---|---|
| mandated-disclosure window (`G > 0`) | 644 | **0.436** |
| placebo (`t > 0`, `G = 0`) | 1,189 | **0.403** |

**Three percentage points.** If the keyword families were reading a firm's actual trigger, the
placebo — where no mandate operates and no goodwill test was necessarily run — should be far
below the window. It is not. **The classifier is reading something that is present whether or
not a goodwill impairment occurred**, and that is the finding: not that the two hypotheses tie,
but that this instrument never had the resolution to separate them.

*Post-hoc, and labelled as such:* the F1 sample suggests what that something is. **16 of the 60
adjudicated windows (26.7%) are accounting-policy boilerplate** — "reviewed for impairment upon
certain triggering events", "we review goodwill for impairment in the fourth quarter of each
year, and also upon the occurrence of triggering events" — prose that recites the *policy* and
names no event. That reading is not a registered quantity, no test turns on it, and it is
recorded in `data/reg-007-polysemy-audit.json` under an explicit post-hoc flag.

## 3 · The falsifiers, including the ones that passed

**F1 · PASSAGE-LEVEL POLYSEMY — PASSES at 6/60 = 10.0% against a 15% ceiling.** Sixty windows
adjudicated by hand, seed 20260813, verdicts committed to `data/reg-007-polysemy-audit.json`.
The six survivors are a Senior Notes change-of-control triggering event, a margin-loan price
trigger, an arrangement-agreement condition precedent, a 2028 Notes repurchase trigger, a
Series A-1 preferred redemption trigger, and a Certificate of Designation dividend step-up.
**REG-007 §2.2 measured that the within-file conjunction removes the exhibit population
entirely — 764 files, 764 accessions, one genuine exhibit and that an EX-13. Ten percent is
what survives inside the primary document, and it is under the ceiling but it is not zero.**

**F2 · RESOLUTION — every registered phrase resolves; two keywords are DEAD, named here.**
`composition of its net assets` and `goodwill impairment loss in the financial statements of a
subsidiary` match **zero** passages in our own sample. The first is our own transcription error:
the standard reads "a change in the composition **or carrying amount** of its net assets", and
collapsing that disjunction produced a string no filing contains. **This is `-18`'s dead XBRL
tag, in our own new code, three hours after the lesson was written down.** F2 caught it by name
on the first run, which is the mechanism working — but REG-007 F2 registered the handling as
*report it, do not fix it*, so the families ran as registered and the defect is published rather
than patched. Fixing it is a new registration.

**F3 · WINDOW SENSITIVITY — PASSES.** Λ (fold-internal) is +0.0201, +0.0414, +0.0436 at
half-widths 375, 750, 1500; *p* = 0.70, 0.38, 0.32. Sign stable, magnitude small, nothing
significant anywhere.

**F4 · DEDUPLICATION — PASSES.** Zero `(cik, fiscal_year)` keys carry two filings. Two firm-years
resolve only to a 10-K/A, recorded.

**F5 · THE `NEITHER` CEILING — FIRED FIRST, AND THE GUARD WAS WRONG, RESOLVABLY, FROM THE
REGISTRATION'S OWN WORDS.** As first coded it returned 213/736 = 28.9% against a 20% ceiling and
refused to report anything. **92 of those 213 firm-years contain none of the nine registered
phrases at all.** REG-007 F5 refutes "the keyword families … as a partition of the (a)–(g)
space"; a firm-year that never presented a point in that space cannot be evidence the families
fail to partition it. That is the exact mirror of REG-006's Q4 guard, which counted firm-years
with no goodwill at all as "unresolved" until the registration was read twice. **The ceiling was
not moved.** Only the denominator was corrected, to firm-years bearing at least one passage:
**119/644 = 18.5%**, and the strict figure **211/736 = 28.7%** is printed beside it. `SILENT` is
now a fifth cell with its own guard, so the two states can never be folded again.

**F6 · THE FTS CAP — DEFINITIONAL, with its reason.** The harvest resolves `(cik, fy)` through
`data.sec.gov/submissions`, which is not capped, so no admissible world truncates a tail here;
the guard exists to catch a refactor back onto the capped endpoint. REG-007 §2.4 separately
measured every full-text batch below 10,000.

**F8 · CONTROL AND PLACEBO IN ONE PASS — PASSES,** and §2 is its output.

**F9 / F10 · THE TWO CODIFICATION FACTS THE DESIGN RESTS ON — verified, with their provenance
and its limits.** `350-20-35-3C(f)` contains "the testing for recoverability of a significant
asset group within a reporting unit", confirmed against three independent verbatim
reproductions (EY FRD BB1499 §3.1.1 dated 14 July 2026; Grant Thornton *Viewpoint 2023* p. 39;
Deloitte DART §2.3.1) and two SEC comment-letter responses that recite the standard
letter-by-letter (NetSol 2014-08-20, KEYW 2016-01-04). The enumeration runs (a) through (g) and
stops. `350-20-50-2` is triggered "for each goodwill impairment loss recognized" and no paragraph
of `350-20-50` compels triggering-event disclosure absent a recognised loss. **FASB's own server
returned 403 to every attempt. This is recorded, not papered over.**

**F11 · THE S-K CITATION — verified and closed, `wealthTensor-20`.** The *Financial Reporting
Manual* §9510.2 cites S-K **303(a)(3)(ii)**. That designation **no longer exists.** Release
33-10890 (Nov 2020) restructured Item 303 so that paragraph (a) is the Objective and carries no
numbered subdivisions at all; the "known trends or uncertainties" requirement §9510.2 is reaching
for now sits at **17 CFR 229.303(b)(2)(ii)** — "Describe any known trends or uncertainties that
have had or that are reasonably likely to have a material favorable or unfavorable impact on net
sales or revenues or income from continuing operations" — with the liquidity twin at (b)(1)(i).
Checked against the eCFR text in force, not against a practitioner reproduction.

The FRM is not so much wrong as **frozen**: Topic 9 still carries "Last updated: December 31,
2009", eleven years before the amendment it has not absorbed. That is a caution about the manual
generally, not about this one citation — REG-007 §1 leans on §9510.1–9510.3 for the proposition
that the no-charge case is MD&A-driven, and that proposition survives (the requirement moved, it
did not disappear), but any *numbering* taken from the FRM is presumptively stale.

Nothing in this result or in the manuscript prints an S-K paragraph citation. If one ever does it
cites **303(b)(2)(ii)** and does not inherit the FRM's numbering.

## 4 · Three corrections that land regardless of Λ

1. **The "not all-inclusive" language is `ASC 350-20-35-3F`, not `35-3C`.** 35-3C ends at (g)
   with no qualifier. Pair 35-3F with **35-3G** for the "no single factor is a standalone
   trigger" point.
2. **`ASC 350-20-35-31` is a four-sentence paragraph.** The "(thus potentially requiring a
   goodwill impairment test)" parenthetical sits in its **second** sentence, inside the "For
   example, if a significant asset group is to be tested for impairment under the Impairment or
   Disposal of Long-Lived Assets Subsections of Subtopic 360-10 (…)" clause. Quoting 35-31 as one
   sentence truncates it.
3. **`IAS 36 ¶104` and `ASC 350-20-35-31` run in OPPOSITE DIRECTIONS and must never be cited for
   each other.** IAS 36.104 is a *loss-allocation waterfall* — once a CGU loss is measured it hits
   goodwill **first**. ASC 350-20-35-31 is a *test-ordering* rule — other assets are written down
   **before** the goodwill test, changing the carrying amount that enters it. The single ordering
   sentence in the field's leading survey is the IFRS one.

## 5 · Prior art — the gap looks real, and the shape of the evidence is stated exactly

The complete published text of **Amel-Zadeh, Glaum & Sellhorn (2023), *European Accounting
Review* 32(2): 415–446** was read (CC-BY version of record, Oxford ORA). Term counts in the full
text: `ASC 350-20` = **0**, `ordering` = **0**, `order in which` = **0**, `co-movement` = **0**;
all six `sequenc` hits are "consequently". Its §5.1.2 internal-validity catalogue names
pooling-of-interests self-selection, dotcom/GFC events, enforcement changes, CEO-turnover
endogeneity and event-study contamination — and the nearest passage to this question is
"goodwill impairments are often accompanied by restructuring charges (Cready et al., 2012;
Hirschey & Richardson, 2002)", framed as **contemporaneous-disclosure contamination in event
studies**, not as test sequencing. Its §5.3.1 "research questions that remain unanswered" does
not mention it. The IASB's own 58-page *Goodwill and impairment: academic evidence* compilation
returns zero for `ordering`, `before goodwill`, `350-20` and `triggering event`.

Also checked: **Riedl (2004)** *TAR* 79(3): 823–852 pools asset classes into an aggregate
write-off and pre-dates SFAS 142, so goodwill sat *inside* SFAS 121's scope and there was no
cross-asset test order to confound — **he cannot be a precedent for, or a victim of, this
confound**. **Ramanna & Watts (2012)** *RAST* 17(4): 749–780 contrasts private information
against agency incentives; the resemblance to sequencing-versus-co-movement is a loose
structural analogy and nothing stronger. The only academic treatment of 8-K Item 2.06 located
anywhere is **Lerman & Livnat (2010)** *RAST* 15(4): 752–778, where it is one row of an
item-level taxonomy — 532 filings, 0.4% of sample.

**This is recorded as "not found by keyword search", not as "does not exist."** Google Scholar
returned `ROBOTS_DISALLOWED` and SSRN search was behind a Cloudflare challenge, so no
citation-forward sweep was possible and a badly-titled working paper would be invisible to it.
The unread leads, named so the next pass starts above zero: **Cready et al. (2012)** and
**Hirschey & Richardson (2002)**.

## 6 · What this does and does not license

- It does **not** license "the co-occurrence is economic." A null from an instrument whose own
  placebo shows it reads boilerplate is not a finding about the world. Same discipline as
  ladders A, A3 and R.
- It **does** license the §5.4 amendment of REG-007 §7.1, which stands on the *selection*
  argument and not on Λ: triggering-event disclosure is compelled by `350-20-50-2(a)` only when
  a loss is recognised and is otherwise MD&A-driven, so any instrument built on it outside the
  mandated window is conditioned on the outcome under study.
- It **does** license the three corrections of §4.
- **The next instrument is not a bigger keyword list.** The registered families reach 0.436 in
  the window and 0.403 in the placebo; adding keywords moves both. What would separate them is a
  measure that only exists in event-specific narrative — the *named* reporting unit, the *dated*
  trigger, the charge amount tied to the sentence — which is a parsing problem, not a lexicon
  problem, and it is a new registration.
