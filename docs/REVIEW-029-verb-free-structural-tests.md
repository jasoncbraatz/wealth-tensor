# REVIEW-029 — CAN ANY VERB-FREE STRUCTURAL TEST RECOVER THE POINTERS FROM THE 341?

*`wealthTensor-89`. §§1–3 were written and committed BEFORE `docs/pointer-groundtruth.tsv`
held a single label and before `scripts/wt166_pointer_groundtruth.py` existed. The prediction
in §3 was therefore made without knowing the base rate it predicts about — this session had
reproduced the 341 and had not read them. §§4–8 were written after. `git log --follow
docs/REVIEW-029-verb-free-structural-tests.md` shows the prediction landing first; the labels
and the scorer land after it in separate commits.*

---

**THE VERDICT, in one sentence someone can mark right or wrong: NO verb-free structural test
recovers the POINTER rows — over the 341 labelled bare-target constructions at `07cd47e`
(15 POINTERs, a 4.40% base rate), the best of the five pre-registered candidates reaches
precision 0.2459 at recall 1.0000 and the best pairwise conjunction reaches precision 0.4074 at
recall 0.7333, so nothing clears the pre-registered bar of precision ≥ 0.50 with recall ≥ 0.80,
and the sole candidate that clears it under any labelling variant is T5, which is a noun list.**

*§§1–3 below are unchanged from `2515eaf`. Only this verdict block, and §§4–8, were added after
the scoring ran.*

---

## 1 · The question REVIEW-028 §8 falsifier 5 left open

`wt160` and `wt163` flag `<VERB> in <TARGET>` where TARGET carries no handle a reader could
follow. REVIEW-028 established that the count they return is a property of the VERB LIST: two
independently-chosen a priori vocabularies returned the same ten while a reading that consulted
no list returned fourteen. The obvious repair — delete the verb list, flag every bare target —
was measured and rejected in §6.4: **341 of the corpus's 444 `<token> in <target>` constructions
at `07cd47e` have a bare target**, and most are ordinary prose. `bites in pharmacokinetics` and
`live in different worlds` are in that 341.

REVIEW-028 §8 falsifier 5 names the one attack that could still rescue the enumeration:

> **Attack §6.4's 341.** If a defensible sub-class of bare targets can be carved out
> structurally — without a verb list — the enumeration problem is soluble and this review's
> pessimism is wrong. That is the single most valuable attack available on this file.

Nobody had run it, because nobody had the labels. **Without labels there is no denominator and
no truth set; every pointer count in this programme rests on one reader's unlabelled judgement,
and no proposed detector — word-list or structural — can be scored at all.** This review builds
the labels and runs the attack.

## 2 · Method

**The denominator is reproduced, not asserted.** Taking every word token immediately preceding
` in ` in `paper-III.md` and `paper-IV.md` at `07cd47e`, over `wt160`'s own flattened text, and
applying `wt160`'s own `_target_window` and `_is_named` (N1–N6) — imported, not
re-implemented — yields **444 constructions, 264 distinct tokens, 341 with a bare target
(282 in Paper III, 59 in Paper IV)**. Those are REVIEW-028 §3's and §6.4's numbers to the row.

**Every one of the 341 is read and labelled by hand, in `docs/pointer-groundtruth.tsv`**, keyed
by `(file, line, token, target)` — unique at 341, and every component recomputable from the
revision — each **POINTER** or **NOT-POINTER** with a one-line reason. **No verb list is
consulted while labelling.** A ground truth built with a word list cannot score a word list;
that is the whole point of the exercise, and it is why the labelling is the expensive half.

The adjudication rule is REVIEW-028 §3's, unchanged and fixed before this reading:

> Label POINTER iff (a) the construction asserts that some content is LOCATED IN a document,
> artefact, run or record — the reader is being asked to go there to check — AND (b) the target
> as written carries no handle a reader could follow. Temporal, manner, idiomatic and
> quantitative uses of `in` are NOT pointers.

Clause (b) is guaranteed for all 341 by construction (N1–N6 are silent on every row), so the
labelling is deciding clause (a) alone, 341 times.

**`scripts/wt166_pointer_groundtruth.py`** then recomputes the 341 from `07cd47e`, **REFUSES
(exit 2) if the TSV's key set differs from the recomputed key set by a single row** — so the
labels cannot silently drift from the corpus — and scores candidate verb-free structural tests
against the labels, reporting **precision and recall for each**.

