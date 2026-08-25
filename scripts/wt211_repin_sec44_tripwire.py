#!/usr/bin/env python3
"""wt211 — re-pin the §4.4 argument tripwire, in the SAME commit as the edit that moved it.

READING: **CARRYING SENTENCE.** Pass D removed one clause from §4.4's table preamble —
"and both are worth having in hand before the table is read" — which tells the reader what
to do with the table rather than stating anything about the world.  It is scaffolding voice
(DoD § 2.5, C-b), and REVIEW-039 § 6.2 names this exact shape as Pass C's own residue and
assigns it to Pass D: "Pass D should read the nineteen edit sites with a C-b eye."

NO NUMBER MOVED, which is the unusual part of this re-pin and the reason it is spelled out:
REG-003 § 7 licenses "one number and the sentences that carry it", and this edit changes a
sentence that carries a number without changing the number.  The rectangle, the domain, the
admissible shares, the runs, the two measured columns and every figure in the table are
byte-identical.  What left the section is a piece of document navigation.
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TEST = ROOT / "tests/test_tripwire_c17_sec44_argument.py"
OLD = "fd56b1fb6f521c4f1e261ff3d98a27f2ff2583af49c8ec0708055f3ec9441002"

NOTE = '''#: RE-PINNED AT wealthTensor-106 (Pass D). READING: CARRYING SENTENCE, and NO NUMBER MOVED
#: -- which is why this entry is longer than its predecessors. Pass D removed one clause from
#: the table preamble, "and both are worth having in hand before the table is read": document
#: navigation, not a claim about the world, and the C-b shape REVIEW-039 section 6.2 hands to
#: Pass D by name as Pass C's own residue. The rectangle, the domain, the admissible shares,
#: the two measured columns, the crossing rate and every figure in the table are byte-identical
#: across this edit; the masked digest moves because the mask covers numerals, not prose.
'''

def main():
    src = TEST.read_text(encoding="utf-8")
    if OLD not in src:
        print("ALREADY-REPINNED (or the pin moved elsewhere) — nothing to do"); return 0
    sys.path.insert(0, str(ROOT / "tests"))
    import test_tripwire_c17_sec44_argument as T
    paper = (ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md").read_text(encoding="utf-8")
    # DERIVED through the test module's own extractor and mask, never transcribed.
    new = T.digest(T.masked(T.section_44(paper)))
    print("derived new masked digest:", new)
    bak = TEST.with_suffix(".py.bak-wt211")
    if not bak.exists(): bak.write_text(src, encoding="utf-8")
    out = src.replace('SEC_44_MASKED_SHA256 = "%s"' % OLD,
                      NOTE + 'SEC_44_MASKED_SHA256 = "%s"' % new, 1)
    TEST.write_text(out, encoding="utf-8")
    print("RE-PINNED %s -> %s" % (OLD[:12], new[:12]))
    return 0

if __name__ == "__main__":
    sys.exit(main())
