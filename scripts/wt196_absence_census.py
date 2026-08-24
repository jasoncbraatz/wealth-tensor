#!/usr/bin/env python3
"""wt196 — Pass B repair of SHIP-LIST SL-9: paper-IV §9 item 9's exhaustiveness claim.

The three named absences are correct and the item's arithmetic checks.  What nothing
supports is the CENSUS: *"the rest"* and *"Three others"* both assert the enumeration is
complete, and no instrument in the frozen set enumerates this paper's absence claims
(DoD §1.1 forbids building the one that would).  The repair is one clause in each of the
two places the census is asserted -- both, because a repair that lands at one leaves the
document asserting both things.  Exhaustiveness is NOT verified here; that is POST-SHIP.

Idempotent: NO-OP on a second run, exit 0.  Exit 2 if a site matches neither state.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/docs/papers/paper-IV-composition/paper-IV.md"

EDITS = [
    ("SL-9a · the lede",
     "9. **One of this paper's absences is measured and the rest are asserted, and §6's own standard is\n   why that is worth stating.**",
     "9. **One of this paper's absences is measured and three others named here are asserted, and §6's\n   own standard is why that is worth stating.**"),
    ("SL-9b · the enumeration",
     "the search*, and it measures the absence that motivates the paper. Three others are not\n   measured: §1.1's *the input-output energy table has no lapse to report*, which is load-bearing\n   for §1.1's reading of §4.3 as *largely unmeasured rather than merely unassembled*; and §7's\n   two\n   within-literature absences,",
     "the search*, and it measures the absence that motivates the paper. Three others, named here, are\n   not measured: §1.1's *the input-output energy table has no lapse to report*, which is\n   load-bearing for §1.1's reading of §4.3 as *largely unmeasured rather than merely unassembled*;\n   and §7's two within-literature absences,"),
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
