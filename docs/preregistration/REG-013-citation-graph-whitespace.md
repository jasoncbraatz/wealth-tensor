# REGISTRATION · REG-013 — the citation-graph whitespace, and the floor that decides whether it means anything
*wealthTensor-53 · 2026-08-16 · registered in its own commit, ahead of the commit that carries the
instrument. `git log --follow` on this file is the ordering, and
`tests/test_registrations_precede_their_instruments.py` is what checks it.*

---

## 0 · What this is

`ADR-001` §Paper IV commissions *"the citation-graph whitespace test (WT-006) as evidence rather
than anecdote."* `WT-006` (2026-08-04) proposed the instrument and named the tooling. **It was
never run.** Two years of project documents cite the whitespace as motivation and the only
support anywhere in this repository is *"I looked and found nothing"* — the exact sentence
WT-006 was written to replace.

Paper IV cannot open on an unrun test. This registers the run.

## 1 · The claim under test

**H1.** The three literatures Paper IV joins — biophysical/thermodynamic economics (**T**),
stock-flow-consistent monetary macro (**S**), and kinetic-exchange econophysics (**K**) — are
mutually near-disjoint in the citation graph: a work citing one of them rarely cites another.

## 2 · The defect this registration exists to avoid, stated before anything is computed

**A low co-citation rate between two literatures is uninformative on its own, because it is the
normal condition of any two specialties.** Sociology and semiconductor lithography do not cite
each other either, and nobody calls that a research opportunity. A bare number here would be the
instrument artefact this project keeps finding: a quantity that looks like evidence because it is
small, with nothing establishing what small means.

So the measurement is **not** the three pairwise rates. It is those rates **placed on a scale
whose two ends are measured in the same run, by the same instrument, from the same source**:

- a **CEILING** — what this instrument reads when two bodies of work genuinely are one literature;
- a **FLOOR** — what it reads for a pair that is unrelated by construction.

Without both ends, the run reports nothing and must say so.

## 3 · The instrument

### 3.1 · Clusters, named here before any query

Each cluster is defined by seed works, resolved in OpenAlex by DOI or exact title. **The seed
lists are fixed by this document and may not be edited after the run** (the R5 discipline of
`CONSTRUCTION-REG-009`, applied here).

- **T · biophysical / thermodynamic economics.** Georgescu-Roegen, *The Entropy Law and the
  Economic Process* (1971); Ayres & Warr, *The Economic Growth Engine* (2009); Ayres & Warr,
  "Accounting for growth: the role of physical work" (2005); Hall, Cleveland & Kaufmann,
  *Energy and Resource Quality* / Hall & Klitgaard, *Energy and the Wealth of Nations* (2012);
  Odum, *Environmental Accounting: Emergy and Environmental Decision Making* (1996); Daly,
  *Steady-State Economics* (1977); Kümmel, *The Second Law of Economics* (2011).
- **S · stock-flow consistent monetary macro.** Godley & Lavoie, *Monetary Economics* (2007);
  Caverzasi & Godin, "Post-Keynesian stock-flow-consistent modelling: a survey" (2015);
  Nikiforos & Zezza, "Stock-flow consistent macroeconomic models: a survey" (2017);
  Godley, "Seven unsustainable processes" (1999); Lavoie, *Post-Keynesian Economics: New
  Foundations* (2014); Dos Santos, "Keynesian theorising during hard times" (2005).
- **K · kinetic-exchange econophysics.** Drăgulescu & Yakovenko, "Statistical mechanics of
  money" (2000); Chakraborti & Chakrabarti, "Statistical mechanics of money: how saving
  propensity affects its distribution" (2000); Bouchaud & Mézard, "Wealth condensation in a
  simple model of economy" (2000); Chatterjee & Chakrabarti, "Kinetic exchange models for income
  and wealth distributions" (2007); Yakovenko & Rosser, "Colloquium: Statistical mechanics of
  money, wealth, and income" (2009); Patriarca, Chakraborti & Kaski, "Statistical model with a
  standard Γ distribution" (2004).

### 3.2 · The two ends of the scale, also named here

- **CEILING — the split-half control.** Each cluster's seed list is split into two halves by a
  fixed rule (seed index parity, in the order printed above — no randomness, no re-draw). The
  overlap between the two halves of the *same* cluster is what this instrument reads when the two
  bodies of work are, by construction, one literature. This control is chosen deliberately over a
  hand-picked "known-joined pair" because it needs no further judgement from the analyst and
  **cannot be tuned**: if the instrument cannot see that half of econophysics is joined to the
  other half of econophysics, it cannot see anything, and the run is void.