### 2.1 · The candidate tests, named before any of them was run

Each is computable from the construction and its sentence alone, with **no verb list**.

| | test | flags a row when |
|---|---|---|
| **T1** | **definite head** | the target begins with a definite determiner (`the`, `this`, `that`, `these`, `those`, `its`, `their`, `our`, `the same`) |
| **T2** | **claim-subject** | the clause's grammatical subject is a claim/result noun rather than an object or an agent |
| **T3** | **determiner + abstract-noun shape** | the target is short (≤ 4 words), determiner-headed, contains no finite verb and no number |
| **T4** | **section position** | the construction sits in the final third of its `##`/`###` section |
| **T5** | **document-class head noun** | the target's head noun is a document/record noun (`statement`, `registration`, `title`, `table`, `logs`, `notes`, `repository`, `paper`, `appendix`, `text`, `record`, `run`, `sweep`, …) |

**T5 is included precisely because it is the one most likely to score well, and it is
disqualified in advance.** It is verb-free and it is NOT vocabulary-free: it relocates the word
list from the verb to the noun. If T5 wins, it wins by moving the enumeration problem one slot
to the right, not by solving it, and this review will say so rather than bank it. Naming that
before the scoring is the only way the disqualification is not a post-hoc excuse.

## 3 · THE PREDICTION — committed before any label exists and before any score was computed

**The bar, named in advance.** A verb-free structural test **CLEARS** iff, over all 341 rows,
it reaches **precision ≥ 0.50 AND recall ≥ 0.80** simultaneously. That bar is deliberately
generous to the attack: precision 0.50 means a successor reads two rows per real finding, which
is cheaper than reading 341, and recall 0.80 means the test may miss one pointer in five and
still count as a solution.

**PREDICTED:**

- **The ground truth holds 14–20 POINTER rows; point estimate 16.** REVIEW-028 §4 found
  fourteen by reading the 444 under this rule, so a careful re-reading of the 341 should
  recover those fourteen and may add one or two the first pass slid past (§8 falsifier 1
  predicted exactly this possibility). If the count comes back below 14 the earlier reading was
  over-generous; if above 20, it was substantially incomplete and REVIEW-028's 10-vs-14 gap is
  understated.
- **NO candidate test clears the bar. Not T1, not T2, not T3, not T4, and not T5.**
- **The mechanism is the base rate, and it is arithmetic, not pessimism.** At ~16 positives in
  341 the prevalence is ~4.7%. Precision ≥ 0.50 at recall ≥ 0.80 requires a feature that selects
  a set of **≤ 26 rows containing ≥ 13 of the 16 pointers** — a 10× enrichment out of a single
  surface feature. Every candidate here keys on the TARGET's shape or the sentence's position,
  and the target's shape is exactly what all 341 rows have in common: they are bare. **The
  feature that separates `recorded in the working notes` from `live in different worlds` is not
  in the target. It is in the verb.** That is what "irreducibly two-part" means, and this review
  expects the numbers to say it.
- **Specifically: T1 reaches high recall and abject precision** (predicted recall ≥ 0.80,
  precision ≤ 0.15), because pointers are overwhelmingly definite-headed and so is most English
  prose about `the market`, `the model`, `the same period`. **T3 trades a little recall for very
  little precision.** **T4 is noise** — predicted precision within a factor of two of the 4.7%
  base rate, because where a sentence sits in its section is not evidence about what its verb
  asserts. **T2 is the only candidate with a real mechanism**, since "a claim is located
  somewhere" is closer to the actual criterion than any target-shape feature — and it is
  predicted to fail on precision anyway, ≤ 0.35, because claim-subject sentences are what an
  academic paper is mostly made of.
- **T5 is predicted to score the best of the five and is still predicted not to clear** —
  precision ≤ 0.45 — because document-class nouns appear constantly in non-pointing prose
  (`the paper argues`, `in the same run`, `in the table below`). If T5 nonetheless clears, the
  finding is NOT that the enumeration is soluble; it is that a NOUN list can do what a VERB list
  could not, and the next session's job is then to test whether that noun list is a property of
  the corpus or of the list — REVIEW-028's question, one slot to the right.

