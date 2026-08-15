---
project: wealth-tensor
gh_sha: acaa4064cd5be233fdcdfef697df5176858e7c56
updated: 2026-08-15
session: wealthTensor-47
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
   ESTATE). **Read §2c first this time** — it is `-47`'s measurement of §3.2's entire ranking, and
   the paragraph about the harness is the one that matters. Then §3.2, then §2b, then §2a's counts.
3. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
4. **`python3 scripts/mutation_control.py --list`** — 41 probes now. **Read its module docstring
   before you grade anything**, including the `-47` section on why `.git` is opt-in.
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
> **`-47` in one line: THE INSTRUMENT BUILT TO STOP FALSE GREENS WAS ITSELF PRODUCING ONE, AND IT
> WAS FOUND IN THE FIRST TWENTY MINUTES BY ASKING WHAT THE HARNESS COULD NOT SEE.**
> `-46` shipped `mutation_control.py` with `.git` excluded from every scratch copy — correct for
> RUNNING the suite, fatal for MEASURING it. Nine tests in this estate skip with *"not a git work
> tree"*, and one of them is the only machine anywhere near **C07, §3.2's item 1**. The C07 probe
> would have come back green while proving nothing: the harness deletes the candidate guard, then
> reports its absence as the measurement. Fixed first, then the sweep: **nineteen probes across all
> seven ranked positions, EIGHTEEN GREEN, and the one red is incidental.** The measurement moved
> **zero** positions — which is the finding, because the column it was derived from was right at
> seven of eight positions and wrong by eleven at the eighth, and nothing in the column tells you
> which you are holding. **The seven confirmations are what hid `-46`'s counterexample for two
> sessions.** C07 is built and graded on its probe. Four sessions running, this estate's prose
> about ITSELF has been the thing that did not survive checking: `-44` the `machine` column, `-45`
> the `source` column, `-46` the ranking prose, `-47` the harness AND the DO-NOT list.
---
### Transport — darlish, zero-bridge
Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
**First try, no fallback, `-06` through `-47`.** If it does not come up the first move is `dsh-fire`
+ `dwait`, not diagnosis. darlish is not on the bridge; never restart the app to fix it.
`darlish-check` is **not** in the cloud kit — do not chase its 127.
`roster leave` ONCE at wrap.
> ### ⚠ SET `GATE_ROSTER_WHO` INLINE. THE `export` FORM IS RETIRED AND NEVER WORKED.
> dx spawns a **fresh remote shell per call and carries no environment**. Inline on `roster join`,
> `roster claim`, the commit, and every `lessons.py` call — first time, every time.
> **Exception: `export GATE_ROSTER_WHO=…` DOES work inside a script you `--put` and run with
> `bash /tmp/x.sh`**, because that is one shell. `-47` ran all its `lessons.py` calls that way.
> ### ⚠ `roster claim` TAKES `--resource`, NOT `--repo`. `record-outcome` TAKES NO `--id`.
> `roster claim --who <who> --resource <repo> --task "<what>"`; `roster join` takes `--who/--task`.
> **`lessons.py record-outcome <task-tag> pass` is TWO positional args and nothing else** — `-47`
> lost four calls to `--id`, which prints a bare usage block and exits 2. One call resolves every
> leaf you marked with `use --task <tag>`.
> ### ⚠ `git commit -F <msg> <paths>` CANNOT STAGE AN UNTRACKED FILE.
> Look, add, then commit — the whole move on a shared repo:
>
> ```
> /tmp/dx 'cd ~/repos/<repo> && git status --porcelain'                 # look FIRST
> /tmp/dx 'cd ~/repos/<repo> && git add <only your new paths>'          # never -A, never .
> /tmp/dx 'cd ~/repos/<repo> && GATE_ROSTER_WHO=big-<sess> ROSTER_BRAKE_ACK=<n> \
>            git commit -F /tmp/msg.txt <all your paths, new AND modified>'
> ```
> **`<n>` is the count of YOUR paths, not the staged total.** `-47`'s was 5.
**COMMIT BY PATH ON `claude-blackbook`, ALWAYS.** `git status --porcelain` first; if a sibling's
leaves are staged, commit by path.

