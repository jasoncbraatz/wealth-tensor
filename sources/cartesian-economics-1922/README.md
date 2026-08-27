# Soddy, *Cartesian Economics* (Hendersons, London, 1922) — reset

A complete reset of Soddy's 1922 pamphlet, recovered from an OCR'd page scan
and typeset so that it can be read — and cited — as a book.

## What's here

| file | what it is |
|---|---|
| `Soddy-Cartesian-Economics-1922.pdf` | the book, 35pp, 6×9in |
| `cartesian.tex` | the source; build with `xelatex` twice |
| `proof.py` | word-level collation of the PDF against the OCR, page by page |
| `ocr-source/` | the 48 raw OCR page files exactly as received |

## Provenance

The scan is the **Harvard College Library (Widener)** copy, barcode
`32044010374809`, from the bequest of George Hayward, M.D. (Boston, class of
1809), accessioned 16 July 1925 — the bookplate, the Harvard accession stamp
and a Widener due-date slip are all in the scan. Worth knowing before citing
it as a British Library holding.

Files `00000001`–`00000009` are a second OCR pass over the same front matter
and pp. 3–5 as `00000010`–`00000017`; the two passes disagree in their errors,
which made them useful for cross-checking. The canonical run is
`00000010`–`00000044` = front matter + pp. 3–32.

## Editorial decisions

- **Pagination is the 1922 pagination.** Folios 3–32 break where the original
  broke, so a page citation taken from this PDF answers to the printed book.
- Silent repairs: word-endings lost at the scanned right margin (p. 6 and p. 8
  were badly clipped), compositor's line-break hyphens, inverted commas,
  and obvious OCR garbage (`hebula`→nebula, `whicu`→which, `himan`→human).
- Decimals set with the mid-point (`10·5`, `12·5`, `5·5`) as a British house of
  the period would have set them; the OCR rendered the same glyph three
  different ways.
- **Left as found, uncertain:** `devitiation` (p. 12); the figure `23 million
  tons` (p. 30).
- The two notes on p. 13 are gathered under one mark — the page carries no
  second reference.
- Set in MFB Oldstyle, a digitisation of Century Oldstyle (M. F. Benton, ATF
  1909).

## Content note

Soddy's language is 1921's and is reproduced unaltered, including the
antisemitic idiom on p. 25 and the reference to racial stock on p. 12.

## Verifying the text

    python3 proof.py

Compares every page of the PDF against its OCR source after normalising away
hyphenation, quotes, running heads and folios. All 30 text pages currently
match; every reported divergence is a deliberate repair listed above.
