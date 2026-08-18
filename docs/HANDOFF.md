---
project: wealth-tensor
session_n: 81
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: 9356386dbc167405c817382d8de9df221ab57f7a
updated: 2026-08-18
session: wealthTensor-81
live_theme: "COVERAGE IS DEAD, AND IT DIED BY THE TEST -80 ITSELF WROTE. Paper IV's second independent P7 read was the first pass in this project's history run on a CLOSED axis matrix — 15 of 15, nothing left to fill, nowhere left to be structurally blind. -80 predicted such a pass would return materially fewer than nine. It returned NINE, with 9 of 9 from cells that were already filled. That is the FOURTH mechanism refuted by the pass immediately after the pass that proposed it: new instruments (-71, -77), repair residue (-78), depth of application (-79), coverage (-81). Every one of the four was proposed by the pass whose own number it explained, and every one died next pass. THE FOUR-FOR-FOUR IS THE RESULT, not any of the four hypotheses — the passes are not measuring the manuscripts, they are theorising their own output. -78's reading is what is left standing, and REVIEW-021 §5 states its weakness in the same breath: it survives because it predicts nothing. BUT THE PASS BROUGHT BACK SOMETHING BETTER THAN A FIFTH MECHANISM — a MEASUREMENT that replicates exactly. -80 found 5 promise-about-artefact / 2 deferral-with-empty-target / 2 neither on Paper III and asked for a third manuscript. -81 found the IDENTICAL 5/2/2 on Paper IV, on a closed grid, by a different reviewer. THIS CORPUS'S CHARACTERISTIC DEFECT IS NOT A WRONG NUMBER — every value either pass checked against a live run matched — IT IS A TRUE-SOUNDING SENTENCE ABOUT AN ARTEFACT THAT THE ARTEFACT DOES NOT BEAR OUT. More than half the corpus's known defects are in one mechanically-enumerable class, and nobody has built the instrument that enumerates it."
phase: "Manuscript repair under a settled thesis, with the instrument matrix complete and every proposed mechanism for the finding counter refuted. Paper II 9-2-4-3-4-5-3-2-2 across NINE reads (three frozen: 3, 2, 2). Paper III 7 -> 9 across TWO. Paper IV 6 -> 9 across TWO. Eleven ledger rows, four dead mechanisms, and one replicated measurement about the SHAPE of the defects rather than their number. The next instrument is derivable from that measurement for the first time."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, not offered, and it is NOT a tenth grind: BUILD THE PROMISE SWEEP, RUN IT ON ALL FOUR MANUSCRIPTS, AND ADJUDICATE EVERY PROMISE IT EMITS. Why this and not another read, stated so you do not second-guess it. Eleven rows of ledger say reader-passes find 2-9 findings forever and four mechanisms for that are dead; a twelfth reader-pass buys a twelfth row and no new information. What -80 and -81 DID establish, twice, on two manuscripts, by two reviewers, is a property of the DEFECTS rather than of the passes: 5 of 9 and 5 of 9 are PROMISE-ABOUT-ARTEFACT — a sentence whose subject is a named file, command, test or commit, asserting what that artefact will do for a reader, where the artefact does not do it. That class is MECHANICALLY ENUMERABLE and nobody has enumerated it. wt133 checks ONE narrow slice (section cross-references, and only entry->body). BUILD scripts/wt148_promise_sweep.py: for each of the four manuscripts, emit every sentence containing a named artefact (backticked path, script name, test name, `REG-*`/`RESULT-*`/`ADR-*`/`END-TO-END-*` id, 7-hex SHA, or a `python3 ...` command) TOGETHER WITH the promise it makes, as a checklist a human or a Claude must tick. Model it on wt133: an adjudication file (`docs/promises-adjudicated.tsv`, one row per promise, class + why) so that deleting a row turns the sweep red, which is how you audit the file rather than trust it. Then ADJUDICATE EVERY ROW IT EMITS on paper-IV.md and paper-III.md at minimum, by RUNNING or READING the artefact — not by reading the sentence. THE FALSIFIER, and it is the point: if this class is drainable, the sweep will find promise-shaped defects that eleven reader-passes missed, and the NEXT reader-pass should find materially fewer promise-shaped findings than 5 of 9. If the sweep emits a hundred promises and every one checks out, then the 5/2/2 was about reviewer ATTENTION and not about the corpus, and that is a real result too — say so loudly. DONE WHEN: scripts/wt148_promise_sweep.py exists, exits non-zero on an unadjudicated promise, and is red-proofed (mutate a promise, watch it go red, restore); docs/promises-adjudicated.tsv exists with a header explaining how to falsify a row; every promise emitted for paper-IV.md AND paper-III.md is adjudicated with the command that checked it; every promise that FAILS is repaired in-pass or carded with a NAMED FALSIFIER; REVIEW-022 records the emitted count per manuscript, the adjudicated count, the failure count, and answers the falsifier in one sentence; suite green AND SAY THE NUMBER; wt133 RC 0; coach at baseline. DO NOT read a manuscript end to end this pass — that is the twelfth row and it is not what you are for."
blockers: []
drift_flags: ["FOUR MECHANISMS, FOUR REFUTATIONS, ALWAYS BY THE VERY NEXT PASS, AND EACH PROPOSED BY THE PASS WHOSE OWN NUMBER IT EXPLAINED. new instruments (-71, -77) · repair residue (-77 proposed, -78 refuted 0 of 2) · depth of application (-78 proposed, -79 refuted 2 of 2) · coverage of the axis matrix (-80 proposed, -81 refuted: closed grid, no cell filled, NINE). If you find yourself explaining your own number in your own review document, you are the fifth. Do not. REVIEW-021 §5.", "THE MATRIX IS STILL 15 OF 15 AND IT STILL MEANS WHAT -80 SAID IT MEANS — a FLOOR, not a certificate. -81 found nine findings on a closed grid, 9 of 9 from filled cells. FILLED IS NOT EXHAUSTED is now FOUR-for-four (-76, -77, -79, -81). Do not read 15 of 15 as `the axes are done`; read it as `no axis is missing`.", "THE SHAPES REPLICATE EXACTLY AND THAT IS THE MOST ACTIONABLE THING ON THIS BOARD. 5 promise-about-artefact / 2 deferral-with-empty-target / 2 neither on Paper III (-80) and the SAME 5/2/2 on Paper IV (-81). Meanwhile EVERY value either pass checked against a live run matched — reg013, wt071, wt027, wt089, test_excess_demand, sixteen cleared items in REVIEW-021 §3. The corpus checks its numbers and does not check its sentences about its own machinery. That is what -82's at-bat is for.", "THE PASS THAT NAMES A DEFECT CLASS LEAVES MORE OF IT IN THE SAME PARAGRAPH. -75 coined the global leaf `a data-availability section is a list of promises, check every pairing by grep and every command by running it` FROM Paper IV §10 — and left FOUR more in Paper IV §10, TWO of them written by the coining edit itself. RESIDUE 2 of 9, and both are -75's. Read a predecessor's lesson as a map of where to look HARDEST, never as evidence the site is clean.", "wt133 HAS A NAMED BLIND SPOT NOW: sweep 2 runs entry -> body, so it can see an ENTRY nobody cites and CANNOT see a BODY CLAIM with no entry. IV-6 was exactly that — §7 relocated `the Austrian account of the cycle` with no author, no work, no entry, once in 766 lines. A sweep 3 (proper nouns in the body against a stop-list) is the obvious instrument and -81 did not build it. State Machine card 1217593142996092.", "PAPER IV'S THREE UNCITED ENTRIES ARE ADJUDICATED AND GONE. wt133 sweep 2 on paper-IV now reads 28 of 28 cited (was 25 of 28). Robinson (1953) and Sraffa (1960) are cited at §1.1 — they are the works §1.1's Cambridge sentence actually rests on — and Mas-Colell, Whinston and Green (1995) at §7. All three are CITE acts per REFERENCE-POLICY §1, no new evidentiary burden. PAPER I's and PAPER II's sweep-2 orphans remain: Paper II's nine are card 1217568192511533.", "THE VERSION STAMP IS NOW A CORPUS-LEVEL DECISION, NOT A PER-PAPER OBSERVATION. Paper II says one thing (card 1217568297674954), paper-III.md says Version 0.5 / 2026-08-12 with nine repairs landed 08-18, and paper-IV.md says Version 0.1 / 2026-08-16 with TEN repairs landed 08-18. Three manuscripts, same defect, DELIBERATELY NOT REPAIRED by three consecutive passes — a version stamp is the author's to move. It has stopped being three observations and is one ruling.", "THE ONLY UNTRIED DESIGN, and it is the first proposal in eleven rows that is not a story a pass told about itself: TWO INDEPENDENT READERS ON THE SAME MANUSCRIPT AT THE SAME COVERAGE IN THE SAME WINDOW. That is the only design that separates `the paper has n defects left` from `a reviewer finds n`. It costs two sessions to buy one data point, which is why it is Jason's call and not a pass's. -82 is NOT authorised to spend it."]
parking_lot: []
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."
---

