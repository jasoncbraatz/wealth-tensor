# RESULT-REG-008 · the instrument got sharper, the answer did not move, and the reason is that the disclosure does not carry the quantity

- **Registration:** `REG-008-p3-entity-anchored-disclosure.md`, commit **b02d02e**, erratum
  **9797ff3**, 2026-08-13 — committed and pushed **alone**, before `wt096` existed.
- **Instrument:** `scripts/wt096_entity_anchored.py`. **11 severe · 1 definitional · 0 vacuous.**
- **Data:** the committed REG-007 corpus, `sha256 939e7bf5…4ed761`, **read and not rebuilt**;
  1,925 firm-years, 5,108 merged spans, **7,817 trigger-bearing sentences**. Zero network calls,
  asserted by F6 rather than promised.
- **Verdict:** **every falsifier passes. The placebo gate passes at 2.2× REG-007's separation —
  the instrument really is sharper — and every registered Λ is null. P2 is not merely null but
  EMPTY, and that emptiness is the result: firms essentially never describe an (f)-family trigger
  in event-specific terms. The disclosure route to §5.4's off-diagonality is closed, and it is
  closed by a measurement rather than by an underpowered guess.**

---

## 1 · WHAT WAS REGISTERED, AND WHAT CAME BACK

REG-007's families read boilerplate: 0.436 inside the mandated-disclosure window against 0.403 in
the placebo (`RESULT-REG-007` §2, read from that table). REG-008 replaced the unit and the
predicate — from a 1,500-character window classified by keyword membership, to a **sentence**
classified by whether it anchors its trigger to a **named reporting unit**.

**The replacement worked, as an instrument.**

| | firm-years classified | M1 rate |
|---|---|---|
| mandated-disclosure window (`G > 0`) | 644 | **0.1025** |
| placebo (`t > 0`, `G = 0`) | 949 | **0.0295** |

**Δ = 0.0730 against REG-007's 0.033.** The compelled population names a reporting unit inside a
trigger sentence 3.5× as often as the uncompelled one, where REG-007's families differed by 8%
relatively. F1's gate — registered as a gate and not as evidence, because §2.6 had already spent
that quantity — passes on the first comparison it was asked to make.

**And every Λ is null.**

| statistic | JOINT | GOODWILL-ONLY | Λ | Fisher *p* | MDE₈₀ |
|---|---|---|---|---|---|
| **M1** named unit *(pooled, SEEN)* | 31 / 281 = 0.1103 | 35 / 363 = 0.0964 | **+0.0139** | 0.6013 | 0.0675 |
| M1 · pilot / retail | 17 / 153 = 0.1111 | 15 / 156 = 0.0962 | +0.0150 | 0.7116 | 0.0971 |
| M1 · replication / computer services | 14 / 128 = 0.1094 | 20 / 207 = 0.0966 | +0.0128 | 0.7131 | 0.0951 |
| **M1 ∧ (f)-term** *(P2)* | **0 / 281 = 0.0000** | **1 / 363 = 0.0028** | −0.0028 | 1.0000 | 0.0088 |
| **M2** dated trigger *(P4)* | 168 / 281 = 0.5979 | 211 / 363 = 0.5813 | +0.0166 | 0.6871 | 0.1095 |
| M2 · pilot | 86 / 153 = 0.5621 | 97 / 156 = 0.6218 | **−0.0597** | 0.2994 | 0.1566 |
| M2 · replication | 82 / 128 = 0.6406 | 114 / 207 = 0.5507 | +0.0899 | 0.1114 | 0.1552 |
| **M3** tied amount *(P4)* | 81 / 281 = 0.2883 | 100 / 363 = 0.2755 | +0.0128 | 0.7246 | 0.1001 |
| M3 · pilot | 40 / 153 = 0.2614 | 39 / 156 = 0.2500 | +0.0114 | 0.8963 | 0.1391 |
| M3 · replication | 41 / 128 = 0.3203 | 61 / 207 = 0.2947 | +0.0256 | 0.6271 | 0.1450 |

