---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: PENDING
updated: 2026-08-19
session: wealthTensor-93
session_n: 93
live_theme: "PAPER II HAS NO KNOWN UNREPAIRED PROSE DEFECT, AND THE PASS THAT REPAIRED IT FOUND THAT AN ADJUDICATION CAN DIE TWO WAYS, NOT ONE. All four defects `-91` left standing are gone: section 7's exception clause now excepts the whole class it conceded (the Gini ceiling, section 3.4's 0.90 criterion, and the three differences of printed values), the abstract bullet was narrowed to match, a THIRD instance nobody had carded -- 'save five closed-form quantities' naming a different five two bullets away -- had its numeral dropped, and all three Paper II bare pointers now name artefacts. The class C row `c9a565b3fe` is DISCHARGED. Paper II: 17 promises, 17 adjudicated, 16 H / 1 N / 0 R / 0 C. AND THE INHERITED DONE-WHEN WAS UNSATISFIABLE BY ANY CORRECT REPAIR: it asked the residue scan to stop finding the numbers, but the defect was never in the numbers -- it was in section 7's claim about them, so the scan is INVARIANT and a new measurement was needed (`unaccounted: []`). Then `wt170 --verify`, written by `-91` to re-run fifteen known commands, caught a SIXTEENTH thing nobody had thought of: row `5a47d4caef`, whose sentence was never edited and whose `promise_id` therefore held, printed `18 quoted at lines: [38, 90, 459]` -- and the repair added four lines above 459."
phase: "TEN criteria green: pytest 1095 passed; wt133, wt148 (153 adjudicated), wt154 (0 of 153), wt156 (0 of 153), wt160, wt163, wt166, wt169 all RC 0; `wt170 --verify` RC 0 (eleven re-run, three RETIRED, one REVISED); `wt172 --verify` RC 0 over all seventeen paper-II rows. Coach at baseline: paper-I 1/0, paper-II 2/0, paper-III 5/0, paper-IV 1/0. Three commits in order, each committed before the next existed: `76355d6` the repair ALONE and deliberately RED (three rows stale, five unadjudicated, so the repaired manuscript is a git object before any evidence about it), `0089c77` the adjudication that closes it, `171a8cc` REVIEW-032. What `-92` did NOT do is start P13 -- the board points there and it is now honest to go, which it was not before."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, ONE THING: P13b -- WRITE `docs/deliverable/RECIPE.md`, AND MEASURE EVERY NUMBER IN IT FROM A REAL BUILD. `docs/CHECKLIST.md`'s first OPEN lane in dependency order is P13 and its blocking sub-row is P13b, because P13a (the stamped PDF) and P13e (the reproducible layout manifest) cannot be built from a recipe that does not exist. P13c and P13d are already CLOSED and they are your foundation, not your problem: `docs/deliverable/preflight.sh` refuses to build on a missing or substituted font (red-proofed three ways by `tests/test_preflight_refuses.py`), and 15 Libertinus + Inconsolata OTFs are vendored with a sha256 each. ADR-002 has ALREADY DECIDED the typeface, the engine and the font-loading discipline and they are NOT yours to re-open -- RECIPE.md implements them and supplies the metrics ADR-002 deliberately left unset. THE ONE THING THAT MAKES THIS HARD, STATED SO YOU DO NOT WALK INTO IT: P13b requires the metrics to be MEASURED FROM THE BUILD RATHER THAN GUESSED, and there is no build yet. So the shape is: build a probe document with the vendored fonts, MEASURE size, leading, measure, margins and display-maths spacing off it (record the command that measured each one, in the file, beside the value), then write the recipe from the measurements. A recipe whose numbers came from taste is the row failing quietly. DONE WHEN: `docs/deliverable/RECIPE.md` exists and is committed; every font family, weight, size and leading, every margin, measure and vertical space, the TeX engine and every package with its version, the figure-placement rules and the reference style appear as VALUES -- and a grep of the file for 'match the existing', 'as before', 'similar to', 'appropriate' and 'as needed' returns nothing; every metric carries the command that measured it; `preflight.sh` still passes and `tests/test_preflight_refuses.py` still refuses three ways; the suite is green AND YOU SAY THE NUMBER; wt133/wt148/wt154/wt156/wt160/wt163/wt166/wt169 all RC 0 AND YOU SAY ALL EIGHT; `wt170 --verify` and `wt172 --verify` both RC 0; coach at baseline or lower; and `docs/CHECKLIST.md`'s P13b row is flipped with the evidence recorded the way its neighbours record theirs. DO NOT ALSO BUILD THE PDF -- P13a and P13e are `-94`'s and they are a different risk profile."
blockers: []
drift_flags:
  - "A DONE-WHEN WRITTEN FROM THE FINDING CAN BE UNSATISFIABLE BY ANY CORRECT REPAIR, AND `-92` INHERITED ONE. The card and the handoff both said: done when the scan's second line reads ['0.1073', '0.99875', '4.6']. That scan measures section 3's DECIMALS against two commands' stdout; the defect was in section 7's CLAIM about those decimals. Only deleting numbers from the results section would have satisfied it. When the repair narrows a claim, the finding's instrument is invariant -- write the done-when as 'the claim now covers the residue', never 'the residue goes away'. If you inherit one of the second kind, SAY SO IN THE REVIEW rather than satisfying it."
  - "AN EVIDENCE COMMAND THAT PRINTS LINE NUMBERS DIES ON ANY EDIT ABOVE THEM, AND NOTHING FLAGS IT STALE. `5a47d4caef`'s sentence was never touched, so its `promise_id` held and `wt148` was perfectly happy; its cell printed `18 quoted at lines: [38, 90, 459]` and `wt171` added four lines above 459. Only `wt170 --verify` -- a re-run -- caught it. 26 of the TSV's 153 rows use `grep -n`, `sed -n` or an explicit L-number. THE NEXT REPAIR PASS ON PAPER III OR IV WILL HIT THIS AT SCALE. Carded 1217633269591608."
  - "THE TSV NOW HAS TWO LEDGER KINDS AND BOTH ARE LOAD-BEARING. `#superseded<TAB>old<TAB>new<TAB>tag<TAB>reason` lets a repaired sentence's row be deleted; `wt170 --verify` forgives the missing pid ONLY if the named successor is itself adjudicated (`wt172` F9 fabricates one pointing at nothing and proves the refusal survives). `#reevidenced<TAB>pid<TAB>tag<TAB>reason` covers a row whose pid held and whose evidence broke; it is honoured ONLY when the committed cell genuinely DIFFERS from `wt170`'s frozen one, so it cannot pardon a row whose unchanged command has started failing (`wt172` F15). Both are `#` comments and every sweep skips them. USE THEM; do not delete a row silently."
  - "`wt160`, `wt163` AND `wt166` READ PAPERS III AND IV ONLY -- HALF THE CORPUS. The G4 bit-identity check the brief demanded was satisfied VACUOUSLY: neither sweep has ever read Paper II. This is why REVIEW-030 section 5.1's seven bare pointers were found by hand-labelling and not by the sweep named for them. `wt171` E5/E6 now assert the blindness alongside the identity. Widening is NOT free -- `wt163`'s D3 pins the exclusions file to exactly six rows and refuses until a successor moves it deliberately. Carded 1217633320596131."
  - "`wt169`'S REVISION PIN IS NOT A REVISION PIN, AND THIS IS NOW SETTLED RATHER THAN CARRIED. `-92` was the first pass ever to repair one of the two manuscripts it labels. `wt171` E7 captured its ENTIRE JSON payload before and after: byte-identical, RC 0, 88 keys recomputed against 88 labels, zero symmetric difference. IT COULD NOT HAVE BEEN OTHERWISE -- `wt169` reads both manuscripts through `git show 83db4d5:` and never touches the working tree. It is a good guard against the ground-truth TSV and the word lists drifting (G5 proves it non-vacuous); it is NOT a guard against manuscript repair. REVIEW-030 section 8 falsifier 4 mis-describes it, and REVIEW-032 section 5 marks that IN PLACE. Do not edit REVIEW-030. THIS FLAG REPLACES the 'inert pin' flag that ran for three handoffs."
  - "PAPER II'S ONE REMAINING N IS NOT A DEFECT IN THE PAPER. `54c1c5fb27`'s artefact `0002374` is `wt148`'s sha rule matching the numeric half of the arXiv id `cond-mat/0002374`; `git cat-file` refuses it. It errs in the EXPENSIVE direction -- an adjudicator who does not run `cat-file` writes a true-sounding note about a commit that does not exist -- and it is invisible to `wt154` and `wt156`. Carded 1217630566080626. Unchanged from `-91`."
  - "`-91`'S VERBATIM-QUOTATION STANDARD (`wt170` N28b) BINDS 17 OF 153 ROWS. Re-running every evidence cell that is a bare shell command: 55 ran, 32 satisfy it, 23 do not, and every one of the 23 predates the rule. 42 more could not be invoked by a crude harness (compound cells, backtick-wrapped, annotated) and 56 are prose instructions. THAT IS NOT A CLAIM THAT 23 ROWS ARE WRONG -- it is a measurement of how far a rule written at `-91` has spread through a file built before it. REVIEW-032 section 6. Carded 1217633269591608."
  - "`wt170`'S WRITING PATH IS STILL ONE-SHOT AND EXITS 2 ON A SECOND RUN; SO IS `wt172`'S. `--verify` is the re-runnable mode in both. `wt172 --verify` is the one a successor wants: it reads EVERY paper-II row out of the committed TSV rather than a fixed list in its own source, so the next repair that adds a Paper II row is covered by it the day it lands."
  - "THE UNSUPPORTED FOUR STILL STANDS IN PRE-002 section 2, RESULT-001 section 1 AND RESULT-002 section 1, carded 1217603625863293. DO NOT EDIT THEM -- in-place edits to a registration or a result document are Jason's standing ruling. Unchanged from `-89`."
  - "T5 IS DEAD AS A PRE-FILTER AND THE 1.0000 MUST NEVER BE REQUOTED. Recall 1.0000 on the corpus its noun list was written against, 0.1429 on text it was not, at a precision BELOW the base rate. Do not resurrect it by lengthening DOC_NOUNS -- `wt169`'s G8 will fail the run. Unchanged from `-90`."
  - "DO NOT 'CORRECT' REVIEW-029 section 6.1 OR REVIEW-028 section 4's FOURTEEN. Both are git objects and both are load-bearing precisely because they were partly wrong. REVIEW-030 section 6 marks them in place. Unchanged from `-90`."
  - "REVIEW-030 section 4.1's GENERALISATION RESTS ON TWO CORPORA. 'Closed-class features transfer, open-class features do not' is disclosed as a falsifier, not sold. Do not quote it as established. Unchanged from `-90`."
  - "REVIEW-028'S PUBLISHED TEN CONTAINS FOUR ROWS `-89` MARKS SOFT and a strict reading gives 11. Disclosed at REVIEW-029 falsifier 2. Changes no verdict. Unchanged from `-89`."
  - "`docs/pointer-exclusions.tsv` is still pinned to SIX rows by `wt163`'s D3. Do not silently append. Unchanged from `-88`."
  - "N1-N6 STILL HAVE FOUR KNOWN GAP CLASSES, all carded 1217629264134185. Unchanged from `-90`."
  - "ANY OTHER TOKEN MATCHER OVER ENGLISH PROSE IN `scripts/` STILL HAS THE \\b-INSIDE-A-COMPOUND BUG UNTIL CHECKED. `wt160` and `wt163` were fixed; `wt166`, `wt169`, `wt170`, `wt171` and `wt172` were written with the guard; nothing else has been audited. Unchanged from `-88`."
  - "PAPER I IS NOT IN THE DEFINITION OF DONE and its 13 promises are deliberately unchecked. `wt170`'s N27 FAILS THE RUN if a session widens `#scope` to `paper-I`. Its FOUR bare pointers (card 1217629169253037) also stand, and that card is now PARTIALLY closed -- Paper II's three are done."
  - "`wt154`'s PREDICATE BLIND SPOT unchanged, card 1217613775009402. `wt133`'s SWEEP-2 BLIND SPOT unchanged, State Machine 1217593142996092."
