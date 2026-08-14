"""C21 · the 0.327 cut is unregistered robustness, and the manuscript called it registered.

WHAT THE MACHINE FOUND
----------------------
`CONSTRAINT-INVENTORY-001` graded C21 — *"unregistered robustness may be reported, labelled
as robustness, and may not change a verdict"* (`REG-004` §6 and `REG-005` §7, identical
wording) — **compliant**, on the strength of §5.4's *"the unregistered shifted estimate is
0.460."* That grade was reached through the `unregistered` keyword, which finds the site
carrying the label and cannot find the site carrying the wrong one.

`REG-003` §3.1 **A3 registers exactly three sensitivities**: annual-attributed charges
excluded, right-censored events excluded, one event per firm. §3.2 registers a four-regime
ladder and no cut. **Dropping the 175 events charged one quarter after the peak is not among
them**, and `RESULT-REG-003` §2 files it — with the three administrative truncations and the
shifted support — under the heading *"Unregistered robustness, reported as robustness and not
as result."*

The manuscript called that cut **"the registered adverse cut"** at three sites and *"the cut
REG-003 registered in advance as the one that would break it"* at a fourth, and reported
unregistered numbers with no label at three more. Seven units, one root cause: **nothing in
the estate knew which cuts are registered**, so the adjective was free.

THE REPAIR IS REPLACE, NOT ABSORB (charter §2)
-----------------------------------------------
Every edit below swaps a false or absent label for a true one. **No claim is weakened and no
hedge is added** — `0.327`, `0.814`, `−0.67` and *"still an order of magnitude above the
calibration"* all survive verbatim, because C21 permits the number and requires the label.
The defensive-sentence count is unchanged (`scripts/defensive_count.py`'s lexicon excludes
scope words by design and by comment), and `tests/test_defensive_count.py` against
`DEFENSIVE-BASELINE.json` is the evidence, not the gitignored `.bak`.

**What is true, and now said:** `REG-003` §3.3's B2 registered the *doubt about the onset
bridge* and its direction in advance. The cut aimed at that doubt was chosen afterwards. The
manuscript said the cut was registered; what was registered was the reason for it.

WHAT THIS DOES NOT TOUCH
------------------------
`RESULT-REG-003` §2's *"Every cut lands in R1. The range across all of them is 0.327 to
0.499"* reads two ways — every REGISTERED cut lands in R1 (true; the ladder's R1 floor is
0.33 and every registered value clears it), or every cut named in the section does (false for
0.327, which is R2 by §3.2's own ladder). It is a result document and a record of a run, so it
is teed up rather than rewritten here. The manuscript's own regime sentence is correct: §5.4's
*"Every cut lands in the same regime"* scopes to the cuts named in that sentence, all of which
are R1, and 0.327 appears two paragraphs later making no regime claim.
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"

EDITS = [
    # ---- limb A · the label is wrong -----------------------------------------------------
    (PAPER,
     "the registered adverse cut — and the hazard rises",
     "the unregistered adverse cut — and the hazard rises",
     "abstract · the adverse cut is unregistered robustness"),
    (PAPER,
     "| **R** at α̂ = 0.327, the registered adverse cut |",
     "| **R** at α̂ = 0.327, the unregistered adverse cut |",
     "§4.4 · the ladder table's column header"),
    (PAPER,
     "measured rate and the registered adverse cut, where the first rung alone turns over",
     "measured rate and the unregistered adverse cut, where the first rung alone turns over",
     "§4.4 · the Kendall τ sentence"),
    (PAPER,
     "the cut REG-003 registered in advance as the one that would break it — the 175 events charged one",  # noqa: E501
     "the unregistered cut aimed at the doubt REG-003 §3.3 registered in advance — the 175 events\ncharged one",  # noqa: E501
     "§4.4 · what was registered was the doubt, not the cut"),

    # ---- limb B · the label is missing ---------------------------------------------------
    (PAPER,
     "**The one cut that removes",
     "**The one unregistered cut that removes",
     "§5.4 · the bolded lead carries the label"),
    (PAPER,
     "0.397, 0.499 and 0.413, and administratively censoring the sample at eight, twelve and sixteen",  # noqa: E501
     "0.397, 0.499 and 0.413. As unregistered robustness, administratively censoring the sample at\n"
     "eight, twelve and sixteen",
     "§5.4 · the three truncations are unregistered robustness"),
    (PAPER,
     "range **0.327–0.499** across every cut, none containing 0.05 |",
     "range **0.327–0.499** across every cut including the unregistered robustness, none containing 0.05 |",  # noqa: E501
     "§7 · the survivals ledger row names the range's source"),
]


def main() -> int:
    apply_edits(EDITS)
    flat = " ".join(PAPER.read_text(encoding="utf-8").split())

    # `(?<!un)` matters: "unregistered adverse cut" CONTAINS "registered adverse cut", so a
    # substring check reports the repair as the defect. Caught here rather than in review.
    for gone in (r"(?<!un)registered adverse cut",
                 r"At the cut REG-003 registered in advance"):
        if re.search(gone, flat):
            raise SystemExit(f"wt110: {gone!r} survives the edit")

    for needed in ("the unregistered adverse cut",
                   "At the unregistered cut aimed at the doubt REG-003 §3.3 registered in advance",
                   "**The one unregistered cut that removes the mass",
                   "As unregistered robustness, administratively censoring",
                   "across every cut including the unregistered robustness"):
        if needed not in flat:
            raise SystemExit(f"wt110: missing {needed!r}")

    # The claims C21 permits, verbatim: the numbers do not move, only their labels.
    for kept in ("**0.327**", "**0.814**", "still an order of magnitude above the calibration",
                 "0.396, 0.398 and 0.404", "range **0.327–0.499**"):
        if kept not in flat:
            raise SystemExit(f"wt110: {kept!r} was lost — this pass may not weaken a claim")

    print("wt110 ok · seven C21 sites relabelled · no claim weakened, no hedge added")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
