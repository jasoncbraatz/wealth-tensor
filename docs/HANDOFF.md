---
project: wealth-tensor
gh_sha: 6fb2de59adfe21a043945264aeac51930bf3768f
updated: 2026-08-16
session: wealthTensor-59
gate_passed: PENDING
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16, superseding the 'three preprints publicly posted' line carried since sessionZero): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF
`gh_sha` names the commit this file describes; **the only thing added after it is this file**, so
`python3 scripts/handoff_gate.py --check` prints `ADVISORY: docs-only drift` and exits 0. Assert the
exit code exactly. **`| tail` MASKS `$?` ON EVERY `dx` CALL** — `cmd; echo rc=$?` with no pipe, or
you are reading `tail`'s status. `gh_sha` is the full SHA from `git rev-parse`, never an expanded
abbreviation.

---
## 0 · NOTHING IS PERISHABLE ANY MORE, AND THAT IS NEW
**`E2` IS SPENT. THERE IS NO LONGER ANY ARTEFACT IN THIS PROJECT THAT A CARELESS FIRST TEN MINUTES
DESTROYS.** For four sessions §0 has been a tripwire: read this before you read that, in this order,
or you burn the last blind leg. **You may now read anything in any order.** `docs/END-TO-END-001.md`
can be opened end to end without cost. Take the ten minutes you would have spent tiptoeing and spend
them on §3 instead.

Two things replace it, both cheap:
1. **`~/Scripts/roster who` before you claim anything.** A sibling has been live in `~/Scripts` and
   `claude-blackbook` for hours at a stretch.
2. **`git status --porcelain` in `claude-blackbook` at student-in, and write down what you saw.** It
   is what makes `ROSTER_BRAKE_ACK` honest later. §6.

---
## ORIENT — read these first, in this order
1. **`docs/RESULT-END-TO-END-001-E2.md`** — `-59`'s, and **the only leg of this pass the corpus has
   won.** §3.1 and §3.2 are the two findings the run built and lost; §3.3 is why the verdict did not
   need the hard question answered; §3.4 is the leg's real content and is the most useful page in the
   document for anyone about to build `P13`.
2. **`docs/RESULT-END-TO-END-001-E2-blind-pass.md`** — the extraction, committed at `53ddda7` **before**
   the candidate existed in the session. Read it for the two builders' lists, which are a free
   corpus-wide defect inventory nobody has mined past `E2`'s question.
3. **`docs/RESULT-END-TO-END-001-E5.md`** (`-58`), **`-E3.md`** (`-57`), **`-E1.md`** (`-56`).
4. **`docs/END-TO-END-001.md`** — the registration. **FIXED. May not be edited in response to a
   result. NOW 0-FOR-7 ON ITS OWN PROSE, and the seventh is new in kind** (`-E2.md` §5).
   ⚠ §0 above: **the reading restriction is lifted.**
5. **`docs/CHECKLIST.md`** — 66 criteria. `./scripts/regen-board.sh`, never `board.py` by hand.
   `P11a`/`P11b`/`P11c`/`P11e` green; `P11d`/`P11f`/`P11g` red and correctly so.
6. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS.**
   `~/Scripts/charter-read.sh wealthTensor-<NN>` — POSITIONAL slug. **Re-stamp IMMEDIATELY BEFORE
   THE GATE**, always.
7. **`docs/REVIEW-004-pre-posting-dossier.md`** — **right five times.** `-59` is the first session in
   four that did **not** find it had already answered the question being asked, which is weak
   evidence it is finally mined out and no evidence at all that it is. **`docs/ROADS-001` is its
   sibling and is STILL UNRULED AT SIX SESSIONS — see §4, and see §3's forcing line.**
8. `docs/adr/ADR-001` (title and §Decision frozen) · `scripts/gen_apparatus_rows.py`'s docstring
   before touching any apparatus row · `scripts/add_p11_rows.py` + `scripts/redproof_p11.py` before
   any `P11` row · `scripts/redproof_apparatus.py` · `tests/test_paper_test_counts_are_derived.py`
   + `scripts/redproof_paper_counts.py` before touching a quoted test count.
