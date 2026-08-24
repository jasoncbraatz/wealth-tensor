#!/usr/bin/env python3
"""wt193 — Pass B repair of SHIP-LIST SL-1 and SL-2 (paper-III §4.9 attributions).

Both are ATTRIBUTION repairs, not number changes: -103 checked the arithmetic in
both sentences and it is correct.  Idempotent: reports NO-OP on a second run and
exits 0 either way.  Exit 2 if neither the old nor the new text is present.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/docs/papers/paper-III-dual-tensor/paper-III.md"

EDITS = [
    (
        "SL-1",
        "outside the\nrectangle whose fastest rate is 0.333, which is §5.4's measured rate arriving from the other\ndirection.",
        "outside the\nrectangle, whose own fastest disclosed rate is 0.333 — and above §5.4's measured peak-to-charge\nrecognition rate of 0.408 per year as well.",
    ),
    (
        "SL-2",
        "The *level* moves it by\n4.3%, from §4.4's 0.00789 at the calibration to 0.00755 at the measured rate, and moves something\nelse besides, which §4.4's tier table now states.",
        "The *level* moves it by\n4.3%, from 0.00789 at the calibration — §4.4's closed form evaluated there — to 0.00755 at the\nmeasured rate, and moves something else besides, which §4.4's tier table now states.",
    ),
]

def main():
    text = P.read_text(encoding="utf-8")
    orig = text
    rc = 0
    for tag, old, new in EDITS:
        if old in text:
            assert text.count(old) == 1, f"{tag}: old text is not unique"
            text = text.replace(old, new)
            print(f"{tag}: APPLIED")
        elif new in text:
            print(f"{tag}: NO-OP (already repaired)")
        else:
            print(f"{tag}: NOT FOUND — neither old nor new text present")
            rc = 2
    if rc == 0 and text != orig:
        P.write_text(text, encoding="utf-8")
        print("wrote", P)
    elif rc == 0:
        print("no write needed")
    return rc

sys.exit(main())
