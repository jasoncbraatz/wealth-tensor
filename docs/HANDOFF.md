---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: 11226ed3d7094439a9afc75bc97420f5a8fdc605
updated: 2026-08-19
session: wealthTensor-98
session_n: 98
live_theme: "THE THREE CLAIMS THAT WERE HELD TO AN EXIT CODE NOW CARRY A NUMBER, AND THE NUMBER IS DERIVED RATHER THAN DECLARED. `verify-layout.sh`, `redproof-layout.sh` and `wt170 --verify` are three of the twenty-six most expensive checks in this repository and TWO OF THEM GUARD THE DELIVERABLE; until now an exit code was the whole of each one, and an exit code stays 0 while the corpus moves underneath it -- which is exactly how `-96` shipped `pytest` 1121 for a suite of 1148. Each now prints ONE stable line carrying a count it MEASURED: 145 pages compared, derived from the freshly rebuilt PDF and cross-checked inside the script against a second independent read; 4 probe verdicts, tallied at the moment each is printed so a probe that dies before reporting LOWERS the number; 11 promise rows re-run against their committed evidence. THE MATRIX BEHIND THEM IS THE POINT -- `redproof_wt180_counts.py` proves each count DERIVED by moving the real corpus (a page out of the PDF, a probe call site out of the script, a row retired out of the adjudication file) and proves the leg BITES a wrong one on the FALSE-CLAIM TAG, with a CONTROL beside every bite requiring that tag to be SILENT on the clean case. AND THE THING THIS SESSION FOUND BY LOOKING ONCE MORE SOMEWHERE IT HAD NOT LOOKED: `docs/p7-passes.tsv` ENDS AT `-83`. FIFTEEN SESSIONS HAVE PASSED WITHOUT A SINGLE FRESH-EYES READ OF A MANUSCRIPT, while the definition of done asks for two consecutive ZERO-finding passes per paper and no paper has ever had one. The board is unchanged -- 57 CLOSED, 9 PENDING-HUMAN, ZERO OPEN -- but the DoD is not the board, and the DoD is where the work is."
phase: "EVERY NUMBER HERE WAS RE-DERIVED BY THE GATE'S CLAIM RE-RUNNER, NOT QUOTED: `pytest` 1167 passed (1156 inherited from `-97`, plus 11 in the new tests/test_the_three_counts_are_derived.py); THE THREE COUNTED-BY-NOTHING CLAIMS NOW CARRY A NUMBER AND THE GATE RE-RAN ALL THREE -- `verify-layout.sh` RC 0 with 145 pages compared against the manifest, derived from the freshly rebuilt PDF and cross-checked inside the script against a second independent pypdf read; `redproof-layout.sh` RC 0 with 4 probes reported, tallied at the moment each verdict is printed so a probe that dies before reporting lowers the number; `wt170 --verify` RC 0 with 11 of fifteen rows verified against their committed evidence, 3 retired to committed successors and 1 re-evidenced in place; NEW `redproof_wt180_counts.py` RC 0 with 12 of 12 declared probes proven over a declared CLAIMS x TAGS matrix -- REGISTERED, DERIVED, BITES and CONTROL for each of the three, every bite asserted on the FALSE-CLAIM tag and every control requiring that tag to be silent on the clean case; `wt173 --verify` RC 0; `wt173 --postconditions` RC 0 over 14 checks with 5 NEGATIVE and 0 failed; `preflight` RC 0 over 16 vendored fonts; `wt133` and `wt148` and `wt154` and `wt156` and `wt160` and `wt163` and `wt166` and `wt169` -- ALL EIGHT RC 0; `wt172 --verify` RC 0 over 17 paper-II rows; `wt177_figure_guard.py` RC 0; `redproof_wt177_figures.py` RC 0 over 21 probes; `wt179_manifest_guard.py` RC 0 over 10 checks with no toolchain; `redproof_wt179_manifest.py` RC 0 with 26 of 26 declared tags proven; `redproof_wt178_claims.py` RC 0 over 17 declared tags; G-CLAIMS run over the committed handoff -- 26 claims declared, 26 re-run un-piped, 26 agreed, exit code captured with rc=$?; `defensive paper-I` and `defensive paper-II` and `defensive paper-III` and `defensive paper-IV` -- 0/0/3/0 sentences outside Limitations, UNCHANGED and NO MANUSCRIPT EDITED (`git diff 54ceeac..HEAD -- docs/papers/` empty); gate v2.61 PASS, tree clean and pushed."
gate_passed: true
gate_version: "2.61"
next_at_bat: "ASSIGNED, ONE THING: **run P7 pass 12 on paper-II, and append its row to the ledger.** NOT another instrument. `docs/p7-passes.tsv` -- the file this project built precisely so that claims about its own review process would be measured rather than told -- ENDS AT `wealthTensor-83`. Fifteen sessions have gone by without one fresh-eyes read of a manuscript, while `definition_of_done` asks for TWO CONSECUTIVE ZERO-FINDING PASSES PER PAPER and no paper has ever had one. Last reads: paper-II at `-79` (2 findings), paper-IV at `-81` (9), paper-III at `-83` (4). Paper II is the closest thing to convergence this corpus has -- 3, 2, 2 across three frozen-instrument passes -- so it is the read that can actually END something. THE SHAPE: read paper-II with fresh eyes under the CHARTER (coach model, not marksman); every finding arrives WITH ITS REPAIR in the order STEELMAN > REPLACE > CUT > TEE-UP, never as a filed objection and NEVER as a new hedge pasted into the manuscript -- ABSORB is the illegal move and the defensive-sentence count is the checkable invariant. A ZERO-FINDING PASS IS A CELEBRATED RESULT, not a failure to find work; it is literally half of what done means here. But it must be an honest zero: `docs/p7-passes.tsv`'s header tells you how to falsify your own row, and five proposed mechanisms for the finding counter have died one pass after being proposed (new instruments, residue, depth, coverage; only enumeration survives) -- so do NOT propose a sixth and do not credit findings to an axis you did not run. DONE WHEN: docs/REVIEW-034-P7-paperII-pass12.md exists with a numbered finding list and its front matter filled in the shape REVIEW-019 uses (new_instrument, instrument_name, findings_from_new_axis, residue_of_previous_pass) plus its own falsifier block; one row appended to docs/p7-passes.tsv that survives that falsifier; every finding carries a landed repair or a carded tee-up; `defensive_count.py` is NON-INCREASING on paper-II (0 outside Limitations, and it must stay 0); and `--claims-all` re-runs 26 claims and agrees. Do NOT close P7 -- it is PENDING-HUMAN and the convergence verdict is Jason's, not a session's; you run the pass, you do not score it. Do NOT close P13g, P9 or P8 either."
blockers: []
claims:
  - id: pytest
    cmd: python3 -m pytest -q
    rc: 0
    count: 1167
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
    count: 11
    count_re: ([0-9]+) of [0-9]+ rows verified
    note: DERIVED from what the run re-ran -- 11 live rows of fifteen, 3 retired to committed successors, 1 re-evidenced. The WRITING path exits 2 by design; --verify is the re-runnable mode
  - id: wt172 --verify
    cmd: python3 scripts/wt172_tsv.py --verify
    rc: 0
    count: 17
    count_re: ([0-9]+) paper-II rows
    note: the claim -93 handed over green while it was red -- the reason this leg exists
  - id: verify-layout.sh
    cmd: bash docs/deliverable/verify-layout.sh
    rc: 0
    count: 145
    count_re: wt176: ([0-9]+) pages compared
    slow: true
    note: needs lualatex, pandoc and a worktree. The count is wt176's, printed un-piped inside this run and DERIVED from the freshly built PDF; the script cross-checks it against a second, independent pypdf read and dies if they disagree
  - id: redproof-layout.sh
    cmd: bash docs/deliverable/redproof-layout.sh
    rc: 0
    count: 4
    count_re: redproof-layout: ([0-9]+) probes reported
    slow: true
    note: 5-8 minutes, four probes. The count is verdicts REPORTED, tallied in say(), so a probe that dies before reporting LOWERS it -- there is deliberately no declared total to print back
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
  - id: wt179_manifest_guard.py
    cmd: python3 scripts/wt179_manifest_guard.py
    rc: 0
    count: 10
    count_re: ([0-9]+) checks run
    note: the cheap guard on LAYOUT-MANIFEST.json -- no TeX, no pandoc, no worktree, 0.07s
  - id: redproof_wt179_manifest.py
    cmd: python3 scripts/redproof_wt179_manifest.py
    rc: 0
    count: 26
    count_re: ([0-9]+) of [0-9]+ declared tags proven
    note: 33 probes; the count is the TAGS registry it covers, not the probe total
  - id: redproof_wt178_claims.py
    cmd: python3 scripts/redproof_wt178_claims.py
    rc: 0
    count: 17
    count_re: ([0-9]+) of [0-9]+ declared tags proven
    note: the red-proof for this leg -- it holds ITSELF to a claim like everything else
  - id: redproof_wt180_counts.py
    cmd: python3 scripts/redproof_wt180_counts.py
    rc: 0
    count: 12
    count_re: ([0-9]+) of [0-9]+ declared probes proven
    note: the CLAIMS x TAGS matrix for the three counts above -- REGISTERED, DERIVED, BITES, CONTROL, proven cheaply by moving the real corpora rather than by rebuilding them
