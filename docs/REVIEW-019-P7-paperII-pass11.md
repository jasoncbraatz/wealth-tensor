---
new_instrument: none
instrument_name: "— (none. All five axes A1–A5 inherited; docs/p7-passes.tsv recorded Paper II at 5 of 5 before this pass began. A6, the docstring axis, remained parked as ordered. The THIRD consecutive frozen pass and the second half of -78's depth experiment.)"
findings_from_new_instrument: 0 of 2
residue_of_previous_pass: 0 of 2
site_already_enumerated_by_78: 2 of 2
# FALSIFY THIS ROW, FOUR WAYS.
#   1. `none`:      git log --diff-filter=A --format='%h %ad' --date=short -- scripts/wt141_paperII_p7pass11.py
#                   wt141 is a PATCH script, not an instrument. §1 cites every axis to the
#                   session that built it. If a new way of LOOKING was invented here, this row
#                   is wrong.
#   2. `residue`:   git blame the two sites at the parent commit. II-37 → 58f7f5bb (-74) and
#                   6b0655b2 (-77); II-38 → f1ceac74 (2026-08-10). -78's commits are 52a18f1 /
#                   3a11f1d / 4eb0a18. If either blames to -78, this row is wrong.
#   3. `site`:      open REVIEW-018 §1 (A5's 20-artefact enumeration, A4's second question) and
#                   REVIEW-018 §4 item 7. Both of this pass's sites are named there. If either
#                   is absent, THIS PASS'S HEADLINE CLAIM IS WRONG and the depth reading lives.
#   4. the count:   scripts/wt141_paperII_p7pass11.py carries 22 post-conditions. Run it.
# Ledger of all nine passes: docs/p7-passes.tsv
---

# REVIEW-019 · Paper II's NINTH independent `P7` read — the depth falsifier, fired

**Session:** `wealthTensor-79` · **Date:** 2026-08-18 · **Manuscript:** `docs/papers/paper-II-redistribution/paper-II.md`, **565 lines read end to end**
**Patch of record:** `scripts/wt141_paperII_p7pass11.py` — **0 manuscript edits**, 2 script edits, 1 checklist edit, **22 post-conditions**
**Result:** **two findings, three repairs, zero carded.** Paper II's counter goes 9 → 2 → 4 → 3 → 4 → 5 → 3 → 2 → **2**.

**THE HEADLINE IS NOT THE COUNT. IT IS THE COLUMN `-78` ASKED FOR.**
`-78` argued that what remains — after new-instruments and after repair-residue were both
refuted — is **depth of application**, and made one sharp prediction: an axis exhausted at its
own sites stays exhausted, so a ninth read at the same depth should find *materially fewer than
two*, and **two or more from sites `-78` already opened** would refute it.

**Both findings come from sites `-78` opened. `2 of 2`.** One is the artefact pair `A5`
enumerated and `A4` ran; the other is item **7 on `-78`'s own not-checked list**, deferred on
its label. Depth of application is **not** the mechanism either.

**And the honest conclusion `-78` pre-committed to is now on the table:** Paper II's counter is
measuring the reviewers rather than the paper. It is Jason's to rule on. §5 states the case
without arguing for it.

---

## 0 · What is NOT claimed here, stated before the findings

* **Nothing was invented.** Five axes, all inherited, all run before a word of prose. `A6` stays
  parked.
* **No finding was manufactured.** Three live candidates died on contact and are named in §3
  with the evidence that killed them, not merely listed.
* **The verdict does not hinge on an accounting choice.** A third defect was found and repaired
  — `II-39`, in the `A1` instrument itself — and it is **deliberately NOT counted**, because
  `wt130_quantifier_sweep.py` is part of the reviewing apparatus and is named nowhere in
  Paper II. The counter counts defects in the paper and in the artefacts the paper names. Two
  is the number either way, so the falsifier's verdict is unaffected. §2.3 records `II-39` in
  full anyway, because a defect in the instrument that measures the paper is worth more to the
  next session than a tidy row.

---

## 1 · The five axes, run before a word of prose