`SILENT` — firm-years with no trigger-bearing sentence at all — is its own cell throughout and
enters no denominator (F10): **28 JOINT, 64 GOODWILL-ONLY, 240 PLACEBO**.

**MDE₈₀ is printed beside every null on purpose.** The pooled M1 cell could have detected
Λ ≥ 0.068 at 80% power; each universe on its own needed Λ ≥ 0.095. The observed +0.014 is a fifth
of the smaller bar. **"We did not find it" and "we could not have found it" are different results**,
and this project has already paid for the confusion in ladders A, A3 and R.

### The registered predictions, adjudicated

**P1 · SEQUENCING, REPLICATED — NOT SUPPORTED.** The *sign* condition holds: Λ_M1 > 0 in both
universes. It is worth almost nothing at *p* = 0.71 and 0.71, and P5 registered the claim as "a
sign, a significance level, and a replication" — two of the three are missing. Reporting sign
agreement between two coin flips as a replication is the move this registration exists to
prevent, and it is not made here.

**P2 · THE (f)-RESTRICTED VARIANT — REFUTED, BY EMPTINESS.** Registered: Λ_M1 restricted to
sentences also carrying an (f)-family term is positive and of the same sign as the unrestricted
variant. **One firm-year in 644 satisfies the conjunction.** The cell is empty, so the variant
cannot agree or disagree — and an empty cell reported as "did not fire" would be a phantom tag at
section scale (`METHOD-001`, and REG-002 E4's erratum). It is reported as EMPTY. §2 is why this
is the session's real finding rather than its disappointment.

**P3 · THE ASYMMETRY — UNCHANGED AND STILL BINDING.** Λ ≈ 0 is not evidence for co-movement. It
was registered that way twice, before either run, and neither run gets to sell a null as a
finding about the world.

**P4 · THE SECONDARY MARKERS DISCRIMINATE LESS THAN THE PRIMARY — REFUTED, TWICE.** Pooled
Λ_M2 = +0.0166 **exceeds** Λ_M1 = +0.0139, and Λ_M2 is **negative** in the pilot universe while
positive in the replication. Both halves of P4 fail. The honest reading is that all three markers
are noise at these sample sizes and their ordering carries no information — which is itself the
prediction's refutation, since P4 asserted an ordering.

---

## 2 · THE FINDING: THE (f)-FAMILY VOCABULARY IS NOT IN THE FILINGS

REG-007's null was ambiguous between "the standard's channel is not there" and "the instrument
cannot see it." REG-008 removes the ambiguity from one side, and the evidence is arithmetic rather
than inferential.

**2.1 · The Codification's own words appear zero times.** Run arm-blind against all 1,925
firm-years (`data/reg-008-resolution-audit.json`, F7):

| string | firm-years |
|---|---|
| `composition of its net assets` — REG-007's registered (f) keyword | **0** |
| `composition or carrying amount of its net assets` — the correction `-21` teed up | **0** |
| `recognition of a goodwill impairment loss in the financial statements of a subsidiary` | **0** |
| `carrying amount of its net assets` | 1 |
| `recoverability of a significant asset group` | 20 |
| `asset group` | 410 |
| `held for sale` | 130 |

**The repair the handoff ordered would have shipped a third dead keyword under a correction's
warrant.** `docs/HANDOFF.md` §6 item 1 instructed this session to fold in the corrected
"composition or carrying amount of its net assets" wording; it matches nothing, because firms do
not quote the Codification. That is checked, not argued, and it is why REG-008 §6 registered *no
new keywords* before any of this was computed.

**2.2 · At sentence level the (f) family and the named unit never meet.** Zero of 281 JOINT
firm-years and one of 363 GOODWILL-ONLY firm-years contain a single sentence carrying both a
registered trigger phrase, a named reporting unit, and any (f)-family term. **A firm that names
its reporting unit and its trigger in one sentence names an external cause** — a decline in
projected cash flows, a share-price fall, a lost customer — essentially always.

That is exactly what REG-007 §5 P3 predicted would happen and registered as unfalsifiable from
the null alone. **REG-008 turns it from a hedge into a measurement**: the asymmetry is not a
possibility that weakens the null, it is a property of the corpus with a count attached. The
disclosure does not contain the quantity. A third instrument built on the same corpus would be
looking for a sentence that 644 filings do not write.

**2.3 · Eight registered patterns are DEAD in our own sample, named here.** Three (f)-family
strings above, plus five EXTERNAL keywords — `raw material`, `labor costs`, `declining cash
flows`, `decline in earnings`, `loss of a customer`. F7's contract is that a zero-hit pattern is
reported by name and cannot quietly contribute zero, which is `-18`'s dead XBRL tag mechanised for
the third registration running.

---

## 3 · THE FALSIFIERS, INCLUDING THE ONES THAT PASSED

**F1 · THE PLACEBO GATE — PASSES at Δ = 0.0730 > 0.033.** Its witness is a runnable falsifying
world: the same Δ computed between two random halves of the window (seed 20260813), which returns
a gap below the threshold. Declared a **gate, not evidence**, in advance (§2.6 of the
registration).

**F2 · SEGMENTATION — PASSES at 0/60 on the registered criterion, and the loose count is
published beside it.** Sixty trigger-bearing sentences adjudicated by hand, verdicts in
`data/reg-008-segmentation-audit.json`. The registered criterion is a boundary error **that
changes marker membership**; none does. **Eleven of the sixty (18.3%) carry a boundary
imperfection that changes nothing** — a section heading or a table stub merged into the sentence
("Goodwill Impairment Testing", "86 Table of Contents Impairment of Long-Lived Assets",
"MANAGEMENT'S DISCUSSION AND ANALYSIS…"). Read item by item, no merged heading carries an M1 name,
an M2 date or an M3 amount, so marker membership is unchanged and the registered ceiling is not
approached. **11/60 is reported because it is the number a future marker keyed on capitalised text
would have to survive, and publishing only the passing figure would hide it.**

**F3 · M1 PRECISION — PASSES at 0/60.** Sixty extractions adjudicated (`data/reg-008-m1-audit.json`).
**Every one is a genuine reporting-unit designator** — *Lucky Vitamin*, *Private Cloud*, *Schuh
Group*, *Best Buy Health*, *U.S. Hosiery*, *Gourmet Foods & Gift Baskets*, *Consumer Fit Brains*.
One capture (`For the Toys-China and Southeast Asia`) retains a leading preposition; the unit is
genuine and **the generic list is frozen, so it is reported rather than fixed.** The extractor is
the strongest component of this instrument and its precision is the reason the null can be read as
a fact about the filings rather than about the regex.

**F4 · WINDOW-EDGE TRUNCATION — PASSES at 24/1,925 = 1.25%** against a 5% ceiling. REG-007's
harvest geometry does not contaminate the sentence unit.

**F5 · CONSTANT PROVENANCE, READ AND WRITE — PASSES.** Every REG-007 constant this run prints
(0.436, 0.403, 0.033, 244, 281, 644, 1,189) is asserted present in `RESULT-REG-007`; the write
side is declared DEFINITIONAL with its reason printed, which is the escape hatch leaving a mark
rather than a silent reclassification. `-21`'s defect was a complete read list beside a write list
that did not exist.

**F6 · NO RE-CRAWL, NO REBUILD, NO NETWORK — PASSES,** after failing twice in ways worth
recording. **First failure: the guard tripped on itself** — the check searched its own source for
the forbidden names, which the source necessarily contains in order to name them. **Second
failure: the rewritten guard was VACUOUS**, and `severity.check` killed the run rather than
passing it. The cause was a `\b` inside a non-raw string fragment, where it is a backspace
character and not a word boundary, so the falsifying world did not falsify. **Both failures were
caught by machinery this project built for exactly this, and neither reached the result.** The
guard now builds the forbidden names by concatenation so it cannot match itself, and checks
`sys.modules` as well as the source.

**F7 · RESOLUTION — PASSES**, and §2.3 is its output.

**F8 · THE ARM LABEL IS NOT READ BY ANY FALSIFIER THAT DOES NOT DECLARE IT — PASSES.** The parse
runs on rows whose `arm`, `universe`, `sic`, `G`, `t_sum` and `A` keys have been **deleted**, and
the labels are rejoined by `(cik, fy_end)` only after F2–F10. This is the one falsifier whose
subject is the analyst, and §4 is why it exists.

**F9 · THE UNIVERSE SPLIT IS COMPUTED ONCE — PASSES.** Pooled and both universe cells are
produced in the same pass and printed together, so a thin cell cannot be discovered and then
re-cut.

**F10 · SILENT IS ITS OWN CELL — PASSES.** REG-007 F5's correction inherited as an assertion
rather than as a memory.

---

## 4 · THE PROCESS FINDING, WHICH OUTLIVES THE RESULT

**This session's first probe conditioned on the arm label before the registration existed.** It is
committed under its own name — `scripts/prototypes/reg008_probe_00_CONTAMINATED.py` — rather than
deleted, and REG-008 §2.6 records what it returned and what that costs. The consequences were
declared before the run and are honoured above: the pooled M1 contrast is labelled SEEN at every
appearance, the placebo gap is a gate rather than a validation, and the confirmatory content was
narrowed to the universe replication, the secondary markers and the (f)-restricted variant.

The mechanical repair, adopted from the second probe onward and promoted to F8: **delete the label
from the rows before counting. A probe that cannot see the arm cannot condition on it.** REG-007
§2's boundary — "a property of the instrument or the size of a population" — is the right rule and
is enforced by judgment; this is the same rule enforced by the type system.

The cost is real and is not hidden by the fact that the contaminated quantity came back null:
**had Λ_M1 come back large, REG-008 could not have claimed it**, and that is the correct
asymmetry. A registration is worth what it refuses.

---

## 5 · POST-HOC OBSERVATIONS, LABELLED AS SUCH

No test turns on anything in this section. It is recorded because the next registration will want
it and because REG-007's own post-hoc boilerplate note is what made this session's design possible.

- **30.4% of the 7,817 trigger-bearing sentences are matched by `events or circumstances` and by
  no other registered phrase**, and **7.9% carry forward-looking-statement or safe-harbour
  language.** The audit sample shows why: five of sixty sampled sentences are safe-harbour
  boilerplate ("we undertake no obligation to update these forward-looking statements to reflect
  events or circumstances after the date of this Report"). One of the nine registered phrases is
  substantially a safe-harbour detector. **The phrase set is frozen and was run as registered**;
  this is the audit's job, not a patch.
- **REG-007 F1's polysemy survivors are visible again**: two of sixty sampled sentences are
  genuine non-impairment triggering events — a Series E preferred change-of-control trigger and a
  Senior Notes repurchase trigger. Consistent with F1's measured 10.0%, and the sentence unit does
  not remove them.
- **The sentence restriction costs a factor of 2.4 in the M1 population** relative to reading the
  whole passage blob (0.1025 against 0.250 in the window). That is the restriction doing its job —
  a name somewhere in a 3,000-character window is not a name attached to the trigger — and it is
  why the placebo gap widened rather than narrowed.

---

## 6 · What this does and does not license

- It **does** license closing the disclosed-trigger line. Two instruments, both pre-registered,
  both with their own placebo: the first measured its own blindness, the second demonstrably reads
  better and finds the quantity absent. §2.2 is a count, not an inference. **A third instrument on
  this corpus is not warranted, and `docs/HANDOFF.md` §6 item 1 is closed.**
- It does **not** license "the co-occurrence is economic." P3 forbade that in advance, twice.
- It does **not** license any claim from Λ_M1 pooled, which was seen before it was registered.
- It **does** license the manuscript repairs of REG-008 §7, which were committed before the run.
- It does **not** revisit REG-006's cells, §4.4's table, or the `-20` and `-18` rulings.
