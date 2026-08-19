#!/usr/bin/env python3
"""wealthTensor-95 · P13f — the figure manifest, and the guard that makes it BITE.

WHY THIS EXISTS
---------------
P13f says every figure is produced by a COMMITTED script from COMMITTED numbers, listed in
`docs/deliverable/FIGURES.tsv` as figure -> script -> source. The corpus has ZERO figures,
and that is the entire difficulty: a manifest with nothing in it closes the row VACUOUSLY
and reopens it SILENTLY the day someone pastes in the first chart, because nothing is
watching. The row's own check only asks whether column 2 of each row is a file that exists
-- so a row can be true and inert at the same time. Inertness is the failure mode here, not
falsehood.

So the manifest carries one row, `@zero-figures`, which is a CLAIM rather than a figure:
*the corpus contains no figures, this script measured that, and this receipt records it.*
This guard is what makes that claim load-bearing:

  * the sentinel may not coexist with a figure (SENTINEL-WITH-FIGURES) -- that is the exact
    silent-reopen the row was written to prevent;
  * the sentinel may not be removed while the count is still zero (SENTINEL-MISSING) --
    that is the header-only file, which the row's own `n>=1` already rejects, refused a
    second time with a message that says why;
  * every figure a manuscript references must have a row (UNLISTED-FIGURE);
  * every row's script AND source must exist (ROW-SCRIPT-MISSING / ROW-SOURCE-MISSING) --
    the row's check only looks at column 2, this looks at both;
  * a row may not name a figure no manuscript uses (ORPHAN-ROW) -- manifest rot, the other
    direction, and the shape that makes a green mean nothing.

WHAT THIS CHECK IS STRUCTURALLY INCAPABLE OF SEEING
---------------------------------------------------
`-94`'s rule, in this script's own words: *when a check returns zero, ask what it is
structurally incapable of seeing.* This one is printed on EVERY run, green included, so a
zero is never filed as a guarantee:

  1. It reads the manuscripts named by `PAPERS=` in `docs/deliverable/build.sh` -- parsed,
     never hardcoded, so a fifth paper is followed automatically. A figure in a document
     OUTSIDE that list (a review doc, an ADR) is not in scope and is not seen.
  2. It cannot see a figure INJECTED by the build -- a `wt175_md2tex.lua` rule or a
     `preamble.tex` macro that emits graphics from non-figure markup. The PDF sweep below
     is the partial answer to that hole, not a complete one.
  3. The PDF sweep counts image XObjects. `pdfimages` is used when present; the raw-byte
     regex is the fallback and CANNOT see an image whose object lives inside a compressed
     `/ObjStm`. Vector art drawn with PDF operators is not an XObject and is invisible to
     both.
  4. It says nothing about whether a listed script actually PRODUCES its figure. That is
     P6's job pointed at pictures, and it needs a figure to exist before it can be written.

USAGE
    python3 scripts/wt177_figure_guard.py            # guard the live repo; rc 0 or 1
    python3 scripts/wt177_figure_guard.py --emit     # rewrite the measurement receipt
    python3 scripts/wt177_figure_guard.py --json     # print the measurement, no verdict
    # red-proof form -- point every input somewhere else, never at the real corpus:
    python3 scripts/wt177_figure_guard.py --paper A.md --paper B.md --manifest F.tsv --no-pdf
"""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD_SH = ROOT / "docs" / "deliverable" / "build.sh"
MANIFEST = ROOT / "docs" / "deliverable" / "FIGURES.tsv"
RECEIPT = ROOT / "docs" / "deliverable" / "FIGURES-MEASURED.json"
PDF = ROOT / "docs" / "deliverable" / "wealth-tensor-capture.pdf"

SENTINEL = "@zero-figures"
GUARD_VERSION = "wt177/2"

