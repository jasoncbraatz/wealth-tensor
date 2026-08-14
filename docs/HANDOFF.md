---
project: wealth-tensor
gh_sha: 3f315af5ee0422421151608246c1a6f597d9197e
updated: 2026-08-14
session: wealthTensor-40
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

*`gh_sha` points at the commit this file describes; the only thing added after it is this file, so
`--check` prints `ADVISORY: docs-only drift` and exits 0. **Read the exit code.***

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff, any
   result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the other
   thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. **`docs/scouting/SCOUT-001-paper-III-opposing-team.md`** — **NEW, and it is the thing to read
   before you touch the manuscript.** `-40`'s at-bat: the scheduled scouting report under §4. Six
   repair tickets, each with its drill and its measurement, and four read-only probes in
   `docs/scouting/probes/` that re-run in seconds. **It is not the manuscript and never becomes it.**
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md` §§3.2, 3.3, 7** —
   promoted up this list because `SCOUT-001` T1 found the manuscript violating §7 in the abstract.
   §3.2 is the four-regime ladder, §3.3 the registered bias directions, §7 the reporting constraints.
   **A registration carries reporting constraints as well as predictions, and they are greppable.**
5. **`docs/preregistration/REG-012-band-count-edge-phase.md`** — §§1–2 are two findings about how the
   question was ASKED; §6 is the two-branch ruling. Read both before touching anything edge- or
   band-shaped.
6. `docs/preregistration/RESULT-REG-012-band-edge-phase.md` — **§0 first** (the two defects), then §3, then §4.
7. **`docs/preregistration/RESULT-TERM-001.md`** — the **five-site ruling**. §2 before touching any *rectangle*.
8. `docs/preregistration/REG-010-p3-half-integer-banding.md` — **§1 is the population ruling**, §3 the two-branch ruling.
9. `docs/preregistration/CONSTRUCTION-REG-010-edge-convention.md` — **§C2 owns the 55.71 % and owns its
   population in the same sentence.** C3 and C5 are the two a later session walks past.
10. `RESULT-REG-010-half-integer-banding.md` §3 then §4 · **`RESULT-TERM-002.md`** the two-numeral
    ruling, §2 before §8, §8.1, §A.2.4 · `RESULT-PIN-001.md` · `RESULT-SCOPE-001.md`.
11. `RESULT-REG-009-band-count-filled.md` §4 → §3 → §6 · `CONSTRUCTION-REG-009-coverage-fill.md`
    (**R5 is load-bearing and unspent**) · `RESULT-REG-009.md` (**§3's S = 0.1391 is load-bearing in a
    test**) · `REG-009-p3-lifetime-sourced-delta.md` (**READ THE HEADER NOTE FIRST**; numbering 6–12 by ruling).

> **`-40` in one line: THE SCOUTING REPORT SHIPPED, AND ITS TWO REAL FINDINGS ARE BOTH THE PAPER
> FAILING TO KEEP A PROMISE IT WROTE DOWN ITSELF.** `REG-003` §7 says *"no sentence anywhere may
> round"* α̂ to *"the recognition rate"*; the abstract rounds it, and so do four other sites, while
> §5.4 — the section that produced the number — complies in full. And `REVIEW-004` C12 named the
> elected annual test date in the dossier era, proposed a diagnostic, and the diagnostic was
> never run: run now, charges concentrate on a firm's own calendar quarter at p < 0.0003 in both
> universes. Neither finding needed a new idea. Both needed somebody to grep a document against a
> promise and run a script somebody else had already specified.

---

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-40`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.

**`--replaces` WORKS and is verified again in `-40`** — `roster join --replaces cloud-<fp>` printed
`absorbed 1 row(s)` and the board showed one name, one session row. `roster leave` ONCE at wrap.

