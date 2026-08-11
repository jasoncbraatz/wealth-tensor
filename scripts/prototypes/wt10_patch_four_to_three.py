#!/usr/bin/env python3
"""wealthTensor-10 · the corpus is three papers now, and two live documents still said four.

WT-057 sweep after Jason's fold-I-into-IV ruling found nine occurrences of "four papers"
or "four preprints". Six are HISTORY and must not move:

    ADR-001 title, §Decision, §Relitigation record   — the decision as it was made
    docs/sessions/2026-08-05-S3.md                   — a session note
    docs/LEDGER.md                                   — append-only by design

Rewriting those would be the tidiness that manufactures a false history, which is the
exact defect logged three hours ago against a renamed PDF.

Two are LIVE and were wrong:

    ADR-001 header  — a reader hits the title before the addendum that amends it, so the
                      amendment goes at the top where ADR convention puts it
    HANDOFF §4c     — the Definition of Done. Load-bearing. A session driving at "four
                      posted" would drive one paper past the finish line.
"""
import sys
sys.path.insert(0, "/Users/jasoncbraatz/repos/wealth-tensor/scripts")
from patchkit import apply_edits  # noqa: E402

ADR = "/Users/jasoncbraatz/repos/wealth-tensor/docs/adr/ADR-001-paper-decomposition.md"
HO = "/Users/jasoncbraatz/repos/wealth-tensor/docs/HANDOFF.md"

apply_edits([
    (
        ADR,
        "- **Relitigation:** none required. If a future session wants to reopen this, read §Consequences",
        "- **AMENDED 2026-08-11 (wealthTensor-10): the corpus is THREE preprints.** Paper I folds into\n"
        "  Paper IV by Jason's ruling — see the final addendum. The title and §Decision below record the\n"
        "  decision **as it was made** and are deliberately not rewritten; the addenda amend it.\n"
        "- **Relitigation:** none required. If a future session wants to reopen this, read §Consequences",
        "ADR-001 header: amendment pointer above the fold",
    ),
    (
        HO,
        "> Four preprints publicly posted, each carrying: abstract, keywords, JEL codes, a numbered",
        "> **Three** preprints publicly posted — **II, III and IV** (Paper I folds into IV, ADR-001\n"
        "> addendum 7, Jason's ruling 2026-08-11) — each carrying: abstract, keywords, JEL codes, a numbered",
        "HANDOFF §4c Definition of Done: four -> three",
    ),
    (
        HO,
        "> Paper III additionally cites PRE-001/002 and their registering commit SHAs. When the fourth is\n"
        "> posted, this project is done and the repo becomes an archive.",
        "> Paper III additionally cites PRE-001/002 and their registering commit SHAs. **Paper IV\n"
        "> additionally carries Paper I's surviving identity — the crossing height IS the volume — and\n"
        "> Paper I's Abandoned Approaches, which will be the longest such entry in the corpus.** When the\n"
        "> third is posted, this project is done and the repo becomes an archive.",
        "HANDOFF §4c: 'the fourth' -> 'the third', and record what IV inherits",
    ),
])
print("patched: two LIVE four-paper claims corrected; six historical ones deliberately left alone")
