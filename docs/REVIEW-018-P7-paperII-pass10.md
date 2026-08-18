---
new_instrument: none
instrument_name: "— (none. All five axes A1–A5 were inherited; every one had already been pointed at Paper II, which docs/p7-passes.tsv recorded as 5 of 5 before this pass began. A6, the docstring axis, remained parked as ordered. The SECOND half of the frozen pair.)"
findings_from_new_instrument: 0 of 2
residue_of_previous_pass: 0 of 2
# FALSIFY THIS ROW, THREE WAYS.
#   1. `none`:    git log --diff-filter=A --format='%h %ad' --date=short -- scripts/wt139_paperII_p7pass10.py
#                 wt139 is a PATCH script, not an instrument. If a new way of LOOKING was
#                 invented here, this row is wrong. Check §1: every axis is cited to the
#                 earlier session that built it.
#   2. `residue`: git blame the two repaired sites at the parent commit. II-35 → 2b3e24b5
#                 (2026-08-17); II-36 → 3b11f236 (2026-08-05). -77's commit is 6b0655b
#                 (2026-08-18). If either blames to -77, this row is wrong.
#   3. the count: scripts/wt139_paperII_p7pass10.py carries 18 post-conditions. Run it.
# Ledger of all eight passes: docs/p7-passes.tsv
---

# REVIEW-018 · Paper II's EIGHTH independent `P7` read — the second half of the frozen pair

**Session:** `wealthTensor-78` · **Date:** 2026-08-18 · **Manuscript:** `docs/papers/paper-II-redistribution/paper-II.md`, **561 lines read end to end** (565 after the patch)
**Patch of record:** `scripts/wt139_paperII_p7pass10.py` — 1 manuscript edit, 1 test edit, **18 post-conditions**
**Result:** **two findings, two repairs, zero carded.** Paper II's counter goes 9 → 2 → 4 → 3 → 4 → 5 → 3 → **2**.

**IT IS NOT A ZERO — AND THE RESIDUE COLUMN SAYS THE REASON IS NOT `-77`'s EITHER.**
`-77` proposed that a repair pass creates the next pass's findings, and made `-78` the
experiment by inheriting four manuscript edits and one test edit into a frozen instrument set.
**Neither finding here touches text `-77` wrote.** One site dates to `2026-08-17`; the other to
**`3b11f23` — `2026-08-05`, the very commit §7 pins, and it survived all eight passes.**

So the count is not explained by new instruments (`-77` showed that) and it is not explained by
repair residue (this pass shows that). §5 argues the remaining explanation, and it is the one
that makes a zero **reachable** rather than structural.

---

## 1 · The five axes, run before a word of prose

| axis | what was run | measured output | findings |
|---|---|---|---|
| `A1` | `scripts/wt130_quantifier_sweep.py --paper II` (RC 0) — built at `-72` | **161 quantifier tokens on 123 of 561 lines**; read forward from every flagged line during the end-to-end read | 0 |
| `A2` | grep Paper II for the failure modes it names in its own prose — originates `-72` | **8 named failure modes** extracted and turned back on the paper (§2.3 "accommodates any observation"; §3.4 "hard ceiling"; §4 "free parameter wearing different clothing"; §4 "it looked like a convergence check"; §7 "a command named for numbers it does not produce"; §7 "nothing in the repository was watching"; §7 "checkable rather than asserted"; §5.5 "the third decimal is not defended") | 0 directly; **the §4 lens is what made `II-36` legible once `A5` had opened the file** |
| `A3` | `scripts/wt133_crossref_sweep.py` (**RC 0**) — built at `-74` | Paper II: **45 §N.M references, 12 distinct, 0 unresolved**; sweep 2: 16 entries, 7 cited, **9 not** (carded `1217568192511533`, deliberately untouched) | 0 |
| `A4` | `wt030_report.py` (RC 0) **and** `wt077_tail_index.py` (RC 0) — originates `-74` | **all 39 tabulated §3 values reproduce**; then `-77`'s *other* question — is there a number in §3 neither command produces? | **`II-35`** |
| `A5` | every named artefact greped against its pairing, **enumerated from the whole document**, and every named command run — originates `-75`, first on Paper II at `-76` | **20 distinct named artefacts**, all resolve; 5 named files exist; 3 named test functions exist at their named sites; 3 named commands run | **`II-36`** |

`A5`'s enumeration was **re-derived from the whole document**, per `-77(iii)`, rather than
inherited: 20 backticked artefacts across §1, §2.3, §3.2, §4, §5.5, §7 and the References note,
plus one **non-backticked** artefact `-76` and `-77`'s greps would both have missed — the commit
SHA `3b11f23` in §7, which is bolded rather than fenced.

