---
project: wealth-tensor
gh_sha: 2a52f14814e386f36e1751cbba5a8741c3e8af1c
updated: 2026-08-16
session: wealthTensor-52
gate_passed: true
gate_version: "2.59"
definition_of_done: "Three preprints (II, III, IV) publicly posted — the corpus-level Definition of Done in ADR-001 as amended (was four; Paper I folded into IV). Per-paper clauses in ADR-001 govern each paper's 'ready to submit' terminal state, and nothing ships until the corpus is done."
---

# wealth-tensor — HANDOFF

`gh_sha` names the commit this file describes; **the only thing added after it is this file**,
so `--check` prints `ADVISORY: docs-only drift` and exits 0. Assert the exit code exactly
(`-39`); `| tail` masks it. That sentence is an **INVARIANT, not a description** — `-51` learned
that the hard way when a post-wrap ADR commit made it false while the gate stayed green, because
`--check` classifies by PATH and any docs-only drift is green. If a post-wrap commit lands,
repoint `gh_sha` and re-master this file.

`-52` landed everything in `2a52f14` and wrote this file alone after it. `gh_sha` is the full
SHA from `git rev-parse`, not an expanded abbreviation (`-51`'s near-miss, still a DO-NOT below).

---

## ORIENT — read these first, in this order

1. **`docs/CHECKLIST.md`** — **START HERE NOW, and this is new.** The board is GENERATED
   (Tier 2): criteria in `docs/done-criteria.tsv`, status measured by
   `~/Scripts/handoff-kit/board.py`. **Never hand-tick it.** It prints distance-to-done and names
   the next piece. As of `-52`: **14 of 23 lines met**, up from 1 of 10 — P1 closed and its
   twelve measurement sub-rows (P1a–P1l) are green with a real command each.
2. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS** over this file, any
   result doc, and any plausible rewrite. §2's repair ladder (STEELMAN / REPLACE / CUT / TEE UP,
   and ABSORB is illegal) and §3.4 ("order the abstract by contribution, not contrition") are the
   two clauses `-52` actually used; read them before you touch prose.
3. **`docs/adr/ADR-001-paper-decomposition.md`** — the sequencing decision. **II → III → IV**,
   submission is a **batch** (`-08`), per-paper Definition of Done clauses, monograph only after
   IV. Read the header note first: the title and §Decision are **deliberately frozen** as the
   decision-as-made; the addenda amend it. Do not "fix" those two. `-52` struck the three places
   that still asserted four papers as live law.
4. **`docs/papers/PREPRINT-CHECKLIST.md`** §A/§B/§D — the per-paper apparatus bar. §A's items are
   now MEASURED for Paper III as rows P1a–P1m; read the rows, not the prose worry.
5. `python3 scripts/handoff_gate.py --check` · `python3 scripts/mutation_control.py --list`
   (61 probes) · `docs/preregistration/CONSTRAINT-INVENTORY-001.md` §2g then §2f, §2e, §2d, §2c
   — **the constraint-inventory thread is PAUSED**, see §3. Read it if you take a guard, not
   before.
6. REG-003 §§3.2/3.3/7 · SCOUT-001 (WORKED, not pending) · REG-012 §§6–7 · RESULT-TERM-001's
   five-site ruling · REG-010 §1/§4 · CONSTRUCTION-REG-009 (R5 unspent) · REG-009 (READ THE
   HEADER NOTE FIRST).

---

## `-52` in one line

**THE PAPER'S ABSTRACT WAS 2.85× THE VENUE'S HARD CEILING AND EIGHT SESSIONS OF AUDIT NEVER
LOOKED AT IT.**

`-42` through `-51` produced eight consecutive findings, every one about the audit apparatus —
a column, a docstring, a harness's regex, a ranking's prose, an ADR's stale heading. `-52` was
the first session in ten told to open `paper-III.md` with intent to change it. Twenty minutes in,
measuring §A item by item: **the abstract was 872 words / 5,480 characters** against
PREPRINT-CHECKLIST §A's 150–250 words and **arXiv's hard 1,920-character metadata limit**
(*"abstracts longer than 1920 characters will not be accepted"* —
`info.arxiv.org/help/prep.html`, re-verified 2026-08-16, because venue rules are exactly the
fact that rots). It is a **submission blocker**, not a style note: the form rejects it. Paper II's
is 261 w / 1,646 c and was never the problem.

