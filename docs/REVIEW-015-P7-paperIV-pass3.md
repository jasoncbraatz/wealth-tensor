# REVIEW-015 · Paper IV's independent `P7` read — `wealthTensor-75`

**Session:** `wealthTensor-75` · **Date:** 2026-08-18 · **Manuscript:** `docs/papers/paper-IV-composition/paper-IV.md`, 748 lines at read, 766 after repair
**Repair script:** `scripts/wt134_paperIV_p7pass3.py` — eight manuscript edits, one dismissals row, guards asserted against the original before any byte moved
**Assigned at-bat:** resolve `wt133`'s red on Paper IV, then give Paper IV its next independent read. Both done. `wt133` exits **0** across all four manuscripts.

---

## §1 · The coverage claim

Three counts, and they reconcile.

| what was swept | instrument | count | result |
|---|---|---|---|
| every `§N.M` cross-reference | `wt133` sweep 1 | 47 references, 16 distinct | 1 unresolved (`§3.1`, L179), 3 already dismissed |
| every reference entry against the body | `wt133` sweep 2 | 28 entries | 25 do work, 3 do not |
| every quantifier token | `wt130` | 194 tokens on 153 lines of 748 | read forward from each |
| every number in the manuscript | **the paper's own §10 commands, executed** | **60 cells** | 60 of 60 reproduce exactly |
| the manuscript, end to end | a reader | lines 1–748 | 6 findings |

**Six findings. Eight edits. Two carded, one as a new card and one as a fifth data point on an
existing one.** `wt133` RC 0. Suite **1078 passed, 0 failed** (66.75 s). Coach RC 0, Paper IV at
its baseline of **1 conduct / 0 concessive**. Board **unmodified — sixth consecutive session.**

### §1.1 · The 60 cells, and what "verified" means here

Nobody had ever run Paper IV's §10 commands. `-74`'s lesson said to run them first, so they were
run first — before a word of the manuscript was read. This is the list, because a coverage claim
that does not say what it counted is not a coverage claim.

**`REG-013`, re-run live against OpenAlex on 2026-08-18 — 25 cells, all exact:**
pooled ceiling 0.477 · floor 0.000 · T×S intersection 23, min audience 1 139, overlap 0.0202,
*z* 0.042 · T×K 15, 1 383, 0.0108, 0.023 · S×K 6, 1 139, 0.0053, 0.011 · split-half intersections
134 / 155 / 380 · split-half overlaps 0.168 / 0.520 / 0.744 · the stricter-ceiling *z* = 0.120 ·
25 of 25 seeds resolved · the VOID rule's 0.20 threshold, not triggered · T's cap at 4 000 · and
"six works in the world", which is licensed because **neither** S nor K is cap-bound (`cap_bound:
false` on both) — so that phrase is not an overreach, it is a consequence of the caps not binding.

That a live citation-graph instrument reproduces twenty-five numbers to the digit two days later
is itself worth writing down. It was not guaranteed and it was not assumed.

**§5 and §8, regenerated from `tests/test_excess_demand.py` and `scripts/wt071_refuter.py` —
18 cells, all exact:**
399 interior grid points · 25 distinct demand schedules · 25 distinct supply schedules · **1**
distinct excess-demand schedule · 500 grid points · first value **+249** · last value **−150** ·
zero monotonicity violations · exactly one sign change · the twelve-point grid's **four** distinct
excess-demand schedules · 26.1× / 8.3× / 113.5× / 47.2× at *N* = 400 / 1 000 / 4 000 / 10 000 ·
the 13.6-fold swing · the control's **0.96** (0.9576, H-indexed) against **0.89** (0.8934, random
subset) · and *D*(*p*\*) = *S*(*p*\*) = |*H* \ *T*| across all 25 allocations.

**Borrowed from Papers II and III — 11 cells, checked against `wt030_report.py`, `wt027_report.py`
and the two manuscripts:**
effective decay 0.02 per period · α = 0.05 · α̂ = 0.408 per year · 4.12× · 2.02× · *p* = 0.0002 on
both arms · power 1.00 at a 5 % injected excess · the tag-list repair's 4.01× and 2.10× · κ's
definition, word for word · and the ρ = 0 result, which `wt030` prints as Gini 0.994 `bounded=False`
for a confiscatory flow levy against 0.994 `bounded=False` for no levy at all — **identical to three
decimals, which is what "statistically indistinguishable" was claiming.**

