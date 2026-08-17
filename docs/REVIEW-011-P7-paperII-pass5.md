# REVIEW-011 — Paper II, `P7` pass 5: the THIRD independent read

**Session:** `wealthTensor-71` · **Date:** 2026-08-17 · **Instrument:** one reader, whole
document, no grep-first.
**Counter before:** pass 3 = 9 findings, pass 4 (`-68`, `REVIEW-008`) = 2. **This pass: 4
repaired + 1 carded.** Consecutive-zero count stays at **0**.

**This is not a zero, and the shape of the four is the interesting part.** None of them is a
wrong number. Every arithmetic claim in this paper checks (§3 below lists the recomputations).
All four are **quantifier and reference defects**: a law stated without its condition, a range
attributed to a table that does not contain it, an "every number" that §7 contradicts in terms,
and a count of two in front of a list of five. A paper this heavily reviewed has stopped getting
its numbers wrong and has not stopped over-claiming the *scope* of its own sentences.

---

## §1 · SCOPE — both halves (`-70`'s `WT-111`)

**What I read.** `docs/papers/paper-II-redistribution/paper-II.md`, lines 1–541, end to end,
once through, in order — abstract, §1–§7, References and the closing citation note. Not by
grep, not by section.

**What I read it against.** The paper's own internal consistency, plus §7's provenance claims
checked against the repository, plus the board criteria that govern this file (`P3a`–`P3n`,
read *before* editing per `-70`'s `WT-110`).

**Provenance verified before reading, not believed.** The handoff said Paper II was untouched
since `-68`. Confirmed independently: `git log -- docs/papers/paper-II-redistribution/paper-II.md`
ends at `3b073bd` (`-68`); `git status` clean; the diff against `.bak-wt68-p7` is exactly two
hunks and both are `-68`'s repairs (§3.1's ρ = 1 footnote, `II-13`; and `six parts in a million`
→ `6 × 10⁻⁶`, `II-14`). One oddity, chased and cleared: all four manuscripts carry an mtime of
2026-08-17 16:53:42 with **identical** timestamps and clean `git status` — a bulk touch that
changed no bytes, not an edit.

**What I changed.** `wt128`, five edits in four places: §3.1's budget bullet, §3.1's table
footnote, §3.4's range sentence, §5's limitation 5, §6's topic sentence. **The abstract, §1,
§2, §3.2, §3.3, §4, §7 and the References were read and NOT edited.**

---

## §2 · FINDINGS

### `II-15` — a law stated without its condition, falsified two subsections later (§3.1)

§3.1's budget bullet read *"for a **stock** base, κ = *r* exactly"*. That is true only at zero
exemption. **§3.3, in the same paper, is the counterexample**: a threshold at 0.25× the mean
*"reduc[es] κ by a quarter"*. A reader quoting the bullet as the paper's closed form is quoting
something the paper itself disproves 110 lines later.

The bullet is scoped *by context* — it explains the third column of a table whose rows are all
θ = 0 — but nothing in the sentence says so, and §3.1's own next-but-one paragraph cites §3.3's
threshold result approvingly, so the author plainly knew. **Repair:** *"for a **stock** base at
zero exemption, κ = *r* exactly — §3.3 raises the threshold and κ falls"*. §3.3 is the witness;
no number and no new claim enters.

### `II-16` — §3.4 quantifies over a sweep §3.1 does not display (§3.1 + §3.4)

§3.4 says *"Across the sweep of §3.1 the bounded runs' Gini spans **0.000–0.891** ... their top
decile spans **0.100–0.861**"*. §3.1 shows a **six-row** table. Its bounded Gini range is
0.125–0.812 and its top-decile range is 0.138–0.734. **Neither endpoint matches, and three of
those four numbers appear nowhere else in the paper** (only 0.000 does, as §3.1's stock
frontier). A referee who tries to check 0.891 goes looking in §3.1 and finds nothing.

This is `-68`'s `II-13` one turn further out. `II-13` was *the table's configuration is
unstated* and was repaired by saying what the rows **are** (ρ = 1). This is *the table's
coverage is unstated* — what the rows are **not**, namely all of it. Same family, opposite half.