> ## ⚠⚠ THE TWO-TARBALL MINUTE-TWO STANZA IS RETIRED. IT COST NINE TESTS AND HID AN AXIS.
> `-46`'s stanza tarred `docs scripts tests src` + `data` and omitted `.git`, `conftest.py`,
> `requirements.txt`, `README.md`, `LICENSE`, `.gitignore`. That is why every session since has
> reported the cloud running **990 passed / 9 skipped** and called the skips normal. They are not
> normal: they are the entire git axis of the estate, and nobody had probed it. **One tarball, and
> the cloud runs the full suite.**
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
> `-47` measured **19,763,527 bytes**, `verified against darwin` in words. `.venv` is **650 MB** —
> exclude it or the tarball is 169 MB. The two `chown`/`find` lines are not optional: macOS tar
> writes `._*` AppleDouble files that show as untracked, and darwin's uid makes git refuse the tree
> with *"dubious ownership"*.
> **`$HOME` in the cloud container is `/root`** — unpack to `/root/wtg` and give Read the absolute
> path. **Never inline a multi-line string in `dx '...'`** — write locally, `--put`, run it.
> `--get` with a leading `~` expands in the CLOUD shell and fails; use `/Users/jasoncbraatz/...`.
> Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.
> **Exit 3** = never reached darwin, safe to re-run · **4** = dropped after the command started,
> check state first · **5** = crossed but mismatched, nothing written, replay-safe.

**SUITE COUNTS — COLLECTED = PASSED + SKIPPED, AND THE SKIPS ARE GONE.**
| | at `HEAD` = `acaa406` (verified in `-47`, both machines, same hour) |
|---|---|
| collected | **1007** (was 999 at `87234f7`; `-47` added 8) |
| cloud, FULL tarball (`PYTHONPATH=/root/wtg/src`) | **1007 passed**, ~112 s, **zero skips** |
| cloud, `-46`'s two-tarball stanza | 998 passed / 9 skipped — **do not use it, and do not report the skips as normal** |
| darwin (`.venv/bin/python -m pytest`) | **1007 passed**, ~62 s |
`scripts/defensive_count.py` **takes a positional `path`** and errors without one.
`pytest -m tripwire` selects the four-file tripwire class; `-m "not tripwire"` excludes it.
A cloud container is **2 CPUs** — the sweep is `--jobs 2`, ~2 min per probe. `-47`'s nineteen
probes were ~35 minutes of wall clock and they were the session. Budget for it.
---
## 0 · THE TELL, NOW IN FORTY-FIVE SHAPES
Ask the instrument-artefact question of numbers that look GOOD (`-28`), that SETTLE AN ARGUMENT
(`-29`), of a REGISTERED CONTROL THAT FAILS (`-30`), OF THE DENOMINATOR (`-31`), OF A TIE-BREAK AT A
NEW CARDINALITY and OF A TELL GONE QUIET (`-32`). `-33`: instruments that agree with themselves; a
guard must scan assertions, not quotations. `-34`: defects nobody introduced. `-35`: defects you are
about to introduce; **a doctrine sentence written in docs/ twice and enforced nowhere is still an
unguarded invariant**. `-36`: pre-commit the FAVOURABLE outcome's meaning. `-37`: a mutation that
does not mutate reports your guard as weak. `-38`: a statistic can be a tautology in measurement's
clothing. `-39`: a handoff silently outranks a doctrine leaf; **assert the EXACT exit code**.
`-40`: a STALE NEGATIVE closes a question harder than an open one. `-41`: a hand-audit that found N
sites found them through ONE DOOR; a paragraph-resolution grade against a sentence rule is a FALSE
GREEN. `-42`: a constraint can be CONDITIONAL and its guard must assert its ANTECEDENT; a
whitespace-identity guard certifies no character moved, not no meaning; the second door is the
SECTION HEADING; evidence in a file outside the SSOT is not in the SSOT. `-43`: a labelling
constraint's second door is the WRONG label; **feed the registration its own forbidden claim before
you trust the green**; a non-vacuity test must assert the CONJUNCTION. `-44`: a column that names a
guard is a COVERAGE CLAIM and nobody ever verifies it; **the reproduced numbers bind, the
prohibitions escape**; an ABSENCE guard cannot enforce *X, not merely Y*; **do not fuse a property
of the artefact with a property of the estate into one partition.** `-45`: a `source` cell is a
PROVENANCE claim and an address that resolves is not an address that is right; a quotation is a
lossy copy and the first things it loses are the ANTECEDENT and the REFERENT. `-46`: a coverage
count read off the `machine` column is a claim about the COLUMN; **a reproducibility pin is not a
freeze**; the number with no artifact is the one that escapes. **`-47` adds three:**
- **A MUTATION THE HARNESS CANNOT SEE REPORTS EVERY GUARD IN THE UNSEEN PART OF THE ESTATE AS
  ABSENT, AND ITS GREEN IS INDISTINGUISHABLE FROM *NO GUARD EXISTS*.** `-46`'s control excluded
  `.git`; nine tests skip without a work tree; C07's probe was about to be graded on that green.
  **Before trusting a green probe, ask which tests the harness prevented from running at all — a
  skip is not a pass and it is not a red.** Banked:
  `2026-08-15-mutation-harness-cannot-see-part-repository`.
