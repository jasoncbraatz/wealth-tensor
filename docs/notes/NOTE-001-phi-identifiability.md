# NOTE-001 · φ is ill-conditioned when estimated jointly with the decay rate — and that, not compute, is what blocks measuring it

- **Status:** exploratory finding on **synthetic data**. Not a result. Not citable as support for
  anything. Produced 2026-08-10, session wealthTensor-04. **Revised the same day** after an
  adversarial audit — see §5, which is the most instructive part of this file.
- **Provenance:** `scripts/prototypes/bench_lag_torch.py` and `bench_identify.py`. Read
  `scripts/prototypes/README.md` first — it carries the **WT-052 declaration** governing how this
  material may be used by a future pre-registration.
- **Why it exists:** Jason asked a hardware question — *will a 3090 do the lift, or should we rent
  GPU time?* Characterising the workload answered it and turned up something more useful.

## 0 · Notation, stated first because getting it wrong is what this note's first draft did

| symbol | meaning | `lag.py` |
|---|---|---|
| **d** | entropy rate | `entropy_rate` (0.05) |
| **m** | maintenance ratio | `maintenance_ratio` (0.6) |
| **δ** | **effective decay, δ = d(1 − m)** — what actually drives the recursion | 0.02 |

E(t+1) = E(t)·(1 − **δ**). The first draft of this note called δ "d", which understated a divisor
by a factor (1 − m) = 0.4 — in the *flattering* direction. See §5.

## 1 · The question that was asked, answered

**No GPU is needed, and for this workload a CPU is the better device.** Measured on a 2-core
2.8 GHz Xeon, deliberately weak so these are upper bounds:

| firms (batched) | forward | forward + backward |
|---|---|---|
| 1 | 6.7 ms | 30 ms |
| 100 | 7.0 ms | 30 ms |
| 10,000 | 80 ms | 323 ms |
| 100,000 | 669 ms | 3.5 s |

**The batch dimension is free until it is wide** — one firm and one hundred cost identical wall
clock, because the cost is 400 *sequential* steps. The recursion is latency-bound, the regime where
a GPU helps least. **And float64 is free on CPU** (6.7 ms fp64 vs 7.5 ms fp32), where a consumer
Ampere card runs fp64 at roughly 1/64 of fp32. Since this programme verifies closed forms to
10⁻¹⁵, double precision is the working default, which disqualifies the consumer GPU on *precision*,
not size.

A full fit — 10,000 firms, 300 Adam steps, float64 — took **76 s** on that box, and **12.4 s** on
darwin. **Trigger for revisiting:** rent when one fit exceeds ~30 min *and* more than ~20 are
needed. Nothing is close. Of the accounts already held, **HF Jobs** is the right shape and gives
real fp64; HF **ZeroGPU** is not (60 s/call, Gradio-only); **DeepInfra GPU instances** work but the
B200 class is wildly oversized.

## 2 · The finding

The fit ran fast and recovered φ **badly**. Substituting ΔE = −δ·E(t) collapses the two recursions:

> **C(t+1) = C(t)·(1 − α) + E(t)·(α − φδ)**,  E(t) = E₀(1 − δ)ᵗ

**φ reaches the observable only through the product φδ.** The series identifies α (from the
(1 − α) coefficient), δ (from the geometric rate of the driving term) and the composite
k = (α − φδ). So **φ = (α − k)/δ** — a division by δ, and the estimator's variance grows like 1/δ².

**Like-for-like** (identical batch B = 2000 and 400 Adam steps in both arms; φ ∈ [0.1, 0.9],
δ ∈ [0.005, 0.035]):

| arm | median abs err | p90 |
|---|---|---|
| δ estimated jointly (the reported layer alone) | **0.21140** | 0.64436 |
| δ pinned at its true value | **0.00073** | 0.01727 |
| noise-free, δ free | 0.21138 | 0.64434 |

**291× improvement in the median**, and the noise-free arm rules noise out as the explanation.

**This is a conditioning result, NOT non-identifiability.** φ stays identifiable in principle at
every δ > 0 and degrades continuously — no cliff:

| true δ | n | median | p90 |
|---|---|---|---|
| 0.005–0.010 | 324 | 0.468 | 0.773 |
| 0.010–0.017 | 502 | 0.468 | 0.727 |
| 0.017–0.025 | 522 | 0.164 | 0.462 |
| 0.025–0.035 | 652 | **0.017** | 0.212 |

At the top bucket the reported layer alone recovers φ to ~2% of its span. The headline 0.211 is
therefore characteristic of **slow-decaying assets**, not of the model generally — the swept δ
range sits mostly in the badly conditioned region.

**Pinning δ helps most where it is needed least.** At §4.2's sector sketches, converted to
effective decay (δ = d(1 − m), m = 0.6), δ pinned:

| sector | entropy rate d | δ | median | p90 |
|---|---|---|---|---|
| warehouse retail | 0.01 | 0.004 | 0.00433 | **0.191** |
| industrial | 0.05 | 0.020 | 0.00054 | 0.00367 |
| software | 0.20 | 0.080 | 0.00026 | 0.00078 |

Even in the best case, the slowest-decaying assets keep a bad tail.

## 3 · What this implies for REVIEW-001 F11

**A usable φ requires an independent determination of δ — and for the slowest-decaying assets, φ
may not be usefully recoverable even then.** Candidate sources for δ, none requiring a GPU:
depreciation schedules and useful-life assumptions in the filings; asset-life tables; capex
replacement cycles; engineering data on physical degradation. A **data-acquisition** problem in a
compute problem's costume.

There is a self-reference the paper may eventually want: **to measure the observability of
degradation, one must observe the degradation from somewhere the reporting layer is not.**

## 4 · What this is NOT — read before citing it anywhere

- **Synthetic.** No real firm data, by design (see the WT-052 declaration).
- **A different estimator from PRE-001/PRE-002**, which tested a *rank ordering of lags by tier*
  non-parametrically. This fits a parametric model. **It explains nothing about their null and may
  not be offered as an account of it.** RESULT-002 §4 applies in full.
- **One conjecture is deliberately left undeveloped.** The PRE-001/002 pilot universe was retail —
  the lowest-δ sketch, hence worst-conditioned for φ. Post-hoc, different estimator, synthetic.
  Written down for the map, not as a rescue. Any test registers from scratch, states its bridge
  proposition (WT-049), obeys WT-052.
- **No free parameter added.** δ was always in the model. This proposes *measuring* it.

## 5 · The audit that corrected this note, recorded because it is the useful part

The first draft made four errors, all caught by an adversarial agent re-checking the numbers
against the code, and **three of the four erred in the direction that flattered the finding**:

1. **The symbol collision.** It wrote the collapse as `α − φd` using `d`, while §4.1 uses `d` for
   the entropy rate — so the printed divisor was 2.5× too large and the conditioning looked
   *better* than it is. **This is the third instance of one symbol carrying two meanings in this
   project** — WT-049 (a model parameter and a measurable sharing a name), WT-055 (Λ vs λ), now
   this. The recurrence is the finding; the fix is cheap and the pattern is not.
2. **Cherry-picked best case.** "recovers to 0.0007 even at d = 0.01" spliced a mixed-δ median onto
   a low-δ claim. At δ = 0.004 the median is 0.00433 and the p90 is 0.191.
3. **Overclaimed "cannot be recovered."** It is conditioning, not non-identifiability, and the
   top δ bucket recovers φ perfectly usably from the reported layer alone.
4. **"The same fit"** compared two different scripts at different batch sizes and iteration
   budgets. The like-for-like pair is in §2 and gives 291×, not 277×.

**A second audit pass caught four more**, including that the paper credited two existing guard
tests to Limitation 4 when they guard section 4.2s closed form, and that Limitation 4s own
collapse had **no test at all**. It has one now:
`test_the_two_layer_recursion_collapses_to_the_form_limitation_4_publishes` (103 tests at head).
The others: a hardware timing attached to the wrong experiment after the like-for-like fix; p90s
dropped from the one sentence they undercut; and section 7 attributing tractability solely to
knowing delta, when magnitude of delta is an independent handle.

*A note on method.* The audit was run because the material was new, not because anything looked
wrong. Three of these four would have survived any amount of re-reading, because each was a
plausible sentence about a real number — the errors were in the *mapping* between them.
