"""REG-009 §7.5's TEE-UP, RUN — how many 1.00-year property bands clear the floor of 30.

WHAT THIS INSTRUMENT IS
-----------------------
§7.5 of `REG-009-p3-lifetime-sourced-delta.md` priced paper III §4.7's proposed design --
"compares timeliness only within a life band" -- and left one quantity uncounted, with the
procedure and the decision rule both written down before any number existed:

    "join `reg-006-ladderC-events-corrected.json`'s 151 property events to the disclosed
     lives, bin them at D3's 1.00-year width, and count how many bands clear 30. That is
     one afternoon on committed data and no new harvest -- the cheap half. Only if fewer
     than two bands clear does the expensive half arrive."

This file is that afternoon. The decision rule is §7.5's, quoted above and pinned in
`DECISION_RULE`; it is not this file's to move once the count is seen.

WHAT IT MAY NOT DO, AND WHY THE CODE SAYS SO RATHER THAN THE COMMENTS
--------------------------------------------------------------------
G3 LIFTS D3's bins through `reg009_ladder_inputs.lift_band_rule()`, which lifts them in
turn out of `reg009_p0_lifetime_values.py` at run time. Nothing about a band is typed
here, and a source-text guard refuses this file if the bin rule reappears in it as a
literal. `-30` learned the matching lesson the expensive way: a source-text guard whose
subject is text it is part of will match ITSELF, so the pattern below is written with
single-character classes and its witness world is composed from fragments.

G4-G7 REPRODUCE §7.5's OWN TABLE BEFORE EXTENDING IT. Every cell of that table was
computed by an uncommitted probe; until this file ran, the published counts -- 151 events,
98 firms, 110 joinable -- had no instrument behind them. Reproducing them is the cheapest
possible check that the join key here is the join key there, and it caught two errata that
a fresh count alone would have silently replaced (G6, G7).

G10 asks the instrument-artefact question of a count that SETTLES AN ARGUMENT: a firm that
discloses a property life in BOTH of SOURCE-001's cycles has two lives and one event, so
something has to choose. The choice is made three ways and the answer is reported under
all three, because a verdict that depends on which of two disclosures you read is a
verdict about the reader.

WHAT IT DOES NOT MEASURE
------------------------
Only 110 of the 151 events can be binned at all: the other 41 belong to firms with no
canonical property life in either cycle. A count on a population the instrument could not
reach is a LOWER bound on the count a coverage fill would produce, never evidence of
absence -- so the ceiling under a complete fill is computed two ways (adversarial and
proportional) and printed beside the count rather than left for a reader to worry about.

USAGE
-----
    .venv/bin/python scripts/reg009_band_count.py
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reg009_ladder_inputs import (  # noqa: E402
    BAND_WIDTH, CYCLES, FIN, LIVES_SHA256, PPE, PRIMARY, RULES, THIN_FLOOR,
    Tee, hr, lift_band_rule,
)
from severity import check, summary  # noqa: E402

# ======================================================================================
# REGISTERED CONSTANTS -- every module-level literal in this file, with where it came
# from. G12 parses this file's own AST and refuses anything not on this list. The band
# width, the floor, the tag names, the rules and the cycle labels are NOT here: they are
# imported from the instrument that registered them.
# ======================================================================================
REGISTERED_CONSTANTS = {
    "EVENTS_SRC": "REG-006's repaired ladder-C events, named by §7.5's tee-up",
    "EVENTS_AS_COLLECTED": "§5's sample as §5 collected it, §7.5's left-hand column",
    "EVENTS_SHA256": "the sha256 of both committed event files, pinned here",
    "TIER_LIFE": "REG-006 §4's tier definitions: which disclosed life, if any, a tier's "
                 "events can be binned by. Tiers 2 and 3 disclose no life (§7.5's table)",
    "SEEN_75": "REG-009 §7.5's table, reproduced before it is extended",
    "TABLE_ALL_FIRMS": "the firm count §7.5's 'all' row prints in BOTH columns",
    "P0_RESULT": "P0-c's committed sweep; §7.5's '7 qualifying bands' is read from it",
    "SEVEN_BANDS": "§7.5's stated qualifying-band count at a 1.00-year width",
    "QUARTERS_PER_YEAR": "q_star is a quarter index; §7.5 states the event span is "
                         "2012Q2-2026Q2, which q_star//4 reproduces as 2012..2026 (G9)",
    "EVENT_SPAN_YEARS": "§7.5's stated event span, as years",
    "PICK_MODES": "G10: the three ways to choose between a firm's two disclosed cycles",
    "PRIMARY_PICK": "G10's primary: the cycle nearest the event's own fiscal year",
    "DECISION_RULE": "§7.5's registered rule, quoted, written before any count existed",
    "BIN_RULE_PAT": "G3: the shape D3's bin rule would have if it were RETYPED here",
    "OUT_JSON": "this run's table",
    "RUN_LOG": "this run's log",
}

EVENTS_SRC = "reg-006-ladderC-events-corrected.json"
EVENTS_AS_COLLECTED = "pre-002-events.json"
EVENTS_SHA256 = {
    "reg-006-ladderC-events-corrected.json":
        "72bd6e4fc6506ac2e7f65a4205d9af6ae74d23ef8a5178dde271518418dbb3fa",
    "pre-002-events.json":
        "974d156b53dfb915f48bdc3df99d7f2f2dd146427fa537fd7bdff4a503006bf0",
}

TIER_LIFE = {0: PPE, 1: FIN, 2: None, 3: None}

SEEN_75 = {
    "corrected|0|events": 151, "corrected|0|firms": 98,
    "corrected|0|joinable": 110, "corrected|0|joinable_firms": 72,
    "corrected|1|events": 135, "corrected|1|firms": 91,
    "corrected|1|joinable": 71, "corrected|1|joinable_firms": 48,
    "corrected|2|events": 78, "corrected|2|firms": 47, "corrected|2|joinable": 0,
    "corrected|3|events": 415, "corrected|3|firms": 234, "corrected|3|joinable": 0,
    "corrected|all|events": 779, "corrected|all|joinable": 181,
    "collected|0|events": 55, "collected|0|firms": 38,
    "collected|0|joinable": 36, "collected|0|joinable_firms": 26,
    "collected|1|events": 136, "collected|1|firms": 91, "collected|1|joinable": 71,
    "collected|2|events": 81, "collected|2|firms": 47, "collected|2|joinable": 0,
    "collected|3|events": 423, "collected|3|firms": 234, "collected|3|joinable": 0,
    "collected|all|events": 695, "collected|all|joinable": 107,
    "collected|all|firms": 307,
}
TABLE_ALL_FIRMS = 307

P0_RESULT = "reg-009-p0-result.json"
SEVEN_BANDS = 7

QUARTERS_PER_YEAR = 4
EVENT_SPAN_YEARS = (2012, 2026)

PICK_MODES = ("near", "early", "late")
PRIMARY_PICK = "near"

DECISION_RULE = ("REG-009 §7.5: \"Only if fewer than two bands clear does the expensive "
                 "half arrive: a universe outside SIC 5200-5999 and 7370-7379 ... "
                 "It is REG-011's.\"")

# Written with single-character classes so the pattern LITERAL cannot match itself, and
# its witness world is composed from fragments below. `-30`'s F9a matched the literal
# inside its own witness; any guard whose subject is text it is part of has this.
BIN_RULE_PAT = r"int\(v [/][/] w\)|\[b [*] w, \(b [+] 1\) [*] w\)"

OUT_JSON = "reg-009-band-count.json"
RUN_LOG = "RESULT-REG-009-band-count-run.log"


# ======================================================================================
# PLUMBING
# ======================================================================================
def _here() -> Path:
    return Path(__file__).resolve().parent


def _digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_events(root: Path, fn: str) -> list:
    """Both universes, flattened. REG-006's pilot/replication split is preserved on each
    row so the per-universe floor can be reported beside the pooled one."""
    d = json.loads((root / "data" / fn).read_text())
    return [dict(e, universe=u) for u, uu in d["universes"].items() for e in uu["events"]]


def load_lives(root: Path) -> tuple:
    """cik -> cycle -> record, plus each cycle's window YEARS lifted from the file's own
    metadata rather than typed here."""
    files = {"2014-15": "reg-009-p0-lives-2015.json",
             "2022-23": "reg-009-p0-lives-2023.json"}
    idx: dict = defaultdict(dict)
    years = {}
    for cyc, fn in files.items():
        p = root / "data" / fn
        check("G2 · " + fn + " is the committed file, by digest",
              _digest(p) == LIVES_SHA256[cyc],
              witness=lambda p=p, cyc=cyc: hashlib.sha256(
                  p.read_bytes() + b"x").hexdigest() == LIVES_SHA256[cyc])
        d = json.loads(p.read_text())
        years[cyc] = tuple(int(w[:4]) for w in d["window"])
        for r in d["records"]:
            idx[int(r["cik"])][cyc] = r
    return idx, years


def joinable(events: list, idx: dict) -> list:
    """An event is joinable when its firm discloses THAT TIER'S life in some cycle. The
    tier's own life, not any life: tier 1's 71 joinable reproduces under the intangible
    tag and not under the property tag, which is G8."""
    out = []
    for e in events:
        tag = TIER_LIFE[e["tier"]]
        if tag is None:
            continue
        if any(tag in r["lives"] for r in idx.get(int(e["cik"]), {}).values()):
            out.append(e)
    return out


def pick_cycle(recs: dict, q_star: int, mode: str, years: dict) -> str:
    """Which of a firm's disclosed cycles supplies the life for THIS event."""
    if len(recs) == 1:
        return next(iter(recs))
    if mode == "early":
        return min(recs, key=lambda c: years[c][0])
    if mode == "late":
        return max(recs, key=lambda c: years[c][0])
    yr = q_star // QUARTERS_PER_YEAR
    return min(recs, key=lambda c: min(abs(yr - y) for y in years[c]))