> ### ⚠ THE `export GATE_ROSTER_WHO=...` LINE EVERY HANDOFF SINCE `-30` CARRIED IS RETIRED. IT NEVER DID ANYTHING.
>
> **`-40` closed card `1217496462088036` after eight consecutive sessions.** dx spawns a **fresh
> remote shell per call and carries no environment**, so an `export` run in the cloud container
> reaches darwin as the empty string — measured in ninety seconds with
> `dx 'echo [$GATE_ROSTER_WHO]'`, which returns `[]`. The card's own narrowing (*"this is NOT a
> variable lost crossing the dx boundary; the hook is not reading it"*) was **backwards**: `-37`
> measured the inline shape against a hook that had no read of the variable at all, so both shapes
> failed for the same reason and the boundary hypothesis was eliminated by a test that could not
> distinguish them. `-38` then fixed the reader, correctly, and nothing re-tested the shape the card
> had ruled out. **A stale negative closes a question harder than an open one.**
>
> **SET IT INLINE, in the same dx invocation as the commit:**
>
> ```
> /tmp/dx 'cd ~/repos/wealth-tensor && GATE_ROSTER_WHO=big-wealthTensor-NN ROSTER_BRAKE_ACK=<n> git commit -F <file>'
> ```
>
> `-40`'s own two commits are the proof, one token apart: `3f315af` **without** the prefix logged
> `cloud-h+04cOcn` and warned the session about its own claim; `f45ee62` **with** it logged
> `big-wealthTensor-40` and named only the two real siblings. Drill:
> `~/Scripts/roster-identity-drill.sh` — three cases against a scratch `ROSTER_DB`, live board never
> written, mutation-proved red at exactly 1. **`-39`'s "commits logged `big-wealthTensor-39`" was
> the `--replaces` half being true and the commit-name half not.**

**THE MINUTE-TWO STANZA IS TWO LINES.** `dx --get`/`--put` are **binary-clean and self-verifying**
(`darwin-scripts 9fd8b1f`). **No base64. No manual `shasum`.**

```
/tmp/dx 'cd ~/repos/wealth-tensor && tar czf /tmp/wt-lite.tgz docs scripts tests src && tar czf /tmp/wt-data.tgz data'
/tmp/dx --get /tmp/wt-lite.tgz /tmp/wt-lite.tgz && /tmp/dx --get /tmp/wt-data.tgz /tmp/wt-data.tgz
```

`-40` measured 1,983,750 + 4,682,857 bytes, both `verified against darwin` **in words**, seconds.
**Trust the sentence, not a number. Exit 5 = bytes crossed but did not match, nothing written,
replay-safe, re-run.** `UNVERIFIED` means dx could not check and deliberately does not share that
exit code. Drill: `~/Scripts/dx-transfer-drill.sh`, run **from the cloud**, also at
`https://system.europeanflorist.com/dsh/dx-transfer-drill.sh`.

