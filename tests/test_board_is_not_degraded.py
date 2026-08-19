"""wealthTensor-95 · a degraded board must not be able to reach a commit.

WHY THIS EXISTS. `board.py` takes four flags and requires one. Run it the obvious way and it
silently emits a DEGRADED `docs/CHECKLIST.md`: correct statuses, generic title, and the whole
`docs/checklist-preamble.md` — the board's statement of what the corpus is FOR — deleted.
Nothing goes red, so a session commits it as "a regeneration."

`-53` found this in its first ten minutes and wrote `scripts/regen-board.sh`, whose header
calls itself "the ONLY supported invocation" and correctly names the real defect: *a fact
filed under the tool instead of under the artefact.* `-95` then hit the identical trap
anyway, forty-two sessions later, and deleted the preamble — because a wrapper documents the
right way without PREVENTING the wrong one, and a session that never opens the wrapper never
reads its warning.

So the knowledge moves from a comment into the suite. This is the fix `-53`'s finding
actually needed: not a better note, a check that fails.
"""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOARD = ROOT / "docs" / "CHECKLIST.md"
PREAMBLE = ROOT / "docs" / "checklist-preamble.md"


def _headings(text: str):
    return [l.strip() for l in text.split("\n") if l.startswith("#")]


def test_the_committed_board_carries_the_whole_preamble() -> None:
    board = BOARD.read_text(encoding="utf-8")
    missing = [h for h in _headings(PREAMBLE.read_text(encoding="utf-8")) if h not in board]
    assert not missing, (
        "docs/CHECKLIST.md is missing preamble section(s): " + "; ".join(missing) +
        "\n\nThis is the degraded board. Regenerate with the supported invocation — "
        "`bash scripts/regen-board.sh` — never `board.py` directly.")


def test_the_board_names_the_project() -> None:
    first = BOARD.read_text(encoding="utf-8").split("\n", 1)[0]
    assert "wealth-tensor" in first, (
        f"docs/CHECKLIST.md's title is {first!r} — board.py fell back to a generic title, "
        f"which means --project defaulted. Regenerate with `bash scripts/regen-board.sh`.")
