# RECIPE.md — the paint-by-numbers build of the wealth-tensor deliverable

**P13b.** ORIENT: `docs/adr/ADR-002-typography-and-the-reproducible-build.md` decides the
typeface, the engine and the font-loading discipline. **They are not this document's to
re-open, and they are not the build session's either.** This file supplies the metrics
ADR-002 deliberately left unset — size, leading, measure, margins, display-maths spacing —
and it supplies them as **values measured from a real build** — never as an instruction to
imitate a layout that already exists, and never as a word where a number belongs.

Execute steps 1 to 17 top to bottom.

**The files that execute it**, all in this directory: `preamble.tex` (steps 3-16 as
LaTeX, block by block), `wt175_md2tex.lua` (the pinned converter's behaviour),
`build.sh` (steps 1, 2 and 17, and the refusals), `TABLE-WIDTHS.tsv` (step 14's
per-table measures), `wt176_layout_manifest.py` and `verify-layout.sh` (P13e). Every
one of them cites the step it implements. Every number below appears in
`docs/deliverable/METRICS-MEASURED.json` and is re-derivable by one command, named beside it.
There is no step here that requires you to judge anything.

---

## 0 · What was measured, what was chosen, and the difference

`scripts/wt173_typography_probe.py` performs three real LuaLaTeX builds over real corpus prose
in the real vendored fonts and reads the metrics back out of the engine. Re-run it any time:

```
python3 scripts/wt173_typography_probe.py --measure      # rebuild METRICS-MEASURED.json
python3 scripts/wt173_typography_probe.py --verify       # hold THIS FILE to a fresh build
python3 scripts/wt173_typography_probe.py --postconditions
python3 scripts/wt173_typography_probe.py --print body.chars_per_line
```

**Measured** (an output of the build): every length, every skip, the characters per line, the
margins read back out of `\oddsidemargin` and `\topmargin`, the package versions taken from the
build log, the overfull-box count, and the rendered bibliography entry.

**Chosen** (a design decision, stated so nobody mistakes it for a measurement) — there are
exactly three, and they are the only judgement calls in this document:

1. **The reading band is 62–68 characters per line**, target 65. Bringhurst's satisfactory
   range for a single column is 45–75; this is a tighter reading of it. The measure follows
   from the band; the band does not follow from anything.
2. **Leading is 1.25 × body size, rounded to the nearest 0.5 pt.** Landed on 14.0 pt.
3. **The heading scale is a 1.18 ratio on the body size**, each step rounded to 0.5 pt.

Everything else in this file is arithmetic on a measurement.

### The one place the corpus overruled the plan

ADR-002 §1 chose Inconsolata so the corpus's longest inline test identifier "does not overflow
the measure", and put that identifier at **58** characters. **The build says both halves are
wrong, and the second one cannot be fixed by choosing differently.**

- The identifier is **64** characters, not 58 (`test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`).
- 64 Inconsolata characters occupy the width of **74.1** Libertinus body characters — and that
  number is **identical at 10, 10.5, 11 and 12 pt**, because it is a ratio between two
  typefaces and not a function of size. So *no* body size lets that identifier sit inline
  inside a comfortable measure. The conflict is scale-invariant.
- At the measure this recipe sets, **55** characters is the most that fits inline. The corpus's
  longest is **64**. Step 13 is the resolution, and it is a break rule rather than a size
  change, because ADR-002 chose this cut so identifiers can be copied out of the PDF and run.

---

## The recipe

1. **Refuse to build on the wrong dependencies.** Run `docs/deliverable/preflight.sh` and stop
   unless it exits 0. It verifies the 15 vendored fonts by **sha256**, not by name, and pins
   TeX Live. There is no fallback path and you are not to add one.

2. **Engine: `lualatex`, TeX Live 2026.** Not `xelatex`, not `pdflatex` — `unicode-math` and
   the `Path=` font loading below require LuaTeX or XeTeX, and `microtype`'s full feature set
   requires LuaTeX. Build with `latexmk -lualatex`.

   **Converter: `pandoc` 3.9.0.2, through `wt175_md2tex.lua`.** The manuscripts are
   Markdown and this recipe is LaTeX, so something converts them, and *that* is where the
   layout silently changes -- a different pandoc can emit a different table environment or
   a different escape and move every page boundary after it. `build.sh` refuses on a
   version mismatch exactly as it refuses on the wrong TeX Live year. The filter pins the
   three behaviours the corpus depends on: inline code spans become `\url{...}` and never
   `\texttt{...}` (step 13); the seven characters no vendored face carries are routed to
   mathematics or to the vendored mark font (step 6a); and every table is given its own
   measure (step 14).

3. **Document class:** `\documentclass[11pt,letterpaper]{article}`, single column.

4. **Body font size is 11.0 pt.** Set it explicitly with `\fontsize{11}{14}\selectfont` rather
   than relying on the class option, so the leading in step 5 is not the class's guess.

5. **Leading is 14.0 pt** (a ratio of 1.2727 on the measured body size). Every line in the text
   block sits exactly 14.0 pt below the last.

6. **Load the fonts BY PATH, never by family name.** This is the whole anti-substitution
   mechanism; a `Path=` load either finds that exact file or errors out, while a family-name
   load asks the operating system, which is helpful, which is the problem.

   ```latex
   \usepackage{fontspec}
   \usepackage{unicode-math}
   \setmainfont{LibertinusSerif-Regular.otf}[
     Path            = ./fonts/ ,
     ItalicFont      = LibertinusSerif-Italic.otf ,
     BoldFont        = LibertinusSerif-Bold.otf ,
     BoldItalicFont  = LibertinusSerif-BoldItalic.otf ]
   \setsansfont{LibertinusSans-Regular.otf}[
     Path            = ./fonts/ ,
     ItalicFont      = LibertinusSans-Italic.otf ,
     BoldFont        = LibertinusSans-Bold.otf ]
   \setmonofont{Inconsolatazi4-Regular.otf}[
     Path            = ./fonts/ ,
     BoldFont        = Inconsolatazi4-Bold.otf ,
     Scale           = MatchLowercase ]
   \setmathfont{LibertinusMath-Regular.otf}[ Path = ./fonts/ ]
   ```

   **6a. Seven characters in the corpus are carried by no Libertinus or Inconsolata
   face, and LaTeX sets nothing for an absent glyph.** It reports `Missing character:` in
   the log and exits 0, so the loss is invisible. Measured over the four manuscripts, the
   corpus uses 75 distinct non-ASCII characters and these seven are not in the faces that
   would be asked to set them:

   | character | count | where it goes |
   |---|---|---|
   | U+2299 `⊙` | 12 | mathematics: `\odot` out of LibertinusMath |
   | U+1D4A9 `𝒩` | 1 | mathematics: `\mathcal{N}` out of LibertinusMath |
   | U+1D62 `ᵢ` | 40 | mathematics: a subscript |
   | U+2713 `✓` | 95 | the vendored mark font |
   | U+29D7 `⧗` | 17 | the vendored mark font |
   | U+270E `✎` | 13 | the vendored mark font |
   | U+26A0 `⚠` | 1 | the vendored mark font |

   The last four are the citation-verification notation the References sections define in
   their own prose, so `FreeSerif.otf` is vendored into `./fonts/` and checksummed in
   `FONTS.tsv` under the same discipline as the other fifteen -- a sixteenth row, not a
   sixteenth rule. Body text never selects it; only `\wtmark` does.

   `ᵢ` is the one to remember. It is present in LibertinusSerif-Regular and -Bold and
   **absent from -Italic and -BoldItalic**, and the corpus writes it as an index on an
   emphasised variable (`*mᵢ*`) -- which is the italic case. A coverage probe run against
   the default face reports it present. **A glyph probe must test every face the document
   can select, not the face it starts in**: the first probe run at wealthTensor-94 tested
   one face and found six; the true number is seven.

7. **The measure is 289.08 pt** (4.0 in). Measured on real corpus prose, that measure carries
   **65.43** characters per line — inside the 62–68 band of §0.

8. **Page geometry.** US Letter, 614.295 pt × 794.97 pt. Left and right margins are
   **162.6075 pt** each, the top margin is **72.27 pt**, the bottom margin is **92.7 pt**. The
   bottom exceeds the top on purpose: the block sits optically centred rather than
   geometrically centred.

   ```latex
   \usepackage[letterpaper,
     textwidth=289.08pt, textheight=630.0pt,
     left=162.6075pt, top=72.27pt, heightrounded=false]{geometry}
   ```

9. **The text height is 630.0 pt, which is exactly 45 lines of 14.0 pt leading.** Do not round
   this to a convenient inch value. The whole point is that the block closes flush on the
   baseline grid, so facing pages align and a display equation does not push the last line off
   the grid for the rest of the page.

10. **`microtype` on**, default settings, loaded after the fonts. This is what makes the
    measured characters-per-line in step 7 reproducible; without it the paragraphs break
    differently and the layout hashes in `LAYOUT-MANIFEST.json` will not reproduce.

11. **Headings**, on the 1.18 scale of §0. Libertinus Serif Display for the title, Libertinus
    Serif Bold for the rest. Title **17.5** pt on 20.0 pt; section **13.0** pt on 15.0 pt;
    subsection 12.0 pt on 14.0 pt; subsubsection 11.0 pt on 14.0 pt.

12. **Display mathematics.** Set these explicitly rather than inheriting them, so that changing
    the document class later cannot move them silently:

    ```latex
    \abovedisplayskip      = 11.0pt plus 3.0pt minus 6.0pt
    \belowdisplayskip      = 11.0pt plus 3.0pt minus 6.0pt
    \abovedisplayshortskip = 0.0pt plus 3.0pt
    \belowdisplayshortskip = 6.5pt plus 3.5pt minus 3.0pt
    ```

13. **Inline code identifiers.** At this measure an inline monospace run fits **55** characters.
    The corpus's longest is **64**. Load `url` and set identifiers with `\url{...}`:

    ```latex
    \usepackage{url}
    \urlstyle{tt}
    \def\UrlBreaks{\do\_}
    ```

    This breaks a long identifier at its underscores and **inserts no character**, so what a
    reader copies out of the PDF is still what runs. Do **not** solve this by centring the
    identifier (measured: a `center` box is still 41.36 pt too wide — centring narrows
    nothing), and do **not** solve it by shrinking the code font, which defeats the reason
    ADR-002 chose this cut. With this step in force the probe build produces **zero** overfull
    boxes.

    **Amended at wealthTensor-94, from the real build.** `\do\_` alone was written for
    identifiers, and not every code span is one. The corpus also carries repository URLs
    (`https://github.com/jasoncbraatz/wealth-tensor`, 47 characters with no underscore
    anywhere) and bare 64-character git SHAs with no break opportunity of any kind; they
    overflowed the measure by 30.76pt and 62.81pt. It also carries 18 spans that contain
    whitespace, and "it can break at its spaces" is not enough -- one holds a
    44-character path token, and `\texttt` cannot break inside a token, which cost another
    88.98pt. So: `xurl` is loaded, adding break opportunities **without inserting a
    character**, which is the property this step actually asks for and the reason pandoc's
    own generated preamble reaches for the same package; and a span containing whitespace
    has each of its tokens set through `\url` inside a `\ttfamily` group, so the same
    guarantee covers command lines. The general shape, and it is the ADR-002 shape with
    the object changed: **a rule written for one kind of object silently claims the kinds
    it never met.**

14. **Tables:** `booktabs` only — `\toprule`, `\midrule`, `\bottomrule`. No vertical rules and
    no `\hline`. Table and figure spacing is the class default, confirmed by the build:
    `\floatsep` 12.0pt plus 2.0pt minus 2.0pt, `\textfloatsep` 20.0pt plus 2.0pt minus 4.0pt,
    `\intextsep` 12.0pt plus 2.0pt minus 2.0pt, `\abovecaptionskip` 10.0pt,
    `\belowcaptionskip` 0.0pt.

    **Each table gets its own measure, and 23 of the 30 do not need one.** A nine-column
    table is not a four-inch object: six tables overflow the body measure, the worst by
    143.65pt. Step 8 leaves 162.6075pt of margin on each side for them not to have to, so
    a table wider than the measure is centred on the page and grows symmetrically into
    that margin -- the **body** measure, which every metric in this file is about, never
    moves. Tabular matter is set at 10.0pt on 12.0pt; step 13's prohibition on shrinking
    type is about the code font, where a reader copies identifiers out of the PDF.

    A **uniform** wide measure is the wrong repair and the rendered page said so: pandoc
    gives any table with a long cell a set of `p{}` columns that are fractions of the
    table's measure, so one width for all of them stretches a two-column table to the same
    width as a nine-column one and opens a canyon down its middle. Each table's measure is
    instead derived from what the engine reported about that table (`./build.sh --retune`,
    which iterates to a fixed point because widening a table rewraps its columns) and
    **committed to `TABLE-WIDTHS.tsv`**, one row per table, carrying the deficit in points
    that forced it. An ordinary build, and every `verify-layout.sh`, is then a single
    deterministic pass over a reviewed file rather than a re-derivation.

15. **Figure placement.** Every figure is `[tb]` — top or bottom of a page, never `[h]` and
    never `[H]`. A figure locked in place mid-column breaks the baseline grid of step 9 and
    moves the page boundaries that `LAYOUT-MANIFEST.json` hashes. Figures are produced by a
    committed script from committed numbers and listed in `FIGURES.tsv` (that is P13f's row,
    not this one, but the placement rule belongs here).

16. **References:** `natbib` in author-date mode over `chicago.bst`.

    ```latex
    \usepackage[authoryear,round]{natbib}
    \bibliographystyle{chicago}
    ```

    This combination was **built**, not assumed: `bibtex` over `chicago.bst` emits
    natbib-compatible `\bibitem[\protect\citeauthoryear{...}]` entries and the pair compiles
    clean. Whether the result satisfies economics house style is **P13g**, which is
    pending-human and is explicitly not closed by the session that builds the layout.

    **Measured at wealthTensor-94: `bibtex` is a no-op on this corpus.** The four
    manuscripts contain zero `\cite` commands and the repository contains no `.bib` file --
    every paper carries a hand-written References section. natbib is loaded exactly as
    specified above and the pair compiles clean; there is simply nothing for `bibtex` to
    process. `LAYOUT-MANIFEST.json` records this as `bibtex.ran: false` rather than
    passing over it, so the day a `\cite` appears a successor knows the leg has never been
    exercised.

17. **Build and verify.** `latexmk -lualatex` twice for cross-references, then `bibtex`, then
    twice more. Then run `python3 scripts/wt173_typography_probe.py --verify` and require exit
    0: it re-measures from a fresh build and holds every value in this file to it.

    `./build.sh` runs all of that and **refuses on three things the toolchain reports at a
    severity below the one that stops it**:

    1. **`Overfull \hbox`** -- text physically outside the measure. A warning.
    2. **`Missing character:`** -- an absent glyph, for which LaTeX sets nothing. A warning.
       126 marks would have vanished from a build that exited 0.
    3. **Ink outside the paper.** *Zero overfull boxes does not mean the document fits on
       the page.* An overfull box is reported when a line exceeds `\hsize`, so any
       construction that WIDENS `\hsize` -- which is exactly what step 14's per-table
       measure does -- silences the warning whether or not the result is still on the
       sheet. An early cut of that environment reported zero overfull boxes while running
       every wide table off the right edge of the paper. `build.sh` therefore measures the
       marked extent of every page with ghostscript's bbox device and requires 18bp of
       clearance on all four edges. **A check that cannot see a failure reports zero of
       them, and zero reads exactly like absence.**

---

## The measured values

Machine-written by `--emit-block`; held to a fresh build by `--verify`. Column three is the
command that prints that value from a fresh build, so every number here carries its own
provenance. Do not hand-edit — edit the build and re-emit.

```wt173-measured
# key	value	the command that prints this value from a fresh build
engine.engine	lualatex	python3 scripts/wt173_typography_probe.py --print engine.engine
engine.texlive_year	2026	python3 scripts/wt173_typography_probe.py --print engine.texlive_year
body.size_pt	11.0	python3 scripts/wt173_typography_probe.py --print body.size_pt
body.leading_pt	14.0	python3 scripts/wt173_typography_probe.py --print body.leading_pt
body.leading_ratio	1.2727	python3 scripts/wt173_typography_probe.py --print body.leading_ratio
body.measure_pt	289.08	python3 scripts/wt173_typography_probe.py --print body.measure_pt
body.measure_in	4.0	python3 scripts/wt173_typography_probe.py --print body.measure_in
body.chars_per_line	65.43	python3 scripts/wt173_typography_probe.py --print body.chars_per_line
body.xheight_pt	4.741	python3 scripts/wt173_typography_probe.py --print body.xheight_pt
body.capheight_pt	7.117	python3 scripts/wt173_typography_probe.py --print body.capheight_pt
body.alphabet_pt	133.98	python3 scripts/wt173_typography_probe.py --print body.alphabet_pt
page.paperwidth_pt	614.295	python3 scripts/wt173_typography_probe.py --print page.paperwidth_pt
page.paperheight_pt	794.97	python3 scripts/wt173_typography_probe.py --print page.paperheight_pt
page.textwidth_pt	289.08	python3 scripts/wt173_typography_probe.py --print page.textwidth_pt
page.textheight_pt	630.0	python3 scripts/wt173_typography_probe.py --print page.textheight_pt
page.margin_left_pt	162.6075	python3 scripts/wt173_typography_probe.py --print page.margin_left_pt
page.margin_right_pt	162.6075	python3 scripts/wt173_typography_probe.py --print page.margin_right_pt
page.margin_top_pt	72.27	python3 scripts/wt173_typography_probe.py --print page.margin_top_pt
page.margin_bottom_pt	92.7	python3 scripts/wt173_typography_probe.py --print page.margin_bottom_pt
page.baseline_grid_lines	45	python3 scripts/wt173_typography_probe.py --print page.baseline_grid_lines
page.probe_overfull_hboxes	0	python3 scripts/wt173_typography_probe.py --print page.probe_overfull_hboxes
page.margin_left_measured_pt	162.6075	python3 scripts/wt173_typography_probe.py --print page.margin_left_measured_pt
page.margin_top_measured_pt	72.27	python3 scripts/wt173_typography_probe.py --print page.margin_top_measured_pt
page.margin_bottom_measured_pt	92.7	python3 scripts/wt173_typography_probe.py --print page.margin_bottom_measured_pt
display_maths.abovedisplayskip	11.0pt plus 3.0pt minus 6.0pt	python3 scripts/wt173_typography_probe.py --print display_maths.abovedisplayskip
display_maths.belowdisplayskip	11.0pt plus 3.0pt minus 6.0pt	python3 scripts/wt173_typography_probe.py --print display_maths.belowdisplayskip
display_maths.abovedisplayshortskip	0.0pt plus 3.0pt	python3 scripts/wt173_typography_probe.py --print display_maths.abovedisplayshortskip
display_maths.belowdisplayshortskip	6.5pt plus 3.5pt minus 3.0pt	python3 scripts/wt173_typography_probe.py --print display_maths.belowdisplayshortskip
monospace.advance_pt	5.1631	python3 scripts/wt173_typography_probe.py --print monospace.advance_pt
monospace.max_inline_identifier_chars	55	python3 scripts/wt173_typography_probe.py --print monospace.max_inline_identifier_chars
monospace.corpus_longest_identifier_chars	64	python3 scripts/wt173_typography_probe.py --print monospace.corpus_longest_identifier_chars
monospace.longest_fits_inline	False	python3 scripts/wt173_typography_probe.py --print monospace.longest_fits_inline
headings.title.size_pt	17.5	python3 scripts/wt173_typography_probe.py --print headings.title.size_pt
headings.title.leading_pt	20.0	python3 scripts/wt173_typography_probe.py --print headings.title.leading_pt
headings.section.size_pt	13.0	python3 scripts/wt173_typography_probe.py --print headings.section.size_pt
headings.section.leading_pt	15.0	python3 scripts/wt173_typography_probe.py --print headings.section.leading_pt
headings.subsection.size_pt	12.0	python3 scripts/wt173_typography_probe.py --print headings.subsection.size_pt
headings.subsection.leading_pt	14.0	python3 scripts/wt173_typography_probe.py --print headings.subsection.leading_pt
headings.subsubsection.size_pt	11.0	python3 scripts/wt173_typography_probe.py --print headings.subsubsection.size_pt
headings.subsubsection.leading_pt	14.0	python3 scripts/wt173_typography_probe.py --print headings.subsubsection.leading_pt
vertical_spacing.parindent	17.0pt	python3 scripts/wt173_typography_probe.py --print vertical_spacing.parindent
vertical_spacing.parskip	0.0pt plus 1.0pt	python3 scripts/wt173_typography_probe.py --print vertical_spacing.parskip
vertical_spacing.floatsep	12.0pt plus 2.0pt minus 2.0pt	python3 scripts/wt173_typography_probe.py --print vertical_spacing.floatsep
vertical_spacing.textfloatsep	20.0pt plus 2.0pt minus 4.0pt	python3 scripts/wt173_typography_probe.py --print vertical_spacing.textfloatsep
vertical_spacing.intextsep	12.0pt plus 2.0pt minus 2.0pt	python3 scripts/wt173_typography_probe.py --print vertical_spacing.intextsep
vertical_spacing.abovecaptionskip	10.0pt	python3 scripts/wt173_typography_probe.py --print vertical_spacing.abovecaptionskip
vertical_spacing.belowcaptionskip	0.0pt	python3 scripts/wt173_typography_probe.py --print vertical_spacing.belowcaptionskip
references.bst	chicago.bst	python3 scripts/wt173_typography_probe.py --print references.bst
references.package	natbib[authoryear,round]	python3 scripts/wt173_typography_probe.py --print references.package
references.natbib_bibitem_format_ok	True	python3 scripts/wt173_typography_probe.py --print references.natbib_bibitem_format_ok
```

---

## What this recipe does not decide

- **P13g** — whether the reference formatting and page furniture read as economics house style.
  A human call, deliberately not automated, and not the layout session's to close.
- **P13a / P13e** — producing the PDF and the layout manifest. This file is the recipe; those
  rows are the capture and its reproducibility proof.
- **The page count of the real corpus.** The probe is 2 pages of sample matter. Nothing here
  claims what the four papers come to.
