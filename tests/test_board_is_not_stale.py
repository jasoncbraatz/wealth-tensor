"""wealthTensor-109 · a stale board must not be able to reach a green suite.

WHY THIS EXISTS
---------------
At `-108`, `pytest -q` reported **1174 passed, 0 failed** while two ship-blocking defects sat
in the tree: session tags leaked into a shipped manuscript (`P7`), and the deliverable's
`LAYOUT-MANIFEST.json` claimed a `source_commit` it had not been built from (`P13e`). Neither
is a unit invariant. Both are rows in `docs/done-criteria.tsv` — a ledger the suite did not
read — and both were caught only because a human reached the handoff gate and the gate
demanded the board. The AAR is `claude-blackbook/aars/2026-08-26-green-suite-hid-two-ship-blockers.md`;
this file is its action A1.

The defect is not "someone forgot to regenerate." It is that the project ran **two verifiers
over two ledgers and only one of them ran on `pytest`**, so "green" meant less than every
session believed it meant. This row makes the board part of what green means.

WHAT THIS COSTS, AND WHY IT IS PAID IN FULL
-------------------------------------------
Regenerating measures all 66 criteria, including `P13e`, which materialises a clean worktree
at the manifest's commit and rebuilds the PDF. Measured on an idle darwin at `-109`: **18.7s**
against a 76s suite. There is no opt-in marker and no default skip, because a guard that is
off by default is a guard that reports the machine's configuration rather than the project's
state — which is the same class of defect as the one above, one level up.

WHY IT WRITES TO A TEMPORARY FILE AND NOT TO `docs/CHECKLIST.md`
----------------------------------------------------------------
`--check` alone would answer the question, but a test that regenerates in place would dirty a
tracked file mid-run, and a criterion that inspects the working tree then reads the test's own
output as dirt (banked global lesson, `2026-08-25-status-board-criterion-inspects-working-tree`).
Measuring into `tmp_path` leaves the repository exactly as it was found.

WHY A DIFFERENCE IS CLASSIFIED RATHER THAN JUST REPORTED
--------------------------------------------------------
`board.py` runs every `cmd:` criterion under `BOARD_CHECK_TIMEOUT` and records a timeout as
`CANNOT VERIFY`, so a board measured on a loaded machine differs from a fresh committed board
for a reason that is **not** staleness (`-96` measured exactly this: a 16s criterion under a
25s default came back `CANNOT VERIFY` while a build ran alongside). Both cases are red — a
`CANNOT VERIFY` is an unfinished check, never a pass, which is the one line the AAR asks
everyone to remember — but they need opposite repairs, and telling a session to "regenerate
and commit" a board carrying a `CANNOT VERIFY` would bake a measurement of the machine into
committed state. So this test says which world it is in.

`scripts/regen-board.sh` is the only supported invocation and sets `BOARD_CHECK_TIMEOUT=300`
itself; this file deliberately passes no timeout of its own, so the margin stays in one place
— under the artefact, where `-53` put it.

RED-PROOFED at `-109`: perturbing a criterion's status produces the stale message naming the
flip, and a `BOARD_CHECK_TIMEOUT=1` run produces the measurement message instead. A verifier
nobody broke on purpose is a verifier nobody has tested.
"""

import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOARD = ROOT / "docs" / "CHECKLIST.md"
REGEN = ROOT / "scripts" / "regen-board.sh"

CANNOT = "CANNOT VERIFY"

# `- [x] P13e · <criterion, which may itself contain em-dashes> — **MET** _(check passed)_`
# The `.*` before the status is greedy on purpose: several criteria carry their own " — ",
# and the status is always the LAST such field on the line.
_ROW = re.compile(r"^- \[[ x]\] (\S+) · (.*) — \*\*(.+?)\*\* _\((.*)\)_$")


def _statuses(text: str) -> dict:
    """(lane, criterion) -> status, for every measured criterion in a rendered board."""
    out = {}
    for line in text.split("\n"):
        m = _ROW.match(line)
        if m:
            out[(m.group(1), m.group(2))] = m.group(3)
    return out