- **FLOOR — the unrelated-field control.** Cluster **X**: six highly-cited works in CRISPR gene
  editing (Jinek et al. 2012; Cong et al. 2013; Mali et al. 2013; Doudna & Charpentier 2014;
  Ran et al. 2013; Komor et al. 2016). Chosen for being unrelated to economics by construction,
  well covered in OpenAlex, and comparable in citation volume to the target clusters. The three
  pairs (T,X), (S,X), (K,X) set the floor.

### 3.3 · The population and the statistic

For each cluster *C*, let **cite(C)** be the set of works citing at least one resolved seed of
*C*, retrieved from OpenAlex's `cites:` filter, capped at `N_MAX = 4000` works per cluster taken
in descending citation count (the cap is stated so that a truncation is never silent; the run
reports whether it bound).

For an ordered-insensitive pair (A,B) the statistic is the **overlap coefficient**

> **O(A,B) = |cite(A) ∩ cite(B)| / min(|cite(A)|, |cite(B)|)**

— the share of the *smaller* literature's audience that also reads the other. The overlap
coefficient is used rather than Jaccard because the clusters differ in size by design and Jaccard
would confound disjointness with size asymmetry.

### 3.4 · Drop accounting, reported whether or not it is flattering

The run reports: seeds requested, seeds resolved, seeds unresolved **by name**; works retrieved
per cluster; whether `N_MAX` bound for any cluster; and the raw intersection counts behind every
reported ratio.

## 4 · The decision rule, pre-committed in both directions

Let **P** be the mean split-half (ceiling) overlap across the three target clusters and **F** the
mean floor overlap across the three (·,X) pairs. Define the **normalised position** of a pair on
the floor-to-ceiling scale:

> **z(A,B) = (O(A,B) − F) / (P − F)**

For each of the three target pairs (T,S), (T,K), (S,K):

- **WHITESPACE — H1 survives for that pair** iff **z ≤ 0.10**. The pair reads as unrelated
  literatures on an instrument that can demonstrably tell related ones apart.
- **JOINED — H1 fails for that pair** iff **z ≥ 0.25**. Paper IV must then say so, name the works
  that bridge it, and drop the whitespace claim *for that pair*.
- **UNDECIDED** for 0.10 < z < 0.25. An undecided pair is reported as undecided; it is not
  rounded toward the hypothesis.

**H1 as a whole survives only if all three target pairs read WHITESPACE.** Two of three is a
partial result and is reported as one.

**VOID, and this outranks every clause above:** if **P < 0.20**, the ceiling control failed — the
instrument cannot see a literature joined to itself — and **no verdict may be read off this run at
all**, favourable or otherwise. A void run is reported as a void run.

**What a favourable result does NOT license, committed now while it is still cheap to say:** a
measured absence of co-citation is evidence that the intersection is *unoccupied*. It is not
evidence that the intersection is *fertile*. Paper IV may cite this result for the first claim
only. The second is what the paper's own argument has to earn.

## 5 · Threats to validity, named before the numbers exist

1. **OpenAlex under-covers pre-1995 references.** `POSITIONING-002` §(the coverage note)
   established this for this project already: the graph is assembled from metadata whose
   reference lists thin out badly before the mid-1990s. Georgescu-Roegen (1971), Odum (1996),
   Daly (1977) and Godley (1999) are therefore expected to resolve with under-counted citation
   sets. **This is why the statistic is computed over the CITING works — which are modern and
   well covered — and never over the seeds' own reference lists.** It still biases cluster T's
   audience toward recent work, and that bias is toward finding *more* bridging, not less, since
   recent work is more interdisciplinary. The bias therefore runs against H1, which is the
   direction one wants.
2. **A seed that fails to resolve silently shrinks its cluster.** Hence the by-name drop
   accounting in §3.4.
3. **The cap.** `N_MAX = 4000` per cluster, taken by descending citation count, over-samples
   well-cited works. Well-cited works are more likely to be interdisciplinary, so this bias also
   runs against H1.
4. **Books resolve badly.** Several T and S seeds are monographs, which OpenAlex indexes
   unevenly. If cluster T or S resolves fewer than four seeds, its result is reported as
   under-powered regardless of which side of the threshold it lands on.

## 6 · What is fixed by this document

The seed lists (§3.1), the two controls (§3.2), the statistic (§3.3), `N_MAX`, the thresholds
0.10 / 0.25 and the VOID rule (§4). **None of these may be re-chosen in response to a number.**
If the instrument turns out to be mis-specified, the repair is a *second* registration that says
so and says why — the `REG-001` precedent — not an edit to this one.
