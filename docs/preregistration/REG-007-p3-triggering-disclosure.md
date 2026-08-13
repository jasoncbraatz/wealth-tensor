# REG-007 · Theory + data registration · the triggering DISCLOSURE, and the mandated-disclosure window that makes it identified

- **Session:** `wealthTensor-19`, 2026-08-13.
- **Status at the time of writing:** committed and pushed **alone**, before a line of `wt093`
  exists, before any classifier is written, and before any statistic named below has a value.
- **Predecessor:** `REG-006` / `RESULT-REG-006`. That registration established the mechanism
  under test here and closed every cheaper route to it. Read it first.
- **Falsifier count:** eleven, of which four can kill the instrument outright.

---

## 0 · The question, and why it has to be the DISCLOSURE

§5.4 of Paper III reports that impairment charges of different asset classes co-occur inside a
firm-quarter far more often than an independence null allows — **4.01× in retail, 2.10× in
computer services** (`RESULT-REG-006` §2, corrected arm; read from that table, not recomputed).
Two explanations survive REG-006, and the charges themselves cannot separate them:

**(A) SEQUENCING / CO-TESTING.** `ASC 350-20-35-3C(f)` lists, among the events and circumstances
that make an interim goodwill test more likely than not to be required, "**the testing for
recoverability of a significant asset group within a reporting unit**." Testing one class
*mechanically summons* the test of the other. The co-occurrence is manufactured by the standard.

**(B) ECONOMIC CO-MOVEMENT.** The assets' values genuinely fall together, the firm tests both
because both are impaired, and the standard is merely present at the scene.

REG-006 established a third channel running the other way: `350-20-35-31`'s recognition ordering
makes the two charges **substitutes at the margin** (KPMG Handbook Example 4.4.10 — \$850 of prior
charges converts a would-be \$700 goodwill impairment to \$0, reproduced exactly by `wt092` F2).
So the observed complementarity is a **net** of a positive testing channel and a negative
recognition channel, and no arithmetic on the charges can decompose it. **The charge is the
outcome of both channels. The disclosure is the only place the firm says which one fired.**

### The discriminator, stated so it can fail

`ASC 350-20-35-3C` enumerates seven families of triggering event, (a) through (g). Six of them
are about the world: (a) macroeconomic conditions, (b) industry and market considerations,
(c) cost factors, (d) overall financial performance, (e) other entity-specific events
(management, key personnel, strategy, customers, bankruptcy, litigation), (g) a sustained
decrease in share price. **One of them is about the accounting**: (f) *events affecting a
reporting unit* — a change in the composition or carrying amount of its net assets, a
more-likely-than-not expectation of disposal, **the testing for recoverability of a significant
asset group within a reporting unit**, or recognition of a goodwill impairment loss in a
subsidiary's financial statements.

> **(A) predicts that firm-years carrying BOTH a goodwill charge and a non-goodwill charge cite
> an (f)-family trigger at a higher rate than firm-years carrying a goodwill charge alone.
> (B) predicts the two groups cite the same external (a)–(e),(g) triggers at the same rate,
> because on (B) the joint-ness comes from the shock and not from the rule.**

That is the whole registration. Everything below exists to make that comparison honest.

---

## 1 · THE SELECTION PROBLEM, AND THE WINDOW THAT SOLVES IT

**This is the part that took the session, and it is why the design has the shape it has.**

The obvious instrument — count 10-K/10-Q filings containing "triggering event" text — is
**conditioned on the outcome under study**, and the conditioning is written into US GAAP:

- **`ASC 350-20-50-2(a)` requires "a description of the facts and circumstances leading to the
  impairment" — and its trigger is "for each goodwill impairment loss recognized."**
- **When an interim test is run and NO loss is recognised, the Codification requires nothing.**
  There is no paragraph in `ASC 350-20-50` (50-1, 50-1A, 50-2, 50-3, 50-3A, 50-3B, 50-4, 50-5,
  50-6, 50-7 — the whole Section) that compels a registrant to disclose a triggering event as
  such. Disclosure in that case is MD&A-driven: Reg S-K Item 303, Release 33-8350 §V, and the
  Division of Corporation Finance *Financial Reporting Manual* §9510.1–9510.3, which asks
  registrants to discuss reporting units "at risk of failing step one." That is staff
  expectation and materiality judgement, not a bright-line requirement.