parking_lot:
  - "`wt173`: generalise `wt172 --verify` to the WHOLE TSV -- a normalisation layer that can invoke a compound or annotated cell (or records it NOT-RUNNABLE with a reason IN the file rather than inferring it with a regex), then hold every runnable cell's stdout to its note line for line. Report, do not fail, on pre-standard rows; turning 23 rows red on day one just gets the guard switched off. Card 1217633269591608."
  - "Widen `wt160.PAPERS` to all four manuscripts (`wt163` and `wt166` inherit it) and adjudicate whatever the widening flags, in the same session. `wt163`'s D3 must be moved deliberately with the movement stated in a review. Card 1217633320596131."
  - "N7/N8 for the two new N1-N6 gaps. Card 1217629264134185. Needs POSITIVE and NEGATIVE post-conditions and a disclosed count movement."
  - "Read the 88 held-out rows a SECOND time, from the TSV header's rule alone with no access to `wt166`, and diff against `-90`'s labels. REVIEW-030 falsifier 1. 429 committed rows now exist for a second reader to disagree with."
  - "`wt133` sweep 3: proper nouns in the body against a stop-list, to catch a body claim with no reference entry. State Machine 1217593142996092."
  - "Patch `wt154`'s D1 to score an exit-code predicate as a read, with a POSITIVE and a NEGATIVE, and disclose how far the count moves. Card 1217613775009402."
  - "Audit every other token matcher in `scripts/` for the \\b-inside-a-hyphenated-compound bug `wt163` surfaced."
  - "roster-brake's exit #1 cannot help when the paths you touched ARE the whole dirty tree; `ROSTER_BRAKE_ACK=N` is the answer and is ranked second. State Machine 1217596263441666."
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
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-93 --task "P13b: RECIPE.md, every metric measured from a real build"'
```
**READY first try at -61 through -92 — THIRTY-TWO for thirty-two.** Budget four minutes; it takes two.
- ▲ **`roster join` IS NOT OPTIONAL BOOKKEEPING — it is what makes `lessons.py` stamp your name.**
  Join FIRST, then `lessons.py add` needs no `--contributor`. Verified again at `-92`:
  `resolve_contributor()` returned `big-wealthTensor-92` with no flag.
- ⚠ `roster join` returns RC=0 with **NO OUTPUT** on a re-join, and prints `absorbed N row(s) …`
  when it adopts a `cloud-<fp>` identity. That line is the healthy path.
- ⚠ `roster claim` syntax: `--who X --resource wealth-tensor --task "..."` — **resource is a NAMED flag.**
- ▲ **Changing your own name mid-session:** `join` new → `claim` new → `leave --who <old>`.
- ⚠ `roster-brake` **WILL** block your first `git add` commit. **`ROSTER_BRAKE_ACK=N` is the
  answer**, ranked SECOND. Card `1217596263441666`. `-88` through `-92` set it on every commit and
  lost nothing.
- ▲ **SIBLING SESSIONS SHARE DARWIN'S WORKING TREE.** At `-92`'s wrap `ipadTravel-1` held claims on
  `Scripts` (dmode only), `darwin-mac-ops` and the everything folder. Banking lessons went through
  cleanly (`lessons.py` commits its own paths). **Stage PATHS, never `-A`, in any repo you do not
  own for the session.** Run `roster who` and `rail` before you touch anything.
### THEN STAGE THE DOCS AS ONE TARBALL
```
mkdir -p /home/claude/wt          # FIRST. $HOME is /root in the container.
/tmp/dx 'mkdir -p /tmp/wt93'
/tmp/dx 'cd ~/repos/wealth-tensor && git pull --ff-only && tar czf /tmp/wt-docs.tgz docs scripts tests'
/tmp/dx --get /tmp/wt-docs.tgz /home/claude/wt/wt-docs.tgz
```
- ⚠ ▲ **THE STAGED TARBALL HAS NO `.git`.** Every post-condition that shells out to `git show`
  FAILS locally — `wt160`, `wt163`, `wt166`, `wt169` all return RC 2 in the container and RC 0 on
  darwin. That is the container, not a regression. `-92` read `[FAIL] C9 … not a git repository`
  and nearly filed it. **Read the failure text before believing the exit code.**
- ⚠ ▲ **NEVER NAME A LOCAL SCRATCH SCRIPT AFTER A STDLIB MODULE.** `-90` wrote a throwaway
  `enum.py` and every subsequent `python3` in that directory died — including `import json`.
  Same trap: `json.py`, `types.py`, `string.py`, `code.py`, `test.py`, `io.py`, `random.py`.
  **Rename the file; do not debug the import.**
- ⚠ **`/tmp/dx --put` will NOT create a missing remote directory.** `mkdir -p` on darwin FIRST.
- ⚠ Stage `tests/` **too**. `.bak` files **sort first** — read the path, not the first line.
- ⚠ **The local Bash tool's working directory PERSISTS between calls.** Lead with
  `cd /home/claude/wt &&` or use absolute paths.
- ⚠ **ANYTHING THAT IMPORTS `src/` MUST RUN ON DARWIN** — all of pytest, and `wt030_report.py`
  and `wt077_tail_index.py`, which several evidence commands shell out to. `wt133` / `wt148` /
  `handoff_gate --coach` are pure-doc and run **locally in under a second**, which is how `-92`
  dry-ran the whole promise delta before touching darwin at all.
- ▲ A script under `tests/` invoked directly needs `PYTHONPATH=src`.
- ⚠ **NEVER** pipe a command through `dx` whose exit code you intend to read — `$?` after a pipe is
  the *last* command's. Redirect inside the remote command and echo `$?` there.
- ▲ ⚠ **PROBE EVERY EVIDENCE COMMAND BEFORE YOU QUOTE IT** (`-91`'s time-saver, used again and it
  paid twice at `-92`). Write the commands into one local `evdefs.py`, `--put` it, run a five-line
  probe that prints `repr(stdout)` for each, and only then write the notes. `-92`'s probe caught a
  `pytest` line reading `'1 passed in 0.18s'` — **a duration in stdout cannot be held to a verbatim
  quotation on a later run**, which is the exact property the guard exists to enforce. One turn.
- ▲ Nested quotes → write the script **LOCALLY**, `--put` it, run `dx 'bash /tmp/x.sh'`. `-83` wrote
  seven that way, `-88` nine, `-89` eleven, `-90` eight, `-91` twelve, **`-92` nine.**
  **WRITE THE FILE.**
- ⚠ ▲ **DO NOT BUILD A PYTHON SOURCE FILE BY STRING-SURGERY ON ITS OWN TEXT WITHOUT RE-EXEC'ING IT.**
  `-92` cut a block with `s.index('X')` … `s.index('# ---', start)` and silently deleted the `EV`
  dict thirty lines below, then shipped it to darwin and burned a three-minute run on
  `NameError: name 'EV' is not defined`. **After every surgical edit, `exec()` the result and
  assert the dicts you expect are present with the sizes you expect.** Two lines.
- ⚠ ▲ **`charter-read.sh` TAKES YOUR OWN SESSION ID, NOT YOUR SUCCESSOR'S.** When YOU run it, pass
  **YOUR** id.
- ⚠ ▲ **`~` DOES NOT EXPAND INSIDE A QUOTED SHELL VARIABLE.** Use `$HOME` or an absolute path.
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to `/tmp/wt93/`, poll with a second
  `dx`. **pytest takes ~70 s and is worth backgrounding.** ⚠ Launch it AFTER your last mutation and
  read the run you started last. ▲ `tests/test_manuscript_sweeps_are_green.py` reads the TSV, so a
  TSV write invalidates a pytest run started before it.
- ▲ **A `dx` call interrupted client-side may still have RUN on darwin.** Check for the effect
  before re-running a mutating one.
---
## THE STATE YOU INHERIT AND MUST PRESERVE
🟢 `python3 -m pytest tests/ -q` → **1095 passed, 1 warning, 67.99 s.** RUN IT AND SAY THE NUMBER.
🟢 ▲ `python3 scripts/wt148_promise_sweep.py` → **RC 0**, **153 adjudicated**: paper-II **17 of 17**
   (**16 H · 1 N**), paper-III **91 of 91** (84 H · 6 N · 1 R), paper-IV **45 of 45** (43 H · 2 R).
   **13 outside scope (Paper I), unchecked on purpose. NO C ANYWHERE.**
🟢 `python3 scripts/wt133_crossref_sweep.py` → **RC 0**.
🟢 `python3 scripts/wt154_evidence_discrimination_sweep.py` → **RC 0**, **0 of 153**.
🟢 `python3 scripts/wt156_reproducibility_sweep.py` → **RC 0**, **0 of 153**.
🟢 `python3 scripts/wt160_bare_pointer_sweep.py` → **RC 0**, **13 considered, 0 flagged**, 12/12.
🟢 `python3 scripts/wt163_pointer_vocabulary.py` → **RC 0**, **21 considered, 6 flagged, all six
   disclosed-excluded, 0 undisclosed**, 13/13, 4 NEGATIVE.
🟢 `python3 scripts/wt166_pointer_groundtruth.py` → **RC 0**, **444 / 341 / 15 POINTER**, 15/15.
🟢 `python3 scripts/wt169_pointer_groundtruth_heldout.py` → **RC 0**, **125 / 88 / 7 POINTER**,
   17/17, 6 NEGATIVE. **There is no RC 1** — it reports a measurement.
🟢 ▲ `python3 scripts/wt170_paperII_promises.py --verify` → **RC 0**: eleven cells re-run and
   matched, **three RETIRED** (each with a committed successor), **one REVISED**.
🟢 ▲ `python3 scripts/wt172_tsv.py --verify` → **RC 0**, **17 paper-II rows** re-run and held to
   their notes line for line. ⚠ Both scripts' WRITING paths exit 2 by design; `--verify` is the
   re-runnable mode.
🟢 coach: paper-I **1 / 0**; paper-II **2 / 0**; paper-III **5 / 0**; paper-IV **1 / 0**.
🟢 GATE: gate v2.60, `gate-selfcheck.sh`, handoff-lint.
**Wrap order:** commit → `gate-selfcheck` → `gate_passed: true` → `--stamp` → commit → push →
`charter-read.sh <YOUR id>` → gate → `--emit`.
The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.
---
## ▶ YOUR AT-BAT · P13b — RECIPE.md, EVERY NUMBER MEASURED FROM A REAL BUILD
`next_at_bat` in the front matter is the full brief and it is binding. The short version:

**P13 is the board's first OPEN lane and P13b is what blocks the rest of it.** P13a (a PDF that
stamps the commit it was built from) and P13e (rebuild reproduces the page count and the per-page
text hash in `LAYOUT-MANIFEST.json`) cannot be built from a recipe that does not exist.

**What is already done and is NOT your problem.** P13c: `docs/deliverable/preflight.sh` refuses to
build on a missing or substituted font — red-proofed three ways by
`tests/test_preflight_refuses.py`. P13d: 15 Libertinus + Inconsolata OTFs vendored from TeX Live
2026 with SIL OFL files and a sha256 per file. **ADR-002 has already decided the typeface, the
engine and the font-loading discipline. They are not yours to re-open.**

**The trap, named so you do not walk into it.** P13b requires the metrics to be *measured from the
build rather than guessed*, and there is no build yet. So: build a probe document with the vendored
fonts, **measure** size, leading, measure, margins and display-maths spacing off it, record the
command that produced each number beside the number, and write the recipe from the measurements. A
recipe whose numbers came from taste is this row failing quietly — and it fails a session later,
when someone tries to reproduce a layout that was never derived from anything.

⚠ **Do not also build the PDF.** P13a and P13e are `-94`'s. A capture and a recipe have different
risk profiles and the recipe has to be right first.
---
## WHAT -92 DID
**Three commits, in this order, each committed before the next existed:**
| commit | what |
|---|---|
| `76355d6` | **the repair ALONE, and deliberately RED** — `wt171`, six edits, 14 post-conditions, 8 NEGATIVE. Three rows STALE and five unadjudicated at this commit, so the repaired manuscript is a git object *before* any evidence about it exists |
| `0089c77` | **the adjudication** — `wt172`, five rows minted, three retired, one re-evidenced, two new ledger kinds, 16 post-conditions, 10 NEGATIVE |
| `171a8cc` | **REVIEW-032** — the verdict, the unsatisfiable done-when, the two deaths, what the instruments cannot see, and how far the verbatim standard reaches |

**The headline, in one sentence someone can mark right or wrong.** Every number in Paper II §3 is
now regenerable from committed scripts or excepted by name in §7 — the residue scan finds seven
decimals neither named command prints, the repaired clause excepts six by name, and the seventh
(`4.6`) is §3.1's `−4.6 %` rounded from the `−4.568 %` the commands do print, so the scan's own
`unaccounted:` line reads `[]`.

**The six edits.** R1 the AI-assistance pointer (`"named in the data-availability statement"` →
`"named in §7"` — *copied*, not invented: Papers III and IV already read `§11` and `§10`, so the
same defect was shipping in one manuscript of three). R2 `"verified to machine precision in the
implementation"` → names `test_the_levy_is_a_pure_transfer` and the `transfer_error < 1e-12` bound
it actually asserts. R3 `"visible in the third column"` → `"the table's κ column"` — the SOFT
pointer the card asked for a ruling on, and **the ruling is repair it**: a positional handle breaks
the moment a column is inserted and it breaks with no diff at the site. R4 and R5 narrow the
exception clause in the abstract and in §7. R6 is bug spray — R5 introduced a *five* two bullets
from a **different** *five*, so the numeral went.

