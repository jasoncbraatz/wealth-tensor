# SHIP-LIST — the blocking set, CLOSED AND FROZEN

**Emitted by `wealthTensor-103` (Pass A), 2026-08-24, per `docs/DEFINITION-OF-DONE-SHIP.md` § 3.**
**STATUS: CLOSED.** Per DoD § 1.2 the blocking set is exactly what this file contains. Anything
discovered from here on goes to `docs/POST-SHIP.md` — not to this list, not to a `p7-passes.tsv`
row, not to an at-bat. **A session that grows this list has broken the definition of done.**

**The single exception, and it is the DoD's own (§ 3, Pass B):** if a repair reveals an adjacent S1
*at the site being repaired*, Pass B repairs and appends it, logged with the repair that surfaced
it. That is the only permitted growth, and it is not a licence to look.

**Nine entries. Six S1, three S2. Zero carried S3** — every S3 is in `POST-SHIP.md`.

---

## ✅ CLOSED AT `wealthTensor-104` (PASS B), 2026-08-24 — ALL NINE REPAIRED IN `1e1e2a5`

**Every entry below carries a `REPAIRED` line naming what landed.** The list did not grow: the
one permitted growth (DoD § 3, Pass B) was not needed — no repair revealed an adjacent S1 at its
own site. Two things Pass B found that are NOT on this list and are in `POST-SHIP.md` instead,
which is § 1.2 working rather than failing:

- `wc -w` on **macOS returns 7 527 in every locale**, so `SL-6`'s defect is invisible on darwin
  and reproduces only under GNU `coreutils`. The repair names the locale for that reason.
- `paper-I` is outside `#scope` in `docs/promises-adjudicated.tsv`, so its 13 promises are
  unadjudicated by design. Untouched here; widening scope is a decision, not a repair.

**Guards these repairs reddened, all closed in this same session:** `TERM-001` (wording),
`REG-003 §7` (the peak-to-charge qualifier), `test_restatement_reach` (§ 4.9 DECLARED for α̂ —
a tighter pin, not a weaker one), and `wt148`'s promise sweep (10 rows adjudicated `H` with
their evidence re-run here, 2 superseded rows dropped with lineage markers).

**`defensive_count.py --against 7c5b6fb` reads +0 on all three manuscripts.**

---

**LINE NUMBERS BELOW ARE AS OF `7b5e114`**, the commit this pass read, with manuscript digests
`paper-II 2bf75ee73f092e2e115cf731796444b5` · `paper-III 0f6dd399d031ab6bafaffae813da1407` ·
`paper-IV f9474da72f15555ea7d1aad0f58c21b4`. **Pass B's own repairs will move them**, so every entry
also quotes the text it names — **find the entry by its quoted text, not by its line number.**

The evidence for every entry is `docs/REVIEW-038-passA-retrospective-scoring.md`. **Each entry below
names its repair specifically enough to execute without re-deriving the finding** — that is Pass A's
successor precondition (DoD § 3.0) and it is the bar this file was written to meet.

---

## S1 · BLOCKING — the manuscript states something that is not true

### `SL-1` · paper-III § 4.9 — `0.333` attributed to § 5.4, whose measured rate is `0.408`

**Site:** `docs/papers/paper-III-dual-tensor/paper-III.md` line 982.
**Text:** *"…outside the rectangle whose fastest rate is 0.333, **which is §5.4's measured rate**
arriving from the other direction."*
**Why it is false:** § 5.4 (lines 1340–1449) states the measured recognition rate as
**`0.408` per year, 95 % interval [0.383, 0.432]** (line 1363). `0.333` does not occur anywhere in
§ 5.4; it is the *rectangle's* own fastest disclosed rate, as line 593 says in those words.
**Source:** `wt184` Rule 1 flag, adjudicated TRUE — one of two of forty-four.
**THE REPAIR:** re-point the relative clause so `0.333` is not its referent. The paper's own
sentence at line 593 already has the correct phrasing to borrow: *"the rectangle's own fastest
disclosed rate of 0.3333."* State § 5.4's rate as `0.408` explicitly if the comparison is wanted.
**Not a number change — an attribution change. The arithmetic in the sentence is correct.**


**REPAIRED** `1e1e2a5` · `scripts/wt193_sl1_sl2_attribution.py`. The relative clause no longer points at
`0.333`: the sentence now reads *"outside the rectangle, whose own fastest disclosed rate is 0.333 —
and above §5.4's measured peak-to-charge recognition rate of 0.408 per year as well."* The
comparison Pass A said was wanted is kept and made true; **the arithmetic was not touched.** The
qualifier is not decoration — `REG-003 §7` forbids attaching a measurement of α̂ to an unqualified
*recognition rate*, and its guard caught the first draft of this repair doing exactly that.

