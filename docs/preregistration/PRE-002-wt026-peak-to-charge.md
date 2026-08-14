# PRE-002 · Pre-registration · WT-026, second and final instrument

- **Status:** REGISTERED — committed before any PRE-002 statistic was computed.
- **Registered:** 2026-08-05 (S3), after PRE-001's result was computed, committed and reported.
- **Relationship to PRE-001:** **PRE-001 stands. It is not superseded, withdrawn or amended.**
  Its prediction failed on the retail pilot and that failure is reported at full strength in
  `RESULT-001` and in the ledger. This document is a **second test of the same hypothesis with a
  different instrument**, and it is registered as such so that nobody — including us — can later
  present it as though it were the first.
- **This is the last one.** See §5. A hypothesis that needs a third instrument is a hypothesis
  being fitted.

---

## 1 · Why a second instrument at all

PRE-001 §5.3 dated the onset of deterioration as the start of an **unbroken run** of
year-over-year quarterly revenue declines ending before the charge. PRE-001 §8.4 predicted, in
advance, that revenue would be an imperfect proxy and that the cost would be *power rather than
bias*.

The cost turned out to be larger than anticipated and the diagnosis is recorded post-hoc, which
is exactly why it does not get to rescue PRE-001:

- **373 material charges were dropped** for having no qualifying run, against 120 retained. Three
  quarters of the sample was discarded by the instrument.
- **Not one event of 120 reached the 20-quarter cap.** Zero censoring. If deferred deterioration
  really ran for years before a goodwill charge, some event should have hit the ceiling.
- **69 % of retained lags are ≤ 6 quarters**, piled at 2–4, with an observed maximum of 15.

An unbroken streak of YoY revenue declines is truncated by *revenue volatility*, not by
accounting recognition. All four tiers draw their onset from the same revenue series, so the same
truncation applies to all four — which compresses precisely the gradient under test. PRE-001
therefore tested a hypothesis about accounting recognition using an instrument whose range was
governed by something else.

**This does not make PRE-001's null uninformative, and we are not claiming that it does.** It
makes it a null with a known power problem. Those are different from each other and both are
different from support.

## 2 · The change, and only this change

**Onset is now the pre-charge peak, not the start of a streak.**

> **Primary.** For event (*i*, *T*, *q\**), let TTM(*q*) be trailing-twelve-month revenue, the
> sum of the four quarters ending at *q*. Onset *q₀* = **argmax** of TTM(*q*) over
> *q* ∈ [*q\** − 20, *q\** − 1]. **lag = q\* − q₀.**
>
> **Ties break toward the latest quarter achieving the maximum.** A flat TTM plateau means the
> firm was still at its high water mark throughout it, so deterioration began after the last of
> those quarters and not the first. The other tie-break would inflate every lag — that is, it
> would move every number in the direction that flatters the hypothesis, which is the one reason
> a tie-break must never be chosen.

Properties, stated before the result:

- **No truncation by noise.** A wobble no longer ends the measurement. The full 1–20 range is
  reachable, so the instrument can express the quantity the hypothesis is about.
- **No mass drop.** A firm peaking at *q\** − 1 yields lag 1 — a legitimate observation that the
  firm was still at its high water mark when it took the charge, not a discard. PRE-001's
  `no_deterioration_run` bucket disappears, and with it the selection it induced: under PRE-001
  an event survived only if the firm happened to be in an unbroken decline, which preferentially
  retained firms whose deterioration was *already visible* — the opposite of the regime the
  hypothesis is about.
- **Censoring becomes meaningful.** An argmax landing on the first quarter of the window is
  right-censored and is reported as such.

> **Secondary.** The same argmax on trailing-twelve-month **operating income with impairment
> charges added back** (`OperatingIncomeLoss` + the tier charges already extracted for that
> quarter). PRE-001 §5.1 rejected operating income because the charge contaminates it; adding the
> charge back removes that contamination, which was not available before the charges had been
> extracted. Reported alongside the primary, never in place of it.

**Requirement:** at least 8 quarters of TTM history before *q\**, else `insufficient_history`.

**Everything else is unchanged and is inherited from PRE-001 verbatim:** the tier ladder and its
GAAP justification, the XBRL tag sets, the 1 %-of-assets materiality floor, the 20-quarter cap,
the pilot and replication universes, the Jonckheere–Terpstra primary statistic, the
Mann–Whitney secondary, the by-firm bootstrap, the four sensitivities, and the full drop
accounting.

## 3 · Negative control — new, and required before the result is reportable

A null result is only worth reading if the pipeline is capable of finding a gradient at all, and a
positive result is only worth reading if the pipeline cannot manufacture one.

**Label permutation.** Tier labels are permuted at random across events 1,000 times, holding the
lag distribution fixed, and the Jonckheere–Terpstra statistic recomputed each time.

- The permutation distribution of *z* must be centred near 0 with standard deviation near 1. If it
  is not, the test statistic is mis-specified for this data and **no result from this pipeline is
  reportable**, in either direction.
- The observed *z* is additionally reported as an **empirical permutation p-value**, which does
  not rely on the normal approximation and is therefore the number to trust when the tier sizes
  are as unbalanced as they were in the pilot (11 / 12 / 18 / 79).

**Synthetic positive control.** The same statistic is run on synthetic events drawn with a known
1-quarter-per-tier gradient at the pilot's observed tier sizes and lag dispersion, to record what
effect size this design could have detected. **This is a power statement, computed as part of the
registration and reported whatever happens** — so that a null arrives with its own detectability
attached rather than as a bare absence.

## 4 · Multiple looks, handled explicitly

This is the second look at one hypothesis in one data source. Ignoring that would be the
cheapest available way to buy a significant result.

- **α = 0.025**, one-sided, for the PRE-002 primary — a Bonferroni adjustment over the two
  registered looks.
- The falsification conditions of PRE-001 §7 otherwise carry over unchanged, including the clause
  that **an underpowered test is inconclusive and never a pass**, and that a pilot pass which does
  not replicate is reported as a pass that did not replicate.

## 5 · The stopping rule

**If PRE-002 fails, WT-026 is recorded as not supported by EDGAR-derived firm-level data, and this
line of testing stops here.**

The next move in that case is not a third instrument on the same data. It is the acknowledged
structural defect that neither registration can fix: **the charge is asset-level and the
deterioration signal is firm-level.** A goodwill impairment is taken against one reporting unit;
consolidated revenue is the sum over all of them. Fixing that needs segment-level data, and it is
a different project with a different registration — not a re-run of this one.

Writing the stopping rule down now, while the result is unknown, is the only moment at which it
can be written honestly.

---

## AMENDMENTS

**`wealthTensor-37`, 2026-08-14 — the two files this registration shipped with, named. Not
registered in advance; written after the fact and marked as such.**

The introducing commit `d655501` carried this registration together with
`scripts/wt026_severe_test.py` — the instrument itself — and `src/wealth_tensor/edgar.py`. **What
makes a prediction a prediction is the commit order, and this one does not have it.** The
consequence is the plain one and is not softened here: nothing in this file was proved to precede
the instrument by the repository, and any severity claim resting on its priority rests instead on
the reader's trust.

This is the live-fire instance the 2026-08-10 lesson was banked from, and its entry in
`tests/test_registrations_precede_their_instruments.py`'s `KNOWN_VIOLATIONS` stays, asserted in
both directions. History is not rewritten to make a test green. The disclosure is added here
because a ledger that lives only in the test suite leaves this document still implying it stood
alone.
