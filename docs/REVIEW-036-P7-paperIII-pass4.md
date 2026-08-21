---
new_instrument: new
instrument_name: "wt184 — `scripts/wt184_pointer_correctness.py`, A3′ MECHANISED. The AXIS is inherited: A3′, the correctness question behind A3, originates `wealthTensor-99` on paper-II (II-40) and was first applied to paper-IV BY HAND at `-100`, which then wrote as its biggest tee-up that the check should be SCRIPTED, with two rules, a negative control, section bounding at the next heading of ANY level, and `**`/`*` normalisation. This pass built exactly that and pointed it at paper-III's 244 `§N.M` references, the most in the corpus. wt133 has printed `0 unresolved` on this manuscript for twenty sessions; wt184 asks the other question and III-5 is its finding. No A1–A5 cell was filled: the grid has been closed at 15 of 15 since `-80` and A6, the docstring axis, remains parked. `scripts/wt185_paperIII_p7pass4.py`, `scripts/wt186_paperIII_promises.py` and `scripts/wt187_restatement_counts.py` are the PATCHES of record, not instruments."
new_instrument_alt: none
findings_from_new_axis: 1 of 3
findings_from_new_instrument: 1 of 3
residue_of_previous_pass: 0 of 3
shape_promise_about_artefact: 1 of 3
shape_deferral_with_empty_target: 1 of 3
shape_neither: 1 of 3
manuscript_edits: 3 of 3
consecutive_zero_passes_after_this_pass: 0
prediction_under_test: "none — `-100`'s row proposes no mechanism and makes no prediction, and this pass does not invent one to settle. See §5."
prediction_verdict: N/A
# FALSIFY THIS ROW, SIX WAYS.
#   1. `new`: `scripts/wt184_pointer_correctness.py` did not exist at the parent commit 74934b9.
#      `git log --diff-filter=A -- scripts/wt184_pointer_correctness.py` returns d162969, this
#      session. If a prior pass shipped a resolving-vs-correct CHECKER, the row should read
#      `inherited-first-application` — grep scripts/ for one and grep REVIEW-034 and -035 for a
#      claim to have built it. What they contain is the tee-up, not the tool.
#   2. `1 of 3` from the new axis: §2 credits each finding to the axis that produced it. III-5 is
#      wt184's. III-6 is A4's second question (`-80`'s move, "is there a number the paper reports
#      that no named command produces?"), and III-7 is A4 proper — RUNNING wt091 and diffing its
#      output against §4.10's table. If III-6 or III-7 traces to wt184, this row undercounts;
#      wt184 flagged neither, and §3 says why it structurally could not.
#   3. `0 of 3` residue: `git blame -L 1050,1071 74934b9 -- docs/papers/paper-III-dual-tensor/paper-III.md`
#      returns 42ca3773 on ALL THREE sites — the 2026-08-12 commit that added §4.10 and wt091 in
#      the same breath, before paper-III had had a single P7 read. Not one site blames to `-73`,
#      `-80` or `-83`. NO MECHANISM IS PROPOSED FROM THIS NUMBER; see §5 and see -77/-78 for why
#      residue is not one.
#   4. `3 of 3` manuscript edits: `scripts/wt185_paperIII_p7pass4.py` touches paper-III.md four
#      times for three findings (III-5 has two sites, a table header and a prose sentence). It
#      carries 19 post-conditions, 8 NEGATIVE, and is idempotent — run it twice. If any finding
#      is repaired outside the manuscript, the count is wrong.
#   5. the shapes: 1 promise / 1 deferral / 1 neither, on REVIEW-019 §6's two definitions
#      unchanged, against the 5/2/2 `-80` found on this manuscript and the 1/2/1 `-83` found.
#      n = 3 and this row claims only what it counted. Re-read §2 against `-79(i)` and `-79(ii)`.
#   6. `consecutive_zero_passes_after_this_pass: 0`. It is not zero because the pass found three
#      things, and §6 says what a reader should conclude from that on a manuscript whose last
#      read was eighteen sessions ago.
# Ledger of all fifteen passes: docs/p7-passes.tsv
---

# REVIEW-036 · Paper III's FOURTH independent `P7` read — the pass that ran the script the paper did not name

