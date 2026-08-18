---
audit_target: docs/promises-adjudicated.tsv
population: 129 adjudicated rows (paper-III 88, paper-IV 41) at parent commit 8855aba
seed: 20260818
draw: "random.Random(20260818).sample(sorted(promise_id), 12)"
sample_committed_before_adjudication: true
sample_commit: c13df88
k_of_12_false: 5
k_of_12_false_sentence: 1
false_rate_wilson95: "[0.193, 0.680]"
false_sentence_rate_wilson95: "[0.015, 0.354]"
rows_repaired_in_pass: 6
manuscript_edits_required: 1
# FALSIFY THIS DOCUMENT, FIVE WAYS.
#   1. the draw: re-run the four lines in §0 against the TSV at 8855aba. Any other twelve ids and
#      this document is wrong. The ids were committed at c13df88 with k PENDING, BEFORE §2 existed.
#   2. the criterion: §1 states it and states the weaker one it subsumes. Score the twelve under
#      -83's literal rule instead and k moves — §1 gives that number too.
#   3. any single verdict: §2 gives, per row, the command or the read that produced it. Run it.
#      A row scored FALSE whose evidence DOES discriminate the sentence is a defect in this audit.
#   4. the repairs: scripts/wt153_paperIV_s1_record_not_command.py (10 post-conditions, 4 NEGATIVE,
#      refuses on a moved anchor) and scripts/wt153b_tsv.py (14 post-conditions, 3 NEGATIVE).
#      Both roll back on failure. RED-PROOF is recorded in §3.
#   5. the interval: 5/12 with a Wilson 95% interval. If you judge n=12 too small to bound
#      a 129-row file, §1 states that objection and answers it in the only honest way available.
---

# REVIEW-024 · The adjudication audit — putting a rate on `docs/promises-adjudicated.tsv`

*Session `wealthTensor-84` · 2026-08-18 · parent commit `8855aba`.*

> `-83` falsified ONE targeted row and it was false. That is a numerator with no denominator.
> This pass drew a random sample, committed it before looking, and put an interval on it.

---

## 0 · THE DRAW — committed before a single row was adjudicated

**Population.** 129 adjudicated rows. (`-83`'s handoff said 128; the true count at `8855aba` is
**129** — `wt148` prints `129 adjudicated`. The audit uses the file, not the handoff.)

**Seed `20260818`.** Procedure, verbatim and reproducible:

```python
ids    = sorted(promise_id for row in tsv if not row.startswith('#'))
sample = random.Random(20260818).sample(ids, 12)
```

**THE TWELVE, listed before any of them was checked.** This section was committed as its own
commit — `c13df88`, front matter reading `k_of_12_false: PENDING` — so the sample cannot have been
chosen after reading. A sample chosen after reading is not a sample.

| # | promise_id | paper | artefact | class as filed |
|---|---|---|---|---|
| 1 | `bf2138f041` | paper-IV | `test_a_flat_gini_does_not_mean_a_bounded_one` | H |
| 2 | `3bdab165bf` | paper-III | `REG-005` | H |
| 3 | `ec8622f081` | paper-IV | `ADR-001` | H |
| 4 | `75220244de` | paper-IV | `docs/papers/PREPRINT-CHECKLIST.md` | H |
| 5 | `6efe91d805` | paper-III | `src/wealth_tensor/lambda_sensitivity.py` | H |
| 6 | `aebdfa4d76` | paper-III | `data/pre-002-riskset.json` | H |
| 7 | `fd2b77f988` | paper-III | `RESULT-REG-008` | H |
| 8 | `c487d43b12` | paper-III | `PRE-002` | N |
| 9 | `76617b04e0` | paper-IV | `src/wealth_tensor/lag.py` | H |
| 10 | `9add6ff45d` | paper-III | `93a159b` | H |
| 11 | `7e1c612368` | paper-III | `WT-059` | H |
| 12 | `388811fc0a` | paper-IV | `REG-013` | H |

---

## 1 · The verdict

**k = 5 of 12.** Wilson 95% interval **[0.19, 0.68]** — between **25 and 88** of the 129 rows.

