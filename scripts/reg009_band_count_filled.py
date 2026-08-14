"""REG-009 §7.5's BAND COUNT, RECOMPUTED ON THE COVERAGE-FILLED JOIN.

WHAT THIS INSTRUMENT IS
-----------------------
`-31` ran §7.5's registered count on the two cycles SOURCE-001 §3b measures and got ONE
band clearing the floor of 30. It reported, in `RESULT-REG-009-band-count` §3, that 41 of
the 151 property events could not be binned at all, so the count is a LOWER bound; that a
proportional fill of those 41 lands a second band on 30.2 against a floor of 30; and that
the measurement which replaces both brackets is the coverage fill named in SOURCE-001 §3b's
own "what this does not establish".

This file is that fill, run. The seven intervening cycles were extracted with
`reg009_p0_lifetime_values.py extract` -- the same instrument, the same window translated
by whole years, the same six-zip shape -- and the count is recomputed on all nine.

The construction rules are registered in
`docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md`, in a commit that carries no
number, so `git log --follow` proves they were chosen before the filled count existed.

WHAT IT MAY NOT DO, AND WHY THE CODE SAYS SO
--------------------------------------------
H1 REPRODUCES `-31`'s ROW BEFORE EXTENDING IT, from the same committed inputs through the
same pure functions -- 151 events, 110 joinable, one band clearing. `-31`'s two findings
both came out of reproducing a published table rather than out of its new measurement, and
this is that rule turned on `-31`. If the reproduction disagrees, the run stops.

H2 REFUSES A WINDOW THIS FILL INVENTED. Every filled window must be the committed 2014-15
window translated by a whole number of years; the witness is a window displaced by one day.

H4 KEEPS THE BIN RULE LIFTED. The pattern is IMPORTED from `reg009_band_count` rather than
retyped, so this file cannot contain the literal at all -- `-30`'s self-matching guard
lesson, taken one step further by not writing the subject down twice.

H7 REPORTS THE FILL'S PRICE. A ninefold cycle set gives some already-binned events a NEARER
disclosure, so the join is not only larger, it is partly re-chosen. The change is
decomposed into newly-joinable / moved / unchanged and all three are printed. A filled
count reported as a single number would hide the re-choosing, which is finding 16 -- *a
per-unit average is a claim about the RULE that produced its denominator* -- one level over.

H10 MEASURES THE PARAMETER THE FILL ITSELF CREATED. With two cycles the `near` pick's
tie-break was structurally unreachable, so no registration ever had to name it. With nine
cycles it decides 50 of 133 events -- and the primary count is 1 under the registered
convention and 2 under its mirror. The straddle is the result; it is reported, never
tuned. This is the standing refusal (*never add a free parameter to absorb an objection*)
in its harder form: the parameter arrived as a CONSEQUENCE of the measurement, so the
refusal has to be to spend it rather than to add it.

WHAT IT DOES NOT MEASURE
------------------------
Consecutive windows abut at 09-30 / 10-31, so a fiscal year ending 1-30 October lies in no
window of the series in any year. Widening the window to close the hole would be a
parameter chosen after the fact, so the hole is MEASURED (H8) and left open. And every band
here is still a band of the DISCLOSED life; the fill buys coverage, never the economic
delta.

USAGE
-----
    .venv/bin/python scripts/reg009_band_count_filled.py
"""

from __future__ import annotations

import ast
import datetime as dt
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reg009_band_count as bc  # noqa: E402
from reg009_ladder_inputs import (  # noqa: E402
    BAND_WIDTH, CYCLES, PPE, PRIMARY, RULES, THIN_FLOOR, Tee, hr, lift_band_rule,
)
from severity import check, summary  # noqa: E402