| axis | what was run | measured output | findings |
|---|---|---|---|
| `A1` | `scripts/wt130_quantifier_sweep.py paper-II` (RC 0) — built at `-72` | **162 quantifier tokens on 124 of 565 lines**, read forward from every flagged line during the end-to-end read | 0 on the manuscript; **`II-39`** on the instrument |
| `A2` | grep Paper II for the failure modes it names in its own prose — originates `-72`. `-78` extracted eight; REVIEW-018 §1 lists them, so they were **inherited rather than re-derived**, per the at-bat | 8 named failure modes turned back on the paper | **`II-37` and `II-38` — BOTH.** §7's *"a command named for numbers it does not produce is a provenance claim that reads as checked and is not"* is `II-37` verbatim; §7's *"nothing in the repository was watching"* is `II-38` verbatim |
| `A3` | `scripts/wt133_crossref_sweep.py` (**RC 0**) — built at `-74` | Paper II: **45 §N.M references, 12 distinct, 0 unresolved, 1 dismissed**; sweep 2: 16 entries, 7 cited, **9 not** (carded `1217568192511533`, untouched) | 0 |
| `A4` | `wt030_report.py` (RC 0) **and** `wt077_tail_index.py` (RC 0) — originates `-74`. **Both of `-77`'s questions asked**: do the values match, and is there a number in §3 neither command produces? | all **39 tabulated §3 values reproduce**; the second question, asked of the *provenance sentence* rather than of a number | **`II-37`** |
| `A5` | every named artefact greped against its pairing, **enumerated from the whole document**, every named command run, **and the artefacts READ** — originates `-75`, first on Paper II at `-76` | **22 distinct named artefacts** (`-78` found 21; the 22nd is below), all resolve; 5 named files exist and were **read**; 3 named test functions exist at their named sites and their arithmetic was read | **`II-38`** |

**`A5`'s enumeration gained one artefact over `-78`'s.** `-78` recorded 20 backticked plus one
non-backticked (the SHA `3b11f23`). The 22nd is **`NBER Working Paper 14730`** in the Benhabib,
Bisin and Zhu entry — non-backticked, and the object §6's characterisation of Propositions 3
and 4 is explicitly *taken from*. It **resolves**: `w14730` is *The distribution of wealth and
fiscal policy in economies with finitely lived agents*, Benhabib, Bisin and Zhu, NBER. Not a
finding — a coverage correction, recorded so the enumeration stops drifting.

---

## 2 · The findings

### `II-37` · §7 promises a command regenerates every §3 number; four §3 numbers are printed by neither command — and `-78` proved they cannot be recovered from what *is* printed

§7 states, and §1's contribution 5 states more strongly:

> **Regenerate every number in §3:** `python3 scripts/wt030_report.py` — except §3.1's four
> closed-form quantities … and except §3.4's Gini ceiling …

> A **reproducible artefact**: every number below is regenerated from a public repository by
> the two commands §7 names — save §3.4's Gini ceiling …

§3.1 reports four numbers that are neither: the κ residuals **−4.3 %, −4.6 %, −5.7 %** at the
tabulated flow rates and **−6.8 %** at *r* = 0.010. They are not closed-form quantities. They
are not the Gini ceiling. And **neither named command printed them** — verified by running both
and by grepping every script for a residual print.

**What makes this sharper than a missing line item is `-78`'s own `II-35`.** That finding
established, with a table, that recomputing these four from the output that *is* printed gives
the WRONG answer: the 4-decimal κ column yields −4.352 / −4.912 / −6.777 against the true
−4.344 / −4.568 / −5.749, wrong by up to **1.05 percentage points**, because at *r* = 0.025 the
display quantum is ±2 % of κ itself. So this is not a provenance claim that is merely unproven.
**It is a provenance claim whose only available execution path produces different numbers than
the paper prints** — which is precisely the failure mode §7 names in its own next sentence.

**This is the third member of a family already worked twice, and both predecessors are cited in
the repository.** `II-27` (`-76`) found two §3.3 numbers missing from `wt030`'s output.
`II-31` (`-76`) found §3.4's Gini ceiling missing from §7's exception list. The residuals sat
between them through both.

