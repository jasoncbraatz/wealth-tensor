---
project: wealth-tensor
gh_sha: baf91a60b8f0116ea0b3bce2bc920dae6baed910
updated: 2026-08-16
session: wealthTensor-55
gate_passed: true
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16, superseding the 'three preprints publicly posted' line carried since sessionZero): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF
`gh_sha` names the commit this file describes; **the only thing added after it is this file**,
so `--check` prints `ADVISORY: docs-only drift` and exits 0. Assert the exit code exactly
(`-39`); `| tail` masks it. That sentence is an **INVARIANT, not a description** — `-51` learned
that the hard way. If a post-wrap commit lands, repoint `gh_sha` and re-master this file.
**`-55` adds the modern reason it breaks: A LIVE SIBLING.** `-54` and `-55` ran concurrently on
one darwin working tree all afternoon. `-55` wrapped at `baf91a6`; if `-54` lands anything after
that, this file is describing a state that has moved, through nobody's error. **Run
`~/Scripts/roster who` BEFORE you trust the header**, and if a sibling is live on wealth-tensor,
repoint before you plan.
`gh_sha` is the full SHA from `git rev-parse`, not an expanded abbreviation.
---
## ORIENT — read these first, in this order
1. **`docs/END-TO-END-001.md`** — **NEW, `-55`'s deliverable, and the thing that decides the
   endgame.** `P11`'s system test, designed and deliberately NOT run. Six legs, each with a failure
   criterion, a refutation criterion and the corpus's **pre-registered** response to every outcome
   including failure. **Read it before you plan anything**, because §3's verdict rule is what
   `P13` renders and §2's E1 is what Papers II and IV may be about to say.
2. **`docs/CHECKLIST.md`** — the generated board. **`./scripts/regen-board.sh`, never `board.py`
   by hand.** As of `-55`: **59 criteria, 45 met, fourteen lines open** — `P13`'s remaining lanes
   plus the corpus rows. Never hand-tick.
3. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS.** Stamp it:
   `~/Scripts/charter-read.sh wealthTensor-<NN>` — POSITIONAL slug, no env var. **And re-stamp
   IMMEDIATELY BEFORE THE GATE whether or not you touched `done-criteria.tsv`** — see §4's first
   item; `-55` learned this the new way.
4. **`docs/adr/ADR-001-paper-decomposition.md`** — the last four addenda are `-54`'s and the third
   **replaced the Definition of Done**. Addendum 6 (`-08`) is the one `END-TO-END-001` answers.
   Title and §Decision stay **deliberately frozen** at four papers as the decision-as-made.
5. **`docs/adr/ADR-002`** — `-54`'s typography decision: Libertinus, loaded by path, vendored and
   checksummed. `P13c`/`P13d` closed.
6. **`docs/papers/paper-IV-composition/paper-IV.md` §3, §4.4.3, §9.2** — repaired by `-55`. Read
   §3's second paragraph: it is the corpus's first correction that no per-paper review could have
   produced.
7. **`scripts/gen_apparatus_rows.py`** — read the docstring before touching any apparatus row. All
   forty `P1x`/`P3x`/`P5x` rows are emitted from one template; a hand-edit is silently reverted.
8. `scripts/redproof_apparatus.py` + `tests/test_apparatus_rows_are_falsifiable.py` (37 mutations,
   0 survivors, ~1 s) · `python3 scripts/handoff_gate.py --check` · `PREPRINT-CHECKLIST.md` §A/§B/§D
   · `mutation_control.py --list` · `CONSTRAINT-INVENTORY-001.md` (**the guard programme is still
   PAUSED**).
9. REG-013 + `RESULT-REG-013` §4.1 · **REG-003 (its diagonality arm is what `-55`'s repair is
   about)** · REG-003 §§3.2/3.3/7 · SCOUT-001 · REG-012 §§6–7 · RESULT-TERM-001 · REG-010 §1/§4 ·
   CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (READ THE HEADER NOTE FIRST).
