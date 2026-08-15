"""C09 · `REG-002` **E2** — *"§4.4 may not report it as the section's headline."*

**THIS FILE IS A TRIPWIRE, NOT A GUARD. READ THE NEXT THREE PARAGRAPHS BEFORE YOU ACT ON A
RED FROM IT.**

A guard fires when a constraint is *violated* and says **this is wrong**. A tripwire fires
when the machine-checkable **antecedent of a re-read** is satisfied and says something
different: **a human must now read this, because the machine cannot.** Same mechanism,
opposite speech act. Every assertion below is on an antecedent. **None of them is the
constraint**, and a red here is never, by itself, evidence of a violation.

`CONSTRAINT-INVENTORY-001` §3.4 is where the class is defined and why it exists; the
one-line version is that `-44` found sixteen rows whose named machine could not see the
constraint it was filed under, and the repair for an unrecognisable constraint is *a
machine on its antecedent and a human on its consequent*. The failure mode this file is
written against is stated there too: **a tripwire whose red message names a violation
teaches the next session to suppress it.** If you edit the messages below, keep them
saying *go and read this*.

WHAT THE CONSTRAINT IS, AND WHY NO MACHINE CAN CHECK IT
-------------------------------------------------------
`REG-002` E2 is conditional. It solves for δ₃\\*, the goodwill decay rate at which the
strict reversal breaks, and pre-commits:

> **If δ₃\\* < 0.010** — i.e. if a goodwill half-life shorter than about seventy years is
> enough to break the strict reversal — then τ = −1 is a knife-edge on an unsourced number
> and **§4.4 may not report it as the section's headline.**

`RESULT-REG-002` §1 records **δ₃\\* = 0.00789** and the falsifier as **FIRED**. So the
constraint is live, today, and `CONSTRAINT-INVENTORY-001` §2 calls it *the closest call in
the table*: §4.4 is *titled* for the validity region and the knife-edge is one bolded
paragraph lead inside it. Compliant — **on a reading**. What a section's *headline* is, is
a judgement about what a reader takes away, and no machine has ever been able to make it.

**WHICH FALSIFIER: E2, NOT E1.** Until `wealthTensor-45` this constraint was filed in
`CONSTRAINT-INVENTORY-001` §1, §2 and in two handoffs as `REG-002` **E1**. It is E2. The
citation survived because **both** falsifiers constrain §4.4's headline — E1 would have
downgraded the headline claim from *inverts* to *destroys* — so every check anyone ran
(does `REG-002` have an E1? does E1 talk about §4.4's headline?) came back yes. E1's
threshold is on mean τ, it is the one `RESULT-REG-002` §2 records as **mis-specified**, and
it did **not** fire. A tripwire whose red message sends the next session to an erratum
about absolute values, to look for a knife edge that is not discussed there, is a tripwire
that gets suppressed on first contact. Hence `test_the_warrant_is_still_E2_and_still_fired`
below: the warrant is asserted, at the scene, in the file that depends on it.

THE TWO ANTECEDENTS
-------------------
1. **§4.4's heading line, pinned byte-for-byte.** A section that is re-headlined is the one
   event after which *"the knife-edge is not the headline"* has to be re-established by a
   reader. Note the heading is `###`, not `##`; `-44`'s handoff said `##`, which is the
   same class of unchecked pointer as the E1 citation above and is corrected here.
2. **The knife-edge's position in the abstract, pinned as a floor.** §2's bullet names
   *"the knife-edge is promoted into the abstract's lead"* as the other re-read trigger.
   The abstract carries τ = −1 today in its **third** prose paragraph. The assertion is
   asymmetric on purpose: moving **earlier** is promotion and fires; moving later, or a new
   paragraph being inserted ahead of it, is not promotion and does not. A tripwire that
   fires on any edit to the abstract would be noise, and noise is how a tripwire dies.

WHAT THIS CANNOT DO
-------------------
It cannot read the section. §4.4 can be re-headlined in the reader's sense without its
`###` line changing — a bolded lead promoted, a paragraph reordered, the table's caption
rewritten — and this file will be green through all of it. It cannot see the abstract's
*emphasis*, only its paragraph order. It does not check compliance and it does not grade
it; `CONSTRAINT-INVENTORY-001` C09 stays `recog: PROXY`, `machine: TRIPWIRE`, and
**TRIPWIRE IS NOT COVERAGE** — C09 is in cell (b) before this file and in cell (b) after
it. What it can do is guarantee that the question is asked out loud at the two moments the
estate wrote down, in prose, and then never built.
"""
from __future__ import annotations

import pathlib
import re

import pytest

pytestmark = pytest.mark.tripwire

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_002 = ROOT / "docs/preregistration/REG-002-p3-section-4-4-disclosed-ladder.md"
RESULT_REG_002 = ROOT / "docs/preregistration/RESULT-REG-002.md"

#: `REG-002` E2's consequent and its antecedent, markdown stripped (see `_flat`).
E2_CONSEQUENT = "§4.4 may not report it as the section's headline"
E2_ANTECEDENT = "If δ₃ < 0.010"

