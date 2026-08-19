# REVIEW-028 — THE POINTER VOCABULARY: is ten a property of the corpus, or of sixteen surface forms?

*`wealthTensor-88`. §§1–4 were written and committed BEFORE `scripts/wt163_pointer_vocabulary.py`
existed and before any widened sweep was run. §§5–8 were written after. The commit that carries
§§1–4 with the measured reading absent is the git object that makes the prediction falsifiable;
if you are reading this file at a later revision, `git log --follow docs/REVIEW-028-pointer-vocabulary.md`
shows the prediction landing first.*

---

## 1 · The question, and why REVIEW-027's exact agreement could not answer it

`wt160` flags `<VERB> in <TARGET>` where TARGET carries no handle a reader could follow. It
reads **eight commissioned verbs in participle and 3sg-present form only — sixteen surface
forms**: recorded/records, named/names, given/gives, listed/lists, documented/documents,
stated/states, set out/sets out, reported/reports.

`wealthTensor-87` predicted ten flags at `07cd47e` by hand and measured ten, the same ten.
REVIEW-027 §5 says at length why that is the WEAKER result: the prediction was made by pulling
**the same eight verbs** out of the manuscripts, so the agreement tests whether N1–N6 are
applicable by hand — the ADJUDICATION — and cannot test whether the vocabulary is right — the
ENUMERATION. An instrument that reads sixteen surface forms and a hand that reads the same
sixteen surface forms will agree whatever the corpus says.

**So: is the count of ten a property of the CORPUS, or of the WORD LIST?**

## 2 · The design, and the one rule that makes it severe

Three counts of the same thing at the same revision, `07cd47e`, under the same criterion
(same twelve-word window, same clause-boundary rule, same N1–N6 named-target tests). Only the
VOCABULARY differs:

| | vocabulary | how the vocabulary was chosen | count |
|---|---|---|---|
| **A** `wt160` | 16 surface forms | a priori, by `wealthTensor-87` | **10** (published, REVIEW-027) |
| **B** `wt163` | the commissioned widening | a priori, by `wealthTensor-87`'s handoff, BEFORE this session read anything | PENDING |
| **C** the hand | **none** | the corpus's own tokens (see §3) | **14** (§4) |

**THE RULE THAT MAKES THIS SEVERE, and the one REVIEW-027 could not obey: the prediction and
the detector must not share a vocabulary.** B's verb list was fixed by the previous session's
handoff and is reproduced verbatim in §5 — this session did not choose it and did not tune it
after seeing C. C was produced without consulting either list, by the method in §3.

If A ≈ B ≈ C, the count is a property of the corpus: three differently-chosen vocabularies
converge on the same sentences because those are the sentences that are there.
If A ≈ B but C is larger, the count is a property of the word list, and the widening does not
rescue it — because a wider list picked the same way is still a list picked the same way.

## 3 · How C was produced: enumerate by the corpus's tokens, not by anyone's list

The pointer class is `<VERB> in <TARGET>`. The preposition is fixed by the criterion; the verb
is the free parameter under test. So the enumeration was driven by the PREPOSITION:

1. Flatten whitespace in `paper-III.md` and `paper-IV.md` at `07cd47e`. Take **every** token
   immediately preceding ` in ` — 444 occurrences, **264 distinct tokens**. This is the corpus's
   own vocabulary, not anyone's guess at one.
2. Read the 264 by eye and keep every token that could locate content in an artefact. Read every
   instance of each in context.
3. Adjudicate each instance under a rule fixed before the reading and stated here:

> **Count a construction iff (a) it asserts that some content is LOCATED IN a document, artefact,
> run or record — the reader is being asked to go there to check — AND (b) the target as written
> carries no handle a reader could follow (no §, no backtick, no programme identifier, no appendix
> label, no file path, no indefinite head). Temporal (`in advance`, `in 1910`), manner and
> idiomatic (`in isolation`, `in full`, `in place`) and quantitative (`in 11.5%`, `in the mean`)
> uses of `in` are not pointers.**

**The denominator this selects from.** Of the 444 constructions, **341 have a bare target** under
N1–N6 (282 in Paper III, 59 in Paper IV). That number is the honest size of the field, and it is
the reason the verb half of the criterion cannot simply be deleted: `bites in pharmacokinetics`
and `live in different worlds` have bare targets and are not pointers. **The criterion is
irreducibly two-part, and dropping the verb does not make it vocabulary-free — it makes it
useless.** Any successor tempted to "fix" the vocabulary problem by removing the verb list should
read all 341 rows first.

## 4 · C — the fourteen, listed verbatim so the prediction is checkable

Fourteen bare pointers at `07cd47e`. Line numbers are of the flattened text's source line.