**Repaired by `II-27`'s precedent — MAKE THE PROMISE TRUE, do not weaken the prose.**
`wt030_report.py` now closes with a `FLOW-BASE KAPPA RESIDUAL` block printing all seven flow
rates from the **unrounded** κ:

```
  flow r=1.000  kappa=0.102609047  r*E[eta+]=0.107268940  residual=-4.344 %
  flow r=0.500  kappa=0.051307705  r*E[eta+]=0.053634470  residual=-4.338 %
  flow r=0.250  kappa=0.025643045  r*E[eta+]=0.026817235  residual=-4.378 %
  flow r=0.100  kappa=0.010236878  r*E[eta+]=0.010726894  residual=-4.568 %
  flow r=0.050  kappa=0.005094683  r*E[eta+]=0.005363447  residual=-5.011 %
  flow r=0.025  kappa=0.002527559  r*E[eta+]=0.002681723  residual=-5.749 %
  flow r=0.010  kappa=0.000999413  r*E[eta+]=0.001072689  residual=-6.831 %
```

Three properties of the repair are deliberate and each has a post-condition:

1. **No extra simulation.** The block reuses the MAIN TABLE's κ. `P13` asserts the block's κ
   agrees with the table's at 4 dp at every flow rate, which is the check that it did not
   quietly re-run anything.
2. **E[η⁺] is IMPORTED from `wt077_tail_index.eta_plus_closed_form`, not restated.** `II-36`
   had already been wrong about this exact constant once; a second copy is a second chance to
   fork. `P12` asserts both that the import is present and that the value `wt030` prints agrees
   with the value `wt077` prints.
3. **The residual is computed against the form the PAPER states**, *r*·E[η⁺], not against
   `wt077`'s `predicted` *r*·E[η⁺]/(1+μ). Adopting the other form changes a stated contribution
   and is Jason-sized (§6(f) of REVIEW-018, still open). The repair leaves that a one-line
   change rather than pre-empting it.

`P5`–`P8` assert the printed residuals round to exactly the four values §3.1 states. `P9` and
`P10` make §3.1's words *"flat between r = 1.000 and r = 0.500"* and *"widens monotonically
below it"* into assertions. `P11` holds the headline *"4–7 %"* range.

**The manuscript was not edited.** `P1` asserts `paper-II.md` is byte-identical.

* **RESIDUE OF `-78`: NO.** §7's bullet blames to `58f7f5bb` (`-74`, 2026-08-17) and
  `6b0655b2` (`-77`, 2026-08-18); §1's clause to `6b0655b2` (`-77`). `-78` wrote the §3.1
  italic note and the corrected values — which *sharpen* the contradiction but are not its
  site. The residuals were unprinted before `-78` too, so the finding stands against the
  pre-`-78` manuscript unchanged.
* **SITE ALREADY ENUMERATED BY `-78`: YES, TWICE OVER.** Both commands are on `A5`'s
  20-artefact list and both were RUN (REVIEW-018 §1: *"3 named commands run"*). And `A4`'s
  second question — *"is there a number in §3 neither command produces?"* — is the question
  that produced `II-35`, pointed at this exact sentence. The axis was applied to the numbers
  and not to the sentence that promises them.

### `II-38` · the References note defers ten entries to a checklist that did not carry the item

The References note closes:

> The remainder are standard works whose details are to be re-checked at submission per
> `docs/papers/PREPRINT-CHECKLIST.md`.

Sixteen entries: **4 marked ✓, 2 marked ✓⧗, 10 unmarked.** The ten unmarked are "the
remainder", and their verification is deferred to a named file.

**`docs/papers/PREPRINT-CHECKLIST.md` carried no such item.** §A is apparatus (title, abstract,
keywords, JEL, contributions, abandoned approaches, limitations, data-and-code, regeneration
script, related work, structural-over-contingent, costless-abandonment, no-live-placeholders).
§B is the reproducibility paragraph. §C is venue. §D is pre-registration. **References appear
nowhere.** The deferral has pointed at a document that was not holding it since **`f1ceac74`,
2026-08-10** — through every read of the References note this paper has had.

