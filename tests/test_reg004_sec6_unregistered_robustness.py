"""`REG-004` §6 and `REG-005` §7, identical wording · **unregistered robustness may be
reported, LABELLED AS ROBUSTNESS, and may not change a verdict.**

WHAT THIS FOUND, WHICH IS THE REASON IT EXISTS
-----------------------------------------------
`CONSTRAINT-INVENTORY-001` graded C21 **compliant**, citing §5.4's shifted estimate: *"the
unregistered shifted estimate is 0.460"* — labelled, verdict-neutral, clean. That grade was
reached through the **`unregistered` keyword**, and the keyword finds the site that carries
the label. It cannot find the site that carries the OPPOSITE label.

The manuscript called the 0.327 cut **"the registered adverse cut"** at four sites, and at a
fifth *"the cut REG-003 registered in advance as the one that would break it."* `REG-003`
§3.1 **A3 registers three sensitivities** — annual-attributed excluded, right-censored
excluded, one event per firm — and §3.2's ladder registers no cut at all. Dropping the 175
events charged one quarter after the peak is **not among them**, and `RESULT-REG-003` §2, the
estate's own primary source, files it under the heading **"Unregistered robustness, reported
as robustness and not as result"** together with the three administrative truncations and the
shifted support.

So the inventory's own §0 tell — *when a hand-audit finds N sites, it found them through one
door* — applied to the inventory's own C21 row, one row after it applied the tell to the
sites. **The second door for a labelling constraint is the wrong label, not the missing one.**

THE TWO LIMBS, MECHANISED SEPARATELY BECAUSE THEY FAIL SEPARATELY
------------------------------------------------------------------
* **Limb A · the label is wrong.** A unit calls a cut *registered* while carrying a value no
  registration registers — or calls any cut *the registered adverse cut*, which is a claim
  about `REG-003` that is false on its face at every value, since `REG-003` registers
  sensitivities and a regime ladder and never an adverse cut.
* **Limb B · the label is missing.** A unit reports an unregistered value and carries no mark
  that it is robustness.

Limb A is deliberately NOT "the word *registered* appears near an unregistered number."
§5.4's own sentence names the three registered sensitivities and the three unregistered
truncations in one breath — legal, and a co-occurrence rule flags it. The rule is the
adjective's BOND to the cut, which is the move the four sites actually made.

RESOLUTION, AND WHY IT IS THE SENTENCE
---------------------------------------
`-41`: *a compliance grade applied at paragraph resolution against a sentence rule is a false
green.* §5.4's paragraph makes the registered/unregistered distinction perfectly clear to a
reader who reads the paragraph. §6 governs what is CLAIMED, unit by unit, and a table header
lifted into a slide deck carries its own label or none. Units here are sentences, and table
rows are units too — one of the five real sites is a §4.4 column header and another is a §7
ledger row.

WHAT IT CANNOT DO
-----------------
It cannot check the constraint's *verdict* limb in general — "may not change a verdict" is a
statement about the paper's reasoning, not about a string. It checks the limb that makes the
verdict limb auditable at all: **a number whose registration status is stated cannot silently
carry a verdict, because the next reader can see what it is.** And it keys on published
values, so a future cut with a new number must be added to one of the two lists below — which
is the committed-baseline pattern, not an oversight.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_003 = ROOT / "docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md"
REG_004 = ROOT / "docs/preregistration/REG-004-p3-age-dependent-recognition.md"
REG_005 = ROOT / "docs/preregistration/REG-005-p3-lag-shape-identifiability.md"
RESULT_REG_003 = ROOT / "docs/preregistration/RESULT-REG-003.md"

#: The constraint, word for word, in both files that carry it.
CONSTRAINT = ("Unregistered robustness may be reported, labelled as robustness, and may not "
              "change a verdict.")

#: `REG-003` §3.1 A3's three sensitivities, named. The allow-list is a READ of the
#: registration, not a judgement.
REGISTERED_SENSITIVITIES = ("annual-attributed charges excluded",
                            "right-censored events excluded",
                            "one event per firm")

#: What `RESULT-REG-003` §2 reports under the registered instrument: the pooled estimate, the
#: two universes, and the three sensitivities above. Values as the manuscript prints them.
REGISTERED_VALUES = ("0.408", "0.4077", "0.433", "0.394", "0.397", "0.499", "0.413")

#: What `RESULT-REG-003` §2 reports under **"Unregistered robustness"**: three administrative
#: truncations, the dropped-lag-one cut, and the shifted support.
UNREGISTERED_VALUES = ("0.396", "0.398", "0.404", "0.327", "0.460")

UNREGISTERED = re.compile("|".join(v.replace(".", r"\.") for v in UNREGISTERED_VALUES))

#: Limb A. Two shapes: *registered* bonded to a cut that carries an unregistered number, and
#: *registered adverse cut*, which is false at any number because no adverse cut is
#: registered. `sensitivities registered with PRE-002` matches neither, and must not.
#:
#: **`(?<!un)` is load-bearing and was paid for.** The first cut of this file omitted it, and
#: the linter went red on its own repair: *"the unregistered adverse cut"* CONTAINS
#: *"registered adverse cut"*. A guard that cannot tell a fix from the defect it fixes reports
#: every future repair as a violation — and the same substring bug had already bitten
#: `wt110`'s post-edit check ten minutes earlier, which is how it was recognised on sight
#: here. The post-edit sites are in `LEGAL_SITES` below so this cannot silently return.
REGISTERED_ADVERSE = re.compile(r"(?<!un)registered\s+adverse\s+cut", re.I)
REGISTERED_CUT = re.compile(r"(?<!un)registered\s+cut|cut\s+(?:that\s+)?REG-\d{3}\s+registered",
                            re.I)

#: Limb B. What counts as labelling a number robustness.
ROBUSTNESS_LABEL = re.compile(r"unregistered|robustness", re.I)


def units(text: str):
    """Sentences, plus table rows as their own units — `test_reg003_sec7_rounding.py`'s
    splitter, for the same reason: two of the five real sites are table rows."""
    for block in re.split(r"\n\s*\n", text):
        if block.lstrip().startswith("|"):
            for row in block.splitlines():
                if row.strip():
                    yield row.strip()
            continue
        flat = " ".join(block.split())
        for sentence in re.split(r"(?<=[.!?]) +(?=[A-Z*_\"'(§])", flat):
            if sentence.strip():
                yield sentence.strip()


def mislabels(unit: str) -> bool:
    """Limb A · an unregistered cut called registered."""
    if REGISTERED_ADVERSE.search(unit):
        return True
    return bool(REGISTERED_CUT.search(unit) and UNREGISTERED.search(unit))


def unlabelled(unit: str) -> bool:
    """Limb B · an unregistered value reported with no robustness label."""
    return bool(UNREGISTERED.search(unit)) and not ROBUSTNESS_LABEL.search(unit)


def violations(text: str) -> list[str]:
    return [u for u in units(text) if mislabels(u) or unlabelled(u)]


# ---------------------------------------------------------------------------------------
# The five real pre-edit sites, verbatim from paper-III.md at e947fb6 — the commit before
# wt110 ran. Hard wraps flattened, because units() flattens; nothing else touched.
# ---------------------------------------------------------------------------------------
PRE_EDIT_SITES = [
    # abstract — limb A, no value in the unit
    "The same registered events establish it: **the peak-to-charge recognition rate is 0.41 "
    "per year against a calibration of 0.05, on both known biases' inflating side**, so the "
    "disclosed lives lie inside the model's domain — 0.97 of the disclosed pairs at that rate "
    "and 0.81 at the registered adverse cut — and the hazard rises with the age of the gap "
    "rather than staying constant as the model assumes.",
    # §4.4's ladder table header — limb A and limb B, in a table row
    "| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** at α = 0.05, the calibration | **R** at "
    "α̂ = 0.408, measured (§5.4) | **R** at α̂ = 0.327, the registered adverse cut | R at a "
    "common δ |",
    # §4.4's τ sentence — limb A, no value
    "Kendall τ = **−1** at the calibrated rate, and **−0.67** at both the measured rate and "
    "the registered adverse cut, where the first rung alone turns over; the rung that "
    "separates them is identified below.",
    # §4.4's prose — limb A in its longest form, and limb B
    "At the cut REG-003 registered in advance as the one that would break it — the 175 events "
    "charged one quarter after the peak dropped, giving **0.327** — the rectangle's own "
    "fastest disclosed rate of 0.3333 is no longer cleared, and **0.814** of the pairs remain "
    "admissible.",
    # §5.4's bolded lead — limb B alone: no false label, no label at all
    "**The one cut that removes the mass where the onset bridge is least credible — the 175 "
    "events charged one quarter after the peak — gives 0.327, still an order of magnitude "
    "above the calibration.**",
    # §5.4's sensitivity sentence — limb B, and the site a co-occurrence rule gets wrong in
    # the other direction: it names the registered three and the unregistered three together
    "The three sensitivities registered with PRE-002 give 0.397, 0.499 and 0.413, and "
    "administratively censoring the sample at eight, twelve and sixteen quarters instead of "
    "twenty gives 0.396, 0.398 and 0.404.",
    # §7's survivals ledger — limb B, in a table row
    "| **The peak-to-charge recognition rate is an order of magnitude above the calibration** "
    "| censored geometric MLE on 695 registered events, two universes, three sensitivities, "
    "four truncations | any cut returning a rate near the swept 0.05 | **α̂ = 0.408/yr** "
    "[0.383, 0.432], on both known biases' inflating side; range **0.327–0.499** across every "
    "cut, none containing 0.05 |",
]

#: Real sentences that report a registered cut, or an unregistered one correctly labelled.
#: A guard that flags these is the ban-the-number guard this file exists not to be.
LEGAL_SITES = [
    # the one site the inventory graded on — correct, and it stays green
    "Against those, the sample contains no lag of zero, so fitting on a support that includes "
    "it understates α̂; the unregistered shifted estimate is 0.460.",
    # registered values, no label needed
    "The censored geometric maximum likelihood estimate is **α̂ = 0.1227 per quarter (se "
    "0.0046), 0.408 per year, 95% interval [0.383, 0.432]**; the median observed gap is five "
    "quarters.",
    "Retail gives 0.433 and computer services 0.394.",
    # a registered cut correctly called registered — limb A must not fire on this
    "The registered cut excluding right-censored events gives 0.499, the highest of the six.",
    # the ladder's verdict, stated over the registered cuts
    "**Every cut lands in the same regime,** and the calibrated 0.05 is outside the interval "
    "of all of them.",
    # ---- the POST-EDIT versions of five of the seven sites above -----------------------
    # The strongest control this file can carry: the same real sentences on both sides of
    # `wt110`, with the label as the only difference. Red before, green after, on text
    # neither side of the pair was invented for.
    "The same registered events establish it: **the peak-to-charge recognition rate is 0.41 "
    "per year against a calibration of 0.05, on both known biases' inflating side**, so the "
    "disclosed lives lie inside the model's domain — 0.97 of the disclosed pairs at that rate "
    "and 0.81 at the unregistered adverse cut — and the hazard rises with the age of the gap "
    "rather than staying constant as the model assumes.",
    "| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** at α = 0.05, the calibration | **R** at "
    "α̂ = 0.408, measured (§5.4) | **R** at α̂ = 0.327, the unregistered adverse cut | R at a "
    "common δ |",
    "Kendall τ = **−1** at the calibrated rate, and **−0.67** at both the measured rate and "
    "the unregistered adverse cut, where the first rung alone turns over; the rung that "
    "separates them is identified below.",
    "At the unregistered cut aimed at the doubt REG-003 §3.3 registered in advance — the 175 "
    "events charged one quarter after the peak dropped, giving **0.327** — the rectangle's "
    "own fastest disclosed rate of 0.3333 is no longer cleared, and **0.814** of the pairs "
    "remain admissible.",
    "As unregistered robustness, administratively censoring the sample at eight, twelve and "
    "sixteen quarters instead of twenty gives 0.396, 0.398 and 0.404.",
]


def test_the_constraint_still_says_this_in_both_files():
    for path in (REG_004, REG_005):
        flat = " ".join(path.read_text(encoding="utf-8").split())
        assert CONSTRAINT in flat, (
            f"{path.name} no longer carries C21's sentence. This guard has lost half its "
            f"warrant; read the registration before trusting anything else in this file."
        )


def test_the_registration_registers_three_sensitivities_and_no_adverse_cut():
    """The allow-list is a READ of `REG-003` §3.1 A3, and this is the read.

    If a future registration adds a cut, this test goes red and the lists above move in the
    same commit — which is the point of pinning the allow-list rather than inferring it.
    """
    flat = " ".join(REG_003.read_text(encoding="utf-8").split())
    for sensitivity in REGISTERED_SENSITIVITIES:
        assert sensitivity in flat, f"REG-003 §3.1 A3 no longer registers {sensitivity!r}"
    assert "adverse cut" not in flat, (
        "REG-003 now contains the phrase 'adverse cut'. If a cut has been registered, this "
        "guard's limb A is enforcing a rule the registration has changed — read §3.1."
    )


def test_the_result_document_files_these_five_as_unregistered():
    """The warrant for the allow-list's other half, from the primary source.

    `RESULT-REG-003` §2's heading is what makes *"the registered adverse cut"* false rather
    than merely unfortunate. If that heading moves, this guard is enforcing an obsolete
    reading and says so.
    """
    flat = " ".join(RESULT_REG_003.read_text(encoding="utf-8").split())
    heading = "**Unregistered robustness, reported as robustness and not as result.**"
    assert heading in flat, "RESULT-REG-003 §2's unregistered-robustness heading is gone"
    tail = flat.split(heading, 1)[1][:600]
    for value in UNREGISTERED_VALUES:
        assert value in tail, (
            f"{value} is no longer reported under RESULT-REG-003 §2's unregistered heading; "
            f"the allow-list above and the result document disagree."
        )


@pytest.mark.parametrize("site", PRE_EDIT_SITES, ids=range(len(PRE_EDIT_SITES)))
def test_the_linter_sees_the_defects_it_was_written_for(site):
    """RED at seven. Without this the zero below is green for free."""
    assert violations(site) == [site]


@pytest.mark.parametrize("site", LEGAL_SITES, ids=range(len(LEGAL_SITES)))
def test_the_legal_uses_are_not_flagged(site):
    """Registered cuts keep their adjective; a labelled unregistered one keeps its number."""
    assert violations(site) == []


def test_the_guard_is_not_vacuous_on_the_manuscript():
    """Every unregistered value is still IN the manuscript, so the zero below is earned.

    A linter reporting no unlabelled unregistered numbers because the numbers were quietly
    deleted is `-40`'s green-for-free in its cheapest form. §5.4 reports all five; if one
    goes, this says so before the scan's zero is read as compliance.
    """
    flat = " ".join(PAPER.read_text(encoding="utf-8").split())
    missing = [v for v in UNREGISTERED_VALUES if v not in flat]
    assert not missing, (
        f"the manuscript no longer reports {missing} — the C21 scan below is now green over "
        f"a smaller set than the one it was written for. Check §5.4 before trusting it."
    )


def test_the_manuscript_labels_every_unregistered_cut():
    found = violations(PAPER.read_text(encoding="utf-8"))
    assert found == [], (
        f"C21 violated at {len(found)} site(s) — a unit calls an unregistered cut registered, "
        f"or reports one of {UNREGISTERED_VALUES} with no robustness label:\n  "
        + "\n  ".join(found)
    )
