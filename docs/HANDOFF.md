---
project: wealth-tensor
gh_sha: 3f8e9843e242c309e275ebfe82713cd2cf18a507
updated: 2026-08-13
session: wealthTensor-25
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. §7's student-in, then §5's at-bat. **§6 first if you are about to run the gate.**

> **`-25` in one line: `SOURCE-001`'s last cheap step is done, and the document's one recurring
> mistake showed up for the third session running — a number that was right, under a quantifier
> that was wrong.** §1. `-23` said a route was closed and it was open; `-24` said a branch was
> property-only and it was not; `-25` says **"flat across a decade" was flat across one quarter.**
> Three sessions, three quantifiers, same document. You will meet the fourth. When you read a
> coverage number in this repo, the question is not *is it right* — they have all been right —
> it is **what is it a number ABOUT.**

## 0 · TRANSPORT — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -25 without exception** (`-25`'s attestation was posted seven
seconds after the request was minted; the five-minute window has never once been the binding
constraint). Roster join/claim as `big-wealthTensor-26` — **`roster claim` takes `--resource`, not
`--repo`**, which cost `-25` one round trip. `export LESSONS_CONTRIBUTOR=opus`.
**`export GATE_ROSTER_WHO=<you>` at the TOP of the session**, not at the gate — §6.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy. In a
cloud container there is no pytest at all until `pip install pytest --break-system-packages`.

**NEVER inline a multi-line string in a `dx '...'` argument — AND A HEREDOC IS NOT AN ESCAPE.**
Write locally → `dx --put /tmp/msg.txt` → `git commit -F /tmp/msg.txt`. The same trick carries
whole scripts: write it in the container, `--put` it, `bash` it. `-25` moved five files and three
commit messages that way and `shasum`-compared every one; zero corruption.

**Stage by PATH. Never `git add -A` on darwin** — one shared tree, and `-25` worked alongside
**seven** sibling claimants on this repo. Four commits, each staged by name, each clean.

**`data.sec.gov` and bulk SEC downloads: CLOUD, NOT DARWIN.** `-24` got darwin IP-flagged. `-25`
pulled **ten FSN notes zips, 5.0 GB**, from the container in under four minutes with no throttling
at all. The container had 30 GB free and finished at 41 % used. This is now twice; treat it as
settled.

## THE TEN THINGS THAT HAVE EACH COST A SESSION A RUN

1–8 unchanged (registered machinery: `onset_rule="peak"`; `peak_onset` returns a tuple; control arm
in the same pass; the panel is registered machinery — REG-008 F6 asserts the no-rebuild in code;
`git log -S` recovers a dangling ordinal and dates a number; **a feasibility probe that reads the
arm label is the experiment, whatever the file is named**; **taking "the latest X" and "the latest
Y" independently is comparing two periods** — the `IMPOSSIBLE = 1.05` guard that earned its keep
seven times on the full panel).

9. **A MEASUREMENT THAT CANNOT REPRESENT THE ANSWER IS NOT EVIDENCE OF ABSENCE.** `-24`'s, twice in
   one session: `companyconcept` 404s on every duration-typed fact, and an 80-firm sample drew zero
   intangibles-dominant firms. Ask of any zero: *could this instrument, or this sample size, have
   produced a non-zero?*

10. **NEW · AND ASK IT OF EVERY NON-ZERO TOO — a rate is a claim about whatever the instrument
    could reach.** `-25`'s, and the generalisation of 9 rather than a new animal. Two forms, both
    live this session:
    - **The window form, caught in flight.** Four quarters of filings said only **0.718** of
      September fiscal-year-ends had a locatable 10-K. A September 30 year end is due about
      December 29; the late half of that season lands in the *next* year's Q1. Two edge quarters
      moved September to 0.923, August and October to 1.000, and the interior not at all.
      **A coverage rate that is low only at the ENDS of the window is measuring the window.**
      The profile is the tell and it is visible in the results table alone.
    - **The slice form, which is `-23`'s and `-24`'s error wearing its third costume.** §3a's
      *"coverage is flat across a decade"* was measured on Q1 zips — which by filing-deadline
      arithmetic contain only December and January year-ends. It is flat there. The series that
      moved is the one it could not see. §1.

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace.
**Manuscript:** `patchkit.apply_edits`, never `sed`. Back the file up first.
**The gh_sha dance is NOT a defect — do not "fix" it.** `--stamp`, then a commit whose whole content
is the stamp, so `gh_sha` trails HEAD by exactly that commit. `--check` calls that
`ADVISORY: docs-only drift` and **exits 0**. Read the exit code.

## 1 · WHAT HAPPENED — the δ half's last gate is discharged, and it discharged in two directions

`4c7d4d3` (SOURCE-001 §3b + the coverage guard). **Manuscript untouched** — paper III is
byte-identical. **590 tests, ~40 s** (was 581).

