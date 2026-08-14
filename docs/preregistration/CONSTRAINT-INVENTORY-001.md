# CONSTRAINT-INVENTORY-001 · every reporting constraint in `docs/preregistration/`

- **Built:** 2026-08-14, `wealthTensor-42`, at `1e474b4`.
- **Why:** `-41` mechanised **one** reporting constraint (`REG-003` §7) and proved the class is
  real — the manuscript had violated it at six sites for two days, in the abstract. There are
  fifteen registration and construction documents in this directory and **nobody had ever
  enumerated what the others forbid.** The point of this file is the LIST.
- **Scope:** constraints on *how a result may be reported*. Predictions, falsifiers and
  instrument specifications are out of scope — they have `RESULT-*` documents and tests already.
- **Status:** this is an inventory, not a ruling. Where it grades the manuscript it says so and
  names the resolution it graded at.

---

## 0 · How this was built, and the two doors

**Door one — the keywords.** `grep -nEi "must not|may not|no sentence|shall not|is reported as|
never as|never instead|forbidden|prohibited"` across all 36 files: **102 candidate lines**.

**Door two — the section headings.** The estate has a *shape* for constraints and the keyword
grep does not find it: `## N · Stopping rule`, `## N · What may be claimed, and what may not`,
`## N · What a pass does NOT license`, `## N · What this may not move`, `## N · What this cannot
do`, and the `R*`/`C*` construction sections. **Twenty-seven sections across the sixteen
registration and construction files, and at least six of them carry a constraint the keyword grep
misses entirely** — `PRE-001` §9, `PRE-002` §3, `REG-001` §7, `REG-009` §4, `REG-012` §7 and
`CONSTRUCTION-REG-009` R3 all state their rule without a single one of those tokens.

> `-41`'s tell, applied to this sweep before it started: *when a hand-audit finds N sites, it
> found them through one door.* An inventory built on the keyword grep alone would have been a
> plausible, shorter, wrong list.

**The resolution column is the load-bearing one.** `-41`'s second tell: a compliance grade
applied at paragraph resolution against a sentence-level rule is a false green. It runs the
other way too — §3.3 below is a **paragraph** rule that `-41`'s sentence-level machinery could
not have expressed.

**And a constraint can be CONDITIONAL.** Three of the constraints below fire only on an outcome.
For those, reading the registration is not enough: you have to go and read which branch the run
landed in. That is why §3.3 sat unchecked while §7, four sections later in the same file,
got a machine.

---

## 1 · The inventory

Legend — **Scope:** MS = governs the manuscript · RES = governs a `RESULT-*` document ·
INST = governs an instrument or its inputs. **Machine:** the test that would go red.

