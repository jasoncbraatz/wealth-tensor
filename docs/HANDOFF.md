---
project: wealth-tensor
gh_sha: 76b39a585a4470aa2e2580a79305cb65ede93681
updated: 2026-08-17
session: wealthTensor-60
gate_passed: false
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16, superseding the 'three preprints publicly posted' line carried since sessionZero): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF
`gh_sha` names the commit this file describes; **the only thing added after it is this file**, so
`python3 scripts/handoff_gate.py --check` prints `ADVISORY: docs-only drift` and exits 0. Assert the
exit code exactly. **`| tail` MASKS `$?` ON EVERY `dx` CALL** — `cmd; echo rc=$?` with no pipe, or
you are reading `tail`'s status.

> ⚠ **`gate_passed: false`, FOURTH CONSECUTIVE SESSION, SAME TWO FILES, AND NOTHING NEW IS WRONG.**
> `G-A`→`G-AJ` all green. Every repo `-60` touched — `wealth-tensor`, `claude-blackbook` — is
> committed AND pushed, tree clean. The single `FAIL` is `~/Scripts DIRTY(2)`:
> `braatz-crawl-check.py` and `serve-braatz-archive.py`, untracked, belonging to
> **`big_worker-braatzArchive`**, now 6 h live and still holding no claim on that repo. **Do not
> commit them.** `-59`'s diagnosis stands verbatim and is not reopened.
>
> **`-60` adds a THIRD attribution route the card did not have, and did not implement it.**
> Both existing routes are wrong: normalising `G-H#22c` does not match, and shared-token overlap on
> `braatz` weakens a safety guard on Jason's own surname. The third is **attribute by TIME, not by
> name** — a file whose mtime predates your own `roster join` and falls inside a live sibling's
> window **cannot be yours**, which is a fact rather than a heuristic, and it can only ever move a
> file *away* from you. It is **strictly stronger** than the weakening route and it generalises to
> siblings with no naming convention at all. Declined here for `-59`'s exact reason, which binds:
> a judgement change to a safety guard wants its own at-bat and its own drill. Drill cases written
> out on card `1217526943288480`.
>
> **And say this out loud, because it is the real cost:** a red that is right about the facts and
> wrong about the owner, four sessions running, stops being a signal and becomes weather. **A
> session that learns to expect a red gate will not notice a real one.**

---
## 0 · TWO ITEMS OFF YOUR LIST BEFORE YOU START — both closed by MEASUREMENT, not by fixing

1. **`lessons.py record-outcome` DOES auto-commit and push. Delete it from every list.** Three
   consecutive handoffs carried *"`record-outcome` STILL DOES NOT AUTO-COMMIT, unlike `add` and
   `use`"*, and `-59` sharpened it to *"the fix is now located: the helper is `lessons.py:1012
   _git_commit_push`, and `record-outcome` is the one caller that never reaches it."* **It reaches
   it at `lessons.py:846`, added 2026-08-04.** Measured live: `record-outcome wt60-e4 pass` →
   `[lessons] auto-committed + pushed: lesson(outcome): wt60-e4 pass: 3 leaf(s)`, tree clean,
   HEAD `cbf44cad`. The only no-commit path is `if touched:` being false, and in that case nothing
   changed either.
2. **The phantom-claim card `1217527629536618` IS updated.** `-59` handed it on as its one loose
   end; the comment landed at 21:43 on the 16th, after the handoff was written. Nothing to do.

**And the lesson that closes both, banked global:** *a teed-up item that names a file and a line has
been **located**, not **verified** — and the precision is exactly what makes the next session skip
the check.* A line number lends a located claim the authority of a measured one. **Before carrying
a teed-up item a fourth time, run it once.** It is cheaper than the sentence describing it.

---
## ORIENT — read these first, in this order
1. **`docs/RESULT-END-TO-END-001-E4.md`** — `-60`'s. Read **§4 before §3**: the verdict is REFUTED
   and the leg's substantive target is untouched by it, which is the whole point of the document.
   §3.2 lists three of `-60`'s own published grounds that round two struck, and is the most useful
   page for anyone about to run `E6`.
2. **`docs/DECISION-001-A2-and-road-one.md`** — `-60`'s, **AND IT IS WAITING ON JASON.** One page,
   three options, tick-boxes. If he has ticked one, that is your at-bat (§3). If he has not, do not
   re-litigate it and do not write a second one.
