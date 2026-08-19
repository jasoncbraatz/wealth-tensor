---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: 827d5e8530dad6271fd7b3e01b5a7ab9eaab836c
updated: 2026-08-19
session: wealthTensor-91
session_n: 91
live_theme: "PAPER II IS IN THE PROMISE INSTRUMENT, IT DID NOT COME OUT CLEAN, AND THE ONLY DEFECT IS A CLAIM ABOUT ITS OWN REPRODUCIBILITY. Nine passes parked the widening; `#scope` now names paper-II, paper-III and paper-IV and `wt148` returns RC 0 at 151 adjudicated rows. Paper II emits FIFTEEN promises, not the 28 the last handoff named -- the 28 was the sweep's grand total over everything outside scope, 15 in Paper II and 13 in Paper I, and the two were fused into one number. All fifteen are adjudicated: 13 H, 1 N, 1 C. The C is `c9a565b3fe`: section 7 says two named commands regenerate every number in section 3 'except section 3.4's Gini ceiling, which is arithmetic in N and is printed by neither', and FOUR numbers in section 3 are printed by neither in any precision -- three differences of printed values (0.035, 0.103, 0.039) and one criterion constant (0.90). The clause cannot hold both readings: it excepts the ceiling BECAUSE it is printed by neither, and (N-1)/N is one step of arithmetic from the N=800 that `wt030_report.py` prints in its own header. The N is `54c1c5fb27`, whose artefact `0002374` is not an artefact at all -- `wt148`'s sha rule matched the numeric half of the arXiv id `cond-mat/0002374`, and `git cat-file` refuses it. And the pass audited ITSELF: `wt170 --verify` was written because the writing path is one-shot, and on its first run it failed FIVE of the fifteen notes for quoting the command's first line and paraphrasing the rest. Every one of those notes was true. None was diffable."
phase: "NINE criteria green: pytest 1095 passed; wt133, wt148 (151 adjudicated), wt154 (0 of 151), wt156 (0 of 151), wt160, wt163, wt166, wt169 all RC 0; and the new wt170 --verify RC 0 over fifteen committed evidence cells. Coach at baseline: paper-I 1/0, paper-II 2/0, paper-III 5/0, paper-IV 1/0. The chain is three commits in order and each was committed before the next existed: `f5691b3` the scope line ALONE, `62217d2` the fifteen rows, `cd67e34` the --verify mode and the five notes it caught. What -91 did NOT do is touch a single character of any manuscript -- deliberately, because a manuscript edit re-keys promise_id and moves the emitted set underneath the pass measuring it. So Paper II now carries FOUR named, unrepaired prose defects: the section 7 exception clause and the three bare pointers, all in one manuscript, all carded, and -92's at-bat is to repair them together."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, ONE THING: REPAIR PAPER II'S PROSE -- THE EXCEPTION CLAUSE AND THE THREE BARE POINTERS, IN ONE PASS. Every defect now standing in Paper II is a prose defect in one manuscript, and repairing them separately means two re-adjudication cycles for one paper. Do them together, in ONE committed script, in the shape wt167/wt168 proved: the repair and the adjudication of the promises it emits budgeted into the SAME session (wealthTensor-87 lesson (iii), now confirmed four times). (1) THE EXCEPTION CLAUSE, card 1217630566080722. paper-II.md L452 and the abstract bullet at L88 both claim the two named commands regenerate every number in section 3 'except section 3.4's Gini ceiling'. Except the whole class instead of one member of it: the Gini ceiling, section 3.4's 0.90 top-decile threshold, and the three quantities quoted as differences of printed values. NARROW THE CLAIM, DO NOT ADD A HEDGE -- charter section 2 REPLACE, not ABSORB, and defensive-sentence count must be non-increasing. (2) THE THREE BARE POINTERS, card 1217629169253037. One of them, `II 11 named in the data-availability statement`, is the IDENTICAL construction wt164 already repaired in Paper III, so the same defect currently ships in one paper and not the other; take that one first and re-use wt164's repair verbatim. USE wt167's G4 PATTERN: wt160's AND wt163's flag sets must be BIT-IDENTICAL across the repair, proved in the script, not asserted in the review. AND THE THING NOBODY HAS EVER BEEN ABLE TO CHECK: wt169's revision pin has been INERT since it was written, because Papers I and II are byte-identical at 83db4d5 and at HEAD and no pass has ever repaired one of them. YOURS IS THE FIRST. When you edit paper-II.md, wt169 must still return RC 0 and its 88 keys must still recompute -- if they do not, you have found either a real drift or a bug in the guard, and BOTH are worth more than the repair (REVIEW-030 section 8 falsifier 4). DONE WHEN: `python3 scripts/wt170_paperII_promises.py --verify`'s c9a565b3fe command prints a second line reading ['0.1073', '0.99875', '4.6'] -- and note that this is a row whose deletion is REQUIRED, because a repaired sentence gets a new promise_id and the old row must be removed in the SAME commit or wt148 reports it STALE; wt148 RC 0 with the new total SAID OUT LOUD and every promise the repair emits adjudicated to the same standard, evidence quoting its command's stdout EVERY LINE, character for character (wt170's N28b is the guard and it caught five paraphrases in -91's own work); wt160 and wt163 flag sets bit-identical, proved; wt169 RC 0 with its 88 keys recomputed AND SAY WHETHER THE PIN FIRED; wt133, wt154, wt156, wt166 all RC 0; suite green AND SAY THE NUMBER; coach at baseline or LOWER (a repair that raises conduct narration has absorbed rather than replaced); docs/REVIEW-032 states in ONE sentence someone could mark right or wrong whether every number in Paper II section 3 is now regenerable from committed scripts, with the counts that settle it. DO NOT START ON P13 -- see WHICH OPEN LANE below for why the deliverable comes after this and not before."
blockers: []
drift_flags:
  - "PAPER II EMITS FIFTEEN PROMISES, NOT 28. The 28 in -90's handoff was wt148's grand total over everything outside scope: 15 in Paper II and 13 in Paper I. Nothing turned on it, and it is flagged because the shape has now appeared twice in three sessions -- a summary line's total re-quoted against a narrower subject. The defence is one command: run the instrument SCOPED to the subject before you quote its number about that subject."
  - "THE C ROW IS NOT A ROUNDING QUIBBLE AND MUST NOT BE DOWNGRADED. wt170's N25 asserts EXACTLY one C and one N among the fifteen, so a later session that quietly upgrades `c9a565b3fe` to H fails the script rather than passing it. If you believe the row is wrong, the way to say so is to run its command and show the second line reads ['0.1073', '0.99875', '4.6'] -- not to re-class it."
  - "wt170'S WRITING PATH IS ONE-SHOT AND EXITS 2 ON A SECOND RUN. That is the twin-guard, not a failure. `--verify` is the re-runnable mode and it is the one a successor wants: it reads the evidence cells OUT OF THE COMMITTED TSV, runs all fifteen, and requires every line of each note's quotation to appear in the output."
  - "FIVE OF -91'S OWN FIFTEEN NOTES QUOTED THE FIRST LINE AND PARAPHRASED THE REST, AND EVERY ONE OF THEM WAS TRUE. They were caught by the guard and rewritten, and N28b now asserts the property at write time. The lesson is not 'be careful': the author cannot catch this by re-reading, because a paraphrase of something you just ran looks correct. Mechanise it in any new adjudication script."
  - "wt169'S REVISION PIN IS STILL INERT, ONE PASS LONGER. Papers I and II remain byte-identical at 83db4d5 and at HEAD because -91 repaired nothing either. The first session to repair one of them must check wt169 still returns RC 0 and its 88 keys still recompute. REVIEW-030 falsifier 4, carried unchanged."
  - "THE `0002374` MIS-PARSE ERRS IN THE EXPENSIVE DIRECTION. A false artefact costs an adjudication, and an adjudicator who does not run `git cat-file -t` writes a true-sounding note about a commit that does not exist -- which is wealthTensor-83's failure mode with the artefact removed altogether. It is invisible to wt154 (the evidence reads the token fine) and to wt156 (a hex string is a valid handle). Carded 1217630566080626."
  - "A PROMISE REPAIRED BY EDITING ITS TARGET RATHER THAN ITS TEXT LEAVES NO TRACE IN THE TSV. Paper II's References defer bibliographic checking to docs/papers/PREPRINT-CHECKLIST.md; the sentence was FALSE when written and is TRUE now because -79 added the item to the CHECKLIST. Same promise_id, clean H, no record of a repair. wt148 sees text drift and not target drift."
  - "T5 IS DEAD AS A PRE-FILTER AND THE 1.0000 MUST NEVER BE REQUOTED. Recall 1.0000 on the corpus its noun list was written against, 0.1429 on text it was not, at a precision BELOW the base rate. Do not resurrect it by lengthening DOC_NOUNS -- wt169's G8 will fail the run. Unchanged from -90."
  - "DO NOT 'CORRECT' REVIEW-029 section 6.1 OR REVIEW-028 section 4's FOURTEEN. Both are git objects and both are load-bearing precisely because they were partly wrong. REVIEW-030 section 6 marks them in place. Unchanged from -90."
  - "REVIEW-030 section 4.1's GENERALISATION RESTS ON TWO CORPORA. 'Closed-class features transfer, open-class features do not' is disclosed as a falsifier, not sold. Do not quote it as established. Unchanged from -90."
  - "THE UNSUPPORTED FOUR STILL STANDS IN PRE-002 section 2, RESULT-001 section 1 AND RESULT-002 section 1, carded 1217603625863293. DO NOT EDIT THEM -- in-place edits to a registration or a result document are Jason's standing ruling. Unchanged from -89."
  - "REVIEW-028'S PUBLISHED TEN CONTAINS FOUR ROWS -89 MARKS SOFT and a strict reading gives 11. Disclosed at REVIEW-029 falsifier 2. Changes no verdict. Unchanged from -89."
  - "docs/pointer-exclusions.tsv is still pinned to SIX rows by wt163's D3. Do not silently append. Unchanged from -88."
  - "N1-N6 STILL HAVE FOUR KNOWN GAP CLASSES, all carded 1217629264134185. Unchanged from -90."
  - "ANY OTHER TOKEN MATCHER OVER ENGLISH PROSE IN scripts/ STILL HAS THE \\b-INSIDE-A-COMPOUND BUG UNTIL CHECKED. wt160 and wt163 were fixed; wt166, wt169 and wt170 were written with the guard; nothing else has been audited. Unchanged from -88."
  - "PAPER I IS NOT IN THE DEFINITION OF DONE and its 13 promises are deliberately unchecked. wt170's N27 FAILS THE RUN if a session widens #scope to paper-I, so widening it is now a decision somebody has to make on purpose rather than a drift."
  - "wt154's PREDICATE BLIND SPOT unchanged, card 1217613775009402. wt133's SWEEP-2 BLIND SPOT unchanged, State Machine 1217593142996092."
  - "RETIRED THIS PASS: 'lessons.py's contributor stamp does not resolve from the roster'. It DOES -- three handoffs carried a stale workaround. dx exports DARLISH_SESSION=cloud-<fp>, `roster join` absorbs that alias, and resolve_contributor() returns the real name. Proof: python3 -c \"import sys,os;sys.path.insert(0,os.path.expanduser('~/repos/claude-blackbook'));import lessons;print(lessons.resolve_contributor())\" -> big-wealthTensor-91. --contributor is no longer needed. RE-TEST AN INHERITED WORKAROUND BEFORE CARRYING IT A FOURTH TIME."
