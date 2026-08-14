"""`REG-004` §6 · **α_eff may not be called "the" recognition rate — it is a function of δ.**

THE SIBLING, ONE SYMBOL OVER
----------------------------
`REG-003` §7 forbids rounding **α̂** to *"the recognition rate"*; the manuscript violated it
at six sites for two days and `-41` mechanised it in `test_reg003_sec7_rounding.py`.
**`REG-004` §6 forbids the same move for α_eff**, and nothing has ever watched it. The
manuscript is clean at all six α_eff sites today, which is precisely the state this estate's
doctrine says rots quietly: an unguarded invariant that happens to hold.

Aiming the guard at α̂ and calling the class covered is `-41`'s one-door tell pointed at the
GUARD rather than at the audit. **Three recognition rates live in this paper** — α̂ (the event
dates), α_ser (the series) and α_eff (the deferral measure) — and §4.10 exists to say they are
three different quantities. A linter that knows about one of them reports the paper clean on
the other two.

THE RULE IS PREDICATION, NOT VOCABULARY — AND THE FORBIDDEN CLAIM HAS A NAME
----------------------------------------------------------------------------
§6 does not ban writing α_eff near the phrase *"recognition rate"*; §4.10 does exactly that,
for a page, and the paragraph is the paper doing the right thing. What §6 forbids is the
**definite predication**: α_eff *is* THE recognition rate, a single number standing for a
quantity that in fact moves with δ. So a unit violates when it

  1. names a **recognition rate**, and
  2. carries **α_eff** — the symbol, or one of α_eff's published values, and
  3. carries **no marker of δ-dependence or plurality**.

Two doors, for the same reason `REG-003` §7's guard needed two: the manuscript can carry the
claim through the SYMBOL (α_eff written out) or through the VALUE alone (0.4368 … 0.4758,
the §4.10 table's column), and a guard watching only the symbol reports a sentence that says
*"the recognition rate is 0.476 per year"* as clean. That is the sixth-site defect of `-41`,
transposed: the number carries the claim the symbol was watched for.

THE CONTROL, BECAUSE A ZERO AGAINST A CLEAN DOCUMENT IS GREEN FOR FREE
-----------------------------------------------------------------------
`-37`: *a mutation that does not mutate reports your guard as weak.* `-40`: *a green case
that is green because the state was already there is the same defect as a red case that is
red for the wrong reason.* There is no pre-edit violating text here — the paper never
committed this one — so the red cases are:

* **the registration's own forbidden claim, verbatim** (`test_the_forbidden_claim_is_red`);
* **a mechanical MUTATION of the one real sentence the guard has to think about**
  (`test_the_qualifier_is_load_bearing`): §4.9's closing sentence reaches the noun-and-symbol
  stage and is saved by its δ-motion clause. Delete exactly that clause and the guard must go
  red. If it does not, the guard is passing that sentence for an incidental reason and its
  green on the manuscript means nothing.

And `test_the_guard_is_not_vacuous_on_the_manuscript` proves at least one real site reaches
the qualifier test at all, so the zero below is a zero the linter had to work for.

WHAT IT CANNOT DO
-----------------
It cannot see a claim made across two sentences, and it cannot see α_eff misused under a
paraphrase that names no recognition rate and prints no value. It watches the move `REG-004`
§6 names and exactly that one.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_004 = ROOT / "docs/preregistration/REG-004-p3-age-dependent-recognition.md"

#: §6's sentence, as the registration spells it. The warrant: if this is deleted or
#: restated, the guard says so rather than enforcing a rule the repository has dropped.
CONSTRAINT = 'That α_eff is "the" recognition rate — it is a function of δ.'

#: The governed noun phrase — the same one `REG-003` §7 governs, which is the point: the
#: paper has three rates and one English phrase for all of them.
NOUN = re.compile(r"recognition rate", re.I)

#: Door one — the symbol.
ALPHA_EFF = re.compile(r"α_eff")

#: Door two — the value. §4.10's own column, plus the two endpoints §4.9 prints. A unit
#: that puts one of these next to "the recognition rate" has made §6's forbidden claim
#: without ever writing the symbol the guard was watching.
ALPHA_EFF_VALUE = re.compile(r"0\.4368|0\.4388|0\.4431|0\.4538|0\.4758|0\.437\b|0\.476\b")

#: What satisfies §6: any mark that the quantity MOVES with δ, or that the paper is naming
#: one of several rates rather than the rate. Each of these is the manuscript's own wording
#: at a real site; none of them is a hedge, which is why compliance here costs no
#: defensive sentence (charter §2 — the repair for this class is a narrower claim, never a
#: caveat).
QUALIFIER = re.compile(
    r"function of δ"
    r"|α_eff\(δ\)"
    r"|runs from"
    r"|rises with the decay rate"
    r"|is not a constant"
    r"|holds α_eff fixed"
    r"|moving δ"
    r"|across the asserted rectangle"
    r"|three recognition rates"
    r"|three different quantities"
    r"|does not name one quantity"
    r"|misstates one end"
)


def units(text: str):
    """Sentences, plus table rows as their own units.

    Borrowed deliberately from `test_reg003_sec7_rounding.py`: §6's claim can be made in a
    table header — §4.10's own column header names α_eff — and a prose-only splitter would
    not look there. The convention that a table row is not prose belongs to
    `defensive_count.py` and does not travel to a reporting constraint.
    """
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
    """The unit reaches §6's question: it names a recognition rate AND carries α_eff.

    Split out from `rounds` so the non-vacuity test can ask how many units the guard
    actually had to adjudicate, rather than how many it flagged.
    """
    return bool(NOUN.search(unit)
                and (ALPHA_EFF.search(unit) or ALPHA_EFF_VALUE.search(unit)))


def calls_alpha_eff_the_rate(unit: str) -> bool:
    """§6's forbidden move, and exactly it."""
    return at_risk(unit) and not QUALIFIER.search(unit)


