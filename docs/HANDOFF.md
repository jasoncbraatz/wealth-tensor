---
project: wealth-tensor
gh_sha: PENDING
updated: 2026-08-13
session: wealthTensor-28
gate_passed: true
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. **`docs/preregistration/RESULT-P0.md`** — new, and it is what unblocks the thread.
4. **`docs/preregistration/REG-009-p3-lifetime-sourced-delta.md`** — §1 chose the arm, **§1.3a is
   new and carries the dispositions**, §3 is the definition of done (items 1, 2, 5, 6 now DONE),
   §4 is a pre-committed refusal that has now been applied.
5. §7's student-in, then §4's at-bat. **§6 first if you are about to run the gate.**

> **`-28` in one line: P0 ran, and §4.7's three bounds now carry numbers instead of assertions —
> bound 2 SPLITS BY CLASS, bounds 1 and 3 are the SAME QUANTITY POINTING BOTH WAYS, and the sixth
> unmeasured quantifier showed up inside this session's own instrument within an afternoon.**
> Property lives are unrevised (0.744 of components identical eight years apart); intangible lives
> are not (0.309). Industry major group explains 0.288 of the variance of log property life and
> 0.080 of intangible — so §4.7's proposed escape hatch (industry-median lives) leaves behind
> exactly the dispersion §4.4 says destroys the ranking. **The escape hatch and the hazard are the
> same door.** And P0-c's first table reported a recovery of 0.998 without mentioning that the band
> held ONE distinct disclosed value. **You will meet the seventh. The grep tell still works; the new
> tell is to run it on your own output, and to ask the instrument-artefact question of numbers that
> look GOOD.**

## 0 · TRANSPORT — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -28 without exception**. Roster join/claim as
`big-wealthTensor-29` — **`roster claim` takes `--resource`, not `--repo`**.
`export LESSONS_CONTRIBUTOR=opus`. **`export GATE_ROSTER_WHO=<you>` at the TOP**, not at the gate — §6.

**NEW · macOS `base64` REJECTS A BARE FILE ARGUMENT.** `base64 -d ~/f.b64 > out` dies with
`invalid argument`; use `cat ~/f.b64 | base64 -d > out` (or `-i`). Cost two minutes mid-transfer and
it will cost the next session the same, because the GNU form is the one in muscle memory.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy.
**685 tests, ~41 s on darwin** (was 654 at the start of `-28`).

**NEVER inline a multi-line string in a `dx '...'` argument — AND A HEREDOC IS NOT AN ESCAPE.**
Write locally → `dx --put` → run it / `git commit -F`. `-28` moved a nine-file tarball, a commit
message and a lesson-banking script that way and `shasum`-compared **all nine files byte-for-byte**;
zero corruption. **Patch scripts beat `sed` for anything structural, and verify EVERY anchor before
writing ANY file** — a partial application across a document is worse than a clean refusal.

**Stage by PATH. Never `git add -A` on darwin** — the tree is shared with siblings.

**Bulk SEC work: CLOUD, NOT DARWIN.** Settled five times. **No free equity price series is reachable
from the container** — Yahoo is SSL-reset by the allowlist, stooq serves a JavaScript challenge.
`data.sec.gov` and `www.sec.gov` are fine and **fast**: a 630 MB FSN notes zip downloads in under a
minute and a full `txt.tsv` scan is ~16 s, so the twelve-zip two-cycle re-read `-28` ran is about
six minutes of compute, not the afternoon §1.2 priced it as. That constraint is load-bearing on a
*ruling* (it is half of why REG-009 chose δ) and the ruling survived its own price being checked.

## THE THIRTEEN THINGS THAT HAVE EACH COST A SESSION A RUN