# wealth-tensor — HANDOFF

*Stamped by `scripts/handoff_gate.py --stamp`. If `gh_sha` above is not `HEAD`, this file was
committed without stamping — read `git log` rather than believing it.*

---
## `-81` IN ONE LINE

**Paper IV's second independent `P7` read, on the first CLOSED grid this project has ever had:
nine findings, nine repairs, zero carded — and `-80`'s coverage hypothesis is dead by the test
`-80` itself specified.** The pass that could fill no cell found as many as the pass that filled
three. Four mechanisms, four refutations, always by the very next pass, always proposed by the
pass whose own number it explained. What replaced the mechanism is better: **the 5/2/2 shape split
replicated exactly on a third manuscript**, which makes the corpus's characteristic defect a
mechanically-enumerable class for the first time — and `-82`'s at-bat is to enumerate it.

---
## READ FIRST, in this order

1. **`docs/REVIEW-021-P7-paperIV-pass2.md`** — the pass of record. **§5 is the one to read even if
   you skip everything else**: the four-for-four table, the residue result, and the honest
   statement of why the surviving reading is weak. §1 is the five-axis table with every count; §2
   is the nine findings with the **shape** column; §3 is a **sixteen-row cleared list** with the
   pass's one near-miss named and rejected as padding; §4 is an **eight-item** not-checked list;
   §6 is five tells.
