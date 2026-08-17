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
| C05 | `PRE-002` §5 | *"The next move in that case is not a third instrument on the same data"* — **`in that case` carries `PRE-002` §5's antecedent, *"if PRE-002 fails"*, which the shorter quotation had dropped; restored `-45`** | the lag gradient | document | MS+INST | yes | honoured; **T2 is carded and barred** on this ruling | READER | none — the ruling lives in `HANDOFF` §2 |
| C06 | `PRE-002` §2 | right-censored events **reported as such** | censoring | sentence | MS | yes | §5.3/§5.4 report censoring rates — **compliant** | MECH | none |
| C07 | `REG-001` §5 | *"this registration may not be amended after the first result commit"* | REG-001 | document | RES | yes | `RESULT-REG-001` returns NO VERDICT and the file is unamended — **compliant** | MECH | **FOR** · `test_reg001_sec5_no_amendment_after_result.py` (`-47`) — ancestry, not date; scope asserted to be REG-001 alone; graded on probe `R1`, which was GREEN before it and is RED after (see §2c). Still incidentally adjacent: `test_registrations_precede_their_instruments.py`, whose docstring says it cannot see this |
| C08 | `REG-001` §7 | a pass licenses exactly one sentence; it does **not** license *"the price-layer result is novel — which it is not, and Wicksteed gets that credit in the text"* | novelty of the price-layer result | document | Paper I | **NO** | **the antecedent never occurred** — `RESULT-REG-001` is NO VERDICT, not a pass. Wicksteed's credit is discharged in `LEDGER` WT-066 and `ADR-001`; paper III does not carry the claim | n/a | none needed |
| C09 | `REG-002` **E2** | if δ₃\* < 0.010, *"§4.4 may not report it as the section's headline"* | τ = −1 | section | MS | **YES — δ₃\* < 0.010** | δ₃\* = 0.0079 < 0.010 → **the constraint FIRES**; §4.4 is titled *"The design has a validity region, and the disclosed numbers fall outside it"* and the knife-edge is one bolded paragraph lead inside it, not the section's headline — **compliant, and this is the closest call in the table**. *Cited as E1 until `-45`; see §2* | PROXY | **TRIPWIRE** · `test_tripwire_c09_sec44_headline.py` — antecedents only, **not coverage** |
| C10 | `REG-002` §5 | E4's re-ask is *"labelled an EXTENSION of E4 throughout, never as E4"* | the α = 0.35 **substitution**, not the token `E4` | sentence | RES | yes | **compliant.** `RESULT-REG-002` names `E4` four times and **only one is the re-ask** (§3's closing sentence); §1's table row, §3's heading and §3's opening name E4 *as the registered test*, which is what it is. The manuscript names `E4` **zero** times — **out of manuscript scope**, now a measurement rather than a reading. The **script** surface is real and is `wt088` alone — see §2f | MECH | **FOR** · `test_reg002_sec5_e4_extension_label.py` (`-50`) — a REFERENT scan at SENTENCE resolution (limb A), a presence limb for the label (limb B), and the same pair scoped to `wt088` (limb C). Graded on the catcher lists, not the pointers (`-44`): `R4` → 2 (limb A owned; limb B genuine — `R4` deletes the label as it mislabels) · `R4b` → **1, limb A alone** · `R4c` → 2 (limb B owned; the fusion pin, genuine — the deletion removes one of §3's two substitution sentences) · `R4d` → 3 (both limb C tests owned; its third, `test_reg009_ladder_inputs.py`'s instrument re-run, is a reproducibility pin and **incidental**, `-46`). Limbs A and B each hold a probe the other is green on, so both are separably load-bearing |
| C11 | `REG-003` §2 | a differently-composed rebuilt sample *"may not be"* silently substituted | the sample | document | RES | yes | §5.4 reports 695 vs 688 and cites the registered reconciliation rule — **compliant** | PROXY | **ADJACENT** · `test_pre002_data_is_pinned.py` (adjacent) |
| C12 | **`REG-003` §3.3** | **if α̂ lands in R1/R2 the finding *"must be reported with that sentence attached, in the same paragraph, not in a limitations section"*** | α̂ | **paragraph** | MS | **YES — R1 in every cut** | **FOUR LIVE VIOLATIONS at `1e474b4`**: §4.4, §5.4's bolded lead, §7's ledger row, §9 limitation 4. Repaired by `wt108` | MECH | **FOR** · **`test_reg003_sec33_asymmetry.py`** (new) |
| C13 | `REG-003` §3.3 | if `d = 0` in any sensitivity cell, *"that cell is reported as UNDEFINED and never as a number"* | α̂ per cell | cell | MS+RES | **NO** | `d` is 228–613 in every published cell; the antecedent never fired — **not live** | n/a | none needed |
| C14 | `REG-003` §4.3 | *"direction is reported as part of the result, never absorbed into a p-value"* | N_co | sentence | MS | yes | §5.4 reports clustering *above* the interval in both universes with the direction named — **compliant** | MECH | none |
| C15 | `REG-003` §7 | *"no sentence anywhere may round it"* — α̂ to *"the recognition rate"* | α̂ | **sentence** | MS | yes | six violations found and repaired by `-41` | MECH | **FOR** · **`test_reg003_sec7_rounding.py`** |
| C16 | `REG-003` §7 | *"rejecting independence in §4 does not rescue PRE-001"* | the lag gradient | document | MS | yes | §5.3/§5.4 draw no such inference — **compliant**; also the ruling barring T2 | MECH | none |
| C17 | `REG-003` §7 | §4.4 *"may change one number and the sentences that carry it, and may not reopen the argument"* | §4.4 | section | MS | yes | §4.4's argument is unchanged since `wt089`; `-41` and `-42` changed numbers and their sentences — **compliant** | PROXY | **TRIPWIRE** · `test_tripwire_c17_sec44_argument.py` — §4.4 numeral-masked, **not coverage** |
| C18 | `REG-004` §5 | S3's general search *"is teed up in the handoff and is not attempted in this session"* | the age-dependent mirror | session | INST | yes | teed up, never attempted — **compliant** | READER | none |
| C19 | **`REG-004` §6** | **may not be claimed: *"that α_eff is 'the' recognition rate — it is a function of δ"*** | α_eff | sentence | MS | yes | **checked through both doors** (noun phrase and symbol): §4.10 names α_eff a function of δ at every site and §4.10's lead says *"three recognition rates now live in this paper and they are three different quantities"* — **compliant** | MECH | **FOR** · **`test_reg004_sec6_alpha_eff.py`** (new, `-43`) |
| C20 | `REG-004` §6 | may not be claimed: that the correction *"rescues PRE-001"* | PRE-001 | document | MS | yes | not claimed — **compliant** | MECH | none |
| C21 | `REG-004` §6 / `REG-005` §7 | *"unregistered robustness may be reported, labelled as robustness, and may not change a verdict"* | any unregistered cut | sentence | MS | yes | **SEVEN LIVE VIOLATIONS at `e947fb6`**, and the compliant grade above was reached through the `unregistered` keyword, which finds the site carrying the label and not the site carrying the **wrong** one. `REG-003` §3.1 A3 registers three sensitivities and §3.2 registers no cut; the 0.327 cut is filed under `RESULT-REG-003` §2's *"Unregistered robustness"* heading and the manuscript called it **"the registered adverse cut"** at four sites, with three more reporting unregistered values unlabelled. Repaired by `wt110` | MECH | **FOR** · **`test_reg004_sec6_unregistered_robustness.py`** (new, `-43`) |
| C22 | `REG-004` §6 / `REG-005` §7 | *"no parameter is added to the model at any point"* | the model | document | MS | yes | no parameter added — **compliant** | MECH | none |
| C23 | `REG-005` §7 | may not be claimed: that a negative result *"licenses removing §4.9's correction"* | §4.9 | section | MS | yes | §4.9 stands and §5.4 holds the lag distribution — **compliant** | MECH | none |
| C24 | `REG-005` §7 | may not be claimed: *"that the fitted lag distribution transfers to classes the PRE-002 sample does not cover"* | the lag distribution | sentence | MS | yes | §6.1's scope sentence (`-41` T5) states the covered classes — **compliant** | MECH | **FOR** · **`test_reg005_sec7_lag_transfer.py`** (new, `-43`) |
| C25 | `REG-005` §7 | may not be claimed: *"that the normalisation of §1 is innocuous — it is generous"* | §1's normalisation | sentence | RES | yes | binds `RESULT-REG-005` — **out of manuscript scope** | MECH | none |
| C26 | `REG-006` **§3** Q1 | *"the word \"impairment\" never appears in it unqualified"* and *"the count of firm-periods behind each ratio is printed next to the ratio"* | REG-006 statistics | every ratio | RES | yes | binds `REG-006`/`RESULT-REG-006` — **out of manuscript scope**. Compliant on limb A, and **not for the reason three handoffs gave**: the document carries twelve occurrences and **two are bare** — they are lawful because neither states a statistic of this study, which is what *in it* means (`-45`). Limb B is **BOUNDED, NOT CLEAN**: §2's internal-control table prints twelve ratios and no counts — see §2d | MECH | **FOR** · `test_reg006_sec3_q1_two_limbs.py` (`-48`) — one locator, two assertions; graded on probes `R2a` and `R2b`, both green before it and red after, each with exactly one catcher |
| C27 | `REG-006` **§3** Q2 | a cell with fewer than 20 firm-periods *"is reported as its count and no ratio is formed from it"* | thin cells | cell | RES | yes | binds `RESULT-REG-006` | MECH | none |
| C28 | `REG-006` **§3** Q2 | the cap region's slope reported *"as a function of L/W, never as a point"* | the cap slope | sentence | MS+RES | **NO** | ladder C **failed as registered** (§7's row); no cap-region slope is reported anywhere, as a point or otherwise — **not live** | n/a | none needed |
| C29 | `REG-006` §8 | if ladder C's corrected lift lands below `REG-003`'s figure, §5.4's number is amended *"in the text where the number is — not in a footnote, and not in Limitation 9"* | §5.4's lift | **placement** | MS | **NO** | ladder C failed; no amendment was owed — **not live** | n/a | none needed |
| C30 | `REG-007` §5 | *"Λ ≈ 0 is NOT evidence for co-movement"* — stated before the run so a null cannot be sold as a finding | Λ | sentence | MS+RES | yes | the manuscript makes no co-movement claim from Λ — **compliant** | MECH | none |
| C31 | `REG-007` P4 | *"the registered claim is a sign and a significance level, nothing more"*; no threshold on Λ | Λ | sentence | MS | yes | §7's row reports the instrument as failed; no Λ magnitude claim — **compliant** | PROXY | none |
| C32 | `REG-007` §9 | if Λ is withheld, *"the counts are published anyway and the withholding is named as such"* | Λ | document | RES | yes | binds `RESULT-REG-007` — **compliant there** | MECH | **ADJACENT** · `test_reg007_resolution.py` (adjacent) |
| C33 | `REG-007` **§3.1** | rebuilding the panel from `edgar.py` *"is forbidden by this registration"* | the panel | instrument | INST | yes | the committed panel is re-read — **compliant** | MECH | none |
| C34 | `REG-008` §9 | thin arms → *"reported as underpowered, the counts are published, and no significance claim is made"* | P1 replication | document | RES | yes | binds `RESULT-REG-008` | MECH | **ADJACENT** · `test_reg008_instrument.py` (adjacent) |
| C35 | `REG-008` §9 | if F1's gate fails, *"no Λ is printed at all"* | Λ | document | RES | yes | binds `RESULT-REG-008` — **compliant** | MECH | **BINDS** · `test_reg008_instrument.py` |
| C36 | `REG-009` §4 | a refusal is *"stated in the same sentence as the number that caused it"* | the δ design | **sentence** | RES | yes | `RESULT-REG-009` §4 states it that way — **compliant**. See §3: this is the constraint behind the §7-ledger presentation item on the board | READER | **TRIPWIRE** · `test_tripwire_c36_sec7_ledger_shape.py` — §7's ledger shape, **not coverage**; a red asks Jason once |
| C37 | `REG-009` §12 | if Ψ and Ψ_rect(α̂) disagree the difference is attributed by S and the columns, *"never by narration"* | Ψ | sentence | RES | yes | `RESULT-REG-009` attributes numerically — **compliant** | PROXY | **ADJACENT** · `test_reg009_ladder_inputs.py` (adjacent) |
| C38 | `REG-009` §12 | §4.4's rectangle sentence repaired *"in one of exactly two ways"*: the rate named **and the rectangle labelled asserted rather than observed** | the rectangle | every mention | MS | yes | eight *asserted rectangle* sites; the label travels — **compliant** | MECH | **PARTIAL** · **`test_term001_rectangle.py`** |
| C39 | `REG-009` §12 | *"no free parameter may be introduced to reconcile Ψ with 99.7 %"* | Ψ | document | MS+INST | yes | §7's row reports 0.659 against 0.998 and reconciles nothing — **compliant** | PROXY | **ADJACENT** · F10, and `test_reg009_ladder_inputs.py` |
| C40 | `REG-009` §12 | §7.5's count lands *"whatever Ψ returns"*: 151/98 repaired against 55/38 as §5 collected it | §4.7's clause | sentence | MS | yes | §4.7 carries both counts — **compliant** | MECH | **BINDS** · `test_reg012_sec6_sec47_frozen.py` — **not** `test_term002_count.py`, which is about §8's free-parameter numeral and never opens §4.7 |
| C41 | `REG-010` §0 | *"P3 failed as registered and REG-010 does not re-score it"* | P3 | document | RES | yes | **closed by ruling** — do not reopen; `RESULT-REG-010` restates the failure in its own voice at §0, §3 and §6 — **compliant** | PROXY | **FOR** · `test_reg009_reg010_supersession_family.py` (`-49`) — a POLARITY pair: no unnegated clause re-scores P3, and the document's own two refusal sentences are pinned present. Graded on probes `R3c` (1 catcher) and `R3f` (1 catcher). Still incidentally PARTIAL via `test_reg010_half_integer_banding.py`, which binds the number and misses the prohibition |
| C42 | `REG-010` §4 | a list of fifteen numbers *"this may not move"*; one new artifact, overwrites nothing | REG-009's numbers | artifact | RES+INST | yes | **compliant** | MECH | **FOR** · `test_reg010_sec4_frozen_numbers.py` (`-46`) — all fifteen frozen at every artifact site AND in the documents that report them, each with its own forbidden move; graded on the mutation, not the pointer (see §2b). Incidentally also `test_reg009_ladder_inputs.py`, `test_reg009_band_count.py`, `test_reg010_half_integer_banding.py` |
| C43 | `CONSTRUCTION-REG-009` R2 | the fill raises *"the joinable column only"* | the fill | artifact | INST | yes | H6 refuses the run if `events_total` moves — **compliant** | MECH | **PARTIAL** · `test_reg009_band_count_filled.py` |
| C44 | `CONSTRUCTION-REG-009` R3 | the count is reported *"BESIDE `-31`'s, never instead of it"* | the band count | artifact | RES | yes | two artifacts, both committed — **compliant**, and the one near-miss (§0's *"the measurement replacing both brackets"*) is lawful at CLAUSE resolution and pinned; see §2e | MECH | **FOR** · `test_reg009_reg010_supersession_family.py` (`-49`) — a REFERENT scan (the verb's object must be `-31`'s count) plus the presence pair *beside* requires. Graded on probes `R3a` (1 catcher) and `R3d` (1 owned catcher; its other five are `test_reg010_sec4_frozen_numbers.py`'s `-42` antecedent and are incidental). Still incidentally PARTIAL via `test_reg009_band_count.py` + `_filled` |
| C45 | `CONSTRUCTION-REG-009` R5 | *"no band edge, band width, floor, tag or interval rule is re-chosen in response to the number"*; `R_MIN` not promoted | the band count | document | RES | yes | **closed by ruling; unspent** | MECH | **ADJACENT** · `test_reg012_band_edge_phase.py` |
| C46 | `CONSTRUCTION-REG-010` C4 | the mirror is *"computed, reported beside, never used to choose"*; *"never promoted"* | the mirror | document | RES | yes | **compliant** — §4 refuses the mirror *"under this outcome or any other"* in the document's own voice | PROXY | **FOR** · `test_reg009_reg010_supersession_family.py` (`-49`) — the same POLARITY pair as C41, on the mirror. Graded on probes `R3b` (1 catcher) and `R3e` (1 catcher). Still incidentally PARTIAL via `test_reg010_half_integer_banding.py` |
| C47 | `REG-012` §4 | E1 and E2 *"are reported beside it, never instead of"* the histogram E3 | the phase histogram | document | RES | yes | **compliant** | MECH | **BINDS** · `test_reg012_band_edge_phase.py` |
| C48 | `REG-012` §6 | *"this measurement produces no new answer to §7.5's decision rule, and no sentence of the manuscript's §4.7 is changed by any outcome of it"* | §4.7 | **sentence** | MS | yes | §4.7 moved once since `REG-012` — at `6314302`, licensed by `ASC 350-30-35-15` and recorded — **compliant**; the `ba59370` anchor is immutable | MECH | **FOR** · **`test_reg012_sec6_sec47_frozen.py`** (new, `-43`) |
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
- **C09 is the closest call in the table.** `REG-002`'s **E2** falsifier *did* trip —
  δ₃\* = 0.0079 is below the registered 0.010 — so §4.4 may not report τ = −1 as its headline.
  It does not: §4.4 is *titled* for the validity region, and the knife-edge is one bolded
  paragraph lead inside it plus a §7 survivals row carrying its eighty-seven-year half-life.
  Compliant on the section's headline, which is what E2 governs — **and worth re-reading the
  moment §4.4 is re-headlined or the knife-edge is promoted into the abstract's lead.**
  **That sentence is now built: `tests/test_tripwire_c09_sec44_headline.py` (`-45`).**
