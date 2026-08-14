---
project: wealth-tensor
gh_sha: 3b365b103bebc73e9b21e44576675793b6c40f1e
updated: 2026-08-14
session: wealthTensor-35
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
3. **`docs/preregistration/RESULT-TERM-002.md`** — `-35`'s repair, and the one place the
   **two-numeral ruling** is registered. Read §2 before touching §8, §8.1 or §A.2.4.
4. **`docs/preregistration/RESULT-PIN-001.md`** — `-34`'s repair: §11's code-state pin, and the
   first costume of the §1.3 shape that was **true when it was written**.
5. `docs/preregistration/RESULT-SCOPE-001.md` — `-33`'s repair: §10's restriction and §5's
   selection, read in the same sitting. §2 is the registered stanza; read it before touching either
   section.
6. `docs/preregistration/RESULT-REG-009-band-count-filled.md` — `-32`'s run. §4 first (the verdict
   and the parameter the fill created), then §3 (the fill's price), then §6 (the manuscript repair).
7. `docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md` — the rules `-32` fixed **in their
   own commit, before any count existed**. `git log --follow` on that file is the ordering proof.
8. `docs/preregistration/RESULT-REG-009-band-count.md` — `-31`'s two-cycle run, **unaltered except
   for the amendment at the end of §4**. Its two errata stay errata.
9. `docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.**
   §§0–5 are Part I, §§6–12 Part II. **The numbering is 6–12 and not 2–8 by ruling.**

> **`-35` in one line: THE PASTE-AND-PERFORM WAS RIGHT ABOUT THE FIND AND WRONG ABOUT THE FIX,
> and catching that was the whole session.** The card pre-wrote "four" at all three `"refused five
> times"` sites. Two of those sites read *"refused ... times in **other costumes** (§8) and should
> have refused here"* — and §8.1's φ move **is** one of §8's four, and is the one the paper concedes
> it did **not** refuse. Pasting the stanza would have asserted a refusal the paper retracts two
> lines later: **the repair introducing a fresh instance of the defect it repairs, signed off as
> done, with a registration document vouching for it.** Registered alone at `75111ea`, performed at
> `d69dbe6` with the count bound to **two** numerals derived from one parse, guarded by a test
> proved by **four** mutations, G-COACH-3 3 → 3 (+0), suite 783 → 790. Then BUG SPRAY at `142a8d7`:
> `-34`'s greppable corollary, written in `docs/` twice and enforced nowhere, is now a test.

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-35`.** If it does not come up, the first move is
`dsh-fire` + `dwait`, not diagnosis. See `-33`'s §4, which still holds.

**`dx --get` IS TEXT-ONLY.** Pulling a `.tgz` wrote a 0-byte file and exited 2. Ship binaries
base64'd and `shasum` both ends — dx prints the on-wire byte count, not the file size, so its own
success line cannot certify a transfer (card `1217488245131362`). **The minute-two shape, run again
in `-35` and worth every second: `tar czf` only `docs scripts tests src` on darwin — 1.8 MB on the
wire, 5.5 MB extracted, out of a 684 MB working tree (measured this session) — base64, ONE `--get`,
`shasum` both ends, extract, then grep and read in the cloud at zero round trips.** `-35` additionally ran the whole edit script and all four mutation
proofs against the **cloud copy first**, then performed on darwin and compared sha256 of the paper
across the two machines — byte-identical. **A cloud dry run costs nothing and means the first thing
that touches the real tree has already worked once.** Do that.

## 0 · THE TELL, NOW IN TEN SHAPES — and `-35`'s is about the fix, not the find

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A CHOICE RULE'S
TIE-BREAK AT A NEW CARDINALITY and OF A TELL THAT HAS GONE QUIET (`-32`). `-33` added two about
instruments that agree with themselves. `-34` added the one that finds defects nobody introduced.
`-35` adds the one that finds defects **you are about to introduce, while holding a card that says
you are done thinking**:

- **A PRE-WRITTEN REPAIR IS AN UNVERIFIED CLAIM, AND ITS AUTHOR HAD LESS CONTEXT THAN YOU DO.**
  A handoff that says *paste and perform* is buying you the **search**, not the **correctness** —
  and the previous session wrote the stanza while its attention was on the find. **Check the
  repair's own truth before pasting it.** The specific shape that bit here, and it generalises far
  past this repo: *a correction that changes ONE number in N places is sound only if all N places
  count the SAME set* — and **"in other costumes", "elsewhere", "besides this one", "excluding the
  present case" are exactly the phrases that silently exclude a member.** Bind the numerals
  SEPARATELY and derive every one of them from one parse of the underlying list, so they cannot
  drift apart.
- **`-34`'s shape, unchanged and still the sharpest:** a claim whose truth value depends on
  something that can change without the claim changing will eventually be false and nothing will
  notice, because the failure signature is that *nobody edited the sentence*. The discriminator is
  *is this sentence's truth a function of the repository's PRESENT state?* **The repair is never a
  fresher number.**
- **The greppable corollary is now MECHANICAL for the one case a machine can see.**
  `tests/test_manuscript_shas_are_instrumented.py` asserts every commit SHA paper III names is also
  named by an instrument under `scripts/`, `tests/` or `src/`. It was **already true** at `142a8d7`
  — it adds no claim; it makes the PIN-001 *shape* unrepeatable. It will fire at posting, when
  §11's deferred head-of-repository pin is added, which is exactly when someone should be asked
  what that pin promises. **A rule written in `docs/` twice and enforced nowhere is still
  unguarded; the second writing feels like progress and buys nothing.**

**Witness contract, unchanged:** `severity.check`'s witness must return **FALSY**, and a witness
that could be true in a legitimate world dies as VACUOUS rather than reporting. **A source-text
guard fires on its own witness** — sidestep it by IMPORTING the subject. `-35` took this one step
further and it is the shape to copy: `scripts/wt100_edits_term002.py` exposes **BUILDERS**
(`class_clause(n)`, `reconciling_clause(refused, position)`, `remote_construction(refused)`) rather
than finished strings, the edit calls them with its declared counts and **the guard calls the same
builders with counts it parses out of the manuscript**. There is then no place to type a numeral
that the arithmetic does not reach.

---

## 1 · WHAT HAPPENED

**`75111ea` — the registration, alone.** `RESULT-TERM-002.md` and nothing else, before the edit
script existed on disk. The pre-edit paper was copied to `/tmp` **before** the tree was dirtied —
`defensive_count.py --against` has no second chance once it is not.

**`d69dbe6` — TERM-002 performed.** Four anchors, none with an internal newline, no heading or rule
moved:

| where | before | after |
|---|---|---|
| §8 | `Refused five times across this programme` | `Faced four times across this programme` |
| §8 | `leaning on an unmeasured φ.` | `…φ — three refused, the fourth not.` |
| §8.1 | `refused five times in other costumes` | `refused three times in other costumes` |
| §A.2.4 | `refused five times in other costumes` | `refused three times in other costumes` |

**Four anchors, not the card's three.** The fourth carries the disclosure *inside §8's existing
sentence* — eight words, no new sentence, no hedge — which is where the class count and the refusal
count are reconciled in the manuscript, and the only place either appears together.

| | |
|---|---|
| **G-COACH-3 across the edit** | **3 → 3 (+0)**, `--against` the pre-edit copy |
| suite | **783 → 790**, then **791**; green in 58 s |
| new guard | `tests/test_term002_count.py`, 7 tests, **proved by four mutations** |
| card | State Machine `1217490492527699` — **closed**, with the performance and the amendment on it |

**The four mutations, all restored green** (`git reset HEAD -- <path>` then
`git checkout HEAD -- <path>`, `git status --porcelain` printing nothing as the proof — five clean
un-mutations this session, zero residue):

| mutation | result |
|---|---|
| a fifth item added to §8's list, prose not renumbered | **4 red** |
| one remote site repaired and not the other | **1 red** |
| the sentence-initial `Refused five times` restored | **2 red** |
| the concession marker removed from the list | **3 red** |

The third one is why the five-check is **case-folded**: the original defect occurred once
sentence-initially and twice mid-sentence, so a lower-case-only guard would have been blind to a
third of its own subject. That is a bug the mutation found in the guard, not in the paper.

**`142a8d7` — BUG SPRAY, its own commit, no claim added.**
`tests/test_manuscript_shas_are_instrumented.py`. Narrowed twice so English cannot trip it: a token
must carry **both a digit and a hex letter** and must **resolve to a real commit**. Proved by **two**
mutations, and the second is the one that matters: a real orphan SHA inserted into §A.2.4 goes red,
**and a hex-shaped token naming no commit stays GREEN** — otherwise it is a shape-matcher and you
cannot tell.

**The card's "while you are in there" item was already done.** `-34` appended the `REVIEW-004`
§7→§8 pointer correction in place at `afbdd5c`. Verified, nothing owed. *Check before you repair;
`-35` nearly spent tokens re-fixing a fix.*

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s, `-32`'s, `-33`'s and `-34`'s rulings stand verbatim: no third disclosure
  instrument; phrase set frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**;
  **§4.8 IS NOT THE COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS AN UPPER
  BOUND — the *disclosed* δ**; **REG-009 IS CLOSED and its numbering is 6–12**; **§4's COVERAGE
  SILENCE STAYS RECORDED, NOT REPAIRED**; **§7.5's TWO ERRATA ARE RECORDED, NOT REPAIRED**; **DO NOT
  SPEND THE TIE-BREAK**; **DO NOT PROMOTE `R_MIN`**; **`data/reg-009-band-count.json` IS `-31`'s**;
  **`test_the_cycle_choice_now_decides_the_answer` IS A RESULT, NOT A DEFECT**; **§10 IS NOT TOUCHED
  BY SCOPE-001 AND THE STEELMAN LIVES IN §5**; **SCOPE-001 IS CLOSED**; **PIN-001 IS CLOSED AND §11
  PINS PER FILE** — do not restore a global "last commit touching `src/`" claim in any form and do
  not tidy the per-file pins back into one SHA; **THE §1.3 GREP IS EXHAUSTED AS AN ENUMERATION.**
- **NEW · TERM-002 IS CLOSED, AND THE COUNT IS TWO NUMERALS, NOT ONE.** §8 states the **class**
  count (four) because that is where the list is; §8.1 and §A.2.4 state the **refusal** count
  (three) because they use the word *refused* and their "other costumes" exclude a member. **Do not
  "tidy" these into a single numeral** — that is the defect, re-introduced, and it is precisely what
  the card's pre-written stanza would have done. **Do not drop the fourth item to make the
  arithmetic clean**: it is the instance that got through and the only one that cost this programme
  anything. If §8's list ever legitimately grows, `tests/test_term002_count.py` goes red in both
  directions and both numerals re-derive from the same parse — change the list, not the guard.
- **NEW · A NUMERAL IN THE MANUSCRIPT THAT COUNTS A LIST MUST BE DERIVED FROM THAT LIST BY AN
  INSTRUMENT.** Stated generally because TERM-002 is unlikely to be the only one, and prose counting
  is invisible to every guard this repository had before `d69dbe6`.

---

## 3 · THE AT-BAT, RANKED

1. **REG-010: the half-integer-edged banding, REGISTERED BEFORE IT IS RUN.** §4's tee-up in
   `RESULT-REG-009`. Bins centred on the heap rather than starting on it. In its own document,
   beside P3's failure, never instead of it. **Run it on the FILLED population — 133, not 110** —
   `reg009_band_count_filled.chronological()` hands you the nine-cycle index in one call. Before
   extending anything a matching rule runs against, **enumerate the rules whose TIES become
   reachable at the new cardinality and register the tie-break in its own commit first.** This is
   now the next real *search*, and the first at-bat in four sessions that is not a paste.
2. **"disclosed rectangle" at paper III §4.4 and §5** — 86.1 % of the disclosure falls outside it,
   so the adjective is wrong at all four sites. Stanza pre-written; recover with
   `git show 958956a~1:docs/HANDOFF.md`. **Six sessions old.** SCOPE-001, PIN-001 and TERM-002 all
   prove the paste-and-perform shape — **and TERM-002 proves you must still check the stanza before
   you paste it.** Read §0's first bullet before starting this one.
3. **Infra, all carded, all Claude-hands:** `@concierge_ingest` / `@concierge_router` carry the same
   Caddy ordering defect `@darlish` had (`1217488447555628`) · the live capability path is committed
   in cleartext to `n8n-stack` and the repo copy has drifted from live (`1217488117177482`) ·
   `dx --get`'s byte count **and its total failure on binary** (`1217488245131362`).
4. **AAR A2** — the four other `post-*` hooks in `darwin-mac-ops/hooks`; plus **A1's residual**
   (`1217468064910605`), now with **six** consecutive sessions' evidence. `GATE_ROSTER_WHO` still
   does not reach the commit hook: every commit in `-35` logged **`cloud-4U6RYyNA`** while the
   roster row said `big-wealthTensor-35`. **`roster leave` BOTH rows at wrap** — `-35` did.
   **`-35` also found a SECOND bug sitting downstream of A1**, cheap, separate and carded nowhere
   yet: the roster brake printed **`⚠️ ROSTER CONTENTION — wealth-tensor is ALSO claimed by:
   big-wealthTensor-35`** on *every* commit. The brake compares the hook's `cloud-*` identity
   against the roster and reports **the committing session's own human-named row as a rival**. It
   is alarming, it is wrong, and its real cost is that it trains sessions to ignore a contention
   warning that will one day be true. It vanishes the moment A1 is fixed, and it can also be fixed
   on its own by having the brake treat a roster claim on the repo it is committing to as *self*
   when no other session holds one.
5. **card-lint's structural false positive** (`1217483699706758`) · **the gate defect card**
   (`1217465036940491`).
6. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
7. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**
   REG-010 may want it.

---

## 4 · WHAT WOULD HAVE SAVED `-35` TIME

- **THE CARD'S PRE-WRITTEN REPAIR WAS FALSE AT TWO OF ITS THREE SITES, AND NOTHING IN THE PROCESS
  WOULD HAVE CAUGHT IT.** The registration, the anchors, the guard, the mutation proof, G-COACH-3
  and the suite would all have gone green over a sentence asserting a refusal the paper retracts two
  lines later. **The only thing standing between the estate and that was reading the replacement
  text in its own context before pasting it, which took five minutes.** Budget those five minutes
  into every paste-and-perform at-bat. This is §0's first bullet and it is the session's whole
  finding.
- **THE CARD'S LINE NUMBERS WERE STALE IN UNDER A DAY** — §A.2.4's site was given as 2246 and was at
  2254, drift of +8. Every anchor *phrase* resolved first try, for the fourth session running.
  **Cards and handoffs for this repo quote anchor text; a line number is a hint to grep near, never
  a coordinate.** This file continues to carry no line numbers.
- **PATCHKIT CONSTRAINS THE ANCHOR, NOT THE REPLACEMENT.** `-35` spent time designing around a
  feared reflow cascade before noticing that a one-line anchor may emit **two** lines. That is what
  let §8's closing edit add the reconciling clause and re-wrap in a single anchor without touching a
  neighbouring line. **Thirteen anchors from `-32` to `-35` — 3, 1, 5, 4 — zero misses.**
- **RUN THE WHOLE THING IN THE CLOUD COPY FIRST.** The edit script, the guard and all four mutations
  were exercised against `/tmp/wt` before darwin saw any of it; the post-edit sha256 then matched
  across both machines. Cost: nothing. Bought: the first command that touched the real tree had
  already worked, and the mutation proofs on darwin were confirmation rather than discovery.
- **THE MUTATION RECIPE FROM `-34` IS CORRECT AND IS NOW CORROBORATED** — `git reset HEAD -- <path>`
  then `git checkout HEAD -- <path>`, `git status --porcelain` printing nothing as the proof; five
  un-mutations, zero residue. `lessons.py use` + `record-outcome pass` filed against
  `2026-08-14-mutation-testing-guard-git-checkout-sha`, which was sitting at `trust: quarantine`
  with `used_count: 0`. **Corroborate the leaf you actually used; a quarantined leaf nobody
  confirms is a lesson the corpus cannot promote.**
- **MUTATE BOTH BRANCHES OF A GUARD THAT NARROWS.** The SHA guard's real content is what it
  *excludes*; proving only that it fires would have shipped a shape-matcher indistinguishable from
  the real thing on every green run.

---

## 5 · DEFINITION OF DONE (carry this forward)

TERM-002 is **done**: registered alone, performed at four anchors, guarded by a test that counts the
list and binds both numerals to it, proved by four mutations, G-COACH-3 non-increasing, suite green,
card closed with the performance **and the amendment** recorded on it. The SHA-instrumentation guard
is **done** and adds no claim. **Every repair the `§1.3` grep produced is now built** — SCOPE-001,
PIN-001 and TERM-002 — and the grep itself is closed as an enumeration.

The next unit of done is **item 1, REG-010**, and it is the first real *search* since `-32`: a
registration document written and committed **alone, before any count exists**, the tie-breaks that
become reachable at 133 enumerated and registered **before** the run, the run on the filled
population, and a result document that sits beside P3's failure rather than instead of it. A session
that finishes it leaves item 2 — the disclosed rectangle, now six sessions old — as the next paste,
and that paste gets §0's first bullet applied to it before a single anchor is touched.
