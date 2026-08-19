# ADR-002 · Typography and the reproducible build

**Status:** ACCEPTED · 2026-08-16 · wealthTensor-54
**Decided by:** Claude, on Jason's express delegation — *"I totally trust you with the font
selection :-D. Basically, whatever is apropos for this type of research paper is the best."*
**Governs:** `P13a`–`P13g`. Subordinate to `ADR-001` and to `docs/CO-AUTHOR-CHARTER.md`.

---

## Context

`P13` is the deliverable: a beautifully designed, arXiv-ready PDF of the corpus, **plus the
recipe that regenerates it**. Jason named the failure mode himself, and it is the reason this
ADR exists rather than a line in a build script:

> *"the worst that could happen, and it'd be a very bad scenario — would be it couldn't find the
> same font for example or it didn't have the spacing recipe we use in this project. It could get
> close perhaps but then I have to go back a re-tweak everything… so that after this project is
> done, I only have to do the layout and viz analysis once on it."*

**The mechanism matters more than the fear.** LaTeX does not fail when a font is missing — it
**substitutes**. The build succeeds. The metrics shift by a fraction. The reflow moves. A page
boundary slides. The document comes out *close*, and close is precisely the failure: it spends
Jason's layout analysis a second time, which is the one cost this deliverable exists to avoid.

**And it is not hypothetical on this machine.** Measured on darwin, 2026-08-16: macOS ships its
own STIX Two Text at `/System/Library/Fonts/Supplemental/STIXTwoText.ttf`, whose metrics differ
from TeX Live's `STIXTwoText` OTF. **A family-name lookup can resolve to either, on a machine that
looks identical from the outside.** That single measurement decided most of what follows.

## Decision

### 1 · Typeface: **Libertinus**, with **Inconsolata** for code

| role | face |
|---|---|
| body, headings, tables | **Libertinus Serif** (Regular / Italic / Bold / BoldItalic / Semibold / SemiboldItalic) |
| title and display | **Libertinus Serif Display** |
| figure labels, axis ticks | **Libertinus Sans** |
| mathematics | **Libertinus Math** (via `unicode-math`) |
| code, file paths, test names | **Inconsolata** (`Inconsolatazi4`, the TeX Live cut with upright quotes) |

**Why Libertinus.**

1. **It has a matched math font.** This corpus is κ, ρ, μΦ(μ/σ) + σφ(μ/σ), tensors, Greek
   throughout. A text face without a metric-compatible math companion means mathematics set in a
   different design — the single most common way a self-typeset paper looks amateur to a referee.
   Libertinus Math is drawn for Libertinus Serif.
2. **Real small caps and oldstyle figures**, which is what lets section heads and the numbers in
   §3's tables sit properly instead of shouting.
3. **SIL Open Font Licence**, which is what makes `P13d` possible at all: the fonts can be
   **vendored into the repository** and redistributed with it. A font we may not carry is a font
   the next machine has to find, and finding is the failure.
4. **It reads as a serious preprint without reading as a template.** Computer Modern says
   "arXiv default"; Libertinus says someone set this.

**Why not the alternatives, recorded so nobody re-derives this.**

- **STIX Two** — the obvious econ/physics choice and genuinely excellent, **rejected on the
  measurement above**: macOS ships a same-named face with different metrics. Choosing it would
  mean the deliverable's single biggest risk is a name collision on the author's own laptop.
- **TeX Gyre Pagella** (Palatino) — beautiful, matched math, GUST licence permits vendoring.
  A legitimate second choice; rejected only because Palatino's larger x-height and wider set
  cost pages on a corpus this long, and because Libertinus's small caps are better.
- **Computer Modern / Latin Modern** — the arXiv default. Rejected: it is the *absence* of a
  typographic decision, and this deliverable exists so Jason can judge how the information
  presents.
- **Times New Roman** — the working-paper reflex. Rejected: no free metric-compatible math
  companion, and it is a system font, i.e. the substitution hazard by construction.

**Why Inconsolata specifically**, and this is corpus-specific rather than taste: the papers cite
test identifiers inline, and the longest is
`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` — **64 characters**. A wide
monospace overflows the measure and forces either a shrunken code size or an ugly break. Inconsolata
is narrow, OFL, already in the TeX tree, and the `zi4` cut has upright quotes, which matters
because those identifiers will be copied out of the PDF and run.

### 2 · Engine: **LuaLaTeX**, TeX Live **2026**, pinned

