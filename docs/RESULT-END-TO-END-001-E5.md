# RESULT · END-TO-END-001 leg E5 — the over-subscribed guard, and the instrument cannot decide it

*`wealthTensor-58` · 2026-08-16 · run against `docs/END-TO-END-001.md` §2/E5 as registered
(`wealthTensor-55`, 2026-08-16), which is FIXED and was not edited in response to this result.*

- **Verdict: E5 does NOT fail — and it is NOT refuted either. The leg returns UNDECIDED, and the
  reason is the registration rather than the corpus.** Its two limbs land in the gap between its own
  failure clause and its own refutation clause, which are not complements. **`T` remains 2. THE
  SYSTEM FAILS still stands, on `E1` and `E3`, unchanged by this leg in either direction.**

**Counts after this leg.** TEST legs run **3** (`E1`, `E3`, `E5`) · TEST legs FAILED **2** · TEST
legs UNDECIDED **1** · AUDIT legs run **0**. **No combined score exists and none is offered**
(`END-TO-END-001` §2.0).

**The one-line version.** *The corpus's shared apparatus is not over-subscribed — the multiplicity
is bibliographic, not load-bearing — and the run that set out to prove it was, built a finding, had
it destroyed by its own refuter, and reports the destruction. What did not survive the afternoon is
the instrument: E5's failure clause asks whether a count MOVES, its refutation clause asks whether
every count is MODULE-SCOPED, and Paper III's count is suite-scoped and pinned, so it neither moves
nor refutes. That is the **fifth** false-or-self-defeating premise found in `END-TO-END-001` by legs
of `END-TO-END-001`, and the fifth in a row that is about the registration and not about the papers.*

---

## 1 · What was under test, and the two limbs

E5 asks *does one test hold two claims that could come apart?* It is a **TEST** — the designer
classified it as one and could not predict it — and it carries two independent limbs:

| limb | FAILURE is shown by | FAILURE is refuted by |
|---|---|---|
| **the guard limb** | *"a guard cited as holding two claims that can come apart"* | *"every cross-cited guard holding exactly one claim, **or** holding a stated conjunction that the paper names as a conjunction"* |
| **the count limb** | *"a count in any paper that moves when another paper's work adds tests to the shared suite"* | *"every count module-scoped rather than suite-scoped"* |

The refutation clause is a **conjunction of the two**; the failure clause is a **disjunction**. That
asymmetry is where the leg dies — §3.

**No code was run against `src/`. No seeds. The whole leg is quotation, one `git ls-tree` count, and
one adversarial pass.**

---

## 2 · The guard limb

### 2.1 · What the two cross-cited guards actually assert

Read from the `assert` statements, not the docstrings.

**`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`** — `tests/test_excess_demand.py:102`.
Asserts **exactly one** proposition: for one `Market` built from the module fixture with
`rng=default_rng(3)`, `excess_demand` evaluated at 500 equally-spaced prices is weakly
non-increasing. One `assert`, one seed, one grid. It does not assert the endpoints (+249 → −150),
the sign-change count, the absence of income effects, or anything about the string "SMD" beyond its
own name. **It performs no file I/O.**

**`test_a_flat_gini_does_not_mean_a_bounded_one`** — `tests/test_redistribution.py:61`. Asserts
**three** propositions about the *unopposed* economy: last-quarter-minus-previous-quarter Gini drift
`< 0.02`; `top_share > 0.95`; `not is_bounded(res)`. **It performs no file I/O.** The number `0.90`
— which §3.4 publishes as half its criterion — appears nowhere in the module.

### 2.2 · The map, built twice

Because the leg's verdict would rest on prose about tests, the map was built **twice** — once by the
run, once by an independent reader given the four manuscripts, both test sources, and a four-way
claim taxonomy (**CODE** / **PROSE** / **CHARACTER** / **POINTER**), with no knowledge of the run's
direction. **The two builds agree on every row.** Consolidated:

| guard | paper · § | the sentence's claim | type |
|---|---|---|---|
| **monotone/SMD** | II · §7 | *"which constrains the companion paper in the same suite"* | PROSE |
| | II · §7 | *"A test suite that constrains its author is a different object from one that flatters him"* | CHARACTER |
| | III · §11 | *"exist solely to make overclaiming fail loudly"* | PROSE |
| | III · §11 | *"Two tests are worth naming because of what they forbid rather than what they check"* | PROSE (governing) |
| | IV · §5 | *"The test suite asserts the monotonicity deliberately … as a standing limit on the claim"* | CODE + PROSE |
| | IV · §10 | *"which forbids §5's instance being sold as an SMD result"* | PROSE |
| **flat-Gini** | II · §4 | *"pinned by a test named … so that any future simplification of the criterion fails loudly **instead of quietly re-scoring condensation as success**"* | CODE |
| | II · §7 | *"which pins §3.4's boundedness criterion so that any future simplification of it fails **instead of quietly re-scoring condensation as success**"* | CODE |
| | III · §11 | *"exist solely to make overclaiming fail loudly"* | PROSE |
| | IV · §10 | *"which forbids a saturating statistic being read as convergence"* | PROSE |

