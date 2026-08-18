---
census_target: docs/promises-adjudicated.tsv
population: 129 adjudicated rows (paper-III 88, paper-IV 41) at parent commit 49766b5
instrument: scripts/wt154_evidence_discrimination_sweep.py
K_at_HEAD_before_repair: 25
K_D1_locate_only: 23
K_D2_under_coverage: 2
K_at_8855aba: 29
review_024_wilson95_rows: "[25, 88] of 129"
K_lands: INSIDE, ON THE LOWER BOUND
rows_repaired_in_pass: 25
manuscript_edits_required: 0
post_conditions_wt154: "10, of which 4 NEGATIVE"
post_conditions_wt155: "12, of which 6 NEGATIVE"
# FALSIFY THIS DOCUMENT, FIVE WAYS.
#   1. the instrument: `git show 49766b5:docs/promises-adjudicated.tsv` is the file before the
#      repairs. Run the sweep against it. Any K but 25 and this document is wrong.
#   2. the before/after pair: the sweep must flag bf2138f041, 75220244de, 76617b04e0 and
#      7e1c612368 at 8855aba and none of them at HEAD. Both directions are post-conditions
#      inside the script, so `python3 scripts/wt154_evidence_discrimination_sweep.py` proves or
#      breaks them on every run. RC 2 means the instrument is broken and its count means nothing.
#   3. any single repair: each of the 25 rows now names a command or a passage. Run it or read
#      it. A row whose evidence does not show what its note says is a defect in this pass.
#   4. THE CONSTRUCTION HAZARD, §5: the detectors were refined AFTER their author read rows.
#      That is the one thing REVIEW-024's sample did not do and this census cannot claim.
#      §5 states what was changed, when, and why, so the tuning is auditable rather than denied.
#   5. the disagreement: 25 is REVIEW-024's LOWER BOUND, not its point estimate. §3 says why a
#      pattern sweep must read low, and names the row that proves it.
---

# REVIEW-025 · The adjudication census — the sweep REVIEW-024 §1 assigned

*Session `wealthTensor-85` · 2026-08-18 · parent commit `49766b5`.*

> REVIEW-024 read twelve rows by hand and put an interval on 129. This pass reads all 129 by
> machine. The two do not measure the same thing, and the gap between them is the result.

---

## 1 · THE NUMBER

**K = 25 of 129** at HEAD before this pass repaired anything — 23 by D1 (locate-only), 2 by D2
(under-coverage). At `8855aba`, the file before `-84`'s repairs, the same sweep returns **29**.

REVIEW-024's Wilson 95% interval was **[0.19, 0.68]**, or **25 to 88 of 129**.

**One sentence, as commissioned: K = 25 lands INSIDE REVIEW-024's interval, exactly on its lower
bound — the census and the sample agree, but they agree at the most charitable number the sample
allowed, and §3 says why that is what a pattern sweep must return rather than a coincidence.**

---

## 2 · The instrument, and the row that forced it to have two detectors

`scripts/wt154_evidence_discrimination_sweep.py`. The question it asks each row is REVIEW-024's,
not `-83`'s:

> **Could the sentence be FALSE with this evidence unchanged?**

**D1 · LOCATE-ONLY.** No read-operation in `evidence` targets the row's own artefact — either the
evidence names no content-printing operation at all, or every read it names is scoped to a
different file. `ls -l`, `git ls-files` and `grep -l` print names, sizes and dates; `grep -n`,
`sed -n`, `head`, `cat`, `git log`, `git show` and `shasum` print content. The flag cluster is
parsed rather than matched, so `-rln` is a locator — the `l` dominates, which is exactly why
`bf2138f041` was false — while `-n` and `-c` are reads, and a bare `grep` prints lines and is a
read. **23 rows.**

**D2 · UNDER-COVERAGE.** The sentence names a sibling programme ID of the row's own artefact
(`WT-nnn`, `PRE-nnn`, `REG-nnn`, …) that appears in neither `evidence` nor `note`. **2 rows.**

