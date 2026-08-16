# END-TO-END-001 — what it would mean for Papers II, III and IV to fail AS A SYSTEM
*wealthTensor-55 · 2026-08-16 · **DESIGN ONLY. NOT RUN.** Registered in its own commit, ahead of
any commit that runs any leg of it, on the `REG-013` precedent
(`tests/test_registrations_precede_their_instruments.py` is what checks that ordering for
registrations; this document asks the same discipline of itself and `git log --follow` is the
evidence).*

**Closes the design half of `P11`. Running it is a later session's at-bat and this document is
what that session is graded against.**

---

## 0 · What this is, and the two-line reason it is not `P7` done three times

`ADR-001` addendum 6 (`wealthTensor-08`, 2026-08-11) recorded Jason's methodological position and
left one question open with no written answer anywhere in this repository:

> *"I want to wait until we have the corpus done (so we can test it end to end; right now we're
> testing the individual parts like those who use error-statistical philosophy; correct approach
> here — when we're done with the papers, I want to re-test the entire system at once)."*
>
> **What would it mean for the three papers to fail as a system, as opposed to one of them
> failing?**

`P7` converges each paper against its own claims. That is a different object. **A corpus of three
individually-correct papers can still be wrong**, and the ways it can be wrong are exactly the ways
a per-paper reviewer is structurally unable to see, because a per-paper reviewer grades a paper
against the claims that paper makes. Nobody in the process so far has been assigned the claims the
corpus makes and no paper states.

**And the answer must be written before it is known.** `P11`'s own board note says so, and it is
this project's standing rule (`REG-001` through `REG-013`, and the reason §6.3 of Paper III was
withdrawn): a test designed after the results are in is not a severe test. The three per-paper
results are already known. What is not yet done to the papers is `P7`, and **a system test written
after `P7` has polished the prose is a test the polished corpus passes.** The window in which this
design can still be honest is open now and `P7` is what closes it. That is why this document exists
in the session it does, and why the session that wrote it did not run it.

---

## 1 · The system under test, stated so that it can fail

The corpus is not three papers about related topics. `ADR-001` §Relitigation record, leg 1, states
what it is, and states it as a **claim**:

> *"The three fields are layers of one stack" is itself the fourth claim, and it is stronger citing
> I–III as established results than asserting all three legs inside one document. The decomposition
> promotes the conjunction; it does not discard it.*

So:

> **S · THE SYSTEM CLAIM.** There is one object — a holding with a physical component and a claim
> component recorded against it — and Papers II, III and IV describe *the same* object's measuring
> layer at three scales. Paper III supplies the firm scale (the reporting filter, φ / α / δ),
> Paper II supplies the sovereign scale (the assessing layer, base / rate / ρ, through κ), and
> Paper IV asserts that these are **one chain and not three analogies**, in terms:
>
> *"Note what makes this a chain rather than three analogies. At each step the same two components
> appear, the same question is asked of them — what does the measuring layer observe? — and the
> answer at each scale is a quantitative one that the paper for that scale reports."* (Paper IV §3)

**S is the thing this test can break.** Every leg below attacks S, or attacks the corpus's ability
to say honestly what it has established, and nothing else.

### 1.1 · The admission criterion for a leg — the guard that keeps this from being `P7` again

> **A leg is admissible only if a competent fresh-eyes review of any ONE paper, done well, could
> not have found it.**

Applied at design time to every leg below, and applied again **at run time**: any finding a run
produces that a single-paper review could have found is **reclassified as a `P7` finding, logged as
one, and does not count as a system-level result.** A run that reports six findings, five of which
are per-paper, has found one thing.

This clause exists because the cheapest possible failure of `P11` is that it re-reads three papers
carefully, finds ordinary defects, declares the corpus audited, and never tests the conjunction at
all. That run would look exactly like a successful one.

### 1.2 · What is NOT a system-level failure — committed here, while it is cheap to say

- A claim inside one paper being wrong. That is `P7`, and it is contained by design (`ADR-001`
  §Consequences).
