---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: a75b15e2aa51e3063173e276d252547fa0c29f0e
updated: 2026-08-24
session: wealthTensor-103
session_n: 103
live_theme: "THE COUNTER WAS FLAT AND EVERYBODY READ IT AS DIMINISHING RETURNS. IT WAS NOT. -103 scored all seventy findings from all sixteen passes against the rubric -102 committed BEFORE any scoring, and the answer is the one nobody expected: 53 are S1 -- the paper stating something FALSE -- 16 are S2, and exactly ONE in seventy is S3. The S1 share by thirds runs 87.5%, 61.9%, 76.0%: SEVERITY NEVER DECAYED EITHER. Six handoffs had explained the flat 2-9 band as the passes scraping the barrel; there was no barrel-scraping and there was no S3 tail, because the S3 tail does not exist. That vindicates Jason's ruling on a stronger ground than it was made on -- a stopping rule waiting for a zero was pointed at a stream that never degraded. AND IT EXPLAINS THE AMENDMENT PERFECTLY: sixteen passes hunting truth found truth defects at a 76% clip and walked past 156 C-class seams, because every seam is a TRUE statement. Sections 2 and 2.5 are not two halves of one instrument. They are two instruments, and only one of them had ever been run."
phase: "EVERY NUMBER HERE WAS RE-DERIVED BY THE GATE'S CLAIM RE-RUNNER, NOT QUOTED: `pytest` 1168 passed; `wt184` RC 0 over 28 post-conditions with 9 NEGATIVE; `wt188` RC 0 over 63 with 20 NEGATIVE; `wt189` RC 0 over 19 with 11 NEGATIVE; `wt190` RC 0 over 10 with 4 NEGATIVE; `wt191` RC 0 over 26 with 12 NEGATIVE; `wt191b` RC 0 over 11 with 5 NEGATIVE; `wt192` RC 0 over 25 with 11 NEGATIVE; `wt192b` RC 0 over 12 with 6 NEGATIVE; `wt192c` RC 0 over 13 with 8 NEGATIVE; `wt185` RC 0 over 19 with 8 NEGATIVE; `wt186` RC 0 over 11 with 8 NEGATIVE; `wt187` RC 0 over 6 with 4 NEGATIVE; `wt182` RC 0 over 20 with 6 NEGATIVE; `wt183` RC 0 over 16 with 4 NEGATIVE; `wt181 --verify` RC 0 over 9 checks; `verify-layout.sh` RC 0 with 145 pages compared; `redproof-layout.sh` RC 0 with 4 probes reported; `wt170 --verify` RC 0 with 11 of 15 rows verified; `redproof_wt180_counts.py` RC 0 over 12 of 12; `wt173 --verify` RC 0; `wt173 --postconditions` RC 0 over 14 checks with 5 NEGATIVE; `preflight` RC 0 over 16 fonts; `wt133` `wt148` `wt154` `wt156` `wt160` `wt163` `wt166` `wt169` -- ALL EIGHT RC 0; `wt172 --verify` RC 0 over 19 paper-II rows; `wt177_figure_guard.py` RC 0; `redproof_wt177_figures.py` 21/21; `wt179_manifest_guard.py` RC 0 over 10 checks; `redproof_wt179_manifest.py` 26 of 26 tags; `redproof_wt178_claims.py` 17/17; `defensive` paper-I/II/III/IV = 0/0/3/0 outside Limitations -- UNCHANGED, and NO MANUSCRIPT WAS TOUCHED THIS PASS, which is the point of Pass A; board 66 criteria BYTE-IDENTICAL after regeneration (Pass A closed no lane, so an empty diff is the correct result); gate v2.61 PASS, tree clean and pushed. NEW DOCUMENTS, none of them a manuscript edit: `docs/SHIP-LIST.md` (CLOSED, 9 entries), `docs/REVIEW-038-passA-retrospective-scoring.md`, and `docs/POST-SHIP.md` extended with the triage. NO p7-passes.tsv ROW WAS ADDED and that is deliberate -- Pass A is not an independent read and claiming a seventeenth would be false."
gate_passed: true
gate_version: "2.61"
next_at_bat: "ASSIGNED, ONE THING -- **PASS B of the ship plan: CLEAR THE TRUTH LIST.** `docs/SHIP-LIST.md` is CLOSED and FROZEN at nine entries -- six S1, three S2 -- and every entry names its repair. READ `docs/DEFINITION-OF-DONE-SHIP.md` FIRST (it wins over every file but the charter); your at-bat is its Pass B, section 3. REPAIR ALL NINE in the charter's order -- STEELMAN, REPLACE, CUT, TEE-UP -- and NEVER ABSORB as manuscript hedging. **NO NEW LOOKING.** You are not a review pass; you are a repair pass working a closed list, and section 1.2 means a finding you discover goes to docs/POST-SHIP.md, not onto the list. THE ONE PERMITTED GROWTH: if a repair reveals an adjacent S1 AT THE SITE YOU ARE REPAIRING, repair it and append it, logged with the repair that surfaced it. FOUR THINGS THAT MAKE THIS SMALLER THAN NINE SOUNDS. (1) SL-3, SL-4 and SL-5 are ONE repair repeated -- three stale version stamps, 21 / 36 / 19 commits past their own dates -- and a single written Jason ruling closes all three if he would rather own version numbering himself. (2) SL-8 and SL-7 each have a LANDED PRECEDENT IN THIS CORPUS to copy rather than invent: SL-8 is -81's IV-7 repair (cite it at the sentence that relies on it, or cut the entry), and SL-7's honest-disclosure form is already written in paper-III section 11's own section 5.3 bullet. (3) SL-1 and SL-2 are ATTRIBUTION changes, not number changes -- the arithmetic in both sentences was checked at -103 and is correct; re-point, do not recompute. (4) SL-6 must NOT be repaired by restating the number: name the command AND its locale, because `wc -w` gives 7367 under LC_ALL=C and 7527 under a UTF-8 locale on the same bytes, and a bare corrected figure just re-creates the defect for the next reader. RUN `defensive_count.py --against` ON EVERY MANUSCRIPT AND SHOW +0; SL-3's revision-history line is the one repair on this list with a real chance of raising the count, so write it as a claim about the work rather than a hedge. DONE WHEN: every ship-list entry is marked repaired with its commit, `defensive_count --against` is +0 on all three manuscripts, `pytest` is green, `--claims-all` agrees, and every guard your repairs reddened is closed IN THE SAME SESSION THAT REDDENED IT. FORBIDDEN: re-scoring anything (Pass A owns the rubric and you own the repairs -- section 1.7's split), building a new instrument, adding to the blocking set except by the one permitted growth above. YOUR SUCCESSOR PRECONDITION, and section 3.0 says you do not close until you meet it: Pass C can start iff the ship list is CLOSED, pytest is green, and no repair left implicit scope for Pass C to discover. AND READ THIS BEFORE YOU BUDGET: Pass C inherits 14 STRUCTURAL items (13 C-d fold problems, 1 C-c orphan) and Pass D inherits 81 repairs plus 8 C-f to FLAG AND NEVER FIX -- counted per type per paper in REVIEW-038 section 4. Do NOT close P7, P13g, P9 or P8."
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
    count: 11
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
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-103 --task "Pass A: ship-list triage"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-103 --resource ~/repos/wealth-tensor --task "Pass A ship list"'
/tmp/dx '~/Scripts/rail'                                     # check before you swing
/tmp/dx '~/Scripts/charter-read.sh wealthTensor-103'         # YOUR id, not your successor's
/tmp/dx 'python3 ~/repos/claude-blackbook/lessons.py search "ship definition of done severity triage" --scope global,wealth-tensor'
```

**READY first try at `-61` through `-102` — FORTY-TWO for forty-two.** Budget four minutes; it
takes two.

⚠ That last line is **not optional**. `-102` banked three leaves that are aimed squarely at your
at-bat — the tee-up-is-a-claim rule, the pre-repair-assertion rule, and the pass-13 record. Reading
them costs you nothing and saves you a rollback.

⚠ `roster claim` needs `--resource` (a NAMED flag), not `--repo`. `ROSTER_BRAKE_ACK=<n files>` on
commits.

⚠ **RUN THE GATE AS `GATE_ROSTER_WHO=big-wealthTensor-103 bash ~/Scripts/gate-selfcheck.sh`.**
Without it, `G-AL` reads the LAST charter stamp in the shared ledger — which may belong to a
sibling — and tells you YOUR definition of done moved. Jason often runs 2–3 sessions at once;
`roster who` before you believe any cross-repo complaint. At `-101` a sibling (`cloud-OlTGfXay`)
held `claude-blackbook` and `strike-zone` the whole session and nothing collided, because both
sides claimed.

▲ **AND IT NOW WORKS — `-102` IS THE CONFIRMATION `-101` COULD NOT PROVIDE.** `-102` ran the gate
with `GATE_ROSTER_WHO=big-wealthTensor-102` and **G-AL printed nothing at all**, which is the
success case, on a session that had a live sibling (`cloud-dpDPkYUo`) holding two other repos.
Here is what was broken, kept because a successor needs to recognise a relapse:
`charter-read.sh` WRITES the stamp under the SLUG (`wealthTensor-101.log`); `G-AL` was handed
`big-wealthTensor-101` and looked for `big-wealthTensor-101.log`, which never exists. It missed
every tier-prefixed session's own stamp, fell through to a warm-ledger scan, graded the session
against whichever sibling `find` returned first, and printed **`ok`** while naming that file.
**The step that exists to stop you working toward someone else's finish line was grading you
against someone else's ledger.** Fixed in `darwin-mac-ops` `d0e4fd2`, proven both directions,
with two controls added to `gate-charter-drill.sh` and red-proofed. **What you should now see is
NOTHING under G-AL** — success is silent, and a printed `(stamped in <other>.log)` line means it
borrowed a sibling's stamp, which is still accepted by design. That design question is carded at
State Machine `1217721634749933`, not yours.

**Working notes on the transport, all earned:**

- ▲ **WRITE THE SCRIPT LOCALLY, `--put` IT, THEN `dx 'python3 /tmp/x.py'`.** `-100` and `-101`
  both followed this from the first file and both paid nothing. `-101` tried ONE inline
  `python3 - <<PY` heredoc through `dx` and bash ate the parentheses in a regex on line 31. One
  wasted round-trip, and the rule is now five sessions deep in evidence.
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to a directory that **already
  exists**, poll with a second `dx`, and **capture the exit code by redirecting `echo $?` to a
  FILE**, never off the last line. `mkdir -p` in the *caller*, not only inside the script.
- ▲ **`python3 -u` FOR ANY BACKGROUNDED SCRIPT YOU INTEND TO POLL.** `-101` launched `wt091`
  (a six-minute sweep) with `nohup python3 … > log`, polled at 50 s, 170 s and 370 s, and saw
  **zero bytes every time** — Python block-buffers stdout when it is not a terminal, so the log
  stays empty until the process exits. It looked exactly like a hung job. Relaunched with `-u`
  it streamed from the first second. **A silent log is not evidence of a stalled process.**
- ▲ **`echo $?` AFTER A PIPE IS THE PIPE'S EXIT CODE.** `-101` ran
  `python3 script.py --postconditions 2>&1 | tail -40; echo "RC=$?"` and got `RC=0` from a script
  that had just printed `post-conditions: FAILURE` and exited 1. Redirect to a file, then
  `echo $?`, then `tail` the file. This is already the rule for sweeps; it is the rule for
  everything.
- ▲ `tests/test_manuscript_sweeps_are_green.py` reads the promise TSV and
  `tests/test_the_three_counts_are_derived.py` reads the layout manifest, so **a TSV write or a
  manuscript edit invalidates a pytest run started before it.** `pytest` takes ~80 s and is worth
  backgrounding — ⚠ launch it AFTER your last mutation.
- ▲ **`dx` exit 3 = never reached darwin** (nothing ran, safe to re-run) · **4 = dropped AFTER the
  command started** (check state before re-running; no blind retry loops).
- ▲ darwin is macOS + zsh: no `grep -P`, `cut -c` is byte-based.

---

## THE STATE YOU INHERIT — every line RE-RUN by `--claims-all`, not quoted

🟢 `pytest` 1168 passed · `--claims-all` RC 0 — 41 claims declared, 41 re-run un-piped, 41 AGREED
🟢 **`docs/SHIP-LIST.md` EXISTS, IS CLOSED AND IS FROZEN — nine entries, six S1 and three S2, each
   naming its repair.** That file is your at-bat. `docs/REVIEW-038-passA-retrospective-scoring.md`
   is the evidence behind every entry.
🟢 **NO MANUSCRIPT WAS TOUCHED THIS PASS.** `defensive` I/II/III/IV = 0/0/3/0 outside §Limitations,
   unchanged, because Pass A may not repair. Three manuscript digests are recorded at the top of
   `SHIP-LIST.md` so you can prove nothing moved under you.
🟢 **NO `p7-passes.tsv` ROW WAS ADDED**, deliberately. Pass A is not an independent read and
   claiming a seventeenth would be a false row in the one ledger built to stop false rows.
🟢 board 66 criteria BYTE-IDENTICAL after `bash scripts/regen-board.sh` — **fourth consecutive**
   empty diff, and correct: Pass A closed no lane.
🟢 `wt184` RC 0 (28 post-conditions, 9 NEGATIVE), and **its 44 Rule-1 flags are now adjudicated**
🟢 `wt188` 63/20 · `wt189` 19/11 · `wt190` 10/4 · `wt191` 26/12 · `wt191b` 11/5 · `wt192` 25/11 ·
   `wt192b` 12/6 · `wt192c` 13/8 — all idempotent, all byte-identical on a second run
🟢 `wt185` · `wt186` · `wt187` · `wt182` · `wt183` 16/4 · `wt181 --verify` 9 checks
🟢 `wt133` · `wt148` · `wt154` · `wt156` · `wt160` · `wt163` · `wt166` · `wt169` — ALL EIGHT RC 0
🟢 verify-layout RC 0, 145 pages · redproof_wt177 21/21 · wt178 17/17 · wt179 26/26 · wt180 12/12
🟢 gate v2.61 PASS on wealth-tensor, `--emit` HANDOFF OK, tree clean and pushed
🟢 **THE TWO ISSUES `-102` HANDED FORWARD ARE BOTH CLEAN.** G-V#3's four stale `acmeLedger` docs are
   gone and **G-AD reports 120 ratified writers / 0 unratified** — the `cqi: weekly trend` job was
   rerouted. SM `1217793699434587` and `1217793594411582` can be closed.
🟡 **ONE NEW GATE WARNING, and it is not wealth-tensor's** — G-T#44, the n8n-spine crontab has
   drifted from its vaulted snapshot. **CARDED, SM `1217795659362669`, with the reason `-103` did
   not just fire the refresh: the fix `--commit`s the LIVE box's crontab INTO the vault, so if the
   live side is the wrong side it destroys the signal instead of resolving it. Diff first.**
   Do NOT let it block your wrap.

---

## ▶ YOUR AT-BAT · ONE THING — **PASS B: CLEAR THE TRUTH LIST**

**Read `docs/DEFINITION-OF-DONE-SHIP.md` first — it wins over this file and over `CHECKLIST.md`;
only `CO-AUTHOR-CHARTER.md` wins over it.** Your at-bat is its § 3, Pass B.

**Repair all nine entries in `docs/SHIP-LIST.md`**, in the charter's order — **STEELMAN → REPLACE →
CUT → TEE-UP** — and never ABSORB as manuscript hedging. `defensive_count.py --against` must read
**+0** on every manuscript.

> **NO NEW LOOKING. You are not a review pass.** DoD § 1.2: a finding you discover goes to
> `docs/POST-SHIP.md`, never onto the list. **The one permitted growth:** a repair that reveals an
> adjacent S1 *at the site you are repairing* — repair it, append it, log it with the repair that
> surfaced it.

### Four things that make nine smaller than it sounds

1. **`SL-3`/`SL-4`/`SL-5` are one repair, three times** — stale version stamps, **21 / 36 / 19
   commits** past their own dates. **One written Jason ruling closes all three** if he would rather
   own version numbering himself; DoD § 2 allows an S1 to close by ruling as well as by repair.
2. **`SL-7` and `SL-8` each have a landed precedent IN THIS CORPUS.** `SL-8` is `-81`'s `IV-7`
   repair — cite it at the sentence that relies on it, or cut the entry. `SL-7`'s honest-disclosure
   form is **already written** in paper-III § 11's own § 5.3 bullet. **Read the precedent before
   inventing a form.**
3. **`SL-1` and `SL-2` are attribution changes, not number changes.** The arithmetic in both
   sentences was checked this session and is correct. **Re-point; do not recompute.**
4. **`SL-6` must not be repaired by restating the number.** `wc -w` gives **7367** under `LC_ALL=C`
   and **7527** under a UTF-8 locale, on the same bytes. Name the command *and* the locale. A bare
   corrected figure re-creates the defect for the next reader.

### DONE WHEN

Every ship-list entry marked repaired with its commit · `defensive_count --against` **+0** on all
three manuscripts · `pytest` green · `--claims-all` agrees · **every guard your repairs reddened
closed in the same session that reddened it.**

### FORBIDDEN THIS PASS

Re-scoring anything (DoD § 5's `L7` — Pass A owns the rubric, Pass B owns the repairs, and neither
grades its own homework) · building a new instrument · growing the blocking set except by the one
permitted growth above.

### ⚠ YOUR SUCCESSOR PRECONDITION — you do not close until you meet it (§ 3.0)

> **Pass C can start iff the ship list is CLOSED, `pytest` is green, and no repair left implicit
> scope for Pass C to discover.**

**AND BUDGET FOR WHAT YOU ARE FEEDING, because `-103` measured it so you would not have to guess:**
Pass C inherits **14 structural items** (13 C-d fold problems, 1 C-c orphan). Pass D inherits **81
repairs** — 15 hard C-e, 61 C-b, 5 C-a — **plus 8 C-f to FLAG AND NEVER FIX.** Per type per paper
in `REVIEW-038` § 4. **Paper-III is 55 % of the coherence work by itself.**

---

## WHAT `-103` DID — Pass A, and the measurement eight sessions were owed

**THE HEADLINE, AND IT INVERTS SIX HANDOFFS' WORTH OF ASSUMPTION.** Seventy findings across sixteen
passes were scored against the rubric `-102` committed *before* any scoring:

| | n | share |
|---|---|---|
| **S1** — the paper states something FALSE | **53** | **75.7 %** |
| **S2** — asserts something nothing supports | 16 | 22.9 % |
| **S3** — precision and taste | **1** | **1.4 %** |

**S1 share by thirds: 87.5 % → 61.9 % → 76.0 %. Severity never fell.** The last six passes returned
**nineteen** S1s against the first five passes' twenty-one — on a corpus already repaired forty-five
times. **`-102`, the sixteenth read, found two findings and both were S1.**

**So the flat counter was never diminishing returns.** And **the S3 tail everybody assumed was
accumulating does not exist — one S3 in seventy.** The apparatus was never producing nitpicks.
That is a compliment to sixteen passes, and it is exactly **why § 2.5's amendment was necessary**:
the rubric graded truth, the axes hunted truth, the passes found truth defects at a 76 % clip, and
**every C-class seam was invisible to all sixteen of them because every seam is a true statement.**

**THE 44 FLAGS: 2 TRUE, 42 FALSE.** Both TRUE are S1, both are in paper-III § 4.9, and both are
`III-5`'s family — a *possessive* attribution of a number to a section carrying something else.
`§4.4's 0.00789` names a value that occurs **once in 2 750 lines, in that sentence**. The 42 FALSE
sort into three named mechanisms and the false-positive-reduction spec is written and **measured
against the full adjudication** — it returns 2 of 44 and both are the true ones. **Not built:
§ 1.1.**