Also mapped and **not** cross-cited, therefore outside the leg: `test_pre001_constants_are_what_was_registered`
(Paper III only) and, in superseded Paper I, `test_excess_demand_is_identically_invariant_to_the_allocation`.

### 2.3 · The finding the run built — and why it does not survive

The run's cell was: *both cross-cited guards are cited as holding several claims that come apart,
demonstrably by a manuscript edit alone, because **neither guard reads the manuscript**.* A third
reader was then instructed to **refute it**, told to default to REFUTED under uncertainty. It
returned **REFUTED**, on five grounds, of which three are decisive and are recorded here because a
run that reports only its surviving findings is grading itself:

1. **§1.1, the admission criterion, is fatal on its own.** *"A leg is admissible only if a competent
   fresh-eyes review of any ONE paper, done well, could not have found it."* **Both of the run's
   come-apart demonstrations are single-paper operations** — "edit Paper IV §5, run Paper IV's test",
   "rewrite `is_bounded`, run Paper II's module". Neither consults a sibling. The cross-citation was
   the finding's *framing*, not its *evidence*. Worse, Paper IV states the mechanism **in its own
   body**: §5 says the suite asserts *the monotonicity* and that the limit is carried *"under the
   name"*. A §5-versus-§10 comparison inside one document is the most ordinary single-paper review
   move there is. Reclassified `P7` per §1.1, which is **not advisory**.
2. **The corpus publishes the run's own thesis, in the sentence the run cited as concealing it.**
   Paper III §11 opens the paragraph: ***"Two tests are worth naming because of what they forbid
   rather than what they check."*** The forbid/check distinction *is* the finding, and the corpus
   states it in terms, unprompted, in the cross-citing passage. A defect cannot consist in failing to
   disclose the thing the disclosure discloses.
3. **The run dropped a scope clause and its second limb depended on the drop.** The run's mechanical
   exhibit was that `is_bounded` can be simplified to `top_share(res) <= 0.94` with the guard still
   green — **and that is true; the refuter checked all 18 tests in the module by exhaustion and
   confirmed no other test catches it.** But Paper II does not say *"any simplification fails."* Both
   of its sentences say *"fails … **instead of quietly re-scoring condensation as success**"*, and
   the `0.94` rewrite does not re-score condensation as success: §3.4's condensed runs sit at top
   decile 0.99–1.00, still above 0.94, still `not is_bounded`. **Under the rewrite every cited claim
   stays true.** That is the definition of *not* coming apart. The run quoted the sentence with its
   scope clause removed and built a come-apart out of the removal.

And the refutation clause is **literally satisfied, on the corpus's own words**, in both disjuncts:

- **monotone/SMD holds exactly one claim.** It asserts one proposition; all three papers describe
  that one proposition's *role*. Purpose ascriptions are not additional claims the guard holds.
- **flat-Gini holds a stated conjunction that the paper names as a conjunction.** Paper II §3.4:
  ***"The criterion now requires a settled Gini **and** a top decile below 0.90."*** §7 points the
  guard at §3.4 by section number. That is E5's second refuting disjunct verbatim.

### 2.4 · And the harm model does not obtain

E5's stated worry is *"a shared single point of failure across the corpus."* **A single point of
failure requires two loads.** Paper IV contains no Gini, no redistribution model and no saturating
statistic — §9.3 says *"This paper contributes no new computation"* — so the flat-Gini guard bears
**zero** load in Paper IV. The monotone/SMD guard bears zero load in Paper III, which merely reports
that *companion modules* carry it. **The multiplicity is bibliographic, not load-bearing** — which is
the opposite of an over-subscribed guard, and is the honest answer to the question E5 asked.

**The guard limb is REFUTED.**

---

## 3 · The count limb — and the fifth defect in the registration

### 3.1 · The counts, and the first time anyone checked one

| paper | the sentence | scope | pinned? | **true?** |
|---|---|---|---|---|
| **II** · §7 | *"the **18** tests in `tests/test_redistribution.py` are the ones that hold this paper's claims in place, and that count is the one quoted in the abstract and in §1"* | **module** | no | **yes** — 18 at `d655501` and 18 at head |
| **III** · §11 | *"**100 tests at the pinned commit d655501** … The suite at the head of the repository is larger and grows with every registration"* | **suite** | **yes** | **yes — verified here for the first time** |
| **IV** · §10 | *"`python3 -m pytest tests/ -q`"* | — | — | no count quoted |