- A reference error, a typo, a stale number, a broken pin. Those are guarded and mechanically
  checked (`P1x`/`P3x`/`P5x`, forty rows, all red-proofed).
- A paper being unpersuasive, thin, or badly organised. That is `P7`'s and `P8`'s business.
- **A registered prediction having failed.** Paper III's did. It is reported at full length and in
  the abstract. A corpus that reports its losses is not thereby a failing corpus, and any run that
  scores §5's null as a system failure has misread this document.

---

## 2 · The six legs

Each leg carries: the check, **what evidence shows failure**, **what evidence refutes it**, a
declared UNDECIDED region where one applies, and its classification.

### 2.0 · TEST vs AUDIT, and why the distinction is registered rather than discovered

A leg whose outcome the designer can already predict is not a severe test. It may still be worth
running — a fact worth stating whole is worth stating whole — but **calling it a test inflates the
run**. A pass that reports "five of six legs clear" means nothing if three of the six could not
have gone the other way. So each leg is classified **now**:

- **TEST** — the outcome is genuinely unknown to the designer at the time of writing. It can lose.
- **AUDIT** — the outcome is anticipated. The value is in stating it whole and in the **remedy,
  which is pre-registered here so that the run cannot argue about it afterwards.**

The run reports the two counts separately. **Three legs are TESTs and three are AUDITs**, and the
run may not report a single combined score.

---

### E1 · THE SHARED DEGENERACY — *is the join between Papers II and III load-bearing, or is it vocabulary?* **[TEST]**

**The corpus asserts this join twice, in two different volumes**, which is what makes it the spine
of S rather than a passing remark:

> *"A levy that cannot see an accrual and a financial statement that does not record a degradation
> are the same structure — a measurement layer with a systematically incomplete view — seen from
> two sides."* (Paper II §3.2)

> *"Paper II's κ … is a composition quantity: it is defined at the sovereign scale and it is a fold
> over household-scale liabilities. Paper III's φ ⊙ δ is a composition quantity…"* (Paper IV §3)

**"Same structure" is either a checkable claim or it is an adjective.** Paper III's structure has a
sharp, published content: the reported series identifies the **product** φδ and contains nothing
further about φ — timeliness and durability are not separately identified, and no estimator can
recover the factor from the observable (§4.2, held to 7 × 10⁻¹⁴). If Paper II's ρ and *r* stand in
the same relation to Paper II's observable, then **Paper II has an unstated non-identification
result of exactly Paper III's form**, and the chain predicted it before anyone looked. If they do
not, the chain's sovereign link is a resemblance the two models deny.

#### E1a · the dimensional pre-check, run FIRST because it can settle the question cheaply

Build a symbol table across the three papers: symbol → paper → definition → domain → what it is a
share **of**. Two failure shapes, both fatal to "same structure" without any simulation:

- a symbol carrying two non-identical definitions across papers;
- an **equated** pair whose referents differ in kind — and the candidate is already visible:
  **φ is a share of a *change* (degradation) that reaches the claim layer; ρ is a share of a
  *gain* that is recognised as flow.** One is about what the recording layer can see of a loss, the
  other about what the assessing layer can see of a profit. That may be the same structure. It may
  also be two things wearing one sentence.

**If E1a returns a difference in kind, E1b is not run**, because a simulation cannot rescue an
equation between two objects of different type. The leg reports FAIL at E1a and says so.

#### E1b · the iso-κ locus, within the flow base

*Read the construction off the committed code, never off the paper's closed form.* The
implementation (`src/wealth_tensor/redistribution.py`) does **not** make κ a clean product of *r*
and ρ, and this is the reason the leg is a test rather than an algebra exercise:
`recognised_flow += rho * gain + wage`, then `assessed = max(recognised_flow, 0)`. The wage enters
the base **unscaled by ρ**, and the clip at zero is non-linear. So *r* scales the liability while ρ
scales the **dispersion** of the base toward a wage floor. Whether the observable can tell those two
apart at matched κ is not obvious from the code and is not stated anywhere in the corpus.