**Nothing was absorbed.** `defensive_count.py` returns 0 outside §Limitations against Paper II's
committed baseline of 0, and the coach counts are unmoved.

### The two ways an adjudication dies — the finding that outlives this at-bat
`wt170 --verify` refused if one of its fifteen rows was missing. Correct, and it made the corpus
**harder to repair than to leave alone**: repairing an adjudicated sentence deletes its row and
turns a green guard red. An incentive pointed the wrong way is a defect even when every individual
check is sound.

- **Death one — the sentence is repaired.** `promise_id` is a hash of the sentence, so it re-keys.
  Three rows died this way. `#superseded` lines now record old → new, and the forgiveness is
  granted only when the named successor is itself adjudicated. **`wt172` F9 fabricates one pointing
  at a pid that does not exist and proves the refusal survives.**
- **Death two — the sentence never moved and the evidence broke anyway.** `5a47d4caef` printed
  `18 quoted at lines: [38, 90, 459]`; the repair added four lines above 459. Its `promise_id` held
  and **nothing flagged it stale**. Replaced with a cell that names the *sections* the count appears
  in — stable under reflow — and recorded with a `#reevidenced` line honoured only when the
  committed cell genuinely differs from `wt170`'s frozen one. **`wt172` F15 proves the pardon cannot
  be forged.**

