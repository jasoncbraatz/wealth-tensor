---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: b4744c431457fcf01d66d182198282f76de21f3e
updated: 2026-08-25
session: wealthTensor-106
session_n: 106
live_theme: "THE CORPUS SHIPPED. v1.0-preprint is tagged, P7 is CLOSED on a check that bites, and the successor is JASON rather than another session. PASS D LANDED 149 C-CLASS REPAIRS AND AN ADVERSARIAL VERIFIER REFUTED FORTY OF THE FIRST 166 -- seven of them FALSE STATEMENTS that every mechanical checker passed. REVIEW-039 section 7 predicted that rate at a quarter of the volume and it held. AND THE DEFECT CLASS NOBODY HAD LOOKED FOR: reading the three manuscripts AGAINST EACH OTHER found nine cross-document defects in 61 claims, including one where paper-III asserted what papers I, II and IV each state -- and this same pass had just cut it from paper-IV. A per-file verifier is structurally blind to the class a corpus-wide pass is most likely to create."
phase: "EVERY NUMBER HERE WAS RE-DERIVED BY THE GATE'S CLAIM RE-RUNNER, NOT QUOTED. THE CORPUS SHIPPED: v1.0-preprint is tagged and P7 is CLOSED on a check that bites rather than on an assertion. pytest 1168 passed; verify-layout.sh RC 0 with 145 pages compared and all 145 per-page hashes reproducing from a clean worktree; wt182 RC 0 over 20 post-conditions; wt185 RC 0 over 19; wt183 16; wt186 11; wt187 6; wt184 RC 0 over 28 post-conditions with 9 NEGATIVE; wt188 63/20; wt189 19/11; wt190 10/4; wt191 26/12; wt191b 11/5; wt192 25/11; wt192b 12/6; wt192c 13/8; wt181 --verify RC 0 over 9 checks with 3 NEGATIVE; wt133 wt148 wt154 wt156 wt160 wt163 wt166 wt169 -- ALL EIGHT RC 0; wt170 --verify RC 0 with 7 of 15 rows verified against committed evidence, DOWN FROM 11 because three rows retired and one was re-evidenced this pass; wt172 --verify RC 0 over 19 paper-II rows; wt173 --verify RC 0 with 50 values held to the build and 0 divergent, 15 of 15 load-bearing values present in the prose, and wt173 --postconditions RC 0 over 14 checks -- both after a re-measure, because the section 4.4 note moved the body characters-per-line from 65.43 to 64.95, still inside RECIPE section 0 62-68 band, so nothing was retuned and RECIPE.md moved at BOTH of its two sites; preflight RC 0 over 16 fonts; wt177_figure_guard.py RC 0; redproof_wt177_figures.py 21/21; wt179_manifest_guard.py RC 0 over 10; redproof_wt179_manifest.py 26 of 26 tags; redproof_wt178_claims.py 17/17; redproof_wt180_counts.py 12 of 12; redproof-layout.sh RC 0 with 4 probes. defensive_count.py --against reads +0 on all four manuscripts and the LEVELS are unchanged at paper-I/II/III/IV = 0/0/3/0 outside Limitations -- ALL THREE IN-SCOPE MANUSCRIPTS WERE EDITED THIS PASS, 149 times, and the invariant held. wt148 reports 0 unadjudicated and 0 stale on all three in-scope manuscripts, after 16 promises were re-keyed with their evidence RE-RUN, 10 retired because the sentence naming the artefact WAS the apparatus leak Pass D was clearing, and one re-evidenced. Board 66 criteria with P7 the ONLY lane that moved, after bash scripts/regen-board.sh -- and it moved to CLOSED. THE LAYOUT BASELINE IS 145 PAGES: 149 before this pass, 144 after the C-class repairs took five pages of scaffolding out with nothing added, and 145 when the section 4.4 known-limitations note put one page back. Gate PASS, tree clean and pushed. THE PASS-D PATCH SCRIPTS (wt209 through wt219) ARE DELIBERATELY NOT REGISTERED CLAIMS: every one is idempotent and goes QUIET on a second run, and the wrap only ever runs a command a second time, so registering one would register a no-op. Each was run twice and its stdout diffed; they are named in the body of this file, not in the phase block."
gate_passed: true
gate_version: "2.61"
next_at_bat: "ASSIGNED, ONE THING -- PASS D of the ship plan: THE COHERENCE PASS, AND THE ONE THAT PRODUCES JASON'S INPUT. Read docs/DEFINITION-OF-DONE-SHIP.md section 3 Pass D; it wins over this line and the charter wins over it. Read docs/REVIEW-039-passC-structural-settlement.md before you plan -- its section 6 states what you inherit so you do not discover it. THE STRUCTURE IS SETTLED: Pass C repaired 24 items and no section will move under you. FIVE THINGS. (1) Clear the remaining C-class: 15 hard C-e, 61 C-b, 5 C-a = 81 repairs, and FLAG the 8 C-f without ever fixing them. (2) Read each manuscript end to end at thirty thousand feet, once, in one sitting, asking only whether it reads as one connected paper. (3) EMIT docs/FIGURE-PLAN.md -- THIS IS THE DELIVERABLE JASON'S LAYOUT WORK RUNS ON. The corpus carries ZERO figure captions and roughly 230 markdown table rows, 157 in paper-III, so the question is not where the charts go, it is which of these tables wants to be a picture and what it would show. YOU MAY PROPOSE CHART FORMS AND MUST NOT BUILD THEM. (4) EMIT docs/SHIP-STATEMENT.md per section 4.2. (5) Rebuild, verify layout, tag v1.0-preprint, close P7. THREE THINGS MAKE 81 SMALLER: C-b clusters -- half of paper-III's 32 are in its References section, so read that as ONE job; the HARD C-e is a delete-on-sight list of fifteen and paper-II has zero, while the other 53 are committed artefacts a reader can fetch and stripping them deletes the provenance promise the whole apparatus exists to keep; and C-g is ZERO across 23 tables with C-c done, so you have no anchor sentences to write. FORBIDDEN: building a new instrument (section 1.1 -- a false-positive reduction is a repair and IS allowed), re-scoring anything, touching C-f at all, and drawing any figure. YOUR SUCCESSOR IS JASON and his precondition is that he can open any manuscript, start rewriting at paragraph one in his own voice, and NEVER discover that a paragraph should not exist, sits in the wrong place, or is missing the chart that would carry it. Ask it in those words, per manuscript. Section 3.0 is a RATCHET, not a countdown: you may not stop because your number came up. P7 IS yours to close; do NOT close P13g, P9 or P8."
blockers: []
claims:
  - id: pytest
    cmd: python3 -m pytest -q
    rc: 0
    count: 1168
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
    count: 7
    count_re: ([0-9]+) of [0-9]+ rows verified
    note: DERIVED from what the run re-ran -- 11 live rows of fifteen, 3 retired to committed successors, 1 re-evidenced. The WRITING path exits 2 by design; --verify is the re-runnable mode
  - id: wt172 --verify
    cmd: python3 scripts/wt172_tsv.py --verify
    rc: 0
    count: 19
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
  - id: wt182
    cmd: python3 scripts/wt182_paperIV_p7pass3.py
    rc: 0
    count: 20
    count_re: post-conditions: ([0-9]+) checks
    note: the P7 pass 13 patch of record -- idempotent, so re-running it is a check and not a mutation
  - id: wt183
    cmd: python3 scripts/wt183_paperIV_promises.py
    rc: 0
    count: 16
    count_re: post-conditions: ([0-9]+) checks
    note: the eight-row re-adjudication wt182's edits forced -- also idempotent. Q10 was NARROWED at -102 from a whole-file #superseded constant to wt183's own six, because the constant went red on another session's correct edit
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
  - id: wt184
    cmd: python3 scripts/wt184_pointer_correctness.py --postconditions
    rc: 0
    count: 28
    count_re: post-conditions: ([0-9]+) checks
    note: A3' mechanised -- does the referent CARRY what the pointer says. 9 of the 28 are NEGATIVE and three of those failed on their first run, each on a real bug
  - id: wt185
    cmd: python3 scripts/wt185_paperIII_p7pass4.py
    rc: 0
    count: 19
    count_re: post-conditions: ([0-9]+) checks
    note: the P7 pass 4 patch of record. IDEMPOTENT by construction -- run it twice; the exactly-once post-conditions are the repair for a first cut that double-applied its inserting edit while fourteen green checks watched
  - id: wt186
    cmd: python3 scripts/wt186_paperIII_promises.py
    rc: 0
    count: 11
    count_re: ([0-9]+) post-conditions
    note: adjudicates the four promises wt185's §11 bullet emitted. Re-running after the rows exist prints the already-present line and exits 0 without writing
  - id: wt187
    cmd: python3 scripts/wt187_restatement_counts.py
    rc: 0
    count: 6
    count_re: ([0-9]+) post-conditions
    note: updates test_restatement_reach's declaration from the manuscript via the guard's own counting function. Idempotent; prints "updated (nothing)" on a second run
  - id: wt188
    cmd: python3 scripts/wt188_paperII_p7pass13.py
    rc: 0
    count: 63
    count_re: post-conditions: ([0-9]+) checks
    slow: true
    note: the patch of record for Paper II pass 13. About 3 min -- E5 runs 35 simulations at the reported T = 1200. Idempotent and AUDIBLE on the second run; without --apply it reports only
  - id: wt189
    cmd: python3 scripts/wt189_paperII_promises.py
    rc: 0
    count: 19
    count_re: ([0-9]+) post-conditions
    note: re-adjudicates the four promises section 7's repair moved. Re-running after the rows exist re-derives and VERIFIES them and prints the same summary line, so the count still moves if a check is deleted
  - id: wt190
    cmd: python3 scripts/wt190_ledger_row_pass13.py
    rc: 0
    count: 10
    count_re: ([0-9]+) post-conditions
    note: the p7-passes.tsv append as a script. Idempotent; the already-appended path re-runs every post-condition against the file on disk
  - id: wt191
    cmd: python3 scripts/wt191_ship_dod_wiring.py
    rc: 0
    count: 26
    count_re: post-conditions: ([0-9]+) checks
    note: wires Jason's ship DoD into done-criteria.tsv, HANDOFF's definition_of_done and POST-SHIP.md. Idempotent and AUDIBLE on the second run -- it re-verifies every wiring assertion against the files on disk rather than returning early
  - id: wt191b
    cmd: python3 scripts/wt191b_freeze_sha_repair.py
    rc: 0
    count: 11
    count_re: post-conditions: ([0-9]+) checks
    note: names both the freeze-declaring commit and the frozen tree state in POST-SHIP.md, DERIVED from git log on the DoD document rather than taken as literals, so the shas cannot drift
  - id: wt192
    cmd: python3 scripts/wt192_coherence_amendment.py
    rc: 0
    count: 25
    count_re: post-conditions: ([0-9]+) checks
    note: Jason's SECOND amendment -- the C-class (section 2.5), the ratchet replacing the -106 countdown (section 3.0), the fourth pass, the restated end product and FIGURE-PLAN.md, and loopholes L9-L11. Idempotent and audible; the section bodies live in /tmp/sec*.md per this repo's write-locally-then-put rule
  - id: wt192b
    cmd: python3 scripts/wt192b_board_amendment.py
    rc: 0
    count: 12
    count_re: post-conditions: ([0-9]+) checks
    note: carries the amendment onto the board's P7 criterion. Its B5/B5b pair caught the note CONTRADICTING ITSELF -- wt191 had written "a hard stop at -106" and appending "the -106 hard stop is GONE" left both in one cell, so the stale clause is REPLACED before the amendment is appended
  - id: wt192c
    cmd: python3 scripts/wt192c_dangling_refs.py
    rc: 0
    count: 13
    count_re: post-conditions: ([0-9]+) checks
    note: closes the dangling references the amendment left -- including the DoD's OWN loophole table, whose L6 row cited a section the amendment had deleted. Nothing went red and nothing could have; found by grepping for mentions of a deleted feature
