# REVIEW-038 — PASS A · the retrospective score, the flag adjudication, and the C-class inventory

**`wealthTensor-103`, 2026-08-24.** Pass A of `docs/DEFINITION-OF-DONE-SHIP.md` § 3.
**Read at `7b5e114`.**

> **THIS IS NOT A P7 READ AND IT ADDS NO `p7-passes.tsv` ROW.** No manuscript was read for new
> defects and none was repaired. Pass A scores what sixteen passes already found, adjudicates one
> instrument's unread output, and counts a class the truth rubric could not see. Adding a ledger row
> for it would claim a seventeenth independent read that did not happen.

**Deliverable:** `docs/SHIP-LIST.md`, CLOSED at nine entries — six S1, three S2.

---

## 1 · THE HEADLINE, WHICH IS THE MEASUREMENT THIS PROJECT HAS BEEN OWED FOR EIGHT SESSIONS

**Seventy findings across sixteen passes. Fifty-three are S1. One is S3.**

| severity | n | share |
|---|---|---|
| **S1** — the manuscript states something that is not true | **53** | **75.7 %** |
| **S2** — the manuscript asserts something nothing supports | 16 | 22.9 % |
| **S3** — precision, taste, honest imperfection | **1** | **1.4 %** |

### 1.1 · Is severity falling while the count is flat? **NO. NEITHER IS FALLING.**

| passes | findings | S1 | S2 | S3 | **S1 share** |
|---|---|---|---|---|---|
| 1–5 · `-71`…`-75` | 24 | 21 | 2 | 1 | **87.5 %** |
| 6–10 · `-76`…`-80` | 21 | 13 | 8 | 0 | **61.9 %** |
| 11–16 · `-81`…`-102` | 25 | 19 | 6 | 0 | **76.0 %** |

**The S1 share dips in the middle third and comes back.** The last six passes returned **nineteen**
S1s — ninety per cent of what the first five returned — **on a corpus that had already been repaired
forty-five times.** `-102`, the sixteenth read, found two findings and **both were S1**.

**WHAT THIS SETTLES, AND IT IS THE UNCOMFORTABLE READING.** Six handoffs assumed the flat counter
meant the passes were scraping the barrel — finding ever-smaller things because the big ones were
gone. **They were not.** Three-quarters of everything ever found was the paper stating something
false, at pass sixteen as at pass one. The stopping rule was not merely unprovable, as § 0 of the
DoD says; **it was pointed at a stream that never degraded in severity either.** Jason's ruling was
right for a reason stronger than the one it was made on.

**AND THE MIRROR IMAGE, WHICH IS THE PART NOBODY PREDICTED.** The S3 tail everyone assumed was
accumulating **does not exist: one S3 in seventy findings.** The apparatus was never producing
nitpicks. That is a compliment to sixteen passes — and it is exactly *why* § 2.5's amendment was
necessary. The rubric graded truth, the axes hunted truth, the passes found truth defects at a
76 % clip, **and every seam the C-class names was invisible to all sixteen of them** because every
seam is a true statement. §§ 2 and 2.5 are not two halves of one instrument. They are two
instruments, and only one of them had ever been run.

> **FOR `SHIP-STATEMENT.md` (DoD § 4.2):** the "known limitations of this review" note has almost
> nothing to draw from the *ledger* — there is one S3 in it. The honest S3 content of this corpus is
> `POST-SHIP.md`'s list, not the pass history. **Do not pad the note to make it look thorough.**

### 1.2 · Per-pass detail