3. **`docs/RESULT-END-TO-END-001-E2.md`** (`-59`) · **`-E5.md`** (`-58`) · **`-E3.md`** (`-57`) ·
   **`-E1.md`** (`-56`). `E3` §5 and `E2`'s blind pass are still the two cheapest unmined pages.
4. **`docs/END-TO-END-001.md`** — the registration. **FIXED. May not be edited in response to a
   result. NOW 0-FOR-8**, and the eighth is the seventh's twin (§5.1 of `-E4`). Read freely; the
   reading restriction was lifted at `-59` and stays lifted.
5. **`docs/CHECKLIST.md`** — 66 criteria, **50 met**. `./scripts/regen-board.sh`, never `board.py`
   by hand. `P11a`–`P11e` green; **`P11f` is the first open lane in dependency order**, `P11g` red
   and correctly so.
6. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS.**
   `~/Scripts/charter-read.sh wealthTensor-<NN>` — POSITIONAL slug. **Re-stamp IMMEDIATELY BEFORE
   THE GATE**, always.
7. `docs/adr/ADR-001` (title and §Decision frozen) · `scripts/gen_apparatus_rows.py`'s docstring
   before touching any apparatus row · `scripts/add_p11_rows.py` + `scripts/redproof_p11.py` before
   any `P11` row · `scripts/redproof_apparatus.py` · `tests/test_paper_test_counts_are_derived.py`
   + `scripts/redproof_paper_counts.py` before touching a quoted test count.
8. REG-013 + `RESULT-REG-013` §4.1 · REG-003 §§3.2/3.3/7 · SCOUT-001 · REG-012 §§6–7 ·
   RESULT-TERM-001/002 · REG-010 §1/§4 · CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (HEADER NOTE
   FIRST).

---
## `-60` in one line
**THE CHEAPEST HONEST LEG LEFT CAME BACK THE OTHER WAY: `E4` EXPECTED ZERO AND THE CORPUS HAS FIVE
CONFIRMED CLAIMS ABOUT THE WORLD — AND THE REASON THE DESIGNER EXPECTED ZERO IS A SENTENCE IN PAPER
III THAT HAS BEEN STALE SINCE THE TWELFTH OF AUGUST.** `E4` — FAILURE REFUTED, AUDIT leg, **`T`
remains 2, THE SYSTEM FAILS still stands on `E1` and `E3`.** Off the leg: **the A2 one-pager exists
after six sessions**, and its headline is that half of Road One was already in Paper II, unlabelled.

---
## 1 · WHAT HAPPENED

### `E4`, and why REFUTED is not a win
E4 asks for *"every claim in the corpus about the world — not about a model, not about a literature
— that any paper asserts as confirmed."* **FAILURE = count zero AND corpus-level silence** — a
conjunction. The count is **five**, so FAILURE cannot hold. All five are Paper III, all measured on
SEC EDGAR: the disclosed-lives first rung (0.659 of 665 pairs), α̂ = 0.408/yr [0.383, 0.432],
Weibull k̂ = 1.210 [1.135, 1.285], the 4.12×/2.02× non-diagonality at *p* = 0.0002, and the REG-008
disclosure absence. Verdict invariant to every merge and strike the run could construct: strictest
merge → 4, strike the strongest item → 3, strike two → 2. **Zero is reachable only by adding a third
exclusion the registration does not contain**, and the registration itself already drew that line
the other way — E2's power check reads *"Paper III measures a filter **and one EDGAR sample**."*

**The leg's target survives its own verdict, and that is the finding.** No document in the corpus
states the corpus-level position; five candidates were tabulated and every one does something else
(a thesis, a dependency disclosure, a normative boundary). **So the silence is real and now conceals
an understatement rather than a zero.**

### The stale sentence — measurable rather than arguable
Paper III §6.1's three-bullet accounting is **byte-identical** in the current manuscript and in
`paper-III.md.bak-pre-wt089` (md5 `620a61e6…` for the block in both). **That backup contains zero
occurrences of `4.12` and has no §5.4 at all.** So *"A reader who wants to know what **this paper**
has established about the world should read that list literally"* was written **before the
measurements it omits existed** and was never updated. **`P7`, Paper III, §6.1. Logged as `P7` under
§1.1, scores nothing at system level, and deliberately NOT repaired by the leg.**

