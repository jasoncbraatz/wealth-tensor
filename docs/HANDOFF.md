---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: b8fb4192644a5c0fdab4eecda767ab7033e14c92
updated: 2026-08-20
session: wealthTensor-99
session_n: 99
live_theme: "THE LEDGER MOVED, AND WHAT IT COST TO LEAVE A NAMED CHECK UNRUN. `docs/p7-passes.tsv` had its last row at `wealthTensor-83` and twenty sessions went by with no fresh-eyes read of any manuscript. Paper II got its TWELFTH `P7` read here and returned THREE findings on a frozen instrument set. The headline is `II-42`: section 3.4 has claimed since Paper II's FIRST independent read that the top-share statistic is also horizon-stable where the Gini is not; `-74` flagged it NOT MEASURED five passes ago AND NAMED THE EXACT CHECK, nobody ran it, and it is FALSE -- the top decile is the LESS stable statistic in 14 of 18 config-seed pairs, worst spread 0.1706 against 0.0496. CUT, not hedged. The other two are both inside the six lines the one intervening repair pass wrote, and `wt133_crossref_sweep` is GREEN on one of them because the section it points at RESOLVES -- A RESOLVING CROSS-REFERENCE IS NOT A CORRECT ONE, which is a class the sweep has never been able to see. RESIDUE 2 of 3, the highest any row carries, AND NO SIXTH MECHANISM IS PROPOSED: residue died at `-78`, and this row's largest finding survived nine reads. The board went RED on `P13e` the instant the prose moved -- the layout capture pins the manuscript sha256 -- and that is the guard working, not a regression. CONSECUTIVE-ZERO COUNT, ALL THREE MANUSCRIPTS: 0, 0, 0."
phase: "EVERY NUMBER HERE WAS RE-DERIVED BY THE GATE'S CLAIM RE-RUNNER, NOT QUOTED: `pytest` 1167 passed; `wt181 --verify` RC 0 over 9 checks, 3 NEGATIVE -- the P7 pass 12 seam, re-deriving section 3.3 as the 0.035 span's only home, the 14-of-18 horizon spread that killed section 3.4's sentence, and the control that the 0.90 criterion separates at 600, 1200 and 2400; `verify-layout.sh` RC 0 with 145 pages compared, REBUILT IN A CLEAN WORKTREE FROM THE COMMIT THAT CARRIES THE REPAIR; `redproof-layout.sh` RC 0 with 4 probes reported; `wt170 --verify` RC 0 with 11 of 15 rows verified; `redproof_wt180_counts.py` RC 0 over 12 of 12 declared probes; `wt173 --verify` RC 0; `wt173 --postconditions` RC 0 over 14 checks with 5 NEGATIVE; `preflight` RC 0 over 16 fonts; `wt133` and `wt148` and `wt154` and `wt156` and `wt160` and `wt163` and `wt166` and `wt169` -- ALL EIGHT RC 0, and `wt148` now reads 154 adjudicated with 0 unadjudicated and 0 STALE after the promise re-key this repair forced; `wt172 --verify` RC 0 over 18 paper-II rows; `wt177_figure_guard.py` RC 0; `redproof_wt177_figures.py` 21/21; `wt179_manifest_guard.py` RC 0 over 10 checks; `redproof_wt179_manifest.py` 26 of 26 tags; `redproof_wt178_claims.py` 17/17; `defensive` paper-I/II/III/IV = 0/0/3/0 outside Limitations -- UNCHANGED, and paper-II moved by TWO EDITS whose delta is +0 (G-COACH-3 holds, proved with `--against`); gate v2.61 PASS, tree clean and pushed."
gate_passed: true
gate_version: "2.61"
next_at_bat: "ASSIGNED, ONE THING: **run the next P7 read on PAPER-IV, and append its row to `docs/p7-passes.tsv`.** NOT another instrument, and NOT paper-II again. Paper IV was last read at `wealthTensor-81` and returned NINE findings; that was 2026-08-18 and it is now the STALEST manuscript in the corpus AND the one whose last count was highest. Paper III is next-stalest at `-83` (4 findings). Paper II was read at `-99` (3 findings) and is deliberately NOT yours: reading it back-to-back would be leg one of the two-independent-readers design, which `docs/p7-passes.tsv` says costs two sessions to buy one data point and is JASON'S to authorise. THE SHAPE, and the CHARTER wins over this file: coach model, not marksman. Every finding arrives WITH ITS REPAIR in the order STEELMAN > REPLACE > CUT > TEE-UP, never as a filed objection and NEVER as a new hedge pasted into the manuscript -- ABSORB is the illegal move and `scripts/defensive_count.py --against` is the checkable invariant (paper-IV is at 0 outside Limitations and must stay 0). A ZERO-FINDING PASS IS A CELEBRATED RESULT and it is literally half of what done means here -- but an HONEST zero: the ledger header tells you how to falsify your own row. FIVE MECHANISMS FOR THE FINDING COUNTER HAVE BEEN PROPOSED AND FOUR DIED ONE PASS LATER (new instruments, residue, depth, coverage; only enumeration lives). DO NOT PROPOSE A SIXTH, and do not credit a finding to an axis you did not run -- NOT-STATED is honest, a guess is not. `-99` had a 2-of-3 residue row sitting there begging to be a mechanism and declined; do the same. DONE WHEN: `docs/REVIEW-035-P7-paperIV-passN.md` exists (derive N from the ledger and the existing filenames -- and see the TEE-UPS section, because the paper-IV filenames currently carry TWO INCOMPATIBLE CONVENTIONS and picking one is part of this at-bat) with a numbered finding list and front matter in `REVIEW-034`'s shape (`new_instrument`, `instrument_name`, `findings_from_new_axis`, `residue_of_previous_pass`) PLUS its own falsifier block; ONE row appended to `docs/p7-passes.tsv` that survives that falsifier; every finding carries a landed repair or a carded tee-up; `defensive_count.py --against` shows +0 on paper-IV; and `--claims-all` re-runs 27 claims and agrees. ⚠ IF YOU EDIT THE MANUSCRIPT, TWO THINGS GO RED AND BOTH ARE YOURS TO CLOSE IN THE SAME SESSION: `wt148` reports STALE promise rows (re-key them, see `-99`'s commit), and `P13e` goes UNMET because the layout capture pins the manuscript sha256 (commit the repair FIRST, then `bash docs/deliverable/build.sh`, then `verify-layout.sh`, then `regen-board.sh`, then commit the recapture -- `-99` did exactly this and the two commits are the worked example). Do NOT close P7 -- it is PENDING-HUMAN, the convergence verdict is Jason's, and the ledger itself says the session doing the work must not score it. You run the pass; you do not call it. Do NOT close P13g, P9 or P8 either."
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
    count: 18
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
  - id: wt181 --verify
    cmd: python3 scripts/wt181_paperII_p7pass12.py --verify
    rc: 0
    count: 9
    count_re: ([0-9]+) checks, [0-9]+ NEGATIVE
    note: the P7 pass 12 SEAM. The patch path is a one-shot -- run it twice and the anchors are gone -- so --verify re-derives the MEASUREMENTS instead: II-40's section locator, II-42's 14-of-18 horizon spread and its true-reading control. Seconds, no toolchain
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
## STEP 0 · transport (zero bridge calls)
The bridge rotates every ~27–33 min (`claude-code#81248`). **DARLISH DOES NOT USE IT.** Asana /
Gmail / Twilio MCP tools **are** bridge-bound: if one vanishes mid-turn it self-heals in ~1 s,
retry next turn, **NEVER declare "can't continue" over it.** Never restart the Claude app for a
darlish problem.
```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
# post the printed DARLISH-ENROLL line, EXACTLY, as an Asana comment on task 1217316841710435
/tmp/darlish-up
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-100 --task "P7 read on paper-IV"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-100 --resource ~/repos/wealth-tensor --task "P7 paper-IV"'
/tmp/dx '~/Scripts/rail'                                     # check before you swing
/tmp/dx '~/Scripts/charter-read.sh wealthTensor-100'         # YOUR id, not your successor's
/tmp/dx 'python3 ~/repos/claude-blackbook/lessons.py search "P7 review pass paper-IV" --scope global,wealth-tensor'
```
**READY first try at `-61` through `-99` — THIRTY-NINE for thirty-nine.** Budget four minutes; it
takes two.
⚠ That last line is **not optional**. `-98` skipped student-in and `-99` did not; the search is
what surfaced `-63`'s backlog-drain leaf before a word of the pass was written.
⚠ `roster claim` needs `--resource` (a NAMED flag), not `--repo`. `ROSTER_BRAKE_ACK=<n files>` on
commits.
⚠ **RUN THE GATE AS `GATE_ROSTER_WHO=big-wealthTensor-100 bash ~/Scripts/gate-selfcheck.sh`.**
Without it, `G-AL` reads the LAST charter stamp in the shared ledger — which may belong to a
sibling — and tells you YOUR definition of done moved. Jason often runs 2–3 sessions at once;
`roster who` before you believe any cross-repo complaint.

