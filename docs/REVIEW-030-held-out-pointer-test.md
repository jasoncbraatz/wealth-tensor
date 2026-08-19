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

---

## 4 · MEASURED — the held-out corpus, and what the pre-filter did on it

`docs/pointer-groundtruth-I-II.tsv`, committed at `6b262aa` before `wt169` existed:
**125 `<token> in <target>` constructions in Papers I and II at `83db4d5`, 88 of them with a
BARE target** (44 in each paper), **7 POINTERs — 4 FIRM, 3 SOFT — a 7.95% base rate**, and 9
SOFT NOT-POINTER rows. All 88 were read in context; none was sampled.

`scripts/wt169_pointer_groundtruth_heldout.py`, committed **UNRUN** at `9e38d18`, imports
`wt166`'s six candidate functions and all five of its word lists **by module import, unmodified**
— `G8` hashes `DOC_NOUNS`, `CLAIM_NOUNS`, `DEFINITE`, `DETERMINERS` and `BE_FORMS` against
digests recorded in its source, so a future session that re-tunes a list makes the run fail
rather than quietly rescore. It re-points the enumerator at Papers I and II, refuses on key-set
drift exactly as `wt166` does, and recomputes Papers III and IV **in the same process**, so the
comparison below is measured here rather than quoted from REVIEW-029.

**THE ANSWER, in one sentence someone could mark right or wrong: T5's recall does not survive —
on Papers I and II the document-class-noun test recovers 1 of the 7 bare pointers, recall
`0.1429` against `1.0000` on Papers III and IV, at precision `0.0714`, which is BELOW that
corpus's own `0.0795` base rate, so it is not a usable pre-filter and reading its 14 flagged rows
is worse per row than reading 14 rows drawn at random.**

**The two corpora, same six tests, both recomputed by `wt169`:**

|  | test | class | III+IV prec | recall | **I+II prec** | **recall** |
|---|---|---|---|---|---|---|
| T1 | definite head | CLOSED | 0.1049 | 1.0000 | **0.1750** | **1.0000** |
| T2 | claim-subject | OPEN (list-bound) | 0.1486 | 0.7333 | **0.0769** | **0.1429** |
| T3 | determiner + abstract-noun shape | CLOSED | 0.1099 | 0.6667 | **0.1905** | **0.5714** |
| T4 | section position (final third) | CLOSED | 0.0259 | 0.2000 | **0.1600** | **0.5714** |
| T5 | document-class head noun | OPEN (list-bound) | 0.2459 | **1.0000** | **0.0714** | **0.1429** |
| T6 | copular/passive frame | CLOSED | 0.0366 | 0.2000 | **0.0769** | **0.2857** |

Nothing clears `0.50 / 0.80`. Nothing reaches the partial-win bar `0.30 / 0.90`. Nothing is a
usable pre-filter. The best pairwise conjunction of the pre-registered five is `T1+T4` at
`0.2857 / 0.5714`, reported here because REVIEW-029 §3 committed in advance to reporting it
whether or not it helped, and it does not.

### 4.1 · The finding nobody predicted: the collapse sorts exactly by word class

Look down the table by CLASS rather than by test. **Both OPEN-CLASS tests collapse and all four
CLOSED-CLASS tests hold or improve.**

- **T5** (open): recall `1.0000 -> 0.1429`. **T2** (open): recall `0.7333 -> 0.1429`.
- **T1** (closed): recall `1.0000 -> 1.0000`, precision *up* `0.1049 -> 0.1750`.
  **T3** (closed): `0.6667 -> 0.5714`. **T4** (closed): `0.2000 -> 0.5714`, precision up 6x — a
  noise test behaving like noise, in the other direction this time.

REVIEW-029 §2.1 declared each candidate CLOSED- or OPEN-CLASS **before any of them was scored**,
and disqualified T5 in advance on that ground alone. That declaration has now made a **prediction
about a corpus that did not exist as data yet, and the prediction is exactly right**: the tests
built on finite function-word sets transfer, and the tests built on content-word lists do not.
The distinction was drawn to keep a disqualification honest; it turned out to be the thing that
tells you which tests generalise. **That is a stronger result than -89 claimed for it, and it
belongs to -89.**

### 4.2 · Why T5 collapses, as arithmetic rather than as a story

Of the 7 held-out POINTERs, exactly ONE has a `DOC_NOUNS` word in its target (`G12` pins this):
`II 11 named in the data-availability statement` — **the same construction Paper III carries**,
and therefore the one row of the seven that is not really held out at all. The other six point at
**`the code and the tests`**, **`the test`**, **`the test suite`**, **`the implementation`**,
**`this programme`** and **`the third column`**. Not one of those head nouns is in the list, and
there is no mystery about why: Papers III and IV point at *registrations, titles, logs and
statements*, so a list read off them names registrations, titles, logs and statements. Papers I
and II are papers about **code**, and they point at code.

