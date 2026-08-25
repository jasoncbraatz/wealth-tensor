#!/usr/bin/env python3
"""wt214 — the two reviewed numbers the section 4.4 note moved, both in this commit.

1. LAYOUT BASELINE 144 -> 145.  wt212 moved it 149 -> 144 when Pass D's C-class repairs took
   five pages of scaffolding out.  The section 4.4 known-limitations note then put one page
   back, deliberately, and this is that page.  Reviewed: 145 pages, 0 overfull boxes, 0 missing
   characters, every page clearing all four edges by at least 18bp.

2. RECIPE.md's MEASURED characters-per-line 65.43 -> 64.95, AT BOTH SITES.  wt173 --verify
   checks the prose step AND the data block, and -105's trap is that --measure moves only the
   JSON: "RECIPE.md carries the value TWICE and --verify checks both."  64.95 is inside section
   0's 62-68 band, so NOTHING IS RETUNED and the band is not widened -- the band is the design
   and the measurement is the outcome.

Idempotent; exit 2 if a site matches neither state.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

EDITS = [
("layout-baseline-145", "tests/test_layout_manifest_is_self_consistent.py",
 'assert (report["pages"], report["fonts"], report["manuscripts"]) == (144, 16, 4)',
 'assert (report["pages"], report["fonts"], report["manuscripts"]) == (145, 16, 4)'),
("baseline-note", "tests/test_layout_manifest_is_self_consistent.py",
 "    # hard apparatus leaks, and a hundred and thirty clauses of process narration.\n    # The fonts and manuscripts should not drift quietly.",
 "    # hard apparatus leaks, and a hundred and thirty clauses of process narration. 144 -> 145\n"
 "    # in the same session when the section 4.4 known-limitations note was added to each paper,\n"
 "    # which is the only prose Pass D ADDED and the only page it put back.\n"
 "    # The fonts and manuscripts should not drift quietly."),
("recipe-prose", "docs/deliverable/RECIPE.md",
 "   **65.43** characters per line — inside the 62–68 band of §0.",
 "   **64.95** characters per line — inside the 62–68 band of §0."),
("recipe-data", "docs/deliverable/RECIPE.md",
 "body.chars_per_line\t65.43\t",
 "body.chars_per_line\t64.95\t"),
]

def main():
    applied = already = 0; fail = []; new = {}
    for tag, rel, old, repl in EDITS:
        p = ROOT / rel
        t = new.get(rel) or p.read_text(encoding="utf-8")
        if t.count(old) == 1 and t.count(repl) == 0:
            new[rel] = t.replace(old, repl, 1); applied += 1; print("APPLIED         %s" % tag)
        elif t.count(old) == 0 and t.count(repl) == 1:
            new[rel] = t; already += 1; print("ALREADY-APPLIED %s" % tag)
        else:
            new[rel] = t; fail.append(tag)
            print("!! NEITHER      %s  old=%d new=%d" % (tag, t.count(old), t.count(repl)))
    if fail:
        print("\nFAIL: %d site(s); NOTHING WRITTEN" % len(fail)); return 2
    for rel, t in new.items():
        p = ROOT / rel
        if p.read_text(encoding="utf-8") != t:
            bak = p.with_suffix(p.suffix + ".bak-wt214")
            if not bak.exists(): bak.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
            p.write_text(t, encoding="utf-8"); print("WROTE %s" % rel)
    print("\napplied=%d already=%d" % (applied, already)); return 0

if __name__ == "__main__":
    sys.exit(main())