**`SOURCE-001` §3b — the fiscal-calendar caveat, run.** §3a measured 0.82 on Q1 notes zips only and
said so in its own limitations. A Q1 zip can only contain filers whose year ended the preceding
October–January; **40.8 % of this panel's 9,782 firm-years end in another month**, and ~31 % in a
month a Q1 zip cannot reach at all. Probe: `scripts/source001_lifetime_by_fyend.py`, **six** FSN
notes quarters per cycle so every fiscal-year-end month has its whole filing season inside the
instrument, unit of analysis the **firm-year**, and coverage decomposed — *no 10-K located* is
reported separately from *located, no life tagged*, because only the second is about tagging.

| | 2014-10-31 … 2015-09-30 | 2022-10-31 … 2023-09-30 |
|---|---|---|
| panel firm-years in window | 847 | 837 |
| 10-K located | 0.949 | 0.981 |
| canonical life, **December** | **0.758** (n=505) | **0.824** (n=540) |
| canonical life, **every other month** | **0.681** (n=342) | **0.822** (n=297) |
| December − other | **+0.077, z = +2.47** | **+0.003, z = +0.09** |
| all firm-years | 0.727 | 0.823 |

1. **Recent years: closed.** No December advantage this measurement can tell from zero. The δ design
   may use 0.82 on any fiscal calendar there.
2. **Early years: closed the other way.** The 2014–15 cycle is 0.727, and the decade's movement is
   carried by **non-December** firm-years (+0.140, z = 4.07) against December's +0.066. A design
   inheriting 0.82 across 2013–2025 **overstates early non-December coverage by ~14 points.**

So REG-009's lifetime half now owes a **year-window decision** in its first section — restrict to the
recent span where coverage is uniform, or carry the whole span with a per-year weight and say why —
and that decision has a measured price on it, which is the only thing `SOURCE-001` exists to produce.

**`tests/test_source001_coverage.py` — nine tests, and the hole they close was total.** `SOURCE-001`
is not a registration, so nothing was watching its tables; by `-25` they are what REG-009's design is
argued from. Two directions per figure: the artifact is recomputable from its own per-record rows,
and the document matches the artifact. It also gives `data/source-001-concentration-full.json` its
**first reader** — `-24` committed it precisely so the 99-of-1,444 count would be auditable without
6,400 SEC calls, and nothing ever audited it, which is `-24`'s own banked lesson about undo rows
(count the writers, count the readers, distrust a ratio with a zero in it). Recomputed from the
per-firm records, **§4b's whole table reproduces exactly** — all four thresholds, all three classes.
Mutation drill: flipping ONE December record's `canon` flag reddens two tests; sha256 restore verified.

**BUG SPRAY, outside this repo — `aar.py sweep`, State Machine `1217468400555940`, now CLOSED.**
The card measured a symptom (one AAR laundering ±3 days of unrelated near-misses). The cause is one
regex and it is worse than the card guessed: `AAR_LINK_RE` requires a literal `AAR:` and every lesson
in the corpus writes `source: AAR <slug>` without the colon — the exact shape the function's own
docstring claimed it matched. **The declaration branch had never once fired**: 7 of 7 swept lessons
resolved through the date window, one of them attributed to a *different* AAR while its own source
named the right one. **A declaration path that cannot match is a fallback path that carries
everything, and from outside it is indistinguishable from a healthy gate, because every line still
prints the reassuring words.** Fixed in `claude-blackbook` `dd51cefe`, gate doc **v2.51** (canonical
`04878cd` in `darwin-everything-meta`, mirrored `bbeec94b`). New `aar.py adopt`; window matches are
labelled and, from `SWEEP_DECLARATION_SINCE = 2026-08-13`, provisional rather than passing — with the
same amnesty argument `SWEEP_BASELINE` makes, so it was non-breaking on a tree with seven live
siblings. Two new selftest assertions for the branch that had none.

## 2 · RULINGS — DO NOT REOPEN

- Prior rulings stand: no third disclosure instrument on this corpus; the two dead (f) keywords stay
  in `INTERNAL`; phrase set frozen at 38; retail PP&E × intangible cells out of §5.4; §4.4 settled;
  References block; §4.5's 400-vs-4,000 not a defect. `SOURCE-001` is **not** a registration.
- `-24`'s reversals stand: a dominant-asset σ design is **not** automatically a property design, and
  the machine-readable route to useful lives is **open**.
- **NEW · §3a's "flat across a decade" is NARROWED, not reversed.** It is true of Q1 filers and false
  of the panel. The banked lesson carries the annotation; do not cite the bare clause.
- **NEW · The δ/σ asymmetry is now fully priced.** δ has a source *and* a known coverage surface
  across the panel's span; σ has neither. Every cheap step named in `SOURCE-001` §6 is run. **The
  next move on that document is σ, or it is REG-009's first section.**

## 3 · NEW MACHINERY

