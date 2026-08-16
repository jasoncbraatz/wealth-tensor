# END-TO-END-001 · leg E2 · THE BLIND PASS, RECORDED BEFORE THE CANDIDATE WAS READ

*`wealthTensor-59` · 2026-08-16T20:59Z · committed at `72ea97f`, **ahead of any commit in which this
session read `END-TO-END-001` lines 205–240**. `git log --follow` is the evidence, on the `REG-013`
precedent that the registration precedes its instrument.*

---

## 0 · Why this file exists on its own, ahead of the result

`END-TO-END-001` §4.2 names the threat to this leg and fixes the mitigation:

> *"**E2's candidate is named in this document and could prime the run.** Mitigated by ordering: the
> blind pass records its list **first**, and the comparison is a measurement of the extraction's
> power, not of the corpus. A run that reads §2's candidate before extracting has destroyed the leg
> and must say so."*

§5 fixes *"E2's blind-first ordering and its power check"* and forbids re-choosing either. §6, in the
same document, instructs the running session to *"read this file end to end before touching
anything"* — which reads §2, which contains the candidate. `RESULT-END-TO-END-001-E3.md` §2.7 found
that contradiction and recorded that `-56` and `-57` had both followed the imperative and were
therefore disqualified. `-58` preserved the eligibility deliberately and handed it on.

**"Records its list first" is a claim about what a file says at a point in the history.** A blind list
written into the same commit as the comparison is a blind list a reader has to take on trust. This
one does not ask for trust: it is a separate commit, its parent contains no reading of the candidate
region, and the mechanism below made the reading impossible rather than merely forbidden.

---

## 1 · Where the reading stopped, when, and who read what

**The registration was never opened in this session.** It was sliced on darwin and only the slices
were transferred:

```
D=$HOME/repos/wealth-tensor/docs/END-TO-END-001.md   # 505 lines
sed -n "1,204p" $D > /tmp/e2e_a.txt                  # 204 lines, sha256 ac2cf1301a50
sed -n "241,505p" $D > /tmp/e2e_b.txt                # 265 lines, sha256 7b9758a883c7
```

Line 204 is blank; line 241 is `### E3 · THE CONTAINMENT MATRIX`. **Lines 205–240 were never read,
never transferred, and never present in this session's context.** `-58`'s protocol was a discipline —
stop scrolling at a heading. This one is a **cut**: the bytes were not available to be read. That is
the cheaper mitigation and it is the one a successor should copy, because it does not depend on the
reader's self-control at the moment the heading appears.

| what | who | when |
|---|---|---|
| `END-TO-END-001` lines 1–204 and 241–505 | `-59` (this session) | before any extraction began |
| `END-TO-END-001` lines **205–240** | **nobody** | — |
| `RESULT-…-E5.md` §6 (the protocol), `RESULT-…-E3.md` §2.7 and §4.2 | `-59` | before any extraction began |
| Papers II, III, IV in full | two independent builders (below) | during the extraction |
| Papers II, III, IV in full | `-59` | **not before the extraction** — only the two builders' returns |

**What `-59` knew about `E2` before extracting, stated so a reader can discount it.** From
`RESULT-…-E3.md` §2.7 and §7 and from `RESULT-…-E5.md` §6: that `E2` is a `[TEST]`, that it carries a
blind pass and a power check, that the blind pass *"needs the three abstracts and the three
contributions lists"*, and that §7 of the `-57` result refers in passing to *"`E2`'s unowned claim"*.
**That last phrase is a subject, not a candidate** — it says the leg is about ownership and does not
say which belief, which paper, or which direction. §4.2's disqualifier is reading *the candidate*.
It was not read. But the phrase was, it is priming of a weaker kind, and the power check below is
scored with it disclosed rather than with it hidden.

---

## 2 · The two blind builders, and why there are two of them differently framed

