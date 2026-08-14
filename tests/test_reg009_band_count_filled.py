"""The coverage-filled band count, pinned — against the filings, not against the run.

Same discipline as `test_reg009_band_count`: every count below is recomputed from the
committed event and lives files through the instrument's PURE functions, and nothing here
runs `main()`, which would rewrite two tracked files and one day be blamed for a dirty
tree at the gate.

The four tests that would catch a real defect:

  * `test_the_tie_break_straddles_the_floor` — the fill CREATED a free parameter. With two
    cycles the nearest-cycle rule's tie-break was structurally unreachable (0 of 110
    joinable events); with nine it decides 50 of 133, and the band count is 1 one way and
    2 the other. If a future session flips the tie-break, or quietly stops measuring it,
    this goes red. It is the whole reason `-32`'s "one band clears" is reported at less
    strength than `-31`'s identical number.
  * `test_the_cycle_choice_now_decides_the_answer` — the exact counterpart of `-31`'s
    `test_the_cycle_choice_does_not_decide_the_answer`, which passed on two cycles. On the
    filled join it does not hold, and that is a RESULT rather than a defect: near 1,
    early 2, late 2. A session that "repairs" this test has repaired away the finding.
  * `test_r_min_is_still_not_primary` — `R_MIN` gives two bands under every cycle choice
    on the filled join, so the temptation §6 refuses is now larger than it was for `-31`.
  * `test_the_second_band_did_not_clear` — `[4, 5)` reached 27, not the 30.2 `-31`'s
    proportional bracket predicted. If that drifts, the fill's verdict drifted with it.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data"

sys.path.insert(0, str(SCRIPTS))

CLEARING_BAND = [5.0, 6.0]
SECOND_BAND = [4.0, 5.0]


@pytest.fixture(scope="module")
def inst():
    import reg009_band_count_filled as m

    return m


@pytest.fixture(scope="module")
def bc():
    import reg009_band_count as m

    return m


@pytest.fixture(scope="module")
def world(inst, bc):
    """The nine-cycle join, rebuilt from the committed files through the instrument's own
    functions — no run log, no result json."""
    base_idx, base_years = bc.load_lives(ROOT)
    idx, years, dupes = inst.chronological(base_idx, base_years, ROOT)
    ev = bc.load_events(ROOT, bc.EVENTS_SRC)
    t0 = [e for e in ev if e["tier"] == 0]
    return base_idx, base_years, idx, years, t0, dupes


def _profile(inst, bc, idx, years, t0, rule=None, mode=None):
    from reg009_ladder_inputs import PRIMARY, lift_band_rule

    mid, _ = lift_band_rule()
    j = bc.joinable(t0, idx)
    return bc.profile(bc.bands_for(j, idx, years, rule or PRIMARY,
                                   mode or bc.PRIMARY_PICK, mid))


def _row(pr, band):
    return next((r for r in pr["rows"] if r["band"] == band), None)


# --------------------------------------------------------------------------------------
# `-31`'s ROW — reproduced before it is extended
# --------------------------------------------------------------------------------------
def test_the_two_cycle_row_still_reproduces(inst, bc, world):
    base_idx, base_years, _, _, t0, _ = world
    pr = _profile(inst, bc, base_idx, base_years, t0)
    assert len(t0) == 151
    assert len(bc.joinable(t0, base_idx)) == 110
    assert pr["occupied"] == 16
    assert pr["clear_events"] == 1
    assert pr["clear_firms"] == 0
    assert inst.TWO_CYCLE_PINS["events_joinable"] == 110


def test_the_fill_raises_the_join_and_not_the_population(inst, bc, world):
    _, _, idx, _, t0, _ = world
    assert len(t0) == 151
    assert len(bc.joinable(t0, idx)) == 133


def test_the_fill_adds_coverage_and_removes_none(inst, bc, world):
    base_idx, _, idx, _, t0, _ = world
    before = {id(e) for e in bc.joinable(t0, base_idx)}
    after = {id(e) for e in bc.joinable(t0, idx)}
    assert before < after


# --------------------------------------------------------------------------------------
# THE COUNT
# --------------------------------------------------------------------------------------
def test_the_clearing_band_is_the_same_band_and_it_grew(inst, bc, world):
    _, _, idx, years, t0, _ = world
    pr = _profile(inst, bc, idx, years, t0)
    row = _row(pr, CLEARING_BAND)
    assert row is not None and row["events"] == 47 and row["firms"] == 22
    assert pr["occupied"] == 17


def test_the_second_band_did_not_clear(inst, bc, world):
    """`-31`'s proportional bracket predicted 30.2 here. The measurement says 27, so the
    unjoined events did not fall like the joined ones."""
    _, _, idx, years, t0, _ = world
    pr = _profile(inst, bc, idx, years, t0)
    assert _row(pr, SECOND_BAND)["events"] == 27
    assert pr["clear_events"] == 1


def test_the_floors_native_unit_is_firms_and_no_band_clears_it(inst, bc, world):
    _, _, idx, years, t0, _ = world
    pr = _profile(inst, bc, idx, years, t0)
    assert pr["clear_firms"] == 0
    assert pr["clear_events_both_universes"] == 0


def test_no_joinable_event_is_lost_or_double_counted(inst, bc, world):
    _, _, idx, years, t0, _ = world
    pr = _profile(inst, bc, idx, years, t0)
    assert sum(r["events"] for r in pr["rows"]) == len(bc.joinable(t0, idx)) == 133


# --------------------------------------------------------------------------------------
# THE PARAMETER THE FILL CREATED
# --------------------------------------------------------------------------------------
def test_the_tie_break_straddles_the_floor(inst, bc, world):
    """The finding. Unreachable on two cycles, decisive on nine, and it crosses §7.5's
    threshold on its own."""
    base_idx, base_years, idx, years, t0, _ = world
    assert inst.near_ties(bc.joinable(t0, base_idx), base_idx, base_years) == 0
    assert inst.near_ties(bc.joinable(t0, idx), idx, years) == 50

    idx_l, years_l, _ = inst.chronological(base_idx, base_years, ROOT, tie_to_later=True)
    registered = _profile(inst, bc, idx, years, t0)
    mirror = _profile(inst, bc, idx_l, years_l, t0)
    assert registered["clear_events"] == 1
    assert mirror["clear_events"] == 2
    assert sum(r["events"] for r in mirror["rows"]) == 133


def test_the_cycle_choice_now_decides_the_answer(inst, bc, world):
    """`-31`'s G10 found all three cycle choices agreeing on two cycles. On the filled
    join they do not, and the registered one is the only one giving 1. Repairing this
    test would repair away the result."""
    _, _, idx, years, t0, _ = world
    got = {m: _profile(inst, bc, idx, years, t0, mode=m)["clear_events"]
           for m in bc.PICK_MODES}
    assert got == {"near": 1, "early": 2, "late": 2}
    assert bc.PRIMARY_PICK == "near"


def test_r_min_is_still_not_primary(inst, bc, world):
    """`R_MIN` clears two bands under every cycle choice on the filled join. §6 refuses to
    promote it BECAUSE it scores best, and the fill made that temptation larger."""
    from reg009_ladder_inputs import PRIMARY

    _, _, idx, years, t0, _ = world
    assert PRIMARY == "R_MID"
    for mode in bc.PICK_MODES:
        assert _profile(inst, bc, idx, years, t0, rule="R_MIN",
                        mode=mode)["clear_events"] == 2
    assert _profile(inst, bc, idx, years, t0, rule="R_MID")["clear_events"] == 1


def test_the_decomposition_partitions_the_151(inst, bc, world):
    """The fill's gain and the fill's price, separated. 14 events moved band without ever
    having been unjoinable; a single filled number would have hidden them."""
    from reg009_ladder_inputs import PRIMARY, lift_band_rule

    base_idx, base_years, idx, years, t0, _ = world
    mid, _ = lift_band_rule()
    j2 = bc.joinable(t0, base_idx)
    jF = bc.joinable(t0, idx)
    was = inst.band_of(j2, base_idx, base_years, PRIMARY, bc.PRIMARY_PICK, mid)
    now = inst.band_of(jF, idx, years, PRIMARY, bc.PRIMARY_PICK, mid)
    newly = [e for e in jF if id(e) not in was]
    moved = [e for e in jF if id(e) in was and was[id(e)] != now[id(e)]]
    same = [e for e in jF if id(e) in was and was[id(e)] == now[id(e)]]
    still = [e for e in t0 if id(e) not in now]
    assert (len(newly), len(moved), len(same), len(still)) == (23, 14, 96, 18)
    assert len(newly) + len(moved) + len(same) + len(still) == len(t0) == 151


# --------------------------------------------------------------------------------------
# THE FILL'S INPUTS
# --------------------------------------------------------------------------------------
def test_every_filled_window_is_the_committed_one_translated_by_whole_years(inst):
    wins = inst.load_windows(ROOT)
    base = wins["2014-15"]
    assert len(wins) == 9
    for cyc in inst.FILL_CYCLES:
        w = wins[cyc]
        assert (w[0].month, w[0].day) == (base[0].month, base[0].day)
        assert (w[1].month, w[1].day) == (base[1].month, base[1].day)
        assert w[1].year - w[0].year == base[1].year - base[0].year
    displaced = (base[0] + dt.timedelta(days=1), base[1])
    assert (displaced[0].month, displaced[0].day) != (base[0].month, base[0].day)


def test_the_fill_files_are_the_committed_ones(inst):
    for cyc, fn in inst.FILL_CYCLES.items():
        got = hashlib.sha256((DATA / fn).read_bytes()).hexdigest()
        assert got == inst.FILL_SHA256[cyc]


def test_the_october_gap_is_reported_and_not_closed(inst, bc, world):
    """Widening the window would close it and would be a parameter chosen after the fact.
    26 panel firm-years fall in a gap; the one gap firm that owns a tier-0 event is joined
    anyway, so the gap cost this count nothing — measured, not assumed."""
    _, _, _, _, t0, _ = world
    wins = inst.load_windows(ROOT)
    gs = inst.gaps(wins)
    assert len(gs) == 8
    assert {(hi - lo).days + 1 for lo, hi in gs} == {30}
    panel = json.loads((DATA / inst.PANEL).read_text())
    fy = {int(f["cik"]): [r["fy_end"] for r in f.get("rows", []) if r.get("fy_end")]
          for f in panel}

    def _d(s):
        return dt.datetime.strptime(s, "%Y-%m-%d").date()

    in_gap = [(c, d) for c, ds in fy.items() for d in ds
              if any(lo <= _d(d) <= hi for lo, hi in gs)]
    assert len(in_gap) == 26
    gap_firms = {c for c, _ in in_gap}
    assert len(gap_firms) == 8
    assert len(gap_firms & {int(e["cik"]) for e in t0}) == 1


def test_duplicate_firm_years_keep_thirty_ones_rule(inst, world):
    _, _, _, _, _, dupes = world
    assert dupes == 35


# --------------------------------------------------------------------------------------
# THE GUARDS THEMSELVES
# --------------------------------------------------------------------------------------
def test_the_bin_rule_is_never_retyped(inst, bc):
    """The pattern is IMPORTED, so this instrument cannot contain its own subject."""
    src = (SCRIPTS / "reg009_band_count_filled.py").read_text()
    assert re.search(bc.BIN_RULE_PAT, src) is None
    assert re.search(bc.BIN_RULE_PAT, "bands[" + "int(v " + "// w)" + "]") is not None


def test_no_unregistered_module_literal(inst):
    src = (SCRIPTS / "reg009_band_count_filled.py").read_text()
    assert inst.unregistered(src) == set()
    assert inst.unregistered(src + "\nSTRAY_KNOB = 0.5\n") == {"STRAY_KNOB"}


def test_the_committed_table_agrees_with_a_fresh_computation(inst, bc, world):
    """The one test that DOES read the run's output — and only to confirm the committed
    json is the run these tests just reproduced, with `-31`'s row still inside it."""
    _, _, idx, years, t0, _ = world
    res = json.loads((DATA / inst.OUT_JSON).read_text())
    assert res["clear_primary"] == 1
    assert res["design_survives"] is False
    assert res["events_total"] == 151 and res["events_joinable"] == 133
    assert res["two_cycle"]["events_joinable"] == 110
    assert res["two_cycle"]["clear_primary"] == 1
    assert res["near_pick_ties"]["straddles_the_floor"] is True
    fresh = _profile(inst, bc, idx, years, t0)
    stored = res["profiles"]["R_MID|near"]
    assert [r["events"] for r in stored["rows"]] == [r["events"] for r in fresh["rows"]]


def test_thirty_ones_artifact_is_untouched(inst, bc):
    """`-32` reports beside `-31`, never instead of it. If a future session overwrites the
    committed two-cycle table with a filled one, this is where it shows."""
    res = json.loads((DATA / bc.OUT_JSON).read_text())
    assert res["events_joinable"] == 110
    assert res["clear_primary"] == 1
    assert res["ceilings"]["unjoined"] == 41
