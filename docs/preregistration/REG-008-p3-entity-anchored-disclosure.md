# REG-008 · Instrument registration · the ENTITY-ANCHORED trigger sentence, and the one probe that spent its own confirmatory status

- **Session:** `wealthTensor-22`, 2026-08-13.
- **Status at the time of writing:** committed and pushed **alone**, before a line of `wt096`
  exists. Two feasibility probes have been run against the committed REG-007 corpus and both are
  reported in §2 — **including one that conditioned on the arm label and therefore forfeited the
  confirmatory status of the statistic it touched.** §2.6 is that disclosure. It is the reason
  this registration separates SEEN quantities from UNSEEN ones by name rather than by assurance.
- **Predecessor:** `REG-007` / `RESULT-REG-007`. Read `RESULT-REG-007` §2 first: the placebo is
  the finding, and it is what this instrument exists to answer.
- **Falsifier count:** ten, of which four can kill the instrument outright.
- **Network calls:** **zero.** The corpus is `data/reg-007-passages.json.gz`, already committed
  (3,704,216 bytes, `sha256 939e7bf5f11aa753e18a6604d53c7f9c09ca80e3f195744ccde6adb09f4ed761`).
  F6 pins that digest and asserts the run opens no socket.

---

## 0 · The question, unchanged; the instrument, replaced

REG-006 left two explanations standing for §5.4's off-diagonality — the standard's own co-testing
rule (`ASC 350-20-35-3C(f)`) against economic co-movement — and REG-007 built the disclosed
trigger into an instrument to separate them. **The instrument did not resolve.** Its registered
keyword families reached **0.436** inside the mandated-disclosure window and **0.403** in the
placebo, where `ASC 350-20-50-2(a)` compels nothing at all (`RESULT-REG-007` §2, read from that
table, not recomputed). Three percentage points between a population compelled to describe its
facts and circumstances and a population under no such compulsion is not a discriminator; it is a
lexicon reading prose that is present either way.

`RESULT-REG-007` §6 named the repair and refused to make it a patch:

> The next instrument is not a bigger keyword list. The registered families reach 0.436 in the
> window and 0.403 in the placebo; adding keywords moves both. What would separate them is a
> measure that only exists in event-specific narrative — the *named* reporting unit, the *dated*
> trigger, the charge amount tied to the sentence — which is a parsing problem, not a lexicon
> problem, and it is a new registration.

This is that registration. The question is REG-007's question. **What changes is the unit and the
predicate: from a 1,500-character window classified by keyword membership, to a SENTENCE
classified by whether it anchors its trigger to a named entity.**

### Why the sentence, and why the name

Boilerplate recites a *policy* and names nothing, because a policy has no particular reporting
unit and no particular date:

> *"Indefinite life intangible assets are not amortized but are tested for impairment annually or
> more frequently when indicators of impairment exist."*

Event-specific narrative cannot avoid naming, because the reader cannot otherwise tell which unit
was tested or when:

> *"…the Company recorded a goodwill impairment charge in its Private Cloud reporting unit during
> the second quarter…"*

Both sentences sit inside REG-007's window and both classify identically under its families. The
first is the placebo's 0.403 wearing the window's clothes. **The registered predicate is the
distinction those two sentences make, and nothing else.**

---

## 1 · WHAT REG-007 ESTABLISHED, AND THE ONE THING IT DID NOT SAY

Carried forward, not re-litigated:

- **The window is still the window.** Firm-years with `G > 0`, because `350-20-50-2(a)` compels
  the facts-and-circumstances description uniformly inside it and — the identification —
  independently of whether a non-goodwill charge also occurred (REG-007 §1). F10 of REG-007
  verified the mandate's scope. Nothing here reopens it.
- **The split is still the split.** JOINT = `G > 0` ∧ (`t0+t1+t2`) > 0; GOODWILL-ONLY = `G > 0` ∧
  `t0 = t1 = t2 = 0`. Read from `data/reg-006-wt092-panel.json` through the committed corpus,
  which already carries the arm label per firm-year. **The panel is not rebuilt** (REG-007 §3.1).