`REFERENCE-POLICY` §1 states the evidentiary requirement and §4 the marks, so the *work* is
fully specified. What was missing was anything that would **ask for it at the moment it comes
due** — §7's *"nothing in the repository was watching"*, applied to the bibliography.

**Repaired in the checklist, not the manuscript.** §A gains a checkbox requiring every entry's
details to be verified against a publisher page, a library catalogue or a Crossref record —
including the entries a draft left unmarked — and requiring the manuscript's marks to be
updated to say so. The manuscript sentence is now true, unedited. `P19`–`P21` assert the item
is present and unique and that the deferral sentence is the one still standing.

* **RESIDUE OF `-78`: NO.** `f1ceac74`, 2026-08-10; the checklist's own last touch is
  `a0f5a3a`, 2026-08-10.
* **SITE ALREADY ENUMERATED BY `-78`: YES, AND NAMED IN WRITING.**
  `docs/papers/PREPRINT-CHECKLIST.md` is one of `A5`'s 20 backticked artefacts and was recorded
  as resolving (*"5 named files exist"*). It is also **item 7 of REVIEW-018 §4**, the
  not-checked list: *"Bibliographic details of the entries not marked ✓ — deferred to
  submission per `PREPRINT-CHECKLIST`."* `-78` wrote the deferral down and trusted it. This is
  `-78(ii)` — *resolving that a named artefact exists is not applying an axis to it* — committed
  by the session that banked the lesson, in the same document, one section later.

### `II-39` · NOT COUNTED — the `A1` instrument's documented single-paper invocation sweeps two manuscripts

`wt130_quantifier_sweep.py`'s docstring documents:

```
    python3 scripts/wt130_quantifier_sweep.py paper-II        # one paper, full enumeration
```

The selector was a bare substring test over the full path. **`paper-II` is a prefix of
`paper-III`**, so that invocation swept **two** manuscripts, 805 lines of output, and the last
`TOTAL:` a reader's eye lands on was **Paper III's — 870 tokens on 673 lines**. `paper-I` is a
prefix of all four and swept **four**.

That is not a hypothetical: *"870 tokens on 673 lines"* is the exact string of the misreading
banked at `-73` (`lessons.py` id `2026-08-17-wt130-quantifier-sweep-py-prints-n`), which
travelled three documents deep. The lesson recorded the misreading; **this is its delivery
mechanism**, and it was still armed.

`-78`'s `A1` line reads `--paper II`, which drops to `sel=["II"]` and also swept two. `-78`
reported Paper II's numbers correctly by reading the FIRST block, so nothing wrong propagated —
this pass reproduced the same invocation and got Paper III's 2,694-line manuscript in the
output before noticing.

**Repaired.** A selector now matches a manuscript's **stem** or its **directory name** exactly,
or a hyphen-delimited prefix of the directory name. `paper-II` → one paper. `paper-I` → one
paper. `paper-II-redistribution` → one paper. **`II` → no match, non-zero exit, and the
existing "no manuscript matched" message**, because a loud failure is worth more than a silent
second manuscript. `P14`–`P18` assert one header for each of the four selectors, non-zero exit
on a bare `II`, four rows in the no-selector census, and that Paper II's own count is unchanged
at 162 / 124 / 565.

---

## 3 · Cleared — what was checked and did not fall

Sixteen rows. Three were **live candidates that died on contact**; naming them is what keeps
the two findings above from being the product of a lowered bar.

