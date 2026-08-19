#!/usr/bin/env python3
"""wealthTensor-95 · red-proof the P13f figure guard.

WHY. A row is not done when it is green; it is done when it has been seen red. P13f's own
criterion is satisfied by a single row whose column 2 happens to exist -- which is a check
that can pass while the manifest is completely inert. `scripts/wt177_figure_guard.py` is
what makes it bite, and a guard nobody has watched fail is a decoration.

`-94`'s fourth trap governs the design of every probe here: *A RED-PROOF CAUGHT BY A
DIFFERENT GUARD THAN THE ONE UNDER TEST PROVES THE WRONG THING, and looks identical to
success.* So each probe

  1. asserts the mutated world is GREEN before the mutation (else the probe proves nothing),
  2. asserts a NON-ZERO exit after it, and
  3. asserts the SPECIFIC FAIL[TAG] it was written to provoke is in the output.

and one probe runs the other way -- a figure that IS properly listed must go GREEN, because
a guard that can only ever fail is not a guard either.

Nothing here touches the real manuscripts. Every probe runs in a fresh temp directory over
COPIES, and the corpus is passed with --paper so the guard never reads docs/papers/.

    python3 scripts/redproof_wt177_figures.py
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
GUARD = ROOT / "scripts" / "wt177_figure_guard.py"
REAL_MANIFEST = ROOT / "docs" / "deliverable" / "FIGURES.tsv"
SENTINEL_ROW = "@zero-figures\tscripts/wt177_figure_guard.py\tdocs/deliverable/FIGURES-MEASURED.json"
HEADER = "figure\tscript\tsource"

# The P13f criterion, verbatim from docs/done-criteria.tsv, with the manifest path made a
# parameter so a probe can point it at a mutated copy. If this drifts from the TSV the
# guard's red-proof is proving something about a check nobody runs -- so it is checked.
CRITERION = (r"""test -f {m} && awk -F'\t' 'NR>1 && $1!~/^#/"""
             r"""{{if(system("test -f " $2)) exit 1; n++}} END{{exit !(n>=1)}}' {m}""")


def guard(papers, manifest, cwd, pdf=None, build_sh=None):
    cmd = [sys.executable, str(GUARD), "--manifest", str(manifest)]
    cmd += (["--pdf", str(pdf)] if pdf else ["--no-pdf"])
    if build_sh:
        cmd += ["--build-sh", str(build_sh)]
    for p in papers:
        cmd += ["--paper", str(p)]
    return subprocess.run(cmd, capture_output=True, text=True, cwd=str(cwd))


def criterion(manifest):
    return subprocess.run(["bash", "-c", CRITERION.format(m=str(manifest))],
                          capture_output=True, text=True, cwd=str(ROOT)).returncode


def tags(proc):
    return set(re.findall(r"FAIL\[([A-Z-]+)\]", proc.stdout + proc.stderr))


class Bench:
    """A throwaway world: two manuscript copies and a manifest, all writable."""

    def __init__(self, tmp):
        self.dir = pathlib.Path(tmp)
        self.papers = []
        for name in ("paper-I.md", "paper-II.md"):
            p = self.dir / name
            p.write_text("# a manuscript with no figures\n\nProse, tables, equations.\n",
                         encoding="utf-8")
            self.papers.append(p)
        self.manifest = self.dir / "FIGURES.tsv"
        self.manifest.write_text(HEADER + "\n" + SENTINEL_ROW + "\n", encoding="utf-8")

        self.pdf = None
        self.build_sh = None

    def run(self):
        return guard(self.papers, self.manifest, ROOT, pdf=self.pdf, build_sh=self.build_sh)


