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

## 6 · MEASURED

*PENDING — written after `wt163` is committed and run.*

## 7 · What was repaired

*PENDING.*

## 8 · Falsifiers

*PENDING.*
