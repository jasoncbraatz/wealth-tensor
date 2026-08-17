# REVIEW-006 · `P7` CONVERGENCE PASS 2 — the re-grade, and the first independent read

*wealthTensor-63 · 2026-08-17 · the second `P7` pass. Its two halves were both required and they
returned opposite verdicts: **-62's repairs all hold**, and **the paper -62 left cleanest is the one
that was least read.** Eight new findings, all eight repaired. `III-3` is settled and closed.*

---

## 0 · What this pass is

`-62`'s pass 1 was a **backlog drain**: it scored thirty-two items that two blind builders and one
card had already surfaced. It was not an independent read of the manuscripts, and it said so. This
pass is the two things that leaves owing:

**(a) Re-grade `-62`'s repairs.** `-58`'s precedent disqualifies a session from scoring its own
repairs; it does not disqualify this one.
**(b) Read what pass 1 did not.** Paper IV had never been read end-to-end by anyone asking `P7`'s
question. Paper III §A.2.3–A.2.4 had been read only for the α and SDG threads. `REVIEW-004` `C6`
and `C10` had been re-served by nobody.

**Result: 8 new findings, 8 repaired. `III-3` settled with an outside fact and repaired at four
sites. No paper earns a zero pass. Consecutive-zero count stays 0 for all three.**

---

## 1 · THE RE-GRADE — all of `-62`'s repairs hold, and there are seven of them, not eight

Every repair was diffed against its `.bak-wt62-p7` snapshot before being read, per `-61`'s standing
order that a corpus under repair has a moving referent and only the filesystem knows.

| item | verdict | check that settled it |
|---|---|---|
| `IV-1` α = 0.05 disclosure | **HOLDS** | 0.408 and *"low by an order of magnitude"* are Paper III §5.4's own words, verified in source |
| `IV-2` domains | **HOLDS** | `§A.1.2` resolves to Paper III L2067; P1's domain carried faithfully |
| `IV-3` two constraints | **HOLDS on the count** | but introduced a regression — see `IV-8` below |
| `IV-4` SDG/Λ⁻¹ | **HOLDS** | quotes Paper III §A.2.2 exactly, including the *"emphatically not"* |
| `III-1` 4.2× | **HOLDS, and is robust** | see below |
| `III-2` significance level | **HOLDS** | α now carries one referent in §5.2 |
| `II-1` provenance pin | **HOLDS** | the pin now excludes the two `scripts/` commands in terms |

**`III-1` deserves its own line, because it survives a check it was not built to survive.** The
repaired abstract reads *"δ leverage is **4.2** times the level at which recovery fails."* §4.4
defines *δ leverage* as the mean per-rung |Δlog δ − Δlog(α − δ)| — **1.193** on the tabulated
ladder — while 0.61 and 2.58 are leverage-to-*budget* ratios. Read literally the sentence compares
a leverage against a ratio. It is nonetheless correct **under both readings**, because the
comparison is scale-invariant: (2.58 / 0.61) = 1.193 / (0.61 × 0.463) = **4.22**. A referee taking
either reading gets 4.2. Recorded because the next session should not re-derive it.

**What does not hold is the arithmetic of the document that reports them.** `REVIEW-005` §0 says
*"Eight are repaired here"*; §1 heads Paper IV *"five"*; §5 reports *"Paper IV — pass 1 run, 5
findings."* §1 documents **`IV-1` … `IV-4`, `III-1`, `III-2`, `II-1` — seven items, four of them
Paper IV's.** The `bak-wt62-p7` → live diff of Paper IV contains **five hunks**, and all five map
onto those four items (`IV-2` produced two, the §A.1.2 pointer and the carried domain). **There is
no undocumented edit** — §6's "what was touched" is complete and the manuscripts are auditable.
The count is simply one high, and it propagates: eleven live is **ten**, and twenty-one dismissed
of thirty-two is **twenty-two**.

`REVIEW-005` is a dated, signed record and this pass does not edit it — the same discipline by
which it scored `E2` from outside. The correction is recorded here and in `LEDGER.md`.

---

## 2 · `III-3` · SETTLED WITH AN OUTSIDE FACT, AND REPAIRED

`-62` left this deliberately, and was right to: *"weakening a headline claim on a guess is worse
than leaving it flagged."* It needed one answer, and the answer is **no**.

**ASC 350-30-35-15**: *"If an intangible asset is determined to have an indefinite useful life, it
shall not be amortized until its useful life is determined to be no longer indefinite."* Such
assets are assigned **no finite useful life**, are **not amortised**, and the disclosure regime
requires carrying amounts and impairment-testing documentation — **no useful life, no amortisation
period, no schedule**. There is no route by which the standards supply an outside determination
of δ for indefinite-lived intangibles.