def probe(name, mutate, expect_tag, expect_rc_nonzero=True):
    with tempfile.TemporaryDirectory() as tmp:
        b = Bench(tmp)
        before = b.run()
        if before.returncode != 0:
            return (name, "INVALID", f"baseline was already red ({tags(before) or 'no tag'}) — "
                                     f"the probe would prove nothing\n{before.stdout[-1500:]}")
        mutate(b)
        after = b.run()
        got = tags(after)
        if expect_rc_nonzero and after.returncode == 0:
            return (name, "WEAK", f"the mutation left the guard GREEN; expected "
                                  f"FAIL[{expect_tag}]\n{after.stdout[-1500:]}")
        if not expect_rc_nonzero:
            if after.returncode != 0:
                return (name, "WEAK", f"expected GREEN, got rc={after.returncode} {got}"
                                      f"\n{after.stdout[-1500:]}")
            return (name, "PROVEN", "green when the figure is properly listed")
        if expect_tag not in got:
            return (name, "WRONG-GUARD", f"guard went red, but on {sorted(got)} — not the "
                                         f"FAIL[{expect_tag}] under test. -94's fourth trap: a "
                                         f"red-proof caught by a different check proves the "
                                         f"wrong thing.\n{after.stdout[-1500:]}")
        return (name, "PROVEN", f"FAIL[{expect_tag}] fired (rc={after.returncode})")


# ---- the probes ------------------------------------------------------------------------

def m_unlisted(b):
    """An image pasted MID-SENTENCE — the exact reference the -93/-94 sweep's `^!\\[`
    anchor walks straight past."""
    p = b.papers[0]
    p.write_text(p.read_text() + "\nAs shown in ![the concentration path](figs/conc.png) "
                                 "the ladder holds.\n", encoding="utf-8")


def m_sentinel_with_figures(b):
    """The silent reopen: someone adds a figure AND dutifully lists it, but leaves the
    sentinel behind. The manifest now says both 'there are no figures' and 'here is one'."""
    p = b.papers[1]
    p.write_text(p.read_text() + "\n![lifetime coverage](figs/cov.png)\n", encoding="utf-8")
    b.manifest.write_text(
        HEADER + "\n" + SENTINEL_ROW + "\n"
        + "figs/cov.png\tscripts/source001_lifetime_coverage.py\tdocs/done-criteria.tsv\n",
        encoding="utf-8")


def m_row_script_missing(b):
    p = b.papers[0]
    p.write_text(p.read_text() + "\n![a chart](figs/x.png)\n", encoding="utf-8")
    b.manifest.write_text(HEADER + "\nfigs/x.png\tscripts/no_such_script.py\t"
                                   "docs/done-criteria.tsv\n", encoding="utf-8")


def m_sentinel_removed(b):
    b.manifest.write_text(HEADER + "\n", encoding="utf-8")


def m_orphan_row(b):
    b.manifest.write_text(HEADER + "\nfigs/ghost.png\tscripts/wt177_figure_guard.py\t"
                                   "docs/done-criteria.tsv\n", encoding="utf-8")


def m_properly_listed(b):
    p = b.papers[0]
    p.write_text(p.read_text() + "\n![the concentration path](figs/conc.png)\n", encoding="utf-8")
    b.manifest.write_text(HEADER + "\nfigs/conc.png\tscripts/source001_concentration.py\t"
                                   "docs/done-criteria.tsv\n", encoding="utf-8")


def m_row_source_missing(b):
    """The row's own criterion only tests column 2. A row whose SOURCE is missing sails
    through it — 'committed numbers' is half of P13f and the awk never looks."""
    p = b.papers[0]
    p.write_text(p.read_text() + "\n![a chart](figs/x.png)\n", encoding="utf-8")
    b.manifest.write_text(HEADER + "\nfigs/x.png\tscripts/wt177_figure_guard.py\t"
                                   "docs/no-such-source.tsv\n", encoding="utf-8")


def m_blank_row(b):
    """A blank line makes the criterion run `test -f \"\"` and exit 1 with nothing on
    stdout. The guard has to say why first, or the next session debugs a silent awk."""
    b.manifest.write_text(HEADER + "\n\n" + SENTINEL_ROW + "\n", encoding="utf-8")


def m_short_row(b):
    b.manifest.write_text(HEADER + "\nfigs/x.png scripts/wt177_figure_guard.py\n",
                          encoding="utf-8")