---
## `-55` in one line
**THE CORPUS'S FIRST SYSTEM-LEVEL TEST IS WRITTEN DOWN — AND WRITING IT FOUND A CONTRADICTION
BETWEEN TWO PAPERS THAT NEITHER PAPER'S OWN REVIEW COULD EVER HAVE SEEN.** Paper IV said
diagonality's test was *"open"* and *"until it returns"*. Paper III had run it and **rejected** it,
at 4.12× and 2.02×, *p* = 0.0002. Paper IV's own §9.2 was a conditional whose antecedent had become
true, so the paper carrying the corpus's composition chain **entailed that its own firm-scale link
was broken and did not know it.** Both papers were internally consistent. That is precisely why
`P11` exists, and it is no longer a hypothesis about the value of the exercise.
---
## 1 · WHAT HAPPENED
**The at-bat was `P11`'s DESIGN half and it is CLOSED. `P11` itself stays unticked and
`PENDING-HUMAN` — the running half is a later session's, by the row's own note.**

### `docs/END-TO-END-001.md` — the answer to a question this repo has carried unanswered since `-08`
> *What would it mean for the three papers to fail as a system, as opposed to one of them failing?*

Committed **before** anything was run, in its own commit (`4ea6361`), on the `REG-013` precedent.
Its structure, and the three parts of it that are load-bearing:

- **§1 states the system claim `S` so that it can fail** — that the three papers describe *the same*
  object's measuring layer at three scales, and that Paper IV's *"a chain rather than three
  analogies"* is the assertion under test. Everything attacks `S` and nothing else.
- **§1.1 · THE ADMISSION CRITERION.** *A leg is admissible only if a competent fresh-eyes review of
  any ONE paper could not have found it* — applied at design time to admit a leg, and again **at run
  time to every finding**. Anything a single-paper review could have found is reclassified `P7` and
  scores nothing. **This is the guard that stops `P11` becoming `P7` done three times**, which is the
  cheapest way for the exercise to fail while looking successful.
- **§2.0 · TEST vs AUDIT, classified in advance.** Three legs are TESTs (outcome unknown to the
  designer, can lose); three are AUDITs (outcome anticipated — the value is stating it whole, and
  the **remedy is pre-registered so the run cannot negotiate it afterwards**). The verdict rule
  counts TESTs only and **the run may not report a combined score.**

| leg | | class |
|---|---|---|
| **E1** | **the shared degeneracy — is the II↔III join load-bearing or vocabulary?** Paper III's series identifies the *product* φδ and never the factor. If Paper II's ρ and *r* stand in that relation to Paper II's observable, the corpus has an unstated non-identification result of the same shape. If not, the chain's sovereign link is a resemblance | **TEST** |
| **E2** | **the unowned claim** — a sentence three abstracts leave a reader holding that lives in none of them. Blind extraction first, with a named-candidate power check | **TEST** |
| **E3** | **the containment matrix** — `ADR-001` promised *"failure is contained"* in 2026-08-05 and nobody ever tested it. Quotation-only 3×3 | **TEST** |
| **E4** | **the corpus's empirical content, stated whole** — three papers each disclose their own share and the sum is nowhere | AUDIT |
| **E5** | **the over-subscribed guard** — two tests are cited by name in two papers each | **TEST** |
| **E6** | **the cross-paper contradiction** — shared facts compared by MODALITY, not just truth value | AUDIT |

**E1 is the spine and it is a real test.** The reason it can lose is in the code, not the paper:
`recognised_flow += rho * gain + wage`, then `assessed = max(recognised_flow, 0)`. **The wage enters
the base unscaled by ρ and the clip is non-linear**, so *r* scales the liability while ρ scales the
base's *dispersion* toward a wage floor. Whether the observable can tell those apart at matched κ
is not stated anywhere in the corpus and was not obvious to the session that wrote the leg.
Thresholds fixed: κ matched to **1 %**, separation **≥ 3×** the within-point seed spread over
**≥ 20 seeds** = FAIL, **≤ 1×** = REFUTED, between = UNDECIDED and **not rounded toward comfort**,
no locus = **VOID**.