def selected_lives(events: list, idx: dict, years: dict, rule: str, mode: str) -> list:
    """(event, cycle, life value) for every event this index can bin -- the selection
    `bands_for` performs, exposed so that a second reader of THIS population gets it from
    here rather than retyping it beside this file.

    REG-012 §3 P2 is why this exists as a function instead of four lines inside the loop
    below: a descriptor of the band count's own lives has to read the band count's own
    lives, and a retyped selection is a statistic about the retyper's idea of the sample.
    One path, so a divergence is impossible rather than merely unlikely. `bands_for`'s
    behaviour is unchanged by the extraction, and REG-012's P3 proves that by re-running
    both committed instruments and comparing their artifacts byte for byte."""
    out = []
    for e in events:
        tag = TIER_LIFE[e["tier"]]
        recs = {c: r for c, r in idx[int(e["cik"])].items() if tag in r["lives"]}
        cyc = pick_cycle(recs, e["q_star"], mode, years)
        out.append((e, cyc, float(recs[cyc]["lives"][tag][rule])))
    return out


def bands_for(events: list, idx: dict, years: dict, rule: str, mode: str, mid) -> dict:
    """Every event placed in exactly one band, by the D3 bin its firm's disclosed
    property life falls in. The bin INDEX is recovered from the lifted midpoint rather
    than recomputed: midpoint = lo + w/2, so index = round((mid - w/2) / w)."""
    out: dict = defaultdict(list)
    for e, _cyc, v in selected_lives(events, idx, years, rule, mode):
        b = int(round((mid(v, BAND_WIDTH) - BAND_WIDTH / 2.0) / BAND_WIDTH))
        out[b].append(e)
    return out


