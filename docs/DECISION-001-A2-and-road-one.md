# DECISION-001 · Paper II: what A2 costs and what Road One buys
*wealthTensor-60 · 2026-08-17 · **written for Jason, to be read once and decided.** Six sessions have
called this "Claude-sized" and not written it. This is the page. Everything below is quoted from the
repository or measured in it; nothing is proposed that needs a number we do not have.*

---

## The one thing nobody's handoff says: **half of Road One is already in Paper II, unlabelled.**

`REVIEW-004` A2 said the fix was a Kesten mechanism — a stock levy **scales** the growth multiplier
(cuts E[log A], leaves Var[log A] alone); a flow levy **truncates** it (cuts both). It said: run it
before you print it. **It was run.** `scripts/wt077_tail_index.py` ran clean, and Paper II §3.1 now
carries the result:

> *"Unlevied, Var[log a] = **0.076542**. Under the **stock** levy at that budget it is **0.076536** —
> a change of six parts in a million, which is to say none at all. Under the **flow** levy it is
> **0.051189**, a third lower. A levy on stock rescales what a holder has and leaves the process that
> got them there exactly as it found it; a levy on flow reaches into the multiplicative term itself."*

And the item `ROADS-001` called *"the strongest claim and the one most likely to be wrong"* also came
back: **at r = 1 the flow levy caps the multiplier below 1 (ess-sup a = 0.9524), so no power-law tail
exists at all.** That is in `HANDOFF-PROMPT.md`, in a parenthesis, and **nowhere in the paper.**

So Road One's price is no longer "two days of computation." Its two hardest computations are done.

---

## Is A2 right? **Two-thirds.** The fatal third is fatal.

**RIGHT, and certain — κ is not the mechanism.** Paper II's own §3.1 table, two rows apart:
stock r = 0.100 → κ **0.1000**, Gini **0.222**; flow r = 1.000 → κ **0.1026**, Gini **0.125**. A
2.6% *larger* budget buys 44% more compression. And §3.3 kills it from the other side: a threshold
at 0.25× the mean *"costs nothing measurable in compression (0.444 against 0.443) while reducing κ
by a quarter."* κ can move a quarter with no effect, and hold fixed while the outcome moves 44%. **No
function of κ alone reproduces both rows.**

**WRONG — the title's *region* claim survives.** A2 says *"if the base set a ceiling the rate could
not cross, the flow base could not beat the stock base at all."* That does not follow: the paper
defines the region by its frontier and already publishes it — *"the frontiers are **nested**, stock
0.000 against flow 0.125."* Flow-at-r=1 beating stock-at-r=0.1 is a comparison **across rates**,
which is exactly what "the rate moves you within it" permits. A2's "44% more compression" is also
loose: the Gini is 44% lower; compression against the unopposed 0.994 baseline is 12.6% more.