**And E1 carries an audit half the corpus has already published without noticing.** Paper II §3.1
reports Gini **0.222 against 0.125** at matched κ ≈ 0.10 across the two bases — κ *under-determines*
the outcome — while Paper III's φδ determines the reported series exactly. **That is a prima facie
disanalogy sitting in numbers both papers already print, and no document in this repository
mentions it.**

### The find: Paper IV did not know its own chain was broken
Found while **reading the three papers to design the legs** — not by running one — and repaired in
the commit immediately after the design (`93e9c7c`), because a correction that lives only in a
document has not been made. **`END-TO-END-001` §2/E6 excludes it from E6's run in terms: a leg does
not get credit for a finding made before it existed.**

| | |
|---|---|
| Paper III §9.9 / §5.4 | *"The diagonality of the reporting layer is an assumption, it was testable, and **it is false**"* — independence rejected in **both** universes, same direction, **4.12× and 2.02×**, both *p* = 0.0002, power 1.00 at a 5 % injected excess (headline survives the tag-list repair at 4.01× / 2.10×) |
| Paper IV §4.4.3 | *"Paper III registers the test. **Until it returns**, the composition chain has an unverified link"* |
| Paper IV §9.2 | *"its test is **open**. **If** recognition events cluster within firm-quarters, the Hadamard form in §3 is wrong and the chain has a broken link"* |

**The antecedent is true.** Three sites repaired, plus §3's *"it is diagonal over asset classes"*
→ *"is **written** as diagonal"* so the section does not assert what its own next paragraph rejects.

**The repair reports the result rather than deleting the chain**, and says the two things that run
against the paper's convenience:
1. **what was rejected is the REPORTING layer's clean composition, not the extensive state's** —
   diagonality is a property of the *filter*, and Paper IV's composition claim is about the *state*,
   which adds however it is recorded. The link is **degraded, not severed**. The honest cost is that
   the firm's *reported* object no longer composes from its classes' reported objects without
   cross-terms, which is the scale anyone actually reads;
2. **the cause is unidentified** — ASC 350-20-35-31/35-32 sequence the tests, so Paper III's design
   cannot separate an economic coupling from an accounting artefact, and **Paper IV may not read the
   rejection as evidence that the underlying degradations are coupled.**

*The `P7` note for whoever polishes Paper IV: §3's second paragraph is new and long. It is right,
and it may want tightening. Do not tighten away clause 2.*

### Bug spray — two tools that asserted more than they measured
Both in `~/Scripts`, `.bak` beside each, both syntax-checked and re-run end to end. **`darwin-mac-ops`/
`Scripts` was taken off a STALE claim** (`cloud-oaujFobu`, 7 h+); §4 of the previous handoff
nominated the first of these for whichever session wanted a small win.

| | |
|---|---|
| `charter-read.sh` | printed `full board: <dir>/DONE.md` and `<dir>/design/ARCHITECTURE.md` **unconditionally**. Neither exists in wealth-tensor, so every stamp since `-53` told the reader to go and read two things that are not there. Each pointer now prints only if the file exists. **Found `-53`, confirmed `-54`, fixed `-55`** |
| `handoff-kit/board.py` | printed **"The next piece is `X`."** — a *scheduling* claim. It knows OPEN status and file order and **nothing about a project's rulings on sequence.** wealth-tensor is the worked case: `P13` is its only OPEN lane and a standing ruling says `P13` is LAST, so **the previous handoff carried a whole paragraph titled "FIRST, THE TRAP" to disarm one generated sentence.** Now reports what it measured — *"the first OPEN lane in dependency order"* — and says a project's ordering rulings outrank it |

**The shape both share is one tell** (§0). Neither could fail loudly, so both stayed wrong quietly
and **the artefacts grew prose to work around them.**