| # | candidate | verdict |
|---|---|---|
| `E1` | §1's *"to within 7 % at every rate tabulated"* is defended by `-78` with **6.831 % at *r* = 0.010** — a rate that is **not tabulated**, which is the very scoping error `II-35` repaired in §3.1 | **DIED ON CONTACT.** The claim is true under *both* scopings: 5.749 % over the tabulated rates, 6.831 % over the full sweep. The defence cited the looser one; the claim survives the tighter one. Nothing to repair. |
| `E2` | §7's exception list should have gained the residuals rather than `wt030` gaining a print — i.e. the repair chose the wrong side | **DIED ON CONTACT.** `II-27`'s precedent is explicit and in the repository: *"Repaired by making the promise TRUE rather than by weakening the prose."* Exempting four numbers no command produces is strictly worse for a replicator than printing them. |
| `E3` | §3.1's *"Rate 1.00 on flow reaches Gini 0.125, which a stock levy reaches at rate 0.25"* — `wt030` gives stock *r* = 0.250 → **0.123**, not 0.125 | **CLEARED.** *"Reaches"* is a threshold claim, not an equality: 0.123 ≤ 0.125, and *r* = 0.25 is the first tabulated stock rate at or below the flow frontier. The sentence is exact as written. |
| `C1` | all **39 tabulated §3 values** | **CLEARED** — every one reproduces from `wt030`/`wt077`. |
| `C2` | the §3.2 realisation table (1.00 → 0.125, 0.25 → 0.395, 0.00 → 0.994) | **CLEARED** — `wt030`'s REALISATION block, exact. |
| `C3` | §3.4's derived margins: gap **0.103**, *"0.039 to spare"*, spans 0.000–0.891 and 0.100–0.861 | **CLEARED** — exact arithmetic on `wt030`'s printed values. |
| `C4` | §3.3's *"spans 0.035"*, the interior minimum **0.451 at P = 30**, the return to **0.469 at P = 50** | **CLEARED** — 0.486 − 0.451 = 0.035; both endpoints printed. |
| `C5` | §3.3's *"reducing κ by a quarter"* (0.0250 → 0.0188) | **CLEARED** — −24.8 %. |
| `C6` | §3.1's *"roughly an order of magnitude apart in κ, at every rate tested"* — a quantifier over the whole sweep, not the table | **CLEARED** — the stock/flow κ ratio runs 10.01, 9.89, 9.81, 9.77, 9.75, 9.75, 9.75 across all seven rates. |
| `C7` | §3.1's *"for a stock base at zero exemption, κ = *r* exactly"* | **CLEARED** — exact at all seven stock rates. |
| `C8` | §3.1's Var[log *a*]: 0.076542 / 0.076536 / 0.051189, *"a change of 6 × 10⁻⁶"*, *"a third lower"* | **CLEARED** — `wt077`, exact; 6 × 10⁻⁶; 33.1 %. |
| `C9` | §5.5's *"five closed-form quantities"* = E[η⁺] + three Var[log *a*] + the Gini ceiling, and *"quadrature"* | **CLEARED** — `wt077` computes all four on a deterministic ±12σ grid, no simulation. §1, §5.5 and §7 agree on five. |
| `C10` | §5.5's *"a single path at `seed = 0`"* | **CLEARED** — `redistribution.py:89`, `seed=0` is the default and the only seed `wt030` uses. |
| `C11` | §2.2's *"verified to machine precision in the implementation"* | **CLEARED** — `transfer_error` is computed and returned, `redistribution.py:123/143/150`. |
| `C12` | the **18**-test count in the abstract, §1 and §7 | **CLEARED** — 18 before and after `wt141`; full suite **1078 passed, 0 failed**. |
| `C13` | §3.1's *"The test suite asserts agreement within 10 %"* | **CLEARED** — `test_redistribution.py:205`, `pytest.approx(ceiling, rel=0.10)`. |
| `C14` | `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` — the sibling named test, read for its **arithmetic** the way `II-36` was found | **CLEARED** — it asserts monotone non-increasing excess demand over 500 prices, and its docstring already carries the correction that the reason is unit demand, not the good count. §7's description of it is accurate. |
| `C15` | `docs/RESULT-END-TO-END-001-E1.md` — does it record *the check, its thresholds, AND that the withdrawal was written down before the check was run*, as §3.2 claims? | **CLEARED** — front matter: *"§5 fixes E1's thresholds…"*; §6: *"The FAIL branch of the design's E1 table, **written before the run**"*. All three. |
| `C16` | `REFERENCE-POLICY` §4 — does §4 carry the pre-publication rule the References note cites it for? | **CLEARED** — §4 is *"The marks"*, and *"The pre-publication rule, stated once"* is inside it. |

---

## 4 · Not checked — six items, named so the next pass starts above zero

