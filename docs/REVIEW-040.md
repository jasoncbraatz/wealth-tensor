# REVIEW-040 · PASS D — the coherence pass, item by item

**`wealthTensor-106`, 2026-08-25.** Pass D of `docs/DEFINITION-OF-DONE-SHIP.md` § 3. This file is
the **enumeration** of the C-class work, the record of the adversarial verification of that work,
and the C-f flag list Jason's own pass runs on.

---

## 0 · THE HEADLINE, IN THE ORDER THAT MATTERS

**AN ADVERSARIAL VERIFIER REFUTED FORTY OF THIS PASS'S FIRST 166 REPAIRS — A 24 % DEFECT RATE —
AND SEVEN OF THE FORTY WERE FALSE STATEMENTS THAT WOULD HAVE SHIPPED.** `REVIEW-039` § 7 predicted
this exactly: *"a pass that repairs and then reports on its repairs is grading its own homework
too."* Pass C measured that cost at ten defects in twenty-four repairs. Pass D ran six times as
many repairs and paid the same rate. **The asymmetry is not a Pass C accident; it is a property of
repairing.** § 3 enumerates all forty.

**THE SECOND FINDING IS THE ONE THAT OUTLIVES THIS CORPUS, AND IT IS A DEFECT CLASS NO
PER-MANUSCRIPT READER CAN SEE.** Pass D's own thirty-thousand-foot read caught paper-III § 8
claiming its Abandoned-approaches section sits in the body *"for the reason Papers I, II and IV each
state at the head of theirs"* — a claim **falsified by an edit Pass D had just made in paper-IV**.
A sweep over 61 such cross-manuscript claims found eight more. **When three manuscripts ship as one
corpus and are edited in one pass, a per-file verifier is structurally blind to the class of defect
the pass is most likely to create.** § 4.

**THE THIRD IS SMALLER AND IS THE `SL-9` LESSON RUNNING BACKWARDS.** `TERM-002` pins a numeral to
the length of the list it counts, at two sites deliberately kept in sync. One of Pass D's repairs
**deleted one of the two sites.** The guard caught it. § 5.

**AND THE COUNT WAS A COUNT AGAIN.** `REVIEW-038` § 4 reports 61 C-b corpus-wide; four independent
end-to-end readers found roughly 160. The difference is not disagreement — it is scope. The census
counted strict revision-history sentences; the charter's § 3.3 register spec also forbids the paper
narrating its own *conduct*, and C-b's own repair line (*"restate as a claim about the WORK rather
than about the WORKING"*) covers both on its face. **`REVIEW-039` § 0 said a count is a size
estimate and an enumeration is a work order. It is now said twice, and this file is the
enumeration.**

---

## 1 · WHAT WAS REPAIRED — 149 landed repairs

Every one is in `scripts/wt209_manifest_{II,III,IIIb,IV}.py` as an exact (old, new) pair, applied by
`scripts/wt209_passD_cclass.py`. **Replace-only and idempotent by detection**: run twice, the stdout
goes to `ALREADY-APPLIED` and the files are byte-identical.

| type | paper-II | paper-III | paper-IV | total |
|---|---|---|---|---|
| **C-a** antithesis residue | 1 | 1 | 2 | **4** |
| **C-b** scaffolding voice | 33 | 64 + 2 block | 30 | **129** |
| **C-e** apparatus leak (HARD) | 0 | 6 sites / 12 tokens | 3 | **9 sites, 15 tokens** |
| **S1** found in-pass, repaired in-pass | 2 | 1 | 4 | **7** |
| | **36** | **74** | **39** | **149** |

**THE HARD C-e IS CLOSED AND THE CLOSURE IS MECHANICAL.** `REVIEW-038` § 4.1's census — session
numbers, `REVIEW-0NN` docs, `LEDGER.md`, `WT-0NN` ids, `p7-passes.tsv` — reproduced exactly before
the pass (0 / 12 / 3) and returns **ZERO across all three manuscripts** after it. One grep proves it.