**THE C-CLASS: 156 counted**, per type per paper. **Two results worth stating positively: C-g is
ZERO across 23 tables — every table already carries an anchor sentence, so Pass D has none to write
— and C-c is ONE.** Those are earned, and they are the payoff of sixteen cross-reference passes.

**TWO GUARDS REPAIRED AT WRAP, and the story is better than the fix.** `--claims-all` went red on
`wt188` and `wt192c`. **Neither manuscript had moved** — both guards read the live `docs/HANDOFF.md`
and asserted text that `-103` was *required* to replace. `-102` had already been burned by exactly
this shape and anchored one end of `wt188`'s before/after pair to a commit; the other end stayed on
the working tree, so the repair lasted one session. Both ends now read a commit; 63/63 and 13/13,
each re-run twice with byte-identical stdout.

**BUG SPRAY, off the at-bat but on the path:** `lessons.py`'s leaf
`2026-08-16-perfection-done-domains-research-papers-anything` was still prescribing **the retired
convergence criterion** as the definition of done for research projects — the exact rule Jason
killed for having no termination proof and for rewarding not looking. **A future Claude searching
"definition of done" was being handed the refuted rule by the corpus that refuted it.** Curated in
place, same id so nothing dangles, keeping the half that still holds and recording what refuted it.

