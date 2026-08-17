# RESULT · REG-013 — the citation-graph whitespace, and it survives on an instrument that can be checked

- **Registered:** `docs/preregistration/REG-013-citation-graph-whitespace.md`, commit `fff7063`,
  **before `scripts/reg013_citation_whitespace.py` existed.**
- **Instrument:** `scripts/reg013_citation_whitespace.py`
- **Run:** 2026-08-16, `wealthTensor-53`, darwin. Log `RESULT-REG-013-run.log`, JSON
  `RESULT-REG-013-run.json`.
- **Verdict:** **H1 SURVIVES.** All three target pairs read WHITESPACE under the registered
  decision rule. The run is **not void** — the ceiling control fired.
- **The sensitivity that a referee would find first is in §4 and it is real:** under a
  *per-cluster* ceiling rather than the registered pooled one, the (T,S) pair moves to UNDECIDED.
  The registered rule is the one that governs; the sensitivity is reported because the difference
  between the two is one clause, and a result whose verdict turns on a clause should say so.

---

## 1 · What was measured

`ADR-001` §Paper IV commissions the citation-graph whitespace *"as evidence rather than anecdote"*,
citing `WT-006` (2026-08-04). **WT-006 proposed the instrument and was never run.** Every
whitespace claim in this repository until today rested on *"I looked and found nothing"*, which is
the sentence WT-006 was written to replace.

Three target clusters — **T** biophysical/thermodynamic economics, **S** stock-flow-consistent
macro, **K** kinetic-exchange econophysics — plus **X**, six highly-cited CRISPR papers, as a
literature unrelated to economics by construction. Seeds fixed in the registration; for each
cluster the **audience** is the set of works citing at least one resolved seed, retrieved from
OpenAlex, capped at `N_MAX = 4000` by descending citation count. The statistic is the overlap
coefficient **O(A,B) = |cite(A) ∩ cite(B)| / min(|cite(A)|, |cite(B)|)**.

## 2 · Drop accounting

| cluster | seeds asked | seeds resolved | audience retrieved | true audience | cap bound |
|---|---|---|---|---|---|
| **T** biophysical | 7 | **7** | 4 000 | **7 801** | **yes (51 %)** |
| **S** stock-flow | 6 | **6** | 1 139 | 1 139 | no |
| **K** kinetic exchange | 6 | **6** | 1 383 | 1 383 | no |
| **X** CRISPR (floor) | 6 | **6** | 4 000 | **43 048** | **yes (9.3 %)** |

**Twenty-five of twenty-five seeds resolved.** No cluster is under-powered by REG-013 §5.4's
four-seed rule. Two caps bound and both are reported above rather than left implicit; §4 states
which direction each one pushes.

## 3 · The result

### 3.1 · The two ends of the scale

The controls are the measurement. Without them the three target numbers below are three small
numbers, and small is the normal condition of any two specialties.

**CEILING — split-half, by seed-index parity, within each cluster:**

| cluster | even seeds | odd seeds | intersection | min audience | **O** |
|---|---|---|---|---|---|
| T | 4 | 3 | 134 | 797 | **0.168** |
| S | 3 | 3 | 155 | 298 | **0.520** |
| K | 3 | 3 | 380 | 511 | **0.744** |

**Pooled ceiling P = 0.477.** REG-013 §4's VOID rule triggers below 0.20; it does not trigger.
The instrument can see a literature joined to itself.

**FLOOR — each target cluster against CRISPR:**

| pair | intersection | min audience | **O** |
|---|---|---|---|
| T,X | **0** | 4 000 | **0.0000** |
| S,X | **0** | 1 139 | **0.0000** |
| K,X | **0** | 1 383 | **0.0000** |

**Pooled floor F = 0.0000.** Not one work in any of the three economics audiences also cites a
CRISPR seed. The floor is exactly zero, which is the strictest value it could have taken — see
§4.2.

### 3.2 · The three target pairs

With P = 0.477 and F = 0.000, z = (O − F)/(P − F) = O/P:

| pair | intersection | min audience | **O** | **z** | verdict |
|---|---|---|---|---|---|
| T,S — biophysical × stock-flow | 23 | 1 139 | 0.0202 | **0.042** | **WHITESPACE** |
| T,K — biophysical × kinetic | 15 | 1 383 | 0.0108 | **0.023** | **WHITESPACE** |
| S,K — stock-flow × kinetic | 6 | 1 139 | 0.0053 | **0.011** | **WHITESPACE** |