### Two rounds, and what round two cost the run
Round one put refuters on the whole finding and on the verdict mechanics; **both failed to reach
zero.** Round two was aimed where `-59`'s fourth tell says — at the survivor — **and also at the
four claims round one introduced while arguing about something else.** That second aim is the new
part and it earned its keep: **three of `-60`'s own published grounds were struck.**
- *"and Paper IV asserts it as settled fact in a second paper"* — **STRUCK.** Paper IV §9.2's flat
  wording first appears in `paper-IV.md.bak-wt56-e1`; the liftoff snapshot reads *"its test is
  **open**. **If** recognition events cluster…"*. It is `-55`'s **own E6 repair**, announced in the
  registration and expressly excluded from E6's run. Citing it is citing the pass to itself — **and
  it would be inadmissible anyway**, because §9.3 says the paper contributes no computation and
  §9.2 carries *"(Paper III §5.4)"* in its own text. One claim seen twice.
- *"all in §4.4 and §5.4"* — **STRUCK.** §A.2.2's SDG 7.3.1 statement and §4.4's ASC statements are
  world-claims of the institutional class.
- *"all pre-registered"* — **STRUCK.** The paper labels three named cuts *unregistered* on their own
  faces.
- A **ninth** registration defect proposed by `-60`'s own refuter was **REJECTED on the record**
  (§5.1 of `-E4`): *"governs"* is a scope-transfer claim, not an assertion a count can falsify. **A
  defect tally that accepts every candidate is worth nothing.**

### `DECISION-001` — six sessions, and the headline nobody expected
**Half of Road One is already in Paper II, unlabelled.** §3.1's Var[log *a*] triple — **0.076542**
unlevied, **0.076536** stock (six parts in a million), **0.051189** flow — **is A2's Kesten
mechanism, measured.** And `wt077_tail_index.py` also returned the item `ROADS-001` called *"the
strongest claim and the one most likely to be wrong"*: at *r* = 1, ess-sup *a* = 0.9524 < 1, **no
power-law tail exists at all.** That is in `HANDOFF-PROMPT.md` in a parenthesis and **nowhere in the
paper.** Road One's two hardest computations are **done**; what blocks it is a literature search
that has **never been run** (grep finds *optimal-taxation-with-Pareto-tails* only at the three
places recommending it).

**A2 is two-thirds right.** κ-as-mechanism is dead, certainly, from the paper's own two rows plus
§3.3's free threshold — and it is still asserted in **five** live places (abstract, §1 contribution
2, §2.4, §3.1's heading and gloss, §6). **A2's title half does not follow:** the frontiers are
*nested* (stock 0.000 < flow 0.125) and the paper says so in its own abstract, so flow-at-*r*=1
beating stock-at-*r*=0.1 is a comparison across rates, which *"the rate moves you within it"*
permits. The accurate charge is `REVIEW-004` E5 #7's, not A2's headline. Three options priced;
**Jason ticks one.**

### Counts, and the numbers
**TEST legs run 4 · FAILED 2 · UNDECIDED 1 · REFUTED 1. AUDIT legs run 1 · FAILED 0 · REFUTED 1.
No combined score exists and none is offered.**

| | |
|---|---|
| board | 66 criteria, **50 met**, `P11d` green; first open lane `P11f` |
| lessons | **3 banked** (2 global, 1 project) · 3 `use` + 1 `record-outcome pass` |
| corpus edits | **none** — an AUDIT leg returning REFUTED should leave the corpus alone |
| commits | `76b39a5` (wealth-tensor, E4 + DECISION-001 + board) · `cbf44cad` and 4 more (blackbook) |
| gate | `G-A`→`G-AJ` green, ONE issue: `~/Scripts DIRTY(2)`, the sibling's |
| cards | `1217529210807546` NEW · `1217526943288480` × 2 comments · `1217527629536618` already closed |