**The verification, because nobody in fifty-eight sessions had run it.** `git ls-tree d655501 tests/`
returns six files; summing `def test_` across them at that commit gives **exactly 100**:

| module | at `d655501` | whose claims it holds |
|---|---|---|
| `test_edgar.py` | 42 | **III** |
| `test_redistribution.py` | 18 | **II** |
| `test_cournot.py` | 11 | **I — superseded** |
| `test_lag.py` | 10 | **III** |
| `test_lambda_sensitivity.py` | 10 | **III** |
| `test_excess_demand.py` | 9 | **I — superseded** |
| **total** | **100** | |

So Paper III's number is **right**, and it is right about the wrong object: of the 100 it offers as
its reproducibility apparatus, **62 hold Paper III's claims, 18 hold Paper II's, and 20 hold the
claims of a paper the corpus has withdrawn.** Paper II, in the same slot of the same template, was
careful to say *"are the ones that hold this paper's claims in place."* Paper III was not.

### 3.2 · The finding is REVIEW-004's, is four days stale, and E5 may not count it

`REVIEW-004` A3, 2026-08-12: *"**The test count contradicts itself across the batch.** Paper II says
**18 tests**; Paper III says **100 at the pinned commit**; the suite today runs **121**. One
repository, three numbers, visible to anyone with both PDFs open. Say '18 of the suite's N tests
cover this module.'"* Standing ruling: **A LEG MAY NOT COUNT A FINDING MADE BEFORE IT EXISTED.**
E5 scores nothing for it. **`REVIEW-004` is now right five times.**

What is new is the **magnitude**: the dossier measured the head suite at **121** four days ago; it
collects **1068** today, a factor of **8.8**. Paper III's *"the suite at the head is larger"* has been
carrying a ninefold gap since Tuesday, and the number sits in the bullet that instructs a replicator
to run `pytest tests/ -q` — which returns 1068, not 100. **The instruction and the number disagree by
an order of magnitude and the reconciliation is a clause about a pin.** Repaired in §5, and repaired
as `REVIEW-004`'s remedy, **not** as E5's.

### 3.3 · The gap, which is the leg's actual result

Apply E5's own two clauses to the count limb:

- **FAILURE** requires *"a count … that **moves** when another paper's work adds tests to the shared
  suite."* Paper II's is module-scoped: it does not move. Paper III's is pinned to a fixed commit:
  **it cannot move.** Failure is **not shown**.
- **REFUTATION** requires *"**every** count module-scoped rather than suite-scoped."* Paper III's is
  suite-scoped. Refutation is **not shown**.

**Both clauses are unmet, and E5 declares no UNDECIDED region.** `E1` declares one and forbids it
being *"rounded toward the corpus's comfort"* — which cuts identically against rounding it toward the
run's. So the count limb is **undecided by construction**, and because the leg's refutation clause is
a conjunction over both limbs, a refuted guard limb cannot carry the leg either.

**This is the fifth false-or-self-defeating premise found in `END-TO-END-001` by legs of
`END-TO-END-001`, and the fifth in a row that is about the registration rather than about the
papers:** §0's *"no written answer anywhere"* (`-56`); E1's audit-half *"no document mentions it"*
(`-56`); §2.0's three-and-three against six headings reading four-and-two (`-57`); §4.2-versus-§6 on
`E2` (`-57`); and now E5's non-complementary clauses. **The document's prose about the corpus has
held up perfectly. Its prose about itself is 0-for-5.** Per §5 the registration is FIXED and was not
edited; the repair, if a future pass wants E5 decided, is `END-TO-END-002` saying what changed.

---

## 4 · Admission accounting — what E5 may and may not count

| item | admissible as system-level? | why |
|---|---|---|
| the guard limb's come-aparts | **NO** | §1.1 — both demonstrations are single-paper operations; reclassified `P7` |
| Paper III's 100 being suite-scoped | **NO** | `REVIEW-004` A3, 2026-08-12, four days before this leg existed |
| the head-suite gap having grown to 8.8× | **NO** | a magnitude update on a pre-existing finding, not a new finding |
| **E5's clauses not being complements** | **YES** | a finding about the instrument, not about a paper; no per-paper reviewer can reach it, because no paper contains it |
| **the 100 at `d655501` verified, and its 62/18/20 decomposition** | **YES, as a measurement** | new, checkable, and nobody had run it; it decides nothing and scores nothing toward `T` |
| Paper II §1's *"18 tests including two"* (§5.2) | **NO** | `P7`/`P1x` — single-paper findable with one grep |