---

## THE TELL, now ONE HUNDRED AND FIFTY-SIX deep

**`-103`(i) · A FLAT COUNTER IS NOT EVIDENCE UNTIL THE DEFECTS ARE SCORED.** Eight sessions read a
flat 2–9 band as the barrel being scraped. It was 76 % S1 throughout. **A flat count of severe
findings and a flat count of nitpicks are opposite situations that look identical on the counter**,
and one session of scoring is the only thing that separates them.

**`-103`(ii) · THE DISCRIMINATOR IN A NATURAL-LANGUAGE CHECKER IS USUALLY A GRAMMATICAL RELATION,
NOT A THRESHOLD.** `wt184` Rule 1 over-fired 42 times out of 44 and the whole difference is the
possessive. **Three sessions proposed narrowing the rule before anyone read its output** — and one
of them, `-101`, described a mechanism the file did not contain. Read the flags, *then* write the
rule.

**`-103`(iii) · A SELF-REFERENTIAL MEASUREMENT MUST NAME ITS MEASURING COMMAND.** `wc -w` is
locale-dependent: 7 367 vs 7 527 on identical bytes. **`-100`'s repair of that sentence fixed it for
one reader and broke it for another**, which is the sharpest possible statement of why the number
alone is not the claim.

**`-103`(iv) · THE `-102` TRAP CAUGHT THE SESSION AUDITING IT, TWICE.** Two verification greps went
red and **both times the check was wrong, not the manuscript** — one pinned to a line break in a
hard-wrapped file, one pinned to `**` around the value. Fourth witness. **Grep the concept.**