1. **Locate the locus numerically.** Sweep (*r*, ρ) on the flow base at the paper's standard
   parameters (*N* = 800, μ = 0.05, σ = 0.20, *a* = 0.05, *T* = 1200, tail-quarter statistics) and
   find pairs whose measured κ agrees to within **1 %** relative. Report the locus, including
   whether it is non-trivial.
2. **Compare the observables**, not one scalar: the **stationary Gini**, the **top-decile share**,
   and **Var[log a]** — the last because Paper II §3.1 already uses it to show that two levies with
   the same κ can act on different objects, which is precisely the discriminating instrument this
   leg needs and it is already in the corpus.
3. **Seed noise is the yardstick and is measured in the same run**: the same (*r*, ρ) point across
   **≥ 20 seeds** gives the within-point spread. Nothing is called a separation that is not large
   against it.

**FAILURE (the join is vocabulary at the sovereign scale) is shown by:** matched-κ (*r*, ρ) pairs
producing statistics separated by **≥ 3×** the within-point seed spread on any of the three
observables. Paper II's observable then identifies the factors that Paper III's observable cannot,
the two layers do not share the structure the corpus attributes to them, and the join is a
resemblance.

**FAILURE IS REFUTED BY:** matched-κ pairs indistinguishable — all three statistics within **1×**
the seed spread across the whole admissible locus. Paper II then carries its own non-identification
result, of Paper III's shape, and **the system test has produced a new result the papers did not
have.**

**UNDECIDED:** separations between 1× and 3× the seed spread. Reported as undecided and **not
rounded toward the corpus's comfort.**

**VOID:** if no non-trivial iso-κ locus exists (the sweep finds no pair beyond the trivial one), the
leg is void for want of a locus and **may not be reported as either outcome.** A void E1b leaves
E1a's verdict standing alone and says so.

**And E1 carries an audit half the corpus has already published without noticing.** Paper II §3.1
reports that at matched κ ≈ 0.10 the **stock** and **flow** bases give Gini 0.222 against 0.125 —
κ under-determines the outcome *across* bases. Paper III's φδ, by contrast, determines the reported
series exactly. **That is a prima facie disanalogy between the two layers, visible in numbers both
papers already print, and no document in this repository mentions it.** The run records whether the
corpus acknowledges it anywhere. It does not, today.

**What the corpus does with each outcome:**

| E1 outcome | what changes, and where |
|---|---|
| **refuted (join load-bearing)** | Paper II gains a short §3.x reporting its own non-identification result, with the locus and the numbers. Paper IV §3 gains the sentence naming the *shared* degeneracy, which is the strongest form the chain claim has ever had. Both are new content earned by the conjunction, which is what a system test is supposed to be able to produce. |
| **failed (join is vocabulary)** | Paper II §3.2's outward-connecting paragraph is cut back to a claim about observability alone, with the "same structure" sentence removed. Paper IV §3's *"a chain rather than three analogies"* is **demoted in terms** to *"three instances of one question, asked at three scales"* — weaker, honest, and still worth publishing. **The demotion is written before the run so that it cannot be negotiated after it.** |
| **undecided / void** | Both papers gain one sentence stating that the correspondence between ρ and φ is asserted structurally and is **not** established quantitatively, with this document cited. An undecided leg buys a disclosure, never a claim. |

---

### E2 · THE UNOWNED CLAIM — *does the conjunction assert something no paper defends?* **[TEST]**

The canonical system-level defect. Three papers, each hedged correctly, can leave a reader holding
a fourth belief that lives in none of them — and **no per-paper review can find it**, by
construction, because each reviewer grades a paper against that paper's claims.

**The check.** A pass that has **not read §2's candidate list below** reads the three abstracts and
the three contributions lists in the corpus's own order (II → III → IV) and writes down, in plain
sentences, what a competent economist would now believe the corpus has established. For each
sentence: name the paper, the section, and the result or the explicit limitation that owns it.