**And the paper already knew.** §4.4, four sections above the defect:

> *"**Two rungs need no inference at all, and they are the two that break the table.** ASC 360 and
> ASC 350-30-50 require disclosure of useful lives for property and for finite-lived intangibles."*

**Two** in §4.4; **three** in §4.7; the abstract inherits the three as *"every class but goodwill."*
The paper contradicts itself across four sections, and the version that reaches a referee first is
the wrong one.

**Repaired at four sites**, and the repair makes §4.8 sharper rather than weaker, because the two
unrescued classes fail for genuinely different reasons:

1. §4.7 *"For three of the four classes"* → *"For two of the four classes."*
2. §4.7's closing *"The class the repair cannot rescue is goodwill"* → both classes named, with
   indefinite-lived intangibles' failure attributed to the absent disclosure (a gap a standard
   could close) and goodwill's to δ = 0 (which no standard can).
3. The abstract: *"restoring φ for every class but goodwill, where at δ = 0 the parameter is
   absent"* → *"restoring φ for the two amortised classes; at δ = 0 goodwill's parameter is
   absent."*

**The abstract repair cost −1 word.** Paper III stood at 248 of 250; it now stands at **247**. This
is the first correction in three sessions to *return* slack to the ceiling `REVIEW-005` §7 warned
about, and it did so by deleting a false generalisation — which is the direction §7 said the
ceiling was pushing the corpus away from.

---

## 3 · NEW FINDINGS — eight, all repaired

### Paper III — two

**`III-4` · §A.2.4 is written entirely in the wrong symbol, in the one section §A.2.1's notation
block was built to protect. THE SHARPEST FINDING IN THIS PASS.**
§A.2.1 opens with an explicit disambiguation, and states why:

> *"**Notation, stated before the argument because two different objects have been sharing one
> symbol in this programme's working notes.** … **λ = C/E** is **dimensionless** … **This is the
> object §A.2.4 reports as a sawtooth**… **Λ = η·C/E** is **dimensional** … the object §A.2.3
> sweeps. **Conflating them is easy and this paper has done it before. Everything below is explicit
> about which is meant.**"*

§A.2.1's own closing pointer obeys the rule — *"λ is not stable, and §A.2.4 shows what shape its
instability takes."* **§A.2.4 then uses `Λ` ten times and `λ` zero times.** The numbers convict it
independently: minimum **1.000000**, *"Λ = 1 exactly at every recognition event"*, floor *"pinned at
unity by construction"* — a dimensional currency-per-joule quantity cannot be pinned at unity
except by setting η = 1, and **`η = 1` occurs zero times in the manuscript** (normalised check).
The paper writes the rule, names the section the rule is for, and breaks it in that section.
**This is `II-1`'s exact shape** — a provenance rule stated and broken eleven lines later — one
paper over, in the appendix, and it survived every prior pass because nobody read §A.2.4.
**`.bak` provenance:** both the §A.2.1 notation block and the §A.2.4 heading are present in every
snapshot back to `bak-pre-wt110-c21`. **This is old and stable, not freshly introduced** — checked
before asserting, per `-62`'s two-directional line-wrap warning.
**Repaired**: ten sites to `λ`, plus a one-line gauge note naming the object and pointing at
§A.2.3 for the dimensional one. A precision fix rode along: mean λ = 1.136838 is the mean **across
the run**, not *"on average in between"* the events — the run includes the sixteen instants where
λ = 1 by construction.

**`III-5` · §10's one-signedness ratchet is stated without the jurisdiction that makes it true.**
Re-serving `REVIEW-004` `C10`. The manuscript:

> *"What makes the wedge one-signed is a second condition, that reported value may fall and may not
> rise: no upward revaluation of property, plant and equipment, no impairment reversal for goodwill
> or indefinite-lived intangibles."*

This is an unqualified assertion — not a stipulation, not a conditional antecedent — and **two of
its three limbs are jurisdiction-specific**. IAS 16 permits the revaluation model; IAS 36 *requires*
reversal for non-goodwill assets. Only the goodwill limb holds in both regimes. The load-bearing
condition of the whole one-signedness argument is stated more generally than it is true, and the
paper's only jurisdictional scoping is a *sample* statement in §6.1, 460 lines away, about the
empirical test rather than the mechanism. `IFRS`, `IAS`, `IAS 36` and `US GAAP` each occur **zero**
times (normalised). **Repaired**: the condition now names US GAAP as the regime the sample files
in, states IAS 36 and IAS 16 as the contrast, and closes *"one-signed for these filers and is not
general."*
*(`C10` also offers a cross-regime registration as a free institutional instrument. **Not taken** —
that is a new registration and wants its own at-bat. Carded.)*

