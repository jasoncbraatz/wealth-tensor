---
project: wealth-tensor
gh_sha: PENDING_STAMP
updated: 2026-08-13
session: wealthTensor-27
gate_passed: false
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. **`docs/preregistration/REG-009-p3-lifetime-sourced-delta.md`** — new, and it is the thread now.
   §1 chose the arm; §3 is the definition of done; §4 is a pre-committed refusal.
4. §7's student-in, then §4's at-bat. **§6 first if you are about to run the gate.**

> **`-27` in one line: the arm is δ, and the reason is not sample size — it is that σ's outstanding
> measurement is a PURCHASE ORDER and δ's is an AFTERNOON.** `SOURCE-001` is closed and stayed
> closed; no probe was run in it. The fifth wrong quantifier was found where the handoff said to
> look — in a design sentence — but the shape moved again. `-23`→`-25` mis-scoped a **number**.
> `-26`'s two were **adjectives promoted past their measurement**. **`-27`'s were adjectives the
> paper itself flagged as load-bearing, in its own voice, and nobody ever built.** Paper III §4.7
> names its weak joint in the sharpest words available and then closes it with three bounds —
> `sticky`, `industry-median`, `industry convention` — **each occurring exactly once in the
> repository, in the sentence that declares it.** The honest naming of an objection was mistaken,
> by everything downstream, for the answering of it. **You will meet the sixth. The tell that has
> now worked twice is a one-minute grep; run it before you trust any sentence that licenses a run.**

## 0 · TRANSPORT — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -27 without exception**. Roster join/claim as
`big-wealthTensor-28` — **`roster claim` takes `--resource`, not `--repo`**.
`export LESSONS_CONTRIBUTOR=opus`. **`export GATE_ROSTER_WHO=<you>` at the TOP**, not at the gate — §6.

**`~/Scripts/bridge-status.sh` no longer errors on line 64** — that was `-27`'s first bug spray and
it had been printing `[: 0\n0: integer expression expected` on every clean run. Details in §3.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy.
**652 tests, ~40 s** (was 640).

**NEVER inline a multi-line string in a `dx '...'` argument — AND A HEREDOC IS NOT AN ESCAPE.**
Write locally → `dx --put` → run it / `git commit -F`. `-27` moved three repo files, two commit
messages, two patch scripts and a lessons-banking script that way, `shasum`-comparing every one;
zero corruption, seven for seven. **Patch scripts beat `sed` for anything structural.** `-27`'s
two-file patch added one refinement worth keeping: **verify EVERY anchor before writing ANY file** —
a partial application across two files is worse than a clean refusal.

**Stage by PATH. Never `git add -A` on darwin** — `-27` shared the tree with **eight** claimants and
the roster brake fired on both commits, exactly as designed.

**Bulk SEC work: CLOUD, NOT DARWIN.** Settled four times. **No free equity price series is
reachable from the container** — Yahoo is SSL-reset by the allowlist and stooq serves a JavaScript
challenge. `data.sec.gov` and `www.sec.gov` are fine. That constraint is now load-bearing on a
*ruling*, not just an inconvenience: it is half of why REG-009 chose δ (§1.2).

## THE TWELVE THINGS THAT HAVE EACH COST A SESSION A RUN

