#!/usr/bin/env python3
"""wt152 · append wealthTensor-83's row to the P7 pass ledger."""
import pathlib, shutil, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
T = ROOT / "docs/p7-passes.tsv"
txt = T.read_text()
if "wealthTensor-83\t" in txt:
    sys.exit("REFUSE: row already present")

ROW = "\t".join([
 "wealthTensor-83", "paper-III", "4", "none",
 "— (all five axes inherited; the grid closed at -80 and Paper III was 5 of 5. What is new is not an "
 "axis but a TARGET: A5 was pointed at docs/promises-adjudicated.tsv itself, read as an artefact to be "
 "falsified rather than a result to be trusted.)",
 "0 of 4",
 "REVIEW-023. THE PREDICTION ROW, AND THE FIRST MECHANISM IN TWELVE TO SURVIVE ITS OWN NEXT PASS. "
 "-82 stopped theorising and enumerated the promise class -- 127 in scope, 2 failed -- and wrote a "
 "prediction its own pass could not settle: materially fewer than 5-of-9 promise-shaped next time. "
 "THIS PASS RETURNED FOUR FINDINGS, 1 of 4 PROMISE-SHAPED (0.25 against 0.556). THE PREDICTION HELD. "
 "Four mechanisms died one pass after being proposed (new instruments -71/-77, residue -77/-78, depth "
 "-78/-79, coverage -80/-81); enumeration is the fifth proposed and the first to live. SHAPES: 1 P / "
 "2 D / 1 -- against the 5/2/2 that -80 found on Paper III and -81 replicated on Paper IV. The "
 "deferral column held at 2 while the promise column collapsed 5 -> 1, so the only column that moved "
 "is the one -82 drained -- which is what makes n=4 readable rather than merely small. "
 "NO DISAMBIGUATION BRANCH FIRED, AND A THIRD MODE DID: the one promise-shaped finding (III-1) names "
 "data/pre-002-events.json and wt148 EMITTED that exact pair -- so it is neither an instrument gap "
 "(branch a) nor a mis-defined class (branch b). Row 93662b4195 was adjudicated H off wt089's "
 "reconciliation block (313 = 122+191) instead of off the file the sentence names, where the union is "
 "307; RESULT-REG-003 §1 states 307 in those words and names the six dual-SIC registrants, and "
 "REG-003 §2's one-event-per-firm sensitivity -- the 0.413 §5.4 quotes -- is computed on n=307. "
 "THE ADJUDICATIONS ARE AN ARTEFACT TOO, AND NOBODY HAS MEASURED THEIR ERROR RATE. That is -84's "
 "at-bat. RESIDUE 0 of 4: no site blames to wt149/wt150; III-1's SITE predates -82 and what -82 added "
 "is the false row, which is apparatus and is counted in REVIEW-023 §1 rather than as residue. "
 "MANUSCRIPT EDITS: 4 of 4 (wt151, 10 post-conditions, 3 NEGATIVE). Both A3 findings are structurally "
 "invisible to both sweeps -- bare noun phrase and bare section number -- which is the corpus texture "
 "the enumeration does not reach and the reason the deferral column did not move."
])
shutil.copyfile(T, T.with_name(T.name + ".bak-wt152"))
T.write_text(txt.rstrip("\n") + "\n" + ROW + "\n")
print("appended wealthTensor-83 row")