parking_lot:
  - "N7/N8 for the two new N1-N6 gaps. Card 1217629264134185. Needs POSITIVE and NEGATIVE post-conditions and a disclosed count movement."
  - "Read the 88 held-out rows a SECOND time, from the TSV header's rule alone with no access to wt166, and diff against -90's labels. REVIEW-030 falsifier 1. 429 committed rows now exist for a second reader to disagree with."
  - "wt133 sweep 3: proper nouns in the body against a stop-list, to catch a body claim with no reference entry. State Machine 1217593142996092."
  - "Patch wt154's D1 to score an exit-code predicate as a read, with a POSITIVE and a NEGATIVE, and disclose how far the count moves. Card 1217613775009402."
  - "Audit every other token matcher in scripts/ for the \\b-inside-a-hyphenated-compound bug wt163 surfaced."
  - "roster-brake's exit #1 cannot help when the paths you touched ARE the whole dirty tree; ROSTER_BRAKE_ACK=N is the answer and is ranked second. State Machine 1217596263441666."
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."
---
# wealth-tensor — HANDOFF
**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**
*Stamped by `scripts/handoff_gate.py --stamp`. If `gh_sha` above is not `HEAD`, this file was
committed without stamping — read `git log` rather than believing it.*
---
## STEP 0 · BRIDGE-BUG ACK, then transport (zero bridge calls)
The bridge rotates every ~27–33 min (`claude-code#81248`). **DARLISH DOES NOT USE IT.** Asana /
Gmail / Twilio MCP tools **are** bridge-bound: if one vanishes mid-turn it self-heals in ~1 s,
retry next turn, **NEVER declare "can't continue" over it.** Never restart the Claude app for a
darlish problem.
```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
# post the printed DARLISH-ENROLL line, EXACTLY, as an Asana comment on task 1217316841710435
/tmp/darlish-up
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-92 --task "Paper II prose repair: the exception clause and the three bare pointers"'
```
**READY first try at -61 through -91 — THIRTY-ONE for thirty-one.** Budget four minutes; it takes two.
- ▲ **`roster join` IS NOT OPTIONAL BOOKKEEPING — it is what makes `lessons.py` stamp your name.**
  `dx` exports `DARLISH_SESSION=cloud-<fp>`; `join` absorbs that alias into your session name; every
  later `lessons.py add` then resolves the contributor from the roster with no flag. Join FIRST.
