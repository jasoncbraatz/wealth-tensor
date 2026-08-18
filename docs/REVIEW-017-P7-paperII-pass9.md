---
new_instrument: none
instrument_name: "— (none. All five axes A1–A5 were inherited and every one of them had already been pointed at Paper II. docs/p7-passes.tsv's matrix read Paper II 5 of 5 before this pass began, and the handoff forbade inventing a sixth while Paper III has three empty cells.)"
findings_from_new_instrument: 0 of 3
# FALSIFY THIS ROW. `none` is the strongest claim in this file, so it is the easiest to break:
#   git log --diff-filter=A --format='%h %ad' --date=short -- scripts/wt137_paperII_p7pass9.py
# wt137 is a PATCH script, not an instrument — it applies edits, it does not look for them.
# If any NEW way of looking was invented here, this row is wrong. The check is REVIEW-017 §1:
# every instrument named there is cited to the earlier session that built it.
# THE POINT OF THIS ROW: it is the first row in the ledger where the toolkit was held still.
# Ledger of all seven passes: docs/p7-passes.tsv
---

# REVIEW-017 · Paper II's SEVENTH independent `P7` read — THE FIRST FROZEN-INSTRUMENT PASS

**Session:** `wealthTensor-77` · **Date:** 2026-08-18 · **Manuscript:** `docs/papers/paper-II-redistribution/paper-II.md`, **557 lines read end to end** (561 after the patch)
**Patch of record:** `scripts/wt137_paperII_p7pass9.py` — 4 manuscript edits, 1 test edit, 8 post-conditions
**Result:** **three findings, three repairs, zero carded as unrepaired.** Paper II's counter goes 9 → 2 → 4 → 3 → 4 → 5 → **3**.

**IT IS NOT A ZERO, AND THE NUMBER IS THE POINT.** This is the first pass in the project's history
run with the instrument set held still — no axis invented, none borrowed from another manuscript,
nothing new to confound the count. Three findings came out of tools Paper II had already seen.
The honest reading is in §5 and it is not the flattering one.

---

## §1 · COVERAGE CLAIM — all five axes, run before a word of prose

Every RC below was recorded before the manuscript was read. **No instrument was invented.** Each
row names the session that built the axis, which is what makes `new_instrument: none` falsifiable.

### 1.1 · The five axes

| axis | built by | run here | count |
|---|---|---|---|
| `A1` quantifier read-forward | `-72` (`wt130`) | `wt130_quantifier_sweep.py` **RC 0** | **161 tokens on 124 of 557 lines**, each read forward |
| `A2` grep the document for the failure mode it names | `-72` (non-script) | 4 named failure modes enumerated, each grepped back at the document | **2 findings** (`II-32`, `II-33`) |
| `A3` cross-reference sweep + reader pass | `-74` (`wt133`) | `wt133_crossref_sweep.py` **RC 0** | 43 §N.M refs, 12 distinct, **0 unresolved**, 1 dismissed |
| `A4` run the manuscript's own regeneration commands and diff | `-74` | `wt030_report.py` **RC 0**, `wt077_tail_index.py` **RC 0** | every §3 number diffed; **1 finding** (`II-32`) |
| `A5` grep each named module against its paired script, run every named command | `-75` | all 6 named artefacts + 3 named commands | **1 finding** (`II-34`) |

Supporting: `handoff_gate.py --coach` **RC 0**, Paper II at baseline **2 conduct / 0 concessive**,
before and after. `pytest tests/ -q` → **1078 passed, 0 failed**, 68.24 s, after the patch.

### 1.2 · `A5` POINTED AT A SITE IT HAD NOT BEEN POINTED AT — §5, not only §7

`-76` ran `A5` against the four modules and three commands **§7** names. `A5`'s originating
statement (`-75`) is broader: *"a data-availability section is a list of promises, so grep every
pairing and run every command."* The manuscript names an artefact **outside** §7 — §5.5 names
`test_the_result_is_not_a_lucky_seed` — and that pairing had never been checked. That is `II-34`.
**This is not a sixth axis.** It is the same operation on a site the enumeration had missed, which
is exactly what the matrix's own caveat warns about: *filled is not exhausted*.