**FAILURE is shown by:** one or more sentences that (a) a reader would carry away from the three
documents read together, (b) are not stated as a claim in any single paper, and (c) have no
evidence anywhere in the corpus and no limitation disclaiming them. **One is enough.** An unowned
claim has no home in which it could ever be checked, which is the whole of the objection.

**FAILURE IS REFUTED BY:** every extracted sentence tracing to a paper, a section, and either a
result or a disclaimer.

**The power check, and it is the reason this leg can be trusted.** The designer's candidate is
recorded here, in advance, and the blind pass runs first:

> Paper IV §4.3: *"the extensive state … **does** survive the sum, and it is very largely not being
> measured."* That is a claim about **the world's measurement practice**. Paper II measures a model
> class. Paper III measures a filter and one EDGAR sample. `REG-013` measured a **citation graph** —
> which is a fact about what a literature reads, not about what anyone measures. If the blind pass
> does not surface this sentence, the extraction lacked the power to find one, and **the leg is
> reported as under-powered rather than as passed** — the `REG-013` ceiling discipline, applied to
> a reading pass instead of an instrument.

**What the corpus does:** an unowned claim is **owned or cut**, and the choice is not free — it is
owned only if a paper can name the evidence, and cut otherwise, in the same session that finds it.
Paper IV is the conjunction's carrier and is the default owner of anything the conjunction asserts.

---

### E3 · THE CONTAINMENT MATRIX — *is the promise `ADR-001` made about failure true?* **[TEST]**

`ADR-001` §Consequences, 2026-08-05, promised a **system-level** property and it has never been
tested:

> *"Failure is contained. A rejection of III no longer takes I and II with it."*

Paper IV states the other direction in terms — *"A reader who rejects Paper II or Paper III should
reject the corresponding link here"* (§9.3) — so containment is already known to be asymmetric. What
is not known is the **shape** of the dependency, and shape is the thing that decides whether the
corpus is a stack or a star.

**The check.** Build a 3 × 3 matrix by **quotation only**: for each ordered pair (P, Q), the cells
list the claims in Q that become unsupported if P's headline claim is assumed false, each cell
justified by a cited sentence from Q. No inference beyond what a quoted sentence says.

**FAILURE is shown by any one of:**

- the matrix is **not** lower-triangular in the corpus's own stated dependency order (II → III → IV)
  — that is, a paper the corpus treats as upstream turns out to depend on one downstream of it;
- striking a **single** paper removes claims from **both** others, making the containment promise
  false as written rather than merely asymmetric;
- the corpus's entire empirical content sits in one cell, so that the corpus's exposure to the
  world is a single point of failure while reading as three.

**FAILURE IS REFUTED BY:** a lower-triangular matrix whose only off-diagonal load is the dependency
Paper IV §9.3 already declares.

**What the corpus does:** if the matrix is a star rather than a stack, **`ADR-001` §Consequences
gets a dated addendum retracting the containment sentence** — the `-37` precedent — and Paper IV's
§9.3 is widened to state the true shape. A promise a decision record made and did not keep is
exactly the kind of thing this repository has been finding for fifty sessions, and the remedy is
always the same: amend the clause, do not let the addendum carry the fix.

---

### E4 · THE CORPUS'S EMPIRICAL CONTENT, STATED WHOLE **[AUDIT]**

Each paper reports its own epistemic position honestly, and the three positions have never been
added up.

- Paper II: *"no empirical data is used at all — every number is generated by simulation"* (§7);
  *"No field evidence is used, required, or available"* (§5.2).
- Paper III: *"**the framework currently has no confirmed empirical claim.** It has a model with
  derived consequences, one registered prediction that failed, and a stated method for building the
  next one"* (§6.1).
- Paper IV: *"This paper contributes no new computation"* (§9.3), plus one measurement on the
  citation graph.

**The check.** Enumerate every claim in the corpus about **the world** — not about a model, not
about a literature — that any paper asserts as confirmed. Count them.

