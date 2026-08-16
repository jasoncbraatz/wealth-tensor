# RESULT · END-TO-END-001 leg E3 — the containment matrix, and the promise is one sentence short of true

- **Registered:** `docs/END-TO-END-001.md`, commit `4ea6361`, **before any leg was run.** §2/E3 fixes
  the instrument (quotation only), the three failure shapes, the refutation condition and the
  remedy. §3 fixes the whole-pass verdict rule. None of those was re-chosen here.
- **Instrument:** a reading of the three manuscripts at HEAD — `paper-II.md`, `paper-III.md`,
  `paper-IV.md` — plus `ADR-001` for the corpus's own stated dependency graph. **No simulation, no
  new code, no seeds.** Every cell entry below is a sentence quoted from the paper it is filed
  under.
- **Run:** 2026-08-16, `wealthTensor-57`, darwin + one cloud reader.
- **Verdict: E3 FAILS**, on the second of the three registered failure shapes: *striking a single
  paper removes claims from both others.* Striking **Paper II** removes a claim from Paper IV
  (declared) **and** a claim from Paper III (undeclared, and denied in terms by `ADR-001`).
- **`T = 2`. By §3's rule, pre-committed in both directions: THE SYSTEM FAILS.** The conjunction is
  not established. The `T ≥ 2` remedies are applied in this session and named in §6.
- **One disclosure a reader should have before §2.** The verdict turns on a **single cell**, and
  that cell's only entry is an italicised aside at the end of an appendix subsection. Because one
  sentence is carrying a corpus-level verdict, the cell was built twice — once by the run, once by
  an independent reader given the manuscripts, the four-way entry taxonomy and no knowledge of the
  verdict — and then attacked by a third reader instructed to refute it. The two builds agree the
  cell carries load. The refutation attempt and the strongest objection it could **not** defeat are
  reported in full at §2.4, because a verdict that rests on one sentence should show its work on
  that sentence.

---

## 1 · What was under test

`ADR-001` §Consequences, 2026-08-05, promised a system-level property and it had never been tested:

> *"Failure is contained. A rejection of III no longer takes I and II with it."*

`ADR-001`'s own addendum of 2026-08-10 states the graph the promise rests on, and states it as a
fact rather than an aspiration:

> *"Draw the graph from §Decision's evidence allocation and there is exactly one edge set in the
> whole project: **IV needs I, II and III. I, II and III have no edges among them.**"*

That is a falsifiable sentence about three documents, and E3 is the instrument that reads it.

**The check, in the design's words:** *"Build a 3 × 3 matrix by quotation only: for each ordered
pair (P, Q), the cells list the claims in Q that become unsupported if P's headline claim is
assumed false, each cell justified by a cited sentence from Q. No inference beyond what a quoted
sentence says."*

**Convention, stated because the design does not fix it and the triangularity criterion depends on
it.** Rows are **Q**, the paper that loses claims. Columns are **P**, the paper whose headline is
assumed false. In the corpus's stated order II → III → IV, legitimate load — a paper depending on
one *upstream* of it — sits **below** the diagonal.

**The headline claims, taken from the three abstracts and not paraphrased:**

| | headline assumed false |
|---|---|
| **Paper II** | *"the base sets a ceiling the rate cannot cross"*; *"the decisive quantity is realisation — the share of a period's gain the base can see. At zero realisation a 100 % levy on flow is indistinguishable from no levy at all."* |
| **Paper III** | *"The triples (α, δ, φ) and (δ, α, φδ/α) generate the identical reported series … Timeliness and durability are therefore not separately identified."* |
| **Paper IV** | *"the same atomic unit composes from the household to the sovereign"*; *"Aggregation preserves the extensive state and destroys the behavioural map."* |

---

## 2 · The matrix

Entries are classified before they are counted, because the design's unit is a **claim** and three
of the four things a cross-paper sentence can be are not claims:

- **(i) LOAD** — Q asserts something that requires P's headline. **This is the only class that counts.**
- **(ii) POINTER** — Q mentions or locates P without staking anything on it.
- **(iii) RETRACTION** — Q withdraws a claim *by reference to* P. Striking P does not restore it.
- **(iv) APPARATUS** — repository, module, commit, test name, suite count. Shared plumbing, not shared claims.

