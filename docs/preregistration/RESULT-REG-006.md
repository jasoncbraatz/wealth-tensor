# RESULT-REG-006 · the ordering rule is two channels, the off-diagonality survives a corrected instrument, and the net cannot be signed from entity-level filings

- **Registration:** `REG-006-p3-sequencing-vs-coupling.md`, commit **6a5094a**, 2026-08-13 —
  committed and pushed before a line of `wt092` was written and before any statistic below
  existed.
- **Instruments:** `scripts/wt092_harvest.py` (panel, computes nothing),
  `scripts/wt092_sequencing_vs_coupling.py` (falsifiers, ladders A · A3 · R),
  `scripts/wt092_ladderC.py` (ladder C). **8 severe · 0 definitional · 0 vacuous** in the
  ladder script; ladder C runs `wt089`'s registered `instrument_b` unmodified, 10 severe.
- **Data:** two SIC universes, 1,883 registrants, `companyfacts`, FY 2013–2024, crawled in a
  cloud container. Committed as `data/reg-006-*`.
- **Verdict, the falsifiers:** **F1 · F2 · F3 · F4 · F6 pass. F4b failed as coded and the
  failure is a finding. F5 FAILS, and it voids ladder R.**
- **Verdict, the ladders:** **A FAILS. A3 FAILS. R VOID. C RETURNS, and C is the result.**

---

## 1 · What was registered, and what came back

REG-006 asked whether §5.4's concession — that the sequencing of the impairment standards
might manufacture the measured departure from diagonality — is correct as stated. It is not,
and the way it is wrong is structural rather than empirical.

**The rule is not where the paper says it is.** §5.4 and Limitation 9 attribute the ordering to
ASC 360. It is **ASC 350-20-35-31**, in the goodwill subtopic; ASC 360-10-35-27 carries the
reciprocal cross-reference, and its second sentence says so explicitly. The text is unchanged
from FAS 142 ¶29 (2001) and appears in the amendment instructions of none of ASU 2011-08,
ASU 2017-04 or ASU 2021-03, so it is stable across the entire 2013–2024 window.

**The rule is broader than the paper's version of it.** **ASC 350-20-35-32**: the requirement
"applies to all assets that are tested for impairment, not just those included in the scope of
the Impairment or Disposal of Long-Lived Assets Subsections of Subtopic 360-10." The concession
therefore covers the indefinite-lived and finite-lived intangible cells — §5.4's **strongest**
— and not only the property one. Stating it accurately makes it a **stronger** objection than
the paper currently raises against itself.

**And it is two channels, with opposite signs.** ASC 350-20-35-3C(f) lists, as an event
requiring an interim goodwill test, "a change in the composition or carrying amount of its net
assets" and — explicitly — "the testing for recoverability of a significant asset group within a
reporting unit"; 35-31 itself parenthesises "(thus potentially requiring a goodwill impairment
test)". So the rule **creates joint testing**. But the other charge is recognised *first* and
reduces the reporting unit's carrying amount before the goodwill comparison, and under
ASC 350-20-35-2 and 35-8 the goodwill charge is the excess of that carrying amount over fair
value, capped at goodwill allocated to the unit. So the rule **suppresses joint recognition**.