**This is `--verify` earning its keep.** `-91` added it to re-run fifteen known commands. It caught
a sixteenth thing nobody had thought of, on the first repair that ran after it, in a row `-91` had
marked H. That is a better argument for the mode than the one it shipped with.
---
## THE TELL, now ONE HUNDRED AND TWENTY-ONE deep
-61–-91 as before. **-92 adds seven.**
- **-92(i) A DONE-WHEN WRITTEN FROM THE FINDING ASKS THE FINDING'S INSTRUMENT TO STOP FINDING IT,
  AND A NARROWED CLAIM LEAVES THAT INSTRUMENT INVARIANT.** Write it as *"the claim now covers the
  residue"*, never *"the residue goes away"*. Inheriting one of the second kind is a review note,
  not a task.
- **-92(ii) AN EVIDENCE COMMAND THAT PRINTS LINE NUMBERS IS INVALIDATED BY ANY EDIT ABOVE THEM,
  INCLUDING ONE THAT CHANGES NOTHING IT ASSERTS.** Content-hash ids do not notice, so nothing
  flags it. Make positional evidence NAME what it locates — the section, the heading, the enclosing
  function — instead of WHERE it sits.
- **-92(iii) A GUARD THAT REFUSES WHEN A RECORD DISAPPEARS MAKES THE THING IT GUARDS HARDER TO
  REPAIR THAN TO LEAVE ALONE.** Do not weaken it: add a committed supersession ledger and forgive a
  missing record only when the ledger names a successor that exists — then fabricate one that
  points at nothing, in-band, and assert the guard still refuses.
