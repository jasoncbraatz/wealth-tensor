---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: PENDING
updated: 2026-08-18
session: wealthTensor-86
session_n: 86
live_theme: "EVERY ROW IN docs/promises-adjudicated.tsv CAN NOW BE RE-RUN BY SOMEONE WHO WAS NOT THERE, AND THE FIRST THING THAT BOUGHT WAS A FALSE SENTENCE. wt156 asked the question BEFORE wt154's: not `did the adjudicator read the artefact` but `can step 1 of this file's own falsification procedure be carried out at all today`. 46 of 129 rows could not -- 36 whose evidence located the record in a session log that no longer exists, 10 whose evidence was a verb with no operand. All 46 are repaired with a command run on 2026-08-18 and the value it returned that day. Of the sixteen the handoff named, 12 agreed with their old note, 2 carried HEAD-indexed values that had legitimately moved, and 2 DISAGREED. One of those two exposed a FALSE SENTENCE that had stood since the section existed: Paper IV section 10 said tests/test_excess_demand.py ASSERTS section 8's twelve-point four, and the module asserted no such thing -- its only twelve-point test counts demand curves and asserts 25. The four is TRUE when measured, so wt158 added the assertion rather than weakening the sentence, and section 8's number is now machine-checked. Both rows had sat on the evidence `read the module`."
phase: "The TSV is clean at BOTH its criteria: wt154 RC 0 (evidence reads rather than locates) and wt156 RC 0 (evidence is runnable today), over 130 rows, with 11/11 and 10/10 post-conditions. What -86 did NOT do is the parking-lot sweep it is now best placed to specify: the pronoun defect it found in the EVIDENCE column ('the script', 'the module') lives in the PROSE too, as pointers whose target is a bare noun phrase, and BOTH existing sweeps miss that class by construction. That is -87's at-bat."
gate_passed: PENDING
gate_version: "2.60"
next_at_bat: "ASSIGNED, ONE THING: FIND THE POINTERS WHOSE TARGET IS A BARE NOUN PHRASE. -86 built a detector for evidence columns that name no runnable handle, and two of the three rows its own author's committed prediction MISSED were missed for one reason: `grep -n E7 on the script` and `grep for each of the three names in the script and the module` read as perfectly runnable, and are not, because `the script` and `the module` are PRONOUNS whose referent the reader silently supplies from a neighbouring column. The same defect is in the manuscripts and neither existing sweep can see it: wt133 resolves section references and reference entries, wt156 reads the TSV, and a sentence saying `recorded in the run log` or `given in the appendix` or `listed in that section` is invisible to both. This is the third item on the parking lot, put there by -83 as the syntax its III-2 and III-3 findings lived in. Write `scripts/wt160_bare_pointer_sweep.py`: over paper-III.md and paper-IV.md, flag every pointer construction -- `recorded in|named in|given in|listed in|documented in|stated in|set out in|reported in <X>` -- where <X> carries NO backticked path, NO section N.M, and NO programme identifier (PRE-00N, REG-0NN, WT-0NN, RESULT-*, REVIEW-0NN), i.e. where the reader must guess which artefact is meant. RC 1 when any flags, RC 0 when none, plus --json. COMMIT THE PREDICTED COUNT BEFORE YOU RUN IT, with the measured field reading PENDING, exactly as -84 did for its sample and -86 did for its sweep -- -86's prediction was wrong by three and the three misses were the finding, which is only true because the prediction was a git object first. THE SEVERE TEST IS IN GIT: -83's III-2 and III-3 were repairs of exactly this syntax; `git log -S` on the repaired phrases finds the repair commit, and its PARENT is the revision at which the sweep MUST flag them, while at HEAD it MUST NOT. Put that before/after pair in the script as post-conditions with at least two NEGATIVE -- a NEGATIVE that matters here is a pointer whose target IS named (`recorded in `docs/preregistration/RESULT-002-pilot-run.log`') and which must not flag. DONE WHEN: wt160 exists and is committed with the before/HEAD pair IN the script; docs/REVIEW-027 reports the predicted count, the measured count, and every row where they disagree; every flagged pointer repaired in-pass -- either the target named concretely in the sentence, or, where the pointer genuinely has no single target, the sentence rewritten so it stops promising one; wt148 RC 0, wt133 RC 0, wt154 RC 0, wt156 RC 0, wt160 RC 0; suite green AND SAY THE NUMBER; coach at baseline. DO NOT widen `#scope` to Papers I and II -- still parked, still deliberate, FIVE passes running. DO NOT re-open REVIEW-026's census; the file is clean at both criteria and re-measuring it is the cheap substitute for the work that is actually left."
blockers: []
drift_flags:
  - "ONE FALSE SENTENCE WAS FOUND AND REPAIRED BY STRENGTHENING THE ARTEFACT, NOT THE PROSE. Paper IV section 10 claimed tests/test_excess_demand.py asserts section 8's twelve-point four; it did not, and until 2026-08-18 nothing in the repository checked that number. It is TRUE (measured: exactly 4 distinct excess-demand schedules on the 12-point grid across the 25 allocations), so wt158 added the assertion. Anyone re-reading section 8 should know the four became machine-checked on 2026-08-18 and was a paragraph before that."
  - "THE 46 ARE A TARGETED STRATUM AND MUST NOT BE READ AS A DRAW. 1 false sentence in 46 rows gives Wilson 95% [0.4%, 11.3%], and that does NOT narrow REVIEW-024's [3, 47] of 129, because the stratum's defining property (unrunnable evidence) is not the property [3, 47] estimates (false sentences). The only thing -86 moves is the FLOOR: one more false sentence is now known and repaired. Any session quoting 1/46 as a rate is making REVIEW-025 section 3's mistake one level further out."
  - "wt154 HAS A BLIND SPOT -86 FOUND AND DID NOT PATCH: it scores an exit-code predicate as a LOCATE. `git merge-base --is-ancestor A B; echo $?` prints nothing to stdout and answers with a return code, and D1 flagged it as naming no content-printing operation. An exit code IS a read -- the same class wt154 already declines to flag for a named test. wt159b widened the EVIDENCE instead (the predicate stays, two timestamps added beside it) and the instrument is carded, 1217613775009402, with a named falsifier. A future session repairing a row with a predicate will hit this."
  - "TWO ROWS CARRY VALUES PINNED TO A HEAD THAT HAS MOVED, AND THAT IS NOT A DEFECT SO MUCH AS A DESIGN NOTE. 6d9934a0bc and c14cdd1f1b recorded `1090 passed at HEAD 73b77f9`; the suite is 1095 now. Naming the revision was RIGHT and it is still uncheckable without a checkout. Both sentences are about the PINNED commit d655501, which tests/test_paper_test_counts_are_derived.py asserts, so nothing failed -- but a value indexed to HEAD does not belong in a row whose job is to be falsifiable."
  - "PAPERS I AND II ARE STILL OUT OF SCOPE AND 28 PROMISES THERE ARE CHECKED BY NOBODY. The sweep prints it on every run -- not silent truncation. Widening `#scope` is ONE LINE of data and goes red immediately. FIVE passes have now parked it."
  - "THE VERSION STAMP IS STILL ONE RULING CLOSING THREE MANUSCRIPTS, and EIGHT consecutive passes have now correctly declined to move it on Jason's behalf. Paper IV took a section 10 repair on 08-18 and its stamp did not move with it. Card 1217568297674954."
  - "THE TWO-INDEPENDENT-READERS DESIGN IS STILL THE ONLY INSTRUMENT LEFT AND IT IS STILL JASON'S CALL. -85's census was named the last cheap substitute; -86's sweep was a DIFFERENT question (runnability, not discrimination) and so does not contradict that, but it is not a third substitute either. Every remaining question about how many defects a reader would find still costs a reader."
  - "wt133 STILL HAS ITS ONE-DIRECTIONAL SWEEP-2 BLIND SPOT (entry -> body, never body -> entry). State Machine 1217593142996092. Unchanged."
  - "lessons.py's CONTRIBUTOR STAMP STILL DOES NOT RESOLVE FROM THE ROSTER -- -86 hit it again and passed `--contributor big-wealthTensor-86` on every add, which works, and all seven leaves are stamped. Still teed up, not fixed."
