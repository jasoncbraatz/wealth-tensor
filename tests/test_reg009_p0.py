"""Tests for REG-009 §2's P0 probe.

Two of these exist because a defect got past a draft and one because a promise in a
docstring was not kept by the code beneath it. Each says which.
"""
from __future__ import annotations

import json
import math
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import reg009_p0_lifetime_values as P  # noqa: E402

DATA = ROOT / "data"
REC_2015 = DATA / "reg-009-p0-lives-2015.json"
REC_2023 = DATA / "reg-009-p0-lives-2023.json"


# ---------------------------------------------------------------- duration parsing
@pytest.mark.parametrize("raw,years", [
    ("P39Y", 39.0), ("P5Y", 5.0), ("P9Y6M", 9.5), ("P18M", 1.5),
    ("P6M", 0.5), ("P1Y3M", 1.25),
])
def test_iso_durations_parse_to_years(raw, years):
    assert P.parse_years(raw) == pytest.approx(years, abs=1e-9)


@pytest.mark.parametrize("raw", ["", "P", "39", "PT5H", "five years", None, "P0Y"])
def test_unparseable_durations_return_none_rather_than_a_number(raw):
    """A duration this probe does not understand must become a COUNTED refusal, never a
    silent zero -- a zero life is an infinite delta and would sail past the domain guard."""
    assert P.parse_years(raw) is None


# ---------------------------------------------------------------- §4.4's ruler
def test_the_lifted_simulation_reproduces_paper_III_4_4s_committed_poles():
    """THE LOAD-BEARING TEST. P0-c prices a band width against §4.4's recovery
    probability. It does not re-implement that simulation -- it lifts the definitions out
    of wt088_disclosed_ladder.py at run time and checks they still print the three
    numbers the manuscript committed to. If either side drifts, P0-c has no ruler."""
    ns = P.load_ladder()
    assert ns["ALPHA"] == 0.05
    assert (ns["DELTA_LO"], ns["DELTA_HI"]) == (0.001, 0.040)
    got_ind = ns["draw_magnitude"](ns["N"], ns["SEED"], False)[0]
    got_ord = ns["draw_magnitude"](ns["N"], ns["SEED"], True)[0]
    got_com = ns["_common_delta_recovery"](ns["SEED"])
    assert got_ind == pytest.approx(0.115, abs=0.002)     # paper III §4.4
    assert got_ord == pytest.approx(0.019, abs=0.002)
    assert got_com == pytest.approx(1.000, abs=0.002)


def test_the_extraction_fails_loudly_rather_than_substituting_a_default(monkeypatch):
    """The first run of this extractor missed the tuple-assigned constants and ABORTED,
    which is the behaviour under test. A ruler that silently defaults is worse than one
    that is missing, because the table it prices still looks finished."""
    monkeypatch.setattr(P, "LADDER_SRC", ROOT / "tests" / "test_reg009_p0.py")
    with pytest.raises(SystemExit) as e:
        P.load_ladder()
    assert "ABORTS" in str(e.value)


def test_a_degenerate_band_recovers_by_arithmetic_not_by_economics():
    """A band holding ONE distinct disclosed life has zero delta dispersion and recovers
    the ordering always. That is not the design working -- it is the band collapsing to a
    point -- and it is why P0-c prints distinct-values-per-band beside every recovery."""
    import numpy as np
    ns = P.load_ladder()
    one = np.array([1 / 5.0] * 50)
    assert P.recovery_from_deltas(one, 0.408, ns, n=400) == pytest.approx(1.0)
    spread = np.array([1 / x for x in np.linspace(2.5, 40, 200)])
    assert P.recovery_from_deltas(spread, 0.408, ns, n=400) < 0.5


# ---------------------------------------------------------------- the guards, as code
def test_a_median_whose_iqr_spans_an_order_of_magnitude_is_called_two_populations():
    """REG-009 §2 promoted this from a lesson to a mechanism; the mechanism is this
    string, so the string is what gets tested."""
    assert "TWO POPULATIONS" in P.med_iqr([1, 1, 2, 50, 100, 200]).upper()
    assert "TWO POPULATIONS" not in P.med_iqr([9, 10, 10, 11, 12]).upper()


