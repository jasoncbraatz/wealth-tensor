#!/usr/bin/env python3
"""wt212 — move the reviewed layout baseline 149 -> 144, in the same commit as the rebuild.

DoD § 4.1 asks for "layout verified at whatever the new page count is". Pass D removed 149
C-class sites -- a 556-word session log at the foot of paper-III's references, fifteen hard
apparatus leaks, and a hundred and thirty clauses of scaffolding voice -- and the corpus
lost FIVE PAGES with it. Nothing was added; the count fell because the seams were prose.

The baseline is a REVIEWED number and this is the review: 144 pages, 0 overfull boxes, 0
missing characters, all 144 per-page text hashes reproducing from a clean worktree, and every
page clearing all four edges by at least 18bp. Idempotent; exit 2 if it matches neither state.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
T = ROOT / "tests/test_layout_manifest_is_self_consistent.py"
OLD = '''    # wealthTensor-104 (Pass B), 147 -> 148 at wealthTensor-105 (Pass C's 24 structural
    # repairs), 148 -> 149 in the same session when its own verification pass repaired
    # ten defects in those repairs. The fonts and manuscripts should not drift quietly.
    assert (report["pages"], report["fonts"], report["manuscripts"]) == (149, 16, 4)'''
NEW = '''    # wealthTensor-104 (Pass B), 147 -> 148 at wealthTensor-105 (Pass C's 24 structural
    # repairs), 148 -> 149 in the same session when its own verification pass repaired
    # ten defects in those repairs, and 149 -> 144 at wealthTensor-106 (Pass D's 149 C-class
    # repairs). PASS D IS THE FIRST PASS TO MOVE THIS NUMBER DOWN, and that is the expected
    # direction for a coherence pass: nothing was added, and the corpus lost five pages of
    # scaffolding -- a 556-word session log at the foot of paper-III's references, fifteen
    # hard apparatus leaks, and a hundred and thirty clauses of process narration.
    # The fonts and manuscripts should not drift quietly.
    assert (report["pages"], report["fonts"], report["manuscripts"]) == (144, 16, 4)'''

def main():
    s = T.read_text(encoding="utf-8")
    if OLD in s and NEW not in s:
        bak = T.with_suffix(".py.bak-wt212")
        if not bak.exists(): bak.write_text(s, encoding="utf-8")
        T.write_text(s.replace(OLD, NEW, 1), encoding="utf-8")
        print("APPLIED: layout baseline 149 -> 144"); return 0
    if NEW in s and OLD not in s:
        print("ALREADY-APPLIED: baseline already reads 144"); return 0
    print("FAIL: the baseline block matches neither state"); return 2

if __name__ == "__main__":
    sys.exit(main())
