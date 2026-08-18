---
new_instrument: none
instrument_name: "— (all five axes inherited; the grid closed at -80. What is new is not an axis but a TARGET: -82's enumeration, docs/promises-adjudicated.tsv, which this pass read as a document to be falsified rather than as a result to be trusted.)"
findings_from_new_instrument: 0 of 4
residue_of_previous_pass: 0 of 4
shape_promise_about_artefact: 1 of 4
shape_deferral_with_empty_target: 2 of 4
shape_neither: 1 of 4
manuscript_edits_required: 4 of 4
prediction_under_test: "-82, REVIEW-022 §5: materially fewer than 5-of-9 promise-shaped"
prediction_verdict: HELD
# FALSIFY THIS ROW, SIX WAYS.
#   1. `none`: the axis matrix in docs/p7-passes.tsv read 15 of 15 at the parent commit 15460d8.
#      Paper III was 5 of 5 before this pass. If any cell was empty there, the row is wrong.
#   2. `0 of 4`: §2 credits each finding to the axis that produced it. No finding traces to an
#      axis this manuscript had not already had.
#   3. `0 of 4` residue: git blame every site at 15460d8. No site blames to -82's two repairs
#      (wt149, wt150) or to -82's TSV. III-1's SITE predates -82; what -82 added is the FALSE
#      ADJUDICATION of it, which is apparatus and is counted in §1, not here.
#   4. `4 of 4` manuscript edits: scripts/wt151_paperIII_p7pass3.py touches paper-III.md four
#      times for four findings, with ten post-conditions, three NEGATIVE. Run it; it refuses on
#      a moved anchor and rolls back on any failed post-condition.
#   5. the shapes: §2's shape column, on REVIEW-019 §6's two definitions unchanged. -80 found
#      5/2/2 on Paper III and -81 found 5/2/2 on Paper IV. This pass found 1/2/1. If a re-read
#      moves any finding into the promise column, the verdict in §1 weakens.
#   6. the verdict: 1 of 4 is 0.25 against 5 of 9 = 0.556. If you judge n=4 too small to call
#      "materially fewer", say so — §1 states the objection and answers it.
# Ledger of all twelve passes: docs/p7-passes.tsv
---

# REVIEW-023 · Paper III's THIRD independent `P7` read — the pass that settles -82's prediction, and finds the third failure mode

*Session `wealthTensor-83` · 2026-08-18 · parent commit `15460d8` · all five axes run before a word
of prose, in the order -80 and -81 ran them.*

---

## 1 · The verdict, first, because it is what this at-bat was for

**-82's prediction HELD.** Four findings, **1 of 4 promise-about-artefact** against the 5-of-9 that
-80 and -81 each returned — 0.25 against 0.556. This is the first mechanism in twelve rows to
survive its own next pass, and it survived it on the design -82 built for exactly that purpose: the
prediction was written before this pass existed, in units this pass could not choose, and the pass
that settles it is an ordinary reader-pass costing nothing extra.

**No disambiguation branch was required, and this section says what would have triggered one.**
Branch (a) — new promise-shaped findings naming an artefact, meaning wt148 has a gap — did not
fire, and could not have: the one promise-shaped finding names `data/pre-002-events.json`, and
**wt148 emitted that exact (sentence, artefact) pair.** Branch (b) — promise-shaped findings naming
no artefact, meaning the class was mis-defined — did not fire either; both bare-noun-phrase findings
scored as deferrals, which is the column they belong in.

**What did fire is a third mode neither branch enumerates, and it is the finding of this pass.**

> **THE INSTRUMENT CAUGHT THE SENTENCE. THE ADJUDICATION WAS FALSE.**

Row `93662b4195` of `docs/promises-adjudicated.tsv` carried §5.4's firm-count sentence, paired with
the right artefact, classed **H**, with an evidence column reading *"wt089 §2 reconciliation block"*
and a note justifying 313 as *"(122+191)"*. The sentence claims the count *"is read back out of the
committed `data/pre-002-events.json`"*. Read back out of that file it is **307** — the number the
sentence calls a discarded earlier revision. The adjudicator checked a different artefact from the
one the sentence names, found a number that agreed, and stopped.

This is not an argument against -82's enumeration. It is -82's enumeration working: the TSV's own
header prescribes the cure — *"Take the row's `evidence` column. It names a command to run or a file
to read. Run it or read it. If it does not show what `note` says it shows, the row is FALSE."* This
pass ran that procedure once, on one targeted row, and the row was false. **A 127-row ledger of
human adjudications is an artefact like any other, and the promise class is drained to 2 of 127 only
if the 125 are true.** The rate at which they are not is now a measurable quantity and nobody has
measured it. That is -84's at-bat and §7 assigns it.