**`-103`(vi) · A GUARD THAT READS `docs/HANDOFF.md` IS GREEN FOR EXACTLY ONE SESSION.** Two claims
went red at wrap and **neither manuscript had moved** — `wt188` and `wt192c` both asserted the
content of the handoff, which every successor is *required* to rewrite. `-102` had already been
burned by this intra-session and anchored the BEFORE side of `wt188`'s pair to a commit; it left the
AFTER side on the working tree, so the fix survived one session and then fired on the pass that
inherited it. **Sixth time in a row that a red guard was wrong about the file rather than the file
being wrong.** Both ends now read a commit. **Before registering a claim, ask what could move this
value for an unrelated reason — and `docs/HANDOFF.md` moves every session, by design.**

**`-103`(v) · A COUNT THAT WOULD MAKE THE NEXT PASS DO THE WRONG THING MUST BE SPLIT BEFORE IT IS
REPORTED.** The raw C-e sweep said 68 apparatus leaks. Reported raw, Pass D would have stripped the
`scripts/wt###.py` pointers out of the § Data-and-code sections — **deleting the provenance promise
the entire S1/S2 apparatus exists to keep.** Split by mechanical census into 15 hard and 53 soft.
**An inventory is for sizing someone else's work, so it owes them the distinction that changes what
they do.**

