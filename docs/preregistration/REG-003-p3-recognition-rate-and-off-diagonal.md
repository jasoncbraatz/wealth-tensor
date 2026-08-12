# REG-003 · Empirical registration · the recognition rate α, and the off-diagonal

- **Status:** REGISTERED — committed and pushed before any line of `wt089` was written and before
  any statistic in it was computed. WT-052.
- **Registered:** 2026-08-12, session `wealthTensor-15`.
- **Series:** `REG-*`. **Unlike REG-001 and REG-002, this one is a claim about the world**, not
  about our own arithmetic. It runs on the PRE-002 event sample and it can fail against EDGAR.
  Results from it may be cited empirically, subject to §7's stopping rules.
- **Instrument to be written after this file is pushed:** `scripts/wt089_recognition_and_offdiagonal.py`.
- **Sample rebuild, already running when this was written:** `harvest.py` re-derives the PRE-002
  event table from EDGAR because the original lived in a dead container's cache. It re-runs
  `edgar.py` — the pre-registration — **unmodified**, and computes none of the statistics below.
  §2 fixes the reconciliation rule in advance, because the rebuilt count is not yet known.

---

## 1 · What is being registered, and why both halves are one file

Two questions, one sample, so one registration. Splitting them would let a second registration be
written after the first one's numbers arrived, on data the second had already seen.

**The recognition rate α is Paper III's only unestimated parameter, and §4.4 now says so in print.**
`wt088` closed §4.4 by establishing that the deferral measure **R = (1 − φ)δ/(α − δ)** exists only
where α > δ, and that at the paper's calibrated **α = 0.05 no disclosed useful life short enough to
appear in a filing satisfies that**: half the disclosed rectangle needs α ≈ 0.19, all of it α > 0.33.
α was never estimated. It was chosen. The section's domain sentence — a positive claim, in print —
rests on a number nobody has measured.

α is *the rate at which a deferred loss gets recognised*. The PRE-002 sample measures exactly that
quantity, once per event: the interval from the onset of deterioration to the impairment charge,
right-censored at twenty quarters. It was collected to test a **gradient across classes** and found
none. **It was never asked for its level**, and the level is what §4.4 needs.

**The off-diagonal is Paper III's Limitation 9 and the largest unclaimed thing in the corpus.**
The paper treats the four GAAP classes as separate ladders. If impairments co-occur across classes
within a firm-quarter more (or less) than independence predicts, the classes are not separate
draws, and every statistic in §5 that treats 688 events as independent — including the permutation
control and the power table — has an effective sample smaller than its nominal one. §9's second
numbered limitation already concedes the *within-firm* version of this. The *across-class* version
is unmeasured.

Neither question needs an observability proxy, a φ-to-GAAP bridge, or new data.

## 2 · The sample, and the reconciliation rule — fixed before the rebuilt count is known

The registered sample is PRE-002's: SEC Financial Statement Data Set registrants, SIC 5200–5999
(pilot, retail trade) and SIC 7370–7379 (replication, computer and data processing services),
2013–2024, built from historical `sub.txt` so that firms which stopped filing are retained.
Events are extracted by `edgar.py` at `onset_rule="peak"`, `signal="revenue"`, materiality floor
1% of prior total assets, twenty-quarter lookback. **RESULT-002 reports 688 events across 311
firms: 244/121 pilot, 444/190 replication.**

`companyfacts` is a live endpoint serving each firm's *latest* view of its own history. A pull in
August 2026 is not the pull of 2026-08-05: restatements land, tags get re-mapped, and firms
deregister. **The rebuilt count will therefore differ from 688, and the size of the difference is
not yet known to anyone.** Registered in advance:

- **Reported unconditionally:** rebuilt n, firms, per-tier counts and censored share against
  RESULT-002's table, plus the full drop accounting, whatever the agreement.
- **≥ 95% agreement in total n and no tier moving by more than 20% of its RESULT-002 count** →
  the rebuild is the registered sample. Proceed.
