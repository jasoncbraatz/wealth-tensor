# RESULT · REG-001 · **NO VERDICT.** The instrument was mis-specified in four ways.

- **Registered:** 2026-08-11, `docs/preregistration/REG-001-p3-second-layer.md`, committed and
  pushed alone before any line of the instrument existed (WT-052).
- **Instrument:** `scripts/wt066_p3_port.py` + `src/wealth_tensor/recognition_fold.py`.
- **Outcome:** **The registered test returns no verdict on P3's portability.** Not a pass, not a
  fail. Three of its four checks are incapable of firing, and the fourth is not robust to
  parameters the registration left free.
- **Caught by:** the WT-065 adversarial pass, fired before a ledger entry, before any paper text,
  and **before Jason was told.** That is the first time the moved trigger has paid for itself.

---

## 1 · What was claimed, and what is withdrawn

The re-scope of Paper I around **P3 · Atomism** needs the fold-invariance to do work somewhere
Wicksteed's subjective-value apparatus cannot follow. REG-001 registered a port to an
accounting-recognition layer to test exactly that, with the falsifier stated in advance.

The instrument ran. H1 passed. H2a failed in all five live regimes. **The interpretation drafted
from that — "fold-invariance is a property of measurement that does not transfer to mechanism,
because the count R is exogenous in the price layer and an endogenous state variable in the
recognition layer" — is WITHDRAWN IN FULL.** It was never entered in the ledger, never written
into a paper, and never reported as a finding. It is recorded here because the *reasons* it
failed are worth more than the claim was.

## 2 · The four defects, in descending order of severity

### D1 · The port is layer-free. It is the price layer under a sign flip.

Set *m* = −*τ*, *p* = −*s*, *H* = *B*. Then `#{i∉H: mᵢ>p}` **is** `#{i∉B: τᵢ<s}` and
`#{i∈H: mᵢ<p}` **is** `#{i∈B: τᵢ>s}`. Demand *is* pending; supply *is* reversible; *z*(*p*) *is*
*n*(*s*). Verified pointwise on the same 399 interior grid points: both halves agree exactly at
every point.

`RecognitionLedger.run()` touches four things — `tau`, `v`, `booked0`, `s` — and not one operation
in it is recognition-specific. **A script invariant to the interpretation of its arrays cannot
produce evidence about a difference between interpretations of its arrays.**

This is **force-fit, not form-fit** (WT-042), and ADR-001 §4 named the exact alarm to listen for.
It did not fire, because the person who should have heard it wrote the thing.

### D2 · The negative control is not a control, and this is the second time this session

`tie_break="index"` sorts by the item's position in the global array. The module docstring asserts
this "smuggles the labelling back in through the ordering." **It does not.** The array index is a
fixed per-item attribute, identical across all 25 labellings — exactly as much a property of units
as *τ* is. Both rules are functions of (pending set, unit attributes); neither reads *B*.

Measured across the six regimes, distinct timings:

| rule | regimes |
|---|---|
| treatment (threshold order) | 1, 2, 2, 2, 2, 3 |
| "control" (index order) | 1, 3, 2, 1, 3, 3 |
| a genuine label-reading rule | 1, 3, 2, 1, 4, 3 |

The control is indistinguishable from the treatment and in one regime is *more* invariant than it.
By the module's own stated criterion — *"a test suite that cannot distinguish it from the real rule
cannot detect failure at all"* — **this guard cannot fire.**

**This is the `4/21 < 4/11 < 4/7 < 4/3` defect, committed in the session that quoted it as a
lesson, inside a control built specifically to prevent it, whose docstring names the lesson.**

### D3 · H3 and H2b have empty failure sets

- **H3** fires if aggregate-coupled recognition breaks **H1**. H1 is an algebraic identity from a
  two-set partition, true for every *B* with |*B*| = *R* whatever the dynamics. It has no failure
  mode. **H3 is a falsifier that cannot falsify.**
- **H2b** scores "magnitude varies" as a pass. With continuous i.i.d. *v* and 25 distinct pending
  pools, 25 distinct sums is a probability-1 event under *any* mechanism — including the variant
  where H2a passes. **H2b carries zero information.**

That leaves H2a as the only check with content. Sweeping the two nuisance parameters REG-001 §6
did not fix — threshold dispersion, and the scrutiny path, which is **nowhere registered** — over
90 live regimes, **H2a passes in 18 % of them.** "Fails in all 5 live regimes" is a draw of 5 from
a distribution with roughly a one-in-five pass rate, on an axis the registration left free.