| artefact the manuscript names | where | verdict |
|---|---|---|
| `src/wealth_tensor/redistribution.py` | §7 | exists; imported by `wt030_report.py` ✓ |
| `scripts/wt030_report.py` | §7 | **RC 0** — and see `II-32` |
| `scripts/wt077_tail_index.py` | §7 | **RC 0**, all four quantities to the digit ✓ |
| `tests/test_redistribution.py` | §1, §7 | **18** `def test_` at head ✓ |
| `tests/test_excess_demand.py` | §7 | holds the second named guard ✓ (`-76`'s `II-30` repair verified) |
| `test_a_flat_gini_does_not_mean_a_bounded_one` | §4, §7 | in the counted module ✓ |
| `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` | §7 | in `test_excess_demand.py` ✓ |
| **`test_the_result_is_not_a_lucky_seed`** | **§5.5** | **`II-34` — runs at `T` = 600; every figure it mitigates is at `T` = 1200** |
| `docs/RESULT-END-TO-END-001-E1.md` | §3.2 | records the check, its thresholds **and** the pre-registration ✓ |
| `python3 -m pytest tests/ -q` | §7 | **RC 0**, 1078 passed ✓ |

### 1.3 · `A4` — §3 re-diffed against the two named commands

`-76` regenerated 39 numbers cell by cell on 2026-08-18 and that work is **settled and was not
repeated**. What was checked here is the one question a value-by-value diff does not ask:
**is there a number in §3 that neither named command produces?** There is exactly one, and the
manuscript already knew: `grep -c 0.99875` against both commands' stdout returns **0 and 0**.
That is `II-32`. `-76`'s `II-27` repair was also re-verified surviving — the patched
`wt030_report.py` prints `every  30 periods at r=0.60  Gini=0.451`.

---

## §2 · FINDINGS

### `II-32` — TWO SITES STILL PROMISE WHAT §7 ITSELF SAYS IS FALSE, AND IT IS THE RESIDUE OF `-76`'s OWN REPAIR

§7's opening sentence, **written at `-76`**, says §3.4's Gini ceiling (*N*−1)/*N* = 0.99875
*"is arithmetic in N and is printed by no command here."*

**Seven lines below it**, §7's regeneration bullet reads *"**Regenerate every number in §3:**
`python3 scripts/wt030_report.py` — except §3.1's four closed-form quantities"* — a list that does
not contain the ceiling. And **§1's contribution 5** reads *"every number below is regenerated from
a public repository by the two commands §7 names"*, with no exception at all.

**Confirmed mechanically, not argued:** `0.99875` appears **zero times** in the stdout of
`wt030_report.py` and **zero times** in the stdout of `wt077_tail_index.py`.

**This is `II-27`'s shape at `II-27`'s own site, one pass later.** The sentence that condemns it is
in the same bullet: *"a single command named for numbers it does not produce is a provenance claim
that reads as checked and is not."* `-76` repaired `II-31` at §7-intro and §5.5 and did not carry
the exception to the two **universal** claims — and §1's is the broader of the two, because it says
*every number*, not *every measured number*, so the escape hatch `-76` explicitly noted for §7's
intro does not exist there.

**Repaired by moving the PROSE, and that is the inverse of `II-27` on purpose.** `-76`(iii) says to
ask which of a claim and its provenance is **right** before deciding which one moves. Here §7's
intro is right: the ceiling is arithmetic in *N*, and making `wt030_report.py` print it would blur
the measured/derived distinction that §5.5 and §7 both draw and that §3.4's whole result depends
on. `wt137`'s post-condition asserts the exception now stands at **four** sites and **re-runs
`wt030_report.py` to confirm `0.99875` is still absent** — a guard against a future session
"fixing" this by moving the wrong object.

### `II-33` — §3.4 CALLS A SATURATED READING "THE CEILING" — IN THE SECTION WHOSE ENTIRE CONTRIBUTION IS SEPARATING THEM

§3.4, twelve lines apart:

> *"the unopposed process reads Gini 0.994 and flat — **short of the 0.99875 ceiling** it is pinned against"*

> *"a gap of 0.103 whose upper edge is **the saturation ceiling itself**"*

**Falsified by the section's own arithmetic.** 0.994 − 0.891 = **0.103**, the number printed.
0.99875 − 0.891 = **0.10775**. The gap's upper edge is the saturated *reading*, not the ceiling —
and the difference between those two objects **is §3.4's result.** The section exists to say that a
drift test failed because it could not tell "stopped rising" from "reached the maximum", and its
own summary sentence collapses the distinction it just drew.

**Repaired without touching the argument.** *"a saturated reading and not the 0.99875 ceiling it
falls short of"* — the upper edge is *N*-dependent either way, which is all the following clause
(*"redrawn for every N"*) needs. `-76`(i) paying out again: the paragraph that names a failure mode
is where to start.

**Considered and NOT counted as a third site:** §3.4 also says *"The drift test was measuring the
ceiling."* That is idiom for measuring headroom exhaustion and does not make an identity claim.
Scoped out deliberately rather than folded in to inflate the finding.

### `II-34` — §5.5's MITIGATION IS MEASURED AT HALF THE HORIZON OF THE FIGURES IT MITIGATES

§5.5, limitation 5 — *"one seed per reported figure"* — offers exactly one answer:

> *"Seed-robustness is asserted separately rather than averaged in: `test_the_result_is_not_a_lucky_seed` holds two configurations inside a stated band across five seeds."*

**Every reported figure is at *T* = 1200** (§2.1, and `wt030_report.py`'s `T=1200`).
**That test runs at *T* = 600** — `tests/test_redistribution.py` sets `T = 600` at module scope and
the test reaches the model through `econ()`. And §3.4 says, in the manuscript's own words, that the
top share *"is also horizon-stable **where the Gini is not**"* — and the band is on the **Gini**.
So the paper's only seed-robustness guard was measured on the statistic it calls horizon-sensitive,
at half the horizon of the numbers it is offered for.

**MEASURED BEFORE ASSERTED**, `-76`(iii) and `-75`(iii):

| | seeds 0–4 | in band |
|---|---|---|
| `T` = 600, stock *r* = 0.025, band (0.35, 0.55) | 0.4300 0.4361 0.4354 0.4186 0.4442 | ✓ |
| `T` = 600, flow *r* = 0.25, band (0.30, 0.50) | 0.3852 0.3924 0.3912 0.3744 0.3961 | ✓ |
| **`T` = 1200**, stock *r* = 0.025 | 0.4430 0.4398 0.4451 0.4318 0.4361 | ✓ |
| **`T` = 1200**, flow *r* = 0.25 | 0.3948 0.3936 0.3957 0.3867 0.3894 | ✓ |

**The claim is TRUE and the guard was short, so this one repairs the PROMISE** — `II-27`'s shape,
and the mirror of `II-32` in the same patch. The test now runs both horizons.

**Guard honesty, both directions, at the NEW horizon, before the assertion was written:** at
*T* = 1200 the bands **pass** for the two real configurations and **fail** for `stock r = 0.100`
(0.2184–0.2215) and `flow r = 1.000` (0.1242–0.1252). A band that could not reject anything at the
new horizon would have been decoration.

**Test count deliberately unchanged at 18.** Three manuscript sites and
`test_paper_test_counts_are_derived.py` all pin it; the body moves, the count does not. `wt137`
asserts `18` as a post-condition.

---

## §3 · CLEARED — 17 rows checked and found sound. `M` = measured, `R` = re-run, `A` = argued

`-76`'s 22 cleared rows are **not** repeated here. These are this pass's own, and three of them
were live candidates that died on contact — which is the part worth reading.

| # | claim | how | verdict |
|---|---|---|---|
| D1 | **§7 names the failure mode *"a sentence whose truth changes … which nothing in the repository was watching"* — so: is the 18-test count watched?** | R | ✓ **YES.** `test_paper_test_counts_are_derived.py::test_paper_ii_module_count_is_live_and_is_what_paper_ii_says` asserts `live == 18` **and** that the manuscript's own phrasing is present. A live `A2` candidate, killed by the repository. |
| D2 | §2.2 *"verified to machine precision in the implementation rather than assumed"* | R | ✓ `transfer_error` is a **relative** error, `max` over assessments, asserted `< 1e-12` |
| D3 | §3.1 *"The test suite asserts agreement within 10 %"* | R | ✓ `pytest.approx(ceiling, rel=0.10)` |
| D4 | §3.1 *"κ = *r* exactly"* on a stock base at zero exemption | R | ✓ `rel=1e-9` |
| D5 | §5.5 *"a single path at `seed = 0`"* | R | ✓ `src` default `seed=0`; `wt030_report.py` never overrides it |
| D6 | §3.1's *"roughly an order of magnitude apart in κ, **at every rate tested**"* | M | ✓ all **seven** matched rates: ratios 9.75–10.0 |
| D7 | §3.2 names `docs/RESULT-END-TO-END-001-E1.md` as recording the check, **its thresholds**, and that the withdrawal was written down **before** the run | R | ✓ all three present (`§5` fixes thresholds; *"Registered … before any leg was run"*) |
| D8 | §3.1's note: flow rows at *"the implementation's default"* ρ = 1 | R | ✓ `realization=1.0` |
| D9 | §2.1's parameter block *N* = 800, μ = .05, σ = .20, *a* = .05, *T* = 1200 | R | ✓ identical to `wt030_report.py`'s header |
| D10 | §7's commit pin **3b11f23** still the last commit touching `redistribution.py` after this patch | R | ✓ `wt137` touches only `docs/` and `tests/` |
| D11 | `-76`'s `II-27` repair survives: the *P* = 30 row is in the named command's output | R | ✓ `every  30 periods at r=0.60  Gini=0.451` |
| D12 | `-76`'s `II-29`/`II-31` repairs agree: §5.5 and §7 both now say **five** closed-form quantities | M | ✓ same five, both sites |
| D13 | §3.3's *"reducing κ by a quarter"* | M | ✓ 0.0250 → 0.0188, 24.8 % |
| D14 | §3.4's 0.103 gap and 0.039 headroom, recomputed from the full 14-row sweep | M | ✓ (their **wording** is `II-33`; their **values** are right) |
| D15 | `A3` reader pass on the two §-references `-76`'s edits added (41 → 43) | M | ✓ both resolve to §3.4, which exists and says it |
| D16 | **§3.1's *"no function of κ alone reproduces this section's table"*** — a live candidate: all six κ in that table are **distinct**, so a lookup function trivially reproduces it, and half the supporting evidence is §3.3's | A | ✓ **cleared.** κ ≈ 0.10 maps to Gini 0.222 and 0.125; any function of κ alone reproducing both would have to be wildly non-smooth across a 2.6 % change in κ. Substantively right, loosely referenced. **Not repaired — repairing it would be taste, not truth.** |
| D17 | **§2.3's *"a stated structural property of **every** real tax system — … the **near-universal** practice"*** — a live `A1` candidate: *every* and *near-universal* in one sentence, and the paper's own reference list carries Toder & Viard on mark-to-market, i.e. the exception | A | ✓ **cleared** on the reading that ρ *as a coordinate* exists in every system while ρ < 1 is near-universal. Recorded because it is a genuine reader stumble, and a future pass may rule otherwise. |

---

## §4 · NOT CHECKED — the honest list, and what it costs `-78`

`-75`(iv)'s rule applied: an item closeable in four minutes was **closed**, not written down. Three
were drafted and closed at drafting — the commit-pin re-verification (became `D10`), the
`RESULT-END-TO-END-001-E1` pairing (became `D7`), and the seed default (became `D5`).

1. **`A6`, the docstring axis — PARKED, NOT SPENT.** The handoff forbade spending it on the frozen
   pass and that was honoured. Nineteen unasserted prose claims remain in
   `tests/test_redistribution.py`. **Its nearest neighbour is now visible from `II-34`:**
   `test_periodicity_is_second_order_at_a_matched_average_rate`'s docstring says *"Verified
   horizon-stable at T = 600 and T = 1200"* — prose, asserted by nothing, about the exact property
   `II-34` turned out to hinge on. `wt137`'s own new docstring joins the nineteen.
2. **THE GENERAL FORM OF `II-34`, DELIBERATELY SCOPED OUT.** `II-34` fixed the one test §5.5
   *names*. But **16 of the 18 tests reach the model through `econ()`, and `econ()` runs at
   *T* = 600**, while every reported figure is at *T* = 1200 — and §7 calls those tests *"the ones
   that hold this paper's claims in place."* Most pin structural facts that are horizon-robust, so
   this is a **question, not yet a finding**: should the suite that holds the claims run at the
   horizon the paper reports? It is the strongest single lead in this document and it was not
   chased, because chasing it inside a frozen pass would have been a fourth finding bought with a
   change of scope.
3. **The nine uncited reference entries.** `wt133` sweep 2, card `1217568192511533`. Untouched.
4. **Bouchaud & Mézard's two quotations, still not read against the source.** `REFERENCE-POLICY`'s
   eighth pass, card `1217556161163494` — now **six** sessions deferred.
5. **Paper I's L568 non-circularity sentence** — still the untested third instance, still one
   `git log --diff-filter=A` away.
6. **`wt077_tail_index.py` is covered by no per-file pin** (`REVIEW-016` §4 item 1). Unchanged.
7. **The version stamp** — card `1217568297674954`, now a **seventh** data point: four more edits
   landed on Paper II today, under a stamp reading *"Version 0.2, 2026-08-11."*

---

## §5 · WHAT THIS PASS SAYS ABOUT THE METHOD — and it is not the flattering reading

**The frozen pass returned three. It did not return zero.**

That is the measurement the definition of done has been waiting seven sessions for, and it points
away from the story the project has been telling itself. The standing explanation for non-decaying
counters was *"each pass brought a new instrument that found what the previous passes structurally
could not."* `-76` made that a three-data-point claim. **This pass is the control, and the control
disagrees:** no new instrument, and Paper II still yielded three.

**Where the three actually came from, which is the useful part:**

* **Two of the three are the residue of the previous pass's own repairs.** `II-32` is `II-31`
  landing at two sites of four. `II-33` sits in a section `-76` did not edit but did re-derive.
  A repair pass **creates surface**, and the next pass reads it for the first time. That is a
  structural reason for a non-zero count that has nothing to do with new instruments — and nothing
  in the ledger was measuring it.
* **One came from an old axis pointed at a new site.** `A5` at §5 rather than §7. The matrix's own
  caveat — *filled is not exhausted* — is now two-for-two: `-76`'s `II-27` came out of a cell `-74`
  had filled, and `II-34` came out of a cell `-76` had filled.

**The honest conclusion, and it is a change to the bar, so it is Jason's to make.** The definition
of done wants two consecutive zero-finding passes. If a repair pass reliably seeds the next pass's
findings, **two consecutive zeros may be unreachable by construction while any pass still repairs
anything** — the first zero requires a predecessor that changed nothing. `-78` is Paper II again,
still frozen, and it is the first session that can test *that*: it inherits four edits, so if the
pattern holds it will find their residue, and if it finds nothing the pattern is broken and the
pair is live. Either way `-78`'s count is informative in a way no previous count has been.
