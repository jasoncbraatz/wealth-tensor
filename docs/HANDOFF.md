---
project: wealth-tensor
gh_sha: 6f7bb410c22919f3d9fcd7a12e44d3583b3bdacc
updated: 2026-08-16
session: wealthTensor-57
gate_passed: false
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16, superseding the 'three preprints publicly posted' line carried since sessionZero): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF
`gh_sha` names the commit this file describes; **the only thing added after it is this file**, so
`--check` prints `ADVISORY: docs-only drift` and exits 0. Assert the exit code exactly (`-39`);
`| tail` masks it — **and `| tail` masks `$?` on EVERY `dx` call, which cost `-57` two round trips.
`cmd; echo rc=$?` with no pipe, or you are reading `tail`'s status.**
`gh_sha` is the full SHA from `git rev-parse`, not an expanded abbreviation.

> ⚠ **`gate_passed: false`, and read §6 before you judge it.** Every repo `-57` touched
> — `wealth-tensor`, `claude-blackbook`, `darwin-mac-ops` — is **committed AND pushed, tree clean.**
> The gate FAILs on `~/Scripts DIRTY(2)`: two untracked files that are provably a **live sibling's**
> work-in-flight (`braatz-crawl-check.py`, `serve-braatz-archive.py`, from `big_worker-braatzArchive`),
> in a repo that sibling did not roster-claim. The gate's only exits there are committing someone
> else's half-finished work or lying. `-57` did neither, made the gate **name the paths** so the next
> session spends a glance instead of a round trip, and carded it (`1217526943288480`). **Verify it
> yourself before you inherit the claim** — `~/Scripts/roster who` and `cd ~/Scripts && git status`.
---
## ORIENT — read these first, in this order
1. **`docs/RESULT-END-TO-END-001-E3.md`** — **NEW, `-57`'s deliverable, and it ends the pass's first
   question.** Read §2.3 (the cell that decides it), §2.4 (the counter-reading, because the verdict
   rests on ONE sentence), §2.5 (the three shapes read against the matrix), §3 (the shape, which is
   more useful than the verdict), §4 (admission), §6 (what was applied, and in which direction).
   **§2.7 is a live obligation on whoever runs `E2` — read it before you read anything else.**
2. **`docs/RESULT-END-TO-END-001-E1.md`** — `-56`'s. Still the reason `T` is 2 and not 1.
3. **`docs/END-TO-END-001.md`** — the registration. **FIXED. May not be edited in response to a
   result.** §3's verdict rule now reads against **`T = 2`**, which is its `THE SYSTEM FAILS` branch.
   **DO NOT READ §2/E2 PAST ITS FIRST CHECK PARAGRAPH IF YOU MIGHT RUN `E2`** — §2.7.
4. **`docs/CHECKLIST.md`** — **66 criteria now, not 59.** `./scripts/regen-board.sh`, never
   `board.py` by hand. `P11a`–`P11g` exist and the board can finally show a leg.
5. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS.**
   `~/Scripts/charter-read.sh wealthTensor-<NN>` — POSITIONAL slug. **Re-stamp IMMEDIATELY BEFORE
   THE GATE**, always.
6. **`docs/REVIEW-004-pre-posting-dossier.md` §§E1–E3, A1, A2** — **now right three times and
   INCOMPLETE once**, which is new information about it. Its §E3 mode 3 predicted E3's finding in
   direction (*"cross-references are decorative by design"*) and understated it: three of Paper
   III's four cross-paper sentences are decorative, and the fourth is a claim that broke the leg.
   **Still assume it contains the answer to whatever you are about to derive — and check whether it
   is the whole answer.** `docs/ROADS-001` is its sibling and **still unruled**.