### `SL-2` · paper-III § 4.9 — `§4.4's 0.00789`, a value § 4.4 does not contain

**Site:** `docs/papers/paper-III-dual-tensor/paper-III.md` line 1000.
**Text:** *"The *level* moves it by 4.3 %, from **§4.4's 0.00789** at the calibration to 0.00755 at
the measured rate…"*
**Why it is false:** `0.00789` occurs **exactly once in all 2 750 lines** — in this sentence.
§ 4.4 runs lines 466–611 and does not carry it. The possessive asserts § 4.4 states a number no
section states.
**Source:** `wt184` Rule 1 flag, adjudicated TRUE — the second of two.
**THE REPAIR:** drop the possessive — *"from 0.00789 at the calibration"* — and, if the provenance
is wanted, say it is this section's own evaluation of § 4.4's closed form `δ₃* = Kα/(1 + K)`, which
§ 4.4 *does* state and which the same paragraph already cites. **Alternative, more expensive:** add
the calibration value to § 4.4's tier table so the pointer becomes true.
**Arithmetic checked and correct:** (0.00789 − 0.00755)/0.00789 = 4.31 %, the 4.3 % stated.
**This is `III-5`'s shape (`-101`) recurring in a second site. Both live sites are in § 4.9.**


**REPAIRED** `1e1e2a5` · same script. The possessive is gone: *"from 0.00789 at the calibration —
§4.4's closed form evaluated there — to 0.00755 at the measured rate"*. `wt090` prints
`reproduces §4.4's published 0.00789 at alpha=0.05`, so the new attribution is the true one.

### `SL-3` · paper-II front matter — a version stamp and a revision note that 21 commits have overtaken