So a naive triggering-disclosure population is a population whose **inclusion probability depends
on whether a charge was taken** — the exact variable the design is trying to explain. Firms that
tested and passed are silently absent, and their absence is indistinguishable from their not
having tested. **That is `-16`'s underflowed tail, `-17`'s truncated tail, and `-18`'s dead
XBRL tag in a fifth costume: a guard that cannot tell EMPTY from ABSENT.** It is registered here
as the primary threat rather than discovered later as a finding.

**THE REGISTERED WINDOW.** The analysis is restricted to **firm-years in which a goodwill
impairment loss was recognised**. Inside that window `350-20-50-2(a)` compels the
facts-and-circumstances description **uniformly**, for every firm-year in the window, and —
critically — **the mandate does not depend on whether a non-goodwill charge also occurred.**
Both arms of the comparison are compelled to speak by the same sentence of the same standard.
The disclosure requirement is therefore orthogonal to the JOINT / GOODWILL-ONLY split that the
comparison is built on. That orthogonality is the identification, and it is the reason the
window is drawn where it is rather than at the larger and more tempting population.

The price of the window is stated once, here, and not re-litigated: **the design says nothing
about firms that tested without charging.** That is a scope limit, not a hedge.

---

## 2 · WHAT THE FEASIBILITY PROBES ESTABLISHED, BEFORE ANY STATISTIC EXISTED

Declared in full, because an undeclared feasibility probe is a researcher degree of freedom
wearing a lab coat. Everything in this section is a property of the *instrument* or the *size*
of a population. No quantity below is an input to any prediction in §4.

**2.1 · EDGAR full-text search evaluates phrase-AND WITHIN A FILE, not across a submission.**
Measured on CIK 0001725134 (Digital Media Solutions), `forms=10-K`, no date filter:
`"triggering event"` → 9 files; `"goodwill impairment"` → 8 files; the conjunction → **6 files,
and those 6 are exactly the set intersection of the two lists.** The three files that drop out
of the first list are `a45-seriesacertificateof.htm`, `a46-seriesbcertificateof.htm` and
`a1021-sharespurchaseagre.htm`; the one that drops out of the second is a 2021 accession. This is
checkable and F7 re-checks it at run time.

**2.2 · The single-phrase population is dominated by a different sense of the phrase, and the
conjunction eliminates it.** `"triggering event"` in 10-K submissions filed in calendar 2023
returns **1,235** files, and the top-ranked ones are almost entirely **exhibits** — Description
of Securities (EX-4), credit agreements (EX-10), certificates of designation (EX-3), clawback
policies (EX-97) — where "triggering event" means a change-of-control put, a preferred-stock
event, or a Rule 10D-1 recovery event. The conjunction with `"goodwill impairment"` returns
**764** files across **764 distinct accessions and 773 distinct CIKs**, and of those 764
filenames exactly **one** (`d410791dex13.htm`, an EX-13 annual report, which *is* the financial
statements) is a genuine exhibit. The other six that tripped a naive `ex\d` regex are tickers:
KEX, EEX, FLEX, NEX, OTEX, IEX. **The within-file conjunction removes the polysemy at the file
level completely.** It does **not** remove it within a single primary document — see F1.

**2.3 · No single phrasing is the population.** Same universe, 10-K, calendar 2023, conjoined
with `"goodwill impairment"` in every case:

| phrase | alone | ∧ "goodwill impairment" |
|---|---|---|
| `"triggering event"` | 1,235 | **764** |
| `"triggering events"` | 952 | **635** |
| `"impairment indicators"` | 1,070 | **707** |
| `"indicators of impairment"` | 1,390 | **865** |
| `"interim impairment test"` | 131 | **126** |
| `"goodwill impairment"` | 2,815 | — |

Four near-synonymous phrasings at the same order of magnitude and none dominant. **A
single-phrase instrument would see roughly half the disclosing population and would fail to
separate "disclosed no trigger" from "used different words."** Worse, phrasing is a firm-level
writing habit, plausibly set by filer size, auditor, or outside-counsel template — all of which
are correlated with the outcome. The registered instrument therefore takes the **union** of the
phrase set fixed in §3.2, and F2 audits every phrase's resolution against our own sample.

**2.4 · The registered sample's own population is large and no query is truncated.** The
`REG-006` committed panel (`data/reg-006-wt092-panel.json`, 1,602 firms — 584 pilot / retail,
1,018 replication / computer services) queried against EDGAR FTS in batches of 25 CIKs,
`forms=10-K`, 2013-01-01 → 2024-12-31, summing over batches:

| query | filings |
|---|---|
| `"triggering event" ∧ "goodwill impairment"` | **1,063** |
| `"triggering events" ∧ "goodwill impairment"` | 906 |
| `"impairment indicators" ∧ "goodwill impairment"` | 930 |
| `"indicators of impairment" ∧ "goodwill impairment"` | 1,469 |
| `"goodwill impairment"` | **5,333** |

**Zero batches reached the 10,000-hit cap.** This is the Q2 answer with a number attached, and it
is the reason the design is not built on the `N_co` cells: those are **41 firm-quarters in retail
and 53 in computer services**, a set over which a share has granularity 1/41 = 2.4% and over
which ladders A, A3 and R already demonstrated what under-powering costs.

**2.5 · Deduplication is required and its magnitude is known.** Of the 773 CIKs in the 2023
conjunction set, **14 (1.8%) have more than one 10-K accession in the same calendar year** —
fiscal-year straddles and 10-K/A amendments. F4 is the guard.

---

## 3 · The registered quantities

### 3.1 · The frame

The unit is the **firm-fiscal-year**. The frame is `data/reg-006-wt092-panel.json`, **unmodified
and re-read, not rebuilt** — it carries `cik`, `sic`, `universe`, and per-`fy_end` rows with the
tier charges `t0`, `t1`, `t2`, `G`, `G_present`, and `A`. Rebuilding it from `edgar.py` is
forbidden by this registration: `-18` lost three runs to reconstructing registered machinery from
its signature instead of copying its call site, and this is the same trap with a JSON file in it.

**The window (§1):** firm-years with `G > 0`.

**The split, inside the window:**
- **JOINT** — `G > 0` and at least one of `t0`, `t1`, `t2` is `> 0` in the same fiscal year.
- **GOODWILL-ONLY** — `G > 0` and `t0 = t1 = t2 = 0`.

### 3.2 · The instrument

For each firm-year in the window, locate the 10-K covering that fiscal year and retrieve the
primary document. A firm-year is **DISCLOSURE-BEARING** if the primary document contains at
least one phrase from the registered set, fixed here and not extended after the run:

```
"triggering event"   "triggering events"   "impairment indicator"   "impairment indicators"
"indicators of impairment"   "indicator of impairment"   "interim impairment test"
"interim goodwill impairment"   "events or circumstances"
```

Around each occurrence, take a **fixed window of 1,500 characters, 750 either side**, clipped at
document boundaries. The window is fixed here, in advance, and F3 is the sensitivity check that
makes the choice falsifiable rather than fitted.

### 3.3 · The classification

Each window is classified against two keyword families derived from `350-20-35-3C`. The families
are fixed here:

- **INTERNAL — the (f) family.** "recoverability of a significant asset group", "asset group",
  "carrying amount of its net assets", "composition ... of its net assets", "long-lived asset
  impairment", "tested ... for recoverability", "recognition of a goodwill impairment loss in
  the financial statements of a subsidiary", "held for sale", "disposal group".
- **EXTERNAL — the (a)–(e),(g) families.** "macroeconomic", "economic conditions", "industry",
  "market conditions", "competitive", "regulatory", "raw material", "labor costs", "declining
  cash flows", "decline in ... revenue", "decline in ... earnings", "loss of a ... customer",
  "management", "key personnel", "litigation", "bankruptcy", "share price", "stock price",
  "market capitalization", "interest rate", "discount rate".

Each firm-year lands in exactly one of **four** cells: `INTERNAL-ONLY`, `EXTERNAL-ONLY`, `BOTH`,
`NEITHER`. **`BOTH` and `NEITHER` are reported as their own rows and are never allocated,
imputed, or dropped.** A share is always reported with its denominator printed beside it.

### 3.4 · The registered statistic

**Λ = P(INTERNAL-ONLY ∪ BOTH | JOINT) − P(INTERNAL-ONLY ∪ BOTH | GOODWILL-ONLY)** — the
difference in the rate at which an (f)-family trigger is named, between joint-charge and
goodwill-only firm-years, inside the mandated-disclosure window. Reported with an exact
Fisher two-sided p-value on the 2 × 2 of {JOINT, GOODWILL-ONLY} × {names (f), does not name (f)},
`BOTH` folded into "names (f)" and `NEITHER` excluded from the test but printed. A second,
pre-registered variant folds `BOTH` the other way; **both variants are reported whatever they
show**, because choosing between them after the run is the researcher degree of freedom this
sentence exists to close.

