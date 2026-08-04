# Findings Ledger

Every serendipitous connection, open problem, dead end and piece of supporting
evidence — whether or not it survives into the manuscript.

**Dead ends are recorded with equal weight.** In a synthesis assembled over eleven
years the expensive failure is not losing a good idea; it is re-deriving a bad one
because nobody wrote down why it was abandoned.

Entry types: `CONNECTION` · `OPEN` · `EVIDENCE` · `RESULT` · `RISK` · `HYGIENE` ·
`METHOD` · `DEAD-END`

---

## WT-001 · CONNECTION · 2026-08-04
**Cournot corner solutions are the marginal pair from the reservation-price section.**

The Cournot test suite failed on its first run: costs `[8,9,10,11,30]` produce a
*negative* analytic output for firm 5. That firm is not loss-making — it is excluded,
because its marginal cost (30) exceeds the price the survivors set (27.6).

That exclusion boundary is exactly the manuscript's "marginal pair": the last agent
holding a unit and the first agent excluded. The Cournot chapter and the axiomatic
price-formation chapter describe the same object from two directions and currently do
not reference each other.

*Why it matters:* first genuine cross-chapter link found. Candidate spine for the
telescope layer. Implemented in `solve_cournot()`; hand-verified.

---

## WT-002 · OPEN · 2026-08-04 · **ADDRESSED IN TEXT** (items 1–3 written; item 4 unbuilt)
**Lambda's second component is dimensionally a price, and that is the paper's weakest wall.**

`eta_work_to_financial` has units `[currency]/[J]`. A free scalar converting a physical
substrate into observed money is the failure mode that sank Odum's emergy programme and
is structurally identical to the transformation problem. Unaddressed, it reads as
"tuned to fit."

Four-part defence, in priority order:
1. Ground it — it is the reciprocal of a published statistic (see WT-003).
2. **Demote it from parameter to dependent variable.** Do not derive price from energy.
   Measure the coupling and argue its *drift and variance* are the phenomenon: C rising
   against flat E is Lambda diverging, i.e. a bubble with a thermodynamic signature.
3. Express headline results as dimensionless (Buckingham pi) groups so the numeraire
   cancels.
4. Publish a sensitivity sweep showing conclusions invariant across orders of magnitude.

Item 4 is the empirical rebuttal and is the reason this repo exists. Not yet built.

---

## WT-003 · EVIDENCE · 2026-08-04
**Lambda^-1 is UN SDG indicator 7.3.1.**

Energy intensity of output is World Bank series `EG.EGY.PRIM.PP.KD` — "Energy intensity
level of primary energy (MJ/$2021 PPP GDP)" — and is formally SDG indicator 7.3.1,
co-tracked by the IEA. Global coverage, long time series.

*Why it matters:* converts "you invented a conversion constant" into "I inverted an
indicator the United Nations reports against." Single most efficient sentence available
for defending WT-002.

---

## WT-004 · RISK · 2026-08-04 · **RESOLVED IN TEXT**
**Georgescu-Roegen is a hostile witness inside our own bibliography.**

The manuscript quotes him: *"the real source of economic value is the subjective
enjoyment of life by individuals."* He is the most-cited authority in the biophysical
section and he explicitly refused the physical-to-monetary reduction that a naive
reading of Lambda proposes. A reviewer finds this immediately and it reads as not
understanding one's own source.

*Resolution:* WT-002 item 2 dissolves it. Measuring the wedge between physical
throughput and financial claims does not claim energy determines value — it measures the
gap Georgescu-Roegen said would exist. **This must be made explicit in the text**, not
left for the reader to reconstruct.

---

## WT-005 · RESULT · 2026-08-04
**Cournot tatonnement is unstable exactly where its own assumption is weakest.**

The linearised undamped best-response map has gain `(n-1)/2`: stable at n=2, marginal at
n=3, non-convergent beyond. Verified numerically across n and damping; output floored at
zero, so it oscillates rather than diverging.

