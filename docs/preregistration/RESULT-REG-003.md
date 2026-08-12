# RESULT-REG-003 · the recognition rate, and the off-diagonal

- **Registration:** `REG-003-p3-recognition-rate-and-off-diagonal.md`, commit **b088cc8**,
  2026-08-12 — committed and pushed before a line of `wt089` was written.
- **Instrument:** `scripts/wt089_recognition_and_offdiagonal.py`. **10 severe · 0 definitional ·
  0 vacuous.** Sample: `data/pre-002-events.json`, risk sets `data/pre-002-riskset.json`.
- **Verdict, A:** **R1** — the recognition rate is an order of magnitude above the calibration,
  and the constant hazard the model assumes is **rejected**.
- **Verdict, B:** **independence across classes is rejected**, both universes, same direction.

---

## 1 · The sample rebuilt to within one per cent

The PRE-002 events existed only in a cloud container's cache, which died with the container.
`companyfacts` serves each firm's *latest* view of its own history, so REG-003 §2 fixed the
reconciliation rule before the rebuilt count was known.

| | RESULT-002 | rebuilt | Δ |
|---|---|---|---|
| events | 688 | **695** | +1.0% |
| firms, retail / computer services | 121 / 190 | **122 / 191** | +1 / +1 |
| tier 0 · PP&E | 55 | 55 | 0 |
| tier 1 · finite-lived intangible | 136 | 136 | 0 |
| tier 2 · indefinite-lived intangible | 80 | 81 | +1 |
| tier 3 · goodwill | 417 | 423 | +1.4% |
| censored share | 7.8% / 14.2% | 7.7% / 14.1% | — |

Agreement 99.0%, worst tier drift 1.4%; the registered rule admits this as **the registered
sample**. Three of four tier counts are identical to the event. The whole of the drift sits in
goodwill, which is where restatement and late tagging would put it.

**And the pooled firm count is 307, not 313, which is a small fact nobody had looked at.** The
universes are built from *historical* `sub.txt`, so a firm that changed SIC between 2013 and 2024
enters both. Six do: Live Ventures, Ubiquity, Right On Brands, Fortune Valley Treasures, IAC and
Match Group. It changes nothing in either universe's own test, which is internal to that universe —
but a **pooled** statistic, which §2 below computes, is pooling two sets that overlap in 2% of
their firms. RESULT-002 reported 121 and 190 and never a union, so the overlap was invisible rather
than absent. It is stated here so the next pooled statistic knows.

**The table is now committed** (`data/pre-002-events.json`, 695 rows), so no future session pays
the crawl again — twenty-five minutes and several gigabytes of transfer, for a table under a
megabyte. That it was ever a cache and never an artifact is the reusable half of this section.

## 2 · INSTRUMENT A · α = 0.408 per year, against a calibration of 0.05

Each event carries the interval from onset of deterioration to charge, right-censored at twenty
quarters. That is α's definition, measured once per event, by an instrument built to look at
something else entirely and which found nothing where it looked.

**Censored geometric MLE, α̂ = d/(d + S) as registered:**

| cut | n | d | α̂ per quarter | **α̂ per year** | 95% interval | regime |
|---|---|---|---|---|---|---|
| **pooled** | 695 | 613 | 0.1227 (se 0.0046) | **0.4077** | [0.383, 0.432] | **R1** |
| retail | 247 | 228 | 0.1323 (se 0.0082) | 0.4330 | [0.390, 0.474] | R1 |
| computer services | 448 | 385 | 0.1177 (se 0.0056) | 0.3940 | [0.363, 0.424] | R1 |
| annual-attributed excluded | 415 | 361 | — | 0.3970 | — | R1 |
| censored excluded | 613 | 613 | — | 0.4986 | — | R1 |
| one event per firm | 307 | 272 | — | 0.4129 | — | R1 |

**Unregistered robustness, reported as robustness and not as result.** Administratively censoring
at 8, 12 and 16 quarters instead of 20: 0.396, 0.398, 0.404. Dropping the 175 events charged one
quarter after the peak — the mass where the onset bridge is least credible: **0.327**. Fitting on
a support that starts at 1, since the sample contains no lag of zero: **0.460**.

**Every cut lands in R1. The range across all of them is 0.327 to 0.499 and no interval contains
0.05.** REG-003 §3.2's ladder is exhaustive, so this is a reading and not a survival.

**What it means for §4.4.** `wt088` established that R exists only where α > δ, and that at
α = 0.05 the entire disclosed rectangle lies outside the domain. At α̂ = 0.408 the entire rectangle
lies **inside** it — a three-year useful life implies δ = 0.333, still below the measured rate.
The domain restriction §4.4 reports is a property of the calibration, not of the disclosure, and
§4.4's first-rung result now holds at a measured rate rather than a hypothetical one.

### 2.1 · The shape was fitted, and it is not the model's shape

WT-080. A constant hazard is an assumption of the *model*; the data were asked.

**Discrete Weibull (Nakagawa–Osaki), P(T > t) = q^((t+1)^k): k̂ = 1.210, 95% profile-likelihood
interval [1.135, 1.285], which excludes 1.** Stable at k̂ = 1.205, 1.210, 1.285 under truncation at
16, 12 and 8 quarters, so it is not an artefact of a thin tail.

The non-parametric hazard shows the structure the single number hides:

| t (quarters) | 1 | 2 | 3 | 4 | 5 | 6–10 | 11–15 | 16–19 |
|---|---|---|---|---|---|---|---|---|
| hazard | **0.252** | 0.085 | 0.103 | 0.124 | 0.163 | 0.105–0.149 | 0.081–0.165 | 0.121–0.278 |