#: §4.4's heading line, byte-for-byte at `a1fef70`. ANTECEDENT ONE.
SEC_44_HEADING = (
    "### 4.4 · The design has a validity region, "
    "and the disclosed numbers fall outside it"
)

#: 1-indexed prose paragraph of the abstract in which the knife-edge first appears, at
#: `a1fef70`. ANTECEDENT TWO — a floor, not an equality. See the module docstring.
KNIFE_EDGE_ABSTRACT_PARAGRAPH = 3

#: τ = −1 in any emphasis, with either the minus sign (U+2212) or the hyphen. The paper
#: writes it both bare (`Kendall τ = −1`) and bolded (`Kendall τ = **−1**`).
KNIFE_EDGE = re.compile(r"τ\s*=\s*\*{0,2}\s*[−-]\s*1")

_HEADING_44 = re.compile(r"^### 4\.4 · .*$", re.M)
_HEADING_45 = re.compile(r"^### 4\.5 · ", re.M)


def _flat(text: str) -> str:
    """Whitespace-collapsed and stripped of the markdown that carries no meaning here.

    `*`, `**` and the `\\` that escapes a literal `*` are emphasis and escaping, not
    content: `REG-002` writes `**If δ₃\\* < 0.010**` and a later pass may well unbold it.
    Flattening them is right for a WARRANT check, and would be wrong for a freeze —
    `-42`'s lesson runs the other way there, and `test_reg012_sec6_sec47_frozen.py` says so.
    """
    return " ".join(text.replace("\\", "").replace("*", "").split())


def paper() -> str:
    return PAPER.read_text(encoding="utf-8")


def abstract_paragraphs(text: str) -> list[str]:
    """The abstract's PROSE paragraphs, in order, excluding the keyword/JEL trailer."""
    start = re.search(r"^## Abstract$", text, re.M)
    assert start, "the manuscript no longer has an `## Abstract` heading"
    rest = text[start.end():]
    end = re.search(r"^## ", rest, re.M)
    assert end, "the abstract no longer ends at a following `##` heading"
    paras = [p.strip() for p in re.split(r"\n\s*\n", rest[: end.start()]) if p.strip()]
    out: list[str] = []
    for p in paras:
        if p.startswith("**Keywords:") or p.startswith("**JEL") or set(p) <= set("-"):
            break
        out.append(p)
    return out


def section_44(text: str) -> str:
    start = _HEADING_44.search(text)
    assert start, "§4.4's heading is gone from the manuscript"
    rest = text[start.start():]
    end = _HEADING_45.search(rest)
    assert end, "§4.5's heading is gone from the manuscript"
    return rest[: end.start()]


# --------------------------------------------------------------------------- the warrant


def test_the_warrant_is_still_E2_and_still_fired():
    """C09 exists only while `REG-002` E2 says what it says AND its antecedent fired.

    Two ways this tripwire could be left guarding nothing, both silent:
    the registration is reworded, or a re-run moves δ₃\\* above 0.010 so E2 never fires and
    §4.4 becomes free to headline τ = −1. `-42`'s rule for a conditional constraint —
    **assert the antecedent** — applies to the tripwire that watches it.
    """
    reg = _flat(REG_002.read_text(encoding="utf-8"))
    assert E2_CONSEQUENT in reg, (
        "REG-002 no longer contains E2's consequent. THIS TRIPWIRE HAS LOST ITS WARRANT — "
        "read the registration before trusting anything else in this file."
    )
    assert E2_ANTECEDENT in reg, (
        "REG-002 no longer states E2's threshold as `If δ₃* < 0.010`. LOST WARRANT."
    )

    result = RESULT_REG_002.read_text(encoding="utf-8")
    e2_row = next(
        (ln for ln in result.split("\n") if ln.startswith("| **E2** |")), None
    )
    assert e2_row is not None, (
        "RESULT-REG-002 §1 no longer carries an E2 row. LOST WARRANT: this tripwire "
        "cannot show that the constraint it watches is live."
    )
    assert "FIRED" in e2_row and "0.00789" in e2_row, (
        f"RESULT-REG-002's E2 row no longer reports δ₃* = 0.00789 as FIRED:\n  {e2_row}\n"
        "If a re-run put δ₃* at or above 0.010, E2 does not fire, §4.4 is free to headline "
        "τ = −1, and C09 IS NOT LIVE — retire this file rather than re-pinning it."
    )


def test_the_constraint_is_about_the_headline_not_the_mention():
    """E2 forbids a HEADLINE, and this file must not be read as forbidding the number.

    The knife-edge is reported in §4.4 — that is required, not forbidden; E2 constrains
    where it sits, not whether it appears. Asserting its presence is what keeps a later
    session from `-43`'s trap of repairing a placement constraint by deletion.
    """
    assert KNIFE_EDGE.search(section_44(paper())), (
        "§4.4 no longer states τ = −1 anywhere. E2 governs whether the knife-edge is the "
        "section's HEADLINE, not whether it is reported; REG-002 E2 requires δ₃* and its "
        "half-life to be reported. Deleting the number is not a way to comply."
    )


# ------------------------------------------------------------------- antecedent one


