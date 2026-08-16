---
project: wealth-tensor
gh_sha: 1f4e98aa8d69e7f567eb134c0302d0db0cd8a3a7
updated: 2026-08-16
session: wealthTensor-54
gate_passed: true
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16, superseding the 'three preprints publicly posted' line carried since sessionZero): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF
`gh_sha` names the commit this file describes; **the only thing added after it is this file**,
so `--check` prints `ADVISORY: docs-only drift` and exits 0. Assert the exit code exactly
(`-39`); `| tail` masks it. That sentence is an **INVARIANT, not a description** — `-51` learned
that the hard way when a post-wrap ADR commit made it false while the gate stayed green, because
`--check` classifies by PATH and any docs-only drift is green. If a post-wrap commit lands,
repoint `gh_sha` and re-master this file.
`-54` landed `770f766` (Paper II's three prose gaps, alone, so that commit is green on its own),
`be0bdfc` (the instrument and everything with it), `206e6c6` (Jason's first DoD ruling — P8 to the
end) and `ef48c4a` (**his second, which replaced the Definition of Done itself**) and `1f4e98a`
(`P13` specified — the recipe rows), then re-mastered this file alone after them. **`-54` is also the worked example of
this paragraph's own instruction:** it wrapped at `be0bdfc`, Jason then ruled on the DoD, the
amendment touched `scripts/` and `tests/`, and `--check` went from `ADVISORY: docs-only drift` to
`BLOCKER: code advanced past the handoff` — exactly as designed. The repair is what you are reading:
repoint `gh_sha`, re-master, re-stamp the charter, re-walk the gate.
`gh_sha` is the full SHA from `git rev-parse`, not an expanded abbreviation.
---
## ORIENT — read these first, in this order
1. **`docs/CHECKLIST.md`** — the generated board. **Regenerate with `./scripts/regen-board.sh`,
   never `board.py` by hand — see `-53`'s note in that file.** Never hand-tick. As of `-54`:
   **59 criteria, 44 met, EIGHT lanes OPEN — every one of them `P13`'s.** First time in this
   project's history the board's open work is the thing Jason actually asked for. **It is still
   the LAST thing Claude builds. Read §3 before you take it.**
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
6. **`docs/adr/ADR-001-paper-decomposition.md`** — `-54`'s TWO addenda at the foot, and the
   second one is a **ruling from Jason that reorders the finish line — read it before you plan
   anything**. The title and The title and
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
**AND THEN JASON MOVED THE FINISH LINE**, mid-session: his own-hand pass (`P8`) is now ONE pass
over the whole corpus, taken LAST, after a new `P11` audits the three papers **as a system**.
Read §1's last block before you plan — **it changes which at-bat is on the critical path.**
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

### The DoD amendment — Jason's ruling, taken mid-session
**In his words:** *"I'm going to do the pending human step as the very last step (after the entire
corpus gets audited as a whole)… in fact since I'll be re-writing this doc with my own hand, I'll
probably do it at that step."*

`P8` was *"Jason's own-hand pass over each converged paper"* — a gate three times over, between
each paper's convergence and the batch declaration. It is now **one pass over the whole corpus,
taken last**, with two rows ahead of it:

| row | | |
|---|---|---|
| **`P11`** | the corpus audited **as a system** | ADR-001 addendum 6's end-to-end test — *what would it mean for the three papers to fail as a system rather than one of them failing* — designed, written down, and run. **Unclaimed since 2026-08-11 and now load-bearing**, because `P8` waits on it |
| **`P12`** | the arXiv endorsement path | PREPRINT-CHECKLIST §C. **The only other human-blocking item on the board, and it was invisible until `P8`'s move exposed it.** arXiv requires an endorsement before a first submission to a category and an unaffiliated first-timer must find a personal endorser; the lead time is social, not computational. SSRN needs none, which is why the batch order already puts II first |

**IT IS NOT A REORDERING, AND READING IT AS ONE IS THE TRAP.** Moving a human gate to the end
changes what *terminal* means upstream of it. If Jason re-writes prose at `P8`, **no session may
treat any paper's prose as final before `P8` closes.** The concrete case was already on the board:
`P1m`/`P3m`/`P5m` said the submission-time SHA *"closes at posting, which is P9's moment."* **A SHA
pinned at `P9` is stale by construction now** — the prose changes after it. All three notes are
repointed at `P8`. That consequence is not *in* the ruling; it *follows* from it, and a session
that had only reordered the rows would have left three pins aimed at a moment that no longer
exists. **`P9` is now the handoff INTO `P8`**, not the end of the line.