**FAILURE (as an audit finding) is shown by:** the count being zero **and** no document in the
corpus stating that at corpus level. The defect is not the zero — a corpus of model-class results
with one honest lost bet is a legitimate and unusually candid object. **The defect is the silence
about the sum**, produced by three papers each disclosing only its own share. That silence is
invisible to every per-paper reviewer and visible immediately to anyone reading all three.

**REFUTED BY:** a positive count with the claims named, or a paper that already states the
corpus-level position in terms.

**Classified AUDIT because the designer expects the count to be zero.** Saying so here is what
stops the run from reporting a discovery.

**What the corpus does — pre-registered, so the run cannot argue about it:** the remedy is **one
sentence in Paper IV**, the conjunction's carrier, in §1 or §9, stating what the corpus has and has
not established about the world. It is **not** a retraction and it is **not** a hedge added to each
paper. The corpus's strongest available move here is to say the thing plainly first, since a
reader who works it out unaided will conclude the papers were arranged to prevent it.

---

### E5 · THE OVER-SUBSCRIBED GUARD — *does one test hold two claims that could come apart?* **[TEST]**

The corpus's reproducibility apparatus is shared. Two tests are cited by name in **two different
papers**:

- `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` — Paper II §7 (*"constrains the
  companion paper in the same suite"*) and Paper IV §10;
- `test_a_flat_gini_does_not_mean_a_bounded_one` — Paper II §7 and §4, and Paper IV §10.

A guard that holds one claim is a guard. A guard cited as holding two claims in two papers is a
**shared single point of failure across the corpus** — and whether the two claims can come apart is
not something either paper's reviewer would ask, because each sees only its own.

**The check.** Build the guard → claim map across all three papers: every test named in any
data-and-code section, every paper that names it, and every claim it is said to hold. Then, for each
multiply-cited guard, ask the discriminating question: **is there a state of the world in which
claim A is false, claim B true, and the test passes in both?** Additionally: is any paper's quoted
**test count** invariant to a sibling paper adding tests to the same suite?

**FAILURE is shown by:** a guard cited as holding two claims that can come apart; **or** a count in
any paper that moves when another paper's work adds tests to the shared suite. A number that is not
invariant to a sibling's edits is a corpus-level fragility, and `P3n` already established the shape
of the repair (derive the count, do not assert it).

**FAILURE IS REFUTED BY:** every cross-cited guard holding exactly one claim, or holding a stated
conjunction that the paper names as a conjunction; and every count module-scoped rather than
suite-scoped.

**What the corpus does:** a guard holding two separable claims is **split into two tests**, one per
claim, and both papers repointed. A suite-scoped count is rewritten as a module-scoped one and
derived, not asserted — `P3n`'s pattern, applied to whatever E5 finds. Both repairs are cheap; the
finding is what is expensive to get.

---

### E6 · THE CROSS-PAPER CONTRADICTION — *does the corpus assert and deny the same fact in two volumes?* **[AUDIT — and it has a worked example, found while this was being designed]**

The purest system-level defect available: two papers, each internally consistent, that disagree
with each other about a fact of the shared framework. **No per-paper review can see it.** Both
papers pass their own review; the corpus is broken.

**The check.** Enumerate the facts the papers **share** — the framework's parameters, the
registered tests and their status, the propositions P1–P3, the corpus's own results as cited across
volumes. For each, extract every paper's statement of it and compare truth value and modality
(*asserted* / *conditional* / *open* / *rejected*).

**FAILURE is shown by:** any shared fact whose modality differs across papers in a way that changes
what a reader may conclude — most sharply, a fact one paper reports as **settled** and another
carries as **pending**.

**FAILURE IS REFUTED BY:** every shared fact agreeing in truth value and modality across every
paper that states it.

#### E6's worked example, disclosed here rather than banked as a future win

**Found on 2026-08-16 while reading the three papers to design this document, not by running this
leg.** It is recorded here because it is the evidence that E6 is worth a session's time, and it is
**excluded from E6's run** — a leg may not count a finding made before it existed.

> **Paper III §9, limitation 9:** *"The diagonality of the reporting layer is an assumption, it was
> testable, and **it is false**. … §5.4 puts the resulting prediction — independence across classes
> within a firm-quarter — to the registered sample and **rejects it in both universes in the same
> direction, at 4.12× and 2.02×** the independence expectation."*
>
> **Paper IV §4.4.3:** *"Diagonality is assumed at the firm scale. §3 names this and Paper III
> registers the test. **Until it returns**, the composition chain has an unverified link at exactly
> the scale where the accounting is done."*
>
> **Paper IV §9.2:** *"Diagonality at the firm scale is assumed and **its test is open**. **If**
> recognition events cluster within firm-quarters, the Hadamard form in §3 is wrong and the chain
> has a broken link."*

**The test returned. The antecedent is true.** Paper IV's own conditional therefore entails that the
Hadamard form in its §3 is wrong and the composition chain has a broken link at the firm scale —
and Paper IV does not know it, because the sentence was written while the test was genuinely open
and nobody has since read the two papers side by side. **The paper carrying the corpus's chain
claim is the paper that does not know the chain's firm-scale link was measured and rejected.**

**Repaired in the commit immediately following this one**, per the standing rule that a correction
which lives only in a document has not been made. The repair states the measured result, the
direction, and the bounded consequence Paper III already supplies (*"the Hadamard form is an
approximation whose error is now measured"*) rather than deleting the chain — a measured
approximation with a stated error is a stronger object than an untested assumption, and it is
also, now, the honest one.

**What the corpus does with E6 generally:** every contradiction found is repaired in the session
that finds it, in the artefact, and the *later-dated* paper is repointed at the *measured* fact —
never the other way round.

---

## 3 · The verdict rule for the pass as a whole, pre-committed in both directions

Let **T** be the count of TEST legs that FAIL and **A** the count of AUDIT legs that FAIL.

- **THE SYSTEM HOLDS** iff **T = 0** and every AUDIT finding has been repaired in the run's own
  session. The corpus may then be described as one corpus, and `P13` may depict it as a stack.
- **THE SYSTEM IS WOUNDED** iff **T = 1**. The corpus is still a corpus, the failed leg's
  pre-registered demotion (§2) is applied in full, and **the demotion is not negotiable after the
  fact** — that is the whole reason it is written above rather than below.
- **THE SYSTEM FAILS** iff **T ≥ 2**. The conjunction is not established. Concretely, and this is
  what "fail as a system" cashes out to:
  1. **Paper IV loses its chain claim** and becomes what it can still honestly be — a survey of
     three literatures, a measured whitespace, and one worked instance — with §3 rewritten from a
     chain into three parallel instances and the abstract's *"the same atomic unit composes from
     the household to the sovereign"* narrowed to the scales actually joined.
  2. **Papers II and III are unaffected and ship as independent works.** That is `ADR-001`
     §Consequences' containment promise being *cashed*, not a consolation. It is also the outcome in
     which the decomposition decision is retrospectively vindicated: a monolith would have taken all
     three down.
  3. **`ADR-001` gets a dated addendum** recording that the fourth claim — the one the relitigation
     record promoted rather than discarded — did not survive its own first end-to-end test, at
     length, with the numbers.
  4. **`P13` renders three works, not one stack.** The deliverable depicts what the corpus is, and
     what the corpus is depends on this verdict. This is why `P13` is last and why running this test
     before building it is not optional sequencing.
- **VOID:** if E1 voids **and** E2 reports under-powered, fewer than two TEST legs returned a
  verdict and **no system-level conclusion may be read off the run at all** — favourable or
  otherwise. A void pass is reported as a void pass and re-run under `END-TO-END-002`.

**The stopping rule.** The corpus gets **exactly one first end-to-end pass** (`ADR-001` addendum 6's
batch ruling). This is it. A second pass may be run only under a **new** registration that says what
changed and why, and it may not cite this pass's numbers as support for its own design.

**What a favourable result does NOT license, committed now while it is still cheap to say.** A
corpus that survives this pass has been shown to be internally coherent and honestly summed. **It
has not thereby been shown to be right about the world.** Paper III §6.1 governs the corpus as it
governs Paper III: the framework has no confirmed empirical claim, and no amount of internal
coherence supplies one. A run that closes with "the system holds, therefore the framework is in
good shape" has committed the corpus-scale version of the error §6.3 of Paper III was withdrawn for.

---

## 4 · Threats to the validity of THIS DESIGN, named before any of it is run

1. **The designer read all three papers before writing the legs.** Unavoidable — a system test
   cannot be designed by someone who has not read the system — and it is the reason E1's outcome had
   to be one the designer could not predict, the reason E2 carries a blind pass with a power check,
   and the reason each leg is classified TEST or AUDIT above rather than after.
2. **E2's candidate is named in this document and could prime the run.** Mitigated by ordering:
   the blind pass records its list **first**, and the comparison is a measurement of the extraction's
   power, not of the corpus. A run that reads §2's candidate before extracting has destroyed the leg
   and must say so.
3. **Six legs are not an exhaustive partition of the ways a corpus can fail.** Nothing here claims
   they are. They are the six a reader can check, in an object with three papers and this particular
   spine. A seventh found during the run is admissible **only if it passes §1.1's admission
   criterion** and is recorded as an addition to the design, dated, with the reason it was not
   foreseen — which is a finding about this document and worth having.
4. **E1's iso-κ locus may not exist**, in which case the leg's cheap half (E1a) carries the whole
   weight. The VOID rule is stated so this cannot be discovered and then quietly absorbed.
5. **This design was written before `P7`, which is its point and also its cost.** `P7` will change
   the prose the legs quote. Every quotation above is therefore anchored to a **section and a
   claim**, not a line number, and a run that finds a quotation moved must locate the claim rather
   than report the leg unrunnable.
6. **The run will be tempted to score the corpus rather than test it.** Six legs, five clean,
   reads like a grade. It is not one: three of the legs cannot lose, and the verdict rule in §3 is
   counted over TESTs only.

---

## 5 · What is fixed by this document

The six legs and their classification (§2), each leg's failure and refutation criteria, E1's
thresholds (1 % κ match, 3× / 1× seed spread, ≥ 20 seeds) and its VOID rule, E2's blind-first
ordering and its power check, the whole-pass verdict rule and the stopping rule (§3), and §1.1's
admission criterion.

**None of these may be re-chosen in response to a result.** If a leg turns out to be
mis-specified, the repair is a **second registration** — `END-TO-END-002` — that says so and says
why, on the `REG-001` precedent, and not an edit to this file.

**What is deliberately left open:** who runs it, in how many sessions, and in what order the legs
are taken — except that **E1a precedes E1b** and **E2's blind pass precedes reading §2's candidate**.

---

## 6 · For the session that runs this

You are `-56` or later. Read this file end to end before touching anything, then:

- `docs/RESULT-END-TO-END-001.md` is the deliverable, in the shape of this repository's other
  `RESULT-*` documents: what was run, what came back, drop accounting, and the verdict read off §3's
  rule rather than off your judgement.
- **Report the TEST and AUDIT counts separately.** §2.0 exists to stop a combined score.
- Every leg you run, run to its stated criterion — including the ones you expect to lose. **A leg
  skipped because its answer seemed obvious is the failure mode this document was built to prevent**,
  and it is the same failure mode as designing the test after the results.
- If you find a seventh leg, §4.3 tells you what it has to clear.
- The verdict changes what `P13` depicts. Do not let anyone build the deliverable before you land.

*Coffee status: ☕ this document is the first thing in fifty-five sessions written to be able to
lose on behalf of the whole corpus. The papers have each been given a severe test. The conjunction
never has. It has one now, and nobody yet knows what it says.* 🥎
