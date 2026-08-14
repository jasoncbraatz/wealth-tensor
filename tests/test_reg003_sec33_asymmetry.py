"""`REG-003` §3.3 is the SECOND reporting constraint in the same registration, and it is
CONDITIONAL — which is why nobody had ever checked it.

    **A low α̂ is strong evidence; a high α̂ is weak.** If α̂_yr lands in R3 or R4, the two
    known biases were working against that finding and it survives them. If it lands in R1
    or R2, the finding is exactly what two upward biases would manufacture, and **it must
    be reported with that sentence attached, in the same paragraph, not in a limitations
    section.**

`-41` mechanised `REG-003` §7 and stopped there, because §7 is the constraint the scouting
report happened to quote. §3.3 sits four sections earlier in the same file, governs the same
number, and differs from §7 in the two ways that made it invisible:

* **It is written at PARAGRAPH resolution, and it names its resolution twice** — *"in the
  same paragraph"* and *"not in a limitations section."* §7 is a sentence rule. A guard
  built on §7's splitter answers a question §3.3 did not ask.
* **It only fires in R1 or R2.** A constraint whose antecedent is an outcome cannot be read
  off the registration alone; you have to go and see which regime the run landed in.
  `RESULT-REG-003` §1 records **R1 in every cut** — pooled 0.4077, and 0.3940 to 0.4986
  across retail, computer services and all three registered sensitivities, every one of
  them at or above §3.2's 0.33 boundary. **The constraint fires, and has since the run.**

THE PART WORTH CARRYING FORWARD
--------------------------------
`-41`'s T1 rewrote the abstract to satisfy §7 and, incidentally, satisfied §3.3 there too —
the pre-edit abstract at `0b26a8a` said *"the recognition rate is 0.41 per year against a
calibration of 0.05"* and the post-edit one says *"...on both known biases' inflating side."*
**Nobody was aiming at §3.3.** The qualification arrived at exactly one site, and the four
other places the manuscript reports the finding did not get it — which is `SCOUT-001`'s own
diagnosis of §7 (*"a qualification that exists in the right paragraph and does not travel"*)
reproduced, in the same session that named it, by the repair for the other constraint.

WHAT THIS DOES NOT DO
---------------------
It does not ban reporting α̂. It does not require the asymmetry beside every mention of the
number: §4.10's three-rates table and §4.4's column headers use α̂ as a *parameter label* and
report no finding about it, and a guard that flagged those would push the paper to strip its
own cross-references. So the rule is predication, not vocabulary, exactly as §7's guard is:
**a unit violates §3.3 when it reports the estimate AS THE RESULT — the value together with
its interval, or against the calibration it overturns — and carries no word about the
direction the two registered biases push.**

THE CONTROL
-----------
`-37`: a mutation that does not mutate reports your guard as weak. `-40`: a green case that
is green because the state was already there is worth nothing. So the red proof feeds the
four real violating units verbatim from `paper-III.md` at `1e474b4` and requires all four to
be flagged, and the green proof feeds the real compliant abstract, the real §5.4 biases
paragraph, and the four real parameter-label sites a cruder cut flags — including the two
`REG-003` §7's own guard had to be taught to leave alone.

THE WARRANT, AND ITS SECOND HALF
---------------------------------
`-41`'s pattern: assert the registration still says it, so a deleted constraint reports a
lost licence instead of quietly enforcing a rule the repository dropped. **A conditional
constraint needs one more assertion than that: its ANTECEDENT.** If a future re-run landed
in R3 or R4 this rule would stop applying, and a guard that kept flagging would be enforcing
a live-looking rule against a world where it had gone quiet. So `test_the_trigger_is_still_
pulled` reads `RESULT-REG-003`'s own regime column and fails if the recorded regime is no
longer R1 or R2 — reporting a lost trigger, not a violation.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_003 = ROOT / "docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md"
RESULT_003 = ROOT / "docs/preregistration/RESULT-REG-003.md"

#: §3.3's sentence, as the registration spells it. Half one of the warrant.
CONSTRAINT = "it must be reported with that sentence attached, in the same paragraph, not in a"

#: §3.3's asymmetry, stated. Half one, continued — the guard enforces *this* sentence and
#: says so.
ASYMMETRY = "A low α̂ is strong evidence; a high α̂ is weak."

#: The two regimes in which §3.3 fires. §3.2's ladder: R1 is α̂_yr ≥ 0.33, R2 is
#: 0.19 ≤ α̂ < 0.33. Half two of the warrant.
FIRING_REGIMES = {"R1", "R2"}

#: The estimate, as the manuscript prints it in each of its two units.
ESTIMATE = re.compile(r"0\.40[0-9]|0\.41 per year|0\.1227")

#: What turns a mention of the estimate into a REPORT OF THE FINDING. Any one of these is
#: the paper saying *this is the result*: the interval it was measured with, the comparison
#: with the calibration it overturns, or the regime verdict itself.
AS_FINDING = re.compile(
    r"\[0\.383, 0\.432\]"
    r"|order of magnitude (?:above|below) the calibration"
    r"|calibration (?:used here )?(?:is|was) low by an order of magnitude"
    r"|against a calibration of 0\.05"
    r"|against the 0\.05 swept",
)

#: The registered direction, in the words the manuscript is free to choose. §3.3 registers
#: B1 (conditioning on a charge) and B2 (the onset bridge), both upward; the qualifier is
#: satisfied by any unit that says the estimate sits on their side.
QUALIFIER = re.compile(
    r"biases'? inflating side"
    r"|biases push this estimate up"
    r"|biased upward"
    r"|two upward biases"
    r"|a high α̂ is weak"
    r"|on the inflating side",
)


def flatten(text: str) -> str:
    """Whitespace-flatten, dropping blockquote markers.

    §3.3's own sentence lives inside a `>` blockquote, so a naive `" ".join(split())`
    leaves `>` tokens scattered through it and the warrant assertion fails against a
    registration that has not changed. A guard that cannot read its own licence is worse
    than no guard, because its red names the wrong thing.
    """
    return " ".join(
        line.lstrip().lstrip(">").strip() for line in text.splitlines()
    ).replace("  ", " ").strip()


#: A numbered or bulleted list item. §9's limitations are a single markdown block of four
#: numbered items, so a splitter that stopped at the blank line would grade all four as one
#: paragraph and report a violation at the wrong limitation. A list item is a paragraph's
#: worth of argument and is treated as one — the same judgement `units()` makes about a
#: table row, for the same reason.
LIST_ITEM = re.compile(r"^\s*(?:\d+\.|[-*+])\s+", re.M)


def units(text: str):
    """Paragraphs, plus table rows and list items as their own units.

    §7's guard splits to SENTENCES because §7 governs *sentences anywhere*. §3.3 governs
    what a PARAGRAPH carries, so this splitter stops at the blank line — and a guard that
    inherited §7's splitter would have graded §5.4's bolded lead against a rule that never
    mentioned sentences. Table rows stay their own units for §7's reason: the §7 survivals
    ledger reports findings in rows, and one of the four real sites is one.
    """
    for block in re.split(r"\n\s*\n", text):
        if block.lstrip().startswith("|"):
            for row in block.splitlines():
                if row.strip():
                    yield row.strip()
            continue
        if LIST_ITEM.search(block):
            pieces = [p for p in LIST_ITEM.split(block) if p and p.strip()]
            for piece in pieces:
                flat = flatten(piece)
                if flat:
                    yield flat
            continue
        flat = flatten(block)
        if flat:
            yield flat


def reports_unqualified(unit: str) -> bool:
    """§3.3's forbidden move, and exactly it."""
    if QUALIFIER.search(unit):
        return False
    return bool(ESTIMATE.search(unit) and AS_FINDING.search(unit))