- **-92(iv) BEFORE ASSERTING THAT AN INSTRUMENT'S OUTPUT IS UNCHANGED BY YOUR EDIT, ASSERT THAT
  THE INSTRUMENT READS THE FILE YOU EDITED.** Three sweeps' flag sets were bit-identical across a
  Paper II repair because none of them reads Paper II; a pinned guard was "exercised for the first
  time" and could not have moved because it reads everything through `git show` at a fixed
  revision. Both greens were true and neither was evidence. **Put the coverage fact in the SAME
  post-condition as the identity check.**
- **-92(v) A DURATION IN AN EVIDENCE COMMAND'S STDOUT CANNOT BE HELD TO A VERBATIM QUOTATION.**
  `pytest -q` prints `1 passed in 0.18s`. Strip the timing at the source, in the cell, so the row
  is re-runnable forever rather than once.
- **-92(vi) DO NOT BUILD A SOURCE FILE BY STRING-SURGERY ON ITS OWN TEXT WITHOUT RE-EXEC'ING IT.**
  A cut bounded by `s.index('# ---', start)` silently deleted a dict thirty lines below the intended
  block, and the file still *parsed*. `ast.parse` is not enough — `exec()` it and assert the objects
  you expect exist, with the sizes you expect.
- **-92(vii) WHEN A CRUDE HARNESS PRODUCES A COUNT, REPORT THE BUCKETS IT COULD NOT PROCESS BESIDE
  THE COUNT.** "23 of 55 fail" is read as a defect tally unless you also say that 42 could not be
  invoked and 56 were prose — and that "not verifiable" is not "wrong". The claim that survives a
  better harness is the direction, not the digits.
