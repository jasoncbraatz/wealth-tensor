"""SOURCE-001's source-probe numbers, pinned to the data they were read off.

WHY THIS EXISTS
---------------
`SOURCE-001` is not a registration and its tables are not results, which is exactly why
nothing was watching them -- and by `-25` they had become the thing REG-009's design is
being argued from. Three sessions have now written counts into that document from
committed JSON artifacts, and until this file there was no guard that the document and
the artifact still agreed. The failure mode is the one `test_restatement_reach` was built
for, one shelf down: a probe gets re-run, the JSON moves, and the prose keeps the old
number in a well-formed sentence.

It also closes the narrower hole that produced this file. `-24` committed
`data/source-001-concentration-full.json` specifically so that the panel count would be
auditable without 6,400 SEC calls -- and then nothing ever audited it. A committed
artifact with no reader is `-24`'s own banked lesson about undo rows: count the writers,
count the readers, be suspicious of any ratio with a zero in it.

WHAT IS PINNED, AND IN WHICH DIRECTION
--------------------------------------
Two separate assertions per figure, because they fail for different reasons:

  * INTERNAL -- the artifact's summary counters are recomputable from its own per-record
    rows. Catches a probe whose aggregation and detail disagree.
  * EXTERNAL -- the figure printed in `SOURCE-001` matches the artifact. Catches prose
    that outlived a re-run.

Offline: reads two JSON artifacts and one markdown file, fetches nothing.
"""
from __future__ import annotations

import json
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOC = ROOT / "docs" / "preregistration" / "SOURCE-001-sigma-and-lifetime.md"
BY_FYEND_2023 = ROOT / "data" / "source-001-lifetime-by-fyend.json"
BY_FYEND_2015 = ROOT / "data" / "source-001-lifetime-by-fyend-2015.json"
CONCENTRATION = ROOT / "data" / "source-001-concentration-full.json"


def _load(p: pathlib.Path) -> dict:
    if not p.exists():                                   # pragma: no cover
        pytest.skip(f"{p.name} not committed")
    return json.loads(p.read_text())


def _doc() -> str:
    return DOC.read_text()


# --------------------------------------------------------------------------------------
# 3b -- the by-fiscal-year-end coverage probe
# --------------------------------------------------------------------------------------

# (artifact, December canonical-life rate, non-December rate, all-rows rate) as printed
# in SOURCE-001 section 3b. Unconditional -- rows, not located submissions -- because
# that is what a firm-year join actually gets.
FYEND_CYCLES = [
    (BY_FYEND_2023, "2022-10-31 ... 2023-09-30", 0.824, 0.822, 0.823),
    (BY_FYEND_2015, "2014-10-31 ... 2015-09-30", 0.758, 0.681, 0.727),
]


def _split(art: dict) -> tuple[dict, dict, dict]:
    """(December, every-other-month, all) counters, recomputed from per-row records."""
    dec = {"rows": 0, "canon": 0}
    rest = {"rows": 0, "canon": 0}
    for r in art["rows"]:
        bucket = dec if r["fy_end"][5:7] == "12" else rest
        bucket["rows"] += 1
        bucket["canon"] += bool(r.get("canon"))
    allb = {k: dec[k] + rest[k] for k in dec}
    return dec, rest, allb


@pytest.mark.parametrize("path,window,_d,_o,_a", FYEND_CYCLES,
                         ids=[c[1][:7] for c in FYEND_CYCLES])
def test_fyend_artifact_summary_matches_its_own_rows(path, window, _d, _o, _a):
    """INTERNAL: the by_month counters are the per-row records, aggregated."""
    art = _load(path)
    dec, rest, allb = _split(art)
    stored_dec = art["by_month"].get("Dec", {})
    assert dec["rows"] == stored_dec.get("rows"), (
        f"{path.name}: December row count disagrees with its own records "
        f"({dec['rows']} recomputed vs {stored_dec.get('rows')} stored)")
    assert dec["canon"] == stored_dec.get("canon", 0)
    assert allb["rows"] == art["total"]["rows"]
    assert allb["canon"] == art["total"]["canon"]
    # every record is one of the two decomposed states, never a silent third
    assert {r["status"] for r in art["rows"]} <= {"submission", "no_submission"}
    # a no_submission record must not also claim a tag
    assert not [r for r in art["rows"]
                if r["status"] == "no_submission" and r.get("canon")]


@pytest.mark.parametrize("path,window,dec_rate,other_rate,all_rate", FYEND_CYCLES,
                         ids=[c[1][:7] for c in FYEND_CYCLES])
def test_fyend_rates_match_the_document(path, window, dec_rate, other_rate, all_rate):
    """EXTERNAL: section 3b's table is what the artifact says, to three decimals."""
    art = _load(path)
    dec, rest, allb = _split(art)
    for label, got, want in (("December", dec["canon"] / dec["rows"], dec_rate),
                             ("non-December", rest["canon"] / rest["rows"], other_rate),
                             ("all firm-years", allb["canon"] / allb["rows"], all_rate)):
        assert round(got, 3) == want, (
            f"{path.name}: {label} canonical-life coverage is {got:.3f}, but "
            f"SOURCE-001 section 3b prints {want:.3f}")
        assert f"{want:.3f}" in _doc(), (
            f"SOURCE-001 no longer prints {want:.3f} ({label}, {window})")