**Provenance — 3 cells:** `5efe626` is the last commit touching the instrument ✓ · `fff7063` adds
the registration and **only** the registration, 157 lines, one file ✓ · both named tests exist ✓.

**The registration, checked against the instrument — 2 cells:** all **25 seeds appear in
`reg013_citation_whitespace.py` in exactly the order `REG-013` §3.1/§3.2 fixes**, cluster by cluster
and within each cluster — which matters because the script's own comment says *"Order is
load-bearing: the split-half control is by index parity in exactly this order. Do not reorder."*
Nobody had ever checked it. It holds. And **`wt026_severe_test.py --universe pilot --onset peak`
exits 0** — run before §10 was allowed to name it.

**The registration's own decision rule — 1 cell:** `REG-013` §4 defines
**z(A,B) = (O − F) / (P − F)**, with **P** the mean split-half overlap across the three target
clusters and **F** the mean floor overlap. mean(0.16813, 0.52013, 0.74364) = **0.47730** = the
published ceiling, and F = 0, so the three published *z* values are `O/P` **only because the floor
came back at exactly zero.** That is not a coincidence worth shrugging at: it means IV-4's question
about what the floor's cap could hide is not cosmetic — a higher true floor would move every *z*
on the board. It would move them **down**, in the paper's favour, which is why the capped floor is
the conservative reading and why §6's direction argument survives IV-4 intact.

25 + 18 + 11 + 3 + 2 + 1 = **60**.

---

## §2 · The findings

### IV-1 · §3 carries two bare cross-document section references, and the sweep can only see one

**This was the assigned red, and the assignment was right about the shape of it.**

L179 read *"and §3.1 reports what the distance between those two rates costs."* Paper IV's §3 has
**no subsections** — `grep '^### 3\.'` returns nothing — so `§3.1` resolves to nothing and `wt133`
flagged it. It belongs to Paper III, whose §3.1 is the deferred-information table, and every
surrounding sentence names Paper III: *"Paper III §2 is that holding"*, *"Paper III §5.4 goes on to
measure"*.

**The line after it does the same thing and no instrument will ever see it.** L180 read *"read
before §4 indexes the holding by asset class."* Paper IV **has** a §4 — *"The tension, resolved
explicitly"* — which indexes nothing by asset class. Paper III's §4 is *"Timeliness and durability
are not separately identified"* and its §4.1 is *"The class index, and why the product is
elementwise"*. So the reference **resolves locally, silently, and to the wrong section**, and a
reader who follows it lands in an argument about SMD.

**Repaired** to *"Paper III §3.1"* and *"that paper's §4"*. The second form is deliberate: it copies
the pattern already used correctly four lines earlier at L221, *"that document's §2"*, which is how
this manuscript writes a foreign section reference when it writes one well.

`docs/crossref-dismissed.tsv` gains one row for `paper-IV §3.1`, with its reason. It is a claim, and
deleting the row re-opens the question.

> **The asymmetry is the lesson of the whole instrument.** A sweep finds the references that resolve
> to **nothing**. Only a reader finds the ones that resolve to the **wrong thing** — and the second
> class is strictly more dangerous, because it fails silently in both directions: the tool is quiet
> and the reader is confident.

### IV-2 · §10 misroutes a replicator three ways, and §1 inherits the error

This one took the longest to find and is the most consequential, because every part of it is a
promise made to somebody trying to check the paper.

**(a) A module paired with a script that does not touch it.** §10 read *"Paper III
(`src/wealth_tensor/lag.py` and `src/wealth_tensor/lambda_sensitivity.py`, regenerated by
`scripts/wt027_report.py`)"*. `wt027_report.py` imports from `wealth_tensor.lag` and nothing else —
`grep -n lambda_sensitivity scripts/wt027_report.py` returns nothing. Paper III's own §11 gets this
right and separates them: `wt027_report.py` for §3 and §A.2.4, `wt002_lambda_report.py` for §A.2.3.

