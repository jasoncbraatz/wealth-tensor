---
new_instrument: inherited-first-application
instrument_name: "A2 grep-the-document-for-the-failure-mode-it-names (originates -72, first on paper-III) · A4 run-the-manuscript's-own-regeneration-commands (originates -74, first on paper-III) · A5 grep-each-module-against-its-paired-script (originates -75, first on paper-III). THREE CELLS FILLED IN ONE PASS. A1 and A3 were already Paper III's, from -73. The axis matrix reaches 15 of 15."
findings_from_new_instrument: 8 of 9
residue_of_previous_pass: 0 of 9
shape_promise_about_artefact: 5 of 9
shape_deferral_with_empty_target: 2 of 9
shape_neither: 2 of 9
manuscript_edits_required: 7 of 9
# FALSIFY THIS ROW, FIVE WAYS.
#   1. `inherited-first-application`: the three axes are cited to the sessions that built them
#      in docs/p7-passes.tsv. If any of A2/A4/A5 was invented HERE, this row is wrong. And if
#      the matrix already showed one of them filled for paper-III, the whole at-bat was
#      misassigned — open the matrix at the -79 revision and check the three EMPTY cells.
#   2. `8 of 9`:  §2 credits each finding to the axis that produced it. Only III-11 came from an
#      inherited cell (A1's read-forward). If two or more trace to A1 or A3, this row is wrong.
#   3. `0 of 9`:  git blame every site at the parent commit. NOT ONE blames to -79, which
#      touched Paper II only. The residue mechanism is not even applicable across manuscripts,
#      and the row says so rather than claiming a result it cannot have.
#   4. the shapes: §2's shape column is the -79 experiment. Re-read the nine findings against
#      -79(i) and -79(ii) as stated in REVIEW-019 §6. If fewer than half carry one, the shapes
#      were Paper II's texture and this row is wrong.
#   5. the count: scripts/wt143_paperIII_p7pass2.py carries its post-conditions. Run it.
# Ledger of all ten passes: docs/p7-passes.tsv
---

# REVIEW-020 · Paper III's SECOND independent `P7` read — the three empty cells, filled

**Session:** `wealthTensor-80` · **Date:** 2026-08-18 · **Manuscript:** `docs/papers/paper-III-dual-tensor/paper-III.md`, **2,694 lines read end to end** (2,723 after repair)
**Patch of record:** `scripts/wt143_paperIII_p7pass2.py`
**Result:** **nine findings, nine repairs, zero carded.** Paper III's counter goes 7 → **9**.

**THE COUNTER WENT UP, AND THAT IS THE MATRIX BEING RIGHT RATHER THAN THE PAPER BEING WORSE.**
`docs/p7-passes.tsv` said it in one line before this pass began: *the counters cannot decay
while cells are still empty.* Paper III was at **2 of 5** and its counter of 7 was measuring the
toolkit. Three axes had never been pointed at this manuscript. Pointing them at it returned
**eight of the nine findings below.** A pass that filled three cells and found fewer than a pass
that filled none would have been the surprising result; this is the expected one, and it is the
first time the project has had the expected one.

**AND THE `-79` EXPERIMENT RETURNS A CLEAN YES.** `-79` found two defects of a shape this
project had never named — sentences ABOUT artefacts rather than defects IN them — and asked
whether they were Paper II's own texture or something general. **Seven of nine carry one of the
two shapes** (five promise-about-artefact, two deferral-with-empty-target), on a different
manuscript, at a different scale, found by three axes `-79` never ran. The shapes generalise.

---

## 0 · What is NOT claimed here

Nine findings on a manuscript at 2 of 5 cells is not evidence that Paper III is worse than
Paper II. It is not comparable to Paper II's 2, because Paper II is at 5 of 5 and has had nine
reads. **A count is only comparable across passes at the same matrix coverage**, and no two
passes in this project's history have had that. The row this pass adds is a data point about
coverage, not about quality, and §5 says what it does and does not settle.