**Visible to `wt160`'s sixteen surface forms (ten):**

| # | file | line | construction | target |
|---|---|---|---|---|
| 1 | III | 11 | named in | the data-availability statement |
| 2 | III | 1001 | states in | the table where it belongs |
| 3 | III | 1551 | given in | the two rows above |
| 4 | III | 1608 | given in | the companion papers of this programme |
| 5 | III | 2372 | named in | its own title |
| 6 | III | 2400 | named in | its own title |
| 7 | III | 2529 | named in | the title |
| 8 | IV | 11 | named in | the data-availability statement |
| 9 | IV | 397 | named in | the registration |
| 10 | IV | 444 | stated in | the registration before the numbers existed |

**INVISIBLE to `wt160` — bare pointers whose verb is simply not on the list (four):**

| # | file | line | construction | target |
|---|---|---|---|---|
| 11 | III | 625 | **visible in** | the parameter sweep |
| 12 | III | 1216 | **declared in** | the registration before the pilot was run |
| 13 | III | 2055 | **printed in** | the same logs |
| 14 | IV | 725 | **verified in** | the sessions that introduced them to Papers II or III |

Rows 1–10 are, verbatim, the ten `wt160` measured. **The hand reproduced the instrument's flag
set exactly and then kept going.** That exact reproduction is what licenses rows 11–14: the
adjudication rule is demonstrably the same one the instrument applies, so the four extras differ
from the ten in VOCABULARY and in nothing else.

**Seven disclosed marginals, NOT counted, each with the reason** — disclosed before the
measurement rather than adjudicated after it, on the model of `wt160`'s N4 and N6:

| | construction | why not counted |
|---|---|---|
| M1 | `visible in the theorem's own statement` (III) | the theorem is stated immediately above; self-locating |
| M2 | `visible in the transform` (III) | the transform is the displayed equation in the same paragraph |
| M3 | `established in the same run` (IV) | "the same run" is fixed by the sentence before it |
| M4 | `appears in two registration modules` (IV) | a count, not a location; the reader is not sent anywhere |
| M5 | `quoted in the paper in the form used here` (III refs) | "the paper" is the reference entry's own subject |
| M6 | `verified in the published text at p. 262` (III refs) | substantively named by page number; N1–N6 do not model page cites |
| M7 | `shipped in the same commit (d655501)` (III) | substantively named by commit SHA; N1–N6 do not model SHAs |

M6 and M7 are a **gap in N1–N6, not in the corpus**: a page number and a commit SHA are handles a
reader can follow, and the named-target tests do not know it. Carded rather than patched mid-pass.

---

## 5 · THE PREDICTION — committed before `wt163` existed, measured reading PENDING

`wt163`'s vocabulary is the widening the `wealthTensor-87` handoff commissioned, verbatim and
unaltered by this session: `held in`, `found in`, `described in`, `specified in`, `covered in`,
`shown in`, `presented in`, `laid out in`, `spelled out in`, `set down in`, `collected in`,
`summarised in`, plus the BASE forms of `wt160`'s eight — `record in`, `name in`, `give in`,
`list in`, `document in`, `state in`, `set out in`, `report in` — on top of `wt160`'s sixteen.

**PREDICTED, at `07cd47e`:**

- **B = 13 flags.**
- Of those 13, **10 are exactly `wt160`'s ten** — the widening finds no new REAL pointer.
- The **3 additions all come from `held in`**, and **all three are FALSE POSITIVES**:
  `held in place by a test suite` (idiom), `held in **100%**` (a statistic), `held in the gap and
  released at rate α` (physical, not a pointer). A fourth `held in` — `held in an unrecognised
  gap` — is excluded by N6.
- **The widening catches ZERO of rows 11–14.** None of `visible`, `declared`, `printed`,
  `verified` appears on the commissioned list.
- Of the twelve commissioned additions, **eleven have zero occurrences in the corpus** and one
  (`held in`) has four, none of them pointers. Of the eight base forms, `give in` and `list in`
  and `set out in` occur; the rest have zero.

**PREDICTED VERDICT:** the count is a property of the WORD LIST. Two independently-chosen a
priori vocabularies — sixteen surface forms and roughly forty — return the SAME ten, while a
reading that consults no list at all returns fourteen; and the widening's only three additions
are all false positives, so widening the list moves the count in the WRONG DIRECTION.

**HOW TO MARK THIS WRONG.** If B > 10 by finding a real pointer rows 1–14 do not contain, the
hand reading was incomplete and C is not a denominator. If B = 10 exactly with no `held in`
flags, the false-positive claim is wrong. If any of rows 11–14 turns out to carry a handle this
review missed, C is 13 or fewer and the gap narrows.

**MEASURED: PENDING.**

---

