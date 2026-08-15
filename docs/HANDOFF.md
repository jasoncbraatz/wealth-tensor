---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-15
session: wealthTensor-46
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
   ESTATE). **Read §2b first this time** — it is `-46`'s finding, and it is about this file's own
   prose. Then §3.2's opening note, then §3.1's PARTIAL block, then §2a's counts.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`python3 scripts/mutation_control.py --list`** — new in `-46`. The instrument that answers
   *what does the suite actually catch*. **Read its module docstring before you grade anything.**
5. **`docs/preregistration/REG-003` §§3.2, 3.3, 7** (`REG-003-p3-recognition-rate-and-off-diagonal.md`)
   — the four-regime ladder, the registered bias asymmetry, the rounding rule.
6. **`docs/scouting/SCOUT-001-paper-III-opposing-team.md`** — **WORKED, NOT PENDING.** Only T2
   remains and T2 is carded and barred on this data. Read it for measurements, not for a to-do list.
7. `REG-012` §§6–7 · `RESULT-REG-012-band-edge-phase` §§4–5 · `RESULT-TERM-001` the five-site
   ruling · `REG-010` **§1 is the population ruling, §4 is the freeze `-46` built** ·
   `CONSTRUCTION-REG-010` **§C2 owns 55.71 % and its population in one sentence**.
8. `RESULT-REG-010` §3 → §4 · **`RESULT-TERM-002`** §2 before §8 · `RESULT-PIN-001` ·
   `RESULT-SCOPE-001` · `CONSTRUCTION-REG-009` (**R5 is load-bearing and unspent**) ·
   `RESULT-REG-009` (**§3's S = 0.1391 is load-bearing in a test**) · `REG-009` (**READ THE HEADER
   NOTE FIRST**; numbering 6–12 by ruling).

> **`-46` in one line: THE AT-BAT'S OWN WARRANT WAS A COVERAGE CLAIM NOBODY HAD MEASURED, AND
> RUNNING THE CONTROL FIRST — EXACTLY AS THE TEE-UP INSTRUCTED — DESTROYED THE TEE-UP.**
> `CONSTRAINT-INVENTORY-001` §3.2 ranked C42 first in cell (b) for two sessions on the sentence
> *"twelve of fifteen unpinned"*, and the `-45` handoff carried it forward as the whole reason to
> build. Twenty-two mutations later: **nineteen were already caught.** Fourteen of the fifteen on
> the artifact side, four of seven on the prose side. The claim was true of the **two named files**
> and false of the **estate**, because the `machine` column names the tests written FOR a constraint
> and never the tests that happen to catch it — eight of C42's fifteen were held by
> `test_the_instrument_reruns_to_the_same_numbers`, which belongs in no row's `machine` cell.
> **This is the third session running that a coverage claim in this estate turned out to be
> unverified: `-44` the `machine` column, `-45` the `source` column, `-46` the inventory's own
> ranking prose.** The three genuinely unguarded probes — the 98 firms, the 110 and the 133 — are
> now guarded, and the tedious measurement is a committed script so the next session does not
> hand-roll it.

---

### Transport — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-46`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.
`darlish-check` is **not** in the cloud kit — do not chase its 127.
`roster leave` ONCE at wrap.

> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
> dx spawns a **fresh remote shell per call and carries no environment**. Inline on `roster join`,
> `roster claim`, the commit, and every `lessons.py` call — first time, every time.
> **Exception: `export GATE_ROSTER_WHO=…` DOES work inside a script you `--put` and run with
> `bash /tmp/x.sh`**, because that is one shell.
> ### ⚠ `roster claim` TAKES `--resource`, NOT `--repo`.
> `-46` lost a call to `--repo` (exit 2, clean usage message). The full move:
> `roster claim --who <who> --resource <repo> --task "<what>"`. `roster join` takes `--who/--task`.
> ### ⚠ `git commit -F <msg> <paths>` CANNOT STAGE AN UNTRACKED FILE.
> Look, add, then commit — the whole move on a shared repo:
>
> ```
> /tmp/dx 'cd ~/repos/<repo> && git status --porcelain'                 # look FIRST
> /tmp/dx 'cd ~/repos/<repo> && git add <only your new paths>'          # never -A, never .
> /tmp/dx 'cd ~/repos/<repo> && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -F /tmp/msg.txt <all your paths, new AND modified>'
> ```
> **`<n>` is the count of YOUR paths, not the staged total.** `-46`'s was 4.

**COMMIT BY PATH ON `claude-blackbook`, ALWAYS.** `git status --porcelain` first; if a sibling's
leaves are staged, commit by path.