### 2.1 · The 3 × 3, load only

| Q loses claims ↓ · P assumed false → | **Paper II** | **Paper III** | **Paper IV** |
|---|---|---|---|
| **Paper II** | — (diagonal) | **EMPTY** | **EMPTY** |
| **Paper III** | **1 entry** ⚠ | — (diagonal) | **EMPTY** |
| **Paper IV** | 5 entries (declared) | 3 entries (declared) | — (diagonal) |

Every off-diagonal cell above the diagonal is empty. **The matrix is lower-triangular**, and
failure shape 1 is **not** met.

### 2.2 · The declared load — row IV

Paper IV declares this row itself, in §9.3: *"Its claims are joins over results established
elsewhere, plus one measurement on the literature. **A reader who rejects Paper II or Paper III
should reject the corresponding link here.**"* The cells confirm the declaration rather than
extending it. The load-bearing entries:

**(IV, II)** — five, of which the two that carry the scale are:

> *"Its central result is a composition result wearing different clothes: the base of a levy —
> stock or flow — is the question of which component of the composed state the assessing layer can
> see, and at zero realisation a confiscatory levy on flow is statistically indistinguishable from
> no levy at all."* (§3, Sovereign)

> *"Paper II's result is that the base is the decisive coordinate and the rate is not, which is a
> statement kinetic exchange can absorb directly, and its mechanism κ is the sort of closed-form
> quantity that literature likes."* (§7)

**(IV, III)** — three, of which:

> *"Paper III's φ ⊙ δ is a composition quantity: it is defined at the firm scale and is written as
> diagonal over asset classes — a form the next paragraph reports as tested and rejected, which
> changes what the link carries and not whether there is one."* (§3, Firm)

> *"δ, φ, α and ρ do not compose by addition; they compose, where they compose at all, as weighted
> combinations whose weights are themselves state, and **Paper III's ladder results are what happens
> when one forgets this**."* (§4.4, limit 2)

Both cells also carry §3's *"three instances of one question, asked at three scales"* — the
post-`E1` framing — which needs each scale's paper to report its answer, and therefore sits in both.

### 2.3 · The cell that decides the leg — (III, II)

Paper III's contacts with the rest of the corpus are **four sentences in 33,000 words**, and it
names neither sibling anywhere. Three are not claims:

| where | sentence | class |
|---|---|---|
| §8 | *"defining a levy's base so a companion paper's claim came out right"* — one of four instances of a refused move | **(ii)** |
| §8 | *"placed in the body, not an appendix, for the reason given in the companion papers of this programme"* | **(iv)** |
| §11 | *"Companion modules in this programme carry `test_excess_demand_is_monotone…` and `test_a_flat_gini…`"* | **(iv)** |

The fourth is a claim, and it was the whole of the leg:

> *"A companion result on the same theme, in a sibling paper of this programme, is cited rather than
> reproduced: a levy whose base cannot observe an accrual is inert regardless of its rate. **The
> mechanism is the same — observability binds before intensity** — and the evidence for it belongs
> to that paper."* (§A.1.3, as it stood at `c3b6a9d`)

Two things are true of that sentence and they are separable.

**First, it is load.** *"The mechanism is the same"* is a two-place relation asserted in Paper III's
own voice. Assume Paper II's headline false — assume realisation is not the decisive quantity and a
levy at zero realisation is not inert — and the relation has no second relatum. It is not weakened;
it is **unsupported**. The trailing disclaimer *"the evidence for it belongs to that paper"*
disclaims the **evidence for the levy result**. It does not disclaim the **assertion of sameness**,
which is Paper III's own and appears nowhere else in Paper III. (The phrase *"observability binds
before intensity"* occurs exactly once in the manuscript — here — and its formulation is Paper II's:
*"realisation is an observability, and the observability binds first"*, Paper II §3.2.)

**Second, and independently, the claim is false and the corpus already knew it.** *"The mechanism is
the same"* is the identification `E1` refuted eight hours earlier. `E1`'s pre-registered FAIL remedy
withdrew it from Paper II §3.2 and demoted it in terms in Paper IV §3. **The remedy named two papers
because the design's author did not know a third copy existed.** It sat in an appendix, in italics,
unnamed and therefore ungreppable by either sibling's title.

