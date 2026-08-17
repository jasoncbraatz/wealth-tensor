---
project: wealth-tensor
gh_sha: 96e54c65b495324f1c1fa38a059e9f68e914d3d1
updated: 2026-08-17
session: wealthTensor-66
gate_passed: true
gate_version: "2.59"
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."
---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-66` IN ONE LINE
**THE LITERATURE SEARCH RAN, AND THE ANSWER IS `KNOWN`.** Bouchaud & Mézard (2000) already
derive the Pareto tail exponent in closed form in a **flow** tax rate, a **stock** tax rate and
the **per-capita rebate fraction of each** — and report the ranking more strongly than
`ROADS-001` proposed it. Option **C collapses on its headline**; Jason's Kelly bet on **A** was
right. Six sessions carried this as *"blocked, never run"*; it cost **one at-bat**. Suite
**1078 passed, 0 failed**. Commit `1e59b6e`.

**AND THE THING THAT NEARLY WENT WRONG, because it is the more portable half:** my headline
absence predicate **could not fire at all**, was dark across eleven economics full texts, and I
was one step from writing that up as a **clean absence** — which is the answer that would have
*re-opened* C. See §THE TELL.

---

## READ FIRST, in this order
1. **`docs/SCOUT-001-truncation-vs-scaling-prior-art.md`** — the deliverable. Verdict in one
   markable sentence, the evidence at source, the method failures, and the one hole named.
2. **`docs/LEDGER.md` `WT-100`** (the fact) and **`WT-101`** (the method).
3. **`docs/ROADS-001-two-reconstructions.md`** — now **ticked**. Its *"What I could not check
   and you should"* section carries the answer. **Do not read it as a live proposal.**
4. `docs/DECISION-001-A2-and-road-one.md` — unchanged, still ticked at A, now with its
   re-allocation test spent.

---

## YOUR AT-BAT — take one, in this order

### 1. **PAPER II's TWO MANDATORY CITATIONS.** Card `1217556375636027`. **This is the one.**
Not optional additions — the difference between a contribution and an uncredited restatement.
**Bouchaud & Mézard (2000)** wherever Paper II contrasts the stock levy with the flow levy in
terms of the multiplier's shape; **Benhabib, Bisin & Zhu (2011) §4.1** wherever the `r = 1` cap
appears. Both read in full at source; exact quotes and DOIs are on the card and in `SCOUT-001`
§4. Bounded, concrete, and it is the direct consequence of this session.
**Before you edit:** `WT-094` (grep `tests/` and `scripts/` first), `WT-099` (census before
patch), and the abstract has **six words of slack that `-65` returned deliberately** — spend
them only if you must.

### 2. **PAPER II's SECOND INDEPENDENT READ** — could start a convergence count. It has now moved
in 24 places in 48 hours. **Diff against `paper-II.md.bak-wt65-decA` and `.bak-wt64-p7`**; do not
read the repaired text as given. *Natural to combine with #1, but they are different jobs: #1 is
a known patch, #2 is an open read. Do not let #1 quietly become the whole at-bat.*

### 3. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
### 4. **The ρ = 0 test UNDER-asserts** — card `1217547799559841`. Read the card first: tightening
the float tolerance to `==` is how you hand the next machine a red suite. Assert the
**structural** property (the ρ = 0 flow base is uniform across agents).
### 5. **PAPER I's FIRST INDEPENDENT READ** — still the only manuscript with no `P7` pass at all.
### 6. **`REFERENCE-POLICY`'s sixth pass** — card `1217556161163494`. Small, portable, and it
nearly cost this project a wrong verdict. See §THE TELL.
### 7. Paper II's companion reference entries — card `1217542940968749`.

**FORCING LINE (`-59`'s ruling, kept): take none of the seven, say why in ONE LINE at the top of
your handoff. It costs nothing.**

---

## WHAT `-66` DID, so you do not re-derive it

**ONE at-bat. No manuscript touched.** The output is a scouting note, two ledger entries, four
committed instruments and a tick.

### A · The verdict: `KNOWN` (`WT-100`)
**Bouchaud, J.-P. & Mézard, M. (2000), *Physica A* 282, 536–545, eqs (11)–(13).** Their wealth
balance carries **both** levies **and both rebates** — `−φ_I dW_i/dt` (flow), `−φ_C W_i` (stock),
`+f_I φ_I dW̄/dt + f_C φ_C W̄` (per-capita redistribution) — and eq. (13) gives the Pareto exponent
µ in closed form in all four. Their stated scope, verbatim: *"the role of income or capital taxes
and of state redistribution of wealth, on the value of the exponent µ."*

And the ranking, **stronger than ours**:

> *"income taxes tend to reduce the inequalities of wealth (i.e., lead to an increase of µ), even
> more so if part of this tax is redistributed. On the other hand, **quite surprisingly, capital
> tax, if used simultaneously to income tax and not redistributed, leads to a decrease of µ**."*

The per-capita rebate `ROADS-001` §2 wanted to introduce as a novel **fifth coordinate** is a
coordinate in their equation. They also state the organising contrast: a term that *"breaks the
symmetry under wealth rescaling"* leaves *"the Pareto tail truncated for large wealths."*

**AND THE `r = 1` CAP IS NOT OURS EITHER.** `ROADS-001` calls it *"the strongest claim and the
one most likely to be wrong."* It is not wrong — it is **Benhabib, Bisin & Zhu (2011)**,
*Econometrica* 79(1) §4.1: *"…where γ_i < 1 for all i … **it is straightforward to show that the
stationary distribution of wealth would be bounded above**."* Their Prop. 4 additionally has tail
inequality rising in a **mean-preserving spread** of the return process.

### B · Why six sessions missed it, which is the reusable part
`REVIEW-004`, `ROADS-001` and `HANDOFF-PROMPT` all name **optimal-taxation-with-Pareto-tails**. I
searched it; the result is not there and was never going to be, because public finance asks what
a tax *raises* and who *bears* it, not what it does to the *shape of a random multiplier*.
**Statistical physics has asked exactly that since the 1990s.**

The blackbook leaf that predicts this precise failure —
`2026-08-12-search-prior-art-shape-equation-subject`, *"search prior art by the SHAPE OF THE
EQUATION, not by the subject matter"*, banked by `-12` during the Bateman search — **is what
found the paper.** It surfaced because `-65`'s process-miss note asked the next session to run
`lessons.py search` at student-in. `use` + `record-outcome pass` recorded against it.

**A handoff good enough to inline the lessons removes the reason to open the tree, and the tree
holds what the project has NOT inlined. `-65` was right, and this session is the receipt.**

### C · What survives, described as the narrow strip it is
`NO_LOSS_OFFSET` is **dark, 0 of 12 valid full texts**. Bouchaud & Mézard's income tax is
`φ_I dW_i/dt`, symmetric in **both signs** — an affine *contraction* of the multiplier. Ours is on
the **realised gain only**, `A − r·(A−1)⁺`, **no loss offset**, which is what makes ours a genuine
*truncation*. Nor does anyone compare at matched **revenue**: Bouchaud & Mézard compare at equal
*rates*; Guvenen et al. (w26284) compare at equal revenue but route to an **efficiency**
conclusion through entrepreneurial reallocation, never to a tail index.
**That is a remark inside a paper. It is not a thesis to lead one with — `ROADS-001` already
tried that.**

### D · The instruments, all committed and re-runnable
| script | what it is |
|---|---|
| `scripts/wt117_litsearch.py` | discovery **v1, superseded**. Kept because **its failure is the lesson** (`WT-101` §1). |
| `scripts/wt117b_litsearch.py` | discovery v2: 4 indexes × 20 queries × 3 tiers, **known-item retrieval** + per-control scoring. |
| `scripts/wt118_fulltext_absence.py` | **the absence half.** 18 works downloaded, `pdftotext`-extracted, 6 **pre-registered** conjunction predicates, per-document validity, **predicate positive controls**. |
| `scripts/wt119_roads_tick.py` | the `ROADS-001` tick; anchored on a whole paragraph, `assert count == 1`, `--dry`, idempotence guard. |

---

## THE TELL, now SEVEN deep

`-61`: a corpus under repair has a moving referent and only the filesystem knows. `-62`: the
line-wrap grep trap runs both ways. `-63`: a backlog drain measures the backlog, not the paper.
`-64`: a review apparatus has the same defect as a manuscript — its own coverage is an unmeasured
claim. `-65` (i): the fix for `WT-092` has `WT-092` — fire your repair, do not read it. `-65`
(ii): an instrument that reads prose cannot report on code.

**`-66` ADDS THE ONE THEY WERE ALL POINTING AT:**

> ### A DARK PREDICATE IS NOT EVIDENCE OF ABSENCE UNTIL A DOCUMENT YOU **KNOW** CONTAINS THE THING HAS MADE IT FIRE.

`TRUNCATION_x_TAIL` — the headline predicate, the one the whole verdict rested on — had every
alternative in its regex containing the literal word *"tail"* or *"Pareto"*. It was therefore
**structurally blind** to the statistical-physics register, which says *"truncated power law"* and
*"exponent µ"* and almost never *"tail."* It was dark across **eleven economics full texts**, and
that darkness read exactly like a finding.

What caught it was adding **predicate positive controls** — corpus members whose job is *not to
be evidence* but to prove the matcher can fire. **Sornette & Cont (1997), a paper TITLED *"power
laws and truncated power laws"*, left it dark**, and the summary line
`predicates_proven_capable_of_firing: []` is what turned the session around. Widened, it fired on
both controls, and then on Bouchaud & Mézard, who had the answer.

**The two ceilings are different instruments.** A *corpus-level* ceiling asks *"do my searches
return papers?"* A *predicate-level* ceiling asks *"does my matcher fire on a document that
certainly contains the thing?"* Only the second one found this. `-64` proved a review's coverage
is an unmeasured claim; `-66` says the same of **the matcher inside the instrument**.

**Two lesser ones, same family, both recorded in `WT-101`:**
- **A calibration gate built as a SUM over controls** cannot distinguish *all fired* from *one
  fired, three failed silently*. v1 printed `apparatus_valid: true` on **one** hit across four
  controls with **ten of fourteen** API calls errored. Score every control, and **name** the
  failures.
- **A threshold tuned on one literature deletes another for being concise.** A 20,000-character
  extraction floor, calibrated on 40-page economics working papers, silently voided *Physical
  Review* letters at 10k and 17k chars — which are four pages **by design**. Also: a
  document-validity ceiling that tested **my vocabulary** rather than the extraction voided four
  papers that had extracted perfectly, because they write *"Pareto parameter"*.
- And `NO_LOSS_OFFSET` initially fired on two papers **entirely via "without loss of generality."**
  **A predicate that matches boilerplate manufactures its own positives** — worse than a dark one,
  because it makes a corpus look covered.

---

## RULINGS NOW SETTLED — do not reopen
- **`DECISION-001` is ruled A, and its re-allocation test is now SPENT.** The search came back
  `KNOWN`. **C does not get re-opened.** There is no remaining Jason-sized decision on this axis.
- **DO NOT RE-RUN THE LITERATURE SEARCH.** `SCOUT-001` is the note; `WT-100` is the fact; the
  instruments are committed. If you want to *extend* it, extend the corpus in
  `wt118_fulltext_absence.py` — do not start over.
- **The `r = 1` cap and the stock-vs-flow tail contrast are CITED, not claimed.** Card
  `1217556375636027`.
- **`REG-012` §4.7** (`WT-096`): `SEC_47_AT_REGISTRATION` is **immutable**; a warranted edit
  **appends an Amendment**.
- **DO NOT widen `ROTTED` by glob** — Paper IV §10 uses the same words correctly.
- **GREP `tests/` AND `scripts/`** before editing a manuscript string (`WT-094`); **census before
  you patch** (`WT-099`). Do not delete *"18 tests"* from Paper II's abstract.
- **DO NOT re-derive** the κ residuals; `III-1`'s 4.2×; the `E2` blind pass; the
  P2-at-three-strengths lead (withdrawn). **DO NOT re-serve `REVIEW-004` by section number** —
  verbatim quotes only, and §A3 is the section every re-serving pass skips.
- **`REVIEW-005` §2's `II-3` diagnosis is WRONG about the code** (`WT-098`). Do not re-serve it
  without opening `src/`.
- The **end-to-end pass is CLOSED** (T=2, A=0, E1–E6 spent).

---

## HONEST LOOSE END, so you do not discover it as a surprise
**`wt117b_litsearch.py` did not finish inside the session.** Its **known-item tier completed
12 of 12, all retrieved** — the ceiling that matters — but the P/T/N sweep was still grinding
when I wrapped and **`/tmp/wt117b-results.json` was never written.** Cause: **Semantic Scholar
rate-limits hard** and the exponential backoff costs ~124 s per failed call.
**The verdict does not depend on it** — the *absence* half (`wt118`) is what licenses the claim
under `REFERENCE-POLICY` §1, and that completed. Treat `wt117b` as unfinished corroboration.
**Cheapest finish:** drop Semantic Scholar from `SOURCES` (OpenAlex covers it) or add an API key,
then re-run — a few minutes, not an at-bat.

---

## TOOLING (▲ = new at `-66`)
- **RUN THE GATE AS:** `GATE_ROSTER_WHO=big-wealthTensor-NN nohup ~/Scripts/gate-selfcheck.sh >
  /tmp/gate.log 2>&1 &`, then **two** polls of ~170 s. Grep the verdict line `GATE SELF-CHECK:`
  and `CANNOT VERIFY` expecting `0`. **Do not `grep -c "G-AL"`** — it returns 1 on a green run.
- **WRAP SEQUENCE:** `gh_sha: PENDING` → commit → `--stamp` → commit → `--emit`. `--emit` does
  not stamp and refuses `PENDING`. **Never set `gate_passed` true to make it print.**
- **EDITED A PAPER? REGENERATE THE BOARD BEFORE THE GATE** (`board.py … --check` → *"matches
  measured reality (66 criteria)"*). `-66` edited no paper; the 66 did not move.
- **▲ `dx` + long-running work: `nohup … &` inside a `dx` call survives**, but **`print(flush=True)`
  is not enough — the log stayed at 0 bytes for minutes.** Check liveness with
  `ps aux | grep -c "[w]t117b"` (the bracket trick; and remember `grep -c` **exits 1 on a count
  of zero**, which is a correct zero — assert the printed number, not `$?`).
- **▲ `pdftotext` is on darwin and handles every NBER/arXiv PDF tried** (13 of 13 that fetched).
  NBER working-paper PDFs follow `https://www.nber.org/system/files/working_papers/wNNNNN/wNNNNN.pdf`
  and fetch cleanly with a browser `User-Agent`.
