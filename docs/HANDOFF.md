---
project: wealth-tensor
session_n: 76
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: PENDING
updated: 2026-08-18
session: wealthTensor-76
live_theme: "Paper II's sixth independent P7 read, taken as assigned, with -75's new axis brought to it as ordered. FIVE findings, five repairs, nothing new carded. The pass has one shape and it is worth stating first: section 7 of Paper II contains, in its own prose, the sentence 'a single command named for numbers it does not produce is a provenance claim that reads as checked and is not' -- and FOUR LINES BELOW IT, promises that wt030_report.py regenerates every number in section 3, when two numbers in 3.3 come from a TEST's sweep and are absent from that command's output. The document coined the rule and broke it within one screen. Then the reading half paid three more, the sharpest being section 3.2's claim that its identity holds 'agent by agent' and is 'stronger than calling it a near-match' -- pinned, until today, by a near-match on one summary statistic."
phase: "Manuscript repair under a settled thesis. Paper II 9-2-4-3-4-5 across SIX reads, still not converging, pair unstarted; Paper III opens at 7, one pass deep, 2694 lines, the biggest unexplored surface; Paper IV at 6. The instrument set has FIVE axes and every pass that added one found what the previous passes structurally could not -- now a three-data-point claim, not an impression."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, not offered: PAPER II'S SEVENTH INDEPENDENT P7 READ. -70's rule holds mechanically -- Paper II returned FIVE findings, so it does not release. Bring the axis Paper II has never had: THE DOCSTRINGS. Section 7 hands a replicator `tests/test_redistribution.py` as the artefact that holds this paper's claims in place; that file contains EIGHTEEN test docstrings plus a module docstring, all of them prose, NONE of them asserted by anything, and exactly ONE has ever been audited against the manuscript -- at -65, and only because DECISION-001 forced it, where the docstring was found still making a claim the manuscript had already retracted ('kappa is the mechanism'). Nineteen unchecked prose claims inside the object the paper points at. DONE WHEN: every docstring in tests/test_redistribution.py, plus the two named guards' docstrings wherever they live, is read against the manuscript's CURRENT text and each recorded agrees/contradicts/stale, BEFORE a word of prose; wt133 and wt130 run first and their counts are the coverage claim; Paper II read end-to-end, all 554 lines; every finding repaired in-pass or carded with a named falsifier; REVIEW-017 exists with its own coverage claim, its own cleared list AND its own not-checked list; suite green, board re-checked, coach at Paper II's baseline of 2 conduct / 0 concessive. A ZERO IS A RESULT -- say so plainly if you get one and do not manufacture a finding to make the pass look like work."
blockers: []
drift_flags: ["-70's RULE HELD AND RELEASES NOTHING: Paper II returned five findings on its sixth read, so -77 is Paper II again. Two consecutive sessions have now honoured the rule without argument (-75, -76). The next session that wants to override it needs a red instrument or an equivalent, in writing, in ONE line at the top of its handoff -- unchanged from -75.", "PAPER II'S COUNTER IS 9 -> 2 -> 4 -> 3 -> 4 -> 5 AND IS STILL NOT CONVERGING, and -76 is the THIRD data point for the same reading, in its strongest form yet: -76 brought exactly ONE new instrument and TWO of its five findings came from that instrument ALONE. The pair of zero-finding passes the definition of done wants HAS NEVER ONCE BEEN ATTEMPTED WITH A FROZEN INSTRUMENT SET. That is now a measurement about the METHOD, not an impression about the papers, and it may be worth saying out loud INSIDE the definition of done.", "The queue's old item 1, 'Paper I's first P7 pass', remains demoted: Paper I is NOT in definition_of_done and Paper II section 7 calls it 'since superseded by its own internal referee'. Carried unchanged from -71 through -76. BUT -76 adds a four-minute item that touches it: Paper I L568 carries the non-circularity sentence -75 found FALSE in Paper IV and -76 found TRUE in Paper II. It is the untested third instance and it is ONE `git log --diff-filter=A` away.", "wt133's sweep-2 orphan lists are ADJUDICATED FOR PAPER IV and remain UNADJUDICATED for Papers I, II and III. Paper II's NINE uncited entries (Draagulescu, Patriarca, Yakovenko, Gabaix, Piketty, Auerbach, Kaldor, Saez, Toder) are card 1217568192511533 and were deliberately not touched by -76. Sweep 2 does not set the exit code, deliberately; do not read RC 0 as covering them.", "PAPER II's STAMP IS NOW THE SHARPEST CASE FOR CARD 1217568297674954, sharper than Paper IV's: 'Version 0.2, 2026-08-11' while its OWN References note dates a re-verification 2026-08-17, INSIDE the document. Paper IV's stamp is wrong against the git log; Paper II's is wrong against Paper II, and a reader needs no repository access to see it. Sixth data point, commented on the card, not repaired -- the ruling is Jason's and there is no rule to follow."]
parking_lot: []
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."