### D4 · The result was refuted by construction, and the refutation was already in our own data

Two properties separate the price layer's mechanism from the port's: the market's mechanism reads
**the fold** (clearing is determined by *z*), and the label **count is conserved** — a reallocation
is a *permutation* of holdings, which is what "allocation" means. The port implemented neither: it
triggers off `pending`, one half, and it creates and destroys membership in *B* at unequal rates
(`k = ceil(α·n_pending)` booked against `j = ceil(α·n_rev)` reversed).

Restore both and the registered expectation is met exactly — across all six configurations:
**distinct timings 1, distinct magnitudes 25, distinct terminal booked sets 25.** H2a PASS, H2b
PASS, under dynamics that are still endogenous, still aggregate-coupled, still path-dependent, and
still composition-divergent. **So "invariance of measurement does not transfer to mechanism" is
false as stated.** It transfers precisely when the mechanism reads the invariant and the count is
conserved — which is the configuration the price layer is in and the one the port failed to build.

**And the isolation run said so, and it was read backwards.** Re-driving the rate off *n*(*s*)
returned timings (2, 1, 1, 3, 1, 1). One is vacuous; of the **five live regimes, three passed.**
Moving the mechanism from a half to the fold took H2a from 0/5 to 3/5 — a large effect in exactly
the direction the hypothesis predicted — and it was written down as "REFUTED." Closing the second
channel takes it to 5/5.

## 3 · Priority, audited separately, and it is worse than the defects

An auditor told that an over-eager priority claim is as damaging as a missed one (L28) returned
**ADJACENT trending to PARTIALLY DISPLACES** on the general proposition, and named four independent
literatures in which it is standard equipment:

- **Markov-chain lumpability** — Kemeny & Snell (1960). A state aggregation exact for the
  measurement requires an extra rate condition to be valid for the dynamics. This is the claim,
  as a theorem, sixty-six years old.
- **Mori–Zwanzig projection-operator coarse-graining.** "The coarse-grained observable is not a
  state variable" is graduate coursework in statistical physics.
- **Granovetter (1978)**, read in full, verbatim: *"Groups with similar average preferences may
  generate very different results; hence it is hazardous to infer individual dispositions from
  aggregate outcomes."* Threshold populations, the same domain.
- **Pesaran & Chudik (2014)**, read in full: the long-run object aggregates cleanly while the
  short-run dynamics does not.

Estimated probability a specialist recognises it instantly as known: **~0.80–0.85** (economic
theorist), **~0.90** (statistical physicist). *"Expect a one-line referee report: 'this is
coarse-graining; see Zwanzig.'"*

**Unread and named as the largest live risk: Forni & Lippi (1997),** *Aggregation and the
Microfoundations of Dynamic Macroeconomics* — an entire book on aggregation versus dynamics,
paywalled, not accessed. The auditor refused to infer its contents and so does this file.

## 4 · Disposition, and the stopping rule

**REG-001's stopping rule stays fired. No second port is built this session.** The temptation to
rebuild with a conserved count and a fold-driven trigger — which the refuter has already shown
passes — is precisely the hypothesis-fitting §5 exists to forbid, and the fact that the repair is
*known to succeed* makes it worse, not better.

**A gap in our own doctrine, found here and worth a rule.** REG-001 §5 cannot distinguish
*repairing a demonstrably mis-specified instrument* from *fitting a hypothesis*. Those are
different acts and the registration gives no test to tell them apart. Until one exists, the
conservative reading holds and the port stays dead.

**What Paper I may claim as a result of this:** nothing. The P3 re-scope is **neither supported nor
refuted**. The generality remains **unexercised**, and Paper I's limitations section must say so in
those words rather than gesture at a second layer it does not have.

## 5 · The one thing worth being pleased about

The moved trigger worked. WT-065 says adversarial review fires when a finding is about to be
**called** a result — ledger, paper, or Jason, whichever is first. Under the old WT-054 rule this
would have been reviewed at preprint time, four artifacts and one conversation too late, exactly as
in wealthTensor-06.

Instead the gap between finding and disbelieving was **one tool call**, and the cost was a few
minutes of agent time. The instrument was built, run, interpreted, refuted, and buried without a
single false claim reaching the ledger or Jason.

*And the joke is on the author.* This session opened by quoting the `4/21 < 4/11` guard as the
lesson a previous session should have caught — and then shipped its own, in a control whose
docstring cites it. A defect that recurs is a tell. **It is now recorded twice, which means the
next session gets to find the third one.** 🪃