Still true: `--put` does **not** create parent directories (fails loudly, exit 1) — **`-40` hit this:
`mkdir -p` the remote directory first, in its own `dx` call.** Remote paths interpolate **raw**, so
`~` and globs expand remotely. **Never inline a multi-line string in `dx '...'`** — write locally,
`--put`, run it. **`ROSTER_BRAKE_ACK=<n>` MUST EQUAL THE STAGED COUNT** (`-40`'s were 5 and 2).

**SUITE COUNTS — COLLECTED + SKIPS, NOT TWO PASS COUNTS.**

| | at `3f315af` (verified in `-40`, both machines, same day) |
|---|---|
| collected | **828** |
| cloud (`PYTHONPATH=<root>/src`) | **820 passed / 8 skipped**, ~138 s, **every skip `not a git work tree`** |
| darwin (`.venv/bin/python -m pytest`) | **828 passed**, ~57 s |

*The cloud figure came off a tree pulled entirely by `--get`, which beats a sha: a sha proves the
tarball, a green suite proves the extracted tree.*

---

## 0 · THE TELL, NOW IN TWENTY-ONE SHAPES

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL GONE QUIET (`-32`). `-33`: instruments that agree with themselves.
`-34`: defects nobody introduced. `-35`: defects you are about to introduce. `-36`: pre-commit the
FAVOURABLE outcome's meaning; an item naming both a document and a population is two claims. `-37`:
a pre-written repair's site count is the one part no anchor can contradict; a mutation that does not
mutate reports your guard as weak. `-38`: a proposed statistic can be a tautology in measurement's
clothing — do the algebra first; a citation carries its population or nothing; grep the estate for
the ANSWER, not the symptom; in a shared tools directory the file-creation verb is the safety check.
`-39`: an inherited claim about HOW something fails is a claim about whether it gets fixed; N
observations with N workarounds and zero causes means the corpus is accumulating; a handoff
instruction silently outranks a standing doctrine leaf; **assert the EXACT exit code, never merely
"nonzero"**; build the fix where it can be proven without shipping it. **`-40` adds three:**

- **A HYPOTHESIS ELIMINATED BY A MEASUREMENT TAKEN AGAINST A SINCE-CHANGED SYSTEM IS A STALE
  NEGATIVE, AND A STALE NEGATIVE CLOSES A QUESTION HARDER THAN AN OPEN ONE.** `-37` ruled out the dx
  environment boundary on a test run against a hook that could not read the variable; `-38` fixed the
  hook; nobody re-tested the ruled-out shape, and the card ran eight sessions on a one-token fix.
  This is `-39`'s severity finding one layer down — there the wrong attribute was *how* it failed,
  here it is *what it is not*. **When you eliminate a hypothesis, record WHAT ELSE WAS TRUE AT THE
  TIME**, because a fix landing anywhere in the chain revives it and nothing will notice.
  Banked: `2026-08-14-hypothesis-eliminated-against-since-changed-system`.
- **A REGISTRATION CARRIES REPORTING CONSTRAINTS AS WELL AS PREDICTIONS, AND THE CONSTRAINTS ARE
  GREPPABLE.** `REG-003` §7 forbade rounding α̂; §5.4 obeyed and the abstract did not, along with three
  other downstream sites. That is the characteristic shape and it is *worse* than a uniform lapse:
  the qualification exists, in the right paragraph, and does not travel. **The audit is a grep** —
  pull every MUST / MAY NOT / NO SENTENCE MAY out of the registrations and grep the manuscript for
  each governed quantity. The repair is always **replace the noun phrase**, never add a caveat: a
  narrower noun phrase is shorter than a hedge and cannot raise the defensive-sentence count.
- **WHEN A ROBUSTNESS CUT IS REPORTED, CHECK IT AGAINST THE BOUNDARY THE *CLAIM* NEEDS, NOT THE
  BENCHMARK THAT FLATTERS IT.** §5.4 reports the adverse cut as *"still an order of magnitude above
  the calibration"* — 0.327 against 0.05, true — while the claim it supports needs 0.327 above
  **0.3333**, which it misses by 0.006. **And note which uncertainty bites:** the 95% interval was
  harmless (0.959 at its lower bound) and the *bridge* uncertainty was fatal, which is the general
  case whenever an instrument is repurposed.

**AND (BUG SPRAY, live again):** `-40`'s first identity drill printed three cases and could not tell
any of them apart, because it copied a live board that already carried both names. **A green case
that is green because the state was already there is the same defect as a red case that is red for
the wrong reason.** Wipe the state each case sets out to create, and add a control that writes a
name belonging to nobody.

**Everything `-33` through `-39` banked is unchanged and still sharp.** A guard must scan assertions,
not quotations. Commit-shaped mutations go in a throwaway worktree. `severity.check`'s witness must
return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory, and
APPEND to an existing drill rather than replacing it — **`-40` obeyed this: `roster-identity-drill.sh`
is a new name checked free, and `roster-oncommit-drill.sh` is untouched.**

---

## 1 · WHAT HAPPENED

**`3f315af` — `SCOUT-001`, the scheduled scouting report. This was the at-bat.** Six findings, six
drills, no bare verdicts, four read-only probes. **`docs/papers/` was not touched**, so `G-COACH-3` is
not engaged and `defensive_count.py` reads **3 invariant / 0 limitations**, identical to
`DEFENSIVE-BASELINE.json`. `G-COACH-4` held: `docs/scouting/` and nothing else.

The two that are real, and they are real in different ways:

- **T1 — `REG-003` §7 forbids the rounding the abstract performs.** *"α̂ is the recognition rate of the
  quantity PRE-002's instrument identifies ... no sentence anywhere may round it to that."* Rounded at
  the abstract (67), §4.4 (614), §4.9 (931), the §7 ledger (1574) and §9 limitation 4 (1747). §5.4
  complies in full. Compounding: α̂ = 0.408 lands in `REG-003` §3.2's **R1**, which §3.3 pre-committed
  as the **weak-evidence** branch — *"a high α̂ is weak ... reported with that sentence attached, in
  the same paragraph"* — and the pre-commitment travelled to one of five sites. **REPLACE the noun
  phrase.** Four sentences.
- **T2 — the elected annual test date, measured.** ASC 350-20-35-28 lets a firm elect any annual test
  date, so for a firm tripping no interim trigger the earliest recognition is that date: a 0–4 quarter
  delay bolted onto every lag, **identical across tiers**. `REVIEW-004` **C12** named it and proposed
  a diagnostic; the diagnostic was never run and it reached neither the manuscript nor any
  registration. Run now: charges concentrate on a firm's own calendar quarter at **0.751 vs a null
  0.575** (retail, ≥2 charges) and **0.665 vs 0.566** (computer services), every threshold, both
  universes, **p < 0.0003** on 4,000 draws. 45% of computer-services charges land in one quarter of
  four. **STEELMAN §5.3's qualification 1** (currently *"unquantified"*); **TEE UP** the fix and do
  not build it — see §2's new ruling.

Three steelmen, each making a claim harder to dismiss rather than repairing one that is wrong:

- **T3** — §4.4's domain rescue is stated at α̂ only. At `REG-003`'s registered adverse cut of 0.327
  the admissible share of the 683 disclosed pairs falls **0.974 → 0.814** (109 pairs) and the asserted
  rectangle leaves the domain, which needs α > 0.3333. *Probe gates on the paper's own 683 and 0.9736
  before reporting.*
- **T4** — §4.2's continuum is a freedom in **two** unobserved quantities, and `wt084`'s own E7 table
  prints the second one a column right: each member demands its own opening gap, **+0.513 at φ = 0**.
  Bounded at |g₀| ≤ 0.10 the identified set is **0.32** wide, not 1.00 — still fatal to a
  cross-sectional ranking, and no longer dismissible as an unbounded-freedom artefact.
- **T5** — §6.1's *"over 2013–2024"* is the **registrant** window from the run logs; the **events**
  run 2012 Q2 → 2026 Q2 and **15.8% / 15.2%** fall outside. No pull date is pinned anywhere, on an
  endpoint §5.4 and the §7 ledger both document as live.
- **T6** — §5.3's *"no reading ... survives that pattern"* rests on tier 2 being the tallest rung,
  which holds in **34%** of firm-clustered resamples in the pilot and 53% in replication. The robust
  statistic is already in hand and is **shorter**: the predicted ordering appears in **5.7% and 5.8%**.
  **The paper overclaiming about its own failure** — its scrupulousness is calibrated against
  flattering itself and has no guard against being dramatically hard on itself.

**And what the scouting hunted for and did NOT find is worth more than the tickets.** Censoring is
**not** tier-differential and goodwill — the predicted-longest tier — is the **least** censored in
both universes (5.1% and 12.5%). Firm clustering is **mild**: 2.02 and 2.35 events per firm, top-five
share 13.0% and 9.8%. **The two obvious mechanical manufacturers of a null were measured and are
absent.**

**`darwin-scripts f45ee62` — the eight-session `GATE_ROSTER_WHO` bug, closed.** Card
`1217496462088036` **CLOSED**. Cause, fix, drill and mutation proof are in the transport box above.
Two additive changes: `roster`'s USAGE gains a NAMING block **at the scene**, and
`roster-identity-drill.sh` is a new file with a name checked free.

**`claude-blackbook` — three global leaves banked, six corroborated.** `use` was run at the moment
each leaf was read, `record-outcome wealthTensor-40 pass` at wrap.

| | |
|---|---|
| **G-COACH-3** | **not engaged — `docs/papers/` untouched**; `defensive_count` 3 / 0 against baseline |
| **G-COACH-4** | held — `docs/scouting/` only |
| suite | **828 collected**; cloud 820 passed / 8 skipped, darwin 828 passed — **both re-run today** |
| new guards | `roster-identity-drill.sh` (3 cases + control, mutation-proved red at exactly 1) |
| probes | 4 read-only, each gated on a figure the paper already publishes |
| lessons | **three** banked global · **six** corroborated via `use` + `record-outcome` |
| cards | `1217496462088036` **closed** · two opened: `1217501628088122` (T2), `1217501627934797` (T1/T3/T4/T5/T6) |

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-39`'s rulings stand **verbatim**: no third disclosure instrument; phrase set
  frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS THE *DISCLOSED* δ**; **REG-009 IS
  CLOSED, numbering 6–12**; **§4's COVERAGE SILENCE AND §7.5's TWO ERRATA STAY RECORDED, NOT
  REPAIRED**; **DO NOT SPEND THE TIE-BREAK**; **DO NOT PROMOTE `R_MIN`**; **`data/reg-009-band-count.json`
  IS `-31`'s**; **`test_the_cycle_choice_now_decides_the_answer` IS A RESULT**; **§10 IS NOT TOUCHED BY
  SCOPE-001**; **SCOPE-001, PIN-001, TERM-001, TERM-002 ARE CLOSED**; **§11 PINS PER FILE**; **P3 FAILED
  AND REG-010 DID NOT RE-SCORE IT**; **REG-010's POPULATION IS Ψ's 683 PAIRS**; **NEITHER BANDING IS
  PROMOTED**; **REG-008 §2's PROVISIONAL FILENAMES STAY and the CONTAMINATED probe's DOCSTRING IS LEFT
  STANDING**; **THE BAND COUNT MAY NOT BE RE-EDGED AND ITS FLOOR RE-READ (R5)**; **REG-012 IS CLOSED ON
  BRANCH F AND ANSWERS NOTHING ABOUT §7.5** — the shifted band count is *refused rather than merely
  unperformed*; **THE TWO SENSITIVITIES ARE SEPARATE AND MUST NOT BE MERGED**; **REG-012's NUMBERS ARE
  THE BAND COUNT'S AND 55.71 % IS Ψ's** — `tests/test_reg012_band_edge_phase.py` goes red if they
  converge; **`selected_lives` IS THE ONE SELECTION PATH.**
- **THE SCOUTING REPORT'S TIMING IS CLAUDE'S CALL, NOT JASON'S** (his ruling, 2026-08-14). Charter §4
  says so at the scene. **`-40` ran it. It is done and it does not run again on this paper** unless the
  manuscript changes materially.
- **`dx --get`/`--put` DO NOT NEED BASE64.** A base64 leg around dx means you are reading a superseded
  leaf. Run `~/Scripts/dx-transfer-drill.sh` and believe it.
- **NEW · `SCOUT-001` IS NOT THE MANUSCRIPT AND MAY NOT FLOW INTO IT RAW.** Charter §4: it feeds
  practice, as §2-style repair tickets. **ABSORB stays illegal** — every ticket in it names a narrower
  claim, and not one asks for a hedging sentence. If a session finds itself pasting a scouting finding
  into the paper as a caveat, it has the direction exactly backwards.
- **NEW · T2 MAY NOT BE RUN ON THIS DATA.** Any design using the annual-test-date confound — an onset
  bridge carrying the offset, or a restriction to interim-triggered charges — is a **third instrument
  for the lag gradient**. PRE-002 §5's stopping rule bars it; `REG-003` §7 bars reading any such
  finding as evidence the gradient was there all along. **Fresh registration, fresh pull, registered
  before the instrument is coded, and it may not cite the present failure as support for anything.**
  Carded at `1217501628088122`. `SCOUT-001` measured only a property of the *instrument* and says so
  in a scope guard in its own docstring.

---

## 3 · THE AT-BAT for `-41` — **work the manuscript tickets. Take T1 first.**

**`SCOUT-001` exists to be worked, not admired.** Card `1217501627934797` carries T1, T3, T4, T5, T6
with every measurement inline; the report itself carries the drills.

**Take T1 first**, for three reasons that are not about severity. It is four sentences. Its repair
shape — **replace the noun phrase, never add a caveat** — is the one every other ticket also wants,
so doing it first calibrates the pass. And it is the only ticket whose cost is paid by a reader who
never gets to §5.4.

**`G-COACH-3` IS MECHANISED AND YOU ARE ABOUT TO ENGAGE IT.** `-40` did not touch `docs/papers/`, so
the baseline is clean and untested this pass. **Take the pre-edit copy BEFORE the tree is dirtied** —
`--against` has no second chance. Every one of T1, T3, T4, T5, T6 is a REPLACE or a STEELMAN that
should leave the count flat or lower it; **if a pass raises it, the ticket was misread.**

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The remaining board:

1. **`SCOUT-001`'s two free steelmen, neither carded because they are one edit each:** add the
   per-tier **censoring column** to §5.3's PRE-001-vs-PRE-002 table (four numbers, closes an attack
   outright), and move §4.3's rate-times-duration sentence up under §4.2's theorem box (it is the
   answer to the identification bench's only live objection and it is buried).
2. **Infra siblings, carded, Claude-hands:** `@concierge_ingest` / `@concierge_router` carry the same
   Caddy ordering defect `@darlish` had (`1217488447555628`) · the live capability path is committed
   in cleartext to `n8n-stack` and the repo copy has drifted (`1217488117177482`).
3. **AAR A2's residual** (`1217496462088036` is **CLOSED**; what remains of the family is the other
   four `post-*` hooks) · card-lint (`1217483699706758`) · the gate card (`1217465036940491`).
4. The phrase set has a passenger: 30.4 % of trigger sentences match only `events or circumstances`;
   7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
5. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
6. **Still open from the dossier era and still good**, re-served by nobody: `REVIEW-004` **C6** (name
   one asset class where §2's domain restriction holds *and* a recognition event is observable in
   filings — ASC 410 asset retirement obligations is the referee's own offered rescue) and **C10**
   (IAS 36's impairment-reversal asymmetry is a free cross-regime falsification test). `SCOUT-001` §5
   names them as open rather than re-arguing them.
7. **Not mine, not touched:** handoff-lint warns `HANDOFF-acmeLedger-07.md:22` and `-09.md:36,42` make
   verification claims with no vantage point. Siblings were live on those; don't clobber.

---

## 4 · WHAT WOULD HAVE SAVED `-40` TIME

- **THE FIRST TEN MINUTES DECIDED THE SESSION FOR THE SIXTH TIME RUNNING** (`-35` truth, `-36`
  population, `-37` count, `-38` premise-and-instrument, `-39` severity, `-40` **the promise the
  document made about itself**). T1 came out of reading `REG-003` §7 *before* the manuscript and then
  grepping one noun phrase. **Spend the ten minutes, and spend them on the registration.**
- **GREP THE ESTATE FOR THE ANSWER BEFORE MEASURING ANYTHING.** T2 was named by `REVIEW-004` C12 with
  its diagnostic attached; `-40`'s contribution was running a script somebody else had specified.
  **`docs/` already contains findings nobody has discharged**, and the dossier era ending did not
  make its contents wrong — only its cadence. Read `REVIEW-004` C-series before hunting fresh.
- **GATE EVERY PROBE ON A NUMBER THE PAPER ALREADY PUBLISHES.** All four of `-40`'s assert against
  683 pairs / 0.9736, `wt084`'s printed E7 endpoints, or §5.3's eight tier medians *before* reporting
  anything new. It caught a real error: a first cut of the continuum probe re-derived g₀ from scratch
  and got +0.316 where `wt084` prints +0.513 — the family is anchored on the g₀ = 0.15 world, not on
  square books. **An ungated probe would have published that number.**
- **WIPE THE STATE A DRILL SETS OUT TO CREATE.** See the bug-spray tell.
- **`--put` DOES NOT CREATE PARENT DIRECTORIES.** `mkdir -p` the remote directory in its own `dx` call
  first. Costs one line; `-40` paid for it in one failed attempt.
- **A SIBLING'S CLAIM IS NOT A BLOCK.** `Scripts` was claimed by two live siblings; `-40` staged by
  path, touched nothing either had, and said so in the commit. **Stage by path, `ROSTER_BRAKE_ACK` =
  staged count.**
- **`roster leave` ONCE**, and if you commit without the inline prefix, `roster release --who
  cloud-<fp>` to drop the stray row the hook wrote.
- **CORROBORATE THE LEAVES YOU USED.** `-40` ran `use` on 6 at the moment each was read and
  `record-outcome wealthTensor-40 pass` at wrap.

---

## 5 · DEFINITION OF DONE (carry this forward)

**The scouting report is done**: scheduled without an ask, run once, landed only in `docs/scouting/`,
six findings each with a drill, every measurement gated on a published figure, both mechanical
accounts of the null hunted and absent, one specific strength named per `G-COACH-5`, and two stopping
rules honoured out loud rather than quietly.

**The `GATE_ROSTER_WHO` bug is done**: cause found rather than symptom re-recorded, the card's own
narrowing overturned by measurement, fix proved on two real commits one token apart, drilled with a
control, mutation-proved red at an exact code, and repaired **at the scene** in the tool every session
reads rather than in a handoff that gets rewritten.

**The research ledger on paper III is still empty, and it stays empty.** The next unit of done is the
**manuscript pass**: `SCOUT-001`'s six tickets worked, `G-COACH-3` engaged with a pre-edit copy taken
first, and the defensive count flat or lower — because every ticket names a narrower claim and not one
asks for a hedge. **A session that goes looking for a new registration should first satisfy itself
that the estate is asking for one. It is not — but for the first time in ten sessions there is a list
of concrete edits waiting, and the paper gets better by somebody making them.**