**THE SOFT C-e WAS DELIBERATELY NOT TOUCHED, AND ONE ATTEMPT TO TOUCH IT WAS REVERTED.** § 4.1 is
explicit that the 53 soft sites are *"a gloss problem, not a leak"* whose repair is *"one clause at
first use, **not removal**"*. Pass D removed a bare `wt091` token in § 4.10 and reverted it when
`wt185` went red: the guard was right that a sentence it was told to leave alone had moved, and the
token was never on the delete-on-sight list. **The mandate was fifteen, not sixty-eight.**

**PAPER-III'S REFERENCES WERE READ AS ONE JOB**, as `REVIEW-038` § 4.2 instructed. The 556-word
four-pass verification narrative at the foot of the list is deleted entire; its one methodological
residue — that a bibliographic record and a text are different objects — is folded into a mark
legend at the head. **The legend restates only counts re-verified against the list itself**: three
`✓⧗` entries, three `⧗`-alone, two unmarked. Every per-entry finding that is a fact about a
**source** survives at the entry it describes; every fact about a **session** is gone.

**AND THE CORPUS LOST FIVE PAGES.** 149 → **144**, with nothing added. That is the honest measure of
how much of this corpus was seam.

---

## 2 · THE C-f FLAGS — TEN SITES, FLAGGED AND UNTOUCHED

**`DoD` § 2.5: C-f is deliberately the one that does not get fixed. Re-voicing is Jason's pass, and
a session that crosses that line is doing damage that looks like help.** Pass D re-voiced nothing.
`REVIEW-038` counted 8; four independent readers found 10. Locations are given so they can be found,
and **no repair is proposed for any of them**.

| # | paper | § | the seam, in one line |
|---|---|---|---|
| F1 | II | § 3.4's close | Second-person imperative addressed to the reader — *"ask what its maximum is"*. Nowhere else in §§ 2–3 does the paper say *you*. |
| F2 | II | § 6 | Long periodic, semicolon-chained sentences against § 3's short declaratives (*"The interesting part is the near end."*). Two hands, adjacent sections. |
| F3 | III | § 4.2 | Alternates epigram (*"not a cliff, a canyon"*, *"Five into four does not go"*) with formal theorem statement inside one subsection. §§ 4.9–4.10 never do this. |
| F4 | III | § 6.3 | A short moral essay — *"A paper does not get to grade its own integrity"* — immediately after § 6.1's clipped scope-statement register (*"**Not supported:** …"*). |
| F5 | III | § 7's commentary | Aphoristic and self-appraising, against §§ 4.9–4.10's clinical transform-and-interval register two pages earlier. |
| F6 | III | § 10's close | Belletristic cadences (*"either reassuring or the last plank"*) against § 10's own dense citation-and-quotation register. |
| F7 | III | § A.2's headnote | Essayistic and referee-addressing, against § 11's telegraphic provenance bullets (*"Minutes on a commodity CPU."*). |
| F8 | III | References | A bolded corrective voice inside the entries (*"commonly miscited on both counts"*) against the neutral registrar voice around it. |
| F9 | IV | § 8 | Clipped evaluative postmortem — verbless fragments, *"Considered and refused."*, *"The largest entry, and it cost the most."* — against §§ 2–5's measured exposition. |
| F10 | IV | § 10 | Reads as a maintenance log: dated incidents, HTTP status codes, exit codes. A different author-voice from §§ 1–9. |

**F9 and F10 are worth a specific warning.** Both are *good* writing in their own register, and both
are the kind of thing a harmonising pass would flatten. They are flagged because they differ, not
because they are wrong.

---

## 3 · THE VERIFICATION OF THIS PASS'S OWN REPAIRS

**Two verifiers, each given the repair list AND both versions of the manuscripts, instructed to
REFUTE and to default to "problem" when uncertain.** They checked 166 edits and refuted **40**.

