---
project: wealth-tensor
session_n: 72
gh_repo: jasoncbraatz/wealth-tensor
branch: main
gh_sha: PENDING
updated: 2026-08-17
session: wealthTensor-72
live_theme: "Paper II's fourth independent read, taken as assigned, with the quantifier sweep run as an INSTRUMENT for the first time — 155 quantifier tokens on 117 lines, enumerated by a committed script rather than by attention. Three findings, three edits, none carded. The sharpest one is a paper that names a failure mode in §7 and commits that exact failure in §1: 'a single command named for numbers it does not produce is a provenance claim that reads as checked and is not' — and §1 claimed a single command. The tool matters more than the findings: this is the first coverage claim in the project that is countable rather than narrative, and it says Paper III is 864 tokens on 668 lines with no independent read at all."
phase: "Manuscript repair under a settled thesis. Paper II's convergence counter runs 9 → 2 → 4 → 3 across six passes and has NOT converged; each independent read finds a new SPECIES rather than a regression. The review method has now outrun the manuscript it was built on — and Paper III, which IS in the definition of done, has never been read once."
gate_passed: true
gate_version: "2.60"
next_at_bat: "ASSIGNED, not offered: PAPER III'S FIRST INDEPENDENT READ, with the quantifier sweep. This SETS ASIDE -70's conditional rule ('if Paper II returns findings, the next session is Paper II again') and the reason is in the handoff body under WHY PAPER III AND NOT PAPER II — the rule was written before the sweep was an instrument and before anyone had counted Paper III. DONE WHEN: Paper III read end-to-end; `python3 scripts/wt130_quantifier_sweep.py paper-III` run FIRST and its 864-token enumeration recorded in REVIEW-013; every finding repaired in-pass or carded with a named falsifier; REVIEW-013 exists with its own cleared list AND its own not-checked list; suite green, board re-checked, coach at Paper III's baseline of 5 conduct / 0 concessive. A ZERO IS AN ACCEPTABLE RESULT and would be the project's most surprising one. ~50 min — Paper III is 668 lines, the largest in the batch. Blocked? take the first startable item in the queue and say which, in ONE LINE, at the top of your handoff."
blockers: []
drift_flags: ["-70's conditional rule ('Paper II returns findings → next session is Paper II again') has now been applied three times and Paper II has not converged: 9 → 2 → 4 → 3, with a new species each pass. -72 is SETTING IT ASIDE for one session rather than overruling it permanently, because Paper III is in the definition_of_done and has had ZERO independent reads while Paper II has had six. If -73 disagrees on reading the reason, run Paper II's fifth read instead and say so — but do not let both defer.", "The queue's old item 1, 'Paper I's first P7 pass', remains demoted to 12: Paper I is NOT in definition_of_done and Paper II §7 calls it 'since superseded by its own internal referee'. Carried from -71, unchanged, still correct."]
parking_lot: []
definition_of_done: "Three preprints (II, III, IV) each at ready-to-submit per ADR-001 clauses, every number regenerated from committed scripts, convergence reached (two consecutive zero-finding review passes per paper), Jason's own-hand pass complete — then the batch declared, once."