| pass | paper | n | S1 | S2 | S3 | findings |
|---|---|---|---|---|---|---|
| `-71` | II | 4 | 3 | 1 | 0 | II-15…II-18 |
| `-72` | II | 3 | 3 | 0 | 0 | II-19…II-21 |
| `-73` | III | 7 | 7 | 0 | 0 | III-1…III-7 (III-8 carded, S2 → `SL-7`) |
| `-74` | II | 4 | 3 | 0 | 1 | II-22…II-24, II-26 (II-25 carded, S1 → `SL-3`) |
| `-75` | IV | 6 | 5 | 1 | 0 | IV-1…IV-6 |
| `-76` | II | 5 | 3 | 2 | 0 | II-27…II-31 |
| `-77` | II | 3 | 1 | 2 | 0 | II-32…II-34 |
| `-78` | II | 2 | 2 | 0 | 0 | II-35, II-36 |
| `-79` | II | 2 | 0 | 2 | 0 | II-37, II-38 (II-39 apparatus, uncounted) |
| `-80` | III | 9 | 7 | 2 | 0 | III-9…III-17 |
| `-81` | IV | 9 | 5 | 4 | 0 | IV-1…IV-9 *(second IV numbering)* |
| `-83` | III | 4 | 4 | 0 | 0 | III-1…III-4 *(second III numbering)* |
| `-99` | II | 3 | 3 | 0 | 0 | II-40…II-42 |
| `-100` | IV | 4 | 3 | 1 | 0 | IV-10…IV-13 |
| `-101` | III | 3 | 2 | 1 | 0 | III-5…III-7 *(third III numbering)* |
| `-102` | II | 2 | 2 | 0 | 0 | II-43, II-44 |
| | | **70** | **53** | **16** | **1** | |

> **A TRAP FOR ANYONE RE-DERIVING THIS TABLE: FINDING IDS ARE NOT UNIQUE ACROSS THE LEDGER.**
> `III-1` names three different findings (`-73`, `-83`, and nothing at `-101`, which restarts at
> `III-5`); `IV-1` names two (`-75`, `-81`). **Always cite a finding as `<pass>/<id>`.** Summing or
> de-duplicating by bare id silently loses findings, and this is the first document to say so.

### 1.3 · Where the S3 went, since there is only one

`-74`/`II-26` — § 3.4 called a Gini gap *"which separates nothing"* when the gap is 0.103.
`REVIEW-014`'s own words: *"a repair of an overstatement, not of an error of fact."* Repaired anyway.

---

## 2 · DISPOSITION — 68 of 70 were repaired by the pass that found them

Two were carded and both are still open: `-73`/`III-8` (thirty sessions) → `SL-7`, and
`-74`/`II-25` (twenty-eight sessions) → `SL-3`. **Nothing else in the ledger is open.**

Five of the highest-value repairs were re-verified against the manuscripts at `7b5e114`:

| repair | check | result |
|---|---|---|
| `-102`/`II-42` | the false horizon-stability sentence is CUT | **absent** ✓ |
| `-102`/`II-44` | *"in closed form in all four coordinates"* is gone | **absent** ✓ |
| `-99`/`II-40` | § 7 points the 0.035 span at § 3.3, not § 3.2 | **§ 3.3, line 462** ✓ |
| `-101`/`III-7` | the 10⁻³ set reaches `k = 0.60`, not 0.50 | **0.60, line 1071** ✓ |
| `-101`/`III-5` | the `0.150` possessive re-attaches to the interval § 5.4 *does* carry | **`[1.135, 1.285]` present in § 5.4 at line 1373** ✓ |

> **METHOD NOTE, AND IT IS THE HANDOFF'S OWN WARNING LANDING ON THE AUDITOR.** Two of those five
> checks went red on the first run and **both times the check was wrong, not the manuscript.** A
> literal-phrase grep for *"six quantities neither command prints"* failed because the manuscript is
> hard-wrapped and the phrase spans a line break; a grep for `reaches k = 0.60` failed because the
> text is `reaches **k = 0.60**`. **A check pinned to a line break or to markdown emphasis is
> pinned to a subject that moves for reasons unrelated to what it is checking** — which is the
> `-102` trap, met twice, by the session auditing it. Both were re-run against the concept and both
> passed.

---

