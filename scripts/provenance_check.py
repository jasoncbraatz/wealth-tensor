#!/usr/bin/env python3
"""provenance_check — a filename is not a provenance.

WHY THIS EXISTS (session wealthTensor-10, 2026-08-11)
-----------------------------------------------------
Two PDFs arrived named `JST_10.2307_2491294.pdf` and `JST_10.2307_2491496.pdf`.
The names assert JSTOR. Both were in fact macOS Preview re-exports of shadow-library
copies -- and each one carried, in its own PDF `Title` metadata, the md5 of the file it
had been exported from:

    Title:    2491294 -- 55f2f577f8f0263e89f8b8ce35ac129a -- Anna's Archive
    Creator:  Preview
    Producer: macOS Version 26.1 Quartz PDFContext

Nobody did anything careless. Two documents were open in Preview; the wrong window got
exported; the metadata rode along silently. The rename was an act of tidiness that
happened to manufacture a false claim about origin.

This is the phantom tag in a fifth costume (see METHOD-001 §5):
    1. a fielder credited with an out he never made
    2. a journal credited with words it never printed
    3. prose credited with rigour it never performed
    4. an abstract credited to a paper that never had one
    5. A FILE CREDITED WITH A PROVENANCE IT DOES NOT HAVE

And it is the argument for REFERENCE-POLICY pass 3 in a single screenshot.
Passes 1, 2, 4 and 5 all *pass* on these files: the work exists (1), the reference does
work (2), it is the published article's own scan so there is no version question (4),
and it was genuinely read at source (5). **Only the provenance pass catches it, and only
if you look inside the file rather than at its name.**

WHAT IT CHECKS
--------------
  A. RE-EXPORT      Producer/Creator indicates the file was regenerated locally
                    (Preview, Quartz, print-to-PDF). It is therefore NOT the object any
                    repository delivered, whatever it is named.
  B. STALE TITLE    PDF `Title` metadata disagrees with the filename -- the single most
                    reliable tell, because re-exporters copy Title and not filename.
  C. SHADOW MARKER  Title/Subject/Keywords name a shadow library.
  D. BARE MD5       Title contains a 32-hex string, which is a content-addressed
                    filename that leaked into metadata. Always worth reading.

SEVERITY, and why it is tiered (added within the hour of writing this, see below)
----------------------------------------------------------------------------------
The first LEGITIMATE file this script ever saw, it flagged. Gorton & Ordoñez (2014),
downloaded from Ordoñez's own university page, carrying the AER's own typesetting and
correct folios 343-378, tripped RE-EXPORT -- because the *author* had made the PDF on his
own Mac in 2011. That is not a defect; that is how authors self-archive.

**A smoke alarm that goes off when you make toast gets unplugged**, and an unplugged guard
is worse than no guard, because it is also an excuse. So:

    HARD signal -- one is enough to FLAG:
        shadow marker in metadata
        embedded md5 that does not match the file's own bytes
    SOFT signal -- one is a NOTE, two or more together FLAG:
        locally regenerated (Preview / Quartz / print-to-PDF)
        filename and embedded Title share no tokens

The JST_ re-exports that prompted this script carry TWO hard signals each and still flag.
Ordoñez's honest self-archived copy carries one soft signal and is now a note.

EXIT CODES (load-bearing, per WT-053)
    0  every file clean or note-only
    1  at least one file FLAGGED
    2  usage error / a file could not be read

USAGE
    python3 scripts/provenance_check.py FILE.pdf [FILE.pdf ...]
    python3 scripts/provenance_check.py ~/Desktop/downloads/*.pdf

This is a SMOKE ALARM, not a judge. A flag means "look at this before you cite it,"
never "this is illegitimate." A clean run means the metadata raised nothing -- it is not
a certificate of provenance, because no metadata can be one.
"""
from __future__ import annotations

import hashlib
import pathlib
import re
import shutil
import subprocess
import sys

