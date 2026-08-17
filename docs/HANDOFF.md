---
project: wealth-tensor
gh_sha: 2b3e24b5c6a01a891eee8a6cb81d37d6ff422b6d
updated: 2026-08-17
session: wealthTensor-64
gate_passed: false
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-64` IN ONE LINE
**PAPER II WAS READ INDEPENDENTLY FOR THE FIRST TIME AND RETURNED NINE FINDINGS, ALL REPAIRED** —
`docs/REVIEW-007-P7-pass-3.md`. Two of the nine are `REVIEW-004` §A3 items that have been live for
five days under a commit message that reads as though A3 was served whole. **And the pass turned up
three things about the review apparatus that are worth more than the nine:** `PIN-001`'s class
repair watches one manuscript of four (Paper IV's `5efe626` is orphaned), the handoff gate never
runs a test suite, and — **read this first** — **the repository's suite is RED at HEAD and has been
since `-63`'s commit.** `LEDGER` `WT-092`→`WT-095`. Board still **52/66**, regenerated and verified.

> 🔴 **NEW AND LOUD: `python3 -m pytest tests/ -q` IS 1073 PASSED, 1 FAILED.** The failure is
> `tests/test_reg012_sec6_sec47_frozen.py::test_section_47_is_byte_identical_to_the_pin`, red since
> `6314302`. **It is not a `REG-012` violation** — §6 freezes §4.7 against *"any outcome of it"* and
> the edit is `-63`'s `III-3` repair, licensed by `ASC 350-30-35-15`, an outside standard. **And the
> guard's own prescribed remedy is impossible**: it tells you to re-pin `SEC_47_SHA256`, while its
> sibling `test_the_pinned_digest_is_the_version_REG_012_saw` asserts the pin equals §4.7 *at the
> registration commit*. No value passes both. **DO NOT re-pin it on the strength of the failure
> message.** Card `1217542940969153` has the whole analysis and the two options. `-64` declined for
> the standing reason: a judgement change to a safety guard — here over a preregistration — wants
> its own at-bat.

> ⚠ **`gate_passed: false`, EIGHTH CONSECUTIVE SESSION, SAME TWO FILES. PERMANENT. YOU WILL INHERIT
> IT.** The single `FAIL` is `~/Scripts DIRTY(2)`: `braatz-crawl-check.py`,
> `serve-braatz-archive.py`. **DO NOT COMMIT THEM.** `-61` measured it: mtimes Aug 16 13:37 / 13:35,
> before any roster join — they cannot be ours, and that is arithmetic. Card `1217526943288480`.
> `-59`→`-64` all declined. **Say it out loud anyway: a session that EXPECTS a red gate will not
> notice a real one** — which is exactly how the pytest red above crossed a `PASS`ing gate.

## FIRST, BEFORE ANYTHING: `DECISION-001` IS STILL UNTICKED
`docs/DECISION-001-A2-and-road-one.md`, all four boxes `☐`, mtime **Aug 17 00:02**, verified at
10:24 today. **If a box is ticked, that outranks the board and everything below.** Do not write a
second one-pager and do not re-litigate it. `II-2` and `II-3` are two of whichever option's edits —
they were **re-found independently by `-64`** (before `REVIEW-005` §2 was read, by a different
route) and stay blocked for `REVIEW-005`'s reason, which is still right.

## STATE
- **The end-to-end pass is CLOSED** (T=2, A=0, the system fails, E1–E6 spent). Settled, not an
  at-bat.
- **`P7` has three documents now**: `REVIEW-005` (`-62`, the backlog drain), `REVIEW-006` (`-63`,
  the re-grade + Papers IV and III·A.2), `REVIEW-007` (`-64`, Paper II).
- **`P7`'s consecutive-zero count is 0 for all three papers**, and every paper has now had exactly
  **one** independent read. Convergence needs **two consecutive zero-finding passes per paper**, so
  the earliest any paper can close is its next pass. Paper II's first read found nine; do not read
  that as "Paper II is the bad one" — Paper IV found six and Paper III's appendix two, on the same
  first look. `WT-091`.
- **§3 of Paper II reproduces byte-exact** from `python3 scripts/wt030_report.py` at `T=1200`,
  `seed=0` — every number, first time anyone ran the committed command rather than reimplementing
  from the prose. The two defects it exposed were both in the one section whose numbers are *not*
  in the table.

## WHAT `-64` DID, so you do not re-derive it
Nine findings, all repaired, 14 hunks in `paper-II.md` + one `LATEST_TOUCH` entry. In full in
`REVIEW-007` §1; the ones that will otherwise cost you time:
- **`II-5` · §7's pin was the `PIN-001` sentence, verbatim, in the sibling manuscript.** *"d655501 —
  the last commit touching `src/`"*, false since 2026-08-10, present since `f1ceac7`, and **absent
  from `PIN-001`'s own census of six occurrences.** Now a per-file pin (`3b11f23`) *and*
  instrumented. `WT-093`.
- **`II-6`/`II-7` · §3.4 carried a 600-period run under a paper-wide `T = 1200`** (0.977/0.988
  against §3.1's 0.994/1.000 — `REVIEW-004` §A3 said *"nothing explains the gap"*; `is_bounded`'s
  own docstring explains it), and its separation range *"0.19–0.50"* is refuted by the paper's own
  sweep **on either reading of the unnamed statistic** (Gini: 0.000–0.891; top decile: 0.100–0.861).
- **`II-8` · *"within 5 % and which the test suite asserts"* was wrong in both halves.** Residuals
  −4.4 / −4.9 / **−6.8** %, and the suite asserts `rel=0.10`. Prose repaired; the code fix is
  carded (`1217542935918371`) **with the term `REVIEW-004` §A3 missed** — the wage is in the flow
  base (`recognised_flow += rho*gain + self.wage`), so the numerator omits a term and the
  denominator omits growth, and they partially cancel.
- **`II-9` · §1 and the closing note both said "§3.1 mentions zakat".** §3.1 does not — zero
  occurrences, normalised. The house-style pass removed it and left both pointers.
- **`II-11` · the abstract said "an open repository with 18 tests"**; the repository holds **572**
  test definitions. §1 and §7 scope it correctly and `-58`'s instrument asserts §7's phrasing, so
  **no test could see it.** Repaired **word-neutrally** (249 words, 4 chars shorter) — see the
  do-not below, this one nearly cost a falsification instrument its subject.

## YOUR AT-BAT — take one, in this order
1. **THE `REG-012` RED.** The corpus is red and everything else is polishing while it is. Card
   `1217542940969153`. It needs one ruling, not one hour, and the analysis is done — you are
   choosing between reverting an outside-licensed repair and restructuring the guard so a warranted
   edit can be recorded without erasing the registration-era anchor.
2. **`PIN-001`'s CLASS HOLE.** Card `1217542847080795`. **Instrument Paper IV's `5efe626` FIRST**,
   then widen `test_manuscript_shas_are_instrumented.py` to a glob over all four manuscripts.
   Widening first goes red. `-64` measured the census without editing the instrument; the numbers
   are in the card.
3. **PAPER II's SECOND INDEPENDENT READ** — the one that could actually start a convergence count.
   Not a re-read of `REVIEW-007`'s findings: a fresh end-to-end pass asking `P7`'s question, of a
   manuscript that changed in 14 places this morning. **`-63`'s corollary applies with force: a
   repair can introduce a defect, and two of `-62`'s seven did.** Diff against
   `paper-II.md.bak-wt64-p7` rather than reading the repaired text as given.
4. **THE ABSTRACT COMPRESSION PASS**, still teed up from `REVIEW-005` §7 and still cheap: III
   247/250, IV 248, **II 249** (unchanged — `-64`'s abstract repair was deliberately word-neutral to
   leave the slack for `DECISION-001`). `-63` showed the cheap direction is deleting false
   generalisations, and it is nearly exhausted.
5. **`P6`'s remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
6. **Paper II's companion reference entries** — card `1217542940968749`, `REFERENCE-POLICY`
   jurisdiction.

**FORCING LINE (`-59`'s ruling, kept): take none of these, say why in ONE LINE at the top of your
handoff. It costs nothing.**

## THE TELL, and it is now four deep
`-61`: **a corpus under repair has a moving referent and only the filesystem knows.**
`-62`: **the line-wrap grep trap runs both ways** — normalise before asserting presence *or*
absence (`tr '\n' ' ' < f | tr -s ' ' | grep -o '…'`), and **never `grep -oc`** (`-c` overrides
`-o` and counts lines; on a flattened file it counts **1**, always — `-64` tripped this and caught
it by re-measuring with `grep -o | wc -l`).
`-63`: **a backlog drain measures the backlog, not the paper, and the two are indistinguishable on
the board.**
**`-64`: A REVIEW APPARATUS HAS THE SAME DEFECT AS A MANUSCRIPT — ITS OWN COVERAGE IS AN UNMEASURED
CLAIM, AND THE SILENCE READS EXACTLY LIKE COVERAGE.** `REVIEW-004` §A3 said "three things" and was
closed by serving one. `PIN-001` said *"this repairs the CLASS"* and hardcoded one of four
manuscripts. The gate says `PASS` and never runs a suite. Each is **right about what it checks and
silent about what it does not reach.** The question that finds all three is not *is this checked?*
but **what is the widest object this check's own words claim, and what is the narrowest thing it
actually touches?** `LEDGER WT-092`.
**Corollary, free, do it every pass:** end by asking *which instrument would have caught this
finding, and does it exist for the other three papers?* Six of `-64`'s nine findings had an
instrument watching the identical thing one file over.

## DO-NOTs THAT ARE NOW RULINGS
- **DO NOT re-pin `SEC_47_SHA256`** because the failure message says to. Read card
  `1217542940969153` first; the sibling test forbids it.
- **DO NOT widen `test_manuscript_shas_are_instrumented.py`** before instrumenting Paper IV's
  `5efe626`. It goes red.
- **DO NOT delete `"18 tests"` from Paper II's abstract.** It is one of only two *literal*
  occurrences (§1 has `the 18 tests in`, §7 has `the **18** tests in`), and it is the subject of
  `scripts/redproof_apparatus.py:105`'s mutation control and of a board row's rationale in
  `gen_apparatus_rows.py:166`. Deleting it starves a falsification instrument **while the suite
  stays green.** `WT-094`. Same rule generally: **grep `tests/` and `scripts/` for any manuscript
  string before you edit it.**
- **DO NOT re-derive the κ residuals.** −6.78 / −4.91 / −4.35 %, monotone, therefore a denominator
  convention. Twice-derived now (`REVIEW-004` §A3 and `-64`, independently, identical).
- **DO NOT re-derive `III-1`'s 4.2×.** Correct under both readings; scale-invariant. `REVIEW-006` §1.
- **DO NOT propose a `REG-013` re-run to "fix" the seeds.** §6 forbids re-choosing a seed list in
  response to anything. The correction note is the whole remedy. `WT-090`.
- **DO NOT re-derive the `P2`-at-three-strengths lead** (withdrawn, `REVIEW-005` §3), **re-mine the
  `E2` blind pass** (all 28 rows scored), or **re-serve `REVIEW-004` by section number** — its §
  numbers are from an earlier draft and do not resolve. **Match on its verbatim quotes only.** And
  note `-64`'s addition: **§A3 is the section every re-serving pass skips**, because Part A reads as
  the big three and A3 reads as the leftovers. It holds three real items.

## TOOLING, measured at `-64`
- **STEP 0 was `READY` on the first try again** (fourth session running): `darlish-up` → post the
  printed `DARLISH-ENROLL` line verbatim as an Asana comment on `1217316841710435` → `darlish-up`
  again → fetch `dx`. Budget four minutes, and it took less.
- **`dx --get` printed the remote `cat: No such file` error and still exited 0.** Observed once,
  on a wrong absolute path (`/root/...` — **darwin's `$HOME` is `/Users/jasoncbraatz`, use `~`**).
  So `--get`'s exit code did not carry a missing-source failure; check the file landed. The
  documented codes (3 = never reached darwin, 4 = dropped after starting) held everywhere else.
- **RUN THE GATE AS:** `GATE_ROSTER_WHO=big-wealthTensor-NN nohup ~/Scripts/gate-selfcheck.sh
  > /tmp/gate.log 2>&1 &` then poll with two `sleep`s (~170s each; cloud Bash caps at 2 min).
  **`G-AL` and `G-AL#board` are SILENT ON SUCCESS.** The thing to grep is
  **`grep -c "CANNOT VERIFY"` == 0**.
