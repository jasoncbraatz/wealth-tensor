---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: c055dd39e8870bae0c38f616864314d879be577d
updated: 2026-08-19
session: wealthTensor-97
session_n: 97
live_theme: "THE HANDOFF NOW RE-RUNS ITS OWN CLAIMS. `-93` asserted `wt172 --verify` RC 0 while that command returned 2 at the exact commit it handed over, because `$?` after a pipe is the pipe's -- and the rule against piping was ALREADY in STEP 0 of the handoff it broke. A rule stated inside a document protects that document's READER, never its writer; only a check closes that. `-96` built it: the front matter carries a `claims:` registry, `handoff_gate.py --claims-all` RE-RUNS every entry un-piped, and a disagreement is re-run before it is reported, because `-95` proved a flaky check will otherwise manufacture a false accusation against an honest predecessor. It caught its own author inside the hour: `pytest` stayed RC 0 while its count went 1121 -> 1148, and the leg refused the stale number three times before calling it false. THE BOARD IS UNCHANGED -- 57 CLOSED, 9 PENDING-HUMAN, ZERO OPEN, every remaining row a human gate."
phase: "THE GATE NOW RE-RUNS WHAT THE HANDOFF CLAIMS, AND EVERY NUMBER HERE WAS RE-DERIVED BY IT RATHER THAN QUOTED: `pytest` 1148 passed (1121 inherited from `-95`, plus 27 in the new tests/test_handoff_claims_leg.py); `wt173 --verify` RC 0; `wt173 --postconditions` RC 0 over 14 checks with 5 NEGATIVE and 0 failed; `preflight` RC 0 over 16 vendored fonts; `wt133` and `wt148` and `wt154` and `wt156` and `wt160` and `wt163` and `wt166` and `wt169` -- ALL EIGHT RC 0; `wt170 --verify` RC 0; `wt172 --verify` RC 0 over 17 paper-II rows; `verify-layout.sh` RC 0, 145 pages rebuilt in a clean worktree, and it did NOT reproduce `-95`'s false red; `redproof-layout.sh` RC 0, four probes; `wt177_figure_guard.py` RC 0; `redproof_wt177_figures.py` RC 0 over 21 probes; NEW `redproof_wt178_claims.py` RC 0, 20 probes, 17 of 17 declared tags covered, and the coverage check proven non-vacuous by deleting one probe; G-CLAIMS run over the committed handoff -- 23 claims declared, 23 re-run un-piped, 23 agreed, exit code captured un-piped; `defensive paper-I` and `defensive paper-II` and `defensive paper-III` and `defensive paper-IV` -- 0/0/3/0 sentences outside Limitations, now MEASURED and registered rather than inherited, and IDENTICAL to what `-96` inherited and NO MANUSCRIPT EDITED; gate v2.61 PASS, tree clean and pushed."
gate_passed: true
gate_version: "2.61"
next_at_bat: "ASSIGNED, ONE THING: **a toolchain-free guard on `docs/deliverable/LAYOUT-MANIFEST.json`.** It is the top item in the parking lot and it is a named hole, not a nicety: `verify-layout.sh`, `redproof-layout.sh` and `wt173 --verify` ALL need lualatex, pandoc and a git worktree, so NOTHING in CI, in a fresh clone, in the container, or in any session that has not run preflight can catch a hand-edited manifest. A file nothing cheap can check is a file that drifts, and P13e's whole claim rests on it. THE SHAPE, and `-96` just built one of these so copy it: the manifest DECLARES what it contains, and the test holds it to its own declaration -- `page_count` equals `len(pages)`, the fonts listed match `FONTS.tsv` row for row, the manuscripts listed are exactly the four on disk, every per-page hash is well-formed and there are `page_count` of them, and the capture commit named in the manifest is an object in this clone. Do NOT let the test discover its own scope by iterating whatever keys happen to be present -- that is `-95`'s nine-of-fourteen defect, and it reads as full coverage. DONE WHEN: `tests/test_layout_manifest_is_self_consistent.py` runs with NO toolchain in under a second and passes on the committed manifest; a red-proof provokes EVERY failure it can report, each asserted by its specific tag rather than by exit status alone, and says the count out loud; the new guard is REGISTERED in the `claims:` block so the gate re-runs it; and `pytest`'s count claim moves with it. Do NOT close P13g, P9 or P8 -- all three PENDING-HUMAN and explicitly not a session's to call."
blockers: []
claims:
  - id: pytest
    cmd: python3 -m pytest -q
    rc: 0
    count: 1148
    count_re: ([0-9]+) passed
    note: about 70s -- the number IS the claim, not decoration
  - id: wt173 --verify
    cmd: python3 scripts/wt173_typography_probe.py --verify
    rc: 0
    slow: true
    note: rebuilds with lualatex, so it cannot run in CI or a fresh clone
  - id: wt173 --postconditions
    cmd: python3 scripts/wt173_typography_probe.py --postconditions
    rc: 0
    count: 14
    count_re: postconditions: ([0-9]+) check
  - id: preflight
    cmd: bash docs/deliverable/preflight.sh
    rc: 0
    count: 16
    count_re: ([0-9]+) font file
  - id: wt133
    cmd: python3 scripts/wt133_crossref_sweep.py
    rc: 0
  - id: wt148
    cmd: python3 scripts/wt148_promise_sweep.py
    rc: 0
  - id: wt154
    cmd: python3 scripts/wt154_evidence_discrimination_sweep.py
    rc: 0
  - id: wt156
    cmd: python3 scripts/wt156_reproducibility_sweep.py
    rc: 0
  - id: wt160
    cmd: python3 scripts/wt160_bare_pointer_sweep.py
    rc: 0
  - id: wt163
    cmd: python3 scripts/wt163_pointer_vocabulary.py
    rc: 0
  - id: wt166
    cmd: python3 scripts/wt166_pointer_groundtruth.py
    rc: 0
  - id: wt169
    cmd: python3 scripts/wt169_pointer_groundtruth_heldout.py
    rc: 0
  - id: wt170 --verify
    cmd: python3 scripts/wt170_paperII_promises.py --verify
    rc: 0
    note: the WRITING path exits 2 by design; --verify is the re-runnable mode
  - id: wt172 --verify
    cmd: python3 scripts/wt172_tsv.py --verify
    rc: 0
    count: 17
    count_re: ([0-9]+) paper-II rows
    note: the claim -93 handed over green while it was red -- the reason this leg exists
  - id: verify-layout.sh
    cmd: bash docs/deliverable/verify-layout.sh
    rc: 0
    slow: true
    note: needs lualatex, pandoc and a worktree; prints no count to hold it to
  - id: redproof-layout.sh
    cmd: bash docs/deliverable/redproof-layout.sh
    rc: 0
    slow: true
    note: 5-8 minutes, four probes, and it prints no count either
  - id: wt177_figure_guard.py
    cmd: python3 scripts/wt177_figure_guard.py
    rc: 0
  - id: redproof_wt177_figures.py
    cmd: python3 scripts/redproof_wt177_figures.py
    rc: 0
    count: 21
    count_re: ([0-9]+)/[0-9]+ probes proven
  - id: defensive paper-I
    cmd: python3 scripts/defensive_count.py docs/papers/paper-I-price-formation/paper-I.md
    rc: 0
    count: 0
    count_re: ([0-9]+) defensive sentence\(s\) outside
  - id: defensive paper-II
    cmd: python3 scripts/defensive_count.py docs/papers/paper-II-redistribution/paper-II.md
    rc: 0
    count: 0
    count_re: ([0-9]+) defensive sentence\(s\) outside
  - id: defensive paper-III
    cmd: python3 scripts/defensive_count.py docs/papers/paper-III-dual-tensor/paper-III.md
    rc: 0
    count: 3
    count_re: ([0-9]+) defensive sentence\(s\) outside
  - id: defensive paper-IV
    cmd: python3 scripts/defensive_count.py docs/papers/paper-IV-composition/paper-IV.md
    rc: 0
    count: 0
    count_re: ([0-9]+) defensive sentence\(s\) outside
    note: the 0/0/3/0 the phase block states -- inherited unverified for three handoffs until -96 measured it
  - id: redproof_wt178_claims.py
    cmd: python3 scripts/redproof_wt178_claims.py
    rc: 0
    count: 17
    count_re: ([0-9]+) of [0-9]+ declared tags proven
    note: the red-proof for this leg -- it holds ITSELF to a claim like everything else