**The objection to this row, answered.** Four findings is a small denominator, and 1 of 4 could be
one coin flip from 2 of 4 (0.50, which is not materially fewer than 0.556). Two things answer it.
The finding count itself fell — 4 against nine and nine — which is the direction the enumeration
predicts and which no previous pass produced. And the *composition* moved in the predicted way
rather than uniformly: deferral-with-empty-target held at 2, exactly where -80 and -81 had it, while
the promise column collapsed from 5 to 1. **The class -82 drained is the only column that moved.**

---

## 2 · The four findings, with their axis and their shape

`shape` is `-79`'s column, on REVIEW-019 §6's definitions unchanged: **P** = promise-about-artefact
· **D** = deferral-with-empty-target · **—** = neither.

| # | § | axis | shape | one line | repair |
|---|---|---|---|---|---|
| **III-1** | 5.4 | A5 | **P** | the pooled firm count is **307**, and the paper calls 307 an erratum | wt151 |
| **III-2** | 6.1 | A3 | **D** | the three post-hoc conjectures are not in the repository's working notes | wt151 |
| **III-3** | 8.2 | A3 | **D** | §10 holds no reading queue, and the list that exists is marked undischarged | wt151 |
| **III-4** | 7 | A1 | **—** | the ledger row reads 7 × 10⁻⁴ where the run says 5 × 10⁻⁴ | wt151 |

**SPLIT: 1 of 4 · 2 of 4 · 1 of 4.**

### III-1 · §5.4 · The pooled firm count is 307, and 307 is not an erratum **[P]**

§5.4 read: *"The firm count is read back out of the committed `data/pre-002-events.json`; an earlier
revision of this sentence said 307, which would have made the rebuild fail the one-per-cent
reconciliation the sentence exists to assert."*

Read back out of that file: pilot 247 events / 122 firms, replication 448 / 191. **313 is the sum of
the two per-universe counts. The union is 307.** `RESULT-REG-003` §1 states it in those words — *"the
pooled firm count is 307, not 313, which is a small fact nobody had looked at"* — and names the six
registrants that changed SIC between 2013 and 2024 and so enter both universes: Live Ventures,
Ubiquity, Right On Brands, Fortune Valley Treasures, IAC and Match Group. It goes on to warn that
*"a **pooled** statistic … is pooling two sets that overlap in 2% of their firms."*

Three things make this worse than a wrong number.

1. **The paper is already using 307.** REG-003 §2's third registered sensitivity is *one event per
   firm*, at **n = 307**, and §5.4 quotes its result two paragraphs later as *"0.413"*. The sentence
   calls an erratum the denominator of a statistic it reports.
2. **The firm count is not in the reconciliation rule at all.** REG-003 §2 registers *"≥ 95%
   agreement in total n and no tier moving by more than 20%"*. There is no one-per-cent
   reconciliation, on firms or on anything else; the artefact's own verdict is *"Agreement 99.0%,
   worst tier drift 1.4%"*. A firm count of 307 could not have made the rebuild fail a rule the firm
   count does not enter.
3. **The clustering argument wants the smaller number.** §5.3's second qualification — *"The 688
   events come from 311 firms … the effective sample is smaller than 688"* — is where a firm count
   does work, and there the union is the conservative figure and the sum is not a count of firms.

**Repaired by `wt151`.** §5.4 now gives both quantities in their own units, names the union as the
*n* of the sensitivity below, and quotes the registered rule verbatim. No hedge added.

### III-2 · §6.1 · The three post-hoc conjectures are not in the working notes **[D]**

§6.1 read: *"Three post-hoc conjectures about where the conjunction broke are recorded in the
repository's working notes."*

`docs/notes/` — the repository's working-notes directory — holds two files. `NOTE-001` is a synthetic-data
note on φ identifiability and mentions exactly one conjecture, which is not one of the three and
which it marks *"deliberately left undeveloped"*. The three live in
`docs/preregistration/RESULT-002-wt026.md` §4, lettered (a) theory, (b) bridge, (c) unit, under the
preamble §6.1 paraphrases.

The sentence's whole purpose is to hand a reader the map while refusing to argue from it — *"It is
written down because the next person deserves the map"*, as the artefact itself puts it. The map's
pointer misses. **Repaired by `wt151`:** §6.1 names the file and section.

### III-3 · §8.2 · §10 holds no reading queue, and the list that exists is undischarged **[D]**

