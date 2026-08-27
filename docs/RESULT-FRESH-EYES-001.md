# RESULT · FRESH-EYES-001 — the judgment rows, judged

*`wealthTensor-109b` · 2026-08-27 · the recorded verdicts for the board rows whose check says a
**fresh-eyes pass** may score them. This document reports judgments; the rows in
`docs/done-criteria.tsv` grep it rather than restating it.*

---

## 0 · Why this file exists, and who was allowed to write it

Jason's ruling of 2026-08-27, on the shape every project in this estate runs in: **TICK is Claude,
all the way to "cleared for liftoff"; TOCK is Jason, once, at the end, in a fresh project.** The
whole value of the tick is that it maximises what Claude finishes *before* a human's calendar is in
the loop, because a human takes a day or five to come back and a board that waits on him for work he
was never needed for wastes the whole gap.

Applied to this board, that ruling exposed a conflation. `board.py` renders every `manual:` row as
🧍 **PENDING-HUMAN**, but `manual:` has never meant *Jason* — it means *judgment, not a script*, and
judgment can be a session's. Eight lanes read PENDING-HUMAN on 2026-08-27 and **exactly one of them
was Jason's**. Two were stale notes on work finished ten days earlier (`P11`, `P6` — both now
derived checks). Four said in their own text that a fresh session was the judge:

| row | what its own check says |
|---|---|
| `P2` | *"the measurer should not also score it — P7's fresh eyes and P8 are the judges"* |
| `P3` | *"the session that closed the gaps should not also score whether the paper is ready"* |
| `P13g` | *"**Jason or a fresh-eyes pass** calls it. Do NOT close this from the session that built the layout"* |
| `P9` | *"**declaring readiness is the session's job** (never ask Jason to trigger anything)"* |

**The bar those rows set is independence, not humanity.** `-109b` did not write these manuscripts,
did not close their gaps, and did not build this layout — the sessions that did were `-52`, `-53`,
`-54` and `-108`. It is therefore eligible under every one of those clauses, and `P7`, the
machine-checkable half of `P2`/`P3`'s stated pair of judges, is CLOSED.

**What this file may not do.** It cannot score `P8` (Jason reads the deliverable and clears it for
liftoff — a human gate a script can satisfy is not a human gate) and it does not touch which drafts
become v1.0. `P5` is Jason's for a reason recorded below.

---

## 1 · P13g — the layout presents to economics convention

> *The manuscript presents to ECONOMICS convention — Chicago author-date references and the house
> layout an arXiv q-fin / econ.GN reader expects.*

**Method.** The built capture was read as a reader meets it, not as markdown: four pages rendered at
110 dpi and looked at (title, a body page of §4.7, a references page, the §9/§10 boundary), plus two
mechanical sweeps over all 147 pages.

- **Verdict: P13g NOT MET** — two defects, both specific, both reproducible, one now repaired.

**Defect 1 — sixteen mid-word line breaks inside monospace identifiers. OPEN.**

Measured against the four manuscripts as ground truth (not against the PDF's own text, which joins
the breaks back together and hides them — the first attempt at this sweep read fragments against
fragments and reported zero):

| break location | count |
|---|---|
| at an underscore — defensible | 10 |
| **mid-word — a defect** | **16** |

Instances include `wt083_ti|er_ladder`, `wt084_identificati|on`, `wt089_recognitio|n`,
`test_excess_demand_is_monotone_h|ere_so_this`. A reader meets `_h` at the end of one line and `ere`
at the start of the next.

**This is a live trade-off, not an oversight, which is why it is reported rather than repaired.**
`preamble.tex` step 13 states the property it wants: identifiers must break **without inserting a
character**, so what a reader copies out of the PDF still runs. `\def\UrlBreaks{\do\_}` delivered
exactly that. Then `-94` measured two cases the underscore rule cannot serve — a 47-character
repository URL with no underscore anywhere, and a bare 64-character SHA with no break opportunity of
any kind, overflowing the measure by 30.8pt and 62.8pt — and added `xurl`, which grants a break
opportunity at **every character**. It fixed the overflow and silently discarded the underscore-only
rule for identifiers. Step 13's *stated* reason survives (copy-paste still works); its *readability*
did not, and nothing re-examined it.

**The remedy is not to drop `xurl`** — that reintroduces two measured overflows. It is to separate
the two populations `wt175_md2tex.lua` currently routes to one macro: snake_case identifiers (break
at `_` only) and URLs/SHAs (break anywhere, as now). Two macros, two behaviours, each matched to its
content. That is a change to `wt175_md2tex.lua`, `preamble.tex` and `RECIPE.md` step 13, plus a
clean-tree rebuild and a manifest regeneration — a well-specified at-bat, and deliberately not taken
unilaterally here because it edits the typographic contract `ADR-002` sets.

**Defect 2 — limitation 9 severed from its own list. REPAIRED at `46b00fc`.**

Page 96 of the previous capture showed limitation 9 floating between two full-width horizontal
rules, detached from limitations 1–8 on the page before and sitting immediately above the §10
heading. Cause: a `---` between items 8 and 9, which in CommonMark terminates the list, so item 9
began a second one. Every other manuscript carries exactly one rule in its Limitations section;
`paper-III.md` carried two, and `paper-III-v1.md` does not have the defect.

It was the worst item to lose that way — 9 is the one conceding that the reporting layer's
diagonality is an assumption, was testable, and **is false**, at 4.12× and 2.02× the independence
expectation. A concession that reads as a stray note is a concession a reader discounts. Rebuilt and
verified: 147 pages, all per-page hashes reproducing from `46b00fc`.