- **A METHOD THAT IS WRONG AND MOSTLY RIGHT IS THE MOST DANGEROUS KIND, BECAUSE ITS CONFIRMATIONS
  ARE WHAT HIDE ITS COUNTEREXAMPLE.** Reading coverage off the `machine` column was right at seven
  of eight measured positions and wrong **by eleven** at the eighth. Auditing a proxy and finding it
  *mostly* agrees is not licence to keep using it — it is evidence its failures are silent.
  Banked: `2026-08-15-method-wrong-mostly-right-dangerous-kind`.
- **"UNTRACKED" AND "GITIGNORED" ARE DIFFERENT FACTS WITH DIFFERENT FAILURE MODES.** This file said
  the `.bak` copies were gitignored; `.gitignore` had no `.bak` pattern and twelve showed as
  untracked — one `git add -A` from the SSOT, defended only by a *second* prose rule forbidding
  `git add -A`. **Make the sentence true, do not soften it**, then give it a machine. Banked:
  `2026-08-15-untracked-gitignored-different-facts-different-failure`.
**Everything `-33` through `-46` banked is unchanged and still sharp.** `severity.check`'s witness
must return FALSY. Check `git ls-files <name>` before a whole-file write into a shared directory.
`patchkit` anchors have **no internal newline**.
---
## 1 · WHAT HAPPENED
**The harness fix came before the sweep, and it is why the sweep is worth anything.** Then nineteen
forbidden moves, one per ranked position and one per limb, each on its own scratch copy of the repo
with the whole suite behind it:
| §3.2 position | probes | caught |
|---|---|---|
| 1 · C07 amended-after-result | `R1` | **0/1** |
| 2 · C26 unqualified *impairment* · the count beside each ratio | `R2a` `R2b` | 0/2 |
| 3 · C44 / C46 / C41 — the **supersession** limb `-46` left unmeasured | `R3a` `R3b` `R3c` | 0/3 |
| 4 · C10 the re-ask labelled `E4` | `R4` | 0/1 |
| 5 · C16 / C20 / C23 / C25 / C30 forbidden claims | `R5a`–`R5e` | 0/5 |
| 6 · C45 `R_MIN` promoted · band rule re-chosen | `R6a` `R6b` | **1/2** |
| 7 · C01–C04, C06 reportable-at-all | `R7a`–`R7e` | 0/5 |
| **total** | **19** | **1** |
The one red, `R6a`, has a single catcher — `test_the_population_is_the_cited_tables_own`, asserting
`art["occupied_bins_reproduced"] == cited["profiles"][art["reading"]]["occupied"]`. A cross-artifact
**consistency** check, green on any re-run that moves both together (`-38`). Not about promotion.
**C45 stays ADJACENT.** Positions moved by the measurement: **zero**.
**Two new files, 8 tests, green on both machines.**
| file | what it is |
|---|---|
| `tests/test_reg001_sec5_no_amendment_after_result.py` (5) | C07. Ancestry not dates (dates lie under rebase) · scope asserted to be REG-001 alone, so a second registration adopting the sentence goes red saying **EXTEND ME** · `-42`'s antecedent: losing §5's sentence reports **LOST WARRANT**, not a violation · non-vacuity runs the real detector against a synthetic git history and asserts the **conjunction** (`-43`) — empty on the compliant leg, one hit after the amendment, same repo |
| `tests/test_backups_are_ignored.py` (3) | the BUG SPRAY. `git check-ignore` over every `*.bak*` found on disk, a non-vacuity leg asserting the set is non-empty, and a third asserting none is tracked — because a `.gitignore` pattern does nothing to a file already in the index |
| `scripts/mutation_control.py` | +19 probes, `{"git": True}` support, and the docstring section explaining why the harness was the first false green |
**Inventory edits:** C07 `ADJACENT` → **`FOR`** (graded on `R1`, green before and red after) · §2a
`FOR` 8→9, `ADJACENT` 8→7 · §3's cross-table 11/32 → **12/31** · §3.2 rewritten from the measurement
with per-position probe slugs, item 1 struck through, and the *what the seven greens do NOT license*
note · §3.1 records C45's red as incidental · **new §2c** carries the sweep and the harness finding.
**BUG SPRAY, found and fixed in-session:** the `.bak` claim (above), and this file's own body said
gate **v2.50** while its frontmatter and the gate itself say **v2.51** — corrected here.
| | |
|---|---|
| **G-COACH-3** | **3 → 3 (+0)** — the manuscript was not touched this session |
| **G-COACH-1** | held — the stale `.bak` sentence and the stale gate version were repaired in-session, not filed |
| **G-COACH-5** | held — the strength named is **`test_registrations_precede_their_instruments.py`'s docstring**, which states in plain words the one thing it cannot do: *"it cannot see a registration edited after its result existed."* That sentence is C07, written by the file that was cited as C07's machine. **A guard that documents its own blind spot hands the next session its at-bat** — this one was a two-year-old note waiting to be read, and reading it cost nothing. |
| suite | **1007 collected** · darwin **1007 passed** (~62 s) · cloud **1007 passed, zero skips** (~112 s) |
| new tests | 2 files, 8 tests |
| lessons | **three** banked global · **four** used and corroborated `record-outcome wealthTensor-47 pass` — two promoted quarantine → active |
| stopping rules | **honoured — no lag gradient computed on any subsample; the research ledger on paper III is still empty** |
---
## 2 · RULINGS — DO NOT REOPEN
- All of `-31`'s through `-46`'s rulings stand **verbatim**: no third disclosure instrument; phrase
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
  AND STAY FOUR**; **`wt107` IS NOT EDITED**; **THE `.bak` COPIES ARE NOW GENUINELY GITIGNORED — CITE
  THE TEST, NOT THE BACKUP**; **`RESULT-REG-003` §2's "EVERY CUT LANDS IN R1" IS TEED UP, NOT
  REPAIRED** (carded `1217518687033967`); **THE `machine` COLUMN IS NOT A COVERAGE COLUMN**; **DO NOT
  RE-GRADE A `machine` CELL WITHOUT DOING THE AUDIT — THE EVIDENCE FOR A BINDS IS A MUTATION THAT
  GOES RED**; **C49's GUARD IS A PAIR**; **DO NOT DELETE THE REFUSAL SENTENCES FROM
  `RESULT-REG-012-band-edge-phase.md`**; **C09's WARRANT IS `REG-002` E2, NEVER E1**; **`TRIPWIRE` IS
  A GRADE AND IT IS NOT COVERAGE**; **A TRIPWIRE'S RED MESSAGE IS PART OF THE ARTEFACT**; **THE THREE
  TRIPWIRE PINS MOVE IN THE SAME COMMIT AS THE EDIT THAT MOVED THEM**; **C42's FIFTEEN ARE FROZEN AS
  LITERALS AND THE LITERALS STAY**; **THE PARSE OF REG-010 §4 IS READING (A)**; **AN INCIDENTAL RED
  IS NOT COVERAGE**; **DO NOT PIN THE 98 AS A STRING**.