Eleven of the twelve checkable §A items were **already satisfied** — the "missing apparatus"
ADR-001 §Consequences worries about (*"All are absent today"*) has been stale for weeks, and
nobody had measured it. One item was not, and no checklist line had ever been pointed at LENGTH.

---

## 1 · WHAT HAPPENED

**The at-bat was P1, and P1 is now CLOSED.** The measurement lives as rows `P1a`–`P1m` in
`docs/done-criteria.tsv`, twelve with a runnable check and one (`P1m`, the submission-time head
SHA) `manual:` and deferred by design. That is the deliverable: the next session ticks a line, it
does not re-read a paragraph.

| | |
|---|---|
| **the gap** | abstract cut 872 w / 5,480 c → **247 w / 1,564 c**, ordered by contribution (charter §3.4), all ten headline figures kept |
| **the cut was proved safe first** | every fact it removed was verified present in the body — 43.9% is there as `43.9%`, which is what the abstract was rounding to "44%"; the 2–4× clustering is there as `4.12×` and `2.02×` |
| **the counter is part of the finding** | `wc -w` said 248, `awk NF` said 266, **same bytes** — GNU vs BSD on em dashes, middots and Greek letters. 7% apart, straddling a 250 bar. `scripts/check_abstract_size.py` counts the DECODED string; both machines now agree at 247 |
| **the suite caught it** | `test_restatement_reach.py` fired on all three figures the abstract lost and was **the only thing in the suite that noticed the abstract had changed at all**. Declarations updated with the reason |

**BUG SPRAY, four, and two were not in this repo.**

1. **A DO-NOT THAT WAS FALSE ON THE DAY IT WAS WRITTEN, INHERITED TEN TIMES.** *"§9's LIMITATIONS
   ARE FOUR LIST ITEMS AND STAY FOUR"* entered at `-42` and rode every handoff since. §9 had
   **nine** items at `e947fb6` — the very commit whose handoff introduced the rule — and has nine
   now. The "four" was lifted from the incident narrative in
   `test_manuscript_lists_are_well_formed.py`, which **asserts no count at all**; it asserts that
   a list marker may not sit mid-line. The live risk was to the manuscript: a session obeying it
   and finding nine would delete five real limitations, from the section whose whole purpose is
   admitting them. Corrected in that file's docstring, where the misreading happened.
2. **TWO INHERITED REDS HIDING THREE VACUOUS GREENS.** `tests/test_handoff_stamp.py` was **red at
   HEAD before `-52` touched anything** — `definition_of_done` joined `handoff_gate.REQUIRED` and
   the hand-written `GOOD` fixture was not updated. The two reds were the cheap half: three more
   tests assert `rc == 1` for named gh_sha conditions and were getting their `rc == 1` from the
   missing key instead. The fixture is now built **from `G.REQUIRED`** and asserts the set is
   covered.
3. **ADR-001 STILL ASSERTED FOUR PAPERS IN THREE MORE PLACES.** `-51` corrected §Order of
   publication; the `-08` batch ruling still read *"before all four reach it"*, its open
   end-to-end question still read *"the four papers"*, and the monograph entry still read *"after
   I–IV ship, compile the four preprints"*. Struck in place, old text kept.
