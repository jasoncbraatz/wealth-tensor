"""Guard tests for patchkit — the force-function added for WT-058.

The property under test is NOT "it edits files". It is "when an anchor misses, the
disk is untouched" — which is the only property that would have prevented the
half-patched tree in wealthTensor-05.
"""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
from patchkit import AnchorError, apply_edits, plan_edits  # noqa: E402


def test_a_missing_anchor_writes_nothing_even_when_earlier_edits_were_valid(tmp_path):
    """This is the WT-058 failure, reproduced. The first edit is fine; the second
    is not. Neither file may change."""
    a = tmp_path / "a.md"
    b = tmp_path / "b.md"
    a.write_text("hello world\n")
    b.write_text("goodbye world\n")

    with pytest.raises(AnchorError):
        apply_edits([
            (a, "hello", "HELLO", "valid edit, must not land"),
            (b, "not present anywhere", "x", "the anchor that misses"),
        ], verbose=False)

    assert a.read_text() == "hello world\n", "an earlier valid edit leaked to disk"
    assert b.read_text() == "goodbye world\n"


def test_an_ambiguous_anchor_is_a_failure_not_a_replace_all(tmp_path):
    """Two occurrences must fail loudly. replace() would silently do both."""
    f = tmp_path / "f.md"
    f.write_text("dup\ndup\n")
    with pytest.raises(AnchorError):
        apply_edits([(f, "dup", "x", "ambiguous")], verbose=False)
    assert f.read_text() == "dup\ndup\n"


def test_edits_to_one_file_compose_in_order(tmp_path):
    """A later edit may legitimately anchor on text an earlier edit created."""
    f = tmp_path / "f.md"
    f.write_text("alpha\n")
    apply_edits([
        (f, "alpha", "beta", "first"),
        (f, "beta", "gamma", "second, anchors on the first's output"),
    ], verbose=False)
    assert f.read_text() == "gamma\n"


def test_plan_edits_is_pure(tmp_path):
    """plan_edits must be safe to call for a dry run."""
    f = tmp_path / "f.md"
    f.write_text("alpha\n")
    planned = plan_edits([(f, "alpha", "beta", "dry run")])
    assert planned[f] == "beta\n"
    assert f.read_text() == "alpha\n", "plan_edits touched the disk"