*`wealthTensor-101` · 2026-08-21 · parent commit `74934b9`. Paper III's first read in EIGHTEEN
sessions. **Three findings, three repairs, all landed in-pass**, plus one apparatus item carded with
its falsifier. Repair commit `d162969` (layout guard RED on purpose), recapture `6937a99`.*

**THE HEADLINE IS THAT ALL THREE FINDINGS CAME OUT OF ONE COMMAND, AND THE PAPER DOES NOT NAME IT.**
§4.10 is titled *"The shape is identified, and the price of admission is four significant figures"* —
the paper's answer to its own title. Its five-row table, its search floor, and its comparison against
the event-date interval are all produced by `scripts/wt091_lag_shape_identifiability.py`, a script
registered against REG-005, committed *after* the registration it obeys, and quoting the manuscript
in its own docstring. §11 — *Data and code availability*, which gives a runnable `Regenerate` bullet
for §3, §A.2.3, §5, §5.4 and §A.2.4 — named no command for §4.10, and the manuscript named that
script only as the bare token `` `wt091` ``, inside a clause about chronology.

Running it took six minutes and returned three defects, one of which the paper's own table already
contradicts. **The script knew what the paper claims. The paper had stopped checking.**

---

## 0 · What is NOT claimed here

**Three findings after eighteen sessions is not evidence that anything decayed.** Every site blames
to `42ca3773`, the 2026-08-12 commit that added §4.10 whole — before paper-III's first P7 read. The
passage has been wrong since it was written and three independent reads went past it. That is a
statement about coverage, not about drift, and §5 says what it does and does not license.

**Nor is this pass comparable to `-83`'s four or `-80`'s nine.** `-80` filled three empty axis cells;
`-83` read a 127-row adjudication ledger as an artefact. This pass ran one command neither of them
ran, because neither of them had a reason to: the paper does not name it, and A4 is defined as
*running the manuscript's own named commands*. **A4's coverage is bounded by the manuscript's
honesty about its own toolchain, and that is the loop III-6 closes.**

No finding below required re-running the severe test's science. Every one is checkable by a reader
with the repository, and each carries the command that kills it.

---

## 1 · THE SIX AXES, RUN BEFORE A WORD OF PROSE

| axis | what was run | scale | findings |
|---|---|---|---|
| **A1** quantifiers read forward | `python3 scripts/wt130_quantifier_sweep.py paper-III` | **902 tokens on 694 of 2 741 lines** | none |
| **A2** the failure mode the paper names, turned on the paper | REVIEW-020 §1's eight modes INHERITED, not re-derived, and the four that are mechanically checkable re-run: §11's *a registration cannot be amended by stealth* (`test_pre001_constants_are_what_was_registered` — live, `tests/test_edgar.py:21`); §7's *a guard that could not fail passing silently* (both companion guards live in `tests/test_excess_demand.py:120` and `tests/test_redistribution.py:61`, not only in the `.bak` files beside them); §11's *differential attrition manufacturing the reported null*; the References' *a reference kept for the look of the list* (wt133: 49 entries, 49 cited) | 8 modes | none |
| **A3** cross-references resolve | `python3 scripts/wt133_crossref_sweep.py` RC 0 — **244 `§N.M` refs, 38 distinct, 0 unresolved · 49 of 49 references cited, 11 explicit "cited in §N.M" claims, 0 flagged** | 244 | none |
| **A3′** cross-references *carry* — **NEW INSTRUMENT, `wt184`** | 247 references parsed into 194 pointer-bearing clauses; **118 numeric attributions and 3 quoted phrases adjudicated** against the named section's own text, bounded at the next heading of ANY level, emphasis stripped from both sides; plus the 72 bare top-level `§N` pointers probed separately | 121 adjudicated | **III-5** |
| **A4** named commands RUN, **and the second question asked** | `wt027_report.py` RC 0 (five blocks, exactly as §11 claims, including all three §3.1 prose-only figures); `wt002_lambda_report.py` RC 0; `pytest tests/ -q` **1168 passed**; `git log -1 --format=%h <sha> -- <path>` on all three per-file pins, each returning its own sha; `shasum -a 256` on both committed data files, both matching §11 to the digit; the `TIER_TAGS` block extracted at `d655501` and at HEAD and hashed — **byte-identical, 330 bytes, `2217dd125d81ed94`**; **and then `wt091_lag_shape_identifiability.py`, which §11 does not name** | 8 named + 1 unnamed | **III-6, III-7** |
| **A5** named artefacts enumerated and read | **27 backticked path-like artefacts, 26 resolving and the 27th a glob that does**; 21 document-name tokens, all resolving; **7 commit shas, all resolving to commits**; `REG-005`, `RESULT-REG-005`, `RESULT-REG-003` and `REG-004` read at the cited section | 55 artefacts | (fed III-5, III-7) |

