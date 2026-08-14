---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-14
session: wealthTensor-33
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
3. **`docs/preregistration/RESULT-SCOPE-001.md`** — `-33`'s repair: §10's restriction and §5's
   selection, read in the same sitting. §2 is the registered stanza; read it before touching either
   section.
4. **`docs/preregistration/RESULT-REG-009-band-count-filled.md`** — `-32`'s run. §4 first (the
   verdict and the parameter the fill created), then §3 (the fill's price), then §6 (the manuscript
   repair, registered and performed).
5. `docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md` — the rules `-32` fixed **in their
   own commit, before any count existed**. `git log --follow` on that file is the ordering proof.
6. `docs/preregistration/RESULT-REG-009-band-count.md` — `-31`'s two-cycle run, **unaltered except
   for the amendment at the end of §4**. Its two errata stay errata.
7. `docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` — **READ THE HEADER NOTE FIRST.**
   §§0–5 are Part I, §§6–12 Part II. **The numbering is 6–12 and not 2–8 by ruling.**

> **`-33` in one line: the fifth costume is REPAIRED, and the session's engineering went into the
> transport it ran over.** §10 restricts §2 to degradation carrying no estimable loss; §5 selects its
> whole sample on recognised impairments. One sentence in §5 — a STEELMAN, not a caveat — places the
> sample on the **boundary** of the restricted region: a charge is the moment degradation *became*
> estimable. §10 untouched, G-COACH-3 3 → 3, suite 772 → 777, guard proved by mutation. And the
> session opened with darlish down for a reason no symptom row covered: a source-IP handler above the
> capability-path handler in Caddy, fixed live, now diagnosed automatically.

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**If it does not come up, the first move is `dsh-fire` + `dwait`, not diagnosis** — one command
through the fallback tells you whether darwin is alive, and that single fact reclassifies everything
after it. See §4.

## 0 · THE TELL, NOW IN EIGHT SHAPES — and this session's two are both about INSTRUMENTS THAT AGREE WITH THEMSELVES

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A CHOICE RULE'S
TIE-BREAK AT A NEW CARDINALITY and OF A TELL THAT HAS GONE QUIET (`-32`). `-33` adds two, and
neither is about the paper:

- **A FAILURE SIGNATURE IS A CLASSIFICATION, NOT A CAUSE.** The pipe was down; every instrument said
  "handshake timeout", which is also what a dead broker, a firewalled port and an unreachable
  upstream say. The cause was a *live* server answering with the *wrong* content. One plain GET on
  the same path separated "nothing is listening" from "the wrong thing is listening" — and only the
  first was an outage. **When a diagnostic reports a symptom that four causes share, the next command
  is the one that splits them, not the one that acts on the most likely.**
- **A MISMATCH REPORTED BY A HAND-ROLLED COMPARISON IS A CLAIM ABOUT THE COMPARATOR.** A one-liner
  interpolated through two layers of `ssh` quoting hashed the escaped quotes along with the value and
  reported that darwin's stored capability path differed from the Caddyfile's. The queued next step
  was to "repair" darwin to match — which would have broken a correct config during an outage. A
  file-shipped re-derivation returned MATCH. **Re-derive a finding by a different route BEFORE it
  triggers a destructive repair.** (AAR `darlish-shadowed-path-outage`; lessons
  `2026-08-14-reverse-proxy-matcher-list-ordered-source`, `2026-08-14-mismatch-reported-hand-rolled-comparison-claim`.)

**Witness contract, unchanged:** `severity.check`'s witness must return **FALSY**, and a witness that
could be true in a legitimate world dies as VACUOUS rather than reporting. Write witnesses that are
*structurally* false. **A source-text guard fires on its own witness** — `-33` sidestepped it the way
`-32` did, by IMPORTING the subject (`test_scope001_steelman.py` imports the sentence from
`scripts/wt093_edits_scope001.py`) rather than retyping it. **And prove a new guard by MUTATION
before trusting it** — commit first so git is the undo path, delete the subject in the working tree,
watch it go red, `git checkout --` it back. `-33` did; 2 of 5 tests fired.

---

## 1 · WHAT HAPPENED

**`4124973` — the registration, alone.** `RESULT-SCOPE-001.md` and nothing else, so the ordering is
provable rather than asserted. It declares the repair to be a STEELMAN, declares it goes in §5 and
not §10, and declares G-COACH-3 will be evaluated across the edit — all before the edit script
existed on disk.

**`3795372` — SCOPE-001 performed.** The find `-32` located to the line: paper III §10 restricts §2's
claim to degradation *"carrying no impairment trigger, no estimable expected loss and no observable
event to key recognition to"*, while §5 selects its whole sample on three recognised-impairment tags
(`edgar.TIER_TAGS_REG006[0]`). Both sentences are correct in their own section; on their face the
restriction excludes exactly the region the selection selects on. One sentence added to §5.1,
immediately after the four-tier table:

> **Every event in this test is a recognised impairment, which places the sample on the boundary of
> §10's restriction rather than inside its complement:** a charge is the moment degradation became
> estimable, so §2 governs the accumulation that precedes it and the event marks where that
> accumulation ends — which is why an interval is measurable on these events and on no others.

§10 was **not touched**. No hedge, no caveat, no free parameter — the ABSORB move charter §2 forbids
was available and refused.

| | |
|---|---|
| **G-COACH-3 across the edit** | **3 → 3 (+0)**, `--against` the pre-edit copy |
| suite | **772 → 777**, green in ~57 s |
| new guard | `tests/test_scope001_steelman.py`, 5 tests, **proved by mutation** |
| card | State Machine `1217484751716249` — **closed**, with the performance recorded on it |

**One correction to the card, on the record.** It said "§5's 151 tier-0 property events". 151 is
REG-009's REG-006-**repaired** population; §5.3's published tier-0 counts are 21 and 34. The claim is
true in every version — all of them are recognised impairments — and `RESULT-SCOPE-001` states it in
the units each number belongs to. **A number inherited from a card is still a number to check.**

**AND THE SESSION OPENED WITH AN OUTAGE, WHICH IS WHERE MOST OF THE ENGINEERING WENT.** darlish would
not come up: enrollment authorized, then `TimeoutError: timed out during opening handshake`, three
times, twenty seconds apart. Root cause: `handle @allowed` (remote_ip `10.10.10.0/24`,
`172.16.0.0/12`) sits ABOVE `handle @darlish` in the n8n.braatz.io site block, and **this container
reached Caddy from 10.10.10.1** — inside `@allowed` — so n8n was served on the capability path. n8n
answers a WS upgrade with 200 HTML and never upgrades. Latent twelve days; every previous container
egressed from a public IP (broker log `xff=160.79.106.x`) and fell through correctly.

- **Fixed live**: `@darlish` block hoisted above `@allowed`, `caddy validate` gating the write,
  `caddy reload`, backup `/opt/n8n/Caddyfile.bak-darlish-order-20260814-125648`, auto-rollback on
  failure. Pipe green on the first try after.
- **The whole diagnosis ran over the three-leg fallback** (`dsh-fire` + `dwait`), which proved darwin
  alive inside two minutes and reached the Linode through it. **darlish being down never meant darwin
  was down**, and the fallback is genuinely load-bearing rather than theoretical.
- **`darlish-check` now asks WHO ANSWERED** on a timeout (426 broker · 200 HTML shadowed · 403 stanza
  missing), names BOTH causes of the 200-HTML case (a stale local path is the cheaper one — try
  `darlish-up` first), and **routes**: a finding that names its own fix now prints State Machine, not
  Batter's Box. The old card paged Jason for a Caddyfile line move. Both branches exercised before
  publish; relay verified byte-identical (`darwin-scripts 93fe470`).
- **DARLISH.md** gains the symptom row it was missing and the converse of the darwin-green trap: the
  route a client takes is a property of THAT client, not of its class (`n8n-stack 20c5fde`).

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s and `-32`'s rulings stand verbatim: no third disclosure instrument; phrase set frozen
  at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE COINCIDENCE
  ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS AN UPPER BOUND — the *disclosed* δ**;
  **REG-009 IS CLOSED and its numbering is 6–12**; **§4's COVERAGE SILENCE STAYS RECORDED, NOT
  REPAIRED**; **§7.5's TWO ERRATA ARE RECORDED, NOT REPAIRED**; **DO NOT SPEND THE TIE-BREAK** (the
  chronological convention was fixed in `958956a` before any count existed — do not flip it, do not
  switch the cycle pick, do not report the mirror as the answer); **DO NOT PROMOTE `R_MIN`**;
  **`data/reg-009-band-count.json` IS `-31`'s**; **`test_the_cycle_choice_now_decides_the_answer` IS
  A RESULT, NOT A DEFECT.**
- **NEW · §10 IS NOT TOUCHED BY SCOPE-001, AND THE STEELMAN LIVES IN §5.** The restriction is correct
  as written. A future session that "tidies" the repair by moving it into §10, or that softens §10 to
  accommodate §5, has converted a steelman into scope creep. `test_scope001_steelman.py` goes red
  both ways.
- **NEW · SCOPE-001 IS CLOSED.** The find is repaired, registered, guarded and carded. What remains
  of that thread is item 1 below, which is the *rest of the grep*, not a re-litigation of this one.

---

## 3 · THE AT-BAT, RANKED

1. **THE §1.3 GREP IS NOT EXHAUSTED — and it is now the oldest live thread.** 31 self-critical
   paragraphs enumerated; 8 read (`-32`), and the ninth became SCOPE-001. **Paragraphs 90, 134–139,
   185–188, 252, 265, 277–283, 294, 305, 316–317, 322, 347 are still unread.** Re-run with the
   **instrument-vs-prose split** as the discriminator, never the raw count — the raw form returns
   nothing because the discussion docs restate every needle 2–6 times. Five costumes so far: a
   mis-scoped NUMBER (`-23…-25`), ADJECTIVES promoted past their measurement (`-26`), adjectives
   flagged load-bearing and never built (`-27`), and now a SCOPE RESTRICTION vs a SAMPLE SELECTION
   (`-33`). **Assume a sixth.**