**Working notes on the transport, all earned:**
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to `/tmp/`, poll with a second `dx`,
  and **capture the exit code by redirecting `echo $?` to a FILE**, never off the last line.
  **`pytest` takes ~78 s and is worth backgrounding.** ⚠ Launch it AFTER your last mutation.
- ▲ `tests/test_manuscript_sweeps_are_green.py` reads the promise TSV and
  `tests/test_the_three_counts_are_derived.py` reads the layout manifest, so **a TSV write or a
  manuscript edit invalidates a pytest run started before it.**
- ▲ **`dx` exit 3 = never reached darwin** (nothing ran, safe to re-run) · **4 = dropped AFTER the
  command started** (check state before re-running; no blind retry loops).
- ⚠ **NESTED QUOTES: write the script LOCALLY, `--put` it, then `dx 'python3 /tmp/x.py'`.**
  `-99` ignored this for ONE `git commit -F -` heredoc and the commit message landed mangled —
  apostrophes eaten, truncated mid-sentence — and had to be `--amend`ed from a `--put` file.
  **Follow it on the FIRST file, not the third.** The rule costs nothing and it is now
  three sessions' worth of evidence.

------
## THE STATE YOU INHERIT AND MUST PRESERVE
**Every line below was RE-RUN by `handoff_gate.py --claims-all`, not quoted from the last handoff.**

