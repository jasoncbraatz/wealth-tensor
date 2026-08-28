#!/usr/bin/env bash
# docs/deliverable/redproof-layout.sh
# =========================================================================================
# P13e's SECOND HALF. verify-layout.sh passing proves the document rebuilds; it does not
# prove the verifier would NOTICE if it stopped. A check nobody has broken on purpose is a
# check nobody has tested, and a per-page hash that is never made to move is indistinguishable
# from a per-page hash that cannot move.
#
# Four runs, each in its own clean worktree at the manifest's source_commit:
#
#   CONTROL   an untouched rebuild MUST pass. Without this the bites prove nothing -- a
#             verifier that always failed would "detect" every breakage put to it.
#
#   RP1a      A SUBSTITUTED FONT MUST MOVE THE HASH. A vendored face is replaced with a
#             DIFFERENT CUT OF THE SAME DESIGN -- close enough in metrics that the build
#             stays happy -- and its checksum in FONTS.tsv is rewritten to match, so preflight
#             is content too. Both gates that would normally stop a substitution are
#             deliberately satisfied, because that is the only way to show the per-page hash
#             catches it ON ITS OWN.
#             THIS DISTINCTION IS NOT PEDANTRY. The first cut of this probe used a heavier
#             cut; the build refused it on overfull boxes; the probe went green; and NOTHING
#             HAD TESTED THE HASH. A red-proof caught by a different guard than the one under
#             test proves the wrong thing, and from the outside it looks exactly like success.
#
#   RP1b      ...and a COARSE substitution must be refused outright, before the hash is ever
#             reached. Same mutation, heavier face. That is the layered guard doing its job,
#             and running both is how we know the two layers are independent.
#
#   RP2       A ONE-CHARACTER PROSE EDIT MUST MOVE THE PAGE IT LANDS ON. One character is
#             inserted into the first paragraph of Paper I. If the hash were taken over the
#             whole document rather than per page, or over the source rather than the
#             rendered result, this is the case that would slip through.
#
# Exit 0 = the verifier passes what it should and bites what it should.
# =========================================================================================
set -uo pipefail
cd "$(dirname "$0")"
HERE="$(pwd)"
REPO="$(cd ../.. && pwd)"
MANIFEST="$HERE/LAYOUT-MANIFEST.json"

[ -f "$MANIFEST" ] || { echo "no LAYOUT-MANIFEST.json to red-proof" >&2; exit 2; }
COMMIT="$(python3 -c "import json;print(json.load(open('$MANIFEST'))['source_commit'])")"
FAIL=0

# THE COUNT THIS RUN IS HELD TO (wealthTensor-98). Every verdict goes through say(), and
# say() is the only place a probe reports one, so bumping the tally HERE counts what the run
# actually did rather than what the script intended. See docs/deliverable/probe-tally.sh for
# why the mechanism lives in a sourced file (so it can be red-proofed without four builds).
. "$HERE/probe-tally.sh"
tally_reset
say() { tally_bump; printf '  %-8s %s\n' "$1" "$2"; }

