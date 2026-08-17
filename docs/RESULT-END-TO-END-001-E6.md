# RESULT · END-TO-END-001 · E6 — THE CROSS-PAPER CONTRADICTION **[AUDIT]**
*wealthTensor-61 · 2026-08-17 · run against `docs/END-TO-END-001.md` §E6 (the leg is FIXED and was
not edited in response to this result). **This is the last unrun leg of the pass.***

## VERDICT
- **Verdict: E6 — FAILURE REFUTED**, on the leg's own clause: *every shared fact agreeing in truth
  value and modality across every paper that states it.* **`E6` is an AUDIT leg: `T` remains 2 and
  THE SYSTEM FAILS still stands, on `E1` and `E3`.**

> **Six candidate contradictions were built and every one of them died.** Three blind single-paper
> extractions produced the shared-fact inventory; a completeness critic was run against the
> inventory to find what the extractions missed; every candidate was put to a dedicated adversarial
> refuter with a mandate to kill it. **Six refuters, six REFUTED.** Two of the six were inherited
> from `-60`'s handoff and are not this run's discoveries; both are named as such in §5.
>
> **TEST legs run 4 · FAILED 2 · UNDECIDED 1 · REFUTED 1**
> **AUDIT legs run 2 · FAILED 0 · REFUTED 2 — the pass is complete and `P11g` is now writable.**
>
> ### The leg is refuted and the run's best finding was an artefact of the pass itself. Read §2.
> The strongest candidate this run built — the model's recognition rate α carried as *settled* in
> Paper IV and *unbridged* in Paper III — rested on a clause of Paper IV **that did not exist until
> `-59` wrote it, four hours before this session started.** The `.bak` chain says so to the byte.
> **`E6`'s honest result is not "the corpus is clean." It is "the corpus is clean, and the pass came
> within one refuter of citing itself as evidence against the corpus."**

---

## 1 · What was under test, and how this run was constrained

E6's check, quoted whole:

> *"Enumerate the facts the papers **share** — the framework's parameters, the registered tests and
> their status, the propositions P1–P3, the corpus's own results as cited across volumes. For each,
> extract every paper's statement of it and compare truth value and modality (*asserted* /
> *conditional* / *open* / *rejected*)."*
> **FAILURE is shown by:** any shared fact whose modality differs across papers in a way that
> changes what a reader may conclude — most sharply, a fact one paper reports as **settled** and
> another carries as **pending**.
> **FAILURE IS REFUTED BY:** every shared fact agreeing in truth value and modality across every
> paper that states it.

**The corpus is Papers II, III and IV** (§1). Paper I was excluded by scope, not overlooked; §6
records what that costs.

**The worked example is excluded from its own run** and was not re-found: diagonality / the Hadamard
form, Paper III §9 limitation 9 against Paper IV §3 / §4.4.3 / §9.2. `-55` repaired it in the commit
after the registration and the repaired text is what is in Paper IV today. Every candidate below was
checked against it.

**Method — and the method is the reason the verdict is worth anything.**
1. **Three blind extractions.** One agent per paper, each forbidden to read the other two papers,
   any `RESULT-*`, any `REVIEW-*`, any `.bak`. Each returned a table of that paper's statements of
   shared facts with a modality assigned from E6's own vocabulary, plus an intra-paper
   double-modality list and an abstract-vs-body list. **Blindness is what makes the comparison a
   measurement rather than a search for a conclusion already chosen.**
2. **Four candidates built from the join**, then **one completeness critic** run against the
   inventory with a single instruction — *what shared fact has this run not checked?* — which
   produced a fifth candidate stronger than any of the four.
3. **Six adversarial refuters**, one per candidate, each told to default to REFUTED, each required
   to re-verify every quote against the bytes and to diff the passage against the `.bak` chain.
4. **Round two aimed at round one's scaffolding**, per `-60`'s tell. It cost this run one of its own
   published grounds (§3.2) and caught the fabricated quote in §3.1.

---

## 2 · §2 IS THE LEG · The run's best candidate was written by the pass, four hours earlier

The candidate the completeness critic found, and the only one with E6's *sharpest* registered shape
— **settled in one volume, pending in another**:

