# REGISTRATION · REG-012 — the band count's own edge-phase question, and the two defects in the way it was asked
*wealthTensor-38 · 2026-08-14 · registered in its own commit, ahead of the commit that carries the
instrument. `git log --follow` on this file is the ordering, and
`tests/test_registrations_precede_their_instruments.py` is what checks it.*

*Numbered REG-012 and not REG-011: §7.5 spoke for REG-011 (`"It is REG-011's"` — the universe
outside SIC 5200–5999 and 7370–7379), and that registration does not exist yet. A number taken by a
sentence is taken.*

---

## 0 · What this is, and the one thing it is not

State Machine card `1217494219393416` records a question that survived `-36`'s split: the band count
of `RESULT-REG-009-band-count-filled` places every event by which unit-width bin its firm's disclosed
property life falls in, D3's bins are half-open on the left, and disclosed lives heap on integers —
so where the edges sit could decide which side of a boundary an event lands on.

**The question is real. The instrument the card proposed for it is not admissible, and the premise
the card gave for it is about a different population.** Both are established below by reading, before
anything is computed, because a registration that inherits its motivating numbers has already spent
its own discipline. What this file registers is the replacement: a description of the heap that reads
no threshold.

**The one thing this is not:** a second reading of §7.5's floor.
`CONSTRUCTION-REG-009-coverage-fill.md` R5 — *"No band edge, band width, floor, tag or interval rule
is re-chosen in response to the number"* — is in force and is not spent here. Nothing in this
registration, its instrument, or its result reports a count of bands, compares any band's occupancy
to 30, re-places an edge, or reaches a verdict on §7.5's decision rule. **That is asserted as an
ABSENCE by the guard, not merely intended** (§5).

---

## 1 · Defect one — the premise is a statistic about another population

The card argues: *"D3's bins are half-open on the left, and 55.7 % of disclosed lives are integers
sitting exactly on a left edge. So the band count has the SAME edge-placement sensitivity Ψ_band
has."*

**The 55.7 % is not a fact about the band count's sample.** `CONSTRUCTION-REG-010-edge-convention.md`
§C2 states its population in the same sentence that reports it: *"Of the 4098 lives entering Ψ_band
across two tags and three interval rules."* `RESULT-REG-010-half-integer-banding.md` reproduces it as
the integer share of Ψ's own 683 pairs, and 683 × 2 tags × 3 rules = 4098 exactly. So the number
counts **lives**, six per pair, over both the property tag and the intangible tag, under `R_MID`,
`R_MIN` and `R_WEIGHT` together.

The band count reads none of that. Its unit is an **event**, not a life; its tag is the property tag
alone; its rule is `R_MID` alone; and each event contributes exactly one life, chosen by the
nearest-cycle pick from up to nine cycles. **Four differences, and the number was carried across all
four.** Whether the band count's own lives heap on integers at 55.7 %, or at some other share, is
unmeasured — and it is the first thing the instrument below measures, so the sentence that
commissioned this work is the first sentence it audits.

**This is a documented failure mode of this project, repeated two documents later.**
`REG-010-p3-half-integer-banding.md` §1 was written to stop exactly it — *"the population is resolved
from the cited document's own instrument, never from the sentence that cites it"* — after
`HANDOFF.md` cited §4's tee-up and directed the run at the filled 133 (State Machine
`1217494028527267`). The card at `1217494219393416` was written the same day, cites the same tee-up,
and imports a cardinality across the same boundary in the opposite direction. **A rule stated in a
registration protects the registration that states it and nothing else.** Recorded here at the scene,
and banked as a lesson.

**Repair (charter §2, REPLACE):** the population for this measurement is resolved from the cited
document's own instrument and from nothing else — §3 below.

## 2 · Defect two — the proposed instrument cannot discriminate

The card proposes: *"how much of the modal band's mass sits within w/2 of an edge, reported as a
description of the heap rather than as a second count."*

