# RESULT — END-TO-END-001, leg E2 · THE UNOWNED CLAIM

*`wealthTensor-59` · 2026-08-16 · run blind, on the protocol in `RESULT-END-TO-END-001-E5.md` §6.
The blind pass is a separate artefact committed **before** this session had the candidate:
`docs/RESULT-END-TO-END-001-E2-blind-pass.md` at `53ddda7`, whose parent `72ea97f` contains no
reading of `END-TO-END-001` lines 205–240. This document was written after.*

**Where the reading stopped, and when.** The registration was never opened whole. It was cut on
darwin — `sed -n "1,204p"` and `sed -n "241,505p"`, sha256 `ac2cf1301a50` and `7b9758a883c7` — and
only the two slices were transferred. Line 204 is blank; line 241 is `### E3`. **Lines 205–240 were
never read, never transferred and never in this session's context until 20:59Z, after `53ddda7` was
pushed.** `-58` preserved the leg by not scrolling past a heading; this run preserved it by not
having the bytes. The second is cheaper and does not depend on anyone's self-control at the moment
the heading appears.

---

- **Verdict: E2 — FAILURE REFUTED.** Every sentence the blind pass extracted traces to a paper, a
  section, and either a result or a disclaimer. **`T` remains 2. THE SYSTEM FAILS still stands, on
  `E1` and `E3`.** TEST legs run 4 · FAILED 2 · UNDECIDED 1 · REFUTED 1. AUDIT legs run 0. No
  combined score exists and none is offered.

---

## 0 · The leg in one line, and the part that matters more than the verdict

**THIS IS THE FIRST LEG OF THE PASS THE CORPUS HAS WON, AND IT WON IT AGAINST THIS RUN'S BEST
EFFORT.** The run built a failure, had it built again independently, put five refuters on it in two
rounds, and **lost every round** — the second time on a witness the run had asserted did not exist
and which is sitting in Paper III §2 with numbers in it. The designer's own pre-registered candidate
does not fail his own leg either, and for a reason he could have checked: **`END-TO-END-001` quotes
the candidate with its trailing scope clause cut off.** That is the first time the registration has
been wrong about the *corpus's* prose rather than about its own, and it is the exact error this
project wrote into its `DO NOT` list four days ago.

---

## 1 · What was run

Quotation only. No code against `src/`, no seeds, no new numbers. One `sed` cut, two blind builders,
five refuters, and a hand check of every fact either builder or any refuter relied on.

### 1.1 · The blind pass — two builders, deliberately given different jobs

`-58`'s standing tell is that **two independent builds which agree have checked the evidence and not
the frame.** So the two builders here were not given the same taxonomy. Neither knew of the other,
neither saw the registration, neither was given a direction.

- **Builder A — the reader.** E2's check, run as written: read only the six abstract-and-contributions
  texts, write in plain sentences what a competent economist would now believe, then return to the
  full text and assign, per belief, which paper *states* it and which paper *supports* it. Returned
  **17 beliefs**, 3 classed UNOWNED.
- **Builder B — the referee.** Given all three papers at once and asked for beliefs **no paper takes
  responsibility for**, told a false positive is worse than a miss. Returned **11 ranked ownership
  breaks** and six checked-and-cleared near-misses.

Both lists are in the blind-pass artefact, unmerged, exactly as pre-committed.

### 1.2 · Then the refuters, before any of it was written up

`-58`'s order — **build → build independently → REFUTE → write** — earned its keep twice in one
afternoon. Round one aimed three refuters at the run's first reading; all three returned REFUTED.
Round two aimed two more at the finding round one left standing; both returned REFUTED. Nothing in
§3 is a claim that has not been attacked by an agent whose instruction was to kill it.

---

## 2 · The power check, and the finding that it cannot fail

`END-TO-END-001` §5 fixes *"E2's blind-first ordering and **its power check**."* The candidate:

> Paper IV §4.3: *"the extensive state … **does** survive the sum, and it is very largely not being
> measured."* … *"If the blind pass does not surface this sentence, the extraction lacked the power
> to find one, and **the leg is reported as under-powered rather than as passed**."*

**Scored three ways, as pre-committed, and the union is not the headline:**

