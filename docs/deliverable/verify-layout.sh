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
python3 "$HERE/wt176_layout_manifest.py" --verify "$FRESH"
RC=$?
[ $RC -eq 0 ] || die "the layout did not reproduce (see above)."

echo
echo "P13e PASS — the committed capture rebuilds, page for page, from ${COMMIT:0:12}."
exit 0
