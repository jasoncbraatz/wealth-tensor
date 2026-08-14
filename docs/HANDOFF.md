---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-14
session: wealthTensor-36
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale. `ADVISORY: docs-only
   drift` exits 0 and is NOT a defect. **Read the exit code.**
3. **`docs/preregistration/REG-010-p3-half-integer-banding.md`** — `-36`'s registration. **§1 is the
   population ruling and §3 is the two-branch ruling. Read both before touching anything REG-010
   named**, and read §3 before reading any number REG-010 produced.
4. `docs/preregistration/CONSTRUCTION-REG-010-edge-convention.md` — `-36`'s construction: C3 (the
   heap is *relocated*, not removed) and C5 (the band the shift creates) are the two that a later
   session will be tempted to walk past.
5. `docs/preregistration/RESULT-REG-010-half-integer-banding.md` — the run. **§3 first** (the reading,
   and why the flattering number is not good news), then **§4** (the finding).
6. **`docs/preregistration/RESULT-TERM-002.md`** — `-35`'s repair, and the one place the
   **two-numeral ruling** is registered. Read §2 before touching §8, §8.1 or §A.2.4.
7. `docs/preregistration/RESULT-PIN-001.md` — `-34`'s repair: §11's code-state pin, and the first
   costume of the §1.3 shape that was **true when it was written**.
8. `docs/preregistration/RESULT-SCOPE-001.md` — `-33`'s repair: §10's restriction and §5's selection,
   read in the same sitting.
9. `docs/preregistration/RESULT-REG-009-band-count-filled.md` — `-32`'s run. §4 first, then §3, then §6.
10. `docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md` — the rules `-32` fixed **in their
    own commit, before any count existed**. **R5 is load-bearing and `-36` nearly had it spent for it.**
11. `docs/preregistration/RESULT-REG-009-band-count.md` — `-31`'s two-cycle run. Its two errata stay errata.
12. `docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.**
    §§0–5 are Part I, §§6–12 Part II. **The numbering is 6–12 and not 2–8 by ruling.**

> **`-36` in one line: THE HANDOFF'S AT-BAT NAMED TWO DIFFERENT POPULATIONS, AND THE CORRECTED
> VERSION THEN RETURNED THE FLATTERING NUMBER THAT ONLY A PRE-COMMITTED READING COULD SURVIVE.**
> Item 1 cited `RESULT-REG-009` §4's tee-up (Ψ_band, **683 disclosed pairs**, two SHA-pinned files)
> and in the same breath directed the run at *"the FILLED population — 133, not 110"* with
> `chronological()` named (151 property **events**, nine cycles, a different instrument, one tag not
> two, a threshold question not a difference question). Re-edging *that* one would also have spent
> `CONSTRUCTION-REG-009-coverage-fill` **R5** — *no band edge is re-chosen in response to the number*
> — because the band count's whole content is a threshold reading. Built on the right population:
> registered alone at `f61f75a`, construction alone at `8d1245b`, performed at `0428422`,
> **|Ψ_band′ − Ψ| = 0.0050 against P3's five points, where D3's banding gives 0.0650.** That is
> Branch B, written down in the registration before the instrument existed, and it says the number is
> the size of the problem rather than a rescue. Then BUG SPRAY at `9530a5c`.

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-36`.** If it does not come up, the first move is
`dsh-fire` + `dwait`, not diagnosis. The MCP bridge dropped and reconnected mid-session again in
`-36`; nothing paused, because darlish is not on it.

**`dx --get` IS TEXT-ONLY.** Base64 binaries and `shasum` both ends — dx prints the on-wire byte
count, not the file size, so its own success line cannot certify a transfer (card `1217488245131362`).
**The minute-two shape, run again in `-36`: `tar czf` only `docs scripts tests src` on darwin, ONE
`--get`, `shasum` both ends, extract.** `-36` additionally pulled **`data/`** the same way (4.7 MB
tarball, 6.2 MB base64, one round trip) and it paid for itself immediately: the whole REG-010
instrument, the suite, and **five of the eight mutation proofs** ran against the cloud copy first.
**The artifact then came out byte-identical on both machines — sha256 `5e24df40`, two interpreters,
two numpy builds, bootstrap intervals included.** Cost: nothing. Do that.

