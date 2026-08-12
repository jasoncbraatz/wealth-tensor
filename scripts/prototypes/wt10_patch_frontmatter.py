#!/usr/bin/env python3
"""wealthTensor-10 · the front-matter items Jason approved: address, interest, AI disclosure."""
import sys
sys.path.insert(0, "/Users/jasoncbraatz/repos/wealth-tensor/scripts")
from patchkit import apply_edits  # noqa: E402

D = "/Users/jasoncbraatz/repos/wealth-tensor/docs/papers"
P2 = f"{D}/paper-II-redistribution/paper-II.md"
P3 = f"{D}/paper-III-dual-tensor/paper-III.md"

DISCLOSURE = (
    "\n**Declaration of interest.** The author is employed by a company building accounting "
    "software for very small businesses. This work was conducted independently, on personal "
    "time, and without company funding, data or direction.\n"
    "\n**Use of AI assistance.** Anthropic Claude Opus 5, at high reasoning effort, was used "
    "throughout as a research and drafting assistant: literature retrieval, adversarial review, "
    "code review and prose drafting. All claims, results and final text are the author's, and "
    "every computational result is produced by committed code in the repository named in the "
    "data-availability statement.\n"
)

edits = []
for path in (P2, P3):
    edits.append((path, "jasoncbraatz@gmail.com", "jason@braatzresearch.com",
                  f"corresponding address ({path[-12:]})"))

edits.append((P2, "**Draft — not yet submitted.** Version 0.2, 2026-08-11.",
              "**Draft — not yet submitted.** Version 0.2, 2026-08-11.\n" + DISCLOSURE,
              "paper-II: interest + AI disclosure"))
edits.append((P3, "**Draft — not yet submitted.** Version 0.4, 2026-08-11.",
              "**Draft — not yet submitted.** Version 0.4, 2026-08-11.\n" + DISCLOSURE,
              "paper-III: interest + AI disclosure"))

apply_edits(edits)
print("patched: address -> jason@braatzresearch.com; interest + AI disclosure in both papers")
