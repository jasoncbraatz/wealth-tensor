---
project: wealth-tensor
gh_sha: 4e85254c3d58b0921622d4c4a014b28359a02178
updated: 2026-08-15
session: wealthTensor-48
gate_passed: true
gate_version: "2.51"
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
   ESTATE). **Read §2d first this time** — it is `-48`'s finding, and the paragraph about the
   tee-up is the one that matters. Then §2c (`-47`'s measurement, still the warrant for the
   ranking), then §3.2, then §2a's counts.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`python3 scripts/mutation_control.py --list`** — 42 probes now. **Read its module docstring
   before you grade anything**, including `-47`'s section on why `.git` is opt-in.
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

> **`-48` in one line: THE DOCUMENT WAS COMPLIANT AND THE HANDOFF'S REASON FOR SAYING SO WAS FALSE,
> AND A GUARD BUILT FROM THAT REASON WOULD HAVE GONE RED ON A WITNESS THAT WAS NEVER WRONG.**
> `-47` teed up C26 with a measurement of its *rank* and a characterisation of its *document*:
> *"`RESULT-REG-006` already carries `impairment` eleven times, every one of them qualified."* It
> carries it **twelve** times and **two are bare**. The document complies anyway — because `-45`
> restored the clause's referent, *never appears **in it** unqualified*, where *it* is **the file's
> own statistics**. That turns the guard's question from *is this occurrence qualified* into *is
> this occurrence naming a statistic*, and under the first question the real document fails at two
> lawful sites. **Five sessions running, the estate's prose about itself is the thing that did not
> survive checking**: `-44` the `machine` column, `-45` the `source` column, `-46` the ranking
> prose, `-47` the harness AND the DO-NOT list, `-48` the tee-up's reading of its own document.
> C26 is **BUILT** and graded **FOR** on `R2a` and `R2b`, one catcher each.

---