7. `docs/adr/ADR-001` (**two edits by `-57`: a new dated addendum at the foot, and the 2026-08-10
   addendum's §1 dependency-graph sentence amended IN PLACE**; title and §Decision still frozen) ·
   `docs/adr/ADR-002` · `scripts/gen_apparatus_rows.py`'s docstring before touching any apparatus
   row · `scripts/add_p11_rows.py` + `scripts/redproof_p11.py` before touching a `P11` row ·
   `scripts/redproof_apparatus.py` · `python3 scripts/handoff_gate.py --check`.
8. REG-013 + `RESULT-REG-013` §4.1 · REG-003 §§3.2/3.3/7 · SCOUT-001 · REG-012 §§6–7 ·
   RESULT-TERM-001/002 · REG-010 §1/§4 · CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (HEADER NOTE
   FIRST).
---
## `-57` in one line
**THE CORPUS PROMISED ON 2026-08-05 THAT ITS PAPERS HAD NO EDGES AMONG THEM, SPENT FIFTY SESSIONS
NEVER CHECKING, AND THE CHECK TOOK ONE AFTERNOON AND NO CODE.** `E3` FAILS on the second registered
failure shape: striking Paper II removes claims from **both** others. Paper IV's five entries are
declared by its own §9.3; **Paper III's one entry is declared by nothing and denied in terms by
`ADR-001`.** The edge is four words in an italicised appendix aside naming nobody — §A.1.3's *"The
mechanism is the same"* — which is *also* the identification `E1` refuted eight hours earlier and
whose withdrawal named two papers because its author did not know a third copy existed.
**`T = 2`. §3's rule, pre-committed in both directions: THE SYSTEM FAILS.**
---
## 1 · WHAT HAPPENED

### The leg
Quotation only. No code, no seeds, one afternoon. Rows are **Q** (loses claims), columns **P**
(headline assumed false); in II → III → IV order, legitimate load sits **below** the diagonal. The
convention is **not fixed by the design** and had to be derived — it is now in the RESULT doc §1 so
nobody derives it twice.

| Q ↓ · P → | II | III | IV |
|---|---|---|---|
| **II** | — | EMPTY (one *retraction*) | EMPTY (one *apparatus* line) |
| **III** | **1** ⚠ | — | EMPTY |
| **IV** | 5 (declared §9.3) | 3 (declared §9.3) | — |

**Shape 1 (not lower-triangular): NOT met** — every above-diagonal cell is empty. **Shape 3 (all
empirical content in one cell): NOT met** — two cells. **Shape 2: MET.** Refutation also missed, on
the same sentence: the condition is *"only off-diagonal load is the dependency Paper IV §9.3 already
declares"*, and cell (III, II) is off-diagonal load §9.3 says nothing about.

### The cell, and why it survives the best objection
Paper III touches the rest of the corpus **four times in 33,000 words** and **names neither sibling
anywhere**. Three are pointers and apparatus. The fourth:

> *"…is cited rather than reproduced: a levy whose base cannot observe an accrual is inert
> regardless of its rate. **The mechanism is the same** — observability binds before intensity — and
> the evidence for it belongs to that paper."* (§A.1.3, as it stood at `c3b6a9d`)

Because one sentence carried a corpus-level verdict, the cell was **built twice** — once by the run,
once by an independent reader given the manuscripts, the four-way entry taxonomy and no knowledge of
the verdict — and then **attacked by a third reader instructed to refute it**. Both builds call it
load. The refutation returned REFUTED on *"the evidence for it belongs to that paper"* being a
disclaimer of reliance — **and conceded the objection it could not defeat, which is the answer: the
disclaimer covers the EVIDENCE and not the ASSERTION.** *"The mechanism is the same"* is a two-place
relation in Paper III's own voice; assume Paper II's headline false and it is not weakened, it is
unsupported. The full attack and both answers are in RESULT §2.4, because a verdict resting on one
sentence should show its work on that sentence.

Its second attack — *counting row IV makes the criterion fire automatically, so E3 is unfalsifiable*
— **is wrong, and its wrongness is the best evidence the criterion is well aimed.** Had the corpus
been as `ADR-001` describes, striking II would remove claims from IV **only**. Shape 2 fires exactly
and only on an **undeclared II↔III edge**, which is the sentence `ADR-001` denies.

### And a fourth defect in the registration
`-56` found two false premises in `END-TO-END-001`. `-57` found two more, and **neither is about the
corpus**:

- **§2.0 and §4.6 say three TESTs and three AUDITs; the six leg headings say four and two.** Does
  not move `T`. Does mean max `T` is **4**, and the anti-inflation guard overstates by one.
- **§4.2 says a run that reads §2/E2's candidate before extracting has destroyed `E2` and must say
  so. §6 says "read this file end to end before touching anything." §2 contains the candidate.**
  Both `-56` and `-57` followed §6. **Both are disqualified from `E2`'s blind pass and this is the
  run that says so.** RESULT §2.7.

**The class is now stable enough to name: a registration is an instrument, and nobody has ever
pointed an instrument at it.** Four for four, all self-referential, none found by the design.

### Counts, and the numbers
**TEST legs run 2. TEST legs failed 2. AUDIT legs run 0. No combined score exists and none is
offered.** `E3`'s admissible new content is the containment finding and the surviving-copy finding;
the identification's *falsity* is `REVIEW-004` §E2 from 2026-08-12 and **scores nothing**; Paper
III's unnamed sibling citations are `P7` and score nothing.

| | |
|---|---|
| suite | **1068 passed**, ~66 s, zero skips |
| red-proof (apparatus) | **37 mutations, 0 survivors, 2 skipped** — back to `-56`'s baseline after a self-inflicted regression, see §1's next block |
| red-proof (`P11`) | **2 proven by mutation, 5 red on their own, 0 WEAK** |
| board | **66 criteria** (was 59), `P11a`–`P11g` added, `P11a`/`P11c` green |
| lessons | **6 banked** (3 global, 3 project) · 3 `use` + 1 `record-outcome pass` |
| commits | `034031c` the run · `d8ef31a` the remedies · `2b0188e` the board · `60cfb0a` the ADR clause · `6f7bb41` the E2 disclosure · `6a363e7` (darwin-mac-ops) the gate |

### Two things `-57` broke and caught
- **The `T ≥ 2` abstract narrowing was 82 words where the sentence it replaced was 26**, which took
  Paper IV's abstract to 281 against `P5a`'s 150–250 bar — **and took `P5l` down with it, because
  `P5l` runs `P5a`'s check first.** Caught by `redproof_apparatus.py` reporting them *"already red
  unmutated"*: `-56` reported **2 skipped**, a session that reports **4** has broken two rows. Both
  green at 248 words; the narrowing is not withdrawn, it is said in 50 words.
- **The student-in lessons search was run LATE and immediately caught a real error.** Leaf
  `2026-08-15-amendment-recorded-addendum-has-amended-decision` (`-51`, caught by Jason): *an
  amendment recorded as an ADDENDUM has not amended the decision — amend the CLAUSE.* `-57` had
  written the addendum and left `ADR-001`'s false sentence standing. Fixed in `60cfb0a`. **Run the
  search FIRST. It is not ceremony; it is the second-cheapest error detector in the project.**
---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-56`'s rulings stand verbatim**, including: `END-TO-END-001` IS FIXED AND
  MAY NOT BE EDITED IN RESPONSE TO A RESULT; A LEG MAY NOT COUNT A FINDING MADE BEFORE IT EXISTED;
  TEST AND AUDIT COUNTS ARE REPORTED SEPARATELY; THE ADMISSION CRITERION IS NOT ADVISORY; DO NOT ADD
  AN OBSERVABLE TO A LEG'S OWN FAILURE CRITERION; REG-013's DECISION RULE IS SPENT; H1 LICENSES
  OCCUPANCY; `P2`/`P3`/`P5` STAY MANUAL; ADR-001's TITLE AND §Decision FROZEN; THE ABSTRACT IS A
  SUBMISSION FIELD; THE ARM IS δ; DO NOT SPEND THE TIE-BREAK; **R5 IS UNSPENT**; T4's WIDTH IS
  31.7 %; **T2 MAY NOT BE RUN ON THIS DATA**; §4.7 IS PINNED AT `ba59370`; `wt107` IS NOT EDITED;
  APPARATUS SUB-ROWS ARE GENERATED; A ROW IS NOT DONE UNTIL SEEN RED; `P8` IS ONE PASS TAKEN LAST;
  `P7` DOES NOT CLOSE THE CORPUS; DONE IS "CLEARED FOR LIFTOFF"; **`P13` IS LAST**; `P13` IS A PDF
  *AND A RECIPE*; **ROW IDS ARE NEVER RENUMBERED AND FILE ORDER IS DEPENDENCY ORDER**; **DO NOT EDIT
  `src/`** (Paper II §7 pins `d655501`).
- **NEW · `T = 2`. THE SYSTEM FAILS. `T` CAN RISE AND CANNOT FALL, AND NO LATER LEG IMPROVES THE
  VERDICT.** §3's branches are `T = 0`, `T = 1`, `T ≥ 2`. There is no route back.
- **NEW · THE `T ≥ 2` REMEDIES ARE SPENT, ALL FOUR, AND EACH DIRECTION IS ON THE RECORD.** Paper
  IV's abstract narrowed; containment cashed **after** the repair that made it true; `ADR-001`
  addendum written **and its clause amended**; `P13` renders three works — **RECORDED, NOT BUILT.**
  Do not re-apply them and do not re-argue them.
- **NEW · `ADR-001` §Consequences' CONTAINMENT SENTENCE IS NOT RETRACTED, AND THAT IS A RULING, NOT
  AN OVERSIGHT.** `E3`'s remedy retracts it *"if the matrix is a star rather than a stack"*. **It is
  a stack** — Paper IV is a pure sink, the matrix is lower-triangular, and *"a rejection of III no
  longer takes I and II with it"* is **true**. Applying a remedy whose antecedent did not occur is
  re-choosing a fixed clause in the direction the corpus prefers. What was false is `ADR-001`'s
  *stronger* 2026-08-10 sentence, and that is amended in place.
- **NEW · `-56` AND `-57` ARE DISQUALIFIED FROM `E2`'s BLIND PASS.** Both read `END-TO-END-001` end
  to end, which §6 instructs and §4.2 says destroys the leg. A session that wants `E2` must stop
  reading §2/E2 at *"…what a competent economist would now believe"* and say in its result where it
  stopped.
---
## 3 · THE AT-BAT for `-58` — **`E5`, THE OVER-SUBSCRIBED GUARD**
**Ranked first because it is the last cheap TEST leg, and because `-57` already paid for half of
it.** `RESULT-END-TO-END-001-E3.md` §5 carries the quotations, collected while reading and
**counted nowhere** — you inherit them without inheriting a finding you did not make.

- **What is already in hand.** Two tests are named in **all three** papers
  (`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`,
  `test_a_flat_gini_does_not_mean_a_bounded_one`). The three test counts are scoped three different
  ways: Paper II *"the **18** tests in `tests/test_redistribution.py`"* (module-scoped, invariant to
  a sibling), Paper III *"**100 tests at the pinned commit `d655501`** … the suite at the head is
  larger and grows with every registration"* (suite-scoped, pinned, growth disclosed), Paper IV
  none. **Whether either is a FAILURE is `E5`'s to decide and `-57` deliberately did not.**
- **What is NOT in hand, and it is the leg's real work.** The guard → claim map across all three
  papers, and then the discriminating question per multiply-cited guard: **is there a state of the
  world in which claim A is false, claim B true, and the test passes in both?** That is the part a
  per-paper reviewer cannot ask.
- **The repair shape is pre-registered and `P3n` already built it once** — split a two-claim guard
  into two tests and repoint both papers; derive a count, do not assert it.
- **Then `E4`** (AUDIT, remedy is one pre-registered sentence in Paper IV — cheap, and its near-miss
  is already measured in RESULT §5) and **`E6`** (AUDIT, its worked example is excluded from its own
  run). Two AUDITs and one TEST left, plus **`P11g`**, the pass-level `RESULT-END-TO-END-001.md`,
  which does not exist and is the one artefact the whole pass is for.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The honest alternatives:
- **`E2`** — the other TEST, and the one leg a rushed session destroys. **You may be the last
  session that can still run it blind.** Read §2.7 first, then §2/E2's check paragraph and STOP.
- **`P7` on Paper IV, §3 and the abstract.** Both now carry `-56`'s and `-57`'s prose in the paper's
  most load-bearing places, and the abstract was rewritten twice today. Fresh eyes are worth real
  money and the "prose a leg may reopen" objection is **spent** — the `T ≥ 2` remedies are all spent.
- **`P7` on Paper III §A.1.3** — `-57` rewrote it and `-57` should not also score it.
- **`P6`'s remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
- **`P13`. STILL LAST — and its subject matter is now DECIDED.** §3's fourth consequence says three
  works, not one stack. Do not build it while `P11` has three legs and a pass document open.
- **Rule on `REVIEW-004` A2 / `ROADS-001`** — see §4. Jason-sized, but a Claude can make it a
  five-minute decision.
---
## 4 · TEED UP, IN ORDER
- **`REVIEW-004` AND `ROADS-001` ARE STILL UNRULED, AND ARE NOW RIGHT THREE TIMES.** A2 calls Paper
  II's title claim fatally refuted by its own table; Road One is the re-cut that follows. Paper II
  still carries the title. **This is a Jason-sized ruling — but the one-page "here is what A2 costs
  and what Road One buys" that makes it a five-minute decision has still not been written by
  anybody, and it is Claude-sized.** Four sessions carrying it now.
- **PAPER IV'S TITLE IS ONE STEP AHEAD OF ITS OWN NARROWED ABSTRACT.** *"one atomic unit from the
  household to the sovereign"* against an abstract that now says the scales share a question and not
  a structure. Same defect as `REVIEW-004` A2 found in Paper II's title, logged the same way:
  **Jason-sized, teed up, not taken** (RESULT §6.3).
- **`G-H#22c` ATTRIBUTES BY EXACT SUBSTRING**, so `braatzArchive` writing `serve-braatz-archive.py`
  is unattributable on case and separators alone. Normalising both sides **widens a downgrade path**
  — a tripwire-weakening decision that needs its own at-bat and its own drill case beside `#9b`/`#9c`.
  Carded `1217526943288480`.
- **`~/Scripts/gate-selfcheck.sh` IS A SYMLINK INTO `~/code/darwin-mac-ops`.** `git add` in
  `~/Scripts` stages nothing **and reports success.** Cost `-57` a commit that silently did nothing.
- **`G-AL`'s REMEDY LINE STILL DOES NOT WORK AS PRINTED** — *"Read it: ~/Scripts/charter-read.sh"*
  with no slug exits 2. The gate knows the slug and prints it in the same sentence. One line. **Fourth
  session it has been carried.**
- **`G-T` calls a STALE claim LIVE** (`-52`) · **the roster cannot tell a GHOST from a sibling**
  (`-56`) · **the brake cannot tell YOU from a sibling** (`-57`, carded `1217526611881763`).
  **Three coats, one bug: identity is resolved in more than one place and the places disagree.** One
  grep for the identity resolution would find every site, including
  `~/.local/state/claude-session/current` being a single global file while Jason runs 2–3 sessions.
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
- **Everything `-31`→`-56` forbade still stands verbatim** — R5, the two sensitivities,
  `selected_lives`, §4.4's 0.3000, T4's 31.7 %, the δ arm, TERM-001/002, §9's list well-formedness,
  `wt107` IS NOT EDITED, §4.7 IS PINNED AT `ba59370`, DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD, DO
  NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION, DO NOT GRADE A CONSTRAINT FROM THE
  `machine` COLUMN, DO NOT WIDEN C07's GUARD, DO NOT WRITE AN OVER-BREADTH SELF-TEST WITH AN ABSENCE
  PREDICATE, DO NOT SLICE THE SWEEP LOG BY SLUG, **DO NOT TYPE A FULL SHA YOU HAVE NOT RESOLVED**,
  DO NOT LEAVE A FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT CORRECTS, DO NOT MEASURE A
  TEXT LENGTH WITH `wc -w`, DO NOT LET A `manual:` ROW BE SCORED BY WHOEVER DID THE WORK, DO NOT RUN
  `board.py` BY HAND, DO NOT HAND-EDIT A `P1x`/`P3x`/`P5x` ROW, DO NOT TRUST A GREEN CLONE, DO NOT
  "STRENGTHEN" A CHECK A MUTATION HARNESS CALLED WEAK UNTIL THE MUTATION IS SHOWN TO LAND, DO NOT
  EDIT `src/`, DO NOT `--no-verify` PAST `roster-brake`.
- **NEW · DO NOT RE-RUN A LEG THAT HAS RUN, AND DO NOT RE-APPLY A SPENT REMEDY.** The corpus gets
  **exactly one** first end-to-end pass (`ADR-001` addendum 6's batch ruling). `E1` and `E3` are
  spent, their remedies are applied, and a second pass needs a **new registration** that says what
  changed and may not cite this pass's numbers as support for its own design.
- **NEW · DO NOT READ "THE SYSTEM FAILS" AS "THE PAPERS ARE WRONG."** §3's second consequence is the
  point of the decomposition: Papers II and III are untouched by both failed legs and **ship as
  independent works.** One question asked at three scales and answered quantitatively at each is
  what survives, is what Paper IV §3 now claims, and is publishable.
- **NEW · DO NOT SKIP `E4`/`E5`/`E6` BECAUSE THE VERDICT CANNOT IMPROVE.** They are repairs the
  corpus needs whatever the verdict says, and §2.0 exists to stop exactly that confusion between a
  verdict and an audit.
- **NEW · DO NOT WRITE A SCRATCH SCRIPT INTO A REPO ROOT.** `~/Desktop/downloads` is the everything
  folder. A repo root is not a scratch pad, and a **shared** repo root is a scratch pad that bills
  other sessions their wrap gate — see the banner and `1217526943288480`.
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe with `while pgrep`. **Do not edit shared infra a sibling is mid-edit on.**
---
## 6 · TRANSPORT — darlish, zero-bridge (worked first try, `-06` → `-57`)
Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. **Never restart the app to fix darlish.** `darlish-check` is not in
the cloud kit; do not chase its 127.
- ⚠ **NEW · RUN `roster join --who <you>` AT STUDENT-IN, BEFORE `roster claim`, AND IT IS
  LOAD-BEARING TWICE.** `dx` resolves you as `cloud-<random>`, so a claim filed under
  `big-wealthTensor-NN` reads to `roster-brake` as **a sibling**, and it blocked two legitimate
  commits. `roster join --who <you>` **absorbs** the darlish rows into your name (*"absorbed 4 row(s)
  from cloud-acub6/h+"*) and the phantom disappears. **`lessons.py` wants the same call for a
  different reason:** without it a banked leaf carries **no contributor stamp** and can never reach
  `trusted` by bless. `roster leave --who <you>` ONCE at wrap.
- ⚠ **`ROSTER_BRAKE_ACK=<staged count>` IS THE HONEST EXIT** when your staged set covers the whole
  dirty tree and you verified the tree was EMPTY at your student-in. Put the reason in the commit
  message. `--no-verify` tells a reader nothing.
- ⚠ **A ROSTER CLAIM CAN BE A GHOST** (`-56`): the test is three facts together — `git status`
  empty, `HEAD` is the claimer's own wrap commit, roster task string is its handoff line.
- ⚠ **`| tail` MASKS `$?` ON EVERY `dx` CALL.** `python3 x.py | tail -8; echo rc=$?` reports
  **tail's** status. `-57` read a failing check as passing this way. No pipe when you need the code.
- ⚠ **HEREDOCS DIE INSIDE THE `dx '...'` ARGUMENT** — they work three times and shatter on the
  fourth. Write locally, `--put`, run with `bash`. A heredoc **inside** a `--put` script is fine and
  is how every multi-step edit in `-56` and `-57` shipped. **Nesting heredocs to GENERATE a `--put`
  script works too** (`python3 - <<'PYEOF' > /tmp/x.py` locally, then `cat | dx --put`) and is the
  cleanest way to ship a script containing its own quotes.
- ⚠ **NON-ASCII IN A `--put` SCRIPT: WRITE THE LITERAL CHARACTER.**
- ⚠ **`--get` NEEDS THE FULL PATH; a leading `~` expands in the CLOUD and fails.** `--put` accepts
  `~`. **Staging the three papers into the cloud with `--get` and reading them there is much cheaper
  than grepping them over `dx`** — Paper III is 202 kB / ~2 200 lines and `-57` read all four papers
  this way for the price of four calls.
- ⚠ **`lessons.py` AUTO-COMMITS AND AUTO-PUSHES each leaf** — and its auto-commit is itself subject
  to `roster-brake`, so a blocked leaf leaves the blackbook dirty. Check `git status` there at wrap.
- ⚠ **`gate-selfcheck.sh` TAKES ~5–6 MINUTES AND A FOREGROUND `Bash` CALL DIES AT 8m20s.** Detach:
  `nohup env GATE_ROSTER_WHO=big-<sess> bash -c "$HOME/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1" &`
  then `sleep 340; grep -E "GATE SELF-CHECK|^  FAIL" /tmp/gate.log`. **COMMIT EVERYTHING FIRST** and
  **re-stamp the charter immediately before it.** A `DIRTY` FAIL now prints the paths (`6a363e7`).
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started ·
  `5` crossed but mismatched.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
**SUITE:** 1068 collected, 1068 passed, zero skips — darwin ~66 s, cloud ~175 s.
`check_abstract_size.py` **is silent on failure — use `--print`.** `defensive_count.py` takes a
positional path and **only a DELTA means anything**. **`redproof_apparatus.py`'s SKIPPED COUNT IS A
SIGNAL: 2 is the baseline. More means you turned a green row red** — and `P5l` runs `P5a`'s check
first, so one over-length abstract costs two rows.
---
## 0 · THE TELL, NOW IN EIGHTY-EIGHT SHAPES
`-28` through `-56`'s tells all stand (the instrument-artefact question; a guard must scan assertions
not quotations; a mutation that does not mutate reports your guard as weak; pre-commit the
FAVOURABLE outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT; a correction that
lives only in a handoff has not been made; a rule can be false on the day it is written; a criterion
that passes because it does not apply is a blank line wearing a tick; a system of documents can hold
a contradiction no per-document review can find; a test whose outcome the designer can predict is
not a test; a type check run against prose and against code can disagree, and the disagreement is
the result; a design document's premise is a claim and it is the one nobody checks; "indistinguishable"
is a statement about sample size until you scale N). `-57` adds four:

- **A CLAIM NOTHING DEPENDS ON IS NOT A CLAIM NOTHING CAN BREAK.** The sentence that failed a
  corpus-level test is structurally inert: delete it and Paper III is unchanged, nothing
  back-references it, and its own paragraph closes itself. **That is what made it dangerous** — an
  inert unsupported claim has no downstream that will ever catch it. Auditing "what does this
  document depend on" by asking "what would break" finds nothing here. Ask instead **what does it
  ASSERT**, and check each assertion's relata exist.
- **A DISCLAIMER THAT COVERS THE EVIDENCE DOES NOT COVER THE ASSERTION.** *"…is cited rather than
  reproduced … the mechanism is the same … and the evidence for it belongs to that paper"* disclaims
  the evidence for the cited result and leaves the **sameness** asserted in the citing document's own
  voice. Split every hedged citation into what it disclaims and what it still claims; the hedge is
  usually load-bearing on only one of them.
- **A WITHDRAWAL APPLIED TO THE DOCUMENTS THAT ARGUE FOR A CLAIM WILL MISS THE ONE THAT MERELY
  MENTIONS IT.** `E1`'s remedy named the two papers that made the identification. The third copy was
  four words in an appendix aside naming no sibling — **ungreppable by either paper's title, and
  invisible to a remedy written by someone who had read all three.** Before declaring a retraction
  applied, grep the corpus for **the claim's own phrasing**, not for the documents you know carry it.
- **A REGISTRATION IS AN INSTRUMENT, AND NOBODY HAS EVER POINTED AN INSTRUMENT AT IT.** Four
  false-or-self-defeating premises found in `END-TO-END-001` by legs of `END-TO-END-001`, **none of
  them about the corpus**: §0's "no written answer anywhere", E1's audit-half "no document mentions
  it", §2.0's three-and-three against four-and-two, and §4.2-versus-§6 on `E2`. The document's prose
  about the corpus has held up perfectly; its prose about **itself** is 0-for-4. Red-proof a
  registration against its own tallies, lists and instructions the way a criterion is red-proofed
  against its own artefact.
---
## 7 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.
**Coffee status:** ☕ TWENTY-THREE SESSIONS. The corpus's system test has now returned twice and lost
twice — and both losses were sitting in the repository in plain sight, correctly written down, filed
under nothing. `-56` found the fact that killed `E1` four days stale in a dossier. `-57` found the
sentence that killed `E3` four words long in an appendix, eight hours after the corpus had withdrawn
the same claim from its other two volumes. **The first end-to-end test of a corpus that documents
everything has established, twice, that documenting is not indexing.** Papers II and III are
untouched and ship. Paper IV is a survey, a measured whitespace and one worked instance — which is
what it can honestly be, and it is enough. 🥎