No finding below required re-running the severe test's science. Every one is checkable in under
a minute by a reader with the repository, and each carries the command that kills it.

---

## 1 · THE FIVE AXES, RUN BEFORE A WORD OF PROSE

| axis | what was run | count | findings |
|---|---|---|---|
| **A1** quantifier read-forward | `python3 scripts/wt130_quantifier_sweep.py paper-III` | **870 tokens on 673 lines**, of 2,694 | III-11 |
| **A2** grep the document for the failure mode it names — **NEW CELL** | eight named failure modes derived from the prose (§3.2's *a test that cannot fail is not a test*; §3.2's *a statistic that answers two questions answers neither*; §7's *a guard that could not fail passing silently*; §11's *a registration cannot be amended by stealth*; §5.3's *a hypothesis that requires one on the same data is a hypothesis being fitted*; §11's *differential attrition … manufacturing the reported null*; §A.2.4's *a quantity that forbids nothing*; the References' *a reference kept for the look of the list*), each turned back on the paper | **8 modes × the sections that could commit them** | III-17 |
| **A3** cross-references as quantifiers | `python3 scripts/wt133_crossref_sweep.py` | **222 §N.M refs, 36 distinct, 0 unresolved · 49 entries, 49 cited, 11 explicit "cited in §N.M" claims, 0 flagged** | none |
| **A4** run the manuscript's own regeneration commands — **NEW CELL** | all four commands §11 names, **and both questions**: do the values match, *and* is there a number the paper reports that no named command produces? | **4 commands · 39 tabulated §3/§A.2 values matched · 6 §3 values produced by nothing** | III-12, III-13, III-14 |
| **A5** enumerate every named artefact and read what it says — **NEW CELL** | **45 named artefacts** from the whole document, backticked and not (25 backticked paths/commands, 6 registrations, 3 test-function names, 3 module symbols, plus `METHOD-001`, `REVIEW-001`, `LEDGER.md`, `TIER_TAGS`, `wt091`, two SHA-256 digests, a World Bank series code and a repository URL); every one resolved, every named command run, and `-79`'s two questions asked at each | **45 enumerated · 44 resolve · 1 resolves only off the path given** | III-9, III-10, III-15, III-16 |

**A4's second question is what paid, and it is `-79`'s II-37 arriving on a different paper.**
§11 opens *"Every simulation result in §A.2 and §§2–3 is produced by open code."* Six §3 figures
were produced by none: §3.2's three full-path volatility ratios, §3.1's two off-grid lags, and
D(0) to four decimals. All six are correct. None was printed.

---

## 2 · THE FINDINGS

`shape` is the `-79` column: **P** = promise-about-artefact · **D** = deferral-with-empty-target
· **—** = neither.

| # | shape | site | falsifier |
|---|---|---|---|
| III-9 | **D** | §9 lim 9 + §5.4 | `RESULT-REG-008` §2.2 |
| III-10 | **P** | References key | count the ⧗ |
| III-11 | **—** | §4.9 | §4.10's own table |
| III-12 | **P** | §11 + `wt027_report.py` | run it, count the blocks |
| III-13 | **P** | §11 | run it, compare to §5.3 |
| III-14 | **—** | §5.4 | count CIKs in the pinned file |
| III-15 | **P** | `wt002_lambda_report.py` | count header names vs row values |
| III-16 | **D** | `wt002_lambda_report.py` | grep Paper III for a §3.3 heading |
| III-17 | **P** | §11 | diff `test_lag.py` across the pin |

### III-9 · A stated zero that is a one, deferred to a section that does not carry the number. **[D]**

§9's ninth limitation read *"the disclosure does not once, in **644** firm-years, tie the
standard's own internal trigger to the unit it fired in, **and §5.4 says that where the numbers
are**."* §5.4 read *"**no firm-year in the window** writes a sentence naming a reporting unit, a
trigger, and any of the standard's own (f)-family language."*