def test_two_cells_refused_as_THIN_are_never_compared(capsys):
    """SOURCE-001 §4c found a probe printing a contrast between two cells whose own rates
    the same function had just declined to report."""
    P.compare_or_refuse("x", {"THIN": True, "label": "a"}, {"THIN": False},
                        lambda a, b: "SHOULD NOT PRINT")
    out = capsys.readouterr().out
    assert "NOT COMPARED" in out and "SHOULD NOT PRINT" not in out


def test_a_comparison_between_two_live_cells_is_printed(capsys):
    P.compare_or_refuse("x", {"THIN": False}, {"THIN": False}, lambda a, b: "PRINTED")
    assert "PRINTED" in capsys.readouterr().out


# ---------------------------------------------------------------- D2's three rules
def _target_rows():
    """Target Corp's FY2022 10-K, 0000027419-23-000015 -- the same filing SOURCE-001 §3a
    hand-audited three independent ways. Building 8-39, fixtures 2-15, computers 2-7."""
    out = []
    for comp, lo, hi in (("BuildingAndBuildingImprovements", 8, 39),
                         ("FixturesAndEquipment", 2, 15),
                         ("ComputerEquipment", 2, 7)):
        for rng_, v in ((P.RANGE_MIN, lo), (P.RANGE_MAX, hi)):
            out.append({"adsh": "x", "tag": P.CANON[0], "ddate": "20230131",
                        "component": comp, "range": rng_, "years": float(v)})
    return out


def test_the_three_D2_rules_reproduce_SOURCE_001_3as_hand_audited_filing():
    lives = P.firm_year_lives(_target_rows())[P.CANON[0]]
    assert lives["components"] == {"BuildingAndBuildingImprovements": 23.5,
                                   "FixturesAndEquipment": 8.5,
                                   "ComputerEquipment": 4.5}
    assert lives["R_MID"] == pytest.approx(8.5)      # median of the three midpoints
    assert lives["R_MIN"] == pytest.approx(2.0)      # median of the three low endpoints
    assert lives["n_components"] == 3
    assert dict(lives["kinds"]) == {"interval": 3}


def test_a_component_with_one_endpoint_is_a_half_interval_and_is_counted_as_one():
    rows = [{"adsh": "x", "tag": P.CANON[0], "ddate": "d", "component": "A",
             "range": P.RANGE_MIN, "years": 5.0}]
    assert P.firm_year_lives(rows)[P.CANON[0]]["kinds"]["half_interval"] == 1


def test_weighted_average_is_a_point_not_an_interval_endpoint():
    rows = [{"adsh": "x", "tag": P.CANON[0], "ddate": "d", "component": "A",
             "range": P.RANGE_WAVG, "years": 7.0}]
    assert P.firm_year_lives(rows)[P.CANON[0]]["kinds"]["point"] == 1


def test_R_WEIGHT_falls_back_to_R_MID_and_says_so_rather_than_absorbing_it():
    """The docstring promised the fallback share would be reported; a draft printed
    nothing, so Target Corp -- three component lives, no component amounts -- carried an
    R_WEIGHT that was silently R_MID."""
    lives = P.firm_year_lives(_target_rows())[P.CANON[0]]
    assert lives["R_WEIGHT_backed"] is False
    assert lives["R_WEIGHT"] == pytest.approx(lives["R_MID"])
    backed = P.firm_year_lives(_target_rows(),
                               {P.CANON[0]: {"ComputerEquipment": 1e9}})[P.CANON[0]]
    assert backed["R_WEIGHT_backed"] is True
    assert backed["R_WEIGHT"] == pytest.approx(4.5)