**What is positively good, said because a verdict of NOT MET on two specifics should not be read as
a verdict on the whole.** The body pages are set properly: Libertinus at a ~65-character measure,
correct discretionary hyphenation (`cross-/sectional`, `ex-/change`), Greek and inline mathematics
sitting on the baseline, superscripts and hats rendering cleanly, `booktabs` tables with no vertical
rules, a running footer carrying the source commit and date on every sheet so no printed page is
ambiguous about which capture it came from. Zero overfull boxes and zero missing characters, both
promoted to fatal by `build.sh`. The references carry an explicit statement of the citation rule and
per-entry verification marks, which is stricter than Chicago asks for.

---

## 2 · P3 — paper II re-measured, gaps closed, ready to submit

- **Verdict: P3 MET.** Read in full against its own criterion. No gap; three nits, none of them a gap.

The apparatus legs `P3a`–`P3n` are green and `P7` is CLOSED, so the mechanical half is settled and
what remains is whether the prose is ready. It is, and unusually so:

- The falsified prediction is in the **abstract**, in §3.1, and in *Abandoned approaches* — reported
  three times and buried nowhere. §3.1 names the surviving claim as *narrower and better*.
- §5's first limitation runs against the paper's own comfort exactly as `P3g` requires, and does it
  honestly: endogenising ρ would make the flow base **weaker** than reported.
- §7 enumerates the **six quantities no command prints**, which is a standard of reproducibility
  disclosure well above the norm, and *Known limitations of this review* names two unchecked things
  rather than leaving them to be found — including that its own "4–7 %" band is an **under-claim**.
- Arithmetic spot-checked and correct: §3.4's 0.103 gap (0.994 − 0.891), its 0.039 margin
  (0.90 − 0.861), §3.3's 0.035 span (0.486 − 0.451).
- Reference orphans checked mechanically rather than by eye: `wt133` reports 15 entries, 15 cited.

**Three nits, recorded so a later pass need not re-find them:**

1. **Two notation collisions handled by apology rather than by renaming** — §2.1's wage *a* against
   §2.4's Var[log *a*], and §2.1's growth drift μ against Bouchaud–Mézard's Pareto exponent μ. Both
   are flagged in-text with almost the same phrase (*"with which it unhappily shares a letter"*), and
   the repetition draws attention to itself. **Register, therefore FLAGGED and not fixed** — re-voicing
   is Jason's pass per `DEFINITION-OF-DONE-SHIP` §2.5.
2. **"The Lucas critique" is cited by name without a year** (§5, limitation 3) while the reference
   list carries Lucas (1976). Strict Chicago author-date wants the date at the mention. `wt133`
   cannot see this: it keys on surname presence, not on citation form.
3. **The same five objects are labelled two ways.** §5's limitation 5 calls them *"the five
   closed-form quantities §7 names"*; §7 calls them *"four closed-form quantities"* plus §3.4's Gini
   ceiling, *"which is arithmetic in N"*. Numerically consistent, and a careful reader trips on the
   label.

---

## 3 · P2 — paper III gaps closed in the prose, in the file

- **Verdict: P2 MET.** Read in full. One presentation defect found and repaired this pass (§1,
  defect 2); no open gap in the prose.

`P1x` is complete and green, `P7` is CLOSED. On the prose, this is the most self-adversarial document
in the corpus and the checks that matter are structural rather than stylistic:

- **The failed prediction is a result, not an excuse.** §5 reports it at full length with its power
  curve, its negative control, and its stopping rule fired. §6.1 goes further than most authors
  would: *"the framework currently has no confirmed empirical claim."* And §6.1 explicitly refuses
  the comfortable reading — *"if nothing in §A.2 or §§2–3 was at risk, then nothing in §A.2 or §§2–3
  was on test."*
- **§6.3 withdraws an argument the paper wanted to make** — the comparison to Odum's emergy
  programme — on three grounds a sceptical reader would have reached first, one of which is that *"a
  paper does not get to grade its own integrity."* Withdrawing a flattering argument unprompted is
  the strongest single signal in the corpus.
- **§8.1 withdraws the paper's own reply to its most serious standing objection**, in full, and says
  so in the section title.
- **§7's survivals ledger names the checks that *rewrote* the paper** — the goodwill-limit row, the
  two-rates row, the row that removed two numbers from §4.7 — rather than only the ones that held.
- **§5.1 discloses that PRE-002's registration shipped in the same commit as its instrument**, and
  distinguishes a *demonstration* from an *account*, inviting the reader to weight them differently.
  That disclosure costs the paper something and was volunteered.

**One nit, and it is the same class as paper II's:** §9's limitation 4 is roughly 15 lines of dense
prose carrying four distinct concessions (φ swept; α measured for the wrong quantity; the bridge
unwritten; §4.9's settlement). It reads as a paragraph that outgrew its list item. **Register,
FLAGGED not fixed.**

---

## 4 · What this pass did NOT judge, and why

- **`P8`** — Jason reads the deliverable and clears it for liftoff. A human gate a script can satisfy
  is not a human gate. Untouched, and it is the only true tock on this board.
- **`P5`** — *Paper IV ready to submit.* Not judged, and not rescoped. Paper IV was **stood down** on
  this branch at `-108`, on the corpus's own end-to-end verdict, so the row now asks whether a
  withdrawn manuscript is ready to submit. Rescoping a criterion changes the definition of done, and
  on a branch whose central open question is *which drafts become v1.0* that decision is upstream of
  this row and is Jason's. **Marked `human:` for that reason and no other** — the moment the v1.0
  ruling lands, `P5` becomes mechanical again.
- **Which drafts become v1.0.** Untouched by construction.
  `docs/deliverable/NOT-IN-CAPTURE.tsv` still declares both `-v1` drafts outside the capture, so the
  deliverable follows that decision rather than anticipating it.