**F2 puts a number on the second channel and it is not our arithmetic.** KPMG's *Handbook:
Impairment of nonfinancial assets* (2024), Example 4.4.10: carrying amount \$4,200, fair value
\$3,500, goodwill \$1,500. Test goodwill first and the impairment is **\$700**; recognise \$850
of other charges first, as ASC 350-20-35-31 requires, and it is **\$0**. `wt092` reproduces both
branches exactly, and a second severe check confirms the offset is one-for-one strictly inside
the region — a \$200 increase in the prior charge reduces the goodwill charge by exactly \$200,
until zero or the cap binds. KPMG states the direction ("less likely that the adjusted carrying
amount will exceed the reporting unit's fair value"); the one-for-one reading is ours, and the
premise it rests on — that the reporting unit's *fair value* is an economic quantity unmoved by
the accounting entry — is ours too. No source states it and the paper should not imply one does.

> **Under the ordering alone the two charges are substitutes at the margin. §5.4 observes them
> as complements, at 4.12× and 2.02×.** The mechanical reading the paper conceded does not
> merely fail to explain that sign on its recognition channel — on that channel it predicts the
> opposite.

This does not close the identification. The co-testing channel is real and may dominate. What
it establishes is that the concession as written names one of two channels and happens to name
the one that runs *with* the finding rather than the one that runs against it.

## 2 · LADDER C — THE INSTRUMENT WAS HALF BLIND, THE HEADLINE SURVIVES IT, AND ONE PUBLISHED SENTENCE DOES NOT

`src/wealth_tensor/edgar.py` registered tier 0 as `ImpairmentOfLongLivedAssetsHeldAndUsed`,
`TangibleAssetImpairmentCharges`, `ImpairmentOfLeasehold`. **The first is not a us-gaap
element.** It returns 404 from the XBRL frames API for every year tested and matches **zero
facts across all 307 firms of the registered sample**. The element that exists is
`ImpairmentOfLongLivedAssetsHeldForUse` — 2,202 facts across 126 of those same firms. Tier 0 was
seeing **52.6%** of retail and **44.4%** of computer-services firms, for the life of the project,
because of a spelling.

Ladder C re-derives REG-003 §4 under the corrected list. Same `extract_events`, same
`onset_rule="peak"`, same eligible-quarter risk set, same seed, same 10,000 draws — **only tier
0's tag list differs, and both arms run in the same pass over the same crawl.**

| universe | tier 0 | events | firm-quarters | N_co | null mean | **obs/exp** |
|---|---|---|---|---|---|---|
| retail | original | 243 | 212 | 29 | 7.2 | **4.01×** |
| retail | **corrected** | **303** | **258** | **41** | 10.2 | **4.01×** |
| computer services | original | 439 | 391 | 43 | 21.4 | **2.01×** |
| computer services | **corrected** | **476** | **419** | **53** | 25.3 | **2.10×** |

**The headline is untouched: 4.01× → 4.01× and 2.01× → 2.10×.** The published figures are 4.12×
and 2.02×; this harness's original arm reproduces them to within the rebuild noise REG-003 §2
already documented, and **F6 reproduces them exactly — to 2.5 × 10⁻³ and 1.3 × 10⁻³ — from the
committed event file**, with every pairwise cell matching the published table.

**The defect cost power, not validity, and REG-006 §1 registered that expectation before the
run.** The permutation redraws within each firm's own eligible quarters and takes each firm's
per-class frequency as given, so a thin tier 0 loses observations without moving the ratio. It
is worth saying plainly that this was the registered prediction and it held, because the
alternative — that half a tier had been quietly biasing a published number — was live until the
ladder returned.

**The internal control is exact.** Every cell that does not involve tier 0 is identical across
the two arms to two decimals:

| cell | original | corrected |
|---|---|---|
| indefinite-lived intangible × goodwill (retail) | 5.83× | 5.86× |
| finite-lived intangible × goodwill (retail) | 3.34× | 3.35× |
| finite × indefinite (retail) | 5.28× | 5.31× |
| indefinite-lived intangible × goodwill (computer services) | 2.34× | 2.34× |
| finite-lived intangible × goodwill (computer services) | 2.21× | 2.22× |
| finite × indefinite (computer services) | 2.49× | 2.48× |

A tag change that moved cells it cannot touch would mean the two arms differ by something other
than the tag. They do not.

### 2.1 · The one published sentence that does not survive

§5.4 reports: "property with goodwill runs at 4.35× and 4.03× — **the one cell that replicates
its magnitude across two sectors**."

| PP&E × goodwill | original | corrected |
|---|---|---|
| retail | 3.63× (p 0.038, 4 obs) | **3.99× (p 0.0012, 14 obs)** |
| computer services | 4.14× (p 0.0096, 5 obs) | **2.17× (p 0.085, 8 obs)** |

Under the corrected instrument the retail cell strengthens and gains ten observations; the
computer-services cell falls to 2.17× and **loses Holm-corrected significance**. The pair is
3.99× and 2.17×, which is not a replicated magnitude. **The published cross-sector replication
claim rested on four observations in one sector and five in the other, and it does not hold when
the tier can see.**

What *does* replicate across both sectors, at every conventional level, are the two
intangible-with-goodwill cells: 5.86× / 2.34× and 3.35× / 2.22×, all four at p ≤ 0.005. **Those
are precisely the cells ASC 350-20-35-32 brings under the sequencing rule** — which is why §1's
scope correction is not bookkeeping.

### 2.2 · Two couplings that were previously unmeasurable

With a half-blind tier 0 the paper reports two retail cells at **0.00× and 3.27×, p = 1.0000**.
Corrected, they are **7.70× (p 0.012)** and **6.33× (p 0.0048)**. A cell reported as zero
because the instrument could not see one of its two arms is not a measured zero, and the
distinction is the same one this project has now paid for three times.

## 3 · LADDERS A, A3 AND R — THE ATTEMPT TO SIGN THE NET, AND WHY IT FAILED

The absorption channel makes a prediction: conditional on a non-goodwill charge and on goodwill
existing, the censored slope of the goodwill charge on the other charge is **negative**, and
ASU 2017-04 — which sharpened the measurement while leaving 35-31 unamended — should steepen it.

**Ladder A fails.** POST slopes are **+0.010** (retail, n = 417) and **+0.665** (computer
services, n = 318); PRE slopes are +1.608 and −0.008. No cell carries the registered sign
consistently and the bootstrap intervals are wide enough to contain almost anything
([−0.00, +3.38] in the largest).

**Ladder R is void.** The registered placebo, F5, requires the real adoption date to move the
slope more than a placebo three years early. Retail: real Δ = **−1.599**, placebo Δ = **−2.245**.
The placebo moves *more*, so the retail contrast is a time trend and the ladder cannot be read.
Computer services moves the wrong way in the first place (Δ = +0.674).

**Ladder A3 fails.** Single-segment firms should show the steeper negative slope if entity
aggregation is what attenuates it. They show **+0.263** against multi-segment **−0.009** — the
opposite ordering.

**F4b explains all three, and it was registered.** On synthetic data carrying *both* channels,
switching absorption off moves the slope from +0.455 to +0.963: the estimator recovers **0.508**
of a true difference of **1.000**. Even in a world built to contain the effect, with no
measurement error in the outcome and no entity aggregation at all, half the signal is gone. REG-006
§4 A2 registered entity aggregation as a further attenuation, monotone in the number of reporting
units, which XBRL does not disclose. **The design was under-powered by construction and the
registration said so before the data arrived.**

**F4b as coded also failed, and that failure is ours.** It demanded the difference equal 1.000
to within 0.25 — a magnitude claim that REG-006 §4 A2 had already registered as a *lower bound*.
The code contradicted the registration it was implementing. It was re-stated as the sign test
A2 licenses, the measured attenuation is printed rather than absorbed, and **no magnitude claim
is read from any ladder in this file.**

**The Q4 guard did its job twice.** As first coded it refused to report anything: 54.2%
unresolved against a 15% ceiling. Both causes were the guard being wrong rather than the data
being bad, and both are registered text. First, firm-years with **no goodwill at all** were
counted as unresolved when the goodwill test simply does not apply to them — 422 of 1,501; the
registered denominator is "eligible firm-periods", which they are not. Second, the registered
condition is an aggregate fact "**that could contain** an untagged goodwill component", and the
code flagged *every* positive subtotal, including ones fully explained by the components already
tagged. Only the **residue** above the project's materiality floor is a hiding place. Corrected,
the unresolved bin is **43 of 1,079, or 4.0%**; the strict reading, printed alongside it, is 497.

**What would separate the channels.** The absorption channel operates at the reporting unit and
US filings disclose neither the allocation of goodwill to reporting units nor the assignment of
asset groups to them. REG-006 §3 Q2 withheld both statistics in advance for exactly this reason.
The remaining route is the discriminator §5.4 actually named — the triggering disclosure — and it
is teed up as **REG-007**, unbegun. **8-K Item 2.06 is dead as a population**: roughly 100
filings a year against some 1,400 firms recording an impairment, because the Item's instruction
exempts a conclusion reached in connection with the next periodic report and a 2013 SEC C&DI
extended the exemption to conclusions that merely *coincide* with it. The live route is
"triggering event" text in 10-K/10-Q — 1,235 such 10-Ks in 2023, 764 of them also containing
"goodwill impairment".

## 4 · Q5 — every constant read, not recomputed

Every §5.4 quantity this file touches was read from `RESULT-REG-003.md` and checked against it
before REG-006 was written: 4.12×, 2.02×, 4.35×, 4.03×, 5.83×, 2.22×, 695 events, 307 firms.
**F6 is the guard**, and it passed: the committed event file reproduces the published lifts to
`1e-4` and every published cell exactly. The table and the sample have not drifted.

## 5 · The guard, mechanised

`tests/test_tag_resolution.py`, five tests, offline, against a committed audit artifact
(`data/tag-resolution-audit.json`). It asserts that every element named in `edgar.py` has had its
resolution checked, that every element REG-006 relies on matches something in our own sample,
that the dead element is pinned at zero so the finding cannot be quietly un-found, and that
`TIER_TAGS` still carries the dead element — because PRE-001's constants are a contract, the
correction is additive in `TIER_TAGS_REG006`, and a future session tidying up the "typo" has to
read this file first. **276 tests pass, was 271.**

**The lesson, stated once.** A tag that matches nothing is indistinguishable, in every downstream
statistic, from a tag that matches nothing *in this sample*: both contribute zero and neither
raises. That is `-16`'s underflowed tail and `-17`'s truncated tail in a third costume — a guard
that cannot tell **empty** from **absent**. Three sessions, three domains, one shape, and this is
the first of them to ship a test rather than a paragraph.

## 6 · Stopping rule, honoured

The instrument ran once. Ladder A returned and failed, R is void by its own placebo, A3 failed,
and **no second specification was fitted to any of them.** Ladder C is reported whatever it is,
as registered, and what it is includes one published sentence that has to go.