- **P3's asymmetry still holds and still runs one way.** An internal, accounting-generated
  trigger is the less newsworthy of the two and the one more likely to go unsaid, so a positive
  result understates and a null remains uninformative about co-movement. Re-registered below as
  P3, unchanged, because the new instrument does not repair the asymmetry — it repairs the
  *resolution*.
- **REG-007 F1's own contingency is the seed of this design.** F1 registered that a polysemy
  fraction above 15% would narrow the instrument "to sentence-level co-occurrence before anything
  else runs." It passed at 10.0%, so the narrowing was not triggered. **REG-008 adopts it anyway
  — not because F1 fired, but because the placebo says the window is too coarse for a different
  reason than F1 was watching for.** That is a design choice and it is declared as one.

**The one thing REG-007 did not say:** it did not say the disclosure is uninformative. It said
*this* instrument, on *this* unit, with *this* lexicon, could not read it — and its own placebo,
registered in advance, is what proved that. A null from an instrument that measured its own
blindness is a finding about the instrument (REG-007 §6, and the standing rule in `docs/HANDOFF.md`
§7). Building a second instrument against the same question is therefore licensed. Building a
second instrument that shares the first's failure mode is not, which is what F1 below exists to
prevent.

---

## 2 · THE FEASIBILITY PROBES, DECLARED IN FULL

Everything in §2.1–§2.5 is a property of the **instrument** or the **size of a population**,
computed with the arm label and the universe label **deleted from every row before any counting**
— enforced in code (`probe2.py`, `probe3.py`: `for k in ("arm","G","t_sum","A","universe","sic"):
r.pop(k, None)`), not promised in prose. §2.6 is the probe that did not meet that standard, and it
is reported at the same level of detail as the ones that did.

**2.1 · The corpus is what the harvest said it is, and absolute offsets are recoverable.**
1,925 firm-years, 4 misses, 9,852 passages. Each passage carries `phrase`, `at` (the offset of the
phrase in the full document text) and `text` (the ±1,500-character window). Because `at` and the
half-width are both recorded, the absolute start of every passage is exactly `max(0, at − 1500)`,
so passages from one document can be **merged on true offsets rather than glued end-to-end**.
Merging collapses 9,852 passages into **5,108 spans** — 4,744 overlaps absorbed — at a median of
2 spans per firm-year and a maximum of 15. **Sentence segmentation runs on the merged spans**, so
a sentence that straddles two overlapping windows is segmented once, not twice.

**2.2 · The window rarely truncates the sentence, and the residual is measured.** Over the first
400 firm-years, **2,208 of 2,261 phrase occurrences (97.66%)** have a sentence boundary on both
sides of the phrase *inside* the retrieved window. 53 do not. Those are the cases where the
sentence runs past the harvest edge, and F4 counts them at run time on the full corpus rather than
trusting this paragraph.

**2.3 · The registered segmenter is legible and its error mode is bounded.** A rule-based
segmenter (frozen in §3.2) applied to the trigger-bearing text of the first 600 firm-years
produces **6,139 trigger-bearing sentences**, median **218** characters, p95 **538**, max 2,801;
**3.6%** exceed 600 characters. Over-long segments are the failure signature of a missed boundary,
and F2 hand-audits a sample of them rather than accepting the 3.6% as harmless.

**2.4 · Sentence-level co-occurrence is not vacuous.** Of those 6,139 trigger-bearing sentences,
**11.9%** contain "reporting unit" in the same sentence. The predicate has a population; it is not
a share of an empty set (`METHOD-001`, and REG-007 Q2).

**2.5 · THE (f)-FAMILY LEXICON IS STANDARD-TEXT, NOT FILING-TEXT — AND THE CORRECTION
`-21` TEED UP IS ALSO DEAD.** REG-007 F2 reported two DEAD keywords and registered the handling as
*report it, do not fix it*, leaving the fix to a new registration. `docs/HANDOFF.md` §6 item 1 then
instructed this session to "fold in the two dead keywords and the corrected 'composition or
carrying amount of its net assets' wording while you are there." **Run against our own corpus,
arm-blind, the corrected wording is dead too**, and so is every variant of the subsidiary phrase
tried:

| string | firm-years |
|---|---|
| `composition of its net assets` (REG-007, transcription error) | **0** |
| `composition or carrying amount of its net assets` (the `-21` correction) | **0** |
| `composition or carrying amount` | 4 |
| `carrying amount of its net assets` | 1 |
| `recognition of a goodwill impairment loss in the financial statements of a subsidiary` | **0** |
| `impairment loss recognized in the financial statements of a subsidiary` | **0** |
| `financial statements of a subsidiary` | **0** |
| `recoverability of a significant asset group` | 20 |
| `significant asset group` | 26 |
| `tested for recoverability` | 36 |
| `asset group` | 410 |
| `held for sale` | 130 |
| `long-lived asset impairment` | 118 |
| `disposal group` | 24 |
| `carrying amount of the reporting unit` | 126 |

**Firms do not quote the Codification's words.** The two sub-item strings the standard uses for
the (f) family are absent from 1,925 filings, and the *repaired* string is absent from the same
1,925 filings — so the repair named in the handoff would have shipped a second dead keyword under
a correction's warrant. The INTERNAL family's mass is carried almost entirely by `asset group`
(410) and `held for sale` (130), which are the vocabulary of long-lived-asset **policy** prose,
not of an (f)-family event. **This is a mechanism for REG-007's null with a number attached, and
it is available before REG-008 computes anything.** It is also why §3 registers no new keywords:
the failure was never a missing string.

**2.6 · THE PROBE THAT WAS NOT A FEASIBILITY PROBE.**

The first probe run this session (`probe.py`) extracted named-reporting-unit candidates from each
firm-year's passages **and printed the rate by arm**, before this registration existed. It
returned:

| arm | firm-years with ≥1 named-unit candidate | rate |
|---|---|---|
| JOINT | 93 / 309 | **0.301** |
| GOODWILL-ONLY | 91 / 427 | **0.213** |
| PLACEBO | 87 / 1,189 | **0.073** |

**That is not a property of the instrument and it is not the size of a population. It is the
comparison.** REG-007 §2's own standard — "no quantity below is an input to any prediction in §4"
— is violated by it, and the violation is not repaired by the fact that the number came out in the
predicted direction. It is worse for having come out that way.

The consequence is stated once, here, and is binding on `RESULT-REG-008`:

1. **The pooled contrast on the named-unit marker is EXPLORATORY, permanently.** Λ_anchor is
   reported with its numbers and its p-value, labelled SEEN-BEFORE-REGISTRATION at every
   appearance including in the manuscript, and **no severity claim attaches to it.** A
   pre-registration has force only over what it has not seen; asserting otherwise here would make
   every other registration in this repo worth less.
2. **The window-versus-placebo gap is a DESIGN INPUT, not a test.** 0.250 in the window against
   0.073 in the placebo is why this instrument was chosen over the alternatives. Choosing an
   instrument because a probe favours it is legitimate and ordinary; calling the probe a
   validation afterwards is not. F1 below is therefore written as a **gate on the run**, not as
   evidence about the world.
3. **What remains genuinely unseen is enumerated in §3.5 and is where the severity lives.** The
   universe split (retail vs computer services) has **not** been inspected in any form; the two
   secondary markers have **not** been conditioned on the arm; the sentence-level restriction has
   **not** been run by arm; no precision audit exists. Those are registered as confirmatory below,
   and this session will not look at them before this file is committed and pushed.

The process finding, recorded because it is more useful than the defect: **a probe that reads the
treatment label is the experiment, whatever the file is named.** REG-007 §2's boundary —
"instrument or population size" — is correct but is enforced by judgment, and judgment ran out
inside the first ten minutes of a session that had just read a handoff whose top warning is about
exactly this class of error. The enforceable form is mechanical and is adopted from §2.1 onward:
**delete the label from the rows before counting.** A probe that cannot see the arm cannot condition
on it.

**2.7 · ADDENDUM, `wealthTensor-37`, 2026-08-14 — THE THREE PROBE FILES, NAMED. NOT REGISTERED IN
ADVANCE; WRITTEN AFTER THE FACT AND MARKED AS SUCH.**

