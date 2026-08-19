#!/usr/bin/env python3
"""docs/deliverable/wt176_layout_manifest.py

P13e -- THE LAYOUT IS REPRODUCIBLE, PROVED NOT PROMISED.

What this records, and why each field is the field it is:

  page_count          A substituted font moves the metrics, moved metrics move the reflow,
                      a moved reflow moves a page boundary. The count is the cheapest
                      detector of the largest class of drift.
  pages[].sha256      ...but a count alone is blind to two compensating shifts, and to any
                      reflow that moves text between pages without changing how many there
                      are. Hashing the EXTRACTED TEXT OF EACH PAGE fixes which words land
                      on which sheet. That is the property the deliverable actually sells.
  fonts               The sixteen vendored faces by sha256. preflight.sh already refuses to
                      build on a mismatch; recording them here means the MANIFEST can also
                      say which fonts it is a statement about, rather than assuming.
  manuscripts         The four sources by sha256, so a manifest can never silently describe
                      a document built from different prose.
  pins                Engine, TeX Live year, pandoc, and the extractor -- because the hash
                      is a joint statement about the document AND the tool that read it.

THE EXTRACTOR IS PART OF THE MEASUREMENT. A pypdf upgrade can change extracted text
without the PDF changing at all, which would look exactly like layout drift. The version is
pinned here and asserted on verify, so that failure reports itself as what it is.

  --emit     write LAYOUT-MANIFEST.json for the PDF in this directory
  --verify   compare a freshly built PDF against the committed manifest (verify-layout.sh)
  --print K  print one value
"""
import argparse, hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
MANIFEST = os.path.join(HERE, "LAYOUT-MANIFEST.json")
PDF = os.path.join(HERE, "wealth-tensor-capture.pdf")
PAPERS = [
    "docs/papers/paper-I-price-formation/paper-I.md",
    "docs/papers/paper-II-redistribution/paper-II.md",
    "docs/papers/paper-III-dual-tensor/paper-III.md",
    "docs/papers/paper-IV-composition/paper-IV.md",
]


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def page_hashes(pdf_path):
    """Per-page sha256 of the extracted text. The unit of the claim is the PAGE."""
    import pypdf
    r = pypdf.PdfReader(pdf_path)
    out = []
    for i, pg in enumerate(r.pages, 1):
        t = pg.extract_text() or ""
        out.append({"page": i, "chars": len(t),
                    "sha256": hashlib.sha256(t.encode("utf-8")).hexdigest()})
    return out


def build_manifest(commit, pandoc_ver, pdf_path):
    import pypdf
    fonts_dir = os.path.join(HERE, "fonts")
    fonts = {fn: sha256_file(os.path.join(fonts_dir, fn))
             for fn in sorted(os.listdir(fonts_dir)) if fn.endswith(".otf")}
    tl = subprocess.run(["lualatex", "--version"], capture_output=True, text=True).stdout
    tl_year = next((w for w in tl.replace(")", " ").split() if w.isdigit() and len(w) == 4), "")
    ph = page_hashes(pdf_path)
    return {
        "_": "P13e. Written by wt176_layout_manifest.py --emit. Do not hand-edit: "
             "verify-layout.sh rebuilds from source_commit in a clean worktree and holds "
             "the PDF to every value below.",
        "source_commit": commit,
        "source_commit_short": commit[:12],
        "commit_date": subprocess.run(
            ["git", "-C", REPO, "show", "-s", "--format=%cs", commit],
            capture_output=True, text=True).stdout.strip(),
        "pdf": os.path.basename(pdf_path),
        "pdf_sha256": sha256_file(pdf_path),
        "page_count": len(ph),
        "pages": ph,
        "pins": {
            "engine": "lualatex",
            "texlive_year": tl_year,
            "pandoc": pandoc_ver,
            "text_extractor": "pypdf",
            "text_extractor_version": pypdf.__version__,
        },
        "silent_wrongness": {
            "overfull_hboxes": 0,
            "missing_characters": 0,
            "_": "Both are LaTeX WARNINGS and both are fatal in build.sh. Zero here is an "
                 "assertion the build enforced, not an observation somebody made.",
        },
        "bibtex": {
            "ran": False,
            "_": "MEASURED at wealthTensor-94: the four manuscripts contain zero \\cite "
                 "commands and the repository contains no .bib file -- each paper carries a "
                 "hand-written References section. RECIPE step 16's natbib/chicago pair is "
                 "loaded as specified and compiles clean; bibtex has nothing to process on "
                 "this corpus. Recorded rather than worked around: the day a \\cite appears, "
                 "this field is how a successor knows the leg was never exercised.",
        },
        "fonts": fonts,
        "manuscripts": {p: sha256_file(os.path.join(REPO, p)) for p in PAPERS},
    }


def cmp_verify(fresh_pdf):
    m = json.load(open(MANIFEST))
    fails = []
    import pypdf
    if pypdf.__version__ != m["pins"]["text_extractor_version"]:
        fails.append("pypdf %s, manifest measured with %s -- the extractor is part of the "
                     "measurement" % (pypdf.__version__, m["pins"]["text_extractor_version"]))
    ph = page_hashes(fresh_pdf)
    if len(ph) != m["page_count"]:
        fails.append("PAGE COUNT %d, manifest says %d" % (len(ph), m["page_count"]))
    n = min(len(ph), m["page_count"])
    moved = [i + 1 for i in range(n) if ph[i]["sha256"] != m["pages"][i]["sha256"]]
    if moved:
        fails.append("PER-PAGE TEXT HASH differs on %d page(s): %s%s"
                     % (len(moved), moved[:12], " ..." if len(moved) > 12 else ""))
    for p, want in m["manuscripts"].items():
        got = sha256_file(os.path.join(REPO, p))
        if got != want:
            fails.append("manuscript changed since the capture: %s" % p)
    return m, ph, fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true")
    ap.add_argument("--verify", metavar="PDF", nargs="?", const=PDF)
    ap.add_argument("--print", dest="key")
    a = ap.parse_args()

    if a.emit:
        commit = os.environ.get("WT_COMMIT") or subprocess.run(
            ["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        m = build_manifest(commit, os.environ.get("WT_PANDOC", ""), PDF)
        with open(MANIFEST, "w") as f:
            json.dump(m, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print("  ok      LAYOUT-MANIFEST.json — %d pages, source_commit %s"
              % (m["page_count"], m["source_commit_short"]))
        return 0

    if a.verify:
        m, ph, fails = cmp_verify(a.verify)
        print("  manifest : %d pages, source_commit %s" % (m["page_count"], m["source_commit_short"]))
        print("  rebuild  : %d pages" % len(ph))
        if fails:
            print("\nLAYOUT DID NOT REPRODUCE:")
            for f in fails:
                print("   FAIL  " + f)
            return 1
        print("  ok       page count and all %d per-page text hashes reproduce" % len(ph))
        return 0

    if a.key:
        m = json.load(open(MANIFEST))
        cur = m
        for part in a.key.split("."):
            cur = cur[int(part)] if part.isdigit() else cur[part]
        print(cur)
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
