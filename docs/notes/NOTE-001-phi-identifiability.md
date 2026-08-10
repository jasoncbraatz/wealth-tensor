# NOTE-001 · φ is confounded with d, and that — not compute — is what blocks measuring it

- **Status:** exploratory finding on **synthetic data**. Not a result. Not citable as support for
  anything. Produced 2026-08-10, session wealthTensor-04.
- **Provenance:** `scripts/prototypes/bench_lag_torch.py` and `bench_identify.py`. Read
  `scripts/prototypes/README.md` first — it carries the **WT-052 declaration** that governs how
  this material may be used by a future pre-registration.
- **Why it exists:** Jason asked a hardware question — *will a 3090 do the lift, or should we rent
  GPU time?* The honest answer required characterising the workload, and characterising the
  workload turned up something considerably more useful than the answer to the question.

---

## 1 · The question that was asked, answered

**No GPU is needed, and for this workload a CPU is the *better* device.** Measured on a 2-core
2.8 GHz Xeon — deliberately the weakest machine available, so these are upper bounds:

| firms (batched) | forward | forward + backward |
|---|---|---|
| 1 | 6.7 ms | 30 ms |
| 100 | 7.0 ms | 30 ms |
| 10,000 | 80 ms | 323 ms |
| 100,000 | 669 ms | 3.5 s |

Two things to read off it.

**The batch dimension is free until it is wide.** One firm and one hundred firms cost identical
wall clock, because the cost is 400 *sequential* steps, not arithmetic. The recursion is
latency-bound, which is the regime in which a GPU helps least: kernel-launch overhead would
dominate, and a port could plausibly come out slower.

**float64 is free on CPU.** 6.7 ms fp64 against 7.5 ms fp32 — no penalty, within noise. A consumer
Ampere card (RTX 3090) runs fp64 at roughly 1/64 of its fp32 rate. Since this programme checks
closed forms to 10⁻¹⁵ (see WT-053's D(φ) = (1−φ)·D(0) result), double precision is the working
default, and that alone rules out the consumer GPU as an upgrade path. A full fit — 10,000 firms
simultaneously, 300 Adam steps, float64 — completed in **76 seconds** on the weak box.

**Trigger condition for revisiting this**, so it is not re-decided from scratch: rent compute when
a single fit exceeds ~30 minutes *and* more than ~20 of them are needed, or when a batch genuinely
will not fit in memory. Neither is close. Of the accounts already held, **HF Jobs** (`hf jobs uv
run --flavor a100-large --timeout 6h`) is the right shape and gives real fp64; HF **ZeroGPU** is
the wrong shape (60 s per call, Gradio-only); **DeepInfra GPU instances** work (SSH, own Docker,
hourly) but the B200 class is wildly oversized for this.

## 2 · The finding that matters

The fit in §1 ran fast **and recovered φ badly** — median absolute error **0.20** against a true
range of 0.1–0.9. Three checks isolate the cause.

| check | result | reading |
|---|---|---|
| Fit the **noise-free** series | error **0.211** | It is **not** the noise. |
| **Pin d** at its true value, fit φ and α only | error **0.00073** | It is **entirely** the confound with d. A 280× improvement. |
| Bucket the error by the firm's true d (d free) | 0.468 at d ∈ [0.005, 0.017] → **0.017** at d ∈ [0.025, 0.035] | Conditioning scales hard with d — 27× across a 3× change. |

**The algebra says exactly why.** Substituting ΔE = −d·E(t) into the two recursions collapses them
to a single line:

> **C(t+1) = C(t)·(1 − α) + E(t)·(α − φd)**,  E(t) = E₀(1 − d)ᵗ

**φ enters the observed series only through the product φd.** What the data can identify is α, d,
and the composite k = (α − φd). Recovering the parameter of interest therefore means

> **φ = (α − k) / d**

— a division by d. The estimator's variance grows as d → 0, and for the warehouse-retail sketch
(d = 0.01) the divisor is a hundredth.

**But the confound, not the decay rate, is the binding constraint.** With d pinned externally, φ
recovers to ~10⁻³ *even at d = 0.01*:

| d, pinned at truth | φ median abs err | p90 |
|---|---|---|
| 0.01 (warehouse retail) | 0.00122 | 0.12262 |
| 0.05 (industrial) | 0.00031 | 0.00105 |
| 0.20 (software) | 0.00020 | 0.00053 |

## 3 · What this implies for REVIEW-001 F11

F11 is the open item asking whether λ's shape prediction can be made to forbid anything while φ, α
and θ are swept rather than measured. This note narrows it sharply:

**To measure φ, acquire an independent estimate of d. Nothing else is blocking.**

Candidate sources for d, none of them requiring a GPU: depreciation schedules and useful-life
assumptions in the filings themselves; asset-life tables; capex replacement cycles; industry
engineering data on physical asset degradation. That is a **data-acquisition** problem in the
costume of a compute problem, and it is a far cheaper one.

There is also a pleasing self-reference in it, and the paper may eventually want to say so: **to
measure the observability of degradation, one must observe the degradation from somewhere the
reporting layer is not.** φ cannot be recovered from the reported series alone without the physical
series it is defined against.

## 4 · What this is NOT — read before citing it anywhere

- **It is synthetic.** No real firm data was used, by design (see the WT-052 declaration).
- **It uses a different estimator from PRE-001/PRE-002.** Those tested a *rank ordering of lags by
  tier*, non-parametrically. This fits a parametric model. **It therefore explains nothing about
  their null and may not be offered as an account of it.** RESULT-002 §4's discipline applies in
  full: everything here arrived after that number.
- **One tempting conjecture is deliberately left undeveloped.** The PRE-001/002 pilot universe was
  retail — the lowest-d sketch in the model, and hence the worst-conditioned sector for identifying
  φ. That observation is *post-hoc, about a different estimator, and on synthetic data*. It is
  written down so the next person has the map, **not** because it rescues anything. Any test of it
  registers from scratch, states its bridge proposition (WT-049), and obeys WT-052.
- **No free parameter has been added.** d was always in the model (`entropy_rate` net of
  `maintenance_ratio`). This note proposes *measuring* it, not introducing it.
