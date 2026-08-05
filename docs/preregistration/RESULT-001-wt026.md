# RESULT-001 · Outcome of PRE-001

- **Registration:** `PRE-001-wt026-observability-lag.md`, commit **9722342**, 2026-08-05.
- **Result computed:** 2026-08-05 (S3), from the code at the commit containing this file.
- **Verdict, pilot:** **THE PREDICTION FAILS.**
- **Verdict, replication:** **THE PREDICTION FAILS.**

---

## 1 · The result

**Pilot — retail trade, SIC 5200–5999.** 673 registrants that filed at any point 2013–2024,
672 with retrievable facts, **120 events across 72 firms.**

| tier | n | median lag (quarters) | IQR | mean |
|---|---|---|---|---|
| 0 · PP&E | 11 | **5.0** | 4.0–6.0 | 5.09 |
| 1 · finite-lived intangible | 12 | **3.0** | 3.0–3.2 | 3.33 |
| 2 · indefinite-lived intangible | 18 | **5.5** | 4.0–8.0 | 6.50 |
| 3 · goodwill | 79 | **4.0** | 3.0–7.0 | 5.15 |

Jonckheere–Terpstra **z = −0.177, p(one-sided) = 0.570.** Mann–Whitney tier 3 > tier 0
**p = 0.737.** median(t3) − median(t0) = **−1.0 quarters**, 95 % CI by firm bootstrap
[−3.0, +1.0].

Two of PRE-001 §7's three failure conditions are met independently: the trend test is not
significant in the predicted direction, **and** median lag for goodwill is *below* median lag for
PP&E. Tier counts of 11 and 79 clear the ≥10 threshold, so this is a **fail, not an
inconclusive.**

**Replication — computer and data processing services, SIC 7370–7379**, declared in PRE-001 §4.2
before the pilot ran and executed with only the SIC filter changed. 1,223 registrants,
**202 events across 106 firms.**

| tier | n | median lag | IQR | mean |
|---|---|---|---|---|
| 0 · PP&E | 13 | **3.0** | 2.0–4.0 | 3.46 |
| 1 · finite-lived intangible | 45 | **3.0** | 2.0–4.0 | 3.76 |
| 2 · indefinite-lived intangible | 17 | **5.0** | 3.0–8.0 | 6.12 |
| 3 · goodwill | 127 | **3.0** | 2.0–6.0 | 4.37 |

Jonckheere–Terpstra **z = +0.634, p = 0.263.** median(t3) − median(t0) = **0.0 quarters**,
CI [−1.0, +2.0]. Fails.

All four registered sensitivities in both universes are reported in the run logs. None reverses
the verdict; two are flagged INCONCLUSIVE on the underpowered rule rather than being allowed to
count.

**The framework predicted a monotone increasing gradient across the GAAP observability ladder.
It is not there.** The one consistent departure from flatness is in the *wrong shape* for the
prediction: tier 2, indefinite-lived intangibles, carries the longest median lag in **both**
universes (5.5 and 5.0), with goodwill below it. A ladder cannot be salvaged by the rung above
the top one behaving.

## 2 · Drop accounting (PRE-001 §9)

| bucket | pilot | replication |
|---|---|---|
| no_revenue_tag | 61 | 125 |
| insufficient_history | 180 | 361 |
| below_materiality | 909 | 591 |
| no_assets_denominator | 48 | 72 |
| **no_deterioration_run** | **373** | **674** |
| right_censored | **0** | **0** |
| ambiguous_tier | 57 | — |
| duplicate_restated_fact | 4,056 | — |
| firms with facts fetched | 672 | 1,222 |

`duplicate_restated_fact` counts **superseded facts replaced by a later filing**, not events
dropped. Restatement is routine and the pipeline takes the latest. The bucket name comes from
PRE-001 §9 and is left alone rather than renamed, because renaming a registered field to read
better is how registrations quietly become descriptions.

## 3 · What follows from this, and what does not

**What follows.** On US-listed retail and on computer services, over 2013–2024, using
firm-level revenue to date the onset of deterioration and XBRL impairment tags to date its
recognition, **there is no monotone relationship between the GAAP observability of an asset class
and the lag before its deterioration is recognised.** That is the claim PRE-001 made and it is not
supported.

**What does not follow.** That the two-layer model of `lag.py` is refuted. The model is about
*deterioration* and *recognition*; this test used two instruments for those, and the failure of a
test is the failure of a conjunction — the theory, the instrument, and the auxiliary assumptions
that connect them. Which link broke is not settled by the p-value. Quine–Duhem is the paper's own
stated caution (WT-025 §3) and it does not get to apply only when the result is inconvenient.

**Post-hoc, and labelled as such because it arrived after the number.** The instrument has a
range problem that the registration anticipated in direction and underestimated in size. PRE-001
§8.4 said revenue would cost *power rather than bias*. Observed:

- **Zero censoring in 320 events across two universes.** Not one reached the 20-quarter cap. If
  deferred degradation ran for years before a goodwill charge, some event should have hit it.
- **69 % of pilot lags are ≤ 6 quarters**, piled at 2–4, observed maximum 15 against a cap of 20.
- **1,047 material charges were discarded** across the two universes for having no qualifying
  run — three to five times the number retained.

An *unbroken* streak of year-over-year revenue declines is terminated by revenue volatility, not
by accounting recognition. All four tiers draw onset from the same revenue series, so the same
truncation applies to all four and compresses exactly the gradient under test. Worse, the
discards are not random: an event survived only if the firm happened to be in an unbroken
decline, which preferentially retains firms whose deterioration was **already visible** — the
opposite of the regime the hypothesis is about.

**This diagnosis does not rescue PRE-001 and is not offered as though it might.** It is a reason
to build a second instrument, registered separately as PRE-002, and to report whatever that one
says. A null with a known power problem is not support; it is a null with a known power problem,
and those two things being different is the only reason to say the second one out loud.

## 4 · The defect neither registration can fix

**The charge is asset-level; the deterioration signal is firm-level.** A goodwill impairment is
taken against one reporting unit. Consolidated revenue is the sum over all of them. A firm can
impair a failing division while total revenue rises, and 1,047 discarded charges are consistent
with exactly that.

This is the design's real limit and no re-run on the same data touches it. Fixing it needs
segment-level data, which is a different project with a different registration.

## 5 · Where this goes in the papers

Into **Paper III, Abandoned Approaches**, at full strength — not as a footnote and not
paraphrased into something softer. ADR-001 promoted that section to load-bearing in every paper
for a reason, and this is the reason: the audience is three children learning what it looks like
when you state a prediction in public, run it, and it does not come out.

The Odum question (WT-043) is unchanged by the direction of the answer. Emergy's fatal defect was
that it **never made a risky prediction at all**. This project has now made one, registered it
before looking, and lost. Losing a stated bet is a different epistemic position from never having
placed one, and it is the better of the two.

---

*Reproduce:*

```
python3 scripts/wt026_severe_test.py --universe pilot        # 120 events, JT z = -0.177
python3 scripts/wt026_severe_test.py --universe replication  # 202 events, JT z = +0.634
```
