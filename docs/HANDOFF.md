---
project: wealth-tensor
gh_sha: 19fa03f3965e7a012813d5396a288d99bc600616
updated: 2026-08-15
session: wealthTensor-45
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
2. **`docs/preregistration/CONSTRAINT-INVENTORY-001.md`** — the map for this thread. Fifty reporting
   constraints on two axes: `recog` (MECH / PROXY / READER / n/a — a property of the CONSTRAINT) and
   a **FOR / BINDS / PARTIAL / ADJACENT / TRIPWIRE** grade on the machine cell (a property of the
   ESTATE). **Read §3.4 first this time** — it is the tripwire class, now built rather than
   described. Then §2's provenance bullet (`-45`'s finding, six wrong rows) and §2a's counts block.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md` §§3.2, 3.3, 7** — the
   four-regime ladder, the registered bias asymmetry, the rounding rule.
5. **`docs/scouting/SCOUT-001-paper-III-opposing-team.md`** — **WORKED, NOT PENDING.** Only T2
   remains and T2 is carded and barred on this data. Read it for measurements, not for a to-do list.
6. `REG-012` §§6–7 · `RESULT-REG-012-band-edge-phase` §§4–5 · `RESULT-TERM-001` the five-site
   ruling · `REG-010` **§1 is the population ruling** · `CONSTRUCTION-REG-010` **§C2 owns 55.71 %
   and its population in one sentence**.
7. `RESULT-REG-010` §3 → §4 · **`RESULT-TERM-002`** §2 before §8 · `RESULT-PIN-001` ·
   `RESULT-SCOPE-001` · `CONSTRUCTION-REG-009` (**R5 is load-bearing and unspent**) ·
   `RESULT-REG-009` (**§3's S = 0.1391 is load-bearing in a test**) · `REG-009` (**READ THE HEADER
   NOTE FIRST**; numbering 6–12 by ruling).

> **`-45` in one line: THE CONSTRAINT THE WHOLE SESSION WAS BUILT AROUND HAD BEEN FILED UNDER THE
> WRONG FALSIFIER SINCE `-42`, AND EVERY CHECK ANYBODY WOULD THINK TO RUN CAME BACK GREEN.**
> C09's row, §2's bullet, §3.3, §3.4 and two handoffs all said `REG-002` **E1**. The clause they
> quote is **E2**'s. E2 is the one `RESULT-REG-002` §1 records as **FIRED** (δ₃\* = 0.00789 <
> 0.010); **E1 is the mean-τ falsifier that §2 of that same RESULT records as MIS-SPECIFIED, and it
> did not fire.** The citation survived because *both* govern §4.4's headline, so *does E1 exist?*
> and *does E1 mention the headline?* both return yes to a wrong pointer. Audited across all fifty
> rows: **six wrong, in three shapes** — four wrong locators (C09, C33, C26, C27, C28), one
> paraphrase that dropped a conditional's **antecedent** (C05), one that dropped a **referent**
> (C26). All repaired, and mechanised so they cannot recur.

