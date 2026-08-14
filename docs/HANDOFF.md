---
project: wealth-tensor
gh_sha: a77c5c516a9d30e5db133836ec8beceba5719eef
updated: 2026-08-14
session: wealthTensor-44
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
2. **`docs/preregistration/CONSTRAINT-INVENTORY-001.md` — the map for this thread, and `-44`
   rewrote it again.** Fifty reporting constraints, now on **two axes**: `recog` (MECH / PROXY /
   READER / n/a — a property of the CONSTRAINT) and a **FOR / BINDS / PARTIAL / ADJACENT** grade
   on the machine cell (a property of the ESTATE). **Read §3 first** — the partition, the audit,
   and §3.4, which is the answer to the question `-42` wrote into the definition of done. Then
   §2's amended bullet and §2a's counts block.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md` §§3.2, 3.3, 7** — the
   four-regime ladder, the registered bias asymmetry, the rounding rule. Three of the estate's
   eight purpose-built guards point here.
5. **`docs/scouting/SCOUT-001-paper-III-opposing-team.md`** — **WORKED, NOT PENDING.** Only T2
   remains and T2 is carded and barred on this data. Read it for measurements, not for a to-do list.
6. `REG-012` §§6–7 · `RESULT-REG-012-band-edge-phase` §§4–5 (the refusal speech act `-44` put a
   machine on) · `RESULT-TERM-001` the five-site ruling · `REG-010` **§1 is the population ruling**
   · `CONSTRUCTION-REG-010` **§C2 owns 55.71 % and its population in one sentence**.
7. `RESULT-REG-010` §3 → §4 · **`RESULT-TERM-002`** §2 before §8 · `RESULT-PIN-001` ·
   `RESULT-SCOPE-001` · `CONSTRUCTION-REG-009` (**R5 is load-bearing and unspent**) ·
   `RESULT-REG-009` (**§3's S = 0.1391 is load-bearing in a test**) · `REG-009` (**READ THE HEADER
   NOTE FIRST**; numbering 6–12 by ruling).

> **`-44` in one line: A COLUMN THAT NAMES A GUARD IS A COVERAGE CLAIM, AND NOBODY HAD EVER
> VERIFIED A SINGLE ROW OF IT.**
> `-43` closed with *"cell (b) — a machine could recognise this and nobody wrote one — is now
> EMPTY and that is the finding to protect."* Protecting a finding means testing it. **It did not
> survive.** The emptiness rested on the inventory's `machine` column being read as coverage;
> audited one row at a time against *"if the constraint were violated, would this named test
> necessarily go RED?"*, the eighteen incidental entries came back **2 BINDS · 6 PARTIAL · 10
> ADJACENT**. **Cell (b) holds thirty-three of the fifty.** And §2's *"nine of the fifty already
> had a machine"* was itself wrong — **twenty-four rows name one** — a count of a column in that
> file, in prose, that nobody had recomputed in two sessions.

---

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-44`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.
`darlish-check` is **not** in the cloud kit — do not chase its 127.

**`--replaces` verified again in `-44`**: `roster join --replaces cloud-<fp>` printed `absorbed 1
row(s)`. `roster leave` ONCE at wrap.

> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
> dx spawns a **fresh remote shell per call and carries no environment**. `-44` used the inline
> form on `roster join`, `roster claim`, both commits, `lessons.py use`, `lessons.py add`,
> `record-outcome` and `gate-selfcheck.sh` — every one first time.

> ### ⚠ NEW · `git commit -F <msg> <paths>` CANNOT STAGE AN UNTRACKED FILE.
> The stanza every handoff since `-40` carries is the *second* half of the move. A new test file
> is untracked, and `git commit -F msg tests/test_new.py` dies with **`error: pathspec ... did not
> match any file(s) known to git`** before the brake is even consulted. `-44` lost a round-trip to
> it. The whole move, on a shared repo:
>
> ```
> /tmp/dx 'cd ~/repos/<repo> && git status --porcelain'                 # look FIRST
> /tmp/dx 'cd ~/repos/<repo> && git add <only your new paths>'          # never -A, never .
> /tmp/dx 'cd ~/repos/<repo> && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -F /tmp/msg.txt <all your paths, new AND modified>'
> ```
> **`<n>` is the count of YOUR paths, not the staged total.** `-44`'s were 4 and 10.