1. **`A6`, the docstring axis — STILL PARKED**, as ordered. `tests/test_redistribution.py`
   carries **twenty-one** unasserted prose claims. Paper III has three empty cells.
2. **The nine uncited reference entries** — card `1217568192511533`. `wt133` sweep 2 does not
   set the exit code. `II-38` is a *different* object: where the unverified DETAILS were
   deferred to, not whether an entry is cited. Both are still open.
3. **`II-25`, the version stamp** — card `1217568297674954`, **NINTH** data point: three more
   commits landed 2026-08-18 under a stamp reading *"Version 0.2, 2026-08-11"*.
4. **The general form of `II-34`** — 16 of 18 tests reach the model through `econ()` at
   `T` = 600 while every reported figure is at `T` = 1200. `-78` produced evidence the lead is
   real (κ residual −4.042 % at `T` = 600 against −4.344 % at `T` = 1200). Still a question.
5. **Whether §3.1's closed form should be *r*·E[η⁺]/(1+μ)** — Jason-sized, changes a stated
   contribution. `II-37`'s repair deliberately does not pre-empt it.
6. **Papers I, III and IV** — out of scope.

---

## 5 · The method result — the falsifier fired, and the remaining reading is uncomfortable

`-78` did the honest thing: it named the mechanism it believed in, derived a prediction from
it, and handed the prediction to the next session as a falsifier it could not control.

**The prediction failed.** Not by a hair — `2 of 2`. Both findings sit at sites `-78` had
already opened, and one of them is an item `-78` wrote down on its own not-checked list and
trusted on its label.

The ledger now reads:

| pass | new instrument | findings | mechanism it was built to test | result |
|---|---|---|---|---|
| `-71` | none | 4 | the new-instrument anecdote | **refuted** |
| `-77` | none (frozen) | 3 | the new-instrument anecdote, deliberately | **refuted**; proposes *repair residue* |
| `-78` | none (frozen) | 2 | repair residue | **refuted** (0 of 2); proposes *depth of application* |
| `-79` | none (frozen) | 2 | depth of application | **refuted** (2 of 2 from opened sites) |

Three mechanisms have been proposed to explain why Paper II's counter does not go to zero.
Each was made falsifiable by the session that proposed it. **All three are dead**, and the two
frozen-pass counts have now gone 3, 2, 2 — the decay stopped.

**What is left is the reading `-78` pre-committed to, and it should be stated plainly because
`-78` earned the right to have it stated:** *Paper II's `P7` counter is measuring the reviewers
rather than the paper.* Nine independent readers, each finding two to nine defects, none of
them the same defects, in a 565-line document that has been repaired thirty-odd times. That is
the signature of a process with a roughly constant per-pass detection probability over a large
population of small imperfections — not of a document converging on correctness.

**Three observations that sharpen it, offered without a recommendation:**

* **Both findings this pass are about SENTENCES ABOUT ARTEFACTS, not about artefacts.** `II-37`
  is a provenance promise; `II-38` is a deferral. Neither is a wrong number. `-78`'s two were a
  wrong derivation and a wrong constant. The population being sampled may be shifting from
  *numbers* to *claims about where numbers live* — and the latter population is larger, because
  every artefact reference is a claim.
* **The one thing that HAS decayed is severity.** `-73`'s findings were wrong values in a
  results table. `-78`'s were a 1-percentage-point error and a fourth-decimal constant. This
  pass's two are true statements about a document that did not hold what they promised, both
  repairable **without touching the manuscript at all** — the first pass in this project's
  history with zero manuscript edits. A counter that holds at 2 while every finding gets cheaper
  is a different object from a counter that holds at 2.
* **The DoD's bar is the thing at risk.** *Two consecutive zero-finding passes* is reachable
  only if the population is finite and the axes can exhaust it. Four refuted mechanisms is
  evidence that it is not, at the granularity the passes are reading at.

