"""`REG-005` §7 and `REG-004` §6 · **the fitted lag distribution may not be claimed to
transfer to classes the PRE-002 sample does not cover.**

THE CONSTRAINT, IN BOTH FILES THAT CARRY IT
--------------------------------------------
`REG-005` §7's *may not be claimed* list: *"That the fitted lag distribution transfers to
classes the PRE-002 sample does not cover."* `REG-004` §6 says it from the other side and
names the classes: *"That the measured lag distribution is the right one for classes other
than those the sample covers; **the sample is retail and computer services**."*

This is the constraint with the largest gap between how easy it is to violate and how hard it
is to notice. §5.4 fits one lag distribution on 695 events from two SIC bands. §4.9 and §4.10
then use it to correct the deferral measure at **disclosed lives spanning the whole of ASC 360
and ASC 350-30-50 practice** — a rectangle of asset lives, not of industries. Every sentence
in that stretch is about *lives*, and a claim about *classes* can slip into one without a
single word changing register.

THE RULE IS PREDICATION, NOT VOCABULARY
----------------------------------------
A unit violates when it

  1. names the **fitted or measured lag distribution**, or the correction that is a function
     of it (§4.9's shape correction — `REG-004` §6 governs the correction's reach for the same
     reason it governs the distribution's), and
  2. makes a claim of **extension**: transfers to, generalises to, is the right one for, holds
     for any/all/other classes, beyond the sample, and
  3. names **no covered class scope** — retail, computer and data processing services, their
     SIC bands, or the ladder the correction was actually computed across.

**`travels` is deliberately not an extension verb.** §4.10's *"why the correction travels with
the lag distribution rather than with the filings"* is the paper making exactly the
distinction this constraint protects — the correction is a property of the fitted
distribution, which is *why* it does not come free with anyone's filings — and a keyword rule
watching for movement flags it. `-41`'s tell says a hand-audit that finds N sites found them
through one door; the sibling failure is a machine whose one door is a synonym list.

THE SCOPE TEST IS A NAMED CLASS, NOT THE WORD `sample`
-------------------------------------------------------
`REG-004` §6's own forbidden claim contains the phrase *"than those the sample covers"* — so a
scope test keyed on the word *sample* passes the registration's own example of the violation.
The qualifier has to be a class actually named. This is `-41`'s false-green in miniature and
it was caught by feeding the registration's words to the linter before trusting it.

WHAT IT CANNOT DO
-----------------
It cannot see the claim made across two sentences, and it cannot judge whether a scope named
in a unit is the RIGHT scope — a unit saying the distribution transfers to retail alone would
pass, and should be read by a human. It watches the move both registrations name.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_004 = ROOT / "docs/preregistration/REG-004-p3-age-dependent-recognition.md"
REG_005 = ROOT / "docs/preregistration/REG-005-p3-lag-shape-identifiability.md"

#: The two sentences that warrant this file.
CONSTRAINT_005 = ("That the fitted lag distribution transfers to classes the PRE-002 sample "
                  "does not cover.")
CONSTRAINT_004 = ("That the measured lag distribution is the right one for classes other than "
                  "those the sample covers")

#: The governed object: §5.4's fit, and the correction that is a function of it.
OBJECT = re.compile(
    r"(?:fitted|measured|estimated)\s+lag distribution"
    r"|shape correction"
    r"|correction to the measure"
    r"|correction of §4\.9",
    re.I,
)

#: A claim of extension past the sample. `travels with` is absent on purpose — see the
#: docstring; it is the manuscript's own phrase for the opposite point.
TRANSFER = re.compile(
    r"transfers?\s+to"
    r"|generalis\w+\s+to"
    r"|carries\s+over\s+to"
    r"|applies\s+(?:equally\s+)?to\s+(?:any|all|other|every)"
    r"|is\s+the\s+right\s+one\s+for"
    r"|holds\s+for\s+(?:any|all|every|other)"
    r"|for\s+(?:any|all|every|other)\s+(?:class|classes|sector|sectors|industry|industries)"
    r"|beyond\s+the\s+sample"
    r"|outside\s+the\s+sampled\s+classes"
    r"|economy-wide|industry-wide|across\s+all\s+classes",
    re.I,
)

#: A named covered scope. NOT the word `sample`: `REG-004` §6's own forbidden claim contains
#: "than those the sample covers", so keying on it would pass the registration's example.
SCOPE = re.compile(
    r"retail"
    r"|computer (?:and data processing )?services"
    r"|SIC 5\d{3}|SIC 7\d{3}"
    r"|classes ranked here"
    r"|tabulated (?:four-tier )?ladder"
    r"|the sampled classes",
    re.I,
)


def units(text: str):
    """Sentences, plus table rows as their own units — the estate's splitter for reporting
    constraints (`test_reg003_sec7_rounding.py`); §7's ledger row is where a transfer claim
    would be shortest and loudest."""
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


def at_risk(unit: str) -> bool:
    """The unit reaches the question: it names the fit and claims extension."""
    return bool(OBJECT.search(unit) and TRANSFER.search(unit))


def claims_transfer(unit: str) -> bool:
    return at_risk(unit) and not SCOPE.search(unit)


def violations(text: str) -> list[str]:
    return [u for u in units(text) if claims_transfer(u)]


# ---------------------------------------------------------------------------------------
# Real sites, verbatim from paper-III.md. Hard wraps flattened, because units() flattens.
# ---------------------------------------------------------------------------------------
LEGAL_SITES = [
    # §4.10 — the site a cruder rule flags. `travels with` is the paper drawing the
    # distinction this constraint exists to protect.
    "The shape correction of §4.9 is recoverable from a reported series, at a precision of "
    "one part in ten thousand per quarter that audited financial statements do not carry for "
    "the relevant quantity — which is why §5.4 dated impairments rather than fitting a series, "
    "and why the correction travels with the lag distribution rather than with the filings.",
    # the abstract — the correction's reach, scoped to the classes it was computed across
    "under a rising hazard there is no domain restriction, and the correction to the measure "
    "is under one per cent across the classes ranked here and 44% at a disclosed three-year "
    "life.",
    # §7's ledger row — the correction's two magnitudes, scoped to the ladder
    "| **The shape correction is small on the ranked ladder and large at disclosed lives** | "
    "measured lag distribution against a geometric of the same mean | the two agreeing, which "
    "would make the fitted shape decorative | **0.67%** across the tabulated ladder, **43.9%** "
    "at a disclosed three-year life |",
    # §4.9 — the model-side lag distribution, no fit and no extension claim
    "**R = (1 − φ)δ/(α − δ) is derived by summing a geometric**, and a geometric is the one "
    "lag distribution whose hazard does not depend on how long the gap has been open.",
    # §6.1's scope sentence, which is the paper's own statement of the covered classes
    "**Not supported:** that recognition lag scales with the unobservability of degradation, "
    "where unobservability is identified with GAAP asset class, in US-listed retail trade "
    "(SIC 5200–5999) or computer and data processing services (SIC 7370–7379), among "
    "registrants filing in 2013–2024.",
]

#: Both registrations' forbidden claims, made as assertions — the sentence a future session
#: would actually write — plus the value of feeding a registration its own words back.
FORBIDDEN_CLAIMS = [
    "The fitted lag distribution transfers to classes the PRE-002 sample does not cover.",
    "The measured lag distribution is the right one for classes other than those the sample "
    "covers.",
    "The shape correction holds for any class of asset with a comparable disclosed life.",
]


def test_both_registrations_still_say_this():
    for path, constraint in ((REG_005, CONSTRAINT_005), (REG_004, CONSTRAINT_004)):
        flat = " ".join(path.read_text(encoding="utf-8").split())
        assert constraint in flat, (
            f"{path.name} no longer carries C24's sentence. This guard has lost part of its "
            f"warrant; read the registration before trusting anything else in this file."
        )


@pytest.mark.parametrize("claim", FORBIDDEN_CLAIMS, ids=range(len(FORBIDDEN_CLAIMS)))
def test_the_forbidden_claim_is_red(claim):
    """Including `REG-004` §6's, which contains the words a lazy scope test would accept."""
    assert violations(claim) == [claim]


