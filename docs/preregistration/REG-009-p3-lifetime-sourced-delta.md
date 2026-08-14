# REG-009 · The lifetime half: a sourced δ, and the four decisions that precede a hypothesis

*wealthTensor-27 · 2026-08-13 · written against `SOURCE-001` §§3a/3b/4c, paper III §§4.4/4.7/4.8,
and `RESULT-REG-003` §4.*

**§1 IS COMMITTED HERE ALONE. THIS FILE DOES NOT YET LICENSE A RUN.** No hypothesis is
pre-committed below and no falsifier is declared; §§2–8 are deliberately absent. What §1 does is
choose the arm, fix the design decisions that a hypothesis would otherwise silently assume, and
declare one pre-condition probe with its price. The registered quantities are written after that
probe reports — in a commit whose whole content is this file's continuation, before the instrument
exists, per the standing rule that a pre-registration must precede the instrument's *code* and not
merely its *result*.

> **NOTE, `wealthTensor-29`, 2026-08-14 — THIS PARAGRAPH IS SUPERSEDED AND IS KEPT AS THE RECORD.**
> Part II below commits §§6–12 and this file now licenses a run. The paragraph above said "§§2–8 are
> deliberately absent" while §§2–5 already existed, and that was true of the *registration template's*
> slots and false of this file's own numbering — a collision nobody would have noticed until they
> tried to write into it. **Resolved by addition, not by renumbering:** §§0–5 keep their addresses,
> because `RESULT-P0` §4 cites "REG-009 §4", `tests/test_reg009_design.py` cites §1.3, and
> re-addressing a pre-commitment after seeing its result is the move a pre-commitment exists to
> prevent. **The map:** §0–§1 the arm and the four decisions · §2 the P0 probe · §3 definition of
> done · §4 the pre-committed stopping rule for P0 · §5 errors in flight · **§6 D2/D3/D4 fixed ·
> §7 registered quantities · §8 the seven registration questions · §9 registered predictions ·
> §10 out of scope · §11 falsifiers · §12 stopping rule.**

---

## 0 · What SOURCE-001 handed this document

`SOURCE-001` is finished. Its §6 steps 1, 2, 3 (as reframed), 4 and 5 are run, and its own closing
ruling is that the next move is a design step rather than a measurement. It hands over a priced
split rather than an open one:

| | **δ — the lifetime half** | **σ — the volatility half** |
|---|---|---|
| source | disclosed useful lives, **0.82** coverage (§3a, §3b) | equity returns on a dominant-asset restriction (§4a–§4c) |
| population | thousands of firm-years across 2013–2025 | **40 firms** at a \$10M materiality floor |
| currently listed | not required | **13 of 40** |
| median last balance sheet | not required | **2016** |
| §2 objections outstanding | see §1.2 — **three, and each occurs once** | count 1 measured and **against** the design; count 3 **not measured** |
| what the outstanding measurement costs | one more pass over six named zips per cycle | a **delisted-inclusive market price series** — a purchase, unreachable from the container |
| does §5's selection problem bind? | **no** — §5 is an argument about σ's observability | yes, and it is the whole difficulty |

## 1 · THE ARM: δ

**REG-009 registers the lifetime half.** The reasons run in increasing order of how much they
decide.

**1.0 · Sample size is the weakest of the three reasons, and it is stated first so it is not
mistaken for the argument.** δ has thousands of firm-years and σ has 40 firms at a floor that
§4c chose in order to *price* the choice rather than to make it. That is a real difference and it
is not why this document chooses δ, because a small clean sample beats a large dirty one and
nothing above establishes which is which.

**1.1 · §5 does not bind on δ, and that is structural rather than lucky.** §5's disjointness —
*the region where σ is observable is close to disjoint from the region where the σ result bites* —
is an argument about which assets carry their own price series. It says nothing about lives, and
`SOURCE-001` §6's step 4 already recorded that the two halves stopped being symmetric the moment
§3a found a δ source. Choosing σ requires resolving §5 first; choosing δ does not require
resolving it at all.

**1.2 · The decisive reason is what each arm's outstanding measurement COSTS.** Both arms have an
unmeasured admissibility question. They are not comparable in kind:

- **σ's count 3** (growth options) needs market-to-book at each matched period end, hence a
  delisted-inclusive price source of the CRSP/Compustat class. §0 of the handoff establishes there
  is **no free equity price series reachable from the container** — Yahoo is network-blocked and
  stooq serves a challenge page. That measurement is a **purchase order**, and it has never been
  quoted a price.
- **δ's outstanding bounds** (§1.3) need the disclosed life *values* from the same six FSN notes
  zips per cycle that §3b already names by filename. That measurement is a **re-read**.

One arm is blocked on procurement and the other on an afternoon of compute. That is the whole
ruling, and it would survive even if the sample sizes were reversed.

### 1.3 · THE FINDING THIS SESSION OWES THE δ ARM — three bounds, each occurring exactly once

Choosing δ is not the same as δ being admissible, and the second question has an answer nobody has
looked at. Paper III §4.7 proposes disclosed useful lives as an *independent* determination of δ —
"made by the firm, audited, published, and *not* derived from the series whose timeliness is in
question" — and then, to its credit, names its own weak joint in the sharpest available words:

> **A disclosed useful life is chosen by the same management whose timeliness is being measured.**
> Audited and published is not the same as exogenous, and a firm that reports slowly may also
> amortise slowly.

It then bounds that joint with three claims and a sign:

1. useful lives are **anchored by industry convention** and by tax and regulatory schedules;
2. they are **sticky within a firm** across the horizon over which timeliness is measured;
3. the design **can be run on industry-median lives** rather than firm-specific ones, at the cost
   of resolution;
4. and the sign of any residual endogeneity runs toward finding *less* timeliness variation than
   exists, not more.

**Run `-26`'s grep tell against each.** Counts are stated **as of `e216037`, the commit this
session opened on and before §1.5's repair below moved two of them** — a count is a fact about a
corpus at a moment, and this document changes the corpus:

| needle | occurrences at `e216037` | where |
|---|---|---|
| `sticky` | **1** | paper III §4.7, the declaring sentence |
| `industry-median` | **1** | paper III §4.7, the declaring sentence |
| `endogeneity` | **1** in paper III | §4.7's sign claim (a second, unrelated, in `RESULT-REG-007`) |
| `industry convention` | **2** | paper III §4.7, and `SOURCE-001` §2 quoting it — one sentence, twice |

Every bound on the weak joint occurs exactly once, in the sentence that declares it. By the rule
`-26` paid for: **an objection with one occurrence is an objection nobody answered** — and here it
is worse-shaped than that, because the objection was raised by the paper *against itself* and then
closed with three assertions and a sign, none of them measured.

**The post-repair counts are pinned in `tests/test_reg009_design.py` per file**, so that the next
occurrence of any of them has to declare itself as a measurement or as a restatement. *An
assertion repeated is not an assertion answered*, and that test is the only thing standing between
those two.

