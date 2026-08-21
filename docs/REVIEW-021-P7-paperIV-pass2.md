---
new_instrument: none
instrument_name: "— (all five axes inherited; Paper IV was 5 of 5 before this pass and the grid closed at -80, so NO cell could be filled. This is the first pass in the project's history run on a CLOSED grid, which is the condition -80's coverage reading needed to be tested in.)"
findings_from_new_instrument: 0 of 9
residue_of_previous_pass: 2 of 9
shape_promise_about_artefact: 5 of 9
shape_deferral_with_empty_target: 2 of 9
shape_neither: 2 of 9
manuscript_edits_required: 9 of 9
# FALSIFY THIS ROW, SIX WAYS.
#   1. `none`: the axis matrix in docs/p7-passes.tsv read 15 of 15 at the parent commit c3b1b31.
#      If any cell for paper-IV was empty there, this at-bat was misassigned and the row is wrong.
#   2. `0 of 9`:  §2 credits each finding to the axis that produced it. If ANY finding traces to
#      an axis this manuscript had not already had, the matrix was wrong, not this row.
#   3. `2 of 9`:  git blame every site at c3b1b31. IV-1 and IV-3 blame to 7ca35c7 (-75); the other
#      seven blame to 5efe626 (-53), the commit that first added the manuscript. Re-run the blame.
#      If a third site blames to -75 or later, this row is wrong.
#   4. `9 of 9` manuscript edits: scripts/wt144_paperIV_p7pass2.py touches paper-IV.md ten times
#      for nine findings (IV-7 has two sites). If any finding is repaired outside the manuscript,
#      the count is wrong. -79's proposed narrower rule and the current rule agree on this pass.
#   5. the shapes: §2's shape column. -80 found 5/2/2 on Paper III. This pass found 5/2/2 on
#      Paper IV. If a re-read of §2 against REVIEW-019 §6's two definitions moves any finding
#      across a column, the replication is weaker than this row claims.
#   6. the count itself: scripts/wt144_paperIV_p7pass2.py carries fifteen post-conditions and
#      scripts/wt145_paperIII_sec54_command.py five. Run both; they are idempotent.
# Ledger of all eleven passes: docs/p7-passes.tsv
---

# REVIEW-021 · Paper IV's SECOND independent `P7` read — the first pass on a closed grid

**Session:** `wealthTensor-81` · **Date:** 2026-08-18 · **Manuscript:** `docs/papers/paper-IV-composition/paper-IV.md`, **766 lines read end to end** (796 after repair)
**Patch of record:** `scripts/wt144_paperIV_p7pass2.py` (15 post-conditions) · sibling repair `scripts/wt145_paperIII_sec54_command.py` (5 post-conditions)
**Result:** **nine findings, nine repairs, zero carded.** Paper IV's counter goes 6 → **9**.

**THE ASSIGNED FALSIFIER, ANSWERED, AND THE ANSWER IS NO.** `-80` proposed COVERAGE OF THE AXIS
MATRIX as the mechanism behind the non-decaying counter: three frozen passes on a manuscript at
5 of 5 returned 3, 2, 2, and `-80` returned 9 on one at 2 of 5 with eight of the nine from the
three newly-filled cells. The prediction that follows is unambiguous — **a pass with no cell to
fill should return materially fewer than nine.** This pass had no cell to fill. It returned
**nine**, and **nine of the nine came from cells that were already filled.** Coverage is dead.

**FOUR MECHANISMS ARE NOW REFUTED BY THE PASS IMMEDIATELY AFTER THE PASS THAT PROPOSED THEM.**
New instruments (`-71`, `-77`), repair residue (`-78`), depth of application (`-79`), coverage
(`-81`). That is four for four, and §5 argues the four-for-four is the finding — not any of the
four mechanisms.

---

## 0 · What is NOT claimed here

Nine findings on Paper IV's second read is **not** evidence that Paper IV is worse than Paper II
at read nine. A rival explanation this pass cannot control is READ DEPTH: a manuscript on its
second full read has more unexamined surface than one on its ninth, whatever the matrix says.
§5 states what the existing rows do and do not do to that rival — briefly, Paper III went 7 → 9
across its first two reads and Paper II's nine reads ran 9, 2, 4, 3, 4, 5, 3, 2, 2, so read depth
predicts neither series either.

What this pass DOES settle is narrower and it is what it was sent to settle: **whether coverage
explains the counter.** It does not. That is a refutation, not a theory.

No finding below required re-running the severe test's science, and no finding below is a matter
of taste. Every one is checkable in under a minute by a reader with the repository, and each
carries the command that kills it.

---

## 1 · THE FIVE AXES, RUN BEFORE A WORD OF PROSE