**TWO BUGS, FOUND BY MAKING THE CHANGE — both in code `-54` had written an hour earlier, and both
the same defect.** `gen_apparatus_rows.py` held `CORPUS` as a hardcoded tuple `("P1".."P10")` and
rewrites the whole file, so the next regeneration would have **deleted `P11` and `P12` silently**.
`test_apparatus_rows_are_falsifiable.py` split row ids with `f[0][:2]`, so `"P11"` read as family
`"P1"` — harmless by luck, and the first row numbered `P30` would have invented a `"P3"` sub-row
out of nothing. **A prefix taken by POSITION is an assumption about how many digits the world will
ever have; an allowlist that ENUMERATES instances is a census that stops counting.** Both are
shapes now (`^P[0-9]+$`, `P[0-9][a-z]`).

**Row ids are stable identifiers and are NEVER renumbered** — handoffs, addenda and lessons cite
them by name — so `P11`/`P12` sit between `P7` and `P8` in **file order, which is dependency
order**. Do not tidy them into numeric order.

| | |
|---|---|
| board | **50 → 52 criteria, 41 met** · the two new lines are both `PENDING-HUMAN` and both are real work, not ceremony |
| suite | **1063 passed**, zero skips, unchanged by the amendment |
| red-proof | 34 mutations, 0 survivors, re-run after the amendment |

### THE DEFINITION OF DONE CHANGED — read this before you plan anything
**In his words:** *"The definition of done is when the wealth tensor paper is done with it's
coaching and editing and python scripts and you make me a pretty cool looking deliverable at the
end to visualize it — then it's cleared for liftoff. The other things I mentioned aren't part of
this project (Jasonizing, perhaps some random questions here and there but that'll be in an ad-hoc
prompts)."*

**`Three preprints publicly posted` was this project's stated DoD for fifty-four sessions and was
never Jason's finish line.** Posting is two projects downstream: Voice Box Jasonizing (the Voice
Box is not trained yet — that happens *after* this project), then his own-hand rewrite for cadence,
telos and ethos, and only then the endorsement ask. **The finished document is the vehicle for that
ask** — he will not approach his old professors without a proof in hand — which is exactly why the
endorsement cannot come earlier. **That is a sequence, not a blocker.**

| | |
|---|---|
| **`P13` NEW** | **the deliverable — the only OPEN lane on the board.** One well-designed, self-contained artefact that *visualises* the corpus. Split so the machine checks what a machine can (it exists, no remote script or stylesheet) and **Jason judges whether it is any good** |
| **`P12` GONE** | the arXiv endorsement row, added by `-54` **one message earlier**. A correct observation filed against the wrong project. Deleted, not rescoped |
| **`P9`** | *"never ask Jason to trigger a SUBMISSION"* had no submission to name. It is the single handoff into `P8` |
| **`P8`** | the **END of the project**, not a step in it |
| **`P1m`/`P3m`/`P5m`** | pinned a *"submission-time head-of-repository SHA"* — **UNREACHABLE here, which is worse than failing**, because an unreachable row reads exactly like a deferred one and nothing would ever have flagged it. Rescoped to the in-scope leg: every 7-hex pin in a data-and-code section must **resolve** to a commit, and the section may not defer its pin to posting. **Three permanent ambers → three greens**, each red-proofed |

**And the rescope caught a live defect in a deliverable.** Paper IV read *"Commit for the results
reported here: **to be pinned at posting**"* — a forward promise to a date that had just stopped
existing. **It walked straight past the no-live-placeholders guard**, because that guard knows the
phrase *"to be migrated"* (the one instance WT-047 found) and not its sibling. Paper IV now pins
`5efe626`. Also swept: the board preamble still named the old destination, and `handoff_gate.py`'s
own docstring used *"three preprints publicly posted"* as its worked example of a good DoD.

| | |
|---|---|
| board | **52 criteria, 44 met, ONE OPEN lane** |
| suite | **1063 passed**, zero skips · defensive counts unchanged after the Paper IV edit |
| red-proof | **37 mutations, 0 survivors** (the three new `m` rows included) |