| # | source | the constraint | governed quantity | resolution | scope | live? | verdict | recog | machine |
|---|---|---|---|---|---|---|---|---|---|
| C01 | `PRE-001` §9 | every dropped event counted in one of ten named buckets; *"saying what we sampled and what we dropped is a condition of the result being reportable at all"* | drop accounting | document | RES | yes | `RESULT-001` §2 *Drop accounting (PRE-001 §9)* tabulates them — **compliant** | MECH | none |
| C02 | `PRE-002` §3 | permutation *z* must be centred near 0 / sd near 1 or **no result from this pipeline is reportable** | negative control | document | MS+RES | yes | §5.3 reports it centred on zero with unit spread — **compliant** | MECH | none |
| C03 | `PRE-002` §3 | the observed *z* additionally reported as an **empirical permutation p-value** | `p` | sentence | MS | yes | §5.3 gives permutation p = 0.590 / 0.520 — **compliant** | MECH | none |
| C04 | `PRE-002` §3 | the synthetic power statement is **reported whatever happens** | power | document | MS | yes | §5.3's *"a power curve to be reported whatever happened"* — **compliant** | MECH | none |
| C05 | `PRE-002` §5 | *"the next move is not a third instrument on the same data"* | the lag gradient | document | MS+INST | yes | honoured; **T2 is carded and barred** on this ruling | READER | none — the ruling lives in `HANDOFF` §2 |
| C06 | `PRE-002` §2 | right-censored events **reported as such** | censoring | sentence | MS | yes | §5.3/§5.4 report censoring rates — **compliant** | MECH | none |
| C07 | `REG-001` §5 | *"this registration may not be amended after the first result commit"* | REG-001 | document | RES | yes | `RESULT-REG-001` returns NO VERDICT and the file is unamended — **compliant** | MECH | **ADJACENT** · `test_registrations_precede_their_instruments.py` (adjacent) |
| C08 | `REG-001` §7 | a pass licenses exactly one sentence; it does **not** license *"the price-layer result is novel — which it is not, and Wicksteed gets that credit in the text"* | novelty of the price-layer result | document | Paper I | **NO** | **the antecedent never occurred** — `RESULT-REG-001` is NO VERDICT, not a pass. Wicksteed's credit is discharged in `LEDGER` WT-066 and `ADR-001`; paper III does not carry the claim | n/a | none needed |
| C09 | `REG-002` E1 | if δ₃\* < 0.010, *"§4.4 may not report it as the section's headline"* | τ = −1 | section | MS | **YES — δ₃\* < 0.010** | δ₃\* = 0.0079 < 0.010 → **the constraint FIRES**; §4.4 is titled *"The design has a validity region, and the disclosed numbers fall outside it"* and the knife-edge is one bolded paragraph lead inside it, not the section's headline — **compliant, and this is the closest call in the table** | PROXY | none |
| C10 | `REG-002` §5 | E4's re-ask is *"labelled an EXTENSION of E4 throughout, never as E4"* | E4 | every mention | RES | yes | the manuscript names no `E`-labels at all (0 occurrences); the constraint binds `RESULT-REG-002` only — **out of manuscript scope** | MECH | none |
| C11 | `REG-003` §2 | a differently-composed rebuilt sample *"may not be"* silently substituted | the sample | document | RES | yes | §5.4 reports 695 vs 688 and cites the registered reconciliation rule — **compliant** | PROXY | **ADJACENT** · `test_pre002_data_is_pinned.py` (adjacent) |
| C12 | **`REG-003` §3.3** | **if α̂ lands in R1/R2 the finding *"must be reported with that sentence attached, in the same paragraph, not in a limitations section"*** | α̂ | **paragraph** | MS | **YES — R1 in every cut** | **FOUR LIVE VIOLATIONS at `1e474b4`**: §4.4, §5.4's bolded lead, §7's ledger row, §9 limitation 4. Repaired by `wt108` | MECH | **FOR** · **`test_reg003_sec33_asymmetry.py`** (new) |
| C13 | `REG-003` §3.3 | if `d = 0` in any sensitivity cell, *"that cell is reported as UNDEFINED and never as a number"* | α̂ per cell | cell | MS+RES | **NO** | `d` is 228–613 in every published cell; the antecedent never fired — **not live** | n/a | none needed |
| C14 | `REG-003` §4.3 | *"direction is reported as part of the result, never absorbed into a p-value"* | N_co | sentence | MS | yes | §5.4 reports clustering *above* the interval in both universes with the direction named — **compliant** | MECH | none |
| C15 | `REG-003` §7 | *"no sentence anywhere may round it"* — α̂ to *"the recognition rate"* | α̂ | **sentence** | MS | yes | six violations found and repaired by `-41` | MECH | **FOR** · **`test_reg003_sec7_rounding.py`** |
| C16 | `REG-003` §7 | *"rejecting independence in §4 does not rescue PRE-001"* | the lag gradient | document | MS | yes | §5.3/§5.4 draw no such inference — **compliant**; also the ruling barring T2 | MECH | none |
| C17 | `REG-003` §7 | §4.4 *"may change one number and the sentences that carry it, and may not reopen the argument"* | §4.4 | section | MS | yes | §4.4's argument is unchanged since `wt089`; `-41` and `-42` changed numbers and their sentences — **compliant** | PROXY | none |
| C18 | `REG-004` §5 | S3's general search *"is teed up in the handoff and is not attempted in this session"* | the age-dependent mirror | session | INST | yes | teed up, never attempted — **compliant** | READER | none |
| C19 | **`REG-004` §6** | **may not be claimed: *"that α_eff is 'the' recognition rate — it is a function of δ"*** | α_eff | sentence | MS | yes | **checked through both doors** (noun phrase and symbol): §4.10 names α_eff a function of δ at every site and §4.10's lead says *"three recognition rates now live in this paper and they are three different quantities"* — **compliant** | MECH | **FOR** · **`test_reg004_sec6_alpha_eff.py`** (new, `-43`) |
| C20 | `REG-004` §6 | may not be claimed: that the correction *"rescues PRE-001"* | PRE-001 | document | MS | yes | not claimed — **compliant** | MECH | none |
| C21 | `REG-004` §6 / `REG-005` §7 | *"unregistered robustness may be reported, labelled as robustness, and may not change a verdict"* | any unregistered cut | sentence | MS | yes | **SEVEN LIVE VIOLATIONS at `e947fb6`**, and the compliant grade above was reached through the `unregistered` keyword, which finds the site carrying the label and not the site carrying the **wrong** one. `REG-003` §3.1 A3 registers three sensitivities and §3.2 registers no cut; the 0.327 cut is filed under `RESULT-REG-003` §2's *"Unregistered robustness"* heading and the manuscript called it **"the registered adverse cut"** at four sites, with three more reporting unregistered values unlabelled. Repaired by `wt110` | MECH | **FOR** · **`test_reg004_sec6_unregistered_robustness.py`** (new, `-43`) |
| C22 | `REG-004` §6 / `REG-005` §7 | *"no parameter is added to the model at any point"* | the model | document | MS | yes | no parameter added — **compliant** | MECH | none |
| C23 | `REG-005` §7 | may not be claimed: that a negative result *"licenses removing §4.9's correction"* | §4.9 | section | MS | yes | §4.9 stands and §5.4 holds the lag distribution — **compliant** | MECH | none |
| C24 | `REG-005` §7 | may not be claimed: *"that the fitted lag distribution transfers to classes the PRE-002 sample does not cover"* | the lag distribution | sentence | MS | yes | §6.1's scope sentence (`-41` T5) states the covered classes — **compliant** | MECH | **FOR** · **`test_reg005_sec7_lag_transfer.py`** (new, `-43`) |
| C25 | `REG-005` §7 | may not be claimed: *"that the normalisation of §1 is innocuous — it is generous"* | §1's normalisation | sentence | RES | yes | binds `RESULT-REG-005` — **out of manuscript scope** | MECH | none |
| C26 | `REG-006` §4 Q1 | *"the word 'impairment' never appears unqualified"* and *"the count of firm-periods behind each ratio is printed next to the ratio"* | REG-006 statistics | every ratio | RES | yes | binds `REG-006`/`RESULT-REG-006` — **out of manuscript scope** | MECH | none |
| C27 | `REG-006` §4 Q2 | a cell with fewer than 20 firm-periods *"is reported as its count and no ratio is formed from it"* | thin cells | cell | RES | yes | binds `RESULT-REG-006` | MECH | none |
| C28 | `REG-006` §4 Q2 | the cap region's slope reported *"as a function of L/W, never as a point"* | the cap slope | sentence | MS+RES | **NO** | ladder C **failed as registered** (§7's row); no cap-region slope is reported anywhere, as a point or otherwise — **not live** | n/a | none needed |
| C29 | `REG-006` §8 | if ladder C's corrected lift lands below `REG-003`'s figure, §5.4's number is amended *"in the text where the number is — not in a footnote, and not in Limitation 9"* | §5.4's lift | **placement** | MS | **NO** | ladder C failed; no amendment was owed — **not live** | n/a | none needed |
| C30 | `REG-007` §5 | *"Λ ≈ 0 is NOT evidence for co-movement"* — stated before the run so a null cannot be sold as a finding | Λ | sentence | MS+RES | yes | the manuscript makes no co-movement claim from Λ — **compliant** | MECH | none |
| C31 | `REG-007` P4 | *"the registered claim is a sign and a significance level, nothing more"*; no threshold on Λ | Λ | sentence | MS | yes | §7's row reports the instrument as failed; no Λ magnitude claim — **compliant** | PROXY | none |
| C32 | `REG-007` §9 | if Λ is withheld, *"the counts are published anyway and the withholding is named as such"* | Λ | document | RES | yes | binds `RESULT-REG-007` — **compliant there** | MECH | **ADJACENT** · `test_reg007_resolution.py` (adjacent) |
| C33 | `REG-007` §4 | rebuilding the panel from `edgar.py` *"is forbidden by this registration"* | the panel | instrument | INST | yes | the committed panel is re-read — **compliant** | MECH | none |
| C34 | `REG-008` §9 | thin arms → *"reported as underpowered, the counts are published, and no significance claim is made"* | P1 replication | document | RES | yes | binds `RESULT-REG-008` | MECH | **ADJACENT** · `test_reg008_instrument.py` (adjacent) |
| C35 | `REG-008` §9 | if F1's gate fails, *"no Λ is printed at all"* | Λ | document | RES | yes | binds `RESULT-REG-008` — **compliant** | MECH | **BINDS** · `test_reg008_instrument.py` |
| C36 | `REG-009` §4 | a refusal is *"stated in the same sentence as the number that caused it"* | the δ design | **sentence** | RES | yes | `RESULT-REG-009` §4 states it that way — **compliant**. See §3: this is the constraint behind the §7-ledger presentation item on the board | READER | none |
| C37 | `REG-009` §12 | if Ψ and Ψ_rect(α̂) disagree the difference is attributed by S and the columns, *"never by narration"* | Ψ | sentence | RES | yes | `RESULT-REG-009` attributes numerically — **compliant** | PROXY | **ADJACENT** · `test_reg009_ladder_inputs.py` (adjacent) |
| C38 | `REG-009` §12 | §4.4's rectangle sentence repaired *"in one of exactly two ways"*: the rate named **and the rectangle labelled asserted rather than observed** | the rectangle | every mention | MS | yes | eight *asserted rectangle* sites; the label travels — **compliant** | MECH | **PARTIAL** · **`test_term001_rectangle.py`** |
| C39 | `REG-009` §12 | *"no free parameter may be introduced to reconcile Ψ with 99.7 %"* | Ψ | document | MS+INST | yes | §7's row reports 0.659 against 0.998 and reconciles nothing — **compliant** | PROXY | **ADJACENT** · F10, and `test_reg009_ladder_inputs.py` |
| C40 | `REG-009` §12 | §7.5's count lands *"whatever Ψ returns"*: 151/98 repaired against 55/38 as §5 collected it | §4.7's clause | sentence | MS | yes | §4.7 carries both counts — **compliant** | MECH | **BINDS** · `test_reg012_sec6_sec47_frozen.py` — **not** `test_term002_count.py`, which is about §8's free-parameter numeral and never opens §4.7 |
| C41 | `REG-010` §0 | *"P3 failed as registered and REG-010 does not re-score it"* | P3 | document | RES | yes | **closed by ruling** — do not reopen | PROXY | **PARTIAL** · `test_reg010_half_integer_banding.py` |
| C42 | `REG-010` §4 | a list of fifteen numbers *"this may not move"*; one new artifact, overwrites nothing | REG-009's numbers | artifact | RES+INST | yes | **compliant** | MECH | **PARTIAL** · `test_reg009_ladder_inputs.py` (four numbers), `test_reg009_band_count.py` (three), `test_reg010_half_integer_banding.py` |
| C43 | `CONSTRUCTION-REG-009` R2 | the fill raises *"the joinable column only"* | the fill | artifact | INST | yes | H6 refuses the run if `events_total` moves — **compliant** | MECH | **PARTIAL** · `test_reg009_band_count_filled.py` |
| C44 | `CONSTRUCTION-REG-009` R3 | the count is reported *"BESIDE `-31`'s, never instead of it"* | the band count | artifact | RES | yes | two artifacts, both committed — **compliant** | MECH | **PARTIAL** · `test_reg009_band_count.py` + `_filled` |
| C45 | `CONSTRUCTION-REG-009` R5 | *"no band edge, band width, floor, tag or interval rule is re-chosen in response to the number"*; `R_MIN` not promoted | the band count | document | RES | yes | **closed by ruling; unspent** | MECH | **ADJACENT** · `test_reg012_band_edge_phase.py` |
| C46 | `CONSTRUCTION-REG-010` C4 | the mirror is *"computed, reported beside, never used to choose"*; *"never promoted"* | the mirror | document | RES | yes | **compliant** | PROXY | **PARTIAL** · `test_reg010_half_integer_banding.py` |
| C47 | `REG-012` §4 | E1 and E2 *"are reported beside it, never instead of"* the histogram E3 | the phase histogram | document | RES | yes | **compliant** | MECH | **BINDS** · `test_reg012_band_edge_phase.py` |
| C48 | `REG-012` §6 | *"this measurement produces no new answer to §7.5's decision rule, and no sentence of the manuscript's §4.7 is changed by any outcome of it"* | §4.7 | **sentence** | MS | yes | §4.7 is unchanged since `REG-012` — **compliant**, and now pinned at `ba59370` | MECH | **FOR** · **`test_reg012_sec6_sec47_frozen.py`** (new, `-43`) |
| C49 | `REG-012` §7 | the shifted band count *"is refused, not merely unperformed"* | the band count | sentence | MS+RES | yes | **compliant** — but `-44` found the guard could not tell a refusal from a silence: both states have zero band counts and `test_reg012_band_edge_phase.py`'s assertion is an **absence**. Paired guard added | MECH | **FOR** · **`test_reg012_sec7_refusal_is_asserted.py`** (new, `-44`, the *presence* limb) + `test_reg012_band_edge_phase.py` (the *absence* limb) |
| C50 | `SOURCE-001` §3 | two caveats *"must be closed before the XBRL route is called closed in general"* | the XBRL route | document | RES | yes | `SOURCE-001` is FINISHED by ruling and the general claim is not made — **compliant** | MECH | **ADJACENT** · `test_source001_coverage.py` |

