# RESULT · END-TO-END-001 — THE PASS
*wealthTensor-61 · 2026-08-17 · the pass-level result for `docs/END-TO-END-001.md`. **All six legs
are run.** This document reports the verdict `§3`'s rule returns; it does not form one.*

## VERDICT
- **Verdict: THE SYSTEM FAILS** — `§3`'s rule, applied: **`T = 2`**, and `THE SYSTEM FAILS` iff
  `T ≥ 2`.

> **`T` = the count of TEST legs that FAIL = 2 (`E1`, `E3`).**
> **`A` = the count of AUDIT legs that FAIL = 0 (`E4` REFUTED, `E6` REFUTED).**
>
> **TEST legs run 4 · FAILED 2 (`E1`, `E3`) · UNDECIDED 1 (`E5`) · REFUTED 1 (`E2`)**
> **AUDIT legs run 2 · FAILED 0 · REFUTED 2 (`E4`, `E6`)**
>
> **The two counts are reported separately and no combined score exists**, per `§2.0`: *"a run may
> not report a single combined score."* A reader who wants one number has been refused it on
> purpose, and the refusal was registered before any leg ran.
>
> **The VOID branch does not apply.** `§3`: *"**VOID:** if `E1` voids **and** `E2` reports
> under-powered…"* — a conjunction. `E1` did not void; it **FAILED**, at `E1a`. The pass returned a
> verdict and it is this one.
>
> ### And `T = 2` was reached at `E3`, on 2026-08-16. Nothing after it moved the verdict.
> `E5` returned UNDECIDED and cannot raise `T`. `E2`, `E4` and `E6` returned REFUTED. **`T` can rise
> and cannot fall**, so the pass's verdict has been fixed since the third leg and the last three
> legs were run knowing they could not change it. **That is the design working, not a waste**: a
> pass that stops the moment it has its answer never learns what else is wrong, and `E4` found the
> corpus's five confirmed empirical claims precisely because it was run after the verdict was safe.

---

## 1 · The six legs, as run

| leg | class | question | verdict | when |
|---|---|---|---|---|
| **`E1`** | TEST | the shared degeneracy — is the II↔III join load-bearing or vocabulary? | **FAILED**, at `E1a` | `-56` |
| **`E2`** | TEST | the unowned claim — does the conjunction assert something no paper defends? | **FAILURE REFUTED** | `-59` |
| **`E3`** | TEST | the containment matrix — is `ADR-001`'s promise about failure true? | **FAILED** | `-57` |
| **`E4`** | AUDIT | the corpus's empirical content, stated whole | **FAILURE REFUTED** | `-60` |
| **`E5`** | TEST | the over-subscribed guard — does one test hold two claims that could come apart? | **UNDECIDED** | `-58` |
| **`E6`** | AUDIT | the cross-paper contradiction — does the corpus assert and deny the same fact in two volumes? | **FAILURE REFUTED** | `-61` |

Each leg's own document is the record; this table is an index and not a substitute. `E5`'s UNDECIDED
is a verdict about the *registration*, not about the corpus — its failure limb was a disjunction and
its refutation limb a conjunction of the same two limbs, leaving a reachable gap the corpus sat in.

---

## 2 · What `THE SYSTEM FAILS` cashes out to, and where each consequence stands

`§3` names four, pre-committed before any leg ran. **They are not negotiable after the fact** — that
is why they were written above the results rather than below them.

