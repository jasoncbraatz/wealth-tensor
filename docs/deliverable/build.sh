#!/usr/bin/env bash
# docs/deliverable/build.sh
# =========================================================================================
# P13a · BUILD THE CAPTURE. Executes docs/deliverable/RECIPE.md steps 1-17 over the four
# manuscripts and produces docs/deliverable/wealth-tensor-capture.pdf plus
# docs/deliverable/LAYOUT-MANIFEST.json.
#
# THE ONE THING THIS SCRIPT IS FOR, beyond running the commands: it promotes the toolchain's
# two SILENT wrongnesses to fatal. LaTeX reports an overfull box and a missing glyph as log
# WARNINGS, so a document that has lost 126 verification marks and pushed a 64-character
# identifier into the margin still exits 0 and still looks plausible. Both are errors here.
#
#   ./build.sh                 build; refuse on any silent-wrongness
#   ./build.sh --no-manifest   build only; do not rewrite LAYOUT-MANIFEST.json (verify uses this)
#
# Env:
#   WT_STAMP_COMMIT   build as if HEAD were this commit (verify-layout.sh sets it)
#   WT_OUT            output directory for the built artefacts (default ./build)
# =========================================================================================
set -uo pipefail
cd "$(dirname "$0")"
HERE="$(pwd)"
REPO="$(cd ../.. && pwd)"

# The converter pin. RECIPE.md step 2 pins the engine; this pins the thing that feeds it.
PIN_PANDOC="${WT_PANDOC_PIN:-3.9.0.2}"

OUT="${WT_OUT:-$HERE/build}"
WRITE_MANIFEST=1
RETUNE=0
for a in "$@"; do
  case "$a" in
    --no-manifest) WRITE_MANIFEST=0 ;;
    --retune)      RETUNE=1 ;;
  esac
done
# The per-table measures are overridable for the same reason the manuscript set is: a
# review build over DIFFERENT manuscripts has different tables, and --retune writes this
# file. Retuning into the committed one would silently re-measure the canonical capture
# against a document it is not a statement about.
TWTSV="${WT_TABLE_WIDTHS:-$HERE/TABLE-WIDTHS.tsv}"

PAPERS="paper-I-price-formation/paper-I.md
paper-II-redistribution/paper-II.md
paper-III-dual-tensor/paper-III.md
paper-IV-composition/paper-IV.md"

# THE MANUSCRIPT SET IS OVERRIDABLE, AND THE LITERAL BLOCK ABOVE IS LOAD-BEARING.
# scripts/wt177_figure_guard.py parses `^PAPERS="..."` out of THIS file to learn what the
# corpus is, so the canonical four must stay written out verbatim -- an override folded into
# the assignment (PAPERS="${WT_PAPERS:-...}") would hand the guard a shell expression and it
# would scope itself to nothing. Hence a separate line, after.
#
# WT_PAPERS      a different manuscript set (paths relative to WT_PAPERS_ROOT)
# WT_PAPERS_ROOT where those paths start (default docs/papers)
# WT_CAPTURE     where the finished PDF lands (default wealth-tensor-capture.pdf, beside this)
#
# wealthTensor-110 added these to typeset the v2 review pair as ITS OWN capture, so that
# docs/deliverable/wealth-tensor-capture.pdf -- which P13e's LAYOUT-MANIFEST.json is a
# statement about, page by page and hash by hash -- is not touched by a review build.
PAPERS_ROOT="${WT_PAPERS_ROOT:-docs/papers}"
CAPTURE="${WT_CAPTURE:-$HERE/wealth-tensor-capture.pdf}"
[ -n "${WT_PAPERS:-}" ] && PAPERS="$WT_PAPERS"

die() { echo; echo "BUILD REFUSED — $*" >&2; exit 1; }
step() { printf '\n== %s\n' "$*"; }

