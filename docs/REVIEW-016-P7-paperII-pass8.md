---
new_instrument: inherited-first-application
instrument_name: "A5 — grep each module a data-availability section names against the script it is paired with, and run every command it names (originated wealthTensor-75 on Paper IV; Paper II had never seen it)"
findings_from_new_instrument: 2 of 5
# FALSIFY THIS ROW. For a script instrument:
#   git log --diff-filter=A --format='%h %ad' --date=short -- scripts/<instrument_name>
# an earlier session's add-commit means the row is wrong. A5 is a NON-SCRIPT axis, so its
# falsifier is REVIEW-015 §2 IV-2: open it and find the axis described, or this row is wrong.
# The two findings claimed: II-27 (diffing the named command's output against §3) and II-30
# (grepping the file §7 names). II-28, II-29 and II-31 came from reading.
# THREE VALUES, NOT TWO, AND THIS ROW IS WHY: no axis was invented here, and five findings
# landed anyway. `new: no` would have recorded the exact opposite of what happened.
# Ledger of all six passes: docs/p7-passes.tsv
---

# REVIEW-016 · Paper II's SIXTH independent `P7` read

**Session:** `wealthTensor-76` · **Date:** 2026-08-18 · **Manuscript:** `docs/papers/paper-II-redistribution/paper-II.md`, 554 lines, read end to end
**Patch of record:** `scripts/wt135_paperII_p7pass8.py` — 3 manuscript edits, 1 script edit, 1 test edit, 4 post-conditions
**Result:** **five findings, five repairs, zero carded as unrepaired.** Paper II's counter goes 9 → 2 → 4 → 3 → 4 → **5**.

---

## §1 · COVERAGE CLAIM — what was actually run, and in what order

Instruments first, prose fourth. Every RC below was recorded before a word of the manuscript was read.

### 1.1 · The mechanical half

| instrument | result |
|---|---|
| `wt133_crossref_sweep.py` | **RC 0.** Paper II: 41 §N.M references, 12 distinct, **0 unresolved**, 1 dismissed as another document's section |
| `wt133` sweep 2 | 16 reference entries, 7 cited in the body, **9 not** — card `1217568192511533`, pre-existing, untouched |
| `wt130_quantifier_sweep.py` | **RC 0.** Paper II: **160 quantifier tokens on 123 of its 554 lines** |
| `handoff_gate.py --coach` | **RC 0**, Paper II at its baseline **2 conduct / 0 concessive**, before and after |
| `pytest tests/ -q` | **1078 passed, 0 failed**, 67.50 s, after the patch |
| `pytest tests/test_redistribution.py -q` | **18 passed** — §7's, the abstract's and §1's shared count, verified rather than assumed |

### 1.2 · THE NEW AXIS — every module in §7 grepped against its paired script, every §7 command run

This is `-75`'s fifth axis, applied to Paper II for the first time. It produced **two of the five findings** and it took about twelve minutes.

