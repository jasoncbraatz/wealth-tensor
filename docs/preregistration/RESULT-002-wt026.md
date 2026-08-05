# RESULT-002 · Outcome of PRE-002 · and the stopping rule fires

- **Registration:** `PRE-002-wt026-peak-to-charge.md`, commit **d655501**, 2026-08-05 — committed
  before this result existed, in the same commit that reported PRE-001's failure.
- **Verdict, pilot:** **THE PREDICTION FAILS.**
- **Verdict, replication:** **THE PREDICTION FAILS.**
- **Stopping rule (PRE-002 §5): FIRED.** WT-026 is recorded as **not supported by
  EDGAR-derived firm-level data.** This line of testing stops here.

---

## 1 · The result

**Pilot — retail trade, SIC 5200–5999.** 244 events across 121 firms (PRE-001 retained 120/72).

| tier | n | median lag | IQR | mean |
|---|---|---|---|---|
| 0 · PP&E | 21 | 5.0 | 3.0–9.0 | 7.05 |
| 1 · finite-lived intangible | 34 | 4.0 | 1.0–8.0 | 5.71 |
| 2 · indefinite-lived intangible | 34 | 5.5 | 1.2–9.0 | 6.12 |
| 3 · goodwill | 155 | 5.0 | 1.0–9.0 | 5.93 |

Jonckheere–Terpstra **z = −0.290**, normal p = 0.614, **empirical permutation p = 0.590**.
median(t3) − median(t0) = **0.0 quarters**, CI [−4.0, +2.0]. α = 0.025 (PRE-002 §4).

**Replication — computer and data processing services, SIC 7370–7379.** 444 events across
190 firms.

| tier | n | median lag | IQR | mean |
|---|---|---|---|---|
| 0 · PP&E | 34 | 5.0 | 1.2–9.8 | 6.62 |
| 1 · finite-lived intangible | 102 | 4.5 | 1.2–10.0 | 6.12 |
| 2 · indefinite-lived intangible | 46 | 6.0 | 2.2–11.0 | 6.85 |
| 3 · goodwill | 262 | 5.0 | 1.0–10.0 | 6.46 |

Jonckheere–Terpstra **z = −0.095**, normal p = 0.538, **empirical permutation p = 0.520**.
median(t3) − median(t0) = **0.0 quarters**, CI [−4.0, +2.5].

Four registered sensitivities per universe are in the run logs. None reverses the verdict.

## 2 · The instrument worked this time, and that is what makes the null bite

PRE-001's null came with a range problem. PRE-002's does not, and the registration required this
to be demonstrated rather than asserted:

| | PRE-001 (streak) | PRE-002 (peak) |
|---|---|---|
| events retained, both universes | 322 | **688** |
| charges discarded for no onset | **1,047** | **0** |
| right-censored | **0 %** | 7.8 % pilot, 14.2 % replication |
| pilot IQR width, tier 3 | 3.0–7.0 | 1.0–9.0 |

The lag distribution now spans the registered range instead of piling against a ceiling imposed
by revenue volatility, and censoring is non-zero, which is what an instrument capable of
observing long lags looks like.

**Negative control (PRE-002 §3).** Tier labels permuted 1,000 times with the lag distribution
held fixed:

| universe | null *z* mean | null *z* sd | observed *z* | empirical *p* |
|---|---|---|---|---|
| pilot | +0.007 | 1.025 | −0.290 | 0.590 |
| replication | −0.002 | 1.000 | −0.095 | 0.520 |

The permutation distribution is centred on zero with unit spread in both universes. The pipeline
does not manufacture a gradient, and the empirical p-values — which do not lean on the normal
approximation, and so do not care that the tier sizes are 21/34/34/155 — agree with the
parametric ones.

**Power (PRE-002 §3), reported because a null without its detectability attached is not a
result:**

| true effect | power, pilot | power, replication |
|---|---|---|
| 0.5 quarters per tier | 0.65 | 0.87 |
| **1.0 quarter per tier** | **0.95** | **1.00** |
| 2.0 quarters per tier | 1.00 | 1.00 |