---
## TOOLING (▲ new at -92)
- ▲ `scripts/wt171_paperII_prose_repaired.py` — the six repairs, one-shot, `.bak-wt171` rollback.
  **14 post-conditions, 8 NEGATIVE.** E5/E6 prove `wt160`'s and `wt163`'s flag sets bit-identical
  **and** assert that neither reads Paper II. E7 captures `wt169`'s entire JSON payload before and
  after. E12 asserts the promise delta is EXACTLY the 3-retired / 5-minted predicted from a local
  dry run before the first byte moved. E14 refuses a ragged reflow.
- ▲ `scripts/wt172_tsv.py` — the five new adjudications, the three retirements, the one
  re-evidencing, and `--verify` over EVERY paper-II row in the committed TSV (not a fixed list in
  its own source, so the next repair is covered the day it lands). **16 post-conditions, 10
  NEGATIVE**, of which F9 and F15 are the two that prove the ledgers have teeth.
- ▲ `scripts/wt170_paperII_promises.py` — **amended**: `--verify` honours `#superseded` and
  `#reevidenced` under the conditions above. Its fifteen are unchanged and its writing path is
  untouched.
- ▲ `docs/promises-adjudicated.tsv` — **153 rows**, plus 3 `#superseded` and 1 `#reevidenced`
  ledger lines. Every sweep skips `#` lines; the ledgers are invisible to all of them.