- **AND RUN THE REPO'S SUITE YOURSELF.** `python3 -m pytest tests/ -q`, ~70 s, 1074 tests. The gate
  does not (`WT-095`). Say the result in your handoff.
- **IF YOU EDIT ANY PAPER, REGENERATE THE BOARD BEFORE THE GATE:**
  `python3 ~/Scripts/handoff-kit/board.py --criteria docs/done-criteria.tsv --project wealth-tensor
  --out docs/CHECKLIST.md --preamble docs/checklist-preamble.md --check` — rc=0 prints *"matches
  measured reality (66 criteria)"*. Drop `--check` to write it.
- **ANY EDIT TO ANY ABSTRACT:** `python3 scripts/check_abstract_size.py <PATH> --print`. **It takes
  a PATH, not a slug.** NEVER hand-count — and note `-64`'s use of it: it will also *measure
  candidate rewrites*, which is how the word-neutral abstract repair was chosen out of four
  candidates in one call. Two of the four were 250 and would have spent the last word of slack.
- **A BATCHED PATCH SCRIPT BEATS N EDITS.** `scripts/wt112_edits_wt64_paperII.py` is this session's
  worked example: one list of `(path, label, old, new)`, `assert count(old) == 1` for **every**
  anchor before any write, `.bak` every touched file, `--dry` mode that writes `*.wt64-dryrun`
  siblings. **Dry-run in the cloud container against a copy and `diff` it there first** — that is
  what caught four ragged rewraps (extend anchors to **sentence** boundaries, per `-63`) before
  anything reached darwin. `awk 'length>100'` before and after: 6 → 6, all pre-existing.