**THE MINUTE-TWO STANZA IS TWO LINES, AND YOU NEED BOTH TARBALLS.**

```
/tmp/dx 'cd ~/repos/wealth-tensor && tar czf /tmp/wt-lite.tgz docs scripts tests src && tar czf /tmp/wt-data.tgz data'
/tmp/dx --get /tmp/wt-lite.tgz /tmp/wt-lite.tgz && /tmp/dx --get /tmp/wt-data.tgz /tmp/wt-data.tgz
```

`-46` measured 2,514,127 + 4,682,858 bytes, both `verified against darwin` **in words**. Trust the
sentence. **Exit 3** = never reached darwin, safe to re-run · **4** = dropped after the command
started, check state first · **5** = crossed but mismatched, nothing written, replay-safe.
**`$HOME` in the cloud container is `/root`, not `/home/claude`** — unpack to `/root/wt` and give
the Read tool the absolute path. **Never inline a multi-line string in `dx '...'`** — write locally,
`--put`, run it.

> **`conftest.py`, `requirements.txt`, `README.md`, `LICENSE` and `.gitignore` ARE NOT IN THE
> TARBALL.** `-46` needed `conftest.py` (`/tmp/dx --get` it — 1,346 bytes) and `requirements.txt`
> (`numpy>=1.26 scipy>=1.11 pytest>=8.0`; `pip install --break-system-packages`). **Copy
> `conftest.py` into `/root/wt` before running pytest** or the `tripwire` marker is unregistered.
> A cloud container is **2 CPUs** — a full-suite mutation sweep is `--jobs 2` and takes ~2 min per
> probe. Budget for it: `-46`'s twenty-two probes were ~40 minutes of wall clock, and they were the
> session.

**SUITE COUNTS — COLLECTED = PASSED + SKIPPED, NOT TWO PASS COUNTS.**

| | at `HEAD` (verified in `-46`, both machines, same hour) |
|---|---|
| collected | **999** (was 976 at `19fa03f`; `-46` added 23) |
| cloud (`PYTHONPATH=<root>/src`) | **990 passed / 9 skipped**, ~118 s, **every skip `not a git work tree`** |
| darwin (`.venv/bin/python -m pytest`) | **999 passed**, ~61 s |

`scripts/defensive_count.py` **takes a positional `path`** and errors without one.
`pytest -m tripwire` selects the four-file tripwire class; `-m "not tripwire"` excludes it.

---

## 0 · THE TELL, NOW IN FORTY-TWO SHAPES

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
COVERAGE CLAIM and nobody ever verifies it; **the reproduced numbers bind, the prohibitions escape**;
an ABSENCE guard cannot enforce *X, not merely Y*; **do not fuse a property of the artefact with a
property of the estate into one partition.** `-45`: a `source` cell is a PROVENANCE claim and an
address that resolves is not an address that is right; when two items in one document constrain the
same thing, a citation to either reads as correct; a quotation is a lossy copy and the first things
it loses are the ANTECEDENT and the REFERENT. **`-46` adds three:**

- **A COVERAGE COUNT READ OFF THE `machine` COLUMN IS A CLAIM ABOUT THE COLUMN, NOT ABOUT THE
  SUITE.** `-44`'s lesson turned on the paragraph that states it. The column names the tests written
  FOR a constraint; the tests that *happen* to catch it are, by construction, never in it — and for
  C42 those were eight of fifteen. **The only instrument that measures coverage is a mutation with
  the whole suite behind it**, which is why `scripts/mutation_control.py` is committed rather than
  scratch. Banked: `2026-08-15-coverage-count-machine-column-claim-about-column`.
- **A REPRODUCIBILITY PIN IS NOT A FREEZE.** Two of C42's fifteen — `A` and `α̂` — were held by
  **nothing but** `test_the_instrument_reruns_to_the_same_numbers`, which regenerates the artifact
  and compares. That catches a hand-edit and is **blind to a number legitimately re-derived by a
  changed instrument**, which is the exact failure mode `REG-010` §4 names. You cannot see this from
  a red; you see it from the CATCHER LIST, which is why `mutation_control.py` prints every catcher
  and not the first. Banked: `2026-08-15-reproducibility-pin-is-not-a-freeze`.
- **THE NUMBER WITH NO ARTIFACT IS THE ONE THAT ESCAPES.** Fourteen of the fifteen live in a `.json`
  and were caught. **The 98 firms exists as a numeral in prose and nowhere else**, and it was the one
  green probe on the artifact axis. The repair is not to pin the string — it is to **recompute the
  quantity from the committed inputs and bind the prose to that**. Generalise: when a frozen list
  mixes recorded and unrecorded quantities, the unrecorded ones are where the guard is missing, and
  they are invisible to any audit that starts from `data/`. Banked:
  `2026-08-15-number-with-no-artifact-escapes`.

