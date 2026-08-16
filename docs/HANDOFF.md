---
project: wealth-tensor
gh_sha: 74cba6795466dc92532d66549eb1c1bd6b70b46e
updated: 2026-08-16
session: wealthTensor-53
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
`-53` landed `fff7063` (the registration, alone), `5efe626` (the paper and everything with it) and
`74cba67` (a correction to a file `5efe626` shipped), then wrote this file alone after them.
`gh_sha` is the full SHA from `git rev-parse`, not an expanded abbreviation.
---
## ORIENT — read these first, in this order
1. **`docs/CHECKLIST.md`** — the generated board (Tier 2). **Regenerate it with
   `./scripts/regen-board.sh`, which is new and exists for a reason — see §1.** Never hand-tick.
   As of `-53`: **27 of 36 lines met, and ZERO lanes OPEN.** Every mechanically checkable
   criterion in the estate is green; the nine that remain are **all `PENDING-HUMAN` by design**.
   The board prints no "next piece" line any more, and that is not a bug — read §3 before you
   read that silence as *done*.
2. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS** over this file, any
   result doc, and any plausible rewrite. §2's repair ladder (STEELMAN / REPLACE / CUT / TEE UP,
   ABSORB illegal) and §3.4 (order by contribution, not contrition) governed every prose decision
   in Paper IV. **Stamp that you read it: `~/Scripts/charter-read.sh wealthTensor-<NN>` — it takes
   a POSITIONAL slug, not an env var, and `G-AL` fails the gate at wrap without the stamp** (`-53`
   burned two calls on this; see §4).
3. **`docs/papers/paper-IV-composition/paper-IV.md`** — **NEW, and the session's deliverable.**
   ~6.3k words. Read §4 first: it is the one section ADR-001 predicted would be got wrong.
4. **`docs/adr/ADR-001-paper-decomposition.md`** — the sequencing decision, plus `-53`'s addendum
   at the foot recording that Paper IV exists and that the whitespace is a measurement. The title
   and §Decision are **deliberately frozen** at four papers as the decision-as-made; do not "fix"
   them. Every live clause says three.
5. **`docs/preregistration/REG-013-citation-graph-whitespace.md`** then **`RESULT-REG-013.md`** —
   the new registration and its result. Read §4.1 of the RESULT before quoting the headline.
6. `python3 scripts/handoff_gate.py --check` · `docs/papers/PREPRINT-CHECKLIST.md` §A/§B/§D ·
   `python3 scripts/mutation_control.py --list` (61 probes) ·
   `docs/preregistration/CONSTRAINT-INVENTORY-001.md` — **the constraint-inventory thread is still
   PAUSED**, see §3.
7. REG-003 §§3.2/3.3/7 · SCOUT-001 (WORKED) · REG-012 §§6–7 · RESULT-TERM-001's five-site ruling ·
   REG-010 §1/§4 · CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (READ THE HEADER NOTE FIRST).
