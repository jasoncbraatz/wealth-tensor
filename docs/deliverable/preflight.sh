#!/usr/bin/env bash
# wealth-tensor · docs/deliverable/preflight.sh
#
# REFUSE TO BUILD RATHER THAN APPROXIMATE. This is P13c, and it exists because of one fact
# about the toolchain: LaTeX does not fail when a font is missing, it SUBSTITUTES. The build
# succeeds, the metrics shift by a hair, the reflow moves, a page boundary slides, and the
# document comes out CLOSE. Close is the failure mode -- it costs Jason the layout and
# visualisation analysis a second time, and doing that ONCE is the entire reason this
# deliverable exists.
#
# Measured on darwin 2026-08-16 and not hypothetical: macOS ships its own STIX Two Text at
# /System/Library/Fonts/Supplemental/STIXTwoText.ttf, with different metrics from TeX Live's
# STIXTwoText OTF. A family-NAME lookup can resolve to either on a machine that looks
# identical from the outside. That is why the recipe loads fonts by PATH and why this script
# verifies them by CHECKSUM.
#
#   ./preflight.sh                 full check: fonts, engine, TeX Live year, packages, tools
#   ./preflight.sh --fonts-only    just the vendored fonts (what P13d asserts)
#
# Exit 0 = every named dependency is present and byte-identical to what the layout was
# measured against. Any other exit = DO NOT BUILD. There is deliberately no fallback path.
set -uo pipefail
cd "$(dirname "$0")"

PIN_TEXLIVE="${WT_TEXLIVE_PIN:-2026}"
FAIL=0
say()  { printf '  %-7s %s\n' "$1" "$2"; }
bad()  { say "FAIL" "$1"; FAIL=1; }
ok()   { say "ok" "$1"; }

# ---------------------------------------------------------------- fonts
check_fonts() {
  echo "== vendored fonts (checksum, not name) =="
  [ -f fonts/FONTS.tsv ] || { bad "fonts/FONTS.tsv is absent — nothing is pinned"; return; }
  local n=0
  while IFS=$'\t' read -r file pkg want src bytes; do
    case "$file" in '#'*|file|'') continue ;; esac
    if [ ! -f "fonts/$file" ]; then
      bad "$file — VENDORED FILE MISSING. Do not substitute; restore it from git."
      continue
    fi
    got=$(shasum -a 256 "fonts/$file" 2>/dev/null | cut -d' ' -f1)
    if [ "$got" != "$want" ]; then
      bad "$file — CHECKSUM MISMATCH (want ${want:0:16}, got ${got:0:16}). The layout was"
      say "" "        measured against the other file. Rebuilding now produces a different document."
      continue
    fi
    n=$((n+1))
  done < fonts/FONTS.tsv
  [ "$FAIL" -eq 0 ] && ok "$n font file(s) present and byte-identical"
}

# ---------------------------------------------------------------- toolchain
check_tools() {
  echo "== engine and toolchain =="
  for t in lualatex latexmk pandoc; do
    command -v "$t" >/dev/null 2>&1 && ok "$t $(command -v "$t")" || bad "$t is absent"
  done

  if command -v lualatex >/dev/null 2>&1; then
    year=$(lualatex --version 2>&1 | grep -oE 'TeX Live [0-9]{4}' | grep -oE '[0-9]{4}' | head -1)
    if [ "$year" = "$PIN_TEXLIVE" ]; then
      ok "TeX Live $year (pinned)"
    else
      bad "TeX Live $year, but the layout was measured against $PIN_TEXLIVE."
      say "" "        A distribution bump can move metrics. If you are changing it DELIBERATELY,"
      say "" "        set WT_TEXLIVE_PIN=$year AND regenerate LAYOUT-MANIFEST.json — the old"
      say "" "        manifest is no longer a statement about this document."
    fi
  fi

  echo "== required packages =="
  for p in unicode-math.sty fontspec.sty microtype.sty booktabs.sty natbib.sty; do
    if kpsewhich "$p" >/dev/null 2>&1; then ok "$p"; else bad "$p is absent (tlmgr install)"; fi
  done
}

case "${1:-}" in
  --fonts-only) check_fonts ;;
  *)            check_fonts; check_tools ;;
esac

echo
if [ "$FAIL" -eq 0 ]; then
  echo "PREFLIGHT PASS — safe to build."
else
  echo "PREFLIGHT FAIL — DO NOT BUILD. Fix the lines above; do not work around them."
  echo "A build that succeeds with a substituted dependency is the failure this script exists"
  echo "to prevent, and it will look fine."
fi
exit "$FAIL"
