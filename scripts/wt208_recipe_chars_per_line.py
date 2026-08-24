#!/usr/bin/env python3
"""wt208 — carry the re-measured characters-per-line into RECIPE.md, both halves.

Pass B added prose to all three manuscripts, so the corpus the typography probe measures
is a different corpus: `body.chars_per_line` moves 65.37 -> 65.4 and the corpus sha with
it. `wt173 --measure` rewrites METRICS-MEASURED.json; it does NOT rewrite RECIPE.md, and
`--verify` holds the recipe to the build in TWO places -- the data block a script reads
and the numbered step a human reads. Both move here or the two recipes drift apart, which
is the exact failure `--verify`'s second assertion exists to catch.

65.4 IS STILL INSIDE SECTION 0'S 62-68 BAND, so nothing is retuned: this is a measurement
following its corpus, not a choice being adjusted to make a number come out.

Idempotent: NO-OP on a second run, exit 0.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/docs/deliverable/RECIPE.md"

EDITS = [
    ("the prose step a human reads", "**65.37** characters per line", "**65.4** characters per line"),
    ("the data block a script reads", "body.chars_per_line\t65.37\t", "body.chars_per_line\t65.4\t"),
]

def main() -> int:
    t = P.read_text(encoding="utf-8")
    orig, rc = t, 0
    for tag, old, new in EDITS:
        if old in t:
            if t.count(old) != 1:
                print(f"{tag}: anchor not unique ({t.count(old)}x)"); return 2
            t = t.replace(old, new); print(f"{tag}: APPLIED")
        elif new in t:
            print(f"{tag}: NO-OP (already 65.4)")
        else:
            print(f"{tag}: NOT FOUND"); rc = 2
    if rc: return rc
    if t != orig:
        P.write_text(t, encoding="utf-8"); print("wrote RECIPE.md")
    else:
        print("no write needed")
    return 0

sys.exit(main())
