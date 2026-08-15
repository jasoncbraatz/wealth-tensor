---
project: wealth-tensor
gh_sha: 11b3b10b67418c3a5e9c0b5544d5bbf69a2e22d3
updated: 2026-08-15
session: wealthTensor-49
gate_passed: true
gate_version: "2.53"
---
# wealth-tensor — HANDOFF
*`gh_sha` points at the commit this file describes; the only thing added after it is this file, so
`--check` prints `ADVISORY: docs-only drift` and exits 0. **Read the exit code, and assert it
exactly (`-39`) — `| tail` will mask it.***
## ORIENT — read these first, in this order
1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff, any
   result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the other
   thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. **`docs/preregistration/CONSTRAINT-INVENTORY-001.md`** — the map for this thread. Fifty reporting
   constraints on two axes: `recog` (MECH / PROXY / READER / n/a — a property of the CONSTRAINT) and
   a **FOR / BINDS / PARTIAL / ADJACENT / TRIPWIRE** grade on the machine cell (a property of the
   ESTATE). **Read §2e first this time** — it is `-49`'s finding, and the paragraph about the two
   discriminators is the one that matters. Then §2d (`-48`), then §2c (`-47`'s measurement, still
   the warrant for the ranking), then §3.2, then §2a's counts.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`python3 scripts/mutation_control.py --list`** — **45 probes now** (42 at `-48`; `-49` added
   `R3d`/`R3e`/`R3f`). **Read its module docstring before you grade anything**, including `-47`'s
   section on why `.git` is opt-in.
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
> **`-49` in one line: THE TEE-UP NAMED ONE PREDICATE, AND THE ONE PREDICATE IS RED ON ALL THREE
> COMPLIANT DOCUMENTS.**
> `-48` teed up the C44/C46/C41 family with a shape: *"assert both documents exist and that the
> later one carries no supersession claim."* That is one scanner, and it fails on every witness it
> governs. C44's document uses *replace* and *supersede* three times **lawfully**, because each
> verb's object is something else — a bracket, a manuscript conditional, a hedge; the discriminator
> is the **REFERENT** (`-45`). C46's and C41's document names the mirror and names P3 **in order to
> refuse them** — *"The mirror is not promoted, under this outcome or any other."* — so a referent
> test cannot tell a refusal from an assertion; the discriminator there is the **POLARITY**. One
> prohibition, three artefacts, **two machines**. **Six sessions running, the thing that did not
> survive checking was the estate's prose about itself**: `-44` the `machine` column, `-45` the
> `source` column, `-46` the ranking prose, `-47` the harness AND the DO-NOT list, `-48` the
> tee-up's reading of its document, `-49` the tee-up's *design* for a guard it had not tried.
> C44, C46 and C41 are **BUILT** and all three grade **FOR**, one catcher each.
---
### Transport — darlish, zero-bridge
Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-49`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.
`darlish-check` is **not** in the cloud kit — do not chase its 127.
`roster leave` ONCE at wrap.
> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
> dx spawns a **fresh remote shell per call and carries no environment**. Inline on `roster join`,
> `roster claim`, the commit, and every `lessons.py` call — first time, every time.
> **Exception: `export GATE_ROSTER_WHO=…` DOES work inside a script you `--put` and run with
> `bash /tmp/x.sh`**, because that is one shell. `-47`, `-48` and `-49` all ran their `lessons.py`
> calls that way. The roster brake still prints the **absorbed** row name (`cloud-…`) in its `you:`
> line; cosmetic, not a mis-identity.
> ### ⚠ `roster claim` TAKES `--resource`, NOT `--repo`. `record-outcome` TAKES NO `--id`.
> `roster claim --who <who> --resource <repo> --task "<what>"`; `roster join` takes `--who/--task`.
> **`lessons.py record-outcome <task-tag> pass` is TWO positional args and nothing else.** One call
> resolves every leaf you marked with `use --task <tag>`.
> ### ⚠ `lessons.py`'s AUTO-COMMIT IS BLOCKED BY THE ROSTER BRAKE **ONLY WHEN A SIBLING HOLDS THE
> REPO — `-49` HIT NO BRAKE AND EVERYTHING SELF-COMMITTED, INCLUDING `record-outcome`.**
> `-48` had to finish `record-outcome` by hand; `-49` did not. **So do not pre-emptively hand-commit
> — LOOK first**, because a hand-commit of already-committed leaves is a no-op that reads like a
> problem. The check is one call and it is the whole procedure:
>
> ```
> /tmp/dx 'cd ~/repos/claude-blackbook && git status --porcelain'    # YOUR leaves listed? then:
> /tmp/dx 'cd ~/repos/claude-blackbook && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -m "lesson(outcome): …" <exactly your leaf paths> && git pull --rebase -q && git push'
> ```
> **Siblings' leaves WILL be dirty in that listing and are not yours.** `-49` saw eight modified and
> two untracked belonging to `opus-acmeLedger-22` and `big_worker-autoBridge-3`, and the gate still
> printed PASS — the gate reads the estate, not your conscience. Commit by path, never `-A`.
> ### ⚠ `git commit -F <msg> <paths>` CANNOT STAGE AN UNTRACKED FILE.
> Look, add, then commit — the whole move on a shared repo:
>
> ```
> /tmp/dx 'cd ~/repos/<repo> && git status --porcelain'                 # look FIRST
> /tmp/dx 'cd ~/repos/<repo> && git add <only your new paths>'          # never -A, never .
> /tmp/dx 'cd ~/repos/<repo> && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -F /tmp/msg.txt <all your paths, new AND modified>'
> ```
> **`<n>` is the count of YOUR paths, not the staged total.** `-49`'s was 3.
> ### ⚠ SMALL DIFFS DO NOT NEED A TARBALL ROUND TRIP. `-49` PUSHED THREE FILES WITH `--put`.
> If you edited **N ≤ ~5 files** in the cloud, `cat f | /tmp/dx --put /Users/jasoncbraatz/repos/wealth-tensor/<path>`
> per file is one call each, prints a **sha256 verified against darwin**, and skips the tar/chown/
> AppleDouble dance entirely. Then run the suite on darwin and commit there. The tarball stanza
> below is for **coming down** (cloud needs the tree) — it is not the way back up.
> ## ⚠ ONE TARBALL, AND IT IS THE INBOUND DIRECTION ONLY.
>
> ```
> /tmp/dx 'cd ~/repos/wealth-tensor && git status --porcelain | wc -l'   # expect 0 before you tar
> /tmp/dx 'cd ~/repos/wealth-tensor && tar czf /tmp/wt-full.tgz \
>            --exclude=.venv --exclude=.pytest_cache --exclude=__pycache__ .'
> /tmp/dx --get /tmp/wt-full.tgz /tmp/wt-full.tgz
> mkdir -p /root/wtg && tar xzf /tmp/wt-full.tgz -C /root/wtg 2>/dev/null
> chown -R root:root /root/wtg && find /root/wtg -name '._*' -delete   # BOTH are required
> cd /root/wtg && git status --porcelain   # expect EMPTY. Anything here means the tar was wrong.
> ```
> `-49` measured **19,929,180 bytes** at `469012b`, `verified against darwin` in words, and
> `git status` empty on the first try. `.venv` is **650 MB** — exclude it. The two `chown`/`find`
> lines are not optional: macOS tar writes `._*` AppleDouble files that show as untracked, and
> darwin's uid makes git refuse the tree with *"dubious ownership"*.
> **`$HOME` in the cloud container is `/root`** — unpack to `/root/wtg` and give Read the absolute
> path. **Never inline a multi-line string in `dx '...'`** — write locally, `--put`, run it.
> `--get` with a leading `~` expands in the CLOUD shell and fails; use `/Users/jasoncbraatz/...`.
> Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
> **Exit 3** = never reached darwin, safe to re-run · **4** = dropped after the command started,
> check state first · **5** = crossed but mismatched, nothing written, replay-safe.
**SUITE COUNTS — COLLECTED = PASSED + SKIPPED, AND THE SKIPS ARE STILL GONE.**
| | at `HEAD` = `11b3b10` (verified in `-49`, both machines, same hour) |
|---|---|
| collected | **1031** (was 1018 at `4e85254`; `-49` added 13) |
| cloud, FULL tarball (`PYTHONPATH=/root/wtg/src`) | **1031 passed**, **~143 s**, **zero skips** |
| darwin (`.venv/bin/python -m pytest`) | **1031 passed**, ~61 s |
`scripts/defensive_count.py` **takes a positional `path`** and errors without one.
`pytest -m tripwire` selects the four-file tripwire class; `-m "not tripwire"` excludes it.
> ### ⚠ PROBE TIMING, MEASURED — AND THE 10-MINUTE TOOL CEILING IS THE REAL CONSTRAINT.
> A cloud container is **2 CPUs**; the sweep is `--jobs 2`. `-49` measured **~2 min 30 s per
> probe** at `--jobs 2`, so **three probes ≈ 7 min and six ≈ 14 min** — and a single foreground
> `Bash` call is killed at **10 minutes**. Run probes with `nohup … &` into a file and poll it;
> **do not poll with a `while pgrep` loop**, which burns the whole ceiling on waiting and dies
> with exit 143 having printed nothing. `pgrep -f mutation_control` can also read *running* for a
> few seconds after the summary block has printed — **trust the summary block, not the pgrep.**
---
## 0 · THE TELL, NOW IN FIFTY-THREE SHAPES
Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL GONE QUIET (`-32`). `-33`: instruments that agree with themselves; a
guard must scan assertions, not quotations. `-34`: defects nobody introduced. `-35`: defects you are
about to introduce. `-36`: pre-commit the FAVOURABLE outcome's meaning. `-37`: a mutation that does
not mutate reports your guard as weak. `-38`: a statistic can be a tautology in measurement's
clothing. `-39`: a handoff silently outranks a doctrine leaf; **assert the EXACT exit code**.
`-40`: a STALE NEGATIVE closes a question harder than an open one. `-41`: **a hand-audit that found
N sites found them through ONE DOOR.** `-42`: a constraint can be CONDITIONAL and its guard must
assert its ANTECEDENT; the second door is the SECTION HEADING. `-43`: a labelling constraint's
second door is the WRONG label; **feed the registration its own forbidden claim before you trust the
green**; a non-vacuity test must assert the CONJUNCTION. `-44`: a column that names a guard is a
COVERAGE CLAIM and nobody ever verifies it; **do not fuse a property of the artefact with a property
of the estate into one partition.** `-45`: a `source` cell is a PROVENANCE claim; **a quotation is a
lossy copy and the first things it loses are the ANTECEDENT and the REFERENT.** `-46`: a coverage
count read off the `machine` column is a claim about the COLUMN; a reproducibility pin is not a
freeze. `-47`: **a mutation the harness cannot see reports every guard in the unseen part of the
estate as absent**; a method that is wrong and mostly right is the most dangerous kind, because its
confirmations hide its counterexample; *untracked* and *gitignored* are different facts.
`-48`: a handoff's CHARACTERISATION of a document is not a MEASUREMENT of it; when a constraint's
referent decides its scope, the referent is the guard's DISCRIMINATOR; the lawful exceptions to a
forbidden word are the sites where the generality is the point.
**`-49` adds four:**
- **A HANDOFF'S PROPOSED GUARD DESIGN IS THE NEXT UNCHECKED SURFACE AFTER ITS COUNTS, AND ONE
  PREDICATE ACROSS A FAMILY OF CONSTRAINTS IS RED ON THE COMPLIANT WITNESSES.** `-48` measured its
  document and then handed forward a *design* nobody had tried. Three constraints saying the same
  sentence about three artefacts needed **two** discriminators — REFERENT where every lawful use of
  the forbidden verb has a different object, POLARITY where the document names the forbidden thing
  in order to refuse it. **Decide the discriminator per document, not per family.** Banked:
  `2026-08-15-one-prohibition-covers-several-artefacts-discriminator`.
- **A TEXT-NORMALISING HELPER IS TUNED TO WHAT ITS OWN CONSTRAINT'S DISCRIMINATOR MUST READ, AND
  COPYING IT CAN MAKE THE NEW GUARD VACUOUS IN BOTH DIRECTIONS.** `-48`'s `own_voice()` strips
  inline code — correct where code spans are XBRL element names, fatal where they are
  **cross-references**. This estate writes `` `-31` `` in backticks, so stripping inline code
  deletes the referent from the lawful sites *and* from `R3a`'s forbidden insertion: zero on the
  real document, zero on the mutation, nothing red, nothing suspicious. Only the `-43` non-vacuity
  test **using the probe's exact string** catches it. Banked:
  `2026-08-15-text-normalising-helper-tuned-its-own`.
- **A SELF-TEST WHOSE PREDICATE IS ABSENCE GOES RED ON THE MUTANT TOO, TURNING ONE DEFECT INTO TWO
  RED LINES AND BURYING THE ONE THAT NAMES IT.** `-49`'s own over-breadth tests read
  `assert not detector(doc + quotation)` and appeared as **spurious second catchers** on three
  probe rows — an over-breadth defect the guard did not have. The predicate must be
  **CONTRIBUTION**: `assert detector(doc + quotation) == detector(doc)`, which is true on a clean
  document and on a violating one. Banked: `2026-08-15-self-test-whose-predicate-absence-goes`.
- **FOR A CONJUNCTION GUARD — token A and token B in the same unit — THE UNIT IS A DESIGN CHOICE AND
  IT IS WHERE THE FALSE RED LIVES.** §0's warning about paragraph-resolution false greens runs the
  other way too. At **sentence** resolution C44's detector is red on a compliant document; at
  **clause** resolution (split on `.!?;`, an em-dashed aside, a colon) the verb and the referent fall
  apart at every lawful site and the detector stays red on the real insertion. **Pick the resolution
  deliberately, say so in the docstring, and pin the near-miss with a second assertion that its
  clauses have not fused.** Banked: `2026-08-15-conjunction-guard-token-token-b-same`.
**Everything `-33` through `-48` banked is unchanged and still sharp.** `severity.check`'s witness
must return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory.
`patchkit` anchors have **no internal newline**.
---
## 1 · WHAT HAPPENED
**Twenty minutes on the documents before a line of test code, for the second session running, and
for the second session running that is where it was won.** `-48`'s finding was that a handoff's
*counts* go unchecked. `-49`'s is one layer out: its *proposed design* does too, and this one would
not merely have mis-sent the session — it would have shipped a guard that is red on three compliant
`RESULT-*` documents.

**One new file, 13 tests, green on both machines: `tests/test_reg009_reg010_supersession_family.py`.**
| what | how |
|---|---|
| **LOST WARRANT**, per constraint | each of R3, C4 and `REG-010` §0 losing its clause reports *retire me*, not *violation* (`-42`), each anchored on its own **section heading** so a renumbered file fails loudly |
| **C44 · the presence pair** | *beside, never instead of* is C49's shape (`-44`): both documents **and** both artifacts. An absence guard cannot express *X, not merely Y*. Named as **not** what grades the row — `-46` already made deletion incidentally red |
| **C44 · the referent scan** | supersession verb **and** a name for `-31`'s count, **in one clause**, with inline code **kept**. The one lawful near-miss (§0's *"the measurement replacing both brackets"*) is pinned, plus a second assertion that its clauses have not fused |
| **C46 / C41 · the polarity scans** | forbidden token in a clause carrying **no negator**. Zero on the real document, one on each mutant, and the two are orthogonal — `R3b` does not trip C41's detector, `R3c` does not trip C46's |
| **C46 / C41 · the refusals, pinned present** | the document's own three refusal sentences. Deleting one is `R3e`/`R3f` and each has exactly one catcher |
| **non-vacuity ×3** | `R3a`/`R3b`/`R3c`'s **exact** insertions, each asserting the **CONJUNCTION** (`-43`), each **skipping** rather than piling on if the real document is already violating (`-39`) |
| **over-breadth ×2** | a quoted prohibition and a quoted forbidden reading must add **no hit** — the CONTRIBUTION predicate, see the tell above |
**Grading, on the reds and not on the column (`-44`).** `R3a` → 1 catcher · `R3b` → 1 · `R3c` → 1,
all three in the new file. `R3e` → 1 · `R3f` → 1. `R3d` → **6**: the owned presence assertion plus
the five `test_reg010_sec4_frozen_numbers.py` reds `-46` measured and correctly called incidental —
which is precisely why the owned catcher had to be separable from them. **C44, C46, C41 all `FOR`.**
**`scripts/mutation_control.py`: +`R3d`/`R3e`/`R3f`, 42 → 45**, plus a `_delete_file` helper.
`-47`'s rule, two sessions old: a limb with no probe is a claim, and the three presence limbs had
none. `R3e`/`R3f` were never measured *before* the guard existed — but their catcher lists contain
only the new file, so removing it leaves zero catchers, and that is the same fact by inference.
**Inventory edits:** C41, C44, C46 `PARTIAL` → **`FOR`** · §2a `FOR` 10→13, `PARTIAL` 5→2 · §3's
cross-table 13/30 → **16/27**, and *"14 of them name a machine that does not bind"* → **11**
(recomputed, not assumed) · §3.1's `PARTIAL (5)` → `(2)` with the three departures explained rather
than deleted · §3.1's C44/C46 blockquote struck through **with its prediction shown to have held** ·
§3.2 item 3 struck through **with its wrong mechanism left in place and corrected underneath** ·
**new §2e** carries the finding, the resolution ruling and the `own_voice()` trap.
**BUG SPRAY / the honest correction, on myself:** the two over-breadth tests shipped in my first
draft with an ABSENCE predicate and showed up as spurious catchers in my own probe run. Found in the
measurement, fixed before the grade, and banked — it is the third tell above.
| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** — the manuscript was not touched this session |
| **G-COACH-1** | held — the tee-up's wrong *mechanism* was corrected in `CONSTRAINT-INVENTORY-001` §2e and §3.2 in-session, not filed |
| **G-COACH-5** | held — the strength named is **`-47`'s two-minute probe**. Re-running `R3a`/`R3b`/`R3c` at `469012b` before writing a line cost seven minutes and turned *"the handoff says they were green"* into *"they are green"*; re-running them after the over-breadth fix cost seven more and removed a spurious co-catcher from three rows. **A measurement cheap enough to repeat is a different instrument from the same measurement taken once.** |
| suite | **1031 collected** · darwin **1031 passed** (~61 s) · cloud **1031 passed, zero skips** (~143 s) |
| new tests | 1 file, 13 tests · 3 new probes (42 → 45) |
| lessons | **four** banked global · **three** used and corroborated `record-outcome wealthTensor-49 pass` — two promoted quarantine → active, one at pass#1 |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |
---
## 2 · RULINGS — DO NOT REOPEN
- All of `-31`'s through `-48`'s rulings stand **verbatim**: no third disclosure instrument; phrase
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
  TRIPWIRE PINS MOVE IN THE SAME COMMIT AS THE EDIT THAT MOVED THEM**; **C42's FIFTEEN ARE FROZEN AS
  LITERALS AND THE LITERALS STAY**; **THE PARSE OF REG-010 §4 IS READING (A)**; **AN INCIDENTAL RED
  IS NOT COVERAGE**; **DO NOT PIN THE 98 AS A STRING**; **`.git` IS OPT-IN IN `mutation_control.py`
  AND A COMMIT-ORDER PROBE MUST SET IT**; **C07'S GUARD IS SCOPED TO REG-001 ON PURPOSE AND
  `9b3b013` IS NOT A VIOLATION**; **§3.2's SEVEN POSITIONS ARE MEASURED AND THE RANKING STANDS**;
  **C26's SCOPE IS `REG-006`/`RESULT-REG-006` AND THE DISCRIMINATOR IS *IS THIS A STATISTIC***;
  **C26's TWO BARE `impairment` SITES ARE LAWFUL AND PINNED**; **C26 LIMB B IS BOUNDED, NOT CLEAN**.
- **NEW · C44's DISCRIMINATOR IS THE REFERENT AND ITS RESOLUTION IS THE CLAUSE.** Three lawful uses
  of *replace*/*supersede* live in `RESULT-REG-009-band-count-filled.md` and a sentence-resolution
  detector is red on the first of them. **If you think the guard is under-broad, read §2e before you
  touch it** — and do not "fix" it by stripping inline code, which deletes the discriminator.
- **NEW · C46's AND C41's DISCRIMINATOR IS THE POLARITY, AND THE REFUSAL SENTENCES ARE PART OF THE
  ARTEFACT.** *"The mirror is not promoted, under this outcome or any other."* and *"It does not
  re-score P3, which failed and stays failed."* are pinned present. Deleting one is a violation of
  the constraint, not a tidy-up: silence and refusal have the same truth value to an absence guard.
- **NEW · AN OVER-BREADTH OR NON-VACUITY SELF-TEST IS PREDICATED ON CONTRIBUTION, NOT ABSENCE.**
  Otherwise it fires on every mutant of its own document and is read as a defect it does not have.
---
## 3 · THE AT-BAT for `-50` — **build item 4, C10.**
Items 1, 2 and 3 are built and struck through. Item 4 is the top of the measured list: **C10 ·
`REG-002` §5 — the re-ask is *"labelled an EXTENSION of E4 throughout, never as E4"***, probe `R4`
green in `-47`'s sweep. It is C21's exact shape one document over, and **C21 is the one that was not
clean** — seven live violations, found only because `-43` built C21's machine and discovered the
inventory's own grade was a one-door verdict.
**AND `-49` SPENT FOUR TOOL CALLS PRE-MEASURING IT, SO YOU DO NOT INHERIT ANOTHER UNCHECKED
CHARACTERISATION.** These are measurements at `11b3b10`, not claims:
- `RESULT-REG-002.md` carries **`E4` four times**, at lines **25, 54, 56 and 68**. **Only line 68 is
  the re-ask** — *"labelled in the script, in the manuscript and here as an **extension of** REG-002
  E4 rather than as the registered test"*, which is `R4`'s probe site. Lines 25, 54 and 56 name E4
  **as the registered test**, which is what it is. **C10 governs the RE-ASK, not every mention of
  `E4`, and a guard requiring every occurrence to carry the label is RED on a compliant document at
  three sites.** `-48`'s and `-49`'s finding, waiting for you a third time — this time defused.
- **The manuscript carries `E4` ZERO times** (`docs/papers/paper-III-dual-tensor/paper-III.md`),
  which confirms §1's C10 verdict — *out of manuscript scope* — as a measurement rather than a
  reading.
- ⚠ **`E4` HAS A HOMOGRAPH IN THE TOOLING AND IT IS EVERYWHERE.** `grep -rn 'E4' scripts/` returns
  **88 hits and essentially all of them are `# noqa: E402`**, a flake8 code containing the substring
  `E4`. C10's own witness says the label travels *"in the script"*, so the third surface is real and
  a naive scan of it is 88 false positives. `-43`'s *unregistered-contains-registered* lesson, in a
  new place: **decide the third surface's scope before you scan it, and use a word boundary that
  excludes `E40x`.**