def test_3b_headline_no_december_advantage_now_and_one_then():
    """The claim section 3b is FOR: the gap closed. Pinned as a comparison, not a rate.

    Rates can both drift and keep their difference; the difference is the finding, so it
    is asserted directly rather than inferred from two pinned numbers.
    """
    now_dec, now_rest, _ = _split(_load(BY_FYEND_2023))
    then_dec, then_rest, _ = _split(_load(BY_FYEND_2015))
    gap_now = now_dec["canon"] / now_dec["rows"] - now_rest["canon"] / now_rest["rows"]
    gap_then = then_dec["canon"] / then_dec["rows"] - then_rest["canon"] / then_rest["rows"]
    assert abs(gap_now) < 0.02, (
        f"section 3b says the December advantage is gone in the recent cycle; it is "
        f"{gap_now:+.3f}")
    assert gap_then > 0.05, (
        f"section 3b says the 2014-15 cycle HAS a December advantage; it is {gap_then:+.3f}")
    # and the movement is carried by the non-December series, which is the actual finding
    rose_rest = now_rest["canon"] / now_rest["rows"] - then_rest["canon"] / then_rest["rows"]
    rose_dec = now_dec["canon"] / now_dec["rows"] - then_dec["canon"] / then_dec["rows"]
    assert rose_rest > rose_dec, (
        "section 3b's finding is that non-December coverage moved MORE than December's "
        f"({rose_rest:+.3f} vs {rose_dec:+.3f})")


def test_thin_buckets_are_declared_not_silently_dropped():
    """A refused bucket must be named in the artifact, so the refusal is auditable."""
    for path in (BY_FYEND_2023, BY_FYEND_2015):
        art = _load(path)
        thin = set(art["thin_months"])
        under = {m for m, b in art["by_month"].items()
                 if b["rows"] < art["thin_threshold"]}
        assert thin == under, (
            f"{path.name}: thin_months {sorted(thin)} does not match the buckets "
            f"actually under the threshold {sorted(under)}")
        assert "Dec" not in thin


# --------------------------------------------------------------------------------------
# 4b -- the dominant-asset concentration count, which had no reader until now
# --------------------------------------------------------------------------------------

# threshold -> (surviving firms, ppe, goodwill, intangibles) as printed in section 4b.
CONCENTRATION_TABLE = {
    "0.50": (255, 92, 107, 56),
    "0.60": (148, 60, 47, 41),
    "0.70": (99, 47, 18, 34),
    "0.80": (59, 32, 4, 23),
}
CLASS_ORDER = ("ppe", "goodwill", "intangibles")


def test_concentration_counts_are_recomputable_from_the_per_firm_records():
    """INTERNAL: -24 committed this file so the count would be auditable. Audit it."""
    art = _load(CONCENTRATION)
    assert art["n_matchable"] == len(art["firms"])
    for thr, (total, *by_class) in CONCENTRATION_TABLE.items():
        t = float(thr)
        winners = [f for f in art["firms"]
                   if f["shares"] and max(f["shares"].values()) >= t]
        assert len(winners) == total, (
            f"threshold {thr}: {len(winners)} firms recomputed from records, "
            f"SOURCE-001 section 4b prints {total}")
        counts = {c: 0 for c in CLASS_ORDER}
        for f in winners:
            top = max(f["shares"], key=lambda k: f["shares"][k])
            if top in counts:
                counts[top] += 1
        assert [counts[c] for c in CLASS_ORDER] == by_class, (
            f"threshold {thr}: composition {counts} does not match section 4b's "
            f"{dict(zip(CLASS_ORDER, by_class))}")


def test_concentration_headline_figures_are_still_in_the_document():
    """EXTERNAL: the 99-of-1,444 denominator REG-009's power calculation leans on."""
    doc = _doc()
    art = _load(CONCENTRATION)
    # the document thousands-separates; match how it prints, not how json stores
    for token in (f"{art['n_universe']:,}", f"{art['n_matchable']:,}", "99", "34"):
        assert token in doc, f"SOURCE-001 no longer prints {token!r}"
    assert len(art["refused"]) == 7, (
        "section 4b reports seven impossible shares refused by name; the artifact has "
        f"{len(art['refused'])}")


def test_the_impossible_share_guard_actually_fired_and_is_reported():
    """Section 4b calls the refusals 'the guard reporting for duty'. Check it reported."""
    art = _load(CONCENTRATION)
    assert art["refused"], "no refusals recorded -- section 4b says there are seven"
    doc = _doc()
    assert "704" in doc, (
        "section 4b names the largest refused share (an intangibles share of 704); "
        "that number is the guard's evidence and should not vanish silently")
