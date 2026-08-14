#!/usr/bin/env python3
"""§4.7's coverage-fill conditional, replaced by the measurement; and `-31`'s §4 amended.

Registered in `docs/preregistration/RESULT-REG-009-band-count-filled.md` §6 BEFORE this
script was written, per charter §2.

EDIT 1-2 are a REPLACEMENT, not a hedge. §4.7 carried a conditional -- "would bring a
second band to the floor IF the unjoined events fall like the joined ones" -- about a
measurement that is now run, and whose antecedent turns out to be false: the second band
reached 27 against a floor of 30 where the proportional bracket predicted 30.2. The
conditional is replaced by the outcome, in the claim's own units. The bound the old
sentence also carried ("no allocation brings more than a third") HELD and is not
re-asserted: a bound the measurement has superseded is a hedge kept past its usefulness,
and re-stating it would be the ABSORB move charter §2 forbids.

EDIT 3 amends RESULT-REG-009-band-count §4 with the one line the tee-up asked for --
which way the second band went -- and does NOT repair anything in `-31`'s document. The
two errata recorded there stay recorded, the count of one stays, and the amendment is
appended beside the verdict rather than rewritten into it.

G-COACH-3 across the edit is evaluated in the same pass (`scripts/defensive_count.py`).

One-shot. It is committed as the record of what was changed and how; re-running it after
the fact raises AnchorError, having written nothing, which is patchkit doing its job.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits                                       # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
P3 = str(ROOT / "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md")
R31 = str(ROOT / "docs" / "preregistration" / "RESULT-REG-009-band-count.md")

EDITS = [
    (P3,
     "two cycles leave between them would bring a second band to the floor if the "
     "unjoined events fall",
     "two cycles leave between them — the seven intervening cycles, run — raises the "
     "join to **133\nof the 151** and leaves the same single band clearing: the second "
     "band reaches twenty-seven against",
     "§4.7a · the conditional becomes the measurement"),
    (P3,
     "like the joined ones, and no allocation of them brings more than a third.",
     "the floor of thirty. The registered reading is the only one that gives one — the "
     "two other cycle\nchoices give two, as does the nearest-cycle rule under the "
     "opposite tie-break.",
     "§4.7b · and carries the reading the count depends on"),
    (R31,
     "the one measurement that could cross it back is named, priced and unrun.",
     "the one measurement that could cross it back is named, priced and unrun.\n\n"
     "> **AMENDED 2026-08-14, `wealthTensor-32` — THE CHEAP FILL IS RUN, AND THE SECOND "
     "BAND DID NOT CLEAR.** The seven intervening cycles raise the join from 110 to "
     "**133 of the 151**, and `[4, 5)` reaches **27** against the floor of 30 where the "
     "proportional bracket above predicted 30.2: the unjoined events did not fall like "
     "the joined ones. One band still clears and §7.5's verdict stands. **But the fill "
     "made the nearest-cycle rule's TIE-BREAK reachable for the first time** — 0 of the "
     "110 joinable events here, 50 of the 133 there — and the count is two under that "
     "tie-break's mirror, under both other cycle choices, and under `R_MIN`. The "
     "registered reading is now the only reading that gives one. Nothing above is "
     "repaired: see `RESULT-REG-009-band-count-filled.md`.",
     "§4 · the amendment the tee-up asked for, appended beside the verdict"),
]

if __name__ == "__main__":
    apply_edits(EDITS)