### Transport — darlish, zero-bridge
Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-48`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.
`darlish-check` is **not** in the cloud kit — do not chase its 127.
`roster leave` ONCE at wrap.

> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
> dx spawns a **fresh remote shell per call and carries no environment**. Inline on `roster join`,
> `roster claim`, the commit, and every `lessons.py` call — first time, every time.
> **Exception: `export GATE_ROSTER_WHO=…` DOES work inside a script you `--put` and run with
> `bash /tmp/x.sh`**, because that is one shell. `-47` and `-48` both ran their `lessons.py` calls
> that way; `-48` confirms it, with one wrinkle worth knowing — the roster brake still prints the
> **absorbed** row name (`cloud-…`) in its `you:` line, which is cosmetic and not a mis-identity.
> ### ⚠ `roster claim` TAKES `--resource`, NOT `--repo`. `record-outcome` TAKES NO `--id`.
> `roster claim --who <who> --resource <repo> --task "<what>"`; `roster join` takes `--who/--task`.
> **`lessons.py record-outcome <task-tag> pass` is TWO positional args and nothing else.** One call
> resolves every leaf you marked with `use --task <tag>`.
> ### ⚠ `lessons.py`'s AUTO-COMMIT IS BLOCKED BY THE ROSTER BRAKE WHEN A SIBLING HOLDS THE REPO.
> New leaves commit and push themselves fine. **`record-outcome` does not** — it writes the outcome
> into three existing files and the brake reads that shape as `git add -A` under contention, prints
> `BLOCKED`, and leaves them staged-but-uncommitted. **Nothing is lost and the gate will not catch
> it, because the files are staged.** `-48` finished the job by hand and you will have to too:
>
> ```
> /tmp/dx 'cd ~/repos/claude-blackbook && git status --porcelain'
> /tmp/dx 'cd ~/repos/claude-blackbook && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -m "lesson(outcome): …" <exactly your leaf paths> && git pull --rebase -q && git push'
> ```
> ### ⚠ `git commit -F <msg> <paths>` CANNOT STAGE AN UNTRACKED FILE.
> Look, add, then commit — the whole move on a shared repo:
>
> ```
> /tmp/dx 'cd ~/repos/<repo> && git status --porcelain'                 # look FIRST
> /tmp/dx 'cd ~/repos/<repo> && git add <only your new paths>'          # never -A, never .
> /tmp/dx 'cd ~/repos/<repo> && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -F /tmp/msg.txt <all your paths, new AND modified>'
> ```
> **`<n>` is the count of YOUR paths, not the staged total.** `-48`'s was 3.

**COMMIT BY PATH ON `claude-blackbook`, ALWAYS.** `git status --porcelain` first; if a sibling's
leaves are staged, commit by path.

> ## ⚠ ONE TARBALL. THE TWO-TARBALL STANZA IS RETIRED AND `-48` RE-CONFIRMS THE REPLACEMENT.
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
> `-48` measured **19,845,361 bytes** at `6f021ee`, `verified against darwin` in words, and
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

| | at `HEAD` = `4e85254` (verified in `-48`, both machines, same hour) |
|---|---|
| collected | **1018** (was 1007 at `acaa406`; `-48` added 11) |
| cloud, FULL tarball (`PYTHONPATH=/root/wtg/src`) | **1018 passed**, ~235 s, **zero skips** |
| darwin (`.venv/bin/python -m pytest`) | **1018 passed**, ~65 s |

`scripts/defensive_count.py` **takes a positional `path`** and errors without one.
`pytest -m tripwire` selects the four-file tripwire class; `-m "not tripwire"` excludes it.
A cloud container is **2 CPUs** — the sweep is `--jobs 2`, ~2 min per probe. **The cloud suite is
now ~4 minutes, not ~2** (`-48` added 11 fast tests; the growth is in `test_lag_shape_*`, unrelated).
Budget one probe per limb you build, not per limb that exists.

---

## 0 · THE TELL, NOW IN FORTY-NINE SHAPES
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
**`-48` adds three:**

- **A HANDOFF'S CHARACTERISATION OF A DOCUMENT IS NOT A MEASUREMENT OF IT, AND BUILDING A GUARD
  FROM THE CHARACTERISATION CAN SEND YOU TO REPAIR A COMPLIANT ARTEFACT.** Eleven-and-all-qualified
  was twelve-and-two-bare. The tee-up names the at-bat; it does not measure the field. **Count the
  occurrences yourself before you write the first assertion** — it cost four tool calls. Banked:
  `2026-08-15-handoff-s-characterisation-document-not-measurement`.
- **WHEN A CONSTRAINT'S REFERENT DECIDES ITS SCOPE, THE REFERENT IS THE GUARD'S DISCRIMINATOR — NOT
  A FOOTNOTE ABOUT IT.** *"…never appears **in it** unqualified"* and the same sentence without
  *in it* are **different predicates**, and only one of them is green on a compliant document.
  `-45` restored two words and thereby chose this guard's algorithm two sessions early. **Pin the
  referent with its own assertion** so a later rewrite that drops it fails loudly instead of
  silently widening the rule — `test_the_referent_is_still_the_files_own_statistics` is that pin.
  Banked: `2026-08-15-constraint-s-referent-decides-its-scope`.
- **WHEN A RULE FORBIDS AN UNQUALIFIED WORD, THE LAWFUL EXCEPTIONS ARE THE SITES WHERE THE
  GENERALITY IS THE POINT, AND QUALIFYING THEM WOULD MAKE THE SENTENCE WRONG.** *"1,400 firms
  recording an impairment"* is bare because it means **any** impairment, tagged or folded — the
  exact undifferentiated thing Q1 exists to keep out of the statistics. Do not repair such a site,
  and **do not leave it unpinned**: pin it verbatim with the adjudication plus an assertion that it
  has not since acquired a ratio. Banked: `2026-08-15-rule-forbids-unqualified-word-lawful-exceptions`.

**And one about scoping a placement rule**, banked as
`2026-08-15-placement-constraint-printed-next-ratio-has`: *next to* has a machine reading inside a
**table row** and only a judgement call inside a paragraph, so **sweep the rows and pin the prose**.
Two mechanisms in one guard is narrower than one sweep and honest about being narrower.

**Everything `-33` through `-47` banked is unchanged and still sharp.** `severity.check`'s witness
must return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory.
`patchkit` anchors have **no internal newline**.

---

## 1 · WHAT HAPPENED

**Twenty minutes on the document before a line of test code, and that is where the session was
won.** The tee-up said *eleven, all qualified*; a wrap-aware scan said **twelve, two bare**. Reading
`§2`'s provenance audit then produced the reason the document is compliant anyway — `-45`'s restored
referent — and the referent, not the tee-up, is what the guard was built from.

**One new file, 11 tests, green on both machines: `tests/test_reg006_sec3_q1_two_limbs.py`.**

| what | how |
|---|---|
| **LOST WARRANT**, per limb | `REG-006` §3 Q1 losing either clause reports *retire me*, not *violation* (`-42`). The Q1 block is located by its own anchor, so a renumbered §3 fails loudly |
| **the referent pin** | drops *in it* → **REFERENT LOST**, with the instruction to re-adjudicate scope in `§2` before touching the guard |
| **limb A** | own-voice scan: blockquotes, fenced code, inline code and double-quoted spans removed (`-33` — this file quotes ASC 350-20-35-32's *"tested for impairment"*), single newlines flattened (`-37` — §1 hard-wraps *"long-lived-asset\\nimpairment"*). Fires on a bare `impairment` sharing a sentence with a **ratio token**, which is Q1's own definition of the statistics it governs |
| **the two lawful bare sites** | pinned verbatim with their adjudication, **plus** an assertion that neither has since acquired a ratio — a pinned exception that quietly turns into a violation is the failure mode |
| **limb B** | table rows swept (a count must be in the row); the prose sites that carry their own count pinned one at a time. A line sweep over all prose returns **25** sites and would enforce a rule nobody wrote |
| **non-vacuity ×3** | `R2a`'s exact insertion, `R2c`'s exact row strip, `R2b`'s exact prose deletion — each asserting the **CONJUNCTION** (`-43`), each **skipping** rather than piling on if the real document is already violating (`-39`, the `test_reg012_sec7` precedent) |
| **over-breadth** | a test that feeds the registration a quoted ASC sentence *beside a ratio* and requires **no** hit |

**Grading, on the reds and not on the column (`-44`).** `R2a` → 1 catcher · `R2b` → 1 catcher ·
`R2c` (new) → 3 catchers, all in the new file. **C26 grades `FOR`.**

**`scripts/mutation_control.py`: +`R2c`.** `R2b` moves a *prose* site, which the guard binds by a
pinned literal; the **table-row** mechanism in the same file had no probe. `-47`'s rule, one session
old, applied to a guard one hour old: a limb with no probe is a claim.

**Inventory edits:** C26 `none` → **`FOR`** · §2a `FOR` 9→10, `none` 23→22 · §3's cross-table
12/31 → **13/30** · cell (b) 31 → **30** · §3.2 item 2 struck through **with its wrong description
left in place and corrected underneath**, because *"a pure regex constraint"* is the instructive
part · **new §2d** carries the finding and the limb-B bound.

**BUG SPRAY / the honest correction, on myself:** my own hand-audit of limb B found *ten* uncounted
ratio sites by reading the two tables I had already opened. The machine found **25** under a line
sweep. `-41`'s tell — *a hand-audit that found N sites found them through one door* — turned on the
session that was quoting it. The scoping decision that followed (rows swept, prose pinned) is in the
guard's docstring **and** in §2d, with the residual named.

| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** — the manuscript was not touched this session |
| **G-COACH-1** | held — the tee-up's wrong count was corrected in `CONSTRAINT-INVENTORY-001` §2d and §3.2 in-session, not filed |
| **G-COACH-5** | held — the strength named is **`-45`'s restored two words**. Restoring *in it* looked like a citation repair and was in fact the choice of this guard's algorithm, made two sessions before anybody needed it. **A provenance audit pays out as a design decision.** Cost to read it: one `grep` |
| suite | **1018 collected** · darwin **1018 passed** (~65 s) · cloud **1018 passed, zero skips** (~235 s) |
| new tests | 1 file, 11 tests · 1 new probe (`R2c`, 41 → 42) |
| lessons | **four** banked global · **three** used and corroborated `record-outcome wealthTensor-48 pass` — all three promoted quarantine → active |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |

---

## 2 · RULINGS — DO NOT REOPEN
- All of `-31`'s through `-47`'s rulings stand **verbatim**: no third disclosure instrument; phrase
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
  `9b3b013` IS NOT A VIOLATION**; **§3.2's SEVEN POSITIONS ARE MEASURED AND THE RANKING STANDS**.
- **NEW · C26's SCOPE IS `REG-006` AND `RESULT-REG-006`, AND THE DISCRIMINATOR IS *IS THIS A
  STATISTIC*, NOT *IS THIS QUALIFIED*.** `-45` ruled the referent and this session built on it.
  Widening limb A to every occurrence makes the guard red on a compliant witness at two sites that
  were adjudicated lawful. **If you think the guard is under-broad, read §2d before you touch it.**
- **NEW · THE TWO BARE `impairment` SITES ARE LAWFUL AND PINNED. DO NOT "REPAIR" THEM.** KPMG's
  Example 4.4.10 walk-through, and the 8-K Item 2.06 population sentence in both documents.
  Qualifying the second one would make it **factually wrong**.
- **NEW · LIMB B IS BOUNDED, NOT CLEAN, AND THAT IS DELIBERATE.** §2's six-row internal-control
  table prints twelve ratios and no counts. The counts exist in the ladder C run log; printing them
  edits a witness. **Carded (`1217525563299334`, State Machine), not repaired.** The pin fails in
  BOTH directions — a seventh uncounted row, or a pinned row that acquires a count.

---

## 3 · THE AT-BAT for `-49` — **build item 3, the C44 / C46 / C41 supersession family.**
Items 1 and 2 are built and struck through. Item 3 is the top of the measured list, and it is the
**best-warranted position left**: `-46` made its *deletion* limb red incidentally and explicitly
recorded the *supersession* limb as unmeasured; `-47` measured it with `R3a`/`R3b`/`R3c` and all
three came back green. **A limb that was named open and then measured open is the strongest ticket
in the file.**

The shape, from `§3.2` item 3 — **one guard, three constraints**:
1. **Assert both documents exist.** C44's *"beside, never instead of"* is a presence pair (C49's
   shape, `-44`): the later artifact may not stand alone. An absence guard cannot express *X, not
   merely Y*, and this is that constraint's whole content.
2. **Assert the later document carries no supersession claim** — `RESULT-REG-009-band-count-filled`
   must not say it replaces, withdraws or supersedes `-31`'s count (`R3a`'s exact insertion), and
   `RESULT-REG-010` must not promote the mirror to the registered reading (`R3b`), and must not
   re-score P3 (`R3c`).
3. **Scan assertions, not quotations** (`-33`) and **flatten the wraps** (`-37`) — the helpers in
   `test_reg006_sec3_q1_two_limbs.py` are written to be read and copied, not imported; `-44`'s
   lesson about a shared helper surviving its own deletion applies.
4. **Then re-run `R3a`/`R3b`/`R3c` and grade the row on the reds** (`-44`). Three reds whose only
   catchers are the new file is a `FOR`; a red whose catcher is somebody else's test is incidental
   and moves nothing.

**And do the twenty minutes first, on whatever this handoff asserts about those three documents.**
`-48`'s finding is that this file's *characterisations* are the unchecked surface, not its rankings.
The sentence above that says *"`-46` explicitly recorded the supersession limb as unmeasured"* is a
claim about `§3.1` — **go read `§3.1`.**

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The obvious alternative is **C37's tripwire**
(`REG-009` §12's *"never by narration"*, `§3.3`, about an hour); it is second because a fifth
tripwire proves less than a guard on a measured gap. The other is **§2.2's four uncounted prose
couplings** (§4 item 2 below) — smaller, and it needs a ruling before it needs a machine.

---

## 4 · TEED UP, IN ORDER
1. **T2 is CARDED (`1217501628088122`) and MAY NOT BE RUN ON THIS DATA.**
2. **NEW · C26 limb B — carded `1217525563299334`, State Machine.** §2's internal-control table:
   twelve ratios, no counts, counts available in `RESULT-REG-006-ladderC-run.log`'s `obs` column.
   Three options are written on the card. **And the named residual: §2.2's four discovered couplings
   (0.00×, 3.27×, 7.70×, 6.33×) are prose ratios with p-values and no counts, adjudicated by
   nobody.** Whoever rules on the table should rule on those in the same pass.
3. **`RESULT-REG-003` §2's "Every cut lands in R1" — carded `1217518687033967`, State Machine.**
   Two readings; under one, 0.327 < 0.33 is R2 by the registration's own ladder. **A `RESULT-*` is
   the record of a run and editing the artefact edits the witness** — the `-37` precedent says the
   repair shape is a dated addendum. C12's guard is unaffected either way.
4. **Cell (b), ranked in `CONSTRAINT-INVENTORY-001` §3.2 — FIVE entries after C26, still MEASURED
   (§2c).** The C44/C46/C41 supersession family (§3 above) · C10 · the five-constraint
   forbidden-claim family · C45's two assertions · the reportable-at-all presence guards.
5. **C37's tripwire** — `REG-009` §12's *"never by narration"*. §3.3 names the adjacent check.
6. **§7's ledger dilutes its own two load-bearing rows — Jason's call, and it is TRIPWIRED, not
   carded.** `test_tripwire_c36_sec7_ledger_shape.py` will ask him the moment the shape moves. **Do
   not card it and do not ask him pre-emptively.**
7. **`-47`'s residual, still open:** the other eight git-aware tests have never had a mutation run
   against them. `-47` fixed the harness and spent its one git probe on C07; `-48` spent its probe
   budget on C26. **Somebody should sweep the rest of that axis** — a probe per invariant, on an
   axis the estate has only just learned it could not see.
8. Infra siblings, carded, Claude-hands: Caddy ordering `1217488447555628` · capability path in
   cleartext + repo drift `1217488117177482`.
9. AAR A2's residual — the other four `post-*` hooks · card-lint `1217483699706758` · gate
   `1217465036940491`.
10. Dossier era, re-served by nobody: `REVIEW-004` **C6** (ASC 410) and **C10** (IAS 36's reversal
    asymmetry, a free cross-regime falsification test).
11. Phrase-set passenger: 30.4 % match only `events or circumstances`; 7.9 % safe-harbour. Outranked.
12. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
13. Not mine, not touched: handoff-lint warns on `HANDOFF-acmeLedger-07.md:22`, `-09.md:36,42`, and
    `-12.md` / `-13.md` carry items with ZERO `verify:` lines. **Leave them alone** — `-16` is
    `opus-acmeLedger-17`'s live document and `-20` was on the roster this session.

---

## 5 · DO NOT
* Everything `-31`→`-47` forbade still stands verbatim — R5, the two sensitivities,
  `selected_lives`, §4.4's `0.3000`, T4's `31.7%`, the δ arm, TERM-001/002, the dossier era, §9's
  FOUR list items, `wt107` IS NOT EDITED, cite the test not the backup, **"THE REGISTERED ADVERSE
  CUT" DOES NOT RETURN**, **§4.7 IS PINNED AT `ba59370`**, **DO NOT "SIMPLIFY" A TRIPWIRE INTO A
  GUARD**, **DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION**, **DO NOT GRADE A
  CONSTRAINT FROM THE `machine` COLUMN, INCLUDING WHEN YOU ARE ONLY RANKING**, **DO NOT RUN A
  COMMIT-ORDER PROBE WITHOUT `{"git": True}`**, **DO NOT WIDEN C07's GUARD TO EVERY REGISTRATION**,
  **DO NOT SOFTEN A DOCTRINE SENTENCE THAT TURNS OUT TO BE FALSE — MAKE IT TRUE, THEN GIVE IT A
  MACHINE**, **DO NOT PIN THE 98 AS A STRING**. §2.
* **NEW · DO NOT WIDEN C26 LIMB A TO EVERY OCCURRENCE OF THE WORD.** Two sites are lawful, pinned
  and adjudicated, and the widened guard is red on a witness that was never wrong. §2d.
* **NEW · DO NOT PRINT COUNTS INTO §2's INTERNAL-CONTROL TABLE WITHOUT UPDATING `UNCOUNTED_ROWS`
  AND §2d IN THE SAME COMMIT.** The pin fails in both directions on purpose; that is the feature.
* **NEW · DO NOT TRUST A HANDOFF'S DESCRIPTION OF A DOCUMENT'S CONTENTS — INCLUDING THIS ONE'S.**
  Every count in §1 above was measured this session on both machines. Every count in §3 and §4 is a
  claim about a file you have not opened yet. **Open it.**
* Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud.

---

## 6 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.

Coffee status: ☕ **FOURTEEN SESSIONS RUNNING, AND THE FIRST TWENTY MINUTES DECIDED THE WHOLE SESSION
AGAIN** — `-35` truth, `-36` population, `-37` count, `-38` premise-and-instrument, `-39` severity,
`-40` the promise the document made about itself, `-41` the resolution it was written at, `-42`
whether it was in force, `-43` who the promise was made about, `-44` whether the thing guarding it
can see it, `-45` whether the address on it was right, `-46` whether the sentence that sent you here
was ever checked, `-47` whether the instrument that checks it can see the whole board, **`-48`
WHETHER THE SENTENCE THAT SENT YOU HERE HAD EVER OPENED THE DOCUMENT.** `-47`'s came from reading a
docstring that admitted its own blind spot. `-48`'s came from counting a word — four tool calls,
against a claim three handoffs had copied forward without once running `grep -c`. **The cheapest
check in the estate is the one nobody runs, because the sentence stating the fact reads like the
fact. Count it yourself.**
