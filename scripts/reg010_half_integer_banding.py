"""REG-010 — Psi recomputed with D3's bin edges shifted by w/2, beside P3's failure.

WHAT THIS INSTRUMENT IS
-----------------------
`RESULT-REG-009` §4 reported that P3 FAILS: every delta collapsed to its D3 band midpoint
moved Psi by 0.0650 against a registered tolerance of five points. It then attached its own
repair, per charter §2, and priced it before it could become a rescue:

    "A second banding whose bin edges fall on half-integers, so the heap sits at a bin's
     centre and the collapse is a rounding rather than a translation, is the robustness row
     this failure asks for. It costs one function and one run on committed data."

This is that function and that run. It is registered in
`docs/preregistration/REG-010-p3-half-integer-banding.md` (commit f61f75a, alone, before
this file existed) and its construction detail in
`docs/preregistration/CONSTRUCTION-REG-010-edge-convention.md` (commit 8d1245b, also alone,
also before this file existed).

WHAT IT MAY NOT DO, AND WHY THE CODE SAYS SO RATHER THAN THE COMMENTS
--------------------------------------------------------------------
P3 FAILED AS REGISTERED AND THIS FILE DOES NOT RE-SCORE IT. REG-009 is closed. The
registration's §3 fixed BOTH branches of the reading before any number existed, and the
dangerous branch is the flattering one: if the shifted banding lands inside P3's five
points, P3 still fails and the outcome is WORSE for Psi, not better -- it would show the
verdict turning on the edge placement of a nuisance parameter nobody registered.

G2 LIFTS D3's rule through `reg009_ladder_inputs.lift_band_rule()` and DERIVES the shift
from the lifted midpoint rather than retyping a bin index. Both conventions are one-line
reflections of the lifted function:

    shifted(v, w) = mid(v + w/2, w) - w/2        the registered convention (C2)
    mirror(v, w)  = -shifted(-v, w)              priced, never chosen (C4)

That is algebraically the construction document's `binner(v + w/2)` with both edges
retarded by w/2 -- subtracting w/2 from both edges subtracts w/2 from their mean -- and G3
checks the defining property directly rather than trusting the algebra. A source-text guard
refuses this file if a bin index is retyped in it. `-30` learned the matching lesson the
expensive way: a source-text guard whose subject is text it is part of will match ITSELF,
so the pattern below is written with a character class and its witness world is composed
from fragments.

G5 REPRODUCES BEFORE IT EXTENDS. Psi, Psi_band, the 683 pairs, the 665 and 673 admissible
rows and the 428 and 178 distinct pairs are recomputed from the two SHA-pinned cycle files
and compared to the committed record; any disagreement aborts. `-31`'s rule, turned on
`-30`.

G6 EXAMINES THE BAND THE SHIFT CREATES. delta enters the model as 1.0/L, so a life
collapsing to zero makes delta infinite and `adm = (d < alpha)` silently FALSE -- the pair
would leave the admissible set with no line of output saying so, and Psi_band' would be
computed on a denominator Psi_band was not. The registration (C5) declared the handling
before the run: count them, ask whether any would have been admissible otherwise, and
REFUSE the run if any would. Do not exclude the life and do not widen a band.

WHAT IT DOES NOT MEASURE
------------------------
Neither banding is the operator-free one. D3 translates a 55.71 % integer heap by +w/2;
the shift translates a 17.45 % half-integer heap by +w/2 and leaves the integers fixed.
The pair of rows brackets the operator's contribution and neither row is the answer without
one. Every number here is the DISCLOSED delta, never the economic one.

USAGE
-----
    .venv/bin/python scripts/reg010_half_integer_banding.py
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reg009_ladder_inputs import (  # noqa: E402
    ALPHA_HAT, BAND_WIDTH, CYCLES, P3_TOL, PRIMARY, QUALIFIER_MARK, RULES, Tee, hr,
    lift_band_rule, lift_ruler, lives, load_population, measure,
)
from severity import check, summary  # noqa: E402

# ======================================================================================
# REGISTERED CONSTANTS -- every module-level literal in this file, with where it came
# from. G8 parses this file's own AST and refuses anything not on this list. The band
# width, alpha, P3's tolerance, the rules, the cycle labels and the qualifier are NOT
# here: they are imported from the instrument that registered them.
# ======================================================================================
REGISTERED_CONSTANTS = {
    "SHIFT_DIVISOR": "CONSTRUCTION-REG-010 C1: the shift is w/2, fixed by RESULT-REG-009 "
                     "§4's own words ('bin edges fall on half-integers'). Not swept.",
    "COMMITTED": "REG-009's committed record, reproduced before it is extended (G5). "
                 "Read from data/reg-009-result.json's pooled R_MID rows by -36 and "
                 "pinned here so a silent change to that file cannot pass unnoticed.",
    "COMMITTED_SRC": "the committed record G5 reproduces, named rather than re-derived",
    "BIN_RULE_PAT": "G2: the shape a RETYPED bin index would have in this file",
    "TOL": "float comparison tolerance for reproducing a committed number; not a "
           "parameter of any measurement",
    "PROBE_LIVES": "G3/G4's fixed probe points, chosen to exercise integer, half-integer, "
                   "interior and sub-w/2 lives. They are inputs to a property check, not "
                   "to a measurement.",
    "OUT_JSON": "this run's table",
    "RUN_LOG": "this run's log",
}

SHIFT_DIVISOR = 2.0

COMMITTED_SRC = "reg-009-result.json"
COMMITTED = {
    "n": 683,
    "raw_admissible": 665, "raw_psi": 0.6586466165413534, "raw_distinct": 428,
    "band_admissible": 673, "band_psi": 0.7236255572065379, "band_distinct": 178,
    "integer_share": 0.5571010248901903,
}

BIN_RULE_PAT = r"[i]nt\([^)]*//[^)]*\)"
TOL = 1e-9
PROBE_LIVES = (1.0, 2.0, 3.0, 5.0, 4.5, 5.5, 6.5, 12.5, 5.4, 5.6, 3.75, 0.25, 0.5)

OUT_JSON = "reg-010-half-integer-banding.json"
RUN_LOG = "RESULT-REG-010-half-integer-banding-run.log"


# ======================================================================================
# THE SHIFT -- DERIVED FROM THE LIFTED MIDPOINT, TYPED NOWHERE
# ======================================================================================
def shifted_rules(mid):
    """CONSTRUCTION-REG-010 C1 and C4, as two reflections of D3's own lifted midpoint.

    `shifted` advances the argument by w/2 and retards the result by w/2, which is the
    construction document's `[lo - w/2, hi - w/2)` at `binner(v + w/2)`: subtracting w/2
    from both edges subtracts w/2 from their mean. `mirror` reflects `shifted` through
    the origin, which turns the inherited half-open-on-the-left into its half-open-on-the-
    right twin without typing an interval anywhere.

    Neither function knows what a bin index looks like. If D3's shape changes,
    `lift_band_rule()` aborts and both of these are never built.
    """
    def shifted(v, w):
        return mid(v + w / SHIFT_DIVISOR, w) - w / SHIFT_DIVISOR

    def mirror(v, w):
        return -shifted(-v, w)

    return shifted, mirror


def displacement(l0, l1, collapse, w):
    """How far the collapse moves the lives it is applied to. C3 declared this is
    reported so the bracket between the two bandings is quantified rather than asserted."""
    vals = np.concatenate([np.asarray(l0, dtype=float), np.asarray(l1, dtype=float)])
    d = np.array([collapse(v, w) - v for v in vals], dtype=float)
    return {"n": int(d.size), "mean_abs": float(np.abs(d).mean()),
            "max_abs": float(np.abs(d).max()), "fixed_points": int((d == 0.0).sum()),
            "moved_up": int((d > 0).sum()), "moved_down": int((d < 0).sum())}


def zero_band(rows, collapse, w, alpha):
    """C5: the band the shift creates, examined rather than assumed.

    A life collapsing to zero makes 1/L infinite, and `adm = (d < alpha)` is then FALSE
    with no line of output saying so. Returns the count and -- the question that decides
    whether the run may continue -- whether any of them would have been admissible on its
    own raw value.
    """
    hit, admissible_raw = 0, 0
    for r in rows:
        for i in (0, 1):
            for rule in RULES:
                v = float(r[f"L{i}_{rule}"])
                if collapse(v, w) == 0.0:
                    hit += 1
                    if (1.0 / v) < alpha:
                        admissible_raw += 1
    return {"collapsed_to_zero": hit, "would_have_been_admissible": admissible_raw}


# ======================================================================================
# G8 -- NO FREE PARAMETER
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
    root = Path(__file__).resolve().parent.parent
    tee = Tee(root / "docs" / "preregistration" / RUN_LOG)
    sys.stdout = tee
    try:
        return _run(root)
    finally:
        sys.stdout = tee._out
        tee.close()


def _digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _run(root: Path) -> int:
    src_self = Path(__file__).resolve().read_text()
    w = BAND_WIDTH
    before = {p.name: _digest(p)
              for p in sorted((root / "data").glob("reg-009-*.json"))}

    hr("REG-010 · THE HALF-INTEGER-EDGED BANDING — beside P3's failure, not instead of it")
    print("  Registered alone at f61f75a; construction alone at 8d1245b; this instrument")
    print("  did not exist at either commit. P3 failed as registered and is not re-scored")
    print("  here. Both branches of the reading were fixed before this run: a difference")
    print("  INSIDE five points is the WORSE outcome for Psi, not the better one.\n")

    print("F1 · THE RULER IS LIFTED, NOT REBUILT")
    ns = lift_ruler()
    phi = ns["PHI"]
    reps, seed = int(ns["N"]), int(ns["SEED"])
    print(f"  bootstrap replicates and seed are LIFTED from wt088 (N={reps}, "
          f"SEED={seed}); this instrument chooses neither.")

    print("\nF2/F7 · THE POPULATION IS PSI's, AND THE DIGESTS GATE THE READ")
    rows, cyc_arr, cik_arr, tally, firms = load_population(root)
    print(f"    {len(rows)} disclosed pairs — NOT the band count's 133 of 151, which is a "
          f"different instrument on a different unit (see the registration §1).")

    # ---- G2: D3's rule is lifted here, and the shift is derived from it ------------
    print("\nG2 · D3's BINS ARE LIFTED, AND THE SHIFT IS DERIVED FROM THE LIFTED FUNCTION")
    mid, mid_desc = lift_band_rule()
    shifted, mirror = shifted_rules(mid)
    witness_world = "i" + "nt(v " + "// w)"
    check("G2a · no bin index is retyped anywhere in THIS file",
          re.search(BIN_RULE_PAT, src_self) is None,
          witness=lambda: re.search(BIN_RULE_PAT, witness_world) is None)
    check("G2b · the lifted midpoint is still D3's own, at D3's width",
          abs(mid(5.0, w) - 5.5) < TOL and abs(mid(5.99, w) - 5.5) < TOL,
          witness=lambda: abs(mid(5.0, w) - 5.0) < TOL)

    # ---- G3: the shifted rule IS a half-integer-edged banding ----------------------
    print("\nG3 · THE SHIFTED COLLAPSE IS THE CENTRE OF A HALF-INTEGER-EDGED BIN")
    check("G3a · every shifted collapse is an integer multiple of the band width — i.e. "
          "the new bin CENTRES sit where D3's EDGES did",
          all(abs(shifted(v, w) / w - round(shifted(v, w) / w)) < TOL
              for v in PROBE_LIVES),
          witness=lambda: all(abs(mid(v, w) / w - round(mid(v, w) / w)) < TOL
                              for v in PROBE_LIVES))
    check("G3b · every life lies within w/2 of its own shifted collapse — i.e. the value "
          "is IN the bin whose centre it is given",
          all(abs(v - shifted(v, w)) <= w / SHIFT_DIVISOR + TOL for v in PROBE_LIVES),
          witness=lambda: all(abs(v - mid(v, w)) <= TOL for v in PROBE_LIVES))

    # ---- G4: C2's inheritance, realised --------------------------------------------
    print("\nG4 · THE TIE-BREAK IS INHERITED FROM D3's HALF-OPENNESS, NOT CHOSEN")
    ints = tuple(v for v in PROBE_LIVES if abs(v - round(v)) < TOL)
    halves = tuple(v for v in PROBE_LIVES
                   if abs(v * 2 - round(v * 2)) < TOL and abs(v - round(v)) >= TOL)
    check("G4a · an integer life is a FIXED POINT of the shifted collapse — the heap "
          "sits at a bin centre and the collapse is a rounding, which is what §4 asked",
          all(abs(shifted(v, w) - v) < TOL for v in ints),
          witness=lambda: all(abs(mid(v, w) - v) < TOL for v in ints))
    check("G4b · a half-integer life sits on the NEW left edge and is carried UP by w/2 "
          "— the heap is relocated, not removed (C3)",
          all(abs(shifted(v, w) - (v + w / SHIFT_DIVISOR)) < TOL for v in halves),
          witness=lambda: all(abs(shifted(v, w) - (v - w / SHIFT_DIVISOR)) < TOL
                              for v in halves))
    check("G4c · the mirror convention disagrees with the registered one on EXACTLY the "
          "half-integer lives, and nowhere else",
          all((abs(mirror(v, w) - shifted(v, w)) > TOL) == (v in halves)
              for v in PROBE_LIVES),
          witness=lambda: all(abs(mirror(v, w) - shifted(v, w)) < TOL
                              for v in PROBE_LIVES))

    # ---- the heap, measured on the population rather than on probe points ----------
    all_lives = [float(r[f"L{i}_{rule}"]) for r in rows for i in (0, 1) for rule in RULES]
    n_int = sum(1 for v in all_lives if abs(v - round(v)) < TOL)
    n_half = sum(1 for v in all_lives
                 if abs(v * 2 - round(v * 2)) < TOL and abs(v - round(v)) >= TOL)
    share_int, share_half = n_int / len(all_lives), n_half / len(all_lives)
    print(f"    of {len(all_lives)} lives entering the collapse: {n_int} integers "
          f"({share_int:.4f}) and {n_half} half-integers ({share_half:.4f}).")
    print(f"    D3's edges are at the integers, so D3 translates the {share_int:.2%} heap "
          f"by +{w/SHIFT_DIVISOR:.2f} y. The shift's edges are at the half-integers, so "
          f"it translates the {share_half:.2%} heap instead and leaves the other fixed.")

    # ---- G5: reproduce before extending -------------------------------------------
    hr("G5 · REG-009's COMMITTED ROW, REPRODUCED BEFORE IT IS EXTENDED")
    rng = np.random.default_rng(seed)
    order = ("raw", "band", "shifted", "mirror")
    collapse = {"raw": None, "band": mid, "shifted": shifted, "mirror": mirror}
    res: dict = {"registration": "REG-010-p3-half-integer-banding.md",
                 "construction": "CONSTRUCTION-REG-010-edge-convention.md",
                 "band_rule_lifted": mid_desc, "width": w,
                 "shift": w / SHIFT_DIVISOR, "alpha_hat": ALPHA_HAT,
                 "p3_tolerance": P3_TOL, "qualifier": QUALIFIER_MARK,
                 "integer_share": share_int, "half_integer_share": share_half,
                 "psi": {}}
    for sub in ("pooled",) + CYCLES:
        idx = (list(range(len(rows))) if sub == "pooled"
               else [i for i, x in enumerate(cyc_arr) if x == sub])
        for key in order:
            res["psi"][f"{sub}|{PRIMARY}|{key}"] = measure(
                [rows[i] for i in idx], cik_arr[idx], PRIMARY, ALPHA_HAT, phi, rng, reps,
                band=key != "raw", mid=collapse[key])

    p = res["psi"]
    raw, band = p[f"pooled|{PRIMARY}|raw"], p[f"pooled|{PRIMARY}|band"]
    print(f"    committed record read from data/{COMMITTED_SRC}")
    check("G5a · the pair count is REG-009's 683",
          raw["n"] == COMMITTED["n"], witness=lambda: raw["n"] == COMMITTED["n"] + 1)
    check("G5b · Psi reproduces the committed 0.6586 exactly",
          abs(raw["psi"] - COMMITTED["raw_psi"]) < TOL,
          witness=lambda: abs(raw["psi"] - COMMITTED["raw_psi"] - 0.01) < TOL)
    check("G5c · Psi_band reproduces the committed 0.7236 exactly",
          abs(band["psi"] - COMMITTED["band_psi"]) < TOL,
          witness=lambda: abs(band["psi"] - COMMITTED["band_psi"] - 0.01) < TOL)
    check("G5d · both admissible counts and both distinct-pair counts reproduce",
          (raw["n_admissible"], band["n_admissible"], raw["distinct_pairs"],
           band["distinct_pairs"]) == (COMMITTED["raw_admissible"],
                                       COMMITTED["band_admissible"],
                                       COMMITTED["raw_distinct"],
                                       COMMITTED["band_distinct"]),
          witness=lambda: raw["n_admissible"] == COMMITTED["band_admissible"])
    check("G5e · the integer share reproduces RESULT-REG-009 §4's published 55.7 %, "
          "which is how this run knows it is reading Psi's population",
          abs(share_int - COMMITTED["integer_share"]) < TOL,
          witness=lambda: abs(share_half - COMMITTED["integer_share"]) < TOL)

    # ---- G6: the band the shift creates -------------------------------------------
    hr("G6 · THE BAND THE SHIFT CREATES — examined, not assumed (C5)")
    zb = {k: zero_band(rows, collapse[k], w, ALPHA_HAT) for k in ("band", "shifted",
                                                                  "mirror")}
    res["zero_band"] = zb
    for k in ("band", "shifted", "mirror"):
        print(f"    {k:<8} collapsed to zero: {zb[k]['collapsed_to_zero']:>3}   "
              f"of those, admissible on their raw value: "
              f"{zb[k]['would_have_been_admissible']}")
    print(f"    admissibility needs 1/L < {ALPHA_HAT}, i.e. L > "
          f"{1.0/ALPHA_HAT:.2f} y; every zero-collapsing life is below "
          f"{w/SHIFT_DIVISOR:.2f} y.")
    check("G6a · D3's own collapse cannot produce a zero — its leftmost band's centre is "
          "w/2, a legal life. The shift's leftmost band centre is 0, which is not.",
          zb["band"]["collapsed_to_zero"] == 0
          and zb["shifted"]["collapsed_to_zero"] > 0,
          witness=lambda: zb["band"]["collapsed_to_zero"] > 0)
    check("G6b · REFUSAL: no life the shift sends to zero would have been admissible on "
          "its own value, so no pair leaves the admissible set unannounced",
          all(z["would_have_been_admissible"] == 0 for z in zb.values()),
          witness=lambda: all(z["collapsed_to_zero"] == 0 for z in zb.values()))

    # ---- the displacement bracket (C3) ---------------------------------------------
    hr("THE OPERATOR'S OWN CONTRIBUTION — declared in C3, computed here")
    l0, l1 = lives(rows, PRIMARY)
    res["displacement"] = {k: displacement(l0, l1, collapse[k], w)
                           for k in ("band", "shifted", "mirror")}
    for k, d in res["displacement"].items():
        print(f"    {k:<8} mean|Δ| {d['mean_abs']:.4f} y   max|Δ| {d['max_abs']:.4f} y   "
              f"fixed {d['fixed_points']:>4}   up {d['moved_up']:>4}   "
              f"down {d['moved_down']:>4}")
    print("    Neither banding is the operator-free one; the pair brackets the operator.")

    # ---- THE ROW -------------------------------------------------------------------
    hr("THE ROW — Psi under each banding  (" + QUALIFIER_MARK + ")")
    for sub in ("pooled",) + CYCLES:
        print(f"  {sub}")
        for key in order:
            m = p[f"{sub}|{PRIMARY}|{key}"]
            print(f"    {key:<8} n={m['n']:>4} adm={m['n_admissible']:>4} "
                  f"A={m['A']:.4f}  Psi={m['psi']:.4f} "
                  f"[{m['ci_lo']:.4f},{m['ci_hi']:.4f}]  distinct={m['distinct_pairs']:>3} "
                  f" modal={m['modal_share']:.4f}")
    print("  Every row is the DISCLOSED life's band, never the economic one.")

    # ---- THE READING, AS REGISTERED -------------------------------------------------
    hr("THE READING — registration §3, both branches fixed before this run")
    d_band = abs(band["psi"] - raw["psi"])
    d_shift = abs(p[f"pooled|{PRIMARY}|shifted"]["psi"] - raw["psi"])
    d_mirror = abs(p[f"pooled|{PRIMARY}|mirror"]["psi"] - raw["psi"])
    res["deltas"] = {"band": d_band, "shifted": d_shift, "mirror": d_mirror}
    res["inside_p3_tolerance"] = {"band": d_band < P3_TOL, "shifted": d_shift < P3_TOL,
                                  "mirror": d_mirror < P3_TOL}
    print(f"    |Psi_band  - Psi| = {d_band:.4f}   (committed; P3's subject)")
    print(f"    |Psi_band' - Psi| = {d_shift:.4f}   (REG-010, registered convention)")
    print(f"    |Psi_mirror- Psi| = {d_mirror:.4f}   (the mirror, priced, never chosen)")
    print(f"    P3's registered tolerance: {P3_TOL}")
    if d_shift >= P3_TOL:
        print("\n    BRANCH A. The failure is not an artefact of the collapse operator:")
        print("    Psi moves past five points under both edge placements. P3's verdict")
        print("    stands and is better supported; §4's observation about integers on")
        print("    left edges is true but not load-bearing.")
    else:
        print("\n    BRANCH B. P3 STILL FAILS — REG-010 does not re-score it. What this")
        print("    establishes is WORSE for Psi, not better: the verdict turns on the")
        print("    edge placement of a nuisance parameter nobody registered. Psi_band and")
        print("    Psi_band' differ by w/2 of arbitrary offset and by nothing else.")
        print("    No sentence is softened and no verdict is amended.")
    # ---- G7: the mirror differs in DIRECTION ONLY ----------------------------------
    hr("G7 · THE MIRROR MOVES THE LIVES EXACTLY AS FAR, AND THE OTHER WAY")
    ds = np.array([shifted(v, w) - v for v in all_lives], dtype=float)
    dm = np.array([mirror(v, w) - v for v in all_lives], dtype=float)
    disagree = np.abs(ds - dm) > TOL
    is_half = np.array([abs(v * 2 - round(v * 2)) < TOL and abs(v - round(v)) >= TOL
                        for v in all_lives])
    res["direction_only"] = {"lives": int(ds.size),
                             "same_magnitude": bool(np.all(np.abs(np.abs(ds) - np.abs(dm))
                                                           < TOL)),
                             "disagreeing": int(disagree.sum())}
    print(f"    {int(disagree.sum())} of {ds.size} lives are collapsed differently by the "
          f"two conventions, and they are exactly the half-integer lives.")
    check("G7a · the two conventions move every life by the SAME distance — so any Psi "
          "they disagree about is a disagreement about DIRECTION, not about magnitude",
          bool(np.all(np.abs(np.abs(ds) - np.abs(dm)) < TOL)),
          witness=lambda: bool(np.all(np.abs(ds - dm) < TOL)))
    check("G7b · and they disagree on exactly the half-integer lives, over the whole "
          "population rather than over probe points",
          bool(np.array_equal(disagree, is_half)),
          witness=lambda: bool(np.array_equal(disagree, ~is_half)))

    # ---- G8/G9 ----------------------------------------------------------------------
    hr("G8 · NO FREE PARAMETER · G9 · NOTHING COMMITTED IS OVERWRITTEN")
    check("G8 · every module-level literal in this file is registered with a provenance",
          not unregistered(src_self),
          witness=lambda: not unregistered(src_self + "\nSTRAY_KNOB = 0.5\n"))
    print(f"    {len(REGISTERED_CONSTANTS)} registered, {len(unregistered(src_self))} "
          f"unregistered")
    out = root / "data" / OUT_JSON
    after = {p.name: _digest(p) for p in sorted((root / "data").glob("reg-009-*.json"))}
    print(f"    {len(after)} committed REG-009 artifacts under data/, digested before and "
          f"after this run")
    check("G9 · every REG-009 artifact is byte-identical after this run — beside, never "
          "instead of",
          after == before,
          witness=lambda: after == {**before, COMMITTED_SRC: "not-the-digest"})

    out.write_text(json.dumps(res, indent=2) + "\n")
    print(f"\n  wrote data/{OUT_JSON}")
    summary("SEVERITY · REG-010 half-integer-edged banding")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
