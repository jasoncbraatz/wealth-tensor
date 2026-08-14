"""T3 · the domain rescue is stated at one α, and `REG-003` registered the cut that moves it.

THE FINDING (`SCOUT-001` T3, re-measured here)
----------------------------------------------
§4.4 closes on a reversal: the calibration was low by an order of magnitude, so the
asserted rectangle *"lies inside the domain after all,"* and **0.974** of the 683 disclosed
pairs with it. Both numbers are right at α̂ = 0.408.

`REG-003` registered, in advance, the cut that would break it: drop the 175 events charged
one quarter after the peak — *"the mass where the onset bridge is least credible"* — which
gives **α̂ = 0.327**. §5.4 reports that number and compares it to **0.05**, where it wins by
an order of magnitude. **The comparison the domain claim needs is against 0.3333**, the
decay rate implied by the three-year life at the fast end of the rectangle, and §4.4 states
that threshold itself four lines above: *"all of it above α = 0.33."*

    0.327 < 0.3333.

At the paper's own registered adverse cut the asserted rectangle is **not** fully inside the
domain, and the sample falls out of `REG-003` §3.2's **R1** into **R2**, whose pre-committed
language is *"the domain sentence stands but is much narrower than written."*

WHICH UNCERTAINTY BITES, WHICH IS THE PART WORTH PRINTING
----------------------------------------------------------
*Sampling* uncertainty is harmless here: at the 95% lower bound of 0.383 the admissible
share is **0.959** and the rectangle is comfortably inside. It is **bridge** uncertainty
that moves the claim — and bridge uncertainty is what `REG-003` §3.3 registered, before the
number existed, as running in the paper-flattering direction. A robustness cut checked
against the benchmark that flatters it (0.05) rather than against the boundary the *claim*
needs (0.3333) is the general failure whenever an instrument is repurposed; §5.4's own
sentence makes exactly that comparison.

WHY THIS IS A STEELMAN AND NOT A CONCESSION
--------------------------------------------
A number replaces an assertion, so the defensive-sentence count falls or holds (charter §2;
`defensive_count.py` matches none of the prose below). And it converts the paper's
weakest-looking move — a domain restriction rescued by the paper's own new measurement —
into its most disciplined one: **the rescue was tested against the cut the registration
nominated in advance as the one that would break it, and here is how far it bends.**

THE COLUMN IS BUILT, NOT TYPED, AND THE GATE IS THE PAPER'S OWN TWO COLUMNS
----------------------------------------------------------------------------
`R(φ, δ, α) = (1 − φ)δ / (α − δ)` is evaluated here for all three rates, and the two rates
the manuscript already prints are **asserted against the manuscript's own published cells
before the third is written**. An ungated probe published +0.316 for a quantity `wt084`
prints as +0.513 in this project last session; the rule that caught it is that every probe
gates on a number the paper already publishes. Same rule, same session, applied to an edit.

BUG SPRAY, FOUND BY THE GATE ITSELF: ONE CELL IS A FLOAT ARTEFACT
------------------------------------------------------------------
The gate refused on its first cell. §4.4 prints **0.2999** for tier 0 at the calibration;
the value is `(1/5)(3/100) / (1/20 − 3/100)` = **3/10**, exactly, in rationals. `0.05 − 0.030`
is `0.020000000000000004` in binary floating point, the quotient comes out
`0.29999999999999993`, and something in the chain that first produced this cell — the
literal is typed into `scripts/wt092_edits_44.py`, so the arithmetic predates the manuscript
— **truncated rather than rounded**, printing a number one unit-in-the-last-place below the
exact one. The repository already knows this exact hazard: `scripts/reg012_band_edge_phase.py`
carries a comment about `4.3 − 4` being `0.2999999999999998`, and `RESULT-REG-012` §4 makes
the same point in prose. It was known in the band-count instrument and not applied to a
published table.

So every cell below is computed in `fractions.Fraction`, where `0.05 − 0.030` is `1/50` and
nothing is one ulp below anything, and the cell is corrected to **0.3000** in the same pass.
`wt092_edits_44.py` is NOT edited: it is the record of an edit that happened, and a record
rewritten to match the present is not a record.
"""
from __future__ import annotations

import itertools
import pathlib
import sys
from fractions import Fraction as F

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"