---

## 2 · The two findings

### `II-35` · §3.1's three κ residuals are computed from the table's four-decimal display, not from κ

§3.1 stated: *"The simulated κ runs **4–7 % below** that form at every rate tabulated, and the
residual is monotone in the rate — **−4.4 %, −4.9 %, −6.8 %** at *r* = 1.000, 0.100, 0.025."*

**Measured at full precision at the reported horizon `T` = 1200:**

| *r* | κ (unrounded) | *r*·E[η⁺] | true residual | paper said | from the 4-dp display |
|---|---|---|---|---|---|
| 1.000 | 0.102609046638 | 0.10726894 | **−4.344 %** | −4.4 % | (0.1026−…)/… = **−4.352 %** |
| 0.100 | 0.010236878093 | 0.01072689 | **−4.568 %** | −4.9 % | (0.0102−…)/… = **−4.912 %** |
| 0.025 | 0.002527559116 | 0.00268172 | **−5.749 %** | −6.8 % | (0.0025−…)/… = **−6.777 %** |

**All three reproduce exactly from the rounded display and two are wrong by 0.33 and 1.05
percentage points** — an order of magnitude outside any rounding of the reported figures. The
mechanism is named and checkable: at *r* = 0.025 the display quantum (±0.00005) is **±2 % of κ
itself**, wider than the spread the sentence reports.

The **−6.8 % is real** — it belongs to *r* = 0.010, the sweep's lowest rate and **a row that is
not in this table**. So the headline range *"4–7 %"* survives across the full sweep and was
**scoped rather than deleted**; what was wrong was attaching the endpoint to a tabulated rate.
*"Monotone in the rate"* was made exact in the same edit: the residual is **flat** from
*r* = 1.000 to *r* = 0.500 (−4.344 %, −4.338 %) and widens monotonically below it.

**§1's independent claim — *"to within 7 % at every rate tabulated"* — was left untouched, and
that is deliberate.** It is TRUE at full precision (max 6.831 % at *r* = 0.010) and a post-condition
asserts it is still present exactly once. Per `-77(ii)` the enumeration is the size of the repair:
the distinguishing phrase was greped across whitespace-flattened text before the first edit, and
the count came back **one** site wrong, not two.

**RESIDUE: NO.** `git blame` → `2b3e24b5`, 2026-08-17 — a session before `-77`.

### `II-36` · the guard for the paper's only named closed-form scalar pins the wrong constant

`tests/test_redistribution.py:195–196`, unchanged since **`3b11f23` (2026-08-05)** — the commit §7 pins:

```
ceiling = mu * Phi + sigma * phi                    # 0.10734...
assert ceiling == pytest.approx(0.10734, abs=1e-4)
```

The closed form's exact value is **0.1072689396**. The reference constant is wrong in the
**fourth decimal**; the guard survives on **71.1 %** of its tolerance budget. Tightening `abs` to
`1e-5` — the obvious *"make this stricter"* move — turns the suite **red against a correct
implementation**, and the inline comment states, in the repository, a wrong value for a scalar
the manuscript prints in two places.

This is Paper II's **own §4 failure mode**, inside the guard that exists to prevent it: *"it
survived initial review because it looked like a convergence check and convergence checks look
like that."* A wrong constant inside a passing assertion looks exactly like a right one.

Repaired to `approx(0.1072689396, abs=1e-7)` — **1 000× tighter** — plus a second assertion that
`round(ceiling, 4) == 0.1073`, which is precisely what §3.1 and §7 print. The manuscript's
*"asserts agreement within 10 %"* sentence and its `rel=0.10` assertion are untouched and
post-conditioned. **Test count held at 18** (both edits are inside an existing body).

**RESIDUE: NO.** `git blame` → `3b11f236`, 2026-08-05. **It predates every P7 pass of this paper.**

---

## 3 · Cleared — 17 rows, and four were live candidates that died on contact