---

## 2 · What the sweep found

**Fifty constraints. Forty-eight were compliant or not live. TWO were violated — C12 at four
sites, found by this sweep; C21 at seven units, found by `-43` when it built C21's machine and
found this file's own grade to be the one-door verdict.**

- **C12 — `REG-003` §3.3 — is the finding.** Every cut of the run landed in **R1**, so the
  registered asymmetry fires, and the manuscript reported α̂ as the result at five places while
  attaching the direction at exactly one. The one that complied is the **abstract**, and it
  complied *by accident*: `-41`'s T1 rewrote it for §7 and the replacement happened to carry
  *"on both known biases' inflating side"* — the pre-edit line at `0b26a8a` had nothing.
  So the defect `SCOUT-001` diagnosed for §7 (*"a qualification that exists in the right
  paragraph and does not travel"*) was **reproduced in the same session that named it, by the
  repair for the other constraint.**
- **Three constraints were conditional and did not fire** (C13, C28, C29), and one had an
  antecedent that never occurred (C08). Recording those is the point: a constraint graded
  *"not live"* with its antecedent named is a question that stays closed, and a constraint
  nobody looked at is a question nobody knows is open.
- **C09 is the closest call in the table.** `REG-002`'s E1 falsifier *did* trip — δ₃\* = 0.0079
  is below the registered 0.010 — so §4.4 may not report τ = −1 as its headline. It does not:
  §4.4 is *titled* for the validity region, and the knife-edge is one bolded paragraph lead
  inside it plus a §7 survivals row carrying its eighty-seven-year half-life. Compliant on the
  section's headline, which is what E1 governs — **and worth re-reading the moment §4.4 is
  re-headlined or the knife-edge is promoted into the abstract's lead.**
- **~~Nine of the fifty already had a machine~~ — EIGHTEEN did, and sixteen of the eighteen do
  not bind (`-44`).** This bullet said *nine, all of them incidental: the test was written for
  a prediction or an artifact and happens to bind the constraint too.* Both halves were wrong,
  and the second one mattered. **Twenty-four rows name a machine**, eighteen of them
  incidental — a count of this file's own column that nobody recomputed until `-44` parsed it.
  And *"happens to bind"* was never verified for a single row. When it was, one question at a
  time — **if the constraint were violated, would this named test necessarily go red?** — the
  eighteen came back **2 BINDS · 6 PARTIAL · 10 ADJACENT**. See §3.
- **The purpose-built class is seven.** C12 and C15 (`-41`, `-42`), C19, C21, C24, C48 (`-43`),
  and C49 (`-44`, the paired presence limb — see §3.1).
- **`-43`'s finding, which is this file's own tell turned on this file.** §0 says an inventory
  built on the keyword grep alone would have been *a plausible, shorter, wrong list*. C21's row
  was graded by exactly that door: grep `unregistered`, find §5.4's labelled 0.460, mark the
  constraint compliant. **The second door for a labelling constraint is the WRONG label, not
  the missing one** — and behind it were four sites calling an unregistered cut *registered*
  and three reporting unregistered numbers bare.

## 2a · The counts, recomputed

`tests/test_constraint_inventory_selfconsistent.py` parses §1's table and requires this block
to match it. It exists because the sentence it replaces — *"nine of the fifty already had a
machine"* — was a count of a column in this file, stated in prose, wrong, and load-bearing for
two sessions.

| grade | n |
|---|---|
| rows | 50 |
| recog:MECH | 35 |
| recog:PROXY | 8 |
| recog:READER | 3 |
| recog:n/a | 4 |
| machine:FOR | 7 |
| machine:BINDS | 3 |
| machine:PARTIAL | 6 |
| machine:ADJACENT | 8 |
| machine:none | 26 |

---

## 3 · THE RECOGNISABILITY PARTITION (`-44`)

`-42` asked, in this file's definition of done: **which of the fifty are constraints a machine
could NEVER recognise, and what does the estate do about those?** `-43` answered it with three
cells — (a) has a machine, (b) could have one and nobody wrote it, (c) recognisable only by a
reader — and reported **(b) EMPTY**.

**(b) is not empty. It holds thirty-three of the fifty**, and the three-cell shape is why it
looked empty. Cell (a) is a fact about the ESTATE — somebody wrote a test. Cell (c) is a fact
about the CONSTRAINT — no test could be written. Those are two different axes fused into one
row of cells, and the fusion has a specific consequence: **anything with a name in the `machine`
column falls into (a) by definition, whether or not the named machine can see the constraint.**
The column was read as coverage. It was an adjacency column.

So the table now carries the axes separately: `recog` for the constraint, the **FOR / BINDS /
PARTIAL / ADJACENT** grade for the estate. Crossing them gives four cells, and the fourth is
the one the three-cell shape had no room for:

| | a machine binds it | nothing binds it |
|---|---|---|
| **machine-recognisable** (MECH·PROXY, 43) | **10** — 7 written FOR the constraint, 3 incidental and genuinely binding | **33** — the cell `-43` reported empty. 16 of them **name a machine that does not bind**: the false-green class |
| **reader-only** (READER, 3) | — | **3** — C05, C18, C36. §4 is what they get instead |

*(Four rows are `n/a`: C08, C13, C28, C29 fire on antecedents that never occurred, so there is
nothing to recognise. 43 + 3 + 4 = 50.)*

### 3.1 · The audit — what "happens to bind" turned out to mean

Each of the eighteen incidental entries was read in full against one question: **if the
constraint were violated, would this named test necessarily go RED?** Sixteen answer no or
not-quite. The pattern is not random and it is worth stating as a rule:

> **The reproduced numbers bind. The prohibitions escape.** A test written for a prediction
> opens the artifact; a constraint on *how a thing is reported* lives in prose the test never
> reads. Of the twelve distinct incidental test files, **three open a `.md` at all**, and two
> of those only to check that a numeral appears somewhere in it.

**BINDS (2).** C47 — `test_reg012_band_edge_phase.py:106` walks every histogram row and
requires it in the document's prose, so dropping E3 while keeping E1 is red. C35 — the F1 gate
is materialised in the committed artifact, so a violating world is a red world; note that it
binds the **antecedent**, going red identically when the constraint is *honoured*, and must be
re-read by a human the moment it fires.

**PARTIAL (6)** — C38, C41, C42, C43, C44, C46. Each binds the number and misses the
prohibition. Sharpest: **C42** names two tests that pin **three of its fifteen** frozen
numbers; moving Ψ, n, the distinct-pair count and **all four prediction verdicts** in
`data/reg-009-result.json` leaves both named files green (the pins that catch it are in
`test_reg009_ladder_inputs.py`, which the row did not name — now corrected). **C44** and
**C46**: neither named test opens a single `.md`, so `RESULT-REG-009-band-count.md` can be
deleted outright and the filled count written as superseding `-31`'s, green.

**ADJACENT (10)** — C07, C11, C32, C34, C37, C39, C45, C50, and two that were pointer defects
rather than coverage defects:
* **C40 named the wrong test entirely.** `test_term002_count.py` is about §8's free-parameter
  refusal numeral and never opens §4.7 or the strings 151/98/55/38. The clause **is**
  incidentally bound — by `test_reg012_sec6_sec47_frozen.py`'s §4.7 freeze, which contains it.
  Row corrected; the grade is BINDS via the right file.
* **C07's own test says so in its docstring** — *"it cannot see a registration edited after its
  result existed"* — which is precisely C07. The row inherited the file because the names
  rhymed.
* **C39's F10 is real and is a declaration check, not a no-free-parameter check.** It AST-scans
  one module for undeclared literals. A parameter added inside a function default, in another
  script, or in prose is invisible. That is an honest PROXY and it was filed as a guard.
* **C49 was the one worth repairing in-session, because its guard was not weak but
  *logically incapable*.** `REG-012` §7 distinguishes *refused* from *merely unperformed*, and
  both states have zero band counts in them; the named assertion is `assert not
  _threshold_reads(doc)`, an **absence**, which has the same truth value in both. Deleting
  every refusal sentence from `RESULT-REG-012-band-edge-phase.md` left the suite green.
  **Repaired as a pair** — `-42`'s whitespace lesson, one domain over: the absence limb stays
  where it is, and `tests/test_reg012_sec7_refusal_is_asserted.py` asserts the *presence* of
  the refusal, in the document's own voice (blockquotes excluded — reporting a prohibition is
  not performing a refusal) and naming its warrant. Red on the merely-unperformed document,
  green on the real one, with the old guard green on both.

