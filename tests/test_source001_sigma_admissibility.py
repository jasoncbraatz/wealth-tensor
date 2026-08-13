"""SOURCE-001 section 4c's numbers, pinned to the artifact they were read off.

WHY THIS EXISTS
---------------
Same reason `test_source001_coverage` exists, one section later: `SOURCE-001` is not a
registration, so nothing watches its tables, and by `-26` they are what REG-009's scope
is argued from. Section 4c makes a stronger claim than its predecessors -- that section
6 step 3's design sentence does not survive -- so its arithmetic needs a reader.

It also gives `data/source-001-sigma-admissibility.json` its first one, on the day it is
committed rather than a session later. `-24` committed the concentration artifact so its
count would be auditable and nothing audited it until `-25`; the interval is the defect,
and the fix is to write the test in the same commit as the data.

WHAT IS PINNED, AND IN WHICH DIRECTION
--------------------------------------
Two assertions per figure, because they fail for different reasons:

  * INTERNAL -- the artifact's aggregates are recomputable from its own per-firm rows,
    and the rows still agree with `source-001-concentration-full.json`, which is the
    upstream this probe did not fetch twice.
  * EXTERNAL -- the figure printed in `SOURCE-001` section 4c matches the artifact.
    Catches prose that outlived a re-run.

And one guard on the guards: the refusals this probe adds (`MATERIALITY_FLOORS`) and
inherits (`THIN`, `IMPOSSIBLE`) are asserted to still be wired in, because a refusal that
is silently removed reads exactly like a refusal that never fired.

Offline: reads two JSON artifacts and one markdown file, fetches nothing.
"""
from __future__ import annotations

import json
import math
import pathlib
import re
import statistics
from collections import Counter

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOC = ROOT / "docs" / "preregistration" / "SOURCE-001-sigma-and-lifetime.md"
ADMISS = ROOT / "data" / "source-001-sigma-admissibility.json"
CONCENTRATION = ROOT / "data" / "source-001-concentration-full.json"

CLASSES = ("ppe", "goodwill", "intangibles")


def _load(p: pathlib.Path) -> dict:
    if not p.exists():                                   # pragma: no cover
        pytest.skip(f"{p.name} not committed")
    return json.loads(p.read_text())


def _doc() -> str:
    return DOC.read_text()


def _s4c() -> str:
    """Section 4c only -- so a figure repeated elsewhere cannot satisfy a 4c assertion."""
    txt = _doc()
    start = txt.index("## 4c ")
    nxt = txt.find("\n## ", start + 1)
    return txt[start:] if nxt == -1 else txt[start:nxt]


def _ok(art: dict) -> list:
    return [r for r in art["firms"] if r.get("status") == "ok"]


def _two_proportion_z(k1, n1, k2, n2) -> float:
    p1, p2 = k1 / n1, k2 / n2
    p = (k1 + k2) / (n1 + n2)
    return (p1 - p2) / math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))


# ======================================================================================
# INTERNAL -- the artifact against itself, and against the upstream it inherited
# ======================================================================================

def test_every_dominant_firm_resolved() -> None:
    """No silent drop. 4c's denominators are all `of 99`, so 99 has to be all of them."""
    art = _load(ADMISS)
    assert art["n_dominant"] == 99
    assert len(art["firms"]) == 99
    assert len(_ok(art)) == 99, (
        "a firm with a non-ok status would silently shrink every denominator in 4c"
    )


def test_rows_agree_with_the_concentration_artifact() -> None:
    """The upstream `-24` committed, re-derived independently rather than trusted.

    This probe recomputes the matched period end and the class share from
    data.sec.gov instead of reading them out of the concentration file. A
    disagreement would mean one of the two is reading a different balance sheet --
    which is section 4a's defect class, and the reason it is asserted here.
    """
    art, conc = _load(ADMISS), _load(CONCENTRATION)
    stored = {f["cik"]: f for f in conc["firms"]}
    for r in _ok(art):
        s = stored[r["cik"]]
        assert r["end"] == s["end"], f"cik {r['cik']}: period end disagrees"
        assert r["share"] == pytest.approx(s["shares"][r["dominant"]], abs=1e-9), (
            f"cik {r['cik']}: class share disagrees with the concentration artifact"
        )
        assert r["dominant"] == max(s["shares"], key=s["shares"].get)