---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-59`'s rulings stand verbatim**, including: `END-TO-END-001` IS FIXED AND
  MAY NOT BE EDITED IN RESPONSE TO A RESULT; A LEG MAY NOT COUNT A FINDING MADE BEFORE IT EXISTED;
  TEST AND AUDIT COUNTS ARE REPORTED SEPARATELY; **THE ADMISSION CRITERION IS NOT ADVISORY**; DO NOT
  ADD AN OBSERVABLE TO A LEG'S OWN FAILURE CRITERION; REG-013's DECISION RULE IS SPENT; H1 LICENSES
  OCCUPANCY; `P2`/`P3`/`P5` STAY MANUAL; ADR-001's TITLE AND §Decision FROZEN; THE ABSTRACT IS A
  SUBMISSION FIELD; THE ARM IS δ; DO NOT SPEND THE TIE-BREAK; **R5 IS UNSPENT**; T4's WIDTH IS
  31.7 %; **T2 MAY NOT BE RUN ON THIS DATA**; §4.7 IS PINNED AT `ba59370`; `wt107` IS NOT EDITED;
  APPARATUS SUB-ROWS ARE GENERATED; A ROW IS NOT DONE UNTIL SEEN RED; `P8` IS ONE PASS TAKEN LAST;
  `P7` DOES NOT CLOSE THE CORPUS; DONE IS "CLEARED FOR LIFTOFF"; **`P13` IS LAST**; ROW IDS ARE
  NEVER RENUMBERED; **DO NOT EDIT `src/`**; `T = 2`, **THE SYSTEM FAILS**, AND `T` CAN RISE AND
  CANNOT FALL; **`E1`, `E2`, `E5` ARE SPENT**; PAPER III §2–§3.1 IS THE HOUSEHOLD-SCALE WITNESS;
  `E2`'s LIMB (b) IS RECORDED AND UNRULED.
- **NEW · `E4` IS SPENT AND ITS ANSWER IS FAILURE REFUTED.** Do not re-run it. **`E4` IS AN AUDIT
  LEG AND CANNOT MOVE `T` IN EITHER DIRECTION.** `T = 2`; THE SYSTEM FAILS, on `E1` and `E3`,
  exactly as before `-E4` existed.
- **NEW · `E4`'s REMEDY IS NOT APPLIED AND MAY NOT BE.** Its one pre-registered sentence in Paper IV
  is stated *unconditionally*, unlike every other leg's — that is a design defect, flagged and
  routed to `END-TO-END-002`. `-57`'s ruling binds: **a remedy whose triggering finding did not
  occur may not be applied.** A successor who thinks the sentence is worth writing anyway should
  note that the true sentence is now *harder* than the designer expected — five claims and a stale
  summary, not a clean zero.
- **NEW · THE CORPUS HAS FIVE CONFIRMED CLAIMS ABOUT THE WORLD, AND EVERY ONE RUNS AGAINST THE
  MODEL.** W1 overturns the paper's own rectangle, W2 its own calibration, W3 its own constant
  hazard, W4 its own diagonality assumption, W5 its own fallback route. **Do not read this as
  "the framework has empirical support."** A corpus that measured its own assumptions false and
  published the numbers has confirmed claims about the world and no confirmed claims in its favour.
  §6.1 is right about that even while it is stale about the rest.
- **NEW · THE REGISTRATION IS 0-FOR-8**, and the eighth is the seventh's species: `§E6` quotes
  Paper IV §9.2 without its trailing scope clause *"at the scale where accounting happens"*, no
  ellipsis. **Twice now unreliable about the corpus, both times by amputating a qualifier.**
- **NEW · `E4`'s CLAUSE PAIR HAS TWO REACHABLE GAPS AND ONE THAT IS NOT.** Reachable: the
  *"in terms"* strictness gap, and the *"with the claims named"* conjunct gap. **NOT reachable:**
  the `document`/`paper` asymmetry, because §1 defines the corpus as exactly Papers II, III and IV,
  so the two terms are coextensive. Routed to `END-TO-END-002`; **do not re-derive this.**

---
## 3 · THE AT-BAT for `-61` — **`E6`, AND THEN THE DOCUMENT THE WHOLE PASS IS FOR**

**Take two. Neither is more than about an hour.**

**1 · `E6` — THE CROSS-PAPER CONTRADICTION (`[AUDIT]`, `P11f`, where the board now points).** The
last unrun leg. **Read the leg's own note FIRST**: its worked example is **excluded from its own
run** (*"a leg may not count a finding made before it existed"*), and `-60` established the
provenance you will need — the example was repaired by `-55` in the commit after the registration,
and the repaired text is what is in Paper IV today. **You are running E6 against a corpus one of
whose contradictions has already been repaired out of it, and the registration says so.** Budget
your reading accordingly, and do not re-find the repaired one and report it.
**Free material, already paid for:** `RESULT-…-E2-blind-pass.md` §§3–4 — 28 belief/ownership rows
from two adversarial builders, of which `E2` asked exactly one question. **Paper IV §1.1's
*"firm-level panels of both are public and free"* against its own §9.1 and Paper III §9.5 is
explicitly `E6`'s shape and has been waiting three sessions.** `-60`'s two extraction passes also
turned up an unscored candidate `E6` should look at: **Paper IV §7 calls SDG 7.3.1
*"the strongest available evidence that the quantity is not an invention of the framework"*, while
Paper III §A.2.2 says *"It is emphatically **not** that SDG 7.3.1 measures Λ⁻¹"* and §9 limitation 5
says *"the same quantity dimensionally, not empirically."* Hedged where produced, flat where used —
which is `E6`'s exact question.**

**2 · `P11g` — THE PASS-LEVEL `docs/RESULT-END-TO-END-001.md`, WHICH STILL DOES NOT EXIST.** After
`E6` it is **the last thing between `P11` and `P13`**, and it becomes writable the moment `E6`
returns. Its verdict is read off §3's rule, not off anyone's judgement, and the rule needs both
counts kept separate — **TEST 4/2/1/1 and AUDIT 2/?/? — never a combined score.** If `E6` finishes
with time left, **write it in the same session**: it is the artefact the whole pass is for, and it
has been one leg away for three sessions.

> **FORCING LINE, and it is `-59`'s ruling, kept: a session that takes neither of the two items
> above must say why in ONE LINE at the top of its handoff.** `-60` took both of its two and reports
> that the line cost nothing and the rule works.

**If Jason has ticked `DECISION-001`,** that is your at-bat instead and it outranks the board. **A**
is ~6 edits and no new computation. **B** is A plus the title plus 4 downstream reference edits. **C**
means the next at-bat is **the literature search**, not the prose — and the prose only follows if
the search comes back clean. **Do not start C's prose before the search.**

**The honest alternatives, ranked:**
- **`P7` on Paper III §6.1** — the stale sentence `-60` found and measured but may not repair
  (a leg may not apply a repair whose antecedent did not occur, and `P7` is scored separately from
  whoever did the work). **The evidence is in `-E4` §4.1 and it is an md5, not an argument.**
- **`P7` on Paper IV's §5 and §10** — the missing regeneration command (Builder B's #7),
  pre-existing, `§1.2`-excluded from system-level failure, unrepaired.
- **`P6`'s remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
- **`P13`. STILL LAST**, and its subject matter is decided: three works, not one stack.

---
## 4 · TEED UP, IN ORDER
- **THE `E2` BLIND PASS IS STILL AN UNMINED DEFECT INVENTORY** — `-60` read it and used none of it
  for `E4`, because `E4`'s question is not its question. Paper III's abstract stronger than its body
  at **three** places (B#2, B#4, B#8's τ = −1 and the 2.58× that is a leverage-to-**budget** ratio
  against a **0.61** threshold, i.e. 4.2×). Live `P7` material nobody has scored.
- **NEW · THE BOARD DOES NOT COUNT `DECISION-001`, AND THAT IS THE MECHANISM `-59` WAS LOOKING
  FOR.** `CHECKLIST.md` and `done-criteria.tsv` contain **zero** rows for A2, `REVIEW-004`,
  `ROADS-001`, Road One or Road Two; `LEDGER.md` has **no `WT-077` entry** and no mention of any of
  them. An item that lives only in handoff prose is an item the project **cannot notice being
  dropped** — which is exactly how six sessions passed on it at no cost. Carded
  **`1217529210807546`** with the general fix (a check that FAILs when `HANDOFF.md` §3/§4 names an
  item no `done-criteria.tsv` row and no `LEDGER.md` entry mentions). `-60` deliberately did **not**
  add a board row unilaterally, because adding a criterion moves the **66** that every handoff
  quotes and that should be somebody's at-bat, not a footnote in the last twenty minutes.
- **NEW · `Λ⁻¹` / SDG 7.3.1 IS AN UNSCORED CROSS-PAPER CANDIDATE** — see §3, item 1. `E6`'s shape.
- **PAPER IV'S TITLE IS ONE STEP AHEAD OF ITS OWN NARROWED ABSTRACT** — *"one atomic unit from the
  household to the sovereign"*. `E2` made the *range* defensible; what is undefended is *unit*.
  Jason-sized.
- **`G-H#22c` — THREE ROUTES NOW, and the third is the good one.** Card `1217526943288480`, drill
  cases written out. Attribute by time, not by name.
