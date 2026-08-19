# REVIEW-030 — THE HELD-OUT TEST: does the document-noun pre-filter survive text it was not built against?

*`wealthTensor-90`, 2026-08-19. Sessions -87, -88 and -89 established, in that order, that a
bare pointer naming no artefact is invisible to every sweep in this repository; that the sweeps
which do see pointers see them through a **verb list**; and that **no verb-free structural test
recovers the pointers** — the best of six reached precision 0.2459 at recall 1.0000 against a
bar of 0.50 / 0.80 named in advance.*

*This review runs the one measurement -89 could not run without contaminating its own corpus.*

---

## 1 · What is actually unvalidated, and why it matters

REVIEW-029 produced two numbers a successor would want to lean on, and **both were measured on
the corpus they were built against**:

- **T5's recall of 1.0000.** The document-class-noun test flags 61 of the 341 bare-target rows
  in Papers III and IV at `07cd47e` and contains all fifteen POINTERs. As a pre-filter for a
  human reader that is a **5.6x reading reduction with zero misses** — the single most useful
  artefact -89 produced. But `DOC_NOUNS` was written by the session that had just read all 341
  labels. REVIEW-027 §5's warning is exactly this shape: *a list that recovers everything on the
  corpus it was written against tells you about the list, not about the class.*
- **T6's failure.** The copular/passive-frame test was invented **after** the labels were read
  and scored on those same labels (0.0366 / 0.2000). A test chosen by looking at the answers is
  fitting, not testing, so its failure is suggestive and nothing more. T6 has never had an
  honest test. **It gets one here**, and that is a real gain regardless of which way it goes.

REVIEW-029 §8's falsifiers 4 and 5 name this as the outstanding work. **Papers I and II are the
held-out text**: they are in the repository, they are out of `#scope` for the promise instrument
(and stay out — this review does not touch `docs/promises-adjudicated.tsv`), and **no instrument
in this programme has ever been run on them.** Nothing in `DOC_NOUNS`, in `CLAIM_NOUNS`, in
`T6`, or in wt160's `N1`–`N6` was written against a single sentence of them.

## 2 · Method, and the one rule that makes it worth doing

1. **Pin the corpus.** `docs/papers/paper-I-price-formation/paper-I.md` and
   `docs/papers/paper-II-redistribution/paper-II.md` at **`83db4d5`**, the repository HEAD at
   the moment this section was written and before any file below existed.
2. **Enumerate** every `<token> in <target>` construction whose target is **BARE** under
   wt160's named-target tests `N1`–`N6`, by **importing wt166's own `enumerate_rows` machinery
   re-pointed at Papers I and II** — not by re-implementing it. Same `TOKEN_RE`, same
   `wt160._flatten`, `_target_window`, `_is_named`.
3. **Read every row in context and label it** POINTER or NOT-POINTER by REVIEW-028 §3's rule,
   unchanged and restated below, with a one-line reason and a FIRM/SOFT confidence. **Do not
   sample.**
4. **Score `T1`–`T6` UNCHANGED.** `wt169` imports the candidate functions and the word lists
   from `wt166` by module import. **Not one word of `DOC_NOUNS` or `CLAIM_NOUNS` is re-tuned.**

**THE RULE THAT MAKES THIS A TEST RATHER THAN A REPEAT: while labelling, no verb list, no
`DOC_NOUNS`, no `CLAIM_NOUNS`, and no candidate test's output was consulted.** The whole value
of this corpus is that nothing here was built against it, and the one way to destroy that value
is to let the thing being tested inform the truth set. If a later reader wants to check that
this held, the labels carry their reasons and the corpus is pinned.

**The adjudication rule, REVIEW-028 §3, fixed before this reading and unchanged:**

> POINTER iff **(a)** the construction asserts that some content is LOCATED IN a document,
> artefact, run or record — the reader is being asked to go there to check — AND **(b)** the
> target as written carries no handle a reader could follow.

Clause (b) holds for every enumerated row by construction, since `N1`–`N6` are silent on all of
them. The labelling therefore decides clause (a) alone, once per row.

## 3 · THE PREDICTION — committed before a single label exists, and before any count was computed

