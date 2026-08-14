"""`REG-003` §3.3 — the registered asymmetry, attached at the four sites that report the
finding without it.

WHAT §3.3 SAYS, AND WHY IT WAS NEVER CHECKED
---------------------------------------------
    **A low α̂ is strong evidence; a high α̂ is weak.** ... If it lands in R1 or R2, the
    finding is exactly what two upward biases would manufacture, and **it must be reported
    with that sentence attached, in the same paragraph, not in a limitations section.**

`-41` mechanised §7 of the same registration — a *sentence* rule about rounding — and
stopped, because §7 is the constraint `SCOUT-001` happened to quote. §3.3 differs in the two
ways that hid it: it is written at **paragraph** resolution, and it is **conditional** on the
regime, so reading the registration is not enough. `RESULT-REG-003` records **R1 in every
cut** (pooled 0.4077; 0.3940–0.4986 across both universes and all three registered
sensitivities). The constraint has been live since the run.

THE SITES, AND THE ONE THAT WAS ALREADY CLEAN
----------------------------------------------
The abstract complies — and it complies *by accident*. `-41`'s T1 rewrote it for §7 and the
replacement happened to carry *"on both known biases' inflating side"*; the pre-edit line at
`0b26a8a` had nothing. Four other sites report the finding and carry no direction:

  1. **§4.4** — the estimate, its interval, the calibration it overturns, and the R1
     consequence (the rectangle inside the domain), with no word about the biases.
  2. **§5.4's bolded lead paragraph** — the section that PRODUCED the number. Its biases
     paragraph sits three paragraphs below, which is the *section* complying and the
     *paragraph* not. That distinction is `-41`'s own second tell, applied to `-41`'s work.
  3. **§7's survivals ledger row** — the row a referee skimming the ledger reads.
  4. **§9 limitation 4** — §3.3 names a limitations section explicitly as the place the
     qualification may *not* live; a restatement of the finding there without it is the
     exile the clause forbids.

Every one is a **REPLACE** under charter §2: the registered direction goes *inside* the
sentence that already carries the number. No sentence is added, so `G-COACH-3`'s count
cannot move, and no new numeric token is introduced, so `test_restatement_reach.py`'s
declared counts cannot move either.

THE GATE
--------
`-41`: *write the edit script's gate against the manuscript's own published cells — a gate
that only protects the new work is half a gate*, and *compute in `fractions.Fraction`, so
the gate finds the artefact instead of being tuned around it.*

So before a byte moves, this script re-derives §3.2's registered annualisation
`α̂_yr = 1 − (1 − α̂_q)⁴` from §5.4's own published per-quarter estimate, in exact rationals,
and requires it to reproduce the published 0.408 **and** to land at or above §3.2's R1
boundary of 0.33. That is the constraint's own antecedent, recomputed rather than inherited:
if the annualisation ever drifted, or if a re-run moved the estimate below 0.33, this script
would refuse before writing — because at that point §3.3 would no longer fire and attaching
its sentence would be enforcing a rule the registration had released.
"""
from __future__ import annotations

import pathlib
import shutil
import sys
from fractions import Fraction

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import patchkit  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
BAK = PAPER.with_suffix(".md.bak-pre-wt108-sec33")

#: §5.4's published per-quarter estimate, exactly as the manuscript prints it.
ALPHA_Q = Fraction(1227, 10_000)
#: §4.4's and §5.4's published annual figure, and §3.2's R1 boundary.
PUBLISHED_YR = Fraction(408, 1000)
R1_FLOOR = Fraction(33, 100)

#: The registered direction, in the words the abstract already uses. One phrase, assembled
#: in one place, so the four sites cannot drift apart the way the six §7 sites did.
DIRECTION = "on both known biases' inflating side"


def gate() -> Fraction:
    """§3.2's annualisation, recomputed in exact rationals from the published cell."""
    alpha_yr = 1 - (1 - ALPHA_Q) ** 4
    rounded = Fraction(round(alpha_yr * 1000), 1000)
    if rounded != PUBLISHED_YR:
        raise SystemExit(
            f"GATE: §3.2's annualisation of §5.4's published α̂_q = {float(ALPHA_Q)} gives "
            f"{float(alpha_yr):.6f} → {float(rounded)}, not the published "
            f"{float(PUBLISHED_YR)}. Nothing written."
        )
    if alpha_yr < R1_FLOOR:
        raise SystemExit(
            f"GATE: α̂_yr = {float(alpha_yr):.4f} is below §3.2's R1 floor of "
            f"{float(R1_FLOOR)}. §3.3 fires only in R1/R2 — the manuscript would be "
            f"RELEASED from the attachment rule, not in breach of it. Nothing written."
        )
    print(f"  gate: α̂_yr = 1 − (1 − {ALPHA_Q})⁴ = {float(alpha_yr):.6f} "
          f"→ {float(PUBLISHED_YR)} published, ≥ {float(R1_FLOOR)} ⇒ regime R1 ✓")
    return alpha_yr


EDITS = [
    (
        PAPER,
        "95% interval [0.383, 0.432]: the calibration used here is low",
        f"95% interval [0.383, 0.432], {DIRECTION}: the calibration used here is low",
        "§4.4 · the estimate carries the direction of the two registered biases",
    ),
    (
        PAPER,
        "**The peak-to-charge recognition rate is 0.41 per year, and the calibration was low",
        f"**The peak-to-charge recognition rate is 0.41 per year {DIRECTION}, and the "
        "calibration was low",
        "§5.4 · the bolded lead — the one line a skimming referee reads",
    ),
    (
        PAPER,
        "**α̂ = 0.408/yr** [0.383, 0.432]; range **0.327–0.499** across every cut",
        f"**α̂ = 0.408/yr** [0.383, 0.432], {DIRECTION}; range **0.327–0.499** across every "
        "cut",
        "§7 · the survivals ledger row",
    ),
    (
        PAPER,
        "against the 0.05 swept through the body, and finds the constant hazard the",
        f"against the 0.05 swept through the body and {DIRECTION}, and finds the constant "
        "hazard the",
        "§9 limitation 4 · the restatement §3.3 forbids exiling the qualifier to",
    ),
]


def main() -> int:
    gate()
    if not BAK.exists():
        shutil.copy2(PAPER, BAK)
        print(f"  backup: {BAK.name}")
    before = PAPER.read_text(encoding="utf-8")
    patchkit.apply_edits(EDITS, expect_structure={})
    after = PAPER.read_text(encoding="utf-8")

    added = len(after) - len(before)
    sites = after.count(DIRECTION)
    print(f"  {DIRECTION!r} now appears at {sites} sites (abstract + 4 repaired)")
    print(f"  +{added} characters, 0 sentences")
    if sites != 5:
        raise SystemExit(f"POST: expected 5 sites, found {sites}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