parking_lot:
  - "Widen `#scope` in docs/promises-adjudicated.tsv to paper-I and paper-II and adjudicate the 28 promises there. One line of data, then the work. FIVE passes have now parked this."
  - "wt133 sweep 3: proper nouns in the body against a stop-list, to catch a body claim with no reference entry (IV-6's class). State Machine 1217593142996092."
  - "Patch wt154's D1 to score an exit-code predicate as a read, with a POSITIVE (synthetic predicate row does not flag) and a NEGATIVE (a bare `ls -l` row still does), and disclose how far the count moves. Card 1217613775009402. Tag wt161+."
  - "roster-brake's exit #1 cannot help when the paths you touched ARE the whole dirty tree; ROSTER_BRAKE_ACK=N is the answer and is ranked second. State Machine 1217596263441666."
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."
---

# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

*Stamped by `scripts/handoff_gate.py --stamp`. If `gh_sha` above is not `HEAD`, this file was
committed without stamping — read `git log` rather than believing it.*

---

## ⚠ BEFORE ANYTHING ELSE: `git log --oneline -8`

**-86 was handed -85's prompt after -85 had already finished, pushed, and left.** Two minutes of
`git log` and a read of *this file* turned a duplicated at-bat into a fresh one. The prompt in your
context is a **snapshot of an intention**; the repository is the **state**. When they disagree, the
repository wins, and you say so out loud in your first message rather than quietly working the wrong
thing. Check `roster who` and `rail` in the same breath — a sibling may be mid-inning.