---

## TOOLING (▲ new at `-103`)

▲ **`docs/SHIP-LIST.md`** — the frozen blocking set. Nine entries. **Find an entry by its quoted
  text, not its line number**: Pass B's own repairs will move the numbers, and the file says so.
▲ **`docs/REVIEW-038-passA-retrospective-scoring.md`** — the severity table, the per-pass
  breakdown, the full 44-flag adjudication with mechanisms, and the C-class census.
▲ **`docs/POST-SHIP.md`** — now carries the triage of seven tee-ups plus the `wt184` reduction spec.
▲ **`wt188` and `wt192c` repaired** — both had post-conditions pinned to the live `docs/HANDOFF.md`.
  A false-positive reduction, which § 1.1 permits explicitly. `.bak-wt103` of each is on disk and
  the previous version is in git.
- Everything else is unchanged from `-102`. **No instrument was built this pass** (§ 1.1).

---

## TEE-UPS — what `-103` found and did NOT do

**All nine carried tee-ups are TRIAGED and none is carried forward as a tee-up.** Two became ship
list entries (`SL-8`, `SL-9`); seven are in `POST-SHIP.md` with their reasons. `REVIEW-038` § 5 is
the table. **Do not re-triage them** — that is the loop this pass existed to end.

What remains genuinely open and is nobody's at-bat until the corpus ships:

