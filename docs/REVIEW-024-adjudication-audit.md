---
audit_target: docs/promises-adjudicated.tsv
population: 129 adjudicated rows (paper-III 88, paper-IV 41) at parent commit 8855aba
seed: 20260818
draw: "random.Random(20260818).sample(sorted(promise_id), 12)"
sample_committed_before_adjudication: true
k_of_12_false: PENDING
---

# REVIEW-024 · The adjudication audit — measuring the error rate of `docs/promises-adjudicated.tsv`

*Session `wealthTensor-84` · 2026-08-18 · parent commit `8855aba`.*

> `-83` falsified ONE targeted row and it was false. That is a numerator with no denominator.
> This pass draws a random sample, commits it before looking, and puts an interval on it.

---

## 0 · THE DRAW — committed before a single row was adjudicated

**Population.** 129 adjudicated rows. (`-83`'s handoff said 128; the true count at `8855aba` is
129 — `-83` retired one row and added three, and `wt148` prints `129 adjudicated`. The audit uses
the file, not the handoff.)

**Seed.** `20260818`. **Procedure**, verbatim and reproducible:

```python
ids = sorted(promise_id for row in tsv if not row.startswith('#'))
sample = random.Random(20260818).sample(ids, 12)
```

**THE TWELVE, listed here before any of them was checked.** This section was written and
committed as its own commit, with `k_of_12_false: PENDING` in the front matter, so that the
sample cannot have been chosen after reading. Re-run the four lines above to confirm the draw.

| # | promise_id | paper | artefact | class as filed |
|---|---|---|---|---|
| 1 | `bf2138f041` | paper-IV | `test_a_flat_gini_does_not_mean_a_bounded_one` | H |
| 2 | `3bdab165bf` | paper-III | `REG-005` | H |
| 3 | `ec8622f081` | paper-IV | `ADR-001` | H |
| 4 | `75220244de` | paper-IV | `docs/papers/PREPRINT-CHECKLIST.md` | H |
| 5 | `6efe91d805` | paper-III | `src/wealth_tensor/lambda_sensitivity.py` | H |
| 6 | `aebdfa4d76` | paper-III | `data/pre-002-riskset.json` | H |
| 7 | `fd2b77f988` | paper-III | `RESULT-REG-008` | H |
| 8 | `c487d43b12` | paper-III | `PRE-002` | N |
| 9 | `76617b04e0` | paper-IV | `src/wealth_tensor/lag.py` | H |
| 10 | `9add6ff45d` | paper-III | `93a159b` | H |
| 11 | `7e1c612368` | paper-III | `WT-059` | H |
| 12 | `388811fc0a` | paper-IV | `REG-013` | H |

**The question each row is asked.** NOT *"is the sentence true?"* — `-83`'s false row passed that
one. The question is:

> **Does the `evidence` column bear on the artefact THE SENTENCE NAMES?**

A row is FALSE if the adjudicator checked a different artefact from the one the sentence names,
even where the number agreed. That is `-83(ii)`, and it is the failure mode this sample is sized
to catch.

---

## 1 · The verdict

*PENDING — this section is written after §2.*

---

## 2 · The twelve, adjudicated

*PENDING.*

