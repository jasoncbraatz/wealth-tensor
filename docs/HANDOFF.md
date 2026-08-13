---
project: wealth-tensor
gh_sha: 1636eaa7b9e77b728c20ac9c56d514708aac2ef1
updated: 2026-08-13
session: wealthTensor-26
gate_passed: PENDING
gate_version: "2.51"
---

# wealth-tensor — HANDOFF

## ORIENT — read these first, in this order

1. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS**: where this handoff,
   any result doc, or any plausible-sounding rewrite conflicts with it, the charter governs and the
   other thing is wrong. *This file is a status report. It is not law and it cannot amend the charter.*
2. `python3 scripts/handoff_gate.py --check` — proves this file is not stale.
3. §7's student-in, then §4's at-bat. **§6 first if you are about to run the gate.**

> **`-26` in one line: `SOURCE-001` has no cheap steps left — every one is run — and the last one
> did not measure σ, it measured the sentence that licensed measuring σ.** §1. `-23` said a route
> was closed and it was open; `-24` said a branch was property-only and it was not; `-25` said
> "flat across a decade" was flat across one quarter; **`-26` says "admissible" was one objection
> of three, and "large enough to run something" included a company with $388 to its name.** Four
> sessions, four wrong quantifiers, same document, and the shape has now changed once: `-23`
> through `-25` mis-scoped a **number**. `-26`'s two were **adjectives** — words in a design
> sentence that no measurement ever licensed. You will meet the fifth. **When you read an
> evaluative word in this repo — admissible, sufficient, tighter, clean, alive — the question is
> not whether it is true. It is which measurement made it sayable.**

## 0 · TRANSPORT — darlish, zero-bridge

Standard bring-up; post the `DARLISH-ENROLL` line to Asana **1217316841710435**, collect, then `dx`.
First collect has worked **-06 through -26 without exception**. Roster join/claim as
`big-wealthTensor-27` — **`roster claim` takes `--resource`, not `--repo`**.
`export LESSONS_CONTRIBUTOR=opus`. **`export GATE_ROSTER_WHO=<you>` at the TOP**, not at the gate — §6.

**Run pytest with `.venv/bin/python`, not `python3`** — the system interpreter has no scipy.
**640 tests, ~40 s** (was 590).

**NEVER inline a multi-line string in a `dx '...'` argument — AND A HEREDOC IS NOT AN ESCAPE.**
Write locally → `dx --put` → run it / `git commit -F`. `-26` moved four repo files, three commit
messages and **four executable patch scripts** that way, `shasum`-comparing every one; zero
corruption. **Patch scripts beat `sed` for anything structural**: `-26`'s asserted its anchors and
exited non-zero rather than guessing, which is what makes a remote edit reviewable.

**Stage by PATH. Never `git add -A` on darwin** — `-26` shared the tree with **eight** claimants and
was warned by the roster brake on both commits. Three commits, each staged by name, each clean.

**Bulk SEC work: CLOUD, NOT DARWIN.** Settled three times now. **New, and it will save you an
hour: `yfinance`/Yahoo is NOT reachable from the cloud container** — `curl_cffi` SSL connection
reset, network allowlist. `data.sec.gov` and `www.sec.gov` are. `stooq.com` serves a JavaScript
challenge, not CSV. So **there is no free equity price series from the container**, which is
precisely why §4c's count 3 is unmeasured rather than zero.

## THE ELEVEN THINGS THAT HAVE EACH COST A SESSION A RUN

