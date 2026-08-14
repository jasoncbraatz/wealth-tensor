"""REG-010's row, pinned — and the two things about it that a session could quietly undo.

WHAT EACH TEST IS PINNED AGAINST
--------------------------------
Nothing here runs `main()`: that would rewrite two tracked files and one day be blamed for
a dirty tree at the gate (`-30`'s lesson, paid for once already). The shifted and mirror
collapses are rebuilt from the instrument's PURE functions against D3's own lifted
midpoint, and the document's numerals are checked against the committed artifact.

The tests that would catch a real defect:

  * `test_the_two_conventions_differ_only_in_direction` — REG-010's finding is that Ψ moves
    0.0311 between two collapses that displace every life by the SAME distance. If that
    stops being true, the finding is no longer about direction and §4 of the result
    document is wrong. Rebuilt from the lifted rule over the whole population, not from
    the artifact.
  * `test_p3_is_not_re_scored` — the registration's Branch B, mechanised. The flattering
    reading was available (0.0050 against a five-point tolerance) and the estate's own
    defence against it is prose in two documents. This asserts the result document still
    says P3 FAILS and still contains no sentence rescuing it.
  * `test_the_bin_rule_is_never_retyped` — the band is D3's or it is nothing, in REG-010
    exactly as in the band count.
  * `test_every_stated_number_is_the_artifacts` — the document's Ψ values, deltas, shares
    and zero-band counts are read out of `data/reg-010-half-integer-banding.json` and
    matched against the prose, so a hand-edited numeral goes red.

WHAT IT CANNOT SEE
------------------
It cannot tell whether the shift is the RIGHT robustness row — there is no ground truth
about the granularity of a disclosed useful life, which is §6 of the result document. It
cannot see a rescue written in words it does not know; `FORBIDDEN` is a list of the
specific claims Branch B rules out, not a semantic check.
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
DOC = ROOT / "docs" / "preregistration" / "RESULT-REG-010-half-integer-banding.md"

sys.path.insert(0, str(SCRIPTS))

P3_FAIL_DELTA = 0.0650          # REG-009 §4's committed failure, restated by REG-010 §0
DIRECTION_GAP = 0.0311          # Ψ(registered) − Ψ(mirror), REG-010's finding

FORBIDDEN = (
    "p3 passes",
    "p3 now passes",
    "p3 holds",
    "rescues p3",
    "p3 is rescued",
    "the failure was an artefact",
    "the failure was an artifact",
)


def _assertions(md: str) -> str:
    """The document's own claims, with QUOTED material removed.

    REG-010 §3 quotes the flattering sentence in order to name and refuse it, and a bare
    substring scan cannot tell an assertion from a quotation of one the document rejects
    — the same shape as this estate's source-text guards firing on their own witness, one
    level up. So blockquotes and quoted spans are dropped before the scan, which makes the
    guard sharper rather than laxer: a rescue the document ASSERTS is still caught, and
    `test_the_rescue_scan_still_bites` proves it on a planted sentence.
    """
    body = "\n".join(ln for ln in md.splitlines() if not ln.lstrip().startswith(">"))
    body = re.sub(r'\*"[^"]*"\*', " ", body)
    body = re.sub(r'"[^"]*"', " ", body)
    return body.lower()


@pytest.fixture(scope="module")
def inst():
    import reg010_half_integer_banding as m

    return m


@pytest.fixture(scope="module")
def rules(inst):
    import reg009_ladder_inputs as li

    mid, _ = li.lift_band_rule()
    shifted, mirror = inst.shifted_rules(mid)
    return mid, shifted, mirror, li.BAND_WIDTH


@pytest.fixture(scope="module")
def all_lives():
    import reg009_ladder_inputs as li

    rows, _, _, _, _ = li.load_population(ROOT)
    return [float(r[f"L{i}_{rule}"])
            for r in rows for i in (0, 1) for rule in li.RULES]


@pytest.fixture(scope="module")
def art():
    return json.loads((DATA / "reg-010-half-integer-banding.json").read_text())


@pytest.fixture(scope="module")
def doc():
    return DOC.read_text()


# ======================================================================================
# THE RULE ITSELF — rebuilt from D3's lift, never from the artifact
# ======================================================================================
def test_the_bin_rule_is_never_retyped(inst):
    src = (SCRIPTS / "reg010_half_integer_banding.py").read_text()
    assert re.search(inst.BIN_RULE_PAT, src) is None, (
        "a bin index has been retyped in REG-010's instrument; the collapse is then a "
        "statement about that session's idea of a band, not about D3's")
    assert re.search(inst.BIN_RULE_PAT, "i" + "nt(v " + "// w)") is not None, (
        "the guard's own pattern no longer recognises a retyped bin index")


def test_an_integer_life_is_a_fixed_point_and_a_half_integer_is_not(rules):
    mid, shifted, mirror, w = rules
    for v in (1.0, 3.0, 5.0, 12.0):
        assert shifted(v, w) == pytest.approx(v), (
            "the whole point of REG-010's banding is that the integer heap sits at a bin "
            "CENTRE; if it moves, this is not the row §4 asked for")
        assert mid(v, w) == pytest.approx(v + w / 2)
    for v in (4.5, 5.5, 12.5):
        assert shifted(v, w) == pytest.approx(v + w / 2)
        assert mirror(v, w) == pytest.approx(v - w / 2)


def test_the_two_conventions_differ_only_in_direction(rules, all_lives):
    """REG-010 §4's finding, rebuilt from the population rather than read off the run."""
    mid, shifted, mirror, w = rules
    ds = [shifted(v, w) - v for v in all_lives]
    dm = [mirror(v, w) - v for v in all_lives]
    assert all(abs(abs(a) - abs(b)) < 1e-9 for a, b in zip(ds, dm)), (
        "the two conventions no longer move every life the same distance, so a Ψ they "
        "disagree about is no longer a disagreement about DIRECTION — REG-010 §4's "
        "finding is about a comparison that holds displacement fixed")
    disagree = [i for i, (a, b) in enumerate(zip(ds, dm)) if abs(a - b) > 1e-9]
    half = [i for i, v in enumerate(all_lives)
            if abs(v * 2 - round(v * 2)) < 1e-9 and abs(v - round(v)) >= 1e-9]
    assert disagree == half
    assert len(half) > 0, "no half-integer life is left, so the mirror is untested"