**PREDICTED VERDICT: NO verb-free structural test recovers the POINTER rows. The class is not
mechanically sweepable, and the two-independent-readers design is the only remaining
instrument.**

**WHAT WOULD CHANGE MY MIND — stated in advance, so the concession is not negotiable after the
fact.** Any single candidate reaching precision ≥ 0.50 with recall ≥ 0.80 falsifies this
prediction outright. So does a *conjunction* of two candidates reaching that bar, and this
review commits in advance to reporting the best pairwise conjunction whether or not it helps.
So does any test reaching precision ≥ 0.30 with recall ≥ 0.90, which would not solve the
enumeration but would make a mechanical PRE-FILTER genuinely useful — a successor reading 50
rows instead of 341 is a real saving and this review would call that a partial win rather than
pretend it was nothing. **And if T5 alone clears, the prediction is wrong on its face and I
will record it as wrong in §6 before drawing the "it is only a noun list" distinction** — the
distinction is a reading of the result, not a reason to keep the prediction.

**MEASURED: §§4–6. Eight of nine sub-claims hold; the headline holds under two labellings
of three, and §6 marks the exception rather than explaining it away.**

---

## 4 · MEASURED — the labels, and the one the fourteen did not contain

All 341 rows were read. **Fifteen are POINTERs**, a base rate of **4.40%**. Fourteen are
REVIEW-028 §4's fourteen, verbatim — post-condition `F3` proves every one of `wt160`'s ten
flags at `07cd47e` is labelled POINTER, so the labelling demonstrably applies the same
adjudication the instrument does. The fifteenth is new:

| file | line | construction | why it is a pointer |
|---|---|---|---|
| III | 1261 | **`are in`** the run logs | four sensitivity analyses are asserted to sit in a record the sentence does not name |

**Its verb is the COPULA, and that is why nobody had it.** REVIEW-028 §3 offered its
enumeration as vocabulary-free: take every token preceding ` in `, all 264 of them, and read
them. But step 2 of that method was *"keep every token that could locate content in an
artefact"* — and `are` does not LOOK like a locating verb, even though in this sentence it does
all of the locating work. **The reading that was offered as free of a word list had a covert one
at step 2, and only labelling every row without exception exposed it.** That is REVIEW-028 §8
falsifier 1, fired — from inside, by the very exercise its §8 commissioned. `F4` pins it: exactly
one POINTER row lies outside the published fourteen, and it is this one.

### 4.1 · What the bare target was concealing

Naming the artefact made the sentence checkable, and it did not check out. `scripts/wt026_severe_test.py`
runs **three** sensitivities; both `RESULT-002-*-run.log` files print exactly three; **no fourth
is named in `PRE-001`, registered in `PRE-002`, implemented in the instrument, or printed in any
log.** The sentence said *four*.

**This is the strongest available argument that the bare-pointer class is not a style nit.** With
no artefact named there was nothing to check the number against, and an unsupported count stood
in a paper about severe testing for as long as the pointer stayed bare. `wt167` re-targets the
pointer and REMOVES the count rather than rewriting it to three: the identical "four" also sits
in `PRE-002` §2, `RESULT-001` §1 and `RESULT-002` §1, and an in-place edit to a registration or a
result document is a standing Jason-sized ruling — Asana `1217603625863293`, the RESULT-001
"320 against 322" card, which is this same class one instance over. The second instance is carded
against it so the one ruling covers both. `wt168` adjudicates the emitted promise **H**, with a
per-file evidence command. **Had the count survived the repair the promise would have adjudicated
R**, and that counterfactual is the finding, not a near miss.

## 5 · MEASURED — the scoring

341 rows · 15 pointers · base rate 4.40% · bar named in advance: **precision ≥ 0.50 AND
recall ≥ 0.80**.

