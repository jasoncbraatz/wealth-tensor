#!/usr/bin/env python3
"""wealthTensor-97 -- the red-proof for scripts/wt179_manifest_guard.py.

A GUARD NOBODY HAS WATCHED FAIL IS A DECORATION. The manifest is correct today, so the
guard is green today, and a green over a correct file proves precisely nothing about
whether any assertion in it can bite. This file breaks the manifest twenty-five different
ways -- in memory and in temp directories, never on disk -- and requires the guard to
report each one.

EACH PROBE IS ASSERTED BY ITS TAG, NEVER BY EXIT STATUS. `-94` and `-95` both paid for
this and `-96` wrote it down: a red-proof caught by a DIFFERENT check than the one under
test proves the wrong thing and is indistinguishable from success. `-95`'s probe went red
because its ROOT broke, not because the check bit. Exit status would have passed every
probe in here for the wrong reason; the tag cannot. Each probe also asserts a CONTROL --
that the unmutated manifest does NOT emit the tag -- so a tag that fires unconditionally
is caught too.

COVERAGE IS ENUMERATED FROM THE CODE UNDER TEST. `wt179_manifest_guard.TAGS` is the
registry; this file imports it rather than scanning its source, because `-95` scanned a
guard's source for its tags, found nine of fourteen, and printed FULL COVERAGE. Held in
both directions: a declared tag no probe provokes prints WEAK, and a probe naming a tag
the guard cannot emit is an ERROR. Delete one probe below and exactly one line goes WEAK.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wt179_manifest_guard as G  # noqa: E402

ROOT = G.ROOT
RESULTS = []


def tags_of(findings):
    return {f.split(" ", 1)[0] for f in findings}


def fresh():
    """A pristine parse of the committed manifest, per probe."""
    return json.loads(Path(G.MANIFEST).read_text(encoding="utf-8"))


BASELINE_TAGS = set()


def probe(name, tag, mutate=None, **kw):
    """Break one thing, require exactly that tag, and require the control to be clean."""
    m = fresh()
    if mutate is not None:
        mutate(m)
    findings, _ran = G.check_all(m, **kw)
    got = tags_of(findings)
    fired = tag in got
    control = tag not in BASELINE_TAGS
    RESULTS.append((name, tag, fired and control, sorted(got)[:4],
                    "" if control else "CONTROL FAILED: the tag fires on the clean manifest"))
    return fired and control


def record(name, tag, ok, note=""):
    RESULTS.append((name, tag, ok, [tag] if ok else [], note))
    return ok


def main() -> int:
    print("RED-PROOF wt179 -- scripts/wt179_manifest_guard.py")
    print("=" * 78)

    # RP0: the control the whole file leans on. Every probe below asserts its tag is absent
    # here, so if this is not clean the probes are meaningless and say so.
    clean, ran = G.check_all(fresh())
    BASELINE_TAGS.update(tags_of(clean))
    record("RP0 committed manifest is clean", "OK", not clean,
           "%d checks, %d finding(s)" % (ran, len(clean)))

    # ---------------------------------------------------------------- reading the file
    with tempfile.TemporaryDirectory() as tmp:
        missing = Path(tmp) / "nope.json"
        _m, f = G.load(missing)
        record("a manifest that is not there", "MANIFEST-MISSING",
               "MANIFEST-MISSING" in tags_of(f))
        broken = Path(tmp) / "broken.json"
        broken.write_text("{ this is not json", encoding="utf-8")
        _m, f = G.load(broken)
        record("a manifest that will not parse", "MANIFEST-UNPARSEABLE",
               "MANIFEST-UNPARSEABLE" in tags_of(f))

    # ---------------------------------------------------------------- declared shape
    probe("a declared key deleted", "MISSING-KEY", lambda m: m.pop("pdf"))
    probe("a key the schema does not declare", "UNKNOWN-KEY",
          lambda m: m.__setitem__("smuggled_in_by_hand", 1))
    probe("a declared key with the wrong type", "BAD-TYPE",
          lambda m: m.__setitem__("page_count", "145"))
    probe("a nested key deleted", "MISSING-KEY", lambda m: m["pins"].pop("engine"))
    probe("a nested key the guard does not declare", "UNKNOWN-KEY",
          lambda m: m["pins"].__setitem__("shell", "zsh"))

    # ---------------------------------------------------------------- the page block
    probe("page_count no longer equals len(pages)", "PAGE-COUNT-DISAGREES",
          lambda m: m.__setitem__("page_count", m["page_count"] + 1))
    probe("a page entry grows a key", "PAGE-ENTRY-SHAPE",
          lambda m: m["pages"][7].__setitem__("note", "hand-edited"))
    probe("pages out of order", "PAGE-NUMBERING",
          lambda m: m["pages"][3].__setitem__("page", 99))
    probe("a per-page hash that is not a hash", "BAD-SHA",
          lambda m: m["pages"][0].__setitem__("sha256", "deadbeef"))
    probe("a per-page hash in upper case", "BAD-SHA",
          lambda m: m["pages"][2].__setitem__("sha256", m["pages"][2]["sha256"].upper()))
    probe("a negative char count", "BAD-CHARS",
          lambda m: m["pages"][1].__setitem__("chars", -1))
    probe("pdf_sha256 that is not a hash", "BAD-SHA",
          lambda m: m.__setitem__("pdf_sha256", "x" * 64))

    # ---------------------------------------------------------------- the font registry
    with tempfile.TemporaryDirectory() as tmp:
        probe("FONTS.tsv is not there", "FONTS-TSV-UNREADABLE",
              None, fonts_tsv=Path(tmp) / "FONTS.tsv")
        headers = Path(tmp) / "header-only.tsv"
        headers.write_text("# a comment\nfile\tpackage\tsha256\tpath\tbytes\n", encoding="utf-8")
        probe("FONTS.tsv with no data rows", "FONTS-TSV-UNREADABLE", None, fonts_tsv=headers)
    probe("a font the TSV does not carry", "FONT-NOT-IN-TSV",
          lambda m: m["fonts"].__setitem__("Comic-Sans.otf", "a" * 64))
    probe("a font the manifest dropped", "FONT-MISSING-FROM-MANIFEST",
          lambda m: m["fonts"].pop(sorted(m["fonts"])[0]))
    probe("a font whose sha moved", "FONT-SHA-DISAGREES",
          lambda m: m["fonts"].__setitem__(sorted(m["fonts"])[0], "b" * 64))

    # ---------------------------------------------------------------- the manuscripts
    probe("a manuscript that is not on disk", "MANUSCRIPT-NOT-ON-DISK",
          lambda m: m["manuscripts"].__setitem__("docs/papers/paper-V-ghost/paper-V.md",
                                                 "c" * 64))
    probe("a manuscript on disk the manifest forgot", "MANUSCRIPT-MISSING-FROM-MANIFEST",
          lambda m: m["manuscripts"].pop(sorted(m["manuscripts"])[0]))

    # ---------------------------------------------------------------- the capture commit
    probe("source_commit that is not a sha", "BAD-COMMIT-SHA",
          lambda m: m.__setitem__("source_commit", "HEAD~1"))
    probe("a short sha that is not a prefix", "COMMIT-SHORT-DISAGREES",
          lambda m: m.__setitem__("source_commit_short", "ffffffffffff"))
    probe("a commit this clone has never seen", "COMMIT-MISSING",
          lambda m: (m.__setitem__("source_commit", "f" * 40),
                     m.__setitem__("source_commit_short", "f" * 12)))
    probe("a capture date the commit does not carry", "COMMIT-DATE-DISAGREES",
          lambda m: m.__setitem__("commit_date", "1999-01-01"))

    # GIT-UNAVAILABLE: provoked for real by taking git off PATH, not by mocking the reader.
    # A guard that silently skips the commit checks when git is absent would report green
    # on a machine that verified nothing; this proves it goes red instead.
    old_path = os.environ.get("PATH", "")
    os.environ["PATH"] = ""
    try:
        probe("git is not on the PATH", "GIT-UNAVAILABLE")
    finally:
        os.environ["PATH"] = old_path

    # ---------------------------------------------------------------- the deliverable
    with tempfile.TemporaryDirectory() as tmp:
        probe("the captured PDF is gone", "PDF-MISSING", None, deliverable=tmp)
        (Path(tmp) / "wealth-tensor-capture.pdf").write_bytes(b"%PDF-1.7 not the deliverable")
        probe("a PDF whose bytes are not the ones described", "PDF-SHA-DISAGREES",
              None, deliverable=tmp)

    # ---------------------------------------------------------------- the build assertions
    probe("an overfull box the build calls fatal", "SILENT-WRONGNESS-NONZERO",
          lambda m: m["silent_wrongness"].__setitem__("overfull_hboxes", 3))
    probe("a missing character the build calls fatal", "SILENT-WRONGNESS-NONZERO",
          lambda m: m["silent_wrongness"].__setitem__("missing_characters", 1))

    # UNREGISTERED-TAG is enforced inside _tag() itself, so it is probed directly.
    msg = G._tag("NOT-A-REAL-TAG", "hello")
    record("an undeclared tag cannot escape", "UNREGISTERED-TAG",
           msg.startswith("UNREGISTERED-TAG"), msg[:60])

    # ---------------------------------------------------------------- report
    print("\nPROBES:")
    failures = 0
    for name, tag, ok, got, note in RESULTS:
        print("  %-4s %-44s %-32s %s"
              % ("PASS" if ok else "FAIL", name, tag, note or ("saw " + ",".join(got))))
        if not ok:
            failures += 1

    print("\nCOVERAGE (enumerated from wt179_manifest_guard.TAGS, not scraped from it):")
    probed = {t for _n, t, ok, _g, _x in RESULTS if ok} - {"OK"}
    stray = {t for _n, t, _ok, _g, _x in RESULTS} - set(G.TAGS) - {"OK"}
    for t in sorted(stray):
        print("  ERROR   probe claims tag %r, which TAGS does not declare" % t)
        failures += 1
    for t in sorted(set(G.TAGS) - probed):
        print("  WEAK    %-32s declared by TAGS and proven by no probe" % t)
        failures += 1
    print("  %d of %d declared tags proven by a probe."
          % (len(set(G.TAGS) & probed), len(G.TAGS)))

    print("\n%s -- %d probe(s), %d failure(s)."
          % ("RED-PROOF PASSED" if failures == 0 else "RED-PROOF FAILED",
             len(RESULTS), failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