`unicode-math` + `fontspec` require LuaTeX or XeTeX; LuaLaTeX is chosen for better reproducibility
and for `microtype`'s full feature set. **The TeX Live year is pinned and preflight refuses a
mismatch** — a distribution bump can move metrics, and a warning is something a session skims.
The override (`WT_TEXLIVE_PIN`) exists, is documented, and **invalidates `LAYOUT-MANIFEST.json`
by design**: changing the distribution deliberately means re-measuring the layout, not silencing
the check.

### 3 · Fonts are loaded **by path**, never by family name

```latex
\setmainfont{LibertinusSerif-Regular.otf}[
  Path            = ./fonts/ ,
  ItalicFont      = LibertinusSerif-Italic.otf ,
  BoldFont        = LibertinusSerif-Bold.otf ,
  BoldItalicFont  = LibertinusSerif-BoldItalic.otf ]
```

**This is the whole anti-substitution mechanism in one line of syntax.** A `Path=` load either
finds that exact file or errors out. A family-name load asks the operating system's font
resolver, which is helpful, which is the problem.

### 4 · The fonts are **vendored**

`docs/deliverable/fonts/` carries 15 OTF files (3.7 MB) copied from TeX Live 2026, their SIL Open
Font Licence files alongside, and `FONTS.tsv` recording every file's **sha256**. `preflight.sh`
verifies the checksums, not the names.

**Vendoring was done in `-54`, deliberately ahead of the rest of `P13`, and the distinction is
worth stating because `P13` is otherwise explicitly LAST:** fonts are a **dependency**, not a
layout decision. Dependencies get pinned as early as possible; layout gets designed as late as
possible, after the prose stops moving. Vendoring now also retires the link rot sitting between
this session and whichever one builds the document.

### 5 · What is deliberately NOT decided here

**Every metric.** Point size, leading, measure, margins, spacing above and below display maths,
figure placement — all of it belongs in `RECIPE.md`, **set by the session that builds the document
and measured from the build rather than guessed here.** Recording a leading value in this ADR that
nobody has looked at on a page would be the same error this project has spent fifty sessions
naming: a characterisation standing in for a measurement.

Indicative starting point only, to be confirmed or overruled by the build: 11 pt on US Letter,
generous outer margin, single column, `microtype` on, `booktabs` for tables, `natbib` with a
Chicago author-date style (`P13g`).

## Consequences

- **`P13c` and `P13d` are closed by this ADR's implementation** — `preflight.sh` and the vendored
  fonts exist and are red-proofed by `tests/test_preflight_refuses.py`, which breaks the preflight
  three ways (a modified font, a missing font, an unpinned distribution) and requires a refusal
  each time. A preflight only ever seen to pass is worth nothing.
- **`P13e` becomes meaningful.** Once fonts and engine are pinned by checksum, a page count and
  per-page text hash are a real statement about the document rather than about the machine.
- **Changing the typeface later is not a preference change, it is a re-measurement.** Any edit to
  `FONTS.tsv` invalidates `LAYOUT-MANIFEST.json` and costs Jason the layout pass again. That is
  the cost this ADR exists to make visible before someone pays it casually.
- Repository grows by 3.7 MB of binary. Accepted: it is the price of *"the same font"* being a
  fact rather than a hope.

## Amendment · 2026-08-19 · wealthTensor-93 (`wt173`)

**The decision above stands. Two facts in its §1 rationale did not survive being measured.**

1. **The identifier is 64 characters, not 58.** Corrected in place above. The number was
   never measured; `scripts/wt173_typography_probe.py` now derives it from the four
   manuscripts rather than quoting it, so it cannot drift again.

2. **"Does not overflow the measure" is false, and no font size makes it true.** Measured
   from a real LuaLaTeX build over the vendored fonts: 64 Inconsolata characters occupy the
   width of **74.1 Libertinus body characters**, and that ratio is *identical* at 10, 10.5,
   11 and 12 pt — it is a property of the two typefaces, not of the size. Any measure wide
   enough to hold that identifier inline therefore carries ~74 characters per line, above
   even Bringhurst's outer limit. Setting it as centred display code does not help either:
   measured, a `center` box is still 41.36 pt too wide, because centring narrows nothing.

**What this does NOT change.** Inconsolata remains the right cut for exactly the reasons §1
gives — OFL, already in the tree, upright quotes so identifiers copy out and run, and
narrower than the alternatives. Being *narrower* was the real argument; *narrow enough* was
the overreach. The residue is handled by `RECIPE.md` step 13, which lets long identifiers
break at their underscores with a zero-width break that inserts no character. With that step
in force the probe build produces zero overfull boxes.

**The general shape, for whoever writes the next ADR here:** a rationale that states a
threshold ("does not overflow") rather than a direction ("is narrower than the alternatives")
has made a measurement it did not take. Prefer the direction; leave the threshold to the row
that measures it.
