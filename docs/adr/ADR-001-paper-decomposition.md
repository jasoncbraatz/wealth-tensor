# ADR-001 · Decompose the manuscript into four papers

- **Status:** ACCEPTED · 2026-08-05 (S2) · decided with Jason, in session
- **Supersedes:** the implicit single-artifact plan carried from S1
- **AMENDED 2026-08-11 (wealthTensor-10): the corpus is THREE preprints.** Paper I folds into
  Paper IV by Jason's ruling — see the final addendum. The title and §Decision below record the
  decision **as it was made** and are deliberately not rewritten; the addenda amend it.
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

**Claim.** *(Sharpened 2026-08-10 — see the Addendum at the foot of this file. The statement below
is the one this ADR was written with; it is true, and it is one step weaker than the code
supports.)* Supply and demand schedules are not independent equations. They are two readings of a
single distribution of reservation prices, so the clearing interval is invariant to the
allocation while the schedules are not — and the textbook cross is therefore a valid *snapshot*
and an invalid *comparative static*.

- **Code:** `excess_demand.py` (10 tests) + `cournot.py` (12 tests) = 22 tests, plus the
  regeneration script `scripts/wt018_report.py` (wealthTensor-06).
- **Ledger:** WT-001, 005, 012, 013, 014, 015, 017, 018, 019, 020, 021.
- **Why these two modules together:** WT-001 established that the Cournot corner solution *is*
  the marginal pair — the same object from two directions — and WT-013 that Cournot's tatonnement
  instability is a micro-instance of SMD. They are one paper, and this is where the manuscript's
  current Cournot/Bertrand material goes, re-genred from narration to assertion (WT-040).
- **Headline numbers:** 25 allocations → 25 demand schedules → **1** clearing interval; exact
  reduction to the Marshallian cross for any fixed allocation; endowment-effect volume decline
  93→49 units, reproducing Kahneman-Knetsch-Thaler as a consequence rather than a fit.
- **SMD is the shield here and only here** (WT-041) — this is the paper where it is on-topic.
- **Needs:** nothing new. Complete in evidence; **drafted as `docs/papers/paper-I-price-
  formation/paper-I.md` in wealthTensor-06**, ~7.1k words, references verified.

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

**II → III → IV.** *(Corrected in place 2026-08-15, `wealthTensor-51`. This section read
**II → III → I → IV** until today — the order as decided on 2026-08-05 and reconfirmed
2026-08-10. The 2026-08-11 `-10` addendum folded Paper I into IV and its "What changes" table
recorded the new order, **and nobody applied it here.** The heading is the live claim; the
addendum was a footnote to it. Item 3 below is struck rather than deleted, because the reasoning
that placed Paper I third is the record of how the decision was reached.*
>
> **This is the failure this ADR predicted about itself.** The `-10` addendum closes:
> *"Recorded because a corpus that quietly becomes three papers, in a repository whose central
> document says four, is a contradiction a future session would find the hard way."* `-51` found
> it the hard way — it quoted the stale order to Jason, in a summary of what the estate had
> already decided, and **Jason caught it.** The correction existed, was correct, was dated, and
> lived one screen below the sentence it corrected.
>
> It is `-50`'s tell and `-51`'s at ADR scale: **a correction that lives only in an addendum has
> not been made**, and **a correction applied to one place while a second asserts the same claim
> has a live reservoir.** Here the reservoir was the section heading — the most-read line in the
> file. Amend the CLAUSE; let the addendum explain why, not carry the fix.)*

Reasoning, since the order is not obvious and is the part most likely to be second-guessed:

1. **II first as the rehearsal.** Jason's stated gap is not the science, it is *"the systems
   knowledge of the preprint infra as it stands today."* Learn abstracts, JEL codes, keywords,
   code-availability statements and the endorsement process on the paper where a mistake costs
   least. II is short, self-contained, and lands in the friendliest venue.
2. **III second, and it does not wait.** WT-026 is a data project that proceeds *in parallel*
   with drafting II, so the flagship is not deferred — it is cooking. By the time it ships there
   is a name already on record and the machinery is understood.
