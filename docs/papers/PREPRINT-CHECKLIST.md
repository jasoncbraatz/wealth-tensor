# Per-paper preprint checklist

ADR-001 converted "the missing apparatus" from a vague worry into a checklist. This is it. Paper
II builds the template; I, III and IV inherit it, so a gap fixed here is fixed four times.

**Verified 2026-08-05 (S3)** against the current arXiv and SSRN documentation, not from memory —
venue rules are exactly the kind of fact that rots in a training set. Re-verify before submitting;
the sources are named at the bottom so the next session re-checks rather than re-researches.

---

## A · Apparatus every paper must carry

WT-047 measured the manuscript and found **zero** occurrences of every item below. All are cheap
and none is optional in 2026.

- [ ] **Title** — a claim, not a topic. "The base caps the region, the rate moves you within it"
      beats "On redistribution in kinetic exchange models."
- [ ] **Author block** — name, **Independent researcher**, email. State the affiliation plainly;
      an empty affiliation line reads as an omission, "Independent researcher" reads as a fact.
- [ ] **Abstract** — 150–250 words, and it must contain the *numbers*. A reviewer decides here.
- [ ] **Keywords** — 6–8.
- [ ] **JEL codes** — an economics convention with no CS analogue, and its absence is a tell that
      the author is from elsewhere. Paper II uses D31, D63, H23, H24, C63.
- [ ] **Explicit numbered contributions list** in the introduction. Now expected; its absence
      forces the referee to construct one, and they will construct a smaller one than yours.
- [ ] **Abandoned Approaches** — load-bearing in *every* paper per ADR-001, populated from the
      ledger's DEAD-END entries and from any claim that half-failed. Not an appendix.
- [ ] **Limitations** — numbered, and at least one must run *against* the paper's own comfort. A
      limitations section containing only limitations that do not matter is an advertisement.
- [ ] **Data and code availability** — repository URL, module path, the exact regeneration
      command, the test command, and **the commit SHA pinned at submission**.
- [ ] **Related work as positioning, not survey.** State what is established, then what is new.
- [ ] **No live placeholders.** WT-047 found *"Further entries to be migrated from the project
      findings ledger as they accumulate"* sitting in the deliverable. The handoff gate refuses
      placeholders; the manuscript has no such guard, so this checkbox is the guard.

## B · The reproducibility paragraph — the largest unexploited asset

Five modules, 58+ tests, every figure regenerable from two scripts, in a **public** repository, in
a field with a known-poor replication record. This is worth more than any single result and it
costs one paragraph. Every paper carries it, naming `github.com/jasoncbraatz/wealth-tensor` and
the commit SHA.

Two of the tests exist specifically to make overclaiming fail loudly
(`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`,
`test_a_flat_gini_does_not_mean_a_bounded_one`). Say so. A test suite that constrains the author
is a different object from one that flatters him, and a referee who notices the difference is a
referee who starts reading in good faith.

## C · Venue, verified 2026-08-05

| | arXiv (q-fin, econ.GN) | SSRN |
|---|---|---|
| **Endorsement** | **Required** before a first submission to a category. At least one positive endorsement per endorsement category. | **None.** A free account with a complete author profile is the requirement. |
| **Endorser** | Must have published in the domain within roughly the last 3–5 years, and is asked to confirm the paper is *appropriate for the subject area* — not that it is correct. | n/a |
| **Affiliation** | Not formally required, but an unaffiliated first-timer must find a personal endorser. | Not required. |
| **Rejection** | Can be reclassified or held; the process is visible. | **Final. No individualised reasons given. No reconsideration.** |

**The asymmetry that should drive sequencing, and it is sharper than "SSRN is easier".** SSRN has
no gate on the way in and no appeal on the way out. arXiv has a gate on the way in and a
conversation on the way out. So SSRN is *not* the low-stakes rehearsal venue it first appears to
be — a rejection there is silent, permanent and uninstructive. The rehearsal value of Paper II is
in **assembling the apparatus**, not in treating the submission itself as a cheap draw. Submit II
when it is right, not when it is ready to be experimented with.

**Practical consequence for the endorsement path:** the endorser is asked whether the paper
belongs in the category, so the ask is far easier once a paper exists in public with a clean
apparatus and a public test suite. II on SSRN first, then the endorsement ask for III, is the
order ADR-001 already chose — and this is a second, independent reason for it.

## D · Pre-registration, where a paper carries an empirical claim

Papers III and IV carry empirical predictions; I and II do not. Where one does:

- [ ] The prediction is registered in `docs/preregistration/` **and committed before the result
      exists**, so the git history is the timestamp.
- [ ] The paper cites the pre-registration file *and the commit SHA of its registering commit*.
- [ ] The result reports the drop accounting, not only the survivors.
- [ ] Where the prediction failed, the failure is in **Abandoned Approaches** at full strength.

---

## Sources

- [arXiv endorsement policy](https://info.arxiv.org/help/endorsement.html)
- [SSRN submission guidelines](https://www.elsevier.support/ssrn/answer/get-started)