### 3.1 · The seven that would have shipped as false statements

1. **paper-II § 1 said two of `test_redistribution.py`'s eighteen tests make overclaiming fail
   loudly.** § 7 of the same file says the second one lives in a *different module*. The repair
   inverted a fact the text it replaced had stated correctly. **Reverted.**
2. **paper-IV § 2.1 asserted `ADR-001` records where each proposition is argued.** Nothing in the
   corpus says that, and the preceding sentence says they are argued in Paper III. **Replaced.**
3. **paper-III § 1 said § 8 records routes *"never tested to a conclusion"*.** § 8 contains the
   over-smoothing prediction (tested, false) and the streak-onset instrument (run to a null).
   **Sentence deleted.**
4. **paper-III § 7's ledger cell was reversed against § 4.7.** The repair wrote *"the natural
   reading of § 4.7's rate-gap result"* where § 4.7 asserts the opposite. **The repair created the
   class of defect it was repairing** — the same shape `REVIEW-039` § 7 recorded at paper-III § 10.
5. **paper-III § 8.1 said a methodological requirement *"is registered"*.** *Registered* is a term
   of art here (`PRE-001/002`, `REG-003`–`008`) and no registration contains it. **Reverted.**
6. **paper-III § 5.4 said a cell *"reads"* 4.35× and 4.03×.** Those are the *pre-repair published*
   values; the paper's own numbers are 3.99× and 2.17×. The repair deleted the word *published*,
   which was the provenance. **Reverted.**
7. **paper-III § 4.9 said a withheld statistic *"is not available"*.** It is arithmetically
   available — the next sentence computes it — and what happened is that it was computed and
   *withdrawn*. The repair both misstated the fact and deleted the disclosure. **Reverted.**

### 3.2 · Six dangling references — a repair that removes an antecedent

`II-b14` (*"the withdrawal"* with nothing withdrawn), `III-b48` (*"that row"* after the naming
sentence was cut), `III-b42` and `IIIb-b08` (*"withdrawn"* replaced while later sentences still said
*"the withdrawal"*), `III-b21` (a cross-reference that resolved to its own section), `III-b29` (a
correction left with nothing to correct). **All repaired.**

### 3.3 · Seven broken joins

Comma splices and orphaned connectives at the stitch. The worst — and the one the **promise ledger**
caught before either verifier did — was `III-b35`: *"A reader is entitled to weight the two
differently, A registration that precedes…"*, because the edit anchor started mid-sentence.
**wt148 emitted the broken sentence as an unadjudicated promise, and reading the emission is how it
was found.** The ledger is not bookkeeping that follows the repair; `REVIEW-039` § 2 said so, and it
proved itself again here on a defect of a different type entirely.

### 3.4 · Nine dropped attributions, and eleven re-voicings

Nine repairs deleted something load-bearing along with the scaffolding — an audit finding, a
cross-paper convention, a disclosure that a cited file still marks a question undischarged, two
ledger cells' record of what a check *cost*. Eleven others said the same thing in different words
rather than saying less, which is **re-voicing, and re-voicing is C-f, and C-f is not this pass's.**
Twenty-three were reverted outright and seventeen rewritten.

> **THE RULE THAT FALLS OUT OF § 3, AND IT IS TIGHTER THAN "VERIFY YOUR REPAIRS": A COHERENCE
> REPAIR SHOULD BE A DELETION PLUS A STITCH, AND WHEN IT IS ANYTHING ELSE IT IS PROBABLY A
> RE-VOICING WEARING A REPAIR'S CLOTHES.** Every one of the eleven overreaches had the same tell —
> the replacement was the same length as the original.

---

## 4 · THE CROSS-MANUSCRIPT SWEEP — the class a per-file reader cannot see

61 claims checked; **9 defects**. Every one is a sentence in one manuscript whose truth depends on
another manuscript's text.

