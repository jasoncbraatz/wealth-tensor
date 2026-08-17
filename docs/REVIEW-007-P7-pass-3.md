# REVIEW-007 · `P7` CONVERGENCE PASS 3 — Paper II, read independently for the first time

*wealthTensor-64 · 2026-08-17 · the third `P7` pass, and the first one aimed at the paper nobody
had read. **Nine new findings, all nine repaired.** `II-2` and `II-3` were re-found independently
and stay `DECISION-001`-blocked. Two of the nine are `REVIEW-004` §A3 items that have been live for
five days under a commit message that reads as though A3 was served. And the pass turned up two
things about the **review apparatus** that are worth more than the nine: `PIN-001`'s class repair
watches one manuscript of four, and the handoff gate never runs a test suite.*

---

## 0 · What this pass is

`-62` drained a backlog. `-63` re-graded those repairs and independently read Paper IV and Paper
III's appendix. Paper II had one repair re-graded and nothing else — it had **never** been read end
to end asking `P7`'s question, which `WT-091` says is the only thing that counts as a pass.

So: Paper II, 449 lines, front matter through the closing citation note, with every numerical claim
checked against the committed code rather than against the printed table.

**Result: 9 new findings, 9 repaired. `§3` reproduces byte-exact from its named command. Paper II's
consecutive-zero count stays 0 — this pass found too much to be a zero, which is the answer
`WT-091` predicted for a paper whose quiet was the quiet of not being read.**

---

## 1 · THE NINE, all repaired

| id | site | the defect | how it was settled |
|---|---|---|---|
| `II-4` | §5 lim. 5 | *"the results are means over a tail window **across seeds**"* — they are **one** seed. `RedistributiveEconomy(seed=0)` is the default and `wt030_report.py` never passes another. `seed` occurs once in the whole manuscript, in this sentence. | code |
| `II-5` | §7 | the pin's defining clause — *"**d655501** — the last commit touching `src/`"* — is **false**, and is the `PIN-001` sentence verbatim. See §3. | git |
| `II-6` | §3.4 | the unopposed run reads *"Gini 0.977 … top decile 0.988"* against §3.1's **0.994 / 1.000** for the same object. `REVIEW-004` §A3 flagged the gap and said *"nothing explains"* it. The code explains it: `is_bounded`'s docstring reports 0.977 *"at N = 800 and **600 periods**"*, and the paper runs `T = 1200` throughout. A stale-era number under a paper-wide horizon declaration. | code + run |
| `II-7` | §3.4 | *"bounded runs sit at 0.19–0.50, condensed runs at 0.99–1.00"* — refuted by the paper's own sweep **on either reading of the unnamed statistic**. As Gini, bounded runs span **0.000–0.891**; as top decile, **0.100–0.861**. `0.19–0.50` is neither, and covers only the four stock rows at *r* ≤ 0.100. | run |
| `II-8` | §1 c2, §3.1 | *"which the simulation reproduces to within 5 % **and which the test suite asserts**"* — both halves wrong. The residuals are **−4.4 %, −4.9 %, −6.8 %**, so the *r* = 0.025 row is **outside** 5 %; and the suite asserts `rel=0.10`. `REVIEW-004` §A3's second item, live five days. | arithmetic + code |
| `II-9` | §1, closing note | two places assert *"§3.1 mentions zakat"*. §3.1 does not — `zakat` occurs at lines 63 and 92 (§1) and 445 (the note), and **zero times** in §3.1. The house-style pass took it out and left both pointers. | normalised grep |
| `II-10` | §1 c5, §7 | *"the companion paper"* denotes **two different papers**: §7's SMD guard constrains the price-formation manuscript, §3.2's *"companion work on the reporting layer"* is Paper III. Neither is named or referenced, and the first has been **superseded by its own internal referee** with no disclosure. | corpus |
| `II-11` | abstract | *"an open repository with 18 tests"* attributes a module-scoped count to the repository, which holds **572** test definitions. §1 and §7 both scope it correctly; the abstract is the one site that does not, and `-58`'s derivation instrument asserts §7's phrasing, so **no test can see it**. This is `REVIEW-004` §A3's third item in its unrepaired half. | code + instrument |
| `II-12` | §3.3 | neither sweep states its configuration. Both are stock at *r* = 0.025 (`wt030_report.py`); a reader can only reverse-engineer it from the 0.443 that matches §3.1's row. | script |

