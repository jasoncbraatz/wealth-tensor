#!/usr/bin/env bash
# docs/deliverable/verify-layout.sh
# =========================================================================================
# P13e · THE LAYOUT IS REPRODUCIBLE, PROVED NOT PROMISED.
#
# Rebuilds the capture FROM A CLEAN CHECKOUT of the commit LAYOUT-MANIFEST.json names, and
# holds the fresh PDF to the committed page count and the committed per-page text hash.
#
# WHY A WORKTREE AND NOT THE WORKING TREE. Rebuilding in place proves almost nothing: the
# build directory still holds the previous run's .aux, the working tree may carry edits the
# capture never saw, and a stale font left in ./fonts/ would be reused rather than restored.
# `git worktree add --detach <source_commit>` is a genuinely clean materialisation of the
# exact tree the capture was built from -- which is what "reproducible" has to mean, or the
# row is satisfied by a build that merely did not change.
#
# A rebuild that reproduces is NOT evidence the check works. See --red-proof in
# tests/test_layout_verifier_bites.py: a substituted font must move the hash, and a
# one-character prose edit must move the page it lands on. A verifier nobody broke on
# purpose is a verifier nobody has tested.
#
# Exit 0 = this document reproduces. Any other exit = it does not, and the manifest is no
# longer a true statement about the committed PDF.
# =========================================================================================
set -uo pipefail
cd "$(dirname "$0")"
HERE="$(pwd)"
REPO="$(cd ../.. && pwd)"
MANIFEST="$HERE/LAYOUT-MANIFEST.json"

die() { echo "VERIFY FAILED — $*" >&2; exit 1; }

[ -f "$MANIFEST" ] || die "LAYOUT-MANIFEST.json is absent — there is nothing to reproduce."
[ -f "$HERE/wealth-tensor-capture.pdf" ] || die "the committed PDF is absent."

COMMIT="$(python3 -c "import json;print(json.load(open('$MANIFEST'))['source_commit'])")"
git -C "$REPO" cat-file -e "${COMMIT}^{commit}" 2>/dev/null \
  || die "source_commit $COMMIT is not a commit in this repository."

WT="$(mktemp -d "${TMPDIR:-/tmp}/wt-verify.XXXXXX")"
cleanup() { git -C "$REPO" worktree remove --force "$WT/src" >/dev/null 2>&1; rm -rf "$WT"; }
trap cleanup EXIT

echo "== P13e · rebuild from a clean checkout"
echo "   source_commit : $COMMIT"
echo "   worktree      : $WT/src"
git -C "$REPO" worktree add --detach "$WT/src" "$COMMIT" >/dev/null 2>&1 \
  || die "could not materialise a clean worktree at $COMMIT"

[ -x "$WT/src/docs/deliverable/build.sh" ] \
  || die "the commit named by the manifest has no docs/deliverable/build.sh — the manifest
        points at a tree that could not have produced this document."

echo "== rebuilding (this runs the full recipe; ~1-2 min)"
if ! WT_STAMP_COMMIT="$COMMIT" bash "$WT/src/docs/deliverable/build.sh" --no-manifest \
     > "$WT/build.log" 2>&1; then
  echo "--- tail of the rebuild log:"; tail -30 "$WT/build.log"
  die "the rebuild itself did not complete."
fi
grep -E '^  (Overfull|Missing|ok      wealth)' "$WT/build.log" | sed 's/^/   /'

FRESH="$WT/src/docs/deliverable/wealth-tensor-capture.pdf"
[ -f "$FRESH" ] || die "the rebuild produced no PDF."

echo "== comparing against the committed manifest"
# Redirected to a FILE and then cat'd, never piped: `tool --verify | tee log` yields tee's
# status, which is the -93 defect this repository has now paid for twice. The log is kept
# because the count below is cross-checked against what wt176 said.
python3 "$HERE/wt176_layout_manifest.py" --verify "$FRESH" > "$WT/verify.log" 2>&1
RC=$?
cat "$WT/verify.log"
[ $RC -eq 0 ] || die "the layout did not reproduce (see above)."

# ------------------------------------------------------------------ THE NUMBER THIS RUN IS HELD TO
# wealthTensor-98. This script used to print no count at all, so its whole claim was an exit
# code -- the weakest half, and the half that stays 0 while the corpus moves. The number is
# DERIVED from the artefact this run just built, and derived TWICE, independently: wt176
# counts the pages it hashed, and pypdf is asked again here from scratch. A value handed to
# a script and printed back is not a measurement (`-92`'s tautology); two instruments that
# have to agree is one.
PAGES="$(python3 -c 'import sys, pypdf; print(len(pypdf.PdfReader(sys.argv[1]).pages))' "$FRESH")" \
  || die "could not count the pages of the rebuilt PDF."
case "$PAGES" in
  ''|*[!0-9]*) die "the rebuilt PDF's page count came back as '$PAGES', which is not a number.";;
esac
SAID="$(sed -n 's/^ *wt176: \([0-9][0-9]*\) pages compared.*/\1/p' "$WT/verify.log")"
[ -n "$SAID" ] || die "wt176 printed no 'pages compared' line -- the count this claim is held to
        has gone missing, and a claim held to a line that is not there is held to nothing."
