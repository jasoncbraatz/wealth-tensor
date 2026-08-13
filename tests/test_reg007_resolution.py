"""REG-007's resolution and adjudication audits, pinned offline.

Sibling of test_tag_resolution.py. That test exists because a us-gaap element that
matched NOTHING was indistinguishable, in every downstream statistic, from one that
matched nothing IN OUR SAMPLE. REG-007 shipped the same defect in its own keyword
families three hours after the lesson was written down -- 'composition of its net
assets', which collapses the standard's 'composition OR CARRYING AMOUNT of its net
assets' into a string no filing contains -- and F2 caught it by name on the first run.

These tests pin the finding so it cannot be quietly un-found, and pin the guard that
found it so it cannot be quietly removed. Offline: they read committed JSON only.
"""
from __future__ import annotations

import json
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PHRASE = ROOT / "data" / "reg-007-phrase-audit.json"
POLY = ROOT / "data" / "reg-007-polysemy-audit.json"
RESULT = ROOT / "data" / "reg-007-result.json"


@pytest.fixture(scope="module")
def phrase():
    return json.loads(PHRASE.read_text())


@pytest.fixture(scope="module")
def poly():
    return json.loads(POLY.read_text())


@pytest.fixture(scope="module")
def result():
    return json.loads(RESULT.read_text())


def test_every_registered_phrase_resolves(phrase):
    """All nine REG-007 sec 3.2 phrases match something in our own sample."""
    assert phrase["dead_phrases"] == [], phrase["dead_phrases"]
    assert len(phrase["phrase_hits"]) == 9
    assert min(phrase["phrase_hits"].values()) > 0


def test_the_two_dead_keywords_stay_found(phrase):
    """The finding is pinned. If a future edit resurrects these, the test fails and the
    edit has to say so out loud -- exactly as test_edgar.py pins the dead tier-0 tag."""
    assert set(phrase["dead_keywords"]) == {
        "composition of its net assets",
        "goodwill impairment loss in the financial statements of a subsidiary",
    }


def test_dead_keyword_is_a_transcription_error_not_an_absent_concept(phrase):
    """'composition of its net assets' matches nothing; the standard's actual wording,
    'composition or carrying amount', is not what we registered. The concept is present
    in the corpus under the sibling keyword, which is why EMPTY and ABSENT had to be
    told apart by name rather than by a zero in a column."""
    assert phrase["keyword_hits"]["composition of its net assets"] == 0
    assert phrase["keyword_hits"]["carrying amount of its net assets"] > 0


def test_polysemy_audit_is_complete_and_under_ceiling(poly):
    assert poly["n"] == 60
    assert len(poly["windows"]) == 60
    assert all(w["sense"] in ("impairment", "non_impairment") for w in poly["windows"])
    n_bad = sum(1 for w in poly["windows"] if w["sense"] == "non_impairment")
    assert n_bad == poly["n_non_impairment"] == 6
    assert poly["share_non_impairment"] == pytest.approx(0.10)
    assert poly["share_non_impairment"] <= poly["ceiling"] == 0.15


def test_every_non_impairment_window_carries_its_reason(poly):
    for w in poly["windows"]:
        if w["sense"] == "non_impairment":
            assert w["reason"].strip(), w


def test_boilerplate_share_is_flagged_post_hoc(poly):
    """The boilerplate reading explains F8's near-null but is NOT registered. The flag
    is load-bearing: it is what stops a future session citing it as a tested quantity."""
    assert "post-hoc" in poly["post_hoc_note"].lower()
    assert poly["n_boilerplate"] == 16


def test_silent_is_a_distinct_cell_from_neither(result):
    """F5's correction, pinned. Folding SILENT into NEITHER is what made the guard refuse
    to report anything, and it is the mirror of REG-006's Q4 defect."""
    cells = result["cells_window"]
    assert "SILENT" in cells and "NEITHER" in cells
    assert cells["SILENT"] == 92
    assert cells["NEITHER"] == 119
    assert result["neither_share"] == pytest.approx(119 / 644, rel=1e-6)
    assert result["neither_share"] <= 0.20
    assert result["neither_strict"] == pytest.approx(211 / 736, rel=1e-6)
    assert result["neither_strict"] > 0.20      # the strict figure is NOT hidden


def test_both_lambda_folds_are_reported_and_disagree(result):
    """REG-007 sec 3.4 required both fold variants precisely so the sign could not be
    chosen after the run. They disagree. That is the reportable fact."""
    a = result["lambda"]["both_internal"]
    b = result["lambda"]["both_external"]
    assert a["lam"] > 0 > b["lam"]
    assert a["p_value"] > 0.05 and b["p_value"] > 0.05


def test_the_placebo_ran_and_is_close_to_the_window(result):
    """F8. The three-point gap is the reason REG-007's discriminator does not
    discriminate; if a future change opens that gap, this test fails and the claim in
    RESULT-REG-007 sec 2 has to be rewritten rather than silently outgrown."""
    assert result["placebo_n"] > 1000
    assert abs(result["f_rate_window"] - result["f_rate_placebo"]) < 0.05


def test_both_arms_clear_the_registered_floor(result):
    assert result["window"]["joint"] >= 30
    assert result["window"]["gwonly"] >= 30