**(b) The number this paper leans on hardest has no command at all.** The diagonality rejection —
4.12× and 2.02×, both *p* = 0.0002 — is cited **three times** in Paper IV: §3 L232, §4.4 L328, §9
L597. It is contribution 1's boundary condition made empirical, and it is the single borrowed
result that most changes what Paper IV may claim. §10 named no way to reproduce it. Paper III §11
names `wt026_severe_test.py --universe pilot --onset peak`, with `--universe replication` for the
second arm.

**(c) A provenance rule that is false of two whole sections.** §1 L125–126 read *"Where a number
appears below without a citation to II or III it is from `REG-013` and is reproducible by the
command in §10"*, and §10 opened *"Everything else it reports is cited from Paper II or Paper III
and is regenerated by those papers' scripts."* Both are false of **every number in §5 and §8** —
the 399 grid points, the 25/25/1, the 500-point sweep, +249 to −150, the twelve-point grid's four
schedules, 26.1×/8.3×/113.5×/47.2×, and the 0.96-against-0.89 control. None of them is `REG-013`'s
and none is cited to II or III.

**And here is the part that turns a wording defect into a real loss: all eighteen of those numbers
regenerate today, exactly, from code that is already committed to this repository.** They are the
surviving apparatus of the fourth paper §8 describes — `tests/test_excess_demand.py` and
`scripts/wt071_refuter.py`. The paper was sitting on a working reproduction of its own worked
instance and telling readers it did not exist.

**Repaired:** §10 now pairs each module with the script that regenerates it, names `wt026` for the
diagonality result, and carries a new bullet, *"Regenerate §5 and §8"*, with both commands. §1's
sentence now says there are two sources and points at §10 for each.

### IV-3 · §9.6's closing sentence is contradicted by four places in its own manuscript

§9 limitation 6 read: *"Ecological economics, industrial ecology, national accounting theory and
the aggregation literature proper all have claims on this territory. **The three named here are the
ones whose results the corpus actually uses.**"*

The corpus uses the aggregation literature's results constantly and says so four times over:

1. **Contribution 1** (§1 L100–105) is *"a composition result and its exact boundary"*, and the
   boundary **is** Sonnenschein–Mantel–Debreu — an aggregation-literature theorem.
2. **The whole of §4** is SMD: §4.1 states it as the strongest available objection, §4.2 answers it,
   §4.3 draws the consequence.
3. **§7 has a paragraph under its own heading**, *"And on the aggregation literature specifically."*
4. **The reference list opens with an eight-entry block headed "Aggregation"** — Aumann, Debreu,
   Grandmont, Hildenbrand, Mantel, Mas-Colell, Sonnenschein twice.

**This is `WT-117`'s fourth instance** — a claim about a set, contradicted by the document that
makes it, at a distance the reader is expected to close and does not. The first three were §1's
"four numbers" in Paper II (twice) and §7's "three quadrature values".

**Repaired** to what is true and is in fact stronger: the three named are the three this paper
*joins*, and the aggregation literature is used as a **limit** rather than joined — which is exactly
the distinction §4 spends a section establishing and §7 states outright. The limitation survives; it
just stops contradicting §4.

### IV-4 · §6's floor states a universal over a set the instrument saw 9.3 % of

§6 read: *"It came back at **exactly zero**: not one work in any of the three economics audiences
also cites a CRISPR seed."*

The CRISPR audience was capped at **4 000 of 43 048** by descending citation count. What was
measured is that no work in the three economics audiences is among the **4 000 most-cited works
citing a CRISPR seed**. The unqualified sentence claims something about all 43 048.

**The asymmetry in the disclosure is the sharper half.** §6's second qualification gives the
biophysical cap its exact magnitude — *"capped at 4 000 of 7 801"*, 51 % — and then says only *"the
floor's cap does the opposite and costs nothing"*, with no number. A reader reasonably infers the
floor's cap is comparable. It is five and a half times tighter.

**The direction argument is sound and survives intact**: a cap can only *remove* intersections, so
the measured floor is a lower bound on the true one, and a floor of exactly zero is the strictest
value available. Nothing about the verdict changes. What changes is that the sentence now says what
was measured, and the reader is told which cap is which.

**And one thing found while checking it, which is disclosed rather than repaired:** neither 7 801
nor 43 048 is produced by the command §10 names. `reg013_citation_whitespace.py` stops paging at
`N_MAX` and never reads OpenAlex's `meta.count`; the committed `RESULT-REG-013-run.json` has no
true-audience field, and today's live re-run reproduces every other number in §6 and still does not
print these two. **So the two figures that carry §6's honesty about what the instrument could not
see are the only figures in §6 that a replicator cannot check.** §6 now says so in its own text.

