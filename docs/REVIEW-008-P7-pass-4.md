# REVIEW-008 · `P7` CONVERGENCE PASS 4 — Paper II, second independent read

*wealthTensor-68 · 2026-08-17 · the fourth `P7` pass, and Paper II's second end-to-end read.
**Two new findings, both repaired.** Pass 3 found nine; this pass found two, both small — the
manuscript is converging, and the count says so more credibly than an adjective would. The
inherited abstract question (card `1217561330623702`) is **decided at (a): leave it**, with the
rationale in §4. Consecutive-zero count stays 0 for Paper II.*

---

## 0 · What this pass is

`-64` (REVIEW-007) read Paper II end-to-end for the first time and found nine. Since then the
manuscript moved in 24 places across `-65`'s Decision-A application and `-67`'s citation
placements — §1, §3.1 and §6 most recently. `WT-091`'s rule: only an end-to-end read asking
`P7`'s question counts as a pass. So: the full current manuscript, 537 lines, **diffed first**
against `.bak-wt67-cites`, `.bak-wt65-decA` and `.bak-wt64-p7` per `-61`'s standing order that a
corpus under repair has a moving referent — and then read as a whole, not as a diff.

Suite before the pass: **1078 passed, 0 failed** (run by this session, number read from the
summary line, not from `$?`). Suite after the repairs: **1078 passed, 0 failed**. Board: 66
criteria, `matches measured reality`, before and after.

---

## 1 · THE RE-GRADE — every repair since pass 3 holds

- **`II-2`** (abstract said "in compression" where §3.1 says "in κ") — repaired by `-65`, holds.
  The abstract now reads "an order of magnitude in κ, the levy's compressive budget."
- **`II-3`** ("statistically indistinguishable" at ρ = 0) — repaired **upward** by `-65` to the
  structural identity, holds, and the claim is *measured*, not asserted: `np.array_equal` on the
  two wealth vectors returns True, max difference 0.0 (LEDGER, `-65`/`-66`). The **test** for it
  still under-asserts — that is apparatus, carded at `1217547799559841`, and not a manuscript
  defect.
- **`-67`'s seven edits** (§3.1 credit paragraph, §6 rewrite in four paragraphs, §1 contribution
  2 narrowed, both reference entries upgraded to ✓⧗) — all hold. **Both §3.1 quotations were
  re-verified verbatim against the preprint itself this pass** (`ar5iv` full text of
  `cond-mat/0002374`; the local PDF did not survive on darwin): *"tend to reduce the inequalities
  of wealth (i.e., lead to an increase of μ), even more so if part of this tax is redistributed"*
  and *"quite surprisingly, capital tax, if used simultaneously to income tax and not
  redistributed, leads to a decrease of μ"* — character-exact, including the comma after "i.e.".
- **The two-rankings coherence check, run because the credit paragraph invites it.** The paper
  now carries two orderings at once: at matched **rate**, stock ≫ flow (the κ order-of-magnitude);
  at matched **budget**, flow out-compresses stock (0.125 against 0.222 at κ ≈ 0.10). B&M's
  income-tax-favourable ranking is the *matched-budget* one, which is the comparison the credit
  paragraph sits inside, and "buys less compression per unit of budget" says so. Dense, but
  consistent — scored as checked, not as a defect.

---

## 2 · THE TWO, both repaired (`scripts/wt124_paperII_p7pass4_edits.py`, `.bak-wt68-p7` kept)

| id | site | the defect | how it was settled |
|---|---|---|---|
| `II-13` | §3.1 table | the table states no configuration for its flow rows. They run at **full realisation, ρ = 1** — `redistribution.py:89`'s default — and a reader can only reverse-engineer that from §2.3 plus the half-failed-prediction paragraph. The exact species of repaired `II-12`, one section over. | code (default read from the constructor) + a one-sentence table note |
| `II-14` | §3.1 | *"a change of six parts in a million"* for 0.076542 → 0.076536. The **absolute** change is 6 × 10⁻⁶ and the phrase is exact under that reading; under the conventional **relative** (ppm) reading it misstates the change by ~13× (true relative ≈ 78 ppm). In a paper that calls a 4–7 % residual "a denominator convention rather than noise", a quantity with two readings an order of magnitude apart is a defect. | arithmetic; the repair writes the number |

Both survived pass 3 — `II-14` verbatim (it is in `.bak-wt64-p7`), `II-13` because §3.1's table
was checked for its *numbers* (byte-exact, `-64` §4) and not for its *configuration statement*.
That is the convergence machine working: what a pass checks, the next pass need not re-find; what
it did not ask, a later pass asks.