`RESULT-REG-008` records the opposite, twice and in bold: **"One firm-year in 644 satisfies the
conjunction"** (§1, P2's adjudication), and §2.2 — *"Zero of 281 JOINT firm-years **and one of
363 GOODWILL-ONLY firm-years** contain a single sentence carrying both a registered trigger
phrase, a named reporting unit, and any (f)-family term."* 281 + 363 = 644. The zero is real and
it belongs to **281**, the both-charges arm — which is exactly what §7's own ledger row says
(*"**0 of 281** joint firm-years"*). Two of the paper's three statements of one result were
right; the third generalised the zero to a denominator that contains a hit.

**And the deferral is empty on its own terms.** `644` appeared **once in the entire manuscript**,
in §9, pointing at a §5.4 that carried 1,833 and 1,925 and never 644. `-79(ii)` costs one grep
and found this in one.

The mirror of REG-008's own warning is what makes it worth nine lines rather than one: P2's
adjudication says *"an empty cell reported as 'did not fire' would be a phantom tag at section
scale (`METHOD-001`)."* The manuscript committed the reflection of that — a one-hit cell reported
as empty, at section scale.

**Repaired** in both sentences, to the true denominators, with `RESULT-REG-008` §2.2 named at the
site. `tests/test_restatement_reach.py` now declares 281 at §5.4, §7 and §9 rather than §7 alone,
so the figure cannot drift back to a single unopposed site. `docs/crossref-dismissed.tsv` gains
the row adjudicating the new `§2.2` as REG-008's own.
**Falsifier:** `grep -n "One firm-year in 644" docs/preregistration/RESULT-REG-008.md`.

### III-10 · The reference list uses a fourth mark the key does not define. **[P]**

The References open with a key defining exactly three: **✓**, **✓✎**, **✓⧗**. The closing note
repeats the enumeration — *"The per-entry findings live in the ✓, ✓✎ and ✓⧗ notes above."*

**Three entries carry a bare ⧗**: Fisher and McGowan (1983), Kay (1976), Nerlove (1958). It is
a coherent and consistently-applied fourth mark — all three notes say *"Not read"* and *"the
record is verified"* — and a reader hitting it has nothing to look it up against. Two further
entries (Lanczos 1956, Marshall and Proschan 1972) carry **no mark**, each explaining why in its
own note, so those are self-accounting; the key still does not mention the case.

This is `-79`'s II-38 family on a different bibliography, and the sibling paper is the contrast
that makes it a defect rather than a style: Paper II's References note enumerates its unmarked
entries by count. Paper III's does not.

**Repaired** by defining **⧗** in the key, stating that three entries carry it and two carry
none, and extending the closing note's enumeration.
**Falsifier:** the key names four marks and the list uses four.

### III-11 · A fraction that is not the fraction. **[—]**

§4.9: *"α_eff runs from **0.437** per year at a forty-year life to **0.476** at a three-year one
— **a ninth of itself** across the asserted rectangle."*

§4.10's own table gives the unrounded pair: **0.4368** and **0.4758**. The move is
(0.4758 − 0.4368)/0.4368 = **8.93 %**. A ninth is 11.11 %. Rounding cannot reach it from either
direction — against the larger value it is 8.19 %. The nearest unit fraction is an **eleventh**.

Surfaced by A1's read-forward: the line carries three quantifier tokens and the sweep put a
reader on it. The figures are right; the descriptor summarising them is not.

**Repaired** to *"nine per cent of itself … nearer an eleventh than the ninth an earlier revision
of this sentence claimed."* `scripts/wt101_edits_term001.py`'s TERM-001 anchor follows the
corrected span — `S3_OLD` is untouched, so the wrong *adjective* still cannot return, which is
what TERM-001 exists to guard.
**Falsifier:** `(0.4758 - 0.4368) / 0.4368`.

### III-12 · "its three tables" of a command that printed four, and six §3 figures no command produced. **[P]**

Two limbs, one bullet, one repair.

