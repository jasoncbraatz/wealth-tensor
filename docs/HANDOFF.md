---
project: wealth-tensor
gh_sha: 349d29393b56614f380d26428baa4411fd097cf8
updated: 2026-08-14
session: wealthTensor-37
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
3. **`docs/preregistration/RESULT-TERM-001.md`** — `-37`'s registration and the one place the
   **five-site ruling** is recorded. §1 is the find (including why the inherited count was wrong)
   and §2 is the ruling and the scope exclusions. Read §2 before touching any *rectangle*.
4. `docs/preregistration/REG-010-p3-half-integer-banding.md` — `-36`'s registration. **§1 is the
   population ruling and §3 is the two-branch ruling. Read both before touching anything REG-010
   named**, and read §3 before reading any number REG-010 produced.
5. `docs/preregistration/CONSTRUCTION-REG-010-edge-convention.md` — C3 (the heap is *relocated*, not
   removed) and C5 (the band the shift creates) are the two a later session will walk past.
6. `docs/preregistration/RESULT-REG-010-half-integer-banding.md` — **§3 first** (why the flattering
   number is not good news), then **§4** (the finding).
7. **`docs/preregistration/RESULT-TERM-002.md`** — `-35`'s repair and the **two-numeral ruling**.
   Read §2 before touching §8, §8.1 or §A.2.4.
8. `docs/preregistration/RESULT-PIN-001.md` · `RESULT-SCOPE-001.md` — `-34`'s and `-33`'s repairs.
9. `docs/preregistration/RESULT-REG-009-band-count-filled.md` — `-32`'s run. §4, then §3, then §6.
10. `docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md` — **R5 is load-bearing.**
11. `docs/preregistration/RESULT-REG-009.md` — **§3's S = 0.1391 is now load-bearing in a test.**
    `test_term001_rectangle` recomputes 1 − S at run time and matches it against the share paper III
    prints. Restating S without restating §4.4's percentage goes red, by design.