**Recognition is bimodal.** 175 of 695 events — a quarter of the sample — are charged one quarter
after the revenue peak. The remaining three quarters face a hazard rising from about 0.09 to about
0.25 over five years, and fitting them alone gives **k̂ = 1.70** [1.58, 1.83]. **The longer a gap
has been open, the likelier it is to close this quarter** — the opposite of the memorylessness a
single α encodes. α̂ is an average over a twenty-quarter window, not a constant of the technology.

### 2.2 · Three biases, all registered before the number

REG-003 §3.3 registered the direction of two, and the run found a third.

| | direction on α̂ | why |
|---|---|---|
| conditioning on a charge occurring | **up** | a gap never recognised leaves no filing |
| PRE-002's revenue-peak onset | **up** | if revenue peaks after value turns, the measured interval is short |
| no lag of zero in the sample | **down** | the registered support includes a mass the data cannot have |

The registered asymmetry: *a low α̂ is strong evidence, a high α̂ is weak.* This estimate is high,
so it is the reading two upward biases would manufacture — which is why the cut that removes the
mass those biases most affect matters. **Removing the 175 lag-one events gives 0.327: still an
order of magnitude above the calibration.** The finding does not rest on its most suspect quarter.

## 3 · INSTRUMENT B · the reporting layer is not diagonal

§9's ninth limitation states the assumption and names its own test. Taking each firm's per-class
impairment frequency as given and redrawing which of that firm's eligible quarters they land in —
10,000 draws, seed fixed in the registration:

| universe | firm-quarters | N_co observed | null mean | central 95% | obs/exp | two-sided *p* |
|---|---|---|---|---|---|---|
| retail | 215 | **30** | 7.3 | [3, 12] | **4.12×** | 0.0002 |
| computer services | 399 | **44** | 21.8 | [15, 29] | **2.02×** | 0.0002 |

Both above, both universes, same direction; *p* is at the floor 10,000 draws can report. The
precondition held with room — 93 firms record two or more distinct classes against a registered
minimum of 20 — and power against an injected excess is **1.00 at every level tested**, including
the smallest (5% of events moved).

**The six cells, Holm-corrected and registered as descriptive:**

| pair | retail obs/exp | computer services obs/exp |
|---|---|---|
| indefinite-lived intangible × goodwill | **5.83×** (p 0.0012) | 2.41× (p 0.0020) |
| finite-lived intangible × goodwill | 3.33× (p 0.0056) | **2.22×** (p 0.0012) |
| PP&E × goodwill | **4.35×** (p 0.0030) | **4.03×** (p 0.0090) |
| finite × indefinite intangible | 5.39× (p 0.0150) | 2.44× (p 0.0056) |
| PP&E × finite-lived intangible | 0 obs | 1.35× (n.s.) |
| PP&E × indefinite-lived intangible | 3.15× (n.s.) | 0 obs |

Property with goodwill is the one cell whose *magnitude* replicates across two unrelated sectors.
It is also the cell with the cleanest mechanical explanation, which is the next paragraph.

**The mechanical reading has to be excluded before the economic one is available, and the paper
named it before the test ran.** ASC 360 requires the recoverability screen on long-lived assets
*before* the goodwill test, so a single triggering event can produce two charges in one quarter by
the ordering of the standards rather than by any coupling of the assets. **This design cannot
separate those**, and a design that could would need the trigger disclosure, not the charge.
What is established is the magnitude of the departure from diagonality, previously unmeasured.

**What does not follow, ruled out in REG-003 §7 before the number existed:** a smaller effective
sample widens PRE-002's intervals; it does not move its point estimates, which were flat. This
result is not a rescue of PRE-001 and may not be cited as one.

## 4 · COMPANION C · descriptive, and it stays that way

Registered with no falsifier. Realised severity (charge / prior total assets), pooled:

| class | n | median | IQR | sd of log severity (firm-clustered 95%) |
|---|---|---|---|---|
| PP&E | 55 | 0.0292 | 0.0147–0.1089 | 1.990 [1.023, 2.953] |
| finite-lived intangible | 136 | 0.0606 | 0.0203–0.2307 | 1.424 [1.284, 1.556] |
| indefinite-lived intangible | 81 | 0.0473 | 0.0199–0.1324 | 1.236 [0.995, 1.486] |
| goodwill | 423 | 0.0773 | 0.0289–0.2009 | 1.513 [1.251, 1.820] |

The intervals overlap. Nothing here is cited anywhere, and §4.7's σ-and-lifetime claim remains
untested: realised return volatility and disclosed useful lives are not in this sample, and a
proxy that shares σ's name and not its meaning is the WT-038 error this project has paid for twice.

## 5 · ERRATA · what this registration got wrong

**One, and it is small.** REG-003 §3.1 registers the geometric on support {0, 1, 2, …}. The sample
contains **no lag of zero** — `peak_onset` dates the peak strictly before the charge quarter, so a
lag of zero is unreachable by construction. The registered estimator therefore places mass where
the instrument cannot produce an observation, and understates α̂ by about five annualised points.
It is reported at the registered specification, with the shifted figure given beside it as a
direction and not as a substitute.

**Generalising it, because that is the only reason to write an erratum down:** REG-003 asked *which
outcomes does this threshold fail to separate* and *is the set non-empty* — both about the
**falsifier**. Neither asks whether the **estimator's support matches the instrument's range.**
The question that would have caught this, in one sentence, at registration:

> **WHICH VALUES CAN THIS INSTRUMENT NOT PRODUCE, AND DOES MY ESTIMATOR ASSIGN THEM MASS?**

It costs nothing, it is checkable before any data arrive, and it is the third member of a family
whose first two members each cost a section-scale error in `-14`.
