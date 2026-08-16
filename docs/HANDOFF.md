---
project: wealth-tensor
gh_sha: be0bdfc8dda7b67af02ac5062279820c669da47c
updated: 2026-08-16
session: wealthTensor-54
gate_passed: true
gate_version: "2.59"
definition_of_done: "Three preprints (II, III, IV) publicly posted — the corpus-level Definition of Done in ADR-001 as amended (was four; Paper I folded into IV). Per-paper clauses in ADR-001 govern each paper's 'ready to submit' terminal state, and nothing ships until the corpus is done."
---
# wealth-tensor — HANDOFF
`gh_sha` names the commit this file describes; **the only thing added after it is this file**,
so `--check` prints `ADVISORY: docs-only drift` and exits 0. Assert the exit code exactly
(`-39`); `| tail` masks it. That sentence is an **INVARIANT, not a description** — `-51` learned
that the hard way when a post-wrap ADR commit made it false while the gate stayed green, because
`--check` classifies by PATH and any docs-only drift is green. If a post-wrap commit lands,
repoint `gh_sha` and re-master this file.
`-54` landed `770f766` (Paper II's three prose gaps, alone, so that commit is green on its own)
and `be0bdfc` (the instrument and everything with it), then wrote this file alone after them.
`gh_sha` is the full SHA from `git rev-parse`, not an expanded abbreviation.
---
## ORIENT — read these first, in this order
1. **`docs/CHECKLIST.md`** — the generated board. **Regenerate with `./scripts/regen-board.sh`,
   never `board.py` by hand — see `-53`'s note in that file.** Never hand-tick. As of `-54`:
   **50 criteria, 41 met, ZERO lanes OPEN**, and the nine that remain are all `PENDING-HUMAN`
   by design. **The board prints no "next piece" line. Read §3 before you read that as done.**
2. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS** over this file, any
   result doc, and any plausible rewrite. **Stamp that you read it:
   `~/Scripts/charter-read.sh wealthTensor-<NN>` — POSITIONAL slug, no env var — and re-stamp
   AFTER you amend `done-criteria.tsv`, because `G-AL` compares the stamped SHA against the file
   as it stands at wrap. `-54` failed the gate on exactly that and it is not a bug: the finish
   line moved because `-54` moved it.**
3. **`scripts/gen_apparatus_rows.py`** — **NEW, and the session's real deliverable.** Read its
   docstring before you touch a single apparatus row. All forty `P1x`/`P3x`/`P5x` rows are
   emitted from one template; **hand-editing a sub-row in `done-criteria.tsv` is now a mistake
   the next regeneration silently reverts.**
4. **`scripts/redproof_apparatus.py`** + **`tests/test_apparatus_rows_are_falsifiable.py`** —
   34 mutations, 0 survivors, ~1 s, wired into the suite with a census.
5. **`docs/papers/paper-II-redistribution/paper-II.md`** — three gaps closed. §Abstract, §5's
   first limitation and §7 all moved. Read the abstract first: it now carries the loss.
6. **`docs/adr/ADR-001-paper-decomposition.md`** — `-54`'s addendum at the foot. The title and
   §Decision stay **deliberately frozen** at four papers as the decision-as-made; do not "fix"
   them. Every live clause says three.
7. `python3 scripts/handoff_gate.py --check` · `docs/papers/PREPRINT-CHECKLIST.md` §A/§B/§D ·
   `python3 scripts/mutation_control.py --list` (61 probes) ·
   `docs/preregistration/CONSTRAINT-INVENTORY-001.md` — **the constraint-inventory thread is
   still PAUSED**, see §3.
8. REG-013 + `RESULT-REG-013` §4.1 (read before quoting the headline) · REG-003 §§3.2/3.3/7 ·
   SCOUT-001 (WORKED) · REG-012 §§6–7 · RESULT-TERM-001's five-site ruling · REG-010 §1/§4 ·
   CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (READ THE HEADER NOTE FIRST).
---
## `-54` in one line
**PAPER II IS MEASURED — AND MEASURING A THIRD PAPER IS WHAT PROVED THE INSTRUMENT WAS
MEASURING TYPOGRAPHY.** Six of the twelve apparatus legs went red on Paper II for reasons that
had nothing to do with whether Paper II satisfies the criterion. `-53` found this defect once,
in `P1c`, and fixed it once. It was six. The rows are generated now, and every green has been
watched to go red.
---
## 1 · WHAT HAPPENED
**The at-bat was P3, and Paper II's gaps are CLOSED. `P3` itself stays `manual:` and unticked —
by the standing ruling, not by omission.**

### The artefact: three real gaps, none of them cosmetic
| | |
|---|---|
| **the abstract** | **265 w → 249 w** (bar 250; chars 1642 → 1513). Not a trim: PREPRINT-CHECKLIST §D says a prediction that was tested and lost goes in the body **and the abstract**, and §3.1's half-failure — *"a flow levy does not oppose the multiplicative term regardless of rate"*, false as stated — appeared only in the body. So the abstract had to lose ~55 words **and gain the loss**. It now names the nested frontiers, **stock 0.000 against flow 0.125**, placed where it leads into the surviving claim rather than where it gets the last word |
| **§1 promised what §7 did not deliver** | Contribution 5 said the claims are held by *"18 tests including two that exist specifically to make overclaiming fail loudly (§7)"* and §7 named **neither**. Both named now, with what each pins, plus the distinction between the 18 that hold this paper's claims and the repository's whole suite |
| **the first limitation did not run against comfort** | Papers III and IV both lead with the item that costs them most and III says so in terms (*"listed first on purpose"*). Paper II led with a scope statement already made twice elsewhere and buried the one that hurts — **ρ is exogenous here and in the world it is not, and endogenising it makes the flow base WEAKER than reported** — at number two. Promoted. No text cut; two items changed places |

**And a tell fired on the way in.** `-53`'s handoff **characterised** Paper II's abstract as
261 w / 1,646 c. Measured today, on a file `git diff` proves has not moved, it was
**265 w / 1,642 c**. A handoff's characterisation is not a measurement — and this is the second
consecutive session to prove it about its own predecessor.

### The instrument: six legs of twelve were keyed to Paper III's formatting
`-52` wrote the twelve legs against Paper III. `-53` hand-cloned them onto Paper IV and **all
twelve passed** — because III and IV happen to share a section numbering and a house style in
which every numbered item opens in bold. Paper II shares neither.

| leg | what it was actually measuring | Paper II |
|---|---|---|
| `P*e` | a **bold prefix** on every numbered contribution | II's five open in plain prose → scored **zero** against a bar of five |
| `P*f` | the literal string `## 8 · Abandoned approaches` | II's is **§4**. Body-ness is now MEASURED — a further numbered section must follow — instead of implied by Paper III's section number |
| `P*g` | `## 9 · Limitations`, **and** the phrase grepped against the whole file rather than item 1, **and** defeated by a markdown line wrap | all three legs repaired; the phrase is now required **in item 1**, whitespace-joined first |
| `P*h` | `## 1[01] · Data and code availability` | II's is **§7** |
| `P*i` | the **English word** "placeholder" | II §7 legitimately uses it as a common noun, in a sentence about why a bare one was refused |
| `P*c` | keywords plus mid-keyword wraps — **`-53`'s find** | II is the case that proves it: unjoined **9**, joined **8** |

**The repair is not six expressions.** `scripts/gen_apparatus_rows.py` emits all forty sub-rows
from ONE template with a per-paper parameter block, so a leg can differ between papers only
where the *paper* genuinely differs. Exactly three legitimately do — the abstract's loss marker,
the first limitation's phrase, the pre-registration clause — and they are the parameter block.
Idempotent; keeps the hand-maintained `P1`–`P10` corpus rows verbatim; **`P1x` and `P5x` stayed
green through the rewrite**, which is the check that the repair did not quietly weaken III and IV.

### The greens are now proven rather than asserted
`scripts/redproof_apparatus.py` applies to each row the smallest mutation that ought to break
it and requires the row's own check to go red. **34 mutations, 0 survivors, ~1 s**, manuscripts
restored byte-for-byte with a sha256 assertion in a `finally:`.
`tests/test_apparatus_rows_are_falsifiable.py` runs it in the suite and carries a **census**, so
a paper that acquires apparatus rows cannot skip red-proofing.

**The first run reported FIVE rows WEAK, and every one was the harness's own mis-aimed
mutation** — in a 200 kB manuscript the first `1. ` is nowhere near the contributions list.
That is the cheaper failure but **not** the harmless one: a mutation that does not mutate reports
a **sound** guard as weak, and invites the next session to "strengthen" a check that was already
right. Mutations are section-scoped now (`within()`).

### New rows
`P3a`–`P3n`. Two are worth knowing individually:
- **`P3k` does not wave the pre-registration clause past.** PREPRINT-CHECKLIST §D says in terms
  that *"Papers III and IV carry empirical predictions; I and II do not"*, so Paper II owes no
  registration — and the row asserts **that clause is still what the list says**, plus a
  tripwire: the day Paper II cites a registration it must cite a SHA with it. *A criterion that
  passes because it does not apply should say why, in a check, or it is a blank line wearing a
  tick.*
- **`P3n` is the first `P6` upgrade to land.** It **derives** Paper II's "18 tests" from
  `pytest --collect-only` and greps for whatever came back, so the claim cannot be satisfied by a
  constant that drifted. This is Jason's `-51` scoping proposal **(a)** applied to one claim.

| | |
|---|---|
| suite | **1063 passed** on darwin (~65 s), zero skips · was 1058; +5 are the falsifiability tests |
| board | **27/36 → 41/50** · P3a–P3l + P3n green, P3m human-deferred · **zero OPEN lanes** |
| defensive sentences | paper-II baseline **0/0**, unchanged by the prose edits; charter §2's non-increasing invariant holds estate-wide |
| lessons | **4 banked** (3 global, 1 project) · `use` on 2 leaves + `record-outcome … pass` both run |
| gate | **PASS ✅ at 2.59** after re-stamping the charter (see §4) |
---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-53`'s rulings stand verbatim**, including: REG-013's decision rule is
  SPENT and may not be re-chosen; H1 licenses OCCUPANCY, not fertility; `P5` and `P2` stay manual;
  §9's limitations are NINE items; ADR-001's title and §Decision are deliberately frozen; the
  abstract is a submission FIELD (`scripts/check_abstract_size.py`, never `wc -w`); no third
  disclosure instrument; phrase set frozen at 38; SOURCE-001 FINISHED; THE ARM IS δ; §4.8 IS NOT
  THE COINCIDENCE ARGUMENT, §4.7 IS; REG-009 CLOSED; DO NOT SPEND THE TIE-BREAK; DO NOT PROMOTE
  R_MIN; **R5 IS UNSPENT**; 55.71% IS Ψ's AND 63.16% IS THE BAND COUNT'S; T4's WIDTH IS 31.7%;
  **T2 MAY NOT BE RUN ON THIS DATA**; §4.7 IS PINNED AT `ba59370`; `wt107` IS NOT EDITED; CITE THE
  TEST, NOT THE `.bak`; **A CORRECTION IS NOT MADE UNTIL THE ARTEFACT IS EDITED.**
- **NEW · `P3` STAYS MANUAL.** Thirteen of Paper II's fourteen rows are green and that is **not**
  *ready to submit*. The session that closed the gaps does not get to score whether the paper is
  ready — same clause as `P2` and `P5`. P7's fresh eyes and P8 are the judges. **All three papers
  are now in exactly this state**, which is the corpus's real position: measured, unjudged.
- **NEW · APPARATUS SUB-ROWS ARE GENERATED, NOT WRITTEN.** Edit
  `scripts/gen_apparatus_rows.py` and re-run it; a hand-edit to a `P1x`/`P3x`/`P5x` row in
  `done-criteria.tsv` is reverted by the next regeneration **without a diff anyone will read**.
  The `P1`–`P10` corpus rows are the exception and are kept verbatim on purpose.
- **NEW · A ROW IS NOT DONE WHEN IT IS GREEN. IT IS DONE WHEN IT HAS BEEN SEEN RED.**
  Any new or changed `cmd:` row gets a mutation in `redproof_apparatus.MUTATIONS`, and the census
  test refuses a paper that has apparatus rows and no manuscript registered in the harness.
- **NEW · A `WEAK` VERDICT IS A CLAIM ABOUT THE HARNESS UNTIL THE MUTATION IS SHOWN TO LAND.**
  Five for five, first run. Check where the edit landed before you touch the guard.
---
## 3 · THE AT-BAT for `-55` — **`P7` ON PAPER IV, AND COME AT §4 FIRST**
**Every mechanically checkable criterion in the estate is green and the board names no next
piece. That is a state to be careful with, not to celebrate.** Nine lines remain, all
`PENDING-HUMAN`, which means *a human or a fresh-eyes pass judges them* — **not** that they are
done. **The DoD is three preprints POSTED. Nothing is posted.** A session that reads the board's
silence as *finished* will be the first this project has had to correct about its own completion.

**Take `P7` on Paper IV — a fresh-eyes review pass.** Reasons, in order:
- **The apparatus programme has run out of road, and that is the signal to stop.** `-52` measured
  Paper III, `-53` measured Paper IV, `-54` measured Paper II and generated the rows. There is no
  fourth paper. The banked lesson *"when an audit programme's last N findings are all about the
  instrument, measure the artefact"* was used this session and paid — three prose gaps in Paper II
  came out of one hour of reading. **Paper IV has never been read by anyone but the session that
  wrote it.**
- **Its §4 is the highest-value target in the estate.** The SMD-versus-scale resolution is the
  paper's load-bearing argument, it was drafted by one Claude in one pass, and ADR-001 predicted
  precisely that section is where the unforced error lives. Come at it first and hard.
- P7 needs **two consecutive zero-finding passes**, so the earliest possible finish is two
  sessions away no matter what. Starting it is the only thing that shortens the corpus.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The honest alternatives:
- **`P7` on Paper II instead** — it also has had no review pass, and it is the paper `-54` just
  edited in three places, which is exactly when a fresh reader is worth most. Weaker than IV only
  because IV's §4 carries more weight.
- **`P6`, the remaining two thirds.** `P3n` proved the shape; `P1n` and `P5n` are the same row
  repointed, and every other number-bearing claim in III and IV is a candidate. Mechanical,
  valuable, and it is the last corpus-level row with a writable check.
- **The end-to-end test, still unclaimed after six sessions** (ADR-001 addendum 6): *what would it
  mean for the three papers to fail as a system, as opposed to one of them failing?* No written
  answer exists anywhere in this repository, it is Jason's own methodological position, and
  **designing it after the results are known is not a severe test.** Biggest genuinely-unclaimed
  thing on the board.

**THE GUARD PROGRAMME REMAINS PAUSED** (Jason, 2026-08-15) and `-54` did not resume it. A new
guard is in-contour **only** when it names the paper claim it protects and that claim sits on an
open P-line. Jason's three scoping proposals from `-51` are **still UNRULED** — (a) audit the
CLASS not the constraint, with one linter over claims naming a count, a filename or a coverage
fact, each required to carry the command that regenerates it; (b) bound by value; (c) audit at
the BOUNDARY. **`-54` is the eighth consecutive session proposal (a) would have caught, and this
time it half-landed on its own**: `P3n` IS proposal (a), applied to one claim, and it took four
lines. That is the cheapest possible evidence that the proposal is right. **A ruling would be
worth more than another session of finding out.**
---
## 4 · TEED UP, IN ORDER
- **`G-AL` COMPARES THE STAMP TO THE FILE AS IT STANDS AT WRAP, SO AMENDING `done-criteria.tsv`
  INVALIDATES YOUR OWN STAMP.** `-54` hit this and it is correct behaviour badly explained: the
  message says *"the definition of done was amended after you read it"*, which reads like a
  sibling did it. **If you change the criteria, re-run `~/Scripts/charter-read.sh <slug>` before
  the gate.** Fix shape: name the amending session when the stamp and the amendment share one.
- **`charter-read.sh` PRINTS TWO PATHS THAT DO NOT EXIST** — `docs/DONE.md` and
  `docs/design/ARCHITECTURE.md`, neither of which is in wealth-tensor. Found by `-53`, confirmed
  still live by `-54`, **still not fixed** and now for a weaker reason than `-53`'s: the sibling
  contention has aged out (`cloud-oaujFobu`'s claims read STALE at 7h+), so the next session that
  wants a small win can take `darwin-mac-ops` and do it. Fix: print each pointer only if the file
  exists, or read both from `project-charters.tsv` like the criteria path.
- **`G-AL`'s REMEDY LINE DOES NOT WORK AS PRINTED** — *"Read it: ~/Scripts/charter-read.sh"* with
  no slug exits 2. The gate knows the slug; it prints it in the same sentence. One line.
- **`G-T` calls a STALE claim LIVE and tells the owner not to commit.** `-52`'s find, unfixed,
  warning-level. Same family as `G-AL`: a check that cannot identify who is asking.
- **`~/.local/state/claude-session/current` is a single global file** and Jason runs 2–3 sessions.
  `G-AL` no longer trusts it; **anything else reading it has the same bug.** One grep would find
  them.
- **`P1n` and `P5n`** — `P3n` repointed at Papers III and IV. The generator already has the shape;
  it needs each paper's regenerating command. Half an hour, and it moves `P6`.
- **The use/mention guard, generalised.** `P*i` now forbids the marker rather than the word, and
  the general repair — *a guard that would fire on a document DISCUSSING the thing it forbids is
  matching vocabulary, not structure* — is banked but applied in exactly one place. Other guards
  in this repo grep for vocabulary.
- **C26 limb B** — carded `1217525563299334`. §2's twelve ratios with no counts.
- **RESULT-REG-003 §2's "Every cut lands in R1"** — carded `1217518687033967`. Repair shape is a
  dated addendum (`-37` precedent).
- **Cell (b), ranked in §3.2 — THREE entries left**, measured, **paused behind the papers.** The
  forbidden-claim family (C16/C20/C23/C25/C30, probes R5a–R5e) · C45's two assertions · the
  reportable-at-all presence guards.
- **No probe has ever mutated `src/` except G7/G8.** Real, small, still unclaimed — and
  `redproof_apparatus.py` is now a worked example of the shape.
- **C37's tripwire** — REG-009 §12's "never by narration"; §3.3 names the adjacent check.
- **§7's ledger dilutes its own two load-bearing rows** — Jason's call, TRIPWIRED not carded.
- **Dossier era, re-served by nobody:** REVIEW-004 C6 (ASC 410) and C10 (IAS 36's reversal
  asymmetry). *That C10 is REVIEW-004's, not the inventory's; the collision has bitten three times.*
- **REG-013 re-run worth doing:** the biophysical audience was capped at 4 000 of 7 801, which
  **suppresses** its overlaps and is the one bias favouring H1. Clean, bounded, pre-specified.
- Infra siblings, carded: Caddy ordering `1217488447555628` · capability path in cleartext
  `1217488117177482` · AAR A2's four post-* hooks · card-lint `1217483699706758` · gate
  `1217465036940491`.
---
## 5 · DO NOT
- **Everything `-31`→`-53` forbade still stands verbatim** — R5, the two sensitivities,
  `selected_lives`, §4.4's 0.3000, T4's 31.7%, the δ arm, TERM-001/002, §9's list well-formedness,
  `wt107` IS NOT EDITED, §4.7 IS PINNED AT `ba59370`, DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD,
  DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION, DO NOT GRADE A CONSTRAINT FROM THE
  `machine` COLUMN, DO NOT WIDEN C07's GUARD, DO NOT WRITE AN OVER-BREADTH SELF-TEST WITH AN
  ABSENCE PREDICATE, DO NOT SLICE THE SWEEP LOG BY SLUG, **DO NOT TYPE A FULL SHA YOU HAVE NOT
  RESOLVED**, DO NOT LEAVE A FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT CORRECTS, DO NOT
  OBEY A DO-NOT THAT NAMES A MACHINE WITHOUT RUNNING THE MACHINE, DO NOT MEASURE A TEXT LENGTH
  WITH `wc -w`, DO NOT ADD A REQUIRED KEY TO A GATE WITHOUT REBUILDING ITS FIXTURES, DO NOT LET A
  `manual:` ROW BE SCORED BY WHOEVER DID THE WORK, DO NOT RUN `board.py` BY HAND, DO NOT READ A
  CO-CITATION NUMBER WITHOUT ITS TWO CONTROLS, DO NOT ROUTE BIBLIOMETRIC API WORK THROUGH THE
  CLOUD CONTAINER, DO NOT PUT A COLON OR COMMA INSIDE AN OPENALEX `filter=` VALUE.
- **NEW · DO NOT HAND-EDIT A `P1x`/`P3x`/`P5x` ROW.** Edit the generator. A hand-edit is reverted
  by the next `gen_apparatus_rows.py` run and leaves no diff anyone will read.
- **NEW · DO NOT TRUST A GREEN CLONE.** A check that passes on a second instance is not evidence
  the check is sound — it is evidence the two instances look alike. Six legs proved this in one
  session.
- **NEW · DO NOT "STRENGTHEN" A CHECK A MUTATION HARNESS CALLED WEAK UNTIL YOU HAVE CONFIRMED THE
  MUTATION LANDED IN THE SECTION THE CHECK READS.** Five false WEAKs, first run.
- **NEW · DO NOT WRITE A FORBIDDEN-TOKEN GUARD THAT WOULD FIRE ON A DOCUMENT DISCUSSING THE THING
  IT FORBIDS.** That guard is matching vocabulary, not structure. Paper II §7 is the worked case.
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe run with `while pgrep`. **Do not edit shared infra a sibling is mid-edit on** —
  check for a `.bak` dated today before you reach for `~/Scripts/`.
---
## 6 · TRANSPORT — darlish, zero-bridge (unchanged, worked first try)
Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. First try, no fallback, `-06` through `-54`. **Never restart the
app to fix darlish — it is not on the bridge.** `darlish-check` is not in the cloud kit; do not
chase its 127. `roster leave` ONCE at wrap.
- ⚠ **SET `GATE_ROSTER_WHO` INLINE** — `dx` spawns a fresh shell per call and carries no
  environment. **`export` DOES work inside a script you `--put` and run with `bash /tmp/x.sh`, and
  that is the right default for anything with more than one step.** `-54` ran its commit batch and
  its lesson batch that way and neither needed a second round trip.
- ⚠ **`roster claim` and `roster join` BOTH need `--who`** even when `GATE_ROSTER_WHO` is set;
  `claim` takes `--resource`, not `--repo`. `record-outcome <tag> pass` is two positionals.
- ⚠ **`gate-selfcheck.sh` TAKES ~5–8 MINUTES AND A FOREGROUND `Bash` CALL DIES AT 8m20s.** `-54`
  lost one round trip to this. Run it detached and poll:
  `nohup env GATE_ROSTER_WHO=big-<sess> bash -c "$HOME/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1" &`
  then `sleep 240; tail /tmp/gate.log`. **And re-stamp the charter first if you amended
  `done-criteria.tsv`** — see §4.
- ⚠ **`board.py` NEEDS FOUR FLAGS AND WARNS ABOUT NONE OF THEM.** `./scripts/regen-board.sh`.
- ⚠ **HEREDOCS INSIDE `dx` DO NOT SURVIVE.** `-51` warned, `-52`, `-53` and `-54` each lost a
  round trip. Write the script to a local file, `--put` it, run `python3 /tmp/x.py`. Four sessions
  have now paid for this; take it the first time. `git checkout <file>` is the free undo.
- ⚠ **NON-ASCII IN A `--put` SCRIPT: WRITE THE LITERAL CHARACTER.** `-54` lost a round trip
  writing `\xc2\xb7` for `·` in a Python string — it encodes to four bytes, every middot-keyed
  grep silently returned nothing, and the probe reported eleven legs red that were fine. **A probe
  that reports everything broken is usually broken itself.**
- ⚠ **SMALL DIFFS DO NOT NEED A TARBALL.** `cat f | /tmp/dx --put /Users/jasoncbraatz/repos/...`
  per file: one call, sha256 verified. `-54` pushed six files that way. The tarball stanza is for
  coming DOWN only. `--get` with a leading `~` expands in the CLOUD and fails; use the full path.
- ⚠ **`lessons.py` AUTO-COMMITS AND AUTO-PUSHES each leaf.** Look before you reach for a commit.
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started ·
  `5` crossed but mismatched.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
**SUITE:** 1063 collected, 1063 passed, zero skips — darwin ~65 s, cloud ~175 s.
`pytest -m tripwire` selects the tripwire class. `scripts/defensive_count.py` takes a positional
path. **Adding a manuscript to `docs/papers/` fails the suite until you add it to
`tests/test_defensive_count.py::MANUSCRIPTS` AND commit a `DEFENSIVE-BASELINE.json` beside it** —
and, as of `-54`, until you register it in `redproof_apparatus.PAPER` too. **Probe sweep:**
~3 min 30 s per probe at `--jobs 2`; `nohup … &` and poll. **Budget for running the sweep twice.**
---
## 0 · THE TELL, NOW IN SEVENTY-FIVE SHAPES
`-28` through `-53`'s tells all stand (ask the instrument-artefact question of numbers that look
GOOD, that SETTLE AN ARGUMENT, of a REGISTERED CONTROL THAT FAILS, OF THE DENOMINATOR; a guard
must scan assertions not quotations; a mutation that does not mutate reports your guard as weak;
pre-commit the FAVOURABLE outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT;
a correction that lives only in a handoff has not been made; the visible reds are the cheap half;
a rule can be false on the day it is written; a count is not a measurement until it agrees across
machines; a commissioned test that was never run is the most durable debt; a favourable result is
when the controls matter most; a count whose answer moves when the file is re-wrapped is measuring
the formatting; a fact can be recorded and still be absent at the point of use). `-54` adds four:
- **AN INSTRUMENT POINTED AT ONLY TWO INSTANCES CANNOT TELL A CRITERION FROM A CONVENTION, AND
  THE THIRD INSTANCE IS THE MEASUREMENT.** Twelve checks were written against one manuscript and
  cloned onto a second, where all twelve passed — because the two papers shared a section
  numbering and a bold-prefix house style. On a third, six went red for reasons having nothing to
  do with the criterion. **The second instance is not a test of the instrument; it is a second
  sample of the same convention**, and a green clone is the weakest evidence available that a
  check measures what it says. `-53` found one of these six and fixed it in place, which was
  right and was also how the other five stayed hidden: **fixing an instance of a defect is what
  stops you looking for the class.**
- **A MUTATION THAT LANDS OUTSIDE THE REGION THE CHECK READS REPORTS A SOUND GUARD AS WEAK, AND
  THAT IS THE MORE DANGEROUS DIRECTION.** Five for five on the first run. A false WEAK does not
  merely waste a session — **it invites the next one to strengthen a check that was already
  right**, which is how a precise guard becomes a broad one and how `DO NOT WIDEN` lists get
  written after the fact. Treat WEAK as a claim about the harness until the edit is shown to land.
- **A GUARD THAT CANNOT TELL USE FROM MENTION SCORES THE MENTION.** A grep forbidding
  `placeholder` fired on the one paragraph in the corpus that explains why a bare placeholder was
  refused. **The document was right and the guard called it wrong.** The general test: *if a
  document DISCUSSING the thing you forbid would trip the guard, the guard is matching vocabulary
  rather than structure* — and the repair is convention (caps, delimiters), not weakening.
- **A CRITERION THAT PASSES BECAUSE IT DOES NOT APPLY IS A BLANK LINE WEARING A TICK.** Paper II
  owes no pre-registration; PREPRINT-CHECKLIST §D says so in terms. The cheap move is to drop the
  row and the honest one is to make the row assert **the clause**, plus a tripwire for the day the
  premise moves. **Inapplicability is a fact about the world and facts about the world can change
  without anyone telling the board.**
---
## 7 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.
**Coffee status:** ☕ TWENTY SESSIONS, and for the first time all three papers have been measured
against the same bar — which is exactly when the bar turned out to be measuring six things that
were never in it. Ten sessions audited the apparatus, `-52` opened a manuscript and found an
abstract 2.85× the ceiling, `-53` ran the test the corpus had been citing since day one without
ever running it, and `-54` pointed the same twelve checks at a third paper and watched half of
them fail at typography. **The corpus is measured. Nobody has read Paper IV but the session that
wrote it.** That is the next at-bat, and it is a reading job, not a tooling one. 🥎
