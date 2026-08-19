# REVIEW-032 · Paper II's prose, repaired — and the two ways an adjudication dies

*`wealthTensor-92`. Companion to `REVIEW-031`, which adjudicated Paper II's fifteen promises and
left four named prose defects standing. This pass repaired all four and re-adjudicated what the
repair moved. Scripts: `scripts/wt171_paperII_prose_repaired.py` (the repair, 14 post-conditions,
8 NEGATIVE) and `scripts/wt172_tsv.py` (the adjudication, 16 post-conditions, 10 NEGATIVE).*

---

## 1 · The verdict, in one sentence someone can mark right or wrong

**Every number in Paper II §3 is now regenerable from committed scripts, or excepted by name in
§7:** the residue scan finds seven decimals in §3 that neither named command prints in any
precision, §7's repaired clause excepts six of them by name, and the seventh — `4.6` — is
§3.1's `−4.6 %` rounded from the `−4.568 %` the commands do print, so the scan's own
`unaccounted:` line reads `[]`. Paper II now stands at **17 promises, 17 adjudicated, 16 H and
1 N, no C and no R**, and the single N is `54c1c5fb27`, whose "artefact" is `wt148` mis-parsing
the arXiv identifier `cond-mat/0002374` and is not a defect in the paper at all.

## 2 · What was repaired, and under which charter mode

| # | where | mode | from | to |
|---|---|---|---|---|
| R1 | L11 | RE-TARGET | "named in the data-availability statement" | "named in §7" |
| R2 | §2.2 | RE-TARGET | "verified to machine precision in the implementation" | names `test_the_levy_is_a_pure_transfer` and the `transfer_error` bound |
| R3 | §3.1 | RE-TARGET | "visible in the third column" | "the table's κ column" |
| R4 | abstract | REPLACE | "save §3.4's Gini ceiling" | "save the five quantities §7 enumerates" |
| R5 | §7 | REPLACE | the one-member exception | the five-member exception, enumerated |
| R6 | §7 | REPLACE | "save five closed-form quantities" | the numeral dropped |

**R1 was not invented, it was copied.** Papers III and IV carry `named in §11` and `named in §10`;
Paper II carried the bare form. The same defect was shipping in one manuscript of three, and
`wt164` had already written the repair for the other two. `wt171` E4 asserts all three now match.

**R3 is the SOFT pointer the card asked for a ruling on, and the ruling is: repair it.** REVIEW-030
classed it SOFT because the table is adjacent, which is true and is not the point. A positional
handle breaks the moment a column is inserted, and it breaks *with no diff at the site* — the
sentence still reads fine and is simply wrong. Naming the column by its header costs one word.

**R6 is bug spray, not part of the brief.** R5 introduces a *five* two bullets below a *different*
five. Two adjacent counts naming different sets is `wealthTensor-91` lesson (i) — a summary total
re-read as a per-subject count — written into a manuscript on purpose. No claim changed; the
numeral went.

**Nothing was absorbed.** `defensive_count.py` over the repaired file returns 0 outside
§Limitations against Paper II's committed baseline of 0 (`wt171` E10), and the coach counts are
unmoved at 2 conduct / 0 concessive.

## 3 · The C row, discharged — and why the inherited done-when could not be met

`wealthTensor-91`'s handoff set this DONE WHEN: *"`wt170 --verify`'s `c9a565b3fe` command prints a
second line reading `['0.1073', '0.99875', '4.6']`."* **It cannot, and no correct repair could make
it.** That command scans §3's decimals against the two commands' stdout. Its output is a property
of §3's *numbers*, and the defect was never in the numbers — it was in §7's claim about them. The
only edit that would produce that line is deleting `0.035`, `0.039`, `0.103` and `0.90` from the
results section, which would be vandalism dressed as compliance.

So the residue is unchanged, deliberately, and `b9dea67210`'s evidence measures the repaired
sentence instead:

```
printed by neither command: ['0.035', '0.039', '0.103', '0.1073', '0.90', '0.99875', '4.6']
named as an exception in the section 7 bullet: ['0.035', '0.039', '0.103', '0.1073', '0.90', '0.99875']
not named, and what it rounds from: {'4.6': ['4.568']}
unaccounted: []
```

Two membership tests, differing on purpose. Against the §7 bullet the test is boundary-guarded (no
digit or dot either side) so `0.103` cannot be credited by matching inside `0.1073`. Against the
commands' stdout it is left as the bare substring test `c9a565b3fe` used, so the two measurements
stay commensurable and the first line can be compared to `-91`'s directly.

**The general form, because it will recur:** a done-when written from the *finding* rather than
from the *repair* asks the instrument that found the defect to stop finding it. When the repair is
a narrowing of a claim, the finding's instrument is invariant and a NEW measurement is required.
Write the done-when as *"the claim now covers the residue"*, never as *"the residue goes away"*.

## 4 · The two ways an adjudication dies, and the ledger each one needed

`wt170 --verify` refuses if one of its fifteen rows is missing from the TSV. That refusal is
correct — an adjudication must not be able to vanish — and as written it made the corpus
**harder to repair than to leave alone**, because repairing an adjudicated sentence deletes its
row and turns a green guard red. An incentive pointed the wrong way is a defect even when every
individual check is sound.

**Death one — the sentence is repaired.** `promise_id` is `sha1(stem, artefact, normalised
sentence)`, so a repair re-keys it. Three rows died this way: `dfd41f5263`, `c9a565b3fe` and
`1cbe31f16c`. The TSV now carries `#superseded<TAB>old<TAB>new<TAB>tag<TAB>reason` lines, and
`wt170 --verify` forgives a missing pid **only** if such a line names a successor that is itself
an adjudicated row. `wt172` F9 fabricates a supersession pointing at a pid that does not exist and
proves the refusal survives: the ledger redirects, it does not excuse.

**Death two — the sentence never moved and the evidence broke anyway.** `5a47d4caef`'s sentence
was untouched, so its `promise_id` held. Its evidence command printed
`18 quoted at lines: [38, 90, 459]`, and `wt171` added four lines above 459. **A positional
evidence command is invalidated by any edit above it, including an edit that changes nothing the
row asserts.** The cell was replaced with one that names the sections the count appears in rather
than the lines — stable under reflow — and a `#reevidenced` line records it. That forgiveness is
honoured only when the committed cell genuinely differs from the one frozen in `wt170`, so it
cannot pardon a row whose unchanged command has started failing for real; `wt172` F15 proves it.

**This is `--verify` earning its keep.** `wealthTensor-91` added `--verify` on the argument that an
adjudication checked once, by its author, on the day it was written, is not a standing check. It
was written to re-run fifteen known commands. It caught a sixteenth thing nobody had thought of,
on the first repair that ran after it, and the defect it caught was in a row `-91` had marked H.
That is a stronger argument for the mode than the one it shipped with.

## 5 · What the instruments cannot see — measured, not asserted

**`wt160`, `wt163` and `wt166` read Papers III and IV only.** The brief asked for `wt167`'s G4
pattern — the two sweeps' flag sets bit-identical across the repair, proved in the script. They
are (`wt171` E5, E6), and the check is *vacuous by construction*: `PAPERS` in both modules is
`[paper-III, paper-IV]`. The bare-pointer sweep, named for the corpus, has never read half of it.
That is why REVIEW-030 §5.1's seven bare pointers in Papers I and II were found by a labelling
pass and not by the instrument built to find bare pointers. E5 and E6 assert the bit-identity
**and** the blindness, so a successor reading a green line reads the reason with it.