**(a) The count.** §11: *"`python3 scripts/wt027_report.py` — its **three tables** are §3.1's two
and §3.2's."* The command prints **four** (A, B, C and D), and D is §A.2.4's sawtooth — which is
why the same bullet claims §A.2.4 at all. The module's own docstring said *"Three tables"* too,
so the manuscript and the artefact were wrong in the same words.

**(b) The promise.** §11's opening sentence promises *every* simulation result in §A.2 and
§§2–3. Six §3 figures were printed by nothing:

| figure | §3 says | now printed |
|---|---|---|
| full-path reported/physical volatility, φ = 0.5 / 0.2 / 0.0 | 1.56 · 2.71 · 3.27 | **1.56 · 2.71 · 3.27** |
| recognition lag at φ = 0.9 and φ = 0.1 | 1 and 24 | **1 and 24** |
| D(0) to four decimals | 1998.99 | **1998.9895** |

`variance_suppression` measures smoothing **between** recognition events by design; §3.2's prose
quotes the **full-path** ratio, which existed nowhere in the repository — not in `src/`, not in
`scripts/`, not in `tests/`. Table A sweeps the five φ §3.1 tabulates, so §3.1's sigmoidal
readings at 0.9 and 0.1 had no producer either.

**Repaired on II-27/II-37's precedent — make the promise true rather than narrow the sentence.**
`wt027_report.py` gains `full_path_volatility_ratio()`, a fifth column on table B, and a block
A′ carrying §3.1's prose-only figures; the bullet now says five blocks and names them. **No
extra simulation is bought**: A′ is the only new run and B's column is computed from the run
table B already makes. Table D is relabelled `lambda` — §A.2.4 opens by distinguishing λ = C/E
from the dimensional Λ = η·C/E, and the command regenerating it called λ "Lambda".
**Falsifier:** `python3 scripts/wt027_report.py | grep -c "^[A-E]"`, and the three rows above.

### III-13 · "Regenerate §5" reaches neither §5.3's sample nor the committed one. **[P]**

§11: *"**Regenerate §5:** `python3 scripts/wt026_severe_test.py --universe pilot --onset peak`
and `--universe replication --onset peak`."* Both were run.

| | events / firms | JT z, pilot | JT z, replication |
|---|---|---|---|
| §5.3, as published | 688 / 311 | **−0.290** | **−0.095** |
| the committed `data/pre-002-events.json` | 695 / 313 | **−0.223** | **−0.083** |
| the named command, run 2026-08-18 | 696 / 313 | **−0.190** | **+0.011** |

The command re-pulls `companyfacts`, which serves each firm's *latest* view of its own history —
§11 explains that six bullets later, about the data pin, and never about the regeneration bullet.
The script has **no flag** that consumes the pinned files: `--universe`, `--onset`, `--signal`,
`--alpha`, `--out`, and nothing else. So a replicator who follows the bullet gets neither §5.3's
sample nor the one the repository commits — and on today's pull the replication statistic has
**crossed zero**, against §5.3's *"Both z-statistics are negative, meaning the point estimates ran
opposite to the predicted ordering in both universes."*

**Nothing in the repository re-derives §5.3's figures from committed data.** The 688-event pull
survives as `docs/preregistration/RESULT-002-pilot-run.log` and `RESULT-002-replication-run.log`
— run logs, which are a record and not a re-analysis.

**Repaired in the manuscript**, because the alternative is a science change: the bullet now says
the command reproduces the *instrument* and not the sample, prints the pinned sample's own two
statistics, names the run logs as §5.3's record, and states that no command re-derives §5.3. A
`--events` path into `wt026_severe_test.py` is the fix that would make the bullet's original
promise true; it is **teed up in §4, not carded**, because it changes what a registered
instrument reads and that is a decision rather than a repair.
**Falsifier:** run either command and compare its header line to §5.3's.

### III-14 · The committed rebuild carries 313 firms; §5.4 said 307. **[—]**

§5.4: *"**The sample rebuilt to within one per cent**, which is itself worth one line. …
Rebuilt: **695 events across 307 firms** against 688 across 311."*