---
## `-53` in one line
**PAPER IV IS WRITTEN, AND THE WHITESPACE IT OPENS ON IS NO LONGER SOMETHING WE ASSERT.**
`ADR-001` §Paper IV has commissioned the citation-graph whitespace *"as evidence rather than
anecdote"* since 2026-08-05, citing `WT-006`, which proposed the instrument and **was never run**.
Every whitespace claim in this repository — the motivation for the entire corpus — rested on
*"I looked and found nothing,"* which is the exact sentence WT-006 was written to replace. It took
one registration, one script and about forty minutes.
It came back **favourable**, which is the outcome that needed the controls most: a ceiling of
0.477, a floor of exactly 0.000, and three target pairs at 0.020 / 0.011 / 0.005. **Six works in
the world cite both a stock-flow-consistent seed and a kinetic-exchange seed.**
---
## 1 · WHAT HAPPENED
**The at-bat was P4, and P4 is CLOSED.** `docs/papers/paper-IV-composition/paper-IV.md` exists as
a full draft with its own measured apparatus (`P5a`–`P5m`).
| | |
|---|---|
| **the paper** | 6,284 words · abstract 224 w / 1,506 c (bar: 250 / 1,920) · 8 keywords · JEL B41 D50 E01 Q57 C63 · 5 numbered contributions · 7 numbered limitations · Abandoned Approaches as **§8, a body section** · defensive-sentence count **zero** |
| **the tension ADR-001 named** | answered in **§4**, by a distinction and not a hedge: **SMD is a theorem about behavioural MAPS; the atomic unit is a STATE.** Aggregation preserves the extensive state and destroys the behavioural map. SMD is not an objection to composition across scales — it is the same statement's other half, proved by the mainstream fifty years ago |
| **Paper I's estate, spent** | the surviving identity (*the crossing height IS the volume*) is **§5**; its two dead framings, the killed re-scope, the noise-dominated headline, the mis-specified control and the verdictless `REG-001` are **§8**, the corpus's largest Abandoned Approaches entry |
| **REG-013** | registered **alone** in `fff7063`, instrument in `5efe626`. 25/25 seeds resolved |
**REG-013, and the design is the result.** A low co-citation rate between two specialties is the
normal condition of any two specialties, so three small numbers would have said nothing. Both ends
of the scale were measured in the same run:
- **CEILING · 0.477** — each literature split in half by seed-index parity and measured against
  itself. It needs no further judgement from the analyst and therefore **cannot be tuned**; the
  registration voids the whole run below 0.20. It fired.
- **FLOOR · exactly 0.0000** — each literature against six CRISPR papers. **Not one work** in any
  of the three economics audiences also cites a CRISPR seed.
- **TARGETS** — biophysical × stock-flow 0.0202 (23 works), biophysical × kinetic 0.0108 (15),
  stock-flow × kinetic 0.0053 (**6**). Against split-half intersections of 134, 155 and 380
  *within* the same literatures. All three below the registered 0.10 bar. **H1 survives.**
- **AND THE RESULT REPORTS ITS OWN SOFT SPOT.** Biophysical economics is on this instrument a
  loose federation — its own split-half is **0.168**, below the 0.20 that would have voided the
  run had it been the pooled figure — so the pooled ceiling scores the biophysical pairs
  generously. Under a stricter per-cluster ceiling, **biophysical × stock-flow reads UNDECIDED**
  (z = 0.120 against a 0.10 bar). **The registered rule was not re-chosen**; the sensitivity is in
  `RESULT-REG-013` §4.1 and in the paper's §6, and it is in the ABSTRACT, because it is the
  nearest thing this paper has to a loss.
**BUG SPRAY, three.**
1. **`P1c` COUNTED KEYWORDS PLUS LINE WRAPS.** `grep -A1 '**Keywords:**' | tr '·' '\n' | grep -c`
   splits on the separator only, so a markdown wrap falling **mid-keyword** survives as a newline
   and counts that keyword twice. Measured on all three manuscripts before saying so: **Paper II
   carries 8 and the expression reads 9.** Paper III passing was formatting luck — its wrap lands
   on a separator. The criterion was evaluating *"6–8 keywords plus mid-keyword wraps"*, and which
   value you get depends on where an editor's line filling lands. Both rows now join the lines
   first. **This was found by the check going red on Paper IV, which is the check working.**
2. **`board.py`'s OBVIOUS INVOCATION SILENTLY DEGRADES THE BOARD.** One of its four flags is
   required. Run it the obvious way and the title becomes `# project — SESSION CHECKLIST` and the
   entire *"## The destination (ADR-001, restated once)"* preamble is **deleted** — while every
   per-row status stays correct, so **nothing goes red.** `-53` did exactly this in its first ten
   minutes. Fixed by `scripts/regen-board.sh`. **And the second commit is the more interesting
   half:** the flags were *not* unrecorded — `project-charters.tsv` carries the full invocation and
   `charter-read.sh` runs it correctly every session. The fact existed on the machine and was still
   absent **at the point of use**, because it was filed under the TOOL instead of under the
   ARTEFACT. That is the harder shape to notice: a search of the right file finds it, and a session
   working inside this repo never opens that file.