- ⚠ `roster join` returns RC=0 with **NO OUTPUT** on a re-join, and prints `absorbed N row(s) …
  (carried 1 claim(s))` when it adopts a `cloud-<fp>` identity. That line is the healthy path.
- ⚠ `roster claim` syntax: `--who X --resource wealth-tensor --task "..."` — **resource is a NAMED flag.**
- ▲ **Changing your own name mid-session:** `join` new → `claim` new → `leave --who <old>`.
- ⚠ `roster-brake` **WILL** block your first `git add` commit. **`ROSTER_BRAKE_ACK=N` is the
  answer**, ranked SECOND. Card `1217596263441666`. -88 through -91 set it on every commit and
  lost nothing.
- ▲ **SIBLING SESSIONS SHARE DARWIN'S WORKING TREE.** At -91's wrap `floristDeputize-2` held live
  claims on `claude-blackbook`, `strike-zone`, `Scripts` and the everything folder. Banking lessons
  went through cleanly (`lessons.py` commits its own paths). **Stage PATHS, never `-A`, in any repo
  you do not own for the session.** Run `roster who` and `rail` before you touch anything.
### THEN STAGE THE DOCS AS ONE TARBALL
```
mkdir -p /home/claude/wt          # FIRST. $HOME is /root in the container.
/tmp/dx 'mkdir -p /tmp/wt92'
/tmp/dx 'cd ~/repos/wealth-tensor && git pull --ff-only && tar czf /tmp/wt-docs.tgz docs scripts tests'
/tmp/dx --get /tmp/wt-docs.tgz /home/claude/wt/wt-docs.tgz
```
- ⚠ ▲ **NEVER NAME A LOCAL SCRATCH SCRIPT AFTER A STDLIB MODULE.** -90 wrote a throwaway
  `enum.py` and every subsequent `python3` in that directory died — including `import json`.
  Same trap: `json.py`, `types.py`, `string.py`, `code.py`, `test.py`, `io.py`, `random.py`.
  **Rename the file; do not debug the import.**