**COMMIT BY PATH ON `claude-blackbook`, ALWAYS — CONFIRMED AGAIN.** `-44` found **fifteen** staged
leaves and **five were a sibling's** (acmeLedger's firewall / cmd-log / containerizing /
producer-reader / ufw leaves). `git commit -F msg <paths>` took the ten that were mine and left
theirs. **`lessons.py` auto-commit is still blocked by the roster brake and still reports you as
`cloud-<fp>`** — cosmetic, the leaf files are written, you commit them yourself. **Check the diff
for `used_by` before committing**: a `use` shows `used_by: [.., wealthTensor-NN]` and a
`record-outcome` shows `passes` and possibly `trust: quarantine -> active`.

**THE MINUTE-TWO STANZA IS TWO LINES, AND YOU NEED BOTH TARBALLS.**

```
/tmp/dx 'cd ~/repos/wealth-tensor && tar czf /tmp/wt-lite.tgz docs scripts tests src && tar czf /tmp/wt-data.tgz data'
/tmp/dx --get /tmp/wt-lite.tgz /tmp/wt-lite.tgz && /tmp/dx --get /tmp/wt-data.tgz /tmp/wt-data.tgz
```

`-44` measured 2,421,423 + 4,682,860 bytes, both `verified against darwin` **in words**. Trust the
sentence. **Exit 3** = never reached darwin, safe to re-run · **4** = dropped after the command
started, check state first · **5** = crossed but mismatched, nothing written, replay-safe.
**`$HOME` in the cloud container is `/root`, not `/home/claude`** — `~/wt` resolves to `/root/wt`
and the Read tool wants the absolute path. **Never inline a multi-line string in `dx '...'`** —
write locally, `--put`, run it; `-44` ran its lessons bank and both commit messages that way.

**SUITE COUNTS — COLLECTED = PASSED + SKIPPED, NOT TWO PASS COUNTS.**

| | at `a77c5c5` (verified in `-44`, both machines, same hour) |
|---|---|
| collected | **944** |
| cloud (`PYTHONPATH=<root>/src`) | **935 passed / 9 skipped**, ~164 s, **every skip `not a git work tree`** |
| darwin (`.venv/bin/python -m pytest`) | **944 passed**, ~60 s |

`scripts/defensive_count.py` **takes a positional `path`** and errors without one:
`python3 scripts/defensive_count.py docs/papers/paper-III-dual-tensor/paper-III.md`.

---

## 0 · THE TELL, NOW IN THIRTY-SIX SHAPES

Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL GONE QUIET (`-32`). `-33`: instruments that agree with themselves; a
guard must scan assertions, not quotations. `-34`: defects nobody introduced. `-35`: defects you are
about to introduce. `-36`: pre-commit the FAVOURABLE outcome's meaning. `-37`: a mutation that does
not mutate reports your guard as weak. `-38`: a statistic can be a tautology in measurement's
clothing. `-39`: a handoff silently outranks a doctrine leaf; **assert the EXACT exit code**.
`-40`: a STALE NEGATIVE closes a question harder than an open one. `-41`: a hand-audit that found N
sites found them through ONE DOOR; a paragraph-resolution grade against a sentence rule is a FALSE
GREEN. `-42`: a constraint can be CONDITIONAL and its guard must assert its ANTECEDENT; a
whitespace-identity guard certifies no character moved, not no meaning; the second door is the
SECTION HEADING; evidence in a gitignored file is not in the SSOT. `-43`: a labelling constraint's
second door is the WRONG label; a repair that is the defect's token with a prefix matches every
substring check; **feed the registration its own forbidden claim before you trust the green**; a
non-vacuity test must assert the CONJUNCTION. **`-44` adds three:**

