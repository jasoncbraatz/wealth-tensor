---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: ff64711c121254dc748964f933b4799d3adb4648
updated: 2026-08-19
session: wealthTensor-95
session_n: 95
live_theme: "P13 IS CLOSED AND THE DELIVERABLE EXISTS: `docs/deliverable/wealth-tensor-capture.pdf`, 145 pages, built by `docs/deliverable/build.sh` from commit 5b525f1754de and CARRYING THAT COMMIT IN THE FOOTER OF EVERY PAGE, so no sheet of a printed copy is ambiguous about which capture it came from. It reproduces: `verify-layout.sh` materialises a clean `git worktree` at the manifest's source_commit, rebuilds, and holds the fresh PDF to the committed page count AND all 145 per-page text hashes -- and `redproof-layout.sh` breaks it four ways to prove the verifier bites. ZERO overfull boxes and ZERO missing characters on the real build, both asserted rather than observed. wt175 closed the parking-lot item: the md->tex converter is PINNED (pandoc 3.9.0.2 + wt175_md2tex.lua) the way step 2 pins the engine. THE BUILD NOW REFUSES ON THREE THINGS THE TOOLCHAIN REPORTS BELOW THE SEVERITY THAT STOPS IT -- overfull boxes, missing glyphs, and INK OFF THE PAPER, which the overfull count structurally cannot see because widening \\hsize suppresses the warning without moving the ink back onto the sheet."
phase: "EVERYTHING GREEN AND THE NUMBERS SAID OUT LOUD: pytest 1101 passed; wt173 --verify RC 0 (50 values held, 15 of 15 in the prose); wt173 --postconditions 14 checks, 5 NEGATIVE, 0 failed; preflight RC 0 over SIXTEEN vendored fonts; wt133, wt148, wt154, wt156, wt160, wt163, wt166, wt169 -- ALL EIGHT RC 0; wt170 --verify RC 0; wt172 --verify RC 0 (REPAIRED THIS PASS -- it was already RED at cbffb8d, the commit -93 handed over green); verify-layout.sh RC 0, 145 pages and 145 per-page hashes reproduce from a clean worktree; redproof-layout.sh RC 0, four probes. Coach 0/0/3/0 outside Limitations, IDENTICAL to what -94 inherited -- NO MANUSCRIPT WAS EDITED. Five commits: 5b525f1 the machinery and the pinned converter, a90f729 the 145-page capture, b8f1957 the four-way red-proof, 3659baf the wt172 repair, plus the board regen. P13, P13a and P13e all flipped to CLOSED on the board; the first OPEN lane is now P13f."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, ONE THING: P13f -- FIGURES.tsv MUST EXIST AND MUST BITE, and the corpus has ZERO figures today, which is the entire difficulty. An empty file closes the row VACUOUSLY and reopens it silently the day somebody adds a chart. Full instructions and a red-proof recipe are already written in State Machine card 1217638815220880 -- READ IT FIRST, it is more specific than this line. MEASURED at -93 and unchanged at -94: `grep -cE '^!\\[|includegraphics|^Figure [0-9]' returns 0,0,0,0` over the four manuscripts, so there is nothing to enumerate and everything to guard. The P13f criterion as written is `awk -F'\\t' 'NR>1 && $1!~/^#/{if(system(\"test -f \" $2)) exit 1; n++} END{exit !(n>=1)}'` -- note it REQUIRES at least one row (n>=1), so a header-only file FAILS it; whatever row you write must name a real committed script and a real committed source. THE TRAP, NAMED: the criterion checks that column 2 is a file that EXISTS, and nothing checks that the figure it names is the figure the manuscript uses -- so the row that closes this can be true and inert at the same time. DONE WHEN: FIGURES.tsv exists with at least one genuine figure -> script -> source row; the criterion passes; AND the row is RED-PROOFED at least two ways -- adding an unlisted image to a manuscript must FAIL something, and pointing a row at a script that does not exist must FAIL. Do not close P13g: it is PENDING-HUMAN and explicitly not a session's to call."
blockers: []
drift_flags:
  - "`wt172 --verify` WAS ALREADY RED AT `cbffb8d`, THE COMMIT `-93` HANDED OVER CLAIMING IT RC 0, and the mechanism is written in this file's own STEP 0: \"$? after a pipe is the LAST command's\". `-93`'s commit `5445f7d` added six tests (1095 -> 1101) and row `5a47d4caef`'s evidence quotes a WHOLE-REPOSITORY collected-test count verbatim, so any test added anywhere reddens a paper-II row. Repaired at `-94` (note now quotes 1101, field count asserted at 7, `.bak` taken); the DURABLE fix swaps the volatile count for an observable that supports the claim and is carded 1217643681032027. THE GENERAL FORM: a rule stated inside a document protects the READER and not the WRITER -- so the repair is a gate that RE-RUNS what a handoff claims, carded 1217643242299336. NEVER report a sweep green from a piped exit code."
  - "ZERO OVERFULL BOXES DOES NOT MEAN THE DOCUMENT FITS ON THE PAGE, and this nearly shipped. TeX reports an overfull hbox when a line exceeds `\\hsize`, so ANY construction that widens `\\hsize` -- which is exactly what step 14's per-table measure does -- silences the warning whether or not the ink is still on the sheet. An early cut of `\\begin{wttable}` reported zero overfull boxes while running every wide table off the right edge of the paper. `build.sh` now measures the marked extent of every page with ghostscript's bbox device and requires 18bp of clearance on four edges. A CHECK WHOSE THRESHOLD IS IN THE UNITS OF AN INTERNAL REGISTER IS NOT A CHECK ON THE PHYSICAL RESULT."
  - "A RED-PROOF CAUGHT BY A DIFFERENT GUARD THAN THE ONE UNDER TEST PROVES THE WRONG THING, AND FROM THE OUTSIDE IT IS INDISTINGUISHABLE FROM SUCCESS. The first font red-proof swapped in a heavier cut; the BUILD refused it on overfull boxes; the probe went green; and the per-page hash -- the thing actually under test -- was never reached. `redproof-layout.sh` now runs RP1a (a different cut of the SAME design, with FONTS.tsv rewritten so preflight is content too, leaving only the hash to notice: caught it, 141 pages against 145) AND RP1b (the coarse swap, refused by the build). WHEN A PROBE GOES GREEN, CHECK WHICH CHECK STOPPED IT."
  - "A BUILD DIRECTORY IS STATE. A refactor of `build.sh` deleted the block that ASSEMBLES `main.tex` and the build KEPT SUCCEEDING -- every check green, right page count -- because `build/` still held the previous run's copy. It surfaced the first time the document was built in a clean worktree, which is the argument in `verify-layout.sh`'s header for why P13e rebuilds in one rather than in place. `build.sh` now `rm`s `main.tex` and asserts it was regenerated. Do not conclude anything from an in-place rebuild."
  - "A GLYPH-COVERAGE PROBE MUST TEST EVERY FACE THE DOCUMENT CAN SELECT, NOT THE FACE IT STARTS IN. The first probe at `-94` tested LibertinusSerif-Regular and reported six characters missing from the corpus's 75; the true number for the body is SEVEN. The seventh, U+1D62 `\\u1d62` (40 occurrences), is present in Regular and Bold and ABSENT from Italic and BoldItalic -- and the corpus writes it as an index on an emphasised variable, which is the italic case. LaTeX sets NOTHING for an absent glyph and exits 0. RECIPE step 6a now carries the whole table, and `FreeSerif.otf` is vendored as a SIXTEENTH checksummed row in `FONTS.tsv` for the four verification marks no Libertinus face carries."
  - "`wt173 --verify` NEEDS lualatex, AND THAT IS WHY tests/test_recipe_is_held_to_the_measurement.py EXISTS. The strong guard rebuilds and re-measures; it cannot run on a machine without TeX Live, which is CI, a fresh clone, and any session that has not run preflight. The six fast tests hold RECIPE.md to the COMMITTED METRICS-MEASURED.json in 0.01s with no toolchain. The division is deliberate and is stated in the module docstring: recipe-vs-JSON drift is caught by the tests, JSON-vs-reality drift ONLY by --verify. If you change a metric, you must run BOTH."
  - "THE MARGINS IN RECIPE.md WERE ONCE AN ECHO OF geometry'S ARGUMENTS, REPORTED AS MEASUREMENTS. Caught in-session and fixed: they are now read back out of `\\oddsidemargin` and `\\topmargin` and post-condition P8 demands the asked-for and the read-back agree. THE GENERAL FORM, and it is the -92(iv) rule with the object swapped: a value you PASSED INTO a tool is not a value you MEASURED FROM it, and the tell is that it is bit-identical to your input every single run -- which reads as agreement and is actually tautology. Any future metric added to `wt173` must be read back by a different path than it was set."
  - "ADR-002 §1 NOW CARRIES AN AMENDMENT AND THE ORIGINAL SENTENCE WAS CORRECTED IN PLACE (58 -> 64 characters). The DECISION is untouched and is not yours to re-open. What was corrected is a fact in its rationale, and `wt173` now DERIVES the identifier from the four manuscripts rather than quoting it, so it cannot drift again. The general shape is written into the amendment: a rationale that asserts a THRESHOLD ('does not overflow') rather than a DIRECTION ('is narrower than the alternatives') has made a measurement it did not take."
  - "THE 62-68 CHARACTERS-PER-LINE BAND, THE 1.25 LEADING RATIO AND THE 1.18 HEADING SCALE ARE CHOICES, NOT MEASUREMENTS, and RECIPE.md §0 says so in as many words. Everything downstream of them is arithmetic on a measurement. Do NOT quietly widen the band to make a number come out -- when the first sweep found nothing inside it, the instrument's own refusal message said 'widen WIDTHS_IN rather than relaxing the band', and that is the discipline. If a successor genuinely needs to move one of the three, move it in a review with the reason, not in a constant."
  - "`docs/deliverable/RECIPE.md` MUST NOT CONTAIN 'match the existing', 'as before', 'similar to', 'appropriate' or 'as needed' -- it is in the inherited done-when AND in `test_the_recipe_states_values_not_instructions_to_imitate`. It contained the first one once, in the opening paragraph, QUOTED IN ORDER TO FORBID IT. A negative grep cannot tell USE from MENTION, which is also why the P13b criterion bans placeholder markers (TODO/TBD/FIXME/XXX) and leaves the wording prohibition to the prose."
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
  - "`wt177`: the front matter of each paper is set with markdown hard breaks by `build.sh`, so the author block no longer becomes one justified paragraph that hyphenates an e-mail address into 'jason@braatzre-search.com'. It still carries a first-line `\\parindent`, which reads slightly oddly on a three-line address block. Cosmetic, unmeasured, and the only thing about the rendered pages `-94` looked at and did not fix."
  - "`redproof-layout.sh` and `verify-layout.sh` BOTH need lualatex, pandoc AND a git worktree, so neither runs in the container or in CI -- the same division `wt173 --verify` already has, and for the same reason. There is no toolchain-free guard on the manifest at all today: nothing catches a hand-edited `LAYOUT-MANIFEST.json` without a full rebuild. A cheap test that the manifest is SELF-CONSISTENT (page_count equals len(pages), fonts listed match `FONTS.tsv`, manuscripts listed match the four on disk) would run in milliseconds and is not written."
  - "The capture INCLUDES Paper I, carrying its own SUPERSEDED banner, because P13 asks for the corpus as it would present if we stopped here and a capture that quietly dropped the paper its own internal referee rejected would not be one. If the deliverable is ever narrowed to the three papers in the definition of done, `wt173 --measure` must be re-run: `monospace.corpus_longest_identifier_chars` is measured across all four."
  - "P13f: FIGURES.tsv must exist and must BITE even though the corpus has ZERO figures today -- an empty file closes the row vacuously and reopens it silently the day someone adds a chart. Full instructions and a red-proof recipe in State Machine 1217638815220880."
  - "If the deliverable is ever widened beyond the four papers to include the REVIEW documents, re-run `wt173 --measure`: `monospace.max_inline_identifier_chars` is measured against the papers only, and REVIEW-001 carries a 73-character identifier where the papers' longest is 64."
  - "`wt174`: generalise `wt172 --verify` to the WHOLE TSV -- a normalisation layer that can invoke a compound or annotated cell (or records it NOT-RUNNABLE with a reason IN the file rather than inferring it with a regex), then hold every runnable cell's stdout to its note line for line. Report, do not fail, on pre-standard rows; turning 23 rows red on day one just gets the guard switched off. Card 1217633269591608."
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
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-94 --task "P13a+P13e: build the capture and prove it reproduces"'
```
**READY first try at -61 through -93 — THIRTY-THREE for thirty-three.** Budget four minutes; it takes two.
- ▲ **`roster join` IS NOT OPTIONAL BOOKKEEPING — it is what makes `lessons.py` stamp your name.**
  Join FIRST, then `lessons.py add` needs no `--contributor`. Verified again at `-93`: five lessons
  banked with no `--contributor` flag and all five stamped correctly.
- ⚠ `roster join` returns RC=0 with **NO OUTPUT** on a re-join, and prints `absorbed N row(s) …`
  when it adopts a `cloud-<fp>` identity. That line is the healthy path.
- ⚠ `roster claim` syntax: `--who X --resource wealth-tensor --task "..."` — **resource is a NAMED flag.**
- ▲ **Changing your own name mid-session:** `join` new → `claim` new → `leave --who <old>`.
- ⚠ `roster-brake` **WILL** block your first `git add` commit. **`ROSTER_BRAKE_ACK=N` is the
  answer**, ranked SECOND. Card `1217596263441666`. `-88` through `-92` set it on every commit and
  lost nothing.
- ▲ **SIBLING SESSIONS SHARE DARWIN'S WORKING TREE.** At `-93`'s wrap the rail was idle and no sibling held a wealth-tensor claim; at `-92`'s wrap `ipadTravel-1` held claims on
  `Scripts` (dmode only), `darwin-mac-ops` and the everything folder. Banking lessons went through
  cleanly (`lessons.py` commits its own paths). **Stage PATHS, never `-A`, in any repo you do not
  own for the session.** Run `roster who` and `rail` before you touch anything.
### THEN STAGE THE DOCS AS ONE TARBALL
```
mkdir -p /home/claude/wt          # FIRST. $HOME is /root in the container.
/tmp/dx 'mkdir -p /tmp/wt94'
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
  seven that way, `-88` nine, `-89` eleven, `-90` eight, `-91` twelve, `-92` nine, `-93` fourteen, **`-94` over forty.**
  **WRITE THE FILE.**