- **Below that** → the rebuild is a **new sample**, reported as such, and every result below is
  labelled as computed on a 2026-08 pull rather than on the sample RESULT-002 analysed. It is
  still analysed — a differently-composed sample is not a corrupt one — but it may not be
  described anywhere as *the* 688 events, and the discrepancy gets its own paragraph.
- **A rebuild that fails to produce a usable sample at all** (n < 200) → both instruments are
  reported as NOT RUN. No substitute sample, no widened SIC range, no second instrument. That is
  PRE-002 §5's stopping rule applied to its own data.

**No result below is conditioned on which branch fires.** The branch is chosen by a count that no
statistic in §§3–5 touches.

**A second, smaller pass is registered here too**, needed only by §4: for each firm that produced
at least one event, the set of quarters in which it is *eligible* — has both a revenue observation
and an assets denominator. This is the risk set the §4 null permutes within. It fetches only the
~300 firms with events, computes nothing, and is registered now so that it cannot later be tuned
to a null that behaves.

---

## 3 · INSTRUMENT A · the recognition rate

### 3.1 What is estimated

Per event: `lag` = q\* − onset in quarters, `censored` = the twenty-quarter lookback was reached
with the run still going, so the true lag is ≥ 20. This is a right-censored discrete duration
sample and α is its hazard.

**A1 · Constant-hazard (geometric) MLE, both universes pooled and each reported separately.**
With P(T = t) = α(1 − α)^t on t = 0, 1, 2, … and right-censored observations contributing
(1 − α)^c, the estimator is closed form:

> α̂_q = d / (d + S),  d = uncensored events,  S = Σ observed lags over **all** events
> se(α̂_q) = [ d/α̂² + S/(1 − α̂)² ]^(−1/2)

Annualised as **α̂_yr = 1 − (1 − α̂_q)⁴**, because §4.4's disclosed rectangle is built from useful
lives in years and δ there is per year. The unit conversion is registered here so it cannot be
chosen later to land on a side of a threshold.

**A2 · The shape, fitted and not assumed** (WT-080). A constant hazard is an assumption of the
*model*, not a fact about the data. Fit a discrete Weibull, S(t) = q^(t^k), by numerical MLE over
(q, k) with the same censoring contribution; report k̂ with a 95% profile-likelihood interval, and
report the non-parametric quarter-by-quarter hazard h_t = d_t / n_t for t = 0…19 beside it.

**A3 · Both universes, and the sensitivities PRE-002 registered**, run again here unchanged:
annual-attributed charges excluded; right-censored events excluded; one event per firm (largest
charge). Reported as a table of α̂_yr, never as a search for the version that clears a threshold.

### 3.2 The falsifier, stated as an exhaustive ladder rather than a threshold

§4.4 names three regimes of α, so a two-sided threshold would collapse two of them. **Which
outcomes does this threshold fail to separate?** — asked here, and answered by refusing to state a
threshold at all:

| regime | α̂_yr | what §4.4 must then say |
|---|---|---|
| **R1** | ≥ 0.33 | The entire disclosed rectangle is inside the model's domain. `wt088`'s domain restriction is an artefact of the calibration, and §4.4's first-rung result — the table wrong at its first step — becomes a live empirical claim rather than a conditional one. |
| **R2** | 0.19 ≤ α̂ < 0.33 | At least half the rectangle is admissible. The domain sentence stands but is much narrower than written, and the first-rung result holds over the admissible half. |
| **R3** | 0.05 < α̂ < 0.19 | Less than half admissible. The domain restriction is real and the calibration is too low; both statements are reported, and §4.4's sentence is corrected in its number, not in its direction. |
| **R4** | ≤ 0.05 | The calibration stands. §4.4's domain sentence stands exactly as written, and is now measured rather than assumed. |

The regimes are exhaustive, mutually exclusive, and stated on the **signed, unbounded** quantity.
There is no outcome for which the table returns nothing, and no pair of outcomes it cannot tell
apart. **Every one of the four is a publishable result and three of the four require §4.4 to be
edited.** That is the point: no cell of this table is the one we are hoping for.

### 3.3 Two biases, their direction registered before the number