## 3 · `wt184` RULE 1 — all forty-four flags adjudicated

**Ruling: 2 TRUE, 42 FALSE.** Rule 1 was run at `7b5e114` (`RC 0`, 118 numbers checked, 44 flagged,
Rule 2: 3 checked, 3 flagged). **The rule was read before it was touched, and it has not been
touched** — `SL-1` and `SL-2` came out of this flag set, and `-101`'s `III-5` came out of an earlier
one. A rule tightened before its output is read deletes findings silently.

### 3.1 · The two TRUE flags — both S1, both § 4.9, both the same shape

| line | flag | ruling |
|---|---|---|
| **982** | `0.333` → § 5.4 | **TRUE.** § 5.4's measured rate is `0.408` (line 1363); `0.333` is nowhere in § 5.4. → `SL-1` |
| **1000** | `0.00789` → § 4.4 | **TRUE.** `0.00789` occurs **once in 2 750 lines**, in this sentence; § 4.4 is lines 466–611. → `SL-2` |

**Both live sites are in § 4.9, and both are `III-5`'s family** — a *possessive* attribution of a
number to a section that carries something else. **§ 4.9 is the site, and that is the finding behind
the finding.**

### 3.2 · The discriminator that separates the two from the forty-two

**The possessive form, and nothing else.** Every flag whose clause says `§X's <number>` and means it
is TRUE. Every flag where `§X` merely appears in the same paragraph is FALSE. The three possessives
that are *not* findings all attach to something § X really does carry:

* `§5.4's [1.135, 1.285]` — present in § 5.4 at line 1373; `0.150` is the sentence's own arithmetic
  on it. **This is `-101`'s `III-5` repair, working exactly as designed, still flagged.**
* `§4.9's tail condition`, `§5.4's own finding`, `§4.4's tier table`, `§4.4's δ₃* = Kα/(1 + K)` —
  possessives attaching to a condition, a finding, a table and a formula, not to a number.

### 3.3 · The forty-two FALSE flags, by mechanism — **this is the false-positive-reduction spec**

DoD § 1.1 permits a false-positive *repair*; it is **not** a new instrument. Nothing was built here.

| # | mechanism | flags | evidence |
|---|---|---|---|
| **FP-1** | **No attribution window on prose.** `wt184` builds a clause from a whole paragraph, so every `§` pointer co-occurs with every number in it. The window that cuts this fires **only on markdown table rows** — `REVIEW-037` measured that and it is the whole defect. | **34** | L566 (4), L579 (5), L624 (2), L755 (5), L820 (4), L976 (1), L995 (2), L1052 (1), L1064 (2), L1070 (1), L1306 (1), L1328 (1), L1552 (1), L1555 (1), L1973 (2), L2276 (1) |
| **FP-2** | **A foreign document's section is read as this manuscript's.** `PRE-001 §4.2` is another document's § 4.2. The `FOREIGN` regex matches `paper-II §3.1` and not this form. **Third witness** — `REVIEW-037` recorded the same shape for paper-II's *"their § 4.1"*. | **5** | L1213, all five |
| **FP-3** | **Numeric literals harvested from identifiers.** `101` out of `wealthTensor-101`; `80` out of `wealthTensor-80`; `7.3` out of `SDG 7.3.1`. (`001` out of `PRE-001` is counted under FP-2.) | **3** | L1973 (2), L2246 (1) |
| | | **42** | |

> **THE REPAIR, IF A POST-SHIP SESSION TAKES IT:** require an **attribution token** between the
> pointer and the number — a possessive `'s`, or a verb of attribution (*gives, states, reports,
> quotes, puts … at*) — instead of paragraph co-occurrence. **Measured against this adjudication
> that rule returns 2 of 44 and both are the TRUE ones.** Add `[A-Z]{2,}-\d{3}` and
> `wealthTensor-\d+` to the exclusion set before extracting numerals, and extend `FOREIGN` to
> `<DOC-ID> §N.M`. **All three are false-positive reductions. None makes the instrument look at
> anything new.**

