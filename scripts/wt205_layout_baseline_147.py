#!/usr/bin/env python3
"""wt205 — the layout baseline moved 145 -> 147 pages, so every place that ASSERTS 145
has to move with it or it is a false statement about the current PDF.

Pass B added prose to all three manuscripts; two pages is what that cost.  The capture
was rebuilt (0 overfull boxes, 0 missing characters) and `verify-layout.sh` reproduces at
147 from a clean worktree of 1e1e2a5.  The 145s below are the ones that CLAIM something
about the PDF as it stands.  The one at HANDOFF `drift_flags` RP1a (`141 pages against
145`) is a RECORD OF A PAST RED-PROOF RUN and is deliberately left alone -- rewriting
history to match the present is how a ledger stops being evidence.

Idempotent: NO-OP on a second run, exit 0.
"""
import sys, pathlib

R = pathlib.Path.home() / "repos/wealth-tensor"

EDITS = [
    ("tests/test_layout_manifest_is_self_consistent.py",
     "`docs/deliverable/LAYOUT-MANIFEST.json` carries P13e's entire claim -- 145 pages, their",
     "`docs/deliverable/LAYOUT-MANIFEST.json` carries P13e's entire claim -- 147 pages, their"),
    ("tests/test_layout_manifest_is_self_consistent.py",
     'assert (report["pages"], report["fonts"], report["manuscripts"]) == (145, 16, 4)',
     'assert (report["pages"], report["fonts"], report["manuscripts"]) == (147, 16, 4)'),
    ("docs/HANDOFF.md", "    count: 145", "    count: 147"),
    ("docs/HANDOFF.md", "zero image XObjects in the 145-page PDF", "zero image XObjects in the 147-page PDF"),
]

def main() -> int:
    rc, bufs = 0, {}
    for rel, old, new in EDITS:
        p = R / rel
        t = bufs.get(rel) or p.read_text(encoding="utf-8")
        if old in t:
            if t.count(old) != 1:
                print(f"{rel}: anchor not unique ({t.count(old)}x)"); return 2
            bufs[rel] = t.replace(old, new); print(f"APPLIED  {rel}: {old.strip()[:60]}")
        elif new in t:
            bufs[rel] = t; print(f"NO-OP    {rel}: already 147")
        else:
            print(f"NOT FOUND {rel}: {old.strip()[:60]}"); rc = 2
    if rc: return rc
    for rel, t in bufs.items():
        p = R / rel
        if p.read_text(encoding="utf-8") != t:
            p.write_text(t, encoding="utf-8"); print("wrote", rel)
    return 0

sys.exit(main())