§8.2 read: *"The crash paper is a later paper in this corpus, written with a price line and after
the reading queue in §10 is discharged."*

§10 is *Relation to existing work*. It contains no queue, discharged or otherwise. The string
*"reading queue"* occurs nowhere else in the repository. The list that exists is
`POSITIONING-002-second-pass.md` §6, titled **"UNDISCHARGED — the reading list, with read-status
attached to every entry"**, opening *"WT-059 applies and is NOT discharged"*, and still carrying
Ryan (1995) as STILL NOT READ, Zhu (2016) as ABSTRACT ONLY and Bushman & Williams as BIBLIOGRAPHIC
ONLY. That file's top-level sections run 1 – 9.6; it has no §10 either, so the pointer cannot be
read as a cross-document reference.

This one gates a whole future paper on a checkpoint that is not where it is said to be, and the
checkpoint that does exist says *not yet*. **Repaired by `wt151`:** §8.2 names the file and section
and states that the file marks it undischarged.

Neither III-2 nor III-3 is reachable by `wt148`: both targets are bare noun phrases, and the sweep
emits on named artefacts. `wt133` cannot reach III-3 either — its sweep resolves `§N.M` forms, and
`§10` is a bare section number.

### III-4 · §7 · The ledger row and §4.10 disagree about the same run **[—]**

§7's row *"Three recognition rates are three quantities"* reported *"agree to **7 × 10⁻⁴** at twenty
years"*. §4.10's prose, on the identical measurement, says *"five parts in ten thousand"*.
`RESULT-REG-005` §5 settles it: `P_rows` at a twenty-year life gives `dev_vs_eff = 0.0005185`, and
the document's own table prints **0.05%**. The 7 × 10⁻⁴ is what you get by dividing the paper's own
4-decimal display (0.4388 − 0.4385) / 0.4385 — a number computed off the manuscript rather than off
the run. **Repaired by `wt151`.**

A plain wrong number, and it is worth one line that this pass found exactly one of them: every other
row of §7 was cross-checked against its own section in the body and against the artefact behind it,
and the other forty-six hold.

---

## 3 · The five axes, and what each returned

