# REVIEW-029 — CAN ANY VERB-FREE STRUCTURAL TEST RECOVER THE POINTERS FROM THE 341?

*`wealthTensor-89`. §§1–3 were written and committed BEFORE `docs/pointer-groundtruth.tsv`
held a single label and before `scripts/wt166_pointer_groundtruth.py` existed. The prediction
in §3 was therefore made without knowing the base rate it predicts about — this session had
reproduced the 341 and had not read them. §§4–8 were written after. `git log --follow
docs/REVIEW-029-verb-free-structural-tests.md` shows the prediction landing first; the labels
and the scorer land after it in separate commits.*

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

**MEASURED: PENDING.**