- ⚠ ▲ **DO NOT BUILD A PYTHON SOURCE FILE BY STRING-SURGERY ON ITS OWN TEXT WITHOUT RE-EXEC'ING IT.**
  `-92` cut a block with `s.index('X')` … `s.index('# ---', start)` and silently deleted the `EV`
  dict thirty lines below, then shipped it to darwin and burned a three-minute run on
  `NameError: name 'EV' is not defined`. **After every surgical edit, `exec()` the result and
  assert the dicts you expect are present with the sizes you expect.** Two lines.
- ⚠ ▲ **`dx` RUNS YOUR COMMAND UNDER ZSH ON DARWIN; `board.py` RUNS A `cmd:` CRITERION UNDER
  `bash -c`.** `-93` tested a new done-criteria row with `eval "$(...)"` through `dx`, got
  `unmatched "` twice, and nearly rewrote a criterion that was already correct. **Test a
  criterion the way the board runs it: `bash -c "$CMD"`.**
- ⚠ ▲ **`"\t"` IN A PYTHON STRING IS A REAL TAB, AND `docs/done-criteria.tsv` IS TAB-SEPARATED.**
  `-93` wrote a shell command containing `grep -c "\t"` into a criterion cell and silently split
  the row into five fields. It still parsed and still looked right in a terminal; the NEXT edit
  failed an assertion instead of the data failing a test. **Assert the field count of the row you
  rewrote, in the same script — and take the `.bak` first, which is what made it a two-minute
  restore.**