- ⚠ **`/tmp/dx --put` will NOT create a missing remote directory.** `mkdir -p` on darwin FIRST.
- ⚠ Stage `tests/` **too**. `.bak` files **sort first** — read the path, not the first line.
- ⚠ `tar xzf` prints macOS xattr warnings with the extraction **perfectly fine**.
- ⚠ **The local Bash tool's working directory PERSISTS between calls.** Lead with
  `cd /home/claude/wt &&` or use absolute paths.
- ⚠ **ANYTHING THAT IMPORTS `src/` MUST RUN ON DARWIN** — all of pytest, and **`wt030_report.py`
  and `wt077_tail_index.py`**, which `wt170`'s evidence commands shell out to. `wt133` / `wt148` /
  `handoff_gate --coach` are pure-doc and run **locally in under a second**. `wt154` / `wt156` /
  `wt160` / `wt163` / `wt166` / `wt169` shell out to `git show`, so those need the repo.
  ▲ **`wt170` needs darwin unconditionally** — six of its fifteen evidence commands run pytest's
  collector or the two report scripts.
- ▲ A script under `tests/` invoked directly needs `PYTHONPATH=src`.
- ⚠ ABSOLUTE local paths in every `cat X | /tmp/dx --put`.
- ⚠ **NEVER** pipe a command through `dx` whose exit code you intend to read — `$?` after a pipe is
  the *last* command's. Redirect inside the remote command and echo `$?` there.
