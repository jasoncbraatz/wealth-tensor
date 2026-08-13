---
project: wealth-tensor
gh_sha: bebeb524e5e8432970d51074be8db8fe7e737287
updated: 2026-08-13
session: wealthTensor-18
gate_passed: true
gate_version: "2.50"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Run
`python3 scripts/handoff_gate.py --check` before trusting this file.*

## 0 · TRANSPORT — darlish, zero-bridge

```
curl -s https://system.europeanflorist.com/dsh/darlish-up -o /tmp/darlish-up && chmod +x /tmp/darlish-up && /tmp/darlish-up
```

Post the printed `DARLISH-ENROLL v1 id=… fp=…` line **exactly** as a comment on Asana task
`1217316841710435` via the session's Asana MCP, then run `/tmp/darlish-up` again to collect.
First collect has worked `-06` through `-18` without exception.

**`-18` is the proof the pipe survives darwin going away entirely.** Jason took a macOS security
update mid-session and rebooted the Mac underneath a running session. `dx --selftest` passed
immediately afterwards, via the in-process WSS, with **no re-enrolment and no re-run of
`darlish-up`**. `-17` proved darlish survives the bridge dropping; `-18` proves it survives the
host rebooting. **Never restart anything to fix darlish, and do not re-enrol after a reboot —
just call `dx`.** The one thing you DO lose to a reboot is your roster row: re-run `roster join`
and `roster claim`.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-19 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-19 --resource wealth-tensor'
```

`export LESSONS_CONTRIBUTOR=opus` **before any `lessons.py add`**. Four leaves banked this
session — three global, one project-scoped — all in §2 and §6 below.

**Never inline a multi-line message in a `dx '...'` argument.** Write a local file, `--put` it,
`git commit -F`. Used four times this session, no incidents; the same trick works for
`lessons.py add`, whose text is full of apostrophes — **write a `bank.sh`, `--put` it, run it.**
`dx --get` fails on binary — base64 both ways. Quote remote paths. Exit 3 = never reached darwin,
safe to re-run; exit 4 = started, check state first. **Use `./.venv/bin/python`** — `python3 -m
pytest` dies at collection because scipy lives only in the venv. **276 tests, ~40 s** (was 271).

**The roster contention warning naming YOU is still noise.** Carded on State Machine
`1217420907841952`. Do not spend a turn on it.

### THE THREE THINGS THAT COST `-18` A RUN EACH — read this before writing any instrument

All three are the same mistake: **reconstructing registered machinery from its signature instead
of copying its call site.** Each cost a full 10–12 minute crawl.

1. **`extract_events` defaults to `onset_rule="streak"`, which is PRE-001. The registered
   PRE-002/REG-003 sample is `onset_rule="peak"`.** Reconstructing the call produced ~350 events
   against a published 695 and would have been reported as an effect of the change under test.
   The call site is in `wt089_harvest.py:83` — `include_annual_attributed=True,
   onset_rule="peak", signal="revenue"`. **Copy it. Do not retype it.**
2. **`peak_onset` returns a TUPLE `(onset, censored)`**, so `if E.peak_onset(...) is not None`
   is always true and silently inflates the eligible-quarter risk set. The real logic is
   `wt089_riskset.eligible_quarters` and it is fourteen lines. Copy those too.
3. **ALWAYS RUN THE UNCHANGED ARM AS A CONTROL, IN THE SAME PASS.** It is the only thing that
   catches 1 and 2. `wt092_ladderC.py` runs both tag lists over one crawl for exactly this
   reason, and the control arm coming back at 4.01× against a published 4.12× is what proved the
   harness sound. A comparison across two runs would have proved nothing.

### `severity.check`'s witness contract, stated once because `-18` got it wrong first

The witness is a **zero-argument callable returning the SAME PREDICATE evaluated on a world where
the claim is FALSE**, and it must come back **falsy**. Returning the raw quantity (a count, a
slope) makes the guard VACUOUS and the run dies with `PHANTOM TAG`. It caught one of mine
immediately, which is the system working. And **a witness world must be RUNNABLE**: two of mine
crashed because the no-absorption comparison world had zero censored observations and the
estimator returned `None`. Recentre the falsifying world to the same censoring rate.

### Editing the manuscript

`scripts/patchkit.py`, `apply_edits`, never `sed`, never a hand-rolled `src.count(old)` loop. Six
anchors this session across two edit scripts (`wt092_edits_reg006.py`, `wt092_edits_44.py`), one
anchor failure, nothing written on the failure — the file wraps its paragraphs, so **copy the
anchor out of a `dx --get` copy WITH ITS LINE BREAKS** and dry-run in the container first.

**And a failure mode patchkit cannot see: PROSE THAT NAVIGATES POSITIONALLY.** §4.4 said "The
column beside it"; inserting a column pointed that sentence at the wrong column and no guard
would ever have flagged it. **Before adding a row, column or list item, grep the surrounding
prose for "the right-hand", "the column beside", "the first", "the latter", "above", "below".**

## 1 · WHAT HAPPENED — THE ORDERING RULE IS TWO CHANNELS, AND OUR OWN INSTRUMENT WAS HALF BLIND

`REG-006` registered and pushed (**6a5094a**) before a line of `wt092` existed;
`scripts/wt092_sequencing_vs_coupling.py` — **8 severe · 0 definitional · 0 vacuous**;
`wt092_ladderC.py` runs `wt089`'s registered `instrument_b` unmodified. **276 tests green (was
271)**; coach ratchet unchanged at **6**; concessive openers **0**; gate PASS; tree clean.

§5.4 conceded that the sequencing of the impairment standards might manufacture the measured
departure from diagonality. **The concession is misattributed, understated in scope, and
internally two-signed.**

> The rule is **ASC 350-20-35-31**, not ASC 360 (ASC 360-10-35-27 carries the reciprocal
> cross-reference). **ASC 350-20-35-32** extends it to *all* assets tested, so it governs the
> intangible cells — §5.4's strongest — and not only property. Text unchanged from FAS 142 ¶29
> (2001) and absent from the amendment instructions of ASU 2011-08, 2017-04 and 2021-03, so it is
> stable across the whole window.

It **creates joint testing** (35-3C(f) names "the testing for recoverability of a significant
asset group within a reporting unit" as a goodwill triggering event) and **suppresses joint
recognition** (the other charge is recognised first and reduces the reporting unit's carrying
amount before the comparison at 35-2/35-8). F2 reproduces **KPMG Handbook Example 4.4.10**
exactly: \$850 of prior charges converts a would-be \$700 goodwill impairment to **\$0**.

**Under the ordering alone the two charges are SUBSTITUTES at the margin. §5.4 observes them as
COMPLEMENTS at 4.12× and 2.02×.** The mechanical reading the paper conceded predicts the opposite
sign on its recognition channel. That does not close the identification — co-testing is real and
may dominate — but the concession named the one channel that runs *with* the finding.

## 2 · THE DEFECT: A TAG THAT MATCHED NOTHING, FOR THE LIFE OF THE PROJECT

`edgar.py`'s registered `TIER_TAGS[0]` named **`ImpairmentOfLongLivedAssetsHeldAndUsed`**, which
is **not a us-gaap element**: 404 from the frames API every year, **zero facts across all 307
firms of the registered sample.** The element that exists is `…HeldForUse` — **2,202 facts across
126 of our own firms**. Tier 0 was seeing **52.6%** of retail and **44.4%** of computer-services
firms, and the cause was a spelling.

**Ladder C re-derived REG-003 §4 with the omission repaired.** Same seed, same 10,000 draws, same
risk set, both arms on one crawl:

| universe | original | **corrected** | events |
|---|---|---|---|
| retail | 4.01× | **4.01×** | 243 → 303 |
| computer services | 2.01× | **2.10×** | 439 → 476 |

**The headline survives.** The defect cost power, not validity — which `REG-006` §1 registered as
the expected mechanism *before* the run, and the alternative (half a tier quietly biasing a
published number) was live until the ladder returned. **Every cell not involving tier 0 is
identical across the two arms to two decimals**, which is the internal control.

**One published sentence does not survive.** §5.4 said property-with-goodwill "is the one cell
that replicates its magnitude across two sectors" at 4.35× and 4.03×. Repaired it is **3.99× and
2.17×**, the second no longer Holm-significant. It rested on **four observations in one sector
and five in the other.** The cells that *do* replicate are the two intangible-with-goodwill ones
— exactly the cells 35-32 brings under the rule. §5.4 and Limitation 9 amended, three ledger rows
added to §7.

**The guard is mechanised**: `tests/test_tag_resolution.py`, five tests, offline, against
`data/tag-resolution-audit.json`. **`TIER_TAGS` is NOT edited** — PRE-001's constants are a
contract and `test_edgar.py` guards them — the correction is additive in **`TIER_TAGS_REG006`**,
and a test pins the dead element so the finding cannot be quietly un-found.

**The lesson, banked globally.** A tag matching nothing is indistinguishable, downstream, from a
tag matching nothing *in this sample*: both contribute zero and neither raises. That is `-16`'s
underflowed tail and `-17`'s truncated tail in a third costume — **a guard that cannot tell EMPTY
from ABSENT** — and it is the first of the three to ship a test rather than a paragraph.

## 3 · WHAT FAILED, AND IT WAS REGISTERED TO

**Ladders A, A3 and R all failed, and F5 voids R outright.** POST slopes are +0.010 and +0.665
where a negative was registered; the retail placebo date moved the slope **further** (−2.245)
than the true one (−1.599), so the regime contrast is a time trend; single-segment firms ran the
wrong way against multi-segment.

**F4b explains all three and was registered.** On synthetic data carrying both channels, the
estimator recovers **0.508** of a true difference of **1.000** — half the signal gone in a world
built to contain it — and `REG-006` §4 A2 registered entity aggregation as a further attenuation,
monotone in the number of reporting units, which XBRL does not disclose. **The design was
under-powered by construction and the registration said so before the data.**

**F4b as coded also failed, and that failure was ours.** It demanded the difference equal 1.000
to within 0.25 — a magnitude claim §4 A2 had already declared a *lower bound*. **The code
contradicted the registration it was implementing.** Banked globally: diff every falsifier against
the registration's own hedges before running, and never widen a threshold to make one pass.

**The Q4 guard fired twice and was right twice.** As first coded it refused to report anything —
54.2% unresolved against a 15% ceiling — and both causes were the guard being wrong, both
resolvable from the registration's own words: firm-years with **no goodwill at all** are not
"unresolved", the test does not apply to them; and the registered condition is an aggregate
"**that could contain** an untagged goodwill component", so only the residue above the
materiality floor is a hiding place. Corrected: **43 of 1,079, 4.0%**. The strict count (497) is
printed beside it so nothing is hidden.

## 4 · JASON'S RULINGS — DO NOT REOPEN

- **§4.4's table is SETTLED.** Ruled `-18`, after a two-round conversation. He took **both**
  moves: the α̂ = 0.408 column **and** the "the calibration" label on the α = 0.05 column. His
  reasoning is worth carrying — the label is what stops the calibration column reading as
  vestigial once a measured column sits beside it, and neither move survives alone. **Off the
  at-bat list permanently. Do not re-raise it.**
- **The `## References` provenance block STAYS AS IT IS.** Ruled `-16`, directly. Settled.
- His standing test for the paper, stated `-18`: **"will the econometrician be able to follow the
  line of thought?"** Reader before referee. Across three papers the pieces have to fit like Lego.