**One sentence on what that does to “2 of 127.”** Of the 5 false rows, **one carried a false
sentence**; the other four carried true sentences that nobody had actually checked. So the
promise class on Papers III and IV is not drained to 2 of 127 but to somewhere in
**[3, 47] of 129** — the interval, not the point, because 1 of 12 is what the sample supports
and a point estimate here would be the same overconfidence the audit was built to find.

### The criterion, stated plainly, and the weaker one it subsumes

`-83` scored a row FALSE when the adjudicator *checked a different artefact from the one the
sentence names*. Applied literally to these twelve, that catches **one** — row `388811fc0a`, where
the note asserts a property of §10 that §10 denies in bold.

This audit uses the criterion the TSV's own header prescribes, generalised one step:

> **A row is FALSE if the `evidence`, run or read, does not DISCRIMINATE — if the sentence could
> be false with that evidence unchanged.**

`-83`'s rule is the special case where the non-discriminating evidence happens to point at another
file. The four extra rows this catches all share one shape, and it is not `-83`'s:

> **THE ADJUDICATOR LOCATED THE ARTEFACT INSTEAD OF READING IT.**

`ls -l` returning *“present, 134 lines”* is a true note. It is also true of a checklist that
prescribes nothing. `grep -rln` returning a filename is a true note, and equally true of a test
that asserts the opposite of what the sentence says it forbids. **These rows record that the
artefact exists. The sentence claims what the artefact DOES.** Three of the four trace to one
adjudication session — `wealthTensor-82`, evidence column `ls -l + git ls-files on darwin` — which
is the enumeration pass itself: the session that built the instrument adjudicated part of its own
output by directory listing.

### The objection, answered

Twelve is a small denominator and the interval is wide — [0.19, 0.68] does not distinguish “one row in
five” from “two rows in three”. That is the honest state of knowledge and the interval says so.
What twelve rows *do* settle is the question that was actually open: **whether the adjudications
are reliable enough that “2 of 127” can be read as a measurement.** The lower bound is 0.19. At
the most charitable end of the interval the file still carries 25 rows that do not check what they
claim to check, and the cheapest reading of “2 of 127” — that the promise class is drained — is
not available at any point inside it.

**What would settle it.** The four location-only rows are mechanically findable: the evidence
column matching `ls -l`, `git ls-files`, `grep -rl`, or `same test` with no read recorded. That is
a sweep, not a sample, and `-85` can run it over all 129 rows for the price of one script. **The
sample was needed to learn the shape; the shape is now cheap to enumerate.** §4 assigns it.

---

## 2 · The twelve, adjudicated

The question each row was asked is NOT *“is the sentence true?”* — `-83`'s false row passed that
one. It is: **does the `evidence` column bear on what the sentence asserts about the artefact
the sentence names?**

**1. `bf2138f041` · paper-IV · `test_a_flat_gini_does_not_mean_a_bounded_one` · filed H — ❌ **FALSE****

evidence is `grep -rln` — a filename list. The sentence says what the test FORBIDS; a filename cannot show that. (Read: the body does forbid it. Sentence holds, row did not check it.)

**2. `3bdab165bf` · paper-III · `REG-005` · filed H — ✅ TRUE**

REG-005 §2 carries F1–F4 and §5 carries ladders I, P, W, S, N — four and five, at the sections the evidence names.

**3. `ec8622f081` · paper-IV · `ADR-001` · filed H — ✅ TRUE**

ADR-001 §Decision reads *“Split into four papers. One claim each. Evidence allocated without overlap.”* — the purpose the sentence attributes to it.

**4. `75220244de` · paper-IV · `docs/papers/PREPRINT-CHECKLIST.md` · filed H — ❌ **FALSE****

evidence is `ls -l`, note is *“present, 134 lines”*. The sentence claims the checklist PRESCRIBES verifying bibliography against live sources. Existence is not prescription. (Read: L42 does prescribe it. Sentence holds.)

**5. `6efe91d805` · paper-III · `src/wealth_tensor/lambda_sensitivity.py` · filed H — ✅ TRUE**

`git log -1 --format=%h b9089c7 -- src/wealth_tensor/lambda_sensitivity.py` → `b9089c7`. The evidence IS the sentence's own command.

**6. `aebdfa4d76` · paper-III · `data/pre-002-riskset.json` · filed H — ✅ TRUE**

`shasum -a 256 data/pre-002-riskset.json` → `60627429…436cce`, character for character what §11 prints.

