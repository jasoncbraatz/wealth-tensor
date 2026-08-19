"""tests/test_handoff_gate_placeholders.py

The handoff gate's placeholder check, held to the distinction it exists to make.

WHY THIS FILE EXISTS. `--emit` refuses a handoff that still carries TODO / TBD / FIXME /
XXX, which is right. It did so with a substring test, which cannot tell a marker LEFT IN
the document from a marker the document NAMES -- and wealth-tensor's own handoff names all
four, in a drift flag whose subject is precisely that "a negative grep cannot tell USE from
MENTION". So the gate refused a correct handoff, at the last act of the wrap, and the cheap
way out was to delete the sentence. Deleting documentation to satisfy a checker is how a
repository forgets things; the checker was fixed instead (wealthTensor-94).

The negative controls are the point. A check that stopped refusing is not an improvement,
it is a removal, and only the POSITIVE cases below can tell those two apart.
"""
import importlib.util
import pathlib

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "wt_handoff_gate",
    pathlib.Path(__file__).resolve().parents[1] / "scripts" / "handoff_gate.py")
_GATE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_GATE)
left = _GATE.placeholders_left


# ---------------------------------------------------------------- POSITIVE: must still bite
@pytest.mark.parametrize("body", [
    "next at bat: TODO",
    "the schedule is TBD",
    "FIXME before shipping",
    "signature: XXX",
    "author: <fill in>",
    "a line of ordinary prose\nand then TODO write the rest\nand more prose",
])
def test_a_real_leftover_is_still_refused(body):
    assert left(body), "a genuine placeholder must still be caught: %r" % body


def test_every_marker_is_reported_by_name():
    problems = left("TODO and TBD and FIXME and XXX and <fill")
    assert len(problems) == 5, problems


# ---------------------------------------------------------------- NEGATIVE: must not bite
def test_the_marker_set_recited_as_itself_is_a_mention():
    """The exact sentence that made the gate refuse a correct handoff."""
    body = ("  classes with no legitimate use (TODO/TBD/FIXME/XXX) and leave wording "
            "prohibitions to prose.")
    assert left(body) == []


def test_a_marker_in_a_code_span_is_a_mention():
    assert left("the gate refuses a bare `TODO` in the body") == []


def test_the_drift_flag_that_documents_the_distinction_is_not_an_offence():
    body = ("A negative grep cannot tell USE from MENTION, which is also why the P13b "
            "criterion bans placeholder markers (TODO/TBD/FIXME/XXX) and leaves the "
            "wording prohibition to the prose.")
    assert left(body) == []


def test_clean_prose_is_clean():
    assert left("nothing to see here; the handoff is complete.") == []


# ------------------------------------------------- the exemptions are NARROW, and stay narrow
def test_a_recital_does_not_launder_a_separate_real_leftover():
    """The dangerous failure mode: an exemption that covers the rest of the line."""
    body = "we ban (TODO/TBD/FIXME/XXX) here, and also FIXME this function"
    assert left(body), "a real leftover beside a recital must still be caught"


def test_a_code_span_does_not_launder_a_separate_real_leftover():
    body = "the gate refuses `TODO` in the body -- TBD whether it should"
    assert left(body), "a real leftover beside a code span must still be caught"


def test_a_lone_marker_is_not_a_recital():
    """A recital needs TWO OR MORE markers joined by slashes; one is just a marker."""
    assert left("TODO/write-this-up") != []