@pytest.mark.parametrize("site", LEGAL_SITES, ids=range(len(LEGAL_SITES)))
def test_the_legal_uses_are_not_flagged(site):
    assert violations(site) == []


def test_the_scope_qualifier_is_load_bearing():
    """`-37`'s mutation test, on the abstract's own sentence.

    Swap the named scope for an unnamed generality — the smallest edit that turns the
    abstract's claim into `REG-005` §7's forbidden one — and the guard must go red.
    """
    site = LEGAL_SITES[1]
    mutant = site.replace("across the classes ranked here", "for any class")
    assert mutant != site, "the mutation did not mutate"
    assert violations(site) == []
    assert violations(mutant) == [mutant]


def test_which_half_of_the_predicate_is_live_on_the_manuscript():
    """State what the green below actually means, rather than letting it imply more.

    `-40`: *a green case that is green because the state was already there is the same defect
    as a red case that is red for the wrong reason.* Here the honest reading is explicit —
    the manuscript names the fitted lag distribution at several sites (**OBJECT fires**), it
    makes extension claims about other things entirely — §4.7's repair restoring φ *"for every
    class that has one"*, §4.2's answer holding *"for every estimator"* — and **the two never
    meet in one unit**. So the linter's zero is a zero over a live object whose conjunction
    with TRANSFER is empty. The control for this file is carried by the two forbidden-claim
    tests and the mutation, not by the manuscript scan.

    **The conjunction is what this asserts, not either conjunct.** The first cut asserted
    TRANSFER fired nowhere in the document and went red on three legal sentences that have
    nothing to do with the lag distribution — a non-vacuity test scoped to a conjunct rather
    than to the predicate is a false alarm generator, which is the same defect as a linter
    scoped to a keyword rather than to a predication.
    """
    units_ = list(units(PAPER.read_text(encoding="utf-8")))
    named = [u for u in units_ if OBJECT.search(u)]
    paired = [u for u in units_ if at_risk(u)]
    assert named, (
        "no unit names the fitted or measured lag distribution. Either §5.4 and §4.10 have "
        "been rewritten or this guard's OBJECT no longer matches the paper's wording — check "
        "before trusting the green."
    )
    assert not paired, (
        "OBJECT and TRANSFER now meet in the same unit, which they did not when this guard "
        "was written. That is not itself a violation — the scope test below decides — but the "
        "manuscript scan is now doing real work and this docstring is out of date:\n  "
        + "\n  ".join(paired)
    )


def test_the_manuscript_claims_no_transfer():
    found = violations(PAPER.read_text(encoding="utf-8"))
    assert found == [], (
        f"C24 violated at {len(found)} site(s) — a unit claims the fitted lag distribution or "
        f"its correction reaches past the sampled classes, naming no covered scope:\n  "
        + "\n  ".join(found)
    )