- **`~/Scripts/gate-selfcheck.sh` IS A SYMLINK INTO `~/code/darwin-mac-ops`.** `git add` in
  `~/Scripts` stages nothing **and reports success.**
- **`~/Scripts` IS STILL `DIRTY(2)`** with the sibling's two untracked files. `git add <paths>`,
  never `-A`.
- **`P1n` and `P5n`** — `P3n` repointed. Half an hour, moves `P6`.
- **The use/mention guard, generalised.** Applied in exactly one place.
- **C26 limb B** — carded `1217525563299334`. **RESULT-REG-003 §2's "Every cut lands in R1"** —
  carded `1217518687033967`.
- **Cell (b), ranked in `-E3` §3.2 — THREE entries left**, measured, paused behind the papers.
- **C37's tripwire** — REG-009 §12's "never by narration". **§7's ledger dilutes its own two
  load-bearing rows** — Jason's call, TRIPWIRED not carded.
- **Dossier era, re-served by nobody:** `REVIEW-004` C6 (ASC 410) and C10 (IAS 36's reversal
  asymmetry). *C10 is `REVIEW-004`'s, not the inventory's; the collision has bitten three times.*
- **REG-013 re-run worth doing:** the biophysical audience was capped at 4 000 of 7 801.
- Infra siblings, carded: Caddy `1217488447555628` · capability path `1217488117177482` ·
  AAR A2's four post-\* hooks · card-lint `1217483699706758` · gate `1217465036940491`.

