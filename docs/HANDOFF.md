---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-17
session: wealthTensor-65
gate_passed: false
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF

**ORIENT: read `docs/CO-AUTHOR-CHARTER.md` first. THE CHARTER WINS over anything in this file.**

## `-65` IN ONE LINE
**THE SUITE IS GREEN. 1078 passed, 0 failed — I ran it, that is the number.** `-64` handed off
`1073 passed, 1 failed`; the red is repaired and three limbs were added on the way. Both apparatus
at-bats are closed: the `REG-012` §4.7 freeze (`3ffb3f1`, `WT-096`) and `PIN-001`'s class hole
(`ba95302`, `WT-097`). **No manuscript was touched this session** — zero paper edits, so the board
is unmoved at 52/66 and needed no regeneration (checked anyway: *"matches measured reality (66
criteria)"*).

**`DECISION-001` IS STILL ALL FOUR `☐`.** Checked first, before anything else, per `-64`'s
instruction. `grep -c "☑"` → 0; file unchanged since Aug 16 19:02 local. Do not write a second
one-pager and do not re-litigate it.

---

## READ FIRST, in this order
1. **`docs/LEDGER.md` `WT-096` and `WT-097`** — this session's two rulings, both with the evidence.
2. **`docs/REVIEW-007-P7-pass-3.md` §9** — still the frame. `-65` is `WT-092` three more times.
3. **`DECISION-001-A2-and-road-one.md`** — unticked, still the biggest single unblock.
4. `REVIEW-006` §7 and `REVIEW-005` §3 remain worth the ten minutes.

---

## WHAT `-65` DID, so you do not re-derive it

### 1 · THE `REG-012` §4.7 RED — ruled, repaired, falsified (`3ffb3f1`, `WT-096`)

**Ruling: NOT a violation.** Reading (b). §6 forbids edits arising from `REG-012`'s **own**
outcome, and its branches R/F/N are about the band count's edge phase; no path runs from any of
them to a sentence about whether indefinite-lived intangibles disclose a useful life. `-63`'s
`6314302` edit is licensed by **ASC 350-30-35-15** and **narrows** the paper's claim (*"For three
of the four classes"* → *"two"*), which is the opposite of the self-flattery §6 exists to stop.

**Verified, not inherited.** `scripts/wt113_sec47_history.py` walks every commit that touched
paper-III since `ba59370` and prints §4.7's digest at each: **byte-identical across eight commits,
moved at exactly one.** The card's history claim was right and had never been checked. A claim
about history is checkable — check it.

**The defect was never the freeze.** `-43` wrote `SEC_47_SHA256` as ONE constant serving two
incompatible roles and a red message prescribing *"re-pin in the SAME commit as the edit"* — which
`test_the_pinned_digest_is_the_version_REG_012_saw` forbids, since it nails that constant to
`ba59370`. **No value passes both. The prescribed remedy was executable exactly zero times**, so
the first warranted edit wedged the guard red permanently.

**The repair:** `SEC_47_AT_REGISTRATION` (immutable, a fact about `ba59370`) + `SEC_47_CURRENT`
(derived from an append-only `AMENDMENTS` ledger). Each amendment carries commit + licence +
resulting digest and **is checked against git** for having actually moved §4.7 to the digest it
claims. A licence naming `REG-012`'s own outcome is refused: that is reading (a) coming through the
door the ledger opened.

**Timing clause ruled:** *"a pin moved in a later commit is a pin nobody reviewed"* wants the
**review**, not the SHA. Naming the licensing commit, the standard and the resulting digest
reconstructs what a same-commit re-pin would have shown. It must be ruled this way, or a guard
whose remedy is impossible could never be repaired at all.

**Also repaired, same commit:** `CONSTRAINT-INVENTORY-001`'s C48 row asserted *"§4.7 is unchanged
since `REG-012` — compliant"*. False since `6314302`, and prose, so it could not go red.

### 2 · `PIN-001`'s CLASS HOLE — closed (`ba95302`, `WT-097`)

**Part 1 first, as the card required, and the ordering was MEASURED.** The widened instrument was
run from a scratch path **against the un-instrumented registry, before anything was edited**. It
went red naming exactly `['paper-IV.md 5efe626']`, and green the moment `LATEST_TOUCH` learned
`scripts/reg013_citation_whitespace.py` → `5efe626`. A red that arrives on schedule is evidence; a
red nobody provoked is a guess.

**Part 2 · the glob.** `PAPERS = sorted((ROOT / "docs/papers").glob("*/paper-*.md"))`. A fifth
manuscript is covered the day its file lands. `*.bak-*` siblings do not end in `.md`.

