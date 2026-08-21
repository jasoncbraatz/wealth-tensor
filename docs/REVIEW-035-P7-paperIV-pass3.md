---
new_instrument: inherited-first-application
instrument_name: "A3′ — THE CORRECTNESS QUESTION BEHIND A3, non-script. A3 has always asked whether a `§N.M` reference RESOLVES. wealthTensor-99 opened the question of whether it is CORRECT (Paper II's II-40: §7 pointed a number at §3.2 when the number lives in §3.3, and wt133 was green because §3.2 exists), applied it to ONE number on ONE manuscript, and wrote that generalising it was a real at-bat NOT claimed there. This pass applied it to Paper IV — to all 97 of its `§N.M` references and to every phrase the manuscript QUOTES from a named section, its own and Paper III's. First application to this manuscript. No axis was invented and no A1–A5 cell was filled: the grid has been closed at 15 of 15 since -80 and A6, the docstring axis, remains parked. `scripts/wt182_paperIV_p7pass3.py` and `scripts/wt183_paperIV_promises.py` are the PATCHES of record — the same object `wt141` was at -79 and `wt181` at -99 — not instruments."
new_instrument_alt: none
findings_from_new_axis: 1 of 4
findings_from_new_instrument: 1 of 4
residue_of_previous_pass: 2 of 4
shape_promise_about_artefact: 2 of 4
shape_deferral_with_empty_target: 2 of 4
shape_neither: 0 of 4
manuscript_edits: 4 of 4
consecutive_zero_passes_after_this_pass: 0
# FALSIFY THIS ROW, SIX WAYS.
#   1. `inherited-first-application`: open REVIEW-034 and docs/p7-passes.tsv's -99 block and find
#      the class described — "A RESOLVING CROSS-REFERENCE IS NOT A CORRECT ONE" — together with the
#      sentence that generalising it "is a real at-bat and is NOT claimed here". If that text is
#      absent, this pass invented the axis and the row should read `new`. If instead a PRIOR pass
#      applied the correctness question to paper-IV, the row should read `none`; grep REVIEW-009,
#      -010, -015 and -021 for it.
#   2. `1 of 4`: §2 credits each finding to the axis that produced it. IV-11 is the only one from
#      A3′. If any of IV-10, IV-12 or IV-13 traces to it, this row undercounts.
#   3. `2 of 4`: git blame the four sites at the parent commit 5b42b4a.
#      IV-11 → L643-644 → 14631bfa (wealthTensor-81).  IV-12 → §10 L656 → 14631bfa.
#      IV-10 → §10 L690-692 → 7ca35c78 (wealthTensor-75).  IV-13 → §8 L528 → 5efe6268 (-53).
#      If a third site blames to -81 or later, this row is wrong. NO MECHANISM IS PROPOSED FROM
#      THIS NUMBER — see §5, and see -78/-77 for why residue is not one.
#   4. `4 of 4` manuscript edits: scripts/wt182_paperIV_p7pass3.py touches paper-IV.md six times
#      for four findings (IV-12 has three sites: §1, §8's count, §10). If any finding is repaired
#      outside the manuscript, the count is wrong. -79's proposed narrower rule and the current
#      rule agree on this pass.
#   5. the shapes: 2 promise / 2 deferral / 0 neither, against the 5/2/2 that -80 found on Paper
#      III and -81 replicated on Paper IV. n = 4 is small and this row does not claim the split
#      moved; it claims what it counted. Re-read §2 against REVIEW-019 §6's two definitions.
#   6. the counts themselves: scripts/wt182_paperIV_p7pass3.py carries 20 post-conditions, 6
#      NEGATIVE; scripts/wt183_paperIV_promises.py carries 15, 4 NEGATIVE. Both are idempotent.
#      `python3 scripts/wt018_report.py` prints IV-10's four numbers in nine seconds.
# Ledger of all thirteen passes: docs/p7-passes.tsv
---

# REVIEW-035 · Paper IV's THIRD independent `P7` read — the pass that asked what a pointer POINTS AT

*`wealthTensor-100` · 2026-08-21 · Paper IV's first read in NINETEEN sessions. Parent commit
`5b42b4a`. **Four findings, four repairs, all landed in-pass**, plus one apparatus correction that
is deliberately NOT counted and one CLEARED item that took the longest to clear of anything here.*

