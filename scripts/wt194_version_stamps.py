#!/usr/bin/env python3
"""wt194 — Pass B repair of SHIP-LIST SL-3, SL-4 and SL-5: three stale version stamps.

One repair, three times.  Each manuscript's front matter asserted a version and a date
that later commits had overtaken (21 / 36 / 19 commits).  Bump to the next version with
today's date and add ONE revision line at the CLASS level.  Charter §3.3 forbids
enumerating findings in a manuscript, so the line says what the passes did, not what
they found.

Idempotent: NO-OP on a second run, exit 0.  Exit 2 if a site matches neither state.
"""
import sys, pathlib

ROOT = pathlib.Path.home() / "repos/wealth-tensor/docs/papers"
DATE = "2026-08-24"

CLASS_LINE = ("independent review passes; results, numbers, claims and\n"
              "citations were corrected where those passes found them wrong.")

EDITS = [
    # SL-3 · paper-II — bump the stamp AND extend the existing revision history
    ("SL-3", "paper-II-redistribution/paper-II.md",
     "**Draft — not yet submitted.** Version 0.2, 2026-08-11.",
     f"**Draft — not yet submitted.** Version 0.3, {DATE}."),
    ("SL-3b", "paper-II-redistribution/paper-II.md",
     "are removed. No result, number, claim or citation changed.*",
     "are removed. No result, number, claim or citation changed.\n"
     "**v0.3** independent review passes; results, numbers, claims and citations were corrected\n"
     "where those passes found them wrong.*"),

    # SL-4 · paper-III — bump the stamp and add a revision note (it had none)
    ("SL-4", "paper-III-dual-tensor/paper-III.md",
     "**Draft — not yet submitted.** Version 0.5, 2026-08-12.",
     f"**Draft — not yet submitted.** Version 0.6, {DATE}."),
    ("SL-4b", "paper-III-dual-tensor/paper-III.md",
     "code review and prose drafting. All claims, results and final text are the author's, and every computational result is produced by committed code in the repository named in §11.\n\n---\n",
     "code review and prose drafting. All claims, results and final text are the author's, and every computational result is produced by committed code in the repository named in §11.\n\n*Revision note: **v0.6**, this draft — " + CLASS_LINE + "*\n\n---\n"),

    # SL-5 · paper-IV — same
    ("SL-5", "paper-IV-composition/paper-IV.md",
     "**Draft — not yet submitted.** Version 0.1, 2026-08-16.",
     f"**Draft — not yet submitted.** Version 0.2, {DATE}."),
    ("SL-5b", "paper-IV-composition/paper-IV.md",
     "code review and prose drafting. All claims, results and final text are the author's, and every computational result is produced by committed code in the repository named in §10.\n\n---\n",
     "code review and prose drafting. All claims, results and final text are the author's, and every computational result is produced by committed code in the repository named in §10.\n\n*Revision note: **v0.2**, this draft — " + CLASS_LINE + "*\n\n---\n"),
]

def main():
    rc = 0
    bufs = {}
    for tag, rel, old, new in EDITS:
        p = ROOT / rel
        text = bufs.get(rel)
        if text is None:
            text = bufs[rel] = p.read_text(encoding="utf-8")
        if old in text:
            if text.count(old) != 1:
                print(f"{tag}: old text is not unique ({text.count(old)}x)"); return 2
            bufs[rel] = text.replace(old, new)
            print(f"{tag}: APPLIED  ({rel})")
        elif new in text:
            print(f"{tag}: NO-OP (already repaired)  ({rel})")
        else:
            print(f"{tag}: NOT FOUND — neither old nor new text present  ({rel})")
            rc = 2
    if rc:
        return rc
    for rel, text in bufs.items():
        p = ROOT / rel
        if p.read_text(encoding="utf-8") != text:
            p.write_text(text, encoding="utf-8")
            print("wrote", rel)
    return 0

sys.exit(main())