| | found the candidate? |
|---|---|
| **Builder A** | **YES** — belief #13, and it reached the designer's own reasoning independently: *"'largely not being measured' is measured nowhere, in a paper stating 'this paper contributes no new computation'"* |
| **Builder B** | **NO.** None of B's eleven is the measurement-practice claim. B's #5 is an adjacent but different defect — IV §1.1's *"firm-level panels of both are public and free"* against IV §9.1 and III §9.5 |
| **either** | YES |

**So the leg is not under-powered, and the under-powered branch is spent.** But the check is worth
less than it looks, and this is a finding rather than an aside:

> **`E2`'s POWER CHECK CANNOT FAIL, BECAUSE ITS TARGET IS INSIDE ITS OWN INPUT.** The check mandates
> that the blind pass read *"the three abstracts and the three contributions lists."* Paper IV's
> **abstract** carries the candidate — *"the half that does, the physical stock and the claim
> recorded against it, **is largely unmeasured**"* — and **contribution 2** carries it again, with the
> section pointer attached: *"**The consequence, which is the corpus's thesis in one sentence**
> (§4.3): aggregation destroys the behavioural information macroeconomics believes it is measuring,
> and preserves the thermodynamic structure **nobody is looking at**."* The sentence, its address and
> the absence of an owning result are all handed to the instrument before it starts. A calibration
> whose standard is printed on the instrument's own input measures nothing about the instrument.

That is reported, not repaired: `END-TO-END-001` is fixed and `END-TO-END-002` is the repair path.

---

## 3 · The verdict, and the two readings that died getting to it

### 3.1 · The claim the run built first, and why it was wrong

The run's first reading was that **E2 returns UNDECIDED on the registration**, on the `E5` precedent:
that the FAILURE clause's limb (b) (*"not stated as a claim in any single paper"*) and the REFUTED
clause (*"tracing to a paper, a section, and either a result or a disclaimer"*) are not complements,
that the designer's candidate sits in the gap between them because Paper IV §4.3 **states** it while
naming no result, and that E2 declares no UNDECIDED region.

**Three refuters killed it, and the shortest kill is the right one.** `-58` lost a leg by looking for
the shape the previous leg had; **`-59` looked for it a leg later.** `E5`'s clauses genuinely were
non-complementary and its evidence genuinely fell between them. Finding the same shape in `E2` was a
prior, not an observation, and the observation that was actually available is in §3.3: **limb (c)
fails, so the interpretive question never had to be answered.**

### 3.2 · The claim the run built second, and why that was wrong too

With the candidate disposed of, the strongest surviving belief was the one **both builders
independently ranked first** — Builder A's #16 and Builder B's #1:

> *the same atomic unit appears at three scales, household included, and the answer at each scale is
> a quantitative one that the paper for that scale reports.*

The run's case: Paper IV §3 asserts the universal and names **two** witnesses (Paper II's κ, Paper
III's φ ⊙ δ); §3's Household paragraph reports no number and cites no paper; `household`, `sovereign`,
`compose`, `extensive`, `fold`, `atomic`, `physical component` and `claim component` are **all zero
occurrences in Paper II**; and none of Paper IV's seven §9 limitations or three §4.4 limits mentions
the household scale.

**Every one of those facts is true and the conclusion is still false.** Two refuters, aimed at that
finding and nothing else, both returned REFUTED, and one of them produced the witness:

> **Paper III §2–§3.1 *is* the household-scale paper, and it reports numbers.** §4 opens: *"**§3
> established what the filter does to one asset.**"* §2 is a single un-summed holding with a physical
> layer and a claim layer — `E(t+1) = E(t)·(1 − d(1−m))` and `C(t+1) = C(t) + φ·ΔE + α·gap(t)` — at
> **effective decay 0.02 per period and recognition rate α = 0.05**. Paper IV §3's household sentence
> is *"a physical component that degrades at some rate and a claim component recorded at some other
> rate … a roof has a service life and a mortgage has an amortisation schedule, and **they are
> different numbers**."* Those are the two numbers. §3.1 then reports the scale's quantitative
> results — the lag table, and `D(φ) = (1 − φ)·D(0)` with `D(0) = 1998.99`, reproduced to 10⁻¹⁵.
>
> And Paper IV supplies the pointer, in the **first clause of the next paragraph**: *"**Firm.** A
> balance sheet is **the household's holding, summed and reported.** Paper III's result is that this
> reporting is a filter…"* The household's holding is named as the object Paper III sums. The
> citation is there; it is across a paragraph break.

