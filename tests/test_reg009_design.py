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

    The SHAPE of that second job was bought over two failures and is the interesting part.
    v1 pinned a corpus TOTAL and failed instantly: this file names every needle in its own
    parametrisation, and §1.5's repair RESTATES the three bounds while flagging them
    unanswered — to a raw count, a repair that propagates a finding and a restatement that
    ignores it are identical. v2 pinned per-file counts and failed again the moment
    HANDOFF.md reported the finding. THE SECOND FAILURE WAS THE SIGNAL: a guard whose only
    maintenance is appending to an exclusion list is on its way to being ignored, which is
    the doctrine's permanently-red check arriving in a new costume.

    v3 holds the two things that are actually invariant. (a) THE ANCHOR: each bound occurs
    exactly once in paper III, in §4.7's declaring sentence — if that moves, the finding is
    about a sentence that no longer exists. (b) THE MEASUREMENT HOMES: no bound appears in
    `scripts/`, `data/` or a `RESULT-*`, because that is where a measurement would land and
    nowhere else. Design docs are not counted at all — they are supposed to discuss this.
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

# The three bounds §4.7 offers against its own weak joint, plus §1.5's tell.
BOUNDS = {
    "sticky": "bound 2 (lives are sticky within a firm) — REG-009 §2's P0-a measures this",
    "industry-median": "bound 3 (the design can run on industry medians) — P0-b measures this",
    "industry convention": "bound 1 (lives are anchored by industry convention) — P0-b",
}

# WHERE A MEASUREMENT WOULD LAND. This is the invariant that carries the finding; the
# directories are the point, not the counts.
MEASUREMENT_HOMES = ("scripts/", "data/")


def _is_measurement_home(path: str) -> bool:
    return path.startswith(MEASUREMENT_HOMES) or "/RESULT-" in path


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

@pytest.mark.parametrize("needle", sorted(BOUNDS))
def test_the_declaring_sentence_in_paper_iii_is_still_the_only_one_there(needle):
    """The ANCHOR of §1.3's finding: each bound appears once in paper III, in §4.7's
    sentence. If that changes, the manuscript changed and §1.3 must be re-decided.

    Deliberately NOT a corpus total. An earlier version of this test pinned every file's
    count and fired twice on legitimate propagation — first on §1.5's repair, then on
    HANDOFF.md reporting the finding. A guard whose only maintenance is appending to an
    exclusion list is a guard on its way to being ignored (doctrine: the permanently-red
    check). What is worth holding is the anchor and the measurement homes, below.
    """
    n = _by_file(needle).get(P3, 0)
    assert n == 1, (
        f"'{needle}' occurs {n} times in paper III (expected 1, §4.7's declaring "
        f"sentence). This is {bound_desc(needle)}.\n"
        f"If §4.7 was rewritten, REG-009 §1.3's finding is about a sentence that no "
        f"longer exists — re-decide it rather than re-pinning this number."
    )


def bound_desc(needle: str) -> str:
    return BOUNDS[needle]


# --------------------------------------------------------------------------- v4
# THE DISCHARGE LEDGER, wealthTensor-28.
#
# v3 asserted that no bound had reached a measurement home, because at `-27` none had.
# `-28` ran REG-009 §2's P0 and all three bounds were measured, so v3 went red -- on the
# very event it was built to detect. Its own failure message said what to do: "If that is
# a MEASUREMENT: good ... move the bound into the discharged column and relax this test by
# name."
#
# The relaxation is NOT an exclusion. An exclusion says "stop looking here"; a LEDGER says
# "this one was answered, HERE, and if that answer disappears the finding reopens." The
# difference is the whole of `-27`'s lesson about guards whose only maintenance is
# appending exclusions: v4 has strictly MORE to fail on than v3, not less.
#
# A bound is discharged only against a named artifact. Undischarged bounds keep v3's rule
# unchanged, so the guard still works the moment §4.7 grows a fourth bound.
DISCHARGED = {
    "sticky": ("P0-a", "docs/preregistration/RESULT-P0.md"),
    "industry convention": ("P0-b", "docs/preregistration/RESULT-P0.md"),
    "industry-median": ("P0-b", "docs/preregistration/RESULT-P0.md"),
}


@pytest.mark.parametrize("needle", sorted(BOUNDS))
def test_every_bound_is_either_undischarged_and_absent_or_discharged_and_cited(needle):
    """THE INVARIANT THAT CARRIES THE FINDING, v4.

    UNDISCHARGED: must not appear in `scripts/`, `data/` or a `RESULT-*`, because that is
    where a measurement lands and nowhere else -- v3's rule, unchanged.

    DISCHARGED: the named result document must exist AND must say which part of P0
    measured it. A bound cannot be marked answered by a dictionary entry alone; §1.3's
    finding was that assertions had been mistaken for measurements, and a ledger that
    accepted its own say-so would be the fifth costume of exactly that.
    """
    if needle not in DISCHARGED:
        offenders = {p: n for p, n in _by_file(needle).items() if _is_measurement_home(p)}
        assert not offenders, (
            f"'{needle}' now appears in an instrument or a result: {offenders}. This is "
            f"{BOUNDS[needle]}.\n"
            "If that is a MEASUREMENT: good — it is the work REG-009 §1.3 asked for. "
            "Add it to DISCHARGED with the artifact that measured it.\n"
            "If it is a mention in passing, rename the variable — this directory is "
            "reserved for the thing that discharges the finding."
        )
        return

    part, doc = DISCHARGED[needle]
    path = ROOT / doc
    assert path.exists(), (
        f"'{needle}' is marked discharged by {part} in {doc}, and {doc} does not exist. "
        "A discharge ledger that outlives its own evidence is worse than no ledger: it "
        "reports an objection as answered by a document nobody can read."
    )
    t = _ws(path.read_text(encoding="utf-8"))
    assert part in t, (
        f"{doc} exists but never mentions {part}, which is what the ledger says "
        f"measured '{needle}'. Point the ledger at the part that did the work, or "
        "un-discharge the bound."
    )


@pytest.mark.parametrize("needle", sorted(DISCHARGED))
def test_a_discharged_bound_carries_a_number_and_not_another_assertion(needle):
    """The bound is answered by a MEASUREMENT or it is not answered. §1.3's whole finding
    is that three assertions and a sign were mistaken for the answering of an objection;
    a result document that discharges them with a fourth assertion repeats it."""
    part, doc = DISCHARGED[needle]
    t = (ROOT / doc).read_text(encoding="utf-8")
    block = [ln for ln in t.splitlines() if part in ln]
    assert block, f"{doc} names no line carrying {part}"
    assert re.search(r"\d+\.\d+", " ".join(block)), (
        f"the {part} lines in {doc} carry no number. '{needle}' is bound 1/2/3 of "
        f"§4.7's weak joint, and it is discharged by a measurement or not at all."
    )


def test_closely_enough_has_not_multiplied_in_the_manuscript():
    """§1.5's tell, held where it matters. The phrase was the thread that unpicked the
    §4.8/§4.7 misattribution; a NEW one in the manuscript is a new unmeasured quantifier
    in a place that licenses runs."""
    n = _by_file("closely enough").get(P3, 0)
    assert n == 0, (
        f"'closely enough' now occurs {n} times in paper III. It was the single "
        "unmeasured quantifier behind §1.5's misattribution; run the §1.3 grep on the "
        "new one before believing the sentence it sits in."
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