drift_flags:
  - "A REPAIR PASS ON A GUARDED CORPUS IS TWO JOBS, AND THE SECOND ONE IS BIGGER THAN IT LOOKS. Nine SHIP-LIST repairs -- none of them large, three of them one clause -- reddened FOUR guards, minted TEN `wt148` promises that each needed their evidence RE-RUN before a row could honestly be written, retired two superseded rows, moved one `test_restatement_reach` declaration and pushed the layout baseline 145 -> 147 pages. THE RATIO IS THE LESSON: the manuscript edits took about a fifth of the pass. BUDGET THE APPARATUS AS THE WORK. And run every script you are about to NAME in a manuscript BEFORE you write the sentence -- seven of the ten new promises are commands, and every figure quoted inside a provenance bullet was grepped out of that command's real stdout first."
  - "SIXTH AND SEVENTH INSTANCES OF THE STANDING TELL, BOTH IN ONE PASS: THE GUARD WAS WRONG ABOUT THE FILE, NOT THE FILE WRONG. (a) `wt182` recognised its own landed repairs by EXACT LINE-WRAPPED STRINGS, so `SL-9` reflowing one paragraph made three intact repairs look absent and its `idempotent, so re-running it is a check` claim went red on a correct manuscript. Repaired by flattening whitespace on the ALREADY-APPLIED side ONLY -- flattening the pre-edit side too turned a SECOND, unrelated edit red, because an `old` string is very often a substring of its own `new` once the newlines go. (b) `wt185` asserted a GLOBAL COUNT (`section 11 carries exactly five Regenerate bullets`) as a proxy for the double-apply it exists to forbid; `SL-7` added four legitimately and the proxy churned. Repaired by asserting the bullets are DISTINCT, which catches a duplicate from ANY pass and is immune to honest growth. BOTH FIXES ARE A TIGHTER SUBJECT. Neither is a weaker assertion, and the counts (20 and 19) did not move."
  - "BACKTICKS IN A COMMIT MESSAGE SENT THROUGH `dx` ARE COMMAND-SUBSTITUTED BY DARWIN'S ZSH AND THE WORD VANISHES FROM THE LOG -- SILENTLY, BECAUSE THE COMMIT STILL SUCCEEDS. A message containing a backtick-quoted identifier inside a double-quoted `git commit -m` argument landed with that identifier replaced by nothing; the only signal was one stderr line the commit output buried. Same door as `$(...)` or `$VAR`. THE FIX IS THIS REPO'S OWN write-locally-then-put RULE ONE LEVEL UP: write the message to a file, `--put` it, `git commit -F`. VERIFY WITH `git log -1 --format=%B` BEFORE PUSHING -- amend is free until you push, and a garbled commit message is a small false statement in the permanent record. Banked global."
  - "`wc -w` IS LOCALE-DEPENDENT ON GNU COREUTILS AND LOCALE-**INDEPENDENT** ON MACOS, WHICH IS WHY `SL-6` COULD NOT BE REPRODUCED ON DARWIN AT ALL. Same bytes (md5 eb56ef67162df6db0fabf50819db78f0): GNU gives 7367 under `LC_ALL=C` and 7527 under `LC_ALL=C.UTF-8`; macOS gives 7527 under C, C.UTF-8 and en_US.UTF-8 alike. The defect was confirmed from the CLOUD side of the session. THE HALF THAT GENERALISES: a self-referential check this project runs on darwin can be green there and red for a reader on Linux, and the document is read by the reader. `-103`'s leaf was enriched in place rather than forked."
  - "A BEFORE/AFTER PAIR MUST ANCHOR **BOTH** ENDS, AND ANCHORING ONLY THE ONE THAT BURNED YOU LEAVES A GUARD THAT FIRES ON YOUR SUCCESSOR FOR DOING ITS JOB. `-102` was burned intra-session by a working-tree phrase count and anchored the BEFORE side of `wt188`'s pair to commit 73e1966 -- correctly -- while leaving the AFTER side reading the live `docs/HANDOFF.md`. Every successor is REQUIRED to rewrite that file, so the check was green for exactly ONE session and red forever after: `-103`'s handoff rewrite dropped the count 6 -> 3 and `--claims-all` went red on a check about `-102`'s own work. `wt192c` had the same shape in a second costume -- R7/R8/R10 assert the content of a completed MIGRATION of the handoff. THE TEST BEFORE REGISTERING ANY CLAIM: name the thing that could change this value for a reason unrelated to what it checks -- and DOCS/HANDOFF.MD ALWAYS CHANGES, BY DESIGN, EVERY SESSION. Both repaired at `-103`, both re-run twice byte-identical."
  - "A FLAT DEFECT COUNTER IS NOT EVIDENCE OF DIMINISHING RETURNS UNTIL THE DEFECTS ARE SCORED, and this project spent eight sessions assuming otherwise. Sixteen passes, seventy findings, a per-pass count flat in a 2-9 band -- and the score is 53 S1 / 16 S2 / ONE S3. The S1 share by thirds is 87.5%, 61.9%, 76.0%. A flat count of SEVERE findings and a flat count of nitpicks are opposite situations and they look identical on the counter. The score costs one session and it is the only thing that separates `the reviewers are thorough` from `the artefact is still broken`."
  - "ADJUDICATE A CHECKER'S WHOLE FLAG SET BEFORE TIGHTENING THE RULE, THEN DERIVE THE RULE FROM THE ADJUDICATION. `wt184` Rule 1's 44 flags resolved 2 TRUE / 42 FALSE, and the discriminator turned out to be GRAMMATICAL rather than a threshold: every TRUE flag is a POSSESSIVE (`section 4.4's 0.00789`) and every FALSE one is co-occurrence inside one paragraph. A rule requiring a possessive or a verb of attribution reproduces 2 of 44 and both are the true ones. Three sessions proposed narrowing this rule before anyone read its output; a rule tightened first deletes its own true positives and you never learn which."
  - "`wc -w` IS LOCALE-DEPENDENT ON GNU COREUTILS AND THE CORPUS SHIPS A SELF-REFERENTIAL WORD COUNT. Same bytes (md5 eb56ef67162df6db0fabf50819db78f0): LC_ALL=C gives 7367, LC_ALL=C.UTF-8 gives 7527, macOS `wc -w` gives 7527, Python `str.split()` gives 7527. Paper-IV calls that number `checkable` and names no command -- so `-100`'s repair from 7,400 to 7,500 FIXED IT FOR ONE READER AND BROKE IT FOR ANOTHER. SL-6. Any self-referential measurement must name its measuring command."
  - "FINDING IDS IN `docs/p7-passes.tsv` ARE NOT UNIQUE ACROSS THE LEDGER. Each pass restarts its own numbering, so `III-1` names three different findings (`-73`, `-83`, and `-101` which restarts at `III-5`) and `IV-1` names two (`-75`, `-81`). ALWAYS cite `<pass>/<id>`. Aggregating or de-duplicating by the bare id silently loses findings, and `-103` was the first pass to aggregate all seventy and the first to hit it."
  - "TWO OF `-103`'S OWN VERIFICATION CHECKS WENT RED AND BOTH TIMES THE CHECK WAS WRONG, NOT THE MANUSCRIPT -- the `-102` trap landing on the session auditing it. A literal-phrase grep failed because the manuscript is HARD-WRAPPED and the phrase spans a line break; another failed because the text carries markdown emphasis inside it (`reaches **k = 0.60**`). A check pinned to a line break or to `**` is pinned to a subject that moves for reasons unrelated to what it checks. Grep the CONCEPT, or strip emphasis and joins first."
  - "A COMMITTED SCRIPT A READER CAN FETCH IS NOT AN APPARATUS LEAK, AND COUNTING IT AS ONE WOULD HAVE PASS D DELETE THE CORPUS'S BEST FEATURE. The raw C-e sweep returned 68; the DoD section 2.5 repair clause says `or at a committed artefact the reader can actually fetch`, which a `scripts/wt###.py` named in a section Data-and-code of a paper shipping beside a public repo plainly is. Split by mechanical census: 15 HARD (session numbers, REVIEW docs, LEDGER ticket ids -- paper-II has ZERO) and 53 SOFT (fetchable but unglossed, a one-clause-at-first-use fix). REVIEW-038 section 4.1."
  - "A TEE-UP THAT NAMES THE MECHANISM TO COPY IS A CLAIM AND MUST BE RE-MEASURED BEFORE IT IS COPIED, BECAUSE A WRONG ONE IS WORSE THAN NO TEE-UP: it sends the successor looking for something that does not exist AND certifies as clean the thing it holds up as the model. `-101` wrote three times that `wt184` Rule 2 should copy `the possessive form Rule 1 already uses, which cut its own flag set from 44 to 5`. Rule 1 has NO possessive logic anywhere in the file, and its flag set was never cut to 5 -- 43 flags at `-101`'s own parent commit 74934b9 and 44 at HEAD, all forty-three unadjudicated while REVIEW-036 adjudicated Rule 2's three explicitly. What cut the count is an attribution WINDOW that fires only on markdown table rows. THE CHEAP GUARD: before acting on `X already does Y`, grep X for Y and re-run the number, in that order; and if the number is a before/after pair, reproduce BOTH ends at the commit that claimed them."
  - "A POST-CONDITION THAT ASSERTS A PRE-REPAIR STATE MUST READ THE BACKUP, NEVER THE LIVE FILE -- otherwise the check that PROVES the finding evaporates the instant the repair lands, and the patch script goes red on its own success. `wt188` asserted `section 7 says five quantities` against the live manuscript; the repair changed five to six and the check failed on the SECOND run, with the repair correctly applied. The second run is what caught it, which is the other half of `-101`'s rule: run every patch script twice AND DIFF THE STDOUT, because run two is the only run the wrap's `--claims-all` ever performs. Anchor every as-it-stood-before assertion to the .bak the script writes before its first edit, and keep a matching after-assertion on the live file."
  - "THREE CHECKS FAILED ON THEIR FIRST RUN THIS SESSION AND ALL THREE WERE WRONG ABOUT THE FILE RATHER THAN THE FILE BEING WRONG -- `-101`'s (iv), third witness, and every fix was a TIGHTER subject rather than a deleted check. (a) `wt188`'s negative control asserted the attribution window would MOVE paper-II's flag count; it does not move at all, because the window fires only on table rows and none of the eleven flagged clauses is one -- so the control was tightened into the stronger true statement, that the window is INERT on prose. (b) Two exactly-once checks counted a byte literal; the manuscript is hard-wrapped at ~100 columns and both replacements land a newline MID-PHRASE, so the fix was to count on whitespace-normalised text plus a NEGATIVE control asserting the byte-literal count misses one. (c) `wt189`'s uniqueness check counted a promise_id across the whole file, and a `#superseded` line legitimately names the NEW id in its third column -- fixed by counting among LIVE rows only. A guard that refuses and is wrong is still telling you something true about your model of the file."
  - "AN AXIS THAT RUNS 'THE MANUSCRIPT'S OWN NAMED COMMANDS' IS BOUNDED BY THE MANUSCRIPT'S HONESTY ABOUT ITS OWN TOOLCHAIN, AND THAT LOOP TOOK THREE PASSES TO CLOSE. A4 is DEFINED as running what the paper names, so a command the paper does not name is invisible to the axis BY CONSTRUCTION. `-73`, `-80` and `-83` each ran A4 correctly on paper-III and each stopped short of §4.10 -- the section whose title IS the paper's headline -- because §11 opens 'Every simulation result in §A.2 and §§2-3 is produced by open code', which is a FLOOR that three passes read as a CEILING. `scripts/wt091_lag_shape_identifiability.py` prints §4.10's whole table, is registered against REG-005, was committed 74 minutes after that registration, and QUOTES THE MANUSCRIPT in its own docstring. THE GENERAL MOVE, and it is the next A4 target on every manuscript: enumerate the sections that report a computed figure, enumerate the sections §Data-and-code covers, and READ THE DIFFERENCE. On paper-III that difference was §4, nine subsections long. This is `-100`'s IV-10 with a different cause -- not a missing artefact, a scope sentence -- and two witnesses make it a class."
  - "A POST-CONDITION THAT CANNOT FAIL ON A DOUBLE APPLICATION IS NOT A POST-CONDITION, AND AN INSERTING EDIT CANNOT USE ITS OWN ANCHOR AS AN IDEMPOTENCY TEST. `wt185`'s first cut appended a bullet after §A.2.3's bullet, so after a successful run THE ANCHOR WAS STILL PRESENT -- and `if new in text and old not in text` answered 'not yet run'. Its second run shipped the §11 bullet TWICE while ALL FOURTEEN of its post-conditions passed, because every one asked whether a string was PRESENT and none asked HOW MANY TIMES. Rolled back from a .bak taken before the first run. Every edit now carries an explicit MARKER unique to the applied state, plus an exactly-once check per edit and a count of the whole bullet list. RUN EVERY PATCH SCRIPT TWICE BEFORE YOU BELIEVE IT -- the second run is the test, and it costs nothing."
  - "A CHECKER THAT RETURNS ZERO ON A CORPUS THAT SHOULD HAVE EXERCISED IT IS A BUG REPORT ABOUT THE CHECKER, NOT A RESULT ABOUT THE CORPUS -- and `wt184` proved it three times in one hour. Its Rule 2 reported ZERO quoted phrases adjudicated on a 2,741-line manuscript that quotes constantly; the cause was that the manuscript is HARD-WRAPPED at ~100 columns, so a quotation opens on one line and closes two lines later, and a line-at-a-time clause splitter can never see one. Rule 1 flagged every section reference as a numeric claim, because `§2.1` matched the number matcher -- unfixed, all 244 of paper-III's references become findings. And a markdown table row is ONE clause across SIX cells, so §7's ledger rows paired a `§5.4` in one cell with unrelated figures in three others. ALL THREE were caught by the NEGATIVE CONTROL DOCUMENT on its first run, which is the second session running to bank the same lesson: a control you were sure of is not a control, and a control that fails immediately is doing its job."
  - "THE REVIEW LEDGER STOPPED AT `-83` AND FIFTEEN SESSIONS DID NOT NOTICE, BECAUSE EVERY ONE OF THEM WAS LOOKING AT THE BOARD. `docs/CHECKLIST.md` has read 57 CLOSED / 9 PENDING-HUMAN / ZERO OPEN for four sessions running, and each of `-95` `-96` `-97` `-98` read that, concluded correctly that no lane was open, and went to the infrastructure parking lot. THE BOARD IS NOT THE DEFINITION OF DONE. `definition_of_done` in this very front matter asks for three preprints at ready-to-submit AND convergence -- TWO CONSECUTIVE ZERO-FINDING P7 PASSES PER PAPER -- and `docs/p7-passes.tsv`, the ledger this project built so that exactly this claim would be measured rather than told, has its last row at `wealthTensor-83`. Paper II was last read at `-79`, paper-IV at `-81`, paper-III at `-83`. NO PAPER HAS EVER HAD A ZERO-FINDING PASS, so convergence is not one pass away for any of them; it is at minimum two per paper, six reads, and the counter has never gone below two. THE GENERAL SHAPE, and it is the expensive one: when a project has a board AND a definition of done, a session that consults only the board will find the board says nothing is open, and will build tools. Tools are cheap to justify and impossible to finish. CONSULT THE DoD FIRST; the board is a subset of it."
  - "A COUNT IS ONLY A MEASUREMENT IF SOMETHING CHEAP CAN MOVE IT, AND THAT IS WHY THE RED-PROOF COSTS SECONDS INSTEAD OF EIGHT MINUTES. The three claims closed here are guarded by four lualatex builds and fifteen re-executed evidence cells; a red-proof that had to RUN them to see whether their numbers move would be a red-proof that runs in no CI, no fresh clone and no container -- which is `-97`'s wt179 lesson pointed at its author's successor. So each number was given a CHEAP SEAM through which the real world can be moved: wt176 prints the pages it compared BEFORE the verdict branch (so a PDF one page short says 144 rather than losing the line to an early return); the probe tally lives in a sourced `probe-tally.sh` (so it can be driven with three verdicts or seven in milliseconds, and the REAL script can be run with its probe BODY stubbed to prove the wiring and with one call site deleted to prove the number falls); and `wt170 --verify` is importable, so the adjudication corpus can be handed a retirement in a temp file. WHAT THE SEAMS DO NOT PROVE is that the real commands print those lines on a real run -- only `--claims-all` at wrap proves that, and BOTH docstrings say so. Do not delete one half because the other is green."
  - "THE 25-SECOND BOARD TIMEOUT WAS STILL LIVE IN THE GATE ITSELF, WHICH IS THE HALF THAT MATTERS. `-96` measured `board.py`'s default `BOARD_CHECK_TIMEOUT` (25s) against P13e's criterion (`verify-layout.sh`, 16s idle -- a 1.6x margin), watched a CLOSED lane come back CANNOT VERIFY from concurrent load alone, and repaired `regen-board.sh`. It said in its own traps that `gate-selfcheck`'s board check was NOT covered, and that is the worse half: the gate runs at WRAP, at the exact moment this handoff tells you to background a twelve-minute `--claims-all`. `-97` fixed it at the artefact -- `gate-selfcheck.sh` now runs the board `--check` with `BOARD_CHECK_TIMEOUT` defaulted to 300 inside the command substitution's own subshell, so it neither leaks to the caller nor overrides an explicit value. Proven three ways: default 300, no leak, caller's 7 still wins. THE GENERAL SHAPE: when a wrapper is repaired and the CALLER is not, the hole moves to whoever did not read the wrapper -- fix every invocation of a shared engine, not the one you were standing in."
  - "THE MANIFEST NOW HAS A CHEAP GUARD AND IT DELIBERATELY DOES NOT REPLACE THE EXPENSIVE ONE. `scripts/wt179_manifest_guard.py` holds `LAYOUT-MANIFEST.json` to itself, to `FONTS.tsv` row for row, to the manuscripts on disk in both directions, to the committed PDF's bytes and to the commit it names -- 10 checks, 0.07s, standard library plus `git`. It CANNOT tell whether the manifest describes reality; only `verify-layout.sh`'s rebuild can, and both module docstrings say so. That division is the one `test_recipe_is_held_to_the_measurement.py` already documents for RECIPE.md, and the reason is the same: without the cheap half, the expensive half is the only half, which in practice means nothing runs in CI, in a fresh clone, or in the container. If you change the manifest you must still run BOTH."
  - "THE BOARD'S CHECK TIMEOUT WAS A KNIFE EDGE AND IT DOWNGRADED A CLOSED LANE UNDER LOAD. `board.py` runs every `cmd:` criterion under `BOARD_CHECK_TIMEOUT`, default 25s. P13e's criterion IS `bash docs/deliverable/verify-layout.sh`, and that takes 16s on an idle darwin -- a 1.6x margin. `-96` regenerated the board while its own `--claims-all` was rebuilding the deliverable in another process, and P13e came back CANNOT VERIFY, `check timed out after 25s`: a CLOSED lane downgraded, in COMMITTED state, by nothing but concurrent load. The condition that trips it is the workflow THIS FILE RECOMMENDS -- background the long builds and poll. Fixed where the artefact is: `scripts/regen-board.sh` now exports `BOARD_CHECK_TIMEOUT=300` unless the caller sets one, which is the same repair `-53` made for the missing flags and for the same reason. Proven: regenerated on a quiet machine, the board comes back BYTE-IDENTICAL to the committed one. TWO RULES FOLLOW. ALWAYS `git diff docs/CHECKLIST.md` before committing a regeneration -- `-96` caught this only by diffing. And do NOT regenerate the board while a build is running; a status derived under load is a measurement of your machine, not of the project."
  - "THE HANDOFF'S CLAIMS ARE NOW A MACHINE-READABLE REGISTRY AND THE GATE RE-RUNS THEM. The frontmatter carries a `claims:` block (id / cmd / rc / count / count_re / slow / note) and `python3 scripts/handoff_gate.py --claims-all` re-runs every entry UN-PIPED before the wrap. `--claims` alone skips the ones marked slow and exits 2, because an un-run claim is not a verified one. TWO THINGS A SUCCESSOR MUST KNOW. (a) `--emit` enforces only the STATIC half -- that every RC or count the `phase:` prose asserts is DECLARED by a claim -- because re-running the sweeps inside `--emit` would double the cost of every wrap and a slow gate is a switched-off gate. THE RE-RUN IS A STEP YOU TAKE, and the wrap order names it. (b) The prose is read as an AUDIT of the registry, never as the work list: an assertion no claim declares turns the leg RED (UNREGISTERED-CLAIM) instead of quietly shrinking what gets run. If you add a sweep to `phase:`, declare it, or the gate will tell you exactly what to paste."
  - "AN EXIT CODE IS THE WEAKEST HALF OF A CLAIM, AND THIS WAS PROVEN LIVE RATHER THAN ARGUED. `-96` added 27 tests, and its own registry still said `pytest` 1121. The RC stayed 0 through every run -- the pipe defect that started this whole card would have reported GREEN -- and only the COUNT moved, 1121 to 1148. The leg re-ran it three times and then refused it. SO: when you register a claim, register a COUNT wherever the command prints one, with a `count_re` that captures exactly one group. Three of the nineteen claims print no number to hold them to (`verify-layout.sh`, `redproof-layout.sh`, `wt170 --verify`) and their `note` says so out loud; making those printable is free value for whoever needs it."
  - "A MANIFEST OVER AN EMPTY SET MUST CARRY AN EXPLICIT SENTINEL ROW UNDER GUARD, NOT ZERO ROWS. `docs/deliverable/FIGURES.tsv` lists figure -> script -> source, and the corpus has no figures, so `every figure is listed` is satisfied VACUOUSLY -- the row closes and reopens in silence the day someone pastes in a chart. The working shape, and it generalises to any manifest over an empty set: a named sentinel (`@zero-figures`) that names a real committed script and a real committed source so the criterion's `test -f` stays honest, plus a guard that refuses to let the sentinel coexist with a real member (SENTINEL-WITH-FIGURES) and refuses to let it be deleted while the count is still zero (SENTINEL-MISSING). The count itself is measured FIVE ways -- the narrow grep, an eight-pattern sweep that catches mid-line images the `^!\\[` anchor walks past, zero image files tracked repo-wide, zero image XObjects in the 147-page PDF, and `preamble.tex` not loading graphicx at all."
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
  - "THE `#scope` LINE IN `docs/promises-adjudicated.tsv` STILL EXCLUDES `paper-I`, so its 13 promises print and do not gate. That is a deliberate scope line and `wt170`'s N27 FAILS THE RUN if a session widens it. Named here so no later pass reads the sweep's own output as a defect. Widening costs 13 rows of re-run evidence and belongs after the ship, if ever."
  - "A LOCALE-PINNING GUARD: every command a manuscript names as checkable could be required to carry its locale, and a test could assert that any `wc`/`sort`/`uniq` a manuscript names is written with one. `SL-6` is the only known instance; the guard is the general form. NEW INSTRUMENT -- section 1.1 forbids it until the corpus ships. In POST-SHIP.md."
  - "`wt133` SWEEP 2 ANSWERS *is this entry cited anywhere*, NOT *is it cited at the sentence that relies on it* -- which is the actual `IV-7`/`SL-8` standard, applied by hand both times. A per-section reachability sweep is the instrument that would mechanise it. In POST-SHIP.md; new instrument."
  - "`wt184` FALSE-POSITIVE REDUCTION, SPEC WRITTEN AND MEASURED, DELIBERATELY NOT BUILT (DoD section 1.1 permits the repair; `-103` had no mandate). Three changes, all reductions: require an attribution token (possessive or verb) instead of paragraph co-occurrence; exclude `[A-Z]{2,}-\\d{3}` and `wealthTensor-\\d+` before harvesting numerals; extend FOREIGN to `<DOC-ID> section N.M`. Measured against a COMPLETE adjudication of all 44 flags, the proposed rule returns 2 and both are the TRUE ones. SM 1217774684736450, REVIEW-038 section 3.3."
  - "THE C-CLASS SOFT TAIL -- 53 unglossed but fetchable pointers (`PRE-`/`REG-`/`RESULT-` codes, commit hashes, `docs/` paths, `scripts/wt###.py`). NOT a leak, a GLOSS problem: one clause at first use. Pass D owns the HARD 15; this tail can wait for Jason's own rewrite, which is where voice decisions belong. Census in REVIEW-038 section 4.1."
  - "`wt188`: sharpen `wt184` Rule 2 -- it currently accepts a quotation and a §N.M pointer CO-OCCURRING in one sentence as attribution, so all three of its paper-III flags are false positives (two are objections the paper quotes and answers, one is Bleck and Liu's phrase attributed to Bleck and Liu). The fix is a verb list (says / states / puts it / calls it / reads) or the possessive form Rule 1 already uses, which cut its own flag set from 44 to 5. Needs a NEGATIVE control in each direction."
  - "`wt192` (RENAMED at `-102`: `wt189` and `wt190` were taken by the pass-13 patch scripts): THE SCOPE-SENTENCE SWEEP. Enumerate the sections of a manuscript that report a computed figure; enumerate the sections its §Data-and-code covers; the difference is the unchecked set. This is the generalisation of BOTH `-100`'s IV-10 and `-101`'s III-6 and it is the one instrument that would have caught either without a human noticing first."
  - "Point `wt184` at paper-I. It has read paper-III only; paper-II and paper-IV are folded into the next two P7 at-bats, and paper-I is out of promise scope but not out of pointer scope."
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
definition_of_done: "SEE docs/DEFINITION-OF-DONE-SHIP.md — IT IS THE SSOT AND IT WINS OVER THIS LINE. THE END PRODUCT IS NOT A CORRECT MANUSCRIPT; IT IS A MANUSCRIPT JASON CAN REWRITE FROM WITHOUT A FALSE START, which is a higher bar. Three preprints (II, III, IV) STRUCTURALLY FINAL: zero OPEN S1 and zero OPEN S2 on the frozen docs/SHIP-LIST.md, zero open C-class (section 2.5 -- antithesis residue, scaffolding voice, orphans, fold problems, apparatus leaks, unplaced evidence; register drift is FLAGGED not fixed, because re-voicing is JASON'S pass), no section that will move again, every table carrying an anchor sentence, docs/FIGURE-PLAN.md and docs/SHIP-STATEMENT.md written, Jason's own-hand rewrite then his to do. THE CONVERGENCE CLAUSE (two consecutive zero-finding passes per paper) WAS RETIRED at -102 after sixteen passes produced zero zeros -- no termination proof, and it rewarded not looking. NO SESSION MAY STOP BECAUSE ITS NUMBER CAME UP: section 3.0 is a RATCHET -- every pass owns its SUCCESSOR'S preconditions and closes when the next pass can start AND finish. Jason rules only when the ratchet stalls TWICE ON THE SAME precondition; a single stall is just work and costs one session."
# wealth-tensor — HANDOFF
**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**
*Stamped by `scripts/handoff_gate.py --stamp`. If `gh_sha` above is not `HEAD`, this file was
committed without stamping — read `git log` rather than believing it.*

