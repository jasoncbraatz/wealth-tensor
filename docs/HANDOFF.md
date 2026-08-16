---
project: wealth-tensor
gh_sha: 4570085ce41b2dcdaa0c2f8a0bc2633bf01f0b47
updated: 2026-08-16
session: wealthTensor-58
gate_passed: false
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16, superseding the 'three preprints publicly posted' line carried since sessionZero): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF

`gh_sha` names the commit this file describes; **the only thing added after it is this file**, so
`python3 scripts/handoff_gate.py --check` prints `ADVISORY: docs-only drift` and exits 0. Assert the
exit code exactly. **`| tail` MASKS `$?` ON EVERY `dx` CALL** — `cmd; echo rc=$?` with no pipe, or
you are reading `tail`'s status. `gh_sha` is the full SHA from `git rev-parse`, never an expanded
abbreviation.
> ⚠ **`gate_passed: false`, for the SECOND CONSECUTIVE SESSION AND THE SAME TWO FILES — read this
> before you judge it.** Every repo `-58` touched — `wealth-tensor`, `claude-blackbook`,
> `darwin-mac-ops` — is **committed AND pushed, tree clean.** The gate FAILs on `~/Scripts DIRTY(2)`:
> `braatz-crawl-check.py` and `serve-braatz-archive.py`, untracked, belonging to
> **`big_worker-braatzArchive`, which was still ACTIVE 1h56m in at my wrap**, in a repo that sibling
> has not roster-claimed. The gate's only exits there are committing a live sibling's half-finished
> work or lying. `-57` did neither; `-58` did neither; the cost is now **measured** rather than
> predicted and is appended to card `1217526943288480` with the cheapest honest fix (catch it at
> WRITE time, not at GATE time — upstream of `#22c` entirely). **Verify it yourself before you
> inherit the claim** — `~/Scripts/roster who` and `cd ~/Scripts && git status`.
---
## 0 · THE ONE THING THAT IS PERISHABLE, AND IT IS YOURS TO SPEND OR BURN
**`E2` IS THE LAST TEST LEG THAT CAN STILL BE RUN BLIND, AND YOU BURN IT BY READING ONE FILE
END TO END.** `-56` and `-57` are disqualified: §6 of `END-TO-END-001` says *"read this file end to
end before touching anything"* and §4.2 says a run that reads §2/E2's candidate before extracting
**has destroyed the leg and must say so.** `-58` proved the eligibility is **preservable**: it read
lines **1–204 and 241–505** and stopped dead at the `### E2` heading, and it never saw the candidate.
**Do the same thing, in your first minute, before anything else can tempt you** — the protocol is
`docs/RESULT-END-TO-END-001-E5.md` §6, and §2.7 of `RESULT-…-E3.md` is why it matters.
Read the file in **two slices** (`sed -n '1,204p'` and `sed -n '241,505p'`). Never `Read` it whole.
---
## ORIENT — read these first, in this order
1. **§0 above. Before anything.** It is one `sed` command and it is not recoverable afterwards.
2. **`docs/RESULT-END-TO-END-001-E5.md`** — **NEW, `-58`'s, and it is the one result in this project
   that reports its own finding being destroyed.** §2.3 (the three grounds the refuter won on) is the
   most useful page in the document; §3.3 is the leg's actual result; §4 is the admission accounting;
   §6 is the `E2` protocol above.
3. **`docs/RESULT-END-TO-END-001-E3.md`** (`-57`) and **`-E1.md`** (`-56`) — the two legs that FAILED
   and the reason `T` is 2.
4. **`docs/END-TO-END-001.md`** — the registration. **FIXED. May not be edited in response to a
   result. NOW 0-FOR-5 ON ITS OWN PROSE (§3.3 of the E5 result).** ⚠ **§0 above governs how you read
   it.**
5. **`docs/CHECKLIST.md`** — 66 criteria. `./scripts/regen-board.sh`, never `board.py` by hand.
   `P11a`/`P11c`/`P11e` green; `P11b`/`P11d`/`P11f`/`P11g` red and correctly so.
6. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS.**
   `~/Scripts/charter-read.sh wealthTensor-<NN>` — POSITIONAL slug. **Re-stamp IMMEDIATELY BEFORE
   THE GATE**, always. (`G-AL`'s remedy line finally prints a runnable command — `-58` fixed it.)
7. **`docs/REVIEW-004-pre-posting-dossier.md`** — **now right FIVE times.** Its A3 predicted E5's
   count limb four days early, in one bullet, with the repair spelled out, and **nobody had applied
   it** — `-58` did. **Assume it contains the answer to whatever you are about to derive, and check
   whether anyone has actually acted on it.** `docs/ROADS-001` is its sibling and **still unruled**.
8. `docs/adr/ADR-001` (title and §Decision frozen) · `scripts/gen_apparatus_rows.py`'s docstring
   before touching any apparatus row · `scripts/add_p11_rows.py` + `scripts/redproof_p11.py` before
   any `P11` row · `scripts/redproof_apparatus.py` · **NEW:** `tests/test_paper_test_counts_are_derived.py`
   + `scripts/redproof_paper_counts.py` before touching a quoted test count in any paper.
9. REG-013 + `RESULT-REG-013` §4.1 · REG-003 §§3.2/3.3/7 · SCOUT-001 · REG-012 §§6–7 ·
   RESULT-TERM-001/002 · REG-010 §1/§4 · CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (HEADER NOTE
   FIRST).
---
## `-58` in one line
**THE RUN BUILT A CORPUS-LEVEL FINDING, HAD IT BUILT AGAIN INDEPENDENTLY AND CONFIRMED, THEN AIMED A
REFUTER AT IT AND LOST — AND THE REFUTER WAS RIGHT.** `E5` asked whether one shared test holds two
claims that can come apart. It does not: the multiplicity of the two cross-cited guards is
**bibliographic, not load-bearing**, and every come-apart the run exhibited was demonstrable **inside
one paper**, which `END-TO-END-001` §1.1 demotes to `P7`. What did not survive the afternoon is the
**instrument**: E5's FAILURE clause asks whether a count *moves*, its REFUTATION clause asks whether
every count is *module-scoped*, and Paper III's is **suite-scoped and commit-pinned** — so it neither
moves nor refutes, and E5 declares no UNDECIDED region. **`E5` returns UNDECIDED, on the registration
rather than on the corpus. `T` remains 2. THE SYSTEM FAILS still stands, on `E1` and `E3`.**
---
## 1 · WHAT HAPPENED
### The leg
Quotation, one `git ls-tree`, one adversarial pass. No code against `src/`, no seeds.
**Built twice, then attacked.** The guard→claim map was built by the run and again by an independent
reader given the four manuscripts, both test sources and a four-way taxonomy (CODE / PROSE /
CHARACTER / POINTER) and **no knowledge of the run's direction**. The two builds agreed on every row.
A third reader, told to REFUTE and to default to REFUTED, killed the cell in one pass. **Two agreeing
builders are not a check — they share the framing.**
**The three grounds it won on**, all in `RESULT-…-E5.md` §2.3:
1. **§1.1.** Both come-apart demonstrations are single-paper operations — *"edit Paper IV §5, run
   Paper IV's test"*. And **Paper IV states the mechanism in its own body**: §5 says the suite asserts
   *the monotonicity* and the limit is carried *"under the name"*. §5-vs-§10 inside one document is
   the most ordinary single-paper review move there is.
2. **The corpus publishes the run's own thesis in the cross-citing sentence.** Paper III §11 opens:
   ***"Two tests are worth naming because of what they forbid rather than what they check."***
3. **The run quoted Paper II with its scope clause removed.** Not *"any simplification fails"* —
   *"fails … **instead of quietly re-scoring condensation as success**"*, and the exhibited rewrite
   does not re-score condensation as success. And Paper II §3.4 **names a conjunction** (*"a settled
   Gini **and** a top decile below 0.90"*), which is E5's refuting disjunct verbatim.
### What is verified that never was
**The suite at `d655501` holds exactly 100 tests** — Paper III's number, right since 2026-08-05 and
checked for the first time on 2026-08-16. Its decomposition is the interesting part:
| module at `d655501` | tests | whose claims |
|---|---|---|
| `test_edgar.py` · `test_lag.py` · `test_lambda_sensitivity.py` | **62** | **Paper III** |
| `test_redistribution.py` | **18** | **Paper II** |
| `test_cournot.py` · `test_excess_demand.py` | **20** | **Paper I — WITHDRAWN** |
### The repairs, and what they are owed to
**None of these is an E5 remedy** — E5 did not fail, and *applying a remedy whose antecedent did not
occur is re-choosing a fixed clause in the direction the run prefers* (`-57`'s ruling, and it binds).
- **Paper III §11's count**, re-scoped into Paper II's template — **`REVIEW-004` A3's own
  prescription**, four days stale, applied verbatim.
- **Paper II §1's *"18 tests including two…"*** — false; only **one** of the two is in the counted
  module, the other is in `tests/test_excess_demand.py`. **Bug spray.** The abstract was not touched.
- **`tests/test_paper_test_counts_are_derived.py`** — every quoted count derived from `git` at each
  paper's pin **and from the live tree** for Paper II's 18, which is the one that can move. 6 tests,
  5 mutations, 5 red, 0 survivors (`scripts/redproof_paper_counts.py`).
- **`G-AL`'s remedy line**, carried four sessions, now prints a command that runs.
### Counts, and the numbers
**TEST legs run 3 · FAILED 2 · UNDECIDED 1. AUDIT legs run 0. No combined score exists and none is
offered.**
| | |
|---|---|
| suite | **1074 passed**, ~68 s, **zero skips** (was 1068; +6) |
| red-proof (apparatus) | **37 mutations, 0 survivors, 2 skipped** — baseline held |
| red-proof (`P11`) | **3 proven by mutation, 4 red on their own, 0 WEAK** |
| red-proof (paper counts) | **5 mutations, 5 red, 0 survivors**, artefacts SHA-256 restored |
| board | 66 criteria, `P11e` green |
| lessons | **5 banked** (4 global, 1 project) · 2 `use` + 1 `record-outcome pass` |
| commits | `944e58e` the leg · `bde6d65` the repairs · `4570085` the board · darwin-mac-ops `G-AL` |
---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-57`'s rulings stand verbatim**, including: `END-TO-END-001` IS FIXED AND
  MAY NOT BE EDITED IN RESPONSE TO A RESULT; A LEG MAY NOT COUNT A FINDING MADE BEFORE IT EXISTED;
  TEST AND AUDIT COUNTS ARE REPORTED SEPARATELY; **THE ADMISSION CRITERION IS NOT ADVISORY**; DO NOT
  ADD AN OBSERVABLE TO A LEG'S OWN FAILURE CRITERION; REG-013's DECISION RULE IS SPENT; H1 LICENSES
  OCCUPANCY; `P2`/`P3`/`P5` STAY MANUAL; ADR-001's TITLE AND §Decision FROZEN; THE ABSTRACT IS A
  SUBMISSION FIELD; THE ARM IS δ; DO NOT SPEND THE TIE-BREAK; **R5 IS UNSPENT**; T4's WIDTH IS
  31.7 %; **T2 MAY NOT BE RUN ON THIS DATA**; §4.7 IS PINNED AT `ba59370`; `wt107` IS NOT EDITED;
  APPARATUS SUB-ROWS ARE GENERATED; A ROW IS NOT DONE UNTIL SEEN RED; `P8` IS ONE PASS TAKEN LAST;
  `P7` DOES NOT CLOSE THE CORPUS; DONE IS "CLEARED FOR LIFTOFF"; **`P13` IS LAST** AND IS A PDF *AND
  A RECIPE*; ROW IDS ARE NEVER RENUMBERED; **DO NOT EDIT `src/`**; `T = 2`, **THE SYSTEM FAILS**, AND
  `T` CAN RISE AND CANNOT FALL; THE `T ≥ 2` REMEDIES ARE ALL FOUR SPENT; ADR-001 §Consequences'
  CONTAINMENT SENTENCE IS NOT RETRACTED.
- **NEW · `E5` IS SPENT AND ITS ANSWER IS UNDECIDED.** Do not re-run it; do not apply its
  pre-registered repairs; do not split a guard or re-scope a count *as an E5 remedy*. A leg that
  returns UNDECIDED has been RUN. `P11e` is green because the verdict is recorded, not because it
  passed.
- **NEW · THE MULTIPLICITY OF THE TWO CROSS-CITED GUARDS IS BIBLIOGRAPHIC, NOT LOAD-BEARING.** Paper
  IV contributes no computation and has no saturating statistic; Paper III merely reports that
  *companion modules* carry the SMD guard. Neither guard bears two loads. That is `-58`'s judgement,
  stated as such, and it is **not** the registration's verdict — do not cite it as one.
- **NEW · `END-TO-END-001`'s PROSE ABOUT ITSELF IS 0-FOR-5, AND THAT IS NOW A STANDING EXPECTATION,
  NOT A RUNNING JOKE.** §0's *"no written answer anywhere"* · E1's audit-half *"no document mentions
  it"* · §2.0's three-and-three against four-and-two · §4.2-versus-§6 on `E2` · E5's
  non-complementary clauses. **Every leg from here checks the registration's own tallies, lists and
  instructions before it checks the corpus**, because that is where five for five have been.
- **NEW · A FINDING IS NOT WRITTEN UP UNTIL A REFUTER HAS FAILED TO KILL IT.** Order is
  **build → build independently → REFUTE → write.** `-57` refuted after writing and survived; `-58`
  refuted after writing and did not, and had to unwrite. A written-up finding acquires sunk cost the
  moment it has section numbers.
---
## 3 · THE AT-BAT for `-59` — **`E2`, BLIND, AND IT IS THE ONLY ITEM WITH A DEADLINE**
Read §0. Do the two-slice read in your first minute. Then run the leg to §2/E2's criterion, and say
in your result **where you stopped reading and when**.
Why it is first even though the verdict cannot improve: `DO NOT SKIP A LEG BECAUSE THE VERDICT CANNOT
IMPROVE` is a standing ruling, `E2` is the **last TEST leg**, and it is the only artefact in the
project that a careless first ten minutes destroys permanently. Three sessions have now had the
chance; one has preserved it.
**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The honest alternatives, ranked:
- **`E4`** (AUDIT) — remedy is one pre-registered sentence in Paper IV; its near-miss is already
  measured in `RESULT-…-E3.md` §5, so most of the reading is done.
- **`E6`** (AUDIT) — its worked example is excluded from its own run; read the leg's own note first.
- **`P11g`** — the pass-level `docs/RESULT-END-TO-END-001.md`, which **does not exist** and is the
  one artefact the whole pass is for. It cannot be honest until `E2`, `E4` and `E6` have run.
- **`P7` on Paper III §11 and Paper II §1** — `-58` rewrote both and **must not also score them**.
- **`P7` on Paper IV**, §3 and the abstract — `-56`'s and `-57`'s prose in the paper's most
  load-bearing places, and the objection that a leg might reopen it is **spent**.
- **`P6`'s remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
- **Rule on `REVIEW-004` A2 / `ROADS-001`** — see §4. **Five sessions carrying it.**
- **`P13`. STILL LAST**, and its subject matter is decided: three works, not one stack.
---
## 4 · TEED UP, IN ORDER
- **`REVIEW-004` A2 AND `ROADS-001` ARE STILL UNRULED — FIVE SESSIONS NOW.** A2 calls Paper II's
  title claim fatally refuted by its own table; Road One is the re-cut that follows. **The one-page
  "here is what A2 costs and what Road One buys" that turns it into a five-minute Jason decision has
  still not been written by anybody, and it is Claude-sized.** Writing it is a better use of an
  hour than another audit leg, and no session has taken it.
- **PAPER IV'S TITLE IS ONE STEP AHEAD OF ITS OWN NARROWED ABSTRACT** — *"one atomic unit from the
  household to the sovereign"* against an abstract that now says the scales share a question and not
  a structure. Same defect A2 found in Paper II's title. Jason-sized, teed up, not taken.
- **A ROSTER CLAIM APPEARED UNDER `-58`'s NAME THAT `-58` DID NOT MAKE** — resource `synthetic`, task
  *"amend the registration after its result"* (a wealth-tensor **tripwire phrase**), and that string
  exists **nowhere on disk** in `~/Scripts`, `done-criteria.tsv`, `.git/hooks` or `darwin-mac-ops`.
  Released cleanly. **This is the FOURTH coat of the identity bug** (`G-T` calls a STALE claim LIVE ·
  the roster cannot tell a GHOST from a sibling · the brake cannot tell YOU from a sibling) and the
  sharpest, because the board **invented a row**. Also a correction worth as much as the bug:
  **`~/.local/state/claude-session/current` DOES NOT EXIST** — that directory holds one `.log` per
  session, so `-57`'s teed-up guess names the wrong site. All evidence in card `1217527629536618`;
  start there, not at zero.
- **`G-H#22c` ATTRIBUTES BY EXACT SUBSTRING**; normalising both sides widens a downgrade path and
  needs its own at-bat and drill case. Carded `1217526943288480`.
- **`~/Scripts/gate-selfcheck.sh` IS A SYMLINK INTO `~/code/darwin-mac-ops`.** `git add` in
  `~/Scripts` stages nothing **and reports success.**
- **`~/Scripts` may still be `DIRTY(2)`** with a sibling's untracked files (`braatz-crawl-check.py`,
  `serve-braatz-archive.py`, `big_worker-braatzArchive`). Verify with `roster who` before you inherit
  anyone's claim about it. Carded `1217526943288480`.
- **`lessons.py record-outcome` EDITS A LEAF AND DOES NOT AUTO-COMMIT** (unlike `add` and `use`), so
  it leaves the blackbook dirty. `-57`'s warning earned its keep in `-58`; the fix — make
  `record-outcome` commit like its siblings — is one function and nobody has taken it.
- **`P1n` and `P5n`** — `P3n` repointed. Half an hour, moves `P6`.
- **The use/mention guard, generalised.** Applied in exactly one place.
- **C26 limb B** — carded `1217525563299334`. **RESULT-REG-003 §2's "Every cut lands in R1"** —
  carded `1217518687033967`.
- **Cell (b), ranked in §3.2 — THREE entries left**, measured, paused behind the papers.
- **C37's tripwire** — REG-009 §12's "never by narration". **§7's ledger dilutes its own two
  load-bearing rows** — Jason's call, TRIPWIRED not carded.
- **Dossier era, re-served by nobody:** `REVIEW-004` C6 (ASC 410) and C10 (IAS 36's reversal
  asymmetry). *C10 is `REVIEW-004`'s, not the inventory's; the collision has bitten three times.*
- **REG-013 re-run worth doing:** the biophysical audience was capped at 4 000 of 7 801.
- Infra siblings, carded: Caddy `1217488447555628` · capability path `1217488117177482` ·
  AAR A2's four post-\* hooks · card-lint `1217483699706758` · gate `1217465036940491`.
---
## 5 · DO NOT
- **Everything `-31`→`-57` forbade still stands verbatim** — R5, the two sensitivities,
  `selected_lives`, §4.4's 0.3000, T4's 31.7 %, the δ arm, TERM-001/002, §9's list well-formedness,
  `wt107` IS NOT EDITED, §4.7 IS PINNED AT `ba59370`, DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD, DO
  NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION, DO NOT GRADE A CONSTRAINT FROM THE
  `machine` COLUMN, DO NOT WIDEN C07's GUARD, DO NOT WRITE AN OVER-BREADTH SELF-TEST WITH AN ABSENCE
  PREDICATE, DO NOT SLICE THE SWEEP LOG BY SLUG, DO NOT TYPE A FULL SHA YOU HAVE NOT RESOLVED, DO NOT
  LEAVE A FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT CORRECTS, DO NOT MEASURE A TEXT LENGTH
  WITH `wc -w`, DO NOT LET A `manual:` ROW BE SCORED BY WHOEVER DID THE WORK, DO NOT RUN `board.py`
  BY HAND, DO NOT HAND-EDIT A `P1x`/`P3x`/`P5x` ROW, DO NOT TRUST A GREEN CLONE, DO NOT "STRENGTHEN"
  A CHECK A MUTATION HARNESS CALLED WEAK, DO NOT EDIT `src/`, DO NOT `--no-verify` PAST
  `roster-brake`, DO NOT RE-RUN A LEG THAT HAS RUN, DO NOT RE-APPLY A SPENT REMEDY, DO NOT READ "THE
  SYSTEM FAILS" AS "THE PAPERS ARE WRONG", DO NOT SKIP A LEG BECAUSE THE VERDICT CANNOT IMPROVE, DO
  NOT WRITE A SCRATCH SCRIPT INTO A REPO ROOT.
- **NEW · DO NOT READ `docs/END-TO-END-001.md` END TO END.** §6 tells you to and §4.2 says it
  destroys `E2`. Two slices: `sed -n '1,204p'` and `sed -n '241,505p'`. **This is the single
  cheapest, most irreversible mistake available in this project right now.**
- **NEW · DO NOT QUOTE A SENTENCE INTO A FINDING WITHOUT ITS TRAILING SCOPE CLAUSE.** The clause a
  summariser drops first is the clause a refuter reaches for first, and it killed `-58`'s second
  limb. Paste the whole sentence, then build the counterexample.
- **NEW · DO NOT TREAT TWO AGREEING INDEPENDENT BUILDS AS A CHECK.** They share the framing, so they
  can only disagree about the evidence — the thing they were least likely to get wrong.
- **NEW · DO NOT REPAIR A WRONG NUMBER WITH A RIGHT NUMBER.** `REVIEW-004` A3 gave the corpus the
  correct sentence on 2026-08-12 and the defect was still there on 2026-08-16, nine times larger,
  because the suite kept growing while the prose stood still. **The deliverable for a wrong number is
  a derivation.**
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe with `while pgrep`. **Do not edit shared infra a sibling is mid-edit on.**
---
## 6 · TRANSPORT — darlish, zero-bridge (worked first try, `-06` → `-58`)
Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. **Never restart the app to fix darlish.** `darlish-check` is not in
the cloud kit; do not chase its 127.
- ⚠ **`dx` RUNS AS `root` IN THE CLOUD CONTAINER, SO `~` IS `/root` AND FILES YOU `--get` LAND OUTSIDE
  `/home/claude` WHERE THE `Read` TOOL LIVES.** `-58` lost a round trip to it. `--get` into an
  absolute path under `/home/claude`, or `cp -r /root/wt/. /home/claude/wt/` after each batch.
- ⚠ **RUN `roster join --who <you>` AT STUDENT-IN, BEFORE `roster claim`.** `dx` resolves you as
  `cloud-<random>`; `join` **absorbs** those rows into your name. `lessons.py` wants the same call or
  a banked leaf carries no contributor stamp. `roster leave --who <you>` ONCE at wrap.
- ⚠ **`roster claim` TAKES `--resource`, NOT `--repo`.** Two seconds, but it exits 2.
- ⚠ **`ROSTER_BRAKE_ACK=<staged count>` IS THE HONEST EXIT** when your staged set covers the whole
  dirty tree and you verified the tree was EMPTY at your student-in. Reason in the commit message.
- ⚠ **A ROSTER CLAIM CAN BE A GHOST**: `git status` empty **and** `HEAD` is the claimer's own wrap
  commit **and** the roster task string is its handoff line. Two of three is not the test.
- ⚠ **`| tail` MASKS `$?` ON EVERY `dx` CALL.** No pipe when you need the code.
- ⚠ **HEREDOCS DIE INSIDE THE `dx '...'` ARGUMENT.** Write locally, `--put`, run with `bash`. A
  heredoc **inside** a `--put` script is fine and is how every multi-step edit in `-56`, `-57` and
  `-58` shipped — including a commit script carrying three multi-paragraph messages.
- ⚠ **NON-ASCII IN A `--put` SCRIPT: WRITE THE LITERAL CHARACTER.**
- ⚠ **`--get` NEEDS THE FULL PATH; a leading `~` expands in the CLOUD and fails.** `--put` accepts
  `~`. **Staging the papers into the cloud with `--get` and reading them there is much cheaper than
  grepping them over `dx`** — and it is what lets you hand a subagent the manuscripts.
- ⚠ **`lessons.py add`/`use` AUTO-COMMIT AND AUTO-PUSH; `record-outcome` DOES NOT.** Check
  `git status` in the blackbook at wrap, every time.
- ⚠ **`gate-selfcheck.sh` TAKES ~5–6 MINUTES AND A FOREGROUND `Bash` CALL DIES AT 8m20s.** Detach:
  `nohup env GATE_ROSTER_WHO=big-<sess> bash -c "$HOME/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1" &`
  then `sleep 340; grep -E "GATE SELF-CHECK|^  FAIL" /tmp/gate.log`. **COMMIT EVERYTHING FIRST** and
  **re-stamp the charter immediately before it.**
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started ·
  `5` crossed but mismatched.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
**SUITE:** 1074 collected, 1074 passed, zero skips — darwin ~68 s, cloud ~180 s.
`check_abstract_size.py` **is silent on failure — use `--print`.** `defensive_count.py` takes a
positional path and **only a DELTA means anything**. **`redproof_apparatus.py`'s SKIPPED COUNT IS A
SIGNAL: 2 is the baseline.**
---
## 0' · THE TELL, NOW IN NINETY-TWO SHAPES
`-28` through `-57`'s tells all stand (the instrument-artefact question; a guard must scan assertions
not quotations; a mutation that does not mutate reports your guard as weak; pre-commit the FAVOURABLE
outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT; a correction that lives only in
a handoff has not been made; a rule can be false on the day it is written; a criterion that passes
because it does not apply is a blank line wearing a tick; a system of documents can hold a
contradiction no per-document review can find; a claim nothing depends on is not a claim nothing can
break; a disclaimer that covers the evidence does not cover the assertion; a withdrawal applied to
the documents that ARGUE for a claim will miss the one that merely MENTIONS it; a registration is an
instrument and nobody has ever pointed an instrument at it). `-58` adds four:
- **A CRITERION'S FAILURE CLAUSE AND ITS REFUTATION CLAUSE ARE TWO DIFFERENT PREDICATES, AND NOTHING
  MAKES THEM COMPLEMENTS EXCEPT SOMEONE CHECKING.** They are written minutes apart, in the same
  voice, about the same object, and they read as each other's negation. E5's are not: one asks
  whether a number *moves*, the other whether it is *module-scoped*. Write both, then name the region
  between them **in the same commit** — §5 will forbid you adding it later.
- **TWO INDEPENDENT BUILDS THAT AGREE HAVE CHECKED THE EVIDENCE AND NOT THE FRAME.** Give them the
  same taxonomy and the same question and they will converge on the same wrong thing, confidently and
  in the same words. Only a reader whose *job* is the opposite conclusion tests the frame — and the
  cost of finding out afterwards is a rewrite, so refute **before** you write.
- **THE CLAUSE THAT NARROWS A CLAIM IS THE CLAUSE YOUR SUMMARY DROPS AND YOUR REFUTER FINDS.**
  *"…fails loudly"* and *"…fails loudly **instead of quietly re-scoring condensation as success**"*
  are different claims, and only one of them was refutable. Quote the whole sentence into the finding
  before you build the state of the world that breaks it.
- **A DOSSIER FINDING WITH A STATED REMEDY AND NO INSTRUMENT WILL BE RE-FOUND, LARGER.** `REVIEW-004`
  wrote the correct sentence on 2026-08-12 and named the three numbers. Four days later nothing was
  fixed and the gap had grown ninefold, because prose is a snapshot and the suite is a process. **The
  deliverable for a wrong number is a derivation, not a corrected number** — a corrected number is
  the same defect with a later timestamp.
---
## 7 · ORIENT-THEN-GO
**Read §0 first.** Then emit one line — `Oriented: <state> · at-bat: <X> · opening with <first
action>.` — and start building. Don't wait for a go. Do not open by asking Jason anything.
**Coffee status:** ☕ TWENTY-FOUR SESSIONS. `-56` found the fact that killed `E1` four days stale in a
dossier. `-57` found the sentence that killed `E3` four words long in an appendix. `-58` went looking
for the same shape a third time, found it, watched an independent reader confirm it, and then watched
a refuter take it apart in one pass — **and the afternoon's real yield came from the machine that
destroyed the finding, not the one that built it.** The registration is now 0-for-5 on its own prose
and 5-for-5 on the corpus's, which is a strange and rather beautiful thing for a document to be.
Papers II and III are untouched and ship. Paper IV is a survey, a measured whitespace and one worked
instance. **One leg can still lose, exactly once, and only if you read the file in two slices.** 🥎
