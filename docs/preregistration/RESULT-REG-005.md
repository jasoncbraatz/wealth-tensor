# RESULT-REG-005 · the shape is identified, and the price of admission is four significant figures

- **Registration:** `REG-005-p3-lag-shape-identifiability.md`, commit **6f0e7be**, 2026-08-12 —
  committed and pushed before a line of `wt091` was written.
- **Instrument:** `scripts/wt091_lag_shape_identifiability.py`. **11 severe · 1 definitional ·
  0 vacuous.** Inputs: RESULT-REG-003's `k̂ = 1.21`, `q̂ = 0.921342` and its profile interval width
  0.150. **Nothing was collected. No EDGAR access. No re-fit.**
- **Verdict, the falsifiers:** **F1, F2, F3, F4 all pass.**
- **Verdict, the ladders:** **I3 · P3 · W2 · S3 · N1.** **Two registered predictions failed** — I2
  and W4 — and they failed in the same direction.

---

## 1 · The count §4.2 takes, taken again

§4.2 proves an impossibility by counting: four observable numbers against five parameters, with the
shortfall landing on φ. That count assumed a constant recognition hazard. REG-004 replaced the
constant hazard with an arbitrary lag distribution `T ≥ 1` — not one more parameter but an
**infinite-dimensional** object — and REG-005 asks whether the extra structure leaves a trace.

**It leaves a trace and the trace has a size.** The best admissible constant-hazard world reproduces
the measured world's reported series to **3.9 × 10⁻⁴ per quarter** over forty quarters at a ten-year
life, and to **4.1 × 10⁻³** at a three-year one — **ladder I3**, against a registered prediction of
I2. That single number is the operative one in the whole file: **it is the precision a reported
series must carry to reject the constant hazard at all.**

The measurement is made in §4.2's **favourable** setting, registered as such in REG-005 §1: the
books open square and the physical scale is granted, which is exactly what §4.2 says a firm-level
series does not supply. A null result would therefore have held *a fortiori*; the result is positive
and carries the condition that the asset is followed from acquisition.

**The best mimic is an economically admissible firm at every one of the twenty settings swept.**
REG-005 §3's third question registered the opposite worry — that an unconstrained optimiser would
wander to φ > 1 and the admissible box, rather than the data, would separate the two worlds. The
free-φ and box-constrained optima are identical to every digit reported at all twenty settings, so
nothing here is an artefact of the constraint.

## 2 · The shapes a series of given precision cannot separate · **W2**

| precision | shapes indistinguishable from k̂ = 1.21 | width | against REG-003's 0.150 |
|---|---|---|---|
| 10⁻⁶ | 1.21 alone | 0.00 | — |
| **10⁻⁴** | **[1.16, 1.26]** | **0.100** | **0.67 ×** |
| 10⁻³ | [0.60, 1.87] | 1.27 | 8.47 × |
| 10⁻² | the whole registered sweep | ≥ 1.40 | ≥ 9.33 × |

**Ladder W = W2 at 8.47, against a registered prediction of W4.** The lower two rows run into the
boundary of the registered sweep [0.6, 2.0], so their widths are **lower bounds**; an unregistered
robustness sweep on [0.2, 3.0] — reported, labelled, and unable to change a verdict per REG-005 §7 —
puts the 10⁻³ interval at [0.50, 1.86], width 1.36, **9.07 ×**, and the ladder is unchanged.

The search's own floor at the true shape is **2.7 × 10⁻⁸**, thirty-seven times below the finest
tolerance in the grid, so the first row measures the model rather than the optimiser.

**At one part in ten thousand the reported series is a better instrument for the shape than the
event dates are** — 0.100 against RESULT-REG-003's 0.150 from hand-collected impairment lags. At one
part in a thousand it is an order of magnitude worse. The identification is real and it is
expensive.

**And what is inside the interval matters more than its width.** At 10⁻³ the set reaches **k = 0.50**
— a *decreasing* hazard, which by §4.9's tail condition admits **no steady-state deferral measure at
any positive decay rate**, its generating function diverging inside the disc the transform is
evaluated on. A series matched to a tenth of a per cent per quarter **cannot separate the world in
which this model is well-posed from one in which it has no steady state at all.** That is a sharper
limit than any width, and it is what REG-003's interval [1.135, 1.285] was buying.

## 3 · The identified set and the estimator answer different questions · **N1**

