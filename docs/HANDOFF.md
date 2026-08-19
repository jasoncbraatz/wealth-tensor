---
project: wealth-tensor
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: be64df855341329916b2fc9a9acc3e285a4979dc
updated: 2026-08-19
session: wealthTensor-90
session_n: 90
live_theme: "THE DOCUMENT-NOUN PRE-FILTER DOES NOT SURVIVE HELD-OUT TEXT, AND THE COLLAPSE SORTS EXACTLY BY WORD CLASS. All 88 bare-target constructions in Papers I and II at 83db4d5 are read and labelled -- 7 POINTERs, a 7.95% base rate -- and wt169 scores wt166's six candidate tests against them with the word lists imported UNMODIFIED and hashed so a re-tune fails the run. T5, the only artefact REVIEW-029 left standing, goes from recall 1.0000 / precision 0.2459 on the corpus its noun list was written against to recall 0.1429 / precision 0.0714 on text it was not: it recovers ONE of seven pointers, at a precision BELOW that corpus's own 0.0795 base rate, which makes it anti-informative rather than merely weak. Six of the seven point at 'the code and the tests', 'the test', 'the test suite', 'the implementation', 'this programme' and 'the third column' -- none of those head nouns is in DOC_NOUNS, because the list was read off two manuscripts that point at registrations, titles and logs. THE RESULT NOBODY PREDICTED IS BETTER THAN THE ONE THAT WAS: both OPEN-CLASS tests collapsed (T5 1.0000->0.1429, T2 0.7333->0.1429) and all four CLOSED-CLASS tests held or improved (T1 1.0000->1.0000, precision UP). REVIEW-029 §2.1 declared each candidate's word class before scoring, purely to keep a disqualification honest; that declaration turns out to predict which tests generalise, and it belongs to -89."
phase: "EIGHT criteria green plus the new ninth: wt148 RC 0 (136 adjudicated), wt133, wt154, wt156, wt160, wt163, wt166 and wt169 all RC 0, suite 1095 passed. wt169's 17 post-conditions include SIX that were predictions about a measurement not yet taken (G6, G7, G11, G12, G13, G14) and all six held; G8 hashes wt166's five word lists so a future re-tune fails loudly. The seven bare pointers the labelling found in Papers I and II are REPORTED AND CARDED, NOT REPAIRED -- deliberately, because -90's at-bat was to measure and neither manuscript was touched. What -90 did NOT do is anything on P13, and it did not unpark #scope: Paper II is one of the three papers in the definition of done and 28 promises there are still checked by nobody, NINE passes running."
gate_passed: false
gate_version: "2.60"
next_at_bat: "ASSIGNED, ONE THING: PAPER II'S TURN — WIDEN #scope TO paper-II AND ADJUDICATE EVERY PROMISE IT EMITS. Nine consecutive passes have parked this and the reason it can no longer wait is in the definition of done: the batch is Papers II, III and IV, so Paper II is a SHIPPING paper, and the promise instrument — 136 rows of adjudicated evidence across III and IV — has never been pointed at it. 28 promises there are checked by nobody. Edit ONE line in docs/promises-adjudicated.tsv: `#scope\tpaper-III\tpaper-IV` becomes `#scope\tpaper-II\tpaper-III\tpaper-IV`. Do NOT add paper-I — it is not in the definition of done, adding it doubles the work for a manuscript nobody is shipping, and the narrowing is the point. Then run `python3 scripts/wt148_promise_sweep.py`, read what it emits, and adjudicate every row to H, N, R or C with the SAME standard the existing 136 rows hold: a row is a CLAIM that a human RAN OR READ the artefact, so the evidence column must quote the command's ACTUAL stdout character for character — wealthTensor-89 lost a post-condition to a note that recorded the EXPECTED output and was never diffed against the real thing, which is why wt168's H14 asserts stdout.strip() == CONSTANT. Write the same guard for your new rows. COMMIT THE SCOPE LINE BEFORE YOU ADJUDICATE ANYTHING, so the emitted set is a git object nobody can quietly reshape. EXPECT R AND C ROWS AND DO NOT FLINCH: Paper II has never been through this, III and IV needed repairs, and a pass that widens scope and reports 28 of 28 clean is more likely to have adjudicated loosely than to have found a clean paper — say so in the review if it happens and show what a FAILING row would have looked like. DONE WHEN: docs/promises-adjudicated.tsv's #scope line names paper-II; every promise wt148 emits for paper-II carries an adjudication with quoted evidence; wt148 RC 0 with the new total SAID OUT LOUD; docs/REVIEW-031 states in ONE sentence someone could mark right or wrong whether Paper II's promises are checkable, with the counts that settle it; wt133 AND wt154 AND wt156 AND wt160 AND wt163 AND wt166 AND wt169 all still RC 0; suite green AND SAY THE NUMBER; coach at baseline. DO NOT REPAIR PAPER II'S THREE BARE POINTERS IN THIS PASS — they are carded on 1217629169253037 and a manuscript edit mid-adjudication makes the promise set move underneath you. If you are editing paper-II.md's prose you have drifted."
blockers: []
drift_flags:
  - "T5 IS DEAD AS A PRE-FILTER AND THE 1.0000 MUST NEVER BE REQUOTED. It was recall 1.0000 on the corpus its noun list was written against and recall 0.1429 on text it was not, at a precision BELOW the base rate. wealthTensor-89's leaf in claude-blackbook has been CURATED to lead with the collapse; -89's warning was right and its 'read T5's 61 first' recommendation is withdrawn by the measurement it asked for. Do not resurrect it by lengthening DOC_NOUNS -- that is the same circular exercise one corpus over, and wt169's G8 will fail the run if you try."
  - "DO NOT 'CORRECT' REVIEW-029 §6.1 OR REVIEW-028 §4's FOURTEEN. Both are git objects and both are load-bearing precisely because they were partly wrong: a careful vocabulary-free reading missed a copula, and a careful successor's prediction got the sign right and the magnitude wrong by a factor of six. REVIEW-030 §6 marks them in place. Same rule -88 and -89 applied to their own reviews."
  - "REVIEW-030 §4.1's GENERALISATION RESTS ON TWO CORPORA. 'Closed-class features transfer, open-class features do not' is the most interesting sentence this programme has produced about language and the least supported one -- four manuscripts, one author, one project. It is disclosed as falsifier 6 rather than sold. Do not quote it as established."
  - "THE HELD-OUT LABELLER HAD READ THE INSTRUMENT FIRST, AND THAT IS DISCLOSED IN THE TSV'S OWN HEADER. -90 read wt166 in full, DOC_NOUNS included, while orienting, BEFORE labelling a row. No row was checked against the list at labelling time, but the independence claim is weaker than -89's and the file says so. The attack is named in REVIEW-030 §8 falsifier 1: re-label the 88 from the header rule alone, with no access to wt166, and diff. The protocol repair for the NEXT held-out exercise is one line -- read the corpus before the instrument."
  - "SEVEN BARE POINTERS STAND UNREPAIRED IN PAPERS I AND II, three of them in Paper II which IS in the definition of done. Card 1217629169253037 lists all seven with confidences. One of them -- `II 11 named in the data-availability statement` -- is the IDENTICAL construction wt164 already repaired in Paper III, so the same defect ships in one paper and not the other. Deliberately not repaired by -90 and deliberately not -91's at-bat."
  - "wt169's REVISION PIN IS CURRENTLY INERT. Papers I and II are byte-identical at 83db4d5 and at HEAD because -90 repaired nothing, so wt169's drift guard is proved non-vacuous only by G5's fabricated row, never by a real repair the way wt166's F9 is. THE FIRST SESSION TO REPAIR ONE OF THE SEVEN must check wt169 still returns RC 0 and its 88 keys still recompute. REVIEW-030 §8 falsifier 4."
  - "G8 GUARDS THE WORD LISTS AND NOTHING ELSE. A future session could leave DOC_NOUNS untouched and change t5_document_head_noun's MATCHING -- stemming, lowercasing differently, a fuzzy compare -- and every digest would still pass. The guard covers the data, not the code."
  - "THE UNSUPPORTED FOUR STILL STANDS IN PRE-002 §2, RESULT-001 §1 AND RESULT-002 §1, carded as a second instance on 1217603625863293 with a named falsifier. DO NOT EDIT THEM -- in-place edits to a registration or a result document are Jason's standing ruling. Unchanged from -89."
  - "REVIEW-028'S PUBLISHED TEN CONTAINS FOUR ROWS -89 MARKS SOFT and a strict reading gives 11. Disclosed at REVIEW-029 §8 falsifier 2 and scored in full as the STRICT variant. It changes no verdict. Unchanged from -89."
  - "docs/pointer-exclusions.tsv is still pinned to SIX rows by wt163's D3. Do not silently append. Unchanged from -88."
  - "ANY OTHER TOKEN MATCHER OVER ENGLISH PROSE IN scripts/ STILL HAS THE \\b-INSIDE-A-COMPOUND BUG UNTIL CHECKED. wt160 and wt163 were fixed; wt166 and wt169 were written with the guard; nothing else has been audited. Unchanged from -88."
  - "N1-N6 NOW HAVE FOUR KNOWN GAP CLASSES, not two. A page number and a commit SHA (REVIEW-028 §4 M6/M7); this document's own named divisions, now including a NUMBERED one, 'Limitation 1' (REVIEW-029 and REVIEW-030 §5.2b); and NEW at -90, a bracketed cross-paper citation whose comma the twelve-word window treats as a clause boundary, so `[III, §2.2]` reaches N2 as `[III` and never matches (REVIEW-030 §5.2a). All carded on 1217629264134185 rather than patched, because N7/N8 move a published count. The window gap produces a FALSE BARE, so it errs safe."
  - "PAPER I IS NOT IN THE DEFINITION OF DONE. The batch is Papers II, III and IV. -90 labelled Paper I because it is held-out TEXT, which is a different use of it from shipping it. Do not let 88 labelled rows turn into a Paper I workstream."
  - "wt154's PREDICATE BLIND SPOT unchanged, card 1217613775009402. wt133's SWEEP-2 BLIND SPOT unchanged, State Machine 1217593142996092."
  - "lessons.py's CONTRIBUTOR STAMP STILL DOES NOT RESOLVE FROM THE ROSTER -- -90 hit it again and passed --contributor big-wealthTensor-90 on all seven adds, which works. Still teed up, not fixed. THIRD session in a row."