def test_sec_44_has_not_been_re_headlined():
    heading = _HEADING_44.search(paper()).group(0)
    assert heading == SEC_44_HEADING, (
        "TRIPWIRE · §4.4 WAS RE-HEADLINED. **THIS IS NOT A FAILURE AND NOTHING IS "
        "NECESSARILY WRONG.**\n"
        f"  pinned  {SEC_44_HEADING!r}\n  current {heading!r}\n\n"
        "GO AND READ §4.4 against REG-002 E2, which FIRED (δ₃* = 0.00789 < 0.010):\n"
        "  'τ = −1 is a knife-edge on an unsourced number and §4.4 may not report it as\n"
        "   the section's headline.'\n"
        "The old title carried the validity region, which is why the knife-edge was one\n"
        "bolded paragraph lead inside the section and not its headline. Ask, as a reader:\n"
        "does the NEW title make τ = −1 what the section is about?\n"
        "  NO  → re-pin SEC_44_HEADING in the SAME commit and say in the message that you\n"
        "        read it against E2. A pin moved in a later commit is a pin nobody read.\n"
        "  YES → that is the violation, and the repair is the title, not this file."
    )


# ------------------------------------------------------------------- antecedent two


def test_the_knife_edge_has_not_been_promoted_in_the_abstract():
    paras = abstract_paragraphs(paper())
    hits = [i for i, p in enumerate(paras, 1) if KNIFE_EDGE.search(p)]
    assert hits, (
        "TRIPWIRE · the knife-edge has left the abstract entirely. Not a violation of E2 — "
        "E2 governs §4.4 — but the pin below now describes nothing, so re-read §4.4's "
        "headline and either re-pin or retire the assertion, in the same commit."
    )
    first = min(hits)
    assert first >= KNIFE_EDGE_ABSTRACT_PARAGRAPH, (
        f"TRIPWIRE · THE KNIFE-EDGE MOVED FORWARD IN THE ABSTRACT — prose paragraph "
        f"{KNIFE_EDGE_ABSTRACT_PARAGRAPH} → {first}. **THIS IS NOT A FAILURE.**\n\n"
        "CONSTRAINT-INVENTORY-001 §2 wrote the trigger and never built it: C09 is 'worth "
        "re-reading the moment §4.4 is re-headlined or the knife-edge is promoted into "
        "the abstract's lead.'\n"
        "GO AND READ §4.4 against REG-002 E2, which FIRED (δ₃* = 0.00789 < 0.010). The "
        "question is not about the abstract — it is whether an abstract that now leads "
        "with τ = −1 has made it §4.4's headline in the only sense E2 can mean.\n"
        "  NOT THE HEADLINE → re-pin KNIFE_EDGE_ABSTRACT_PARAGRAPH in the SAME commit.\n"
        "  IT IS NOW        → E2 forbids it; repair §4.4, not this file."
    )


# ----------------------------------------------------------------------- non-vacuity
#
# `-43`: feed the thing its own forbidden state before trusting the green. Each control
# breaks exactly the one antecedent its assertion watches, and asserts the DETECTOR fires.


def test_a_re_headline_would_be_detected():
    mutated = paper().replace(
        SEC_44_HEADING,
        "### 4.4 · The ranking does not blur, it inverts: Kendall τ = −1",
        1,
    )
    assert _HEADING_44.search(mutated).group(0) != SEC_44_HEADING, (
        "VACUOUS — a rewritten §4.4 heading still compares equal to the pin."
    )


def test_a_promotion_into_the_abstract_lead_would_be_detected():
    paras = abstract_paragraphs(paper())
    assert not KNIFE_EDGE.search(paras[0]), (
        "the abstract's lead paragraph already carries the knife-edge, so the promotion "
        "assertion cannot distinguish promoted from not — READ §4.4 AGAINST E2."
    )
    promoted = paras[0] + " The composite inverts the ranking, Kendall τ = −1."
    assert KNIFE_EDGE.search(promoted), (
        "VACUOUS — KNIFE_EDGE does not match τ = −1 written into a lead paragraph."
    )


def test_the_knife_edge_pattern_matches_both_emphases_and_both_minus_signs():
    """The paper writes the same number four ways; a pattern that saw one would be a
    false green everywhere else. `-43`: assert the conjunction, not a conjunct."""
    for form in ("Kendall τ = −1.", "Kendall τ = **−1** at", "τ = -1", "τ=−1"):
        assert KNIFE_EDGE.search(form), f"KNIFE_EDGE misses {form!r}"
    for form in ("τ = +1", "τ = **+1**", "τ moves from −1 to −0.67"):
        assert not KNIFE_EDGE.search(form.replace("−1 to", "X to")), (
            f"KNIFE_EDGE matches {form!r}, which is not the knife edge"
        )


def test_a_lost_warrant_would_be_detected():
    assert E2_CONSEQUENT not in _flat("REG-002 has been rewritten and says nothing"), (
        "VACUOUS — the warrant check passes on a registration that lost the clause."
    )
    assert "FIRED" not in "| **E2** | where does the strict reversal break | not fired |"
