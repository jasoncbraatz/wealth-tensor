"""REG-009 §7.5's band count, pinned — against the filings, not against the run.

WHAT EACH TEST IS PINNED AGAINST, AND WHY IT MATTERS
----------------------------------------------------
`test_reg009_ladder_inputs` set the discipline: a test that reads the instrument's own
output only proves the instrument is deterministic. So every count below is recomputed
from the committed event and lives files through the instrument's PURE functions, and
nothing here runs `main()` — which would rewrite two tracked files and one day be blamed
for a dirty tree at the gate (`-30`'s lesson, paid for once already).

The three tests that would catch a real defect:

  * `test_the_bin_rule_is_never_retyped` — the band is D3's or it is nothing. If a future
    session inlines `int(v // w)` here or in the instrument, the count silently becomes a
    statistic about that session's idea of a band. G3a in the instrument, pinned here.
  * `test_the_interval_rule_moves_the_answer_across_the_threshold` — `R_MID` 1, `R_MIN` 2.
    The verdict depends on the rule §6 refuses to promote, so a session that quietly
    changes `PRIMARY` flips a published conclusion. This test makes that loud.
  * `test_the_two_errata_are_still_errata` — the §7.5 cells this run could not reproduce.
    If someone repairs §7.5, these go red and the repair gets noticed rather than
    absorbed.
"""

from __future__ import annotations

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


@pytest.fixture(scope="module")
def inst():
    import reg009_band_count as m

    return m


@pytest.fixture(scope="module")
def world(inst):
    """The join, rebuilt from the committed files through the instrument's own
    functions — no run log, no result json."""
    idx: dict = {}
    years = {}
    for cyc, fn in (("2014-15", "reg-009-p0-lives-2015.json"),
                    ("2022-23", "reg-009-p0-lives-2023.json")):
        d = json.loads((DATA / fn).read_text())
        years[cyc] = tuple(int(w[:4]) for w in d["window"])
        for r in d["records"]:
            idx.setdefault(int(r["cik"]), {})[cyc] = r
    ev = inst.load_events(ROOT, inst.EVENTS_SRC)
    return idx, years, ev


def _profile(inst, world, rule, mode):
    idx, years, ev = world
    t0 = [e for e in ev if e["tier"] == 0]
    j0 = inst.joinable(t0, idx)
    mid, _ = inst.lift_band_rule()
    return inst.profile(inst.bands_for(j0, idx, years, rule, mode, mid))


# --------------------------------------------------------------------------------------
# §7.5's TABLE — the cells paper III now prints
# --------------------------------------------------------------------------------------
def test_the_published_property_counts_reproduce_from_the_filings(inst, world):
    idx, _, ev = world
    t0 = [e for e in ev if e["tier"] == 0]
    j0 = inst.joinable(t0, idx)
    assert len(t0) == 151
    assert len({e["cik"] for e in t0}) == 98
    assert len(j0) == 110
    assert len({e["cik"] for e in j0}) == 72


def test_joinable_means_the_tiers_own_life_and_not_any_life(inst, world):
    """Tier 1's 71 reproduces under the intangible tag; the property tag gives 96. A join
    key that let any disclosed life count would have printed 96 and looked fine."""
    idx, _, ev = world
    t1 = [e for e in ev if e["tier"] == 1]
    assert len(inst.joinable(t1, idx)) == 71
    loose = [e for e in t1
             if any(inst.PPE in r["lives"] for r in idx.get(int(e["cik"]), {}).values())]
    assert len(loose) == 96


def test_every_reproducible_cell_of_the_table_still_reproduces(inst, world):
    idx, _, _ = world
    for label, fn in (("corrected", inst.EVENTS_SRC),
                      ("collected", inst.EVENTS_AS_COLLECTED)):
        ev = inst.load_events(ROOT, fn)
        got = {label + "|all|events": len(ev),
               label + "|all|firms": len({e["cik"] for e in ev}),
               label + "|all|joinable": len(inst.joinable(ev, idx))}
        for t in sorted(inst.TIER_LIFE):
            es = [e for e in ev if e["tier"] == t]
            js = inst.joinable(es, idx)
            got[label + "|" + str(t) + "|events"] = len(es)
            got[label + "|" + str(t) + "|firms"] = len({e["cik"] for e in es})
            got[label + "|" + str(t) + "|joinable"] = len(js)
            got[label + "|" + str(t) + "|joinable_firms"] = len({e["cik"] for e in js})
        for k, want in inst.SEEN_75.items():
            if k.startswith(label + "|"):
                assert got[k] == want, k


# --------------------------------------------------------------------------------------
# THE COUNT
# --------------------------------------------------------------------------------------
def test_exactly_one_band_clears_the_floor_under_the_primary_rule(inst, world):
    pr = _profile(inst, world, inst.PRIMARY, inst.PRIMARY_PICK)
    assert pr["occupied"] == 16
    assert pr["clear_events"] == 1
    clearing = [r for r in pr["rows"] if r["events"] >= inst.THIN_FLOOR]
    assert [r["band"] for r in clearing] == [CLEARING_BAND]
    assert clearing[0]["events"] == 36
    assert clearing[0]["firms"] == 20