- **A COLUMN THAT NAMES A GUARD IS A COVERAGE CLAIM, AND NOBODY EVER VERIFIES IT.** Eighteen rows
  of `CONSTRAINT-INVENTORY-001` said *"incidental — the test was written for a prediction and
  happens to bind the constraint too."* That phrase had never been checked for a single row.
  Audited against one question — *would this test go RED if the constraint were violated?* — the
  eighteen came back **2 BINDS / 6 PARTIAL / 10 ADJACENT**, and one named the wrong test entirely.
  **THE PATTERN IS NOT RANDOM: THE REPRODUCED NUMBERS BIND, THE PROHIBITIONS ESCAPE.** A test
  written for a prediction opens the data artifact; a constraint on *how a thing may be reported*
  lives in prose the test never reads — **of twelve distinct incidental test files, three open a
  `.md` at all**, and two of those only to check a numeral appears somewhere in it. The audit is
  cheap and parallel: one reader per test, a mutation on a scratch copy as the tiebreak.
  Banked: `2026-08-14-column-names-guard-coverage-claim-nobody`.
- **WHEN A RULE SAYS "X, NOT MERELY Y", AN ABSENCE GUARD IS LOGICALLY INCAPABLE OF ENFORCING IT —
  BOTH STATES SHARE THE ABSENCE.** `REG-012` §7 requires the shifted band count to be *refused,
  not merely unperformed*. Its guard asserts the document names no way of computing one — a
  strong, un-gameable **absence**, with the same truth value in the compliant world and the
  violating one. Deleting every refusal sentence from the RESULT left the suite green. The repair
  is a **pair**, not a better absence: presence of the declaration, in the document's own voice
  (blockquotes excluded — reporting a prohibition is not performing a refusal), naming its
  warrant. Generalises to *disclosed not omitted*, *declined not overlooked*, *deprecated not
  deleted*. Banked: `2026-08-14-rule-says-x-merely-y-absence`.
- **AN UNRECOGNISABLE CONSTRAINT GETS A MACHINE ON ITS ANTECEDENT AND A HUMAN ON ITS CONSEQUENT —
  A TRIPWIRE, NOT A GUARD.** Same mechanism, opposite speech act: it fires on a checkable
  antecedent and says *a human must read this*, not *this is wrong*. **A tripwire whose red
  message names a violation teaches the next session to suppress it.** The corollary is how the
  gap hid for two sessions: **do not fuse a property of the artefact with a property of the estate
  into one partition.** `-43`'s three cells were *has a machine / could have one / reader only* —
  the first is about who did work, the third about what is knowable — and the fusion left no cell
  for *a machine is named and cannot see the constraint*, which is where sixteen rows lived.
  Banked: `2026-08-14-constraint-machine-cannot-recognise-machine-its`.

**Everything `-33` through `-43` banked is unchanged and still sharp.** `severity.check`'s witness
must return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory
(`-44` checked; all three new names were free). `patchkit` anchors have **no internal newline**.

---

## 1 · WHAT HAPPENED

**`a77c5c5` — the recognisability partition, and the audit that inverted `-43`'s headline.**

- **`docs/preregistration/CONSTRAINT-INVENTORY-001.md`** — two axes where there was one. §1's table
  carries `recog` beside a binding grade; **§2a is a machine-readable counts block**; **§3 is the
  partition, the audit, cell (b) ranked eight-deep, and §3.3's adjacent check named for each
  reader-only constraint**; **§3.4 is what an unrecognisable constraint gets instead of a machine**
  — a ruling, Jason's call, or a tripwire, with the three tripwires the estate owes (C09, C17,
  C36) named. §3.0 preserves `-43`'s list verbatim.
- **The four cells**, where `-43` had three: **10 bound** (7 written FOR the constraint, 3
  incidental and genuinely binding) · **33 in cell (b)**, sixteen of which *name a machine that
  does not bind* · **3 reader-only** (C05, C18, C36) · **4 not live**.
