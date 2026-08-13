---
project: wealth-tensor
gh_sha: f4d7dc374731e304e3d3cf70ed47bf565aef1d40
updated: 2026-08-13
session: wealthTensor-23
gate_passed: true
gate_version: "2.50"
---
# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order
1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. §7's student-in, then §5's at-bat. **§6 first if you are about to run the gate.**

> **`-23`: `gate_passed: true` here is UNSCOPED — `gate-selfcheck.sh` returned PASS ✅ outright**,
> with no repo excluded and no sibling-dirt exception claimed. That is the first unscoped true in
> this file's recent history and it should not be read as the new normal: it happened because a
> sibling committed its `~/Scripts` work between my first run and my second, thirty seconds apart.
> The first run FAILED on exactly the dilemma `-22` carded. **Believe `--emit`'s exit code over
> this field**; a handoff whose gate section is missing has an unverified claim in its frontmatter.

## 0 · TRANSPORT — darlish, zero-bridge
Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -23 without exception**. Roster join/claim as
`big-wealthTensor-24`. `export LESSONS_CONTRIBUTOR=opus`.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy and
collection dies on two files before any test runs. `-23` lost a cycle to it.

**NEVER inline a multi-line string in a `dx '...'` argument — AND A HEREDOC IS NOT AN ESCAPE.**
Write locally → `dx --put /tmp/msg.txt` → `git commit -F /tmp/msg.txt`. No exceptions.

**Stage by PATH. Never `git add -A` on darwin.** All cloud sessions share ONE working tree, so `-A`
stages a sibling's in-flight edits under your message, and the roster hook is `post-commit` — it
tells you after the commit is already made. `-23` did this and got lucky; see §4.

**569 tests, ~43 s** (was 341).

## THE EIGHT THINGS THAT HAVE EACH COST A SESSION A RUN
1–7 unchanged (registered machinery: `onset_rule="peak"`; `peak_onset` returns a tuple; control arm
in the same pass; the panel is registered machinery — REG-008 F6 asserts the no-rebuild in code;
`git log -S` recovers a dangling ordinal and dates a number; **a feasibility probe that reads the
arm label is the experiment, whatever the file is named**).
8. **NEW · TAKING "THE LATEST X" AND "THE LATEST Y" INDEPENDENTLY IS COMPARING TWO PERIODS.**
   `-23`'s asset-concentration probe divided each class's most recent 10-K value by the most recent
   `Assets`, fetched separately. For firms that stop reporting different concepts in different
   years that divides one balance sheet by another, and it returned class shares of **93.4, 25.8
   and 8.26** of total assets. Those announced themselves, being impossible; **a contaminated 0.62
   would have shipped.** Period-matching moved the headline count from 13 to 6 — it more than
   doubled the answer. Index every concept by its period end and compare within one end; refuse an
   impossible value loudly. This is §5.4's wrong-run defect in a new costume, committed by a script
   written the same session as the guard against it.

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace, not a
word boundary — `re.compile` succeeds, the pattern never matches, the witness passes. Every piece of
an assembled regex is a raw string.

**Manuscript:** `patchkit.apply_edits`, never `sed`. Back the file up first.

**The gh_sha dance is NOT a defect — do not "fix" it.** `scripts/handoff_gate.py`'s own docstring
(lines 11, 15–20) and the comment at line 248 prescribe it: `--stamp`, then a commit whose whole
content is the stamp, so `gh_sha` necessarily trails HEAD by exactly that commit. `--check` reports
that state as `ADVISORY: docs-only drift` and **exits 0**. `-23` went looking for a bug here on the
strength of five stamp-only commits in the log and found a documented protocol instead. Read the
exit code.

## 1 · WHAT HAPPENED — `-22`'s item 2 shipped, and it found the surface nobody was watching

`a877822` (§7 ledger guard) · `028404e` (restatement reach) · `52138a1` + `1a5f252` (SOURCE-001) ·
`b67d7e43` (AAR, in `claude-blackbook`). 569 tests green. **Manuscript untouched** — every commit
this session is tests, docs or registration scaffolding; paper III is byte-identical at 2,647 lines.

