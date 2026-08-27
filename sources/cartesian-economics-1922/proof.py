#!/usr/bin/env python3
"""Word-level collation of the typeset PDF against the OCR source.

Compares each original page (OCR files 00000015..00000044 -> pages 3..32)
with the corresponding page of cartesian.pdf, after normalising away
hyphenation, quote styles, running heads and folios.  Reports words that
appear in one and not the other, so that dropped or invented text shows up.
"""
import re, subprocess, sys, difflib, pathlib

HERE = pathlib.Path(__file__).parent
OCR = HERE / "ocr-source"
PDF = HERE / "cartesian.pdf"

# OCR file N  ->  original page N-12  (file 15 == page 3 ... file 44 == page 32)
PAGES = [(n, n - 12) for n in range(15, 45)]
# PDF sheet for original page p: 4 front-matter sheets precede page 3
PDF_SHEET = lambda p: p + 2


def norm(text):
    t = text
    t = t.replace("—", " ").replace("–", " ").replace("---", " ")
    t = re.sub(r"[‘’“”`'\"]", "", t)
    t = t.replace("·", ".").replace("­", "")
    # join words broken across a line by a hyphen
    t = re.sub(r"-\s*\n\s*", "", t)
    t = t.replace("\n", " ")
    t = t.lower()
    t = re.sub(r"[^a-z0-9£]+", " ", t)
    words = t.split()
    # drop running heads / folios
    out = []
    for w in words:
        if w in ("cartesian", "economics") and len(out) < 3:
            continue
        out.append(w)
    return out


def pdf_page_text(n):
    return subprocess.run(
        ["pdftotext", "-f", str(n), "-l", str(n), "-layout", str(PDF), "-"],
        capture_output=True, text=True, check=True).stdout


bad = 0
for fnum, page in PAGES:
    src = (OCR / f"{fnum:08d}.txt").read_text(encoding="utf-8", errors="replace")
    a = norm(src)
    b = norm(pdf_page_text(PDF_SHEET(page)))
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    ratio = sm.ratio()
    dropped, added = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("delete", "replace"):
            dropped += a[i1:i2]
        if tag in ("insert", "replace"):
            added += b[j1:j2]
    flag = "ok " if ratio > 0.955 else "SEE"
    if ratio <= 0.955:
        bad += 1
    print(f"{flag} p.{page:<3} match={ratio:6.3f}  ocr={len(a):4d} set={len(b):4d}")
    if ratio <= 0.985:
        if dropped:
            print(f"      only in OCR : {' '.join(dropped[:40])}")
        if added:
            print(f"      only in set : {' '.join(added[:40])}")
print(f"\npages below threshold: {bad}")