The list did not fail to be long enough. **It was a list of how two particular manuscripts happen
to name their artefacts**, which is REVIEW-027 §5's warning arriving on schedule, and it is the
same shape as REVIEW-028's verb-list finding one part of speech to the right.

### 4.3 · -89's LOOSE surprise does not reproduce

`wt166`'s `F14` pinned a genuine surprise: on Papers III and IV, under the LOOSE labelling, T5
alone cleared the bar (`0.7377 / 0.8824`), and `F15` deflated it by measuring that LOOSE promotes
mostly document-noun rows. **On held-out text the flip is gone**: T5 under LOOSE reaches
`0.5714 / 0.5000` and clears nothing. So the one place -89's headline broke was itself a property
of that corpus. `F14` was right to pin it and right not to relax the bar; it is now also known to
be local.

## 5 · What the labelling turned up in Papers I and II — reported, NOT repaired

### 5.1 · Seven bare pointers, and the manuscripts are out of scope for repair

These two manuscripts are out of scope for repair in this pass: the at-bat was to MEASURE, and a
repair pass carries a different risk profile and needs its own severe test. **Not one word of
either manuscript was changed by this session.** The seven, for whoever takes them:

| | where | construction | conf |
|---|---|---|---|
| 1 | Paper I, front matter | **Fixed in the code and the tests** | FIRM |
| 2 | Paper I §5 | **in the regeneration script and in the test** | FIRM |
| 3 | Paper II, AI-assistance note | **named in the data-availability statement** | FIRM |
| 4 | Paper II §2.2 | **verified to machine precision in the implementation** | FIRM |
| 5 | Paper I §1 | **a proposition stated elsewhere in this programme** | SOFT |
| 6 | Paper I §4 | **asserted in the test suite deliberately** | SOFT |
| 7 | Paper II §3.1 | **the budget is visible in the third column** | SOFT |

Row 3 is the construction Paper III carries verbatim and `wt164` already repaired there — so
**the identical defect stands unrepaired in Paper II**, which is worth knowing on its own. Rows 5
and 6 are SOFT because the handle arrives immediately afterwards, outside the target, and row 7
because the table is the one directly above.

### 5.2 · Two instrument gaps the held-out corpus surfaced, carded not patched

**(a) THE TWELVE-WORD WINDOW CAN CUT A HANDLE IN HALF.** Paper I §1 reads *"is stated with its
domain in the companion paper on the dual tensor **[III, §2.2]**"* — a followable handle. The
window stops at the first clause boundary, the comma inside `[III, §2.2]` **is** a clause
boundary, so the target `wt160` sees ends at `[III` and `N2` never gets to look at the section
reference. The row is therefore counted as BARE when the reader can plainly follow it. REVIEW-028
listed the window as an INVITED ATTACK; this is the first concrete instance of it firing, and it
is a *false bare*, not a missed pointer — the error runs the safe direction.

**(b) A NUMBERED DIVISION IS STILL NOT A NAMED TARGET.** Paper I §6 reads *"its generalisation is
stated **in Limitation 1** rather than demonstrated"*. `N1`–`N6` do not model a numbered division
of the document in hand, which is the third instance of the gap REVIEW-029 opened with `the
abstract`, `the body` and `*Abandoned Approaches*`.

Neither is patched here, for the reason -89 gave and it has not weakened: adding `N7`/`N8` moves
a published count, so it needs its own pass and its own severe test. Both are carded.

## 6 · The predictions, marked

**-89's, scored by a session that did not write it.** REVIEW-029 §6.1: *"On a held-out corpus it
will be lower."* **RIGHT** — and the useful part is the magnitude, which -89 declined to guess:
recall `1.0000 -> 0.1429`, precision `0.2459 -> 0.0714`. Not lower. **Effectively gone.** -89 also
wrote that a successor *"should read T5's 61 rather than all 341"* on Papers I and II; on the
actual numbers that advice would have found **one** of the seven pointers and missed six.
**That recommendation is hereby withdrawn, by the measurement it asked for.**

**This session's, from §3, which was a git object before a single label existed:**

| | predicted | outcome |
|---|---|---|
| P1 | T5's recall on Papers I and II is below 1.0000 | **RIGHT** — 0.1429 |
| P2 | T5 is not a usable pre-filter on held-out text | **RIGHT** — `G14`, no candidate is |
| P3 | no pre-registered candidate clears, or reaches partial-win | **RIGHT** — `G7`, `G11` |
| P4 | T6, given its first honest test, fails: precision < 0.15, recall < 0.50 | **RIGHT** — 0.0769 / 0.2857 |
| P5 | base rate between 2% and 9% | **RIGHT** — 7.95% |
| P6 | 100–190 constructions, 75–145 bare, 2–9 POINTERs | **RIGHT** — 125, 88, 7 |