1–8 unchanged (registered machinery: `onset_rule="peak"`; `peak_onset` returns a tuple; control arm
in the same pass; the panel is registered machinery; `git log -S` recovers a dangling ordinal;
a feasibility probe that reads the arm label is the experiment; taking "the latest X" and "the
latest Y" independently is comparing two periods).

9. **A MEASUREMENT THAT CANNOT REPRESENT THE ANSWER IS NOT EVIDENCE OF ABSENCE.** Ask of any zero:
   *could this instrument, or this sample size, have produced a non-zero?*
10. **AND ASK IT OF EVERY NON-ZERO TOO — a rate is a claim about whatever the instrument could
    reach.** The window form (low only at the ENDS of a window = measuring the window) and the
    slice form (flat on the slice it measured, moving on the one it could not).
11. **NEW · AN ADJECTIVE IN A DESIGN SENTENCE IS AN UNMEASURED QUANTITY UNTIL YOU NAME THE
    MEASUREMENT.** 9 and 10 are about numbers whose scope drifted. This is the class above them:
    words that were never numbers at all, sitting in sentences that license runs. Two of them cost
    `-26` the whole session's premise —
    - **"admissible."** §2 rejected equity volatility on **three** counts, each fatal *on its own*;
      §6 step 3 said the dominant-asset restriction "is what makes it admissible under §2." It
      clears **one**. **The cheap tell is a grep:** search for each objection's keyword. `levered`
      and `growth options` appeared **exactly once each in the entire repository** — in the sentence
      declaring them fatal. *An objection with one occurrence is an objection nobody answered.*
    - **"large enough to run something."** §4b's 99 firms. **35 of them have total assets under
      $1M and the smallest has $388.** A ratio is silent about its denominator, and nobody had
      printed a size.

**Witness contract:** a `\b` inside a NON-RAW fragment of a concatenated regex is a backspace.
**Manuscript:** `patchkit.apply_edits`, never `sed`. Back the file up first.
**The gh_sha dance is NOT a defect — do not "fix" it.** `--stamp`, then a commit whose whole content
is the stamp. `--check` calls that `ADVISORY: docs-only drift` and **exits 0**. Read the exit code.

## 1 · WHAT HAPPENED — §6 step 5 ran, and it never reached σ

`c28fbe6` (§4c + probe + artifact + 48 tests) and `67996c6` (bug spray + 2 tests). **Manuscript
untouched** — paper III is byte-identical. **640 tests, ~40 s.**

**`SOURCE-001` §4c — the restriction clears one of §2's three counts.** §2 rejects equity return
volatility as a σ proxy on three independent counts, "any one of which is fatal": it is **levered**,
it **aggregates** every asset, it prices **growth options**. §4's dominant-asset restriction is
aimed at aggregation, and §4a/§4b priced how hard it bites there. §6 step 3 then promoted that to
*"the restriction is what makes it admissible under §2 rather than a proxy in violation of it."*
One count doing three counts' work — and running the σ probe on that sentence would have committed
WT-038 **with the restriction serving as the alibi.**

| | 0.70, no floor | ≥ $1M | ≥ $10M | ≥ $100M |
|---|---|---|---|---|
| firms | **99** | 64 | **40** | 18 *(THIN)* |
| composition | ppe 47, gw 18, int 34 | 28 / 17 / 19 | 19 / 12 / 9 | 10 / 7 / 1 |
| median total assets | **$4.76M** | $21.0M | $95.5M | $895M |
| current registrant | 24 / 99 | 18 / 64 | 13 / 40 | 4 / 18 |

1. **Count 1, measured, and it runs AGAINST the restriction.** Book equity / assets, period-matched
   to the same balance sheet the class share came off — under the accounting identity that *is* the
   deleveraging factor E/(D+E). At a $10M floor the pooled median is **0.384**, so
   σ_equity ≈ **2.6 ×** σ_asset. By class the **PP&E arm is the most levered of the three**: 0.113
   against goodwill's 0.641 and intangibles' 0.605 (z = +2.04 on the share below 0.50; all three
   buckets are `THIN`, so their rates are refused and only the comparison is reported). **Property
   is collateral and collateral supports debt, so PP&E-dominance and leverage are one balance sheet
   read from either side.** The restriction buys count 2 by selecting the firms that fail count 1
   hardest. That is not a confound to control for; it is the same fact twice.
2. **Count 3 is NOT MEASURED**, recorded in the artifact as `count3_measured: false` with its reason
   so nothing downstream can read the silence as a zero. Growth options need **market** equity and
   no market-data source is reachable from the container. §3's error, refused by naming it.
3. **A fourth objection §2 never listed.** A class share is a ratio; a ratio is silent about its
   denominator. The restriction **concentrates** sub-$1M filers rather than inheriting them —
   0.354 inside against 0.128 in the complement, **z = +6.18** (sub-$10M, z = +7.86) — and does so
   **monotonically harder as the threshold tightens** (median assets $33.5M → $12.0M → $4.76M →
   **$1.28M** across 0.50 / 0.60 / 0.70 / 0.80). **So §4b's third consequence inverts:** 0.80 does
   not "buy a much tighter restriction, which is exactly the trade §2 cares about." It buys
   concentration by trading real firms for shells.
4. **Reach, two independent instruments that never touch.** 38 / 47 of the PP&E arm last filed by
   2019 (median last balance sheet **2016**); 4 / 47 are current registrants (z = −3.49 vs
   intangibles). They agree without collusion: **0 / 61** of firms last filing ≤2019 are current
   registrants, **23 / 32** of those filing ≥2023 are. **Stated as an antecedent only** — a
   CURRENT-registrant file cannot establish that no price series exists; that would be §3's 404 read
   as a fact about the filer, in a new coat.
5. **The intangibles arm, which §4b left open, is answered without needing the argument.** `-24`
   proposed an untested §2 reading (acquisition residue, nearer the goodwill objection). §4c does
   not need it: the arm is 34 firms with **median total assets $1.28M**, nine above $10M, one above
   $100M. Whether they pass §2 is downstream of whether enough of them exist. *(The n=1 cell at
   $100M is explicitly declined, not read — that would be §4b's own error with the roles swapped.)*

**New refusal carried as code: `MATERIALITY_FLOORS`, swept rather than assumed** — which floor to
use is REG-009's choice to defend, and the probe's job is only to price it. `THIN` and `IMPOSSIBLE`
inherited. **And one incoherence found in my own guard mid-build:** a two-proportion z printed
between two `THIN` buckets launders rates the same paragraph just refused. Not suppressed — that
hides information — but **labelled**, so the comparison stays and the refusal is not quietly undone.

**BUG SPRAY (`67996c6`), two finds.** (a) `source001_concentration.py` is the file `-24` was running
when darwin got **IP-flagged**, and its docstring still offered *"darwin's disk runs hot"* as the
only siting consideration — i.e. it read as guidance to run it there. The cloud warning had landed
in `source001_lifetime_by_fyend.py`, written a session later; **the lesson went to the newer file
and not to the one that earned it.** (`source001_lifetime_coverage.py` deliberately left alone — it
reads local zips and makes no network call.) (b) §4c's corrections to §4b and §6 are **pointers**,
and this document's own finding is that a caveat which does not gate the conclusion is decoration.
Two tests now hold the cross-references in §§2, 4, 4b and 6, and hold §6 step 5 marked **RUN**, so
`-27` does not re-run a finished step.

**Mutation drills, both commits.** A firm moved across the $1M floor reddens three tests; a changed
digit in a quoted z reddens exactly one; silently shortening `MATERIALITY_FLOORS` reddens the
guard-on-the-guards; dropping §4b's "INVERTED BY §4c" pointer reddens one. sha256 restore verified
each time.

## 2 · RULINGS — DO NOT REOPEN

- Prior rulings stand: no third disclosure instrument; the two dead (f) keywords stay in `INTERNAL`;
  phrase set frozen at 38; retail PP&E × intangible cells out of §5.4; §4.4 settled; References
  block; §4.5's 400-vs-4,000 not a defect. `SOURCE-001` is **not** a registration.
- `-24`'s reversals stand: a dominant-asset σ design is **not** automatically a property design, and
  the machine-readable route to useful lives is **open**.
- `-25`'s stands: §3a's "flat across a decade" is **narrowed, not reversed** — true of Q1 filers,
  false of the panel. Do not cite the bare clause.
- **NEW · The dominant-asset restriction delivers a SAMPLE, not an admissible σ.** §6 step 3's
  admissibility clause does not survive. Restricting to PP&E remains a legitimate *choice*, argued
  from §2 — it is not a description of what the panel contains (`-24`) and it is not an
  admissibility argument (`-26`).
- **NEW · §4b's "0.80 buys the trade §2 cares about" is INVERTED.** Tightening the threshold buys
  shells. Any future threshold choice states its materiality floor in the same sentence.
- **NEW · `SOURCE-001` IS FINISHED as a source document.** §6's steps 1, 2, 3 (as reframed), 4 and 5
  are all run; there is no cheap probe left in it. **`-27` should not go looking for one.** The next
  artifact is `REG-009`, a different document, and the step that replaces step 5 is a *design* step.

## 3 · NEW MACHINERY

`scripts/source001_sigma_admissibility.py` (counts 1 and 2 period-matched, the concentration
trajectory, two reach instruments, `MATERIALITY_FLOORS` swept; **`--from-json` regenerates the whole
report offline from the artifact**, which is what makes the tests possible without 400 SEC calls) ·
`data/source-001-sigma-admissibility.json` (99 per-firm records + provenance + `count3_measured`) ·
`tests/test_source001_sigma_admissibility.py` (50). **640 tests.**

## 4 · THE AT-BAT, RANKED

1. **`REG-009` §1. It is now the only move on this thread, and it is a DESIGN step — nothing
   further needs measuring before it can be written.** `-25` framed it as three open decisions;
   §4c collapses that. The δ/σ split is no longer symmetric:
   - **δ**: sourced, 0.82 coverage over thousands of firm-years, one live decision — §3b's
     **year-window** choice (restrict to the recent span where coverage is uniform, or carry the
     whole span with a per-year, per-fiscal-calendar weight and say why), with a measured price.
   - **σ**: **40 firms** at a $10M floor, 13 currently listed, the arm's median last balance sheet
     **2016**, the most levered of the three classes, and **count 3 not measured at all**. Plus
     §5's choose-your-shape, unchanged.

   So §1 writes itself as: choose δ and make the year-window call, or choose σ and first buy count 3
   **and** a delisted-inclusive price series. **Write the definition of done into REG-009's first
   handoff**, per the standing rule — this thread has now spent four sessions on a source document.
2. **Count 3, if and only if §1 chooses σ.** Market-to-book at each matched period end, hence a
   **delisted-inclusive** price source (CRSP/Compustat class — Yahoo and stooq are both out from the
   container, see §0). **Price the source before running anything**: this design has never been
   quoted a data cost, and §4c's reach table says why it will not be zero.
3. **Fill in the coverage series between §3b's two cycles** — *only if* the year-window decision
   takes the whole span. Six FSN zips per cycle, ~90 s each, **from the cloud**. Mechanical;
   `--compare` already does the arithmetic.
4. **The gate defect card** — State Machine `1217465036940491`. Still open, still a good warm-up.
5. **AAR actions A1/A2** — the `pre-commit` roster brake (`1217468064910605`) and an audit of the
   other four `post-*` hooks in `darwin-mac-ops/hooks`. **Untouched for FOUR sessions.** `-26` was
   warned by the brake on both commits and it worked exactly as intended — which is the argument for
   finishing it, not for continuing to rely on eight siblings being polite.
6. **The phrase set has a passenger** (unchanged): 30.4 % of trigger sentences match only
   `events or circumstances`; 7.9 % carry safe-harbour language. Post-hoc, labelled, outranked.
7. **Widen the reach guard to REG-001/002/006's non-ledger restatements.** Third layer, mechanical.
8. Cready et al. (2012) full text, if prior art is reopened.

## 5 · WHAT I WOULD DO DIFFERENTLY

**I measured leverage before I described the population, and the population is what made the
leverage number mean anything.** The first table said **median E/A = −0.476** for the PP&E arm. That
number is *true*. It is also dominated by book-insolvent shells, and it would have gone into §4c as
a statement about levered operating firms. What saved it was not care at the writing stage — it was
that the **IQR was `[−3.257, 0.317]`**, and a distribution that straddles a sign change by four
units is not one population. **The general version, cheap enough to be automatic: before quoting a
median, look at the IQR; if it spans a sign change or an order of magnitude, you have two
populations and the median describes neither.** Ten minutes. It is `-25`'s "the shape was wrong"
lesson one shelf over — and note that both saves came from the *dispersion*, not the *centre*.

Second, and it is the same mistake wearing its process costume: **the order should have been
describe-then-measure, and I did measure-then-describe and got lucky.** I only looked at asset size
because a median came back negative. Had the shells been merely small rather than insolvent, nothing
would have announced them and §4c would have reported a clean-looking leverage table on a population
half of which cannot carry the design.

Third, small: I built a guard that printed a two-proportion z between two buckets whose *rates* the
same function had just refused as `THIN`. Caught it while reading my own output, not while writing
it. **Guards need to be coherent with each other, not just individually correct** — a refusal in one
line and a comparison of the refused quantities in the next is a gate with a door beside it.

## 6 · THE GATE

See the frontmatter for the verdict; **believe `--emit`'s exit code over this field.** Run
`export GATE_ROSTER_WHO=big-wealthTensor-27` **before** `~/Scripts/gate-selfcheck.sh` — without it
the script cannot tell a sibling's dirt in `~/Scripts` from yours, and with eight claimants that is
the difference between a named warning and a false blocker.

**`HANDOFF-GATE.md` in `claude-blackbook` is a MIRROR.** Canonical is
`~/Desktop/downloads/HANDOFF-GATE.md` (repo `darwin-everything-meta`); edit there and run
`~/Scripts/mirror-handoff-gate.sh`, which syncs *and pushes* claude-blackbook by itself.

## 7 · STUDENT-IN

`lessons.py doctrine`, then `search "<task>" --scope global,wealth-tensor`. `-26` banked three
global leaves, **curated one**, and corroborated two through the attribution loop.

**The curation is worth reading before you trust a snippet.** `-26` used the dominant-asset leaf at
student-in, then its own work narrowed the leaf's *first sentence* — "THE DOMINANT-ASSET ROUTE TO AN
ADMISSIBLE σ IS ALIVE" — which is exactly the clause `search` prints as the snippet. It had led with
an unearned word for three sessions and been corroborated to `active` on the way. **A leaf can pass
the trust loop and still be wrong in the sentence a skimming reader acts on**, because the loop
measures whether the *session* succeeded, not whether the *lead clause* held. Curated in place, one
leaf, current truth first, the intact part (the count/composition split) marked as still standing.
*When you `use` a leaf, re-read its first sentence at wrap and ask whether your work still licenses
it — `record-outcome pass` does not do that for you.*

The new ones worth knowing before you start: **a fix that clears one of N independent disqualifying
conditions clears one, not N — and the grep tell: an objection keyword that occurs exactly once in
the repo is an objection nobody answered** · **a ratio is silent about its denominator, so a share
threshold with no materiality floor selects for tiny denominators, monotonically harder as it
tightens** · **`company_tickers.json` is CURRENT registrants only — a lower bound on price-series
existence, never evidence of absence; corroborate with an independent survival instrument.**