def violations(text: str) -> list[str]:
    return [u for u in units(text) if reports_unqualified(u)]


# ---------------------------------------------------------------------------------------
# The four real sites, verbatim from paper-III.md at 1e474b4 — before wt108 ran.
# Hard-wraps flattened, because units() flattens; nothing else touched.
# ---------------------------------------------------------------------------------------
PRE_EDIT_SITES = [
    # §4.4 — reports the estimate, its interval, the calibration it overturns AND the R1
    # consequence (the rectangle inside the domain), with no word about the biases.
    "**That made the recognition rate, not the ordering, the quantity to establish first — "
    "and §5.4 establishes it.** On the registered sample the recognition rate PRE-002's "
    "instrument identifies is **α̂ = 0.408 per year**, 95% interval [0.383, 0.432]: the "
    "calibration used here is low by an order of magnitude, and the asserted rectangle lies "
    "inside the domain at the measured rate and across its 95% interval.",
    # §5.4's own lead paragraph — the section that produced the number, and the one line a
    # skimming referee reads. Its biases paragraph is three paragraphs below, which is the
    # section complying and the paragraph not.
    "**The peak-to-charge recognition rate is 0.41 per year, and the calibration was low by "
    "an order of magnitude.** Each event carries the interval from the onset of "
    "deterioration to the charge, right-censored at twenty quarters. The censored geometric "
    "maximum likelihood estimate is **α̂ = 0.1227 per quarter (se 0.0046), 0.408 per year, "
    "95% interval [0.383, 0.432]**; the median observed gap is five quarters.",
    # §7 survivals ledger — a table row, which is why units() keeps rows.
    "| **The peak-to-charge recognition rate is an order of magnitude above the "
    "calibration** | censored geometric MLE on 695 registered events, two universes, three "
    "sensitivities, four truncations | any cut returning a rate near the swept 0.05 | "
    "**α̂ = 0.408/yr** [0.383, 0.432]; range **0.327–0.499** across every cut, none "
    "containing 0.05 |",
    # §9 limitation 4 — reports the finding against the calibration inside the limitations
    # section. §3.3 names limitations explicitly as the place the qualification may NOT
    # live; a restatement of the finding there without it is the exile the clause forbids.
    "4. **φ and θ are not measured; they are swept.** α is measured, but for the quantity "
    "PRE-002's instrument dates rather than for the model's α: §5.4 estimates that rate at "
    "0.408 per year on the registered sample, against the 0.05 swept through the body, and "
    "finds the constant hazard the model assumes to be rejected.",
]