#: Exact rationals, never floats: `0.05 - 0.030` is `1/50` here and `0.020000000000000004`
#: in binary, and one published cell already carries the difference.
CALIBRATED = F(5, 100)
MEASURED = F(408, 1000)
#: `REG-003` §3.3's registered adverse cut: α̂ with the 175 one-quarter events dropped.
ADVERSE = F(327, 1000)

#: (label, φ, δ, R at the calibration as PRINTED, R at the measured rate as PRINTED).
#: The last two are the gate: they come out of the manuscript, not out of this file.
TIERS = [
    ("0 · property, plant and equipment", F(80, 100), F(30, 1000), "0.2999", "0.0159"),
    ("1 · finite-lived intangibles",      F(60, 100), F(20, 1000), "0.2667", "0.0206"),
    ("2 · indefinite-lived intangibles",  F(40, 100), F(10, 1000), "0.1500", "0.0151"),
    ("3 · goodwill",                      F(20, 100), F(2, 1000),  "0.0333", "0.0039"),
]

#: The one cell where the manuscript and exact arithmetic disagree, declared rather than
#: silently overwritten: tier 0 at the calibration is 3/10, printed as a truncated 0.2999.
KNOWN_TYPO = {("0 · property, plant and equipment", CALIBRATED): ("0.2999", "0.3000")}


def R(phi: F, delta: F, alpha: F) -> F:
    """The deferral measure, exactly. Defined only for δ < α — which is the whole ticket."""
    if delta >= alpha:
        raise ValueError(f"outside the domain: δ={delta} ≥ α={alpha}")
    return (1 - phi) * delta / (alpha - delta)


def q(x: F) -> str:
    """Four decimals, rounded half-up from the exact rational. No float ever appears."""
    scaled = x * 10000
    n = scaled.numerator // scaled.denominator
    if 2 * (scaled - n) >= 1:
        n += 1
    return f"{n // 10000}.{n % 10000:04d}"


def kendall_tau(values: list[F]) -> float:
    """τ of the tabulated order against the predicted (rising) one."""
    pairs = list(itertools.combinations(range(len(values)), 2))
    con = sum(1 for i, j in pairs if values[j] > values[i])
    return (con - (len(pairs) - con)) / len(pairs)


def gate() -> list[str]:
    """Reproduce both published columns, or write nothing."""
    for label, phi, delta, r_cal, r_meas in TIERS:
        for alpha, printed in ((CALIBRATED, r_cal), (MEASURED, r_meas)):
            got = q(R(phi, delta, alpha))
            if got == printed:
                continue
            fix = KNOWN_TYPO.get((label, alpha))
            if fix and fix == (printed, got):
                print(f"wt103 gate · declared correction · {label} at α={float(alpha)}: "
                      f"manuscript {printed} → exact {got}  (= {R(phi, delta, alpha)})")
                continue
            raise SystemExit(
                f"wt103 GATE FAILED · {label} at α={float(alpha)}: computed {got}, "
                f"manuscript prints {printed}. The formula or the table has moved; "
                f"nothing was written.")
    tau_meas = kendall_tau([R(phi, delta, MEASURED) for _, phi, delta, _, _ in TIERS])
    if round(tau_meas, 2) != -0.67:
        raise SystemExit(f"wt103 GATE FAILED · τ at the measured rate is {tau_meas}, "
                         f"manuscript prints −0.67")
    adverse = [R(phi, delta, ADVERSE) for _, phi, delta, _, _ in TIERS]
    tau_adv = kendall_tau(adverse)
    if round(tau_adv, 2) != -0.67:
        raise SystemExit(f"wt103 · τ at the adverse cut is {tau_adv}; the prose below says "
                         f"it is unchanged at −0.67. Fix the prose, not this check.")
    print(f"wt103 gate ok · both published columns reproduced · "
          f"τ = {tau_meas:+.2f} measured, {tau_adv:+.2f} adverse")
    return [q(a) for a in adverse]


ADV = gate()

#: The corrected calibration column, after the declared repair.
CAL = [KNOWN_TYPO.get((t[0], CALIBRATED), (None, t[3]))[1] for t in TIERS]


def row(i: int) -> str:
    label, phi, delta, _, r_meas = TIERS[i]
    return (f"| {label} | {float(phi):.2f} | {float(1 - phi):.2f} | {float(delta):.3f} "
            f"| {float((1 - phi) * delta):.5f} "
            f"| **{CAL[i]}** | **{r_meas}** | **{ADV[i]}** |")


#: The four `R at a common δ` cells, untouched: they are the design's own world and the
#: adverse cut has nothing to say about them.
COMMON = ["0.1333", "0.2667", "0.4000", "0.5333"]