`data/pre-002-events.json` — the file §11 pins, whose SHA-256 the manuscript prints and which
verifies — holds 247 pilot events across **122** distinct CIKs and 448 replication events across
**191**. 695 events ✓. **313 firms.**

**The wrong number contradicts the sentence it was supporting.** 313 against 311 is +0.64 %,
inside the one per cent the sentence asserts. 307 against 311 is −1.29 %, outside it. The claim
was true and its own evidence said otherwise.

While there: *"three of four tier counts identical"* holds for the **pilot** (21/34/34/158
against 21/34/34/155) and not for the replication (34/102/47/265 against 34/102/46/262, two of
four). The sentence named no universe. Repaired to say the pilot; §7's row repeats the phrase
without a universe and is left alone — see §4, item 7.
**Falsifier:** `python3 -c "import json;d=json.load(open('data/pre-002-events.json'));print(sum(len({e['cik'] for e in u['events']}) for u in d['universes'].values()))"` → 313.

### III-15 · The §A.2.3 regeneration command's header is two columns short. **[P]**

`scripts/wt002_lambda_report.py` — named twice by the manuscript, once in §11 and once in
§A.2.3's own parenthesis — prints a nine-name header over eleven values per row. The two
unlabelled trailing columns are `mean_coupling_ratio` and `min_coupling_ratio`: precisely the
quantities §A.2.3's table reports in its row *"mean / min / terminal coupling ratio."* A reader
running the command to regenerate that row cannot tell which unlabelled column is which.

Resolving that the file exists — three passes have — does not read what it prints. That is
`-78`'s own quarantined lesson, and it is why this sat through both.

**Repaired**: the header names all eleven.
**Falsifier:** `python3 scripts/wt002_lambda_report.py | head -3 | awk '{print NF}'`.

### III-16 · A named artefact defers to a section of Paper III that does not exist. **[D]**

The same file's `scaling_collapse()` docstring: *"**Paper III section 3.3** quotes these
figures."* Paper III's §3 runs **3.1 and 3.2**. The figures are quoted in **§A.2.3**.

`wt133` reads manuscripts, not scripts, so its *0 unresolved* says nothing about this. And the
corpus makes it sharper rather than softer: a `§3.3` **does** exist — REG-003's — and
`docs/crossref-dismissed.tsv` has carried the row adjudicating Paper III's one reference to it
since `-74`. The docstring names Paper III explicitly and points at nothing.

**Repaired**, to §A.2.3, with the miss named in place.
**Falsifier:** `grep -n "^### 3\.3" docs/papers/paper-III-dual-tensor/paper-III.md` → empty.

### III-17 · "three of its additions" is six, and it was six two days before the sentence was written. **[P]**

§11, immediately after the two counts `tests/test_paper_test_counts_are_derived.py` holds:
*"…**three of its additions** guard claims this paper makes and change no model code: two for
§3.1's closed form … and one asserting the algebraic collapse §4 publishes."*

`tests/test_lag.py` carries **ten** definitions at the pin `d655501` and **sixteen** at HEAD.
The six additions:

| test | added | guards |
|---|---|---|
| `test_deferred_information_is_exactly_linear_in_unobservability` | f1ceac7, 08-10 | §3.1's D(φ) = (1 − φ)·D(0) |
| `test_recognition_lag_is_not_linear_in_unobservability` | f1ceac7, 08-10 | §3.1's negative claim |
| `test_the_two_layer_recursion_collapses_to_the_form_limitation_4_publishes` | a0f5a3a, 08-10 | §4's algebraic collapse |
| `test_no_steady_state_deferral_ratio_once_decay_outruns_recognition` | **cc1d198, 08-12** | §4.4/§4.9's domain |
| `test_the_crossing_rate_closed_form_44_publishes_is_exact` | **cc1d198, 08-12** | §4.4's δ₃\* |
| `test_the_first_rung_boundary_44_publishes_is_exact` | **cc1d198, 08-12** | §4.4's first rung |