**Repaired from both sides, because a scope note needs two halves (`WT-111`).** §3.1's footnote
now says the six rows are a selection and that §3.4 quantifies over the whole sweep; §3.4 now
says *"Across §3.1's full rate sweep — wider than the six rows tabulated there —"* instead of
pointing at §3.1 as though the range were readable there. **No new number enters either side**,
deliberately: the honest fix is to stop the paper claiming the reader can check the range
against a table, not to paste in more rows this pass did not regenerate.

### `II-17` — "every number above" is contradicted by §7, in terms (§5)

§5's limitation 5: *"every number above is a mean over a tail window of a **single** path at
`seed = 0`"*. §7: *"except the three Var[log *a*] values in §3.1, which are **quadrature over
the multiplier's distribution rather than simulation output**"*. Two sections of one paper, in
flat contradiction, and the paper is *right in §7*.

**Severity is higher than a quantifier slip, and it runs against the paper.** Those three values
are 0.076542 / 0.076536 / 0.051189, and they carry §3.1's *"a change of 6 × 10⁻⁶, which is to
say none at all"* — the sentence on which the stock-truncates-the-outcome / flow-damps-the-
generator distinction rests. Limitation 5 ends *"the third decimal is not defended"*. Read
literally, §5 **withdraws the precision §3.1 needs** and hands a referee the paper's own
retraction of its own headline contrast. **Repair:** scope the quantifier to simulated numbers
and name the exception in §7's own words — *"the exception is §3.1's three Var[log *a*] values,
which are quadrature rather than simulation output (§7)"* — so §5 now says what §7 already said.

### `II-18` — a count of two in front of a list of five (§6)

§6 opens *"**Two results** in that literature are prior to this paper's central contrast"*. Two
paragraphs later: Benhabib, Bisin and Zhu *"supply **three further results**"*, the first of
which (their Proposition 3) is then said to have made this paper's §3.1 frontiers *"already
visible"* — i.e. is itself prior. Bouchaud and Mézard supply two more. The topic sentence
promises two and the section delivers five.

The noun is what is wrong. Exactly **two bolded works** are cited, and the paragraph structure
says so. **Repair:** `results` → `works`. One word; the sentence's count becomes true and the
arithmetic reading disappears.

### `II-19` — CARDED, not repaired: §3.1 and §6 describe one source twice

§3.1: *"Bouchaud and Mézard (2000) carry a flow levy, a stock levy and the per-capita
redistribution of each in **a single** wealth balance, and give the stationary Pareto exponent
in closed form in all four coordinates."*
§6: *"**Bouchaud and Mézard (2000)** carry a flow levy, a stock levy and the per-capita
redistribution of each in **one** wealth balance and give the stationary Pareto exponent in
closed form in all four coordinates."*

~40 words, near-verbatim, in two sections. **Nothing is wrong today** — they agree. This is
`-70`'s `IV-15` shape exactly: *a paraphrase of another section's content is a standing drift
generator that nothing measures*, and `IV-15` is proof the generator fires.

**Why it is carded and not fixed here.** The placement is **settled**: `bf07363` (`-67`) placed
*"the two mandatory citations ... where they bind"*, and §3.1's copy carries the verbatim
quotations and the μ-collision disclosure that §6's does not. Deleting either, or merging them,
is a structural decision about where the credit lives — a ruling this pass has no standing to
reopen on a defect that is currently latent.

**Named falsifier:** edit one description without the other; the paper then describes one source
two ways. **Cheapest guard:** assert `norm()` of the Bouchaud–Mézard description is identical in
§3.1 and §6, or that only one exists.

---

## §3 · CLEARED — read, checked, found innocent

Recorded so `-72` does not pay to re-derive any of it. **A cleared list is a coverage claim and
this one is deliberately specific about what "checked" means in each row.**

1. **Every §7 provenance claim, checked against the repository, all true.** The pin `3b11f23`
   *is* still the last commit touching `src/wealth_tensor/redistribution.py` (2026-08-05).
   `scripts/wt030_report.py` and `scripts/wt077_tail_index.py` both exist.
   `tests/test_redistribution.py` defines **18** `test_` functions.
   `test_a_flat_gini_does_not_mean_a_bounded_one` and `test_the_result_is_not_a_lucky_seed` are
   in it at lines 61 and 234; `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`
   is in `tests/test_excess_demand.py` at 102 — which is what §1's *"a companion module of the
   same suite"* claims, so §1 and §7 agree about where the second guard lives.