`RESULT-…-E5.md`'s standing tell: **two independent builds that agree have checked the evidence and
not the frame.** Agreement between two builders given the same taxonomy is not a check. So the two
builders here were given **different jobs**, and neither was given this leg, this document, this
repository, or any direction:

- **Builder A — the reader.** Asked to read only the three abstracts and the three contributions
  lists, write down in plain sentences what a competent economist would now believe, and only then
  return to the full text to ask, per belief, which paper *states* it and which paper *supports* it.
  This is the extraction `END-TO-END-001`'s blind pass asks for, run as written.
- **Builder B — the referee.** Asked, as a referee holding all three papers at once, to find the
  beliefs a reader will come away with **that no paper takes responsibility for**, and to say
  precisely how ownership breaks in each case. Told that a false positive is worse than a miss.

Neither builder was told the other existed. Neither was told what the answer might look like. The
two lists are recorded separately below and are **not merged** — merging them before the power check
would inflate the power, since a candidate found by either would then read as found by "the blind
pass". Both scorings are reported in the result.

---

## 3 · BUILDER A — what a competent economist would now believe

Recorded verbatim in substance. Classification is Builder A's own: OWNED (one paper states and
supports), SPLIT, UNOWNED, DISCLAIMED.

| # | belief | A's class |
|---|---|---|
| 1 | Multiplicative wealth condenses without bound, so any distribution that is not condensed is being held down by something. | OWNED (II §1 / §3.1) |
| 2 | A period-assessed levy is exhaustively described by base, rate, periodicity, threshold plus a realisation share, and the process's behaviour depends on nothing else. | **UNOWNED** — II §2.2 *defines*; the contributions list calls it *"a demonstration"*; no demonstration exists |
| 3 | The base sets a ceiling the rate cannot cross; the two bases are an order of magnitude apart, the mechanism is κ, closed form within 5 %. | OWNED, with an abstract slip: abstract says an order of magnitude *in compression*, §3.1 says *in κ* |
| 4 | The author's own stronger prediction was falsified by his own sweep (stock 0.000 vs flow 0.125). | OWNED (II §3.1) |
| 5 | At zero realisation a 100 % levy on flow is indistinguishable from no levy at all. | OWNED (II §3.2), narrowed by §5 Limitation 1 |
| 6 | Periodicity and threshold are trim, not structure. | OWNED (II §3.3) |
| 7 | A summary statistic with a hard ceiling cannot serve as a convergence criterion. | OWNED (II §3.4) |
| 8 | Timeliness and durability are not separately identified: (α, δ, φ) and (δ, α, φδ/α) emit the identical series. | OWNED (III §4.2) — the best-supported claim in the corpus |
| 9 | With physical scale unobserved the identified set is a continuum; 1.67× in scale spans the unit interval of φ. | OWNED (III §4.2) |
| 10 | The composite orders asset classes and inverts the intended ranking (τ = −1), constraining cross-sectional conditional-conservatism measures. | DISCLAIMED in part — §4.6's three qualifications; τ = −1 holds only at the calibrated α the same paper rejects |
| 11 | The framework's sharpest prediction was pre-registered, tested at power 0.95–1.00 on 688 EDGAR events, and failed informatively. | DISCLAIMED in part — §5.3's *"what it does not support"*, §6.1's *"no confirmed empirical claim"* |
| 12 | There is a repair needing no new data: disclosed lives supply δ, restoring φ for every class but goodwill. | DISCLAIMED / abstract-only in part — body names two classes; §4.8 retracts the goodwill limit; one band of sixteen clears the floor |
| 13 | **Aggregation preserves the extensive state and destroys the behavioural map — so macroeconomics estimates the half that does not survive, while the half that does is largely unmeasured.** | **UNOWNED** — destructive half is SMD (external, 1972–74); constructive half is a definition by IV §2.2's own admission; *"largely not being measured"* is measured nowhere, in a paper stating *"this paper contributes no new computation"* |
| 14 | In a market for one indivisible good the crossing height is not a behavioural aggregate but the allocation mismatch. | OWNED in statement, **UNOWNED in provenance** — IV §10 gives no regeneration command for §5 |
| 15 | The three literatures genuinely do not read each other — measured, pre-registered, with a ceiling and a floor. | OWNED (IV §6, `REG-013`) |
| 16 | **One atomic unit underwrites all three papers, II being its sovereign-scale instance.** | **UNOWNED** — IV §3 asserts it *about Paper II*; Paper II contains no atomic unit, no physical/claim decomposition, no tensor |
| 17 | You cannot locate a real economy in II's parameter space from reported data, since ρ is a reporting-layer property and φ is unidentified. | DISCLAIMED — denied in all three papers, unusually well |