## 6 · MEASURED — and the prediction MISSED, which is the stronger outcome

`wt163` was committed unrun at `ae06184`, after the prediction at `c89f764` and before any
widened sweep existed. Measured at `07cd47e`:

| | vocabulary | how chosen | **flags** |
|---|---|---|---|
| **A** `wt160` | 16 surface forms | a priori, `wealthTensor-87` | **10** |
| **B** `wt163` | ~50 surface forms | a priori, the `-87` handoff | **17** first run, **16** after §6.2 |
| **C** the hand | none — the corpus's own 264 tokens | §3 | **14** |

**B's ten wt160 flags are wt160's ten, verbatim** (post-condition D1, comparing multisets).
**B found ZERO real bare pointers wt160 missed.** Every one of B's six additions is a FALSE
POSITIVE, disclosed with its reason in `docs/pointer-exclusions.tsv`.

### 6.1 · The miss: predicted 13, measured 17

§5 predicted **13** — the ten plus three `held in` false positives. The measurement returned
**17**. **The prediction missed four, and it missed them in the enumeration, which is precisely
the faculty this review was built to test.**

Three of the four are `holds in`: `holds in **100%** of them`, `holds in **66.2%**`, `holds in
all nine is the sign`. The handoff commissioned `held in`; this session mirrored `wt160`'s
participle **and 3sg-present** symmetry onto every commissioned verb — a defensible design
choice, made in the open in `wt163`'s `WIDENING` list — and then wrote §5's arithmetic counting
only the participle. **The author of the word list could not predict what his own word list
would flag.** If the person who wrote the vocabulary cannot enumerate its consequences over a
3,550-line corpus, the proposition that a vocabulary is a way of finding bare pointers is in
serious trouble, and that is the finding.

This is `wealthTensor-87` lesson (i) collecting: an exact agreement built from a shared
vocabulary is weak, and a MISS is informative. REVIEW-027 could not have produced this
information, because its prediction and its detector were the same sixteen forms.

### 6.2 · The fourth miss was better than a miss: a tokenisation defect

The fourth was `specified in four ways` — from **`The instrument was mis-specified in four
ways`**. `\b` matches inside the hyphenated compound, so the matcher read `specified in` out of
a word whose meaning is the **negation** of the verb matched. The lookbehind `(?<![\w-])` fixes
it; `wt163` D12 pins the case, and **D13 proves the guard leaves `wt160`'s published ten at
`07cd47e` untouched (10 → 10)**, which is why it was applied to `wt160` as well and pinned there
as C12. The defect was latent in `wt160` for its whole life and could not fire, because none of
its eight verbs occurs as the tail of a hyphenated compound in this corpus. **A wider vocabulary
did not find a bare pointer; it found a bug in the instrument.** That is a real return on the
widening, and it is not the return the widening was commissioned to produce.

### 6.3 · The verdict, in one sentence someone can mark right or wrong

> **The count of ten is a property of the WORD LIST, not of the corpus: two independently chosen
> a priori vocabularies — sixteen surface forms and roughly fifty — return the SAME ten real
> bare pointers at `07cd47e`, while a reading that consults no list at all returns fourteen; the
> widening's only additions are six false positives, so tripling the vocabulary moved the count
> of real findings by exactly zero and the count of noise by six.**

**10 and 14 are the two numbers that settle it.** 16 is the third, and it is the one that shows
widening is not the repair: the gap between what the lists find (10) and what is there (14) did
not close by a single sentence, and 6 of the 16 flags a successor would have to read are noise.

### 6.4 · Why the verb list cannot simply be deleted

The obvious inference — drop the verb half and flag every bare target — is wrong, and §3
measures how wrong: **341 of the corpus's 444 `<token> in <target>` constructions have a bare
target**. `bites in pharmacokinetics` and `live in different worlds` are among them. The
criterion is irreducibly two-part. **The enumeration cannot be closed by a word list and cannot
be closed by deleting the word list either** — which is why `wt164` repairs by hand and
`wt163` records its own blindness as a post-condition rather than growing to cover it.

---

## 7 · What was repaired

`wt164` (`scripts/wt164_offlist_pointers_repaired.py`, 8 post-conditions, 3 NEGATIVE) repaired
all four off-list bare pointers, in the two sanctioned modes of `docs/CO-AUTHOR-CHARTER.md` §2:

| | mode | before | after |
|---|---|---|---|
| R1 | **remove** | `The reason is visible in the parameter sweep:` | `The reason is that the two monotonicities compound:` |
| R2 | **re-target** | `declared in the registration before the pilot was run` | ``declared in `PRE-001` §4.2 before the pilot was run`` |
| R3 | **re-target** | `printed in the same logs` | ``printed in those same run logs (`docs/preregistration/RESULT-002-*-run.log`)`` |
| R4 | **remove** | `verified in the sessions that introduced them to Papers II or III` | ``verified against the sources the mark table in `docs/REFERENCE-POLICY.md` requires`` |