- ▲ **A `lualatex` probe run is ~40 s and three of them is ~2 min — background it.** `-93` ran
  `--measure` six times before it was right. `nohup ... > /tmp/wt94/out 2>&1 &` and poll.
- ⚠ ▲ **`\prevgraf` RETURNS 0 UNDER LuaTeX IN BOTH PLACES YOU WOULD TRY IT** — on the page the
  output routine resets it mid-paragraph, and inside a `\vbox` it is never set at all. It does not
  error; it returns a NUMBER, so a chars-per-line calculation divides by it happily and produces a
  confident fabricated measure. `-93` got 36 zeroes, twice. **Count lines by box geometry instead**
  (`\lineskiplimit=-\maxdimen`, open with `\strut`, height == strut + (lines−1)×baselineskip) and
  **refuse when the division is not integral** — an instrument that cannot produce an integer line
  count is not measuring lines.
- ⚠ ▲ **`charter-read.sh` TAKES YOUR OWN SESSION ID, NOT YOUR SUCCESSOR'S.** When YOU run it, pass
  **YOUR** id. ▲ **AND RE-RUN IT IF YOU AMEND `done-criteria.tsv`** — `-93` strengthened the P13b
  criterion and gate G-AL failed at wrap because the definition of done had moved after it was
  read. Re-reading is the fix and takes two seconds; the gate is right to insist.