**Method note.** `wt124` carries the full `-67` guard kit: whole-anchor `assert count == 1`
before any write, `.bak` first, `--dry`, idempotence guard **normalised and asserted** — and then
**fired**: a second live run exits 2, verified this session rather than read. Glyph guard (no
U+00B5 entered a manuscript; census after: 0). Edit labels are `ED`-prefixed; the exhibit-label
canary stayed green through the full suite.

---

## 3 · SCORED AND NOT DEFECTS

- **The version stamp** (*"v0.2, 2026-08-11"* over four further sessions of repairs) — pre-scored
  by `-64` §5 as a corpus-wide convention question belonging to `P8`/`P11`. Not re-scored.
- **The ρ = 0 test under-assert** — carded (`1217547799559841`), apparatus not manuscript; the
  manuscript's claim itself is measured (§1 above).
- **"stock 0.000 asserted, not tabulated"** — unchanged since `-64` scored it not-a-defect.
- **"Rate 0.25 on stock reaches 0.125"** — produced by the committed command (`wt030_report.py`
  sweeps *r* ∈ {0.01, 0.025, 0.05, 0.10, **0.25**, 0.50, 1.00}); not re-derived, provenance
  confirmed.
- **The abstract's ceiling sentence** — decided, next section.

---

## 4 · CARD `1217561330623702`, DECIDED AT (a): THE ABSTRACT STAYS

The question `-67` raised and refused to decide: §6 now concedes the bare stock-versus-flow
contrast to Bouchaud & Mézard; the abstract still opens its results with "the base sets a ceiling
the rate cannot cross." Does the abstract owe the concession?

**No, on four grounds, and the decision belongs to this read because the card said so.**

1. **The abstract claims no priority.** It states the paper's results in the paper's own
   coordinates. The overclaim hazard would be "novel", "first", "we show for the first time" —
   none present. Stating a result an abstract's paper demonstrates is not an assertion that
   nobody else ever demonstrated its coarser form.
2. **The quantitative content the abstract does stake out is the paper's own** per `WT-103`: the
   order of magnitude **in κ**, the closed form, the self-falsified prediction reported as false.
   The part that is prior — the bare contrast — is precisely the part the abstract's specific
   numbers do not claim.
3. **The concession is one click away, not two.** §1's contribution 2 — the first substantive
   text after the abstract — says in terms: *"The stock-versus-flow contrast this result sharpens
   is prior and is credited in §6."* A referee who recognises B&M from the abstract meets the
   credit in the same minute.
4. **The economics of the ceiling.** 244/250 words; `-65` measured twelve candidate rewrites and
   every one that *added* a clause blew the limit. A citation cannot appear in this journal
   register's abstract anyway, and a creditless hedge ("a known contrast") would weaken a
   measured statement without discharging the obligation — the obligation discharges where a
   citation can appear, which is §1 and §6, where it now does.

The falsifier that would reopen this: a referee report that reads the abstract as a priority
claim. If that arrives, the repair is `WT-102`'s shape — achieve the demotion by **deleting** an
assertion, not by arguing with it — and the six words of slack are still on the table.

---

## 5 · CONVERGENCE ARITHMETIC, stated plainly

Paper II end-to-end reads: pass 3 → **9 findings**; pass 4 (this) → **2 findings**, both
repaired in-pass. `P7`'s bar is two *consecutive* zero-finding passes, so the count **stays 0** —
but the trajectory 9 → 2 is the first measured evidence of convergence for any manuscript in the
batch. The next independent read of Paper II is the first with a live chance of being a zero.

*(Student-in delta, recorded per the handoff's instruction: `lessons.py` surfaced two leaves the
handoff does not carry that shaped this read — the Gini-hard-ceiling leaf (WT-034), which is §3.4's
own result and was checked for consistency at every site quoting 0.994; and the
multi-document-contradiction leaf, which is why §3.2's and §7's two different "companion" works
were re-checked as distinct rather than trusted as repaired.)*

---

## 6 · WHAT WAS TOUCHED

- `docs/papers/paper-II-redistribution/paper-II.md` — 2 hunks, 2 findings. `.bak-wt68-p7` kept.
- `scripts/wt124_paperII_p7pass4_edits.py` — the patch script (tag `wt124`; `wt125` is free).
- `docs/REVIEW-008-P7-pass-4.md` — this document.
- `docs/LEDGER.md` — `WT-105` (fact), `WT-106` (method).
- Board regenerated: `matches measured reality (66 criteria)`, before and after — the board did
  not move for a config-note and a wording repair, consistent with `-66b`/`-67`'s standing
  observation that no criterion tracks framing.
- Abstract untouched: `check_abstract_size.py` → **244 words / 1478 chars**, unchanged.
- Full suite after: **1078 passed, 0 failed**.