`PYTHONPATH=<root>/src` is needed for the suite in the cloud; darwin's `.venv` has the package
installed. Cloud suite is 787 passed / 4 skipped in ~226 s; darwin is **805 passed in ~59 s** (the
four `test_registrations_precede_their_instruments` tests skip outside a git work tree, by design).

## 0 · THE TELL, NOW IN ELEVEN SHAPES — and `-36`'s is about the number you WANT

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL THAT HAS GONE QUIET (`-32`). `-33` added two about instruments that
agree with themselves. `-34` added the one that finds defects nobody introduced. `-35` added the one
that finds defects you are about to introduce while holding a card that says you are done thinking.
`-36` adds two:

- **PRE-COMMIT THE INTERPRETATION OF THE *FAVOURABLE* OUTCOME, NOT JUST THE UNFAVOURABLE ONE.**
  Registrations reflexively fix what a failure means, because failure is what an author fears. The
  outcome that corrupts a programme is the flattering one, **because nothing downstream objects to
  it.** Live fire: REG-010 re-ran a control that had FAILED at 0.0650 under a banding the failure's
  own write-up teed up, and got **0.0050** — comfortably inside the five-point tolerance. The
  sentence *"the failure was an artefact of the translation"* was available, true-sounding, and
  would have passed **the registration, the commit-order proof, four guards, twenty-five severity
  checks, G-COACH-3 and all 805 tests.** The only thing between the estate and it was §3 of the
  registration, written before the instrument existed, saying in the branch's own words that landing
  *inside* the tolerance is the **worse** result. **When a robustness row is teed up BY a failure,
  the registration must say what a PASS is allowed to mean before the row is run, or the row is a
  rescue with paperwork.** Banked: `2026-08-14-pre-commit-interpretation-favourable-outcome-unfavourable`.
- **A HANDOFF ITEM THAT NAMES BOTH A SOURCE DOCUMENT AND A POPULATION IS TWO CLAIMS, AND THE
  CITATION BEING RIGHT IS NO EVIDENCE THE POPULATION IS.** Resolve the population from the **cited
  document's own instrument**, never from the sentence that cites it. **The tell: the item's two
  halves can be satisfied by two different files and no single instrument can satisfy both.** Root
  cause is diagnosable and will recur — `-32` through `-35` all lived downstream of the coverage
  fill, so "the filled 133" and "a tie reachable at a new cardinality" were the live facts, and a
  tee-up from a *different* file (`RESULT-REG-009.md`, written by `-30`) got pulled into that frame
  on the way past. Companion to `-35`'s one-number-in-N-places rule: same disease, one level up,
  where the two places are a citation and a population rather than two numerals. Banked:
  `2026-08-14-handoff-item-names-both-source-document`.

**`-35`'s and `-34`'s shapes are unchanged and still sharp.** A pre-written repair is an unverified
claim whose author had less context than you. A claim whose truth depends on something that can
change without the claim changing will eventually be false and nothing will notice; **the repair is
never a fresher number.**

**AND: A FORBIDDEN-PHRASE GUARD OVER A DOCUMENT MUST SCAN ITS ASSERTIONS, NOT ITS QUOTATIONS** —
because the best documents *quote* the sentence they exist to refuse. `-36`'s rescue scanner went red
on `RESULT-REG-010` §3's own paragraph naming and rejecting the flattering claim. Both naive fixes
are wrong: deleting the quotation removes the document's strongest passage, deleting the phrase
removes the guard. Strip blockquotes and quoted spans, then **prove both branches** — an asserted
rescue must go red and a quoted-and-refused one must stay green (`test_the_rescue_scan_still_bites`),
or the stripper has swallowed the claims with the quotes and nobody can tell. Same shape as a
source-text guard firing on its own witness, one level up: **the guard needs a way to tell VOICE
apart, not just text.**

**Witness contract, unchanged:** `severity.check`'s witness must return **FALSY**, and a witness that
could be true in a legitimate world dies as VACUOUS. **A source-text guard fires on its own witness**
— compose the witness world from fragments (`"i" + "nt(v " + "// w)"`).

**EXPOSE BUILDERS, NOT FINISHED STRINGS** (`-35`) generalised in `-36` to **rules, not just strings**:
REG-010's two bandings are one-line reflections of D3's **lifted** midpoint —
`shifted(v,w) = mid(v + w/2, w) - w/2` and `mirror(v,w) = -shifted(-v,w)` — so nothing about a bin is
typed anywhere and a change to D3 propagates into REG-010 or aborts both. **A derived rule cannot
drift from its parent; a retyped one always eventually does.**

