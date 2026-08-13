"""REG-008's instrument, pinned. Offline: no network, no corpus rebuild, no scipy needed.

Three of these tests exist because the registration FREEZES something (the phrase set, the
generic list, the audit ceilings). A frozen thing with no test is a promise; with a test it
is a contract. `-21` shipped tests/test_cell_provenance.py for the same reason and the same
family of defect: a guard scoped to what a run CONSUMED does not cover what it EMITS.
"""
from __future__ import annotations

import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wt096_entity_anchored as W                                      # noqa: E402

DATA = ROOT / "data"


# --------------------------------------------------------------- the segmenter (§3.2)
@pytest.mark.parametrize("text,n", [
    ("The unit failed. The charge was taken.", 2),
    ("Sales in the U.S. fell sharply. We tested goodwill.", 2),
    ("The charge was $12.4 million. It hit one unit.", 2),
    ("Ended Dec. 31, 2019. A trigger occurred.", 2),
    ("No boundary here at all", 1),
])
def test_segment_counts(text, n):
    assert len(W.segment(text)) == n


def test_segment_does_not_split_inside_an_abbreviation():
    segs = W.segment("Our U.S. Hosiery reporting unit was tested. It passed.")
    assert segs[0].startswith("Our U.S. Hosiery")
    assert "U.S." in segs[0]


def test_segment_restores_every_protected_period():
    text = "Sales in the U.S. fell $1.5 million in Q1. Goodwill was tested."
    assert W.DOT not in "".join(W.segment(text))
    assert "".join(W.segment(text)).replace(" ", "") == text.replace(" ", "")


# --------------------------------------------------------------- the extractor (§3.3)
@pytest.mark.parametrize("sentence,expected", [
    ("the Private Cloud reporting unit failed", ["Private Cloud"]),
    ("our Lucky Vitamin reporting unit was reviewed", ["Lucky Vitamin"]),
    ("the fair value of the reporting unit exceeded", []),
    ("each reporting unit is tested annually", []),
    ("its reporting units were tested", []),
    ("the U.S. Hosiery reporting unit", ["U.S. Hosiery"]),
])
def test_m1_names(sentence, expected):
    assert W.m1_names(sentence) == expected


def test_m1_rejects_the_generic_determiners_that_carry_the_boilerplate():
    """The whole instrument is this distinction: a POLICY names no unit."""
    boiler = ("Goodwill is tested annually at the reporting unit level, or whenever "
              "events or circumstances indicate that the fair value of a reporting unit "
              "is less than its carrying amount.")
    assert W.m1_names(boiler) == []


# ------------------------------------------------------- the frozen sets are a contract
def test_phrase_set_is_reg007s_verbatim_and_has_not_been_extended():
    assert W.PHRASES == (
        "triggering event", "triggering events", "impairment indicator",
        "impairment indicators", "indicators of impairment", "indicator of impairment",
        "interim impairment test", "interim goodwill impairment", "events or circumstances")


def test_generic_list_is_frozen_at_its_registered_size():
    """REG-008 §3.3 freezes it. Widening it raises M1 precision, narrowing it raises
    recall, and doing either after the run is the researcher degree of freedom the
    registration closed. 38 members, and a test that says so."""
    assert len(W.GENERIC) == 38
    for must in ("the", "a", "each", "its", "any", "certain", "respective"):
        assert must in W.GENERIC


def test_internal_family_still_carries_the_two_strings_reg007_reported_dead():
    """They are DEAD, and they STAY, because REG-007 F2 registered the handling as
    'report it, do not fix it' and REG-008 §2.5 found the proposed fix is dead too.
    Deleting them here would erase the finding."""
    assert "composition of its net assets" in W.INTERNAL
    assert ("recognition of a goodwill impairment loss in the financial statements "
            "of a subsidiary") in W.INTERNAL