def test_composition_recomputes_from_rows() -> None:
    art = _load(ADMISS)
    assert Counter(r["dominant"] for r in _ok(art)) == {
        "ppe": 47, "goodwill": 18, "intangibles": 34
    }


def test_materiality_floor_counts_recompute_from_rows() -> None:
    """4c's headline table, every cell, from the per-firm assets alone."""
    rows = _ok(_load(ADMISS))
    expected = {
        0.0: (99, {"ppe": 47, "goodwill": 18, "intangibles": 34}),
        1e6: (64, {"ppe": 28, "goodwill": 17, "intangibles": 19}),
        1e7: (40, {"ppe": 19, "goodwill": 12, "intangibles": 9}),
        1e8: (18, {"ppe": 10, "goodwill": 7, "intangibles": 1}),
    }
    for floor, (n, comp) in expected.items():
        sub = [r for r in rows if r["assets"] >= floor]
        assert len(sub) == n, f"floor {floor:g}: count moved"
        assert Counter(r["dominant"] for r in sub) == comp, f"floor {floor:g}"


def test_the_shell_that_motivates_the_floor_is_really_there() -> None:
    """4c names a $388 filer. If it is gone, the section's motivating example is."""
    rows = _ok(_load(ADMISS))
    smallest = min(rows, key=lambda r: r["assets"])
    assert round(smallest["assets"]) == 388
    assert smallest["dominant"] == "ppe"
    assert smallest["share"] == pytest.approx(0.729, abs=5e-4)
    assert sum(1 for r in rows if r["assets"] < 1e6) == 35


def test_the_restriction_concentrates_small_filers_z_recomputes() -> None:
    """z = +6.18 and +7.86, recomputed from the two artifacts rather than quoted."""
    art, conc = _load(ADMISS), _load(CONCENTRATION)
    rows = _ok(art)
    thr = art["threshold"]
    complement = [f for f in conc["firms"]
                  if max(f["shares"].values(), default=0.0) < thr]
    for floor, want in ((1e6, 6.18), (1e7, 7.86)):
        z = _two_proportion_z(sum(1 for r in rows if r["assets"] < floor), len(rows),
                              sum(1 for f in complement if f["assets"] < floor),
                              len(complement))
        assert z == pytest.approx(want, abs=0.01), f"floor {floor:g}"
        assert z > 0, "the restriction must be concentrating, not diluting"


def test_median_assets_fall_monotonically_in_the_threshold() -> None:
    """4c's second table, and the claim that rests on it: tightening buys shells."""
    conc = _load(CONCENTRATION)
    meds, small = [], []
    for t in (0.50, 0.60, 0.70, 0.80):
        sub = [f for f in conc["firms"]
               if max(f["shares"].values(), default=0.0) >= t]
        meds.append(statistics.median([f["assets"] for f in sub]))
        small.append(sum(1 for f in sub if f["assets"] < 1e6) / len(sub))
    assert meds == sorted(meds, reverse=True), "median size must fall as the threshold rises"
    assert small == sorted(small), "the sub-$1M share must rise as the threshold rises"
    assert meds[2] / 1e6 == pytest.approx(4.76, abs=0.01)
    assert meds[3] / 1e6 == pytest.approx(1.28, abs=0.01)
    assert small[3] == pytest.approx(0.475, abs=5e-4)


def test_leverage_medians_recompute_at_the_ten_million_floor() -> None:
    rows = [r for r in _ok(_load(ADMISS)) if r["assets"] >= 1e7]
    assert len(rows) == 40
    assert statistics.median([r["ea"] for r in rows]) == pytest.approx(0.384, abs=5e-4)
    want = {"ppe": (19, 0.113), "goodwill": (12, 0.641), "intangibles": (9, 0.605)}
    for cls, (n, med) in want.items():
        sub = [r["ea"] for r in rows if r["dominant"] == cls]
        assert len(sub) == n, cls
        assert statistics.median(sub) == pytest.approx(med, abs=5e-4), cls
    assert want["ppe"][1] < want["goodwill"][1], (
        "4c's load-bearing direction: the PP&E arm is the MOST levered of the three"
    )