### 3.4 · Rule 2's three flags

Out of scope for this at-bat, which the DoD scopes to Rule 1's forty-four. `REVIEW-036` adjudicated
Rule 2's flag set explicitly at `-101`. **Recorded here so the next session does not read the
absence as an oversight.**

---

## 4 · THE C-CLASS INVENTORY — count per type per paper

**DoD § 2.5. Counted, not repaired.** Three manuscripts swept end to end.

| type | paper-II | paper-III | paper-IV | **total** | whose pass |
|---|---|---|---|---|---|
| **C-a** antithesis residue | 2 | 1 | 2 | **5** | D |
| **C-b** scaffolding voice | 14 | 32 | 15 | **61** | D |
| **C-c** orphan | 0 | 0 | 1 | **1** | **C** |
| **C-d** fold problem | 2 | 7 | 4 | **13** | **C** |
| **C-e** apparatus leak *(see § 4.1 — this number needs splitting)* | 7 | 42 | 19 | **68** | D |
| **C-f** register drift *(FLAG ONLY — never fix)* | 2 | 4 | 2 | **8** | D flags it |
| **C-g** unplaced evidence | 0 | 0 | 0 | **0** | — |
| | **27** | **86** | **43** | **156** | |

### 4.1 · C-e SPLITS IN TWO, AND THE RAW 68 WOULD MISLEAD PASS D

§ 2.5's repair for C-e is *"repoint at the paper's own §, **or at a committed artefact the reader can
actually fetch**."* **A `scripts/wt###.py` named in a § Data-and-code section of a paper that ships
beside a public repository is a committed artefact the reader can fetch.** It is the provenance
promise the entire S1/S2 apparatus exists to keep. Counting it as a leak would have Pass D deleting
the corpus's best feature.

**Mechanical census, re-runnable, one `grep -o … | wc -l` per row:**

| what | paper-II | paper-III | paper-IV |
|---|---|---|---|
| **HARD — a reader cannot fetch or interpret it** | | | |
| session numbers (`wealthTensor-NN`) | 0 | 5 | 3 |
| `REVIEW-0NN` documents | 0 | 1 | 0 |
| `LEDGER.md` / `WT-0NN` ticket ids | 0 | 6 | 0 |
| `p7-passes.tsv` | 0 | 0 | 0 |
| **hard subtotal** | **0** | **12** | **3** |
| **SOFT — fetchable, but named without a gloss** | | | |
| `scripts/wt###.py` | 2 | 7 | 10 |
| `PRE-`/`REG-`/`RESULT-`/`ADR-` doc codes | 1 | 48 | 20 |
| raw commit hashes | 1 | 11 | 2 |
| `docs/` file paths | 4 | 14 | 11 |

**HARD C-e = 15 corpus-wide, and paper-II has none.** That is Pass D's delete-on-sight list and it is
small. The soft 53 are a *gloss* problem, not a leak: a reader meeting `` `REG-006` repairs the
omission `` with no antecedent stumbles, and the repair is one clause at first use, **not removal.**

### 4.2 · What the numbers mean for Pass C and Pass D

* **Pass C owns 14 items** — 13 C-d plus 1 C-c. **That is a small, bounded, structural pass**, which
  is the good news in this table. Paper-III carries half of it (7 C-d).
* **Pass D owns 15 hard C-e + 61 C-b + 5 C-a = 81 repairs, plus 8 C-f to FLAG AND LEAVE**, plus the
  soft-C-e gloss pass if it takes it. **Paper-III is 55 % of the work by itself.**
* **C-b is the real mass, and it clusters.** Roughly half of paper-III's 32 are in the **References
  section** — dated verification notes, *"an earlier draft of this entry recorded…"*, a to-do
  addressed to a future work session. **Pass D should read paper-III's References as one job.**

### 4.3 · Two results worth stating positively, because they are earned