🟢 `python3 -m pytest -q` → **1167 passed, 1 warning.** RUN IT AND SAY THE NUMBER.
🟢 ▲ **NEW** `python3 scripts/wt181_paperII_p7pass12.py --verify` → **RC 0, 9 checks, 3 NEGATIVE.**
   The `P7` pass 12 seam — re-derives §3.3 as the 0.035 span's only home, the **14 of 18**
   horizon spread that killed §3.4's sentence, and the control that the 0.90 criterion separates
   at *T* = 600, 1200 and 2400. Seconds, no toolchain.
🟢 `wt173 --verify` → **RC 0** · `wt173 --postconditions` → **RC 0, 14 checks, 5 NEGATIVE.**
🟢 `bash docs/deliverable/preflight.sh` → **RC 0** over **16** vendored fonts.
🟢 `wt133` · `wt148` · `wt154` · `wt156` · `wt160` · `wt163` · `wt166` · `wt169` — **ALL EIGHT RC 0.**
   ▲ `wt148` now reads **167 promises emitted, 154 adjudicated, 0 unadjudicated, 0 STALE** — three
   rows moved at `-99` (two re-keys and one MINTED, see below).
🟢 `wt170 --verify` → **RC 0, 11 of 15 rows** · `wt172 --verify` → **RC 0**, **18** paper-II rows — seventeen inherited plus the one `-99` minted.
   ⚠ Both WRITING paths exit 2 by design; `--verify` is the re-runnable mode.