**THE HEADLINE IS `IV-10`, AND IT IS ABOUT A TABLE THAT EXISTS.** §5 reports the anti-SMD sweep as
*"zero monotonicity violations across 500 grid points, running from **+249** to **−150** with one
sign change."* No command §10 named produced those numbers. No test asserted them. And
`scripts/wt018_report.py` **prints all four of them, as a table, from a configuration its own
header says is "identical to `tests/test_excess_demand.py` so the paper, the tests and this script
all describe one experiment rather than three similar ones"** — a script Paper IV named nowhere, in
812 lines, through three independent reads and two scoped ones. The script knew it was the paper's
source. The paper did not know the script existed.

---

## 0 · What is NOT claimed here, and the naming ruling this at-bat owed

**Four findings on a nineteen-session-old manuscript is not evidence that anything decayed.** The
comparison this pass cannot make is against `-81`'s nine, because the two passes did not read the
same object: `-81` read 766 lines, this one read 812, and sessions `-82` through `-99` edited Paper
IV five times without reading it. **No mechanism is proposed for the number four.** Four have been
proposed and refuted, always by the very next pass, and `-99` had a 2-of-3 residue row begging to
be a fifth and declined. This row is 2 of 4 and declines for the same reason: residue was proposed
at `-77` and refuted at `-78`, and the two residue findings here are the *smallest* two of the four
— the one that names a script the paper never named is `-75`'s, and the one that leaves §8's own
stated test unapplied has been in the tree since the manuscript was drafted.

**THE FILENAME CONVENTION, RULED (tee-up 2 from `-99`, and it is now closed).** Paper IV's review
documents carried two incompatible conventions. The ruling: **`passN` on a paper-IV review filename
counts INDEPENDENT `P7` reads**, because that is the unit the definition of done counts — two
consecutive zero-finding passes *per paper* — and scoped passes say in their own front matter that
they do not advance it. The mapping, so nobody re-derives it:

| document | session | what it was | independent read # |
|---|---|---|---|
| `REVIEW-009-P7-paperIV-narrowing-reread.md` | `-69` | SCOPED, §1–§3 only | — (its own §0 says so) |
| `REVIEW-010-P7-paperIV-sections4to10.md` | `-70` | SCOPED, §4–§10 only | — (its own §0 says so) |
| `REVIEW-015-P7-paperIV-**pass3**.md` | `-75` | independent, end to end | **1** |
| `REVIEW-021-P7-paperIV-**pass2**.md` | `-81` | independent, end to end | **2** |
| `REVIEW-035-P7-paperIV-**pass3**.md` | `-100` | independent, end to end | **3** |

`REVIEW-015`'s filename says `pass3` under the older all-reads count and this document says `pass3`
under the independent-read count. **The collision is cosmetic and deliberate: twelve documents cite
these files by REVIEW number, and `-99` was explicit that committed filenames are not to be
renamed.** The REVIEW number disambiguates; the suffix now has one meaning going forward.

---

## 1 · THE AXES, RUN BEFORE A WORD OF PROSE

| axis | what was run | count | findings |
|---|---|---|---|
| **A1** quantifier read-forward | `python3 scripts/wt130_quantifier_sweep.py paper-IV` | **226 tokens on 178 lines that carry one, of 812** | IV-12 |
| **A2** the document's own named failure modes, turned back on it | the four modes `REVIEW-021` §1 derived, INHERITED rather than re-derived, plus `docs/REFERENCE-POLICY.md` §1's absence rule | **5 modes, 2 turned up a site** | IV-13, and IV-11's site |
| **A3** cross-references as a quantifier | `python3 scripts/wt133_crossref_sweep.py` | **97 §N.M refs, 20 distinct, 0 unresolved, 5 dismissed · 28 entries, 28 cited, 0 not** | none — and that is the point of A3′ |
| **A3′** *does the referent carry what the pointer says?* | all 97 `§N.M` references and every phrase the manuscript quotes from a named section — its own §§1.1/4.3/6/7 and Paper III's §2, §3.1, §4, §5.3, §5.4, §A.1.2, §A.2.2 | **11 cross-document claims and 6 quoted phrases checked; 1 wrong** | IV-11 |
| **A4** run the manuscript's own regeneration commands, and ask BOTH questions | all eight commands §10 names plus its one declared negative control (`wt026_severe_test.py`, named as printing *none* of those numbers), on darwin | **9 commands run, 9 RC 0 · 3 numbers §5 reports that no named command produces** | IV-10, IV-12 |
| **A5** every named artefact against its paired script | **43 named artefacts enumerated** — 39 backticked spans over 52 occurrences, plus 4 not backticked (`ADR-001`, `5efe626`, `ASC 350-20-35-31/35-32`, `SDG 7.3.1`) | **21 files existence-checked, 0 missing · 4 test names resolved to real `def`s · 1 script that produces this paper's numbers named nowhere** | IV-10 |