- **~~`REG-002` E1~~ — THE ROW CITED THE WRONG FALSIFIER FOR THREE SESSIONS, AND EVERY CHECK
  ANYBODY COULD HAVE RUN CAME BACK GREEN.** C09's row, this bullet, §3.3, §3.4 and two
  handoffs all named **E1**. The clause quoted in the row — *"§4.4 may not report it as the
  section's headline"* — is **E2**'s, and E2 is the one `RESULT-REG-002` §1 records as
  **FIRED**. E1 is the mean-τ falsifier that §2 of that same RESULT records as
  **mis-specified**, and it did not fire. The citation survived because **both** falsifiers
  constrain §4.4's headline — E1 would have downgraded the headline claim from *inverts* to
  *destroys* — so an existence check (*does `REG-002` have an E1? does it mention §4.4's
  headline?*) returns yes to a wrong pointer. This is `-44`'s finding one column to the left:
  **a `source` cell is a provenance claim exactly as a `machine` cell is a coverage claim, and
  nobody had verified a single one of those either.** The audit question that catches it is
  not *does the cited section exist* but **does the cited section contain the words in the
  quotation column** — mechanised in `test_constraint_inventory_selfconsistent.py`
  (`test_every_quoted_constraint_appears_in_its_cited_source`, `-45`), which now reads all
  fifty rows on every run.