# ⛳ THE CORPUS SHIPPED. THE SUCCESSOR IS JASON, NOT A SESSION.

**`v1.0-preprint` is tagged. `P7` is CLOSED — on a check that bites, not on an assertion.** The
four-pass plan in `docs/DEFINITION-OF-DONE-SHIP.md` is complete: Pass A made the end countable,
Pass B cleared the truth list, Pass C settled the structure, and Pass D (`-106`) cleared the
coherence class and produced the two documents the next hours run on.

**THIS FILE IS NO LONGER ADDRESSED TO A CLAUDE.** The at-bat that remains is a human rewrite, and
the § below called **WHAT JASON OPENS FIRST** is the whole of the instruction. A session arriving
here should read that § too, understand that **it is not their at-bat**, and go read `P11`, `P9`
or `P8` on the board instead — none of which Pass D was entitled to touch.

---

---

## STEP 0 · transport (zero bridge calls)

The bridge rotates every ~27–33 min (`claude-code#81248`). **DARLISH DOES NOT USE IT.** Asana /
Gmail / Twilio MCP tools ARE bridge-bound — if one vanishes mid-turn it self-heals in ~1 s, retry
next turn, NEVER declare "can't continue" over it. Never restart the Claude app for a darlish
problem.

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
# post the printed DARLISH-ENROLL line, EXACTLY, as an Asana comment on task 1217316841710435
/tmp/darlish-up
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-106 --task "Pass D: the coherence pass"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-106 --resource ~/repos/wealth-tensor --task "Pass D"'
/tmp/dx '~/Scripts/rail'                                # check before you swing
/tmp/dx '~/Scripts/charter-read.sh wealthTensor-106'    # YOUR id, not your successor's
/tmp/dx 'python3 ~/repos/claude-blackbook/lessons.py search "scaffolding voice antithesis residue coherence figure plan" --scope global,wealth-tensor'
```

READY first try at `-61` through `-105` — **FORTY-FIVE for forty-five.** Budget four minutes; it
takes two.

⚠ `roster claim` needs `--resource` (a NAMED flag), not `--repo`. When a SIBLING has staged work in
a shared repo the clean exit is `git commit --only <your path>`, NOT `ROSTER_BRAKE_ACK`.

⚠ `--put` PATHS MUST BE QUOTED: `dx --put '~/path'`. Unquoted, your local shell expands `~` to
`/root` and dx refuses before bytes move.

⚠ **RUN THE GATE AS `GATE_ROSTER_WHO=big-wealthTensor-106 bash ~/Scripts/gate-selfcheck.sh`.**

⚠ **BACKTICKS IN A `git commit -m` MESSAGE SENT THROUGH `dx` ARE COMMAND-SUBSTITUTED BY DARWIN'S
ZSH.** The word disappears and the commit still succeeds. Write the message to a local file,
`--put` it, `git commit -F` it, read it back with `git log -1 --format=%B`. **`-105` avoided this
by writing commit messages with NO backticks at all** — cheaper than remembering the rule.

⚠ **A THREE-SHELL QUOTING CHAIN (cloud bash → dx → darwin zsh → python heredoc) WILL EAT YOUR
PATCH.** `-105` lost two round trips to it. **Write the patch to a local file, `--put` it into
`scripts/`, and run it by name.** Every non-trivial edit this session was made that way.

---


## 📖 WHAT JASON OPENS FIRST, AND WHAT HE FINDS THERE

**Open `docs/FIGURE-PLAN.md`. Not a manuscript.**

Here is why, and it is a claim about the shape of the work rather than about the documents. The
three manuscripts are structurally final: you can start rewriting at paragraph one of any of them
and you will not hit a paragraph that should not exist or one that sits in the wrong place. **What
you WILL hit, repeatedly, is a table that should have been a picture** — twenty-three of them, and
the corpus carries **zero figure captions.** If you start at paragraph one you will make that
discovery on your own, at whatever page it first bites, and you will make it again on the next
page, and the decisions will accumulate as interruptions to the writing instead of as a pass of
their own.

`FIGURE-PLAN.md` is that pass, done in advance. **29 rows: one per table, one per proposed
figure, six columns each.** For every table it names the sentence that fails without it, the
earliest point a reader can read it, whether an argument breaks without it, and either
`TABLE — stays a table` with the reason or the shape it wants and why that shape. **Nothing is
drawn** — § 4.3 of the DoD says the plan is the deliverable and the drawing is yours, and that
ruling is restated at the foot of the file so you can overrule it.

**The three things in it worth knowing before you open anything else:**

1. **Two figures carry a paper's title claim and have neither a table nor a picture today.**
   `NEW-F3` is paper-III's sharpest statement — *a factor of 1.67 in the unobserved physical scale
   spans the entire unit interval of timeliness* — and `NEW-F5` is paper-II's title, currently
   carried by one sentence. **If only two things ever get drawn, draw those.**
2. **The single largest table should not be drawn at all.** § 7's survivals ledger is fifty rows of
   heterogeneous outcomes with a full sentence per row. Its problem is *pagination*, not
   visualisation, and § 3 of the plan says so along with five other tables that would be worse as
   pictures. **That negative list will save you more time than the positive one.**
3. **`III-T19` is the strongest conversion in the corpus.** § A.2.4 claims λ *is a sawtooth* — a
   statement about a shape — and supports it with five summary statistics, which is the worst
   available way to assert a shape. The series exists; `wt002_lambda_report.py` prints it.

**Then open `docs/SHIP-STATEMENT.md` § 6, and only § 6.** It is two pages of what is
known-imperfect and shipping anyway: the two S3s, the ten flagged register-drift sites, the
fifty-three soft apparatus references left unglossed on purpose, the one structural judgement call
that is yours to overrule, and the fact that **the framework has no confirmed empirical claim** —
which paper-III § 6.1 states at full length and which nothing in the review apparatus softens.

**Then start writing, in any of the three.** The voice is deliberately NOT harmonised. **Seven
sites carrying FIVE decisions** are in `docs/REVIEW-040.md` § 2, each one naming what the two
registers are and naming no winner — **no repair is proposed for any of them**, because re-voicing
is your pass and a session that does it has spent your hours for you and probably lost something.

**The list arrived at ten and the triage that produced seven was itself audited**: a verifier
overturned six of ten verdicts, three flags came off with controls that were checked rather than
asserted, and **two of the seven are sites nobody had seen** — one of them because this pass
flattened one half of a matched pair of appendix headnotes and never looked at the other.
**Decision A is the one to take first**: it is a single second-person tic at two sites, in two
different papers, and settling it once settles both.

---

## 🧾 WHAT PASS D ACTUALLY DID, IN FIVE LINES


## 🩹 ONE CORRECTION LANDED AFTER THE FIRST TAG, AND IT IS THE MOST INSTRUCTIVE THING HERE

**The corpus shipped with a broken sentence in it.** paper-IV § 3 read *"a confiscatory levy on
flow **is / leaves** the wealth vector exactly unchanged"* — a stranded copula, left behind when a
late correction replaced the predicate and not the verb before it.

**It passed 1,168 tests, thirty green guards, forty-one re-run claims, a page-for-page layout
reproduction, and two adversarial verifiers.** A third verifier, reading for something else
entirely, happened on it.

**THE GAP IS NOT THAT THE APPARATUS IS WEAK — IT IS THAT A LATE CORRECTION ROUND INHERITS NONE OF
THE VERIFICATION OF THE ROUND IT CORRECTS.** Both adversarial sweeps and the mechanical stitch
check were run over the first 166 repairs and none over the corrections that followed them. If you
take one process lesson from this session, take that one: **the last edits are the least checked
edits, and they are the ones that ship.**

Repaired at `wt220`, with a second milder instance beside it; the tag was moved onto the repair and
the move is recorded in the tag's own message. `SHIP-STATEMENT.md` § 6.6 carries it as the sharpest
instance of **nothing in this repository reads English**.

* **149 C-class repairs** landed across the three manuscripts — 129 scaffolding voice, 15 hard
  apparatus leaks at 9 sites, 4 antithesis residues, and 7 S1s found and repaired in-pass.
* **The corpus lost five pages and gained one back.** 149 → 144 with nothing added; 144 → 145 when
  the § 4.4 known-limitations note went in. **Five pages is the honest measure of how much of this
  corpus was seam rather than argument.**
* **An adversarial verifier refuted forty of the first 166 repairs** — seven of them false
  statements that every mechanical checker passed. All forty adjudicated: 23 reverted, 17 rewritten.
* **Reading the three manuscripts against each other found nine more defects in 61 cross-document
  claims** — a class no per-file verifier can see, and one this pass had itself created.
* **`docs/FIGURE-PLAN.md`, `docs/SHIP-STATEMENT.md` and `docs/REVIEW-040.md` are written**, the
  deliverable is rebuilt and layout-verified at 145 pages, `v1.0-preprint` is tagged and `P7` is
  closed.

---

## 🔴 THE THREE THINGS A FUTURE SESSION MUST NOT GET WRONG

**1 · `C-f` IS FLAGGED, NEVER FIXED, AND THAT IS PERMANENT.** Ten sites in `REVIEW-040` § 2. A
session that "harmonises the voice" is doing damage that looks like help. This is the one line in
the whole plan whose violation costs Jason something he cannot get back.

**2 · A REPAIRING PASS CANNOT VERIFY ITSELF, AND THE RATE IS NOW MEASURED TWICE.** Pass C: ten
defects in twenty-four repairs. Pass D: forty in 166. **Same rate, six times the volume.** If you
repair anything in this corpus, hand a fresh verifier your repair list AND both versions of the
text and tell it to REFUTE, defaulting to "problem" when uncertain. And the tell that predicts
which repairs are wrong: **a coherence repair should be a deletion plus a stitch, so when the
replacement is the same length as the original it is probably a re-voicing wearing a repair's
clothes.** Every one of Pass D's eleven overreaches had that shape.

**3 · WHEN THREE DOCUMENTS SHIP AS ONE CORPUS, VERIFY THEM AGAINST EACH OTHER.** paper-III claimed
its abandonments section sits in the body *"for the reason Papers I, II and IV each state at the
head of theirs"* — and Pass D had just cut that reason from paper-IV. Eight more of the same class
followed: an exhaustive *"the two tests that exist"* that a sibling contradicts in as many words, κ
called a *mechanism* where paper-II is explicit it is *a budget and not a mechanism*, and **P2**
restated without the qualifier paper-III uses to demonstrate its deniability. **The sweep is cheap:
grep every manuscript for references to the others, open the cited passage, check it still says
what the citing sentence claims.** No instrument in this repository does it.

---

## 🟢 THE STATE — every line RE-RUN by `--claims-all`, not quoted

🟢 `pytest` **1168 passed** · `--claims-all` **41 agreed, 0 FLAKY, 0 FALSE**
🟢 **`v1.0-preprint` TAGGED** · **`P7` CLOSED**, and the check **bites**: it returns 0 today and
   returns 1 the moment the tag is taken away — proven, not asserted
🟢 **HARD `C-e` IS ZERO** across all three manuscripts. One grep proves it: no session number, no
   `REVIEW` doc, no `LEDGER.md`, no `WT-0NN` id survives anywhere in the corpus
🟢 **145 pages**, all 145 per-page text hashes reproducing from a clean worktree · 0 overfull
   boxes · 0 missing characters · every page clearing all four edges by ≥ 18bp
🟢 `defensive_count --against` **+0 on every manuscript**; levels unchanged at 0/0/3/0 outside
   Limitations. **G-COACH-3 held across a pass that edited all three, 149 times.**
🟢 `wt148` **0 unadjudicated, 0 stale**. 16 promises re-keyed with evidence RE-RUN, 10 retired
   because the sentence naming the artefact **was** the leak, 1 re-evidenced
🟢 `wt173 --verify` 50 values held, 0 divergent, 15 of 15 in the prose, after a `--measure`;
   `RECIPE.md` moved at **both** sites, 65.43 → 64.95, inside the 62–68 band, **nothing retuned**
🟢 Board 66 criteria, **`P7` the only lane that moved** — and it moved to CLOSED
🟢 gate: `~/repos/wealth-tensor` ok, tree clean, pushed
🟡 **THE GATE MAY STILL END ON A FAIL THAT IS NOT THIS REPO'S.** `claude-blackbook` carried six of
   a sibling's staged leaves at `-105`; `G-H#22c` attributes by filename rather than by the leaf's
   own `contributor:` field. **Carded SM 1217804787201829. Do NOT commit a sibling's staged work to
   go green.** Also live: `G-T#44` n8n-spine crontab drift, SM 1217795659362669.