**A4's second question is what paid, and it arrived on paper-III as `-100`'s IV-10 arrived on
paper-IV.** `-80` asked it first — *is there a number the paper reports that no named command
produces?* — and found six §3 figures. It asked it of §3 because §11's scope sentence scopes to
*"§A.2 and §§2–3"*. **The scope sentence is what hid §4.10 for three passes:** the sentence is
accurate, and it is a floor rather than a ceiling, and a reader who takes it as a ceiling never asks
where §4.10's numbers come from.

---

## 2 · THE THREE FINDINGS, WITH THEIR AXIS AND THEIR SHAPE

`shape` is `-79`'s column, on REVIEW-019 §6's definitions unchanged: **P** = promise-about-artefact ·
**D** = deferral-with-empty-target · **—** = neither.

| # | § | axis | shape | one line | repair |
|---|---|---|---|---|---|
| **III-5** | 4.10 | A3′ (`wt184`) | **D** | the reference width **0.150** is attributed to §5.4, twice; §5.4 carries the interval, never its width | `wt185` |
| **III-6** | 11 | A4 (second question) | **P** | §11 names a `Regenerate` command for five sections and none for §4.10, whose table `wt091` prints entire | `wt185` |
| **III-7** | 4.10 | A4 | **—** | the 10⁻³ set "reaches **k = 0.50**"; the *registered* sweep reaches **0.60**, and the paper's own table says so | `wt185` |

**SPLIT: 1 of 3 · 1 of 3 · 1 of 3.**

### III-5 · §4.10 · A pointer that resolves and does not carry **[D]**

Two sites, a table header and a prose sentence, both reading **`against §5.4's 0.150`**:

> `| precision of the reported series | shapes it cannot separate from k̂ = 1.21 | width | against §5.4's 0.150 |`
>
> *"— an interval of 0.100 against §5.4's 0.150 from hand-collected impairment lags."*

**§5.4 contains no `0.150` and no `0.15`.** What §5.4 contains is *"k̂ = 1.210, 95% profile interval
[1.135, 1.285]"*. 1.285 − 1.135 = 0.150, so the number is *derivable* from §5.4 and is *stated*
nowhere in it. A reader who follows the pointer to check the denominator of the paper's own ratio
column does not find it.

**And both upstream sources attribute the number to something else.** `RESULT-REG-005` §2's table
header reads *"against **REG-003's** 0.150"* and its prose reads *"0.100 against **RESULT-REG-003's**
0.150"*. `wt091` prints `= 0.67 x REG-003's 0.150` on every one of the four rows. **The manuscript
re-attributed the number when it transcribed the table, from a registration to a section of itself,
and the section it chose does not carry it.** That is `-99`'s II-40 class exactly — a reference that
resolves is not a reference that is correct — and it is the first time the class has been found by a
script rather than by a reader's eye.

**Repaired by `wt185`.** Both sites now read *"the 0.150 width of §5.4's [1.135, 1.285]"*. The number
survives, the interval it is the width of is named at the point of comparison, and §4.10 already used
`[1.135, 1.285]` five lines below, so the repair speaks the section's existing vocabulary rather than
importing new. No hedge added.

### III-6 · §11 · The paper's answer to its own title has no runnable provenance **[P]**

§11 is *Data and code availability*. It carries four `Regenerate` bullets — §3 (and §A.2.4), §A.2.3,
§5, §5.4 — each naming a runnable path. **There was none for §4.10.** §4.10's five-row precision
table, its search floor at the fitted shape, its profile at the constant hazard and its comparison
against the event-date interval are produced by `scripts/wt091_lag_shape_identifiability.py`, which:

* runs the ladders REG-005 registered, exhaustively, as its own docstring states — *"Ladders I, P, W, S and N are exhaustive"*;
* was first committed at `42ca377`, **one hour and fourteen minutes after** the registration it obeys was committed at `6f0e7be`, which is precisely what §4.10 claims when it says *"REG-005 registered the question, four falsifiers and five ladders before `wt091` existed"*;
* **opens by quoting the manuscript**: *"Section 4.2 proves an impossibility by counting …"*.

The script knew it was the paper's source. §11 did not know the script existed. `-100` named this
family on paper-IV — *look for the artefact that knows about the manuscript* — and it is here, on a
different manuscript, with the same shape and a different cause: not a missing artefact, a section
whose own scope sentence let three reads stop short.

**Repaired by `wt185`:** §11 now carries a fifth bullet naming the path, the registration, the
pre-registration commit, and the runtime, and says plainly that until `wealthTensor-101` this section
named no command for §4.10. `wt148` went RED with four new promises the moment the bullet landed —
the guard working — and `wt186` adjudicated all four, evidence run in this session, class H·H·H·N.

### III-7 · §4.10 · An unregistered number carrying a registered argument **[—]**

> *"At one part in a thousand the set reaches **k = 0.50**, below one, a *decreasing* hazard …"*

**The registered sweep reaches 0.60.** §4.10's own table, two paragraphs above, gives the 10⁻³ row as
**[0.60, 1.87]**, and its own parenthetical says the lower rows *"run into the boundary of the
pre-registered sweep"* and that **0.50** comes from *"a sweep extended to [0.2, 3.0]"*. `wt091`
confirms both, and then makes the paper's argument itself, with the registered number:

> `I(1e-3) reaches k = 0.60 < 1 — a DECREASING hazard, which by §4.9 admits no steady-state deferral measure at any positive decay rate.`
>
> `ROBUSTNESS (unregistered, cannot change a verdict): on k in [0.20, 3.00] the sigma = 1e-3 interval is [0.50, 1.86] …`

This matters more here than it would in another paper, because **this manuscript has a convention and
§4.10 broke it.** §5.4 labels every unregistered cut *"Unregistered robustness"*, in those words,
because `RESULT-REG-003` labels them that way; REG-005 §7 says unregistered robustness is *reported,
labelled, and unable to change a verdict*. §4.10 let an unregistered number carry a verdict-shaped
sentence without the label.

**Repaired by `wt185`, and the repair is a STEELMAN.** The sentence now reads *"the registered
sweep's set reaches **k = 0.60**"*. 0.60 < 1 carries the decreasing-hazard argument unchanged, the
extended sweep's [0.50, 1.86] stays disclosed two paragraphs above, and the claim stops depending on
an unregistered sweep. **A finding that looked like it demanded a caveat demanded a narrower claim
instead, and the narrower claim is the stronger one.** Defensive count 3 → 3 (+0).

---

## 3 · What `wt184` is, what it found, and what it structurally cannot see

`wt133` has asked, for twenty sessions, whether a `§N.M` reference RESOLVES. It prints `0 unresolved`
on all four manuscripts and it is right every time. `wt184` asks whether the referent CARRIES what the
pointer says, on two rules:

* **RULE 1 — NUMBER CARRIED.** A clause naming a section and stating a figure asserts the figure is in that section.
* **RULE 2 — PHRASE CARRIED.** A clause naming a section and quoting a phrase asserts the phrase is in it, **after markdown emphasis is stripped from BOTH sides** — `-100` lost a finding to a checker that called *"emphatically not"* absent from a section containing `emphatically **not**`.

**Its three negative controls failed on their first run and every failure was a real bug.** That is
the instrument earning its keep, and it is worth four lines because two of the three would have made
the axis worthless while looking green:

1. **A section number is not a numeric claim.** `§2.1` was read as the literal `2.1`, checked against §2.1, and flagged. Unfixed, every one of paper-III's 244 references becomes a finding.
2. **A line-at-a-time reader sees one quoted phrase in 2 741 lines.** The manuscript is hard-wrapped at ~100 columns, so quotations open on one line and close two later. Rule 2 was *vacuously clean* until clauses were built from paragraphs.
3. **A markdown table row is one clause across six cells.** §7's ledger rows put a `§5.4` in one cell and unrelated figures in three others, all of which flagged. Attribution is now windowed to the fragment carrying the pointer.