| axis | what was run | count | findings |
|---|---|---|---|
| **A1** quantifier read-forward | `python3 scripts/wt130_quantifier_sweep.py paper-IV` | **203 quantifier tokens on 160 lines that carry one, of 766** | IV-4 |
| **A2** the document's own named failure modes, turned back on it | four modes derived from Paper IV's prose (§6 *an absence found by searching is a property of the search*; §8 *an abandonment that could not have cost anything is an advertisement*; §3 *applicability is not evidence*; §7 *recording which constraint, and when it lapsed, is more checkable*), plus `docs/REFERENCE-POLICY.md` §1's absence rule | **4 modes, 3 turned up a site** | IV-6, IV-8, IV-9 |
| **A3** cross-references as a quantifier | `python3 scripts/wt133_crossref_sweep.py`, then read around every flag | **68 §N.M refs, 17 distinct, 0 unresolved, 4 dismissed · 28 entries, 25 cited, 3 NOT** | IV-7 |
| **A4** run the manuscript's own regeneration commands, and ask BOTH questions | all six commands §10 names, on darwin, plus `wt089` | **6 commands run · 1 produces none of what it is named for · 2 numbers §10 promises are asserted by nothing** | IV-1, IV-2, IV-3 |
| **A5** every named artefact, backticked and not, against its paired script | **32 named artefacts enumerated** (28 backticked, 4 not: `ADR-001`, `5efe626`, `ASC 350-20-35-31/35-32`, `SDG 7.3.1`) | **32 enumerated · 11 files existence-checked · 0 missing · 1 artefact this paper's own results depend on is named nowhere** | IV-3, IV-5 |

**The A1 sweep is the axis that paid least and it is the one that has always paid least on this
manuscript** — one finding of nine, against `-73`'s seven-of-seven on Paper III. Recorded because
a table of axes that only lists the productive ones is an advertisement.

**A4's SECOND question is where this pass lives.** *Is there a number the paper reports that no
named command produces?* — three of the nine. `-80` reported the same asymmetry on Paper III and
it now holds on two manuscripts: the first question (do the values match?) cleared everything it
touched; the second question found the section.

---

## 2 · THE FINDINGS

Shape column: **[promise]** = a sentence ABOUT an artefact that the artefact does not bear out ·
**[deferral]** = a pointer whose target carries nothing · **[—]** = neither.
Class: **[P]** presentation · **[D]** disclosure · **[—]** plain error.

### IV-1 · §10 names a command for a result the command does not produce. **[P]** **[promise]**

§10: *"The diagonality rejection cited in §3, §4.4 and §9 comes from neither: it is Paper III
§5.4's, and its command is `python3 scripts/wt026_severe_test.py --universe pilot --onset peak`,
with `--universe replication` for the second arm."*

**Both arms were run.** Neither prints 4.12×, 2.02×, *p* = 0.0002, any off-diagonal ratio, any
co-occurrence lift, or the word *independence*. `wt026_severe_test.py` is Paper III **§5.3's**
instrument — the PRE-002 peak-to-charge tier ordering, whose verdict in both universes is
PREDICTION FAILS. Its `argparse` offers `--universe`, `--onset`, `--signal`, `--alpha`, `--out`;
no flag can reach the off-diagonal.

The instrument that DOES produce every one of those numbers is
**`scripts/wt089_recognition_and_offdiagonal.py`**, run for this review:
`null mean 7.3 · central 95% [3, 12] · two-sided p = 0.0002 · ABOVE · observed / expected = 4.12×`,
then `21.8 · [15, 29] · p = 0.0002 · 2.02×`, then `π = 0.05 → power 1.00` — which is also §3's
*"detects an injected excess of five per cent of events with probability 1.00"*, verified here for
the first time.

**Paper II §7 states the rule this breaks, in the corpus's own words:** *"a single command named
for numbers it does not produce is a provenance claim that reads as checked and is not."*

**REPAIRED.** §10 now names `wt089`, says what it prints, and says in the same breath that
`wt026` is §5.3's command and prints none of it. `docs/crossref-dismissed.tsv` gains the
`paper-IV 5.3` row the new sentence requires.

**FALSIFIER:** `python3 scripts/wt026_severe_test.py --universe pilot --onset peak | grep -c 4.12`
returns 0. If it ever returns non-zero, this finding is wrong.

**AND THE ROOT WAS REPAIRED TOO, IN PAPER III.** `-75` did not invent the error; it reached for
the nearest command Paper III named. Paper III §11's *"Regenerate §5"* bullet names `wt026` — and
Paper III has never, in any draft, named a command for §5.4 at all. `scripts/wt145` adds the
bullet. **Not counted as a Paper IV finding** (cf. `-79`'s II-39, an apparatus fix deliberately
uncounted), but it is the reason the next inheritance cannot happen.