- **▲ When a full text is unreachable, that is a RESULT to record, not a gap to paper over.**
  `SCOUT-001` §6 names Bastani & Waldenström (2023), lists the three routes tried, marks it
  **✓◐**, and states in terms that **it carries no weight in any absence claim**.
- **▲ NAME YOUR PATCH SCRIPT IN A FREE `wtNNN` TAG.** Tags now run to **`wt119`; `wt120` is free.**
- **A BATCHED PATCH SCRIPT BEATS N EDITS** — `wt119` is the newest worked example (whole-paragraph
  anchor, `assert count == 1`, `.bak` first, `--dry`, **plus an idempotence guard** so a re-run
  refuses rather than double-applies).
- **EXTEND ANCHORS TO PARAGRAPH BOUNDARIES** in wrapped prose, not sentence boundaries.
- **`awk 'length>100'` COUNTS BYTES** — κ, ρ, —, × are multi-byte. Measure characters in Python.
- **▲ USE ABSOLUTE LOCAL PATHS IN EVERY `cat X | dx --put`** — held again; zero cwd losses this
  session by writing every local artefact to `/home/claude/wt/` and never relying on `cd`.
- **`dx` chokes on multiline / apostrophe-bearing command strings.** Write locally, `--put`, run
  there. `COMMITMSG.txt` → `--put` → `git commit -F`. **Also true of `lessons.py add --text`:**
  keep it one line and apostrophe-free.
