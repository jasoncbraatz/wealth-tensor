---
project: wealth-tensor
session_n: 76
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: a47cf1777cfee46b4df49f78934d4d2e8ae255ff
updated: 2026-08-18
session: wealthTensor-76
live_theme: "Paper II's sixth independent P7 read, taken as assigned, with -75's new axis brought to it as ordered. FIVE findings, five repairs, nothing new carded. The pass has one shape and it is worth stating first: section 7 of Paper II contains, in its own prose, the sentence 'a single command named for numbers it does not produce is a provenance claim that reads as checked and is not' -- and FOUR LINES BELOW IT, promises that wt030_report.py regenerates every number in section 3, when two numbers in 3.3 come from a TEST's sweep and are absent from that command's output. The document coined the rule and broke it within one screen. Then the reading half paid three more, the sharpest being section 3.2's claim that its identity holds 'agent by agent' and is 'stronger than calling it a near-match' -- pinned, until today, by a near-match on one summary statistic."
phase: "Manuscript repair under a settled thesis. Paper II 9-2-4-3-4-5 across SIX reads, still not converging, pair unstarted; Paper III opens at 7, one pass deep, 2694 lines, the biggest unexplored surface; Paper IV at 6. The instrument set has FIVE axes and every pass that added one found what the previous passes structurally could not -- now a three-data-point claim, not an impression."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, not offered: PAPER II'S SEVENTH INDEPENDENT P7 READ, AND IT IS THE FIRST FROZEN-INSTRUMENT PASS IN THIS PROJECT'S HISTORY. -70's rule holds mechanically -- Paper II returned FIVE findings, so it does not release. But -76's rider work changed WHAT the pass should be, and this is the important part: docs/p7-passes.tsv's axis matrix says PAPER II IS AT 5 OF 5 AXES. Every instrument this project has ever invented has now been pointed at Paper II. So DO NOT INVENT A SIXTH -- the rider's part 3 forbids it while cells are empty, and Paper II has none. Run all five, invent nothing, and record `new_instrument: none`. THAT IS THE ENTIRE POINT: across ~10 reads corpus-wide no paper has produced even ONE zero, and every pass has been confounded by a fresh axis. A zero from a frozen instrument set is the first zero that would MEAN anything, and it is the only kind the definition of done can honestly count. DONE WHEN: all five axes run against Paper II BEFORE prose, each with its count recorded -- A1 wt130, A2 grep the document for the failure mode it names, A3 wt133, A4 run wt030_report.py and wt077_tail_index.py and diff their output against every number in section 3, A5 grep every module section 7 names against its paired script; Paper II read end-to-end, all 554 lines; every finding repaired in-pass or carded with a named falsifier; REVIEW-017 exists with its own coverage claim, its own cleared list AND its own not-checked list, and its front matter carries new_instrument/instrument_name/findings_from_new_instrument; docs/p7-passes.tsv gains its row; suite green, board re-checked, coach at Paper II's baseline of 2 conduct / 0 concessive. A ZERO IS THE OUTCOME THIS PROJECT NEEDS AND THIS IS THE FIRST PASS THAT CAN PRODUCE AN HONEST ONE -- say so plainly if you get it, and do not manufacture a finding to make the pass look like work."
blockers: []
drift_flags: ["THE ANECDOTE IS NOW MEASURED AND IT WAS HALF WRONG. -75's rider landed at -76: docs/p7-passes.tsv holds all six P7 passes with a three-valued new_instrument field, and its axis matrix reads 12 OF 15 CELLS FILLED, with ALL THREE EMPTY CELLS ON PAPER III (A2, A4, A5). Two consequences, both load-bearing. (1) Paper II and Paper IV are at 5/5, so their counters can finally decay and -77 is the first frozen-instrument pass. (2) TWO OF THE SIX ROWS ARE `NOT-STATED` for findings_from_new_axis, because -73 and -75 never recorded the split they were later cited as evidence for -- the project has been asserting an attribution it did not measure. AND -71 IS THE ROW THAT CUTS AGAINST THE STORY OUTRIGHT: no new axis, four findings anyway.", "-70's RULE HELD AND RELEASES NOTHING: Paper II returned five findings on its sixth read, so -77 is Paper II again. Two consecutive sessions have now honoured the rule without argument (-75, -76). The next session that wants to override it needs a red instrument or an equivalent, in writing, in ONE line at the top of its handoff -- unchanged from -75.", "PAPER II'S COUNTER IS 9 -> 2 -> 4 -> 3 -> 4 -> 5 AND IS STILL NOT CONVERGING, and -76 is the THIRD data point for the same reading, in its strongest form yet: -76 brought exactly ONE new instrument and TWO of its five findings came from that instrument ALONE. The pair of zero-finding passes the definition of done wants HAS NEVER ONCE BEEN ATTEMPTED WITH A FROZEN INSTRUMENT SET. That is now a measurement about the METHOD, not an impression about the papers, and it may be worth saying out loud INSIDE the definition of done.", "The queue's old item 1, 'Paper I's first P7 pass', remains demoted: Paper I is NOT in definition_of_done and Paper II section 7 calls it 'since superseded by its own internal referee'. Carried unchanged from -71 through -76. BUT -76 adds a four-minute item that touches it: Paper I L568 carries the non-circularity sentence -75 found FALSE in Paper IV and -76 found TRUE in Paper II. It is the untested third instance and it is ONE `git log --diff-filter=A` away.", "wt133's sweep-2 orphan lists are ADJUDICATED FOR PAPER IV and remain UNADJUDICATED for Papers I, II and III. Paper II's NINE uncited entries (Draagulescu, Patriarca, Yakovenko, Gabaix, Piketty, Auerbach, Kaldor, Saez, Toder) are card 1217568192511533 and were deliberately not touched by -76. Sweep 2 does not set the exit code, deliberately; do not read RC 0 as covering them.", "PAPER II's STAMP IS NOW THE SHARPEST CASE FOR CARD 1217568297674954, sharper than Paper IV's: 'Version 0.2, 2026-08-11' while its OWN References note dates a re-verification 2026-08-17, INSIDE the document. Paper IV's stamp is wrong against the git log; Paper II's is wrong against Paper II, and a reader needs no repository access to see it. Sixth data point, commented on the card, not repaired -- the ruling is Jason's and there is no rule to follow."]
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
3. **`docs/p7-passes.tsv`** — new at `-76`, on `-75`'s rider. Six rows, one per `P7` pass, each
   falsifiable by one `git log --diff-filter=A`, plus the **5-axis × 3-manuscript matrix** whose
   count reassigns your at-bat. Read the header block; it carries its own audit instructions.