**That quantity is 100 % for every band of every sample, by construction.** A band is
`[b·w, (b+1)·w)`; for any `v` in it, `min(v − b·w, (b+1)·w − v) ≤ w/2`. Every point of a half-open
band of width `w` is within `w/2` of its nearer edge. The proposed statistic is a tautology wearing
a measurement's clothes: it would have returned 1.000, been reported as a description of the heap,
and discriminated nothing — a green number that proves nothing, which this estate holds to be worse
than an absent one because it reads as coverage.

**Repair (charter §2, REPLACE):** the descriptor of §4, which is a property of the sample's
fractional parts and is not satisfiable by construction.

---

## 3 · The population, resolved from the cited document's own instrument

The cited document is `RESULT-REG-009-band-count-filled.md`. Its instrument is
`scripts/reg009_band_count_filled.py`; its committed table is `data/reg-009-band-count-filled.json`.
The population of this measurement is **the events that instrument bins under the registered reading
— `R_MID`, cycle nearest the event — and the one disclosed property life each of those events is
placed by.**

It is obtained by running that instrument's own selection path, not by re-deriving one, and not by
reading a numeral out of prose. Concretely, and registered before the run:

- **P1.** The event set, the join, the cycle pick and the tie-break are `bc.load_events`,
  `bc.joinable`, `chronological` and `bc.bands_for` as committed. No event is added, dropped or
  re-picked here.
- **P2.** The life each event is placed by is lifted from the **same selection path** `bands_for`
  uses, not retyped beside it. `reg009_band_count.py` gains one helper that returns the (cycle,
  value) pair `bands_for` already computes internally, and `bands_for` is rewritten to consume it,
  so there is exactly one selection path in the repository and a divergence is impossible rather
  than merely unlikely. *(Retyping the selection would make this a statistic about this session's
  idea of the population — the defect `lift_band_rule()` exists to prevent, one level up.)*
- **P3.** That refactor is **behaviour-preserving or it does not ship**: both committed instruments
  are re-run in a scratch copy of the tree and their artifacts must compare **byte-identical** to
  the committed ones. The published tables are the test.
- **P4.** The run **reproduces the cited row before describing it** — the joinable count, the
  occupied-band count and the full `R_MID|near` row vector, recomputed from the committed inputs and
  compared against the committed artifact. The run stops if they disagree. This is `-31`'s own
  discipline, turned on `-32`.
- **P5.** No cardinality of this population is typed into the instrument as a literal. Every count
  reported is bound to the length of the set it counts.

**No number from the card, from `HANDOFF.md`, or from any prose sentence enters the instrument.**

## 4 · The measurement — a description of the heap that reads no threshold

Under an edge phase `s ∈ [0, 1)` — bins at `[b·w + s, (b+1)·w + s)` — an event's bin index is
`floor(v − s)`, which equals `floor(v) − [frac(v) < s]`. **The entire edge-phase behaviour of the
sample is therefore a function of the multiset of fractional parts `frac(v)` and of nothing else.**
That multiset is a description of the heap. Reporting it reads no threshold, moves no edge, and
produces no count of bands.

Registered, in this order:

- **E1 · edge mass.** The share of the population with `frac(v) = 0` exactly — lives sitting on a
  left edge. *This is the band count's own version of the number §1 says the card imported, and it
  is what settles whether the card's premise was true of this sample.*
- **E2 · granularity.** The number of distinct fractional values present, and the share on the modal
  one.
- **E3 · the fractional-part histogram itself**, every value with its share. E1 and E2 are summaries
  of it and are reported beside it, never instead of it.
- **E4 · phase rigidity.** The grouping the bins induce on the population — the partition into
  co-binned sets, ignoring the bins' labels — is piecewise constant in `s`, changing only where `s`
  crosses a distinct fractional value. Reported: the **total measure of phases `s ∈ [0,1)` whose
  induced grouping is identical to the registered one**, and the largest single interval of them.
  *A grouping, never a count; identical-or-not, never how-many-clear.*

**`w` is D3's committed 1.00-year width, lifted, not re-chosen. `s = 0` remains the registered
placement and is not moved.** The phases in E4 are the axis a description is reported along, exactly
as a coverage series is reported along cycles; no phase is adopted, promoted, or read for a verdict.

**Artifact:** `data/reg-012-band-edge-phase.json`. **Instrument:**
`scripts/reg012_band_edge_phase.py`. **Neither exists at this commit.**