---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-72` IN ONE LINE

**Took the assigned at-bat as ordered: Paper II's fourth independent `P7` read.** Ran the
quantifier sweep (`WT-115`) on a whole manuscript for the first time, **and turned it into a
committed instrument while doing so**. **Three findings, three edits (`wt129`), none carded.**
The counter runs **9 → 2 → 4 → 3**.

**The instrument is the deliverable; the three findings are its first receipt.**
`scripts/wt130_quantifier_sweep.py` enumerates every quantifier in any of the four manuscripts with
its line number. Paper II: **155 tokens on 117 lines.** That is the first coverage claim in this
project you can put a *number* on, diff against a later pass, and hand to someone else. *"I read it
carefully"* cannot be diffed. **`155 tokens on 117 lines, here is the list`** can.

Suite **1078 passed, 0 failed** (67.02 s). Board **66 criteria — `docs/CHECKLIST.md` unmodified,
the board did not move.** Coach **RC 0, all four papers at baseline** (II = 2/0). Abstract
**byte-identical, `PASS`.**

---

## READ FIRST, in this order

1. **`docs/REVIEW-012-P7-paperII-pass6.md`** — the pass of record. **§2's `II-19` is the one to
   read even if you skip everything else**: §7 of this paper *names a failure mode by name* and §1
   commits exactly it, four hundred lines earlier, and `REVIEW-005` quoted §7's warning approvingly
   without ever reading §1 against it. **§3 is a 17-row CLEARED list with the read-forward verdict
   spelled out**, **§4 is `wt128`'s blast-radius audit**, **§5 is the not-checked list and your
   brief is written from it**.
2. **`docs/LEDGER.md` `WT-116`** — the instrument, and the number that should decide your session:
   **Paper III is 864 quantifier tokens on 668 lines, more than the other three combined, and has
   never been independently read.** `WT-117` is the tell; `WT-118` is a guard-kit hardening that
   costs four lines and belongs in every patch script from here.
3. **`scripts/wt129_paperII_p7pass6_edits.py`** — `wt128`'s shape plus the `WT-118` before-check.
   Its docstring is the finding list. **`wt128` remains the exemplar for census-and-rewrap; `wt129`
   is the exemplar for guard honesty.**

---

## YOUR AT-BAT — ASSIGNED. Do not choose.

> # ▶ `-73`, YOUR AT-BAT IS: **PAPER III'S FIRST INDEPENDENT READ.**
>
> **Start here. You do not need to read the rest of this file to begin.** ~50 min — it is 668
> lines, the largest manuscript in the batch.
>
> **RUN THE INSTRUMENT BEFORE YOU READ A WORD.**
> `python3 scripts/wt130_quantifier_sweep.py paper-III --md`
> That prints 864 quantifier tokens with line numbers, in markdown, ready to paste into
> `REVIEW-013`. **The enumeration IS your reading order and IS your coverage claim.** For each
> line, read **FORWARD** to the end of the document and ask one question: *does anything below this
> sentence belong to the set it just counted, and is it in it?* A quantifier is written while
> looking at the material **above** it; the set it ranges over is finished **below** it — so the
> falsifier is never local and never upstream, and **`-72` proved that "downstream" includes four
> lines later in the same section** (`WT-117`). Do not skip the short hops.
>
> **Then read it whole anyway.** The sweep is one class of sentence. Paper III has had *no*
> independent read of any kind — numbers, references, cross-references, structure. The sweep gives
> you a spine and a countable floor; it is not the ceiling.
>
> **DONE WHEN:** Paper III read end-to-end; the sweep run and its enumeration recorded in
> `REVIEW-013`; every finding repaired in-pass or carded with a **named falsifier**; `REVIEW-013`
> carries its own **cleared** list AND its own **not-checked** list; suite green; board re-checked;
> coach at Paper III's baseline of **5 conduct / 0 concessive**.
>
> **A ZERO IS AN ACCEPTABLE RESULT** — and on a 668-line manuscript nobody has read, it would be
> the most surprising result this project has produced. Say so plainly if you get one.

### WHY PAPER III AND NOT PAPER II — the reason, because `-72` set a standing rule aside

`-70` wrote a conditional and it has been honoured twice: *"if Paper II returns findings, the next
session is Paper II again."* `-72` returned three findings, so by that rule you would be reading
Paper II a seventh time. **`-72` is setting the rule aside for one session, on purpose, and this
paragraph is the whole argument so you can overrule it if you disagree.**

- **The counter says the rule is not converging Paper II.** 9 → 2 → 4 → 3 across six passes. Each
  independent read finds a **new species** — pass 5 found scope, pass 6 found quantifiers — which
  means the sequence is not descending toward zero, it is enumerating categories.
- **Paper III is in the `definition_of_done`. It has had ZERO independent reads.** Paper II has had
  six. A manuscript at three findings is far closer to done than a manuscript at *unknown*.
- **The instrument that would be spent on Paper II's seventh pass has never been pointed at the
  place the numbers say it will pay.** 864 tokens against 155.
- **`-71` already re-ranked Paper III to queue item 1** for exactly the DoD reason. `-72` is
  following that ranking, not inventing one.

**If you read that and disagree, run Paper II's fifth read and say so in one line.** The one
outcome that must not happen is both sessions deferring. `-74`'s likely assignment: **Paper II's
fifth read**, which is the first half of its consecutive-zero pair — unless Paper III returns
enough to need a second pass, in which case Paper III again.

### THE QUEUE BEHIND IT — context, not a menu. Do not shop here.

**Reading this list is not a decision you are being asked to make.**

1. **Paper II's fifth independent read** — promoted from the assignment slot for the reason above.
   Counter at 3, six passes deep, species-per-pass still rotating.
2. **Paper IV §1–§3, re-read against `wt125`'s OWN output** (~15 min). `-69` read §1–§3 against
   `wt121` then patched them; **nobody has read them against `wt125`.**
3. **`REFERENCE-POLICY`'s seventh pass** — card `1217556161163494`. **`-72` did not read Paper II's
   References for anything but quantifier counts either** (`REVIEW-012` §5.3). That is **seven**
   sessions it would have covered — the single most-deferred item in the project.
4. **A `§N` cross-reference sweep**, the natural sibling of the quantifier sweep and named in
   `REVIEW-012` §5.7: Paper II carries ~40 `§x.y` references and **nobody has ever checked one
   against the actual section numbering**. Countable, scriptable, ~20 lines — `wt130` is the
   template. **`-72` would rank this above items 5–11 if it were not already handing you Paper III.**
5. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
6. **The ρ = 0 test UNDER-asserts** — card `1217547799559841`. Read the card first: tightening the
   float tolerance to `==` hands the next machine a red suite. Assert the **structural** property.
7. **The U+00B5 guard** — card `1217561398864561`. Five patch scripts now carry an in-script glyph
   guard; the tree-wide one is still missing.
8. **The `CONDUCT_ALLOWED_SECTIONS` gap** — card `1217562682350929`. `-68` hit it; `-69` through
   `-72` all avoided it only by reading the tuple first. **A landmine five sessions have walked
   around** — which is five data points that the tuple should be documented where the writer looks.
9. **A gate check that a `§N` named in `HANDOFF.md` exists in the paper it names** — card
   `1217564707330383` (`WT-112`). ~6 lines. Overlaps item 4; do them together.
10. **The duplicated Bouchaud–Mézard description** — card `1217565324215216`, filed by `-71`. §3.1
    and §6 carry the same ~40 words about one source. **`-72` confirms it is still there** and
    still latent; the placement was settled at `bf07363`, so it needs a decision, not a patch.
11. **PASTE THE HANDOFF forcing function** — card `1217560480809492`. (`-67` through `-72` all
    pasted. **Six** data points, still not a fix.)
12. **Paper II's companion reference entries** — card `1217542940968749`.
13. **PAPER I'S FIRST `P7` PASS** — still demoted, still for `drift_flags`' reason.
14. **`A3` from the PAN AAR — estate-level, STILL UNCHECKED.** Not a wealth-tensor at-bat; named as
    unchecked so it is not mistaken for checked.

---

## WHAT `-72` DID, so you do not re-derive it

**One at-bat: Paper II read whole, lines 1–545, quantifier sweep plus `wt128` blast-radius audit.**
Provenance verified before reading rather than believed: the diff against `.bak-wt71-p7` was taken
**first** and is exactly `wt128`'s five edits and nothing else.

**The three findings, all applied by `wt129`:**

- **`II-19` — §1 makes the exact claim §7 forbids by name.** §1 contribution 5: *"every number
  below is regenerated by **a single command** from a public repository."* §7: *"The two commands
  are named separately because **a single command named for numbers it does not produce is a
  provenance claim that reads as checked and is not**."* Now: *"regenerated from a public
  repository by the two commands §7 names"*. **The general rule is `WT-117`: when a document names
  a failure mode, grep the document for that failure mode. It is the highest-yield grep available
  and it is free.**
- **`II-20` — §7 contradicts itself four lines later, and this is `wt128`'s blast radius.** §7
  opens *"every number is generated by simulation"*; four lines on it carves out the three
  Var[log *a*] values as *"quadrature rather than simulation output"*. `wt128` propagated that
  carve-out into §5 limitation 5 and did not read §7's own universal against it. **The repair
  APPENDS rather than rewrites** — *"…by simulation, save the three quadrature values the next
  bullet names"* — because the original clause is **quoted verbatim** in `docs/END-TO-END-001.md`
  and `docs/RESULT-END-TO-END-001-E3.md`, both dated records of a **CLOSED** result. `wt129`
  carries a substring guard proving the quotation still resolves. **Records are preserved; the live
  document moves around them.**
- **`II-21` — §2.3's *"no result below depends on a value of ρ we picked"* is falsified by §3.1 and
  §3.2.** Every flow row in §3.1 is at ρ = 1 (its own footnote says *"the implementation's
  default"*), and §3.2 shows the reachable flow Gini running **0.125 → 0.395 → 0.994** across the ρ
  axis. §3.1's headline *"stock 0.000 < flow 0.125"* **is** the ρ = 1 number; at ρ = 0 there is no
  nesting. Now: *"§3.1's flow rows are stated at ρ = 1 and labelled as such, §3.2 sweeps the axis,
  and the paper's central result is a statement about the whole ρ axis rather than about a value of
  ρ chosen to make it come out right."* The defensible half survives.

**`wt128`'s blast radius, audited in full (`REVIEW-012` §4) — one hit, and one pleasant surprise.**
The one hit is `II-20`. The surprise: **`wt128`'s "these six rows are a selection" footnote
retroactively REPAIRED three sentences it did not touch** — §3.1's *"at every rate tested"*, its
*"a stock levy reaches at rate 0.25"* (no such row exists in the table) and §3.4's
*"0.000–0.891"* span, all of which had no visible support before that footnote existed. Blast
radius runs both directions and this project had only ever recorded the bad one.

**Nothing was carded.** All three were repairable in-pass with no new number and no decision owed
to Jason.

---

## ✅ NEW SETTLED, DO NOT REOPEN

- **`-72`'s three repairs are settled AS REPAIRS.** Their blast radius is `-73`'s job only if `-73`
  touches Paper II, which the assignment says it should not.
- **The abstract was deliberately NOT changed** although it carries `II-21`'s undisclosed ρ = 1
  dependency (*"the frontiers are nested, stock 0.000 against flow 0.125"*). 244 words / 1478
  characters is the closest to arXiv's ceiling in the batch, `P3l` needs `falsified` **and**
  `nested` to survive in it, and §3.1's footnote discloses ρ = 1 one screen below. **`wt129`
  asserts the abstract is byte-identical.** If a later pass judges it must carry the caveat, that
  is a word-budget decision, not a review finding — and `REVIEW-012` §2 says so in writing.
- **`END-TO-END-001` and `RESULT-...-E3`'s quotations of Paper II §7 were left alone on purpose**
  and remain valid — the repair was an append precisely so they would. Same doctrine as
  `patch_wt56_e1_remedy.py`'s quoted text. **Do not "fix" them into agreement with the new
  sentence; they are dated records.**
- Everything `-71` settled stays settled: `wt128` ran and is not to be edited (the successor script
  is the fix); Paper II §5 item 1 is `P3g`'s and stays there; the *"Version 0.2, 2026-08-11"* header
  above 2026-08-17 content is a **CONVENTION** across all four manuscripts, not rot — do not "fix"
  it into an inconsistency. Paper IV's framing ruled and propagated through §10; card
  `1217561330623702` at (a); `DECISION-001` closed at A; `WT-103`; the 14 household-to-sovereign
  occurrences untouched on purpose; `REG-012` §4.7 appends Amendments; `WT-094` grep `tests/` +
  `scripts/` first; **never delete "18 tests"**; no re-deriving κ residuals / III-1's 4.2× / E2
  blind pass; `REVIEW-004` verbatim quotes only; `REVIEW-005` §2's `II-3` is WRONG about the code;
  end-to-end **CLOSED**.

---

## THE TELL, now EIGHTEEN deep

`-61` through `-68` as before. `-69`(i): a framing patch's blast radius is every line that agreed
with the old framing in its own words. `-69`(ii): a guard on a self-describing document must be
written in identity, not quantity. `-70`(i): a census and an identity guard prove what the text
SAYS; neither looks at WHERE IT SITS. `-70`(ii): the censused string is not the only string — and a
scope note needs two halves. `-71`: a quantifier is contradicted downstream, never upstream — so
read forward from it.

**`-72`(i): DOWNSTREAM INCLUDES FOUR LINES LATER.** `-71` gave the direction; the open question was
how far to read. The answer is *"to the end, starting immediately"*, and the immediate part is the
half that gets skipped. A reviewer hunting cross-section contradictions treats the next paragraph
as already-read — but they read those lines **before the quantifier registered as a claim about a
set**, which is not the same as having checked them against it. §7's universal and §7's carve-out
are one paragraph apart and survived five passes.

**`-72`(ii): WHEN A DOCUMENT NAMES A FAILURE MODE, GREP THE DOCUMENT FOR THAT FAILURE MODE.** Free,
mechanical, and it caught the sharpest finding of the session. A document articulate enough to
describe a defect is a document worth searching for that defect — and the more carefully the rule
is written, the more likely the author was fixing one instance rather than sweeping for all of
them. `REVIEW-005` even *quoted* §7's rule approvingly, one review pass, while §1 sat in violation.

**`-72`(iii), on the kit rather than the manuscript: A GUARD HAS TWO FAILURE MODES AND THE RED
OUTPUT CANNOT TELL THEM APART.** *The edit broke the invariant* and *the invariant was never true*
look identical. `wt129` failed its first run on a phrase that had **always** wrapped; the guard was
wrong, not the edit. The fix is four lines — assert every invariant against the ORIGINAL before
checking it against the patch — and it puts the distinction **in the error message**, at the moment
it is worth the most. This is `-49`'s vacuous-predicate rule rotated 180°: `-49` covered a guard
that passes when it should not; this covers a guard that fails when nothing is wrong. **`WT-118`.**

---

## TOOLING (▲ new at `-72`)

Everything from `-71` stands: gate as
`GATE_ROSTER_WHO=big-wealthTensor-NN nohup ~/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1 &`,
~170 s polls. Wrap: PENDING → commit → `--stamp` → commit → push → `--emit` → **PASTE**. Run the
coach directly rather than waiting for the gate: `python3 scripts/handoff_gate.py --coach`, RC 0
when all four are at baseline (I = 1, II = 2, III = 5, IV = 1 conduct; 0 concessive throughout).
`--coach-refresh` is a deliberate act, not a fix for a red run. **Read
`scripts/handoff_gate.py`'s `CONDUCT` / `CONCESSIVES` / `CONDUCT_ALLOWED_SECTIONS` tuples
(~L246–260, case-sensitive) BEFORE writing prose** — four clean sessions running, all four for
that reason. Five-second board read:
`awk -F"\t" '/paper-III/{print NR": "$1" | "$2}' docs/done-criteria.tsv`.

- ▲ **`scripts/wt130_quantifier_sweep.py`** — the sweep as an instrument. `--md` emits a markdown
  table straight into a `REVIEW` doc. No args = counts for all four manuscripts in four lines,
  which is the cheapest orientation move in the repo. **Run it before reading anything.**
- ▲ **`wt129`'s before-check (`WT-118`)** — copy the four lines into every patch script.
- ▲ **`--census` on the patch script matches the patch script itself.** Expected, not a bug: the
  anchors are literals in the source. `.bak-*` files are skipped because their suffix is not `.md`,
  which is also correct — but neither is obvious at 2 a.m., so both are written down here.
- ▲ **Appending to a big doc** (unchanged, worked first try): `--put` the block to `/tmp/`, then
  `dx 'cp X X.bak-wtNN && cat /tmp/block >> X'`. One round trip, backup first, never re-upload a
  60 KB ledger.
- ▲ **A multi-command bank/wrap script beats chaining through `dx`.** `-72` put a 5-line
  `bash` script with three `lessons.py add` calls plus `use` plus `record-outcome` to `/tmp/` and
  ran it in one call — no quoting war with nested single quotes inside `dx '...'`, and the whole
  thing is re-runnable if a leg fails.
- ▲ Tags run to `wt130`; **`wt131` is free.** `.bak-*` gitignored — the undo path lives on darwin,
  do not force-add.

---

## JASON-SIZED, not yours

**(a)** `DECISION-001` closed. **(b)** Paper IV framing ruled and propagated.

**(c) `P7` is still ONE BOOLEAN — the only open wealth-tensor Jason item — and `-72` closes the
argument rather than adding to it.** `-70` moved the board with an edit that changed no sentence.
`-71` changed five sentences and the board did not move. **`-72` changed three more and it did not
move again.** Three sessions, same direction: **the board is a working instrument pointed at
STRUCTURE — position, presence, naming — and it is silent on TRUTH.** That is no longer a
suspicion.

So the live question is the one `-71` posed — *should a criterion track internal consistency at
all, or is that permanently the reviewer's job?* — and `-72` can now put a concrete proposal under
it, which is what changed:

> **A criterion cannot check whether a quantifier is TRUE. It can check whether the ENUMERATION HAS
> BEEN RUN AND RECORDED for this manuscript at this SHA.** `wt130_quantifier_sweep.py` emits a
> countable artefact — `155 tokens on 117 lines` — and a board row could require that
> `REVIEW-0NN` for each paper carries a sweep whose counts match a fresh run. That measures
> **coverage**, not truth, which is the honest thing a script can know — and it is the first
> criterion this project could add that is not about structure.

**One line of yours settles it: yes, add the coverage row, or no, reviewing stays narrative.**

**(d)** The PAN history purge — Batter's Box `1217561667484767`; do NOT rewrite `claude-blackbook`
history on your own initiative.

🥎

---

## WHY NOT `P13`, since `charter-read.sh` asks

`charter-read.sh` reports **`P13` as the first OPEN lane in dependency order** — the beautifully
designed, arXiv-ready PDF. `-72` worked **`P7`** instead, as assigned, and the project's own
ordering ruling is why: **`P13` is a point-in-time capture of the corpus**, and capturing a corpus
whose manuscripts still yield three to four findings per read produces a beautiful PDF of prose
that is about to change. `P7` → `P13` → `P8` is the DoD's own sequence. **This is the answer every
session from `-61` on has given; it is written down here so `-73` can point at it in one line
instead of re-deriving it.**

`-72` adds one number to it rather than restating it: **Paper III is 864 quantifier tokens on 668
lines and has never been read.** Typesetting a manuscript nobody has reviewed is the strongest
form of the same mistake, and it is the reason `P13` should not move until Paper III has had at
least one pass.

---

## AT WRAP

`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` **and say the number** (summary line,
never `$?`, never through a pipe); `roster leave --who <you>` once; and **paste a handoff better
than this one into the chat as the last act.** Assign `-74` ONE at-bat with a definition of done.
Do not hand them a menu. 🥎