3. ~~**I third.** Complete, but it is the most likely to draw territorial referees, and it is
   strongest when the author is not an unknown.~~ **SUPERSEDED 2026-08-11 (`-10`): Paper I is not
   a preprint.** Its surviving identity — *the crossing height IS the volume* — is a subsection of
   IV, and its dead framings become IV's Abandoned Approaches entry. The reasoning above is kept
   as the record of a decision that was later overtaken by Paper I's claims dying to their own
   referees (WT-066, WT-070), not by a change of mind about ordering.
4. **IV last**, necessarily — and it now carries Paper I's subsection as well as its own charter.

> **AND THE ORDER IS A BATCH, NOT A SCHEDULE** (`-08` addendum, 2026-08-11, Jason's ruling).
> Nothing ships until the corpus is done, because the conjunction gets exactly one first
> end-to-end pass and shipping early spends it. **A session's job is to bring a paper to
> "ready to submit"** — that is a paper's terminal state, and no session should ask Jason to
> trigger a submission before all three reach it.

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

## Relitigation record

- **2026-08-10 · wealthTensor (Fable session, with Jason) · REAFFIRMED.** Jason invoked the
  §Status clause deliberately — "I'm not convinced it needs to be split" — and brought the
  strongest available reason: the thesis IS the conjunction (three literatures each describing
  a different layer of one abstraction stack), so splitting risks losing the whole Picasso.
  Answered on four legs, recorded here so no future session rebuilds the argument:
  1. **The objection names Paper IV, not a merger.** "The three fields are layers of one
     stack" is itself the fourth claim, and it is stronger citing I–III as established results
     than asserting all three legs inside one document. The decomposition *promotes* the
     conjunction; it does not discard it.
  2. **The stack analogy cuts toward the split.** TCP/IP was not one RFC — IP got 791, TCP got
     793, and the architecture claim got its own literature. A layered-stack claim is credible
     precisely because each layer's spec stands alone. "Lego-by-lego" (Jason, accepting,
     2026-08-10).
  3. **Containment is no longer a design argument — it is an observed outcome.** §Consequences
     promised "failure is contained" on 2026-08-05; RESULT-002 (the severe test failing twice,
     with power) landed the same week and touched Paper III alone, exactly as promised. The
     insurance policy was bought Tuesday and the house caught fire Thursday.
  4. **A monolith invites the 1993 failure mode, three times at once.** Each field's referee
     hits ~950 words of "their" layer, rejects out of frame, and the conjunction never gets a
     hearing. Split, only Paper IV asks a reader to cross a boundary, and its readers
     self-select for it.
