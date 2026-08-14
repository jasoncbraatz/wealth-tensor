"""T4 · the continuum is priced in the wrong currency — plus the §4.2 form-independence move.

T4 · WHAT §4.2 SAYS AND WHAT `wt084` PRINTS
--------------------------------------------
§4.2 closes the identification argument with a range:

    Assuming a physical scale of 0.76 implies φ = 0; assuming 1.27 implies φ = 1 ...
    **A factor of 1.67 in the unobserved physical scale spans the entire unit interval of
    timeliness.**

Exactly true, and **incomplete in a way the repository's own run output shows**. `wt084`'s
E7 table prints a second column beside the one the prose quotes: each member of the family
demands its own **opening gap**, and the φ = 0 end requires **g₀ = +0.513** — books opening
more than half again above the physical asset. The family is a freedom in *two* unobserved
quantities, not one, and the second one is a quantity accountants have intuitions about.

Priced in that currency (`docs/scouting/probes/continuum_gap_price.py`, gated on `wt084`'s
printed endpoints before it reports anything new):

    |g₀| ≤ 0.02  → φ ∈ [0.815, 0.881],  6.6% of the unit interval
    |g₀| ≤ 0.05  → φ ∈ [0.765, 0.930], 16.5%
    |g₀| ≤ 0.10  → φ ∈ [0.683, 1.000], 31.7%

**The paper loses nothing by publishing this and gains the argument.** A 32%-wide identified
set on a parameter defined on [0, 1], available at a 10% opening gap no filing discloses, is
still fatal to a cross-sectional ranking of φ — which is all §4.3 and §4.6 need. What it
stops being is *dismissible as an unbounded-freedom artefact*, which is exactly how a referee
disposes of "φ is free" when the price is never quoted. STEELMAN: the claim is right and
under-armed.

The second half of the ticket is an ambiguity, and the drill is CUT rather than caveat. The
continuum is computed on a world that **already opens with g₀ = +0.15** — the shifted map two
paragraphs above — and not on §4.2's own square books, `C(0) = E(0) = E₀`, introduced a page
earlier. A reader running the repository finds that in the run output; a reader who does not
is entitled to assume the square books. One clause fixes it.

THE FREE STEELMAN, UNCARDED BECAUSE IT IS A MOVE AND NOT AN EDIT
-----------------------------------------------------------------
`SCOUT-001` §1.2: the identification bench's residual attack is not *"you rediscovered
flip-flop"* — §4.2 concedes Bateman, Garrett, Kuan–Wright–Duffull, Bellman–Åström and Nerlove
at length, and that concession is the paper's best defensive work. The residual is *"the
theorem is about a filter someone chose, and its reach over accounting is an assumption."*

**The paper has the answer and files it in the wrong room.** §4.3's closing paragraph —
*"Any model in which reporting lag attenuates a physical signal will multiply a timeliness
parameter by an asset-life parameter somewhere, because the observable is a rate times a
duration"* — is the form-independence argument, and it sits at the end of a subsection about
rankings, two pages after the objection it answers. Moved to sit directly under the
observational-equivalence box, it converts *this filter* into *any filter of this kind* at
the moment the reader first doubts it.

Nothing is added and nothing is cut: one paragraph changes rooms, and its opening clause is
re-pointed from §4.3's ranking claim to §4.2's theorem. §4.3 then ends on *"That is why the
standards distinguish them"* — a better last line than the one it had.
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"

#: `wt084` E7's printed endpoints, and the probe's derived widths. Every number below is
#: reproduced by `docs/scouting/probes/continuum_gap_price.py`, which asserts the endpoints
#: against `wt084`'s own output before it reports a width.
G0_AT_PHI_ZERO = "51%"          # +0.513158, rounded down to the nearest per cent
SET_WIDTH_AT_10PCT = "31.7%"    # 0.3174 wide on φ ∈ [0.6826, 1.0000], as a share of [0, 1].
#: Printed as a PERCENTAGE OF THE UNIT INTERVAL rather than as `0.32`, deliberately:
#: `tests/test_restatement_reach.py` pins where each registered figure is restated, and
#: `0.32` is already REG-002's ladder draw in §4.4 and §7. A second, unrelated quantity
#: printed with the same token would pin the collision instead of the restatement — the
#: exact failure that file's NOT_COUNTED list exists to name. The guard caught it; the
#: repair is a better number, since 31.7% is what the probe reports and 0.32 was a rounding.
ANCHOR_GAP = "15%"              # the world the family is actually built around: g₀ = +0.15

#: The paragraph that changes rooms. Held as one literal so the move is auditable as a move:
#: the same bytes come out of §4.3 and go into §4.2, with one clause re-pointed.
FORM_INDEPENDENCE_OLD = """
This is not a defect of the present model. Any model in which reporting lag attenuates a physical
signal will multiply a timeliness parameter by an asset-life parameter somewhere, because the
observable is a rate times a duration. The model's contribution is to make the product explicit
enough to be checked.
"""

FORM_INDEPENDENCE_NEW = """
**And this is not a property of the particular filter.** Any model in which reporting lag attenuates
a physical signal will multiply a timeliness parameter by an asset-life parameter somewhere, because
the observable is a rate times a duration. The model's contribution is to make the product explicit
enough to be checked.
"""

#: The theorem box, re-emitted verbatim: patchkit's WT-090 rule is that an anchor spanning a
#: structural element must put it back, and a `>` block is the closest thing §4.2 has to one.
THEOREM_BOX_TAIL = (
    "> the *identical* reported series. The filter's two roots — the reporting rate and the physical\n"
    "> decay rate — are exchangeable, and the quantity preserved by the exchange is exactly **φδ**.\n"
)

EDITS = [
    # ---- T4a · the family is anchored on an open-gap world, not on the square books -----
    (PAPER,
     "It is free.** Fix a reported series generated at φ = 0.60 and ask what other parameter vectors",  # noqa: E501
     f"It is free.** Fix a reported series generated at φ = 0.60 in a world whose books already open\n"
     f"{ANCHOR_GAP} above the physical asset — the shifted map above, not §4.2's square opening — and ask\n"
     f"what other parameter vectors",
     "§4.2 · CUT the ambiguity about which world the continuum is computed in"),

    # ---- T4b · the second freedom, priced -----------------------------------------------
    (PAPER,
     "unit interval of timeliness.** The reported series is consistent with a firm that recognises",
     f"unit interval of timeliness.** Each member of that family also carries its own opening gap, and\n"
     f"the φ = 0 end requires books opening **{G0_AT_PHI_ZERO} above** the physical asset — the state\n"
     f"impairment accounting exists to prevent. Bounding that gap at ten per cent still leaves an\n"
     f"identified set covering **{SET_WIDTH_AT_10PCT}** of the unit interval, which is fatal to\n"
     f"a cross-sectional ranking and not an artefact of an unbounded freedom. The reported series is\n"
     f"consistent with a firm that recognises",
     "§4.2 · the continuum priced in the opening gap"),

    # ---- the move · out of §4.3 ---------------------------------------------------------
    (PAPER, FORM_INDEPENDENCE_OLD, "\n", "§4.3 · form-independence paragraph out"),

    # ---- the move · into §4.2, under the observational-equivalence box -------------------
    (PAPER, THEOREM_BOX_TAIL, THEOREM_BOX_TAIL + FORM_INDEPENDENCE_NEW,
     "§4.2 · form-independence paragraph in, under the theorem box"),
]


def main() -> int:
    apply_edits(EDITS)
    text = PAPER.read_text(encoding="utf-8")
    flat = " ".join(text.split())

    # Flattened: the paragraph is hard-wrapped differently in its new room, and a raw-text
    # count would report the move as a deletion.
    body = "Any model in which reporting lag attenuates a physical signal"
    if flat.count(body) != 1:
        raise SystemExit(f"wt104: the moved paragraph appears {flat.count(body)} times, not once")

    # It moved, rather than being copied into §4.2 and left in §4.3. §4.2's theorem box ends
    # at the observational-equivalence blockquote; §4.3 ends at the standards sentence.
    box = flat.index("the quantity preserved by the exchange is exactly **φδ**")
    moved = flat.index(body)
    ranking = flat.index("That is why the standards distinguish them.")
    if not box < moved < ranking:
        raise SystemExit("wt104: the paragraph is not between the theorem box and §4.3's close")

    for needed in (f"**{G0_AT_PHI_ZERO} above**", f"**{SET_WIDTH_AT_10PCT}** of the unit interval",
                   f"already open {ANCHOR_GAP} above the physical asset"):
        if needed not in flat:
            raise SystemExit(f"wt104: missing {needed!r}")

    print("wt104 ok · continuum priced in g₀ · form-independence paragraph moved under the box")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