**`T` is unchanged at 2. No leg improves a verdict, and this one does not worsen it either.**

---

## 5 · What was done to the corpus

**None of this is an E5 remedy.** E5 did not fail; **applying a remedy whose antecedent did not occur
is re-choosing a fixed clause in the direction the run prefers** (`-57`'s ruling on `ADR-001`
§Consequences, and it binds here). Every edit below is owed to `REVIEW-004` A3 or to bug spray, and
is labelled as such.

### 5.1 · Paper III §11's count, module-scoped and derived — `REVIEW-004` A3's remedy, verbatim

The dossier's own prescription was *"Say '18 of the suite's N tests cover this module.'"* Applied to
Paper III in Paper II's template, with the numbers **derived rather than asserted** (`P3n`'s pattern):
the suite at `d655501` holds 100 tests, of which the **62** in `test_lag.py`,
`test_lambda_sensitivity.py` and `test_edgar.py` hold this paper's claims.

### 5.2 · Paper II §1's contribution 5 — bug spray, found while mapping

§1 said the claims are *"held in place by 18 tests **including two** that exist specifically to make
overclaiming fail loudly."* **Only one of the two is among the 18.** `test_a_flat_gini_does_not_mean_a_bounded_one`
lives in `tests/test_redistribution.py`; `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`
lives in `tests/test_excess_demand.py` and is not in the counted module. §7 never claimed it was —
§1 compressed §7 and lost the distinction. One sentence, corrected in place. **The abstract was not
touched**: it says only *"an open repository with 18 tests"*, which §7's scoping makes true, and it is
a submission field with a word bound that `-57` broke by lengthening one.

### 5.3 · `tests/test_paper_test_counts_are_derived.py` — the repair that makes it stay fixed

Prose repaired by hand rots. The counts are now **derived from `git` at each paper's own pinned
commit and asserted against the manuscripts**, so a future session that adds tests to the shared
suite and lets a paper's number drift gets a red test rather than a reader with two PDFs open. This
is the corpus-level half of the fragility and it is the half `REVIEW-004` could not fix with prose.

### 5.4 · What was deliberately NOT done

- **`END-TO-END-001` was not edited.** §5 forbids it and the defect found here is exactly the kind a
  run is most tempted to edit away.
- **E5's pre-registered repairs were not applied.** No guard was split; no count was rewritten *as an
  E5 remedy*. The leg did not fail.
- **`P7` on Paper III was not opened.** This run rewrote Paper III §11 and **must not also score it**
  (`-57`'s rule, applied to itself).

---

## 6 · Supplementary — measured, outside the verdict

**`-58` IS STILL ELIGIBLE FOR `E2`'s BLIND PASS, AND DELIBERATELY SO.** `-56` and `-57` are
disqualified because §6 told them to read `END-TO-END-001` end to end and §4.2 says that destroys the
leg. **This run read lines 1–204 and 241–505 and stopped at the `### E2` heading, never reading
§2/E2's candidate.** The reading was cut at the boundary on purpose, before any of this leg's work
began. **`E2` is therefore still runnable blind by this session or by a successor briefed the same
way — and it is the one leg a rushed session destroys by opening the file.**

**Collected in passing, counted nowhere.** Superseded Paper I quotes a third scoping — *"109 tests
across the repository, of which 22 hold this paper's two modules"* at commit `6492157` — which
matches neither `d655501`'s 100/20 nor head's 566/22. Paper I is withdrawn and marked so; it is
recorded here only because it is the *third* incompatible scoping of one quantity in one repository,
and because 20 of Paper III's 100 are its.

---

## 7 · What this does not license

A leg that returns UNDECIDED has **not** shown the apparatus is sound. It has shown that **E5, as
written, cannot tell** — and, separately and more usefully, that on the evidence gathered the
multiplicity of the two cross-cited guards is bibliographic rather than load-bearing (§2.4). Those
are different statements and the second is the run's judgement, not the registration's verdict. A
successor that wants the verdict must write `END-TO-END-002`.

And the pass verdict is unchanged: **THE SYSTEM FAILS**, on `E1` and `E3`, at `T = 2`, with `E4`,
`E6` and the pass-level `RESULT-END-TO-END-001.md` still open and `E2` still blind.

*Coffee status: ☕ the run built a finding, aimed a refuter at it, and lost — which is the machinery
working, not failing. The afternoon's real yield is that the corpus's fifth self-referential defect
was found the same way the other four were: by a leg of the document, pointed at the document. Five
for five, all about itself, none found by the design.* 🥎