# ---- RECIPE step 1 · refuse to build on the wrong dependencies -------------------------
step "step 1 · preflight (fonts by checksum, engine, TeX Live year)"
./preflight.sh >/tmp/wt-preflight.$$ 2>&1
PF=$?
tail -3 /tmp/wt-preflight.$$
[ $PF -eq 0 ] || { cat /tmp/wt-preflight.$$; die "preflight exit $PF. There is deliberately no fallback path."; }
rm -f /tmp/wt-preflight.$$

# ---- wt175 · pin the converter ---------------------------------------------------------
step "wt175 · converter pin"
command -v pandoc >/dev/null || die "pandoc absent"
GOT_PANDOC="$(pandoc --version | head -1 | awk '{print $2}')"
if [ "$GOT_PANDOC" != "$PIN_PANDOC" ]; then
  die "pandoc $GOT_PANDOC, but the layout was measured against $PIN_PANDOC.
        The converter is where the layout silently changes: a different pandoc can emit a
        different table environment or a different escape and move every page boundary after
        it. If you are changing it DELIBERATELY, set WT_PANDOC_PIN=$GOT_PANDOC AND regenerate
        LAYOUT-MANIFEST.json — the old manifest is no longer a statement about this document."
fi
echo "  ok      pandoc $GOT_PANDOC (pinned)"

# ---- the stamp · a function of the COMMIT, never of the wall clock ---------------------
step "P13a · commit stamp"
COMMIT="${WT_STAMP_COMMIT:-$(git -C "$REPO" rev-parse HEAD)}"
git -C "$REPO" cat-file -e "${COMMIT}^{commit}" 2>/dev/null || die "not a commit: $COMMIT"
SHORT="$(git -C "$REPO" rev-parse --short=12 "$COMMIT")"
CDATE="$(git -C "$REPO" show -s --format=%cs "$COMMIT")"
echo "  ok      $SHORT  ($CDATE)"