#: Real units that mention α̂ and violate nothing. The first is the abstract, which `-41`
#: made compliant without aiming at this constraint. The rest are the parameter-label sites
#: a cruder "flag any unit carrying 0.408" rule flags — and two of them are the very rows
#: `REG-003` §7's guard had to be taught to leave alone, so a guard that flagged them here
#: would have re-broken what that file went quiet on.
LEGAL_SITES = [
    # the abstract — compliant since 7088f6b
    "The same registered events establish it: **the peak-to-charge recognition rate is 0.41 "
    "per year against a calibration of 0.05, on both known biases' inflating side**, so the "
    "disclosed lives lie inside the model's domain.",
    # §5.4's biases paragraph — the qualification itself
    "**Two biases push this estimate up, and one pushes it down; the direction of each was "
    "registered before the number.** A gap that opened and was never recognised leaves no "
    "filing, so conditioning on a charge over-represents short intervals.",
    # §4.4's column header — α̂ as a parameter label, reporting nothing
    "| tier | φ | 1 − φ | δ | (1 − φ)δ | **R** at α = 0.05, the calibration | **R** at "
    "α̂ = 0.408, measured (§5.4) | **R** at α̂ = 0.327, the registered adverse cut | R at a "
    "common δ |",
    # §4.10's three-rates table — 0.408 as a row value, three quantities being distinguished
    "| 20 years | 0.050 | 0.408 | 0.4385 | 0.4388 |",
    # §7's domain row — the governed quantity is the rectangle's admissibility, not α̂; the
    # rate appears as the rate the test was run AT.
    "| **The *asserted* rectangle lies outside the model's domain *at the calibrated rate*** "
    "| useful lives spanning disclosure practice against α = 0.05, and the 683 disclosed "
    "pairs against the measured rate | any part of it admitting a steady-state deferral "
    "measure | **0%** admissible at α = 0.05; **all** of the asserted rectangle and "
    "**0.974** of the disclosed pairs at the measured α̂ = 0.408 |",
    # §5.4's memorylessness sentence — names α̂ as an average, reports no estimate
    "**The longer a gap has been open, the likelier it is to close** — which is the opposite "
    "of the memorylessness a single α encodes, and it means α̂ is an average over a window "
    "and not a constant of the technology.",
]


