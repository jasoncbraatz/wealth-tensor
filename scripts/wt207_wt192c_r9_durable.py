#!/usr/bin/env python3
"""wt207 — repair wt192c's R9, which is pinned to a MOVING subject.

R9 asserts the wt184 false-positive-reduction card's gid "still resolves in both places"
and measures that as `docs/HANDOFF.md`.count(gid) >= 2.  THAT FILE IS REWRITTEN WHOLESALE
EVERY SESSION, BY DESIGN -- it is the same defect this repository has already named twice
in its own drift flags (`-102`'s wt188 pair, `-103`'s wt192c R7/R8), arriving a third time
in a check that survived both repairs because it looked like a durable negative.

It is not a negative. It is a POSITIVE assertion that a pointer is not orphaned, and
"both places" was never two places -- it was two MENTIONS inside one moving file, one of
which lived in the at-bat text that every successor is required to replace.

THE TIGHTER SUBJECT, and it is the one R9 was actually written to protect: the gid
resolves in `docs/HANDOFF.md`'s parking lot AND in `docs/POST-SHIP.md`, which is where
new-instrument ideas live after the freeze. TWO FILES, one of them durable. A future
handoff that drops the card from its parking lot still goes red; a future handoff that
merely re-words its at-bat does not.

Idempotent: NO-OP on a second run, exit 0.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/scripts/wt192c_dangling_refs.py"

OLD = ('chk("R9 NEGATIVE: the wt184 card gid still resolves in both places",\n'
       '    h.count("1217774684736450") >= 2, True)')
NEW = ('# R9 was `h.count(gid) >= 2` until wealthTensor-104 -- two MENTIONS in one file that every\n'
       '# successor rewrites, which is the wt188 shape in a third costume. It now reads TWO FILES,\n'
       '# one of them durable, so it fires on an orphaned card and not on an ordinary handoff rewrite.\n'
       'POSTSHIP = (REPO / "docs/POST-SHIP.md").read_text(encoding="utf-8")\n'
       'chk("R9 NEGATIVE: the wt184 card gid still resolves in the handoff AND in POST-SHIP",\n'
       '    "1217774684736450" in h and "1217774684736450" in POSTSHIP, True)')

def main() -> int:
    t = P.read_text(encoding="utf-8")
    if "R9 NEGATIVE: the wt184 card gid still resolves in the handoff AND in POST-SHIP" in t:
        print("wt207: NO-OP (already repaired)"); return 0
    if OLD not in t:
        print("wt207: anchor not found"); return 2
    P.write_text(t.replace(OLD, NEW, 1), encoding="utf-8")
    print("wt207: APPLIED — R9 re-pointed at two files, one of them durable")
    return 0

sys.exit(main())
