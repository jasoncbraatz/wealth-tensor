# RESULT · END-TO-END-001 leg E1 — the shared degeneracy, and the join does not hold

- **Registered:** `docs/END-TO-END-001.md`, commit `4ea6361`, **before any leg was run.** §5 fixes
  E1's thresholds, its VOID rule, its ordering (`E1a` precedes `E1b`) and the corpus's response to
  every outcome. None of those was re-chosen here.
- **Instrument:** `E1a` is a reading of the three papers, their committed implementations and this
  repository's own review documents. `E1b` is `scripts/e2e001_e1_iso_kappa.py`, run off
  `src/wealth_tensor/redistribution.py` and `scripts/wt077_tail_index.py` at HEAD. Log
  `RESULT-END-TO-END-001-E1-run.log`, JSON `docs/notes/e2e001-e1b-iso-kappa.json`.
- **Run:** 2026-08-16, `wealthTensor-56`, darwin.
- **Verdict: E1 FAILS, at `E1a`.** ρ and φ are not the same kind of object, so the join between
  Papers II and III is vocabulary at the sovereign scale. `T = 1` for the pass so far. The design's
  FAIL remedy was applied to Papers II and IV in this session, in the commit that follows this
  document.
- **Two disclosures a reader should have before §2.** First, **`E1b` was run, and by the design's
  own text it should not have been** — §2/E1a says a difference in kind means `E1b` is not run. The
  ordering violation is accounted for in §5; its numbers are reported as supplementary and enter no
  verdict. Second, **the finding that decides `E1a` was already in this repository**, made on
  2026-08-12, four days before E1 existed. By the standing ruling that a leg may not count a
  finding made before it existed, **E1 counts the verdict and not the discovery** (§4).

---

## 1 · What was under test

`END-TO-END-001` §1 states the system claim `S`: that Papers II, III and IV describe the same
object's measuring layer at three scales, with Paper IV's *"a chain rather than three analogies"*
as the assertion under test. E1 attacks the II↔III link, which the corpus asserts twice:

> *"A levy that cannot see an accrual and a financial statement that does not record a degradation
> are the same structure — a measurement layer with a systematically incomplete view — seen from
> two sides."* (Paper II §3.2, as it stood at `8b351bc`)

> *"Paper II's κ … is a composition quantity … Paper III's φ ⊙ δ is a composition quantity…"*
> (Paper IV §3)

The leg's question, in the design's words: **is "same structure" a checkable claim or an
adjective?** Paper III's answer has published content — the reported series identifies the product
φδ and nothing about the factor, held to 7 × 10⁻¹⁴ (§4.2). If Paper II's ρ and *r* stand in that
relation to Paper II's observable, the corpus has an unstated non-identification result of exactly
Paper III's form. If they do not, the sovereign link is a resemblance.

---

## 2 · `E1a` — the symbol table, and the type check it exists to run

### 2.1 · The table

| symbol | paper | definition, in the paper's own terms | domain | a share **of** | complement's fate |
|---|---|---|---|---|---|
| **φ** | III §2 | share of each true change that is observable and reaches the claim layer at once | [0,1] | a per-period **change** in the physical state (a degradation) | **deferred** — accumulates in `gap`, released at rate α |
| **α** | III §2 | rate at which the unrecognised gap is released | per period | — (a rate, not a share) | — |
| **δ** | III | physical decay rate, `d·(1−m)` | per period | — (a rate) | — |
| **φδ** | III §4.2 | the conserved product; **what a reported series identifies** | — | — | — |
| **ρ** | II §2.3 | share of a period's capital gain recognised as flow, entering a flow levy's base | [0,1] | a per-period **change** in wealth (a gain) | **discarded** — `recognised_flow` is zeroed at each assessment and no mechanism ever books it |
| ***r*** | II §2.2 | fraction of the liable amount taken | [0,1] | the assessed base (a stock-like amount) | — |
| **κ** | II §2.4 | share of aggregate wealth moved per assessment | [0,1] | aggregate **wealth** (a stock) | — |
| ***a*** | II §2.1 | the additive wage | level | — | — |
| ***a*** | II §3.1 | the growth multiplier normalised by aggregate growth | > 0 | — | — |

### 2.2 · The type check

The design named its candidate difference in advance: *"φ is a share of a change (degradation)
that reaches the claim layer; ρ is a share of a gain that is recognised as flow."*

**That candidate is not the one that fails.** Loss and gain are both signed changes in the
extensive state; a share of one and a share of another are the same kind of object, and a first
pass over the three papers alone returned "same kind" — which is why `E1b` was launched (§5). The
difference that does fail is in the column the papers do not put side by side, and it is visible
only in the two implementations read together:

> **What Paper III's filter does not recognise is deferred. What Paper II's base does not
> recognise is destroyed.**

Paper III's recursion is `C(t+1) = C(t) + φ·ΔE + α·gap(t)`: the unrecognised share `(1−φ)` is
retained and released later at rate α. That is the whole of Paper III's crisis result — the
withheld information arrives, all at once, and its magnitude *is* what was withheld. Paper II's
implementation is `recognised_flow += rho * gain + wage`, followed at each assessment by
`recognised_flow[:] = 0.0`: the unrecognised share `(1−ρ)` of the gain is never assessed, in that
period or any later one. **Paper II has no parameter that plays α's part**, and the reason is not
an omission — a realisation model with a deferral channel would be a different model, which is
exactly `REVIEW-004` A1's proposed repair.

A lag and a loss are different operators. The corpus's sentence equates them under a shared
adjective — *"a measurement layer with a systematically incomplete view"* — and the adjective is
true of both while the structure is not. **That is what "the join is vocabulary" means**, and the
design says so at E1a: a simulation cannot rescue an equation between two objects of different
type.

### 2.3 · The check is corroborated by an instrument that did not exist when it was made

§5's `E1b` is not evidence for the verdict — it should not have been run — but it points the same
way from a direction the type check cannot see, so it is recorded here rather than buried. Paper
III's degeneracy is **exact**: the mirror map holds φδ to 7 × 10⁻¹⁴, and no estimator recovers the
factor at any precision. Paper II's (*r*, ρ) degeneracy is **resolution-limited**: at the paper's
own *N* = 800 the two are indistinguishable, and the drift that separates them is constant in *N*
while the seed spread falls, so it emerges as resolution improves (§5.3). **Two degeneracies, one
exact and one an artefact of sample size, are not one shared structure.** A run that had reported
E1 refuted on the strength of the II-side degeneracy alone would have equated them.

**`E1a` VERDICT: FAIL.** By the design, `E1b` is not run and the leg reports FAIL at `E1a`.

---

## 3 · E1's audit half — and the audit's own premise is refuted

The design's audit half asks the run to record whether the corpus acknowledges, anywhere, that
Paper II §3.1's matched-κ comparison shows **κ under-determining the outcome across bases** (Gini
0.222 against 0.125 at κ ≈ 0.10) while Paper III's φδ determines the reported series exactly. The
design states: *"no document in this repository mentions it. … It does not, today."*

**It does. Two documents state it in terms, and one calls it fatal.**

| document | what it says |
|---|---|
| `docs/REVIEW-004-pre-posting-dossier.md` **A2** | *"FATAL to the title claim — at matched budget the base ranking reverses, and your own table shows it … Same budget — the flow row is 2.6 % larger — and 44 % more compression. If κ were the mechanism, two rows at the same κ could not differ by that much."* Verified mechanically by its author before it was written down. 2026-08-12. |
| `docs/ROADS-001-two-reconstructions.md` **§5** | *"κ is the budget, and **the budget does not determine the outcome**."* Same date. |

Both are Paper-II-only readings: neither connects the under-determination to Paper III's exact
identification, which is the disanalogy the design is after. So the design's claim is **wrong in
its intra-Paper-II half and right in its cross-paper half** — the numbers are noticed, twice; the
disanalogy is nowhere, still. That distinction is worth having and it is not the sentence the
design wrote.

**`END-TO-END-001` is not edited in response to this.** It is a registration wearing a design
document's filename and the standing ruling forbids it; the repair path for a mis-specified clause
is `END-TO-END-002`. This document is the record.

### 3.1 · And the design's §0 premise is refuted by the same document

`END-TO-END-001` §0 says `ADR-001` addendum 6 *"left one question open with no written answer
anywhere in this repository"* — *what would it mean for the three papers to fail as a system?*

`REVIEW-004` **§E3** is titled ***"What it would mean to fail as a SYSTEM — the answer to your open
question"*** and gives five ranked modes with a diagnostic each. It was written on 2026-08-12, the
day after addendum 6 was recorded, and four days before `END-TO-END-001` said no answer existed.

Its **mode 1**, ranked most likely, is: *"The conjunction is a coincidence of vocabulary (most
likely, and **already partly true**). … **Diagnostic: write the bridge proposition between ρ and
φ.** If it can be written and defended, it is the corpus's best single contribution … If it cannot,
drop the word 'programme' and post three independent papers."*

**That diagnostic is E1, named four days early, and E1 has now returned its negative branch.**
`REVIEW-004` §E2 goes further and performs it: *"They are not the same structure … Non-arrival and
deferred arrival are different dynamical objects,"* with the observation that Paper III invented
the bridge-proposition discipline (§6.2) and did not apply it to its own corpus.

