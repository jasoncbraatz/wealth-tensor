#!/usr/bin/env python3
"""wealthTensor-65 · `G16` — the probe that proves the widening bought coverage.

`G11` writes an uninstrumented SHA into paper III and is caught. That was true before this
session and stays true after it, so `G11` alone cannot tell you whether widening
`test_manuscript_shas_are_instrumented.py` to a glob did anything at all.

`G16` makes the identical forbidden move in **paper I** — a manuscript the old instrument
could not see, because its subject was a constant. Run against `-64`'s tree it comes back
GREEN, and the green means *the guard is blind here*; run against this commit it comes back
RED. That difference is the measurement, and it is the only evidence that separates a class
repair from a repair of one instance wearing the word "class".

`G11`'s body is extracted rather than copied — a probe harness carrying two copies of its
own forbidden move is the `PIN-001` shape arriving in the harness. Its docstring, which is
load-bearing history about why the SHA may not be named here, stays where it is.
"""
from __future__ import annotations

import pathlib
import shutil
import sys

DRY = "--dry" in sys.argv
ROOT = pathlib.Path(__file__).resolve().parents[1]
MC = "scripts/mutation_control.py"

OLD_BODY = '''    text = (root / MS).read_text()
    instruments = "\\n".join(
        q.read_text(encoding="utf-8", errors="ignore")
        for d in ("scripts", "tests", "src")
        for q in sorted((root / d).rglob("*.py"))
    )
    picked = None
    for line in subprocess.run(
            ["git", "log", "--format=%h", "-60"], cwd=str(root),
            capture_output=True, text=True).stdout.split():
        if (len(line) >= 7 and any(c.isdigit() for c in line)
                and any(c in "abcdef" for c in line)
                and line not in instruments and line not in text):
            picked = line
            break
    if picked is None:
        raise SystemExit("PROBE SITE MISSING: no commit is absent from every instrument")
    i = text.find("\\n## ", len(text) // 2)
    if i < 0:
        raise SystemExit("PROBE SITE MISSING: no mid-document heading in the manuscript")
    claim = f"\\n\\nThe analysis in this section was produced at commit {picked}.\\n"
    (root / MS).write_text(text[:i] + claim + text[i:])
'''

NEW_BODY = '''    _orphan_sha_in(root, MS)


def _orphan_sha_in(root: Path, rel: str):
    """`G11`'s forbidden move, aimed at whichever manuscript is named.

    Extracted by `-65` so `G16` can make the identical move in a different paper without
    the harness carrying two copies of it — which would be the PIN-001 shape arriving in
    the instrument that probes for the PIN-001 shape.
    """
    text = (root / rel).read_text()
    instruments = "\\n".join(
        q.read_text(encoding="utf-8", errors="ignore")
        for d in ("scripts", "tests", "src")
        for q in sorted((root / d).rglob("*.py"))
    )
    picked = None
    for line in subprocess.run(
            ["git", "log", "--format=%h", "-60"], cwd=str(root),
            capture_output=True, text=True).stdout.split():
        if (len(line) >= 7 and any(c.isdigit() for c in line)
                and any(c in "abcdef" for c in line)
                and line not in instruments and line not in text):
            picked = line
            break
    if picked is None:
        raise SystemExit("PROBE SITE MISSING: no commit is absent from every instrument")
    i = text.find("\\n## ", len(text) // 2)
    if i < 0:
        raise SystemExit(f"PROBE SITE MISSING: no mid-document heading in {rel}")
    claim = f"\\n\\nThe analysis in this section was produced at commit {picked}.\\n"
    (root / rel).write_text(text[:i] + claim + text[i:])


def _orphan_sha_in_paper_i(root: Path):
    """G16 - the same move as G11, in a manuscript the OLD instrument could not see.

    `test_manuscript_shas_are_instrumented.py` hardcoded paper III until `-65`. Its own
    docstring said it repaired the CLASS; it touched one file of four, and `-64` found the
    shape alive in paper IV. Against a tree where that instrument is still a constant this
    probe is GREEN, and the green is the finding. Against this commit it is RED.

    Paper I is chosen deliberately: it is the manuscript that pins NOTHING today, so a
    catcher here cannot be an accident of some other guard already watching its SHAs.
    """
    _orphan_sha_in(root, PAPER_I)
'''

EDITS = [
    (MC, "PAPER_I path constant",
     'GUARD = "tests/test_reg012_sec6_sec47_frozen.py"\n',
     'GUARD = "tests/test_reg012_sec6_sec47_frozen.py"\n'
     'PAPER_I = "docs/papers/paper-I-price-formation/paper-I.md"\n'),

    (MC, "extract G11's body, add G16's mover", OLD_BODY, NEW_BODY),

    (MC, "G16 probe row",
     '     _repin_the_registration_anchor, {"git": True}),\n]',
     '     _repin_the_registration_anchor, {"git": True}),\n'
     '    ("G16", "write an uninstrumented commit SHA into PAPER I — the move G11 makes in "\n'
     '            "paper III, aimed where the instrument was blind until -65 [git]",\n'
     '     _orphan_sha_in_paper_i, {"git": True}),\n]'),
]


def main() -> int:
    src = {}
    for rel, label, old, new in EDITS:
        p = ROOT / rel
        if rel not in src:
            src[rel] = p.read_text(encoding="utf-8")
        n = src[rel].count(old)
        if n != 1:
            print(f"ABORT · anchor not unique ({n}x) · {rel} · {label}")
            return 1
        src[rel] = src[rel].replace(old, new, 1)
        print(f"ok  {rel:32s}  {label}")

    for rel, text in src.items():
        p = ROOT / rel
        if DRY:
            out = p.with_suffix(p.suffix + ".wt65-dryrun")
            out.write_text(text, encoding="utf-8")
            print(f"DRY  wrote {out}")
        else:
            shutil.copy2(p, p.with_suffix(p.suffix + ".bak-wt65-g16"))
            p.write_text(text, encoding="utf-8")
            print(f"WROTE {rel}  (.bak-wt65-g16 kept)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