| # | candidate | verdict |
|---|---|---|
| `D1` | **§7's pin `3b11f23` is true but unwatched** — the paper's own diagnosis of the *old* pin was *"nothing in the repository was watching"* | **DIED ON CONTACT.** `tests/test_pin001_code_state.py` imports `LATEST_TOUCH` from `scripts/wt099_edits_pin001.py`, which carries `"src/wealth_tensor/redistribution.py": "3b11f23"`, and `test_each_pinned_path_was_last_touched_by_the_sha_the_paper_discloses` goes red the day the module moves. Verified exact today. |
| `D2` | **the top-decile share also has a hard ceiling (1.000)** and §3.4's own rule condemns saturating statistics as convergence criteria | **DIED ON CONTACT.** The rule is about *drift* tests; the criterion uses top-decile as a *level* test (below 0.90). The paper says so itself: *"it is the second condition that does all of the separating."* |
| `D3` | §3.1 defends **6 × 10⁻⁶** on Var[log *a*] while §5.5 says *"the third decimal is not defended"* | **DIED ON CONTACT.** Var[log *a*] is **quadrature, not simulation** — §5.5 excepts it by name among the five closed-form quantities. `-77`'s enumeration is what made this a 30-second check. |
| `D4` | §3.3 rests *"costs nothing measurable"* on **0.444 against 0.443** — a third-decimal comparison | **CLEARED.** The claim is that the difference is *not* measurable, which is the safe direction of an undefended decimal. |
| `D5` | **`wt077`'s κ column disagrees with `wt030`'s** at every flow rate (0.10216 vs 0.1026 at *r* = 1) | **CLEARED — different objects.** `wt077`'s κ is the *analytic* *r*·E[η⁺]/(1+μ); `wt030`'s is simulated. §3.1 cites `wt030`'s. Reproduced to 6 dp. |
| `D6` | §1's *"to within 7 % at every rate tabulated"* | **CLEARED and deliberately not edited** — true at full precision (max 6.831 %). |
| `D7` | a **third undisclosed symbol collision** beyond the two the paper discloses (*a*, μ) | **CLEARED.** Swept η, ρ, σ, θ, *P*, *N*, *T*, κ, *r*, Φ, φ — no third collision. |
| `D8` | **0.99875** printed by a named command, which would falsify `-77`'s `II-32` repair | **CLEARED.** Zero occurrences in either command's stdout, re-verified today. `II-32`'s repair holds at all four sites. |
| `D9` | the **18**-test count drifted | **CLEARED.** `test_paper_test_counts_are_derived.py` asserts live == 18; live count is 18 before and after `wt139`. |
| `D10` | §5.5's horizon promise — *"at the reported `T` = 1200 as well as at the suite's `T` = 600"* | **CLEARED.** `test_the_result_is_not_a_lucky_seed` runs `for horizon in (T, 1200)` with `T = 600`. `-77`'s `II-34` repair verified surviving. |
| `D11` | §3.1's *"monotone in the rate"* is **false** — the residual is flat from *r* = 1.000 to 0.500 | **LIVE, but folded into `II-35` rather than counted separately.** The deviation is 0.006 pp; counting it as a third finding would have been manufacturing. It is repaired in the same edit. |
| `D12` | the 5 named files do not exist | **CLEARED** — all 5 exist. |
| `D13` | the 3 named test functions do not exist at their named sites | **CLEARED** — all 3 exist. |
| `D14` | §3's 39 tabulated values do not reproduce | **CLEARED** — all 39 reproduce from `wt030`/`wt077`. |
| `D15` | §3.4's derived margins (gap 0.103, *"0.039 to spare"*) | **CLEARED** — exact arithmetic on `wt030`'s printed values (0.994−0.891; 0.90−0.861). |
| `D16` | §3.3's *"spans 0.035"* and *"reducing κ by a quarter"* | **CLEARED** — 0.486−0.451 = 0.035; 0.0250→0.0188 = −24.8 %. |
| `D17` | the frontier claim **stock 0.000 < flow 0.125** | **CLEARED** — `wt030`'s REACHABLE FRONTIER block, exact. |

---

## 4 · Not checked — seven items, named so the next pass starts above zero

1. **`A6`, the docstring axis — STILL PARKED**, as ordered. `tests/test_redistribution.py` now carries **twenty-one** unasserted prose claims (`wt139` added one). Spend it on Paper III's three empty cells, or on Paper II after the pair resolves.
2. **The nine uncited reference entries** — card `1217568192511533`. `wt133` sweep 2 does **not** set the exit code; RC 0 does not cover them.
3. **`II-25`, the version stamp** — card `1217568297674954`, now the **EIGHTH** data point: two more edits landed 2026-08-18 under a stamp reading *"Version 0.2, 2026-08-11"*.
4. **The general form of `II-34`** — 16 of 18 tests reach the model through `econ()` at `T` = 600 while every reported figure is at `T` = 1200. **This pass produced new evidence that the lead is real:** at *r* = 1.000 the κ residual is **−4.042 % at `T` = 600 against −4.344 % at `T` = 1200**, a difference larger than the precision §3.1 reports. Still a question, not a finding; chasing it inside a frozen pass buys a third finding with a change of scope.
5. **Whether §3.1's closed form should be *r*·E[η⁺]/(1+μ).** `wt077` **already computes and prints exactly that**, labelled `predicted`, and it matches the simulation to **0.44 %** where the paper's cruder form is off by 4–7 %. Not a defect — the paper discloses the convention in prose — but a possible strengthening, and Jason-sized because it changes a stated contribution.
6. **Papers I, III and IV** — out of scope.
7. **Bibliographic details** of the entries not marked ✓ — deferred to submission per `PREPRINT-CHECKLIST`.