**B1 · The sample is conditioned on a charge occurring.** A gap that opened and was never
recognised is invisible to EDGAR by construction — there is no filing for a thing that did not
happen. Conditioning on eventual recognition over-represents short lags. **α̂ is biased upward.**

**B2 · The onset bridge is PRE-002's and inherits PRE-002's doubt.** `peak_onset` dates the gap
from the firm's revenue peak. RESULT-002 §4(b) already names this bridge as the likeliest place
the conjunction broke. If revenue peaks *after* economic value has turned — the ordinary case for
a business whose customers have not yet left — the true interval is longer than the measured one.
**α̂ is biased upward again.**

**Both biases run in the paper-flattering direction, and that asymmetry is registered now so that
it cannot be discovered after the fact:**

> **A low α̂ is strong evidence; a high α̂ is weak.** If α̂_yr lands in R3 or R4, the two known
> biases were working against that finding and it survives them. If it lands in R1 or R2, the
> finding is exactly what two upward biases would manufacture, and it must be reported with that
> sentence attached, in the same paragraph, not in a limitations section.

**Is the set non-empty?** α̂ requires d > 0 (at least one uncensored event). RESULT-002 reports
censoring at 7.8% and 14.2%, so d is ~86–92% of n; but the check is registered explicitly rather
than assumed, because it is the E4 failure in its general form. **If d = 0 in any cell of the
sensitivity table, that cell is reported as UNDEFINED and never as a number.**

## 4 · INSTRUMENT B · the off-diagonal

### 4.1 The unit and the statistic

Unit: the **firm-quarter** (cik, q\*). A firm-quarter carries between one and four distinct tiers.

- **N_co** = the number of firm-quarters carrying **≥ 2 distinct tiers**. Primary statistic.
- **M[t, t′]** = the number of firm-quarters carrying both tier *t* and tier *t′*, for the six
  unordered pairs. This matrix, against its null expectation, **is** the off-diagonal.

Both are **counts**, never shares. **Is the set I am taking a share of guaranteed non-empty?** —
the set of co-occurring firm-quarters is *not* guaranteed non-empty, and a statistic defined as a
fraction of it would be undefined in precisely the most interesting case. A count of zero against
a positive null expectation is a strong, reportable finding; a share of zero is a division by zero
wearing a result's clothes. Registered as counts for that reason.

### 4.2 The null, and what it holds fixed

For each firm *f* and tier *t*, let n(f,t) be the number of distinct quarters in which *f* records
a tier-*t* event, and let Q(f) be *f*'s eligible-quarter set from §2's second pass. Under the null,
independently for each *t*, redraw n(f,t) quarters uniformly without replacement from Q(f).
Recompute N_co and M. **10,000 draws, seed 20260812, fixed here.**

This preserves every per-firm, per-tier marginal exactly — how often each firm impairs each class —
and destroys only the within-quarter alignment across classes, which is the thing under test. It
does not preserve the number of events per quarter, and must not: that is the quantity being
tested, and a null that fixes it tests nothing.

### 4.3 The falsifier, two-sided on purpose

**REGISTERED FALSIFIER.** Independence across classes within a firm-quarter is rejected when the
observed N_co falls outside the null's central 95% interval **in both universes, in the same
direction**.

**Which outcomes does this threshold fail to separate?** A one-sided test would fail to separate
independence from **anti-co-occurrence** — firms that impair goodwill systematically *not* touching
PP&E in the same quarter, which is what a "one bad quarter at a time" earnings-management pattern
would look like and is at least as interesting as clustering. It is stated two-sided, and the
**direction is reported as part of the result, never absorbed into a p-value**:

| outcome | what it means for the paper |
|---|---|
| N_co **above** the interval in both universes | Classes cluster. Limitation 9 is real and quantified; §5's independence assumption is violated in a stated direction, and the effective sample is smaller than 688 by a measured factor. |
| N_co **below** the interval in both universes | Classes are *dispersed* across quarters — a pattern independence does not predict either, and one that points at discretion in the timing of recognition rather than at the economics. Reported as its own finding, not as "independence rejected." |
| inside the interval in both universes | Independence is not rejected **at this power**, which is reported with it (§4.4 below). |
| the two universes **disagree in direction** | Reported as a failure to replicate, and neither direction is claimed. Retail and computer services were declared in advance precisely so this outcome would have a name. |

