"""Tests for the WT-026 severe-test machinery.

All fixtures are synthetic. The point of a pre-registered test is that a stranger can check the
logic without trusting our data pull, so nothing here touches the network.
"""

from __future__ import annotations

import datetime as dt
from collections import defaultdict

import pytest

from wealth_tensor import edgar as E


# --------------------------------------------------------------------------------------
# The pre-registration is a contract. This is the guard on it.
# --------------------------------------------------------------------------------------

def test_pre001_constants_are_what_was_registered():
    """If this fails, someone amended a pre-registration by editing a constant.

    That is not a bug in the code -- it is the code and the registered document disagreeing
    about what was predicted, which is the one failure this whole exercise exists to prevent.
    Change the document, date the amendment, then change the number.
    """
    assert E.MATERIALITY_FLOOR == 0.01
    assert E.MIN_RUN == 2
    assert E.MAX_LOOKBACK == 20
    assert E.MIN_HISTORY_QUARTERS == 12
    assert E.PILOT_SIC == (5200, 5999)
    assert E.REPLICATION_SIC == (7370, 7379)
    assert set(E.TIER_TAGS) == {0, 1, 2, 3}
    assert E.TIER_TAGS[3] == ("GoodwillImpairmentLoss",)
    assert E.TIER_TAGS[2] == ("ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill",)
    assert E.REVENUE_TAGS[0] == "RevenueFromContractWithCustomerExcludingAssessedTax"


# --------------------------------------------------------------------------------------
# Quarter arithmetic
# --------------------------------------------------------------------------------------

def test_qindex_is_monotone_and_yoy_is_exactly_four():
    assert E.qindex(dt.date(2020, 3, 31)) + 4 == E.qindex(dt.date(2021, 3, 31))
    assert E.qindex(dt.date(2020, 12, 31)) + 1 == E.qindex(dt.date(2021, 1, 31))


def test_a_january_year_end_filer_lands_on_the_same_axis_as_a_december_one():
    """The reason fiscal labels are not used: retail is full of off-calendar year ends."""
    jan_fye_q1 = E.qindex(dt.date(2021, 5, 1))     # fiscal Q1 ends early May
    assert E.qindex(dt.date(2022, 4, 30)) - jan_fye_q1 == 4


# --------------------------------------------------------------------------------------
# companyfacts parsing
# --------------------------------------------------------------------------------------

def _fact(start, end, val, filed="2024-01-01", form="10-Q"):
    d = {"end": end, "val": val, "filed": filed, "form": form}
    if start:
        d["start"] = start
    return d


def _facts(tag_to_rows):
    return {"facts": {"us-gaap": {t: {"units": {"USD": r}} for t, r in tag_to_rows.items()}}}


def test_direct_quarterly_facts_are_read():
    f = _facts({"Revenues": [_fact("2020-01-01", "2020-03-31", 100),
                             _fact("2020-04-01", "2020-06-30", 110)]})
    s, tag, _ = E.duration_series(f, ("Revenues",))
    assert tag == "Revenues"
    assert s[E.qindex(dt.date(2020, 3, 31))] == 100
    assert s[E.qindex(dt.date(2020, 6, 30))] == 110


def test_q4_is_recovered_by_differencing_cumulatives():
    """The load-bearing case: Q4 is almost never tagged as a quarter, only as FY minus 9M.

    Tiers 2 and 3 are tested annually under ASC 350, so their charges land overwhelmingly in Q4.
    A parser blind to this deletes most of the half of the ladder the prediction is about.
    """
    f = _facts({"Revenues": [
        _fact("2020-01-01", "2020-03-31", 100),
        _fact("2020-01-01", "2020-06-30", 210),
        _fact("2020-01-01", "2020-09-30", 330),
        _fact("2020-01-01", "2020-12-31", 500, form="10-K"),
    ]})
    s, _t, _ = E.duration_series(f, ("Revenues",))
    assert s[E.qindex(dt.date(2020, 3, 31))] == 100
    assert s[E.qindex(dt.date(2020, 6, 30))] == 110
    assert s[E.qindex(dt.date(2020, 9, 30))] == 120
    assert s[E.qindex(dt.date(2020, 12, 31))] == 170     # 500 - 330, invisible to a naive parser


def test_a_directly_tagged_quarter_beats_a_derived_one():
    f = _facts({"Revenues": [_fact("2020-01-01", "2020-03-31", 100),
                             _fact("2020-01-01", "2020-06-30", 210),
                             _fact("2020-04-01", "2020-06-30", 115)]})
    s, _t, _ = E.duration_series(f, ("Revenues",))
    assert s[E.qindex(dt.date(2020, 6, 30))] == 115