---

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-45`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.
`darlish-check` is **not** in the cloud kit — do not chase its 127.

**`--replaces` verified again in `-45`**: `roster join --replaces cloud-<fp>` printed `absorbed 1
row(s)`. `roster leave` ONCE at wrap.

> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
> dx spawns a **fresh remote shell per call and carries no environment**. `-45` used the inline form
> on `roster join`, `roster claim`, the commit, and every `lessons.py` call — first time, every time.
> **Exception, and it is worth knowing: `export GATE_ROSTER_WHO=…` DOES work inside a script you
> `--put` and run with `bash /tmp/x.sh`**, because that is one shell. `-45` banked four lessons and
> a `record-outcome` that way in a single call.

> ### ⚠ `git commit -F <msg> <paths>` CANNOT STAGE AN UNTRACKED FILE.
> Look, add, then commit — the whole move on a shared repo:
>
> ```
> /tmp/dx 'cd ~/repos/<repo> && git status --porcelain'                 # look FIRST
> /tmp/dx 'cd ~/repos/<repo> && git add <only your new paths>'          # never -A, never .
> /tmp/dx 'cd ~/repos/<repo> && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -F /tmp/msg.txt <all your paths, new AND modified>'
> ```
> **`<n>` is the count of YOUR paths, not the staged total.** `-45`'s was 7, first try.

**COMMIT BY PATH ON `claude-blackbook`, ALWAYS.** `-45` found the tree clean and `lessons.py`
auto-commit **working and pushing** — four `add`s, three `use`s and a `record-outcome` all
self-committed. Do not assume that; **`git status --porcelain` first**, and if a sibling's leaves
are staged, commit by path as `-44` had to.

**THE MINUTE-TWO STANZA IS TWO LINES, AND YOU NEED BOTH TARBALLS.**

```
/tmp/dx 'cd ~/repos/wealth-tensor && tar czf /tmp/wt-lite.tgz docs scripts tests src && tar czf /tmp/wt-data.tgz data'
/tmp/dx --get /tmp/wt-lite.tgz /tmp/wt-lite.tgz && /tmp/dx --get /tmp/wt-data.tgz /tmp/wt-data.tgz
```

`-45` measured 2,452,442 + 4,682,860 bytes, both `verified against darwin` **in words**. Trust the
sentence. **Exit 3** = never reached darwin, safe to re-run · **4** = dropped after the command
started, check state first · **5** = crossed but mismatched, nothing written, replay-safe.
**`$HOME` in the cloud container is `/root`, not `/home/claude`** — unpack to `/root/wt` and give
the Read tool the absolute path. **Never inline a multi-line string in `dx '...'`** — write locally,
`--put`, run it.

> **`conftest.py`, `requirements.txt`, `README.md`, `LICENSE` and `.gitignore` ARE NOT IN THE
> TARBALL** and `-45` needed one of them. The stanza pulls `docs scripts tests src` + `data`, so a
> repo-root file is invisible in the cloud: `pytest` runs anyway (the cloud uses
> `PYTHONPATH=<root>/src` instead of conftest's `sys.path` insert), which is exactly why nobody
> noticed. If your at-bat touches pytest configuration, markers, or dependencies, `/tmp/dx --get`
> the file first — do not infer it from the suite passing.

**SUITE COUNTS — COLLECTED = PASSED + SKIPPED, NOT TWO PASS COUNTS.**

| | at `19fa03f` (verified in `-45`, both machines, same hour) |
|---|---|
| collected | **976** (was 944 at `a1fef70`; `-45` added 32) |
| cloud (`PYTHONPATH=<root>/src`) | **967 passed / 9 skipped**, ~135 s, **every skip `not a git work tree`** |
| darwin (`.venv/bin/python -m pytest`) | **976 passed**, ~59 s |

`scripts/defensive_count.py` **takes a positional `path`** and errors without one.
**New: `pytest -m tripwire` selects the four-file tripwire class; `-m "not tripwire"` excludes it.**

---

## 0 · THE TELL, NOW IN THIRTY-NINE SHAPES

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
second door is the WRONG label; **feed the registration its own forbidden claim before you trust the
green**; a non-vacuity test must assert the CONJUNCTION. `-44`: a column that names a guard is a
COVERAGE CLAIM and nobody ever verifies it — audit it with ONE question asked identically of every
row; **the reproduced numbers bind, the prohibitions escape**; when a rule says *X, not merely Y*, an
ABSENCE guard is logically incapable of enforcing it; an unrecognisable constraint gets a machine on
its ANTECEDENT and a human on its CONSEQUENT; **do not fuse a property of the artefact with a
property of the estate into one partition.** **`-45` adds three:**

- **A `source` CELL IS A PROVENANCE CLAIM, AND AN ADDRESS THAT RESOLVES IS NOT AN ADDRESS THAT IS
  RIGHT.** `-44`'s finding one column to the left, and it had the same shape: nobody had verified a
  single one. **Both** an existence check (*does E1 exist?*) **and** a whole-file search (*is this
  text in `REG-002`?*) pass a wrong citation. The question that catches it is *does the **cited
  block** contain the words in the **quotation column***, and it needs two things a looser check
  does not have: **resolve the exact block** (heading or bold label to the next peer, not the file),
  and **NEST multi-part locators** — `§4 Q1` means Q1 *inside* §4, and a union resolves it correctly
  whenever the label happens to be unique in the file, which is how C26, C27 and C28 pointed at the
  wrong section for four sessions. Also: compare the **conjunction** of a row's quotations. The
  first cut used `any`, and C05's paraphrase passed on the strength of a correctly-quoted fragment
  beside it. Banked: `2026-08-15-citation-column-provenance-claim-nobody`.
- **WHEN TWO ITEMS IN ONE DOCUMENT CONSTRAIN THE SAME THING, A CITATION TO EITHER READS AS CORRECT.**
  `REG-002` E1 and E2 both govern §4.4's headline, so the wrong one was **more** durable than an
  obviously-wrong one would have been — it passed every check a reader would think to run. This is
  the general case for any registration that pre-commits several ways to fail one section. The
  repair is to **assert the warrant at the scene**: the tripwire built this session asserts E2's
  clause *and* that `RESULT-REG-002`'s E2 row still reads FIRED. Banked:
  `2026-08-15-two-items-one-document-constrain-same`.
- **A QUOTATION IS A LOSSY COPY, AND THE FIRST THINGS IT LOSES ARE THE ANTECEDENT AND THE REFERENT.**
  Two of the six defects were not wrong addresses: C05's *"the next move is not a third instrument"*
  for *"the next move **in that case** is not…"* — dropping the conditional's antecedent, which
  turns a rule that fires only on failure into an unconditional ban — and C26's *"never appears
  unqualified"* for *"never appears **in it** unqualified"*, which turns a rule about one document's
  own statistics into a rule about the manuscript. `-42`'s rule has a twin: **a conditional
  constraint's QUOTATION must carry its antecedent.** Banked:
  `2026-08-15-quotation-lossy-copy-first-things`.

**Everything `-33` through `-44` banked is unchanged and still sharp.** `severity.check`'s witness
must return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory.
`patchkit` anchors have **no internal newline**.

---

## 1 · WHAT HAPPENED

**`19fa03f` — the tripwire class built and registered, and the source column audited.**

**Four new test files, 32 tests, all green on both machines.**

| file | what it is |
|---|---|
| `tests/test_tripwire_c09_sec44_headline.py` (8) | C09. §4.4's heading pinned byte-for-byte (**it is `###`, not the `##` two handoffs said**) and the knife-edge's paragraph position in the abstract pinned **as a floor** — earlier is promotion and fires, later or pushed down by an insert is not and does not. Asserts its own warrant: `REG-002` E2's clause **and** `RESULT-REG-002`'s E2 row still reading FIRED |
| `tests/test_tripwire_c17_sec44_argument.py` (6) | C17. **Not a freeze** — `REG-003` §7 *licenses* one number and the sentences carrying it, so a byte pin would go red every time the registration did what it registered. The pin is §4.4 with every numeric literal **masked** |
| `tests/test_tripwire_c36_sec7_ledger_shape.py` (7) | C36. §7's ledger column tuple and row count. **The prose said forty rows for two sessions; it is forty-seven** — corrected in three places. The red message says **ask Jason, once** |
| `tests/test_tripwire_class_is_registered.py` (11) | the class registrar. File name · `tripwire` marker (`conftest.py`) · `TRIPWIRE` grade in the inventory, bound in **both** directions, plus the SHAPE of every member's red message |