This registration's introducing commit `b02d02e` has the subject *"the entity-anchored trigger
sentence, **registered alone**"* and it was not alone. It carried three files, disclosed here at the
paths they actually occupy:

| file, as committed | what it is | how §2 refers to it |
|---|---|---|
| `scripts/prototypes/reg008_probe_00_CONTAMINATED.py` | the probe that read the arm label and printed the rate by arm | §2.6's `probe.py` |
| `scripts/prototypes/reg008_probe_01_armblind.py` | arm- and universe-blind by construction; §2.5's lexicon table | §2's `probe2.py` |
| `scripts/prototypes/reg008_probe_02_segmentation.py` | arm-blind; §2.3's segmentation feasibility and the INTERNAL head | §2's `probe3.py` |

**The mapping is read off the files, not inferred from the order.** `reg008_probe_01_armblind.py`
and `reg008_probe_02_segmentation.py` open with the words *"REG-008 probe 2"* and *"REG-008 probe
3"*, and both carry verbatim the `r.pop` line §2 quotes as the enforcement. `reg008_probe_00` is
the one that counts by `r["arm"]`, which is §2.6's subject and its whole defect.

**And the contaminated probe's own docstring says it is clean.** As committed at `b02d02e` it reads
*"computes no statistic that any REG-008 prediction depends on. Declared in REG-008 section 2"* —
in the same commit as §2.6, which rules that what it computed is *"not a property of the instrument
… It is the comparison"* and makes Λ_anchor permanently exploratory on that ground. The file and
the registration contradict each other inside one commit, and the only thing on disk that agrees
with §2.6 is the `CONTAMINATED` suffix in the filename. The docstring is left standing: it is
evidence of what was believed at the time, and correcting it now would edit the witness. **This
paragraph is the correction.**

**Nothing here is repaired, and that is deliberate.** The commit-order violation happened; its entry
in `tests/test_registrations_precede_their_instruments.py`'s `KNOWN_VIOLATIONS` stays, asserted in
both directions, and history is not rewritten to make anything green. §2.6's rulings are unchanged
and still binding. What was missing was only that the ledger lived in the test suite while this
document went on asserting it had shipped alone — so the disclosure is added where the violation
happened, and a guard now requires it of every entry in the ledger.

---

## 3 · The registered quantities

### 3.1 · The frame

Unchanged from REG-007 §3.1 and re-read, not rebuilt: `data/reg-007-passages.json.gz`, whose rows
carry `cik`, `universe`, `sic`, `fy_end`, `arm` ∈ {`JOINT`, `GWONLY`, `PLACEBO`}, `G`, `t_sum`,
`A`, and the passage list. **The window** is `arm ∈ {JOINT, GWONLY}`; **the placebo** is
`arm = PLACEBO`. The 4 harvest misses stay missing and are printed.

### 3.2 · The segmenter, frozen

Passages are merged on absolute offsets (§2.1). Each merged span is segmented by the following
rule, fixed here and not tuned after the run:

1. Protect the period in each of these abbreviations: `U.S. U.K. Inc. Corp. Co. Ltd. LLC. L.P.
   L.L.C. No. Nos. St. Mr. Mrs. Ms. Dr. Jr. Sr. vs. etc. e.g. i.e. Fig. approx. Sec. Art. Ch. pp.
   Ph.D. A.M. P.M. Jan. Feb. Mar. Apr. Jun. Jul. Aug. Sept. Sep. Oct. Nov. Dec.`
2. Protect the period in a decimal (`\d\.\d`), in an initialism (`\b[A-Z]\.(?=[A-Z]\.)`), and in
   an initial before a capitalised word (`\b[A-Z]\.(?=\s[A-Z][a-z])`).
3. Split on `(?<=[.!?])\s+(?=["'(\[]?[A-Z0-9$])`.
4. Restore protected periods; drop empty segments.

A sentence is **TRIGGER-BEARING** if it contains at least one phrase from REG-007 §3.2's frozen
set — that set is inherited verbatim and **not extended** (`triggering event`, `triggering events`,
`impairment indicator`, `impairment indicators`, `indicators of impairment`, `indicator of
impairment`, `interim impairment test`, `interim goodwill impairment`, `events or circumstances`).