---

## 4 · THE SEVEN REGISTRATION QUESTIONS, EACH ANSWERED IN ONE SENTENCE, BEFORE ANY DATA

**Q1 · WHICH OUTCOMES DOES THIS THRESHOLD FAIL TO SEPARATE?** (`-14`)
A 1,500-character window around "triggering event" in a 200-page 10-K cannot separate an
impairment triggering event from a change-of-control triggering event in the debt note when both
happen to sit near a mention of goodwill — §2.2 shows the within-file conjunction kills this at
the *file* level and F1 measures what survives at the *passage* level.

**Q2 · IS THE SET I AM TAKING A SHARE OF GUARANTEED NON-EMPTY?** (`-14`)
Yes and it is measured, not assumed: **5,333 filings** in the registered sample mention goodwill
impairment and **1,063** carry the primary phrase alongside it (§2.4) — and the design is
deliberately *not* built on the `N_co` cells of 41 and 53, whose granularity is coarser than the
effect anyone should expect.

**Q3 · WHICH VALUES CAN THIS INSTRUMENT NOT PRODUCE, AND DOES MY ESTIMATOR ASSIGN THEM MASS?**
(`-15`)
It cannot produce any value for a firm-year whose 10-K is unretrievable or whose window is
`NEITHER`, and the estimator therefore **assigns those zero mass by exclusion and prints them as
their own row** rather than imputing them into either arm — a `NEITHER` share above 20% voids the
comparison outright (F5).

**Q4 · CAN THIS GUARD TELL AN EXHAUSTED TAIL FROM AN UNDERFLOWED ONE?** (`-16`)
EDGAR FTS silently truncates at 10,000 hits, so every query is issued in CIK batches whose
individual counts are recorded, and **the run aborts if any single batch returns ≥ 10,000** —
§2.4 confirms zero batches are near the cap today, and F6 re-asserts it at run time rather than
trusting this paragraph.

**Q5 · IS THIS CONSTANT READ FROM THE TABLE THAT PUBLISHED IT, OR RECOMPUTED FROM ITS INPUTS?**
(`-17`)
The 4.01× and 2.10× comparison figures are read from `RESULT-REG-006` §2's committed table; the
`350-20-35-3C` sub-item text is read from the standard and not reconstructed from memory; and
**one constant is knowingly unverified and flagged** — the *Financial Reporting Manual* §9510.2
cites S-K **303(a)(3)(ii)**, which is pre-Release-33-10890 numbering, and F11 verifies the
current citation against the CFR before any of it is printed.

**Q6 · DOES EVERY IDENTIFIER I NAME ACTUALLY RESOLVE TO SOMETHING IN MY OWN SAMPLE?** (`-18`)
No identifier is trusted: **F2 runs every one of the nine registered phrases and every keyword in
both classification families against our own 1,602 firms and writes the hit counts to a committed
audit file**, exactly as `tests/test_tag_resolution.py` now does for `TIER_TAGS` — a phrase
matching nothing in our sample is recorded as DEAD, loudly, and cannot quietly contribute zero.

**Q7 · DOES EVERY FALSIFIER AGREE WITH THIS REGISTRATION'S OWN HEDGES?** (`-18`)
Checked before running: no falsifier below demands a magnitude this document has hedged, and in
particular **F8 asserts only a SIGN and a nonzero count, never a level** — because §5 concedes in
advance that the disclosed trigger is a lower bound on the true one.

---

## 5 · The registered predictions

**P1 · Sequencing.** Λ > 0. Joint-charge firm-years name an (f)-family trigger more often.

**P2 · Co-movement.** Λ ≈ 0, and the external-family *composition* is statistically
indistinguishable between the two arms.

**P3 · The asymmetry that makes P1 conservative and P2 uninformative — registered in advance.**
`350-20-50-2(a)` mandates *a* description of the facts and circumstances; it does not mandate
that the description name the proximate trigger, and a firm may satisfy it entirely with an
external narrative ("a decline in the reporting unit's projected cash flows") while the actual
proximate cause was the asset-group test. **The omission runs one way**: an internal,
accounting-generated trigger is the less newsworthy and more embarrassing of the two, and is the
one more likely to go unsaid. Therefore **Λ > 0 is evidence for sequencing at a strength the
measured magnitude understates, and Λ ≈ 0 is NOT evidence for co-movement.** This is stated
before the run so that a null cannot later be sold as a finding — the mistake ladders A, A3 and
R made available to `-18` and which `REG-006` §4 A2 had, to its credit, already forbidden.