# ---------------------------------------------------------------- the artifacts
@pytest.mark.skipif(not REC_2023.exists(), reason="P0 extract not present")
def test_the_P0_artifact_carries_VALUES_where_the_source_001_artifact_carries_BOOLEANS():
    """REG-009 §5's error, pinned. `source-001-lifetime-by-fyend.json` answers *was a life
    tagged* -- four booleans and a tag COUNT. Nothing in it can answer *what was the
    life*, and the two are indistinguishable from the filename. This test is the
    difference, asserted rather than described."""
    old = json.loads((DATA / "source-001-lifetime-by-fyend.json").read_text())["rows"]
    sample = [r for r in old if r.get("status") == "submission"][0]
    assert set(sample) >= {"any", "canon", "ppe", "intangible", "facts"}
    assert all(isinstance(sample[k], bool) for k in ("any", "canon", "ppe", "intangible"))
    assert isinstance(sample["facts"], int)          # a COUNT, not a life

    new = json.loads(REC_2023.read_text())["records"][0]
    tag = next(iter(new["lives"]))
    for rule in ("R_MID", "R_MIN", "R_WEIGHT"):
        assert isinstance(new["lives"][tag][rule], (int, float))
        assert new["lives"][tag][rule] > 0


@pytest.mark.skipif(not REC_2023.exists(), reason="P0 extract not present")
def test_P0s_coverage_reproduces_3bs_registered_coverage_machinery():
    """P0 re-reads the zips with a different question. If its firm-year join drifted from
    §3b's, its coverage would drift too -- so §3b's own numbers are the cross-check."""
    for path, expected in ((REC_2015, 0.727), (REC_2023, 0.823)):
        b = json.loads(path.read_text())
        t = b["tally"]
        got = t["firm_years_with_a_life"] / t["panel_firm_years_in_window"]
        assert got == pytest.approx(expected, abs=0.012), (path.name, got, expected)


@pytest.mark.skipif(not REC_2023.exists(), reason="P0 extract not present")
def test_no_silent_caps_every_declined_row_is_counted():
    t = json.loads(REC_2023.read_text())["tally"]
    for k in ("submission_no_life_value", "dupe_iprx_dropped", "unparseable_duration",
              "no_submission", "rows_prior_period_comparative"):
        assert k in t
    assert any(k.startswith("excluded_tag:") for k in t)


@pytest.mark.skipif(not REC_2023.exists(), reason="P0 extract not present")
def test_p0b_point_estimate_lies_inside_its_own_bootstrap_interval():
    """THE DEFECT THAT ANNOUNCED ITSELF. A first draft ran one estimator for the point and
    a different one for the bootstrap -- the point applied the THIN rule, the resample did
    not -- and the CI came back entirely ABOVE the point it was printed beside. A
    confidence interval on a different statistic is worse than none."""
    recs = [r for p in (REC_2015, REC_2023)
            for r in json.loads(p.read_text())["records"]]
    b = P.p0b(recs, P.CANON[0], "R_MID", 30)
    assert not b["THIN"]
    lo, hi = b["ratio_ci95"]
    assert lo <= b["ratio"] <= hi, (lo, b["ratio"], hi)
    assert b["boot_reps"] >= 100


@pytest.mark.skipif(not REC_2023.exists(), reason="P0 extract not present")
def test_stickiness_is_measured_at_the_horizon_4_7s_bound_actually_names():
    """§4.7 says lives are 'sticky within a firm across the horizon over which timeliness
    is measured', and the panel's horizon is 2013-2025. A one-year read does not test that
    sentence; a cycle-to-cycle read does, which is why P0 reads two cycles."""
    recs = [r for p in (REC_2015, REC_2023)
            for r in json.loads(p.read_text())["records"]]
    comps = [c for p in (REC_2015, REC_2023)
             for c in json.loads(p.read_text())["comparatives"]]
    a = P.p0a(recs, comps, P.CANON[0], "R_MID", 30)
    assert not a["decade"]["THIN"] and a["decade"]["n"] >= 100
    assert not a["decade_by_component"]["THIN"]
    # the component-level read is the confound-free one and it is the one that holds
    assert a["decade_by_component"]["unchanged_share"] > a["decade"]["unchanged_share"]