**Everything `-33` through `-45` banked is unchanged and still sharp.** `severity.check`'s witness
must return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory.
`patchkit` anchors have **no internal newline**.

---

## 1 · WHAT HAPPENED

**The control came first, and it is the deliverable.** Twenty-two forbidden moves, each on its own
scratch copy of the repo, each with the whole suite behind it:

| axis | probes | caught BEFORE `-46` | caught after |
|---|---|---|---|
| the fifteen moved in `data/` | 15 | **14** | 15 |
| the same numbers moved in `RESULT-*` PROSE ONLY | 7 | 4 | 7 |
| **total** | **22** | **19** | **22** |

The three that were green: **the 98 firms, the 110, the 133** — all three in the band-count
documents, which no reproducibility test regenerates.

**Two new files, 23 tests, green on both machines.**

| file | what it is |
|---|---|
| `tests/test_reg010_sec4_frozen_numbers.py` (23) | C42. §4's sentence pinned verbatim · the fifteen frozen as LITERALS at every artifact site · the document side bound by anchors **built from the artifacts, never retyped** · the 98 recomputed from the filings through `reg009_band_count`'s pure functions · one forbidden move per number, each required to **name its own item** · a separate non-vacuity for the prose limb · `-42`'s antecedent asserted before anything is read |
| `scripts/mutation_control.py` | the control, committed. `--list`, `--only <slug>`, `--jobs`. Prints **every** catcher per probe, not the first, because that is how you tell a freeze from a reproducibility pin |

**Inventory edits:** C42 `PARTIAL` → **`FOR`** (graded on the mutation, per `-44`'s ruling) · §2a
counts `FOR` 7→8, `PARTIAL` 6→5 · §3's cross-table 10/33 → **11/32** · §3.2 renumbered to seven
items with a note that **every remaining position rests on an unmeasured claim of the same kind** ·
§3.1's PARTIAL block rewritten · **new §2b** carries the measurement.

**BUG SPRAY, found and fixed in-session:** §3.1 asserted that `RESULT-REG-009-band-count.md` *"can
be deleted outright … green"*. `-46`'s own guard made that false the moment it landed — the deletion
is now five reds. **Corrected in place, and the grades deliberately did NOT move**: an incidental red
is not coverage, which is the whole point of §3's two axes. The supersession-prose limb of C44/C46
is still unmeasured and is now the live half of §3.2's item 3.

| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** — the manuscript was not touched this session |
| **G-COACH-1** | held — the stale C44/C46 sentence was repaired in-session, not filed |
| **G-COACH-5** | held — the strength named is **`test_reg009_band_count.py`'s docstring**, which pins its counts *against the filings rather than against the run* and says why. That paragraph is what taught this session to recompute the 98 instead of pinning its string. **A guard that recomputes its subject outlives the artifact that recorded it.** |
| suite | **999 collected** · darwin **999 passed** (~61 s) · cloud **990 passed / 9 skipped** (~118 s) |
| new tests | 2 files, 23 tests |
| lessons | **three** banked global · **three** used and corroborated `record-outcome wealthTensor-46 pass` |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |

---

## 2 · RULINGS — DO NOT REOPEN

- All of `-31`'s through `-45`'s rulings stand **verbatim**: no third disclosure instrument; phrase
  set frozen at 38; §4.4 settled; **`SOURCE-001` IS FINISHED**; **THE ARM IS δ**; **§4.8 IS NOT THE
  COINCIDENCE ARGUMENT; §4.7 IS**; **EVERY P0 AND REG-009 NUMBER IS THE *DISCLOSED* δ**; **REG-009 IS
  CLOSED, numbering 6–12**; **§4's COVERAGE SILENCE AND §7.5's TWO ERRATA STAY RECORDED, NOT
  REPAIRED**; **DO NOT SPEND THE TIE-BREAK**; **DO NOT PROMOTE `R_MIN`**; **SCOPE-001, PIN-001,
  TERM-001, TERM-002 ARE CLOSED**; **§11 PINS PER FILE**; **P3 FAILED AND REG-010 DID NOT RE-SCORE
  IT**; **REG-010's POPULATION IS Ψ's 683 PAIRS**; **NEITHER BANDING IS PROMOTED**; **R5 IS UNSPENT**;
  **REG-012 IS CLOSED ON BRANCH F**; **THE TWO SENSITIVITIES ARE SEPARATE**; **55.71 % IS Ψ's AND
  63.16 % IS THE BAND COUNT'S**; **`selected_lives` IS THE ONE SELECTION PATH**; **§4.4's TIER-0
  CALIBRATION CELL IS `0.3000`**; **T4's IDENTIFIED-SET WIDTH IS `31.7%`**; **`SCOUT-001` IS WORKED**;
  **T2 MAY NOT BE RUN ON THIS DATA** (carded `1217501628088122`); **"THE REGISTERED ADVERSE CUT" DOES
  NOT RETURN AT ANY SITE**; **§4.7 IS PINNED AT `ba59370`**; **§9's LIMITATIONS ARE FOUR LIST ITEMS
  AND STAY FOUR**; **`wt107` IS NOT EDITED**; **THE `.bak` COPIES ARE GITIGNORED — CITE THE TEST, NOT
  THE BACKUP**; **`RESULT-REG-003` §2's "EVERY CUT LANDS IN R1" IS TEED UP, NOT REPAIRED** (carded
  `1217518687033967`); **THE `machine` COLUMN IS NOT A COVERAGE COLUMN**; **DO NOT RE-GRADE A
  `machine` CELL WITHOUT DOING THE AUDIT — THE EVIDENCE FOR A BINDS IS A MUTATION THAT GOES RED**;
  **C49's GUARD IS A PAIR**; **DO NOT DELETE THE REFUSAL SENTENCES FROM
  `RESULT-REG-012-band-edge-phase.md`**; **C09's WARRANT IS `REG-002` E2, NEVER E1**; **`TRIPWIRE` IS
  A GRADE AND IT IS NOT COVERAGE**; **A TRIPWIRE'S RED MESSAGE IS PART OF THE ARTEFACT**; **THE THREE
  TRIPWIRE PINS MOVE IN THE SAME COMMIT AS THE EDIT THAT MOVED THEM**.