**A4's SECOND question is where this pass lives, for the third manuscript running.** *Is there a
number the paper reports that no named command produces?* — two of the four. `-80` found the
asymmetry on Paper III, `-81` on Paper IV, and it holds again: the first question (do the values
match?) cleared **everything it touched**, sixty-plus numbers, and the second question found the
section. **A1 paid least again** — one finding of four, on the manuscript where it has paid least
every time.

**And A3 went green while A3′ found something, which is the whole content of the new axis.** 97
references, 0 unresolved. `wt133` cannot fail on IV-11 because §4.3 exists.

---

## 2 · THE FINDINGS

Shape column: **[promise]** = a sentence ABOUT an artefact that the artefact does not bear out ·
**[deferral]** = a pointer whose target carries nothing. Class: **[P]** presentation, **[D]**
disclosure, **[—]** plain error.

### IV-10 · §5 reports three numbers no command §10 names produces, and the script that prints them is named nowhere. **[D]** **[promise]**

§5: *"Excess demand here is monotone and single-crossing — **zero monotonicity violations across 500
grid points, running from +249 to −150 with one sign change** — because each agent demands at most
one unit..."*

§10's inventory of what regenerates §5 was two commands and one exhaustive-sounding remainder:
`pytest tests/test_excess_demand.py -q` *"for §5's schedule counts on the 399 interior grid points,
its 500-point monotonicity sweep, and the twelve-point tie convention §8 records"*, `wt071_refuter.py`
for the crossing-height identity, and then *"§5's **399** interior grid points and §8's twelve-point
**four** are asserted by `tests/test_excess_demand.py` rather than printed by it."*

**Run the module and read its asserts.** `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`
builds the 500-point sweep and asserts exactly one thing: `assert all(a >= b for a, b in zip(zs, zs[1:]))`.
Monotonicity. **The endpoints and the sign change are asserted by nothing in the repository** — and
§10's list of what the command only *asserts* names 399 and four, and stops.

**Then grep the repository for the numbers.** `scripts/wt018_report.py` §E:

```
  grid points                                     500
  monotonicity violations                         0
  z at grid min / max                             249 / -150
  sign changes                                    1
```