1–8 unchanged (registered machinery: `onset_rule="peak"`; `peak_onset` returns a tuple; control arm
in the same pass; the panel is registered machinery; `git log -S` recovers a dangling ordinal; a
feasibility probe that reads the arm label is the experiment; taking "the latest X" and "the latest
Y" independently is comparing two periods).

9. **A MEASUREMENT THAT CANNOT REPRESENT THE ANSWER IS NOT EVIDENCE OF ABSENCE.**
10. **AND ASK IT OF EVERY NON-ZERO TOO — a rate is a claim about whatever the instrument could reach.**
11. **AN ADJECTIVE IN A DESIGN SENTENCE IS AN UNMEASURED QUANTITY UNTIL YOU NAME THE MEASUREMENT.**
    The cheap tell is a grep: an objection keyword occurring exactly ONCE is an objection nobody answered.
12. **AND THE WORST CASE IS THE OBJECTION THE DOCUMENT RAISED AGAINST ITSELF.** Self-criticism reads
    as rigour and counts as coverage, and it is neither until something measures it.
13. **NEW · ASK THE INSTRUMENT-ARTEFACT QUESTION OF NUMBERS THAT LOOK GOOD.** `-25` learned it on a
    number that looked like delinquency (*a coverage rate low only at the ends of the window is
    measuring the window*). `-28` needed it on a number that looked like success: P0-c's
    quarter-year life band recovered the registered ordering **99.8 %** of the time because the band
    contained **one distinct disclosed value** — dispersion collapsed by ARITHMETIC, not economics.
    **A validity statistic computed on a coarse proxy is an UPPER BOUND on the thing it stands for,
    and the coarseness has to be printed in the same table or the bound reads as the estimate.**

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace.
**Manuscript:** `patchkit.apply_edits`, never `sed`. Back the file up first.
**The gh_sha dance is NOT a defect — do not "fix" it.** `--stamp`, then a commit whose whole content
is the stamp. `--check` calls that `ADVISORY: docs-only drift` and **exits 0**. Read the exit code.

## 1 · WHAT HAPPENED — the probe, run

`67c53c4` in `wealth-tensor`: `scripts/reg009_p0_lifetime_values.py`, `RESULT-P0.md`,
`RESULT-P0-run.log`, three data artifacts, `tests/test_reg009_p0.py` (**28**), and v4 of
`tests/test_reg009_design.py`. Plus five lessons banked and two corroborated (one promoted
quarantine→active). **Manuscript untouched — paper III is byte-identical for the fourth session
running.**

**TWO CHECKS SAY THE READER READ CORRECTLY**, and they are worth copying rather than admiring.
Coverage lands within four thousandths of §3b's on both cycles (**0.723 vs 0.727**, **0.817 vs
0.823**) through §3b's own firm-year join, *imported rather than copied*. And the values reproduce
`SOURCE-001` §3a's independently hand-audited Target Corp filing component for component
(**23.5 / 8.5 / 4.5** from P8Y–P39Y, P2Y–P15Y, P2Y–P7Y), pinned against the filing rather than
against P0's own output.

**P0-a · BOUND 2 SPLITS BY CLASS, and the split is the finding.** 0.744 of property components carry
the *identical* disclosed life eight years apart, median move exactly zero, IQR to 0.057 — not
merely sticky, **unrevised**. 0.309 of intangible components manage it, median move 0.207 in log.
Of intangible firms with ≥3 observations, **0.761 revise more than once**. §4.7 states the bound
once, over both classes, in one clause; it is true of one of them. *Measured per component as well
as per firm-year, because a firm-year life is a median across components and moves when the MIX
moves — that confound would otherwise have been read as instability.*

**P0-b · BOUNDS 1 AND 3 ARE THE SAME QUANTITY POINTING BOTH WAYS.** SIC major group accounts for
**0.288** of the variance of log property life and **0.080** of log intangible life (clustered CIs
in the doc). §4.7 offers industry-median lives as the escape from its weak joint "at the cost of
resolution" — and the measured cost is that the median discards the firm-level endogeneity while
keeping ~0.71 of the dispersion as within-band noise, which is the quantity §4.4 says destroys the
ranking.

**P0-c · §1.4's UNCOMPUTED INPUT, COMPUTED — and the ruler was LIFTED, not rebuilt.** §4.4's
simulation is extracted from `wt088_disclosed_ladder.py` **at run time by name** and refuses to run
unless it still prints the manuscript's committed poles — **0.115 / 1.000 / 0.019**, matched
exactly. One substitution only: the δ support becomes a band's own measured δ = 1/L. Run at §5.4's
**measured α̂ = 0.408**, because at §4.4's calibrated 0.05 the entire disclosed rectangle is outside
the model's domain. *The extraction ABORTED on its first run — it missed two tuple-assigned
constants — which is the behaviour under test and is now a test.*