- ▲ ⚠ **-91's SHARPEST TIME-SAVER: PROBE EVERY EVIDENCE COMMAND BEFORE YOU QUOTE IT.** Write the
  commands into one local `evdefs.py`, `--put` it, run a five-line probe that prints `repr(stdout)`
  for each, and only then write the notes. Three of -91's fifteen were WRONG on that probe — two
  substring tests used a typographic apostrophe where the file has a straight one, and a
  rounding-tolerant number scan silently credited a figure to an unrelated quantity. Probing cost
  one turn. Not probing costs a review that has to be rewritten after the commit.
- ▲ Nested quotes → write the script **LOCALLY**, `--put` it, run `dx 'bash /tmp/x.sh'`. -83 wrote
  seven that way, -88 nine, -89 eleven, -90 eight, **-91 twelve**, and none lost a turn.
  **WRITE THE FILE.**
- ⚠ ▲ **`charter-read.sh` TAKES YOUR OWN SESSION ID, NOT YOUR SUCCESSOR'S.** -90 passed
  `wealthTensor-91` and `G-AL` failed at the very last step. When YOU run it, pass **YOUR** id.
- ⚠ ▲ **`~` DOES NOT EXPAND INSIDE A QUOTED SHELL VARIABLE.** Use `$HOME` or an absolute path in
  any variable holding a command. -89 lost a turn to eleven identical failures; -90 and -91 used
  `$HOME` and lost nothing.
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to `/tmp/wt92/`, poll with a second
  `dx`. **pytest takes ~70 s and is worth backgrounding.** ⚠ Launch it AFTER your last mutation and
  read the run you started last. ▲ **`tests/test_manuscript_sweeps_are_green.py` reads the TSV**,
  so a TSV write invalidates a pytest run started before it.
- ▲ **A `dx` call interrupted client-side may still have RUN on darwin.** Check for the effect
  before re-running a mutating one.
---
## THE STATE YOU INHERIT AND MUST PRESERVE
🟢 `python3 -m pytest tests/ -q` → **1095 passed, 1 warning, 69.36 s.** RUN IT AND SAY THE NUMBER.
🟢 ▲ `python3 scripts/wt148_promise_sweep.py` → **RC 0**, **151 adjudicated**: paper-II **15 of 15**
   (13 H · 1 N · 1 C), paper-III **91 of 91** (84 H · 6 N · 1 R), paper-IV **45 of 45** (43 H · 2 R).
   **13 outside scope (Paper I), unchecked on purpose.**
🟢 `python3 scripts/wt133_crossref_sweep.py` → **RC 0**.
🟢 `python3 scripts/wt154_evidence_discrimination_sweep.py` → **RC 0**, **0 of 151**.
🟢 `python3 scripts/wt156_reproducibility_sweep.py` → **RC 0**, **0 of 151**, 4 NEGATIVE.
🟢 `python3 scripts/wt160_bare_pointer_sweep.py` → **RC 0**, **0 flagged of 13**, 12/12 post-conditions.
🟢 `python3 scripts/wt163_pointer_vocabulary.py` → **RC 0**, **21 considered, 6 flagged, all six
   disclosed-excluded, 0 undisclosed**, 13/13 post-conditions, 4 NEGATIVE.
🟢 `python3 scripts/wt166_pointer_groundtruth.py` → **RC 0**, **444 / 341 / 15 POINTER**, 15/15, 5 NEGATIVE.
🟢 `python3 scripts/wt169_pointer_groundtruth_heldout.py` → **RC 0**, **125 / 88 / 7 POINTER**,
   17/17 post-conditions, 6 NEGATIVE. **There is no RC 1** — it reports a measurement.
🟢 ▲ `python3 scripts/wt170_paperII_promises.py --verify` → **RC 0**, fifteen committed evidence
   cells re-run and matched line for line. **Without `--verify` it exits 2 by design** — the
   writing path is one-shot and refuses to write twins. That refusal is the guard.
🟢 coach: paper-I **1 / 0**; paper-II **2 / 0**; paper-III **5 / 0**; paper-IV **1 / 0**.
🟢 GATE: gate v2.60, `gate-selfcheck.sh`, handoff-lint.
**Wrap order:** commit → `--stamp` → commit → push → `charter-read.sh` → gate → `--emit`.
The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.
---
## ▶ YOUR AT-BAT · REPAIR PAPER II'S PROSE — THE EXCEPTION CLAUSE AND THE THREE BARE POINTERS
`next_at_bat` in the front matter is the full brief and it is binding. The short version:
**every defect now standing in Paper II is a prose defect in one manuscript.** Repairing them in
two passes means two re-adjudication cycles for one paper. Do them together, in ONE committed
script, in the shape `wt167`/`wt168` proved: the repair AND the adjudication of the promises it
emits, budgeted into the same session.