**P4 · The magnitude is not predicted.** No threshold on Λ is registered, because no source
supports one and inventing one would be a free parameter. The registered claim is a **sign and a
significance level**, nothing more.

---

## 6 · What this registration explicitly does NOT do

- It does **not** touch `TIER_TAGS`, `edgar.py`, or any PRE-001 constant. `wt093` is additive.
- It does **not** revisit ladders A, A3 or R, or read their failure as evidence about the world.
- It does **not** use 8-K Item 2.06. That population is dead — roughly 100 filings a year against
  ~1,400 firms recording an impairment — because the Instruction to Item 2.06 exempts a
  conclusion reached in connection with the next periodic report and **Exchange Act Form 8-K
  C&DI Question 110.01 [May 16, 2013]** reaches conclusions that merely *coincide* with the
  preparation, review or audit of the financial statements for that report. This is recorded so
  that a future session does not rediscover it. (The word "extended" is ours; the staff
  characterises 110.01 as an interpretation of the existing Instruction.)
- It does **not** proxy σ or asset lifetime. Neither is in this sample and a quantity that shares
  σ's name without its meaning is the WT-038 error, which has now been paid for three times.
- It does **not** claim novelty. §7 commits to the check instead.
- It does **not** extend the phrase set or the keyword families after the run. Both are frozen
  above. An extension is a new registration.

---

## 7 · The manuscript repairs this registration commits to, whatever Λ returns

Committed now, so that the writing is not contingent on the result:

1. **§5.4 and Limitation 9 gain the selection statement of §1** — that triggering-event
   disclosure is compelled by `350-20-50-2(a)` only when a loss is recognised, and is otherwise
   MD&A-driven — replacing, not supplementing, whatever weaker sentence currently stands there.
   Under the charter's non-increasing-hedge invariant, this is a **replacement**.
2. **The prior-art claim gets its check before it gets its sentence.** Reconnaissance this
   session read the complete published text of **Amel-Zadeh, Glaum & Sellhorn (2023), *European
   Accounting Review* 32(2): 415–446** and found `ASC 350-20` appears **zero** times, `ordering`
   **zero** times, and the only ordering reference in the paper is a one-line descriptive mention
   of **IAS 36 ¶104** — which is a *loss-allocation waterfall* running in the **opposite
   direction** from `350-20-35-31`'s *test-ordering* rule and must never be cited for it. The
   IASB's own 58-page *Goodwill and impairment: academic evidence* compilation likewise contains
   no ordering, no `350-20`, and no triggering-event material. **The gap appears real. It is
   recorded as "not found by keyword search", not as "does not exist"**, because Google Scholar
   and SSRN search were both inaccessible to that pass and a badly-titled working paper would be
   invisible to it. The unread leads are named in the handoff so the next session starts above
   zero: Cready et al. (2012) and Hirschey & Richardson (2002) on restructuring charges
   accompanying impairments, which AZG&S cite as the co-occurrence confound and which are the
   nearest thing in that literature to this question.
3. **Two corrections land regardless of Λ**, both found while registering: the "not all-inclusive"
   language is `350-20-35-3F`, **not** `35-3C`; and `350-20-35-31` is a **four-sentence
   paragraph** whose "(thus potentially requiring a goodwill impairment test)" parenthetical sits
   in its second sentence — quoting it as one sentence truncates it. Any place the manuscript
   cites either, it gets the corrected form.
4. **`RESULT-REG-007` reports Λ once, with its denominators, and reports `BOTH` and `NEITHER`
   beside it.** If the window is too thin to support the comparison, the counts are published and
   the ratio is withheld — the REG-004/REG-005 precedent, and the withholding is deliberate and
   in advance.

---

## 8 · Falsifiers

Each runs **before** Λ is computed. Each carries a `severity.check` witness: a zero-argument
callable returning **the same predicate evaluated on a world where the claim is false**, which
must come back **falsy**, and whose falsifying world must be **runnable** — the two failure modes
`-18` paid for.

