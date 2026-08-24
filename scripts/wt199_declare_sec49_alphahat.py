#!/usr/bin/env python3
"""wt199 — close the guard SL-1's repair reddened, by DECLARING the count it added.

`tests/test_restatement_reach.py` pins how many times each registered figure is printed
per section, and states the bargain in its own docstring: an edit that legitimately adds
a mention turns the suite red and the author updates the number here.  SL-1's repair is
that edit.  The false clause it removed said 0.333 WAS §5.4's measured rate; the repair
states §5.4's rate as 0.408 explicitly -- which is SHIP-LIST SL-1's own named repair --
so §4.9 now prints α̂ once where it printed it never.

This TIGHTENS the declaration: §4.9 gains a pinned count, so a copy drifting there is now
watched where before it was not.  It does not relax anything.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/tests/test_restatement_reach.py"

OLD = ('    # α̂ = 0.408 is load-bearing in five sections at once.\n'
       '    "0.408":  {"4.10": 5, "4.4": 2, "5.4": 1, "7": 2, "9": 1},\n')
NEW = ('    # α̂ = 0.408 is load-bearing in six sections at once. §4.9\'s copy is the youngest:\n'
       '    # wealthTensor-104 repaired SHIP-LIST SL-1 there, where a relative clause had called\n'
       '    # the rectangle\'s own fastest rate (0.333) "§5.4\'s measured rate". The repair names\n'
       '    # §5.4\'s rate instead of mis-pointing at it, so the section prints α̂ once.\n'
       '    "0.408":  {"4.10": 5, "4.4": 2, "4.9": 1, "5.4": 1, "7": 2, "9": 1},\n')

def main():
    text = P.read_text(encoding="utf-8")
    if NEW in text:
        print("wt199: NO-OP (already declared)"); return 0
    if OLD not in text:
        print("wt199: NOT FOUND — neither old nor new declaration present"); return 2
    if text.count(OLD) != 1:
        print("wt199: anchor is not unique"); return 2
    P.write_text(text.replace(OLD, NEW), encoding="utf-8")
    print("wt199: APPLIED — §4.9 declared for 0.408")
    return 0

sys.exit(main())
