"""The SCOPE-001 guard — the steelman stays in §5, and §10's restriction stays intact.

WHY THIS EXISTS
---------------
`RESULT-SCOPE-001.md` records a defect that survived five sessions of grepping: §10
restricts §2's claim to degradation carrying "no impairment trigger, no estimable expected
loss and no observable event to key recognition to", while §5 selects its entire sample on
recognised-impairment tags. Neither sentence is wrong; they had simply never been read in
the same sitting, and nothing in the repository could notice, because BOTH ARE
WELL-FORMED PROSE IN SECTIONS THAT ARE NEVER OPEN AT THE SAME TIME.

The repair is one sentence in §5. A sentence is the least durable artefact this repository
produces: a future reflow of §5.1 deletes it without any test going red, and the paper is
back in the state that took five sessions to find — with the result doc still claiming it
was repaired. That asymmetry is the whole reason for this file.

THE WITNESS PROBLEM, AND HOW IT IS SIDESTEPPED
----------------------------------------------
A source-text guard that RETYPES the sentence it looks for fires on its own witness: the
test and the manuscript drift apart, and the test keeps passing against the copy it
carries. So nothing here is retyped. The steelman is IMPORTED from the edit script that
performed it (`scripts/wt093_edits_scope001.py`), which is the only place its text is
written down, and §10's restriction is located by the two phrases the result doc quotes —
`no observable event` and `predicts nothing` — which the grep already established occur
twice and three times respectively in the whole repository, and once each in paper III.

WHAT IT CANNOT DO
-----------------
It cannot tell whether the steelman is TRUE, and it cannot tell whether §5 still reads
well around it. It pins location and survival, which are the two things a reflow silently
takes away.
"""

import pathlib
import re
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from wt093_edits_scope001 import ANCHOR, NEW  # noqa: E402

PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
RESULT_DOC = ROOT / "docs/preregistration/RESULT-SCOPE-001.md"

#: The steelman alone: the edit's `new` text is the sentence FOLLOWED BY the anchor it was
#: inserted above, so the anchor is stripped rather than re-typed.
STEELMAN = NEW[: NEW.index(ANCHOR)].strip()


@pytest.fixture(scope="module")
def paper() -> str:
    return PAPER.read_text(encoding="utf-8")


def _section(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]



def _flat(s: str) -> str:
    """Whitespace-normalised. These assertions read POST-repair prose only, so flattening
    cannot make a before look like an after -- the failure mode wealthTensor-104 hit in
    wt182. Added at -105, where "\u00a72's domain restriction" fell across a line break and a
    landed repair read as absent."""
    return " ".join(s.split())

def test_the_steelman_is_in_the_manuscript_exactly_once(paper):
    assert paper.count(STEELMAN) == 1, (
        "the SCOPE-001 steelman is missing from paper III or duplicated. It is the whole "
        "repair recorded in RESULT-SCOPE-001.md; if §5.1 was reflowed, re-wrap the "
        "sentence in scripts/wt093_edits_scope001.py and re-run it rather than deleting it."
    )


def test_the_steelman_is_in_section_5_and_not_in_section_10(paper):
    five = _section(paper, "\n## 5 · ", "\n## 6 · ")
    ten = _section(paper, "\n## 10 · ", "\n## 11 · ")
    assert STEELMAN in five, "the steelman must live in §5 — it explains the SAMPLE"
    assert STEELMAN not in ten, (
        "the steelman must NOT be in §10. RESULT-SCOPE-001 §2 registers that §10's "
        "restriction is correct as written and is not touched by this repair."
    )


def test_the_restriction_is_stated_with_the_model_and_is_unweakened(paper):
    """The restriction must SURVIVE, unweakened, and sit where the model is stated.

    It lived in §10 until wealthTensor-105, and this guard pinned it there because that is
    where it was. Pass C ruled the location a C-d fold -- §5.1 pointed at it across 740 lines,
    and it is a statement of §2's domain, not a concession to a rival literature -- and moved
    it into §2. THE SUBJECT OF THIS CHECK WAS NEVER THE SECTION NUMBER: it is that the
    restriction exists, is not softened, and is reachable from the sentence that leans on it.
    Pinning it to §10 made a legitimate move look like a deletion.
    """
    two = _section(paper, "\n## 2 · ", "\n## 3 · ")
    assert "no observable event to key recognition" in _flat(two), (
        "the SCOPE-001 restriction has left §2. It is the half of the pair the steelman leans "
        "on; weakening or deleting it converts a steelman into the scope creep SCOPE-001 refused."
    )
    assert "recognition is faster than the market and this model predicts nothing" in _flat(two)
    ten = _section(paper, "\n## 10 · ", "\n## 11 · ")
    assert "§2's domain restriction" in _flat(ten), (
        "§10 must still NAME the restriction it credits to Basu, or the Basu paragraph is "
        "crediting an object the reader cannot find."
    )


def test_the_steelman_names_the_boundary_rather_than_hedging(paper):
    # The registered repair is positive: it says the sample is the BOUNDARY of the
    # restricted region. A future edit that turns it into a concession ("may not",
    # "cannot be ruled out") has absorbed the objection, which charter §2 forbids and
    # defensive_count.py counts.
    assert "boundary" in STEELMAN
    assert not re.search(r"may not|cannot be ruled out|caveat|arguably", STEELMAN, re.I)


def test_the_result_doc_still_documents_the_pair(paper):
    doc = RESULT_DOC.read_text(encoding="utf-8")
    assert "TIER_TAGS_REG006" in doc
    assert "predicts nothing" in doc
    assert "boundary" in doc