---
## 5 · DO NOT
- **Everything `-31`→`-59` forbade still stands verbatim** — R5, the two sensitivities,
  `selected_lives`, §4.4's 0.3000, T4's 31.7 %, the δ arm, TERM-001/002, §9's list well-formedness,
  `wt107` IS NOT EDITED, §4.7 IS PINNED AT `ba59370`, DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD, DO
  NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION, DO NOT GRADE A CONSTRAINT FROM THE
  `machine` COLUMN, DO NOT WIDEN C07's GUARD, DO NOT SLICE THE SWEEP LOG BY SLUG, DO NOT TYPE A FULL
  SHA YOU HAVE NOT RESOLVED, DO NOT LEAVE A FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT
  CORRECTS, DO NOT MEASURE A TEXT LENGTH WITH `wc -w`, DO NOT LET A `manual:` ROW BE SCORED BY
  WHOEVER DID THE WORK, DO NOT RUN `board.py` BY HAND, DO NOT HAND-EDIT A `P1x`/`P3x`/`P5x` ROW, DO
  NOT TRUST A GREEN CLONE, DO NOT EDIT `src/`, DO NOT `--no-verify` PAST `roster-brake`, DO NOT
  RE-RUN A LEG THAT HAS RUN, DO NOT RE-APPLY A SPENT REMEDY, DO NOT READ "THE SYSTEM FAILS" AS "THE
  PAPERS ARE WRONG", DO NOT SKIP A LEG BECAUSE THE VERDICT CANNOT IMPROVE, DO NOT QUOTE A SENTENCE
  INTO A FINDING WITHOUT ITS TRAILING SCOPE CLAUSE, DO NOT TREAT TWO AGREEING INDEPENDENT BUILDS AS
  A CHECK, DO NOT CONCLUDE "NO PAPER CONTAINS X" FROM A WORD COUNT, DO NOT READ A SECTION'S
  PARAGRAPHS AS SEALED CELLS, DO NOT REPAIR TWO SENTENCES TOGETHER BECAUSE THEY LOOK ALIKE, DO NOT
  STOP AT ONE ROUND OF REFUTATION.
- **NEW · DO NOT ADD AN EXCLUSION TO A FIXED CHECK BECAUSE THE ANSWER CAME BACK WRONG.** `E4`'s
  exclusion list is exactly two items. A third — *"and not about accounting recognition practice"* —
  would have zeroed the count, and `-60` could have written it in one clause and nobody would have
  noticed. **Adding an exclusion after seeing the result is the mirror image of adding an observable
  to a leg's own failure criterion**, and the same ruling forbids both.
- **NEW · DO NOT CITE THIS PASS'S OWN REPAIRS AS CORPUS EVIDENCE.** `-60` nearly published Paper IV
  §9.2 as independent corroboration; it is `-55`'s repair, made in the commit after the registration
  and expressly excluded from `E6`'s run. **Before citing a manuscript sentence as pre-existing
  content, diff it against the `.bak` chain.** `ls -la` on the paper's directory gives you the
  chronology in one call.
- **NEW · DO NOT COUNT A REPOINTING TWICE.** Paper IV §9.3 says it contributes no computation, and
  its restatements of Paper III's results carry `(Paper III §5.4)` in their own text. **One claim
  seen twice is one claim.**
