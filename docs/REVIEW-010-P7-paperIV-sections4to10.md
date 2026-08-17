# REVIEW-010 · `P7` CONVERGENCE PASS 6 — Paper IV, §4–§10 read after the narrowing

*wealthTensor-70 · 2026-08-17 · Paper IV's second read against the **narrowed** framing
(`WT-102`), covering the range `-69` deliberately left. **Three findings, three edits, all
repaired in-pass** (`wt126`), plus **one repair-of-the-repair** (`wt127`) that the board caught
and this session did not. Like `REVIEW-009` this is a **SCOPED** pass — one question, asked of
§4–§10 — not an end-to-end read, so it does **not** advance Paper IV's consecutive-zero count
and does **not** count as a `P7` pass under `WT-091`.*

---

## 0 · What this pass is, and what it deliberately is not

The assigned question, asked of every section from §4 to the end, one section at a time:
**does this prose assert the ladder, or bound a claim the abstract no longer makes?**

Suite before: **1078 passed, 0 failed** (run by this session; number read from the summary line,
not `$?`). Board: **66 criteria, matches measured reality.** Coach: Paper IV
`concessive 0 / conduct_outside_allowed 1`, at baseline. Abstract **238 words / 1585 chars**.

**The assignment named a range that does not exist.** `-69`'s handoff, this file's charter and
the forcing line all say *"§4–§11"*. **Paper IV has ten numbered sections** — §1–§10, then
References. §11 is Paper III's numbering (Paper III's Limitations is §11; Paper IV's is §9,
which `P5h`'s criterion text already records: *"III is 11, IV is 10, II is 7"*). Nothing was
missed by this — the range read was §4 through §10 plus References — but the handoff inherited a
section number from a sibling manuscript and three documents repeated it. Recorded here because
the next reader of that phrase should not go looking for a §11.

**Scope discipline** (`-64`'s tell, `-68`'s amendment). This pass did **not** re-read §4–§10 for
numbers, citations, apparatus or reference formatting. It read them for one shape. §5's arithmetic,
§6's table and §10's commit pin were not re-derived. See §5 below for the full not-checked list.

---

## 1 · The findings

### `IV-14` · §4.1 — the ladder phrase itself, alive in the objection, minus two articles · **REPAIRED**

§4.1 states the objection the paper would deserve, in the referee's voice. Before, its opening
sentence:

> *You claim a unit that **composes from household to sovereign**. But the best-established result
> about aggregation in economics says the opposite.*

That is **the phrase `WT-102` removed**, with both definite articles dropped. `wt120`'s census
searched for *"from the household to the sovereign"* and reported it gone from `paper-IV.md`;
that report was true, and it was true of a string that differs from this one by two function
words. `-69`'s tell said *a paraphrase has no string*. This is the sharper case: **the paraphrase
had a string, and it was not the one anybody censused.**

The severity is higher than its position suggests. §4.1 is not a stray sentence — it is the paper
**putting words in a referee's mouth about what the paper claims**, and it is the strongest such
statement in the manuscript, since §4.1's whole purpose is to state the claim at maximum
exposure. After `wt121` the abstract and §4.1 disagreed about what is being claimed, and **§4.1
is the one that reads as the paper's real position**, with the abstract as the hedge — the exact
inversion `WT-102` was written to prevent.

After:

> *You claim a unit that **keeps one type at the household, firm and sovereign scales and
> survives being summed**. But the best-established result about aggregation in economics says the
> opposite.*

Nothing was softened. The objection is **stronger** in the new wording, because "survives being
summed" lands directly on the paragraph's own closing line — *"you cannot cite the theorem that
aggregation destroys structure and then claim structure survives aggregation"* — which the old
opening reached only by implication. The rest of the paragraph is unchanged; `wt126` asserts that
mechanically, comparing the normalised text after the first sentence in anchor and replacement,
because the repair rewraps eight lines and a rewrap is an excellent place to hide an edit.

### `IV-15` · §8 — a cross-reference that `wt125` falsified two hours before this session opened · **REPAIRED**