### 3.2 · Cell (b), ranked — what is worth building next

Thirty-three entries, so this is a ranking and not a to-do list. Ordered by *what a violation
would cost times how cheaply it can be caught*, and each names the shape it should take.

1. **C42 · the fifteen frozen numbers** — twelve of fifteen unpinned, and the constraint is a
   literal list. This is the cheapest high-value guard in the estate: one test, fifteen
   assertions, no judgement anywhere in it.
2. **C07 · amended-after-result** — a git test, and the shape already exists in
   `test_reg012_sec6_sec47_frozen.py`. Compare each registration's last-modifying commit
   against its `RESULT-*` commit.
3. **C26 · *"the word 'impairment' never appears unqualified"*** — a pure regex constraint,
   over `RESULT-REG-006`, and its sibling limb (the count printed next to each ratio) is the
   `-43` two-limb shape.
4. **C44 / C46 / C41 · the "beside, never instead of / never promoted / does not re-score"
   family** — one guard, three constraints: assert both documents exist and that the later one
   carries no supersession claim. All three are currently guarded only by numerals.
5. **C10 · *"labelled an EXTENSION of E4 throughout, never as E4"*** — C21's exact shape, one
   document over, and C21 is the one that was not clean. Two limbs: wrong label, missing label.
6. **C16 / C20 / C23 / C25 / C30 · the forbidden-claim family** — five constraints, one
   claim-scanner shape, already built twice (C19, C24). Feed each registration its own
   forbidden claim before trusting the green (`-43`).