### 3.3 · The extractor, frozen

**M1 · NAMED UNIT.** Within a trigger-bearing sentence, a named reporting unit is a match of

```
((?:[A-Z][A-Za-z0-9&./'\-]*)(?:\s+(?:and|of|&|the)?\s*[A-Z][A-Za-z0-9&./'\-]*){0,4})\s+reporting unit\b
```

with leading tokens stripped while they belong to the generic list `the a an each our its their
one that this these those such any certain both all no single same other others remaining
applicable respective relevant affected two three four five of and or which whose company's
companys`, and the residue discarded if empty or itself generic. **The generic list is frozen
here.** Widening it after the run to raise precision, or narrowing it to raise recall, is a new
registration.

**M2 · DATED TRIGGER.** Within a trigger-bearing sentence: `(first|second|third|fourth) quarter`,
`Q[1-4] 20\d\d`, a month name followed by an optional day and a `20\d\d` year, or `(three|six|
nine|twelve) months ended`.

**M3 · TIED AMOUNT.** Within a trigger-bearing sentence: `\$\s?\d[\d,.]*\s*(million|billion|
thousand)?`.

**The three markers are reported separately and are never combined into an index, a score, or an
n-of-3 rule.** A composite would carry a weight nothing in the standard supports, and a threshold
on it would be a free parameter — the WT-038 error in a new costume. §6 restates this as a
prohibition because it is the most tempting move available after the run.

### 3.4 · The statistics

For marker `M ∈ {M1, M2, M3}` and arm `a`, **R_M(a)** is the share of firm-years in `a` carrying at
least one trigger-bearing sentence in which `M` matches. Every share is printed with its
denominator. Then

> **Λ_M = R_M(JOINT) − R_M(GOODWILL-ONLY)**, with an exact Fisher two-sided *p* on the 2 × 2.

and, for the gate only, **Δ_M = R_M(window) − R_M(placebo)** where the window pools JOINT and
GOODWILL-ONLY.

### 3.5 · SEEN AND UNSEEN, ENUMERATED

| quantity | status | what may be claimed |
|---|---|---|
| Λ_M1 pooled | **SEEN** (§2.6) | reported with numbers; labelled; **no severity claim** |
| Δ_M1 (window vs placebo) | **SEEN** (§2.6) | design input; drives F1 as a gate, not as evidence |
| **Λ_M1 in retail, and Λ_M1 in computer services, separately** | **UNSEEN** | confirmatory (P1) |
| **Λ_M2, Λ_M3, pooled and by universe** | **UNSEEN** | confirmatory (P4) |
| **Λ_M1 restricted to sentences that also carry an (f)-family term** | **UNSEEN** | confirmatory (P2) |
| **M1 extraction precision (F3 hand-audit)** | **UNSEEN** | instrument validity |
| Δ_M2, Δ_M3 | **UNSEEN** | reported; feed F1's gate |

**The confirmatory content of REG-008 is the replication across two universes, the two secondary
markers, and the (f)-restricted variant.** That is a smaller claim than this registration would
have made had §2.6 not happened, and stating the smaller claim is the whole point.

---

## 4 · THE SEVEN REGISTRATION QUESTIONS

**Q1 · WHICH OUTCOMES DOES THIS THRESHOLD FAIL TO SEPARATE?** (`-14`) M1 cannot separate a firm
that names its reporting unit because the trigger was specific from a firm that names it because
its house style always does — a firm-level writing habit, exactly the confound REG-007 §2.3 raised
against a single-phrase instrument — and the registered answer is the **universe replication**
(house style does not respect a SIC boundary, so a habit-driven Λ has no reason to reproduce in
both) plus **Δ_placebo**, where the same firms writing the same way with no goodwill charge sit at
a rate this probe has already measured as far lower.

**Q2 · IS THE SET I AM TAKING A SHARE OF GUARANTEED NON-EMPTY?** (`-14`) Measured, not assumed:
6,139 trigger-bearing sentences in the first 600 firm-years alone, 11.9% of them naming a reporting
unit (§2.3, §2.4), and every share below prints its denominator.