**The run read §3's three paragraphs as three sealed cells and asked whether the household cell
carried a citation.** It does not. The bridge sentence does. That is a real defect in the paper's
prose — §6.1 repairs it — but it is a missing clause, not a missing witness.

### 3.3 · The verdict, and it does not need the interpretive question answered

FAILURE is a **conjunction**: (a) carried away ∧ (b) not stated in any single paper ∧ (c) **no
evidence anywhere in the corpus and no limitation disclaiming it**. `One is enough` governs the
number of sentences, not the number of limbs.

**Limb (c) fails for every belief either builder produced that was put to a refuter:**

| belief | why limb (c) fails |
|---|---|
| the designer's candidate — *"very largely not being measured"* | **§4.4 limit 1** — *"A state that composes is not thereby a state anyone can observe … The framework's own results are the reason to be sceptical that the composed state is available"* — nine lines below it, in a section headed *"the limits of the resolution, **stated here rather than in §9**"*. Plus **§9 limitation 1** (*"runs directly against the paper's own comfort … a weaker asset than the argument's confidence might suggest"*) and **§9.7**, which forbids in advance the exact over-reading the candidate alleges: *"`REG-013` can establish that an intersection is unoccupied. That it is worth occupying is what the argument has to earn."* |
| the three-scale / atomic-unit belief | **Paper III §2–§3.1** is the evidence, as above |
| A#2 — the levy's four coordinates *"and nothing else"* | Paper II §5 limitations 3, 4 and 6 — *"No production, no labour supply, no portfolio choice… The Lucas critique applies in full force and is not answered here"*; *"One good, one asset, no prices"* |
| A#17, B#6 — ρ ↔ φ, Λ⁻¹ ↔ SDG 7.3.1 | disclaimed in terms in all three papers; III §A.2.2's *"emphatically not"*, III §9.5's *"the same quantity dimensionally, not empirically"* |
| B#7, B#11 — §5's provenance, the pins and counts | §1.2 excludes these from system-level failure **by name**: *"A reference error, a typo, a stale number, a broken pin."* They trace to a paper and a section and report results |
| B#2, B#3, B#4, B#8 — Paper III's abstract stronger than its body | §4.6's three qualifications, §4.8's retraction, §9.4's *"this paper has not written it"*. Where a disclaimer is genuinely absent the defect is an abstract overreaching its own body, which §1.2 classes `P7` |

**So FAILURE cannot fire, and the reason is not limb (b).** That matters: the whole of §3.1's dead
claim turned on how limb (b) should be read, and **the leg is decidable without answering it.** The
ambiguity is real and is recorded in §5 as a finding about the registration, but it carries no part
of this verdict and no reading of it would change the verdict.

REFUTED requires *every* extracted sentence to trace. All 17 of A's and all 11 of B's do, to a paper,
a section, and a result or a disclaimer — the table above covers the contested ones and the rest are
uncontested.

> **E2 — FAILURE REFUTED.**

### 3.4 · What the corpus actually did right, stated because it is the leg's real content

E2 hunts a belief living in the gaps between three separately-hedged papers. **The corpus does not
have those gaps, and the reason is a decision `ADR-001` made for other reasons entirely.** The
decomposition put a **conjunction-carrier** in the corpus: Paper IV states the corpus-level claims in
its own body, in its own voice, and then disclaims them in its own limitations — ten of them across
§4.4 and §9, four of which bear directly on the beliefs this leg extracted. The demotion `E1` forced
is carried **in all three volumes**, against interest, including in the appendix of the paper that
lost the least by it.

A monolith would have had the gaps. Three papers with no carrier would have had them worse. **The
corpus is not immune to E2 by luck; it is immune because someone wrote the limitations sections
honestly and put the conjunction where it could be read.** That is worth a sentence in a document
whose other four legs have gone the other way.

---

## 4 · Admission accounting — what E2 may and may not count

`END-TO-END-001` §1.1: a finding a competent single-paper review could have made is reclassified
`P7`, logged as one, and **scores nothing.**