**`wt169`'s revision pin is not a revision pin.** REVIEW-030 §8 falsifier 4 says the pin "has never
been exercised by a real repair" and asks the first repairing session to exercise it. `wt171` E7
exercises it: the entire JSON payload, captured before and after the edit, is byte-identical.
**It could not have been otherwise.** `wt169` reads both manuscripts through `git show 83db4d5:`
and never touches the working tree, so a working-tree repair cannot move it *by construction*. It
is a guard against the ground-truth TSV and the word lists drifting, and it is a good one — G1
recomputed 88 keys against 88 labels with zero symmetric difference, and G5 proves the guard is
not vacuous by fabricating a row. It is **not** a guard against manuscript repair, and falsifier 4
mis-describes what it does. E7 captures the payload rather than the exit code precisely so that
the successor reading this can see the claim was tested rather than reasoned about.

## 6 · How far the verbatim-quotation standard actually reaches

`-91`'s N28b — every non-empty line of an evidence command's stdout appears verbatim in its note —
applies to **17 of the TSV's 153 rows**. Re-running every cell that is a bare shell command (55 of
them; 42 more are compound or annotated and this crude harness cannot invoke them, 56 are prose
instructions like `read docs/X.md §2`) gives **32 satisfying the standard and 23 not**. Every one
of the 23 predates the standard.

Stated carefully, because the number is easy to misread: **that is not a claim that 23 rows are
wrong.** It is a measurement of how far a rule written at `-91` has spread through a file built
before it. The 23 abbreviate or reflow their evidence in the note — which is exactly the shape
that hid five true-but-unverifiable notes inside `-91`'s own pass until a guard was written. The
successor instrument is named in §8.

## 7 · Falsifiers

1. **§1's verdict.** Run `b9dea67210`'s evidence cell. If `unaccounted:` is not `[]`, or if the
   second line does not list six of the seven, the verdict is false.
2. **The supersession ledger.** Delete a `#superseded` line and re-run `wt170 --verify`; it must
   go RC 2. Point one at a fabricated pid; it must go RC 2 (this is `wt172` F9, run in-band).
3. **The re-evidencing forgiveness.** Add a `#reevidenced` line for a row whose cell still equals
   `wt170`'s frozen one and break its note; `wt170 --verify` must still fail (`wt172` F15).
4. **§5's claim about `wt169`.** Edit `paper-II.md` arbitrarily and re-run `wt169`. If its payload
   moves at all, this section is wrong and the pin does read the working tree somewhere.
5. **§5's claim about the sweeps.** Introduce a blatant bare pointer into Paper II — "as set out
   in the appendix" — and run `wt160` and `wt163`. If either flags it, they are not blind to
   Paper II and E5/E6 are misstated.
6. **§6's counts.** Re-run the audit in `docs/` history; the 32/23 split is a property of one
   crude runnable-detector and a different detector will give different numbers. The claim that
   survives is the direction, not the digits.

## 8 · What closes here and what does not

**Closes.** Both Paper II cards — `1217630566080722` (the §7 exception clause) and Paper II's
three rows of `1217629169253037` (the bare pointers). Paper II carries **no known unrepaired prose
defect**. `P13` — the arXiv-ready PDF — is now the honest next lane, which it was not before,
because a capture built from a manuscript with a carded reproducibility defect spends the capture
on a corpus already known to be stale.

**Does not close.** `1217629169253037` keeps its **four Paper I rows**; Paper I is outside `#scope`
and `wt170`'s N27 fails any run that widens scope to it, so widening is a decision somebody makes
on purpose. `54c1c5fb27`'s arXiv mis-parse (`1217630566080626`) still stands. Two new cards:
`wt160`/`wt163`/`wt166` covering two manuscripts of four, and the whole-file evidence re-runner
§6 argues for.

**P7's counter for Paper II moves to ZERO by design, not by failure.** A repair pass is not a
fresh-eyes review pass. Two consecutive zero-finding reviews are what closes a paper, and this
pass found things — including one in its own instrumentation — so it starts the count rather than
advancing it.
