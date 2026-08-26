# METHOD-002 · Measuring whitespace instead of asserting it

*A pre-registered bibliometric instrument for the claim "these literatures do not read each other,"
with both ends of its scale fixed in the same run. Written at wealthTensor-108 from `paper-IV.md` §6,
carried over with the manuscript's own wording when the fourth paper was stood down.*

---

## 0 · Why this is a `docs/` method and not a section of Paper II or Paper III

The instrument was built for a manuscript whose motivation was a **three-literature junction** —
biophysical economics, stock-flow-consistent modelling, kinetic exchange. Neither surviving paper
makes that claim. Paper III places itself result-by-result against accounting, pharmacokinetics and
identification theory (§12); Paper II places itself inside kinetic exchange and public finance (§6).
A measurement that no surviving claim rests on does not belong inside either.

The obvious alternative — a subsection of Paper III §13 — was refused on a narrower ground. **§13 is
an enumeration of the registered materials that produce Paper III's numbers**: PRE-001, PRE-002 and
REG-003 through REG-008. REG-013 produces none of them. Adding it there would make §13 false about
its own scope, which is a worse defect than the orphaning it was meant to cure.

So it lives here, next to `METHOD-001`, under the same reasoning `ADR-001` gives for a public
`docs/`: **a reusable instrument is worth more than the paper it was built for.** Anyone motivating
a paper by a gap can run it.

---

## 1 · The problem it solves

A paper that joins several literatures usually motivates itself by reporting that they do not meet,
and the evidence offered is that the author looked. That is the first thing a referee attacks, and
correctly: **an absence found by searching is a property of the search.**

So it was measured instead, and pre-registered first (`REG-013`, committed before the instrument
existed). The design's whole content is that a low co-citation rate between two specialties is
**uninformative on its own** — sociology and semiconductor lithography do not cite each other
either. What makes a number here mean something is a scale with both ends fixed in the same run.

---

## 2 · The instrument

Each literature is defined by seed works named in `REG-013`, and its *audience* is the set of works
citing at least one seed, taken from OpenAlex. For two literatures the statistic is the overlap
coefficient — the share of the smaller audience that also reads the other. Audiences are truncated
at the 4 000 most-cited works before the overlap is taken; §4's second qualification states what
each truncation costs. Twenty-five of twenty-five seeds resolved.

**The ceiling** is each literature split in half by seed index and measured against itself. It
cannot be tuned: if the instrument cannot see that half of econophysics is joined to the other
half, it cannot see anything, and the registration voids the run below 0.20. It came back at
**0.477** pooled.

**The floor** is each literature against six highly-cited CRISPR papers — unrelated to economics by
construction. It came back at **exactly zero**: of the 4 000 most-cited works citing a CRISPR
seed, not one is in any of the three economics audiences.

---

## 3 · The three pairs, on that floor-to-ceiling scale

The position *z* places a pair's overlap on that scale — (overlap − floor) ÷ (ceiling − floor), so
the floor reads 0 and the ceiling 1 — and `REG-013` fixed the bar in both directions before the run:
*z* ≤ 0.10 is whitespace, *z* ≥ 0.25 is joined, and the band between them is undecided.

| pair | works citing both | audience (smaller) | overlap | position *z* |
|---|---|---|---|---|
| biophysical × stock-flow | **23** | 1 139 | 0.0202 | 0.042 |
| biophysical × kinetic exchange | **15** | 1 383 | 0.0108 | 0.023 |
| stock-flow × kinetic exchange | **6** | 1 139 | 0.0053 | 0.011 |

Against split-half intersections of 134, 155 and 380 *within* the same three literatures. **Six
works in the world cite both a stock-flow-consistent seed and a kinetic-exchange seed.** All three
pairs sit below the whitespace bar; the whitespace is where it was claimed to be.

---

## 4 · Two qualifications, both stated as the registration requires

**One.** Biophysical economics is on this instrument a *loose federation*: its own split-half overlap
is 0.168, well below stock-flow's 0.520 and kinetic exchange's 0.744, because its seeds are
monographs spanning four decades and three sub-traditions that do not much cite each other.
Scoring the biophysical pairs against the pooled ceiling is therefore generous to them. Under a
stricter per-literature ceiling, biophysical × kinetic exchange and stock-flow × kinetic exchange
remain whitespace, and **biophysical × stock-flow becomes undecided** (*z* = 0.120 against a 0.10
bar). The registered rule is the one that governs — re-choosing a ceiling after seeing which
verdict it yields is not available — but the result is stated as it is: *two pairs are whitespace
under every reading tried, and one is whitespace under the registered rule and undecided under a
stricter one.*

**Two.** The biophysical audience was capped at 4 000 of 7 801 by descending citation count, so a
bridging work in its tail is invisible here, which suppresses both biophysical overlaps. The floor's
cap is tighter still — 4 000 of 43 048, 9.3 per cent — and it does the opposite and costs nothing: a
cap can only remove intersections, so the measured floor is a lower bound on the true one, and a
floor of exactly zero is the strictest value available. Both true-audience sizes are
`RESULT-REG-013` §2's. The instrument stops retrieving at the cap and does not print them, which
makes them the two numbers here that §5's command does not regenerate.

**And what the measurement does not establish, stated in `REG-013` before the numbers existed:** an
unoccupied intersection is not thereby a fertile one. This instrument establishes that literatures
do not read each other. That there is something worth finding where they meet is what a paper's
own results have to earn.

---

## 5 · Reproduction

- **Pre-registration:** `docs/preregistration/REG-013-citation-graph-whitespace.md`, committed in
  `fff7063`, before the instrument existed.
- **Instrument:** `scripts/reg013_citation_whitespace.py`
- **The record:** `docs/preregistration/RESULT-REG-013-run.log` and
  `RESULT-REG-013-run.json`, the committed output of the 2026-08-16 run, with
  `RESULT-REG-013.md` reading the verdict off them. **Those files, not a command, are the record.**
- **Re-run:** `python3 scripts/reg013_citation_whitespace.py`. It reproduces the *instrument* and
  not the *pull*. Each cluster's audience is retrieved live from OpenAlex, so a run depends on that
  graph on the day it is made and on the API's rate limit: one attempt on 2026-08-18 exited non-zero
  on `HTTP 429` inside the ceiling control, and a second the same day exited zero and returned every
  figure above unchanged — the three intersections, the three overlaps, the three split-half
  intersections, the pooled ceiling and the zero floor — while the seed citation counts the run
  prints had already moved. That second run is committed at
  `docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json`, and it replicates the result on the
  live graph rather than regenerating it from anything held here. **Nothing in this repository
  re-derives these figures from committed data**, and that is a property of a citation-graph
  instrument rather than a gap in the archive.

---

## 6 · If you want to use it

The transferable part is not the numbers; it is the shape. **Fix both ends of the scale in the same
run, register the bars before you look, and report the reading a stricter ceiling would give.** A
co-citation count with no ceiling and no floor is a number with no units, and a referee is right to
say so.