> Paper IV §3 (*Household*), the **only** occurrence of `0.05` in the entire paper: *"**Paper III §2
> is that holding**, before anything is summed: its physical layer degrades at an effective 0.02 per
> period and its claim layer recognises at α = 0.05, and §3.1 reports what the distance between
> those two rates costs. The household scale's quantitative answer is Paper III's."*
> Paper IV contains **zero** occurrences of `0.408`, `hazard`, `swept`, `calibrat*`, `Weibull`.
>
> Paper III §9 limitation 4: *"**φ and θ are not measured; they are swept** … **The bridge from that
> rate to the model's α** is the one §6.2 requires of every registration, and **this paper has not
> written it.**"* Paper III §4.4: *"**α̂ = 0.408 per year** … the calibration used here is **low by
> an order of magnitude**."*

It has the shape. It is cross-paper. It survived the §1.1 admissibility attack — the refuter tried
and reported the attack **did not land**. And it is dead, on a fact no amount of reading the two
papers side by side would ever have surfaced:

| snapshot | mtime | Paper IV §3 *Household* |
|---|---|---|
| `paper-IV.md.bak-wt54-liftoff` | 16:32:34 | ends at *"…and they are different numbers."* **No numbers. No Paper III pointer.** |
| `paper-IV.md.bak-wt56-e1` | 17:25:22 | unchanged |
| `paper-IV.md.bak-wt57-e3` | 18:19:08 | unchanged |
| `paper-IV.md.bak-wt59-e2` | **19:58:06** | **still unchanged** |
| `paper-IV.md` (live) | 21:27:20 | contains the entire attacked clause |

**Every clause of the candidate was inserted by `wealthTensor-59` between 19:58 and 21:27 on the
16th**, as a `P7` bug-spray repair announced in `RESULT-END-TO-END-001-E2.md` §6.1 — *"It now names
**Paper III §2's calibration** and §3.1's result"* — where the repairer characterises the inserted
number, in advance and in his own words, as **the calibration**, which is the exact reading that
kills the contradiction. `E2` §6 also carries the `-58` precedent that binds here: **the session
which rewrites a passage may not grade it.**

**This is the handoff's third DO-NOT, and it very nearly took a verdict.** *"DO NOT CITE THIS PASS'S
OWN REPAIRS AS CORPUS EVIDENCE. Diff against the `.bak` chain first."* The run had that sentence in
front of it, ran five candidates through the `.bak` check without incident, and then built its
strongest finding on a four-hour-old repair anyway — because **the completeness critic found this
one, and a candidate that arrives as the answer to "what did you miss?" arrives wearing the
authority of a gap rather than of a claim.** The `.bak` diff was in the refuter's mandate and
nowhere else. If it had been left out of that prompt, this document would be reporting a FAILURE.

**And the deeper point, which is the leg's, not the run's:** a corpus that is being repaired *while
being audited* has a moving referent. Five of the six candidates were byte-identical to their
pre-registration snapshots and could be compared honestly. **The sixth was not, and nothing about
reading it disclosed that.** Only the file's mtime did.

---

## 3 · The six candidates, and what killed each

### 3.1 · The four built from the blind join

