#!/usr/bin/env bash
# Regenerate docs/CHECKLIST.md — the ONLY supported invocation.
#
# WHY THIS FILE EXISTS (wealthTensor-53, found in the first ten minutes of the session).
# `board.py` takes four flags and only one of them is required. Run it the obvious way —
#     python3 ~/Scripts/handoff-kit/board.py --criteria docs/done-criteria.tsv
# — and it silently produces a DEGRADED board: the title becomes "# project — SESSION
# CHECKLIST" and the whole "## The destination (ADR-001, restated once)" preamble is
# dropped, because --project and --preamble defaulted. The statuses are still correct, so
# nothing goes red; a session that committed it would have deleted the board's statement of
# what the corpus is for and called it a regeneration.
#
# The flags were recorded nowhere runnable. They are recorded here now.
# Reversible by construction: it writes one generated file that git can restore.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 "${HOME}/Scripts/handoff-kit/board.py" \
    --criteria docs/done-criteria.tsv \
    --project wealth-tensor \
    --preamble docs/checklist-preamble.md \
    "$@"