**Builder A's own nomination for the most striking case: #16, with #13 falling out of it.** Its
closing sentence: *"The corpus's most quotable sentence is the one sentence in the corpus that no
paper both states and supports."*

## 4 · BUILDER B — the referee's ranked ownership breaks

| rank | belief the corpus installs | how ownership breaks (B's words, compressed) |
|---|---|---|
| **1** | **The same atomic unit has been shown to compose from household to firm to sovereign, "answered quantitatively at each" scale.** | **Asserted by Paper IV about Paper II's content, where Paper II contains no such content** — *household*, *sovereign*, *compose*, *extensive*, *fold*, *atomic* all zero occurrences in II — **plus a household leg with no paper at all** |
| 2 | Disclosed useful lives repair identification for three of four GAAP classes, needing no new data. | Abstract contradicts §4.7's own *"grant both roots exactly … the family is untouched"*; one band of sixteen clears the floor, none on firms |
| 3 | The filter model is well-posed over disclosed asset lives (97.4 % admissible). | Carried by an identification the same paper says it has not made (§4.5, §9.4) |
| 4 | The theorem constrains the conditional-conservatism literature. | Unconditional in the abstract, retracted twice in §4.6 |
| 5 | The data constraint that forced the old models has lapsed; firm-level panels are public and free. | IV §1.1 uncited, contradicted by III §9.5, III §4.3 and IV's own §9.1 |
| 6 | Λ is not an invention — the UN publishes its inverse. | IV §7 unconditional where III §A.2.2 disclaims it *"emphatically"* and calls the leg the weaker one |
| 7 | The 25-allocation excess-demand instance is an established computational result of this corpus. | **No provenance anywhere** — no module, script, command or commit; home paper unpublished |
| 8 | τ = −1 with δ leverage 2.58× the failure level. | Condition dropped between body and abstract; denominator misstated (0.61 threshold ⇒ 4.2×, not 2.58×) |
| 9 | The ρ = 0 result is a substantive discovery about observability. | Support is definitional — at ρ = 0 the base is empty by construction — and no paper says so |
| 10 | A pre-registered cross-scale test adjudicated the chain claim. | Carried entirely by a repository document none of the three papers reproduces |
| 11 | Every number is pinned, with a derived test count per paper. | II's pin contradicted by III; §3's scripts never pinned; 38 ≠ 18 |

Builder B also filed six **checked-and-cleared** near-misses so the list would not read as padded,
including that the E1 demotion is recorded consistently and against interest in all three papers.

---

## 5 · What is fixed by this file, before the candidate is read

1. Both lists above, as the blind pass's record. **Neither may be extended after §2/E2 is read.**
2. The power check will be scored **three ways and all three reported**: did Builder A find it, did
   Builder B find it, and did either. The union is the weakest of the three and is not the headline.
3. A candidate that appears in neither list is a **miss**, and a miss is reported as a miss —
   including if the extraction's failure is more interesting than the corpus's.
4. **The lists are not evidence about the corpus yet.** They are two readings. Anything either
   builder found that survives into the result has to survive a refuter first, on `-58`'s standing
   order: **build → build independently → REFUTE → write.**

*Coffee status: ☕ the leg that three sessions could have destroyed by opening a file was preserved by
not opening the file. `sed` is not a subtle instrument, but it cannot be tempted.* 🥎
