#!/usr/bin/env python3
"""wealthTensor-10 · bug spray on the Paper III reference apparatus.

Two stale lines, both created by the -09 late addition of the fourth pass and the
third mark, both invisible to every check the project runs (L35: RE-READ YOUR OWN
DOCUMENT AFTER A LATE CORRECTION -- no script does it).

  1. "Three passes ran, in this order" is immediately followed by FOUR numbered items.
  2. "The per-entry findings live in the checkmark and pencil notes" omits the hourglass
     mark, which -09 added in the same edit.

Nothing here touches a result, a number, a claim or a citation.
"""
import sys
sys.path.insert(0, "/Users/jasoncbraatz/repos/wealth-tensor/scripts")
from patchkit import apply_edits  # noqa: E402

P = "/Users/jasoncbraatz/repos/wealth-tensor/docs/papers/paper-III-dual-tensor/paper-III.md"

apply_edits([
    (
        P,
        "**Three passes ran, in this order, and each one found what the previous one structurally could not.**",
        "**Four passes ran, in this order, and each one found what the previous ones structurally could not.**",
        "count: three -> four (four items are listed)",
    ),
    (
        P,
        "reader nothing. The per-entry findings live in the ✓ and ✓✎ notes above, attached to the entries they",
        "reader nothing. The per-entry findings live in the ✓, ✓✎ and ✓⧗ notes above, attached to the entries they",
        "marks list: add the version mark added in -09",
    ),
])
print("patched: paper-III.md apparatus (2 stale lines from the -09 late addition)")