🟢 ▲ `bash docs/deliverable/verify-layout.sh` → **RC 0**, **145 pages compared**, rebuilt in a
   clean worktree from **`8df6d40b2791`** — the commit that carries `-99`'s prose repair, not the
   one before it.
🟢 `bash docs/deliverable/redproof-layout.sh` → **RC 0**, **4 probes reported.**
🟢 `wt177_figure_guard.py` RC 0 · `redproof_wt177_figures.py` **21/21** ·
   `wt179_manifest_guard.py` **RC 0, 10 checks** · `redproof_wt179_manifest.py` **26 of 26 tags** ·
   `redproof_wt178_claims.py` **17/17** · `redproof_wt180_counts.py` **12 of 12 declared probes**.
🟢 `handoff_gate.py --claims-all` → **RC 0**, **27 claims declared, 27 re-run un-piped, 27 agreed.**
   `--claims` alone skips the slow ones and exits **2** on purpose.
🟢 `defensive_count.py <each paper>` → **0 / 0 / 3 / 0** outside §Limitations for papers I–IV.
   ▲ **paper-II moved by TWO edits at `-99` and the delta is +0**, proved with `--against` rather
   than by re-quoting the level. G-COACH-3 holds.
🟢 GATE: gate v2.61, `gate-selfcheck.sh` **PASS**, tree clean and pushed.

**Board:** 57 CLOSED, 9 PENDING-HUMAN, **zero OPEN** — unchanged. `P13e` went **UNMET** mid-session
and was **restored in the same session**; see WHAT `-99` DID.

**Wrap order:** commit → `GATE_ROSTER_WHO=<you> gate-selfcheck` → `handoff_gate.py --claims-all`
→ `gate_passed: true` → `--stamp` → commit → push → `charter-read.sh <YOUR id>` → gate → `--emit`
→ `roster leave --who <you>`.
⚠ Run `--claims-all` **after your last mutation** — it runs `pytest` and the full layout
verification, and a run started before your last edit answers a question you no longer asked. It
takes **twelve to fourteen minutes**; background it and poll.

The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first…"*) must be **verbatim, above the
fold** — put it in FIRST.

---
## ▶ YOUR AT-BAT · ONE THING — THE NEXT P7 READ ON PAPER-IV
`next_at_bat` in the front matter is the full brief and it is binding. What follows is why.

**THE BOARD IS NOT THE DEFINITION OF DONE, and this is the second handoff in a row that has to say
so.** `docs/CHECKLIST.md` reads 57 CLOSED / 9 PENDING-HUMAN / **zero OPEN** and has for five
sessions. `-95` `-96` `-97` `-98` each read that, concluded correctly that no lane was open, and
built infrastructure. `definition_of_done` — in this file's own front matter — asks for **two
consecutive zero-finding review passes per paper.** Here is the actual state of that clause:

| manuscript | last read | findings | sessions since | consecutive zeros |
|---|---|---|---|---|
| **paper-IV** | `-81` | **9** | **19** | **0** |
| paper-III | `-83` | 4 | 17 | 0 |
| paper-II | `-99` | 3 | 1 | 0 |

**No paper has ever had a zero-finding pass.** Convergence is at minimum six more reads. Paper IV
is the stalest AND its last count was the highest, which is why it is yours.

**Paper II is deliberately NOT yours.** Reading it back-to-back would be leg one of the
two-independent-readers design, and `docs/p7-passes.tsv` says in its own header that this costs two
sessions to buy one data point and is **Jason's to authorise.** Do not spend it by accident.