# ---------------------------------------------------------------------------------------
# The warrant
# ---------------------------------------------------------------------------------------
def test_the_registration_still_says_this():
    """If §3.3 is deleted or restated, this guard has lost its licence and says so."""
    flat = flatten(REG_003.read_text(encoding="utf-8"))
    assert ASYMMETRY in flat, (
        "REG-003 §3.3's asymmetry sentence is gone or restated. This guard enforces THAT "
        "sentence; it has lost its warrant and must be re-derived, not repaired."
    )
    assert CONSTRAINT in flat, (
        "REG-003 §3.3's attachment clause is gone or restated. The rule this file enforces "
        "-- same paragraph, not a limitations section -- no longer exists in the "
        "registration."
    )


def test_the_trigger_is_still_pulled():
    """The half of the warrant a non-conditional constraint does not need.

    §3.3 fires only in R1 or R2. If a re-run ever lands in R3 or R4 the manuscript is
    *released* from this rule, and a guard still flagging would be enforcing a rule that
    had gone quiet. So read the regime off `RESULT-REG-003`'s own verdict line.
    """
    flat = flatten(RESULT_003.read_text(encoding="utf-8"))
    recorded = set(re.findall(r"\*\*Verdict, A:\*\* \*\*(R[1-4])\*\*", flat))
    assert recorded, "RESULT-REG-003 no longer records a regime verdict for instrument A."
    assert recorded <= FIRING_REGIMES, (
        f"RESULT-REG-003 now records {sorted(recorded)}. §3.3 fires only in R1/R2, so this "
        f"guard has lost its TRIGGER, not merely its warrant: the manuscript is released "
        f"from the attachment rule and this file must be retired rather than satisfied."
    )


# ---------------------------------------------------------------------------------------
# The control: red on the real defect, green on the real legal text
# ---------------------------------------------------------------------------------------
@pytest.mark.parametrize("site", PRE_EDIT_SITES, ids=range(len(PRE_EDIT_SITES)))
def test_the_linter_sees_the_defect_it_was_written_for(site):
    assert reports_unqualified(site), (
        "A real pre-edit §3.3 violation is not flagged. The linter has been narrowed past "
        "the defect it exists for."
    )


@pytest.mark.parametrize("site", LEGAL_SITES, ids=range(len(LEGAL_SITES)))
def test_the_legal_uses_are_not_flagged(site):
    assert not reports_unqualified(site), (
        "A legal use of α̂ is flagged. This guard requires a qualifier where the estimate is "
        "reported AS THE RESULT, not everywhere the number appears."
    )


def test_the_two_proofs_are_disjoint():
    """A red set and a green set that overlap prove nothing about either."""
    assert not (set(PRE_EDIT_SITES) & set(LEGAL_SITES))


# ---------------------------------------------------------------------------------------
# The manuscript
# ---------------------------------------------------------------------------------------
def test_the_manuscript_attaches_the_registered_asymmetry():
    found = violations(PAPER.read_text(encoding="utf-8"))
    assert not found, (
        "REG-003 §3.3: the manuscript reports α̂ as the result without the registered "
        "asymmetry attached in the same paragraph. Every cut landed in R1, so the estimate "
        "is the reading two upward biases would manufacture and the registration requires "
        "that said where the number is said. The repair is a REPLACE -- name the direction "
        "inside the sentence that carries the number -- never a new hedging sentence.\n\n"
        + "\n\n".join(f"  * {u[:300]}" for u in found)
    )


def test_the_qualification_is_not_exiled_to_limitations():
    """§3.3's own placement clause, enforced as a placement.

    A manuscript could satisfy the rule above by carrying the asymmetry only inside
    §Limitations and nowhere else -- which is the exile §3.3 names and forbids in the same
    breath as the attachment.
    """
    text = PAPER.read_text(encoding="utf-8")
    body = re.split(r"\n#+ .*Limitations", text)[0]
    assert QUALIFIER.search(body), (
        "The registered asymmetry appears nowhere outside §Limitations. §3.3 forbids "
        "exactly that placement."
    )