7. **C45 · `R_MIN` not promoted** — two assertions: `art["reading"]` and `art["band_rule"]`
   are the registered ones. Currently unguarded in both limbs.
8. **C01–C04, C06 · the reportable-at-all family** — presence guards, low cost, low risk,
   and C02's is conditional (assert the antecedent, `-42`).

### 3.3 · The three that are reader-only, and the adjacent check for each

This is the half of `-42`'s question that has a real answer, and the deliverable is the
sentence *saying which is which* — the adjacent check is never the constraint.

| | the constraint (reader) | the adjacent check (machine) | what the gap is |
|---|---|---|---|
| **C36** | a refusal is *"stated in the same sentence as the number that caused it"* — the reader's worry is §7's forty-row ledger diluting the §4.5 row that **refused in 400 of 400 draws** | the registration's literal requirement: the refusal and its number share a sentence. `RESULT-REG-009` §4 complies, and this is checkable | the registration says nothing about the row sharing a table with thirty rows that risked nothing. **A machine can check the sentence; only a reader can see the table.** Jason's call |
| **C05** | *"the next move is not a third instrument on the same data"* | no new instrument script targets the lag gradient; T2's card stays closed | the constraint is about a research *decision*, made by whoever holds the next at-bat. There is no artifact to read, because the artifact would be the violation |
| **C18** | S3's general search *"is teed up in the handoff and is not attempted in this session"* | the handoff carries the tee-up; no S3 instrument exists | *"in this session"* is unaddressable — a machine reading the repo cannot see which session did what, only what is there now |