## 5 · THE PAPERS

**Paper III** — `docs/papers/paper-III-dual-tensor/paper-III.md`, **2,624 lines** (was 2,600).
Numbering preserved: 2 `#`, 15 `##`, 29 `###`, 17 `---` — unchanged.

| § | what changed |
|---|---|
| 4.4 | the α̂ = 0.408 column, the calibration label, and the positional reference re-anchored by name. **Jason's ruling. Closed.** |
| 5.4 | the concession rewritten: ASC 350-20-35-31, 35-32's scope, and the two channels; the pairwise-cells sentence corrected for tier 0 |
| 9 · Limitation 9 | the sequencing named correctly and identified as two channels of opposite sign |
| 7 | **three ledger rows** — the off-diagonality surviving the corrected tier, the standards' own suppression, and the entity-level test failing |

## 6 · THE AT-BAT, RANKED

1. **REG-007 · THE TRIGGERING-DISCLOSURE INSTRUMENT.** This is now #1 because `REG-006` closed
   every cheaper route to it. The discriminator §5.4 named is the triggering *disclosure*, not the
   charge. **8-K Item 2.06 is DEAD as a population** — roughly 100 filings a year against ~1,400
   firms recording an impairment, because the Item's instruction exempts a conclusion reached in
   connection with the next periodic report and a **2013 SEC C&DI** extended the exemption to
   conclusions that merely *coincide* with it. **The live route is "triggering event" text in
   10-K/10-Q**: 1,235 such 10-Ks in 2023, 764 of them also containing "goodwill impairment"; EDGAR
   full-text search supports phrase-AND and `data.sec.gov/submissions/CIK…json` exposes
   `filings.recent.items` for clean 8-K item codes. **Register before deriving. Crawl in the
   cloud** — both `data.sec.gov` and `www.sec.gov` are reachable there and darwin's disk is at 95%.