All three sit below the registered 0.10 bar. **H1 survives.**

The intersections are worth reading as counts rather than ratios, because that is what they are.
**Six works in the world cite both a stock-flow-consistent seed and a kinetic-exchange seed.**
Fifteen cite both a biophysical seed and a kinetic-exchange seed. Twenty-three cite both a
biophysical and a stock-flow seed. Against split-half intersections of 134, 155 and 380 *within*
each literature.

## 4 · What this result is exposed to, and one exposure is live

### 4.1 · The pooled ceiling is generous to the T pairs, and a per-cluster ceiling moves one verdict

**This is the sharpest thing to say against this result and it is said here first.**

Cluster T's own split-half overlap is **0.168** — far below S's 0.520 and K's 0.744, and below the
0.20 at which REG-013 would have voided the whole run had it been the pooled figure. That is not
surprising in hindsight: T's seeds are monographs spanning 1971 to 2012 across sub-traditions
(entropy economics, emergy accounting, energy-return analysis) that genuinely do not cite each
other much. **Biophysical economics is, on this instrument, itself a loose federation.**

Because z divides by the *pooled* P, the T pairs are scored against a ceiling that is substantially
higher than their own literature can reach. Recomputing with the stricter per-pair ceiling
min(P_A, P_B):

| pair | registered z (pooled P = 0.477) | stricter z (per-cluster P) | stricter verdict |
|---|---|---|---|
| T,S | 0.042 → WHITESPACE | 0.0202 / 0.168 = **0.120** | **UNDECIDED** |
| T,K | 0.023 → WHITESPACE | 0.0108 / 0.168 = **0.065** | WHITESPACE |
| S,K | 0.011 → WHITESPACE | 0.0053 / 0.520 = **0.010** | WHITESPACE |

**The registered rule governs, and it is not being re-chosen here** — REG-013 §6 forbids exactly
that, and re-picking the ceiling after seeing which verdict it produces is the instrument-tuning
this project exists not to do. But the honest statement of the result is: *two of the three pairs
are whitespace under every reading tried; the biophysical × stock-flow pair is whitespace under
the registered rule and undecided under a stricter one.*

Paper IV states it that way.

### 4.2 · The two caps, and which way each pushes

- **T truncated to 4 000 of 7 801 (51 %).** T's audience is its top half by citation count, so a
  bridging work in T's tail is invisible to this run. That **suppresses** O(T,S) and O(T,K) and
  therefore **biases toward H1**. It is the one bias in the run that runs in the paper's favour,
  and it compounds §4.1. Uncapping T is the obvious next run and it is not free — the intersection
  is computed against sets, so the cost is linear in the audience.
- **X truncated to 4 000 of 43 048 (9.3 %).** X's cap can only *lower* the measured floor, and the
  floor came back at exactly zero. A higher floor would push every z *down* (both numerator and
  denominator shrink, and the numerator shrinks faster for these small O). **F = 0 is therefore the
  strictest floor available**, and the cap on X costs the result nothing.

### 4.3 · What the instrument cannot see

- **Co-citation is not the only kind of contact.** Two literatures can be joined by a person, a
  conference, a textbook or a shared method without either citing the other's canon. This measures
  the citation graph, which is what WT-006 asked for, and nothing else.
- **Seed choice is a judgement.** Six or seven works cannot be a literature. The seeds are named in
  the registration, fixed before the run, and are the works this corpus actually cites — which
  makes them the right seeds for *this* claim (does the work I am building on get read together?)
  and not necessarily for a general claim about the fields.
- **OpenAlex under-covers pre-1995 references.** Anticipated in REG-013 §5.1 and the reason the
  statistic runs over citing works rather than over the seeds' reference lists. It still tilts T's
  audience recent, which — recent work being more interdisciplinary — biases against H1.
- **Occupancy, not fertility.** REG-013 §4's final clause, restated because it is the one a
  favourable result makes easy to forget: an empty intersection is not thereby a valuable one.

