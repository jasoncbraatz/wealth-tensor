# RESULT-P0 · The disclosed life VALUES: three bounds measured, and a design that clears
# its own threshold on one rung out of six
*wealthTensor-28 · 2026-08-13 · REG-009 §2's probe, declared and priced before it was
written. Instrument: `scripts/reg009_p0_lifetime_values.py`. Full output:
`RESULT-P0-run.log`. Records: `data/reg-009-p0-lives-{2015,2023}.json`. Table:
`data/reg-009-p0-result.json`.*

**THIS DOCUMENT REPORTS NUMBERS. IT DOES NOT FIX D2, D3 OR D4.** Those are fixed in
REG-009 §2, in a later commit, citing this table. A probe that both measures the choice
and makes it is the shape `SOURCE-001` §4c spent a session unwinding, and REG-009 §2
declared this separation before the instrument existed.

---

## 0 · What was read, and the two checks that say it was read correctly

Twelve FSN notes zips — six per cycle, the filenames `SOURCE-001` §3b names — re-read for
the disclosed life **values** (`txt.tsv`'s `value` column, dimensioned through `dim.tsv`),
which is a different file and a different column from the one §3b counted tags in.

| | 2014-15 cycle | 2022-23 cycle |
|---|---|---|
| panel firm-years in window | 847 | 837 |
| 10-K located | 804 | 821 |
| **firm-years with a canonical life VALUE** | **612 (0.723)** | **684 (0.817)** |
| §3b's canonical-life coverage, for comparison | 0.727 | 0.823 |
| prior-period comparatives kept | 166 | 246 |

**Check 1 — the join did not drift.** P0 asks a different question of the same zips through
the same firm-year join, imported from `source001_lifetime_by_fyend` rather than copied.
Its coverage lands within four thousandths of §3b's on both cycles. A value reader that
disagreed with the registered coverage machinery would be measuring a different population
and saying so nowhere.

**Check 2 — the values are right, against a filing audited independently a session ago.**
`SOURCE-001` §3a hand-audited Target Corp (CIK 27419, `0000027419-23-000015`) three ways —
the FSN row, Target's own inline-XBRL 10-K fetched from `Archives/edgar/`, and a
`companyconcept` 404. P0 reproduces all three components exactly:

| component | §3a's audit | P0's midpoint |
|---|---|---|
| Building and building improvements | P8Y – P39Y | **23.5** |
| Fixtures and equipment | P2Y – P15Y | **8.5** |
| Computer equipment | P2Y – P7Y | **4.5** |

Pinned in `tests/test_reg009_p0.py` against the filing, not against P0's own output.

**Declined and counted, because a tag set is a coverage claim** (REG-009 §2's *no silent
caps*): 329 filings located with no canonical life value · 316 duplicate `iprx` rows · 51
unparseable durations · **4,990 rows on 177 non-canonical `*UsefulLife*` tags**, of which
`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` alone is 4,304. That last
number is not a rounding error and REG-010 may want it; it is excluded here to keep the
population identical to §3a's and §3b's.

**D2's shape problem, measured on components:** **interval 0.512 · point 0.461 ·
half-interval 0.027**. §1.6 said the disclosure is an interval for the majority of
firm-years and that nothing in this repository maps one to a δ. Half of the components
carry two endpoints; the collapse is not optional.

---

## 1 · P0-a · STICKINESS — §4.7's bound 2, and it splits by class

*|Δlog L| between two observations of the same firm. 0 means the disclosed life did not
move. Reported at the horizon the bound actually names: §4.7 says lives are sticky "across
the horizon over which timeliness is measured", and the panel's horizon is 2013-2025, so a
one-year read does not test that sentence. Reading two cycles eight years apart does — and
that, rather than coverage, is the reason P0 reads two cycles.*

A firm-year life is a **median across components**, so it moves when the component *mix*
changes and not only when a life is revised. That confound would be read as instability, so
the same measurement is run per component, matching on the component member string.

| PP&E (`R_MID`) | n | unchanged | median \|Δlog L\| | IQR |
|---|---|---|---|---|
| adjacent years | 31 | 0.323 | 0.2231 | 0.0000 – 0.5048 |
| decade, firm-year | 268 | 0.429 | 0.0846 | 0.0000 – 0.2877 |
| **decade, per component** | **703** | **0.744** | **0.0000** | **0.0000 – 0.0572** |

| finite-lived intangibles (`R_MID`) | n | unchanged | median \|Δlog L\| | IQR |
|---|---|---|---|---|
| adjacent years | 240 | 0.267 | 0.1397 | 0.0000 – 0.3567 |
| decade, firm-year | 124 | 0.145 | 0.2719 | 0.0750 – 0.4925 |
| **decade, per component** | **194** | **0.309** | **0.2073** | **0.0000 – 0.4353** |

**BOUND 2 HOLDS FOR PROPERTY AND FAILS FOR FINITE-LIVED INTANGIBLES, and the split is the
finding.** Three quarters of property components carry the *identical* disclosed life eight
years apart — the median move is exactly zero and the IQR reaches 0.057, so the typical
property life is not merely sticky, it is unrevised. Fewer than a third of intangible
components manage that, and their median move over the same span is 23 per cent of the
life. §4.7 states bound 2 once, over both classes, in one clause. It is true of one of them.

The `≥3 observations` cut is thin for property (12 firms, refused) and live for
intangibles (71 firms): **never changed 0.042 · moved once 0.197 · moved more than once
0.761.** A class where three quarters of firms revise more than once across the span is not
holding δ constant for anybody.

*The per-component row is identical across the three D2 rules by construction — a component
carries its own midpoint before any rule collapses the firm-year — so it is one measurement
printed three times, not three.*

---

## 2 · P0-b · INDUSTRY ANCHORING — §4.7's bounds 1 and 3, and the escape hatch is expensive

*ratio = within-SIC sd of log L ÷ total sd of log L, on SIC major groups clearing the 30
firm-year floor. 1.00 says industry convention explains nothing; 0.00 says it explains
everything. Bound 1 ("anchored by industry convention") and bound 3 ("can be run on
industry-median lives, at the cost of resolution") are one claim from two sides, and this
ratio **is** that cost.*

| | rule | n | SIC groups kept / refused | coverage | **ratio** | CI95 (clustered on firms) |
|---|---|---|---|---|---|---|
| PP&E | `R_MID` | 1206 | 8 / 1 | 0.984 | **0.844** | 0.808 – 0.875 |
| PP&E | `R_MIN` | 1206 | 8 / 1 | 0.984 | 0.958 | 0.933 – 0.974 |
| PP&E | `R_WEIGHT` | 1206 | 8 / 1 | 0.984 | 0.876 | 0.841 – 0.907 |
| intangibles | `R_MID` | 773 | 3 / 6 | 0.875 | **0.959** | 0.921 – 0.977 |
| intangibles | `R_MIN` | 773 | 3 / 6 | 0.875 | 0.968 | 0.932 – 0.983 |
| intangibles | `R_WEIGHT` | 773 | 3 / 6 | 0.875 | 0.968 | 0.937 – 0.983 |

**BOUNDS 1 AND 3 ARE WEAK, AND FOR INTANGIBLES THEY ARE ALMOST EMPTY.** On the most
favourable rule, industry major group accounts for **28.8 per cent of the variance** of log
property life and **8.0 per cent** of log intangible life. Everything else is within-industry.

That is a measurement of bound 1 and a *price* for bound 3 in the same number. §4.7 offers
industry-median lives as the escape from its weak joint, "at the cost of resolution."
Measured, the cost is that an industry median throws away the firm-level endogeneity *and*
keeps seven-tenths of the dispersion as within-band noise — which is the quantity §4.4 says
destroys the ranking. **The escape hatch and the hazard are the same door.**

Six of nine intangible SIC groups are refused as THIN and are not compared with anything,
per the guard `SOURCE-001` §4c earned.

---

## 3 · P0-c · WITHIN-BAND δ DISPERSION — D3's ruler, and §1.4's uncomputed input, computed

**The ruler was lifted, not rebuilt.** §4.4's simulation is extracted from
`wt088_disclosed_ladder.py` at run time by name and refuses to run unless it still prints
the manuscript's committed poles — **δ independent 0.115 · δ common 1.000 · the standards'
falling ladder 0.019**, against paper III §4.4's 0.115 / 1.000 / 0.019. One substitution is
made and only one: the δ support becomes a life band's own measured δ = 1/L.

**Run at α̂ = 0.408**, §5.4's measured recognition rate. This is not a refinement, it is the
precondition: at §4.4's calibrated α = 0.05 the entire disclosed rectangle lies outside the
model's domain. Even at the measured rate, δ ≥ α — a life under 2.45 years — still removes
**6.0 %** of property firm-years under `R_MIN` and **15.5 %** of intangible ones, counted
and excluded rather than clipped.

**PP&E, `R_MIN`** (the strongest rung; the full six-way sweep is in `RESULT-P0-run.log`):

| band width | qualifying bands | firm-yrs | coverage | recovery | worst band | distinct values/band | modal share |
|---|---|---|---|---|---|---|---|
| 0.25 y | 7 | 962 | 0.798 | 0.998 | 0.996 | **1.0** | **1.000** |
| 0.50 y | 7 | 962 | 0.798 | 0.998 | 0.996 | **1.0** | **1.000** |
| **1.00 y** | **7** | **1109** | **0.920** | **0.934** | **0.820** | **2.0** | 0.932 |
| 2.00 y | 4 | 1119 | 0.928 | 0.683 | 0.539 | 4.5 | 0.665 |
| 3.00 y | 4 | 1146 | 0.950 | 0.422 | 0.314 | 5.5 | 0.522 |
| 5.00 y | 3 | 1157 | 0.959 | 0.486 | 0.447 | 9.0 | 0.631 |
| 10.0 y | 2 | 1180 | 0.978 | 0.245 | 0.231 | 18.0 | 0.423 |
| 20.0 y | 1 | 1180 | 0.978 | 0.210 | 0.210 | 36.0 | 0.414 |
| *whole disclosed range as one band* | — | — | — | *0.201* | — | — | — |

**THE TWO RIGHTMOST COLUMNS ARE THE REASON THIS TABLE HAS THEM, AND THEY WERE NOT IN THE
DECLARED DESIGN.** A disclosed life is a round number far more often than an economic life
could be — under `R_MIN`, **87.5 % of property firm-years disclose an integer and 65.8 % one
of {3,5,7,10,15,20,25,30,39,40,50}; 46 distinct values carry 1,206 firm-years.** So at a
quarter-year band the band contains **one** distinct number, within-band δ dispersion is
zero **by arithmetic rather than by economics**, and recovery goes to 0.998 without the
design having done anything.

**Every recovery in this table is therefore an UPPER BOUND.** It is computed from the
*disclosed* δ, and the gap between the disclosed and the economic δ is precisely §4.7's
weak joint — the thing REG-009 §1.3 found unmeasured and which P0 does not measure either.
A table that printed 0.998 without that column would have been this thread's sixth
unmeasured quantifier, produced by the probe built to catch the fifth.

---

## 4 · REG-009 §4's PRE-COMMITTED STOPPING RULE, APPLIED — and an erratum in the rule

The rule, declared before the instrument existed: *if no band width achieves a §4.4 recovery
probability above 0.80 while leaving at least 30 firm-years per band, the δ design is
refused and P0's table is the result.*

**As written, the rule is cleared — by all six (tag, rule) pairs, at a 0.25-year band.**

**ERRATUM, RECORDED AND NOT REPAIRED.** The rule prices recovery and the THIN floor and says
nothing about **coverage** — the share of firm-years living in bands that clear the floor.
It is therefore satisfied by a width that recovers beautifully on a quarter of the sample:
intangibles under `R_WEIGHT` clear at 0.25 y with **coverage 0.257**. Rewriting a
pre-commitment after seeing the table is the one move a pre-commitment exists to prevent, so
the verdict stands as computed and the omission is recorded here — REG-002 E1's precedent,
where a falsifier stated on |mean τ| was left defective in the record rather than quietly
corrected.

**Held to coverage ≥ 0.80, exactly one rung survives:**

| tag | rule | width | recovery | worst band | coverage | distinct/band | |
|---|---|---|---|---|---|---|---|
| **PP&E** | **`R_MIN`** | **1.00 y** | **0.934** | **0.820** | **0.920** | 2.0 | **clears** |
| PP&E | `R_MID` | 1.00 y | 0.764 | 0.472 | 0.857 | 4.0 | refused |
| PP&E | `R_WEIGHT` | 1.00 y | 0.679 | 0.361 | 0.804 | 27.5 | refused |
| intangibles | `R_MID` | 1.00 y | 0.743 | 0.456 | 0.832 | 11.0 | refused |
| intangibles | `R_MIN` | 2.00 y | 0.615 | 0.543 | 0.834 | 15.0 | refused |
| intangibles | `R_WEIGHT` | 2.00 y | 0.600 | 0.316 | 0.921 | 44.0 | refused |

**`R_WEIGHT` is not a third rule on most of this sample.** Component carrying amounts back
it on a minority of firm-years; the rest fall back to `R_MID`. Target Corp — three component
lives, no component amounts — is one of them. The share is printed per tag in the run log
and the fallback is asserted in the tests, because a docstring promising the share would be
reported while nothing printed it is the same defect one level down.

---

## 5 · What this does and does not establish

**Establishes.** §4.7's three bounds now carry numbers instead of assertions, and they do
not all survive: bound 2 holds for property and fails for finite-lived intangibles; bounds 1
and 3 are weak for property and nearly empty for intangibles, and bound 3's escape hatch is
priced in the same quantity that §4.4 says destroys the ranking. §1.4's uncomputed input is
computed. The δ design clears its own pre-committed threshold on **one** (class, rule, width)
combination that retains 92 % of its sample.

**Does not establish.** That the disclosed δ is the economic δ — §4.7's weak joint is
untouched, and it is the slack in every recovery number above. That two cycles are a series:
the intervening cycles are still unfilled, and D1's per-year weight still needs them. That
`R_MIN` is the right rule — P0 does not choose, and the reason `R_MIN` scores highest is
partly that it heaps hardest, which is an argument about the disclosure and not about the
rule. And nothing here touches σ, which is REG-010's.

**The one thing a reader should carry out of this document:** the design's recovery is high
exactly where the life band has stopped being a band and become a single disclosed integer.
That is not a defect in the design — stratifying on the disclosed number is what §4.7
proposed — but it relocates the whole question onto the disclosure's fidelity, which is the
bound nobody has measured yet and which P0 was not built to measure.