**`II-2` and `II-3` were re-found from scratch before `REVIEW-005` §2 was read** — the abstract's
*"order of magnitude in compression"* against §3.1's *"in κ"*, and *"statistically
indistinguishable"* for something the model forces at ρ = 0. Both stay unrepaired for
`REVIEW-005`'s reason, which is still the right one: they are edits of whichever `DECISION-001`
option is ticked. An independent read arriving at the same two items by a different route is worth
recording as corroboration.

---

## 2 · `REVIEW-004` §A3 WAS SERVED ONE-THIRD, AND THE COMMIT MESSAGE READS AS THOUGH IT WAS SERVED WHOLE

§A3 — *"Three smaller things I verified in passing"* — contains three Paper II items:

1. **the unopposed run has two values in one paper** → live until this pass (`II-6`)
2. **the κ closed form is better than advertised** → live until this pass (`II-8`)
3. **the test count contradicts itself across the batch** → repaired for Paper III by `-58`'s
   derivation instrument; **still live in Paper II's abstract** until this pass (`II-11`)

Commit `bde6d65` is titled *"REVIEW-004 A3's remedy, four days late, and made to stay fixed by
derivation."* It served item 3. Items 1 and 2 have been live for the five days since, and the
title is the reason nobody looked: **a bucket named for its smallest member gets closed by its
smallest member.** `-63` warned that `REVIEW-004`'s section numbers do not resolve and that only
its verbatim quotes can be matched; the sharper hazard is that its Part A reads as *the big three*
and A3 reads as *the leftovers*, so A3 is the one section a re-serving pass skips.

**The referee's arithmetic was right and this pass re-derived it independently.** −6.78 %,
−4.91 %, −4.35 % — computed here from Φ(0.25) and φ(0.25) before §A3 was found, and identical to
it. §A3 also supplies the diagnosis this pass did **not** act on: κ is measured against
post-growth wealth, so the exact form carries a `1/(1 + μ + a/w̄)` factor and agreement tightens
to under 1 %. See §6 for why that is carded rather than done.

---

## 3 · `PIN-001` REPAIRED THE CLASS IN ONE MANUSCRIPT OF FOUR, AND ITS OWN CENSUS MISSED THE SECOND

`RESULT-PIN-001` is emphatic that it is fixing a *class*: *"PIN-001 repaired the sentence. This
repairs the CLASS, in the one place it is mechanical."* Its census reads: *"`d655501` occurs six
times in this repository and every one of them is prose — **paper III four times**, `LEDGER.md`,
`RESULT-002-wt026.md`, the session notes."*

**Paper II §7 said `d655501` too, in the same words, and is not in that list.** Not introduced
later either: `git log -S` puts the phrase in Paper II at `f1ceac7`, the commit that completed the
paper — so it was there, false since 2026-08-10, throughout `PIN-001`'s own session. And both
instruments the repair built are hardcoded to one file:

```
tests/test_manuscript_shas_are_instrumented.py:  PAPER = ROOT / "…/paper-III-dual-tensor/paper-III.md"
tests/test_pin001_code_state.py:                 PAPER = ROOT / "…/paper-III-dual-tensor/paper-III.md"
```

**The census across all four manuscripts, run this pass:**

| manuscript | commits it pins | orphaned (named by no instrument) |
|---|---|---|
| paper-I | — | — |
| paper-II | `d655501` | none — but the **sentence** was false |
| paper-III | `0569ab6` `93a159b` `ad779eb` `b9089c7` `d655501` | none |
| paper-IV | `5efe626` `fff7063` | **`5efe626`** |

So the hole is wider than Paper II: **widening `test_manuscript_shas_are_instrumented.py` to every
manuscript goes red on Paper IV today**, because `5efe626` — the per-file pin for
`scripts/reg013_citation_whitespace.py` — lives only in prose. That is the `PIN-001` shape, intact,
in the newest paper. It is carded, not committed, because a red suite is not a repair.