- ▲ `docs/REVIEW-032-paper-II-prose-repair.md` — §1 the verdict in one markable sentence, §3 why
  the inherited done-when was unsatisfiable and the general form, §4 the two deaths, §5 what the
  instruments cannot see (measured), §6 how far the verbatim standard reaches, §7 six falsifiers.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
  **Tags run to `wt172`; `wt173` is free** (and is the parking-lot item the §6 measurement argues for).
---
## ESTATE
**CLOSED:** `1217630566080722` (the §7 exception clause) — completed, with the unsatisfiable
done-when written into the closing comment.
**PARTIALLY CLOSED:** `1217629169253037` — Paper II's three bare pointers repaired; **Paper I's
four stand** and Paper I is outside `#scope`.
**NEW:** `1217633320596131` (`wt160`/`wt163`/`wt166` read two manuscripts of four) and
`1217633269591608` (the verbatim standard binds 17 of 153; `wt173`).
**BUG SPRAY, outside this repo, cleared at wrap because a gate FAIL is a blocker.** (1) Three
sibling session notes were sitting untracked in the everything folder — `HANDOFF-floristDeputize-1`,
`HANDOFF-ipadTravel-2`, `SESSION-creditSentinel-1-20260818` — reported against `-92` because no
live roster claim covered the repo. Committed verbatim, unedited: the everything folder is a cache,
and a handoff left in a cache is a handoff waiting to be lost. (2) G-AE was red on
`com.braatz.vnc-autores`, a launchd job that existed nowhere but darwin. Banked to
`~/repos/darwin-remote-access/launchagents/` — its own project repo — rather than to `~/Scripts`
beside `vnc-autores.sh`, because a live `rail-runner` held the Scripts claim. Census now reads
**0 unbacked**. Neither job was reloaded and neither plist was edited.
**Carried:** `1217630566080626`, `1217629264134185`, `1217603625863293` (two instances),
`1217613775009402`, `1217568297674954`, `1217568192511533`, `1217596263441666`,
`1217596233063153`, `1217561667484767`, `1217593142996092`.
## JASON-SIZED, not -93's
(a) **The two-independent-readers design** — 429 labelled pointer rows plus 153 adjudicated promise
rows now exist, each carrying its own reason, so a second reader's disagreement is a diff rather
than an argument; (b) the version stamp — **FOURTEEN passes have declined to move it**; (c) the
four-vs-three ruling, folded into the RESULT-001 in-place-edit card; (d) DECISION-001 closed,
ROADS-001 unchanged; (e) `wt077` already prints r·E[η⁺]/(1+μ), matching to 0.44 % where Paper II
§3.1's form is off 4–7 % — changes a stated contribution, unassigned since `-81`. **`-92` edited
the paragraph next to it and did not touch this**, deliberately: it is a claim about the model, not
about the prose, and it wants its own at-bat; (f) the PAN history purge.
---
## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)
`docs/CHECKLIST.md`'s first OPEN lane in dependency order is **P13** and `-92` did not touch it —
by the ruling `-91` wrote and this pass discharged: *repair first, capture second*. P13 is a
point-in-time capture of the corpus as it would present if we stopped here, and building it from a
manuscript with a carded reproducibility defect and three bare pointers would have spent the
capture on a corpus already known to be stale, with the `LAYOUT-MANIFEST` hashes invalidated by the
very repairs already carded. **That condition is now discharged: Paper II has no known unrepaired
prose defect, and P13 is `-93`'s lane.**

