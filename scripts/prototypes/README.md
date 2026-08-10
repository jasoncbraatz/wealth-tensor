# `scripts/prototypes/` — declared scratch, not results

**Declared 2026-08-10, session wealthTensor-04, before the code existed** (doctrine: *scratch is
declared before it exists* — an undeclared artifact becomes an unidentifiable orphan that costs a
future session a full investigation before anyone dares toss it).

## What lives here

Exploratory code that is **not** part of any paper's results and produces **no** published number.
Everything here runs on **synthetic data only**. Nothing here has touched EDGAR, and nothing here
may, until the condition below is satisfied.

| file | what it is |
|---|---|
| `bench_lag_torch.py` | Differentiable port of `wealth_tensor.lag.LayeredFirm` in PyTorch, batched over firms, correction mechanism disabled. Times forward and forward+backward at several batch sizes and both precisions, then runs a full parameter-recovery fit. |
| `bench_identify.py` | Diagnoses **why** that fit fails. Three checks isolating noise, the φ–d confound, and the conditioning's dependence on d. |

## ⚠ WT-052 DECLARATION — read this before writing PRE-003

`docs/LEDGER.md` **WT-052** (recorded the same day these files were written) requires that **a
pre-registration precede the instrument's code, not merely the result**, and provides exactly one
escape hatch for the case where an instrument must be prototyped first:

> *Where an instrument must be prototyped first, the prototype is committed and the registration
> then declares which committed SHA it is registering — the ordering has to be visible either way.*

**This directory is that case, and this file is that declaration.** These scripts are
instrument-adjacent to any future test that estimates φ by fitting. Therefore:

1. **A future PRE-003 (or any registration involving parameter fitting) MUST name the commit SHA of
   this directory's state at the time of registration.** The ordering must remain visible.
2. **No code in here may be pointed at EDGAR before that registration exists.** The moment fitting
   code that has seen the real data exists in this repo unregistered, WT-052 fires against us — one
   day after we wrote it.
3. If the prototypes change materially before a registration, that is fine and expected. The
   registration names the SHA it registers; drift before registration is visible in `git log`.

## Running them

These need PyTorch, which is deliberately **not** added to the project's `requirements` or the
darwin `.venv` — the test suite must stay a 2-second, stdlib-plus-numpy affair.

```
pip install torch --index-url https://download.pytorch.org/whl/cpu
python3 scripts/prototypes/bench_lag_torch.py
python3 scripts/prototypes/bench_identify.py
```

Both seed `torch.manual_seed(0)` and are deterministic. Figures quoted in
`docs/notes/NOTE-001-phi-identifiability.md` were produced on a **2-core 2.8 GHz Xeon** — chosen
deliberately as a weak machine, so the timings are an upper bound rather than a best case.

## What came out of them

See **`docs/notes/NOTE-001-phi-identifiability.md`**. Short version: the binding constraint on
measuring φ is not compute and never was. It is that **φ and the decay rate d are confounded in
the observed series**, and the fix is an independent estimate of d — a data-acquisition problem,
not a hardware one.