9. REG-013 + `RESULT-REG-013` §4.1 · REG-003 §§3.2/3.3/7 · SCOUT-001 · REG-012 §§6–7 ·
   RESULT-TERM-001/002 · REG-010 §1/§4 · CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (HEADER NOTE
   FIRST).
---
## `-59` in one line
**THE RUN BUILT A FAILURE, HAD IT BUILT AGAIN INDEPENDENTLY, PUT FIVE REFUTERS ON IT IN TWO ROUNDS,
AND LOST EVERY ROUND — AND THE CORPUS WON ITS FIRST LEG OF THE PASS.** `E2` asks whether the
conjunction asserts something no paper defends. It does not: every sentence the blind pass extracted
traces to a paper, a section, and either a result or a disclaimer. **`E2` — FAILURE REFUTED. `T`
remains 2. THE SYSTEM FAILS still stands, on `E1` and `E3`.** Off the leg: **the phantom roster claim
that four sessions could not source is solved, fixed and red-proofed.**

---
## 1 · WHAT HAPPENED
### The leg, and how it was kept blind
Quotation only. No code against `src/`, no seeds. **The registration was never opened.** It was cut on
darwin — `sed -n "1,204p"` and `sed -n "241,505p"` — and only the slices were transferred, so lines
205–240 were not in the session to be read. `-58` preserved the leg by not scrolling past a heading;
`-59` preserved it by not having the bytes. **Copy the second, not the first**: a protocol that
depends on self-control tests self-control at the exact moment temptation arrives.

The blind list was committed **in its own commit** (`53ddda7`), whose parent contains no reading of
the candidate region — which is what turns *"the blind pass records its list first"* from an
assertion into something `git log` can check.

### The two findings the run built, and what killed them
**Round one — three refuters, all REFUTED.** The run's first reading was `E5`'s shape again: the
FAILURE and REFUTED clauses are not complements, the candidate sits in the gap, so UNDECIDED on the
registration. It was a **prior, not an observation** — `-58` lost a leg hunting the previous leg's
shape and `-59` hunted it one leg later.

**Round two — two more refuters, both REFUTED, on a witness the run said did not exist.** The
surviving finding was that Paper IV §3 asserts a quantitative answer at three scales and names two
witnesses, with no household paper. **Paper III §2–§3.1 IS the household paper.** §4 opens *"§3
established what the filter does to one asset"*; §2 is the single unsummed holding at effective decay
**0.02** and **α = 0.05** — Paper IV's *"they are different numbers"* — and §3.1 reports the lag table
and `D(φ) = (1 − φ)·D(0)`. Paper IV supplies the pointer in the **first clause of the next
paragraph**: *"a balance sheet is the household's holding, summed and reported."* The run had read
§3's three paragraphs as three sealed cells.

**And the verdict never needed the hard question answered.** Limb (c) fails for every belief either
builder produced, so the leg is decidable without ruling on limb (b)'s ambiguity — and ruling on a
fixed clause you did not need to rule on is re-choosing.

### The registration, now 0-for-7, and the seventh is a different animal
1. **`E2`'s power check cannot fail, because its target sits inside its own mandated input.** The
   check reads abstracts and contributions lists; the candidate is in Paper IV's **abstract** and in
   **contribution 2** with its section number attached.
2. **`E2` defines ownership four times and they do not agree** — three evidentiary, limb (b)
   presence-based. Recorded; not ruled on, because limb (c) settled the leg.
3. **THE REGISTRATION MISQUOTES THE CORPUS.** It registers the candidate without §4.3's trailing
   *"because it is not what an aggregate is usually built for"* — **the exact error `-58` wrote into
   §5 four days earlier.** The first six were the document being unreliable about *itself* while
   reliable about the corpus. That run is over.

### Off the leg — the phantom roster claim, four sessions old, SOLVED
`-58` recorded a claim appearing under its own name that it never made — resource `synthetic`, task
*"amend the registration after its result"* — and reported, correctly, that the string existed
**nowhere on disk**. It reappeared under `-59` at `16:26:43`, one second-for-second match with a
commit, and that timestamp is what cracked it.

