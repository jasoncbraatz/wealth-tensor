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

**MEASURED: was PENDING at `07cd47e`; §4 fills it.** This section was committed with the field
reading PENDING and the table above already frozen, exactly
as -84 did for its sample and -86 did for its sweep. -86's prediction was wrong by three
and *the three misses were the finding* — which is only true because the prediction was a
git object first.

## 4 · MEASURED

`python3 scripts/wt160_bare_pointer_sweep.py` — RC 1, all eleven post-conditions holding,
six of them NEGATIVE.

| | considered | predicted | **measured** |
|---|---:|---:|---:|
| `paper-III.md` | 16 | 7 | **7** |
| `paper-IV.md` | 3 | 3 | **3** |
| **TOTAL** | **19** | **10** | **10** |

The ten, in file order:

| # | file | line | pointer | what the reader had to supply |
|---|---|---:|---|---|
| 1 | III | 11 | `named in the data-availability statement` | which section that is |
| 2 | III | 1001 | `states in the table where it belongs` | which table |
| 3 | III | 1551 | `given in the two rows above` | which rows — **and they are the wrong ones** |
| 4 | III | 1608 | `given in the companion papers of this programme` | which paper, which section |
| 5 | III | 2372 | `named in its own title` | the phrase itself |
| 6 | III | 2400 | `named in its own title` | the phrase itself |
| 7 | III | 2529 | `named in the title` | the phrase itself |
| 8 | IV | 11 | `named in the data-availability statement` | which section |
| 9 | IV | 397 | `named in the registration` | which registration |
| 10 | IV | 444 | `stated in the registration before the numbers existed` | which registration |

## 5 · Where predicted and measured disagree — and why the agreement is the weaker result

**They do not disagree. Ten predicted, ten measured, and the same ten.** The considered
count agrees too, at nineteen.

That is a worse outcome than -86's, and it is worth being precise about why. -86 predicted
43 and measured 46, and **the three misses were the finding** — they exposed a class
(pronoun targets) the author had read straight past. An exact agreement exposes nothing.
Worse, the prediction and the sweep share a blind spot **by construction**: the prediction
was made by pulling every occurrence of *the same verb vocabulary the script uses* out of
both manuscripts with whitespace flattened, and adjudicating each window by hand. So the
agreement is evidence that **N1–N6 are applicable by a human without ambiguity** — which is
worth having, since a criterion two readers apply differently is not a criterion — and it is
**no evidence at all** that the vocabulary is the right vocabulary. A pointer verb outside
the eight is invisible to the prediction and to the sweep alike.

That is falsifier #4 in §8, and it is the live attack on this pass. `held in`, `found in`,
`described in`, `specified in`, `covered in` are all pointer verbs in ordinary English, and
none of them was run.

**One thing the sweep did find that no reader had:** flag 3. See §7.

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

## 7 · Repairs — `wt161` (13 post-conditions, 4 NEGATIVE) and `wt162` (12, 4 NEGATIVE)

All ten repaired in-pass, in the two sanctioned modes: **four pointers re-targeted** so the
target is named, and **six constructions removed outright** so the sentence stops promising a
target at all. `wt160`'s considered count therefore falls from 19 to 13, and its flagged
count to zero.

### 7.1 · The one that was not merely vague

Paper III §7's ledger row *"The repair's strength is the asset's, not the analyst's"* read:

> …regime-independent; the σ exponents are not, and **are given in the two rows above**.

The two rows above it are *"Returns cannot touch the scale continuum"* and *"News, not
returns, restores identification"*. **Neither carries an exponent in σ.** The σ exponents are
two rows **below** — *"Neither degradation exponent is a model constant"* (collinearity spans
−1.07 to −0.38, se(φ̂) −0.78 to −0.09) and *"The response to news flattens as decay slows"* —
and §4.7 states both ranges in prose. The pointer resolved to the wrong place: **the III-2
class exactly, found this time by a machine rather than by a reader.** Repaired to
*"and §4.7 gives both ranges"*, with post-condition D3 asserting §4.7 still states both.

This is the answer to -83's open question about whether an instrument for this class would
ever earn its keep. One defect is not a rate, and §8's falsifier 5 still stands.

### 7.2 · The other nine

| # | repair | mode |
|---|---|---|
| 1, 8 | `named in §11` (III) / `named in §10` (IV) | re-targeted |
| 2 | `which §4.4's tier table now states` | construction removed |
| 4 | the companions' own sentence stated inline — *"a result reported without the routes that failed is a result the reader cannot calibrate"* — instead of pointed at | construction removed |
| 5, 6, 7 | the title's phrase quoted (*the asymmetric timeliness of earnings*; *biases and lags in book value*; *L = λW*) | construction removed |
| 9, 10 | `named in \`REG-013\`` / `stated in \`REG-013\`` | re-targeted |

### 7.3 · RED-PROOF, and the two post-conditions that were wrong

`wt161` refuses to touch anything unless `wt160`'s flag set is EXACTLY the ten it is written
against, and after repairing it re-runs `wt160` at `07cd47e` — the pre-repair commit — and
requires all ten to flag **there** still. The repair moves the file, not the instrument.

**Its first run rolled back on three post-conditions, and two of the three were the
post-condition's error rather than the repair's.** D1 asserted 19 constructions would remain
considered; 13 do, because six repairs removed the construction rather than re-targeting it —
a mode the criterion sanctions and the post-condition had not been written to expect. D6's
anchor spanned a line break in `paper-IV.md` and so was never found. **D13 was right**: `wt148`
went non-zero, because naming `REG-013` in two sentences **emitted two promises**, which is the
repair working, not failing. Those two are adjudicated by `wt162` against evidence that is run
inside the script itself (E7, E8) — the seed titles matched verbatim against `REG-013` with
whitespace flattened (T 7/7, S 5/6, K 5/6, X 0/6, with every zero and every miss explained in
the note), and the registration's own fertility disclaimer alongside the two add-dates that
put `REG-013` in the repository sixteen minutes before the numbers.

A repair that makes prose checkable **adds** rows to the adjudication file. That is the cost
of the criterion and it is the right cost.

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
6. **One recovered defect is not a detection rate.** §7.1 is one wrong pointer in ten flags in
   two manuscripts. Nothing here estimates how many more of its kind exist, and a bare pointer
   that happened to resolve correctly was repaired without anyone learning anything.
7. **The class is not the population.** Nothing here narrows REVIEW-024's [3, 47]; a bare
   pointer is not a false sentence, and a repaired bare pointer may still say something
   false about its newly-named target.