# ======================================================================================
# REGISTERED CONSTANTS -- every module-level literal in this file, with where it came
# from. H12 parses this file's own AST and refuses anything not on this list. The band
# width, the floor, the tags, the interval rules, the two base cycle LABELS, the decision
# rule and the bin-rule pattern are NOT here: they are imported from the instruments that
# registered them.
# ======================================================================================
REGISTERED_CONSTANTS = {
    "BASE_FILES": "the two committed cycle files `-31`'s load_lives pins by digest. Read "
                  "here for their WINDOW metadata only; every record comes through "
                  "bc.load_lives, so the base half of the index cannot drift from `-31`'s",
    "FILL_CYCLES": "the seven intervening cycles, R1: §3b's window translated by whole "
                   "years. Each file is this session's `extract` run, same instrument",
    "FILL_SHA256": "the sha256 of the seven committed fill files, pinned here",
    "PANEL": "REG-006's committed panel, for H8's hole measurement only",
    "TWO_CYCLE_PINS": "-31's committed row, which H1 reproduces before extending it",
    "OUT_JSON": "this run's table",
    "RUN_LOG": "this run's log",
    "REGISTRATION": "the construction rules, committed before this file computed anything",
    "DAY": "one day, for H2's witness and for deriving the inter-window gap",
}

BASE_FILES = {"2014-15": "reg-009-p0-lives-2015.json",
              "2022-23": "reg-009-p0-lives-2023.json"}

FILL_CYCLES = {
    "2015-16": "reg-009-p0-lives-2015-16.json",
    "2016-17": "reg-009-p0-lives-2016-17.json",
    "2017-18": "reg-009-p0-lives-2017-18.json",
    "2018-19": "reg-009-p0-lives-2018-19.json",
    "2019-20": "reg-009-p0-lives-2019-20.json",
    "2020-21": "reg-009-p0-lives-2020-21.json",
    "2021-22": "reg-009-p0-lives-2021-22.json",
}
FILL_SHA256 = {
    "2015-16":
        "9dcfb12c779d828d4e02d09456151521853a622ac795e8d40d40cdc4c77b3d26",
    "2016-17":
        "2fcaa229b279e115fdd0c9a2cbdd79de89216225f9ce6d045fb75b58eaeb54a2",
    "2017-18":
        "c6b7863452129142ad95c9003a77c81c1e5b957f039e1cd4356a11aa417e4f06",
    "2018-19":
        "1ec9a828b4cad40a7126de393f9c4e21ec1f766cd9a4098958add512fd5346df",
    "2019-20":
        "45bdd431ec08b64961fcd907dc547c4da98b9a961f1c7b97b40c01925a91871d",
    "2020-21":
        "4f17b4a7dc42b0159cf1435d69d7f7b6cf1f2f4fe52a49da56303c5d35980e16",
    "2021-22":
        "6f3abbadcebe9132c5ced09c3dcc2f351b0dee7e7e13a9011fcf4d54b96048a0",
}

PANEL = "reg-006-wt092-panel.json"

TWO_CYCLE_PINS = {"events_total": 151, "events_joinable": 110, "clear_primary": 1,
                  "clear_firms": 0, "occupied": 16}

OUT_JSON = "reg-009-band-count-filled.json"
RUN_LOG = "RESULT-REG-009-band-count-filled-run.log"
REGISTRATION = "docs/preregistration/CONSTRUCTION-REG-009-coverage-fill.md"
DAY = 1


# ======================================================================================
# PLUMBING
# ======================================================================================
def _here() -> Path:
    return Path(__file__).resolve().parent


def _digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _window(d: dict) -> tuple:
    return tuple(dt.datetime.strptime(w, "%Y%m%d").date() for w in d["window"])


def load_windows(root: Path) -> dict:
    """Every cycle's window, read from the file's own metadata rather than typed."""
    out = {}
    for cyc, fn in list(BASE_FILES.items()) + list(FILL_CYCLES.items()):
        out[cyc] = _window(json.loads((root / "data" / fn).read_text()))
    return out