- **NEW · §3.2's RANKING IS NOT EVIDENCE, AND `-46` PROVED IT ON ITS OWN TOP ITEM.** Every position
  in that list was assigned from the `machine` column. One was measured and it was wrong by eleven.
  **Do not build the next guard on a ranked position without running its probe first** — and the
  probe is now a two-minute call, so there is no excuse: `python3 scripts/mutation_control.py`.
- **NEW · C42's FIFTEEN ARE FROZEN AS LITERALS AND THE LITERALS STAY.** The document anchors are
  derived from the artifacts on purpose; the fifteen values are **not**, because a check that only
  asserts *the document agrees with the record* goes green when both move together (`-38`). If a
  registered re-run legitimately moves one of the fifteen, that is a `REG-010` §4 event and it wants
  a ruling, not a quiet edit to `PSI_CELL`.
- **NEW · THE PARSE OF §4 IS READING (A), AND IT IS WRITTEN DOWN.** `Ψ = 0.6586 and its clustered
  interval` is ONE item; `the 110 and the 133 of the band counts` is TWO. Reading (B) is the mirror
  and also gives fifteen. Both freeze the same sixteen quantities. **Do not "fix" the parse** — the
  file's docstring states it and `test_section_4_still_says_what_this_file_read` pins the sentence,
  so a reword is red under either reading.
- **NEW · AN INCIDENTAL RED IS NOT COVERAGE.** `test_reg010_sec4_frozen_numbers.py` makes deleting
  `RESULT-REG-009-band-count.md` red. That did **not** move C44's or C46's grade and must not be
  read as having done so.

---

## 3 · THE AT-BAT for `-47` — **measure §3.2's ranking, then build from the top of the MEASURED list.**

The tee-up `-46` inherited was wrong, and the reason it was wrong applies unchanged to the seven
positions left in `CONSTRAINT-INVENTORY-001` §3.2. **The instrument now exists and the sweep is the
at-bat.**

The shape:

1. **Write one probe per ranked position** into `scripts/mutation_control.py`'s `PROBES` — the
   forbidden move that constraint names, one move per probe. C07: amend a registration after its
   `RESULT-*` commit. C26: write *impairment* unqualified into `RESULT-REG-006`. C44/C46/C41: the
   **supersession prose** limb, which `-46` explicitly left unmeasured. C10: label the re-ask `E4`.
   C16/C20/C23/C25/C30: assert each registration's own forbidden claim. C45: promote `R_MIN`.
   C01–C04/C06: delete the reportable-at-all disclosure.
2. **Run the sweep** (`--jobs 2`, ~2 min per probe) and **record the catcher list, not just the
   colour** — a probe whose only catcher reruns an instrument is a reproducibility pin, not a guard,
   and that distinction is invisible in a pass/fail column.
