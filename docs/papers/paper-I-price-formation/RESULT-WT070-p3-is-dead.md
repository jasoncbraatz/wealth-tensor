# RESULT · WT-070/071/072 · **P3 · Atomism is dead, and what killed it is a better paper**

- **At-bat:** write Paper I at the P3 level, as re-scoped by Jason 2026-08-11 (ADR-001 addendum 4).
- **Outcome:** the P3 framing did not survive its own adversarial pass. **Not one word of the paper
  was written.** The three claims that were about to carry it are each false or unsupported, and the
  process that established that also produced the replacement.
- **Caught by:** WT-065, fired before a ledger entry, before any paper text, and **before Jason was
  told.** Second time the moved trigger has paid for itself. The gap between building the instrument
  and disbelieving its interpretation was three tool calls.
- **Instruments:** `scripts/wt070_p3_fold.py` · `scripts/wt071_refuter.py` ·
  `scripts/wt072_coupling.py`. All committed, all run, every guard mutation-tested (WT-069).

---

## 1 · What was going to be claimed

> Excess demand is a **fold over units**. The supply and demand schedules are folds over units **and
> the allocation** *H*, which is not a property of the population. The Marshallian decomposition
> manufactures two objects that present as aggregates while carrying information no fold contains.
> **P3 caught in the act on the most canonical diagram in economics.**

Three supporting results were built and verified numerically. All three arithmetics are correct. The
framing they were built to support is not.

---

## 2 · The three things that killed it, each settled by running it

### D1 · The crossing height **is** the volume — so the diagram is not caught in the act

At a clearing price *p*\* strictly inside the interval, {*i* : *mᵢ* > *p*\*} is exactly *T*, the
top-*S* valuers. Therefore

> *D*(*p*\*) = |*T* \ *H*| and *S*(*p*\*) = |*H* \ *T*| = **V**, and the two are equal.

Verified for all 25 allocations. **The quantity coordinate of the Marshallian cross is the allocation
mismatch** — the one thing *z* cannot deliver. The two curves are not gratuitous carriers of
irrelevant information; the price coordinate reads the population and the height reads the coupling,
and the diagram does both jobs in one picture.

*This inverts the conclusion.* The honest paper explains what the two curves are **for**. It does not
indict them.

*One thing the attacker got wrong and it is worth keeping:* he called the cross the *minimal*
sufficient structure. It is not — (*z*, *V*) is smaller, and (*m*₍S₎, *m*₍S₊₁₎, *V*) smaller still.
The cross is a **maximally redundant** encoding that happens to expose the scalar as a crossing
height. Adequate, elegant, not minimal.

### D2 · The headline number was noise, and the control was misspecified

The claim was: "raise NON-HOLDERS 20%" (specified via *H*) gives 23 distinct clearing intervals
spanning **26× the baseline interval width**, while "raise EVERYONE 20%" gives 1.

| *N* | interval width | spread | ratio |
|---|---|---|---|
| 400 | 0.036665 | 0.9576 | **26.1×** |
| 1,000 | 0.056690 | 0.4715 | **8.3×** |
| 4,000 | 0.004385 | 0.4977 | **113.5×** |
| 10,000 | 0.004435 | 0.2093 | **47.2×** |

A 13.6-fold non-monotone swing. The denominator is the gap between two consecutive order statistics —
**a single random draw with enormous relative variance.** The ratio is dominated by noise in its own
denominator and is not a statistic. *(The attacker predicted Θ(*N*) growth and was wrong about the
mechanism while right that it is not an effect size. The real reason is worse than the one he gave.)*

And the control was wrong:

| perturbation | spread | distinct intervals |
|---|---|---|
| raise NON-HOLDERS 20% — *indexed by H* | 0.9576 | 23 |
| **raise a RANDOM 250 by 20% — never names *H*** | **0.8934** | **21** |
| raise EVERYONE 20% — *rank-preserving* | 0.0000 | 1 |

The 23-vs-1 contrast was **rank-scrambling versus rank-preserving**, not allocation-indexed versus
population-defined. *H* contributed essentially nothing. This is the `4/21 < 4/11` defect in its
fourth costume: a control that controls for the wrong thing.

### D3 · The load-bearing sentence is false in the formalism we cite

*"H is not a property of the population."* Let the unit be (*mᵢ*, *hᵢ*). Then