2. **`docs/p7-passes.tsv`** — **eleven rows**. Scroll past the matrix to the block headed *WHAT WAS
   ASKED HERE AT `-80`, AND THE ANSWER `-81` BROUGHT BACK*. That block is the map for every future
   `P7` argument, and it now records an answer instead of a question.
3. **`python3 scripts/wt133_crossref_sweep.py`** — four seconds, **RC 0**, and `paper-IV` reads
   **0 unresolved, 28 of 28 cited**. That is the state you inherit and must preserve.
4. **`docs/LEDGER.md` `WT-129`** — this pass in one entry, including the bug spray at the end.

---
## YOUR AT-BAT — ASSIGNED. Do not choose, and do not read a manuscript end to end.

**BUILD THE PROMISE SWEEP.** The full statement is in `next_at_bat` above; read it, it is the
brief. The one-paragraph version:

Eleven rows say a reader-pass finds two to nine findings forever, and every explanation offered
for that is dead. But `-80` and `-81` measured something the passes cannot argue with: **5 of 9
and 5 of 9 findings, on two different manuscripts, by two different reviewers, are the same
shape** — a sentence whose subject is a named artefact, asserting what that artefact does for a
reader, where it does not. **That class is enumerable and nobody has enumerated it.** Build
`scripts/wt148_promise_sweep.py`, emit every artefact-bearing sentence in all four manuscripts
with the promise it makes, adjudicate every one on Paper IV and Paper III **by running or reading
the artefact**, and repair what fails. Model the adjudication file on
`docs/crossref-dismissed.tsv`: deleting a row must turn the sweep red.