**What this pass did do.** §7 now pins **per file** — `3b11f23`, the last commit touching
`redistribution.py` — which is the form `PIN-001` chose as the remedy, *and* the pin is now
instrumented: `LATEST_TOUCH` in `wt099_edits_pin001.py` carries the module, so
`test_each_pinned_path_was_last_touched_by_the_sha_the_paper_discloses` goes red on the next commit
that moves it. A per-file pin without that line would have been the same defect in a smaller font.

*The old pin was not even wrong about the bytes: `redistribution.py` last moved at `3b11f23`, which
is **before** `d655501`, so `d655501`'s tree state of the module was correct and still is. The
sentence was false about why.*

---

## 4 · WHAT §3 REPRODUCES — the first reproduction from the committed command

`python3 scripts/wt030_report.py`, run this pass at `T = 1200`, `seed = 0`, reproduces **every
number §3 prints**: 0.994 / 1.000 unopposed; stock 0.443 and 0.222; flow 0.812, 0.596, 0.125; κ
0.0250, 0.1000, 0.0025, 0.0102, 0.1026; ρ 0.125 / 0.395 / 0.994; frontiers 0.000 / 0.125 / 0.395 /
0.994; threshold 0.443 → 0.770 with 0.444 at 0.25×; periodicity 0.486 → 0.456.

`REVIEW-004`'s referee reimplemented the table *from the prose*. Nobody had run the command. It
works, and the two defects it exposed (`II-6`, `II-7`) were both in the one section whose numbers
**are not in the table** — which is where the drift went, because the table is what gets checked.

---

## 5 · SCORED AND NOT DEFECTS

- **Periodicity reverses at *P* = 50.** The sweep goes 0.486, 0.484, 0.480, 0.471, 0.456, **0.469**
  — the trend turns because the matched rate saturates at 1.00. Not a defect: the paper quotes
  *P* = 1 → 20 and claims nothing beyond it, and the suite's monotonicity assert stops at 20 too.
- **`stock 0.000` is asserted and not tabulated.** True (`r = 1.000` takes everything and
  redistributes per capita) and produced by the frontier sweep the paper names. Printing the row
  would help a reader; its absence is not a false claim.
- **The 18-test count itself is consistent**, exactly as `REVIEW-005` §3 dismissed it. `II-11` is
  not that finding re-litigated: the integer is right in all three places, and the abstract is
  wrong about the **noun it attaches to**.
- **§3.2's *"companion work on the reporting layer"*** needs no edit — it is unambiguous in kind.
  `II-10` is repaired on §1's and §7's side, where the *other* companion was unnamed.
- **The version stamp reads *"v0.2, 2026-08-11"*** over three sessions of repairs. Corpus-wide
  convention question, not a Paper II defect; it belongs to `P8`/`P11`, and is noted here so the
  next pass does not score it as new.

---

## 6 · THE NEAR-MISS, AND WHY IT IS THE LESSON

The first draft of the abstract repair **deleted** *"with 18 tests"* outright — word-negative,
returns three words of slack, kills the false attribution. Grepping the instruments before writing
found what that would have cost:

```
scripts/redproof_apparatus.py:105     sub(r"18 tests", "19 tests", 0, count=0)
scripts/gen_apparatus_rows.py:166     "The paper says '18 tests' in the abstract and in 1; this row DERIVES…"
```

§1's phrasing is `the 18 tests in` and §7's is `the **18** tests in` — so the abstract's *literal*
`18 tests` is one of only two targets the mutation control has, and one of two facts a board row's
rationale asserts. Deleting it would have starved a falsification instrument of its subject **while
every test still passed**, which is the failure mode `redproof` exists to prevent, arriving through
the front door. The repair chosen instead keeps the literal string, is **word-neutral** (249, and
four characters shorter), and preserves the paper's one word of abstract slack for
`DECISION-001`.

**The rule: before editing a manuscript string, grep `tests/` and `scripts/` for it. A repair that
silently removes an instrument's subject cannot be caught by running the suite, because the suite
goes green.**

---

## 7 · WHAT WAS TOUCHED

- `docs/papers/paper-II-redistribution/paper-II.md` — 14 hunks, 9 findings.
  `.bak-wt64-p7` kept.
