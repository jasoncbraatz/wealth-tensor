"""patchkit's structure guard — the -15 trap, mechanised.

An anchor whose `old` spans a heading or a horizontal rule must re-emit it in `new`.
Nothing about failing to is ambiguous, so validate-then-write cannot catch it: every
anchor resolves exactly once and the patch reports success while a section quietly
vanishes into the one above it. These pin the guard that now refuses that write.
"""

import pathlib

import pytest

from patchkit import (AnchorError, StructureError, apply_edits, check_structure,
                      structure)

DOC = """# Title

intro

## 5 · The severe test

body of five

---

## 6 · What may now be claimed

body of six

### 6.1 · The demotion

detail
"""


def _write(tmp_path) -> pathlib.Path:
    p = tmp_path / "paper.md"
    p.write_text(DOC)
    return p


def test_structure_reads_headings_by_level_and_counts_rules():
    sig = structure(DOC)
    assert sig["#"] == ["# Title"]
    assert sig["##"] == ["## 5 · The severe test", "## 6 · What may now be claimed"]
    assert sig["###"] == ["### 6.1 · The demotion"]
    assert sig["---"] == 1


def test_the_minus_15_trap_is_refused_and_nothing_is_written(tmp_path):
    """The anchor spans `---` and `## 6`; the replacement forgets to put them back."""
    p = _write(tmp_path)
    old = "body of five\n\n---\n\n## 6 · What may now be claimed"
    new = "body of five\n\n### 5.4 · A new subsection\n\nnew body"
    with pytest.raises(StructureError) as exc:
        apply_edits([(p, old, new, "insert 5.4")])
    assert "LOST" in str(exc.value)
    assert "## 6 · What may now be claimed" in str(exc.value)
    assert p.read_text() == DOC          # all-or-nothing still holds


def test_the_same_edit_passes_when_the_delimiter_is_re_emitted(tmp_path):
    p = _write(tmp_path)
    old = "body of five\n\n---\n\n## 6 · What may now be claimed"
    new = ("body of five\n\n### 5.4 · A new subsection\n\nnew body"
           "\n\n---\n\n## 6 · What may now be claimed")
    apply_edits([(p, old, new, "insert 5.4")], verbose=False,
                expect_structure={"###": +1})
    txt = p.read_text()
    assert "## 6 · What may now be claimed" in txt
    assert "### 5.4 · A new subsection" in txt


def test_an_undeclared_addition_is_refused_even_though_it_loses_nothing(tmp_path):
    """Silence is not consent in either direction: gains are declared too."""
    p = _write(tmp_path)
    with pytest.raises(StructureError) as exc:
        apply_edits([(p, "detail\n", "detail\n\n### 6.2 · Another\n\nmore\n")])
    assert "GAINED" in str(exc.value)
    assert p.read_text() == DOC


def test_a_body_only_edit_needs_no_declaration(tmp_path):
    p = _write(tmp_path)
    apply_edits([(p, "body of six", "body of six, revised")], verbose=False)
    assert "body of six, revised" in p.read_text()


def test_a_dropped_horizontal_rule_is_caught_on_its_own(tmp_path):
    p = _write(tmp_path)
    with pytest.raises(StructureError) as exc:
        apply_edits([(p, "\n---\n", "\n")])
    assert "---" in str(exc.value)
    assert p.read_text() == DOC


def test_structure_error_is_an_anchor_error_so_existing_handlers_still_catch_it():
    assert issubclass(StructureError, AnchorError)


def test_check_structure_is_usable_without_files():
    check_structure("## a\n", "## a\nbody\n")
    with pytest.raises(StructureError):
        check_structure("## a\n", "")