**And the glob is asserted too** — `test_the_glob_still_finds_every_manuscript`, floor of four.
Widening a constant into a discovery trades one failure mode for another: `-49`'s rule is that an
absence predicate passes vacuously on a missing file, and **a glob matching nothing passes every
downstream assertion vacuously**.

**`LATEST_TOUCH`'s own comment** said the mapping was *"as of this edit"* — `PIN-001`'s edit,
2026-08-11 — after gaining Paper II's module (`-64`) and Paper IV's (here). Repaired.

### 3 · THREE NEW MUTATION PROBES, because a guard nobody fired is the defect being repaired

Added to `scripts/mutation_control.py` — **not** to a private harness. `-65` built one, got 7/7,
and **deleted it**: the estate's harness already does this better (whole suite per probe, catcher
lists, `{"git": True}`), and shipping a second weaker one would have been one more instrument
silent about what it does not reach.

```
G14  launder reading (a) into the AMENDMENTS ledger as a licence   3 catchers
G15  re-pin SEC_47_AT_REGISTRATION, declared immutable             1 catcher
G16  uninstrumented SHA into PAPER I — where the guard was blind    2 catchers
G13, G11 (pre-existing)                                            still caught
```
`3/3` and `2/2`, **0 UNGUARDED** both runs. `G16` exists because `G11` is caught before *and*
after the widening and therefore proves nothing about it; paper I was chosen because it pins
nothing today, so a catcher there cannot be another guard's accident.

---

## THE TELL, now five deep

`-61`: a corpus under repair has a moving referent and only the filesystem knows. `-62`: the
line-wrap grep trap runs both ways. `-63`: a backlog drain measures the backlog, not the paper.
`-64`: **a review apparatus has the same defect as a manuscript — its own coverage is an unmeasured
claim, and the silence reads exactly like coverage.**

**`-65` ADDS: THE FIX FOR `WT-092` HAS `WT-092`. Ask the question of your own repair, before you
ship it, by FIRING IT — not by reading it.** Three instruments this session claimed a class and
touched an instance, and the third was mine:

- the `REG-012` freeze — one constant for two roles, remedy impossible;
- `PIN-001`'s SHA guard — one paper of four, under a docstring saying **CLASS**;
- **my own new emptiness limb** — it compared `SEC_47_CURRENT` to the anchor, but `SEC_47_CURRENT`
  is *derived from* `AMENDMENTS`, so deleting every amendment collapses it back onto the anchor,
  the two constants agree, and a test named *"an amendment is declared exactly when §4.7 has
  moved"* reports a correctly-empty ledger **for a section that moved**. It was measuring its own
  bookkeeping instead of the manuscript. Caught by the mutation pass, not by re-reading the code —
  which is the whole point. **Fifth instance of `-63`'s corollary that a repair can introduce a
  defect, and the first where the introduced defect was the same class as the one being repaired.**

`LEDGER WT-096`. Free corollary, unchanged and still cheap: end every pass by asking which
instrument would have caught each finding, and whether it exists for the other three papers.

---

## YOUR AT-BAT — take one, in this order

1. **PAPER II's SECOND INDEPENDENT READ** — now the highest-value item, because the two apparatus
   at-bats that were blocking it are closed and the corpus is green. A fresh end-to-end pass of a
   manuscript that moved in 14 places yesterday; **diff against `paper-II.md.bak-wt64-p7`, do not
   read the repaired text as given.** This is the pass that could start a convergence count.
2. **THE ABSTRACT COMPRESSION PASS**, still teed up from `REVIEW-005` §7: III 247/250, IV 248,
   II 249 (**unchanged** — `-64`'s repair was deliberately word-neutral to leave the slack for
   `DECISION-001`; two of its four candidates measured 250 and would have spent it).
3. **P6's remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).
4. **Paper II's companion reference entries** — card `1217542940968749`, `REFERENCE-POLICY`
   jurisdiction.
5. **Paper I's second independent read** — the only manuscript with no `P7` pass at all. It pins
   nothing and is the quietest file in the corpus, which after this session is a reason to look,
   not a reason to relax.