---

## 1 · WHAT HAPPENED

**`f61f75a` — the registration, alone.** No instrument on disk. It pins two things a later session
cannot re-choose: the **population** (§1) and **both branches of the verdict** (§3), the flattering
one in its own words. It also declares the manuscript consequence in advance — **none**, because
paper III carries no Ψ_band, no P3 and no granularity claim, checked *before* the file was written
rather than after a number existed.

**`8d1245b` — the construction, alone.** Still no instrument. C1 (the shift is derived, not retyped),
C2 (the tie-break is **inherited** from D3's half-openness, not chosen — and it decides **715
lives**), C3 (**the heap is relocated, not removed**: 55.71 % integers → 17.45 % half-integers, and
the *direction* of the expected difference predicted in advance so it cannot be reported as a
discovery later), C4 (the mirror, priced, never chosen), C5 (**the band the shift creates**).

**`0428422` — REG-010 performed.** 25 severe checks, 0 definitional, 0 vacuous.

| reading | \|Ψ_x − Ψ\| | inside P3's five points |
|---|---|---|
| D3's banding — P3's registered subject | **0.0650** | **no — P3 FAILS** |
| half-integer edges, registered convention | **0.0050** | yes |
| half-integer edges, mirror | **0.0361** | yes |

**§4 is the finding, and it is not the 0.0050.** The registered convention and its mirror move
**every** life by exactly the same distance — checked pointwise over all 4098 lives, not on probe
points — and disagree on **exactly the 715 half-integer lives**. Identical displacement profiles:
mean 0.1838 y, max 0.5000 y, 740 fixed points, 626 moved. The only difference is which way the
half-integer heap goes (495 up / 131 down against 116 up / 510 down). **They give Ψ = 0.6536 and
Ψ = 0.6225 — 0.0311 of Ψ from the direction of a half-open interval, with distance held exactly
fixed, six times the whole shifted-versus-raw difference.** §4 of `RESULT-REG-009` was pointing at
half a mechanism: **the operator's magnitude is the visible half; its direction is the half that
moves the answer.**

**C5 discharged, and it was not decorative.** δ = 1/L, and the shift's leftmost band has centre **0**,
which the estimator cannot consume: `adm = (δ < α̂)` is silently **false** for an infinite δ. **7
lives collapse to zero under the registered convention and 9 under the mirror; D3's collapse produces
none.** Registered handling was *count them, ask whether any would have been admissible, and REFUSE
if any would* — never exclude, never widen a band. The guard passed with **sixteen real subjects**
rather than vacuously.

| | |
|---|---|
| **G-COACH-3 across the session** | **3 → 3 (+0)**, with **zero** files changed under `docs/papers/` |
| suite | **791 → 805**, green in 59 s |
| new guards | `tests/test_reg010_half_integer_banding.py` (11) · `tests/test_registrations_precede_their_instruments.py` (4) |
| mutations | **eight**, all red, all restored, zero residue |
| cards | State Machine `1217494028527267` **closed** with the performance · `1217494219393416` open |

**`9530a5c` — BUG SPRAY, its own commit, no claim added.**
`tests/test_registrations_precede_their_instruments.py`: the commit introducing a registration
document must introduce nothing under `scripts/` or `src/`. The rule was banked **twice**
(2026-08-05, 2026-08-10) and enforced nowhere. **It found two violations on its first run, and one
was new**: `REG-008` (`b02d02e`) has the commit subject *"registered alone"* and carried three
prototype probes under `scripts/prototypes/`, one named `reg008_probe_00_CONTAMINATED.py`, none of
which `REG-008-p3-entity-anchored-disclosure.md` mentions — **eight days after the lesson forbidding
it was banked.** `PRE-002` (`d655501`) was the already-known one. **History is not rewritten to make
a test green**: `KNOWN_VIOLATIONS` is a ledger on the `DEFENSIVE-BASELINE.json` pattern — *never X
SILENTLY* — asserted in **both** directions, so a new violation goes red for being absent and an
entry that stops being a violation also goes red.