**Q3 · WHICH VALUES CAN THIS INSTRUMENT NOT PRODUCE, AND DOES MY ESTIMATOR ASSIGN THEM MASS?**
(`-15`) It cannot produce a value for a firm-year with no trigger-bearing sentence at all; those
are a **SILENT** row with its own count, never folded into "does not name" — REG-007 F5 paid for
that distinction and REG-008 inherits the fifth cell rather than re-deriving it.

**Q4 · CAN THIS GUARD TELL AN EXHAUSTED TAIL FROM AN UNDERFLOWED ONE?** (`-16`) The corpus is
fixed and pinned by digest, so no query can truncate; the live version of this question is the
harvest **window** edge, and F4 measures the sentences the edge truncates instead of assuming
§2.2's 2.34% holds on the whole corpus.

**Q5 · IS THIS CONSTANT READ FROM THE TABLE THAT PUBLISHED IT, OR RECOMPUTED FROM ITS INPUTS?**
(`-17`, `-21`) **0.436 and 0.403 are read from `RESULT-REG-007` §2's table and never recomputed**,
and F5 asserts they appear there. `-21` closed a defect where a run's *read* list was audited and
its *write* list did not exist; `tests/test_cell_provenance.py` now covers §5.4, and F5 extends the
same discipline to every REG-007 constant this registration prints.

**Q6 · DOES EVERY IDENTIFIER I NAME ACTUALLY RESOLVE TO SOMETHING IN MY OWN SAMPLE?** (`-18`)
§2.5 is that audit, run before this file was written, and it is the reason no new keyword is
registered: three of the strings a naive repair would have added resolve to **zero** firm-years.
F7 re-runs the resolution audit at run time and writes it to a committed file.

**Q7 · DOES EVERY FALSIFIER AGREE WITH THIS REGISTRATION'S OWN HEDGES?** (`-18`) Checked before
running: no falsifier demands a magnitude this document hedges, and in particular F1 asserts a
**gate**, not a finding, because §2.6 already spent that quantity's evidential value.

---

## 5 · The registered predictions

**P1 · SEQUENCING, REPLICATED.** Λ_M1 > 0 in **both** universes separately. This is the
confirmatory prediction. Pooled positivity is already known (§2.6) and is not evidence for it: a
pooled difference can be carried entirely by one universe, and P1 fails if it is.

**P2 · THE (f)-RESTRICTED VARIANT AGREES.** Λ_M1 restricted to trigger-bearing sentences that also
carry an (f)-family term is positive and of the same sign as the unrestricted variant. If the
anchoring effect survives only when the (f) vocabulary is removed, M1 is reading narrative
specificity in general and not an accounting-generated trigger.

**P3 · THE ASYMMETRY, RE-REGISTERED UNCHANGED.** `350-20-50-2(a)` mandates *a* description, not
that the description name the proximate trigger, and the omission runs one way. **Λ > 0 is
evidence for sequencing at a strength the magnitude understates; Λ ≈ 0 is NOT evidence for
co-movement.** Stated before the run, as in REG-007 §5.

**P4 · THE SECONDARY MARKERS DISCRIMINATE LESS THAN THE PRIMARY.** Λ_M2 and Λ_M3 are positive but
smaller than Λ_M1, because a date and a dollar amount attach to *any* charge narrative while the
unit name attaches to the *test*. If either exceeds Λ_M1, the design's reading of what makes a
sentence event-specific is wrong and §7's manuscript sentence is rewritten accordingly.

**P5 · NO MAGNITUDE IS PREDICTED.** No threshold on any Λ is registered. The registered claims are
a **sign**, a **significance level**, and a **replication**.

---

## 6 · What this registration explicitly does NOT do

- It does **not** extend the phrase set, the INTERNAL family, or the EXTERNAL family. §2.5 shows
  the failure was never a missing string, and REG-007 §3.3's families are frozen where they stand.
  **In particular it does not "fix" the two dead keywords**: the repair named in `docs/HANDOFF.md`
  §6 is itself dead in our sample, and shipping it would add a third zero-hit string under the
  authority of a correction.