### `P13` — what the deliverable actually is, and why the recipe is the load-bearing half
**In his words:** *"a paint-by-numbers as to how the tex is formatted, font, line, etc all has to
be Claude-Opus-ready to just walk through like a checklist so there are no surprises it has to
debug — the worst that could happen … would be it couldn't find the same font for example or it
didn't have the spacing recipe we use in this project. It could get close perhaps but then I have
to go back a re-tweak everything … so that after this project is done, **I only have to do the
layout and viz analysis once on it**."*

**THE CATASTROPHE HAS A MECHANISM. TeX does not fail on a missing font — it SUBSTITUTES.** The
build succeeds, the metrics change by a hair, the reflow moves, a page boundary shifts, and the
document is *close*. **Close is the failure**, because it spends Jason's layout analysis a second
time. `P13a`–`P13g` are therefore not about producing a PDF; they are about making a rebuild
**provably the same document**, and about **refusing loudly rather than approximating**.

| row | | |
|---|---|---|
| `P13a` | the PDF **stamps its source commit** | a point-in-time capture that cannot be confused with a later one |
| `P13b` | `RECIPE.md` is a **numbered checklist** | every font family/weight/size/leading · every margin, measure and vertical space · engine and every package **with its version** · figure placement · reference style — **as values, never as "match the existing look"** |
| `P13c` | **preflight that FAILS** | on a missing or substituted font, tool or version. No fallback, no nearest match. **Refusing to build is the feature** |
| `P13d` | fonts **vendored** or pinned by name+version+checksum | *"the same font"* has to be a fact on disk, not a hope about the next machine |
| `P13e` | **layout reproducible, proved not promised** | a rebuild must reproduce the committed page count and **per-page text hash**. A build that merely *looks* right cannot pass |
| `P13f` | every figure from a **committed script and committed numbers** | `FIGURES.tsv` maps figure → script → source. **No model-generated and no hand-drawn imagery** — charts in an economics paper have to be the data. `P6`'s rule pointed at the pictures |
| `P13g` | economics house convention (Chicago author-date) | **manual on purpose**: a reference-style linter passes documents that are technically Chicago and read wrong |

**`P13e` IS THE ROW TO DEFEND** if a later session wants to relax something. Every other row can be
argued down to taste. That one is the mechanical detector of a silent font substitution, and it is
the whole difference between *"we wrote down how it was made"* and *"we can prove the rebuild is
the same document."* This project has said the same thing about backups for fifty sessions:
**reversibility you never verified is not reversibility. A recipe nobody re-ran is not a recipe.**

**Scope note.** Jason editing the `.md` for language, marking where graphics go, and a session
reformatting to submission spec is *"its own, likely just one-off prompt of 'final paper
reformatting' or somesuch."* **Not wealth-tensor.** What wealth-tensor owes it is a recipe good
enough that the successor never re-derives a spacing value or hunts for a font.
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
  Five for five, first run.
- **NEW · `P8` IS ONE PASS, OVER THE WHOLE CORPUS, TAKEN LAST — JASON'S RULING, 2026-08-16.** It
  does not interleave and it is not per-paper. **Nothing that depends on final prose may be spent
  before it closes**, the submission-time SHA pins above all. `P9` declares the batch ready *for*
  that pass, exactly once, and stops.
- **NEW · `P7` DOES NOT CLOSE THE CORPUS.** Converging three papers individually is a different
  object from auditing the conjunction. That is why `P11` exists rather than being folded into
  `P7`, and folding it back in is how the corpus would ship without ever having been read whole.
- **NEW · DONE IS "CLEARED FOR LIFTOFF", NOT "POSTED" — JASON'S RULING, 2026-08-16.** Coaching
  and editing converged · the corpus audited whole · the scripts done · **one well-designed
  deliverable that visualises the work** · then he clears it and Claude is finished here.
  **Jasonizing, his own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects.**
  Ad-hoc questions to a session are fine and are not this project either.
- **NEW · `P13` IS LAST, NOT NEXT.** Eight OPEN lanes make it look like the at-bat. It is not.
  Building the pretty thing before the prose converges means building it twice, and Jason asked
  for it *"at the end"*. See §3.
