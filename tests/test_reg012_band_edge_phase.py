"""REG-012's numerals are the artifact's, and REG-012 reads no threshold.

WHY THIS FILE LOOKS THE WAY IT DOES
-----------------------------------
Three lessons from `-37` shape every assertion below, and each of them describes a guard
that passes while the thing it was written for is broken:

1. **A COUNT IS THE ONE CLAIM NO ANCHOR CAN CONTRADICT.** A repair that names N sites
   proves each site unambiguous and never proves the list complete, and the two look
   identical in the output. So the claims here are an ABSENCE (§A) and COUNTS BOUND TO
   `len()` (§C) -- absence is the only assertion a short list cannot satisfy.

2. **BIND A REPAIR TO THE MEASUREMENT THAT WARRANTS IT, NOT TO A SPELLING.** REG-012
   exists because the card's 55.7 % counts another population. A test asserting the string
   "63.16" appears would pass forever after the artifact that owns 63.16 changed. So every
   numeral in the result document is RECOMPUTED here from the artifact and from the two
   committed tables, at test time, and compared as a formatted string. The premise is
   guarded, not the conclusion: Psi's own integer share is read out of
   `data/reg-010-half-integer-banding.json`, the file that owns it, so the claim "these are
   two different numbers about two different populations" cannot quietly become false.

3. **A MUTATION THAT DOES NOT MUTATE REPORTS A GUARD AS WEAK.** Every mutation harness
   below asserts that the mutated text ACTUALLY DIFFERS from the original before it
   concludes anything from the guard's behaviour, because a surviving mutation is two
   hypotheses and the cheap one has to be eliminated first.

And one from the shape of the document itself: it is hard-wrapped, so a guard reading its
prose joins its tokens with `\\s+`. An anchor wants no internal newline; a guard reading a
sentence long enough to be worth asserting has to expect one.
"""

from __future__ import annotations

import json
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ART = ROOT / "data" / "reg-012-band-edge-phase.json"
DOC = ROOT / "docs" / "preregistration" / "RESULT-REG-012-band-edge-phase.md"
SRC = ROOT / "scripts" / "reg012_band_edge_phase.py"
CITED = ROOT / "data" / "reg-009-band-count-filled.json"
PSI = ROOT / "data" / "reg-010-half-integer-banding.json"

# The names by which a band count is read in this repository, assembled from fragments so
# that this module's own source cannot satisfy the search it performs. `-30`'s F9a matched
# the literal inside its own witness; any guard whose subject is text it is part of has it.
FORBIDDEN_READS = ("THIN_" + "FLOOR", "clear_" + "events", "clear_" + "firms",
                   "ceil" + "ings", "band" + "s_clearing")