**Secondary, and labelled secondary:** the six pairwise cells with two-sided empirical p-values,
Holm-corrected across the six. The pairwise matrix is where the *interesting* structure would live
— goodwill with indefinite-lived intangibles is one economic story, goodwill with PP&E is another —
but with six cells and these counts it is descriptive, and it is registered as descriptive so that
a striking cell cannot be promoted to the headline after the fact.

### 4.4 Preconditions and power, registered because a null without detectability is not a result

- **Precondition.** If fewer than 20 firms across both universes ever record two distinct tiers in
  their entire history, the null's expectation of N_co is too small to reject anything, and the
  test is reported **INCONCLUSIVE — no power**, never as "independence holds." Checked and reported
  before the p-value, in the same output.
- **Power.** Synthetic: inject a known co-occurrence excess by, with probability π, moving one
  tier's quarter onto another tier's quarter within the same firm; report the detection rate at
  π = 0.05, 0.10, 0.20, 0.40 over 400 trials at the observed sample sizes. **Reported whether or
  not the primary test rejects.** If the primary does not reject and power at π = 0.20 is below
  0.80, the result is "not detected at this power," and the paper says that instead.

## 5 · COMPANION C · severity dispersion by class — descriptive, no falsifier

§4.7 claims identification strength is a property of the asset, and the natural test ranks the four
classes by realised return volatility and asset life. **Neither is in this sample.** Returns need
price data and disclosed lives need a filing scrape; both are new data, and this registration
promised none. Saying so is cheaper than a proxy that shares a name with σ and not its meaning —
which is the WT-038 error the project has already paid for twice.

What the sample *does* carry is `severity` = charge / prior total assets: the realised size of the
accumulated shock at the moment it is recognised. Reported **descriptively** — per-class median,
IQR, and the dispersion of log severity, with bootstrap intervals clustered by firm — as a first
look at whether the classes differ in shock size at all.

**No falsifier, no threshold, and no claim.** It is registered so that it exists in writing before
the numbers, and so that if a difference appears it is visibly a **question for a future
registration**, not a result this one may report. Nothing in §5 may be cited as support for
anything in §4.7.

## 6 · The discipline this registration is trying not to repeat

REG-002 §5 records two falsifiers that were themselves wrong, both visible at registration time for
one sentence each. Both questions were asked of every falsifier above, and both changed something:

- **Which outcomes does this threshold fail to separate?** → §3.2's binary threshold became a
  four-regime exhaustive ladder; §4.3's one-sided test became two-sided with the direction reported
  as part of the result.
- **Is the set I am taking a share of guaranteed non-empty?** → §4.1's statistic became a count
  rather than a share of co-occurring firm-quarters, and §3.3 registers the d = 0 check explicitly
  rather than assuming a censoring rate holds in every sensitivity cell.

## 7 · Stopping rules, and what does not follow from any of this

- **One pull, one run.** If the rebuild lands in §2's second branch, that is the sample. There is
  no third pull, no widened SIC range and no re-derivation under a different onset rule. A
  hypothesis that needs one on the same data is a hypothesis being fitted (PRE-002 §5).
- **α̂ is the recognition rate of the quantity PRE-002's instrument identifies**, under PRE-002's
  onset bridge. It is not "the" recognition rate of US GAAP, and no sentence anywhere may round it
  to that.
- **Rejecting independence in §4 does not rescue PRE-001.** A smaller effective sample widens
  PRE-002's confidence intervals; it does not move its point estimates, which were flat. Any
  attempt to read a co-occurrence finding as evidence that the lag gradient was there all along is
  ruled out here, in advance, in writing.
- **§4.4 gets edited by whatever §3 returns, in the direction §3.2's table specifies**, including
  the outcome where the section is left exactly as it is. §4.4 has been rewritten whole twice and
  is closed as an argument; this registration may change one number and the sentences that carry it,
  and may not reopen the argument.
