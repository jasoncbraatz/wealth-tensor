#!/usr/bin/env python3
"""§4.7's feasibility sentence, repaired to carry REG-009 §7.5's measured band count.

Registered in `docs/preregistration/RESULT-REG-009-band-count.md` §5 BEFORE this script
was written, per charter §2. Both edits are REPLACEMENTS of a claim that measured wrong,
not hedges added beside it: the old sentence divided 151 by the qualifying-band count of
the rule §6 refuses to promote, and divided the crawl rather than the joinable
population. G-COACH-3 across the edit: 3 -> 3.

One-shot. It is committed as the record of what was changed and how; re-running it after
the fact raises AnchorError, having written nothing, which is patchkit doing its job.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits                                       # noqa: E402

P = str(pathlib.Path(__file__).resolve().parent.parent /
        "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md")

EDITS = [
    (P,
     "a disclosed life. Across the one-year life bands that design requires, 151 events "
     "average 21 per",
     "a disclosed life. Across the one-year life bands that design requires, those 110 "
     "events occupy",
     "§4.7a · the population the bands are drawn from is the joinable one"),
    (P,
     "band against §5's floor of 30.",
     "sixteen bands and **exactly one clears §5's floor of 30** — thirty-six events from "
     "twenty firms\nat a five-year life — with none clearing on firms rather than events. "
     "Filling the coverage §5's\ntwo cycles leave between them would bring a second band "
     "to the floor if the unjoined events fall\nlike the joined ones, and no allocation "
     "of them brings more than a third.",
     "§4.7b · the feasibility claim carries the measured band count"),
]

if __name__ == "__main__":
    apply_edits(EDITS)