---

## 🧰 THE INSTRUMENTS THAT MOVED, AND WHY EACH WAS ALLOWED TO

**Four instrument changes in the whole ship, and every one is a FALSE-POSITIVE REDUCTION under
DoD § 1.1's narrow exception, with the reading written at the pin.** None makes an instrument look
at anything new.

* `wt186` refused on a pid `wt148` no longer emits, because Pass D deleted the sentence that made
  the promise. It now honours the ledger's `#retired` convention as `wt170` already honours
  `#superseded`.
* `wt188` pinned the corrected Bouchaud–Mézard credit at **exactly two** occurrences. Two was the
  number of *sites that restated it*, never the finding — and `REVIEW-039` § 7 hands that
  restatement to Pass D **by name**. Re-asserted as at-least-one with the count printed.
* `wt191` C6 and `wt192b` B10 asserted *"P7 is still manual"*, true only while the plan was
  running. **A guard that fires when the plan's last step executes is asserting the plan will never
  finish.** Widened to the wiring claim they were always about.

**AND ONE OF THOSE GUARDS DID NOT ONLY CHECK — IT WROTE.** `wt192b` re-appends its amendment
paragraph whenever that paragraph is absent from `P7`'s fourth column, so the first `--claims-all`
after the closure **appended 900 words of prose onto the end of a shell command.** Caught by the
claim re-runner, which is the run that matters. The repair is one character of insight: a `cmd:`
criterion runs through `bash -c`, so the narrative survives as a **trailing shell comment** — the
check runs, every string the guards grep for is still in the row, and nothing is deleted.