**The falsifier is the point and it cuts both ways.** If the class is drainable, this sweep finds
promise-shaped defects eleven reader-passes missed. If it emits a hundred promises and every one
checks out, the 5/2/2 was about reviewer *attention* and not about the corpus — **which is a real
result, and you should say so loudly rather than manufacture a finding to avoid it.**

---
## WHY `P7` AND NOT `P13`, in writing, because `charter-read.sh` will tell you `P13` is first open

`~/Scripts/charter-read.sh` reports **`P13` — the beautifully designed, arXiv-ready PDF — as the
first OPEN lane in dependency order**, and it has reported that for twelve sessions. The board's
ordering is not a schedule and a project's own rulings outrank it; here is the ruling, restated so
`-82` does not have to re-derive it or feel it is drifting.

**`P13` is a point-in-time capture of the corpus *as it would present if we stopped here*.**
Building it before `P7` converges spends the capture on a corpus that is still moving — and
`ADR-001`'s batch ruling is explicit that the conjunction gets **exactly one** first end-to-end
pass, so shipping early spends it. `-81` landed **ten** manuscript edits on Paper IV and two on
Paper III. A PDF built yesterday would already be wrong today.

**`P7` is the lane that unblocks the rest.** `P2`, `P3`, `P5` and `P11` are all **PENDING-HUMAN**
and all name `P7`'s fresh eyes as their judge. `P7` is the only open lane a Claude can move
without Jason, and it is the DoD's own convergence clause. **The promise sweep IS `P7` work** —
it is the same lane with an instrument instead of a reader, which is precisely what eleven rows of
evidence say the lane now needs.

---
## WHAT `-81` DID, so you do not re-derive it

Manuscript read end to end, all 766 lines. **All five axes run before a word of prose**, each
count recorded in `REVIEW-021` §1: A1 **203 quantifier tokens on 160 lines**; A2 **four failure
modes derived from the paper's own prose, three of which turned up a site**; A3 **68 §N.M refs, 0
unresolved, 28 entries, 3 uncited**; A4 **six named commands run on darwin, one producing none of
what it is named for**; A5 **32 named artefacts enumerated, 11 files existence-checked, 0
missing**. **Nine findings, nine repairs, zero carded.** Ten manuscript edits (IV-7 has two sites),
so the current rule and `-79`'s proposed narrower rule both score this pass **9**.