> **CORRECTION · `wealthTensor-62`, 2026-08-17 — appended by the seed-provenance check, NOT an edit
> to the text above.**
> §4.3's second bullet defends the seed choice with a claim about this repository's own
> bibliography: *"The seeds are named in the registration, fixed before the run, and **are the works
> this corpus actually cites** — which makes them the right seeds for *this* claim (does the work I
> am building on get read together?)."* **The seed lists and the corpus's bibliography are neither a
> subset nor a superset of one another. The claim fails in both directions**, checked against the
> live text of Papers I, II, III and IV with newlines normalised to spaces, so that a title wrapping
> a line boundary cannot read as an absence.
>
> **Direction one — five of the nineteen target seeds are works this corpus does not cite, anywhere:**
>
> | cluster | seeds | cited in Papers I–IV | **cited nowhere in Papers I–IV** |
> |---|---|---|---|
> | **T** biophysical | 7 | 5 | Ayres & Warr, *The Economic Growth Engine* (2009) · Kümmel, *The Second Law of Economics* (2011) |
> | **S** stock-flow | 6 | **3** | Godley, "Seven unsustainable processes" (1999) · Lavoie, *Post-Keynesian Economics: New Foundations* (2014) · Dos Santos, "Keynesian theorising during hard times" (2005) |
> | **K** kinetic exchange | 6 | **6** | — |
>
> `Kümmel`, `Second Law of Economics`, `Economic Growth Engine`, `Seven Unsustainable`,
> `new foundations`, `Keynesian theorising` and `Dos Santos` each return **zero** over all four
> manuscripts. All six `K` seeds are in Paper II's reference list; **half of cluster `S` is in no
> paper's**, and `S` supplies the smaller audience — the statistic's denominator — in two of the
> three target pairs, including the `S,K` pair the abstract quotes.
>
> **Direction two — the corpus cites work inside a seeded literature that is not a seed.** Paper II
> §References carries **Chakrabarti, Chakraborti, Chakravarty & Chatterjee (2013), *Econophysics of
> Income and Wealth Distributions*, Cambridge University Press** — kinetic-exchange econophysics by
> its own title, by three of cluster `K`'s own seed authors, and not in cluster `K`. Paper III
> carries **Soddy (1926/1961), *Wealth, Virtual Wealth and Debt*,** whose membership in cluster `T`
> is arguable rather than certain and is flagged as arguable here; the Chakrabarti volume needs no
> such hedge.
>
> **What this touches and what it does not.** It does not move a number, it does not reopen the
> verdict, and it may not: `REG-013` §6 fixes the seed lists and forbids re-choosing them in
> response to anything, this correction included. What it removes is a **defence**. §4.3's first
> sentence — *"Seed choice is a judgement"* — names the one threat in this run that no
> pre-registration can retire, because the registration is the place where the judgement is
> exercised. The bullet answers it by saying the judgement was not the analyst's but the
> bibliography's. For fourteen seeds that answer holds; for five it does not, and one work the
> bibliography does supply was left out. **The seeds are a defensible curation of these three
> literatures. They are not a transcription of this corpus's reference lists, and the sentence that
> says they are is the sentence a referee can take away in one grep** — so it is taken away here
> first.
>
> **One smaller thing, recorded rather than claimed as a second finding.** `REG-013` §3.1's fourth
> `T` seed names two different works by two different author teams separated by a slash — *"Hall,
> Cleveland & Kaufmann, `Energy and Resource Quality` / Hall & Klitgaard, `Energy and the Wealth of
> Nations` (2012)"* — under one date. §6 declares the seed lists fixed, but that entry does not fix
> a work. The instrument resolved **`W2784652317`, Hall & Klitgaard** (`RESULT-REG-013-run.log`
> line 4), which is the one the corpus cites, so the run is unaffected; the choice was nonetheless
> made by the script, after the registration. §6's guarantee is one seed weaker than it reads, and
> `Cleveland` returns zero across all four manuscripts.
>
> Appended rather than applied, because a result document is a dated record and rewriting it would
> destroy the evidence — `RESULT-END-TO-END-001-E6.md` §7's precedent, followed here. **No
> manuscript is edited and none needs to be:** the provenance claim occurs only at line 140 of this
> file (`grep -rn "works this corpus actually cites" docs/` returns one hit), and Paper IV §6 says
> only *"Each literature is defined by seed works named in the registration"*, which is true.

## 5 · Reproduce

```
python3 scripts/reg013_citation_whitespace.py > RESULT-REG-013-run.json 2> RESULT-REG-013-run.log
```

The instrument hits a live API and the graph grows, so the counts will drift upward with re-runs.
The *shape* — a ceiling near 0.5, a floor at or near 0, targets one to two orders of magnitude
below the ceiling — is the claim; a re-run that reverses it is a finding and should be reported as
one.