**WHAT A GOOD PASS LOOKS LIKE, from twelve of them.** Run all five axes *before you write a word of
prose about them* — `wt130_quantifier_sweep.py paper-IV` (A1), grep the paper for the failure modes
it names in its own prose (A2, and REVIEW-021 §1 has paper-IV's list — **inherit it, do not
re-derive**), `wt133_crossref_sweep.py` (A3), run every command §N names and diff the output against
the tables (A4), and enumerate every backticked artefact and read it (A5). Then read the manuscript
end to end. **Then** decide what is a finding.

**AND READ THE PREVIOUS REVIEW'S "WHAT WAS NOT CHECKED" SECTION AS A STOCK, NOT A COURTESY.** That
is `-99`'s single most transferable finding: `II-42` came off `-74`'s not-checked list, where it had
sat for **five passes** with its target, its method and its negative control already written down.
When it was finally run it falsified a manuscript sentence that had survived **nine** `P7` reads.
REVIEW-021 §4 is paper-IV's equivalent list. Open it first.

---
## WHAT `-99` DID
**Paper II's TWELFTH independent `P7` read.** `scripts/wt181_paperII_p7pass12.py`, **24
post-conditions, 8 NEGATIVE, RC 0**, two manuscript edits, net −1 line, zero carded.
Full document: `docs/REVIEW-034-P7-paperII-pass12.md`. Ledger row: `docs/p7-passes.tsv`.
Counter: 9 → 2 → 4 → 3 → 4 → 5 → 3 → 2 → 2 → **3**.