### 1.3a · DISPOSITION, `wealthTensor-28` — the three bounds now carry numbers

*Appended, not substituted. §1.3's finding was true when it was written and the record of it stays
as it stands; what follows is what happened when someone measured. `RESULT-P0` is the evidence and
`tests/test_reg009_design.py`'s v4 discharge ledger is the thing that will notice if it goes away.*

| §4.7's bound | disposition | the number |
|---|---|---|
| 1 · anchored by **industry convention** | **MEASURED, and weak** (P0-b) | SIC major group accounts for 0.288 of the variance of log property life, 0.080 of log intangible life |
| 2 · **sticky** within a firm | **MEASURED, and it SPLITS BY CLASS** (P0-a) | 0.744 of property components carry the identical life eight years apart; 0.309 of intangible components do |
| 3 · can be run on **industry-median** lives | **MEASURED, and the price is the hazard** (P0-b) | the same ratio: an industry median discards the firm-level endogeneity and keeps ~0.71 of the dispersion as within-band noise |
| 4 · the sign runs toward *less* variation | **NOT MEASURED**, and out of scope here | — |
| §1.4's fifth adjective · δ "approximately constant" | **PRICED** (P0-c) | recovery 0.934 at a 1-year property band under `R_MIN`, coverage 0.920 — and an UPPER BOUND, because the disclosure is heaped |

**The shape moved once more, and it is worth naming.** Bounds 1 and 3 are not merely
unmeasured-then-measured; measuring them showed they are **the same quantity pointing both ways** —
§4.7 offers industry medians as the escape from its weak joint, and the dispersion that escape
leaves behind is the dispersion §4.4 says destroys the ranking. An objection and its proposed remedy
scored on one ruler, and nobody had put a number on either.

**And the sixth quantifier arrived on schedule, in this session's own instrument.** P0-c's first
table reported a recovery of 0.998 at a quarter-year band and said nothing about the disclosed life
being a round number 87.5 % of the time. The band was not homogeneous; it held ONE distinct value.
A probe built to catch adjectives promoted past their measurement had promoted one of its own inside
an afternoon — caught by asking of a suspiciously good number the question §3a's tell asks of a
suspiciously bad one: *could this instrument have produced this number for a reason that has nothing
to do with the world?*

This is the fifth wrong quantifier, and the shape has changed again. `-23` through `-25` mis-scoped
a **number**. `-26`'s two were **adjectives promoted past what any measurement licensed**. `-27`'s
are **adjectives that were correctly flagged as load-bearing, in the paper's own voice, and then
never built** — the honest naming of a weak joint was mistaken, by everything downstream, for the
answering of it.

### 1.4 · The fifth adjective is the one with a ruler already waiting for it

There is a fifth, and it is the one that decides whether the arm can run at all. §4.7's third
recommendation for the design reads:

> It **holds δ approximately constant by construction**, which is the condition §4.4 identifies.

§4.4 does identify that condition, and §4.4 has already **priced** it. Drawing 4,000 four-class
ladders: the deferral measure recovers the registered ordering in **11.5%** of them when δ is drawn
independently across classes, in **100.0%** when δ is held common, and in **1.9%** when the
standards' falling ladder is imposed. §4.4's own summary is that *δ dispersion is what destroys the
ranking and the ordering is what turns the wreckage into a reversal.*

**So the exchange rate exists and the input has never been computed.** "Approximately constant" is
a claim about residual within-band dispersion of implied δ, band width is the analyst's free
parameter, and no one has measured what any band width buys. Unlike the four quantifiers before it,
this one does not need a new instrument to become sayable — it needs a number fed into a simulation
that is already written and already committed.

### 1.5 · A citation defect, repaired here

`SOURCE-001` §2 says: *"§4.8 already argues the two coincide closely enough for δ to be read off a
disclosure; that argument is on the record and is not reopened here."*

**§4.8 does not argue that.** §4.8's claim is that the readability result is *checkable by a reader
against a disclosed useful life*, and its stated virtue is the opposite move — that it **"does not
require inferring a physical decay rate from a reporting rule."** The argument `SOURCE-001` needs
is in **§4.7**, where it appears with its weak joint attached. A reader chasing the licence lands on
a section that declines to give it, and "is not reopened here" then closes a door in front of an
empty room. *Repair: retarget the citation to §4.7 and carry §4.7's weak joint with it, so the
bound travels with the licence.* `closely enough` also occurs exactly once in the repository, which
is how this was found.

### 1.6 · THE FOUR DECISIONS §1 FIXES

The inherited handoff names one live decision. There are four, and three of them are unpriced.

