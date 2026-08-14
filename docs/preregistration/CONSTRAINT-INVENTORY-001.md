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

| # | source | the constraint | governed quantity | resolution | scope | live? | verdict | machine |
|---|---|---|---|---|---|---|---|---|
| C01 | `PRE-001` §9 | every dropped event counted in one of ten named buckets; *"saying what we sampled and what we dropped is a condition of the result being reportable at all"* | drop accounting | document | RES | yes | `RESULT-001` §2 *Drop accounting (PRE-001 §9)* tabulates them — **compliant** | none |
| C02 | `PRE-002` §3 | permutation *z* must be centred near 0 / sd near 1 or **no result from this pipeline is reportable** | negative control | document | MS+RES | yes | §5.3 reports it centred on zero with unit spread — **compliant** | none |
| C03 | `PRE-002` §3 | the observed *z* additionally reported as an **empirical permutation p-value** | `p` | sentence | MS | yes | §5.3 gives permutation p = 0.590 / 0.520 — **compliant** | none |
| C04 | `PRE-002` §3 | the synthetic power statement is **reported whatever happens** | power | document | MS | yes | §5.3's *"a power curve to be reported whatever happened"* — **compliant** | none |
| C05 | `PRE-002` §5 | *"the next move is not a third instrument on the same data"* | the lag gradient | document | MS+INST | yes | honoured; **T2 is carded and barred** on this ruling | none — the ruling lives in `HANDOFF` §2 |
| C06 | `PRE-002` §2 | right-censored events **reported as such** | censoring | sentence | MS | yes | §5.3/§5.4 report censoring rates — **compliant** | none |
| C07 | `REG-001` §5 | *"this registration may not be amended after the first result commit"* | REG-001 | document | RES | yes | `RESULT-REG-001` returns NO VERDICT and the file is unamended — **compliant** | `test_registrations_precede_their_instruments.py` (adjacent) |
| C08 | `REG-001` §7 | a pass licenses exactly one sentence; it does **not** license *"the price-layer result is novel — which it is not, and Wicksteed gets that credit in the text"* | novelty of the price-layer result | document | Paper I | **NO** | **the antecedent never occurred** — `RESULT-REG-001` is NO VERDICT, not a pass. Wicksteed's credit is discharged in `LEDGER` WT-066 and `ADR-001`; paper III does not carry the claim | none needed |
| C09 | `REG-002` E1 | if δ₃\* < 0.010, *"§4.4 may not report it as the section's headline"* | τ = −1 | section | MS | **YES — δ₃\* < 0.010** | δ₃\* = 0.0079 < 0.010 → **the constraint FIRES**; §4.4 is titled *"The design has a validity region, and the disclosed numbers fall outside it"* and the knife-edge is one bolded paragraph lead inside it, not the section's headline — **compliant, and this is the closest call in the table** | none |
| C10 | `REG-002` §5 | E4's re-ask is *"labelled an EXTENSION of E4 throughout, never as E4"* | E4 | every mention | RES | yes | the manuscript names no `E`-labels at all (0 occurrences); the constraint binds `RESULT-REG-002` only — **out of manuscript scope** | none |
| C11 | `REG-003` §2 | a differently-composed rebuilt sample *"may not be"* silently substituted | the sample | document | RES | yes | §5.4 reports 695 vs 688 and cites the registered reconciliation rule — **compliant** | `test_pre002_data_is_pinned.py` (adjacent) |
| C12 | **`REG-003` §3.3** | **if α̂ lands in R1/R2 the finding *"must be reported with that sentence attached, in the same paragraph, not in a limitations section"*** | α̂ | **paragraph** | MS | **YES — R1 in every cut** | **FOUR LIVE VIOLATIONS at `1e474b4`**: §4.4, §5.4's bolded lead, §7's ledger row, §9 limitation 4. Repaired by `wt108` | **`test_reg003_sec33_asymmetry.py`** (new) |
| C13 | `REG-003` §3.3 | if `d = 0` in any sensitivity cell, *"that cell is reported as UNDEFINED and never as a number"* | α̂ per cell | cell | MS+RES | **NO** | `d` is 228–613 in every published cell; the antecedent never fired — **not live** | none needed |
| C14 | `REG-003` §4.3 | *"direction is reported as part of the result, never absorbed into a p-value"* | N_co | sentence | MS | yes | §5.4 reports clustering *above* the interval in both universes with the direction named — **compliant** | none |
| C15 | `REG-003` §7 | *"no sentence anywhere may round it"* — α̂ to *"the recognition rate"* | α̂ | **sentence** | MS | yes | six violations found and repaired by `-41` | **`test_reg003_sec7_rounding.py`** |
| C16 | `REG-003` §7 | *"rejecting independence in §4 does not rescue PRE-001"* | the lag gradient | document | MS | yes | §5.3/§5.4 draw no such inference — **compliant**; also the ruling barring T2 | none |
| C17 | `REG-003` §7 | §4.4 *"may change one number and the sentences that carry it, and may not reopen the argument"* | §4.4 | section | MS | yes | §4.4's argument is unchanged since `wt089`; `-41` and `-42` changed numbers and their sentences — **compliant** | none |
| C18 | `REG-004` §5 | S3's general search *"is teed up in the handoff and is not attempted in this session"* | the age-dependent mirror | session | INST | yes | teed up, never attempted — **compliant** | none |
| C19 | **`REG-004` §6** | **may not be claimed: *"that α_eff is 'the' recognition rate — it is a function of δ"*** | α_eff | sentence | MS | yes | **checked through both doors** (noun phrase and symbol): §4.10 names α_eff a function of δ at every site and §4.10's lead says *"three recognition rates now live in this paper and they are three different quantities"* — **compliant** | **`test_reg004_sec6_alpha_eff.py`** (new, `-43`) |
| C20 | `REG-004` §6 | may not be claimed: that the correction *"rescues PRE-001"* | PRE-001 | document | MS | yes | not claimed — **compliant** | none |
| C21 | `REG-004` §6 / `REG-005` §7 | *"unregistered robustness may be reported, labelled as robustness, and may not change a verdict"* | any unregistered cut | sentence | MS | yes | **SEVEN LIVE VIOLATIONS at `e947fb6`**, and the compliant grade above was reached through the `unregistered` keyword, which finds the site carrying the label and not the site carrying the **wrong** one. `REG-003` §3.1 A3 registers three sensitivities and §3.2 registers no cut; the 0.327 cut is filed under `RESULT-REG-003` §2's *"Unregistered robustness"* heading and the manuscript called it **"the registered adverse cut"** at four sites, with three more reporting unregistered values unlabelled. Repaired by `wt110` | **`test_reg004_sec6_unregistered_robustness.py`** (new, `-43`) |
| C22 | `REG-004` §6 / `REG-005` §7 | *"no parameter is added to the model at any point"* | the model | document | MS | yes | no parameter added — **compliant** | none |
| C23 | `REG-005` §7 | may not be claimed: that a negative result *"licenses removing §4.9's correction"* | §4.9 | section | MS | yes | §4.9 stands and §5.4 holds the lag distribution — **compliant** | none |
| C24 | `REG-005` §7 | may not be claimed: *"that the fitted lag distribution transfers to classes the PRE-002 sample does not cover"* | the lag distribution | sentence | MS | yes | §6.1's scope sentence (`-41` T5) states the covered classes — **compliant** | **`test_reg005_sec7_lag_transfer.py`** (new, `-43`) |
| C25 | `REG-005` §7 | may not be claimed: *"that the normalisation of §1 is innocuous — it is generous"* | §1's normalisation | sentence | RES | yes | binds `RESULT-REG-005` — **out of manuscript scope** | none |
| C26 | `REG-006` §4 Q1 | *"the word 'impairment' never appears unqualified"* and *"the count of firm-periods behind each ratio is printed next to the ratio"* | REG-006 statistics | every ratio | RES | yes | binds `REG-006`/`RESULT-REG-006` — **out of manuscript scope** | none |
| C27 | `REG-006` §4 Q2 | a cell with fewer than 20 firm-periods *"is reported as its count and no ratio is formed from it"* | thin cells | cell | RES | yes | binds `RESULT-REG-006` | none |
| C28 | `REG-006` §4 Q2 | the cap region's slope reported *"as a function of L/W, never as a point"* | the cap slope | sentence | MS+RES | **NO** | ladder C **failed as registered** (§7's row); no cap-region slope is reported anywhere, as a point or otherwise — **not live** | none needed |
| C29 | `REG-006` §8 | if ladder C's corrected lift lands below `REG-003`'s figure, §5.4's number is amended *"in the text where the number is — not in a footnote, and not in Limitation 9"* | §5.4's lift | **placement** | MS | **NO** | ladder C failed; no amendment was owed — **not live** | none needed |
| C30 | `REG-007` §5 | *"Λ ≈ 0 is NOT evidence for co-movement"* — stated before the run so a null cannot be sold as a finding | Λ | sentence | MS+RES | yes | the manuscript makes no co-movement claim from Λ — **compliant** | none |
| C31 | `REG-007` P4 | *"the registered claim is a sign and a significance level, nothing more"*; no threshold on Λ | Λ | sentence | MS | yes | §7's row reports the instrument as failed; no Λ magnitude claim — **compliant** | none |
| C32 | `REG-007` §9 | if Λ is withheld, *"the counts are published anyway and the withholding is named as such"* | Λ | document | RES | yes | binds `RESULT-REG-007` — **compliant there** | `test_reg007_resolution.py` (adjacent) |
| C33 | `REG-007` §4 | rebuilding the panel from `edgar.py` *"is forbidden by this registration"* | the panel | instrument | INST | yes | the committed panel is re-read — **compliant** | none |
| C34 | `REG-008` §9 | thin arms → *"reported as underpowered, the counts are published, and no significance claim is made"* | P1 replication | document | RES | yes | binds `RESULT-REG-008` | `test_reg008_instrument.py` (adjacent) |
| C35 | `REG-008` §9 | if F1's gate fails, *"no Λ is printed at all"* | Λ | document | RES | yes | binds `RESULT-REG-008` — **compliant** | `test_reg008_instrument.py` |
| C36 | `REG-009` §4 | a refusal is *"stated in the same sentence as the number that caused it"* | the δ design | **sentence** | RES | yes | `RESULT-REG-009` §4 states it that way — **compliant**. See §3: this is the constraint behind the §7-ledger presentation item on the board | none |
| C37 | `REG-009` §12 | if Ψ and Ψ_rect(α̂) disagree the difference is attributed by S and the columns, *"never by narration"* | Ψ | sentence | RES | yes | `RESULT-REG-009` attributes numerically — **compliant** | `test_reg009_ladder_inputs.py` (adjacent) |
| C38 | `REG-009` §12 | §4.4's rectangle sentence repaired *"in one of exactly two ways"*: the rate named **and the rectangle labelled asserted rather than observed** | the rectangle | every mention | MS | yes | eight *asserted rectangle* sites; the label travels — **compliant** | **`test_term001_rectangle.py`** |
| C39 | `REG-009` §12 | *"no free parameter may be introduced to reconcile Ψ with 99.7 %"* | Ψ | document | MS+INST | yes | §7's row reports 0.659 against 0.998 and reconciles nothing — **compliant** | F10, and `test_reg009_ladder_inputs.py` |
| C40 | `REG-009` §12 | §7.5's count lands *"whatever Ψ returns"*: 151/98 repaired against 55/38 as §5 collected it | §4.7's clause | sentence | MS | yes | §4.7 carries both counts — **compliant** | `test_term002_count.py` |
| C41 | `REG-010` §0 | *"P3 failed as registered and REG-010 does not re-score it"* | P3 | document | RES | yes | **closed by ruling** — do not reopen | `test_reg010_half_integer_banding.py` |
| C42 | `REG-010` §4 | a list of fifteen numbers *"this may not move"*; one new artifact, overwrites nothing | REG-009's numbers | artifact | RES+INST | yes | **compliant** | `test_reg009_band_count.py`, `test_reg010_half_integer_banding.py` |
| C43 | `CONSTRUCTION-REG-009` R2 | the fill raises *"the joinable column only"* | the fill | artifact | INST | yes | H6 refuses the run if `events_total` moves — **compliant** | `test_reg009_band_count_filled.py` |
| C44 | `CONSTRUCTION-REG-009` R3 | the count is reported *"BESIDE `-31`'s, never instead of it"* | the band count | artifact | RES | yes | two artifacts, both committed — **compliant** | `test_reg009_band_count.py` + `_filled` |
| C45 | `CONSTRUCTION-REG-009` R5 | *"no band edge, band width, floor, tag or interval rule is re-chosen in response to the number"*; `R_MIN` not promoted | the band count | document | RES | yes | **closed by ruling; unspent** | `test_reg012_band_edge_phase.py` |
| C46 | `CONSTRUCTION-REG-010` C4 | the mirror is *"computed, reported beside, never used to choose"*; *"never promoted"* | the mirror | document | RES | yes | **compliant** | `test_reg010_half_integer_banding.py` |
| C47 | `REG-012` §5 | E1 and E2 *"are reported beside it, never instead of"* the histogram E3 | the phase histogram | document | RES | yes | **compliant** | `test_reg012_band_edge_phase.py` |
| C48 | `REG-012` §6 | *"this measurement produces no new answer to §7.5's decision rule, and no sentence of the manuscript's §4.7 is changed by any outcome of it"* | §4.7 | **sentence** | MS | yes | §4.7 is unchanged since `REG-012` — **compliant**, and now pinned at `ba59370` | **`test_reg012_sec6_sec47_frozen.py`** (new, `-43`) |
| C49 | `REG-012` §7 | the shifted band count *"is refused, not merely unperformed"* | the band count | sentence | MS+RES | yes | **compliant**; the distinction is load-bearing and named in `HANDOFF` §2 | `test_reg012_band_edge_phase.py` |
| C50 | `SOURCE-001` §5 | two caveats *"must be closed before the XBRL route is called closed in general"* | the XBRL route | document | RES | yes | `SOURCE-001` is FINISHED by ruling and the general claim is not made — **compliant** | `test_source001_coverage.py` |

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
- **Nine of the fifty already had a machine**, all of them incidental: the test was written for
  a prediction or an artifact and happens to bind the constraint too. **C12 and C15 were the
  only two with a machine written FOR the constraint**, and `-41` wrote one of them. `-43`
  added four more — C19, C21, C24, C48 — so the class now has **six** purpose-built guards and
  the only unmechanised entry in §3 is C36, which is a judgement about a reader and stays
  Jason's call.
- **`-43`'s finding, which is this file's own tell turned on this file.** §0 says an inventory
  built on the keyword grep alone would have been *a plausible, shorter, wrong list*. C21's row
  was graded by exactly that door: grep `unregistered`, find §5.4's labelled 0.460, mark the
  constraint compliant. **The second door for a labelling constraint is the WRONG label, not
  the missing one** — and behind it were four sites calling an unregistered cut *registered*
  and three reporting unregistered numbers bare.

## 3 · The ones a machine could recognise — FOUR OF FIVE NOW HAVE ONE (`-43`)

Ranked by what a violation would cost. Written by `-42` as *"none of these is a defect today"*;
**that held for three of the four and not for C21**, which is the entry to read first.

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

## 4 · What this file is not

It is not a licence to re-open anything in `HANDOFF` §2. Where a constraint is marked *closed by
ruling*, the ruling governs and this row is a pointer to it. It is not a substitute for reading
the registration: every quotation here is short enough to have lost its context, and the
verdicts were reached by reading the sections, not the greps.

And it is a snapshot. **A constraint's status can change without the constraint changing** —
three of these fire on an outcome, and C12 sat unchecked for exactly that reason. Re-read the
`live?` column against any new `RESULT-*`.