EDITS = [
    # ---- the table: one column, four cells, built above ---------------------------------
    (PAPER,
     "| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** at α = 0.05, the calibration | **R** at α̂ = 0.408, measured (§5.4) | R at a common δ |",  # noqa: E501
     "| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** at α = 0.05, the calibration | **R** at α̂ = 0.408, measured (§5.4) | **R** at α̂ = 0.327, the registered adverse cut | R at a common δ |",  # noqa: E501
     "§4.4 table · header"),
    (PAPER,
     "|---|---|---|---|---|---|---|---|",
     "|---|---|---|---|---|---|---|---|---|",
     "§4.4 table · separator"),
] + [
    (PAPER,
     f"| {TIERS[i][0]} | {float(TIERS[i][1]):.2f} | {float(1 - TIERS[i][1]):.2f} "
     f"| {float(TIERS[i][2]):.3f} | {float((1 - TIERS[i][1]) * TIERS[i][2]):.5f} "
     f"| **{TIERS[i][3]}** | **{TIERS[i][4]}** | {COMMON[i]} |",
     f"{row(i)} {COMMON[i]} |",
     f"§4.4 table · tier {i}")
    for i in range(4)
] + [
    # ---- the τ sentence: the ordering does not move at the adverse cut ------------------
    (PAPER,
     "Kendall τ = **−1** at the calibrated rate, and **−0.67** at the",
     "Kendall τ = **−1** at the calibrated rate, and **−0.67** at both the",
     "§4.4 · τ, first half"),
    (PAPER,
     "measured one, where the first rung alone turns over; the rung that separates them is identified",  # noqa: E501
     "measured rate and the registered adverse cut, where the first rung alone turns over; the rung\n"
     "that separates them is identified",
     "§4.4 · τ, second half"),

    # ---- the domain claim: a range replacing a flat assertion ---------------------------
    (PAPER,
     "[0.383, 0.432]: the calibration used here is low by an order of magnitude, the asserted rectangle",  # noqa: E501
     "[0.383, 0.432]: the calibration used here is low by an order of magnitude, and the asserted rectangle",  # noqa: E501
     "§4.4 · domain sentence, lead"),
    (PAPER,
     "lies inside the domain after all, and so do **0.974** of the 683 disclosed pairs. The domain",
     "lies inside the domain at the measured rate and across its 95% interval, where **0.974** of\n"
     "the 683 disclosed pairs are admissible and **0.959** at the interval's lower bound. At the cut\n"
     "REG-003 registered in advance as the one that would break it — the 175 events charged one\n"
     "quarter after the peak dropped, giving **0.327** — the rectangle's own fastest disclosed rate\n"
     "of 0.3333 is no longer cleared, and **0.814** of the pairs remain admissible. The domain",
     "§4.4 · the adverse cut, against the boundary the claim needs rather than the one that flatters it"),  # noqa: E501
    (PAPER,
     "restriction is a property of the calibration and not\nof the disclosure.",
     "restriction is a property of the calibration and not of the disclosure, and what its remaining\n"
     "margin turns on is the onset bridge rather than the sample.",
     "§4.4 · which uncertainty bites"),

    # ---- the abstract: the qualification has to travel ----------------------------------
    (PAPER,
     "side**, so the disclosed lives lie inside the model's domain,",
     "side**, so the disclosed lives lie inside the model's domain — 0.97 of the disclosed pairs at\n"
     "that rate and 0.81 at the registered adverse cut —",
     "abstract · the same range, because a qualification that does not travel is the defect"),
]


def main() -> int:
    apply_edits(EDITS)
    flat = " ".join(PAPER.read_text(encoding="utf-8").split())
    if "lies inside the domain after all" in flat:
        raise SystemExit("wt103: the flat domain assertion survives")
    for needed in ("0.814", "0.3333 is no longer cleared", "0.81 at the registered adverse cut"):
        if needed not in flat:
            raise SystemExit(f"wt103: missing {needed!r}")
    for i, v in enumerate(ADV):
        if f"**{v}**" not in flat:
            raise SystemExit(f"wt103: tier {i}'s adverse-cut cell {v} is not in the table")
    if "**0.2999**" in flat:
        raise SystemExit("wt103: the truncated 0.2999 cell survives")
    print("wt103 ok · adverse-cut column live, flat assertion gone, abstract mirrors §4.4")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