**Site:** `docs/papers/paper-II-redistribution/paper-II.md` lines 7 and 14–18.
**Text:** *"Version 0.2, 2026-08-11."* and *"**v0.2** the house-style pass … **No result, number,
claim or citation changed.**"*
**Why it is false:** `git log --since=2026-08-11 -- <the file>` returns **21 commits**, last touched
**2026-08-24**. Those commits include `II-42` (a sentence CUT for being false), `II-44` (a citation
claim about Bouchaud & Mézard rewritten at three sites) and `II-35` (three reported percentages
corrected). Results, numbers, claims and citations all changed. The document asserts it is the
2026-08-11 v0.2 and it is not.
**Source:** `II-25`, carded at `-74`, **open for twenty-eight sessions.**
**THE REPAIR:** bump to the next version with today's date and add one revision-history line naming
what the P7 passes changed at the class level (*"v0.3 — sixteen independent review passes; see
§ Limitations and the ship statement"*). **Do not enumerate seventy findings in the manuscript** —
that is conduct-narration and charter § 3.3 forbids it.
**Checkable after repair:** `git log --since=<the new stamped date>` returns 0 commits before the
repair commit itself.


**REPAIRED** `1e1e2a5` · `scripts/wt194_version_stamps.py`. **Version 0.3, 2026-08-24**, and one
class-level line appended to the existing revision history. No ruling from Jason had landed, so the
bump was made rather than waited for. `git log --since=2026-08-24 -- <the file>` returned 0 commits
before the repair commit itself.

### `SL-4` · paper-III front matter — same defect, 36 commits

**Site:** `docs/papers/paper-III-dual-tensor/paper-III.md` line 7. **Text:** *"Version 0.5,
2026-08-12."*
**Measured:** **36 commits** since that date; last touched 2026-08-21.
**THE REPAIR:** as `SL-3`.


**REPAIRED** `1e1e2a5` · same script. **Version 0.6, 2026-08-24**, plus a *Revision note* (this
paper carried no revision history at all). Same class-level wording as `SL-3`.

### `SL-5` · paper-IV front matter — same defect, 19 commits

**Site:** `docs/papers/paper-IV-composition/paper-IV.md` line 7. **Text:** *"Version 0.1,
2026-08-16."*
**Measured:** **19 commits** since that date; last touched 2026-08-21.
**Source:** named at `-100` in `REVIEW-035`'s not-checked list as *"Jason's to fix."* It is a false
statement in a manuscript, so it is an S1 and it is on this list. **If Jason wants to own the
version numbering himself, that is the written ruling that closes `SL-3`, `SL-4` and `SL-5`
together** — DoD § 2 allows an S1 to close by ruling as well as by repair.
**THE REPAIR:** as `SL-3`.


**REPAIRED** `1e1e2a5` · same script. **Version 0.2, 2026-08-24**, plus a *Revision note*.

### `SL-6` · paper-IV § 8 — a word count that is 7 367 or 7 527 depending on the locale, declared checkable

**Site:** `docs/papers/paper-IV-composition/paper-IV.md` line 521.
**Text:** *"A complete draft existed — **roughly 7,500 words**, references verified — … the draft
itself is in the repository … **which is the only place the word count above is checkable.**"*
**Why it is false:** on byte-identical content (`md5 eb56ef67162df6db0fabf50819db78f0`):

| how it is counted | result |
|---|---|
| `LC_ALL=C wc -w` (and any non-UTF-8 locale) | **7 367** |
| `LC_ALL=C.UTF-8 wc -w`, macOS default `wc -w`, Python `str.split()` | **7 527** |

A 160-word spread. The paper invites the check and names **no command and no locale**, so one
legitimate reader gets 7 367 — for which *"roughly 7,500"* reads as wrong and the previous wording
*"roughly 7,400"* was right. Two readers disagree, so **DoD § 2.4 resolves it upward to S1.**
**Source:** found while verifying that `IV-12`'s repair (`-100`, which moved 7,400 → 7,500) had
held. It had not held for every reader.
**THE REPAIR:** name the command *and* its locale in § 10 beside the other regeneration bullets —
`LC_ALL=C.UTF-8 wc -w docs/papers/paper-I-price-formation/paper-I.md` → 7 527 — and keep *"roughly
7,500."* **Do not restate the number without naming how it is counted; that is the defect.**


**REPAIRED** `1e1e2a5` · `scripts/wt195_wordcount_locale.py`. § 10 gains a **Regenerate §8's word
count** bullet naming the command *and* the locale —
`LC_ALL=C.UTF-8 wc -w docs/papers/paper-I-price-formation/paper-I.md` → **7,527** — and states that
the same bytes return **7,367** under GNU `wc` in a non-UTF-8 locale. § 8 now points at § 10 instead
of claiming the draft file is the only place the count is checkable. *"roughly 7,500"* is unchanged,
as Pass A required. **Note for anyone re-checking on darwin: macOS `wc` returns 7 527 in every
locale. The 7 367 reproduces under GNU `coreutils`.**

---

## S2 · BLOCKING — the manuscript asserts something nothing supports

### `SL-7` · paper-III § 11 — a scope sentence narrower than the promise the front matter makes

**Sites:** `paper-III.md` line 11 (front matter) and line 1970 (§ 11's scope sentence).
**Front matter:** *"**every** computational result is produced by committed code in the repository
named in § 11."*
**§ 11 itself:** *"Every simulation result in **§A.2 and §§2–3** is produced by open code."*
**Why nothing supports the wider claim:** § 11 carries Regenerate bullets for § 3/§ A.2.4, § A.2.3,
§ 4.10, § 5 and § 5.4. **§§ 4.1–4.9 have none** — and that is where § 4.4's tier table, § 4.5's
ladder table, the 66.2 % robustness figure and § 4.9's crossing figures live. This is the rubric's
own § 2 example: *"a claim of scope … that is narrower than what the paper reports."*
**The code exists** — `scripts/wt083_tier_ladder_antialignment.py`,
`scripts/wt088_disclosed_ladder.py`, `scripts/wt092_ladderC.py`, `scripts/reg009_ladder_inputs.py`
are committed. **It is the signposting that is missing, not the artefact.** That is what makes this
S2 rather than S1.
**Source:** `III-8`, carded at `-73`, **open for thirty sessions** — the oldest item on this list.
**THE REPAIR:** widen § 11's scope sentence to name § 4 and add a **Regenerate § 4** bullet naming
which script prints which table. Where no single command reproduces a figure, **copy § 11's own
existing honest pattern** — the § 5.3 bullet already says *"Nothing in this repository re-derives
§ 5.3's figures from committed data"* — rather than inventing a new disclosure form.


**REPAIRED** `1e1e2a5` · `scripts/wt197_paperIII_sec4_provenance.py`. § 11's scope sentence now reads
*"Every simulation result in §A.2, §§2–3 and §4 is produced by open code, and the bullets below name
the command that prints it. Where a figure is printed by no command here, the bullet says so."*
Four **Regenerate** bullets follow, covering §§ 4.2, 4.4, 4.5, 4.6, 4.7, 4.8 and 4.9 — `wt084`,
`wt083`, `wt088`, `wt085`, `wt086`, `wt087` and `wt090`. **Every figure quoted in them was re-run
before it was written down**, and all seven are adjudicated `H` in `docs/promises-adjudicated.tsv`.
One figure has no command and the bullet says so rather than implying one: **§ 4.2's 31.7%** is
`wt084`'s printed family restricted to a ten-per-cent opening gap, and the restriction is applied in
the prose. That is § 11's own § 5.3 form, copied rather than reinvented.

### `SL-8` · paper-II — nine of sixteen reference entries are never cited in the body

**Site:** `docs/papers/paper-II-redistribution/paper-II.md`, References.
**Measured this session by `wt133_crossref_sweep.py` sweep 2:** paper-II **16 entries, 7 cited,
9 not** — Drăgulescu, Patriarca, Yakovenko, Gabaix, Piketty, Auerbach, Kaldor, Saez, Toder.
**For contrast, and it is the reason this is a paper-II defect and not a corpus one:** paper-III is
**49 of 49** cited and paper-IV is **28 of 28**.
**Why nothing supports it:** § 1 and § 6 lean on both the kinetic-exchange literature and the tax
literature and credit neither at the sentence that relies on it. This is `IV-7`'s shape exactly
(Mas-Colell, Robinson, Sraffa on paper-IV), which scored S2 and was repaired at `-81`.
**Source:** tee-up 4, card `1217568192511533`, **seventh pass carrying it.**
**THE REPAIR: `IV-7`'s, already landed once in this corpus — read it first and copy it.** For each
of the nine: cite it at the sentence that relies on it, **or cut the entry.** Both are permitted;
padding the body to justify an entry is not.
**Checkable after repair:** `wt133_crossref_sweep.py` reports paper-II `n of n cited, 0 not`.


**REPAIRED** `1e1e2a5` · `scripts/wt198_paperII_citations.py`, copying `-81`'s `IV-7` repair. Eight of
the nine are now cited at the sentence that relies on them — the three kinetic-exchange entries at
§ 1's *"the kinetic-exchange literature has established this repeatedly"*, Gabaix at § 6's tail-index
clause, and Kaldor, Auerbach, Toder and Viard, and Saez and Zucman at § 6's public-finance paragraph.
**Piketty (2014) is CUT:** no sentence relies on it, the paper is positive throughout and says so,
and padding the body to justify an entry is the move Pass A forbade. **Checked:**
`wt133_crossref_sweep.py` sweep 2 now reports paper-II **15 entries, 15 cited, 0 not**.

### `SL-9` · paper-IV § 9 item 9 — an exhaustive count of the paper's own unmeasured absences

**Site:** `docs/papers/paper-IV-composition/paper-IV.md` lines 642–652.
**Text:** *"**Three others are not measured:** § 1.1's *the input-output energy table has no lapse
to report* … and § 7's two within-literature absences…"*
**Why nothing supports it:** the three named are correct and the item's internal arithmetic checks.
But *"three others"* asserts the enumeration is **complete**, and **no instrument in the frozen set
enumerates this paper's absence claims** — the one that would is the scope-sentence sweep, which
DoD § 1.1 forbids building before the ship. The paper claims a census it cannot currently defend.
This is `II-43`'s shape (*"five quantities"* where there were six).
**Source:** tee-up 7, whose own words were *"rule on it or build the check, don't re-notice it."*
**Building is forbidden, so this is the ruling.**
**THE REPAIR — one clause, and it is the point of the ruling:** make the sentence claim what it can
support. *"Three others, named here, are not measured"* asserts the three are unmeasured without
asserting they are all of them. **Do not attempt to verify exhaustiveness; that is POST-SHIP work
and is already logged there.**


**REPAIRED** `1e1e2a5` · `scripts/wt196_absence_census.py`. **Two clauses, not one** — the item asserted
its census twice, and a repair landing at one site leaves the document asserting both things. The
lede is now *"One of this paper's absences is measured and three others named here are asserted"*
and the enumeration *"Three others, named here, are not measured"*. Exhaustiveness was **not**
verified; that is POST-SHIP work and is logged there.

---

## WHAT IS NOT ON THIS LIST, AND WHY — so nobody re-derives it

| | |
|---|---|
| **The other 68 of 70 ledger findings** | **Repaired in the pass that found them**, and five of the highest-value repairs were re-verified against the current text this session. See `REVIEW-038` § 2. |
| **42 of `wt184`'s 44 Rule-1 flags** | **Adjudicated FALSE with the reason and the mechanism**, in `REVIEW-038` § 3. Four distinct false-positive mechanisms are named there. |
| **All C-class findings (156 counted)** | **DoD § 2.5: C-class never appears on the S1/S2 ship list.** C-d and C-c belong to Pass C, the rest to Pass D. The counts are in `REVIEW-038` § 4 so those passes are sized rather than hoped for. |
| **Seven of the nine carried tee-ups** | S3 or new-instrument ideas → `POST-SHIP.md`. Two (4 and 7) became `SL-8` and `SL-9`. |
| **Every `wt184` / `wt181` / `wt133` instrument defect** | Apparatus, not manuscript. `REVIEW-038` § 3.3 carries the false-positive-reduction spec; DoD § 1.1 permits it as a *repair*, and it does not block. |