drift_flags:
  - "THE REVIEW LEDGER STOPPED AT `-83` AND FIFTEEN SESSIONS DID NOT NOTICE, BECAUSE EVERY ONE OF THEM WAS LOOKING AT THE BOARD. `docs/CHECKLIST.md` has read 57 CLOSED / 9 PENDING-HUMAN / ZERO OPEN for four sessions running, and each of `-95` `-96` `-97` `-98` read that, concluded correctly that no lane was open, and went to the infrastructure parking lot. THE BOARD IS NOT THE DEFINITION OF DONE. `definition_of_done` in this very front matter asks for three preprints at ready-to-submit AND convergence -- TWO CONSECUTIVE ZERO-FINDING P7 PASSES PER PAPER -- and `docs/p7-passes.tsv`, the ledger this project built so that exactly this claim would be measured rather than told, has its last row at `wealthTensor-83`. Paper II was last read at `-79`, paper-IV at `-81`, paper-III at `-83`. NO PAPER HAS EVER HAD A ZERO-FINDING PASS, so convergence is not one pass away for any of them; it is at minimum two per paper, six reads, and the counter has never gone below two. THE GENERAL SHAPE, and it is the expensive one: when a project has a board AND a definition of done, a session that consults only the board will find the board says nothing is open, and will build tools. Tools are cheap to justify and impossible to finish. CONSULT THE DoD FIRST; the board is a subset of it."
  - "A COUNT IS ONLY A MEASUREMENT IF SOMETHING CHEAP CAN MOVE IT, AND THAT IS WHY THE RED-PROOF COSTS SECONDS INSTEAD OF EIGHT MINUTES. The three claims closed here are guarded by four lualatex builds and fifteen re-executed evidence cells; a red-proof that had to RUN them to see whether their numbers move would be a red-proof that runs in no CI, no fresh clone and no container -- which is `-97`'s wt179 lesson pointed at its author's successor. So each number was given a CHEAP SEAM through which the real world can be moved: wt176 prints the pages it compared BEFORE the verdict branch (so a PDF one page short says 144 rather than losing the line to an early return); the probe tally lives in a sourced `probe-tally.sh` (so it can be driven with three verdicts or seven in milliseconds, and the REAL script can be run with its probe BODY stubbed to prove the wiring and with one call site deleted to prove the number falls); and `wt170 --verify` is importable, so the adjudication corpus can be handed a retirement in a temp file. WHAT THE SEAMS DO NOT PROVE is that the real commands print those lines on a real run -- only `--claims-all` at wrap proves that, and BOTH docstrings say so. Do not delete one half because the other is green."
  - "THE 25-SECOND BOARD TIMEOUT WAS STILL LIVE IN THE GATE ITSELF, WHICH IS THE HALF THAT MATTERS. `-96` measured `board.py`'s default `BOARD_CHECK_TIMEOUT` (25s) against P13e's criterion (`verify-layout.sh`, 16s idle -- a 1.6x margin), watched a CLOSED lane come back CANNOT VERIFY from concurrent load alone, and repaired `regen-board.sh`. It said in its own traps that `gate-selfcheck`'s board check was NOT covered, and that is the worse half: the gate runs at WRAP, at the exact moment this handoff tells you to background a twelve-minute `--claims-all`. `-97` fixed it at the artefact -- `gate-selfcheck.sh` now runs the board `--check` with `BOARD_CHECK_TIMEOUT` defaulted to 300 inside the command substitution's own subshell, so it neither leaks to the caller nor overrides an explicit value. Proven three ways: default 300, no leak, caller's 7 still wins. THE GENERAL SHAPE: when a wrapper is repaired and the CALLER is not, the hole moves to whoever did not read the wrapper -- fix every invocation of a shared engine, not the one you were standing in."
  - "THE MANIFEST NOW HAS A CHEAP GUARD AND IT DELIBERATELY DOES NOT REPLACE THE EXPENSIVE ONE. `scripts/wt179_manifest_guard.py` holds `LAYOUT-MANIFEST.json` to itself, to `FONTS.tsv` row for row, to the manuscripts on disk in both directions, to the committed PDF's bytes and to the commit it names -- 10 checks, 0.07s, standard library plus `git`. It CANNOT tell whether the manifest describes reality; only `verify-layout.sh`'s rebuild can, and both module docstrings say so. That division is the one `test_recipe_is_held_to_the_measurement.py` already documents for RECIPE.md, and the reason is the same: without the cheap half, the expensive half is the only half, which in practice means nothing runs in CI, in a fresh clone, or in the container. If you change the manifest you must still run BOTH."
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
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-99 --task "P7 pass 12 on paper-II"'
/tmp/dx '~/Scripts/rail'                     # check before you swing
/tmp/dx '~/Scripts/charter-read.sh wealthTensor-99'   # YOUR id, not your successor's
```
**READY first try at -61 through -98 — THIRTY-EIGHT for thirty-eight.** Budget four minutes; it takes two.
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

🟢 `python3 -m pytest -q` → **1167 passed, 1 warning.** RUN IT AND SAY THE NUMBER.
   (1156 inherited from `-97`, plus `-98`'s 11 in `test_the_three_counts_are_derived.py`.)
🟢 `python3 scripts/wt173_typography_probe.py --verify` → **RC 0**, 50 values held to a
   fresh build, 15 of 15 load-bearing values in the prose.
🟢 `python3 scripts/wt173_typography_probe.py --postconditions` → **RC 0**, **14 checks,
   5 NEGATIVE, 0 failed.**
🟢 `bash docs/deliverable/preflight.sh` → **RC 0** over **16** vendored fonts.
🟢 `wt133` · `wt148` · `wt154` · `wt156` · `wt160` · `wt163` · `wt166` · `wt169` — **ALL EIGHT RC 0.**
🟢 ▲ `wt170 --verify` → **RC 0, 11 of fifteen rows verified** against their committed evidence
   (3 retired to committed successors, 1 re-evidenced in place) · `wt172 --verify` → **RC 0**,
   17 paper-II rows. ⚠ Both WRITING paths exit 2 by design; `--verify` is the re-runnable mode.
🟢 ▲ `bash docs/deliverable/verify-layout.sh` → **RC 0**, **145 pages compared against the
   manifest**, rebuilt in a clean worktree from `5b525f1754de`. The count is `wt176`'s, printed
   un-piped inside the run and derived from the fresh PDF; the script now cross-checks it against a
   second independent `pypdf` read and **dies if the two instruments disagree**. ⚠ It did **not**
   reproduce `-95`'s false red — six clean runs against one, and the drift flag stands.
🟢 ▲ `bash docs/deliverable/redproof-layout.sh` → **RC 0**, **4 probes reported** — tallied in
   `say()` as each verdict is printed, so a probe that dies before reporting **lowers** it.
🟢 `python3 scripts/wt177_figure_guard.py` → **RC 0** · `python3 scripts/redproof_wt177_figures.py`
   → **RC 0, 21/21 probes proven.**
🟢 ▲ `python3 scripts/wt179_manifest_guard.py` → **RC 0, 10 checks**, 145 pages / 16 fonts /
   4 manuscripts described, in **0.07 s with no toolchain** — the whole point of it.
🟢 ▲ `python3 scripts/redproof_wt179_manifest.py` → **RC 0, 33 probes, 26 of 26 declared tags
   proven.** Delete the two `SILENT-WRONGNESS-NONZERO` probes and exactly one **WEAK** line
   appears, exit 1 — measured, not assumed.
🟢 ▲ **In a FRESH CLONE** (`git clone`, nothing built, no preflight): guard **RC 0 in 0.047 s**,
   `test_layout_manifest_is_self_consistent.py` **8 passed in 1.11 s**. That is the claim the
   at-bat was about, proven rather than argued.
🟢 `python3 scripts/redproof_wt178_claims.py` → **RC 0, 20 probes, 17 of 17 declared tags
   proven.** The coverage line is not decoration: delete one probe and exactly one **WEAK** line
   appears naming the orphaned tag (measured, not assumed).
🟢 ▲ `python3 scripts/redproof_wt180_counts.py` → **RC 0, 12 of 12 declared probes proven** — a
   declared CLAIMS × TAGS matrix (REGISTERED · DERIVED · BITES · CONTROL) over the three counts
   above. Every DERIVED probe MOVES the real corpus; every BITES asserts the **`FALSE-CLAIM` tag**;
   every CONTROL requires that tag to be **silent** on the clean case. ~90 s.
🟢 `python3 scripts/handoff_gate.py --claims-all` → **RC 0**, **26 claims declared, 26
   re-run, 26 agreed** — the exit code captured with `rc=$?`, not read off the last line.** `--claims` alone skips the three slow ones and exits **2** on purpose.
🟢 `python3 scripts/defensive_count.py <each paper>` → defensive sentences **outside**
   §Limitations are **0 / 0 / 3 / 0** for papers I–IV. ▲ **Registered as four claims at `-96`** —
   the number had been inherited unverified for three handoffs, and the prose audit did not flag
   it because it is neither an `RC n` nor an `N passed`. Measuring it was the last thing `-96`
   did, and it agreed. Identical to the commit `-96` inherited, and `-96` edited no manuscript — proved, not
   asserted, by an empty `git diff 448b0be..HEAD -- docs/papers/`.
🟢 GATE: gate v2.61, `gate-selfcheck.sh` **PASS**, tree clean and pushed.
✅ **CLOSED at `-98`: all 26 claims that can print a count now do.** The three that were held to
   an exit code alone carry a `count` and a one-group `count_re`, each number derived from what the
   run did and each proven to bite.
⚠ **THE REAL RESIDUE IS NOT IN THE CLAIMS BLOCK.** `docs/p7-passes.tsv` ends at `-83` — **fifteen
   sessions with no fresh-eyes read of a manuscript** — while `definition_of_done` asks for two
   consecutive **zero-finding** P7 passes per paper and **no paper has ever had one.**
   **That is `-99`'s at-bat, and it is the first at-bat in five sessions that touches a paper.**

**Wrap order** (one step longer than you inherited — the new step is `--claims-all`):
commit → `gate-selfcheck` → **`handoff_gate.py --claims-all`** → `gate_passed: true` → `--stamp`
→ commit → push → `charter-read.sh <YOUR id>` → gate → `--emit`.
⚠ Run `--claims-all` **after your last mutation** — it runs `pytest` and the full layout
verification, and a run started before your last edit is answering a question you no longer asked.
It takes about **twelve to fourteen minutes** now (`redproof_wt180_counts.py` adds ~90 s and it
re-runs `wt170 --verify` twice by design); background it and poll. **Capture the exit code by
redirecting `echo $?` to a FILE** — not off the last line.

The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.

---
## ▶ YOUR AT-BAT · ONE THING — RUN P7 PASS 12 ON PAPER-II
`next_at_bat` in the front matter is the full brief and it is binding.

**Why this one, and why it is not another instrument.** Four sessions in a row — `-95`, `-96`,
`-97`, `-98` — opened `docs/CHECKLIST.md`, read **57 CLOSED / 9 PENDING-HUMAN / zero OPEN**,
correctly concluded that no lane was open, and went to the infrastructure parking lot. Each built
something good. **None of them read a paper.** `-98` looked once more in a place it had not
looked and found `docs/p7-passes.tsv` — the ledger this project built *precisely* so that claims
about its own review process would be measured rather than told — **ends at `wealthTensor-83`.**

| paper | last P7 read | findings | passes since |
|---|---|---|---|
| paper-II | `-79` | 2 | **none in 19 sessions** |
| paper-IV | `-81` | 9 | none in 17 |
| paper-III | `-83` | 4 | none in 15 |

Meanwhile `definition_of_done`, in this file's own front matter, asks for **two consecutive
ZERO-finding passes per paper**. **No paper has ever had one.** Convergence is therefore not one
read away for anybody — it is six reads minimum, and the counter has never gone below two.
**The board is not the definition of done.** Read the DoD first; the board is a subset of it.

**Why paper-II specifically.** It is the closest thing to convergence this corpus has: three
consecutive frozen-instrument passes returned **3, 2, 2**, it is at 5-of-5 on the axis matrix, and
`-79` was the first pass in the project's history with **zero manuscript edits** — both repairs
made an existing sentence true instead of changing it. It is the read that can actually *end*
something.

**How to run it, and the charter wins here.** Coach model, not marksman. Every finding arrives
**with its repair attached**, in order of preference — **STEELMAN → REPLACE → CUT → TEE-UP** — and
never as a filed objection. **ABSORB is the illegal move**: pasting the objection into the
manuscript as a new caveat. If a finding seems to demand fresh hedging prose, it demands a
*narrower claim* instead — rewrite the claim, delete the hedge. The checkable invariant is
`scripts/defensive_count.py`: paper-II is at **0** defensive sentences outside §Limitations and it
must not rise.

**A ZERO-FINDING PASS IS A CELEBRATED RESULT** — it is literally half of what done means here, and
Jason has said in the standing brief that he will jump for joy at an honest one. But it has to be
an *honest* zero. `docs/p7-passes.tsv`'s header tells you how to falsify your own row; use it.

**⚠ THE MECHANISM TRAP, five deep.** Every pass that proposed a mechanism for the finding counter
had it **refuted by the very next pass**: new instruments (`-71`/`-77`), residue (`-77`/`-78`),
depth of application (`-78`/`-79`), coverage of the axis matrix (`-80`/`-81`). Only **enumeration**
(`-82`/`-83`) has survived one pass. **Do not propose a sixth**, and do not credit a finding to an
axis you did not actually run — `NOT-STATED` is an honest cell and a guess is not.

**DONE WHEN** — `docs/REVIEW-034-P7-paperII-pass12.md` exists with a numbered finding list and
front matter in the shape `REVIEW-019` uses (`new_instrument`, `instrument_name`,
`findings_from_new_axis`, `residue_of_previous_pass`) **plus its own falsifier block**; one row
appended to `docs/p7-passes.tsv` that survives that falsifier; every finding carries a **landed
repair or a carded tee-up**; `defensive_count.py` on paper-II is **non-increasing (0, and it stays
0)**; and `--claims-all` re-runs **26** claims and agrees. **Do NOT close P7** — it is
PENDING-HUMAN, the convergence verdict is Jason's, and the row itself says the session that does
the work must not also score it. **You run the pass; you do not call it.** Do not close P13g, P9
or P8 either.

## WHAT `-98` DID
**The residue `-96` named and `-97` left is closed.** Three of the twenty-six claims printed no
count, so an exit code was the whole of each one — the half that stays 0 while the corpus moves,
which is exactly how `-96` shipped `pytest` 1121 for a suite of 1148. All three now print one
stable line carrying a number they **measured**.

- **`verify-layout.sh` → `wt176: 145 pages compared against the manifest`.** The line is printed
  by `wt176_layout_manifest.py --verify`, **before** its verdict branch (how many pages were
  compared is a fact about the run whether or not they matched — and a red-proof that removes a
  page has to *see* 144 rather than lose the line to an early return). The script then counts the
  fresh PDF **again, independently, with `pypdf`**, and **dies if the two instruments disagree**.
  Its own `verify-layout: 145 pages reproduced from …` line is the human-readable summary; the
  registry keys on `wt176`'s, which is the machine-stable one and can be reproduced in two seconds.
- **`redproof-layout.sh` → `redproof-layout: 4 probes reported`.** The tally lives in a new
  **`docs/deliverable/probe-tally.sh`** and is bumped inside `say()` — the single place a probe
  reports a verdict — so the number counts what the run **did**, not what the script intended.
  There is deliberately **no declared total** to compare against: a total written into the file
  would be a constant printed back at its reader. `tally_line` **refuses on zero** rather than
  printing a tidy `0 probes reported` for a `count_re` to match.
- **`wt170 --verify` → `11 of 15 rows verified against their committed evidence`.** This one
  needed no new code — the line was already there and already derived (`len(PIDS) − retired −
  revised`); it needed a `count_re`. Three rows are retired to committed successors and one is
  re-evidenced, which is why the honest number is 11 and not 15.

### The red-proof, and the reason it costs seconds instead of eight minutes
**`scripts/redproof_wt180_counts.py` — 12 of 12 declared probes, a CLAIMS × TAGS matrix.**

| | REGISTERED | DERIVED | BITES | CONTROL |
|---|---|---|---|---|
| `verify-layout.sh` | ✅ | a page out of the PDF → **144** | declared 146 → **FALSE-CLAIM** | declared 145 → tag **silent** |
| `redproof-layout.sh` | ✅ | a probe call site deleted → **3** | declared 5 → **FALSE-CLAIM** | declared 4 → tag **silent** |
| `wt170 --verify` | ✅ | a row retired to a successor → **10** | declared 12 → **FALSE-CLAIM** | declared 11 → tag **silent** |

Three things worth carrying forward:

1. **DERIVED is asserted by moving the real corpus, never by trusting the script.** `-92`'s trap is
   that a hand-written constant is bit-identical to its input on every run, which reads as
   agreement and is tautology. Each row above changes the world and requires the number to follow.
2. **BITES is asserted on the TAG, and every bite has a CONTROL beside it.** `-94` and `-95` each
   paid for a red-proof caught by a *different* guard than the one under test. A tag that fires on
   the clean case as well proves nothing, so the control is not optional decoration.
3. **The replay is real, not a golden file.** The BITES/CONTROL probes run the REAL `claims_leg()`
   over a throwaway handoff whose `cmd` is `cat <the line the real script printed minutes ago>` —
   captured this run, so it cannot go stale, and cheap enough that both probes run every time.

**The wiring proof is the part that is easy to skip.** A sourced tally proves the *mechanism*
counts; it does not prove `redproof-layout.sh` is wired to it. So the red-proof copies the **real
script**, replaces the body of `probe()` with a one-line stub, and runs it: real call sites, real
`say()`, real bump, real summary line, **no lualatex**. It reports 4. Delete one call site and it
reports 3. That is the corpus-with-one-fewer-member proof, on the actual artefact, in under a
second.

**What this does NOT prove, said plainly so nobody deletes the other half:** that the real commands
print those lines with those numbers on a real run. Only `--claims-all` at wrap proves that, and
both docstrings say so. `-98` ran `verify-layout.sh` for real anyway and watched both new lines
appear with 145.

### Bug spray — caught by the check, on its author, inside a minute
`-98`'s first cut of `test_wt170_counts_the_rows_it_actually_re_ran` took the **first two of
`PIDS`** and asserted two rows would be verified. **One was** — `dfd41f5263` is retired in the real
corpus. A list of *intentions* is not a list of *what runs*. Repaired with `R.live_pids()`, which
reads the committed corpus and excludes the superseded and the re-evidenced; the docstring records
the miss, because the cheapest possible place to learn that distinction is a test that fails in six
seconds.

## THE TELL, now ONE HUNDRED AND THIRTY-SEVEN deep
-61–-92 as before, `-93` added five, `-94` five, `-95` two, `-96` two, `-97` two. **-98 adds two.**
- **-98(i) A PROJECT WITH A BOARD *AND* A DEFINITION OF DONE WILL BE READ BOARD-FIRST, AND THE
  BOARD WILL SAY THERE IS NOTHING TO DO.** Four consecutive sessions read `zero OPEN`, concluded
  correctly, and built tools — while the DoD's own convergence clause had gone **fifteen sessions**
  without a single manuscript read. Tools are cheap to justify and impossible to finish; a paper
  read is neither. **CONSULT THE DoD FIRST. The board is a subset of it, not a synonym.**
- **-98(ii) GIVE EVERY EXPENSIVE CHECK A CHEAP SEAM, OR ITS COUNT WILL NEVER BE RED-PROOFED.**
  Three claims guarded by four lualatex builds and fifteen evidence cells now have their numbers
  proven derived *in seconds* — because the count line is printed before the verdict branch, the
  tally is sourced rather than inline, and the verifier is importable. **The seam is what makes the
  difference between a red-proof that runs everywhere and one that runs nowhere.**
- **-97(i) FIXING THE WRAPPER MOVES THE HOLE TO EVERYONE WHO NEVER OPENS IT.** `-96` repaired the
  board timeout in `regen-board.sh` — the supported invocation, with a twenty-line header
  explaining why — and the gate's own `--check`, which calls the same engine by a different path,
  kept the 25s default. The wrapper documents the right call without preventing the wrong one
  (that is `-95`'s lesson); repairing **only** the wrapper leaves the defect sitting with whoever
  did not read it. **When you fix a shared engine's invocation, grep for every caller.**
- **-97(ii) A CHEAP CHECK IS NOT A WEAK CHECK — IT IS THE ONLY ONE THAT EVER RUNS.** Three guards
  covered `LAYOUT-MANIFEST.json` and all three needed lualatex, pandoc and a worktree, so its real
  coverage in CI, in a fresh clone, and in every container session was **zero**. The 0.07s guard
  catches strictly less than the rebuild and catches it **everywhere and always**. When the
  expensive check is the only check, the artefact is unguarded everywhere the expensive check
  cannot go — which is nearly everywhere.

## TOOLING (▲ new at -98)
- ▲ **`python3 scripts/redproof_wt180_counts.py`** — the CLAIMS × TAGS matrix for the three counts.
  Importable: `registry()`, `live_pids()`, `tally_says(n)`, `stub_probe_run(drop_probes=)`,
  `wt176_verify(pdf)`, `pdf_minus_one_page()`, `wt170_verify(tsv=)`, `replay(...)`. ~90 s.
- ▲ **`docs/deliverable/probe-tally.sh`** — `tally_reset` / `tally_bump` / `tally_line <name>`.
  Sourced, so a count can be driven and checked without running the thing that produces it.
  `tally_line` **exits 1 on zero** rather than printing a matchable `0`.
- ▲ `tests/test_the_three_counts_are_derived.py` (11, ~7 s, no toolchain).
- ▲ **`python3 scripts/wt179_manifest_guard.py`** — the cheap manifest guard. `--json` for
  machines, `--manifest PATH` to point it at a copy. Exit **0** clean, **1** with findings; every
  finding is prefixed with its **TAG**. **No TeX, no pandoc, no worktree, 0.07s.**
- ▲ `scripts/redproof_wt179_manifest.py` — 33 probes over the real `check_all()`, each asserted by
  its tag **and** by a control proving that tag is silent on the clean manifest. Coverage is
  enumerated from `wt179_manifest_guard.TAGS`, never scraped.
- ▲ `tests/test_layout_manifest_is_self_consistent.py` (8, **0.96s**, no toolchain) — the guard
  green over the committed manifest, the red-proof re-run, the CLI proven to go red on a hand-edit,
  `SCHEMA` bound to the committed manifest's actual key set, and the coverage report proven
  non-vacuous **in both directions** in-process.
- ⚠ **In the container's staged tarball the guard is RED by design**, tagged `NOT-A-GIT-CLONE`,
  because there is no `.git` to check the capture commit against — the same standing trap that
  reddens `wt160`/`wt163`/`wt166`/`wt169` there. **Read the tag.** In a real clone it is green.
- ▲ **`python3 scripts/handoff_gate.py --claims-all`** — now **26** claims, **and every claim that
  can print a count now declares one.** `--claims` skips the slow ones and exits **2** (an un-run
  claim is not a verified one). **A registered `cmd` may not contain `|`, `;` or `&`** — which is
  why the red-proof's replay uses `cat FILE` and not a pipeline.
- ▲ `scripts/redproof_wt178_claims.py` (20 probes, 17 tags) · `tests/test_handoff_claims_leg.py`
  (27) — `-96`'s, and they hold **this repository's registry**, not just the leg.
- ▲ `scripts/wt177_figure_guard.py` · `scripts/redproof_wt177_figures.py` (21 probes) — P13f.
- ⚠ **`bash scripts/regen-board.sh` IS THE ONLY SUPPORTED BOARD REGENERATION.** It exports
  `BOARD_CHECK_TIMEOUT=300`, and as of `-97` **so does `gate-selfcheck`'s own board check.**
  **Diff the board before you commit it** — that is still the only thing that caught `-96`'s
  downgrade, and do not regenerate while anything is building.
- ⚠ A full deliverable build is ~2 min, `redproof-layout.sh` ~5–8, and **`--claims-all` is ~12**.
  Background them (`nohup … > /tmp/x.out 2>&1 &`), poll with a second `dx`, and capture the exit
  code with **`rc=$?`** — never off the last line.
- ▲ darwin is **macOS + zsh**: no `grep -P`, `cut -c` is byte-based. Nested quotes → write the
  script **LOCALLY**, `--put` it, `dx 'bash /tmp/x.sh'`. `-97` wrote eight and smuggled zero
  quotes; the rule works when you follow it on the first file rather than the third.
- ▲ **After string-surgery on a Python or shell file, `py_compile` / `bash -n` it before shipping.**
  Used on every patch this session.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
  **Tags run to `wt180`; `wt174` is still a gap.**

## ESTATE
**Board unchanged:** 57 CLOSED, 9 PENDING-HUMAN, **zero OPEN**. `-98` closed no row and reopened
none. ⚠ **And that sentence is the trap** — it has been true for four sessions and it is *why* four
sessions built tools. The work that is left is not on the board; it is in `definition_of_done`, and
`docs/p7-passes.tsv` says it has not been touched since `-83`.
**OPEN:** `1217654200494124` — propagate the claims leg to the global `HANDOFF-GATE.md` as **G-AM**
(filed by `-96`, untouched by `-97` on purpose: it is a global-artefact change and it deserves its
own at-bat rather than a ride-along).
**Carried:** `1217630566080626`, `1217629264134185`, `1217603625863293` (two instances),
`1217613775009402`, `1217568297674954`, `1217568192511533`, `1217596263441666`,
`1217596233063153`, `1217561667484767`, `1217593142996092`, `1217633320596131`,
`1217633269591608`, `1217629169253037` (partially closed — Paper I's four bare pointers stand).

## JASON-SIZED, not -99's
(a) **The two-independent-readers design** — 429 labelled pointer rows plus 153 adjudicated
promise rows, each carrying its own reason; (b) the version stamp — **SEVENTEEN passes have
declined to move it**; (c) the four-vs-three ruling, folded into the RESULT-001 in-place-edit card;
(d) DECISION-001 closed, ROADS-001 unchanged; (e) `wt077` already prints r·E[η⁺]/(1+μ), matching
to 0.44 % where Paper II §3.1's form is off 4–7 % — **changes a stated contribution, unassigned
since `-81`**, and `-96` and `-97` both left it: it is a claim about the MODEL and it wants its own
at-bat, with a coach's repair attached rather than a finding filed; (f) the PAN history purge.
**(g) STILL THE BIG ONE: with zero OPEN lanes left, every remaining row is a human gate** — P2, P3,
P5, P6, P7, P11, P13g, P9, P8. ⚠ **But P7 is a human gate for the VERDICT, not for the WORK.**
Sessions `-71` through `-83` ran thirteen P7 passes and wrote their REVIEW documents; what stays
Jason's is *declaring convergence*. Reading the row as "no session may touch it" is how it went
fifteen sessions untouched. **Run the pass. Do not score it.**

---
## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)
**None, and that is the honest answer rather than a dodge.** `docs/CHECKLIST.md` has had no OPEN
lane since `-95` closed P13f; every remaining row is a human gate, and P13g, P9 and P8 are
explicitly not a session's to call. `-97` therefore worked the parking lot's top item, which is
where the highest-value Claude-doable work now lives — and it is not a coincidence that the item
was *"the artefact P13e rests on has no cheap check."* **A successor should keep asking the
question**; a lane can reopen, and `test_board_is_not_degraded.py` plus `charter-read.sh` are what
would tell you. Regenerate with `bash scripts/regen-board.sh`, never `board.py`.

**One judgement still not settled, now for the third handoff running:** P9 is the single handoff
into P8, and its own criterion says declaring readiness is the session's job. `-95` did not declare
it because P7's convergence counters are unmet and P9's criterion names convergence explicitly.
`-96` did not revisit it; neither did `-97`. **Re-examine it deliberately; do not inherit it as
settled** — three sessions of not-revisiting is how an unexamined judgement becomes a fact.
