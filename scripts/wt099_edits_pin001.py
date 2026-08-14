"""PIN-001 · §11's code-state pin, replaced by per-file pins that cannot rot.

Registered first in `docs/preregistration/RESULT-PIN-001.md` §2, committed alone at
`214ff57` before this script existed on disk. The find: §11 tells a replicator that
`d655501` is "the last commit touching `src/`" and "is verifiable now", and it is not —
four commits have touched `src/` since, one of them (`93a159b`) adding twenty-one lines
to `edgar.py`, a module §11's own **Modules** bullet names. The same section says the
head of the repository carries 103 tests; it carries 777.

The repair is a STEELMAN. A global SHA is the wrong instrument for a per-file
guarantee: it fails the moment any module changes for any reason, including reasons that
leave this paper's results untouched. The per-file pins are strictly stronger, they
survive every commit that does not touch a pinned file, and they let §11 DISCLOSE the
REG-006 correction instead of leaving it hidden behind a stale global pin.

Five anchors, every one a span with NO internal newline (patchkit's rule of thumb). No
heading and no horizontal rule is added or removed, so the structure delta is declared
empty. Both edits stay inside §11.

THE SHAs ARE WRITTEN DOWN HERE AND NOWHERE ELSE. `tests/test_pin001_code_state.py`
imports them rather than retyping them, so the guard cannot drift from its own witness —
the same move `-32` and `-33` used to keep a source-text guard from firing on its own
copy of the subject.
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

PAPER = (
    pathlib.Path(__file__).resolve().parents[1]
    / "docs/papers/paper-III-dual-tensor/paper-III.md"
)

#: The per-file pins §11 publishes: the commit whose content produced this paper's
#: results, per file. `lag.py` and `lambda_sensitivity.py` have one commit each and have
#: never moved; `edgar.py` was pinned at `d655501` and has moved once since, at
#: `LATEST_TOUCH` below, in a way the manuscript now discloses.
PINS: dict[str, str] = {
    "src/wealth_tensor/edgar.py": "d655501",
    "src/wealth_tensor/lag.py": "ad779eb",
    "src/wealth_tensor/lambda_sensitivity.py": "b9089c7",
}

#: The commit that most recently touched each pinned path, as of this edit. THIS is what
#: the guard checks, and it is what makes the defect impossible to reintroduce silently:
#: the next commit touching a pinned file makes the guard red, so the pin and the paper
#: move together or the suite says so.
LATEST_TOUCH: dict[str, str] = {
    "src/wealth_tensor/edgar.py": "93a159b",
    "src/wealth_tensor/lag.py": "ad779eb",
    "src/wealth_tensor/lambda_sensitivity.py": "b9089c7",
}

#: sha256 of the `TIER_TAGS` block — from `TIER_TAGS: ` through its closing brace — which
#: is byte-identical at `d655501` and at the head of the repository. This is the SUBSTANCE
#: of §11's disclosure about `93a159b`: the commit APPENDS `TIER_TAGS_REG006` beside the
#: registered list without editing it, so the tags that selected §5's published sample are
#: unchanged. A SHA equality proves the commit; this proves the claim about the commit.
TIER_TAGS_BLOCK_SHA256 = (
    "e7fce6a9aae7b94ecf8b7a346be50a8f06c7095a97b6e0e5fc885a2f233b0827"
)

#: The two phrases the repair removes. Named here so the guard can assert their absence
#: without retyping them either.
ROTTED = (
    "last commit touching",
    "The head of the repository carries 103.",
)

# --------------------------------------------------------------------------------------
# EDIT 1 · the test-suite bullet — a live count replaced by a statement that stays true
# --------------------------------------------------------------------------------------

A1_OLD = (
    "  is the state that produced every result in §A.2 and §2. "
    "The head of the repository carries 103."
)
A1_NEW = (
    "  is the state that produced every result in §A.2 and §2. "
    "The suite at the head of the repository"
)

A2_OLD = (
    "  The three later additions guard claims this paper makes and change no model code: "
    "two for §3.1's"
)
A2_NEW = (
    "  is larger and grows with every registration in `docs/preregistration/`; three of its additions\n"
    "  guard claims this paper makes and change no model code: two for §3.1's"
)

# --------------------------------------------------------------------------------------
# EDIT 2 · the code-state bullet — one global SHA replaced by three per-file pins
# --------------------------------------------------------------------------------------

B1_OLD = (
    "- **Code state for the results reported here:** commit **d655501** "
    "(last commit touching `src/`)."
)
B1_NEW = (
    "- **Code state for the results reported here:** the per-file pins —\n"
    "  `src/wealth_tensor/edgar.py` at commit **d655501**, `src/wealth_tensor/lag.py` at **ad779eb**\n"
    "  (its only commit) and `src/wealth_tensor/lambda_sensitivity.py` at **b9089c7** — each\n"
    "  verifiable with `git log -1 --format=%h <sha> -- <path>`. `src/` as a whole has moved since,\n"
    "  on companion-paper modules and, at **93a159b**, on one addition to `edgar.py` that appends\n"
    "  the REG-006-corrected tier-0 tag list beside the registered one without editing it: the\n"
    "  `TIER_TAGS` block that selected §5's published sample is byte-identical at **d655501** and at\n"
    "  the head of the repository."
)

B2_OLD = (
    "  A submission-time head-of-repository SHA will be pinned when this paper is posted; "
    "**d655501** is"
)
B2_NEW = (
    "  A submission-time head-of-repository SHA will be pinned when this paper is posted; "
    "the per-file"
)

B3_OLD = "  the SHA a replicator needs and is verifiable now."
B3_NEW = "  pins are what a replicator needs and are verifiable now."


def main() -> int:
    apply_edits(
        [
            (PAPER, A1_OLD, A1_NEW, "§11 · the head-of-repository test count stops being a number"),
            (PAPER, A2_OLD, A2_NEW, "§11 · the three named additions keep their description"),
            (PAPER, B1_OLD, B1_NEW, "§11 · per-file pins replace the global one, REG-006 disclosed"),
            (PAPER, B2_OLD, B2_NEW, "§11 · the deferred submission SHA now defers to the per-file pins"),
            (PAPER, B3_OLD, B3_NEW, "§11 · what a replicator needs, in the plural"),
        ],
        expect_structure={},
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