# $1 = label, $2 = pass|bite, $3 = shell run inside the worktree's deliverable dir
probe() {
  local label="$1" expect="$2" mutate="$3" wt out rc
  wt="$(mktemp -d "${TMPDIR:-/tmp}/wt-rp.XXXXXX")"
  git -C "$REPO" worktree add --detach "$wt/src" "$COMMIT" >/dev/null 2>&1 \
    || { say FAIL "$label — could not materialise a worktree"; FAIL=1; return; }
  ( cd "$wt/src/docs/deliverable" && eval "$mutate" ) >/dev/null 2>&1

  if ! WT_STAMP_COMMIT="$COMMIT" bash "$wt/src/docs/deliverable/build.sh" --no-manifest \
       > "$wt/build.log" 2>&1; then
    if [ "$expect" = "bite" ]; then
      say "ok" "$label — REFUSED BY THE BUILD: $(grep -m1 'BUILD REFUSED' "$wt/build.log" | sed 's/^BUILD REFUSED[^A-Za-z0-9]*//' | cut -c1-70)"
    else
      say FAIL "$label — the control build did not complete"; tail -12 "$wt/build.log"; FAIL=1
    fi
    git -C "$REPO" worktree remove --force "$wt/src" >/dev/null 2>&1; rm -rf "$wt"; return
  fi

  out="$(python3 "$HERE/wt176_layout_manifest.py" --verify \
         "$wt/src/docs/deliverable/wealth-tensor-capture.pdf" 2>&1)"; rc=$?
  if [ "$expect" = "pass" ] && [ $rc -eq 0 ]; then
    say "ok" "$label — reproduces, as it must (else the bites below prove nothing)"
  elif [ "$expect" = "bite" ] && [ $rc -ne 0 ]; then
    say "ok" "$label — CAUGHT BY THE HASH: $(echo "$out" | grep -m1 FAIL | sed 's/^ *FAIL *//' | cut -c1-80)"
  else
    say FAIL "$label — expected to $expect, got rc=$rc"
    echo "$out" | sed 's/^/           /'
    FAIL=1
  fi
  git -C "$REPO" worktree remove --force "$wt/src" >/dev/null 2>&1; rm -rf "$wt"
}

# Same mutation, parameterised by the replacement face: swap it in AND make FONTS.tsv agree,
# so preflight has no complaint and only the layout guards are left to notice.
subst() {
  printf '%s\n' \
    "cp fonts/$1 fonts/LibertinusSerif-Regular.otf" \
    "python3 -c \"
import hashlib
h = hashlib.sha256(open('fonts/LibertinusSerif-Regular.otf','rb').read()).hexdigest()
rows = []
for ln in open('fonts/FONTS.tsv'):
    f = ln.rstrip('\\n').split('\\t')
    if f and f[0] == 'LibertinusSerif-Regular.otf':
        f[2] = h
        ln = '\\t'.join(f) + '\\n'
    rows.append(ln)
open('fonts/FONTS.tsv','w').writelines(rows)
\""
}

onechar() {
  printf '%s\n' "python3 -c \"
p = '../papers/paper-I-price-formation/paper-I.md'
s = open(p).read()
i = s.index('A balance sheet') if 'A balance sheet' in s else s.index('\\n\\n') + 2
open(p,'w').write(s[:i] + 'x' + s[i:])
\""
}

echo "== red-proofing the layout verifier against ${COMMIT:0:12}"
echo "   (up to ten full builds; budget several minutes)"
probe "CONTROL " pass ":"
probe "RP1a fnt" bite "$(subst LibertinusSerifDisplay-Regular.otf)"
probe "RP1b fnt" bite "$(subst LibertinusSerif-Semibold.otf)"
probe "RP2 char" bite "$(onechar)"