| | |
|---|---|
| suite | **1068 passed** on darwin (~66 s), zero skips |
| red-proof | **37 mutations, 0 survivors**, re-run after the Paper IV edit |
| defensive sentences | paper-IV **0/0** against a **0/0** baseline — unchanged by the repair |
| board | **59 criteria, 45 met** |
| lessons | **5 banked** (4 global, 1 project) · `use` + `record-outcome … pass` both run on `wt55-p11-design` |
| commits | `4ea6361` design · `93e9c7c` Paper IV repair · `baf91a6` board · `~/Scripts` `49826c7` |
---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-54`'s rulings stand verbatim**, including: REG-013's decision rule is
  SPENT; H1 licenses OCCUPANCY, not fertility; `P2`/`P3`/`P5` stay manual; ADR-001's title and
  §Decision are frozen; the abstract is a submission FIELD (`check_abstract_size.py`, never
  `wc -w`); no third disclosure instrument; phrase set frozen at 38; SOURCE-001 FINISHED; THE ARM
  IS δ; §4.8 IS NOT THE COINCIDENCE ARGUMENT, §4.7 IS; REG-009 CLOSED; DO NOT SPEND THE TIE-BREAK;
  DO NOT PROMOTE R_MIN; **R5 IS UNSPENT**; 55.71 % IS Ψ's AND 63.16 % IS THE BAND COUNT'S; T4's
  WIDTH IS 31.7 %; **T2 MAY NOT BE RUN ON THIS DATA**; §4.7 IS PINNED AT `ba59370`; `wt107` IS NOT
  EDITED; APPARATUS SUB-ROWS ARE GENERATED, NOT WRITTEN; A ROW IS NOT DONE UNTIL IT HAS BEEN SEEN
  RED; A `WEAK` VERDICT IS A CLAIM ABOUT THE HARNESS; `P8` IS ONE PASS OVER THE WHOLE CORPUS TAKEN
  LAST; `P7` DOES NOT CLOSE THE CORPUS; DONE IS "CLEARED FOR LIFTOFF", NOT "POSTED"; **`P13` IS
  LAST, NOT NEXT**; `P13` IS A PDF *AND A RECIPE*; A CRITERION THAT CANNOT BE REACHED IS WORSE THAN
  ONE THAT FAILS; **ROW IDS ARE NEVER RENUMBERED AND FILE ORDER IS DEPENDENCY ORDER.**
- **NEW · `END-TO-END-001` IS FIXED AND MAY NOT BE EDITED IN RESPONSE TO A RESULT.** Its §5 says
  which clauses are fixed. If a leg turns out mis-specified the repair is a **second registration**,
  `END-TO-END-002`, that says so and why — the `REG-001` precedent — **not an edit to the file.**
  This is the single easiest ruling in the project to break, because the file is a design document
  and design documents feel editable. It is a registration.
- **NEW · A LEG MAY NOT COUNT A FINDING MADE BEFORE IT EXISTED.** E6's diagonality catch is `-55`'s
  and is excluded from E6's run by the design's own text. A run that scores it has inflated itself.
- **NEW · THE RUN REPORTS TEST AND AUDIT COUNTS SEPARATELY, AND THE VERDICT COUNTS TESTS ONLY.**
  "Five of six legs clear" is not available and never was.
- **NEW · THE ADMISSION CRITERION IS NOT ADVISORY.** Every finding the run produces gets asked
  *could a single-paper review have found this?* If yes it is a `P7` finding and scores nothing.
---
## 3 · THE AT-BAT for `-56` — **RUN `E1`, THE ONLY LEG THAT MUST GO BEFORE `P7`**
**The design is fixed and the legs are now schedulable. They do not all want the same slot, and
this is the one piece of sequencing `END-TO-END-001` deliberately left open (§5) — so it is a
recommendation, not a clause, and you may overrule it in one line.**

**Take `E1`, both halves, and take it now:**
- **It is the only leg whose result changes what the papers SAY.** E2/E3/E5/E6 grade the text.
  **E1 can add a result to Paper II and a sentence to Paper IV** — and if `P7` polishes those
  sections first, `P7` polishes prose E1 is about to rewrite. **Everything else in the design is
  better run AFTER `P7`, on the text that will actually ship; E1 is the one that must run before.**
- **It is prose-independent**, so nothing `P7` does can overtake it.
- **It is cheap.** `src/wealth_tensor/redistribution.py` and `scripts/wt030_report.py` exist; the
  leg is a sweep, a locus, three statistics and a seed-noise yardstick.
- **`E1a` FIRST and it can settle the whole leg on its own.** Build the symbol table across the
  three papers. **φ is a share of a *change* (a degradation) that reaches the claim layer; ρ is a
  share of a *gain* that is recognised as flow.** If those are different in kind, "same structure"
  fails at E1a and **E1b is not run** — a simulation cannot rescue an equation between two objects
  of different type.
- Then `E1b`: locate the iso-κ locus **numerically, off the committed code, never off the paper's
  closed form**, and compare **Gini, top-decile share and Var[log a]** — the third because Paper II
  §3.1 already uses it to show two levies at one κ can act on different objects. That is the
  discriminating instrument and it is already in the corpus.
- **Write `docs/RESULT-END-TO-END-001-E1.md`** in the shape of the other `RESULT-*` documents: what
  was run, what came back, drop accounting, verdict read off §2's rule rather than off your
  judgement. The corpus's response to each outcome is **already written** in the design's E1 table.
  Apply it; do not renegotiate it.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The honest alternatives:
- **`P7` on Paper IV, §4 first and hard.** Still the highest-value prose target in the estate:
  load-bearing, drafted by one Claude in one pass, and ADR-001 predicted the unforced error lives
  there. **`-55` has just added a long new paragraph to §3 that would benefit from fresh eyes.**
  Defensible — but you are polishing §3/§4.4/§9 that E1 may reopen, so say you accept that.
- **`P7` on Paper II** — also unreviewed. Same caveat: E1's refuted branch adds a §3.x to it.
- **`P6`'s remaining two thirds.** `P1n`/`P5n` are `P3n` repointed at Papers III and IV; the
  generator has the shape and needs each paper's regenerating command. Mechanical, ~30 minutes,
  moves the last corpus-level row with a writable check.
- **`P13`.** Eight lanes were open, two closed by `-54`. **STILL LAST, and now for a second and
  sharper reason: §3 of the design makes `P13`'s subject matter conditional on the verdict.** If the
  system fails, `P13` renders *three works*, not one stack. Building the deliverable before `P11`
  lands is building a picture of a corpus that may not be one.

**THE GUARD PROGRAMME REMAINS PAUSED** (Jason, 2026-08-15). **Jason's three `-51` scoping proposals
are STILL UNRULED** — (a) audit the CLASS not the constraint; (b) bound by value; (c) audit at the
BOUNDARY. `-55` is the **ninth** consecutive session (a) would have caught, and `-55` is a
particularly clean instance: **`END-TO-END-001`'s E5 leg is proposal (a) pointed at the test suite,
and E6 is proposal (a) pointed at the prose.** Two independent sessions have now half-implemented
the same unruled proposal. **A ruling would be worth more than another session of finding out.**
---
## 4 · TEED UP, IN ORDER
- **NEW, AND IT COST `-55` A NEAR-MISS · RE-STAMP THE CHARTER IMMEDIATELY BEFORE THE GATE, ALWAYS.**
  `G-AL` compares your stamp against `done-criteria.tsv` **as it stands at wrap**, and Jason runs
  2–3 sessions **on one darwin working tree**. `-55` stamped `wealthTensor@1a3c2ab` at student-in
  and `@56da9dc` an hour later **without ever touching the file** — `-54` closed `P13c`/`P13d` in
  the same tree. The previous handoff framed this as "if you amend the criteria, re-stamp." **That
  is too narrow. A live sibling invalidates your stamp while you are innocent**, and `G-AL`'s
  message — *"the definition of done was amended after you read it"* — reads like you did it.
  Fix shape: have `G-AL` name the amending session when it can, and say *"by you or by a sibling."*
- **`G-AL`'s REMEDY LINE STILL DOES NOT WORK AS PRINTED** — *"Read it: ~/Scripts/charter-read.sh"*
  with no slug exits 2. The gate knows the slug and prints it in the same sentence. One line.
  *(`-55` was in this file and did not fix it — it is in the gate, not in `charter-read.sh`, and
  `-55` had already taken `Scripts` off a stale claim once. Small, free, unclaimed.)*
- **`G-T` calls a STALE claim LIVE and tells the owner not to commit.** `-52`'s find, unfixed,
  warning-level. Same family as `G-AL`: a check that cannot identify who is asking.
- **`~/.local/state/claude-session/current` is a single global file** and Jason runs 2–3 sessions.
  `G-AL` no longer trusts it; **anything else reading it has the same bug.** One grep would find them.
- **JASON'S THREE `-51` SCOPING PROPOSALS ARE STILL UNRULED.** See §3's last paragraph — the
  evidence for (a) is now two sessions deep and arrived from two different directions.
- **`P1n` and `P5n`** — `P3n` repointed. Half an hour, and it moves `P6`.
- **The use/mention guard, generalised.** `P*i` forbids the marker rather than the word; the general
  repair is banked and applied in exactly one place. Other guards in this repo grep for vocabulary.
- **C26 limb B** — carded `1217525563299334`. §2's twelve ratios with no counts.
- **RESULT-REG-003 §2's "Every cut lands in R1"** — carded `1217518687033967`. Dated addendum
  (`-37` precedent).
- **Cell (b), ranked in §3.2 — THREE entries left**, measured, **paused behind the papers.**
- **No probe has ever mutated `src/` except G7/G8.** `redproof_apparatus.py` is the worked shape.
- **C37's tripwire** — REG-009 §12's "never by narration"; §3.3 names the adjacent check.
- **§7's ledger dilutes its own two load-bearing rows** — Jason's call, TRIPWIRED not carded.
- **Dossier era, re-served by nobody:** REVIEW-004 C6 (ASC 410) and C10 (IAS 36's reversal
  asymmetry). *That C10 is REVIEW-004's, not the inventory's; the collision has bitten three times.*
- **REG-013 re-run worth doing:** the biophysical audience was capped at 4 000 of 7 801, which
  **suppresses** its overlaps and is the one bias favouring H1.
- Infra siblings, carded: Caddy ordering `1217488447555628` · capability path in cleartext
  `1217488117177482` · AAR A2's four post-* hooks · card-lint `1217483699706758` · gate
  `1217465036940491`.
---
## 5 · DO NOT
- **Everything `-31`→`-54` forbade still stands verbatim** — R5, the two sensitivities,
  `selected_lives`, §4.4's 0.3000, T4's 31.7 %, the δ arm, TERM-001/002, §9's list well-formedness,
  `wt107` IS NOT EDITED, §4.7 IS PINNED AT `ba59370`, DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD, DO
  NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION, DO NOT GRADE A CONSTRAINT FROM THE
  `machine` COLUMN, DO NOT WIDEN C07's GUARD, DO NOT WRITE AN OVER-BREADTH SELF-TEST WITH AN ABSENCE
  PREDICATE, DO NOT SLICE THE SWEEP LOG BY SLUG, **DO NOT TYPE A FULL SHA YOU HAVE NOT RESOLVED**,
  DO NOT LEAVE A FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT CORRECTS, DO NOT OBEY A DO-NOT
  THAT NAMES A MACHINE WITHOUT RUNNING THE MACHINE, DO NOT MEASURE A TEXT LENGTH WITH `wc -w`, DO
  NOT ADD A REQUIRED KEY TO A GATE WITHOUT REBUILDING ITS FIXTURES, DO NOT LET A `manual:` ROW BE
  SCORED BY WHOEVER DID THE WORK, DO NOT RUN `board.py` BY HAND, DO NOT READ A CO-CITATION NUMBER
  WITHOUT ITS TWO CONTROLS, DO NOT ROUTE BIBLIOMETRIC API WORK THROUGH THE CLOUD CONTAINER, DO NOT
  PUT A COLON OR COMMA INSIDE AN OPENALEX `filter=` VALUE, DO NOT HAND-EDIT A `P1x`/`P3x`/`P5x` ROW,
  DO NOT TRUST A GREEN CLONE, DO NOT "STRENGTHEN" A CHECK A MUTATION HARNESS CALLED WEAK UNTIL THE
  MUTATION IS SHOWN TO LAND, DO NOT WRITE A FORBIDDEN-TOKEN GUARD THAT WOULD FIRE ON A DOCUMENT
  DISCUSSING THE THING IT FORBIDS.
- **NEW · DO NOT EDIT `END-TO-END-001.md` IN RESPONSE TO A RESULT.** It is a registration wearing a
  design document's filename. `END-TO-END-002` is the repair path.
- **NEW · DO NOT RUN A LEG YOU EXPECT TO LOSE ANYWAY BY SKIPPING IT.** A leg skipped because its
  answer seemed obvious is the same failure mode as designing the test after the results, and the
  design says so in §6.
- **NEW · DO NOT BUILD `P13` BEFORE `P11` LANDS.** What the deliverable depicts is now
  *conditional on the verdict* — one stack, or three works.
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe with `while pgrep`. **Do not edit shared infra a sibling is mid-edit on** — check
  for a `.bak` dated today before you reach for `~/Scripts/`.
---
## 6 · TRANSPORT — darlish, zero-bridge (unchanged, worked first try, `-06` → `-55`)
Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. **Never restart the app to fix darlish — it is not on the bridge.**
`darlish-check` is not in the cloud kit; do not chase its 127. `roster leave` ONCE at wrap.
- ⚠ **SET `GATE_ROSTER_WHO` INLINE** — `dx` spawns a fresh shell per call and carries no
  environment. **`export` DOES work inside a script you `--put` and run with `bash /tmp/x.sh`**, and
  that is the right default for anything with more than one step. `-55` ran every commit, every
  patch and the whole lesson batch that way; **zero heredoc losses, zero round trips lost.**
- ⚠ **`roster claim`/`join` BOTH need `--who`** even with `GATE_ROSTER_WHO` set; `claim` takes
  `--resource`, not `--repo`. `record-outcome <tag> pass` is two positionals.
- ⚠ **`gate-selfcheck.sh` TAKES ~5–8 MINUTES AND A FOREGROUND `Bash` CALL DIES AT 8m20s.** Detach:
  `nohup env GATE_ROSTER_WHO=big-<sess> bash -c "$HOME/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1" &`
  then `sleep 300; grep -E "GATE SELF-CHECK|^  FAIL" /tmp/gate.log`. **COMMIT EVERYTHING FIRST** —
  the gate reads the working tree and a gate started before your last commit fails on DIRTY (`-54`
  lost a full run to it). **And re-stamp the charter immediately before it** (§4, item 1).
- ⚠ **`board.py` NEEDS FOUR FLAGS AND WARNS ABOUT NONE.** `./scripts/regen-board.sh`.
- ⚠ **HEREDOCS INSIDE `dx` DO NOT SURVIVE.** Write locally, `--put`, run. `git checkout <file>` is
  the free undo. **A nested heredoc inside a `--put` script is fine** — `-55` shipped Python
  heredocs inside `bash` scripts all afternoon; it is only the `dx '...'` argument that eats them.
- ⚠ **NON-ASCII IN A `--put` SCRIPT: WRITE THE LITERAL CHARACTER.** `\xc2\xb7` for `·` encodes to
  four bytes and every middot-keyed grep silently returns nothing.
- ⚠ **SMALL DIFFS DO NOT NEED A TARBALL.** `cat f | /tmp/dx --put /Users/jasoncbraatz/repos/...` —
  one call, sha256 verified. **`--get` with a leading `~` expands in the CLOUD and fails; use the
  full path** (`--put` accepts `~`, `--get` does not — `-55` confirmed both).
- ⚠ **`lessons.py` AUTO-COMMITS AND AUTO-PUSHES each leaf.** Look before you reach for a commit.
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started ·
  `5` crossed but mismatched.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
**SUITE:** 1068 collected, 1068 passed, zero skips — darwin ~66 s, cloud ~175 s. `pytest -m tripwire`
selects the tripwire class. `defensive_count.py` takes a positional path and **only a DELTA means
anything** — the tool says so itself. **Adding a manuscript to `docs/papers/` fails the suite until
you add it to `test_defensive_count.py::MANUSCRIPTS`, commit a `DEFENSIVE-BASELINE.json` beside it,
AND register it in `redproof_apparatus.PAPER`.** **Probe sweep:** ~3 min 30 s per probe at
`--jobs 2`; `nohup … &` and poll. **Budget for running the sweep twice.**
---
## 0 · THE TELL, NOW IN EIGHTY-ONE SHAPES
`-28` through `-54`'s tells all stand (ask the instrument-artefact question of numbers that look
GOOD, that SETTLE AN ARGUMENT, of a REGISTERED CONTROL THAT FAILS, OF THE DENOMINATOR; a guard must
scan assertions not quotations; a mutation that does not mutate reports your guard as weak;
pre-commit the FAVOURABLE outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT; a
correction that lives only in a handoff has not been made; a rule can be false on the day it is
written; an instrument pointed at two instances cannot tell a criterion from a convention; a guard
that cannot tell use from mention scores the mention; **moving a gate changes what *terminal* means
upstream of it and the consequence is never in the instruction**; a row that cannot be reached is
indistinguishable from one merely deferred; a criterion that passes because it does not apply is a
blank line wearing a tick). `-55` adds three:

- **A SYSTEM OF DOCUMENTS CAN HOLD A CONTRADICTION THAT NO PER-DOCUMENT REVIEW CAN FIND, BECAUSE
  EVERY REVIEWER GRADES A DOCUMENT AGAINST THAT DOCUMENT'S OWN CLAIMS.** Both papers passed their
  own review; the corpus was broken. **The detector is a shared-fact table that compares MODALITY,
  not truth value** — asserted / conditional / open / rejected — and the killing shape is one
  document carrying as PENDING what another reports as SETTLED. It is worse when the pending one is
  a **conditional whose antecedent has since become true**, because the document then *entails its
  own defect* and reads as careful while doing it. Paper IV's §9.2 was exactly that sentence, and it
  had been true-in-form and false-in-fact since the day `REG-003` returned.
- **A TOOL THAT ASSERTS MORE THAN IT MEASURED GROWS WORKAROUND PROSE IN THE ARTEFACTS IT SERVES —
  AND THAT PROSE IS THE FIND-IT SIGNAL.** `board.py` measured OPEN status and file order and printed
  a *schedule*; the cost was a handoff paragraph titled "FIRST, THE TRAP" whose entire job was to
  contradict one generated sentence. `charter-read.sh` claimed two files existed and readers
  concluded the *repo* was broken rather than the tool. **When you find a doc paragraph that exists
  to work around a tool's output, the bug is in the tool**, and the repair is almost always to
  report the measurement instead of issuing the conclusion.
- **A TEST WHOSE OUTCOME THE DESIGNER CAN PREDICT IS WORTH RUNNING AND IS NOT A TEST, AND MIXING
  THE TWO IS HOW A PASS REPORTS A NUMBER THAT MEANS NOTHING.** Six legs, five clear, reads like a
  grade — and is worthless if three of the six could not have lost. **Classify TEST vs AUDIT before
  the run, pre-register the AUDIT legs' remedies so they cannot be argued about afterwards, and
  score the two separately.** The corollary is the admission criterion: without one, a system-level
  pass silently degenerates into the component pass done N times, **and that run looks exactly like
  a successful one.**
---
## 7 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.
**Coffee status:** ☕ TWENTY-ONE SESSIONS. This one had one job — write down what it would mean for
the whole corpus to fail, *before* anyone knows — and the reading it took to do that job turned up a
paper that did not know its own chain was broken. **The design has not been run and it has already
paid for itself.** Fourteen lines open, one leg wants the next slot, and for the first time in
fifty-five sessions there is a written answer to a question this repository has been carrying since
August the eleventh. 🥎