**D1 · THE YEAR WINDOW.** §3b, priced. Coverage is 0.823 on the 2022–23 cycle and 0.727 on
2014–15, and the shortfall is concentrated in non-December firm-years (+0.140, z = 4.07 across the
decade, against December's +0.066). Either restrict to the recent span where coverage is uniform
across fiscal-calendar months, or carry the whole 2013–2025 span with a per-year,
per-fiscal-calendar weight. **RULING: carry the whole span with a per-year weight**, and fill the
intervening cycles first (six zips each, mechanical, `--compare` already does the arithmetic).
Reason: the δ design's power is in firm-years and the early span is roughly half of them; a
0.727-vs-0.823 coverage gap with a *measured* shape is a weight, whereas discarding the early span
to avoid a weight is a truncation nobody priced. The weight is auditable and the truncation is not.

**D2 · INTERVAL → POINT.** §3a found an explicit `Range=Minimum` / `Range=Maximum` axis on
**0.57** of dimension sets, crossed with an asset-component axis. **For the majority of firm-years
the disclosure is an interval, not a number**, and nothing anywhere in this repository says how an
interval becomes a δ. **DECLARED UNPRICED.** A midpoint rule, an endpoint rule and a
component-weighted rule are all defensible and they do not agree; which to register is decided by
P0's output, not by preference, because the quantity that matters downstream is not the point
estimate but the *dispersion*, and the three rules do different things to dispersion.

**D3 · LIFE-BAND WIDTH.** The validity condition of §4.4, the ruler of §1.4. **DECLARED UNPRICED,
ruler already built.** Band width trades residual within-band δ dispersion against firm-years per
band; §4.4's simulation converts a dispersion into a recovery probability. P0 reports the sweep.
Following §4c's `MATERIALITY_FLOORS` precedent: **the probe prices the choice, it does not make it.**

**D4 · FIRM-SPECIFIC VS INDUSTRY-MEDIAN LIVES.** §4.7's own bound 3, offered as the escape from its
weak joint at "the cost of resolution." **DECLARED UNPRICED**, and it cannot be priced before D3,
because the cost of resolution *is* a dispersion statement: substituting an industry median removes
firm-level endogeneity and adds within-band dispersion, and whether that trade is good is exactly
the number §4.4 converts.

### 1.6a · DISPOSITION, `wealthTensor-29` — D2, D3 and D4 are now FIXED

*Appended, not substituted, on §1.3a's precedent. The three DECLARED UNPRICED rulings above were
true when they were written and stay as they stand.* `RESULT-P0` priced all three and, per §2's
reporting rule, did not choose. **§6 chooses, citing the table:** D2 → `R_MID` primary with all
three rules reported in one pass (and `R_MIN` refused *because* it scores best, which is a heaping
fact rather than a rule fact); D3 → 1.00 year, property, `R_MIN`, the one rung of six that clears
§4 at coverage ≥ 0.80; D4 → firm-specific, and the industry-median variant is not run at all. D1's
ruling is unchanged and its intervening cycles are still unfilled.

## 2 · P0 — THE PRE-CONDITION PROBE, DECLARED AND PRICED

**One probe prices D2, D3 and D4 together, and measures two of §1.3's three bounds.** It is
registered here, before it is written, and it is not a hypothesis test.

**What it reads.** The same six FSN notes zips per cycle that §3b names by filename
(`2022q4` … `2024q1`, and the 2014–15 cycle's six), **reading the disclosed life VALUES and their
dimension axes** — `num.tsv` durations and `txt.tsv`'s value column, plus the component ×
`Range` axis.

**Measured this session, so nobody assumes otherwise again: §3b's committed artifacts CANNOT
answer this.** `data/source-001-lifetime-by-fyend{,-2015}.json` carry per-firm-year rows keyed
`{cik, fy_end, status, adsh, any, canon, ppe, intangible, facts}` — four booleans and a
**count of tag occurrences**. `scan_zip()` opens `txt.tsv`, filters on `"UsefulLife" in tag`, and
increments a counter; it never opens the value column and never touches `num.tsv`. The artifact
answers *was a life tagged*, not *what was the life*. **The price of P0 is therefore a re-read of
the zips, not a groupby on a file already on disk** — this paragraph exists because "cheap" was
about to be this document's own unmeasured adjective, and the rule that caught it is the one §1.3
is about.

**Siting: CLOUD, NOT DARWIN.** Settled three times; darwin was IP-flagged in `-24`. `data.sec.gov`
and `www.sec.gov` are reachable from the container.

**What it reports.**

- **P0-a · STICKINESS.** Within-firm dispersion of the disclosed life across years — §4.7's bound
  2, measured for the first time. Reported as a distribution, not a mean, and with the
  never-changed share stated separately from the moved-once share.
- **P0-b · INDUSTRY ANCHORING.** Within-SIC dispersion of the disclosed life — §4.7's bounds 1 and
  3 together, since "anchored by industry convention" and "can be run on industry-median lives"
  are the same claim measured from two sides.
- **P0-c · WITHIN-BAND δ DISPERSION, SWEPT OVER BAND WIDTH** — D3's ruler, fed into §4.4's
  committed simulation to yield a recovery probability per band width, per interval→point rule
  (D2's three candidates run side by side in one pass, so a rule cannot be discovered and then
  re-chosen).

**Guards inherited as code, not as memory.** `THIN` refuses any band or SIC cell under 30
firm-years (§3b's guard, §4b's mistake). Every quoted gap carries a two-proportion *z* or its
continuous analogue. No comparison is printed between two cells whose own rates the same function
has just refused — §4c's incoherent-guard find, promoted to an assertion. And before any median is
quoted, its **IQR is printed beside it**, and a median whose IQR spans a sign change or an order of
magnitude is reported as two populations rather than one — `-26`'s "what I would do differently,"
promoted from a lesson to a mechanism.

**Reporting rule, declared now.** P0 reports numbers. It does not choose D2, D3 or D4; those are
fixed in REG-009 §2 in a later commit, citing P0's table. A probe that both measures the choice and
makes it is the shape §4c spent a session unwinding.

## 3 · DEFINITION OF DONE

*Written because this thread has spent four sessions on a source document, and a definition of done
is the thing that ends that. Each item is checkable by someone who was not here.*

**REG-009 is DONE when all six hold:**

1. **§1 fixes D1–D4**, each with either a number attached or an explicit *declared unpriced, and
   here is why*. **D1 is fixed above.** D2–D4 are fixed in §2 after P0.
2. **P0 has run and `RESULT-P0` is committed**, carrying P0-a, P0-b and P0-c with their guards, and
   the per-firm-year records behind them, so both counts are auditable without re-reading the zips.
   **DONE, `wealthTensor-28`** — `RESULT-P0.md`, `RESULT-P0-run.log`,
   `data/reg-009-p0-lives-{2015,2023}.json` (1,296 firm-year records), `data/reg-009-p0-result.json`.
3. **§§2–8 are committed ALONE** — registered quantities, the seven registration questions, the
   registered predictions, the falsifiers with their *kills the run / kills the marker / kills the
   interpretation* verdicts, and a stopping rule — **in a commit that ships no instrument code.**
   **DONE, `wealthTensor-29`** — the slots landed at **§§6–12**, not §§2–8, because §§2–5 were
   already occupied when this item was written; see the header note. The five artifacts item 3
   names are what was checked, and they are all present.
4. **The instrument runs and `RESULT-REG-009` is committed**, reporting what was registered and
   what happened, in that order.
5. **Paper III §4.7's three bounds each carry a disposition** — a measurement, or an explicit "not
   established, and here is what the design does instead." §1.3's finding is not discharged by
   REG-009 choosing δ; it is discharged by the bounds getting answers or getting scope.
   **DONE, `wealthTensor-28`** — see §1.3a. Three measured, one (the sign) explicitly out of scope
   and marked as such rather than left to look answered.
6. **§1.5's citation repair is applied** to `SOURCE-001` §2 and any downstream text that inherited
   it.

**EXPLICITLY NOT IN SCOPE, so that finishing is distinguishable from stopping.** The σ arm; count 3
and its price series; §5's choose-your-shape between *estimate the exponent on the observable
region* and *make the truncation the instrument*. Those are **REG-010**, and they are named here so
that REG-009 closing does not read as the σ question closing. `SOURCE-001` §5 stands untouched and
unanswered.

## 4 · STOPPING RULE, PRE-COMMITTED

**If no band width achieves a §4.4 recovery probability above 0.80 while leaving at least 30
firm-years per band, the δ design is refused and P0's table is the result.** Published as a
population report, with the refusal stated in the same sentence as the number that caused it.

The threshold is a choice and is defended rather than derived: §4.4's own poles are 1.000 at δ
common and 0.115 at δ independently dispersed, so 0.80 sits nearer the clean pole than the midpoint
and leaves room for a design that is good but not perfect, while 30 firm-years is §3b's inherited
`THIN` line rather than a new number invented to make this pass. **Declared before P0 runs, so that
a bad dispersion is a finding and not a temptation** — and per §4c's precedent, a refusal that
arrives with its number attached is worth more to the next reader than a design that quietly widens
its bands until the number complies.

## 5 · Two errors made in flight, kept because both tells are cheap and general

**The word "cheap" was this document's own unmeasured adjective, and it survived about ten
minutes.** §1.2's ruling rests on δ's outstanding measurement being a re-read rather than a
purchase, and the first draft of that sentence said the dispersion probe was a groupby on
`data/source-001-lifetime-by-fyend.json`, which is committed and on disk. It is not: those rows
carry four booleans and a tag *count*, and `scan_zip()` never opens a value column. **The document
diagnosing unmeasured adjectives was one paragraph from shipping one**, in the sentence that
carries its central ruling. The ruling survives — a zip re-read is still not a purchase order —
but it survives at a price that was checked rather than assumed, and §2 now states that price.

**The test that holds §1.3 failed on its own author twice, and the SECOND failure was the useful
one.** `tests/test_reg009_design.py` greps the repository for each bound.

- **v1 pinned a corpus total** and failed instantly, for two reasons that are both self-reference:
  the test names every needle in its own parametrisation, and §1.5's repair *restates* the three
  bounds while flagging them unanswered. That second one is the deep one — **to a raw count, a
  repair that propagates a finding and a restatement that ignores it are identical.**
- **v2 pinned per-file counts** and failed again the moment this session's handoff reported the
  finding. **That is the signal to redesign, not to keep appending to an exclusion list.** A guard
  whose only maintenance is exclusions is on its way to being ignored — the doctrine's
  permanently-red check, arriving in a new costume and looking like diligence.
- **v3 holds the two things that are actually invariant.** *The anchor:* each bound occurs exactly
  once **in paper III**, in §4.7's declaring sentence — if that moves, §1.3 is a finding about a
  sentence that no longer exists and must be re-decided rather than re-pinned. *The measurement
  homes:* no bound appears in `scripts/`, `data/` or a `RESULT-*`, **because that is where a
  measurement would land and nowhere else.** Design documents are not counted at all; discussing
  this is their job.

The general form, and it cost two iterations to see: **when a guard fires on legitimate propagation
twice, the guard is measuring the wrong thing.** The first firing is information about the code; the
second is information about the guard.

---

*§1 is written against `SOURCE-001` §§3a/3b/4c and paper III §§4.4/4.7/4.8. The three greps behind
§1.3 (`sticky`, `industry-median`, `endogeneity` — one occurrence each) and the one behind §1.5
(`closely enough` — one occurrence) are reproducible from the repository root and are the whole
evidence for that finding; they cost about a minute. §2's P0 is declared and not yet written, which
is the point.*

---

# PART II · THE REGISTRATION PROPER — §§6–12

*`wealthTensor-29` · 2026-08-14 · written after `RESULT-P0` reported and before any instrument for
this part exists. §§6–12 are the slots §3's item 3 calls "§§2–8": registered quantities, the seven
registration questions, the registered predictions, the falsifiers with their verdicts, and a
stopping rule. **They are numbered 6–12 because §§2–5 were already occupied when item 3 was
written** — see the numbering note in this file's header. Nothing in Part I is rewritten; §1.6a is
a dated pointer and §3's item 3 carries a dated disposition line, both appended in the §1.3a manner.*

## 6 · D2, D3 AND D4 — FIXED, CITING `RESULT-P0`'s TABLE

§1.6 declared three of its four decisions UNPRICED and named the probe that would price them.
`RESULT-P0` priced them and, per §2's reporting rule and §4c's precedent, did not choose. **This
section chooses.** Each ruling cites the table and states the reason the table alone does not
supply, because a table can price a choice and still not make it.

**D2 · INTERVAL → POINT. RULED: `R_MID` is primary; all three rules are reported side by side in
every table, in one pass, as §2 already requires.**

The rule that scores best in `RESULT-P0` §3 is `R_MIN`, and **that is not why it is refused as
primary — it is why it is refused.** P0-c measured that under `R_MIN` **87.5 % of property
firm-years disclose an integer**, 65.8 % one of eleven round values, and **46 distinct values carry
1,206 firm-years**. `R_MIN` scores highest partly because it heaps hardest, and a rule chosen on a
column that a heap inflates is an argument about the disclosure wearing the costume of an argument
about the rule. That is the shape §1.3 exists to catch, and choosing `R_MIN` on the recovery column
would have been this thread's seventh unmeasured quantifier — arriving, again, inside the document
warning about it.

Three reasons, in increasing order of how much they decide:

1. `R_WEIGHT` **cannot be primary on this population, on a count.** Component carrying amounts back
   it on both tags in **273 of the 683 paired firm-years (0.400)**; the other 410 fall back to
   `R_MID` silently. A primary rule that is a different rule on three fifths of its own sample is
   two rules sharing a name.
2. **`R_MID` is the only rule that uses both disclosed endpoints.** §1.6's D2 rests on the
   disclosure being an interval, and P0 measured the shape it takes on components: **interval
   0.512 · point 0.461 · half-interval 0.027.** Half the components carry two numbers, and a rule
   that discards one of them throws away disclosed information in a registration whose entire arm
   is *use the disclosure*.
3. **The decisive reason is that the statistic registered in §7 is a comparison between two
   tags read off the same filing**, and `R_MIN` collapses the two toward each other by construction
   — it takes the shortest life on both sides. A rule whose bias runs along the axis of the
   comparison cannot be the primary rule for that comparison. `R_MID` has no such alignment, and
   `R_MIN` and `R_WEIGHT` still run beside it, so the sensitivity is reported rather than argued.

**D3 · LIFE-BAND WIDTH. RULED: 1.00 year, on property, under `R_MIN`** — the single rung of
`RESULT-P0` §4's six that clears §4's recovery threshold while retaining a majority of its sample
(**recovery 0.934, worst band 0.820, coverage 0.920**). Two things this ruling is not:

- It is **not** a repair of §4's stopping rule. §4 prices recovery and the THIN floor and is silent
  on coverage; `RESULT-P0` §4 records that erratum and does not fix it, and neither does this
  ruling. Held to the rule as written, all six pairs clear at a quarter-year band. Held additionally
  to coverage ≥ 0.80 — a condition applied here and declared here, not retrofitted into §4 — one
  rung survives. Both readings stay in the record. REG-002 E1's precedent.
- It is **not** decorative in a design that has no bands. §7's registered statistic is evaluated
  **pointwise**, per firm-year pair, and needs no band at all. D3 is load-bearing anyway, as §7.3's
  Ψ_band: the same statistic recomputed with every δ collapsed to its 1.00-year band midpoint. **If
  a one-year rounding moves Ψ, the statistic is reading the heap rather than the ladder**, and the
  registration would rather find that out in its own robustness row than in a referee's letter.

**D4 · FIRM-SPECIFIC VS INDUSTRY-MEDIAN LIVES. RULED: firm-specific, and the reason is now a
measurement rather than a preference.** §4.7 offers industry medians as the escape from its weak
joint at "the cost of resolution"; P0-b priced that cost and found the escape hatch and the hazard
are the same door — SIC major group accounts for **0.288** of the variance of log property life and
**0.080** of log intangible life, so a median discards the firm-level information and keeps roughly
seven tenths of the dispersion as within-band noise, which is the quantity §4.4 says destroys a
ranking. **On this registration's unit the objection is sharper still.** §7's unit is a *within-firm
pair* of disclosed lives read off one filing. Substituting industry medians would assign every firm
in a group the same pair and collapse 683 pairs onto at most **8 property groups × 3 intangible
groups** that clear P0-b's THIN floor — a statistic computed on two dozen distinct points and
reported as though it had 683. The industry-median variant is therefore **not run at all**, rather
than run and de-emphasised, and §11's F9 asserts its absence.

**What the table does NOT license, stated here so a later sentence cannot borrow it.** Every
recovery, coverage and dispersion number in `RESULT-P0` is computed from the **disclosed** δ. The
gap between the disclosed δ and the economic δ is §4.7's weak joint; P0 did not measure it and was
not built to. Every number in §§7–12 below inherits that qualifier, and §11's F4 makes it an
assertion rather than a memory.

## 7 · THE REGISTERED QUANTITIES

### 7.1 · The frame

**Population.** The 1,296 firm-year records committed as
`data/reg-009-p0-lives-{2015,2023}.json`, covering `SOURCE-001` §3b's two cycles
(windows `20141031`–`20150930` and `20221031`–`20230930`). **No zip is re-read, no filing is
fetched, and no new δ source is introduced.** This registration is a computation on committed data.

**Unit.** The **firm-year pair**: one filing that discloses *both* a canonical property life and a
canonical finite-lived intangible life. Counted before this file was written, from the committed
records and nothing else:

| | 2014-15 | 2022-23 | pooled |
|---|---|---|---|
| firm-years with any canonical life | 612 | 684 | **1,296** |
| … with a property life | 567 | 639 | 1,206 |
| … with a finite-lived intangible life | 366 | 407 | 773 |
| **… with BOTH — the registered unit** | **321** | **362** | **683** |
| distinct firms carrying a pair | 321 | 362 | **577** |
| … of which appear in **both** cycles | — | — | **106** |
| pairs where `R_WEIGHT` is amount-backed on **both** tags | 122 | 151 | **273 (0.400)** |

All three D2 rules resolve on all 683 pairs. **613 firm-years carry one tag and not the other**;
they are §11's F9 row and never enter a denominator.

**Why the unit is a pair, and why that is the whole design.** §4.4's first rung is a comparison
between property and finite-lived intangibles. The manuscript evaluates it over a **rectangle** —
a 400 × 400 uniform grid on lives asserted as `LIFE_PPE = (10, 40)` and `LIFE_FIN = (3, 20)` in
`scripts/wt088_disclosed_ladder.py`, with δ₀ and δ₁ swept **independently**. A filing does not
supply a rectangle. It supplies one point, for one firm, in one year, with both coordinates chosen
by the same management on the same page. **This registration replaces a product measure on an
assumed support with the empirical joint distribution the disclosure actually has**, and that
substitution is the experiment.

### 7.2 · The δ source, and why it is trusted this far and no further

δ = 1/L, the bridge REG-002 §3.2 states and §4.4 uses. Two checks already stand behind the values,
and they are named here because a registration that leans on a prior artifact should say what makes
it load-bearing: `RESULT-P0` §0's coverage lands within **four thousandths** of §3b's on both cycles
through §3b's own firm-year join **imported rather than copied**, and P0's values reproduce
`SOURCE-001` §3a's independently hand-audited Target Corp filing component for component
(**23.5 / 8.5 / 4.5**), pinned in `tests/test_reg009_p0.py` against the filing rather than against
P0's own output. A value reader that disagreed with the registered coverage machinery would be
measuring a different population and saying so nowhere; this one does not.

**And no further.** The disclosed δ is not the economic δ. That gap is §4.7's weak joint, it is
unmeasured, and it is the slack in every quantity below.

### 7.3 · The registered statistics

Let φ = (0.80, 0.60) — property and finite-lived intangibles, **read from paper III §4.4's table**,
never re-derived. Let *g*(δ) = δ/(α − δ) and R_i = (1 − φ_i)·*g*(δ_i). The first rung **rises** when
R₁ > R₀, and the boundary in closed form is δ₁ < αδ₀/(2α − δ₀), which is
`wt088_disclosed_ladder.py`'s own line and is **extracted from that file at run time by name**, on
P0-c's precedent, so this registration cannot drift from the ruler it claims to be using.

**Ψ — THE REGISTERED STATISTIC.** The share of *admissible* disclosed pairs at which the first rung
rises, at α̂ = **0.408** (§5.4's measured recognition rate, read from that table). Reported per D2
rule, per cycle and pooled, with a **firm-clustered** bootstrap interval (577 firms carry 683 pairs;
some firms appear in both cycles).

**A — THE ADMISSIBLE SHARE.** The share of disclosed pairs with **both** δ < α̂. R is undefined
outside that region and pairs outside it are counted, named and excluded — never clipped, never
folded into Ψ's denominator.

**S — THE SUPPORT SHARE.** The share of disclosed pairs falling inside the manuscript's asserted
rectangle, L₀ ∈ [10, 40] and L₁ ∈ [3, 20]. This measures the assumption directly rather than
arguing about it.

**Ψ_rect(α) — THE BRIDGE, AND IT IS NOT OPTIONAL.** The manuscript's own computation — the uniform
400 × 400 grid on the asserted rectangle — re-run at three rates in the same pass: **α = 0.05**
(the calibration, where the admissible rectangle is empty and the manuscript reports 0.0 %),
**α = 0.35** (the rate at which `wt088`'s labelled EXTENSION produces the **99.7 %** the manuscript
quotes), and **α̂ = 0.408** (the measured rate, at which nothing has been reported anywhere).
**Without Ψ_rect(α̂), a difference between Ψ and 99.7 % cannot be attributed**: it could be the
disclosure, or it could be the recognition rate. Asking that question of a number *before* it
exists is the same question `-28` had to ask of a number that looked good afterwards.

**Ψ_band — THE HEAPING ROBUSTNESS ROW.** Ψ recomputed with each δ collapsed to its D3 band
midpoint (1.00 year). Printed beside Ψ, never instead of it.

**Reported beside every Ψ, in the same table:** the number of **distinct disclosed pairs** behind
it and the **modal pair's share**. `RESULT-P0` §3 reported a recovery of 0.998 on a band holding
one distinct value; that column is why the reader could tell. A share computed over 683 rows
carrying a dozen distinct points is not a share over 683 independent facts, and the table has to
say so itself.

### 7.4 · SEEN and UNSEEN, enumerated

**SEEN before this file was committed**, and therefore spent as evidence:

- the counts in §7.1 — every denominator, and the 0.400 `R_WEIGHT` backing share;
- everything `RESULT-P0` published: P0-a's stickiness splits, P0-b's variance shares, P0-c's
  sweep including the heaping columns, and §4's six-rung table;
- `wt088`'s constants and its printed 0.0 % / 99.7 % / 0.611, and paper III §4.4's φ, DELTA and
  boundary arithmetic;
- §7.5's event counts.

**UNSEEN, and each is a registered quantity above:** Ψ, A, S, Ψ_rect(α̂), Ψ_band, the distinct-pair
and modal-pair columns, the empirical support of either life within the paired subsample, and the
within-firm dependence between the two disclosed lives. **No value of any of these has been computed
by this session.** The feasibility probes deliberately printed counts and nothing else — no life
value, no percentile, no correlation — because looking at them spends them (REG-008 §2.6's
precedent, applied to this session's own hands).

### 7.5 · THE DESIGN §4.7 RECOMMENDS IS NOT THIS ONE, AND THE REASON IS A COUNT

§4.7's second repair proposes a design that "uses disclosed useful lives as an independent δ, and
compares timeliness only within a life band," and adds that **"it runs on the sample §5 already
collected."** That last clause is a feasibility claim, it is stated once, and until this session
nobody had counted it. Counted, from `data/pre-002-events.json` joined to the committed lives:

**The class has two counts, and printing one of them would have been the mistake this
section is about.** `data/pre-002-events.json` is §5's sample as §5 collected it — and its tier-0
tag list is the one `REG-006` found defective and repaired, the omission §5.4 records as "a tier
whose tag list omitted the element most filers use for it." Both counts, on the same crawl:

| tier | §5 as collected: events / firms | joinable | `REG-006`-repaired: events / firms | joinable |
|---|---|---|---|---|
| 0 · property, plant and equipment | **55 / 38** | 36 / 26 | **151 / 98** | **110 / 72** |
| 1 · finite-lived intangibles | 136 / 91 | 71 / 48 | 135 / 91 | 71 / 48 |
| 2 · indefinite-lived intangibles | 81 / 47 | 0 — no life is disclosed | 78 / 47 | 0 |
| 3 · goodwill | 423 / 234 | 0 — no life is disclosed | 415 / 234 | 0 |
| all | 695 / 307 | 107 (0.154) | 779 / 307 | 181 (0.232) |

**Read the repaired column: 151 events across 98 firms, 110 of them joinable.** The joinable figure
is limited by P0 covering two cycles out of a 2012Q2–2026Q2 event span, so filling the coverage
series raises it; **the 151 is the whole property population of that crawl and no coverage fill
moves it.** D2, D3 and D4 all select property, §4's coverage-held rung is property, and §4.7's
design compares timeliness *within a life band* — so those events have to survive being **divided
across bands**, against §3b's inherited THIN floor of 30 **per band**. P0-c's one surviving rung
holds 7 qualifying bands at a 1.00-year width. **151 events over 7 bands averages 21, and the bands
are not equal**: the disclosure heaps, so the modal band would clear the floor and most of the
others would not.

**The verdict is MARGINAL, not refused, and the distinction is the whole value of having counted.**
One or two bands may clear; a design registered on "compare within a life band" and delivered as
"one band cleared" is a different paper from the one §4.7 proposes. That is a design question with a
number attached, which is what it did not have an hour ago.

**This is the seventh unmeasured quantifier, and it is in the repair rather than in the critique.**
The six before it were adjectives inside arguments the paper was making; this one is inside the fix
the paper proposes for them, which is the harder place to look and the more expensive place to be
wrong.

> **AND THE MIRROR TELL CAUGHT THIS SECTION'S OWN FIRST DRAFT, which is why both columns are here.**
> §7.5 was written with the 55 alone and read as a refusal. `-28`'s rule — *ask whether the
> instrument could have produced this number for a reason that has nothing to do with the world* —
> applied to a number that looked decisive rather than to one that looked good, and the answer was
> yes: 55 is the count under a tag list this repository had already repaired. The repaired count is
> **2.7 times** larger and it changes the verdict from *exhausted* to *marginal*. **A count is a
> claim about the tag list that produced it**, and the tell now has three shapes: a number that
> disappoints, a number that pleases, and a number that settles an argument.

**This is the seventh unmeasured quantifier, and it is in the repair rather than in the critique.**
The six before it were adjectives inside arguments the paper was making; this one is inside the
fix the paper proposes for them, which is the harder place to look and the more expensive place to
be wrong.

**Repair, attached, per the charter — REPLACE and TEE UP, not a hedge.**

- **REPLACE.** The disclosed-δ arm's first runnable use is the ladder-input test registered in
  §§7.1–7.4, which the same disclosure supports at **683 pairs across 577 firms** — a population
  the within-band timeliness design does not have and cannot be given by filling coverage.
- **TEE UP, with its price quoted rather than assumed.** The within-band timeliness design is
  **feasibility-marginal on the repaired count and its price is now quotable**: join
  `reg-006-ladderC-events-corrected.json`'s 151 property events to the disclosed lives, bin them at
  D3's 1.00-year width, and count how many bands clear 30. That is one afternoon on committed data
  and no new harvest — the cheap half. Only if fewer than two bands clear does the expensive half
  arrive: a universe outside SIC 5200–5999 and 7370–7379, which is a new population and a new
  instrument rather than a re-cut of §5's, priced as a harvest on the discipline §1.2 applied to
  σ's price series. It is REG-011's, and §10 states it is out of scope here so that this
  registration closing does not read as that design closing.
- **Not absorbed.** No sentence of paper III §4.7 is hedged in response. §12 commits the manuscript
  repair, and the repair is a count in the sentence that makes the feasibility claim, or the clause
  goes.

## 8 · THE SEVEN REGISTRATION QUESTIONS, EACH ANSWERED BEFORE ANY DATA

**Q1 · WHICH OUTCOMES DOES THIS STATISTIC FAIL TO SEPARATE?** Ψ moving away from 99.7 % is
consistent with three different worlds — the asserted *support* is wrong, the uniform *measure* is
wrong, or the recognition *rate* is doing the work — and Ψ alone separates none of them. The
registered answer is that all three channels are computed in the same pass and printed together:
**S** isolates the support, the distinct-pair and modal-pair columns isolate the measure, and
**Ψ_rect(α̂)** isolates the rate. A registration whose headline number has three possible causes
and reports one of them is inviting the reader to pick.

**Q2 · IS THE SET I AM TAKING A SHARE OF GUARANTEED NON-EMPTY?** Measured, not assumed: **683
pairs, 321 and 362 by cycle, 577 distinct firms** — §7.1's table, computed from the committed
records before this file was written. Each cycle clears §3b's THIN floor of 30 by more than tenfold,
so the per-cycle replication is available rather than hoped for. Every share below prints its
denominator.

**Q3 · WHICH VALUES CAN THIS INSTRUMENT NOT PRODUCE, AND DOES MY ESTIMATOR ASSIGN THEM MASS?** It
cannot produce a value for a firm-year carrying one tag and not the other (613 of them), and it
cannot produce R for a pair with δ ≥ α̂ — a life at or under 2.45 years, which P0 counted as 6.0 %
of property and 15.5 % of intangible firm-years on its own marginal populations. Neither gets mass
in Ψ: the first is F9's own row, the second is **A**, a reported quantity rather than a discarded
one. **The manuscript's §7 row states that the disclosed rectangle is "all" admissible at
α̂ = 0.408.** That is a property of the asserted rectangle, whose shortest intangible life is three
years; it is not a property of a disclosure that contains lives shorter than 2.45 years. **A is
therefore registered as a gate on the run, not as evidence about the world** — its direction is
already forced by P0's marginal counts, and a quantity whose direction is known cannot buy severity.
REG-008 F1's distinction, inherited.

**Q4 · CAN THIS GUARD TELL AN EXHAUSTED TAIL FROM AN UNDERFLOWED ONE?** The population is two
committed files pinned by digest, so no query can truncate. The live version of the question is the
**window**: two cycles eight years apart are not a series, D1's ruling wants the intervening years,
and they are unfilled. The guard is the per-cycle replication — a Ψ that differs between 2014-15
and 2022-23 by more than its clustered interval is reported as a **series question, not a pooled
number**, and pooling is withheld rather than defended.

**Q5 · IS THIS CONSTANT READ FROM THE TABLE THAT PUBLISHED IT, OR RECOMPUTED FROM ITS INPUTS?**
φ = (0.80, 0.60) is read from paper III §4.4's table. α̂ = 0.408 and its interval [0.383, 0.432] are
read from §5.4. The boundary δ₁ < αδ₀/(2α − δ₀), the asserted rectangle, and the 99.7 % pole are
**extracted from `wt088_disclosed_ladder.py` at run time by name** and the run aborts if the
extraction stops matching or stops reproducing the committed poles — P0-c's mechanism, which caught
its own miss on its first run. Nothing above is retyped.

**Q6 · DOES EVERY IDENTIFIER I NAME ACTUALLY RESOLVE TO SOMETHING IN MY OWN SAMPLE?** The two
canonical tags, the three D2 rules, the `R_WEIGHT_backed` flag and every `wt088` symbol are resolved
at run time and written to `data/reg-009-resolution-audit.json`; anything resolving to zero is
reported **DEAD by name** in `RESULT-REG-009`. One resolution fact is already known and is a finding
rather than a failure: `R_WEIGHT` is amount-backed on both tags in 273 of 683 pairs, and §11's F3
requires that share be printed wherever `R_WEIGHT` is.

**Q7 · DOES EVERY FALSIFIER AGREE WITH THIS REGISTRATION'S OWN HEDGES?** Checked before running.
No falsifier demands a magnitude this document hedges: **A** is a gate rather than a finding because
Q3 spends its direction; **F4** asserts the upper-bound qualifier this registration states in §6 and
§7.2 rather than asserting the bound itself; and no falsifier requires Ψ to take any particular
value, because §9's predictions are directional and §12 commits the manuscript repair at every
outcome.

## 9 · THE REGISTERED PREDICTIONS

**P1 · THE DIRECTION SURVIVES CONTACT WITH THE ACTUAL DISCLOSURE.** Ψ > 0.50 under `R_MID`, in
**both cycles separately**. This is the confirmatory prediction. Its mechanism is institutional
rather than statistical — ASC 350-30 amortises finite-lived intangibles over materially shorter
lives than ASC 360 assigns to property, so δ₁ > δ₀ is what a filing presents — and P1 fails if a
majority of firms that disclose both do not present it. Pooled positivity is not evidence for P1: a
pooled majority can be carried by one cycle, and P1 fails if it is.

**P2 · THE MAGNITUDE DOES NOT.** Ψ < 0.997 under `R_MID`, with 0.997 outside Ψ's clustered
bootstrap interval. The reason is stated before the number exists: the manuscript's 99.7 % is a
uniform product measure on an asserted support, and the disclosure is neither uniform nor a product
— it heaps on round integers (P0-c: 46 distinct values over 1,206 property firm-years) and its two
coordinates are chosen by one management on one page. **P2 is a prediction against this project's
own published number**, and it is the one that can embarrass the framework rather than decorate it.

**P3 · THE HEAP IS NOT DOING THE WORK.** |Ψ_band − Ψ| < 0.05 under `R_MID`. If a one-year rounding
of every disclosed life moves the registered statistic by more than five points, Ψ is a statistic
about the granularity of the disclosure and §10 says so instead. This is the negative control, and
it is a control on *this* instrument rather than on the world.

**P4 · THE RULES AGREE ON DIRECTION AND MAY DISAGREE ON LEVEL.** Ψ under `R_MIN` and `R_WEIGHT`
lands on the same side of 0.50 as `R_MID`. A D2 rule that flips the direction of §4.4's first rung
would mean the rung is a property of the interval-collapse and not of the disclosure, which is a
larger finding than anything else registered here and is reported as one.

## 10 · WHAT THIS REGISTRATION EXPLICITLY DOES NOT DO

- **It does not measure the gap between the disclosed δ and the economic δ.** §4.7's weak joint is
  untouched. It is the slack in Ψ, in A, in S, and in every recovery number `RESULT-P0` printed.
  `RESULT-REG-009` states it in the same table as the numbers, not in a closing paragraph.
- **It does not re-test §5.1's lag gradient**, and it is not a third instrument for it. §5's
  stopping rule bars that and this registration does not touch it: no onset, no charge date, no lag
  enters any registered quantity. §7.5's counts are a feasibility disclosure about a design that is
  **not** being run.
- **It does not read φ per firm.** φ stays at the registration's (0.80, 0.60). This registration
  prices the ladder's δ inputs; the φ inputs are §4.4's and are unchanged.
- **It does not run the industry-median variant** (§6, D4), and F9 asserts the absence rather than
  leaving it to a reader to notice.
- **It does not quote a price for the property-impairing universe** §7.5 tees up. That is REG-011's,
  and naming it here is what stops REG-009 closing from reading as that question closing.
- **It does not touch σ.** REG-010's, per §3. `SOURCE-001` §5 stands untouched and unanswered.

## 11 · FALSIFIERS

Each runs **before** Ψ is computed, in the order listed, and each carries a `severity.check`
witness: a zero-argument callable returning the same predicate evaluated on a world where the claim
is FALSE, which must come back falsy and whose falsifying world must be runnable.

**F1 · THE RULER IS LIFTED, NOT REBUILT.** The boundary function, `PHI`, `LIFE_PPE` and `LIFE_FIN`
are extracted from `scripts/wt088_disclosed_ladder.py` at run time **by name**, and the run aborts
unless the extracted code reproduces that script's committed poles: admissible **0.0 %** at
α = 0.05, and the first rung rising in **99.7 %** of the admissible rectangle at α = 0.35. If
`wt088` moves, this registration is measuring against a ruler the manuscript no longer uses and must
be re-decided rather than re-run. *Kills the run.*

**F2 · THE POPULATION IS THE ONE THIS FILE COUNTED.** Assert the pair join reproduces §7.1's table
exactly — 321, 362, 683, 577, 273 — from the committed records, and that each cycle carries at least
30 pairs. A population that moved between registration and run is a different experiment.
*Kills the run.*

**F3 · `R_WEIGHT` DECLARES ITS FALLBACK WHEREVER IT APPEARS.** Assert that every table printing an
`R_WEIGHT` quantity prints the amount-backed share beside it, per tag, computed in the same pass.
`RESULT-P0` §4 established that `R_WEIGHT` is not a third rule on most of the sample; this makes the
statement travel with the number instead of living in a prior document. *Kills the marker.*

**F4 · EVERY REGISTERED NUMBER CARRIES THE UPPER-BOUND QUALIFIER.** Assert that no line of
`RESULT-REG-009` reports Ψ, A, S or Ψ_band without the disclosed-versus-economic δ gap named in the
same table, and that the phrase appears in the document's own summary rather than only in a
footnote. §6's ruling, promoted from prose to an assertion. *Kills the interpretation.*

**F5 · THE THREE RATES ARE COMPUTED IN ONE PASS.** Assert Ψ_rect(0.05), Ψ_rect(0.35), Ψ_rect(α̂)
and Ψ are produced by a single invocation and printed in one table, so a difference cannot be
discovered and then attributed to whichever channel is convenient. REG-007 F8 and REG-008 F9's
one-pass rule, applied to the attribution rather than to a subgroup. *Kills the interpretation.*

**F6 · HEAPING IS A COLUMN.** Assert that the distinct-pair count and the modal-pair share are
printed beside every Ψ, and that the run raises if either is absent. A validity statistic computed
on a coarse support is an upper bound on the thing it stands for, and the coarseness has to be in
the same table or the bound reads as the estimate. `-28` paid for this on a number that looked good.
*Kills the interpretation.*

**F7 · NO NEW SOURCE, NO NETWORK, NO ZIP.** Assert the sha256 of both
`data/reg-009-p0-lives-{2015,2023}.json`, that the instrument imports no network module, and that no
`*_notes.zip` is opened. §2 sites bulk SEC work in the cloud; this run is not bulk SEC work and must
not become it by accident. *Kills the run.*

**F8 · THE STATISTIC DOES NOT SEE ANYTHING BUT THE PAIR.** Ψ, A, S and Ψ_band are computed from rows
whose `cik`, `name`, `sic`, `adsh`, `period` and `components` keys have been deleted, and the
function raises if it touches a deleted key. **Two declared exceptions**: the `cycle` label, which
Q4's per-cycle replication requires and which is passed only to the splitting function; and `cik`,
which the clustered bootstrap requires and which is passed only to the resampler, never to the
predicate. §11's own subject is the analyst rather than the filings. *Kills the run.*

**F9 · EMPTY IS DISTINGUISHABLE FROM ABSENT, AND ABSENCE IS ASSERTED.** Assert that the 613
firm-years carrying one tag and not the other are counted as their own row, broken out by which tag
is missing, and never folded into a denominator; and assert that no industry-median variant is
computed anywhere in the run (§6, D4). *Kills nothing; makes EMPTY distinguishable from ABSENT, and
makes a refusal checkable rather than remembered.*

**F10 · NO FREE PARAMETER.** Assert that the instrument exposes no tunable that was not fixed in
this file before it was written — no adjustable rectangle, no band width other than D3's 1.00 year,
no α other than the three named in §7.3, no threshold discovered from the output. This programme has
refused a free parameter to absorb an objection six times; the seventh refusal is a test rather than
a memory. *Kills the run.*

## 12 · STOPPING RULE

`scripts/reg009_ladder_inputs.py` is written **after this file is committed and pushed alone**. It
runs F1–F10 in order, aborting on any falsifier marked *kills the run*, then computes §7.3's
statistics, then writes `RESULT-REG-009` and `RESULT-REG-009-run.log`.

**If either cycle carries fewer than 30 pairs**, the per-cycle replication is reported as
underpowered, the counts are published, and no cross-cycle claim is made for that cycle. Declared
now, so that a thin cycle is a result and not a temptation. §7.1 says it will not happen; the rule
exists because §7.1 could be wrong.

**If Ψ and Ψ_rect(α̂) agree to within Ψ's clustered interval**, the registered finding is that the
manuscript's rectangle is an adequate stand-in for the disclosure at the measured rate, **and that
is a result, reported in one sentence with its number** — not a null to be buried. The rectangle
would then be doing honest work and §4.4 would need only its α named.

**If they disagree**, the difference is attributed by S, by the distinct-pair columns and by
Ψ_rect(α̂) — never by narration.

**The manuscript repair lands at every outcome, and is committed here so that the result cannot
decide whether the paper gets fixed.** §4.4's sentence *"across the rectangle of lives disclosure
spans — ten to forty years for property, three to twenty for finite-lived intangibles — the first
rung rises in 99.7% of it"* is repaired in one of exactly two ways: the recognition rate at which
99.7 % is computed is named in the sentence and the rectangle is labelled as asserted rather than
observed; **or** the sentence is replaced by the measured share over disclosed pairs with its
denominator. §7's row on the disclosed rectangle's admissibility is repaired in the same pass, since
"all of it" is a statement about the asserted support and not about the disclosure. **This is a
REPLACE under charter §2, not a caveat**: the defensive-sentence count of §4.4 does not rise, and if
the measured number is worse for the paper the claim narrows rather than acquiring a hedge.

**And §7.5's count lands whatever Ψ returns.** Paper III §4.7's clause "it runs on the sample §5
already collected" is repaired to carry the count — **151 property events across 98 firms on the
`REG-006`-repaired tag list, 55 across 38 as §5 collected it** — or the clause is cut. The repaired
figure is the one that goes in the sentence, and the unrepaired one goes beside it, because the gap
between them is the reason the clause was never checked. A feasibility claim with a countable denominator does not get to stay
uncounted in a paper that spends §4.4 on the cost of unmeasured quantities.

**No free parameter may be introduced to reconcile Ψ with 99.7 %.** Refused six times; F10 asserts
the seventh.