The shape, from `§3.2` item 4 — **two limbs, and they fail differently (`-42`)**: the **wrong
label** (the re-ask called `E4` outright) and the **missing label** (the re-ask named with no
`extension of` at all). Scan assertions, not quotations (`-33`); flatten the wraps (`-37`); the
helpers in `test_reg009_reg010_supersession_family.py` are written to be read and **copied, not
imported** — and read the third tell above before you copy `own_voice()`, because `-49`'s whole
finding is that copying it unexamined is what breaks a guard silently.
**Then re-run `R4` and grade on the reds (`-44`).**
**AND DO THE TWENTY MINUTES ANYWAY.** Everything above is measured; the *design* is not. `-48`
proved a handoff's counts go unchecked and `-49` proved its guard designs do too. **Try the
predicate on the real document before you write the first assertion.**
**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The strongest alternative is now
**§4 item 6 — the git-axis sweep**, which has been open since `-47` and is the only place the estate
knows its instrument was blind. It is second only because the ranking is measured and this is a
residual; **it must not be allowed to become permanent.** The other is **C37's tripwire**
(`REG-009` §12's *"never by narration"*, `§3.3`, about an hour).
---
## 4 · TEED UP, IN ORDER
1. **T2 is CARDED (`1217501628088122`) and MAY NOT BE RUN ON THIS DATA.**
2. **C26 limb B — carded `1217525563299334`, State Machine.** §2's internal-control table: twelve
   ratios, no counts, counts available in `RESULT-REG-006-ladderC-run.log`'s `obs` column. Three
   options on the card. **Named residual: §2.2's four discovered couplings** (0.00×, 3.27×, 7.70×,
   6.33×) are prose ratios with p-values and no counts, adjudicated by nobody. Rule on both together.