- **NEW · `.git` IS OPT-IN IN `mutation_control.py` AND A COMMIT-ORDER PROBE MUST SET IT.** A probe
  for a constraint about history without `{"git": True}` is measuring nothing, and its green is a
  statement about the harness. The nine git-aware tests are the affected set.
- **NEW · C07'S GUARD IS SCOPED TO REG-001 ON PURPOSE, AND `9b3b013` IS NOT A VIOLATION.** That
  commit amended `PRE-002` and `REG-008` after both results existed — dated addenda disclosing
  violations that had lived only in `tests/`. Neither registration ever promised not to be amended.
  A guard that flagged them would enforce a rule nobody wrote and would be deleted the first time it
  fired. If a second registration adopts §5's sentence, the guard goes red saying **EXTEND ME**.
- **NEW · §3.2's SEVEN POSITIONS ARE MEASURED AND THE RANKING STANDS.** Do not re-derive the
  measurement to build the next guard; do re-run the probe for the position you are building
  (`--only <slug>`, two minutes). **But do not read the `machine` column again for a position that
  has no probe** — being right seven times is what made the eighth invisible.
---
## 3 · THE AT-BAT for `-48` — **build C26, the top of the MEASURED list.**
Item 1 is built and struck through; **item 2 is now the top, and unlike `-46`'s and `-47`'s at-bats
its warrant is a measurement rather than a sentence.** `R2a` and `R2b` are both green.
The shape:
1. **`REG-006` §3 Q1 states two limbs in one sentence** — *"the word 'impairment' never appears in
   it unqualified, and the count of firm-periods behind each ratio is printed next to the ratio."*
   Two limbs, two probes, two assertions — the `-43` two-limb shape, and they fail for different
   reasons so they get different messages (`-42`).
