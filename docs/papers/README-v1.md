# The v1.0 drafts

Two papers and one figure suite, built 2026-08-26 on branch `paper-rebuild`.

| file | what it is |
|---|---|
| `paper-III-dual-tensor/paper-III-v1.md` | **Two firms file the same numbers** — paper III rebuilt to lead with the identification theorem. |
| `paper-II-redistribution/paper-II-v1.md` | **A levy cannot tax what its base cannot see** — paper II sharpened, with the outcome/generator distinction promoted. |
| `wt-figures.html` | Nine figures across both papers in one visual language. Open in a browser. |
| `../../scripts/wt221_paperII_figure_data.py` | Regenerates paper II figure data from the committed model. |
| `../../scripts/wt222_paperIII_figure_data.py` | Regenerates paper III figure data. |

The v0.x drafts (`paper-III.md`, `paper-II.md`, `paper-IV.md`) are untouched on `main` and still
tagged `v1.0-preprint`, with all guards passing. Nothing here overwrites them.

---

## Paper IV is not carried forward

Its thesis is that the three scales are one structure — the manuscript's own phrase for it,
quoted in the check below, is *"a chain rather than three analogies"*. The corpus's own
end-to-end check (`docs/RESULT-END-TO-END-001-E1.md`) put that assertion under test and **failed it at leg `E1a`**: *"ρ and φ are not the same kind of object, so the join between Papers II and III is vocabulary at the sovereign scale."*
`paper-IV.md` now opens with a stood-down header saying so and naming where each surviving part
went. **The redistribution was completed at wealthTensor-108** and is this:

| paper IV's part | disposition | why there |
|---|---|---|
| **The SMD-as-boundary argument** (§4) | **Landed** — paper III, Appendix **A.4**, *"The boundary on P3, and it is a fifty-year-old theorem."* | Appendix A.2 already names P3 (atomism) as "where this framework's commitment actually bites". SMD is the strongest non-strawman objection to P3, so the boundary belongs against the proposition rather than in §11 Limitations, which is about *this paper's results* and not about the framework. Six references travelled with it, each verified against Crossref or the publisher's page on 2026-08-26. Its limit 2 was remapped to paper III's own §5 and limit 3 to §9.5. |
| **The crossing-height instance** (§5) | **Retired from the papers, kept whole** at `docs/RESULT-CROSSING-HEIGHT-001.md`. | It was *not* folded into paper III §5.6. The two objects share the English word *crossing* and no operator: §5.6's crossing is a threshold in δ at which a published ranking inverts; this one is the *ordinate* of a Marshallian intersection, and it measures allocation mismatch. Folding them would have repeated inside the repair the exact identification error `RESULT-END-TO-END-001-E1.md` caught. §0 of that file argues the refusal at length. |
| **The pre-registered citation-whitespace instrument** (§6) | **Standalone method note** at `docs/METHOD-002-citation-whitespace.md`, beside `METHOD-001`. | Neither surviving paper claims a three-literature junction, so nothing rests on it. Paper III §13 was refused as a home on a narrower ground: it enumerates the registrations that produce paper III's *numbers* (PRE-001, PRE-002, REG-003–008), and REG-013 produces none of them — filing it there would make §13 false about its own scope. |

**Nothing was dropped without a home.** The guard
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` outlives the manuscript it was
written for, and paper II §7 already says so in the manuscript of record.

---

## What else wealthTensor-108 repaired on this branch

The v1 rebuild landed with five red guards. All five are settled here — four repaired, and the
fifth **declared** rather than faked.

- **Sixteen orphan reference entries in `paper-III-v1.md`.** The rebuild cut 788 lines of paper III
  and the reference entries those sections carried stayed behind. Thirteen were deleted (the
  crash-risk block — Andreou, Fama, Hutton, Jin, Zhu — and Elbers & Ridder, Hayek, Little,
  Mann & Whitney, Mayo & Spanos, Mises, Piketty, Popper). **Three were the opposite defect and were
  restored to the body instead**: "severe test" is Mayo's (1996) term and headed §9 unattributed;
  the registration discipline §9 reports is Nosek *et al.*'s (2018); and §12's "not new as a
  structure" claim about stock-flow-consistent modelling named nobody, where it means Godley and
  Lavoie (2007). All thirteen deleted entries survive in `paper-III.md` on `main`.
- **Four stale "Cited in §N.M" claims**, casualties of the same renumbering the rebuild performed:
  Fisher, Kay and Long claimed §5.2 and are named in §6; Ryan (1995) claimed §7 and is named in §7.3.
- **A dangling pointer.** Appendix A's preamble promised the full development at
  `docs/appendix/A-framework.md`, and that file did not exist on any branch. It does now —
  paper III v0.x's Appendix A extracted verbatim, with its own provenance header.
- **Two class-A cross-reference false positives** recorded in `docs/crossref-dismissed.tsv`, which
  keys on the manuscript stem and therefore did not carry over to the `-v1` files.
- **Declared outside the capture, and therefore green.** `docs/deliverable/LAYOUT-MANIFEST.json`
  describes only the v0.x corpus — the four `paper-*.md` files, 147 pages — and that is now a
  *stated* fact rather than a standing red. `docs/deliverable/NOT-IN-CAPTURE.tsv` carries one row
  per `-v1` draft saying it is deliberately outside the built PDF and why, so
  `scripts/wt179_manifest_guard.py` reports **10 checks, 0 findings** instead of a permanent "you
  forgot to rebuild" about a manuscript that could not possibly be in the capture. Delete a row and
  the guard goes red on the next run, which is how that file is audited rather than trusted.
  **Still true, and the reason the row is a declaration and not a hash:** never add `-v1` hashes by
  hand. When a draft becomes v1.0 its row comes out and the deliverable is rebuilt **from a clean
  tree** — `build.sh` stamps `source_commit` from HEAD, so a dirty build makes the manifest name a
  commit it was not built from, and only `verify-layout.sh` can see that.
