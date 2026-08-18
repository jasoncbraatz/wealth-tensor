"""wealthTensor-82 · the manuscript sweeps are bound to the suite, not to the handoff.

WHY THIS EXISTS
---------------
`wt133_crossref_sweep.py` has been committed since `-73` and has never had a test. Its exit
code is load-bearing and every handoff since has carried a line of ritual — *"run
wt133_crossref_sweep.py AND SAY ITS RC"* — which is a procedure living in a document, which
is the thing `WT-116` was banked to stop: *"a procedure that lives in a ledger entry is a
procedure the next session re-derives."* A sweep whose only trigger is a sentence in a
handoff is one forgetful session away from silence, and it went eight sessions before anyone
noticed it had no guard.

`wt148_promise_sweep.py` would inherit the same fate on the day it was written, so both are
bound here at once.

Both sweeps are pure-document — no network, no `src/` import, no data pull — and together
they run in well under a second over roughly 4 800 lines of manuscript, which is why they can
sit in the suite rather than in a session's memory.

WHAT A FAILURE HERE MEANS. Not "a script broke." It means a manuscript now carries a
cross-reference that resolves to nothing, or a sentence promising something about a named
artefact that nobody has checked. The fix is to adjudicate or repair, never to loosen the
assertion.
"""

import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

SWEEPS = [
    pytest.param("wt133_crossref_sweep.py", id="crossref"),
    pytest.param("wt148_promise_sweep.py", id="promise"),
]


def _run(script: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script)],
        capture_output=True, text=True, cwd=str(ROOT),
    )


@pytest.mark.parametrize("script", SWEEPS)
def test_the_sweep_exits_zero(script: str) -> None:
    r = _run(script)
    assert r.returncode == 0, (
        f"scripts/{script} exits {r.returncode}. Its output says which manuscript and which "
        f"line; adjudicate or repair it, and do not relax this assertion.\n\n{r.stdout[-4000:]}"
    )


def test_every_in_scope_manuscript_is_fully_adjudicated() -> None:
    """The promise sweep's green must mean 'checked', not 'nothing in scope'."""
    r = _run("wt148_promise_sweep.py")
    assert "declares no #scope line" not in r.stdout, (
        "docs/promises-adjudicated.tsv lost its #scope line — the sweep gates nothing and its "
        "exit code is decoration."
    )
    in_scope = [ln for ln in r.stdout.split("\n") if "[IN SCOPE]" in ln]
    assert len(in_scope) >= 2, f"fewer than two manuscripts are gated: {in_scope}"


def test_the_adjudication_file_is_readable_and_every_row_is_complete() -> None:
    """A row missing its evidence column is a tick with nothing behind it."""
    tsv = ROOT / "docs/promises-adjudicated.tsv"
    rows = [ln for ln in tsv.read_text(encoding="utf-8").split("\n")
            if ln.strip() and not ln.lstrip().startswith("#")]
    assert rows, "docs/promises-adjudicated.tsv has no rows"
    for ln in rows:
        f = ln.split("\t")
        assert len(f) == 7, f"row has {len(f)} fields, expected 7: {ln[:90]}"
        assert f[3] in {"H", "N", "R", "C"}, f"unknown class {f[3]!r}: {ln[:90]}"
        assert f[4].strip(), f"row has an empty evidence column: {ln[:90]}"
        assert f[5].strip(), f"row has an empty note column: {ln[:90]}"