2. **The unqualified limb is a regex over `RESULT-REG-006.md` and it is the harder one.** The
   document already carries *"impairment"* eleven times, every one of them qualified — *goodwill
   impairment*, *tested for impairment*. The guard must scan **assertions, not quotations**
   (`-33`): the file quotes ASC 350-20-35-32 and PwC's Example 4.4.10, and a naive regex will call
   the standard's own words a violation. Blockquote-exclusion is already implemented in
   `test_reg012_sec7_refusal_is_asserted.py` — read it before writing a second one.
3. **Feed the registration its own forbidden claim before you trust the green** (`-43`), and assert
   the **conjunction** — the guard must go red on the violating document AND green on the real one,
   in the same test, or it passes for a scanner that flags everything.
4. **Then re-run `R2a` and `R2b` and grade the row on the reds**, per `-44`. Both should be red with
   the new file as the catcher; if either is red with somebody else's test as the only catcher, that
   is an incidental red and the grade does not move.
**Why this and not another guard.** Three sessions have now each built one guard from the top of
this list, and `-47` converted the rest of the list from assertion into measurement so that the next
three do not each have to re-derive their own warrant. **Spend that.** The remaining positions after
C26 are items 3–7 in §3.2, in order, each with its probe slug beside it.
**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The obvious alternative is **C37's tripwire** —
`REG-009` §12's *"never by narration"*, teed up in `CONSTRAINT-INVENTORY-001` §3.3, about an hour.
It is second because a fifth tripwire proves less than a guard on a measured gap.
---
## 4 · TEED UP, IN ORDER
1. **T2 is CARDED (`1217501628088122`) and MAY NOT BE RUN ON THIS DATA.**
2. **`RESULT-REG-003` §2's "Every cut lands in R1" — carded `1217518687033967`, State Machine.**
   Two readings; under one, 0.327 < 0.33 is R2 by the registration's own ladder. **A `RESULT-*` is
   the record of a run and editing the artefact edits the witness** — the `-37` precedent says the
   repair shape is a dated addendum. C12's guard is unaffected either way.
3. **Cell (b), ranked in `CONSTRAINT-INVENTORY-001` §3.2 — SIX entries after C07, and the ranking is
   now MEASURED (§2c).** C26 (§3 above) · the C44/C46/C41 supersession family, whose limb `-46` left
   open is measured and green · C10 · the five-constraint forbidden-claim family · C45's two
   assertions · the reportable-at-all presence guards.
4. **C37's tripwire** — `REG-009` §12's *"never by narration"*. §3.3 names the adjacent check.
5. **§7's ledger dilutes its own two load-bearing rows — Jason's call, and it is TRIPWIRED, not
   carded.** `test_tripwire_c36_sec7_ledger_shape.py` will ask him the moment the shape moves. **Do
   not card it and do not ask him pre-emptively.**