| | test | class | flagged | TP | FP | FN | precision | recall | |
|---|---|---|---|---|---|---|---|---|---|
| **T1** | definite head | closed-class | 143 | 15 | 128 | 0 | **0.1049** | **1.0000** | fails |
| **T2** | claim-subject | open-class (list-bound) | 74 | 11 | 63 | 4 | **0.1486** | **0.7333** | fails |
| **T3** | determiner + abstract-noun shape | closed-class | 91 | 10 | 81 | 5 | **0.1099** | **0.6667** | fails |
| **T4** | section position (final third) | closed-class | 116 | 3 | 113 | 12 | **0.0259** | **0.2000** | fails |
| **T5** | document-class head noun | open-class (list-bound) | 61 | 15 | 46 | 0 | **0.2459** | **1.0000** | fails |
| T6 | copular/passive frame | closed-class | 82 | 3 | 79 | 12 | 0.0366 | 0.2000 | fails — *exploratory* |

**Best pairwise conjunction of the pre-registered five, reported as committed in advance whether
or not it helped:** `T2+T5`, 27 rows flagged, **precision 0.4074, recall 0.7333** — the closest
anything comes, and it still fails both halves of the bar.

**T6 is EXPLORATORY and cannot falsify anything.** It was invented after reading the labels, and
a test chosen by looking at the answers and then scored on those same answers is fitting. It is
reported because it is the most natural structural idea in the space — *the construction sits in
a copular or passive frame* — and because it **failed badly** (precision 0.0366, recall 0.2000),
which is worth knowing even from a compromised design. The honest test of T6 needs a held-out
corpus, and one already exists, untouched: **Papers I and II, out of `#scope` for seven passes.**

### 5.1 · The verdict does not turn on the judgement calls, except in one direction

Every candidate was scored three times: **PRIMARY** (the labels as written, 15 pointers),
**STRICT** (the 11 FIRM pointers only), and **LOOSE** (PRIMARY plus all 36 SOFT NOT-POINTERs,
51). PRIMARY and STRICT agree: **nothing clears under either** (`F8`).

**Under LOOSE, T5 clears — precision 0.7377, recall 0.8824.** §3 named this outcome in advance
and committed to recording it as a hit against the prediction before drawing any distinction, so:
**the prediction is wrong on its face for one of three labelling variants, and the variant is not
one I can dismiss for being unreasonable — I constructed it myself, before the scoring, as the
generous reading.** `F14` pins it rather than tidying it away.

What deflates it is a number, not a rhetorical move. **T5 flags 30 of the 36 SOFT NOT-POINTER
rows that LOOSE promotes to positives — 83%** (`F15`). Those rows are the self-locating ones:
*the abstract*, *this section*, *its own note*, *the same directory*. They were marked SOFT
precisely because they name document-ish things while not sending the reader anywhere, which is
the feature T5 selects on. **LOOSE is close to being the set T5 was built to find**, so its
clearance is substantially circular — and it is still a real result, because it says the
document-noun feature tracks *something*, just not the evidential distinction the class is about.

## 6 · The prediction, marked

| predicted at `2515eaf`, before a label existed | measured | |
|---|---|---|
| ground truth holds 14–20 POINTERs, point estimate 16 | **15** | ✅ in band |
| base rate ≈ 4.7% | **4.40%** | ✅ |
| **no candidate clears the bar** | none under PRIMARY or STRICT; **T5 clears under LOOSE** | ⚠️ **two of three** |
| T1: recall ≥ 0.80, precision ≤ 0.15 | 1.0000 / 0.1049 | ✅ both halves |
| T2: fails on precision, ≤ 0.35 | 0.1486 | ✅ |
| T3: trades recall for very little precision | 0.6667 / 0.1099 | ✅ |
| T4: noise, precision within 2× the base rate | 0.0259 against 0.0440 — *below* it | ✅ |
| T5: scores best of the five, precision ≤ 0.45 | best of five; 0.2459 | ✅ |
| partial-win bar: precision ≥ 0.30 at recall ≥ 0.90 | nothing reaches it; T5 nearest at 0.2459 / 1.0000 | ✅ not met |

Eight of nine sub-claims hold. The ninth — the headline — holds under two labellings of three,
and the exception is the candidate that was disqualified in advance for being a noun list.

**And the mechanism §3 predicted is the mechanism the numbers show.** T1 has *perfect* recall:
every one of the 15 pointers has a definite-headed target. So does T5. Neither can turn that into
precision, because **143 of 341 bare targets are definite-headed and 15 of them are pointers.**
The feature that separates `are recorded in the working notes` from `live in different worlds` is
not in the target — both targets are bare noun phrases and one of them is definite. It is in the
verb, or in the sentence's evidential intent, which no closed-class feature reaches.