*Why it matters:* the manuscript argues tatonnement rests on an expectation falsified
every period. The instability boundary makes that argument quantitative instead of
rhetorical — and damping, which rescues convergence, is an inertia assumption the
original model does not contain.

---

## WT-006 · METHOD · 2026-08-04
**The whitespace claim should be a citation-graph result, not a search anecdote.**

"I looked and found nothing" is the first thing a reviewer attacks. Instead: compute
co-citation between seed clusters (biophysical/Georgescu-Roegen-Soddy · stock-flow
consistent/Godley-Lavoie · kinetic exchange/Chakraborti). Near-zero inter-cluster
citation is *quantified evidence* of the gap.

Tooling: OpenAlex (CC0 full snapshot on public S3, no key required for bulk),
Semantic Scholar Academic Graph, Unpaywall for locked DOIs. Verify OpenAlex API key
policy at build time — official docs and a third-party report disagree as of 2026-07.

Hardware: `shellac` (Ryzen 9950X / 96GB / RTX 3090) is idle and sized for a local
snapshot with no rate limits.

---

## WT-007 · EVIDENCE · 2026-08-04
**The existing bibliography is already ~97% open access.**

Audit of the ~57 references: arXiv x4, PMC x4, IDEAS/RePEc x3, financialresearch.gov x3,
plus EconStor, NBER, PLOS, Frontiers, PDXScholar, Digital CSIC, Bank of Greece, JASSS and
numerous university-hosted PDFs. One or two paywalled entries total.

*Why it matters:* no institutional subscription is required for this project. Econophysics
and heterodox macro are preprint cultures. The access anxiety was unfounded.

---

## WT-008 · HYGIENE · 2026-08-04 · **FRAGMENTS FIXED** · checkboxes still deferred
**Six duplicated/orphaned sentence fragments in the manuscript.**

Each sits immediately after an italicised formula — the tell of a paste that split text
following a formula run. Includes two fully duplicated paragraphs (Transformation
Efficiency Vector; the closing paragraph of Project 3) and a stray solitary period.

Restore point taken and verified before any edit:
`RESTORE POINT 2026-08-04 — Axiomatic Reconstruction of Wealth (pre-Claude-edit)`
(40,052 chars · 253 paragraphs · 4 tables). All six defects removed 2026-08-04 (716 chars, arithmetic reconciled) and verified absent by independent read-back. Checkbox-list question remains unanswered.

Also deferred: all bulleted lists in the manuscript are *checkbox* lists, including all
57 references. Intent unconfirmed.

---

## WT-009 · HYGIENE · 2026-08-04 · DEFERRED
**A twin document exists and its title lies.**

`2The Axiomatic Reconstruction of` (19KB, 2026-08-03) sits alongside the canonical 29KB
version. Title truncated mid-sentence. Not yet diffed; unknown whether it is an earlier
draft, a partial export, or holds unique content the canonical copy lost.


---

## WT-010 · METHOD · 2026-08-04
**Google Docs API: two formatting traps, both found the hard way.**

1. **Insertion inherits the style of the paragraph you insert into.** Inserting at an
   index that is the *first character of a heading* silently gives every inserted
   paragraph that heading's style. Eight body paragraphs came out as H2. Symptomless in
   the API response — it reports success. Only a read-back reveals it.
2. **Applying `NORMAL_TEXT` wipes character formatting that spans the whole paragraph.**
   A partial bold run survived; a full-width italic run did not. Apply paragraph styles
   *before* character styles, never after.

*Standing rule for this project:* every batch of doc edits is followed by an independent
read-back that checks rendering, not just the API's success reply. The API reporting
"6 operations succeeded" says nothing about whether the result is correct.

---

## WT-011 · HYGIENE · 2026-08-04 · FIXED
**Body paragraph absorbed into a checkbox list.**

"To capture financial capitalism, this exchange framework is extended to the loan
interest model..." was glued to the final item of the Policy Interventions list, so it
rendered as a list item rather than as body prose. Bullet removed, paragraph normalised.

Found by the verification subagent as an incidental observation while checking something
else — an argument for having the verifier look at the whole document rather than only
at the diff.