1. **The exception clause** — card `1217630566080722`. `L452` and the abstract bullet at `L88`
   claim the two named commands regenerate every number in §3 *"except §3.4's Gini ceiling"*.
   Except the whole class: the ceiling, §3.4's `0.90` top-decile threshold, and the three
   quantities quoted as differences of printed values. **Narrow the claim; do not add a hedge.**
2. **The three bare pointers** — card `1217629169253037`. Take `II 11 named in the
   data-availability statement` FIRST: it is the identical construction `wt164` already repaired
   in Paper III, so the same defect ships in one paper and not the other, and the repair is
   already written.
3. **And the thing nobody has ever been able to check.** `wt169`'s revision pin has been INERT
   since it was written — Papers I and II are byte-identical at `83db4d5` and at HEAD because no
   pass has ever repaired one. **Yours is the first.** `wt169` must still return RC 0 and its 88
   keys must still recompute. If they do not you have found either a real drift or a bug in the
   guard, and **both are worth more than the repair.**

⚠ **A repaired sentence gets a new `promise_id`, so the old row must be DELETED in the same
commit** or `wt148` reports it STALE. That is not a wart — it is how the file refuses to let a
check survive the sentence it checked.
---
## WHAT -91 DID
**Three commits, in this order, each committed before the next existed:**
| commit | what |
|---|---|
| `f5691b3` | **the `#scope` line ALONE** — one line, nothing else, so the emitted set became a git object before any adjudication existed |
| `62217d2` | **the fifteen rows** — `wt170`, 28 post-conditions, 8 NEGATIVE |
| `cd67e34` | **`--verify`, and the five paraphrased notes it caught in this same pass** — 29 post-conditions, 9 NEGATIVE |

**The headline, in one sentence someone can mark right or wrong.** Paper II's promises are
checkable: all fifteen `wt148` emits carry an adjudication whose evidence command was RUN and
whose note quotes that command's stdout **character for character** — 13 H, 1 N, 1 C — so the
paper enters the instrument with exactly one substantive defect, and that defect is named,
falsifiable and deliberately unrepaired.

**The C, as arithmetic rather than as a story.** Scan every decimal in §3 (section references and
heading lines excluded) against both commands' stdout: 49 decimals, seven unmatched. Three of the
seven are fine — `0.1073` and `4.6` are printed quantities at the paper's own precision
(`0.107269`, `−4.568 %`), and `0.99875` is the exception the sentence names. **Four are not**:

| number | line | what it is |
|---|---|---|
| 0.035 | L294 | the periodicity span, 0.486 − 0.451 |
| 0.103 | L324 | the Gini gap, 0.994 − 0.891 |
| 0.039 | L327 | the top-decile margin, 0.90 − 0.861 |
| 0.90 | L321 | §3.4's top-decile threshold — a criterion constant |

The clause cannot hold both readings at once: it excepts the ceiling **because it "is printed by
neither"**, and `(N−1)/N` is one step of arithmetic from the `N=800` that `wt030_report.py`
prints in its own header. As written it is §7's own named failure mode — *"a provenance claim that
reads as checked and is not"* — applied to §7.

**The N is an instrument mis-parse, and it errs in the expensive direction.** `wt148`'s sha rule
matched `0002374` out of `arXiv cond-mat/0002374`; `git cat-file -t` refuses it. An adjudicator
who does not run `cat-file` writes a true-sounding note about a commit that does not exist — and
that is invisible to `wt154` (the evidence reads the token fine) and to `wt156` (a hex string is a
valid handle). Carded `1217630566080626` with a candidate repair and the NEGATIVE post-condition
it needs.