**So: this design would have detected a one-quarter-per-tier gradient with 95 % probability in
retail and with certainty in computer services, and it found nothing.** That is not an absence of
evidence. That is evidence of absence, over the effect sizes the framework would need.

## 3 · What is now established, stated plainly

**The sharpest prediction this framework makes — that recognition lag scales with the
unobservability of degradation, with GAAP asset class supplying the observability ranking — is
not true of US-listed retail or computer services over 2013–2024.** It was registered before the
data were touched, tested twice with two instruments, replicated in a second sector declared in
advance, controlled against a permutation null, and it lost.

Per PRE-002 §5 the stopping rule fires. There is no third instrument. A hypothesis that needs one
on the same data is a hypothesis being fitted.

## 4 · Where the conjunction may have broken — post-hoc, and it does not count as evidence

*Everything in this section arrived after the number. None of it is support for anything, none of
it may be cited as a result, and any of it that is ever tested must be registered first, from
scratch. It is written down because the next person deserves the map, not because it rescues
anything.*

**(a) The theory may simply be wrong.** The reporting layer may not lag differentially by the
observability of what is degrading. This possibility is listed first on purpose. It is the one
the author has the strongest incentive to list last.

**(b) The bridge assumption may be wrong — and it is the same species of error as WT-038.**
PRE-001 mapped `lag.py`'s φ, the observability of *degradation*, onto the observability of the
*accounting treatment* — whether the asset carries an amortisation schedule. Those are different
quantities and may even be anti-correlated. Goodwill has no schedule, but its impairment is
triggered by conspicuously public signals: a share-price fall, a missed segment, a lost contract.
The physical condition of a distribution centre has a schedule, and is visible to essentially
nobody outside the firm. On that reading the ladder is not a φ gradient at all; it may be closer
to its inverse.

WT-038 diagnosed a type error — an axiom is a proposition, a model is a structure, and rewording
cannot promote one to the other. This is the same shape: **a quantity in the model was matched to
a quantity in the world that shares its name and not its meaning.** If that is what happened, the
lesson is not about accounting. It is that the bridge from a model's parameter to a measurable
was never itself written down as a proposition and checked.

**(c) The unit mismatch, already named in RESULT-001 §4 and unfixed by either registration.** The
charge is asset-level; the deterioration signal is firm-level. A firm can impair a failing
reporting unit while consolidated revenue rises. Fixing this needs segment-level data and is a
different project with a different registration.

**(b) and (c) are conjectures. (a) is a live possibility. The data do not distinguish them, and
this document does not pretend otherwise.**

## 5 · What this does to the project

**It does not touch Papers I or II.** They contain no empirical prediction; their results are
properties of stated models and are unaffected.

**Paper III changes, and honestly it gets better.** Three edits, none of them cosmetic:

1. **The severe test is reported as run and failed**, in the body and in the abstract — not
   buried in *Abandoned Approaches*, because a pre-registered failed prediction is a *result*, and
   filing it under abandonments would be the softest available way to hide it. *Abandoned
   Approaches* carries the PRE-001 instrument defect, which is a genuine methodological dead end.
2. **The lag-scaling claim is demoted from a prediction the framework makes to a prediction the
   framework made and lost at this level of aggregation.** Any surviving version must state its
   measurable and its bridge before it is tested again.
3. **§5, "what this does not settle", gains its strongest entry** — and the paper gains something
   most preprints in this space cannot buy: a registration, a public dataset, a null, and a
   stopping rule the author honoured while it still stung.

**On the Odum question (WT-043), which is the one that actually matters.** Emergy's fatal defect
was never that its predictions failed. It was that it *made none*, and so slid into closed
bookkeeping that could not lose. This framework registered a prediction in public, ran it against
public data, and lost. **The trap WT-043 identified is escaped by the act of betting, not by
winning the bet.** A theory that has lost a stated bet is falsifiable; that is the whole of the
difference, and it is not a consolation prize.

---

*Reproduce:*

```
python3 scripts/wt026_severe_test.py --universe pilot       --onset peak   # 244 events, z = -0.290
python3 scripts/wt026_severe_test.py --universe replication --onset peak   # 444 events, z = -0.095
```