def _measure(tmp_path) -> str:
    """Regenerate the board into a scratch file and return it. Never touches the repo."""
    out = tmp_path / "CHECKLIST.measured.md"
    try:
        r = subprocess.run(
            ["bash", str(REGEN), "--out", str(out)],
            capture_output=True, text=True, cwd=str(ROOT), timeout=900,
        )
    except subprocess.TimeoutExpired:
        raise AssertionError(
            "scripts/regen-board.sh did not finish in 900s, so the board was NOT measured. "
            "This is a CANNOT VERIFY, which is an unfinished check and not a pass. Re-run it "
            "by hand on an idle machine — `bash scripts/regen-board.sh --check` — and do not "
            "commit a board generated under that load."
        )
    assert r.returncode == 0, (
        f"scripts/regen-board.sh exits {r.returncode} and produced no board to compare "
        f"against. board.py exits 2 when docs/done-criteria.tsv is missing or parses to zero "
        f"rows — an empty board is a broken parser, not a done project.\n\n"
        f"stdout:\n{r.stdout[-2000:]}\nstderr:\n{r.stderr[-2000:]}"
    )
    assert out.exists(), (
        "scripts/regen-board.sh exited 0 but wrote no file — `--out` is no longer honoured, "
        "so this guard is measuring nothing. Fix the wrapper before trusting a green here."
    )
    return out.read_text(encoding="utf-8")


def test_the_committed_board_is_not_stale(tmp_path) -> None:
    committed = BOARD.read_text(encoding="utf-8")
    measured = _measure(tmp_path)
    if measured == committed:
        return

    was, now = _statuses(committed), _statuses(measured)
    flips = [(k, was[k], now[k]) for k in was.keys() & now.keys() if was[k] != now[k]]
    unverified = [(k, o, n) for k, o, n in flips if n == CANNOT]

    if unverified:
        raise AssertionError(
            "The board could not be MEASURED this run — %d criterion/criteria came back "
            "%s:\n%s\n\nThis is not necessarily a stale board, and the repair is NOT to "
            "regenerate and commit: that would freeze a measurement of this machine into "
            "committed state. Re-run `bash scripts/regen-board.sh --check` on an idle "
            "machine (nothing else building), and raise BOARD_CHECK_TIMEOUT in "
            "scripts/regen-board.sh if a criterion has genuinely grown slower."
            % (len(unverified), CANNOT,
               "\n".join("  %s · %s → %s  (%s)" % (k[0], o, n, k[1][:70]) for k, o, n in unverified))
        )

    added = sorted(now.keys() - was.keys())
    gone = sorted(was.keys() - now.keys())
    detail = []
    if flips:
        detail.append("criteria that changed status:\n" + "\n".join(
            "  %s · %s → %s  (%s)" % (k[0], o, n, k[1][:70]) for k, o, n in sorted(flips)))
    if added:
        detail.append("criteria in done-criteria.tsv but not on the committed board:\n" +
                      "\n".join("  %s · %s" % (l, c[:70]) for l, c in added))
    if gone:
        detail.append("criteria on the committed board but no longer in done-criteria.tsv:\n" +
                      "\n".join("  %s · %s" % (l, c[:70]) for l, c in gone))
    if not detail:
        detail.append(
            "no criterion changed status, so the difference is in the board's prose — the "
            "title, the preamble, or board.py's own rendering. Regenerating will settle it.")

    raise AssertionError(
        "docs/CHECKLIST.md is STALE: it does not describe the tree it was committed with.\n\n"
        + "\n\n".join(detail)
        + "\n\nA criterion can flip on the very commit meant to close it, so regenerate AFTER "
          "the last commit, not before it:\n"
          "    bash scripts/regen-board.sh          # the ONLY supported invocation\n"
          "    git add docs/CHECKLIST.md && git commit\n\n"
          "If a criterion went red, the board's own 'how it was measured' line names the "
          "check that failed — fix the defect, never the criterion."
    )