# THE TAG REGISTRY. Every failure this guard can report, declared once. The guard refuses
# to emit a tag that is not here (UNREGISTERED-TAG), and scripts/redproof_wt177_figures.py
# reads this dict to demand a probe for each -- so a future session that adds a check
# without red-proofing it gets a red, by construction, instead of a silent unproven check.
# `-94`'s rule, made mechanical: a zero from a check nobody has watched fail is a number,
# not a guarantee.
TAGS = {
    "CORPUS-UNREADABLE": "the manuscript list could not be parsed, or a named file is absent",
    "CORPUS-EMPTY": "zero manuscripts in scope — a guard over nothing finds nothing",
    "MANIFEST-MISSING": "docs/deliverable/FIGURES.tsv does not exist",
    "BLANK-ROW": "a blank line, on which the row's own awk runs `test -f \"\"` and dies mute",
    "SHORT-ROW": "a row with fewer than three tab-separated fields",
    "ROW-SCRIPT-MISSING": "a row's script (column 2) does not exist",
    "ROW-SOURCE-MISSING": "a row's source (column 3) does not exist — the half the awk skips",
    "UNLISTED-FIGURE": "a manuscript references a figure no row names",
    "ORPHAN-ROW": "a row names a figure no manuscript uses — manifest rot",
    "SENTINEL-WITH-FIGURES": "the zero-figures claim survives alongside a real figure",
    "SENTINEL-WITH-ROWS": "the zero-figures claim survives alongside a real row",
    "SENTINEL-DUPLICATED": "more than one zero-figures row",
    "SENTINEL-MISSING": "no figures and no rows — the vacuous close P13f exists to prevent",
    "PDF-IMAGE-UNDECLARED": "the built PDF carries an image no manuscript and no row declares",
    "UNREGISTERED-TAG": "the guard emitted a tag absent from TAGS — this registry has drifted",
}

# Every way a figure can enter a markdown/LaTeX manuscript that this guard knows about.
# Deliberately WIDER than the `^!\[|includegraphics|^Figure [0-9]` sweep -93 and -94 ran:
# that one is anchored to line start, so an inline image mid-sentence walks straight past it.
# `.pdf` is excluded from IMAGE_FILE on purpose -- the manuscripts may name the deliverable
# PDF in prose, and a guard that cries wolf is a guard somebody switches off.
PATTERNS = [
    ("md-image", re.compile(r"!\[[^\]]*\]\(\s*<?([^)>\s]+)")),
    ("includegraphics", re.compile(r"\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}")),
    ("html-img", re.compile(r"<img\b[^>]*\bsrc\s*=\s*[\"']([^\"']+)[\"']", re.I)),
    ("image-file", re.compile(r"([\w./+-]+\.(?:png|jpe?g|gif|svg|eps|tiff?|webp))\b", re.I)),
    ("figure-env", re.compile(r"\\begin\{figure\*?\}")),
    ("tikz", re.compile(r"\\begin\{tikzpicture\}")),
    ("pgfplots-axis", re.compile(r"\\begin\{axis\}")),
    ("caption-line", re.compile(r"^\s*(?:\*\*|__)?(?:Figure|Fig\.)\s*[0-9]")),
]


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def papers_from_build_sh(build_sh=None):
    """Parse the corpus out of build.sh. NEVER hardcode it: the sentence this guard signs
    is 'the manuscripts the deliverable is built from', and an evidence command must
    observe the thing the sentence claims, not something nearby."""
    b = build_sh or BUILD_SH
    if not b.is_file():
        return None, f"{b} is missing"
    m = re.search(r'^PAPERS="([^"]*)"', b.read_text(encoding="utf-8"), re.M | re.S)
    if not m:
        return None, f'no PAPERS="..." block in {b}'
    rels = [ln.strip() for ln in m.group(1).split("\n") if ln.strip()]
    return [ROOT / "docs" / "papers" / r for r in rels], None