All six guard Paper III claims; the last three guard results §7's ledger prints. `cc1d198`'s own
commit subject is *"REG-002 results, errata, ledger WT-088, and **three tests S4.4 needed**"*.

**The sentence was never true.** It was first written at `a74a4ca` (2026-08-14) — **two days
after** the last three landed — and last edited at `bde6d65` (2026-08-16), the commit whose
subject is *"REVIEW-004 A3's remedy, four days late, and made to stay fixed by derivation."* The
sentence beside the derived counts was the one nothing derived.

This is the A2 finding, and the failure mode is one of the paper's own instruments':
`test_paper_test_counts_are_derived.py::test_paper_iii_names_every_module_it_counts` carries the
docstring *"A subtotal whose modules are not named is a number a reader cannot check."* §11
quotes a subtotal one sentence later and names no module.

**Repaired**: §11 says **six**, names the module, and attributes the last three to `cc1d198`.
Because naming a commit in prose trips
`tests/test_manuscript_shas_are_instrumented.py` — which refuses a pin that lives only in prose
*and refuses the repair of pasting the SHA into a comment* — the repair ships an instrument:
`tests/test_paper_iii_lag_additions_are_counted.py`, four assertions, which fails if the
additions are not exactly those six, if §11 stops saying six or goes back to three, if the three
`cc1d198` names were not introduced there, or if that commit ever touched `src/`.
**Falsifier:** `git show d655501:tests/test_lag.py | grep -c '^def test_'` → 10; at HEAD → 16.

---

## 3 · CLEARED — checked and standing, including the ones that died on contact

Nothing below is a finding. Each was opened as a live candidate and closed.

1. **`test_a_flat_gini_does_not_mean_a_bounded_one` appeared to exist only in `.bak` files.** It
   does not; it is at `tests/test_redistribution.py:61`. **A `| head -2` on my own verification
   grep manufactured the absence** — the two `.bak-wt137`/`.bak-wt139` copies sort first. The
   most nearly-shipped false finding of the pass, and it was self-inflicted. §6 banks it.
2. **`LEDGER.md`, cited bare twice, resolves only at `docs/LEDGER.md`.** Not a defect: the paper
   cites `METHOD-001`, `REVIEW-001` and `REG-003`…`REG-008` bare as well, and gives full paths
   only for `docs/notes/…` and `docs/RESULT-END-TO-END-001-E*.md`. A convention, applied
   consistently.
3. **§4.9's overstatement column.** 0.6 % and 1.2 % recompute to 0.40 % and 1.34 % from the
   table's rounded 4-dp values — but the rounding intervals admit both (row 1 spans 0–0.81 %,
   row 2 spans 1.15–1.53 %). Rows 3–5 match exactly. Not a finding.
4. **§4.2's "largest deviation … 8 × 10⁻¹⁶" against §7's 7 × 10⁻¹⁴.** Different rows of the
   ledger: 8 × 10⁻¹⁶ is the conserved-quantity row's one setting against its rival map's
   3 × 10⁻¹, which is the pairing §4.2 states; 7 × 10⁻¹⁴ is the five-setting mirror row.
5. **§8's "faced four times" against §A.2.4's "refused three times in other costumes."**
   Consistent: three refused, the fourth is the one §8.1 concedes.
6. **§4.4's 665 admissible pairs against §7's 683 disclosed.** 0.974 × 683 = 665. And §4.4's
   "86.1 % fall outside" is the exact complement of §7's 0.139 inside.
7. **The abstract's "δ leverage is 4.2 times the level at which recovery fails."** 2.58/0.61 = 4.23.
8. **§4.5's "more robust by a factor of six."** 66.2/11.5 = 5.76.
9. **§A.1.3's "E₀ = 100 to 0.031 over 400 periods."** 100 × 0.98⁴⁰⁰ = 0.0310.
10. **§4.9's δ₃\* movements.** Shape 0.13 % (0.00755 → 0.00754); level 4.3 % (0.00789 → 0.00755);
    goodwill's 0.002 a factor of 3.775 inside. All three as printed.