**Six for six is not a boast, it is a warning about the bar.** P6's ranges were wide enough to be
cheap; P5 was nearly as safe. The three that had content were P1, P2 and P4, and the honest thing
to say about P1 is that it predicted the *direction* and got the *magnitude* badly wrong in the
comfortable direction: §3 expected T5 to miss *a* pointer whose head noun was outside the list.
It missed six of seven and landed below the base rate. **A prediction that is right about the sign
and off by a factor of six on the size is not a well-calibrated prediction, and this section is
not going to grade it as one.**

## 7 · What this session did NOT anticipate

Four things, none of which appear in §3, all of which are in the numbers:

1. **T5's precision falls BELOW the base rate** (`0.0714` against `0.0795`). §3 predicted a recall
   failure and said nothing about precision. The consequence is sharper than a recall failure
   alone: T5 on unseen text is not a weak filter, it is an *anti-informative* one.
2. **T2 collapses too** — `0.7333 -> 0.1429` — and §3 never mentioned it. The finding of §4.1 is
   only visible because BOTH open-class tests moved together, and this session predicted neither.
3. **T4's precision rises six-fold** (`0.0259 -> 0.1600`) while remaining noise. A test with no
   mechanism will wander; the wandering is the evidence that it has none.
4. **-89's LOOSE flip does not reproduce.** §3 did not think to ask whether the *surprise* would
   transfer, only whether the headline would.

The pattern in all four: §3 predicted the thing it had been told to predict and was blind to the
comparisons it had not been handed. **The cross-corpus table in §4 is the artefact that caught
them, and it exists only because `wt169` recomputes both corpora in one process instead of
quoting REVIEW-029's numbers.** Recomputing what you could have quoted is what made three of
these four visible.

## 8 · Falsifiers

1. **THE DISCLOSED CONTAMINATION, and it is the strongest attack on this file.** This session read
   `scripts/wt166_pointer_groundtruth.py` in full — `DOC_NOUNS` included — while orienting,
   **before** labelling a single row. No row was checked against the list at labelling time and
   the labels were made from REVIEW-028 §3's rule and the sentences, but the labeller was not
   ignorant of the list, and a labeller who knows the list can favour rows it misses without
   intending to. **The attack: re-label the 88 rows from the TSV's header rule alone, with no
   access to `wt166`, and diff.** A second reader who reproduces 7 POINTERs closes this; one who
   returns 12 with `DOC_NOUNS` words in them destroys §4's headline. The protocol repair is one
   line and is carded: **on a held-out exercise, read the corpus before the instrument.**
2. **Seven positives is a small numerator.** One relabelled row moves T5's recall by 0.14. §4's
   headline survives any single reclassification — T5 would have to gain five of the six it
   missed to reach 1.0000 — but no *rate* here should be quoted to more than one significant
   figure, and this review has quoted four throughout because that is what the instrument prints.
3. **`STRICT` is only four rows.** T6 scores `0.0000 / 0.0000` there, which is a real number about
   a four-element set and nothing more. Do not quote it.
4. **The revision pin is currently INERT.** Papers I and II are byte-identical at `83db4d5` and at
   HEAD, because this session repaired nothing. `wt169`'s drift guard is therefore proved
   non-vacuous by `G5`'s fabricated row (as `wt166`'s `F11` is), but it has not yet been proved by
   a real repair, the way `wt166`'s `F9` is. **The first session to repair one of the seven should
   check that `wt169` still returns RC 0 and that its 88 keys still recompute.**
5. **`G8` guards the word lists and nothing else.** A future session could leave `DOC_NOUNS`
   untouched and change `t5_document_head_noun`'s *matching* — stemming, say — and every digest
   would still pass. The guard covers the data, not the code.
6. **The generalisation in §4.1 rests on two corpora.** "Closed-class transfers, open-class does
   not" is a claim about English, tested on four manuscripts by one author in one programme. It
   is the most interesting sentence in this review and the least supported one.

## 9 · What this closes

REVIEW-027 asked whether the bare-pointer class could be swept. REVIEW-028 found the sweeps were
reading a verb list. REVIEW-029 found that no verb-free structural test recovers the class and
left exactly one usable-looking artefact standing: a document-noun pre-filter with perfect recall
on the corpus it was built against. **That artefact is now measured on text it was not built
against, and it recovers one pointer in seven at below-chance precision.**

So the last mechanical route is closed, and it is closed the useful way — with a number, on
held-out text, by an instrument that refuses to run if its inputs drift. **P7's convergence bar
cannot be met by any instrument this programme can build for this class. A second human reader is
not a nice-to-have; it is the only remaining instrument, and as of this pass there are 429
labelled rows across four manuscripts for that reader to disagree with.**