**The pass audited itself, and the audit found five.** `--verify` exists because the writing path
is one-shot: without it the fifteen commands would have been checked on the day they were written
and on no other day. On its first run it failed **five of the fifteen** notes — each quoted its
command's first line verbatim and then paraphrased the rest. **Every one of them was true.** True
is not the bar; a paraphrase cannot be diffed. All five were rewritten and `N28b` now asserts the
property at write time.
---
## THE TELL, now ONE HUNDRED AND FOURTEEN deep
-61–-90 as before. **-91 adds seven.**
- **-91(i) A GRAND TOTAL PRINTED BY AN INSTRUMENT IS NOT A PER-SUBJECT COUNT.** `wt148`'s TOTAL
  line said *28 left unchecked outside scope* over FOUR manuscripts and it was re-quoted as one
  manuscript's. Run the instrument **scoped to the subject** before you quote its number about
  that subject.
- **-91(ii) A ONE-SHOT WRITER VERIFIES ITS EVIDENCE ONCE AND THEN NEVER AGAIN.** A script that
  refuses a second invocation so it cannot write twins also refuses to re-check what it wrote.
  Give it a `--verify` that reads the evidence **out of the committed artefact** — not out of its
  own constants — and re-runs it. Thirty lines; converts a one-time check into a standing one.
- **-91(iii) A NOTE THAT QUOTES THE FIRST LINE AND PARAPHRASES THE REST READS AS CHECKED AND IS
  NOT.** Five of fifteen, all true, none diffable. **The author will not catch this by
  re-reading**, because a paraphrase of something you just ran looks correct. Assert every
  non-empty line of stdout appears verbatim in the note.
- **-91(iv) AN EXCEPTION CLAUSE CONCEDES A PRINCIPLE AND THEN GETS APPLIED TO ONE MEMBER OF THE
  CLASS.** When you read an *except* clause, take its **stated reason** and sweep the document for
  other members of that class — the reason is the author telling you what the test is.
- **-91(v) A SHA-SHAPED REGEX OVER PROSE MATCHES ARXIV IDENTIFIERS.** Resolve every sha candidate,
  or exclude a hex run preceded by a slash or an arXiv-style prefix — and give the fix a NEGATIVE
  post-condition proving a real sha still survives.
- **-91(vi) A TOLERANCE INVENTED TO BE FAIR TO ONE NUMBER SILENTLY RESCUES AN UNRELATED ONE.** A
  round-to-the-paper's-precision rule added for `0.1073` also credited `0.103` to a κ of
  `0.102609047`, hiding a real defect. **Match verbatim and classify the residue by hand in the
  write-up**, so the mechanical half stays reviewable and every judgement call is visible.
- **-91(vii) RE-TEST AN INHERITED WORKAROUND BEFORE YOU CARRY IT A FOURTH TIME.** Three handoffs
  carried *"lessons.py's contributor stamp does not resolve from the roster; pass `--contributor`"*.
  It does resolve — the precondition is `roster join`, which absorbs `dx`'s `cloud-<fp>` alias.
  Re-testing cost one command.
---
## TOOLING (▲ new at -91)
- ▲ `scripts/wt170_paperII_promises.py` — writes Paper II's fifteen adjudications (one-shot,
  refuses twins) and re-verifies them (`--verify`, re-runnable forever). **29 post-conditions,
  9 NEGATIVE.** `G1..G15` hold every evidence command's stdout to its note's quotation; `N25`
  asserts the pass did NOT come out clean (exactly one C, one N); `N27` FAILS THE RUN if `#scope`
  is widened to `paper-I`; `N28b` asserts every line of every note is verbatim. Guards before the
  first byte is written: `wt148`'s unadjudicated set must equal the fifteen exactly, and
  `paper-II.md` must be byte-identical to `f5691b3`.
- ▲ `docs/REVIEW-031-paper-II-promises.md` — §1 the verdict in one markable sentence with the
  counts, §2 the 28-versus-15 subtraction, §3 the C in full, §4 the N, §5 what a failing row
  looks like (and the five the guard caught), §6 four things -91 did not anticipate, §7 five
  falsifiers, §8 what closes and what does not.
- ▲ `docs/promises-adjudicated.tsv` — **151 rows**, `#scope` = paper-II · paper-III · paper-IV.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
  **Tags run to `wt170`; `wt171` is free.**