**A ruling is now genuinely required, and `-79` recommends one — narrowly.**
`-78` recommended leaving the bar alone on the ground that depth-of-application made a zero
reachable. **That ground is gone.** `-79` does not recommend changing the *number* — it
recommends changing what the passes are asked to *count*, so that the bar measures the paper
again: **count only findings that require a manuscript edit.** Under that rule this pass scores
**zero**, `-78` scores **one** (`II-35`; `II-36` was a test edit), and the counter starts
measuring the document rather than its apparatus. That is a scope question, it is Jason's, and
`-79` states it as a proposal rather than acting on it — the current bar is unchanged in this
document and in `docs/p7-passes.tsv`.

---

## 6 · The tell, thirty-eight deep

`-61`–`-78` as before.

**`-79(i)` · A PROMISE ABOUT AN ARTEFACT IS A CLAIM, AND IT DOES NOT GET CHECKED BY CHECKING THE
ARTEFACT.** `A5` resolves the artefact; `A4` runs it; neither reads the *sentence* that says what
the artefact will do for a reader. `II-37` and `II-38` are both of that shape and both survived
a pass whose stated purpose was to read artefacts deeply. The check is one question per
reference: **if a replicator followed this sentence, what would they get?**

**`-79(ii)` · A DEFERRAL WHOSE TARGET DOES NOT CARRY THE ITEM IS NOT A DEFERRAL; IT IS A DROPPED
BALL WITH A CITATION.** Deferring is legitimate and this project does it well. What makes it
legitimate is that something downstream is holding the item. Grep the target. `-78` named this
deferral in writing on its not-checked list and never opened the file it pointed at.

**`-79(iii)` · WHEN A SESSION HANDS THE NEXT ONE A FALSIFIER IT CANNOT CONTROL, THE PROJECT WINS
WHICHEVER WAY IT FIRES.** `-78`'s prediction was wrong and its method was excellent: name the
mechanism, derive the prediction, hand it over, pre-commit to the uncomfortable conclusion. Four
mechanisms have now been killed in four sessions because each one was built to be killable. Copy
the shape, not the hypothesis.

**`-79(iv)` · A PREFIX IS A SILENT SET-SELECTOR BUG, AND IT DELIVERS EXACTLY THE ERROR THE
PROJECT ALREADY BANKED.** `paper-II` selecting `paper-III` printed a second manuscript's TOTAL
last, which is how a Paper III number gets into a Paper II document. The lesson about the
misreading was banked at `-73`; the mechanism that delivers it lived on for six sessions
because nobody ran the documented invocation and counted the headers.

---

## 7 · Tooling

* **`scripts/wt141_paperII_p7pass11.py`** — 3 repairs, **0 manuscript edits**, **22
  post-conditions**. `P1` is the load-bearing one and it is a *negative*: `paper-II.md` is
  byte-identical. Three post-conditions are new in kind: one asserts the two commands §7 names
  **have not forked on E[η⁺]** by comparing what each prints (the guard `II-36` needed and did
  not have); one asserts the repair bought **no extra simulation** by matching the residual
  block's κ against the MAIN TABLE's at 4 dp; and one asserts a selector **fails loudly**
  (`P16`, non-zero exit on a bare `II`) — the first post-condition in this project that pins a
  *refusal* rather than a result.
* **`scripts/wt030_report.py`** — gains the `FLOW-BASE KAPPA RESIDUAL` block. Imports E[η⁺]
  from `wt077_tail_index`; `scripts/` is **appended** to `sys.path`, never inserted, so it can
  never shadow stdlib or site-packages.
* **`scripts/wt130_quantifier_sweep.py`** — `_selects()` replaces the substring test; docstring
  carries the selector note and the reason.
* **`docs/papers/PREPRINT-CHECKLIST.md`** — §A gains the reference-verification item.
* Tags run to `wt141`; **`wt142` is free.**

---

## 8 · State at wrap

* `python3 -m pytest tests/ -q` → **1078 passed, 0 failed, 72.10 s**
* `python3 scripts/wt133_crossref_sweep.py` → **RC 0**
* `python3 scripts/wt030_report.py` → **RC 0**, now with the residual block
* `python3 scripts/wt077_tail_index.py` → **RC 0**
* `python3 scripts/wt130_quantifier_sweep.py paper-II` → **RC 0**, one manuscript, 162 / 124 / 565
* `paper-II.md` — **unchanged**, 565 lines
