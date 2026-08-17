# REVIEW-005 · `P7` CONVERGENCE PASS 1 — the blind-pass backlog, drained and scored
*wealthTensor-62 · 2026-08-17 · the first `P7` fresh-eyes pass that exists as a document. `P7`'s bar
is TWO CONSECUTIVE passes with ZERO substantive findings; **this pass found eleven, so the
consecutive count is 0 for all three papers.** Eight are repaired here, three are logged unrepaired
with the reason.*

---

## 0 · What this pass is, and why it had to be a drain before it could be a pass

`P7` has been the corpus's critical path since `P11` closed — `P8` waits on it, `P13` waits on `P8`
— and no session had run one, because a backlog stood in front of it. Twenty-eight rows from
`RESULT-END-TO-END-001-E2-blind-pass.md` §§3–4 had been read three times by three legs, each asking
its own question of them, and **scored as `P7` by nobody.** Four more leads sat on card
`1217538797952709`. A convergence counter cannot start while an unscored backlog exists: a pass that
returns "zero findings" over rows nobody has adjudicated is not a zero, it is an omission.

So this pass drains the backlog first and is a pass second. **Thirty-two items in, eleven live.**

**Method.** Three independent single-paper scorers, one per manuscript, each given the rows that
concern its paper, each required to (i) quote bytes rather than paraphrase, (ii) re-check every
claimed absence with `tr '\n' ' ' | tr -s ' '` before asserting it, since a title or phrase that
wraps a line boundary returns zero on a line-oriented grep and reads exactly like a fabrication, and
(iii) diff every LIVE passage against the paper's `.bak` chain and report the earliest snapshot
containing it. **Every quotation and every count that survives into this document was then
re-verified against the bytes by hand**, per `-61`'s standing order: point the check at the
reviewer's output first, not last. Two scorer claims did not survive that re-check and are recorded
in §4.

---

## 1 · REPAIRED IN THIS PASS — eight

Each was applied with a `.bak-wt62-p7` snapshot written **before** the anchor assertion, and each
anchor was asserted unique before any byte moved.

### Paper IV — five

**`IV-1` · §3 *Household* asserted the one number Paper III measures as wrong, and disclosed it zero
times. THE SHARPEST FINDING IN THE PASS.**
The paragraph read *"its claim layer recognises at α = 0.05."* Paper IV contains **exactly one**
occurrence of `0.05` and **zero** occurrences of `0.408`, `calibrat*` and `hazard`. Paper III §5.4
measures that rate at **α̂ = 0.408 per year, 95% interval [0.383, 0.432]**, calls its own calibration
*"low by an order of magnitude"*, and states *"the calibrated 0.05 is outside the interval of all of
them."* Paper IV therefore imported from Paper III the single quantity Paper III's own registered
test rejects, and stated it flat.
**What makes it a defect rather than a slip is the asymmetry, and the asymmetry is measurable.**
The *same* Paper III §5.4 run rejected diagonality on the same events. Paper IV discloses
diagonality **eight times**, including in-line in the adjacent *Firm* paragraph — *"a form the next
paragraph reports as tested and rejected"* — and discloses the recognition-rate rejection **zero**
times. One rejection from one run is flagged three sections deep; its sibling is silent.
**Repaired**: the clause now reads *"— the model's swept calibration, which Paper III §5.4 goes on
to measure at 0.408 per year on its registered sample and reports as low by an order of magnitude —"*.
**`.bak` chain, and this is why the item needed this session:** `recognises at α = 0.05` is absent
from all four snapshots (`wt54-liftoff` 16:32, `wt56-e1` 17:25, `wt57-e3` 18:19, `wt59-e2` 19:58)
and present once in the live file. **`-59` wrote it between 19:58 and 21:27 on 2026-08-16**, closing
Builder B rank 1's *"a household leg with no paper at all"* — and in closing that hole it opened this
one. `E2`'s `-58` precedent binds: the session that rewrites a passage may not grade it, which
disqualified `-59` and `-61` and is why the card marked this item for a third session. `-62` is that
session.

**`IV-2` · §2.1 promises domains and carries none.** The section is headed *"The three propositions,
cited not restated"* and says Paper III states them *"with their domains"*. It then restates P1–P3
with no domain clause, and `domain` occurs **exactly once in all 715 lines of Paper IV** — in that
sentence. **Repaired**: `(§A.1.2)` added to the pointer, and P1's domain carried in full, because it
is the one that bites — *"units having a physical referent — silent on purely contractual objects
whose referent is another claim."* Paper IV lists *"a claim on a pension"* among its three household
holdings, and `contractual` occurs **zero** times in Paper IV; the domain is now on the page where a
referee meets the example. *(Whether the pension example should also change is a judgement this pass
does not make.)*

