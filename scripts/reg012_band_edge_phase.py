"""REG-012 · the band count's own edge-phase question — a description of the heap.

Registered in `docs/preregistration/REG-012-band-count-edge-phase.md` (`ba59370`), alone,
in a commit that carried no code. This file did not exist at that commit.

WHAT THIS COMPUTES, AND WHAT IT REFUSES TO
------------------------------------------
`RESULT-REG-009-band-count-filled` places each tier-0 property event in the D3 bin its
firm's disclosed property life falls in. D3's bins are half-open on the left, so where the
edges sit could decide which side of a boundary an event lands on. Under an edge phase
`s in [0, 1)` the bin index is `floor(v - s) = floor(v) - [frac(v) < s]`, so the entire
edge-phase behaviour of a sample is a function of the multiset of FRACTIONAL PARTS and of
nothing else. That multiset is a description of the heap, and describing it reads no
threshold.

`CONSTRUCTION-REG-009-coverage-fill.md` R5 forbids re-choosing a band edge, width, floor,
tag or interval rule in response to the number. This file therefore reports NO count of
bands, compares NO occupancy to anything, moves NO edge, and reaches NO verdict on §7.5's
decision rule. That refusal is asserted as an ABSENCE by A1 below and by
`tests/test_reg012_band_edge_phase.py`, rather than merely intended -- `-37`'s rule that
the completeness of a list is invisible to every check its correctness passes.

THE TWO DEFECTS THE REGISTRATION FOUND BEFORE THIS FILE EXISTED
---------------------------------------------------------------
§1: the card's premise (55.7 % of lives are integers on a left edge) is Psi_band's
statistic, over 683 pairs x 2 tags x 3 interval rules = 4098 lives. This population is
events, one tag, one rule, one life each. E1 below is the band count's own version of that
number, so the first thing this instrument measures is the sentence that commissioned it.

§2: the card's proposed statistic -- the share of a band's mass within w/2 of an edge --
is 1.000 for every band of every sample, since every point of a half-open band of width w
is within w/2 of its nearer edge. Replaced, not run.
"""

from __future__ import annotations

import ast
import json
import sys
from collections import Counter, defaultdict
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reg009_band_count as bc  # noqa: E402
import reg009_band_count_filled as filled  # noqa: E402
from reg009_ladder_inputs import (  # noqa: E402
    BAND_WIDTH, PRIMARY, Tee, hr, lift_band_rule,
)
from severity import check, summary  # noqa: E402

# ======================================================================================
# REGISTERED CONSTANTS -- every module-level literal in this file, with where it came
# from. A2 parses this file's own AST and refuses anything not on this list. The band
# width, the interval rule, the pick mode, the tag and the bin rule are NOT here: they
# are imported from the instruments that registered them.
# ======================================================================================
REGISTERED_CONSTANTS = {
    "CITED_TABLE": "the cited document's committed table, whose row this run reproduces "
                   "before describing the population behind it (REG-012 §3 P4)",
    "CITED_DOC": "the document the card cites; named so a reader can find the row",
    "READING": "the registered reading, composed from the two instruments' own PRIMARY "
               "and PRIMARY_PICK rather than typed as a string",
    "OUT_JSON": "this run's table",
    "RUN_LOG": "this run's log",
    "REGISTRATION": "the registration, committed alone before this file existed",
    "FORBIDDEN_READS": "A1: the names by which a band count is read in this repository, "
                       "assembled from fragments so the guard cannot match itself",
}

CITED_TABLE = "reg-009-band-count-filled.json"
CITED_DOC = "RESULT-REG-009-band-count-filled.md"
READING = PRIMARY + "|" + bc.PRIMARY_PICK
OUT_JSON = "reg-012-band-edge-phase.json"
RUN_LOG = "RESULT-REG-012-band-edge-phase-run.log"
REGISTRATION = "docs/preregistration/REG-012-band-count-edge-phase.md"

# Assembled from fragments, so that the literal below cannot match the source text of the
# guard that uses it. `-30`'s F9a matched its own witness; any guard whose subject is text
# it is part of has this shape.
FORBIDDEN_READS = ("THIN_" + "FLOOR", "clear_" + "events", "clear_" + "firms",
                   "ceil" + "ings", "band" + "s_clearing")