# --------------------------------------------------------------- exact Fisher (§3.4)
@pytest.mark.parametrize("t,expected", [
    ((1, 9, 11, 3), 0.0027594),      # Fisher's own tea-tasting-shaped table
    ((10, 10, 10, 10), 1.0),
    ((31, 250, 35, 328), 0.6013),    # the pooled M1 cell of RESULT-REG-008
])
def test_fisher_matches_known_values(t, expected):
    assert W.fisher(*t) == pytest.approx(expected, abs=5e-4)


def test_fisher_agrees_with_scipy_where_scipy_exists():
    scipy_stats = pytest.importorskip("scipy.stats")
    for t in [(31, 250, 35, 328), (0, 281, 1, 362), (168, 113, 211, 152), (3, 7, 9, 1)]:
        assert W.fisher(*t) == pytest.approx(scipy_stats.fisher_exact(
            [[t[0], t[1]], [t[2], t[3]]])[1], rel=1e-9)


def test_mde_is_larger_than_the_effect_this_study_reported():
    """The null is only interpretable beside this number, so it is pinned."""
    assert W.mde(31, 281, 35, 363) == pytest.approx(0.0675, abs=5e-4)
    assert W.mde(31, 281, 35, 363) > 0.0139 * 4


# --------------------------------------------------------------- offset merging (§2.1)
def test_merged_spans_uses_true_offsets_and_does_not_duplicate_overlap():
    row = {"passages": [{"at": 1500, "text": "A" * 1000 + "B" * 1000},
                        {"at": 2000, "text": "B" * 1000 + "C" * 1000}]}
    spans = W.merged_spans(row, 1000)
    assert len(spans) == 1
    a, b, text = spans[0]
    assert (a, b) == (500, 3000)
    assert len(text) == b - a            # the invariant: the span IS its text
    assert text.count("A") == 1000
    assert text.count("B") == 1000       # the overlap is carried once, not twice
    assert text.count("C") == 500


def test_merged_spans_keeps_disjoint_passages_apart():
    row = {"passages": [{"at": 1000, "text": "X" * 10}, {"at": 90000, "text": "Y" * 10}]}
    assert len(W.merged_spans(row, 0)) == 2


# ------------------------------------------------- the audits cannot be quietly widened
def test_segmentation_audit_meets_its_registered_ceiling():
    a = json.loads((DATA / "reg-008-segmentation-audit.json").read_text())
    v = a["verdicts"]
    assert len(v) == 60
    assert sum(x["boundary_error"] for x in v) / 60 <= 0.10
    # the loose count is REPORTED, not guarded - pinned so it cannot silently vanish
    assert sum(x["loose_boundary"] for x in v) == 11


def test_m1_audit_meets_its_registered_ceiling():
    a = json.loads((DATA / "reg-008-m1-audit.json").read_text())
    v = a["verdicts"]
    assert len(v) == 60
    assert sum(not x["genuine_unit"] for x in v) / 60 <= 0.15


def test_the_f_family_strings_are_dead_and_the_result_says_so():
    """REG-008 §2.5's finding, pinned. If a future crawl makes one of these resolve, this
    goes red and the finding gets revisited rather than silently outliving its evidence."""
    a = json.loads((DATA / "reg-008-resolution-audit.json").read_text())
    for s in ("internal:composition of its net assets",
              "internal:recognition of a goodwill impairment loss in the financial "
              "statements of a subsidiary"):
        assert a["counts"][s] == 0
        assert s in a["dead"]


def test_result_json_reports_every_marker_pooled_and_by_universe():
    r = json.loads((DATA / "reg-008-result.json").read_text())
    assert r["corpus_sha256"] == W.CORPUS_SHA
    for key in ("m1", "m2", "m3", "m1_f"):
        assert r["pooled"][key]["joint_n"] and r["pooled"][key]["gwonly_n"]
        assert set(r["by_universe"][key]) == {"pilot", "replication"}
    assert r["placebo_gate"]["delta"] > r["placebo_gate"]["reg007_gap"]
