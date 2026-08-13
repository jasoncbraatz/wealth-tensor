"""The guard for a gate that was not running: `docs/HANDOFF.md` must carry its anchors.

WHY THIS EXISTS
---------------
`scripts/handoff_gate.py --emit` refuses to bless a handoff that does not (a) tell the next
session to read `docs/CO-AUTHOR-CHARTER.md` at ORIENT and (b) carry the precedence clause
`THE CHARTER WINS`. Without the second one, a plausible rewrite in a handoff silently
becomes law -- the handoff is a status report and the charter is the constitution, and a
session that reads only the former cannot tell which it is holding.

`wealthTensor-21` ran `--emit`, was refused on both anchors, and then checked backwards:

    ZERO of the last EIGHT handoffs carried either anchor.

Every one of them nonetheless shipped with `gate_passed: true` in its frontmatter -- a
field the AUTHOR writes by hand. So for eight sessions the recorded state was "gate
passed" and the gate that would have said otherwise either refused unseen or was never
run. **The frontmatter boolean is a CLAIM; `--emit` is the EVIDENCE**, and this project
has a gate check (`G-AH`, "a log line is not evidence") for exactly that confusion in
shell scripts while the handoff was making it in markdown.

`--emit` is the right gate and it works. What it lacked was anything that ran it. The
suite runs every session; these two assertions do not depend on anyone remembering.

Deliberately NOT checked here: staleness (`gh_sha` vs HEAD), a dirty tree, TODO
placeholders. Those are `--emit`'s job and they need git. This file guards only the part
that is a property of the text, so it stays offline like every test here.
"""

from __future__ import annotations

import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
HANDOFF = ROOT / "docs" / "HANDOFF.md"
CHARTER = ROOT / "docs" / "CO-AUTHOR-CHARTER.md"

# Kept byte-identical to handoff_gate.ANCHOR_READ / ANCHOR_PRECEDENCE on purpose: if that
# script's constants move, test_the_anchor_strings_match_the_gate below goes red rather
# than this file quietly guarding a string nothing else uses.
ANCHOR_READ = "docs/CO-AUTHOR-CHARTER.md"
ANCHOR_PRECEDENCE = "THE CHARTER WINS"


@pytest.fixture(scope="module")
def handoff() -> str:
    return HANDOFF.read_text(encoding="utf-8")


def test_the_charter_exists():
    """A handoff cannot cite what is not there."""
    assert CHARTER.exists(), f"{CHARTER} is missing -- the charter is the SSOT."


def test_handoff_sends_the_next_session_to_the_charter(handoff):
    assert ANCHOR_READ in handoff, (
        f"docs/HANDOFF.md does not point the next session at {ANCHOR_READ} at ORIENT. "
        f"handoff_gate.py --emit refuses on this (G-ANCHOR-1); eight consecutive handoffs "
        f"shipped without it while recording gate_passed: true."
    )


def test_handoff_carries_the_precedence_clause(handoff):
    assert ANCHOR_PRECEDENCE in handoff, (
        f"docs/HANDOFF.md carries no {ANCHOR_PRECEDENCE!r} clause (G-ANCHOR-2). Without it "
        f"a rewrite in a handoff silently becomes law: the next session cannot tell a "
        f"status report from the constitution."
    )


def test_the_anchor_strings_match_the_gate():
    """A copy of the logic under test rots while the original moves. Read the real one.

    Same failure mode `claude-blackbook` records for drills that carry their own copy of
    the thing they check: extract from the source at run time and fail loudly if the
    extraction stops matching.
    """
    gate = (ROOT / "scripts" / "handoff_gate.py").read_text(encoding="utf-8")
    for name, value in (("ANCHOR_READ", ANCHOR_READ),
                        ("ANCHOR_PRECEDENCE", ANCHOR_PRECEDENCE)):
        assert f'{name} = "{value}"' in gate, (
            f"handoff_gate.py no longer defines {name} = {value!r}. This file is guarding "
            f"a string the gate has moved on from -- re-read the gate and update both."
        )