| finding | class | why |
|---|---|---|
| E2's failure is refuted; every extracted sentence traces | **system-level, admissible** | Needs all three papers and the corpus-level reading. It is the leg's verdict |
| The power check's target sits inside the power check's own mandated input | **about the design, not the corpus — scores nothing** | §5. Sixth defect a leg of this pass has found in the pass's own registration |
| `END-TO-END-001` quotes Paper IV §4.3 with its trailing causal clause cut | **about the design — scores nothing** | §5. The first defect in the registration's handling of the *corpus's* prose rather than its own |
| E2 defines ownership four times and one definition is the odd one out | **about the design — scores nothing** | §5. Does not carry the verdict; limb (c) settles it |
| Paper IV §3's Household paragraph carries no citation and no number, relying on the next paragraph's first clause | **`P7`** | A referee of Paper IV alone sees three scales asserted and two papers named, four lines apart. Repaired anyway (§6.1) |
| Paper IV's contribution 2 says *"the thermodynamic structure **nobody is looking at**"* where the body carries a hedged quantifier | **`P7`** | A universal summarising a hedge. Repaired (§6.2) |
| The same repair attempted on the **abstract** and **withdrawn**, on measurement and then on merit | **`P7` — NOT A FINDING** | §6.2. Logged because a repair tried and withdrawn is cheaper to read than one silently not made |
| Paper IV §5 has no regeneration command in §10 | **`P7`, and pre-existing** | Builder B's #7. §1.2 excludes a broken pin. Teed up, not taken here — `-59` has already edited Paper IV twice and a third edit in the same session is not a third check |

**Counts, reported separately as §2.0 requires. TEST legs run: 4. FAILED: 2 (`E1`, `E3`). UNDECIDED:
1 (`E5`). REFUTED: 1 (`E2`). AUDIT legs run: 0.** No combined score is available and none is offered.

---

## 5 · What the registration got wrong this time — and one of them is new in kind

`-58` recorded that `END-TO-END-001`'s prose about itself was **0-for-5** and made checking it a
standing first move. It is now **0-for-7**, and the seventh is of a kind the previous six were not.

1. **THE POWER CHECK'S TARGET IS INSIDE THE POWER CHECK'S OWN INPUT** (§2). The check reads abstracts
   and contributions lists; the candidate is in Paper IV's abstract and in contribution 2 with its
   section number attached. The instrument cannot miss and therefore cannot measure. `-58`'s tell
   generalises: **a calibration standard printed on the instrument's input is a blank line wearing a
   tick.**
2. **E2 DEFINES OWNERSHIP FOUR TIMES AND THEY DO NOT AGREE.** The check's line 10 (*"the result or
   the explicit limitation **that owns it**"*), the REFUTED clause (*"either a result or a
   disclaimer"*) and the remedy (*"**owned only if a paper can name the evidence**"*) are all
   evidentiary. FAILURE's limb (b) (*"not **stated** as a claim in any single paper"*) is
   presence-based. Under the presence reading, a `[TEST]` leg cannot lose, because the corpus has a
   conjunction-carrier — and §2.0 says a leg that cannot lose is an AUDIT and calling it a TEST
   inflates the run. **This run does not rule on it**, because limb (c) decides the leg without it,
   and ruling on a fixed clause you did not need to rule on is re-choosing.
3. **AND THE NEW KIND — THE REGISTRATION MISQUOTES THE CORPUS.** The candidate is registered as
   *"the extensive state … **does** survive the sum, and it is very largely not being measured."*
   Paper IV §4.3 reads *"…and it is very largely not being measured, **because it is not what an
   aggregate is usually built for**."* The clause is dropped without an ellipsis, and it is the
   clause that converts a census of the world's instruments into a claim about **what aggregates are
   constructed to do** — which §4.3's three preceding sentences argue, with SMD, with Hildenbrand and
   Grandmont, and with three named instances. **The registration committed, against the corpus, the
   exact error `-58` wrote into §5 of the handoff four days ago:** *do not quote a sentence into a
   finding without its trailing scope clause.*

The first six were the registration being unreliable about **itself** while remaining reliable about
the corpus — `-58` called that *"a strange and rather beautiful thing for a document to be."* The
seventh ends that run. `END-TO-END-001` is not edited; `END-TO-END-002` is the repair path.

---

## 6 · What was done to the corpus

