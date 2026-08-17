# SCOUT-001 · the truncation-versus-scaling prior-art search

**Card:** `1217547572131984` · **Session:** `wealthTensor-66` · **Date:** 2026-08-17
**Instruments:** `scripts/wt117_litsearch.py` (v1, superseded), `scripts/wt117b_litsearch.py`
(discovery), `scripts/wt118_fulltext_absence.py` (absence). All re-runnable; artefacts
`/tmp/wt117b-results.json`, `/tmp/wt118-absence.json`.

---

## THE VERDICT, IN ONE SENTENCE SOMEBODY CAN MARK RIGHT OR WRONG

> **KNOWN.** Bouchaud & Mézard (2000), *Physica A* **282**, 536–545, equations (11)–(13),
> derive the Pareto tail exponent µ of a multiplicative wealth process in closed form as a
> function of an **income (flow) tax rate φ_I**, a **capital (stock) tax rate φ_C**, and the
> **fractions f_I, f_C of each that are redistributed per capita** — and report the ranking,
> with the sign surprise: the flow levy raises µ (compresses), while the stock levy *lowers*
> µ (disperses) unless enough of it is rebated. That is the substance of what `ROADS-001`
> proposed to lead option **C** with, published twenty-six years ago, in a literature none of
> `REVIEW-004`, `ROADS-001` or `HANDOFF-PROMPT` named.

**Consequence, stated plainly:** option **C** collapses on its headline. Jason's Kelly bet on
**A** was right, and it cost one at-bat instead of a 26 KB rewrite that would have opened with
someone else's equation. This is the outcome `DECISION-001`'s tick was waiting on; the
"re-allocate the bet" test has run and it says do not re-allocate.

---

## 1 · WHERE THE THREE DOCUMENTS SENT ME, AND WHY THAT WAS THE WRONG PLACE

`REVIEW-004` (line 115), `ROADS-001` (line 99) and `HANDOFF-PROMPT` all name the same
target: **the optimal-taxation-with-Pareto-tails literature**. I searched it. It does not
contain the result.

**It was never going to.** The blackbook already holds the leaf that predicts this, and it is
the single most valuable thing the lessons tree returned that `HANDOFF.md` had not inlined:

> *"SEARCH PRIOR ART BY THE SHAPE OF THE EQUATION, NOT BY THE SUBJECT MATTER — a within-field
> search cannot find a result that lives in another field's vocabulary."*
> — `claude-blackbook`, `2026-08-12-search-prior-art-shape-equation-subject`, banked by
> `wealthTensor-12` during the Bateman/flip-flop priority search.

The object is a Kesten recursion `x' = A·x + κ` with `E[A^α] = 1`, and the two operations are
a **scaling** and a **truncation** of `A`. Written that way, the question belongs to at least
five literatures. The public-finance one the documents named is the only one that does **not**
carry it, because public finance asks what a tax raises and who bears it, not what it does to
the shape of a random multiplier. **Statistical physics has asked exactly the latter since the
1990s**, and it is where the answer was.

`-65`'s process-miss note said to run `lessons.py search` at student-in and record what the
tree returned that the handoff did not. It returned the thing that found the paper.

---

## 2 · WHAT WAS SEARCHED (so a reader can judge whether it was wide enough)

### 2.1 · Discovery half — `wt117b_litsearch.py`

Four indexes — **OpenAlex, Semantic Scholar, arXiv, Crossref** — against a 20-query matrix in
three tiers, asking the question in six vocabularies: economics (wealth vs capital-income
tax), applied probability (random difference equations, perpetuities), statistical physics
(multiplicative processes with a bound), actuarial mathematics (stop-loss vs quota-share
reinsurance on a heavy tail), and public finance (Domar–Musgrave loss offset).

### 2.2 · Absence half — `wt118_fulltext_absence.py`

`REFERENCE-POLICY` §1 is jurisdictional here and it is unambiguous:

> *"an abstract can never establish that something is **not** in a paper. Every zero-hit table
> this project has published came from `grep` over an extracted full text, and that is the only
> thing that licenses one."*