def profile(bands: dict) -> dict:
    rows = []
    for b in sorted(bands):
        es = bands[b]
        rows.append({"band": [b * BAND_WIDTH, (b + 1) * BAND_WIDTH],
                     "events": len(es),
                     "firms": len({e["cik"] for e in es}),
                     "pilot": sum(e["universe"] == "pilot" for e in es),
                     "replication": sum(e["universe"] == "replication" for e in es)})
    return {"occupied": len(rows),
            "clear_events": sum(r["events"] >= THIN_FLOOR for r in rows),
            "clear_firms": sum(r["firms"] >= THIN_FLOOR for r in rows),
            "clear_events_both_universes": sum(
                r["pilot"] >= THIN_FLOOR and r["replication"] >= THIN_FLOOR
                for r in rows),
            "rows": rows}


def ceilings(rows: list, spare: int) -> dict:
    """What a COMPLETE coverage fill could do to the count, two ways.

    ADVERSARIAL: hand every unjoined event to whichever bands are cheapest to lift over
    the floor -- the largest number of bands the fill could POSSIBLY produce.
    PROPORTIONAL: scale every occupied band by (total / joined) -- what the fill produces
    if the unjoined events are distributed like the joined ones.
    Neither is a prediction. They bracket a quantity this instrument cannot reach."""
    joined = sum(r["events"] for r in rows)
    deficits = sorted(max(0, THIN_FLOOR - r["events"]) for r in rows)
    n, budget = 0, spare
    for d in deficits:
        if d == 0:
            n += 1
            continue
        if budget >= d:
            budget -= d
            n += 1
    scale = (joined + spare) / joined if joined else 0.0
    return {"joined": joined, "unjoined": spare,
            "adversarial_max_bands": n,
            "proportional_scale": scale,
            "proportional_bands": sum(r["events"] * scale >= THIN_FLOOR for r in rows),
            "proportional_counts": [round(r["events"] * scale, 1) for r in rows]}


