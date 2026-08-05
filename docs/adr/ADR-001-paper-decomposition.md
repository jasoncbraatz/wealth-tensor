# ADR-001 · Decompose the manuscript into four papers

- **Status:** ACCEPTED · 2026-08-05 (S2) · decided with Jason, in session
- **Supersedes:** the implicit single-artifact plan carried from S1
- **Relitigation:** none required. If a future session wants to reopen this, read §Consequences
  first and bring a reason not already answered there.

## Context

The manuscript is **7,711 words of body** covering **eight topics** — Piketty, Cournot,
Bertrand, VNM, biophysics, kinetic exchange, the proposed framework, and three research
projects. That is roughly 950 words each, which is why nothing is developed: the atomic unit,
the paper's central object, receives **280 words**.

The defect is not length. 7,711 words is a normal paper. The defect is **breadth for that
length**, and it produces every downstream symptom already logged: the contribution beginning at
76% of the body (WT-040), the results living in the repo and not the paper (WT-037), and a
first-principles claim asserted four times and defined zero times (WT-038).

Every strategic move of S2 narrowed the attack surface — SMD demoted to a shield (WT-041), the
architecture dependency demoted to an open question (WT-045), Λ reframed as an entailment
(WT-038). This decision applies the same discipline at the level nobody had applied it: the
document.

**Audience, stated by Jason at the close of S2, and it is load-bearing for this ADR:** his three
children. The paper is a stewardship artifact demonstrating what sustained independent inquiry
looks like. That has two consequences recorded in §Consequences, and they are not sentimental —
they change what gets published and how.

## Decision

Split into four papers. One claim each. Evidence allocated without overlap.

### Paper I — Price formation without independent curves

**Claim.** Supply and demand schedules are not independent equations. They are two readings of a
single distribution of reservation prices, so the clearing interval is invariant to the
allocation while the schedules are not — and the textbook cross is therefore a valid *snapshot*
and an invalid *comparative static*.

- **Code:** `excess_demand.py` (9 tests) + `cournot.py` (11 tests) = 20 tests.
- **Ledger:** WT-001, 005, 012, 013, 014, 015, 017, 018, 019, 020, 021.
- **Why these two modules together:** WT-001 established that the Cournot corner solution *is*
  the marginal pair — the same object from two directions — and WT-013 that Cournot's tatonnement
  instability is a micro-instance of SMD. They are one paper, and this is where the manuscript's
  current Cournot/Bertrand material goes, re-genred from narration to assertion (WT-040).
- **Headline numbers:** 25 allocations → 25 demand schedules → **1** clearing interval; exact
  reduction to the Marshallian cross for any fixed allocation; endowment-effect volume decline
  93→49 units, reproducing Kahneman-Knetsch-Thaler as a consequence rather than a fit.
- **SMD is the shield here and only here** (WT-041) — this is the paper where it is on-topic.
- **Needs:** nothing new. Complete.

### Paper II — Redistribution as a parameter space

**Claim.** In multiplicative-additive wealth processes the *base* of a levy caps the reachable
inequality region and the rate only moves you within it. The decisive parameter is
**realisation**: at zero realisation a confiscatory levy on flow is statistically
indistinguishable from no levy at all.

- **Code:** `redistribution.py` (18 tests).
- **Ledger:** WT-029, 030, 033, 034, 035.
- **Positioning:** kinetic exchange (Chakrabarti, Chatterjee, Chakravarty). Positive, never
  normative — WT-029's boundary is maintained throughout.
- **Needs:** almost nothing. Shortest and closest to done.

### Paper III — The dual tensor and the reporting layer *(the flagship)*

**Claim.** Wealth is a compound of a physical and a claim component obeying different laws; the
claim component is a low-pass filter on the physical one; lag and crisis severity scale with the
**unobservability** of degradation; and the coupling between components is an entailment of the
composition axiom whose drift is the deferred information.

- **Code:** `lag.py` (10 tests) + `lambda_sensitivity.py` (10 tests) = 20 tests.
- **Ledger:** WT-002, 003, 004, 022, 023, 024, 025, 026, 027, 028, 031, 036, 038, 043.
- **The axioms live here.** P1 composition, P2 decay, P3 atomism, stated as propositions with
  stated domains (WT-038). This is the paper closest to Jason's heart and it should carry the
  intellectual core rather than deferring it to the synthesis.