- **NEW · DO NOT INFLATE A DEFECT TALLY.** `-60`'s own refuter proposed a ninth registration defect
  and `-60` rejected it on the record. **A tally that accepts every candidate is worth nothing**,
  and "0-for-N" is only load-bearing while N is earned.
- **NEW · DO NOT CARRY A TEED-UP ITEM A FOURTH TIME WITHOUT RUNNING IT ONCE.** §0.
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe with `while pgrep`. **Do not edit shared infra a sibling is mid-edit on.**

---
## 6 · TRANSPORT — darlish, zero-bridge (worked first try, `-06` → `-60`)
Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. **Never restart the app to fix darlish.** `darlish-check` is not in
the cloud kit; do not chase its 127.

### ⚠ THE ONE THAT BIT `-60`, AND IT IS ON THE SHELF SIX TIMES ALREADY
**A multi-line commit message inside `dx '...'` is a trap that FAILS PARTIALLY.** `-60` used
`git commit -F - <<EOF` and got a commit whose message was truncated at the first apostrophe
(*"the corpus's"* closed the outer quote), while the remainder leaked into the shell as syntax
errors — **and the commit itself succeeded**, so the damage looked like a content problem. There are
**six** quarantined lessons saying exactly this and `-60` read none of them until afterwards.
**So here is the recipe instead of the warning. Copy it:**
```
# LOCAL: write the message to a file, then
/tmp/dx --put '/tmp/<sess>-commitmsg.txt' < COMMITMSG.txt
/tmp/dx 'cd ~/repos/wealth-tensor && git commit -F /tmp/<sess>-commitmsg.txt'
```
**And if you have already made the truncated commit:** `git commit --amend -F /tmp/<file>` fixes it,
then run `git commit --amend --no-edit` **without** `--no-verify` so the hooks re-run on the same
tree and no bypass stands in the record. `-60` did exactly that; the amend is `76b39a5`.

### ⚠ STAGE THE DOCS AS ONE TARBALL — much cheaper than `-59`'s three files
```
/tmp/dx 'cd ~/repos/wealth-tensor && tar czf /tmp/wt-docs.tgz docs'
/tmp/dx --get /tmp/wt-docs.tgz /home/claude/wt/wt-docs.tgz
```
One `--get` brings the whole `docs/` tree (~4.4 MB gzipped) into the cloud, including **every
`.bak`** — which is what let `-60` settle the Paper IV provenance question and the §6.1 staleness
question with `md5sum` instead of argument. **The `.bak` files are the project's version control
for prose and nobody has been using them.** `papers/` is inside `docs/`; do not name it separately
(it is not a top-level directory and `tar` will error).

- ⚠ **`dx` RUNS AS `root` IN THE CLOUD CONTAINER, SO `~` IS `/root`.** `--get` into an absolute path
  under `/home/claude` or the `Read` tool cannot see the file. `--get` needs the FULL path; a
  leading `~` expands in the CLOUD and fails. `--put` accepts `~`.
- ⚠ **`roster join --who <you>` AT STUDENT-IN, BEFORE `roster claim`.** `dx` resolves you as
  `cloud-<random>`; `join` **absorbs** those rows. `roster leave --who <you>` ONCE at wrap.
- ⚠ **`roster claim` TAKES BOTH `--who` AND `--resource`** — not `--repo`, and `--who` is **not**
  optional even after `join`. `-60` lost a call to that. **The `post-commit` hook claims the repo
  for you anyway**, using your commit subject as the task, so an explicit `claim` is usually
  redundant.
- ⚠ **`lessons.py use` IS `use <id> --task <tag>`** — id positional, task a NAMED flag. `-60` lost a
  call to that too. `record-outcome <tag> pass` is positional in both.
- ⚠ **`ROSTER_BRAKE_ACK=<staged count>` IS THE HONEST EXIT** when your staged set covers the whole
  dirty tree and **you verified the tree was EMPTY at your student-in.** Reason it in the commit
  message. `-60` did not need it: both repos were clean at student-in and stayed that way.
- ⚠ **A ROSTER CLAIM CAN BE A GHOST**: `git status` empty **and** `HEAD` is the claimer's own wrap
  commit **and** the roster task string is its handoff line. Two of three is not the test.
- ⚠ **A `STALE` CLAIM IS ADVISORY, NOT A LOCK.** `-60` took `claude-blackbook` while
  `big_worker-braatzArchive` held a 5 h-stale claim on it, found the tree clean, and says so here —
  which is the whole of the protocol.
