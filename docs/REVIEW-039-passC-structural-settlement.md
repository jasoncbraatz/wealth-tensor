# REVIEW-039 · PASS C — the structural settlement, item by item

**`wealthTensor-105`, 2026-08-24.** Pass C of `docs/DEFINITION-OF-DONE-SHIP.md` § 3. This file is
the **enumeration** of the C-d and C-c work, which `REVIEW-038` § 4 counted and did not name.

---

## 0 · THE HEADLINE, STATED LOUDLY BECAUSE § 3.5 ASKS FOR IT

**THE FOURTEEN CAME BACK AS TWENTY-FOUR, AND THE REASON IS NOT THAT PASS A COUNTED BADLY.**

`REVIEW-038` § 4 reports a **count per type per paper** — 13 C-d and 1 C-c — and § 4 opens with
*"Counted, not repaired."* The handoff into this session said *"THEY ARE ALREADY FOUND. Pass A
counted them and named them. You are not searching; you are reordering."* **The first half is
true and the second is not.** Only ONE of the fourteen carries a location anywhere in the
corpus: the C-c orphan at paper-IV's *"Paper III's ladder results"*. The other thirteen exist as
a number in a table.

**So Pass C's first half-day was the search Pass A had already done once, redone.** That is the
cost worth carrying forward, and `REVIEW-038` § 4.4 half-predicted it — *"C-a, C-c and C-d are
the judgement calls, and C-d is the one that matters most to Pass C, so Pass C should expect to
find fold problems this sweep missed and should not treat 13 as a ceiling."* It was right. The
ceiling was not 13.

**THE GENERAL SHAPE, WHICH IS THE PART THAT OUTLIVES THIS CORPUS: A COUNT IS A SIZE ESTIMATE AND
AN ENUMERATION IS A WORK ORDER, AND A HANDOFF THAT PROMISES THE SECOND WHILE CARRYING THE FIRST
COSTS ITS SUCCESSOR THE WHOLE SEARCH.** A rough count genuinely does beat an elegant absence of
one — `REVIEW-038` § 4.4's own line, and it held. What it does not beat is a rough LIST. The two
cost the counting pass almost the same, because the pass that counts has each item in front of it
at the moment it increments.

**None of this is a stall.** Pass D's precondition is met — § 5 below answers it per manuscript,
in the words § 3.0 requires.

---

## 1 · WHAT WAS FIXED — twenty-four structural items

Repairs follow § 2.5's prescription: **C-d reorders, C-c anchors or cuts.** Where a fold's honest
repair was to move a DEFINITION forward rather than to move a SECTION, that is what was done and
the reason is in § 3.

### paper-II — 4 items (census said 2 C-d, 0 C-c)

