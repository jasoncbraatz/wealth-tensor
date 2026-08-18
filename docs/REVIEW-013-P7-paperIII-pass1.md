# REVIEW-013 · Paper III · `P7` pass 1 — the first independent read

*Session `wealthTensor-73`. Manuscript at `3a3ef0d` (repo HEAD when the read began);
repairs land at `74734de`. Instrument: `scripts/wt130_quantifier_sweep.py` (WT-115/WT-116),
run before a word was read.*

**Paper III had never been independently reviewed.** Papers II and IV have had six and three
passes between them; this manuscript — 2,685 lines, the largest in the batch — had none. That
is why `-72` set aside `-70`'s "Paper II again" rule, and the rule is not overruled by this
document: it is discharged for one session and Paper II's fifth read is `-74`'s to take.

**Result: seven findings, thirteen edits, one carded.** On a manuscript this size after zero
passes, a zero would have been the surprising outcome and this is not one. Every finding fell
out of the same move — the sweep read **forward** — and three of the seven are the exact
species `WT-117` describes: a universal falsified by material a few lines below it, or a
provenance claim naming a section that does not carry what is attributed to it.

---

## 1 · The coverage claim, which is countable

`python3 scripts/wt130_quantifier_sweep.py paper-III --md`

| | at `3a3ef0d` (read) | at `74734de` (after `wt131`) |
|---|---|---|
| quantifier tokens | **864** | 870 |
| lines carrying one | **668** | 673 |
| manuscript lines | 2,685 | 2,694 |

