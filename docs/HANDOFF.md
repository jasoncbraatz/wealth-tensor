---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-14
session: wealthTensor-34
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
3. **`docs/preregistration/RESULT-PIN-001.md`** — `-34`'s repair: §11's code-state pin, and the
   first costume of the §1.3 shape that was **true when it was written**.
4. `docs/preregistration/RESULT-SCOPE-001.md` — `-33`'s repair: §10's restriction and §5's
   selection, read in the same sitting. §2 is the registered stanza; read it before touching either
   section.
5. `docs/preregistration/RESULT-REG-009-band-count-filled.md` — `-32`'s run. §4 first (the verdict
   and the parameter the fill created), then §3 (the fill's price), then §6 (the manuscript repair).
6. `docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md` — the rules `-32` fixed **in their
   own commit, before any count existed**. `git log --follow` on that file is the ordering proof.
7. `docs/preregistration/RESULT-REG-009-band-count.md` — `-31`'s two-cycle run, **unaltered except
   for the amendment at the end of §4**. Its two errata stay errata.
8. `docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.**
   §§0–5 are Part I, §§6–12 Part II. **The numbering is 6–12 and not 2–8 by ruling.**

> **`-34` in one line: THE §1.3 GREP IS FINISHED, it produced a sixth costume, and the sixth
> costume is a claim that was RIGHT when it was written.** All 26 remaining paragraphs read. §11
> told a replicator that `d655501` was "the last commit touching `src/`" and "is verifiable now";
> four commits had touched `src/` since, one of them adding twenty-one lines to `edgar.py`, a module
> §11's own **Modules** bullet names. Nineteen lines earlier the same section put the head of the
> repository at 103 tests; it carries 783. Registered alone at `214ff57`, performed at `a74a4ca`,
> guarded by a **git** check proved by **three** mutations, G-COACH-3 3 → 3 (+0), suite 777 → 783.

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
It came up first try in `-34` with no fallback needed. **If it does not, the first move is
`dsh-fire` + `dwait`, not diagnosis.** See `-33`'s §4, which still holds.

**`dx --get` IS TEXT-ONLY.** Pulling a `.tgz` wrote a 0-byte file and exited 2. Ship binaries
base64'd and `shasum` both ends — dx prints the on-wire byte count, not the file size, so its own
success line cannot certify a transfer (card `1217488245131362`, addendum filed). **The shape that
paid: `tar czf` only `docs scripts tests src` on darwin (1.8 MB of a 684 MB repo), base64, ONE
`--get`, extract, then grep and read in the cloud at zero round trips.** That is worth doing on
minute two of any session that will read this repository.

## 0 · THE TELL, NOW IN NINE SHAPES — and `-34`'s is the one that finds defects nobody introduced

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A CHOICE RULE'S
TIE-BREAK AT A NEW CARDINALITY and OF A TELL THAT HAS GONE QUIET (`-32`). `-33` added two about
instruments that agree with themselves. `-34` adds the one that is not about a mistake at all:

- **A CLAIM WHOSE TRUTH VALUE DEPENDS ON SOMETHING THAT CAN CHANGE WITHOUT THE CLAIM CHANGING WILL
  EVENTUALLY BE FALSE, AND NOTHING WILL NOTICE** — because the failure signature is that *nobody
  edited the sentence*, and every reflow guard, diff review and re-read in this repository is
  structurally blind to that. **The discriminator is not "is this quantity measured?" but "is this
  sentence's truth a function of the repository's PRESENT state?"** — a HEAD, a *last commit
  touching X*, a live count, a file list, an *as of today*. **The repair is never a fresher number**,
  because the fresh one rots identically: replace the moving target with a fixed one (per-file
  commit pins instead of a global "nothing has changed"), then pin *that* with a check that goes red
  on the next event that would invalidate it, so the doc and the state must move in the same commit.
- **The greppable corollary that makes the class findable: a load-bearing identifier occurring ONLY
  in prose and never in `scripts/`, `tests/` or `src/` is unguarded by construction.** `d655501`
  occurs six times in this repository and every one is prose. Every *other* load-bearing SHA in the
  estate — `93a159b`, `b02d02e`, `656b914`, `6a5094a`, `e216037` — sits in an instrument header
  where something would notice.

**Witness contract, unchanged:** `severity.check`'s witness must return **FALSY**, and a witness
that could be true in a legitimate world dies as VACUOUS rather than reporting. **A source-text
guard fires on its own witness** — sidestep it by IMPORTING the subject (`-32`, `-33`, and
`test_pin001_code_state.py`, which imports every SHA, the `TIER_TAGS` hash and both rotted phrases
from `scripts/wt099_edits_pin001.py`) rather than retyping it. **And prove a new guard by MUTATION**
— see §4 for the correction to that recipe that `-34` paid for.

---

## 1 · WHAT HAPPENED

**`214ff57` — the registration, alone.** `RESULT-PIN-001.md` and nothing else, before the edit
script existed on disk.

**`a74a4ca` — PIN-001 performed.** Five anchors, all inside §11, no heading or rule moved:

> - **Code state for the results reported here:** the per-file pins — `src/wealth_tensor/edgar.py`
>   at commit **d655501**, `src/wealth_tensor/lag.py` at **ad779eb** (its only commit) and
>   `src/wealth_tensor/lambda_sensitivity.py` at **b9089c7** — each verifiable with
>   `git log -1 --format=%h <sha> -- <path>`. `src/` as a whole has moved since, on companion-paper
>   modules and, at **93a159b**, on one addition to `edgar.py` that appends the REG-006-corrected
>   tier-0 tag list beside the registered one without editing it: the `TIER_TAGS` block that
>   selected §5's published sample is byte-identical at **d655501** and at the head of the repository.

and the test-suite bullet stops quoting a live count while keeping the three named additions, which
were always correctly described. **STEELMAN, not cut**: a global SHA is the wrong instrument for a
per-file guarantee, and the per-file version additionally *discloses* the REG-006 correction instead
of leaving it behind a stale pin.

| | |
|---|---|
| **G-COACH-3 across the edit** | **3 → 3 (+0)**, `--against` the pre-edit copy |
| suite | **777 → 783**, green in 56 s |
| new guard | `tests/test_pin001_code_state.py`, 6 tests, **proved by three mutations** |
| card | State Machine `1217490178082403` — the find, the repair, the performance |

**The guard is a git check, not a source-text guard with a git check bolted on**, because PIN-001's
signature is that nobody edited the sentence. `test_each_pinned_path_was_last_touched_by_the_sha_the_paper_discloses`
goes red on the **next** commit that touches a pinned module — the one moment §11 needs re-reading —
and `test_the_registered_tier_tags_block_is_byte_identical_at_both_shas` checks the **substance** of
the disclosure rather than only the SHA. It skips outside a git work tree, so a source tarball does
not read a lie about the paper.

**Three mutations, all reversible, committed first so git was the undo path.** (1) §11 reverted to
the rotted prose → 2 of 6 red. (2) **A real commit touching a pinned module**, made in a throwaway
`git worktree` on a scratch branch → the load-bearing test red, naming the offending SHA. That is
the 2026-08-13 event that went unnoticed for nine days, replayed. (3) The registered `TIER_TAGS`
list edited → the byte-identity test red. Worktree and branch removed; tree clean.

**`afbdd5c` — a docs-only pointer fix.** `REVIEW-004` sends a reader to paper III **§7** for the
"refused five times" list; it is in §8. Appended, not substituted, in the §1.3a manner.

**AND THE GREP THAT RAN FOR SIX SESSIONS IS FINISHED.** All 26 remaining paragraphs read, in the
instrument-vs-prose form. Two findings, one repaired here and one carded (§3 item 1).

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s, `-32`'s and `-33`'s rulings stand verbatim: no third disclosure instrument; phrase
  set frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS AN UPPER BOUND — the *disclosed*
  δ**; **REG-009 IS CLOSED and its numbering is 6–12**; **§4's COVERAGE SILENCE STAYS RECORDED, NOT
  REPAIRED**; **§7.5's TWO ERRATA ARE RECORDED, NOT REPAIRED**; **DO NOT SPEND THE TIE-BREAK**;
  **DO NOT PROMOTE `R_MIN`**; **`data/reg-009-band-count.json` IS `-31`'s**;
  **`test_the_cycle_choice_now_decides_the_answer` IS A RESULT, NOT A DEFECT**; **§10 IS NOT TOUCHED
  BY SCOPE-001 AND THE STEELMAN LIVES IN §5**; **SCOPE-001 IS CLOSED.**
- **NEW · PIN-001 IS CLOSED, AND §11 PINS PER FILE FROM NOW ON.** Do not restore a global "last
  commit touching `src/`" claim in any form, and do not "tidy" the per-file pins back into one SHA —
  that is the defect, re-introduced. When a pinned module legitimately moves, update `LATEST_TOUCH`
  in `scripts/wt099_edits_pin001.py` **and** the §11 sentence **in the same commit**, and say in the
  paper what the new commit changed. If it changed a published result, register that first.
- **NEW · THE §1.3 GREP IS EXHAUSTED AS AN ENUMERATION.** All 31 (in fact 34, see §4) paragraphs are
  read. A seventh run is a new instrument, not a resumption — and if one is built, it enumerates by
  **anchor phrase**, never by paragraph index. See §4.

---

## 3 · THE AT-BAT, RANKED

1. **`"refused five times"` — three sites, a list of four. Carded with the repair pre-written and
   the one ruling already made: `1217490492527699`.** paper III asserts the count at three places;
   §8's list enumerates four items, and the fourth is not a refusal at all — §8.1's φ move was made,
   relied on, and withdrawn. `REVIEW-004` recorded this on 2026-08-13 and nothing was built:
   **`-27`'s costume, not a new one.** The card carries the registration stanza, three single-line
   anchors, the wrap hazard on the first one, and a guard that **counts the list and asserts the
   numeral matches it**, so the number and the enumeration can never disagree again in either
   direction. Ruling on the card: **four**, keeping the instance that got through and saying so —
   dropping to three to make the arithmetic clean would delete the one case that cost something.
2. **REG-010: the half-integer-edged banding, REGISTERED BEFORE IT IS RUN.** §4's tee-up in
   `RESULT-REG-009`. Bins centred on the heap rather than starting on it. In its own document,
   beside P3's failure, never instead of it. **Run it on the FILLED population — 133, not 110** —
   `reg009_band_count_filled.chronological()` hands you the nine-cycle index in one call. Before
   extending anything a matching rule runs against, enumerate the rules whose TIES become reachable
   at the new cardinality and register the tie-break in its own commit first.
3. **"disclosed rectangle" at paper III §4.4 and §5** — 86.1 % of the disclosure falls outside it,
   so the adjective is wrong at all four sites. Stanza pre-written; recover with
   `git show 958956a~1:docs/HANDOFF.md`. **Five sessions old.** SCOPE-001 and PIN-001 both prove the
   paste-and-perform shape: `-33` and `-34` each spent zero tokens searching.
4. **Infra, all carded, all Claude-hands:** `@concierge_ingest` / `@concierge_router` carry the same
   Caddy ordering defect `@darlish` had (`1217488447555628`) · the live capability path is committed
   in cleartext to `n8n-stack` and the repo copy has drifted from live (`1217488117177482`) ·
   `dx --get`'s byte count **and its total failure on binary** (`1217488245131362`, addendum filed).
5. **AAR A2** — the four other `post-*` hooks in `darwin-mac-ops/hooks`; plus **A1's residual**
   (`1217468064910605`), now with **five** consecutive sessions' evidence. `GATE_ROSTER_WHO` still
   does not reach the commit hook: every commit in `-34` logged `cloud-JuwyZKqj` while the roster
   row said `big-wealthTensor-34`. `-33` narrowed it to the hook's own subprocess.
6. **card-lint's structural false positive** (`1217483699706758`) · **the gate defect card**
   (`1217465036940491`).
7. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
8. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**
   REG-010 may want it.

---

## 4 · WHAT WOULD HAVE SAVED `-34` TIME

- **THE HANDOFF'S OWN PARAGRAPH INDICES WERE STALE BY +1, AND THAT COST THE FIRST HALF HOUR.** `-32`
  enumerated against the pre-SCOPE-001 paper; `-33`'s edit (`3795372`) inserted a new blank-line
  block at what is now block **206**, so every listed index ≥ 206 was off by one. Uncorrected, four
  of them land on a horizontal rule or a bare heading — which reads like a broken enumerator rather
  than a shifted one. **Both members of each ±1 pair were read, so the coverage claim does not
  depend on the correction being right.** The list also contained 26 indices against a stated 22,
  and 8 read + 26 unread = 34 against "31 enumerated": the arithmetic was never checkable because
  **the enumerator was never committed.** *This is the session's own finding turned on the session's
  own paperwork — coordinates are a moving target. A handoff should carry anchor phrases, not line
  numbers or block indices. This file does.*
- **THE MUTATION RECIPE IN `-33`'s HANDOFF IS WRONG FOR ONE COMMON FORM.** `git checkout <sha> --
  <path>` **also stages** the old blob, so the documented `git checkout -- <path>` restores the
  *mutation* from the index and the tests stay red — which reads exactly like a guard that cannot be
  un-mutated, at the moment you are least able to tell. **Correct un-mutation:
  `git reset HEAD -- <path>` then `git checkout HEAD -- <path>`, with `git status --porcelain`
  printing nothing as the proof.**
- **MUTATE IN A `git worktree` WHEN THE MUTATION IS A COMMIT.** Proving that
  `test_each_pinned_path_was_last_touched_by_...` fires needed a *real* commit touching a pinned
  file. `git worktree add -b <scratch> /tmp/<dir> HEAD`, commit there, run pytest with the main
  `.venv/bin/python`, then `git worktree remove --force` + `git branch -D`. The live tree is never
  in a state `git status` cannot describe. **And a guard mutated one way has been proved one way** —
  PIN-001 was mutated three, and each reddened a different test.
- **`defensive_count.py` takes a PATH and is meaningless without `--against`.** Copy the pre-edit
  file to `/tmp` *before* running the patch script; there is no second chance once the tree is dirty.
- **The patchkit anchor rule paid a third time**: five single-line anchors, no internal newlines,
  all five resolved first try. Three edits in `-32`, one in `-33`, five in `-34`, zero misses.
- **`git checkout <sha> -- <path>` aside, never interpolate a comparison through nested `ssh`** —
  write it to a file, ship it, run it. `-33`'s one violation produced a false mismatch that nearly
  triggered a destructive repair.

---

## 5 · DEFINITION OF DONE (carry this forward)

PIN-001 is **done**: registered alone, performed on §11, guarded by a git check proved by three
mutations, G-COACH-3 non-increasing, suite green at 783, card carrying the find and the performance.
**The §1.3 grep is done as an enumeration** — six sessions, six costumes, every enumerated paragraph
read.

The next unit of done is **item 1**, and it is a paste-and-perform, not a search: the
`"refused five times"` count, registered alone in a two-paragraph `RESULT-TERM-002.md`, performed at
three anchors, guarded by a test that **counts §8's list and asserts the numeral matches it**, and
proved by mutation. The card has all of it, including the ruling. A session that finishes it should
land in under two hours and leave item 2 — REG-010 — as the next real search.
