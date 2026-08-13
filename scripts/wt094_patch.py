#!/usr/bin/env python3
"""wealthTensor-20 — three evidence-backed repairs.

1. §7's dangling ordinal. At 85d578b (the commit that wrote the paragraph) the
   table's fifth row WAS "The inversion spares the lag statistic" — 400 draws,
   carrying the italic tag "the check that overturned this paper's own draft
   claim". The table has since grown to ~40 rows and the ordinal drifted onto
   an unrelated row. Named, not guessed.

2. §5.4's property cell compares PUBLISHED-crawl 4.35x/4.03x against
   NEW-crawl corrected 3.99x/2.17x and attributes the movement to the repair.
   RESULT-REG-006 §2.1 gives the same-crawl original: 3.63x/4.14x. The repair
   RAISES retail. The section already uses the same-crawl idiom for the
   headline one sentence later; the property cell silently dropped it.

3. RESULT-REG-006 §2.2 says "the paper reports" two cells the manuscript has
   never printed.
"""
import sys

sys.path.insert(0, "scripts")
from patchkit import apply_edits

PAPER = "docs/papers/paper-III-dual-tensor/paper-III.md"
RESULT = "docs/preregistration/RESULT-REG-006.md"

edits = [
    (
        PAPER,
        """The fifth is the reason this section is not decoration. The draft that preceded this one asserted
that the identification result explained the registered null. The check in that row was written to
confirm it and refused, in every one of 400 draws, and the claim came out of the paper. A survivals
ledger that contains only survivals is an advertisement; this one contains the row that cost the
paper its neatest sentence.""",
        """The row on the inversion sparing the lag statistic is the reason this section is not decoration.
The draft that preceded this one asserted that the identification result explained the registered
null. The check in that row was written to confirm it and refused, in every one of 400 draws, and
the claim came out of the paper. A survivals ledger that contains only survivals is an
advertisement; this one contains the row that cost the paper its neatest sentence.""",
        "§7 · name the row instead of counting to it",
    ),
    (
        PAPER,
        """2.22×, all four surviving Holm correction. Property with goodwill runs at 4.35× and 4.03× on a
tier whose tag list omitted the element most filers use for it; `REG-006` repairs the omission and
re-derives that cell at **3.99×** and **2.17×**, the second no longer significant, so its
cross-sector agreement does not survive the repair.""",
        """2.22×, all four surviving Holm correction. Property with goodwill was published at 4.35× and
4.03× on a tier whose tag list omitted the element most filers use for it; `REG-006` repairs the
omission and re-derives that cell at **3.99×** and **2.17×**, against **3.63×** and **4.14×** from
the same crawl unrepaired — so the repair *raises* the retail cell and takes the computer-services
one below significance, and its cross-sector agreement does not survive the repair.""",
        "§5.4 · same-crawl control on the property cell",
    ),
    (
        RESULT,
        """With a half-blind tier 0 the paper reports two retail cells at **0.00× and 3.27×, p = 1.0000**.""",
        """With a half-blind tier 0 the ladder returns two retail cells at **0.00× and 3.27×, p = 1.0000**.""",
        "RESULT-REG-006 §2.2 · the ladder returns, the paper does not",
    ),
    (
        RESULT,
        """because the instrument could not see one of its two arms is not a measured zero, and the
distinction is the same one this project has now paid for three times.""",
        """because the instrument could not see one of its two arms is not a measured zero, and the
distinction is the same one this project has now paid for three times.

**Correction and scope ruling, `wealthTensor-20`.** This section originally said *the paper*
reports those two cells. It does not, and never has: `git log -S"0.00×"` against the manuscript
returns no commit, and §5.4 prints only the goodwill-paired cells. The zero lives in this ladder's
run log. That distinction also settles what to do with the pair — they are couplings the repair
**discovered**, not published claims the repair **revised**, so they stay out of §5.4. `REG-006`
registered the re-derivation of *published* cells; promoting cells that became significant under
the repair is a new registration, not an amendment.""",
        "RESULT-REG-006 §2.2 · correction + scope ruling",
    ),
]

apply_edits(edits)
print("\nOK — all four anchors resolved and written.")