def test_leverage_z_and_the_no_floor_medians_recompute() -> None:
    rows = _ok(_load(ADMISS))
    at10 = [r for r in rows if r["assets"] >= 1e7]
    k = {c: (sum(1 for r in at10 if r["dominant"] == c and r["ea"] < 0.50),
             sum(1 for r in at10 if r["dominant"] == c)) for c in CLASSES}
    assert _two_proportion_z(*k["ppe"], *k["intangibles"]) == pytest.approx(2.04, abs=0.01)
    # the no-floor row, which 4c quotes precisely to show why a floor is needed first
    assert statistics.median([r["ea"] for r in rows]) == pytest.approx(0.052, abs=5e-4)
    assert statistics.median(
        [r["ea"] for r in rows if r["dominant"] == "ppe"]) == pytest.approx(-0.476, abs=5e-4)
    assert sum(1 for r in rows if r["ea"] < 0) == 49


def test_reach_two_instruments_agree_and_z_recomputes() -> None:
    art = _load(ADMISS)
    rows = _ok(art)
    listed = {int(k) for k, v in art["reach_current_registrant"].items() if v}
    last = {int(k): v for k, v in art["reach_last_fy_end"].items()}

    ppe = [r for r in rows if r["dominant"] == "ppe"]
    assert sum(1 for r in ppe if last[r["cik"]] <= 2019) == 38
    assert sum(1 for r in ppe if r["cik"] in listed) == 4
    assert statistics.median([last[r["cik"]] for r in ppe]) == 2016

    intan = [r for r in rows if r["dominant"] == "intangibles"]
    assert sum(1 for r in intan if r["cik"] in listed) == 14
    z = _two_proportion_z(4, len(ppe), 14, len(intan))
    assert z == pytest.approx(-3.49, abs=0.01)

    # the cross-check: the two instruments were never allowed to touch each other
    dead = [r for r in rows if last[r["cik"]] <= 2019]
    alive = [r for r in rows if last[r["cik"]] >= 2023]
    assert sum(1 for r in dead if r["cik"] in listed) == 0
    assert (sum(1 for r in alive if r["cik"] in listed), len(alive)) == (23, 32)


def test_structural_versus_terminal_recomputes() -> None:
    art = _load(ADMISS)
    ppe = [r for r in _ok(art) if r["dominant"] == "ppe"]
    with_lag = [r for r in ppe if r.get("share_lag") is not None]
    assert len(with_lag) == 31
    assert sum(1 for r in with_lag if r["share_lag"] >= art["threshold"]) == 17
    assert statistics.median(
        [r["share"] - r["share_lag"] for r in with_lag]) == pytest.approx(0.142, abs=5e-4)


def test_count_three_is_recorded_as_unmeasured_not_as_zero() -> None:
    """Section 3's error, refused in the artifact rather than only in the prose.

    An absent key would let a downstream reader treat count 3 as measured-and-null,
    which is the exact move that made section 3 declare a live route closed.
    """
    art = _load(ADMISS)
    assert art["count3_measured"] is False
    assert art["count3_reason"]
    assert not any("growth" in k for k in art["firms"][0])


def test_artifact_carries_its_provenance() -> None:
    """The convention `-24` set on the concentration artifact, kept.

    A committed artifact whose provenance is missing is a number with no way back
    to the run that made it, which is how section 3's conclusion outlived its
    evidence for two sessions.
    """
    prov = _load(ADMISS).get("provenance", "")
    assert "wealthTensor-26" in prov
    assert "source001_sigma_admissibility.py" in prov
    assert "NOT measured" in prov, "count 3's absence must survive in the provenance"


def test_the_refusals_are_still_wired_in() -> None:
    """A refusal that is silently removed reads exactly like one that never fired.

    `-25` found `aar.py`'s declaration branch had never once matched while every
    log line still printed the reassuring word. This asserts the constants, and the
    probe's own docstring naming them, are still present in the file that runs.
    """
    src = (ROOT / "scripts" / "source001_sigma_admissibility.py").read_text()
    assert "MATERIALITY_FLOORS = (0.0, 1e6, 1e7, 1e8)" in src
    assert "THIN = 30" in src
    assert "IMPOSSIBLE = 1.05" in src
    art = _load(ADMISS)
    assert art["materiality_floors"] == [0.0, 1e6, 1e7, 1e8]
    assert art["thin"] == 30 and art["impossible"] == 1.05