RE_EXPORTERS = ("quartz", "preview", "print to pdf", "printtopdf", "microsoft: print")
SHADOW_MARKERS = ("anna's archive", "anna’s archive", "annas archive",
                  "library genesis", "libgen", "sci-hub", "scihub", "z-library", "zlibrary")
MD5_IN_TEXT = re.compile(r"\b[0-9a-f]{32}\b")


def pdfinfo(path: pathlib.Path) -> dict:
    exe = shutil.which("pdfinfo") or "/opt/homebrew/bin/pdfinfo"
    out = subprocess.run([exe, str(path)], capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip() or "pdfinfo failed")
    fields = {}
    for line in out.stdout.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fields[k.strip()] = v.strip()
    return fields


def norm(s: str) -> set:
    """Word-ish tokens, lowercased, for a loose filename/title comparison.

    Length > 2, not > 3: the first legitimate file this saw was renamed
    `..._AER.pdf` against a Title of "Collateral Crises Final AER", and a
    four-character floor threw away the one token that matched.
    """
    return {t for t in re.split(r"[^a-z0-9]+", s.lower()) if len(t) > 2}


def check(path: pathlib.Path) -> tuple:
    """Return (hard, soft) — lists of signal strings. Caller decides severity."""
    info = pdfinfo(path)
    title = info.get("Title", "")
    producer = info.get("Producer", "")
    creator = info.get("Creator", "")
    blob = " ".join((title, producer, creator, info.get("Subject", ""),
                     info.get("Keywords", ""))).lower()
    hard, soft = [], []

    if any(m in producer.lower() or m in creator.lower() for m in RE_EXPORTERS):
        soft.append(
            f"RE-EXPORT · regenerated locally ({creator or '?'} / {producer or '?'}). "
            f"Not the file any repository served — though an author self-archiving his "
            f"own paper produces exactly this signature."
        )

    for m in SHADOW_MARKERS:
        if m in blob:
            hard.append(f"SHADOW MARKER · metadata names a shadow library ({m!r}).")
            break

    if title:
        stem_tokens, title_tokens = norm(path.stem), norm(title)
        if stem_tokens and title_tokens and not (stem_tokens & title_tokens):
            soft.append(
                f"STALE TITLE · filename and embedded Title share no tokens.\n"
                f"           filename: {path.name}\n"
                f"           Title:    {title}"
            )

    for h in MD5_IN_TEXT.findall(title.lower()):
        actual = hashlib.md5(path.read_bytes()).hexdigest()
        if h == actual:
            soft.append(f"BARE MD5 · Title embeds this file's own hash {h}. Harmless, but "
                        f"it means the name came from a content-addressed store.")
        else:
            hard.append(
                f"BARE MD5MISMATCH · Title embeds hash {h}, but this file hashes to "
                f"{actual}.\n           **The file is carrying a hash of its ancestor.** "
                f"It was re-exported from something else."
            )

    return hard, soft


def main(argv: list) -> int:
    paths = [pathlib.Path(a).expanduser() for a in argv]
    if not paths:
        print(__doc__.split("USAGE")[1].strip(), file=sys.stderr)
        return 2

    worst, unread = 0, 0
    for p in paths:
        if not p.is_file():
            print(f"?? {p} — not a file"); unread += 1; continue
        try:
            hard, soft = check(p)
        except Exception as exc:                                  # noqa: BLE001
            print(f"?? {p.name} — could not read: {exc}"); unread += 1; continue

        flagged = bool(hard) or len(soft) >= 2
        if flagged:
            worst = 1
            print(f"\n⚑ FLAGGED  {p.name}")
        elif soft:
            print(f"\n· note     {p.name}")
        else:
            print(f"✓ clean    {p.name}")
        for s in hard + soft:
            print(f"   • {s}")

    print(f"\n{len(paths)} file(s) · {'FLAGS RAISED' if worst else 'no flags'}"
          f"{f' · {unread} unreadable' if unread else ''}")
    print("A clean run means the metadata raised nothing. It is not a certificate of "
          "provenance; no metadata can be one.")
    return 2 if unread else worst


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
