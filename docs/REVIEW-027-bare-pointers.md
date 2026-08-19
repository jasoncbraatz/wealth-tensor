# REVIEW-027 · The bare-pointer sweep

*`wealthTensor-87` · 2026-08-18/19 · instrument: `scripts/wt160_bare_pointer_sweep.py`*

**Scope: `paper-III.md` and `paper-IV.md`.** Papers I and II remain out of `#scope`,
deliberately, for the sixth consecutive pass.

---

## 1 · The question, and why no instrument in this repository could already answer it

`wealthTensor-83` read Paper III by hand and found III-2: *"Three post-hoc conjectures
about where the conjunction broke are recorded in the repository's working notes."* They
were not in the working notes; they were in `docs/preregistration/RESULT-002-wt026.md` §4.
REVIEW-023 recorded, in one sentence, why no machine caught it:

> Neither III-2 nor III-3 is reachable by `wt148`: both targets are bare noun phrases, and
> the sweep emits on named artefacts. `wt133` cannot reach III-3 either — its sweep
> resolves `§N.M` forms, and `§10` is a bare section number.

That sentence has sat on the parking lot since -83, through five passes. `wealthTensor-86`
then found the identical defect one level out, in the TSV's own evidence column: `grep -n
E7 on the script` and `grep for each of the three names in the script and the module` read
as perfectly runnable and are not, because **`the script` and `the module` are pronouns
whose referent the reader silently supplies from a neighbouring column**. Two of the three
rows -86's committed prediction missed were missed for exactly that reason.

The defect is one defect wearing two costumes. This pass builds the instrument for the
prose costume.

## 2 · The criterion, fixed before the count was predicted

Over both manuscripts, whitespace flattened so a pointer straddling a line break is still
one pointer, flag every `<VERB> in <TARGET>` where VERB is one of the eight commissioned
pointer verbs — *recorded, named, given, listed, documented, stated, set out, reported* —
or its third-person-singular present form, and TARGET names no checkable handle.

TARGET is read from just after `in ` to the **first** of a clause boundary
(`. ; : ! ? , | ) ] —`) or **twelve words**. The window is deliberately tight: a `§` or a
backtick appearing later in the same sentence must not rescue a pointer whose own target is
bare. That is -86's lesson (i) — *letting a neighbouring column rescue the row collapses
the count to near zero and makes the file unfalsifiable by construction* — and it is
guarded by post-condition **C7**.

A TARGET is NAMED, and so not flagged, when it carries a backticked span (**N1**), a
section reference (**N2**), a programme identifier (**N3**), an appendix label (**N4**), a
bare path with a file extension (**N5**), or an indefinite head — `a`/`an` (**N6**).

**N4 and N6 are the two judgement calls, and both are disclosed here rather than patched in
after the measurement.** N4: `Appendix A` is a unique, resolvable label in the same
document; the reader is not being asked to guess. N6: *"an instrument named in **a paper**
before it is registered"* QUANTIFIES — there is no target the reader must supply, so there
is nothing to repair. Each carries its own NEGATIVE post-condition (C4, C5). Anyone who
thinks either is a bend can delete it and re-run: N4 adds one flag, N6 adds one, and both
are one edit away from being tested.

## 3 · PREDICTED — committed as a git object before the sweep was run

Predicted by reading, not by running: every occurrence of the verb vocabulary was pulled
out of both manuscripts with whitespace flattened, and each of the resulting windows was
adjudicated by hand against §2's criterion.

| | pointer constructions considered | **predicted flags** |
|---|---:|---:|
| `paper-III.md` | 16 | **7** |
| `paper-IV.md` | 3 | **3** |
| **TOTAL** | **19** | **10** |

The seven predicted in Paper III: `named in the data-availability statement` (front
matter); `states in the table where it belongs` (§4.4); `given in the two rows above`
(§7 ledger); `given in the companion papers of this programme` (§9 preamble); and three
reference-entry annotations — `named in its own title` ×2 and `named in the title`.
The three predicted in Paper IV: `named in the data-availability statement` (front
matter); `named in the registration` (§2 instrument); `stated in the registration` (§2
close).

**MEASURED: PENDING.** This section is committed with the field reading PENDING, exactly
as -84 did for its sample and -86 did for its sweep. -86's prediction was wrong by three
and *the three misses were the finding* — which is only true because the prediction was a
git object first.

## 4 · MEASURED

*PENDING — filled in the commit after the sweep runs.*

## 5 · Where predicted and measured disagree

*PENDING.*

## 6 · The severe test in git, and the leg of it that is not satisfiable

-83's III-2 and III-3 were both repaired by `wt151` in commit `908d5b1`. The severe test the
handoff commissioned is: at `908d5b1^` the sweep MUST flag them; at `908d5b1` it MUST NOT.

**The III-2 leg is satisfiable and is in the script as C9/C10.** At the parent the sentence
reads *"...are recorded in the repository's working notes."* — verb in vocabulary, target
bare. At the repair commit it names the file and section.

**The III-3 leg is not, and the rule was not widened to make it pass.** At the parent §8.2
reads *"...after the reading queue in §10 is discharged."* There is no commissioned verb
before `in`, and the target **is** a section reference, so N2 excludes it. III-3's defect is
*resolves-to-the-wrong-thing* — §10 held no queue — which is a different class from
*resolves-to-nothing*, and is the class `wealthTensor-75` already recorded as reachable only
by a reader. **C11 pins that limit as a NEGATIVE post-condition.** Widening a criterion so
that a post-condition passes is the opposite of a severe test.

## 7 · Repairs

*PENDING.*

## 8 · Falsifier block — how to attack this pass

1. **The window is too tight.** Raise `WORD_CAP` past twelve, or drop the boundary set, and
   show that a flag it currently raises has its target named later in the same sentence. If
   one does, that flag is a false positive and the count moves.
2. **N6 is a bend.** Delete the indefinite test and show the flag it adds is a real pointer
   with a real target a reader must supply.
3. **N4 is a bend.** Delete the appendix test and show `Appendix A` is not resolvable.
4. **The vocabulary is arbitrary.** Eight verbs plus their present forms is a choice. Add
   `held in`, `found in`, `described in`, `specified in` and show the count is not a
   property of the corpus but of the word list. **This is the strongest attack available
   and it has not been run.**
5. **C9 proves only that one historical sentence flags.** One recovered defect is not a
   detection rate. This sweep has never been shown to catch a bare pointer nobody had
   already found by hand — until §4's measured flags are adjudicated, that remains true.
6. **The class is not the population.** Nothing here narrows REVIEW-024's [3, 47]; a bare
   pointer is not a false sentence, and a repaired bare pointer may still say something
   false about its newly-named target.