**The string was never on disk because it is a commit subject inside a fixture.**
`tests/test_reg001_sec5_no_amendment_after_result.py :: test_the_detector_fires_on_a_synthetic_amendment`
builds a scratch repo and commits into it. **`core.hooksPath` is set GLOBALLY**, so the estate's
`post-commit` fires inside that fixture exactly as in a real repo, and `roster-oncommit.py` does its
job perfectly: basename of the work tree (`synthetic`) as the resource, commit subject as the task.
A real claim, on the live board, for a directory that stops existing a second later.

**Fixed at the class, not the instance** — a work tree under the system temp directory is a fixture
and the hook returns before the board. Keyed on **location, not name**. `~/Scripts/roster-oncommit.py`,
committed and pushed at `2e9e10d`, with `~/Scripts/roster-oncommit-drill.sh` beside it: restores the
pre-fix file, runs the test, counts synthetic claims (**1**), restores the fix, runs it again, counts
(**0**), and prints PROVEN only on 1-then-0. **Measured today: red 1, green 0.**

Every test in the estate that commits was a phantom-row generator, across 107 repos. The one-line fix
inside wealth-tensor's test would have hidden that.

### The repairs, and the one that was withdrawn
Both `P7`, **neither an E2 remedy** — no unowned claim was found, and applying a remedy whose
antecedent did not occur is re-choosing (`-57`'s ruling, and it binds).
- **Paper IV §3's Household paragraph now names its witness** (Paper III §2's two rates, §3.1's
  result) instead of leaving its citation to the next paragraph's opening clause.
- **Contribution 2's *"the thermodynamic structure nobody is looking at"*** now carries the body's
  reason. A universal was standing in for a hedge.
- **THE SAME REPAIR WAS ATTEMPTED ON THE ABSTRACT AND WITHDRAWN.** `check_abstract_size.py` went red
  — **Paper IV's abstract is 248 words against a 250 ceiling** — but that is not why. It was
  withdrawn because the abstract says *"largely unmeasured"* where the body says ***"very** largely"*:
  the abstract is **weaker**, and what it drops is a causal explanation, not a scope qualifier.
  **`-59` had grouped two sentences by their surface without checking whether they failed the same
  way** — a small copy of the error it spent the afternoon losing to. The guard caught the length;
  only re-reading caught the merit.

### Counts, and the numbers
**TEST legs run 4 · FAILED 2 · UNDECIDED 1 · REFUTED 1. AUDIT legs run 0. No combined score exists
and none is offered.**

| | |
|---|---|
| suite | **1074 passed**, ~67 s, **zero skips** — baseline held |
| red-proof (apparatus) | **37 mutations, 0 survivors, 2 skipped** — baseline held |
| red-proof (`P11`) | **4 proven by mutation, 3 red on their own, 0 WEAK** (`P11b` moved into proven) |
| red-proof (paper counts) | **5 mutations, 5 red, 0 survivors** |
| abstracts | II 249 · III 247 · **IV 248** — all inside 250 words / 1920 chars |
| board | 66 criteria, `P11b` green |
| lessons | **8 banked** (6 global, 2 project) · 2 `use` + 1 `record-outcome pass` |
| commits | `53ddda7` blind list · `6fb2de5` the leg + repairs · `2e9e10d` (`~/Scripts`) the phantom fix · `e8bd3006` (blackbook) |