**The enumeration is in Appendix A of this document, all 668 rows.** *(`wt130` printed those two numbers as "864 quantifier tokens on 668 lines"; `wt131c` reworded all three of its print sites so the manuscript's own length now appears beside the count and the two cannot be conflated again.)* It is the reading order
and it is the coverage claim: unlike *"I read it carefully"* it can be diffed by `-74`.

> **A correction to the brief `-73` inherited, made here because it will mislead the next
> session too.** `wt130` prints *"668 lines"* meaning **lines that carry a quantifier**, not
> manuscript length. `-72`'s handoff, `LEDGER` `WT-116` and `docs/HANDOFF.md` all read that as
> the manuscript's size and budgeted "~50 min — 668 lines" for a document four times that long.
> The conclusion drawn from it was right for a different reason: Paper III **is** the largest
> manuscript in the batch, at 2,685 lines against Paper I's 730, Paper II's 547 and Paper IV's
> 748. The counts of tokens are unaffected. `wt130`'s output line is the thing to reword.

**The manuscript was then read whole, lines 1–2,685**, because the sweep is one class of
sentence and this paper had had no read of any kind — numbers, cross-references, references,
structure.

---

## 2 · Findings

### III-1 · §2 says the word *crisis* is kept in the title. It is not in the title.

§2's terminology note closes: *"The word **crisis** is kept in the title and for the phenomenon
the paper is about."* The title is **"Timeliness and durability are not separately identified
from a reported series"** and contains no such word.

The retitling is dated in the repository. `paper-III.md.bak-pre-roadtwo` opens
*"# A crisis is deferred information arriving at once: the dual tensor of wealth, and a
pre-registered prediction it lost"*; every later backup carries the present title. §8.2 —
written after the change — says the crisis framing *"is not defended here and not deleted
either"* and that **"The crash paper is a later paper in this corpus."** So the note was
written against a title that no longer exists and asserts, in the manuscript's own front
matter, a framing §8.2 spends a section declining to make.

**Read-forward verdict:** a claim about the document's own first line, falsified by the first
line, and separately by §8.2 1,530 lines below.
**Repaired.** The note now says the word is used for the phenomenon §2 models and for nothing
wider, that it is **not** in the title, and where §8.2 puts the framing. The banking-crisis
disclaimer — the part that was doing work — is unchanged.

### III-2 · §A.1.3 promises a failure regime for *each proposition* and delivers one, plus a non-proposition.

> *"Here it is demonstrated, because the regimes in which **each proposition** fails are
> committed, tested code rather than thought experiments:"*

Two bullets follow. The first is **P2 fails at complete maintenance**. The second is
**the framework's own central mechanism switches off at φ = 1** — and the bullet itself says
*"which is a separate and equally important point"*, which is correct: the φ = 1 switch-off is
not a proposition failing, and the bullet goes on to say **"P2 still holds at φ = 1."**
**P1 and P3 have no regime at all.**

This is `WT-117` exactly: the universal is written looking at the material above it, and the
set it ranges over is finished four lines below it, by a list that carves itself out in its own
second item.

**Read-forward verdict:** three propositions claimed, one demonstrated, and the second item
disclaims membership in the set it is offered as a member of.
**Repaired.** The sentence now says *one* of the three, names P2, points P1 and P3 at §A.1.1
and §A.1.4 where they **are** argued deniable, and labels the second item what it is. Nothing
is added to the demonstration and nothing is removed from it; the claim is cut to the evidence.

### III-3 · §11 scopes the repository's provenance to "§A.2 and §2" four times. §2 reports no simulation result.

`§11 · Data and code availability` says, in four places:

* *"Every simulation result in §A.2 and §2 is produced by open code."*
* *"**Regenerate §2 (and §A.2.4):** `python3 scripts/wt027_report.py`"*
* *"the state that produced every result in §A.2 and §2"*
* *"Every figure in §A.2 and §2 regenerates on a commodity CPU in seconds."*

**§2 is the model statement and carries no table and no measured number.** Every simulation
result the named command produces is in §3: `wt027_report.py`'s own docstring lists three
tables — A and C are §3.1's two, B is §3.2's. And **§6.1, in the same manuscript, writes the
same scope correctly, twice**: *"every result in §A.2 and §§2–3"*, *"everything in §A.2 and
§§2–3, because those are theorems about a simulation."*

This is `II-19`'s species — *"a single command named for numbers it does not produce is a
provenance claim that reads as checked and is not"* — with the correct wording available
500 lines upstream in the paper's own text.

**Read-forward verdict:** a data-availability statement whose scope is one section short of the
sections it covers, contradicted by §6.1 and by the named script's docstring.
**Repaired.** All four now read `§§2–3`, and the regeneration line names §3 and says in one
clause which tables it produces and that §2 reports none.

### III-4 · §7's survivals row is titled with a number from a different recognition rate than the one it ran at.

The row: **"The rectangle's 99.7% is a property of the assumed support, not of the disclosure"**
— design column *"against the same test on the asserted rectangle **at the same rate**"*,
outcome column *"rises in 0.659 of admissible pairs [0.621, 0.696] against **0.998** on the
rectangle."* §4.4 reports the same comparison as **99.8%**.

**99.7% is not a rounding of 0.998.** It is `REG-002` E4's figure, and
`docs/preregistration/RESULT-REG-002.md` §4 says where it comes from: *"The rung question was
then re-asked at an α for which it has a domain (α = 0.35): the first rung rises in 99.7% of
the rectangle."* The row ran at the **measured** α̂ = 0.408. The manuscript carries 99.7%
nowhere else, so a reader has no route from the title to the row four columns to its right.

**Read-forward verdict:** a row title naming a number its own outcome cell contradicts, at a
recognition rate the row does not use.
**Repaired**, to 99.8%, which is what §4.4 and the row's own cell report. `RESULT-REG-002`'s
99.7% is correct at its own α and is a dated result of record: **not touched.**
`tests/test_ledger_provenance.py` uses the row title as its lookup key in five places and those
move with it — the key is a locator, and the same test file's data is what proves the row's
value is 0.998.

### III-5 · The Bleck and Liu entry credits §4.4 for a result that is §3.2's.

> *"§4.4 and §10 both cite it against this paper: it states §4.4's volatility result nineteen
> years earlier."*

Bleck and Liu appear at four lines in this manuscript: §3.2 (the citation), §8.2, §10, and the
entry itself. **§4.4 does not mention them**, and §8.2 says where the material lives in terms:
*"is retained in §§3.2 and 10."* The volatility-relocation result is §3.2's throughout.

**Read-forward verdict:** two wrong section numbers in one sentence, in the section of the
paper whose stated second pass was *"every entry checked against the body — does this reference
do any work?"*
**Repaired** to §3.2 in both places. Nothing about the source, the edition or the verification
mark is changed.

### III-6 · The Jin and Myers entry names "§10's ONE quotation" and gives a sentence the manuscript does not contain.

Three claims in one entry, and the manuscript falsifies all three.

1. *"§10's **one** quotation"* — §10 carries **five** quoted fragments from Jin and Myers: the
   saintly-manager sentence, the four-line pressure-vessel block quote, *"cannot see the news
   as it happens"*, *"good or bad news accumulating"* and *"according to a pre-defined
   schedule."*
2. The sentence the entry names — *"For simplicity, we ignore depreciation and reinvestment"* —
   **appears nowhere in the manuscript.** §10 gives the paraphrase instead: *"The operating
   asset neither depreciates nor is reinvested in by declared assumption."*
3. The entry then states the rule the manuscript is breaking, in its own next sentence:
   *"§10 quotes the sentence because it is what establishes that the model has no physical
   layer, and **a reader entitled to doubt that on a paraphrase should be able to see the
   words**."* §10 supplies exactly the paraphrase.

**Read-forward verdict:** an entry whose count is wrong, whose named quotation is absent, and
which states the standard its own section fails.
**Repaired by restoring the words to §10** — the smaller change, and the one the entry's own
rule asks for — and by replacing *"§10's one quotation"* with what the sentence actually is.
The verification record (*"verified in the published text at p. 262, character for character"*)
is untouched: it is a dated fact about the source, not a claim about §10.

**And the References' own fourth pass is falsified by the entries it describes.** Its closing
note reads: *"It found that the crash-risk papers had been read in pre-publication and
untypeset versions and cited as though they were the published articles. **Hence ✓⧗**, and
hence the single surviving quotation in §10 being attributed to the working paper."*
**No crash-risk entry carries ✓⧗.** Jin and Myers, Hutton et al., Andreou et al., Zhu, and
Bleck and Liu all carry **✓**; the Jin and Myers entry records why — it was later read in the
typeset article and the sentence verified unchanged. The three ✓⧗ entries in the list are
Dutta and Patatoukas, Potepa and Thomas, and Long and Ravenscraft, cited in §§4.6, 4.9 and 4.4.

**Repaired by APPEND, not rewrite** — `wt129`'s shape. The pass-4 paragraph is a dated record
of what that pass found; what it found was afterwards discharged, and the discharge is now
written beneath it rather than in place of it.

### III-7 · §4.7 attributes its floor of 30 to §5, which states no such floor.

*"those 110 events occupy sixteen bands and **exactly one clears §5's floor of 30**."*

**§5 states no floor of 30 anywhere.** The word *floor* occurs there once, as *"the materiality
floor"* among PRE-002's researcher degrees of freedom, with no value; and §5.3's own published
tier cells run as low as **n = 21**, below the floor §4.7 attributes to it. The number is real
and registered — `REG-009` calls it *"§3b's inherited `THIN` line"* and `THIN` *"refuses any
band or SIC cell under 30"* — but it is not §5's.

**Read-forward verdict:** a provenance claim that reads as checked and is not; the same species
as III-3 at one-tenth the size.
**Repaired** to *"the registered floor of 30"*, which drops the false attribution and keeps the
number and its status.

**§4.7 is frozen by `REG-012` §6, and this edit went through the freeze rather than around it.**
`tests/test_reg012_sec6_sec47_frozen.py` went red on the edit — correctly, and that is the
guard working. The edit is the file's reading (b): it comes from a review of the manuscript
against itself, not from any outcome of `REG-012`. So an `Amendment` is appended (`wt131b`),
naming commit `74734de`, the licence, and the digest §4.7 landed on, taken out of git rather
than typed. `SEC_47_AT_REGISTRATION` is untouched. The freeze's whole design is that this
question gets asked out loud at the moment §4.7 moves; it was.

### III-8 · CARDED — §11 supplies no regeneration command for §4.

**Not repaired in-pass, because it is a session-sized audit rather than an edit.**

The front matter claims, over the whole paper: *"**every computational result** is produced by
committed code in the repository named in the data-availability statement."* That statement is
§11, and §11 names four commands: `wt027_report.py` (§3 and §A.2.4), `wt002_lambda_report.py`
(§A.2.3), and two `wt026_severe_test.py` invocations (§5). **§4 gets none** — and §4 is where
the paper's largest body of measured numbers lives: §4.4's 4,000 ladders and the fitted
logistic, §4.7's and §4.8's swept exponents, §4.9's α_eff table, §4.10's identified-set widths
and the three-recognition-rates table.

The numbers are not unsupported — `REG-002`, `REG-004`, `REG-005` and `REG-009` and their
`RESULT-*` docs carry them, and the suite holds them. What is missing is the line in §11 that
lets a replicator run them, which is what the front-matter sentence promises and what
`PREPRINT-CHECKLIST`'s *"exact regeneration command"* asks for. III-3 corrected §11's **label**;
it did not and could not supply this.

**Named falsifier, so the card can be closed or killed:** run every command §11 names, capture
stdout, and grep it for §4's published figures — `11.5`, `1.58`, `2.58`, `0.0079`, `1.30`,
`0.408`, `1.210`, `3.9e-04`. If §4's numbers appear in that output, **this card is wrong** and
§11 already covers §4. If they do not, the repair is a `wt132` that names the scripts which do
produce them, one line per subsection.

Filed to **State Machine**, not the Batter's Box: a Claude with darwin and the repos can run
the falsifier and write the line.

---

## 3 · CLEARED — read forward and found sound

*The point of this list is that a later pass does not pay to re-derive it. Every row was
checked in this session and the verdict is spelled out, not implied.*

| # | the claim | how it was read forward | verdict |
|---|---|---|---|
| C1 | §4.2 *"Admissibility requires φδ ≤ α, which holds at **every** parameter setting used **anywhere in this paper**"* | the widest quantifier in the manuscript. Evaluated at §2's calibration (φδ ≤ 0.020 < 0.050 at every swept φ), at all four of §4.4's tiers (0.0240, 0.0120, 0.0040, 0.00040 against 0.050), and at §4.2's own mirror world, where the condition becomes φδ ≤ δ and reads 0.012 ≤ 0.020 | **holds** |
| C2 | §4.4's δ-decomposition, *"at every rung ... the combined δ contribution (−0.81, −0.98, −1.79) outweighs the design term (+0.69, +0.41, +0.29)"* | recomputed all six from the table's own φ and δ: (+0.693, −0.811), (+0.405, −0.981), (+0.288, −1.792) | **holds to 2 d.p., and every step's sign is the one claimed** |
| C3 | §4.4's *"Checking only the log δ term would have got the first rung right for the wrong reason"* | at rung 0→1 the design term (+0.693) exceeds the bare log δ term (−0.405) in magnitude, and the step still falls because the −log(α − δ) channel adds another −0.405 | **holds** |
| C4 | §4.4's three **R** columns, twelve values | all twelve recomputed from R = (1 − φ)δ/(α − δ) at α = 0.05, 0.408 and 0.327 | **all twelve match to the printed precision** |
| C5 | §4.4's *"Kendall τ = −1 ... and −0.67 at both the measured rate and the unregistered adverse cut, where the **first rung alone** turns over"* | τ recomputed from the columns themselves: −1 at 0.05; at 0.408 the concordance count is 1 of 6 → −0.667, and tier 0→1 is the only rising pair | **holds, including the "first rung alone" clause** |
| C6 | §4.4's *"R at a common δ"* column and its τ = +1 | reproduced at δ = 0.02 for all four tiers (0.1333, 0.2667, 0.4000, 0.5333), strictly rising | **holds** |
| C7 | §4.3's *"it **changes sign**, from +0.267 to −1.267"* | recomputed at (α, δ, φ) = (0.05, 0.02, 0.60) and at its mirror (0.02, 0.05, 0.24) | **holds** |
| C8 | §4.2's *"at t = 400 its physical stock stands at 4 × 10⁻⁶ of the original world's"* | 0.95⁴⁰⁰/0.98⁴⁰⁰ = 4.0 × 10⁻⁶ | **holds** |
| C9 | §4.2's *"A factor of **1.67** in the unobserved physical scale"* | 1.27/0.76 = 1.671 | **holds** |
| C10 | the abstract's *"δ leverage is **4.2** times the level at which recovery fails"* | §4.4's ladder sits at 2.58, the half-probability crossing at 0.61; 2.58/0.61 = 4.23 | **holds** |
| C11 | §5.2/§5.3's event and firm arithmetic | 120 + 202 = 322; 244 + 444 = 688; 121 + 190 = 311; tiers sum to 244 and to 444 | **every sum closes** |
| C12 | §4.7's tier-0 counts, *"151 property events across 98 firms ... against 55 across 38 on the list as first collected"* | §5.3's tier-0 cells are 21 and 34, summing to the 55 §4.7 names as the unrepaired list | **consistent** |
| C13 | §4.4's *"665 admissible firm-year pairs"* against *"0.974 of the 683 disclosed pairs"* | 665/683 = 0.9736; and §7's *"only 0.139 of the pairs fall inside it"* against §4.4's 86.1% outside | **both close** |
| C14 | §11's test split, *"held **100** tests, of which the **62** ... The remaining 38"* and *"**three** of its additions ... two ... and one"* | 62 + 38 = 100; 2 + 1 = 3 | **both close** |
| C15 | §A.1.3's *"from E₀ = 100 to 0.031 over 400 periods"* at φ = 1 | 100 × 0.98⁴⁰⁰ = 0.0310 | **holds** |
| C16 | §A.2.3's *"recognition events 16"* at φ = 0.3 and §A.2.4's *"all 16"* | §3.1's frequency table gives 16 events at the industrial entropy rate d = 0.05, which is the calibration | **consistent**; §A.2.3's own note that the 300-period figure differs (12 events, 0.6100) is stated in the text |
| C17 | §A.2.4's *"overstates it by ~14%"* | mean λ = 1.136838 | **holds** |
| C18 | §9 item 9's *"in **644** firm-years"* against §7's *"**0 of 281** joint firm-years"* and §5.4's *"1,833 classified firm-years"* / *"1,925 filings"* | three denominators for adjacent claims, which is the shape a defect takes. All three are `REG-007`/`REG-008` registered constants — `scripts/wt096_entity_anchored.py` F5 reads `("0.436","0.403","244","281","644","1,189")` from `RESULT-REG-007` — and they scope different populations: the mandated window, its joint arm, and the classified set | **not a contradiction** |
| C19 | §4.2's and §4.7's *"**291-fold**"* against the printed 0.211 and 0.00073 | dividing the printed figures gives 289. `docs/notes/NOTE-001-phi-identifiability.md` §2 gives 0.21140 and 0.00073 and states 291× — the denominator is rounded at the fourth decimal, which is where the two per cent goes | **not an error**; a reader cannot reproduce 291 from the printed pair, and that is a rounding, not a claim |
| C20 | §5.1's *"the boundary of **§10's restriction**"* | §10 does state one: *"§2's claim is correspondingly restricted to degradation on which conservatism has nothing further to bite ... Where a loss is estimable, recognition is faster than the market and §2 predicts nothing"* | **resolves** |
| C21 | §4.9's *"goodwill's tabulated rate stays a factor of **3.8** inside it"* and §4.4's δ₃\* = **0.0079** | 0.00755/0.002 = 3.78; §4.9's 0.00789 at the calibration rounds to §4.4's 0.0079 | **both hold** |
| C22 | §7's *"**7 × 10⁻¹⁴**, five parameter settings"* against §4.2's *"largest deviation ... **8 × 10⁻¹⁶**"* | a maximum over five settings is not required to equal one setting's figure, and 7 × 10⁻¹⁴ ≥ 8 × 10⁻¹⁶ | **not a contradiction** |
| C23 | §11's *"A submission-time head-of-repository SHA will be pinned when this paper is posted"* against board row `P1m`'s *"the section may not defer its pin to posting"* | the section does not defer the pin a replicator needs — it supplies per-file pins and says so in the same clause, *"the per-file pins are what a replicator needs and are verifiable now."* `P1m`'s command passes and its prose is satisfied | **not a finding**; deliberately left |
| C24 | *"§4.6's question"*, twice — §4.7's *"So §4.6's question answers yes"* and §7's *"which would leave §4.6's question open the other way"* | §4.6 contains no question mark. Its third qualification poses the issue (*"the returns-based measures condition on a second series. That second series does break the equivalence"*) and defers the result to §4.7 | **loose, not false** — deliberately **not** repaired; recorded so `-74` does not spend the same ten minutes |
| C25 | §9's numbered list carrying a `---` between items 8 and 9 | CommonMark renders a list opening at `9.` as `<ol start="9">`, so the numbering survives the break, and `tests/test_manuscript_lists_are_well_formed.py` covers the section | **holds** |
| C26 | §2's *"An earlier draft of this paper used *correction* for the event thirty times"* — a `CONDUCT` phrase outside `§§6–11` | this is one of Paper III's five baseline conduct hits, not a new one. The coach reads 5/0 before and after `wt131` | **at baseline, unchanged** |
| C27 | the *"Version 0.5, 2026-08-12"* header above later content | the settled convention across all four manuscripts (`-72`'s settled list) | **not touched, on purpose** |

### The two mechanical sweeps, and what they cost

Both are cheap, both are re-runnable, and between them they are the coverage claim for the
classes of defect a careful read is worst at.

* **Every `§N.M` cross-reference in the body resolves to an existing heading.** Extracted all
  `§`-references from lines 1–2,288 and checked each against the heading list: **zero
  unresolved.** The single apparent miss, §4.4's *"REG-003 §3.3"*, is `REG-003`'s own §3.3 —
  *"Two biases, their direction registered before the number"* — and it is the right one.
* **Every reference entry's "cited in §N.M" checked against that section's text.** Thirty-three
  entries, forty-one section claims. Seven flagged; six are legitimate — four name the *source's*
  own section (Sims's §5, Ball et al.'s §4.4) and two make a claim *about* a section rather than
  asserting a citation *in* it (Zhu, Potepa and Thomas). **One was real: III-5.** The pass is
  worth its five minutes for that one, and the ratio is the honest thing to record.

---

## 4 · NOT CHECKED — the explicit list

**Nothing below was verified in this pass. A later session that treats this document as
coverage should treat this section as the boundary of it.**

1. **Every simulation residual**, reported at one or two significant figures — 3.9 × 10⁻⁴,
   4.1 × 10⁻³, 2 × 10⁻¹³, 5 × 10⁻¹⁶, 2 × 10⁻¹⁶, 8 × 10⁻¹⁶, 2 × 10⁻⁴ and their kin. Not
   re-derived. The suite and the `RESULT-*` docs own them.
2. **§4.9's α_eff table and the pole at 0.435 per year.** §4.10 says 0.435 is the reciprocal
   mean lag 1/**E**[T]; §4.9 says it is the constant-hazard form's pole. Both may be true and
   neither was reproduced here.
3. **§4.10's identified-set widths**, the 200-draw estimator quantiles, and the window
   non-monotonicity (1.40 / 1.26 / 0.98 / 1.32).
4. **§5.4's Weibull fit**, the 4.12×/2.02× off-diagonal permutation, the `REG-006` re-crawl
   cells, and every `REG-007`/`REG-008` disclosure rate.
5. **§4.4's 4,000-ladder logistic** — slope +1.58, se 0.081, z +19.5, crossing 0.61, ladder at
   2.58 — and the 11.5% / 1.9% / 23.8% / 100.0% recovery shares.
6. **Whether any quoted passage says what the manuscript attributes to it.** This pass checked
   only **where** each entry claims to be cited, never **what** the source says. The References'
   four passes own that question and this document does not extend them.
7. **Papers I, II and IV.** Untouched. The only bytes that moved are Paper III's, one lookup key
   in `tests/test_ledger_provenance.py`, and one appended `Amendment`.
8. **The abstract's word and character budget.** `wt131` asserts the abstract byte-identical
   rather than re-counting it; `P1a` runs the count.
9. **Whether §4's numbers have a regeneration command anywhere.** That is III-8, carded above
   with its falsifier. III-3 repaired §11's label and establishes nothing about §4.
10. **`DEFENSIVE-BASELINE.json`, `POSITIONING-001`, `POSITIONING-002` and `REVIEW-001`** in the
    paper's own directory. Not read this pass.

---

## Appendix A · The enumeration

*`python3 scripts/wt130_quantifier_sweep.py paper-III --md`, at `3a3ef0d`. 864 tokens on 668
lines. This is the reading order and the coverage claim; `-74` can diff it against a fresh run.*

**docs/papers/paper-III-dual-tensor/paper-III.md — 864 quantifier tokens on 668 lines**

| 11 | `all,every` | **Use of AI assistance.** Anthropic Claude Opus 5, at high reasoning effort, was used throughout as a research and drafting assistant: literature retr |
| 19 | `each` | share **φ** of each true change passes through at once, the rest released at rate **α** from an |
| 23 | `exactly` | physical decay rate: the roots exchange, preserving φδ exactly. Timeliness and durability are |
| 24 | `every` | therefore not separately identified, and where the asset's physical scale is unobserved (every |
| 26 | `the whole` | the whole unit interval. |
| 29 | `four` | Across the four GAAP classes, δ leverage is **4.2** times the level at which recovery fails, and |
| 35 | `two` | pre-registered, tested on 688 EDGAR-derived events in two pre-declared sectors, and **failed** |
| 37 | `two` | the failure: **disclosed useful lives supply δ from outside the series**, restoring φ for the two |
| 51 | `the whole` | That sentence is the whole paper, and the rest of it is an attempt to make the sentence cost |
| 60 | `only` | changes only when someone records something, then the gap between them is an accumulating quantity |
| 65 | `exactly` | exactly proportional to (1 − φ), where φ is the share of degradation the reporting layer can see. |
| 70 | `two` | The filter has two roots: the rate at which the reporting layer releases what it has withheld, and |
| 71 | `two` | the rate at which the physical layer decays. **Those two roots are exchangeable, and the exchange |
| 72 | `nothing` | preserves the product of timeliness and decay.** A reported series therefore contains φδ and nothing |
| 77 | `every` | That constraint is not a property of this framework. It is a property of the object every |
| 81 | `four` | comparison of timeliness. Across the four GAAP classes, with the decay rates the standards themselves imply, the |
| 83 | `all,no` | imposed survives in **11.5%** of ladders even when no durability ordering is imposed at all. |
| 91 | `never` | substitute whose relation to the model was never written down. A theorem about identification, a |
| 92 | `three,two` | registered null, and the discovery that the two are less connected than they look, are three |
| 93 | `three` | different results, and this paper reports them as three. |
| 98 | `two` | 1. **An exact observational equivalence, with its proof and its reach** (§4.2). The filter's two |
| 99 | `any` | roots exchange, preserving φδ, so timeliness is not recoverable from a reported series by any |
| 102 | `all,two` | scale is unobserved the degeneracy widens from two points to a continuum spanning all of φ. |
| 107 | `three` | 3. **A constraint on the conditional-conservatism measures** (§4.6), stated with its three |
| 112 | `no` | by the decay rate and reverses sign as that rate nears zero, and no horizon attains the root-T |
| 114 | `no` | 4. **A repair that needs no new data** (§4.7). Disclosed useful lives supply δ from outside the |
| 119 | `any` | 6. **A bridge discipline** (§6.2) arising from that loss, and now with an argument behind it: any |
| 128 | `no` | this paper has no claim on a reader's seriousness if it takes that route. |
| 130 | `three` | The framework the filter was built inside — three propositions about the composition of wealth, and |
| 131 | `nothing` | the coupling they oblige — is set out in **Appendix A**. Nothing in §§2–7 depends on it, which is |
| 138 | `two` | Two layers and one parameter that matters. |
| 144 | `each` | Of each true change, a share **φ** is *observable* — announced capital expenditure, a disclosed |
| 147 | `only` | statements. It accumulates in the gap and is recognised only at rate α per period: |
| 153 | `exactly` | and its magnitude is exactly the information that had been withheld.** |
| 171 | `any` | **φ is not a fudge factor**, and the distinction is load-bearing enough to state before any |
| 191 | `exactly` | **Deferred information is exactly proportional to (1 − φ), and this is a closed form rather than a |
| 193 | `two` | E(t+1) − C(t) = gap(t) + ΔE into the two recursions gives |
| 197 | `at every` | so with gap(0) = 0 the gap at every t is (1 − φ) times its value on the φ = 0 path. Since ΔE < 0 |
| 198 | `every,exactly` | throughout, every term shares a sign and the absolute integral inherits the factor exactly: |
| 203 | `exactly` | it. **A doubling of unobservability doubles the integral of what the statements owe, exactly.** |
| 208 | `two` | unobservability while the *delay* in delivering it is not, and the two should not be expected to |
| 222 | `two` | therefore a **position in a parameter space**, not a rhetorical flourish. Two firms with identical |
| 228 | `whole` | Measured across a whole path, **that prediction is false wherever the mechanism is actually |
| 231 | `never,only` | The prediction survives only at φ ≥ 0.8, where the gap never reaches the recognition threshold and |
| 232 | `no` | there are no recognition events to dominate anything; there the ratio is 1.00 and 0.93. **So the original |
| 233 | `nothing,only` | claim was not merely wrong, it was right only in the regime where the model has nothing to say.** |
| 237 | `all` | recognition events, while the share of all reported movement occurring **inside** recognition events rises |
| 248 | `every` | At zero observability, **essentially every reported movement is a recognition event.** The signature is |
| 254 | `only` | stability, volatility actually accumulates only to hit the market at a later date," transferring |
| 261 | `no` | statistic is unfalsifiable by construction: the asset class with no amortisation schedule has |
| 262 | `all` | essentially all of its recognised change arrive discretely *as a matter of accounting definition*, |
| 264 | `exactly` | not a test. Neither pre-registration included it, on exactly those grounds, before either was |
| 270 | `two` | wrong object: one number was being asked to carry two claims. Two now exist — smoothing measured |
| 272 | `two` | answers two questions answers neither. |
| 280 | `every,four` | caution about estimation: it holds for every estimator, it has a four-line proof, and it applies to |
| 281 | `any` | measures built without reference to this model or any like it. |
| 289 | `each` | purpose. Index the classes *i*. Each carries its own physical decay rate δᵢ, its own observable |
| 290 | `two` | share φᵢ, its own recognition rate αᵢ and its own threshold θᵢ, and §2's two recursions become one |
| 297 | `each` | in a distribution centre does not force recognition against a trademark. Each class's filter reads |
| 298 | `nothing` | its own gap and nothing else. |
| 302 | `single` | identification result below is a remark about a single parameter. With it, the remark acquires a |
| 310 | `single` | recursions to a single line: |
| 316 | `two` | A = 1 − α and D = 1 − δ for the two roots, |
| 320 | `two` | and the reported series is a linear combination of two geometrics whose exponents are the |
| 325 | `both` | coefficient requires α − φδ = α(1 − φ′). Both reduce to |
| 329 | `two` | Two equations, one unknown, and they agree. That coincidence is the theorem: the system is |
| 334 | `two` | > the *identical* reported series. The filter's two roots — the reporting rate and the physical |
| 335 | `exactly` | > decay rate — are exchangeable, and the quantity preserved by the exchange is exactly **φδ**. |
| 337 | `any` | **And this is not a property of the particular filter.** Any model in which reporting lag attenuates |
| 346 | `at every` | conserved quantity and a plausible wrong one. Admissibility requires φδ ≤ α, which holds at every |
| 353 | `two` | **What the two worlds disagree about is the firm, not the filing.** The mirror is not a |
| 354 | `no` | mathematical curiosity with no economic content. It is a slow reporter of a fast-decaying asset: |
| 356 | `all` | above an asset that has all but evaporated. That is a recognisable kind of company. It files the |
| 359 | `nothing` | **The mathematics is old, and saying so costs nothing.** Subtract E(t) from the closed form and the |
| 364 | `every` | a scalar amplitude carrying every trace of φ, multiplied by a shape function that is invariant |
| 370 | `single` | *local* identifiability, "in that there exists a finite set of parameter values (rather than a single |
| 371 | `two` | set) that solves the problem" — which is precisely the two-point structure above. Their own caution |
| 375 | `two` | of two roots, is therefore the simplest member of that family rather than the general one. The general framework is Bellman |
| 378 | `all` | a set, which is the exchange above stated once and for all. |
| 382 | `every,two` | eliminating the two unobservables leaves a reduced form in which **every systematic coefficient is a |
| 384 | `exactly` | on its second lag, βγa₁ on the price. The conditional mean is exactly invariant under exchanging the |
| 385 | `two` | two behavioural rates. What distinguishes them is the disturbance, γ[u(t) − (1 − β)u(t−1)], which is |
| 393 | `nothing` | nothing is lost. A plasma profile has an unknown volume of distribution, and a balance sheet has an |
| 397 | `two` | **The result is stronger than a two-point ambiguity.** The closed form has two roots and two |
| 398 | `everything,four` | amplitudes: four numbers, and that is everything a reported series contains. The model has five |
| 399 | `any` | parameters — α, δ, φ, the physical scale E₀, and any gap g₀ already open when the observation |
| 400 | `four` | starts. Five into four does not go, and the shortfall lands on φ. |
| 402 | `both,two` | Two consequences, both exact. First, opening the books with a gap already in place does not rescue |
| 407 | `two` | Second, and this is the sharp form: **when the physical scale is not observed, φ is not two-valued. |
| 410 | `exactly` | parameter vectors reproduce it exactly. Assuming a physical scale of 0.76 implies φ = 0; assuming |
| 411 | `every,one of` | 1.27 implies φ = 1; every assumption in between implies an intermediate φ, and every one of them |
| 413 | `each,entire` | spans the entire unit interval of timeliness.** Each member of that family also carries its own |
| 418 | `everything,nothing` | recognises everything at once and with a firm that recognises nothing. |
| 423 | `exactly` | which aggregates assets of many vintages, so the scale that would pin φ is exactly what a |
| 426 | `all` | The earlier conditioning result stands underneath all of this and is worth keeping for its size: |
| 434 | `two` | against 66, 25 against 80, 36 against 133, and two pairs where one side is silent entirely). **The |
| 435 | `no` | trigger reads E, which no filing reports.** The information that breaks the degeneracy arrives |
| 451 | `two` | **(1 − φ) ⊙ δ**, divided elementwise by (α − δ). Decay reaches the ranking through two channels, |
| 460 | `only` | **Timeliness sets the ranking only when durability is constant across the classes being ranked** — |
| 471 | `every` | every firm whose asset lives are read off its filings. |
| 473 | `four` | Order the four GAAP classes as the registration did — property, plant and equipment; finite-lived |
| 478 | `both,no` | enough to schedule. Goodwill sits at the end of both: least observable, and with no degradation |
| 479 | `all` | schedule at all. |
| 489 | `exactly,nothing` | nothing else. There the deferral measure rises monotonically up the ladder exactly as predicted, |
| 490 | `two` | Kendall τ = +1. The two **R** columns are the world the standards describe, at the recognition rate |
| 492 | `both` | too — **running the other way.** Kendall τ = **−1** at the calibrated rate, and **−0.67** at both the |
| 507 | `exactly` | so the deferral measure rises from one tier to the next exactly when |
| 511 | `two` | The first term is the design. **The other two are facts about δ**, and on a falling ladder they |
| 512 | `at every` | carry the same sign, so they add. At every rung of the ladder above, the combined δ contribution |
| 514 | `every,only` | predicts the direction of every step. Checking only the log δ term would have got the first rung |
| 515 | `two` | right for the wrong reason: there the design term is the larger of the two, and the step still falls, |
| 522 | `two` | **Dispersion and ordering do different damage, and the two are worth separating.** Draw 4,000 |
| 523 | `four` | four-class ladders under the design's own constraint alone — observability falls up the ladder — |
| 525 | `exactly` | **11.5%** of them and exactly reverses it in **1.1%**, mean Kendall τ **+0.32**. Hold δ common |
| 526 | `four` | across the four classes instead and redraw: recovery is **100.0%**. Now impose the standards' |
| 538 | `only,three` | it ordered only while per-rung δ leverage stays under about three fifths of the design budget. The |
| 541 | `three` | **The tabulated ladder is a knife edge in its own top rung.** Holding the first three tiers fixed, |
| 546 | `no` | which is **0.0079**, a half-life of eighty-seven periods. Five per cent above it the ladder is no |
| 548 | `no` | reversal therefore needs goodwill to lose half its value no faster than in eighty-seven years, and |
| 557 | `both` | the crossing rate. Both halves of the inference from an absent schedule therefore push the same way. |
| 559 | `all,no,two` | **Two rungs need no inference at all, and they are the two that break the table.** ASC 360 and |
| 561 | `only` | a disclosed life *L* fixes a write-down rate 1/*L*. The first rung falls only when |
| 568 | `three` | on, and it turns on the recognition rate's *level* rather than its shape: the top three rungs are |
| 572 | `both` | firms, both lives read off one page — **the first rung rises in 65.9% of them**, in both cycles |
| 574 | `three` | *assumed* to span — ten to forty years for property, three to twenty for finite-lived intangibles — |
| 578 | `only` | **And the binding constraint is the model's domain, not the ordering.** R is defined only for δ < α. |
| 580 | `no` | period 400 at δ = 0.20 — and there is no steady-state deferral measure to rank. At the α = 0.05 |
| 581 | `entire,every` | calibrated here **the entire asserted rectangle lies outside the domain**: every useful life short |
| 583 | `all,only` | rectangle is admissible only at α ≈ 0.19, and all of it above α = 0.33. **That made the recognition |
| 586 | `both` | 95% interval [0.383, 0.432], on both known biases' inflating side: the calibration used here is low by an order of magnitude, and the |
| 592 | `no` | 0.3333 is no longer cleared, and **0.814** of the pairs remain admissible. The domain restriction is |
| 601 | `two` | detonated an industrial-organisation literature. Two things about its reception instruct the present |
| 604 | `no` | almost no information about economic ones — did not survive: it was rebutted on the arithmetic and |
| 613 | `everything` | Everything above concerns a *magnitude* — how much a class defers. The registration did not order |
| 623 | `both` | Monotone under both, and the falling-δ ladder makes the ordering *steeper* rather than flattening |
| 624 | `at every` | it. The reason is visible in the parameter sweep: lag falls in φ at every δ, and rises as δ falls at |
| 625 | `both,every,two` | every φ, so on a ladder where both move the way the standards say they do, **the two effects add.** |
| 630 | `two` | measure. Lag is the more robust of the two by a factor of six, and it is robust in that ratio rather |
| 633 | `any` | **The identification result does not, by itself, wreck a design ordered on lag.** Any claim that the |
| 637 | `no` | ΔC, and ΔE is the change in physical value, which no filing reports.** The one statistic the |
| 638 | `any` | confound spares is the one that cannot be computed from public data. Any empirical instrument must |
| 641 | `never` | model's lag has never been written down. |
| 657 | `only` | If a timeliness parameter reaches a reported series only in product with an asset-life parameter, |
| 658 | `any,two` | then a cross-sectional comparison of any of these measures is a comparison of the product. **Two |
| 660 | `two` | two industries with identical scores may differ arbitrarily in practice.** The sign of the induced |
| 668 | `any` | correctly. Under §4.4 those are the readings a δ channel would produce whether or not any |
| 669 | `all,the whole,two` | recognition practice differed at all. The data cannot separate the two accounts, which is the whole |
| 670 | `both` | of the present claim; it may well be both. |
| 674 | `exactly` | conditional conservatism, and name the channel exactly: "the unconditionally conservative nature of |
| 679 | `two` | stated mechanism, and it leaves the two parameters separately meaningful; the claim here is that the |
| 687 | `no,two` | A degeneracy is not a bias. When two parameter vectors generate the identical series, no control |
| 688 | `nothing` | recovers the difference between them, because there is nothing in the series to recover it from. |
| 692 | `nothing` | a title-word with it and almost nothing else.** Dutta and Patatoukas (2017) decompose the |
| 695 | `three` | distribution is skewed, while the second moves with three properties of the news process — expected |
| 696 | `two` | returns, cash-flow persistence, and the skewness itself — at a fixed degree of conservatism. Two |
| 699 | `no` | reporting rule — and their firm is a cash-flow stream with no capitalised asset in it to carry one. |
| 703 | `no,two` | itself invariant, so no statistic computed from it separates the two worlds. Ryan (2006), whose |
| 705 | `no` | conservatism in practice and makes no claim of the econometric kind. |
| 708 | `no` | of bad news recognised — this paper's φ. Here δ is the physical decay rate, and has no counterpart |
| 711 | `each,three` | Three qualifications. First, the mapping from this filter to each of those estimators is not |
| 713 | `exactly` | exactly. Second, the magnitude-versus-timing distinction of §4.5 matters, and these measures sit on |
| 714 | `both` | both sides of it — Basu's coefficient is a slope on returns rather than a delay, and is closer to |
| 729 | `two` | supplies δ from outside the series restores φ.** Two things do, and they are priced very |
| 733 | `two` | breaks the two-point equivalence immediately and by a wide margin. Under the exchange the mirror |
| 734 | `two` | firm's asset decays at α rather than δ, so two worlds whose books agree to fourteen decimal places |
| 735 | `every,three` | differ in return by α − δ in every period — three percentage points a year, indefinitely. The |
| 739 | `both,exactly` | degeneracy is a degeneracy in the unobserved physical scale.** Grant an analyst both roots exactly — |
| 741 | `every` | with the reported series reproduced to 2 × 10⁻¹⁶, and every member of that family emits the |
| 742 | `no` | *identical* return series, bit for bit. A scale divides out of a ratio, so no quantity of returns |
| 746 | `nothing` | property of a noiseless economic path: when the asset's value decays geometrically and does nothing |
| 747 | `any,single` | else, the reported series has a single geometric driving term and a scale factor absorbs any |
| 752 | `exactly` | matrix that is exactly singular at zero volatility. |
| 755 | `both` | not switch on at the first innovation; it fades in. Over a twelvefold range of return volatility both |
| 758 | `four` | model, and neither should be read as one.** Across nine (α, δ) settings spanning the four decay |
| 760 | `all,always` | standard error's from −0.78 to −0.09. What holds in all nine is the sign: identification always |
| 763 | `two` | **What the exponents track is more useful than their values, and the two rates do different jobs.** |
| 764 | `two` | The decay rate governs how strongly identification *responds* to volatility; the gap between the two |
| 769 | `two` | (α − δ)^−0.70. The two must be kept apart or they read as a contradiction: a sweep at one volatility |
| 770 | `everything` | says the decay rate hardly matters, a sweep across volatilities says it decides everything, and they |
| 773 | `any,never` | The sample cannot compensate either. The standard error **never attains the root-T rate at any |
| 775 | `all,every,nothing` | 2.00, and from 400 to 1,600 periods it buys nothing measurable at all. Every term in the estimating |
| 781 | `two` | Two things follow, pointing opposite ways. The first is a defence of the field's specification |
| 783 | `all` | which is the same variation Basu's regression requires in order to run at all; an instrument |
| 784 | `exactly` | conditioning on returns is drawing on exactly the right information, and the return-variance |
| 787 | `every` | The corner in which every term above is worst is a quiet asset whose book amortisation rate sits |
| 788 | `two` | close to its true rate of decline — small σ **together with a small gap between the two rates**. |
| 790 | `two` | because a slow asset stays alive to be observed. §4.8 separates the two and gives the arithmetic. |
| 791 | `both` | What holds of both terms is that a design cannot buy its way out of either — the panel saturates |
| 803 | `two` | regression into a two-component decomposition. That is this section's repair, run empirically |
| 805 | `exactly` | separate a persistent understatement from a delay, which is exactly the separation §4.2 shows a |
| 816 | `two` | the two processes, or an estimated cutoff at which the rate constants exchange — share that shape. |
| 819 | `four,two` | For two of the four classes, the standards already supply that outside determination. Finite-lived |
| 824 | `only` | δ, and compares timeliness only within a life band, is reading φ rather than φδ, and it runs on |
| 828 | `exactly` | sixteen bands and **exactly one clears §5's floor of 30** — thirty-six events from twenty firms |
| 829 | `none` | at a five-year life — with none clearing on firms rather than events. Filling the coverage §5's |
| 830 | `two` | two cycles leave between them — the seven intervening cycles, run — raises the join to **133 |
| 831 | `single` | of the 151** and leaves the same single band clearing: the second band reaches twenty-seven against |
| 832 | `only,two` | the floor of thirty. The registered reading is the only one that gives one — the two other cycle |
| 833 | `two` | choices give two, as does the nearest-cycle rule under the opposite tie-break. |
| 835 | `no,three` | Three properties recommend that design over the one this paper registered. It is diagonal-safe: no |
| 846 | `three` | exogenous, and a firm that reports slowly may also amortise slowly. Three things bound the |
| 850 | `any` | sign of any residual endogeneity is toward finding *less* timeliness variation than exists, not |
| 853 | `two` | **The repair does not reach the two unamortised classes, and it fails them for different reasons.** |
| 855 | `no,nothing` | no life is disclosed and there is nothing to pin δ to — a gap in the evidence, and one a standard |
| 861 | `all,at every,exactly,no` | **exactly** zero at every φ — not small, zero, at all eleven values swept — and no recognition event |
| 862 | `any` | occurs at any φ in 400 periods. **At zero decay, φ is not ill-conditioned. It is absent from the |
| 866 | `two` | is.** The run requires two conditions, not one: δ = 0 *and* an asset whose value does not otherwise |
| 867 | `exactly` | move. Set δ = 0 and let the value receive news, and the gap reopens and φ is recovered exactly — to |
| 869 | `any,never` | not to a slowly-decaying one.** An asset whose value never changes for any reason is not goodwill. |
| 873 | `two` | **What decides whether a class is readable is the gap between the two rates, not either rate alone.** |
| 877 | `no` | realistic amortisation rate the goodwill decay rate is no harder to read than property's — 0.021 |
| 879 | `two` | asset's true rate of decline**, which is hard for the plainest reason in econometrics: the two |
| 881 | `the whole` | so φ is readable to ±0.26 — the whole interval. |
| 883 | `both,two` | The two rates do different jobs and both are needed. The gap sets the level; the decay rate sets how |
| 890 | `two` | That claim has two properties the goodwill version lacks. It is checkable by a reader against a |
| 895 | `no` | Within the deterministic filter, the class the standards decline to amortise produces no recognition |
| 896 | `nothing,single` | events, so the model has nothing to say about it — and the registered test drew its largest single |
| 900 | `any` | easiest. **Which classes this model can speak about is decided by the δ ladder before any hypothesis |
| 903 | `all,none` | **None of this was known when the registration was written, and all of it was derivable.** §5 reports |
| 912 | `everything` | the gap has been open. Everything §4.3 and §4.4 read off that expression — the cross-class ranking, |
| 926 | `exactly,never` | exactly. **The constant hazard was never doing structural work. It was supplying a closed form for |
| 929 | `each,three` | Three checks, each of which could have ended the section. The general form reproduces the published |
| 931 | `each,no` | each aged one period and multiplied by its own P(T ≥ a+1)/P(T ≥ a), no closed form anywhere in the |
| 934 | `at every` | bound. And R(φ)/R(0) = (1 − φ) to **zero**, at every φ on a tenth-grid: φ is a pure scale under |
| 935 | `every,exactly` | age-dependence exactly as it is under memorylessness, so §4.2's proportionality result and every |
| 938 | `exactly` | **What the assumption *was* doing is holding up the domain.** R is finite exactly when |
| 940 | `any,single` | function and therefore on its **tail** — not on its mean, and not on any single rate. For a |
| 942 | `every` | verbatim. For a lag whose hazard *rises*, the survival function outruns every geometric and the |
| 943 | `at every,entire` | generating function is entire: at k̂ = 1.21 the transform is finite at every decay rate swept, up |
| 944 | `no` | to δ = 0.80 per year where it is 7.5 × 10²⁵ and still a number. **The existence condition has no |
| 948 | `both` | both limits at α. An increasing one puts the first at infinity — and a *decreasing* one puts it at |
| 949 | `no` | zero, so a lag distribution with a fattening tail would admit no steady-state deferral measure at |
| 950 | `all,any` | any positive decay rate at all. **The interval [1.135, 1.285] is therefore doing more than |
| 952 | `no` | same fit returned k̂ < 1 the closed form would have had no domain to be restricted to. |
| 956 | `everything` | the domain is everything, that share is one by construction and its complement is empty; a share of |
| 958 | `both` | everywhere and moves in both directions — and does. |
| 962 | `at every` | implicitly makes — the measured distribution defers **less**, at every decay rate, on the direction |
| 975 | `four` | *(φ held at 0.5 throughout, since it is a common scale.)* Across §4.4's tabulated four-tier ladder, |
| 977 | `three` | ASC 350-30-50 disclosure actually spans it reaches **43.9%**, at the three-year life the second of |
| 986 | `three` | forty-year life to **0.476** at a three-year one — a ninth of itself across the asserted rectangle, |
| 988 | `four` | four-tier ladder it moves by six parts in a thousand, which is why the magnitudes there barely move. |
| 989 | `any` | **A recalibration is therefore available and is not a repair:** any comparative static that holds |
| 990 | `single` | α_eff fixed while moving δ is using the wrong derivative, and a single recognition rate quoted for a |
| 994 | `exactly,two` | §4.4's δ₃\* = Kα/(1 + K) generalises exactly, to Π(1/(1 − δ₃\*)) = 1 + K. REG-004 named the two |
| 1002 | `four` | from its own constant-hazard match in the reported series — four orders of magnitude below the |
| 1004 | `exactly,two` | exactly as far from that match's mirror, which is forced rather than discovered, since the two |
| 1011 | `never` | (Little, 1961), and its insensitivity to shape is a property of a *constant* flow. This model never |
| 1017 | `four,three` | three to four years on average, with the delay extending to ten for a third of firms (Hayn and |
| 1020 | `none` | coefficient. In none of it is the recognition lag's **shape** estimated rather than assumed. §5.4 |
| 1022 | `four,three` | one per cent where the paper's own ladder sits, forty-four per cent at a disclosed three-year life, |
| 1023 | `never` | and one domain restriction that was never a fact about disclosure. |
| 1025 | `four` | ### 4.10 · The shape is identified, and the price of admission is four significant figures |
| 1027 | `two` | §4.2 proves an impossibility by counting. A reported series is a sum of two geometrics, so it holds |
| 1028 | `four,two` | four numbers — two roots and two amplitudes — against five parameters, and the shortfall lands on φ. |
| 1032 | `exactly` | constant-hazard world reproduce an age-dependent one exactly? |
| 1034 | `four` | **It leaves a trace, and the trace has a size.** REG-005 registered the question, four falsifiers and |
| 1041 | `three` | quarter** over ten years at a ten-year life, rising to **4.1 × 10⁻³** at a three-year one, with the |
| 1042 | `at every,every` | best mimic an admissible firm at every rate and every φ swept rather than a fit escaping into |
| 1043 | `the whole` | inadmissible parameters. That number is the whole answer in one figure: **it is the precision a |
| 1044 | `all,two` | reported series must carry to reject the constant hazard at all.** Coarser than that and the two |
| 1048 | `each,three` | separate from the measured one, fitting the remaining three parameters freely at each shape: |
| 1055 | `the whole` | | 10⁻² | the whole range swept | ≥ 1.40 | ≥ 9.3 × | |
| 1057 | `two` | *(The lower two rows run into the boundary of the pre-registered sweep, so their widths are lower |
| 1069 | `any,no` | decreasing-hazard lag admits no steady-state deferral measure at any positive decay rate, because its |
| 1072 | `all,any,no` | one in which it has no steady state at all.** That is a sharper limit than any width, and it is the |
| 1075 | `both` | **The identified set and the estimator answer different questions, and both were registered.** The |
| 1076 | `every` | widths above are deterministic and worst-case: every shape that *could* have produced the series. |
| 1079 | `two` | than the event-date interval. The two are not in tension. Forty observations average independent |
| 1088 | `each,single` | reaches its steady state each further quarter repeats a single number — the deferral measure itself — |
| 1090 | `any` | This is an identification property rather than a sample-size one, which is the general result for any |
| 1093 | `exactly` | §5), a statement he makes of exactly the rational lag distributions of which a constant hazard is the |
| 1096 | `three` | **Three recognition rates now live in this paper and they are three different quantities.** |
| 1110 | `three` | a three-year one, where they differ by **15%** and move in opposite directions from α̂. Least squares |
| 1112 | `no,single,three` | dates: three functionals of one distribution, with no obligation to coincide. §4.9 says a single |
| 1113 | `single` | effective rate misstates one end of the asserted rectangle; the series adds that a single |
| 1116 | `all` | **§4.2's exchange survives into all of this, and it is forced rather than discovered.** The mimic |
| 1118 | `any,both,two` | since the theorem makes the two worlds one series and any third series is equidistant from both by |
| 1120 | `each` | worlds fitting within one part in a million of the best spans **0.128 in each root and 0.577 in φ**. |
| 1129 | `four` | infinite-dimensional lag does not disappear into the four numbers; it leaves a residue, and the |
| 1130 | `four` | residue is measurable by anyone who can read a balance sheet to four significant figures. |
| 1132 | `two` | **Two predictions registered in advance were wrong, in the same direction.** REG-005 predicted the |
| 1135 | `three` | and from the classical ill-conditioning of exponential sums, where a three-term signal is reproduced |
| 1136 | `no,two` | by two terms to a few parts in ten thousand with rates bearing no relation to the truth (Lanczos, |
| 1137 | `four` | 1956, as quantified by Varah, 1982). The measured residue is four times larger than that reading |
| 1142 | `single` | restriction and a moment condition (Elbers and Ridder, 1982) — and a single reported series supplies |
| 1143 | `none,three` | none of the three, which is why the answer here had to be measured rather than cited. |
| 1153 | `only` | section at one point only, and that point is §4.5's second half: the model's lag is defined against a |
| 1154 | `no` | physical series that no filing reports, so the instrument below measures a substitute. Read §5 as the |
| 1160 | `no` | question, and no amount of prose does the work of one empirical result. The framework's sharpest available prediction is the one that |
| 1172 | `four` | unit of observation this test did not have. That yields a four-tier ordering, predicted in advance to be monotone in lag: |
| 1181 | `every` | **Every event in this test is a recognised impairment, which places the sample on the boundary |
| 1184 | `no` | accumulation ends — which is why an interval is measurable on these events and on no others. |
| 1187 | `any` | pushed, before any lag was computed; the analysis code did not yet exist. The git history is the |
| 1188 | `entire` | timestamp, and it is the entire evidence that the prediction preceded the outcome — which is why |
| 1201 | `no` | No claim is made here that they were exploited, and the author's account is that they were not. |
| 1203 | `two` | demonstration. A reader is entitled to weight the two differently, and this programme now requires |
| 1209 | `both,two` | The first test (PRE-001) returned a null in both universes, and the two nulls did not even agree |
| 1210 | `each` | with each other. The Jonckheere–Terpstra statistic sums the pairwise Mann–Whitney counts across the ordered tiers, so a |
| 1211 | `no` | tier ordering carrying no information returns z near zero from either direction — which is what happened, |
| 1217 | `no` | neither significant: the signature of a measurement carrying no information about the ordering |
| 1220 | `both` | The instrument was then examined, and it had a defect. Across the 322 events retained by both |
| 1222 | `no` | fewer, and **1,047 charges were discarded for having no measurable onset**. An onset rule requiring |
| 1224 | `only` | phenomenon: the rule can only find an onset when the signal happens to fall monotonically, which is |
| 1232 | `no` | **stopping rule** stating in advance that there would be no third instrument. |
| 1259 | `four` | quarters**, CI [−4.0, +2.5]. Four registered sensitivity analyses per universe are in the run logs; |
| 1260 | `none` | none reverses the verdict. |
| 1266 | `both` | | events retained, both universes | 322 | **688** | |
| 1267 | `no` | | charges discarded for no onset | **1,047** | **0** | |
| 1275 | `four` | predicted to lag longest, carries the least censoring of the four in the replication and the |
| 1285 | `both` | The permutation distribution is centred on zero with unit spread in both universes. The pipeline |
| 1298 | `nothing` | and with certainty in computer services, and it found nothing.** |
| 1300 | `three` | Three qualifications belong immediately next to that sentence rather than in a limitations section, |
| 1304 | `always` | the observed lag distribution and adds a noiseless per-tier shift. The peak rule always finds an |
| 1306 | `any` | than proof of its quality. Any measurement error in the onset attenuates a true gradient, and |
| 1310 | `all` | power simulation all treat events as independent. The effective sample is smaller than 688 and |
| 1312 | `never` | 3. **One quarter per tier was never derived from the model.** It is a plausible round number, not a |
| 1315 | `never` | be well-powered against an effect size the theory never specified. |
| 1318 | `no` | pre-registered, replicated test found no gradient, and if a gradient of the size tested exists it |
| 1320 | `never` | the framework's own predicted effect has been ruled out, because the framework never named that |
| 1325 | `both` | **The shape of the failure, stated as sharply as the data allow.** Both z-statistics are negative, |
| 1326 | `both` | meaning the point estimates ran *opposite* to the predicted ordering in both universes, as they had |
| 1329 | `both` | both universes, with goodwill sitting below it** (5.5 against 5.0 in the pilot, 6.0 against 5.0 in |
| 1334 | `no` | **The stopping rule fired.** There is no third instrument. A hypothesis that requires one on the |
| 1337 | `two` | ### 5.4 · The same sample answers two questions it was not collected for |
| 1340 | `never,two` | questions it was never asked. Two were registered in `REG-003`, committed and pushed before the |
| 1341 | `both` | instrument existed, and both returned. Neither is a re-test of §5.1's prediction and neither may be |
| 1345 | `each` | each firm's latest view of its own history, so a re-pull is not the original pull. Rebuilt: **695 |
| 1346 | `four,three` | events across 307 firms** against 688 across 311, with three of four tier counts identical and |
| 1350 | `both` | **The peak-to-charge recognition rate is 0.41 per year on both known biases' inflating side, and the calibration was low by an order |
| 1352 | `each` | Each event carries the interval from the onset of deterioration to the charge, right-censored at |
| 1356 | `three` | quarters. Retail gives 0.433 and computer services 0.394. The three sensitivities registered with PRE-002 give |
| 1359 | `every` | quarters instead of twenty gives 0.396, 0.398 and 0.404. **Every cut lands in the same regime,** and |
| 1360 | `all` | the calibrated 0.05 is outside the interval of all of them. |
| 1363 | `exactly` | in Nakagawa and Osaki's (1975) parameterisation, whose hazard is increasing exactly when its shape |
| 1369 | `single` | opposite of the memorylessness a single α encodes, and it means α̂ is an average over a window and |
| 1372 | `each,two` | **Two biases push this estimate up, and one pushes it down; the direction of each was registered |
| 1373 | `never,no` | before the number.** A gap that opened and was never recognised leaves no filing, so conditioning on |
| 1376 | `no` | the true one. Against those, the sample contains no lag of zero, so fitting on a support that |
| 1384 | `each` | another, so events should be independent across classes within a firm-quarter. Taking each firm's |
| 1386 | `each,two` | within each firm's own eligible-quarter set — firm-quarters carrying two or more classes are |
| 1388 | `two` | | universe | observed | null mean | central 95% | observed/expected | two-sided *p* | |
| 1393 | `both` | Both universes, the same direction, at the resolution 10,000 draws can report; the design detects an |
| 1396 | `two` | with finite-lived intangibles in computer services (2.22×), and it is these two |
| 1397 | `both` | intangible-with-goodwill cells that replicate across both sectors — 5.83× and 2.41×, 3.33× and |
| 1398 | `all,four` | 2.22×, all four surviving Holm correction. Property with goodwill was published at 4.35× and |
| 1408 | `two` | named it, and it is two readings rather than one.** The ordering is imposed by ASC 350-20-35-31, |
| 1409 | `any` | which requires that any other asset or asset group of a reporting unit be tested before goodwill, |
| 1410 | `every,only` | and by ASC 350-20-35-32, which extends that requirement to every asset tested rather than only to |
| 1414 | `single,two` | single trigger fires two tests. On the other it suppresses joint *recognition*: the other charge is |
| 1418 | `two` | the two charges are substitutes at the margin, and this sample shows them as complements.** Signing |
| 1419 | `two` | the net requires the two charges at the reporting-unit level, which US filings do not disclose; |
| 1420 | `no` | `REG-006` registered an entity-level test of the suppressing channel and it returned no consistent |
| 1423 | `each,only` | a description of the facts and circumstances leading to the impairment only *for each goodwill |
| 1424 | `nothing` | impairment loss recognized*; where a test is run and nothing is charged the Codification compels |
| 1425 | `nothing` | nothing, and disclosure falls to MD&A. A triggering-event population assembled without that |
| 1427 | `both` | does fall — and falls on both arms alike, which is what makes the comparison available — filers |
| 1429 | `all,no` | that took a non-goodwill charge and no goodwill charge, on whom the mandate does not fall at all. |
| 1430 | `three` | Three points across 1,833 classified firm-years measures the vocabulary of the disclosure, not the |
| 1433 | `only` | joint-versus-goodwill-only difference stays at **+0.014** (*p* 0.60) in a design that could have |
| 1434 | `no` | detected 0.068. The reason is countable: **no firm-year in the window writes a sentence naming a |
| 1435 | `any,two` | reporting unit, a trigger, and any of the standard's own (f)-family language**, and the two phrases |
| 1436 | `none` | the Codification uses for that family appear in none of the 1,925 filings. The disclosure does not |
| 1443 | `exactly` | ### 6.1 · The demotion, stated exactly |
| 1451 | `every` | **Unaffected:** every result in §A.2 and §§2–3. Those are properties of a stated model, established by |
| 1455 | `nothing` | **And that sentence is a problem, not a reassurance.** If nothing in §A.2 or §§2–3 was at risk, then |
| 1456 | `every,nothing,only` | nothing in §A.2 or §§2–3 was on test — and a framework that retains every claim after losing its only |
| 1457 | `exactly` | public bet is in exactly the position §6.3 accuses Odum's of occupying. The accounting is therefore: |
| 1460 | `entire` | of observation. That conjunction was the framework's *entire empirical content* as of this |
| 1462 | `everything,never` | - **What was never at risk:** everything in §A.2 and §§2–3, because those are theorems about a |
| 1463 | `never,no` | simulation. They were never capable of losing and no result of the severe test could have |
| 1464 | `one of` | retracted one of them. Calling them "unaffected" states a fact about their logical type, not a |
| 1466 | `no` | - **What follows:** **the framework currently has no confirmed empirical claim.** It has a model |
| 1476 | `any` | the framework made, at one level of aggregation, with one bridge, and lost.* Any surviving version |
| 1479 | `three` | Three post-hoc conjectures about where the conjunction broke are recorded in the repository's |
| 1480 | `each` | working notes. They are excluded from this paper's argument deliberately: **each arrived after the |
| 1481 | `any,none` | number, none is evidence for anything, and any of them that is ever tested must be registered from |
| 1482 | `only` | scratch.** One is worth naming here only because it generalises into a discipline rather than a |
| 1487 | `never,no` | The registration contained a tier table and no **bridge proposition**. It never wrote down, as a |
| 1495 | `no` | different quantities, and they may even be anti-correlated: goodwill carries no schedule, but its |
| 1504 | `every` | must itself be stated as a proposition and checked, and this programme now requires it of every |
| 1510 | `no` | Odum's emergy programme — that emergy's fatal defect was making no risky predictions, and that |
| 1513 | `three` | That argument is withdrawn, on three counts a sceptical reader would have reached first. |
| 1514 | `any,no` | It selects its own reference class: introduce a comparator that made no predictions and any loss |
| 1528 | `no,only` | A paper that reports only its failures gives a reader no way to weigh them. This programme's public |
| 1529 | `every` | record has been unbalanced in that direction: every test run is reported, and until this section |
| 1530 | `none` | existed, none of the ones that held were collected anywhere a reader could find them. Here they are, |
| 1531 | `each` | with what would have killed each. |
| 1535 | `any` | | **D(φ) = (1 − φ)·D(0)** | closed form against simulation, φ swept | any φ at which the ratio departs from (1 − φ) | held to **10⁻¹⁵** | |
| 1536 | `any` | | **(α, δ, φ) ~ (δ, α, φδ/α)** | mirrored simulation, five parameter settings | any visible separation between a series and its mirror | **7 × 10⁻¹⁴** |
| 1537 | `both,two` | | **φδ is the conserved quantity, not (1 − φ)δ** | both candidate maps run against the reported series | the two maps agreeing, which would make the c |
| 1538 | `exactly` | | **An open initial gap does not restore identification** | mirror rebuilt at g₀ = 0.15 with the shifted map | the shifted map failing, or the g₀ = 0  |
| 1539 | `all,any` | | **Unobserved physical scale ⇒ φ free over [0, 1]** | one-parameter family constructed and regenerated | any member of the family failing to reproduc |
| 1540 | `every,two` | | **Returns kill the two-point exchange** | mirror rebuilt with its own asset, return series compared | the two worlds' returns agreeing, which would  |
| 1541 | `any` | | **Returns cannot touch the scale continuum** | the nine-member family regenerated, return series compared across it | any member emitting a differen |
| 1543 | `two` | | **The repair's strength is the asset's, not the analyst's** | σ swept 12×, T swept 32×, at nine (α, δ) settings | the panel buying the root-T rate,  |
| 1544 | `both,two` | | **Neither degradation exponent is a model constant** | both re-fitted over nine (α, δ) settings on the GAAP ladder | the nine agreeing to within fit |
| 1545 | `no` | | **The response to news flattens as decay slows** | |exponent| ranked against δ(α − δ) | no rank relationship, which would make the spread noise | Sp |
| 1547 | `each` | | **The rate gap governs readability; the decay rate does not** | each held fixed while the other is swept, 15× and 16× | the decay rate dominating, w |
| 1548 | `two` | | **The two rates do different jobs** | volatility exponent re-fitted across δ at a fixed rate gap | the exponent being flat across δ, which would col |
| 1550 | `two` | | **The ranking inverts, not just blurs** | 4,000 ladders drawn on the two qualitative facts alone | the intended ordering surviving often enough to b |
| 1552 | `no` | | **The inversion belongs to the ordering; the destruction belongs to the dispersion** | 4,000 ladders with δ drawn independently, no durability order |
| 1553 | `any` | | **τ = −1 is a knife edge in its top rung** | closed form for the crossing rate, verified by bisection to 1 × 10⁻⁹ | a crossing rate far above any de |
| 1554 | `exactly` | | **Lumpy defers more than slow at an identical mean rate** | compound-Poisson decline, 2,000 paths, mean rate matched exactly | the ratio at or below |
| 1556 | `all,any` | | **The *asserted* rectangle lies outside the model's domain *at the calibrated rate*** | useful lives spanning disclosure practice against α = 0.05,  |
| 1557 | `only,two` | | **The rectangle's 99.7% is a property of the assumed support, not of the disclosure** | §4.4's first rung evaluated on 683 disclosed firm-year pairs |
| 1558 | `any,both,every,four,none,three,two` | | **The peak-to-charge recognition rate is an order of magnitude above the calibration** | censored geometric MLE on 695 registered events, two univer |
| 1560 | `no` | | **The closed form survives an age-dependent hazard** | general form against an age-structured simulation carrying the gap as cohorts, no closed form |
| 1561 | `any,exactly` | | **φ is a pure scale under age-dependence too** | R(φ)/R(0) against (1 − φ), φ swept on a tenth-grid | any φ at which the ratio departs | held to **e |
| 1562 | `at every` | | **The domain restriction is the constant hazard's, not the disclosure's** | the transform evaluated to a proven remainder bound across the disclosed |
| 1563 | `three,two` | | **The shape correction is small on the ranked ladder and large at disclosed lives** | measured lag distribution against a geometric of the same mean |
| 1564 | `both,each` | | **The reporting layer is not diagonal** | 10,000 within-firm permutations of which quarters each class's impairments land in | co-occurrence at the  |
| 1565 | `both,four,three` | | **The sample rebuilds from a live endpoint** | full re-pull of both universes a week after the original | drift large enough to make the original un |
| 1567 | `any,exactly` | | **Results are dimensionless** | η swept over **twelve orders of magnitude** | any dimensionless output moving with η | spread **exactly 0.0** | |
| 1568 | `every` | | …and not because η is unused | mutation testing | a mutant that leaves results unchanged | **every substituted vacuous witness killed its run** | |
| 1569 | `no` | | **Recognition frequency is driven by δ** | sweep at fixed φ | δ having no effect on event counts | 0 → 16 → 100 events | |
| 1570 | `no` | | **The tier instrument has no baked-in ordering** | label permutation | a non-null under randomised labels | z-mean **+0.007**, sd 1.025 | |
| 1571 | `three` | | **The registered design had power** | power analysis, to be reported whatever the outcome | power too low to interpret a null | **0.95–1.00**, with  |
| 1572 | `any,four,three` | | **The lag's shape leaves a trace in the reported series** | best admissible constant-hazard mimic, five disclosed lives x four φ | a mimic reproduci |
| 1573 | `any,three` | | **The T = 0 mass is invisible in the reported series** | conditioning on T ≥ 1 against a compensating φ, five lives x three φ | any series moving af |
| 1574 | `no` | | **A decreasing-hazard lag is NOT mimicked by a constant one** | k = 0.5 witness at matched δ and φ | the metric fitting a world with no steady state |
| 1575 | `three` | | **Three recognition rates are three quantities** | series match vs. deferral match vs. event-date MLE across the asserted rectangle | the three agre |
| 1577 | `both,every,two` | | **The departure from diagonality is not an artefact of tier 0's tag list** | §5.4's permutation re-derived with the omitted element restored, both a |
| 1578 | `single` | | **Testing another asset first REDUCES the goodwill charge** | the single-step measurement run against a published worked example | the sequenced and |
| 1579 | `no` | | **The suppressing channel is not visible in entity-level filings** | censored slope of the goodwill charge on the other charge, by sector and by ASU |
| 1580 | `only,two` | | **The disclosed trigger does not separate the two channels** | rate at which filers name the standard's own internal trigger, joint-charge against g |
| 1581 | `no,only` | | **A sharper disclosure instrument finds the quantity absent, not merely unresolved** | sentence-level co-occurrence of a registered trigger phrase w |
| 1583 | `two` | Two rows deserve a comment. |
| 1587 | `every,one of` | null. The check in that row was written to confirm it and refused, in every one of 400 draws, and |
| 1588 | `only` | the claim came out of the paper. A survivals ledger that contains only survivals is an |
| 1599 | `every` | *Every route below was actually taken and then abandoned. The section is placed in the body, not an |
| 1604 | `nothing` | definition, and definitions forbid nothing. Several attempts to repair it by rewording failed |
| 1609 | `any` | one. Abandoned because it is falsified by any case where financial signals *lead* physical change, |
| 1614 | `whole` | volatile than the physical layer. Measured over a whole path this is **false**, and the probe |
| 1633 | `nothing,only` | only where nothing can be checked. |
| 1637 | `only` | recovery is ill-conditioned by construction rather than by bad luck: φ reaches the observable only |
| 1641 | `any,two` | successor has two handles rather than one: **φ becomes tractable as δ grows, and — at any δ — as δ |
| 1644 | `only` | jointly; slow-decaying assets are not, and for those an independent δ is the only handle available. |
| 1648 | `four` | **Adding a free parameter to absorb an objection.** Faced four times across this programme and |
| 1649 | `each` | worth recording as a class, since each instance looked locally reasonable: introducing a scaling |
| 1652 | `any,three` | leaning on an unmeasured φ — three refused, the fourth not. A quantity that can accommodate any |
| 1653 | `nothing` | observation forbids nothing. |
| 1659 | `any` | The strongest standing objection to any lag thesis is efficient-markets in its plainest form: |
| 1661 | `no` | **pure-delay** model has no answer to this and is straightforwardly falsified by cases where |
| 1663 | `single` | a single unit of capital is built, and such cases obviously exist. |
| 1665 | `the whole` | This model is not a pure-delay model, and the asymmetry is the whole mechanism. **The claim layer |
| 1667 | `no` | zero lag, zero deferred information, coupling identically 1, no recognition events. So the objection holds |
| 1668 | `exactly,no,nothing` | *exactly* where the model predicts no lag, and has nothing to act on where degradation is |
| 1669 | `two` | undisclosed. The two are not in competition; they partition the space by φ. |
| 1675 | `every` | low" concedes every case an efficient-markets reader could check and claims every case nobody can, |
| 1676 | `no` | along a coordinate no one has observed. That is a free parameter absorbing an objection, which is |
| 1677 | `three` | the move this programme has refused three times in other costumes (§8) and should have refused here. |
| 1680 | `everything,only` | conceding everything the efficient-markets reading claims and retaining only the unobserved residue |
| 1695 | `exactly` | once, and the magnitude of the discontinuity is exactly the information that had been withheld. That |
| 1696 | `everything` | reading survives everything in this paper. What it does not yet have is a price, an agent, an |
| 1701 | `three` | volatility-relocation result and its 2007 antecedent, the three-cell taxonomy locating the wedge in |
| 1714 | `three` | 1. **The severe test failed and this paper does not know why.** Three post-hoc explanations exist — |
| 1718 | `both` | 2. **The unit mismatch is real, unfixed, and was unfixed by both registrations.** The impairment |
| 1723 | `no,single` | 3. **The filter model is deterministic and single-firm.** No stochastic degradation, no |
| 1724 | `every,no` | heterogeneity, no interaction between firms, no market. Every empirical signature it suggests is |
| 1728 | `single` | Admitting stochastic degradation is the single change to this model most likely to alter what it |
| 1732 | `both` | at 0.408 per year on the registered sample, against the 0.05 swept through the body and on both |
| 1734 | `every` | bridge from that rate to the model's α is the one §6.2 requires of every registration, and this |
| 1739 | `any,no` | any firm's φ is known. That is no longer a concession about this construction: §4.2 establishes |
| 1740 | `no` | that **no** estimator recovers φ from a reported series, because the series does not contain it. |
| 1744 | `only` | preceded the theorem: `docs/notes/NOTE-001-phi-identifiability.md`. Synthetic data only. It is |
| 1759 | `any` | 8. **The framework claims necessary conditions, not uniqueness.** Any adequate account must |
| 1762 | `only` | argued to be the only one that does. |
| 1772 | `both` | registered sample and rejects it in both universes in the same direction, at **4.12×** and |
| 1777 | `every` | standards impose — though that sequencing, imposed by ASC 350-20-35-31 and extended to every |
| 1778 | `two` | asset class by 35-32, is itself two channels of opposite sign, one creating joint testing and |
| 1808 | `exactly,nothing` | beneath. *r > g* may hold exactly as described at the abstraction layer while saying nothing about |
| 1810 | `two` | makes the two accounts complementary rather than rival. |
| 1815 | `exactly` | than moral; §2 is a formalisation of exactly that concern. Mises's malinvestment — misallocated |
| 1819 | `single` | claim made here is a structural analogy, not an identity. What it offers is a single mechanism |
| 1820 | `each` | reproducing a phenomenon that mutually hostile traditions each describe in their own vocabulary. |
| 1830 | `only` | only the undisclosed residue. |
| 1838 | `both` | extended both continuously since. **That is §3.2 in a different vocabulary, and on evidence this |
| 1839 | `two` | paper is much the weaker of the two accounts**: crash risk is measured on prices, tested on large |
| 1846 | `no` | themselves set out and this paper claims no priority over.** Before their model begins, they consider |
| 1847 | `always,never` | an opaque firm run by "a saintly manager who always acts in shareholders' interest, never taking a |
| 1853 | `all` | > released all at once, like a pressure vessel letting off steam." |
| 1855 | `all` | **Accumulation to a threshold and release all at once, with the agency conflict switched off, was |
| 1856 | `no` | written down in 2004.** No claim of priority over it is made here, and an earlier draft of this |
| 1861 | `no` | the news as it happens." Their friction is verifiability toward outsiders; §2's manager knows no more |
| 1863 | `only,three,two` | unrecognised unknown degradation are three objects, and only the third is §2's.** Two further |
| 1864 | `two` | differences follow from the same page rather than from a defence of it. Their case is **two-sided** — |
| 1867 | `any,no` | crash results are then identified. And it has no accounting layer of any kind; the working paper |
| 1868 | `no` | contains no occurrence of *goodwill*, *intangible*, *impair*, *GAAP*, *book value* or *historic |
| 1870 | `only` | footnote attached to that assumption concedes only depreciation "according to a pre-defined |
| 1871 | `no` | schedule" — which, being common knowledge, enters value and price identically and opens no wedge at |
| 1872 | `all` | all. |
| 1878 | `exactly` | regulatory regime, and the post-SOX dissipation Hutton, Marcus and Tehranian report is exactly that |
| 1896 | `two` | **Two things must be conceded here, or §2's claim is not narrow but wrong.** |
| 1902 | `only` | physical layer that only degrades. That assumption is not by itself sufficient — degradation at a |
| 1903 | `two` | stochastic rate around a booked rate produces a two-signed reporting error, which is Jin and Myers' |
| 1904 | `no` | case again, long tails and no skew. What makes the wedge one-signed is a second condition, that |
| 1906 | `no` | in, no upward revaluation of property, plant and equipment, and no impairment reversal for |
| 1913 | `nothing` | correspondingly restricted to degradation on which conservatism has nothing further to bite — |
| 1914 | `no` | carrying no impairment trigger, no estimable expected loss and no observable event to key recognition |
| 1915 | `nothing` | to. Where a loss is estimable, recognition is faster than the market and §2 predicts nothing. |
| 1920 | `only` | "accumulate[s] and only eventually materialize[s]," and greater opacity produces more frequent and |
| 1923 | `only` | stability, volatility actually accumulates only to hit the market at a later date," transferring |
| 1926 | `two` | private benefit while knowing it will not recover, and their regimes are two discrete alternatives |
| 1936 | `the whole` | coefficient cannot. **The ordering remains the whole of the claim — the recognition event is the |
| 1948 | `all` | registration, the negative control, the power analysis and the stopping rule are all conventional, |
| 1949 | `nothing` | and are claimed as nothing more than that. |
| 1955 | `every,only` | Every simulation result in §A.2 and §2 is produced by open code. The severe test in §5 uses only |
| 1966 | `the whole` | - **Test suite:** `python3 -m pytest tests/ -q` runs the whole repository; at the pinned commit |
| 1967 | `every` | **d655501** — the state that produced every result in §A.2 and §2 — that suite held **100** tests, |
| 1970 | `only` | remaining 38 hold a companion paper's claims and are named here only because a suite total is a |
| 1971 | `any,both` | property of the repository and not of any one paper in it. Both counts are derived from the |
| 1973 | `every` | drifts. The suite at the head of the repository is much larger — it grows with every registration |
| 1974 | `three` | in `docs/preregistration/`, which is why the paper-scoped count is the one quoted; three of its |
| 1976 | `no,two` | guard claims this paper makes and change no model code: two for §3.1's |
| 1978 | `no` | and one asserting the algebraic collapse §4 publishes — which had no test until an |
| 1980 | `every,none` | - **Hardware:** none required. Every figure in §A.2 and §2 regenerates on a commodity CPU in seconds. |
| 1981 | `four,two` | The fits reported in §4 use two thousand synthetic firms at four hundred gradient steps |
| 1982 | `three` | in double precision; a larger reference fit of ten thousand firms at three hundred steps |
| 1983 | `two` | completed in **76 seconds on two 2.8 GHz cores**, a machine chosen deliberately so the figure is |
| 1984 | `no,none` | an upper bound. No accelerator is used and none is needed. |
| 1986 | `no` | Sets for the CIK→SIC mapping including dead registrants. No proprietary or restricted data is |
| 1989 | `nothing,single` | commit **9722342** — a single-file commit containing the registration and nothing else · |
| 1995 | `each,only` | (its only commit) and `src/wealth_tensor/lambda_sensitivity.py` at **b9089c7** — each |
| 1996 | `whole` | verifiable with `git log -1 --format=%h <sha> -- <path>`. `src/` as a whole has moved since, |
| 2003 | `each` | - **Data retrieval, pinned.** `companyfacts` serves each firm's *latest* view of its own |
| 2004 | `every` | history, so a re-pull is not the original pull and the sample grows with every filing — |
| 2017 | `two` | Two tests are worth naming because of what they forbid rather than what they check. |
| 2018 | `any` | `test_pre001_constants_are_what_was_registered` fails if any registered constant is edited, so a |
| 2021 | `both,solely` | `test_a_flat_gini_does_not_mean_a_bounded_one`, both of which exist solely to make overclaiming |
| 2032 | `three` | *Three propositions about the composition of wealth, and the coupling they oblige. This material |
| 2033 | `two` | motivated the filter and is retained in full: it states the domain within which §2's two layers are |
| 2034 | `two` | the right two layers, and it carries the invariance evidence the ledger in §7 cites. It is an |
| 2035 | `nothing` | appendix rather than a section because **nothing in §§2–7 depends on it.** The identification |
| 2036 | `any,two` | result holds for any two-layer filter of the stated form, whatever one believes about the |
| 2039 | `three` | ## A.1 · Three propositions |
| 2053 | `no` | and definitions generate no empirical content. The useful notion is the one from computing: a |
| 2054 | `never` | **invariant** — never proved undeniable, proved *preserved*, within a **stated domain**. "Sound |
| 2063 | `every` | depreciation** — δK appears in every growth model from Solow forward, and claiming otherwise would |
| 2064 | `exactly` | be an error of exactly the kind §6.2 is about. What P3 puts at issue is different and narrower: |
| 2070 | `three` | commitment actually bites. The three propositions below are offered as principles on that test. |
| 2074 | `every` | > **P1 · Composition.** Every unit of wealth is a compound of a physical component and a claim |
| 2077 | `any` | > *Domain:* units of wealth having any physical referent. Silent on purely contractual objects |
| 2080 | `no` | > **P2 · Decay.** The physical component degrades absent maintenance. No store is inert. |
| 2085 | `no` | > **P3 · Atomism.** Measured aggregates are folds over units. No aggregate is more fundamental |
| 2088 | `any` | > *Domain:* any measurement presented as a property of an economy rather than of a population. |
| 2091 | `each,no,three` | Three, not ten. Each is stated so that a competent economist can say *no* to it and mean something |
| 2097 | `each` | by assertion. Here it is demonstrated, because the regimes in which each proposition fails are |
| 2101 | `all,no` | so a fully maintained asset has no dynamics at all and the model collapses to an identity. This |
| 2102 | `no` | is the regime in which "no store is inert" is simply not true, and it is reachable by setting one |
| 2105 | `entire` | important point. Perfect observability annihilates the entire phenomenon: recognition lag 0, |
| 2108 | `everything` | over 400 periods). What vanishes is the *gap*, and therefore everything this paper is about. |
| 2116 | `no` | than definitional. It is not itself a refutation, and no refutation is offered here. |
| 2123 | `all,never` | released at rate α, while what a levy's base fails to recognise is never assessed at all, and a |
| 2124 | `no,two` | levy has no parameter that plays α's part. The two results share the question and not the |
| 2131 | `only` | P1 concerns composition and is silent about time. P2 concerns time and presupposes only that a |
| 2134 | `both,single` | different scales and is independent of both: an economy of inert single-component units would |
| 2135 | `each,no` | satisfy P3 while violating P1 and P2. No proposition is derivable from the others, and each is |
| 2142 | `three` | *This section is where Λ is defended. It is defended here, at full strength, on three independent |
| 2150 | `two` | **Notation, stated before the argument because two different objects have been sharing one symbol |
| 2154 | `both` | - **λ = C/E** is **dimensionless** — a ratio of the claim measure to the physical measure once both |
| 2161 | `everything` | Conflating them is easy and this paper has done it before. Everything below is explicit about which |
| 2164 | `two` | **The entailment argument, and its actual reach.** If P1 holds, wealth is a compound of two |
| 2165 | `any` | components measured in different units, so *some* relation between them exists in any unit of |
| 2172 | `all,no` | at all — and P1's own wording, *obeying different laws*, is if anything a reason to expect that no |
| 2173 | `single` | single constant suffices. So the honest version of this leg is narrower than the version this |
| 2176 | `no` | prove.** What follows in §A.2.3 is a demonstration that no conclusion here depends on the scalar's |
| 2178 | `exactly` | and the difference is exactly the kind of thing §6.2 will show this programme has previously |
| 2189 | `exactly,nothing` | That series has **the dimensions of Λ⁻¹**, and the claim made here is exactly that and nothing |
| 2190 | `two` | more. It is emphatically **not** that SDG 7.3.1 measures Λ⁻¹. The two differ in a way this paper is |
| 2192 | `two` | two stocks** (a claim stock in currency over a physical stock in joules), while **SDG 7.3.1 is a |
| 2193 | `two` | ratio of two flows** (annual primary energy over annual PPP output). Two quantities can share |
| 2195 | `no` | that error is in no position to commit it a second time in its own defence. |
| 2198 | `no` | an exotic dimension and not this author's coinage.** An institution with no stake in this framework |
| 2205 | `no` | If, as §A.2.3 demonstrates, no conclusion in this paper depends on the coupling's value, then |
| 2206 | `any,two` | anchoring that value to a published statistic cannot be load-bearing for any result here. The two |
| 2208 | `only` | made up"*, and this section answers *"the dimension you are working in is invented"* — and only the |
| 2209 | `nothing` | first is doing work for the results. A reader who finds this section unconvincing loses nothing |
| 2214 | `exactly` | The dimensional objection can be answered by algebra, and algebra is exactly what a sceptical |
| 2215 | `two` | reviewer declines to take on trust. So the two-layer system of §2 is **dressed in units** — the |
| 2224 | `at every` | | diagnostic | value at every η | spread across the sweep | |
| 2233 | `never` | Not "within tolerance." **Bit-identical**, because the coupling never enters the recursion; it is |
| 2237 | `never,nothing` | build a module in which nothing depends on a parameter *because the parameter is never used*. So |
| 2239 | `exactly` | **do** move, and they move exactly as a unit conversion must: |
| 2246 | `no` | η is used, the currency figures track it linearly to twelve decimal places, and no conclusion moves |
| 2247 | `all,both,four` | at all. Both directions are mutation-tested: leaking η into the dynamics fails four tests, and |
| 2248 | `two` | removing the scaling fails two. |
| 2250 | `two` | **Scaling collapse.** Two systems differing in energy scale (1 J against 6.02 × 10²³ J) *and* in |
| 2251 | `every,single` | coupling (10⁻⁶ against 42) lie on a single dimensionless curve — every diagnostic identical, pairwise |
| 2252 | `exactly` | difference **exactly 0**, at φ = 0.3 over 300 periods. (The shorter horizon is inherited from the |
| 2258 | `every` | coefficient is a numeraire; every result reported here is invariant to it across twelve orders of |
| 2259 | `every,exactly` | magnitude, while every currency-denominated quantity scales with it exactly linearly.* |
| 2264 | `nothing` | dimensional **Λ = η·C/E** swept in §A.2.3. The numeraire enters nothing below.* |
| 2266 | `never,nothing` | A freely-varying λ that is never pinned would forbid nothing, and a quantity that forbids nothing |
| 2267 | `three` | is the free parameter this programme has refused three times in other costumes. So the claim is not |
| 2279 | `all,at every,exactly` | | λ = 1 exactly at every recognition event | **yes, all 16** | |
| 2281 | `only` | **λ equals its physical value only at the instants the claim layer snaps to the physical one, and |
| 2295 | `no` | priority rests on it, the entry is **dual-dated** `original/consulted`. A reprint that changes no |
| 2303 | `none` | survives a bibliographic check intact: the article exists, with those details, and none of that is |
| 2311 | `any` | version; any quotation is attributed to the version read and may not appear in the article of record. |
| 2318 | `both` | takes both the 5.5%→27% figure and the universe split from it directly: the 27% is the |
| 2325 | `nothing` | article, which earlier revisions of this entry could not obtain. Nothing is quoted from it.)* |
| 2336 | `one of` | direct rebuttal of the invalidity critiques. Asset maturity is one of several examples they give of a |
| 2337 | `no` | comparative static, not their headline; §4.6 is worded accordingly. **No page is cited**: the text |
| 2340 | `every,nothing,two` | Accounting Review*) refused every retrieval route attempted, so nothing is quoted beyond the two |
| 2341 | `no` | phrases above and no absence is claimed of the typeset article.)* |
| 2345 | `nothing,only` | *(Cited for the function that bears its name and for nothing else; §4.2 characterises only the |
| 2347 | `no` | the author's own copy, and no text is quoted.)* |
| 2377 | `two` | paper's equation (6.2) — a hazard bounded between two constants bounds the survival function |
| 2383 | `no` | page — vol. 45 no. 2, May 2007, DOI 10.1111/j.1475-679X.2007.00231.x — so it is the typeset article |
| 2384 | `both` | and not a pre-publication version. §4.4 and §10 both cite it against this paper: it states §4.4's |
| 2395 | `nothing,two` | two independent secondary sources that state it identically, and the entry claims nothing beyond |
| 2396 | `none,single,three` | it. The point §4.10 draws is that a single reported series supplies none of the three, which is |
| 2410 | `nothing` | level; nothing is quoted.)* |
| 2414 | `no` | not an edition, so no dual date.)* |
| 2424 | `both` | both for C_Score and for its reported association between longer investment cycles and higher |
| 2433 | `two` | parameter values but a partial permutation of the set"; §4.2 carries that qualification too. Two |
| 2434 | `no,three` | short phrases are quoted; no page is cited, the article running to three pages without internal |
| 2440 | `three` | Anderson working-paper version, read in full for the decomposition, the three named confounders and |
| 2442 | `no,nothing` | nothing interior to their coefficient B is asserted here and no page is cited. Pagination of the |
| 2451 | `no` | read in full, and on secondary accounts. No quotation is taken from it.)* |
| 2454 | `two` | Accounting, Auditing & Finance*, 21(3), 223–265. ✓ *(§4.9 cites it for the two figures its abstract |
| 2455 | `four,three` | states: goodwill write-offs lag the economic impairment of goodwill by an average of three to four |
| 2463 | `any` | any desired accuracy by a rational lag function, of which a constant hazard is the lowest-order |
| 2466 | `nothing` | verbatim; the body was not read and nothing else is attributed to it.)* |
| 2470 | `no` | exponential-sum fitting. **Not read**, and the entry carries no verification mark for that reason: |
| 2471 | `every,no` | every copy located was lending-restricted and no full text was obtained. The page range is from the |
| 2472 | `everything` | NIST Statistical Reference Datasets documentation of the same example, and everything §4.10 draws |
| 2473 | `nothing` | from it is drawn through Varah (1982), which quotes it with page citations. Nothing here rests on |
| 2479 | `never` | requires: a constant arrival rate. This model never has one, which is why its deferral measure is a |
| 2481 | `nothing` | nothing is quoted.)* |
| 2495 | `exactly` | parameterisation P(T ≥ t) = q^(t^k) the source defines, whose discrete hazard is increasing exactly |
| 2501 | `each` | treatment of impairment *timing*: their design tracks each acquisition to its first impairment |
| 2503 | `no` | It is cited for what it is and for what it is not — a covariate model with no baseline shape |
| 2515 | `no` | consulted is the open FTC Bureau of Economics Working Paper No. 94, June 1983, read in full; the |
| 2516 | `nothing` | published comment is verified bibliographically and has not been read. Nothing is quoted.)* |
| 2521 | `two` | 417, which corrects two typesetting errors in equation (5) — a "+" printed for the "=", and |
| 2522 | `no` | ΔMV_{i,t−10} printed for BV_{i,t−10} — and changes no coefficient, hypothesis or result. The |
| 2529 | `solely` | 511–525. ✓ *(Cited in §4.6 solely to distinguish a near-identical title. **Read at source.** The |
| 2532 | `nothing` | the empirical sense of detecting conservatism in data. Nothing is quoted.)* |
| 2539 | `exactly` | distributions (see Jorgenson (1966))" as exactly the approximating class the result covers, p. 1628. |
| 2543 | `both` | "essentially" — this entry is commonly miscited on both counts.**)* |
| 2547 | `all` | quantified form of Lanczos's example, and it is the route by which Lanczos is cited at all. **Read |
| 2549 | `three` | and reports the Hessian's smallest eigenvalue falling by roughly three orders of magnitude per |
| 2557 | `every` | here — symmetry of every systematic coefficient in β ↔ γ, asymmetry of the disturbance — was |
| 2559 | `nothing` | taken from Nerlove's text, and the entry claims nothing beyond the model's structure. A session with |
| 2564 | `nothing` | *Journal of Financial Economics*, 94(1), 67–86. ✓ *(Nothing is quoted from the body, which was read |
| 2576 | `only` | **p. 262**, character for character; an earlier revision of this entry recorded it as checked only |
| 2578 | `no` | had not. §10 quotes the sentence because it is what establishes that the model has no physical layer, |
| 2581 | `exactly` | as an easy extension, and it is the interaction of exactly that schedule with recognition timeliness |
| 2587 | `one of,two` | Mann, H. B., & Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically |
| 2594 | `both` | has not read. Both the edition-consulted rule and the first-appearance rule select 1996, and they agree |
| 2625 | `two` | Quine, W. V. O. (1951). Two dogmas of empiricism. *Philosophical Review*, 60(1), 20–43. ✓ |
| 2636 | `no,none` | not in the author's library. No claim of priority is made in the text, so none is made here.)* |
| 2647 | `nothing` | reason. Nothing is quoted.)* |
| 2650 | `nothing` | reader nothing. The per-entry findings live in the ✓, ✓✎ and ✓⧗ notes above, attached to the entries they |
| 2653 | `each,four` | **Four passes ran, in this order, and each one found what the previous ones structurally could not.** |
| 2655 | `every` | 1. **Bibliographic.** Every entry checked against a publisher page, a library catalogue, a Crossref |
| 2658 | `any,every` | 2. **Cited-in-text.** Every entry checked against the body. It asks *does this reference do any work?* |
| 2660 | `exactly` | removed rather than retro-fitted, because a reference kept for the look of the list is exactly the |
| 2662 | `every` | 3. **Provenance.** Every entry checked against the author's own copy. It asks *is this the object the |
| 2665 | `two` | surname matched a different scholar entirely. Two entries were corrected, reverted, and corrected |
| 2669 | `both` | of record?* — which passes 1 and 3 both leave open, the first because the article exists either |
| 2672 | `single` | though they were the published articles. Hence **✓⧗**, and hence the single surviving quotation in |
| 2676 | `two` | evidence of a correct *bibliography*. The two are different documents that happen to share a page. |
| 2681 | `every` | pass came back clean — every work exists, with those details, from a publisher or a catalogue. The |
| 2682 | `three` | provenance pass an hour later found that **three of the five books present in the author's library |
| 2683 | `both` | were being cited as the wrong object**. Both passes were correct; they answer different questions, and |
| 2684 | `only` | only the second one asks whether the citation points at the thing that was read. See `LEDGER.md` |

TOTAL: 864 tokens / 668 lines