def m_manifest_missing(b):
    b.manifest.unlink()


def m_sentinel_duplicated(b):
    b.manifest.write_text(HEADER + "\n" + SENTINEL_ROW + "\n" + SENTINEL_ROW + "\n",
                          encoding="utf-8")


def m_sentinel_with_rows(b):
    """A real row lands, the figure reference is there, and the sentinel stays. Distinct
    from sentinel-with-figures: this is the manifest contradicting ITSELF."""
    b.manifest.write_text(HEADER + "\n" + SENTINEL_ROW + "\nfigs/ghost.png\t"
                          "scripts/wt177_figure_guard.py\tdocs/done-criteria.tsv\n",
                          encoding="utf-8")


def m_pdf_image_undeclared(b):
    """A figure that entered through the BUILD, not the prose — the hole the manuscript
    sweep is structurally incapable of seeing on its own."""
    pdf = b.dir / "fake.pdf"
    pdf.write_bytes(b"%PDF-1.7\n1 0 obj\n<< /Type /XObject /Subtype /Image /Width 8 "
                    b"/Height 8 >>\nstream\nendstream\nendobj\n%%EOF\n")
    b.pdf = pdf


def m_corpus_unreadable(b):
    bs = b.dir / "build.sh"
    bs.write_text("#!/bin/bash\n# a build.sh with no PAPERS block\n", encoding="utf-8")
    b.build_sh = bs
    b.papers = []          # force the build.sh path


def m_corpus_empty(b):
    bs = b.dir / "build.sh"
    bs.write_text('#!/bin/bash\nPAPERS="\n   \n"\n', encoding="utf-8")
    b.build_sh = bs
    b.papers = []


PROBES = [
    ("unlisted-figure", m_unlisted, "UNLISTED-FIGURE", True),
    ("sentinel-with-figures", m_sentinel_with_figures, "SENTINEL-WITH-FIGURES", True),
    ("row-script-missing", m_row_script_missing, "ROW-SCRIPT-MISSING", True),
    ("sentinel-removed", m_sentinel_removed, "SENTINEL-MISSING", True),
    ("orphan-row", m_orphan_row, "ORPHAN-ROW", True),
    ("row-source-missing", m_row_source_missing, "ROW-SOURCE-MISSING", True),
    ("blank-row", m_blank_row, "BLANK-ROW", True),
    ("short-row", m_short_row, "SHORT-ROW", True),
    ("manifest-missing", m_manifest_missing, "MANIFEST-MISSING", True),
    ("sentinel-duplicated", m_sentinel_duplicated, "SENTINEL-DUPLICATED", True),
    ("sentinel-with-rows", m_sentinel_with_rows, "SENTINEL-WITH-ROWS", True),
    ("pdf-image-undeclared", m_pdf_image_undeclared, "PDF-IMAGE-UNDECLARED", True),
    ("corpus-unreadable", m_corpus_unreadable, "CORPUS-UNREADABLE", True),
    ("corpus-empty", m_corpus_empty, "CORPUS-EMPTY", True),
    ("green-when-listed", m_properly_listed, None, False),
]