| # | type | the fold | repair |
|---|---|---|---|
| II-1 | C-d | § 3.1's table carries a **`bounded`** verdict column; the criterion producing it is defined only in § 3.4, three subsections later. § 2.4 is titled *What is measured* and did not carry it. | **REORDER.** § 2.4 now states the criterion — settled Gini **and** top decile below 0.90 — before any table adjudicates on it. § 3.4 keeps the *result* that a settled Gini alone does not separate. |
| II-2 | C-d | **Var[log *a*]**, a co-equal witness to κ in § 3.1 and § 6, was defined mid-result inside § 3.1 while § 2.4 read as a closed inventory of three statistics. | **REORDER.** § 2.4 defines it as the fourth measured quantity, including the *a*/*a*(η) letter collision. § 3.1 now points at § 2.4 instead of re-defining. |
| II-3 | C-d | § 3.1's *"κ is necessary and it is not sufficient"* paragraph rests on § 3.3's threshold numbers (0.444 against 0.443) two subsections before § 3.3 reports them. | **REORDER.** The paragraph moved to the end of § 3.3, where both of its legs are on the page. Its internal anchors were rewritten from *"the paragraph above"* to named sections. |
| II-4 | precision | § 1's contribution 2 says the Bouchaud–Mézard contrast *"is credited in § 6"*; the full credit is carried in § 3.1 as well. | **REPLACE.** *"credited where it is used, in § 3.1, and again in § 6"*. |

### paper-III — 11 items (census said 7 C-d, 0 C-c) — plus 2 S1s, § 2

| # | type | the fold | repair |
|---|---|---|---|
| III-1 | C-d | The **lag statistic** is tabulated in § 3.1 and reasoned about through § 4; its construction (a cross-correlation of ΔE and ΔC) is stated only in § 4.5, ~460 lines later, and delivered there as a gotcha. | **REORDER.** § 3.1 states the construction before its own table. § 4.5 keeps the consequence — *ΔE is what no filing reports* — which is the finding. |
| III-2 | C-c | **⊘** appears three times in the abstract and § 1 and is defined nowhere; ⊙ is defined at § 4.1 and § 4.3 silently abandons ⊘ for prose. | **ANCHOR.** § 4.1 defines both operators; the abstract's first use carries *"both operators elementwise across classes"*. |
| III-3 | C-d | § 4.4 leans on **α̂ = 0.408** — sample, estimator and censoring rule all in § 5.4, ~800 lines on. | **REORDER of the definition.** § 4.4 names the registered sample (695 impairment events), the interval, the twenty-quarter censoring and the censored geometric MLE at first use. PRE-002's attribution retained — see § 4. |
| III-3b | C-c | *"the unregistered adverse cut"* has no referent until § 5.4. | **ANCHOR.** Glossed in place as a refit of the same sample with the 175 one-quarter events dropped. |
| III-4 | C-d | § 4.9 **opens** on § 5.4's discrete-Weibull fit — k̂, its profile interval and its truncation robustness — before the reader has the sample or the family. | **REORDER of the definition.** The fit is named before its result, and *"a constant hazard is k = 1"* makes the rejection legible in place. |
| III-5 | C-d | § 2's domain restriction — the model predicts nothing where a loss is estimable — is stated in § 10, while § 5.1 points at *"§ 10's restriction"* 740 lines earlier. | **REORDER.** The restriction is stated in § 2 with the model. § 10 keeps the Basu credit and points back rather than restating. |
| III-6 | C-c | § 3.1's column *"inter-period smoothing"* is defined nowhere; § 3.2's near-identical column is called *"inter-event smoothing"*. | **ANCHOR.** Both are `variance_suppression` under two regimes, verified in `src/wealth_tensor/lag.py`. § 3.1 now says so and defines the statistic once. |
| III-7 | C-d | **η**, **Λ** and **P1** are used in §§ 7, 9 and 10 and defined only in Appendix A. | **ANCHOR at first use** — η in § 7's ledger row, Λ in § 9's fifth limitation — plus the § 1 S1 below. The appendix did not move. |
| III-9 | C-d | The condition making § 2's wedge one-signed — no upward revaluation, no impairment reversal, and its US-GAAP dependence — is disclosed in § 10, as a concession to a rival literature. | **REORDER.** Stated in § 2 as the modelling assumption it is. |
| III-10 | C-c | *"the registered floor of 30"* appears once, unstated and unsourced. | **ANCHOR.** Glossed as the minimum events a life band must carry before a within-band comparison runs. |

### paper-IV — 9 items (census said 4 C-d, 1 C-c)

| # | type | the fold | repair |
|---|---|---|---|
| IV-1 | C-d | § 1 says *"the fourth paper's apparatus"* with a definite article; the fourth paper is introduced in § 8, seven sections later. § 10 handles the same reference correctly. | **REORDER.** § 1 names it — *a fourth paper on price formation, written, refereed against itself and not published, for the reasons § 8 gives*. |
| IV-2 | C-d | § 3's Household paragraph reports **α = 0.05**, a measured counterpart and a verdict, before the Firm paragraph defines what α names. | **REORDER of the definition.** α glossed at first use as the release rate of a change incurred but not recorded. |
| IV-3 | C-d | § 3 announces a rejection *"the paragraph after next"* reports, with an unrelated paragraph wedged between — a fold patched with a pointer rather than fixed. | **REORDER.** The `END-TO-END-001` demotion paragraph moved ahead of *"Note what this is"*, which it sets up; the pointer is now *"the next paragraph"*. |
| IV-4 | C-d | § 6's table carries a **position *z*** column and is judged against a 0.10 bar; neither is defined until after the table. | **REORDER.** Both stated before the table, with the undecided band, which § 6's own qualification paragraph needs. **The first draft of this repair was WRONG and was caught by its own wt148 row** — see § 2. |
| IV-5 | C-d | § 6's floor rests on a 4 000-work audience cap disclosed two paragraphs later. | **REORDER.** The truncation is disclosed where audiences are defined. |
| IV-6 | **C-c** | **The one orphan the census named.** *"Paper III's ladder results"* — used once, defined nowhere, and the sole evidence for its limitation. | **ANCHOR.** Given its content in place, from paper-III § 4.3: a cross-class ranking reads the product φ ⊙ δ, so it recovers a ranking of φ only where δ is constant across the classes ranked. |
| IV-7 | C-c | **Λ** carries § 7's only concrete contact with the biophysical literature and is defined nowhere in this manuscript. | **ANCHOR.** Glossed as energy per unit of recorded economic stock. |
| IV-8 | C-c | § 4.1's objection — staged as the strongest thing anyone will say — turns on *"your own Paper I"*, a document this manuscript never identifies and the References never list. | **ANCHOR.** Recast onto the corpus's own price-formation paper, which § 8 records. |
| IV-9 | C-c | § 5's heading promises *"the volume"*; the word appears nowhere in the section. | **ANCHOR.** The quantity coordinate is named as the volume traded at the crossing. |

---

## 2 · TWO S1s FOUND AND REPAIRED IN-SESSION (DoD § 1.2's successor rule)

Half 1 is *"one read per manuscript against the frozen instrument set."* Both of these came out of
that read. Neither is on `SHIP-LIST.md` and neither reopens it: § 1.2 sends post-freeze findings to
POST-SHIP, and § 3 Pass C sends S1/S2 to a repair **in the same session**. That is what happened.

**S1-a · a cross-reference that resolves to nothing, at two sites.** paper-III § 4.7 said *"So
§ 4.6's question answers yes"*, and § 7's ledger said *"which would leave § 4.6's question open the
other way."* **§ 4.6 poses no question. There is no question mark anywhere in §§ 4.1–4.6.** DoD § 2
names *"a cross-reference that resolves to the wrong place"* as an S1 example verbatim. Repaired at
BOTH sites — § 4.7's prose now states the question it is answering, and the ledger row points at
§ 4.7 — because a repair landing at one site leaves the document asserting both, which is `SL-9`'s
lesson.

**S1-b · a promise the manuscript breaks two sections later.** paper-III § 1 said *"Nothing in
§§ 2–7 depends on"* Appendix A. **§ 7's survival ledger carries two rows whose entire content is a
claim about η, which is defined only in Appendix A.** Repaired by making the promise true rather
than by moving the appendix: *"No result in §§ 2–6 depends on it… § 7's survival ledger records the
appendix's own checks alongside the rest, and §§ 9 and 10 name the propositions where they bound
what may be claimed."* P1–P3 are also named at that first use, so § 9's and § 10's uses have an
antecedent.

**A third defect was caught by the promise ledger before it could become an S1, and it is the most
useful thing in this file.** IV-4's first draft wrote *z* as *"the overlap divided by the pooled
ceiling."* `REG-013` § 4 defines **z = (O − F)/(P − F)**. The two agree **only because this run's
floor came out at exactly 0.000** — so the sentence was true of the numbers and false of the
construction. It was caught by writing the wt148 row, which forced the registration to be re-read.
**THE ROW IS NOT BOOKKEEPING THAT FOLLOWS THE REPAIR; IT IS PART OF THE REPAIR.**

---

## 3 · THE ONE JUDGEMENT CALL, NAMED SO PASS D AND JASON CAN OVERRULE IT

**Four folds (III-3, III-4, and the shape behind III-1 and III-5) are forward dependencies from
§ 4 onto § 5.4's empirical fit.** The literal § 2.5 repair for C-d is *"Reorder"*, and the maximal
reading of that is to move § 4.9 and § 4.10 after § 5.4.

**That was considered and not done, and here is the reasoning.** § 4 is the identification theory
and § 5 is the severe test; § 4.9 and § 4.10 are about what the closed form assumes, which is § 4's
subject. Moving them would renumber every section the rest of the corpus and the instrument set
point at, to relocate paragraphs that are thematically where they belong. **What actually made a
first-time reader stumble was never the forward pointer — a long paper may point forward — it was
that the pointer arrived carrying an unevaluable number and an undefined term.** So the repair was
to move the DEFINITION forward to the point of use in each case, leaving the section order alone.

**This is a decision, not an omission, and it is the reason § 5 can answer Pass D's precondition
in the affirmative.** If Pass D reads § 4 at thirty thousand feet and finds the § 4 → § 5.4
dependency still costs the reader, that is a section move and it belongs to Jason's ruling, not to
a fourth session doing it quietly.

---

## 4 · WHAT THE REPAIRS COST — the second job, budgeted as work

`-104`'s finding was that a repair pass on a heavily-guarded corpus is two jobs. It is still two
jobs, and the second one behaved exactly as its handoff predicted.

* **Five wt148 promises re-minted, four rows retired with lineage markers**, every one of the five
  with its evidence RE-RUN before the row was written (`wt089` for both PRE-002 rows, `REG-003`
  § 3.3 and `REG-013` § 4 read, the § 10 record bullet printed).
* **Two of the repairs were WEAKENED by their own first draft and restored.** Rewriting § 4.4's and
  § 4.9's sentences to add the sample and the estimator dropped the words *PRE-002's instrument* —
  which is a provenance loss traded for a legibility gain. Both were rewritten to carry BOTH.
  **A C-d repair that silently deletes an attribution has not repaired anything.**
* **One repair created a defect in a guard's own class.** § 3.1's new gloss contained *"names in
  this paper"*, which `wt160` and `wt163` correctly read as a bare pointer. **The guard was right
  and the prose was wrong** — the first time in eight instances of this repo's standing tell that
  it has run that way round. Repaired by rewriting the sentence, not the vocabulary.
* **Two guards were red and were wrong about the file** — the seventh and eighth instances, now
  ninth and tenth. Both closed by a TIGHTER subject, in the same session that reddened them:
  * `wt182` failed its IV-12a **precondition** at 0 occurrences with every edit intact, because its
    idempotence test recognises a landed repair by the whole wrapped paragraph. `-104` flattened
    whitespace here, which fixed the REFLOW case and left the REWORD case — and teed it up. This
    session hit it. Repaired with a `LANDED` marker per tag: the **distinctive claim** each repair
    introduced, which is also that repair's own postcondition subject, so *applied* and *passes*
    cannot disagree. `scripts/wt200_wt182_landed_markers.py`.
  * `wt188` failed three checks. Two were pinned to the literal count **11** of `wt184` RULE-1
    flags on paper-II; the finding was never the number, it was that **every** flag is a
    co-occurrence false positive. Re-asserted as `elsewhere == num_flag > 0`, and the count is
    printed rather than pinned — it reads **12** today. The third, *"papers I, III and IV are
    byte-identical across this repair"*, read `git status` on the live working tree: a check about
    one repair's blast radius, pointed at a subject every later session moves. Re-anchored to a
    before/after digest pair taken by the run itself. `scripts/wt201_wt188_moving_subjects.py`.

**Both guard repairs are FALSE-POSITIVE REDUCTIONS under DoD § 1.1's narrow exception. Neither
makes an instrument look at anything new.** Both patch scripts run twice with byte-identical
stdout and are therefore deliberately NOT registered claims, for the reason `-104` gives: the wrap
only ever runs a command a second time, so registering an idempotent no-op registers a no-op.

---

## 5 · PASS D'S PRECONDITION, ANSWERED IN § 3.0'S WORDS, PER MANUSCRIPT

> **"Will any section move again?"**

* **paper-II — NO.** One paragraph moved (II-3, § 3.1 → § 3.3). No section moved. Its two remaining
  folds were definition-slot repairs inside § 2.4. Nothing is outstanding.
* **paper-III — NO.** No section moved. Two domain statements moved § 10 → § 2, which is a move of
  material INTO the section that owns it, not a reordering of the document. The § 4 → § 5.4
  dependency is settled by § 3's ruling above and is flagged there rather than left silent.
* **paper-IV — NO.** Two paragraphs swapped inside § 3 (IV-3). No section moved.

**The order is settled. Pass D may read at thirty thousand feet.**

---

## 6 · WHAT PASS D INHERITS FROM PASS C, STATED SO IT IS NOT DISCOVERED

1. **`REVIEW-038` § 4's C-a, C-b, C-e and C-f counts were taken before this session's edits.** Pass C
   added prose in nineteen places. **It added ZERO hard C-e** — no session number, no `REVIEW` doc,
   no `p7-passes.tsv`, no `LEDGER` id was introduced. Named artefacts introduced this pass are
   `PRE-002`, `REG-003`, `REG-013` and `src/wealth_tensor/lag.py`, all committed and fetchable, and
   all already inside § 4.1's SOFT census. **The delete-on-sight 15 is unchanged.**
2. **C-b may have grown slightly and it was not counted.** Sentences such as paper-III § 3.1's
   *"Two of the three columns need their construction stated before they can be read"* are a
   definitional gloss, but they narrate the document. **Pass D should read the nineteen edit sites
   with a C-b eye**; `git diff 1618d6a..HEAD -- docs/papers/` names all of them in one command.
3. **C-f was not touched, anywhere, at all.** No sentence was re-voiced.
4. **Three LOW-confidence items were found and deliberately NOT repaired** — they are in
   `POST-SHIP.md` under this session's block, with the reason for each.
5. **paper-II's § 2.4 is now the definition slot for four quantities and one criterion.** If Pass D
   moves anything in § 2.4, § 3.1's table stops being self-supporting.