**AND TWICE A GUARD WAS RIGHT AND PASS D WAS WRONG.** `TERM-002` binds § 8's class numeral to the
length of the list it counts, at two remote sites kept in sync. One Pass D repair changed the
construction; another **deleted one of the two sites**. Both reverted. **That is `SL-9` running
backwards — not a repair landing at one of two sites, but a repair *un-landing* at one of two —
and it is why a guard that looks pedantic gets to stay.**

---

## ⚠ THE TRAPS THAT ARE STILL LIVE

⚠ **`board.py` treats `manual:` as NEVER auto-closing.** A lane whose check is `manual:` can never
render CLOSED however true its criterion becomes, and editing the prose does nothing. To close one,
convert the fourth column to a `cmd:` check and **prove it bites** by breaking a condition.
⚠ **A THREE-SHELL QUOTING CHAIN (cloud bash → dx → zsh → python heredoc) WILL EAT YOUR PATCH.**
Write the patch to a local file, `--put` it into `scripts/`, run it by name. Every non-trivial edit
in this session was made that way, and the two that were not both failed.
⚠ **NEVER `re.sub` A FRONTMATTER WITH `re.S` AND `.*$`.** `.` then matches newlines and the
replacement swallows the file to EOF. A frontmatter is a list of lines; edit it as one. Caught by
an assert before anything was written, at `-106`, which is the only reason this file still exists.
⚠ **`*_edits_*.py` SCRIPTS ARE NOT IDEMPOTENT AGAINST AN EDITED `NEW`** — they insert a second
copy. Edit the constant → repair the file directly.
⚠ **RUN EVERY PATCH SCRIPT TWICE AND DIFF THE STDOUT.** `echo $?` after a pipe is the PIPE's code.
⚠ **THE BUILD STAMPS FROM A COMMIT** — commit every manuscript edit BEFORE you build.
⚠ **`git diff docs/CHECKLIST.md` before committing it**; regenerate with `bash scripts/regen-board.sh`,
NEVER `board.py`, and never while anything is building.
⚠ **FINDING IDS ARE NOT UNIQUE**: `III-1` names three, `IV-1` two. Cite `<pass>/<id>`.
▲ darwin is macOS + zsh: no `grep -P`, no `cat -A`, and **an unquoted `$var` does not word-split**
— `for c in $list` iterates once over the whole string. Use `${=c}` or write a script file.

