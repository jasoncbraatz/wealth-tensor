#!/usr/bin/env python3
"""wt195 — Pass B repair of SHIP-LIST SL-6: paper-IV's word count, made checkable.

The defect was never the figure.  `wc -w` returns 7 527 under a UTF-8 locale and 7 367
under a non-UTF-8 one ON THE SAME BYTES (md5 eb56ef67162df6db0fabf50819db78f0), so a
paper that invites the check and names no command and no locale is wrong for one
legitimate reader whichever number it prints.  The repair NAMES THE COMMAND AND ITS
LOCALE in §10, beside the other regeneration bullets, and keeps "roughly 7,500".

Idempotent: NO-OP on a second run, exit 0.  Exit 2 if a site matches neither state.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/docs/papers/paper-IV-composition/paper-IV.md"

EDITS = [
    # §8 — point the reader at the command instead of at the file alone
    ("SL-6a",
     "at `docs/papers/paper-I-price-formation/paper-I.md` — which is the only place the word count above\nis checkable. Had the",
     "at `docs/papers/paper-I-price-formation/paper-I.md`, and §10 names the command and the locale\nthat count it. Had the"),
    # §10 preamble — point at the bullet
    ("SL-6b",
     "fourth paper §8 describes; and §8's word count for that paper is `wc -w` on the superseded draft\n§8 names.",
     "fourth paper §8 describes; and §8's word count for that paper is the `wc -w` named below, on the\nsuperseded draft §8 names."),
    # §10 — the bullet itself, beside the other regeneration bullets
    ("SL-6c",
     "is a verdict and not a table; `wt018_report.py` is the table.\n- **Commit for the results reported here:**",
     "is a verdict and not a table; `wt018_report.py` is the table.\n"
     "- **Regenerate §8's word count:** `LC_ALL=C.UTF-8 wc -w docs/papers/paper-I-price-formation/paper-I.md`\n"
     "  returns **7,527**, the *roughly 7,500* §8 reports. **The locale is part of the command:** the\n"
     "  same bytes return **7,367** under GNU `wc` in a non-UTF-8 locale, so a word count quoted without\n"
     "  a locale is checkable only by accident.\n"
     "- **Commit for the results reported here:**"),
]

def main():
    text = P.read_text(encoding="utf-8")
    orig, rc = text, 0
    for tag, old, new in EDITS:
        if old in text:
            if text.count(old) != 1:
                print(f"{tag}: old text is not unique ({text.count(old)}x)"); return 2
            text = text.replace(old, new); print(f"{tag}: APPLIED")
        elif new in text:
            print(f"{tag}: NO-OP (already repaired)")
        else:
            print(f"{tag}: NOT FOUND — neither old nor new text present"); rc = 2
    if rc: return rc
    if text != orig:
        P.write_text(text, encoding="utf-8"); print("wrote", P.name)
    else:
        print("no write needed")
    return 0

sys.exit(main())