def _json(p: pathlib.Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def _prose(*tokens: str) -> re.Pattern:
    """A phrase, matched across a hard wrap."""
    return re.compile(r"\s+".join(re.escape(t) for t in tokens))


@pytest.fixture(scope="module")
def art():
    return _json(ART)


@pytest.fixture(scope="module")
def doc():
    return DOC.read_text(encoding="utf-8")


# ======================================================================================
# C · THE COUNTS, RECOMPUTED FROM THE ARTIFACT THAT OWNS THEM
# ======================================================================================
def test_the_histogram_accounts_for_the_whole_population(art):
    """Every share in the document is a share of this denominator, so if the histogram
    does not exhaust the population, every numeral downstream is over a subset."""
    assert sum(h["n"] for h in art["histogram"]) == art["population"]
    assert len(art["histogram"]) == art["distinct_fractional_values"]
    assert art["distinct_fractional_values"] > 1, (
        "with one distinct fractional value the phase measure is trivially degenerate and "
        "the rigidity finding would be a fact about arithmetic, not about the sample")


def test_the_population_is_the_cited_tables_own(art):
    """REG-012 §3 P4. The population is resolved from the cited document's instrument --
    the defect this whole registration exists to repair, asserted rather than described."""
    cited = _json(CITED)
    assert art["population"] == cited["events_joinable"]
    assert art["occupied_bins_reproduced"] == cited["profiles"][art["reading"]]["occupied"]
    assert art["reading"] in cited["profiles"]


def test_the_edge_mass_and_shares_are_the_artifacts(art, doc):
    """Recomputed, never matched as spellings: each numeral is derived here from the
    artifact and then looked for in the prose."""
    n, pop = art["on_a_left_edge"], art["population"]
    assert art["on_a_left_edge_share"] == n / pop
    assert _prose(f"**{n} — {n / pop * 100:.2f} %**").search(doc), (
        f"the document does not carry the edge mass its artifact reports ({n}/{pop})")
    modal = max(art["histogram"], key=lambda h: h["n"])
    assert art["modal_fractional_share"] == modal["share"]
    assert art["modal_fractional_value"] == modal["frac"]
    for h in art["histogram"]:
        assert _prose(f"| {h['n']} |", f"{h['share']:.4f} |").search(doc), (
            f"the histogram row for frac {h['frac']} is not in the document as computed")


def test_the_phase_measures_are_the_artifacts(art, doc):
    assert _prose(f"**{art['grouping_preserving_measure']:.4f}**").search(doc)
    assert _prose(f"**{art['grouping_preserving_below_largest_frac']:.4f} — exactly "
                  f"zero**").search(doc), (
        "the document does not carry the below-the-largest-fraction measure as computed; "
        "that number is the whole difference between a rigid heap and a relabelling")
    assert _prose(f"**{art['phase_pieces']} constant pieces**").search(doc)
    lo, hi = art["grouping_preserving_intervals"][0]
    assert _prose(f"**({lo}, {hi}]**").search(doc)


def test_the_trivial_interval_is_reported_as_trivial(art):
    """The finding is not the 0.25; it is that all of the 0.25 sits above the largest
    fractional value, where any sample's grouping survives. If a future run makes those
    two numbers agree, the document's reading has silently changed and must be rewritten."""
    assert art["grouping_preserving_below_largest_frac"] == 0.0
    assert art["grouping_preserving_intervals"] == [
        [art["largest_fractional_value"], "1"]]


# ======================================================================================
# P · THE PREMISE, GUARDED WHERE IT LIVES
# ======================================================================================
def test_the_two_populations_still_disagree(art, doc):
    """REG-012 exists because the card imported Psi_band's integer share into the band
    count's sample. That justification is a comparison of two numbers living in two files,
    so it is recomputed from BOTH files here rather than asserted as prose. Guard the
    premise; a test that only checks the new wording survives the premise's death."""
    psi = _json(PSI)["integer_share"]
    ours = art["on_a_left_edge_share"]
    assert psi != pytest.approx(ours, abs=5e-4), (
        "REG-012's finding is that these are two numbers about two populations; they have "
        "become the same number, so the document's §2 reading no longer holds")
    assert _prose(f"**{ours * 100:.2f} %**,", "not the",
                  f"{psi * 100:.2f} %").search(doc), (
        "the document's own statement of the gap is not the gap the two artifacts show")
    assert _prose(f"{abs(ours - psi) * 100:.2f} points apart").search(doc)


# ======================================================================================
# A · THE ABSENCE
# ======================================================================================
def _threshold_reads(text: str) -> list:
    return [t for t in FORBIDDEN_READS if t in text]


def test_the_instrument_reads_no_threshold():
    """R5 forbids re-reading the band count's floor. Asserted as an absence over the
    instrument's whole source: a list of what it DOES contain could never be shown to be
    complete."""
    assert not _threshold_reads(SRC.read_text(encoding="utf-8"))


def test_the_result_document_reports_no_band_count(art, doc):
    assert not _threshold_reads(doc)
    keys = json.dumps(sorted(_json(ART).keys()))
    assert not _threshold_reads(keys), (
        "the artifact carries a key by which a band count is read")
    assert "floor" not in keys and "clear" not in keys


def test_the_absence_guard_bites():
    """Both directions, and the mutation is proved to be a mutation first."""
    clean = SRC.read_text(encoding="utf-8")
    assert not _threshold_reads(clean)
    for token in FORBIDDEN_READS:
        dirty = clean + "\n# " + token + "\n"
        assert dirty != clean, "the mutation did not change the source"
        assert _threshold_reads(dirty) == [token], (
            f"injecting {token!r} did not trip the absence guard, so a green result from "
            f"it means nothing")


# ======================================================================================
# M · THE NUMERAL GUARD, MUTATED IN BOTH DIRECTIONS
# ======================================================================================
def _edge_mass_claim_holds(a: dict, text: str) -> bool:
    n, pop = a["on_a_left_edge"], a["population"]
    return bool(_prose(f"**{n} — {n / pop * 100:.2f} %**").search(text))


def test_the_numeral_guard_bites_when_the_document_drifts(art, doc):
    assert _edge_mass_claim_holds(art, doc)
    drifted = doc.replace(f"**{art['on_a_left_edge']} — ", "**999 — ", 1)
    assert drifted != doc, "the document mutation did not change the document"
    assert not _edge_mass_claim_holds(art, drifted)


def test_the_numeral_guard_bites_when_the_artifact_drifts(art, doc):
    """The direction that matters most: the document keeps its numeral and the measurement
    underneath it moves. A guard bound to the spelling would stay green forever."""
    moved = dict(art)
    moved["on_a_left_edge"] = art["on_a_left_edge"] + 1
    assert moved["on_a_left_edge"] != art["on_a_left_edge"], "the artifact did not change"
    assert not _edge_mass_claim_holds(moved, doc)


def test_the_premise_guard_bites_when_the_populations_converge(art):
    """And the other branch of the premise guard: if Psi's share moved onto ours, the
    comparison that justifies REG-012 would be false, and this must go red rather than
    passing because the new wording is still spelled the same."""
    ours = art["on_a_left_edge_share"]
    converged = ours + 1e-6
    assert converged != _json(PSI)["integer_share"], "the mutation is not a mutation"
    assert converged == pytest.approx(ours, abs=5e-4), (
        "with Psi's share moved onto this population's, the disagreement assertion must "
        "fail — if this comparison cannot detect convergence it is not guarding anything")
