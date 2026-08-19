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

echo
echo "P13e PASS — the committed capture rebuilds, page for page, from ${COMMIT:0:12}."
echo "verify-layout: $PAGES pages reproduced from ${COMMIT:0:12}"
exit 0
