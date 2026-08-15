---
project: wealth-tensor
gh_sha: 842d7f22bda1980ec54e11cc1709c5c4b63cca32
updated: 2026-08-15
session: wealthTensor-51
gate_passed: true
gate_version: "2.58"
definition_of_done: "Three preprints (II, III, IV) publicly posted — the corpus-level Definition of Done in ADR-001 as amended (was four; Paper I folded into IV). Per-paper clauses in ADR-001 govern each paper's 'ready to submit' terminal state, and nothing ships until the corpus is done."
---
# wealth-tensor — HANDOFF
*`gh_sha` points at the commit this file describes; the only thing added after it is this file, so
`--check` prints `ADVISORY: docs-only drift` and exits 0. **Read the exit code, and assert it
exactly (`-39`) — `| tail` will mask it.***
> **`-50` tripped this gate and the gate was right**, by landing a `.py` docstring change in the
> handoff commit. `-51` did not: code and the inventory went in `3f63237`, this file alone after it.
> **Land code and docs in the commit `gh_sha` names, and write the handoff alone in the next.**
>
> **AND `gh_sha` MOVED ONCE MORE, DELIBERATELY.** After `-51` wrapped, Jason's questions produced a
> coda — an ADR correction in `842d7f2` — so `gh_sha` was **repointed from `3f63237` to `842d7f2`**,
> the last commit that is not this file. The sentence above is an INVARIANT, not a description:
> *the only thing after `gh_sha` is this file.* When a post-wrap commit breaks it, **repoint
> `gh_sha` and re-master this file** — do not let the gate's exit 0 stand in for the sentence being
> true. `--check` classifies by PATH, so it is green whenever the drift is docs-only; it cannot
> tell you that `docs/adr/…` is not `docs/HANDOFF.md`. **`-51` found this by re-reading its own
> preamble when Jason asked whether the handoff was still good. The gate was passing and the
> sentence was false.**