### Paper IV — six

Paper IV was the pass-2 zero-pass candidate: all four of its pass-1 findings were repaired and
none were `DECISION-001`-blocked. **It was read independently for the first time and it is not
close.**

**`IV-5` · §1.1 points at §6 for content that is in §7, and the paper's own contribution list says
§7.** L93: *"§6 states it as a method rather than leaving it as a habit."* §6 is *"The whitespace,
measured"* — a citation-graph measurement containing nothing about relocation. The method is §7,
*"Relation to existing work, and the method used to state it."* The paper contradicts itself
twenty-four lines later at L117: *"5. **A stated method** (§7)."* **Repaired**: `§6` → `§7`.

**`IV-6` · §4.3 attributes to Hildenbrand and Grandmont the reverse of their result.** L295:
*"The response to SMD in practice has been to **restrict preference heterogeneity** until the
aggregate is well-behaved — **Hildenbrand and Grandmont**, and the representative agent as **the
limiting case**."* Both run the other way: sufficient **dispersion** is what restores well-behaved
aggregate demand. Princeton University Press's own description of Hildenbrand (1994): *"The Law of
Demand is due mainly to the 'heterogeneity' of the population of households. In his view,
'rationality' of individual behavior plays only a minor role,"* on hypotheses of *"increasing
dispersion"* and *"increasing spread."* **The paper's own reference list gives it away** — L654:
*"Grandmont, J.-M. (1992). Transformations of the commodity space, **behavioral heterogeneity**,
and the aggregation problem."* Placing them on a ray whose limiting case is the representative
agent inverts both. **This is the most expensive class of error in the corpus** — a misattribution
to named scholars, in print, verifiable in one search. The paragraph's conclusion survives the
correction untouched, so the repair is narrow. **Repaired**: *"impose distributional restrictions
… where it is sufficient dispersion of household characteristics that does the work, and the
representative agent as the degenerate case at the other end."*

**`IV-7` · three named sources have no reference entry.** `Piketty` (L443), `Chatterjee` (L476)
and `Aumann` (L536) each occur **exactly once in the whole file** (normalised) — in the body, never
in the References. Chatterjee and Chakrabarti is additionally a **`REG-013` seed**, which makes its
absence a provenance gap and not only a courtesy one. **Repaired**: three entries added — Piketty
carried verbatim from Paper III's ✓-verified entry, Chatterjee and Chakrabarti from Paper II's,
Aumann (1964) *Econometrica* 32(1–2), 39–50.

**`IV-8` · `-62`'s `IV-3` repair introduced an ambiguity that reads as a flat contradiction.**
The repaired text lists the **two** constraints that lapsed, then says *"**The second** has no lapse
to report."* The intended referent is the second of the **three** original constraints; the nearest
enumeration is the two that did lapse, under which *"the second"* is SDG 7.3.1 — which the same
sentence has just said *did* lapse. Diffed against `bak-wt62-p7`: the sentence did not exist before
the `IV-3` repair. **A repair that fixed a count introduced a referent.** **Repaired**: the
constraint is now named outright.

**`IV-9` · "No new code" is contradicted by §10's own instrument.** L122: *"**No new code and no
new simulation.**"* §10: *"**Instrument:** `scripts/reg013_citation_whitespace.py`"*, pinned at
`5efe626`, with the pre-registration *"committed in `fff7063`, **before the instrument existed**."*
The paper's own data-availability section is the byte that convicts it. The intended claim — no new
*model* code — is defensible and true. **Repaired**: one word, *"No new model code."*

**`IV-10` · §8's series arithmetic is off by one against its own opening words.** The entry opens
*"**A fourth paper**, on price formation"* and closes *"had the route worked, this paper would be
**the fifth** in a series rather than the third."* Three ship; add one and this paper is the
**fourth**. No numbering convention in the corpus yields five. **Repaired**: `fifth` → `fourth`.

