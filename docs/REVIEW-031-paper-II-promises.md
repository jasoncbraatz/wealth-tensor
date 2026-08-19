# REVIEW-031 — Paper II enters the promise instrument

*`wealthTensor-91`, 2026-08-19. Scope line committed at `f5691b3` before a single adjudication
existed; the fifteen rows at `62217d2`; this document after both. The order is the argument.*

---

## 1 · The verdict, in one sentence someone can mark right or wrong

**Paper II's promises are checkable: all fifteen that `wt148` emits now carry an adjudication
whose evidence command was RUN and whose note quotes that command's stdout character for
character — thirteen HELD, one NOT-A-PROMISE, one CARDED — so the paper enters the instrument
with exactly one substantive defect, and that defect is named, falsifiable and deliberately
unrepaired.**

Counts that settle it:

| | emitted | adjudicated | H | N | R | C |
|---|---|---|---|---|---|---|
| paper-II *(new)* | 15 | 15 | 13 | 1 | 0 | 1 |
| paper-III | 91 | 91 | 84 | 6 | 1 | 0 |
| paper-IV | 45 | 45 | 43 | 0 | 2 | 0 |
| **in scope** | **151** | **151** | **140** | **7** | **3** | **1** |
| paper-I *(deliberately out of scope)* | 13 | 0 | — | — | — | — |

`python3 scripts/wt148_promise_sweep.py` → **RC 0**, 151 adjudicated.
`python3 scripts/wt170_paperII_promises.py` → **RC 0**, 29 post-conditions, 9 NEGATIVE.
`python3 scripts/wt170_paperII_promises.py --verify` → **RC 0**, fifteen committed evidence cells
re-run and matched. *(The writing path is one-shot: a second run without `--verify` exits 2 by
design, refusing to write twins. That refusal is the guard, not a failure.)*

## 2 · The first finding is in the brief, and it is a subtraction

`-90`'s handoff assigned this at-bat with the words *"28 promises there are checked by nobody"*,
where *there* is Paper II. **Paper II emits 15.** The 28 is the correct total for everything
outside scope — 15 in Paper II and **13 in Paper I** — and the two were fused into one number
somewhere between the sweep's `TOTAL` line, which reports `28 left unchecked outside scope` over
four manuscripts, and a sentence naming one manuscript.

It changes no verdict and it is worth a paragraph anyway, because the same shape has now
appeared twice in this programme in three sessions: a **grand total attributed to a part**. `-89`
lost a post-condition to a note recording an expected output that was never diffed against the
real one; this is the same defect one layer up — a number read off a summary line and re-quoted
against a narrower subject. The cheap defence is the one this pass used before touching
anything: run the instrument, per manuscript, and read *its* number.

## 3 · The one that failed — `c9a565b3fe`, class C

**The claim.** §7 L452: *"Regenerate every number in §3: `python3 scripts/wt030_report.py` —
except §3.1's four closed-form quantities … and except §3.4's Gini ceiling, which is arithmetic
in *N* and is printed by neither."* The abstract's bullet 5 makes the same claim.

**The measurement.** Scan every decimal in §3 (section references and heading lines excluded)
against the concatenated stdout of both commands:

```
decimals in section 3: 49
printed by neither command: ['0.035', '0.039', '0.103', '0.1073', '0.90', '0.99875', '4.6']
```

Of the seven, **three are fine**: `0.1073` and `4.6` are printed quantities at the paper's own
precision (`0.107269` and `−4.568 %`), and `0.99875` is the exception the sentence names. The
**other four are numbers in §3 that neither command prints in any precision and that the sentence
does not except**:

| number | line | what it is |
|---|---|---|
| 0.035 | L294 | the periodicity sweep's span, 0.486 − 0.451 |
| 0.103 | L324 | the Gini gap, 0.994 − 0.891 |
| 0.039 | L327 | the top-decile margin, 0.90 − 0.861 |
| 0.90 | L321 | §3.4's top-decile threshold — a criterion constant, not an output |