So **18 works were downloaded, extracted with `pdftotext`, and grepped** with six
pre-registered conjunction predicates, each declaring in the code what a positive would have
looked like. The corpus is listed in the script with a recorded reason for each membership;
it includes **three field surveys** (Benhabib & Bisin's *JEL* survey, Gabaix's *Power Laws in
Economics and Finance*, Scheuer & Slemrod's *JEP* wealth-tax survey), because covering a field
is a survey's entire job and its silence is the strongest absence evidence obtainable.

---

## 3 · WHAT A POSITIVE WOULD HAVE LOOKED LIKE — AND WHAT ONE ACTUALLY LOOKED LIKE

The predicates, and their final counts over the **12 valid documents**:

| predicate | a positive would have been | fired in |
|---|---|---|
| `TRUNCATION_x_TAIL` | a sentence linking truncation/capping of the growth process to the tail index | **4** |
| `SCALING_vs_TRUNCATION` | the two operations named in the same breath, as the organising contrast | **1** |
| `EQUAL_REVENUE_PAIR` | an explicit matched-budget stock-vs-flow comparison | **2** |
| `VARIANCE_OF_RETURN_x_TAIL` | a tax's tail effect routed *through* the dispersion of the multiplier | **2** |
| `NO_LOSS_OFFSET` | the asymmetry that makes a flow levy a truncation rather than a contraction | **0** |
| `NO_POWER_LAW_AT_ALL` | a tax strong enough to destroy the power law outright | **0** |

**Every hit was read at source.** Three of the four `TRUNCATION_x_TAIL` hits are false
positives on inspection (Piketty & Saez merely assert their own distribution is Pareto;
Benhabib & Bisin's survey discusses truncated support in the normalisation of a Pareto
density; the 2026 arXiv hit landed in a bibliography). The fourth is not.

---

## 4 · THE FINDING, AT SOURCE

### 4.1 · Bouchaud & Mézard (2000) — the result itself

*Wealth condensation in a simple model of economy*, **Physica A 282, 536–545**
(arXiv `cond-mat/0002374`, read at source — full text). Their stated scope, from the
introduction, verbatim:

> *"We discuss the influence of simple parameters, such as the connectivity of the exchange
> network, **the role of income or capital taxes and of state redistribution of wealth, on the
> value of the exponent µ**."*

Their equation (11) is a wealth balance carrying **both levies and both rebates** —
`−φ_I dW_i/dt` (flow), `−φ_C W_i` (stock), `+f_I φ_I dW̄/dt + f_C φ_C W̄` (per-capita
redistribution of each). Equation (13) gives the Pareto exponent µ in closed form in all four
coordinates. And then, verbatim:

> *"It shows that income taxes tend to reduce the inequalities of wealth (i.e., lead to an
> increase of µ), even more so if part of this tax is redistributed. On the other hand, **quite
> surprisingly, capital tax, if used simultaneously to income tax and not redistributed, leads
> to a decrease of µ, i.e. to a wider distribution of wealth.** Only if a fraction
> `f_C > f_I φ_I/(1 + φ_I)` is redistributed will the capital tax be a truly social tax."*

Set that beside the sentence `ROADS-001` proposed for option C's abstract — *"a levy
contingent on the realised gain compresses a wealth distribution substantially more than a
proportional levy on the stock … that is counterintuitive, it reverses the standard
wealth-tax-is-stronger prior, and it is a fact about your model that as far as I can find
nobody has stated."* Bouchaud & Mézard stated it in 2000, more strongly (their stock levy can
*reverse sign*, not merely compress less), in closed form, with **the rebate fraction as an
explicit coordinate** — which is precisely the "fifth coordinate" `ROADS-001` §2 proposed to
introduce.

They also, separately, make the scaling-versus-truncation observation itself, about a
Lotka–Volterra variant: that variant *"has an additional term … which **breaks the symmetry
under wealth rescaling**, and as a consequence **the Pareto tail is truncated for large
wealths**."* Rescaling symmetry preserves the power law; breaking it truncates the tail. That
is `ROADS-001`'s organising principle, in their words.

### 4.2 · Benhabib, Bisin & Zhu (2011) — the `r = 1` claim is theirs too

*The Distribution of Wealth and Fiscal Policy in Economies With Finitely Lived Agents*,
**Econometrica 79(1), 123–157**, `doi:10.3982/ECTA8416` (read at source, NBER w14730 full
text). §4.1, verbatim:

> *"heavy tails in the stationary distribution require that the economy has sufficient capital
> income risk, with some γ_i > 1. Consider instead an economy with limited capital income risk,
> where γ_i < 1 for all i and where γ̄ is the upper bound of γ_n: **In this case it is
> straightforward to show that the stationary distribution of wealth would be bounded above**."*