def test_the_shift_creates_a_band_the_estimator_cannot_consume(rules, all_lives):
    """C5, pinned: the hazard is real, and its subjects exist."""
    mid, shifted, mirror, w = rules
    assert all(mid(v, w) != 0.0 for v in all_lives), (
        "D3's own collapse has started producing a zero life; 1/L is then infinite")
    zeroed = [v for v in all_lives if shifted(v, w) == 0.0]
    assert zeroed, "C5's guard has lost its subjects and would now pass vacuously"
    import reg009_ladder_inputs as li

    assert all((1.0 / v) >= li.ALPHA_HAT for v in zeroed), (
        "a life the shift sends to zero would have been admissible on its own value, so "
        "a pair leaves the admissible set unannounced — C5 registered REFUSE here")


# ======================================================================================
# THE DOCUMENT — the numbers it prints are the record's
# ======================================================================================
def test_every_stated_number_is_the_artifacts(art, doc):
    p = art["psi"]
    for key, label in (("raw", "raw"), ("band", "D3"), ("shifted", "registered"),
                       ("mirror", "mirror")):
        val = p[f"pooled|R_MID|{key}"]["psi"]
        assert f"{val:.4f}" in doc, (
            f"the document does not print Ψ({label}) = {val:.4f}, which is what the run "
            f"recorded")
    for key in ("band", "shifted", "mirror"):
        assert f"{art['deltas'][key]:.4f}" in doc, (
            f"the document does not print |Ψ_{key} − Ψ| = {art['deltas'][key]:.4f}")
    for share in ("integer_share", "half_integer_share"):
        pct = f"{art[share] * 100:.2f} %"
        assert pct in doc, (
            f"the document does not print the {share.replace('_', ' ')} as {pct}, and "
            f"§1's whole claim is that the shift RELOCATES the heap between these two")
    for key in ("band", "shifted", "mirror"):
        assert str(art["zero_band"][key]["collapsed_to_zero"]) in doc