def test_the_latest_restatement_wins_and_the_supersession_is_counted():
    f = _facts({"Revenues": [_fact("2020-01-01", "2020-03-31", 100, filed="2020-05-01"),
                             _fact("2020-01-01", "2020-03-31", 90, filed="2021-05-01")]})
    s, _t, sup = E.duration_series(f, ("Revenues",))
    assert s[E.qindex(dt.date(2020, 3, 31))] == 90
    assert sup == 1


def test_revenue_tag_fallback_order_is_respected():
    f = _facts({"SalesRevenueNet": [_fact("2020-01-01", "2020-03-31", 7)]})
    _s, tag, _ = E.duration_series(f, E.REVENUE_TAGS)
    assert tag == "SalesRevenueNet"


def test_instant_facts_ignore_durations():
    f = _facts({"Assets": [_fact(None, "2020-03-31", 1000),
                           _fact("2020-01-01", "2020-03-31", 5)]})
    s = E.instant_series(f, "Assets")
    assert s[E.qindex(dt.date(2020, 3, 31))] == 1000


def test_annual_only_charges_are_flagged_not_silently_merged():
    """An annual charge with no quarterly companion is attributable only to the year end."""
    f = _facts({"GoodwillImpairmentLoss": [_fact("2020-01-01", "2020-12-31", 500, form="10-K")]})
    out = E.annual_only_charges(f, ("GoodwillImpairmentLoss",))
    assert out == {E.qindex(dt.date(2020, 12, 31)): 500}


def test_an_annual_charge_is_not_attributed_when_a_quarter_already_reported_it():
    f = _facts({"GoodwillImpairmentLoss": [
        _fact("2020-04-01", "2020-06-30", 500),
        _fact("2020-01-01", "2020-12-31", 500, form="10-K"),
    ]})
    assert E.annual_only_charges(f, ("GoodwillImpairmentLoss",)) == {}


# --------------------------------------------------------------------------------------
# Onset detection  (PRE-001 s5.3)
# --------------------------------------------------------------------------------------

def _rev(base_q, values):
    return {base_q + i: v for i, v in enumerate(values)}


def test_onset_is_the_first_quarter_of_the_run_not_the_last():
    # eight quarters: four flat, then four declining year-over-year
    rev = _rev(100, [10, 10, 10, 10, 9, 8, 7, 6])
    onset, censored = E.deterioration_onset(rev, q_star=108)
    assert onset == 104 and not censored
    assert 108 - onset == 4


def test_a_single_declining_quarter_is_not_a_run():
    rev = _rev(100, [10, 10, 10, 10, 10, 10, 10, 9])
    assert E.deterioration_onset(rev, q_star=108)[0] is None


def test_the_impairment_quarter_itself_cannot_start_the_run():
    """A charge and the revenue collapse that triggered it land together constantly.

    If the event quarter counted as evidence, the event would be dating itself and every lag
    would be biased toward zero -- uniformly, so the *gradient* would be flattened, which is the
    quantity under test.
    """
    rev = _rev(100, [10, 10, 10, 10, 10, 10, 10, 1])     # only q=107 declines
    assert E.deterioration_onset(rev, q_star=107)[0] is None


def test_a_missing_quarter_breaks_the_run_rather_than_being_bridged():
    rev = _rev(100, [10, 10, 10, 10, 9, 8, 7, 6])
    del rev[105]
    onset, _c = E.deterioration_onset(rev, q_star=108)
    assert onset == 106


def test_a_run_still_going_at_the_lookback_cap_is_reported_censored():
    rev = {100 + i: 100 - i for i in range(60)}           # declining forever
    onset, censored = E.deterioration_onset(rev, q_star=150)
    assert censored is True
    assert 150 - onset <= E.MAX_LOOKBACK


def test_growth_is_not_deterioration():
    rev = _rev(100, [10, 10, 10, 10, 11, 12, 13, 14])
    assert E.deterioration_onset(rev, q_star=108)[0] is None


# --------------------------------------------------------------------------------------
# Jonckheere-Terpstra  (PRE-001 s6)
# --------------------------------------------------------------------------------------

def test_jt_detects_a_clean_increasing_trend():
    g = [[1, 1, 2], [3, 4, 4], [6, 7, 7], [9, 10, 11]]
    r = E.jonckheere_terpstra(g)
    assert r["z"] > 3 and r["p_one_sided"] < 0.01


def test_jt_is_near_zero_when_there_is_no_trend():
    g = [[1, 5, 9], [9, 1, 5], [5, 9, 1], [1, 9, 5]]
    r = E.jonckheere_terpstra(g)
    assert abs(r["z"]) < 1.0 and r["p_one_sided"] > 0.15


def test_jt_does_not_reward_a_decreasing_trend():
    """One-sided by design: the direction was named in advance, so the wrong direction must lose."""
    g = [[9, 10, 11], [6, 7, 7], [3, 4, 4], [1, 1, 2]]
    r = E.jonckheere_terpstra(g)
    assert r["z"] < -3 and r["p_one_sided"] > 0.99