The widths of §2 are deterministic and worst-case: every shape that *could* have produced the
series. Ladder N asks the statistical question instead — 200 draws, seed `20260812` recorded, the
shape fitted jointly with the other three parameters on a series carrying independent relative noise:

| noise | median k̂ | interquartile range | on the sweep boundary |
|---|---|---|---|
| 10⁻⁴ | 1.210 | 0.0122 | 0% |
| **10⁻³** | **1.211** | **0.125** | **0%** |
| 10⁻² | 1.153 | 1.189 | 34% |

**N1** at 10⁻³: an interquartile range of 0.125, *narrower* than the event-date interval. That is
not in tension with W's 8.47. Forty observations average independent noise down by about a factor of
six, and the estimator meets the identified set at the resulting effective tolerance rather than at
the raw one. At 10⁻² the estimator breaks, and the boundary pile-up is reported as a fraction rather
than as the quantiles of a censored distribution — which is what REG-005 §5 registered it would be.

## 4 · A longer series does not help, and the reason is where the information sits · **S3**

| window | interval at 10⁻³ | width |
|---|---|---|
| 20 quarters | [0.60, 2.00] | 1.40 |
| 40 quarters | [0.60, 1.86] | 1.26 |
| **80 quarters** | **[0.84, 1.82]** | **0.98** |
| 400 quarters | [0.68, 2.00] | 1.32 |

**Not monotone.** The narrowest window is **twenty years** and a hundred years is *worse* than ten.
Once the gap reaches its steady state each further quarter repeats a single number — the deferral
measure itself — so extending the window adds redundancy to an average and dilutes the transient
that carries the shape. Ladder **S3**: the width at 400 quarters is 1.06 times the width at 20,
against 4.47 for an `N^{−1/2}` rate. **This is an identification property, not a sample-size one.**

REG-005 §4 registered the residual metric as relative-per-point *and registered the reason*: under a
norm-relative metric a geometrically decaying series' late points carry almost no norm, so this
ladder would have landed on S3 by construction, having measured the decay of `C` rather than the
information in it. The metric was chosen so the ladder could have landed elsewhere. It did not.

## 5 · Three recognition rates, and where they part company · **P3**

| life | δ/yr | α̂ (event dates) | α_ser (series) | α_eff (deferral) | ser vs α̂ | ser vs α_eff |
|---|---|---|---|---|---|---|
| 40 y | 0.025 | 0.408 | 0.4383 | 0.4368 | 7.50% | **0.33%** |
| 20 y | 0.050 | 0.408 | 0.4385 | 0.4388 | 7.57% | **0.05%** |
| 10 y | 0.100 | 0.408 | 0.4388 | 0.4431 | 7.63% | 0.96% |
| 5 y | 0.200 | 0.408 | 0.4370 | 0.4538 | 7.18% | 3.72% |
| 3 y | 0.333 | 0.408 | 0.4037 | 0.4758 | **0.97%** | **15.14%** |

**P3**, as registered in advance. The series-matching constant is nearly flat at 0.438/yr across the
rectangle — the **reciprocal mean lag** `1/E[T] = 0.435/yr` to within a per cent — while α_eff rises
with δ because the transform weights the tail, and α̂ is the geometric maximum-likelihood summary of
the same sample. They agree to **five parts in ten thousand** at a twenty-year life and part company
at a three-year one, where they differ by **15.1%** and move in **opposite directions** from α̂.
Least squares on the series matches the mean; the transform matches the tail; the likelihood matches
the event dates. The near-coincidence of α_ser and α̂ at the three-year life is a crossing of two
curves moving in opposite directions and is not a mechanism.

## 6 · §4.2's exchange survives, forced rather than discovered

The mimic search returns the mirror pair `(α, δ, φ)` and `(δ, α, φδ/α)` at an **identical**
objective — recovered at machine distance in fourteen of the twenty settings — which it must, since
§4.2's theorem makes the two worlds one series and any third series is equidistant from both by
construction. What the mirror costs is the mimic's own parameters. At a forty-year life the set of
worlds fitting within one part in a million of the best spans **0.128 in each root and 0.577 in φ**.
**The best-fitting constant hazard is not a world. It is a pair, and φ inside it is as free as §4.2
says it is.**

## 7 · The four falsifiers, and the one that proves an erratum cannot bite