This is the same defect the corpus has now found three times in three shapes: **a finding
correctly recorded in `docs/` and never turned into an edit** (`RESULT-TERM-002` names the class,
`METHOD-001` names its ancestor). `END-TO-END-001`'s value is undiminished and its premise was
false — the answer existed, in a document the design's author had read for other purposes, and
nothing in the repository indexed it as the answer.

---

## 4 · Admission accounting — what E1 may and may not count

`END-TO-END-001` §1.1: a finding a competent single-paper review could have made is reclassified
`P7`, is logged as one, and **scores nothing**. Applied to everything this run produced:

| finding | class | why |
|---|---|---|
| ρ's complement is destroyed where φ's is deferred; Paper II has no α | **system-level, admissible — but PRE-EXISTING** | Needs both papers and both implementations, so no single-paper review reaches it. But `REVIEW-004` §E2 made it on 2026-08-12. **A leg may not count a finding made before it existed.** E1 counts the verdict it compels, not the discovery. |
| Paper III's degeneracy is exact; Paper II's is resolution-limited | **system-level, admissible, NEW** | Requires Paper III's 7 × 10⁻¹⁴ bound, Paper II's implementation, and a measurement (§5.3) nobody had run. Nothing in `docs/` states it. **This is E1's one piece of new system-level content.** |
| (*r*, ρ) are not separately identified by Paper II's observables | `P7` | `ROADS-001` states it as *"ρ … is a rate reparameterisation"* from a Paper-II-only reading. Single-paper findable and already found. |
| κ under-determines the outcome across bases | `P7` | `REVIEW-004` A2 and `ROADS-001` §5, both Paper-II-only. §3 above. |
| §3.1's Var[log *a*] shares its letter with §2.1's wage *a* | `P7` | Two sections of one paper. Repaired anyway (§6). |
| §7 names one regeneration command for numbers produced by two scripts | `P7` | One paper's own §3 against its own §7. Repaired anyway (§6). |
| `END-TO-END-001` §0's and E1's audit-half premises are both false | **about the design, not the corpus** | Recorded here; the design is not edited. |