[ "$SAID" = "$PAGES" ] || die "two independent counts of the rebuilt PDF disagree: wt176 says
        '$SAID', a fresh pypdf read of the same file says '$PAGES'. One of the two instruments
        is broken; do not believe either number until you know which."

# ===================================================================================== P13e-b
# THE HALF THIS SCRIPT COULD NOT SEE, AND THE WAY IT WAS FOUND.
#
# Everything above rebuilds from a CLEAN WORKTREE AT THE MANIFEST'S OWN COMMIT. That proves
# the committed PDF is not a hand-edited artefact and that the recipe is deterministic. It
# says NOTHING WHATEVER about the tree you are standing in.
#
# wealthTensor-110 added \usepackage{graphicx}, a figure measure and a \wtdoclabel macro to
# preamble.tex, changed the lua filter and changed build.sh -- then ran this script and got
# a green PASS. The green was real and was about SOMEBODY ELSE'S SOURCE: the worktree it
# built came from ebb02ed, which predates every one of those edits. A verifier that checks
# out an old commit is structurally incapable of failing on your change. (It happened that
# the change moved nothing -- measured separately, by hand, which is exactly the manual step
# this leg exists to abolish.)
#
# So: when any layout-deciding input differs between the manifest's commit and the tree as it
# stands right now -- committed or not, `git diff` here spans both -- rebuild AGAIN from the
# current tree and hold that build to the same manifest.
#
# A FAILURE HERE IS NOT A BUG IN THIS SCRIPT. It means the manifest is no longer a true
# statement about this tree, and the remedy is to re-emit it (build.sh, without
# --no-manifest) once the new layout is the one you meant.
INPUTS="docs/deliverable/build.sh
docs/deliverable/preamble.tex
docs/deliverable/preflight.sh
docs/deliverable/wt175_md2tex.lua
docs/deliverable/wt176_layout_manifest.py
docs/deliverable/TABLE-WIDTHS.tsv
docs/deliverable/fonts
docs/papers"
echo
echo "== P13e-b · and the CURRENT tree, which the rebuild above cannot see"
DRIFT="$(git -C "$REPO" diff --name-only "$COMMIT" -- $INPUTS 2>/dev/null)"
if [ -z "$DRIFT" ]; then
  echo "  ok      every layout-deciding input is identical to ${COMMIT:0:12};"
  echo "          the rebuild above already IS a statement about this tree"
else
  echo "  $(printf '%s\n' "$DRIFT" | wc -l | tr -d ' ') input(s) differ from ${COMMIT:0:12}:"
  printf '%s\n' "$DRIFT" | sed 's/^/            /'
  CUR="$WT/cur"
  mkdir -p "$CUR"
  # A build.sh that predates the WT_CAPTURE override would ignore it and write the tracked
  # capture instead, and the leg would then verify a PDF that is not there -- which is how
  # this was found: a FileNotFoundError wearing the costume of a layout failure. A leg that
  # CANNOT RUN is not a leg that passed.
  grep -q "WT_CAPTURE" "$HERE/build.sh" || die "this tree's docs/deliverable/build.sh has no
        WT_CAPTURE override, so the current-tree rebuild cannot be run without overwriting the
        committed capture. P13e-b cannot execute here, and a check that cannot execute is not
        a check that passed."
  if ! WT_STAMP_COMMIT="$COMMIT" WT_OUT="$CUR/build" WT_CAPTURE="$CUR/capture.pdf" \
       bash "$HERE/build.sh" --no-manifest > "$WT/cur-build.log" 2>&1; then
    echo "--- tail of the current-tree rebuild log:"; tail -30 "$WT/cur-build.log"
    die "the CURRENT tree does not build at all. The manifest commit still does (above), so
        this is a break introduced after ${COMMIT:0:12}."
  fi
  python3 "$HERE/wt176_layout_manifest.py" --verify "$CUR/capture.pdf" > "$WT/cur-verify.log" 2>&1
  CRC=$?
  sed 's/^/  /' "$WT/cur-verify.log"
  [ $CRC -eq 0 ] || die "the current tree builds, but it does NOT reproduce the committed
        layout. One of the inputs listed above moved a page. Either that was the intention --
        in which case re-emit LAYOUT-MANIFEST.json with ./build.sh -- or it was not, in which
        case the capture and the tree have parted company and the manifest is now false."
  CSAID="$(sed -n 's/^ *wt176: \([0-9][0-9]*\) pages compared.*/\1/p' "$WT/cur-verify.log")"
  case "$CSAID" in
    ''|*[!0-9]*) die "the current-tree verify printed no usable page count (got '$CSAID').
        See -98: a claim held to a line that is not there is held to nothing." ;;
  esac
  echo "  ok      the current tree reproduces the same $CSAID pages; those inputs move nothing"
fi

echo
echo "P13e PASS — the committed capture rebuilds, page for page, from ${COMMIT:0:12}."
echo "verify-layout: $PAGES pages reproduced from ${COMMIT:0:12}"
exit 0