**Why this is a defect and not pedantry, in the sentence's own terms.** Three of the four are one
subtraction from numbers printed on the same page, so a reader might fairly call them
regenerated. But the sentence has already ruled on that question in the other direction: it
excepts the Gini ceiling **because it "is printed by neither"**, and `(N−1)/N` is one step of
arithmetic from the `N=800` that `wt030_report.py` prints in its own header line. The clause
cannot hold both readings at once. As written it is §7's own named failure mode — *"a provenance
claim that reads as checked and is not"* — applied to §7.

**Why C rather than R.** The repair is a manuscript edit; a manuscript edit re-keys `promise_id`
and moves the emitted set underneath the pass measuring it. Carded **`1217630566080722`** with
the repair already written out, per charter §2.4: except the whole class rather than one member
of it, in one sentence, at L452 and at L88. **No hedging is added and none is proposed** — the
repair narrows the claim, which is charter §2's REPLACE, not ABSORB.

## 4 · The one that is not a promise — `54c1c5fb27`, class N

`wt148`'s `sha` rule matches any 7–40 character hex run containing a digit. Paper II's References
carry *"Text consulted: arXiv `cond-mat/0002374`, read in full."* The rule matched **`0002374`**,
so the sweep demanded an adjudication for a commit that does not exist:

```
git cat-file -t 0002374 -> fatal: Not a valid object name 0002374
```

Classed **N**, with the mis-parse written into the note rather than ticked over. This one is
worth naming loudly because of how it fails: **an adjudicator who does not run `cat-file` writes
a true-sounding note about a nonexistent commit.** That is `-83`'s failure mode — *an adjudication
is false if it checked a different artefact from the one the sentence names* — with the artefact
removed altogether, and it is invisible to `wt154` (the evidence would read the artefact token
just fine) and to `wt156` (a hex string is a valid handle). Instrument gap carded
**`1217630566080626`** with a candidate repair and the NEGATIVE post-condition it needs.

## 5 · What a FAILING row would have looked like

`-90`'s brief anticipated the wrong risk in the right spirit: *"a pass that widens scope and
reports 28 of 28 clean is more likely to have adjudicated loosely than to have found a clean
paper."* It did not come out clean, so the warning did not bind — but the guard against loose
adjudication is worth showing, because it is mechanical and it fired.

Every row's evidence command is run inside `wt170`, and `G1..G15` assert
`stdout.strip() == QUOTED[pid]` — the note's quotation, character for character. **Three of the
fifteen failed that check on their first probe**, and every one of them would have shipped as a
confident, wrong note without it:

- `4eae009313` printed `thresholds: False`. The substring test used a typographic apostrophe
  (`E1’s`) where `RESULT-END-TO-END-001-E1.md` has a straight one. A note reading *"E1 records
  its thresholds"* would have been true of the document and false of the check that was run.
- `50503d9ee7` printed `carries a reference-verification item: False`, same cause.
- `c9a565b3fe`'s first scanner credited `0.103` as regenerated because a rounding-tolerant
  comparison matched it against an **unrelated** κ of `0.102609047`. The tolerance was invented
  to be fair to `0.1073`; it silently rescued a number that is not the same quantity at all.
  The scanner in the committed row is verbatim-only, and the rounding cases are classified in
  the note by hand, where a reader can disagree with them.

**And then it fired again, on this pass's own notes.** The writing path refuses a second
invocation — it will not write a twin — so as first written, the fifteen evidence commands would
have been checked once, on the day they were written, and never again. That is the defect this
whole file exists to attack, one level up. `--verify` was added to close it: it reads each
evidence cell **out of the committed TSV**, runs it, and holds the stdout to the note's
quotation. On its first run it failed **five of the fifteen** — `c138f0078e`, `95e60baa81`,
`1cbe31f16c`, `cd94f1a9bc` and `54c1c5fb27` — because each note quoted its command's *first* line
verbatim and then **paraphrased the rest** ("and the four `Var[log a]` lines the command emits").
Every one of those notes was true. Every one of them also read as checked in a way that a later
reader could not diff. The five were rewritten to quote every line, and `N28b` now asserts that
property at write time, so the paraphrase cannot come back.

`N25` makes the non-clean result load-bearing: it asserts **exactly one C and exactly one N**, so
a later session that quietly upgrades either to H fails the script rather than passing it.

## 6 · What this pass did not anticipate