parking_lot:
  - "Repair the seven bare pointers in Papers I and II. Card 1217629169253037. Paper II's three are the ones that matter for the definition of done; Paper I's four are optional. Use wt167's G4 pattern: wt160's AND wt163's flag sets must be bit-identical across the repair, and wt169 must still return RC 0."
  - "N7/N8 for the two new N1-N6 gaps. Card 1217629264134185. Needs POSITIVE and NEGATIVE post-conditions and a disclosed count movement."
  - "Read the 88 held-out rows a SECOND time, from the TSV header's rule alone with no access to wt166, and diff against -90's labels. REVIEW-030 §8 falsifier 1. This is the cheapest second-reader experiment this programme has ever been able to run, because for the first time the thing to disagree with is 429 rows of committed data."
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
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-91 --task "Paper II's promises: widen #scope"'
```
**READY first try at -61 through -90 — THIRTY for thirty.** Budget four minutes; it takes two.
- ⚠ `roster join` returns RC=0 with **NO OUTPUT** on a re-join, and prints `absorbed N row(s) …
  (carried 1 claim(s))` when it adopts a `cloud-<fp>` identity. That line is the healthy path.
- ⚠ `roster claim` syntax: `--who X --resource wealth-tensor --task "..."` — **resource is a NAMED flag.**
- ▲ **Changing your own name mid-session:** `join` new → `claim` new → `leave --who <old>`.
- ⚠ `roster-brake` **WILL** block your first `git add` commit. **`ROSTER_BRAKE_ACK=N` is the
  answer**, ranked SECOND. Card `1217596263441666`. -88, -89 and -90 set it on every commit and
  lost nothing.
- ▲ **SIBLING SESSIONS SHARE DARWIN'S WORKING TREE.** At -90's wrap `floristDeputize-2` held a
  live claim on `claude-blackbook`; committing a lesson printed a CONTENTION heads-up and went
  through anyway (the brake is pre-commit and only refuses the `git add -A` shape). **Stage
  PATHS, never `-A`, in any repo you do not own for the session.** Run `roster who` and `rail`
  before you touch anything.
### THEN STAGE THE DOCS AS ONE TARBALL
```
mkdir -p /home/claude/wt          # FIRST. $HOME is /root in the container.
/tmp/dx 'mkdir -p /tmp/wt91'
/tmp/dx 'cd ~/repos/wealth-tensor && git pull --ff-only && tar czf /tmp/wt-docs.tgz docs scripts tests'
/tmp/dx --get /tmp/wt-docs.tgz /home/claude/wt/wt-docs.tgz
```
- ⚠ ▲ **NEVER NAME A LOCAL SCRATCH SCRIPT AFTER A STDLIB MODULE.** -90 wrote a throwaway
  `enum.py` in its working directory and every subsequent `python3` invocation in that directory
  died — including `python3 -c "import json"`, because `json` imports `re` which imports `enum`.
  The traceback points at YOUR file from inside the stdlib and reads like a broken interpreter.
  Same trap: `json.py`, `types.py`, `string.py`, `code.py`, `test.py`, `io.py`, `random.py`.
  **Rename the file; do not debug the import.** One turn, and it looked like a container fault.
- ⚠ **`/tmp/dx --put` will NOT create a missing remote directory.** `mkdir -p` on darwin FIRST.
- ⚠ Stage `tests/` **too**.
- ⚠ `tar xzf` prints macOS xattr warnings with the extraction **perfectly fine**.
- ⚠ `.bak` files **sort first**. Read the path, not the first line.
- ⚠ **The local Bash tool's working directory PERSISTS between calls.** Lead with
  `cd /home/claude/wt &&` or use absolute paths.
- ⚠ **ANYTHING THAT IMPORTS `src/` MUST RUN ON DARWIN** — wt027 / wt002 / wt026 / wt071 / wt089 and
  all of pytest. `wt133` / `wt148` / `handoff_gate --coach` are pure-doc and run **locally in
  under a second**. `wt154` / `wt156` and **wt160's, wt163's, wt166's and wt169's post-conditions**
  shell out to `git show`, so those need the repo.
  ▲ **`wt166` AND `wt169` need the repo unconditionally**, not just for post-conditions: both read
  their corpus through `git show`, and `wt169` additionally re-runs `wt166`'s enumeration at
  `07cd47e` to build the cross-corpus comparison. There is no `--skip-postconditions` shortcut.
- ▲ A script under `tests/` invoked directly needs `PYTHONPATH=src`.
- ⚠ ABSOLUTE local paths in every `cat X | /tmp/dx --put`.
- ⚠ **NEVER** pipe a command through `dx` whose exit code you intend to read — `$?` after a pipe is
  the *last* command's. Redirect inside the remote command and echo `$?` there.
- ▲ Nested quotes → write the script **LOCALLY**, `--put` it, run `dx 'bash /tmp/x.sh'`. -83 wrote
  all seven that way, -84 six, -85 four, -86 six, -87 five, -88 nine, -89 eleven, **-90 eight**,
  and none lost a turn. **WRITE THE FILE.**
- ⚠ ▲ **`charter-read.sh` TAKES YOUR OWN SESSION ID, NOT YOUR SUCCESSOR'S.** The handoff's AT
  WRAP line names the NEXT session because it is addressed to them; when YOU run it, pass
  YOUR id. -90 passed `wealthTensor-91` and `G-AL` failed at the very last step.
- ⚠ ▲ **`~` DOES NOT EXPAND INSIDE A QUOTED SHELL VARIABLE.** `L="python3 ~/repos/.../lessons.py"`
  then `$L add …` fails on every call. **Use `$HOME` or an absolute path in any variable holding a
  command.** -89 lost a turn to eleven identical failures; -90 used `$HOME` and lost nothing.
- ▲ Long remote jobs survive the local Bash timeout — `nohup` to `/tmp/wt91/`, poll with a second
  `dx`. **pytest takes ~72 s and is worth backgrounding.** ⚠ Launch it AFTER your last mutation and
  read the run you started last.
- ▲ **A `dx` call interrupted client-side may still have RUN on darwin.** Check for the effect
  before re-running a mutating one.
---
## THE STATE YOU INHERIT AND MUST PRESERVE
🟢 `python3 -m pytest tests/ -q` → **1095 passed, 1 warning, 72.12 s.** RUN IT AND SAY THE NUMBER.
🟢 `python3 scripts/wt148_promise_sweep.py` → **RC 0**, **136 adjudicated**: paper-III **91 of 91**
   (84 H · 6 N · 1 R), paper-IV **45 of 45** (43 H · 2 R). **28 outside scope, unchecked.**
🟢 `python3 scripts/wt133_crossref_sweep.py` → **RC 0**.
🟢 `python3 scripts/wt154_evidence_discrimination_sweep.py` → **RC 0**, **0 of 136**.
🟢 `python3 scripts/wt156_reproducibility_sweep.py` → **RC 0**, **0 of 136**, 4 NEGATIVE.
🟢 `python3 scripts/wt160_bare_pointer_sweep.py` → **RC 0**, **0 flagged of 13**, 12/12 post-conditions.
🟢 `python3 scripts/wt163_pointer_vocabulary.py` → **RC 0**, **21 considered, 6 flagged, all six
   disclosed-excluded, 0 undisclosed**, 13/13 post-conditions, 4 NEGATIVE.
🟢 `python3 scripts/wt166_pointer_groundtruth.py` → **RC 0**, **444 considered / 341 bare /
   15 POINTER**, 15/15 post-conditions, 5 NEGATIVE.
🟢 ▲ `python3 scripts/wt169_pointer_groundtruth_heldout.py` → **RC 0**, **125 considered / 88 bare /
   7 POINTER (4 FIRM, 3 SOFT)**, **17/17 post-conditions, 6 NEGATIVE**. RC 2 = the held-out labels
   have drifted from Papers I/II, or a word list was re-tuned, or a post-condition failed.
   **There is no RC 1** — it reports a measurement, not defects.
🟢 coach: paper-III **5 conduct / 0 concessive**; paper-IV **1 / 0**; paper-I **1 / 0**;
   paper-II **2 / 0**.
🟢 GATE: **PASS**, gate v2.60, `gate-selfcheck.sh` PASS, handoff-lint clean.
**Wrap order:** commit → `--stamp` → commit → push → `charter-read.sh` → gate → `--emit`.
The ANCHOR line (*"ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything
in this file."*) must be **verbatim, above the fold** — put it in FIRST.
---
## ▶ YOUR AT-BAT · PAPER II'S TURN — WIDEN `#scope` AND ADJUDICATE ITS PROMISES
`next_at_bat` in the front matter is the full brief and it is binding. The short version:
**Nine consecutive passes have parked this, and the reason it can no longer wait is the definition
of done.** The batch is Papers **II**, III and IV. Paper II is a shipping paper. The promise
instrument now holds **136 rows of adjudicated evidence** across III and IV — and it has never
been pointed at Paper II. **28 promises there are checked by nobody.**
Edit ONE line in `docs/promises-adjudicated.tsv`:
`#scope\tpaper-III\tpaper-IV` → `#scope\tpaper-II\tpaper-III\tpaper-IV`.
**Commit that line BEFORE you adjudicate anything**, so the emitted set is a git object nobody can
quietly reshape. **Do not add `paper-I`** — it is not in the definition of done, and the narrowing
is the point rather than a shortcut.
**⚠ DO NOT REPAIR PAPER II'S THREE BARE POINTERS IN THIS PASS.** They are carded on
`1217629169253037`. A manuscript edit mid-adjudication makes the promise set move underneath you —
`wt167`'s repair emitted a promise that `wt168` then had to adjudicate, and that was one row, on
purpose, at the end of a pass. If you are editing `paper-II.md`'s prose you have drifted.
---
## WHAT -90 DID
**The chain is in git, in this order, and each link was committed before the next existed:**
| commit | what | when |
|---|---|---|
| `cd46d3d` | **REVIEW-030 §§1–3 — the prediction** | before a single held-out label existed |
| `6b262aa` | **`docs/pointer-groundtruth-I-II.tsv` — 88 labelled rows** | before the scorer existed |
| `9e38d18` | **`wt169` — the scorer, committed UNRUN** | before it had ever been run |
| *(next)* | the measurement, REVIEW-030 §§4–9 | after |
**The headline, in one sentence someone can mark right or wrong.** T5's recall does not survive:
on Papers I and II the document-class-noun test recovers **1 of the 7** bare pointers, recall
**0.1429** against **1.0000** on Papers III and IV, at precision **0.0714** — **below that
corpus's own 0.0795 base rate**, so reading its 14 flagged rows is worse per row than reading 14
at random. It is not a weak filter; it is an anti-informative one.
**Why, as arithmetic rather than as a story.** Exactly ONE of the seven pointers has a `DOC_NOUNS`
word in its target (`G12` pins it): `II 11 named in the data-availability statement` — the same
construction Paper III carries, and therefore the one row of the seven that is not really held out
at all. The other six point at **`the code and the tests`**, **`the test`**, **`the test suite`**,
**`the implementation`**, **`this programme`** and **`the third column`**. Papers III and IV point
at registrations, titles and logs, so a list read off them names registrations, titles and logs.
**Papers I and II are papers about code, and they point at code.**
**THE UNPREDICTED RESULT IS THE BETTER ONE — the collapse sorts exactly by word class:**
| test | class | III+IV recall | **I+II recall** |
|---|---|---|---|
| T5 document-class head noun | OPEN | 1.0000 | **0.1429** |
| T2 claim-subject | OPEN | 0.7333 | **0.1429** |
| T1 definite head | CLOSED | 1.0000 | **1.0000** (precision UP, 0.1049→0.1750) |
| T3 determiner + abstract shape | CLOSED | 0.6667 | **0.5714** |
| T4 section position | CLOSED | 0.2000 | **0.5714** (noise, wandering) |
| T6 copular frame | CLOSED | 0.2000 | **0.2857** (first honest test; still fails) |
REVIEW-029 §2.1 declared each candidate CLOSED- or OPEN-CLASS **before any of them was scored**,
purely to keep T5's disqualification honest. That declaration has now made a prediction about a
corpus that was not yet data, and it is exactly right. **It is a stronger result than -89 claimed
for it, and it belongs to -89.**
**Three more things measured that nobody asked for.** `T6` got its first honest test and still
fails (0.0769 / 0.2857). `-89`'s LOOSE surprise — `wt166`'s `F14`, where T5 alone cleared under the
loosest labelling — **does not reproduce** on held-out text. And the best pairwise conjunction is
`T1+T4` at 0.2857 / 0.5714, reported because REVIEW-029 §3 committed in advance to reporting it
whether or not it helped.
**Six post-conditions were predictions and all six held.** `G6` (T5 does not reach recall 1.0000),
`G7` (nothing clears), `G11` (nothing partial-wins), `G12` (exactly one pointer carries a
`DOC_NOUNS` word), `G13` (T5's recall is strictly lower here, recomputed rather than quoted) and
`G14` (nothing is a usable pre-filter) were all written into a file that had never been run.
**`G8` is the guard that makes this a test rather than a repeat**: it hashes `DOC_NOUNS`,
`CLAIM_NOUNS`, `DEFINITE`, `DETERMINERS` and `BE_FORMS` against digests in `wt169`'s own source,
so a future session that re-tunes a list fails the run instead of quietly rescoring.
---
## THE TELL, now ONE HUNDRED AND SIX deep
-61–-89 as before. **-90 adds seven.**
- **-90(i) A WORD LIST SCORED ON THE CORPUS IT WAS WRITTEN AGAINST MEASURES THE LIST, AND THE GAP
  IS NOT SMALL.** Recall 1.0000 → 0.1429 on held-out text from the *same project, same author,
  same genre*. The list enumerates how THOSE documents happen to name their artefacts. **Do not
  ship a pre-filter until it has been scored on text nobody consulted while building it.**
- **-90(ii) CLOSED-CLASS FEATURES TRANSFER; OPEN-CLASS FEATURES DO NOT — AND SAYING WHICH IS WHICH
  BEFORE SCORING PREDICTS IT.** The declaration cost one sentence at design time and turned out to
  be the only advance signal of transfer available. Do it on any feature set you intend to reuse.
- **-90(iii) ON A HELD-OUT LABELLING EXERCISE, READ THE CORPUS BEFORE THE INSTRUMENT.** Reading the
  detector's word list while orienting — with no intention of using it — is a contamination you
  can only disclose, because a labeller who knows the list can favour rows it misses without
  meaning to. **The protocol that survives is ORDER, not intent.**
- **-90(iv) WHEN SCORING AN INSTRUMENT ON A NEW CORPUS, RECOMPUTE THE OLD ONE IN THE SAME PROCESS
  INSTEAD OF QUOTING THE PUBLISHED NUMBERS.** Three of -90's four unanticipated results were
  invisible in the new corpus alone and obvious in the two columns side by side. Quoting would have
  produced the right headline and none of the understanding.
- **-90(v) COMPUTE THE BASE RATE AND COMPARE PRECISION TO IT.** "Precision 0.07" is a number;
  "precision 0.0714 against a base rate of 0.0795" is a verdict. **A filter whose precision is
  below the prevalence is ANTI-INFORMATIVE** — the advice is to stop using it, not to tune it.
- **-90(vi) SIX FOR SIX ON PREDICTIONS IS A WARNING ABOUT THE BAR, NOT A BOAST.** -90's §3 got the
  sign right on every claim and the *magnitude* of its headline wrong by a factor of six, and two
  of its six predictions were ranges wide enough to be free. **§7 exists to list the four things
  it did not anticipate at all**, because a prediction table with no misses is usually measuring
  the predictor's caution rather than its insight.
- **-90(vii) NEVER NAME A SCRATCH SCRIPT AFTER A STDLIB MODULE.** A throwaway `enum.py` broke every
  `python3` call in that directory, including `import json`, and the traceback reads like a
  corrupted interpreter. Rename; do not debug.
---
## TOOLING (▲ new at -90)
- ▲ `docs/pointer-groundtruth-I-II.tsv` — **88 rows**, keyed `(file, line, token, target)`, unique
  and fully recomputable, pinned to `83db4d5`. Columns: label · confidence (FIRM/SOFT) · one-line
  reason. 7 POINTER (4 FIRM, 3 SOFT), 9 SOFT NOT-POINTER. Its header **discloses the one
  contamination the labeller could not undo** rather than claiming an independence it does not
  have. Sister file to `docs/pointer-groundtruth.tsv`; together they are **429 labelled rows across
  four manuscripts**, which is the first thing a second human reader has ever had to disagree with.
- ▲ `scripts/wt169_pointer_groundtruth_heldout.py` — `--json`, `--skip-postconditions`. Imports
  wt166's candidates AND word lists by module import; **`G8` hashes all five lists**; **refuses
  (exit 2) on a single row of key-set drift**, and `G5` proves that guard is not vacuous.
  Recomputes Papers III and IV in the same process, so the cross-corpus table is measured.
  17 post-conditions, 6 NEGATIVE. Adding a corpus is: a TSV, a `PAPERS` list, and a `REV`.
- ▲ `docs/REVIEW-030-held-out-pointer-test.md` — §§1–3 the prediction (a git object at `cd46d3d`),
  §4 the measurement, §4.1 the word-class finding, §4.2 the arithmetic, §4.3 the LOOSE surprise
  failing to reproduce, §5.1 the seven unrepaired pointers, §5.2 two new N1–N6 gaps, §6 both
  predictions marked, §7 the four things -90 did not anticipate, §8 six falsifiers, §9 what closes.
- ⚠ `reg013_citation_whitespace.py` takes ~5 min and can 429 — never in a critical path.
  **Tags run to `wt169`; `wt170` is free.**
---
## ESTATE
Two new cards, both with named falsifiers and a DONE-WHEN: **`1217629169253037`** (the seven
unrepaired bare pointers in Papers I and II) and **`1217629264134185`** (the two new N1–N6 gaps).
Carried: `1217603625863293` (two instances), `1217613775009402`, `1217568297674954`,
`1217568192511533`, `1217596263441666`, `1217596233063153`, `1217561667484767`,
`1217593142996092`.
## JASON-SIZED, not -91's
(a) **The two-independent-readers design** — and it is now cheap in a way it has never been: 429
labelled rows exist, each carrying its own one-line reason, so a second reader's disagreement is a
diff rather than an argument. -90's own disclosed contamination (§8 falsifier 1) is a live example
of why one reader building, predicting and scoring his own instrument is fallible. (b) the version
stamp — **TWELVE passes have declined to move it**; (c) the four-vs-three ruling, folded into the
RESULT-001 in-place-edit card; (d) DECISION-001 closed, ROADS-001 unchanged; (e) `wt077` already
prints r·E[η⁺]/(1+μ), matching to 0.44% where Paper II §3.1's form is off 4–7% — changes a stated
contribution, unassigned since -81; (f) the PAN history purge; (g) `lessons.py`'s contributor
stamp, now three sessions running.
---
## WHICH OPEN LANE THIS WAS (the gate's CONTOUR question, answered)
`docs/CHECKLIST.md`'s first OPEN lane in dependency order is **P13** (the arXiv-ready PDF) and this
pass did not touch it. That is deliberate drift and it is **guard work**, so per the gate's own
instruction: **the claim the guard protects is P7's.**
P7 closes a paper when two consecutive fresh-eyes passes yield zero substantive findings — evidence
only if the checks that found nothing were *capable* of finding something. -83 found a row that had
checked the wrong artefact; -84 measured the rate at 5 of 12; -85 put a floor of 25 of 129 under
it; -86 established that 46 rows could not have been re-checked by anyone; -87 showed a pointer
naming no artefact was invisible to every sweep; -88 showed the sweeps that see pointers see them
through a word list; -89 showed no verb-free structural test recovers the class on the corpus it
was built against. **-90 answers the one question -89 could not: the single artefact that looked
usable was fitted, and on held-out text it is worse than chance.** So P7's bar cannot be met by any
instrument this programme can build for this class — and that finding is now *measured on text the
instrument never saw*, which is the only form of it a referee would accept. **A human second reader
is the only remaining instrument, and for the first time there are 429 committed rows for that
reader to disagree with.**
**And a note -91 should not skip: this is the FOURTH consecutive pass of guard work, and the next
at-bat is deliberately NOT guard work.** Widening `#scope` to Paper II is P-line work on a shipping
paper. The pointer programme has reached its own conclusion; going round it again would be the
drift `docs/CHECKLIST.md`'s contour section was written to name.
---
## THE SELF-REVIEW TRIAD, ANSWERED IN WRITING (gate v2.60, G-A / G-B / G-G)
**1 · Did we capture everything for a zero-memory future Opus?** Yes, and the test is that every
claim here has a command beside it — plus the thing this pass adds: **the result is now a
CROSS-CORPUS table computed in one process, so a successor does not have to trust either review.**
`wt169` recomputes Papers III and IV rather than quoting REVIEW-029, and `G8` hashes the word lists
so the comparison cannot silently drift. **Undo path:** nothing in either manuscript was touched,
so there is nothing to undo in the corpus; every step is a separate commit, and reverting the last
one leaves the labels, the scorer and the prediction standing — which is exactly the order that
makes the chain checkable. The one place a successor must be careful is `wt169`'s revision pin,
which is **inert until somebody repairs Papers I or II** — disclosed as falsifier 4 rather than
dressed up as a working guard.
**2 · What did we learn the hard way that is not yet written down?** All seven are banked in
`claude-blackbook` (six global, one project-scoped, all stamped `--contributor
big-wealthTensor-90`) and restated as **-90(i)–(vii)** above. **And one stale leaf was CURATED
rather than left standing:** -89's `only-usable-pre-filter-bare-pointer` led with "the only usable
pre-filter … is the document-noun test"; it now leads with the collapse, credits -89's warning as
right, and withdraws its own recommendation. The two that cost the most: **a scratch file named
`enum.py`**, and the realisation while writing §8 that **reading the instrument before the corpus
had already happened and could only be disclosed.**
**3 · What ONE thing makes the next Opus's life easier, and did we add it THIS pass?** Added, this
pass: **a held-out corpus with a scorer that refuses to run against it if either drifts.** Before
today every claim about this class was measured on the text it was tuned on. Now there is a second
labelled corpus, a scorer that imports the first instrument rather than reimplementing it, and a
hash guard that fails the run if anyone re-tunes a word list to rescue a result. And the honest
half: **-90's own headline prediction was right about the sign and wrong about the size by a
factor of six**, §6 grades it as a poorly-calibrated hit rather than a win, and §7 lists four
results it did not anticipate at all.
---
## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-91` immediately before the gate — **that argument is
YOUR OWN session id, not your successor's.** -90 read the charter under `wealthTensor-91`,
which stamps the ledger for a session that does not exist yet, and `G-AL` failed with
*"wealthTensor-90 never read its charter this session"*. Ten seconds to fix, and it looks
like a broken gate rather than a typo; gate detached **with**
`GATE_ROSTER_WHO`; pytest **AND SAY THE NUMBER**; wt148 AND wt133 AND wt154 AND wt156 AND wt160
AND wt163 AND wt166 AND wt169 **AND SAY ALL EIGHT RCs**; `roster leave --who` once; paste a handoff
better than this one as the last act — and assign -92 **ONE** at-bat with a definition of done. Do
not hand them a menu. 🥎
