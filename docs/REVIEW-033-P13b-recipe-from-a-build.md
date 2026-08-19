# REVIEW-033 · P13b — writing a recipe from a build instead of from taste

*wealthTensor-93 · 2026-08-19 · `wt173` · closes P13b*

## 1 · The verdict, in one sentence someone can mark right or wrong

Every metric in `docs/deliverable/RECIPE.md` is an output of a real LuaLaTeX build over the
vendored fonts — 50 values re-derived on demand by `wt173 --verify`, which also holds the 15
load-bearing ones to the numbered prose — and the one claim the build **refuted** is ADR-002's
own: that Inconsolata is narrow enough to keep the corpus's longest test identifier inline.
That identifier is **64** characters, not the 58 the ADR states, and it occupies the width of
**74.1** body characters at 10, 10.5, 11 *and* 12 pt, so it does not fit a readable measure at
any size this document could have chosen.

## 2 · Why the row could not be discharged by writing carefully

P13b's text is unusually specific about the failure it fears: metrics "measured from the build
rather than guessed". The trap the inherited brief named is real and it is subtle — there was
no build, so *every* number in a recipe written today would have been a preference wearing a
unit. The recipe would have looked identical. It would have said 11 pt and 4.5 in and
"Inconsolata, which is narrow enough", and it would have been wrong in exactly one place, and
that place would have been discovered by whoever first set a 64-character identifier and
watched it walk into the margin.

So the order matters and it is recorded in the commit graph rather than asserted here:
`a177773` is the instrument and the measurements **alone**, and at that commit P13b is RED
because `RECIPE.md` does not exist. The numbers became a git object before the document that
quotes them.

## 3 · The finding: a conflict no font size can resolve

ADR-002 §1 justifies Inconsolata partly on a corpus-specific ground — the papers cite test
identifiers inline, the longest is 58 characters, and a wide monospace would overflow the
measure. Measured:

| body size | mono advance | serif average | 64 mono characters, in body-character widths |
|---|---|---|---|
| 10.0 pt | 5.179 pt | 4.053 pt | **74.1** |
| 10.5 pt | 5.438 pt | 4.256 pt | **74.1** |
| 11.0 pt | 5.697 pt | 4.458 pt | **74.1** |
| 12.0 pt | 6.215 pt | 4.864 pt | **74.1** |

The column does not move, because it is a ratio between two typefaces and not a function of
size. **Any measure wide enough to hold that identifier inline carries about 74 characters per
line at every size** — above Bringhurst's outer limit of 75 once the identifier is not alone on
the line, and far outside the 62–68 band the recipe set before measuring anything.

Two ways out were tried and one was measured to fail:

- **Set it as centred display code.** Measured: the `center` box is still 41.36 pt too wide.
  Centring narrows nothing. This is worth recording because it is the intuitive fix and it
  produces a document that looks deliberate while still overflowing.
- **Shrink the code font until it fits.** Rejected on ADR-002's own ground: the `zi4` cut was
  chosen so identifiers can be copied out of the PDF and run, and a size chosen to defeat a
  measure is a size nobody read.

The resolution is step 13 — `url` with `\UrlBreaks` set to the underscore, which breaks a long
identifier at its underscores and **inserts no character**, so the copied string still runs.
With that step in force the probe build reports **zero** overfull boxes, which is the whole
claim, measured rather than promised.

## 4 · Two instrument failures, both the -92(iv) shape

`-92` left the rule: *before asserting an instrument's output is unchanged by your edit, assert
that the instrument reads the file you edited.* Both of this pass's mistakes are that rule with
the object swapped — before believing a number, assert the instrument can produce it.

- **`\prevgraf` returned 0, thirty-six times, twice.** First on the page, where the output
  routine fires mid-paragraph and resets it; then inside a `\vbox`, where under LuaTeX it never
  gets set at all. The first failure produced a clean, plausible, entirely fabricated set of
  line counts. Nothing flagged it: zero is a number, and `chars / (lines - 0.5)` happily
  divides by −0.5. Line counts now come from box geometry, and `choose()` **refuses** when the
  height-to-leading division is not integral — an instrument that cannot produce an integer
  line count is not measuring lines.
- **The margins were the values `geometry` was handed, echoed back as if measured.** Three of
  the four numbers in the recipe's most physical-sounding step were an input dressed as an
  output. They are now read out of `\oddsidemargin` and `\topmargin`, and post-condition P8
  demands the asked-for and the read-back agree.

## 5 · What the instruments cannot see, stated so nobody assumes otherwise

- **`--verify` proves the recipe matches a build; it cannot prove the build is beautiful.**
  Nothing here is evidence about how the corpus *looks*. P13g is pending-human for that reason
  and this pass did not touch it.
- **The characters-per-line figure carries about half a line of bias.** It comes from one
  ~138-line paragraph with a partial last line; `choose()` subtracts 0.5 lines for it. At 138
  lines that is under half a percent, and it is a bias, not noise — the same direction every run.
- **The probe is 2 pages of sample matter.** It says nothing about the page count of the four
  papers, which is P13a/P13e's business.
- **The three design choices are choices.** The 62–68 band, the 1.25 leading ratio and the 1.18
  heading scale are stated as such in RECIPE.md §0. Everything downstream is arithmetic on a
  measurement; those three are not, and calling them measured would be the exact error this row
  exists to prevent.

## 6 · Falsifiers

1. Change `body.size_pt` in the recipe's block to `12.0` — `wt173 --verify` must exit 1 naming
   that key. (Post-condition N1.)
2. Delete the ```wt173-measured block — `--verify` must refuse rather than pass vacuously. (N2.)
3. Change a leading in the numbered prose while leaving the block correct — must be caught. (N3.)
4. Substitute any vendored font — `preflight.sh` must refuse before a build happens at all.
5. Re-run `--measure` on a machine with TeX Live ≠ 2026 — preflight must refuse, and the
   committed metrics must be treated as invalid rather than reconciled.
6. Set a 64-character identifier inline without step 13 — the build must report an overfull box.
7. Replace the sweep's real corpus prose with lorem ipsum — `body.chars_per_line` must move,
   because the figure is a property of this corpus's character mix and not of the font alone.