| axis | what was run | scale | findings |
|---|---|---|---|
| **A1** quantifiers read forward | `wt130` (898 quantifier tokens on 691 of paper-III's 2 735 lines); §4.4's ladder recomputed from the closed form at all three α; §§3.1/3.2/4.9/4.10/5.3/5.4 tables recomputed; abstract reconciled to body; all 47 rows of §7 cross-checked against their sections | ~120 numeric claims | III-4 |
| **A2** the failure mode the paper names, turned on the paper | §7's *"every test run is reported"*; the charter's non-increasing defensive count; §6.2's bridge discipline; §11's pointer discipline; the TSV header's own falsification procedure | 5 modes | (fed III-1) |
| **A3** cross-references | `wt133` RC 0 (240 §N.M refs, 37 distinct, 0 unresolved; 49 of 49 references cited) — **plus the pointers wt133 structurally cannot reach**: bare `§N` forms and bare noun phrases | 240 + 2 unreachable | III-2, III-3 |
| **A4** named commands RUN | `wt027_report.py` RC 0 (five blocks, and every §3 figure it claims to print is printed); `wt002_lambda_report.py` RC 0; `pytest tests/ -q` **1094 passed**; `git log -1 --format=%h <sha> -- <path>` on all three per-file pins, all three returning their own sha; `lag.py` commit count = 1; the `TIER_TAGS` block extracted at `d655501` and at HEAD and hashed — **byte-identical**, as §11 claims; `shasum` on both committed data files | 9 commands | none |
| **A5** named artefacts enumerated | 20 paths existence-checked; five commit stats resolved (`9722342` single-file ✓, `d655501` nine files incl. the instrument ✓, `cc1d198` exactly three tests ✓, `0569ab6`, `5efe626`); REG-003 / REG-005 / REG-008 / REG-009 / REG-009-filled / REG-010 / RESULT-001 / RESULT-002 read at the cited section; **`docs/promises-adjudicated.tsv` read as an artefact and one row falsified** | 31 artefacts | III-1 |

**A note on RESULT-001, recorded and not counted.** `RESULT-001-wt026.md` line 92 reads *"Zero
censoring in 320 events across two universes"*, while its own §§1–2 report 120 and 202. The paper
says 322 and the paper is right; the artefact's summary line is the slip. It is not a finding
against the manuscript and is not counted as one. Carded — see §5.

---

## 4 · What was checked and held

Every figure `wt027_report.py` prints matches §3 to the digit, including the three prose-only
values §11 promises are in there (lag 1 at φ = 0.9, lag 24 at φ = 0.1, D(0) = 1998.9895).
`wt002_lambda_report.py` reproduces §A.2.3 entire: lag 22, smoothing 0.6097, concentration 0.9199,
16 events, relative magnitude 0.20138, every dimensionless spread exactly 0.0, both log-log slopes
1.000000000000.

§4.4's ladder was recomputed from `R = (1 − φ)δ/(α − δ)` at all three recognition rates: every cell
of all four **R** columns, τ = −1 / −0.67 / +1, the three design terms (+0.69, +0.41, +0.29) and the
three δ contributions (−0.81, −0.98, −1.79), δ₃\* = 0.0079 and its 87-period half-life, the
first-rung boundary at 0.0214 (46.7 years, inside by a fourteenth) and at 0.0156. The abstract's
1.67 reconciles to §4.2's 1.27/0.76 and its 4.2 to §4.4's 2.58/0.61. §4.9's five overstatement
percentages reconcile to their own R columns under 4-dp rounding. §4.2's *"4 × 10⁻⁶ of the original
world's"* is 3.95 × 10⁻⁶ computed, and §A.1.3's terminal 0.031 is 0.030965.

Against the artefacts: `RESULT-REG-009` gives Ψ = 0.6586 [0.6211, 0.6964] and per-cycle 0.6326 /
0.6818 — §4.4's 65.9%, 63.3% and 68.2% and §7's [0.621, 0.696]; S = 0.1391 — §4.4's 86.1% outside
and §7's 0.139 inside. `RESULT-REG-009-band-count` gives 151 events / 98 firms / 110 joinable / 16
bands / `[5,6)` at 36 events and 20 firms, and the filled run gives 133 of 151 with `[4,5)` at 27
against the floor of 30 — §4.7 verbatim. `SCOUT-001` gives 0.9590 at α̂'s lower bound and 0.8141 at
0.327 — §4.4's 0.959 and 0.814. `RESULT-REG-003` gives 0.433 / 0.394 retail and computer services,
0.396 / 0.398 / 0.404 under truncation, 0.460 shifted, 0.327 dropped, and labels every one of them
*"Unregistered robustness"* — which is the word §5.4 uses and `SCOUT-001` §T3 does not.
`RESULT-REG-008` §2.2 gives 0 of 281 and 1 of 644 — §5.4 and §9's ninth limitation both.

The two tests §11 names by name for what they forbid are both live and both defined in the
companion modules §11 says carry them, not only in the guard that asserts their names.

---

## 5 · Estate

**Carded — one, with a named falsifier.**

- `RESULT-001-wt026.md`'s summary line says 320 where its own components sum to 322. **Falsifier:**
  open the file; §1 says *"120 events across 72 firms"* and §2 says *"202 events across 106 firms"*;
  120 + 202 = 322. Not repaired in-pass on purpose: it is a committed result document for a
  registered run, and editing one to fix a summary slip is a move that wants its own ruling rather
  than a reader-pass's initiative. Paper III is unaffected — it prints 322 in both places it prints
  it. State Machine.

**Nothing else carded.** All four findings repaired in-pass by `wt151`, 10/10 post-conditions,
3 NEGATIVE.

**Apparatus changed:** `docs/promises-adjudicated.tsv` — row `93662b4195` retired as FALSE (not
stale-by-rewrite; false on its own evidence column), three new promises adjudicated **H** against
the artefacts read this session. Paper III now runs 88 promises over 58 sentences, 88 adjudicated,
81 H · 6 N · 1 R.

---

## 6 · State at wrap

| gate | result |
|---|---|
| `python3 -m pytest tests/ -q` | **1094 passed, 0 failed** |
| `python3 scripts/wt148_promise_sweep.py` | **RC 0** — 88 of 88 adjudicated in scope on paper-III, 41 of 41 on paper-IV |
| `python3 scripts/wt133_crossref_sweep.py` | **RC 0** |
| `python3 scripts/handoff_gate.py --coach` | paper-III **5 conduct / 0 concessive** — baseline |
| defensive-sentence count | 6 → 6, non-increasing (charter §2) |

---

## 7 · What this pass hands forward

**The promise class is drained to 2 of 127 only if the other 125 rows are true, and nobody has
measured how often they are.** This pass falsified one targeted row and it was false. The TSV's own
header tells you to falsify three at random before trusting it; -82 wrote that instruction and did
not have a later pass to run it. **-84's at-bat is to run it, at a sample large enough to put a rate
on it** — and §1 explains why that is the one measurement that can now move the number -82
established.