4. **THE GATE ITSELF, TWICE** (`darwin-mac-ops` `95f9b9e`, taken from a >4h STALE claim by
   `cloud-oaujFobu` — advisory, not a lock, and said out loud here per the roster's instruction).
   `G-AL` asked *"did THIS session read its charter"* and answered from
   `~/.local/state/claude-session/current` — **one global file on a machine running 2–3 sessions**
   — so it failed a wealth-tensor session for a sibling's acmeLedger stamp, and the remedy it
   offered would have stamped the sibling's charter as freshly read by a session that never
   opened it. `G-AL#board` looked for `dirname(criteria)/tools/gen-done.py` — braatzio-plan's
   layout — and called its absence a hand-maintained board, which would have failed **every**
   project on the shared engine, i.e. everyone else by construction.

| | |
|---|---|
| suite | **1055 passed** on darwin (~64 s), zero skips · unchanged count, three test files edited |
| board | **1/10 → 14/23** · P1 CLOSED, P1a–P1l green, P1m human-deferred |
| defensive sentences | **3 → 3** (charter §2's non-increasing invariant held) |
| lessons | **7 banked** (6 global, 1 project) · no twins · all auto-pushed |
| gate | **PASS ✅ at 2.59** (the frontmatter said 2.58; trust `gate-selfcheck.sh`'s printed line) |

**NOT DONE, and say so: no `lessons.py use` / `record-outcome` this session.** `-52` worked from
this handoff, not from the shelf — it never ran a `lessons.py search` at student-in, so it has no
leaf it honestly used and **stamping one would be `-51`'s exact error in reverse**. The
corroboration ledger stays untouched. Do the search first; it costs one call.

---

## 2 · RULINGS — DO NOT REOPEN

- **All of `-31`'s through `-51`'s rulings stand verbatim.** No third disclosure instrument;
  phrase set frozen at 38; §4.4 settled; SOURCE-001 FINISHED; THE ARM IS δ; §4.8 IS NOT THE
  COINCIDENCE ARGUMENT, §4.7 IS; REG-009 CLOSED (numbering 6–12); DO NOT SPEND THE TIE-BREAK;
  DO NOT PROMOTE R_MIN; SCOPE-001 / PIN-001 / TERM-001 / TERM-002 CLOSED; REG-010's POPULATION IS
  Ψ's 683 PAIRS; NEITHER BANDING IS PROMOTED; **R5 IS UNSPENT**; REG-012 CLOSED ON BRANCH F;
  55.71% IS Ψ's AND 63.16% IS THE BAND COUNT'S; T4's WIDTH IS 31.7%; SCOUT-001 IS WORKED and
  **T2 MAY NOT BE RUN ON THIS DATA** (carded `1217501628088122`); §4.7 IS PINNED AT `ba59370`;
  `wt107` IS NOT EDITED; CITE THE TEST, NOT THE `.bak`; THE `machine` COLUMN IS NOT A COVERAGE
  COLUMN; C07's GUARD IS `test_reg001_sec5_no_amendment_after_result.py`; A GREEN FROM
  `mutation_control.py` IS ONLY A MEASUREMENT IF `rc == 0`; G10 AND G13 ARE ESTABLISHING PROBES
  AND ARE EXPECTED GREEN; G12 IS NON-ISOLATING; **A CORRECTION IS NOT MADE UNTIL THE ARTEFACT IS
  EDITED.**
- **NEW · §9's LIMITATIONS ARE NINE ITEMS, AND NOTHING MANDATES A COUNT.** The `-42`–`-51`
  DO-NOT saying "FOUR, AND STAY FOUR" was **false when written** and is **struck**.
  `test_manuscript_lists_are_well_formed.py` asserts one thing: a list marker may not sit
  mid-line. **Re-wrap the ITEMS, never the block.** If you need a count, run the command in that
  file's docstring — it is a measurement, not a rule.
- **NEW · ADR-001's TITLE AND §Decision ARE DELIBERATELY FROZEN** at four papers, by its own
  header, as the record of the decision as made. **Do not "correct" them.** Every *live* clause
  now says three; `-52` struck the last three that did not.
- **NEW · THE ABSTRACT IS A SUBMISSION FIELD, NOT PROSE.** 247 w / 1,564 c, guarded by
  `scripts/check_abstract_size.py` and by row P1a. Any edit that grows it past **250 words or
  1,920 characters** breaks the board. Count with that script, never with `wc -w`.
- **NEW · THE MEASUREMENT LIVES IN `done-criteria.tsv`, NOT IN THIS FILE.** P1a–P1m each carry
  their own command. A future session that wants to know whether Paper III has its apparatus runs
  the board; it does not read a paragraph, and it does not re-litigate ADR-001's stale
  "all are absent today" line.

---

## 3 · THE AT-BAT for `-53` — **PAPER IV, WHICH DOES NOT EXIST**

**The board names it: `The next piece is P4`.** It is the only OPEN line on the board — every
other unmet line is `PENDING-HUMAN` and most of them are *downstream of IV existing*. It is also
substantively the long pole and **no session has ever claimed it**: `docs/papers/` contains
`paper-I-price-formation/`, `paper-II-redistribution/` and `paper-III-dual-tensor/`, and nothing
else. Nothing posts until IV is ready, by the `-08` batch ruling.

**P4's criterion, quoted:** *"Paper IV exists as a full draft (own charter + Paper I's surviving
subsection + Abandoned Approaches)."* Its check is `ls .../paper-IV*/paper-IV.md`, which is
deliberately weak — **it measures existence, not quality**, and P5 is the ready-to-submit bar.
Do not let the cheap green tempt you into a stub; write the draft.

**The three inputs are all written down already, which is why this is a drafting at-bat and not a
research one:**

- **ADR-001 §Paper IV** is its charter: the three literatures join, the same atomic unit composes
  from household to sovereign, the citation-graph whitespace (WT-006) as *evidence*, the
  relocation method (WT-039), the constraint-expiry argument — *force-fit, not form-fit* (WT-042)
  — as motivation. **And the one unforced error is named there:** the SMD-versus-scale tension
  must be resolved **explicitly** — the tensor composes, behaviour does not. Claiming clean
  composition without saying so, in a paper that cites SMD, is the mistake the ADR predicts.
- **Paper I's surviving identity** — *the crossing height IS the volume* — is a **subsection of
  IV**, per the `-10` addendum. Its dead framings become IV's *Abandoned Approaches* entry
  (WT-066, WT-070; `RESULT-WT070-p3-is-dead.md` is the record). Paper I is not a preprint. Read
  `docs/papers/paper-I-price-formation/paper-I.md` (7,367 words) as **source material**, not as a
  paper to revive.
- **Code:** none of its own. IV cites I, II and III as established results.

**OPEN WITH THE TWENTY MINUTES, AND POINT THEM AT THE PAPER.** Read `docs/HANDOFF-PROMPT.md`
§STEP 2's four rules first — **WT-079** (the deliverable is the paper, in the file, not a memo of
fixes), WT-078 (coaches not umpires), WT-080 (run the math before writing the finding), WT-081
(contribute and have fun). Then charter §3. Then draft. The apparatus bar is already enumerated:
**clone rows P1a–P1m into P5a–P5m against `paper-IV.md`** once a draft exists — the checks are
written and only the path changes, so IV inherits a measured apparatus for free. That is the
whole point of having done P1 as rows instead of prose.

**IF YOU TAKE SOMETHING ELSE, SAY WHY IN ONE LINE.** The two honest alternatives:

- **P2/P7 on Paper III** — a fresh-eyes review pass over the manuscript now that the abstract
  moved. Legitimate: P7 needs two consecutive zero-finding passes and has zero so far, and the
  abstract cut is the largest prose change in ten sessions. Weaker than P4 only because III is
  already the most-reviewed artefact in the estate and IV is at zero.
- **P3 on Paper II** — cheap (3,864 words, apparatus already close, abstract 261 w / 1,646 c so
  P1a-equivalent nearly passes). A good half-session, not a full one.

**THE GUARD PROGRAMME REMAINS PAUSED** (Jason, 2026-08-15) and `-52` did not resume it. A new
guard is in-contour **only** when it names the paper claim it protects and that claim sits on an
open P-line. The 61 probes are an asset, not a destination. Jason's three scoping proposals from
`-51` are **still UNRULED** — do not treat them as decided:
(a) audit the CLASS, not the constraint — one linter over claims naming a count, a filename or a
coverage fact, each required to carry the command that regenerates it, would have caught
`-44`, `-45`, `-46`, `-47`, `-50`, `-51` **and `-52`'s own false DO-NOT** in one pass;
(b) bound by value, not by list; (c) audit at the BOUNDARY — after III freezes, not continuously.

---

## 4 · TEED UP, IN ORDER

- **`G-T` calls a STALE claim LIVE and tells the owner not to commit.** Found by `-52`, **not
  fixed** — warning-level, and a third shared-infra edit at wrap was the wrong risk. The gate
  reported `darwin-mac-ops` DIRTY as *"LIVE roster claim by 'cloud-oaujFobu'. Do NOT commit it"*
  while the roster printed *STALE (>4h)* for that same claim in the same minute, **and** while
  the asking session held its own live claim on the resource. Net effect: the gate told the
  session that owned the change not to commit it. Fix: read the roster's own staleness verdict,
  and check whether the asker also holds a claim. Same family as `G-AL` — a check that cannot
  identify who is asking.
- **`~/.local/state/claude-session/current` is a single global file** and Jason runs 2–3 sessions.
  `G-AL` no longer trusts it (`CHARTER_SLUG` → `GATE_ROSTER_WHO` → the file), but **anything else
  reading it has the same bug.** One grep would find them.
- **C26 limb B** — carded `1217525563299334`. §2's twelve ratios with no counts; counts are in
  `RESULT-REG-006-ladderC-run.log`'s `obs` column. Named residual: §2.2's four discovered
  couplings (0.00×, 3.27×, 7.70×, 6.33×) are prose ratios with p-values and no counts. Rule on
  both together.
- **RESULT-REG-003 §2's "Every cut lands in R1"** — carded `1217518687033967`. Two readings; under
  one, 0.327 < 0.33 is R2. A `RESULT-*` is the record of a run, so the repair shape is a dated
  addendum (`-37` precedent). C12's guard is unaffected either way.
- **Cell (b), ranked in §3.2 — THREE entries left**, measured (§2c), **paused behind the paper**.
  The forbidden-claim family (C16/C20/C23/C25/C30, probes R5a–R5e, all five rc=0 under the
  repaired harness) · C45's two assertions · the reportable-at-all presence guards. Paused is not
  abandoned; if you take it, say why it beats Paper IV.
- **No probe has ever mutated `src/` except G7/G8.** The module surface is where the harness was
  blind and it is thin. Real, small, and still unclaimed.
- **C37's tripwire** — REG-009 §12's "never by narration"; §3.3 names the adjacent check.
- **§7's ledger dilutes its own two load-bearing rows** — Jason's call, TRIPWIRED not carded.
  `test_tripwire_c36_sec7_ledger_shape.py` asks him when the shape moves. Do not pre-empt it.
- **Dossier era, re-served by nobody:** REVIEW-004 C6 (ASC 410) and C10 (IAS 36's reversal
  asymmetry — a free cross-regime falsification test). *That C10 is REVIEW-004's, not the
  inventory's; the collision has bitten three times. Say which C10 you mean, always.*
- Infra siblings, carded: Caddy ordering `1217488447555628` · capability path in cleartext +
  repo drift `1217488117177482` · AAR A2's four post-* hooks · card-lint `1217483699706758` ·
  gate `1217465036940491`.
- Phrase-set passenger: 30.4% *match only events or circumstances*; 7.9% safe-harbour. Outranked.
- `AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded.
- Not mine, not touched: handoff-lint warns on `HANDOFF-acmeLedger-25.md` (zero `verify:` lines).

---

## 5 · DO NOT

- **Everything `-31`→`-51` forbade still stands verbatim** — R5, the two sensitivities,
  `selected_lives`, §4.4's 0.3000, T4's 31.7%, the δ arm, TERM-001/002, §9's list well-formedness,
  `wt107` IS NOT EDITED, cite the test not the backup, §4.7 IS PINNED AT `ba59370`, DO NOT
  "SIMPLIFY" A TRIPWIRE INTO A GUARD, DO NOT REPAIR A PROVENANCE FAILURE BY DELETING THE
  QUOTATION, DO NOT GRADE A CONSTRAINT FROM THE `machine` COLUMN, DO NOT RUN A COMMIT-ORDER PROBE
  WITHOUT `{"git": True}`, DO NOT WIDEN C07's GUARD, DO NOT PIN THE 98 AS A STRING, DO NOT WRITE
  AN OVER-BREADTH OR NON-VACUITY SELF-TEST WITH AN ABSENCE PREDICATE, DO NOT REVERT
  `mutation_control.py` TO `-rf`, DO NOT SLICE THE SWEEP LOG BY SLUG, DO NOT DRIVE `lessons.py
  use` FROM A `grep` OVER LEAF FILENAMES, **DO NOT TYPE A FULL SHA YOU HAVE NOT RESOLVED**, DO NOT
  LET `--check`'s EXIT 0 STAND IN FOR THE PREAMBLE BEING TRUE, DO NOT LEAVE A FINDING IN A HANDOFF
  WITHOUT EDITING THE ARTEFACT IT CORRECTS.
- **NEW · DO NOT OBEY A DO-NOT THAT NAMES A MACHINE WITHOUT RUNNING THE MACHINE.** One of the
  lines above was false for ten sessions because a count was lifted from an incident narrative in
  a test's docstring and nobody re-ran the test. A DO-NOT is the one part of this file nobody
  re-measures. **When a rule cites its guard, run the guard — it is one command — and be most
  suspicious when the rule points at REMOVING something.**
- **NEW · DO NOT MEASURE A TEXT LENGTH WITH `wc -w` OR `awk NF`.** They disagree by 7% with each
  other on this manuscript, across platforms, on the same bytes. `scripts/check_abstract_size.py`.
  And pick the strictest defensible definition **before** you look at the number — tokenising
  punctuation away after seeing the result is instrument-tuning, and this is exactly the moment it
  is tempting.
- **NEW · DO NOT ADD A REQUIRED KEY TO A GATE WITHOUT REBUILDING ITS FIXTURES FROM THAT SET.**
  Every test asserting the gate REFUSES starts passing for the wrong reason, and those greens are
  more dangerous than the reds beside them.
- **NEW · DO NOT LET A `manual:` ROW BE SCORED BY WHOEVER DID THE WORK.** P2 stayed
  `PENDING-HUMAN` on purpose even though every P1x sub-row is green: the session that measured
  should not also grade. P7's fresh eyes and P8 are the judges.
- Do not `git add -A` on darwin. Do not run bulk SEC work on darwin — cloud. Do not poll a
  background probe run with `while pgrep`.

---

## 6 · TRANSPORT — darlish, zero-bridge (unchanged, worked first try)

Standard bring-up; post the `DARLISH-ENROLL` line to Asana `1217316841710435` via the session's
Asana MCP, collect, then `dx`. First try, no fallback, `-06` through `-52`. If it does not come
up the first move is `dsh-fire` + `dwait`, not diagnosis. **Never restart the app to fix darlish
— it is not on the bridge.** `darlish-check` is not in the cloud kit; do not chase its 127.
`roster leave` ONCE at wrap.

- ⚠ **SET `GATE_ROSTER_WHO` INLINE.** `dx` spawns a fresh shell per call and carries no
  environment. Inline on `roster join`, `roster claim`, the commit, and every `lessons.py` call.
  `export` DOES work inside a script you `--put` and run with `bash /tmp/x.sh` — one shell.
- ⚠ **AND NOW ALSO ON `gate-selfcheck.sh`** (new, `-52`): `GATE_ROSTER_WHO=big-<sess>
  ~/Scripts/gate-selfcheck.sh`, or G-AL checks a sibling's project. See §4.
- ⚠ `roster claim` takes `--resource`, NOT `--repo`. `record-outcome <tag> pass` is two
  positionals, no `--id`. **Check a claim's output** — `-52` piped its first one to `/dev/null`
  and spent a round trip proving it had actually landed.
- ⚠ `lessons.py` AUTO-COMMITS AND AUTO-PUSHES each leaf. **Look before you reach for a commit.**
  It also **refuses** text that looks like captured command output (a real guard, hit once this
  session) and **forks a twin on an id collision** — `ls lessons/*/$(date +%F)-*` first.
- ⚠ **SMALL DIFFS DO NOT NEED A TARBALL.** `cat f | /tmp/dx --put /Users/jasoncbraatz/repos/...`
  per file: one call, sha256 verified against darwin. `-52` pushed six files that way. The
  tarball stanza is for coming DOWN only:
  `tar czf ... --exclude=.venv --exclude=.pytest_cache --exclude=__pycache__`, then
  `chown -R root:root` **and** `find -name '._*' -delete` (both required), unpack to `/root/wtg`.
  `--get` with a leading `~` expands in the CLOUD and fails; use `/Users/jasoncbraatz/...`.
  For docs-only work, `tar czf /tmp/wt-docs.tgz docs` is 1.2 MB against 20 MB.
- ⚠ **WRITE PYTHON PATCH SCRIPTS TO A FILE, THEN `--put`.** `-52` lost a round trip to a heredoc
  nesting Python inside Python inside bash, exactly as `-51` warned. The warning was right; take
  it the first time. `git checkout <file>` is the free undo.
- Exit codes: `3` never reached darwin (safe to re-run) · `4` dropped after the command started
  (check state first) · `5` crossed but mismatched, nothing written.
- Deps: `pip install --break-system-packages 'numpy>=1.26' 'scipy>=1.11' 'pytest>=8.0'`.

**SUITE:** 1055 collected, 1055 passed, zero skips — darwin ~64 s, cloud ~170 s. Without `.git`:
1034 passed / 14 skipped. `pytest -m tripwire` selects the four-file tripwire class.
`scripts/defensive_count.py` takes a positional path. **Probe sweep:** ~3 min 30 s per probe at
`--jobs 2`; a foreground `Bash` call dies at 10 minutes, so `nohup … &` and poll with
`sleep N; tail`. Use `--out <json>` — probes print in completion order. **Budget for running the
sweep twice**; `-49`, `-50` and `-51` all found the real defect on the second run.

---

## 0 · THE TELL, NOW IN SIXTY-SEVEN SHAPES

`-28` through `-51`'s tells all stand (ask the instrument-artefact question of numbers that look
GOOD, that SETTLE AN ARGUMENT, of a REGISTERED CONTROL THAT FAILS, OF THE DENOMINATOR; a guard
must scan assertions not quotations; a mutation that does not mutate reports your guard as weak;
pre-commit the FAVOURABLE outcome's meaning; a handoff's CHARACTERISATION is not a MEASUREMENT;
a correction that lives only in a handoff has not been made; a red the harness cannot parse
reports the guard as absent). `-52` adds six:

- **THE ARTEFACT IS ALSO A SURFACE, AND EIGHT SESSIONS OF INSTRUMENT FINDINGS IS THE SIGNAL TO GO
  LOOK AT IT.** A high finding rate against the apparatus is evidence the apparatus is deep, not
  that the subject is safe. They are not the same measurement, and one of them had not been taken
  in ten sessions. The finding was on line 15.
- **A RULE CAN BE FALSE ON THE DAY IT IS WRITTEN.** Not stale — *born* false. Staleness has a
  mechanism you can reason about (something changed); this has none, so nothing prompts the
  re-check. The only defence is running the machine a rule names, and DO-NOT lists are precisely
  where nobody does.
- **A COUNT IS NOT A MEASUREMENT UNTIL IT AGREES ACROSS MACHINES.** `wc -w` 248, `awk NF` 266,
  same bytes, 7% apart and straddling the threshold — so the criterion would have passed on the
  machine that wrote it and failed on the machine that runs the board. Count the decoded string
  and print both numbers on both machines *before* the threshold goes into a criteria file.
- **THE VISIBLE REDS ARE THE CHEAP HALF.** Adding a required key to a gate turned two tests red
  and three tests vacuously green. The greens assert `rc == 1` and were getting it from the new
  key rather than from the condition each names. **A green that no longer tests its own name is
  worse than the red beside it** — and only the reds announce themselves.
- **A CHECK WHOSE SUBJECT IS "THIS SESSION" MUST BE ABLE TO IDENTIFY THIS SESSION.** `G-AL` read
  one global file on a machine running three sessions. Its misattribution was worse than its false
  alarm: the remedy it printed would have laundered a sibling's real warning into an all-clear.
- **A GENERALISED ENGINE MAKES ITS PREDECESSOR'S LAYOUT LOOK LIKE A DEFECT.** `G-AL#board` tested
  for one project's `gen-done.py` and read its absence as "hand-maintained" — failing every
  project that adopted the shared engine, which is *everyone else, by construction*. When a tool
  is generalised, grep for checks that still assert the old shape.

---

## 7 · ORIENT-THEN-GO

Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
building. Don't wait for a go. Do not open by asking Jason anything.

**Coffee status:** ☕ EIGHTEEN SESSIONS RUNNING, and for the first time in ten the first twenty
minutes were spent on **the paper** instead of on the thing that measures the paper — `-44`
whether the guard can see it, `-45` whether its address was right, `-46` whether the sentence
that sent you here was ever checked, `-47` whether the instrument sees the whole board, `-49`
whether the machine was ever run, `-50` whether the correction reached the file, `-51` whether
the instrument can read its own output, and `-52` **whether anyone had read the abstract.** The
answer was no. It was 872 words in a 1,920-character box, it had been that way since the paper
existed, sixty-one probes and fifty catalogued constraints had been built around it, and the
thing that finally caught it was counting to two hundred and fifty. 🥎