Three PROXY rows sit just inside the boundary and are worth naming here because their adjacent
checks are already built and are mistaken for the constraint: **C09** (a machine can pin §4.4's
*title*; only a reader knows what a section's **headline** is), **C17** (*"may not reopen the
argument"* — a machine can freeze the argument's paragraphs, as C48 does for §4.7), and
**C37** (*"never by narration"* — a machine can require a numeral in the attribution paragraph;
whether the prose is doing the attributing is a reading).

---

## 3.0 · The `-43` list, preserved — the ones a machine could recognise, four of five now have one

Ranked by what a violation would cost. Written by `-42` as *"none of these is a defect today"*;
**that held for three of the four and not for C21**, which is the entry to read first. Superseded
in scope by §3 — this was a list of five, and the real cell holds thirty-three — but every entry
below is still the best short account of what building each of these guards actually cost.

1. **C19 · `REG-004` §6 — α_eff may not be called "the" recognition rate.** ✅ **MECHANISED** —
   `tests/test_reg004_sec6_alpha_eff.py`. The exact sibling of C15, one symbol over, and the
   manuscript is clean at all six α_eff sites. Two doors, as C15 needed: the symbol and the
   VALUE, because §4.10's table can carry the claim with the symbol left out. No pre-edit
   violating text exists, so the control is the registration's own forbidden claim plus a
   mechanical mutation of §4.9's one at-risk sentence — delete the δ-motion clause and the guard
   must go red, or its green on the manuscript means nothing.
2. **C21 · unregistered robustness must be labelled as robustness.** ✅ **MECHANISED, AND IT WAS
   NOT CLEAN** — `tests/test_reg004_sec6_unregistered_robustness.py`, seven live units repaired
   by `wt110`. See §2. The row above graded this constraint compliant off the one site that
   carries the label; the machine reads `REG-003` §3.1 A3's three registered sensitivities and
   `RESULT-REG-003` §2's unregistered heading, and asks about the label the manuscript actually
   used. Two limbs, because they fail separately: the label is WRONG, or the label is MISSING.
3. **C48 · no sentence of §4.7 is changed by any outcome of `REG-012`.** ✅ **MECHANISED** —
   `tests/test_reg012_sec6_sec47_frozen.py`, pinned at `ba59370`, the commit that registered
   `REG-012`. **The pin records which version it froze**, and a git test reads §4.7 out of that
   commit and requires it to hash to the pin — otherwise the freeze silently re-anchors to
   whenever somebody last ran the file, which is a snapshot wearing a freeze's clothes. The red
   message states both readings (REG-012's outcome → revert; anything else → re-pin in the same
   commit and name the licence), because a guard that cannot tell them apart teaches the next
   session to re-pin without reading.
4. **C24 · the fitted lag distribution may not be claimed to transfer beyond the sample's
   classes.** ✅ **MECHANISED** — `tests/test_reg005_sec7_lag_transfer.py`. Clean, and the file
   says out loud which half of its predicate is live: the manuscript names the fit, makes
   extension claims about other things, and never pairs them. Two traps found while building it:
   `travels` is not an extension verb (§4.10's *"travels with the lag distribution rather than
   with the filings"* is the paper making this constraint's own point), and a scope test keyed on
   the word *sample* passes `REG-004` §6's own example of the violation.
5. **C36 · a refusal is stated in the same sentence as the number that caused it.** This is the
   constraint underneath the presentation item on the board — §7's forty-row ledger dilutes the
   §4.5 row that **refused in 400 of 400 draws**. The registration requires the refusal and its
   number to share a sentence; it says nothing about the row sharing a table with thirty rows
   that risked nothing. That gap is a judgement about a reader and stays Jason's call.

## 3.4 · WHAT AN UNRECOGNISABLE CONSTRAINT GETS INSTEAD OF A MACHINE

`-42`'s question had a second half and the estate has been answering it for eleven sessions
without writing the answer down. There are exactly three instruments in use, and they are not
interchangeable:

1. **A RULING, in `HANDOFF` §2.** What C05 has. It is durable (it is read at student-in, every
   session), it is cheap, and its failure mode is precisely known: **`-39` established that a
   handoff instruction silently outranks a doctrine leaf**, so a ruling is only as strong as
   the document it sits in and loses to any later, more specific instruction. A ruling is what
   a constraint gets when nothing can watch it *and* the decision is the estate's own.
2. **JASON'S CALL.** What C36 has. Reserved, per the charter, for judgements about a reader —
   not for anything a Claude with darwin and the repos could decide. C36 qualifies because the
   thing at issue is what a referee's eye does with a forty-row table, which is not a fact
   about the repo.
3. **A TRIPWIRE — and this is the one the estate keeps inventing in prose and never builds.**

**The tripwire is the general answer, and it is not the adjacent check.** An adjacent check
fires when a *machine-checkable neighbour* of the constraint is violated and says *"this is
wrong."* A tripwire fires when the **antecedent of a re-read** is satisfied and says something
different: *"a human must now read this, because the machine cannot."* Same mechanism, opposite
speech act, and the difference is the whole answer to `-42`'s second half.

The estate already wrote one, in prose, in §2's C09 bullet: *"worth re-reading the moment §4.4
is re-headlined or the knife-edge is promoted into the abstract's lead."* That sentence names a
**machine-checkable antecedent** (the section title changes; the knife-edge string enters the
abstract) attached to a **reader-only consequent** (is τ = −1 now the headline?). Nobody built
it, so it is a re-read that depends on a future session happening to read this bullet — which
is exactly the failure `-39` documented.

Three tripwires are owed, and each is two assertions and a message that says *go read this*:

* **C09** — §4.4's title, and the knife-edge out of the abstract's lead.
* **C17** — §4.4's argument paragraphs, frozen the way C48 freezes §4.7. A changed hash is not
  a violation; it is *"§4.4 moved — read it against `REG-003` §7's may-not-reopen."*
* **C36** — the shape of §7's ledger. If a column separating algebra rows from rows that risked
  something is ever added, or if the row count moves, the presentation judgement Jason owns is
  live again and he should be asked once, not silently inherited.

**The rule to carry forward: a constraint a machine cannot recognise gets a machine on its
ANTECEDENT and a human on its consequent — and a guard whose red message names a violation
when it should name a re-read teaches the next session to suppress it.** `-42` learned the
same lesson about conditional constraints in the other direction: different failures, different
messages.

---

## 4 · What this file is not

It is not a licence to re-open anything in `HANDOFF` §2. Where a constraint is marked *closed by
ruling*, the ruling governs and this row is a pointer to it. It is not a substitute for reading
the registration: every quotation here is short enough to have lost its context, and the
verdicts were reached by reading the sections, not the greps.

And it is a snapshot. **A constraint's status can change without the constraint changing** —
three of these fire on an outcome, and C12 sat unchecked for exactly that reason. Re-read the
`live?` column against any new `RESULT-*`.
