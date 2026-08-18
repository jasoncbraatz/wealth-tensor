# REVIEW-022 · P7 · the PROMISE SWEEP — the class enumerated, not sampled

- **Session:** `wealthTensor-82` · 2026-08-18 · darwin, from a cloud container over darlish
- **At-bat, as assigned:** build the promise sweep. Enumerate the class. **Do not read another
  manuscript.** No manuscript was read end to end in this pass.
- **Instrument:** `scripts/wt148_promise_sweep.py` (new) · adjudication file
  `docs/promises-adjudicated.tsv` (new) · binding test
  `tests/test_manuscript_sweeps_are_green.py` (new)
- **Repairs:** `scripts/wt149_paperIII_drop_accounting.py` · `scripts/wt150_paperIV_reg013_record.py`
- **Suite:** **1094 passed**, 0 failed, 69.56 s (1090 before; the four additions are this
  review's binding test). `wt133_crossref_sweep.py` **RC 0**, Paper IV still 0 unresolved and
  28 of 28 cited. `wt148_promise_sweep.py` **RC 0**.

---

## 1 · Why a sweep instead of a twelfth read

Eleven ledger rows say a reader-pass on this corpus finds 2–9 findings, forever. Every
mechanism offered for that rate is dead — new instruments (`-71`/`-77`), residue (`-78`),
depth (`-79`), coverage (`-81`) — and each was proposed by the pass whose own number it
explained and killed by the very next pass. What survived was not a mechanism but a
**measurement**: `-80` and `-81` independently scored **5 of 9** findings, on two different
manuscripts, as one shape — *a sentence whose subject is a named file, command, test or
commit, asserting what it does for a reader, where it does not.*

A shape two reviewers agree on is a shape a grep can enumerate. `wt133` already checks one
narrow slice of it (does `§N.M` resolve, and only entry→body). Nobody had enumerated the rest.

## 2 · What the sweep does, and what it cannot do

For each manuscript it emits every **(sentence, named artefact)** pair, where a named artefact
is a backticked path or glob, a bare file name, a script tag (`wt091`), a test name, a
`REG-`/`PRE-`/`ADR-`/`METHOD-`/`END-TO-END-`/`RESULT-`/`WT-` identifier, a 7–40 character commit
SHA, or a `python3 …` command. Each pair needs a row in `docs/promises-adjudicated.tsv` naming
**the command run or the file read** and what it showed. Delete a row and the sweep goes red;
reword the sentence and the row is reported STALE, because the row's id is a hash of
(paper, artefact, sentence). That is how the file is audited instead of trusted — the pattern
`docs/crossref-dismissed.tsv` established, with a staleness check added.

**Its blind spot, stated so a green run is not read as more than it is:** a promise that names
no artefact is invisible to it. `-81`'s `IV-6` — *"The Austrian account of the cycle"*, naming
no author, no work and no constraint — is exactly that class and this sweep cannot see it. It
also cannot tell a promise from a mention; deciding that **is** the adjudication, and the
adjudication is a human running the artefact.

Scope is declared in the TSV's own `#scope` line rather than in the code, so widening it is a
data edit that goes red on the next run. Paper I and Paper II are **out of scope and the sweep
says so on every run**: 28 promises there are checked by nobody.

## 3 · The count

| manuscript | emitted | adjudicated | H · held | N · not a promise | R · repaired | C · carded | gated |
|---|---|---|---|---|---|---|---|
| **paper-III.md** | 86 | **86** | 79 | 6 | **1** | 0 | yes |
| **paper-IV.md** | 41 | **41** | 40 | 0 | **1** | 0 | yes |
| paper-II.md | 15 | 0 | — | — | — | — | **no** |
| paper-I.md | 13 | 0 | — | — | — | — | **no** |
| **in scope** | **127** | **127** | **119** | **6** | **2** | **0** | |

Every one of the 127 was adjudicated by running or reading the artefact. Nine commands were
run on darwin (`pytest tests/ -q`, `pytest tests/test_excess_demand.py -q`, `wt027_report.py`,
`wt002_lambda_report.py`, `wt026_severe_test.py --universe pilot --onset peak`,
`wt071_refuter.py`, `wt089_recognition_and_offdiagonal.py`, `wt030_report.py`,
`reg013_citation_whitespace.py`); twelve SHAs resolved with `git cat-file` and
`git show --name-only`; thirty-one paths existence-checked; both `RESULT-002` run logs read end
to end; `REG-003`, `REG-005`, `REG-006`, `REG-007`, `REG-008`, `PRE-002`, `METHOD-001`,
`RESULT-REG-013`, `RESULT-REG-001` and both `END-TO-END-001` legs read at the cited section.

## 4 · The two that failed

### `III-1` — §11's drop accounting promised a per-tier breakdown that has never existed

§11 said the attrition to the 688 analysed events was in the run logs *"by universe and by
tier"*, and then instructed: **"A reader should check that attrition does not differ
systematically by tier, since differential attrition is the one selection channel capable of
manufacturing the reported null."**

Both logs were read end to end. They carry a flat ten-bucket drop table per universe and **no
per-tier attrition of any kind**. The only tier-keyed numbers in either log are the *surviving*
events' lag distributions and one bucket, `ambiguous_tier` (57 in the pilot), which counts
charges whose tier could not be resolved — the opposite of attrition from a tier. The
instrument agrees: `src/wealth_tensor/edgar.py` declares a flat `DROP_BUCKETS` tuple and every
increment in the file is `drops["<bucket>"] += n`. **There is no tier key anywhere, so nothing
ever recorded the breakdown.**

This is the sharpest instance of the class in the corpus, because the sentence does not merely
describe an artefact — it hands the reader a task, on the paper's own account of the one
channel that could manufacture its null, and the artefact cannot support the task.

**Repaired** (`wt149`, 10/10 post-conditions, two of them NEGATIVE): the claim is narrowed to
what the logs bear, the absence is stated positively as a fact about the counter, and the check
that *does* exist — the registered label-permutation control, whose null (+0.007, sd 1.025 over
1 000 draws, against an observed *z* of −0.290) is printed in the same logs — takes the place of
the one that does not. No hedge was added; `test_defensive_count.py` stayed green.

### `IV-1` — §10's "Regenerate §6" names a command that regenerates nothing, and never names the record that does

§10 carried the bare bullet **`- Regenerate §6: python3 scripts/reg013_citation_whitespace.py`**.
Run on darwin on 2026-08-18 it **exits 1**, on `HTTP 429 Too Many Requests` from
`api.openalex.org`, part-way through the split-half ceiling control, after resolving all 25
seeds and retrieving four audiences. And a clean run would not regenerate §6 either: a cluster's
audience is the set of works *citing* its seeds, retrieved live, and that set grows every day.
§6's audience sizes (7 801 and 43 048) and its overlap coefficients are the record of **one
pull, on 2026-08-16**.

That record is committed — `docs/preregistration/RESULT-REG-013-run.json` and `-run.log`, both
entered at `5efe626`, with `RESULT-REG-013.md` reading the verdict off them. **§10 named none of
the three.**

What makes this one worth the space is that **the repair was already written, one manuscript
over**. Paper III §11, at `-80`, learned this exact lesson in this exact register: *"That command
reproduces the instrument and not the sample… those logs, not a command, are the record of §5.3.
Nothing in this repository re-derives §5.3's figures from committed data, and this bullet implied
otherwise until wealthTensor-80."* Paper IV's identical bullet then survived two whole-manuscript
reader-passes, one of which (`-81`) ran six of §10's named commands.

**Repaired** (`wt150`, 10/10 post-conditions, three NEGATIVE — including that §1's promise
*"§10 names the command for each"* must remain true, and that no new SHA entered the manuscript).

## 5 · The falsifier, answered

`-82`'s at-bat set it both ways: if the class is drainable the sweep finds defects eleven
reader-passes missed; if a hundred promises all check out, the 5/2/2 was about reviewer
attention, not about the corpus.

> **Neither pole: 127 promises emitted, 127 adjudicated, 2 failed — and both were missed by
> eleven reader-passes, so the class is real, was never reviewer noise, and one grep exhausted
> what eleven passes had been sampling.**

The prediction that follows is sharp and cheap to test, which is the point of writing it here.
**`-83`'s reader-pass on Paper III or Paper IV should find materially fewer than 5-of-9
promise-shaped findings.** If it does not, the disambiguation is mechanical and must be run
before any theorising:

- the new findings **name an artefact** → this sweep has a bug or a gap in `ARTEFACT_PATTERNS`;
  fix the instrument, do not add a row to the ledger;
- the new findings **name no artefact** (`IV-6`'s shape) → the class was mis-defined as
  *artefact-naming*, and the next instrument is the one that catches a promise whose subject is
  a bare noun phrase.

Either branch is information. That is the first time in twelve rows the rate has had a
prediction attached that can be wrong in a stated way.

## 6 · Red-proof

Run on darwin against the real tree, three legs, all restored:

1. **Delete one adjudication row** (`d4dd6baf17`, the `IV-1` repair row): 127 → 126 rows,
   sweep **RC 1**, `[ ] d4dd6baf17 L666` listed as unadjudicated. Restored → **RC 0**.
2. **Mutate a promise sentence** (§11's *"not per tier"* → *"per tier"*): sweep **RC 1**, one
   UNADJUDICATED **and** one STALE row (`b2d5dcca15`) — the row is reported dead, not silently
   carried. Restored → **RC 0**.
3. **Mutate an artefact name** (`reg013_citation_whitespace.py` → `reg013_whitespace.py`):
   sweep **RC 1**, the fabricated path emitted as an unadjudicated promise. Restored → **RC 0**.

`sha256` manifest of all four manuscripts and the TSV **identical** before and after all three
mutations.

## 7 · What this pass did not do

No manuscript was read end to end — that was the instruction and it was followed. The 28
promises in Paper I and Paper II are emitted, counted, printed on every run, and **checked by
nobody**; widening `#scope` to them is `-83`'s at-bat and is stated as such in the handoff.
`wt133` and `wt148` are now both bound to the suite by
`tests/test_manuscript_sweeps_are_green.py`, so neither depends on a handoff remembering to ask
for its exit code — `wt133` had gone eight sessions with no guard, which is `WT-116` recurring.