**Neither of these is an E2 remedy.** E2's remedy (*"owned or cut"*) is conditioned on an unowned
claim and no unowned claim was found; applying it would be re-choosing a fixed clause in the
direction the run prefers, which `-57` ruled against and which binds. Both are `P7` repairs under the
standing bug-spray order, logged as `P7` in §4, and **`-59` does not also score them** — the `-58`
precedent that the session which rewrites a passage may not grade it.

### 6.1 · Paper IV §3's Household paragraph now names its witness

The paragraph asserted *"they are different numbers"* and printed neither, leaving its citation to be
carried by the next paragraph's opening clause. It now names Paper III §2's calibration and §3.1's
result, which is where the numbers have been since 2026-08-05. `.bak-wt59-e2` beside the file.

### 6.2 · Contribution 2 repaired; the same repair attempted on the abstract and WITHDRAWN

The body reads *"very largely not being measured, **because it is not what an aggregate is usually
built for**."* Two summaries of it were checked.

**Contribution 2 — repaired.** It said *"preserves the thermodynamic structure **nobody is looking
at**."* *Nobody* is a universal standing in for *very largely*, which is a hedge, so the summary is
**stronger than what it summarises**. It now carries the reason. The contributions list has no length
ceiling and the repair costs nothing.

**The abstract — attempted, measured, withdrawn, and the withdrawal is the more useful of the two.**
The clause was appended and `scripts/check_abstract_size.py` went red: **Paper IV's abstract is 248
words against a 250 ceiling** (`PREPRINT-CHECKLIST` §A; arXiv's is 1920 characters), the clause is 12
tokens, and the result was 260. **Two words of headroom is the whole budget.** That is a fact about
the abstract nobody had written down and it is now here.

But the measurement is not why the repair was withdrawn — a guard that says *no room* is a reason to
find room, not a reason to stop. It was withdrawn because **on inspection it was not warranted.** The
abstract says *"largely unmeasured"* where the body says *"**very** largely not being measured"*: the
abstract is **weaker**, not stronger. What it drops is a *causal explanation*, and what §1.2 and this
project's standing tell are about is a dropped *scope qualifier*. **An abstract compressing away a
`because` is compression; an abstract dropping a hedge is overreach.** Contribution 2 was the second.
The abstract was the first, and the run had classed them together on a resemblance.

This is recorded rather than quietly reverted because **`-59` made, inside its own repair, a smaller
copy of the error it had spent the afternoon losing to**: it grouped two sentences by their surface
and did not check whether they failed in the same way. The guard caught the length. Only re-reading
caught the merit.

### 6.3 · What was deliberately NOT done

- **`END-TO-END-001` is not edited.** Three findings against it in §5 and the standing ruling forbids
  anything else.
- **Papers II and III are not edited.** The leg gives them nothing to do. Paper III §2–§3.1 is the
  witness that refuted the run's own finding; it needed nothing.
- **`src/` is not touched.** No code was run against it.
- **Paper IV §5's missing regeneration command is teed up, not taken** (§4). It is `P7`, it is
  pre-existing, and it is a third edit to a paper this session has already edited twice.
- **Paper IV's title is still one step ahead of its narrowed abstract** — *"one atomic unit from the
  household to the sovereign"*. `-57` teed it up as Jason-sized and it stays Jason-sized: this leg
  establishes that the household scale **has** a witness, which makes the title's range claim
  defensible and its *unit* claim a separate question the corpus has not asked.

---

## 7 · What this does not license

**A refuted leg is not a passed corpus.** `E2` asked one question and got one answer: no belief the
extraction produced is unowned. It says nothing about whether the owners are *right* — three of the
sentences in §3.3's table trace to disclaimers rather than to results, which is ownership, not
support. `E4` is the leg that asks what the corpus has established about the world, and it has not
been run.

**And the pass verdict is unchanged: THE SYSTEM FAILS**, on `E1` and `E3`, at `T = 2`, with `E4`,
`E6` and the pass-level `RESULT-END-TO-END-001.md` still open. `T` can rise and cannot fall, and a
refuted leg does not lower it.

*Coffee status: ☕ the run built a finding, refuted it, built a better one, refuted that too, and the
thing that killed the second one was a paper reporting a number in 2026-08-05 that the run had spent
an afternoon asserting nobody had ever reported. Five refuters, two rounds, nothing left standing —
and the corpus wins its first leg of the pass by having written its limitations sections honestly.
**A blind pass is worth having. A refuter is worth having twice.*** 🥎