**1 · Paper IV loses its chain claim** and becomes *"a survey of three literatures, a measured
whitespace, and one worked instance — with §3 rewritten from a chain into three parallel instances
and the abstract's 'the same atomic unit composes from the household to the sovereign' narrowed to
the scales actually joined."*
**STATUS: applied in substance, and its certification is wrong about itself.** §3's rewrite was done
by `-56` at `28bf7c2` as `E1`'s FAIL remedy, and the abstract now carries the demotion in terms
(*"the corpus's end-to-end test found the sovereign and firm scales share **one question, not one
structure**"*). **But `RESULT-…-E3.md` §6.1 item 1 certifies the narrowing with a quotation of a
sentence that does not exist** — *"the same atomic **state** composes by addition wherever it is
summed"* occurs nowhere in the corpus, and the phrase §3 names for narrowing, *"from the household
to the sovereign"*, is **still in the abstract and still in Paper IV's title.** `-61` measured this
against `paper-IV.md.bak-wt57-e3` and recorded it at `RESULT-…-E6.md` §6, with a dated correction
note appended to `-E3`. **The remaining decision — narrow the abstract's leading clause and the
title, or ratify the appended form as sufficient — is Jason's**, and `E2` already ruled the title
Jason-sized.

**2 · Papers II and III are unaffected and ship as independent works.**
**STATUS: cashed, and `E3` forced one correction to make it true** — Paper III §A.1.3's companion
aside was repaired in that leg. This is `ADR-001` §Consequences' containment promise being *paid*,
and the decomposition decision retrospectively vindicated: a monolith would have taken all three
down.

**3 · `ADR-001` gets a dated addendum** recording that the fourth claim did not survive its own
first end-to-end test.
**STATUS: applied at `-57`.**

**4 · `P13` renders three works, not one stack.**
**STATUS: decided, not yet built.** `P13` is last by standing ruling. Its subject matter is now
fixed by this verdict and is not a design choice the deliverable session may reopen.

---

## 3 · What the pass established, and it is not what the verdict alone suggests

**The corpus failed as a system and is in better shape than when the pass started.** Both halves are
true and the second is not consolation.

- **`E1`** established that the II↔III join is **vocabulary at the sovereign scale**: ρ and φ are
  not the same kind of object. The identification was withdrawn from **three** papers, each in its
  own voice, and each names the check that killed it.
- **`E3`** established that `ADR-001`'s containment promise was **one sentence short of true** and
  made it true.
- **`E2`** put two independent adversarial builders on the corpus and found that the conjunction's
  strongest unowned belief **had a witness after all** — Paper III §2–§3.1.
- **`E4`** established that the corpus has **five confirmed claims about the world**, all Paper III,
  all on SEC EDGAR — and that **every one of them runs against the model**: the paper's own
  rectangle, its own calibration, its own constant hazard, its own diagonality assumption, its own
  fallback route. It also established that **no document in the corpus states the corpus-level
  position**, and that Paper III §6.1's summary of it has been stale since 12 August. **That silence
  is the pass's one unrepaired substantive finding.**
- **`E6`** enumerated the shared facts across all three volumes from three blind extractions and
  found **no shared fact carried at different modalities** — no registered test that one paper closes
  and another leaves open, which is the sharpest shape the leg registered. Six candidates, six
  refuted, and the strongest of them turned out to rest on **a clause the pass itself had written
  four hours earlier.**
- **`E5`** established that the *registration* can leave a gap a corpus sits in, and that saying so
  is worth more than forcing a verdict.

**What the pass did NOT establish, committed in `§3` before it ran and repeated here because it is
the sentence most likely to be dropped:** *"A corpus that survives this pass has been shown to be
internally coherent and honestly summed. **It has not thereby been shown to be right about the
world.**"* And it did not survive. Paper III §6.1 governs the corpus as it governs Paper III — with
the correction `E4` supplies: the framework has **no confirmed empirical claim in its own favour**,
and five against itself.

---

## 4 · The registration graded against itself

`END-TO-END-001` designed six legs, ran none, and is **0-for-8 on its own prose** — eight defects,
each found by the leg it governed, each recorded in that leg's document, none repaired, because
**the registration is FIXED and may not be edited in response to a result.** Two of the eight are
the same species: quoting the corpus without a trailing scope clause (`-59` at `§4.3`, `-60` at
`§E6`). Two candidate ninths were **rejected on the record** — one by `-60`, one by `-61` — because
a defect tally that accepts every candidate is worth nothing.

**The registration's design defects, routed to `END-TO-END-002` and not resolved here:**
- `E5`'s clause pair — failure limb a disjunction, refutation limb a conjunction of the same limbs.
- `E4`'s two reachable gaps — the *"in terms"* strictness gap and the *"with the claims named"*
  conjunct gap.
- `E4`'s remedy stated **unconditionally**, unlike every other leg's, and therefore not applicable.
- **`E6` declares no UNDECIDED region**, in common with `E4` and `E5`, though `§0'` promises one
  *"where one applies"*. Three of six legs, same omission.

**The stopping rule holds.** `§3`: *"The corpus gets **exactly one first end-to-end pass**. This is
it."* **This document closes it.** A second pass runs only under a new registration that says what
changed and why, **and may not cite this pass's numbers as support for its own design.**

---

## 5 · What this document does not license

- **It does not license re-running any leg.** `E1`, `E2`, `E3`, `E4`, `E5`, `E6` are all SPENT.
- **It does not license a combined score**, now or in `P13`.
- **It does not license reading `A = 0` as "the audits were clean."** `E4` returned REFUTED **and
  left its substantive target undiagnosed** — the corpus is still silent about its own empirical
  sum, and the silence now conceals an understatement rather than a zero. `E6` returned REFUTED and
  its own §2 says the run came within one refuter of citing the pass to itself. **An AUDIT leg's
  REFUTED is not a clean bill; it is the absence of the specific defect the leg named.**
- **It does not license `P13` before its own preconditions.** `P13` is last, and the verdict fixes
  its subject matter without discharging its checklist.
- **It does not license closing `P11`.** `P11` is `PENDING-HUMAN` and stays there: the pass is run
  and recorded, and whether the corpus is *done* being audited is Jason's call, not a row's.