### IV-2 · §10's own preamble contradicts §10's own bullets, and §1 gets it right. **[—]** **[promise]**

§10 opened: *"This paper's own contribution is one measurement... **Everything else it reports is
cited from Paper II or Paper III and is regenerated by those papers' scripts.**"* Three bullets
below, §10 itself says §5's and §8's numbers come from *"the surviving apparatus of the fourth
paper §8 describes"* — neither cited from II or III nor regenerated by their scripts.

§1 states it correctly and states it first: *"Numbers appearing below without a citation to II or
III come from **two places** and §10 names the command for each."* §10's preamble compressed §1's
two places into one and lost the half that is this paper's own.

**REPAIRED.** The preamble now says two places, in §1's words.

**FALSIFIER:** read §1's *"What this paper does not contain"* and §10's preamble against each
other. If they say the same thing, this finding is wrong.

### IV-3 · The one `src/` module this paper's own results depend on is named nowhere. **[P]** **[promise]**

§10 names `src/wealth_tensor/redistribution.py` (Paper II) and `lag.py` and
`lambda_sensitivity.py` (Paper III). §5 and §8's numbers come from
**`src/wealth_tensor/excess_demand.py`**, which appears in Paper I's §10 and in no other
manuscript. Paper IV names the test module and the script and never the module under both.

**Apparatus row P5h is the tell.** It requires the section to name *module paths*, and its check
is `grep -q 'src/wealth_tensor/'` — satisfied, green, by a **sibling's** module. The row could not
see the gap, which is what a filled cell looks like from the inside.

Two further promises in the same bullet are unheld: *"§5's schedule counts on the **399** interior
grid points"* — `399` appears nowhere in `tests/`, `src/` or any script but the patch script that
wrote the sentence, and the module asserted `grid.size > 300` — and *"the twelve-point tie
convention §8 records"*, §8's **four** distinct excess-demand schedules, which **no test in the
suite measured**. `test_but_the_curves_themselves_are_not_invariant` builds the same 12-point grid
and counts DEMAND schedules (25), a different number about a different object.

**REPAIRED, and the promises made TRUE rather than withdrawn** (the `-76`/`-79` precedent, II-27
and II-37). §10 names the module and says the two numbers are *asserted* rather than printed.
`tests/test_excess_demand.py`'s bound is now `assert grid.size == 399`. New module
`tests/test_paper_iv_tie_convention_is_counted.py` asserts the four, asserts that excluding the
two endpoints collapses it to one — the witness for §8's *explanation* of the four, not just its
value — and asserts the neighbouring 25 so the lazy repair of repointing the old test is red.