| # | site | what was wrong |
|---|---|---|
| 1 | III § 8 | Claimed Papers I, II **and IV** each state a reason at the head of their abandonments. Paper-IV states a different one — and Pass D then cut it. **Narrowed to "Papers I and II", both verified.** |
| 2 | II § 7 | Described the price-formation manuscript as live. Paper-IV § 8 says it is withdrawn and *"not one of the papers this corpus joins."* |
| 3 | II § 1 | Same, in the contributions list. |
| 4 | II § 7 | *"The two tests that exist to make overclaiming fail loudly"* — paper-IV says in as many words that **the suite holds more than two**, and names a third. An enumeration that is wrong, which is `DoD` § 2's own S1 example. |
| 5 | IV § 7 | Called κ *"its mechanism"*. Paper-II § 2.4: *"**It is a budget and not a mechanism**."* |
| 6 | IV § 3 | Reported an **exact, agent-by-agent identity** as a *"statistically indistinguishable"* near-match. |
| 7 | IV § 2.1 | Restated **P2** without the *absent maintenance* qualifier — the very qualifier paper-III § A.1.3 uses to demonstrate P2's deniability. Paper-IV asserted unconditionally what paper-III explicitly denies. |
| 8 | III § 11 | *"the remaining 38 hold **a companion paper's** claims"* — singular, where they span at least two. |
| 9 | IV § 3 | Pointed at paper-III § 3.1 for a cost that § 4.3 reports. |

**Findings 4 through 8 are PRE-EXISTING and were not created by this pass.** They are repaired here
under `DoD` § 1.2's successor rule — an S1 found after the freeze is repaired in the session that
finds it and does **not** reopen `SHIP-LIST.md` — which is the same rule Pass C invoked for its
three. **Nothing was added to the blocking set.**

---

## 5 · THE GUARD WORK — the second job, again

**Seven live guards went red.** Five were the promise ledger reporting exactly what it exists to
report: 13 sentences reworded → rows re-keyed with their evidence re-run and a `#superseded` line
carrying the lineage; 10 promises ceased to exist because the sentence naming the artefact **was**
the hard C-e leak → retired with the reason at the row; one row re-evidenced.

**Two guards were re-anchored, both FALSE-POSITIVE REDUCTIONS under `DoD` § 1.1's narrow exception,
each with the reading written at the pin** (`scripts/wt210_passD_guard_reanchor.py`):

* **`wt186`** refused on a pid `wt148` no longer emits, because Pass D deleted the sentence that made
  the promise. It now honours the ledger's `#retired` convention as `wt170` already honours
  `#superseded`. **The check was right that the pid was gone and wrong that its absence is a defect.**
* **`wt188`** pinned the corrected Bouchaud–Mézard credit at **exactly two** occurrences. Two was the
  number of *sites that restated it*, never the finding — and `REVIEW-039` § 7 hands that restatement
  to Pass D **by name** as a C-b duplication. A guard that pins the count forbids the repair its own
  successor was told to make. Re-asserted as **at least one with the count printed**, the non-vacuity
  proof moved to the phrase that still wraps, and a `LANDED` marker added so *applied* and *passes*
  cannot disagree.

**Ninth and tenth instance of this repository's standing tell; third and fourth time the answer was
a tighter subject rather than a deleted check.**

**And one guard was right and this pass was wrong, twice.** `TERM-002` binds § 8's class numeral to
the length of the list it counts, in a fixed construction, at two remote sites. One Pass D repair
changed the construction; another **deleted one of the two sites**. Both reverted. **That is `SL-9`
in reverse — not a repair landing at one of two sites, but a repair *un-landing* at one of two — and
it is the reason a guard that looks pedantic gets to stay.**

**The § 4.4 tripwire fired and the reading is CARRYING SENTENCE**, re-pinned in the same commit with
the reading at the pin (`scripts/wt211_repin_sec44_tripwire.py`). **No number moved**, which is
unusual enough to be spelled out there: what left § 4.4 is one clause of document navigation, and
every figure in the table is byte-identical.