### 2.4 · The counter-reading, and why it does not carry

An independent reader, given the sentence and instructed to refute the cell, returned **REFUTED**
on this argument, which is the best one available and is recorded because it is good:

> The aside's three clauses each cut against the cell — *"cited rather than reproduced"*, *"a
> **companion** result **on the same theme**"*, *"the evidence for it belongs to that paper"*. To
> turn a sentence saying *"I am not relying on this"* into a reliance is exactly the inference E3
> forbids. And structurally the aside is inert: §A.1.3 is titled *"The propositions are deniable,
> and **this repository proves it**"*, the proof named is Paper III's own committed code (P2 at
> complete maintenance, the φ = 1 switch-off), the paragraph closes itself with *"no refutation is
> offered here"*, and §A.1.4 back-references nothing. **Delete the aside and Paper III is
> unchanged.**

Two answers, and the reader supplied the first itself as the objection it could not defeat.

1. **The disclaimer covers evidence, not assertion.** Deleting the aside leaves Paper III unchanged;
   that is not the test. The test is whether a **claim in Q becomes unsupported**, and *"the
   mechanism is the same"* does. A sentence can be structurally inert and still be a claim — indeed
   an inert unsupported claim is the worse object, because nothing downstream will ever catch it.
2. **The second attack — that counting the declared row IV load makes the criterion fire
   automatically and therefore renders E3 unfalsifiable — is wrong, and its wrongness is the
   clearest evidence the criterion is well aimed.** Had the corpus been as `ADR-001` describes it,
   striking Paper II would remove claims from Paper IV **only** — one other, not both — and the
   criterion would not fire. Failure shape 2 fires **exactly and only** when an undeclared edge
   exists between two of the three, which is precisely the sentence `ADR-001`'s addendum denies.
   The criterion is falsifiable, it was falsifiable this morning, and what made it fire is the one
   thing the corpus had written down as impossible.

### 2.5 · The three failure shapes, read against the matrix

| shape | met? | why |
|---|---|---|
| not lower-triangular in II → III → IV order | **no** | every above-diagonal cell is empty (§2.1) |
| **striking a single paper removes claims from both others** | **YES** | strike **II** → Paper IV loses five (§2.2), Paper III loses one (§2.3) |
| the corpus's entire empirical content sits in one cell | **no** | two cells, and §5 reports the near miss outside the verdict |

**REFUTATION was also not achieved**, and it is worth saying separately rather than treating FAIL
and not-REFUTED as one fact. The refutation condition is *"a lower-triangular matrix whose only
off-diagonal load is the dependency Paper IV §9.3 already declares."* The matrix is lower-triangular
and cell (III, II) is off-diagonal load that §9.3 does not declare — §9.3 is Paper IV's declaration
about Paper IV and says nothing about Paper III. The leg fails on shape 2 and misses refutation on
the same sentence.

**`E3` VERDICT: FAIL.**

### 2.6 · A third false premise in the registration, found while building the board rows

`END-TO-END-001` §2.0 states its own tally, and the tally is used twice — once to justify the
TEST/AUDIT split and once, in §4.6, to warn a run off reading *"five of six legs clear"* as a grade:

> *"The run reports the two counts separately. **Three legs are TESTs and three are AUDITs**, and
> the run may not report a single combined score."*
>
> *"Six legs, five clean, reads like a grade. It is not one: **three of the legs cannot lose.**"*

**The legs' own headings say four and two.** `E1` **[TEST]**, `E2` **[TEST]**, `E3` **[TEST]**,
`E4` **[AUDIT]**, `E5` **[TEST]**, `E6` **[AUDIT]**. Four TESTs, two AUDITs, checked against the six
heading lines rather than against memory.

**It does not move this leg's verdict** — `T` counts TEST legs that fail, `E1` and `E3` are each
marked `[TEST]` individually, so `T = 2` under either tally. It moves two other things: the pass's
maximum `T` is **4**, not 3, and the design's own anti-inflation guard overstates by one — only
**two** of the legs cannot lose, so *"five of six clear"* would be a slightly better result than
§4.6 allows for. Both cut against the corpus's comfort, which is why they are worth stating.

