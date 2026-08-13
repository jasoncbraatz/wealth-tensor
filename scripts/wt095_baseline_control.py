#!/usr/bin/env python3
"""wealthTensor-21 — the intangible pair carried a new-crawl number in a published slot.

REG-003 (published) puts indefinite-lived intangible x goodwill in computer services at
2.41x. The manuscript printed 2.34x, which is REG-006's own harness value on the new
crawl. Introduced by 93a159b -- the commit that was correcting a published sentence.
Fix the number, and give the four intangible cells the same-crawl control the property
cell and the headline already carry (REG-007 F8).
"""
import sys

sys.path.insert(0, "scripts")
from patchkit import apply_edits

PAPER = "docs/papers/paper-III-dual-tensor/paper-III.md"
RESULT = "docs/preregistration/RESULT-REG-006.md"

apply_edits([
    (
        PAPER,
        "intangible-with-goodwill cells that replicate across both sectors — 5.83× and 2.34×, 3.33× and",
        "intangible-with-goodwill cells that replicate across both sectors — 5.83× and 2.41×, 3.33× and",
        "paper III §5.4 · the published pair is 5.83× and 2.41×, not 2.34×",
    ),
    (
        PAPER,
        """one below significance, and its cross-sector agreement does not survive the repair. The headline does: **4.01× and 2.10×**
repaired, against 4.01× and 2.01× from the same crawl unrepaired.""",
        """one below significance, and its cross-sector agreement does not survive the repair. The headline
does: **4.01× and 2.10×** repaired, against 4.01× and 2.01× from the same crawl unrepaired. So
does the intangible cells' agreement: **5.86× and 2.34×**, **3.35× and 2.22×** repaired, against
5.83× and 2.34×, 3.34× and 2.21× from that crawl unrepaired.""",
        "paper III §5.4 · the intangible cells get their same-crawl control, and the line re-flows",
    ),
    (
        RESULT,
        """**F6 is the guard**, and it passed: the committed event file reproduces the published lifts to
`1e-4` and every published cell exactly. The table and the sample have not drifted.""",
        """**F6 is the guard**, and it passed: the committed event file reproduces the published lifts to
`1e-4` and every published cell exactly. The table and the sample have not drifted.

**Correction, `wealthTensor-21` — the guard's scope was READ, and the exposure was WRITE.** The
list above is every constant this file *read out of* `RESULT-REG-003.md`. It is not every constant
this file *wrote into the manuscript*, and the gap between those two sets is where a defect sat for
a session. The replacement sentence §2.1 licensed — "it is these two intangible-with-goodwill cells
that replicate across both sectors" — shipped the pair **5.83× and 2.34×**. `RESULT-REG-003` puts
indefinite-lived intangible × goodwill in computer services at **2.41×** (p 0.0020); **2.34×** is
*this file's* number, from the new crawl, where it is the value on both arms. The retail half of
that pair was the published run's and the computer-services half was the repair's, in a sentence
whose whole job was to report what the published run found — the same baseline substitution
`wealthTensor-20` found one clause away in the property cell, introduced here by the very commit
that was correcting a published sentence. §5.4 now reads **2.41×**, and the four cells carry their
repaired arm (5.86× / 2.34×, 3.35× / 2.22×) against the same crawl unrepaired, so the intangible
claim is controlled the way the property and headline claims already were.

**The generalisation, for the next guard.** A constants list that enumerates what a run *consumed*
does not guard what that run *emits*. `F6` is a read-side guard; it passed, correctly and
irrelevantly, while the write side went unchecked. Any registration that amends published prose
should enumerate the constants it *introduces* and resolve each against the run that owns it.""",
        "RESULT-REG-006 §4 · the read-side guard did not cover the write side",
    ),
])
print("\nOK — 2.41× restored, intangible control added, guard-scope finding recorded.")