The fix — one line reading `meta.count` — is **deliberately not applied here**, and the reason is
`WT-121`'s shape: §10 pins `5efe626` as *"the last commit touching"* that file, so editing the
instrument falsifies the pin in the same stroke. The instrument change and the pin update have to
land together. **Carded: `1217574341282011`**, with the falsifier written into the card.

### IV-5 · §10's non-circularity rationale describes a choice that was not available

§10 read: *"The same non-circularity that governs Papers II and III applies: **a paper cannot cite
the commit that adds the paper**, so what is pinned is the code."*

`git show --stat 5efe626` puts **`docs/papers/paper-IV-composition/paper-IV.md`, +646 lines**, in
that very commit. `5efe626` **is** the commit that adds the paper. The sentence explains a choice
between two commits where there was only one, and it tells a reader that the pin predates the
manuscript, which it does not.

For Papers II and III the argument is sound — their code commits and their manuscript commits are
genuinely different objects. Paper IV inherited a true sentence into a place where it is vacuous.

**Repaired** to the stronger true statement: the instrument and the manuscript entered the
repository in the same commit, so the pin is **exact rather than approximate**, and what is pinned
is the state of the code.

### IV-6 · §8 declares a test applied to "every entry" and one entry does not answer it

§8 opens by naming its own standard: *"The test applied to every entry is: had this route worked,
which sentence in this paper would be different? **An abandonment that could not have cost anything
is an advertisement, not a disclosure.**"*

The superposition entry then says, in its own text, *"Rejected on technical grounds **before it
reached a draft**"*, and never says which sentence would differ. By the section's own second
sentence, an entry that never touched a draft is the thing §8 says it will not print.

This is the **softest of the six** and it is named as such. The entry is a real disclosure of a real
consideration, and the repair is one clause rather than a deletion: it now answers the test —
§5's account of what an agent's *role* is would read differently — and says out loud that it never
reached a draft, so a reader can weigh it.

It is also `-72`'s lesson used a second time and paying a second time: **when a document names a
failure mode, grep the document for that failure mode.** §8 named the failure mode in its opening
paragraph. Six lines of its own body committed it.

---

## §3 · The cleared list — 30 rows, and which ones moved from inference to measurement

Everything below was checked and is **right**. Thirty rows. The **M** column is the point: `M` = measured
against regenerated output this session; `R` = read and reconciled against another document; `A` =
argued through. Prior passes could only ever produce `A` rows for §6 and §5, because nobody had run
the commands.

