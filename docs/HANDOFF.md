---
project: wealth-tensor
gh_sha: a61989c97c92b9b36584dd8dfa2c4a13f60c6e97
updated: 2026-08-17
session: wealthTensor-65
gate_passed: true
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-65` IN ONE LINE
**`DECISION-001` IS TICKED — Jason ruled option A on 2026-08-17 — and A is applied, tested and
pushed.** Do not re-read the one-pager to decide anything; read it to see the reasoning, which is
now recorded on the page. The suite is **green: 1078 passed, 0 failed**, up from `-64`'s
`1073 passed, 1 failed`. Three at-bats closed: the `REG-012` §4.7 freeze (`3ffb3f1`, `WT-096`),
`PIN-001`'s class hole (`ba95302`, `WT-097`), and `DECISION-001` option A (`52ef4f2`, `WT-098`
and `WT-099`).

**THE RULING, IN JASON'S WORDS, because it is a sequencing decision and not simply "A":**

> *make a full Kelly bet on A, and only re-allocate that bet once we can build — or IF we can
> build — credibility behind C.*

**So option C is NOT dead. It is deferred behind its own blocker, and that blocker is now YOUR
AT-BAT** — see §1 below. B was declined for a reason about *order* rather than about B: if C
happens, C replaces the title anyway.

---

## READ FIRST, in this order
1. **`docs/DECISION-001-A2-and-road-one.md`** — ticked, with the full defensibility reasoning
   recorded under the tick. This is where the "why not C yet" argument lives.
2. **`docs/LEDGER.md` `WT-096` → `WT-099`** — this session's four entries.
3. **`docs/REVIEW-007-P7-pass-3.md` §9** — still the frame.
4. `REVIEW-006` §7 and `REVIEW-005` §3 remain worth ten minutes — **but see `WT-098`: `REVIEW-005`
   §2's `II-3` diagnosis is WRONG about the code. Do not re-serve it without opening `src/`.**

---

## YOUR AT-BAT — take one, in this order

### 1. **THE LITERATURE SEARCH.** Card `1217547572131984`. This is the one.
Six sessions carried option C as *"blocked on one literature search, never run"*. It went unrun
because it was filed behind the decision, the decision waited on the price of C, and the price of
C is exactly what the search reports — **two items politely holding the door for each other for
six sessions.** A literature search is a Claude with web access and an afternoon; it is not a
Jason-sized decision, and treating it as a blocker is what kept it one.

**The question:** has anyone already published the **truncation-vs-scaling effect on the tail
index** of a multiplicative (Kesten-type) wealth process — a stock levy *rescales* the growth
multiplier, a flow levy *truncates* it? `REVIEW-004`, `ROADS-001` and `HANDOFF-PROMPT` all name
the same place to look: **optimal-taxation-with-Pareto-tails**.

Either answer is worth the at-bat. Clean → C is fully priced and Jason decides with information
(and its two hardest computations are already done and sitting in Paper II). Known → C collapses,
A was right, and it cost one at-bat instead of a 26 KB rewrite that would have led with someone
else's result. **The trap:** *"I searched and found nothing"* is only a result if the search was
wide enough to have found something. Say which terms and databases, and what a positive would have
looked like — otherwise it is an absence predicate passing vacuously (`-49`'s rule).

### 2. **PAPER II's SECOND INDEPENDENT READ** — the pass that could start a convergence count.
Paper II moved in **24 places in the last 24 hours** (`-64`'s nine, then this session's ten).
**Diff against `paper-II.md.bak-wt65-decA` and `paper-II.md.bak-wt64-p7`; do not read the repaired
text as given.** Its consecutive-zero count is still 0.

### 3. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
### 4. **Paper II's companion reference entries** — card `1217542940968749`, `REFERENCE-POLICY`.
### 5. **The ρ = 0 test under-asserts** — card `1217547799559841`. The manuscript now says
*"leaves the wealth vector exactly unchanged"* in three places and **nothing asserts the
exactness**. Read the card before touching it: the naive repair (tighten the float tolerance to
`==`) is how you hand the next machine a red suite. Assert the *structural* property instead — that
the ρ = 0 flow base is uniform across agents — which is what makes the identity and is
platform-independent.
### 6. **PAPER I's FIRST INDEPENDENT READ** — the only manuscript with no `P7` pass at all.

**FORCING LINE (`-59`'s ruling, kept): take none of the six, say why in ONE LINE at the top of your
handoff. It costs nothing.**

---

## WHAT `-65` DID, so you do not re-derive it

### A · The `REG-012` §4.7 red — ruled, repaired, falsified (`3ffb3f1`, `WT-096`)
**Not a violation.** §6 forbids edits from `REG-012`'s **own** outcome (branches R/F/N, band-count
edge phase); `-63`'s `6314302` is licensed by **ASC 350-30-35-15** and *narrows* the paper's claim.
Verified by walking every commit that touched paper-III since `ba59370`
(`scripts/wt113_sec47_history.py`): §4.7 held **byte-identical across eight** and moved at
**exactly one**.

**The defect was never the freeze.** `-43` wrote one constant for two roles and a red message
prescribing a re-pin its own sibling test forbids — **the remedy was executable exactly zero
times**. Repaired into `SEC_47_AT_REGISTRATION` (immutable) + `SEC_47_CURRENT` (derived from an
append-only, git-checked `AMENDMENTS` ledger).

### B · `PIN-001`'s class hole — closed (`ba95302`, `WT-097`)
Paper IV's orphaned `5efe626` instrumented; the SHA guard widened from one hardcoded manuscript to
`glob("docs/papers/*/paper-*.md")`, **with a floor of four asserted on the glob itself** because a
glob that matches nothing passes everything vacuously. Ordering measured, not trusted: the widened
instrument was run against the un-instrumented registry first and went red naming exactly
`['paper-IV.md 5efe626']`.

### C · `DECISION-001` option A — applied (`52ef4f2`, `WT-098`, `WT-099`)
Ten edits, two files. κ demoted from *mechanism* to *budget* everywhere; the sentence A calls for
added after §3.1's matched-κ paragraph, **with both witnesses** (§3.1 matches two levies at κ and
finds them compressing unequally; §3.3 removes a quarter of κ at no measurable cost). `II-2` and
`II-3` repaired, as `REVIEW-005` §2 said they would be by whichever option was ticked.

**THE CENSUS FOUND A SIXTH SITE, AND IT WAS NOT IN A MANUSCRIPT.** `DECISION-001` prices A as
*"5 places"*, all in `paper-II.md`. Swept across manuscripts, `tests/`, `scripts/` and `src/`
**before editing any of them** (`scripts/wt115_kappa_census.py`), κ-as-mechanism had **six**:
`tests/test_redistribution.py`'s docstring opened *"kappa … is the mechanism"*. Nothing asserts a
docstring — the manuscript would have retracted a claim its own suite goes on making. The test's
*name* was right all along and every assertion in it is a budget fact; only the prose overreached.
**The source was already correct** (`redistribution.py:50` has said *"the levy's compressive
budget"* the whole time).

**AND `REVIEW-005` HAD THE ρ = 0 MECHANISM WRONG, IN THE PAPER'S FAVOUR — `WT-098`, read it.**
`II-3` says ρ = 0 *"sets the base and κ to exactly zero"*. That was about to go into the abstract.
`redistribution.py:131` is `recognised_flow += self.rho * gain + self.wage`, so **the ρ = 0 flow
base is the accrued WAGE**. Measured (`scripts/wt115_rho_zero.py`): **κ = 0.000565, not zero, over
1200 assessments that really fire.** And the conclusion is nevertheless true and **stronger than
anyone claimed** — `np.array_equal` on the wealth vectors is **True**, max difference **0.0** —
because `self.wage` is a scalar identical for every agent, so the levy is a uniform assessment with
a uniform per-capita rebate, which is the identity map. **What ρ = 0 removes is not the levy but the
dispersion in its base.** The paper said *"statistically indistinguishable"*; repaired **upward** in
three places.

**It also moved the decision.** `ROADS-001`'s case for C was that this tautology *"becomes a passed
test — the framework predicting in advance that ρ cannot change *A*'s shape."* That needs the result
to be about the multiplicative term. It is about a constant wage. **One of C's two headline
payoffs was resting on the same misdiagnosis**, found twenty minutes after the tick.

**Abstract: 249 → 244 words** (ceiling 250), 1478 chars (ceiling 1920). **Six words of slack
RETURNED rather than spent.** Twelve candidates measured before one was chosen; round 1's twelve
*all* blew the ceiling at 262–274 because every one **added** a "κ is a budget, not a mechanism"
clause. **The demotion is achieved by DELETING the assertion, not by arguing with it** — and an
abstract that argues with a claim it no longer makes is defensive narration besides.

### D · Five new mutation probes, in the estate's own harness
`G14` (launder reading (a) into the amendments ledger), `G15` (re-pin the immutable anchor), `G16`
(uninstrumented SHA into **paper I**, where the guard was blind until now). `G11`/`G13` still
caught. `3/3` and `2/2`, **0 UNGUARDED**. `-65` built a private mutation harness, got 7/7, and
**deleted it** — the estate's harness already does it better, and a second weaker one would have
been one more instrument silent about what it does not reach.

---

## THE TELL, now six deep

`-61`: a corpus under repair has a moving referent and only the filesystem knows. `-62`: the
line-wrap grep trap runs both ways. `-63`: a backlog drain measures the backlog, not the paper.
`-64`: **a review apparatus has the same defect as a manuscript — its own coverage is an unmeasured
claim, and the silence reads exactly like coverage.**

**`-65` ADDS TWO, and they are the same border crossed in opposite directions:**

**(i) THE FIX FOR `WT-092` HAS `WT-092`. Ask the question of your own repair, and answer it by
FIRING the repair, not by reading it.** My new emptiness limb compared `SEC_47_CURRENT` to the
anchor — but `SEC_47_CURRENT` is *derived from* `AMENDMENTS`, so deleting every amendment collapses
it onto the anchor and the test cheerfully reports a correctly-empty ledger **for a section that
moved**. It was measuring its own bookkeeping instead of the manuscript. The mutation pass caught
it; re-reading the code had not.

**(ii) A REVIEW IS AN INSTRUMENT, AND AN INSTRUMENT THAT READS PROSE CANNOT REPORT ON CODE.**
`REVIEW-005` reasoned about `redistribution.py` from the manuscript and got the mechanism wrong.
This is `-64`'s `REVIEW-004` finding — the referee who reimplemented §3's table *from the prose*
instead of running `wt030_report.py` — recurring one level up. **Before writing a review's
diagnosis into a manuscript, open the file the diagnosis is about.** Four minutes; it bought a
better sentence than either document proposed.

**And the census corollary (`WT-099`):** when a decision doc, card or handoff prices work as
*"N places"*, treat the number as a **hypothesis** and the file list as the real claim. **Write the
census as a script before writing the patch** — re-runnable afterwards as verification, and the only
thing that distinguishes *five sites* from *five sites somebody could see from where they stood*.

---

## THE SELF-REVIEW TRIAD, answered in writing (the gate requires it)
1. **Captured everything for a zero-memory future Opus?** Yes. Four `LEDGER` entries
   (`WT-096`–`WT-099`), seven committed scripts each carrying a docstring saying *why*, a
   `.bak-wt65-*` beside every touched file, the reasoning recorded on `DECISION-001` itself, two
   Asana cards, and discrete commits so any one is revertible alone.
2. **Learned the hard way and not yet written down?** Now written: the tooling deltas marked ▲
   above, and three lessons banked to `claude-blackbook` — the guard-with-no-remedy rule, the
   class-repair-with-a-constant-subject rule, and *a review's claim about the code is itself an
   unverified claim*. The `G-AL` grep correction was the last one outstanding and is in this file.
3. **The ONE thing that makes the next session's life easier, added THIS pass?**
   **The census-before-patch pattern** (`scripts/wt115_kappa_census.py`). `DECISION-001` priced
   option A as *"5 places"*; the census found **six**, and the sixth was in a test docstring where
   nothing could ever have failed. Four minutes, re-runnable afterwards as verification, and it
   generalises to every *"N places"* claim this project will make. Runner-up: the SHA instrument is
   a glob now, so manuscript five is covered on the day it lands.

---

## THE EIGHT-SESSION GATE RED IS **RESOLVED** — stop expecting it
**`GATE SELF-CHECK: PASS ✅`.** The `~/Scripts` `DIRTY(2)` pair — `braatz-crawl-check.py` and
`serve-braatz-archive.py` — that `-59`→`-64` each declined and each carried forward is **gone**. A
sibling session banked them: `~/Scripts` commit `48c9d9f`, *"braatz-archive: bank the preview server
and crawl checker from braatzArchive-01"*. Verified independently rather than inferred from the
green: `git status --short` in `~/Scripts` is empty and `git log @{u}..` is empty. Card
`1217526943288480` can be closed by whoever owns it.

**DELETE THE EXPECTATION, NOT JUST THE ROW.** Six handoffs running told the next session to expect
exactly one red and treat it as normal, and `-64` wrote the reason that matters: *a session that
EXPECTS a red gate will not notice a real one* — which is precisely how the pytest red survived four
days. **The gate is green now. If yours is not, that is news.**

`WT-095` is unchanged by any of this: **the gate does not run a test suite.** Run it yourself and
say the number. `-65` did: **1078 passed, 0 failed.**

---

## RULINGS NOW SETTLED — do not reopen
- **`DECISION-001` is ruled: A, with C deferred behind the literature search.** Do not re-litigate,
  do not write a second one-pager. If the search comes back clean, C is a *new* decision for Jason
  with the price finally known.
- **`REG-012` §4.7 is ruled** (`WT-096`). `SEC_47_AT_REGISTRATION` is **immutable**. A warranted
  §4.7 edit **appends an `Amendment`**.
- **DO NOT widen `ROTTED` by glob.** `test_pin001_code_state.py` asserts *"last commit touching"* is
  **absent** from paper III; **Paper IV §10 uses the same words correctly** — the per-file form
  `PIN-001` chose as the remedy. **The rot was never the phrase; it was the phrase with a directory
  after it.**
- **GREP `tests/` AND `scripts/` FOR ANY MANUSCRIPT STRING BEFORE YOU EDIT IT** (`WT-094`), and
  **census before you patch** (`WT-099`). Do not delete *"18 tests"* from Paper II's abstract.
- **DO NOT re-derive** the κ residuals (−6.78/−4.91/−4.35 %, a denominator convention, twice
  derived); `III-1`'s 4.2×; the `E2` blind pass (all 28 rows scored); the P2-at-three-strengths lead
  (withdrawn). **DO NOT re-serve `REVIEW-004` by section number** — match on verbatim quotes only,
  and §A3 is the section every re-serving pass skips.
- The **end-to-end pass is CLOSED** (T=2, A=0, the system fails, E1–E6 spent).

---

## TOOLING (▲ = new at `-65`)
- **RUN THE GATE AS:** `GATE_ROSTER_WHO=big-wealthTensor-NN nohup ~/Scripts/gate-selfcheck.sh >
  /tmp/gate.log 2>&1 &`, then **two** polls of ~170 s (cloud Bash caps at 2 min; the gate takes
  ~5 min). The verdict line is `GATE SELF-CHECK:` — grep for that, and for `CANNOT VERIFY`
  expecting `0`.
- **▲ DO NOT `grep -c "G-AL"` AS A PASS/FAIL TEST.** Earlier handoffs said *"zero `G-AL` lines is
  `G-AL` passing"*. It returns **1** on a perfectly green run, because the string sits in a help
  footer: *"Full gate: ~/Desktop/downloads/HANDOFF-GATE.md (G-A->G-AL)"*. A signal indistinguishable
  from boilerplate is not a signal — grep the verdict line.
- **`handoff_gate.py --emit` WILL REFUSE** on `gate_passed != true`, which has been the standing
  state since `-58`. **Do not set it true to make `--emit` print** — that is falsifying a gate
  result, the exact defect `WT-096` repaired. Run `--stamp`, commit, let `--emit` refuse, **read its
  `G-COACH-2/3` table** (`-65`: concessive openers **0** across all four papers; conduct narration
  1/1/5/2), and paste the handoff into chat yourself.
- **WRAP SEQUENCE:** `gh_sha: PENDING` → commit → `--stamp` → commit. `--emit` does not stamp.
- **EDITED A PAPER? REGENERATE THE BOARD BEFORE THE GATE:** `python3
  ~/Scripts/handoff-kit/board.py --criteria docs/done-criteria.tsv --project wealth-tensor --out
  docs/CHECKLIST.md --preamble docs/checklist-preamble.md --check` → *"matches measured reality
  (66 criteria)"*. `-65` edited Paper II and the 66 did not move — **no criterion tracks
  κ-as-mechanism**, which is its own small finding.
- **ANY ABSTRACT EDIT:** `python3 scripts/check_abstract_size.py <PATH> --print`. Takes a PATH.
  **▲ Measure the CANDIDATES in bulk** — `scripts/wt115_abstract_candidates.py` is the worked
  example: write each candidate into a copy of the real manuscript, run the committed instrument on
  it, print a table. Twelve candidates, one call, and it killed all twelve of round 1.
- **A BATCHED PATCH SCRIPT BEATS N EDITS.** `wt113_`, `wt114_`, `wt114b_`, `wt116_`, `wt116b_` are
  five more worked examples: `assert count(old) == 1` for **every** anchor before any write, `.bak`
  each file, `--dry` writing `*.wt65-dryrun`. **DRY-RUN AND `diff` IN THE CLOUD FIRST.**
- **▲ EXTEND ANCHORS TO PARAGRAPH BOUNDARIES IN WRAPPED PROSE, not sentence boundaries.** `-63`
  said sentence; `-65` obeyed that and still produced **two ragged lines**, because a replacement's
  last line collides with whatever survived on the same source line. For a re-wrapped paragraph the
  only safe anchor is **the whole paragraph**. Caught in the dry-run diff.
- **▲ `awk 'length>100'` COUNTS BYTES.** `κ`, `ρ`, `—`, `×` are multi-byte, so a 98-character line
  reports as 101+. Measure characters in Python and compare against the file's own `.bak`.
- **▲ A test file can be dry-run under the REAL suite** at `<repo>/.some-dir/x.py` — `parents[1]`
  still resolves to the repo and pytest skips dot-directories. `rm -rf` the scratch before
  `git add -A`.
- **▲ USE ABSOLUTE LOCAL PATHS IN EVERY `cat X | dx --put`.** The cloud Bash cwd does **not**
  reliably persist between calls; `-65` lost it twice. The second time the pipe hung five minutes on
  a missing file and wrote a **0-byte file** to darwin. The `.bak` taken first is what made it a
  non-event.
- **▲ `dx --put` into a missing directory FAILS** (`zsh: no such file or directory`). `mkdir -p`
  first.
- **▲ `grep -c` EXITS 1 ON A COUNT OF ZERO** — a correct zero. Assert the printed number, not `$?`.
- **NAME YOUR PATCH SCRIPT IN A FREE `wtNNN` TAG.** Tags now run to `wt116b`; **`wt117` is free.**
- **`dx` chokes on multiline / apostrophe-bearing command strings.** Write locally, `--put`, run
  there. `COMMITMSG.txt` → `--put` → `git commit -F`.
- **`lessons.py use` / `record-outcome` can hang past 4 min** — one per `dx` call at 300 s, never
  chained with `&&`; two `use` calls separated by `;` are fine. `add` is fast and auto-pushes.
- **Asana `create_tasks` silently drops `projects`** — `update_tasks` with `add_projects`, then
  verify with `get_task opt_fields=name,projects.name`. Held again this session.

---

## A PROCESS MISS OF MINE
**I never ran `lessons.py search` at student-in.** I followed the `dx` and batched-patch rules
because *this handoff restates them*, not because I read the leaves. **A handoff good enough to
inline the lessons removes the reason to open the tree** — and the tree holds the leaves this
project has *not* inlined. Next session: run
`lessons.py search "<the at-bat>" --scope global,wealth-tensor` **before** finishing this file, and
record what it returned that this file did not.

---

## JASON-SIZED, not yours to decide
- **(a) `DECISION-001` — DONE.** Ticked A on 2026-08-17. The next Jason-sized moment on this axis
  arrives only *after* the literature search, and it is a different question: *given what the search
  found, is C worth it?*
- **(b) Paper IV's title and abstract leading clause** still read *"from the household to the
  sovereign"*. Narrow it, or ratify the appended demotion as sufficient. **Now the oldest open
  Jason item.**
- **(c) `P7` is still ONE BOOLEAN** for a criterion that is per-paper with a two-pass counter. The
  board cannot distinguish *"no paper has ever been read"* from *"every paper has had exactly one
  independent read and found between two and nine defects"*. Adding rows moves the 66, so it wants
  its own at-bat.

## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` and **say the number**; `roster leave
--who` once; and paste a handoff better than this one into the chat as the **last act**.