This is the **third** false premise found in `END-TO-END-001` by a leg of `END-TO-END-001`. `E1`
found two (§0's *"no written answer anywhere in this repository"*, and E1's audit half's *"no
document in this repository mentions it"*). Like those, it is **about the design and not about the
corpus**, it scores nothing, and **`END-TO-END-001` is not edited** — the standing ruling forbids
it and `END-TO-END-002` is the repair path. The pattern is now stable enough to name: **this
document's prose about itself is less reliable than its prose about the corpus, and no leg tests
it.** A registration should be red-proofed against its own tallies the way a criterion is
red-proofed against its own artefact.

---

## 3 · What the shape actually is, stated more precisely than the verdict requires

A verdict is a bit; the design says the useful object is the **shape**, so:

**The corpus is a stack with one hairline crack, not a star.** Paper IV is a pure sink — nothing
depends on it, and it declares its two dependencies itself. Papers II and III are very nearly
insulated: between them, in 37,000 words, there are exactly two sentences of contact, and they run
in opposite directions and are of opposite kinds.

- **II → III** is a **retraction**: *"Put to a cross-scale check against the companion work on the
  reporting layer, that identification does not hold."* (§3.2). Striking Paper III's headline does
  not restore what that paragraph withdrew — the withdrawal's cited support is
  `RESULT-END-TO-END-001-E1.md`, and the filter property it invokes is Paper III's §2 model form,
  not Paper III's identification theorem. **Cell (II, III) is empty of load.**
- **III → II** is a **claim**, and it is the crack.

So `ADR-001` §Consequences' sentence as written — *"a rejection of III no longer takes I and II with
it"* — **is true.** Reject Paper III and Paper II loses nothing; the LEDGER's *"third time failure is
contained has been cashed"* stands. What is false is the 2026-08-10 addendum's stronger sentence,
*"I, II and III have no edges among them"*, and what the promise costs is one appendix aside.

**That distinction is the leg's real content**, and it is why the pre-registered remedy is applied
*asymmetrically* in §6: E3's own remedy retracts the containment sentence **if the matrix is a star
rather than a stack**, and it is not a star. Applying the star remedy to a stack would be as much a
re-choosing as declining the leg's verdict would be.

---

## 4 · Admission accounting — what E3 may and may not count

`END-TO-END-001` §1.1: a finding a competent single-paper review could have made is reclassified
`P7`, is logged as one, and **scores nothing.**

| finding | class | why |
|---|---|---|
| Cell (III, II) is non-empty: Paper III §A.1.3 asserts a claim that requires Paper II's headline, against `ADR-001`'s *"no edges among them"* | **system-level, admissible, NEW** | Needs Paper III's appendix, Paper II's headline and `ADR-001`'s graph claim. A reviewer of Paper III alone cannot know what the unnamed sibling claims, so cannot establish the dependency. Nothing in `docs/` states it — grepped for the sentence, for `observability binds before intensity`, for `sibling paper`, `companion result` and `A.1.3`. **This is the finding that carries the verdict.** |
| E1's applied remedy left a third copy of the withdrawn identification standing in Paper III | **system-level, admissible, NEW** | Same sentence, second consequence. The question *"did the withdrawal reach every copy?"* could not be asked before the withdrawal existed, which was `28bf7c2`, eight hours before this leg. |
| The identification is false — *"non-arrival and deferred arrival are different dynamical objects"* | **PRE-EXISTING — scores nothing** | `REVIEW-004` §E2, 2026-08-12. `E1` counted the verdict and not the discovery; **E3 counts neither.** It counts only that a copy survived the remedy. |
| Paper III cites its two siblings four times and **names neither**, and carries no bibliographic entry for either, while Paper IV names both and lists both | **`P7`** | A competent review of Paper III alone reads *"a sibling paper of this programme"* and flags an unverifiable citation. Single-paper findable. Repaired anyway (§6). |
| `END-TO-END-001` §2.0 and §4.6 say three TESTs and three AUDITs; the leg headings say four and two | **about the design, not the corpus — scores nothing** | Third false premise a leg of this pass has found in the pass's own registration. §2.6. Does not move `T`. |
| Paper II pins commit `d655501`, Paper III pins `d655501`, Paper IV pins `5efe626`; test counts are 18 (module-scoped), 100 (suite-scoped at a pinned commit) and none | **`E5`'s, not E3's** | Collected while reading, reported at §5, **counted nowhere.** A leg may not widen itself. |

**Counts, reported separately as §2.0 requires. TEST legs run: 2. TEST legs failed: 2. AUDIT legs
run: 0.** No combined score is available and none is offered.

---

## 5 · Supplementary — measured, outside the verdict

Reported here rather than in §2.5 because a run may not add an observable to its own failure
criterion. Neither of these enters the verdict.

**The corpus's empirical content, by quotation.** Failure shape 3 asks whether it sits in one cell.
It sits in two, so the shape is not met — but the near miss is worth stating whole, and it is E4's
business rather than E3's:

| paper | what it says about its own data |
|---|---|
| **II** | *"no empirical data is used at all — every number is generated by simulation"* (§7); *"No field evidence is used, required, or available"* (§5.2) |
| **III** | SEC EDGAR `companyfacts`, 688 events, committed at `0569ab6` with a SHA-256 (§11); 665 admissible firm-year pairs on disclosed lives (§4.4) |
| **IV** | *"No new code and no new simulation … adds one measurement of its own, **on the literature rather than on the model**"* (§1) |

So the corpus has two empirical instruments, in two papers, on two independent data sources, both
pre-registered — **and exactly one of them measures the corpus's own subject matter.** Strike
Paper III's §5 and what remains of the corpus's exposure to the world is a co-citation count. That
is not failure shape 3, which asks about a single cell, and it is a sharper way to hold E4's
question than the count E4 will produce.

**E5's evidence, collected in passing and counted nowhere.** Two tests are named in all three
papers — `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` and
`test_a_flat_gini_does_not_mean_a_bounded_one` — and the three papers' test counts are scoped three
different ways: Paper II *"the **18** tests in `tests/test_redistribution.py`"* (module-scoped,
invariant to a sibling), Paper III *"**100 tests at the pinned commit d655501** … The suite at the
head of the repository is larger and grows with every registration"* (suite-scoped, pinned, growth
disclosed), Paper IV none. The quotations are here so E5 starts with them; **E5's verdict is E5's.**