**FORCING LINE (`-59`'s ruling, kept): take none of the five, say why in ONE LINE at the top of
your handoff. It costs nothing.**

---

## KNOWN, DIAGNOSED, PERMANENT — do not re-derive, do not commit
The gate **FAILs** on `~/Scripts` `DIRTY(2)`, `braatz-crawl-check.py` and
`serve-braatz-archive.py` — **ninth** session running. Card `1217526943288480`. `-59`→`-65` all
declined. Jason's gate rule: **`CANNOT VERIFY == 0`, exactly ONE issue, that one.** Measured this
session: `grep -c "CANNOT VERIFY"` → **0**, `grep -c "G-AL"` → **0** (silent on success), one
issue, that one.

**AND THE WARNING THAT EARNED ITSELF:** *a session that EXPECTS a red gate will not notice a real
one* — which is exactly how the pytest red got here. `WT-095` still stands: **the gate does not run
a test suite**, so run it yourself and say the number in the handoff. `-64` did. `-65` did:
**1078 passed, 0 failed.**

---

## RULINGS THAT ARE NOW SETTLED — do not reopen
- **`REG-012` §4.7 is ruled** (`WT-096`). `SEC_47_AT_REGISTRATION` is **immutable**; a red there
  means the extractor changed meaning or history was rewritten, never a re-pin. A warranted §4.7
  edit **appends an `Amendment`**, in the same commit where possible, naming the licensing commit
  where not.
- **DO NOT widen `ROTTED` by glob** the way the SHA instrument was widened.
  `test_pin001_code_state.py` asserts *"last commit touching"* is **absent** from paper III because
  there it was the rotted whole-directory claim; **Paper IV §10 uses the same words correctly** —
  *"the last commit touching `scripts/reg013_citation_whitespace.py`"* — which is the per-file form
  `PIN-001` chose as **the remedy**. Glob it and you go red on a correct pin. **The rot was never
  the phrase; it was the phrase with a directory after it.** Written into the instrument's own
  docstring, where the session reaching for the glob will be standing.
- **DO NOT re-derive the κ residuals** (−6.78/−4.91/−4.35 %, monotone, therefore a denominator
  convention — twice-derived independently).
- **DO NOT re-serve `REVIEW-004` by section number** — its § numbers are from an earlier draft.
  **Match on verbatim quotes only.** §A3 is the section every re-serving pass skips, because Part A
  reads as the big three and A3 reads as the leftovers; it holds three real items and one is still
  open.
- **DO NOT** re-derive `III-1`'s 4.2× (`REVIEW-006` §1), propose a `REG-013` re-run to "fix" the
  seeds (§6 forbids it; `WT-090`), re-mine the `E2` blind pass (all 28 rows scored), or re-derive
  the P2-at-three-strengths lead (withdrawn, `REVIEW-005` §3).
- The **end-to-end pass is CLOSED** (T=2, A=0, the system fails, E1–E6 spent). Settled.

---

## TOOLING, measured at `-65` (deltas from `-64` marked ▲)
- **RUN THE GATE AS:** `GATE_ROSTER_WHO=big-wealthTensor-NN nohup ~/Scripts/gate-selfcheck.sh >
  /tmp/gate.log 2>&1 &` then poll with sleeps (~170 s each; cloud Bash caps at 2 min). **It needs
  two polls, not one** — `-65` measured ~5 minutes wall clock. `G-AL` and `G-AL#board` are silent
  on success; grep `CANNOT VERIFY` and expect `0`.
- **▲ `grep -c` exits 1 when the count is 0**, and that is a *correct* zero, not a failure. Assert
  the printed number, not `$?`, on any `grep -c` used as a measurement. (Sibling of `-64`'s
  `| tail` masking rule and `-62`'s `grep -oc` trap.)
- **▲ `dx --put` into a directory that does not exist FAILS** (`zsh: no such file or directory`,
  exit 1). `mkdir -p` on darwin first — the same trap the cloud side has for `--get`.
- **▲ The cloud Bash cwd does NOT reliably persist between calls.** `-65` lost it mid-session; a
  `cat relative-path | dx --put` then hung five minutes on an empty pipe and wrote a **0-byte
  file** to darwin. **Use absolute local paths in every `dx --put` pipeline.** The `.bak` taken
  first is what made that a non-event.
- **THIS REPO HAS ITS OWN WRAP SEQUENCE** (`scripts/handoff_gate.py` docstring): edit
  `docs/HANDOFF.md` with `gh_sha: PENDING` → commit → `--stamp` → commit → `--emit`. `--emit` does
  **not** stamp and refuses `PENDING`. It also runs `G-COACH-2/3` against all four papers.
- **▲ `--emit` WILL REFUSE, and that is the standing state, not your bug.** `handoff_gate.py:343`
  refuses on `gate_passed != true`, and `gate_passed` has been `false` since `-58` because the gate
  FAILs on the known `~/Scripts` pair. **Do not set it `true` to make `--emit` print** — that is
  falsifying a gate result, which is the exact class of defect `WT-096` spent this session
  repairing, and `G-COACH` would be the only thing left watching. Run `--stamp`, commit, let
  `--emit` refuse, read its `G-COACH-2/3` table for regressions (`-65`: concessive openers **0**
  across all four; conduct narration 1/1/5/2, unchanged), and **paste the handoff into the chat
  yourself** — which is what `-59`→`-65` each did.
- **IF YOU EDIT ANY PAPER, REGENERATE THE BOARD BEFORE THE GATE:**
  `python3 ~/Scripts/handoff-kit/board.py --criteria docs/done-criteria.tsv --project wealth-tensor
  --out docs/CHECKLIST.md --preamble docs/checklist-preamble.md --check` (rc=0 prints *"matches
  measured reality (66 criteria)"*). `-65` edited no paper and ran `--check` anyway; it is cheap.
- **ANY EDIT TO ANY ABSTRACT:** `python3 scripts/check_abstract_size.py <PATH> --print`. Takes a
  PATH, not a slug. Never hand-count. Use it to measure **candidate** rewrites.
- **A BATCHED PATCH SCRIPT BEATS N EDITS.** `scripts/wt113_edits_wt65_reg012.py`,
  `wt114_edits_wt65_pin001class.py`, `wt114b_probe_g16.py` are three more worked examples: one
  list of `(path, label, old, new)`, `assert count(old) == 1` for **every** anchor before any
  write, `.bak` every touched file, `--dry` writing `*.wt65-dryrun` siblings. **Dry-run and `diff`
  first** — it caught a PEP8 blank-line defect before anything landed.
- **▲ A test file can be dry-run under the REAL suite** by putting it at `<repo>/.some-dir/x.py`:
  `ROOT = parents[1]` still resolves to the repo, and a dot-directory is skipped by pytest
  collection. That is how the widened instrument was proven red-then-green without touching
  `tests/`. **`rm -rf` the scratch dir before `git add -A`.**
- **▲ `awk 'length>100'` counts BYTES, not characters** — `§` and `—` are multi-byte, so a
  99-character line can report 103. Measure with Python (`max(len(l) for l in ...)`) when it
  matters, and compare against the file's own `.bak` baseline rather than to zero.
- **NAME YOUR PATCH SCRIPT IN A FREE `wtNNN` TAG.** `-64` collided at `wt093`; tags now run to
  `wt114b`, so **`wt115` is free**.
- **`dx` chokes on multiline / apostrophe-bearing command strings.** Write locally, `dx --put`,
  run there. Corroborated again this session (`pass#3`, ACTIVE).
- **`COMMITMSG.txt` → `dx --put` → `git commit -F`.** Never inline a multi-line message.
- **`lessons.py use` / `record-outcome` can hang past 4 minutes.** One per `dx` call, 300 s
  timeout; two `use` calls separated by `;` in one call worked fine. `add` is fast (~10 s) and
  auto-commits and pushes.
- **Asana `create_tasks` silently drops `projects`** — `update_tasks` with `add_projects`, then
  verify with `get_task opt_fields=name,projects.name`.
- **`roster claim` needs `--who` AND `--resource`. `lessons.py use <id> --task <tag>` — id
  positional.**

---

## A PROCESS MISS OF MINE, SO THE NEXT SESSION DOES NOT REPEAT IT
**I never ran `lessons.py search` at student-in.** I followed the `dx` multiline rule and the
batched-patch convention because **this handoff restates them**, not because I read the leaves —
and then corroborated them at wrap, which is corroboration of a practice I got from the wrapper
rather than from the tree. That is a quiet failure mode worth naming: **a handoff good enough to
inline the lessons removes the reason to open the lesson tree**, and the tree is where the leaves
that this project has *not* inlined are sitting. Next session: run
`lessons.py search "<the at-bat>" --scope global,wealth-tensor` **before** reading the rest of
this file, and record what it returned that this handoff did not.

---

## JASON-SIZED, already surfaced, not yours to decide
- **(a) `DECISION-001`, A/B/C, still unticked.** `II-2` and `II-3` are two of whichever option's
  edits; do not repair them separately. **Six sessions have now waited on this**, and it is the
  single largest unblock on the board.
- **(b) Paper IV's title and abstract leading clause** still read *"from the household to the
  sovereign"*. Narrow it, or ratify the appended demotion as sufficient.
- **(c) `P7` is still ONE BOOLEAN** for a criterion that is per-paper with a two-pass counter. The
  board cannot distinguish *"no paper has ever been read"* from *"every paper has had exactly one
  independent read and found between two and nine defects"* — which is the true state today.
  Adding rows moves the 66, so it wants its own at-bat.

## AT WRAP
`~/Scripts/charter-read.sh wealthTensor-NN` **immediately** before the gate; the gate detached
**with `GATE_ROSTER_WHO` set**; `python3 -m pytest tests/ -q` and **say the number**; `roster
leave --who` once; and paste a handoff better than this one into the chat as the **last act**.