R1 removes rather than re-targets because **there is no artefact to name**: no committed object
in this repository holds the (φ, δ) sweep the sentence gestured at. Naming one would have been
worse than the gesture. R4 likewise: *sessions* are not openable, and the mark table that
actually defines the tick is.

**`wt164`'s E4 is the post-condition that carries the review's claim.** It requires `wt163`'s
flag set to be **bit-identical** before and after all four repairs — and it is, 6 → 6. An
instrument that noticed these repairs would be an instrument that could have found the defects.
Neither could. That silence is the result, mechanised.

### 7.1 · The three promises the repairs emitted, adjudicated in the same pass

Naming an artefact emits a promise, and `wt148` went red with three of them the moment `wt164`
landed — `wealthTensor-87` lesson (iii), budgeted for this time. `wt165_tsv.py` (13
post-conditions, 4 NEGATIVE) adjudicates all three **H**, keys each sentence off `wt148 --json`
so the text is byte-exact, and runs all three evidence commands inside itself.

**One of the three nearly went in on evidence that refuted it.** The first `PRE-001` evidence
command ran `git log --diff-filter=A` over the registration AND the pilot log **in one
invocation**. That prints two dates newest-first and attributes neither to a file, and read
naively it appeared to show the pilot log entering the repository 35 minutes BEFORE the
registration — i.e. to falsify "before the pilot was run". Split per file it shows the truth:
`9722342` at 17:11:01 added `PRE-001` alone; `d655501` at 17:46:52 added the pilot's run log
together with PRE-002 and the RESULT-001 documents. **A `git log` over several paths yields
dates you cannot attribute**, and an evidence column that cannot attribute its own output is
worse than none, because it reads as diligence. `wt165`'s F3 and F4 require the per-file form.

### 7.2 · Three post-conditions of this session's own were wrong

Counting `wealthTensor-87`'s two, that makes five in two sessions, and none of the five was a
verdict on the repair it guarded.

- **`wt163` D1** compared **sets**, so the two `named in its own title` flags and the two `named
  in the data-availability statement` flags collapsed and `wt160`'s published ten read as
  **eight**. Multisets now.
- **`wt163` D3** pinned the exclusions file to the three rows the prediction named. The
  measurement produced six. Disclosed in §6.1 and in the file's own header rather than absorbed.
- **`wt164` E8** asserted "line-count drift is exactly the three added wraps" and failed at +1,
  because three of the four anchors **already spanned a line break**, so replacing a two-line
  span with a two-line span is net zero. Replaced with a wrap-independent check — flatten the
  pre-repair text, apply the four substitutions, require byte-equality with the flattened
  post-repair text — which is strictly stronger and which the first version should have been.
  `wealthTensor-87` lesson (vii), earned again by the same mechanism.

---

## 8 · Falsifiers

1. **Find a real bare pointer at `07cd47e` that §4's fourteen does not contain.** Then C is not a
   denominator and the 10-vs-14 gap is understated, not overstated. The enumeration in §3 is
   reproducible in one command: take every token before ` in `, read the 264.
2. **Show that one of rows 11–14 carries a handle this review missed.** Then C is 13 or fewer.
   R1 is the softest — someone may hold that "the parameter sweep" is recoverable from §4.4's
   own table; the repair removes the question rather than defending it.
3. **Show that one of the six exclusions is a real pointer.** `holds in all nine is the sign` is
   the softest: "all nine" is nine (α, δ) settings named in the preceding sentence, and a reader
   who thinks that sentence is doing pointer work should say so and the row comes out.
4. **Widen the vocabulary again and find a real pointer.** This review predicts you will not,
   and predicts the marginal return is false positives. `visible`, `declared`, `printed`,
   `verified` are now known — adding *them* is not a test, it is fitting.
5. **Attack §6.4's 341.** If a defensible sub-class of bare targets can be carved out
   structurally — without a verb list — the enumeration problem is soluble and this review's
   pessimism is wrong. That is the single most valuable attack available on this file.
6. **Attack the design itself:** C was produced by the same reader who wrote B's arithmetic.
   The two-independent-readers instrument remains the only real answer, and it remains unbuilt
   and Jason-sized. §6.1's miss is evidence the single reader is fallible in exactly the way
   that design exists to catch.
7. **Attack the tokenisation guard.** `(?<![\w-])` also refuses a match after an underscore or a
   digit. If some legitimate construction begins that way, the guard has cost a flag; D13 shows
   it costs none at `07cd47e`, and says nothing about any other revision.