def test_the_direction_gap_is_the_one_the_document_claims(art):
    p = art["psi"]
    gap = abs(p["pooled|R_MID|shifted"]["psi"] - p["pooled|R_MID|mirror"]["psi"])
    assert gap == pytest.approx(DIRECTION_GAP, abs=5e-5), (
        "REG-010 §4 states the direction of a half-open interval is worth this much of Ψ; "
        "if the run no longer says so, the section is wrong")
    assert gap > art["deltas"]["shifted"], (
        "§4's claim that the direction effect exceeds the shifted-versus-raw difference "
        "no longer holds")


def test_p3_is_not_re_scored(art, doc):
    """The registration's Branch B, mechanised — the flattering reading was available."""
    assert art["deltas"]["band"] == pytest.approx(P3_FAIL_DELTA, abs=5e-5)
    assert art["inside_p3_tolerance"]["band"] is False
    assert art["inside_p3_tolerance"]["shifted"] is True, (
        "REG-010 landed on Branch A, so this test is guarding the wrong branch and its "
        "reasoning must be re-read rather than its constant adjusted")
    assert "P3 FAILS" in doc or "P3 fails" in doc
    claims = _assertions(doc)
    for phrase in FORBIDDEN:
        assert phrase not in claims, (
            f"the result document ASSERTS {phrase!r}. REG-010's registration fixed "
            f"Branch B before the run: a control that failed on the banding it was "
            f"registered against cannot be un-failed by a banding built afterwards.")


def test_the_rescue_scan_still_bites(doc):
    """The other branch of `_assertions`: dropping quotations must not drop claims."""
    planted = doc + "\n\nOn reflection the failure was an artefact of the translation.\n"
    assert any(p in _assertions(planted) for p in FORBIDDEN), (
        "a rescue asserted in the document's own voice is no longer caught — the "
        "quotation stripper has swallowed the claims along with the quotes")
    quoted = doc + '\n\nA careless session might write *"P3 passes"* here and be wrong.\n'
    assert not any(p in _assertions(quoted) for p in FORBIDDEN), (
        "a quoted-and-refused rescue is still being read as an assertion")


def test_the_document_carries_the_disclosed_qualifier_on_its_tables(art, doc):
    blocks = [b for b in doc.split("\n\n") if "|" in b and "---" in b]
    reporting = [b for b in blocks if "Ψ" in b]
    assert reporting, "no table in the document reports Ψ"
    assert any(art["qualifier"] in b for b in reporting), (
        "no table reporting Ψ carries the disclosed-versus-economic δ qualifier")


def test_the_result_sits_beside_p3s_failure_and_not_instead_of_it():
    """`-32`'s rule: a second reading of a committed measurement goes beside the first."""
    assert (ROOT / "docs" / "preregistration" / "RESULT-REG-009.md").exists()
    assert DOC.exists()
    reg009 = (ROOT / "docs" / "preregistration" / "RESULT-REG-009.md").read_text()
    assert "**P3 FAILS" in reg009, (
        "RESULT-REG-009 §4 no longer scores P3 as failing — REG-010 is a row beside that "
        "failure and has no meaning without it")
    assert "0.7236" in reg009 and "0.0650" in reg009, (
        "§4's committed numbers have moved; REG-010 reproduces them and would abort, but "
        "this says so at suite time rather than at run time")