# ======================================================================================
# EXTERNAL -- the document against the artifact
# ======================================================================================

def test_doc_has_section_4c() -> None:
    assert "## 4c ·" in _doc()


@pytest.mark.parametrize("needle", [
    # the headline floor table
    "**99**", "ppe 47, gw 18, int 34", "$4.76M", "24 / 99 = 0.242",
    "ppe 28, gw 17, int 19", "18 / 64 = 0.281",
    "ppe 19, gw 12, int 9", "13 / 40 = 0.325",
    "ppe 10, gw 7, int 1", "4 / 18 = 0.222",
    # the concentration-of-shells result
    "z = +6.18", "z = +7.86", "**$388**",
    # the threshold trade
    "$1.28M", "0.475",
    # count 1
    "**0.113**", "0.641", "0.605", "**0.384**", "z = +2.04", "2.6 ×",
    "ppe −0.476", "intangibles −0.009",
    # reach
    "**38 / 47 = 0.809**", "**4 / 47 = 0.085**", "14 / 34 = 0.412",
    "z = −3.49", "**0 / 61**", "23 / 32",
    # structural vs terminal
    "**17 / 31 = 0.548**", "**+0.142**",
])
def test_doc_prints_the_artifact_figure(needle: str) -> None:
    """Every number section 4c states, asserted present in section 4c specifically."""
    assert needle in _s4c(), f"SOURCE-001 section 4c no longer prints {needle!r}"


def test_doc_does_not_claim_count_three_was_measured() -> None:
    s = _s4c()
    assert "NOT MEASURED" in s or "not measured" in s
    assert "delisted-inclusive" in s, (
        "the instrument that would close count 3 must stay named, or the gap "
        "degrades into an unexplained silence"
    )


def test_doc_refuses_the_n_equals_one_class_claim() -> None:
    """4c's own guard against repeating section 4b's error with the roles swapped.

    The $100M cell has one intangibles-dominant firm. A class conclusion drawn from
    it would be a zero cell read as a finding, which is the mistake 4b named.
    """
    s = _s4c()
    assert "n=1" in s or "n = 1" in s
    assert re.search(r"not made here|is not made", s), (
        "4c must explicitly decline the n=1 class claim, not merely avoid it"
    )


def test_the_corrections_4c_makes_are_wired_into_the_sections_they_correct() -> None:
    """A caveat that does not gate the conclusion is decoration -- this document's
    own finding, applied to its own cross-references.

    Section 4c overturns two sentences that live elsewhere in the file: section 4b's
    third consequence ("0.80 ... buys a much tighter restriction, which is exactly
    the trade section 2 cares about") and section 6 step 3's ("where the restriction
    is what makes it admissible under section 2"). Without this test a later edit
    could drop either pointer and leave 4c sitting beside the claim it reverses,
    with both reading as current. That is exactly how section 3's conclusion
    outlived its own bolded caveat for two sessions.
    """
    txt = _doc()
    for anchor, wants in (
        ("## 4b ", ("INVERTED BY §4c", "0.475")),
        ("## 6 ", ("§4c", "one count\n   doing three counts' work")),
        ("## 4 ", ("ONE COUNT OF THREE", "§4c")),
        ("## 2 ", ("§4c",)),
    ):
        assert anchor in txt, f"{anchor.strip()} vanished from SOURCE-001"
        start = txt.index(anchor)
        nxt = txt.find("\n## ", start + 1)
        section = txt[start:] if nxt == -1 else txt[start:nxt]
        for want in wants:
            assert want in section, (
                f"section {anchor.strip()} no longer carries 4c's correction: {want!r}"
            )


def test_step_five_is_marked_run_not_pending() -> None:
    """Section 6's own ledger. `-25` handed over "step 5 is the only cheap one left";
    if 4c lands and step 5 still reads as pending, the next session re-runs it."""
    txt = _doc()
    start = txt.index("## 6 ")
    nxt = txt.find("\n## ", start + 1)
    s6 = txt[start:] if nxt == -1 else txt[start:nxt]
    assert "**RUN — §4c" in s6, "step 5 must be marked run"
    assert "Step 6" in s6, "section 6 must name what replaces step 5"