def test_jt_tie_correction_actually_bites():
    """Lags are whole quarters, so ties are the common case, not an edge case."""
    g = [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2]]
    r = E.jonckheere_terpstra(g)
    ns = [len(x) for x in g]
    N = sum(ns)
    naive = (N ** 2 * (2 * N + 3) - sum(n ** 2 * (2 * n + 3) for n in ns)) / 72.0
    assert r["var"] < naive        # ignoring ties would overstate significance

def test_jt_handles_degenerate_input_without_pretending_to_a_result():
    assert E.jonckheere_terpstra([[1, 2, 3]])["n"] == 0
    assert E.jonckheere_terpstra([])["n"] == 0


def test_mann_whitney_direction_matches_the_registered_alternative():
    lo, hi = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
    assert E.mann_whitney_one_sided(lo, hi)["p_one_sided"] < 0.05
    assert E.mann_whitney_one_sided(hi, lo)["p_one_sided"] > 0.95


def test_median_and_iqr():
    assert E.median([3, 1, 2]) == 2
    assert E.median([4, 1, 2, 3]) == 2.5
    lo, hi = E.iqr([1, 2, 3, 4, 5])
    assert (lo, hi) == (2.0, 4.0)


# --------------------------------------------------------------------------------------
# Event extraction  (PRE-001 s5.2)
# --------------------------------------------------------------------------------------

def _firm(charge_tag, charge_q_end, charge_val, assets=1000.0, rev_start_year=2018):
    """Twelve quarters of revenue, flat then declining, plus one impairment."""
    rows = []
    q = 0
    for y in range(rev_start_year, rev_start_year + 4):
        for m_end in ("03-31", "06-30", "09-30", "12-31"):
            val = 100 if q < 8 else 100 - (q - 7) * 5
            start = f"{y}-{ {'03-31':'01-01','06-30':'04-01','09-30':'07-01','12-31':'10-01'}[m_end] }"
            rows.append(_fact(start, f"{y}-{m_end}", val))
            q += 1
    assets_rows = [_fact(None, f"{y}-{m}", assets)
                   for y in range(rev_start_year, rev_start_year + 4)
                   for m in ("03-31", "06-30", "09-30", "12-31")]
    _qstart = {"03-31": "01-01", "06-30": "04-01", "09-30": "07-01", "12-31": "10-01"}
    charge_start = f"{charge_q_end[:4]}-{_qstart[charge_q_end[5:]]}"
    return _facts({"Revenues": rows, "Assets": assets_rows,
                   charge_tag: [_fact(charge_start, charge_q_end, charge_val)]})


def test_a_material_goodwill_charge_becomes_an_event_with_a_lag():
    f = _firm("GoodwillImpairmentLoss", "2021-12-31", 100.0)
    drops = defaultdict(int)
    evs = E.extract_events(f, "1", "TestCo", drops)
    assert len(evs) == 1
    assert evs[0]["tier"] == 3
    assert evs[0]["lag"] >= E.MIN_RUN


def test_a_charge_below_the_materiality_floor_is_dropped_and_counted():
    f = _firm("GoodwillImpairmentLoss", "2021-12-31", 5.0)      # 0.5% of assets
    drops = defaultdict(int)
    assert E.extract_events(f, "1", "TestCo", drops) == []
    assert drops["below_materiality"] == 1


def test_a_firm_with_no_deterioration_run_is_dropped_not_scored_as_zero():
    """Scoring 'never deteriorated' as lag 0 would be the single most dishonest bug available."""
    f = _firm("GoodwillImpairmentLoss", "2019-06-30", 100.0)    # charge lands during the flat era
    drops = defaultdict(int)
    assert E.extract_events(f, "1", "TestCo", drops) == []
    assert drops["no_deterioration_run"] == 1


def test_a_combined_rollup_is_dropped_when_its_components_are_already_counted():
    f = _firm("GoodwillImpairmentLoss", "2021-12-31", 100.0)
    f["facts"]["us-gaap"][E.COMBINED_TAG] = {
        "units": {"USD": [_fact("2021-10-01", "2021-12-31", 150.0)]}}
    drops = defaultdict(int)
    evs = E.extract_events(f, "1", "TestCo", drops)
    assert len(evs) == 1 and evs[0]["charge"] == 100.0
    assert drops["ambiguous_tier"] == 1


def test_annual_attribution_is_switchable_and_flagged():
    """A bias that runs in the hypothesis's favour has to be visible and switchable."""
    f = _firm("GoodwillImpairmentLoss", "2021-12-31", 100.0)
    f["facts"]["us-gaap"]["GoodwillImpairmentLoss"]["units"]["USD"] = [
        _fact("2021-01-01", "2021-12-31", 100.0, form="10-K")]
    on = E.extract_events(f, "1", "TestCo", defaultdict(int), include_annual_attributed=True)
    off = E.extract_events(f, "1", "TestCo", defaultdict(int), include_annual_attributed=False)
    assert len(on) == 1 and on[0]["annual_attributed"] is True
    assert off == []


