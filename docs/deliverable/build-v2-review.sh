#!/usr/bin/env bash
# docs/deliverable/build-v2-review.sh
# =========================================================================================
# wealthTensor-110 · typeset the V2 REVIEW PAIR, and nothing else.
#
# The v2 pair is paper II and paper III at their v1 cut -- the version whose arguments the
# author kept -- run through scripts/wt224_voice_pass.py and given the nine figures. It is a
# READING COPY, not the capture: docs/deliverable/wealth-tensor-capture.pdf and the
# LAYOUT-MANIFEST.json that is a per-page statement about it belong to the canonical four
# manuscripts in docs/papers/, and this script is written so that it cannot touch either.
#
# The four env vars below are the whole of the isolation, and each one guards a file that a
# naive `./build.sh` over a different manuscript set WOULD have overwritten:
#
#   WT_PAPERS_ROOT  docs/papers-v2, not docs/papers
#   WT_CAPTURE      its own PDF, so wealth-tensor-capture.pdf is untouched (P13e stays true)
#   WT_TABLE_WIDTHS its own measures, because --retune WRITES that file and the v2 pair has
#                   different tables -- retuning into the committed one would re-measure the
#                   canonical capture against a document it is not a statement about
#   WT_DOCLABEL     its own page footer, because a review build is otherwise byte-for-byte
#                   plausible as the capture and nothing else would tell a reader apart
#
# --no-manifest is passed unconditionally and is not an option: LAYOUT-MANIFEST.json is P13e's.
#
#   ./build-v2-review.sh              build (regenerates the manuscripts first)
#   ./build-v2-review.sh --retune     ...and re-derive the v2 table measures from the engine
# =========================================================================================
set -uo pipefail
cd "$(dirname "$0")"
HERE="$(pwd)"
REPO="$(cd ../.. && pwd)"

OUT="${WT_V2_OUT:-$HERE/build-v2}"
PDF="$HERE/wealth-tensor-v2-review.pdf"

echo "== regenerate the v2 manuscripts (voice pass + figure embeds)"
python3 "$REPO/scripts/wt225_build_v2.py" || exit 1

echo
echo "== typeset"
WT_PAPERS_ROOT="docs/papers-v2" \
WT_PAPERS="paper-II-redistribution/paper-II.md
paper-III-dual-tensor/paper-III.md" \
WT_OUT="$OUT" \
WT_CAPTURE="$PDF" \
WT_TABLE_WIDTHS="$HERE/TABLE-WIDTHS-v2.tsv" \
WT_DOCLABEL="wealth-tensor v2 review — not the capture" \
  ./build.sh --no-manifest "$@" || exit 1

# THE ONE THING THAT WOULD MAKE THIS SCRIPT A LIE. Everything above is arranged so the
# canonical artefacts are not written; this checks that they were not, rather than trusting
# that they were not.
echo
echo "== the canonical artefacts are untouched"
FAIL=0
for f in wealth-tensor-capture.pdf LAYOUT-MANIFEST.json TABLE-WIDTHS.tsv; do
  if [ -n "$(git -C "$REPO" status --porcelain -- "docs/deliverable/$f")" ]; then
    echo "  FAIL   docs/deliverable/$f was modified by a review build"; FAIL=1
  else
    echo "  ok     docs/deliverable/$f"
  fi
done
[ "$FAIL" -eq 0 ] || { echo; echo "REFUSED — a review build wrote a canonical artefact."; exit 1; }
echo
echo "V2 REVIEW OK — $PDF"