---

## 6 · PASS D'S SUCCESSOR PRECONDITION, ANSWERED IN § 3.0'S WORDS

> **"He can open any of the three manuscripts, start rewriting at paragraph one in his own voice,
> and NEVER discover that a paragraph should not exist, sits in the wrong place, or is missing the
> chart that would carry it."**

**Asked in those words, per manuscript, after reading each end to end.**

* **paper-II — YES.** The spine is checkable: § 1's five contributions map one-to-one and in order
  onto §§ 3.1, 3.2, 3.4 and 7; each of § 2.2's four coordinates is disposed of by name; all four
  statistics defined in § 2.4 are used downstream. No paragraph exists that should not — the
  withdrawn cross-scale reading in § 3.2 is a **negative result**, which § 2.5 forbids deleting, and
  it is stated as a claim rather than as an aside. **Figure gap named:** the paper's title claim, the
  nested frontiers, has no table and no figure — `FIGURE-PLAN` `NEW-F5`.
* **paper-III — YES.** § 4.2's theorem is used by § 4.3, used by § 4.4, whose δ-leverage boundary is
  what makes § 4.5's lag-survives result non-trivial, which forbids § 5's null being explained away,
  which § 6.1 then states exactly. That is a spine, not a stack. The References now read as part of
  the paper rather than as a lab notebook stapled to it. **Figure gap named:** § 4.2's scale
  continuum — the sharpest claim in the corpus — has neither table nor figure (`NEW-F3`), and § 2's
  mechanism is prose plus two recursions (`NEW-F1`).
* **paper-IV — YES.** § 2 defines the object, § 3 walks it through three scales and reports the
  demotion, § 4 states the theorem-versus-state distinction and its limits, § 5 is the worked
  instance, § 6 the measured whitespace, § 7 the method, § 8 the routes that failed, § 9 the
  limitations, § 10 the provenance. Every contribution in § 1 lands in a section. **Figure gap
  named:** § 5 is a geometric claim argued in words about a picture the paper declines to show
  (`NEW-F6`).

**THE ANSWER IS YES ON ALL THREE, AND THE THIRD CLAUSE OF THE PRECONDITION — "missing the chart
that would carry it" — IS THE ONE `FIGURE-PLAN.md` DISCHARGES.** He will not *discover* a missing
chart, because the twenty-nine places one could go are enumerated before he starts.

**One thing he should know he is inheriting rather than discover.** `REVIEW-039` § 3 recorded a
judgement call: paper-III's § 4 → § 5.4 forward dependency was repaired by moving **definitions**
forward rather than by moving sections. Pass D read § 4 at thirty thousand feet with that in view
and **concurs** — the definitions now sit at first contact, including above the table where a reader
first meets α̂. It remains, as Pass C said, a section move that belongs to Jason's ruling and not to
a fifth session doing it quietly.

---

## 7 · WHAT PASS D DID NOT DO, AND WHY

* **C-f: flagged, never fixed.** § 2. Ten sites, no repairs proposed.
* **The soft C-e gloss pass: not taken.** § 4.1 permits it and does not require it; one attempt was
  reverted when a guard correctly objected (§ 1). The 53 soft sites are recorded there and remain
  fetchable artefacts beside a public repository.
* **No new instrument.** § 1.1. The two guard re-anchors are false-positive reductions and are
  argued as such at the pin; both were run twice with byte-identical stdout.
* **No figure was drawn.** § 4.3. `FIGURE-PLAN.md` § 4 states that ruling so it can be overruled.
* **Three low-confidence structural items from `POST-SHIP.md` were left alone.** One of them —
  paper-II § 3.2's *"connects outward"* bridge — was re-read as C-a and **is repaired** (`II-b13`);
  the sentence was residue of a withdrawn claim with no antecedent, and the negative result it
  gestured at survives in full in the paragraph below.