**What it cannot see, stated so no pass credits it with more.** A pointer at another document's
section (23 on paper-III) is out of scope. A clause naming two sections is tested against the UNION
of their bodies, which is the weaker test — such a clause can fail to produce a finding but can never
produce one. The 72 bare top-level `§N` pointers are bucketed, not adjudicated; **probed separately,
they carry ZERO numeric attributions**, so the class `-83`'s III-3 came from is empty on this reading.
And **RULE 2 returned three flags on paper-III and all three are false positives** — two are
rhetorical objections the paper quotes and answers, one is Bleck and Liu's phrase attributed to Bleck
and Liu. Rule 2 needs an *attributed-to-a-section* test, not co-occurrence. §7 tees that up rather
than claiming it.

`wt184 --postconditions`: **RC 0, 28 checks, 9 NEGATIVE.**

---

## 4 · What was checked and held — the anti-cheerleader section, and it is specific

Charter §5 asks for at least one named, checkable strength. There are six, and each names the command.

1. **§11's `TIER_TAGS` byte-identity claim is exactly true.** Extracted at `d655501` and at HEAD, both blocks are 330 bytes with SHA-256 prefix `2217dd125d81ed94`. §11 says the block that selected §5's published sample is byte-identical across a commit that touched `edgar.py`; it is.
2. **All three per-file pins resolve to themselves.** `git log -1 --format=%h d655501 -- src/wealth_tensor/edgar.py` → `d655501`; likewise `ad779eb` for `lag.py` and `b9089c7` for `lambda_sensitivity.py`. Both committed data files' SHA-256 match §11 to the digit.
3. **§4.10's provenance claim survives the sharpest test available to it.** *"REG-005 registered the question, four falsifiers and five ladders before `wt091` existed"* — `6f0e7be` at 15:10:24 on 2026-08-12, `42ca377` at 16:24:12 the same day. Seventy-four minutes, and in the right order.
4. **`wt027_report.py` prints five blocks, as §11 says, and every prose-only figure it promises.** A, A′, B, C, D — with 199.8990 at φ = 0.9, 1799.0906 at φ = 0.1 and D(0) = 1998.9895 all printed, the three §11 says are in there and were printed by nothing until `-80`.
5. **The two tests §11 names for what they forbid are live in the companion modules, not only in the guard asserting their names** — `tests/test_excess_demand.py:120` and `tests/test_redistribution.py:61`, each with `.bak` siblings beside it that a careless grep would have accepted instead.
6. **`test_restatement_reach` behaved exactly as its docstring promised.** The III-5 repair moved §4.10's count of `1.135` and `1.285` from 1 to 3 and the guard went red with the section named and both counts printed. Its docstring had stated that bargain in advance — *"the author must update a number here … the update is mechanical"* — and it was: `wt187` reads the new counts out of the manuscript with the guard's own counting function rather than transcribing them from the failure message.

---

## 5 · Estate, and the mechanism this pass declines to propose

**Carded — one, with a named falsifier.**

* `docs/preregistration/RESULT-REG-005.md` line 60 carries III-7's slip too: *"At 10⁻³ the set reaches **k = 0.50**"*, against its own §2 table row `[0.60, 1.87]` and its own line 50, which attributes `[0.50, 1.86]` to the unregistered extension. **Falsifier:** open the file; if §2's 10⁻³ row reads `[0.50, …]`, this card is wrong. Not repaired in-pass on purpose — it is a committed result document for a registered run, and editing one to fix a slip is a move that wants its own ruling rather than a reader-pass's initiative. **The `-83` III-5/RESULT-001 precedent, applied.** Paper III is unaffected: `wt185` repaired the manuscript. State Machine.

**Nothing else carded.** All three findings repaired in-pass.

**RESIDUE IS 0 OF 3 AND NO MECHANISM IS PROPOSED FROM IT.** Five mechanisms have been proposed across
fifteen rows — new instruments (`-71`/`-77`), residue (`-77`/`-78`), depth (`-78`/`-79`), coverage
(`-80`/`-81`), enumeration (`-82`/`-83`) — and only enumeration survived its own next pass. `-99` had
a 2-of-3 residue row and declined; `-100` had 2-of-4 and declined. **This row has 0 of 3, which is the
cleanest residue number in the ledger, and proposing a sixth mechanism from a clean number on n = 3
would be the same error with a friendlier face.** What the number says, and all it says: three
findings on a passage added whole at `42ca3773` and read past by `-73`, `-80` and `-83`.