`ROADS-001` calls our `r = 1` cap — the flow levy driving `ess-sup A = 0.9524 < 1`, so that no
power-law tail exists at all — *"the strongest claim and the one most likely to be wrong."* It
is not wrong. It is a special case of an aside that Econometrica printed in 2011 and called
**straightforward to show**. `WT-098`'s note on the card asked whether the `r = 1` cap needs
this search to be publishable under A: it does not need it, but it must now be **cited, not
claimed**.

Their **Proposition 4** is the third piece: *wealth inequality, measured by the tail Gini,
increases with a mean-preserving spread of the effective return process* — the general
statement that the **dispersion** of the multiplier, not its mean, sets tail inequality. Their
Proposition 3 has the tail index rising in both the estate tax and the capital income tax.

### 4.3 · What was NOT found, and is therefore where any residual novelty lives

Across the whole valid corpus, including all three surveys:

- **`NO_LOSS_OFFSET` is dark, 0 of 12.** Bouchaud & Mézard's income tax is `φ_I dW_i/dt`,
  applied **symmetrically to both signs** — an affine contraction of the multiplier toward 1.
  Our flow levy is on the **realised gain only**, `A − r·(A−1)⁺`, with **no loss offset**. That
  asymmetry is what makes ours a genuine *truncation* rather than a contraction, and it does
  not appear anywhere in the corpus.
- **No matched-*revenue* comparison.** Bouchaud & Mézard compare at equal *rates*; Guvenen et
  al. compare at equal revenue but route through reallocation across heterogeneous-productivity
  entrepreneurs to an **efficiency** conclusion, not through the multiplier to a **tail-index**
  one. Our κ-matched budget accounting is a different question from either.
- **Discrete Kesten recursion** with an explicit budget identity, versus their continuous-time
  mean-field Langevin.

**This is a narrow strip, and it must be described as a narrow strip.** It is not a thesis to
lead a paper with; it is at most a remark inside one, and the remark's first duty is to cite
Bouchaud & Mézard (2000) and Benhabib, Bisin & Zhu (2011).

---

## 5 · THE APPARATUS FAILED THREE TIMES BEFORE IT WORKED, AND THAT IS THE METHOD FINDING

Recorded because the verdict is only worth what the instrument is worth, and because two of the
three would have produced a **confident, clean, wrong** answer.