and §B, above it, prints §5's whole table — `interior grid points, ties excluded 399`, `distinct
DEMAND schedules 25`, `distinct SUPPLY schedules 25`, `distinct EXCESS-DEMAND schedules 1`,
`excess demand == count(m_i > p) - S, identically True`. Its configuration block reads *"identical
to `tests/test_excess_demand.py` so the paper, the tests and this script all describe one experiment
rather than three similar ones."* **`grep -c wt018 paper-IV.md` was 0.**

This is `-81`'s IV-3 one level up. IV-3 found the one `src/` module the paper's results depend on
named nowhere; this is the one *script* that prints the paper's own table, named nowhere, in the
section whose office is naming it.

**REPAIRED, twice over.** §10's bullet now opens with `python3 scripts/wt018_report.py` and says
what it prints, endpoints included; and `tests/test_excess_demand.py` gains
`test_the_monotone_sweep_endpoints_and_single_crossing_are_what_section_5_reports`, which holds all
four numbers **with a negative control that is the honest half of this finding** (see §3, item 1).

**FALSIFIER:** `python3 scripts/wt018_report.py | sed -n '/E · EXCESS DEMAND IS MONOTONE/,/sign changes/p'`
and `git log -1 --format=%h -- scripts/wt018_report.py`. If the script ever stops printing those
four lines the new test goes red and §10's bullet needs re-cutting.

### IV-11 · §9's ninth limitation quotes a phrase and attributes it to the section that does not contain it. **[—]** **[deferral]**

§9 item 9 — **the limitation `wealthTensor-81` added, as IV-9's repair**:

> *"...§1.1's* the input-output energy table has no lapse to report*, which is load-bearing for
> **§4.3's** *largely unmeasured rather than merely unassembled*..."*

**§4.3 does not contain that phrase.** §4.3 says the extensive state *"does survive the sum, and it
is very largely not being measured."* The italicised words are **§1.1's** — *"which is one reason
§4.3 finds the composed state largely unmeasured rather than merely unassembled"* — §1.1's
characterisation of what §4.3 finds, re-attributed one section later as a quotation from §4.3.

**This is the class `wealthTensor-99` opened and did not claim beyond one number.** `wt133` is green
on it, and green for the same reason it was green on Paper II's II-40: §4.3 **resolves**. A3 has
never asked whether a pointer is right. Applied here to quoted phrases rather than to numbers, the
question found this in the first six it checked.

**REPAIRED by attribution.** The clause now reads *"which is load-bearing for §1.1's reading of §4.3
as largely unmeasured rather than merely unassembled"*. The phrase keeps its content and acquires
its author. No word of §4.3 or §1.1 moved.

**FALSIFIER:** search §4.3 for the phrase, with markdown emphasis stripped — see §3 item 3 for why
that qualification is not pedantry. It is absent at `5b42b4a` and absent now; §1.1 carries it.

### IV-12 · "Two places" is an exhaustive count over the paper's own numbers, and §8's word count is a third. **[D]** **[promise]**

§10: *"Numbers reported without a citation to Paper II or Paper III come from **two** places, which
is what §1 says: §6's are `REG-013`'s, and §5's and §8's are the surviving apparatus of the fourth
paper §8 describes. **Everything else** is cited from Paper II or Paper III and is regenerated by
those papers' scripts."* §1 says it too, in its own words.

§8 reports *"a complete draft existed — **roughly 7,400 words**"*. That number is cited to neither
Paper II nor Paper III, and it is not produced by the fourth paper's *apparatus*: it is `wc -w` on
the fourth paper's *manuscript*. **And it is `-81`'s own repair that made it checkable** — IV-5 added
*"the draft itself is in the repository ... at `docs/papers/paper-I-price-formation/paper-I.md` —
which is the only place the word count above is checkable"*, and did not go back to the census two
sections away that the new pointer falsifies.

**This is IV-4's shape, in IV-4's own section, one pass later.** `-81` cut §10's census over the
suite's guard tests and left §10's census over the paper's number-sources standing.

**REPAIRED by CUT, not by re-counting.** A census that has now been wrong twice in one section is
the defect; §1 and §10 both drop the count and keep the record-for-each, and both name the third:
*"§8's word count for that paper is `wc -w` on the superseded draft §8 names."*

**And the number moved with it.** `wc -w docs/papers/paper-I-price-formation/paper-I.md` returns
**7 527**, and has since `623a117` on 2026-08-10 — before Paper IV existed. §8 now says *roughly
7,500*. See §4 item 1 for the apparatus half of this, which is NOT counted.

**FALSIFIER:** `wc -w docs/papers/paper-I-price-formation/paper-I.md`; and
`grep -c 'two places\|\*\*two\*\* places' docs/papers/paper-IV-composition/paper-IV.md` was 2 and is 0.

### IV-13 · §8 declares a test for every entry, and one entry still does not answer it. **[D]** **[deferral]**

§8's opening: *"The test applied to **every** entry is: had this route worked, **which sentence in
this paper would be different?** An abandonment that could not have cost anything is an
advertisement, not a disclosure."*

**"Its first framing: attacking the diagram"** ends: *"**The cost was the most rhetorically
satisfying claim the project had.**"* That is a cost to the *project*. It names no sentence in this
paper. Read mechanically against §8's own question, the eight entries answer it seven times.

**`-81` asked for exactly this re-read, in writing.** REVIEW-021's IV-8 falsifier: *"read §8's eight
entries against §8's own first paragraph. If a second entry lacks a counterfactual, this finding was
incomplete rather than wrong — say so and repair it."* **Saying so: the finding was incomplete.**
`-81` repaired the `REG-001` entry and the class survived two entries away, which is the
`-81` lesson — naming a defect class does not exhaust it in the site where it was named — turned on
`-81`.

**REPAIRED by STEELMAN.** The entry now closes: *"Had the route worked, §5 would indict the
Marshallian cross rather than explain what its two curves are for, and §4 would be defending a
critique of general equilibrium instead of using SMD once, as a boundary."* Both clauses are checks
a reader can run against §5 and §4 as they stand.

**FALSIFIER:** the same one, unchanged and still standing — read §8's entries against §8's first
paragraph. **Two candidates were considered and NOT repaired,** and they are named in §4 item 2 so
the next pass does not have to find them again.

---

## 3 · CLEARED — checked and standing

Twelve things this pass checked and did not find wrong. **A pass that reports only its hits is
unmeasurable**, and two of these cost more than two of the findings did.

1. **§5's +249 and −150 are correct, and the reason they might not have been is now a test.** The
   500-point grid is CLOSED: both endpoints are `M.min()` and `M.max()`, which are data points —
   exactly the points `test_excess_demand_is_identically_invariant_to_the_allocation` **excludes**,
   because the strict inequalities disagree there about one agent whose holding status varies by
   allocation. That is §8's own tie convention, met in §5. So the endpoint reading is **not
   guaranteed** to equal §5's identity `#{i : mᵢ > p} − S`. **At the paper's configuration it does,
   at both ends.** At `S = 180`, same population, same grid, the lower endpoint reads 220 where the
   identity gives 219. **The agreement §5 relies on is a measured fact, not an algebraic one**, and
   the new test asserts it with the `S = 180` disagreement as its negative control. *Nothing in the
   manuscript changed for this. It was the closest call in the pass.*