**C-g is ZERO. Twenty-three tables across three manuscripts, every one anchored** by a sentence
telling the reader what to see in it. § 4.1 of the DoD asks for that as a ship condition and the
corpus already meets it. **Pass D has no anchor sentences to write.**

**C-c is ONE.** Three manuscripts, one orphan (paper-IV line 327, *"Paper III's ladder results"*,
a term used and never defined here). A corpus this long with one dead end is the payoff of sixteen
cross-reference passes.

### 4.4 · The honest limits of this count

**A ROUGH COUNT BEATS AN ELEGANT ABSENCE OF ONE — and this is a rough count.** It was produced by
reading each manuscript end to end against § 2.5's seven definitions and § 2.6's tie-breaker.
**C-f is impressionistic by construction** and is flagged, never fixed, so its precision does not
matter. **C-b and C-e are near-exhaustive** — both have grep-able signatures. **C-a, C-c and C-d are
the judgement calls**, and C-d is the one that matters most to Pass C, so **Pass C should expect to
find fold problems this sweep missed and should not treat 13 as a ceiling.**

---

## 5 · THE NINE CARRIED TEE-UPS, TRIAGED

| # | tee-up | ruling |
|---|---|---|
| 2 | the scope-sentence sweep as a script | **new instrument → POST-SHIP** (DoD § 1.1). Already there. |
| 3 | `wt133` sweep-3 | **new instrument → POST-SHIP.** Already there. |
| 4 | nine uncited reference entries on paper-II | **S2 → `SL-8`.** Re-measured this session: 16 entries, 7 cited, 9 not. |
| 5 | the general form of `II-34` | **a measurement, not a manuscript claim → POST-SHIP.** Already there. |
| 6 | `A6`, the docstring axis | **S3 → POST-SHIP.** DoD § 2 names `A6` as its own S3 example, which settles it. |
| 7 | paper-IV § 9 item 9's census | **S2 → `SL-9`.** The tee-up said *"rule on it or build the check"*; building is forbidden, so this is the ruling. |
| 8 | paper-IV § 7's Piketty relocation | **S3 → POST-SHIP.** Already there. |
| 9 | the zakat citation gap | **S3 → POST-SHIP.** The paper discloses the gap in its own closing note and says the argument does not depend on it — the DoD's S3 case exactly. **Fifth pass carrying it; this ruling ends the re-noticing.** |
| 10 | § 3.1's *"4–7 %"* band | **S3 → POST-SHIP.** Named in DoD § 2's S3 examples verbatim. Already there. |

Tee-up 1 was folded into this at-bat as step 2 and is § 3 above.

---

## 6 · WHAT PASS B NEEDS, AND WHERE IT IS (DoD § 3.0)

**`docs/SHIP-LIST.md`, closed at nine entries, each naming its repair.** Beyond that:

1. **Three of the nine are one repair repeated** (`SL-3`/`SL-4`/`SL-5`, the version stamps) and
   **one Jason ruling closes all three at once** if he wants to own version numbering.
2. **Two of the nine have a landed precedent in this corpus to copy rather than invent** —
   `SL-8` is `-81`'s `IV-7` repair, and `SL-7`'s honest-disclosure form is already written in
   § 11's own § 5.3 bullet.
3. **Two of the nine are attribution changes, not number changes** (`SL-1`, `SL-2`). The arithmetic
   in both sentences was checked this session and is correct. **Do not recompute; re-point.**
4. **`SL-6` must not be repaired by restating the number.** Naming the command and its locale is
   the repair; a bare corrected figure re-creates the defect for the next reader with a different
   locale.
5. **`defensive_count.py --against` must read +0** on every manuscript. Paper-III's baseline is 3
   outside § Limitations; paper-II and paper-IV are 0. **`SL-3`'s revision-history line is the one
   repair on this list with a real chance of raising the count — write it as a claim about the
   work, not a hedge.**