- `scripts/wt099_edits_pin001.py` — one `LATEST_TOUCH` entry, so §7's new pin is guarded.
  `.bak-wt64-p7` kept.
- `scripts/wt112_edits_wt64_paperII.py` — the patch script. 15 anchors, each asserted to occur
  exactly once before any write; dry-run against a copy in the cloud container and diffed there
  first; long-line count unchanged at 6, all pre-existing.
- Board regenerated: `matches measured reality (66 criteria)`, rc=0.
- Abstract re-measured with `check_abstract_size.py`: **249 words, 1509 chars** (was 249 / 1513).
- Targeted suite green (73 passed). Full suite **1073 passed, 1 failed** — the failure is §8's,
  is in a file this pass did not touch, and predates it.

---

## 8 · THE SUITE IS RED, THE GATE CANNOT SEE IT, AND THE GUARD'S OWN REMEDY IS IMPOSSIBLE

`tests/test_reg012_sec6_sec47_frozen.py::test_section_47_is_byte_identical_to_the_pin` **fails at
`HEAD` (6314302)**, and has since `-63` committed. `git status` this session shows `paper-III.md`
unmodified, so it is not this pass's.

**It is not a `REG-012` violation.** §6 freezes §4.7 against *"any outcome of it"*; the edit is
`-63`'s `III-3` repair, licensed by `ASC 350-30-35-15` — an outside accounting standard. The
registration is intact. The guard is stricter than the clause it enforces.

**And the guard's prescribed remedy cannot be executed.** Its failure message offers reading (b):
*"Re-pin `SEC_47_SHA256` in the SAME commit as the edit."* But the same file also asserts

```
test_the_pinned_digest_is_the_version_REG_012_saw:
    assert digest(section_47(blob_at_REG_012_COMMIT)) == SEC_47_SHA256
```

so the pin must simultaneously equal **today's** §4.7 and **the registration's** §4.7. Once §4.7
moves for a legitimate reason there is **no value of `SEC_47_SHA256` that passes both tests.** The
instrument's advice is forbidden by the instrument. Resolving it means choosing between reverting a
correct repair and restructuring a registration guard — *"a judgement change to a safety guard
wants its own at-bat"*, the ruling `-59`→`-63` applied five times running. **Carded, not touched.**

**Why nobody knew: the gate does not run a test suite.** `grep pytest ~/Scripts/gate-selfcheck.sh`
returns exactly one line, and it is a directory-exclusion list (`.pytest_cache`). The gate proves
every repo is committed and pushed; it says nothing about whether what was pushed is green. `-63`
handed off a `PASS`ing gate over a red suite, correctly, because the gate was never asked.

---

## 9 · WHAT THIS PASS EXPOSES

**The tell, and it is now four deep.** `-61`: a corpus under repair has a moving referent and only
the filesystem knows. `-62`: the line-wrap grep trap runs both ways. `-63`: a backlog drain
measures the backlog, not the paper. **`-64`: A REVIEW APPARATUS HAS THE SAME PROBLEM AS A
MANUSCRIPT — ITS OWN COVERAGE IS AN UNMEASURED CLAIM.** `REVIEW-004` §A3's three items were served
one-third under a title that said otherwise. `PIN-001` said *"this repairs the CLASS"* and
hardcoded one of four manuscripts, with the second one missing from its own census. The gate
reports `PASS` over a red suite. **Each is an instrument that is right about what it checks and
silent about what it does not reach — and the silence reads exactly like coverage.** The question
that finds all three is not *is this checked?* but **what is the widest object this check's own
words claim, and what is the narrowest thing it actually touches?**

**Corollary, cheap and immediate:** a `P7` pass should end by asking *which instrument would have
caught this finding, and does that instrument exist for the other three papers?* Six of this pass's
nine findings have an instrument watching the identical thing one file over.

*Coffee status: ☕ the pin sentence that `PIN-001` chased through nine days and five sessions of
grepping was, the whole time, sitting in the sibling manuscript in the same words — inside a
paragraph explaining why pinning the code rather than the prose is the honest thing to do. The
corpus is now four papers, 1074 tests and three review documents deep in the business of watching
itself, and its most reliable discovery is that whatever is watching, something adjacent is not.
Which is, on the whole, a better problem than the alternative.* 🥎