12. `docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.**
    **The numbering is 6–12 and not 2–8 by ruling.** §12 is where the *asserted rectangle* term was
    registered, and `-37`'s §2.7-style disclosure pattern now applies to §2 of `REG-008`.

> **`-37` in one line: THE LAST PRE-WRITTEN PASTE NAMED FOUR SITES AND THERE WERE FIVE, AND THE COUNT
> WAS THE ONE CLAIM IN IT THAT NO ANCHOR COULD HAVE CONTRADICTED.** `patchkit` proves every anchor
> resolves **exactly once** and refuses to write otherwise — which reads as total coverage and is
> not: **it cannot know the list is short.** A four-anchor patch would have reported success, left
> the fifth site standing two hundred lines away, and kept all 805 tests green. The omitted site was
> inside **§4.4**, the section `REG-009` §12's repair was aimed at, where *"the entire **disclosed**
> rectangle lies outside the domain"* sat **five lines above** *"the **asserted** rectangle lies
> inside the domain after all"*: one object, two names, one paragraph, either side of the paper's
> sharpest reversal. Registered alone at `c0c0814`, performed at `f8e271d`, then BUG SPRAY at
> `9b3b013`. **The estate is now out of pre-written pastes: the next at-bat is CHOSEN, not pasted.**

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-37`.** If it does not come up, the first move is
`dsh-fire` + `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.

**`dx --get` IS TEXT-ONLY.** Base64 binaries and `shasum` both ends — dx prints the on-wire byte
count, not the file size, so its own success line cannot certify a transfer (card `1217488245131362`).
**The minute-two shape, run again in `-37`:** `tar czf` `docs scripts tests src` **and** `data`
separately on darwin, base64, ONE `--get` each, `shasum` both ends, extract. 1.9 MB + 4.7 MB out of
a 684 MB tree, and it paid for itself twice: the whole TERM-001 instrument, both mutation harnesses
(twelve mutations), and every suite run happened in the cloud copy first, so **the first command
that touched the real tree had already worked.** `-37` went further and did not cross the edited
manuscript at all — it crossed the *builder* and ran it on darwin, and **the artifact came out
byte-identical on both machines, sha256 `fc5595b7`, two interpreters.** Do that: it is a free
reproduction proof.

`PYTHONPATH=<root>/src` for the suite in the cloud. Cloud is **806 passed / 8 skipped in ~229 s**
and **every skip is `not a git work tree`** — that is the whole explanation, checked in `-37`, so
nobody needs to re-derive it. Darwin is `.venv/bin/python -m pytest`, **816 passed in ~56 s**.

## 0 · THE TELL, NOW IN TWELVE SHAPES — and `-37`'s is about a number nothing can contradict

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL THAT HAS GONE QUIET (`-32`). `-33` added two about instruments that
agree with themselves. `-34` added the one that finds defects nobody introduced. `-35` added the one
that finds defects you are about to introduce. `-36` added two: **pre-commit the interpretation of
the FAVOURABLE outcome**, and **a handoff item naming both a source document and a population is two
claims.** `-37` adds three:

- **A PRE-WRITTEN REPAIR'S SITE COUNT IS THE ONE PART NO ANCHOR CAN CONTRADICT.** Validate-then-write
  patching proves each anchor is *unambiguous*; nothing proves the list is *complete*, and the two
  feel identical in the output. **So resolve the site set yourself — one exhaustive grep, then read
  every hit in its own context, because the referent decides membership and only reading decides the
  referent.** And shape the guard against the failure: **assert an ABSENCE and a COUNT, never N
  presences** — absence is the only assertion a short list cannot satisfy, and a count bound to
  `len(EDITS)` is the only numeral that cannot drift. Companion to `-35`'s rule: `-35` covers whether
  each replacement is TRUE, this covers whether the LIST is COMPLETE, **and the second is invisible
  to every check the first passes.** Banked: `2026-08-14-pre-written-repair-s-site-count`.
- **BIND A TERMINOLOGY REPAIR TO THE MEASUREMENT THAT WARRANTS IT, NOT TO A SPELLING.** The guard
  everyone writes — assert the new word, assert the old one is gone — passes forever after the
  measurement that justified the rename has been removed or restated, leaving a word whose
  justification has quietly left the repository. `test_term001_rectangle` instead reads S out of
  `RESULT-REG-009` and recomputes 1 − S against the share paper III prints. **Whenever an edit's
  justification is a number living in another file, the guard must read THAT number, or you have
  guarded the conclusion and not the premise.** Banked:
  `2026-08-14-bind-terminology-repair-measurement-warrants-spelling`.
- **A MUTATION THAT DOES NOT ACTUALLY MUTATE REPORTS YOUR GUARD AS WEAK, AND THE FALSE ALARM IS
  INDISTINGUISHABLE FROM A REAL HOLE.** Live fire: proving a guard fails on an empty edit list, the
  drill rewrote `EDITS = [` to `EDITS = [] if False else [` — valid Python evaluating to the FULL
  list. The suite stayed green and the honest reading of that was *"the vacuity check does not
  bite"*, which was false. **A surviving mutation is TWO hypotheses and the cheap one is that the
  mutation is inert — eliminate it first by asserting the artefact actually changed.** The second
  harness this session does that in code. Banked:
  `2026-08-14-mutation-does-actually-mutate-reports-guard`.

**AND (BUG SPRAY): A LEDGER OF KNOWN VIOLATIONS THAT LIVES ONLY IN THE TEST SUITE IS NOT A
DISCLOSURE.** `KNOWN_VIOLATIONS` recorded both commit-order violations correctly, in both directions
— in `tests/`, while `REG-008` went on being subjected *"registered alone"* and `PRE-002`'s
AMENDMENTS said *"(none)"*. The repair is a **dated addendum at the scene, marked as written after
the fact**, plus a guard requiring every file the ledger records to be **named, by basename**, in
the document that shipped it — basename because *a path is a fact about the tree and a name is a
fact about the disclosure*, so a file that later moves cannot silently un-disclose itself. Banked:
`2026-08-14-ledger-known-violations-lives-only-test`.

**Everything `-33` through `-36` banked is unchanged and still sharp.** A guard must scan assertions,
not quotations. Expose builders, not finished strings — and now not finished RULES either. Commit-
shaped mutations go in a throwaway worktree. `severity.check`'s witness must return FALSY.

---

## 1 · WHAT HAPPENED

**`c0c0814` — TERM-001 registered, alone, pushed before the instrument existed.** Five sites, the
referent test recorded, and the scope exclusions stated as rules rather than conveniences.

**`f8e271d` — TERM-001 performed.** `scripts/wt101_edits_term001.py` builds **both** noun phrases
from one adjective pair, so neither is typed anywhere. `tests/test_term001_rectangle.py` asserts the
absence, the count, each repaired span's uniqueness, and the warrant. **Six mutations, all red:** the
term reappearing at one site; the site numeral and the section numeral each moved alone (both
directions of the count); the edit list emptied; S drifting; and the paper dropping the share that
warrants the word (both directions of the warrant). Artifact byte-identical on both machines.

**`9b3b013` — BUG SPRAY, its own commit, no claim added.** `REG-008` §2.7 and `PRE-002`'s AMENDMENTS
now name what their commits carried. **The tee-up was wrong in a useful direction:** `REG-008` §2
*does* discuss all three probes — by the provisional names `probe.py`, `probe2.py`, `probe3.py`,
which have never existed on disk. So the defect was disclosure-in-substance with broken provenance,
and the mapping was **read off the files** (`probe_01` and `probe_02` open *"REG-008 probe 2"* and
*"REG-008 probe 3"*; `probe_00` is the one counting by `r["arm"]`), not inferred from the order.
**And the find nobody teed up: `reg008_probe_00_CONTAMINATED.py`'s own docstring says it is clean** —
*"computes no statistic that any REG-008 prediction depends on"*, committed in the same commit as
§2.6, which rules that what it computed **is** the comparison and makes Λ_anchor permanently
exploratory. The file has not been modified since `b02d02e` and was **not** modified here: the
docstring is evidence of what was believed at the time, correcting it would edit the witness, and
the addendum is the correction. **`PRE-002` was worse** — it named neither of its two files, one of
them the instrument itself. Six more mutations, all red, each asserted to have actually changed the
file before its verdict was read.

| | |
|---|---|
| **G-COACH-3 across the session** | **3 → 3 (+0)**, against a pre-edit copy taken before the tree was dirtied (`bd4ae3be`, identical in cloud and on darwin) |
| suite | **805 → 816**, green in 56 s |
| new guards | `tests/test_term001_rectangle.py` (9) · two added to `test_registrations_precede_their_instruments.py` |
| mutations | **twelve**, all red, all restored, zero residue |
| lessons | **four** banked global; **three** quarantined leaves corroborated `pass` |
| cards | State Machine `1217496274465337` · `1217496491255205` · `1217496462088036` (all new) |

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-36`'s rulings stand verbatim: no third disclosure instrument; phrase set
  frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS AN UPPER BOUND — the *disclosed*
  δ**; **REG-009 IS CLOSED and its numbering is 6–12**; **§4's COVERAGE SILENCE STAYS RECORDED, NOT
  REPAIRED**; **§7.5's TWO ERRATA ARE RECORDED, NOT REPAIRED**; **DO NOT SPEND THE TIE-BREAK**; **DO
  NOT PROMOTE `R_MIN`**; **`data/reg-009-band-count.json` IS `-31`'s**;
  **`test_the_cycle_choice_now_decides_the_answer` IS A RESULT, NOT A DEFECT**; **§10 IS NOT TOUCHED
  BY SCOPE-001**; **SCOPE-001, PIN-001, TERM-002 ARE CLOSED**; **§11 PINS PER FILE**; **TERM-002's
  COUNT IS TWO NUMERALS AND §8's FOURTH ITEM STAYS**; **P3 FAILED AND REG-010 DID NOT RE-SCORE IT**;
  **REG-010's POPULATION IS Ψ's 683 DISCLOSED PAIRS, NOT THE FILLED 133**; **NEITHER BANDING IS
  PROMOTED — THE PAIR OF ROWS IS THE DELIVERABLE**; **THE BAND COUNT MAY NOT BE RE-EDGED AND ITS
  FLOOR RE-READ (R5).**
- **NEW · TERM-001 IS CLOSED AT FIVE SITES AND THE RECTANGLE IS *ASSERTED* IN THE MANUSCRIPT.** The
  eleven bare occurrences of the noun keep their wording — the defect was the adjective's claim, not
  the shape. **Do not "finish the job" in the records:** `RESULT-REG-004`, `RESULT-REG-003`,
  `RESULT-REG-002`, `RESULT-P0`, `REG-003`, `REG-004` and `SOURCE-001` said what they said when they
  said it. **And do not rename the instrument prose** — `wt088_disclosed_ladder.py` and four siblings
  print the phrase inside severity-check descriptions and run logs that other documents quote and
  pin; renaming there edits the witness to match the testimony. `RESULT-TERM-001` §2 is the
  disclosure of that inconsistency and is the honest form of it.
- **NEW · REG-008 §2's PROVISIONAL FILENAMES STAY.** §2 refers to `probe.py`, `probe2.py`,
  `probe3.py`; §2.7 maps them to the real paths. **Do not edit §2 to use the real names** — it is a
  record, the mapping is disclosed, and the addendum is dated and marked as after-the-fact precisely
  so nobody mistakes it for something registered in advance.
- **NEW · `reg008_probe_00_CONTAMINATED.py`'s DOCSTRING IS LEFT STANDING.** It contradicts §2.6 and
  that contradiction is the evidence. It is disclosed, not repaired. Do not "fix" the file.

---

## 3 · THE AT-BAT, RANKED — **and for the first time in eight sessions, none of these is a paste**

There is no pre-written stanza left. **Every item below needs a session to decide its own shape**,
which is a different kind of at-bat from the last eight and worth knowing before you start.

1. **The band count's own half-integer question** (`1217494219393416`) — the largest genuinely open
   *research* item. Real, separate, and **cannot** be answered by re-reading the floor of 30;
   `CONSTRUCTION-REG-009-coverage-fill` **R5 forbids re-edging in response to the number**. It must
   be a **description of the heap that reads no threshold**. **Read the card before starting**, and
   register the interpretation of the *favourable* outcome before running anything (`-36`'s rule).
2. **AAR A2 + A1's residual** (`1217468064910605`, new datum at `1217496462088036`) — **EIGHT**
   consecutive sessions. `-37` narrowed it: `GATE_ROSTER_WHO=big-wealthTensor-37` was exported
   **inside the same `dx` invocation as the `git commit`**, i.e. in the committing process's own
   environment, and the hook *still* logged `cloud-RRvNUwGw`. **So this is not a variable lost
   crossing the dx boundary — the hook is not reading it, or reads it before it is set.** Cheap next
   step: read the hook in `darwin-mac-ops/hooks` and check how it resolves identity. Eight sessions
   of re-observing is enough. Plus A2's four other `post-*` hooks.
3. **Infra, all carded, all Claude-hands:** `@concierge_ingest` / `@concierge_router` carry the same
   Caddy ordering defect `@darlish` had (`1217488447555628`) · the live capability path is committed
   in cleartext to `n8n-stack` and the repo copy has drifted from live (`1217488117177482`) ·
   `dx --get`'s byte count **and its total failure on binary** (`1217488245131362`).
4. **card-lint's structural false positive** (`1217483699706758`) · **the gate defect card**
   (`1217465036940491`).
5. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
6. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**
7. **Not mine, not touched:** handoff-lint warns `HANDOFF-acmeLedger-07.md:22` makes a verification
   claim with no vantage point. A sibling was live on it; don't clobber, but it is still open.

---

## 4 · WHAT WOULD HAVE SAVED `-37` TIME

- **RESOLVE THE SITE SET FROM THE DOCUMENT, NOT FROM THE ITEM THAT NAMES IT.** One `grep -o | wc -l`
  and five reads-in-context, before writing a line. It cost ten minutes and it **decided what the
  session was** — the inherited count was wrong and nothing downstream would have said so. This is
  the third session running whose first ten minutes were the whole game (`-35` truth, `-36`
  population, `-37` count).
- **CHECK THE ARITHMETIC IN YOUR OWN NEW PROSE BEFORE COMMITTING IT.** Three claims in the draft
  registration — a line offset, a paragraph boundary, and a count of bare nouns — were wrong, all
  three caught by one grep, all three fixed before the commit. **A registration is committed alone
  and pushed; there is no quiet second chance at its wording.**
- **CHECK BEFORE YOU REPAIR, AGAIN, AND IT CHANGED THE FINDING AGAIN.** The tee-up said `REG-008`
  mentions none of its three probes. It discusses all three, under names that never existed on disk
  — a different defect with a different repair, found by one grep. `-36` recorded this same rule
  after nearly carding a plausible claim; it has now paid twice.
- **A PRE-EDIT COPY BEFORE THE TREE IS DIRTIED, ON BOTH MACHINES.** `--against` has no second chance,
  and the two copies hashing identically (`bd4ae3be`) is what let the cloud dry-run stand in for the
  real one.
- **CROSS THE BUILDER, NOT THE ARTIFACT.** Running `wt101` on darwin instead of shipping the edited
  manuscript produced a byte-identical file for free — a reproduction proof at zero cost, and one
  fewer large file on the wire.
- **`git commit -F <file>` VIA `dx --put`, `shasum`'d BOTH ENDS.** Never inline a multi-line string
  in `dx '...'`. Nine files crossed this session, every one matched.
- **`ROSTER_BRAKE_ACK=<n>` MUST EQUAL THE STAGED COUNT** — `-37`'s were 1, 3, 3.
- **`roster leave` BOTH rows at wrap** — the human-named one and the `cloud-*` one the hook creates.

---

## 5 · DEFINITION OF DONE (carry this forward)

TERM-001 is **done**: registered alone before any anchor was touched, five sites each read in its own
context first, the count bound to one parse, the adjective bound to the measurement that warrants it,
six mutations, G-COACH-3 at (+0), suite green, and the card carrying the find **and** the
performance. The BUG SPRAY disclosure is **done** and adds no claim.

**The estate is out of pre-written pastes**, and every repair the `§1.3` grep produced is built
(SCOPE-001, PIN-001, TERM-002, TERM-001). **Every row `RESULT-REG-009` §4 teed up is run.**

The next unit of done is **item 1, the band count's half-integer question** — the last open research
item on paper III, and the first at-bat in eight sessions that has to be *designed* rather than
performed. Its definition of done is a **description of the heap that reads no threshold**, registered
with both branches — including what a favourable answer is allowed to mean — before the instrument
exists. A session that finishes it leaves the estate with only infra and process cards, which is the
cleanest the ledger has been.