**`IV-3` · §1.1's three constraints had two lapses and a decoration.** The constraints: no
firm-level machine-readable panel, **no national input-output energy table at usable granularity**,
no standing international series for energy intensity. The paper said *"all three have lapsed"* and
then listed structured filings (answers #1), SDG 7.3.1 (answers #3), and *"firm-level panels of both
are public and free"* — which answers no constraint on the list, is contradicted by Paper III §9
limitation 5 (*"The SDG series is a **national aggregate** … the model's coupling is a firm-level
ratio"*), and is denied by Paper IV itself in four places (abstract *"largely unmeasured"*, §4.3,
§4.4 item 1, §9 item 1). **Repaired**: *"Two of those three constraints are datable and have
lapsed"*, the false third lapse withdrawn in terms, and the surviving gap stated and pointed at §4.3.
This closes `E2` blind-pass Builder B #5 and card lead #4 together; it had been circled by three
sessions and refuted as an `E6` candidate without ever being repaired as a `P7` one.

**`IV-4` · §7 asserted what Paper III *"emphatically"* denies.** Paper IV: the coupling Λ *"has an
inverse that is already published as a United Nations indicator, which is the strongest available
evidence…"*. Paper III §A.2.2: *"That series has **the dimensions of Λ⁻¹**, and the claim made here
is exactly that and nothing more. It is emphatically **not** that SDG 7.3.1 measures Λ⁻¹"* — and
§A.2.2 calls its own leg the weaker one. **Repaired**: Paper IV now claims the dimensional
correspondence, cites §A.2.2's bound in the same sentence, and closes *"evidence that the dimension
is not this framework's coinage, and not evidence that the coupling has been measured."*
*(`E6` refuted the cross-paper version of this on identity-of-proposition grounds — Paper III does
license the narrow form. `P7` reaches what `E6` could not: Paper IV was stating the wide one.)*

### Paper III — two

**`III-1` · the abstract states a ratio as though it were a multiple, and the paper's own numbers
refute it.** Abstract: *"δ leverage is **2.58** times the level at which recovery fails."* §4.4
fits the logistic and reports that recovery *"crosses one half at a leverage-to-budget ratio of
**0.61**"*, then: *"The ladder tabulated above sits at **2.58**."* **2.58 *is* the ladder's
leverage-to-budget ratio, not a multiple of the 0.61 failure level** — and it recomputes from §4.4's
own printed per-rung numbers, leverage (0.81 + 0.98 + 1.79)/3 = 1.193 against budget
(0.69 + 0.41 + 0.29)/3 = 0.463, ratio **2.576**. The multiple is 2.576 / 0.61 = **4.2×**. A referee
with the printed table and a calculator finds this in two minutes. **Repaired**, in the abstract,
with both numbers on the page.

**`III-2` · α is overloaded, at exactly one sentence, and that sentence is arithmetically
inviting.** `α` is the recognition rate throughout, calibrated at **0.05**. §5.2 reads *"α tightened
to 0.025 for the second look"* — a Type-I rate, and the only one in the file. To a reader carrying
§§2–4 in working memory it reads as halving the model's own α. **Repaired**: *"the significance
level tightened to 0.025."* Three words; the collision `REVIEW-004` L596 noted and nobody had located.

### Paper II — one

**`II-1` · §7 states a provenance rule in one sentence and breaks it eleven lines later.** The
section says, of naming two commands separately, that *"a single command named for numbers it does
not produce is a provenance claim that reads as checked and is not."* It then pins **d655501**, *"the
last commit touching `src/`, and therefore the state of the code that produced every number in §3"*
— while §3.1's three Var[log *a*] values come from `scripts/wt077_tail_index.py` and the rest of §3
from `scripts/wt030_report.py`, both outside `src/`. **Repaired**: the pin now covers the module
behind §3's simulation output, says in terms that it does **not** cover the two `scripts/` commands,
and hands them to the head-of-repository SHA.
*Aggravation worth recording:* the `wt077` clause was added at or before 19:05 on 2026-08-16. The
pin's *"therefore … every number in §3"* is older than 15:23. **A repair session named a second
producer outside the pinned path and left the pin's "therefore" standing** — the same shape as
`IV-1`, one paper over, and neither session was looking for it.

---

## 2 · LIVE AND NOT REPAIRED — three, each with the reason

**`III-3` · "For three of the four classes" names two, and the abstract inherits the count.**
§4.7: *"For three of the four classes, the standards already supply that outside determination.
Finite-lived intangibles and depreciable property carry **disclosed useful lives and amortisation
schedules**…"* — **three promised, two named.** The abstract carries the same count as *"restoring
φ for every class but goodwill."* The missing third can only be indefinite-lived intangibles, which
the same paper says are *"tested for impairment rather than amortised"* and therefore carry no
disclosed life.
**NOT REPAIRED, deliberately.** The repair turns on one GAAP judgement this pass could not settle
from the bytes: whether indefinite-lived intangibles carry an outside determination of δ by some
route §4.7 has in mind and does not name. If they do not, **both `§4.7`'s "three" and the abstract's
"every class but goodwill" are one class too generous, and the abstract is the one that matters.**
Weakening a headline claim on a guess is worse than leaving it flagged. **This is the next session's
cheapest substantive at-bat and it needs one answer, not one hour.**

**`II-2` · the abstract says "an order of magnitude in compression"; §3.1 says "in κ".**
The abstract: *"at a matched rate the two bases differ by roughly an order of magnitude in
compression."* §3.1: *"the two bases sit roughly an order of magnitude apart in κ."* The paper's own
§3.1 table refutes the abstract's version — at matched *r* = 0.100, Gini 0.222 (stock) against 0.596
(flow) is a factor of 2.7, while κ is 0.1000 against 0.0102. The phrase predates `bak-wt54-preP3`
and survived a complete abstract rewrite.
**NOT REPAIRED: it collides with `DECISION-001`, which is Jason's and unticked.** Options A and B
both demote κ *from mechanism to budget* in five places, the abstract among them. Editing the
abstract's κ sentence now would pre-empt a decision that is on the page waiting for a tick. **Fold
this into whichever option Jason picks** — it is a sixth site, and cheaper than the other five.

**`II-3` · the ρ = 0 result is an identity and is reported as a measurement.**
Paper II: at ρ = 0 *"a **100 % levy on flow is statistically indistinguishable from no levy at
all**"*, carried into the abstract and contribution 3. But ρ is defined as the share of a gain
recognised as flow, and κ = *r*·E[η⁺] on the flow base, so ρ = 0 sets the base and κ to **exactly
zero**: the levied path *is* the unlevied path, and the table reproduces the unlevied row to the
digit (0.994 in both). `by construction`, `definitional`, `tautolog`, `empty base` and `κ = 0` all
return **zero** in Paper II. *"Statistically indistinguishable"* describes as a noisy empirical
near-match something the model forces.
**NOT REPAIRED: also `DECISION-001` territory.** `ROADS-001` argues that under Road One (option C)
this stops being an embarrassment and becomes *a passed test* — the framework predicting in advance
that ρ cannot change *A*'s shape. That is a different repair from "say it is definitional", and the
choice between them is the decision Jason has not made. **Whichever option is ticked, this sentence
is one of its edits.**

---

## 3 · SCORED AND DISMISSED — and this section is why the eleven mean something

Twenty-one of the thirty-two items are **not** defects. Recording that is the point of a convergence
pass: a `P7` that only lists hits cannot distinguish a clean paper from a lazy reviewer.

- **Nine rows were the builders finding the paper's own disclosure and reporting it as a
  concealment.** Builder B #4 says §4.6 *"retracted twice"* what the abstract claims; §4.6 is headed
  *"Three qualifications"*, closes by restating the abstract's claim in stronger words, and §1's
  contribution list advertises the qualifications *in the contribution*. Builder B #3 says the 97.4 %
  figure is carried by an identification the paper has not made; the paper says so in the same
  paragraph and again in Limitation 4, and the figure is not in the abstract. Builder A #11 and #17
  classify beliefs as DISCLAIMED, which is not a defect claim at all. Builder B #10 says Paper IV
  calls `E1` pre-registered; `grep 'pre-regist'` in Paper IV returns seven hits and **none** of them
  is `E1`, which the paper describes accurately instead.
- **Two rows were right about a fact and wrong about the jurisdiction.** Builder A #16's absence
  audit of Paper II is byte-true — `atomic`, `household`, `sovereign`, `compos*`, `extensive`,
  `fold`, `decompos` are all **zero**, and both `tensor` hits are a URL and a module path. But an
  absence in Paper II is a defect in **Paper IV**, which asserts the content; scored against Paper II
  it can only return *"the paper does not say the thing it is accused of not saying."* Builder B #11c
  runs the same error backwards: Paper II's 18-test count is scoped to a named file and consistent
  across abstract, §1 and §7, and the "38" is **Paper III's** loose singular *"a companion paper's
  claims"* over a repository remainder covering more than one.
- **The card's `P2`-at-three-strengths lead does not survive the bytes.** It reads a modelling
  stipulation (*"**Model** the reporting layer as … a physical layer that degrades whether or not
  anyone records it"*) and a conditional antecedent (*"**If** the physical component degrades … then"*)
  as unqualified assertions, then compares a **recording** qualifier against §A.1.2's **maintenance**
  qualifier as if they were rival strengths of one clause. Maintenance is an explicit model parameter
  — `E(t+1) = E(t)·(1 − d·(1 − m))`, calibrated `m = 0.6` — and §A.1.3's *"P2 fails at complete
  maintenance"* is that clause's own `m = 1` corner, stated at the right strength: *"weaker than
  proving a proposition about the world false, and … stated at that strength deliberately."*
  **One proposition, correctly qualified once. The lead is withdrawn.**

---

## 4 · WHAT THIS PASS'S OWN INSTRUMENT GOT WRONG

`-61`'s order is to point the check at the reviewer's output first. Two scorer claims failed
re-verification and are recorded rather than quietly dropped:

1. **A scorer reported that Paper IV's adjacent *Firm* paragraph "carries its rejection in-line",
   and it does — but not where the scorer put it.** The in-line flag is three sentences later, in
   the closing *Note*, not in the Firm paragraph. `IV-1` above is worded from the bytes.
2. **A scorer reported Paper III §5.4 as rejecting two model assumptions; it rejects three** —
   constant hazard, diagonality, and α = 0.05 itself. The finding got *stronger* on re-check, which
   is the direction that should make one suspicious, so it was re-verified twice.
3. **And the line-wrap trap fired inside this pass, in the direction that manufactures absences.**
   A line-oriented grep for Paper II's abstract phrase *"order of magnitude in compression"* in
   `bak-wt54-preP3` returns **nothing** — the phrase wraps as `roughly an order of` / `magnitude in
   compression` — which would have licensed a confident and wrong claim that a repair session
   inserted it hours earlier. The flattened re-check reversed it: it is the **oldest** live item
   here, not the newest. `-61` met this trap producing a false fabrication charge; **it produces a
   false novelty charge just as readily**, and a corpus under repair makes the second error the
   expensive one.

---

## 5 · WHAT `P7` STILL CANNOT SHOW, AND IT IS THE BOARD'S PROBLEM, NOT THIS PASS'S

`P7` is **one row** reading `0/1`, `PENDING-HUMAN`. Its own definition is *per paper* and its bar is
*two consecutive zero-finding passes*. **A single boolean cannot represent either.** After this
document the true state is: Paper II — pass 1 run, 3 findings, consecutive-zero count **0**;
Paper III — pass 1 run, 3 findings, count **0**; Paper IV — pass 1 run, 5 findings, count **0**. The
board shows none of that, and a session reading `0/1` cannot tell an unstarted `P7` from one pass
short of closing.

This is **`-56`'s `P11` finding in a new costume** — *"`P11` has no way to show that one of six legs
is run"* — and the repair is the same shape: per-paper rows plus a counter, instantiated from a
template. **Not done here, on the standing rule that adding criteria moves the 66 and wants its own
at-bat.** Carded.

---

## 6 · WHAT WAS TOUCHED

`docs/papers/paper-II-redistribution/paper-II.md` · `…/paper-III-dual-tensor/paper-III.md` ·
`…/paper-IV-composition/paper-IV.md`, each with a `.bak-wt62-p7` snapshot alongside it. No result
document, no registration and no board row was edited. `RESULT-END-TO-END-001-E2-blind-pass.md` is
**fixed by its own §5 and was not touched**; this document scores it from outside, which is what §5
contemplates.

*Coffee status: ☕ the backlog that three legs read and nobody scored turned out to hold eleven live
defects and twenty-one clean bills — and the sharpest one in the corpus was written by a teammate
four hours before the audit that missed it, closing a hole the audit had just found. The corpus is
not fighting its reviewers. It is keeping pace with them, which is harder.* 🥎