---

## STEP 0 · BRIDGE-BUG ACK, then transport (zero bridge calls)

The desktop bridge rotates its websocket every ~27–33 min (claude-code#81248). **DARLISH DOES NOT
USE IT.** Asana/Gmail/Twilio MCP tools ARE bridge-bound: if one vanishes mid-turn it self-heals in
~1s — retry next turn, and **never declare "can't continue" over it**. Never restart the Claude app
for a darlish problem.

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
```
Post the printed `DARLISH-ENROLL v1 id=… fp=…` line, **EXACTLY**, as an Asana comment on task
**1217316841710435**; then run `/tmp/darlish-up` again; then

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-87 --task "The bare-pointer sweep: wt160"'
```

**READY first try at -61 through -86 — TWENTY-SIX for twenty-six.** Budget four minutes; it takes two.

- ⚠ `roster join` returns RC=0 with **NO OUTPUT** on a re-join, and prints `absorbed N row(s) …
  (carried 1 claim(s))` when it adopts a `cloud-<fp>` identity from an earlier command in the same
  container. That line is the healthy path, not a warning.
- ⚠ `roster claim` syntax: `--who X --resource wealth-tensor --task "..."` — **resource is a NAMED flag.**
- ▲ **If you have to change your own name mid-session** (as -86 did, -85 → -86): `join` under the new
  name, `claim` under the new name, THEN `leave --who <old>`. `leave` on a name that is not this
  session leaves your own identity untouched and tombstones the old row for an hour. It is clean.
- ⚠ `roster-brake` **WILL** block your first `git add` commit, reporting you as `cloud-<fp>`
  contending with your own human name. **`ROSTER_BRAKE_ACK=N` is the answer**, ranked SECOND in the
  brake's own output. Card 1217596263441666. -86 set it on every commit and lost nothing.
- At -86's wrap the board carried `opus-spi-menu` (claims STALE) and a live `opus-florist-order`.
  Neither touches `wealth-tensor`. The rail lane was idle, metaQa / ledgerLens / helloRelay all
  `complete`.

### THEN STAGE THE DOCS AS ONE TARBALL

```
mkdir -p /home/claude/wt          # FIRST. $HOME is /root in the container.
/tmp/dx 'cd ~/repos/wealth-tensor && git pull --ff-only && tar czf /tmp/wt-docs.tgz docs scripts tests'
/tmp/dx --get /tmp/wt-docs.tgz /home/claude/wt/wt-docs.tgz
```

- ⚠ Stage `tests/` **too**.
- ⚠ `tar xzf` prints macOS xattr warnings with the extraction **perfectly fine**.
- ⚠ `.bak` files **sort first**. Read the path, not the first line.
- ⚠ **ANYTHING THAT IMPORTS `src/` MUST RUN ON DARWIN** — wt027 / wt002 / wt026 / wt071 / wt089 and
  all of pytest. `wt133` / `wt148` / `handoff_gate --coach` are pure-doc and run **locally in under
  a second**; run all three before you read anything. `wt154` and `wt156` shell out to `git show`
  for their post-conditions, so they need the repo and run on darwin.
  ▲ **A script under `tests/` that you invoke directly needs `PYTHONPATH=src`**; pytest supplies it
  and a bare `python3` does not. -86 lost one turn to that.
- ⚠ ABSOLUTE local paths in every `cat X | /tmp/dx --put`.
- ⚠ **NEVER** pipe a command through `dx` whose exit code you intend to read — redirect inside the
  remote command and echo `$?` there.
- ▲ Nested quotes → write the script **LOCALLY**, `--put` it, run `dx 'bash /tmp/x.sh'`. -83 wrote
  all seven of its scripts that way, -84 all six, -85 all four, **-86 all six**, and none of the four
  lost a turn. WRITE THE FILE.
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to `/tmp/wt87/`, poll with a second
  `dx`. **pytest takes ~70s and is worth backgrounding**; -86 launched eight regeneration runs in
  one backgrounded batch and read them all fifteen minutes later, which is the whole reason the
  sixteen re-runs cost nothing.
- ▲ **A `dx` call that is interrupted client-side may still have RUN on darwin.** -86's `lessons.py`
  batch was cancelled mid-flight and every add had already landed; the re-run reported seven
  `sim 1.00` dupes, which is the tell. **Check for the effect before re-running a mutating dx call.**

---

## THE STATE YOU INHERIT AND MUST PRESERVE

🟢 `python3 -m pytest tests/ -q` → **1095 passed, 0 failed, 69.66 s.** RUN IT AND SAY THE NUMBER.
   (1094 before; `wt158` added one.)
🟢 `python3 scripts/wt148_promise_sweep.py` → **RC 0**, **130 adjudicated**: paper-III 88 of 88
   (81 H · 6 N · 1 R), paper-IV **42 of 42** (40 H · 2 R).
🟢 `python3 scripts/wt133_crossref_sweep.py` → **RC 0**.
🟢 `python3 scripts/wt154_evidence_discrimination_sweep.py` → **RC 0**, 130 rows, 0 flagged, 10/10
   post-conditions. RC 2 means the sweep itself is broken.
🟢 ▲ `python3 scripts/wt156_reproducibility_sweep.py` → **RC 0**, 130 rows, 0 flagged, **11/11
   post-conditions, 4 NEGATIVE**, including the `b50bccd`-vs-HEAD pair. RC 2 means broken.
🟢 coach: paper-III **5 conduct / 0 concessive**; paper-IV **1 / 0**.
🟢 GATE: **PASS**, gate v2.60.

**Wrap order:** commit → `--stamp` → commit → push → `charter-read.sh` → gate → `--emit`.
The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.

---

## ▶ YOUR AT-BAT · THE POINTERS THAT POINT AT NOTHING

Read `next_at_bat` above; it is the specification and it is one thing. The short version:

`the script`, `the module`, `the run log`, `that section` — a pointer whose target is a **bare noun
phrase** promises the reader a specific artefact and does not name one. -86 found this class in the
`evidence` column, by accident, because its own committed prediction missed two rows for exactly
that reason. **wt133 cannot see it** (it resolves `§N.M` references and reference entries) and
**wt156 cannot see it** (it reads the TSV, not the prose). It is -83's III-2/III-3 syntax and it has
been on the parking lot since.

Predict the count, commit the prediction, then run the sweep. Repair every flag. Say what the
prediction got wrong — that is the part the next session cannot get from the code.

---

## WHAT -86 DID

**The instrument.** `scripts/wt156_reproducibility_sweep.py`. Two detectors, reported separately,
with the `b50bccd`-vs-HEAD pair inside it as post-conditions.

- **D1 · RECORD IN A VANISHED SESSION** — the evidence locates the result in a session, a log or a
  machine, and nothing re-executable survives once those locators are stripped. **36 rows.**
- **D2 · NO OPERAND** — the evidence is a verb or a back-reference with nothing to act on. **10 rows.**

**The handoff's own rule and its own post-condition contradicted each other, again.** The
commissioned rule was *a run with no committed output file, no printed value in the note, and no
named test*; five of the sixteen carry real values in their notes (`D(0)=1998.9895`, `4.12x`,
`9 severe, 0 definitional, 0 failed`), so the literal rule cannot flag them, while the commissioned
post-condition says all sixteen must. This is **-85(ii) arriving a second time**, and the answer was
the same: build the rule the FILE's own header licenses — *step 1 of the falsification procedure,
applied to the column the header names* — rather than bend the one that was handed over.

**The prediction was committed at `127cec9` with every measured field reading `PENDING`, and it was
wrong by three, all low:** `6c9aacc322` (`ls -l + git ls-files on darwin`, simply overlooked),
`01ed28c1a8` and `1d538d6e60` (`grep … on the script`, `grep for each of the three names in the
script and the module`). Those last two are the finding, and they are -87's at-bat.

**The sixteen, re-run on darwin 2026-08-18.** 12 agreed · 2 had HEAD-indexed values that had moved
· **2 disagreed**.

- **`d4dd6baf17`** — the note said *"a clean run would not regenerate §6 either — the audience is a
  live citing set that grows daily."* A clean run returned **RC 0 and every figure §6 reports,
  unchanged**: 23 / 15 / 6, 0.0202 / 0.0108 / 0.0053, 134 / 155 / 380, ceiling 0.4773, floor 0.0,
  `H1 SURVIVES`. Only the seed `cited_by` counts moved, and two of four audience sizes were
  byte-identical two days on. `wt157` rewrote §10 to say **replication, not regeneration**, kept the
  load-bearing sentence verbatim, and **committed the re-run's JSON** as
  `docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json` — which emitted a new promise,
  `df3cdc8d2a`, adjudicated in the same pass.
- **`10d2d456ea` / `30191fec1a`** — **the false sentence.** §10 said `tests/test_excess_demand.py`
  *asserts* §5's **399** and §8's twelve-point **four**. The 399 is asserted at
  `assert grid.size == 399`. **The four was asserted nowhere** — the module's only twelve-point test
  counts DEMAND curves and asserts 25, and never builds the excess-demand set at all. Measured, the
  12-point grid returns exactly **4** distinct excess-demand schedules, so `wt158` **added the
  assertion** instead of softening the prose. Both rows had sat on the evidence `read the module`.

**Four notes corrected without any sentence failing:** `d9f85198a4` and `ff83025f93` shared a note
saying *"RESULT-001-* logs entered at d655501 and the analysed result later"* — `RESULT-001-wt026.md`
is IN `d655501`; PRE-002's own outcome, `RESULT-002-wt026.md`, is the one that came later, at
`c43c484`, twelve minutes on. `150f86a167` put *"written before the leg ran"* in E1 §2.2; §2.2 is the
type check and §6 carries that sentence.

**RED-PROOF, this pass, on the real tree, twice.** wt157's C7 failed on its first run because the
load-bearing sentence had re-wrapped across a line, and the script **rolled back and changed
nothing** — the check was then made whitespace-insensitive rather than dropped. And wt159 refuses
outright unless its repair set is **exactly** the set wt156 flags, then re-runs the sweep at
`b50bccd` afterwards and requires all 46 still to flag there: the repair moved the FILE, not the
instrument.

---

## THE TELL, now SEVENTY-EIGHT deep

-61–-85 as before. **-86 adds seven.**

**-86(i) AN EVIDENCE COLUMN THAT NAMES A PLACE INSTEAD OF A COMMAND CANNOT REACH STEP 2 OF ITS OWN
FALSIFICATION PROCEDURE** — and the rule must be written against the column the file's own header
names as the handle. Letting a neighbouring column rescue the row collapses the count to near zero
and makes the file unfalsifiable by construction, which is the exact failure the sweep exists to
detect. Put that objection in the falsifier block and invite the attack.

**-86(ii) "THE SCRIPT" AND "THE MODULE" ARE PRONOUNS, AND A HUMAN SKIMMING AN EVIDENCE VOCABULARY
SUPPLIES THE REFERENT WITHOUT NOTICING THEY HAVE DONE IT** — two of a committed prediction's three
misses read as perfectly runnable commands and neither is. The machine cannot borrow context from
the next column over, which is the whole argument for running the sweep rather than reading the list.

**-86(iii) WHEN A MANUSCRIPT SAYS A TEST MODULE ASSERTS A NUMBER AND IT DOES NOT, MEASURE THE NUMBER
BEFORE YOU TOUCH THE PROSE** — if it is true, add the assertion and the sentence becomes true; only
if it is false is this a manuscript repair. The cheap fix weakens the paper, the right one
strengthens the artefact, and the two are told apart by one measurement.

**-86(iv) A NOTE THAT PINS ITS VALUE TO HEAD IS HONEST AND STILL UNCHECKABLE ONCE HEAD MOVES** —
`1090 passed at HEAD 73b77f9` names its revision, which is strictly better than not naming it, and a
later reader still cannot re-run it without a checkout. Pin to a REGISTERED commit, or to an
invariant a green test asserts.

**-86(v) AN EXIT CODE IS A READ, AND A DETECTOR THAT REQUIRES STDOUT WILL FLAG A PREDICATE AS A
LOCATE** — `git merge-base --is-ancestor A B; echo $?` is the right evidence for a claim about order
and wt154 flagged it. When a repair pass trips an instrument the pass is not about, **widen the
EVIDENCE and card the INSTRUMENT**; patching a committed detector's criterion mid-repair is how a
count and its criterion drift apart unnoticed.

**-86(vi) A REASON WHY A RE-RUN WOULD FAIL IS NOT EVIDENCE; THE RE-RUN IS** — and its output belongs
in the repository beside the claim. "A clean run would not regenerate §6" was a plausible,
well-argued, *false* prediction that had been sitting in an adjudication note as though it were a
finding.

**-86(vii) A PASTED HANDOFF IS A SNAPSHOT OF AN INTENTION; THE REPOSITORY IS THE STATE** — check
`git log --oneline -8` and read `docs/HANDOFF.md` before you swing, and when they disagree say so in
your first message. -86 was handed -85's prompt after -85 had finished and pushed; two minutes of
`git log` turned a duplicated at-bat into a fresh one.

---

## TOOLING (▲ new at -86)

- ▲ `scripts/wt156_reproducibility_sweep.py` — the runnability sweep. `--json`, `--rev REV`,
  `--skip-postconditions`. RC 0 / 1 / **2 (post-condition failed — the sweep is broken)**. Reports
  `no_value_in_note` alongside the flags.
- ▲ `scripts/wt157_paperIV_s10_reg013_rerun.py` — §10's reg013 bullet, 12 post-conditions, 5
  NEGATIVE; refuses on a moved anchor; refuses if the re-run does NOT reproduce the committed run;
  rolls back from `.bak-wt157`.
- ▲ `scripts/wt158_twelve_point_four.py` — adds the assertion of §8's four, 10 post-conditions, 5
  NEGATIVE, runs pytest on the module as one of them.
- ▲ `scripts/wt159_tsv.py` — the 46 re-adjudications + 1 new row, 13 post-conditions, 4 NEGATIVE;
  **refuses unless its repair set equals wt156's flag set**; keys the new row's sentence off
  `wt148 --json` so it is byte-exact.
- ▲ `scripts/wt159b_tsv.py` — one evidence column widened after wt154 flagged a predicate,
  9 post-conditions; runs all four sweeps as post-conditions.
- ▲ `docs/REVIEW-026-reproducibility.md` — the rule, the prediction-vs-measurement, the sixteen
  re-run, **§4 the false sentence**, **§5 what this does NOT do to [3, 47] and wt154's blind spot**.
  Five-way falsifier block in the front matter.
- ▲ `docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json` — the committed record of the
  2026-08-18 replication.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and **can** 429 — never put it in a critical path.
  It did NOT 429 on 2026-08-18; it returned RC 0. Budget for both.
- Tags run to **wt159b**; **wt160 is free**.

---

## ESTATE

**Two cards with named falsifiers:**
- `1217603625863293` — `RESULT-001-wt026.md`'s summary line says "320 events" where its own §§1–2
  report 120 and 202 (=322). Paper III prints 322 in both places and is unaffected. Not repaired
  in-pass on purpose: the ruling wants to be made once, by Jason, then applied.
- ▲ `1217613775009402` — wt154's D1 scores an exit-code predicate as a LOCATE. Named falsifier and
  the shape of the fix are in the card.

**Standing cards unchanged:** `1217593142996092` (wt133 sweep 2 one-directional),
`1217568297674954` (version stamp), `1217568192511533` (Paper II's nine orphans),
`1217596263441666` (roster-brake), `1217596233063153`, `1217561667484767` (PAN purge, Batter's Box).

---

## JASON-SIZED, not -87's

- **(a) THE TWO-INDEPENDENT-READERS DESIGN IS STILL THE ONLY INSTRUMENT LEFT.** -82's prediction,
  -84's audit and -85's census were the three cheap substitutes. -86's sweep asked a *different*
  question (runnability, not discrimination) and so is not a fourth — but it is not a substitute
  either. Every remaining question about how many defects a reader would find costs a reader.
- **(b) The version stamp** — ONE ruling closing THREE manuscripts; EIGHT passes have declined it.
  Paper IV took a §10 repair on 08-18 and its stamp did not move.
- **(c) The `RESULT-001` in-place-edit ruling**, card `1217603625863293`.
- **(d) DECISION-001 closed, ROADS-001 unchanged.**
- **(e) wt077 already prints r·E[η⁺]/(1+μ)**, matching to 0.44% where Paper II §3.1's form is off
  4–7% — changes a stated contribution, unassigned since -81.
- **(f) The PAN history purge.**
- **(g) lessons.py's contributor stamp** still does not resolve from the roster.

---

## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)

`docs/CHECKLIST.md`'s first OPEN lane in dependency order is **P13** (the arXiv-ready PDF), and this
pass did not touch it. That is deliberate drift and it is **guard work**, so per the gate's own
instruction: **the claim the guard protects is P7's, and this time P6's as well.**

P7 closes a paper when two consecutive fresh-eyes passes yield zero substantive findings — evidence
only if the checks that found nothing were *capable* of finding something. -83 found a row that had
checked the wrong artefact; -84 measured the rate at 5 of 12; -85 put a floor of 25 of 129 under it;
**-86 established that 46 of those rows could not have been re-checked by anyone at all, and turned
up a false sentence in the process.** A ledger whose rows cannot be re-run cannot support P7.

**P6** ("every number regenerates from a COMMITTED script") is the direct beneficiary this time:
`f8f41df587`, `e91d103026` and `4c35bb44b7` are the three "Papers cited as established results"
regeneration claims, and all three were **actually re-run on 2026-08-18** rather than asserted — as
were `ac16838bdb`, `d6c6430592`, `f7674cbd06` and `a00820b165`.

---

## AT WRAP

`~/Scripts/charter-read.sh wealthTensor-87` immediately before the gate; gate detached **with**
`GATE_ROSTER_WHO`; pytest **and say the number**; wt148 **and** wt133 **and** wt154 **and** wt156
**and say all four RCs**; `roster leave --who` once; run `lessons.py search` before finishing and
`use` + `record-outcome` at wrap (**-86 corroborated FIVE leaves — one reached `trusted`, one moved
`quarantine → active` — and banked SEVEN new, six of them global**); ⚠ pass `--contributor`
explicitly on every `lessons.py add`; paste a handoff better than this one as the last act — and
**assign -88 ONE at-bat with a definition of done. Do not hand them a menu.** 🥎