- **F1 · Nesting.** The general convolution reproduces §4.2's published closed form at a geometric
  lag to **1.9 × 10⁻¹⁵**, worst over five lives × four φ × three α.
- **F2 · Non-vacuity.** Given a series generated in a constant-hazard world, the search recovers the
  generating parameters or their exact §4.2 mirror to **6.6 × 10⁻⁷** at worst, from the deterministic
  64-point start grid alone.
- **F3 · The witness.** A `k = 0.5` world — no steady state at any positive decay rate — leaves
  **5.4 × 10⁻³**, a **14 ×** separation from the measured shape's **3.9 × 10⁻⁴** at the same life and
  the same φ. *(Against ladder I's worst cell, a different life and a different φ, the ratio is 1.3 ×;
  that comparison is printed and is not the one read, because a witness has to be judged against the
  world it stands in for.)*
- **F4 · The `T = 0` mass is a pure φ reparameterisation, proved rather than assumed.** The fitted
  Weibull places 7.87% of its mass at a lag `peak_onset` cannot produce. Conditioning on `T ≥ 1`
  divides the gap by `q̂` at every age and every date alike, and the gap is proportional to `(1 − φ)`,
  so the conditioning is absorbed exactly by `(1 − φ) → (1 − φ)/q̂`: the reported series moves by
  **4.8 × 10⁻¹⁶**. **REG-003's erratum, which bit REG-004 twice and on a second estimator, cannot
  bite the series at all.**

## 8 · And the erratum arrived a third time anyway, in the level rather than the series

**`α_eff` was recomputed from REG-003's two fitted constants and came back 6% high at every life** —
0.4646 against RESULT-REG-004 §5's published 0.4368 at a forty-year life, 6.4% high, and so on across the
rectangle. The cause is F4's own subject arriving from the other side. RESULT-REG-004 reported
`α_eff` on both the as-fitted and the `T ≥ 1` distributions and **prints the conditioned one**;
dropping the `T = 0` mass raises `E[T]` from 6.93 to 7.52 quarters and lowers `α_eff` by about a
sixteenth everywhere. **The series cannot see that conditioning at all — F4 proves it — and the level
sees it at 6%.** A downstream instrument recomputing `α_eff` from the same two constants therefore
gets the other curve, silently, and ladder P's entire right-hand column was wrong until it was
caught.

The repair is not a comment. `alpha_eff_annual` now takes the conditioning explicitly, defaults to
the curve the manuscript prints, prints **both** columns so nobody downstream repeats this, and is
guarded by a severe check that reproduces RESULT-REG-004 §5's five published values to `1e-4` — with
a witness that is the as-fitted curve failing that same check. **A constant recomputed from its
inputs is not the same object as a constant read from the table that published it**, and the
difference is invisible until something compares them.

## 9 · What may be claimed

**May be claimed.** That a constant-hazard world reproduces the measured world's reported series to
3.9 × 10⁻⁴ per quarter at a ten-year life and 4.1 × 10⁻³ at a three-year one; that a series accurate
to one part in ten thousand identifies the shape more tightly than the event dates do and one part in
a thousand does not; that the shapes indistinguishable at 10⁻³ include decreasing hazards, for which
the model has no steady state; that the informative window is about twenty years and a longer one is
worse; that the series-matching constant is the reciprocal mean lag and is a third quantity distinct
from α̂ and α_eff; and that the best-fitting constant hazard is a mirror pair rather than a world.

**May not be claimed.** That any of this bears on the empirical identifiability of **φ** beyond what
§4.2 already proves — this file adds the shape and does not revisit φ. That a positive result
transfers to a firm-level series: REG-005 §1 registered the normalisation as the generous one, and
the identification measured here is for an asset followed from acquisition. That the fitted lag
distribution transfers to classes PRE-002 does not cover. That anything here touches PRE-001;
REG-003 §7 ruled that out in writing before these numbers existed.

**And the two failed predictions are a result, not a preface.** REG-005 predicted I2 and W4 from the
density of rational lag distributions in lag space (Jorgenson, 1966) read with the meagreness of
finite-dimensional approximations to it (Sims, 1971) and the classical ill-conditioning of
exponential-sum fitting (Lanczos, 1956, as quantified by Varah, 1982). The measured residue is four
times larger than that reading allows and the interval is nine times the event-date interval rather
than a hundred. Approximation theory describes what a family can do in the limit; this is one
distribution over one horizon, and it leaves more behind than the general argument suggests.