**§4's STOPPING RULE, APPLIED AS WRITTEN: CLEARED**, by all six (tag, rule) pairs, at a 0.25-year
band. **ERRATUM RECORDED NOT REPAIRED:** the rule prices recovery and the THIN floor and is silent
on **coverage**, so it is satisfied by a width that recovers beautifully on a quarter of the sample.
Rewriting a pre-commitment after seeing the table is the one move a pre-commitment exists to
prevent (REG-002 E1's precedent). **Held to coverage ≥ 0.80, exactly one rung survives: property
under `R_MIN` at a 1-year band — recovery 0.934, worst band 0.820, coverage 0.920.**

**THE `-27` GUARD FIRED A THIRD TIME, on the event it was built to detect.** v3 asserted no bound had
reached a measurement home; `-28` measured them and it went red **on success**. Its own failure
message said what to do. **v4 is a DISCHARGE LEDGER, not an exclusion** — an exclusion says *stop
looking here*, a ledger says *this was answered HERE and reopens if the answer disappears* — and v4
has strictly **more** to fail on than v3: a discharged bound must name its artifact, the artifact
must exist, must cite the part of P0 that did the work, and that part's lines must carry a **number**.

## 2 · RULINGS — DO NOT REOPEN

- Prior rulings stand: no third disclosure instrument; the two dead (f) keywords stay in `INTERNAL`;
  phrase set frozen at 38; retail PP&E × intangible cells out of §5.4; §4.4 settled; References
  block; §4.5's 400-vs-4,000 not a defect. **`SOURCE-001` IS FINISHED** and is not a registration.
- **THE ARM IS δ.** Reopening it requires a *quoted price* for a delisted-inclusive series.
- **D1 IS RULED: the whole span, with a per-year, per-fiscal-calendar weight.**
- **§4.8 IS NOT THE COINCIDENCE ARGUMENT; §4.7 IS, AND IT COMES WITH A WEAK JOINT.**
- **NEW · P0 DOES NOT CHOOSE D2/D3/D4.** It priced them. The choice is REG-009 §2's, in a commit
  that cites P0's table — §4c's precedent, declared before the instrument existed and honoured.
- **NEW · EVERY P0-c RECOVERY NUMBER IS AN UPPER BOUND.** It is computed from the *disclosed* δ, and
  the gap between disclosed and economic δ is §4.7's weak joint, which P0 did not measure and was
  not built to. Any later text quoting 0.934 without that qualifier is the seventh quantifier.
- **NEW · `R_WEIGHT` IS NOT A THIRD RULE ON MOST OF THE SAMPLE.** Component amounts back it on a
  minority of firm-years; the rest fall back to `R_MID`. Target Corp is one of them.

## 3 · NEW MACHINERY

`scripts/reg009_p0_lifetime_values.py` (`extract` per cycle → records; `report` → P0-a/b/c, offline
and rerunnable) · `docs/preregistration/RESULT-P0.md` + `RESULT-P0-run.log` ·
`data/reg-009-p0-lives-{2015,2023}.json` (**1,296 firm-year records, 412 comparatives**) ·
`data/reg-009-p0-result.json` · `tests/test_reg009_p0.py` (**28**) · v4 of
`tests/test_reg009_design.py`. **685 tests.**

**Guards that are code, not memory:** THIN at 30 · a *z* or a **clustered** bootstrap on every
quoted gap · no comparison between two cells this file just refused · an IQR beside every median
with an order-of-magnitude span called two populations · **no silent caps** (329 filings with no
value, 316 duplicate `iprx` rows, 51 unparseable durations and 4,990 rows on 177 non-canonical
`*UsefulLife*` tags are each counted and named).

**Mutation drill.** Reverting the two edited files reddens exactly **3** tests and re-applying
returns the same sha256 and green. **The restore was exercised, not trusted.**

## 4 · THE AT-BAT, RANKED

1. **REG-009 §§2–8, committed ALONE, before any instrument exists.** This is the whole point of the
   thread and P0 was the only thing in front of it. Registered quantities; the seven registration
   questions; predictions; falsifiers with their *kills the run / kills the marker / kills the
   interpretation* verdicts; a stopping rule. **Fix D2, D3 and D4 in §2 citing `RESULT-P0`'s table —
   and note that the table's own best rung (`R_MIN`) scores highest partly because it heaps
   hardest, which is an argument about the disclosure and not about the rule.**
2. **Fill the coverage series between §3b's two cycles.** Unconditional since D1's ruling. Six FSN
   zips per cycle, **~1 min download + ~16 s scan each** — much cheaper than previously priced.
   `--compare` already does the arithmetic, and `reg009_p0_lifetime_values.py extract` will now give
   you values for the same zips in the same pass.
3. **Run the §1.3 grep on paper III's OTHER self-critical passages.** `-27` ran it on one and found
   three unanswered bounds; `-28` measured all three and two came back **against** the paper. The
   paper names its own weak joints in several places. **Still the cheapest remaining lead in the
   repository — one minute per passage.**
4. **The gate defect card** — State Machine `1217465036940491`. Still open, still a good warm-up.
5. **AAR actions A1/A2** — the `pre-commit` roster brake (`1217468064910605`) and an audit of the
   other four `post-*` hooks in `darwin-mac-ops/hooks`. **Untouched for SIX sessions.** Do it first.
6. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
7. **Widen the reach guard to REG-001/002/006's non-ledger restatements.** Third layer, mechanical.
8. **`AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife` is 4,304 rows P0 excluded** to
   keep its population identical to §3a's and §3b's. It is a weighted-average life straight from the
   filing and REG-010 may want it. Named here so the exclusion does not become invisible.
9. Cready et al. (2012) full text, if prior art is reopened.

## 5 · WHAT I WOULD DO DIFFERENTLY

**I shipped a table with a 0.998 in it and only caught the reason on a second pass.** P0-c's first
run priced band widths and printed nothing about the disclosed life being a round number 87.5 % of
the time. The number was not wrong; it was *about the disclosure's coarseness rather than about the
assets*, and nothing in the table said so. What caught it was reading my own output the way `-25`
read a suspiciously LOW coverage figure — **could this instrument have produced this number for a
reason that has nothing to do with the world?** I had been running that question on numbers that
disappointed me. **The document diagnosing unmeasured adjectives grew one inside an afternoon, which
is the second session running that this has happened to; treat it as the base rate, not the anecdote.**

**Second: I wrote a docstring that promised something the code did not do, and only a test caught
it.** `R_WEIGHT`'s docstring said the fallback share "IS REPORTED rather than absorbed" and no line
printed it — so Target Corp, three component lives and no component amounts, was carrying an
`R_WEIGHT` that was silently `R_MID`. **A docstring is an assertion in a design sentence.** Rule 11
applies to your own code, and the cheap tell is to grep your own prose for what it promises and
check each promise has a `print`.

**Third: my point estimate and my bootstrap were two different estimators and the CI announced it
by not bracketing the point** (0.914 with a 95 % interval of [0.930, 0.980]). One estimator function
taking a sample, called for the point AND inside every replicate. The non-bracketing interval is the
cheapest possible tell and it is worth *looking* for.

## 6 · THE GATE

See the frontmatter for the verdict; **believe `--emit`'s exit code over this field.** Run
`export GATE_ROSTER_WHO=big-wealthTensor-29` **before** `~/Scripts/gate-selfcheck.sh` — without it
the script cannot tell a sibling's dirt in `~/Scripts` from yours.

**`HANDOFF-GATE.md` in `claude-blackbook` is a MIRROR.** Canonical is
`~/Desktop/downloads/HANDOFF-GATE.md` (repo `darwin-everything-meta`); edit there and run
`~/Scripts/mirror-handoff-gate.sh`, which syncs *and pushes* claude-blackbook by itself.

## 7 · STUDENT-IN

`lessons.py doctrine`, then `search "<task>" --scope global,wealth-tensor`. `-28` banked **three
global leaves and two project leaves**, and corroborated **two** through the attribution loop
(`wt28-reg009-p0 pass`) — **one of which, `-25`'s window leaf, went quarantine→active on its second
pass.** That leaf is the direct ancestor of thing 13 above.

**The `-26` discipline, run and reported.** *"SOURCE-001's 0.82 coverage is a RECENT-YEARS number"* —
still licensed, still load-bearing, and now **reproduced independently** by a different reader on the
same zips (0.723/0.817 against 0.727/0.823). *"A coverage rate low only at the ends of the window is
measuring the window"* — used, generalised, and promoted. Neither needed curation.

The new ones worth knowing before you start: **an absence-asserting guard goes RED ON SUCCESS —
convert it to a discharge ledger, never an exclusion** · **ask the instrument-artefact question of
numbers that look good** · **a bootstrap CI that does not bracket its own point estimate means two
different estimators** · **(project) FSN life VALUES need `dim.tsv`, a `ddate == period` filter and
an `iprx` dedupe** · **(project) disclosed lives are heaped, so every within-band δ dispersion is an
upper bound**.