2. **THE TWO CELLS THE REPAIRED INSTRUMENT CAN NOW SEE, AND THE PAPER STILL REPORTS AS ZERO.**
   With a half-blind tier 0, retail's PP&E × finite-lived and PP&E × indefinite-lived cells read
   **0.00× (p = 1.0000)** and **3.27×**. Repaired they are **7.70× (p 0.012)** and **6.33×
   (p 0.0048)**. `RESULT-REG-006` §2.2 reports them; **§5.4 does not**, because §5.4 reports the
   registered committed sample and these come from the repaired re-derivation. That is a
   defensible scope line and it is also a live question: a cell printed as a measured zero that
   is actually a significant coupling is the same empty-versus-absent defect wearing a fourth
   costume. **Decide it deliberately; do not let it drift.**
3. **THE σ-AND-LIFETIME RESULT STILL NEEDS NEW DATA.** Realised return volatility and disclosed
   useful lives are not in this sample; Companion C's severity dispersion by class has
   overlapping intervals. **Do not proxy** — a quantity sharing σ's name and not its meaning is
   the WT-038 error, a three-time payer.
4. **THE PRIOR-ART GAP IS REAL AND UNCONFIRMED.** A subagent found **no** paper separating
   standard-imposed sequencing from economic co-movement, in impairment or any other accounting
   context, and **no** accounting literature on Item 2.06 at all — but it searched the open web
   only, not Scholar/SSRN/JSTOR, and could not read the full text of any paper in its shortlist.
   **Before claiming novelty, check Amel-Zadeh, Glaum & Sellhorn (2023), *European Accounting
   Review* 32(2): 415–446** — the field's survey. If it already flags the sequencing gap, the
   framing changes. Riedl (2004) *TAR* 79(3): 823–852 is the nearest neighbour; Ramanna & Watts
   (2012) *RAST* 17(4): 749–780 is the reverse-sign version of the same identification problem.