3. **Rewrite §3.2 from the measurement**, and say in the file how many positions the measurement
   moved. If the answer is *none moved*, that is a celebrated result and it is worth the sweep.
4. **Then build the top of the measured list**, with its own non-vacuity, as `-45` and `-46` did.

**Why this and not another guard.** `-44`, `-45` and `-46` each found one unverified claim and each
repaired it one row at a time. The pattern is now three deep and the general form is visible: **this
estate's prose about itself is the least-audited surface it has.** A sweep converts the remaining
ranking from assertion into measurement in one pass, and every guard built afterwards starts from a
number instead of a sentence.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The obvious alternative is **C37's tripwire** —
`REG-009` §12's *"never by narration"*, teed up in `CONSTRAINT-INVENTORY-001` §3.3, the same shape as
`-45`'s three and about an hour. It is second because a fifth tripwire proves less than the sweep
does, and because the sweep is the thing that stops the next session inheriting a wrong warrant.

---

## 4 · TEED UP, IN ORDER

1. **T2 is CARDED (`1217501628088122`) and MAY NOT BE RUN ON THIS DATA.**
2. **`RESULT-REG-003` §2's "Every cut lands in R1" — carded `1217518687033967`, State Machine.**
   Two readings; under one, 0.327 < 0.33 is R2 by the registration's own ladder. **A `RESULT-*` is
   the record of a run and editing the artefact edits the witness** — the `-37` precedent says the
   repair shape is a dated addendum. C12's guard is unaffected either way.
3. **Cell (b), ranked in `CONSTRAINT-INVENTORY-001` §3.2 — SEVEN entries, and the ranking is
   unmeasured (§3 above).** C07's amended-after-result git test · C26's *"never appears in it
   unqualified"* regex · the beside/never-promoted/does-not-re-score family (C44/C46/C41, whose
   **deletion limb is now red and whose supersession limb is not**) · C10 (C21's exact shape, one
   document over) · the five-constraint forbidden-claim family · C45's two assertions · the
   reportable-at-all presence guards.
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

* Everything `-31`→`-45` forbade still stands verbatim — R5, the two sensitivities,
  `selected_lives`, §4.4's `0.3000`, T4's `31.7%`, the δ arm, TERM-001/002, the dossier era, §9's
  FOUR list items, `wt107` IS NOT EDITED, the gitignored `.bak`, **"THE REGISTERED ADVERSE CUT"
  DOES NOT RETURN**, **§4.7 IS PINNED AT `ba59370`**, **DO NOT "SIMPLIFY" A TRIPWIRE INTO A GUARD**,
  **DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION**, **DO NOT ASSUME THE CLOUD
  TARBALL IS THE REPO**. §2.
* **NEW · DO NOT GRADE A CONSTRAINT FROM THE `machine` COLUMN, INCLUDING WHEN YOU ARE ONLY
  *RANKING*.** `-44` made this a ruling for grades; `-46` found the ranking prose doing the same
  thing one paragraph away from the ruling that forbids it. Ranking is grading.
* **NEW · DO NOT DELETE `PSI_CELL`, `S_R_MID`, `PSI_RECT`, `ALPHA_HAT*`, `VERDICTS`,
  `REG_009_NUMBERING`, `EVENTS_TOTAL`, `FIRMS`, `JOINABLE_*` AND LEAVE THE DERIVED ANCHORS.** That
  turns a freeze into a consistency check and it goes green on a re-run that moved everything.
* **NEW · DO NOT PIN THE 98 AS A STRING.** It is recomputed from the filings on purpose. A string
  pin would survive the filings changing, which is the one thing worth catching.
* Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud.

---

## 6 · ORIENT-THEN-GO

Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.

Coffee status: ☕ **TWELVE SESSIONS RUNNING, AND THE FIRST TEN MINUTES DECIDED THE WHOLE SESSION
AGAIN** — `-35` truth, `-36` population, `-37` count, `-38` premise-and-instrument, `-39` severity,
`-40` the promise the document made about itself, `-41` the resolution it was written at, `-42`
whether it was in force, `-43` who the promise was made about, `-44` whether the thing guarding it
can see it, `-45` whether the address on it was right, **`-46` WHETHER THE SENTENCE THAT SENT YOU
HERE WAS EVER CHECKED.** `-45`'s came from opening the section a row said it was quoting. `-46`'s
came from doing what the handoff told it to do — run the control first — and reading the answer
instead of the instruction. **The tee-up is not evidence. Spend the ten minutes measuring the thing
the last session was sure of.**