> *D*(*p*) = Σᵢ (1 − *hᵢ*)·1[*mᵢ* > *p*] and *S*(*p*) = Σᵢ *hᵢ*·1[*mᵢ* < *p*]

are **additive folds over units in exactly the sense *z* is.** Same reduction, richer per-unit
function. Nothing is manufactured. This is Arrow–Debreu's (preferences, endowment), Aumann (1964) and
Hildenbrand (1974)'s distribution over characteristics — and Hildenbrand (1994) p. 36, *which this
programme spent the morning establishing and was about to cite*: the household characteristic is
(income, demand function). **We would have cited the source that refutes us.**

Five rescue routes were tried. Four fail:

- **Anonymity/exchangeability** — fails fastest. Under the diagonal S_N action, *D* and *S* are
  relabelling-invariant *and they see H*. Both are symmetric functions of the multiset {(*mᵢ*, *hᵢ*)}.
- **"Permute holdings among agents with fixed *m*"** — the stabiliser is almost surely trivial for
  continuous *m*; the twisted action is the claim written as a group. **Gerrymandered.**
- **Sufficiency** — no likelihood, so it is an analogy. Its honest form concedes the point: *h* is
  **ancillary for the price and informative for the volume**.
- **State vs. characteristic** — real, but a modelling convention until a process is specified, and
  under any process with friction *h* feeds back into prices.
- **Fréchet-class rearrangement group** — *works, is natural rather than gerrymandered, and ratifies
  the prosecution.* Its invariants are exactly the marginals.

**One genuine asymmetry survives and is worth a footnote, not a framing:** the *hᵢ* are subject to a
global constraint Σ*hᵢ* = *S*, so they can never be conditionally i.i.d. across units — under any
exchangeable prior they are hypergeometrically, not binomially, distributed. *H* is a **globally
constrained labelling, not an independently drawn per-unit characteristic.** That does not save the
sentence.

---

## 3 · And the exhibit that was supposed to demonstrate it was measuring a hypergeometric

The reported crossing-height range **85 to 103** across 25 uniform allocations:

| | |
|---|---|
| hypergeometric mean *S*(*N*−*S*)/*N* | **93.75** |
| hypergeometric sd | **4.69** |
| ±2 sd band | **[84.4, 103.1]** |
| 25 uniform draws | min 85 · mean 94.36 · max 103 |

**Every single draw is inside ±2 sd of a number the population fixes.** The quantity the paper is
about had never actually been varied. *And v0.1's "93 → 49" volume table inherits this: its baseline
93 is* S(N−S)/N *to two significant figures, and nobody noticed for two sessions.*

Vary the **coupling** instead of resampling, and it moves:

| coupling | crossing height | clearing interval |
|---|---|---|
| comonotone (*H* = top-*S*) | **0** | [21.4619, 21.4985] |
| antitone (*H* = bottom-*S*) | **150** | [21.4619, 21.4985] |
| block (*H* = middle-*S*) | 125 | [21.4619, 21.4985] |
| alternating | 93 | [21.4619, 21.4985] |
| uniform random | 97 | [21.4619, 21.4985] |

**Volume traverses its entire range, 0 to 150. The clearing interval is bit-identical in every row.**
That is the exhibit the paper always needed and had never run.

---

## 4 · The replacement, and it is a theorem rather than a framing

With a per-unit wedge *t* — a holder sells only if *mᵢ* < *p* − *t* —

> *z*(*p*) = #{*i* : *mᵢ* > *p*} − *S* + **#{*i* ∈ *H* : *p* − *t* ≤ *mᵢ* ≤ *p*}**

and the allocation stops cancelling. The residual is a sliding-window count *W*(*p*) of the
**locked-in holders**.

| *t* | distinct *z* schedules over 25 couplings | locked-in holders (mean of *S* = 150) |
|---|---|---|
| **0.00** | **1** | — |
| 0.05 | 25 | 1.1 |
| 0.25 | 25 | 1.5 |
| 1.00 | 25 | 8.2 |
| 3.00 | 25 | 22.3 |

**And *W* identifies the coupling exactly.** Across 25 holder sets with identical population marginal:

| *t* | distinct *W* profiles | distinct holder valuation sets |
|---|---|---|
| **0.00** | **1** | 25 |
| 0.01 | **25** | 25 |
| 0.10 | **25** | 25 |
| 1.00 | **25** | 25 |

Including the hardest case — two holder sets differing in **exactly one agent** — separated at every
*t* ≥ 0.01. Separation degrades as *t* → 0 exactly as it should:

| *t* | L¹ distance between the two *W* profiles (single-agent swap) |
|---|---|
| 0.001 | **0** ← below grid resolution; a limit of the measurement, not of the theorem |
| 0.01 | 1 |
| 0.10 | 8 |
| 1.00 | 76 |
| 3.00 | 228 |

**The identified set for the coupling is EVERYTHING at *t* = 0 and a SINGLETON at every *t* > 0.
Identification is discontinuous at zero.**

> **Frictions are not what invalidate the allocation-invariance of price. They are what make
> misallocation visible in it.**

That sentence contains P3's true content as the degenerate case, converts the most damaging objection
into the main theorem, and is falsifiable in a way P3 was not.

---

## 5 · What this costs, stated plainly

1. **The indictment goes.** No "manufactures two objects," no "provably irrelevant information," no
   canonical diagram caught in the act. The diagram is fine. The polemic was the appeal and it is
   unrecoverable.
2. **"H is not a property of the population" goes**, replaced by *the price functional factors through
   the marginal; the schedule functional does not.* Ontology becomes factorisation. Less quotable,
   and true.
3. **The 23-vs-1 headline goes — and should be inverted and reported as a confirmation.** The honest
   control giving 0.8934/21 against 0.9576/23 is exactly what the factorisation predicts: *H*
   contributes nothing to the price because price is a marginal functional. The prosecution's best
   hit is the paper's cleanest supporting experiment, misfiled as a headline.
4. **The centre of gravity moves from *t* = 0 to *t* > 0** — from an invariance that is plausibly a
   known quasilinearity corollary to an identification theorem that is plausibly new.
5. **This is no longer a re-scope of Paper I. It is a different paper**, and that is Jason's call
   under ADR-001, not a session's.

---

## 6 · Three open exposures, none of them closeable by a session alone

- **Is the *t* = 0 invariance a known corollary of quasilinearity?** MWG ch. 10, Shapley–Shubik,
  Böhm-Bawerk's marginal pairs. The defender flagged this as **the largest threat, larger than any
  of A1–A4**, and flagged it as background knowledge rather than verified. Novelty cannot live at
  *t* = 0.
- **The identification theorem versus the bunching literature.** Kleven (2016, *Annual Review*); Best
  & Kleven (2018). "Notches make the underlying distribution visible" is their reduced form. The
  structural injectivity statement must be positioned against it explicitly, not claimed as virgin
  territory.
- **The lock-in literature is crowded and one paper is very close.** Cho, Li & Uren (2024,
  *Quantitative Economics*), *"Stamping out stamp duty: Housing mismatch and welfare"* — stamp duty
  as a buyer-side wedge, mismatched homeowners falling 13.4% → 4.6% when removed. A paper whose
  contribution is "*H* matters when *t* > 0" is scooped. The contribution has to be the
  **identification discontinuity at zero**, or there is no contribution.

---

## 7 · The method note, because `docs/` is written for three specific readers

**Three agents ran and the one told to DEFEND the paper killed it.** The prosecution found that the
framing was false. The defender found that it was false *and* supplied the replacement, *and* found
that the prosecution's own best hit had the mechanism wrong, *and* found the same hypergeometric
defect in the exhibit the prosecution had left standing. **Second session running that the defence
attorney has done the most damage.** L28 is now confirmed twice and should be treated as doctrine
rather than as a tip.

**The `4/21 < 4/11` defect has now recurred four times across three sessions** — a PASS scored from a
regime with zero events; a negative control that controlled for nothing; a test comparing an
invariant with itself; and now a control that varied rank-preservation while claiming to vary the
allocation. *It recurs because it is the same mistake wearing the costume of whatever the session is
about.* The only thing that has ever caught it is running the control that was not asked for.

**And the pleasing part.** The session was briefed to write a paper. It wrote three scripts, killed
its own thesis, and did not write the paper — and that is the correct outcome, arrived at in one
session, at a cost of a few minutes of agent time, with nothing false reaching the ledger, the papers
or Jason. The framing died at 4-and-a-half hours old. Wicksteed's chapter took 116 years to catch up
with Paper I v0.1; P3 · Atomism managed not to survive the morning it was born. 🪃