4. **`docs/LEDGER.md` `WT-124`** — this pass in one entry, including the cleared row worth as much
   as a finding (`IV-5` does **not** generalise to Paper II).

---

## YOUR AT-BAT — ASSIGNED. Do not choose.

**Paper II's seventh independent `P7` read — and it is THE FIRST FROZEN-INSTRUMENT PASS IN THIS
PROJECT'S HISTORY. You invent nothing.**

`-70`'s rule releases nothing: Paper II returned **five**. It is Paper II again. But `-75`'s rider
landed this session and it **changed what the pass should be**, which is the single most useful
thing `-76` did.

**`docs/p7-passes.tsv`'s matrix says Paper II is at 5 of 5 axes.** Every instrument this project has
ever invented — `A1` the quantifier read-forward, `A2` grep the document for the failure mode it
names, `A3` the cross-reference sweep, `A4` run the manuscript's own regeneration commands, `A5`
grep each module against its paired script — has now been pointed at Paper II. **There is no empty
cell to fill and therefore no licence to invent a sixth.** The rider's part 3 is explicit: fill the
empty cells for your manuscript before inventing a new axis. Paper II has none.

**So run all five, add nothing, and record `new_instrument: none`.**

| axis | what to run |
|---|---|
| `A1` | `python3 scripts/wt130_quantifier_sweep.py`, then **read forward** from every flagged line |
| `A2` | grep Paper II for the failure modes it names in its own prose — `-76` found §7 breaking a rule it coined **four lines above itself** |
| `A3` | `python3 scripts/wt133_crossref_sweep.py`, then read the passages **around** every flag (`-75`(i): the sweep cannot see a reference that resolves to the *wrong* thing) |
| `A4` | run `wt030_report.py` and `wt077_tail_index.py` and **diff their output against every number in §3** — `-74` ran them, `-76` diffed them, and the diff is where `II-27` came from |
| `A5` | grep every module §7 names against the script it is paired with; run every command it names |

**Why a frozen pass is the assignment, and it is the whole argument.** Across roughly ten reads
corpus-wide, **no paper has produced even one zero**, and every single pass has been confounded by a
fresh instrument. The definition of done wants **two consecutive zero-finding passes per paper**.
A zero produced while the toolkit is still growing measures the toolkit; **a zero from a frozen
instrument set measures the manuscript**, and it is the only kind the bar can honestly count.
`-77` is the first session in a position to produce one.

**THE RIDER YOU PASS ON, whatever you find.** Fill the empty cells for **your** manuscript before
inventing a sixth axis, and **record your row in `docs/p7-passes.tsv`**. Parts 1 and 2 of `-75`'s
rider **landed in full at `-76`** — the fields are in `REVIEW-016`'s front matter and the ledger and
its matrix exist — so you do **not** need to re-derive any of it.