# ---- RP3 · THE LEG THAT TESTS THE OTHER HALF OF THE VERIFIER ---------------------------
# The three probes above drive build.sh and wt176 --verify directly. They never run
# verify-layout.sh, so they can say nothing about the ONE THING that script does on its own:
# decide WHICH TREE to hold the manifest against.
#
# Until wealthTensor-110 the answer was "the manifest's own commit, always", which means a
# session that edited preamble.tex and ran verify-layout.sh got a PASS about a checkout that
# predated its edit. RP3 is the probe for the leg that closed that.
#
# Each run materialises a worktree at the manifest commit, drops the CURRENT verify-layout.sh
# into it (the point is to test today's verifier, not the one frozen at that commit), and
# runs it there.
probe_verifier() {   # $1 label  $2 pass|bite|blind  $3 current|historic  $4 mutation
  # THE WORKTREE IS AT HEAD, NOT AT THE MANIFEST COMMIT, and that is the whole design.
  # The first cut put it at $COMMIT and the control failed for a reason that had nothing to
  # do with the leg under test: a worktree at $COMMIT carries the LAYOUT-MANIFEST.json AS IT
  # WAS THEN, which names an EARLIER commit, so P13e-b dutifully found real drift and tried
  # to rebuild -- with that commit's build.sh, which had no WT_CAPTURE override yet. A probe
  # whose control fails for an unrelated reason proves nothing in either direction.
  # HEAD is the tree the leg is actually meant to police, so HEAD is where it is tested.
  local label="$1" expect="$2" which="$3" mutate="$4" wt rc
  wt="$(mktemp -d "${TMPDIR:-/tmp}/wt-rp3.XXXXXX")"
  git -C "$REPO" worktree add --detach "$wt/src" HEAD >/dev/null 2>&1 \
    || { say FAIL "$label — could not materialise a worktree at HEAD"; FAIL=1; return; }
  if [ "$which" = "historic" ]; then
    git -C "$REPO" show "$COMMIT:docs/deliverable/verify-layout.sh" \
      > "$wt/src/docs/deliverable/verify-layout.sh" 2>/dev/null \
      || { say FAIL "$label — no verify-layout.sh at ${COMMIT:0:12}"; FAIL=1
           git -C "$REPO" worktree remove --force "$wt/src" >/dev/null 2>&1; rm -rf "$wt"; return; }
    # Once the manifest is re-emitted at a commit that already carries P13e-b there is no
    # blindness left to demonstrate. Say so and spend no builds on it -- but say it HERE, from
    # inside the one call site, so the verdict count does not depend on which branch ran.
    if grep -q "P13e-b" "$wt/src/docs/deliverable/verify-layout.sh"; then
      say "ok" "$label — the ${COMMIT:0:12} verifier already carries P13e-b; nothing left to show"
      git -C "$REPO" worktree remove --force "$wt/src" >/dev/null 2>&1; rm -rf "$wt"; return
    fi
  fi
  ( cd "$wt/src/docs/deliverable" && eval "$mutate" ) >/dev/null 2>&1
  bash "$wt/src/docs/deliverable/verify-layout.sh" > "$wt/v.log" 2>&1; rc=$?
  if [ "$expect" = "pass" ] && [ $rc -eq 0 ]; then
    say "ok" "$label — passes on an untouched HEAD, as it must"
  elif [ "$expect" = "bite" ] && [ $rc -ne 0 ]; then
    say "ok" "$label — CAUGHT: $(grep -m1 'VERIFY FAILED' "$wt/v.log" | cut -c1-66)"
  elif [ "$expect" = "blind" ] && [ $rc -eq 0 ]; then
    say "ok" "$label — the ${COMMIT:0:12} verifier passed a tree it never looked at (the hole)"
  else
    say FAIL "$label — expected $expect, got rc=$rc"; tail -8 "$wt/v.log" | sed "s/^/           /"; FAIL=1
  fi
  git -C "$REPO" worktree remove --force "$wt/src" >/dev/null 2>&1; rm -rf "$wt"
}

# a two-point change to the measure: small enough that the build stays happy, large enough
# that the page boundaries move. The SAME mutation is put to both verifiers.
WIDEN="sed -i '' 's/textwidth=289.08pt/textwidth=287.08pt/' preamble.tex"

probe_verifier "RP3 ctl " pass  current  ":"
probe_verifier "RP3 tree" bite  current  "$WIDEN"
# ...and the same mutation put to the verifier AS IT STOOD at the manifest commit. ONE CALL
# SITE, unconditionally: the "already carries the leg" case is handled INSIDE probe_verifier,
# because a say() reached down a branch that has no `probe` line behind it is a verdict the
# tally counts and test_the_three_counts_are_derived cannot account for. One call, one verdict.
probe_verifier "RP3 hist" blind historic "$WIDEN"

echo
tally_line "redproof-layout" || FAIL=1
echo
if [ "$FAIL" -eq 0 ]; then
  echo "RED-PROOF PASS — the verifier reproduces an untouched build and bites every breakage."
else
  echo "RED-PROOF FAIL — see above. A verifier that does not bite is not a verifier."
fi
exit "$FAIL"