2. **Every number in §6, against the committed run.** `RESULT-REG-013-run.json`: ceiling
   `0.47730` → **0.477**; floor `0.0` → **exactly zero**; the three pairs `23/1139 = 0.020193`,
   `15/1383 = 0.010846`, `6/1139 = 0.005268` → **0.0202, 0.0108, 0.0053**; `z` = overlap ÷ ceiling →
   **0.042, 0.023, 0.011**; split-half intersections **134, 155, 380** and overlaps **0.168, 0.520,
   0.744**; the stricter per-literature reading **0.0202 ÷ 0.168 = 0.1201** → **0.120** against a
   0.10 bar. Twelve numbers, twelve exact.
3. **`Paper III §A.2.2` really does say *"emphatically not"*, and the check that said otherwise was
   the check's fault.** The first locator run against Paper III reported the quotation MISSING. It
   is present — as `emphatically **not**`, with markdown emphasis between the two words. **A
   verbatim-quotation check that does not strip markup reports a true quotation as false**, which is
   `-99`'s locator trap in a second costume: the pointer was fine and the instrument was wrong.
   Recorded here rather than quietly fixed.
4. **`Twenty-five of twenty-five seeds resolved` reconciles.** `RESULT-REG-013` §2: T 7, S 6, K 6 —
   nineteen for the three literatures — plus the floor's six CRISPR seeds. The manuscript names the
   six two paragraphs later, so the arithmetic is available to a reader without leaving §6.
5. **`Paper III §5.4` carries every number §3 and §9 attribute to it**: 4.12×, 2.02×, both
   *p* = 0.0002, α̂ = 0.408, and the tag-list repair's 4.01× and 2.10×. `wt089_recognition_and_offdiagonal.py`
   prints the first four and `π = 0.05 → power 1.00`, which is the power curve §3 quotes.
6. **`Paper III §5.3`'s command.** §10 calls `wt026_severe_test.py --universe pilot --onset peak`
   *"Paper III §5.3's command"*. §5.3's body does not name it; **Paper III's own §11 does** —
   *"`wt026_severe_test.py` is §5.3's instrument"*. The attribution is the sibling's own.
7. **"That document's §2"**, in §3's demotion sentence, is `END-TO-END-001.md` §2 and the demotion
   is there — leg E1b's outcome table, *"Paper IV §3's 'a chain rather than three analogies' is
   demoted in terms to 'three instances of one question, asked at three scales'"*, with *"the
   demotion is written before the run so that it cannot be negotiated after it."* §3 of that
   document cites it as `(§2)` too.