11. **§4.10's "five parts in ten thousand", its "15 %", and "0.438 … 1/E[T] = 0.435 to within a
    per cent."** All reachable from the table at its stated precision.
12. **"✓⧗ now marks three entries, cited in §§4.4, 4.6 and 4.9."** Exactly three entry marks —
    Long and Ravenscraft (§4.4), Dutta and Patatoukas (§4.6), Potepa and Thomas (§4.9). The
    claim is right in every particular. The *other* mark is III-10.
13. **A3, in full.** 222 §N.M references, 36 distinct, 0 unresolved; 49 entries, 49 cited; 11
    explicit "cited in §N.M" claims, 0 flagged.
14. **Every commit pin and digest §11 prints.** `edgar.py` at `d655501`, `lag.py` at `ad779eb`
    (and `lag.py` has exactly one commit), `lambda_sensitivity.py` at `b9089c7`; `9722342` is a
    single-file commit containing PRE-001 and nothing else; `d655501` does contain PRE-002 *and*
    `wt026_severe_test.py`, as §5.1's disclosure says; `93a159b` touches `edgar.py` by +21 lines
    and the `TIER_TAGS` block is byte-identical at `d655501` and HEAD; both SHA-256 digests
    verify against the committed files.
15. **§11's 100 and 62.** 11 + 42 + 9 + 10 + 10 + 18 = 100 at the pin; 42 + 10 + 10 = 62. Derived
    and green. The guard holding them is why III-17 is visible at all — it drew the eye to the
    one sentence beside them that nothing derived.
16. **§5.4's 1,833 classified firm-years** = REG-007's 644 window + 1,189 placebo. **§5.4's 0.103
    against 0.030** = REG-008's window and placebo M1 rates.
17. **`wt091`, `wt085_returns_conditioning.py`, `METHOD-001`, `REVIEW-001`, `NOTE-001`, all six
    REG-00x, `RESULT-002-*-run.log`, all four test modules and all three named test functions,
    `TIER_TAGS`, `variance_suppression`, `variance_concentration`, `n_crises`, `EG.EGY.PRIM.PP.KD`.**
    Forty-four of the forty-five enumerated artefacts resolve at the path or name given.
18. **All 39 tabulated §3 and §A.2 values.** Tables A–D of `wt027_report.py` and the whole of
    `wt002_lambda_report.py`'s sweep, collapse and slopes reproduce §3.1, §3.2, §A.2.3 and
    §A.2.4 exactly as printed. The §3 problem was never the tabulated values; it was the prose.

---

## 4 · NOT CHECKED — named so the next pass starts above zero

1. **§4.10's ten-cell α_ser/α_eff grid was not regenerated.** It was checked for internal
   consistency against §4.9's prose and against `RESULT_REACH`'s declarations; no named command
   produces it. This is III-12's family one section over, and it is the most likely site of the
   next A4 finding.
2. **§5.4's REG-006 lift figures** (4.01× → 4.01×, 2.01× → 2.10×, and the four intangible cells)
   were read against `RESULT-REG-006.md`'s headline and not re-derived from
   `data/reg-006-ladderC-*.json`.
3. **§4.7's band arithmetic** — 151 property events across 98 firms, 110 and then 133 joining to
   a disclosed life, sixteen bands, exactly one clearing the floor of 30 — was not re-derived
   from `data/reg-009-band-count*.json`.
4. **The bibliography's *content*.** III-10 audited the marks. Not one entry's bibliographic
   detail was re-verified; the four-pass note in the References is taken on its own account.
5. **33 of §7's 45 rows.** Twelve were checked against §§3–5's own restatements of the same
   figures. The rest were read and not re-run.
6. **§A.2.3's mutation counts** — *"leaking η into the dynamics fails four tests, and removing
   the scaling fails two"* — were not verified by mutation. Four and two are unguarded numbers
   about the test suite, which is III-17's shape exactly, and the suite is where to look.