drift_flags:
  - "THE BOARD'S CHECK TIMEOUT WAS A KNIFE EDGE AND IT DOWNGRADED A CLOSED LANE UNDER LOAD. `board.py` runs every `cmd:` criterion under `BOARD_CHECK_TIMEOUT`, default 25s. P13e's criterion IS `bash docs/deliverable/verify-layout.sh`, and that takes 16s on an idle darwin -- a 1.6x margin. `-96` regenerated the board while its own `--claims-all` was rebuilding the deliverable in another process, and P13e came back CANNOT VERIFY, `check timed out after 25s`: a CLOSED lane downgraded, in COMMITTED state, by nothing but concurrent load. The condition that trips it is the workflow THIS FILE RECOMMENDS -- background the long builds and poll. Fixed where the artefact is: `scripts/regen-board.sh` now exports `BOARD_CHECK_TIMEOUT=300` unless the caller sets one, which is the same repair `-53` made for the missing flags and for the same reason. Proven: regenerated on a quiet machine, the board comes back BYTE-IDENTICAL to the committed one. TWO RULES FOLLOW. ALWAYS `git diff docs/CHECKLIST.md` before committing a regeneration -- `-96` caught this only by diffing. And do NOT regenerate the board while a build is running; a status derived under load is a measurement of your machine, not of the project."
  - "THE HANDOFF'S CLAIMS ARE NOW A MACHINE-READABLE REGISTRY AND THE GATE RE-RUNS THEM. The frontmatter carries a `claims:` block (id / cmd / rc / count / count_re / slow / note) and `python3 scripts/handoff_gate.py --claims-all` re-runs every entry UN-PIPED before the wrap. `--claims` alone skips the ones marked slow and exits 2, because an un-run claim is not a verified one. TWO THINGS A SUCCESSOR MUST KNOW. (a) `--emit` enforces only the STATIC half -- that every RC or count the `phase:` prose asserts is DECLARED by a claim -- because re-running the sweeps inside `--emit` would double the cost of every wrap and a slow gate is a switched-off gate. THE RE-RUN IS A STEP YOU TAKE, and the wrap order names it. (b) The prose is read as an AUDIT of the registry, never as the work list: an assertion no claim declares turns the leg RED (UNREGISTERED-CLAIM) instead of quietly shrinking what gets run. If you add a sweep to `phase:`, declare it, or the gate will tell you exactly what to paste."
  - "AN EXIT CODE IS THE WEAKEST HALF OF A CLAIM, AND THIS WAS PROVEN LIVE RATHER THAN ARGUED. `-96` added 27 tests, and its own registry still said `pytest` 1121. The RC stayed 0 through every run -- the pipe defect that started this whole card would have reported GREEN -- and only the COUNT moved, 1121 to 1148. The leg re-ran it three times and then refused it. SO: when you register a claim, register a COUNT wherever the command prints one, with a `count_re` that captures exactly one group. Three of the nineteen claims print no number to hold them to (`verify-layout.sh`, `redproof-layout.sh`, `wt170 --verify`) and their `note` says so out loud; making those printable is free value for whoever needs it."
  - "A MANIFEST OVER AN EMPTY SET MUST CARRY AN EXPLICIT SENTINEL ROW UNDER GUARD, NOT ZERO ROWS. `docs/deliverable/FIGURES.tsv` lists figure -> script -> source, and the corpus has no figures, so `every figure is listed` is satisfied VACUOUSLY -- the row closes and reopens in silence the day someone pastes in a chart. The working shape, and it generalises to any manifest over an empty set: a named sentinel (`@zero-figures`) that names a real committed script and a real committed source so the criterion's `test -f` stays honest, plus a guard that refuses to let the sentinel coexist with a real member (SENTINEL-WITH-FIGURES) and refuses to let it be deleted while the count is still zero (SENTINEL-MISSING). The count itself is measured FIVE ways -- the narrow grep, an eight-pattern sweep that catches mid-line images the `^!\\[` anchor walks past, zero image files tracked repo-wide, zero image XObjects in the 145-page PDF, and `preamble.tex` not loading graphicx at all."
  - "A RED-PROOF'S OWN COVERAGE CHECK MUST ENUMERATE FROM A DECLARED REGISTRY IN THE CODE UNDER TEST, NEVER BY SCRAPING ITS SOURCE TEXT. `-95` wrote a coverage check that regexed `wt177_figure_guard.py` for its failure tags, found NINE of the FOURTEEN it can emit, and printed FULL COVERAGE -- a check that could not see what it claimed to count, reporting a guarantee. This is `-94`'s rule biting its own author within the hour. The repair is a `TAGS` dict in the guard that the guard holds ITSELF to (it emits UNREGISTERED-TAG on drift) and that the red-proof imports, so a check added without a probe goes red BY CONSTRUCTION. Red-proofed: delete one probe and exactly one line goes WEAK, naming the orphaned tag."
  - "A WRAPPER SCRIPT DOCUMENTS THE RIGHT INVOCATION WITHOUT PREVENTING THE WRONG ONE. `board.py` takes four flags and requires one; called directly it silently drops `--project` and `--preamble` and emits a correct-status board with the whole `checklist-preamble.md` deleted. `-53` found that in its first ten minutes and wrote `scripts/regen-board.sh`, whose header calls itself `the ONLY supported invocation`. `-95` hit the identical trap FORTY-TWO SESSIONS LATER, because a session that never opens the wrapper never reads its warning. WHEN A WRONG PATH DEGRADES AN ARTEFACT, PUT THE CHECK ON THE ARTEFACT: `tests/test_board_is_not_degraded.py` fails on the degraded board and catches every future caller regardless of what they ran. REGENERATE THE BOARD WITH `bash scripts/regen-board.sh`, never `board.py`."
  - "`verify-layout.sh` PRODUCED A REAL-LOOKING FALSE RED AND THE CAUSE IS UNKNOWN. Once, this session: `FAIL manuscript changed since the capture: paper-III.md`, with no manuscript edited (`git diff 46f48fc..HEAD -- docs/papers/` empty). It would not reproduce. Measured against it: the live sha equals the manifest sha exactly, for all four papers, in git at the capture commit AND live; `wt176 --verify` against the committed PDF is RC 0; `verify-layout.sh` alone is RC 0; `verify-layout.sh` run CONCURRENTLY with a full pytest is RC 0, and no test in `tests/` writes a manuscript; `redproof-layout.sh` is RC 0 and mutates only inside its own worktrees. The one repair that WAS available is made: `wt176` now PRINTS wanted, got, and the path it read, so the next occurrence is diagnosable in two minutes instead of unreproducible. DO NOT report P13e green from a single run; if it goes red, re-run before believing it, and read the two shas. Carded 1217643242299336."
  - "`handoff_gate.py --emit` WAS UNSATISFIABLE BY ANY CORRECT HANDOFF UNTIL -94, and would have refused at -93 too. Its placeholder check was a substring test for TODO/TBD/FIXME/XXX, and this handoff NAMES all four -- in the drift flag whose subject is that a negative grep cannot tell USE from MENTION. It fails at the LAST ACT of the wrap, where the cheap way out is to delete the sentence; deleting documentation to satisfy a checker is how a repository forgets things. The CHECKER was fixed: the marker set recited as itself, and markers inside code spans, are mentions. tests/test_handoff_gate_placeholders.py, 14 tests, and the load-bearing ones are the controls -- a bare TODO in prose is still refused, and neither exemption may launder a real leftover beside it. If you widen those exemptions, add the control first."
  - "AN EVIDENCE COMMAND MUST OBSERVE THE THING THE SENTENCE CLAIMS, AND ROW 5a47d4caef BROKE TWICE IN TWO SESSIONS PROVING IT. Its first line printed a WHOLE-REPOSITORY collected-test count, quoted verbatim in the note, while the sentence it adjudicates is about tests/test_redistribution.py -- so every test added ANYWHERE reddened a paper-II row. -93's six tests took it 1095->1101 and -93 HANDED IT OVER REPORTED GREEN; -94 found it red at cbffb8d, then broke it again the same session with fourteen tests of its own (1101->1115). Now a PREDICATE (this paper's file is in the whole-repository collection), red-proofed both ways: three tests added elsewhere leave wt172 --verify RC 0, one test added to the paper's own file makes it RC 2. If it observes something merely NEARBY, every change to the neighbourhood is a false alarm, and false alarms are how a guard gets switched off. HOW A RED SWEEP GETS REPORTED GREEN is the other half and is unfixed: '$? after a pipe is the LAST command's' -- `tool --verify | tail -5` prints the success line AND yields tail's 0. That rule was already in this file's STEP 0; it protected the reader, not the writer. CLOSED at `-96`: card 1217643242299336 is done and the gate now re-runs the claims itself (`--claims-all`). NEVER report a sweep green from a piped exit code -- and note that the leg REFUSES to register a command containing a pipe, a semicolon or an ampersand, so the defect cannot be re-imported through the registry built to catch it."
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
  - "State Machine 1217654200494124 -- PROPAGATE THE CLAIM RE-RUNNER TO THE GLOBAL `HANDOFF-GATE.md` AS G-AM. The defect it catches is not this repository's: every project's handoff asserts exit codes in the same voice, and `$?` after a pipe is the pipe's everywhere. `-96` built and red-proofed the mechanism here and deliberately did NOT propagate it in the same at-bat -- that file is 212KB, sat at v2.61 the same day, and the edit needs a version bump, a changelog entry and a grep-verified sweep of every `G-A -> G-AL` range reference. The card carries the design constraints to carry over and the G-AI question (wire a mechanical check, or write the leg and SAY that wealth-tensor is its only mechanical implementation -- a doc-only leg that pretends to be mechanical is worse than one that admits it)."
  - "BOTH OF THE GATE CARDS ARE NOW CLOSED. 1217643681032027 (the durable re-evidence of row 5a47d4caef) closed at -94 in the session it was filed. 1217643242299336 (a gate that re-runs the sweeps a handoff claims green) closed at -96: the leg is built, red-proofed three ways, and running green over 23 declared claims. What is left of that thread is its PROPAGATION, filed as 1217654200494124 and ranked first in the context list -- the class is solved here and unsolved everywhere else."
  - "`wt177`: the front matter of each paper is set with markdown hard breaks by `build.sh`, so the author block no longer becomes one justified paragraph that hyphenates an e-mail address into 'jason@braatzre-search.com'. It still carries a first-line `\\parindent`, which reads slightly oddly on a three-line address block. Cosmetic, unmeasured, and the only thing about the rendered pages `-94` looked at and did not fix."
  - "**THIS IS `-97`'S AT-BAT** -- `redproof-layout.sh` and `verify-layout.sh` BOTH need lualatex, pandoc AND a git worktree, so neither runs in the container or in CI -- the same division `wt173 --verify` already has, and for the same reason. There is no toolchain-free guard on the manifest at all today: nothing catches a hand-edited `LAYOUT-MANIFEST.json` without a full rebuild. A cheap test that the manifest is SELF-CONSISTENT (page_count equals len(pages), fonts listed match `FONTS.tsv`, manuscripts listed match the four on disk) would run in milliseconds and is not written. See `next_at_bat` for the full brief and the done-when."
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
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-97 --task "toolchain-free guard on LAYOUT-MANIFEST.json"'
/tmp/dx '~/Scripts/rail'                     # check before you swing
/tmp/dx '~/Scripts/charter-read.sh wealthTensor-97'   # YOUR id, not your successor's
```
**READY first try at -61 through -96 — THIRTY-SIX for thirty-six.** Budget four minutes; it takes two.
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
**Every line below was RE-RUN by `handoff_gate.py --claims-all`, not quoted from the last
handoff.** That is new at `-96` and it is the point of the whole session: the `claims:` block in
the front matter is the machine-readable form of this list, and the gate holds the prose to it.

🟢 `python3 -m pytest -q` → **1148 passed, 1 warning.** RUN IT AND SAY THE NUMBER.
   (1121 inherited from `-95`, plus `-96`'s 27 in `test_handoff_claims_leg.py`.)
🟢 `python3 scripts/wt173_typography_probe.py --verify` → **RC 0**, 50 values held to a
   fresh build, 15 of 15 load-bearing values in the prose.
🟢 `python3 scripts/wt173_typography_probe.py --postconditions` → **RC 0**, **14 checks,
   5 NEGATIVE, 0 failed.**
🟢 `bash docs/deliverable/preflight.sh` → **RC 0** over **16** vendored fonts.
🟢 `wt133` · `wt148` · `wt154` · `wt156` · `wt160` · `wt163` · `wt166` · `wt169` — **ALL EIGHT RC 0.**
🟢 `wt170 --verify` → **RC 0** · `wt172 --verify` → **RC 0**, 17 paper-II rows.
   ⚠ Both WRITING paths exit 2 by design; `--verify` is the re-runnable mode.
🟢 `bash docs/deliverable/verify-layout.sh` → **RC 0**, 145 pages, rebuilt in a clean
   worktree from `5b525f1754de`. ⚠ It did **not** reproduce `-95`'s false red — five clean runs
   against one, and the drift flag stands.
🟢 `bash docs/deliverable/redproof-layout.sh` → **RC 0**, four probes.
🟢 `python3 scripts/wt177_figure_guard.py` → **RC 0** · `python3 scripts/redproof_wt177_figures.py`
   → **RC 0, 21/21 probes proven.**
🟢 ▲ `python3 scripts/redproof_wt178_claims.py` → **RC 0, 20 probes, 17 of 17 declared tags
   proven.** The coverage line is not decoration: delete one probe and exactly one **WEAK** line
   appears naming the orphaned tag (measured, not assumed).
🟢 ▲ `python3 scripts/handoff_gate.py --claims-all` → **RC 0**, **23 claims declared, 23
   re-run, 23 agreed** — the exit code captured with `rc=$?`, not read off the last line.** `--claims` alone skips the three slow ones and exits **2** on purpose.
🟢 `python3 scripts/defensive_count.py <each paper>` → defensive sentences **outside**
   §Limitations are **0 / 0 / 3 / 0** for papers I–IV. ▲ **Registered as four claims at `-96`** —
   the number had been inherited unverified for three handoffs, and the prose audit did not flag
   it because it is neither an `RC n` nor an `N passed`. Measuring it was the last thing `-96`
   did, and it agreed. Identical to the commit `-96` inherited, and `-96` edited no manuscript — proved, not
   asserted, by an empty `git diff 448b0be..HEAD -- docs/papers/`.
🟢 GATE: gate v2.61, `gate-selfcheck.sh` **PASS**, tree clean and pushed.

**Wrap order** (one step longer than you inherited — the new step is `--claims-all`):
commit → `gate-selfcheck` → **`handoff_gate.py --claims-all`** → `gate_passed: true` → `--stamp`
→ commit → push → `charter-read.sh <YOUR id>` → gate → `--emit`.
⚠ Run `--claims-all` **after your last mutation** — it runs `pytest` and the full layout
verification, and a run started before your last edit is answering a question you no longer asked.
It takes about **twelve minutes**; background it and poll.

The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.

---
## ▶ YOUR AT-BAT · ONE THING — A TOOLCHAIN-FREE GUARD ON `LAYOUT-MANIFEST.json`
`next_at_bat` in the front matter is the full brief and it is binding.

**Why this one.** The board still has no OPEN lanes — 57 CLOSED, 9 PENDING-HUMAN, zero OPEN, and
every remaining row is a human gate. So the work is the parking lot again, and with the gate card
closed this is its top item. It is a **named hole**, not a nicety: `verify-layout.sh`,
`redproof-layout.sh` and `wt173 --verify` all need lualatex, pandoc and a git worktree, so
**nothing** in CI, in a fresh clone, in the container, or in any session that has not run preflight
can notice a hand-edited `LAYOUT-MANIFEST.json`. P13e's entire claim rests on that file, and a file
nothing cheap can check is a file that drifts.

**The shape, and `-96` just built one of these — copy it.** The manifest DECLARES what it contains;
the test holds it to its own declaration. `page_count` equals `len(pages)`; the fonts listed match
`FONTS.tsv` row for row; the manuscripts listed are exactly the four on disk; every per-page hash
is well-formed and there are `page_count` of them; the capture commit named in the manifest is an
object in this clone. **Do not let the test discover its own scope** by iterating whatever keys
happen to be present — that is `-95`'s nine-of-fourteen defect and it reads as full coverage.

**DONE WHEN** `tests/test_layout_manifest_is_self_consistent.py` runs with **no toolchain** in
under a second and passes on the committed manifest; a red-proof provokes **every** failure it can
report, each asserted by its **specific tag** rather than by exit status alone, and says the count
out loud; the new guard is **registered in the `claims:` block** so the gate re-runs it; and
`pytest`'s count claim moves with it.

**DO NOT** close P13g, P9 or P8. All three are PENDING-HUMAN and explicitly not a session's to call.

**Ranked context, NOT a menu** — you have one assignment; this is here so you know what you are
not doing. (1) `1217654200494124`, propagating the claim re-runner to the global `HANDOFF-GATE.md`
as G-AM — real value, but it is a 212KB shared file another project's sessions edit the same day,
and it wants its own at-bat. (2) `wt174`, generalising `wt172 --verify` to the whole TSV
(`1217633269591608`). (3) widening `wt160.PAPERS` to all four manuscripts (`1217633320596131`).
(4) making `verify-layout.sh` and `redproof-layout.sh` print a count, so their claims can carry one.

**A guess at `-98`'s assignment, free, because the thinking is already done:** whichever of (1) or
(2) you did not take. If your at-bat lands early, do NOT start a second one — write the handoff.

## WHAT -96 DID
**One at-bat, three commits, and the gate caught its own author inside the hour.**

| commit | what |
|---|---|
| `f69555e` | `G-CLAIMS` in `scripts/handoff_gate.py` + `--claims` / `--claims-all` |
| `b6a2ca1` | `scripts/redproof_wt178_claims.py` — 20 probes, 17 of 17 declared tags |
| `3b67ff0` | `tests/test_handoff_claims_leg.py` — 27 toolchain-free tests, 0.06s |
| `6023e54` | the `claims:` registry and the handoff for `-97` |
| *(this one)* | `regen-board.sh` carries its check timeout — the board no longer downgrades a lane under load |

**The headline, in one sentence someone can mark right or wrong.** A handoff can no longer assert
an exit code or a count that nothing re-derives: the front matter declares its claims, the gate
re-runs each one un-piped, and a claim the registry omits turns the gate red rather than silently
leaving the work list.

**The three red-proofs the card demanded, said out loud.** A handoff asserting **TRUE** RCs
**PASSES** (exit 0). A handoff asserting a **FALSE** RC **FAILS** (exit 1, tag `FALSE-CLAIM`) — and
it was run **three** times before it was called false, asserted against the probe's own counter
file rather than inferred from the output. A check that **fails once then passes** is reported
**`FLAKY`** (exit 2), and the words `FALSE-CLAIM` appear nowhere in that run.

### The design decision `-95`'s two findings forced
The obvious build is a regex over the `phase:` prose that finds the claims and runs them. **That
build is `-95`'s nine-of-fourteen defect with a new subject:** an assertion the regex cannot parse
silently leaves the work list, and the leg prints a clean board over a shrunken set. So the handoff
**DECLARES** its claims in a registry and the leg holds it to the registry — and the prose is read
only in the **negative** direction, as an audit of the declaration. *Same regex, opposite failure
mode.* Proven non-vacuous on the real file: delete the `wt172 --verify` declaration and the leg
names the exact orphaned assertion.

The same rule is applied to the leg's own verdicts. `CLAIM_TAGS` is a declared registry of every
tag it can emit; `_tag()` is the single emission point and returns `UNREGISTERED-TAG` for anything
not in it; the red-proof **imports** that dict and prints `WEAK` for any tag it has no probe for.
Delete one probe and exactly one WEAK line appears. A verdict added without a probe goes red by
construction.

### The finding that outlives this at-bat
**An exit code is the weakest half of a claim, and this was proven live rather than argued.**
`-96` added 27 tests and its own registry still said `pytest` 1121. **The RC stayed 0 through every
run** — the pipe defect that started this entire card would have reported green — and only the
**count** moved, 1121 to 1148. The leg asked three times, got the same answer three times, and
refused it. *Register a count wherever the command prints one.* Three of the nineteen claims print
no number at all, and their `note` fields say so rather than pretending.

## THE TELL, now ONE HUNDRED AND THIRTY-THREE deep
-61–-92 as before, `-93` added five, `-94` five, `-95` two. **-96 adds two.**
- **-96(i) A CHECK MAY READ PROSE AS AN AUDIT OF A DECLARATION, NEVER AS ITS WORK LIST.** Same
  regex, opposite failure mode. Scraped, an assertion the parser cannot see silently **leaves**
  the work list and the check reports full coverage over a smaller set; used as an audit of a
  registry the thing under test **declares**, that same unparsed assertion turns the check
  **red**. This is `-95(i)` with the direction of the arrow named, and the build order follows
  from it: **the declaration first, the parser second.**
- **-96(ii) AN EXIT CODE IS THE WEAKEST HALF OF A CLAIM; THE COUNT IS WHAT MOVES.** A sweep that
  keeps passing while the world changes underneath it reports RC 0 forever. `pytest` went
  1121 → 1148 without its exit code flinching. **Hold a command to the number it prints**, and
  when it prints none, say so in the record instead of accepting the weaker claim in silence.

## TOOLING (▲ new at -96)
- ▲ **`python3 scripts/handoff_gate.py --claims-all`** — re-runs every entry in the front
  matter's `claims:` block, un-piped, and refuses the handoff on a disagreement that survives
  three attempts. `--claims` skips the slow ones and exits **2** (an un-run claim is not a verified
  one). Exit codes are the file's existing tri-state: **0** pass, **1** blocker, **2** cannot
  verify. **A registered `cmd` may not contain `|`, `;` or `&`** — the defect the leg exists to
  catch may not be re-imported through the registry built to catch it.
- ▲ `scripts/redproof_wt178_claims.py` — 20 probes over the **real** `claims_leg()`, each
  asserting its **specific tag**, plus a coverage check that imports `CLAIM_TAGS` from the code
  under test rather than scraping it.
- ▲ `tests/test_handoff_claims_leg.py` (27, 0.06s, no toolchain) — these hold **this
  repository's registry**, not the leg: every registered command names a file that exists, none
  can mask an exit code, every asserted count is observable, and the prose audit is non-vacuous.
- ▲ `scripts/wt177_figure_guard.py` · `scripts/redproof_wt177_figures.py` (21 probes) — P13f,
  from `-95`. The corpus list is PARSED from `PAPERS=` in `build.sh`, never hardcoded.
- ⚠ **`bash scripts/regen-board.sh` IS THE ONLY SUPPORTED BOARD REGENERATION.** `board.py`
  directly = a correct-status board with its preamble deleted. `test_board_is_not_degraded.py`
  catches it now regardless of what anybody ran. ▲ It now also exports
  `BOARD_CHECK_TIMEOUT=300`: the 25s default is 1.6x P13e's 16s check and downgrades that lane
  to CANNOT VERIFY whenever anything else is building. **Diff the board before you commit it.**
- ⚠ A full deliverable build is ~2 min, `redproof-layout.sh` ~5–8, and **`--claims-all` is ~12**.
  Background them (`nohup … > /tmp/x.out 2>&1 &`) and poll with a second `dx`. The leg flushes
  each line as it goes, so polling the file actually shows progress.
- ▲ darwin is **macOS + zsh**: no `grep -P`, no `cat -A`, `cut -c` is byte-based. Nested quotes →
  write the script LOCALLY, `--put` it, `dx 'bash /tmp/x.sh'`. `-94` wrote over forty, `-95` about
  twenty, `-96` a dozen — and `-96` lost one turn to a heredoc that tried to smuggle a quote
  through `\x27`, which is exactly the thing this line has been telling you not to do.
- ▲ **After string-surgery on a Python file, `py_compile` it before shipping.** Used on every
  patch this session. Two seconds, and it caught nothing — which is what a cheap guard looks like
  when it is working.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
  **Tags run to `wt178`; `wt174` is still a gap and `wt179` is next.**

## ESTATE
**CLOSED:** `1217643242299336` — the gate that re-runs what a handoff claims. Built, red-proofed
three ways, running green over 23 declared claims, and the closing comment carries the design
argument and every number.
**FILED:** `1217654200494124` — propagate the leg to the global `HANDOFF-GATE.md` as **G-AM**,
with the constraints to carry over and the G-AI question about whether a doc-only leg is honest.
**Board unchanged:** 57 CLOSED, 9 PENDING-HUMAN, **zero OPEN**. `-96` closed no row and reopened
none; its at-bat was infrastructure, which is the only kind of work left that is not a human gate.
**Carried:** `1217630566080626`, `1217629264134185`, `1217603625863293` (two instances),
`1217613775009402`, `1217568297674954`, `1217568192511533`, `1217596263441666`,
`1217596233063153`, `1217561667484767`, `1217593142996092`, `1217633320596131`,
`1217633269591608`, `1217629169253037` (partially closed — Paper I's four bare pointers stand).

## JASON-SIZED, not -97's
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
**None, and that is the honest answer rather than a dodge.** `docs/CHECKLIST.md` has had no OPEN
lane since `-95` closed P13f; every remaining row is a human gate, and P13g, P9 and P8 are
explicitly not a session's to call. `-96` therefore worked the parking lot's top item, which is
where the highest-value Claude-doable work now lives. **A successor should keep asking the
question** — a lane can reopen, and `test_board_is_not_degraded.py` plus `charter-read.sh` are
what would tell you. Regenerate with `bash scripts/regen-board.sh`, never `board.py`.

**One judgement `-96` did not make and is not settled:** P9 is the single handoff into P8, and its
own criterion says declaring readiness is the session's job. `-95` did not declare it because P7's
convergence counters are unmet and P9's criterion names convergence explicitly. `-96` did not
revisit that. **Re-examine it deliberately; do not inherit it as settled.**