def chronological(base_idx: dict, base_years: dict, root: Path,
                  tie_to_later: bool = False) -> tuple:
    """The nine-cycle index, built in CHRONOLOGICAL order.

    `tie_to_later` builds the MIRROR world — the same nine cycles inserted in reverse —
    and exists only so H10 can measure how much the tie-break is worth. It is never used
    to choose an answer; the registered convention is the chronological one (R4), fixed
    before any count existed, and the mirror is reported beside it rather than instead
    of it.

    Order is load-bearing and is therefore a registered choice rather than an accident:
    `pick_cycle`'s `near` mode breaks a tie by dict order, and with nine cycles a tie is
    reachable (an event in 2016 is equidistant from 2015-16 and 2016-17). Inserting
    chronologically makes every tie break to the EARLIER disclosure, and H9 counts how
    often that tie is actually reached rather than assuming it is rare.

    Duplicate (cik, cycle) rows -- a firm that changed its fiscal year end can have two
    firm-years inside one window -- keep the LAST in file order, which is exactly what
    `-31`'s two-cycle index did. The rule is unchanged; the count of rows it decides is
    printed rather than absorbed.

    The BASE half of the index is `-31`'s own, passed in from `bc.load_lives`, so no
    re-read of the two committed files can silently redefine it.
    """
    years = dict(base_years)
    recs: dict = {}
    for cyc, fn in FILL_CYCLES.items():
        d = json.loads((root / "data" / fn).read_text())
        years[cyc] = tuple(int(w[:4]) for w in d["window"])
        recs[cyc] = d["records"]
    idx: dict = defaultdict(dict)
    dupes = 0
    for cyc in sorted(years, key=lambda c: years[c][0], reverse=tie_to_later):
        if cyc in CYCLES:
            for cik, per in base_idx.items():
                if cyc in per:
                    idx[cik][cyc] = per[cyc]
        else:
            for r in recs[cyc]:
                cik = int(r["cik"])
                if cyc in idx[cik]:
                    dupes += 1
                idx[cik][cyc] = r
    return idx, years, dupes


def gaps(wins: dict) -> list:
    """The dates the series cannot reach: between one window's end and the next one's
    start. Derived from the windows themselves, never typed."""
    order = sorted(wins, key=lambda c: wins[c][0])
    out = []
    for a, b in zip(order, order[1:]):
        lo = wins[a][1] + dt.timedelta(days=DAY)
        hi = wins[b][0] - dt.timedelta(days=DAY)
        if lo <= hi:
            out.append((lo, hi))
    return out


def near_ties(events: list, idx: dict, years: dict) -> int:
    """How many events the `near` pick cannot decide on distance alone — i.e. how much
    work the insertion-order tie-break is doing. On two cycles this is structurally zero;
    H10 checks that rather than asserting it."""
    n = 0
    for e in events:
        rr = {c: r for c, r in idx[int(e["cik"])].items() if PPE in r["lives"]}
        if len(rr) < 2:
            continue
        yr = e["q_star"] // bc.QUARTERS_PER_YEAR
        ds = sorted(min(abs(yr - y) for y in years[c]) for c in rr)
        if ds[0] == ds[1]:
            n += 1
    return n


def band_of(events: list, idx: dict, years: dict, rule: str, mode: str, mid) -> dict:
    """event identity -> band index, for the events this index can bin. The band comes
    from the same `bands_for` the published count used; nothing about a band is computed
    here."""
    out = {}
    for b, es in bc.bands_for(events, idx, years, rule, mode, mid).items():
        for e in es:
            out[id(e)] = b
    return out