§8's chain entry, before:

> What is left is weaker, **is what §3 now says**, and is still worth publishing: one question,
> asked at three scales, answered quantitatively at each.

`wt125`'s `ED2` — `-69`'s own repair, landed the same day — added a third conjunct to §3's
closing: *"the question, the fact that each scale answers it quantitatively, **and the addition of
§2.2**"*. From that moment the colon-list above stopped being what §3 says.

**`-69` discovered the species and generated a fresh instance of it, one section outside the
range it was reading.** `REVIEW-009` §1 states the mechanism exactly — *a framing patch's blast
radius is every line that agreed with the old framing in its own words* — and the blast radius of
`wt125` reached §8 while `-69` was writing that sentence about `wt121`. The scope note in
`REVIEW-009` §5 is honest about not having opened §4–§11; what neither document could see is that
a repair inside the read range had reached outside it.

Repaired by **deleting** the cross-reference, not by resyncing it (`WT-098`, third application):

> What is left is weaker and is still worth publishing: one question, asked at three scales,
> answered quantitatively at each.

§8's entry already names §3 in its first sentence, so nothing is lost. And the clause was a
**standing drift generator**: a paraphrase of another section's content has to be re-synced every
time that section moves, and nothing in the tree measures whether it has been. Resyncing it would
have bought one correct sentence and left the generator running.

### `IV-16` · §9 — the Limitations section does not carry the limitation the abstract advertises · **REPAIRED**

The narrowed abstract makes exactly two headline statements, and the second is a **limit**:

> This paper joins them on one claim — the same atomic **state** has one type at the household,
> firm and sovereign scales — **and on one limit its own end-to-end test imposed: those scales
> share one question, not one structure.**

§9 is titled *Limitations*. It carried seven items. **None of them was that one.** The limit lived
in a §3 paragraph and in §8's abandonments — both correct places for it to *also* live, neither
the section a referee opens when checking whether a paper honours its own stated bound. §4.4's
heading (*"The limits of the resolution, stated here rather than in §9"*) shows the paper treats
§9 as the default home for limits and **announces** departures from it; this departure was never
announced, because before `wt121` the limit was a mid-section demotion rather than an
abstract-level claim. **The narrowing promoted it and no one moved it.**

Repaired by adding it to §9, worded from §3 and §8 so that **nothing new is asserted** —
`END-TO-END-001` leg `E1`'s finding, the deferred-vs-never-assessed contrast, and the absence of
a counterpart to α, all of which the manuscript already states elsewhere. §9 now carries eight
items.

---

## 2 · The repair, its guards, and the guard that was not in the kit

`scripts/wt126_paperIV_p7_sections4to10.py`, full kit per `wt125`: census first (`WT-099`),
`.bak` first, anchors asserted `== 1` literal *and* normalised, idempotence guard normalised and
**ASSERTED — fired, exit 2**, glyph guard, width guard as a **set**, G-COACH guard document-wide.
Two guards are new and both earned their place:

- **An identity guard on the renumber.** `ED3` inserts an item and shifts seven ordinals. The
  guard asserts the **list of item bodies** after the edit equals the list before plus exactly
  the one new body. A count guard (*"8 items where there were 7"*) passes while silently eating
  item 5; `WT-108` and `-69(ii)` say guard over sets and identities, and this is that rule applied
  to a list rather than to a document's self-references.
- **A rewrap guard on `ED1`.** The normalised text following the changed first sentence must be
  identical in anchor and replacement. Without it, an eight-line rewrap is unreviewable by eye.

### The census needed a third category, and the first `--dry` proved it

`wt126`'s first `--dry` failed its own census assertion, correctly and uselessly: `ED1`'s anchor
occurs in **nine** `paper-IV.md.bak-*` files and `ED2`'s in seven plus
`scripts/patch_wt56_e1_remedy.py`. The guard as first written said *"the anchor must occur in one
file"*, which is false of **every** anchor in this corpus, because the corpus deliberately keeps
its own undo paths and its own spent one-shots.