- **Pointer defects, all corrected in the table.** C40 named the wrong test entirely
  (`test_term002_count.py` is about §8's free-parameter numeral and never opens §4.7 or the
  strings 151/98/55/38; the real binder is `test_reg012_sec6_sec47_frozen.py`'s §4.7 freeze).
  C42's two named tests pin **three of its fifteen** frozen numbers. C47 and C50 cited the wrong
  section. **C07's own test docstring says it cannot see the thing C07 forbids** — the row
  inherited the file because the names rhymed.
- **`scripts/wt111_inventory_recognisability.py`** reproduces the graded file **byte-for-byte**
  from the pre-edit copy, verified.

**Two new guards:**

| guard | what goes red |
|---|---|
| `tests/test_reg012_sec7_refusal_is_asserted.py` (9 tests) | the C49 repair. The **presence** limb of a pair: the refusal must be declared in the document's own voice and name R5. **Red on the merely-unperformed document, with the old absence guard green on it** — which is the demonstration, not the assertion. Carries a LOST WARRANT branch if `REG-012` §7 drops the sentence. |
| `tests/test_constraint_inventory_selfconsistent.py` (12 tests) | the inventory counts itself: header-and-cell alignment, C01–C50 contiguous, grade ⟺ pointer, every named machine exists on disk, `n/a` ⟺ not live, and §2a against §1. Six mutation controls, each firing on its own defect. |

**Two defects this pass introduced and caught** (the `-35` tell, on itself): `wt111`'s first cut
announced `recog` in the header **one position left of where it inserted the cells** — fifty rows
misaligned, table still rendering, caught by recomputing counts rather than by reading it. And the
self-check's pointer regex was `[a-z0-9_]`-only, so a `..._OLD.py` rename **failed to match at all**
and the grade-agreement test fired instead, blaming the wrong thing — *a pointer regex narrower than
the filenames it must catch reports the WRONG defect, which is worse than reporting none.* Both are
now assertions in the file.

| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** — the manuscript was not touched this session. Evidence: `DEFENSIVE-BASELINE.json` + `tests/test_defensive_count.py`, both in the SSOT (`-42`'s bug-spray tell honoured) |
| **G-COACH-1** | held — every weakness named shipped a repair: C49 REPAIRED in-session, the other fifteen re-graded honestly and ranked, four pointer defects corrected |
| **G-COACH-5** | held — the strength named is **`REG-012` §5's own defence of its absence guard**: *"an absence is the only assertion a short list cannot satisfy."* That is exactly right about the limb it defends, and writing it down is what made the OTHER limb visible. A document that argues for its own guard is auditable; one that just asserts coverage is not. |
| suite | **944 collected** · darwin **944 passed** (~60 s) · cloud **935 passed / 9 skipped** (~164 s) |
| new tests | 2 files, 21 tests |
| lessons | **three** banked global · **seven** used and corroborated `record-outcome wealthTensor-44 pass` |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-43`'s rulings stand **verbatim**: no third disclosure instrument; phrase
  set frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS THE *DISCLOSED* δ**; **REG-009 IS
  CLOSED, numbering 6–12**; **§4's COVERAGE SILENCE AND §7.5's TWO ERRATA STAY RECORDED, NOT
  REPAIRED**; **DO NOT SPEND THE TIE-BREAK**; **DO NOT PROMOTE `R_MIN`**; **SCOPE-001, PIN-001,
  TERM-001, TERM-002 ARE CLOSED**; **§11 PINS PER FILE**; **P3 FAILED AND REG-010 DID NOT RE-SCORE
  IT**; **REG-010's POPULATION IS Ψ's 683 PAIRS**; **NEITHER BANDING IS PROMOTED**; **R5 IS UNSPENT**;
  **REG-012 IS CLOSED ON BRANCH F**; **THE TWO SENSITIVITIES ARE SEPARATE**; **55.71 % IS Ψ's AND
  63.16 % IS THE BAND COUNT'S**; **`selected_lives` IS THE ONE SELECTION PATH**; **§4.4's TIER-0
  CALIBRATION CELL IS `0.3000`**; **T4's IDENTIFIED-SET WIDTH IS `31.7%`**; **`SCOUT-001` IS WORKED**;
  **T2 MAY NOT BE RUN ON THIS DATA** (carded `1217501628088122`); **THE SCOUTING REPORT'S TIMING IS
  CLAUDE'S CALL**; **"THE REGISTERED ADVERSE CUT" DOES NOT RETURN AT ANY SITE**; **§4.7 IS PINNED AT
  `ba59370`**; **§9's LIMITATIONS ARE FOUR LIST ITEMS AND STAY FOUR**; **`wt107` IS NOT EDITED**;
  **THE `.bak` COPIES ARE GITIGNORED — CITE THE TEST, NOT THE BACKUP**; **`RESULT-REG-003` §2's
  "EVERY CUT LANDS IN R1" IS TEED UP, NOT REPAIRED** (carded `1217518687033967`).
- **NEW · THE `machine` COLUMN IS NOT A COVERAGE COLUMN AND MAY NOT BE READ AS ONE.** A row's grade
  is **FOR / BINDS / PARTIAL / ADJACENT**, and only the first two mean the constraint is guarded. A
  session adding a machine adds its grade **in the same commit**, and
  `test_constraint_inventory_selfconsistent.py` refuses a pointer without a grade or a grade
  without a pointer. **Do not re-derive the counts in prose** — §2a is the counts block and the
  test binds it to the table.
- **NEW · CELL (b) IS THIRTY-THREE AND THAT IS A RANKING, NOT A BACKLOG.** §3.2 orders eight by
  cost×cheapness. Nothing in cell (b) is a live defect: **every one of the fifty is compliant or
  not live at `a77c5c5`** — what is missing is the machine, not the compliance. Building one is
  never urgent and is often the cheapest real work available.
- **NEW · C49's GUARD IS A PAIR AND BOTH HALVES ARE LOAD-BEARING.**
  `test_reg012_sec7_refusal_is_asserted.py` asserts the *other* file still contains
  `assert not _threshold_reads(doc)`. Tidying either file alone breaks the constraint silently.
- **NEW · `RESULT-REG-012-band-edge-phase.md`'s REFUSAL SENTENCES ARE NOW LOAD-BEARING TEXT.**
  §4's *"Branch F does not license the measurement it makes tempting"* and §5's *"refused rather
  than merely unperformed"* are asserted by a test. Rewording is allowed; deleting is a red suite.

---

## 3 · THE AT-BAT for `-45` — **build the tripwire the estate keeps describing.**

§3.4 names three tripwires the estate owes and has never built. **C09 is the one to build**, and
it is the highest-value hour on the board because it is the only place where a *closest-call*
compliance verdict is protected by nothing at all:

> `REG-002` E1 fired — δ₃\* = 0.0079 < 0.010 — so **§4.4 may not report τ = −1 as the section's
> headline.** It currently does not: §4.4 is *titled* for the validity region and the knife-edge is
> one bolded paragraph lead inside it. §2's own bullet calls this **the closest call in the table**
> and says it is *"worth re-reading the moment §4.4 is re-headlined or the knife-edge is promoted
> into the abstract's lead."* **That sentence is a tripwire specification and nobody built it.**

The shape, and the thing that makes it a tripwire rather than a guard:

1. **Two machine-checkable antecedents.** §4.4's `##` title, pinned; and the knife-edge's numeral
   or phrase entering the abstract's lead. Neither is the constraint — *headline* is a reader's
   judgement — and the file must say so in its docstring, at the scene.
2. **The red message names a RE-READ, not a violation.** *"§4.4 was re-headlined — read it against
   `REG-002` E1, which fired. This is not a failure."* Get this wrong and the next session learns
   to re-pin without reading, which is the failure mode `-43` called out for C48's freeze.
3. **Then C17 and C36**, which are the same shape: C17 freezes §4.4's *argument* paragraphs the way
   C48 freezes §4.7 (a changed hash asks *did this reopen the argument?*); C36 watches §7's ledger
   shape, and if a column separating algebra rows from rows that risked something is ever added, or
   the row count moves, Jason's presentation judgement is live again and he is asked **once**.
4. **Register the class.** A tripwire is not a guard, and a suite that cannot tell them apart will
   eventually have one deleted as a false alarm. Whatever marks it — a `tripwire_` name prefix, a
   marker, a line in the inventory — decide it in `-45` while there is exactly one.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The obvious alternative is §3.2 item 1 —
**C42's fifteen frozen numbers**, twelve of them unpinned, one test, no judgement anywhere in it.
That is the cheapest real guard in the estate and a perfectly good session; it is second only
because C42's failure mode is *a number moves and nobody notices*, while C09's is *the paper's
closest compliance call quietly stops being true*.

**One warning from `-44`, and it cost the most time.** The audit's value came from **one question
asked identically of every row** — *would this test go red?* — not from reading the tests well.
Four parallel readers, each given the constraint's exact quotation and told to construct a
concrete surviving violation, produced a better result in twelve minutes than a careful sequential
read would have in an hour, **and the two that empirically injected their violation into a scratch
copy were the two whose findings needed no re-checking**. Make the mutation, not the argument.

---

## 4 · TEED UP, IN ORDER

1. **T2 is CARDED (`1217501628088122`) and MAY NOT BE RUN ON THIS DATA.**
2. **`RESULT-REG-003` §2's "Every cut lands in R1" — carded `1217518687033967`, State Machine.**
   Two readings; under one, 0.327 < 0.33 is R2 by the registration's own ladder. **A `RESULT-*` is
   the record of a run and editing the artefact edits the witness** — the `-37` precedent says the
   repair shape is a dated addendum. C12's guard is unaffected either way.
3. **NEW · cell (b), ranked in `CONSTRAINT-INVENTORY-001` §3.2.** C42's fifteen numbers · C07's
   amended-after-result git test · C26's *"never appears unqualified"* regex · the
   beside/never-promoted/does-not-re-score family (C44/C46/C41, one guard, three constraints) ·
   C10 (C21's exact shape, one document over) · the five-constraint forbidden-claim family ·
   C45's two assertions · the reportable-at-all presence guards.
4. **§7's ledger dilutes its own two load-bearing rows — Jason's call**, and it is inventory C36,
   which makes it the worked example for the tripwire class. **Do not card it; tripwire it.**
5. Infra siblings, carded, Claude-hands: concierge pinholes carry the same Caddy ordering defect
   `1217488447555628` · capability path in cleartext in n8n-stack + repo drift `1217488117177482`.
6. AAR A2's residual — the other four `post-*` hooks · card-lint `1217483699706758` · gate
   `1217465036940491`.
7. Dossier era, re-served by nobody: `REVIEW-004` **C6** (ASC 410) and **C10** (IAS 36's reversal
   asymmetry, a free cross-regime falsification test).
8. Phrase-set passenger: 30.4 % match only `events or circumstances`; 7.9 % safe-harbour. Outranked.
9. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
10. Not mine, not touched: handoff-lint warns `HANDOFF-acmeLedger-07.md:22`, `-09.md:36,42`, and
    `-12.md` / `-13.md` carry items with ZERO `verify:` lines.

---

## 5 · DO NOT

* Everything `-31`→`-43` forbade still stands verbatim — R5, the two sensitivities,
  `selected_lives`, §4.4's `0.3000`, T4's `31.7%`, the δ arm, TERM-001/002, the dossier era, §9's
  FOUR list items, `wt107` IS NOT EDITED, the gitignored `.bak`, **"THE REGISTERED ADVERSE CUT"
  DOES NOT RETURN**, **§4.7 IS PINNED AT `ba59370`**. §2.
* **NEW · DO NOT RE-GRADE A `machine` CELL WITHOUT DOING THE AUDIT.** The grades in §1 each cost a
  full read of the named test against the constraint's exact quotation. Upgrading ADJACENT →
  BINDS because a test *looks* related recreates the exact defect this session removed. The
  evidence for a BINDS is a mutation that goes red.
* **NEW · DO NOT DELETE THE REFUSAL SENTENCES FROM `RESULT-REG-012-band-edge-phase.md`**, and do
  not "simplify" `test_reg012_sec7_refusal_is_asserted.py` by folding it into the absence guard.
  The pair is the point.
* Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud.

---

## 6 · ORIENT-THEN-GO

Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.

Coffee status: ☕ **TEN SESSIONS RUNNING, AND THE FIRST TEN MINUTES DECIDED THE WHOLE SESSION
AGAIN** — `-35` truth, `-36` population, `-37` count, `-38` premise-and-instrument, `-39` severity,
`-40` the promise the document made about itself, `-41` the resolution it was written at, `-42`
whether it was in force, `-43` who the promise was made about, **`-44` WHETHER THE THING GUARDING
IT CAN SEE IT.** The entire `-44` finding came from parsing the inventory's own table to count a
column the prose had already counted, and getting a different number. One script, ninety seconds.
**Spend the ten minutes, and spend them recomputing something the document already tells you.**