7. **§7's "three of four tier counts identical", unscoped.** III-14 repaired §5.4 to say *in the
   pilot*; §7's ledger row repeats the phrase with no universe, and the replication rebuild has
   two of four. Whether a ledger row inherits its section's scoping is a curation question, not
   a defect I should decide — but it is the same sentence and the next pass should rule.
8. **The `--events` path into `wt026_severe_test.py`** (III-13's real repair). Teed up here
   rather than carded: it changes what a registered instrument reads.

---

## 5 · THE METHOD RESULT

**The matrix predicted this pass and the pass agreed with it.** Ten reads in, this is the first
data point the project has had on its own central question that is not confounded: every prior
comparison of finding counts was made across passes at different matrix coverage. `-77`, `-78`
and `-79` froze the *instrument set* and got 3, 2, 2 on a manuscript at 5 of 5. This pass filled
**three cells at once** on a manuscript at 2 of 5 and got **nine**, **eight of them from the
three new cells**. Coverage, not novelty, not residue, not depth.

**That does not resurrect the new-instrument anecdote, and the distinction matters.** No
instrument was invented here. A2, A4 and A5 are `-72`'s, `-74`'s and `-75`'s, unchanged. What
this pass adds is that an axis *this manuscript had never seen* pays on first application — which
is a claim about **coverage of the matrix**, not about inventing axes. Four rows now refute
"a new instrument is what produces findings" (`-71`, `-77`, `-78`, `-79`); this row refutes
nothing and completes the grid.

**So the question `-79` left for Jason is now askable on evidence it did not have.** With 15 of
15 filled, the next read of *any* manuscript is the first one in this project's history with
nowhere left to be structurally blind. If Paper III's third read returns a number near Paper
II's 2, coverage explains the whole history and the counter can start measuring documents. If it
returns nine again, it does not.

**And `-79`'s narrower proposal now has a second data point.** Under *count only findings that
require a manuscript edit*, this pass scores **7** and `-79` scores 0. **The two rules separate
these two passes by exactly the same distance** — 9 against 2 on the current rule, 7 against 0 on
the proposed one — so on this pair the change buys no resolution it did not already have. What it
would buy is elsewhere: it makes a pass's score independent of how much reviewing apparatus the
pass happened to touch, which is what `-79` was actually after. Still Jason's to rule on; still
not applied, and row 10 below is on the current rule.

---

## 6 · THE TELLS

**-80(i) · A `| head -N` on a verification grep can manufacture a finding, and the `.bak` files
sort first.** The one near-miss of this pass was a real test reported as missing because the
truncation ate the live file. **Verification greps take no `head`.** Count first, then truncate.

**-80(ii) · A number that appears exactly once in a document has nothing to disagree with, and
that is a defect independent of whether it is right.** `644` appeared once, deferring to a
section that did not carry it. Every other REG-007/008 figure is restated in §7 and disagrees
loudly when it drifts. **A load-bearing figure with one site is unguarded by construction** —
which is `test_manuscript_shas_are_instrumented.py`'s argument about SHAs, and it generalises to
figures.

**-80(iii) · When a wrong number contradicts the sentence it is supporting, the sentence is
usually right.** §5.4 asserted a rebuild within one per cent and printed a firm count 1.29 %
away. The claim was true; the evidence was mistyped. **Read the claim and its own number against
each other before reading either against the world** — it costs one subtraction and it found
III-14.

**-80(iv) · Fill the empty cell before arguing about the count.** Six handoffs argued about why
a counter would not decay while three cells of a fifteen-cell matrix had never been touched. The
matrix was built at `-76` and answered the question in one line; it took four more sessions to
act on it. **Build the coverage table early; it makes the argument unnecessary.**

**-80(v) · The guards are the reviewer's instrument, not just the author's.** Three of this
pass's repairs were rejected by the suite on the first run — TERM-001's anchor, REACH's
declaration for `281`, and the SHA-instrumentation refusal — and each rejection was correct and
improved the repair. **A repository whose guards fight your patch is telling you what your patch
forgot.** The SHA guard in particular refused the lazy fix by name and got an instrument out of
me instead.