The fix is not to loosen the assertion but to **classify**: `live` / `historical (.bak-*)` /
`spent one-shot`, printed separately, with uniqueness asserted **only** over live. Same species as
`-66b`'s census rule and `REVIEW-009` §4's width guard — *an instrument must distinguish what it
found from what was already there.* A census that folds the `.bak` files into the live count makes
every anchor look ambiguous; one that drops them silently makes a genuine live duplicate
invisible.

`patch_wt56_e1_remedy.py`'s status is settled (`REVIEW-009` §3): its quoted text is a record of
what the paper said when it ran, and it is left alone. `wt126` **re-verifies rather than inherits**
that it is dead code, by looking for its name on a line that also carries an execution verb — a
line that merely names it (`wt125`'s docstring does) is a citation, not a caller. *Someone checked
once* is not a guard.

### And then the board caught what none of the guards could: an ORDINAL

`wt126`'s `ED3` placed the new limitation **first**, reasoning that §9 is ordered by weight and
the abstract ranks that limit second of its two headline statements. Every guard passed. The suite
passed, 1078. Then `regen-board.sh --check` went **STALE** and **`P5g` flipped ✅ → 🔨** — the
first board movement in five sessions, caused by an insertion that changed no sentence.

`P5g` is *"Limitations is a numbered list and THE FIRST ITEM runs against the paper's own
comfort"*, and its check greps **item 1 specifically** for `A composed state nobody can read`.

**A census and an identity guard prove what the text SAYS; neither looks at WHERE IT SITS.**
`wt126` asserted that every pre-existing §9 body survived byte-identically under the renumber, and
every one of them did. What moved was an **ordinal** — and in a corpus that measures list position,
an ordinal is a criterion. **Any insertion at the head of a numbered list in a manuscript is an
edit to a criterion, not just to prose.**

`scripts/wt127_paperIV_sec9_order.py` moves the new item to position 2. Two things it deliberately
does not do:

- **It does not reword the new item to carry `P5g`'s phrase.** That would satisfy the checker while
  demoting the item the criterion exists to protect — gaming a green, which is the species
  `-66b` named.
- **It does not edit `wt126`.** `wt126` ran; editing a spent script falsifies the record of what
  ran (`-69`'s ruling on `wt124`, kept). The two-script trail *is* the finding.

`wt127` guards the swap on the **multiset** of item bodies plus the exact new order, and asserts
that a pure reordering leaves the paper's word multiset unchanged. Idempotence is checked on
**position**, since no body changes — a content sentinel would be blind here.

### Verification after both scripts

Suite **1078 passed, 0 failed**. `regen-board.sh --check` **66 criteria, matches measured
reality**, and `docs/CHECKLIST.md` is **byte-identical to `HEAD`** — the board is unmoved for the
**fifth** straight session, which is now a datum collected across a session that moved it and put
it back. Coach **paper-IV 0 concessive / 1 conduct, at baseline**, no refresh. Abstract **238
words, 1585 chars**, untouched — checked anyway, per `-68`'s rule.

---

## 3 · What was read and CLEARED — the part that is a result, not an absence

`-69`'s handoff named §4.4 and §9 as the *likeliest* sites, on the reasoning that a section
written to **bound** a claim may re-assert the claim in order to bound it. That prediction was
half right — §9's defect was an **omission**, not an assertion — and the two specific suspicions
were both checked and both cleared:

- **§4.4's *"the composition claim therefore has a degraded link at exactly the scale where the
  accounting is done"*** reads at first as chain imagery, and §8 records *"a chain rather than
  three analogies"* as an **abandoned** framing. It is not the chain. §3 uses "link" three times
  (L209, L226, L243) for the **within-scale** claim that a firm's reporting composes from its
  classes' reporting without cross-terms — the Hadamard diagonality — and §4.4's usage is that
  same object, as is §9's. A link **at** a scale is not a link **between** scales. Cleared on
  §3's own usage, not on impression.
- **§4.4's *"Paper III's ladder results"*** collides with "the ladder" as this project's name for
  the framing defect, which is a genuine reading hazard for anyone working from `WT-102`. It is
  **Paper III's own established term**: `paper-III.md` uses ladder/rung 56 times for the ordering
  of asset classes by durability (*"falling up the ladder"*, *"at every rung"*, *"400 randomly
  drawn admissible ladders"*). Renaming it in Paper IV to spare a reviewer's ear would desynchronise
  a cross-manuscript term. **Left alone deliberately, and named here so the next pass does not
  re-open it.**
- **§7's relocation method — read end-to-end, zero findings.** Named as unread in `REVIEW-009` §5.
  Its four relocations (Piketty, Solow, the Austrian account, SMD) turn on *differently
  constrained case*, not on derivation between scales, and its closing paragraph on aggregation
  states the post-narrowing position exactly: *"SMD is the theorem for the map, this framework is
  the claim for the state, and neither implies the other."*
- **§5's worked instance — read end-to-end, zero findings.** Also named as unread. Its composition
  language (*"read as a composition statement"*, *"the behavioural map stops composing"*) is about
  a single market at a single scale.
- **§4.2, §4.3, §6, §10 — read end-to-end, zero findings.** §4.2's *"aggregation preserves the
  extensive state and destroys the behavioural map"* is the narrowed claim stated correctly and is
  the sentence the rest of the paper should be measured against.

**Four of the seven sections read produced nothing, including the two `REVIEW-009` flagged as
unread and one of the two it flagged as likely.** That is the honest shape of this pass: the
defects were not where the prediction put them, and the prediction is still what made them
findable, because it is what got §4 and §9 opened at all.

---

## 4 · What this pass did NOT do

Stated explicitly, because a pass's coverage is shaped by its question and an unstated scope reads
as full coverage (`-64`).

- **The single question was the framing.** §4–§10 were **not** re-read for numbers, citations,
  apparatus, reference formatting or internal arithmetic. §5's 25/399/500 figures, §6's overlap
  table and *z* values, §9's 4.12×/2.02×/*p* = 0.0002 and §10's commit pin `5efe626` were
  **not** re-derived or re-verified.
- **References were not read.** The bibliography cannot assert a framing, so it is vacuous for
  this question — but it is also the subject of a live open item (`REFERENCE-POLICY`'s sixth pass,
  card `1217556161163494`, **fifth** session it would have saved) and this pass did not do it.
- **§1–§3 were not re-read.** They are `REVIEW-009`'s range and are treated as propagated. `IV-15`
  is evidence that a repair inside a read range can land outside it, so *"propagated"* means
  *"read after the narrowing"*, not *"read after `wt125`"*. **Nobody has read §1–§3 against
  `wt125`'s own output.** This is a small range and a real gap.
- **The other manuscripts were not checked for Paper IV's old framing.** `REVIEW-009` §5 left this
  open and it stays open. `wt120`'s census classified fourteen non-`paper-IV` occurrences as
  historical records — **a classification made about the string, not about paraphrases**, and
  `IV-14` is now direct evidence that the censused string was not the only string.
- **The content-word census across all four manuscripts WAS run, and is a zero.** Named here
  because it started life on this list. `IV-14` proved the censused string was not the only
  string, so the check was redone over content words in order rather than over the phrase as
  typed — `compos[a-z]*.{0,60}household.{0,60}sovereign` and its reverse and
  `household.{0,40}to.{0,20}sovereign`, whitespace-collapsed first so a line wrap cannot hide a
  match (`-62`). **Papers I, II and III: zero hits each.** Paper IV: two, both correct
  post-narrowing text — the title's *"one atomic unit at the household, firm and sovereign
  scales"* and §3's *"a composition quantity: it is defined at the sovereign scale and it is a
  fold over household-scale liabilities"*, which is the addition claim stated properly. **The
  ladder is gone from the manuscripts in every form searched for.** What remains unsearched is
  paraphrase without those three content words, which is the residue `-69`'s tell describes and
  no grep reaches.
- **Paper I still has no `P7` pass at all.**
- **Paper II's third independent read did not happen this session.** Untouched since `-68`, so the
  eyes are as fresh as they were.