- **`lessons.py use` / `record-outcome` can hang past 4 min** — one per `dx` call at 300 s, never
  chained with `&&`. `add` is fast and auto-pushes. *(All four calls this session returned in
  seconds — the hang is intermittent, not reliable.)*
- **Asana `create_tasks` silently drops `projects`** — **it did NOT this session** (both cards
  landed in State Machine on the first call, verified with `get_task opt_fields=projects.name`).
  **Keep verifying anyway**; a flake that stops flaking is not a flake that is fixed.

---

## THE SELF-REVIEW TRIAD, answered in writing
1. **Captured everything for a zero-memory future Opus?** Yes. A 17.5 KB scouting note carrying
   the verdict, the evidence at source, the method failures and the named hole; two `LEDGER`
   entries; four committed instruments each with a docstring saying *why*; `.bak` beside both
   touched docs; three lessons banked global/project; three Asana cards (one closed, two filed).
2. **Learned the hard way and not yet written down?** Now written: the predicate-control rule
   (`WT-101`, banked global), the sum-gate rule (banked global), and the settled prior-art fact
   (banked `wealth-tensor` so no future session re-runs this search). The `wt117b` non-completion
   is disclosed above rather than buried.
3. **The ONE thing that makes the next session's life easier, added THIS pass?**
   **The predicate positive control.** Every project that ever publishes a zero-hit table needs
   it, `REFERENCE-POLICY`'s five passes do not contain it, and it is the only reason this
   session's verdict is `KNOWN` rather than a confident, clean, wrong `CLEAN`. Card
   `1217556161163494` proposes it as that document's **sixth pass**. Runner-up: `SCOUT-*.md` now
   has a worked example — verdict in one markable sentence, what a positive would have looked
   like *declared in the code*, and the hole named in its own section.

---

## JASON-SIZED, not yours to decide
- **(a) `DECISION-001` — CLOSED FOR GOOD.** A was ruled, and the re-allocation test has now run
  and returned `KNOWN`. **There is no follow-up Jason moment on this axis.** `-65` said the next
  one would arrive *after* the search; the search says it does not arrive.
- **(b) Paper IV's title and abstract leading clause** still read *"from the household to the
  sovereign"*. Narrow it, or ratify the appended demotion as sufficient. **NOW THE ONLY OPEN
  JASON ITEM, and it has been the oldest for several sessions.**
- **(c) `P7` is still ONE BOOLEAN** for a criterion that is per-paper with a two-pass counter.
  Adding rows moves the 66, so it wants its own at-bat.

## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` and **say the number**; `roster
leave --who` once; and paste a handoff better than this one into the chat as the **last act**.