2. **The "18 tests" coupling holds at all three sites** — abstract, §1 contribution 5, §7 — and
   `wt128` asserts the count did not move. Not deleted, not changed. (`P3n` derives it live.)
3. **κ's closed form recomputed by hand.** E[η⁺] = μΦ(μ/σ) + σφ(μ/σ) at μ = 0.05, σ = 0.20:
   Φ(0.25) = 0.598706, φ(0.25) = 0.386669 → 0.029935 + 0.077334 = **0.107269**. The paper prints
   **0.1073**. Correct.
4. **The three residuals recomputed from the table's own κ column.** (0.0025 − 0.0026823)/
   0.0026823 = **−6.80 %**; (0.0102 − 0.010727)/0.010727 = **−4.91 %**; (0.1026 − 0.107269)/
   0.107269 = **−4.35 %**. The paper prints −6.8 / −4.9 / −4.4 at r = 0.025 / 0.100 / 1.000,
   asserts the residual is **monotone in the rate** (it is), says the form runs **4–7 % below**
   (it does), and §1 contribution 2 claims agreement **within 7 %** (max 6.80 %). All four
   statements are true of the printed table.
5. **"A confiscatory levy on flow has approximately the budget of a 10 % levy on stock":**
   κ = 0.1026 against 0.1000. True.
6. **The Gini ceiling.** (N−1)/N at N = 800 = **0.99875**, exactly as §3.4 prints it.
7. **§3.4's "0.039 to spare"** = 0.90 − 0.861. Arithmetic correct — the defect in `II-16` is
   where 0.861 *comes from*, not what it is.
8. **§3.2's ρ = 0 identity argument is internally valid** against §2.1's process. At ρ = 0 the
   recognised flow is the wage *a* alone, which is identical for every agent; a 100 % levy on a
   uniform base with a per-capita rebate is the identity on the wealth vector. The paper's
   *"what ρ = 0 removes is not the levy but the dispersion in its base"* is the correct
   statement of it.
9. **Both symbol collisions are disclosed and there are no others.** §3.1 discloses *a* (the
   normalised multiplier vs §2.1's wage) and μ (Bouchaud–Mézard's Pareto exponent vs §2.1's
   growth drift), and calls the second *"the second such collision"* — the count is right.
   κ, ρ, θ, σ, η, *P* and *r* each carry exactly one referent throughout.
10. **Glyph census, whole file: clean.** 26 distinct non-ASCII code points. All nine μ are
    **U+03BC GREEK SMALL LETTER MU**; **zero U+00B5 MICRO SIGN**; no mojibake; the superscripts
    in `6 × 10⁻⁶` and `E[η⁺]` are the intended code points.
11. **The stale version header is a CONVENTION, not rot — checked, not assumed.** The front
    matter says *"Version 0.2, 2026-08-11"* while the paper carries content dated 2026-08-17
    (the re-verified Crossref entries) and has had substantive edits since. This is **not** a
    Paper II defect: all four manuscripts behave the same way — I 0.1/08-10, II 0.2/08-11,
    III 0.5/08-12, IV 0.1/08-16 — and III and IV were both edited on 08-17 without a bump.
    Version bumps in this project are deliberate acts, not per-commit. **Named here so the next
    reader does not re-derive it and does not "fix" it into an inconsistency.**
12. **The board's positional criterion was read before editing** (`-70`'s `WT-110`, the whole
    reason it exists). Paper II's positional row is **`P3g`**: it greps **item 1** of
    Limitations for `Endogenising ρ would make the flow base` and requires ≥ 4 items matching
    `^[0-9]+\. \*\*`. `ED4` edits item **5** and inserts nothing, so no ordinal moves; `wt128`
    asserts both legs before *and* after, and the board came back green in one run.