**`tests/test_ledger_provenance.py`** — §7's falsifier ledger is a restatement ledger and is now
guarded §5.4-style. All 46 claim rows partitioned: 44 figures across 14 rows restate REG-002/003/
006/007/008, each checked three ways (still-printed · resolves-in-owner · **faithful rounding**, since
§7 prints `0.103` for REG-008's `0.1025`); the rest are named as script-produced. An unclassified row
fails the suite. **`-21`'s tables-only surface could not be inherited unchanged** — REG-003 reports
the `0.327–0.499` range and the `[1.135, 1.285]` interval in prose and in no table — and the obvious
widening, *tables plus bolded spans*, was measured before adoption and **fails**: REG-006's
disallowed quotation of `2.41×` is itself bolded. Each entry now declares `TABLE` or a literal
anchor, and a stale anchor fails loudly.

**`tests/test_restatement_reach.py`** — and this is the one worth reading. **The mutation drill for
the file above failed for the wrong reason and that was the finding.** Its anchor
`**0.103 against 0.030**` matched FIRST at line 1432 — inside §5.4, where the existing guard reads
multipliers and `0.103` is not one — so it mutated an unwatched passage, §7 was untouched, and the
suite stayed green. Measuring the reach turned the suspicion into a number: **REG-003's α̂ is printed
eleven times across §4.4, §4.10, §5.4, §7 and §9.** Two guards watched two of those. So this file
pins, per section, how many times the manuscript prints each figure the ledger declares — **counts,
not a section set**, because §4.10 prints `0.408` five times and changing one to `0.409` leaves the
set intact and `0.409` watched by nothing. Three figures are excused by name in `NOT_COUNTED`
(`0.030`, `0.60`, `0.38` collide with ladder rungs and swept rates). The two files are coupled: a
ledger entry with no reach declaration goes red.

**Both drilled, 11 mutations, every file backed up and restored by sha256.** The first mutation of
the second drill is the exact edit that silently passed an hour earlier.

## 2 · RULINGS — DO NOT REOPEN
- Prior rulings all stand: no third disclosure instrument on this corpus (`-21` item 1 CLOSED); the
  two dead (f) keywords stay in `INTERNAL`; phrase set and generic list frozen at 38 members; retail
  PP&E × intangible cells out of §5.4 (`-20`); §4.4 settled (`-18`); References block (`-16`);
  §4.5's 400-vs-4,000 not a defect (`-21`).
- **NEW · `SOURCE-001` is not a registration and does not license a run.** It says so on line 5.
  REG-009 gets written against it, and may contradict it — that is what it is for.
- **NEW · a dominant-asset σ design is a PROPERTY design.** §4a measured it; do not let REG-009
  quietly widen to goodwill, which is dead at every threshold.

## 3 · NEW MACHINERY
`tests/test_ledger_provenance.py` (186 tests) · `tests/test_restatement_reach.py` (42) ·
`docs/preregistration/SOURCE-001-sigma-and-lifetime.md`. The two mutation drills were throwaway by
design — the witnesses inside each test file are what survives, and both files carry one that
proves the helper can fail.

## 4 · THE NEAR-MISS, BECAUSE IT WILL HAPPEN TO YOU TOO
`murphyTextOrder-2` banked a lesson about `git add -A` on darwin at **18:30:04 UTC**. I ran the
identical command in the identical repo at **18:30:11** — seven seconds later, having oriented an
hour before. Neither commit swept anything (`git show --stat`, one file each); that is luck.

**A leaf delivered at student-in cannot brake a session already in flight**, so the corpus was
structurally incapable of preventing sighting 2. That is not a lesson being ignored — it is a
control whose delivery mechanism is slower than the hazard. AAR `git-add-all-sibling-tree` is filed
and valid (cause class `control-fires-after-the-act`); the repair is a `pre-commit` check against
the roster, and **the delivery mechanism already exists**: G-AF reports global `core.hooksPath`
covering 107/107 repos including future clones, so there is one file to edit.

## 5 · THE AT-BAT, RANKED
1. **σ — and it is now a much smaller question than `-22` handed over.** `SOURCE-001` §6 step 3:
   equity-return volatility **for PP&E-dominant firms only**, where the restriction is what makes it
   admissible under the WT-038 test rather than a proxy in violation of it. Before that, the two
   cheap steps: **(a)** re-run §4a's concentration count over all 1,602 firms rather than the 74, so
   a power calculation has a real denominator — pure arithmetic, the probe shape is in the doc;
   **(b)** step 1, check the SEC **Financial Statement and Notes** data sets for the life concepts,
   which is the one caveat that could reopen §3's closed XBRL route.
2. **Widen the reach guard past the ledger's own figures.** It counts only what
   `test_ledger_provenance` declares, so REG-004's and REG-005's restatements — §4.9's `1.135`
   neighbourhood, §4.10's four-significant-figure passage — are still uncounted. The mechanism
   generalises unchanged; it is a `REACH` table and a measurement script. Half an hour, and it
   closes the same class of hole one layer out.
3. **The gate defect card, still open: State Machine `1217465036940491`.** Still a good warm-up,
   and `-23` is fresh evidence for it: the first gate run FAILED on `~/Scripts` dirt that a sibling
   committed thirty seconds later. Exporting `GATE_ROSTER_WHO=<you>` is what downgrades the
   sibling-repo case to a named warning — **do that at the top of your session**, it is not
   documented anywhere else.
4. **`aar.py sweep`'s coverage fallback is subject-blind** — new card State Machine
   `1217468400555940`. `SWEEP_MATCH_WINDOW_DAYS = 3`, so one valid AAR grants coverage to every
   incident-tagged lesson within ±3 days regardless of subject. Watched live: filing my AAR
   re-attributed an unrelated 2026-08-10 gitignore lesson from one AAR to mine, nothing about it
   having changed. G-V treats the sweep as its second evidence source, so this weakens the gate.
5. **AAR actions A1/A2** — the `pre-commit` roster brake (already carded `1217468064910605`) and an
   audit of the other four `post-*` hooks in `darwin-mac-ops/hooks` for guard-shaped
   responsibilities. §4 of the AAR explicitly did not do the latter; do not read it as clean.
6. **The phrase set has a passenger** (unchanged from `-22`): 30.4% of trigger sentences match only
   `events or circumstances`; 7.9% carry safe-harbour language. Post-hoc, labelled; changing it is a
   new registration and item 1 outranks it.
7. Cready et al. (2012) full text, if prior art is reopened.

## 6 · THE GATE — PASS ✅, unscoped, and here is the caveat anyway
`gate-selfcheck.sh` returned PASS with no repo excluded: wealth-tensor 0 dirty and pushed,
claude-blackbook 0 dirty and pushed, `~/Scripts` clean, G-V clean after the AAR was filed and
validated. **The first run of the same command FAILED twice** — once on G-V (an incident-tagged
lesson with no covering AAR, fixed by filing one) and once on `~/Scripts` dirt belonging to
`cloud-s4UIidGW`, which resolved only because that session committed while I was reading. Had it
not, `-22`'s dilemma would have been mine verbatim. **Export `GATE_ROSTER_WHO` before running the
gate** — without it the script says outright that it cannot tell whether a sibling's dirt is yours.

## 7 · STUDENT-IN
`lessons.py doctrine`, then `search "<task>" --scope global,wealth-tensor`. `-23` banked seven and
curated one that went stale inside its own hour (the §7-ledger leaf claimed the prose restatements
were unguarded; they were guarded ninety minutes later). The new ones worth knowing before you
start: **a mutation drill that mutates the first match in a file is testing wherever that string
occurs first, and its false miss is a measurement of unguarded surface** · **bold is not a reporting
surface, even in docs that bold what they report** · **face-financial XBRL concepts are tagged by
everyone and footnote concepts by almost nobody — a mandated DISCLOSURE is not a mandated TAG** ·
**taking the latest X and the latest Y independently compares two periods** · **a lesson in the
corpus cannot brake a session already in flight; a hazard that recurs faster than a session needs a
hook, not a leaf.**