**A SIXTH AXIS EXISTS AND IS DELIBERATELY PARKED, so you do not re-invent it and do not spend it
early.** `A6`, the docstring axis: §7 hands a replicator `tests/test_redistribution.py` as *"the ones
that hold this paper's claims in place"*, and that file carries a module docstring plus **eighteen
test docstrings** — prose, **asserted by nothing**, of which **exactly one has ever been read against
the manuscript** (at `-65`, only because `DECISION-001` forced it, and it was found still calling κ
the *mechanism* after the paper had retracted that in five places: *"Nothing asserts a docstring, so
the retraction in the manuscript would have left the test suite still making the claim"*). Nineteen
unchecked prose claims inside the artefact the paper points at. **It is a real axis and it will find
things — which is exactly why it must not be spent on the frozen pass.** Spend it on **Paper III**,
where three cells are empty anyway, or on Paper II *after* the frozen pair resolves.

**DONE WHEN:** all five axes run against Paper II **before a word of prose**, each with its count
recorded; Paper II read end-to-end, all 554 lines; every finding repaired in-pass or carded with a
named falsifier; **`REVIEW-017`** exists with its own coverage claim, its own cleared list **and**
its own not-checked list, and its **front matter carries `new_instrument` / `instrument_name` /
`findings_from_new_instrument`**; **`docs/p7-passes.tsv` gains its row**; suite green, board
re-checked, coach at Paper II's baseline of **2 conduct / 0 concessive**.

**A ZERO IS THE OUTCOME THIS PROJECT NEEDS, AND YOURS IS THE FIRST PASS THAT CAN PRODUCE AN HONEST
ONE.** Say so plainly if you get it. Do not manufacture a finding to make the pass look like work —
that is the one way this at-bat can be failed. And do not aim for zero either: `-76` found five.

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
▲ **`docs/p7-passes.tsv`** — `-75`'s rider, landed in full. Six rows + the 5×3 axis matrix, with its
own falsifier command in its header block the way `docs/crossref-dismissed.tsv` carries its audit
instructions. **`scripts/wt136_rider_review016_frontmatter.py`** put the three instrument fields into
`REVIEW-016`'s front matter under the same guard-then-backup ordering.
· `wt133` (**green**), `wt130`, `wt128`/`wt129`/`wt132`/`wt134`, `wt131b` all unchanged. **Tags run
to `wt136`; `wt137` is free.**

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
(e) **THE ANECDOTE IS NOW A FILE, AND IT WAS HALF WRONG.** `docs/p7-passes.tsv` — six rows, one
per `P7` pass, each falsifiable by one `git log --diff-filter=A`. Read it instead of another
paragraph of narrative. Three things fell out of measuring the story six sessions had been telling:
**the matrix reads 12 of 15 cells filled, and all three empties are Paper III** (`A2`, `A4`, `A5`) —
which is why `-77` is Paper II's first *frozen-instrument* pass and why Paper III's counter is not
yet measuring Paper III; **two of the six rows are `NOT-STATED`**, because `-73` and `-75` never
recorded the instrument attribution they were later cited as evidence for; and **`-71` is a row that
cuts against the story outright** — no new axis, four findings anyway. *And filled is not exhausted:
`-76`'s `II-27` came out of a cell `-74` had already filled.*

**(e2) ONE LINE FROM YOU, AND IT IS A CHANGE TO THE BAR, SO IT IS NOT MINE TO MAKE: should the
definition of done require that at least ONE of the two consecutive zero-finding passes brought NO
new axis?** Today's bar is satisfiable by two passes that looked in the same places with the same
tools — the exact failure the new field exists to expose. Yes or no; `-77` is the first session that
could satisfy the stricter version, so a ruling now costs nothing and lands immediately.
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

## TEED UP, NOT CHASED — one estate observation `-76` could not close without hijacking the session

**`G-AL` appears to go silent exactly when a session does what the handoff tells it to.** Observed
twice at `-76`'s wrap, on darwin:

* `~/Scripts/gate-selfcheck.sh` with **no** environment → prints
  `=== G-AL · the session knew what DONE looks like ===` followed by
  `WARN CANNOT VERIFY: no current session tag`.
* `GATE_ROSTER_WHO=big-wealthTensor-76 ~/Scripts/gate-selfcheck.sh` → the output goes
  **`G-AJ` → `GATE SELF-CHECK: PASS ✅` with no `G-AL` section printed at all.**

Both runs exit 0 and both print PASS. If that reproduces, it is `G-AI`'s own species — *a gate step
that vanishes with its instrument* — and it vanishes under the **recommended** invocation, which is
the worst possible case for a check whose whole job is asking whether the session knew what done
looked like. **`-76` did not chase it**: it lives in `~/Scripts`, not this repo, and diagnosing it
would have hijacked a manuscript pass. **The one command that settles it**, and it is cheap:

```
~/Scripts/gate-selfcheck.sh > /tmp/a.out 2>&1
GATE_ROSTER_WHO=big-wealthTensor-77 ~/Scripts/gate-selfcheck.sh > /tmp/b.out 2>&1
diff <(grep -o '=== G-A[A-Z][^=]*' /tmp/a.out) <(grep -o '=== G-A[A-Z][^=]*' /tmp/b.out)
```

Empty diff → `-76` misread its own tail and this note should be deleted. Non-empty → file it in
**State Machine**, not the Batter's Box: a Claude with darwin can fix it.

---

## AT WRAP

`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` **and say the number** (summary line,
never `$?`, never through a pipe); **`python3 scripts/wt133_crossref_sweep.py` and say its RC**;
`roster leave --who <you>` once; and **paste a handoff better than this one into the chat as the
last act.** Assign `-78` ONE at-bat with a definition of done. Do not hand them a menu. 🥎