**7. `fd2b77f988` · paper-III · `RESULT-REG-008` · filed H — ✅ TRUE**

§2.2 prints 0/281 and 1/363 and the sentence follows. *But the note's “Both figures at the section cited” overstates by one addition* — “one in 644” is the two disjoint strata summed and is printed verbatim at §1's P2. Note corrected in pass; the row still discriminates.

**8. `c487d43b12` · paper-III · `PRE-002` · filed N — ✅ TRUE**

class N is right: the sentence dates a programme RULE against PRE-002 and asserts nothing of PRE-002 that could fail on its own. §5.1 is where it sits (L1206).

**9. `76617b04e0` · paper-IV · `src/wealth_tensor/lag.py` · filed H — ❌ **FALSE****

evidence is `ls -l`, note is *“present, 164 lines”*. The sentence claims lag.py is REGENERATED BY `wt027_report.py`. A line count is silent on that. (Read: wt027_report.py line 1 says exactly that. Sentence holds.)

**10. `9add6ff45d` · paper-III · `93a159b` · filed H — ✅ TRUE**

`git cat-file -t 93a159b` → commit, 2026-08-13, REG-006, and its stat includes `src/wealth_tensor/edgar.py` (+21) — the post-pin move the sentence discloses. The sentence's second clause (`TIER_TAGS` byte-identity) is a SEPARATE row, `c9994614d2`, carrying a real test.

**11. `7e1c612368` · paper-III · `WT-059` · filed H — ❌ **FALSE****

evidence greps WT-059's line number and never opens WT-062 — which is the entry carrying the sentence's “two entries” and its “the search was wrong”. (Read: WT-062 is titled *“Two false conclusions in one session”* and names them. Sentence holds.)

**12. `388811fc0a` · paper-IV · `REG-013` · filed H — ❌ **FALSE****

**the sentence is false, and this is the one that matters.** Note asserts *“§10 does name a command for each.”* §10 says, in bold: *“Those files, not a command, are the record of §6.”* §10 also says *“Nothing in this repository re-derives §6's figures from committed data, and this bullet said ‘regenerate’ until wealthTensor-82.”* §10 was repaired at `-82`; §1's promise ABOUT §10 was not.

---

## 3 · The repairs, and the red-proof

**One manuscript edit.** `scripts/wt153_paperIV_s1_record_not_command.py` rewrites Paper IV §1 so
that what it promises of §10 is what §10 delivers:

> *…and §10 names the **record** for each: §6's are `REG-013`'s, and its record is the committed
> output of that run rather than a command, because the instrument re-queries a live database;
> §5's and §8's are the output of the fourth paper's apparatus, which is still in this repository
> and still runs.*

Ten post-conditions, **four NEGATIVE** (the old clause is gone; the forbidden string occurs
nowhere; no defensive opener was added — ABSORB is illegal under CO-AUTHOR-CHARTER §2; the
em-dash count is unchanged). It refuses on a moved anchor and rolls back on any failure.

**RED-PROOF, on the real tree.** Rewording the sentence took `wt148` to **RC 1**, reporting
`388811fc0a` STALE and one unadjudicated promise `f06ce25844` — exactly as designed. `wt153b_tsv.py`
retires the stale row, adjudicates the replacement **R**, and re-adjudicates the four
location-only rows plus `fd2b77f988`'s overstated note. Fourteen post-conditions, three NEGATIVE.
`wt148` returns **RC 0**.

**Every repaired row's new evidence names a read, and its note says what the read showed.** That
is the whole repair: the rows were not wrong about their artefacts, they were silent about their
sentences.

---

## 4 · What `-85` inherits

**The sweep this sample makes cheap.** Four of five false rows are detectable by pattern: an
`evidence` column that locates rather than reads. A script that flags every row whose evidence
matches `ls -l`, `git ls-files`, `grep -rl`, `shasum` without a printed digest, or a bare `same
test` back-reference, over all 129 rows, converts this sample into a census. `-84` deliberately
did **not** write it: the sample had to be scored blind first, or the pattern would have been
chosen to fit the rows it found.

**What this pass did NOT do, on purpose.** No fourth reader-pass. `#scope` was not widened to
Papers I and II — still parked, still deliberate.