8. **`RESULT-REG-013` §2 carries both capped audience sizes**: `7 801` (51 %) and `43 048` (9.3 %),
   the two numbers §6 says its command does not regenerate.
9. **The two commit pins.** `5efe626` is still the last commit touching
   `scripts/reg013_citation_whitespace.py` — the ONLY commit touching it — and still the add-commit
   of `paper-IV.md`. `fff7063` is REG-013's registration commit, dated before it.
10. **Every named test exists.** `test_the_forbidden_claim_is_red` in exactly **two** registration
    modules, as §10 says; `test_pre001_constants_are_what_was_registered` in `tests/test_edgar.py`;
    `test_a_flat_gini_does_not_mean_a_bounded_one` and
    `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` both live. `-81`'s IV-4
    repair has not rotted.
11. **§8's `N`-dependence table and its control, re-run.** 26.1×, 8.3×, 113.5×, 47.2×, *"13.6-fold
    swing, non-monotone in N"*, and `raise a RANDOM 250 by 20% spread 0.8934` against `raise
    NON-HOLDERS 20% spread 0.9576` — §8's *"0.89 against 0.96"*.
12. **21 named files exist, 0 missing.** Including all four `src/` modules, and `excess_demand.py`
    is still the only one that is not a sibling's — `grep -on 'src/wealth_tensor/[a-z_]*\.py'`
    returns exactly four hits.

---

## 4 · NOT CHECKED — named so the next pass starts above zero

**A not-checked list is a stock of unspent work, not a courtesy** (`-99`, and it is why II-42 fell).

1. **THE APPARATUS HALF OF IV-12, REPAIRED BUT DELIBERATELY NOT COUNTED.** `REVIEW-021`'s IV-5
   states that `paper-I.md` is *"730 lines and **7,367 words**"* and builds its finding on it —
   *"the word count is the proof, not a coincidence."* **The file has been 7 527 words since
   `623a117` (2026-08-10)**, including at `c3b1b31`, the commit `-81` read. `-81`'s own falsifier is
   `wc -w`, and `wc -w` has never returned 7 367. `docs/promises-adjudicated.tsv` row `cbd18be550`
   has the right number — *"present, 730 lines, 7 527 words"* — so the TSV and the review document
   have disagreed for nineteen sessions and no pass compared them. This is the reviewing apparatus,
   which Paper IV names nowhere, and it is scored the way `-79` scored II-39: **repaired, not
   counted.** A marked correction is appended to REVIEW-021 §2 IV-5; the historical text is not
   rewritten. **`-83` opened the class — the adjudications are an artefact too. This says the
   REVIEW DOCUMENTS are one as well, and nobody has measured their error rate either.**
2. **Two more §8 entries that may fail §8's own test, considered and NOT repaired.** *"And a control
   that controlled for the wrong thing"* names no counterfactual, but it is a rider on the second
   framing rather than a route of its own. *"Centring SMD as the defence"* states what §4 does
   (*"uses SMD as a boundary, once"*) rather than what it would do otherwise. Both are judgement
   calls about what counts as an entry, not checks; a pass that wants them should first rule on
   whether §8 has eight entries or nine.
3. **§9 item 9's census, "Three others are not measured".** §7 makes a within-literature absence
   claim about the THIRD literature too — stock-flow consistency's *"stocks are financial"* and *"a
   physical stock degrades on a schedule the financial accounting does not record"* — in different
   words from the two the limitation quotes. If that is an absence of the same kind, the census
   undercounts, and it is IV-4's shape a third time. **NOT COUNTED because it is not checkable in
   under a minute**, which is this project's own bar for a finding. It is the sharpest unspent item
   on this list.
4. **§7's Piketty relocation records no constraint and no lapse.** §7's stated standard is
   *"recording which constraint, and when it lapsed."* Solow's clause meets it (§1.1 dates the
   lapse); SMD's is a boundary rather than a relocation; **Piketty's — *"he is measuring a different
   layer"* — records neither.** That is IV-6's shape, in the paragraph IV-6 edited, surviving the
   cut. Same reason as item 3: it turns on whether "a different layer" is "a different constraint",
   which is taste.
5. **Bibliographic verification of any reference entry.** Six of 28 carry `✓`. Unchanged since
   `-81`. `PREPRINT-CHECKLIST.md` defers it to pre-submission.
6. **`wt133`'s sweep-3 blind spot, still named and still unbuilt.** A body proper noun with no
   reference entry is invisible to both sweeps. `-81` named it after IV-6; nothing has built it.
   **A3′ is the other half of the same gap and this pass ran it by hand.**
7. **§4 and §5's mathematics**, and §8's *"three supporting results were built and all three
   arithmetics were correct"* — still not enumerated in the manuscript. Both inherited from `-81`
   §4 unchanged.
8. **The version stamp.** `paper-IV.md` still reads *Version 0.1, 2026-08-16* with fourteen repairs
   landed since. Third manuscript in that state; **it is Jason's**, and it has been on this list
   since `-81`.

---

## 5 · THE METHOD RESULT — AND THIS PASS DOES NOT PROPOSE ONE

**Five mechanisms have been proposed for the non-decaying counter. Four died one pass after being
proposed. This pass proposes nothing, and the reason is inside its own row.**

Residue is 2 of 4 here, and residue was proposed at `-77` and refuted at `-78`. More to the point,
**the two residue findings are the two that cost least.** IV-10 — the largest, the one that found a
script printing this paper's numbers that this paper never named — blames to `-75`, Paper IV's
FIRST independent read, and survived two more. IV-13's site is `5efe626`, the commit that added the
manuscript, and it has survived **all five** reads of it. A mechanism that cannot touch either of
the two largest findings in its own row is not a mechanism, which is `-99`'s sentence and it holds
again on a different manuscript.

**What this pass DOES add is about the instruments, and it is `-99`'s class carried one step.** `-99`
showed that a cross-reference can resolve and be wrong, on one number, on one manuscript. Applied to
Paper IV — to 97 references and six quoted phrases — the question found one more, **inside the
limitation the previous pass added**. Two manuscripts, two reviewers, the same class: A3 as built
answers *"does the target exist"*, and the corpus keeps asking it as though it answered *"is the
pointer right"*. That is a property of the instrument, not of either paper, and it is now the
biggest unbuilt thing in this project (see the handoff's tee-up 1, still unclaimed).

**And the honest note on the other side.** The one wrong pointer turned up in the first six phrases
checked, and there are more quoted phrases in this manuscript than six — every internal `§N` claim
about what a section *does*, as opposed to what it *says*, went unchecked. **The correctness
question is not exhausted on Paper IV. It is opened on it.**

---

## 6 · THE TELLS

1. **THE SCRIPT KNEW.** `wt018_report.py`'s configuration block says it exists so that "the paper,
   the tests and this script all describe one experiment rather than three similar ones." It was
   written to be the paper's table and the paper never learned its name. **Look for the artefact
   that knows about the manuscript before looking for the manuscript that knows about the artefact.**
2. **A NEGATIVE CONTROL THAT FAILS IS DOING ITS JOB.** The first version of IV-10's new test
   asserted the endpoints follow from `(N−1) − S` and predicted `(299, −100)` at `S = 100`. The
   module returned `(300, −100)`. The derivation was wrong, the control caught it, and what it
   caught became CLEARED item 1 — the best thing in this pass's cleared list. **A control you were
   sure of is not a control.**
3. **STRIP THE MARKUP BEFORE YOU CALL A QUOTATION MISSING.** `emphatically **not**` is
   `emphatically not` to a reader and two tokens to a grep. One false MISS, caught by reading the
   target rather than trusting the tool.
4. **THE PREVIOUS PASS'S FALSIFIERS ARE THE CHEAPEST FINDINGS IN THE ROOM.** IV-13 came out of
   `REVIEW-021` IV-8's own falsifier, verbatim, and IV-12's third place came out of `-81`'s own
   IV-5 repair. Two of four findings were written down, by the previous reviewer, as things to
   check. **Read the previous review's falsifiers before you read the manuscript.**
5. **AN EXHAUSTIVE COUNT IN §10 HAS NOW BEEN WRONG TWICE.** IV-4 was a census of guard tests; IV-12
   is a census of number-sources, four paragraphs above it. The repair both times was to stop
   counting. **A census in a prose section is a promise nobody can keep.**
