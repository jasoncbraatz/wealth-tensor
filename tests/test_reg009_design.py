"""wealthTensor-27 · REG-009 §1 — the design step, held as assertions.

Two jobs, and they are different in kind.

(1) THE CITATION REPAIR (§1.5) STAYS APPLIED. SOURCE-001 §2 sent readers to paper III §4.8
    for the useful-life/T coincidence argument. §4.8 does not make it — its stated virtue is
    that its claim "does not require inferring a physical decay rate from a reporting rule".
    The argument is in §4.7, with its weak joint attached. A pointer that is merely correct
    today and unheld is decoration, which is `-26`'s own finding about `-25`'s pointers.

(2) THE GREP TELL BEHIND §1.3 STAYS INTERPRETABLE. The finding is that each of §4.7's three
    bounds on its weak joint occurs exactly once at `e216037` — in the sentence that declares
    it — which by `-26`'s rule marks an objection nobody answered.

    Counts are pinned PER FILE, not as a total, and that shape was bought the hard way: the
    first version of this test totalled the corpus and failed immediately, because (a) this
    file names the needles in its own parametrisation, and (b) §1.5's repair RESTATES the
    three bounds while flagging them unanswered. To a grep, the repair and the failure mode
    look identical. Per-file pins make a new occurrence declare itself — a bound word
    appearing in `scripts/` or a `RESULT-*` means somebody MEASURED it, which is the event
    this test exists to be told about.
"""

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE001 = ROOT / "docs" / "preregistration" / "SOURCE-001-sigma-and-lifetime.md"
REG009 = ROOT / "docs" / "preregistration" / "REG-009-p3-lifetime-sourced-delta.md"
PAPER3 = ROOT / "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md"
SELF = pathlib.Path(__file__).resolve()

SEARCH_GLOBS = ("docs/**/*.md", "scripts/**/*.py", "tests/**/*.py")

# Excluded from every count, with the reason, because an unexplained exclusion is how a
# guard quietly stops guarding:
#   REG009 — reports the finding; counting it would let the document refute itself by
#            being written.
#   SELF   — names every needle in its own parametrisation and messages.
EXCLUDED = {REG009.resolve(), SELF}


def _ws(s: str) -> str:
    """Collapse whitespace. A substring assertion that a line wrap can break is a test
    about the text editor, not about the document."""
    return re.sub(r"\s+", " ", s)


def _corpus():
    for g in SEARCH_GLOBS:
        for p in sorted(ROOT.glob(g)):
            rp = p.resolve()
            if ".venv" in p.parts or "__pycache__" in p.parts or rp in EXCLUDED:
                continue
            yield p, p.read_text(encoding="utf-8", errors="replace")