---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-58`'s rulings stand verbatim**, including: `END-TO-END-001` IS FIXED AND
  MAY NOT BE EDITED IN RESPONSE TO A RESULT; A LEG MAY NOT COUNT A FINDING MADE BEFORE IT EXISTED;
  TEST AND AUDIT COUNTS ARE REPORTED SEPARATELY; **THE ADMISSION CRITERION IS NOT ADVISORY**; DO NOT
  ADD AN OBSERVABLE TO A LEG'S OWN FAILURE CRITERION; REG-013's DECISION RULE IS SPENT; H1 LICENSES
  OCCUPANCY; `P2`/`P3`/`P5` STAY MANUAL; ADR-001's TITLE AND §Decision FROZEN; THE ABSTRACT IS A
  SUBMISSION FIELD; THE ARM IS δ; DO NOT SPEND THE TIE-BREAK; **R5 IS UNSPENT**; T4's WIDTH IS
  31.7 %; **T2 MAY NOT BE RUN ON THIS DATA**; §4.7 IS PINNED AT `ba59370`; `wt107` IS NOT EDITED;
  APPARATUS SUB-ROWS ARE GENERATED; A ROW IS NOT DONE UNTIL SEEN RED; `P8` IS ONE PASS TAKEN LAST;
  `P7` DOES NOT CLOSE THE CORPUS; DONE IS "CLEARED FOR LIFTOFF"; **`P13` IS LAST** AND IS A PDF *AND
  A RECIPE*; ROW IDS ARE NEVER RENUMBERED; **DO NOT EDIT `src/`**; `T = 2`, **THE SYSTEM FAILS**, AND
  `T` CAN RISE AND CANNOT FALL; **`E5` IS SPENT AND ITS ANSWER IS UNDECIDED**; THE MULTIPLICITY OF
  THE TWO CROSS-CITED GUARDS IS BIBLIOGRAPHIC; ADR-001 §Consequences' CONTAINMENT SENTENCE IS NOT
  RETRACTED.
- **NEW · `E2` IS SPENT AND ITS ANSWER IS FAILURE REFUTED.** Do not re-run it. Do not apply its
  remedy (*"owned or cut"*) to anything — its antecedent did not occur. **A leg that is REFUTED has
  been RUN**; `P11b` is green because the verdict is recorded.
- **NEW · PAPER III §2–§3.1 IS THE CORPUS'S HOUSEHOLD-SCALE WITNESS.** Two independent builders and
  a full afternoon concluded it did not exist. It does. **Any future finding of the form "scale X has
  no witness" must first grep the other two papers for the OBJECT, not the WORD** — Paper II carries
  zero occurrences of *household*, *sovereign*, *compose*, *extensive*, *fold* and *atomic*, and that
  is a fact about its vocabulary, not about its content.
- **NEW · `E2`'s LIMB (b) AMBIGUITY IS RECORDED AND UNRULED, DELIBERATELY.** `E2` defines ownership
  four times; three are evidentiary and limb (b) is presence-based. **`-59` did not rule**, because
  limb (c) decided the leg without it. A successor that needs the ruling needs `END-TO-END-002`, not
  an opinion.
- **NEW · THE REGISTRATION IS 0-FOR-7 ON ITS OWN PROSE AND HAS NOW ALSO MISQUOTED THE CORPUS ONCE.**
  The *"5-for-5 on the corpus's prose"* line from `-58` is **retired**. Keep checking the
  registration's own tallies, lists and instructions before checking the corpus — but no longer
  assume its quotations are faithful either.

---
## 3 · THE AT-BAT for `-60` — **`E4`, AND THEN THE THING NOBODY HAS TAKEN IN SIX SESSIONS**
**Take two items, not one.** Neither is more than about an hour and they are different muscles.

**1 · `E4` — THE CORPUS'S EMPIRICAL CONTENT, STATED WHOLE (`[AUDIT]`, `P11d`, where the board
points).** The cheapest honest leg left. Its remedy is **one pre-registered sentence in Paper IV**
§1 or §9, and **most of the reading is already done for you**: `RESULT-…-E3.md` §5 tabulates each
paper's statement about its own data, and the `E2` blind pass (`Builder B`, checked-and-cleared
list) independently confirms Paper III §6.1's *"the framework currently has no confirmed empirical
claim"* is never repeated in Paper IV's limitations. **Run it to its stated criterion anyway** — it
is an AUDIT and the designer expects zero, which is exactly the leg a session is tempted to write up
without running.

**2 · `REVIEW-004` A2 AND `ROADS-001` — THE ONE-PAGER. SIX SESSIONS. TAKE IT.** A2 calls Paper II's
title claim fatally refuted by its own table; Road One is the re-cut that follows. **The one page
that says what A2 costs and what Road One buys — turning it into a five-minute Jason decision — has
now been described as "Claude-sized and better than another audit leg" by two consecutive handoffs,
by sessions that then did not write it.** That is not a backlog item any more, it is a **process
defect**, and it is the kind this project exists to fix. `-59` names it as such rather than passing
it on a third time with the same adjective.

> **FORCING LINE, and it is `-59`'s ruling: a session that takes neither of the two items above must
> say why in one line at the top of its handoff.** Not a paragraph. One line. `-58` wrote the correct
> sentence about A2 and moved on; a rule that costs one line is the cheapest thing that would have
> stopped it.

**The honest alternatives, ranked:**
- **`E6`** (AUDIT) — its worked example is excluded from its own run; read the leg's own note first.
- **`P11g`** — the pass-level `docs/RESULT-END-TO-END-001.md`, which **does not exist** and is the
  artefact the whole pass is for. It cannot be honest until `E4` and `E6` have run. **After those two,
  it is the last thing between `P11` and `P13`.**
- **`P7` on Paper IV §3 and contribution 2** — `-59` rewrote both and **must not also score them**.
- **`P7` on Paper IV's §5 and §10** — the missing regeneration command (Builder B's #7), pre-existing,
  `§1.2`-excluded from system-level failure, and unrepaired.
- **`P6`'s remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
- **`P13`. STILL LAST**, and its subject matter is decided: three works, not one stack.

---
## 4 · TEED UP, IN ORDER
- **THE `E2` BLIND PASS IS AN UNMINED DEFECT INVENTORY.** Two builders produced **28 belief/ownership
  rows** between them and `E2` only ever asked one question of them. Several are live `P7` material
  nobody has scored: Paper III's abstract stronger than its body at **three** separate places
  (B#2 the disclosed-lives repair, B#4 the conservatism constraint, B#8 τ = −1 and the 2.58× that is
  a leverage-to-**budget** ratio against a **0.61** threshold, i.e. 4.2×); Paper IV §1.1's *"firm-level
  panels of both are public and free"* against its own §9.1 and Paper III §9.5 (**that one is `E6`'s
  shape and should be left for `E6`**). Read `docs/RESULT-END-TO-END-001-E2-blind-pass.md` §§3–4
  before starting any fresh review — it is an hour of adversarial reading already paid for.
- **PAPER IV'S TITLE IS ONE STEP AHEAD OF ITS OWN NARROWED ABSTRACT** — *"one atomic unit from the
  household to the sovereign"*. **`E2` changes the balance here and a successor should know it:** the
  household scale **does** have a witness, so the title's *range* is defensible; what is undefended is
  *unit*, which is a different and narrower objection than `-57` teed up. Jason-sized.
- **`lessons.py record-outcome` STILL DOES NOT AUTO-COMMIT**, unlike `add` and `use` — third session
  running to leave the blackbook dirty at wrap. **The fix is now located: the helper is
  `lessons.py:1012 _git_commit_push(path, scope, text)`, and `record-outcome` is the one caller that
  never reaches it.** Not taken by `-59` because a sibling was mid-flight *running* that script, and
  editing a tool someone is executing is the one thing §5 names about shared infra. **Two minutes for
  whoever finds the blackbook uncontended.**
- **`G-H#22c` ATTRIBUTES BY EXACT SUBSTRING**; normalising both sides widens a downgrade path and
  needs its own at-bat and drill case. Carded `1217526943288480`.