def test_insufficient_history_is_dropped():
    f = _facts({"Revenues": [_fact("2020-01-01", "2020-03-31", 100)],
                "Assets": [_fact(None, "2020-03-31", 1000)]})
    drops = defaultdict(int)
    assert E.extract_events(f, "1", "TestCo", drops) == []
    assert drops["insufficient_history"] == 1


def test_every_drop_bucket_named_in_pre001_exists():
    assert set(E.DROP_BUCKETS) >= {
        "no_revenue_tag", "insufficient_history", "below_materiality",
        "no_assets_denominator", "no_deterioration_run", "right_censored",
        "ambiguous_tier", "duplicate_restated_fact"}


# --------------------------------------------------------------------------------------
# PRE-002 · peak-to-charge onset and the controls
# --------------------------------------------------------------------------------------

def test_ttm_needs_all_four_quarters():
    s = {100: 1, 101: 2, 102: 3, 103: 4}
    assert E.ttm(s, 103) == 10
    assert E.ttm(s, 104) is None


def test_peak_onset_finds_the_high_water_mark_not_a_streak():
    """The whole point of PRE-002: a wobble must not end the measurement."""
    s = {}
    for i in range(24):
        s[100 + i] = 100 if i < 8 else (60 if i != 12 else 95)   # peak, drop, one bounce, drop
    onset, _c = E.peak_onset(s, q_star=124)
    assert onset == 107               # last quarter of the TTM plateau, 17 quarters of lag
    assert 124 - onset == 17


def test_peak_onset_does_not_truncate_where_the_streak_rule_did():
    s = {100 + i: (100 if i < 8 else 60) for i in range(24)}
    streak, _ = E.deterioration_onset(s, q_star=124)
    peak, _ = E.peak_onset(s, q_star=124)
    assert streak is None or (124 - peak) > (124 - streak)


def test_a_firm_still_at_its_peak_yields_lag_one_rather_than_a_discard():
    s = {100 + i: 100 + i for i in range(24)}          # growing throughout
    onset, _c = E.peak_onset(s, q_star=124)
    assert 124 - onset == 1


def test_peak_onset_censors_when_the_maximum_sits_at_the_window_edge():
    s = {100 + i: 100 - i for i in range(40)}          # declining from before the window
    onset, censored = E.peak_onset(s, q_star=135)
    assert censored is True


def test_peak_onset_refuses_when_history_is_too_short():
    s = {100 + i: 10 for i in range(6)}
    assert E.peak_onset(s, q_star=106)[0] is None


def test_permutation_null_is_centred_on_zero():
    """If this fails, the statistic is mis-specified for the data and NO result is reportable."""
    events = [{"lag": (i * 7) % 13, "tier": i % 4} for i in range(120)]
    r = E.permutation_null(events, n_perm=300)
    assert abs(r["z_mean"]) < 0.25
    assert 0.7 < r["z_sd"] < 1.4


def test_permutation_null_recovers_a_planted_gradient():
    """A control that cannot detect an effect is not a control."""
    events = ([{"lag": 2, "tier": 0}] * 30 + [{"lag": 4, "tier": 1}] * 30
              + [{"lag": 6, "tier": 2}] * 30 + [{"lag": 8, "tier": 3}] * 30)
    r = E.permutation_null(events, n_perm=300)
    assert r["p_empirical"] < 0.01


def test_synthetic_power_rises_with_effect_size():
    pool = [2, 3, 4, 5, 6, 7, 8]
    weak = E.synthetic_power([11, 12, 18, 79], pool, effect_per_tier=0.0, n_trials=200)
    strong = E.synthetic_power([11, 12, 18, 79], pool, effect_per_tier=2.0, n_trials=200)
    assert weak["power"] < 0.10 < strong["power"]


def test_peak_and_streak_rules_are_both_reachable_from_extract_events():
    f = _firm("GoodwillImpairmentLoss", "2021-12-31", 100.0)
    a = E.extract_events(f, "1", "T", defaultdict(int), onset_rule="streak")
    b = E.extract_events(f, "1", "T", defaultdict(int), onset_rule="peak")
    assert len(a) == 1 and len(b) == 1
    assert b[0]["lag"] >= a[0]["lag"]        # the peak rule cannot see less than the streak rule


def test_pre001_onset_function_is_untouched_by_pre002():
    """PRE-001's result must stay reproducible. Its instrument is frozen, not corrected."""
    rev = _rev(100, [10, 10, 10, 10, 9, 8, 7, 6])
    assert E.deterioration_onset(rev, q_star=108) == (104, False)
