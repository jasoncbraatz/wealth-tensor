# REVIEW-001 · Internal adversarial referee report on Paper III v0.1, and the responses

- **Draft reviewed:** `paper-III.md` v0.1, 2026-08-10, session wealthTensor-04.
- **Reviewer:** an adversarial agent instructed to find reasons to **reject**, given the draft, the
  ADR, the checklist, the pre-registrations, the ledger and the sibling paper. It was told not to
  praise and not to summarise.
- **Verdict returned:** *Reject with the option to resubmit.* 16 findings, 2 FATAL.
- **Status:** all FATAL and all integrity-critical SERIOUS findings addressed in **v0.2**, same
  session. Remaining items are listed below as open with their disposition.

**Why this file exists and is public.** `docs/` is a working lab notebook by decision (ADR-001
§Consequences). A paper whose central claim to seriousness is that it reported its own failed
prediction cannot then suppress the review that told it the reporting was still too flattering.
The referee's two FATAL findings were both of that kind, and both were right.

---

## The two findings that mattered most

**F1 · The paper certified that losing the bet cost it nothing.** §6.1 said every result in §3 and
§4 was "unaffected" by the failure; §6.3 claimed the framework had thereby escaped the trap that
closed on emergy. Those cancel. If nothing was at risk, nothing was on test, and a framework that
keeps every claim after losing its only public bet is *in* the trap, not out of it.

*Response (v0.2 §6.1):* accepted in full. The paper now states the accounting explicitly — what was
at risk and lost (the conjunction of model, bridge and unit of observation, which was the
framework's entire empirical content), what was never at risk (the §3/§4 theorems, which could not
have lost), and the consequence: **the framework currently has no confirmed empirical claim.**

**F2 · §6.3 converted the loss into a virtue claim, and its disclaimer performed the thing it
denied.** "It is not offered as a consolation prize" does not stop the preceding two sentences from
being one. The reference class was chosen so that any loss became a comparative win, and it sat at
the end of the section, so it was the last thing a reader carried away from the failure.

*Response (v0.2 §6.3):* the Odum comparison is **withdrawn**, and the withdrawal is what the
section now reports. The referee also observed that the paper announced its own integrity in the
abstract, §1, §5.2, §7, §9 and §10 — and that by the paper's own rule in §3, *a defence that recurs
is a tell*. Five of those instances were cut.

---

## The finding that was about the project, not the paper

**F3 · The git-timestamp discipline does not cover the test the paper reports.** PRE-001 was
committed alone at `9722342` before any analysis code existed — exemplary. But the reported result
comes from **PRE-002**, whose registration shipped in commit `d655501` *together with the
implementation of its own instrument*. The result came later, so the registration still precedes
the outcome; what is no longer demonstrable is that the instrument's details — onset window,
tie-break direction, materiality floor — were fixed before anyone saw what they produced. On a
second look, that is exactly where the remaining researcher degrees of freedom live.

*Response:* disclosed in v0.2 §5.1 and in §10, at the strength the referee stated it. The programme
rule is amended: **a registration must precede the instrument's code, not merely the result.** See
`docs/LEDGER.md` WT-052. This is a real methodological gap in work already done and it cannot be
repaired retroactively — only disclosed.

---

## Substantive findings accepted and fixed in v0.2

| # | Finding | Disposition |
|---|---|---|
| F4 | "Evidence of absence" unsupported: the power sim assumes error-free onset, treats 688 events from 311 firms as independent, and the one-quarter-per-tier effect was never derived from the model. Contradicts §6.2 — the bridge cannot be too broken to license a prediction *and* sound enough to license its refutation. | Phrase removed; three qualifications now sit next to the power table; claim restated at the strength the evidence carries. |
| F5 | §4.3 (the efficient-markets reply) is a free parameter absorbing an objection — φ is unmeasured, so the partition concedes every checkable case and claims every uncheckable one. The evidence that was to license it *was* WT-026, and WT-026 failed. | §4.3 rewritten as an **open problem, not a reply**, and added to *Abandoned Approaches*. |
| F6 | "Λ" denoted two different objects — the dimensional coupling η·C/E and the dimensionless ratio C/E — in the section the paper calls its most-attacked. | Notation introduced in §3.1: **Λ** dimensional, **λ** dimensionless. |
| F7 | The entailment argument equivocates: "some relation must exist" does not entail "a scalar exists", and the objection is to the scalar. Plus an "only open questions" uniqueness leak. | Narrowed explicitly: the coupling is entailed, its **representability as a scalar is an additional assumption this paper makes and does not prove**. |
| F8 | SDG 7.3.1 stated as an identity in the abstract; it is a **flow/flow** ratio where Λ is **stock/stock** — the same type error §6.2 diagnoses. And if no conclusion depends on Λ's value, anchoring the value is not load-bearing. | Identity claim withdrawn; stock/flow mismatch named; the leg is now explicitly labelled weaker than §3.3 and non-load-bearing. |
| F9 | **Scope violation.** §2.3 imported Paper II's headline empirical result as evidence inside Paper III's argument — the exact alarm ADR-001's 2026-08-10 addendum §4 had been written to listen for, *earlier the same session*. Plus four near-verbatim passages shared with Paper II. | Result now cited, not reproduced. Three duplicated passages rewritten. |
| F10 | Variance concentration promoted to the abstract as "a sharper empirical target" — but PRE-001 had already recorded that this exact statistic *cannot fail* against accounting data and excluded it "so no future session re-discovers it as a finding." It was re-discovered as a finding. | Disclosed in §4.4; explicitly **not** offered as the replacement severe test. |
| F12 | Apparatus: abstract 327 words against a 150–250 limit; drop accounting absent; §3.3's scaling-collapse figures existed only in the test suite and were produced by no regeneration script — violating a checklist rule added *the same day* after WT-027's hand-transcribed table was found not to regenerate. | Abstract cut to ~250. Drop accounting pointer added to §10. `scripts/wt002_lambda_report.py` extended with the collapse, with its 300-period horizon disclosed. |
| F13 | Uniqueness leaks in the world's voice ("the only thing a deferral can eventually do"). | Rewritten as a claim about the model. |
| F15 | §5.3 softened by omission: both z-statistics run opposite to prediction, and **tier 2 carries the longest median lag in both universes, with goodwill below it** — the sharpest description of the failure, present in the repo and absent from the paper. | Added to §5.3 verbatim in substance. |
| F16 | §2.1's discriminating example was a strawman: neoclassical economics does not deny physical depreciation (δK is in Solow). | Replaced — the commitment that actually bites is **P3**, not P2. |