# ======================================================================================
# H12 -- NO FREE PARAMETER
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

    hr("REG-009 §7.5's BAND COUNT, ON THE COVERAGE-FILLED JOIN")
    print("  " + bc.DECISION_RULE)
    print("  The rule is §7.5's and is not moved here. Construction: " + REGISTRATION)
    print("  R_MIN is not promoted under any outcome of this run (R5).")

    # ---- H1: `-31`'s row, reproduced from the committed inputs --------------------
    hr("H1 · `-31`'s ROW, REPRODUCED BEFORE IT IS EXTENDED")
    base_idx, base_years = bc.load_lives(root)
    ev = bc.load_events(root, bc.EVENTS_SRC)
    t0 = [e for e in ev if e["tier"] == 0]
    j2 = bc.joinable(t0, base_idx)
    p2 = bc.profile(bc.bands_for(j2, base_idx, base_years, PRIMARY, bc.PRIMARY_PICK, mid))
    two = {"events_total": len(t0), "events_joinable": len(j2),
           "clear_primary": p2["clear_events"], "clear_firms": p2["clear_firms"],
           "occupied": p2["occupied"]}
    check("H1 · the two-cycle count reproduces `-31`'s committed row exactly",
          two == TWO_CYCLE_PINS,
          witness=lambda: {**two, "clear_primary": two["clear_primary"] + 1}
          == TWO_CYCLE_PINS)
    print("    " + json.dumps(two))
    committed = json.loads((root / "data" / bc.OUT_JSON).read_text())
    check("H1b · and agrees with the artifact `-31` committed",
          committed["clear_primary"] == two["clear_primary"]
          and committed["events_joinable"] == two["events_joinable"],
          witness=lambda: committed["clear_primary"] == two["clear_primary"] + 1)

    # ---- H2/H3: the fill's inputs -------------------------------------------------
    hr("THE FILL'S INPUTS — seven cycles, no window invented")
    for cyc, fn in FILL_CYCLES.items():
        p = root / "data" / fn
        want = FILL_SHA256.get(cyc)
        check("H3 · " + fn + " is the committed file, by digest",
              want is not None and _digest(p) == want,
              witness=lambda p=p, want=want: hashlib.sha256(
                  p.read_bytes() + b"x").hexdigest() == want)

    idx, years, dupes = chronological(base_idx, base_years, root)
    wins = load_windows(root)
    base_win = wins[CYCLES[0]]

    def translated(w, b) -> bool:
        return ((w[0].month, w[0].day) == (b[0].month, b[0].day)
                and (w[1].month, w[1].day) == (b[1].month, b[1].day)
                and w[1].year - w[0].year == b[1].year - b[0].year)

    bad = [c for c in FILL_CYCLES if not translated(wins[c], base_win)]
    check("H2 · every filled window is the committed 2014-15 window translated by whole "
          "years — this fill invented no window",
          not bad,
          witness=lambda: translated(
              (base_win[0] + dt.timedelta(days=DAY), base_win[1]), base_win))
    for c in sorted(wins, key=lambda c: wins[c][0]):
        print("    %-8s [%s .. %s]%s"
              % (c, wins[c][0], wins[c][1], "   (committed, `-31`'s)"
                 if c in CYCLES else "   (this fill)"))
    print("    duplicate (cik, cycle) rows, last-in-file kept (`-31`'s rule): "
          + str(dupes))

    # The fill's own coverage series, read out of the nine artifacts' tallies. This is
    # P0's rate -- firm-years whose 10-K yielded a PARSED canonical life VALUE -- and it
    # is NOT §3b's rate, which counts a life being TAGGED on a different instrument. The
    # two are one level apart and are never printed as one series: that conflation is
    # exactly finding 16, and REG-009 §5 keeps the error that produced it.
    print("\n    P0's coverage series across the nine cycles (parsed life VALUE per "
          "panel firm-year in window — NOT §3b's tagging rate):")
    series = []
    for c in sorted(wins, key=lambda c: wins[c][0]):
        fn = BASE_FILES.get(c) or FILL_CYCLES[c]
        d = json.loads((root / "data" / fn).read_text())
        n, den = len(d["records"]), d["tally"]["panel_firm_years_in_window"]
        series.append({"cycle": c, "with_a_life": n, "panel_firm_years": den,
                       "rate": round(n / den, 3)})
        print("      %-8s %3d / %3d = %.3f%s"
              % (c, n, den, n / den, "   (committed)" if c in CYCLES else ""))
    res_series = series

    # ---- H8: what the window shape cannot reach ------------------------------------
    hr("H8 · WHAT THE SERIES CANNOT REACH — the October gap, measured not closed")
    gs = gaps(wins)
    panel = json.loads((root / "data" / PANEL).read_text())
    fy = {int(f["cik"]): [r["fy_end"] for r in f.get("rows", []) if r.get("fy_end")]
          for f in panel}

    def _d(s):
        return dt.datetime.strptime(s, "%Y-%m-%d").date()

    in_gap = [(c, d) for c, ds in fy.items() for d in ds
              if any(lo <= _d(d) <= hi for lo, hi in gs)]
    gap_firms = {c for c, _ in in_gap}
    t0_firms = {int(e["cik"]) for e in t0}
    check("H8 · the series leaves one gap between every pair of consecutive windows, and "
          "this run reports it rather than widening the window to remove it",
          len(gs) == len(wins) - 1 and len({(hi - lo).days for lo, hi in gs}) == 1,
          witness=lambda: len(gs) == len(wins))
    print("    %d inter-window gaps, each %d days (1-30 October, every year)."
          % (len(gs), (gs[0][1] - gs[0][0]).days + DAY))
    print("    %d panel firm-years across %d firms fall in a gap; %d of those firms own a "
          "tier-0 property event."
          % (len(in_gap), len(gap_firms), len(gap_firms & t0_firms)))

    # ---- THE FILLED COUNT ----------------------------------------------------------
    hr("THE FILLED COUNT — 1.00-year property bands clearing " + str(THIN_FLOOR))
    jF = bc.joinable(t0, idx)
    check("H5 · the filled join is a SUPERSET of the two-cycle one — the fill adds "
          "coverage and removes none",
          {id(e) for e in j2} <= {id(e) for e in jF},
          witness=lambda: {id(e) for e in j2} | {DAY} <= {id(e) for e in jF})
    check("H6 · the fill does not move the 151",
          len(t0) == TWO_CYCLE_PINS["events_total"],
          witness=lambda: len(t0) + 1 == TWO_CYCLE_PINS["events_total"])

    res: dict = {"registration": REGISTRATION,
                 "decision_rule": bc.DECISION_RULE, "band_rule": mid_desc,
                 "floor": THIN_FLOOR, "width": BAND_WIDTH,
                 "cycles": sorted(years, key=lambda c: years[c][0]),
                 "two_cycle": {**two, "profile": p2},
                 "events_total": len(t0), "events_joinable": len(jF),
                 "duplicate_cik_cycle_rows": dupes,
                 "p0_coverage_series": res_series,
                 "october_gap": {"gaps": len(gs), "panel_firm_years": len(in_gap),
                                 "firms": len(gap_firms),
                                 "firms_owning_a_tier0_event":
                                     len(gap_firms & t0_firms)},
                 "profiles": {}}
    for rule in RULES:
        for mode in bc.PICK_MODES:
            res["profiles"][rule + "|" + mode] = bc.profile(
                bc.bands_for(jF, idx, years, rule, mode, mid))
    for rule in RULES:
        print("\n  " + rule + ("  (PRIMARY)" if rule == PRIMARY else ""))
        for mode in bc.PICK_MODES:
            pr = res["profiles"][rule + "|" + mode]
            print("    %-6s %2d occupied bands · %d clear %d EVENTS · %d clear %d FIRMS "
                  "· %d clear in BOTH universes"
                  % (mode, pr["occupied"], pr["clear_events"], THIN_FLOOR,
                     pr["clear_firms"], THIN_FLOOR, pr["clear_events_both_universes"]))

    prim = res["profiles"][PRIMARY + "|" + bc.PRIMARY_PICK]
    print("\n  " + PRIMARY + " / " + bc.PRIMARY_PICK
          + " — the FILLED profile, with `-31`'s two-cycle row beside it:")
    b2 = {tuple(r["band"]): r for r in p2["rows"]}
    for r in prim["rows"]:
        was = b2.get(tuple(r["band"]))
        mark = "  <== clears" if r["events"] >= THIN_FLOOR else ""
        print("      [%5.2f, %5.2f)  events %3d (was %3s)  firms %3d (was %3s)  "
              "(pilot %3d / repl %3d)%s"
              % (r["band"][0], r["band"][1], r["events"],
                 was["events"] if was else "-", r["firms"], was["firms"] if was else "-",
                 r["pilot"], r["replication"], mark))

    check("H11 · every joinable event lands in exactly one band, and none is lost",
          sum(r["events"] for r in prim["rows"]) == len(jF),
          witness=lambda: sum(r["events"] for r in prim["rows"]) == len(jF) + 1)

    # ---- H7: the fill's price ------------------------------------------------------
    hr("H7 · THE FILL'S PRICE — the join is not only larger, it is partly RE-CHOSEN")
    was_b = band_of(j2, base_idx, base_years, PRIMARY, bc.PRIMARY_PICK, mid)
    now_b = band_of(jF, idx, years, PRIMARY, bc.PRIMARY_PICK, mid)
    newly = [e for e in jF if id(e) not in was_b]
    moved = [e for e in jF if id(e) in was_b and was_b[id(e)] != now_b[id(e)]]
    same = [e for e in jF if id(e) in was_b and was_b[id(e)] == now_b[id(e)]]
    still = [e for e in t0 if id(e) not in now_b]
    check("H7 · the three parts and the residual partition the 151 exactly",
          len(newly) + len(moved) + len(same) + len(still) == len(t0),
          witness=lambda: len(newly) + len(moved) + len(same) + len(still) + 1
          == len(t0))
    print("    newly joinable   %3d events / %2d firms   (the fill's GAIN)"
          % (len(newly), len({e["cik"] for e in newly})))
    print("    moved band       %3d events / %2d firms   (a NEARER disclosure now "
          "supplies the life — the fill's PRICE)"
          % (len(moved), len({e["cik"] for e in moved})))
    print("    unchanged        %3d events" % len(same))
    print("    still unjoined   %3d events / %2d firms   (out of reach in all nine "
          "cycles)" % (len(still), len({e["cik"] for e in still})))
    res["decomposition"] = {"newly_joinable": len(newly), "moved": len(moved),
                            "unchanged": len(same), "still_unjoined": len(still)}
    if moved:
        print("    the moves, band before -> after (each is a re-choosing, not a gain):")
        mv: dict = defaultdict(int)
        for e in moved:
            mv[(was_b[id(e)], now_b[id(e)])] += 1
        for (a, b), n in sorted(mv.items()):
            print("      [%d, %d) -> [%d, %d)   %d event(s)" % (a, a + 1, b, b + 1, n))

    # ---- H10: the parameter the FILL created, measured before it is trusted ---------
    hr("H10 · THE TIE-BREAK — a free parameter the FILL created, and it straddles the "
       "floor")
    ties_f = near_ties(jF, idx, years)
    ties_2 = near_ties(j2, base_idx, base_years)
    check("H10a · the near-pick tie was UNREACHABLE on two cycles and is reachable on "
          "nine — no prior registration could have stated this convention",
          ties_2 == 0 and ties_f > 0,
          witness=lambda: ties_2 > 0)
    print("    two cycles : %d of %d joinable events hit a tie (%d had a life in both "
          "cycles at all)"
          % (ties_2, len(j2), sum(1 for e in j2 if sum(
              PPE in r["lives"] for r in base_idx[int(e["cik"])].values()) > 1)))
    print("    nine cycles: %d of %d joinable events hit a tie" % (ties_f, len(jF)))

    idx_l, years_l, _ = chronological(base_idx, base_years, root, tie_to_later=True)
    mirror = bc.profile(bc.bands_for(bc.joinable(t0, idx_l), idx_l, years_l,
                                     PRIMARY, bc.PRIMARY_PICK, mid))
    check("H10b · the registered tie-break and its mirror are computed on the SAME "
          "joinable population — the convention moves bands, never coverage",
          sum(r["events"] for r in mirror["rows"]) == len(jF),
          witness=lambda: sum(r["events"] for r in mirror["rows"]) == len(jF) + 1)
    print("    registered (tie -> EARLIER disclosure): %d band(s) clear %d"
          % (prim["clear_events"], THIN_FLOOR))
    print("    mirror     (tie -> LATER   disclosure): %d band(s) clear %d"
          % (mirror["clear_events"], THIN_FLOOR))
    straddle = (prim["clear_events"] >= 2) != (mirror["clear_events"] >= 2)
    print("    §7.5's threshold is %s by the tie-break alone."
          % ("CROSSED" if straddle else "not crossed"))
    res["near_pick_ties"] = {"two_cycle": ties_2, "filled": ties_f,
                             "registered_clear": prim["clear_events"],
                             "mirror_clear": mirror["clear_events"],
                             "straddles_the_floor": straddle,
                             "mirror_rows": mirror["rows"]}

    # ---- the residual ceiling ------------------------------------------------------
    hr("THE RESIDUAL — what is STILL out of reach")
    ceil = bc.ceilings(prim["rows"], len(still))
    res["ceilings"] = ceil
    print("  %d joined · %d still unjoined · a complete fill of the residual would scale "
          "each band by %.3f"
          % (ceil["joined"], ceil["unjoined"], ceil["proportional_scale"]))
    print("  ADVERSARIAL  — at most %d bands could clear."
          % ceil["adversarial_max_bands"])
    print("  PROPORTIONAL — %d bands clear (%s)."
          % (ceil["proportional_bands"],
             ", ".join("%.1f" % x for x in ceil["proportional_counts"])))
    print("  `-31`'s brackets, on 41 unjoined: adversarial %d, proportional %d — those "
          "were the estimates THIS run replaces."
          % (committed["ceilings"]["adversarial_max_bands"],
             committed["ceilings"]["proportional_bands"]))

    # ---- THE VERDICT ---------------------------------------------------------------
    hr("§7.5's DECISION RULE, APPLIED TO THE FILLED COUNT")
    res["clear_primary"] = prim["clear_events"]
    res["design_survives"] = prim["clear_events"] >= 2
    print("  Two-cycle (`-31`, stands): %d band(s) clear %d events under %s / %s."
          % (p2["clear_events"], THIN_FLOOR, PRIMARY, bc.PRIMARY_PICK))
    print("  Coverage-filled (this run): %d band(s) clear." % prim["clear_events"])
    print("  §7.5: fewer than two -> the expensive half arrives. VERDICT ON THE FILLED "
          "POPULATION: " + ("the design is supported on the sample §4.7 runs on."
                            if res["design_survives"]
                            else "REG-011 still needs the new universe."))
    print("  In the floor's NATIVE unit — §3b counts FIRM-years — %d band(s) clear."
          % prim["clear_firms"])
    print("  By interval rule (filled): "
          + ", ".join("%s %d" % (r, res["profiles"][r + "|" + bc.PRIMARY_PICK]
                                 ["clear_events"]) for r in RULES)
          + ".  R_MIN is NOT promoted (R5).")
    print("  By cycle pick (filled, " + PRIMARY + "): "
          + ", ".join("%s %d" % (m, res["profiles"][PRIMARY + "|" + m]["clear_events"])
                      for m in bc.PICK_MODES)
          + ".  `-31` reported all three AGREEING at 1; on the filled join they do not.")
    print("  And the primary pick's own tie-break moves it: registered %d, mirror %d."
          % (prim["clear_events"], mirror["clear_events"]))
    print("  THE REGISTERED READING IS THE ONLY ONE THAT GIVES %d. That is reported as "
          "the strength it has, not as the strength the rule's binary suggests."
          % prim["clear_events"])
    print("  Every band above is a band of the DISCLOSED life. The economic delta is "
          "unmeasured here and the fill does not touch it.")

    # ---- H4/H12 --------------------------------------------------------------------
    hr("H4/H12 · THE GUARDS ON THIS FILE ITSELF")
    witness_world = "bands[" + "int(v " + "// w)" + "].append(v)"
    check("H4 · the bin rule appears nowhere in THIS file as a literal (the pattern is "
          "imported, so its subject is never written down twice)",
          re.search(bc.BIN_RULE_PAT, src_self) is None,
          witness=lambda: re.search(bc.BIN_RULE_PAT, witness_world) is None)
    extra = unregistered(src_self)
    check("H12 · every module-level literal in this file is registered with a provenance",
          not extra,
          witness=lambda: bool(unregistered(src_self + "\nSTRAY_KNOB = 0.5\n")) is False)
    print("    " + str(len(REGISTERED_CONSTANTS)) + " registered, "
          + str(len(extra)) + " unregistered")

    (root / "data" / OUT_JSON).write_text(json.dumps(res, indent=2) + "\n")
    print("\n  wrote data/" + OUT_JSON)
    summary("SEVERITY · REG-009 §7.5 band count, coverage-filled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