### 6.1 · The one thing a successor should actually take from this

**T5 flags 61 rows of 341 and contains all fifteen pointers — recall 1.0000 at precision 0.2459.**
It misses the pre-registered partial-win bar (0.30) by 0.054, so by the letter of §3 it is not a
win, and this review will not move a bar it named in advance. But as a **pre-filter for a human
reader** it is a 5.6× reduction with, on this corpus, zero misses. A successor who wants to read
this class on Papers I and II should read T5's 61 rather than all 341 — **and should hold that
recall of 1.0000 in exactly the suspicion REVIEW-028 taught**, because T5's noun list was written
by the same session that read the labels, and a list that recovers everything on the corpus it
was written against is the definition of the result REVIEW-027 §5 warned about. **On a held-out
corpus it will be lower. How much lower is the measurement Papers I and II are sitting there
waiting to supply.**

## 7 · Post-conditions of this session's own that were wrong

Two. Neither is a verdict on the work it guarded, and both are recorded because
REVIEW-028 §7.2 established that hiding them is the expensive move.

- **`wt166` F8** asserted that PRIMARY, STRICT and LOOSE all agree on the verdict. They do not —
  T5 clears under LOOSE. F8 was a prediction about the measurement and the measurement refuted
  it. It was **not relaxed and the variant was not dropped**: F8 now pins the true, narrower fact
  (PRIMARY and STRICT agree) and the new `F14` pins the surprise, with `F15` quantifying why it
  deflates. That is seven wrong post-conditions across three sessions and the ledger stays open.
- **`wt168`'s evidence NOTE**, first draft, quoted its own command's output as showing
  `INCONCLUSIVE (underpowered)` in **both** `RESULT-002` logs. Only the pilot log has one; the
  replication log reports `PREDICTION FAILS` alone. The note was a paraphrase of what the command
  was expected to print rather than a transcript of what it printed, and `H3`'s displayed output
  is what caught it. **The repair is a new post-condition, `H14`: the note must quote the
  command's actual stdout character for character.** An evidence note that paraphrases its own
  evidence is a note nobody has checked — the same defect as `wealthTensor-88`'s unattributable
  `git log`, one layer up, and now mechanically impossible in this row.

## 8 · Falsifiers

1. **Read the 341 again and disagree with a label.** Every row carries a one-line reason, so
   disagreement is cheap to state and cheap to check. The 36 SOFT rows are where to start, and
   `III 2195` — *"two different objects have been sharing one symbol in this programme's working
   notes"* — is the softest NOT-POINTER in the file: it is the exact target-shape of the III-2
   defect that founded this class, and it is excluded only because the working notes are offered
   as the MOTIVE for stating notation rather than as the location of evidence. Overturn it and
   the count is 16.
2. **Attack the four SOFT POINTERs.** `given in the two rows above` and the three `its own
   title` rows are self-locating; a strict reading drops them and the count is 11. That reading
   is scored in full as STRICT, and it changes no verdict — but it does mean **REVIEW-028's
   published ten contains four rows this session would not have counted**, which is a live
   inconsistency in the programme's own adjudication and is stated here rather than smoothed.
3. **Score a verb-free test this review did not think of.** The labels are committed and the
   scorer takes a new candidate in four lines. A test clearing precision 0.50 at recall 0.80
   under PRIMARY falsifies §3 outright.
4. **Run T6 on Papers I and II.** It failed here, on the corpus that invented it, which is the
   worst possible showing. If it does better on held-out text, the exploratory design was the
   problem rather than the test.
5. **Attack the 5.6× pre-filter claim in §6.1.** T5's recall of 1.0000 was measured on the same
   corpus its noun list was written against. Papers I and II are the held-out set and nobody has
   run it there.
6. **Attack the labeller.** Every objection REVIEW-028 §8 falsifier 6 raised stands here and is
   worse: the same reader labelled 341 rows, wrote the tests, and wrote the prediction. §7's two
   wrong post-conditions and §4's copula miss are direct evidence that this reader is fallible in
   exactly the way the **two-independent-readers design** exists to catch. **That design is now
   the only instrument left for this class, and this review is the strongest argument for it that
   the programme has produced** — because it is the first pass that can say what a second reader
   would be checking *against*.