**`II-42` · §3.4's horizon claim is FALSE · CUT.** *"The top-share statistic is also horizon-stable
where the Gini is not"* has been in the manuscript since Paper II's **first** independent read
(`2b3e24b5`). `-74` flagged it **NOT MEASURED**, named the exact check and called it *"a natural
`wt133`"*. Five passes went by. Measured at `wt181` E5: across *T* = 600/1200/2400, six
configurations × three seeds, **the top decile's spread exceeds the Gini's in 14 of 18 config-seed
pairs**, worst **0.1706** against **0.0496** — 3.4×. Cut rather than replaced, because the sentence
has two readings that disagree (REVIEW-008's `II-14` shape), stating the true one costs three
numbers §7 would then have to account for, and the sentence in front of it already carries the
separation **and** its 0.039 margin. The true reading is kept **measured** in REVIEW-034 §2.3.

**`II-40` and `II-41` · both inside the six lines `-92` wrote.** §7's exception clause points the
0.035 periodicity span at **§3.2** (it is in **§3.3**) and calls 0.039 a *"difference of numbers
both commands do print"* eleven words after declaring one of its two inputs unprinted. One edit
repairs both.

**THE CLASS WORTH STEALING: A RESOLVING CROSS-REFERENCE IS NOT A CORRECT ONE.**
`wt133_crossref_sweep` is **green** on `II-40`, because §3.2 exists. `A3` asks whether a pointer
*resolves* and has never asked whether it is *right*. `wt181` exposes `section_of()` as the seam
that separates the two questions for one number. **Generalising it — every `§N.M` reference that
carries a NUMBER must have that number inside that section — is a real at-bat and is NOT claimed
here.** It is the highest-value item in TEE-UPS below.

**`P13e` WENT RED AND CAME BACK, IN THE SAME SESSION.** The layout capture pins each manuscript's
sha256, so a prose repair invalidates it: `test_wt176_prints_the_pages_it_compared…` and
`test_the_sweep_exits_zero[promise]` both failed the moment the bytes moved, and the board
regenerated `P13e` as **UNMET**. That is the guard working. The fix is a two-commit dance and it is
**the worked example for your session** if you edit paper-IV:
`8df6d40` commits the repair RED and says so in its message → `bash docs/deliverable/build.sh` →
`verify-layout.sh` (rebuilds from a clean worktree at that commit) → `regen-board.sh` → `bbae6aa`
commits the recapture. **The rebuild needs a `source_commit` that CONTAINS the repair**, which is
why the red commit has to exist first.

**THE PROMISE TSV MOVED, AND ONE ROW WAS MINTED RATHER THAN RE-KEYED.** `promise_id` hashes
(paper, artefact, sentence), so editing a sentence re-keys it and `wt148` reports the old row STALE.
`b9dea67210 → fbd08a63f6` and `5f6d5c4fb9 → c6f855de23` are re-keys with the evidence carried
**byte-identical** — and that identity is the argument that they are re-keys and not
re-adjudications. `7ed9443301` is **new**: the repaired clause names `wt030_report.py`, and a repair
that names an artefact **emits a promise**. Its evidence carries a negative control (`wt030` prints
0.486/0.451/0.994/0.891/0.861 and does **not** print 0.90), which is the whole reason the clause
could stop calling the 0.039 margin a difference of printed numbers.

**NO SIXTH MECHANISM WAS PROPOSED, AND DECLINING WAS THE HARD PART.** Residue is **2 of 3** — the
highest fraction any row carries — and the story writes itself: the one intervening session edited
six lines without re-reading, and two of three findings are in them. Repair residue was proposed at
`-77` and **refuted at `-78`**. One row does not revive it, and this row carries its own
counter-evidence: `II-42` blames to Paper II's first read and survived nine of them. **A mechanism
that explains two findings and cannot touch the largest of the three is not a mechanism.**

---
## THE TELL, now ONE HUNDRED AND THIRTY-NINE deep
`-61`–`-97` as before, `-98` added two. **`-99` adds two.**
- **`-99`(i) A NOT-CHECKED LIST IS A STOCK, AND ITS OLDEST ENTRY IS ITS MOST VALUABLE.** `II-42`
  sat on `-74`'s list for five passes with its **target, method and negative control already
  written**, and when finally run it falsified a sentence nine `P7` reads had read past. The lists
  at the end of every REVIEW document are not a courtesy to the next session; they are the cheapest
  unspent work in the repository, because someone already did the thinking. **Open the previous
  review's §4 before you open the manuscript.**
- **`-99`(ii) A GUARD THAT ASKS WHETHER A POINTER *RESOLVES* IS GREEN ON A POINTER THAT IS
  *WRONG*.** `wt133` reports **0 unresolved** on a §7 clause that sends the reader to §3.2 for a
  number that lives in §3.3, because §3.2 exists. The sweep is not broken — it answers a narrower
  question than its name suggests, and three sessions read its green line as coverage it never
  claimed. **When a check goes green over a defect, ask what question it actually asks**, and write
  the answer next to the green line. Same family as `-98`(ii)'s cheap seam and `-94`'s
  mention-vs-use.

## TOOLING (▲ new at `-99`)
- ▲ **`python3 scripts/wt181_paperII_p7pass12.py --verify`** — 9 checks, 3 NEGATIVE, seconds, no
  toolchain. Importable seams: `section_of(text, needle)` (which `### N.M` subsection actually
  contains a string — bounded at the next heading of ANY level), `measure_horizons()`,
  `separation_by_horizon()`. **This is the pattern for every future P7 patch script:** the patching
  path is a one-shot and cannot go in the claim list, so give it a `--verify` that re-derives the
  MEASUREMENTS. Without it a pass's central fact is checkable exactly once, on the day it was made.
- ⚠ **`section_of()`'s first cut was WRONG and it failed closed** — it ended the last `### N.M` at
  end-of-file, swallowing §4–§7 into "3.4", so it reported the §7 *pointer* as an occurrence of the
  thing it points at. The repair rolled back untouched and the bug is recorded in the committed
  docstring rather than quietly fixed. **A locator whose ranges are wrong returns the one answer
  that cannot falsify anything.**
- ⚠ **`bash scripts/regen-board.sh` IS THE ONLY SUPPORTED BOARD REGENERATION**, never `board.py`,
  never while anything is building, and **diff it before you commit it.** At `-99` the diff was the
  thing that made `P13e` going red legible instead of alarming.
- ⚠ A full deliverable build is ~2 min, `verify-layout.sh` ~3, `redproof-layout.sh` ~5–8, and
  **`--claims-all` is ~12–14.** Background them and capture the exit code to a FILE.
- ▲ darwin is **macOS + zsh**: no `grep -P`, `cut -c` is byte-based. **Nested quotes → write the
  script LOCALLY, `--put` it, `dx 'python3 /tmp/x.py'`.** See STEP 0 for what `-99` paid for
  ignoring this once.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
  **Tags run to `wt181`; `wt174` is still a gap.**

## TEE-UPS — carded work `-99` found and did NOT do, with enough context to start at its high-water mark
1. **GENERALISE THE RESOLVING-vs-CORRECT CHECK. Highest value here.** `A3` (`wt133`) reports
   `0 unresolved` on paper-II while a `§N.M` pointer sends the reader to the wrong section. The
   checkable rule: **a cross-reference that carries a NUMBER must have that number inside the
   section it names.** `wt181.section_of()` is a working locator for exactly one number; the general
   sweep would run over all four manuscripts and is a natural `wt182`. It needs a NEGATIVE control
   (a pointer known-correct must stay silent) and it must not fire on a number that legitimately
   appears in two sections. **This is a new axis (A7) and would make its row `new`** — which is
   fine, as long as the row says so.
2. **PAPER-IV'S REVIEW FILENAMES CARRY TWO INCOMPATIBLE CONVENTIONS, and one of them is wrong.**
   `REVIEW-015-P7-paperIV-pass3.md` is titled *"Paper IV's independent P7 read"*;
   `REVIEW-021-P7-paperIV-pass2.md`, written SIX SESSIONS LATER, is titled *"Paper IV's SECOND
   independent P7 read"*. So `pass3` counts project-wide passes and `pass2` counts per-manuscript
   independent reads — and paper-II's files (`pass8`…`pass12`) use a third. **Pick one, say which
   in the new file, and do NOT rename the committed files** — twelve documents cite them by name and
   a rename breaks every pointer. Record the mapping instead.
3. **BOUCHAUD & MÉZARD'S TWO VERBATIM QUOTATIONS IN PAPER II §3.1, STILL NOT READ AGAINST SOURCE.**
   Flagged at `-74`, again at `-77`, again at `-99`. **THREE PASSES DEFERRED.** It is now the oldest
   unrun named check on paper-II, and `-99`'s lesson is exactly what those turn out to be worth.
   `REFERENCE-POLICY` §4 governs it; the entry names arXiv `cond-mat/0002374` as the text consulted.
4. **THE GENERAL FORM OF `II-34`, still a question rather than a finding.** 16 of the 18 tests reach
   the model through `econ()` at *T* = 600 while every reported figure is at *T* = 1200, and §7 calls
   those 18 *"the ones that hold this paper's claims in place."* `II-42` **strengthens** the lead:
   the top decile moves up to 0.17 between horizons. `-99` checked that **no current assertion
   breaks** — the three `top_share(res) > 0.95` lines are one-sided on the condensed side, which
   only strengthens with *T* — so it stays a question. Someone should answer it.
5. **`A6`, the docstring axis — PARKED, NOT SPENT.** Nineteen unasserted prose claims in
   `tests/test_redistribution.py`, and `test_periodicity_is_second_order_at_a_matched_average_rate`'s
   *"Verified horizon-stable at T = 600 and T = 1200"* is one of them — **the same words as `II-42`,
   in the apparatus rather than the manuscript.** Highest-value docstring of the nineteen.
6. **The nine uncited reference entries** (`wt133` sweep 2, card `1217568192511533`) and **the zakat
   citation gap** (flagged by the paper's own closing note, fourth pass running). Both untouched.

## ESTATE
**OPEN:** `1217654200494124` — propagate the claims leg to the global `HANDOFF-GATE.md` as `G-AM`
(filed by `-96`; it is a global-artefact change and deserves its own at-bat, not a ride-along).
**Carried:** `1217630566080626`, `1217629264134185`, `1217603625863293` (two instances),
`1217613775009402`, `1217568297674954`, `1217568192511533`, `1217596263441666`,
`1217596233063153`, `1217561667484767`, `1217593142996092`, `1217633320596131`,
`1217633269591608`, `1217629169253037` (partially closed — Paper I's four bare pointers stand),
`1217660747249042` (`bb-writers-audit`, repaired at `claude-blackbook` by `-98`).
⚠ `-99` filed **no** new card: everything it found either landed a repair or is in TEE-UPS above,
with enough context that the next session starts at this session's high-water mark.

## JASON-SIZED, not `-100`'s
(a) **The two-independent-readers design** — the only experiment that separates *"the paper has n
defects left"* from *"a reviewer finds n"*, and the first proposal in twelve rows that is not a
story a single pass told about itself. It costs two sessions to buy one data point. `-99` came out
of paper-II with the counter at 3 and a 2-of-3 residue row, which is the cleanest setup this has
ever had — **and it is still not a session's to spend.**
(b) The version stamp — **EIGHTEEN passes have declined to move it.**
(c) `wt077` already prints κ = *r*·E[η⁺]/(1+μ), matching to 0.44 % where Paper II §3.1's form is off
4–7 % — **changes a stated contribution, unassigned since `-81`.** `-99` re-opened it and closed it
again as a died-on-contact candidate (REVIEW-034 §3.2: REVIEW-004 already gives the exact form with
the wage term and REVIEW-011 adjudicated the sentence), **so it is no longer a defect — it is a
choice about how much of the closed form to put in the manuscript**, and that is a claim about the
MODEL that wants its own at-bat with a coach's repair attached.
(d) DECISION-001 closed, ROADS-001 unchanged. (e) The PAN history purge.
**(f) P7 IS A HUMAN GATE FOR THE VERDICT, NOT FOR THE WORK.** Sessions `-71` through `-99` ran
fourteen `P7` passes and wrote their REVIEW documents; what stays Jason's is **declaring
convergence**. Reading the row as *"no session may touch it"* is how it went twenty sessions
untouched. **Run the pass. Do not score it.**

---
## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)
**`P7`, and for the first time in five sessions that is not a dodge.** `docs/CHECKLIST.md` has had
no OPEN lane since `-95` closed `P13f`, and every remaining row is a human gate — but `P7`'s row is
a gate on the **verdict**, and its **work** is a session's. `-99` ran the work and did not score it:
`P7` is untouched at PENDING-HUMAN, and `docs/p7-passes.tsv` carries the twelfth row with the
consecutive-zero count stated at **0**.
**`P13e` reopened and re-closed inside the session** — the only board movement, and it was caused
by the at-bat rather than by drift.
A successor should keep asking the question; `test_board_is_not_degraded.py` and `charter-read.sh`
are what would tell you a lane reopened. Regenerate with `bash scripts/regen-board.sh`, never
`board.py`.

**The judgement still not settled, now for the fourth handoff running:** `P9` is the single handoff
into `P8`, and its own criterion says declaring readiness is the session's job. `-95` did not
declare it because `P7`'s convergence counters are unmet and `P9`'s criterion names convergence
explicitly. `-96`, `-97`, `-98` and `-99` did not revisit it. **The counters are still unmet — all
three papers sit at zero consecutive zero-finding passes — so the reason still holds.** But
re-examine it deliberately rather than inheriting it: four sessions of not-revisiting is how an
unexamined judgement becomes a fact.