- **THE PROVENANCE AUDIT, ASKED OF ALL FIFTY: SIX ROWS WERE WRONG, IN THREE SHAPES.** Forty-six
  rows quote; four describe (C02, C03, C04, C06, pinned, because deleting a quotation is the
  cheapest way to silence this check). Of the forty-six:
  * **Wrong locator, right document — four rows.** C09 (`E1` → **E2**) · C33 (`§4` → **§3.1**;
    the panel-rebuild prohibition is in §3.1's frame) · C26, C27, C28 (`§4 Q1/Q2` → **§3** Q1/Q2;
    §4 of `REG-006` is *The registered predictions* and the Q-block is §3). **Every one of these
    resolves under an existence check and under a whole-file search** — which is why the audit
    had to resolve the *exact* cited block, and why the machine nests its locators: `Q1` is
    unique in `REG-006`, so a union of `§4` and `Q1` finds the right text under a wrong address.
  * **A paraphrase that dropped the antecedent — one row.** C05 quoted *"the next move is not a
    third instrument on the same data"*; `PRE-002` §5 says *"The next move **in that case** is
    not a third instrument…"*, and *in that case* is the conditional's antecedent (*if PRE-002
    fails*). `-42`'s rule — **a conditional constraint's guard must assert its antecedent** —
    has a twin here: **a conditional constraint's QUOTATION must carry its antecedent**, or the
    row records an unconditional rule the registration never wrote.
  * **A paraphrase that dropped a referent — one row.** C26 quoted *"the word 'impairment' never
    appears unqualified"*; the registration says *"never appears **in it** unqualified"*, where
    *it* is the file's own statistics. The shorter form reads as a rule about the manuscript.
  The check compares the **conjunction** of a row's quotations, not any one of them: the first
  cut used `any`, and C05's paraphrase passed on the strength of the correctly-quoted fragment
  sitting beside it. A containment test over a disjunction certifies its weakest conjunct.
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

## 2b · C42, and the third coverage claim nobody had measured (`-46`)

> **`-44` FOUND THAT THE `machine` COLUMN WAS A COVERAGE CLAIM NOBODY VERIFIED. `-45` FOUND
> THE SAME OF THE `source` COLUMN. `-46` FOUND IT OF THIS FILE'S OWN PROSE — AND THE PROSE
> WAS WRONG BY ELEVEN.**

§3.2 ranked **C42 first in cell (b) for two sessions** on the sentence *"twelve of fifteen
unpinned"*, and the `-45` → `-46` handoff carried it forward as the at-bat's whole warrant
(*"twelve of those mutations pass today — run the control BEFORE you write the guard"*).
`-46` ran the control first, exactly as instructed, and the instruction's own premise did not
survive it. Each of `REG-010` §4's fifteen was moved on a scratch copy of the repo and the
whole suite run:

| | probes | caught before `-46` |
|---|---|---|
| the fifteen, moved in `data/` | 15 | **14** |
| the same numbers moved in the `RESULT-*` PROSE ONLY, artifacts untouched | 7 | 4 |
| **total** | **22** | **19** |

**The three that were green** are the 98 firms, the 110 and the 133 — all three of them in
`RESULT-REG-009-band-count.md` and `RESULT-REG-009-band-count-filled.md`, which no
reproducibility test regenerates. **The 98 is the sharpest: it is the one frozen number with
no field in any artifact at all.** It exists as a numeral in prose and nowhere else, so
`test_reg010_sec4_frozen_numbers.py` recomputes it from the committed filings through the
band-count instrument's own pure functions and binds the prose to *that*.

**Why the claim was wrong, and why it read as right.** The grade was derived from the
`machine` column — *these two files pin three of the fifteen* — and the column names the
tests written **for** a constraint, never the tests that happen to catch it. Eight of the
fifteen turn out to be held by `test_reg009_ladder_inputs.py`'s
`test_the_instrument_reruns_to_the_same_numbers`, which is in no row's `machine` cell for
C42 and would not belong there. So the sentence was true of the **named files** and false of
the **estate**, and every check a reader would run — *does the row name the right tests? do
those tests pin only three?* — returns yes.

> **THE RULE, AND IT IS THE THIRD IN THIS FAMILY: A COVERAGE COUNT READ OFF THE `machine`
> COLUMN IS A CLAIM ABOUT THE COLUMN. The only instrument that measures coverage is a
> mutation with the whole suite behind it.** Every other position in §3.2's ranking was
> assigned the same way and none of them has been measured. Read §3.2's note.

**And a second finding, smaller and worth keeping.** Of the fourteen already caught, **two —
`A` and `α̂` — were caught by NOTHING BUT the instrument-reruns-to-itself test.** That test
regenerates the artifact and compares, so it catches a *hand-edit* and is blind to a number
**legitimately re-derived** by a changed instrument, which is the failure mode §4 names.
**A reproducibility pin is not a freeze.** `test_reg010_sec4_frozen_numbers.py` holds the
fifteen as literals for that reason, beside the derived-from-artifact document anchors rather
than instead of them: a check that only asserts the document agrees with the artifact goes
green when both move together (`-38`).

## 2c · Cell (b)'s ranking, MEASURED — and the harness that would have faked the answer (`-47`)

> **`-46` MEASURED THE TOP OF §3.2's RANKING AND FOUND ITS WARRANT WRONG BY ELEVEN, THEN
> RULED THAT THE RANKING IS NOT EVIDENCE. `-47` MEASURED THE REST OF IT. NINETEEN PROBES,
> ONE PER RANKED POSITION AND ONE PER LIMB: EIGHTEEN GREEN.**

Every remaining position in §3.2 was assigned the same way C42's was — by reading the
`machine` column — and none had been measured. `scripts/mutation_control.py` now carries a
probe for each, so this is a number rather than a sentence:

| §3.2 position | probes | caught | what the one red was |
|---|---|---|---|
| 1 · C07 amended-after-result | `R1` | **0/1** | — |
| 2 · C26 unqualified *impairment* · the count beside each ratio | `R2a` `R2b` | 0/2 | — |
| 3 · C44 / C46 / C41, the **supersession** limb `-46` left unmeasured | `R3a` `R3b` `R3c` | 0/3 | — · *re-measured 0/3 at `469012b` by `-49`, then built; §2e* |
| 4 · C10 the re-ask labelled `E4` | `R4` | 0/1 | — · *re-measured 0/1 at `11b3b10` by `-50`, then built with three more doors `R4b`/`R4c`/`R4d`; §2f* |
| 5 · C16 / C20 / C23 / C25 / C30 forbidden claims | `R5a`–`R5e` | 0/5 | — |
| 6 · C45 `R_MIN` promoted · the band rule re-chosen | `R6a` `R6b` | **1/2** | `test_reg012_band_edge_phase.py::test_the_population_is_the_cited_tables_own` |
| 7 · C01–C04, C06 reportable-at-all | `R7a`–`R7e` | 0/5 | — |

**HOW MANY POSITIONS THE MEASUREMENT MOVED: ZERO.** Every one of the seven is as unguarded
as the ranking said, and the single red is incidental in the precise sense `-46` ruled on —
`test_the_population_is_the_cited_tables_own` asserts
`art["occupied_bins_reproduced"] == cited["profiles"][art["reading"]]["occupied"]`, a
*consistency* check between two artifacts. It goes red because promoting `R_MIN` breaks a
cross-reference, and it would go green on a re-run that moved both together (`-38`). It is
not about promotion and **C45's grade stays ADJACENT.**

> **AND THAT IS THE FINDING, NOT A FORMALITY. A METHOD THAT IS WRONG AND MOSTLY RIGHT IS
> THE WORST KIND, BECAUSE ITS CONFIRMATIONS HIDE ITS COUNTEREXAMPLE.** Reading coverage off
> the `machine` column gave the right answer at seven of eight positions and a wrong one —
> by eleven — at the eighth, and there is no way to tell from the column which kind you are
> holding. Seven greens do not license the eighth; they are what made it invisible for two
> sessions. **A confirmed ranking and an unverified ranking look identical until you run the
> probe, and the probe is now two minutes.**

**THE HARNESS WAS THE FIRST FALSE GREEN, AND IT WAS FOUND BEFORE THE FIRST PROBE RAN.**
`mutation_control.py` as `-46` shipped it excluded `.git` from every scratch copy. ~~Nine tests~~
**Fourteen** tests
in this estate skip with *"not a git work tree"*, and one of them is the only machine
anywhere near C07 — §3.2's **item 1**. **That machine is
`test_reg001_sec5_no_amendment_after_result.py`, measured from `R1`'s catcher list in `-51`;
`mutation_control.py`'s docstring named a different file here until `-51` corrected it, and
that uncorrected copy is what `-50`'s pre-measurement inherited. See §2g.** Under that harness
`R1` would have returned green
while proving nothing, because the harness would have deleted the only candidate guard and
then reported its absence as the measurement.

> **A MUTATION THE HARNESS CANNOT SEE REPORTS EVERY GUARD IN THE UNSEEN PART OF THE ESTATE
> AS ABSENT.** `-37` found that a mutation which does not mutate reports a guard as weak;
> this is that tell one level up, inside the instrument built to catch it. `.git` is now
> copied on request and `R1` was re-run under a real work tree before C07's guard was
> written. The same finding retired the cloud's two-tarball stanza: a source tarball without
> `.git` drops exactly the axis nobody had probed.
>
> **AND THE COUNT ITSELF WENT STALE, WHICH IS THE `-46` TELL A FIFTH TIME.** `-47` wrote
> *"nine tests · 990/999"*; it was true then. Measured at `142d386` by `-50`: **1034 passed,
> 14 skipped, across SIX files** — the suite grew and the sentence did not. It is corrected
> above rather than softened, and the durable repair is in `mutation_control.py`'s docstring:
> **the number is replaced by the one command that produces it.** A count in prose is a
> claim; a command is an instrument. `-51`'s residual (§4 item 6) is therefore **13 tests,
> not 8** — `R1` spent one of the fourteen.

**C07 is built** — `tests/test_reg001_sec5_no_amendment_after_result.py`, and `R1` is red
with exactly one catcher, the guard written for it. The other six positions are unchanged in
rank and now rest on a measurement instead of a column.

## 2d · C26 built — and the document's compliance was right for the wrong reason (`-48`)

> **THREE HANDOFFS DESCRIBED `RESULT-REG-006` AS CARRYING *"impairment"* ELEVEN TIMES,
> *"EVERY ONE OF THEM QUALIFIED"*. IT CARRIES IT TWELVE TIMES AND TWO ARE BARE. THE
> DOCUMENT IS COMPLIANT ANYWAY — FOR A REASON NOBODY HAD WRITTEN DOWN.**

The tee-up's premise was that limb A is a regex requiring every occurrence to be qualified.
Built that way the guard is **RED on the real document**, at:

- *"Test goodwill first and the impairment is \$700"* — KPMG *Handbook* Example 4.4.10,
  narrated. The \$700 is KPMG's arithmetic and not a measurement of this study.
- *"1,400 firms recording an impairment"* — the 8-K Item 2.06 population, in both
  `REG-006` §5 and `RESULT-REG-006` §3. Here the bare word is **doing honest work**: it
  means *any* impairment, tagged or folded, which is the undifferentiated thing Q1 exists
  to say the threshold cannot separate. Qualifying it would make the sentence wrong.

What saves both is the referent `-45` restored: **the clause reads *never appears IN IT
unqualified*, and *it* is the file's own statistics.** So the discriminator is not *is this
occurrence qualified* but *is this occurrence naming a statistic* — and Q1's own third
conjunct says what kind of statistic it means: one with a count of firm-periods behind it, a
ratio. The guard fires on a bare `impairment` sharing a sentence with a ratio token, which is
exactly probe `R2a`'s insertion and neither of the two sites above.

> **A GUARD BUILT FROM A HANDOFF'S CHARACTERISATION OF A DOCUMENT WOULD HAVE SENT THIS
> SESSION TO REPAIR A COMPLIANT WITNESS.** `-44` the `machine` column, `-45` the `source`
> column, `-46` the ranking prose, `-47` the harness and the DO-NOT list, `-48` the tee-up's
> reading of the document it was teeing up. **Five sessions, five times, the estate's prose
> about itself. Measure the artefact, not the sentence that sent you to it.**

**And limb B is bounded, not clean.** *"The count of firm-periods behind each ratio is
printed next to the ratio"* is a **placement** rule (C29's shape), so the count has to be in
the row. §2's headline table prints `events`, `firm-quarters` and `N_co`; §2.1's PP&E table
prints `4 obs` / `14 obs`; §3's slopes print `n = 417` / `n = 318`. **§2's six-row
internal-control table prints twelve ratios and not one count**, and the counts exist — the
`obs` column of each pair block in `RESULT-REG-006-ladderC-run.log`. Printing them into that
table edits a witness, which the `-37` precedent says is a dated addendum's job and not a
test's, so the guard **bounds** it: the six rows are pinned, an unpinned seventh goes red, and
a pinned row that acquires a count goes red saying SHRINK ME. Carded, not repaired.

**A named residual, so nobody inherits it as a silence:** §2.2's four discovered couplings
(0.00×, 3.27×, 7.70×, 6.33×) are reported in prose with p-values and no counts. *Next to* is
unambiguous inside a table row and a judgement call in a paragraph, so they sit outside the
locator's scope and **nobody has adjudicated them.**

## 2e · The supersession family built — one prohibition, two discriminators (`-49`)

> **THE TEE-UP SAID *"ASSERT BOTH DOCUMENTS EXIST AND THAT THE LATER ONE CARRIES NO
> SUPERSESSION CLAIM."* THAT IS ONE PREDICATE, AND THE ONE PREDICATE IS RED ON ALL THREE
> COMPLIANT DOCUMENTS.**

C44, C46 and C41 say the same thing about three objects — *a later measurement stands beside
an earlier verdict and never in place of it* — so they share a file. They do **not** share a
discriminator, and finding that out was the session:

- **C44 · the REFERENT** (`-45`'s lesson, one domain over). `CONSTRUCTION-REG-009` R3 forbids
  superseding **`-31`'s count**. A bare verb scan returns three sites in
  `RESULT-REG-009-band-count-filled.md`, all lawful, because each verb's object is something
  else: §0's *"the measurement replacing both brackets"*, §6's *"the conditional is REPLACED …
  by the measured outcome"*, §6's *"a bound that the measurement has superseded"*. The object
  is the discriminator.
- **C46 / C41 · the POLARITY.** `RESULT-REG-010` names the mirror and names P3 precisely in
  order to refuse them — *"The mirror is not promoted, under this outcome or any other."* ·
  *"It does not re-score P3, which failed and stays failed."* A referent test cannot tell a
  refusal from a promotion. An unnegated clause can.

**AND THE RESOLUTION IS THE LOAD-BEARING CHOICE, RUNNING THE OTHER WAY FROM §0's WARNING.**
§0 records `-41`'s tell that *a grade applied at paragraph resolution against a sentence-level
rule is a false green*. Here the danger is one notch finer. At **sentence** resolution C44's
detector is RED on the compliant document, because §0's opening sentence carries a reference
to `RESULT-REG-009-band-count` and the verb *replacing* — and is lawful. At **clause**
resolution (splitting on `.!?;`, an em-dashed aside, a colon) the verb and the referent fall
in different clauses at every lawful site, and the detector is clean on the document and red
on `R3a`'s exact insertion. That sentence is pinned as `LAWFUL_NEAR_MISS` with a second
assertion that its clauses have not fused, so a rewrite is read by a human.

> **A COPIED `own_voice()` HELPER WOULD HAVE MADE C44 VACUOUS, AND ONLY THE `-43` NON-VACUITY
> TEST WOULD HAVE SAID SO.** `-48`'s helper strips inline code for a reason correct in its own
> file — *"`GoodwillImpairmentLoss` is an XBRL element, not the word `impairment`"*. This
> estate writes cross-references in backticks, so `` `-31` `` **is** inline code: stripping it
> deletes the referent from the lawful sites and from `R3a`'s forbidden insertion alike, and
> the detector then reports zero on both. **An own-voice filter is not a portable utility; it
> is tuned to what the constraint's discriminator has to read.** `-44` said copy helpers
> rather than import them; this is the case that shows copying is not merely tidier.

**Six probes, six reds, and the ownership is legible.** `R3a`/`R3b`/`R3c` (the prose limbs)
each have **exactly one** catcher, all in the new file. `R3e`/`R3f` delete the document's own
refusal sentences — C49's shape, `-44`: *an absence guard cannot express X-not-merely-Y* — and
each has exactly one catcher. `R3d` deletes `RESULT-REG-009-band-count.md` and has **six**: the
owned presence assertion, and the five `test_reg010_sec4_frozen_numbers.py` reds `-46` measured
and correctly called incidental. The grade is written off the owned ones.

**A defect this session introduced and caught in its own probe run**, recorded because the
mechanism generalises: the two over-breadth tests first asserted *the detector finds nothing
in document + quotation*. On `R3a`'s mutant that assertion is **also** red — the document is
violating, so the detector correctly finds the violation, and an over-breadth test reads as an
over-breadth defect the guard does not have. `-39`'s tell, in a new place: **a self-test whose
predicate is ABSENCE turns one defect into two red lines and buries the one that names it.**
The predicate is now CONTRIBUTION — *the quotation adds no hit* — which is true on a violating
document and on a clean one, and it removed a spurious co-catcher from three probe rows.

## 2f · C10 built — and the correction that lived in a handoff and never reached the estate (`-50`)

**C10 is `FOR`.** `tests/test_reg002_sec5_e4_extension_label.py`, three limbs, four probes,
`R4` `R4b` `R4c` `R4d` green before and red after. The build is unremarkable. Three things
found on the way to it are not.

### The estate kept the wrong cell after the handoff recorded the right reading

`-49` spent four tool calls pre-measuring C10 so `-50` would not inherit an unchecked
characterisation, and its finding was exact: **`RESULT-REG-002` names `E4` four times and
only one of them is the re-ask.** A guard requiring every occurrence to carry the label is
red on a compliant document at three sites.

That correction went into the handoff. **It never went into this file.** C10's `resolution`
cell still read *"every mention"* — the precise reading `-49` had disproved — and its
`governed quantity` cell still read *"E4"*, the token, rather than the substitution. A
session that built C10 from its own row, as every session is told to, would have built the
guard that is red on three lawful sites, and `-49`'s measurement would have been sitting in
a handoff two commits away saying so.

> **A CORRECTION THAT LIVES ONLY IN A HANDOFF HAS NOT BEEN MADE.** The handoff is a message
> to one session; the inventory is the estate. `-44` found a column that was a coverage
> claim nobody verified, `-45` a `source` column, `-46` the ranking prose, `-47` the harness,
> `-48` a handoff's characterisation of a document, `-49` a handoff's design for a guard.
> **`-50` adds the delivery: a measurement can be right, be written down, and still not
> arrive.** The cells are corrected above — `governed quantity` is now *the α = 0.35
> substitution, not the token `E4`*, and `resolution` is *sentence*.

### The resolution knob is the same knob as `-49`'s and it turns the other way

`-49` built C44 at **clause** resolution because at sentence resolution its detector was red
on a compliant document. C10's governed sentence is

    That substitution is labelled in the script, in the manuscript and here as an
    **extension of** REG-002 E4 rather than as the registered test.

and `R4` mutates its tail to *"and here as REG-002 E4, the registered test."* The referent
and the token are separated by **commas only**. Measured both ways before a line was written:

| resolution | real document | `R4` mutant |
|---|---|---|
| **sentence** | 0 | **1** ← built here |
| comma-clause | 0 | **0** ← vacuous, and silently so |

**So the unit is not a preference and it is not portable.** For C44 the wrong unit was a
false RED, loud and self-announcing. For C10 it is a false GREEN. `-49` said pick the
resolution deliberately and say so in the docstring; the sharper form is **measure it on the
probe, in both units, and pin the table** — `test_the_resolution_choice_is_pinned` holds it.

### The tee-up's remedy for the third surface is necessary and not sufficient

C10's witness says the label travels *"in the script, in the manuscript and here"*. `-49`
warned that scanning `scripts/` returns ~88 hits *"and essentially all of them are
`# noqa: E402`"*, and prescribed a word boundary excluding `E40x`. Measured at `11b3b10`:

    substring `E4`            90
    of which `noqa: E402`     61      ← the boundary removes these
    residual                  29      ← ALL of them true \bE4\b, across SEVEN files

**"Essentially all" is 68 %.** The 29 survivors are the estate's **local exhibit labels**,
reassigned per script: `wt085`'s E4 is *news collapses the continuum*, `wt086`'s is *the
level*, `reg012`'s is *phase rigidity*. Only 8 of the 29 are REG-002's. So the word boundary
is necessary and leaves 21 false positives; **only scoping to `wt088_disclosed_ladder.py`
makes the third surface scannable at all**, and `test_the_third_surface_scope_is_warranted`
pins that as three numbers so the scope cannot decay into a habit nobody can defend.

*Generalisable, and it is `-43`'s unregistered-contains-registered lesson one level out:*
**a homograph count is not a homograph audit.** Knowing what the noise IS does not tell you
how much of it the fix removes, and a remedy sized by inspection was off by a factor of
three here.

### The honest correction, on myself

The first draft of this file shipped four self-tests with **ABSENCE** predicates — the exact
defect `-49` banked one session earlier — and the sweep put them in every catcher list:
`R4` had four catchers where it should have two, `R4b` four where it should have one, `R4c`
four where it should have one. Two needed `-39`'s already-violating skip, one needed to stop
re-asserting limb A, and one needed to skip rather than assert when a *different* probe
deletes the sentence its anchor lives in. **Found in the measurement, fixed before the
grade** — and the reason it was found is that the probe sweep is two minutes and was run
twice rather than once (`-49`'s G-COACH-5 strength, spent again and earning again).

## 2a · The counts, recomputed

`tests/test_constraint_inventory_selfconsistent.py` parses §1's table and requires this block
to match it. It exists because the sentence it replaces — *"nine of the fifty already had a
machine"* — was a count of a column in this file, stated in prose, wrong, and load-bearing for
two sessions.

> **`machine:TRIPWIRE` IS NOT A COVERAGE GRADE AND MUST NOT BE ADDED TO ONE.** Only **FOR**
> and **BINDS** mean a constraint is guarded. `-45`'s three tripwires moved C09, C17 and C36
> from `none` to `TRIPWIRE`, and moved **none of them out of cell (b) or out of reader-only**
> — the cells in §3 are unchanged at 10 / 33 / 3 / 4. What changed is that somebody is now
> guaranteed to be asked. `tests/test_tripwire_class_is_registered.py` asserts that no row
> ever carries a FOR or BINDS grade against a `test_tripwire_*` file.

| grade | n |
|---|---|
| rows | 50 |
| recog:MECH | 35 |
| recog:PROXY | 8 |
| recog:READER | 3 |
| recog:n/a | 4 |
| machine:FOR | 14 |
| machine:BINDS | 3 |
| machine:PARTIAL | 2 |
| machine:ADJACENT | 7 |
| machine:TRIPWIRE | 3 |
| machine:none | 21 |

---

## 2g · The git axis probed at last — and the harness that called its loudest red a green (`-51`)

> **THE INSTRUMENT REPORTED `[GREEN]` FOR A MUTATION THAT STOPPED THE SUITE FROM COLLECTING
> AT ALL. IN THIS FILE'S VOCABULARY, GREEN MEANS *NO GUARD EXISTS*.**

`-47` found that a harness which deletes `.git` reports every git-gated guard as absent, made
`.git` opt-in, and set `{"git": True}` on exactly one probe. Four sessions later that was still
the only one. Fourteen tests skip without a work tree, `R1` spends one, and **the other
thirteen had never had a mutation run against them** — the only place the estate had proof its
instrument was blind. `-51` built `G1`–`G13` and ran the sweep twice.

### The finding: a red the harness could not PARSE was reported as a guard that does not exist

`G8` mutates a **module** — the registered `TIER_TAGS` block in `edgar.py` — and is the first
probe in this estate ever aimed at one rather than at a document. Three modules reference
`TIER_TAGS` by name, so the import died, pytest reported the affected files as `ERROR` and
stopped at collection having run no test at all. `run_probe` parsed lines matching
`^FAILED (tests/\S+)`, found none, and printed:

```
[GREEN]  G8  edit the registered TIER_TAGS block [git]
```

**The instrument was anti-monotonic in severity: the more damage a probe did, the cleaner its
green.** A quiet mutation yields a parseable red; a catastrophic one yields an unparseable
green — and green is the state that licenses *"write a guard, there is none"*.

This is `-37`'s tell at the third level. `-37`: a mutation that does not mutate reports a guard
as weak. `-47`: a mutation the harness cannot **see** reports every guard in the unseen part of
the estate as absent. `-51`: **a red the harness cannot PARSE does the same, and the parse — not
the mutation, not the coverage — is what failed.** Every previous probe edited a document or a
JSON file, which cannot break an import; the blindness was real from the day the harness
shipped and simply had nothing to reveal it.

**Repaired, and given a machine** (`-35`'s ruling: do not soften a sentence that turns out to be
false — make it true, then give it a machine): `-rf` → `-rfE`; the recogniser is hoisted to
`CATCHER_RE` and matches `ERROR` as well as `FAILED`; and `is_unparsed_red(rc, catchers)` gives
*did-not-complete-and-nothing-attributable* its own printed state, which is **not** green.
`tests/test_mutation_control_reads_errors.py` pins both halves separately, because fixing only
the recogniser leaves the defect reachable through a collection stop. Its assertions are
CONTRIBUTION-predicated (`-49`/`-50`), never presence.

**No recorded grade moved.** The five greens the ranking rests on — `R5a`–`R5e`, §3.2 item 5 —
were re-run under the fixed harness and all five returned **rc = 0**: the suite ran to
completion and passed. Genuine greens, and the ranking stands. That check is the point: a
harness repair is a claim about every measurement ever taken with it.

### The second finding: a right total hiding a wrong attribution

`-50`'s pre-measurement of this at-bat said *"`R1` spent one of the fourteen
(`test_registrations_precede_their_instruments.py`)"*. `-51` ran `R1` and read the catcher
list: its **sole** catcher is
`test_reg001_sec5_no_amendment_after_result.py::test_the_registration_was_not_amended_after_its_result_commit`.
The other file is a guard on a different invariant and its own docstring says it *"cannot see a
registration edited after its result existed"* — which is precisely C07.

`-47` had already diagnosed this exact confusion and corrected it, in **§2b of this file**
(*"the row inherited the file because the names rhymed"*) — and left the identical claim
standing in `scripts/mutation_control.py`'s module docstring, which the handoff's ORIENT list
tells every session to read **before grading anything**. `-50` read it, believed it, propagated
it. **A CORRECTION APPLIED TO ONE ARTEFACT WHILE A SECOND ARTEFACT ASSERTS THE SAME CLAIM IS A
CORRECTION WITH A LIVE RESERVOIR** — and the reservoir is usually the instrument, because this
estate grades documents and merely reads instruments. `-50`'s rule was *edit the artefact, not
just the handoff*; the corollary is **grep the CLAIM, not the file.**

Note what did not catch it. **The residual count was right.** `13 = 14 − 1` is correct whichever
test the 1 is, it was computed by running the command rather than quoting prose, and it is
re-verified here (1034 passed / 14 skipped without `.git`, unchanged). **A right total is what
makes a wrong attribution invisible.** The corrected split by file is below.

### The thirteen, measured — the count was right, the map was not

| file | git-gated | probe | catchers | reading |
|---|---|---|---|---|
| `test_registrations_precede_their_instruments.py` | 4 | `G1` `G2` `G3` `G12` | 1 · 3 · 3 · 196 | **4 unprobed before this session, not 3** |
| `test_backups_are_ignored.py` | 3 | `G4` `G5` `G6` | 1 · 1 · 1 | three limbs, three clean owns |
| `test_pin001_code_state.py` | 3 | `G7` `G8` `G9` | 1 · 3 · 2 | `G8` is the module probe above |
| `test_reg001_sec5_no_amendment_after_result.py` | 2 | `R1` (`-47`) + `G10` | 1 · **0** | **1 unprobed before this session, not 2** — `R1` is here |
| `test_reg012_sec6_sec47_frozen.py` | 1 | `G13` | 1 | the catcher is **not** the git-gated test |
| `test_manuscript_shas_are_instrumented.py` | 1 | `G11` | 1 | owned |

**Eleven of the thirteen now have a probe; nine of those are isolating.** The remaining two are
recorded as measurements, not as gaps — `-46`'s rule, that what a probe *cannot* reach belongs
in the row:

* **`test_both_documents_are_in_history` is unreachable from the working tree, and its own
  docstring said otherwise.** It read *"a rename that empties the check must be loud"*.
  Measured: `_first_commit` is `git rev-list HEAD -- <path>`, a pathspec matches commits that
  touched the path **in history**, and after `G10` renames `RESULT-REG-001.md` two commits
  still resolve — the suite stays green at **rc = 0**. What it actually guards is the constant
  drifting to a path that was never committed. A real guard, correctly green, wrongly described;
  docstring repaired in the same commit.
* **`test_the_pinned_digest_is_the_version_REG_012_saw` reads the blob at `ba59370`, so no move
  on the tree can reach it.** `G13` edits §4.7 at HEAD and the catcher is
  `test_section_47_is_byte_identical_to_the_pin` — a different, non-git test. **The freeze is
  owned by that test; the git-gated one is a self-consistency check on immutable history.**
  That is exactly `-46`'s freeze-versus-pin distinction, and it is now in the row rather than
  counted as coverage.

`G12` is kept and labelled **non-isolating**: it catches its target
(`test_the_scan_found_registrations_to_scan`) inside a catcher list of **196**, because the only
single move that empties a registration scan is a convention change that trips the whole estate
first. Its green would be informative; its red is not coverage. Said out loud rather than
counted (`-46`), and the `--list` description says so where a reader will meet it.

**No silent caps.** `G1`–`G13` are thirteen probes against thirteen invariants but not a
bijection: `G12` reaches the scan's non-vacuity limb, `G10` and `G13` are establishing probes
expected green. Suite: **1055 passed, zero skips** with `.git` (1048 at `142d386`; `-51` added
7). Without `.git`: **1034 passed, 14 skipped**, unchanged — the axis is probed now, not
narrowed.

## 3 · THE RECOGNISABILITY PARTITION (`-44`)

`-42` asked, in this file's definition of done: **which of the fifty are constraints a machine
could NEVER recognise, and what does the estate do about those?** `-43` answered it with three
cells — (a) has a machine, (b) could have one and nobody wrote it, (c) recognisable only by a
reader — and reported **(b) EMPTY**.

**(b) is not empty. It held thirty-three of the fifty when `-44` measured it, thirty-two since `-46` built C42's guard, thirty-one since `-47` built C07's, thirty since `-48` built C26's, twenty-seven since `-49` built the C44/C46/C41 family in one file, and twenty-six since `-50` built C10's**, and the three-cell shape is why it
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
| **machine-recognisable** (MECH·PROXY, 43) | **17** — 14 written FOR the constraint, 3 incidental and genuinely binding | **26** — the cell `-43` reported empty. 11 of them **name a machine that does not bind**: the false-green class (C10 left this cell from `none`, so the eleven are unchanged — recomputed, not assumed) |
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

**PARTIAL (2)** — C38, C43. Each binds the number and misses the prohibition.

> **THREE OF THIS ROW'S FIVE LEFT IT ON 2026-08-15.** C41, C44 and C46 are **FOR** since
> `-49` built `tests/test_reg009_reg010_supersession_family.py`; the sentence that stood
> here — *"**C44** and **C46**: neither named test opens a single `.md`"* — was true when
> it was written and is the reason the family was buildable. Their PARTIAL pointers are
> kept in §1's rows, marked incidental, because the pointer is still true and is still not
> coverage. §2e is the build.

> **HALF OF C44/C46's SENTENCE WENT STALE ON 2026-08-15 AND IS CORRECTED HERE RATHER THAN
> LEFT TO ROT.** It read *"so `RESULT-REG-009-band-count.md` can be deleted outright and
> the filled count written as superseding `-31`'s, green."* `-46` deleted the file on a
> scratch copy and ran the suite: **five red**, all of them in
> `test_reg010_sec4_frozen_numbers.py`, whose `-42` antecedent check asserts that the
> documents the freeze reads still exist. **The grades do not move.** That test binds
> C42's fifteen numbers and is blind to C44/C46's *beside, never instead of* — deleting
> the file is caught, and rewriting its claim as superseding still is not. **An incidental
> red is not coverage, which is the whole lesson of §3's two axes.** ~~The second limb —
> the supersession prose — remains unmeasured and is the live half of §3.2's item 3.~~
> **MEASURED by `-47` (`R3a`/`R3b`/`R3c`, all green), re-measured green at `469012b` by
> `-49`, and BUILT by `-49`. This paragraph's own prediction held exactly**: `-49` added
> `R3d`, which deletes `RESULT-REG-009-band-count.md`, and its catcher list is the owned
> guard plus the five `test_reg010_sec4_frozen_numbers.py` reds `-46` measured here — the
> incidental set, now visibly separable from the owned one, which is what a probe is for.

> **C42 WAS THE SIXTH, AND ITS GRADE WAS DERIVED FROM THIS COLUMN RATHER THAN FROM THE
> SUITE.** The sentence that stood here read *"names two tests that pin three of its
> fifteen"*, and `-46` measured it: **fourteen of the fifteen already went red.** The claim
> was true of the **named files** and false of the **estate**, and reading the first as the
> second is `-44`'s own lesson turned on the paragraph that states it. §2b has the
> measurement and C42's row now carries **FOR**.

> **C45's ADJACENT SURVIVED A PROBE, WHICH IS NOT THE SAME AS EARNING A GRADE (`-47`).**
> `R6a` promoted `R_MIN` in `data/reg-012-band-edge-phase.json` and one test went red:
> `test_the_population_is_the_cited_tables_own`, which asserts
> `art["occupied_bins_reproduced"] == cited["profiles"][art["reading"]]["occupied"]`. That is
> a **consistency check between two artifacts**, red because a cross-reference broke, green
> on any re-run that moved both together (`-38`). `R6b`, which re-chooses the band rule —
> R5's other limb, in R5's own words — is **green**. So C45 is ADJACENT on the measurement
> and not merely on the reading, and the incidental red must not be read as coverage.

**ADJACENT (10)** — C07 *(now FOR, `-47`; the row is kept here because the adjacent pointer
is still true and still not coverage)*, C11, C32, C34, C37, C39, C45, C50, and two that were pointer defects
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

Thirty-one entries, so this is a ranking and not a to-do list. Ordered by *what a violation
would cost times how cheaply it can be caught*, and each names the shape it should take.

> **EVERY POSITION BELOW HAS NOW BEEN MEASURED, AND THE MEASUREMENT MOVED NONE OF THEM.**
> `-46` removed C42 from this cell after finding the ranking's reason for putting it first
> (*"twelve of fifteen unpinned"*) wrong by eleven, and ruled that **a ranking read off the
> `machine` column is a claim about the column**. `-47` ran a probe for each of the seven
> positions that remained — nineteen probes, one per limb — and **eighteen came back green**.
> The single red is incidental and C45's grade did not move. **§2c is the measurement, and it
> is the reason this list may now be built from top-down without re-deriving its own warrant
> each time.** Item 1 (C07) has been built and is struck through below; before adding a
> position to this list, run its probe — `python3 scripts/mutation_control.py --only <slug>`.
>
> **What the seven greens do NOT license: reading the `machine` column again.** The column
> was right at seven of these eight positions and wrong by eleven at the other, and nothing
> visible in the column distinguishes the two. The confirmations are what hid the
> counterexample for two sessions.

1. ~~**C07 · amended-after-result**~~ — **BUILT (`-47`)**, probe `R1`, green before and red
   after: `tests/test_reg001_sec5_no_amendment_after_result.py`. It compares ancestry rather
   than dates, and asserts that REG-001 is still the only registration making the promise, so
   a second one adopting it goes red saying EXTEND ME.
2. ~~**C26 · *"the word 'impairment' never appears **in it** unqualified"***~~ — **BUILT
   (`-48`)**, probes `R2a` and `R2b`, both green before and red after, one catcher each:
   `tests/test_reg006_sec3_q1_two_limbs.py`. **It is not the pure regex this line said it
   was**, and the entry is left in place with the correction attached because the wrong
   description is the instructive part: the constraint's referent (`-45`: *it* = the file's
   own statistics) is what decides which occurrences are in scope, and a regex over every
   occurrence goes RED on a compliant document. §2d.
3. ~~**C44 / C46 / C41 · the "beside, never instead of / never promoted / does not re-score"
   family**~~ — **BUILT (`-49`)**, `tests/test_reg009_reg010_supersession_family.py`, probes
   `R3a`/`R3b`/`R3c` green before and red after with **exactly one catcher each**, plus three
   new probes `R3d`/`R3e`/`R3f` for the presence limbs. **The description above was right
   about the shape and wrong about the mechanism**, and the entry is left in place with the
   correction attached because the wrong half is the instructive half: *"assert … that the
   later one carries no supersession claim"* is one predicate, and the family needs **two** —
   a REFERENT test for C44 (whose lawful uses of *replace* have different objects) and a
   POLARITY test for C46/C41 (whose lawful sites name the mirror and name P3 **in order to
   refuse them**). A single predicate is red on all three compliant documents. §2e.
4. ~~**C10 · *"labelled an EXTENSION of E4 throughout, never as E4"*** — probe `R4` green.
   C21's exact shape, one document over, and C21 is the one that was not clean. Two limbs:
   wrong label, missing label.~~ — **BUILT (`-50`)**,
   `tests/test_reg002_sec5_e4_extension_label.py`, probes `R4`/`R4b`/`R4c` plus a new third
   surface probe `R4d`, all green before and red after. **The description above was right
   about the two limbs and silent about the thing that decides them**, and it is kept for
   the same reason item 3 is: C21's shape carried over the *audit* lesson (a labelling
   constraint's second door is the wrong label) and not the *scope* one. C10 governs the
   **substitution**, not the token — three of the document's four `E4` mentions are lawful —
   and the two limbs are separated at **sentence** resolution, where C44's needed the clause.
   A third limb was needed for the script surface the constraint's own witness names. §2f.
5. **C16 / C20 / C23 / C25 / C30 · the forbidden-claim family** — probes `R5a`–`R5e`, all
   five green, each having asserted that registration's own forbidden claim in the document
   it governs. Five constraints, one claim-scanner shape, already built twice (C19, C24).
   Feed each registration its own forbidden claim before trusting the green (`-43`).
6. **C45 · `R_MIN` not promoted** — probe `R6b` green; `R6a`'s red is a cross-artifact
   consistency check and not coverage (§3.1). Two assertions: `art["reading"]` and
   `art["band_rule"]` are the registered ones.
7. **C01–C04, C06 · the reportable-at-all family** — probes `R7a`–`R7e`, all five green;
   deleting the drop accounting, the negative control, the permutation p, the power statement
   or the censoring row leaves the suite silent. Presence guards, low cost, low risk, and
   C02's is conditional (assert the antecedent, `-42`).

### 3.3 · The three that are reader-only, and the adjacent check for each

This is the half of `-42`'s question that has a real answer, and the deliverable is the
sentence *saying which is which* — the adjacent check is never the constraint.

| | the constraint (reader) | the adjacent check (machine) | what the gap is |
|---|---|---|---|
| **C36** | a refusal is *"stated in the same sentence as the number that caused it"* — the reader's worry is §7's forty-seven-row ledger diluting the §4.5 row that **refused in 400 of 400 draws** | the registration's literal requirement: the refusal and its number share a sentence. `RESULT-REG-009` §4 complies, and this is checkable | the registration says nothing about the row sharing a table with thirty rows that risked nothing. **A machine can check the sentence; only a reader can see the table.** Jason's call |
| **C05** | *"the next move is not a third instrument on the same data"* | no new instrument script targets the lag gradient; T2's card stays closed | the constraint is about a research *decision*, made by whoever holds the next at-bat. There is no artifact to read, because the artifact would be the violation |
| **C18** | S3's general search *"is teed up in the handoff and is not attempted in this session"* | the handoff carries the tee-up; no S3 instrument exists | *"in this session"* is unaddressable — a machine reading the repo cannot see which session did what, only what is there now |

Three PROXY rows sit just inside the boundary and are worth naming here because their adjacent
checks are already built and are mistaken for the constraint: **C09** (a machine can pin §4.4's
*title*; only a reader knows what a section's **headline** is), **C17** (*"may not reopen the
argument"* — a machine can freeze the argument's paragraphs, as C48 does for §4.7), and
**C37** (*"never by narration"* — a machine can require a numeral in the attribution paragraph;
whether the prose is doing the attributing is a reading).

**C09 and C17 now have tripwires on exactly those adjacent facts (`-45`, §3.4), and the
distinction this paragraph draws is the reason the tripwires say what they say.** The pin is
the title; the constraint is the headline. A red is *go and read §4.4*, never *§4.4 is wrong*.
**C37 is the obvious fourth** and is not built: its antecedent — a numeral leaving the
attribution paragraph of `RESULT-REG-009` — is the same shape and about an hour of work.

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
   `tests/test_reg012_sec6_sec47_frozen.py`, anchored at `ba59370`, the commit that registered
   `REG-012`. **The anchor records which version it froze**, and a git test reads §4.7 out of
   that commit and requires it to hash to the anchor — otherwise the freeze silently re-anchors
   to whenever somebody last ran the file, which is a snapshot wearing a freeze's clothes.
   **`-43` wrote that anchor and the working-tree freeze as ONE constant, and the red message
   told the next session to re-pin it — an instruction this same file forbids**, since the git
   test nails the constant to `ba59370` and no single value can also equal an edited §4.7. The
   remedy could be executed zero times, so the first warranted edit (`6314302`, `ASC
   350-30-35-15`) wedged the guard red and it stayed red for four days under a gate that
   reports `PASS` without running a suite. `-65` split it: `SEC_47_AT_REGISTRATION` is
   immutable, `SEC_47_CURRENT` follows an `AMENDMENTS` ledger, and each amendment is checked
   against git for having moved §4.7 to the digest it claims — a warrant is checkable or it is
   decoration. Probes `G14` and `G15` fire the two doors the ledger opens. `WT-096`.
4. **C24 · the fitted lag distribution may not be claimed to transfer beyond the sample's
   classes.** ✅ **MECHANISED** — `tests/test_reg005_sec7_lag_transfer.py`. Clean, and the file
   says out loud which half of its predicate is live: the manuscript names the fit, makes
   extension claims about other things, and never pairs them. Two traps found while building it:
   `travels` is not an extension verb (§4.10's *"travels with the lag distribution rather than
   with the filings"* is the paper making this constraint's own point), and a scope test keyed on
   the word *sample* passes `REG-004` §6's own example of the violation.
5. **C36 · a refusal is stated in the same sentence as the number that caused it.** This is the
   constraint underneath the presentation item on the board — §7's forty-seven-row ledger dilutes the
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
   thing at issue is what a referee's eye does with a forty-seven-row table, which is not a fact
   about the repo.
3. **A TRIPWIRE — ~~the one the estate keeps inventing in prose and never builds~~. BUILT IN
   `-45`.** All three below exist, are marked as a class in three places, and are green:
   `tests/test_tripwire_c09_sec44_headline.py` · `tests/test_tripwire_c17_sec44_argument.py` ·
   `tests/test_tripwire_c36_sec7_ledger_shape.py`, registered by
   `tests/test_tripwire_class_is_registered.py` and the `tripwire` marker in `conftest.py`.

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

Three tripwires were owed. **`-45` built all three**, and what each turned out to be:

* **C09** — `tests/test_tripwire_c09_sec44_headline.py`. §4.4's heading pinned byte-for-byte,
  and the knife-edge's paragraph position in the abstract pinned **as a floor**: moving earlier
  is promotion and fires, moving later or being pushed down by an inserted paragraph is not and
  does not. A tripwire that fires on any edit to the abstract is noise, and noise is how a
  tripwire dies. It also asserts its own warrant — `REG-002` E2's clause, **and**
  `RESULT-REG-002`'s E2 row still reading FIRED — because C09 is conditional and a re-run that
  put δ₃\* above 0.010 would leave the file guarding nothing, silently (`-42`'s rule, applied
  to the tripwire rather than to the guard). *The heading is `###`, not the `##` two handoffs
  said.*
* **C17** — `tests/test_tripwire_c17_sec44_argument.py`. **Not** a freeze: `REG-003` §7
  *licenses* one number and the sentences carrying it, so a byte pin would go red every time
  the registration did exactly what it registered. The pin is over §4.4 **with every numeric
  literal masked** — a number moving is silent, prose moving is not. Its blind spots are in
  its docstring, and the first is that section cross-references are numerals too.
* **C36** — `tests/test_tripwire_c36_sec7_ledger_shape.py`. §7's ledger column tuple and row
  count (**47**), and the red message says *ask Jason, once*, with the re-pin path as the way
  his answer gets recorded. It does not grade the presentation and must not be improved into
  doing so.

**Registering the class, which is the part that keeps them alive.** A tripwire is not a guard,
and a suite that cannot tell them apart will eventually have one deleted as a false alarm. The
class is marked in **three** places — the file name `test_tripwire_*.py`, a `tripwire` pytest
marker registered in `conftest.py` (so `-m tripwire` selects the class and `-m "not tripwire"`
excludes it), and a `TRIPWIRE` grade in §1's `machine` column — and
`tests/test_tripwire_class_is_registered.py` requires all three to agree in both directions,
because any one alone rots quietly: a file renamed, a marker dropped in a tidy-up, a row
re-graded. **`TRIPWIRE` IS NOT COVERAGE**, and that is asserted rather than trusted: no row may
carry a FOR or BINDS grade against a `test_tripwire_*` file. The three cells in §3 are
unchanged — C09 and C17 are still in cell (b), C36 is still reader-only. What changed is that
somebody is now guaranteed to be asked.

**The rule to carry forward: a constraint a machine cannot recognise gets a machine on its
ANTECEDENT and a human on its consequent — and a guard whose red message names a violation
when it should name a re-read teaches the next session to suppress it.** `-42` learned the
same lesson about conditional constraints in the other direction: different failures, different
messages. **`-45`'s addition: the antecedent has to be the one a reader would actually act on.**
Every one of the three had a cheaper, wronger version available — freeze the section, fire on
any abstract edit, count the rows and grade them — and each of those would have been green
today and deleted within three sessions.

---

## 4 · What this file is not

It is not a licence to re-open anything in `HANDOFF` §2. Where a constraint is marked *closed by
ruling*, the ruling governs and this row is a pointer to it. It is not a substitute for reading
the registration: every quotation here is short enough to have lost its context, and the
verdicts were reached by reading the sections, not the greps.

And it is a snapshot. **A constraint's status can change without the constraint changing** —
three of these fire on an outcome, and C12 sat unchecked for exactly that reason. Re-read the
`live?` column against any new `RESULT-*`.
