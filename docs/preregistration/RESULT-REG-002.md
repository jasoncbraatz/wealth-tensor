# RESULT-REG-002 · §4.4 on the observable pair

- **Registered:** 2026-08-12, `wealthTensor-14`, `REG-002`, pushed at `650fcd4` (E1–E6) and
  `8cf58d7` (E7) before `scripts/wt088_disclosed_ladder.py` existed.
- **Instrument:** `scripts/wt088_disclosed_ladder.py` — **14 severe · 0 definitional · 0 vacuous**.
- **Run log:** `RESULT-REG-002-run.log`.
- **Manuscript:** §4.4 replaced, §4.5 narrowed, §4.2 re-attributed, abstract and contribution 3
  updated, six rows added to the §7 survivals ledger. 124 tests pass. Coach ratchet unchanged at 6.

---

## 0 · The one-line result

**The inversion is not the general case; it is what the confound does at one corner of a region. The
region has a closed-form boundary, it is small, and every route from a published number to δ lands
outside it — three of them for different reasons.**

## 1 · The seven registered checks

| | registered question | measured | falsifier |
|---|---|---|---|
| **E1** | drop the durability ordering | mean τ **−0.414 → +0.318**; recovery 1.9% → **11.5%**; reversal 23.8% → **1.1%** | **mis-specified — see §2** |
| **E2** | where does the strict reversal break | **δ₃\* = 0.00789**, an 87-period half-life; the table assigns 0.002 | **FIRED** (< 0.010) |
| **E3** | lumpy at the same mean rate | deferral **1.303×** the closed form (se 0.002, 2,000 paths); δ-equivalent **0.0123** | conjecture held |
| **E4** | the disclosed-life rectangle | **0%** of it inside the model's domain at α = 0.05 | **VACUOUS — see §3** |
| **E5** | what governs the direction | logit slope **+1.58** (se 0.081, z = +19.5), crossover **0.611** | fitted, no threshold |
| **E6** | behaviour past δ = α | no steady state; growth at exactly log((1−α)/(1−δ)) per period | **FIRED** |
| **E7** | does the lag survival survive | **100% → 66.2%** (M = 2,000, se 0.011), 3.55 se below threshold | **FIRED** (< 0.70) |

## 2 · ERRATUM · E1's falsifier is defective, and the defect is the reusable part

REG-002 E1 reads: *"If mean τ ∈ (−0.10, +0.10), the inversion is a property of the assumed ordering
rather than of the confound, and §4.4's headline claim is downgraded."*

**That threshold is stated on an absolute value, and an absolute value cannot distinguish an effect
that vanished from one that changed sign.** The measured unordered mean is **+0.318** — far outside
the band — so the registered test *as literally written* returns "the inversion survives," which is
the exact opposite of what the number says. The number is unambiguous and the registration is wrong.

Recorded rather than rewritten, per WT-052. The lesson generalises past this run:

> **A falsifier stated on |x| cannot tell a dead effect from a reversed one.** State the threshold
> on the signed quantity, or state two thresholds. The symmetric band feels conservative — it looks
> like it is guarding both directions — and it is in fact the one form that is blind to the most
> interesting outcome a directional hypothesis has.

**The correct reading**, on the signed quantity the falsifier should have named: without the
durability ordering the inversion is not weakened, it is **absent**. The design's own term is then
the only systematic force in the ladder and the ranking runs, on average, the way it was built to.
What survives without the ordering is a different and smaller claim — that δ *dispersion alone*
destroys the ranking, recovery falling from 100.0% at a common δ to 11.5% — and §4.4 now makes that
claim rather than the one the ordering was carrying.

## 3 · E4's falsifier is vacuous at the paper's own calibration, and that is the bigger finding

REG-002 E4 asks what fraction of the **admissible** disclosed rectangle sees the first rung rise. At
α = 0.05 the admissible rectangle is **empty**: every useful life short enough to appear in a filing
implies a decay rate at or above the recognition rate, and R is undefined there. A share of an empty
set is not a pass and not a failure, and reporting "does not fire" would have been a phantom tag at
section scale.

**E6 was registered as a boundary check on a corner of the parameter space. It is not a corner. It
is where the disclosed numbers all live.** Half the rectangle becomes admissible only at α ≈ 0.19
and all of it above α = 0.33, against the 0.05 calibrated here.

The rung question was then re-asked at an α for which it has a domain (α = 0.35): **the first rung
rises in 99.7%** of the rectangle. That substitution is labelled in the script, in the manuscript
and here as an **extension of** REG-002 E4 rather than as the registered test.

## 4 · What changed in the paper, and what deliberately did not

**Changed.** §4.4's heading and its entire closing third; §4.5's 100% figure now carries its
unordered companion; §4.2's Bellman & Åström attribution narrowed to the transfer-function
definition, which is what a reader can check (nothing readable in the source puts the unordered-pair
statement in their mouths — the same shape as the Kuan adjective, caught before a referee could).

**Not changed, deliberately.** §4.2's Bateman/Nerlove concession. §4.5's withdrawal of the
"PRE-001 was doomed by the φδ confound" claim — E7 narrows the *margin* of the lag statistic's
survival and does not restore that claim; 66.2% against 11.5% is still a factor of six. §4.6, §4.7
and §4.8 are untouched.

**Deleted rather than added to.** The ten-line "the ladder is an assumption" paragraph, replaced by
five positive results with numbers in their own units; and a clause in §4.5 narrating the paper's
own draft history, which is conduct narration and belongs here rather than in the manuscript
(charter §3.3). The additions are paid for by the deletions: the coach ratchet is unchanged at 6.

## 5 · Three tests that should have existed already

§4.4 publishes two closed forms and a domain restriction. None had a test. Added to
`tests/test_lag.py`:

- the crossing rate δ₃\* = Kα/(1 + K), verified against bisection which knows nothing about the
  algebra;
- the first-rung boundary δ₁ < αδ₀/(2α − δ₀), asserted to track the measure itself at six rates
  rather than only at the published one;
- the domain restriction — and writing it surfaced something the run had not: **convergence to the
  closed form slows without bound as δ → α.** At δ = 0.045 the 400-period gap ratio is still 11%
  short of its own limit, which is why §4.3's transient bound is quoted for the tabulated ladder and
  not near the pole. Past the pole the growth rate is exactly log((1 − α)/(1 − δ)) per period,
  pinned at δ = 0.051 and 0.060 only: by δ = 0.100 the ratio reaches 10⁹⁴ by period 4,000 and a
  longer check would be measuring float64's exponent range rather than the model.