- It does **not** combine M1, M2 and M3 into an index, a score, or an n-of-3 rule (§3.3).
- It does **not** rebuild the panel or re-crawl EDGAR. F6 asserts both mechanically.
- It does **not** claim confirmatory status for Λ_M1 pooled or for Δ_M1 (§2.6, §3.5).
- It does **not** touch `TIER_TAGS`, `edgar.py`, `wt093`, or any PRE-001 constant; `wt096` is
  additive and reads only committed data.
- It does **not** revisit ladders A, A3, R, or REG-007's Λ, and does not read any of their nulls as
  evidence about the world.
- It does **not** proxy σ or asset lifetime (WT-038, a three-time payer).
- It does **not** reopen the two retail PP&E × intangible cells (`-20` ruling, `RESULT-REG-006`
  §2.2) or §4.4's table (`-18` ruling).

---

## 7 · The manuscript repairs this registration commits to, whatever Λ returns

Committed now, so the writing is not contingent on the result:

1. **§5.4 and Limitation 9 gain one sentence and lose none**: that the disclosed trigger was tested
   as a discriminator and that the instrument's own placebo showed it reads accounting-policy
   prose. Under the charter's non-increasing-hedge invariant this **replaces** the weaker
   disclosure sentence rather than supplementing it.
2. **The (f)-family lexicon finding of §2.5 lands regardless of Λ** — that the Codification's own
   sub-item language appears in zero of 1,925 filings — because it is the mechanism behind
   REG-007's null and it is checkable from committed data by any reader.
3. **The three corrections of `RESULT-REG-007` §4 stay as they are** (35-3F not 35-3C; 35-31 is
   four sentences; IAS 36 ¶104 and 350-20-35-31 run in opposite directions and are never cited for
   each other). REG-008 adds nothing to them.
4. **`RESULT-REG-008` reports every Λ once, with denominators, with SILENT printed beside them, and
   with the SEEN/UNSEEN column of §3.5 reproduced verbatim.** If a cell is too thin (§9), the
   counts are published and the ratio is withheld — the REG-004/005/007 precedent.

---

## 8 · Falsifiers

Each runs **before** any Λ is computed, in the order listed. Each carries a `severity.check`
witness: a **zero-argument callable** returning the same predicate evaluated on a world where the
claim is FALSE, which must come back **falsy**, and whose falsifying world must be **runnable**.
The call site copied is `scripts/wt092_sequencing_vs_coupling.py:172`, not the signature.

**F1 · THE PLACEBO GATE.** Δ_M1 = R_M1(window) − R_M1(placebo) must exceed **0.033**, the
REG-007 gap read from `RESULT-REG-007` §2's table. **If the new instrument does not separate the
compelled population from the uncompelled one by more than the instrument it replaces, it has not
improved on it and every Λ is withheld.** This is a gate on the run, not evidence about the world
(§2.6). *Kills the instrument.*

**F2 · SEGMENTATION.** Hand-audit 60 trigger-bearing sentences drawn at random (seed 20260813)
with the over-length stratum (> 600 characters) sampled at its true rate. **If more than 10% carry
a boundary error that changes marker membership — a merged sentence that imports a name from its
neighbour, or a split that severs one — the segmenter is refuted and the unit reverts to the
merged span.** Verdicts committed to `data/reg-008-segmentation-audit.json`. *Kills the unit.*

**F3 · M1 PRECISION.** Hand-audit 60 M1 extractions (same seed). **If more than 15% are not
genuine reporting-unit designators, M1 is refuted and Λ_M1 is withheld** — the families are not
narrowed to make this pass, which is REG-006 F4b's rule. Verdicts committed to
`data/reg-008-m1-audit.json`. *Kills the primary marker.*

**F4 · WINDOW-EDGE TRUNCATION.** Count trigger-bearing sentences that touch a merged span's edge.
**If more than 5% do, the sentence unit is contaminated by REG-007's harvest geometry** and the
affected firm-years are reported as a separate row rather than classified. §2.2 measured 2.34% on
a 400-firm-year slice; this asserts it on all 1,925. *Kills a subpopulation.*