- ⚠ **`| tail` MASKS `$?` ON EVERY `dx` CALL.**
- ⚠ **A RECURSIVE `grep` OVER `~/repos` FROM THE CLOUD WILL TIME OUT THE 5-MINUTE `Bash` LIMIT.**
  Name the directories, exclude `.venv`.
- ⚠ **`gate-selfcheck.sh` TAKES ~5–6 MINUTES AND A FOREGROUND `Bash` CALL DIES AT 8m20s.** Detach:
  `nohup env GATE_ROSTER_WHO=big-<sess> bash -c "$HOME/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1" &`
  then `sleep 300; grep -E "GATE SELF-CHECK|^  FAIL" /tmp/gate.log`. **COMMIT EVERYTHING FIRST** and
  **re-stamp the charter immediately before it.**
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started ·
  `5` crossed but mismatched.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
**SUITE:** 1074 collected, 1074 passed, zero skips — darwin ~67 s, cloud ~180 s. **`-60` did not run
it** (no code touched, docs only) and says so rather than quoting `-59`'s number as its own.
`check_abstract_size.py` **is silent on failure — use `--print`, AND PASS THE PAPER PATH: it defaults
to Paper III.** `defensive_count.py` takes a positional path and **only a DELTA means anything**.
**`redproof_apparatus.py`'s SKIPPED COUNT IS A SIGNAL: 2 is the baseline.**

---
## 0' · THE TELL, NOW IN A HUNDRED AND TWO SHAPES
`-28` through `-59`'s tells all stand. `-60` adds three:

- **AN AUDIT LEG'S EXPECTED ANSWER IS AN INSTRUMENT READING TAKEN BEFORE THE INSTRUMENT WAS BUILT.**
  `E4` was classified AUDIT *"because the designer expects the count to be zero"* — and the designer
  had Paper III §9's ninth limitation open while writing, quoted *"4.12× and 2.02×"* verbatim into
  `E6` in the same document, and still expected zero. The expectation was not lazy; **it was
  inherited from the corpus's own summary sentence, which had been stale for two weeks.** A designer
  who quotes a paper's self-assessment into a leg's premises **imports that paper's staleness into
  his own instrument** — and the only thing that catches it is running the leg he told you the
  answer to. *Classifying a leg AUDIT protects the run from reporting a discovery. It does not
  protect the designer from being wrong.*
- **A REFUTER'S SCAFFOLDING IS MORE DANGEROUS THAN A REFUTER'S CONCLUSION.** Round one's job is your
  finding; the provenance, precedents, tallies and clause readings it drags in to do that job arrive
  wearing three refuters' authority and were produced *in passing*. **They are as publishable-looking
  as the survivor and likelier to be wrong.** Round two has two targets, not one: the survivor, and
  the scaffolding. Aiming at both cost `-60` three of its own published grounds and saved it a ninth
  defect it had not earned.
- **A LOCATED FIX IS NOT A VERIFIED FIX, AND THE LINE NUMBER IS WHY.** Three handoffs carried
  *"`record-outcome` never reaches `_git_commit_push`"*, the third with a file and a line. **The
  citation is exactly what stopped anybody opening the file.** A claim that names `foo.py:1012`
  borrows the authority of a measurement without having done one. **Run it once.**

---
## 7 · ORIENT-THEN-GO
Nothing to preserve, nothing to tiptoe past. Emit one line — `Oriented: <state> · at-bat: <X> ·
opening with <first action>.` — and start building. Don't wait for a go. Do not open by asking Jason
anything **except** whether he has ticked `DECISION-001`, and check the file before you ask.
**If you take neither `E6` nor `P11g`, §3's forcing line wants one sentence from you at the top of
your handoff.**

**Coffee status:** ☕ TWENTY-SIX SESSIONS. `-56` found the fact that killed `E1` four days stale in a
dossier. `-57` found the sentence that killed `E3` four words long in an appendix. `-58` built a
finding and watched a refuter take it apart. `-59` did that twice in one afternoon. **`-60` was
handed the cheapest leg on the board, told the answer in advance, and found the answer was wrong —
because the sentence the designer trusted had been stale since the fifth of August and nobody had
diffed it against a `.bak` sitting in the same directory.** The corpus has five confirmed claims
about the world and every one of them is a claim against itself, which is either the most honest
thing in the repository or the funniest, and after twenty-six sessions those are the same joke.
**Five legs down, one to go, and the pass-level document that nobody has written is now exactly one
leg away.** 🥎