## 5 · The refusals, mechanised as an ABSENCE

`-37` established that a count of sites is the one claim no anchor can contradict, and that the
repair is to assert an **absence** rather than N presences. The same shape applies to a refusal:
"this run reads no threshold" is a claim about everything the run does *not* contain, so it is
asserted that way.

The guard requires of `scripts/reg012_band_edge_phase.py`, its result document and its artifact:

- **A1.** No occurrence of the floor's value as a threshold read, and no import or use of
  `THIN_FLOOR`, `profile`, `clear_events`, `clear_firms` or `ceilings` — the names by which a band
  count is read in this repository.
- **A2.** No band-clearing count and no verdict on §7.5's decision rule anywhere in the artifact's
  keys or the result's assertions.
- **A3.** The reported counts are bound to the lengths of the sets they count, so no cardinality in
  the result can drift from the artifact that owns it.

**A1–A3 are proved by mutation in both directions** (§6): a run that reads the threshold must go
red, and a run that does not must stay green — a guard proved only in the failing direction is a
shape-matcher and cannot be told from a real one.

## 6 · Both branches, pre-committed — including what a favourable answer may mean

`-36`'s rule: the outcome that corrupts a programme is the flattering one, because nothing
downstream objects to it. Both branches are written here, before the number, and the flattering one
is written at greater length because it is the dangerous one.

**Branch R — RIGID.** The fractional parts are concentrated (a large edge mass, few distinct values),
so the grouping survives a large measure of phases, or the mass moves together rather than apart.

*This is the flattering branch, and here is the complete list of what it is allowed to mean:* the
grouping of these lives into co-binned sets is insensitive to where the edges are placed. **That is
all.** Registered now so it cannot be spent later, it does **not** mean:

  - that §7.5's count is robust. The straddle `RESULT-REG-009-band-count-filled` §4 reports —
    registered reading gives one, every other reading of the same events gives two — is created by
    the **nearest-cycle tie-break deciding 50 of the events**, a different parameter of a different
    kind. Edge phase cannot touch it, and a rigid heap must never be reported as though it had.
  - that §4.7's within-band design is supported. It is not supported, by
    `RESULT-REG-009-band-count-filled` §4, and this measurement does not reach that question.
  - that a second band clears, or would clear, under any placement. No such count is computed.
  - that `R_MIN`, the earliest-cycle pick, the latest-cycle pick or the later-disclosure tie-break
    may be promoted. R5 stands; §6 of REG-009 refuses `R_MIN` because it scores best.
  - that the δ qualifier weakens. Every life here is a **disclosed** life and the disclosed-vs-
    economic δ qualifier stands on all of it.

**Branch F — FRAGILE.** The fractional parts are spread, so the grouping changes across most of the
phase circle.

Then the card's worry is a live one for this population, and the honest report is a **limitation of
the band count**: its placement of events into bands depends on an edge convention the registration
fixed for a reason unrelated to this sample. **Branch F does not license the forbidden measurement
either.** R5 forbids re-edging the band count and re-reading the floor whether the heap is rigid or
fragile; a fragile answer is a disclosure written beside the count, and a card, not a permit.

**Branch N — the population does not resolve.** If P3's byte-identity fails, or P4's reproduction
disagrees, the run stops and **no descriptor is reported at all**. A descriptor of a population the
instrument cannot prove it is reading is not a weaker result; it is a different one.

**Common to all three branches, registered:** this measurement produces **no new answer to §7.5's
decision rule**, and no sentence of the manuscript's §4.7 is changed by any outcome of it. If a
future session wants to say otherwise, it needs a registration of its own and R5 in its way.

## 7 · What this cannot do

It cannot make a disclosed life an economic one. It cannot say whether the *events* would move
between particular bands under a particular shift — that computation is a re-edged band count and is
refused, not merely unperformed. It cannot reach the 18 events the fill leaves unjoined, which have
no life to have a fractional part. It says nothing about Ψ_band, whose population is the one §1 is
about. And it does not price REG-011's universe, which §7.5 put out of scope and which stays there.