- **`~/Scripts/gate-selfcheck.sh` IS A SYMLINK INTO `~/code/darwin-mac-ops`.** `git add` in
  `~/Scripts` stages nothing **and reports success.**
- **`~/Scripts` MAY STILL BE `DIRTY(2)`** with `big_worker-braatzArchive`'s untracked
  `braatz-crawl-check.py` and `serve-braatz-archive.py`. **`-59` committed and pushed its own
  `~/Scripts` change (`2e9e10d`) without touching theirs** — `git add <paths>`, never `-A`. Carded
  `1217526943288480`.
- **THE PHANTOM CLAIM IS CLOSED — REMOVE IT FROM YOUR LIST.** Card `1217527629536618` should be
  updated with the cause (fixture commit + global `core.hooksPath`), the fix (`2e9e10d`), and the
  drill. **`-59` did not update the card**; that is the one loose end it is handing on, and it is two
  minutes with the Asana MCP.
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
- **Everything `-31`→`-58` forbade still stands verbatim** — R5, the two sensitivities,
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
  NOT WRITE A SCRATCH SCRIPT INTO A REPO ROOT, DO NOT QUOTE A SENTENCE INTO A FINDING WITHOUT ITS
  TRAILING SCOPE CLAUSE, DO NOT TREAT TWO AGREEING INDEPENDENT BUILDS AS A CHECK, DO NOT REPAIR A
  WRONG NUMBER WITH A RIGHT NUMBER.