6. **NEW, small, teed up not fixed:** the other eight git-aware tests have never had a mutation run
   against them. `-47` fixed the harness and spent its one git probe on C07. **Somebody should sweep
   the rest of that axis** now that it is reachable — the shape is a probe per invariant, and the
   estate has just learned what an unprobed axis costs.
7. Infra siblings, carded, Claude-hands: Caddy ordering `1217488447555628` · capability path in
   cleartext + repo drift `1217488117177482`.
8. AAR A2's residual — the other four `post-*` hooks · card-lint `1217483699706758` · gate
   `1217465036940491`.
9. Dossier era, re-served by nobody: `REVIEW-004` **C6** (ASC 410) and **C10** (IAS 36's reversal
   asymmetry, a free cross-regime falsification test).
10. Phrase-set passenger: 30.4 % match only `events or circumstances`; 7.9 % safe-harbour. Outranked.
11. `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
12. Not mine, not touched: handoff-lint warns `HANDOFF-acmeLedger-07.md:22`, `-09.md:36,42`, and
    `-12.md` / `-13.md` carry items with ZERO `verify:` lines. **And G-V#3 fails on stale refs in
    `HANDOFF-acmeLedger-16.md`** — that is `opus-acmeLedger-17`'s live document. Leave it alone.
---
## 5 · DO NOT
* Everything `-31`→`-46` forbade still stands verbatim — R5, the two sensitivities,
  `selected_lives`, §4.4's `0.3000`, T4's `31.7%`, the δ arm, TERM-001/002, the dossier era, §9's
  FOUR list items, `wt107` IS NOT EDITED, cite the test not the backup, **"THE REGISTERED ADVERSE
  CUT" DOES NOT RETURN**, **§4.7 IS PINNED AT `ba59370`**, **DO NOT "SIMPLIFY" A TRIPWIRE INTO A
  GUARD**, **DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE QUOTATION**, **DO NOT GRADE A
  CONSTRAINT FROM THE `machine` COLUMN, INCLUDING WHEN YOU ARE ONLY RANKING**, **DO NOT DELETE
  `PSI_CELL` ET AL AND LEAVE THE DERIVED ANCHORS**, **DO NOT PIN THE 98 AS A STRING**. §2.
* **RETIRED, AND SAY SO IF YOU SEE IT REPEATED: "DO NOT ASSUME THE CLOUD TARBALL IS THE REPO."**
  The rule was right and the fix is better — **the cloud tarball IS the repo now.** One full
  tarball, `git status` empty, 1007/1007, zero skips. If a session reports 990/9 it used the retired
  stanza and its measurements of the git axis are worthless.
* **NEW · DO NOT RUN A COMMIT-ORDER PROBE WITHOUT `{"git": True}`**, and do not read any green probe
  without first asking what the harness skipped.
* **NEW · DO NOT "FIX" C07's GUARD BY WIDENING IT TO EVERY REGISTRATION.** Two registrations carry
  dated addenda made after their results, lawfully. The EXTEND ME assertion is the intended path.
* **NEW · DO NOT SOFTEN A DOCTRINE SENTENCE THAT TURNS OUT TO BE FALSE.** Make it true, then give it
  a machine. The `.bak` line is the worked example.
* Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud.
---
## 6 · ORIENT-THEN-GO
Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.
Coffee status: ☕ **THIRTEEN SESSIONS RUNNING, AND THE FIRST TWENTY MINUTES DECIDED THE WHOLE SESSION
AGAIN** — `-35` truth, `-36` population, `-37` count, `-38` premise-and-instrument, `-39` severity,
`-40` the promise the document made about itself, `-41` the resolution it was written at, `-42`
whether it was in force, `-43` who the promise was made about, `-44` whether the thing guarding it
can see it, `-45` whether the address on it was right, `-46` whether the sentence that sent you here
was ever checked, **`-47` WHETHER THE INSTRUMENT THAT CHECKS IT CAN SEE THE WHOLE BOARD.** `-46`'s
came from running the control first and reading the answer instead of the instruction. `-47`'s came
from reading the docstring of the file the inventory had cited for four sessions, which said in
plain words that it could not see the thing it was cited for. **The tee-up is not evidence, and
neither is the instrument. Spend the twenty minutes on whichever one nobody has pointed at itself.**