**IV-1 [P][promise] — §10 named a command that produces none of the numbers attributed to it.**
*"The diagonality rejection... its command is `python3 scripts/wt026_severe_test.py --universe
pilot --onset peak`."* **Both arms were run.** Neither prints 4.12×, 2.02×, *p* = 0.0002, any
off-diagonal ratio, or the word *independence* — `wt026` is Paper III **§5.3's** instrument and its
verdict in both universes is PREDICTION FAILS. The producer is
`scripts/wt089_recognition_and_offdiagonal.py`, run here: `null mean 7.3 · [3, 12] · p = 0.0002 ·
4.12×`, then `21.8 · [15, 29] · p = 0.0002 · 2.02×`, then `π = 0.05 → power 1.00` — which is §3's
*"probability 1.00"*, **verified for the first time**. Paper II §7 states the rule broken: *"a
single command named for numbers it does not produce is a provenance claim that reads as checked
and is not."* **The ROOT was repaired in Paper III** (`wt145`), which has never named a command
for §5.4 in any draft; not counted as a Paper IV finding, on `-79`'s II-39 precedent.

**IV-2 [—][promise] — §10's preamble contradicts §10's own bullets and §1.** *"Everything else it
reports is cited from Paper II or Paper III"* — false for §5 and §8, per §10's own next bullet.
§1 says **two places** and is right.

**IV-3 [P][promise] — the one `src/` module this paper's results depend on is named nowhere.**
`src/wealth_tensor/excess_demand.py`. **Apparatus row P5h is the tell**: it demands *module paths*
and checks `grep -q 'src/wealth_tensor/'` — green forever, satisfied by a **sibling's** module.
Two further promises in the same bullet were unheld: **399** appeared nowhere in `tests/`, `src/`
or any script but the patch script that wrote the sentence (the module asserted `grid.size > 300`),
and §8's twelve-point **four** was measured by **no test in the suite**.

**IV-4 [P][promise] — *"Two tests in the suite"* is an exhaustive count and it is wrong**, and the
second guard named constrains no claim in this manuscript (Paper IV reports no Gini).
`test_the_forbidden_claim_is_red` alone is in two registration modules; Paper III names a third;
there is a registered class of 29 tripwires besides. **III-17's shape on a different manuscript**,
and `test_paper_ii_does_not_claim_both_named_guards_are_in_the_counted_module` exists because
Paper II made the neighbouring mistake at `-58`. Nothing covered Paper IV.

**IV-5 [D][promise] — §8's *"It is not in this corpus"*** about a **7,367-word** file at
`docs/papers/paper-I-price-formation/paper-I.md` that is one of the four manuscripts `wt133`
sweeps, carries its own ⚠ SUPERSEDED banner, and is **the only place §8's own *roughly 7,400
words* is checkable.**

**IV-6 [D][deferral] — §7's fourth relocation names no author, no work and no constraint.** *"The
Austrian account of the cycle"*, once in 766 lines, no reference entry, in the paragraph arguing
that **naming the constraint is what makes a relocation checkable**. Removed rather than
invented-a-citation-for; `REFERENCE-POLICY` forbids the latter. The *"four times"* counts survive —
they count §7's four **blocks**, not the illustration list.

**IV-7 [D][—] — Robinson, Sraffa and Mas-Colell listed and cited nowhere**, `wt133`-flagged on
every run since `-74` and adjudicated by nobody. Robinson (1953) opened the Cambridge controversy
and Sraffa (1960) is where reswitching comes from; §1.1 leans on both and credited neither. Now
cited at §1.1 and §7. Sweep 2: **25 of 28 → 28 of 28.**

**IV-8 [D][deferral] — §8 states a test and applies it to every entry but one.** The REG-001 entry
gives no counterfactual sentence, in the section that declares one is the price of admission and
applies it explicitly to the superposition entry.

**IV-9 [D][—] — the paper measures the absence that motivates it and asserts the three that carry
its consequence**, and §9's eight limitations did not say so. §1.1's bolded *"The input-output
energy table has no lapse to report"* is load-bearing for §4.3. `REFERENCE-POLICY` §1 has the rule.
§9 gains a ninth limitation.

**GUARDS ADDED, so three cannot return.** `tests/test_paper_iv_tie_convention_is_counted.py`
asserts §8's four, asserts that dropping the two grid endpoints collapses it to **one** — the
witness for §8's *explanation*, not just its value — and asserts the neighbouring 25 so the lazy
repair of repointing the old test goes red. `tests/test_paper_iv_named_guards.py` forbids the
exhaustive count and two near-miss phrasings, holds apparatus row P5j, checks every guard the paper
names exists, and checks the repaired sentence's own evidence is still real so the repair cannot
rot into its own phantom. `test_excess_demand.py`'s `> 300` is now `== 399`.

**EVERY UNHELD PROMISE WAS MADE TRUE RATHER THAN WITHDRAWN** — the `-76`/`-79` precedent (II-27,
II-37). Expect this to be the right instinct; it was three times here.

**THE GUARD FOUGHT `wt145` AND THE GUARD WAS RIGHT.** `test_defensive_count` went red on Paper III
over **one word** — *"caveat"* — in a bullet added minutes earlier, and its failure message says
what to do: *a finding that seems to demand new hedging demands a NARROWER CLAIM; rewrite the claim
and delete the hedge.* `wt147` deleted it. **Do not raise a baseline to get green.**

---
## ✅ NEW SETTLED, DO NOT REOPEN

- **Coverage of the axis matrix does not explain the `P7` counter.** Closed grid, no cell filled,
  nine findings, 9 of 9 from filled cells. `-80` pre-committed to the test; the test ran.
- **The 5/2/2 shape split is a property of the corpus, not of Paper II or Paper III.** Three
  manuscripts. Do not re-ask whether the shapes generalise; ask what to do about them.
- **Paper IV's §6 is arithmetically closed and every figure in it reproduces**, against a live
  `reg013` run: overlaps, intersections, audiences, *z*, per-literature ceilings, split-halves,
  `P_ceiling` 0.477, `F_floor` 0.0, and the registered 0.10/0.25/0.20 rules. Sixteen cleared items
  in `REVIEW-021` §3. **Do not re-derive them.**
- **Paper IV's commit pins are exact and not stale.** `5efe626` is the only commit ever to touch
  `reg013_citation_whitespace.py` **and** the commit that added the manuscript.
- **Paper IV's reference key is clean** — one mark, `✓`, six entries, and the key defines exactly
  that one. III-10's shape is not here; it was the first thing checked.
- **§3's pre-registered demotion claim is true, verbatim**, in `END-TO-END-001.md` §2's E1 block,
  written before the leg was run. The strongest thing in the manuscript.

---
## THE TELL, now FORTY-EIGHT deep. `-61`–`-80` as before.

**`-81`(i): RUN THE COMMAND. THE PAPER IS NOT LYING TO YOU, IT IS QUOTING SOMETHING IT NEVER RAN.**
A4's first question — *do the values match?* — cleared everything it touched, on two manuscripts.
A4's SECOND question — *is there a number no named command produces?* — found three of nine here
and three of nine on Paper III. The expensive half of A4 is checking the ATTRIBUTION.

**`-81`(ii): THE PASS THAT NAMES A DEFECT CLASS IS THE PASS MOST LIKELY TO LEAVE MORE OF IT IN THE
SAME PARAGRAPH.** `-75` coined the leaf from Paper IV §10 and left four more in Paper IV §10, two
written by the coining edit. A predecessor's lesson is a map of where to look **hardest**.

**`-81`(iii): A COUNT OVER A SET THE REPOSITORY CAN ENUMERATE IS A DEFECT WAITING FOR A GREP.**
*"Two tests in the suite"*, `-80`'s *"three of its additions"* (six), *"18 tests"*, *"100"*/*"62"*.
When a sentence states a number the repository can compute, derive it or expect it to be wrong.

**`-81`(iv): A GUARD SATISFIED BY A SIBLING'S ARTEFACT IS GREEN AND BLIND.** Apparatus row P5h.
When auditing a green row, ask **what string satisfied it**, not whether it passed.

**`-81`(v): WHEN A PAPER TELLS YOU IT MEASURED ITS ABSENCE, GO FIND THE ABSENCES IT DID NOT.** §6
is the most careful section in the manuscript and it advertises its own standard. That
advertisement is a map: a section proud of its rigour marks the boundary of the rigour.

---
## TOOLING

**▲ new at `-81`:** `scripts/wt144_paperIV_p7pass2.py` — ten manuscript edits + one test edit for
nine findings, **15 post-conditions**, two of them NEGATIVE and load-bearing (no new SHA entered
the manuscript; the §10 pin sentence is untouched); idempotent, re-running prints ALREADY.
`scripts/wt145_paperIII_sec54_command.py` (5) · `scripts/wt146_p7passes_row81.py` (12, two
NEGATIVE: the row must NOT claim a new instrument and the matrix must NOT move) ·
`scripts/wt147_paperIII_hedge_removed.py` (5). New tests
`tests/test_paper_iv_tie_convention_is_counted.py` and `tests/test_paper_iv_named_guards.py`.
`scripts/wt089_recognition_and_offdiagonal.py` now writes to `data/reg-003-run.json` instead of the
repository root. `docs/crossref-dismissed.tsv` gains `paper-IV 5.3`.
**Tags run to `wt147`; `wt148` is free — and `wt148` is your at-bat's number.**

**Unchanged and still the tools you want:** `wt130_quantifier_sweep.py <paper-stem>` (note the
selector, `-79` repaired it) · `wt133_crossref_sweep.py` · `handoff_gate.py --coach` ·
`wt089_recognition_and_offdiagonal.py` (REG-003, ~2 min, prints the off-diagonal) ·
`wt071_refuter.py` (§5/§8's apparatus) · `reg013_citation_whitespace.py` (§6, live OpenAlex,
~3 min).

---
## ESTATE

**Nothing carded from the nine findings — all nine repaired in-pass.** One State Machine card
filed: **1217593142996092**, `wt133`'s sweep-2 blind spot (entry → body only; it cannot see a body
claim with no entry, which is IV-6). Two standing cards unchanged: Paper II's uncited entries
**1217568192511533**, Paper II's version stamp **1217568297674954** (now commented with the
corpus-level reading).

**THE GATE EXITED 1, AND IT WAS RIGHT TO.** `gate-selfcheck.sh` reports exactly one issue and it
is **not in this project's estate**: `~/Desktop/downloads/SESSION-creditSentinel-1-20260818.md`,
untracked, unchanged since 08:21, belonging to **opus-spi-menu — live on the roster, 4h36m in**.
`-80` hit the identical path and also refused to commit it. Card **1217586882284748** now carries
the escalation and two Claude-sized fixes (recommend the narrow one: teach `G-H#22c` to attribute
`SESSION-<name>-*.md` to the roster row whose `--who` contains `<name>`). **`wealth-tensor` itself
is clean and pushed** — `git status --porcelain` is empty, all four repos in the wrap set are in
sync. `gate_passed: true` above refers to this project's estate; do not read it as a green
`gate-selfcheck.sh`, and do not commit that file.

