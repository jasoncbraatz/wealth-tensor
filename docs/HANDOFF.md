---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: a67fa96ed5059811a1eccc63bea5ac5a633b5d48
updated: 2026-08-19
session: wealthTensor-96
session_n: 96
live_theme: "THE BOARD HAS NO OPEN LANES LEFT. 66 criteria: **57 CLOSED, 9 PENDING-HUMAN, ZERO OPEN**. P13f was the last row a Claude could close, and `-95` closed it. What remains is P2, P3, P5, P6, P7, P11, P13g, P9 and P8 -- every one of them a HUMAN gate, and P13g/P9/P8 explicitly not a session's to call. The deliverable stands: `docs/deliverable/wealth-tensor-capture.pdf`, 145 pages, built from `5b525f1754de`, that commit in the footer of every page, reproducing page-for-page and hash-for-hash from a clean worktree. P13f's shape is the one worth carrying: the corpus has ZERO figures, so `FIGURES.tsv` carries a single `@zero-figures` row that is a CLAIM rather than a figure, and `scripts/wt177_figure_guard.py` refuses to let that claim coexist with a real figure, refuses to let it be deleted while the count is still zero, and is red-proofed on all FOURTEEN failures it can report. AN EMPTY MANIFEST CLOSES A ROW VACUOUSLY AND REOPENS IT IN SILENCE; A SENTINEL UNDER GUARD DOES NOT."
phase: "EVERYTHING GREEN AND THE NUMBERS SAID OUT LOUD: pytest **1121 passed** (1115 inherited + 4 for the figure manifest + 2 for the board guard); `wt173 --verify` RC 0 (50 values held, 15 of 15 in the prose); `wt173 --postconditions` 14 checks, 5 NEGATIVE, 0 failed; preflight RC 0 over 16 vendored fonts; wt133, wt148, wt154, wt156, wt160, wt163, wt166, wt169 -- ALL EIGHT RC 0; `wt170 --verify` RC 0; `wt172 --verify` RC 0; `verify-layout.sh` RC 0, 145 pages and 145 per-page hashes reproduce from a clean worktree (run THREE times this session, see the drift flag); `redproof-layout.sh` RC 0, four probes; NEW `wt177_figure_guard.py` RC 0 and `redproof_wt177_figures.py` 21/21 probes proven. Coach 0/0/3/0 outside Limitations, IDENTICAL to what `-95` inherited -- NO MANUSCRIPT WAS EDITED, proved by an empty `git diff 46f48fc..HEAD -- docs/papers/`. Three commits: 772e476 the manifest and its guard, d4a8f6f the board plus a guard against the degraded regeneration, 6ae9599 the wt176 diagnosability repair. P13f flipped to CLOSED; there is no first OPEN lane any more."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, ONE THING: **State Machine card 1217643242299336 -- MAKE THE GATE RE-RUN WHAT A HANDOFF CLAIMS.** It is the highest-value open item in the parking lot, it is the CLASS rather than an instance, and `-95` added the constraint that decides its design. THE PROBLEM: a handoff's `phase:` block asserts a list of exit codes and counts, and nothing re-runs them. `-93` handed over `wt172 --verify` RC 0 when it was already red at `cbffb8d`, because `$?` after a pipe is the pipe's. THE CONSTRAINT `-95` ADDS, and it is not optional: `verify-layout.sh` went RED once this session with a real-looking `manuscript changed since the capture` while no manuscript had been edited, and then would not reproduce across three further runs. A gate that re-runs claims WILL therefore, on a flaky check, manufacture a false accusation against an honest predecessor -- and a gate that cries liar is a gate somebody switches off. So it needs a RE-RUN-ON-DISAGREEMENT rule before it reports a handoff as wrong: one green and one red is a FLAKY CHECK, not a caught liar. DONE WHEN: a gate leg parses the RC/count claims out of the handoff front matter and re-runs each un-piped (`cmd >out 2>&1; rc=$?`); a disagreement is re-run before it is reported; the leg RED-PROOFS three ways -- a handoff asserting a false RC must FAIL, a handoff asserting true RCs must PASS, and a check that fails once then passes must be reported FLAKY rather than as a false claim -- and you SAY all three results out loud. Do NOT close P13g, P9 or P8: all three are PENDING-HUMAN and explicitly not a session's to call."
blockers: []
drift_flags:
  - "A MANIFEST OVER AN EMPTY SET MUST CARRY AN EXPLICIT SENTINEL ROW UNDER GUARD, NOT ZERO ROWS. `docs/deliverable/FIGURES.tsv` lists figure -> script -> source, and the corpus has no figures, so `every figure is listed` is satisfied VACUOUSLY -- the row closes and reopens in silence the day someone pastes in a chart. The working shape, and it generalises to any manifest over an empty set: a named sentinel (`@zero-figures`) that names a real committed script and a real committed source so the criterion's `test -f` stays honest, plus a guard that refuses to let the sentinel coexist with a real member (SENTINEL-WITH-FIGURES) and refuses to let it be deleted while the count is still zero (SENTINEL-MISSING). The count itself is measured FIVE ways -- the narrow grep, an eight-pattern sweep that catches mid-line images the `^!\\[` anchor walks past, zero image files tracked repo-wide, zero image XObjects in the 145-page PDF, and `preamble.tex` not loading graphicx at all."
  - "A RED-PROOF'S OWN COVERAGE CHECK MUST ENUMERATE FROM A DECLARED REGISTRY IN THE CODE UNDER TEST, NEVER BY SCRAPING ITS SOURCE TEXT. `-95` wrote a coverage check that regexed `wt177_figure_guard.py` for its failure tags, found NINE of the FOURTEEN it can emit, and printed FULL COVERAGE -- a check that could not see what it claimed to count, reporting a guarantee. This is `-94`'s rule biting its own author within the hour. The repair is a `TAGS` dict in the guard that the guard holds ITSELF to (it emits UNREGISTERED-TAG on drift) and that the red-proof imports, so a check added without a probe goes red BY CONSTRUCTION. Red-proofed: delete one probe and exactly one line goes WEAK, naming the orphaned tag."
  - "A WRAPPER SCRIPT DOCUMENTS THE RIGHT INVOCATION WITHOUT PREVENTING THE WRONG ONE. `board.py` takes four flags and requires one; called directly it silently drops `--project` and `--preamble` and emits a correct-status board with the whole `checklist-preamble.md` deleted. `-53` found that in its first ten minutes and wrote `scripts/regen-board.sh`, whose header calls itself `the ONLY supported invocation`. `-95` hit the identical trap FORTY-TWO SESSIONS LATER, because a session that never opens the wrapper never reads its warning. WHEN A WRONG PATH DEGRADES AN ARTEFACT, PUT THE CHECK ON THE ARTEFACT: `tests/test_board_is_not_degraded.py` fails on the degraded board and catches every future caller regardless of what they ran. REGENERATE THE BOARD WITH `bash scripts/regen-board.sh`, never `board.py`."
  - "`verify-layout.sh` PRODUCED A REAL-LOOKING FALSE RED AND THE CAUSE IS UNKNOWN. Once, this session: `FAIL manuscript changed since the capture: paper-III.md`, with no manuscript edited (`git diff 46f48fc..HEAD -- docs/papers/` empty). It would not reproduce. Measured against it: the live sha equals the manifest sha exactly, for all four papers, in git at the capture commit AND live; `wt176 --verify` against the committed PDF is RC 0; `verify-layout.sh` alone is RC 0; `verify-layout.sh` run CONCURRENTLY with a full pytest is RC 0, and no test in `tests/` writes a manuscript; `redproof-layout.sh` is RC 0 and mutates only inside its own worktrees. The one repair that WAS available is made: `wt176` now PRINTS wanted, got, and the path it read, so the next occurrence is diagnosable in two minutes instead of unreproducible. DO NOT report P13e green from a single run; if it goes red, re-run before believing it, and read the two shas. Carded 1217643242299336."
  - "`handoff_gate.py --emit` WAS UNSATISFIABLE BY ANY CORRECT HANDOFF UNTIL -94, and would have refused at -93 too. Its placeholder check was a substring test for TODO/TBD/FIXME/XXX, and this handoff NAMES all four -- in the drift flag whose subject is that a negative grep cannot tell USE from MENTION. It fails at the LAST ACT of the wrap, where the cheap way out is to delete the sentence; deleting documentation to satisfy a checker is how a repository forgets things. The CHECKER was fixed: the marker set recited as itself, and markers inside code spans, are mentions. tests/test_handoff_gate_placeholders.py, 14 tests, and the load-bearing ones are the controls -- a bare TODO in prose is still refused, and neither exemption may launder a real leftover beside it. If you widen those exemptions, add the control first."
  - "AN EVIDENCE COMMAND MUST OBSERVE THE THING THE SENTENCE CLAIMS, AND ROW 5a47d4caef BROKE TWICE IN TWO SESSIONS PROVING IT. Its first line printed a WHOLE-REPOSITORY collected-test count, quoted verbatim in the note, while the sentence it adjudicates is about tests/test_redistribution.py -- so every test added ANYWHERE reddened a paper-II row. -93's six tests took it 1095->1101 and -93 HANDED IT OVER REPORTED GREEN; -94 found it red at cbffb8d, then broke it again the same session with fourteen tests of its own (1101->1115). Now a PREDICATE (this paper's file is in the whole-repository collection), red-proofed both ways: three tests added elsewhere leave wt172 --verify RC 0, one test added to the paper's own file makes it RC 2. If it observes something merely NEARBY, every change to the neighbourhood is a false alarm, and false alarms are how a guard gets switched off. HOW A RED SWEEP GETS REPORTED GREEN is the other half and is unfixed: '$? after a pipe is the LAST command's' -- `tool --verify | tail -5` prints the success line AND yields tail's 0. That rule was already in this file's STEP 0; it protected the reader, not the writer. Carded 1217643242299336: make the gate RE-RUN what a handoff claims. NEVER report a sweep green from a piped exit code."
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
  - "State Machine 1217643681032027 (the durable re-evidence of row 5a47d4caef) IS DONE, closed at -94 in the same session it was filed, because the fragility bit again within the hour. 1217643242299336 (a gate that re-runs the sweeps a handoff claims green) is OPEN and is the one that matters: it is the class, not the instance."
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
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-96 --task "gate re-runs what a handoff claims (card 1217643242299336)"'
```
**READY first try at -61 through -95 — THIRTY-FIVE for thirty-five.** Budget four minutes; it takes two.
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
🟢 `python3 -m pytest -q` → **1121 passed, 1 warning.** RUN IT AND SAY THE NUMBER.
   (1115 inherited from `-94`, plus `-95`'s four in `test_figures_manifest_bites.py` and two in
   `test_board_is_not_degraded.py`.)
🟢 `python3 scripts/wt173_typography_probe.py --verify` → **RC 0**, **50 values held to a fresh
   build, 0 divergent, 15 of 15 load-bearing values present in the prose.**
🟢 `python3 scripts/wt173_typography_probe.py --postconditions` → **RC 0**, **14 checks,
   5 NEGATIVE, 0 failed.**
🟢 `bash docs/deliverable/preflight.sh` → **RC 0** over **16** vendored fonts.
🟢 `wt133` · `wt148` · `wt154` · `wt156` · `wt160` · `wt163` · `wt166` · `wt169` — **ALL EIGHT RC 0.**
🟢 `wt170 --verify` → **RC 0** · `wt172 --verify` → **RC 0**, 17 paper-II rows.
   ⚠ Both WRITING paths exit 2 by design; `--verify` is the re-runnable mode.
🟢 `bash docs/deliverable/verify-layout.sh` → **RC 0**, 145 pages, 145 per-page hashes, rebuilt in
   a clean worktree from `5b525f1754de`. ⚠ **Read the fourth drift flag before you trust one run.**
🟢 `bash docs/deliverable/redproof-layout.sh` → **RC 0**, four probes.
🟢 ▲ `python3 scripts/wt177_figure_guard.py` → **RC 0** · `python3 scripts/redproof_wt177_figures.py`
   → **RC 0, 21/21 probes proven.**
🟢 coach: defensive sentences **outside** §Limitations are **0 / 0 / 3 / 0** for papers I–IV,
   **identical to the commit `-95` inherited**, and `-95` edited no manuscript at all — proved,
   not asserted, by an empty `git diff 46f48fc..HEAD -- docs/papers/`.
🟢 GATE: gate v2.60, `gate-selfcheck.sh` **PASS**, handoff-lint clean, tree clean and pushed.
**Wrap order:** commit → `gate-selfcheck` → `gate_passed: true` → `--stamp` → commit → push →
`charter-read.sh <YOUR id>` → gate → `--emit`.
The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.

---
## ▶ YOUR AT-BAT · ONE THING — MAKE THE GATE RE-RUN WHAT A HANDOFF CLAIMS
`next_at_bat` in the front matter is the full brief and it is binding. **READ State Machine card
`1217643242299336` FIRST** — it carries `-94`'s original filing, `-95`'s evidence, and the design
constraint below.

**Why this one, when the board has no OPEN lanes.** Every remaining row is a human gate. The
highest-value work left that a Claude can do is not on the board at all: it is the parking lot,
and this is its top item — *the class, not the instance.* `-93` handed over `wt172 --verify` RC 0
when it was already red at `cbffb8d`, because `$?` after a pipe is the pipe's. The rule that would
have caught it was already written in STEP 0 of the very handoff that broke it: **it protected the
reader, not the writer.** A rule stated inside a document protects that document and nothing else.

**THE CONSTRAINT `-95` ADDS, AND IT IS NOT OPTIONAL.** `verify-layout.sh` went red once this
session with a real-looking `manuscript changed since the capture: paper-III.md` while no
manuscript had been edited, and then would not reproduce across three further runs (see the fourth
drift flag for everything ruled out). So a gate that re-runs a handoff's claims will, on a flaky
check, **manufacture a false accusation against an honest predecessor** — and a gate that cries
liar is a gate somebody switches off, which is exactly how false alarms have killed guards in this
repo before. **One green and one red is a FLAKY CHECK, not a caught liar.** Build the
re-run-on-disagreement rule in from the start; do not bolt it on after the first false accusation.

**DONE WHEN** a gate leg parses the RC/count claims out of the handoff front matter's `phase:`
block and re-runs each one **un-piped** (`cmd >out 2>&1; rc=$?`); a disagreement is re-run before
it is reported; and the leg is RED-PROOFED three ways, each result said out loud — a handoff
asserting a FALSE RC must FAIL, a handoff asserting TRUE RCs must PASS, and a check that fails
once then passes must be reported **FLAKY** rather than as a false claim.

**DO NOT** close P13g, P9 or P8. All three are PENDING-HUMAN and explicitly not a session's to call.

---
## WHAT -95 DID
**Three commits, in this order:**

| commit | what |
|---|---|
| `772e476` | `FIGURES.tsv` + `wt177_figure_guard.py` + `redproof_wt177_figures.py` + `test_figures_manifest_bites.py` — P13f |
| `d4a8f6f` | the board regenerated (P13f CLOSED) + `test_board_is_not_degraded.py` |
| `6ae9599` | `wt176` prints the two shas on a mismatch — the one repair the unexplained red allowed |

**The headline, in one sentence someone can mark right or wrong.** P13f is closed against a
manifest that has nothing to enumerate, by making the emptiness itself a guarded claim rather
than an absence — and every one of the guard's fourteen failures has been provoked and observed.

**The measurement that made the design.** Zero figures, five ways: the `-93`/`-94` grep (0,0,0,0);
an eight-pattern sweep that also catches an image pasted mid-sentence, which the `^!\[` anchor
walks straight past (0); zero image files tracked anywhere in the repo; zero image XObjects in the
145-page PDF; and `preamble.tex` does not load `graphicx`, so the deliverable currently **cannot
render a figure at all.**

### The finding that outlives this at-bat
**`-94` named four traps that are one shape — *a check that cannot see a failure reports zero of
them, and zero reads exactly like absence.* `-95` then committed that exact error, within the
hour, in the code written to honour the rule.** The red-proof's coverage check enumerated the
guard's failure tags by regexing its source, found **nine of fourteen**, and printed FULL
COVERAGE. It was caught only because the count printed `14/9` and the ratio was the wrong way
round — a cosmetic tell, not a guard.

The general repair, and it is stronger than the rule it replaces: **do not let a check DISCOVER
what it is supposed to cover — make the thing under test DECLARE it.** The guard now carries a
`TAGS` registry it holds itself to, the red-proof imports that registry, and a check added without
a probe goes red by construction. *A rule you must remember protects the person who remembers it;
a registry protects everyone downstream.*

---
## THE TELL, now ONE HUNDRED AND THIRTY-ONE deep
-61–-92 as before, `-93` added five, `-94` added five. **-95 adds two.**
- **-95(i) A CHECK THAT DISCOVERS ITS OWN SCOPE WILL UNDER-DISCOVER IT SILENTLY.** Scraping,
  globbing, and pattern-matching to find "everything that needs covering" all fail the same way:
  they return a smaller set and report full coverage over it. **Make the thing under test declare
  its scope in a registry, and hold it to the registry.** Nine of fourteen, reported as complete.
- **-95(ii) A DOCUMENTED WORKAROUND IS NOT A FIX IF THE WRONG PATH IS STILL SILENT.** `-53` found
  the degraded-board trap, wrote the wrapper, and called it the only supported invocation; the
  trap caught `-95` forty-two sessions later. **If the wrong path degrades an ARTEFACT, put the
  check on the ARTEFACT** — then it does not matter what anybody ran, or whether they read the
  warning.

---
## TOOLING (▲ new at -95)
- ▲ `scripts/wt177_figure_guard.py` — the P13f guard. `--emit` writes `FIGURES-MEASURED.json`;
  `--json` prints the measurement with no verdict; `--paper/--manifest/--pdf/--no-pdf/--build-sh`
  point every input elsewhere for red-proofing. **The corpus list is PARSED from `PAPERS=` in
  `build.sh`, never hardcoded.** It prints what it is **BLIND TO** on every run, green included.
- ▲ `scripts/redproof_wt177_figures.py` — 21 probes. Each asserts the **specific** `FAIL[TAG]`,
  because a red-proof caught by a different guard proves the wrong thing; one probe must go
  **GREEN**; one checks the probed criterion is still the committed one.
- ▲ `tests/test_figures_manifest_bites.py` (4) · `tests/test_board_is_not_degraded.py` (2).
- ⚠ **`bash scripts/regen-board.sh` IS THE ONLY SUPPORTED BOARD REGENERATION.** `board.py`
  directly = a correct-status board with its preamble deleted. The test now catches it.
- ⚠ A full deliverable build is ~2 min and `redproof-layout.sh` is ~5–8. **Background them**
  (`nohup … > /tmp/x.out 2>&1 &`) and poll with a second `dx`.
- ▲ darwin is **macOS + zsh**: no `grep -P`, no `cat -A`, `cut -c` is byte-based. Nested quotes →
  write the script LOCALLY, `--put` it, `dx 'bash /tmp/x.sh'`. `-94` wrote over forty; `-95` about
  twenty, and every one of them was cheaper than fighting the quoting.
- ▲ **After string-surgery on a Python file, `ast.parse` it AND `exec_module` it** before shipping
  — `-92`'s rule, used twice this session, worth the two lines both times.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
  **Tags run to `wt177`; `wt174` is a gap and `wt178` is next.**

---
## ESTATE
**CLOSED:** **P13f**, on the board — and with it, the last OPEN lane in the project.
`1217638815220880` closed with the full recipe, the measurement, and what was carried forward.
**COMMENTED, not closed:** `1217643242299336` — `-95` added the flaky-check constraint and the
evidence; **it is `-96`'s at-bat.**
**Carried:** `1217630566080626`, `1217629264134185`, `1217603625863293` (two instances),
`1217613775009402`, `1217568297674954`, `1217568192511533`, `1217596263441666`,
`1217596233063153`, `1217561667484767`, `1217593142996092`, `1217633320596131`,
`1217633269591608`, `1217629169253037` (partially closed — Paper I's four bare pointers stand).

## JASON-SIZED, not -96's
(a) **The two-independent-readers design** — 429 labelled pointer rows plus 153 adjudicated
promise rows, each carrying its own reason; (b) the version stamp — **SIXTEEN passes have declined
to move it**; (c) the four-vs-three ruling, folded into the RESULT-001 in-place-edit card;
(d) DECISION-001 closed, ROADS-001 unchanged; (e) `wt077` already prints r·E[η⁺]/(1+μ), matching
to 0.44 % where Paper II §3.1's form is off 4–7 % — changes a stated contribution, unassigned
since `-81`, and `-95` did not touch it either: it is a claim about the MODEL, and it wants its
own at-bat; (f) the PAN history purge. **(g) NEW AND THE BIG ONE: with zero OPEN lanes left,
every remaining row is a human gate — P2, P3, P5, P6, P7, P11, P13g, P9, P8.** P9 is the single
handoff into P8 and its own criterion says declaring readiness is the session's job; `-95` did
NOT declare it, because P7's convergence counters are not met and the criterion for P9 names
convergence explicitly. **That is a judgement a successor should re-examine deliberately, not
inherit as settled.**

---
## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)
`docs/CHECKLIST.md`'s first OPEN lane in dependency order was **P13f**, and `-95` worked exactly
that and nothing else. **There is now no first OPEN lane** — the board reads 57 CLOSED, 9
PENDING-HUMAN, 0 OPEN, and the pointer line the board emits for the next lane is gone because
there is none to point at.

**P7's counters did not move and `-95` did not move them, correctly.** P7 closes a paper when two
consecutive fresh-eyes passes yield zero substantive findings. This was a deliverable-layer pass
that edited no manuscript at all, so it is neither a fresh-eyes pass nor a regression: the
counters are untouched rather than reset.

---
## THE SELF-REVIEW TRIAD, ANSWERED IN WRITING (gate v2.60, G-A / G-B / G-G)
**1 · Did we capture everything for a zero-memory future Opus?** Yes, and the test is that every
claim here has a command beside it. The one thing that would have been lost without deliberate
effort is the **negative** result: `verify-layout.sh` went red once and would not reproduce. The
tempting write-up is silence, because it is green now and green is the number that goes in the
handoff. It is in the drift flags instead, with the five things ruled out, because a P13e green
from a single run is now known to be worth less than it reads. **Undo path:** three separate
ordered commits; `docs/deliverable/wt176_layout_manifest.py.bak-wt95` on disk; every new file is
additive, so reverting `772e476` removes P13f's machinery whole and leaves the board's own
regeneration as the only thing to redo.

**2 · What did we learn the hard way that is not yet written down?** Both are banked in
`claude-blackbook` (three global, one project-scoped) and restated as **-95(i)–(ii)** above. The
one that cost the most is the one that is embarrassing: **`-94` spent a whole session naming the
shape "a check that cannot see a failure reports zero of them", I read it in the brief, wrote it
into a docstring, and then committed that exact error in the coverage check itself** — caught by a
cosmetic tell (`14/9`, the wrong way round), not by a guard. That is the strongest available
argument for the repair: the rule is now a registry, not a reminder.

**3 · What ONE thing makes the next Opus's life easier, and did we add it THIS pass?** Added:
**`tests/test_board_is_not_degraded.py`.** `-53` documented the degraded-board trap in a wrapper
forty-two sessions ago and it still caught me, because documentation protects readers and the
person about to make the mistake is by definition not reading it. The board is now checked as an
artefact, so the next session cannot commit a board with its preamble deleted no matter which
command they run. And the honest half: **I only found it because I diffed my own regeneration
before committing it** — the fix is in the suite so the next session does not need my paranoia.

---
## AT WRAP
⚠ **`--emit` REFUSES while `gate_passed:` is `false`.** Order: **commit → `gate-selfcheck` →
`gate_passed: true` → `--stamp` → commit → push → `charter-read.sh <YOUR id>` → gate → `--emit`.**
⚠ **RE-RUN `charter-read.sh` IF YOU AMEND `done-criteria.tsv`** — gate G-AL checks that the
definition of done had not moved after you read it.
`~/Scripts/charter-read.sh wealthTensor-96` — **that argument is YOUR OWN session id, not your
successor's.** Gate detached **with** `GATE_ROSTER_WHO`; pytest **AND SAY THE NUMBER**; wt133 AND
wt148 AND wt154 AND wt156 AND wt160 AND wt163 AND wt166 AND wt169 **AND SAY ALL EIGHT RCs**, plus
`wt170 --verify`, `wt172 --verify`, `wt173 --verify`, and now `wt177_figure_guard.py` AND
`redproof_wt177_figures.py`. **Capture every RC un-piped** (`cmd >out 2>&1; rc=$?`) — that is the
bug your at-bat is about, and handing it over while committing it would be quite the own goal.
`roster leave --who` once; paste a handoff better than this one as the last act — and assign `-97`
**ONE** at-bat with a definition of done. Do not hand them a menu. 🥎