13. **§3.3's numbers are consistent with §3.1's** (Gini 0.443 at r = 0.025 zero exemption
    appears in both), and the periodicity claim's two quoted endpoints (0.486 at P = 1, 0.456 at
    P = 20) are the paper's own named endpoints rather than a claim to span a sweep — so §3.3
    does **not** carry `II-16`'s defect.
14. **The abstract was read and cross-checked against §3** — the nested frontiers (stock 0.000
    against flow 0.125), the ρ = 0 result (Gini 0.994, top decile 1.000), the order-of-magnitude
    κ separation, the threshold-is-near-free claim, and "18 tests" all match the body. **It was
    not edited**, and `check_abstract_size.py` was run anyway (`PASS`), because it is 244/1478
    and the tightest in the batch.
15. **Cosmetic, accepted deliberately:** `ED3` and `ED4` leave two short ragged lines
    (`"0.994, which separates nothing; their top"` and `"separately rather than averaged"`).
    Re-flowing the surrounding paragraphs would have widened the blast radius of a
    quantifier fix for a difference invisible in rendered output. Named, not hidden.

---

## §4 · NOT CHECKED by this pass

**This list is the coverage claim's honest complement.** Everything here was in the file and was
not the instrument's subject.

1. **The References section's bibliographic details.** Read for *structure* only (the ✓/✓⧗ marks
   and the two consulted-version notes are present and internally coherent). **No entry was
   re-verified against a live source or a Crossref record.** `REFERENCE-POLICY`'s sixth pass —
   card `1217556161163494` — is now the **sixth** session it would have covered.
2. **Whether the code implements what §2 describes.** `REVIEW-005` §2's `II-3` is the standing
   warning that a prose instrument cannot report on code. §3's numbers were **not regenerated**;
   in particular §3.1's *"the implementation measures κ against post-growth wealth"* — the
   explanation offered for the 4–7 % residual — was **not** checked against
   `redistribution.py`. It is the most load-bearing unchecked sentence in the paper.
3. **The endpoints 0.891 / 0.861 / 0.100 were not regenerated.** `ED2`/`ED3` make the paper
   honest about where they come from; they do not verify them. `scripts/wt030_report.py` sweeps
   seven rates per base, which is *consistent with* a wider range than the six displayed rows,
   and stock at r = 1.00 would give Gini 0.000 / top decile 0.100 by construction — but that is
   reasoning about the script, not a run of it.
4. **Paper II's companion reference entries** — card `1217542940968749`. Untouched.
5. **§3.3's periodicity sweep beyond the two quoted endpoints.** The script runs to P = 50; the
   paper quotes P = 1 and P = 20. No overclaim (see cleared #13), but the intervening rows were
   not looked at.
6. **The zakat citation gap.** Already flagged by the paper's own closing note; not addressed,
   not re-scoped.
7. **`docs/RESULT-END-TO-END-001-E1.md`**, cited by §3.2 as the record of the withdrawn
   cross-scale identification. Its existence was confirmed; **its contents were not read**, so
   §3.2's characterisation of what that check found is uncorroborated by this pass.
8. **The other three manuscripts.** This pass opened Paper II only.

---

## §5 · STATE AT CLOSE

| thing | result |
|---|---|
| suite | **1078 passed, 0 failed**, 68.67s |
| board | `regen-board.sh --check` → **matches measured reality (66 criteria)**, one run, no STALE |
| coach | `--coach` **RC 0**, Paper II at 2 conduct / 0 concessive — **baseline, unmoved** |
| abstract | `check_abstract_size.py` **PASS**, untouched |
| census | `wt128 --census`, 19011 files, **CLEAN** — every anchor unique over LIVE |
| undo path | `paper-II.md.bak-wt71-p7` (written before the edit, `.bak-*` is gitignored) |

**The board did not move this session.** `-70` moved it with an edit that changed no sentence
and moved it back; this session changed five sentences and the board is silent. That is the
same evidence from the other side and it points the same way: **the board measures structure —
position, presence, naming — and is silent on whether a sentence is true.** All four findings
here are truth-of-a-quantifier defects and not one of them was visible to 66 criteria. That is
a missing axis, not a broken instrument, and it is `(c)` on the Jason list.