2. **REG-010: the half-integer-edged banding, REGISTERED BEFORE IT IS RUN.** §4's tee-up in
   `RESULT-REG-009`. Bins centred on the heap rather than starting on it. In its own document, beside
   P3's failure, never instead of it. **Run it on the FILLED population — 133, not 110** —
   `reg009_band_count_filled.chronological()` hands you the nine-cycle index in one call. And per
   `-32`'s lesson: before extending anything a matching rule runs against, enumerate the rules whose
   TIES become reachable at the new cardinality and register the tie-break in its own commit first.
3. **"disclosed rectangle" at paper III lines 964, 996, 1123, 1573.** 86.1 % of the disclosure falls
   outside it, so the adjective is wrong at all four. Stanza pre-written — recover with
   `git show 958956a~1:docs/HANDOFF.md` — paste into a two-paragraph `RESULT-TERM-001.md`, perform,
   then re-run `test_ledger_provenance` + `test_restatement_reach`. **Four sessions old.** SCOPE-001
   proves the paste-and-perform shape works: `-33` spent zero tokens searching.
4. **Infra, all carded, all Claude-hands:** `@concierge_ingest` / `@concierge_router` carry the same
   ordering defect `@darlish` had (State Machine `1217488447555628`) · the live capability path is
   committed in cleartext to `n8n-stack` and the repo copy has drifted from live
   (`1217488117177482`) · `dx --get` reports the on-wire byte count as the file size
   (`1217488245131362`).
5. **AAR A2** — the four other `post-*` hooks in `darwin-mac-ops/hooks`; plus **A1's residual**
   (`1217468064910605`), now with **four** consecutive sessions' evidence and one new datum: the env
   var reaches `roster` when dx runs it directly and is lost only in the hook's own subprocess, which
   narrows the fault to how the pre-commit hook builds its environment.
6. **card-lint's structural false positive** (`1217483699706758`) · **the gate defect card**
   (`1217465036940491`).
7. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
8. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.**
   REG-010 may want it.

---

## 4 · WHAT WOULD HAVE SAVED `-33` TIME

- **THE FIRST FIVE MINUTES OF A DEAD PIPE BELONG TO `dsh-fire` + `dwait`, NOT TO DIAGNOSIS.** Firing
  one command through the fallback proves whether darwin is alive, and that single fact reclassifies
  everything after it. `-33` spent three `darlish-check` runs before reaching for it.
  `curl -s https://system.europeanflorist.com/dsh/{dsh-fire,dwait} -o /tmp/…` — the secret is already
  at `/tmp/.dsh-fire.env` after `darlish-up`'s collect phase, even when the pipe itself fails.
- **`/tmp/dfx` is worth re-creating in one paste** if darlish is down: fire + parse the token + wait,
  with dx-shaped exit codes (3 = never reached darwin, 75 = fired but no result). It made the
  fallback feel like `dx` and cost four minutes to write. Copy it out of this session's outputs.
- **NEVER interpolate a comparison through nested `ssh`.** Write it to a file, ship it, run it, and
  have it print MATCH/MISMATCH plus both hashes. `-33`'s one violation of this produced a false
  mismatch that nearly triggered a destructive repair. (Same rule the ROSTER BRAKE section states for
  multi-line strings — it applies to *comparisons*, not just to edits.)
- **`defensive_count.py` takes a PATH and is meaningless without `--against`.** Copy the pre-edit file
  to `/tmp` *before* running the patch script; there is no second chance once the tree is dirty.
- **The patchkit anchor rule paid again**: one single-line anchor with no internal newline, replaced
  by multi-line text, resolved first try. Three edits in `-32`, one in `-33`, zero misses.
- **`aar.py eject` will duplicate cards you already filed.** Set an action's urgency to `medium`/`low`
  with a pointer to the existing card, or you get a second card for the same work — and note that
  `eject` files to **State Machine**, correctly, not to Batter's Box.

---

## 5 · DEFINITION OF DONE (carry this forward)

SCOPE-001 is **done**: registered alone, performed on §5, guarded by a mutation-proved test, G-COACH-3
non-increasing across the edit, suite green at 777, card closed with the performance recorded on it.
The transport it ran over is **done and better than it was found**: the outage is fixed, the runbook
carries the symptom row, and `darlish-check` now discriminates the cause instead of naming the
symptom.

The next unit of done is **item 1** — the rest of the §1.3 grep, in its instrument-vs-prose form,
starting at paragraph 90. It is a SEARCH, not a paste-and-perform, and it should end the way `-32`'s
did: with the find located to the line and its repair pre-written on a card, whether or not the same
session performs it.