- **NEW · `P13` IS A PDF *AND A RECIPE*, AND THE RECIPE IS THE DELIVERABLE THAT OUTLIVES THIS
  PROJECT.** Do not ship a beautiful PDF with an undocumented build. **A preflight that
  approximates instead of refusing is a bug, not a convenience**, and `P13e` — page count plus
  per-page text hash — is the row that proves the rebuild rather than promising it.
- **NEW · A CRITERION THAT CANNOT BE REACHED IS WORSE THAN ONE THAT FAILS.** `P1m`/`P3m`/`P5m` sat
  amber for weeks describing an event this project never reaches. **An unreachable row and a
  deferred row are indistinguishable on a board**, so nothing flags it. When a row has been amber
  a long time, ask what would have to happen for it to close — and whether that thing is in scope.
- **NEW · ROW IDS ARE NEVER RENUMBERED. FILE ORDER IS DEPENDENCY ORDER.** `P11`/`P12` between
  `P7` and `P8` is deliberate. Every handoff, addendum and lesson cites rows by name. Check where the edit landed before you touch the guard.
---
## 3 · THE AT-BAT for `-55` — **DESIGN `P11`'s END-TO-END TEST, BEFORE `P7` POLISHES THE PAPERS**
**Every mechanically checkable criterion in the estate is green and the board names no next piece.
That is a state to be careful with, not to celebrate.** Eleven lines remain, all `PENDING-HUMAN`,
which means *a human or a fresh-eyes pass judges them* — **not** that they are done. **The DoD is
three preprints POSTED. Nothing is posted.**

**FIRST, THE TRAP.** `P13` — the deliverable — is the only OPEN lane, so the board points at it
and it is by far the most fun job on the list. **It is the LAST thing Claude builds, not the next.**
Jason asked for it *"at the end"*, and a visualisation built before the prose converges is a
visualisation built twice — the second time after `P7` has changed the very sentences it renders.
Its OPEN status is a statement about the finish line, not about this week.

**Take `P11`'s DESIGN half — write the end-to-end test down, do not run it.** The reasoning is the
ruling's own:
- **`P8` now waits on `P11`, so the end-to-end test moved onto the critical path** after five
  sessions of sitting unclaimed. It is no longer the interesting optional thing; it is the gate.
- **And it has to be designed BEFORE `P7`, not after.** `P11`'s own note says designing the test
  after the results are known is not a severe test. The three results are already known — but the
  papers have not yet been polished by fresh-eyes passes, and **a system test written after `P7`
  will be a test the polished corpus passes.** The window where the design can still be honest is
  open right now and `P7` is what closes it.
- It is Jason's own methodological position, it has **no written answer anywhere in this
  repository**, and it is the biggest genuinely-unclaimed thing on the board.
- **Design only.** Write `docs/END-TO-END-001.md`: what a system-level failure would look like,
  what evidence would show it, and what the corpus would have to do about each outcome — committed
  *before* the answer is known, the same discipline every `REG-0xx` in this repo follows. Running
  it is `-56`'s job at the earliest, and running it in the same sitting that designed it satisfies
  neither half.

**Then `P7`, and Paper IV first.** Its §4 — the SMD-versus-scale resolution — remains the
highest-value target in the estate: load-bearing, drafted by one Claude in one pass, and ADR-001
predicted precisely that section is where the unforced error lives. `P7` needs **two consecutive
zero-finding passes**, so the earliest possible finish is two sessions away no matter what.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The honest alternatives:
- **`P7` on Paper IV now, and design `P11` after.** Defensible if you judge the severity argument
  above to be over-fine — say so explicitly and record the judgement, because it is the exact
  trade `P11`'s note was written to force into the open.
- **`P7` on Paper II** — also unreviewed, and it is the paper `-54` just edited in three places.
- **`P13`, the deliverable, deliberately early.** Defensible on ONE argument and only one: a
  rough pass reveals layout and fold behaviour that could inform what `P7` does to the prose,
  rather than the other way round. If you take it on that reasoning, **say so and build it
  throwaway** — do not commit it as the deliverable, because `P13` closing early is how the corpus
  ships a picture of a draft.