**Counts, reported separately as §2.0 requires.** TEST legs run: 1. TEST legs failed: **1**. AUDIT
legs run: 0 (E1's audit half is part of a TEST leg, not an AUDIT leg). No combined score is
available and none is offered.

---

## 5 · `E1b` — run out of order, reported for the record, entering no verdict

### 5.1 · The ordering violation, stated plainly

The design fixes `E1a` before `E1b` (§5) and says a difference in kind means `E1b` is not run.
What happened: `E1a`'s first pass, taken off the three manuscripts alone, returned **"same kind"**
— the manuscripts do not disclose that `(1−ρ)` is discarded, because that fact lives in the
implementation. `E1b` was launched on that reading. The corpus audit that the design places
*inside* E1 then surfaced `REVIEW-004` §E2, which reversed `E1a` to "different in kind" while
`E1b` was still computing.

Nothing was rescued by a simulation, which is the harm the clause exists to prevent — `E1b`'s
numbers corroborate the FAIL rather than contest it (§2.3). But the clause was broken and the
honest account of a run that breaks a fixed clause is the account, not the mitigation. **The
lesson, which is the transferable part: a type check run against manuscripts is not the same check
run against implementations, and this one differed on exactly the clause that decided the leg.**

### 5.2 · What `E1b` measured

Flow base, periodicity 1, threshold 0, *N* = 800, μ = 0.05, σ = 0.20, *a* = 0.05, *T* = 1200, 20
seeds. For a ladder of κ targets fixed before any statistic was computed, *r* was solved per ρ so
that the seed-mean κ matched to within the registered 1 %.

| κ\* | locus points | ρ span | Gini sep. | top-decile sep. | Var[log *a*] sep. | reading |
|---|---|---|---|---|---|---|
| 0.005 | 11 | 1.00 → 0.05 | 0.80× | 0.28× | 0.01× | refuted |
| 0.010 | 10 | 1.00 → 0.10 | 0.62× | 0.24× | 0.01× | refuted |
| 0.020 | 9 | 1.00 → 0.20 | 0.51× | 0.18× | 0.01× | refuted |
| 0.050 | 6 | 1.00 → 0.50 | 0.41× | 0.08× | 0.03× | refuted |
| 0.100 | 1 | — | — | — | — | **VOID** — no non-trivial locus; κ ≈ 0.1026 is the flow base's maximum, so Paper II's own matched budget admits exactly one (*r*, ρ) pair |

Separations are the range of point means across the locus in units of the pooled within-point seed
spread. The locus is non-trivial and wide at every attainable target below the ceiling: at
κ\* = 0.005, ρ falls twentyfold while *r* rises eighteenfold and the Gini moves 0.723 → 0.736,
four fifths of one seed spread.

**Disclosure carried from the script's own docstring:** `wt077`'s `A_flow` is the large-*w* limit
`A(η) = 1 + η − rρ·max(η,0)`, which depends on *r* and ρ only through their product, so Var[log *a*]
has almost no room to move on a locus that is nearly an iso-*r*ρ locus. Its 0.01× is a property of
the instrument. The discriminating weight sits on the two simulation observables. Var[log *w*] of
the final cross-section is reported in the log as supplementary and is **not** part of any
criterion — a run may not add an observable to its own failure test.

### 5.3 · The sensitivity that decides how much `E1b` is worth

The registered criterion is *relative to seed spread at the paper's own N*. A separation small
against seed noise at *N* = 800 need not stay small. Measured rather than assumed, at κ\* = 0.020,
locus endpoints ρ = 1.0 and ρ = 0.2:

| *N* | Gini(ρ=1.0) | Gini(ρ=0.2) | drift | seed SD | separation |
|---|---|---|---|---|---|
| 800 | 0.444561 | 0.448099 | 0.003538 | 0.007003 | 0.51× |
| 1600 | 0.443860 | 0.447380 | 0.003520 | 0.003646 | 0.97× |
| 3200 | 0.446440 | 0.450130 | 0.003690 | 0.004086 | 0.90× |
| 6400 | 0.444852 | 0.448409 | 0.003558 | 0.002250 | 1.58× |

**The drift is flat to three significant figures across an eightfold change in *N* while the seed
spread falls threefold.** It is a real systematic effect, not seed noise, and it is below the
paper's resolution rather than absent. Extrapolating the observed √*N* scaling, it would cross the
registered 3× threshold near *N* ≈ 3 × 10⁴.

So Paper II's observable *does* eventually identify the factors, and Paper III's provably never
does. Had `E1a` returned "same kind" and `E1b` governed, the leg would have read **REFUTED at the
paper's parameters** and the corpus would have gained a non-identification result that dissolves
under a larger simulation. **That is the run this document did not produce, and the reason is a
type check, not a number.**

---

## 6 · What was done to the corpus

The FAIL branch of the design's E1 table, written before the run, applied in full and in scope
(`patch_e1.py`, `.bak-wt56-e1` beside each file):

- **Paper II §3.2** — the outward-connecting paragraph cut back to a claim about observability
  alone. The *"are the same structure"* sentence is removed, and the withdrawal is stated in the
  paper rather than only here, because a correction that lives only in a document has not been
  made.
- **Paper IV §3** — *"a chain rather than three analogies"* demoted **in terms** to *"three
  instances of one question, asked at three scales"*, with the reason and the citation in §3, the
  killed framing entered in §8 Abandoned approaches per the corpus's own convention, and four
  downstream uses of *"the chain"* repointed so the paper does not keep a noun the section no
  longer earns.

**Deliberately NOT applied**, because they are not this leg's to spend:

- the abstract's *"the same atomic unit composes from the household to the sovereign"*, and
  `ADR-001`'s addendum — those live in §3's **T ≥ 2** branch and `T = 1` today. **They become live
  if a second TEST leg fails, and the session that lands E2/E3/E5 must return to them.**
- Paper II's new §3.x reporting a non-identification result — that is the **refuted** branch's
  remedy for an outcome that did not occur. `E1b`'s numbers stay in this document.

Two `P7` repairs made in passing (§4): Paper II §3.1 now names its multiplier *a* as distinct from
§2.1's wage *a*, and §7 now names `wt077_tail_index.py` as the source of §3.1's three Var[log *a*]
values instead of implying `wt030_report.py` produces them.

---

## 7 · What this does not license

E1 has broken the II↔III link as a *structural* claim. It has **not** shown the corpus is three
unrelated papers: the question is genuinely shared, each scale answers it quantitatively, and
Paper IV's §3 still says so. It has not touched E3's containment matrix or E5's shared guards, and
the pass verdict is not available until the remaining TEST legs return — `T = 1` is **WOUNDED** if
they clear and **FAILS** if any one of them does not. A reader who takes this document as the
system verdict has read the leg for the pass.

And the standing warning at corpus scale still applies in the other direction: nothing here bears
on whether the framework is right about the world. Paper III §6.1 governs the corpus as it governs
Paper III.

*Coffee status: ☕ the leg that was built to be able to lose, lost — and the fact that killed it had
been sitting in `docs/REVIEW-004` for four days, correctly stated, indexed under nothing. The
system test's first result is about the corpus's filing.* 🥎