D2 exists because **the fourth row REVIEW-024 filed as LOCATED is not one.** `7e1c612368`'s
evidence at `8855aba` was `grep -n WT-059 docs/LEDGER.md` — a genuine read, of the artefact the
row names, with the found text quoted in the note. No locate-detector can flag that, and
REVIEW-024's own candidate-pattern list says so in a parenthetical: *the `-l` is the tell; `grep
-n` is a read*. The commissioned post-condition and the commissioned pattern set contradicted each
other.

What was actually wrong with the row is a different thing: the sentence claims a record spanning
**WT-059 and WT-062**, and the evidence never opened WT-062. Bending D1 until it caught a `grep
-n` would have been tuning the instrument to a known answer — a rescued control, which is the
failure this whole sweep exists to avoid. Naming the second failure mode was the honest repair,
and it earns its keep immediately: D2 also caught `f43958893d`, the *mirror* row on the same
sentence, whose evidence opened WT-062 and never opened WT-059. Neither half had read the other.

**A design note, stated because it is a choice and not a discovery.** D2 fires even when the
sibling has its own adjudicated row, as WT-062 did. That is deliberate and it follows the TSV's
own header, which defines a row as the claim that a human read the artefact and found **the
sentence** borne out — the sentence, not the row's share of it. A conjunctive sentence therefore
costs two full reads, and both rows on this one now carry both entries.

---

## 3 · Why 25 is a FLOOR, and why that is the finding

25 of 129 is **19.4%**. The sample's point estimate was 5 of 12, **41.7%**. The census lands on
the interval's lower bound, and the temptation is to read that as the sample having been unlucky
high. It is not what happened, and the reason is visible in a single row.

**A pattern sweep can only find defects that have a shape. REVIEW-024's reader found one that did
not.** `7e1c612368` needed a second detector, and that detector was written *after* reading the
answer REVIEW-024 had already produced by hand. Had `-84` not drawn that row, D2 would not exist
and this census would read 23. There is no reason to believe the twelve exhausted the shapes.

So the two instruments are not competing estimates of one quantity:

| | what it measures | what it misses |
|---|---|---|
| REVIEW-024's sample, n=12 | the true non-discrimination rate, with an interval | nothing in principle; everything to width |
| this census, n=129 | the rate of *mechanically visible* non-discrimination | every shape no one has read yet |

**The census is a lower bound on the sample's quantity, and it lands where a lower bound should
land.** That the two are consistent is worth having — a census reading 90 would have meant one of
them was broken — but the honest reading is that **the file carried at least 25 rows that did not
check what they claimed to check, and REVIEW-024's estimate that the true figure is nearer 54
survives this pass untouched.** Nothing here narrows [25, 88]. The lower end is now measured
rather than inferred; the rest is still open.

**What that does to "2 of 127."** Unchanged from REVIEW-024: **[3, 47] of 129**, as an interval.
This pass repaired the evidence of 25 rows and the class of none, because every one of the 25
sentences HELD on reading (§4). Repairing an adjudication does not drain a promise; it makes the
row mean what it always claimed to.

---

## 4 · The repairs — 25 rows, 0 manuscript edits

`scripts/wt155_tsv_readnotlocate.py` (12 post-conditions, 6 NEGATIVE, backup written before the
edit, rolls back on any failure). Every one of the 25 artefacts was read this pass, on darwin.
**Every sentence held.** No `sentence`, `class`, `artefact` or `promise_id` changed — post-
conditions bind all four, which is what keeps `wt148` at RC 0 rather than reporting 25 rows STALE.

The shape of what was there, and what is there now:

| was | rows | now |
|---|---|---|
| `ls -l + git ls-files on darwin, wealthTensor-82` | 15 | the module docstring, the commit `--stat`, or the line the figure sits on |
| `same test` / `same test module` | 4 | the command that returns the sha, or the def-test count at the pin |
| `grep -rln …` (filenames only) | 4 | the test body, `sed -n`-extracted |
| `git log/cat-file …` (D2) | 1 | both commits, both `--stat`s |
| `grep -n WT-062 …` (D2) | 1 | both ledger entries |

Three findings fell out of doing it, none of which a locate-detector could have told anyone:

- **`fa005fbebe` / `af9d1b09c3` — the 62 is real and nobody had counted it.** `git show
  d655501:tests/test_edgar.py | grep -c '^def test_'` returns 42; `test_lag.py` returns 10;
  `test_lambda_sensitivity.py` returns 10. 42 + 10 + 10 = **62**, the number Paper III §11 gives.
  The three rows carrying that claim previously said `same test module`.
- **`a3511853e3` / `31fea3ed33` / `6db7b7ce3d` — the asymmetry the sentence draws between the two
  registrations is true in the commits.** `9722342` is *1 file changed, 283 insertions* — PRE-001
  alone. `d655501` is 9 files: PRE-002's registration beside `edgar.py` (622 lines) and
  `wt026_severe_test.py` (224). "Also contains the implementation" holds of the second and not the
  first, which is precisely what the bullet claims.
- **`3df66f9481` — the twin of a row REVIEW-024 already repaired.** The same sentence names
  `PREPRINT-CHECKLIST.md` and `docs/REFERENCE-POLICY.md`; `-84` repaired the checklist row and the
  policy row stayed at `ls -l`. It holds: L226 *"Pass 1 — record verified against a publisher
  page, catalogue, Crossref or issuing body"*. **A repair pass that fixes one artefact in a
  two-artefact sentence leaves the other half exactly as it was** — the `-84(iv)` lesson, arriving
  again from the other side.

### What this sweep does NOT flag, counted and named rather than dropped

- **16 rows** carry `run on darwin, wealthTensor-82; output in the session log`. That evidence
  *ran* something — a read of behaviour, not a location — but the session log is gone, so no later
  reader can re-check it. That is a real defect and a **different** one: unreproducible, not
  undiscriminating. Widening this sweep to cover it would make K incomparable with REVIEW-024,
  which scored on discrimination alone. Counted under `unreproducible` in `--json`. **Teed up for
  `-86`.**
- **18 rows** carry `git log/cat-file on darwin, wealthTensor-82`. Those commands print content,
  so the rows are reads. Terse is not the defect this sweep measures.
- **3 rows** trip D1 and are rescued by the rule in §5. **1 row** (`2f8a433aa7`) was flagged by D1
  and, on reading, its `grep -rln` turned out to be the *right* read: the sentence's claim is
  about which files carry a definition, and a filename count answers exactly that. D1 over-flags
  on count-of-files claims. It was repaired anyway — the new evidence counts the filenames *and*
  reads Paper III naming the third test, which the old evidence did not.

---

## 5 · THE CONSTRUCTION HAZARD — stated, because the sample did not have it

REVIEW-024's strongest move was committing its twelve ids with `k_of_12_false: PENDING` before
reading any of them. **This census cannot make that claim and does not.** The detectors were
written, run, and then *refined after their author read flagged rows*. Concretely, in order:

1. D1 first flagged **33**. Reading them showed six false positives: rows whose artefact is a
   programme ID (`PRE-001`, `REG-006`) where the settling read legitimately lives in another file —
   a claim about what PRE-001 *returned* is checked by reading `RESULT-001`, never the
   registration. The wrong-file arm was scoped to artefacts that ARE files. **−4.**
2. Two rows cited a named green test (`tests/test_pin001_code_state.py::…`) against a module.
   Asserting things about other modules is a test's entire job, so a test reference was made
   unscoped. **−2.**
3. Two class-**N** rows tripped D2 on a §5.3 table header naming both PRE-001 and PRE-002. Class N
   means the sentence asserts nothing that could fail independently, so there is no conjunction to
   under-cover. D2 now skips class N. **−2.**
4. The rescue rule was widened from {sha, digest, §ref} to include decimal figures shared with the
   sentence, after `bb9fba4abf` — whose note carries α̂ = 0.4077 → the paper's 0.408 — was flagged.
   **−1 (net, with the arm changes above).**

**33 → 25.** Every one of those changes narrowed the criterion, and every one was made after
looking. A reader who thinks any of the eight is a defect being explained away should re-run the
sweep with that change reverted; the four rows in §2's before/after pair hold under all of them,
which is the only thing the post-conditions can prove and is less than blindness would have
proved.

**The rescue rule**, for completeness: a row that trips D1 is rescued when its `note` carries a
sha, digest, section reference or decimal figure that also appears **verbatim in the sentence**.
`6efe91d805`'s evidence is the bare back-reference `same test`, but its note reads *"pinned at
b9089c7"* and the sentence pins `lambda_sensitivity.py` at b9089c7 — the sentence cannot be false
with that note unchanged, which is why REVIEW-024 scored it TRUE by hand. The shared-token
requirement is what stops it rescuing everything: *"present, 134 lines"* carries a number too, and
134 is not a number any sentence makes a claim about.

**The consequence for the programme, stated plainly.** REVIEW-024 §4 called the census "the last
thing the sample made cheap," and it was right. **Both cheap substitutes are now spent**: `-82`'s
prediction, `-84`'s sample, `-85`'s census. Each was cheaper than the two-independent-readers
design and each measured something narrower than it. There is no third substitute, and this
document is the reason why — a sweep can only ever find the shapes someone has already read.

---

## 6 · State at wrap

| gate | result |
|---|---|
| `wt154_evidence_discrimination_sweep.py` | **RC 0** (10/10 post-conditions, 4 NEGATIVE) |
| `wt155_tsv_readnotlocate.py` | **RC 0** (12/12 post-conditions, 6 NEGATIVE) |
| `wt148_promise_sweep.py` | **RC 0** — paper-III 88 of 88, paper-IV 41 of 41 |
| `wt133_crossref_sweep.py` | **RC 0** |
| `handoff_gate.py --coach` | baseline — paper-III 5 conduct / 0 concessive, paper-IV 1 / 0 |

Manuscripts: untouched. `#scope` unchanged — Papers I and II remain parked, deliberately, for the
fourth consecutive pass.