def violations(text: str) -> list[str]:
    return [u for u in units(text) if calls_alpha_eff_the_rate(u)]


# ---------------------------------------------------------------------------------------
# The real α_eff sites, verbatim from paper-III.md. Hard wraps flattened, because units()
# flattens; nothing else touched. These are the GREEN cases and they include every site a
# cruder cut — one watching the noun and the symbol without the qualifier — would flag.
# ---------------------------------------------------------------------------------------
LEGAL_SITES = [
    # §4.9 — the sentence the guard has to think about: noun, symbol, and the δ-motion
    # clause that makes it legal. A rule without QUALIFIER flags this one.
    "**A recalibration is therefore available and is not a repair:** any comparative static "
    "that holds α_eff fixed while moving δ is using the wrong derivative, and a single "
    "recognition rate quoted for a cross-section of asset lives misstates one end of it.",
    # §4.9's lead — symbol and values, no recognition-rate noun.
    "**An effective rate exists and it is not a constant.** Writing α_eff(δ) = δ Π(z)/(Π(z) − 1) "
    "returns the published form verbatim, R = (1 − φ)δ/(α_eff − δ).",
    "But α_eff runs from **0.437** per year at a forty-year life to **0.476** at a three-year "
    "one — a ninth of itself across the asserted rectangle, in the direction that a "
    "faster-decaying class behaves as though recognition were faster.",
    # §4.10's lead — the noun, plural, no value.
    "**Three recognition rates now live in this paper and they are three different quantities.**",
    # §4.10's table header — the symbol in a row, named for what it measures.
    "| disclosed life | δ per year | α̂, the event dates | α_ser, the series | α_eff, the "
    "deferral measure |",
    # §4.10's closing — the noun, and the refusal to let it name one quantity.
    "§4.9 says a single effective rate misstates one end of the asserted rectangle; the "
    "series adds that a single *recognition rate* does not name one quantity.",
]

#: `REG-004` §6's forbidden claim, made as an assertion. This is not invented prose: it is
#: the registration's own words with the "may not be claimed" frame removed, which is
#: exactly the sentence a future session would write.
FORBIDDEN_CLAIMS = [
    "α_eff is the recognition rate.",
    # The VALUE door: §6's claim with the symbol left out. §4.10's three-year-life column
    # entry, predicated as the rate.
    "The recognition rate is **0.4758** per year at a three-year life, and the ladder's "
    "magnitudes follow from it.",
    # A table row, because §4.10's numbers live in one.
    "| 3 years | 0.333 | the recognition rate, 0.4758 |",
]


def test_the_registration_still_says_this():
    flat = " ".join(REG_004.read_text(encoding="utf-8").split())
    assert " ".join(CONSTRAINT.split()) in flat, (
        "REG-004 §6's constraint is gone or restated. This guard has lost its warrant; "
        "read the registration before trusting anything else in this file."
    )


@pytest.mark.parametrize("claim", FORBIDDEN_CLAIMS, ids=range(len(FORBIDDEN_CLAIMS)))
def test_the_forbidden_claim_is_red(claim):
    """The registration's own forbidden claim, and the value-door version of it."""
    assert violations(claim) == [claim]


@pytest.mark.parametrize("site", LEGAL_SITES, ids=range(len(LEGAL_SITES)))
def test_the_legal_uses_are_not_flagged(site):
    """§4.10's whole point is that the paper carries three rates. It keeps its English."""
    assert violations(site) == []


def test_the_qualifier_is_load_bearing():
    """`-37`'s mutation test, on the one real sentence the guard must adjudicate.

    Strip the δ-motion clause out of §4.9's closing sentence — the smallest edit that turns
    it into §6's forbidden claim — and the guard must go red. A guard whose green survives
    the mutation is green for an incidental reason.
    """
    site = LEGAL_SITES[0]
    mutant = QUALIFIER.sub("uses α_eff", site)
    assert mutant != site, "the mutation did not mutate — the qualifier never matched"
    assert violations(site) == []
    assert violations(mutant) == [mutant]


def test_the_guard_is_not_vacuous_on_the_manuscript():
    """At least one real site reaches §6's question and is saved by its qualifier.

    Without this the zero below is a zero over an empty set: a linter whose predicate never
    fires reports every document clean, including one that violates the rule in a shape it
    cannot see.
    """
    reached = [u for u in units(PAPER.read_text(encoding="utf-8")) if at_risk(u)]
    assert reached, (
        "no unit of the manuscript names a recognition rate and carries α_eff. Either "
        "§4.10 has been rewritten or this guard's doors no longer match the paper's "
        "notation — check before trusting the green."
    )


def test_the_manuscript_calls_alpha_eff_the_rate_nowhere():
    found = violations(PAPER.read_text(encoding="utf-8"))
    assert found == [], (
        f"REG-004 §6 violated at {len(found)} site(s) — a unit names a recognition rate and "
        f"attaches α_eff with no mark that it moves with δ:\n  " + "\n  ".join(found)
    )