1. **v1's calibration limb was `sum(positive_controls) > 0`.** It returned `apparatus_valid:
   true` on **one** screened-in hit across four positive controls while **ten of fourteen** API
   calls had errored. A sum cannot distinguish *"every control fired"* from *"one fired and
   three silently failed."* Replaced with per-control scoring plus a **known-item tier**: twelve
   works named in advance, each searched by title, each checked for retrieval. A search
   apparatus that cannot retrieve a paper you *know* is there has zeros that mean nothing.

2. **The document-validity ceiling was testing my vocabulary, not the extraction.** It required
   the phrase *"tail index | Pareto exponent | …"* and voided four documents that had extracted
   perfectly at 100k–286k characters, merely because they write *"Pareto parameter."* Split into
   an **extraction** limb (function words), a **topic** limb, and a non-gating **dialect** probe.

3. **THE ONE THAT MATTERS. `TRUNCATION_x_TAIL` — the headline predicate — could not fire.**
   Every alternative in its regex contained the literal word *"tail"* or *"Pareto"*, so it was
   blind to the statistical-physics register, which says *"truncated power law"* and
   *"exponent µ"* and almost never *"tail."* It was dark across eleven economics full texts and
   **I was one step from writing that up as a clean absence.**

   What caught it was adding **predicate positive controls**: corpus members whose job is not to
   be evidence but to prove the predicate *can* fire. Sornette & Cont (1997) — a paper titled
   *"power laws and **truncated** power laws"* — left `TRUNCATION_x_TAIL` **dark**, and the
   summary line `predicates_proven_capable_of_firing: []` is what turned the session around.
   With the regex widened, the predicate fired on both controls, and then on Bouchaud & Mézard,
   who had the answer.

   > **A dark predicate is not evidence of absence until a document you know contains the thing
   > has made it fire.** A corpus-level ceiling (*"do my positive controls return papers?"*) and
   > a predicate-level ceiling (*"does my matcher fire on a paper that certainly contains it?"*)
   > are different instruments, and only the second one found this.

4. A fourth, minor and worth the line: `NO_LOSS_OFFSET` initially fired on Boar & Midrigan and
   Piketty & Saez entirely via the mathematician's idiom **"without loss of generality."** A
   predicate that matches boilerplate manufactures its own positives, which is worse than a dark
   one — it makes a corpus look covered.

---

## 6 · THE HOLE IN THIS SEARCH, NAMED

**Bastani & Waldenström (2023),** *Taxing the wealthy: the choice between wealth and capital
income taxation*, *Oxford Review of Economic Policy* **39**(3), 604–616,
`doi:10.1093/oxrep/grad030` — **could not be full-texted.** It is the one survey whose entire
subject is this policy pair. Routes attempted: IFN working-paper server (404), the DiVA
repository copy (robots-disallowed to this session's fetcher), publisher (paywalled).

Per `REFERENCE-POLICY` §4 it is therefore **✓◐** — bibliographically verified, not read at
source, and **it contributes nothing to the absence claim in §4.3**, because an abstract cannot
establish an absence. Its abstract does show the paper's frame is empirical and administrative
(Swedish register data, unrealised gains, presumed returns, liquidity, business-asset
exemptions) rather than random-growth-theoretic, which *lowers* the risk that it hides the
result without eliminating it. **A future session with library access should close this.**
It does not change the verdict, which rests on Bouchaud & Mézard read in full.

---

## 7 · WHAT THIS CHANGES

- **`DECISION-001` stays ticked at A.** The re-allocation test has run and returned KNOWN. C
  does not get re-opened; the price is now known and it is "someone else's result."
- **Paper II acquires two mandatory citations**, not optional ones: **Bouchaud & Mézard (2000)**
  wherever the stock-versus-flow tail contrast is made, and **Benhabib, Bisin & Zhu (2011)**
  wherever the `r = 1` cap or the bounded-multiplier claim appears. Card filed.
- **`ROADS-001` needs a tick recording that its §"what I could not check and you should" has now
  been checked, and came back KNOWN.** It should not be read again as a live proposal.
- **`REFERENCE-POLICY` gets a new §** on the predicate-level ceiling — §3's five passes are all
  about a *reference*, and none of them asks whether the *instrument that found (or missed) it*
  could fire. That is a sixth pass, and it belongs in the portable document.

---

## 8 · REFERENCES

Marks per `REFERENCE-POLICY` §4.

- **✓⧗** Bouchaud, J.-P., & Mézard, M. (2000). Wealth condensation in a simple model of economy.
  *Physica A: Statistical Mechanics and its Applications*, **282**(3–4), 536–545.
  `doi:10.1016/S0378-4371(00)00205-3`. *Consulted: arXiv `cond-mat/0002374` (2000-02-24), read
  in full. Quotations in §4.1 are attributed to that preprint and may not appear verbatim in the
  article of record. Consulted 2026-08-17 / published 2000.*
- **✓⧗** Benhabib, J., Bisin, A., & Zhu, S. (2011). The Distribution of Wealth and Fiscal Policy
  in Economies With Finitely Lived Agents. *Econometrica*, **79**(1), 123–157.
  `doi:10.3982/ECTA8416`. *Consulted: NBER Working Paper 14730 full text, read in full.
  Quotation in §4.2 attributed to that version. Consulted 2026-08-17 / published 2011.*
- **✓⧗** Sornette, D., & Cont, R. (1997). Convergent multiplicative processes repelled from
  zero: power laws and truncated power laws. *Journal de Physique I*, **7**(3), 431–444.
  *Consulted: arXiv `cond-mat/9609074`. Used here as a predicate control, not as evidence.*
- **✓⧗** Guvenen, F., Kambourov, G., Kuruşçu, B., Ocampo, S., & Chen, D. Use It or Lose It:
  Efficiency Gains from Wealth Taxation. *Consulted: NBER Working Paper 26284 full text.*
- **✓◐** Bastani, S., & Waldenström, D. (2023). Taxing the wealthy: the choice between wealth
  and capital income taxation. *Oxford Review of Economic Policy*, **39**(3), 604–616.
  `doi:10.1093/oxrep/grad030`. *Not read at source — see §6. No claim is made of its contents
  beyond what its own abstract states, and it carries no weight in any absence claim here.*

Full corpus, per-document predicate results and every retrieved window:
`/tmp/wt118-absence.json`, regenerable by `python3 scripts/wt118_fulltext_absence.py`.