**And the provenance machine**, in `test_constraint_inventory_selfconsistent.py`:
`test_every_quoted_constraint_appears_in_its_cited_source` reads all fifty rows every run, plus
`test_the_unquoted_rows_are_the_pinned_four` (deleting a quotation is the cheapest way to silence
the check, so the set of describing-not-quoting rows is pinned) and a non-vacuity test that feeds it
the real defect — C09's quotation must be in E2 and **must not be** in E1.

**Six inventory rows repaired**: C09 `E1`→**E2** · C33 `§4`→**§3.1** · C26, C27, C28 `§4 Q1/Q2`→
**§3 Q1/Q2** · C05 and C26's quotations made verbatim.

| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** — the manuscript was not touched this session |
| **G-COACH-1** | held — six provenance defects found and **repaired in-session**, not filed; C37's tripwire teed up rather than half-built |
| **G-COACH-5** | held — the strength named is **`test_reg012_sec6_sec47_frozen.py`'s docstring**, which argues for its own design rather than asserting it (*"the pin records which version it froze"*). That paragraph is what taught this session that C09's tripwire had to assert its warrant. **A guard that argues is reusable; one that asserts is not.** |
| suite | **976 collected** · darwin **976 passed** (~59 s) · cloud **967 passed / 9 skipped** (~135 s) |
| new tests | 4 files, 32 tests |
| lessons | **four** banked global · **three** used and corroborated `record-outcome wealthTensor-45 pass` |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |

**Verification was empirical, not argued** (`-44`'s rule). Five mutations against the C09 tripwire
(re-headline · promotion into the abstract lead · warrant reworded · E2 no longer FIRED ·
knife-edge deleted from §4.4) and seven against the provenance check (each of the six real defects
re-injected, plus deleting a quotation to silence it): **every one RED on a scratch copy, unmutated
GREEN.**

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-44`'s rulings stand **verbatim**: no third disclosure instrument; phrase
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
  "EVERY CUT LANDS IN R1" IS TEED UP, NOT REPAIRED** (carded `1217518687033967`); **THE `machine`
  COLUMN IS NOT A COVERAGE COLUMN**; **DO NOT RE-GRADE A `machine` CELL WITHOUT DOING THE AUDIT —
  THE EVIDENCE FOR A BINDS IS A MUTATION THAT GOES RED**; **C49's GUARD IS A PAIR**; **DO NOT DELETE
  THE REFUSAL SENTENCES FROM `RESULT-REG-012-band-edge-phase.md`**.
- **NEW · C09's WARRANT IS `REG-002` E2. IT WAS NEVER E1.** E1 is the mean-τ falsifier
  `RESULT-REG-002` §2 records as **mis-specified**; it did not fire and its consequent was
  discharged by rewriting §4.4. Do not "restore" the E1 citation because older documents carry it —
  §2's ERRATUM in `RESULT-REG-002` is the record, and
  `test_every_quoted_constraint_appears_in_its_cited_source` now refuses it.
- **NEW · `TRIPWIRE` IS A GRADE AND IT IS NOT COVERAGE.** Only **FOR** and **BINDS** mean a
  constraint is guarded. `-45`'s three tripwires moved C09, C17 and C36 from `none` to `TRIPWIRE`
  and moved **none of them out of cell (b) or out of reader-only** — §3's cells are unchanged at
  **10 / 33 / 3 / 4**. `test_tripwire_class_is_registered.py` refuses any row carrying FOR or BINDS
  against a `test_tripwire_*` file.
- **NEW · A TRIPWIRE'S RED MESSAGE IS PART OF THE ARTEFACT AND IS ASSERTED.** Every member must be
  tagged `TRIPWIRE ·`, say **NOT A FAILURE**, and name what to read or whom to ask. Rewording is
  allowed; dropping any of the three is a red suite. A tripwire whose red names a violation teaches
  the next session to suppress it.
- **NEW · THE THREE TRIPWIRE PINS MOVE IN THE SAME COMMIT AS THE EDIT THAT MOVED THEM**, with the
  reason in the commit message — `SEC_44_HEADING`, `KNIFE_EDGE_ABSTRACT_PARAGRAPH`,
  `SEC_44_MASKED_SHA256`, `LEDGER_COLUMNS`, `LEDGER_ROWS`. A pin moved in a later commit is a pin
  nobody reviewed.

---

## 3 · THE AT-BAT for `-46` — **C42's fifteen frozen numbers.**

`CONSTRAINT-INVENTORY-001` §3.2 ranked cell (b) eight deep and C42 has been item 1 for two
sessions. It is now the top of the board on both halves of the ranking:

> `REG-010` §4 lists **fifteen numbers this may not move**. Its two named tests pin **three of
> them**. Moving Ψ, n, the distinct-pair count and **all four prediction verdicts** in
> `data/reg-009-result.json` leaves both named files green — the pins that catch those live in
> `test_reg009_ladder_inputs.py`, which the row did not name until `-44` corrected it.

**Why it is the at-bat and not a chore.** It is the cheapest real guard in the estate — one test,
fifteen assertions, **no judgement anywhere in it** — and its failure mode is the one this project
keeps re-discovering under different names: *a number moves and nobody notices*. `-45` just spent a
session proving that the estate's own prose counts drift silently (forty rows that were
forty-seven; nine machines that were twenty-four; an E1 that was an E2). Fifteen frozen numbers
with twelve unpinned is the same defect waiting in the one place where it would be load-bearing.

The shape, and the two traps:
1. **Read `REG-010` §4 and take the list verbatim.** Fifteen means fifteen; if the count you
   extract is not fifteen, that is the finding and you stop and say so.
2. **Assert the antecedent** (`-42`): §4's list is *"one new artifact, overwrites nothing"* — so
   the guard must also assert that the artifact `-31`'s numbers live in still exists and is the one
   being read. A freeze on numbers in a file that could be deleted is an absence guard (`-44`).
3. **Feed it its own forbidden move** (`-43`): mutate each of the fifteen on a scratch copy and
   require red. Twelve of them are currently unpinned, so **twelve of those mutations pass today** —
   run the control BEFORE you write the guard and record the number, because that measurement is
   the evidence the guard was needed.
4. **Do not re-grade C42's cell without the audit.** It is `PARTIAL` today and the grade moves to
   `FOR` only when a mutation goes red.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The obvious alternative is **C37's tripwire** —
`REG-009` §12's *"never by narration"*, teed up in `CONSTRAINT-INVENTORY-001` §3.3, the same shape
as the three built this session and about an hour. It is second because the class now exists and a
fourth member proves less than the first three did, while C42 is fifteen unguarded load-bearing
numbers.

---

## 4 · TEED UP, IN ORDER

1. **T2 is CARDED (`1217501628088122`) and MAY NOT BE RUN ON THIS DATA.**
2. **`RESULT-REG-003` §2's "Every cut lands in R1" — carded `1217518687033967`, State Machine.**
   Two readings; under one, 0.327 < 0.33 is R2 by the registration's own ladder. **A `RESULT-*` is
   the record of a run and editing the artefact edits the witness** — the `-37` precedent says the
   repair shape is a dated addendum. C12's guard is unaffected either way.
3. **Cell (b), ranked in `CONSTRAINT-INVENTORY-001` §3.2**, C42 first (§3 above), then C07's
   amended-after-result git test · C26's *"never appears unqualified"* regex · the
   beside/never-promoted/does-not-re-score family (C44/C46/C41, one guard, three constraints) ·
   C10 (C21's exact shape, one document over) · the five-constraint forbidden-claim family ·
   C45's two assertions · the reportable-at-all presence guards.
4. **C37's tripwire** — `REG-009` §12's *"never by narration"*. §3.3 names the adjacent check: a
   numeral in `RESULT-REG-009`'s attribution paragraph. Same shape as `-45`'s three.
5. **§7's ledger dilutes its own two load-bearing rows — Jason's call, and it is TRIPWIRED, not
   carded.** `test_tripwire_c36_sec7_ledger_shape.py` will ask him the moment the shape moves. **Do
   not card it and do not ask him pre-emptively.**
6. Infra siblings, carded, Claude-hands: Caddy ordering `1217488447555628` · capability path in
   cleartext + repo drift `1217488117177482`.
7. AAR A2's residual — the other four `post-*` hooks · card-lint `1217483699706758` · gate
   `1217465036940491`.
8. Dossier era, re-served by nobody: `REVIEW-004` **C6** (ASC 410) and **C10** (IAS 36's reversal
   asymmetry, a free cross-regime falsification test).
9. Phrase-set passenger: 30.4 % match only `events or circumstances`; 7.9 % safe-harbour. Outranked.
10. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
11. Not mine, not touched: handoff-lint warns `HANDOFF-acmeLedger-07.md:22`, `-09.md:36,42`, and
    `-12.md` / `-13.md` carry items with ZERO `verify:` lines.

---

## 5 · DO NOT

* Everything `-31`→`-44` forbade still stands verbatim — R5, the two sensitivities,
  `selected_lives`, §4.4's `0.3000`, T4's `31.7%`, the δ arm, TERM-001/002, the dossier era, §9's
  FOUR list items, `wt107` IS NOT EDITED, the gitignored `.bak`, **"THE REGISTERED ADVERSE CUT"
  DOES NOT RETURN**, **§4.7 IS PINNED AT `ba59370`**. §2.
* **NEW · DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD.** Each of the three had a cheaper, wronger
  version available — byte-freeze §4.4, fire on any abstract edit, count §7's rows and grade them —
  and **each of those would be green today and deleted within three sessions.** In particular:
  `KNIFE_EDGE_ABSTRACT_PARAGRAPH` is a **floor, not an equality** (later is not promotion), and
  C17's digest is **numeral-masked on purpose** (`REG-003` §7 licenses the number).
* **NEW · DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION.** It is the cheapest
  silencing move available and `test_the_unquoted_rows_are_the_pinned_four` refuses it. Three
  readings of a red are in the assertion message; only one of them is a typo.
* **NEW · DO NOT ASSUME THE CLOUD TARBALL IS THE REPO.** `conftest.py`, `requirements.txt`,
  `README.md`, `LICENSE` and `.gitignore` are outside `docs scripts tests src data`.
* Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud.

---

## 6 · ORIENT-THEN-GO

Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.

Coffee status: ☕ **ELEVEN SESSIONS RUNNING, AND THE FIRST TEN MINUTES DECIDED THE WHOLE SESSION
AGAIN** — `-35` truth, `-36` population, `-37` count, `-38` premise-and-instrument, `-39` severity,
`-40` the promise the document made about itself, `-41` the resolution it was written at, `-42`
whether it was in force, `-43` who the promise was made about, `-44` whether the thing guarding it
can see it, **`-45` WHETHER THE ADDRESS ON IT WAS RIGHT.** `-44`'s finding came from parsing a table
to count a column the prose had already counted. `-45`'s came from opening the section a row said it
was quoting, and reading it. Ninety seconds, and it moved the whole session's warrant. **Spend the
ten minutes, and spend them checking something the document has already told you twice.**
