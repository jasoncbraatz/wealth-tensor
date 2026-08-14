"""REG-009's ladder-input run, pinned.

WHAT EACH TEST IS PINNED AGAINST, AND WHY IT MATTERS
----------------------------------------------------
`RESULT-P0`'s tests pinned P0's values against the FILING rather than against P0's own
output, because a test that reads the instrument's output only proves the instrument is
deterministic. The same discipline is applied here as far as it can go:

  * the population is recomputed from the committed records, so it does not read the
    instrument at all;
  * the ruler is re-lifted from `wt088_disclosed_ladder.py`, so a drifting manuscript
    breaks this suite and not just the next run;
  * the band midpoint is re-derived from `reg009_p0_lifetime_values.py`'s own bin lines;
  * and Psi itself -- which IS the output and cannot be pinned against anything else --
    is cross-checked between `data/reg-009-result.json` and the sentences of
    `RESULT-REG-009.md`, so a hand-edited document fails rather than merely disagreeing.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "preregistration"

sys.path.insert(0, str(SCRIPTS))

PPE = "PropertyPlantAndEquipmentUsefulLife"
FIN = "FiniteLivedIntangibleAssetUsefulLife"

REGISTERED_COUNTS = {
    "pairs_2014_15": 321, "pairs_2022_23": 362, "pairs_pooled": 683,
    "firms_pooled": 577, "firms_both_cycles": 106, "r_weight_both": 273,
    "one_tag_only": 613, "ppe_only": 523, "fin_only": 90,
}


@pytest.fixture(scope="module")
def result():
    return json.loads((DATA / "reg-009-result.json").read_text())


@pytest.fixture(scope="module")
def report():
    return (DOCS / "RESULT-REG-009.md").read_text()


# ======================================================================================
# The population, recomputed from the records without touching the instrument
# ======================================================================================
def test_the_pair_population_is_reg009_section_7_1s():
    tally = {}
    firms = {}
    for cyc, name in (("2014-15", "reg-009-p0-lives-2015.json"),
                      ("2022-23", "reg-009-p0-lives-2023.json")):
        recs = json.loads((DATA / name).read_text())["records"]
        pairs = [r for r in recs if PPE in r["lives"] and FIN in r["lives"]]
        tally[cyc] = {
            "any": len(recs),
            "ppe": sum(PPE in r["lives"] for r in recs),
            "fin": sum(FIN in r["lives"] for r in recs),
            "pair": len(pairs),
            "wboth": sum(bool(r["lives"][PPE].get("R_WEIGHT_backed"))
                         and bool(r["lives"][FIN].get("R_WEIGHT_backed"))
                         for r in pairs),
        }
        firms[cyc] = {r["cik"] for r in pairs}

    got = {
        "pairs_2014_15": tally["2014-15"]["pair"],
        "pairs_2022_23": tally["2022-23"]["pair"],
        "pairs_pooled": tally["2014-15"]["pair"] + tally["2022-23"]["pair"],
        "firms_pooled": len(firms["2014-15"] | firms["2022-23"]),
        "firms_both_cycles": len(firms["2014-15"] & firms["2022-23"]),
        "r_weight_both": tally["2014-15"]["wboth"] + tally["2022-23"]["wboth"],
        "one_tag_only": sum(t["any"] - t["pair"] for t in tally.values()),
        "ppe_only": sum(t["ppe"] - t["pair"] for t in tally.values()),
        "fin_only": sum(t["fin"] - t["pair"] for t in tally.values()),
    }
    assert got == REGISTERED_COUNTS


def test_the_one_tag_only_firm_years_are_never_a_denominator(result):
    """F9: 613 is a reported row, not a base. No Psi row may carry it as its n."""
    assert result["counts"]["one_tag_only"] == 613
    assert all(cell["n"] != 613 for cell in result["psi"].values())


# ======================================================================================
# The ruler, re-lifted -- so a drifting manuscript breaks this suite
# ======================================================================================
def test_the_ruler_still_lifts_and_still_reproduces_wt088s_poles():
    import reg009_ladder_inputs as inst

    ns = inst.lift_ruler()
    assert (float(ns["PHI"][0]), float(ns["PHI"][1])) == (0.80, 0.60)
    assert tuple(ns["LIFE_PPE"]) == (10.0, 40.0)
    assert tuple(ns["LIFE_FIN"]) == (3.0, 20.0)
    assert abs(ns["_poles"]["admissible_at_alpha"] - 0.0) <= inst.POLE_TOL
    assert abs(ns["_poles"]["rises_at_a_ext"] - 0.997) <= inst.POLE_TOL
    # and what was lifted is what wt088 still prints
    assert abs(ns["_poles"]["wt088_printed_rises"] - 0.997) <= inst.POLE_TOL


def test_the_band_midpoint_is_p0s_own_bin_and_not_this_repos_idea_of_one():
    import reg009_ladder_inputs as inst

    mid, desc = inst.lift_band_rule()
    assert "int(v // w)" in desc
    # an integer life sits on a bin's LEFT edge, so the midpoint TRANSLATES it by +w/2.
    # This is the mechanism RESULT-REG-009 §4 names for P3's failure; if the bin rule
    # ever changes shape, that paragraph stops being true and this test says so.
    assert mid(7.0, 1.0) == pytest.approx(7.5)
    assert mid(7.9, 1.0) == pytest.approx(7.5)
    assert mid(8.0, 1.0) == pytest.approx(8.5)


# ======================================================================================
# The result, and the document that reports it, cross-checked against each other
# ======================================================================================
def test_the_registered_statistics_are_the_committed_ones(result):
    p = result["psi"]["pooled|R_MID|raw"]
    assert p["n"] == 683 and p["n_admissible"] == 665
    assert p["psi"] == pytest.approx(0.6586, abs=5e-4)
    assert p["ci_lo"] == pytest.approx(0.6211, abs=5e-4)
    assert p["ci_hi"] == pytest.approx(0.6964, abs=5e-4)
    assert p["distinct_pairs"] == 428
    assert result["psi"]["pooled|R_MID|band"]["psi"] == pytest.approx(0.7236, abs=5e-4)
    assert result["S"]["R_MID"][0] == pytest.approx(0.1391, abs=5e-4)
    # Psi_rect at the paper's own calibration is UNDEFINED, not zero: the admissible
    # rectangle is empty there. `null` in the record is the point, not a gap in it.
    assert result["psi_rect"]["calibration"]["admissible_share"] == 0.0
    assert result["psi_rect"]["calibration"]["rises_of_admissible"] is None
    assert result["psi_rect"]["measured"]["rises_of_admissible"] == pytest.approx(
        0.9980, abs=5e-4)


def test_the_registered_predictions_scored_as_committed(result):
    assert result["predictions"] == {"P1": True, "P2": True, "P3": False, "P4": True}
    assert result["stopping"]["agree_within_interval"] is False


def test_the_document_reports_the_numbers_the_record_holds(result, report):
    """A hand-edited RESULT doc fails here rather than quietly disagreeing with its data."""
    p = result["psi"]["pooled|R_MID|raw"]
    for value in (f"{p['psi']:.4f}", f"{p['ci_lo']:.4f}", f"{p['ci_hi']:.4f}",
                  f"{result['psi']['pooled|R_MID|band']['psi']:.4f}",
                  f"{result['psi_rect']['measured']['rises_of_admissible']:.4f}",
                  f"{result['S']['R_MID'][0]:.4f}"):
        assert value in report, f"{value} is in the record and not in the document"
    assert "**FAILS**" in report, "P3 failed; the document must say so in its table"


def test_the_qualifier_travels_in_every_table_that_reports_a_statistic(report):
    """F4, pinned: the disclosed-vs-economic gap is a column, not a closing paragraph."""
    import reg009_ladder_inputs as inst

    assert not inst.scan_f4(report)
    assert not inst.scan_f3(report)
    assert not inst.scan_f5(report)
    assert not inst.scan_f6(report)
    # and the scanners are not vacuous
    assert inst.scan_f4(report.replace(inst.QUALIFIER_MARK, "xxx"))
    assert inst.scan_f3(report.replace(inst.RWEIGHT_MARK, "xxx"))


def test_the_instrument_declares_every_module_level_literal_it_owns():
    """F10, pinned: a constant added later without a provenance string fails here."""
    import reg009_ladder_inputs as inst

    src = (SCRIPTS / "reg009_ladder_inputs.py").read_text()
    assert not inst.f10_unregistered(src)
    assert inst.f10_unregistered(src + "\nFUDGE = 0.5\n") == {"FUDGE"}


def test_the_run_log_records_a_run_with_no_vacuous_guard():
    log = (DOCS / "RESULT-REG-009-run.log").read_text()
    m = re.search(r"REG-009 LADDER INPUTS: (\d+) severe · (\d+) definitional · "
                  r"(\d+) failed/vacuous", log)
    assert m, "the run log does not carry a severity summary"
    assert int(m.group(1)) >= 24
    assert int(m.group(3)) == 0


def test_the_instrument_opens_no_archive_and_names_no_url():
    """F7, pinned against the source rather than against a run."""
    import reg009_ladder_inputs as inst

    body = (SCRIPTS / "reg009_ladder_inputs.py").read_text().split(
        "REGISTERED_CONSTANTS = {", 1)[1]
    assert not re.search(inst.NET_PAT, body, re.M)
    assert re.search(inst.NET_PAT, "import " + "zipfile", re.M)


def test_the_instrument_reruns_to_the_same_numbers():
    """The seed and replicate count are lifted from wt088, so the run is reproducible.

    Slow, and the only test that executes the whole instrument -- which means it WRITES
    four tracked files. A test that leaves the working tree dirty is a test that will
    one day be blamed for a gate failure, so every output is snapshotted and restored
    unconditionally. The restore is a no-op when the run is reproducible, which is the
    thing being asserted; it matters precisely when it is not.
    """
    outputs = [DATA / "reg-009-result.json", DATA / "reg-009-resolution-audit.json",
               DOCS / "RESULT-REG-009.md", DOCS / "RESULT-REG-009-run.log"]
    before = {f: f.read_text() for f in outputs}
    try:
        proc = subprocess.run([sys.executable, str(SCRIPTS / "reg009_ladder_inputs.py")],
                              cwd=str(ROOT), capture_output=True, text=True, timeout=1800)
        assert proc.returncode == 0, proc.stdout[-3000:] + proc.stderr[-3000:]
        after = {f: f.read_text() for f in outputs}
    finally:
        for f, text in before.items():
            f.write_text(text)
    # the run log carries no clock, so it too should be byte-identical
    for f in outputs:
        assert after[f] == before[f], f"{f.name} changed on a rerun of the same inputs"
