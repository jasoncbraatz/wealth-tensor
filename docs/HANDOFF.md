---
project: wealth-tensor
gh_sha: 28bf7c247ca30528327beec5e07143179fb6943f
updated: 2026-08-16
session: wealthTensor-56
gate_passed: true
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16, superseding the 'three preprints publicly posted' line carried since sessionZero): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF
`gh_sha` names the commit this file describes; **the only thing added after it is this file**, so
`--check` prints `ADVISORY: docs-only drift` and exits 0. Assert the exit code exactly (`-39`);
`| tail` masks it. That sentence is an **INVARIANT, not a description**. If a post-wrap commit
lands, repoint `gh_sha` and re-master this file. `-55`'s modern reason it breaks — **a live
sibling** — still stands: run `~/Scripts/roster who` BEFORE you trust the header. `-56` adds the
counter-case: **the roster's warning can be a GHOST**, and telling the two apart is a measurement,
not a vibe. See §6's first bullet.
`gh_sha` is the full SHA from `git rev-parse`, not an expanded abbreviation.
---
## ORIENT — read these first, in this order
1. **`docs/RESULT-END-TO-END-001-E1.md`** — **NEW, `-56`'s deliverable, and it changes what two
   papers say.** The corpus's first end-to-end leg, run. **It FAILS.** Read §2.2 (the type check
   that decides it), §3.1 (the design's own premise, refuted), §4 (admission accounting) and §6
   (what was and was NOT applied). **§6's "deliberately NOT applied" list is a live obligation on
   whoever lands the next TEST leg** — do not let it rot.
2. **`docs/END-TO-END-001.md`** — `-55`'s registration. Still FIXED, still may not be edited in
   response to a result. Five legs remain. §3's verdict rule now reads against **`T = 1`**.
3. **`docs/CHECKLIST.md`** — the generated board. **`./scripts/regen-board.sh`, never `board.py`
   by hand.** 59 criteria, 45 met, fourteen open — unchanged by `-56`, and §4's first item explains
   why that is a defect rather than a fact.
4. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS.**
   `~/Scripts/charter-read.sh wealthTensor-<NN>` — POSITIONAL slug. **Re-stamp IMMEDIATELY BEFORE
   THE GATE**, always, sibling or no sibling.
5. **`docs/REVIEW-004-pre-posting-dossier.md` §§E1, E2, E3, A1, A2** — **read this before you plan
   anything.** `-56` went looking for E1's evidence and found that this document had already made
   the finding that decides the leg (§E2), had already answered `ADR-001` addendum 6's open
   question under a heading naming it (§E3), and had already stated E1's audit half twice (§A2).
   **It is four days old and nothing indexed it.** Assume it contains the answer to whatever you
   are about to derive.
6. **`docs/ROADS-001-two-reconstructions.md`** — same era, same problem. Road One is a whole
   re-cut of Paper II built on *"κ is the budget, and the budget does not determine the outcome"*,
   which is `REVIEW-004` A2's fatal finding turned into a spine. **Neither was ever ruled on.**
7. `docs/adr/ADR-001` (addendum 6 is what `END-TO-END-001` answers; title and §Decision frozen) ·
   `docs/adr/ADR-002` (typography, `P13c`/`P13d` closed) · `scripts/gen_apparatus_rows.py`'s
   docstring before touching any apparatus row · `scripts/redproof_apparatus.py` +
   `tests/test_apparatus_rows_are_falsifiable.py` · `python3 scripts/handoff_gate.py --check`.
8. REG-013 + `RESULT-REG-013` §4.1 · REG-003 §§3.2/3.3/7 · SCOUT-001 · REG-012 §§6–7 ·
   RESULT-TERM-001/002 · REG-010 §1/§4 · CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (HEADER NOTE
   FIRST).
---
## `-56` in one line
**THE CORPUS'S FIRST SYSTEM-LEVEL TEST HAS ITS FIRST RESULT AND IT IS A LOSS — AND THE FACT THAT
KILLED IT HAD BEEN CORRECTLY WRITTEN DOWN IN THIS REPOSITORY FOR FOUR DAYS.** Paper II's ρ and
Paper III's φ are not the same kind of object: what the reporting filter does not recognise is
**deferred**, held in a gap and released at rate α — that is the whole of Paper III's crisis result
— while what the levy's base does not recognise is **destroyed**, and Paper II has no parameter
that plays α's part. A lag and a loss share the adjective *"a measurement layer with a
systematically incomplete view"* and share nothing else. `E1` FAILS at `E1a`, the pre-registered
demotion is applied to Papers II and IV, and `T = 1`.
---
## 1 · WHAT HAPPENED

### The leg, and the two ways it could have gone wrong
`E1a` is a symbol table and one question: are ρ and φ the same kind of object? **Run against the
three manuscripts it returns "same kind"** — the papers do not disclose what happens to their own
unrecognised remainders, because no paper has a reason to. **Run against the two implementations it
returns "different in kind"**, on `recognised_flow[:] = 0.0` against `C(t+1) = C(t) + φ·ΔE +
α·gap(t)`. The design says a difference in kind ends the leg: a simulation cannot rescue an
equation between objects of different type.

**`E1b` was run anyway, and it should not have been.** `E1a`'s manuscript pass returned "same kind",
`E1b` was launched on that reading, and the corpus audit *inside E1* then surfaced `REVIEW-004` §E2
while the sweep was still computing. The clause was broken; the result document says so in its own
§5.1 rather than in a footnote. **Nothing was rescued by a simulation** — `E1b` corroborates the
FAIL from a direction the type check cannot see — but that is mitigation, not exoneration.

### What `E1b` found, which is worth more than its verdict
`scripts/e2e001_e1_iso_kappa.py`, 20 seeds, five κ targets fixed before any statistic was computed.
The iso-κ locus is wide and real: at κ\* = 0.005, ρ falls twentyfold while *r* rises eighteenfold
and every registered observable moves less than one seed spread. **Read alone that says REFUTED and
hands Paper II a non-identification result.** The disclosed sensitivity is what stops it:

| *N* | drift (Gini) | seed SD | separation |
|---|---|---|---|
| 800 | 0.003538 | 0.007003 | 0.51× |
| 1600 | 0.003520 | 0.003646 | 0.97× |
| 3200 | 0.003690 | 0.004086 | 0.90× |
| 6400 | 0.003558 | 0.002250 | **1.58×** |

**The drift is flat to three significant figures across an eightfold *N* while the noise falls.**
Paper II's degeneracy is *resolution-limited* and emerges near *N* ≈ 3 × 10⁴. Paper III's is
**exact**, at 7 × 10⁻¹⁴. Two degeneracies, one real and one an artefact of sample size, are not one
shared structure — which is `E1a`'s verdict arriving by a second road.

### The find: the answer was already here
| | |
|---|---|
| `REVIEW-004` **§E2** (2026-08-12) | *"They are not the same structure … **Non-arrival and deferred arrival are different dynamical objects**."* — the finding that decides `E1a`, made four days early |
| `REVIEW-004` **§E3** | titled ***"What it would mean to fail as a SYSTEM — the answer to your open question"***, five ranked modes; **mode 1 is *"the conjunction is a coincidence of vocabulary (most likely, and already partly true)"*** with diagnostic *"write the bridge proposition between ρ and φ"* — **which is E1** |
| `END-TO-END-001` **§0** (2026-08-16) | *"left one question open with **no written answer anywhere in this repository**"* |
| `REVIEW-004` **A2** + `ROADS-001` §5 | E1's audit half — *"κ is the budget, and the budget does not determine the outcome"* — against the design's *"no document in this repository mentions it"* |

**The design's premise was false and its value is undiminished**, which is the interesting part.
`END-TO-END-001` is a registration and **was not edited**; `RESULT-…-E1.md` §3/§3.1 is the record.

### Admission accounting, because it is the whole point
`E1`'s FAIL rests on a pre-existing finding, so **`E1` counts the verdict and not the discovery**.
Its one piece of genuinely new system-level content is the **exact-versus-resolution-limited**
contrast, which needs both papers plus a measurement nobody had run. Four other findings were
reclassified `P7` and score nothing (the (*r*, ρ) reparameterisation — `ROADS-001` already had it;
the κ under-determination; two Paper II defects repaired in passing). **TEST legs run 1, TEST legs
failed 1, AUDIT legs run 0. No combined score exists.**

| | |
|---|---|
| suite | **1068 passed**, ~66 s, zero skips |
| red-proof | **37 mutations, 0 survivors**, 2 skipped |
| defensive sentences | paper-II **0/0**, paper-IV **0/0** — unchanged by the edits |
| board | 59 criteria, 45 met (unchanged — see §4) |
| lessons | **5 banked** (3 global, 2 project) · 2 `use` calls at student-in |
| commits | `91e26cd` the run · `28bf7c2` the remedy · this file |
---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-55`'s rulings stand verbatim**, including: `END-TO-END-001` IS FIXED
  AND MAY NOT BE EDITED IN RESPONSE TO A RESULT (`END-TO-END-002` is the repair path); A LEG MAY
  NOT COUNT A FINDING MADE BEFORE IT EXISTED; TEST AND AUDIT COUNTS ARE REPORTED SEPARATELY AND THE
  VERDICT COUNTS TESTS ONLY; THE ADMISSION CRITERION IS NOT ADVISORY; REG-013's DECISION RULE IS
  SPENT; H1 LICENSES OCCUPANCY; `P2`/`P3`/`P5` STAY MANUAL; ADR-001's TITLE AND §Decision FROZEN;
  THE ABSTRACT IS A SUBMISSION FIELD; THE ARM IS δ; DO NOT SPEND THE TIE-BREAK; **R5 IS UNSPENT**;
  T4's WIDTH IS 31.7 %; **T2 MAY NOT BE RUN ON THIS DATA**; §4.7 IS PINNED AT `ba59370`; `wt107` IS
  NOT EDITED; APPARATUS SUB-ROWS ARE GENERATED; A ROW IS NOT DONE UNTIL SEEN RED; A `WEAK` VERDICT
  IS A CLAIM ABOUT THE HARNESS; `P8` IS ONE PASS TAKEN LAST; `P7` DOES NOT CLOSE THE CORPUS; DONE
  IS "CLEARED FOR LIFTOFF"; **`P13` IS LAST**; `P13` IS A PDF *AND A RECIPE*; **ROW IDS ARE NEVER
  RENUMBERED AND FILE ORDER IS DEPENDENCY ORDER.**
- **NEW · `T = 1`. THE PASS IS `WOUNDED` IF E2, E3 AND E5 ALL CLEAR AND `FAILS` IF ANY ONE OF THEM
  DOES NOT.** That is §3's rule, not a preference, and it is now one leg from either branch.
- **NEW · E1's DEMOTION IS APPLIED AND IS NOT REVISITED.** Paper II §3.2's "same structure"
  sentence is withdrawn; Paper IV §3 says *"three instances of one question, asked at three
  scales"*. It was written before the run precisely so a later session could not argue with it.
- **NEW · THE `T ≥ 2` REMEDIES ARE NOT SPENT AND ARE NOT FORGOTTEN.** Paper IV's abstract
  (*"the same atomic unit composes from the household to the sovereign"*) and `ADR-001`'s addendum
  belong to the system-fail branch. `-56` deliberately did **not** touch them. **Whoever lands the
  second TEST leg owns that decision**, in either direction, and must say which.
- **NEW · DO NOT EDIT `src/wealth_tensor/`.** Paper II §7 pins `d655501` as *"the last commit
  touching `src/`"* and calls it the state of the code that produced its numbers. A purely additive
  statistic on `run()` moves that pin and breaks a published provenance claim. Measure from
  `scripts/`.
---
## 3 · THE AT-BAT for `-57` — **E3, THE CONTAINMENT MATRIX**
**Ranked first, and the ranking has a reason that did not exist yesterday.** With `T = 1`, §3's
verdict is one leg from `FAILS`, and the `T ≥ 2` branch's *first* consequence is *"Papers II and
III are unaffected and ship as independent works — `ADR-001` §Consequences' containment promise
being **cashed**."* **E3 is the leg that tests whether that promise is true.** If the corpus is
about to lean on containment, the session that leans should be the one that checked it.

- **It is quotation-only.** A 3 × 3 matrix, each cell justified by a cited sentence from the
  depended-on paper. No simulation, no new instrument, no seeds. Cheap and it cannot be fudged.
- **It has a known partial answer to beat.** Paper IV §9.3 already declares one direction. The
  design's three failure shapes are: not lower-triangular in II → III → IV order; striking one
  paper removing claims from **both** others; or the corpus's whole empirical content sitting in
  one cell.
- **Read `REVIEW-004` §E3 mode 3 first** — *"No joints — an anthology with a system's ambition …
  cross-references are decorative **by design** (REVIEW-001 F9 enforced it)"*. That is a stated
  prior about what E3 will find, from the document that has now been right twice. **It does not
  excuse you from running the leg** (the design forbids skipping a leg whose answer seems obvious)
  and it does tell you where to look.
- **Then `E5`** — the over-subscribed guard, also cheap, also a TEST, and `P3n` already established
  the repair shape. `E2` wants a genuinely blind pass and is the one leg whose value a rushed
  session can destroy by reading §2's candidate first.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The honest alternatives:
- **`P7` on Paper IV, §3 and §8 first.** `-56` has just added a paragraph to each and both are new
  prose in the paper's most load-bearing section. Fresh eyes are worth real money there — and E1 is
  done, so the "you are polishing prose E1 may reopen" objection is **spent for §3**. Defensible
  and possibly better than E3 if you would rather ship than adjudicate.
- **`P7` on Paper II** — §3.1, §3.2 and §7 all changed today.
- **`P6`'s remaining two thirds.** `P1n`/`P5n` are `P3n` repointed. Mechanical, ~30 minutes.
- **`P13`.** **STILL LAST**, and now sharper: §3 makes `P13`'s subject matter conditional on the
  verdict, and the verdict is one leg from "three works, not one stack."
- **Rule on Jason's three `-51` scoping proposals** — (a) audit the CLASS not the constraint;
  (b) bound by value; (c) audit at the BOUNDARY. `-56` is the **tenth** consecutive session (a)
  would have caught. **THE GUARD PROGRAMME REMAINS PAUSED** (Jason, 2026-08-15).
---
## 4 · TEED UP, IN ORDER
- **`P11` HAS NO WAY TO SHOW THAT ONE OF SIX LEGS IS RUN, AND `-56` DELIBERATELY DID NOT FIX IT.**
  The board reads 45/59 today and read 45/59 yesterday; a fresh session would conclude `P11` is
  untouched. The right repair is six sub-rows `P11a`–`P11f`, one per leg — **but a new `cmd:` row is
  not done until it has been seen red**, so each needs a mutation in `redproof_apparatus.MUTATIONS`
  that makes it fail. That is a real half-hour, it is the correct half-hour, and doing it badly
  (green-only rows) is worse than the gap. **Row ids are never renumbered; file order is dependency
  order.** Take this before E3 if you would rather leave the board honest than the corpus audited.
- **`REVIEW-004` AND `ROADS-001` ARE UNRULED AND HAVE NOW BEEN RIGHT TWICE.** A2 calls Paper II's
  title claim fatally refuted by its own table; Road One is the re-cut that follows. Paper II still
  carries the title. **This is a Jason-sized ruling, not a Claude-sized one** — but a Claude can
  write the one-page "here is what A2 costs and what Road One buys" that makes it a five-minute
  decision. Nobody has.
- **`G-AL`'s REMEDY LINE STILL DOES NOT WORK AS PRINTED** — *"Read it: ~/Scripts/charter-read.sh"*
  with no slug exits 2. The gate knows the slug and prints it in the same sentence. One line. Third
  session it has been carried.
- **`G-T` calls a STALE claim LIVE and tells the owner not to commit.** `-52`'s find, unfixed.
  `-56` hit the same family from the other side (§6) — the roster cannot tell a ghost from a
  sibling and neither can the gate.
- **`~/.local/state/claude-session/current` is a single global file** and Jason runs 2–3 sessions.
  One grep would find everything else that reads it.
- **`P1n` and `P5n`** — `P3n` repointed. Half an hour, moves `P6`.
- **The use/mention guard, generalised.** Applied in exactly one place.
- **C26 limb B** — carded `1217525563299334`. **RESULT-REG-003 §2's "Every cut lands in R1"** —
  carded `1217518687033967`.
- **Cell (b), ranked in §3.2 — THREE entries left**, measured, paused behind the papers.
- **No probe has ever mutated `src/` except G7/G8.** And now `src/` is pinned — see §2's last
  ruling before you plan one.
- **C37's tripwire** — REG-009 §12's "never by narration". **§7's ledger dilutes its own two
  load-bearing rows** — Jason's call, TRIPWIRED not carded.
- **Dossier era, re-served by nobody:** REVIEW-004 C6 (ASC 410) and C10 (IAS 36's reversal
  asymmetry). *C10 is REVIEW-004's, not the inventory's; the collision has bitten three times.*
- **REG-013 re-run worth doing:** the biophysical audience was capped at 4 000 of 7 801.
- Infra siblings, carded: Caddy `1217488447555628` · capability path `1217488117177482` ·
  AAR A2's four post-\* hooks · card-lint `1217483699706758` · gate `1217465036940491`.
---
## 5 · DO NOT
- **Everything `-31`→`-55` forbade still stands verbatim** — R5, the two sensitivities,
  `selected_lives`, §4.4's 0.3000, T4's 31.7 %, the δ arm, TERM-001/002, §9's list well-formedness,
  `wt107` IS NOT EDITED, §4.7 IS PINNED AT `ba59370`, DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD, DO
  NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION, DO NOT GRADE A CONSTRAINT FROM THE
  `machine` COLUMN, DO NOT WIDEN C07's GUARD, DO NOT WRITE AN OVER-BREADTH SELF-TEST WITH AN ABSENCE
  PREDICATE, DO NOT SLICE THE SWEEP LOG BY SLUG, **DO NOT TYPE A FULL SHA YOU HAVE NOT RESOLVED**,
  DO NOT LEAVE A FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT CORRECTS, DO NOT MEASURE A
  TEXT LENGTH WITH `wc -w`, DO NOT LET A `manual:` ROW BE SCORED BY WHOEVER DID THE WORK, DO NOT RUN
  `board.py` BY HAND, DO NOT ROUTE BIBLIOMETRIC API WORK THROUGH THE CLOUD CONTAINER, DO NOT
  HAND-EDIT A `P1x`/`P3x`/`P5x` ROW, DO NOT TRUST A GREEN CLONE, DO NOT "STRENGTHEN" A CHECK A
  MUTATION HARNESS CALLED WEAK UNTIL THE MUTATION IS SHOWN TO LAND.
- **NEW · DO NOT ADD AN OBSERVABLE TO A LEG'S OWN FAILURE CRITERION.** `E1b` measured
  Var[log *w*] as well and it is reported as **supplementary**, outside the verdict, because the
  design fixes three observables. A run that widens its own test has re-chosen a fixed clause.
- **NEW · DO NOT READ `E1b`'s REFUTED-SHAPED NUMBERS AS A RESULT.** They are in the record because
  hiding them would be worse. The leg failed at `E1a` and `E1b` was not entitled to run.
- **NEW · DO NOT EDIT `src/`** (§2). **DO NOT `--no-verify` PAST `roster-brake`** — `ROSTER_BRAKE_ACK=<n>`
  is the exit that leaves a reader something true.
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe with `while pgrep`. **Do not edit shared infra a sibling is mid-edit on.**
---
## 6 · TRANSPORT — darlish, zero-bridge (worked first try, `-06` → `-56`)
Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. **Never restart the app to fix darlish.** `darlish-check` is not in
the cloud kit; do not chase its 127. `roster leave` ONCE at wrap.
- ⚠ **NEW · A ROSTER CLAIM CAN BE A GHOST, AND THE TEST IS THE WORKING TREE.** `-56` opened to
  `roster who` showing `cloud-5X4JlAFI` (i.e. `-55`) live on wealth-tensor, synthetic, Scripts and
  claude-blackbook, 30–40 minutes old. It was dead: **`git status` was empty, `HEAD` was `-55`'s own
  wrap commit, and its roster task string was its handoff line.** Those three together are the
  measurement. `roster-brake` will then block your first multi-path commit as an `add -A` shape —
  **`ROSTER_BRAKE_ACK=<staged count>`** is the honest exit, and it verifies the count.
- ⚠ **SET `GATE_ROSTER_WHO` INLINE** — `dx` spawns a fresh shell per call and carries no
  environment. **`export` works inside a script you `--put` and run with `bash /tmp/x.sh`**, which
  is the right default for anything with more than one step.
- ⚠ **`roster claim`/`join` BOTH need `--who`**; `claim` takes `--resource`, not `--repo`.
  `record-outcome <tag> pass` is two positionals.
- ⚠ **`gate-selfcheck.sh` TAKES ~5–8 MINUTES AND A FOREGROUND `Bash` CALL DIES AT 8m20s.** Detach:
  `nohup env GATE_ROSTER_WHO=big-<sess> bash -c "$HOME/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1" &`
  then `sleep 300; grep -E "GATE SELF-CHECK|^  FAIL" /tmp/gate.log`. **COMMIT EVERYTHING FIRST**
  and **re-stamp the charter immediately before it.**
- ⚠ **HEREDOCS INSIDE `dx '...'` DO NOT SURVIVE — AND `-56` LOST ONE PROVING IT AGAIN.** A
  `python3 - <<PYEOF` inside the `dx` argument worked three times and then shattered mid-string on
  the fourth with `unterminated triple-quoted string literal`. **It is not "usually fine"; it is
  luck.** Write locally, `--put`, run with `bash`. A nested heredoc **inside** a `--put` script is
  fine and is how every multi-step edit in this session shipped.
- ⚠ **NON-ASCII IN A `--put` SCRIPT: WRITE THE LITERAL CHARACTER.**
- ⚠ **`--get` NEEDS THE FULL PATH; a leading `~` expands in the CLOUD and fails.** `--put` accepts
  `~`. Small diffs do not need a tarball: `cat f | /tmp/dx --put /Users/jasoncbraatz/repos/...`.
- ⚠ **`lessons.py` AUTO-COMMITS AND AUTO-PUSHES each leaf.**
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started ·
  `5` crossed but mismatched.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
**SUITE:** 1068 collected, 1068 passed, zero skips — darwin ~66 s, cloud ~175 s.
`defensive_count.py` takes a positional path and **only a DELTA means anything**. **Adding a
manuscript to `docs/papers/` fails the suite until you add it to
`test_defensive_count.py::MANUSCRIPTS`, commit a `DEFENSIVE-BASELINE.json` beside it, AND register
it in `redproof_apparatus.PAPER`.** **`e2e001_e1_iso_kappa.py` is ~130 s at 20 seeds and five
targets with `--resolution`; `--quick` is a 12 s smoke test.**
---
## 0 · THE TELL, NOW IN EIGHTY-FOUR SHAPES
`-28` through `-55`'s tells all stand (the instrument-artefact question of numbers that look GOOD,
that SETTLE AN ARGUMENT, of a REGISTERED CONTROL THAT FAILS, OF THE DENOMINATOR; a guard must scan
assertions not quotations; a mutation that does not mutate reports your guard as weak; pre-commit
the FAVOURABLE outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT; a correction
that lives only in a handoff has not been made; a rule can be false on the day it is written; a
guard that cannot tell use from mention scores the mention; a criterion that passes because it does
not apply is a blank line wearing a tick; a system of documents can hold a contradiction no
per-document review can find; a tool that asserts more than it measured grows workaround prose; a
test whose outcome the designer can predict is not a test). `-56` adds three:

- **A TYPE CHECK RUN AGAINST PROSE AND THE SAME CHECK RUN AGAINST CODE CAN DISAGREE, AND THE
  DISAGREEMENT IS THE RESULT.** Two papers said their two parameters were "the same structure".
  The manuscripts say "same kind"; the implementations say "different in kind", on the fate of the
  unrecognised remainder — deferred in one, destroyed in the other. **Neither paper states it,
  because no paper has a reason to describe what its own complement does.** A cross-document
  identification claim is checkable only against the code both documents pin.
- **A DESIGN DOCUMENT'S PREMISE IS A CLAIM AND IT IS THE ONE NOBODY CHECKS.** `END-TO-END-001` said
  a question had *"no written answer anywhere in this repository"* and built six legs on it. The
  answer was four days old, in a dossier its author had read, under a heading naming the question
  — **and the dossier had also already made the finding that decides leg one and stated leg one's
  audit half twice.** The defect is not memory, it is **indexing**: a finding filed under the
  document that produced it is invisible to a search for the question it answers. **Before writing
  "nowhere in this repository", grep the review documents for the question's own words.**
- **"INDISTINGUISHABLE" IS A STATEMENT ABOUT SAMPLE SIZE UNTIL YOU SCALE N.** A separation of
  0.51× the seed spread reads as a clean non-identification. Re-run at 2×, 4× and 8× the agents and
  the **drift is flat to three significant figures while the noise falls as 1/√N** — the pair is
  identified and the published design cannot see it. Any threshold phrased *"k times the noise"*
  inherits this. **Report the scaling beside the verdict, or the verdict is on loan** — and note
  that this one would have handed the corpus a result that dissolves at *N* ≈ 3 × 10⁴.
---
## 7 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.
**Coffee status:** ☕ TWENTY-TWO SESSIONS. The document written to be able to lose on behalf of the
whole corpus lost its first leg — and the fact that beat it had been sitting in `docs/` for four
days, correctly stated, filed under nothing. **The first thing the corpus's system test found out
about the corpus is that it does not read itself.** Five legs left, `T = 1`, one more loss and
Paper IV becomes a survey. 🥎