mkdir -p "$OUT"
# FIGURES TRAVEL TO THE BUILD DIRECTORY, and are referenced by bare filename.
# latexmk runs with its CWD in $OUT, so an \includegraphics path has to resolve from there.
# The alternatives were both worse: \graphicspath with an absolute repo path makes the .tex
# machine-dependent, and a relative ../../ path makes it depend on where $OUT happens to be.
# A copy costs 250KB and makes the build directory self-contained.
if [ -d "$REPO/docs/figures" ]; then
  cp "$REPO"/docs/figures/*.pdf "$OUT/" 2>/dev/null || true
fi
printf '%% generated by build.sh — do not edit\n\\def\\wtcommit{%s}\n\\def\\wtbuilt{%s}\n' \
  "$SHORT" "$CDATE" > "$OUT/wt-stamp.tex"
printf '\\def\\wtdoclabel{%s}\n' "${WT_DOCLABEL:-wealth-tensor capture}" >> "$OUT/wt-stamp.tex"
# WT_FOOTER_STAMP=off drops the commit + date from the page footer. Default on: P13a asks
# for a capture no sheet of which is ambiguous, and that row is not being retired here.
printf '\\def\\wtfooterstamp{%s}\n' "${WT_FOOTER_STAMP:-on}" >> "$OUT/wt-stamp.tex"

# ---- convert · Markdown -> LaTeX through the pinned filter -----------------------------
step "wt175 · convert four manuscripts"
BODIES=""
for rel in $PAPERS; do
  src="$REPO/$PAPERS_ROOT/$rel"
  [ -f "$src" ] || die "manuscript absent: $src"
  slug="$(basename "$(dirname "$rel")")"
  # The leading '# Title' line is lifted out and set at the TITLE scale of RECIPE step 11;
  # the rest is shifted up one level so '##' becomes \section (13.0pt), which is what the
  # heading scale is written for. Converting '#' to \section would set a paper's title in
  # the same face and size as its own subsections.
  title="$(sed -n '1s/^# //p' "$src")"
  [ -n "$title" ] || die "$rel has no level-1 title on line 1"
  # FRONT MATTER IS STRUCTURE THAT MARKDOWN WROTE AS CONSECUTIVE LINES. Author, affiliation
  # and e-mail sit on three lines and become ONE paragraph, which set the address flush into
  # a justified line and HYPHENATED IT -- "jason@braatzre-search.com", an address that looks
  # like it contains a hyphen and does not. Every non-blank line before the manuscript's
  # first horizontal rule gets a markdown hard break, which is what those line endings meant.
  python3 - "$src" "$OUT/$slug.body.md" <<'PYFM'
import sys
lines = open(sys.argv[1]).read().split("\n")[1:]        # drop the level-1 title
end = next((i for i, l in enumerate(lines) if l.strip() == "---"), len(lines))
for i in range(end):
    nxt = lines[i + 1] if i + 1 < len(lines) else ""
    if lines[i].strip() and nxt.strip() and not lines[i].rstrip().endswith("  "):
        lines[i] = lines[i].rstrip() + "  "
open(sys.argv[2], "w").write("\n".join(lines))
PYFM
  WT_SLUG="$slug" pandoc "$OUT/$slug.body.md" \
      --from=markdown+pipe_tables+tex_math_dollars+smart \
      --to=latex \
      --top-level-division=section \
      --shift-heading-level-by=-1 \
      --lua-filter="$HERE/wt175_md2tex.lua" \
      --wrap=preserve \
      -o "$OUT/$slug.body.tex" || die "pandoc failed on $rel"
  { printf '\\clearpage\n\\wtpapertitle{'
    printf '%s' "$title" | sed 's/\\/\\textbackslash{}/g; s/&/\\&/g; s/%/\\%/g; s/#/\\#/g; s/_/\\_/g'
    printf '}\n'
    cat "$OUT/$slug.body.tex"
  } > "$OUT/$slug.tex"
  echo "  ok      $slug  ($(wc -l < "$OUT/$slug.tex") lines tex)"
  BODIES="$BODIES$slug"$'\n'
done

# ---- assemble --------------------------------------------------------------------------
step "assemble main.tex"
# Regenerated EVERY run, and the guard below is not ceremony: an earlier cut of this script
# lost the assemble block entirely and kept building, because build/ still held the previous
# run's main.tex. It only surfaced in a clean worktree -- which is precisely why P13e
# rebuilds in one rather than in place.
rm -f "$OUT/main.tex"
{
  printf '%% generated by build.sh — do not edit. Edit preamble.tex and the manuscripts.\n'
  printf '\\input{preamble.tex}\n'
  printf '\\begin{document}\n'
  printf '\\thispagestyle{wtcapture}\n'
  # WT_COVER=off omits the corpus cover page. The default is the capture's cover, so an
  # unset environment builds exactly what it always built. A public preprint is a single
  # manuscript and must not open on a page announcing a four-paper corpus at a git commit.
  if [ "${WT_COVER:-capture}" != "off" ]; then
    printf '\\wtpapertitle{wealth-tensor: a point-in-time capture}\n'
    printf '\\noindent\\textbf{Jason C. Braatz}\\\\\n'
    printf '\\emph{Independent researcher}\\\\\n'
    printf 'jason@braatzresearch.com\n\\par\\vspace{14.0pt}\n'
    printf '\\noindent This document is a capture of the wealth-tensor corpus at commit\n'
    printf '\\texttt{\\wtcommit}, dated \\wtbuilt. It is not a submission and its four\n'
    printf 'manuscripts are at different stages: Paper~I carries its own supersession notice\n'
    printf 'and is retained as written. The layout is generated from\n'
    printf '\\texttt{docs/deliverable/RECIPE.md} and its reproducibility is asserted by\n'
    printf '\\texttt{docs/deliverable/verify-layout.sh}; the commit above appears in the footer\n'
    printf 'of every page so that no sheet of a printed copy is ambiguous about which capture\n'
    printf 'it came from.\n\\par\\vspace{14.0pt}\n'
    printf '\\noindent\\textbf{Contents}\n\\par\\vspace{7.0pt}\n'
    printf '\\begin{itemize}\\setlength{\\itemsep}{0pt}\n'
    for slug in $BODIES; do
      printf '\\item %s\n' "$(echo "$slug" | sed 's/paper-\([IV]*\)-\(.*\)/Paper \1 — \2/; s/-/ /g')"
    done
    printf '\\end{itemize}\n'
  fi
  for slug in $BODIES; do printf '\\input{%s.tex}\n' "$slug"; done
  printf '\\end{document}\n'
} > "$OUT/main.tex"
[ -s "$OUT/main.tex" ] || die "main.tex was not assembled"
echo "  ok      $(wc -l < "$OUT/main.tex" | tr -d ' ') lines"

emit_widths() {
  : > "$OUT/wt-tablewidths.tex"
  if [ -f "$TWTSV" ]; then
    awk -F'\t' 'NR>1 && $1!~/^#/ && $1!="table_id" && NF>=3 {
      printf "\\expandafter\\def\\csname wt@tw@%s\\endcsname{%s}\n",$1,$2
      if ($3 != "-")
        printf "\\expandafter\\def\\csname wt@ts@%s\\endcsname{\\fontsize{%s}{%s}\\selectfont}\n",$1,$3,$4 }' \
      "$TWTSV" > "$OUT/wt-tablewidths.tex"
  fi
  printf '%s' "$(grep -c 'wt@tw@' "$OUT/wt-tablewidths.tex" 2>/dev/null || echo 0)"
}

run_latex() {
  rm -f "$OUT/main.pdf" "$OUT/main.log"
  TEXINPUTS=".:$OUT:" latexmk -lualatex -interaction=nonstopmode -halt-on-error \
     -outdir="$OUT" "$OUT/main.tex" >"$OUT/latexmk.out" 2>&1
}

step "per-table measures"
N=$(emit_widths)
if [ -f "$TWTSV" ]; then
  echo "  ok      TABLE-WIDTHS.tsv — $N table(s) given a wider measure; the rest are body width"
else
  echo "  ok      no TABLE-WIDTHS.tsv yet — every table at the body measure (run --retune)"
fi

# ---- RECIPE step 17 · build ------------------------------------------------------------
step "step 17 · latexmk -lualatex"
run_latex
RC=$?
if [ $RC -ne 0 ]; then
  echo "--- last 40 lines of the engine log:"; tail -40 "$OUT/main.log" 2>/dev/null
  die "latexmk exit $RC"
fi

# ---- --retune · derive each table's measure FROM THE BUILD ------------------------------
# Widths are not guessed and not uniform: each table is built at the body measure, the engine
# says by how much it overflowed, and that number plus a point becomes its measure. Widening
# a table rewraps its p-columns, so the residual is not linear and one pass does not settle
# it -- the loop iterates to a fixed point. The RESULT is committed to TABLE-WIDTHS.tsv, so
# an ordinary build (and every verify) is a single deterministic pass that reads a reviewed
# file rather than re-deriving it.
if [ "$RETUNE" -eq 1 ]; then
  step "--retune · deriving per-table measures from the engine"
  for pass in 1 2 3 4 5 6; do
    CHANGED=$(python3 - "$OUT/main.log" "$TWTSV" <<'PYTUNE'
import re, sys, os
log, tsv = sys.argv[1], sys.argv[2]
BODY, CAP, SLACK = 289.08, 500.0, 1.0
SIZES = [("10.0", "12.0"), ("9.0", "11.0"), ("8.0", "10.0")]

cur, order = {}, []
if os.path.exists(tsv):
    for ln in open(tsv):
        if ln.startswith("#") or not ln.strip():
            continue
        f = ln.rstrip("\n").split("\t")
        if len(f) >= 5 and f[0] != "table_id":
            cur[f[0]] = f
            order.append(f[0])

text = open(log, errors="replace").read()
# Walk the log IN ORDER, tracking which table we are inside. An alignment box is the table
# itself being too wide; a paragraph box inside a table is one CELL too narrow, and those
# scale differently -- hence the two buckets.
pat = (r"WT-TABLE-BEGIN:([^:\s]+):(\d+):([\d.]+)pt"
       r"|WT-TABLE-END:(\S+)"
       r"|^Overfull \\hbox \(([\d.]+)pt too wide\) in (alignment|paragraph)")
align, cell, ncols, width, active = {}, {}, {}, {}, None
for m in re.finditer(pat, text, re.M):
    if m.group(1):
        active = m.group(1)
        ncols[active] = max(1, int(m.group(2)))
        width[active] = float(m.group(3))
    elif m.group(4):
        active = None
    elif m.group(5) and active:
        v, kind = float(m.group(5)), m.group(6)
        d = align if kind == "alignment" else cell
        if v > d.get(active, 0.0):
            d[active] = v

changed = 0
for tid in sorted(set(align) | set(cell)):
    w, n = width.get(tid, BODY), ncols.get(tid, 1)
    # a table too wide needs its own deficit; a cell too narrow needs it once per column
    need = max(align.get(tid, 0.0), cell.get(tid, 0.0) * n)
    new_w = min(CAP, round((w + need + SLACK) * 2) / 2)
    row = cur.get(tid, [tid, "%.1fpt" % BODY, "-", "-", "", ""])
    size, lead = (row[2], row[3]) if row[2] != "-" else SIZES[0]
    why = "table overflowed by %.2fpt" % align[tid] if tid in align else \
          "a cell overflowed its column by %.2fpt across %d columns" % (cell[tid], n)
    if new_w <= w + 0.01:
        # already at the cap and still too wide: step the type down instead
        idx = next((k for k, (a, b) in enumerate(SIZES) if a == size), 0)
        if idx + 1 >= len(SIZES):
            continue
        size, lead = SIZES[idx + 1]
        why += "; at the %.0fpt cap, so its type steps to %s/%s" % (CAP, size, lead)
        new_w = w
    cur[tid] = [tid, "%.1fpt" % new_w, size, lead, "%.2f" % need, why]
    if tid not in order:
        order.append(tid)
    changed += 1

if changed:
    with open(tsv, "w") as f:
        f.write("# docs/deliverable/TABLE-WIDTHS.tsv\n")
        f.write("# ONE MEASURE PER TABLE, derived by `build.sh --retune` from what the engine\n")
        f.write("# actually reported, and COMMITTED so that an ordinary build -- and every\n")
        f.write("# verify -- is a single deterministic pass over a reviewed file rather than a\n")
        f.write("# re-derivation. A table absent from this list is set at the body measure\n")
        f.write("# (289.08pt) at 10.0/12.0. Column 5 is the deficit, in points, that forced the\n")
        f.write("# width in column 2, so every row carries the measurement that justifies it.\n")
        f.write("# Do not hand-edit: run ./build.sh --retune.\n")
        f.write("table_id\twidth\tsize_pt\tleading_pt\tdeficit_pt\twhy\n")
        for t in order:
            if t in cur:
                f.write("\t".join(cur[t]) + "\n")
print(changed)
PYTUNE
)
    echo "  pass $pass: $CHANGED table(s) rewidened"
    [ "${CHANGED:-0}" = "0" ] && break
    emit_widths >/dev/null
    run_latex || die "latexmk failed during retune pass $pass"
  done
  echo "  ok      TABLE-WIDTHS.tsv settled"
fi

[ -f "$OUT/main.pdf" ] || die "latexmk exited 0 but produced no PDF"

# ---- THE TWO SILENT WRONGNESSES, PROMOTED TO FATAL -------------------------------------
step "the two silent wrongnesses"
OVER=$(grep -c '^Overfull \\hbox' "$OUT/main.log" 2>/dev/null || true); OVER=${OVER:-0}
MISS=$(grep -c '^Missing character:' "$OUT/main.log" 2>/dev/null || true); MISS=${MISS:-0}
UNDER=$(grep -c '^Underfull \\hbox' "$OUT/main.log" 2>/dev/null || true); UNDER=${UNDER:-0}
echo "  Overfull \\hbox   : $OVER"
echo "  Missing character: $MISS"
echo "  Underfull \\hbox  : $UNDER   (reported, not fatal — an underfull box is loose, not wrong)"
if [ "$MISS" -ne 0 ]; then
  echo "--- the missing glyphs:"; grep '^Missing character:' "$OUT/main.log" | sort -u | head -20
  die "$MISS missing character(s). LaTeX sets NOTHING for these and exits 0. A capture with
        silently absent glyphs is the failure this check exists to make loud."
fi
if [ "$OVER" -ne 0 ]; then
  echo "--- the overfull boxes:"; grep -A2 '^Overfull \\hbox' "$OUT/main.log" | head -60
  die "$OVER overfull box(es). RECIPE step 13 requires zero on the probe and the inherited
        done-when requires zero on the real build. If these are tables, run ./build.sh --retune."
fi
echo "  ok      zero overfull boxes, zero missing characters"

# ---- THE THIRD SILENT WRONGNESS: INK OFF THE PAPER -------------------------------------
# ZERO OVERFULL BOXES DOES NOT MEAN THE DOCUMENT FITS ON THE PAGE, and this check exists
# because that was nearly shipped. An overfull box is reported when a line exceeds \hsize --
# so any construction that WIDENS \hsize (which is exactly what the wide-table environment
# does) silences the warning whether or not the result is still on the sheet. An early cut of
# \begin{wttable} reported zero overfull boxes while running every wide table off the right
# edge of the paper; only measuring the ink caught it.
step "ink on the paper (what the overfull count cannot see)"
if command -v gs >/dev/null 2>&1; then
  python3 - "$OUT/main.pdf" <<'PYBBOX'
import subprocess, sys, re
pdf = sys.argv[1]
PAPER_W, PAPER_H = 612.0, 792.0     # US Letter in PostScript points (bp)
MIN = 18.0                          # a quarter inch of clearance, on all four sides
out = subprocess.run(["gs","-q","-dNOPAUSE","-dBATCH","-sDEVICE=bbox",pdf],
                     capture_output=True, text=True).stderr
boxes = [tuple(map(float, m.groups()))
         for m in re.finditer(r"%%HiResBoundingBox: ([\d.-]+) ([\d.-]+) ([\d.-]+) ([\d.-]+)", out)]
if not boxes:
    print("  WARN    ghostscript reported no bounding boxes; check skipped"); sys.exit(0)
bad = [(i+1,b) for i,b in enumerate(boxes)
       if b[0] < MIN or b[1] < MIN or b[2] > PAPER_W-MIN or b[3] > PAPER_H-MIN]
print("  %d pages measured; ink spans x %.1f..%.1f  y %.1f..%.1f bp on a %gx%g sheet"
      % (len(boxes), min(b[0] for b in boxes), max(b[2] for b in boxes),
         min(b[1] for b in boxes), max(b[3] for b in boxes), PAPER_W, PAPER_H))
if bad:
    print("  %d page(s) put ink within %.0fbp of a paper edge:" % (len(bad), MIN))
    for n,b in bad[:10]:
        print("     page %-4d bbox %.1f %.1f %.1f %.1f" % (n,b[0],b[1],b[2],b[3]))
    sys.exit(1)
print("  ok      every page clears all four edges by at least %.0fbp" % MIN)
PYBBOX
  [ $? -eq 0 ] || die "ink runs off the paper on at least one page. Zero overfull boxes did
        not catch it and never could: widening \\hsize suppresses the warning without moving
        the ink back onto the sheet."
else
  echo "  WARN    ghostscript absent; page-bounds check skipped"
fi

cp "$OUT/main.pdf" "$CAPTURE"
PAGES=$(python3 -c "import pypdf;print(len(pypdf.PdfReader('$CAPTURE').pages))")
echo "  ok      $(basename "$CAPTURE") — $PAGES pages"

if [ "$WRITE_MANIFEST" -eq 1 ]; then
  step "P13e · LAYOUT-MANIFEST.json"
  WT_COMMIT="$COMMIT" WT_PANDOC="$GOT_PANDOC" python3 "$HERE/wt176_layout_manifest.py" --emit
fi
echo
echo "BUILD OK"