1–8 unchanged (registered machinery: `onset_rule="peak"`; `peak_onset` returns a tuple; control arm
in the same pass; the panel is registered machinery; `git log -S` recovers a dangling ordinal;
a feasibility probe that reads the arm label is the experiment; taking "the latest X" and "the
latest Y" independently is comparing two periods).

9. **A MEASUREMENT THAT CANNOT REPRESENT THE ANSWER IS NOT EVIDENCE OF ABSENCE.**
10. **AND ASK IT OF EVERY NON-ZERO TOO — a rate is a claim about whatever the instrument could
    reach.**
11. **AN ADJECTIVE IN A DESIGN SENTENCE IS AN UNMEASURED QUANTITY UNTIL YOU NAME THE MEASUREMENT.**
    `-26`'s "admissible" and "large enough to run something". **The cheap tell is a grep: an
    objection keyword occurring exactly ONCE in the repository is an objection nobody answered.**
12. **NEW · AND THE WORST CASE IS THE OBJECTION THE DOCUMENT RAISED AGAINST ITSELF.** 11 is about
    adjectives nobody noticed. This is the class beside it: adjectives *correctly identified as
    load-bearing*, named in the author's own voice, and then closed with assertions. Paper III §4.7
    writes *"a disclosed useful life is chosen by the same management whose timeliness is being
    measured"* — a perfect statement of the problem — and bounds it with three claims that have
    **one occurrence each**. **Self-criticism reads as rigour and counts as coverage, and it is
    neither until something measures it.** The grep tell catches this one too, and it is the reason
    to run the grep on passages you *admire* rather than only on passages you doubt.

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace.
**Manuscript:** `patchkit.apply_edits`, never `sed`. Back the file up first.
**The gh_sha dance is NOT a defect — do not "fix" it.** `--stamp`, then a commit whose whole content
is the stamp. `--check` calls that `ADVISORY: docs-only drift` and **exits 0**. Read the exit code.

## 1 · WHAT HAPPENED — the design step, taken

`94c3916` (REG-009 §1 + the §1.5 citation repair + 12 tests) in `wealth-tensor`, and `ef87a86`
(two-instance bug spray) in `darwin-scripts`. **Manuscript untouched** — paper III is byte-identical
for the third session running. **652 tests, ~40 s.**

**THE ARM IS δ.** Three reasons, in increasing order of how much they decide, and REG-009 §1 states
them in that order on purpose:

- **§1.0 · Sample size is the weakest and is stated first so it is not mistaken for the argument.**
  δ has thousands of firm-years; σ has 40 firms at a \$10M floor. A small clean sample beats a large
  dirty one and nothing established which is which.
- **§1.1 · §5's selection problem does not bind on δ.** It is an argument about which *assets* carry
  price series; it is silent about lives. σ requires resolving it first. δ does not require it at all.
- **§1.2 · The decisive one: what each arm's outstanding measurement COSTS.** σ's count 3 needs
  market-to-book from a delisted-inclusive source — CRSP/Compustat class, unreachable from the
  container, **never quoted a price**. δ's outstanding bounds need one more pass over six zips
  already named by filename. **One is procurement; the other is an afternoon.** That ruling would
  survive the sample sizes being reversed, which is why it is the one that decides.

**§1.3 · THE FINDING.** Above, and in the one-liner. Three bounds, one occurrence each, on an
objection paper III raised against itself.

**§1.4 · THE FIFTH ADJECTIVE HAS ITS RULER ALREADY BUILT, and this is the part to read twice.**
§4.7's third recommendation is that the design *"holds δ approximately constant by construction,
which is the condition §4.4 identifies."* §4.4 **does** identify it — and §4.4 has **already priced
it**: over 4,000 simulated four-class ladders, the deferral measure recovers the registered ordering
in **100.0%** of them at δ common, **11.5%** at δ drawn independently, and **1.9%** under the
standards' falling ladder. **The exchange rate is committed, simulated and sitting in the manuscript;
the input has never been computed.** Unlike the four quantifiers before it, this one needs no new
instrument — only a number fed into code that already exists.

**§1.5 · A citation defect, repaired.** `SOURCE-001` §2 sent readers to §4.8 for the coincidence
argument. §4.8 does not make it: its *stated virtue* is that its claim **"does not require inferring
a physical decay rate from a reporting rule"** — the opposite move. The argument is §4.7's, and the
repair carries §4.7's weak joint along with the citation so **the bound travels with the licence**.
`closely enough` occurs exactly once, which is how this was found. Applied by an anchor-asserting
patch script, backup first, restore exercised.

**§1.6 · FOUR DECISIONS, where the inherited handoff named one.**

| | decision | status |
|---|---|---|
| **D1** | year window (§3b) | **RULED: carry the whole span with a per-year weight.** A measured 0.727-vs-0.823 gap is a weight; the truncation that avoids it is a truncation nobody priced. |
| **D2** | interval → point | **DECLARED UNPRICED.** §3a found `Range=Min/Max` on **0.57** of dimension sets — for most firm-years the disclosure is an **interval**, and nothing in this repo maps one to a δ. |
| **D3** | life-band width | **DECLARED UNPRICED, ruler built** (§4.4). Band width trades within-band δ dispersion against firm-years per band. |
| **D4** | firm-specific vs industry-median | **DECLARED UNPRICED**, and unpriceable before D3 — "the cost of resolution" *is* a dispersion statement. |

**§2 · P0 IS DECLARED AND PRICED, NOT WRITTEN.** One probe prices D2/D3/D4 and measures two of the
three bounds: **P0-a** within-firm dispersion across years (stickiness, §4.7 bound 2, never
measured), **P0-b** within-SIC dispersion (bounds 1 and 3, which are the same claim from two sides),
**P0-c** within-band δ dispersion swept over band width, fed into §4.4's committed simulation.
Guards inherited **as code**: `THIN` at 30, a *z* on every quoted gap, no comparison between two
cells whose rates were just refused (§4c's find), **and an IQR printed beside every median** —
`-26`'s "what I would do differently", promoted from a lesson to a mechanism.

**§3 · DEFINITION OF DONE — six checkable items** — plus **EXPLICITLY NOT IN SCOPE** (the σ arm,
count 3, §5's choose-your-shape → **REG-010**) so that finishing is distinguishable from stopping.
**§4 · STOPPING RULE, pre-committed**: if no band width reaches §4.4 recovery **> 0.80** at **≥ 30**
firm-years per band, the δ design is **refused** and P0's table is the result. Threshold defended
rather than derived (§4.4's own poles are 1.000 and 0.115; 30 is §3b's inherited `THIN` line, not a
new number invented to pass).

## 2 · RULINGS — DO NOT REOPEN

- Prior rulings stand: no third disclosure instrument; the two dead (f) keywords stay in `INTERNAL`;
  phrase set frozen at 38; retail PP&E × intangible cells out of §5.4; §4.4 settled; References
  block; §4.5's 400-vs-4,000 not a defect. `SOURCE-001` is **not** a registration.
- `-24`'s, `-25`'s and `-26`'s stand unchanged, including: the dominant-asset restriction delivers a
  **sample**, not an admissible σ; §4b's "0.80 buys the trade §2 cares about" is **INVERTED**;
  **`SOURCE-001` IS FINISHED** — `-27` did not open it for a probe and neither should you.
- **NEW · THE ARM IS δ.** Registered in REG-009 §1 with the cost argument above. Reopening it
  requires a *quoted price* for a delisted-inclusive series, not an intuition about sample size.
- **NEW · D1 IS RULED: the whole span, with a per-year, per-fiscal-calendar weight.** The
  intervening cycles get filled (§4 item 2) rather than the early span getting dropped.
- **NEW · §4.8 IS NOT THE COINCIDENCE ARGUMENT; §4.7 IS, AND IT COMES WITH A WEAK JOINT.** Anything
  citing §4.8 for the licence to read δ off a disclosure is citing the wrong section, and the right
  section does not hand the licence over unbounded.

## 3 · NEW MACHINERY

`docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` (§1 only — **ships no instrument and
licenses no run**, deliberately) · `tests/test_reg009_design.py` (**12**) which pins the citation
repair, the per-file locations of every bound keyword, and an independent invariant that **no bound
has leaked into `scripts/` or a `RESULT-*`** — because that is where a *measurement* would land.
**652 tests.**

**BUG SPRAY, `ef87a86` in `darwin-scripts`, and the second instance is the interesting one.**
`grep -c PATTERN file || echo 0` **prints "0" AND exits 1** on no-match, so the fallback appends a
*second* zero and every later `-gt` dies on `0\n0`. **It fires only on the clean path** — which is
why it survived for months in two places. Instance 1 was `bridge-status.sh`, throwing on the very
first command of this session. Instance 2 was found by asking *where else does this shape live*:
`shred-call-artifacts.sh`, where the corrupted value feeds the block telling an operator whether a
Time Machine snapshot may still hold a **pre-shred plaintext copy** of just-destroyed call
artifacts. A PII destroy tool's one safety report was ending in a bash error on the all-clear path.
Fixed with `|| true` + `${n:-0}`; three-branch drill (0 matches / 2 matches / no file) extracting
the fixed idiom rather than reimplementing it — the middle branch matters, because the *naive* fix
`n=$(grep -c …) || n=0` also silences the error while discarding a real count.

**Mutation drill.** Restoring `SOURCE-001` from its `.bak` reddens exactly 3 tests (the citation
test and two pinned locations); re-applying returns sha256 `eebdf18a` and green. **The restore was
exercised, not trusted.**

## 4 · THE AT-BAT, RANKED

1. **P0. It is the only thing standing between REG-009 and its §§2–8.** REG-009 §2 declares it in
   full; write it, run it **from the cloud**, commit `RESULT-P0`. Reads the six FSN notes zips per
   cycle for the disclosed life **VALUES** (`num.tsv` durations, `txt.tsv`'s value column, plus the
   component × `Range` axis). **Do not price this as a groupby on
   `data/source-001-lifetime-by-fyend*.json`** — `-27` nearly did, and the reason it is wrong is in
   §5 below. Outputs P0-a/b/c; then REG-009 §2 fixes D2/D3/D4 **citing P0's table**, and the probe
   does not get to choose (§4c's precedent).
2. **Then REG-009 §§2–8, committed ALONE**, before the instrument exists: registered quantities, the
   seven registration questions, predictions, falsifiers with their *kills the run / kills the
   marker / kills the interpretation* verdicts. A registration must precede its instrument's **code**.
3. **Fill the coverage series between §3b's two cycles.** Now unconditional — D1 ruled for the whole
   span, so this is required rather than optional. Six FSN zips per cycle, ~90 s each, **cloud**.
   `--compare` already does the arithmetic.
4. **The gate defect card** — State Machine `1217465036940491`. Still open, still a good warm-up.
5. **AAR actions A1/A2** — the `pre-commit` roster brake (`1217468064910605`) and an audit of the
   other four `post-*` hooks in `darwin-mac-ops/hooks`. **Untouched for FIVE sessions now.** The
   brake fired correctly on both of `-27`'s commits, which is the argument for finishing it rather
   than for continuing to rely on eight siblings being polite. **This is the item most likely to be
   deferred a sixth time; consider doing it first, before the at-bat gets interesting.**
6. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
7. **Widen the reach guard to REG-001/002/006's non-ledger restatements.** Third layer, mechanical.
8. **Run the §1.3 grep on paper III's OTHER self-critical passages.** `-27` ran it on one and found
   three unanswered bounds. The paper names its own weak joints in several places and that habit is
   a *virtue*; the finding is that the naming was never followed by measurement. One minute per
   passage. **This is the cheapest remaining lead in the repository.**
9. Cready et al. (2012) full text, if prior art is reopened.

## 5 · WHAT I WOULD DO DIFFERENTLY

**I called a measurement cheap in the sentence that carried my central ruling, and "cheap" was my
own unmeasured adjective.** §1.2's whole argument is that δ's outstanding measurement is a re-read
and σ's is a purchase order. The first draft said the dispersion probe was a *groupby on a committed
file already on disk* — `data/source-001-lifetime-by-fyend.json`, which every prose reference in the
repo describes as carrying "per-firm-year records". It carries four booleans and a **count of tag
occurrences**; `scan_zip()` filters `txt.tsv` on the tag *name* and never opens a value column. So
the probe is a re-read of the zips. **The ruling survived — a zip re-read is still not a purchase
order — but it survived at a price I checked rather than assumed, and I checked it only because I
was writing a document about unmeasured adjectives.** The general form is cheap and worth
automating in your head: **an artifact built to answer *was X present* does not answer *what was X*,
and the two are indistinguishable from the filename and from the prose that cites it.** Sixty
seconds in the JSON.

**Second: my guard failed on its own author twice, and the SECOND failure was the useful one.**
`test_reg009_design.py` greps the corpus to hold §1.3's finding. **v1** pinned a corpus total and
died immediately — the test names every needle in its own parametrisation, *and* §1.5's repair
**restates** the three bounds while flagging them unanswered. (**To a raw count, a repair that
propagates a finding and a restatement that ignores it are identical.**) **v2** pinned per-file
counts and died again the moment *this handoff* reported the finding. I very nearly just added
`HANDOFF.md` to the exclusion list. **That would have been the third symptom treated as the second
fix.** A guard whose only maintenance is appending exclusions is the doctrine's permanently-red
check wearing a diligence costume. **v3** holds the two things that are genuinely invariant — *the
anchor* (each bound occurs once **in paper III**, §4.7's declaring sentence; if that moves, §1.3 is
about a sentence that no longer exists) and *the measurement homes* (no bound in `scripts/`,
`data/` or a `RESULT-*`, because that is where a measurement would land and nowhere else). Design
docs are not counted at all — discussing this is their job. **The general form: when a guard fires
on legitimate propagation twice, the guard is measuring the wrong thing. The first firing is
information about the code; the second is information about the guard.**

**Third, small and structural: I nearly let the handoff's own ranking pick my finding for me.** The
inherited §4 said δ has "ONE live decision". It has four; three were invisible because nobody had
asked what the *shape* of a disclosed life is (an interval, 57 % of the time). A handoff's ranked
list is a previous session's model of the work, and it is exactly as good as that session's
scope — **the item that says "one live decision" is the one to audit, because a count is a
quantifier and this repository's speciality is quantifiers that were never measured.**

## 6 · THE GATE

See the frontmatter for the verdict; **believe `--emit`'s exit code over this field.** Run
`export GATE_ROSTER_WHO=big-wealthTensor-28` **before** `~/Scripts/gate-selfcheck.sh` — without it
the script cannot tell a sibling's dirt in `~/Scripts` from yours, and with eight claimants that is
the difference between a named warning and a false blocker.

**`HANDOFF-GATE.md` in `claude-blackbook` is a MIRROR.** Canonical is
`~/Desktop/downloads/HANDOFF-GATE.md` (repo `darwin-everything-meta`); edit there and run
`~/Scripts/mirror-handoff-gate.sh`, which syncs *and pushes* claude-blackbook by itself.

## 7 · STUDENT-IN

`lessons.py doctrine`, then `search "<task>" --scope global,wealth-tensor`. `-27` banked **three
global leaves and one project leaf**, and corroborated **two** through the attribution loop
(`wt27-reg009 pass`).

**The `-26` discipline, run and reported rather than assumed.** Both used leaves' lead clauses were
re-read at wrap against this session's work. *"SOURCE-001's 0.82 coverage is a RECENT-YEARS number
and does not hold across the panel's span"* — **still licensed, and now load-bearing**: it is the
whole of D1's ruling. *"A coverage rate that is low only at the ends of the window is measuring the
window"* — untouched, still true. Neither needed curation. That is a real check with a null result,
which §5 of the charter says to report as plainly as a find.

The new ones worth knowing before you start: **`grep -c P f || echo 0` yields `0\n0` and fails only
on the clean path** · **a test that greps the corpus to protect a finding is part of the corpus, and
so is the document reporting the finding — pin per file, not a total** · **before pricing a
follow-up measurement as cheap because "the artifact is on disk", open the artifact and read its row
schema** · **(project) the δ arm's exogeneity case is unmeasured and §4.8 is not where it lives.**