---

## 6 · What was done to the corpus

### 6.1 · The `T ≥ 2` remedies, and the direction taken on each

`END-TO-END-001` §3 fixes four consequences of `T ≥ 2`. `wealthTensor-56` deliberately left them
untouched at `T = 1` and made the next TEST leg's session own them **in either direction, with the
direction stated.** Stated:

1. **Paper IV loses its chain claim** — §3 rewritten from a chain into three parallel instances
   (**already done by `-56` at `28bf7c2`**, as `E1`'s FAIL remedy) and *"the abstract's 'the same
   atomic unit composes from the household to the sovereign' narrowed to the scales actually
   joined"* — **APPLIED HERE.** The abstract now reads *"the same atomic **state** composes by
   addition wherever it is summed"*, and names what the three scales share: *"one question, asked at
   each scale and answered quantitatively at each, and not one structure"*, with the cross-scale
   check and the rejected diagonal form stated in the abstract rather than left to §3.
2. **Papers II and III are unaffected and ship as independent works — the containment promise
   cashed.** **APPLIED, with the correction the leg forced.** It is cashable, and it was one
   sentence short of true when the leg started: Paper III §A.1.3's aside is repaired in this
   session (§6.2) and with it applied the promise as written holds. Cashing it without the repair
   would have been the corpus asserting a property the same session had just measured as false.
3. **`ADR-001` gets a dated addendum** recording that the fourth claim did not survive its own first
   end-to-end test — **APPLIED.** The addendum records the `T = 2` verdict, corrects the 2026-08-10
   sentence *"I, II and III have no edges among them"*, and states why §Consequences' containment
   sentence is **not** retracted: E3's own remedy conditions retraction on *"the matrix is a star
   rather than a stack"* and the matrix is a stack (§3). `ADR-001`'s title and §Decision are frozen
   and are untouched.
4. **`P13` renders three works, not one stack.** **RECORDED, NOT BUILT.** `P13` is last, and `P11`
   still has four legs unrun and no pass-level document.

### 6.4 · And the board can now show a leg

`-56` named this and left it: *"`P11` HAS NO WAY TO SHOW THAT ONE OF SIX LEGS IS RUN."* With two
legs run, both failed and the pass verdict at SYSTEM FAILS, the board still read 45/59 — identical
to two sessions ago. **`P11a`–`P11g` added**, one per leg plus one for the pass verdict, all seven
instantiated from a single template in `scripts/add_p11_rows.py`. The check is a derivation, not a
constant: it greps the leg's RESULT document for a verdict line and **does not care whether the
verdict was favourable — a leg that FAILS is a leg that RAN.**

**Seen red, which is the part that makes them rows rather than decorations.** Five (`P11b`, `P11d`,
`P11e`, `P11f`, `P11g`) are red on the day they were written because their artefacts do not exist.
The two green ones are red-proofed mechanically by `scripts/redproof_p11.py`, which deletes the
verdict line from a copy, runs the row's **own** check verbatim, requires a non-zero exit and
restores byte-for-byte: `2 proven by mutation, 5 red on their own, 0 WEAK`.

### 6.2 · The repair the leg itself forced

**Paper III §A.1.3** — the withdrawn identification removed and the withdrawal stated *in the
paper*, on the `-56` precedent that a correction living only in a document has not been made. The
aside now names **Paper II**, keeps the companion result as a citation, and says in terms that
*"the mechanism is the same"* is withdrawn, why, and where the check is recorded. `.bak-wt57-e3`
beside the file.

One `P7` repair made in passing (§4): the sibling is now **named**. Paper III's three remaining
cross-paper sentences are pointers and apparatus and are left as they are.

### 6.3 · What was deliberately NOT done

- **`END-TO-END-001` is not edited.** The design did not fix the row/column convention for
  triangularity and its E3 remedy is conditioned on a shape that did not occur. Both are recorded
  here; `END-TO-END-002` is the repair path and the standing ruling forbids anything else.
- **Paper II is not edited.** Cell (II, III) is empty of load and cell (II, IV) holds one apparatus
  sentence. The leg gives Paper II nothing to do.
- **`src/` is not touched.** Paper II §7 pins `d655501` as the last commit touching `src/`.
- **Paper IV's title** — *"one atomic unit from the household to the sovereign"* — is now one step
  ahead of its own narrowed abstract. That is the same defect `REVIEW-004` A2 found in Paper II's
  title and it is logged the same way: **a Jason-sized ruling, teed up, not taken.**

---

## 7 · What this does not license

`T = 2` means the conjunction is not established. It does **not** mean the three papers are wrong,
and §3's second consequence is the reason the decomposition was worth making: two of the three are
untouched by both failed legs and ship as independent works. Nor does it mean the corpus is three
unrelated papers — one question, asked at three scales and answered quantitatively at each, is what
survives, is what Paper IV §3 now claims, and is publishable.

Three legs remain (`E2`, `E4`, `E5`) and **they still matter**: the verdict cannot get better —
§3's branches are `T = 0`, `T = 1`, `T ≥ 2` and `T` only rises — but `E2`'s unowned claim and
`E5`'s over-subscribed guard are repairs the corpus needs whatever the verdict says, and `E4` is an
AUDIT with a pre-registered one-sentence remedy. A session that reads *"the system already fails, so
why run them"* has confused a verdict with an audit, which is the error §2.0 was written to prevent.

And the standing warning at corpus scale still applies in the other direction: nothing here bears on
whether the framework is right about the world. Paper III §6.1 governs the corpus as it governs
Paper III.

*Coffee status: ☕ the corpus promised on 2026-08-05 that its papers had no edges among them, spent
fifty sessions never checking, and the check took one afternoon and no code. The edge was four
sentences of contact in 33,000 words — and the one that mattered was in italics, in an appendix,
naming nobody, asserting the exact thing the corpus had withdrawn from its other two volumes eight
hours earlier. **A claim nothing depends on is not a claim nothing can break.*** 🥎