- **`P6`, the remaining two thirds.** `P3n` proved the shape; `P1n` and `P5n` are the same row
  repointed. Mechanical, valuable, last corpus-level row with a writable check.

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
- **JASON'S THREE `-51` SCOPING PROPOSALS ARE STILL UNRULED** — (a) audit the CLASS not the
  constraint, with one linter over claims naming a count, a filename or a coverage fact, each
  required to carry the command that regenerates it; (b) bound by value; (c) audit at the
  BOUNDARY. **`-54` is the eighth consecutive session (a) would have caught, and this time it
  half-landed on its own**: `P3n` IS proposal (a) applied to one claim, and it took four lines.
  That is the cheapest possible evidence the proposal is right. **A ruling would be worth more
  than another session of finding out.**
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
## 0 · THE TELL, NOW IN SEVENTY-EIGHT SHAPES
`-28` through `-53`'s tells all stand (ask the instrument-artefact question of numbers that look
GOOD, that SETTLE AN ARGUMENT, of a REGISTERED CONTROL THAT FAILS, OF THE DENOMINATOR; a guard
must scan assertions not quotations; a mutation that does not mutate reports your guard as weak;
pre-commit the FAVOURABLE outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT;
a correction that lives only in a handoff has not been made; the visible reds are the cheap half;
a rule can be false on the day it is written; a count is not a measurement until it agrees across
machines; a commissioned test that was never run is the most durable debt; a favourable result is
when the controls matter most; a count whose answer moves when the file is re-wrapped is measuring
the formatting; a fact can be recorded and still be absent at the point of use). `-54` adds seven:
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
- **MOVING A GATE CHANGES WHAT *TERMINAL* MEANS UPSTREAM OF IT, AND THAT CONSEQUENCE IS NEVER IN
  THE INSTRUCTION.** Jason moved his own-hand pass to the end of the project. The instruction was
  one sentence; the consequence was that three submission-time SHA pins, each saying it "closes at
  posting, which is P9's moment", were now aimed at a moment that no longer exists — because the
  prose changes after them. **A session that had only reordered the rows would have done exactly
  what was asked and left the corpus broken in a way nobody would find until posting day.** When a
  gate moves, walk everything that named the old ordering and ask what it was assuming; the
  instruction names the gate, and the damage is always somewhere else.
- **AND THE SAME TELL FIRED THREE TIMES IN TWO HOURS, WHICH IS THE REAL LESSON.** Ruling one
  moved `P8` to the end and stranded three SHA pins aimed at `P9`. Ruling two moved the finish line
  itself and stranded **the same three rows again**, plus an endorsement row a session had added an
  hour earlier, the board preamble, a docstring inside the gate, and a sentence inside a
  manuscript. **Each time the instruction named the gate and the damage was somewhere else.** After
  a scope or ordering change, `grep` the whole estate for the OLD terminal event by name — here it
  was the word *posting* — and read every hit. The instruction is one line; the blast radius is
  every place anyone ever wrote "when X happens".
- **A ROW THAT CANNOT BE REACHED IS INDISTINGUISHABLE FROM A ROW THAT IS MERELY DEFERRED, AND ONLY
  ONE OF THEM IS FINE.** `P1m`/`P3m`/`P5m` described an event outside the project's scope and sat
  amber, patiently, looking exactly like good practice. **Nothing on a board can flag this**,
  because "not done yet" and "will never be done" render identically. Ask of any long-amber row:
  *what exactly would have to happen for this to close, and is that thing in this project?*
- **A CRITERION THAT PASSES BECAUSE IT DOES NOT APPLY IS A BLANK LINE WEARING A TICK.** Paper II
  owes no pre-registration; PREPRINT-CHECKLIST §D says so in terms. The cheap move is to drop the
  row and the honest one is to make the row assert **the clause**, plus a tripwire for the day the
  premise moves. **Inapplicability is a fact about the world and facts about the world can change
  without anyone telling the board.**
---
## 7 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.
**Coffee status:** ☕ TWENTY SESSIONS, and this one ended three times. First: all three papers
measured against the same bar — which is exactly when the bar turned out to be measuring six things
that were never in it. Second: Jason moved his own-hand pass to the very end, which stranded three
SHA pins aimed at a moment that had just stopped existing. Third: he said what *done* actually
means, and it is **cleared for liftoff** — not the "three preprints publicly posted" this project
had been driving at since sessionZero, two whole projects too far down the road. **The corpus is
measured, the finish line is finally the real one, and there is exactly one thing left to build.**
Not yet, though. 🥎