*(A seventh candidate — δ used twice in Paper IV and glossed nowhere — is real but minor; it was
repaired in the same anchor as `IV-5`'s neighbour at zero extra cost rather than carded.)*

---

## 4 · WHAT THIS PASS'S OWN INSTRUMENT GOT WRONG

`-61`'s order is to point the check at the reviewer's output first, not last. Two of this pass's
own instrument's claims failed re-verification and are recorded rather than dropped:

1. **An independent reader measured Paper IV's abstract at 243 words, "seven under the ceiling."**
   `scripts/check_abstract_size.py` returns **248**. The reader had counted by hand. Had a repair
   been sized against 243, it would have been budgeted five words of slack that do not exist — and
   `REVIEW-005` §7 is the record of what that costs. **The checker is the only measurement that
   counts, on every abstract, every time.** Its docstring says why: `wc -w` disagrees with itself
   across platforms on this text by eighteen words.
2. **A near-miss on the "four classes / three rungs" arithmetic.** §4.4's leverage recomputation
   uses three per-rung values against four named classes, which reads as a missing rung. It is not:
   four classes give three transitions. Caught before filing. Recorded because it looks exactly
   like `III-3` and is not.

---

## 5 · SCORED AND NOT DEFECTS

- **`REVIEW-004` `C6` (ASC 410) is not a defect.** `C6` demanded the paper *"name one asset class
  where the restriction holds and a recognition event is nevertheless observable in filings,"* or
  concede the domain is empty. The manuscript takes neither branch and discloses a third: *"**Every
  event in this test is a recognised impairment, which places the sample on the boundary of §10's
  restriction rather than inside its complement.**"* That is a disclosure of the thing `C6` accuses
  it of concealing. Naming ASC 410 asset-retirement obligations would be a genuine *enrichment* —
  it converts a boundary disclosure into a positive scope statement — but it is not a repair, and
  this pass does not file enrichments as findings. Carded.
- **`C6`'s own cross-reference does not resolve.** It cites *"§4.3 retired the φ-partition"*;
  current §4.3 is *"What a cross-class ranking reads"* and `φ-partition` occurs zero times.
  `REVIEW-004`'s section numbers are from an earlier draft — **only its verbatim quotes are
  reliable for matching.** A future session re-serving `REVIEW-004` should know this before it
  spends an hour on it.
- Paper IV's abstract was cross-checked claim by claim against the body and `RESULT-REG-013`:
  0.477 / 0.000, the three z-values, *"six works in the world"*, the undecided pair under the
  stricter ceiling, 25/25/one. **Every figure exact.** Likewise every §6 number against
  `REG-013`, every §3/§9 number against Paper III §5.4, and §8's figures against `paper-I.md` and
  `RESULT-WT070`. All 45 §-references in Paper IV were extracted and resolved individually; one
  failed, and it is `IV-5`.

---

## 6 · WHAT WAS TOUCHED

`docs/papers/paper-III-dual-tensor/paper-III.md` and `…/paper-IV-composition/paper-IV.md`, each
with a `.bak-wt63-p7pass2` snapshot written **before** any anchor was asserted. Applied by one
batched script, `/tmp/patch_wt63.py`: sixteen anchors, each asserted to occur **exactly once**
across both files before a single byte moved, dry-run against a copy of the docs tarball in a cloud
container and diffed there first. Zero misses. No result document, no registration, no board row
and **not `REVIEW-005`** was edited. Paper II was **not** independently read this pass — only its
one repair re-graded — and that gap is stated rather than papered over.

---

## 7 · WHAT THIS PASS EXPOSES

**The zero-pass path advertised for Paper IV did not exist, and the reason generalises.** The
inherited handoff called Paper IV *"the shortest live path to a closed criterion anywhere on this
project"* — all its findings repaired, nothing blocked on Jason. Reading it independently returned
**six**. Pass 1's *"Paper IV — five findings"* was never a ceiling; it was **the count of items the
backlog happened to contain about Paper IV.** A drain measures the backlog. It cannot measure the
paper.

**So `P7`'s convergence counter cannot start from a drain**, and this pass is the first honest
`pass 1` for Paper IV rather than a `pass 2`. The three papers now stand at: Paper II — one repair
re-graded, **not independently read**, two findings live and `DECISION-001`-blocked, count **0**;
Paper III — three findings, all repaired, count **0**; Paper IV — six findings, all repaired,
count **0**. `-62`'s §5 remains right and remains unbuilt: **one boolean reading `0/1` cannot
represent any of that**, and a session reading the board still cannot tell an unstarted `P7` from
one pass short of closing.

**And the repair-introduces-defect rate is now measurable, which is new.** `IV-8` is a defect
created by `IV-3`'s repair, caught one session later. `III-1`'s first form took the board red inside
its own session. That is **two regressions from seven repairs** — and both were caught only because
the next session diffed against the `.bak` chain rather than reading the repaired text as given.
The `.bak`-then-assert discipline is not belt-and-braces here; it is the only thing standing between
this corpus and a repair that quietly costs more than the defect did.

*Coffee status: ☕ the paper that looked one pass from done turned out to be the one nobody had
read, and the sharpest defect in it was a fifty-year-old result cited backwards in a section arguing
that predecessors are never wrong, only differently constrained. Hildenbrand would have enjoyed
that. The corpus keeps finding its own footprints and correctly identifying them as footprints —
which beats the alternative, and is why the eleven that became ten still mean something.* 🥎