**P7's counter for Paper II is at ZERO, by design and not by failure.** P7 closes a paper when two
consecutive fresh-eyes passes yield zero substantive findings. A repair pass is not a fresh-eyes
review pass, and this one found things — including one in its own instrumentation — so it starts
the count rather than advancing it.
---
## THE SELF-REVIEW TRIAD, ANSWERED IN WRITING (gate v2.60, G-A / G-B / G-G)
**1 · Did we capture everything for a zero-memory future Opus?** Yes, and the test is that every
claim here has a command beside it — plus the thing this pass adds: **the standing re-verification
is now keyed off the FILE rather than off a list in a script.** `wt172 --verify` reads every
paper-II row out of the committed TSV, so a successor does not have to trust REVIEW-032 or this
file, and the next repair that adds a Paper II row is covered by it without anyone remembering to
add it. **Undo path:** `paper-II.md.bak-wt171` and `promises-adjudicated.tsv.bak-wt172` are on
disk, and the three commits are separate and ordered so that reverting the last two leaves the
repaired manuscript standing with its adjudications red — which is the state that makes the chain
checkable rather than a state that hides anything. The one place a successor must be careful is
that both writing paths are one-shot; disclosed above rather than left as a surprising exit 2.

**2 · What did we learn the hard way that is not yet written down?** All seven are banked in
`claude-blackbook` (five global, two project-scoped) and restated as **-92(i)–(vii)** above. The
two that cost the most: **a done-when we inherited could not be satisfied by any correct repair**,
which was only visible after running the command and thinking about what it measures rather than
what it was quoted for; and **a source file rebuilt by string-surgery still parsed after silently
losing a dict**, which cost a three-minute remote run to discover. Both are mechanised now — the
first as a review section with the general form, the second as a two-line habit. And `-91`'s
retired workaround stayed retired: `resolve_contributor()` returned `big-wealthTensor-92` with no
flag, so **that item is not carried a fifth time**.

**3 · What ONE thing makes the next Opus's life easier, and did we add it THIS pass?** Added: **the
two ledger kinds.** Before today, repairing an adjudicated sentence turned a green guard red, which
is a standing reason not to repair — the exact incentive this project exists to fight. Now a
repaired row can be retired and a broken cell can be replaced, both on the record, both with a
fabrication test proving the forgiveness cannot be forged. And the honest half: **neither ledger
was in the plan.** `#superseded` was designed after the first `wt172` run failed F8, and
`#reevidenced` after `wt170 --verify` caught a row nobody expected it to touch. The pass found the
shape of the problem by running into it twice.
---
## AT WRAP
⚠ ▲ **`--emit` REFUSES while `gate_passed:` is `false`.** Walk the gate, set the field to `true`,
`--stamp`, THEN `--emit`. Correct order: **commit → gate-selfcheck → `gate_passed: true` →
`--stamp` → commit → push → `--emit`.**
`~/Scripts/charter-read.sh wealthTensor-93` — **that argument is YOUR OWN session id.** Gate
detached **with** `GATE_ROSTER_WHO`; pytest **AND SAY THE NUMBER**; wt133 AND wt148 AND wt154 AND
wt156 AND wt160 AND wt163 AND wt166 AND wt169 **AND SAY ALL EIGHT RCs**, plus `wt170 --verify` and
`wt172 --verify`; `roster leave --who` once; paste a handoff better than this one as the last act —
and assign `-94` **ONE** at-bat with a definition of done. Do not hand them a menu. 🥎