3. **`RESULT-REG-003` §2's "Every cut lands in R1" — carded `1217518687033967`, State Machine.**
   Two readings; under one, 0.327 < 0.33 is R2 by the registration's own ladder. **A `RESULT-*` is
   the record of a run and editing the artefact edits the witness** — the `-37` precedent says the
   repair shape is a dated addendum. C12's guard is unaffected either way.
4. **Cell (b), ranked in `CONSTRAINT-INVENTORY-001` §3.2 — FOUR entries after C10, still MEASURED
   (§2c).** C10 (§3 above) · the five-constraint forbidden-claim family · C45's two assertions ·
   the reportable-at-all presence guards.
5. **C37's tripwire** — `REG-009` §12's *"never by narration"*. §3.3 names the adjacent check.
6. **`-47`'s residual, OPEN THREE SESSIONS NOW:** the other eight git-aware tests have never had a
   mutation run against them. `-47` fixed the harness and spent its one git probe on C07; `-48`
   spent its budget on C26; `-49` spent its three on the supersession family. **A probe per
   invariant, on the one axis the estate has proof it could not see.** If `-50` takes the ranking
   again, `-51` should take this — and somebody should say so out loud rather than re-deferring it
   a fourth time.
7. **§7's ledger dilutes its own two load-bearing rows — Jason's call, and it is TRIPWIRED, not
   carded.** `test_tripwire_c36_sec7_ledger_shape.py` will ask him the moment the shape moves. **Do
   not card it and do not ask him pre-emptively.**