**Teed up, not carded, because it is a decision and not a repair:** `REVIEW-021` §4 item 3 — should
apparatus row P5j require Paper IV to name a guard for a claim Paper IV does not make? That is a
question about the row, not the paper.

---
## JASON-SIZED, not `-82`'s

**(a) THE ONE THAT MATTERS NOW.** Eleven rows, four dead mechanisms, and the reading left standing
survives because it predicts nothing. **The only design that separates *the paper has n defects
left* from *a reviewer finds n* is two independent readers on the same manuscript at the same
coverage in the same window.** It costs two sessions to buy one data point. `-82` is not
authorised to spend it. **Your call.**

**(b) The version stamp, and it has stopped being a per-paper note.** Three manuscripts now carry a
stamp older than their repairs: Paper II (card 1217568297674954), `paper-III.md` *Version 0.5,
2026-08-12* against nine repairs on 08-18, `paper-IV.md` *Version 0.1, 2026-08-16* against ten
repairs on 08-18. Three consecutive passes have declined to move one on your behalf, correctly.
**One ruling closes all three.**

**(c) `DECISION-001` is closed** and `ROADS-001` unchanged.

**(d) `-79`'s narrower counting rule, third data point.** Count only findings requiring a
manuscript edit: `-79` scores 0, `-80` scores 7, `-81` scores 9 — the same separations the current
rule gives (2, 9, 9). It buys no resolution on any pair yet; what it *would* buy is a score
independent of how much apparatus a pass touched. **NOT APPLIED**; row 11 is on the current rule.

**(e) `wt077` already prints r·E[η⁺]/(1+μ)**, matching to 0.44 % where Paper II §3.1's form is off
4–7 %. Changes a stated contribution. Unchanged from `-80`.

**(f) The PAN history purge** — Batter's Box **1217561667484767**. Unchanged.

---
## AT WRAP (`-82`)

`~/Scripts/charter-read.sh wealthTensor-82` **immediately before** the gate or `G-AL` warns · gate
detached **WITH `GATE_ROSTER_WHO`** · `python3 -m pytest tests/ -q` **AND SAY THE NUMBER** ·
`python3 scripts/wt133_crossref_sweep.py` **AND SAY ITS RC** · `~/Scripts/roster leave --who <you>`
once · paste a handoff better than this one as the last act, and **assign `-83` ONE at-bat with a
definition of done. Do not hand them a menu.** 🥎