# ======================================================================================
# G12 -- NO FREE PARAMETER
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

    hr("REG-009 §7.5 · THE BAND COUNT — the tee-up's cheap half, run")
    print("  " + DECISION_RULE)
    print("  The rule was written before this instrument existed and is not moved here.\n")

    # ---- G1/G2: the inputs are the committed files -------------------------------
    print("G1 · THE EVENT FILES ARE THE COMMITTED ONES, BY DIGEST")
    for fn, want in EVENTS_SHA256.items():
        p = root / "data" / fn
        check("G1 · " + fn + " is the committed file, by digest", _digest(p) == want,
              witness=lambda p=p, want=want: hashlib.sha256(
                  p.read_bytes() + b"x").hexdigest() == want)

    print("\nG2 · AND SO ARE THE LIVES  (the same digests REG-009's instrument pins)")
    idx, years = load_lives(root)
    print("    cycle windows lifted from the files' own metadata: " + repr(years))

    # ---- G3: D3's bins are lifted, and are not retyped here -----------------------
    print("\nG3 · D3's BINS ARE LIFTED THROUGH REG-009's INSTRUMENT, NOT RETYPED")
    mid, mid_desc = lift_band_rule()
    retyped = re.search(BIN_RULE_PAT, src_self)
    witness_world = "bands[" + "int(v " + "// w)" + "].append(v)"
    check("G3a · the bin rule appears nowhere in THIS file as a literal",
          retyped is None,
          witness=lambda: re.search(BIN_RULE_PAT, witness_world) is None)
    check("G3b · the lifted midpoint is the centre of the lifted bin, at the width "
          "REG-009 §6 D3 registered",
          abs(mid(5.0, BAND_WIDTH) - 5.5) < 1e-12
          and abs(mid(5.99, BAND_WIDTH) - 5.5) < 1e-12,
          witness=lambda: abs(mid(5.0, BAND_WIDTH) - 5.0) < 1e-12)

    # ---- G4-G8: §7.5's table, reproduced before it is extended --------------------
    hr("§7.5's TABLE, REPRODUCED BEFORE IT IS EXTENDED")
    got = {}
    for label, fn in (("corrected", EVENTS_SRC), ("collected", EVENTS_AS_COLLECTED)):
        ev = load_events(root, fn)
        got[label + "|all|events"] = len(ev)
        got[label + "|all|firms"] = len({e["cik"] for e in ev})
        got[label + "|all|joinable"] = len(joinable(ev, idx))
        for t in sorted(TIER_LIFE):
            es = [e for e in ev if e["tier"] == t]
            js = joinable(es, idx)
            got[label + "|" + str(t) + "|events"] = len(es)
            got[label + "|" + str(t) + "|firms"] = len({e["cik"] for e in es})
            got[label + "|" + str(t) + "|joinable"] = len(js)
            got[label + "|" + str(t) + "|joinable_firms"] = len({e["cik"] for e in js})
        print("  " + label + ":")
        for t in sorted(TIER_LIFE):
            k = label + "|" + str(t)
            print("    tier %d  %4d events / %3d firms   joinable %3d / %3d firms"
                  % (t, got[k + "|events"], got[k + "|firms"],
                     got[k + "|joinable"], got[k + "|joinable_firms"]))
        print("    all     %4d events / %3d firms   joinable %3d"
              % (got[label + "|all|events"], got[label + "|all|firms"],
                 got[label + "|all|joinable"]))

    disagree = {k: (v, got[k]) for k, v in SEEN_75.items() if got.get(k) != v}
    check("G4 · every cell of §7.5's table that this instrument can reach reproduces",
          not disagree,
          witness=lambda: got["corrected|0|events"] == got["collected|0|events"])
    print("    " + str(len(SEEN_75)) + " cells checked, " + str(len(disagree))
          + " disagreements")

    ev_c = load_events(root, EVENTS_SRC)
    t0 = [e for e in ev_c if e["tier"] == 0]
    t1 = [e for e in ev_c if e["tier"] == 1]
    j0 = joinable(t0, idx)
    ppe_on_t1 = [e for e in t1
                 if any(PPE in r["lives"] for r in idx.get(int(e["cik"]), {}).values())]
    check("G8 · 'joinable' means the TIER'S OWN life: tier 1's 71 reproduces under the "
          "intangible tag and not under the property tag",
          len(ppe_on_t1) != SEEN_75["corrected|1|joinable"],
          witness=lambda: len([e for e in t1 if any(
              FIN in r["lives"] for r in idx.get(int(e["cik"]), {}).values())])
              != SEEN_75["corrected|1|joinable"])
    print("    tier 1 under the PROPERTY tag would be " + str(len(ppe_on_t1))
          + ", not " + str(SEEN_75["corrected|1|joinable"]))

    # ---- G6/G7: the two errata ----------------------------------------------------
    hr("TWO ERRATA IN §7.5's TABLE — measured, recorded, NOT repaired retroactively")
    check("G6 · §7.5's 'all' row prints " + str(TABLE_ALL_FIRMS) + " firms in BOTH "
          "columns, and the repaired file carries more",
          got["corrected|all|firms"] != TABLE_ALL_FIRMS
          and got["collected|all|firms"] == TABLE_ALL_FIRMS,
          witness=lambda: got["corrected|all|firms"] == TABLE_ALL_FIRMS)
    print("    ERRATUM 1 · the repaired crawl carries "
          + str(got["corrected|all|firms"]) + " distinct firms, not "
          + str(TABLE_ALL_FIRMS) + ". " + str(TABLE_ALL_FIRMS) + " is the count under "
          "the tag list REG-006 repaired; the repair added firms as well as events.")

    p0 = json.loads((root / "data" / P0_RESULT).read_text())
    qual = {}
    for tag, v in p0["by_tag"].items():
        for rule, c in v["p0c"].items():
            for s in c["sweep"]:
                if abs(s["width_years"] - BAND_WIDTH) < 1e-12:
                    qual[tag + "|" + rule] = s["n_qualifying_bands"]
    prim_key = PPE + "|" + PRIMARY
    min_key = PPE + "|R_MIN"
    check("G7 · §7.5's '7 qualifying bands' is P0-c's count under R_MIN, and the "
          "primary rule gives a different one",
          qual[min_key] == SEVEN_BANDS and qual[prim_key] != SEVEN_BANDS,
          witness=lambda: qual[prim_key] == SEVEN_BANDS)
    print("    ERRATUM 2 · P0-c at a 1.00-year width, property: R_MIN " + str(qual[min_key])
          + " qualifying bands, " + PRIMARY + " " + str(qual[prim_key]) + ".")
    print("    §7.5's '151 over 7 bands averages 21' therefore divides by the "
          "qualifying-band count of the rule §6 REFUSES to promote. Under the primary "
          "rule the same arithmetic gives %.1f." % (SEEN_75["corrected|0|events"]
                                                    / qual[prim_key]))

    # ---- G9: the quarter index, and the span §7.5 states --------------------------
    hr("THE JOIN, AND WHAT IT CANNOT REACH")
    qs = [e["q_star"] for e in ev_c]
    span = (min(qs) // QUARTERS_PER_YEAR, max(qs) // QUARTERS_PER_YEAR)
    check("G9 · q_star//4 reproduces §7.5's stated event span",
          span == EVENT_SPAN_YEARS,
          witness=lambda: (min(qs) // (QUARTERS_PER_YEAR + 1),
                           max(qs) // (QUARTERS_PER_YEAR + 1)) == EVENT_SPAN_YEARS)
    print("    events span %d..%d; the disclosed lives are measured in %s only."
          % (span[0], span[1], " and ".join(CYCLES)))
    print("    %d of %d property events are joinable; %d are not, and no band can hold "
          "them." % (len(j0), len(t0), len(t0) - len(j0)))
    two_cycle = [e for e in j0
                 if sum(PPE in r["lives"] for r in idx[int(e["cik"])].values()) == 2]
    print("    %d joinable events (%d firms) belong to a firm that discloses a property "
          "life in BOTH cycles — G10's subject." % (len(two_cycle),
                                                    len({e["cik"] for e in two_cycle})))

    # ---- THE COUNT ---------------------------------------------------------------
    hr("THE COUNT — 1.00-year property bands clearing " + str(THIN_FLOOR))
    res: dict = {"decision_rule": DECISION_RULE, "band_rule": mid_desc,
                 "floor": THIN_FLOOR, "width": BAND_WIDTH,
                 "events_total": len(t0), "events_joinable": len(j0),
                 "profiles": {}}
    for rule in RULES:
        for mode in PICK_MODES:
            pr = profile(bands_for(j0, idx, years, rule, mode, mid))
            res["profiles"][rule + "|" + mode] = pr
    for rule in RULES:
        print("\n  " + rule + ("  (PRIMARY)" if rule == PRIMARY else ""))
        for mode in PICK_MODES:
            pr = res["profiles"][rule + "|" + mode]
            print("    %-6s %2d occupied bands · %d clear %d EVENTS · %d clear %d FIRMS "
                  "· %d clear in BOTH universes"
                  % (mode, pr["occupied"], pr["clear_events"], THIN_FLOOR,
                     pr["clear_firms"], THIN_FLOOR, pr["clear_events_both_universes"]))
        pr = res["profiles"][rule + "|" + PRIMARY_PICK]
        print("    " + PRIMARY_PICK + "'s profile:")
        for r in pr["rows"]:
            mark = "  <== clears" if r["events"] >= THIN_FLOOR else ""
            print("      [%5.2f, %5.2f)  events %3d  firms %3d  (pilot %3d / repl %3d)%s"
                  % (r["band"][0], r["band"][1], r["events"], r["firms"],
                     r["pilot"], r["replication"], mark))

    prim = res["profiles"][PRIMARY + "|" + PRIMARY_PICK]
    modes_agree = len({res["profiles"][PRIMARY + "|" + m]["clear_events"]
                       for m in PICK_MODES}) == 1
    check("G10 · the primary count does not depend on which of a firm's two disclosed "
          "cycles is read",
          modes_agree,
          witness=lambda: len({res["profiles"][r + "|" + PRIMARY_PICK]["clear_events"]
                               for r in RULES}) == 1)
    print("\n  G10 · all three cycle choices give %d band(s) under %s — but the three "
          "INTERVAL RULES do not agree with each other: %s."
          % (prim["clear_events"], PRIMARY,
             ", ".join("%s %d" % (r, res["profiles"][r + "|" + PRIMARY_PICK]
                                  ["clear_events"]) for r in RULES)))

    check("G11 · every joinable event lands in exactly one band, and none is lost",
          sum(r["events"] for r in prim["rows"]) == len(j0),
          witness=lambda: sum(r["events"] for r in prim["rows"]) == len(j0) + 1)

    # ---- WHAT THE INSTRUMENT COULD NOT REACH -------------------------------------
    hr("THE CEILING A COVERAGE FILL COULD REACH — a lower bound is not an absence")
    ceil = ceilings(prim["rows"], len(t0) - len(j0))
    res["ceilings"] = ceil
    print("  %d joined · %d unjoined · a complete fill scales each band by %.3f"
          % (ceil["joined"], ceil["unjoined"], ceil["proportional_scale"]))
    print("  ADVERSARIAL  — every unjoined event handed to the cheapest bands: at most "
          "%d bands could clear." % ceil["adversarial_max_bands"])
    print("  PROPORTIONAL — unjoined events distributed like the joined ones: %d bands "
          "clear (%s)." % (ceil["proportional_bands"],
                           ", ".join("%.1f" % x for x in ceil["proportional_counts"])))
    print("  Neither is a prediction. Filling SOURCE-001's coverage series between the "
          "two cycles is the measurement that would replace them.")

    # ---- THE VERDICT --------------------------------------------------------------
    hr("§7.5's DECISION RULE, APPLIED")
    lives_design = prim["clear_events"] >= 2
    res["clear_primary"] = prim["clear_events"]
    res["design_survives"] = lives_design
    print("  Bands clearing %d events under %s, %s: %d."
          % (THIN_FLOOR, PRIMARY, PRIMARY_PICK, prim["clear_events"]))
    print("  §7.5: fewer than two -> the expensive half arrives. VERDICT: "
          + ("the design survives on this count."
             if lives_design else "REG-011 needs the new universe."))
    print("  And under the floor's NATIVE unit — §3b counts FIRM-years, not events — "
          "%d band(s) clear." % prim["clear_firms"])

    # ---- G12 ----------------------------------------------------------------------
    hr("G12 · NO FREE PARAMETER")
    extra = unregistered(src_self)
    check("G12 · every module-level literal in this file is registered with a provenance",
          not extra,
          witness=lambda: bool(unregistered(src_self + "\nSTRAY_KNOB = 0.5\n")) is False)
    print("    " + str(len(REGISTERED_CONSTANTS)) + " registered, 0 unregistered")

    (root / "data" / OUT_JSON).write_text(json.dumps(res, indent=2) + "\n")
    print("\n  wrote data/" + OUT_JSON)
    summary("SEVERITY · REG-009 §7.5 band count")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
