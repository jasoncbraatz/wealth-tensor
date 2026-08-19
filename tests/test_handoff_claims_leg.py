"""tests/test_handoff_claims_leg.py

G-CLAIMS -- the leg that RE-RUNS what the handoff's `phase:` block claims -- held to the
guarantees its red-proof structurally cannot give.

THE DIVISION, and it is the same one `wt173 --verify` and
tests/test_recipe_is_held_to_the_measurement.py already have. `scripts/redproof_wt178_claims.py`
provokes every verdict the leg can emit, against handoffs it builds itself; that is a proof
about the LEG. These tests are a proof about THIS REPOSITORY'S handoff: that its registry
parses, that it points at commands that exist, that none of them can mask an exit code, and
that the prose audit passing is a fact rather than a vacuum.

WHY THE LAST ONE IS HERE AT ALL. The audit reports nothing when the registry covers the
prose, and reports nothing when it has found nothing to look at -- and from the outside those
are the same silence. `-95` shipped a coverage check that could not see what it counted and
printed FULL COVERAGE, so a green audit in this repository is not believed until a deletion
has been shown to redden it. That is what test_the_prose_audit_is_not_vacuous does.
"""
import importlib.util
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "wt_handoff_gate_claims", ROOT / "scripts" / "handoff_gate.py")
_GATE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_GATE)

HANDOFF = ROOT / "docs" / "HANDOFF.md"
BLOCK = _GATE.frontmatter_block(str(HANDOFF))
CLAIMS, PARSE_PROBLEMS = _GATE.parse_claims(BLOCK)


def _write(tmp_path, frontmatter):
    p = tmp_path / "HANDOFF.md"
    p.write_text("---\n" + frontmatter.rstrip("\n") + "\n---\n\n# body\n")
    return str(p)


def test_the_registry_parses_without_a_single_refusal():
    assert PARSE_PROBLEMS == []
    assert CLAIMS, "the handoff declares no claims at all"


def test_every_registered_command_names_a_file_that_exists():
    """A registry pointing at a deleted script would fail at RUN time with a shell error and
    an exit code that is not the claimed one -- caught, but as a FALSE-CLAIM against an
    honest predecessor. Catching it here says the true thing instead."""
    missing = []
    for c in CLAIMS:
        for token in c["cmd"].split():
            if token.endswith((".py", ".sh")) and not (ROOT / token).exists():
                missing.append((c["id"], token))
    assert missing == [], "registered commands name files that do not exist: %r" % missing


def test_no_registered_command_can_mask_its_exit_code():
    """The whole reason the leg exists: `$?` after a pipe is the pipe's. A registry that
    could carry `tool --verify | tail -5` would re-import the defect it was built to catch."""
    for c in CLAIMS:
        for bad, _human in _GATE.CLAIM_FORBIDDEN:
            assert bad not in c["cmd"], "%s: %r contains %r" % (c["id"], c["cmd"], bad)


def test_every_claim_that_asserts_a_count_can_observe_it():
    for c in CLAIMS:
        if c.get("count") is not None:
            assert c["_rx"] is not None, "%s asserts a count with no usable count_re" % c["id"]
            assert c["_rx"].groups == 1


def test_the_prose_audit_passes_on_the_committed_handoff():
    assert _GATE.claims_static(str(HANDOFF)) == []


def test_the_prose_audit_is_not_vacuous(tmp_path):
    """Delete one declaration and the audit must NAME the assertion left undeclared. A green
    audit that cannot be reddened is not a green audit, it is an audit that never ran."""
    victim = CLAIMS[0]["id"]
    src = HANDOFF.read_text()
    mutated = re.sub(r"\n  - id: %s\n(?:    .*\n)+" % re.escape(victim), "\n", src, count=1)
    assert mutated != src, "the mutation did not apply -- the test proves nothing"
    p = tmp_path / "HANDOFF.md"
    p.write_text(mutated)
    problems = _GATE.claims_static(str(p))
    assert any(x.startswith("UNREGISTERED-CLAIM") for x in problems), \
        "removing the %r claim reddened nothing: %r" % (victim, problems)


def test_a_slow_claim_that_was_not_run_is_not_reported_as_verified(tmp_path):
    """An un-run claim is an unverifiable claim, and this file's oldest doctrine is that an
    unverifiable claim must never be reported as a verified one. Exit 2, never 0."""
    fm = ('phase: "`slowthing` RC 0"\n'
          "claims:\n  - id: slowthing\n    cmd: true\n    rc: 0\n    slow: true\n")
    assert _GATE.claims_leg(run_slow=False, path=_write(tmp_path, fm)) == 2
    assert _GATE.claims_leg(run_slow=True, path=_write(tmp_path, fm)) == 0


def test_a_flake_is_never_reported_as_a_false_claim(tmp_path, capsys):
    """`-95` watched an honest check go red once and never again. A gate that called that a
    lie would be switched off within the week, so the mixed verdict is FLAKY and exit 2."""
    counter = tmp_path / "counter.sh"
    counter.write_text("f=%s/n\nn=$(cat $f 2>/dev/null || echo 0)\nn=$((n+1))\n"
                       "echo $n > $f\ntest $n -ge 2\n" % tmp_path)
    fm = ('phase: "`counter` RC 0"\n'
          "claims:\n  - id: counter\n    cmd: bash %s\n    rc: 0\n" % counter)
    assert _GATE.claims_leg(path=_write(tmp_path, fm)) == 2
    out = capsys.readouterr().out
    assert "FLAKY" in out and "FALSE-CLAIM" not in out


def test_a_claim_false_on_every_attempt_is_a_blocker(tmp_path):
    """The control for the test above. A check that stopped refusing is not an improvement,
    it is a removal, and only this case can tell those two apart."""
    fm = ('phase: "`nope` RC 0"\n'
          "claims:\n  - id: nope\n    cmd: false\n    rc: 0\n")
    assert _GATE.claims_leg(path=_write(tmp_path, fm)) == 1


@pytest.mark.parametrize("tag", sorted(_GATE.CLAIM_TAGS))
def test_every_declared_tag_is_emitted_through_the_registry_check(tag):
    assert _GATE._tag(tag, "x").startswith(tag + ":")


def test_an_undeclared_tag_cannot_be_emitted_silently():
    assert _GATE._tag("NOT-A-TAG", "x").startswith("UNREGISTERED-TAG")