- **Name your patch script in a free `wtNNN` tag.** `-64` first wrote `wt093_…` and collided with
  another session's five-script family; tags run to `wt111`, so `wt112` was free.
- **`lessons.py use` / `record-outcome` can hang past 4 minutes.** One per `dx` call, 300 s
  timeout. `lessons.py add` was fast (~10 s) and auto-commits and pushes `claude-blackbook`.
- **`COMMITMSG.txt` → `dx --put` → `git commit -F`.** Never inline a multi-line message in `dx '…'`.
- **Asana `create_tasks` silently drops `projects`** — `update_tasks` with `add_projects`, then
  **verify** with `get_task opt_fields=name,projects.name`. Held again this session.
- **`roster claim` needs `--who` AND `--resource`. `lessons.py use <id> --task <tag>` — id
  positional.**
- **The project's own wrap sequence for this file** (from `scripts/handoff_gate.py`'s docstring, and
  it is load-bearing): edit content with `gh_sha: PENDING` → commit → `--stamp` → commit → `--emit`.
  `--emit` does **not** stamp, and it refuses a `PENDING` sha.

## JASON-SIZED, already surfaced, not yours to decide
- **(a) `DECISION-001`, A/B/C, still unticked.** `II-2` and `II-3` are two of whichever option's
  edits; do not repair them separately.
- **(b) Paper IV's title and abstract leading clause** still read *"from the household to the
  sovereign"*. Narrow it, or ratify the appended demotion as sufficient.
- **(c) `P7` is still ONE BOOLEAN** reading 0/1 for a criterion that is per-paper with a two-pass
  counter. `-62` carded it, `-63` confirmed it, and `-64` now makes it concrete: **the board cannot
  distinguish "no paper has ever been read" from "every paper has had exactly one independent read
  and found between two and nine defects"** — which is the true state today. Adding rows moves the
  66, so it wants its own at-bat.

## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` and say the number; `roster leave`
once; and paste a handoff better than this one into the chat as the **last act**.