- ⚠ ▲ **`~` DOES NOT EXPAND INSIDE A QUOTED SHELL VARIABLE.** Use `$HOME` or an absolute path.
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to `/tmp/wt94/`, poll with a second
  `dx`. **pytest takes ~70 s and is worth backgrounding.** ⚠ Launch it AFTER your last mutation and
  read the run you started last. ▲ `tests/test_manuscript_sweeps_are_green.py` reads the TSV, so a
  TSV write invalidates a pytest run started before it.
- ▲ **A `dx` call interrupted client-side may still have RUN on darwin.** Check for the effect
  before re-running a mutating one.
------
## THE STATE YOU INHERIT AND MUST PRESERVE
🟢 `python3 -m pytest tests/ -q` → **1101 passed, 1 warning.** RUN IT AND SAY THE NUMBER.
   (1095 inherited from `-92`, plus `-93`'s six in `test_recipe_is_held_to_the_measurement.py`.)
🟢 ▲ `python3 scripts/wt173_typography_probe.py --verify` → **RC 0**, **50 values held to a
   fresh build, 0 divergent, 15 of 15 load-bearing values present in the prose.**
🟢 ▲ `python3 scripts/wt173_typography_probe.py --postconditions` → **RC 0**, **14 checks,
   5 NEGATIVE, 0 failed.**
🟢 ▲ `cd docs/deliverable && ./preflight.sh` → **RC 0** · `pytest tests/test_preflight_refuses.py`
   → **5 passed** (still refuses three ways).
🟢 `python3 scripts/wt148_promise_sweep.py` → **RC 0**, **153 adjudicated**: paper-II **17 of 17**
   (**16 H · 1 N**), paper-III **91 of 91** (84 H · 6 N · 1 R), paper-IV **45 of 45** (43 H · 2 R).
   **13 outside scope (Paper I), unchecked on purpose. NO C ANYWHERE.**
🟢 `wt133` → **RC 0** · `wt154` → **RC 0, 0 of 153** · `wt156` → **RC 0, 0 of 153**
🟢 `wt160` → **RC 0, 13 considered, 0 flagged** · `wt163` → **RC 0, 21 considered, 6 flagged,
   all six disclosed-excluded, 0 undisclosed** · `wt166` → **RC 0, 444 / 341 / 15 POINTER** ·
   `wt169` → **RC 0, 125 / 88 / 7 POINTER** (**there is no RC 1** — it reports a measurement).
🟢 `wt170 --verify` → **RC 0** (11 re-run, 3 RETIRED, 1 REVISED) · `wt172 --verify` → **RC 0**,
   **17 paper-II rows.** ⚠ Both WRITING paths exit 2 by design; `--verify` is the re-runnable mode.
🟢 ▲ coach: defensive sentences **outside** §Limitations are **0 / 0 / 3 / 0** for papers I–IV,
   **identical to the commit `-93` inherited**, and `-93` edited no manuscript at all.
🟢 GATE: gate v2.60, `gate-selfcheck.sh` **PASS**, handoff-lint clean.
**Wrap order:** commit → `gate-selfcheck` → `gate_passed: true` → `--stamp` → commit → push →
`charter-read.sh <YOUR id>` → gate → `--emit`.
The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.
---
## ▶ YOUR AT-BAT · P13a + P13e — BUILD THE CAPTURE AND PROVE IT REPRODUCES
`next_at_bat` in the front matter is the full brief and it is binding. The short version:
**RECIPE.md now exists and is paint-by-numbers. Execute it.** Do not re-derive its metrics, do
not re-open ADR-002, and do not close P13g.
**Why the two rows are one at-bat.** P13a is the PDF; P13e is the proof it reproduces. Shipping
P13a alone means `-95` finds out the layout does not reproduce *after* the artefact is committed
and quoted — which is precisely the cost ADR-002 exists to stop Jason paying twice.
**You are unblocked on figures.** Measured this pass: the four manuscripts contain **zero**
figure references. P13f does not gate you and is carded (State Machine `1217638815220880`).
**The trap, named so you do not walk into it.** The manuscripts are Markdown, the recipe is
LaTeX, and **the converter is where the layout silently changes**. RECIPE.md step 13 needs inline
code spans to become `\url{...}`, not `\texttt{...}`; a converter that emits `\texttt` overflows
the 64-character identifier in every paper, and **LaTeX reports that as a warning, so the build
succeeds and the document is merely wrong**. Pin the converter and its version the way step 2
pins the engine, and assert zero overfull boxes on the real build the way `wt173` does on the probe.
---
## WHAT -93 DID
**Five commits, in this order, each committed before the next existed:**
| commit | what |
|---|---|
| `a177773` | **the instrument and the measurements ALONE, and deliberately RED** — at this commit `RECIPE.md` does not exist, so `--verify` fails and P13b is unmet. The numbers are a git object *before* the document that quotes them |
| `72f6d5c` | **RECIPE.md**, 17 steps — plus the P13b criterion strengthened and red-proofed four ways |
| `060d3b6` | **REVIEW-033 and the ADR-002 amendment** — the claim the build refuted |
| `5445f7d` | **six toolchain-free tests**, red-proofed five ways |
**The headline, in one sentence someone can mark right or wrong.** Every metric in `RECIPE.md`
is an output of a real LuaLaTeX build over the vendored fonts — 50 values re-derived on demand
by `wt173 --verify`, which also holds the 15 load-bearing ones to the numbered prose — and the
one claim the build **refuted** is ADR-002's own: that Inconsolata is narrow enough to keep the
corpus's longest test identifier inline.
### The finding that outlives this at-bat: a conflict no font size can resolve
ADR-002 §1 justifies Inconsolata partly on a corpus-specific ground — the papers set test
identifiers inline, the longest is 58 characters, and a wide monospace would overflow. Measured:
| body size | mono advance | serif average | 64 mono chars, in body-character widths |
|---|---|---|---|
| 10.0 pt | 5.179 pt | 4.053 pt | **74.1** |
| 10.5 pt | 5.438 pt | 4.256 pt | **74.1** |
| 11.0 pt | 5.697 pt | 4.458 pt | **74.1** |
| 12.0 pt | 6.215 pt | 4.864 pt | **74.1** |
The column does not move. It is a **ratio between two typefaces**, so it is scale-invariant and
**no body size fits that identifier inline inside a readable measure**. Two exits were tried:
centring it as display code (**measured: still 41.36 pt too wide — centring narrows nothing**)
and shrinking the code font (**rejected on ADR-002's own ground**: the `zi4` cut was chosen so
identifiers can be copied out and *run*). The resolution is a **break** rule, not a size — `url`
with `\UrlBreaks` set to the underscore inserts **no character**, so the copied string still
runs, and with it the probe reports **zero** overfull boxes.
**The general shape, written into the ADR amendment:** a rationale that asserts a **threshold**
("does not overflow") rather than a **direction** ("is narrower than the alternatives") has made
a measurement it did not take. Prefer the direction; leave the threshold to the row that measures it.
---
## THE TELL, now ONE HUNDRED AND TWENTY-SIX deep
-61–-92 as before. **-93 adds five.**
- **-93(i) AN INSTRUMENT THAT RETURNS A NUMBER CAN STILL BE FAILING, AND ZERO IS THE MOST
  DANGEROUS NUMBER IT RETURNS.** `\prevgraf` gave 0 thirty-six times, twice, and
  `chars / (lines - 0.5)` divided by −0.5 without complaint. **Before believing a measurement,
  assert the instrument is capable of producing it** — here, that the line count is a positive
  integer, checked by requiring the height-to-leading division to come out integral.
- **-93(ii) A VALUE YOU PASSED INTO A TOOL IS NOT A VALUE YOU MEASURED FROM IT.** Three of four
  page margins were reported as measurements when they were `geometry`'s own arguments echoed
  back. The tell is that the number is bit-identical to your input **every** run, which reads as
  agreement and is tautology. Read it back by a **different path** and assert the two agree.
- **-93(iii) WHEN A CONSTRAINT IS A RATIO BETWEEN TWO THINGS THAT SCALE TOGETHER, MEASURE IT AT
  SEVERAL SCALES AND STOP LOOKING FOR A SCALE THAT WORKS.** 74.1 at every body size, to one
  decimal, is not a coincidence to be tuned around — it is the shape of the problem telling you
  the fix belongs on a different axis.
- **-93(iv) A NEGATIVE GREP GUARD CANNOT TELL USE FROM MENTION, AND THE DOCUMENT MOST LIKELY TO
  MENTION A FORBIDDEN PHRASE IS THE ONE WRITTEN TO FORBID IT.** A check banning "match the
  existing look" flagged the very recipe whose opening paragraph forbids it. Ban **mechanical**
  classes with no legitimate use (TODO/TBD/FIXME/XXX) and leave wording prohibitions to prose.
- **-93(v) WRITE THE DONE-WHEN'S CHECK STRONG ENOUGH THAT THE WRONG ARTEFACT FAILS IT.** P13b's
  criterion was "the file exists, has a line starting `1.`, and mentions eight keywords" — an
  eight-word file passed. A row can be honestly closed against a check that could not have caught
  a dishonest closing. **When you close a row, ask what the weakest artefact that passes its
  check looks like** — and if you would not ship that artefact, strengthen the check in the same
  session.
---
## TOOLING (▲ new at -93)
- ▲ `scripts/wt173_typography_probe.py` — three real LuaLaTeX builds. `--measure` writes
  `METRICS-MEASURED.json`; `--verify` re-measures and holds RECIPE.md to it (block **and** prose);
  `--print KEY` prints one metric from a fresh build (`--from-json` reads the committed one);
  `--emit-block` writes the three-column data block; `--postconditions` runs the 14 checks.
  ⚠ **`--measure` and `--verify` take ~40 s each** (font loading + three builds). Background them.
- ▲ `docs/deliverable/RECIPE.md` — 17 numbered steps, 50 measured values, each carrying the
  command that prints it. **Do not hand-edit the data block; edit the build and re-emit.**
- ▲ `docs/deliverable/METRICS-MEASURED.json` — the measurement of record, including the full
  36-cell sweep under `provenance.sweep_rows` and 22 packages with the versions the build reported.
- ▲ `tests/test_recipe_is_held_to_the_measurement.py` — six tests, 0.01 s, **no toolchain**.
- ▲ `docs/REVIEW-033-P13b-recipe-from-a-build.md` — §3 the scale-invariant conflict, §4 the two
  instrument failures, §5 what the instruments cannot see (measured), §6 seven falsifiers.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
  **Tags run to `wt173`; `wt174` is free** (and is the first parking-lot item).
---
## ESTATE
**CLOSED:** P13b, on the board, with the criterion strengthened and red-proofed rather than
merely satisfied.
**NEW:** `1217638815220880` (P13f's FIGURES.tsv must exist and must BITE at zero figures, plus
the 73-character identifier in REVIEW-001 that only matters if the deliverable widens).
**Carried:** `1217630566080626`, `1217629264134185`, `1217603625863293` (two instances),
`1217613775009402`, `1217568297674954`, `1217568192511533`, `1217596263441666`,
`1217596233063153`, `1217561667484767`, `1217593142996092`, `1217633320596131`,
`1217633269591608`, `1217629169253037` (partially closed — Paper I's four bare pointers stand).
## JASON-SIZED, not -94's
(a) **The two-independent-readers design** — 429 labelled pointer rows plus 153 adjudicated
promise rows, each carrying its own reason; (b) the version stamp — **FIFTEEN passes have
declined to move it**; (c) the four-vs-three ruling, folded into the RESULT-001 in-place-edit
card; (d) DECISION-001 closed, ROADS-001 unchanged; (e) `wt077` already prints r·E[η⁺]/(1+μ),
matching to 0.44 % where Paper II §3.1's form is off 4–7 % — changes a stated contribution,
unassigned since `-81`, and `-93` did not touch it either: it is a claim about the model, not
about the prose or the layout, and it wants its own at-bat; (f) the PAN history purge.
---
## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)
`docs/CHECKLIST.md`'s first OPEN lane in dependency order is **P13**, and `-93` worked its
blocking sub-row **P13b** exactly as `-92` assigned. P13a and P13e could not be built from a
recipe that did not exist; the recipe now exists, is executable top to bottom, and is held to a
build. **P13a and P13e are `-94`'s and they are the whole remaining critical path**, since P13c
and P13d are closed, P13f is unblocked-and-vacuous, and P13g is pending-human.
**P7's counter for Paper II is still at ZERO and `-93` did not move it, correctly.** P7 closes a
paper when two consecutive fresh-eyes passes yield zero substantive findings. This was a
deliverable-layer pass that edited no manuscript at all, so it is neither a fresh-eyes pass nor a
regression: the counter is untouched rather than reset.
---
## THE SELF-REVIEW TRIAD, ANSWERED IN WRITING (gate v2.60, G-A / G-B / G-G)
**1 · Did we capture everything for a zero-memory future Opus?** Yes, and the test is that every
claim here has a command beside it — plus the thing this pass adds: **the recipe is held by two
guards with different failure modes and different prerequisites.** `--verify` rebuilds and
re-measures but needs lualatex; the six tests hold the recipe to the committed measurement in
0.01 s with no toolchain, so a machine that cannot build still cannot silently drift. **Undo
path:** `done-criteria.tsv.bak-wt173` and `ADR-002...md.bak-wt173` are on disk, and the five
commits are separate and ordered so reverting the last four leaves the instrument and the
measurements standing — which is the state that makes the chain checkable. The one place a
successor must be careful is that `--measure` OVERWRITES `METRICS-MEASURED.json`: re-run it only
when you mean to re-baseline, and expect `--verify` to go red until RECIPE.md is re-emitted.
**2 · What did we learn the hard way that is not yet written down?** All five are banked in
`claude-blackbook` (all global) and restated as **-93(i)–(v)** above. The two that cost the most:
**`\prevgraf` returned a plausible, entirely fabricated set of line counts** and nothing flagged
it, because zero is a number; and **the margins were an echo of the arguments I handed
`geometry`**, which I would have shipped as measurements had I not gone looking for a second
path to the same value. Both are mechanised now — the first as a refusal inside `choose()`, the
second as post-condition P8.
**3 · What ONE thing makes the next Opus's life easier, and did we add it THIS pass?** Added:
**the P13b criterion is now strong enough that the wrong artefact fails it.** Before today the
row's check passed on a file containing the word "font" and a line starting "1." — the row could
have been closed honestly against a check that could not have caught a dishonest closing. It now
requires the measured JSON, ≥17 numbered steps, ≥40 rows in the data block and no placeholder,
and it is red-proofed four ways. And the honest half: **I strengthened it only because I went
looking for the weakest file that would pass, and I only went looking because the at-bat brief
warned that a recipe written from taste "is this row failing quietly".** The warning did the
work; the check is just where I put it so the next session does not need the warning.
---
## AT WRAP
⚠ ▲ **`--emit` REFUSES while `gate_passed:` is `false`.** Walk the gate, set the field to `true`,
`--stamp`, THEN `--emit`. Correct order: **commit → gate-selfcheck → `gate_passed: true` →
`--stamp` → commit → push → `--emit`.**
⚠ ▲ **RE-RUN `charter-read.sh` IF YOU AMEND `done-criteria.tsv`.** `-93` strengthened the P13b
criterion and gate **G-AL failed at wrap** — the definition of done had moved after it was read.
Two seconds to fix; the gate is right to insist.
`~/Scripts/charter-read.sh wealthTensor-94` — **that argument is YOUR OWN session id.** Gate
detached **with** `GATE_ROSTER_WHO`; pytest **AND SAY THE NUMBER**; wt133 AND wt148 AND wt154 AND
wt156 AND wt160 AND wt163 AND wt166 AND wt169 **AND SAY ALL EIGHT RCs**, plus `wt170 --verify`,
`wt172 --verify` and `wt173 --verify`; `roster leave --who` once; paste a handoff better than this
one as the last act — and assign `-95` **ONE** at-bat with a definition of done. Do not hand them
a menu. 🥎
