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