def scan(paper: pathlib.Path, root: pathlib.Path):
    """Every figure reference in one manuscript, as (key, kind, lineno, raw)."""
    hits = []
    try:
        rel = str(paper.relative_to(root))
    except ValueError:
        rel = paper.name
    for lineno, line in enumerate(paper.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
        for kind, rx in PATTERNS:
            for m in rx.finditer(line):
                target = m.group(1) if rx.groups else None
                key = target if target else f"{kind}@{rel}:{lineno}"
                hits.append({"key": key, "kind": kind, "file": rel, "line": lineno,
                             "raw": line.strip()[:160]})
    # one reference may match two patterns (an `![](x.png)` is also an image-file); keep one.
    seen, uniq = set(), []
    for h in hits:
        sig = (h["key"], h["file"], h["line"])
        if sig not in seen:
            seen.add(sig)
            uniq.append(h)
    return uniq


def pdf_image_count(pdf: pathlib.Path):
    """(count, how). Two observers, because each is blind to something the other sees."""
    if not pdf.is_file():
        return 0, "absent"
    n_regex = len(re.findall(rb"/Subtype\s*/Image", pdf.read_bytes()))
    how = f"regex:{n_regex}"
    n = n_regex
    if shutil.which("pdfimages"):
        try:
            out = subprocess.run(["pdfimages", "-list", str(pdf)], capture_output=True,
                                 text=True, timeout=120)
            rows = [l for l in out.stdout.split("\n")[2:] if l.strip()]
            how += f" pdfimages:{len(rows)}"
            n = max(n, len(rows))
        except Exception as exc:  # a broken tool must not silently read as zero
            how += f" pdfimages:ERROR({exc})"
            n = max(n, n_regex)
    return n, how


def read_manifest(path: pathlib.Path):
    """(rows, fatal). rows are dicts; fatal is a list of (TAG, message) parse refusals."""
    fatal, rows = [], []
    if not path.is_file():
        return rows, [("MANIFEST-MISSING", f"{path} does not exist")]
    lines = path.read_text(encoding="utf-8").split("\n")
    for i, line in enumerate(lines, 1):
        if i == 1:
            continue  # the header row; the P13f criterion skips it with NR>1
        if line.startswith("#"):
            continue
        if not line.strip():
            # A blank line is not a comment. The row's OWN awk criterion would run
            # `test -f ""` on it and exit 1 with nothing on stdout to say why, so it is
            # refused here first, with a message. The last element of split("\n") is the
            # artefact of the trailing newline and is not a line.
            if i != len(lines):
                fatal.append(("BLANK-ROW", f"line {i} is blank; FIGURES.tsv admits a header "
                                           "row, # comment lines and data rows only"))
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            fatal.append(("SHORT-ROW", f"line {i} has {len(parts)} tab-separated field(s), "
                                       f"needs 3 (figure/script/source): {line[:80]!r}"))
            continue
        rows.append({"line": i, "figure": parts[0].strip(), "script": parts[1].strip(),
                     "source": parts[2].strip()})
    return rows, fatal


def matches(row_figure: str, ref_key: str) -> bool:
    if row_figure == SENTINEL:
        return False
    if row_figure == ref_key:
        return True
    return pathlib.PurePosixPath(row_figure).name == pathlib.PurePosixPath(ref_key).name


def measure(papers, manifest_path, pdf_path):
    per_file, refs = [], []
    for p in papers:
        hits = scan(p, ROOT if str(p).startswith(str(ROOT)) else p.parent)
        refs.extend(hits)
        per_file.append({"path": str(p.relative_to(ROOT)) if str(p).startswith(str(ROOT)) else p.name,
                         "sha256": sha256(p), "figure_references": len(hits)})
    n_pdf, how = pdf_image_count(pdf_path) if pdf_path else (0, "skipped")
    return {
        "_": ("P13f. Written by scripts/wt177_figure_guard.py --emit. Do not hand-edit: the "
              "guard re-measures on every run and tests/test_figures_manifest_bites.py holds "
              "this file to what it finds."),
        "guard_version": GUARD_VERSION,
        "manifest": str(manifest_path.relative_to(ROOT)) if str(manifest_path).startswith(str(ROOT)) else str(manifest_path),
        "corpus_source": "PAPERS= in docs/deliverable/build.sh (parsed, not hardcoded)",
        "manuscripts": per_file,
        "figure_references_total": len(refs),
        "figure_references": refs,
        "pdf": {"path": str(pdf_path.relative_to(ROOT)) if pdf_path and str(pdf_path).startswith(str(ROOT)) else None,
                "sha256": sha256(pdf_path) if pdf_path and pdf_path.is_file() else None,
                "image_xobjects": n_pdf, "observed_by": how},
        "patterns": [k for k, _ in PATTERNS],
        "blind_to": [
            "documents outside the PAPERS= list (review docs, ADRs)",
            "figures injected by wt175_md2tex.lua or preamble.tex macros",
            "images inside a compressed /ObjStm when pdfimages is unavailable",
            "vector art drawn with PDF operators rather than an image XObject",
            "whether a listed script actually produces its figure (that is P6's job)",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="P13f figure-manifest guard")
    ap.add_argument("--paper", action="append", default=None,
                    help="override a manuscript path (repeatable); red-proof use only")
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--build-sh", default=None,
                    help="override the file the corpus list is parsed from; red-proof use only")
    ap.add_argument("--no-pdf", action="store_true")
    ap.add_argument("--emit", action="store_true", help="rewrite FIGURES-MEASURED.json")
    ap.add_argument("--json", action="store_true", help="print the measurement, no verdict")
    a = ap.parse_args()

    if a.paper:
        papers, err = [pathlib.Path(p).resolve() for p in a.paper], None
    else:
        papers, err = papers_from_build_sh(
            pathlib.Path(a.build_sh).resolve() if a.build_sh else None)
    if err:
        print(f"FAIL[CORPUS-UNREADABLE] {err}")
        return 1
    missing = [p for p in papers if not p.is_file()]
    if missing:
        print("FAIL[CORPUS-UNREADABLE] manuscript(s) named but absent: "
              + ", ".join(str(p) for p in missing))
        return 1
    if not papers:
        print("FAIL[CORPUS-EMPTY] zero manuscripts in scope — a guard over nothing "
              "reports zero findings and means nothing")
        return 1

    manifest_path = pathlib.Path(a.manifest).resolve() if a.manifest else MANIFEST
    pdf_path = None if a.no_pdf else (pathlib.Path(a.pdf).resolve() if a.pdf else PDF)

    m = measure(papers, manifest_path, pdf_path)
    if a.json:
        print(json.dumps(m, indent=2))
        return 0
    if a.emit:
        RECEIPT.write_text(json.dumps(m, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {RECEIPT.relative_to(ROOT)} "
              f"({m['figure_references_total']} figure reference(s) over {len(papers)} manuscript(s))")
        return 0

    rows, fails = read_manifest(manifest_path)
    refs = m["figure_references"]
    n_pdf = m["pdf"]["image_xobjects"]
    data_rows = [r for r in rows if r["figure"] != SENTINEL]
    sentinels = [r for r in rows if r["figure"] == SENTINEL]

    for r in rows:
        for col, tag in (("script", "ROW-SCRIPT-MISSING"), ("source", "ROW-SOURCE-MISSING")):
            if not (ROOT / r[col]).is_file():
                fails.append((tag, f"line {r['line']}: {col} {r[col]!r} does not exist. "
                                   f"P13f wants a COMMITTED script and COMMITTED numbers; a "
                                   f"row naming neither is a decoration."))

    for ref in refs:
        if not any(matches(r["figure"], ref["key"]) for r in data_rows):
            fails.append(("UNLISTED-FIGURE",
                          f"{ref['file']}:{ref['line']} references {ref['key']!r} "
                          f"({ref['kind']}) and no FIGURES.tsv row names it: {ref['raw']!r}"))

    for r in data_rows:
        if not any(matches(r["figure"], ref["key"]) for ref in refs):
            fails.append(("ORPHAN-ROW",
                          f"line {r['line']}: {r['figure']!r} is listed but no manuscript "
                          f"references it. A row nothing uses is how a manifest rots into "
                          f"a green that means nothing."))

    if sentinels and refs:
        fails.append(("SENTINEL-WITH-FIGURES",
                      f"{SENTINEL} claims the corpus has no figures, and {len(refs)} "
                      f"reference(s) say otherwise. THIS IS THE ROW REOPENING. Delete the "
                      f"sentinel and list the figure -> script -> source."))
    if sentinels and data_rows:
        fails.append(("SENTINEL-WITH-ROWS",
                      f"{SENTINEL} coexists with {len(data_rows)} real row(s); it is a claim "
                      f"that there are none, so it goes the moment the first one lands."))
    if len(sentinels) > 1:
        fails.append(("SENTINEL-DUPLICATED", f"{len(sentinels)} {SENTINEL} rows; expected 1"))
    if not sentinels and not refs and not data_rows:
        fails.append(("SENTINEL-MISSING",
                      f"the corpus has no figures and the manifest has no rows. A header-only "
                      f"FIGURES.tsv closes P13f vacuously and reopens it in silence; the "
                      f"{SENTINEL} row is what keeps the claim on the record."))
    if n_pdf and not data_rows:
        fails.append(("PDF-IMAGE-UNDECLARED",
                      f"the built PDF carries {n_pdf} image XObject(s) that no manuscript "
                      f"references and no FIGURES.tsv row declares — a figure entered "
                      f"through the build, not the prose."))

    print(f"wt177 · P13f figure guard ({GUARD_VERSION})")
    print(f"  corpus      : {len(papers)} manuscript(s), from PAPERS= in build.sh")
    for pf in m["manuscripts"]:
        print(f"                {pf['figure_references']:>3}  {pf['path']}")
    print(f"  references  : {len(refs)}  (patterns: {', '.join(k for k, _ in PATTERNS)})")
    print(f"  pdf images  : {n_pdf}  ({m['pdf']['observed_by']})")
    print(f"  manifest    : {len(data_rows)} figure row(s), {len(sentinels)} sentinel")
    print("  BLIND TO    : " + "; ".join(m["blind_to"]))

    for tag, _ in list(fails):
        if tag not in TAGS:
            fails.append(("UNREGISTERED-TAG", f"{tag!r} is not in TAGS; add it there (and a "
                                              f"probe in redproof_wt177_figures.py) or drop it"))

    if fails:
        print(f"\n{len(fails)} FAILURE(S):")
        for tag, msg in fails:
            print(f"  FAIL[{tag}] {msg}")
        return 1
    print("\nPASS — every figure reference is listed, every listed row exists, and the "
          "zero on the left is a measured zero with its blind spots named.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