8. Infra siblings, carded, Claude-hands: Caddy ordering `1217488447555628` · capability path in
   cleartext + repo drift `1217488117177482`.
9. AAR A2's residual — the other four `post-*` hooks · card-lint `1217483699706758` · gate
   `1217465036940491`.
10. Dossier era, re-served by nobody: `REVIEW-004` **C6** (ASC 410) and **C10** (IAS 36's reversal
    asymmetry, a free cross-regime falsification test). *(That `C10` is REVIEW-004's, not the
    inventory's — different numbering space, and the collision has now bitten twice.)*
11. Phrase-set passenger: 30.4 % match only `events or circumstances`; 7.9 % safe-harbour. Outranked.
12. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
13. Not mine, not touched: handoff-lint warns on `HANDOFF-acmeLedger-07.md:22`, `-09.md:36,42`, and
    `-12.md` / `-13.md` carry items with ZERO `verify:` lines. **Leave them alone** — `acmeLedger-22`
    was on the roster this session.
---
## 5 · DO NOT
* Everything `-31`→`-48` forbade still stands verbatim — R5, the two sensitivities,
  `selected_lives`, §4.4's `0.3000`, T4's `31.7%`, the δ arm, TERM-001/002, the dossier era, §9's
  FOUR list items, `wt107` IS NOT EDITED, cite the test not the backup, **"THE REGISTERED ADVERSE
  CUT" DOES NOT RETURN**, **§4.7 IS PINNED AT `ba59370`**, **DO NOT "SIMPLIFY" A TRIPWIRE INTO A
  GUARD**, **DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION**, **DO NOT GRADE A
  CONSTRAINT FROM THE `machine` COLUMN, INCLUDING WHEN YOU ARE ONLY RANKING**, **DO NOT RUN A
  COMMIT-ORDER PROBE WITHOUT `{"git": True}`**, **DO NOT WIDEN C07's GUARD TO EVERY REGISTRATION**,
  **DO NOT SOFTEN A DOCTRINE SENTENCE THAT TURNS OUT TO BE FALSE — MAKE IT TRUE, THEN GIVE IT A
  MACHINE**, **DO NOT PIN THE 98 AS A STRING**, **DO NOT WIDEN C26 LIMB A TO EVERY OCCURRENCE OF THE
  WORD**, **DO NOT PRINT COUNTS INTO §2's INTERNAL-CONTROL TABLE WITHOUT UPDATING `UNCOUNTED_ROWS`
  AND §2d IN THE SAME COMMIT**. §2.
* **NEW · DO NOT COPY AN `own_voice()` HELPER WITHOUT ASKING WHICH OF ITS REMOVALS YOUR
  DISCRIMINATOR NEEDS TO SURVIVE.** Stripping inline code is right for C26 and makes C44 vacuous in
  both directions, which is invisible everywhere except the non-vacuity test. §2e.
* **NEW · DO NOT WRITE AN OVER-BREADTH OR NON-VACUITY SELF-TEST WITH AN ABSENCE PREDICATE.** Use
  `detector(doc + quotation) == detector(doc)`. An absence predicate fires on the guard's own
  mutants and reports a defect that is not there.
* **NEW · DO NOT DELETE `RESULT-REG-010`'s REFUSAL SENTENCES**, and do not "tidy" the §3 paragraph
  that spells out the flattering reading in order to refuse it. It is quoted on purpose, the guard
  is built to leave it alone, and it is the best paragraph in the document.
* **NEW · DO NOT TRUST A HANDOFF'S DESIGN FOR A GUARD — INCLUDING THIS ONE'S §3.** Every number in
  §1 and every `E4` measurement in §3 was measured this session at `11b3b10`. The *shape* proposed
  for C10 is a claim about a predicate nobody has run. **Run it on the real document first.**
* Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud.
* Do not poll a background probe run with `while pgrep` — the 10-minute tool ceiling eats it.
---
## 6 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.
Coffee status: ☕ **FIFTEEN SESSIONS RUNNING, AND THE FIRST TWENTY MINUTES DECIDED THE WHOLE SESSION
AGAIN** — `-35` truth, `-36` population, `-37` count, `-38` premise-and-instrument, `-39` severity,
`-40` the promise the document made about itself, `-41` the resolution it was written at, `-42`
whether it was in force, `-43` who the promise was made about, `-44` whether the thing guarding it
can see it, `-45` whether the address on it was right, `-46` whether the sentence that sent you here
was ever checked, `-47` whether the instrument that checks it can see the whole board, `-48` whether
the sentence that sent you here had ever opened the document, **`-49` WHETHER THE MACHINE THE
SENTENCE TOLD YOU TO BUILD HAD EVER BEEN RUN AGAINST THE DOCUMENT IT GOVERNS.** `-48`'s came from
counting a word. `-49`'s came from running one regex, by hand, in a scratch file, before writing any
test — four minutes, against a design three sessions had agreed on without once trying it. **The
cheapest check in the estate is still the one nobody runs. Now it is not the fact that reads like
the fact — it is the PLAN that reads like the finished thing. Run the predicate first.**