## 7 · DO NOT

- **ASK A SUBAGENT FOR ITS UNVERIFIED LIST EXPLICITLY.** It was the most useful output of both
  subagents this session — one of them refuted a paragraph number I had asserted, corrected my
  tag name before I built on it, and flagged that "dollar for dollar" appears in no source. **Do
  not let a plausible search snippet be promoted to a verified fact.**
- Do not read §5.4 as a rescue of PRE-001. REG-003 §7 ruled it out in writing before the number
  existed; nothing in REG-004, REG-005 or REG-006 touches it.
- Do not restore "PRE-001 was doomed by the φδ confound" — false; wt082, wt083, wt088 E7.
- Do not remove the Bateman, Nerlove or Beaver & Ryan concessions. Do not restore "global rather
  than local" to Kuan, the unordered-pair statement to Bellman & Åström, or the bias/lag DESIGN to
  Ryan (1995). Do not reopen Griliches (1967) — closed with evidence.
- **DO NOT REOPEN the `## References` provenance block or §4.4's table.** Both ruled by Jason.
- **DO NOT POLISH §4.9, §4.10 or §5.4.** §4.10 reports a registered result; §5.4 was amended
  surgically this session under REG-006 §7 and is otherwise closed.
- **Do not edit `TIER_TAGS`.** It is PRE-001 and it produced the published RESULT-REG-003;
  `test_edgar.py` and `test_tag_resolution.py` both guard it. The correction lives in
  `TIER_TAGS_REG006`.
- Do not quote a single "recognition rate" — §4.10 shows the name covers three quantities 15%
  apart at a three-year life. Do not quote a single "effective recognition rate" — α_eff is a
  function of δ.
- Do not report a δ-rectangle share from REG-004 or REG-005 — both complements are empty and both
  were withheld deliberately, in advance.
- **Do not read ladders A/R/A3's failure as evidence that absorption is absent.** F4b shows the
  estimator loses half the signal in a world built to contain it. A null from an instrument that
  registered its own under-powering is not a finding about the world.
- Do not hand Jason a ranked list of problems as the deliverable. Do not run a pure-teardown pass.
- Do not invoke Mayo or error-statistical philosophy as a warrant. Pragmatic justification.
- Do not ask him to submit anything. Never add a free parameter to absorb an objection.
- Do not rewrite or summarise the charter inside a handoff.
- Adding a section means DELETING conduct narration elsewhere, not refreshing `.coach-baseline.json`.
- **gate-selfcheck is PASS.** G-AE failed at the start of `-18`'s wrap — `com.braatz.flowers-dupe-verify`
  was a loaded launchd job whose plist existed nowhere but darwin — and was fixed, not deferred
  (`darwin-mac-ops` **782359d**). The three `HANDOFF-floristAlix-2.md` warnings are report-only
  handoff-lint on another project's document. **If the GATE fails for you it is new.**

## 8 · STUDENT-IN, AND THE ONE STEP `-17` AND `-18` BOTH SKIPPED

```
python3 ~/repos/claude-blackbook/lessons.py doctrine
python3 ~/repos/claude-blackbook/lessons.py search "<the task>" --scope global,wealth-tensor
```

**Run the search BEFORE you write anything.** `-17` skipped it and said so; `-18` skipped it too
and ran it only at teacher-out — where it confirmed no existing leaf covered either finding, which
is a fine outcome but was luck rather than method. Two of the three run-costing mistakes in §0
would have been caught by a leaf that now exists. **Then corroborate what you used:**
`lessons.py use <id> --task <tag>` at student-in, `lessons.py record-outcome <tag> pass` at wrap.