**This section is a git object written before `docs/pointer-groundtruth-I-II.tsv` existed and
before the enumerator had been run even once.** Everything below is blind.

**The bars, taken over unchanged from REVIEW-029 §3 so the two measurements are commensurable:**
a test **CLEARS** iff precision >= 0.50 AND recall >= 0.80; a test is a **PARTIAL WIN** iff it
reaches precision >= 0.30 with recall >= 0.90.

**And one bar this review adds, because "pre-filter" is the claim actually at issue and
REVIEW-029 never defined it operationally. A candidate is a USABLE PRE-FILTER iff, on text it
was not built against, it reaches recall = 1.0000 AND flags <= 25% of rows.** Recall must be
*perfect*, not merely high: a pre-filter exists so a human can decline to read the rows it does
not flag, and a single miss means the human must read them all anyway to be sure — 0.93 recall
buys nothing that 0.00 does not. The 25% is the point at which a 4x reduction is worth the
ceremony of running the tool at all.

**PREDICTED, in order of how much I would bet on each:**

- **P1 · THE HEADLINE: T5's recall on Papers I and II is BELOW 1.0000.** `DOC_NOUNS` holds 30
  nouns and there are more ways to name a document than that. Specifically I expect it to miss
  a pointer whose target head noun is one of `notebook`, `supplement`, `derivation`, `proof`,
  `caption`, `code`, `archive`, `manuscript`, `preprint`, `dataset`, `panel`, `footnote`,
  `annex`, `bibliography` — none of which is in the list. **A recall that survives at 1.0000
  would falsify this outright**, and I would then have to say that the list is capturing
  something about how documents are named in English rather than about these two manuscripts.
- **P2 · T5 is NOT a usable pre-filter on held-out text** by the definition just given — it
  fails on recall, per P1, not on flagged fraction.
- **P3 · NO pre-registered candidate (`T1`..`T5`) clears precision >= 0.50 with recall >= 0.80,
  and none reaches the partial-win bar either.** Same mechanism REVIEW-029 §3 named: the base
  rate. The separating feature is in the verb, and none of these tests can see the verb.
- **P4 · T6, given its first honest test, fails: precision < 0.15 and recall < 0.50.** Its
  III/IV numbers (0.0366 / 0.2000) were fitted, so held-out numbers no worse than those would
  be mildly surprising and worth saying out loud.
- **P5 · The base rate on Papers I and II is between 2% and 9%,** i.e. of the same order as
  III/IV's 4.40% — this class is a property of how these manuscripts are written, not of Paper
  III's length.
- **P6 · BLIND DENOMINATOR.** Papers I and II are 83,845 characters against III and IV's
  264,171 — 31.7%. If constructions scale with length, 444 x 0.317 = ~141 constructions and
  341 x 0.317 = ~108 bare rows. **Predicted: 100–190 constructions, 75–145 bare rows, and
  between 2 and 9 POINTERs.** This one is cheap to check and it is here because a prediction
  that costs nothing to make should still cost something to be wrong about.

**-89's OWN PREDICTION, restated here so it can be marked by someone other than its author.**
REVIEW-029 §6.1 says of T5's recall of 1.0000: *"On a held-out corpus it will be lower. How much
lower is the measurement Papers I and II are sitting there waiting to supply."* **That is a
prediction across a session boundary, scored in §6 below by a session that did not write it** —
which is the closest this programme has come to a second reader, and it is worth noting that it
only became possible because -89 wrote the prediction down instead of leaving it as an instinct.

**WHAT WOULD MAKE ME CALL THE PRE-FILTER USABLE, stated now so the concession is not negotiable
after the numbers arrive: T5 reaching recall 1.0000 on Papers I and II while flagging <= 25% of
the rows.** If that happens, P1 and P2 are wrong on their face, I will record them as wrong in
§6 before drawing any distinction about noun lists, and the honest reading is that a successor
may use T5 as a pre-filter on unread text — with the caveat that two corpora is still two.

**PREDICTED VERDICT: the document-noun pre-filter does not survive the held-out test, and the
last route to a mechanical sweep of this class closes with it.**

*MEASURED: §§4 onward, written after the labels and the scoring existed.*