| §7 names | grep `^from\|^import` | verdict |
|---|---|---|
| `src/wealth_tensor/redistribution.py` ↔ `scripts/wt030_report.py` | `from wealth_tensor.redistribution import (RedistributiveEconomy as E, stationary_gini, …)` | **PAIRED** ✓ |
| `src/wealth_tensor/redistribution.py` ↔ `scripts/wt077_tail_index.py` | `numpy`, `scipy.optimize.brentq`, `scipy.stats.norm` — **no `src/` code at all** | **NOT PAIRED — and correctly disclosed.** §7's pin bullet already says it "does not cover the two `scripts/` commands". See §4, item 1 |
| `tests/test_redistribution.py` | `from wealth_tensor.redistribution import (BASES, RedistributiveEconomy, gini, …)` | **PAIRED** ✓ |
| `tests/test_excess_demand.py` (the second named guard's actual home) | `from wealth_tensor.excess_demand import Market` | different module — **`II-30`** |

| §7 command | RC | covers what it promises? |
|---|---|---|
| `python3 scripts/wt030_report.py` | **0** | **NO — `II-27`.** Its periodicity sweep is `P ∈ (1,2,4,10,20,50)`; §3.3 quotes `P = 30` and a span the printed rows cannot produce |
| `python3 scripts/wt077_tail_index.py` | **0** | **YES.** Prints all four closed-form quantities §7 pairs with it, to the digit |
| `python3 -m pytest tests/ -q` | **0** | YES — 1078 passed |

### 1.3 · Numbers regenerated cell by cell (39), not argued

Every number in §3 was checked against the output of the command §7 names for it.

* **§3.1's table, all 24 cells** — 6 rows × (Gini, κ, top-10 %, bounded) — reproduce exactly from `wt030_report.py`'s main table.
* **§3.1's closed form** E[η⁺] = μΦ(μ/σ) + σφ(μ/σ) = **0.1073** ✓ (`wt077`: `0.107269`), and the residual claim: predicted κ = *r*·0.107269 against simulated κ gives **−4.35 %, −4.91 %, −6.79 %** at *r* = 1.000 / 0.100 / 0.025 — the manuscript's −4.4 / −4.9 / −6.8 ✓, monotone in the rate ✓, and inside 4–7 % **at all seven tabulated flow rates**, not merely the three quoted.
* **§3.1's three Var[log *a*]** — 0.076542 / 0.076536 / 0.051189 ✓ (`wt077`, exact).
* **§3.1's frontiers** stock 0.000 < flow 0.125 ✓.
* **§3.2's ρ table** 0.125 / 0.395 / 0.994 ✓, and the **agent-by-agent identity measured directly**: `np.array_equal` on the 800-vector is **True**, max abs diff **0.0**, at both *T* = 600 and *T* = 1200. See `II-28`.
* **§3.3's threshold row** 0.443 → 0.770, and 0.444 against 0.443 at 0.25× with κ falling 0.0250 → 0.0188 — **24.8 %, "a quarter"** ✓.
* **§3.3's periodicity** 0.486 (*P* = 1) and 0.456 (*P* = 20) ✓ from the named command; **0.451 at *P* = 30 and the 0.035 span are TRUE (measured 0.4507, 0.0353 at *T* = 1200) but were NOT in it** — `II-27`.
* **§3.4** — 0.891 / 0.994 / gap **0.103** ✓; top decile 0.100–0.861 against 1.000, clearing 0.90 by **0.039** ✓; ceiling (800−1)/800 = **0.99875** ✓ arithmetic; unopposed Gini 0.994397 ✓.
* **§3.1/§5's test claims** — "asserts agreement within 10 %" ✓ (`rel=0.10`); "two configurations inside a stated band across five seeds" ✓ (two configs, `range(5)`).

### 1.4 · The commit pin, checked rather than trusted

`git log -1 -- src/wealth_tensor/redistribution.py` → **`3b11f23`** ✓ exactly as §7 pins it, and `git show --stat 3b11f23` touches **only** that module and its test file.

**And §7's non-circularity parenthetical is TRUE HERE, which matters because `-75` found the identical sentence FALSE in Paper IV.** Paper II's manuscript was added by **`d655501`**, a different commit which touches no `src/` file at all. `IV-5` does not generalise to Paper II. Paper I carries the same sentence at L568 and was **not** checked — §4, item 4.

---

## §2 · FINDINGS

### `II-27` — §7 promises a command that does not produce two of §3's numbers, and §7 itself names this exact failure mode

§7: *"**Regenerate every number in §3:** `python3 scripts/wt030_report.py`"*. Its periodicity loop is `for P in (1,2,4,10,20,50)`, printing a span of **0.030**.

§3.3 says: *"the minimum is **interior**, 0.451 at *P* = 30 … The whole sweep spans 0.035."* Neither number is in that command's output. Both are **true** — measured today at *T* = 1200, P = 30 → **0.4507**, span → **0.0353** — and both came from a **test's** sweep, not the paper's regeneration command.

**Two things make this worse than a typo.** First, it is self-inflicted and recent: `wealthTensor-74` added both numbers to §3.3 (`wt132`, edit `II-23`) **in the same pass that edited §7 twice**, and its own docstring records that *"the paper's own regeneration command prints the P = 50 row"* — the P = 30 gap was visible at the moment of writing. Second, **§7 names this failure mode in its own prose, four lines above the defect**: *"a single command named for numbers it does not produce is a provenance claim that reads as checked and is not."* That is `-72`'s standing lesson — when a document names a failure mode, grep the document for it — paying out on the document that coined it.

**Repaired by making the promise true, not by weakening the prose.** `P = 30` joins the sweep. `wt135`'s fourth post-condition **runs the patched command and demands the row**: `every  30 periods at r=0.60  Gini=0.451  bounded=True`.

### `II-28` — §3.2's strongest sentence claims more than a near-match and was pinned by a near-match

§3.2: *"the two paths agree **agent by agent** rather than merely on the summary statistics. **The identity is structural, and saying so is stronger than calling it a near-match.**"* The abstract and contribution 3 both carry the same word, *exactly*.

The only committed check, `test_a_flow_levy_is_powerless_when_gains_are_unrealised` — the test file's own docstring calls it **"THE HEADLINE"** — asserted `pytest.approx(stationary_gini(nothing), abs=0.01)` and `top_share > 0.95`. **A near-match on one summary statistic**, which is the precise thing the manuscript says it is being stronger than.

**The claim is true.** Measured: `np.array_equal` on the 800-agent wealth vector → **True**, max abs diff **0.0**, at *T* = 600 and *T* = 1200.

**Repaired in the test, `-74`'s move.** `assert np.array_equal(unrealised["wealth"], nothing["wealth"])` now precedes the approx line. **Guard honesty, both halves verified before the assertion was written** (`-75`(iii)): it **passes** at ρ = 0.00 and **fails** at ρ = 0.10, 0.25 and 1.00. Test count unchanged at 18, so §7's, the abstract's and §1's shared number still holds.

### `II-29` — limitation 5 still says "three" and cites, in the same sentence, the section that says "four"

§5.5: *"the exception is §3.1's **three** Var[log *a*] values, which are quadrature rather than simulation output **(§7)**."*

`wealthTensor-74`'s `II-22` established that E[η⁺] = 0.1073 is a **fourth** closed-form quantity and repaired **§7 in two places**. It missed this third site — the one that *points at* §7. A reader who follows the cross-reference finds the count contradicted by its own source.

### `II-30` — §7's second overclaiming guard is said to be "in the same suite"; the suite it names four lines above does not contain it

§7's bullet: *"`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` … **in the same suite**"*. The nearest antecedent is the previous bullet's *"the **18** tests in `tests/test_redistribution.py`"*. The test is in **`tests/test_excess_demand.py`** (L102). A replicator greps the file §7 names and finds **one of the two** guards §7 promises.

**The manuscript already contains the correct pattern** — §1's contribution 5 says *"in a **companion module** of the same suite"*. Repaired by copying it and naming the module, which is `IV-1`'s repair shape: name the owning object **at the site**.

### `II-31` — THE SOFTEST, and named as such — §7's enumeration of its non-simulation numbers is still one short

§7: *"every measured number is generated by simulation, **save the four closed-form quantities the next bullet names**."* §3.4 states the Gini ceiling **(N−1)/N = 0.99875** (and contribution 4 states the general form). It is printed by **neither** `wt030_report.py` **nor** `wt077_tail_index.py`; it is arithmetic in *N*.

**Why it is soft, stated rather than hidden:** 0.99875 is arguably not a *measured* number at all, so §7's sentence can be read as not reaching it. **Why it is a finding anyway:** neither are the four §7 does list, and §7 lists them — so the category being enumerated is §7's own, and by §7's own usage the count is five. Repaired at both §5 and §7 so the two sections now agree on the same five.

---

## §3 · CLEARED — 22 rows checked and found sound. `M` = measured, `R` = re-run, `A` = argued from the text

| # | claim | how | verdict |
|---|---|---|---|
| C1 | §7's commit pin **3b11f23** is the last commit touching `redistribution.py` | R | ✓ exact |
| C2 | §7's *"a paper cannot cite the commit that adds the paper"* — **`IV-5` does NOT generalise here** | R | ✓ `d655501` added the paper; disjoint from `3b11f23` |
| C3 | §7's **18 tests** in `test_redistribution.py` | R | ✓ 18 passed |
| C4 | §7's *"that count is the one quoted in the abstract and in §1"* | M | ✓ both say 18 |
| C5 | §7 ↔ `wt030_report.py` module pairing | M | ✓ imports it |
| C6 | `wt077_tail_index.py` produces all four quantities §7 pairs with it | R | ✓ to the digit |
| C7 | §3.1's 24 table cells | R | ✓ exact |
| C8 | §3.1's E[η⁺] closed form and value | R | ✓ 0.107269 |
| C9 | §3.1's −4.4 / −4.9 / −6.8 % residuals **and** contribution 2's "within 7 % at every rate tabulated" — checked at **all seven** flow rates, not the three quoted | M | ✓ 4.4–6.8 %, monotone |
| C10 | §3.1's three Var[log *a*] | R | ✓ exact |
| C11 | §3.1's κ = *r* exactly on a stock base at zero exemption | R | ✓ `rel=1e-9` in the suite |
| C12 | §3.1's matched-κ pair 0.222 against 0.125 | R | ✓ |
| C13 | §3.1's nested frontiers, stock 0.000 < flow 0.125 | R | ✓ |
| C14 | §3.2's ρ table, three rows | R | ✓ |
| C15 | §3.2's *"top decile 1.000 in both"* | M | ✓ 0.999987 both |
| C16 | §3.3's threshold sweep endpoints 0.443 → 0.770 | R | ✓ |
| C17 | §3.3's *"reducing κ by a quarter"* at 0.25× | M | ✓ 24.8 % |
| C18 | §3.3's *P* = 1 / 20 / 50 endpoints | R | ✓ |
| C19 | §3.4's 0.103 gap and 0.039 headroom | M | ✓ |
| C20 | §3.4's ceiling 0.99875 = (800−1)/800 | M | ✓ (its *provenance* is `II-31`, its value is right) |
| C21 | §3.1/§5's two test-behaviour claims ("within 10 %", "five seeds") | R | ✓ both |
| C22 | **`-75`(i)'s reader-only check: every §-reference read at its site for a WRONG-document resolution** — all 41, including both `§4.1`s (Benhabib's, attributed at both), `§4` (`REFERENCE-POLICY`'s, named at the site), and §7's `§3.2` (Paper II's own, correct) | M | ✓ **no collisions. Paper II is clean on the half no sweep can reach.** |

---

## §4 · NOT CHECKED — the honest list, and what it will cost `-77`

`-75`(iv)'s rule was applied: an item closeable in four minutes was **closed**, not written down. **Four items were drafted here and closed at drafting** — the commit-pin verification (became `C1`), the `IV-5` generalisation question (became `C2`), the seven-rate residual sweep (became `C9`), and the ρ = 0 identity itself (became `II-28`). Five remain.

1. **`wt077_tail_index.py` is covered by no pin.** §7 pins `redistribution.py`; `wt077` imports nothing from `src/`, so the four closed-form quantities have **no pinned provenance** beyond "head of repository at posting". §7 discloses that the pin excludes the two scripts, so this is honest as written — but a replicator wanting the quadrature values reproducibly needs a **second per-file pin**. Deliberately not invented here: it is a policy question, and the same booby trap as `IV-4b` applies (adding a pin means the commit that adds it moves it).
2. **The nine uncited reference entries.** `wt133` sweep 2. Card `1217568192511533`. Untouched.
3. **Bouchaud & Mézard's two quotations in §3.1 were not read against the source.** The entry discloses they come from the arXiv preprint and may not be verbatim in the article of record. This is `REFERENCE-POLICY`'s eighth pass, card `1217556161163494` — four sessions deferred, now five.
4. **Paper I carries §7's non-circularity sentence verbatim at L568 and was not checked.** `-75` found it false in Paper IV; `C2` finds it true in Paper II; **Paper I is the untested third instance**, and it is one `git log --diff-filter=A` away. Paper I is not in `definition_of_done`, which is why it is here rather than done.
5. **Paper II's front-matter stamp is wrong INSIDE the document.** *"Version 0.2, 2026-08-11"*, while its own References note dates a re-verification **2026-08-17**, and five edits landed 2026-08-18. This is card `1217568297674954`'s **sixth data point and its sharpest**: unlike Paper IV, the contradiction is visible to a reader **without leaving the page**. Not repaired, because the card asks Jason for the rule and there is not one.

---

## §5 · WHAT THIS PASS SAYS ABOUT THE METHOD

Paper II's counter now reads **9 → 2 → 4 → 3 → 4 → 5**, and `-75`'s process finding gets its **third** data point, in the strongest available form: this pass brought exactly one new instrument, and **two of its five findings came from that instrument alone** — `II-27` from running the §7 command and diffing its output against §3, `II-30` from grepping the file §7 names. The three found by reading (`II-28`, `II-29`, `II-31`) were all available to the five previous passes and none of them saw them.

The pair of consecutive zero-finding passes the definition of done requires **has still never been attempted with a frozen instrument set.** That is now a measured claim about the method, not an impression.