def every_guard_tag_has_a_probe():
    """NO SILENT CAPS. A check the guard can emit but nobody has provoked has never been
    seen red — which is the whole complaint this file exists to answer. The tag list is read
    from the guard's own TAGS registry rather than scraped out of its source text: the first
    version of this check used a regex, found 9 of 14 tags, and reported full coverage —
    a check that could not see what it claimed to count, which is the exact failure `-94`
    spent a session naming. Add a check to the guard without a probe here and this goes red."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import wt177_figure_guard as g
    emitted = set(g.TAGS) - {"UNREGISTERED-TAG"}   # provoking that one needs a broken guard
    probed = {tag for _, _, tag, _ in PROBES if tag}
    missing = sorted(emitted - probed)
    stray = sorted(probed - emitted)
    detail = f"all {len(emitted)} tag(s) in the guard's TAGS registry have a probe"
    if missing:
        detail = f"never seen red: {', '.join(missing)} — write the probe or delete the check"
    elif stray:
        detail = f"probes for tags the guard cannot emit: {', '.join(stray)}"
    return ("coverage:every-guard-tag-has-a-probe",
            "PROVEN" if not (missing or stray) else "WEAK", detail)


def criterion_probes():
    """The row's OWN awk, red-proofed. The guard is the interesting half of P13f, but the
    criterion is what the board runs, and a criterion nobody has seen red is a decoration
    for exactly the same reason."""
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        d = pathlib.Path(tmp)
        good = d / "good.tsv"
        good.write_text(HEADER + "\n" + SENTINEL_ROW + "\n", encoding="utf-8")
        out.append(("criterion:green-on-the-real-shape", "PROVEN" if criterion(good) == 0
                    else "WEAK", f"rc={criterion(good)} (expected 0)"))
        header_only = d / "header.tsv"
        header_only.write_text(HEADER + "\n", encoding="utf-8")
        rc = criterion(header_only)
        out.append(("criterion:header-only-file", "PROVEN" if rc != 0 else "WEAK",
                    f"rc={rc} (expected non-zero — n>=1 is what kills the empty file)"))
        bad = d / "bad.tsv"
        bad.write_text(HEADER + "\nfigs/x.png\tscripts/no_such_script.py\tdocs/done-criteria.tsv\n",
                       encoding="utf-8")
        rc = criterion(bad)
        out.append(("criterion:row-script-missing", "PROVEN" if rc != 0 else "WEAK",
                    f"rc={rc} (expected non-zero)"))
        absent = d / "not-there.tsv"
        rc = criterion(absent)
        out.append(("criterion:manifest-absent", "PROVEN" if rc != 0 else "WEAK",
                    f"rc={rc} (expected non-zero)"))
    return out


def criterion_is_the_committed_one():
    """The criterion string above must still be the one in done-criteria.tsv. A red-proof
    of a check that has since been edited proves something about a check nobody runs."""
    tsv = (ROOT / "docs" / "done-criteria.tsv").read_text(encoding="utf-8")
    row = [l for l in tsv.split("\n") if l.startswith("P13f\t")]
    if not row:
        return ("criterion:matches-done-criteria", "WEAK", "no P13f row in done-criteria.tsv")
    committed = row[0].split("\t")[3]
    mine = CRITERION.format(m="docs/deliverable/FIGURES.tsv")
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    ok = norm(mine) in norm(committed)
    return ("criterion:matches-done-criteria", "PROVEN" if ok else "WEAK",
            "the probed criterion is the committed one" if ok else
            f"DRIFT.\n  committed: {norm(committed)}\n  probed   : {norm(mine)}")


def main() -> int:
    results = [probe(*p) for p in PROBES]
    results.append(every_guard_tag_has_a_probe())
    results.append(criterion_is_the_committed_one())
    results += criterion_probes()

    width = max(len(r[0]) for r in results)
    print("wt177 red-proof · P13f figure manifest\n")
    for name, verdict, detail in results:
        green_probe = name in ("green-when-listed", "criterion:green-on-the-real-shape") \
            or name.startswith("coverage:") or name.endswith("matches-done-criteria")
        mark = {"PROVEN": "  seen green" if green_probe else "  seen red  ",
                "WEAK": "  WEAK       ", "WRONG-GUARD": "  WRONG      ",
                "INVALID": "  INVALID    "}[verdict]
        print(f"{mark}  {name.ljust(width)}  {detail.splitlines()[0] if detail else ''}")
        if verdict != "PROVEN":
            for line in detail.split("\n")[1:]:
                print(f"                {line}")
    bad = [r for r in results if r[1] != "PROVEN"]
    print(f"\n{len(results) - len(bad)}/{len(results)} probes proven.")
    if bad:
        print("A probe that is not PROVEN is the finding, not the pass.")
        return 1
    print("Every failure the P13f guard can report, and every way its criterion can fail, "
          "has been provoked and observed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