| # | site | claim | | verdict |
|---|---|---|---|---|
| C1 | Abstract | ceiling 0.477, floor 0.000, targets 0.020/0.011/0.005 | **M** | exact, live re-run |
| C2 | Abstract | "six works in the world cite both" | **M** | S and K both **uncapped**, so "in the world" is licensed, not rhetorical |
| C3 | Abstract | "25 allocations … 25 / 25 / **one**" | **M** | exact |
| C4 | §1.1 | XBRL phase-in ending 2011; SDG indicator 7.3.1 | A | both datable and correctly dated |
| C5 | §1.1 | Samuelson (1966) conceded reswitching | A | "A Summing Up", QJE 80(4) — correct paper, correct concession |
| C6 | §1.1 → §4.3 | "§4.3 finds the composed state largely unmeasured" | R | §4.3 L307–309 says exactly that |
| C7 | §2.1 | Paper III §A.1.2 states the propositions with domains | R | correct, and already dismissed in the TSV |
| C8 | §3 | "physical layer degrades at an effective 0.02 per period" | R | Paper III L167: `d = 0.05, m = 0.6 (effective decay 0.02 per period)` |
| C9 | §3 | "claim layer recognises at α = 0.05" | R | same line |
| C10 | §3 | Paper III §5.4 measures 0.408/yr, "low by an order of magnitude" | **M** | Paper III L586 and L1559; the direction is stated the same way in both |
| C11 | §3 | 4.12× and 2.02×, both *p* = 0.0002, power 1.00 at 5 % | R | Paper III L1391–92, L1565 |
| C12 | §3 | "survives that section's tag-list repair at 4.01× and 2.10×" | R | Paper III L1404 and L1578 — the repaired pair, correctly transcribed |
| C13 | §3 | "the paragraph after next reports as tested and rejected" | R | counted: L212–224 is next, L226–234 is after next. Correct |
| C14 | §3 | κ "the share of aggregate wealth actually moved per assessment" | R | Paper II L151–152, **word for word** |
| C15 | §3 | flow at ρ = 0 "indistinguishable from no levy at all" | **M** | `wt030`: 0.994 `bounded=False` against 0.994 `bounded=False` |
| C16 | §3 | "that document's §2" (END-TO-END-001) | A | the possessive names the owner — this is the pattern IV-1 restores |
| C17 | §4.1 | SMD inherits only continuity, homogeneity of degree 0, Walras's Law | A | correct statement of the theorem |
| C18 | §4.3 | Hildenbrand and Grandmont, sufficient *dispersion* | A | correct attribution of the mechanism |
| C19 | §4.4 | Paper III's ladder ranks by parameter rather than product | R | Paper III L482's `(1 − φ)δ` column and L498's anti-alignment |
| C20 | §5 | 399 interior grid points; 25 / 25 / 1 | **M** | `linspace(min,max,401)[1:-1]`, tie-filtered → **399** |
| C21 | §5 | zero monotonicity violations, +249 to −150, one sign change | **M** | all four exact on the 500-point grid |
| C22 | §6 | 25 of 25 seeds resolved (7 + 6 + 6 + 6) | **M** | exact |
| C23 | §6 | split-half 0.168 / 0.520 / 0.744, intersections 134 / 155 / 380 | **M** | exact, and in the order the sentence implies |
| C24 | §6 | stricter-ceiling *z* = 0.120 for biophysical × stock-flow | **M** | 0.02019 / 0.16813 = 0.1201 |
| C25 | §6 | "whitespace under **every** reading tried" for the other two pairs | **M** | 0.0645 and 0.0102 against the 0.10 bar — both readings, both pairs |
| C26 | §8 | 26.1× / 8.3× / 113.5× / 47.2×, 13.6-fold swing; control 0.96 vs 0.89 | **M** | `wt071`, exact |
| C27 | §10 | `5efe626` is the last commit touching the instrument; `fff7063` adds only the registration | **M** | `git log -1 -- <file>` and `git show --stat` |
| C28 | §6 | the instrument's 25 seeds are the registration's 25, **in the registered order** | **M** | T, S, K and X all match `REG-013` §3.1/§3.2 index for index; the split-half parity is therefore the registered one |
| C29 | §10 (new) | `wt026_severe_test.py --universe pilot --onset peak` runs clean | **M** | RC 0, before §10 was allowed to name it |
| C30 | §6 | *z* is the registered statistic, not an arithmetic coincidence | **M** | `REG-013` §4: z = (O − F)/(P − F); P = mean split-half = 0.47730; F = 0 |

**Fifteen of these thirty are `M` rows and fourteen of the fifteen could not have been `M` rows
before this session**, because §6's and §5's commands had never been executed. That is the whole
return on eleven minutes of typing, and it is the second consecutive session where it has been the
single highest-yield act available.

**Three rows most likely to be re-litigated, flagged now so a later pass does not spend the
tokens:**

- **C13** — "the paragraph after next" is a positional claim that any edit to §3 breaks silently.
  It is correct today. It is also the most fragile sentence in the manuscript.
- **C19** — Paper IV says Paper III's ladder results "are what happens when one forgets this and
  ranks classes by a parameter rather than by a product". Paper III's §4.4 is about a *validity
  region*, not only about ranking; Paper IV's one-clause gloss is true but compresses hard.
- **The one I could not turn into a finding and will not pretend otherwise:** L179's *"§3.1 reports
  what the distance between those two rates costs"*. Paper III §3.1 sweeps **φ**, not the gap
  between δ = 0.02 and α = 0.05, and its closed form is `D(φ) = (1 − φ)·D(0)`. The deferred
  information §3.1 measures **is** the integral of the divergence between the physical layer and the
  claim layer, and the steady-state gap does depend on α — so the sentence is defensible. It is also
  **loose**, and I repaired only its attribution, not its content. A later pass that decides to
  tighten it has my reasoning here rather than a blank.