1. **The `wt184` false-positive reduction.** Spec written and measured; **not built**, § 1.1.
   SM `1217774684736450`.
2. **The C-class soft tail** — 53 unglossed but fetchable pointers. A gloss pass, not a leak.
3. **G-T#44, the n8n-spine crontab drift.** SM `1217795659362669`. **Not this repo's**, and the
   card says why firing the refresh blind is the wrong move.

---

## ESTATE

- **Carded this session:** G-T#44 crontab drift — State Machine `1217795659362669`.
- **CLOSEABLE — verified clean at `-103`'s gate run:** SM `1217793699434587` (G-V#3 stale
  acmeLedger docs) and `1217793594411582` (G-AD Batter's Box writer). **Both read clean.**
- **Carried:** `docs/preregistration/RESULT-REG-005.md` line 60 (`-101`'s card) — a committed
  result document for a registered run, **State Machine**, behind the same Jason ruling as `-83`'s
  RESULT-001. **Not on the ship list: it is not a manuscript.**
- **Carried:** `verify-layout.sh`'s one unreproducible false red, card `1217643242299336` — do NOT
  report P13e green from a single run; if it goes red, re-run before believing it.
- **Lessons banked:** four global, one project-scoped, plus one **curation** of the refuted
  convergence leaf. Three leaves corroborated under task `wt103-passA`; one promoted
  quarantine → active.

---

## JASON-SIZED, not `-104`'s

- **THE VERSION STAMPS (`SL-3`/`SL-4`/`SL-5`).** Pass B can bump them, and will unless you say
  otherwise. **If you would rather own version numbering yourself, one written line closes all
  three** and Pass B skips them.
- **The zakat citation.** Paper-II's own note promises a primary source *"at submission."* Ruled
  **S3** and moved to POST-SHIP because the paper discloses it and the argument does not depend on
  it — **but posting a preprint is arguably that submission, and the call is yours, at posting.**
- **Editing a committed registered result document** (RESULT-REG-005, and `-83`'s RESULT-001).
  Two queued behind the same ruling.
- **The two-independent-readers design** — two sessions to buy one data point. Still yours.
- **P8, your own-hand rewrite**, is what Pass D is building toward. **`FIGURE-PLAN.md` is the
  artefact it runs on** and Pass D emits it: 23 tables, zero figures, and the question is which
  table wants to be a picture.

---

## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)

**P7 · corpus · PENDING-HUMAN.** `-103` ran Pass A of the ship plan and did **not** score the lane.
`docs/CHECKLIST.md` regenerated **byte-identical** — 57 CLOSED / 9 PENDING-HUMAN / ZERO OPEN — the
**fourth consecutive** session to produce that empty diff deliberately. **Pass A is on the path to
P7's stated criterion**: zero OPEN S1 and zero OPEN S2 on a frozen `SHIP-LIST.md` cannot be measured
until the list exists, and now it does.