**F1 · PASSAGE-LEVEL POLYSEMY.** Sample 60 windows at random from documents in the window and
hand-audit the fraction in which "triggering event" refers to something other than impairment.
**If that fraction exceeds 15%, the 1,500-character window is refuted and the instrument is
narrowed to sentence-level co-occurrence before anything else runs.** *Kills the instrument.*

**F2 · PHRASE AND KEYWORD RESOLUTION.** Every registered phrase and every classification keyword
is run against our own 1,602 firms; counts are written to `data/reg-007-phrase-audit.json` and
pinned by a test. **Any phrase or keyword with zero hits in our own sample is reported as DEAD in
`RESULT-REG-007`, by name.** *Kills nothing; makes EMPTY distinguishable from ABSENT.*

**F3 · WINDOW SENSITIVITY.** Recompute the classification at 750, 1,500 and 3,000 characters.
**If the sign of Λ flips across those three, Λ is a property of the window and not of the
filings, and it is withheld.** *Kills the result.*

**F4 · DEDUPLICATION.** Assert that after deduplication on `(cik, fiscal_year)` no key carries
two conflicting classifications; **if any does, abort and print them** rather than picking the
later filing. §2.5 says to expect roughly 1.8% multi-accession firm-years. *Kills the run.*

**F5 · THE `NEITHER` CEILING.** **If more than 20% of window firm-years classify as `NEITHER`,
the keyword families are refuted as a partition of the (a)–(g) space and Λ is withheld** — the
families are not widened to make this pass, because widening a threshold to rescue a falsifier is
precisely what `REG-006` F4b caught. *Kills the result.*

**F6 · THE FTS CAP.** Assert every batch count `< 10,000`. *Kills the run.*

**F7 · WITHIN-FILE CONJUNCTION.** Re-run §2.1's Digital Media Solutions probe and assert the
conjunction is exactly the set intersection. **If EDGAR has changed its matching semantics, every
population count in §2 is wrong and the registration is re-derived before use.** *Kills the run.*

**F8 · THE CONTROL ARM, IN THE SAME PASS.** Λ is computed for the pilot and replication universes
**in one crawl**, and the whole classification is additionally run over a **placebo window** —
firm-years with `t0 + t1 + t2 > 0` and `G = 0`, where `350-20-50-2(a)` does *not* apply and the
(f)-family rate should therefore be *lower* in both arms. **Two separate runs prove nothing**;
this is `-18`'s ladder-C lesson, promoted to a falsifier. *Kills the interpretation.*

**F9 · THE ORDERING RULE'S OWN TEXT.** Assert that the phrase "the testing for recoverability of
a significant asset group within a reporting unit" appears in sub-item **(f)** of
`350-20-35-3C` and nowhere else in the enumeration. Verified this session against three
independent reproductions (EY FRD BB1499 §3.1.1, Grant Thornton *Viewpoint 2023* p. 39, Deloitte
DART §2.3.1) and two SEC comment-letter responses that recite the standard letter-by-letter
(NetSol 2014-08-20, KEYW 2016-01-04). **FASB's own server returned 403 to every attempt; this is
recorded, not papered over.** *Kills the discriminator.*

**F10 · THE MANDATE'S SCOPE.** Assert that `ASC 350-20-50-2`'s trigger is "for each goodwill
impairment loss recognized" and that no paragraph in `350-20-50` compels triggering-event
disclosure absent a recognised loss. **If this is wrong, §1's identification collapses and the
window is the wrong window.** *Kills the design.*

**F11 · THE S-K CITATION.** The *Financial Reporting Manual* §9510.2 cites S-K
**303(a)(3)(ii)**; Release 33-10890 (Nov 2020) restructured Item 303. **Verify the current
subsection against the CFR before printing any S-K citation.** Knowingly unverified as of this
commit. *Kills a footnote, and footnotes are where citations go to die.*

---

## 9 · Stopping rule

The instruments are written after this file is committed and pushed **alone**. `wt093_harvest.py`
retrieves and computes nothing; `wt093_triggering_disclosure.py` runs F1–F11 and then Λ, in that
order, aborting on any falsifier marked *kills the run*. `RESULT-REG-007` is written from the
output and reports every falsifier's verdict including the ones that passed. If Λ is withheld
under F3 or F5, the counts are published anyway and the withholding is named as such.

**If the window turns out to contain fewer than 30 firm-years in either arm, the comparison is
abandoned and the section is written as a measured population report with the ordering-rule
corrections of §7.3 — which land regardless.** Declared now, so that a thin cell is a result and
not a temptation.