---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-76` IN ONE LINE

**Took the assigned at-bat as ordered and brought the assigned instrument to it.** Paper II read end
to end, all 554 lines. **Five findings, five repairs (`wt135`), nothing new carded.** Paper II's
counter goes to **5**.

**The headline is one screen of text disagreeing with itself.** §7 writes *"a single command named
for numbers it does not produce is a provenance claim that reads as checked and is not"* — and
**four lines below**, promises that `python3 scripts/wt030_report.py` regenerates **every** number
in §3. Two numbers in §3.3 — *"the minimum is **interior**, 0.451 at *P* = 30"* and *"the whole
sweep spans 0.035"* — are **true** and come from a **test's** sweep, not that command's. `-72`'s
standing lesson paying out on the document that coined it.

**And the reading half paid three more.** The sharpest: §3.2 claims its ρ = 0 identity holds *"agent
by agent rather than merely on the summary statistics"* and that saying so is *"stronger than calling
it a near-match."* The only committed check — the test file's self-described **HEADLINE** — was
`pytest.approx(abs=0.01)` on **one summary statistic**. The claim is true (`np.array_equal`, max abs
diff **0.0**) and nothing was watching it.

Suite **1078 passed, 0 failed** (67.50 s). `test_redistribution.py` **18 passed**, so §7's, the
abstract's and §1's shared count survives the patch. `wt133` **RC 0**. Coach **RC 0, Paper II at
baseline 2 / 0**, before and after. Abstract, front matter and references **byte-identical**,
asserted in `wt135`'s guards.

---

## READ FIRST, in this order

1. **`docs/REVIEW-016-P7-paperII-pass8.md`** — the pass of record. **§1.2 is the one to read even if
   you skip everything else**: it is the grep-and-run table, four modules and three commands, and it
   is where two of the five findings came from. §1.3 lists **39 numbers regenerated cell by cell**;
   §3 is a **22-row cleared list** with an `M/R/A` column; §4 is the **five-item not-checked list**,
   which also records the **four items closed at drafting** so the shrinkage is auditable.
2. **`python3 scripts/wt133_crossref_sweep.py` — run it first, before you read anything.** Four
   seconds, **green**, and that is the state you are responsible for preserving.
3. **`docs/LEDGER.md` `WT-124`** — this pass in one entry, including the cleared row worth as much
   as a finding (`IV-5` does **not** generalise to Paper II).

---

## YOUR AT-BAT — ASSIGNED. Do not choose.

**Paper II's seventh independent `P7` read — and the new axis is THE DOCSTRINGS.**

`-70`'s rule releases nothing: Paper II returned **five**. It is Paper II again.

**The instrument, and it runs before prose.** §7 hands a replicator `tests/test_redistribution.py`
as *"the ones that hold this paper's claims in place."* That file contains a module docstring and
**eighteen test docstrings** — several of them long, several of them argumentative, **none of them
asserted by anything**, and **exactly one has ever been audited against the manuscript**: at `-65`,
where `test_reallocation_intensity_is_what_the_base_caps`'s docstring was found still calling κ the
*mechanism* after the manuscript had retracted that in five places. Its own comment says it:
*"Nothing asserts a docstring, so the retraction in the manuscript would have left the test suite
still making the claim — the abstract-versus-body defect one file out."*

**That was found once, by accident, because `DECISION-001` forced someone to look. Nineteen of them
have never been read against the paper at all.**

For each: read it against the manuscript's **current** text and record `agrees` / `contradicts` /
`stale`. Then read the prose.

**Why this and not another careful read.** It is the same shape that produced `II-27` and `II-30`
today and `IV-2` on Paper IV: **prose that a replicator is pointed at and no instrument checks.** A
docstring is the purest form of it — unasserted prose inside the artefact the data-availability
section names.

**DONE WHEN:** every docstring in `tests/test_redistribution.py` — plus the two named guards'
docstrings wherever they live — is read against the manuscript's current text with its verdict
recorded, **before a word of prose**; `wt133` and `wt130` run first and their counts are your
coverage claim; Paper II read end-to-end, all 554 lines; every finding repaired in-pass or carded
with a named falsifier; **`REVIEW-017`** exists with its own coverage claim, its own cleared list
**and** its own not-checked list; suite green, board re-checked, coach at Paper II's baseline of
**2 conduct / 0 concessive**.

**A ZERO IS THE OUTCOME THIS PROJECT NEEDS.** If you find nothing, say so plainly and do not
manufacture a finding to make the pass look like work — that is the one way this at-bat can be
failed. Equally do not aim for zero: `-76` found five where `-74` found four.

### THE QUEUE BEHIND IT — context, not a menu. Do not shop here.

1. **Paper III's second read** — counter at 7, one pass deep, 2 694 lines. Still the biggest
   unexplored surface in the corpus, and still not your at-bat, for the reason in one line above.
2. **`REFERENCE-POLICY`'s eighth pass** — card `1217556161163494`. **Five sessions deferred**, the
   single most-deferred item in the project.
3. **`III-8`** — card `1217567136996151`. §11 names no regeneration command for Paper III's §4.
4. **`IV-4b`** — card `1217574341282011`. The `reg013` / §10-pin booby trap.
5. **`II-25`** — card `1217568297674954`, now six data points deep and Paper II is the sharpest.
6. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
7. **The nine uncited reference entries** — card `1217568192511533`.

---

## WHAT `-76` DID, so you do not re-derive it

**`II-27`** — §7's command does not produce §3.3's `P = 30` row or its 0.035 span. Measured today at
*T* = 1200: **0.4507** and **0.0353**. Both were added by `-74` from a *test's* sweep in the same
pass that edited §7 twice. **Repaired by making the promise true**, not by weakening the prose:
`P = 30` joins `wt030_report.py`'s periodicity tuple, and `wt135`'s fourth post-condition **re-runs
the patched command and demands the row**.

**`II-28`** — §3.2's *"agent by agent … stronger than calling it a near-match"*, pinned by a
near-match. Verified true and now asserted with `np.array_equal`. **Guard honesty confirmed in both
directions before the line was written**: passes at ρ = 0.00, fails at ρ = 0.10 / 0.25 / 1.00.

**`II-29`** — §5.5 still says *"three Var[log *a*] values"* while citing, in the same sentence, the
§7 that `-74` moved to **four**. Third site of `II-22`, and the one that points at the fix.

**`II-30`** — §7's *"in the same suite"* sits four lines under a bullet naming
`tests/test_redistribution.py`; the test is in `tests/test_excess_demand.py`. Repaired by copying
§1's own correct pattern, *"a companion module of the same suite"*, and naming the module.

**`II-31`, the softest and named as such** — §7's enumeration of non-simulation numbers is one
short: §3.4's **(N−1)/N = 0.99875** is printed by neither named command.

**Carded:** nothing new. `1217568297674954` gains its sixth and sharpest data point.

---

## ✅ NEW SETTLED, DO NOT REOPEN

**The 39 numbers in `REVIEW-016` §1.3 were regenerated on 2026-08-18. Do not re-derive them.** In
particular:

* **All 24 cells of §3.1's table, §3.2's ρ table, §3.3's threshold and periodicity endpoints and
  §3.4's four derived figures reproduce exactly** from `wt030_report.py`, and §3.1's **four**
  closed-form quantities reproduce exactly from `wt077_tail_index.py`.
* **Contribution 2's "within 7 % at every rate tabulated" was checked at ALL SEVEN flow rates**, not
  the three §3.1 quotes: **4.4 %–6.8 %, monotone in the rate.** It holds.
* **§7's commit pin `3b11f23` is exact** — `git log -1` on the module returns it, and
  `git show --stat` touches only that module and its test file.
* **`IV-5` DOES NOT GENERALISE TO PAPER II.** `paper-II.md` was added by **`d655501`**, which touches
  no `src/` file. §7's *"a paper cannot cite the commit that adds the paper"* is **true here**.
  **Paper I carries the same sentence at L568 and is the untested third instance** — one
  `git log --diff-filter=A` away, and deliberately left for a session that has Paper I in scope.
* **The ρ = 0 identity is bit-exact**, not approximate: `np.array_equal` on the 800-vector at
  *T* = 600 **and** *T* = 1200, max abs diff **0.0**.
* **`-75`(i)'s reader-only check was run on all 41 of Paper II's §-references and Paper II is
  CLEAN** — no foreign section number collides with a local heading. Both `§4.1`s are Benhabib's and
  attributed at both sites; `§4` is `REFERENCE-POLICY`'s and named at the site; §7's `§3.2` is Paper
  II's own and correct.

---

## THE TELL, now TWENTY-NINE deep

`-61`–`-74` as before. `-75`: a sweep finds references that resolve to nothing, only a reader finds
the ones that resolve to the wrong thing · a data-availability section is a list of promises, so
grep every pairing and run every command · a guard that cannot pass and a guard that cannot fail are
the same bug wearing different clothes · a not-checked item closeable in four minutes should be
closed, not written down.

**`-76`(i): WHEN A DOCUMENT NAMES A FAILURE MODE, START AT THE PARAGRAPH THAT NAMES IT.** `-72`
established that a document articulating a defect is worth searching for that defect. `-76` tightens
the aim: §7 coined the rule and **broke it four lines below itself**. A section that can articulate a
defect was written by someone reasoning about the defect **in the abstract**, not auditing themselves
against it — and the audit is the cheap part. *(Folded into `-72`'s existing leaf rather than forked;
the dupe-guard fired at sim 0.64 and it was right.)*

**`-76`(ii): A COMPARATIVE ADJECTIVE IN A MANUSCRIPT IS A POINTER AT AN ASSERTION THAT SHOULD
EXIST.** §3.2 said its identity was *"stronger than calling it a near-match"* and the only committed
check **was** a near-match. The prose named the exact weakness of its own guard and no one followed
the pointer. **Grep manuscripts for *"exactly"*, *"stronger than"*, *"bit-identical"*, *"agent by
agent"*, *"to machine precision"* — and diff each against the assertion that pins it.** Free, and it
found the paper's headline claim unpinned.

**`-76`(iii): REPAIR THE PROMISE, NOT THE PROSE, WHEN THE PROSE IS TRUE.** `II-27` could have been
closed by deleting *"0.451 at P = 30"* from §3.3. That would have removed a **true, load-bearing**
observation — the interior minimum is the whole reason periodicity is trim rather than monotone — to
make a stale command look correct. One line in `wt030_report.py` made the promise true instead. **When
a section's claim and its provenance disagree, ask which one is right before deciding which one moves.**

---

## TOOLING (▲ new at `-76`)

▲ **`scripts/wt135_paperII_p7pass8.py`** — three manuscript edits, one script edit, one **test
assertion**, under `wt129`'s guard ordering, with **four post-conditions**: front-matter-and-abstract
identity, references identity, `wt133`'s sweep re-run on the patched text, and — the new one —
**running the patched `wt030_report.py` and asserting the row the manuscript names is in its
output**. Its docstring carries a `NOT DONE HERE` block per `wt134`'s pattern.
▲ **The post-condition that re-runs a patched *script* rather than re-reading a patched *document*.**
`wt134` re-ran a sweep on the patched text; `wt135` re-runs the **artefact it edited** and greps its
stdout for the manuscript's own number. That is the cheapest available proof that a provenance
repair actually repaired provenance.
· `wt133` (**green**), `wt130`, `wt128`/`wt129`/`wt132`/`wt134`, `wt131b` all unchanged. **Tags run
to `wt135`; `wt136` is free.**

---

## JASON-SIZED, not yours

(a) `DECISION-001` closed. (b) Paper IV framing ruled.
(c) **`P7` is still ONE BOOLEAN — and the argument is now SEVEN sessions deep.** `-70` moved the
board with an edit that changed no sentence; `-71` changed five and it did not move; `-72` three;
`-73` thirteen; `-74` seven including the first edit to a test's assertions; `-75` eight across six
findings; `-76` **five across five findings, including a second edit to a test's assertions and the
first edit to a regeneration script**. It has not moved once in seven sessions. **One line from you
settles it: yes add the coverage row, or no, reviewing stays narrative.**
(d) **Does a `P7` repair pass bump a manuscript's minor version, or does the stamp only move at
submission?** Card `1217568297674954`, **six data points, and Paper II is now the sharpest**: its
stamp reads *"Version 0.2, 2026-08-11"* while its **own References note** dates a re-verification
**2026-08-17**. Paper IV's stamp is wrong against the git log; **Paper II's is wrong against Paper
II**, and a reader needs no repository access to see it. Second half still worth a word: if the stamp
only moves at submission, it should **say** it is a first-draft date.
(e) **The process finding, now with a THIRD data point and in its strongest form.** Paper II's
counter is 9 → 2 → 4 → 3 → 4 → **5**. `-76` brought exactly **one** new instrument and **two of its
five findings came from that instrument alone**. **The pair of consecutive zero-finding passes the
definition of done requires has never once been attempted with a frozen instrument set.** That is a
measurement about the method, not an impression about the papers — and it is the strongest argument
yet for saying so *inside* the definition of done.
(f) The PAN history purge — Batter's Box `1217561667484767`.

---

## WHY NOT `P13`, since `charter-read.sh` asks

`charter-read.sh` reports **`P13` as the first OPEN lane in dependency order** — the beautifully
designed, arXiv-ready PDF. `-76` worked **`P7`** instead, as assigned, and the project's own ordering
ruling is why: **`P13` is a point-in-time capture of the corpus**, and capturing a corpus whose
manuscripts still yield findings per read produces a beautiful PDF of prose that is about to change.
`P7` → `P13` → `P8` is the DoD's own sequence.

**`-76` sharpens `-75`'s sharpening by one turn.** `-75` observed that a point-in-time capture whose
own point in time is wrong on all four papers, and wrong by construction, is not a capture. `-76`
found the first case where **the document itself proves the stamp wrong without any external
reference**: Paper II dates its own bibliography work six days after the version it claims to be.
`P13` should not move until `II-25` is ruled and Paper II's and Paper III's pairs are at least
started.

---

## AT WRAP

`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` **and say the number** (summary line,
never `$?`, never through a pipe); **`python3 scripts/wt133_crossref_sweep.py` and say its RC**;
`roster leave --who <you>` once; and **paste a handoff better than this one into the chat as the
last act.** Assign `-78` ONE at-bat with a definition of done. Do not hand them a menu. 🥎