## ORIENT — read these first, in this order
1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff, any
   result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the other
   thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. **`docs/preregistration/CONSTRAINT-INVENTORY-001.md`** — the map for this thread. Fifty reporting
   constraints on two axes: `recog` (MECH / PROXY / READER / n/a — a property of the CONSTRAINT) and
   a **FOR / BINDS / PARTIAL / ADJACENT / TRIPWIRE** grade on the machine cell (a property of the
   ESTATE). **Read §2g first this time** — it is `-51`'s finding, and the paragraph about an
   instrument that printed its loudest red as a green is the one that matters. Then §2f (`-50`),
   §2e (`-49`), §2d (`-48`), §2c (`-47`'s measurement, still the warrant for the ranking), then
   §3.2, then §2a's counts.
3. **`docs/adr/ADR-001-paper-decomposition.md` — THE SEQUENCING DECISION, AND READ §Order of
   publication AND the addenda TOGETHER.** Three preprints, **II → III → IV**, submission is a
   **batch** (`-08`), Definition of Done clauses per paper, monograph only after IV. `-51`
   corrected §Order of publication in place (`842d7f2`) after quoting its stale four-paper order
   to Jason and being caught. **`docs/HANDOFF-PROMPT.md` goes with it** — frozen at `-11`, and it
   carries **WT-079: the deliverable is the paper, not a list of fixes.**
4. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
5. **`python3 scripts/mutation_control.py --list`** — **61 probes now** (48 at `-50`; `-51` added
   `G1`–`G13`). **Read its module docstring before you grade anything** — including the paragraph
   `-51` added about the file it used to name wrongly, and the one that replaces a stale count with
   the command that produces it.
6. **`docs/preregistration/REG-003` §§3.2, 3.3, 7** (`REG-003-p3-recognition-rate-and-off-diagonal.md`)
   — the four-regime ladder, the registered bias asymmetry, the rounding rule.
7. **`docs/scouting/SCOUT-001-paper-III-opposing-team.md`** — **WORKED, NOT PENDING.** Only T2
   remains and T2 is carded and barred on this data. Read it for measurements, not for a to-do list.
8. `REG-012` §§6–7 · `RESULT-REG-012-band-edge-phase` §§4–5 · `RESULT-TERM-001` the five-site
   ruling · `REG-010` **§1 is the population ruling, §4 is the freeze `-46` built** ·
   `CONSTRUCTION-REG-010` **§C2 owns 55.71 % and its population in one sentence**.
9. `RESULT-REG-010` §3 → §4 · **`RESULT-TERM-002`** §2 before §8 · `RESULT-PIN-001` ·
   `RESULT-SCOPE-001` · `CONSTRUCTION-REG-009` (**R5 is load-bearing and unspent**) ·
   `RESULT-REG-009` (**§3's S = 0.1391 is load-bearing in a test**) · `REG-009` (**READ THE HEADER
   NOTE FIRST**; numbering 6–12 by ruling).

> **`-51` in one line: THE INSTRUMENT PRINTED `[GREEN]` — ITS WORD FOR *NO GUARD EXISTS* — FOR A
> MUTATION THAT STOPPED THE SUITE FROM COLLECTING AT ALL.**
> `mutation_control.py` recognised a red by parsing pytest's `FAILED ` lines. `G8` is the first
> probe in this estate ever aimed at a **module** rather than a document; it broke three imports,
> pytest emitted `ERROR ` lines and stopped at collection having run no test, nothing matched, and
> the harness reported the position **unguarded**. **The instrument was anti-monotonic in severity:
> the more damage a probe did, the cleaner its green.** Eight sessions running, the thing that did
> not survive checking was the estate's account of itself — `-44` the `machine` column, `-45` the
> `source` column, `-46` the ranking prose, `-47` the harness's blind axis AND the DO-NOT list,
> `-48` the tee-up's reading, `-49` the tee-up's guard *design*, `-50` the DELIVERY of a correction,
> **`-51` the INSTRUMENT'S ABILITY TO READ ITS OWN OUTPUT.** The git axis is probed: **eleven of the
> thirteen have a probe, nine of those isolating, and the two unreachable ones are measurements with
> reasons, not gaps.**

---

### Transport — darlish, zero-bridge
Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-51`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.
`darlish-check` is **not** in the cloud kit — do not chase its 127.
`roster leave` ONCE at wrap.
**The gate moved to 2.58 during `-51` (the inherited prompt said 2.54).** `gate-selfcheck.sh`
prints the version in force — **trust that line, not this one**, and update this frontmatter
when it disagrees. `-51` found the drift only because the self-check prints it; the gate range
is now `G-A`→`G-AK`.

> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
> dx spawns a **fresh remote shell per call and carries no environment**. Inline on `roster join`,
> `roster claim`, the commit, and every `lessons.py` call — first time, every time.
> **Exception: `export GATE_ROSTER_WHO=…` DOES work inside a script you `--put` and run with
> `bash /tmp/x.sh`**, because that is one shell. `-47` through `-51` all ran their `lessons.py`
> calls that way. The roster brake still prints the **absorbed** row name (`cloud-…`) in its `you:`
> line; cosmetic, not a mis-identity.
> ### ⚠ `roster claim` TAKES `--resource`, NOT `--repo`. `record-outcome` TAKES NO `--id`.
> `roster claim --who <who> --resource <repo> --task "<what>"`; `roster join` takes `--who/--task`.
> **`lessons.py record-outcome <task-tag> pass` is TWO positional args and nothing else.** One call
> resolves every leaf you marked with `use --task <tag>`.
> ### ⚠ NEVER DRIVE `lessons.py use` FROM A LOOP OVER A `grep` OF LEAF FILENAMES. **`-51` DID.**
> Meaning to corroborate the ONE leaf it had built on, `-51` looped over
> `ls lessons/global/ | grep -i correction`, matched **six**, and `record-outcome` then promoted
> **four leaves it had never read**. Corroboration is what lifts a leaf out of quarantine, so an
> unearned `use` is the trust signal lying. **`use` takes an exact id.** Repaired in
> `claude-blackbook` `5a8f7224` and banked; the repair shape is in that leaf, and note that `use`
> auto-pushes on the spot, so it is public before you notice.
> ### ⚠ `lessons.py` AUTO-COMMITS AND AUTO-PUSHES EACH LEAF. **DO NOT HAND-COMMIT AFTERWARDS.**
> `-49`, `-50` and `-51` all hit no brake — every `add`, `use` and `record-outcome` self-committed
> and self-pushed. **LOOK before you reach for a commit**; a hand-commit of already-committed leaves
> is a no-op that reads like a problem:
>
> ```
> /tmp/dx 'cd ~/repos/claude-blackbook && git log --oneline origin/main..HEAD | wc -l'   # 0 = done
> /tmp/dx 'cd ~/repos/claude-blackbook && git status --porcelain'                        # siblings'
> ```
> **`record-outcome` is the exception**: it stages a `passes:` bump and leaves it UNCOMMITTED, so a
> `git status` that is dirty in exactly your corroborated leaves is normal — commit those by path.
> **Siblings' leaves WILL also be dirty and are not yours.** Commit by path, never `-A`.
> ### ⚠ `lessons.py add` SILENTLY FORKS A TWIN ON AN ID COLLISION — CHECK, THEN CURATE.
> `-50`'s collided and was banked as `…-same-2.md`. **Doctrine says curate the ONE leaf.** The move:
> read both, rewrite the ORIGINAL to carry both measurements, name both sessions in `source:`,
> `git rm` the twin, commit by path. `-51` checked with `ls lessons/*/2026-08-15-*` and forked none.
> ### ⚠ `git commit -F <msg> <paths>` CANNOT STAGE AN UNTRACKED FILE.
> Look, add, then commit — the whole move on a shared repo:
>
> ```
> /tmp/dx 'cd ~/repos/<repo> && git status --porcelain'                 # look FIRST
> /tmp/dx 'cd ~/repos/<repo> && git add <only your new paths>'          # never -A, never .
> /tmp/dx 'cd ~/repos/<repo> && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -F /tmp/msg.txt <all your paths, new AND modified>'
> ```
> **`<n>` is the count of YOUR paths, not the staged total.** `-51`'s was 4.
> ### ⚠ SMALL DIFFS DO NOT NEED A TARBALL ROUND TRIP. `-51` PUSHED FOUR FILES WITH `--put`.
> If you edited **N ≤ ~5 files** in the cloud, `cat f | /tmp/dx --put /Users/jasoncbraatz/repos/wealth-tensor/<path>`
> per file is one call each, prints a **sha256 verified against darwin**, and skips the tar/chown/
> AppleDouble dance entirely. Then run the suite on darwin and commit there. The tarball stanza
> below is for **coming down** (cloud needs the tree) — it is not the way back up.
> ### ⚠ WRITE PYTHON PATCH SCRIPTS TO A FILE. **`-51` LOST A ROUND TRIP TO NESTED-STRING ESCAPING.**
> A patch script that embeds a block of Python inside a Python string inside a heredoc has three
> levels of `\n` escaping and the middle one is silent: the block was written with real newlines
> inside its string literals and `mutation_control.py` came back with an unterminated string. The
> move is `Write` the block to `/tmp/block.py` as ORDINARY code, then a three-line inserter reads
> both files and splices. `git checkout <file>` is the free undo; take it early rather than debug
> the escaping.
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
> `-51` measured **20,183,651 bytes** at `281421c`, `verified against darwin` in words, and
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

| | at `HEAD` = `3f63237` (verified in `-51`, both machines, same hour) |
|---|---|
| collected | **1055** (was 1048 at `142d386`; `-51` added 7) |
| cloud, FULL tarball (`PYTHONPATH=/root/wtg/src`) | **1055 passed**, **~170 s**, **zero skips** |
| darwin (`.venv/bin/python -m pytest`) | **1055 passed**, ~63 s |
| cloud **without** `.git` | **1034 passed, 14 skipped** — unchanged; the axis is probed, not narrowed |

`scripts/defensive_count.py` **takes a positional `path`** and errors without one.
`pytest -m tripwire` selects the four-file tripwire class; `-m "not tripwire"` excludes it.

> ### ⚠ PROBE TIMING, RE-MEASURED. A GIT PROBE IS NOT SLOWER, BUT THERE ARE THIRTEEN MORE OF THEM.
> A cloud container is **2 CPUs**; the sweep is `--jobs 2`. `-50` measured ~3 min 30 s per probe and
> `-51` measured the same for the `G` family — `{"git": True}` copies `.git` (~20 MB) and costs
> nothing noticeable. **Thirteen probes at `--jobs 2` is ~25 minutes**, and a single foreground
> `Bash` call is killed at **10 minutes**: run with `nohup … &` into a file and poll with
> `sleep N; tail`. **Do not poll with `while pgrep`.** Prefer `--out <json>` and read the JSON —
> `-51` mis-counted a catcher list by `awk`-ing the log between two slugs, and probes print in
> **completion order**, not argument order, so log-slicing interleaves. The JSON is per-probe and
> exact. **Budget for running the sweep twice**; `-49`, `-50` and `-51` all found a real defect on
> the second run and all three would have shipped it on the first.

---

## 0 · THE TELL, NOW IN SIXTY-ONE SHAPES
Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL GONE QUIET (`-32`). `-33`: instruments that agree with themselves; a
guard must scan assertions, not quotations. `-34`: defects nobody introduced. `-35`: defects you are
about to introduce. `-36`: pre-commit the FAVOURABLE outcome's meaning. `-37`: a mutation that does
not mutate reports your guard as weak. `-38`: a statistic can be a tautology in measurement's
clothing. `-39`: a handoff silently outranks a doctrine leaf; **assert the EXACT exit code**.
`-40`: a STALE NEGATIVE closes a question harder than an open one. `-41`: **a hand-audit that found
N sites found them through ONE DOOR.** `-42`: a constraint can be CONDITIONAL and its guard must
assert its ANTECEDENT. `-43`: **feed the registration its own forbidden claim before you trust the
green**; a non-vacuity test must assert the CONJUNCTION. `-44`: a column that names a guard is a
COVERAGE CLAIM and nobody ever verifies it. `-45`: a `source` cell is a PROVENANCE claim; **a
quotation is a lossy copy and the first things it loses are the ANTECEDENT and the REFERENT.**
`-46`: a coverage count read off the `machine` column is a claim about the COLUMN; a reproducibility
pin is not a freeze. `-47`: **a mutation the harness cannot see reports every guard in the unseen
part of the estate as absent**; *untracked* and *gitignored* are different facts. `-48`: a handoff's
CHARACTERISATION of a document is not a MEASUREMENT of it. `-49`: a handoff's proposed GUARD DESIGN
is the next unchecked surface after its counts; for a conjunction guard the UNIT is a design choice.
`-50`: **a correction that lives only in a handoff has not been made**; a homograph count is not a
homograph audit; any self-test reading the real document is a second catcher unless it skips on a
dirty base.

**`-51` adds six** — four from the at-bat, two from the coda Jason's wrap-up questions produced:

- **A RED THE HARNESS CANNOT *PARSE* REPORTS THE GUARD AS ABSENT — AND THE LOUDEST RED IS THE ONE IT
  CANNOT PARSE.** `mutation_control.py` matched `^FAILED (tests/\S+)`. A probe that mutates a
  **module** breaks an import; pytest reports those files as `ERROR`, and past a handful it stops at
  collection having run no test at all — so nothing matched and `G8` printed `[GREEN]`, this
  instrument's word for *no guard exists*. **Anti-monotonic in severity: the more damage, the
  cleaner the green.** Every earlier probe edited a document or a JSON file, which cannot break an
  import, so the blindness was there from day one with nothing to reveal it. Fixed (`-rfE`,
  `CATCHER_RE`, `is_unparsed_red`), pinned in `tests/test_mutation_control_reads_errors.py`, and
  **`R5a`–`R5e` re-run under the fixed harness all returned `rc=0`, so no recorded grade moved** —
  a harness repair is a claim about every measurement ever taken with it. Banked:
  `2026-08-15-mutation-harness-recognises-red-parsing-pytest`.
- **A CORRECTION APPLIED TO ONE ARTEFACT WHILE A SECOND ASSERTS THE SAME CLAIM HAS A LIVE
  RESERVOIR — AND THE RESERVOIR IS THE INSTRUMENT.** `-47` diagnosed that C07's row had inherited
  `test_registrations_precede_their_instruments.py` *"because the names rhymed"* and corrected the
  inventory — leaving the identical claim in `mutation_control.py`'s docstring, which ORIENT tells
  every session to read **before grading anything**. `-50` read it and wrote it into its
  pre-measurement. `-51` ran `R1`: its sole catcher is
  `test_reg001_sec5_no_amendment_after_result.py`. **Grep the CLAIM, not the file.** Banked:
  `2026-08-15-correction-applied-one-artefact-while-second`.
- **A RESIDUAL OF (TOTAL − SPENT) CAN HAVE A RIGHT TOTAL AND A WRONG ATTRIBUTION, AND THE RIGHT
  TOTAL IS WHAT MAKES THE WRONG ATTRIBUTION INVISIBLE.** `13 = 14 − 1` is correct whichever test
  the 1 is. `-50` ran the command for the total — the durable repair `-47` asked for — and took the
  attribution from prose, **in the same bullet**. The subtraction is an instrument; the map is a
  claim. Banked: `2026-08-15-residual-computed-total-minus-spent-can`.
- **A PROBE WHOSE MOVE IS *"INTRODUCE AN IDENTIFIER NO INSTRUMENT NAMES"* CANNOT NAME IT, BECAUSE
  THE HARNESS LIVES INSIDE THE ESTATE IT MUTATES.** `G11`'s first draft wrote its chosen SHA into a
  docstring under `scripts/`; the guard asks whether the SHA appears anywhere under
  `scripts/tests/src`; the probe came back **GREEN, entirely correctly**. The probe's documentation
  of the identifier's absence is what falsified its own precondition. Choose such identifiers at run
  time. Banked: `2026-08-15-probe-whose-forbidden-move-introduce-identifier`.

- **AN AMENDMENT RECORDED AS AN *ADDENDUM* HAS NOT AMENDED THE DECISION — AMEND THE CLAUSE.**
  `ADR-001` §Order of publication said **II → III → I → IV** for five days after the `-10` addendum
  folded Paper I into IV and recorded **II → III → IV** in its own "What changes" table. `-51`
  quoted the stale heading to Jason while summarising what the estate had already decided, **and
  Jason caught it.** The addendum had literally predicted this in its closing line — *"a corpus
  that quietly becomes three papers, in a repository whose central document says four, is a
  contradiction a future session would find the hard way."* **Predicting a failure mode in the same
  document you decline to fix is not a mitigation.** Strike the superseded clause in place, keep the
  old reasoning struck-through as the record, and reserve the addendum for the WHY. Fixed in
  `842d7f2`. Banked: `2026-08-15-amendment-recorded-addendum-has-not-amended`.
- **WHEN AN AUDIT KEEPS PRODUCING FINDINGS, CHECK WHAT THE FINDINGS ARE *ABOUT* BEFORE READING THE
  RATE AS A REASON TO CONTINUE.** This programme found two live violations in its first two sessions
  and then produced **eight consecutive findings every one of which was about the audit apparatus
  itself.** A high finding rate against the instrument is evidence the instrument is deep, not that
  the artefact is unsafe. Two cheaper questions decide it: **are the findings about the SUBJECT or
  the INSTRUMENT**, and **does the artefact still get EDITED** (regression guards are worth most on
  living code and least on something about to be frozen and posted). Banked:
  `2026-08-15-audit-programme-keeps-producing-findings-check`.

**Everything `-33` through `-50` banked is unchanged and still sharp.** `severity.check`'s witness
must return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory.
`patchkit` anchors have **no internal newline**.

---

## 1 · WHAT HAPPENED
**Twenty minutes on the documents before a line of test code, for the fourth session running, and
for the fourth session running that is where it was won.** The at-bat was `-47`'s residual, open
since `-47`, deferred three times, and `-50` pre-measured it so `-51` inherited numbers rather than
a characterisation. **The numbers were right and the map was not**, which `-51` found by doing what
§3 said and running one probe before writing a design: `R1`, whose catcher list disagreed with the
sentence that sent it there.

**One new file, 7 tests, green on both machines: `tests/test_mutation_control_reads_errors.py`** —
the first test in this estate whose subject is **the measuring instrument**, not the manuscript.

| what | how |
|---|---|
| **the harness fix** | `-rf` → `-rfE`; recogniser hoisted to `CATCHER_RE` and matching `ERROR`; `is_unparsed_red(rc, catchers)` gives *did-not-complete-and-nothing-attributable* its own printed state, which is not green |
| **both halves pinned separately** | fixing only the recogniser leaves the defect reachable through a collection stop, so the recogniser and the rc rule are two tests, not one |
| **CONTRIBUTION, not presence** (`-49`/`-50`) | the recogniser test asserts what adding one `ERROR` line does to a FIXED transcript, which a match-everything regex cannot satisfy; a third test denies it the non-`tests/` path, the prose mention and the indented line |
| **the conjunction asserted** (`-43`) | `is_unparsed_red(2, ["tests/x.py"])` is False — asserting only the rc leg would flag every hard-stopped run whose reds we can in fact read |
| **the flag pinned** | both halves are correct and useless if `-rf` comes back; the invocation is asserted in its own test |
| **the fix proved red on the old harness** | the pre-fix regex and rc rule were replayed by hand against the same transcript: contribution assertion **False**, `unparsed(2,[])` **False → GREEN**. `-43`'s rule applied to a repair |

**The thirteen, and the grading (on the reds, `-44`).** `G1` → 1 · `G2` → 3, all in the guard's own
family · `G3` → 3 (1 owned, 2 genuine document-name catchers) · `G4` `G5` `G6` → 1 each, three limbs
three clean owns · `G7` → 1 · `G8` → 3 (owned + two genuine `test_tag_resolution.py` siblings)
· `G9` → 2 · `G11` → 1 · `G13` → 1. **Eleven of thirteen probed, nine isolating.**

**The two that are not, recorded as measurements rather than gaps** (`-46`): `G10` establishes that
`test_both_documents_are_in_history` is **unreachable from the working tree** — `git rev-list HEAD --
<path>` matches commits that touched the path *in history*, so after the rename two commits still
resolve and the suite stays `rc=0`; **its docstring claimed a rename would empty it and that is
measurably false**, repaired in the same commit. `G13` establishes that
`test_the_pinned_digest_is_the_version_REG_012_saw` reads the blob at `ba59370`, so the §4.7 freeze
is owned by `test_section_47_is_byte_identical_to_the_pin` — a different, non-git test — and the
git-gated one is a self-consistency check on immutable history. `G12` is kept and **labelled
non-isolating in its own `--list` description**: it catches its target inside a list of **196**.

**BUG SPRAY, on myself, twice.** (1) `G8`'s first draft renamed the `TIER_TAGS` block, which is what
exposed the harness defect — but once the harness could see it, the probe was still red *for the
wrong reason*: collection died before the digest guard ran. Narrowed to editing one registered tag
string, and it now catches its own guard. **A mutation big enough to stop the suite cannot tell you
which guard saw it.** (2) `G11`'s self-referential literal, above. Both found on the second sweep run.

**BUG SPRAY, third, and it was not in this repo:** the `lessons.py use` loop that corroborated four
leaves this session never read. Reverted and pushed (`claude-blackbook` `5a8f7224`), banked, and
written into the transport block above.

**Inventory edits:** **new §2g** carries the harness finding, the attribution correction, the
thirteen-row table, the two unreachable invariants and the `R5a`–`R5e` re-run · §2c's C07 sentence
now **names the right machine** and points at §2g.
**Instrument edits:** `mutation_control.py`'s docstring no longer names the wrong file, and says why
it mattered · `test_reg001_sec5_no_amendment_after_result.py`'s docstring corrected.

| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** — the manuscript was not touched this session |
| **G-COACH-1** | held — the wrong-file claim and the wrong docstring were fixed **in-session**, in the same commit, and this entry names the files |
| **G-COACH-5** | held — the strength named is **the sweep run TWICE**, third consecutive session where the second run produced the finding. `-51` adds a second: **run ONE probe before writing a design.** `R1` took four minutes and disproved the sentence the whole at-bat was framed by |
| suite | **1055 collected** · darwin **1055 passed** (~63 s) · cloud **1055 passed, zero skips** (~170 s) · without `.git` **1034 / 14 skipped**, unchanged |
| new tests | 1 file, 7 tests · **13 new probes (48 → 61)** |
| lessons | **five** banked global + **one** project-scoped · corroborated `record-outcome wealthTensor-51 pass`, then **un-corroborated four that were stamped in error** |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |

### The coda — what Jason's wrap-up questions produced, AFTER the gate had passed

**`-51` was wrapped, gated and off the roster when Jason asked two ordinary questions: *paste the
handoff*, and *how many more handoffs do you estimate?* The second one could not be answered without
reading `ADR-001`, and nobody had read it in ten sessions.** Everything below came from that.

| what | outcome |
|---|---|
| **the estate had drifted off its own written sequencing decision** | `ADR-001` (II → III → IV), `HANDOFF-PROMPT.md` (**WT-079: the deliverable is the paper**), and the `-08` batch ruling were never in dispute — they were just not what `-42`→`-51` did. §3 carries the measurements |
| **`ADR-001` §Order of publication was five days stale** | `-51` quoted it to Jason; **Jason caught it**; corrected in place at `842d7f2`, item 3 struck-through not deleted |
| **two things `-51` told Jason were WRONG** | (1) *"no Definition of Done exists"* — it does, per-paper clauses plus corpus-level *"Three preprints publicly posted…"*; (2) papers do **not** ship individually — the `-08` ruling makes the order a **batch**, so a paper's terminal state is *ready to submit* |
| **`gh_sha` repointed `3f63237` → `842d7f2`** | the ADR commit broke the preamble's invariant. See the preamble: the gate was passing and the sentence was false |
| **the at-bat retargeted** | §3 is now Paper III toward ready-to-submit; the guard track is **paused, not abandoned**, with three scoping proposals recorded and marked **UNRULED** |
| **`paper-IV.md` DOES NOT EXIST** | and nothing posts until it does. **IV is the long pole, not III** — measured from the `docs/papers/` listing, and no session has ever claimed it |

**BUG SPRAY, on myself, a fourth time — and this one is the sharpest.** Re-mastering this file,
`-51` wrote a **full 40-character `gh_sha` it had never seen**, expanding the abbreviation
`842d7f2` from imagination. It was caught in the same breath and replaced with
`git rev-parse 842d7f2`'s real output. **An abbreviated SHA is a HANDLE and a full SHA is a
CLAIM**, and this estate's entire PIN-001 lineage is about SHAs that live in prose being unguarded
by construction. **Never type a SHA you have not resolved. `git rev-parse` is one call.**


---

## 2 · RULINGS — DO NOT REOPEN
- All of `-31`'s through `-50`'s rulings stand **verbatim**: no third disclosure instrument; phrase
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
  DISCRIMINATOR IS *IS THIS A STATISTIC***; **C44's DISCRIMINATOR IS THE REFERENT AND ITS RESOLUTION
  IS THE CLAUSE**; **C46's AND C41's DISCRIMINATOR IS THE POLARITY**; **AN OVER-BREADTH OR
  NON-VACUITY SELF-TEST IS PREDICATED ON CONTRIBUTION, NOT ABSENCE**; **C10 GOVERNS THE SUBSTITUTION,
  NOT THE TOKEN, AND ITS RESOLUTION IS THE SENTENCE**; **C10's THIRD SURFACE IS `wt088` AND NOTHING
  ELSE**; **A CORRECTION IS NOT MADE UNTIL THE ARTEFACT IS EDITED**.
- **NEW · C07's MACHINE IS `test_reg001_sec5_no_amendment_after_result.py`, MEASURED FROM `R1`'s
  CATCHER LIST.** `test_registrations_precede_their_instruments.py` is a guard on a *different*
  invariant — commit-order at INTRODUCTION — and its own docstring says it cannot see C07's move.
  Three artefacts said otherwise at some point; two are corrected and the third (`-50`'s handoff) is
  superseded by this file. **If a sentence tells you which guard covers a constraint, run its
  probe.**
- **NEW · A GREEN FROM `mutation_control.py` IS ONLY A MEASUREMENT IF THE RUN COMPLETED.** `rc=0`
  with no catchers is the real thing; anything else with no catchers now prints `[UNPARSED RED]` and
  **must not be graded**. Do not re-introduce `-rf`; the test will tell you.
- **NEW · G10 AND G13 ARE ESTABLISHING PROBES AND ARE EXPECTED GREEN.** Their green IS the
  measurement — do not "fix" them into reds, and do not count their invariants as unguarded. §2g.
- **NEW · G12 IS NON-ISOLATING (196 CATCHERS) AND ITS RED IS NOT COVERAGE.** Kept deliberately;
  the reason is in its `--list` description and in §2g.

---

## 3 · THE AT-BAT for `-52` — **PAPER III, TOWARD READY-TO-SUBMIT. JASON'S RULING, 2026-08-15.**

**THE GUARD PROGRAMME IS PAUSED, NOT ABANDONED, AND THIS IS THE OUT-LOUD SAYING-SO.** Jason asked
`-51` at wrap how many handoffs remained; the answer required reading `ADR-001`, and reading it
found that **the estate had drifted off its own written sequencing decision without ever recording
a decision to drift.** `ADR-001` §Order of publication (corrected in place, `842d7f2`) says
**II → III → IV**; `docs/HANDOFF-PROMPT.md` says **WT-079 · THE DELIVERABLE IS THE PAPER, NOT A
LIST OF FIXES**; and the `-08` addendum says nothing ships until the corpus is done. None of that
was ever in dispute. It was simply not what sessions `-42` through `-51` did.

**THE MEASUREMENTS THAT SETTLED IT — all re-derivable, none a characterisation:**

- `docs/HANDOFF-PROMPT.md`, the standing prompt naming the deliverable, is **frozen at `-11`**.
- `docs/LEDGER.md`'s last entry is **WT-088, `-14`**. Thirty-seven sessions, zero research entries
  — which every recent handoff has been reporting under stopping rules and nobody read as a signal.
- `CONSTRAINT-INVENTORY-001` was built at `-42`, **nine days after the ADR and two days after the
  pre-posting dossier**, and its own header scopes it: *"The point of this file is the LIST"* and
  *"this is an inventory, not a ruling."* **It never claimed to be a gate on posting.** The
  escalation from *enumerate* to *build a machine for each of the fifty* happened implicitly, via
  §3.2's RANKING — and a ranking is a priority order, not a mandate to exhaust.
- The sweep's payload landed early: **50 constraints, 48 compliant or not-live, 2 violated**
  (C12, C21), both FOUND. Everything since is regression insurance.
- **All eight findings from `-44` to `-51` are about the estate's account of ITSELF. Not one is
  about the manuscript.** A high finding rate against the instrument is evidence the instrument is
  deep, not that the paper is unsafe.
- `paper-III.md` is **32,831 words on disk**. `REVIEW-004-pre-posting-dossier.md` opens:
  *"Nothing here is a reason not to post."*

**WHAT "DONE" MEANS, AND IT WAS ALREADY WRITTEN DOWN — `-51` SAID IT WAS NOT AND WAS WRONG.**
`ADR-001` carries per-paper **Definition of Done** clauses and the corpus-level one, amended to
**"Three preprints publicly posted…"**. And by the `-08` ruling the order is a **submission BATCH,
not a schedule**: *"ready to submit"* is a paper's terminal state and nothing posts until II, III
and IV all reach it. **So your at-bat is III toward READY-TO-SUBMIT. It is not "post III."** Do
not ask Jason to trigger a submission.

**OPEN WITH THE TWENTY MINUTES, AIMED SOMEWHERE NEW.** You are the first session in ten to open
`paper-III.md` with intent to change it. Read `docs/HANDOFF-PROMPT.md` §STEP 2's four rules first
— **WT-079** (a straw man in the prose, in the file; not a memo of fixes), **WT-078** (coaches not
umpires), **WT-080** (run the math before writing the finding), **WT-081** (contribute and have
fun). Then `REVIEW-004` as INPUT, never as a template. Then measure, do not characterise, what
still stands between III and ready-to-submit: the ADR's per-paper Definition of Done clause is the
checklist, and `§Consequences`'s missing-apparatus list (abstract, keywords, JEL codes,
contributions list, limitations, data/code availability, *Independent researcher*) is cheap and
may already be partly done. **Nobody has measured which of those III currently has. Do that
before you write a word of prose** — it is this thread's whole method, pointed at the paper.

**THE AUDIT IS KEPT, AND JASON ASKED FOR IT TO BE SCOPED MORE FORMALLY AND RUN MORE EFFICIENTLY.**
`-51` proposed three moves and **Jason has not ruled on them — do not treat them as decided:**
1. **Audit the CLASS, not the constraint.** All eight recent findings are one species: a sentence
   about the repo that drifted from the command that produces it. ONE linter over claims naming a
   count, a filename or a coverage fact — each required to carry the command that regenerates it
   — would have caught `-44`, `-45`, `-46`, `-47`, `-50` and `-51` in a single pass. `-51` banked
   the seam: **grep the CLAIM, not the file.**
2. **Bound by value, not by list.** §3.2 ranked 7 positions and 3 remain (the forbidden-claim
   family C16/C20/C23/C25/C30, C45, the reportable-at-all family). The other ~19 in cell (b) were
   never argued to be worth machines.
3. **Audit at the BOUNDARY, not continuously.** Guards protect against edits, and III is about to
   be heavily edited. Run the guard pass **after III freezes** — worth most, costs least.
**And the higher-level audit Jason asked for already exists, designed and unclaimed:** the `-08`
addendum's **end-to-end test** — *"the end-to-end test is itself a deliverable and has [nobody
claimed it]"* — is the conjunction-level severe test his own methodological position calls for,
and the `-10` addendum notes it is **easier to pose for three papers than four**. It is the
natural successor to the parts-level guard programme, and it belongs after IV.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE** — and if you take a guard, say why it beats
the paper, because for ten sessions nobody asked that question.

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
4. **Cell (b), ranked in §3.2 — THREE entries left, still MEASURED (§2c), and now PAUSED behind
   the paper by Jason's 2026-08-15 ruling.** The forbidden-claim family (C16/C20/C23/C25/C30,
   probes `R5a`–`R5e`, **all five re-verified `rc=0` under the repaired harness by `-51`**) ·
   C45's two assertions · the reportable-at-all presence guards. **Paused is not abandoned**: the
   ranking is measured and still good, and §3 carries the three scoping proposals Jason asked for
   and has not yet ruled on. Do not silently resume this track — if you take it, say why it beats
   Paper III.
5. **C37's tripwire** — `REG-009` §12's *"never by narration"*. §3.3 names the adjacent check.
6. ~~**`-47`'s residual, the git axis**~~ — **DONE (`-51`)**, `G1`–`G13`, §2g. What remains is not a
   gap but two recorded unreachables and one non-isolating probe; **do not re-open them as work.**
   The live follow-on is smaller and real: **no probe in this estate has ever mutated `src/`
   except `G7`/`G8`.** The module surface is where the harness was blind, and it is thin.
7. **§7's ledger dilutes its own two load-bearing rows — Jason's call, and it is TRIPWIRED, not
   carded.** `test_tripwire_c36_sec7_ledger_shape.py` will ask him the moment the shape moves. **Do
   not card it and do not ask him pre-emptively.**
8. Infra siblings, carded, Claude-hands: Caddy ordering `1217488447555628` · capability path in
   cleartext + repo drift `1217488117177482`.
9. AAR A2's residual — the other four `post-*` hooks · card-lint `1217483699706758` · gate
   `1217465036940491`.
10. Dossier era, re-served by nobody: `REVIEW-004` **C6** (ASC 410) and **C10** (IAS 36's reversal
    asymmetry, a free cross-regime falsification test). *(That `C10` is REVIEW-004's, not the
    inventory's — different numbering space, and the collision has now bitten three times. Say which
    C10 you mean, always.)*
11. Phrase-set passenger: 30.4 % match only `events or circumstances`; 7.9 % safe-harbour. Outranked.
12. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
13. Not mine, not touched: handoff-lint warns on `HANDOFF-acmeLedger-07.md:22`, `-09.md:36,42`, and
    `-12.md` / `-13.md` carry items with ZERO `verify:` lines. **Leave them alone.**

---

## 5 · DO NOT
* Everything `-31`→`-50` forbade still stands verbatim — R5, the two sensitivities,
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
  **DO NOT DELETE `RESULT-REG-010`'s REFUSAL SENTENCES**, **DO NOT WIDEN C10 TO EVERY OCCURRENCE OF
  `E4`**, **DO NOT MOVE C10's DETECTOR TO CLAUSE RESOLUTION**, **DO NOT SCAN `scripts/` REPO-WIDE
  FOR `E4`**, **DO NOT QUOTE THE GIT-SKIP COUNT FROM PROSE — RUN THE COMMAND**, **DO NOT LEAVE A
  FINDING IN A HANDOFF WITHOUT EDITING THE ARTEFACT IT CORRECTS**. §2.
* **NEW · DO NOT REVERT `mutation_control.py` TO `-rf`, AND DO NOT READ A `[GREEN]` WITHOUT ITS
  `rc`.** A green is a claim that the estate is unguarded at that position. `rc=0` earns it;
  anything else with no catchers is `[UNPARSED RED]` and earns nothing.
* **NEW · DO NOT WRITE A PROBE'S TARGET IDENTIFIER AS A LITERAL IN THE PROBE.** If the constraint is
  about an identifier appearing nowhere under `scripts/tests/src`, the probe's own source is inside
  that search space. Choose it at run time. `G11`.
* **NEW · DO NOT MAKE A PROBE BIGGER TO MAKE IT REDDER.** `G8`'s first draft stopped collection and
  its catcher list was two import errors, with the guard it was aimed at never having run. **A
  mutation big enough to stop the suite cannot tell you which guard saw it.**
* **NEW · DO NOT SLICE THE SWEEP LOG BY SLUG.** Probes print in **completion** order, not argument
  order. Use `--out <json>`.
* **NEW · DO NOT DRIVE `lessons.py use` FROM A `grep` OVER LEAF FILENAMES.** Exact ids only. An
  unearned corroboration is the trust signal lying, and it auto-pushes before you notice.
* **NEW · DO NOT TYPE A FULL SHA YOU HAVE NOT RESOLVED.** `-51` expanded `842d7f2` into a
  fabricated 40-character `gh_sha` while re-mastering this file and caught it one line later. An
  abbreviated SHA is a handle; a full SHA is a claim. `git rev-parse <short>` is one call, and
  `RESULT-PIN-001` is the whole reason this estate cares.
* **NEW · DO NOT LET `handoff_gate.py --check`'s EXIT 0 STAND IN FOR THE PREAMBLE BEING TRUE.** It
  classifies by PATH, so any docs-only drift is green — including a `docs/adr/…` commit that makes
  *"the only thing added after it is this file"* false. If a post-wrap commit lands, **repoint
  `gh_sha` and re-master.**
* Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud.
* Do not poll a background probe run with `while pgrep` — the 10-minute tool ceiling eats it.

---

## 6 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.

Coffee status: ☕ **SEVENTEEN SESSIONS RUNNING, AND THE FIRST TWENTY MINUTES DECIDED THE WHOLE
SESSION AGAIN** — `-44` whether the thing guarding it can see it, `-45` whether the address on it
was right, `-46` whether the sentence that sent you here was ever checked, `-47` whether the
instrument can see the whole board, `-48` whether the sentence that sent you here had ever opened
the document, `-49` whether the machine that sentence told you to build had ever been run, `-50`
whether the correction somebody already made ever reached the file it was about, **`-51` WHETHER THE
INSTRUMENT CAN READ ITS OWN OUTPUT.** It went: run `R1`, read four lines of catcher list, notice
they name a different file than the sentence that sent you. Four minutes. Then thirteen probes, and
the thirteenth-from-last came back GREEN on a mutation that had stopped the suite dead — and green,
in that instrument's own words, means *no guard exists*. **The estate had been asking its instrument
what it could not see. It had never asked what it could not READ.**