---

## §4 · The not-checked list — write the next brief from this

Nine items. Numbered so `-76` can cite one.

**Three items that were on this list when it was drafted are not on it now, because they were
checked instead of deferred**, and the draft list is preserved in this paragraph so the swap is
auditable. The seed-order audit against `REG-013` §3.1 — the highest-value item on the draft list —
came back clean and is `C28`. `wt026_severe_test.py` was run before IV-2 was allowed to name it in
§10 — RC 0, `C29` — because a data-availability section naming a command that fails is a worse
defect than the one it replaced. And §6's *z* was read out of `REG-013` §4 rather than inferred
from three matching decimals, `C30`. **A not-checked list is a promise about the next session's
cost, so an item that can be closed in four minutes should be closed rather than written down.**

1. **Paper IV's §7 was read for accuracy of characterisation, not against the sources.**
   *"Godley and Lavoie … insists that the accounting close"*, *"kinetic exchange … has mostly not
   had a base"* — these are claims about what four literatures do and do not contain, and they were
   checked against Paper II's and Paper III's related-work sections, not against the works.
   `REFERENCE-POLICY`'s eighth pass (card `1217556161163494`) is still the only instrument for this
   and is still the most-deferred item in the project.
2. **The three uncited reference entries are a measurement, not a finding, and were not resolved.**
   Mas-Colell, Robinson, Sraffa. Commented onto card `1217568192511533` with the per-manuscript
   breakdown; Robinson and Sraffa look less like uncited entries than like §1.1's Cambridge-
   controversy sentence being one clause short. Nobody decided.
3. **The front-matter stamp is now wrong by construction.** "Version 0.1, 2026-08-16" with eight
   claim-changing edits behind it, made 2026-08-18. Left alone deliberately — card
   `1217568297674954` asks Jason the ruling and there is not one. Fifth data point added to it.
4. **`docs/CHECKLIST.md` and the board were not re-derived after the edits.** The board did not move
   (sixth consecutive session) and `done-criteria.tsv`'s fifteen `paper-IV` rows were read, not
   re-scored. `P7` remains one boolean; see the handoff.
5. **§5's numbers were regenerated; §5's *argument* was not adversarially attacked.** The identity
   holds and the tie convention is understood. Whether a referee can get from "the crossing height
   is the allocation mismatch" to "this is a composition statement" in the two paragraphs §5 gives
   it is a judgement nobody made this session.
6. **The abstract was guarded byte-identical and therefore not reviewed.** `wt134` asserts it did
   not move. That is a safety property, not a reading. The abstract has never had its own pass.
7. **`END-TO-END-001` leg `E1` was taken on trust.** §3, §8 and §9 all cite it for the demotion from
    "chain" to "one question at three scales". `docs/RESULT-END-TO-END-001-E1.md` was not opened.
8. **No check that IV-2's new §10 bullet is *complete*.** It names `test_excess_demand.py` and
    `wt071_refuter.py`, which together cover all 18 §5/§8 cells verified here. Whether some other
    §5 or §8 number lives in a third file was not swept for — the sweep was from the manuscript's
    numbers to the code, never from the code back to the manuscript.
9. **Paper I is still not in `definition_of_done` and still has no `P7` pass.** Unchanged from
    `-71` through `-74`. Noted, not acted on. `wt133` sweeps it and it is clean.

---

## §5 · One thing for Jason, in one line each

- **`P7` is still one boolean, and the argument is now six sessions deep.** `-70` changed nothing
  and the board did not move; `-71` five, `-72` three, `-73` thirteen, `-74` seven, `-75` **eight
  across six findings including two in a data-availability section**. It has not moved once. Either
  the coverage row goes on the board or reviewing stays narrative — one line settles it.
- **Paper IV's counter opens at 6**, against Paper II's 9 → 2 → 4 → 3 → 4 and Paper III's 7. Every
  pass that used a new instrument found what the previous ones structurally could not, and this pass
  used two that Paper IV had never seen: the cross-reference sweep, and the paper's own commands.
  **The pair of consecutive zeros the definition of done wants may be unreachable while the
  instrument set is still growing** — which is not a reason to lower the bar, and may be a reason to
  say so out loud inside it.