**The eight mutations.** Five in the cloud copy (retyped bin index · altered Ψ numeral · a rescue
**asserted** outside a quotation · mirror collapsed onto the registered convention · mirror moving a
*different* distance); three commit-shaped ones in a **throwaway `git worktree`** (a registration
committed with an instrument · a ledger entry whose recorded files no longer match · a scan that
finds nothing, which must go red rather than pass on an empty set). Worktree removed,
`git worktree list` back to one, real tree never touched.

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-35`'s rulings stand verbatim: no third disclosure instrument; phrase set
  frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS AN UPPER BOUND — the *disclosed*
  δ**; **REG-009 IS CLOSED and its numbering is 6–12**; **§4's COVERAGE SILENCE STAYS RECORDED, NOT
  REPAIRED**; **§7.5's TWO ERRATA ARE RECORDED, NOT REPAIRED**; **DO NOT SPEND THE TIE-BREAK**; **DO
  NOT PROMOTE `R_MIN`**; **`data/reg-009-band-count.json` IS `-31`'s**;
  **`test_the_cycle_choice_now_decides_the_answer` IS A RESULT, NOT A DEFECT**; **§10 IS NOT TOUCHED
  BY SCOPE-001 AND THE STEELMAN LIVES IN §5**; **SCOPE-001, PIN-001 AND TERM-002 ARE CLOSED**; **§11
  PINS PER FILE**; **TERM-002's COUNT IS TWO NUMERALS, NOT ONE, AND §8's FOURTH ITEM STAYS**; **THE
  §1.3 GREP IS EXHAUSTED AS AN ENUMERATION.**
- **NEW · P3 FAILED AND REG-010 DID NOT RE-SCORE IT.** `RESULT-REG-009` §4 is not edited, no sentence
  anywhere is softened, and **REG-010's row does not enter any table that reports P3.** A control that
  failed on the banding it was registered against cannot be un-failed by a banding built after the
  failure was seen. **The 0.0050 is the size of the problem, not a rescue** — and if that reading ever
  looks over-strict, re-read the registration's §3 before re-reading the number.
- **NEW · REG-010's POPULATION IS Ψ's 683 DISCLOSED PAIRS, NOT THE BAND COUNT'S FILLED 133.** They
  are different instruments on different units answering different questions. **Do not merge them,
  and do not "fix" REG-010 to run on the 133.**
- **NEW · NEITHER BANDING IS THE OPERATOR-FREE ONE, AND NEITHER IS PROMOTED.** D3's stays primary
  because it is the one D3 priced and the one P3 was registered against; the mirror is never promoted
  under any outcome. **The pair of rows is the deliverable** — it brackets the operator's
  contribution, which a single row cannot supply.
- **NEW · THE BAND COUNT MAY NOT BE RE-EDGED AND ITS FLOOR RE-READ.**
  `CONSTRUCTION-REG-009-coverage-fill` R5 forbids it, and the band count's entire content is a
  threshold reading. The legitimate version of that question is carded at `1217494219393416` and must
  be a description of the heap that reads no threshold.

---

## 3 · THE AT-BAT, RANKED

1. **"disclosed rectangle" at paper III §4.4 and §5** — 86.1 % of the disclosure falls outside it, so
   the adjective is wrong at all four sites. Stanza pre-written; recover with
   `git show 958956a~1:docs/HANDOFF.md`. **SEVEN sessions old** and it is now the only paste left.
   **APPLY §0's `-35` BULLET TO THAT STANZA BEFORE YOU TOUCH AN ANCHOR** — read the replacement text
   in its own context first; that check cost five minutes in `-35` and saved the estate a false
   sentence. Budget those five minutes.
2. **`REG-008`'s undisclosed prototypes, now that a guard names them.** `b02d02e` carried three probes
   the registration does not mention, one of them named `CONTAMINATED`, and REG-008 §2.6's own
   feasibility-probe discussion is the natural home for a disclosure. **The repair is a paragraph in
   REG-008 naming the three files and what they were**, not a history rewrite and not a ledger
   deletion — the ledger entry stays either way, because the violation happened. Cheap, and it closes
   the loop the BUG SPRAY guard opened.
3. **Infra, all carded, all Claude-hands:** `@concierge_ingest` / `@concierge_router` carry the same
   Caddy ordering defect `@darlish` had (`1217488447555628`) · the live capability path is committed
   in cleartext to `n8n-stack` and the repo copy has drifted from live (`1217488117177482`) ·
   `dx --get`'s byte count **and its total failure on binary** (`1217488245131362`).
4. **AAR A2** — the four other `post-*` hooks in `darwin-mac-ops/hooks`; plus **A1's residual**
   (`1217468064910605`), now with **seven** consecutive sessions' evidence. `GATE_ROSTER_WHO` still
   does not reach the commit hook: every commit in `-36` logged **`cloud-IHUHXX6L`** while the roster
   row said `big-wealthTensor-36`. **`roster leave` BOTH rows at wrap** — `-36` did.
   **New datum on the self-as-rival bug:** `-35` saw `⚠️ ROSTER CONTENTION` on every commit; `-36` saw
   the brake print `[roster] wealth-tensor claimed for cloud-IHUHXX6L` instead — i.e. the hook
   **takes its own claim under the cloud identity**, which is the mechanism that then makes the
   human-named row look like a rival. Both symptoms have one cause and A1 is it.
5. **card-lint's structural false positive** (`1217483699706758`) · **the gate defect card**
   (`1217465036940491`).
6. **The band count's own half-integer question** (`1217494219393416`) — real, separate, and
   **cannot** be answered by re-reading the floor of 30. Read the card before starting it.
7. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
8. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**

---

## 4 · WHAT WOULD HAVE SAVED `-36` TIME

- **RESOLVE THE AT-BAT'S POPULATION FROM THE CITED DOCUMENT'S INSTRUMENT BEFORE WRITING A LINE.** It
  took ten minutes — open `reg009_ladder_inputs.load_population` (two SHA-pinned files, 683 pairs)
  and `reg009_band_count_filled.chronological` (nine cycles, events, one tag) and see that no single
  instrument can satisfy both halves of the instruction. Everything after that was clean. **This is
  the cheapest check in the session and it decided what the session was.**
- **THE CLOUD DRY RUN IS NOW LOAD-BEARING, NOT A LUXURY.** The instrument, the suite, the two new
  test files and **five of eight mutations** ran in `/tmp/wt` first; the first command that touched
  the real tree had already worked. Pull `data/` as well as `docs scripts tests src` — 4.7 MB, one
  `--get`, and it removes every remaining reason to iterate on darwin.
- **THE GUARDS I WROTE FAILED THEIR OWN STANDARDS TWICE, AND CATCHING THAT WAS FIVE MINUTES.** One
  check asserted a claim its condition did not test (a phantom tag by the estate's own definition,
  written by the session that knows the rule); one scanner could not tell an assertion from a
  quotation. **Re-read your own new checks against the severity doctrine before running them, not
  after** — both were caught by asking *what would this check let through?*
- **A COMMIT-SHAPED MUTATION BELONGS IN A THROWAWAY WORKTREE AND IT IS CHEAP.**
  `git worktree add --detach`, mutate, commit with `--no-verify`, assert red, `git worktree remove
  --force`, `git worktree prune`. Three mutations, zero risk to the real tree, one script.
- **`git commit -F <file>` WITH THE MESSAGE SHIPPED VIA `dx --put` AND `shasum`'d BOTH ENDS.** Never
  inline a multi-line string in `dx '...'`. Seven files crossed this session and every one matched.
- **THE ROSTER BRAKE'S `ROSTER_BRAKE_ACK=<n>` MUST EQUAL THE STAGED COUNT** — `-36`'s were 1, 1, 5, 1.
- **CHECK BEFORE YOU REPAIR.** `-36` nearly carded REG-008's probes as a violation without first
  grepping REG-008 for their names. It does not mention them — but the grep is what made the card
  true rather than plausible, and it cost one command.

---

## 5 · DEFINITION OF DONE (carry this forward)

REG-010 is **done**: registered alone before any number existed, the edge convention registered
separately and also alone, run on Ψ's own 683 pairs, a result document beside P3's failure rather
than instead of it, 25 severe checks with none vacuous, guarded by a test proved by five mutations,
G-COACH-3 non-increasing at (+0), suite green at 805, and the card carrying the find **and** the
performance. The BUG SPRAY guard is **done** and adds no claim.

**Every repair the `§1.3` grep produced is built** (SCOPE-001, PIN-001, TERM-002) and the grep is
closed. **Every row `RESULT-REG-009` §4 teed up is now run.**

The next unit of done is **item 1, the disclosed rectangle** — the last pre-written paste on the
pile, seven sessions old, and it gets §0's `-35` bullet applied to its stanza before a single anchor
is touched. A session that finishes it leaves **item 2** (REG-008's undisclosed prototypes, a
paragraph) as a clean small at-bat, and the estate is then out of pastes again.