- **Order II → III → I → IV reconfirmed by Jason same date** ("I'd probably like to just stick
  to it in order").
- **New post-IV artifact, TEED UP, not scheduled — THE MONOGRAPH.** After ~~I–IV ship, compile
  the four preprints~~ **II, III and IV ship, compile the three preprints** *(corrected in place
  2026-08-16, `wealthTensor-52`, per the `-10` amendment; Paper I is a subsection of IV, not a
  preprint)* back into a single narrative volume for the stated audience: connective
  tissue, the ledger stories, the lost bet honoured, Abandoned Approaches in full. The
  preprints are the scholarly deliverable; the monograph is the stewardship one. Guernica had
  dozens of standalone studies; the mural came after. Do not start it before IV exists.

### Addendum · 2026-08-10 · wealthTensor-04 · the ORDER question, answered separately from the split

Jason reopened **order** (not the split) the same day: *"do you think we should start at paper I
instead? … if we don't do them in order, will we lose fidelity? Or will it allow us to 'work
backwards' by doing III first?"* — and notably he was arguing **against** his own preference,
suspicious of himself for favouring III. Answered and accepted; recorded so this is the last time
it is rebuilt from scratch.

1. **The numbering is not a dependency order.** Draw the graph from §Decision's evidence
   allocation and there is exactly one edge set in the whole project: **IV needs I, II and III.**
   I, II and III have no edges among them. The I/II/III/IV numbering is a *reading* order for the
   monograph, not a construction order, and conflating the two is what makes the question feel
   hard.
2. **III is the root, not the middle — because the axioms live in it.** Starting at I means
   drafting a paper whose foundation is stated nowhere on paper, only in Jason's head and in a
   ledger entry. That is precisely the condition WT-038 diagnosed as the original defect
   (*"absent from the page, carried in his head"*); doing I first would recreate it on purpose.
   **III-first IS topological order.** Nothing is being worked backwards.
3. **THE WRINKLE, and it is a genuine gap in this ADR that cuts TOWARD III-first.** §Decision
   allocated **code and ledger entries** exhaustively and without overlap — correctly — but it
   never allocated **propositions**, so one conceptual edge is invisible in the table: **Paper I's
   central claim is an instance of P3.** Schedules read off a single distribution of reservation
   prices *are* folds over units. Write I first and that thought gets stated ad hoc in I's own
   register and then again as P3 in III — the same idea twice, in two vocabularies, with no stated
   relation. Write III first and I opens with "this is P3 [III §2], instantiated in a price
   system": one statement, one citation, zero duplication.
4. **The force-fit guard, named with Jason's own phrase (WT-042).** The real risk in III-first is
   that I later gets *bent* to satisfy P1–P3 — force-fit, not form-fit. The guard is already in
   place: I's results are properties of a reservation-price distribution and never invoke P1 or
   P2. **The alarm to listen for while drafting III is the urge to reach into I's or II's
   evidence.** It did not fire in S3 or in wealthTensor-04.
5. **Already tested once, empirically.** Paper II was drafted *ahead* of III and made a clean
   forward gesture without needing III to exist — §3.2's *"a levy that cannot see an accrual and a
   financial statement that does not record a degradation are the same structure."* The
   out-of-numbering-order fidelity test has been run and passed.
6. **The best argument for I-first, recorded so it is not re-derived either:** I is complete and is
   the most conventionally-economics artifact in the set, which makes it the easiest arXiv
   endorsement ask (the endorser is asked only whether the paper belongs in the category).
   §Order-of-publication already answered it — territorial referees, and I is strongest when the
   author is not an unknown — and that answer stands. It is the real cost of choosing III, and it
   is a cost, not a wash.

**Outcome: order II → III → I → IV unchanged. Jason accepted the same day** ("your recommendation
definitely wins here — I see the picture now"). The clarification is that the order was never in
tension with the argument's logic; it only looked that way because the numbering reads like a
chain.

### Addendum · 2026-08-10 · wealthTensor-06 · Paper I's claim was one step weaker than its own code

Recorded here because §Decision's claim statement is what a future session reads first, and it
understates what `excess_demand.py` demonstrates. Nothing about the split or the order changes.

§Decision says *"the clearing interval is invariant to the allocation while the schedules are not."*
True, and it is an **inference**: two objects that both move under a perturbation leaving the
equilibrium fixed cannot be independent equations. Writing Paper I's regeneration script found the
**identity** underneath it. Measured over 25 allocations at 399 interior grid points: 25 distinct
demand schedules, 25 distinct supply schedules, and **one** distinct excess-demand schedule, equal
to `#{i : m_i > p} − S` at every point. The *S* holders partition at any price into those above it
and those below it, so the allocation enters the two counts with opposite signs and cancels — at
every price, not merely at the zero.

The upgrade is not rhetorical. The inference licenses *"the schedules are not independent"*; the
identity licenses *"the decomposition of excess demand into a supply half and a demand half carries
no economic content"*, which is a strictly stronger statement and needs no inferential step a
referee can contest. It also gives the reduction result its proper shape: the Marshallian cross is a
valid snapshot **because** it reads the zero of *z* correctly, and an invalid comparative static
**because** it treats a bookkeeping split as two perturbable objects. Same theorem, both directions.

A second result arrived the same way. WT-005's gloss — *damping rescues convergence but is an extra
assumption* — is now sharpened: the stabilising damping is `d < 4/(n+1)` and therefore **vanishes
like 4/n**, so the repair requires each firm to know how many rivals it has and slow itself in
proportion. The fix needs precisely the information Cournot's static expectation denies.

Ledger: **WT-063**, **WT-064**. Both pinned by tests. Neither was visible from the ledger, the ADR
or the paper drafts — **only from writing the script that regenerates the numbers**, which is worth
noting for its own sake: `scripts/wt018_report.py` was built to guard against WT-027's failure mode
(hand-transcribed figures that stop regenerating), the figures all regenerated, and the script
earned its keep anyway by making the modules state what they actually prove.

### Addendum · 2026-08-11 · wealthTensor-07 · Paper I is re-scoped around P3, and the re-scope is currently unsupported

Recorded here because §Decision's statement of Paper I's claim is what a future session reads first,
and that claim is now **displaced prior art**.

**What happened.** `REVIEW-002` (wealthTensor-06) rejected Paper I v0.1 and left one claim standing:
the allocation cancels from excess demand identically, at every non-reservation price. It made a
literature search a **precondition** of any redraft. The search found the claim in **Wicksteed
(1910), Bk II Ch. IV** — same horse market, same reallocation exercise, and the §5 thesis about the
Marshallian cross as well. `REVIEW-003` carries the audit; `WT-066` carries the ledger entry.

**Nothing about the split or the order changes.** What changes is the level at which Paper I states
its claim.

**The decision (Jason, 2026-08-11), and the argument that survived testing.** Jason's reading was
that *our* case is the general one and theirs the special case. Tested on three axes, it came back
split, and the split is the useful part:

1. **Böhm-Bawerk — he is right.** *Marginal pairs* needs four parties in two pairs; pooling the
   eighteen valuations at *S* = 8 collapses them to two order statistics. The distinction his
   statement requires is dissolved, not specialised.
2. **Wicksteed, within the market — he is wrong, and this must be conceded in print.** Wicksteed
   covers divisible goods and multi-unit holdings. Our unit-demand identity is a strict special
   case of his.
3. **Wicksteed, on the axis that matters — he is right, and this ADR already said so.** The third
   addendum records that Paper I's claim is an instance of **P3 · Atomism**. Read through P3 the
   claim is not Wicksteed's: excess demand is a fold over units; the two schedules are folds over
   units **and the allocation**, which is not a property of the population. Wicksteed's apparatus is
   subjective scales of preference and is domain-bound by construction — he has no P3, and complains
   that the diagram is *misleading* rather than that its halves are not the kind of object they
   present themselves as.

**So Paper I was not scooped. It was written one level too low** — it went out as a market result
and met the man who owns markets. The third addendum had the right reading and the draft did not use
it.

**The condition attached to this decision, and it is not yet met.** The P3 framing is only worth
anything if the identity does work somewhere Wicksteed's apparatus cannot follow. `REG-001` was
registered to test exactly that and **returned no verdict** — the instrument was mis-specified in
four ways, and its priority audit put the general proposition in four established literatures, the
earliest being Markov-chain lumpability (Kemeny & Snell, 1960). See `RESULT-REG-001.md` and `WT-067`.

**Therefore:** Paper I is re-scoped around P3, and **its limitations section must state that the
generality is unexercised, in those words**, until a second instantiation exists that survives an
adversarial pass. A re-scope whose justifying condition is unmet is an honest draft with a stated
exposure; a re-scope that hides the gap is the thing this programme exists not to do.

**Citations now mandatory whatever Paper I becomes:** Wicksteed (1910) Bk II Ch. IV **in front**;
Böhm-Bawerk (1889, Smart trans.) for *marginal pairs*; Shapley & Shubik (1971), whose §4 is titled
*"The Horse Market of Böhm-Bawerk"*; Theocharis (1960), Fisher (1961), Bischi et al. (2010) eq. 2.26
for §4.2; Coase (1960) and Gorman (1953) as adjacent-not-displacing.

### Addendum · 2026-08-11 · wealthTensor-08 · the P3 re-scope is dead, and so is its replacement

Recorded here because addendum 4 recorded the re-scope, and a decision record that logs a re-scope
without logging its death is a document that lies by omission.

**What happened.** The session was briefed to write Paper I at the P3 level. It built three
instruments, fired WT-065 before calling anything a result, and the framing did not survive. **No
paper was written.** Full report: `docs/papers/paper-I-price-formation/RESULT-WT070-p3-is-dead.md`;
ledger `WT-070`.

**Why the P3 framing fails, in one line each.**

1. **The diagram is not caught in the act.** At an interior clearing price, *D*(*p*\*) = *S*(*p*\*) =
   |*H* \ *T*| = volume. The crossing *height* is the allocation mismatch — the one quantity *z*
   cannot deliver. The two curves read the population on one axis and the coupling on the other. The
   conclusion was inverted.
2. **"H is not a property of the population" is false** under the standard unit (*mᵢ*, *hᵢ*), which
   makes *D* and *S* additive folds in exactly the sense *z* is. This is Arrow–Debreu, Aumann (1964),
   Hildenbrand (1974), and **Hildenbrand (1994) p. 36** — a source this same session established and
   was preparing to cite.
3. **The supporting exhibit measured a hypergeometric.** The reported crossing-height range was ±2 sd
   of *S*(*N*−*S*)/*N*. The quantity at issue had never been varied.

**Why the replacement also fails.** The frictional identification result — the coupling is
unidentified at *t* = 0 and exactly identified at every *t* > 0 — is verified and is displaced twice:
the *t* = 0 invariance is asserted in print by Azevedo–Weyl–White (2013), Gul–Pesendorfer–Zhang
(2019) and Baldwin–Jagadeesan–Klemperer–Teytelboym (*JPE*), each as an aside justifying the omission
of endowments; and the uniqueness lemma is the **Titchmarsh convolution theorem (1926)**, with the
claim's shape already published as Bertanha–McCallum–Seegert (2023). It also requires an observable
nobody has: the entire excess-demand schedule over a continuum of prices.

**What this does NOT change.** Nothing about the split, the order, or Papers II–IV. Checked rather
than assumed (WT-057): **Paper III's P3 survives untouched** — it is the weaker claim that measured
aggregates are folds over units and no aggregate is more fundamental than its constituents, aimed at
the aggregate production function, and it never depended on Paper I. **Papers II and III cite Paper I
zero times.** §Consequences' promise that failure is contained has now been cashed three times, and
this is the first time the fire was in the room the policy named.

**What Paper I is now, pending Jason's decision.** Not written, not re-scoped, and no longer
obviously a paper. What survives is a subsection-sized expository observation — *the crossing height
is the volume, so here is what the two curves are for* — and a large Abandoned Approaches entry.
**Recommendation: fold into Paper IV**, whose charter already covers composition across scales and
the tensor-composes-behaviour-does-not tension. **Not Paper III** — that would be force-fit, and per
addendum 2 §4 the alarm to listen for is the urge to reach into another paper's evidence. It was
audible and is recorded here rather than acted on.

**Open, and Jason's:** whether Paper I survives as a paper at all, or becomes a section of IV. The
publication order II → III → I → IV is not reopened by this; what is in question is only whether the
third slot still contains a paper.

### Addendum · 2026-08-11 · wealthTensor-08 · **nothing ships until the corpus is done** — Jason's ruling

Recorded here because §Order of publication reads as a sequence of separate submission events, and it
is not one. **Five consecutive handoffs recorded Paper II as "ready to submit, awaiting Jason's word"
and instructed the next session to go and get that word.** The word was not missing. The decision had
been made and no session had asked in a way that surfaced the reason.

> **Jason, 2026-08-11:** *"I want to wait until we have the corpus done (so we can test it end to
> end; right now we're testing the individual parts like those who use error-statistical philosophy;
> correct approach here — when we're done with the papers, I want to re-test the entire system at
> once)."*

**This is a methodological position and it is his.** Every paper so far has been given a severe test
of its own parts — a hostile referee, a priority audit, a pre-registration with a stated falsifier, a
mutation-tested guard. **What has never been tested is the conjunction.** ADR-001 §Relitigation
record already establishes that the conjunction *is* the fourth claim; it follows that the conjunction
needs its own test, and that a corpus gets exactly one first end-to-end pass. Shipping II early spends
that pass to bank a partial win.

**What changes.** Nothing about the split, the order, or the per-paper Definition of Done. ~~**II → III
→ I → IV**~~ **II → III → IV is now the order of a submission *batch*, not a schedule of separate
events.** A session's job is to bring papers to DONE; "ready to submit" is the terminal state for an
individual paper, and no session should ask Jason to trigger a submission before all ~~four~~
**three** reach it.

> *Counts corrected in place 2026-08-16 (`wealthTensor-52`). This addendum is dated `-08` and the
> `-10` addendum below it — same day, hours later — folded Paper I into Paper IV. The batch ruling
> itself is untouched and still governs; only its arithmetic moved. Struck rather than deleted, per
> `-51`'s precedent at §Order of publication. **This is the third site in this file found asserting
> the four-paper count after `-10` amended it, and the second found after `-51` corrected the
> first** — the header's "the addenda amend it" policy is exactly what lets a superseded count keep
> reappearing in clauses a reader treats as live. Grep the CLAIM, not the file.*

**What this opens, and nobody has claimed it.** The end-to-end test is itself a deliverable and has
not been designed. **What would it mean for the ~~four~~ three papers to fail as a system, as opposed
to one of them failing?** That question has no written answer anywhere in this repository. It should have one
before the fourth paper is finished, not after — a test designed once the result is known is not a
severe test, which is the whole point of the position being recorded here.

---

### Addendum · 2026-08-11 · wealthTensor-10 · **Paper I folds into Paper IV. The corpus is three preprints.** — Jason's ruling

**Asked in -09 and not answered; asked again in -10 and answered immediately.** Jason's ruling:
**fold into IV.** The recommendation on the table was the same, so this addendum records a decision
rather than a change of course — but it changes the shape of the corpus and the Definition of Done,
so it is recorded at full length.

**What died, and it died twice.** Paper I was briefed as *Price formation without independent
curves*, re-scoped around P3 in -07 when the original claim proved one step weaker than its own code,
and the re-scope was killed in -08 along with its replacement. `RESULT-WT070-p3-is-dead.md` and
addenda 3 and 4 above carry the argument. **The paper was never written**, which is the one mercy in
the sequence: nothing is being retracted, only not-written.

**What survives is subsection-sized and it is real.** The identity

> **the crossing height IS the volume** — *D*(*p*\*) = *S*(*p*\*) = |*H* \ *T*|

survives every attack made on it, in -06, -07 and -08. It is a true statement about the object and it
is worth publishing. It is not worth a preprint.

**Why IV and not III.** Paper IV's charter — *composition across scales* — already covers the thing
the identity is about: a quantity defined at one level of aggregation turning out to be the same
object as a quantity defined at another. The identity is an instance of the charter rather than an
addition to it. **Paper III was considered and rejected as a force-fit**, and the WT-042 alarm was
audible when the option was raised: III is the reporting-layer paper and the identity has no
reporting layer in it. Grafting it there would have been placement by convenience.

**The Abandoned Approaches entry travels with it, and it is large.** Two dead framings, a re-scope,
the re-scope's replacement, and a registered prediction that failed. It will be the longest such
entry in the corpus and it is the part of Paper I with the highest teaching value — which is the
audience test that governs `docs/` (§Consequences), applied to a paper rather than a directory.

## What changes

| | before | after |
|---|---|---|
| **corpus size** | four preprints | **three preprints** |
| **submission batch order** | II → III → I → IV | **II → III → IV** |
| **Definition of Done** | "Four preprints publicly posted…" | **"Three preprints publicly posted…"** — every other clause unchanged |
| **Paper I's charter** | its own preprint | a subsection of IV, plus IV's Abandoned Approaches |

**What does NOT change.** The split itself, the per-paper Definition of Done clauses, `ADR-001`
§Order of publication's *reasoning*, and the -08 ruling that nothing ships until the corpus is done.
Paper I's existing documents — `paper-I.md`, `RESULT-WT070-p3-is-dead.md`, `REVIEW-002`, `REVIEW-003`
— **stay exactly where they are.** They are the record of how the decision was reached, and deleting
them would be the tidiness that manufactures a false history.

**And it sharpens the open question rather than shrinking it.** The end-to-end test (addendum 6,
still unclaimed) asks *what would it mean for the papers to fail as a system?* That question is
**easier to answer for three papers than four, and harder to dodge** — with I folded in, the corpus
is redistribution, the reporting layer, and composition across scales, which is a conjunction with a
shape rather than a list with four items. Whoever designs the test now has a smaller and better-posed
object to design it against.

*Recorded because a corpus that quietly becomes three papers, in a repository whose central document
says four, is a contradiction a future session would find the hard way.* (L35.)