# ======================================================================================
# PLUMBING
# ======================================================================================
def _here() -> Path:
    return Path(__file__).resolve().parent


def frac(v: float) -> Fraction:
    """The fractional part of a disclosed life, read losslessly.

    `repr` is the shortest decimal string that round-trips to the same float, i.e. the
    number as the artifact wrote it; H3 asserts the round trip for every value, so this
    is a re-reading and not a rounding. Binary subtraction is avoided on purpose: 4.3 - 4
    is 0.2999999999999998 in binary floating point, and a histogram of the heap built on
    that would show two hundred distinct fractional values where the disclosure has a
    dozen -- an artefact of the arithmetic, reported as a property of the sample.
    """
    d = Decimal(repr(v))
    return Fraction(d - int(d))


def grouping(sel: list, shifted: set) -> frozenset:
    """The partition the bins induce on the population -- co-binned sets, IGNORING the
    bins' labels. A grouping, never a count: which events share a bin, not how many bins
    hold how many events."""
    groups: dict = defaultdict(set)
    for i, (_e, _c, v) in enumerate(sel):
        groups[int(Decimal(repr(v)) // 1) - (1 if i in shifted else 0)].add(i)
    return frozenset(frozenset(g) for g in groups.values())


def pieces(fracs: list) -> list:
    """The phase axis, cut into the intervals on which the grouping is constant.

    `S(s) = {i : frac_i < s}` changes only where `s` crosses a distinct fractional value,
    so the grouping is constant on `[0, d_0]` and on each `(d_k, d_k+1]`, with the last
    piece running to 1. Returns (lo, hi, S) with the interval half-open at the LEFT,
    matching the `<` in the bin rule; lengths therefore sum to exactly 1.
    """
    ds = sorted(set(fracs))
    out, prev = [], Fraction(0)
    for d in ds + [Fraction(1)]:
        if d <= prev:
            continue
        out.append((prev, d, {i for i, f in enumerate(fracs) if f < d}))
        prev = d
    return out


# ======================================================================================
# A2 -- NO FREE PARAMETER
# ======================================================================================
def _module_literals(source: str) -> set:
    out = set()
    for node in ast.parse(source).body:
        if not isinstance(node, ast.Assign):
            continue
        try:
            ast.literal_eval(node.value)
        except (ValueError, SyntaxError, TypeError):
            continue
        for t in node.targets:
            if isinstance(t, ast.Name):
                out.add(t.id)
    return out


def unregistered(source: str) -> set:
    return _module_literals(source) - set(REGISTERED_CONSTANTS) - {"REGISTERED_CONSTANTS"}


# ======================================================================================
# MAIN
# ======================================================================================
def main() -> int:
    root = _here().parent
    tee = Tee(root / "docs" / "preregistration" / RUN_LOG)
    sys.stdout = tee
    try:
        return _run(root)
    finally:
        sys.stdout = tee._out
        tee.close()


def _run(root: Path) -> int:
    src_self = Path(__file__).resolve().read_text()
    mid, mid_desc = lift_band_rule()

    hr("REG-012 · THE BAND COUNT'S EDGE-PHASE QUESTION — a description of the heap")
    print("  Registration: " + REGISTRATION + " (committed alone; this file did not "
          "exist at that commit).")
    print("  R5 stands: no edge is moved, no width re-chosen, no threshold read, and no "
          "count of bands appears below.")
    print("  Reading: " + READING + "   ·   bin rule lifted: " + mid_desc)

    # ---- P4 · the cited row, reproduced before the population behind it is described --
    hr("P4 · THE CITED ROW, REPRODUCED BEFORE ITS POPULATION IS DESCRIBED")
    base_idx, base_years = bc.load_lives(root)
    idx, years, _dupes = filled.chronological(base_idx, base_years, root)
    ev = bc.load_events(root, bc.EVENTS_SRC)
    t0 = [e for e in ev if e["tier"] == 0]
    jF = bc.joinable(t0, idx)

    cited = json.loads((root / "data" / CITED_TABLE).read_text())
    rows = bc.profile(bc.bands_for(jF, idx, years, PRIMARY, bc.PRIMARY_PICK, mid))["rows"]
    check("P4 · the joinable population reproduces the cited table's own count",
          len(jF) == cited["events_joinable"],
          witness=lambda: len(jF) + 1 == cited["events_joinable"])
    check("P4b · and the whole " + READING + " row vector reproduces it, band for band "
          "— the population described below is the one the cited table was built from",
          rows == cited["profiles"][READING]["rows"],
          witness=lambda: rows[:-1] == cited["profiles"][READING]["rows"])
    print("    %d events joinable, in %d occupied bins, from %s"
          % (len(jF), len(rows), CITED_DOC))

    # ---- P2 · the lives, from the count's own selection path -------------------------
    hr("P2 · THE LIVES, TAKEN FROM THE COUNT'S OWN SELECTION PATH")
    sel = bc.selected_lives(jF, idx, years, PRIMARY, bc.PRIMARY_PICK)
    check("P2 · every joinable event contributes exactly one life, and the count of them "
          "is bound to the population rather than typed",
          len(sel) == len(jF) and len({id(e) for e, _c, _v in sel}) == len(jF),
          witness=lambda: len(sel) + 1 == len(jF))
    hist_bins: dict = defaultdict(int)
    for _e, _c, v in sel:
        hist_bins[int(Decimal(repr(v)) // 1)] += 1
    check("P2b · binning those lives by the lifted rule rebuilds the cited row exactly, "
          "so these are the values the published table was built from",
          [hist_bins[int(r["band"][0] / BAND_WIDTH)] for r in rows]
          == [r["events"] for r in rows],
          witness=lambda: [hist_bins[int(r["band"][0] / BAND_WIDTH)] for r in rows]
          == [r["events"] + 1 for r in rows])

    # ---- H3 · the fractional parts are re-read, not rounded ---------------------------
    hr("H3 · THE FRACTIONAL PARTS — re-read losslessly, not rounded")
    bad = [v for _e, _c, v in sel if float(Decimal(repr(v))) != v]
    check("H3 · every life round-trips through its own shortest decimal, so the "
          "fractional parts below are the values as written and not a quantisation",
          not bad, witness=lambda: bool(bad) or float(Decimal("0.1")) != 0.1)
    fracs = [frac(v) for _e, _c, v in sel]

    # ---- E1..E3 · the heap ------------------------------------------------------------
    hr("E1-E3 · THE HEAP")
    counts = Counter(fracs)
    on_edge = counts[Fraction(0)]
    modal_frac, modal_n = counts.most_common(1)[0]
    check("E-vac · the histogram accounts for the whole population, so no share below is "
          "computed over a subset this file chose",
          sum(counts.values()) == len(sel),
          witness=lambda: sum(counts.values()) == len(sel) - 1)
    print("    lives sitting exactly on a left edge : %d of %d = %.4f"
          % (on_edge, len(sel), on_edge / len(sel)))
    print("    distinct fractional values           : %d" % len(counts))
    print("    modal fractional value               : %s, %d of %d = %.4f"
          % (modal_frac, modal_n, len(sel), modal_n / len(sel)))
    print("\n    the fractional-part histogram (E3) — every value, with its share:")
    for f, n in sorted(counts.items()):
        print("      %-6s %4d   %.4f" % (str(f), n, n / len(sel)))

    # ---- E4 · phase rigidity ----------------------------------------------------------
    hr("E4 · PHASE RIGIDITY — how much of the phase circle leaves the grouping alone")
    registered = grouping(sel, set())
    ps = pieces(fracs)
    same = [(lo, hi) for lo, hi, S in ps if grouping(sel, S) == registered]
    measure = sum(hi - lo for lo, hi in same)
    widest = max((hi - lo for lo, hi in same), default=Fraction(0))
    contiguous = (bool(ps) and ps[0][0] == Fraction(0) and ps[-1][1] == Fraction(1)
                  and all(a[1] == b[0] for a, b in zip(ps, ps[1:])))
    check("E4-vac · the phase axis is partitioned exactly — contiguous from 0 to 1, "
          "lengths summing to 1 — so the measure below is a share of the whole circle "
          "and not of a window this file chose",
          contiguous and sum(hi - lo for lo, hi, _S in ps) == Fraction(1),
          witness=lambda: sum(hi - lo for lo, hi, _S in ps[:-1]) == Fraction(1))
    # The two ways `grouping` could report rigidity that is not there, both checked on
    # THIS population rather than on a toy: it could be blind to its argument (then every
    # phase looks identical), or it could be keyed on the bins' labels rather than their
    # contents (then no phase ever looks identical). A measure computed by a function
    # that fails either is a number about the function, not about the heap.
    everything = set(range(len(sel)))
    check("E4-blind · shifting EVERY life down one bin leaves the grouping identical — "
          "so this measure reads which events share a bin, not which bin they share",
          grouping(sel, everything) == registered,
          witness=lambda: grouping(sel, everything - {0}) == registered)
    crowded = next((b for b, n in sorted(hist_bins.items()) if n > 1), None)
    one_of_them = next(i for i, (_e, _c, v) in enumerate(sel)
                       if int(Decimal(repr(v)) // 1) == crowded)
    check("E4-alive · shifting ONE life out of a bin that holds others does change the "
          "grouping — so a phase reported as grouping-preserving is a fact about the "
          "sample and not a function that cannot tell",
          crowded is not None and grouping(sel, {one_of_them}) != registered,
          witness=lambda: grouping(sel, set()) != registered)
    # A phase larger than every fractional value present carries the WHOLE heap down one
    # bin, which E4-blind proves preserves the grouping for any sample whatsoever. Such a
    # phase is a relabelling, not a fact about this heap, so the two are reported apart:
    # a rigidity measure that silently included the translation would read as evidence of
    # concentration in a sample that has none.
    top = max(fracs)
    below = sum(hi - lo for lo, hi in same if hi <= top)
    print("    grouping-preserving phases : measure %s = %.4f of the circle"
          % (measure, float(measure)))
    for lo, hi in same:
        print("      (%s, %s]%s" % (lo, hi, "   — the whole heap moves together here; "
              "this interval preserves the grouping of ANY sample" if lo >= top else ""))
    print("    widest single such interval: %s = %.4f" % (widest, float(widest)))
    print("    of that, below the largest fractional value present (%s): %s = %.4f"
          % (top, below, float(below)))
    print("    constant pieces of the phase axis: %d" % len(ps))

    # ---- A1 · the absence -------------------------------------------------------------
    hr("A1 · THE ABSENCE — this run reads no threshold")
    present = [t for t in FORBIDDEN_READS if t in src_self]
    check("A1 · this instrument names none of the ways a band count is read in this "
          "repository — asserted as an ABSENCE, because a list of what a file DOES "
          "contain cannot be shown to be complete",
          not present,
          witness=lambda: not [t for t in FORBIDDEN_READS
                               if t in src_self + FORBIDDEN_READS[0]])
    stray = unregistered(src_self)
    check("A2 · every module-level literal in this file is on the registered list",
          not stray,
          witness=lambda: not unregistered(src_self + "\nSTRAY_LITERAL = 1\n"))

    out = {"registration": REGISTRATION,
           "cited_document": CITED_DOC,
           "cited_table": CITED_TABLE,
           "reading": READING,
           "band_rule": mid_desc,
           "width": BAND_WIDTH,
           "population": len(sel),
           "occupied_bins_reproduced": len(rows),
           "on_a_left_edge": on_edge,
           "on_a_left_edge_share": on_edge / len(sel),
           "distinct_fractional_values": len(counts),
           "modal_fractional_value": str(modal_frac),
           "modal_fractional_share": modal_n / len(sel),
           "histogram": [{"frac": str(f), "n": n, "share": n / len(sel)}
                         for f, n in sorted(counts.items())],
           "phase_pieces": len(ps),
           "grouping_preserving_measure": float(measure),
           "grouping_preserving_widest": float(widest),
           "grouping_preserving_intervals": [[str(lo), str(hi)] for lo, hi in same],
           "largest_fractional_value": str(top),
           "grouping_preserving_below_largest_frac": float(below)}
    (root / "data" / OUT_JSON).write_text(json.dumps(out, indent=1) + "\n")

    return summary("REG-012 band edge phase")


if __name__ == "__main__":
    raise SystemExit(main())