- **NEW · DO NOT CONCLUDE "NO PAPER CONTAINS X" FROM A WORD COUNT.** Paper II has zero occurrences of
  every word Paper IV uses for the thing Paper II demonstrably contains. `grep` finds vocabulary;
  only reading finds objects. **This cost `-59` an afternoon and it was the second finding it lost.**
- **NEW · DO NOT READ A SECTION'S PARAGRAPHS AS SEALED CELLS.** Paper IV §3's household citation is
  the first clause of the *next* paragraph. A finding of the form "paragraph P cites nothing" must
  read the paragraph after it before it is a finding.
- **NEW · DO NOT REPAIR TWO SENTENCES TOGETHER BECAUSE THEY LOOK ALIKE.** Check which way each moves
  the claim's strength first. An abstract dropping a `because` is compressing; an abstract dropping a
  hedge is overreaching, and they are identical in a diff.
- **NEW · DO NOT STOP AT ONE ROUND OF REFUTATION.** Round one kills what you built; the finding it
  leaves standing has been *asserted* by refuters arguing another lens and *attacked* by nobody. **Aim
  round two at the survivor.** Both of `-59`'s findings died, and only the second round could kill the
  second one.
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe with `while pgrep`. **Do not edit shared infra a sibling is mid-edit on.**

---
## 6 · TRANSPORT — darlish, zero-bridge (worked first try, `-06` → `-59`)
Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. **Never restart the app to fix darlish.** `darlish-check` is not in
the cloud kit; do not chase its 127.
- ⚠ **`dx` RUNS AS `root` IN THE CLOUD CONTAINER, SO `~` IS `/root`.** `--get` into an absolute path
  under `/home/claude` or the `Read` tool cannot see the file. **`-59` did this correctly on the
  first try by using absolute paths everywhere — copy that.**
- ⚠ **RUN `roster join --who <you>` AT STUDENT-IN, BEFORE `roster claim`.** `dx` resolves you as
  `cloud-<random>`; `join` **absorbs** those rows. `roster leave --who <you>` ONCE at wrap.
- ⚠ **`roster claim` TAKES `--resource`, NOT `--repo`.**
- ⚠ **`ROSTER_BRAKE_ACK=<staged count>` IS THE HONEST EXIT** when your staged set covers the whole
  dirty tree and **you verified the tree was EMPTY at your student-in.** Reason it in the commit
  message. `-59` did this once, in `claude-blackbook`, and the message says why.
- ⚠ **A ROSTER CLAIM CAN BE A GHOST**: `git status` empty **and** `HEAD` is the claimer's own wrap
  commit **and** the roster task string is its handoff line. Two of three is not the test.
- ⚠ **`| tail` MASKS `$?` ON EVERY `dx` CALL.**
- ⚠ **HEREDOCS DIE INSIDE THE `dx '...'` ARGUMENT.** Write locally, `--put`, run with `bash`. A
  heredoc **inside** a `--put` script is fine and is how every edit in `-56`→`-59` shipped.
- ⚠ **NON-ASCII IN A `--put` SCRIPT: WRITE THE LITERAL CHARACTER.**
- ⚠ **`--get` NEEDS THE FULL PATH; a leading `~` expands in the CLOUD and fails.** `--put` accepts `~`.
  **Staging the papers into the cloud with `--get` is much cheaper than grepping them over `dx`, and
  it is what lets you hand a subagent the manuscripts** — `-59` ran seven subagents off three staged
  files.
- ⚠ **A RECURSIVE `grep` OVER `~/repos` FROM THE CLOUD WILL TIME OUT THE 5-MINUTE `Bash` LIMIT.**
  `-59` lost a call to it. Name the directories, and exclude `.venv`.
- ⚠ **`lessons.py add`/`use` AUTO-COMMIT AND AUTO-PUSH; `record-outcome` DOES NOT.** §4.
- ⚠ **`gate-selfcheck.sh` TAKES ~5–6 MINUTES AND A FOREGROUND `Bash` CALL DIES AT 8m20s.** Detach:
  `nohup env GATE_ROSTER_WHO=big-<sess> bash -c "$HOME/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1" &`
  then `sleep 340; grep -E "GATE SELF-CHECK|^  FAIL" /tmp/gate.log`. **COMMIT EVERYTHING FIRST** and
  **re-stamp the charter immediately before it.**
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started ·
  `5` crossed but mismatched.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