**Apparatus changed.** `docs/promises-adjudicated.tsv` gains four rows for the promises §11's new
bullet emits — `wt186`, 11 post-conditions, 8 NEGATIVE, seventh column derived from `wt148.emit()`.
Paper III now runs 95 promises over 63 sentences, 95 adjudicated, 87 H · 7 N · 1 R.

---

## 6 · State at wrap

| gate | result |
|---|---|
| `python3 -m pytest tests/ -q` | **1168 passed, 0 failed** |
| `python3 scripts/wt148_promise_sweep.py` | **RC 0** — 173 emitted, 160 adjudicated, **0 unadjudicated, 0 STALE** |
| `python3 scripts/wt133_crossref_sweep.py` | **RC 0** — 244 refs, 0 unresolved |
| `python3 scripts/wt184_pointer_correctness.py --postconditions` | **RC 0** — 28 checks, 9 NEGATIVE |
| `python3 scripts/wt185_paperIII_p7pass4.py` | **RC 0** — 19 checks, 8 NEGATIVE, idempotent |
| `python3 scripts/wt186_paperIII_promises.py` | **RC 0** — 11 checks, 8 NEGATIVE |
| `python3 scripts/wt187_restatement_counts.py` | **RC 0** — 6 checks, 4 NEGATIVE, idempotent |
| `bash docs/deliverable/verify-layout.sh` | **RC 0** — 145 pages, clean worktree, `source_commit d16296959820` |
| `defensive_count.py --against` the pre-edit file | **3 → 3 (+0)** outside §Limitations · G-COACH-3 holds |
| `bash scripts/regen-board.sh` | **RC 0** — `docs/CHECKLIST.md` diff **EMPTY** |

**CONSECUTIVE-ZERO COUNT AFTER THIS PASS: 0.** The pass does not score `P7`; that is PENDING-HUMAN.

---

## 7 · What this pass hands forward

1. **RULE 2 NEEDS AN ATTRIBUTION TEST, AND IT IS CHEAP.** `wt184`'s quotation rule returned three
   flags on paper-III and all three are false positives, because it accepts *co-occurrence* of a quote
   and a pointer as attribution. The fix is a verb list — `§N.M says / states / puts it / calls it` —
   or the possessive form, which Rule 1 already uses and which cut its own flag set from 44 to 5. This
   is the half of `-100`'s tee-up 1 that is built but not yet sharp.
2. **POINT `wt184` AT PAPER-II AND PAPER-IV.** It has only ever read paper-III. Paper-II is where II-40
   — the defect that opened this axis — was found by hand, and the script has never been asked whether
   it recovers it. **That is a held-out test of the instrument, not just of the manuscripts**, and it is
   the same design `-83`'s prediction and `wt169`'s held-out pointer test used.
3. **THE SCOPE SENTENCE IS THE NEXT A4 TARGET, ON EVERY MANUSCRIPT.** §11 opens *"Every simulation
   result in §A.2 and §§2–3 is produced by open code"*, and that sentence is why three passes never
   asked where §4.10's numbers came from. The check is one question per manuscript: **enumerate the
   sections that report a computed figure, and enumerate the sections §Data-and-code covers. The
   difference is the unchecked set.** On paper-III it was §4, and §4 is nine subsections long.
4. **`wt133` sweep-3 still unbuilt** — a body proper noun with no reference entry is invisible to both
   sweeps. Named after IV-6 at `-81`, unbuilt through three passes now.
5. **Bouchaud & Mézard's two verbatim quotations in Paper II §3.1, unread against source.** Flagged at
   `-74`, `-77`, `-99`, `-100` — five passes deferred. Tee-up 1's sharpened Rule 2 makes the first step
   minutes.
6. **Nine uncited reference entries on Paper II** (card `1217568192511533`), sixth pass carrying it.
   Paper-IV is 28 of 28, paper-III is 49 of 49, paper-II is 7 of 16 and `wt133` prints the nine names
   every run.
7. **A6, the docstring axis** — parked since `-80`, nineteen unasserted prose claims.