---

## 5 · The method result — and it is the second half of the experiment

`-77` ran the control and returned three. It offered a mechanism for why the counter will not
decay: **a repair pass creates surface.** `-78` was built to test it: the same five axes, nothing
invented, four manuscript edits and one test edit inherited, and a per-finding residue column.

**The answer is 0 of 2.** Neither finding touches text `-77` wrote. `II-35` blames to
`2b3e24b5` (2026-08-17); `II-36` blames to **`3b11f236` (2026-08-05)** — the commit §7 pins,
which means that defect was present for **every one of Paper II's eight independent reads** and
was missed by all of them, including the two that ran `A5` at the very file it lives in.

So the ledger now has **three** rows that cut against the standing anecdote, and they cut in
different directions:

* `-71` — no new axis, four findings. The anecdote's first counterexample.
* `-77` — no new axis, three findings, **two of them residue.** Mechanism proposed.
* `-78` — no new axis, two findings, **zero of them residue.** Mechanism not supported here.

**What is left is neither breadth of toolkit nor residue. It is DEPTH OF APPLICATION.** `A5`'s
site list has included `tests/test_redistribution.py` at `-76`, `-77` and `-78`. Three passes
opened that file; `-77` even edited a test inside it. The wrong constant sat on line 196 the
whole time, one line below a comment restating it. The axis was pointed at the right file and
**nobody read the arithmetic.**

**This is the reading that makes a zero REACHABLE.** `-77`'s mechanism, if it generalised, made
two consecutive zeros unreachable by construction — the first zero would need a predecessor that
changed nothing, which no productive pass can be. Depth-of-application has no such property: an
axis can be exhausted at its own sites, and once it is, it stays exhausted. The counter is not
measuring an artefact of the method. **It is measuring how much of each axis has actually been
spent** — and `-78` spent `A5` deeper than any previous pass by re-deriving its enumeration from
the whole document and then *reading the values*, not merely checking that the artefacts resolve.

**The falsifier is cheap and `-79` is holding it.** If depth-of-application is the mechanism, a
ninth read that re-runs the same five axes at the same depth should find **materially fewer than
two** — the sites `-78` exhausted are exhausted. If it finds two or more from sites `-78` already
opened, depth is not the mechanism either, and the honest conclusion is that Paper II's counter
is measuring the reviewers rather than the paper.

**Both of Jason's rulings are now better posed than they were this morning**, and `-78` recommends
neither, only states them precisely:

1. **Does a zero-finding pass require a frozen instrument set?** Two frozen passes are now on the
   board (3, then 2). The freeze did not produce a zero, but it did produce a **decaying** count
   for the first time in the project's history.
2. **Does the DoD's bar change?** `-77`'s reason for changing it — residue makes consecutive zeros
   structurally unreachable — is **not supported by this pass**. On the depth reading the existing
   bar (*two consecutive zero-finding passes*) is reachable and is measuring the right thing.
   **`-78`'s answer to the question `-77` raised is therefore: leave the bar alone.** That is a
   recommendation on a methodological question, not on a scope question, and it is Jason's to
   overrule.

---

## 6 · Coverage claim

Paper II was read **end to end, all 561 lines**, after all five axes had been run and their counts
recorded. Every §3 number was checked against a command that produces it, at the reported horizon,
**unrounded**. Every named artefact in the whole document — not only §7's — was enumerated,
resolved and, where it was a command, run. Both findings were **measured before they were
asserted**, and both repairs carry post-conditions that fail loudly if a future session undoes them.

**What this pass does NOT claim:** it did not run `A6`; it did not adjudicate the nine uncited
references; it did not chase the `T` = 600 / `T` = 1200 question in §4 item 4; and it read no
other manuscript. Those four are named in §4 with what is known about each, so `-79` starts at
this pass's high-water mark rather than at zero.