def _by_file(needle: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for p, text in _corpus():
        c = len(re.findall(re.escape(needle), text, flags=re.IGNORECASE))
        if c:
            out[p.relative_to(ROOT).as_posix()] = c
    return out


P3 = "docs/papers/paper-III-dual-tensor/paper-III.md"
S1 = "docs/preregistration/SOURCE-001-sigma-and-lifetime.md"

# Pinned AFTER §1.5's repair. Every entry is a design/registration document; none is a
# script, a RESULT or a data artifact, which is the whole point.
PINNED = {
    "sticky": ({P3: 1, S1: 1},
               "bound 2 (lives are sticky within a firm) — REG-009 §2's P0-a measures this"),
    "industry-median": ({P3: 1},
                        "bound 3 (the design can run on industry medians) — P0-b measures this"),
    "industry convention": ({P3: 1, S1: 2},
                            "bound 1 (lives are anchored by industry convention) — P0-b"),
    "closely enough": ({S1: 1},
                       "§1.5's tell — the quantifier that unpicked the §4.8/§4.7 misattribution"),
}


# --------------------------------------------------------------------------- (1)

def test_reg009_exists_and_declares_it_does_not_license_a_run():
    assert REG009.exists(), "REG-009 §1 is the wealthTensor-27 deliverable"
    t = _ws(REG009.read_text(encoding="utf-8"))
    assert "DOES NOT YET LICENSE A RUN" in t, (
        "REG-009 §1 is a design step. A registration that licenses a run before its "
        "falsifiers exist is the shape SOURCE-001 was written to avoid."
    )


def test_source001_no_longer_attributes_the_coincidence_argument_to_4_8():
    t = _ws(SOURCE001.read_text(encoding="utf-8"))
    assert "§4.8 already argues" not in t, (
        "REG-009 §1.5's repair has been reverted. §4.8 does not argue that a disclosed "
        "useful life and the model's T coincide; §4.7 does, and §4.8's stated virtue is "
        "the opposite move."
    )
    assert "weak joint" in t, (
        "The repair must retarget the citation AND carry §4.7's weak joint with it. "
        "A licence that travels without its bound is what the repair was for."
    )


def test_paper_iii_4_8_still_declines_to_infer_delta_from_a_reporting_rule():
    """The premise of the repair, held against the manuscript rather than assumed."""
    t = _ws(PAPER3.read_text(encoding="utf-8"))
    assert "does not require inferring a physical decay rate from a reporting rule" in t, (
        "§4.8's disclaimer is the evidence that it is not the section SOURCE-001 wanted. "
        "If §4.8 was rewritten, REG-009 §1.5 needs re-deciding, not this test loosening."
    )


def test_paper_iii_4_7_still_names_its_weak_joint():
    t = _ws(PAPER3.read_text(encoding="utf-8"))
    assert "chosen by the same management whose timeliness is being measured" in t, (
        "§4.7's weak joint is what REG-009 §1.3 is about. If it moved, §1.3 moves with it."
    )


# --------------------------------------------------------------------------- (2)

@pytest.mark.parametrize("needle", sorted(PINNED))
def test_bound_keyword_locations_are_pinned_per_file(needle):
    expected, bound = PINNED[needle]
    actual = _by_file(needle)
    assert actual == expected, (
        f"'{needle}' moved: expected {expected}, found {actual}. This is {bound}.\n"
        f"If a script/ or RESULT-* file gained it, somebody MEASURED it — that is the "
        f"work REG-009 §1.3 asked for. Update §1.3, move the bound into the discharged "
        f"column of §3's definition-of-done item 5, and re-pin here.\n"
        f"If another design doc merely RESTATED it, that is the failure mode §1.3 is "
        f"about: an assertion repeated is not an assertion answered."
    )


def test_no_bound_has_leaked_into_a_script_or_a_result():
    """The invariant that actually matters, stated independently of the counts above:
    a MEASUREMENT of any bound would land in scripts/ or in a RESULT document."""
    offenders = {}
    for needle in ("sticky", "industry-median", "industry convention"):
        for path, n in _by_file(needle).items():
            if path.startswith("scripts/") or "/RESULT-" in path or path.startswith("data/"):
                offenders[f"{needle} @ {path}"] = n
    assert not offenders, (
        f"A §4.7 bound now appears in an instrument or a result: {offenders}. If that is a "
        "measurement, REG-009 §1.3's finding is discharged in part — say so there and in "
        "§3's item 5 rather than leaving the design doc claiming it is unanswered."
    )


# --------------------------------------------------------------------------- DoD

def test_reg009_carries_a_definition_of_done_and_a_stopping_rule():
    t = _ws(REG009.read_text(encoding="utf-8"))
    assert "DEFINITION OF DONE" in t, (
        "The standing rule: write the definition of done into the first handoff. This "
        "thread spent four sessions on a source document for want of one."
    )
    assert "STOPPING RULE, PRE-COMMITTED" in t
    assert "EXPLICITLY NOT IN SCOPE" in t, (
        "Finishing must be distinguishable from stopping: the σ arm, count 3 and §5's "
        "choose-your-shape are REG-010, and REG-009 closing is not those closing."
    )


def test_reg009s_unpriced_decisions_are_declared_rather_than_assumed():
    """D2/D3/D4 are unpriced. An unpriced decision that does not SAY it is unpriced is
    exactly the adjective-in-a-design-sentence failure REG-009 §1.3 is about."""
    t = _ws(REG009.read_text(encoding="utf-8"))
    assert t.count("DECLARED UNPRICED") >= 3, (
        "D2 (interval->point), D3 (life-band width) and D4 (firm-specific vs industry "
        "median) are each unpriced and each must say so in its own line."
    )
    assert "the probe prices the choice, it does not make it" in t, (
        "§4c's precedent, inherited: P0 reports numbers and REG-009 §2 chooses."
    )


def test_reg009_states_that_3bs_artifact_cannot_answer_the_dispersion_question():
    """The measured correction that saved §1.2's ruling from its own adjective."""
    t = _ws(REG009.read_text(encoding="utf-8"))
    assert "never opens the value column" in t and "count of tag occurrences" in t, (
        "§2 must keep stating that data/source-001-lifetime-by-fyend*.json carries "
        "booleans and a tag count, not life values — otherwise the next session prices "
        "P0 as a groupby on a committed file, which is what this session nearly did."
    )
