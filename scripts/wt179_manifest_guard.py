#!/usr/bin/env python3
"""wealthTensor-97 -- the CHEAP guard on docs/deliverable/LAYOUT-MANIFEST.json.

WHY THIS EXISTS. P13e's entire claim rests on that manifest, and until now the only things
that could notice a hand-edit were `verify-layout.sh`, `redproof-layout.sh` and
`wt173 --verify` -- ALL THREE of which need lualatex, pandoc and a clean git worktree. So
CI could not check it. A fresh clone could not check it. The cloud container could not check
it. Any session that had not run preflight could not check it. A file that nothing cheap can
check is a file that drifts, and it drifts in the direction of whoever last edited it by hand.

This runs in well under a second with the Python standard library and `git`. It cannot
verify that the manifest describes reality -- only a rebuild can do that, which is exactly
what `verify-layout.sh` is for and why this does not replace it. What it CAN do is hold the
manifest to ITSELF, to the two registries beside it (`fonts/FONTS.tsv`, the manuscripts on
disk), to the committed PDF's bytes, and to the commit it names. Every one of those is an
internal consistency the strong guard would also catch -- eight minutes and a TeX Live
installation later.

THE SCOPE IS DECLARED, NOT DISCOVERED. `-95` wrote a coverage check that found what happened
to be in front of it, reported FULL COVERAGE over nine of fourteen, and was believed. The
inverse discipline is the whole architecture here: `SCHEMA` names every key this manifest
may contain and `check_all` refuses anything else (UNKNOWN-KEY), so a key added to the
manifest without a check added here turns this RED rather than sailing past unexamined.
Iterating whatever keys are present would have made that key invisible; declaring the shape
makes its arrival an event.

TAGS ARE THE INTERFACE. Every finding is prefixed with a tag from `TAGS`, `_tag()` refuses
to emit one that is not declared there, and `scripts/redproof_wt179_manifest.py` imports
`TAGS` to prove each one has been watched to fire. An exit code says only that something
went wrong; the tag says WHICH check bit, which is the difference between a red-proof that
proves the guard works and one that proves the temp directory was missing.

USAGE
    python3 scripts/wt179_manifest_guard.py           # human; exit 0 clean, 1 with findings
    python3 scripts/wt179_manifest_guard.py --json    # machine
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DELIVERABLE = ROOT / "docs" / "deliverable"
MANIFEST = DELIVERABLE / "LAYOUT-MANIFEST.json"
FONTS_TSV = DELIVERABLE / "fonts" / "FONTS.tsv"
PAPERS = ROOT / "docs" / "papers"

# --------------------------------------------------------------------------- declarations
# Every failure this guard can report. The red-proof imports this and holds itself to it in
# both directions: a tag no probe provokes prints WEAK, a probe naming a tag that is not
# here is an error. Adding a check without a probe goes red BY CONSTRUCTION.
TAGS = {
    "MANIFEST-MISSING": "LAYOUT-MANIFEST.json is not on disk",
    "MANIFEST-UNPARSEABLE": "LAYOUT-MANIFEST.json is not valid JSON",
    "MISSING-KEY": "a key the schema declares is absent",
    "UNKNOWN-KEY": "a key the schema does not declare is present",
    "BAD-TYPE": "a declared key carries the wrong type",
    "PAGE-COUNT-DISAGREES": "page_count does not equal len(pages)",
    "PAGE-ENTRY-SHAPE": "a page entry's keys are not exactly page/chars/sha256",
    "PAGE-NUMBERING": "pages are not numbered 1..page_count in order",
    "BAD-SHA": "a sha256 is not 64 lowercase hex characters",
    "BAD-CHARS": "a page's chars is not a non-negative integer",
    "FONTS-TSV-UNREADABLE": "fonts/FONTS.tsv is missing or has no data rows",
    "FONT-NOT-IN-TSV": "the manifest lists a font FONTS.tsv does not",
    "FONT-MISSING-FROM-MANIFEST": "FONTS.tsv lists a font the manifest does not",
    "FONT-SHA-DISAGREES": "a font's sha differs between the manifest and FONTS.tsv",
    "MANUSCRIPT-NOT-ON-DISK": "the manifest lists a manuscript that is not on disk",
    "MANUSCRIPT-MISSING-FROM-MANIFEST": "a manuscript on disk is not in the manifest",
    "BAD-COMMIT-SHA": "source_commit is not a 40-character lowercase hex sha",
    "COMMIT-SHORT-DISAGREES": "source_commit_short is not a prefix of source_commit",
    "COMMIT-MISSING": "source_commit is not a commit object in this clone",
    "NOT-A-GIT-CLONE": "the tree under test is not a git clone, so the commit checks cannot run",
    "COMMIT-DATE-DISAGREES": "commit_date is not the commit date of source_commit",
    "GIT-UNAVAILABLE": "git could not be run, so the commit checks did not happen",
    "PDF-MISSING": "the captured PDF the manifest names is not on disk",
    "PDF-SHA-DISAGREES": "the captured PDF's bytes do not hash to pdf_sha256",
    "SILENT-WRONGNESS-NONZERO": "a silent-wrongness counter the build treats as fatal is not zero",
    "UNREGISTERED-TAG": "the guard tried to emit a tag TAGS does not declare",
}

# The manifest's declared shape. Anything present and not named here is UNKNOWN-KEY;
# anything named here and absent is MISSING-KEY. This is the anti-drift surface: the file
# cannot grow a field in silence.
SCHEMA = {
    "_": str,
    "source_commit": str,
    "source_commit_short": str,
    "commit_date": str,
    "pdf": str,
    "pdf_sha256": str,
    "page_count": int,
    "pages": list,
    "pins": dict,
    "silent_wrongness": dict,
    "bibtex": dict,
    "fonts": dict,
    "manuscripts": dict,
}
PIN_KEYS = ("engine", "texlive_year", "pandoc", "text_extractor", "text_extractor_version")
SILENT_KEYS = ("overfull_hboxes", "missing_characters", "_")
SILENT_COUNTERS = ("overfull_hboxes", "missing_characters")
BIBTEX_KEYS = ("ran", "_")
PAGE_KEYS = frozenset({"page", "chars", "sha256"})

SHA256_RE = re.compile(r"\A[0-9a-f]{64}\Z")
COMMIT_RE = re.compile(r"\A[0-9a-f]{40}\Z")


def _tag(tag: str, message: str) -> str:
    """Every finding goes through here so an undeclared tag cannot escape unnoticed."""
    if tag not in TAGS:
        return "UNREGISTERED-TAG %s (tried to report: %s)" % (tag, message)
    return "%s %s" % (tag, message)


# --------------------------------------------------------------------------- loading
def load(path: Path):
    """(manifest_or_None, findings). A file that will not parse ends the run early --
    every later check would be reporting on a dict that does not exist."""
    if not Path(path).is_file():
        return None, [_tag("MANIFEST-MISSING", "%s is not on disk" % path)]
    try:
        return json.loads(Path(path).read_text(encoding="utf-8")), []
    except (ValueError, UnicodeDecodeError) as exc:
        return None, [_tag("MANIFEST-UNPARSEABLE", "%s: %s" % (path, exc))]


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read_fonts_tsv(path: Path):
    """(name -> sha, findings). The TSV is `file<TAB>package<TAB>sha256<TAB>path<TAB>bytes`
    with `#` comments and one header row."""
    if not Path(path).is_file():
        return {}, [_tag("FONTS-TSV-UNREADABLE", "%s is not on disk" % path)]
    rows = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cells = line.split("\t")
        if len(cells) < 3 or cells[0] == "file":
            continue
        rows[cells[0]] = cells[2]
    if not rows:
        return {}, [_tag("FONTS-TSV-UNREADABLE", "%s carries no data rows" % path)]
    return rows, []


# --------------------------------------------------------------------------- the checks
# Each returns a list of findings and is counted, so "N checks run" is a real number and a
# deleted check is visible in the claim the handoff registers.
def check_shape(m):
    out = []
    for key, want in SCHEMA.items():
        if key not in m:
            out.append(_tag("MISSING-KEY", "the manifest has no %r" % key))
        elif not isinstance(m[key], want) or (want is int and isinstance(m[key], bool)):
            out.append(_tag("BAD-TYPE", "%r is %s, the schema declares %s"
                            % (key, type(m[key]).__name__, want.__name__)))
    for key in m:
        if key not in SCHEMA:
            out.append(_tag("UNKNOWN-KEY", "%r is in the manifest and not in this guard's "
                            "SCHEMA. Add the check, then add the key." % key))
    return out


def check_nested_shape(m):
    """pins / silent_wrongness / bibtex are held to their key sets by the same rule."""
    out = []
    for block, keys in (("pins", PIN_KEYS), ("silent_wrongness", SILENT_KEYS),
                        ("bibtex", BIBTEX_KEYS)):
        sub = m.get(block)
        if not isinstance(sub, dict):
            continue                      # already reported by check_shape
        for key in keys:
            if key not in sub:
                out.append(_tag("MISSING-KEY", "%s has no %r" % (block, key)))
        for key in sub:
            if key not in keys:
                out.append(_tag("UNKNOWN-KEY", "%s carries %r, which this guard does not "
                                "declare" % (block, key)))
    pins = m.get("pins")
    if isinstance(pins, dict):
        for key in PIN_KEYS:
            if key in pins and not (isinstance(pins[key], str) and pins[key].strip()):
                out.append(_tag("BAD-TYPE", "pins.%s is not a non-empty string" % key))
    bib = m.get("bibtex")
    if isinstance(bib, dict) and "ran" in bib and not isinstance(bib["ran"], bool):
        out.append(_tag("BAD-TYPE", "bibtex.ran is not a boolean"))
    return out


def check_page_count(m):
    pc, pages = m.get("page_count"), m.get("pages")
    if not isinstance(pc, int) or isinstance(pc, bool) or not isinstance(pages, list):
        return []                          # already reported by check_shape
    if pc != len(pages):
        return [_tag("PAGE-COUNT-DISAGREES",
                     "page_count is %d and pages carries %d entr%s"
                     % (pc, len(pages), "y" if len(pages) == 1 else "ies"))]
    return []


def check_page_entries(m):
    """Shape, numbering, hash form and char counts -- the per-page half of the at-bat."""
    out, pages = [], m.get("pages")
    if not isinstance(pages, list):
        return out
    for i, entry in enumerate(pages, start=1):
        where = "pages[%d]" % (i - 1)
        if not isinstance(entry, dict) or set(entry) != PAGE_KEYS:
            out.append(_tag("PAGE-ENTRY-SHAPE", "%s has keys %s, wanted exactly %s"
                            % (where, sorted(entry) if isinstance(entry, dict)
                               else type(entry).__name__, sorted(PAGE_KEYS))))
            continue
        if entry["page"] != i:
            out.append(_tag("PAGE-NUMBERING", "%s says page %r; pages must run 1..page_count "
                            "in order" % (where, entry["page"])))
        if not (isinstance(entry["sha256"], str) and SHA256_RE.match(entry["sha256"])):
            out.append(_tag("BAD-SHA", "%s.sha256 is not 64 lowercase hex: %r"
                            % (where, entry["sha256"])))
        if (not isinstance(entry["chars"], int) or isinstance(entry["chars"], bool)
                or entry["chars"] < 0):
            out.append(_tag("BAD-CHARS", "%s.chars is %r, wanted a non-negative integer"
                            % (where, entry["chars"])))
    return out


def check_scalar_shas(m):
    out = []
    val = m.get("pdf_sha256")
    if val is not None and not (isinstance(val, str) and SHA256_RE.match(val)):
        out.append(_tag("BAD-SHA", "pdf_sha256 is not 64 lowercase hex: %r" % val))
    for block in ("fonts", "manuscripts"):
        sub = m.get(block)
        if not isinstance(sub, dict):
            continue
        for name, sha in sub.items():
            if not (isinstance(sha, str) and SHA256_RE.match(sha)):
                out.append(_tag("BAD-SHA", "%s[%r] is not 64 lowercase hex: %r"
                                % (block, name, sha)))
    return out


def check_fonts(m, fonts_tsv):
    """Row for row against FONTS.tsv, in both directions, shas included."""
    tsv, out = read_fonts_tsv(fonts_tsv)
    fonts = m.get("fonts")
    if not isinstance(fonts, dict) or not tsv:
        return out
    for name in sorted(set(fonts) - set(tsv)):
        out.append(_tag("FONT-NOT-IN-TSV", "the manifest lists %r; FONTS.tsv does not. A "
                        "font that is not in the TSV is not vendored or not checksummed."
                        % name))
    for name in sorted(set(tsv) - set(fonts)):
        out.append(_tag("FONT-MISSING-FROM-MANIFEST",
                        "FONTS.tsv lists %r and the manifest does not" % name))
    for name in sorted(set(fonts) & set(tsv)):
        if fonts[name] != tsv[name]:
            out.append(_tag("FONT-SHA-DISAGREES", "%s: manifest %s, FONTS.tsv %s"
                            % (name, fonts[name][:12], tsv[name][:12])))
    return out


def check_manuscripts(m, root, papers):
    """Exactly the manuscripts on disk -- both directions, so neither a deletion nor an
    addition can pass. A new paper turns this red until the capture is regenerated, which
    is the correct answer: the manifest describes a PDF that does not contain it."""
    out = []
    listed = m.get("manuscripts")
    if not isinstance(listed, dict):
        return out
    on_disk = {str(p.relative_to(root)) for p in sorted(Path(papers).glob("*/paper-*.md"))}
    for path in sorted(set(listed) - on_disk):
        out.append(_tag("MANUSCRIPT-NOT-ON-DISK",
                        "the manifest lists %s and it is not there" % path))
    for path in sorted(on_disk - set(listed)):
        out.append(_tag("MANUSCRIPT-MISSING-FROM-MANIFEST",
                        "%s is on disk and the manifest does not list it" % path))
    return out


def check_commit(m, git_root):
    """The capture commit must be a real commit object HERE, and carry the date claimed."""
    out = []
    sha, short = m.get("source_commit"), m.get("source_commit_short")
    if not (isinstance(sha, str) and COMMIT_RE.match(sha)):
        return [_tag("BAD-COMMIT-SHA", "source_commit is %r" % sha)]
    if not (isinstance(short, str) and short and sha.startswith(short)):
        out.append(_tag("COMMIT-SHORT-DISAGREES",
                        "source_commit_short %r is not a prefix of %s" % (short, sha)))
    # One spawn does both jobs: `^{commit}` makes this fail for a sha that is absent or is
    # not a commit, and the format prints the date when it is there.
    try:
        seen = subprocess.run(["git", "-C", str(git_root), "show", "-s", "--format=%cs",
                               sha + "^{commit}"], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as exc:
        return out + [_tag("GIT-UNAVAILABLE", "the commit checks did not run: %s" % exc)]
    if seen.returncode != 0:
        # WHICH failure is this? `-95` paid a session for a red whose text nobody read, and
        # the standing container trap in this repo's handoff is that a staged tarball has no
        # `.git`, so EVERY git-shelling check goes red there for a reason that is not drift.
        # Say so in the tag rather than making the next reader diff hashes for ten minutes.
        inside = subprocess.run(["git", "-C", str(git_root), "rev-parse", "--git-dir"],
                                capture_output=True, text=True, timeout=30)
        if inside.returncode != 0:
            return out + [_tag("NOT-A-GIT-CLONE", "%s is not a git clone, so the capture commit "
                               "cannot be checked here. This is the expected result in a staged "
                               "tarball; it is NOT evidence that the manifest drifted." % git_root)]
        return out + [_tag("COMMIT-MISSING", "%s is not a commit object in %s -- the capture "
                           "names a commit this clone has never seen" % (sha, git_root))]
    got = seen.stdout.strip()
    if got and got != m.get("commit_date"):
        out.append(_tag("COMMIT-DATE-DISAGREES", "the manifest says %r and %s is dated %s"
                        % (m.get("commit_date"), sha[:12], got)))
    return out


def check_pdf(m, deliverable):
    """The one check that reaches the deliverable's actual bytes. It is cheap -- half a
    megabyte -- and it is the strongest thing here: a manifest that describes a different
    PDF than the one committed beside it is caught in milliseconds instead of in a rebuild."""
    name, want = m.get("pdf"), m.get("pdf_sha256")
    if not isinstance(name, str) or not name:
        return []
    path = Path(deliverable) / name
    if not path.is_file():
        return [_tag("PDF-MISSING", "the manifest names %s and it is not in %s"
                     % (name, deliverable))]
    if isinstance(want, str) and SHA256_RE.match(want):
        got = _sha256_file(path)
        if got != want:
            return [_tag("PDF-SHA-DISAGREES", "%s hashes to %s and the manifest claims %s"
                         % (name, got[:16], want[:16]))]
    return []


def check_silent_wrongness(m):
    """The manifest's own note calls these `an assertion the build enforced`. An assertion
    is checkable; this is where it gets checked."""
    out = []
    sub = m.get("silent_wrongness")
    if not isinstance(sub, dict):
        return out
    for key in SILENT_COUNTERS:
        val = sub.get(key)
        if isinstance(val, bool) or not isinstance(val, int):
            out.append(_tag("BAD-TYPE", "silent_wrongness.%s is %r, wanted an integer"
                            % (key, val)))
        elif val != 0:
            out.append(_tag("SILENT-WRONGNESS-NONZERO",
                            "silent_wrongness.%s is %d. build.sh treats it as fatal, so a "
                            "committed manifest cannot honestly carry it." % (key, val)))
    return out


CHECKS = (
    ("shape", lambda c: check_shape(c["m"])),
    ("nested-shape", lambda c: check_nested_shape(c["m"])),
    ("page-count", lambda c: check_page_count(c["m"])),
    ("page-entries", lambda c: check_page_entries(c["m"])),
    ("scalar-shas", lambda c: check_scalar_shas(c["m"])),
    ("fonts", lambda c: check_fonts(c["m"], c["fonts_tsv"])),
    ("manuscripts", lambda c: check_manuscripts(c["m"], c["root"], c["papers"])),
    ("commit", lambda c: check_commit(c["m"], c["git_root"])),
    ("pdf", lambda c: check_pdf(c["m"], c["deliverable"])),
    ("silent-wrongness", lambda c: check_silent_wrongness(c["m"])),
)


def check_all(m, root=ROOT, fonts_tsv=None, papers=None, deliverable=None, git_root=None):
    """Run every declared check. Returns (findings, checks_run).

    The paths are parameters so the red-proof can point them at a temp tree and provoke the
    registry failures for real, rather than mocking the reader and proving nothing."""
    ctx = {
        "m": m,
        "root": Path(root),
        "fonts_tsv": Path(fonts_tsv) if fonts_tsv else Path(root) / "docs/deliverable/fonts/FONTS.tsv",
        "papers": Path(papers) if papers else Path(root) / "docs/papers",
        "deliverable": Path(deliverable) if deliverable else Path(root) / "docs/deliverable",
        "git_root": Path(git_root) if git_root else Path(root),
    }
    findings = []
    for _name, fn in CHECKS:
        findings.extend(fn(ctx))
    return findings, len(CHECKS)


def run(manifest_path=MANIFEST, root=ROOT, **kw):
    m, findings = load(Path(manifest_path))
    if m is None:
        return m, findings, 0
    more, ran = check_all(m, root=root, **kw)
    return m, findings + more, ran


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="machine-readable report")
    ap.add_argument("--manifest", default=str(MANIFEST))
    args = ap.parse_args(argv)

    m, findings, ran = run(Path(args.manifest))
    pages = len(m["pages"]) if isinstance(m, dict) and isinstance(m.get("pages"), list) else 0
    fonts = len(m["fonts"]) if isinstance(m, dict) and isinstance(m.get("fonts"), dict) else 0
    scripts = (len(m["manuscripts"]) if isinstance(m, dict)
               and isinstance(m.get("manuscripts"), dict) else 0)

    if args.json:
        print(json.dumps({"findings": findings, "checks_run": ran, "pages": pages,
                          "fonts": fonts, "manuscripts": scripts}, indent=2))
        return 1 if findings else 0

    print("wt179 -- LAYOUT-MANIFEST.json, held to itself (no TeX, no pandoc, no worktree)")
    print("=" * 78)
    for f in findings:
        print("  FAIL " + f)
    print("  %d page(s), %d font(s), %d manuscript(s) described." % (pages, fonts, scripts))
    print("wt179: %d checks run, %d finding(s)." % (ran, len(findings)))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