**F5 · CONSTANT PROVENANCE, READ AND WRITE.** Assert that every REG-007 constant printed by
`wt096` (0.436, 0.403, 0.033, 244, 281, 644, 1,189) appears in `RESULT-REG-007`, **and** that
every constant `wt096` writes into `RESULT-REG-008` is either read from a named committed table or
computed by `wt096` in the same run. `-21`'s defect was a complete read list beside a
non-existent write list. *Kills the report.*

**F6 · NO RE-CRAWL, NO REBUILD, NO NETWORK.** Assert `sha256(data/reg-007-passages.json.gz)` ==
`939e7bf5f11aa753e18a6604d53c7f9c09ca80e3f195744ccde6adb09f4ed761`, that `wt096` imports no
network module, and that `data/reg-006-wt092-panel.json` is not opened. REG-007 §3.1 forbids the
rebuild in writing; this asserts it in code. *Kills the run.*

**F7 · RESOLUTION, RE-RUN.** Every registered phrase, every INTERNAL and EXTERNAL keyword, and
every M1/M2/M3 pattern is run against the corpus and its hit count written to
`data/reg-008-resolution-audit.json`. **Any pattern with zero hits is reported as DEAD by name in
`RESULT-REG-008`.** §2.5 predicts four of them. *Kills nothing; makes EMPTY distinguishable from
ABSENT.*

**F8 · THE ARM LABEL IS NOT READ BY ANY FALSIFIER THAT DOES NOT DECLARE IT.** `wt096` computes
**F2–F7** from rows whose `arm`, `universe`, `sic`, `G`, `t_sum` and `A` keys have been deleted,
and raises if any of those functions touches a deleted key. **F1 is the single declared exception**
— the placebo gate is arm-conditional by construction, it is the SEEN quantity of §2.6, and it
receives the arm label and nothing else: never the universe label, which P1 depends on and which
remains unseen until F1–F10 have passed. **This is §2.6 promoted from a lesson to a mechanism**,
and it is the one falsifier whose subject is the analyst rather than the filings. *Kills the run.*

> **ERRATUM, 2026-08-13, before `wt096` existed and before any statistic below had a value.** As
> first written this falsifier said "computes F1–F7 from arm-blind rows", which F1 cannot do: the
> placebo gate is a comparison between arms. The inconsistency was found while writing the
> instrument and is corrected here rather than resolved silently in code — a registration that
> contradicts itself gets amended in public, dated, with the reason, or it is not a registration.
> Nothing else moved; F1's threshold, its status as a gate, and §3.5's SEEN/UNSEEN table are
> unchanged. `git log -S` dates this edit, which is the check `-21` established for exactly this.

**F9 · THE UNIVERSE SPLIT IS COMPUTED ONCE.** Assert that the retail and computer-services cells
are computed in the same pass as the pooled figure and printed together, so that a thin cell
cannot be discovered and then re-cut. REG-007 F8's control-and-placebo-in-one-pass rule, applied
to the split that carries P1. *Kills the interpretation.*

**F10 · SILENT IS ITS OWN CELL.** Assert that firm-years with no trigger-bearing sentence are
counted as `SILENT` and never enter a denominator as "does not name". REG-007 F5's correction,
inherited as an assertion rather than as a memory. *Kills the result.*

---

## 9 · Stopping rule

`wt096_entity_anchored.py` is written after this file is committed and pushed **alone**. It runs
F1–F10 in order, aborting on any falsifier marked *kills the run*, then computes the statistics of
§3.4, then writes `RESULT-REG-008`.

**If either arm carries fewer than 30 firm-years in either universe, P1's replication is reported
as underpowered, the counts are published, and no significance claim is made for that universe.**
Declared now, so that a thin cell is a result and not a temptation.

**If F1's gate fails, no Λ is printed at all** and `RESULT-REG-008` is written as a population
report plus §2.5's lexicon finding plus §7's repairs — all of which land regardless, and the
second failed instrument is reported as plainly as the first. Two failed instruments against one
question is a finding about how much of this mechanism the disclosure can carry, and REG-007 §6
would have to be rewritten to say so.
