---
project: wealth-tensor
gh_sha: 393eaa8dfe1493d1a123acb294145abc618ad2c4
updated: 2026-08-15
session: wealthTensor-50
gate_passed: true
gate_version: "2.54"
---
# wealth-tensor — HANDOFF
*`gh_sha` points at the commit this file describes; the only thing added after it is this file, so
`--check` prints `ADVISORY: docs-only drift` and exits 0. **Read the exit code, and assert it
exactly (`-39`) — `| tail` will mask it.***
> **`-50` tripped this gate and the gate was right.** The first handoff commit carried a
> **docstring** change to `scripts/mutation_control.py` alongside the handoff, and `--check` called
> `BLOCKER: code advanced past the handoff` — correctly, because it classifies by PATH and cannot
> know a `.py` diff was prose. The fix was to repoint `gh_sha` at the commit that actually holds the
> described state, **not** to rewrite pushed history and **not** to teach the gate to guess.
> **Lesson for you: land code and docs in the commit `gh_sha` names, and write the handoff alone in
> the one after it.** A gate that is conservative about a `.py` file is doing its job.

## ORIENT — read these first, in this order
1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff, any
   result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the other
   thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. **`docs/preregistration/CONSTRAINT-INVENTORY-001.md`** — the map for this thread. Fifty reporting
   constraints on two axes: `recog` (MECH / PROXY / READER / n/a — a property of the CONSTRAINT) and
   a **FOR / BINDS / PARTIAL / ADJACENT / TRIPWIRE** grade on the machine cell (a property of the
   ESTATE). **Read §2f first this time** — it is `-50`'s finding, and the paragraph about a
   correction that never reached the estate is the one that matters. Then §2e (`-49`), §2d (`-48`),
   §2c (`-47`'s measurement, still the warrant for the ranking), then §3.2, then §2a's counts.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`python3 scripts/mutation_control.py --list`** — **48 probes now** (45 at `-49`; `-50` added
   `R4b`/`R4c`/`R4d`). **Read its module docstring before you grade anything** — including the new
   paragraph that replaces a stale count with the command that produces it.
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

> **`-50` in one line: THE TEE-UP MEASURED IT, WROTE IT DOWN, AND THE ESTATE NEVER GOT THE MEMO.**
> `-49` spent four tool calls proving that only ONE of `RESULT-REG-002`'s four `E4` mentions is the
> re-ask, and that a guard on *"every mention"* is red on three lawful sites. It put that in its
> handoff. **C10's row in `CONSTRAINT-INVENTORY-001` still said `resolution: every mention` and
> `governed quantity: E4`** — the exact reading `-49` had disproved, sitting in the file every
> session is told to build from, two commits away from the measurement that killed it. **Seven
> sessions running, the thing that did not survive checking was the estate's prose about itself**:
> `-44` the `machine` column, `-45` the `source` column, `-46` the ranking prose, `-47` the harness
> AND the DO-NOT list, `-48` the tee-up's reading of its document, `-49` the tee-up's *design* for a
> guard, **`-50` the DELIVERY — a measurement that was right, was written down, and never arrived.**
> C10 is **BUILT** and grades **FOR**, four probes, every limb separably load-bearing.

---

### Transport — darlish, zero-bridge
Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-50`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.
`darlish-check` is **not** in the cloud kit — do not chase its 127.
`roster leave` ONCE at wrap.

> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
> dx spawns a **fresh remote shell per call and carries no environment**. Inline on `roster join`,
> `roster claim`, the commit, and every `lessons.py` call — first time, every time.
> **Exception: `export GATE_ROSTER_WHO=…` DOES work inside a script you `--put` and run with
> `bash /tmp/x.sh`**, because that is one shell. `-47` through `-50` all ran their `lessons.py`
> calls that way. The roster brake still prints the **absorbed** row name (`cloud-…`) in its `you:`
> line; cosmetic, not a mis-identity.
> ### ⚠ `roster claim` TAKES `--resource`, NOT `--repo`. `record-outcome` TAKES NO `--id`.
> `roster claim --who <who> --resource <repo> --task "<what>"`; `roster join` takes `--who/--task`.
> **`lessons.py record-outcome <task-tag> pass` is TWO positional args and nothing else.** One call
> resolves every leaf you marked with `use --task <tag>`.
> ### ⚠ `lessons.py` AUTO-COMMITS AND AUTO-PUSHES EACH LEAF. **DO NOT HAND-COMMIT AFTERWARDS.**
> `-49` hit no brake; `-50` hit none either — every `add`, `use` and `record-outcome` self-committed
> and self-pushed while a sibling held the repo. **LOOK before you reach for a commit**; a
> hand-commit of already-committed leaves is a no-op that reads like a problem:
>
> ```
> /tmp/dx 'cd ~/repos/claude-blackbook && git log --oneline origin/main..HEAD | wc -l'   # 0 = done
> /tmp/dx 'cd ~/repos/claude-blackbook && git status --porcelain'                        # siblings'
> ```
> **Siblings' leaves WILL be dirty in that listing and are not yours.** `-50` saw five modified and
> one untracked belonging to `opus-acmeLedger-23`. Commit by path, never `-A`.
> ### ⚠ `lessons.py add` SILENTLY FORKS A TWIN ON AN ID COLLISION — CHECK, THEN CURATE.
> `-50`'s conjunction-resolution leaf collided with `-49`'s and was banked as
> `…-same-2.md`, printing one line about it in a wall of banner text. **Doctrine says curate the ONE
> leaf.** The move: read both, rewrite the ORIGINAL to carry both measurements, name both sessions in
> `source:`, `git rm` the twin, commit by path. `-50` did this; the merged leaf is
> `2026-08-15-conjunction-guard-token-token-b-same` and it is worth reading — it is one rule measured
> from both sides.
> ### ⚠ `git commit -F <msg> <paths>` CANNOT STAGE AN UNTRACKED FILE.
> Look, add, then commit — the whole move on a shared repo:
>
> ```
> /tmp/dx 'cd ~/repos/<repo> && git status --porcelain'                 # look FIRST
> /tmp/dx 'cd ~/repos/<repo> && git add <only your new paths>'          # never -A, never .
> /tmp/dx 'cd ~/repos/<repo> && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -F /tmp/msg.txt <all your paths, new AND modified>'
> ```
> **`<n>` is the count of YOUR paths, not the staged total.** `-50`'s was 3.
> ### ⚠ SMALL DIFFS DO NOT NEED A TARBALL ROUND TRIP. `-50` PUSHED FOUR FILES WITH `--put`.
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
> `-50` measured **20,020,423 bytes** at `8cdf78e`, `verified against darwin` in words, and
> `git status` empty on the first try. `.venv` is **650 MB** — exclude it. The two `chown`/`find`
> lines are not optional: macOS tar writes `._*` AppleDouble files that show as untracked, and
> darwin's uid makes git refuse the tree with *"dubious ownership"*.
> **`$HOME` in the cloud container is `/root`** — unpack to `/root/wtg` and give Read the absolute
> path. **Never inline a multi-line string in `dx '...'`** — write locally, `--put`, run it.
> `--get` with a leading `~` expands in the CLOUD shell and fails; use `/Users/jasoncbraatz/...`.
> Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
> **Exit 3** = never reached darwin, safe to re-run · **4** = dropped after the command started,
> check state first · **5** = crossed but mismatched, nothing written, replay-safe.

**SUITE COUNTS — COLLECTED = PASSED + SKIPPED, AND THE SKIPS ARE STILL GONE (with `.git`).**

| | at `HEAD` = `142d386` (verified in `-50`, both machines, same hour) |
|---|---|
| collected | **1048** (was 1031 at `11b3b10`; `-50` added 17) |
| cloud, FULL tarball (`PYTHONPATH=/root/wtg/src`) | **1048 passed**, **~234 s**, **zero skips** |
| darwin (`.venv/bin/python -m pytest`) | **1048 passed**, ~62 s |
| cloud **without** `.git` | **1034 passed, 14 skipped** — see §4 item 6 |

`scripts/defensive_count.py` **takes a positional `path`** and errors without one.
`pytest -m tripwire` selects the four-file tripwire class; `-m "not tripwire"` excludes it.

> ### ⚠ PROBE TIMING, RE-MEASURED, AND IT IS SLOWER THAN `-49` RECORDED.
> A cloud container is **2 CPUs**; the sweep is `--jobs 2`. `-49` measured ~2 min 30 s per probe.
> **`-50` measured ~3 min 30 s** at the same `--jobs` — the suite grew. **Four probes ≈ 14 min**,
> and a single foreground `Bash` call is killed at **10 minutes**. Run probes with `nohup … &` into
> a file and poll it with `sleep N; tail`; **do not poll with a `while pgrep` loop**, which burns
> the whole ceiling on waiting and dies with exit 143 having printed nothing. `pgrep -f
> mutation_control` can also read *running* for seconds after the summary block prints — **trust
> the summary block, not the pgrep.** Budget for running the sweep **twice**; `-49` and `-50` both
> found a real defect on the second run and both would have shipped it on the first.

---

## 0 · THE TELL, NOW IN FIFTY-SEVEN SHAPES
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
estate as absent**; a method that is wrong and mostly right is the most dangerous kind; *untracked*
and *gitignored* are different facts. `-48`: a handoff's CHARACTERISATION of a document is not a
MEASUREMENT of it; when a constraint's referent decides its scope, the referent is the guard's
DISCRIMINATOR. `-49`: a handoff's proposed GUARD DESIGN is the next unchecked surface after its
counts; a text-normalising helper is tuned to its own constraint's discriminator; a self-test whose
predicate is ABSENCE goes red on the mutant too; for a conjunction guard the UNIT is a design choice.

**`-50` adds four:**

- **A CORRECTION THAT LIVES ONLY IN A HANDOFF HAS NOT BEEN MADE.** `-49` measured C10's real scope,
  found *"every mention"* wrong, wrote the right reading into its handoff — and **the inventory row
  a session is instructed to build from still carried the disproved cell.** The handoff is a message
  to one session; the inventory is the estate. **A finding is not banked until the ARTEFACT it
  corrects has been edited, in the same commit, and the handoff entry names the file it changed.**
  Banked: `2026-08-15-correction-lives-only-handoff-has-not-been-made`.
- **FOR A CONJUNCTION GUARD, THE UNIT'S WRONG CHOICE FAILS IN BOTH DIRECTIONS, AND THE CHEAP-LOOKING
  DIRECTION IS THE DANGEROUS ONE.** `-49` moved C44 to CLAUSE resolution to escape a false RED. C10's
  referent and token are separated by **commas only**, so clause resolution returns **0 on the real
  document and 0 on `R4`'s mutant** — vacuous, silent, indistinguishable from a clean pass. A false
  red announces itself; a false green does not. **Run the predicate at BOTH resolutions against the
  exact probe string before writing a line, and pin the table in a test.** Merged into `-49`'s leaf
  (see the transport note on twins): `2026-08-15-conjunction-guard-token-token-b-same`.
- **A HOMOGRAPH COUNT IS NOT A HOMOGRAPH AUDIT.** `-49` sized C10's third surface as *"~88 hits and
  essentially all of them are `# noqa: E402`"* and prescribed a word boundary. Measured: **90
  substring, 61 noqa, and all 29 survivors are true `\bE4\b` across SEVEN files** — `E4` is a
  per-script *local exhibit label*. The remedy removes 61 and leaves 21. **Knowing what the noise IS
  does not tell you how much of it the fix removes.** Banked:
  `2026-08-15-homograph-count-not-homograph-audit`.
- **ANY SELF-TEST THAT READS THE REAL DOCUMENT, LIVING IN A FILE THE SWEEP MUTATES, IS A SECOND
  CATCHER FOR EVERY PROBE UNLESS IT SKIPS ON A DIRTY BASE.** Not just over-breadth tests — a
  near-miss pin that re-asserts the main limb, a resolution pin that assumes a clean base, a
  non-vacuity test whose anchor a *different* probe deletes. All four fired. **Predicate on
  CONTRIBUTION; skip on a dirty base and name the limb that owns the red; skip rather than assert
  when a probe removes your anchor.** Banked:
  `2026-08-15-test-reads-real-document-asserts-property`.

**Everything `-33` through `-49` banked is unchanged and still sharp.** `severity.check`'s witness
must return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory.
`patchkit` anchors have **no internal newline**.

---

## 1 · WHAT HAPPENED
**Twenty minutes on the documents before a line of test code, for the third session running, and for
the third session running that is where it was won.** `-48` found a handoff's *counts* go unchecked;
`-49` found its *designs* do; `-50` found that even when both are right and written down, **the file
they correct does not necessarily get edited.**

**One new file, 17 tests, green on both machines: `tests/test_reg002_sec5_e4_extension_label.py`.**

| what | how |
|---|---|
| **LOST WARRANT** ×2 | `REG-002` §5's clause and `RESULT-REG-002` §3's existence each report *retire me*, not *violation* (`-42`), each anchored on its own **section heading** so a renumber fails loudly |
| **limb A · the referent scan** | a supersession marker (*substitution* / *re-ask*) **and** a bare `E4` in **one sentence**, where `LABELLED_E4` has not already covered that occurrence. Matched as a unit, so the guard carries no magic character window |
| **limb A · the three lawful sites, pinned** | §1's table row, §3's heading, §3's opening — all name E4 *as the registered test*. Pinned so a rewrite that pulls a substitution word into one is read by a human, not by a widened regex |
| **limb B · the presence limb** | an absence guard cannot express *X, not merely not-Y* (`-44`'s C49 shape). Limb A is **green** on a document that simply deletes the labelling sentence; limb B is not |
| **limb C · the third surface** | the same pair scoped to `wt088_disclosed_ladder.py` **alone**, because `E4` is a per-script local label in six other scripts. The scope is pinned as three numbers, not as a habit |
| **`own_voice()`, asked one removal at a time** | blockquotes **stripped** (`-33`) · fenced code **stripped** · **inline code DELIBERATELY KEPT** — this document writes `E4` bold and bare, never in backticks, so the removal buys nothing and would blind the guard the day someone writes `` `E4` ``. `-49`'s lesson, applied in the *don't* direction |
| **resolution, measured both ways** | sentence → 0 real / 1 mutant · comma-clause → 0 / **0**. Pinned in `test_the_resolution_choice_is_pinned` |
| **non-vacuity ×4** | each probe's **exact** string, each asserting the **CONJUNCTION** (`-43`), each **skipping** rather than piling on when the base is dirty (`-39`) |
| **over-breadth ×2** | the CONTRIBUTION predicate — `detector(doc + quotation) == detector(doc)` |

**Grading, on the reds and not on the column (`-44`).** `R4` → 2 catchers (limb A owned; limb B
genuine — `R4` deletes the label as it mislabels) · `R4b` → **1, limb A alone** · `R4c` → 2 (limb B
owned; the fusion pin, genuine) · `R4d` → 3 (both limb C tests owned; the third,
`test_reg009_ladder_inputs.py`'s instrument re-run, is a reproducibility pin and **incidental**,
`-46`). **Limbs A and B each hold a probe the other is green on — separably load-bearing, measured.**

**`scripts/mutation_control.py`: +`R4b`/`R4c`/`R4d`, 45 → 48.**

**Inventory edits:** C10 `none` → **`FOR`** · **its `resolution` cell `every mention` → `sentence`
and its `governed quantity` cell `E4` → *the α = 0.35 substitution, not the token*** — the correction
`-49` measured and nobody applied · §2a `FOR` 13→14, `none` 22→21 · §3's cross-table 16/27 →
**17/26** with the eleven false-greens **recomputed and unchanged** · §3.2 item 4 struck through with
what it was silent about named · §2c's *"nine tests · 990/999"* corrected to **14 across six files**
with the stale-count tell recorded rather than the sentence softened · **new §2f** carries all of it.

**BUG SPRAY / the honest correction, on myself:** the first draft shipped **four** self-tests with
ABSENCE predicates — `-49`'s banked defect, one session old, read and then reproduced — and the
sweep put them in every catcher list (`R4` had four catchers where it has two, `R4b` four where it
has one). Found in the measurement, fixed before the grade, banked as the fourth tell above.
**Knowing the lesson was not enough; running the sweep twice was.**

**BUG SPRAY, second:** `lessons.py` forked a twin on an id collision. Merged into the original leaf,
twin `git rm`'d, both sessions named in `source:` — see the transport note.

| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** — the manuscript was not touched this session |
| **G-COACH-1** | held — `-49`'s uncorrected inventory cells were fixed **in-session**, not filed |
| **G-COACH-5** | held — the strength named is **the two-minute-per-probe sweep, run TWICE**. `-49` named it and spent it; `-50` spent it again and it paid again, catching four spurious co-catchers that review had passed. **A measurement cheap enough to repeat is a different instrument from the same measurement taken once — and this is now the second consecutive session where the second run, not the first, produced the finding.** |
| suite | **1048 collected** · darwin **1048 passed** (~62 s) · cloud **1048 passed, zero skips** (~234 s) |
| new tests | 1 file, 17 tests · 3 new probes (45 → 48) |
| lessons | **three** banked global + **one merged** into `-49`'s leaf · **five** used and corroborated `record-outcome wealthTensor-50 pass` — four promoted quarantine → active, one at pass#3 |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |

---

## 2 · RULINGS — DO NOT REOPEN
- All of `-31`'s through `-49`'s rulings stand **verbatim**: no third disclosure instrument; phrase
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
  `machine` CELL WITHOUT DOING THE AUDIT**; **C49's GUARD IS A PAIR**; **DO NOT DELETE THE REFUSAL
  SENTENCES FROM `RESULT-REG-012-band-edge-phase.md` OR `RESULT-REG-010`**; **C09's WARRANT IS
  `REG-002` E2, NEVER E1**; **`TRIPWIRE` IS A GRADE AND IT IS NOT COVERAGE**; **A TRIPWIRE'S RED
  MESSAGE IS PART OF THE ARTEFACT**; **THE THREE TRIPWIRE PINS MOVE IN THE SAME COMMIT AS THE EDIT
  THAT MOVED THEM**; **C42's FIFTEEN ARE FROZEN AS LITERALS**; **THE PARSE OF REG-010 §4 IS READING
  (A)**; **AN INCIDENTAL RED IS NOT COVERAGE**; **DO NOT PIN THE 98 AS A STRING**; **`.git` IS
  OPT-IN IN `mutation_control.py` AND A COMMIT-ORDER PROBE MUST SET IT**; **C07'S GUARD IS SCOPED TO
  REG-001 ON PURPOSE**; **§3.2's SEVEN POSITIONS ARE MEASURED AND THE RANKING STANDS**; **C26's
  DISCRIMINATOR IS *IS THIS A STATISTIC*; ITS TWO BARE SITES ARE LAWFUL AND PINNED; LIMB B IS
  BOUNDED, NOT CLEAN**; **C44's DISCRIMINATOR IS THE REFERENT AND ITS RESOLUTION IS THE CLAUSE**;
  **C46's AND C41's DISCRIMINATOR IS THE POLARITY**; **AN OVER-BREADTH OR NON-VACUITY SELF-TEST IS
  PREDICATED ON CONTRIBUTION, NOT ABSENCE**.
- **NEW · C10 GOVERNS THE SUBSTITUTION, NOT THE TOKEN, AND ITS RESOLUTION IS THE SENTENCE.**
  `RESULT-REG-002` names `E4` four times and **three of them are lawful** — §1's table row, §3's
  heading, §3's opening sentence all name E4 *as the registered test*, which is what it is. **If you
  think the guard is under-broad, read §2f before you touch it**, and do not "fix" it by moving to
  clause resolution, which makes it vacuous in both directions.
- **NEW · C10's THIRD SURFACE IS `wt088_disclosed_ladder.py` AND NOTHING ELSE.** `E4` is a per-script
  local exhibit label in six other scripts. The manuscript is out of scope and that is a
  **measurement** (zero occurrences), not a reading — `test_the_manuscript_is_out_of_scope_as_a_measurement`
  will tell you the day the premise changes.
- **NEW · A CORRECTION IS NOT MADE UNTIL THE ARTEFACT IS EDITED.** Writing a finding into a handoff
  is telling one session. Editing the inventory row is telling the estate. Do both, in one commit,
  and name the file you changed.

---

## 3 · THE AT-BAT for `-51` — **§4 item 6, THE GIT-AXIS SWEEP. IT IS ITS TURN AND THIS IS THE
OUT-LOUD SAYING-SO `-49` ASKED FOR.**

`-49` wrote: *"If `-50` takes the ranking again, `-51` should take this — and somebody should say so
out loud rather than re-deferring it a fourth time."* **`-50` took the ranking. So this is the
at-bat, and it is not negotiable against a fifth deferral.** It has been open since `-47` and it is
the **only place the estate has proof its instrument was blind.**

**AND `-50` PRE-MEASURED IT, SO YOU DO NOT INHERIT ANOTHER UNCHECKED CHARACTERISATION.** These are
measurements at `142d386`, not claims:

- **The residual is 13 tests across 6 files, not 8.** `-47`'s *"nine tests"* was true when written
  and rotted; the suite grew. Measured: the full suite **without `.git`** is **1034 passed, 14
  skipped**. `R1` spent one of the fourteen (`test_registrations_precede_their_instruments.py`), so
  **thirteen git-gated invariants have never had a mutation run against them.** The count is now a
  command, not a number — it is in `mutation_control.py`'s docstring, and §2c records the tell.
- **The six files, with their git-gated test counts:**
  `test_registrations_precede_their_instruments.py` (4, one probed by `R1`) ·
  `test_backups_are_ignored.py` (3) · `test_pin001_code_state.py` (3) ·
  `test_reg001_sec5_no_amendment_after_result.py` (2) ·
  `test_reg012_sec6_sec47_frozen.py` (1) · `test_manuscript_shas_are_instrumented.py` (1).
- **`{"git": True}` appears on exactly ONE probe today** (`R1`). Every probe you add here needs it or
  it measures nothing — that is `-47`'s ruling and it is the whole reason this axis is dark.

The shape: **a probe per invariant, not per file.** Each of the thirteen asserts something about
history — a pin, a commit order, an ignore rule, a SHA resolving — so each needs a mutation that is
a *history* move (amend, reorder, un-ignore, retarget a SHA), and `_amend_after_result` /
`_git` in `mutation_control.py` are the helpers already written for exactly that. Grade on the reds
(`-44`). Expect some of the thirteen to be **reproducibility pins rather than freezes** (`-46`) —
say which, in the row, rather than counting them as coverage.

**AND DO THE TWENTY MINUTES ANYWAY.** Everything above is measured; the *design* is not. `-48` proved
a handoff's counts go unchecked, `-49` proved its guard designs do, `-50` proved its corrections can
fail to arrive. **Run the predicate — here, the probe — against the real thing before you write the
first assertion.**

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The strongest alternative is **§3.2 item 5, the
five-constraint forbidden-claim family** (`R5a`–`R5e`, all green, one claim-scanner shape already
built twice at C19 and C24) — cheap and well-understood, which is exactly why it should not be
allowed to displace the axis nobody can see. The other is **C37's tripwire** (`REG-009` §12's
*"never by narration"*, `§3.3`, about an hour).

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
4. **Cell (b), ranked in `CONSTRAINT-INVENTORY-001` §3.2 — THREE entries left, still MEASURED
   (§2c).** The five-constraint forbidden-claim family · C45's two assertions · the
   reportable-at-all presence guards.
5. **C37's tripwire** — `REG-009` §12's *"never by narration"*. §3.3 names the adjacent check.
6. **`-47`'s residual — NOW §3, THE AT-BAT. Do not re-defer it.** 13 unprobed git-gated invariants
   across 6 files; numbers and file list in §3.
7. **§7's ledger dilutes its own two load-bearing rows — Jason's call, and it is TRIPWIRED, not
   carded.** `test_tripwire_c36_sec7_ledger_shape.py` will ask him the moment the shape moves. **Do
   not card it and do not ask him pre-emptively.**
8. Infra siblings, carded, Claude-hands: Caddy ordering `1217488447555628` · capability path in
   cleartext + repo drift `1217488117177482`.
9. AAR A2's residual — the other four `post-*` hooks · card-lint `1217483699706758` · gate
   `1217465036940491`.
10. Dossier era, re-served by nobody: `REVIEW-004` **C6** (ASC 410) and **C10** (IAS 36's reversal
    asymmetry, a free cross-regime falsification test). *(That `C10` is REVIEW-004's, not the
    inventory's — different numbering space, and the collision has now bitten three times, including
    once in this session's own search results. Say which C10 you mean, always.)*
11. Phrase-set passenger: 30.4 % match only `events or circumstances`; 7.9 % safe-harbour. Outranked.
12. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
13. Not mine, not touched: handoff-lint warns on `HANDOFF-acmeLedger-07.md:22`, `-09.md:36,42`, and
    `-12.md` / `-13.md` carry items with ZERO `verify:` lines. **Leave them alone** — `acmeLedger-23`
    was on the roster this session.

---

## 5 · DO NOT
* Everything `-31`→`-49` forbade still stands verbatim — R5, the two sensitivities,
  `selected_lives`, §4.4's `0.3000`, T4's `31.7%`, the δ arm, TERM-001/002, the dossier era, §9's
  FOUR list items, `wt107` IS NOT EDITED, cite the test not the backup, **"THE REGISTERED ADVERSE
  CUT" DOES NOT RETURN**, **§4.7 IS PINNED AT `ba59370`**, **DO NOT "SIMPLIFY" A TRIPWIRE INTO A
  GUARD**, **DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION**, **DO NOT GRADE A
  CONSTRAINT FROM THE `machine` COLUMN, INCLUDING WHEN YOU ARE ONLY RANKING**, **DO NOT RUN A
  COMMIT-ORDER PROBE WITHOUT `{"git": True}`**, **DO NOT WIDEN C07's GUARD TO EVERY REGISTRATION**,
  **DO NOT SOFTEN A DOCTRINE SENTENCE THAT TURNS OUT TO BE FALSE — MAKE IT TRUE, THEN GIVE IT A
  MACHINE**, **DO NOT PIN THE 98 AS A STRING**, **DO NOT WIDEN C26 LIMB A TO EVERY OCCURRENCE**,
  **DO NOT COPY AN `own_voice()` HELPER WITHOUT ASKING WHICH REMOVALS YOUR DISCRIMINATOR NEEDS TO
  SURVIVE**, **DO NOT WRITE AN OVER-BREADTH OR NON-VACUITY SELF-TEST WITH AN ABSENCE PREDICATE**,
  **DO NOT DELETE `RESULT-REG-010`'s REFUSAL SENTENCES**. §2.
* **NEW · DO NOT WIDEN C10 TO EVERY OCCURRENCE OF `E4`.** Three of the four are lawful and the
  widened guard is red on a compliant document. §2f, and the near-miss pin will tell you.
* **NEW · DO NOT MOVE C10's DETECTOR TO CLAUSE RESOLUTION.** It goes vacuous in both directions and
  nothing turns red to say so. The pin test carries the measured table; read it before you edit the
  splitter.
* **NEW · DO NOT SCAN `scripts/` REPO-WIDE FOR `E4`.** A word boundary leaves 21 false positives
  from six unrelated scripts. Scope to `wt088`.
* **NEW · DO NOT QUOTE THE GIT-SKIP COUNT FROM PROSE — RUN THE COMMAND.** It was nine, it is
  fourteen, and it will move again. The command is in `mutation_control.py`'s docstring.
* **NEW · DO NOT LEAVE A FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT CORRECTS.** That is
  this session's whole finding, and it will happen again the moment somebody is in a hurry.
* **NEW · DO NOT TRUST A HANDOFF'S DESIGN — INCLUDING THIS ONE'S §3.** Every number in §1 and every
  git-axis measurement in §3 was measured this session at `142d386`. The *shape* proposed for the
  git sweep is a claim about probes nobody has run. **Run one first.**
* Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud.
* Do not poll a background probe run with `while pgrep` — the 10-minute tool ceiling eats it.

---

## 6 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.

Coffee status: ☕ **SIXTEEN SESSIONS RUNNING, AND THE FIRST TWENTY MINUTES DECIDED THE WHOLE SESSION
AGAIN** — `-35` truth, `-36` population, `-37` count, `-38` premise-and-instrument, `-39` severity,
`-40` the promise the document made about itself, `-41` the resolution it was written at, `-42`
whether it was in force, `-43` who the promise was made about, `-44` whether the thing guarding it
can see it, `-45` whether the address on it was right, `-46` whether the sentence that sent you here
was ever checked, `-47` whether the instrument that checks it can see the whole board, `-48` whether
the sentence that sent you here had ever opened the document, `-49` whether the machine that sentence
told you to build had ever been run, **`-50` WHETHER THE CORRECTION SOMEBODY ALREADY MADE EVER
REACHED THE FILE IT WAS ABOUT.** `-49`'s came from running one regex by hand. `-50`'s came from
reading C10's inventory row and its handoff paragraph side by side and noticing they disagreed —
**one minute, and the row had been wrong since before the measurement that disproved it was taken.**
The cheapest check in the estate is still the one nobody runs. It was the fact, then the plan, and
now it is **THE DELIVERY. A finding you wrote down and did not install is a finding the estate does
not have.**