3. **ADR-001 ASSERTED TWO THINGS THAT WERE FALSE.** §Consequences' *"All are absent today"* about
   the per-paper apparatus (named stale by `-52`'s measurement and by a banked lesson, **still
   asserted as live law**) and its *"One live placeholder to clear"* (cleared long ago, and now
   guarded by rows `P1i`/`P5i`). Both struck in place, old text kept, each pointed at the row that
   measures it.
| | |
|---|---|
| suite | **1058 passed** on darwin (~64 s), zero skips · was 1055; +3 are Paper IV's parametrised defensive-count rows |
| board | **14/23 → 27/36** · P4 CLOSED · P5a–P5l green, P5m human-deferred · **zero OPEN lanes** |
| defensive sentences | paper-IV baseline **0** · charter §2's non-increasing invariant holds estate-wide |
| lessons | **4 banked** (3 global, 1 project) + **1 curated** · `use` + `record-outcome` both run |
| gate | **PASS ✅ at 2.59**, one pre-existing warning (`G-T#45`, the n8n box, not this project's) |
**DONE, and `-52` explicitly could not say this:** `lessons.py search` ran at student-in, one leaf
was genuinely used (`2026-08-05-measure-document-before-opining-its-structure` — it is why the
keyword over-count was *measured on three manuscripts* before it was asserted), and both
`lessons.py use` and `record-outcome … pass` are recorded. The corroboration ledger moved.
---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-52`'s rulings stand verbatim**, including `-52`'s four new ones:
  §9's limitations are NINE items and nothing mandates a count; ADR-001's title and §Decision are
  deliberately frozen; the abstract is a submission FIELD (count it with
  `scripts/check_abstract_size.py`, never `wc -w`); the measurement lives in `done-criteria.tsv`,
  not in this file. And the long tail: no third disclosure instrument; phrase set frozen at 38;
  SOURCE-001 FINISHED; THE ARM IS δ; §4.8 IS NOT THE COINCIDENCE ARGUMENT, §4.7 IS; REG-009 CLOSED;
  DO NOT SPEND THE TIE-BREAK; DO NOT PROMOTE R_MIN; **R5 IS UNSPENT**; 55.71% IS Ψ's AND 63.16% IS
  THE BAND COUNT'S; T4's WIDTH IS 31.7%; **T2 MAY NOT BE RUN ON THIS DATA**; §4.7 IS PINNED AT
  `ba59370`; `wt107` IS NOT EDITED; CITE THE TEST, NOT THE `.bak`; **A CORRECTION IS NOT MADE UNTIL
  THE ARTEFACT IS EDITED.**
- **NEW · REG-013's DECISION RULE IS SPENT AND MAY NOT BE RE-CHOSEN.** The pooled ceiling, the
  0.10/0.25 thresholds, the seed lists, `N_MAX` and the VOID rule are fixed by the registration
  (§6) and were fixed before the numbers existed. The per-cluster sensitivity is **reported, not
  adopted**. If the instrument is genuinely mis-specified the repair is a SECOND registration
  saying so — the `REG-001` precedent — never an edit to REG-013.
- **NEW · H1 SURVIVED, AND WHAT IT LICENSES IS OCCUPANCY, NOT FERTILITY.** Pre-committed in the
  registration while it was still cheap to say. Paper IV may cite REG-013 for *the three
  literatures do not read each other* and for nothing else. That the intersection is worth
  occupying is what §§3–5 have to earn on their own, and no re-run of the instrument can help.
- **NEW · `P5` STAYS MANUAL, AND SO DOES `P2`.** Eleven of Paper IV's twelve apparatus rows are
  green and that is **not** *ready to submit*. The session that drafted the paper does not get to
  score whether it is ready; P7's fresh eyes and P8 are the judges. **Do not upgrade a `manual:`
  row to a `cmd:` row because its sub-rows went green** — that is the failure the `manual:`
  designation exists to prevent.
- **NEW · `charter-read.sh` TAKES A POSITIONAL SLUG.** `charter-read.sh wealthTensor-53`. Not
  `CHARTER_SLUG=`, not `GATE_ROSTER_WHO=`. Both env forms print *"no session tag — open one
  first"* and exit 2, and `G-AL` then fails your gate at wrap. See §4.
---
## 3 · THE AT-BAT for `-54` — **PAPER II (`P3`), AND READ THIS BEFORE THE BOARD'S SILENCE**
**The board no longer names a next piece, because every OPEN lane is closed.** That is a state to
be careful with, not to celebrate: the nine remaining lines are `PENDING-HUMAN`, which means *a
human or a fresh-eyes pass judges them*, **not** that they are done. A session that reads the
absence of a "next piece" line as *the corpus is finished* will be the first one this project has
had to correct about its own completion. **The DoD is three preprints POSTED. Nothing is posted.**
**Take `P3` — Paper II re-measured against the same two lists.** Reasons, in order:
- It is the **cheapest full close** left. Paper II is 3,864 words, its apparatus is already close
  (abstract 261 w / 1,646 c — over the 250-word bar by eleven words and comfortably inside arXiv's
  character ceiling), and **the rows are now written twice over.** Clone `P1a`–`P1m` a second time
  as `P3a`–`P3m` against `paper-II.md`; only the path moves. That is the third use of the same
  twelve checks and the whole argument for having built them as rows.
- **`P3c` will fail on Paper II and you already know why** — its keywords line reads 9 for 8, the
  defect `-53` fixed in `P1c`/`P5c`. The fixed expression is in `done-criteria.tsv`; copy that one,
  not the old shape from a `.bak`.
- It closes the **last paper nobody has measured**, which is what makes P6/P7/P8 startable.
**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The honest alternatives:
- **`P7` on Paper IV — a fresh-eyes review pass.** Legitimate and arguably better: IV was drafted
  in one session by the session that also chose its criteria, it has had **zero** review passes,
  and P7 needs two consecutive zero-finding ones. **Its §4 is the highest-value target in the
  estate right now** — the SMD-versus-scale resolution is the paper's load-bearing argument, it was
  written by one Claude in one pass, and ADR-001 predicted precisely this section is where the
  unforced error lives. If you take this, come at §4 first and hard.
- **`P6`** — enumerate the per-paper regeneration scripts and upgrade the row to `cmd:`. Mechanical,
  valuable, and it is the last corpus-level row with a writable check.
- **The end-to-end test, still unclaimed after five sessions** (ADR-001 addendum 6): *what would it
  mean for the three papers to fail as a system, as opposed to one of them failing?* It has no
  written answer anywhere in this repository, it is Jason's own methodological position, and
  **designing it after the result is known is not a severe test** — so it should be designed
  *before* IV converges, which is now. This is the biggest genuinely-unclaimed thing on the board.
**THE GUARD PROGRAMME REMAINS PAUSED** (Jason, 2026-08-15) and `-53` did not resume it. A new guard
is in-contour **only** when it names the paper claim it protects and that claim sits on an open
P-line. Jason's three scoping proposals from `-51` are **still UNRULED** — (a) audit the CLASS not
the constraint, with one linter over claims naming a count, a filename or a coverage fact, each
required to carry the command that regenerates it; (b) bound by value; (c) audit at the BOUNDARY.
**`-53` is the seventh consecutive session proposal (a) would have caught** — `P1c` was a claim
about a count that named no regenerating command, and it was wrong.
---
## 4 · TEED UP, IN ORDER
- **`charter-read.sh` PRINTS TWO PATHS THAT DO NOT EXIST**, for this project and presumably for
  every project whose layout differs from braatzio-plan's. It stamps successfully and then reports
  `full board: …/docs/DONE.md` and `the charter it derives from: …/docs/design/ARCHITECTURE.md` —
  **neither file exists in wealth-tensor.** The stamp is sound (it hashes `done-criteria.tsv`,
  which does exist); the two pointers are hardcoded defaults. Net effect: a check whose whole
  purpose is *make sure the session read the right document* teaches two wrong paths to it.
  **Found by `-53`, NOT fixed, deliberately:** `~/Scripts/gate-selfcheck.sh` carries a `.bak`
  dated today and named `ctxband01-galstale-20260816` — **a sibling session is mid-edit on G-AL
  right now**, and darwin-mac-ops is claimed (STALE, `cloud-oaujFobu`). Editing shared infra
  underneath a live sibling is the one thing the roster exists to stop. Fix shape: print each
  pointer only if the file exists, or read both from `project-charters.tsv` like the criteria path.
- **`G-AL`'s REMEDY LINE DOES NOT WORK AS PRINTED.** It says *"Read it (it takes ten seconds):
  ~/Scripts/charter-read.sh"* — with no slug. Run exactly that and you get *"no session tag — open
  one first"* and exit 2. The gate knows the slug (it prints `session 'wealthTensor-53'` in the
  same sentence) and should interpolate it. One line, same file, same sibling-contention caveat.
- **`G-T` calls a STALE claim LIVE and tells the owner not to commit.** Found by `-52`, still
  unfixed, still warning-level. Same family as `G-AL`: a check that cannot identify who is asking.
- **`~/.local/state/claude-session/current` is a single global file** and Jason runs 2–3 sessions.
  `G-AL` no longer trusts it; **anything else reading it has the same bug.** One grep would find
  them. `-53` hit the downstream face of this — `charter-read.sh` with no argument reads that file,
  finds nothing, and refuses.
- **C26 limb B** — carded `1217525563299334`. §2's twelve ratios with no counts; §2.2's four
  discovered couplings (0.00×, 3.27×, 7.70×, 6.33×) are prose ratios with p-values and no counts.
- **RESULT-REG-003 §2's "Every cut lands in R1"** — carded `1217518687033967`. Two readings; under
  one, 0.327 < 0.33 is R2. Repair shape is a dated addendum (`-37` precedent).
- **Cell (b), ranked in §3.2 — THREE entries left**, measured, **paused behind the paper.**
  The forbidden-claim family (C16/C20/C23/C25/C30, probes R5a–R5e) · C45's two assertions · the
  reportable-at-all presence guards. Paused is not abandoned; if you take it, say why it beats P3.
- **No probe has ever mutated `src/` except G7/G8.** Real, small, still unclaimed.
- **C37's tripwire** — REG-009 §12's "never by narration"; §3.3 names the adjacent check.
- **§7's ledger dilutes its own two load-bearing rows** — Jason's call, TRIPWIRED not carded.
- **Dossier era, re-served by nobody:** REVIEW-004 C6 (ASC 410) and C10 (IAS 36's reversal
  asymmetry). *That C10 is REVIEW-004's, not the inventory's; the collision has bitten three times.*
- **REG-013 re-runs, and one is worth doing.** The biophysical audience was capped at 4 000 of
  7 801, which **suppresses** both its overlaps and is the one bias in the run that favours H1.
  Uncapping it is a clean, bounded, pre-specified follow-up. Note the instrument hits a live API,
  so counts drift upward with re-runs; the *shape* is the claim.
- Infra siblings, carded: Caddy ordering `1217488447555628` · capability path in cleartext
  `1217488117177482` · AAR A2's four post-* hooks · card-lint `1217483699706758` · gate
  `1217465036940491`.
---
## 5 · DO NOT
- **Everything `-31`→`-52` forbade still stands verbatim** — R5, the two sensitivities,
  `selected_lives`, §4.4's 0.3000, T4's 31.7%, the δ arm, TERM-001/002, §9's list well-formedness,
  `wt107` IS NOT EDITED, §4.7 IS PINNED AT `ba59370`, DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD,
  DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION, DO NOT GRADE A CONSTRAINT FROM THE
  `machine` COLUMN, DO NOT WIDEN C07's GUARD, DO NOT WRITE AN OVER-BREADTH SELF-TEST WITH AN ABSENCE
  PREDICATE, DO NOT SLICE THE SWEEP LOG BY SLUG, **DO NOT TYPE A FULL SHA YOU HAVE NOT RESOLVED**,
  DO NOT LEAVE A FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT CORRECTS, DO NOT OBEY A DO-NOT
  THAT NAMES A MACHINE WITHOUT RUNNING THE MACHINE, DO NOT MEASURE A TEXT LENGTH WITH `wc -w`, DO
  NOT ADD A REQUIRED KEY TO A GATE WITHOUT REBUILDING ITS FIXTURES, DO NOT LET A `manual:` ROW BE
  SCORED BY WHOEVER DID THE WORK.
- **NEW · DO NOT RUN `board.py` BY HAND. RUN `./scripts/regen-board.sh`.** The hand invocation
  loses the project name and the destination preamble and **goes green doing it.**
- **NEW · DO NOT READ A CO-CITATION NUMBER WITHOUT ITS TWO CONTROLS.** Near-zero overlap is the
  normal condition of any two specialties. The floor and the split-half ceiling are not
  robustness checks bolted onto REG-013; they are the measurement, and the three target numbers
  mean nothing without them printed beside them.
- **NEW · DO NOT ROUTE BIBLIOMETRIC API WORK THROUGH THE CLOUD CONTAINER.** `api.openalex.org`
  returned HTTP 429 on the container's **first** request (shared egress IP) and served darwin
  unauthenticated without complaint. This is the opposite of the standing bulk-work routing, and
  it cost `-53` a false start.
- **NEW · DO NOT PUT A COLON OR COMMA INSIDE AN OPENALEX `filter=` VALUE.** They are parsed
  positionally; a subtitle after a colon is an HTTP 400, and it reads like a transport failure.
  `scripts/reg013_citation_whitespace.py::_filter_safe` is the two-line answer.
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe run with `while pgrep`. **Do not edit shared infra a sibling is mid-edit on** —
  check for a `.bak` dated today before you reach for `~/Scripts/`.
---
## 6 · TRANSPORT — darlish, zero-bridge (unchanged, worked first try)
Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. First try, no fallback, `-06` through `-53`. **Never restart the app
to fix darlish — it is not on the bridge.** `darlish-check` is not in the cloud kit; do not chase
its 127. `roster leave` ONCE at wrap.
- ⚠ **SET `GATE_ROSTER_WHO` INLINE.** `dx` spawns a fresh shell per call and carries no
  environment. Inline on the commit and every `lessons.py` call. `export` DOES work inside a
  script you `--put` and run with `bash /tmp/x.sh` — one shell. **`-53` used that shape for the
  commit and the lesson batch and it is the right default.**
- ⚠ **`roster claim` and `roster join` BOTH need `--who`** even when `GATE_ROSTER_WHO` is set;
  `claim` takes `--resource`, not `--repo`. `record-outcome <tag> pass` is two positionals.
- ⚠ **`gate-selfcheck.sh` needs `GATE_ROSTER_WHO=big-<sess>` inline** or G-AL checks a sibling's
  project. **And you must have run `~/Scripts/charter-read.sh <slug>` — POSITIONAL — or G-AL fails
  regardless.** `-53` spent two calls discovering the env-var forms do nothing.
- ⚠ **`board.py` NEEDS FOUR FLAGS AND WARNS ABOUT NONE OF THEM.** `./scripts/regen-board.sh`.
- ⚠ **HEREDOCS INSIDE `dx` DO NOT SURVIVE.** `-51` warned, `-52` lost a round trip, **`-53` lost
  one too** — a python heredoc with parentheses and apostrophes died in bash's `eval`. Write the
  script to a local file, `--put` it to `/tmp/`, run `python3 /tmp/x.py`. Three sessions have now
  paid for this; take it the first time. `git checkout <file>` is the free undo.
- ⚠ **SMALL DIFFS DO NOT NEED A TARBALL.** `cat f | /tmp/dx --put /Users/jasoncbraatz/repos/...`
  per file: one call, sha256 verified. `-53` pushed eight files that way. The tarball stanza is for
  coming DOWN only: `tar czf /tmp/wt-docs.tgz docs` is 1.2 MB against 20 MB and is all you need for
  docs-only work. `--get` with a leading `~` expands in the CLOUD and fails; use the full path.
- ⚠ **`lessons.py` AUTO-COMMITS AND AUTO-PUSHES each leaf.** Look before you reach for a commit. It
  refuses text that looks like captured command output and forks a twin on an id collision.
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started ·
  `5` crossed but mismatched.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
**SUITE:** 1058 collected, 1058 passed, zero skips — darwin ~64 s, cloud ~170 s.
`pytest -m tripwire` selects the tripwire class. `scripts/defensive_count.py` takes a positional
path. **Adding a manuscript to `docs/papers/` fails the suite until you add it to
`tests/test_defensive_count.py::MANUSCRIPTS` AND commit a `DEFENSIVE-BASELINE.json` beside it** —
`test_every_manuscript_in_the_estate_is_covered` is the census and it fired on Paper IV exactly as
designed, which is the nicest red this project has produced. **Probe sweep:** ~3 min 30 s per probe
at `--jobs 2`; a foreground `Bash` call dies at 10 minutes, so `nohup … &` and poll with
`sleep N; tail`. **Budget for running the sweep twice.**
---
## 0 · THE TELL, NOW IN SEVENTY-ONE SHAPES
`-28` through `-52`'s tells all stand (ask the instrument-artefact question of numbers that look
GOOD, that SETTLE AN ARGUMENT, of a REGISTERED CONTROL THAT FAILS, OF THE DENOMINATOR; a guard must
scan assertions not quotations; a mutation that does not mutate reports your guard as weak;
pre-commit the FAVOURABLE outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT;
a correction that lives only in a handoff has not been made; the visible reds are the cheap half;
a rule can be false on the day it is written; a count is not a measurement until it agrees across
machines). `-53` adds four:
- **A COMMISSIONED TEST THAT WAS NEVER RUN IS THE MOST DURABLE KIND OF DEBT, BECAUSE EVERY
  CITATION OF IT MAKES IT LOOK MORE ESTABLISHED.** `WT-006` proposed an instrument on day one, was
  cited as the whitespace's evidence in the corpus's central ADR, and sat unrun for eleven days
  across fifty sessions. Nothing pointed at it, because a METHOD entry reads like a finished
  object and a proposal cited often enough stops being read as a proposal. **When a document says
  a claim rests on a named test, run the test — the naming is not the running**, and the gap
  between them is invisible from either end.
- **A FAVOURABLE RESULT IS WHEN THE CONTROLS MATTER MOST, AND IT IS EXACTLY WHEN NOBODY LOOKS AT
  THEM.** REG-013 came back the way the corpus wanted. Everything load-bearing about it is in the
  two controls — a ceiling that cannot be tuned, a floor at exactly zero — and a reader who takes
  the three headline numbers alone has read nothing at all, because near-zero co-citation is the
  normal condition of any two specialties. **Design the controls before the run and print them
  beside the answer, or the answer is decoration.**
- **A COUNT WHOSE ANSWER MOVES WHEN THE FILE IS RE-WRAPPED IS MEASURING THE FORMATTING TOO.** `P1c`
  counted keywords plus mid-keyword line wraps and passed for two months because Paper III's wrap
  happened to land on a separator. **The failure mode is not that it was wrong; it is that it was
  right by accident**, which no re-run detects. Ask of every counter: what edit changes this number
  without changing the content?
- **A FACT CAN BE RECORDED AND STILL BE ABSENT AT THE POINT OF USE, AND THAT IS THE COMMON CASE.**
  `board.py`'s correct invocation was written down, in a machine-level registry the project's own
  tooling reads every session. It was still missing where a session needed it, because it was filed
  under the TOOL and the session was working inside the ARTEFACT. **"Is it written down?" is the
  wrong question. "Is it written down where the hand that needs it will already be?" is the one** —
  and the first question returns YES for most of the defects this project keeps finding.
---
## 7 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.
**Coffee status:** ☕ NINETEEN SESSIONS, and for the first time the corpus has all three papers on
disk. Ten sessions audited the apparatus, `-52` finally opened the manuscript and found an abstract
2.85× the venue's ceiling, and `-53` went looking for the sentence the whole project stands on —
*these three literatures don't meet* — and discovered that the test proving it had been commissioned
on day one, cited ever since, and never run. It runs now. **Six papers in the world cite both a
stock-flow-consistent seed and a kinetic-exchange seed.** The whitespace was where we said it was;
we just had never been able to say so with a number. 🥎