## Open, with disposition

- **F11 · λ's "shape prediction" forbids nothing. — CLOSED, same session.** §3.1 stopped calling
  λ's instability "the paper's primary observable", and **§8 Limitation 4 was rewritten from a bare
  concession into the paper's sharpest limitation**: φ is ill-conditioned when estimated jointly
  with the effective decay δ, because it reaches the observable only through the product φδ, so
  φ = (α − k)/δ and the variance grows like 1/δ². Measured like-for-like: δ free → median 0.211,
  δ pinned → 0.00073, a 291× improvement. §7 gains a matching abandonment ("Estimating φ from the
  reported series alone") that states the obstacle and deliberately **not** the instrument, so a
  future PRE-003 is not pre-announced. Method and figures:
  `docs/notes/NOTE-001-phi-identifiability.md`; WT-056.

  **Two audit passes on that addition found ten further errors, seven of them flattering** — a
  symbol collision (δ written as d, understating the divisor 2.5×), a cherry-picked best case, an
  overclaim of "cannot be recovered" where the result is conditioning, a cross-script comparison
  described as "the same fit", a hardware figure attached to the wrong experiment, dropped p90s in
  the one sentence they undercut, and a claim that two existing tests guarded Limitation 4's
  collapse when **it had no test at all**. It has one now:
  `test_the_two_layer_recursion_collapses_to_the_form_limitation_4_publishes`. NOTE-001 §5 records
  the full list, because that section teaches more than the finding does.
- **F14 · §3.3's tables need their parameters in the caption. — CLOSED, wealthTensor-05.** The two
  diagnostics now carry the paper's names in §3.3's table and in the scaling-collapse prose, with the
  module identifiers (`variance_suppression`, `variance_concentration`, `n_crises`) disclosed once in
  the caption so the report script stays traceable. Closing it turned up a fourth slip of the same
  family: §4.4's own table said *inter-crisis smoothing* where the abstract, §3.3 and §4.4's method
  note all say *inter-correction*. Fixed. **Left for Jason, not decided here:** the paper uses
  *correction* 29 times and *crisis* 12 times for the same event, and the title is built on *crisis*
  — that is a vocabulary choice, and vocabulary is his.
- **Piketty relocation (§9)** performs a move ADR-001 allocates to Paper IV. Referee rated MINOR;
  positioning is required by the checklist. Left as is, flagged for the Paper IV session.
- **References — CLOSED for bibliography, ONE ITEM OPEN for provenance, wealthTensor-05.** All seventeen verified against publisher pages, library
  catalogues, Crossref and issuing-body documentation, and marked ✓. The check found more than
  bibliography: **seven entries were listed and never cited in the body.** Six were given the work
  they were listed for (§5.1 the FASB topics, §5.2 Mann & Whitney, §9 Fama, Popper, Mayo and Nosek);
  Chakrabarti et al. was removed as Paper II's literature rather than retro-fitted. A referee reading
  the list against the text would have found this before reading a single equation.

---

*A note on method, since the audience for `docs/` includes people learning how this is done.* Two
agents were run against the draft: one checking every number against the code that produced it, one
trying to reject the paper outright. The first found four numeric errors, including a conflation of
two universes' statistics **inside the section about honesty**. The second found that the honesty
section was still, in three separate places, grading its own homework. Neither would have been
caught by re-reading. The cost of both was a few minutes; the cost of a referee finding F1 instead
would have been the paper.*

## Open, added wealthTensor-05

- **Four cited books are not in the author's library, and he cannot say which edition he read.**
  A provenance pass against his own digitised collection (`~/Desktop/downloads` and the `BOOK MASTERS`
  archive, both copy-matched to prints he owned before donating them) located **Popper, Soddy,
  Georgescu-Roegen, Piketty and Chakrabarti** and corrected three of those citations to the edition
  actually consulted. It did **not** locate **Mises (*Human Action*), Godley & Lavoie (*Monetary
  Economics*), Mayo (*Statistical Inference as Severe Testing*) or Odum (*Environmental Accounting*)**.
  All four are cited in §7 or §9. Journal articles are excluded from this finding — a book archive is
  not expected to hold them.

  This is **not** an accusation that the works were not read; it is the observation that the citation
  cannot presently name an edition on the same evidence the other five can. Two of those four carry
  more weight than the other two: §9 cites **Mises** specifically for *malinvestment*, which predates
  *Human Action* (1949) by decades, and §7 rests an entire withdrawn comparison on **Odum**. Resolving
  it needs the author, not a session.