`scripts/source001_lifetime_by_fyend.py` (six-quarter cycles, firm-year unit, decomposed coverage;
`THIN` refuses any month bucket under 30 firm-years, and every between-bucket gap prints a
two-proportion **z** — which is what demotes 0.824-vs-0.822 to nothing and promotes the cross-cycle
move to a result; `--compare` takes a prior cycle's JSON) ·
`data/source-001-lifetime-by-fyend{,-2015}.json` (per-firm-year records, 837 + 847) ·
`tests/test_source001_coverage.py` (9). 590 tests.
Outside the repo: `aar.py adopt`, `aar.py` declaration reader + provisional coverage, gate v2.51.

## 4 · THE AT-BAT, RANKED

1. **σ. It is now the only cheap step left on `SOURCE-001`, and both arms are unassessed.**
   §6 step 3: equity-return volatility for the **47 PP&E-dominant firms** at the 0.70 threshold —
   still the right *first* probe under §2. And the **34 intangibles-dominant firms** still have
   nobody arguing whether they pass §2. `-24`'s read, which I did not test and am passing on
   unchanged: they sit closer to the goodwill objection than to the vessel case, because recognised
   intangibles are mostly acquisition residue one step removed from goodwill. **That is an argument
   to make. §4b's whole lesson is that absence is not one.**
2. **REG-009 §1 can be drafted now, and it has exactly three decisions in it.** (a) the δ/σ split —
   δ is sourced and does not depend on §5's selection problem at all; (b) if δ, the **year-window**
   decision §3b just priced; (c) if σ, §5's choose-your-shape (estimate the exponent on the
   observable region and scope it honestly, versus make the truncation the instrument and test the
   sign). Nothing more needs measuring before that document can be written.
3. **Fill in the coverage series between the two cycles**, *only if* (b) chooses the whole span.
   Six FSN zips per cycle, ~90 s of compute each, **from the cloud**. Two points cannot tell a step
   from a ramp, and a per-year weight wants the shape. Mechanical; `--compare` already does the
   arithmetic.
4. **The gate defect card** — State Machine `1217465036940491`. Still open, still a good warm-up.
5. **AAR actions A1/A2** — the `pre-commit` roster brake (`1217468064910605`) and an audit of the
   other four `post-*` hooks in `darwin-mac-ops/hooks`. Untouched for three sessions running; each
   of us has shared the tree with a crowd and got lucky. Luck is not a control.
6. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
7. **Widen the reach guard to REG-001/002/006's non-ledger restatements.** The mechanism and the
   precision rule exist; third layer, mechanical.
8. Cready et al. (2012) full text, if prior art is reopened.

## 5 · WHAT I WOULD DO DIFFERENTLY

**I built the window before I asked what the window could contain, and then I nearly published the
consequence.** The four-quarter run's September row (0.718 located) is a perfectly well-formed
number that would have gone into the table as delinquency. What saved it was not care at the writing
stage — it was that the *shape* was wrong: low at both ends, flat in the middle. Ten minutes and two
more zips. **The general version, and it is cheap enough to be automatic: before reading a rate off a
bounded window, name the LAG between the event and its record, and confirm the window exceeds the
event set by that lag at BOTH ends.** For SEC filings that lag is 60–90 days with a p99 near 220 and
a measured max of 453.

Second, smaller: I changed `_covered_by_existing_aar`'s return type from `str` to `tuple` and two
`selftest` call sites went with it. Both failed **loudly** and immediately, which is the system
working — but `if f(...)` on a function that now returns `("", "")` is truthy, and that one only
failed loudly by luck of it being an assertion. Grep the callers before widening a return type;
`grep -n` cost five seconds and I did it *after*.

## 6 · THE GATE

See the frontmatter for the verdict; **believe `--emit`'s exit code over this field.** Run
`export GATE_ROSTER_WHO=big-wealthTensor-26` **before** `~/Scripts/gate-selfcheck.sh` — without it
the script cannot tell a sibling's dirt in `~/Scripts` from yours, and with a crowd this size that is
the difference between a named warning and a false blocker. This is documented nowhere else.

**New, and it will bite someone: `HANDOFF-GATE.md` in `claude-blackbook` is a MIRROR.** The canonical
copy is `~/Desktop/downloads/HANDOFF-GATE.md` (repo `darwin-everything-meta`); edit there and run
`~/Scripts/mirror-handoff-gate.sh`, which syncs *and pushes* claude-blackbook by itself. Editing the
blackbook copy directly is the COPIED-not-DERIVED trap this estate has ten lessons about. The mirror
script stages only that one file — verified, on a tree with seven other claimants.

## 7 · STUDENT-IN

`lessons.py doctrine`, then `search "<task>" --scope global,wealth-tensor`. `-25` banked three,
curated one (`-23`'s XBRL leaf, whose "flat from 2015 to 2023" clause is now annotated with its
scope), and corroborated `-24`'s dominant-asset leaf — which **graduated `quarantine` → `active`** on
its second pass. That is the corroboration loop finally paying out; do it, it takes one command.

The new ones worth knowing before you start: **a declaration path that cannot match is a fallback
path that carries everything** (and the tell is a COUNT — instrument both branches of a two-tier
decision and look at the split; a primary at 0 % and a fallback at 100 % is a dead branch whatever
the code looks like) · **a coverage rate that is low only at the ends of the window is measuring the
window** · **a coverage number measured on one slice is flat only on that slice.**