**FALSIFIER:** `grep -rn 399 tests/ src/ scripts/ | grep -v wt134 | grep -v wt144` returned one
irrelevant hit (`wt066_p3_port.py`'s `k=399` default) before this pass. Re-run it.

### IV-4 · "Two tests in the suite" is an exhaustive count over a set the repository can enumerate, and it is wrong. **[P]** **[promise]**

§10: *"**Two tests in the suite** exist specifically to make overclaiming fail loudly"*, naming
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` and
`test_a_flat_gini_does_not_mean_a_bounded_one`.

The suite holds more. `test_the_forbidden_claim_is_red` — *"the registration's own forbidden
claim, and the value-door version of it"* — is in `test_reg004_sec6_alpha_eff.py` **and**
`test_reg005_sec7_lag_transfer.py`. Paper III names a third for the same office,
`test_pre001_constants_are_what_was_registered`. Beyond those:
`test_the_manuscript_never_calls_the_asserted_product_disclosed`,
`test_doc_does_not_claim_count_three_was_measured`,
`test_limb_a_the_substitution_is_never_called_e4`, `test_reg012_sec7_refusal_is_asserted`, and a
**registered class of 29 tripwires**.

**And the second named guard constrains nothing in this manuscript.** Paper IV reports no Gini, no
saturating statistic and no convergence claim — `grep -in 'gini\|condensat\|saturat'` returns one
hit in a reference title. It is Paper II's guard, inherited into Paper IV's §10 as though it held
a claim here.

**This is III-17's shape on a different manuscript**, and the sibling papers show the corpus knows
better: Paper III's version is careful (*"both of which exist solely to make overclaiming fail
loudly"* — a claim about those two, not a census), Paper II §1's is careful, and
`test_paper_ii_does_not_claim_both_named_guards_are_in_the_counted_module` exists **because Paper
II made the neighbouring mistake and was caught at `-58`.** No equivalent covered Paper IV.

**REPAIRED**, and held by derivation. §10 now names two, says the suite holds more, and cites the
two it can point at. New module `tests/test_paper_iv_named_guards.py` forbids the exhaustive form
and its two near-miss phrasings, asserts apparatus row P5j's requirement that both names survive,
asserts that every guard the paper names exists, asserts that the repaired sentence's own evidence
(`test_the_forbidden_claim_is_red` in ≥ 2 modules, and `test_pre001_...`) is still real — so the
repair cannot rot into its own phantom — and carries a non-vacuity test.

**FALSIFIER:** `grep -rn 'def test_the_forbidden_claim_is_red' tests/` returns two modules. If it
ever returns one, the repaired sentence needs re-cutting, and the new guard goes red saying so.

### IV-5 · §8 says the dead paper "is not in this corpus"; it is in the repository, and it is the only place §8's own word count is checkable. **[D]** **[promise]**

§8: *"A complete draft existed — roughly **7,400 words**, references verified — arguing that supply
and demand are not independent equations. **It is not in this corpus.**"*

`docs/papers/paper-I-price-formation/paper-I.md` is 730 lines and **7,367 words**, titled *Supply
and demand are not independent equations*, carrying its own `⚠ SUPERSEDED` banner, and it is one
of the **four** manuscripts `wt133_crossref_sweep.py` sweeps on every run. §10 invites the reader
into `docs/` two paragraphs later — *"deliberately public and is the project's working notebook"*.

The word count is the proof, not a coincidence: *roughly 7,400* is a claim a referee can only
check against the file §8 says is not there.

**REPAIRED.** §8 now says what is true — not published, not one of the papers this corpus joins,
draft in the repository at its path, superseded and marked so — and points at the file the count
is checkable against.

**FALSIFIER:** `wc -w docs/papers/paper-I-price-formation/paper-I.md`.

> **CORRECTION, wealthTensor-100 (2026-08-21).** The word count stated above is wrong. `docs/papers/paper-I-price-formation/paper-I.md` is **7 527** words, not 7,367, and has been since `623a117` on 2026-08-10 — before Paper IV existed and at `c3b1b31`, the commit this pass read. This finding's own falsifier is `wc -w`, and `wc -w` has never returned 7,367. `docs/promises-adjudicated.tsv` row `cbd18be550` carries the right number, so the TSV and this document disagreed for nineteen sessions and no pass compared them. The FINDING stands — the count is checkable only against the file §8 said was not there, which is exactly what IV-5 claims — but the number supporting it did not. The original text above is left unrewritten; wealthTensor-100 moved the manuscript's *roughly 7,400* to *roughly 7,500* as part of IV-12 and recorded the apparatus half in `REVIEW-035` §4 item 1, NOT COUNTED as a manuscript finding under the `-79`/II-39 precedent.

### IV-6 · §7's fourth relocation names no work, no author and no constraint, in the section whose method is naming the constraint. **[D]** **[deferral]**

§7's move paragraph relocated four predecessors: *Piketty*, *Solow's scalar*, **"The Austrian
account of the cycle names a different cause and describes the same architecture"**, and *SMD*.
Three carry reference entries. The Austrian clause names no author, cites no work, appears
**exactly once** in 766 lines, has no entry in the References, and is never developed anywhere in
the corpus.

**And §7 states the standard it fails, two paragraphs later:** *"Recording which constraint, and
when it lapsed, is a stronger and more checkable statement than 'the received view is mistaken,'
and it is falsifiable in a way that the received-view complaint is not."* The Austrian relocation
records neither constraint nor lapse. It is the unfalsifiable form, inside the paragraph arguing
against it.

**`wt133` cannot see this class.** Sweep 2 runs entry → body and flags entries nobody cites. This
is the mirror: a body claim with no entry. Noted in §4 as a gap in the instrument.

**REPAIRED by removal.** The counts survive: §7's *"performing it silently four times"* and §1
contribution 5's *"deployed four times by accident"* both count §7's four **blocks** (biophysical,
stock-flow, kinetic exchange, aggregation), not the illustration list, and the blocks are
untouched. **A future session may restore the clause WITH a verified citation** —
`docs/REFERENCE-POLICY.md` forbids asserting a bibliographic record this session cannot verify,
which is why the repair is a cut and not an invented entry.

**FALSIFIER:** `grep -c Austrian docs/papers/paper-IV-composition/paper-IV.md` was 1 and no
References entry existed. Check `git show c3b1b31`.

### IV-7 · Three reference entries are cited nowhere, and two of them are the works §1.1's argument actually rests on. **[D]** **[—]**

`wt133` sweep 2 has flagged this on **every run since `-74`** and no pass has adjudicated it:
*not cited: Mas-Colell, Robinson, Sraffa.*

- **Robinson (1953)** opened the Cambridge controversy and **Sraffa (1960)** is where reswitching
  comes from. §1.1 leans on both — *"the Cambridge controversy was fought over precisely that —
  Samuelson (1966) conceded that with **reswitching** available..."* — and credits neither. The
  manuscript uses two works it lists and does not cite.
- **Mas-Colell, Whinston and Green (1995)** carried no load anywhere in the manuscript. Paper I
  cites it twice, with sections; Paper IV inherited the entry and never used it.

**REPAIRED.** §1.1 now reads *"the Cambridge controversy — opened by Robinson (1953), and given
the reswitching apparatus by Sraffa (1960) — was fought over precisely that"*, and §7's
aggregation paragraph names MWG as SMD's textbook statement. All three are **CITE** acts in
`REFERENCE-POLICY` §1's sense — pointing at a work whose bibliographic record the manuscript
already carries — and none is a CHARACTERIZE, so no new evidentiary burden is taken on.

**FALSIFIER:** `python3 scripts/wt133_crossref_sweep.py` — paper-IV sweep 2 read *25 cited, 3 not*
before this pass and **28 of 28** after.

### IV-8 · §8 states a test and applies it to every entry but one. **[D]** **[deferral]**

§8's opening: *"The test applied to **every** entry is: had this route worked, which sentence in
this paper would be different? An abandonment that could not have cost anything is an
advertisement, not a disclosure."* The section is self-conscious about it — the superposition
entry ends *"which is what earns it a place under this section's test despite its never having
reached a draft."*

**The REG-001 entry answers it with nothing.** *"...the run produced no usable answer in either
direction. It is recorded here as an instrument dead end — which is what it is — and not as a
result, because it never became one."* No counterfactual sentence, in the one section that
declares a counterfactual sentence is the price of admission.

**REPAIRED.** The entry now answers: had it returned, §5's identity would be reported as holding
beyond the single-good case and §9's fifth limitation would be a narrower claim than it now is.

**FALSIFIER:** read §8's eight entries against §8's own first paragraph. If a second entry lacks a
counterfactual, this finding was incomplete rather than wrong — say so and repair it.

### IV-9 · The paper measures the absence that motivates it and asserts the absences that carry its consequence, and §9 does not say so. **[D]** **[—]**

§6 exists for one reason, stated: *"an absence found by searching is a property of the search"* —
so the whitespace was measured, pre-registered, floored and ceilinged. The paper is right to be
proud of it.

Three other absences are asserted:

1. §1.1, **in bold**: *"The input-output energy table has no lapse to report."* It is
   load-bearing — it is *"one reason §4.3 finds the composed state largely unmeasured rather than
   merely unassembled"*, which is the paper's own thesis sentence.
2. §7: biophysical economics *"has generally not had"* an accounting-shaped object.
3. §7: kinetic exchange *"has mostly not had"* a base.

**And this project has a written rule about exactly this.** `docs/REFERENCE-POLICY.md` §1: *"an
abstract can never establish that something is not in a paper... Every zero-hit table this project
has published came from `grep` over an extracted full text, and that is the only thing that
licenses one."*

§9 carried eight limitations and none of them was this one. **None of the three claims is known to
be false**, and the finding is not that they are wrong — it is that the paper applies a standard
to one absence, does not apply it to three others, and does not tell the reader which is which.

**REPAIRED.** §9 gains a ninth limitation naming all three and the asymmetry.

**FALSIFIER:** count §9's items and read item 9. If a reader can find the disclosure elsewhere in
the manuscript at `c3b1b31`, this finding is wrong.

---

## 3 · CLEARED — checked and standing

Sixteen things this pass checked and did not find wrong. This list is the honest half of the
coverage claim: an axis that only reports hits is unmeasurable.

1. **§6's entire numeric content, against a live run of `reg013_citation_whitespace.py`.**
   Overlaps 0.0202 / 0.0108 / 0.0053; intersections 23 / 15 / 6; smaller audiences 1 139 / 1 383 /
   1 139; *z* 0.042 / 0.023 / 0.011; per-literature ceilings 0.168 / 0.520 / 0.744; split-half
   intersections 134 / 155 / 380; `P_ceiling` 0.477; `F_floor` 0.0. **Every one matches.**
2. **§6's arithmetic is internally closed.** 23/1 139 = 0.0202; 0.0202/0.477 = 0.042; the stricter
   ceiling z = 0.0202/0.168 = 0.120, exactly as §6 states. The table cannot be quietly wrong in
   one cell.
3. **§6 against `REG-013`.** WHITESPACE iff *z* ≤ 0.10 ✓, UNDECIDED for 0.10 < *z* < 0.25 ✓
   (§6's 0.120 is correctly called undecided), VOID iff P < 0.20 ✓, `"void": false` ✓.
4. **"Twenty-five of twenty-five seeds resolved."** The output's `even_seeds`/`odd_seeds` give
   7 + 6 + 6 = 19 economics seeds, and the CRISPR block lists 6. 19 + 6 = 25 ✓.
5. **The abstract against §6.** 0.020 / 0.011 / 0.005 round correctly from 0.0202 / 0.0108 /
   0.0053; 0.477; *exactly zero*; *six works in the world* ✓.
6. **§5 and §8's numbers, all of them, against `wt071_refuter.py` and a direct re-run of the
   module.** 26.1× / 8.3× / 113.5× / 47.2×, a 13.6-fold non-monotone swing ✓. The control at
   **0.8934 vs 0.9576**, which §8 reports as *0.89 against 0.96* ✓. The 12-point grid returns
   **4** ✓ (true — and, before this pass, asserted nowhere). The 500-point sweep runs **+249 to
   −150 with one sign change** ✓, which is *N* − *S* = 400 − 150 and −*S* exactly. 399 interior
   grid points, post-filter ✓. 25 / 25 / 1 ✓.
7. **§3's citations of Paper III's calibration.** Paper III §2 line 167: *"E₀ = 100, d = 0.05,
   m = 0.6 (effective decay 0.02 per period), α = 0.05"* ✓. §5.4's measured **α̂ = 0.408 per year**
   ✓, and Paper III's own words for it are *"an order of magnitude above the calibration"*, which
   is what §3 says ✓.
8. **All three `Paper III §5.4` pointers resolve** to Paper III's *"The same sample answers two
   questions it was not collected for"*, which carries both the recognition rate and the
   off-diagonal ✓. `crossref-dismissed.tsv`'s `paper-IV 5.4` row is true.
9. **§3's tag-list repair figures.** *"the headline survives that section's tag-list repair at
   4.01× and 2.10×"* matches Paper III's ledger row exactly ✓.
10. **§3's pre-registered demotion claim.** `END-TO-END-001.md` §2's E1 block carries, verbatim
    and before the run: *"Paper IV §3's 'a chain rather than three analogies' is demoted in terms
    to 'three instances of one question, asked at three scales'... The demotion is written before
    the run so that it cannot be negotiated after it."* ✓ The strongest thing in the manuscript.
11. **§8's REG-001 characterisation.** `RESULT-REG-001.md`'s title is *"NO VERDICT. The instrument
    was mis-specified in four ways."* ✓ Word for word.
12. **The commit pins.** `5efe626` is the ONLY commit ever to touch
    `scripts/reg013_citation_whitespace.py` and is the commit that added `paper-IV.md` — so §10's
    *"the pin is exact rather than approximate"* is literally true ✓. `fff7063` added `REG-013` ✓.
    Nothing has touched `src/wealth_tensor/excess_demand.py` (623a117) or `wt071_refuter.py`
    (fcb27a0) since. **No SHA in this manuscript is stale.**
13. **The reference key.** Paper IV uses **one** mark, `✓`, on six entries, and the key defines
    exactly that one. **III-10's shape is not here** — the first thing this pass looked for, and
    it is absent.
14. **`ADR-001`, `REG-003`, `REG-013`, `PREPRINT-CHECKLIST.md`, `REFERENCE-POLICY.md`,
    `RESULT-END-TO-END-001-E1.md`** — every named artefact exists and says what it is said to say.
    Eleven files existence-checked, zero missing.
15. **§1.1's "two of those three constraints"** — filings 2011, SDG 7.3.1, and the input-output
    table with no lapse. Two ✓. (The third is IV-9's subject for a different reason.)
16. **The coach.** `handoff_gate.py --coach` reads **1 conduct / 0 concessive** for Paper IV,
    before and after ten edits. The baseline held.

**THE ONE NEAR-MISS, NAMED.** §6 says the two true-audience sizes *"are the two numbers in this
section that §10's command does not regenerate."* **9.3 per cent** is 4 000/43 048 and is
therefore also not regenerable — 43 048 is one of the two. I nearly filed it as a third
un-regenerated number and it is **not one**: it is the second number divided by the first, both
already disclosed in the same sentence, and a reader who has the disclosure has the percentage's
provenance. Filing it would have been padding a count with an arithmetic restatement of a
disclosure the paper already makes. It is recorded here so the next pass does not re-derive it.

---

## 4 · NOT CHECKED — named so the next pass starts above zero

1. **Bibliographic verification of any reference entry.** Six of 28 carry `✓`; 22 do not, and
   `PREPRINT-CHECKLIST.md` defers the rest to pre-submission. Nothing in this pass touched it, and
   IV-7's three new citations are CITE acts against records already in the manuscript.
2. **`wt133`'s blind spot, now named.** Sweep 2 runs entry → body. It cannot see a body claim with
   no entry, which is exactly IV-6. A sweep 3 — proper nouns in the body with no reference entry,
   against a stop-list — is the obvious instrument and this pass did not build it.
3. **Whether `test_a_flat_gini_does_not_mean_a_bounded_one` should be named in Paper IV at all.**
   IV-4's repair keeps it because apparatus row **P5j requires both names**, and explains why it is
   there. Whether P5j should require a guard for a claim the paper does not make is a question
   about the row, not the paper, and it is Jason's or a later pass's.
4. **Paper III's §11 beyond the one bullet `wt145` added.** `-80` read it whole; this pass entered
   it only to find IV-1's root and did not re-read it.
5. **§4 and §5's mathematics.** Read for internal consistency and against the suite; not
   re-derived. The SMD characterisation in §4.1 is the objection stated in a referee's voice and
   was not checked against Sonnenschein, Mantel or Debreu directly.
6. **The abstract's length against `check_abstract_size.py`** (apparatus row P5a). The suite is
   green so the row is green; not separately re-run for this review.
7. **§8's "three supporting results were built and all three arithmetics were correct."** The
   three are not enumerated in Paper IV; they are inferable from §8's three numbered reasons. A
   pass that wanted to be strict about A1 would ask for the enumeration.
8. **The version stamp.** `paper-IV.md` still reads *Version 0.1, 2026-08-16* with ten repairs
   landed 2026-08-18. Deliberately not moved — a version stamp is the author's, and this is the
   **third** manuscript now in that state (Paper II is card 1217568297674954, Paper III is `-80`'s
   note (d)). It has stopped being a per-paper observation and is now a corpus-level decision
   waiting on Jason.

---

## 5 · THE METHOD RESULT

**COVERAGE IS DEAD, AND IT DIED THE WAY THE OTHER THREE DID.**

`-80` proposed coverage of the axis matrix, from a pass that filled three cells and returned nine
with 8 of 9 from the new cells. The prediction was explicit and this at-bat was built to test it:
*a pass with nowhere left to be structurally blind should return materially fewer than nine.*
This pass had a closed grid, filled no cell, and returned **nine**, **9 of 9 from filled cells.**

That is the fourth mechanism refuted by the pass immediately after the pass that proposed it:

| mechanism | proposed by | refuted by | how |
|---|---|---|---|
| new instruments | the handoffs, six times | `-71`, `-77` | frozen set, four findings then three |
| repair residue | `-77` | `-78` | 0 of 2 blame to `-77` |
| depth of application | `-78` | `-79` | 2 of 2 from sites `-78` had opened |
| **coverage of the matrix** | **`-80`** | **`-81`** | **closed grid, no cell filled, nine findings** |

**FOUR FOR FOUR IS THE RESULT, NOT ANY OF THE FOUR MECHANISMS.** Every mechanism this project has
proposed was proposed by the pass whose own number it explained, and every one has died on the
next pass. A regularity that holds four times is worth more than any of the four hypotheses, and
it says something uncomfortable: **the passes are not measuring the manuscripts, they are
theorising their own output.** That is `-78`'s reading — the counter measures the REVIEWERS — and
it is what is left standing.

**AND I MUST SAY THE WEAKNESS OF THE READING I AM LEFT DEFENDING.** `-78`'s reading survives
partly because it predicts nothing. It cannot be killed the way the other four were killed,
because it does not say what the next pass will find. A hypothesis nothing can refute is not a
better hypothesis than four that could be and were; it is the residue. Recording that honestly is
worth more than a fifth mechanism from the pass that just produced a nine.

**WHAT THIS PASS CAN OFFER INSTEAD OF A FIFTH MECHANISM — a measurement, not a theory.**

`-75` read this manuscript end to end, found six, and banked a **global** lesson written FROM this
very section: *"A DATA-AVAILABILITY SECTION IS A LIST OF PROMISES, SO CHECK EVERY PAIRING BY GREP
AND EVERY COMMAND BY RUNNING IT. Two failures found in one section of Paper IV in ten minutes."*

**Four of this pass's nine are in that section**, and **two of the nine blame to `-75`'s own
repair commit** — IV-1's wrong command and IV-3's unheld promises were both **added by `-75`**,
in the edit that repaired the defect the leaf describes. At `5efe626` §10 had no diagonality
clause and no *"Regenerate §5 and §8"* bullet at all; `-75` wrote both, and checked neither by
running them.

So: **naming a defect class does not exhaust it, even in the site where it was named, even by the
pass that named it.** That is not depth-of-application (`-79` killed that: it was about a pass
re-entering sites its PREDECESSOR opened). It is narrower and more damning — the coining pass left
five more instances of its own class in the paragraph it coined the class from.

**RESIDUE, this pass: 2 of 9.** Non-zero for the first time since `-77`, and both in the section
the previous pass rewrote. The other **7 of 9 blame to `5efe626`** — present since 2026-08-16,
through `-69`'s scoped read, `-70`'s scoped read and `-75`'s full read. Residue still does not
explain the counter. It never has. But it is not zero, and where it is non-zero it is exactly
where the last pass put its hands.

**THE SHAPES REPLICATE EXACTLY, AND THAT IS THE PASS'S CLEANEST POSITIVE RESULT.**
`-79` named two shapes on Paper II. `-80` found **5 promise-about-artefact, 2 deferral, 2
neither** on Paper III and asked for a third manuscript. This pass found **5 / 2 / 2** on Paper
IV — the same split, on a third manuscript, on a closed grid, by a different reviewer. Two data
points made a conjecture; three make it a property of the corpus: **this corpus's characteristic
defect is not a wrong number. It is a true sentence about an artefact that the artefact does not
bear out.** Every single one of this pass's five `[promise]` findings is a sentence whose subject
is a file, a command or a test.

That is also the actionable half. A number can be checked by re-deriving it, and this corpus is
very good at that — **§3 is right, every figure in this pass's cleared list is right, and the one
place values were checked against a live run they all matched.** What the corpus does not check is
its own sentences about its own machinery. `wt133` checks one class of those. `wt144`'s two new
modules check three more. There are many left.

**SCORING, on both rules.** Current rule: **9**. `-79`'s proposed narrower rule (count only
findings requiring a manuscript edit): **9** — all nine required one. The two rules have now
agreed on `-81` and separated `-79` (0 vs 2) and `-80` (7 vs 9) by the same margin. Third data
point, still not applied; the row is on the current rule.

---

## 6 · THE TELLS

`-61`–`-80` as recorded in their own reviews. Five new.

**`-81`(i): RUN THE COMMAND. THE PAPER IS NOT LYING TO YOU, IT IS QUOTING SOMETHING IT NEVER RAN.**
A4's first question — *do the values match?* — cleared every number it touched, on two manuscripts
now. A4's SECOND question — *is there a number the paper reports that no named command produces?*
— found three of nine here and three of nine on Paper III. The expensive half of A4 is not
checking arithmetic. It is checking the ATTRIBUTION, and the only way is to run the thing and grep
its output for the number.

**`-81`(ii): THE PASS THAT NAMES A DEFECT CLASS IS THE PASS MOST LIKELY TO LEAVE MORE OF IT IN THE
SAME PARAGRAPH.** `-75` coined *a data-availability section is a list of promises* from Paper IV
§10 and left four more promises in Paper IV §10, two of them written by the coining edit. Reading
a predecessor's lesson tells you where to look **hardest**, not where it is safe not to look.

**`-81`(iii): A COUNT OVER A SET THE REPOSITORY CAN ENUMERATE IS A DEFECT WAITING FOR A GREP.**
*"Two tests in the suite"*, `-80`'s *"three of its additions"* which was six, Paper II's *"18
tests"*, Paper III's *"100"* and *"62"*. The corpus has already built the general repair
(`test_paper_test_counts_are_derived.py`) and applied it to two of four manuscripts. When a
sentence says a number and the repository can compute it, the sentence is a bug report.

**`-81`(iv): A GUARD SATISFIED BY A SIBLING'S ARTEFACT IS GREEN AND BLIND.** Apparatus row P5h
demands Paper IV's data section name *module paths* and checks `grep -q 'src/wealth_tensor/'`.
Papers II's and III's modules satisfied it while the module this paper's own §5 and §8 depend on
was named nowhere. When a row's predicate is a substring and the manuscript cites siblings, the
row can be green forever without ever having read the thing it exists to read.

**`-81`(v): WHEN THE PAPER TELLS YOU IT MEASURED ITS ABSENCE, GO FIND THE ABSENCES IT DID NOT.**
§6 is the most careful section in the manuscript and it advertises its own standard. That
advertisement is a map: the three sentences that assert an absence without measuring one were
found by taking §6 at its word and asking where else the paper says *there is no*. A section proud
of its rigour marks the boundary of the rigour.