- **Λ is defended once, with three legs, and then used without apology** (WT-043): it is an
  entailment of P1; the numeraire cancels across twelve orders of magnitude with spread exactly
  0.0; Λ⁻¹ is UN SDG indicator 7.3.1.
- **Needs: WT-026** — the severe test. This is the one paper with an unbuilt dependency, and it
  is why WT-026 is the START HERE in the handoff.

### Paper IV — The atomic theory: composition across scales

**Claim.** The three literatures join, the same atomic unit composes from household to sovereign,
and the whitespace at their intersection is real.

- **Code:** none of its own. It cites I, II and III as established results.
- **Ledger:** WT-006, 007, 039, 040, 041, 042, 044, 045, plus the joins.
- **Carries:** the constraint-expiry argument — *force-fit, not form-fit* (WT-042) — as its
  motivation; the relocation method stated deliberately (WT-039); and the citation-graph
  whitespace test (WT-006) as evidence rather than anecdote.
- **The SMD-versus-scale tension must be resolved explicitly here:** the tensor composes,
  behaviour does not. Aggregation destroys the behavioural information macro believes it is
  measuring while preserving the thermodynamic structure nobody is looking at. Claiming clean
  composition without saying this, in a paper that cites SMD, is the one unforced error available.
- **Needs:** I–III to exist.

## Order of publication

**II → III → I → IV.** Reasoning, since the order is not obvious and is the part most likely to
be second-guessed:

1. **II first as the rehearsal.** Jason's stated gap is not the science, it is *"the systems
   knowledge of the preprint infra as it stands today."* Learn abstracts, JEL codes, keywords,
   code-availability statements and the endorsement process on the paper where a mistake costs
   least. II is short, self-contained, and lands in the friendliest venue.
2. **III second, and it does not wait.** WT-026 is a data project that proceeds *in parallel*
   with drafting II, so the flagship is not deferred — it is cooking. By the time it ships there
   is a name already on record and the machinery is understood.
3. **I third.** Complete, but it is the most likely to draw territorial referees, and it is
   strongest when the author is not an unknown.
4. **IV last**, necessarily.

## Alternatives considered

- **Ship the single document as-is.** Rejected: eight topics at 950 words each, and a referee
  cannot check any of the five results because none appear in it.
- **Restructure into one bigger paper** (the S2 plan, WT-040). Not wrong, and its five-part spine
  survives *inside* Paper III — but it keeps one artifact carrying four claims, so one weak
  section sinks all of them. Superseded by this ADR, not contradicted.
- **Two papers (theory + empirics).** Rejected: the theory half still carries three unrelated
  claims and the split does no work.
- **Publish III first because it is closest to his heart.** Seriously considered and it remains
  Jason's call to override. Rejected only because III is the paper that most benefits from
  machinery already learned, and because the parallel WT-026 work means choosing II costs no
  delay to III. Joy is co-equal with shipping in the standing brief; if this ordering ever makes
  the work less enjoyable, invert it — that is a legitimate reason and not a concession.

## Consequences

- **No re-litigation.** Evidence is allocated exhaustively and without overlap. A future session
  proposing to move a module between papers must first read the join that put it there.
- **Failure is contained.** A rejection of III no longer takes I and II with it.
- **The synthesis gets stronger, not weaker.** "We showed in [1]… and in [2]…" beats asserting
  all three in one document, and it is the model Jason already knows from CS: a series of papers
  building a system.
- **Reproducibility becomes the differentiator.** Five modules, 58 tests, every figure regenerable
  from two scripts, in a field with a known-poor replication record. Every paper carries a code
  availability statement naming `github.com/jasoncbraatz/wealth-tensor` and the commit SHA. This
  is the largest unexploited asset in the project.
- **`docs/` stays public — decided, closed.** The working notes are not an embarrassment to be
  scrubbed before publication; given the stated audience they are the demonstration. A ledger in
  which WT-030 half-failed and was sharpened rather than defended teaches more about method than
  any conclusion the papers reach. Add one README line framing `docs/` as a working lab notebook.
  **`Abandoned Approaches` is therefore promoted from a distinctive section to a load-bearing
  one, and appears in every paper**, populated from the ledger's DEAD-END entries.
- **The missing apparatus is now a per-paper checklist**, not a vague worry: abstract, keywords,
  JEL codes, explicit contributions list, limitations section, data/code availability, and
  *Independent researcher* as the affiliation. All are absent today; all are cheap.
- **One live placeholder to clear:** *"Further entries to be migrated from the project findings
  ledger as they accumulate"* is a TODO sitting in the deliverable.