**C1 · The propositions' domains — REFUTED.** Paper III §A.1.2 states P1/P2/P3 each with an explicit
*Domain* clause (P1: *"Silent on purely contractual objects whose referent is another claim"*);
Paper IV §2.1, headed *"The three propositions, cited not restated"*, restates all three with no
domain, and `domain` occurs **exactly once** in Paper IV — in the sentence saying Paper III states
them *"with their domains."*
**Killed on the bytes.** The run's sharpest sub-claim — that Paper IV's P2 (*"degrades whether or
not the degradation is recorded"*) is a different proposition from Paper III's (*"absent
maintenance. No store is inert"*) — is **false**: Paper IV's wording is Paper III's **own**, at
Paper III's abstract and §1 (*"a physical component degrades whether or not anyone records the
degradation"*). The three-strengths-of-P2 tension is therefore **entirely inside Paper III** →
single-paper → `P7`. What is left of C1 — Paper IV promising domains it does not carry — is a
completeness defect a Paper IV-only referee finds unaided, which §1.1 reclassifies as `P7`, and on
which no Paper IV claim depends (§4.4 bounds the object by **extensivity**, independently stated).

**C2 · "firm-level panels of both are public and free" — REFUTED, and not this run's.** Paper IV
§1.1's third datable lapse against Paper III §9 limitation 5 (*"The SDG series is a **national
aggregate** … the model's coupling is a **firm-level** ratio"*) and §4.5 (*"ΔE … **which no filing
reports**"*).
**Killed by §1.1.** Paper IV denies it in **four** of its own places — the abstract (*"largely
unmeasured"*), §4.3 (*"very largely not being measured"*), §4.4 item 1 (*"A state that composes is
not thereby a state anyone can observe"*), §9 item 1 (*"the state is largely unobserved"*). A
one-paper referee finds it without opening Paper III. `P7`, not E6. **Prior art:** `E2`'s blind pass,
Builder B #5, 2026-08-16 21:00, with all four contradicting sites already named.

**C3 · Paper IV recruiting Paper II to a "sovereign scale" — REFUTED.** Measured: `paper-II.md`
contains **zero** occurrences of `household`, `sovereign`, `compos*`, `extensive`, `fold`, `atomic`,
`claim component`, `physical component`, `measuring layer`.
**Killed three ways.** (i) *Assertion + silence is not assertion + denial*, and E6's REFUTED clause
is scoped to *"every paper that **states** it."* (ii) Paper IV's *"a fold over household-scale
liabilities"* is **true** on Paper II's bytes — κ is (sum of per-holder liabilities)/(aggregate
wealth). (iii) Paper IV names no institution acting; *"sovereign"* is a scale label, and Paper II
§1 licenses institutions *"as a **coordinate**"*. **Prior art:** `E2`'s blind pass, Builder A #16
and Builder B #1, both ranked first by their builders, **already put to two refuters and already
REFUTED** (`RESULT-…-E2.md` §3.2).
**And the run got a quote wrong here.** See §3.2.

**C4 · SDG 7.3.1 / Λ⁻¹, hedged where produced and flat where used — REFUTED, and not this run's.**
Paper IV §7's *"the strongest available evidence that the quantity is not an invention of the
framework"* against Paper III §A.2.2's *"It is emphatically **not** that SDG 7.3.1 measures Λ⁻¹."*
**Killed on identity of proposition.** Paper III §A.2.2 states, in terms, what survives its own
qualification: *"currency-per-energy is not an exotic dimension and **not this author's coinage**"*
— which is Paper IV's proposition in different words, and §9 limitation 5 licenses it explicitly:
*"The correspondence licenses 'this dimension is one institutions already report'."* Paper IV never
asserts the forbidden half. **And the flat form is in Paper III too**, as §A.2.2's own section
heading: *"**Λ⁻¹ is an indicator the United Nations already publishes**."* The finding's structure —
hedged where produced — is false at the producing volume. **Prior art:** `E2`'s blind pass Builder B
#6, adjudicated and refuted at `RESULT-…-E2.md` §3.3 the same evening; nominated for E6 by name in
`-60`'s handoff, framing phrase and all.

### 3.2 · One published ground of this run's own, struck by round two

- **STRUCK · the Paper IV §3 quotation *"…what happens when a **sovereign assesses** that sum."***
  **That string does not exist.** The bytes read *"…what happens when **a levy is assessed** on that
  sum"* — **passive, with no agent** — in the live file and in all four `.bak`s. The run paraphrased
  an agentless passive into an agent, and the manufactured agent was the entire basis of C3's
  "institutional claim" limb. **This is the registration's own seventh and eighth defect, committed
  by the session auditing it**: `-59` found the registration quoting the corpus without a trailing
  scope clause, `-60` found it again one leg over, and `-61` did it in a refuter prompt. The prompt
  did carry *"VERIFY THIS QUOTE"* beside it, which is why it was caught — **but a flagged
  fabrication is still a fabrication, and the flag is not a substitute for the grep.**
- **And a scaffolding check of this run's own returned a false negative.** Auditing round one, the
  run grepped Paper IV for `A rate is not extensive`, got nothing, and briefly recorded the
  refuter's citation as fabricated. It is not — the phrase **wraps a line boundary** (`A rate is
  not` / `extensive.`) and a line-oriented grep cannot see it. **A grep for a phrase that crosses a
  newline returns zero and reads exactly like a fabrication.** The run nearly published that
  accusation against its own instrument.

---

## 4 · What was checked and found to AGREE — the part that makes REFUTED honest rather than lazy

A REFUTED verdict on a universal clause is worth nothing unless the enumeration is exhibited. These
shared facts were extracted from every paper that states them and **agree in truth value and
modality**:

1. **The `E1` withdrawal (ρ ≠ φ)** — *rejected* in all three volumes, same citation. Paper II §3.2
   (*"that identification does not hold … Deferred arrival and non-arrival are different
   operators"*); Paper III §A.1.3 (*"That identification is withdrawn … a levy has no parameter that
   plays α's part"*); Paper IV §3 and §8 (*"they are not"*).
2. **The ρ = 0 inertness result** — Paper II §3.2 = Paper III §A.1.3 = Paper IV §3, and each carries
   the **surviving** *"regardless of rate"* form rather than the one Paper II §3.1 falsified. This
   was checked specifically because it is the trap.
3. **κ's definition** — Paper II abstract/§3.1 and Paper IV §3, same object, same modality.
4. **Registered-test status across volumes.** Every registration token was enumerated in all three
   files. Paper II names **none**; Paper III names PRE-001, PRE-002, REG-003…REG-008; Paper IV names
   REG-001, REG-003, REG-013. **`REG-003` is the only registration named in two papers**, both
   report it as registered-before-instrument, run, and rejecting independence, same direction, same
   numbers — and it is the excluded worked example. **There is no registered test that one paper
   closes and another leaves open.** That is the leg's sharpest shape, searched for directly, absent.
5. **The Hadamard recursion** — Paper IV §3's form is character-consistent with Paper III §4.1,
   including the claim that the elementwise form is not notation.
6. **φ's non-identifiability** — Paper IV nowhere treats φ as separately determinate; it carries the
   product (§3, §4.4 item 2).
7. **Paper II's falsified prediction** — Paper IV states the *surviving* narrow claim, not the
   falsified *"regardless of rate"* form.
8. **"No new computation"** — Paper IV §9.3 / §10 consistent with II's and III's provenance
   statements.

---

## 5 · Provenance, stated because the leg is cheap to overclaim

**Two of the six candidates were handed to this run by name.** `-60`'s handoff §3 nominates Paper IV
§1.1's *"public and free"* (*"explicitly `E6`'s shape and has been waiting three sessions"*) and the
SDG 7.3.1 pair (*"Hedged where produced, flat where used — which is `E6`'s exact question"*). **This
run did not discover either.** It ran them, and both died — one to §1.1, one to identity of
proposition. A third, C3, was found first by `E2`'s blind pass and already refuted there.

**What is this run's own:** C1 (the propositions' domains), the α candidate of §2 and the `.bak`
measurement that killed it, the §6 finding below, and the agreement inventory of §4. **Of those, C1
reclassifies to `P7` and the α candidate is void.** The run's net contribution to the corpus's
knowledge is §2's tell and §6's defect — which is a smaller haul than six candidates suggests, and
saying so is the point of this section.

---

## 6 · A defect found while running the leg, and it is not E6's — `RESULT-…-E3.md` certifies a repair it did not make

`RESULT-END-TO-END-001-E3.md` §6.1 item 1 reports `E3` applying `§3`'s `T ≥ 2` remedy, and states,
in quotation marks, what the repaired text now says:

> *"**APPLIED HERE.** The abstract now reads *"the same atomic **state** composes by addition
> wherever it is summed"*…"*

**That string occurs nowhere in the corpus.** `grep -rn "wherever it is summed"` over all of `docs/`
returns exactly one hit: that line of `-E3` itself. What the abstract actually reads, then and now:

> *"the same atomic **state** composes **from the household to the sovereign** — and states exactly
> where composition stops — sooner than an earlier draft claimed, because the corpus's end-to-end
> test found the sovereign and firm scales share **one question, not one structure**."*

Diffed against `paper-IV.md.bak-wt57-e3`, `E3`'s actual edit was `unit` → `**state**` plus the
appended *"sooner than an earlier draft claimed…"* clause. **The phrase §3's remedy names for
narrowing — *"from the household to the sovereign"* — is still there.** The substance of the
correction was appended; the narrowing the result document quotes was not performed, and the
sentence certifying it is a quotation of text that has never existed.

**Why this matters more than the wording.** `§3`'s remedy is the corpus's pre-committed response to
`THE SYSTEM FAILS`, and `P11g` reads its verdict off `§3`. A result document that certifies a
`§3` remedy as applied, in a quotation, is the artefact every later session trusts — and `E2`
subsequently recorded Paper IV's **title** (*"one atomic unit from the household to the sovereign"*)
as still open and *"Jason-sized"*, without anyone noticing that the abstract's version of the same
phrase was supposed to have been narrowed already. **This is `-60`'s lesson in a new costume: a
claim that quotes a repair borrows the authority of a diff without having run one.**

**Classification, stated plainly:** this is **not an E6 finding** — E6 compares papers, and this
compares a result document against a paper. It is not repaired here, because a result document is a
dated record and rewriting it would destroy the evidence. **A dated correction note is appended to
`-E3` §6.1 rather than an edit to its prose**, and the residual question — whether §3's narrowing
should now be applied to the abstract and the title — is **Jason's**, because §3 item 1 names the
title and `E2` already ruled that Jason-sized.

---

## 7 · What was done to the corpus: nothing, and one correction note added to a result document

- **No manuscript was edited.** E6 returned REFUTED; there is no contradiction to repair, and E6's
  standing instruction (*"every contradiction found is repaired in the session that finds it"*) has
  no antecedent. The `P7` items surfaced in §3 are logged and **not** repaired by this leg — `P7` is
  scored separately from whoever did the work, and `E2`'s `-58` precedent binds: **the session which
  rewrites a passage may not grade it.**
- **The registration is FIXED and was not edited.** No ninth defect is claimed; §3.1's fabricated
  quote is charged to *this run*, not to the registration.
- **One dated correction note appended to `RESULT-…-E3.md` §6.1**, recording that the quoted
  abstract string does not exist and what the applied edit actually was. The prose above it is left
  intact.

---

## 8 · What this does not license

- **It does not license "the corpus is internally coherent, therefore the framework is right."**
  §3 pre-commits against exactly this: *"A corpus that survives this pass has been shown to be
  internally coherent and honestly summed. **It has not thereby been shown to be right about the
  world.**"*
- **It does not license reading `T` as improved.** `E6` is an AUDIT leg and cannot move `T` in
  either direction. `T = 2`; **THE SYSTEM FAILS**, on `E1` and `E3`.
- **It does not license a combined score.** §2.0 forbids one. TEST 4/2/1/1 and AUDIT 2/0/2 stay
  separate.
- **It does not license re-running `E6`.** `E6` IS SPENT AND ITS ANSWER IS FAILURE REFUTED. The
  stopping rule in §3 also binds: **the corpus gets exactly one first end-to-end pass, and this
  document closes it.**
- **It does not license treating the six REFUTEDs as six clean bills.** Two were prior art, one was
  void, and one was reclassified. **The corpus survived E6 on four honest comparisons and two
  inherited ones**, and a successor who reads "six candidates, six refuted" as strength has read the
  count and not the section.

---

## 0' · The tell this leg adds

**A CORPUS UNDER REPAIR HAS A MOVING REFERENT, AND ONLY THE FILESYSTEM KNOWS.** Five of six
candidates were byte-identical to their pre-registration snapshots. The sixth was written by the
pass's own previous session four hours earlier, read exactly like the other five, and was the
strongest of them. **Nothing in the prose disclosed it. `ls -la` did.** When an audit and a repair
programme run in the same week, *diff before you conclude* is not hygiene — it is the difference
between a verdict and a self-portrait.

*Corollary, cheaper and just as load-bearing:* **a candidate produced by asking "what did I miss?"
arrives with a gap's authority rather than a claim's, and gets less scrutiny for it.** The
completeness critic is the right instrument and its output is the least-audited thing in the run.
Point the `.bak` check at the critic's findings first, not last.