---

## 📋 WHAT IS LEFT, AND NONE OF IT IS PASS D'S

**`P7` was Pass D's to close and it is closed. `P11`, `P9` and `P8` are NOT** — they were named as
Jason's in the brief that opened this session and nothing here changes that.

* **`P11`** — the corpus audited AS A WHOLE. `ADR-001`'s batch ruling says the conjunction gets
  exactly ONE first end-to-end pass, and it is unclaimed since 2026-08-11. **`P8` waits on it.**
* **`P9` / `P8`** — Jason's own-hand pass. That is the rewrite `FIGURE-PLAN.md` exists to serve.
* **`P2`, `P5`, `P6`** — ready-to-submit judgements, deliberately manual.

**And three instruments worth building, all blocked by § 1.1 until the corpus shipped — which, as
of this file, it has.** They are in `POST-SHIP.md` and they are now unblocked:
1. **A first-contact sweep.** Nothing in this repository measures where a reader FIRST meets a
   value. Pass C repaired a fold a hundred lines below the table that introduces the term, and
   every checker stayed green.
2. **A cross-manuscript consistency sweep.** Pass D found nine defects by hand; the sweep that
   found them was a one-off, not an instrument.
3. **A per-section reference-reachability sweep**, and a locale-pinning guard.

---

## 🔁 THE WRAP ORDER (unchanged, and it worked)

commit → `GATE_ROSTER_WHO=<you> bash ~/Scripts/gate-selfcheck.sh` → `--claims-all` (12–14 min,
**AFTER** your last mutation) → `gate_passed: true` → `--stamp` → commit ONLY `docs/HANDOFF.md` →
push → `charter-read.sh <you>` → gate → `--emit` → `roster leave --who`.
⚠ `--stamp` BEFORE the final commit means `gh_sha` lags; `--check` returns RC 1 until you stamp.