**So the live defect is κ, not the region** — and it is worse now than when A2 was written, because
the evidence that refutes κ-as-mechanism sits **four paragraphs below** the sentence asserting it, in
the same section, with nothing connecting them. Still asserting κ-as-mechanism today: the **abstract**
(*"The mechanism is κ"*), **§1 contribution 2**, **§2.4** (*"the quantity through which the base does
its work"*), **§3.1's heading and gloss**, and **§6** (*"a closed-form mechanism (κ)"*).

---

## The three options, priced

| | **A · The narrowing repair** | **B · A + retire the title** | **C · Road One (full re-cut)** |
|---|---|---|---|
| **What changes** | Demote κ from *mechanism* to *budget* in 5 places; add one sentence after §3.1's matched-κ paragraph saying what the paper's own numbers already show — κ is necessary, not sufficient, and §3.3 is the second witness. | A, plus a title the body defends, plus 4 downstream reference/exemplar edits. | New title, new abstract, new §1; §3 becomes the inversion + the tail index + the r = 1 cap; §4 "trim"; §5 demotes κ; new §6 "what was tested and survived"; §7 gains the retraction. |
| **Edits** | ~6, one file | ~11, four files | a rewrite of a 26 KB paper |
| **New computation** | **none** | **none** | **none left** (wt077 done) |
| **Blocked on** | nothing | nothing | **one literature search, never run** |
| **Retracts** | κ-as-mechanism only | + the title claim | + §1 contribution 2, §2.4, §6 |
| **Downstream** | none | Paper IV §7 (1 sentence) + 3 reference entries + `PREPRINT-CHECKLIST.md`'s title exemplar | same as B |
| **Leaves C available** | **yes** | **yes** | — |

**The blocker on C, stated plainly.** `REVIEW-004`, `ROADS-001` and `HANDOFF-PROMPT` all demand the
same search before the truncation-vs-scaling result is claimed in print — *"whether anyone has
already published the truncation-vs-scaling effect on the tail index … optimal-taxation-with-Pareto-tails
is where it would live … **this is the one thing I would most want searched, precisely because it is
the thing I am telling you to lead with**."* Grep across all of `docs/` finds that phrase **only at
the three places recommending it**. No scouting note, no result, no ledger entry. **The search has
never been run.** A is not blocked by it; C cannot honestly be written until it is.

**What C buys, and it is the real argument for it** (`ROADS-001`, and I think it is right):
*"Your two embarrassments become confirmations, honestly, with no reframing sleight of hand."* A1's
ρ = 0 tautology becomes a passed test — the framework predicts in advance that ρ cannot change *A*'s
shape, and then it doesn't. The free threshold stops being an apology and becomes the sharpest
instance. B1's wrong-signed periodicity result stops needing a causal story. Five results with no
spine become one principle. And it reverses a standing prior — *the wealth tax is not the stronger
instrument* — which is the paper's only real answer to the forum dismissal.

---

## What binds, whichever you pick

- **`E1`'s refuted-branch remedy may NOT be moved into Paper II.** *"Paper II's new §3.x reporting a
  non-identification result — that is the **refuted** branch's remedy for an outcome that did not
  occur. `E1b`'s numbers stay in this document."* Any repair is built from Paper II's own published
  numbers and `wt077`'s, not from E1b's.
- **The abstract is a submission field** — 150–250 words **and** ≤ 1920 characters, measured on the
  decoded string, never with `wc -w`.
- **No ruling freezes Paper II's title.** ADR-001's title is frozen; Paper II's is not, and Paper
  III's title was already changed when Road Two ran. Precedent exists.
- **`P3` stays manual and the session that does the work may not score it.**

---

## ☑ Jason's call — RULED 2026-08-17, in session `wealthTensor-65`

- **☑ A** — stop the internal contradiction now, cheapest honest move, C stays open. **TICKED.**
- **☐ B** — A plus retire a title that is two revisions behind its own body. *(`-60`'s
  recommendation. Declined, and for a reason about ORDER rather than about B: if C happens, C
  replaces the title anyway, which makes B the option most likely to be wasted work. The title
  question rides with the C decision.)*
- **☐ C** — commit to Road One. **NOT foreclosed — deferred behind its own blocker.** The
  literature search is now the next session's at-bat, exactly as this line says.
- **☐ none of the above / talk to me first.**

**THE RULING, IN JASON'S WORDS**, because it is a sequencing decision and not simply "A":

> *make a full Kelly bet on A, and only re-allocate that bet once we can build — or IF we can
> build — credibility behind C.*

**Why the search stopped being a blocker and became an at-bat.** Six sessions carried C as
*"blocked on one literature search, never run"*. A literature search is a Claude with web access
and an afternoon; it is not a decision. It went unrun because it was filed behind the decision,
and the decision waited on the price of C, and the price of C is the thing the search reports —
two items politely holding the door for each other. Breaking the deadlock costs one at-bat.

**The defensibility case that decided it**, recorded so the next session does not relitigate:

* What is actually indefensible today is not that κ is overclaimed, it is that **the paper
  contains its own refutation and does not notice** — §3.1's own table, plus §3.3, sitting four
  paragraphs below the sentence they kill. A referee who finds that concludes the author did not
  read his own table, and that judgement contaminates the parts of the paper that are right.
  **All three options fix this**, so the choice was only ever about what else to take on.
* **C's risk is the search, not the work.** `ROADS-001` calls truncation-vs-scaling *"the
  strongest claim and the one most likely to be wrong"*. Under A, if the effect turns out to be
  known, it is a supporting observation in §3 and gains a citation. Under C it is the title, and
  *"this is known and the author did not know"* is the one referee outcome no reproducibility
  apparatus can absorb.
* **C raises the evidentiary bar without raising the evidence.** Today the paper makes a
  measurement claim defended by committed code that reproduces byte-exact. C makes a theory claim
  about redistributive instruments in general — and `REVIEW-007` has just established that §5's
  results are **one seed** and that §3.4 had carried a 600-period number under a paper-wide
  T = 1200. Those are repaired as prose; the computational base underneath is unchanged.
* **The apparatus is the moat.** This paper's distinctive asset with referees is not its claims;
  it is that it is pre-registered, reproducible, and publicly documents predictions that failed.
  A modest paper behind that apparatus is close to unassailable. An ambitious one invites someone
  to test the ambition against the apparatus — and the apparatus is honest enough to answer.
* **And one of C's two headline payoffs was resting on a misdiagnosis.** `ROADS-001` argued that
  under Road One the ρ = 0 tautology becomes *a passed test — the framework predicting in advance
  that ρ cannot change A's shape*. `-65` measured it: `redistribution.py:131` is
  `recognised_flow += self.rho * gain + self.wage`, so at ρ = 0 the base is the **wage**, κ =
  0.000565 rather than zero, and the identity holds because the wage is **uniform across agents**
  — nothing to do with the multiplicative term. See `WT-098`. The result is real and is stronger
  than the paper claimed; the *story* C wanted to tell about it was not.

**What A cost, measured:** ten edits across two files, no new computation, abstract 249 → **244**
words (six of slack returned rather than spent), suite green. **`II-2` and `II-3` are repaired
here**, as `REVIEW-005` §2 said they would be by whichever option was ticked.

---

### Two process findings this page turned up, both worth more than the decision

1. **`CHECKLIST.md` and `done-criteria.tsv` contain ZERO rows** for A2, `REVIEW-004`, `ROADS-001`,
   Road One or Road Two. **The one-pager was unmeasured for six sessions, which is exactly why six
   sessions could pass it on.** A board built to make the law countable does not count this item.
   That is the mechanism of the process defect `-59` named, and it is now located.
2. **`LEDGER.md` has no `WT-077` entry** and no mention of A2 or ROADS. The sessions that wrote
   `ROADS-001`, ran the tail index, executed Road Two on Paper III and inserted the Var[log a]
   paragraph left no ledger trace. **This is `WT-089`'s lesson happening again**: *"the fact that
   killed `E1` had been sitting in `docs/REVIEW-004` for four days, correctly stated, indexed under
   nothing."* A2's answer has been sitting in §3.1 of the paper since 12 August, indexed under
   nothing, while three handoffs described A2 as untaken.