**SUITE:** 1074 collected, 1074 passed, zero skips — darwin ~67 s, cloud ~180 s.
`check_abstract_size.py` **is silent on failure — use `--print`, AND PASS THE PAPER PATH: it defaults
to Paper III.** `defensive_count.py` takes a positional path and **only a DELTA means anything**.
**`redproof_apparatus.py`'s SKIPPED COUNT IS A SIGNAL: 2 is the baseline.**

---
## 0' · THE TELL, NOW IN NINETY-EIGHT SHAPES
`-28` through `-58`'s tells all stand (the instrument-artefact question; a guard must scan assertions
not quotations; a mutation that does not mutate reports your guard as weak; pre-commit the FAVOURABLE
outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT; a correction that lives only in
a handoff has not been made; a rule can be false on the day it is written; a criterion that passes
because it does not apply is a blank line wearing a tick; a system of documents can hold a
contradiction no per-document review can find; a claim nothing depends on is not a claim nothing can
break; a registration is an instrument and nobody has ever pointed an instrument at it; a criterion's
failure clause and its refutation clause are two different predicates; two agreeing builds check the
evidence and not the frame; the clause that narrows a claim is the clause your summary drops; a
dossier finding with no instrument will be re-found larger). `-59` adds four:

- **A CALIBRATION STANDARD PRINTED ON THE INSTRUMENT'S OWN INPUT MEASURES NOTHING.** `E2`'s power
  check asks whether a blind pass surfaces a sentence, and hands the pass the sentence, its section
  number and the absence of its owning result — in the abstract and the contributions list the check
  itself mandates. It cannot miss, so a hit is not evidence of power. **Before believing a "the pass
  found it", check where the answer was sitting while the pass ran.**
- **A `grep` FINDS VOCABULARY; ONLY READING FINDS OBJECTS.** Paper II carries zero occurrences of
  every word Paper IV uses for the thing Paper II contains. **An absence proven by word count is a
  fact about a lexicon**, and two independent builders plus a full afternoon can be built on top of
  one before anybody opens the section.
- **THE FINDING THAT SURVIVES ROUND ONE HAS BEEN ASSERTED BY REFUTERS AND ATTACKED BY NOBODY.** Round
  one refuters are arguing *against your claim*, so whatever they lean on to kill it arrives
  unexamined and wearing three refuters' authority. **That is the most dangerous object in the
  session, and it is the one about to be published.** Aim round two at it.
- **THE ERROR YOU JUST LOST TO IS THE ERROR YOU WILL COMMIT IN THE REPAIR.** `-59` spent an afternoon
  losing to two sentences grouped by resemblance, then grouped two sentences by resemblance inside its
  own repair, and the abstract's word ceiling caught it before any reasoning did. **Re-read a repair
  as if a stranger wrote it, especially the half you are confident about.**

---
## 7 · ORIENT-THEN-GO
Nothing to preserve, nothing to tiptoe past. Emit one line — `Oriented: <state> · at-bat: <X> ·
opening with <first action>.` — and start building. Don't wait for a go. Do not open by asking Jason
anything. **If you take neither `E4` nor the A2 one-pager, §3's forcing line wants one sentence from
you at the top of your handoff.**

**Coffee status:** ☕ TWENTY-FIVE SESSIONS. `-56` found the fact that killed `E1` four days stale in a
dossier. `-57` found the sentence that killed `E3` four words long in an appendix. `-58` built a
finding, confirmed it independently, and watched a refuter take it apart. `-59` did that **twice in
one afternoon** — and the second refuter killed it with a table of numbers that had been sitting in
Paper III since the fifth of August, under a heading that says exactly what it is. **The corpus wins
its first leg of the pass, and it wins it by having written its limitations sections honestly.**
Papers II and III ship. Paper IV is a survey, a measured whitespace, one worked instance — and, as of
today, a household paragraph that names its witness. Four legs down, two to go, and the pass-level
document that nobody has written yet is the only thing standing between `P11` and `P13`. 🥎
