#!/usr/bin/env python3
"""§4.4's table: the measured column, and the calibration label. Jason's ruling, -18.

Open since -16. He chose both moves together: the label explains why the α = 0.05 column
stays (killing the vestigial-column risk), and the α̂ column gives the section's four
"at the measured rate" clauses something visible to point at.

The two-word prose change is NOT optional -- §4.4 navigates the table positionally
("The column beside it"), so inserting a column breaks the sentence unless it is
re-anchored by name. Structure delta: NONE.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits

P = str(pathlib.Path(__file__).resolve().parent / "paper-III.md")

TABLE_OLD = """| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** | R at a common δ |
|---|---|---|---|---|---|---|
| 0 · property, plant and equipment | 0.80 | 0.20 | 0.030 | 0.00600 | **0.2999** | 0.1333 |
| 1 · finite-lived intangibles | 0.60 | 0.40 | 0.020 | 0.00800 | **0.2667** | 0.2667 |
| 2 · indefinite-lived intangibles | 0.40 | 0.60 | 0.010 | 0.00600 | **0.1500** | 0.4000 |
| 3 · goodwill | 0.20 | 0.80 | 0.002 | 0.00160 | **0.0333** | 0.5333 |"""

TABLE_NEW = """| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** at α = 0.05, the calibration | **R** at α̂ = 0.408, measured (§5.4) | R at a common δ |
|---|---|---|---|---|---|---|---|
| 0 · property, plant and equipment | 0.80 | 0.20 | 0.030 | 0.00600 | **0.2999** | **0.0159** | 0.1333 |
| 1 · finite-lived intangibles | 0.60 | 0.40 | 0.020 | 0.00800 | **0.2667** | **0.0206** | 0.2667 |
| 2 · indefinite-lived intangibles | 0.40 | 0.60 | 0.010 | 0.00600 | **0.1500** | **0.0151** | 0.4000 |
| 3 · goodwill | 0.20 | 0.80 | 0.002 | 0.00160 | **0.0333** | **0.0039** | 0.5333 |"""

PROSE_OLD = """The right-hand column is the world the design assumed: classes differing in observability and in
nothing else. There the deferral measure rises monotonically up the ladder exactly as predicted,
Kendall τ = +1. The column beside it is the world the standards describe. There the deferral measure
is monotone too — **running the other way.** Kendall τ = **−1** at the calibrated rate, and **−0.67**
at the measured one; the rung that separates them is identified below."""

PROSE_NEW = """The right-hand column is the world the design assumed: classes differing in observability and in
nothing else. There the deferral measure rises monotonically up the ladder exactly as predicted,
Kendall τ = +1. The two **R** columns are the world the standards describe, at the recognition rate
calibrated here and at the one §5.4 goes on to measure. There the deferral measure is monotone
too — **running the other way.** Kendall τ = **−1** at the calibrated rate, and **−0.67** at the
measured one, where the first rung alone turns over; the rung that separates them is identified
below."""

if __name__ == "__main__":
    apply_edits([
        (P, TABLE_OLD, TABLE_NEW, "§4.4 · the measured column, and the calibration label"),
        (P, PROSE_OLD, PROSE_NEW, "§4.4 · re-anchor the positional reference by name"),
    ], expect_structure={})