def test_the_floors_native_unit_is_firms_and_no_band_clears_it(inst, world):
    """§3b's THIN floor counts firm-years. §7.5's arithmetic counted events. Both are
    reported; only one of them ever clears."""
    pr = _profile(inst, world, inst.PRIMARY, inst.PRIMARY_PICK)
    assert pr["clear_firms"] == 0
    assert pr["clear_events_both_universes"] == 0


def test_the_cycle_choice_does_not_decide_the_answer(inst, world):
    counts = {m: _profile(inst, world, inst.PRIMARY, m)["clear_events"]
              for m in inst.PICK_MODES}
    assert set(counts.values()) == {1}, counts


def test_the_interval_rule_moves_the_answer_across_the_threshold(inst, world):
    """The verdict is 'fewer than two'. R_MIN gives two — and R_MIN is the rule §6
    refuses to promote BECAUSE it scores best. If this test ever goes green with
    PRIMARY == 'R_MIN', a published conclusion changed without a registration."""
    got = {r: _profile(inst, world, r, inst.PRIMARY_PICK)["clear_events"]
           for r in inst.RULES}
    assert got == {"R_MID": 1, "R_MIN": 2, "R_WEIGHT": 0}
    assert inst.PRIMARY == "R_MID"


def test_no_joinable_event_is_lost_or_double_counted(inst, world):
    idx, _, ev = world
    t0 = [e for e in ev if e["tier"] == 0]
    pr = _profile(inst, world, inst.PRIMARY, inst.PRIMARY_PICK)
    assert sum(r["events"] for r in pr["rows"]) == len(inst.joinable(t0, idx)) == 110


def test_the_coverage_ceiling_brackets_rather_than_predicts(inst, world):
    """41 events cannot be binned. The proportional fill lands the second band on 30.2
    against a floor of 30 — which is why the coverage fill is decision-relevant and not
    tidy. If this drifts, the tee-up's price drifted with it."""
    pr = _profile(inst, world, inst.PRIMARY, inst.PRIMARY_PICK)
    ceil = inst.ceilings(pr["rows"], 151 - 110)
    assert ceil["joined"] == 110 and ceil["unjoined"] == 41
    assert ceil["adversarial_max_bands"] == 3
    assert ceil["proportional_bands"] == 2
    assert max(ceil["proportional_counts"]) == pytest.approx(49.4, abs=0.05)


# --------------------------------------------------------------------------------------
# THE GUARDS THEMSELVES
# --------------------------------------------------------------------------------------
def test_the_bin_rule_is_never_retyped(inst):
    """The instrument's band is D3's or it is nothing. Composed from fragments so the
    witness world cannot be matched out of this file's own source."""
    src = (SCRIPTS / "reg009_band_count.py").read_text()
    assert re.search(inst.BIN_RULE_PAT, src) is None
    assert re.search(inst.BIN_RULE_PAT, "bands[" + "int(v " + "// w)" + "]") is not None


def test_the_midpoint_is_the_centre_of_p0s_own_bin(inst):
    mid, _ = inst.lift_band_rule()
    assert mid(5.0, inst.BAND_WIDTH) == pytest.approx(5.5)
    assert mid(5.99, inst.BAND_WIDTH) == pytest.approx(5.5)


def test_no_unregistered_module_literal(inst):
    src = (SCRIPTS / "reg009_band_count.py").read_text()
    assert inst.unregistered(src) == set()
    assert inst.unregistered(src + "\nSTRAY_KNOB = 0.5\n") == {"STRAY_KNOB"}


def test_the_two_errata_are_still_errata(inst, world):
    """If §7.5 is ever repaired, these go red and the repair is noticed."""
    idx, _, ev = world
    assert len({e["cik"] for e in ev}) == 338 != inst.TABLE_ALL_FIRMS
    p0 = json.loads((DATA / inst.P0_RESULT).read_text())
    qual = {}
    for tag, v in p0["by_tag"].items():
        for rule, c in v["p0c"].items():
            for s in c["sweep"]:
                if abs(s["width_years"] - inst.BAND_WIDTH) < 1e-12:
                    qual[tag + "|" + rule] = s["n_qualifying_bands"]
    assert qual[inst.PPE + "|R_MIN"] == inst.SEVEN_BANDS
    assert qual[inst.PPE + "|" + inst.PRIMARY] == 9


def test_the_committed_table_agrees_with_a_fresh_computation(inst, world):
    """The one test that DOES read the run's output — and it reads it only to confirm the
    committed json is the run these tests just reproduced."""
    res = json.loads((DATA / inst.OUT_JSON).read_text())
    assert res["clear_primary"] == 1
    assert res["design_survives"] is False
    assert res["events_total"] == 151 and res["events_joinable"] == 110
    fresh = _profile(inst, world, inst.PRIMARY, inst.PRIMARY_PICK)
    stored = res["profiles"][inst.PRIMARY + "|" + inst.PRIMARY_PICK]
    assert [r["events"] for r in stored["rows"]] == [r["events"] for r in fresh["rows"]]