1. **Paper II's `git` pin is stronger than Paper III's, and nobody said so.**
   `src/wealth_tensor/redistribution.py` has **exactly one commit in its entire history**
   (`3b11f23`), so *"the last commit touching the module, and therefore the state that produced
   §3"* has no gap between the pin and the state at all. Paper III's equivalent pin needed a
   disclosure paragraph because `src/` moved afterwards (row `9add6ff45d`). The strongest
   provenance claim in the corpus is the one that argues for itself least.
2. **`wt077_tail_index.py` prints four `Var[log a]` values and the paper quotes three.** The
   sentence says *"the three Var[log *a*] values"*, which is a claim about what §3.1 uses, not
   about what the script prints. That is true and it is one careless reading away from an R.
   Row `1cbe31f16c` prints both lists so the distinction survives the next reader.
3. **`docs/papers/PREPRINT-CHECKLIST.md` bears the sentence out now and did not when it was
   written**, and the checklist itself is the document that says so: `-79` added the
   reference-verification item after finding that *"ten of its sixteen entries were deferred to a
   document that was not holding them."* A promise repaired by editing its **target** rather than
   its **text** keeps the same `promise_id` and adjudicates clean, leaving no trace in this file
   — which is a blind spot of the instrument worth knowing about, not a defect in the row.
4. **The evidence commands are the review.** Thirteen of the fifteen rows took longer to write
   than to check, because writing a command whose stdout can be quoted forces the adjudicator to
   decide, in advance, exactly which fact settles the sentence. `95e60baa81` — a bare
   `- **Module:** src/wealth_tensor/redistribution.py` — is the clearest case: locating the file
   proves nothing, and the row instead reads what *depends* on it.

## 7 · Falsifiers

1. **Re-run the C row's command.** If its second line reads `['0.1073', '0.99875', '4.6']`, the
   §3 defect does not exist and row `c9a565b3fe` is FALSE — delete it and `wt148` goes red.
2. **Re-adjudicate any of the thirteen H rows from its evidence column alone.** Each names a
   runnable command; if its stdout does not show what the note says it shows, the row is FALSE.
   `python3 scripts/wt170_paperII_promises.py --verify` does exactly that — it takes the evidence
   cells out of the committed TSV, runs all fifteen, and requires every line of each note's
   quotation to appear in the output. So this falsifier is one command away, forever, and not
   only on the day the rows were written.
3. **The `N` on `54c1c5fb27` is the weakest verdict here.** *"Read in full"* is a claim about a
   human act, and classing it N asserts that no repository artefact could falsify it. A reader who
   holds that the §3.1 quotations are checkable against the arXiv text — they are — should argue
   that this is a bibliography promise the instrument cannot see, and that the right class is a
   sixth one this file does not have.
4. **The four-out-of-49 count depends on the scanner's exclusions.** It drops decimals preceded by
   `§` and decimals on heading lines. Both are defensible and neither is proved: re-scan without
   the exclusions and the residue grows by three section references (`2.3`, `3.3`, `3.4`), which
   is how the exclusions were chosen and is therefore not independent evidence for them.
5. **`P20` proves the seven sibling sweeps still return 0; it does not prove they *saw* the new
   rows.** `wt154` and `wt156` do read the TSV, so they did. `wt160`, `wt163`, `wt166` and `wt169`
   read the manuscripts, which this pass did not touch — their green is a non-regression, not a
   corroboration, and reading it as the latter would be this programme's own `-87` mistake.

## 8 · What this closes and what it does not

**Closes.** Paper II is no longer the shipping manuscript nobody checked. All three papers in the
definition of done are gated by the same instrument at the same standard, and the standard is
now mechanical rather than cultural: `wt170`'s `G1..G15` make a paraphrased note fail the run.

**Does not close.** `P7` still needs two consecutive zero-finding passes per paper, and this pass
found one substantive defect in Paper II, so its counter is at zero. The three bare pointers in
Paper II (card `1217629169253037`) remain, and one of them is the construction `wt164` already
repaired in Paper III — the same defect shipping in one paper and not the other. And Paper I's
13 promises are still checked by nobody, **which is correct**: Paper I is not in the definition
of done, and `wt170`'s `N27` fails the run if a later session widens `#scope` to it without
deciding to.