---
## ESTATE
Two new cards, both with a named falsifier and a DONE-WHEN: **`1217630566080722`** (the §7
exception clause) and **`1217630566080626`** (`wt148`'s sha pattern vs arXiv ids).
Carried: `1217629169253037`, `1217629264134185`, `1217603625863293` (two instances),
`1217613775009402`, `1217568297674954`, `1217568192511533`, `1217596263441666`,
`1217596233063153`, `1217561667484767`, `1217593142996092`.
## JASON-SIZED, not -92's
(a) **The two-independent-readers design** — 429 labelled pointer rows plus 151 adjudicated
promise rows now exist, each carrying its own reason, so a second reader's disagreement is a diff
rather than an argument; (b) the version stamp — **THIRTEEN passes have declined to move it**;
(c) the four-vs-three ruling, folded into the RESULT-001 in-place-edit card; (d) DECISION-001
closed, ROADS-001 unchanged; (e) `wt077` already prints r·E[η⁺]/(1+μ), matching to 0.44 % where
Paper II §3.1's form is off 4–7 % — changes a stated contribution, unassigned since -81 and now
**directly adjacent to -92's at-bat**, because -92 will be editing that very paragraph's
reproducibility clause; (f) the PAN history purge.
---
## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)
`docs/CHECKLIST.md`'s first OPEN lane in dependency order is **P13** (the arXiv-ready PDF) and
this pass did not touch it. It was not guard work either: widening `#scope` to a **shipping**
paper and adjudicating its promises is `P7` apparatus pointed at Paper II for the first time, and
it is the definition of done's *"every number regenerated from committed scripts"* clause taken
literally — which is exactly why it found something.

**And the reason -92 should not start on P13 either, stated so it can be argued with.** P13 is a
*point-in-time capture of the corpus as it would present if we stopped here*. Building that
capture from a manuscript with a carded reproducibility defect and three bare pointers spends the
capture on a corpus we already know is stale, and the LAYOUT-MANIFEST hashes P13e requires would
then be invalidated by the very repairs already carded. **Repair first, capture second.** After
-92, Paper II has no known unrepaired prose defect and P13 is the honest next lane.

**P7's counter for Paper II is at ZERO**, and that is this pass's real contribution to it: P7
closes a paper when two consecutive fresh-eyes passes yield zero substantive findings, and a pass
that *could not* have found something is not evidence. -91's found one, mechanically, with the
command that finds it committed.
---
## THE SELF-REVIEW TRIAD, ANSWERED IN WRITING (gate v2.60, G-A / G-B / G-G)
**1 · Did we capture everything for a zero-memory future Opus?** Yes, and the test is that every
claim here has a command beside it — plus the thing this pass adds: **fifteen of those commands
are now re-runnable against the committed record by a single flag.** `wt170 --verify` takes the
evidence cells out of the TSV, runs them, and requires every line of each note's quotation in the
output, so a successor does not have to trust REVIEW-031 or this file. **Undo path:** no
manuscript was touched, so there is nothing to undo in the corpus; the three commits are separate
and reverting the last leaves the scope line and the rows standing, which is the order that makes
the chain checkable. The one place a successor must be careful is that the writing path is
one-shot — disclosed above rather than left as a surprising exit 2.

**2 · What did we learn the hard way that is not yet written down?** All eight are banked in
`claude-blackbook` (seven global, two project-scoped) and restated as **-91(i)–(vii)** above. The
two that cost the most: **five of our own notes paraphrased their evidence and were caught only by
a guard written after the fact**, and **a rounding tolerance invented to be fair to one number
silently rescued an unrelated one**, which would have turned the C into an H. Both are mechanised
now, not merely written down. And one inherited item was **verified and RETIRED** rather than
carried a fourth time.

**3 · What ONE thing makes the next Opus's life easier, and did we add it THIS pass?** Added:
**`--verify`.** Before today, every adjudication in this repository was checked once, by its
author, on the day it was written; `wt148` could only tell you a row EXISTS. Now fifteen of the
151 can be re-run against their own record by one command, and the pattern generalises to the
other 136. And the honest half: **`--verify` was not in the original design.** It was added after
the fifteen rows were already committed, because re-running the script exposed that its own guard
made it un-re-runnable — the pass found this defect in itself only by trying to use it.
---
## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-92` immediately before the gate — **that argument is
YOUR OWN session id, not your successor's.** Gate detached **with** `GATE_ROSTER_WHO`; pytest
**AND SAY THE NUMBER**; wt133 AND wt148 AND wt154 AND wt156 AND wt160 AND wt163 AND wt166 AND
wt169 **AND SAY ALL EIGHT RCs**, plus `wt170 --verify`; `roster leave --who` once; paste a
handoff better than this one as the last act — and assign -93 **ONE** at-bat with a definition of
done. Do not hand them a menu. 🥎
